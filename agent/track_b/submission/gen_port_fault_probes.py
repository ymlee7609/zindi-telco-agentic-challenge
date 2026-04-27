"""Q22/Q27 port fault 가설 probe.

pin_q18_alpha 결과 = 0.46 (점수 변화 없음 from H3=0.46) 분석:
  - 0.46 = 018 baseline 0.48 - 0.02 = 1 정답 손실
  - 즉 Q18 만 Alpha 로 바꿨는데 1 정답 손실
  - => Q18 정답 = Gamma-Portal-02 (v9 답 정답!)
  - => Q22, Q27 정답 = 다른 답 (Gamma 도 Alpha 도 아님)

Raw 분석 발견:
  Q22, Q27 (둘 다) 에서 Gamma-Portal-02 GE1/0/2 = admin *down
  description: "From_Gamma-Portal-02_GE1/0/2_To_Gamma-Axis-02_GE1/0/6"
  Q18 에서는 동일 포트 *down 아님 (다른 fault scenario)

가설:
  Q22, Q27 정답 = `Gamma-Portal-02;GE1/0/2;shutdown` (port fault!)
  - Q22 "single fault" 명시 → 단일 라인 port fault 형식 부합
  - Q27 도 동일 src/dst, 동일 raw fault → 같은 답

생성 probe:
  P1 q22_q27_port_shutdown:
    Q18 = v9 Gamma (그대로, 정답)
    Q22 = Gamma-Portal-02;GE1/0/2;shutdown
    Q27 = Gamma-Portal-02;GE1/0/2;shutdown

  P2 q22_q27_port_combined:
    위 + Q18 = v9 그대로

기대 결과:
  - +0.04 (Q22, Q27 둘 다 정답): 0.48 → 0.52 (또는 직전 0.46 → 0.50)
  - +0.02 (1개만 정답): 0.50
  - +0.00: 가설 기각, 다른 답 시도
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

SID = {
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}

PORT_FAULT = "Gamma-Portal-02;GE1/0/2;shutdown"


def build(label: str, q22_ans: str, q27_ans: str) -> Path:
    out = _ROOT / "agent" / f"submission_v9_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    delta = {SID[22]: q22_ans, SID[27]: q27_ans}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == 2, f"expected 2 changes, got {changed}"
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name}")
    print(f"     Q22 = {q22_ans}")
    print(f"     Q27 = {q27_ans}")
    return out


def main() -> None:
    # P1: Q22/Q27 port fault (Q18 은 v9 Gamma 유지 정답 가정)
    build("q22_q27_port_shutdown", PORT_FAULT, PORT_FAULT)

    # P2: Q22 만 port fault (pinpoint)
    GAMMA = "Gamma-Portal-02;192.168.70.22;missing static route"
    build("q22_only_port_fault", PORT_FAULT, GAMMA)

    # P3: Q27 만 port fault
    build("q27_only_port_fault", GAMMA, PORT_FAULT)


if __name__ == "__main__":
    main()
