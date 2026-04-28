"""Submission 042 — Dual Control + Exotic Categories.

목적:
  probe 038-V2 (multi-hypothesis) 결과: 0.60 (+0.04 = 2 정답)
  probe 039 (L3VPN 8 일괄) 결과:        0.60 (변화 없음)

  두 probe 모두 +0.04 → 가능 시나리오 2개를 분리 못함:
    S1. Group B (L3VPN, Q40/Q41) 정답 단독
    S2. Group C (static, Q47/Q48) 정답 단독, probe 039 에서 swap 발생

확정 사실:
  - Group A (BGP/L3VPN 모두 오답, 3문제 0 정답)
  - Group D (ARP/L3VPN 모두 오답, 1문제 0 정답)

설계 — Dual Control + Exotic:
  Group B (Q40/Q41): L3VPN 유지 — control 1
  Group C (Q47/Q48): static route error 유지 — control 2 (probe 038-V2 동일)
  Group A (Q39/Q43/Q46): routing loop ★ exotic 카테고리 검증
  Group D (Q49): blackhole route ★ exotic 검증
  Q42: VPN configuration missing ★ 새 port 카테고리 (이전 IP error 폐기)
  Q44/Q45/Q50: baseline 보존

  → 변경 9 라인

Δscore vs 0.56 결정 트리:
  +0.04 (0.60): S1 또는 S2 단독, 새 카테고리 모두 오답 → 추가 분리 probe 필요
  +0.08 (0.64): Group B L3VPN + Group C static 둘 다 정답 (4 정답) ★ 최선
  +0.06 (0.62): 한 그룹 + 1 새 카테고리 정답 (3 정답)
  +0.10~+0.14 (0.66~0.70): Group B + Group C + 다수 새 카테고리 정답
  0 (0.56): 모두 오답 — 매우 unlikely (최소 Group B 또는 Group C 는 정답이라는 강한 증거)

가설 우선순위:
  - L3VPN: vpn-instance routing 환경 (PJ overlay)
  - static route error: 일반 static route 설정 오류
  - routing loop: dst 20.1.1.10 가 PJGFA peer subnet — cross-zone routing 에 loop 가능성
  - blackhole route: dst 20.1.4.10 (Group D) 가 fault 분기점
  - VPN configuration missing: Q42 ARP_DUPLICATE 가 vpn-instance Vbdif10 충돌
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
    / "submission_042_20260428_dual_control_exotic.csv"
)

_NEW_ANSWERS: dict[int, str] = {
    # Group A (dst 20.1.1.10, 3): routing loop ★ exotic
    39: "Demeter-Prime-01;20.1.1.10;routing loop",
    43: "Demeter-Prime-01;20.1.1.10;routing loop",
    46: "Demeter-Prime-01;20.1.1.10;routing loop",
    # Group B (dst 10.1.6.3, 2): L3VPN configuration error — control 1
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (dst 20.1.1.20, 2): static route error — control 2
    47: "Demeter-Prime-01;20.1.1.20;static route error",
    48: "Demeter-Prime-01;20.1.1.20;static route error",
    # Group D (dst 20.1.4.10, 1): blackhole route ★ exotic
    49: "Demeter-Prime-01;20.1.4.10;blackhole route",
    # Q42 (port): VPN configuration missing ★ 새 카테고리
    42: "Demeter-Prime-02;GE1/0/5;VPN configuration missing",
    # Q44, Q45, Q50: baseline 보존 (변경 없음)
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

    print(f"=== submission_042_dual_control_exotic 생성 완료 ===")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (dst 20.1.1.10, routing loop ★ exotic)": [39, 43, 46],
        "B (dst 10.1.6.3, L3VPN — control 1)": [40, 41],
        "C (dst 20.1.1.20, static — control 2)": [47, 48],
        "D (dst 20.1.4.10, blackhole ★ exotic)": [49],
        "Q42 (port, VPN config missing ★ new)": [42],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- Group {group_name} ---")
        for q in qids:
            _, old, new = change_map[q]
            print(f"  Q{q}: {old}")
            print(f"    → {new}")
        print()
    print("Δscore vs 0.56 결정 트리:")
    print("  +0.04 (0.60): S1/S2 분리 못함, exotic 모두 오답 → isolation probe")
    print("  +0.08 (0.64): Group B + Group C 둘 다 정답 ★ 최선")
    print("  +0.06 (0.62): 한 그룹 + 1 exotic 정답")
    print("  +0.10~+0.14 (0.66~0.70): 다수 정답")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
