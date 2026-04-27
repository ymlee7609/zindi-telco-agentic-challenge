"""Q24 진짜 정답 + Q19/Q26 v9 정답 검증 probe.

H4+Q24_multi 결과 0.52 (변동 없음) → Q24 정답 ≠ multi-line, ≠ v9 missing.
Q19/Q26 fault node 에 admin *down link 없음 → v9 정답 가능성 큼.
4 오답 = Q22 + Q27 (해결) + Q24 + Q19/Q26 중 1.

생성 probe:

A. q24_single_port_only
   Q22/Q27 multi (H4) + Q24 single port fault only
   Q24 = `Delta-Portal-02;GE1/0/5;shutdown`

B. q24_target_side_port
   Q22/Q27 multi + Q24 = target side port fault
   Q24 = `Delta-Aegis-02;GE0/0/1;shutdown`

C. q24_target_arp
   Q22/Q27 multi + Q24 = target ARP fault
   Q24 = `Delta-Aegis-02;192.168.72.78;ARP configuration error`

D. q24_3line_multi
   Q22/Q27 multi + Q24 = 3-line multi-fault
   Q24 = port + routing + alpha-center routing

E. test_q19_change (검증용)
   Q22/Q27 multi + Q19 = multi-line variant
   Q19 = `Beta-Portal-02;GE1/0/5;shutdown\\nBeta-Portal-02;192.168.70.22;missing static route`
   - 만약 -0.02 → Q19 v9 = 정답 확정, multi 변경이 손실 유발
   - 만약 0 → Q19 v9 = 오답 (multi 도 오답)

F. test_q26_change
   Q22/Q27 multi + Q26 변경 (v9 정답 검증)
   Q26 = different reason
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

SID = {
    19: "674afa1d-ae0d-4a52-81d7-b391efbd2414",
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    24: "1bbdb90e-e0d1-435c-aa52-cf8c27b0b724",
    26: "c408d8a4-b09b-49cf-a9c9-b783575cf547",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}

H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)


def build(label: str, deltas: dict[int, str]) -> Path:
    out = _ROOT / "agent" / f"submission_v9_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    sid_delta = {SID[q]: v for q, v in deltas.items()}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in sid_delta:
            r[2] = sid_delta[r[0]]
            changed += 1
    assert changed == len(sid_delta)
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name}")
    return out


def main() -> None:
    BASE = {22: H4_MULTI, 27: H4_MULTI}

    # A: Q24 single port fault
    build("A_q24_single_port", {**BASE, 24: "Delta-Portal-02;GE1/0/5;shutdown"})

    # B: Q24 target side port (GE0/0/1)
    build("B_q24_target_port", {**BASE, 24: "Delta-Aegis-02;GE0/0/1;shutdown"})

    # C: Q24 target ARP
    build("C_q24_target_arp",
          {**BASE, 24: "Delta-Aegis-02;192.168.72.78;ARP configuration error"})

    # D: Q24 3-line multi (port + routing + Alpha-Center-02)
    D_VAL = (
        r"Delta-Portal-02;GE1/0/5;shutdown\n"
        r"Delta-Portal-02;192.168.72.78;missing static route\n"
        r"Alpha-Center-02;192.168.72.78;missing static route"
    )
    build("D_q24_3line", {**BASE, 24: D_VAL})

    # E: Q19 multi-line variant (검증용)
    E_VAL = (
        r"Beta-Portal-02;GE1/0/5;shutdown\n"
        r"Beta-Portal-02;192.168.70.22;missing static route"
    )
    build("E_q19_multi_test", {**BASE, 19: E_VAL})

    # F: Q26 multi-line variant
    F_VAL = (
        r"Gamma-Axis-02;GE1/0/2;shutdown\n"
        r"Gamma-Axis-02;192.168.74.45;missing static route"
    )
    build("F_q26_multi_test", {**BASE, 26: F_VAL})


if __name__ == "__main__":
    main()
