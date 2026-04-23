"""submission_combined_test.csv — HIGH + MEDIUM-HIGH 신뢰도 Opus 답 반영.

submission_combined.csv (018 기반, HIGH disagreement 2건만 교체) 대비 차이점:
- MEDIUM-HIGH entry 도 opus_answer 를 사용
- 실제로 현재 GROUND_TRUTH.json 에서 MEDIUM-HIGH 27건 전부 opus == baseline
  이므로 결과 내용은 combined 와 동일하지만, **test submission 용도**로
  별도 파일 로 저장 (확신도 범위 명시).

용도: Zindi test 업로드 비교 실험용.

Source:
- Track A: agent/track_a/submission/submission_v2.csv (500)
- Track B: GROUND_TRUTH.json entries 중 confidence ∈ {HIGH, MEDIUM-HIGH} 만 Opus 답 사용
  (MEDIUM/LOW 는 0건이므로 실질적으로 전 50 entry)

Output:
- agent/common/submission/submission_combined_test.csv
"""
# pyright: reportMissingImports=false

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS))

_PROJECT_ROOT = _THIS.parent.parent.parent
_GROUND_TRUTH = _PROJECT_ROOT / "agent" / "track_b" / "opus_reference" / "GROUND_TRUTH.json"
_TRACK_A_CSV = _PROJECT_ROOT / "agent" / "track_a" / "submission" / "submission_v2.csv"
_EXAMPLE = _PROJECT_ROOT / "agent" / "common" / "submission_example.csv"
_OUT = _THIS / "submission_combined_test.csv"

_ALLOWED_CONF = {"HIGH", "MEDIUM-HIGH"}


def main() -> int:
    # 1. GROUND_TRUTH 필터링
    with _GROUND_TRUTH.open(encoding="utf-8") as f:
        doc = json.load(f)

    tb_by_sid: dict[str, str] = {}
    stats = {"included": 0, "skipped": 0, "disagree_with_baseline": 0}
    by_conf = {"HIGH": 0, "MEDIUM-HIGH": 0, "MEDIUM": 0, "LOW": 0}

    for e in doc["entries"]:
        by_conf[e["confidence"]] = by_conf.get(e["confidence"], 0) + 1
        if e["confidence"] not in _ALLOWED_CONF:
            stats["skipped"] += 1
            continue
        tb_by_sid[e["scenario_id"]] = e["opus_answer"]
        stats["included"] += 1
        if not e["agrees_with_baseline"]:
            stats["disagree_with_baseline"] += 1

    print("[GROUND_TRUTH 통계]")
    print(f"  total entries: {len(doc['entries'])}")
    print(f"  by confidence: {by_conf}")
    print(f"  allowed (HIGH+MEDIUM-HIGH): {stats['included']}")
    print(f"  skipped (MEDIUM/LOW): {stats['skipped']}")
    print(f"  disagreements vs baseline (in included): {stats['disagree_with_baseline']}")

    # 2. Track A 로드
    track_a_map: dict[str, str] = {}
    with _TRACK_A_CSV.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            val = (r.get("Track A") or "").strip()
            if val:
                track_a_map[r["ID"]] = val
    print(f"\n[Track A source] {_TRACK_A_CSV.name}: {len(track_a_map)} filled")

    # 3. example template 순서대로 조립
    with _EXAMPLE.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or ["ID", "Track A", "Track B"])
        order = [r["ID"] for r in reader]

    out_rows: list[dict[str, str]] = []
    for sid in order:
        out_rows.append({
            "ID": sid,
            "Track A": track_a_map.get(sid, ""),
            "Track B": tb_by_sid.get(sid, ""),
        })

    filled_a = sum(1 for r in out_rows if r["Track A"])
    filled_b = sum(1 for r in out_rows if r["Track B"])
    both = sum(1 for r in out_rows if r["Track A"] and r["Track B"])
    print(f"\n[OUTPUT composition]")
    print(f"  total rows: {len(out_rows)}")
    print(f"  Track A filled: {filled_a}")
    print(f"  Track B filled: {filled_b}")
    print(f"  both filled: {both} (should be 0)")

    # 4. 저장
    with _OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"\n[SAVED] {_OUT}")

    # 5. Format sanity
    print("\n[FORMAT CHECK] literal \\n 유지 확인")
    shown = 0
    for r in out_rows:
        tb = r["Track B"]
        if tb and shown < 3:
            has_lit = "\\n" in tb
            has_real = "\n" in tb
            print(f"  {r['ID'][:16]}: literal_n={has_lit}, real_n={has_real}, len={len(tb)}")
            shown += 1

    # 6. vs baseline 비교 요약
    print("\n[DIFF vs baseline 016 (topofault_rt)]")
    baseline_tb: dict[str, str] = {}
    baseline_csv = _PROJECT_ROOT / "agent" / "track_b" / "submission" / "submission_v12_topofault_rt.csv"
    with baseline_csv.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            val = (r.get("Track B") or "").strip()
            if val:
                baseline_tb[r["ID"]] = val
    diff_count = 0
    for r in out_rows:
        sid = r["ID"]
        if sid in baseline_tb and r["Track B"] != baseline_tb[sid]:
            diff_count += 1
            print(f"  {sid[:16]}:")
            print(f"    base: {baseline_tb[sid][:80]}")
            print(f"    test: {r['Track B'][:80]}")
    print(f"  TOTAL Track B diff: {diff_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
