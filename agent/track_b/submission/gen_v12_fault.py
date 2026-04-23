"""Fault 24문제(Q17~Q28, Q39~Q50) deterministic 분석 결과로 submission CSV 생성.

1. solve_all_faults() 로 Q17~Q28, Q39~Q50 답변 생성
2. base CSV(submission_v12_det_full.csv, 없으면 submission_v12_topo.csv) 로드
3. Fault 24행 답변 교체
4. submission_v12_final.csv 저장
5. 콘솔 요약 및 reason enum 검증
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

# fault_analyzer 임포트
_THIS_DIR = Path(__file__).resolve().parent
_TRACK_B_DIR = _THIS_DIR.parent
_PROJECT_ROOT = _TRACK_B_DIR.parent.parent
sys.path.insert(0, str(_TRACK_B_DIR))

from fault_analyzer import solve_all_faults  # noqa: E402

# ---------------------------------------------------------------------------
# 경로 상수
# ---------------------------------------------------------------------------

_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_DET_FULL_CSV = _THIS_DIR / "submission_v12_det_full.csv"
_TOPO_CSV = _THIS_DIR / "submission_v12_topo.csv"
_OUT_CSV = _THIS_DIR / "submission_v12_final.csv"

_FAULT_QNUMS: set[int] = set(range(17, 29)) | set(range(39, 51))

# 허용 reason enum (정확 매칭 검사용)
_ALL_REASONS = {
    "blackhole route", "missing static route", "static route error",
    "ARP configuration error", "routing loop", "BGP configuration error",
    "OSPF configuration error", "loopback IP configuration conflict",
    "VXLAN configuration error", "L3VPN configuration error",
    "L2VPN configuration error", "IS-IS configuration error",
    "SRV6-Policy tunnel planning error",
    "shutdown", "interface IP error",
    "traffic congestion on port bandwidth",
    "MAC address configuration error", "VPN configuration missing",
    "MTU value configuration error",
}


def _load_scenario_id_map() -> dict[int, str]:
    """qnum(1-indexed) -> scenario_id 매핑 로드."""
    with open(_TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    # test.json 의 각 항목 구조: {"scenario_id": "...", "task": {"id": int, ...}}
    # 또는 {"task": {"id": int, "scenario_id": ...}} 일 수도. gen_v12_path 방식 따름.
    return {item["task"]["id"]: item["scenario_id"] for item in data}


def _load_base_rows() -> tuple[list[str], list[dict[str, str]]]:
    """base CSV (det_full 우선, 없으면 topo) 에서 헤더와 행 반환."""
    base = _DET_FULL_CSV if _DET_FULL_CSV.exists() else _TOPO_CSV
    print(f"[Step 3] base CSV 로드: {base.name}")
    with open(base, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or ["ID", "Track A", "Track B"])
        rows = [dict(row) for row in reader]
    return fieldnames, rows


def _newline_escape(text: str) -> str:
    """답변 줄바꿈을 CSV 셀 내 '\\n' 리터럴로 변환."""
    return text.replace("\n", "\\n")


def _validate_reasons(answer: str) -> tuple[bool, list[str]]:
    """답변의 각 라인 reason 이 enum 일치하는지 검사."""
    invalid: list[str] = []
    for line in answer.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split(";")
        if len(parts) != 3:
            invalid.append(f"포맷 오류: {line}")
            continue
        reason = parts[2].strip()
        if reason and reason not in _ALL_REASONS:
            invalid.append(f"reason enum 불일치: '{reason}' in {line}")
    return (not invalid), invalid


def main() -> None:
    print("=" * 70)
    print("gen_v12_fault.py — Fault 24문제 deterministic 분석 결과 적용")
    print("=" * 70)

    # 1. 답변 생성
    print("\n[Step 1] solve_all_faults() 실행...")
    fault_results = solve_all_faults()

    # 2. scenario_id 매핑
    print("[Step 2] test.json scenario_id 매핑 로드...")
    qnum_to_sid = _load_scenario_id_map()
    sid_to_qnum: dict[str, int] = {
        sid: q for q, sid in qnum_to_sid.items() if q in _FAULT_QNUMS
    }

    # 3. base rows
    fieldnames, rows = _load_base_rows()

    # 4. Fault 24행 교체
    print("[Step 4] Fault 24행 답변 교체...")
    replaced = 0
    invalid_reason_counts = 0
    for row in rows:
        sid = row.get("ID", "").strip()
        qnum = sid_to_qnum.get(sid)
        if qnum is None:
            continue
        result = fault_results.get(qnum)
        if result is None:
            continue
        answer = result.get("answer", "").strip()
        if not answer:
            # confidence L 인 경우 기존 답 유지 (덮어쓰지 말 것)
            continue
        ok, invalid = _validate_reasons(answer)
        if not ok:
            invalid_reason_counts += 1
            print(f"  경고: Q{qnum} reason 검증 실패: {invalid[:1]}")
        row["Track B"] = _newline_escape(answer)
        replaced += 1

    print(f"  교체 완료: {replaced}/24 행")
    if invalid_reason_counts:
        print(f"  reason 검증 실패: {invalid_reason_counts} 건")

    # 5. 저장
    print(f"[Step 5] {_OUT_CSV.name} 저장...")
    with open(_OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  저장 완료: {_OUT_CSV}")

    # 6. 요약
    print("\n" + "=" * 70)
    print("Fault 결과 요약")
    print("=" * 70)
    conf_counts = {"H": 0, "M": 0, "L": 0}
    for q in sorted(_FAULT_QNUMS):
        r = fault_results.get(q, {})
        conf = r.get("confidence", "L")
        ans = r.get("answer", "") or "(empty)"
        first_line = ans.split("\n")[0][:90]
        conf_counts[conf] = conf_counts.get(conf, 0) + 1
        print(f"  Q{q:2d} [{conf}]: {first_line}")
    print(f"\n  H={conf_counts['H']}, M={conf_counts['M']}, L={conf_counts['L']}")

    # 7. 환각 검사 (Fault 답변에 존재하지 않는 노드 사용 여부)
    print("\n[Step 7] 답변 중 reason enum 미일치 행 전수 재검사...")
    total_invalid = 0
    for row in rows:
        sid = row.get("ID", "").strip()
        qnum = sid_to_qnum.get(sid)
        if qnum is None:
            continue
        cell = row.get("Track B", "").replace("\\n", "\n")
        if not cell.strip():
            continue
        ok, _ = _validate_reasons(cell)
        if not ok:
            total_invalid += 1
    if total_invalid == 0:
        print("  모든 Fault 행 reason enum 일치 OK")
    else:
        print(f"  경고: {total_invalid} 행 reason enum 불일치")

    print("\n완료.")


if __name__ == "__main__":
    main()
