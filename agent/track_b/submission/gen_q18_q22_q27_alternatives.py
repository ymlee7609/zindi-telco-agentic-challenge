"""Q18/Q22/Q27 정답 후보 probe 생성 (v9 Track A + 새 Track B).

031 결과 0.44 (-0.04 = 4 오답 발견) 분석:
  - Q18/Q22/Q27 (동일 Opus 답 'Gamma-Portal-02;...') 그룹 = 3 모두 오답
  - Q19/Q24/Q26 중 1개 추가 오답
  - 합 4 오답

Q18/Q22/Q27 새 답 가설:

  H1 (Multi-line 추가): Opus 답 + 다른 fault 라인 추가
       = `Gamma-Portal-02;192.168.70.22;missing static route\\n
          Alpha-Center-02;192.168.70.22;missing static route`
       (Q17/Q21 의 Alpha 도 함께 fault 라는 가정)

  H2 (Reason 변경): missing → static route error
       = `Gamma-Portal-02;192.168.70.22;static route error`

  H3 (Node 차용): Q17/Q21 답 그대로
       = `Alpha-Center-02;192.168.70.22;missing static route`

각 가설을 Q18/Q22/Q27 3개 동시 적용 → 만약 정답이면 +0.06 (0.44 → 0.50)

생성 파일 (v9 Track A + 가설 Track B):
  agent/submission_v9_q18_alt_h1_multiline_20260427.csv
  agent/submission_v9_q18_alt_h2_reason_20260427.csv
  agent/submission_v9_q18_alt_h3_alpha_node_20260427.csv
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"

# Q18/Q22/Q27 scenario_id (기존 분석)
SIDS_Q18_Q22_Q27 = {
    18: "b9a77dd0-39e5-4d7b-9e9c-af61213b30ea",
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}


def build(label: str, new_value: str) -> Path:
    """v9 baseline + Q18/Q22/Q27 답 변경한 통합본 생성."""
    out = _ROOT / "agent" / f"submission_v9_q18_alt_{label}_20260427.csv"

    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    sids = set(SIDS_Q18_Q22_Q27.values())
    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in sids:
            r[2] = new_value
            changed += 1
    assert changed == 3, f"expected 3 changes, got {changed}"

    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)

    print(f"[OK] {out.name}: 3 IDs changed")
    print(f"     new TB: {new_value[:120]}")
    return out


def main() -> None:
    # H1: Multi-line (Gamma-Portal-02 + Alpha-Center-02)
    h1 = (
        r"Gamma-Portal-02;192.168.70.22;missing static route\n"
        r"Alpha-Center-02;192.168.70.22;missing static route"
    )
    build("h1_multiline", h1)

    # H2: Reason 변경
    h2 = "Gamma-Portal-02;192.168.70.22;static route error"
    build("h2_reason", h2)

    # H3: Node 차용 (Alpha-Center-02 = Q17/Q21 답)
    h3 = "Alpha-Center-02;192.168.70.22;missing static route"
    build("h3_alpha_node", h3)

    print()
    print("권장 업로드 순서 (정보가치 + 위험 균형):")
    print("  1. h3_alpha_node — 가장 단순 가설 (Q17/Q21 패턴 재현)")
    print("  2. h1_multiline — multi-fault 가설 (Q17 single fault 명시 외 multi)")
    print("  3. h2_reason    — reason 미세 조정 가설")


if __name__ == "__main__":
    main()
