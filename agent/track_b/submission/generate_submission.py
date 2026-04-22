#!/usr/bin/env python3
"""Generate Zindi submission CSV matching the official submission_example.csv schema.

Schema: ID, Track A, Track B  (header row + 550 scenario rows)
- Track A rows (id not in our Track B set): leave Track A/B blank (we don't participate in Track A)
- Track B rows (scenario_id matching Track B test.json): fill Track B only; leave Track A blank

Usage:
    python generate_submission.py \\
        --results agent/results_v6_full/result.csv \\
        --override agent/results_v6_retry3/result.csv \\
        --out agent/submission/submission_latest.csv

Multiple --override files may be passed; later overrides win for a given id.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
TEST_JSON = ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
EXAMPLE = ROOT / "agent" / "common" / "submission_example.csv"

# common/submission/merge_submission.py 를 import 하여 combined CSV 자동 갱신
sys.path.insert(0, str(ROOT / "agent" / "common" / "submission"))
from merge_submission import update_track  # noqa: E402


def load_id_to_scenario() -> dict[int, str]:
    with open(TEST_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {item["task"]["id"]: item["scenario_id"] for item in data}


def flatten_newlines(text: str) -> str:
    """Convert actual newline chars to literal '\\n' (2 chars) so each CSV cell
    stays on a single physical line. Required because Zindi's parser does not
    support quoted fields containing newlines (error: 'Unclosed quoted field')."""
    if text is None:
        return ""
    return text.replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")


def load_predictions(path: Path) -> dict[int, str]:
    preds: dict[int, str] = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            try:
                qid = int(row["id"])
            except (KeyError, ValueError):
                continue
            preds[qid] = flatten_newlines(row.get("prediction", ""))
    return preds


def build_submission(pred_files: list[Path], out_path: Path,
                     update_combined: bool = True) -> None:
    id_to_sid = load_id_to_scenario()

    merged: dict[int, str] = {}
    for p in pred_files:
        merged.update(load_predictions(p))

    sid_to_pred = {id_to_sid[i]: v for i, v in merged.items() if i in id_to_sid}

    with open(EXAMPLE, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    if header != ["ID", "Track A", "Track B"]:
        raise SystemExit(f"Unexpected example header: {header}")

    filled = 0
    body = []
    for r in rows[1:]:
        if not r:
            continue
        sid = r[0]
        track_a = ""
        track_b = ""
        if sid in sid_to_pred:
            track_b = sid_to_pred[sid]
            filled += 1
        body.append([sid, track_a, track_b])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)

    print(f"Wrote {out_path}")
    print(f"Rows: {len(body)}, Track B filled: {filled}")

    if update_combined:
        # common/submission/submission_combined.csv 의 Track B 열 갱신
        update_track("B", sid_to_pred, verbose=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Zindi submission CSV")
    ap.add_argument("--results", required=True, type=Path,
                    help="Base result.csv (id,prediction)")
    ap.add_argument("--override", action="append", default=[], type=Path,
                    help="Additional result.csv files to override base (order matters)")
    ap.add_argument("--out", required=True, type=Path,
                    help="Output submission CSV path")
    ap.add_argument("--skip-combined", action="store_true",
                    help="Skip updating agent/common/submission/submission_combined.csv")
    args = ap.parse_args()

    files = [args.results, *args.override]
    build_submission(files, args.out, update_combined=not args.skip_combined)


if __name__ == "__main__":
    main()
