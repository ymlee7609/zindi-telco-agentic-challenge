"""Submission 표준 경로/명명 헬퍼 (NAMING.md 참조).

사용:
    from agent.common.submission.lib_paths import (
        SUBMISSION_DIR, BACKUP_DIR,
        TRACK_A_V7SC, TRACK_A_V9,
        BEST_V7SC, BEST_V9,
        next_serial, build_path, build_best_path,
    )

규칙:
    제출 파일 출력은 항상 SUBMISSION_DIR.
    1일 이상 지난 파일은 BACKUP_DIR 로 이동.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# 표준 디렉토리
SUBMISSION_DIR = _ROOT / "agent" / "common" / "submission"
BACKUP_DIR = SUBMISSION_DIR / "backup"

# Track A 베이스 (활성 통합본 = v7sc + 018, v9 + 018)
TRACK_A_V7SC = SUBMISSION_DIR / "submission_041_20260427_v7sc_018.csv"
TRACK_A_V9 = SUBMISSION_DIR / "submission_042_20260427_v9_018.csv"

# 현재 BEST 통합본 (Track A 별)
BEST_V7SC = SUBMISSION_DIR / "submission_BEST_0_56_track_ab_v7sc_20260427.csv"
BEST_V9 = SUBMISSION_DIR / "submission_BEST_0_56_track_ab_20260427.csv"

# Track B 018 baseline (BEST delta 계산용)
TRACK_B_018 = _ROOT / "agent" / "track_b" / "submission" / "submission_018_20260423_ground_truth.csv"

# 현재 BEST Track B delta (0.56 점수)
SID_BEST_DELTA = {
    22: "25413f55-4923-4b8c-9da5-0b45367e9dd7",
    24: "1bbdb90e-e0d1-435c-aa52-cf8c27b0b724",
    26: "c408d8a4-b09b-49cf-a9c9-b783575cf547",
    27: "05970bd7-fbe3-4cdd-9eef-1e0ac009c90c",
}
BEST_DELTA_VALUES = {
    SID_BEST_DELTA[22]: (
        r"Gamma-Portal-02;GE1/0/2;shutdown\n"
        r"Gamma-Portal-02;192.168.70.22;missing static route"
    ),
    SID_BEST_DELTA[27]: (
        r"Gamma-Portal-02;GE1/0/2;shutdown\n"
        r"Gamma-Portal-02;192.168.70.22;missing static route"
    ),
    SID_BEST_DELTA[24]: "Delta-Portal-02;GE1/0/5;shutdown",
    SID_BEST_DELTA[26]: "Gamma-Axis-02;192.168.74.45;static route error",
}


_SERIAL_RE = re.compile(r"^submission_(\d{3})_")


def next_serial() -> int:
    """현재 SUBMISSION_DIR + BACKUP_DIR 의 최대 serial + 1 반환."""
    max_n = 0
    for d in (SUBMISSION_DIR, BACKUP_DIR):
        if not d.exists():
            continue
        for p in d.glob("submission_*.csv"):
            m = _SERIAL_RE.match(p.name)
            if m:
                max_n = max(max_n, int(m.group(1)))
    return max_n + 1


def build_path(serial: int, label: str, date: str | None = None) -> Path:
    """일반 실험 probe 경로.

    예: build_path(44, 'q19_multi_test') -> SUBMISSION_DIR / 'submission_044_20260428_q19_multi_test.csv'
    """
    if date is None:
        date = datetime.now().strftime("%Y%m%d")
    if not re.match(r"^[a-z0-9_]+$", label):
        raise ValueError(f"label must be snake_case: {label!r}")
    return SUBMISSION_DIR / f"submission_{serial:03d}_{date}_{label}.csv"


def build_best_path(score: float, source: str, date: str | None = None) -> Path:
    """베스트 통합본 경로.

    예: build_best_path(0.56, 'track_ab_v7sc')
        -> submission_BEST_0_56_track_ab_v7sc_20260427.csv
    """
    if date is None:
        date = datetime.now().strftime("%Y%m%d")
    score_str = f"{score:.2f}".replace(".", "_")
    return SUBMISSION_DIR / f"submission_BEST_{score_str}_{source}_{date}.csv"


__all__ = [
    "SUBMISSION_DIR", "BACKUP_DIR",
    "TRACK_A_V7SC", "TRACK_A_V9",
    "BEST_V7SC", "BEST_V9",
    "TRACK_B_018",
    "SID_BEST_DELTA", "BEST_DELTA_VALUES",
    "next_serial", "build_path", "build_best_path",
]
