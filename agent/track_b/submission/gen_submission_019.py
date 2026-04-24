"""Submission 019: Topology Q31/Q32 링크 추가 delta.

Baseline: submission_018_20260423_ground_truth.csv (Zindi 0.48, 24/50)
Delta: 2개 문제만 수정 (Q31, Q32)
  - Q31 Janus-Prime-01: GE1/0/3->Aegis-Prime-02(GE1/0/2) 추가
  - Q32 Aegis-Prime-01: GE1/0/2->Janus-Prime-01(GE1/0/5) 추가

근거 (Tier 5 cross-reference):
  Q31 GE1/0/3 peer:
    - Aegis-Prime-02 자체 description: 'To-Janus-Prime-01-GE1/0/3'
    - Q31 data 내 확증됨
  Q32 GE1/0/2 peer:
    - Janus-Prime-01 description (reverse): Aegis-Prime-01(GE1/0/2)
    - Aegis-Prime-01 자체 description: 'to Janus-Prime-01-GE1/0/5'
    - 양방향 확증

포맷 규칙:
  - Multi-line 답은 literal '\\n' (백슬래시+n 2글자)
  - 링크 순서: port 오름차순 (GE1/0/0, 1, 2, 3, ...)
"""

from __future__ import annotations

import csv
from pathlib import Path

# 경로 설정
_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"
_OUTPUT = _DIR / "submission_019_20260424_topo_eth_trunk.csv"

# 수정 대상 scenario_id + 수정 후 답변
# 각 답변은 literal '\n' 으로 라인 구분, 링크는 port 오름차순 정렬
_DELTA: dict[str, str] = {
    # Q31 Janus-Prime-01: 기존 5개 + GE1/0/3 추가 → 6개
    "a346ef65-4abd-4e27-b7c6-06fc70a4f1c0": (
        r"Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)\n"
        r"Janus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)\n"
        r"Janus-Prime-01(GE1/0/2)->PX1(GE1/0/0)\n"
        r"Janus-Prime-01(GE1/0/3)->Aegis-Prime-02(GE1/0/2)\n"
        r"Janus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)\n"
        r"Janus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)"
    ),
    # Q32 Aegis-Prime-01: 기존 3개 + GE1/0/2 추가 → 4개
    "d5a0f37b-4042-4570-ba17-7677fc7ebe01": (
        r"Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)\n"
        r"Aegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)\n"
        r"Aegis-Prime-01(GE1/0/2)->Janus-Prime-01(GE1/0/5)\n"
        r"Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)"
    ),
}


def main() -> None:
    if not _BASELINE.exists():
        raise SystemExit(f"baseline not found: {_BASELINE}")

    with _BASELINE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    # ID, Track A, Track B 순서인지 확인
    if header[:3] != ["ID", "Track A", "Track B"]:
        raise SystemExit(f"unexpected header: {header}")

    changed = 0
    for row in rows[1:]:
        sid = row[0]
        if sid in _DELTA:
            old = row[2]
            row[2] = _DELTA[sid]
            changed += 1
            print(f"  [CHANGED] ID={sid[:8]}...")
            print(f"    -: {old!r}")
            print(f"    +: {row[2]!r}")
            print()

    if changed != len(_DELTA):
        raise SystemExit(f"expected {len(_DELTA)} changes, got {changed}")

    # 출력
    with _OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"Wrote {_OUTPUT} ({changed} changes, {len(rows)-1} data rows)")


if __name__ == "__main__":
    main()
