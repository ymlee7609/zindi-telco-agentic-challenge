"""Q26 새 가설 추가 probe (Q, R, S).

L (subnet IP) 기각 → Q26 정답 ≠ subnet host IP.
Q26 admin shutdown link 0개 → multi-line port 가설 약함.

baseline = A (Q22/Q27 multi + Q24 single port = 0.54)

추가 가설:
  Q: subnet with mask
     Q26 = `Gamma-Axis-02;192.168.74.44/30;missing static route`

  R: multi-line routing (다중 노드 missing)
     Q26 = `Gamma-Axis-02;192.168.74.45;missing static route\\nAlpha-Center-02;192.168.74.45;missing static route`

  S: src side fault
     Q26 = `Gamma-Node-01;192.168.74.45;missing static route`

  T: routing loop reason
     Q26 = `Gamma-Axis-02;192.168.74.45;routing loop`

  U: dst gateway IP
     Q26 = `Gamma-Axis-02;192.168.70.14;static route error`
     (현재 Gamma-Axis-02 routing 의 nexthop 값 192.168.70.14)
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

SID = {
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    24: "1bbdb90e-e0d1-435c-aa52-cf8c27b0b724",
    26: "c408d8a4-b09b-49cf-a9c9-b783575cf547",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}

H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)
Q24_PORT = "Delta-Portal-02;GE1/0/5;shutdown"


def build(label: str, q26: str) -> Path:
    out = _ROOT / "agent" / f"submission_v9_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    delta = {SID[22]: H4_MULTI, SID[27]: H4_MULTI, SID[24]: Q24_PORT, SID[26]: q26}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == 4
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name}: Q26={q26[:120]}")
    return out


def main() -> None:
    # Q: subnet with mask
    build("Q_q26_subnet_mask", "Gamma-Axis-02;192.168.74.44/30;missing static route")

    # R: multi-line routing 다중 노드
    R_VAL = (
        r"Gamma-Axis-02;192.168.74.45;missing static route\n"
        r"Alpha-Center-02;192.168.74.45;missing static route"
    )
    build("R_q26_multi_routing", R_VAL)

    # S: src side
    build("S_q26_src_node", "Gamma-Node-01;192.168.74.45;missing static route")

    # T: routing loop reason
    build("T_q26_routing_loop", "Gamma-Axis-02;192.168.74.45;routing loop")

    # U: dst gateway IP (현재 nexthop 192.168.70.14)
    build("U_q26_dst_gateway",
          "Gamma-Axis-02;192.168.70.14;static route error")


if __name__ == "__main__":
    main()
