"""Topology 11문제 deterministic 파서 결과로 submission_v12_topo.csv 생성.

1. solve_all_topology() 로 Q1~Q6, Q29~Q33 답변 생성
2. 기존 submission_v6_full_v11.csv 로드
3. Topology 11행만 새 답으로 교체
4. submission_v12_topo.csv 저장 (v11 절대 덮어쓰지 않음)
5. 콘솔에 각 Q 요약 출력
6. 환각 alias 검사
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

# topology_parser 임포트
_THIS_DIR = Path(__file__).resolve().parent
_TRACK_B_DIR = _THIS_DIR.parent
sys.path.insert(0, str(_TRACK_B_DIR))

from topology_parser import check_hallucination, solve_all_topology

# ---------------------------------------------------------------------------
# 경로 상수
# ---------------------------------------------------------------------------

_PROJECT_ROOT = _TRACK_B_DIR.parent.parent
_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_V11_CSV = _THIS_DIR / "submission_v6_full_v11.csv"
_V12_CSV = _THIS_DIR / "submission_v12_topo.csv"

# Topology 질문 번호 (1-indexed, test.json 순서)
_TOPOLOGY_QNUMS = {1, 2, 3, 4, 5, 6, 29, 30, 31, 32, 33}

# 환각 패턴 (submission CSV 검사용)
_HALL_PAT = re.compile(r"\b(Spine[12]?|PC[0-9]|Core-[0-9])\b", re.IGNORECASE)


def _load_scenario_id_map() -> dict[int, str]:
    """qnum(1-indexed) -> scenario_id 매핑 로드."""
    with open(_TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {i + 1: item["scenario_id"] for i, item in enumerate(data)}


def _load_v11_rows() -> tuple[list[str], list[dict[str, str]]]:
    """v11 CSV 에서 헤더와 행 목록 반환 (BOM 처리)."""
    rows: list[dict[str, str]] = []
    with open(_V11_CSV, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or ["ID", "Track A", "Track B"]
        for row in reader:
            rows.append(dict(row))
    return list(fieldnames), rows


def _newline_escape(text: str) -> str:
    """답변의 줄바꿈을 CSV 셀 내 '\\n' 리터럴로 변환."""
    return text.replace("\n", "\\n")


def main() -> None:
    print("=" * 70)
    print("gen_v12_topo.py — Topology 11문제 deterministic 파서 결과 적용")
    print("=" * 70)

    # 1. 답변 생성
    print("\n[Step 1] solve_all_topology() 실행...")
    topo_results = solve_all_topology()

    # 2. scenario_id 매핑 로드
    print("[Step 2] test.json scenario_id 매핑 로드...")
    qnum_to_sid = _load_scenario_id_map()
    sid_to_qnum: dict[str, int] = {
        sid: qnum
        for qnum, sid in qnum_to_sid.items()
        if qnum in _TOPOLOGY_QNUMS
    }

    # 3. v11 CSV 로드
    print("[Step 3] v11 CSV 로드...")
    fieldnames, rows = _load_v11_rows()

    # 4. 교체
    print("[Step 4] Topology 11행 답변 교체...")
    replaced_count = 0
    for row in rows:
        sid = row["ID"]
        if sid not in sid_to_qnum:
            continue
        qnum = sid_to_qnum[sid]
        result = topo_results[qnum]
        row["Track B"] = _newline_escape(result["answer"])
        replaced_count += 1

    print(f"  교체 완료: {replaced_count}행")

    # 5. v12 CSV 저장
    print(f"[Step 5] {_V12_CSV.name} 저장...")
    with open(_V12_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  저장 완료: {_V12_CSV}")

    # 6. 콘솔 요약
    print("\n" + "=" * 70)
    print("결과 요약")
    print("=" * 70)
    print(f"{'Q':>3}  {'target':25s}  {'C'}  {'res':>3}/{'tot':>3}  {'method'}")
    print("-" * 70)
    for qnum in sorted(topo_results.keys()):
        r = topo_results[qnum]
        hall = check_hallucination(r["answer"])
        hall_str = f" *** 환각: {hall}" if hall else ""
        print(
            f"Q{qnum:>2d}  {r['target']:25s}  {r['confidence']}  "
            f"{r['resolved_ports']:>3}/{r['total_up_ports']:>3}  {r['method']}"
            f"{hall_str}"
        )
        # 답변 앞 100자
        first_line = r["answer"].split("\n")[0] if r["answer"] else "(빈 답변)"
        print(f"      {first_line[:100]}")

    # 7. 환각 검사 (CSV 전체)
    print("\n[Step 7] 환각 alias 검사...")
    hall_count = 0
    with open(_V12_CSV, encoding="utf-8") as f:
        content = f.read()
    matches = _HALL_PAT.findall(content)
    if matches:
        print(f"  [WARN] 환각 alias 검출: {set(matches)}")
        hall_count = len(matches)
    else:
        print("  환각 alias 0건 OK")

    print("\n완료.")
    if hall_count:
        sys.exit(1)


if __name__ == "__main__":
    main()
