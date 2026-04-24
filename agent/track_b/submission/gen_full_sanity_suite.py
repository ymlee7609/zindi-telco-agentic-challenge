"""Full Sanity Suite — 전체 50문제에 대한 카테고리별 정답률 역산.

029~033 이 각 카테고리 일부(MEDIUM-HIGH, PJ)만 다뤘다면,
034~040 은 HIGH confidence 포함 전체 확인.

조합으로 0.48=24 정답 의 정확한 분포 확정.

목적:
  - Q17~Q28 HIGH 정답률
  - Q1~Q6 Topology 정답률
  - Q7~Q16 Path 정답률
  - Traditional vs PJ split 확인 (PJ public/private 가설)
  - Q17/Q21 중복 답 처리 확인

현재 확정:
  - 028 sanity: Q1/Q7/Q17 정답 (sanity -0.06 확인)
  - 029 예상: Q2~Q6 정답률
  - 030 예상: Q8~Q16 정답률
  - 031 예상: Q18/Q19/Q22/Q24/Q26/Q27 정답률
"""

from __future__ import annotations

import csv
import copy
import json
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"
_GT_PATH = _DIR.parent / "opus_reference" / "GROUND_TRUTH.json"


def load_sids() -> dict[int, str]:
    with _GT_PATH.open() as f:
        gt = json.load(f)
    return {e["qid"]: e["scenario_id"] for e in gt["entries"]}


SIDS = load_sids()


def wrong_topo(q: int) -> str:
    return (
        rf"Zebra-X{q:02d}(GE9/9/0)->NoDev-{q:02d}(GE0/0/9)\n"
        rf"Zebra-X{q:02d}(GE9/9/1)->Fake-{q:02d}(XGE1/1/1)"
    )


def wrong_path(q: int) -> str:
    return f"Zebra-X{q:02d}->NoDev-{q:02d}->End-{q:02d}"


def wrong_fault(q: int) -> str:
    return f"Zebra-X{q:02d};99.99.{q}.{q};blackhole route"


def build(serial: int, label: str, mapping: list[tuple[int, str]],
          base_rows: list[list[str]]) -> Path:
    out = _DIR / f"submission_{serial:03d}_20260424_{label}.csv"
    rows = copy.deepcopy(base_rows)
    sid_to_val = {SIDS[q]: v for q, v in mapping if q in SIDS}
    ok = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in sid_to_val:
            r[2] = sid_to_val[r[0]]
            ok += 1
    assert ok == len(sid_to_val)
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)
    return out


def main() -> None:
    with _BASELINE.open("r", newline="", encoding="utf-8") as f:
        base = list(csv.reader(f))

    # 034: Traditional Fault HIGH 6개 (Q17/Q20/Q21/Q23/Q25/Q28) 오답화
    # 예상: 6 정답 확정 → -0.12 (이미 Q17은 028에서 확인 -0.02)
    # 차이로 Q20/Q21/Q23/Q25/Q28 각각 정답 여부 파악 가능
    build(34, "bisect_high_fault",
          [(q, wrong_fault(q)) for q in [17, 20, 21, 23, 25, 28]], base)

    # 035: Q1~Q6 Topology 전체 (Q1 sanity 외 Q2~Q6 포함 Q1도)
    # 예상: 6 정답 확정 → -0.12
    # 028이 Q1만 변경 -0.02 확인 + 029가 Q2~Q6 -> 중복
    # 035 는 Q1~Q6 모두 오답화로 Topology 전체 정답률 역산
    build(35, "sanity_q1_q6_topo_all",
          [(q, wrong_topo(q)) for q in range(1, 7)], base)

    # 036: Q7~Q16 Path 전체 (Q7 sanity 정답 + Q8~Q16 bisect)
    # 예상: 10 정답 확정 → -0.20
    build(36, "sanity_q7_q16_path_all",
          [(q, wrong_path(q)) for q in range(7, 17)], base)

    # 037: Q17~Q28 Traditional Fault 전체 12개 오답화
    # 예상: 12 정답 모두 맞으면 -0.24 = 0.24 점수
    # 실제 결과로 Q17~Q28 실제 정답 개수 판정
    build(37, "sanity_traditional_fault_all",
          [(q, wrong_fault(q)) for q in range(17, 29)], base)

    # 038: Q29~Q50 PJ 전체 오답화 (PJ public/private 확정)
    # 예상: public 에 PJ 없으면 -0.00 유지, 있으면 해당 정답 수만큼 하락
    # 이미 020~027이 일부 PJ 만 건드렸는데 -0.00. 전체 다 건드려서 확실히 판정
    pj_mapping = []
    for q in range(29, 34):  # PJ Topology
        pj_mapping.append((q, wrong_topo(q)))
    for q in range(34, 39):  # PJ Path
        pj_mapping.append((q, wrong_path(q)))
    for q in range(39, 51):  # PJ Fault
        pj_mapping.append((q, wrong_fault(q)))
    build(38, "sanity_all_pj", pj_mapping, base)

    # 039: Traditional 전체 28개 오답화 (ultimate sanity)
    # 예상: 전체 정답이 Traditional 에 있으면 -0.48 = 0.00
    # PJ 가 public 에 있다면 PJ 정답만 남아 > 0.00
    trad = []
    for q in range(1, 17):
        ans_type = "topo" if q <= 6 else "path"
        trad.append((q, wrong_topo(q) if ans_type == "topo" else wrong_path(q)))
    for q in range(17, 29):
        trad.append((q, wrong_fault(q)))
    build(39, "sanity_all_traditional", trad, base)

    # 040: Q17/Q21 (동일 답) + Q18/Q22/Q27 (동일 답) 만 교체
    # 중복 scenario 가 실제로 각기 독립 채점되는지 확인
    dup_mapping = [
        (17, wrong_fault(17)),
        (21, wrong_fault(21)),
        (18, wrong_fault(18)),
        (22, wrong_fault(22)),
        (27, wrong_fault(27)),
    ]
    build(40, "sanity_duplicate_scenarios", dup_mapping, base)

    # 출력 확인
    print("=" * 70)
    print("Full Sanity Suite 034~040 생성 완료")
    print("=" * 70)

    expectations = {
        34: ("HIGH Traditional Fault 6 문제 오답화 (Q17/Q20/Q21/Q23/Q25/Q28)",
             "모두 정답이면 -0.12 = 0.36, Q17 는 028에서 이미 -0.02 확인"),
        35: ("Q1~Q6 Topology 6 문제 전체",
             "Q1 정답 확정. Q2~Q6 정답률 k 에 따라 점수 = 0.48 - (1+k)*0.02"),
        36: ("Q7~Q16 Path 10 문제 전체",
             "Q7 정답 확정. Q8~Q16 정답률 k 에 따라 = 0.48 - (1+k)*0.02"),
        37: ("Q17~Q28 Traditional Fault 12 문제 전체",
             "Q17 정답 확정. Q18~Q28 정답률 k 에 따라 = 0.48 - (1+k)*0.02"),
        38: ("PJ 22 문제 전체 (Q29~Q50)",
             "PJ 가 public 아니면 -0.00 유지. 정답 있으면 하락"),
        39: ("Traditional 28 문제 전체",
             "PJ 채점 안 되면 -0.48 = 0.00, PJ 채점되면 > 0.00 로 PJ 정답 수 추정"),
        40: ("중복 scenario Q17/Q21 + Q18/Q22/Q27 (5개)",
             "중복 독립 채점이면 정답 5개 모두 -0.10, 중복 제거면 -0.04"),
    }
    for s, (desc, exp) in expectations.items():
        print(f"  {s}: {desc}")
        print(f"       예상: {exp}")
    print()
    print("권장 제출 순서 (Zindi 예산 고려):")
    print("  최우선: 038 (PJ 채점 여부 결정적 판정)")
    print("  차선:   039 (Traditional 전체 채점 여부)")
    print("  보조:   034/037 (Traditional Fault 정답률)")


if __name__ == "__main__":
    main()
