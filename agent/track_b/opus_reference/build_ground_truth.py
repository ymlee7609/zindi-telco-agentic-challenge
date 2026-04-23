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
    29: {"type": "TOPO", "opus": None, "conf": "MEDIUM", "notes": "PJ zone, LLDP 없음, solver 신뢰"},
    30: {"type": "TOPO", "opus": None, "conf": "MEDIUM", "notes": "PJ zone, LLDP 없음"},
    31: {"type": "TOPO", "opus": None, "conf": "MEDIUM", "notes": "PJ zone, PX1 외부 장비 포함"},
    32: {"type": "TOPO", "opus": None, "conf": "MEDIUM", "notes": "PJ zone, Eth-Trunk 기반"},
    33: {"type": "TOPO", "opus": None, "conf": "MEDIUM", "notes": "PJGFA zone, LLDP 없음"},

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
    34: {"type": "PATH", "opus": None, "conf": "MEDIUM",      "notes": "PJ intra-zone 5 hops, 대안 경로 가능성"},
    35: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH", "notes": "PJ→Node cross-zone 11 hops, Q36 과 역대칭"},
    36: {"type": "PATH", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Node→PJ cross-zone, Q35 와 역대칭"},
    37: {"type": "PATH", "opus": None, "conf": "MEDIUM",      "notes": "Node intra-zone 5 hops"},
    38: {"type": "PATH", "opus": None, "conf": "MEDIUM",      "notes": "PJ→Node-02, Q35 와 마지막 2 hop 만 다름"},

    # ---- FAULT 24 (Q17-28, Q39-50) ----
    17: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "Alpha-Center-02 routing 에 192.168.70.x 부재 (파일럿)"},
    18: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    19: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    20: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "port shutdown, interface brief 확인"},
    21: {"type": "FAULT", "opus": None, "conf": "HIGH",        "notes": "Q17 과 동일 구조"},
    22: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    23: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "Delta zone inter-zone fault"},
    24: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    25: {"type": "FAULT",
         "opus": "Alpha-Center-02;192.168.70.70;missing static route",
         "conf": "LOW",
         "notes": "solver 실패 (conf=L), baseline(Beta-Node-01;...;static route error) 은 fallback heuristic. Opus 가설 HIGH 우선순위로 실험 가치"},
    26: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "solver conf=H"},
    27: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q22 와 동일"},
    28: {"type": "FAULT",
         "opus": "Alpha-Center-02;192.168.70.93;missing static route",
         "conf": "LOW",
         "notes": "solver 실패, Q25 와 유사 가설. 실험 가치"},
    39: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "PJ zone"},
    40: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "PJ zone"},
    41: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "Q40 중복"},
    42: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "MAC alarm log 기반"},
    43: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "Q39 중복"},
    44: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Eth-Trunk shutdown"},
    45: {"type": "FAULT", "opus": None, "conf": "MEDIUM-HIGH", "notes": "Q44 와 동일 fault"},
    46: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "Q39 중복"},
    47: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "solver 일관"},
    48: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "Q47 중복"},
    49: {"type": "FAULT", "opus": None, "conf": "MEDIUM",      "notes": "solver 일관"},
    50: {"type": "FAULT",
         "opus": "Hermes-Prime-01;10.1.1.20;missing static route",
         "conf": "LOW",
         "notes": "solver 실패, baseline(...;ARP configuration error) fallback. PJ zone context 부족"},
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
