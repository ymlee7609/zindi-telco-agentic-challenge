# Track B PJ 영역(Q29~Q50) 결과 검증

## Context

Track B 에이전트가 푸는 50문제 중 **PJ(Spine-Leaf VXLAN) 영역의 Q29~Q50 22문제**는 정답 포맷 혼동 의심이 보고되었다 (탐색: Path 문제인데 링크 형식으로 기록된 케이스 다수). 이 영역의 현재 결과(`docs/track_b/03-3_problems.md`)가 신뢰 가능한지 사람이 직접 점검·재현할 필요가 있다.

이번 작업은 방금 추가한 `agent/track_b/cli.py`를 도구로 활용해 다음을 산출한다.

- Q29~Q50 각 문제에 대해 **사람이 읽고 따라갈 수 있는 풀이 로그**를 `docs/track_b/check/` 에 파일로 기록
- 각 로그에 (1) 풀이 단계 (어떤 cli 명령 → 어떤 응답 → 어떻게 추론), (2) 도출한 답, (3) `03-3_problems.md` 의 현재 답, (4) 두 가지 기준의 비교(엄격·의미), (5) 결론(일치/불일치/의심)을 포함
- 결과 INDEX 로 한눈에 일치/불일치 분포를 파악

산출 로그는 사용자가 향후 03-3_problems.md 수정 또는 에이전트 개선의 근거로 활용한다. **이 작업은 검증만 수행하며, 03-3_problems.md 본문은 직접 수정하지 않는다.**

## 사용자 확정 결정

| 항목 | 결정 |
|---|---|
| 검증 범위 | Q29~Q50 (PJ 영역 22문제) |
| 비교 정책 | 엄격(string-equal) + 의미(순서·공백 무시) **두 섹션 모두 기록** |
| cli.py 호출 | `--exec` 단발 호출 (Bash 매번 spawn) — 로그 재현성 확보 |
| 파일 명명 | `Q{NN}_{type}_{scenario}.md` (예: `Q29_topology_BigData.md`) |

## 조사 결과 요약

- **INPUT**: `docs/track_b/03-3-1_problems_detail.md` — 50문제 상세 (질문, 권장 쿼리 순서, 출력 포맷)
- **OUTPUT (검증 대상)**: `docs/track_b/03-3_problems.md` — 각 문제의 현재 정답
- **정답 형식 5종**: 링크(`Node(port)->Node(port)`), 경로(`A->B->C`), Routing fault (`device;ip;reason`), Port fault (`device;port;state`), 혼합형
- **유형별 명령 수**: Topology 2~3 / Path 5~15 / Fault 6~15
- **Tool Server**: `data/Track B/server.py` (Flask, `0.0.0.0:7860`, 단일 endpoint `POST /api/agent/execute`)
- **CLI**: `agent/track_b/cli.py` (방금 추가) — `--question N --device X --exec "CMD"` 단발 모드 지원, exit 0/1 정확
- **Q29~Q50 유형 분포** (탐색 보고서 기반):
  - Topology: Q29~Q33 (5문제)
  - Path: Q34~Q38 (5문제)
  - Fault: Q39~Q50 (12문제)

## 추가 설계 결정 (Plan 작성자 판단)

- **검증 단위**: 한 세션에서 22문제 전부 완료가 이상적이지만 토큰/시간 한계로 중단될 수 있음. 각 Q파일은 독립적으로 의미를 가지므로 중단 시점 이후 다음 세션에서 이어가도 안전.
- **명령 출력 인용**: cli 응답 전체가 아니라 **풀이에 결정적인 라인만** 인용 (예: 라우팅 테이블 100줄 중 next-hop 1줄). 전체 응답은 길이가 크면 truncate 표시(`... [N lines omitted]`).
- **답 도출 불가 케이스**: cache miss 404 다발 또는 정보 부족 시 결론을 `검증 불가 (이유: ...)` 로 기록하고 다음 문제 진행. 작업 중단하지 않음.
- **INDEX 파일**: `docs/track_b/check/INDEX.md` — Q번호, 유형, 결론(일치/불일치/의심/검증불가), 한 줄 비고. 진행 현황과 결과 분포를 한눈에 본다.
- **사전 확인**: Tool Server `127.0.0.1:7860` 기동 여부를 작업 시작 시 1회 체크. 미기동이면 사용자에게 안내 후 중단.

## 검증 파일 표준 구조

각 `docs/track_b/check/Q{NN}_{type}_{scenario}.md` 는 다음 7개 섹션:

```markdown
# Q{N} — {Type} ({Scenario})

- 문제 ID / 유형 / 시나리오 영역
- 검증 일시 / Tool Server URL / 검증 모델

## 1. 문제 요약 (from 03-3-1_problems_detail.md)
질문 본문 + 출력 포맷 요구

## 2. 풀이 단계
### Step 1: 목적
명령: `python agent/track_b/cli.py --question N --device X --exec "..."`
응답 핵심: (인용 — 결정적 라인만)
해석: 1~3줄

### Step 2: ...

## 3. 도출한 답
```
<답 텍스트>
```
근거: 어느 step에서 어떻게 추론

## 4. 03-3_problems.md 의 현재 답
```
<원본 인용>
```

## 5. 비교 결과
- 엄격 (string-equal): 일치 | 불일치 (차이 N라인)
- 의미 (순서·공백 무시): 일치 | 불일치
- 차이 상세: 라인별 diff 또는 의미 차이 설명

## 6. 결론
일치 | 불일치 | 의심 | 검증 불가
권장 액션: ...
```

## 작업 절차 (Execution)

### 사전 단계

1. Tool Server 기동 확인: `ss -tlnp 2>/dev/null | grep ':7860 '` — 미기동이면 사용자에게 알리고 중단
2. `docs/track_b/check/` 디렉토리 생성 (이미 있으면 그대로 사용)
3. `docs/track_b/03-3-1_problems_detail.md` / `docs/track_b/03-3_problems.md` 메모리에 로드 (Read tool, 필요 부분만)
4. `INDEX.md` 초기 헤더 작성 (Q번호 행은 비워두고 진행에 따라 채움)

### Q29 → Q50 순차 진행

각 N에 대해:

1. 03-3-1_problems_detail.md 에서 Q{N} 섹션 추출 (Grep + Read offset/limit)
2. 03-3_problems.md 에서 Q{N} 정답 섹션 추출
3. 풀이 전략 결정 (유형에 따라):
   - **Topology**: 대상 장비에서 `display lldp neighbor brief` → 보충 시 `display interface description`, `display arp`
   - **Path**: 출발 장비에서 `display ip routing-table` → next-hop IP → 다음 hop 장비로 → 반복
   - **Fault**: 영역 내 핵심 장비들에서 `display interface brief` (port down), `display ip routing-table` (missing route), 필요 시 `display logbuffer` (ARP duplicate)
4. cli.py `--exec` 단발 호출로 필요한 명령 실행. 응답에서 결정적 라인만 추출
5. 답 도출 → 03-3 정답과 두 기준으로 비교
6. `Q{NN}_{type}_{scenario}.md` 파일 작성
7. `INDEX.md` 한 줄 업데이트

### 중단 조건 (실패 시)

- Tool Server 응답 없음(연결 거부 다발 ≥3) → 작업 중단, 사용자에게 알림
- 한 문제에서 cli 호출이 ≥20회 발생하면 그 문제는 `검증 불가 (명령 폭증)` 결론으로 기록 후 다음 진행
- 토큰/시간 한계 도달 → 마지막 완료된 Q번호를 보고하고 정중히 종료. 다음 세션에서 이어서 가능

## 변경할/생성할 파일

| 경로 | 변경 |
|---|---|
| `docs/track_b/check/` | 신규 디렉토리 |
| `docs/track_b/check/INDEX.md` | 신규 (진행 현황·결과 색인) |
| `docs/track_b/check/Q29_topology_*.md` ~ `Q50_fault_*.md` | 신규 22개 |

다른 파일은 수정하지 않는다 (특히 `03-3_problems.md`, `agent/track_b/agent.py`, `agent/track_b/cli.py` 모두 read-only).

## 재사용 패턴

- `agent/track_b/cli.py` — `--exec` 단발 모드, exit 0=성공/1=실패. 출력 파싱 시 메타라인 `[OK] vendor=... exec=...` 는 stderr로 감
- 풀이에 자주 쓸 명령은 cli.py 의 `commands` REPL 명령으로 사전 탐색 가능 (캐시된 명령 목록 확인용)
- 응답 빈 줄은 cli.py가 자동 제거 (방금 수정한 `_normalize_eol`) — 인용 시 깨끗

## 검증 (End-to-End)

1. **단일 문제 시범**: Q29 한 문제만 먼저 완전히 처리해 파일 구조와 시간 예산이 합리적인지 확인. 사용자에게 보여주고 OK 받으면 Q30~Q50 일괄 진행.
2. **INDEX 체크**: 모든 완료 항목이 INDEX 표에 정확히 기록되었는지 (`grep -c "^| Q" docs/track_b/check/INDEX.md`)
3. **파일 누락 체크**: `ls docs/track_b/check/Q*.md | wc -l` 가 진행한 문제 수와 일치
4. **결론 분포**: INDEX 의 결론 컬럼 집계 (일치/불일치/의심/검증 불가) 를 최종 보고에 포함
5. **샘플 정확성**: 무작위 1~2개 Q파일을 사용자가 직접 03-3_problems.md 와 대조해 검증 로그가 사람이 따라갈 수 있는 수준인지 확인

## 비범위 (Out of Scope)

- 03-3_problems.md 직접 수정 — 결과 보고 후 사용자가 별도 결정
- 에이전트(`agent/track_b/agent.py`) 수정 — 별도 작업
- Q1~Q28 (전통 영역) 검증 — 추후 별도 세션
- 자동 정답 갱신·diff PR 자동 생성
- cli.py 자체 추가 기능 (현재 도구만 사용)
