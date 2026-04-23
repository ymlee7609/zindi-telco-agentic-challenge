"""Path 15문제(Q7~Q16, Q34~Q38) deterministic 경로 추적 결과로 submission CSV 생성.

1. solve_all_paths() 로 Q7~Q16, Q34~Q38 경로 생성 (underlay BFS)
2. 기존 submission_v12_topo.csv 로드
3. Path 15행 답변 교체
4. submission_v12_det_full.csv 저장 (underlay BFS 기본)
5. 콘솔 요약 및 환각 검사

두 CSV 모두 Zindi 업로드로 점수 비교 가능 (Phase 1 unlimited).
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

# path_tracer 임포트
_THIS_DIR = Path(__file__).resolve().parent
_TRACK_B_DIR = _THIS_DIR.parent
_PROJECT_ROOT = _TRACK_B_DIR.parent.parent
sys.path.insert(0, str(_TRACK_B_DIR))

from path_tracer import solve_all_paths, _PATH_QIDS  # noqa: E402

# ---------------------------------------------------------------------------
# 경로 상수
# ---------------------------------------------------------------------------

_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_BASE_CSV = _THIS_DIR / "submission_v12_topo.csv"  # 이전 단계 결과 (base)
_OUT_CSV = _THIS_DIR / "submission_v12_det_full.csv"

# Path 질문 번호 (1-indexed, test.json 순서)
_PATH_QNUMS: set[int] = set(_PATH_QIDS)

# 환각 패턴
_HALL_PAT = re.compile(r"\b(Spine[12]?|PC[0-9]|Core-[0-9]|Node-10|Node-1[1-9])\b", re.IGNORECASE)


def _load_scenario_id_map() -> dict[int, str]:
    """qnum(1-indexed) -> scenario_id 매핑 로드."""
    with open(_TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {item["task"]["id"]: item["scenario_id"] for item in data}


def _load_base_rows() -> tuple[list[str], list[dict[str, str]]]:
    """base CSV 에서 헤더와 행 목록 반환."""
    with open(_BASE_CSV, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or ["ID", "Track A", "Track B"])
        rows = [dict(row) for row in reader]
    return fieldnames, rows


def main() -> None:
    print("=" * 70)
    print("gen_v12_path.py — Path 15문제 deterministic BFS 경로 적용")
    print("=" * 70)

    # Step 1: 경로 생성
    print("\n[Step 1] solve_all_paths() 실행...")
    path_results = solve_all_paths()

    # Step 2: scenario_id 매핑
    print("[Step 2] test.json scenario_id 매핑 로드...")
    qid_to_sid = _load_scenario_id_map()
    sid_to_qid: dict[str, int] = {
        sid: qid
        for qid, sid in qid_to_sid.items()
        if qid in _PATH_QNUMS
    }

    # Step 3: base CSV 로드
    print(f"[Step 3] base CSV 로드: {_BASE_CSV.name}")
    fieldnames, rows = _load_base_rows()

    # Step 4: 교체 (underlay BFS)
    print("[Step 4] Path 15행 답변 교체...")
    replaced = 0
    for row in rows:
        sid = row["ID"]
        if sid not in sid_to_qid:
            continue
        qid = sid_to_qid[sid]
        result = path_results.get(qid, {})
        answer = result.get("answer", "")
        if answer:
            row["Track B"] = answer
            replaced += 1

    print(f"  교체 완료: {replaced}행")

    # Step 5: CSV 저장 (underlay BFS)
    print(f"[Step 5] {_OUT_CSV.name} 저장...")
    with open(_OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  저장 완료: {_OUT_CSV}")

    # Step 6: 콘솔 요약
    print("\n" + "=" * 70)
    print("경로 결과 요약")
    print("=" * 70)
    print(f"{'Q':>3}  {'C'}  {'src':20s}  {'dst/dst_ip':20s}  {'answer'}")
    print("-" * 70)
    for qid in sorted(path_results.keys()):
        r = path_results[qid]
        answer = r.get("answer", "")
        conf = r.get("confidence", "?")
        src = r.get("src", "")
        dst = r.get("dst", "") or r.get("dst_ip", "")
        hops = len(answer.split("->")) if answer else 0
        print(f"Q{qid:>2d}  {conf}  {src:20s}  {dst:20s}  hops={hops}")
        if answer:
            print(f"       {answer[:90]}")
        else:
            print(f"       (경로 없음)")

    # Step 7: 환각 검사
    print("\n[Step 7] 환각 alias 검사...")
    with open(_OUT_CSV, encoding="utf-8") as f:
        content = f.read()
    matches = _HALL_PAT.findall(content)
    if matches:
        print(f"  [WARN] 환각 alias 검출: {set(matches)}")
    else:
        print("  환각 alias 0건 OK")

    # Step 8: 포맷 검증 (공백 없음, -> 구분)
    print("\n[Step 8] 포맷 검증...")
    fmt_errors = 0
    for qid, r in path_results.items():
        answer = r.get("answer", "")
        if not answer:
            continue
        if " " in answer:
            print(f"  [WARN] Q{qid}: 공백 포함 -> {answer[:50]}")
            fmt_errors += 1
        if not answer.replace("->", "").replace("-", "").replace("_", "").isalnum():
            pass  # 노드 이름에 하이픈 포함 허용
    if fmt_errors == 0:
        print("  포맷 검증 통과 (공백 없음, -> 구분)")

    print("\n완료.")


if __name__ == "__main__":
    main()
