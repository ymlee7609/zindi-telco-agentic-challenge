# Track A 개선 방안 — 0.149 → 0.30 목표

> 작성일: 2026-04-23
> 목표 제출: submission_v2 (Phase 1 데드라인 2026-05-04 내)
> 스코프: **P0 + P1 + P2 공격적 개선**, 목표 Zindi 스코어 **0.30**

---

## 1. Context (왜 이 작업을 하는가)

Track A submission v1이 Zindi 리더보드에서 **0.149** 점수를 받았다. Track B는 동일한 Qwen3.5-35B-A3B 모델로 **0.18**을 달성했으므로, Track A에는 구조적·예측 분포의 문제가 존재한다.

`agent/track_a/results_batch_a/eval_detail.jsonl`, `results_batch_b/eval_detail.jsonl`, `results_pilot_v3/eval_detail.jsonl` 정량 분석 결과:

| 지표 | pilot_v3 (0-49) | batch_a (50-249) | batch_b (250-499) |
|------|-----------------|------------------|-------------------|
| n | 50 | 200 | 250 |
| fallback_used (P7) | 22 (44%) | 134 (67%) | 187 (75%) |
| max_iter reached (≥20) | 0 | 108 (54%) | 167 (67%) |
| avg iterations | 4.5 | 13.2 | 15.2 |
| "Empty response from model" | 47 | 85 | 80 |

전체 submission 예측 분포 vs 실제 test 분포 비교:

| 항목 | submission_v1 | test.json 실제 | 괴리 |
|------|----------------|----------------|------|
| single-answer | 497/500 | 433/500 | +64 |
| multi-answer | **3/500** | **67/500** | **-64 (22배 부족)** |
| P7 fallback (insufficient data) | 343/500 (68.6%) | train 기준 12.6% | 5-6배 과잉 |

### 근본 원인 (Root Cause)

1. **RC1 — Multi-answer 예측 실패 (영향 최대)**: `agent/track_a/agent.py:336-348` forced fallback이 tag를 확인하지만 실제 응답은 `\boxed{C#}` 단일 옵션으로 수렴. `forced_answer_prompt()` (prompts.py:234-249)가 multi-answer 태그에 대해 "2-4개 선택"을 요구하지만 empty/XML 응답 후 재시도 단계가 약함.
2. **RC2 — XML 오염 복구 부재**: `agent.py:304-323`에서 XML 오염 감지 시 재질의하지만 **iteration 카운터가 증가**하여 max_iter=20을 빠르게 소진. Track B는 `find_last_valid_assistant_answer()`로 메시지 버퍼에서 마지막 유효 답을 복구하지만 Track A에는 없음.
3. **RC3 — P7 over-prediction**: forced_answer가 옵션 목록에 P7 라벨이 포함되면 "Insufficient data" 선택이 편향된 default가 되어 단일 옵션 반환 시 P7을 선호함.
4. **RC4 — 병렬 실행 지연 번인**: pilot(직렬) avg_iter=4.5 → batch_b(병렬) avg_iter=15.2. OpenRouter latency 상승 시 XML 오염/empty 응답이 기하급수적으로 증가.
5. **RC5 — RAG 14-dim 특징 빈약**: `rag.py:60-107`의 14차원 벡터는 ping-pong(unique_pci)·overshoot(max_tilt)만 대강 포착. Neighbor RSRP vs Serving RSRP 차이, SINR 안정성, ping-pong 빈도 같은 pattern-level feature 누락.

---

## 2. 개선 전략 (3 Tier)

### P0 — Critical Fix (score 복구 핵심)

#### P0-1. Multi-answer 강제 분기 + 재검증

**파일**: `agent/track_a/agent.py:336-348` (forced fallback 블록)

변경 내용:
- `scenario.get("tag")`가 `"multiple-answer"`일 때 `forced_answer_prompt()` 호출 후 응답을 검증
- 응답에 `|`가 없으면 **최대 2회 재시도** ("너는 multi-answer tag인데 단일 옵션만 반환했다 — 2-4개로 다시 제출하라")
- 여전히 실패 시 top-k RAG neighbor (same multi-tag)에서 **투표된 공통 옵션**을 answer로 사용 (비상 fallback)
- 참조할 Track B 패턴: `agent/track_b/agent.py:1604-1696` (forced validation + retry)

기대 효과: 67개 multi-answer 시나리오 중 **50+개에서 multi 예측 확보** → IoU 0 → 0.5 개선 시 +15~20 포인트.

#### P0-2. XML 오염 복구 (Port Track B)

**파일**: `agent/track_a/agent.py` (신규 유틸 추가 + run 루프 통합)

변경 내용:
- Track B `agent.py:780-826`의 `has_tool_call_xml()` + `find_last_valid_assistant_answer()`를 Track A에 포팅
- `run()` 루프 종료 후 (`status == "unresolved"` 혹은 extract_answer가 빈 경우), 메시지 버퍼를 역순 스캔하여 `\boxed{...}` 포함 + XML 미포함 + extract_answer 성공하는 assistant content를 찾아 복구
- 복구 성공 시 `status = "recovered"`, `fallback_used = False`로 마킹

기대 효과: max_iter 도달 시나리오 중 XML 오염 이전 단계에 **유효 답이 존재하는 경우** 복구. 약 100~150개 시나리오 recovery 예상.

#### P0-3. P7 fallback 억제 프롬프트

**파일**: `agent/track_a/prompts.py:234-249` (forced_answer_prompt 변형)

변경 내용:
- `forced_answer_prompt()` 시그니처에 `allow_p7: bool = False` 파라미터 추가
- single-answer일 때 **allow_p7=False**면 옵션 목록에서 "Insufficient data" 라벨 옵션을 제외하고 강제 선택 요구 ("pick the BEST NON-P7 option based on the evidence gathered so far")
- 첫 번째 forced 재시도는 allow_p7=False, 두 번째 재시도에만 allow_p7=True (최종 안전망)

기대 효과: P7 비율 68.6% → **30-40%로 감소**, 실제 P7 정답(12.6%) 근접.

---

### P1 — Stability Enhancement (번인 방지)

#### P1-1. XML 재질의를 iteration 카운터에서 분리

**파일**: `agent/track_a/agent.py:283-329` (run 루프 구조 변경)

변경 내용:
- `run()` 내부에 `xml_retry_budget = 5` 별도 카운터 도입
- `xml_polluted and not has_boxed` 분기에서 iteration `i`를 증가시키지 않고 `xml_retry_budget -= 1`만 수행
- `xml_retry_budget == 0` 시 강제 forced fallback으로 이동
- `max_iterations`는 현재 20 → **25**로 소폭 상향 (추가 tool-call 여유)

기대 효과: `Max iterations reached` 비율 67% → **30% 이하**로 감소.

#### P1-2. 병렬 실행 축소 + 선택적 직렬 재실행

**파일**: `agent/track_a/agent.py` (`--parallel`, `--rerun-fallback` CLI 옵션 추가)

변경 내용:
- `--parallel N` 기본값 현 수준 → **축소 (N=2 또는 직렬)** 및 CLI로 지정 가능
- `--rerun-fallback RESULT_CSV` 옵션: 기존 결과 CSV에서 `fallback_used=True` 또는 empty prediction 시나리오만 골라 **직렬**로 재실행, 결과를 patch file로 출력
- patch는 기존 `generate_submission.py`의 `overrides` 인자로 병합 가능 (`submission_v2.csv` 생성 시)

기대 효과: batch_b의 avg_iter 15.2 → 6~8 수준으로 회복, empty/max_iter 비율 절반 이하.

#### P1-3. Single/Multi 전용 system prompt 분기

**파일**: `agent/track_a/prompts.py` (SYSTEM_PROMPT를 2 variant로 분리)

변경 내용:
- `SYSTEM_PROMPT_SINGLE`: 기존 내용에서 "MULTIPLE-ANSWER RULES" 섹션 축소 + "ONLY ONE option will be correct" 강조
- `SYSTEM_PROMPT_MULTI`: multi-answer 전용 — "YOU MUST return 2-4 options" + P3/P4 combination 예시를 상단으로 이동 + "NEVER return a single C#"
- `agent.py run()`에서 `scenario["tag"]`에 따라 분기 선택

기대 효과: multi-answer 태그에서 single 예측 오류 감소 (현 64/67 → 목표 10 이하).

---

### P2 — Quality Improvement (feature 강화)

#### P2-1. RAG 14-dim → 22-dim 확장

**파일**: `agent/track_a/rag.py:60-107` (extract_features 확장), 재precompute 필요

추가할 특징 (+8 dim):
- `[14]` Serving RSRP - Dominant neighbor RSRP 평균 차이 (P3 overshoot 지표)
- `[15]` SINR 분산 (P5 server issue vs P3 overshoot 구분)
- `[16]` PCI transitions (time-series PCI 변경 횟수 — P2 ping-pong)
- `[17]` A3Offset variance across cells (셀 간 편차)
- `[18]` Total tilt max - min (P3/P6 구분)
- `[19]` Throughput recovery flag (degradation → recovery 패턴 존재 여부)
- `[20]` Cell power max (P4 coverage hole: power < 30 여부)
- `[21]` Number of neighbor cells with RSRP >= -100 (P4 지표)

변경 절차:
1. `rag.py`의 `extract_features()` 확장
2. `rag.py precompute_train()` 재호출 (기존 cache 백업 후)
3. `_STATS_KEY` mean/std 재계산
4. `.moai/cache/track_a_train_features.json` 갱신 (1.1MB → 1.6MB 예상)

기대 효과: RAG retrieval 품질 상승 → train eval 50 IoU 0.22 → **0.28+** 예상.

#### P2-2. Self-consistency (n=3) on high-uncertainty

**파일**: `agent/track_a/agent.py` (신규 `run_self_consistent()` 메소드)

변경 내용:
- `--self-consistency` 플래그 시 확장 모드 활성화
- **대상 시나리오 필터**: v2 결과에서 `fallback_used=True` 또는 `status=unresolved`만 재실행 (전체 500 중 약 100-150개 예상)
- 각 시나리오 n=3 독립 실행 (temperature=0.3), 다수결 투표 (multi-answer는 option별 득표수 합산)
- 비용 제어: 150 × 3 = 450 추가 호출, 전체 약 2x 비용

기대 효과: fallback 시나리오에서 답이 존재하는 경우 ~30~40% 추가 정답화.

#### P2-3. RAG few-shot에 최소 reasoning 추가

**파일**: `agent/track_a/rag.py:224-253` (`format_few_shot_from_retrieval`)

변경 내용:
- 현재 `(Similar solved example) \boxed{...}`만 제공 → pattern 힌트 추가
- 각 RAG neighbor에 대해 train scenario의 14-dim 벡터에서 파생된 **간략 evidence** 포함:
  - 예: `(Similar: ping-pong detected, 2 cells alternating, both A3Offset=2) \boxed{C16}`
- 생성 로직: `_feature_hint(features: list[float], answer: str) -> str` 헬퍼 추가 (50토큰 이하)

기대 효과: few-shot 품질 상승으로 태그 분류 정확도 향상, token 증가 최소.

---

## 3. 실행 순서 (Priority High → Low)

1. **[Priority High] P0-1, P0-2, P0-3 구현 → 단일 커밋**
   - 파일: `agent/track_a/agent.py`, `agent/track_a/prompts.py`
   - 재사용: Track B `agent/track_b/agent.py:780-826` 함수 포팅
2. **[Priority High] Train eval 50 재실행** (v3 RAG 샘플 동일)
   - 명령: `python agent/track_a/agent.py --source train --max-samples 50 --save-dir agent/track_a/results_train_eval_50_v4/`
   - 기대: IoU 0.22 → **0.28+**
3. **[Priority Medium] P1-1, P1-2, P1-3 구현**
   - 파일: `agent/track_a/agent.py`, `agent/track_a/prompts.py`
4. **[Priority Medium] Train eval 50 재검증** → v5 결과
5. **[Priority Low] P2-1 RAG 22-dim precompute** 
   - 명령: `python agent/track_a/rag.py --precompute`
   - Cache 백업: `.moai/cache/track_a_train_features.json.bak`
6. **[Priority Low] P2-3 few-shot reasoning 추가**
7. **[Priority Low] Train eval 50 최종 검증** → v6 결과 (IoU ≥ 0.28 게이트)
8. **[Priority High] Test 500 본 실행 (submission_v2 생성)**
   - `python agent/track_a/agent.py --source test --max-samples 500 --save-dir agent/track_a/results_batch_v2/ --max-iterations 25 --parallel 2`
9. **[Priority Medium] P2-2 Self-consistency** (v2 결과 대상)
   - `python agent/track_a/agent.py --rerun-fallback agent/track_a/results_batch_v2/result.csv --self-consistency --save-dir agent/track_a/results_batch_v2_sc/`
10. **[Priority High] Submission v2 패치 머지**
    - `python agent/track_a/generate_submission.py --base results_batch_v2/result.csv --override results_batch_v2_sc/result.csv --out submission/submission_v2.csv`
11. **Zindi 업로드 + 점수 확인** → 목표 0.30 달성 여부 판정

---

## 4. 수정 대상 파일 요약

| 파일 | 변경 유형 | 주요 수정 |
|------|----------|-----------|
| `agent/track_a/agent.py` | Modify | P0-1 multi-answer retry, P0-2 XML recovery port, P1-1 xml_retry_budget, P1-2 CLI options, P2-2 self-consistency |
| `agent/track_a/prompts.py` | Modify | P0-3 allow_p7 flag, P1-3 SYSTEM_PROMPT_SINGLE/MULTI 분리 |
| `agent/track_a/rag.py` | Modify | P2-1 14→22 dim 확장, P2-3 feature_hint 추가 |
| `.moai/cache/track_a_train_features.json` | Regenerate | P2-1 재precompute (기존 백업 후) |
| `agent/track_a/generate_submission.py` | Read-only 활용 | 기존 `--override` 기능으로 패치 머지 |
| `agent/track_a/submission/submission_v2.csv` | Create | 최종 v2 제출본 |
| `agent/common/submission/submission_combined.csv` | Update | Track A v2 + Track B 기존 50 병합 |

### 재사용할 기존 코드
- `agent/track_b/agent.py:780-791` — `_TOOL_CALL_XML_RE` 정규식, `has_tool_call_xml()`
- `agent/track_b/agent.py:794-826` — `find_last_valid_assistant_answer()` 로직 (Track A용 단순화 — validation은 extract_answer 성공 여부만)
- `agent/track_a/generate_submission.py:51-88` — `build_submission()` override 병합
- `agent/track_a/eval_local.py:27-41` — `iou_score()` 로컬 검증
- `data/Track A/utils.py:156-170` — `compute_score()` Zindi 호환 검증

---

## 5. 검증 전략

### 5.1 단계별 게이트

| 게이트 | 지표 | 임계값 | 실패 시 |
|--------|------|--------|---------|
| G1: P0 완료 후 train eval 50 | IoU mean | **≥ 0.25** | P0 구현 재검토 |
| G2: P1 완료 후 train eval 50 | IoU mean | **≥ 0.27** + empty rate < 10% | max_iter, 병렬 설정 조정 |
| G3: P2 완료 후 train eval 50 | IoU mean | **≥ 0.28** | P2-1 feature 재검토 |
| G4: test batch v2 실행 | fallback_used 비율 | **≤ 25%** | P0-3 prompt 재조정 |
| G5: test batch v2 multi 분포 | multi prediction 수 | **≥ 50/500** | P0-1, P1-3 prompt 강화 |
| G6: Zindi submission v2 | 리더보드 | **≥ 0.25** (목표 0.30) | v3 planning |

### 5.2 검증 명령 (복사-붙여넣기용)

```bash
# Gate G1/G2/G3 — train eval 50
python agent/track_a/eval_local.py agent/track_a/results_train_eval_50_v4/result.csv --source train

# Gate G4/G5 — test batch v2 분석
python3 -c "
import json
from collections import Counter
rows = [json.loads(l) for l in open('agent/track_a/results_batch_v2/eval_detail.jsonl')]
fb = sum(1 for r in rows if r.get('fallback_used'))
multi = sum(1 for r in rows if '|' in (r.get('prediction') or ''))
print(f'fallback={fb}/{len(rows)} ({fb/len(rows)*100:.1f}%), multi={multi}')
"

# Gate G6 — submission 최종 검증
python agent/track_a/generate_submission.py \
    --base agent/track_a/results_batch_v2/result.csv \
    --override agent/track_a/results_batch_v2_sc/result.csv \
    --out agent/track_a/submission/submission_v2.csv
wc -l agent/track_a/submission/submission_v2.csv  # 551 예상
```

### 5.3 회귀 방지
- 기존 `submission_v1.csv`, `results_batch_a/`, `results_batch_b/` 유지 (절대 삭제 금지)
- cache precompute 전 `.moai/cache/track_a_train_features.json` → `.json.bak` 백업
- 모든 커밋은 conventional commit: `feat(track_a)`, `fix(track_a)`, `perf(track_a)`

---

## 6. 예상 점수 영향 분해

| 개선 항목 | 영향 범위 | 기대 IoU 증분 |
|-----------|----------|---------------|
| P0-1 Multi-answer 강제 분기 | 67 multi 시나리오 | +0.04 (0.3→0.65 IoU on multi) |
| P0-2 XML 복구 | ~100-150 시나리오 (max_iter 도달) | +0.03 |
| P0-3 P7 억제 | 343 P7 fallback → ~150 | +0.05 |
| P1-1 XML 카운터 분리 | max_iter 도달 감소 | +0.01 |
| P1-2 직렬 재실행 | empty response 복구 | +0.02 |
| P1-3 Single/Multi prompt 분기 | prompt 정확도 | +0.02 |
| P2-1 RAG 22-dim | retrieval 품질 | +0.02 |
| P2-2 Self-consistency (100-150개) | fallback 시나리오 | +0.02 |
| P2-3 RAG few-shot reasoning | 전체 | +0.01 |
| **합계 (이론치)** | | **+0.22** |
| 현재 0.149 + 증분 이론치 | | **≤ 0.37** |
| **현실적 목표** | 감쇠 고려 | **0.28-0.32** |

주: 개선 항목 간 시너지/중복이 존재하므로 단순 합보다 낮게 설정. 목표 0.30 달성 가능성은 합리적 수준.

---

## 7. 리스크 및 대응

| 리스크 | 확률 | 대응 |
|--------|------|------|
| OpenRouter rate-limit 재발 (batch v2 실행 중) | 중 | `--parallel 1` 직렬 실행으로 fallback, 재개 지점 `--resume` 활용 |
| P2-1 precompute 중 기존 submission 영향 | 낮 | `.json.bak` 백업 + `--cache-file` 별도 경로 지정 |
| P0-3 P7 억제로 실제 P7 정답 시나리오도 틀림 | 중 | G4에서 fallback 비율 모니터, train eval per-tag 분석 |
| Self-consistency 비용 급증 | 낮 | `--rerun-fallback`로 대상 시나리오 제한, 토큰 상한 점검 |
| Zindi 리더보드 점수 ≤ v1 (회귀) | 낮 | submission_v1.csv 유지, v2가 열위 시 v1 복원 가능 |

---

## 8. 완료 정의 (Definition of Done)

- [ ] `agent/track_a/agent.py`에 P0-1/P0-2/P1-1/P1-2 구현 및 ruff check 통과
- [ ] `agent/track_a/prompts.py`에 P0-3/P1-3 구현 및 신규 SYSTEM_PROMPT 2종 분리
- [ ] `agent/track_a/rag.py`에 P2-1/P2-3 구현, cache precompute 성공
- [ ] Train eval 50 (v3 샘플 동일) IoU ≥ 0.28
- [ ] Test 500 batch v2 실행 완료, fallback 비율 ≤ 25%, multi 예측 ≥ 50
- [ ] `submission_v2.csv` 생성 (551 rows, Track A 500 filled, Track B 50 filled)
- [ ] `submission_combined.csv` 갱신
- [ ] `docs/track_a/08_track_a_progress.md`에 v2 실행 결과 기록
- [ ] Zindi 업로드 후 점수 기록 (목표 0.30)
- [ ] 기존 `submission_v1.csv` 및 `results_batch_{a,b}/` 보존

---

Version: 1.0
Author: MoAI orchestrator (claude-opus-4-7)
Target: submission_v2 Zindi score ≥ 0.30
