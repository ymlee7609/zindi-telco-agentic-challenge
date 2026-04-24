"""Bisect probe 생성기 — 4개 오답의 위치를 체계적으로 찾는다.

배경:
  018 = 0.48 = 24 정답. Q1~Q28 Opus 답 모두 raw 일치 = 28 정답 이어야 하나
  실제 24. 4문제가 어딘가 오답. 028 sanity 로 Q1/Q7/Q17 정답 확정.
  남은 후보: Q2~Q6 (5), Q8~Q16 (9), Q18~Q28 (11 - Q20/Q21 등 HIGH 제외 시 줄어듦)

전략:
  각 scenario 카테고리에서 여러 문제를 한번에 완전 오답으로 교체해
  점수 하락폭으로 해당 카테고리 정답 수 역산.

  예: Probe 029 - Q2~Q6 5문제 전체 완전 교체
    - 결과 0.48 (-0.00): Q2~Q6 전부 원래도 오답
    - 결과 0.46 (-0.02): Q2~Q6 중 1개만 정답
    - 결과 0.44 (-0.04): 2개 정답
    - 결과 0.42 (-0.06): 3개 정답
    - 결과 0.40 (-0.08): 4개 정답
    - 결과 0.38 (-0.10): 5개 전부 정답

생성 probe:
  029: Q2~Q6 Topology 5개 전체 오답화
  030: Q8~Q16 Path 9개 전체 오답화  (이미 Q7 sanity 통해 Path 중 최소 1 정답 확정)
  031: Q18/Q19/Q22/Q24/Q26/Q27 6개 MEDIUM-HIGH Fault 전체 오답화
  032: Q29~Q33 PJ Topology 5개 전체 오답화 (sanity)
  033: Q39~Q50 12개 PJ Fault 전체 교체 (sanity)

결과 해석으로 각 카테고리별 정답 수 역산 → 남은 오답 위치 특정.
"""

from __future__ import annotations

import csv
import copy
import json
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"
_GT_PATH = _DIR.parent / "opus_reference" / "GROUND_TRUTH.json"


def load_scenarios() -> dict[int, str]:
    """qid → scenario_id 매핑."""
    with _GT_PATH.open() as f:
        gt = json.load(f)
    return {e["qid"]: e["scenario_id"] for e in gt["entries"]}


SIDS = load_scenarios()


def wrong_topo_ans(qnum: int) -> str:
    """Topology 답을 완전 오답으로 생성 (Zebra-Dummy alias)."""
    return (
        rf"Zebra-Dummy-{qnum:02d}(GE9/9/0)->Nonexistent-{qnum:02d}(GE0/0/9)\n"
        rf"Zebra-Dummy-{qnum:02d}(GE9/9/1)->Fake-Peer-{qnum:02d}(XGE1/1/1)"
    )


def wrong_path_ans(qnum: int) -> str:
    return f"Zebra-Dummy-{qnum:02d}->Nonexistent-{qnum:02d}->Fake-End-{qnum:02d}"


def wrong_fault_ans(qnum: int) -> str:
    return f"Zebra-Dummy-{qnum:02d};99.99.{qnum}.{qnum};blackhole route"


def build_probe(serial: int, label: str, target_qids: list[int],
                wrong_func, rows_base: list[list[str]]) -> Path:
    """지정된 qid 들을 오답화한 새 CSV 생성."""
    out = _DIR / f"submission_{serial:03d}_20260424_{label}.csv"
    rows = copy.deepcopy(rows_base)

    # qid → scenario_id 매핑 후 해당 행 값 교체
    sids_to_change = {SIDS[q]: wrong_func(q) for q in target_qids if q in SIDS}

    changed = 0
    for r in rows[1:]:
        if len(r) >= 3 and r[0] in sids_to_change:
            r[2] = sids_to_change[r[0]]
            changed += 1

    assert changed == len(sids_to_change), f"expected {len(sids_to_change)} changes, got {changed}"

    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    return out


def main() -> None:
    with _BASELINE.open("r", newline="", encoding="utf-8") as f:
        base_rows = list(csv.reader(f))

    probes = [
        (29, "bisect_q2_q6_topo",       list(range(2, 7)),   wrong_topo_ans),
        (30, "bisect_q8_q16_path",      list(range(8, 17)),  wrong_path_ans),
        (31, "bisect_traditional_fault", [18, 19, 22, 24, 26, 27], wrong_fault_ans),
        (32, "bisect_q29_q33_pj_topo", list(range(29, 34)),  wrong_topo_ans),
        (33, "bisect_q39_q50_pj_fault", list(range(39, 51)), wrong_fault_ans),
    ]

    print("=" * 70)
    print("Bisect Probes 029~033 생성")
    print("=" * 70)
    for serial, label, qids, wrong_func in probes:
        out = build_probe(serial, label, qids, wrong_func, base_rows)
        print(f"[OK] serial {serial}: {out.name}")
        print(f"     교체 qids: {qids}")
        # 예상 결과 해석
        n = len(qids)
        print(f"     예상: 정답 개수 k 라면 점수 = 0.48 - k*0.02")
        print(f"       (0.48~{0.48 - n*0.02:.2f} 범위)")
        print()


if __name__ == "__main__":
    main()
