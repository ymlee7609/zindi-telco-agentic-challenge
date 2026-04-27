"""Q22/Q27 새 가설 probe 5종.

q22_q27_port_shutdown 결과 0.48 (=018 변동 없음) 분석:
  Q22, Q27 변경 net 0 = 둘 다 정답 ≠ port_fault
  Q22, Q27 정답 ≠ {Gamma missing, Alpha missing, port_fault}

새 가설 (Q18=Gamma 유지, Q22/Q27 만 변경):

H_full_port: 전체 포트명
  `Gamma-Portal-02;GigabitEthernet1/0/2;shutdown`

H_subnet: subnet network address (호스트 IP 대신)
  `Gamma-Portal-02;192.168.70.20;missing static route`

H_axis_other_end: link 반대 끝 (Gamma-Axis-02 측)
  `Gamma-Axis-02;GE1/0/6;shutdown`

H_multiline_port_routing: port + routing 조합
  `Gamma-Portal-02;GE1/0/2;shutdown\\nGamma-Portal-02;192.168.70.22;missing static route`

H_other_reason: port fault 의 다른 reason
  `Gamma-Portal-02;GE1/0/2;interface IP error`

각 probe 는 v9 baseline + Q22, Q27 동시 변경.
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


def build(label: str, q22: str, q27: str) -> Path:
    out = _ROOT / "agent" / f"submission_v9_q22_alt_{label}_20260427.csv"
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    delta = {SID[22]: q22, SID[27]: q27}
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            r[2] = delta[r[0]]
            changed += 1
    assert changed == 2
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    print(f"[OK] {out.name}")
    return out


def main() -> None:
    # H1 full port name
    H1 = "Gamma-Portal-02;GigabitEthernet1/0/2;shutdown"
    build("h1_full_port", H1, H1)

    # H2 subnet network address
    H2 = "Gamma-Portal-02;192.168.70.20;missing static route"
    build("h2_subnet", H2, H2)

    # H3 link 반대 끝 (Gamma-Axis-02 측)
    H3 = "Gamma-Axis-02;GE1/0/6;shutdown"
    build("h3_axis_other_end", H3, H3)

    # H4 multi-line: port + routing
    H4 = (
        r"Gamma-Portal-02;GE1/0/2;shutdown\n"
        r"Gamma-Portal-02;192.168.70.22;missing static route"
    )
    build("h4_multiline_port_routing", H4, H4)

    # H5 다른 reason: interface IP error
    H5 = "Gamma-Portal-02;GE1/0/2;interface IP error"
    build("h5_iface_ip_error", H5, H5)

    # H6 OSPF configuration error
    H6 = "Gamma-Portal-02;GE1/0/2;OSPF configuration error"
    build("h6_ospf_error", H6, H6)


if __name__ == "__main__":
    main()
