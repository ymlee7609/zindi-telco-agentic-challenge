# 통합 Submission — `agent/common/submission/`

Zindi 최종 제출은 `ID, Track A, Track B` 3-column CSV 단일 파일.
Track A (500 행, `\boxed{C#}` 형식) 와 Track B (50 행, 자유 텍스트) 를
하나의 파일에서 유지하기 위한 공용 디렉토리.

## 파일

- `submission_combined.csv` — Zindi 에 최종 제출할 통합 CSV (git tracked, 550 rows)
- `merge_submission.py` — Track A/B generate_submission.py 에서 호출하는 merge 헬퍼

## 작동 방식

각 Track 의 `generate_submission.py` 는 자체 submission 파일을 생성함과 **동시에**
`submission_combined.csv` 의 해당 Track 열만 갱신합니다 (다른 Track 열은 기존 값 보존).

```bash
# Track A 제출 생성 → Track A 열 자동 갱신
python agent/track_a/generate_submission.py \
    --results agent/track_a/results_batch_b/result.csv \
    --out agent/track_a/submission/submission_v1.csv

# Track B 제출 생성 → Track B 열 자동 갱신
python agent/track_b/submission/generate_submission.py \
    --results agent/track_b/results_v6_full/result.csv \
    --override agent/track_b/results_v6_retry/result.csv \
    --out agent/track_b/submission/submission_v9.csv

# 둘 다 실행 후 combined 상태 확인
python agent/common/submission/merge_submission.py --status
```

## CLI

```bash
# 현재 combined 상태 (어느 트랙 몇 행 채워졌는지)
python agent/common/submission/merge_submission.py --status

# 명시적으로 combined 를 특정 result.csv 로 부분 갱신 (수동 overlay 용)
python agent/common/submission/merge_submission.py \
    --track A --results agent/track_a/submission/overlay_patch.csv

# 모든 셀 초기화 (신중히 사용)
python agent/common/submission/merge_submission.py --reset
```

## 옵션

각 Track 의 `generate_submission.py` 에 `--skip-combined` 플래그 제공:
- 디폴트는 combined 자동 갱신
- 실험용 결과 (final 아님) 는 `--skip-combined` 로 combined 오염 방지

## 제출 절차

1. Track A / Track B 결과를 각각 생성 (combined 자동 갱신)
2. `--status` 로 양쪽 채워졌는지 확인 (목표: Track A 500, Track B 50)
3. `agent/common/submission/submission_combined.csv` 를 Zindi 에 업로드
