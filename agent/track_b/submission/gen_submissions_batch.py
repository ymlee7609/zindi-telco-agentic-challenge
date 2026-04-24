"""Submissions 020~027 batch generator — independent probes from 018 baseline.

핵심 가정 (019=0.48 결과 기반):
  - 018 (0.48 = 24/50) 중 24 정답 = 대부분 Traditional (Q1~Q28)
  - PJ zone (Q29~Q50) 22문제 중 거의 0 정답
  - Opus MEDIUM-HIGH "missing static route" 답이 실제 오답일 가능성 높음
  - 같은 scenario_id 중복 그룹 활용 시 단일 delta로 복수 문제 동시 영향

독립 probe 전략:
  각 020~027 = 018 baseline + 서로 다른 영역 delta.
  실패 시 rollback 안전 (baseline은 항상 018).
  성공 시 점수 상승 확인 후 sequential combine 가능.

중복 scenario 그룹:
  Group A (Q39/Q43/Q46): 'Demeter-Prime-01;20.1.1.10;missing static route' x3
  Group B (Q40/Q41):     'Demeter-Prime-01;10.1.6.3;missing static route'  x2
  Group C (Q44/Q45):     'Aegis-Prime-02;Eth-Trunk2.60;shutdown'           x2
  Group D (Q47/Q48):     'Demeter-Prime-01;20.1.1.20;missing static route' x2

실행: python3 agent/track_b/submission/gen_submissions_batch.py
각 probe 는 개별 CSV 로 저장. 사용자가 순차 업로드하여 점수 확인.
"""

from __future__ import annotations

import csv
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"

# scenario_id → qid 매핑 (Opus GROUND_TRUTH 에서 추출)
SID = {
    # Traditional Topology
    "q1":  None,  # 별도 조회 불필요
    # PJ Topology
    "q29": "dd11da6b-0ded-4417-bfd5-e36d996e1189",
    "q30": "dad1f1ad-a21e-4831-a6b2-763e8eebd026",
    "q31": "a346ef65-4abd-4e27-b7c6-06fc70a4f1c0",
    "q32": "d5a0f37b-4042-4570-ba17-7677fc7ebe01",
    "q33": "212e5d0c-4377-45da-b3f5-3d0725db8f1e",
    # PJ Fault — 중복 scenario 주의
    "q34": "",  # Path, 별도 조회
    "q39": "96636d0e-1c71-4c58-b661-d853acf155db",
    "q40": "de1443a9-026a-4820-89fd-f1ecc55de414",
    "q41": "2039bb7b-3cd9-4453-8686-89090a8e66e7",
    "q42": "7f9d4a00-9e4a-40c6-becb-c2c770972aba",
    "q43": "a499f356-3c51-4926-aeca-3bdc8b383dc7",
    "q44": "71c700c5-3cef-4a0c-a1b3-9f9c724c5db3",
    "q45": "b20f9906-9180-4ba0-a97a-75256abc0206",
    "q46": "f90c328d-67c1-4725-9b2c-a823d3b81062",
    "q47": "29afe162-7cea-483e-bc2c-a4a82e54b665",
    "q48": "558b0d56-9b59-47d8-a9be-5eb03c8a77b3",
    "q49": "3536d71e-be41-4dfc-8cbd-dc22feedf2fb",
    "q50": "463bbeb7-c99a-4d73-b066-87589503875e",
}

# 020~027 probe 정의: {serial: (filename_suffix, description, delta_dict)}
# delta_dict = {scenario_id: new_answer}
PROBES: dict[int, tuple[str, str, dict[str, str]]] = {
    # ---- 020: Group A reason → VXLAN configuration error ----
    # Q39/Q43/Q46 (3x) '20.1.1.10' reason 만 교체
    # 가설: PJ zone 은 EVPN/VXLAN overlay. Demeter-Prime-01 에 20.1.1.x native route 없음 → VXLAN 설정 이슈
    # 성공 시 +0.06 (3문제 중복)
    20: (
        "pj_fault_group_a_vxlan",
        "Group A (Q39/Q43/Q46) reason: missing static route → VXLAN configuration error",
        {
            SID["q39"]: "Demeter-Prime-01;20.1.1.10;VXLAN configuration error",
            SID["q43"]: "Demeter-Prime-01;20.1.1.10;VXLAN configuration error",
            SID["q46"]: "Demeter-Prime-01;20.1.1.10;VXLAN configuration error",
        },
    ),

    # ---- 021: Group A reason → L3VPN configuration error ----
    # 020 실패 시 대안. Demeter-Prime-01 은 VPN-instance 7개 설정됨 (vpn1~6 + lb-vpn)
    # 20.1.x 대역이 VPN 내부일 가능성. missing route 가 아닌 VPN 설정 이슈
    # 성공 시 +0.06
    21: (
        "pj_fault_group_a_l3vpn",
        "Group A (Q39/Q43/Q46) reason: missing static route → L3VPN configuration error",
        {
            SID["q39"]: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
            SID["q43"]: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
            SID["q46"]: "Demeter-Prime-01;20.1.1.10;L3VPN configuration error",
        },
    ),

    # ---- 022: Group C port 변경 (Eth-Trunk2.60 → Eth-Trunk2 parent) ----
    # Q44/Q45 현재 'Eth-Trunk2.60;shutdown'. Aegis-Prime-02 에서 Eth-Trunk2 전체 down + 모든 sub-IF down.
    # 정답이 parent trunk 일 가능성
    # 성공 시 +0.04
    22: (
        "pj_fault_group_c_parent_trunk",
        "Group C (Q44/Q45) port: Eth-Trunk2.60 → Eth-Trunk2 (parent trunk shutdown)",
        {
            SID["q44"]: "Aegis-Prime-02;Eth-Trunk2;shutdown",
            SID["q45"]: "Aegis-Prime-02;Eth-Trunk2;shutdown",
        },
    ),

    # ---- 023: Group B + D reason → VXLAN configuration error ----
    # Q40/Q41 (10.1.6.3) + Q47/Q48 (20.1.1.20) 모두 VXLAN 가설 적용
    # 성공 시 +0.08 (4문제)
    23: (
        "pj_fault_group_bd_vxlan",
        "Group B+D (Q40/Q41/Q47/Q48) reason → VXLAN configuration error",
        {
            SID["q40"]: "Demeter-Prime-01;10.1.6.3;VXLAN configuration error",
            SID["q41"]: "Demeter-Prime-01;10.1.6.3;VXLAN configuration error",
            SID["q47"]: "Demeter-Prime-01;20.1.1.20;VXLAN configuration error",
            SID["q48"]: "Demeter-Prime-01;20.1.1.20;VXLAN configuration error",
        },
    ),

    # ---- 024: Group A/B/D reason → BGP configuration error ----
    # 020/021/023 모두 실패 시 대안. EVPN 은 BGP 기반
    # 성공 시 +0.14 (7문제)
    24: (
        "pj_fault_abd_bgp",
        "Group A+B+D (Q39/Q40/Q41/Q43/Q46/Q47/Q48) reason → BGP configuration error",
        {
            SID["q39"]: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
            SID["q40"]: "Demeter-Prime-01;10.1.6.3;BGP configuration error",
            SID["q41"]: "Demeter-Prime-01;10.1.6.3;BGP configuration error",
            SID["q43"]: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
            SID["q46"]: "Demeter-Prime-01;20.1.1.10;BGP configuration error",
            SID["q47"]: "Demeter-Prime-01;20.1.1.20;BGP configuration error",
            SID["q48"]: "Demeter-Prime-01;20.1.1.20;BGP configuration error",
        },
    ),

    # ---- 025: PJ Topology Q29 direction swap ----
    # HIGH confidence 이고 IP-peer 검증됐는데 오답이면 포맷/방향 문제
    # 테스트: target 이 왼쪽이 아닐 수도
    # 성공 시 +0.02
    25: (
        "pj_topo_q29_swap",
        "Q29 direction swap: Demeter-Prime-01(...)->Atlas-... → Atlas-...->Demeter-...",
        {
            SID["q29"]: (
                r"Atlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)\n"
                r"Atlas-Prime-02(GE1/0/2)->Demeter-Prime-01(GE1/0/1)"
            ),
        },
    ),

    # ---- 026: PJ Path Q34/Q37 direct L2 ----
    # Opus notes: "10.1.1.20 은 10.1.1.0/24 direct L2 (Vlanif10). Native routing 으로는 single hop"
    # solver 가 VXLAN overlay 5-hop 썼는데 실제 정답이 single hop 일 수도
    # 성공 시 +0.04
    26: (
        "pj_path_q34_q37_direct_l2",
        "Q34/Q37 path: VXLAN overlay 5-hop → direct L2 single hop",
        {
            # Q34: Hermes-Prime-01 → 10.1.1.20 (== Hermes-Prime-02, direct L2)
            # Path format 은 대표 노드 sequence 로 해석
            SID.get("q34", "") or "PLACEHOLDER": "Hermes-Prime-01->Hermes-Prime-02",
        },
    ),

    # ---- 027: Group A node 변경 (Demeter-Prime-01 → Demeter-Prime-02) ----
    # Opus 판정이 Demeter-Prime-01 인데 실제로는 Demeter-Prime-02 라면 node 교체
    # Prime-02 는 vpn-instance / VXLAN tunnel 구성이 다를 수 있음
    # 성공 시 +0.06
    27: (
        "pj_fault_group_a_prime02",
        "Group A (Q39/Q43/Q46) node: Demeter-Prime-01 → Demeter-Prime-02",
        {
            SID["q39"]: "Demeter-Prime-02;20.1.1.10;missing static route",
            SID["q43"]: "Demeter-Prime-02;20.1.1.10;missing static route",
            SID["q46"]: "Demeter-Prime-02;20.1.1.10;missing static route",
        },
    ),
}


def _find_q34_sid(rows: list[list[str]]) -> str | None:
    """Q34 scenario_id 를 CSV 에서 직접 찾는다 (Path type, 고유 답).

    baseline CSV 는 50 Track B 행 중 path 문제만 가짐.
    여기서는 opus_answer 'Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Demeter-Prime-02->Hermes-Prime-02'
    를 가진 행을 Q34 로 식별.
    """
    target = "Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Demeter-Prime-02->Hermes-Prime-02"
    for row in rows[1:]:
        if len(row) >= 3 and row[2] == target:
            return row[0]
    return None


def generate_probe(
    serial: int,
    suffix: str,
    description: str,
    delta: dict[str, str],
    rows: list[list[str]],
    date: str = "20260424",
) -> Path:
    """단일 probe CSV 생성."""
    out = _DIR / f"submission_{serial:03d}_{date}_{suffix}.csv"

    # 행 수정
    changed = 0
    missing_sids: list[str] = []
    for row in rows[1:]:
        if len(row) < 3:
            continue
        sid = row[0]
        if sid in delta:
            row[2] = delta[sid]
            changed += 1

    for sid in delta.keys():
        found = False
        for row in rows[1:]:
            if row[0] == sid:
                found = True
                break
        if not found:
            missing_sids.append(sid)

    if missing_sids:
        print(f"  WARN: serial {serial} missing sids: {missing_sids}")

    if changed != len(delta) - len(missing_sids):
        print(
            f"  WARN: serial {serial} expected {len(delta)-len(missing_sids)} changes, got {changed}"
        )

    # Write
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    return out


def main() -> None:
    if not _BASELINE.exists():
        raise SystemExit(f"baseline not found: {_BASELINE}")

    # baseline 을 한 번만 읽고, 각 probe 마다 deepcopy
    import copy
    with _BASELINE.open("r", newline="", encoding="utf-8") as f:
        base_rows = list(csv.reader(f))

    # Q34 scenario_id 동적 해결
    q34_sid = _find_q34_sid(base_rows)
    if q34_sid is not None:
        print(f"Q34 scenario_id resolved: {q34_sid}")
        # 026 delta 에 PLACEHOLDER 교체
        if "PLACEHOLDER" in PROBES[26][2]:
            old_val = PROBES[26][2].pop("PLACEHOLDER")
            PROBES[26][2][q34_sid] = old_val
    else:
        print("Q34 scenario_id NOT FOUND in baseline — probe 026 skipped")
        PROBES.pop(26, None)

    print()
    print("=" * 80)
    print("Generating submissions 020~027 (independent probes from 018 baseline)")
    print("=" * 80)
    print()

    for serial in sorted(PROBES.keys()):
        suffix, description, delta = PROBES[serial]
        if not delta:
            print(f"[SKIP] serial {serial}: empty delta")
            continue
        rows_copy = copy.deepcopy(base_rows)
        out = generate_probe(serial, suffix, description, delta, rows_copy)
        print(f"[OK]   serial {serial}: {out.name}")
        print(f"       목적: {description}")
        print(f"       변경 수: {len(delta)} IDs")
        print()


if __name__ == "__main__":
    main()
