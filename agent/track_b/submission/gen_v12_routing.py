"""v12 Topology + Fault + Routing-trace Path 통합 CSV 생성.

- Topology: gen_v12_topo.py 결과 유지
- Fault: gen_v12_fault.py 결과 유지
- Path: routing-table hop-by-hop (solve_all_paths_by_routing) 사용
  (BFS 버전은 0.12 역효과 확인)
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_TRACK_B_DIR = _THIS_DIR.parent
_PROJECT_ROOT = _TRACK_B_DIR.parent.parent
sys.path.insert(0, str(_TRACK_B_DIR))

from path_tracer import solve_all_paths_by_routing  # noqa: E402

_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_BASE_CSV = _THIS_DIR / "submission_v12_topo_fault.csv"  # Topo+Fault only, Path=v11
_OUT_CSV = _THIS_DIR / "submission_v12_topofault_rt.csv"

_PATH_QNUMS: set[int] = set(range(7, 17)) | set(range(34, 39))


def main() -> None:
    with open(_TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    qid_to_sid = {item["task"]["id"]: item["scenario_id"] for item in data}
    path_sid_to_qid = {
        qid_to_sid[q]: q for q in _PATH_QNUMS if q in qid_to_sid
    }

    rt = solve_all_paths_by_routing()

    with open(_BASE_CSV, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or ["ID", "Track A", "Track B"])
        rows = [dict(r) for r in reader]

    replaced = 0
    for row in rows:
        sid = row.get("ID", "")
        qid = path_sid_to_qid.get(sid)
        if qid is None:
            continue
        ans = rt.get(qid, {}).get("answer", "").strip()
        if not ans:
            continue
        row["Track B"] = ans  # Path 답은 단일 라인이므로 newline 변환 불필요
        replaced += 1

    with open(_OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Path 교체: {replaced}/15")
    print(f"저장: {_OUT_CSV}")

    # 요약
    h = sum(1 for q in _PATH_QNUMS if rt.get(q, {}).get("confidence") == "H")
    m = sum(1 for q in _PATH_QNUMS if rt.get(q, {}).get("confidence") == "M")
    l = sum(1 for q in _PATH_QNUMS if rt.get(q, {}).get("confidence") == "L")
    print(f"confidence: H={h}, M={m}, L={l}")


if __name__ == "__main__":
    main()
