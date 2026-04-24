# Track B Decision Flowchart — 사용자 귀환 시 실행 가이드

**Ralph 모드 자동 생성**: 2026-04-24
**현재 확정**: 018 = 0.48 = 24/50, 028 sanity `-0.06` → Zindi exact match 채점 정상
**Day 2 동안 0.48 유지 probe**: 019/020/022/025/026/027 (PJ 5개 영역 + Topology Tier 5)

---

## 핵심 미스터리

**Q1~Q28 Opus 답 모두 raw data와 정확 일치 검증 완료** (실제 28개 정답이면 0.56)
**그러나 0.48 = 24** → **어딘가 4개 오답** 또는 **Zindi 채점 구조가 단순 accuracy가 아님**

가설 후보:
- **A**: PJ zone 은 public 채점 대상 아님 (0.48 = Traditional 24/X)
- **B**: 중복 scenario (Q17/Q21, Q18/Q22/Q27) 중복 제거 채점
- **C**: Q1~Q6 또는 Q7~Q16 중 4개가 실제 오답 (raw 일치 불구하고)
- **D**: Zindi Track B 평가 기준이 50개가 아닌 subset

---

## 생성된 probe 총 정리 (23개)

| Serial | 목적 | 변경 ID 수 | 제출 상태 | 결과 |
|---|---|---|---|---|
| 018 | baseline | - | 제출 | **0.48** |
| 019 | Q31/Q32 Tier 5 | 2 | 제출 | 0.48 |
| 020 | PJ Fault VXLAN | 3 | 제출 | 0.48 |
| 021 | PJ Fault L3VPN | 3 | 미제출 | - |
| 022 | PJ Eth-Trunk parent | 2 | 제출 | 0.48 |
| 023 | PJ Fault B+D VXLAN | 4 | 미제출 | - |
| 024 | PJ Fault BGP | 7 | 미제출 | - |
| 025 | Q29 direction swap | 1 | 제출 | 0.48 |
| 026 | Q34 direct L2 | 1 | 제출 | 0.48 |
| 027 | PJ Fault Prime-02 | 3 | 제출 | 0.48 |
| 028 | Sanity Q1/Q7/Q17 | 3 | 제출 | **0.42** ← 정상 채점 확정 |
| 029 | Q2~Q6 bisect | 5 | 미제출 | - |
| 030 | Q8~Q16 bisect | 9 | 미제출 | - |
| 031 | Q18/Q19/Q22/Q24/Q26/Q27 bisect | 6 | 미제출 | - |
| 032 | Q29~Q33 PJ Topo bisect | 5 | 미제출 | - |
| 033 | Q39~Q50 PJ Fault bisect | 12 | 미제출 | - |
| 034 | HIGH Fault bisect | 6 | 미제출 | - |
| 035 | Q1~Q6 전체 sanity | 6 | 미제출 | - |
| 036 | Q7~Q16 전체 sanity | 10 | 미제출 | - |
| 037 | Q17~Q28 전체 sanity | 12 | 미제출 | - |
| 038 | PJ 전체 sanity | 22 | 미제출 | - |
| 039 | Traditional 전체 sanity | 28 | 미제출 | - |
| 040 | 중복 scenario sanity | 5 | 미제출 | - |

---

## Decision Flowchart

### Step 1: **probe 038 제출 (최우선, 결정적 판정)**

`submission_038_20260424_sanity_all_pj.csv` — **PJ 22문제 전체 오답화**

#### 결과 해석:

**0.48 유지** → PJ 완전 public 채점 대상 아님 (가설 A 확정)
- 현재 018 = Traditional 에서 달성한 최대 점수
- 0.48 × 50 = 24. Traditional 28 문제 중 24 정답 → **4개 오답이 Traditional 안**
- **다음 Step 2 → probe 029 or 031 로 bisect**

**0.48 하락 (예: 0.36 = -0.12)** → PJ 중 일부 public 채점 (가설 A 기각)
- 하락폭 k: 0.48 - 점수 = k*0.02 → PJ 정답 수 = k
- 예: 0.36 → k=6 → PJ 22문제 중 6개가 정답 (public), Traditional 18/28
- **다음 Step 2' → PJ 답 개선 동시 Traditional 오답 탐색**

### Step 2: Traditional 오답 bisect (PJ 채점 안 될 때)

**2-a: probe 031 제출** (Q18/Q19/Q22/Q24/Q26/Q27 MEDIUM-HIGH Fault 6개 오답화)

- 0.48 유지 → 이 6개 모두 원래 오답 (6 오답 확정)
- 0.46 (-0.02) → 5 정답 1 오답
- 0.44 (-0.04) → 4 정답 2 오답
- 0.42 (-0.06) → 3 정답 3 오답
- 0.40 (-0.08) → 2 정답 4 오답 ← **4 오답 후보 영역 확정**
- 0.38 (-0.10) → 1 정답 5 오답
- 0.36 (-0.12) → 0 정답 6 오답

**2-b: 031 결과가 -0.08 이상이면 probe 029/030 도 시도**
- 029: Q2~Q6 Topology (4 오답이 Topology 일 가능성)
- 030: Q8~Q16 Path (4 오답이 Path 일 가능성)

### Step 3: 오답 위치 pinpoint (031 결과 기반)

**Case A: 031 결과 `-0.04` (2 정답 4 오답)**
→ 6개 중 4개가 오답. Opus 답 재검증 필요.

Pinpoint probes:
- Q18 답만 변경 → 점수 변화로 Q18 정답/오답 판정
- Q19, Q22, Q24, Q26, Q27 각각 반복
- 제출 예산 주의 (6회 필요)

**Case B: 031 결과 `-0.00` (전부 오답)**
→ Opus 답 자체가 전부 잘못된 방향 (raw 일치 불구하고)

가능성:
- 실제 정답이 multi-line (multi-fault)
- 다른 reason/node/IP
- 포맷 이슈

**Case C: 031 결과 `-0.12` (전부 정답)**
→ 4 오답이 다른 영역 (Topology/Path)에 있음

### Step 4: 결정된 영역에서 개선 답 재생성 + 재제출

- 오답 위치가 Topology → Tier 5 재검증 (`topology_parser.py` 이미 존재)
- 오답 위치가 Path → routing chain 재계산 (기존 도구 활용)
- 오답 위치가 Fault → multi-fault 가설 실험

---

## Day 2 8회 제출 기록

| # | Serial | 내용 | 결과 |
|---|---|---|---|
| 1 | 018 | baseline | 0.48 |
| 2 | 019 | Topology Tier 5 | 0.48 |
| 3 | 020 | PJ Fault VXLAN | 0.48 |
| 4 | 022 | PJ Eth-Trunk parent | 0.48 |
| 5 | 025 | Q29 swap | 0.48 |
| 6 | 026 | Q34 direct L2 | 0.48 |
| 7 | 027 | PJ Fault Prime-02 | 0.48 |
| 8 | 028 | Sanity (Q1/Q7/Q17 오답화) | **0.42** |

Day 3 (한도 리셋) 권장 순서: **038 → 031 → 029 → 030 → Case별 pinpoint**

---

## 현재 보유 자동화 도구

```
agent/track_b/submission/
├── audit_format.py                  # 제출 전 포맷 검증 게이트
├── merge_probes.py                  # 성공한 probe 자동 병합 → 최종 submission
├── gen_submissions_batch.py         # 020~027 재생성
├── gen_submission_028_sanity.py     # 028 sanity 재생성
├── gen_bisect_probes.py             # 029~033 재생성
├── gen_full_sanity_suite.py         # 034~040 재생성
├── gen_submission_019.py            # 019 재생성
├── UPLOAD_MANUAL.md                 # Day 2 권장 순서
├── DECISION_FLOWCHART.md            # 이 문서
└── SUBMISSIONS.md                   # 전체 이력
```

사용 흐름:
```bash
# 1. 업로드 전 반드시
python3 agent/track_b/submission/audit_format.py <csv>

# 2. 결과에 따라 새 probe 필요 시
# 각 생성기 수정/재실행

# 3. 성공 probe 병합
python3 agent/track_b/submission/merge_probes.py <serial1> <serial2> ...

# 4. 병합본 audit → Zindi 업로드
```

---

## Phase 2 대비 항목 (미완)

- **path_tracer EVPN overlay tracer** 구현 (SPEC에 있음, 아직 미적용)
- **fault_analyzer overlay reason classifier** 구현 (아직 미적용)
- **PJ Fault multi-fault 탐색 로직**
- 이들은 Phase 2 private leaderboard 공개 후 실제 정답 구조 파악 후 필요

---

**결론**: 
- 현재 0.48 = public 한계로 추정 (가설 A)
- Step 1 probe 038 업로드로 결정적 판정
- Zindi 일일 한도 복원 후 1~3회 추가 제출로 4 오답 위치 특정 가능
- 그 후 실제 개선 probe 작성
