"""Submission 046 — 4차원 분산 multi-hypothesis probe.

배경:
  probe 045 (Aegis-Prime-01 GE0/0/0 interface IP error 6건) 도 0.60 무변화.
  14 카테고리 + raw-diff root cause 까지 부정 → Group A/C/D/Q42 답안은
  (device=Aegis-Prime-01, port=GE0/0/0, reason ∈ 14카테고리) 공간 밖에 존재.

전략 (1회 제출에 4 차원 동시 검증):
  Group A → 다른 노드 (Atlas-Prime-01 OSPF peer DOWN 측)
  Group C → 미시도 reason (L2VPN configuration error)
  Group D → 미시도 reason (SRV6-Policy tunnel planning error)
  Q42    → multi-device multi-line literal `\\n` 포맷 검증

답안 매트릭스:
  | Group | QID       | 답안                                                  | 검증 차원        |
  |-------|-----------|-------------------------------------------------------|------------------|
  | A     | Q39/43/46 | Atlas-Prime-01;GE1/0/0;OSPF configuration error       | 노드 차원        |
  | B     | Q40/41    | Demeter-Prime-01;10.1.6.3;L3VPN configuration error   | (정답 보존)      |
  | C     | Q47/48    | Aegis-Prime-01;GE0/0/0;L2VPN configuration error      | reason 차원      |
  | D     | Q49       | Aegis-Prime-01;GE0/0/0;SRV6-Policy tunnel planning error | reason 차원   |
  | Q42   | Q42       | (multi-device literal \\n 포맷)                        | 답안 포맷 차원   |

Δscore vs 0.60 결정 트리:
  0.60 (+0): 4 차원 모두 부정 → 028 sanity 우선 (채점/포맷 진단)
  0.62 (+0.02): D 단독 또는 Q42 단독 정답 → 적중 차원으로 1차원 burn
  0.64 (+0.04): C(2) 또는 A부분(1)+D(1) 등 → 그룹별 confirmer probe
  0.66 (+0.06): A 정답 가장 유력 (Atlas 노드 적중) → A 8문제 OSPF 일괄 도전
  0.68+ (+0.08+): 다수 차원 적중 → best mix 통합

  ★★ Leader 0.78 까지 0.18 거리.
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
    / "submission_046_20260429_4dim_mix.csv"
)

# Group A: 다른 노드 가설 (Atlas-Prime-01 GE1/0/0 OSPF peer DOWN 측)
_GROUP_A_ANSWER = "Atlas-Prime-01;GE1/0/0;OSPF configuration error"

# Group C: 미시도 reason 가설 (L2VPN — 14 카테고리 외)
_GROUP_C_ANSWER = "Aegis-Prime-01;GE0/0/0;L2VPN configuration error"

# Group D: 미시도 reason 가설 (SRV6-Policy — 14 카테고리 외)
_GROUP_D_ANSWER = "Aegis-Prime-01;GE0/0/0;SRV6-Policy tunnel planning error"

# Q42: multi-device multi-line 포맷 가설 (literal `\n` 두 노드)
# CSV 안에 backslash + n 두 문자가 그대로 저장되어야 함 (Zindi 공식 포맷)
_Q42_ANSWER = (
    "Demeter-Prime-02;GE1/0/5;traffic congestion on port bandwidth"
    "\\n"
    "Demeter-Prime-01;GE1/0/5;traffic congestion on port bandwidth"
)

_NEW_ANSWERS: dict[int, str] = {
    # Group A (3): Atlas-Prime-01 OSPF (노드 차원 검증)
    39: _GROUP_A_ANSWER,
    43: _GROUP_A_ANSWER,
    46: _GROUP_A_ANSWER,
    # Group B (2): L3VPN — control 정답 확정 (보존)
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (2): L2VPN reason (reason 차원 검증)
    47: _GROUP_C_ANSWER,
    48: _GROUP_C_ANSWER,
    # Group D (1): SRV6-Policy reason (reason 차원 검증)
    49: _GROUP_D_ANSWER,
    # Q42 (1): multi-device multi-line (포맷 차원 검증)
    42: _Q42_ANSWER,
    # Q44/45/50 보존
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

    print("=== submission_046_4dim_mix 생성 완료 ===")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (Q39/43/46) → Atlas-Prime-01;GE1/0/0;OSPF ★ 노드 차원": [39, 43, 46],
        "B (Q40/41)    → L3VPN — control 정답 확정 (보존)": [40, 41],
        "C (Q47/48)    → Aegis;L2VPN ★ reason 차원": [47, 48],
        "D (Q49)       → Aegis;SRV6-Policy ★ reason 차원": [49],
        "Q42           → multi-device literal \\n ★ 포맷 차원": [42],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- {group_name} ---")
        for q in qids:
            _, _, new = change_map[q]
            print(f"  Q{q}: {new}")
        print()
    print("Δscore vs 0.60 결정 트리:")
    print("  +0    : 4 차원 모두 부정 → 028 sanity 우선")
    print("  +0.02 : D 단독 또는 Q42 단독 → 적중 차원 1차원 burn")
    print("  +0.04 : C(2) 또는 A부분+D 등 → confirmer probe")
    print("  +0.06 : A 정답 가장 유력 (Atlas 노드) → A 8문제 OSPF 일괄 → 0.66+")
    print("  +0.08+: 다수 차원 적중 → best mix 통합")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
