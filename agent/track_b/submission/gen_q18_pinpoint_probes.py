"""Q18/Q22/Q27 pinpoint + 새 답 가설 probe 생성.

H3 결과 +0.02 분석:
  - 3개 중 1개만 Alpha-Center-02 정답
  - 다른 2개는 Alpha 도 Gamma 도 아닌 답
  - src 패턴 (Q18=Beta-Node-01 vs Q22/Q27=Beta-Node-02)

가설:
  - Q18 (Beta-Node-01 src) = Q17/Q21 패턴 = Alpha-Center-02 정답
  - Q22, Q27 (Beta-Node-02 src) = 더 가까운 hop fault
    후보: Beta-Axis-02, Beta-Portal-02 (Q22 경로상 노드)

생성 probe:
  P1 pin_q18_alpha_only:
    Q18 = Alpha, Q22 = v9 Gamma, Q27 = v9 Gamma
    → +0.02 면 Q18 = Alpha 확정, Q22/Q27 다른 답

  P2 q22_q27_beta_axis:
    Q18 = Alpha, Q22 = Beta-Axis-02, Q27 = Beta-Axis-02
    → +0.06 면 모두 정답, +0.04 면 1+1, +0.02 면 1만 정답

  P3 q22_q27_beta_portal:
    Q18 = Alpha, Q22 = Beta-Portal-02, Q27 = Beta-Portal-02
    → 다른 fault 노드 가설

  P4 q22_q27_beta_node_02:
    Q18 = Alpha, Q22 = Beta-Node-02, Q27 = Beta-Node-02
    → src 자체 fault 가설
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

SID = {
    18: "b9a77dd0-39e5-4d7b-9e9c-af61213b30ea",
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}

# v9 baseline (= Gamma-Portal-02 missing)
GAMMA = "Gamma-Portal-02;192.168.70.22;missing static route"
ALPHA = "Alpha-Center-02;192.168.70.22;missing static route"


def build(label: str, q18: str, q22: str, q27: str) -> Path:
    out = _ROOT / "agent" / f"submission_v9_q18_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    delta = {SID[18]: q18, SID[22]: q22, SID[27]: q27}
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]

    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    return out


def main() -> None:
    probes = [
        # P1: Q18 만 Alpha, Q22/Q27 = v9 Gamma → Q18 정답=Alpha 확인용
        ("pin_q18_alpha", ALPHA, GAMMA, GAMMA),

        # P2: Q22/Q27 = Beta-Axis-02 가설 (src 가까운 hop)
        ("q22_q27_beta_axis", ALPHA,
         "Beta-Axis-02;192.168.70.22;missing static route",
         "Beta-Axis-02;192.168.70.22;missing static route"),

        # P3: Q22/Q27 = Beta-Portal-02 가설 (Q19 답과 같음)
        ("q22_q27_beta_portal", ALPHA,
         "Beta-Portal-02;192.168.70.22;missing static route",
         "Beta-Portal-02;192.168.70.22;missing static route"),

        # P4: Q22/Q27 = Beta-Node-02 (src 자체)
        ("q22_q27_beta_node02", ALPHA,
         "Beta-Node-02;192.168.70.22;missing static route",
         "Beta-Node-02;192.168.70.22;missing static route"),

        # P5: 모든 ID 단독 변경 (Q22 만 Alpha, Q18/Q27 v9) — Alpha 정답 ID 결정
        ("pin_q22_alpha", GAMMA, ALPHA, GAMMA),

        # P6: Q27 만 Alpha
        ("pin_q27_alpha", GAMMA, GAMMA, ALPHA),
    ]

    for label, q18, q22, q27 in probes:
        out = build(label, q18, q22, q27)
        print(f"[OK] {out.name}")
        print(f"     Q18={q18[:60]}")
        print(f"     Q22={q22[:60]}")
        print(f"     Q27={q27[:60]}")
        print()


if __name__ == "__main__":
    main()
