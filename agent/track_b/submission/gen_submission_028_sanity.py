"""Submission 028 — Zindi 채점 엔진 Sanity Check.

목적:
  020/022/025/026/027 5개 probe 가 서로 다른 영역을 건드렸는데
  모두 0.48 유지 → Zindi 채점 엔진 이상 여부 진단.

전략:
  HIGH confidence 로 확정된 Traditional 답 3개를 의도적으로
  완전히 틀린 답으로 교체.

  - Q1 (Topology): 파일럿 검증된 6-link 답 → 완전 다른 device/port
  - Q7 (Path): Traditional Path, 확정 정답 → 완전 다른 경로
  - Q17 (Fault): HIGH, 파일럿 검증 → 완전 다른 node/target/reason

예상 결과:
  정상 채점 시: -0.06 (3개 정답이 오답화)
  0.48 유지 시: Zindi 채점 엔진 미작동 확정
              → 020~027 모든 probe 결과도 무효, Zindi 공식 문의 필요
  부분 점수 시: -0.02 ~ -0.04 → partial match 채점 확정

중요: 이 파일은 sanity check 전용. 절대 최종 제출 아님.
"""

from __future__ import annotations

import csv
import copy
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_BASELINE = _DIR / "submission_018_20260423_ground_truth.csv"
_OUT = _DIR / "submission_028_20260424_sanity_check.csv"

# Q1: Gamma-Aegis-01 Topology (HIGH, 파일럿 검증)
Q1_SID = "535afb0d-fa81-419b-9bcc-b456d032df5d"
Q1_WRONG = (
    r"Zebra-Dummy-99(GE9/9/9)->Nonexistent-Device-00(GE0/0/0)\n"
    r"Zebra-Dummy-99(GE9/9/8)->Another-Fake-01(XGE1/1/1)"
)

# Q7: Traditional Path (확정 정답)
# scenario_id 동적 해결 필요 (Track B 첫 번째 path 답)
# 일단 알려진 path 패턴으로 찾아낼 것
Q7_WRONG = "Zebra-Dummy->Nonexistent->Fake-End"

# Q17: Alpha-Center-02 missing static route (HIGH, 파일럿)
Q17_SID = "a643f2d3-a4af-46ae-aa5d-8c63b3804658"
Q17_WRONG = "Zebra-Dummy-99;99.99.99.99;VXLAN configuration error"


def find_q7_sid(rows: list[list[str]]) -> str | None:
    """Q7 Path scenario_id 를 CSV에서 찾음.

    Q7 Opus 답은 Beta-Node-01 기반 path. 'Beta-Node-01->' 로 시작하는 답 중
    Path 형식(;없음, (없음) 인 것 첫 번째.
    """
    # GROUND_TRUTH 에서 Q7 sid 확인
    import json
    with open(Path(__file__).parent.parent / "opus_reference" / "GROUND_TRUTH.json") as f:
        gt = json.load(f)
    for e in gt["entries"]:
        if e["qid"] == 7:
            return e["scenario_id"]
    return None


def main() -> int:
    if not _BASELINE.exists():
        print(f"baseline not found: {_BASELINE}")
        return 1

    with _BASELINE.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    q7_sid = find_q7_sid(rows)
    if q7_sid is None:
        print("Q7 scenario_id 찾을 수 없음")
        return 1
    print(f"Q7 sid: {q7_sid}")

    delta = {
        Q1_SID: Q1_WRONG,
        q7_sid: Q7_WRONG,
        Q17_SID: Q17_WRONG,
    }

    out_rows = copy.deepcopy(rows)
    changed = 0
    for r in out_rows[1:]:
        if len(r) >= 3 and r[0] in delta:
            old = r[2][:60]
            r[2] = delta[r[0]]
            print(f"  [CHANGED] sid={r[0][:8]}...")
            print(f"    -: {old!r}")
            print(f"    +: {r[2]!r}")
            changed += 1

    assert changed == len(delta), f"expected {len(delta)} changes, got {changed}"

    with _OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(out_rows)

    print(f"\nSANITY CHECK probe written: {_OUT.name}")
    print("예상 결과:")
    print("  - 정상 채점: 점수 0.42 (-0.06)")
    print("  - 0.48 유지: Zindi 채점 미작동 확정")
    print("  - 0.44~0.46: partial match 채점 확정")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
