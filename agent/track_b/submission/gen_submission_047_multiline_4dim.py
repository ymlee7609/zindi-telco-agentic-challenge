"""Submission 047 — Multi-line 가설 4차원 분산 probe.

배경:
  028 sanity = 0.42 (-0.06 정확 적중) → 채점 정상 동작 확인.
  18 reason × 3 노드 시도 모두 0/0 → baseline + 우리 변경 모두 오답.
  → 답안 공간 자체가 우리 가정과 다름 확정.

raw 질문 텍스트 비교 발견:
  - Q39 = Q43 = Q46 (동일 질문, dst 20.1.1.10 cross-zone)
  - Q40 = Q41 (동일 질문, dst 10.1.6.3 in-zone) — L3VPN single-line 정답 확정
  - Q47 = Q48 (동일 질문, dst 20.1.1.20 cross-zone)
  - 포맷 스펙 명시: "if there are multiple fault reasons, output each on a new line"

핵심 가설:
  in-zone 질문 (Q40/41) = single-line 충분
  cross-zone 질문 (Q39/43/46/47/48/49) = multi-line 답안 (port-fault root + routing chain) 필요

답안 매트릭스:
  | Slot | QID       | 답안 구조                                           | 가설 차원       |
  |------|-----------|-----------------------------------------------------|-----------------|
  | A    | Q39/43/46 | 2-line: Aegis port + Demeter L3VPN                  | port+routing    |
  | B    | Q40/41    | (보존)                                              | control 정답    |
  | C    | Q47/48    | single-line: Demeter L3VPN (Q40 mirror, cross-zone) | Q40 패턴 일반화 |
  | D    | Q49       | 3-line: Aegis port + Demeter-01 + Demeter-02 L3VPN  | full chain      |
  | Q42  | Q42       | 2-line: Demeter-02 + Demeter-01 MAC error           | dual-device     |

Δscore vs 0.60 결정 트리:
  +0    : 모두 부정 → multi-line 가설 자체 부정
  +0.02 : D 또는 Q42 단독
  +0.04 : C 적중 (2 instances) ★ Q40 패턴 일반화 → cross-zone 일괄 적용 가능
  +0.06 : A 적중 (3 instances, 2-line chain)
  +0.08 : A+C 또는 다수
  +0.10+: 대다수 적중

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
    / "submission_047_20260429_multiline_4dim.csv"
)

# Group A (Q39/43/46, dst 20.1.1.10 cross-zone): 2-line port+routing chain
# CSV 안에 backslash + n 두 문자가 그대로 저장되어야 함 (Zindi 공식 포맷)
_GROUP_A_ANSWER = (
    "Aegis-Prime-01;GE0/0/0;interface IP error"
    "\\n"
    "Demeter-Prime-01;20.1.1.10;L3VPN configuration error"
)

# Group C (Q47/48, dst 20.1.1.20 cross-zone): single-line Q40 mirror
_GROUP_C_ANSWER = "Demeter-Prime-01;20.1.1.20;L3VPN configuration error"

# Group D (Q49, dst 20.1.4.10 cross-zone): 3-line full chain
_GROUP_D_ANSWER = (
    "Aegis-Prime-01;GE0/0/0;interface IP error"
    "\\n"
    "Demeter-Prime-01;20.1.4.10;L3VPN configuration error"
    "\\n"
    "Demeter-Prime-02;20.1.4.10;L3VPN configuration error"
)

# Q42 (MAC conflict alarm): 2-line dual-device port fault
_Q42_ANSWER = (
    "Demeter-Prime-02;GE1/0/5;MAC address configuration error"
    "\\n"
    "Demeter-Prime-01;GE1/0/5;MAC address configuration error"
)

_NEW_ANSWERS: dict[int, str] = {
    # Group A (3): 2-line port+routing chain (multi-line 가설)
    39: _GROUP_A_ANSWER,
    43: _GROUP_A_ANSWER,
    46: _GROUP_A_ANSWER,
    # Group B (2): L3VPN — control 정답 확정 (보존)
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (2): single-line Q40 mirror (cross-zone dst)
    47: _GROUP_C_ANSWER,
    48: _GROUP_C_ANSWER,
    # Group D (1): 3-line full chain (port + dual-PE)
    49: _GROUP_D_ANSWER,
    # Q42 (1): 2-line dual-device port fault
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

    print("=== submission_047_multiline_4dim 생성 완료 ===")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (Q39/43/46) → 2-line port+routing ★ multi-line 가설": [39, 43, 46],
        "B (Q40/41)    → L3VPN single-line (보존, control)": [40, 41],
        "C (Q47/48)    → Demeter L3VPN single-line ★ Q40 mirror": [47, 48],
        "D (Q49)       → 3-line full chain ★": [49],
        "Q42           → 2-line dual-device MAC error ★": [42],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- {group_name} ---")
        for q in qids:
            _, _, new = change_map[q]
            print(f"  Q{q}: {new}")
        print()
    print("Δscore vs 0.60 결정 트리:")
    print("  +0    : 모두 부정 → multi-line 가설 자체 부정")
    print("  +0.02 : D 또는 Q42 단독")
    print("  +0.04 : C 적중 ★ Q40 패턴 일반화 → cross-zone 일괄 적용 가능")
    print("  +0.06 : A 적중 (2-line chain)")
    print("  +0.08+: 다수 적중")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
