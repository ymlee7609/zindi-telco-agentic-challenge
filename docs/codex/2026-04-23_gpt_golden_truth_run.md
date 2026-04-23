# 2026-04-23 GPT Golden Truth 실행 기록

> 작성: 2026-04-23
> 실행 주체: Codex
> 목적: 현재 프로젝트 구조를 이해한 뒤, Track A / Track B에 대해 GPT 기반 시뮬레이션 결과를 별도 디렉토리에 저장하고 문서화

---

## 1. 목적과 해석 기준

이번 실행은 기존 결과 디렉토리와 섞이지 않도록 별도 세션 디렉토리에 저장했다.

- 세션 산출물 루트: [`codex_runs/20260423_gpt_golden_truth/`](../../codex_runs/20260423_gpt_golden_truth/)
- 세션 요약 README: [`codex_runs/20260423_gpt_golden_truth/README.md`](../../codex_runs/20260423_gpt_golden_truth/README.md)

중요한 점:

- **Track A**는 hidden test 정답이 없으므로, 진짜 ground truth는 `train.json`의 라벨뿐이다.
- **Track B**는 저장소 안에 이미 curated truth가 있으며, `agent/track_b/opus_reference/GROUND_TRUTH.json`을 기준으로 비교했다.

즉, 이번 문서의 "golden truth"는 다음 두 기준을 뜻한다.

- Track A: labeled train split
- Track B: curated Opus reference truth

---

## 2. 프로젝트 이해 요약

### Track A

- 메인 에이전트: [`agent/track_a/agent.py`](../../agent/track_a/agent.py)
- 로컬 평가기: [`agent/track_a/eval_local.py`](../../agent/track_a/eval_local.py)
- 로컬 train/test 시뮬레이터: [`data/Track A/server.py`](../../data/Track%20A/server.py)
- 특징:
  - 로컬 시뮬레이터 도구 호출
  - 외부 LLM API 추론
  - train split에서만 정답 비교 가능

### Track B

- 메인 에이전트: [`agent/track_b/agent.py`](../../agent/track_b/agent.py)
- curated truth: [`agent/track_b/opus_reference/GROUND_TRUTH.json`](../../agent/track_b/opus_reference/GROUND_TRUTH.json)
- 로컬 CLI 시뮬레이터: [`data/Track B/server.py`](../../data/Track%20B/server.py)
- 특징:
  - topology / path / fault 분기
  - CLI 툴 호출 기반 추론
  - Exact Match 평가가 매우 엄격함

---

## 3. 분리 저장 디렉토리

이번 세션 산출물은 다음 위치에만 저장했다.

### Track A

- truth materialization:
  - [`codex_runs/20260423_gpt_golden_truth/track_a/train_ground_truth/result.csv`](../../codex_runs/20260423_gpt_golden_truth/track_a/train_ground_truth/result.csv)
- GPT simulation:
  - [`codex_runs/20260423_gpt_golden_truth/track_a/gpt_sim_train_50/result.csv`](../../codex_runs/20260423_gpt_golden_truth/track_a/gpt_sim_train_50/result.csv)
  - [`codex_runs/20260423_gpt_golden_truth/track_a/gpt_sim_train_50/eval_detail.jsonl`](../../codex_runs/20260423_gpt_golden_truth/track_a/gpt_sim_train_50/eval_detail.jsonl)

### Track B

- truth materialization:
  - [`codex_runs/20260423_gpt_golden_truth/track_b/ground_truth_reference/result.csv`](../../codex_runs/20260423_gpt_golden_truth/track_b/ground_truth_reference/result.csv)
- GPT simulation:
  - [`codex_runs/20260423_gpt_golden_truth/track_b/gpt_sim_test_50/result.csv`](../../codex_runs/20260423_gpt_golden_truth/track_b/gpt_sim_test_50/result.csv)
  - [`codex_runs/20260423_gpt_golden_truth/track_b/gpt_sim_test_50/eval_detail.jsonl`](../../codex_runs/20260423_gpt_golden_truth/track_b/gpt_sim_test_50/eval_detail.jsonl)

### 로그

- [`codex_runs/20260423_gpt_golden_truth/logs/`](../../codex_runs/20260423_gpt_golden_truth/logs/)

---

## 4. 실행 조건

- 모델: `openai/gpt-4o-mini`
- 경유: OpenRouter
- Track A:
  - 로컬 train 시뮬레이터 사용
  - train 앞 50개 시나리오 대상으로 실행
- Track B:
  - 로컬 CLI 시뮬레이터 사용
  - test 50문제 전체 실행

---

## 5. 결과 요약

### Track A

비교 기준:

- truth source: [`data/Track A/data/Phase_1/train.json`](../../data/Track%20A/data/Phase_1/train.json)
- GPT 결과: `gpt_sim_train_50`

결과:

- 실행 수: `50`
- exact match: `7/50` = `14.00%`
- mean IoU: `0.1617`

해석:

- Track A는 multi-answer 비중이 있는 문제 구조라 exact 외에도 IoU를 함께 보는 것이 맞다.
- 이번 결과는 "GPT 시뮬레이션 baseline"으로는 유효하지만, 기존 Track A 전용 전략보다 강하지는 않다.

### Track B

비교 기준:

- curated truth source: [`agent/track_b/opus_reference/GROUND_TRUTH.json`](../../agent/track_b/opus_reference/GROUND_TRUTH.json)
- GPT 결과: `gpt_sim_test_50`

에이전트 상태 기준:

- `solved=47`
- `max_iterations=2`
- `validation_failed=1`

truth 비교 결과:

- raw exact match: `1/50`
- newline normalization 후 exact match: `3/50`
- normalized exact-match QIDs: `5, 6, 37`

해석:

- Track B의 내부 `solved`는 "포맷상 답변을 냈다"는 뜻이지 curated truth 일치와 동일하지 않다.
- 이번 run에서는 substantive mismatch가 많았다.
- formatting 차이도 존재했다.
  - GPT 결과는 multi-line 답변에 실제 개행을 넣음
  - curated truth는 submission style literal `\n` 사용

---

## 6. 관찰된 주요 실패 패턴

### Track A

- train 50 기준으로 일부 single-answer는 맞췄지만, multi-answer 조합 정확도가 낮았다.
- 결과적으로 partial IoU는 일부 확보했지만 정답 조합 재현력은 부족했다.

### Track B

- Q8, Q16: `max_iterations`
- Q32: `validation_failed`
- topology/path/fault 모두에서 "답을 냈다"와 "정답을 맞췄다" 사이의 차이가 컸다.

예시 경향:

- wrong peer port 추론
- wrong zone/path 선택
- fault를 과다 나열하거나 wrong node에 귀속
- PJ area에서 alias / overlay / underlay 해석 혼선

---

## 7. 결론

이번 Codex run은 두 가지를 분명히 남겼다.

1. 현재 프로젝트의 **truth 기준**은 Track A와 Track B가 다르다.
   - Track A: labeled train only
   - Track B: curated reference truth
2. GPT 단독 시뮬레이션 baseline은 저장할 가치가 있지만, 현재 repo의 specialized Track B / Track A 자산을 대체할 정도의 품질은 아니다.

그래도 이번 실행은 의미가 있다.

- 기존 결과와 섞이지 않는 독립 세션 산출물을 남겼고
- 실제 GPT 실행 로그를 확보했고
- 향후 "generic GPT baseline vs repo-specialized solver" 비교 기준점을 만들었다

---

## 8. 참고

- 세션 요약: [`codex_runs/20260423_gpt_golden_truth/README.md`](../../codex_runs/20260423_gpt_golden_truth/README.md)
- Track A progress: [`docs/track_a/08_track_a_progress.md`](../track_a/08_track_a_progress.md)
- Track B progress: [`docs/track_b/06_progress_report.md`](../track_b/06_progress_report.md)
