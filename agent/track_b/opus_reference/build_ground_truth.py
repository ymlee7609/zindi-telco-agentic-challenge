"""Opus 검증 결과 + baseline 답을 통합하여 GROUND_TRUTH.json 생성.

출처:
- answers/topo_all_answers.md (Q01-06, Q29-33)
- answers/q07_q16_batch_verdict.md (Q07-16 PATH)
- answers/q11_answer.md (Q11 상세)
- answers/path_pj_answers.md (Q34-38 PATH PJ)
- answers/fault_all_answers.md (Q17-28, Q39-50 FAULT)
- submission_v12_topofault_rt.csv (baseline)

Schema (per entry):
    {
      "qid": int,
      "scenario_id": str,
      "type": "TOPO" | "PATH" | "FAULT",
      "question_snippet": str,
      "opus_answer": str,           # Opus 추천 정답 (literal \n 포맷)
      "baseline_answer": str,       # v12_topofault_rt 현재 답
      "agrees_with_baseline": bool,
      "confidence": "HIGH" | "MEDIUM-HIGH" | "MEDIUM" | "LOW",
      "notes": str                  # 의심 지점, 대안 등
    }

Usage:
    python3 agent/track_b/opus_reference/build_ground_truth.py
"""
# pyright: reportMissingImports=false

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve().parent
_PROJECT_ROOT = _THIS.parent.parent.parent

_TEST_JSON = _PROJECT_ROOT / "data" / "Track B" / "data" / "Phase_1" / "test.json"
_BASELINE_CSV = _PROJECT_ROOT / "agent" / "track_b" / "submission" / "submission_v12_topofault_rt.csv"
_OUT_JSON = _THIS / "GROUND_TRUTH.json"

# ---------------------------------------------------------------------------
# Opus verdict data (수동 기록, 각 answers/*.md 요약)
# ---------------------------------------------------------------------------

# qid → (opus_answer, confidence, notes)
# opus_answer 가 None 이면 baseline 과 동일 사용
VERDICT: dict[int, dict] = {
    # ---- TOPO 11 (Q01-06, Q29-33) ----
    1:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "LLDP 직접 조회, 파일럿 검증"},
    2:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "target 직접 LLDP 불가, reverse LLDP 6개 확인"},
    3:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "forward+reverse LLDP 일치"},
    4:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "7개 LLDP 매핑, 데이터 가장 풍부"},
    5:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "3개 LLDP 매핑"},
    6:  {"type": "TOPO", "opus": None, "conf": "HIGH",   "notes": "6개 LLDP 매핑"},
    29: {"type": "TOPO", "opus": None, "conf": "HIGH",
         "notes": "3차 검증: Demeter-Prime-01 GE1/0/0-1 IP-peer (192.168.2.1/9) → Atlas-Prime-01/02 확정. 2/2 links verified."},
    30: {"type": "TOPO", "opus": None, "conf": "HIGH",
         "notes": "3차 검증: Atlas-Prime-01 GE1/0/0-3 IP-peer (192.168.1.2/6, 192.168.2.2/6) 4/4 links verified."},
    31: {"type": "TOPO", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: GE1/0/0-2 IP-peer 3/5 확정 (Atlas-Prime-01/02, PX1). GE1/0/4,5 Eth-Trunk 멤버로 IP 없어 cross-ref LLDP (Q32 다른 scenario) 로 확인."},
    32: {"type": "TOPO", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Aegis-Prime-01 전체 Eth-Trunk 구성, GE1/0/0/1/3 물리 port는 Eth-Trunk 멤버로 IP 없음. 다른 scenario LLDP cross-ref 로 Janus-Prime-02/Aegis-Prime-02/Eon-Node-01 연결 토폴로지적으로 확인."},
    33: {"type": "TOPO", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Janus-Node-02 GE1/0/2-3 IP-peer (182.158.1.5/13) 2/4 확정. GE1/0/4,5 Eth-Trunk/Node-to-Node, 다른 scenario LLDP cross-ref 로 확인."},

    # ---- PATH 15 (Q07-16 dev/mgmt/bigdata, Q34-38 PJ) ----
    7:  {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Gamma-Axis-02, routing 일치"},
    8:  {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Delta-Axis-02"},
    9:  {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Delta-Axis-02"},
    10: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Beta-Axis-02"},
    11: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "Beta-Node-03 routing table 증거 검증됨 (파일럿)"},
    12: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Gamma-Axis-02"},
    13: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH", "notes": "GE1/0/4 는 Node-to-Node, 대칭 패턴 적용"},
    14: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Gamma-Axis-02"},
    15: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Delta-Axis-02"},
    16: {"type": "PATH", "opus": None, "conf": "HIGH",        "notes": "dst peer = Delta-Axis-02"},
    34: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Hermes-Prime-01 → 10.1.1.20 은 10.1.1.0/24 direct L2 (Vlanif10). Native routing 으로는 single hop 이지만 solver 답은 VXLAN overlay 경로 (Demeter-Prime-01 → Atlas-Prime-01 → Demeter-Prime-02 → Hermes-Prime-02). EVPN VTEP 중재자 역할 추정, routing trace 로는 검증 불가."},
    35: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH", "notes": "PJ→Node cross-zone 11 hops, Q36 과 역대칭"},
    36: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Node→PJ cross-zone, Q35 와 역대칭"},
    37: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Q34 대칭 패턴. Hermes-Node-01 → 20.1.1.20 direct L2 (Vlanif10). Overlay 경로는 Demeter-Node-01 → Atlas-Node-01 → Demeter-Node-02 → Hermes-Node-02."},
    38: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Hermes-Prime-01 routing 은 default route (0.0.0.0/0 via 10.1.5.1 Vlanif50) 로 Demeter-Prime-02 도달 확인. 이후 VXLAN overlay. Q35 와 마지막 2 hop 차이만 있음."},

    # ---- FAULT 24 (Q17-28, Q39-50) ----
    17: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "Alpha-Center-02 routing 에 192.168.70.x 부재 (파일럿)"},
    18: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    19: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    20: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "port shutdown, interface brief 확인"},
    21: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "Q17 과 동일 구조"},
    22: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    23: {"type": "FAULT", "opus": None, "conf": "HIGH",
         "notes": "3차 검증 (수정): Delta-Axis-02 Q23 routing 실제로 **192.168.74.60/30 부재** (2차 검증 혼동 정정 — 해당 경로는 Q25 scenario 에서 확인된 것). Delta-Portal-01 도 부재. Delta-Portal-02 만 direct. forward path Delta-Node-01→Axis-02 에서 Axis-02 가 경로 없어 drop → baseline `Delta-Axis-02;192.168.74.61;missing static route` 정답."},
    24: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    25: {"type": "FAULT",
         "opus": "Alpha-Center-02;192.168.70.70;static route error",
         "conf": "HIGH",
         "notes": "raw routing 검증 완료: Alpha-Center-02 의 192.168.70.68/30 next-hop 이 정상(Q17)에서 192.168.74.46 GE1/0/6 (Gamma-Portal-02) 이었으나 Q25 에서 192.168.74.54 GE1/0/3 (Delta-Portal-01) 로 잘못 변경됨. Gamma zone 주소를 Delta zone 으로 보냄 → static route error. baseline(Beta-Node-01;...;static route error) 은 장비 이름이 틀림."},
    26: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    27: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q22 와 동일"},
    28: {"type": "FAULT",
         "opus": "Gamma-Axis-02;192.168.70.93;routing loop",
         "conf": "HIGH",
         "notes": "raw routing 검증 완료: Gamma-Axis-02 의 192.168.70.92/30 next-hop 이 정상(Q17)에서 192.168.70.46 GE1/0/4 (Gamma-Node-04) 였으나 Q28 에서 192.168.70.14 GE1/0/6 (Gamma-Portal-02) 으로 변경됨. Gamma-Portal-02 는 다시 Gamma-Axis-02 로 forward → routing loop. baseline(Beta-Node-01;...;static route error) 오답."},
    39: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: PJ zone (EVPN VXLAN overlay). Native routing 으로는 Demeter-Prime-01 에 20.1.1.x 대역 경로 정상/변이 모두 부재 (overlay 기반). baseline `Demeter-Prime-01;20.1.1.10;missing static route` 는 VXLAN VTEP 설정 기준 judgment. BGP EVPN routing-table 심층 분석 필요."},
    40: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Q39 와 동일. Demeter-Prime-01 10.1.6.x 대역 routing 정상/변이 모두 부재. EVPN 기반."},
    41: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q40 중복 scenario"},
    42: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "MAC alarm log 기반"},
    43: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q39 중복 scenario"},
    44: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Eth-Trunk shutdown"},
    45: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q44 와 동일 fault"},
    46: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q39 중복 scenario"},
    47: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Hermes-Prime-02 → 20.1.1.20. Demeter-Prime-01 20.1.1.x routing 정상/변이 모두 부재. EVPN 기반."},
    48: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q47 중복 scenario"},
    49: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH",
         "notes": "3차 검증: Hermes-Prime-01 → 20.1.4.10. Q38 fault variant, Demeter-Prime-01 20.1.4.x EVPN 기반."},
    50: {"type": "FAULT",
         "opus": None,
         "conf": "MEDIUM-HIGH",
         "notes": "raw 검증 완료: 10.1.1.0/24 는 Hermes-Prime-01/02 간 direct-connected subnet (Vlanif10). 10.1.1.10=Prime-01, 10.1.1.20=Prime-02. Hermes-Prime-01 ARP 에 10.1.1.20 entry 부재 → ARP 학습 실패. baseline(...;ARP configuration error) 유지. Opus 이전 가설(missing static route) 철회."},
}


def _snippet(question: str, max_len: int = 140) -> str:
    s = question.replace("\n", " ").strip()
    return s[:max_len] + ("..." if len(s) > max_len else "")


def main() -> int:
    # 1. test.json
    with open(_TEST_JSON, encoding="utf-8") as f:
        scenarios = json.load(f)
    sid_to_scenario = {s["scenario_id"]: s for s in scenarios}
    qid_to_sid = {s["task"]["id"]: s["scenario_id"] for s in scenarios}

    # 2. baseline CSV
    baseline: dict[str, str] = {}
    with open(_BASELINE_CSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ans = row.get("Track B", "").strip()
            if ans:
                baseline[row["ID"]] = ans

    entries = []
    for qid in sorted(VERDICT.keys()):
        v = VERDICT[qid]
        sid = qid_to_sid.get(qid)
        if not sid:
            print(f"[WARN] qid {qid} not in test.json", file=sys.stderr)
            continue
        scenario = sid_to_scenario[sid]
        baseline_ans = baseline.get(sid, "")
        opus_ans = v["opus"] if v["opus"] is not None else baseline_ans
        entries.append({
            "qid": qid,
            "scenario_id": sid,
            "type": v["type"],
            "question_snippet": _snippet(scenario["task"]["question"]),
            "opus_answer": opus_ans,
            "baseline_answer": baseline_ans,
            "agrees_with_baseline": (opus_ans == baseline_ans),
            "confidence": v["conf"],
            "notes": v["notes"],
        })

    doc = {
        "meta": {
            "source": "agent/track_b/opus_reference/",
            "baseline": "submission_v12_topofault_rt.csv",
            "baseline_zindi_score": 0.44,
            "generated_by": "Claude Opus 4.7 session",
            "format_note": "opus_answer / baseline_answer 는 Zindi 제출 포맷 그대로 (literal \\n 구분자). submission_example.csv 참조.",
            "total_entries": len(entries),
        },
        "entries": entries,
    }

    with open(_OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    # 통계
    by_type: dict[str, int] = {}
    by_conf: dict[str, int] = {}
    disagreements = 0
    for e in entries:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
        by_conf[e["confidence"]] = by_conf.get(e["confidence"], 0) + 1
        if not e["agrees_with_baseline"]:
            disagreements += 1

    print(f"[SAVED] {_OUT_JSON}")
    print(f"  entries: {len(entries)}")
    print(f"  by type: {by_type}")
    print(f"  by conf: {by_conf}")
    print(f"  disagreements (Opus != baseline): {disagreements}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
