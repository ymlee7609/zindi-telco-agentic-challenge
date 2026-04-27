# Track A 만점 전략 — IoU 0.3174 → 1.0

## Context

Track A (Wireless 5G Drive-Test Optimization)에서 현재 Zindi 공개 리더보드 점수는 **IoU 0.3174**이다.
만점 1.0까지 **0.6826**의 격차가 존재한다. Phase 1 데드라인은 2026-05-04, Phase 2는 05-04~05-18 (상위 30명 → Phase 3), Phase 3는 05-18~05-29 (최종 순위, 시간 할인 적용).

현재 아키텍처: Qwen3.5-35B-A3B + 7-pattern system prompt + RAG 22-dim + XML recovery + self-consistency fallback.

**핵심 문제**: Qwen이 정답 패턴을 올바르게 분류하지 못하는 경우가 74%에 달한다.

---

## 현재 실패 분석 (Train eval 50 기준)

| 실패 유형 | 비율 | 설명 |
|-----------|------|------|
| 패턴 오분류 (P1↔P6, P3↔P4 등) | ~50% | Qwen이 evidence를 수집하지만 잘못된 패턴에 매칭 |
| Tool 사용 불충분 | ~15% | 핵심 tool을 호출하지 않아 evidence 부족 |
| Multi-answer 조합 불완전 | ~10% | 2-4개 중 일부만 맞추거나 순서/조합 오류 |
| Format 오류 (XML 오염 등) | ~10% | P0 recovery가 대부분 처리하나 잔여 오류 |
| 기타 | ~15% | Edge case, 비정형 시나리오 |

---

## 전략 로드맵 (5단계)

### Phase 1A: 전수 에러 분석 (Priority: Critical)

**목표**: Train 2000 전수 평가로 정확한 실패 분포 파악

**작업**:
1. Train eval 2000 전수 실행 (agent.py --source train, 직렬)
2. eval_local.py로 IoU 전수 계산
3. 오답 카테고리 분류:
   - 패턴별 정답률 (P1~P7 각각)
   - Single vs Multi 정답률
   - Tool call 패턴 vs 정답 상관관계
   - RAG retrieval 품질 (검색된 few-shot의 정답과 실제 정답 일치율)

**산출물**: `results_train_eval_2000/analysis.md` — 패턴별/유형별 정확도 히트맵

**핵심 파일**: `agent/track_a/agent.py`, `agent/track_a/eval_local.py`

### Phase 1B: Opus 골든 레퍼런스 확장 (Priority: High)

**목표**: Opus 4.6/4.7로 train 100+ 시나리오를 수작업 풀이하여 "골든 답안" 데이터셋 구축

**작업**:
1. Train에서 패턴별 층화 샘플링 (P1~P7 각 15~20개, 총 100~140개)
2. Opus로 각 시나리오 reasoning trace + 정답 생성
3. Opus 정답 vs 실제 정답 비교 → Opus 정확도 측정
4. Opus가 틀린 케이스 분석 → "본질적으로 어려운" 시나리오 식별
5. 정답 reasoning trace를 fine-tuning 데이터로 변환

**산출물**: `data/track_a_golden/golden_100.jsonl` — 골든 레퍼런스 + reasoning trace

### Phase 2: 프롬프트 엔지니어링 고도화 (Priority: High)

**목표**: 7-pattern 분류 정확도 향상

**작업**:
1. **패턴 결정 트리 구조화**: 현재 checklist 형태 → 명확한 if-then 분기 트리로 변환
   - 1단계: throughput 저하 구간 정의 (TP < 100 Mbps 연속 ≥3 샘플)
   - 2단계: Serving PCI 안정성 판단 (stable → P1/P5/P6/P7, pingpong → P2, handover → P1)
   - 3단계: SINR 기반 분기 (<5 → P3, ≥10+TP변동 → P5, 중간 → P4/P6)
   - 4단계: RSRP 기반 최종 분류

2. **옵션-패턴 매핑 테이블 주입**: 22개 옵션의 라벨을 사전 파싱하여 패턴별 관련 옵션 필터링
   - 예: "Decrease A3 Offset" 라벨 → P1 Late HO 후보
   - "Lift tilt angle" 라벨 → P4/P6 후보
   - 이 매핑을 system prompt에 explicit하게 포함

3. **Structured Output Format**: `\boxed{}` 앞에 reasoning 구조 강제
   ```
   PATTERN: P3 (Overshoot)
   EVIDENCE: SINR=-2dB at t=5.2s, cell 3267220_1 RSRP=-85 vs serving -95
   OPTIONS_MATCHING: C3(Decrease power 3267220_1), C12(Press tilt 3267220_1)
   \boxed{C3|C12}
   ```

4. **Few-shot 품질 향상**: RAG few-shot에 reasoning trace 포함 (골든 레퍼런스에서)

**핵심 파일**: `agent/track_a/prompts.py`

### Phase 3: RAG 시스템 대폭 강화 (Priority: High)

**목표**: 검색 정확도 및 few-shot 품질 대폭 향상

**작업**:
1. **Feature 확장 (22 → 40+ dim)**:
   - Traffic/signaling 이벤트 카운트
   - MR 데이터 통계 (UL/DL throughput variance in MR)
   - gNodeB 위치 기반 UE-cell 거리
   - Option label 기반 feature (어떤 종류의 옵션이 있는지 — tilt/power/A3/azimuth 비율)
   
2. **Embedding 기반 Retrieval**:
   - 현재 L2 distance → BAAI/bge-m3 embedding 기반 cosine similarity로 전환
   - Scenario의 전체 data를 텍스트로 직렬화 → embedding → 벡터 검색
   - 패턴 + 수치 + 텍스트 hybrid retrieval (가중 합산)

3. **Top-K 확대 + Reranking**:
   - Top-3 → Top-5 retrieval + reranking (패턴 유사도 기준)
   - Same-tag 필터 유지, 하지만 cross-tag도 1개 허용 (다양성)

4. **Few-shot 답변 검증**: 검색된 train 시나리오의 정답이 현재 시나리오의 옵션 라벨과 패턴적으로 일치하는지 검증

**핵심 파일**: `agent/track_a/rag.py`

### Phase 4: Self-Consistency + 앙상블 (Priority: Medium)

**목표**: 예측 안정성 및 정확도 향상

**작업**:
1. **전역 Self-Consistency (n=3~5)**:
   - 현재 fallback 43건에만 적용 → 전체 500건으로 확대
   - Temperature 0.3~0.7 범위에서 3~5회 실행
   - 다수결 투표 (IoU 기준 최적 조합 선택)
   - 비용: 3~5x 증가 (Phase 1은 unlimited submission이므로 OK)

2. **Multi-Provider 앙상블**:
   - OpenRouter Qwen + HuggingFace Qwen + DashScope Qwen 동시 실행
   - 동일 모델이지만 inference 구현 차이로 다양성 확보
   - 3 provider × 3 runs = 9 predictions → 다수결

3. **Confidence-based Routing**:
   - Qwen 응답의 reasoning 길이, tool call 수, pattern 명시 여부로 confidence 추정
   - Low confidence → 추가 self-consistency run (adaptive)

**핵심 파일**: `agent/track_a/agent.py` (self-consistency 로직)

### Phase 5: LoRA Fine-tuning (Priority: Critical for Phase 3)

**목표**: Qwen3.5-35B-A3B의 도메인 적응

**작업**:
1. **학습 데이터 구성**:
   - Train 2000 시나리오 → (system_prompt, tool_calls, reasoning, answer) 튜플로 변환
   - Opus 골든 레퍼런스 100+ → 고품질 reasoning trace 포함
   - Format: ChatML 또는 Qwen chat format

2. **LoRA 설정**:
   - Rank: 16~64, Alpha: 32~128
   - Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
   - Learning rate: 1e-4 ~ 5e-5
   - Epochs: 3~5
   - Gradient accumulation: batch effective size 32~64

3. **평가 전략**:
   - Train 2000에서 1600 train / 400 validation 분할
   - Validation IoU 기준 early stopping
   - Overfitting 방지: LoRA rank를 작게 유지, dropout 적용

4. **Phase 3 대비**:
   - Fine-tuned weights를 `.safetensors` 또는 adapter 형태로 패키징
   - main.py에서 로컬 모델 로딩 + inference 파이프라인 구현
   - 5분 time discount 내 500 scenarios 처리 가능한 latency 확보 (시나리오당 0.6초)

**핵심 파일**: 신규 `agent/track_a/finetune/` 디렉토리

---

## 예상 IoU 개선 로드맵

| 단계 | 현재 | 예상 IoU | 주요 기여 |
|------|------|----------|----------|
| 현재 (v2_sc) | 0.317 | — | baseline |
| Phase 1A+1B 완료 | — | — | 데이터/분석만, 직접 점수 변화 없음 |
| Phase 2 (프롬프트) | — | 0.40~0.45 | 패턴 분류 정확도 +15~20pp |
| Phase 3 (RAG) | — | 0.50~0.55 | retrieval 정확도 + few-shot 품질 |
| Phase 4 (SC+앙상블) | — | 0.55~0.65 | 안정성 + 다수결 보정 |
| Phase 5 (LoRA) | — | 0.70~0.85 | 도메인 적응, 패턴 내재화 |
| Phase 5 + 전체 최적화 | — | 0.85~0.95 | 모든 개선 시너지 |

**만점(1.0) 달성 난이도**: 매우 높음. 이유:
- 일부 시나리오는 본질적으로 모호 (Opus도 오답 가능)
- Multi-answer 4-option 조합의 정확한 매칭은 확률적으로 어려움
- C# 옵션 라벨이 시나리오마다 다르게 매핑되어 일반화 어려움

**현실적 목표**: Phase 2+3+4 → **IoU 0.55~0.65** (Phase 1 내), Phase 5 LoRA 포함 → **0.70~0.85** (Phase 3)

---

## 우선순위 실행 순서

```
[즉시] Phase 1A: Train 2000 전수 평가 (병목 식별)
   ↓
[1-2일] Phase 1B: Opus 골든 레퍼런스 100+ 구축
   ↓
[동시] Phase 2: 프롬프트 구조화 + Phase 3: RAG 확장
   ↓
[Phase 1 마감 전] Phase 4: Self-Consistency 전역 적용
   ↓
[Phase 2-3 대비] Phase 5: LoRA Fine-tuning
```

---

## 검증 방법

1. **로컬 검증**: `python eval_local.py <result.csv> --source train` (train eval N에서 IoU 측정)
2. **층화 검증**: 패턴별/태그별 IoU breakdown 추가 (eval_local.py 확장)
3. **Zindi 제출**: 각 개선 후 test 500 재실행 → Zindi 업로드 → 공개 점수 확인
4. **A/B 비교**: 동일 50건 샘플에서 구/신 버전 IoU 비교 (paired test)

---

## 핵심 파일 목록

| 파일 | 역할 | 수정 여부 |
|------|------|----------|
| `agent/track_a/agent.py` | 메인 에이전트 실행기 | 수정 (SC 전역, confidence routing) |
| `agent/track_a/prompts.py` | 시스템 프롬프트 + few-shot | 대폭 수정 (결정 트리, 구조화) |
| `agent/track_a/rag.py` | RAG feature 추출 + 검색 | 대폭 수정 (40+ dim, embedding) |
| `agent/track_a/eval_local.py` | 로컬 평가 | 확장 (패턴별 breakdown) |
| `agent/track_a/finetune/` | LoRA 학습 파이프라인 | 신규 생성 |
| `data/track_a_golden/` | Opus 골든 레퍼런스 | 신규 생성 |
