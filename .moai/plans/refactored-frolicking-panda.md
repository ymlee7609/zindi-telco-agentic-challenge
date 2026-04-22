# Plan: NOC API 직접 문제 풀이 + 에이전트 구조 개선

## Context

현재 agent.py v5는 질문 유형 감지와 cold-start 힌트를 갖추고 있지만, 실제 네트워크 데이터의 구조와 풀이 전략을 충분히 반영하지 못함. 특히:
- Path 문제: Groq에서 2홉만 추적 (정답은 7홉)
- Fault 문제: 어떤 커맨드 조합이 필요한지 검증 안 됨
- 컨텍스트 관리: 라우팅 테이블이 크면 TPM 초과

**접근**: 직접 NOC API를 호출해 유형별 문제를 풀고, 그 경험으로 에이전트 개선.

## Phase 1: 직접 문제 풀이 (유형별 대표 문제)

각 유형별 1-2문제를 직접 NOC API 호출로 풀면서 다음을 파악:
- 어떤 커맨드가 유용하고 어떤 것이 불필요한지
- API 응답 데이터 크기와 형식
- 최적의 쿼리 순서와 전략

### 1-1. Topology (Q6 - Delta-Axis-01, 직접 쿼리 가능)
- `display lldp neighbor brief` on Delta-Axis-01
- `display interface brief` on Delta-Axis-01
- LLDP에 없는 링크는 ARP fallback

### 1-2. Path (Q7 - Beta-Node-01 -> Gamma-Node-01)
- 목적지 IP 확인: `display ip interface brief` on Gamma-Node-01
- Hop-by-hop: `display ip routing-table` on 각 노드
- Next-hop IP → 어느 장비인지 식별

### 1-3. Fault (Q17 - Beta-Node-01→Gamma-Node-01, 용의 노드 3개)
- 용의 노드별: `display ip routing-table`, `display interface brief`, `display current-configuration`
- 장애 패턴 식별: missing route, blackhole, shutdown, IP error

### 1-4. PJ Path (Q34 - Hermes-Prime-01 → 10.1.1.20)
- PJ 영역 네트워크 토폴로지 파악
- 라우팅 테이블 기반 경로 추적

### 1-5. MAC Conflict Fault (Q42 - Demeter-Prime-02 MAC 충돌)
- `display arp`, `display current-configuration` 확인
- MAC 주소 충돌 패턴 파악

## Phase 2: 에이전트 구조 개선 (직접 풀이 결과 기반)

### 2-1. 시스템 프롬프트 개선
- **파일**: `agent/agent.py` SYSTEM_PROMPT
- 실제 데이터 기반 전략 구체화
- 불필요한 커맨드 제거, 핵심 커맨드 우선순위화
- 응답 크기가 큰 커맨드 주의사항 추가

### 2-2. 컨텍스트 관리 개선
- **파일**: `agent/agent.py` run_agent()
- 라우팅 테이블/설정 결과를 요약/축약하는 로직
- 이전 iteration 결과를 압축하는 메커니즘
- TPM 한도 초과 방지

### 2-3. Path 풀이 전략 강화
- 첫 턴에서 source + destination 양쪽 동시 쿼리
- Hop-by-hop 추적 시 next-hop IP를 정확히 해석
- 충분한 홉을 추적하도록 유도

### 2-4. Fault 풀이 전략 강화
- 장애 유형별 체크리스트 (routing vs port)
- 설정 파일에서 키워드 기반 오류 감지 패턴
- 결과 포맷 엄격 검증

## Phase 3: 검증

- 개선된 에이전트로 Q2, Q7, Q17, Q34, Q39 재실행
- v5 결과와 비교하여 품질 개선 확인
- Groq 한도 내에서 가능한 범위까지 실행

## Critical Files

- `agent/agent.py` - 메인 에이전트 (SYSTEM_PROMPT, run_agent, postprocess_answer)
- `data/Track B/data/Phase_1/test.json` - 50개 문제 데이터
- `agent/results_v5_groq/` - 현재 최선 결과
- `agent/results/result.csv` - v1 참조 결과

## Verification

1. NOC API 직접 호출로 각 유형별 정답 도출
2. 개선된 에이전트로 동일 문제 실행 → 직접 풀이 결과와 비교
3. 이전 v1/v3 정답과 일치 확인
