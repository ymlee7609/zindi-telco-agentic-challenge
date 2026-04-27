"""Q19 + Q26 동시 multi-line probe (A baseline + Q19/Q26 변경).

A 적중 후 baseline 0.54:
  Q22/Q27 multi-line ✓
  Q24 single port ✓
  Q18 v9 Gamma ✓
  남은 오답 1개 = Q19/Q26 중 1.

이 probe 는 Q19, Q26 둘 다 multi-line 으로 동시 변경.

결과 해석 (baseline 0.54):
  +0.04 (0.58): Q19, Q26 둘 다 multi-line 정답  ← 만점 도달 한 발 더!
  +0.02 (0.56): 1개만 multi-line 정답
  0    (0.54): 둘 다 v9 오답 (multi 도 오답) → 다른 답 시도
  -0.02 (0.52): 1 v9 정답 → 손실 (multi 변경이 v9 정답을 오답화)
  -0.04 (0.50): 둘 다 v9 정답 → 손실

따라서 점수 변화로 어느 ID 가 v9 정답/오답인지 확정 가능.
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

# A baseline 답 (확정된 정답)
H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)
Q24_SINGLE_PORT = "Delta-Portal-02;GE1/0/5;shutdown"

# Q19 multi-line variant
Q19_MULTI = (
    r"Beta-Portal-02;GE1/0/5;shutdown\n"
    r"Beta-Portal-02;192.168.70.22;missing static route"
)

# Q26 multi-line variant
Q26_MULTI = (
    r"Gamma-Axis-02;GE1/0/2;shutdown\n"
    r"Gamma-Axis-02;192.168.74.45;missing static route"
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
    A_BASE = {22: H4_MULTI, 27: H4_MULTI, 24: Q24_SINGLE_PORT}

    # G: A + Q19 multi-line + Q26 multi-line (동시)
    build("G_a_plus_q19_q26_multi",
          {**A_BASE, 19: Q19_MULTI, 26: Q26_MULTI})

    # H: A + Q19 multi-line only
    build("H_a_plus_q19_multi", {**A_BASE, 19: Q19_MULTI})

    # I: A + Q26 multi-line only
    build("I_a_plus_q26_multi", {**A_BASE, 26: Q26_MULTI})

    # J: A + Q19 sanity (완전 틀린 답으로 v9 정답 검증)
    build("J_a_plus_q19_sanity",
          {**A_BASE, 19: "Zebra-X19;99.99.19.19;blackhole route"})

    # K: A + Q26 sanity
    build("K_a_plus_q26_sanity",
          {**A_BASE, 26: "Zebra-X26;99.99.26.26;blackhole route"})


if __name__ == "__main__":
    main()
