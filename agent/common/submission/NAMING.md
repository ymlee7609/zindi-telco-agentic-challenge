# Submission File Naming Rules

**공식 submission 디렉토리**: `agent/common/submission/`

모든 Track A + Track B 통합 제출본은 이 디렉토리에 저장. 1일 이상 지난 파일은 `backup/` 서브디렉토리로 이동.

---

## 디렉토리 구조

```
agent/common/submission/
├── NAMING.md                                       # 이 문서
├── lib_paths.py                                    # 표준 경로/명명 헬퍼
├── submission_NNN_YYYYMMDD_label.csv               # 활성 제출 파일 (24h 이내)
├── submission_BEST_<score>_<sources>_YYYYMMDD.csv  # 베스트 점수 통합본
└── backup/                                          # 1일 이상 지난 파일
    └── submission_*.csv
```

생성기(.py) 코드는 `agent/track_b/submission/gen_*.py` 에 유지하되 **출력은 항상 `agent/common/submission/`** 로.

---

## 파일 명명 규칙 (필수 준수)

### 1. 일반 실험 probe

```
submission_NNN_YYYYMMDD_<label>.csv
```

| 필드 | 형식 | 예시 |
|---|---|---|
| `NNN` | 3자리 serial (단조 증가) | `044`, `045` |
| `YYYYMMDD` | 작성일 (8자리) | `20260427` |
| `<label>` | snake_case 영문 (실험 이름) | `pj_static_error`, `q26_subnet` |

**예시**:
- `submission_044_20260428_q19_multi_test.csv`
- `submission_045_20260428_pj_group_a_bgp.csv`

### 2. 베스트 통합본 (특별 명명)

```
submission_BEST_<score>_<sources>_YYYYMMDD.csv
```

| 필드 | 형식 | 예시 |
|---|---|---|
| `<score>` | Zindi 점수 (소수점 → underscore) | `0_56`, `0_72` |
| `<sources>` | track_a_source + track_b_source | `track_ab_v7sc`, `track_ab_v9` |
| `YYYYMMDD` | 작성일 | `20260427` |

**예시**:
- `submission_BEST_0_56_track_ab_v7sc_20260427.csv` ← v7_sc Track A + BEST Track B
- `submission_BEST_0_56_track_ab_v9_20260427.csv` ← v9 Track A + BEST Track B
- `submission_BEST_0_72_track_ab_v9_20260428.csv` ← 향후 점수 갱신 시

### 3. 진단/sanity probe (특수 라벨)

```
submission_NNN_YYYYMMDD_sanity_<purpose>.csv
```

**예시**:
- `submission_044_20260428_sanity_q19_v9_check.csv`
- `submission_045_20260428_sanity_pj_subset.csv`

---

## Serial 번호 관리

- **현재 사용된 마지막 serial**: 043 (2026-04-27)
- **다음 사용**: 044 부터
- **Serial 사용 후 SUBMISSIONS.md 인덱스 업데이트 필수**: `agent/track_b/submission/SUBMISSIONS.md`

---

## 라벨 작성 규칙

- snake_case 영문만 사용 (한글 X, 공백 X, 대문자 X)
- 최대 30자
- 의미 명확하게:
  - 좋은 예: `pj_fault_static_error`, `q26_subnet_mask`, `q19_multi_test`
  - 나쁜 예: `test1`, `try`, `final`, `new`

특별 prefix:
- `BEST_<score>_` : 베스트 점수 통합본
- `sanity_` : 진단용 probe (HIGH 답 의도적 변경)
- `bisect_` : 카테고리 정답률 역산 probe
- `pj_` : PJ zone 관련 probe
- `td_` : Traditional 관련 probe (선택)

---

## 백업 규칙

### 자동 백업 트리거

다음 경우 즉시 backup 으로 이동:
1. 작성 후 24시간 경과
2. 더 이상 활성 비교 대상 아닌 실험 probe
3. 같은 가설의 다른 variant 가 더 좋은 결과를 내서 의미 사라짐

### 백업 위치

```
agent/common/submission/backup/
```

### 백업 명령

```bash
# 1일 이상 지난 모든 csv 자동 이동
find agent/common/submission/ -maxdepth 1 -name "submission_*.csv" -mtime +1 \
  -exec git mv {} agent/common/submission/backup/ \;
```

또는 활성 파일을 명시적으로 keep, 나머지 backup:

```bash
# 활성 파일 외 모두 backup
KEEP=("submission_BEST_0_56_track_ab_v7sc_20260427.csv" "submission_BEST_0_56_track_ab_v9_20260427.csv")
# (생략) - lib_paths.py 의 archive_old() 함수 사용 권장
```

---

## 생성기(.py) 작성 가이드

모든 새 생성기는 다음 표준 따름:

```python
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_OUT_DIR = _ROOT / "agent" / "common" / "submission"  # 표준 출력 경로
_TRACK_A_BASELINE = _ROOT / "agent" / "common" / "submission" / "submission_042_20260427_v9_018.csv"
# 또는 v7_sc 기반: submission_041_20260427_v7sc_018.csv
```

또는 `agent/common/submission/lib_paths.py` import 사용 권장.

---

## 검증 절차

제출 전 항상 실행:

```bash
# 1. 포맷 검증
python3 agent/track_b/submission/audit_format.py \
  agent/common/submission/submission_NNN_*.csv

# 2. diff 확인 (BEST 대비 변경 영역 명시)
diff agent/common/submission/submission_BEST_*.csv \
     agent/common/submission/submission_NNN_*.csv | head -10
```

PASS 한 파일만 Zindi 업로드.

---

## 인덱스 관리

새 활성 submission 추가 시 **반드시 `SUBMISSIONS.md` 업데이트**:

```
agent/track_b/submission/SUBMISSIONS.md
```

기록 항목:
- Serial / 파일명 / 작성일 / Zindi 점수 / 비고

---

Version: 1.0
Last Updated: 2026-04-27
