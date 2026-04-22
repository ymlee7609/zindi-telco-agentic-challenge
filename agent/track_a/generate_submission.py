#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Track A Zindi submission CSV 생성기.

Track A result.csv (scenario_id, prediction) 를 Zindi submission_example.csv
스키마 (ID, Track A, Track B) 에 맞춰 Track A 열을 채움.

Usage:
    python agent/track_a/generate_submission.py \\
        --results agent/track_a/results_batch_b/result.csv \\
        --override agent/track_a/submission/overlay_patch.csv \\
        --out agent/track_a/submission/submission_v2.csv

여러 --override 인자는 나중 파일이 우선 (override base).
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "agent" / "common" / "submission_example.csv"

# common/submission/merge_submission.py 를 import 하여 combined CSV 자동 갱신
sys.path.insert(0, str(ROOT / "agent" / "common" / "submission"))
from merge_submission import update_track  # noqa: E402


def flatten_newlines(text: str | None) -> str:
    if text is None:
        return ""
    return text.replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")


def load_predictions(path: Path) -> dict[str, str]:
    preds: dict[str, str] = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            sid = row.get("scenario_id") or row.get("id")
            if not sid:
                continue
            pred = row.get("prediction", "")
            preds[sid] = flatten_newlines(pred)
    return preds


def build_submission(base: Path, overrides: list[Path], out_path: Path,
                     update_combined: bool = True) -> None:
    merged: dict[str, str] = {}
    merged.update(load_predictions(base))
    for p in overrides:
        merged.update(load_predictions(p))

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
        if sid in merged:
            track_a = merged[sid]
            filled += 1
        body.append([sid, track_a, track_b])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)

    print(f"Wrote {out_path}")
    print(f"Rows: {len(body)}, Track A filled: {filled}")

    if update_combined:
        # common/submission/submission_combined.csv 의 Track A 열 갱신
        update_track("A", merged, verbose=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, type=Path,
                    help="Base Track A result.csv (scenario_id,prediction)")
    ap.add_argument("--override", action="append", default=[], type=Path,
                    help="Override CSV(s); later wins per scenario")
    ap.add_argument("--out", required=True, type=Path,
                    help="Output Zindi submission CSV path")
    ap.add_argument("--skip-combined", action="store_true",
                    help="Skip updating agent/common/submission/submission_combined.csv")
    args = ap.parse_args()

    build_submission(args.results, args.override, args.out,
                     update_combined=not args.skip_combined)


if __name__ == "__main__":
    main()
