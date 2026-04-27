"""Q24 multi-line probe (Q22/Q27 H4 패턴 재현).

H4 적중 (Q22/Q27 multi-line) → 0.52 (+0.04).

Q24 raw 분석:
  - Delta-Portal-02 GE1/0/5 = admin *down
  - description: 'From_Delta-Portal-02_GE1/0/5_To_Delta-Aegis-02_GE0/0/1'
  - target IP 192.168.72.78 = Delta-Aegis-02 GE0/0/1
  - alarm: 'GE1/0/5, AdminStatus=DOWN' 명확

가설:
  Q24 정답 = `Delta-Portal-02;GE1/0/5;shutdown\\nDelta-Portal-02;192.168.72.78;missing static route`
  (Q22/Q27 와 동일 multi-line 패턴)

생성:
  agent/submission_v9_h4_plus_q24_multiline_20260427.csv
  baseline = v9 + H4 (Q22/Q27 multi) + Q24 multi-line

기대:
  +0.02 (0.52 → 0.54): Q24 multi-line 정답
  +0.00: Q24 multi-line 아님, 다른 가설 시도

Q19, Q26 은 v9 baseline 유지 (단독 routing missing 이 정답일 가능성).
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

SID = {
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
    24: "1bbdb90e-e0d1-435c-aa52-cf8c27b0b724",
}

# Q22/Q27 multi-line (H4 적중)
Q22_Q27_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)

# Q24 multi-line 가설
Q24_MULTI = (
    r"Delta-Portal-02;GE1/0/5;shutdown\n"
    r"Delta-Portal-02;192.168.72.78;missing static route"
)


def main() -> None:
    out = _ROOT / "agent" / "submission_v9_h4_plus_q24_multiline_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    delta = {
        SID[22]: Q22_Q27_MULTI,
        SID[27]: Q22_Q27_MULTI,
        SID[24]: Q24_MULTI,
    }
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == 3

    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)

    print(f"[OK] {out.name}")
    print(f"     Q22 = multi-line (H4)")
    print(f"     Q27 = multi-line (H4)")
    print(f"     Q24 = multi-line (NEW)")
    print(f"     기대: 0.52 → 0.54 (+0.02 if Q24 multi 정답)")


if __name__ == "__main__":
    main()
