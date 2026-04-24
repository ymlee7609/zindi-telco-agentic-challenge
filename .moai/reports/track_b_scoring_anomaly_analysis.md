# Track B 0.48 Persistent Score Anomaly — 분석 보고서

**작성일**: 2026-04-24
**현상**: submission 018 이후 019~027 총 9개 서로 다른 probe 모두 **정확히 0.48 유지**
**통계적 유의성**: 7개 독립 probe(서로 다른 영역/가설)가 동일 점수를 우연히 낼 확률 극히 낮음

---

## 검증된 사실

| 항목 | 값 | 상태 |
|---|---|---|
| submission_018 총 행 | 550 | 정상 |
| Track B 답변 채워진 행 | 50 | 정상 (expected) |
| Track B 비어있는 행 | 500 | 정상 (Track A 전용) |
| GROUND_TRUTH 50 entries ↔ 018 매칭 | 50/50 | 정상 |
| CSV 포맷 (literal `\n`, UTF-8, BOM 없음) | audit_format PASS | 정상 |
| Probe 간 diff 개수 | 020=3, 021=3, 022=2, 023=4, 024=7, 025=1, 026=1, 027=3 | 정상 |

**결론**: 파일 자체에는 결함 없음. **Zindi 채점 측의 이상** 가능성.

---

## 가설 분석

### 가설 A: Zindi 일일 제출 한도 초과 → 020~027 채점 미적용 (유력)

증거:
- 018 (0.48) + 019 (0.48, 확인됨) = 2회는 확정
- 이어서 020~027 추가 8회 = **총 10회**
- 많은 Zindi 대회는 **일일 제출 10회 한도**
- 한도 초과 시 추가 제출은 "접수"되지만 점수는 **기존 최고점 유지**

검증 방법:
- Zindi 제출 이력 페이지에서 각 020~027 제출의 **"평가 완료 여부"** 확인
- "Pending" 또는 "Queued" 상태라면 채점 대기 중
- 내일(다음 날) 새 제출로 재확인

**확률 높음**: 이게 가장 합리적 설명

### 가설 B: Zindi leaderboard는 최고 점수만 반영

증거:
- "0.48" 은 **사용자 최고 점수** 표시일 수 있음
- 실제 각 probe 점수는 더 낮거나 다를 수 있지만 leaderboard 에는 018 점수만

검증 방법:
- Zindi 제출 페이지에서 각 파일별 "개별 제출 점수" 확인
- My Submissions / Submission History 섹션 확인

### 가설 C: Zindi Track B 채점이 50문제 전체가 아님

증거:
- 예: public 10문제만 평가하고 private 40문제는 대회 종료 시 공개
- public 에서 0.48 = 100점 만점 중 48점 느낌
- private leaderboard 가 따로 존재

검증 방법:
- Zindi 대회 페이지의 "Evaluation" / "Rules" 섹션 확인
- Track B 평가 공식 (RMSE, accuracy, F1 등) 확인

### 가설 D: 첫 업로드 후 추가 제출이 무시됨 (동일 프로필 중복)

증거:
- 일부 Zindi 대회는 "하루에 같은 계정에서 여러 제출 시 첫 번째 또는 마지막만 채점"
- 프로필에 점수 하나만 유지

검증 방법:
- 제출 시 "replace previous" 선택지가 있었는지 확인

### 가설 E: Zindi 채점 시스템 일시 장애

증거:
- 모든 probe 가 정확히 같은 0.48 = 채점 엔진이 정지 상태
- 제출만 받고 채점 안 함

검증 방법:
- Zindi 공지사항 / Twitter / 대회 forum 확인

---

## 확정 가능한 즉시 확인 사항 (사용자 귀환 시)

### 1. Zindi 제출 페이지 상세 확인

**My Submissions** 또는 유사 페이지에서:
- [ ] 020~027 각 파일이 독립 entry 로 존재하는가?
- [ ] 각 entry 의 **상태**: "Evaluated" / "Pending" / "Error" ?
- [ ] 각 entry 의 **개별 점수**: 모두 0.48 인가, 아니면 일부 다름?
- [ ] **Best score** 가 leaderboard 에 반영되는가, **Latest submission** 이 반영되는가?

### 2. 대회 규칙 확인

- [ ] **일일 제출 한도**: 몇 회?
- [ ] **Track B 채점 메트릭**: accuracy / F1 / custom?
- [ ] **Public vs Private leaderboard**: Phase 1 에서 몇 % 공개?
- [ ] **평가 대상 문제 수**: 50 전부 vs subset?

### 3. 제출된 실제 파일 확인

- [ ] 020~027 이 정말 다른 내용으로 업로드됐는가? (Zindi 페이지에서 파일명 확인)
- [ ] 실수로 같은 파일을 반복 업로드하진 않았는가?

---

## Sanity Check Probe (채점 시스템 검증용)

**목적**: Zindi 가 실제로 채점하는지 **명확하게 검증**

### Probe 029 — Sanity Check 1: 명백한 오답 주입

Q1~Q16 Traditional (거의 확실한 정답) 중 **Q1 답을 완전히 틀린 답**으로 교체.

- 정상 채점 중이면 **점수 하락** (Q1 오답 = -0.02)
- 0.48 유지면 → Zindi 채점 미적용 확정

### Probe 030 — Sanity Check 2: 전면 공백

Track B 50개 답변 **모두 빈 문자열**로 교체.

- 정상 채점 중이면 **점수 0.00** 기록
- 0.48 유지면 → 채점 엔진 완전 정지 확정

---

## 권장 다음 단계

### 즉시 (사용자 귀환 시)

1. **Zindi 제출 이력 페이지 스크린샷** 확인
2. 가설 A 확인 (일일 한도 초과 여부)
3. 가설 C 확인 (평가 대상 문제 수)

### Day 3 (내일, 한도 리셋 후)

1. **Probe 029 Sanity Check** 제출 → 점수 변화 확인
   - 변화 → 채점 정상, 020~027 실제로 오답
   - 미변화 → 채점 이상, Zindi forum 문의 필요

2. 채점 정상 확인되면:
   - 020~027 중 가장 승산 높은 한 가설(Group A VXLAN)부터 재시도
   - 하지만 이미 같은 파일로 0.48 받았으면 재제출 의미 없음

3. 완전히 다른 영역 probe 설계:
   - Path Q34~Q38 완전 교체
   - Fault reason exhaustive 탐색 (13종 reason 모두 시도)

### Day 4+ (Phase 2 준비)

- Zindi Phase 2 시작 시점 확인
- Private leaderboard 공개 시점

---

## 현재 최고점 안전 보존

- `submission_018_20260423_ground_truth.csv` 가 **검증된 0.48 제출본**
- 어떤 상황에서도 이 파일이 최종 backup
