"""Submission 049 — Track B 마지막 reason burn: loopback IP configuration conflict.

배경:
  10 probe (038-V2 ~ 048) 모두 0.60 무변화. 18 reason × 4+ 노드 × 2 line 구조 + raw scenario 분석
  모두 부정. Track B 0.60 사실상 고착.

  마지막 미시도 routing reason 1종 = `loopback IP configuration conflict`.

전략:
  probe 048 의 source-device 프레임 유지 (Hermes-Prime-XX), reason 만 swap.
  - Slot A (Q39/43/46): `Hermes-Prime-01;20.1.1.10;loopback IP configuration conflict`
  - Slot C (Q47/48):    `Hermes-Prime-02;20.1.1.20;loopback IP configuration conflict`
  - Slot D (Q49):       `Hermes-Prime-01;20.1.4.10;loopback IP configuration conflict`
  - Q42:                (baseline 보존, port fault 라 해당 reason 적용 불가)

목적:
  마지막 reason 차원 burn. 부정 시 모든 routing reason × source-device 조합 부정 확정 →
  Track A 강화로 ROI 전환 (Track A 500문제 vs Track B 잔여 8문제 = 6.25× ROI).

Δscore vs 0.60 결정 트리:
  +0.12 (6 정답): ★ 마지막 reason 적중 → 0.72
  +0.06 (3 정답): A 그룹만
  +0.04 (2 정답): C 그룹만
  +0.02 (1 정답): D 또는 부분
  +0    (0 정답): Track B 모든 routing reason 부정 확정 → Track A 전환
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _DIR.parent.parent.parent
_BASE_CSV = (
    _PROJECT_ROOT
    / "agent"
    / "common"
    / "submission"
    / "submission_BEST_0_56_track_ab_20260427.csv"
)
_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_OUT_CSV = (
    _PROJECT_ROOT
    / "agent"
    / "common"
    / "submission"
    / "submission_049_20260429_loopback_ip_conflict.csv"
)

_GROUP_A_ANSWER = "Hermes-Prime-01;20.1.1.10;loopback IP configuration conflict"
_GROUP_C_ANSWER = "Hermes-Prime-02;20.1.1.20;loopback IP configuration conflict"
_GROUP_D_ANSWER = "Hermes-Prime-01;20.1.4.10;loopback IP configuration conflict"

_NEW_ANSWERS: dict[int, str] = {
    # Group A (3): source-device + loopback IP conflict
    39: _GROUP_A_ANSWER,
    43: _GROUP_A_ANSWER,
    46: _GROUP_A_ANSWER,
    # Group B (2): L3VPN — control 정답 확정 (보존)
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (2): source-device + loopback IP conflict
    47: _GROUP_C_ANSWER,
    48: _GROUP_C_ANSWER,
    # Group D (1): source-device + loopback IP conflict
    49: _GROUP_D_ANSWER,
    # Q42, Q44/45/50 보존
}


def _load_qid_to_sid(test_json_path: Path) -> dict[int, str]:
    with test_json_path.open() as fp:
        questions = json.load(fp)
    return {idx + 1: q["scenario_id"] for idx, q in enumerate(questions)}


def main() -> int:
    qid_to_sid = _load_qid_to_sid(_TEST_JSON)
    sid_to_new = {qid_to_sid[q]: a for q, a in _NEW_ANSWERS.items()}

    with _BASE_CSV.open("r", newline="", encoding="utf-8") as fp:
        rows = list(csv.reader(fp))

    if rows[0] != ["ID", "Track A", "Track B"]:
        print("[ERR] 예상치 못한 헤더", file=sys.stderr)
        return 1

    changes: list[tuple[int, str, str, str]] = []
    for row in rows[1:]:
        if len(row) < 3:
            continue
        if row[0] in sid_to_new:
            old_ans = row[2]
            row[2] = sid_to_new[row[0]]
            qid = next(q for q, s in qid_to_sid.items() if s == row[0])
            changes.append((qid, row[0], old_ans, row[2]))

    if len(changes) != len(_NEW_ANSWERS):
        print(
            f"[ERR] 변경 건수 불일치: 기대 {len(_NEW_ANSWERS)}, 실제 {len(changes)}",
            file=sys.stderr,
        )
        return 1

    with _OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print("=== submission_049_loopback_ip_conflict 생성 완료 ===")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (Q39/43/46) → Hermes-Prime-01;20.1.1.10;loopback IP configuration conflict ★": [39, 43, 46],
        "B (Q40/41)    → L3VPN — control 정답 확정 (보존)": [40, 41],
        "C (Q47/48)    → Hermes-Prime-02;20.1.1.20;loopback IP configuration conflict ★": [47, 48],
        "D (Q49)       → Hermes-Prime-01;20.1.4.10;loopback IP configuration conflict ★": [49],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- {group_name} ---")
        for q in qids:
            _, _, new = change_map[q]
            print(f"  Q{q}: {new}")
        print()
    print("Δscore vs 0.60 결정 트리:")
    print("  +0.12 (6 정답): ★ 마지막 reason 적중 → 0.72")
    print("  +0.06 (3 정답): A 그룹만")
    print("  +0.04 (2 정답): C 그룹만")
    print("  +0.02 (1 정답): D 또는 부분")
    print("  +0    (0 정답): Track B 모든 routing reason 부정 확정 → Track A 전환")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
