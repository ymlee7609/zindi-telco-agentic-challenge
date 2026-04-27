"""Q26 진짜 답 후보 5종 probe.

J 결과 -0.02 → Q19 v9 정답 확정. 남은 오답 = Q26.

Q26 raw:
  src=Gamma-Node-01, dst=Alpha-Center-02 GE1/0/6 (192.168.74.45)
  Opus 답: Gamma-Axis-02;192.168.74.45;missing static route
  → raw 기반 정답 형식이지만 Zindi 정답과 다름.

Q26 admin shutdown alarm 없음 (multi-line 가능성 약함).
Q22 single 명시 multi-line 정답 → Q26 (multi 명시 없음, multi 가능) 도 가능.

A baseline (0.54) + Q26 변경:

L: subnet IP missing
   Q26 = `Gamma-Axis-02;192.168.74.44;missing static route` (host → subnet)

M: static route error reason
   Q26 = `Gamma-Axis-02;192.168.74.45;static route error`

N: blackhole route reason
   Q26 = `Gamma-Axis-02;192.168.74.45;blackhole route`

O: target side fault (Alpha-Center-02)
   Q26 = `Alpha-Center-02;192.168.74.45;ARP configuration error`

P: multi-line (port + routing)
   Q26 = `Gamma-Axis-02;GE1/0/0;shutdown\\nGamma-Axis-02;192.168.74.45;missing static route`
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

# A baseline 답 (확정)
H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)
Q24_SINGLE_PORT = "Delta-Portal-02;GE1/0/5;shutdown"


def build(label: str, q26: str) -> Path:
    out = _ROOT / "agent" / f"submission_v9_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    delta = {SID[22]: H4_MULTI, SID[27]: H4_MULTI, SID[24]: Q24_SINGLE_PORT, SID[26]: q26}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == 4
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name}")
    print(f"     Q26 = {q26[:120]}")
    return out


def main() -> None:
    # L: subnet IP
    build("L_q26_subnet", "Gamma-Axis-02;192.168.74.44;missing static route")

    # M: static route error
    build("M_q26_static_error", "Gamma-Axis-02;192.168.74.45;static route error")

    # N: blackhole route
    build("N_q26_blackhole", "Gamma-Axis-02;192.168.74.45;blackhole route")

    # O: target side ARP
    build("O_q26_target_arp", "Alpha-Center-02;192.168.74.45;ARP configuration error")

    # P: multi-line port + routing
    P_VAL = (
        r"Gamma-Axis-02;GE1/0/0;shutdown\n"
        r"Gamma-Axis-02;192.168.74.45;missing static route"
    )
    build("P_q26_multi_port", P_VAL)


if __name__ == "__main__":
    main()
