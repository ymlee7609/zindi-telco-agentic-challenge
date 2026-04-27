"""Track A v7_sc + Track B BEST (0.56) 통합 제출본 생성기.

소스:
  - Track A: agent/track_a/submission/submission_v7_sc_combined.csv
              (v7_sc Track A 500개 + Track B 50개 채워진 형태)
  - Track B BEST 답:
      018 baseline + Q22/Q27 multi-line + Q24 single port + Q26 static error
      = Traditional 28/28 정답 (Zindi 0.56)

출력:
  agent/submission_BEST_0_56_track_ab_v7sc_20260427.csv
"""

from __future__ import annotations

import csv
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_TRACK_A = _ROOT / "agent" / "track_a" / "submission" / "submission_v7_sc_combined.csv"
_TRACK_B_018 = _ROOT / "agent" / "track_b" / "submission" / "submission_018_20260423_ground_truth.csv"
_OUT = _ROOT / "agent" / "submission_BEST_0_56_track_ab_v7sc_20260427.csv"

# Track B BEST delta (over 018 baseline)
SID = {
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    24: "1bbdb90e-e0d1-435c-aa52-cf8c27b0b724",
    26: "c408d8a4-b09b-49cf-a9c9-b783575cf547",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}

H4_MULTI = (
    r"Gamma-Portal-02;GE1/0/2;shutdown\n"
    r"Gamma-Portal-02;192.168.70.22;missing static route"
)
Q24_PORT = "Delta-Portal-02;GE1/0/5;shutdown"
Q26_STATIC_ERR = "Gamma-Axis-02;192.168.74.45;static route error"

BEST_DELTA = {
    SID[22]: H4_MULTI,
    SID[27]: H4_MULTI,
    SID[24]: Q24_PORT,
    SID[26]: Q26_STATIC_ERR,
}


def main() -> None:
    if not _TRACK_A.exists():
        raise SystemExit(f"v7_sc source not found: {_TRACK_A}")
    if not _TRACK_B_018.exists():
        raise SystemExit(f"Track B 018 not found: {_TRACK_B_018}")

    # 018 Track B 답을 모두 로드 (BEST_DELTA 외는 018 그대로)
    with _TRACK_B_018.open(newline="", encoding="utf-8") as f:
        b018_map = {r["ID"]: r["Track B"] for r in csv.DictReader(f)}

    # v7_sc baseline 로드
    with _TRACK_A.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    assert header[:3] == ["ID", "Track A", "Track B"], f"unexpected header: {header}"

    # Track B 강제 sync: 모든 50 ID 의 Track B 답을 018 + BEST_DELTA 기준으로
    track_b_changes = 0
    for r in rows[1:]:
        if len(r) < 3:
            continue
        sid = r[0]
        # BEST_DELTA 우선 적용
        new_tb = BEST_DELTA.get(sid, b018_map.get(sid, ""))
        if new_tb and r[2] != new_tb:
            r[2] = new_tb
            track_b_changes += 1

    # 카운트
    ta_count = sum(1 for r in rows[1:] if len(r) >= 2 and r[1].strip())
    tb_count = sum(1 for r in rows[1:] if len(r) >= 3 and r[2].strip())

    with _OUT.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(rows)

    print(f"[OK] {_OUT.name}")
    print(f"     Track A: {ta_count}/500 (v7_sc 답)")
    print(f"     Track B: {tb_count}/50 (BEST 0.56 답)")
    print(f"     Track B sync changes: {track_b_changes}")
    print(f"     - 018 baseline + Q22/Q27 multi + Q24 port + Q26 static error")


if __name__ == "__main__":
    main()
