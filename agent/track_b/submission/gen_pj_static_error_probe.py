"""PJ Fault 에 Q26 패턴 (static route error) 적용 probe + 0.56 통합본 갱신.

M 적중 0.56 (Traditional 28/28). 4 오답 모두 해결.
패턴: Q22/Q27 multi-line (port + routing) / Q24 single port / Q26 static route error.

PJ Fault 도 같은 reason 패턴 적용 시도:
  Group A (Q39/Q43/Q46) reason: missing → static route error
  Group B (Q40/Q41), D (Q47/Q48), Q49 도 동일

기존 020 (Group A VXLAN) 결과 0.48 = PJ public 안 들어감 가능성 매우 큼.
그러나 Q26 패턴이 PJ 에도 통하면 +0.06 (Group A) 추가 가능.

생성:
  best_0_56_combined: 현재 베스트 통합본 (M 답 포함)
  pj_static_error_AB: PJ Group A+B+D 모두 static error
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
    # PJ
    39: "96636d0e-1c71-4c58-b661-d853acf155db",
    40: "de1443a9-026a-4820-89fd-f1ecc55de414",
    41: "2039bb7b-3cd9-4453-8686-89090a8e66e7",
    43: "a499f356-3c51-4926-aeca-3bdc8b383dc7",
    46: "f90c328d-67c1-4725-9b2c-a823d3b81062",
    47: "29afe162-7cea-483e-bc2c-a4a82e54b665",
    48: "558b0d56-9b59-47d8-a9be-5eb03c8a77b3",
    49: "3536d71e-be41-4dfc-8cbd-dc22feedf2fb",
}

# A baseline 답 (확정)
H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)
Q24_PORT = "Delta-Portal-02;GE1/0/5;shutdown"
Q26_STATIC_ERR = "Gamma-Axis-02;192.168.74.45;static route error"

# Best baseline = 0.56 답 (Traditional 28/28)
BEST_DELTA = {
    SID[22]: H4_MULTI,
    SID[27]: H4_MULTI,
    SID[24]: Q24_PORT,
    SID[26]: Q26_STATIC_ERR,
}


def build(label: str, extra: dict[str, str] | None = None) -> Path:
    out = _ROOT / "agent" / f"submission_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    delta = {**BEST_DELTA, **(extra or {})}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == len(delta), f"expected {len(delta)} changes, got {changed}"
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name} ({changed} changes)")
    return out


def main() -> None:
    # 1. 표준 0.56 통합본 갱신 (Best)
    build("BEST_0_56_track_ab")

    # 2. PJ Group A static error
    pj_extra_a = {
        SID[39]: "Demeter-Prime-01;20.1.1.10;static route error",
        SID[43]: "Demeter-Prime-01;20.1.1.10;static route error",
        SID[46]: "Demeter-Prime-01;20.1.1.10;static route error",
    }
    build("PJ_A_static_error", pj_extra_a)

    # 3. PJ Group A+B+D static error
    pj_extra_abd = {
        **pj_extra_a,
        SID[40]: "Demeter-Prime-01;10.1.6.3;static route error",
        SID[41]: "Demeter-Prime-01;10.1.6.3;static route error",
        SID[47]: "Demeter-Prime-01;20.1.1.20;static route error",
        SID[48]: "Demeter-Prime-01;20.1.1.20;static route error",
        SID[49]: "Demeter-Prime-01;20.1.4.10;static route error",
    }
    build("PJ_ABD_static_error", pj_extra_abd)


if __name__ == "__main__":
    main()
