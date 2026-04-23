# Track B Opus Reference Context Extractor

Track B 50개 네트워크 문제에 대해 Opus 모델이 참조할 수 있는 구조화된 context 파일을 생성합니다.

## 파이프라인 개요

```
test.json (50 시나리오)
  +
devices_outputs/{qid}/{device}/*.txt (raw CLI 출력)
  +
submission_v12_final.csv (기존 v12 답변)
        |
        v
prepare_context.py
        |
        v
contexts/q{qid:02d}_context.md  (Opus 입력용 구조화 context)
        |
        v
[Opus 호출 — 별도 작업]
        |
        v
Opus reference answer (v12 비교 + 개선 → 제출)
```

## 질문 유형별 context 구성

| 유형 | qid 범위 | context 핵심 내용 |
|------|----------|------------------|
| **TOPO** (링크 복원) | Q1-6, Q29-33 | 타겟 노드 LLDP graph + 역방향 LLDP + interface description + ARP |
| **PATH** (경로 추적) | Q7-16, Q34-38 | src→dst 라우팅 테이블 trace + next-hop chain + IP 인터페이스 |
| **FAULT** (장애 탐지) | Q17-28, Q39-50 | 의심 장비 라우팅 + interface 상태(DOWN 포함) + logbuffer |

## 사용법

```bash
# 파일럿: Q1, Q11, Q17 만 생성
python3 agent/track_b/opus_reference/prepare_context.py --qids 1 11 17

# Q01 품질 확인 (stdout 출력 포함)
python3 agent/track_b/opus_reference/prepare_context.py --qids 1 11 17 --print-q01

# 전체 50개 생성 (주의: 시간 소요)
python3 agent/track_b/opus_reference/prepare_context.py --all
```

## 재활용된 기존 parser 함수

| 모듈 | 함수 | 용도 |
|------|------|------|
| `cli_parsers` | `list_devices`, `read_file` | 장비 목록 및 raw 파일 읽기 |
| `cli_parsers` | `parse_lldp` | LLDP neighbor graph 구성 |
| `cli_parsers` | `parse_interface_brief` | 인터페이스 UP/DOWN 상태 |
| `cli_parsers` | `parse_ip_interface_brief` | IP 주소 매핑 |
| `cli_parsers` | `parse_routing_table` | 라우팅 테이블 분석 |
| `cli_parsers` | `lookup_longest_prefix`, `find_ip_owner` | IP 소유자 탐색 |
| `topology_parser` | `solve_topology`, `format_answer` | TOPO deterministic 풀이 |
| `fault_analyzer` | `extract_fault_scenarios`, `solve_fault` | FAULT deterministic 풀이 |
| `path_tracer` | `extract_path_info`, `trace_path_by_routing` | PATH deterministic 풀이 |

## 출력 파일 구조

각 `q{qid:02d}_context.md` 파일은 다음 섹션으로 구성됩니다:

1. **헤더** — qid, 유형, scenario_id, v12 답변 요약
2. **Question** — test.json 원문
3. **Devices in Scenario** — 장비 목록 + 관련 장비 식별
4. **Topology Snapshot** — LLDP 인접 관계 (유형별 특화)
5. **Interface Status** — UP/DOWN 상태 + IP 주소
6. **ARP Mappings** (TOPO) / **Routing Context** (PATH/FAULT) — 유형별 경로 정보
7. **Raw File References** — Opus가 직접 확인 가능한 파일 경로
8. **Deterministic Solver Result** — 기존 solver의 결정론적 답변
9. **v12 Answer** — 현재 제출본 (검증 대상)

## 목표 파일 크기

- 각 context 파일: **5KB ~ 30KB** (Opus 단일 요청에 적합)
- raw 파일 전체 복붙 금지 — 요약된 구조화 정보 위주

## 주의사항

- `prepare_context.py` 는 Opus API 호출 코드를 포함하지 않습니다
- 기존 `agent.py`, `fault_analyzer.py`, `path_tracer.py`, `topology_parser.py` 를 수정하지 않습니다 (read-only import)
- 프로젝트 루트에서 실행하거나 `PYTHONPATH` 를 적절히 설정하세요
