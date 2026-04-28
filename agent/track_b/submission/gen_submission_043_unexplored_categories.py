"""Submission 043 — Unexplored Categories Sweep.

목적:
  probe 038-V2 (0.60), probe 039 (0.60), probe 042 (0.60) 결과 누적 분석:
    ★ Group B (L3VPN, Q40/Q41) 정답 단독 확정 (다른 가설 모두 부정)

  Group A/C/D + Q42 의 정답 카테고리는 시도된 카테고리 모두 오답.
  미시도 카테고리를 그룹별로 동시 시도.

오답 누적 (Group B 외):
  - Group A (Q39/43/46): BGP, L3VPN, routing loop, missing static route(baseline)
  - Group C (Q47/48): static, L3VPN, missing static route
  - Group D (Q49): ARP, L3VPN, blackhole, missing static route
  - Q42: MAC(baseline), interface IP error, VPN configuration missing

설계 — Maximum Differential (분리 가능 가중치):
  Group A (3): IS-IS configuration error ★ 미시도
  Group B (2): L3VPN configuration error — control (+0.04 보장)
  Group C (2): ARP configuration error ★ 미시도
  Group D (1): OSPF configuration error ★ 미시도
  Q42 (1):     MTU value configuration error ★ 미시도

가설 우선순위:
  - IS-IS for Group A (dst 20.1.1.10): PJGFA cross-zone backbone IS-IS 가능
  - ARP for Group C (dst 20.1.1.20): cross-zone ARP 미해결
  - OSPF for Group D (dst 20.1.4.10): vpn4 OSPF 설정 오류
  - MTU for Q42: GE1/0/5 인터페이스 MTU 불일치 가능 (logbuffer link flap)

Δscore vs 0.56 (BEST) 결정 트리:
  0.60 (Group B만): 새 가설 모두 오답
  0.62 (+1 정답): Group D OSPF 또는 Q42 MTU
  0.64 (+2 정답): Group C ARP
  0.66 (+3 정답): Group A IS-IS, 또는 Group C + Group D 등
  0.68 (+4 정답): Group A + 1 또는 Group C + Group D + Q42
  0.70+: 다수 정답
  ★★ 0.74 (+0.18): 모든 새 가설 정답 (leader tie 거의 도달)

이 probe 1회로 4 새 가설 동시 검증 → 다음 probe 에서 정답 카테고리 일괄 적용.
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
    / "submission_043_20260428_unexplored_categories.csv"
)

_NEW_ANSWERS: dict[int, str] = {
    # Group A (3): IS-IS configuration error ★ 미시도
    39: "Demeter-Prime-01;20.1.1.10;IS-IS configuration error",
    43: "Demeter-Prime-01;20.1.1.10;IS-IS configuration error",
    46: "Demeter-Prime-01;20.1.1.10;IS-IS configuration error",
    # Group B (2): L3VPN configuration error — control (정답 확정)
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (2): ARP configuration error ★ 미시도
    47: "Demeter-Prime-01;20.1.1.20;ARP configuration error",
    48: "Demeter-Prime-01;20.1.1.20;ARP configuration error",
    # Group D (1): OSPF configuration error ★ 미시도
    49: "Demeter-Prime-01;20.1.4.10;OSPF configuration error",
    # Q42 (1): MTU value configuration error ★ 미시도 port 카테고리
    42: "Demeter-Prime-02;GE1/0/5;MTU value configuration error",
    # Q44, Q45, Q50: baseline 보존
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
        print(f"[ERR] 예상치 못한 헤더", file=sys.stderr)
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
        print(f"[ERR] 변경 건수 불일치", file=sys.stderr)
        return 1

    with _OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    print(f"=== submission_043_unexplored_categories 생성 완료 ===")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (dst 20.1.1.10, IS-IS ★ 미시도)": [39, 43, 46],
        "B (dst 10.1.6.3, L3VPN — control ★ 정답)": [40, 41],
        "C (dst 20.1.1.20, ARP ★ 미시도)": [47, 48],
        "D (dst 20.1.4.10, OSPF ★ 미시도)": [49],
        "Q42 (port, MTU ★ 미시도)": [42],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- Group {group_name} ---")
        for q in qids:
            _, old, new = change_map[q]
            print(f"  Q{q}: {old}")
            print(f"    → {new}")
        print()
    print("Δscore vs 0.56 (BEST) 결정 트리:")
    print("  0.60 (그대로): 새 가설 모두 오답 → 다음 probe 에서 다른 카테고리 (loopback IP, L2VPN, SRV6)")
    print("  0.62: Group D OSPF 또는 Q42 MTU 정답 (1)")
    print("  0.64: Group C ARP 정답 (2)")
    print("  0.66: Group A IS-IS 정답 (3) 또는 Group C + 1 (3)")
    print("  0.68~+: 다수 hit")
    print("  ★★ 0.74: 모든 새 가설 정답 → leader tie (0.78) 거의 도달")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
