"""v12_final 에서 Path 15행만 v11 원본으로 롤백.

실측 결과: v11 Path(LLM 기반) 는 0.12 점수 기여, v12 Path(BFS) 는 0점 기여.
Topology + Fault 개선은 유지하되 Path 만 v11 답으로 되돌린다.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _THIS_DIR.parent.parent.parent
_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_V11_CSV = _THIS_DIR / "submission_v6_full_v11.csv"
_V12_FINAL = _THIS_DIR / "submission_v12_final.csv"
_OUT_CSV = _THIS_DIR / "submission_v12_topo_fault.csv"

_PATH_QNUMS: set[int] = set(range(7, 17)) | set(range(34, 39))


def _load_rows(csv_path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or ["ID", "Track A", "Track B"])
        rows = [dict(row) for row in reader]
    return fieldnames, rows


def _load_path_sid_set() -> set[str]:
    with open(_TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {
        item["scenario_id"]
        for item in data
        if item["task"]["id"] in _PATH_QNUMS
    }


def main() -> None:
    print("v12_final → Path 15행만 v11 로 롤백")

    path_sids = _load_path_sid_set()
    print(f"  Path scenario_id: {len(path_sids)} 개")

    v11_fields, v11_rows = _load_rows(_V11_CSV)
    v12_fields, v12_rows = _load_rows(_V12_FINAL)

    # v11 의 Path 답 dict
    v11_path: dict[str, str] = {
        r["ID"]: r.get("Track B", "")
        for r in v11_rows
        if r.get("ID") in path_sids
    }

    # v12_final 복사 후 Path 15행만 v11 답으로 교체
    replaced = 0
    for row in v12_rows:
        sid = row.get("ID", "")
        if sid in path_sids and sid in v11_path:
            row["Track B"] = v11_path[sid]
            replaced += 1

    print(f"  Path 롤백: {replaced}/15 행")

    with open(_OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=v12_fields)
        writer.writeheader()
        writer.writerows(v12_rows)
    print(f"  저장: {_OUT_CSV}")


if __name__ == "__main__":
    main()
