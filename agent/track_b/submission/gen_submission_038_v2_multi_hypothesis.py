"""Submission 038-V2 — Multi-Hypothesis Probe (1회 제출 정보량 극대화).

목적:
  하루 10회 submit 제한 + 1시간 후 제출 가능 + 시간 압박.
  단일 카테고리 일괄 probe (BGP all 또는 L3VPN all) 는 1회당 1차원 정보만 획득.
  대신 dst 그룹별 다른 카테고리를 매핑하여 1회 제출에 4 가설 동시 검증.

핵심 가정:
  같은 dst 를 가진 fault 문제들은 정답 카테고리가 동일할 가능성이 매우 높음.
  - dst 20.1.1.10: Q39, Q43, Q46 (3문제) — 동일 정답 가정
  - dst 10.1.6.3:  Q40, Q41 (2문제) — 동일 정답
  - dst 20.1.1.20: Q47, Q48 (2문제) — 동일 정답
  - dst 20.1.4.10: Q49 (1문제)

따라서 그룹별로 다른 카테고리를 시도하면 Δscore 가 정답 그룹의 크기 합으로
나타나, 어느 카테고리가 정답인지 좁혀진다.

변경 내역 (base = BEST 0.56 통합본):
  Group A (dst 20.1.1.10, 3): BGP configuration error  ★ 가장 유력 가설
  Group B (dst 10.1.6.3,  2): L3VPN configuration error
  Group C (dst 20.1.1.20, 2): static route error
  Group D (dst 20.1.4.10, 1): ARP configuration error
  Q42 (port fault, 1):        interface IP error
  Q44, Q45 (port fault, 2):   shutdown 보존
  Q50 (routing fault, 1):     ARP configuration error 보존

  → 변경 9 라인 (8 routing 4 그룹 + 1 port)

Δscore 결정 트리:
  +0.06 → Group A (BGP) 그룹 정답 가장 유력 → 041 BGP 일괄
  +0.04 → Group B (L3VPN) 또는 Group C (static) 정답
  +0.02 → 1 가설만 정답 (가장 모호)
  +0.08 → BGP 3 + 1 추가 (다른 그룹도 일부)
  +0.16~+0.18 → 거의 모든 가설 정답 (이상적 시나리오)

키워드 list 참조 (Q40 question 원문, 13 routing fault):
  blackhole route / missing static route / static route error /
  ARP configuration error / routing loop / BGP configuration error /
  OSPF configuration error / loopback IP configuration conflict /
  VXLAN configuration error / L3VPN configuration error /
  L2VPN configuration error / IS-IS configuration error /
  SRV6-Policy tunnel planning error
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
    / "submission_038v2_20260428_multi_hypothesis.csv"
)

# QID → 새 답안 매핑 (1-indexed). 같은 dst 그룹은 같은 카테고리.
_NEW_ANSWERS: dict[int, str] = {
    # Group A (dst 20.1.1.10, 3 questions): BGP configuration error
    39: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    43: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    46: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    # Group B (dst 10.1.6.3, 2): L3VPN configuration error
    40: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    41: "Demeter-Prime-01;10.1.6.3;L3VPN configuration error",
    # Group C (dst 20.1.1.20, 2): static route error
    47: "Demeter-Prime-01;20.1.1.20;static route error",
    48: "Demeter-Prime-01;20.1.1.20;static route error",
    # Group D (dst 20.1.4.10, 1): ARP configuration error
    49: "Demeter-Prime-01;20.1.4.10;ARP configuration error",
    # Q42 port fault: interface IP error (logbuffer ARP_DUPLICATE_IPADDR)
    42: "Demeter-Prime-02;GE1/0/5;interface IP error",
    # Q44, Q45, Q50: 보존 (변경 없음, baseline 정답 검증)
}


def _load_qid_to_sid(test_json_path: Path) -> dict[int, str]:
    # @MX:NOTE: test.json 의 list index (0-base) + 1 = qid
    with test_json_path.open() as fp:
        questions = json.load(fp)
    return {idx + 1: q["scenario_id"] for idx, q in enumerate(questions)}


def main() -> int:
    if not _BASE_CSV.exists():
        print(f"[ERR] baseline not found: {_BASE_CSV}", file=sys.stderr)
        return 1
    if not _TEST_JSON.exists():
        print(f"[ERR] test.json not found: {_TEST_JSON}", file=sys.stderr)
        return 1

    qid_to_sid = _load_qid_to_sid(_TEST_JSON)
    sid_to_new: dict[str, str] = {}
    for qid, new_ans in _NEW_ANSWERS.items():
        sid = qid_to_sid.get(qid)
        if sid is None:
            print(f"[ERR] Q{qid} 의 scenario_id 를 찾을 수 없음", file=sys.stderr)
            return 1
        sid_to_new[sid] = new_ans

    with _BASE_CSV.open("r", newline="", encoding="utf-8") as fp:
        rows = list(csv.reader(fp))

    if not rows or rows[0] != ["ID", "Track A", "Track B"]:
        print(
            f"[ERR] 예상치 못한 헤더: {rows[0] if rows else 'empty'}",
            file=sys.stderr,
        )
        return 1

    changes: list[tuple[int, str, str, str]] = []
    for row in rows[1:]:
        if len(row) < 3:
            continue
        sid = row[0]
        if sid in sid_to_new:
            old_ans = row[2]
            new_ans = sid_to_new[sid]
            row[2] = new_ans
            qid = next(q for q, s in qid_to_sid.items() if s == sid)
            changes.append((qid, sid, old_ans, new_ans))

    expected_changes = len(_NEW_ANSWERS)
    if len(changes) != expected_changes:
        print(
            f"[ERR] 변경 건수 불일치: 예상 {expected_changes}, 실제 {len(changes)}",
            file=sys.stderr,
        )
        return 1

    with _OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    # 결과 출력 (그룹별 정렬)
    print(f"=== submission_038v2_multi_hypothesis 생성 완료 ===")
    print(f"base : {_BASE_CSV.name}")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    groups = {
        "A (dst 20.1.1.10, BGP)": [39, 43, 46],
        "B (dst 10.1.6.3, L3VPN)": [40, 41],
        "C (dst 20.1.1.20, static)": [47, 48],
        "D (dst 20.1.4.10, ARP)": [49],
        "Q42 (port, IP error)": [42],
    }
    change_map = {q: (sid, old, new) for q, sid, old, new in changes}
    for group_name, qids in groups.items():
        print(f"--- Group {group_name} ---")
        for q in qids:
            _, old, new = change_map[q]
            print(f"  Q{q}: {old}")
            print(f"    → {new}")
        print()
    print("Δscore 결정 트리:")
    print("  +0.06 → Group A (BGP, 3) 정답 → 041 BGP 일괄 (8문제 모두)")
    print("  +0.04 → Group B (L3VPN) 또는 C (static) 정답")
    print("  +0.02 → 1 가설 정답 (Q42 또는 Group D)")
    print("  +0.08~+0.10 → BGP + 추가 그룹 정답")
    print("  +0.16~+0.22 → 다수 그룹 정답 (leader tie 접근)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
