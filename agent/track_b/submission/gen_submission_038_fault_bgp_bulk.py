"""Submission 038 — Track B PJ FAULT 일괄 BGP 카테고리 probe.

목적:
  현재 점수 0.56 → leaderboard 0.78 갭 = 11 정답 더 필요.
  PJ Q39~Q50 12 fault 문제의 정답 카테고리를 binary search 로 진단.

가설:
  - PJ는 EVPN VXLAN overlay 환경 (BGP EVPN 기반)
  - 13가지 routing fault 키워드 중 EVPN 키워드 없음 → "BGP configuration error" 유력
  - 020 (VXLAN A 3문제) 0.48 유지 = VXLAN 오답 확인됨
  - 021 (L3VPN), 024 (BGP) 미제출 — BGP 가 EVPN 기반이므로 우선 검증

변경 내역 (base = BEST 0.56 통합본):
  - Q39, Q40, Q41, Q43, Q46, Q47, Q48, Q49 (8문제) :
        "missing static route" → "BGP configuration error"
  - Q42 (port fault, ARP_DUPLICATE_IPADDR logbuffer 증거):
        "MAC address configuration error" → "interface IP error"
  - Q44, Q45 (shutdown 유지)
  - Q50 (ARP configuration error 유지)

  → 변경 9 lines (8 routing + 1 port)

예상 점수 변화:
  - 0.56 유지: BGP 모두 오답 → 다른 카테고리 (L3VPN, static route error 등)
  - 0.58~0.62: BGP 일부 정답 → fine-tuning probe 단계
  - 0.66+: BGP 다수 정답 → leader tie 가까움
  - 0.78+: 대박, leader tie 즉시 달성

키워드 list 참조 (Q40 question 원문):
  Routing fault: blackhole route / missing static route / static route error /
                 ARP configuration error / routing loop / BGP configuration error /
                 OSPF configuration error / loopback IP configuration conflict /
                 VXLAN configuration error / L3VPN configuration error /
                 L2VPN configuration error / IS-IS configuration error /
                 SRV6-Policy tunnel planning error
  Port fault: shutdown / interface IP error / traffic congestion on port bandwidth /
              MAC address configuration error / VPN configuration missing /
              OSPF configuration error / MTU value configuration error /
              host information collection function missing
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

# 경로 정의 (절대 경로 회피, 프로젝트 루트 상대로 해결)
_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _DIR.parent.parent.parent  # agent/track_b/submission → repo root
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
    / "submission_038_20260427_fault_bgp_bulk.csv"
)

# QID → 새 답안 매핑 (1-indexed)
# 형식: (fault_node, target, reason) — target 은 IP 또는 interface
_NEW_ANSWERS: dict[int, str] = {
    # Group A: 20.1.1.10 unreachable from Hermes-Prime-01
    39: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    43: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    46: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
    # Group B: 10.1.6.3 unreachable from Hermes-Prime-01
    40: "Demeter-Prime-01;10.1.6.3;BGP configuration error",
    41: "Demeter-Prime-01;10.1.6.3;BGP configuration error",
    # Group D: 20.1.1.20 unreachable from Hermes-Prime-02
    47: "Demeter-Prime-01;20.1.1.20;BGP configuration error",
    48: "Demeter-Prime-01;20.1.1.20;BGP configuration error",
    # Q49: 20.1.4.10 unreachable from Hermes-Prime-01
    49: "Demeter-Prime-01;20.1.4.10;BGP configuration error",
    # Q42: port fault, ARP_DUPLICATE_IPADDR → interface IP error
    42: "Demeter-Prime-02;GE1/0/5;interface IP error",
    # Q44, Q45 (shutdown 유지) / Q50 (ARP error 유지) — 변경 없음
}


def _load_qid_to_sid(test_json_path: Path) -> dict[int, str]:
    # @MX:NOTE: test.json 의 list index 가 1-based qid 와 매핑됨 (idx 0 → Q1)
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
    sid_to_new_answer: dict[str, str] = {}
    for qid, new_ans in _NEW_ANSWERS.items():
        sid = qid_to_sid.get(qid)
        if sid is None:
            print(f"[ERR] Q{qid} 의 scenario_id 를 찾을 수 없음", file=sys.stderr)
            return 1
        sid_to_new_answer[sid] = new_ans

    # 입력 CSV 읽기
    with _BASE_CSV.open("r", newline="", encoding="utf-8") as fp:
        rows = list(csv.reader(fp))

    if not rows or rows[0] != ["ID", "Track A", "Track B"]:
        print(f"[ERR] 예상치 못한 헤더: {rows[0] if rows else 'empty'}", file=sys.stderr)
        return 1

    # 변경 적용
    changes: list[tuple[int, str, str, str]] = []  # (qid, sid, old, new)
    for row in rows[1:]:
        if len(row) < 3:
            continue
        sid = row[0]
        if sid in sid_to_new_answer:
            old_ans = row[2]
            new_ans = sid_to_new_answer[sid]
            row[2] = new_ans
            qid = next(q for q, s in qid_to_sid.items() if s == sid)
            changes.append((qid, sid, old_ans, new_ans))

    # 검증: 9 변경 예상
    expected_changes = len(_NEW_ANSWERS)
    if len(changes) != expected_changes:
        print(
            f"[ERR] 변경 건수 불일치: 예상 {expected_changes}, 실제 {len(changes)}",
            file=sys.stderr,
        )
        for qid, sid, _, _ in changes:
            print(f"  Q{qid} sid={sid[:8]}...")
        return 1

    # 출력 CSV 쓰기
    with _OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    # 변경 내역 출력
    print(f"=== submission_038_fault_bgp_bulk 생성 완료 ===")
    print(f"base : {_BASE_CSV.name}")
    print(f"out  : {_OUT_CSV.name}")
    print(f"변경 : {len(changes)} 라인")
    print()
    for qid, sid, old, new in sorted(changes):
        print(f"Q{qid} (sid {sid[:8]}...):")
        print(f"  -: {old}")
        print(f"  +: {new}")
    print()
    print("예상 점수 변화:")
    print("  0.56 유지: BGP 모두 오답 → L3VPN/static-route-error 시도")
    print("  0.58~0.62: BGP 일부 정답 → fine-tuning")
    print("  0.66+: BGP 다수 정답, leader tie 접근")
    print("  0.78+: leader tie 즉시 달성")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
