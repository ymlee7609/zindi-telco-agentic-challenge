#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zindi 통합 submission (Track A + Track B) 관리기.

Zindi 최종 제출은 `ID, Track A, Track B` 3-column CSV 단일 파일.
Track A (500 행) 와 Track B (50 행) 을 하나의 파일에서 유지하기 위해,
각 Track 의 `generate_submission.py` 실행 시 본 모듈의 `update_track()` 을 호출하여
`agent/common/submission/submission_combined.csv` 의 해당 열만 갱신.

사용 예:
    from merge_submission import update_track
    update_track('A', {sid: 'C9', ...})
    update_track('B', {sid: 'Hermes-Node-01->...', ...})

CLI 직접 호출:
    python merge_submission.py --track A --results agent/track_a/results_batch_b/result.csv
    python merge_submission.py --status                 # 현재 combined 상태 요약
    python merge_submission.py --reset                  # submission_example 로 초기화
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Literal


ROOT = Path(__file__).resolve().parents[3]
EXAMPLE = ROOT / "agent" / "common" / "submission_example.csv"
COMBINED = ROOT / "agent" / "common" / "submission" / "submission_combined.csv"
HEADER = ["ID", "Track A", "Track B"]


def _load_example_order() -> list[str]:
    """submission_example.csv 의 scenario_id 순서를 보존."""
    if not EXAMPLE.exists():
        raise SystemExit(f"submission_example.csv 누락: {EXAMPLE}")
    with EXAMPLE.open(encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    if header != HEADER:
        raise SystemExit(f"예상과 다른 example 헤더: {header}")
    return [r[0] for r in rows[1:] if r]


def read_combined() -> dict[str, tuple[str, str]]:
    """Return {scenario_id: (track_a, track_b)}."""
    if not COMBINED.exists():
        # 파일이 없으면 빈 값으로 초기화
        return {sid: ("", "") for sid in _load_example_order()}
    with COMBINED.open(encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if rows and rows[0] != HEADER:
        raise SystemExit(f"combined 헤더 불일치: {rows[0]}")
    return {r[0]: (r[1] if len(r) > 1 else "", r[2] if len(r) > 2 else "")
            for r in rows[1:] if r}


def write_combined(data: dict[str, tuple[str, str]]) -> None:
    """submission_example 의 순서를 유지하며 덮어쓰기."""
    order = _load_example_order()
    COMBINED.parent.mkdir(parents=True, exist_ok=True)
    with COMBINED.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        for sid in order:
            a, b = data.get(sid, ("", ""))
            w.writerow([sid, a, b])


def flatten_newlines(text: str | None) -> str:
    """Zindi parser 는 quoted field 내 newline 에 실패 — 모두 literal \\n 으로 평탄화."""
    if text is None:
        return ""
    return text.replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n")


def update_track(track: Literal["A", "B"], preds: dict[str, str], verbose: bool = False) -> dict:
    """combined 에서 지정된 track 열만 preds 로 덮어쓰기.

    Args:
        track: 'A' 또는 'B'
        preds: {scenario_id: prediction}. 없는 scenario_id 는 기존 값 유지.
        verbose: 변경된 row 수를 로그에 찍을지

    Returns:
        {'changed': N, 'total_filled_a': ..., 'total_filled_b': ...}
    """
    if track not in ("A", "B"):
        raise ValueError(f"track must be 'A' or 'B', got {track!r}")
    data = read_combined()
    changed = 0
    for sid in list(data.keys()):
        a, b = data[sid]
        if sid not in preds:
            continue
        new = flatten_newlines(preds[sid])
        if track == "A" and a != new:
            data[sid] = (new, b)
            changed += 1
        elif track == "B" and b != new:
            data[sid] = (a, new)
            changed += 1
    write_combined(data)
    filled_a = sum(1 for a, _ in data.values() if a)
    filled_b = sum(1 for _, b in data.values() if b)
    if verbose:
        print(f"[merge_submission] track={track} changed={changed} "
              f"total Track A filled={filled_a}/{len(data)}, "
              f"Track B filled={filled_b}/{len(data)}, "
              f"combined={COMBINED}")
    return {"changed": changed, "filled_a": filled_a, "filled_b": filled_b, "total": len(data)}


def reset_combined() -> None:
    data = {sid: ("", "") for sid in _load_example_order()}
    write_combined(data)
    print(f"reset {COMBINED} (all cells empty, {len(data)} rows)")


def status() -> None:
    data = read_combined()
    filled_a = sum(1 for a, _ in data.values() if a)
    filled_b = sum(1 for _, b in data.values() if b)
    both = sum(1 for a, b in data.values() if a and b)
    print(f"Combined: {COMBINED}")
    print(f"  exists: {COMBINED.exists()}")
    print(f"  total rows: {len(data)}")
    print(f"  Track A filled: {filled_a}")
    print(f"  Track B filled: {filled_b}")
    print(f"  both filled: {both} (should be 0 — each scenario belongs to one track)")


def _load_preds_csv(path: Path) -> dict[str, str]:
    preds: dict[str, str] = {}
    with path.open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            sid = row.get("scenario_id") or row.get("id")
            if not sid:
                continue
            preds[sid] = row.get("prediction", "")
    return preds


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", choices=["A", "B"])
    ap.add_argument("--results", type=Path, help="result.csv (scenario_id,prediction)")
    ap.add_argument("--status", action="store_true", help="Show combined status and exit")
    ap.add_argument("--reset", action="store_true", help="Reset combined CSV to empty")
    args = ap.parse_args()

    if args.status:
        status()
        return
    if args.reset:
        reset_combined()
        return
    if not args.track or not args.results:
        ap.error("--track and --results required (or use --status / --reset)")
    if not args.results.exists():
        sys.exit(f"results not found: {args.results}")

    preds = _load_preds_csv(args.results)
    info = update_track(args.track, preds, verbose=True)
    print(info)


if __name__ == "__main__":
    main()
