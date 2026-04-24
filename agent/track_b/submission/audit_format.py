"""Submission CSV 포맷 검증 게이트 — 제출 전 필수 통과.

Zindi Track B 정답 포맷 규칙:
  - CSV 헤더: 'ID', 'Track A', 'Track B'
  - 550 data rows
  - multi-line 답변: literal '\\n' (backslash + n 두 글자)
  - 실제 개행 문자 (LF 0x0A) 금지 (cell 내부에)
  - UTF-8 BOM 금지
  - trailing/leading 공백 금지
  - reason enum 정확 매칭 (routing/port fault)
  - topology 링크: 'Node(port)->Peer(port)' 포맷
  - path: 'A->B->C' 포맷
  - fault: 'node;target;reason' 세미콜론 2개

사용:
  python3 agent/track_b/submission/audit_format.py <submission.csv>
  exit code 0 = 통과, 1 = 실패

통과 후에만 Zindi 업로드 권장.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

# fault_analyzer 와 동일 enum (복사 아닌 import 우선)
ROUTING_FAULT_REASONS = frozenset({
    "blackhole route",
    "missing static route",
    "static route error",
    "ARP configuration error",
    "routing loop",
    "BGP configuration error",
    "OSPF configuration error",
    "loopback IP configuration conflict",
    "VXLAN configuration error",
    "L3VPN configuration error",
    "L2VPN configuration error",
    "IS-IS configuration error",
    "SRV6-Policy tunnel planning error",
})

PORT_FAULT_REASONS = frozenset({
    "shutdown",
    "interface IP error",
    "traffic congestion on port bandwidth",
    "MAC address configuration error",
    "VPN configuration missing",
    "OSPF configuration error",
    "MTU value configuration error",
})

ALL_FAULT_REASONS = ROUTING_FAULT_REASONS | PORT_FAULT_REASONS

# 포맷 regex
_TOPO_LINK = re.compile(
    r"^[A-Za-z][\w\-]*(?:-\d+)?\((?:GE|XGE|10GE|25GE|40GE|100GE|Eth-Trunk|GigabitEthernet)\S+?\)"
    r"->[A-Za-z][\w\-]*(?:-\d+)?\((?:GE|XGE|10GE|25GE|40GE|100GE|Eth-Trunk|GigabitEthernet)\S+?\)$"
)
_PATH_SEGMENT = re.compile(r"^[A-Za-z][\w\-]*(?:-\d+)?$")
_FAULT_LINE = re.compile(
    r"^[A-Za-z][\w\-]*(?:-\d+)?"
    r";"
    r"[\w\./:-]+"
    r";"
    r".+$"
)


def audit(path: Path) -> tuple[bool, list[str]]:
    """CSV 포맷 검증. 통과 여부와 오류 메시지 리스트 반환."""
    errors: list[str] = []

    if not path.exists():
        return False, [f"file not found: {path}"]

    # UTF-8 BOM 검사
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("UTF-8 BOM detected (forbidden)")

    # CSV 파싱
    try:
        with path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except UnicodeDecodeError as exc:
        return False, [f"UTF-8 decode error: {exc}"]

    # 헤더 검사
    if not rows:
        return False, ["empty CSV"]
    header = rows[0]
    expected = ["ID", "Track A", "Track B"]
    if header[:3] != expected:
        errors.append(f"unexpected header: {header[:3]} (expected {expected})")

    # 행 수 검사
    data_rows = rows[1:]
    if len(data_rows) != 550:
        errors.append(f"expected 550 data rows, got {len(data_rows)}")

    # 셀 내용 검사
    for i, row in enumerate(data_rows, start=2):  # 1-indexed + header
        if len(row) < 3:
            errors.append(f"row {i}: too few columns ({len(row)})")
            continue

        sid, _track_a, track_b = row[0], row[1], row[2]

        # ID whitespace
        if sid != sid.strip():
            errors.append(f"row {i}: ID has leading/trailing whitespace")

        # Track B 가 비어있으면 Track A 전용 행 → skip
        if not track_b:
            continue

        # Track B whitespace
        if track_b != track_b.strip():
            errors.append(f"row {i} ID={sid[:8]}: Track B has leading/trailing whitespace")

        # 실제 LF 검사 (cell 내부)
        if "\n" in track_b or "\r" in track_b:
            errors.append(f"row {i} ID={sid[:8]}: Track B contains real LF/CR (should be literal \\n)")

        # Track B 포맷별 검증
        _validate_track_b_format(i, sid, track_b, errors)

    return len(errors) == 0, errors


def _validate_track_b_format(row_num: int, sid: str, answer: str, errors: list[str]) -> None:
    """Track B 답변 포맷 검증."""
    # literal \n 으로 split
    lines = answer.split(r"\n")

    for line_idx, line in enumerate(lines):
        # trailing space 검사
        if line != line.strip():
            errors.append(
                f"row {row_num} ID={sid[:8]} line {line_idx}: "
                f"leading/trailing space: {line!r}"
            )

        # 라인 타입 판정 후 검증
        if "->" in line and ";" not in line:
            # Topology 또는 Path
            if "(" in line:
                # Topology: Node(port)->Peer(port)
                if not _TOPO_LINK.match(line):
                    # 관대한 매칭 시도
                    if "->" not in line or "(" not in line or ")" not in line:
                        errors.append(
                            f"row {row_num} ID={sid[:8]} line {line_idx}: "
                            f"invalid Topology link format: {line!r}"
                        )
            else:
                # Path: A->B->C
                segments = line.split("->")
                if len(segments) < 2:
                    errors.append(
                        f"row {row_num} ID={sid[:8]} line {line_idx}: "
                        f"invalid Path format: {line!r}"
                    )
                for seg in segments:
                    if not _PATH_SEGMENT.match(seg):
                        errors.append(
                            f"row {row_num} ID={sid[:8]} line {line_idx}: "
                            f"invalid path segment {seg!r}: {line!r}"
                        )
                        break
        elif ";" in line:
            # Fault: node;target;reason
            parts = line.split(";")
            if len(parts) != 3:
                errors.append(
                    f"row {row_num} ID={sid[:8]} line {line_idx}: "
                    f"Fault line must have exactly 2 semicolons: {line!r}"
                )
            else:
                reason = parts[2]
                if reason not in ALL_FAULT_REASONS:
                    errors.append(
                        f"row {row_num} ID={sid[:8]} line {line_idx}: "
                        f"unknown reason enum {reason!r}"
                    )


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 audit_format.py <submission.csv>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    ok, errors = audit(path)

    print(f"Auditing: {path}")
    if ok:
        print(f"  PASS (0 errors)")
        return 0
    else:
        print(f"  FAIL ({len(errors)} errors):")
        for e in errors[:30]:
            print(f"    - {e}")
        if len(errors) > 30:
            print(f"    ... and {len(errors)-30} more")
        return 1


if __name__ == "__main__":
    sys.exit(main())
