"""Submission serial 018 생성 — GROUND_TRUTH.json Opus 답 기반.

Source: agent/track_b/opus_reference/GROUND_TRUTH.json (50 entries, HIGH 23 + MEDIUM-HIGH 27)
Base template: agent/common/submission_example.csv (550 rows, Track A/B 컬럼)
Output: agent/track_b/submission/submission_018_20260423_ground_truth.csv

차이점 (vs baseline serial 016 = submission_v12_topofault_rt.csv):
- Q25: Beta-Node-01;192.168.70.70;static route error
     → Alpha-Center-02;192.168.70.70;static route error  (HIGH, routing evidence)
- Q28: Beta-Node-01;192.168.70.93;static route error
     → Gamma-Axis-02;192.168.70.93;routing loop         (HIGH, routing loop 증거)
나머지 48 entry 는 baseline 과 동일 (Opus 검증된 정답 유지).

포맷 스펙 (agent/common/submission_example.csv 기준):
- Multi-line 답 은 literal `\n` (backslash+n) 으로 구분
- Track A 컬럼 은 example 값 그대로 유지 (본 스크립트는 Track B 만 다룸)

Usage:
    python3 agent/track_b/submission/gen_submission_018.py --dry-run
    python3 agent/track_b/submission/gen_submission_018.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve().parent
_PROJECT_ROOT = _THIS.parent.parent.parent

_GROUND_TRUTH = _PROJECT_ROOT / "agent" / "track_b" / "opus_reference" / "GROUND_TRUTH.json"
_EXAMPLE_CSV = _PROJECT_ROOT / "agent" / "common" / "submission_example.csv"
_BASELINE_CSV = _THIS / "submission_v12_topofault_rt.csv"
_OUT_CSV = _THIS / "submission_018_20260423_ground_truth.csv"


def _load_ground_truth() -> dict[str, dict]:
    """scenario_id → entry 매핑."""
    with _GROUND_TRUTH.open(encoding="utf-8") as f:
        doc = json.load(f)
    return {e["scenario_id"]: e for e in doc["entries"]}


def _load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    return rows, fieldnames


def main() -> int:
    parser = argparse.ArgumentParser(description="submission 018 생성")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # 1. GROUND_TRUTH 로드
    if not _GROUND_TRUTH.exists():
        print(f"[ERROR] {_GROUND_TRUTH} 없음", file=sys.stderr)
        return 1
    gt = _load_ground_truth()
    print(f"[INFO] ground truth entries: {len(gt)}")

    # 2. example CSV 를 template 으로 로드 (550 rows, Track A 포함)
    example_rows, fieldnames = _load_csv(_EXAMPLE_CSV)
    print(f"[INFO] example template: {len(example_rows)} rows")

    # 3. baseline CSV 로드 (Track A 답변 소스)
    baseline_rows, _ = _load_csv(_BASELINE_CSV)
    baseline_by_id = {r["ID"]: r for r in baseline_rows}
    print(f"[INFO] baseline rows: {len(baseline_rows)}")

    # 4. submission 018 rows 구성
    out_rows: list[dict[str, str]] = []
    track_b_changes: list[tuple[int, str, str, str]] = []  # (qid, baseline, new, confidence)
    track_b_filled = 0
    for row in example_rows:
        sid = row["ID"]
        new_row = {"ID": sid, "Track A": "", "Track B": ""}

        # Track A: baseline 값 유지 (v12_topofault_rt 는 Track B 만 채움;
        # 실제 제출 시에는 별도 Track A 작업 필요 — 본 작업 범위 밖)
        if sid in baseline_by_id:
            new_row["Track A"] = baseline_by_id[sid].get("Track A", "") or ""

        # Track B: ground truth 의 opus_answer 사용
        if sid in gt:
            entry = gt[sid]
            opus = entry["opus_answer"]
            base = entry["baseline_answer"]
            new_row["Track B"] = opus
            track_b_filled += 1
            if opus != base:
                track_b_changes.append(
                    (entry["qid"], base, opus, entry["confidence"])
                )

        out_rows.append(new_row)

    print(f"[INFO] Track B filled: {track_b_filled} / {len(out_rows)}")
    print(f"[INFO] baseline 대비 Track B 변경: {len(track_b_changes)}")
    for qid, base, new, conf in track_b_changes:
        print(f"\n  Q{qid:02d} [{conf}]")
        print(f"    base: {base}")
        print(f"    opus: {new}")

    if args.dry_run:
        print("\n[DRY-RUN] 저장 안 함.")
        return 0

    # 5. 저장
    with _OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"\n[SAVED] {_OUT_CSV}")
    print(f"        rows={len(out_rows)}, Track B={track_b_filled}")

    # 6. Sanity: Track B 첫 3 entry 포맷 확인 (literal \n 유지)
    print("\n[FORMAT CHECK] Track B sample (literal \\n 유지 확인)")
    with _OUT_CSV.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        shown = 0
        for r in reader:
            tb = r.get("Track B", "")
            if tb and shown < 3:
                has_literal = "\\n" in tb
                has_real = "\n" in tb
                print(f"  {r['ID'][:16]}: literal_n={has_literal}, real_n={has_real}, len={len(tb)}")
                shown += 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
