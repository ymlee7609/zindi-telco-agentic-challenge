# Agent Architecture

> `agent/agent.py` 구조 설명서
> 최종 업데이트: 2026-04-14 | 버전: v4

## 1. 전체 흐름

```mermaid
flowchart TD
    START([CLI 실행]) --> INIT[초기화]
    INIT --> |".env 로드<br/>프로바이더 설정"| EVAL[evaluate]
    EVAL --> |"50문제 순회"| AGENT[run_agent]

    AGENT --> LOOP{반복 루프<br/>max 30회}
    LOOP --> |"시간 초과?"| TIMEOUT[강제 답변 요청]
    LOOP --> |"정상"| LLM[LLM API 호출]

    LLM --> DECISION{응답 유형?}

    DECISION --> |"tool_calls"| TOOL[Tool 실행]
    TOOL --> |"call_noc_api"| SERVER[Agent Tool Server<br/>:7860]
    SERVER --> |"CLI 결과"| TOOL
    TOOL --> |"결과를 messages에 추가"| LOOP

    DECISION --> |"content"| POST[postprocess_answer]
    POST --> RESULT[결과 반환]

    DECISION --> |"빈 응답"| EMPTY{3회 연속?}
    EMPTY --> |"아니오"| LOOP
    EMPTY --> |"예"| FORCE[강제 답변 요청]
    FORCE --> POST

    TIMEOUT --> POST
    RESULT --> CSV[CSV 기록]
    CSV --> EVAL

    style START fill:#4CAF50,color:#fff
    style RESULT fill:#2196F3,color:#fff
    style SERVER fill:#FF9800,color:#fff
    style TIMEOUT fill:#f44336,color:#fff
    style FORCE fill:#f44336,color:#fff
```

## 2. 모듈 구조

```mermaid
block-beta
    columns 3

    block:CONFIG["설정 (L19-94)"]:3
        ENV[".env 로드"]
        PROVIDERS["PROVIDERS dict<br/>openrouter|huggingface<br/>dashscope|local"]
        GLOBALS["모듈 변수<br/>API_KEY, MODEL_BASE_URL<br/>MODEL_NAME, MAX_*"]
    end

    block:CORE["핵심 로직"]:3
        POSTPROC["postprocess_answer<br/>(L108-146)"]
        NOC["call_noc_api<br/>(L160-173)"]
        RUNAGENT["run_agent<br/>(L300-460)"]
    end

    block:IO["입출력"]:3
        TOOLS_DEF["TOOLS 정의<br/>(L180-210)"]
        PROMPT["SYSTEM_PROMPT<br/>(L216-293)"]
        BATCH["evaluate<br/>(L472-533)"]
    end

    block:CLI_BLOCK["CLI"]:3
        CLI_MAIN["__main__<br/>(L540-569)"]
    end

    style CONFIG fill:#E3F2FD
    style CORE fill:#FFF3E0
    style IO fill:#E8F5E9
    style CLI_BLOCK fill:#F3E5F5
```

## 3. 주요 컴포넌트 설명

### 3.1 설정 (Configuration) — L19~94

```mermaid
flowchart LR
    ENV[.env 파일] --> |"os.environ.setdefault"| ENVVAR[환경변수]
    CLI_ARG[--provider 옵션] --> RESOLVE
    ENVVAR --> RESOLVE[_resolve_api_key]
    TOKEN_FILE["~/.cache/huggingface/token"] --> RESOLVE
    RESOLVE --> ACTIVE["활성 설정<br/>API_KEY<br/>MODEL_BASE_URL<br/>MODEL_NAME"]
```

**프로바이더 우선순위**: CLI `--provider` > 환경변수 `LLM_PROVIDER` > 기본값 `openrouter`

| 프로바이더 | Base URL | 모델명 | 인증 |
|-----------|----------|--------|------|
| `openrouter` | openrouter.ai/api/v1 | qwen/qwen3.5-35b-a3b | `OPENROUTER_API_KEY` |
| `huggingface` | router.huggingface.co/novita/v3/openai | qwen/qwen3.5-35b-a3b | `HF_TOKEN` or token file |
| `dashscope` | dashscope.aliyuncs.com/compatible-mode/v1 | qwen3.5-flash | `DASHSCOPE_API_KEY` |
| `local` | localhost:8000/v1 | Qwen/Qwen3.5-35B-A3B | 불필요 |

### 3.2 후처리 (Post-processing) — L96~146

```mermaid
flowchart TD
    RAW[모델 원본 출력] --> SPLIT[줄 단위 분리]
    SPLIT --> REGEX{정규식 매칭}

    REGEX --> |"NodeA(port)->NodeB(port)"| TOPO[Topology 라인 추출]
    REGEX --> |"node;target;cause"| FAULT[Fault 라인 추출]
    REGEX --> |"NodeA->NodeB->NodeC"| PATH[Path 라인 추출<br/>가장 긴 것 선택]
    REGEX --> |"매칭 실패"| CLEAN[프리앰블 제거]

    TOPO --> OUT[정규화된 답변]
    FAULT --> OUT
    PATH --> OUT
    CLEAN --> OUT
```

**정규식 패턴**:
- Topology: `^[\w-]+\([A-Za-z0-9/]+\)\s*->\s*[\w-]+\([A-Za-z0-9/]+\)$`
- Path: `^[\w-]+(?:\s*->\s*[\w-]+)+$`
- Fault: `^[\w-]+;[^;\n]+;[^;\n]+$`

### 3.3 에이전트 루프 (run_agent) — L300~460

```mermaid
stateDiagram-v2
    [*] --> Init: 메시지 초기화<br/>[system + user]

    Init --> CheckTimeout: 반복 시작

    CheckTimeout --> TimeoutForce: elapsed > 540s
    CheckTimeout --> CallLLM: 정상

    CallLLM --> HandleToolCalls: tool_calls 있음
    CallLLM --> HandleContent: content 있음
    CallLLM --> HandleEmpty: 둘 다 없음
    CallLLM --> APIError: 예외 발생

    HandleToolCalls --> ExecuteTool: tool별 실행
    ExecuteTool --> AppendResult: 결과 messages에 추가
    AppendResult --> CheckTimeout: 다음 반복

    HandleContent --> PostProcess: postprocess_answer()
    PostProcess --> Return_Solved: status=solved

    HandleEmpty --> IncrEmpty: empty_count++
    IncrEmpty --> ForceAnswer: empty_count >= 3
    IncrEmpty --> CheckTimeout: empty_count < 3

    ForceAnswer --> PostProcess: tools 없이 호출
    TimeoutForce --> PostProcess: tools 없이 호출
    APIError --> Sleep2s: 2초 대기
    Sleep2s --> CheckTimeout: 재시도

    Return_Solved --> [*]

    state HandleToolCalls {
        [*] --> ParseArgs
        ParseArgs --> CallNOC: call_noc_api()
        CallNOC --> Truncate: len > 12000
        CallNOC --> AppendTool: len <= 12000
        Truncate --> AppendTool
    }
```

**핵심 파라미터**:
| 파라미터 | 값 | 설명 |
|---------|-----|------|
| `MAX_ITERATIONS` | 30 | 최대 LLM 호출 횟수 |
| `MAX_TOKENS` | 16,000 | LLM 응답 최대 토큰 |
| `TIMEOUT_SECONDS` | 540 | 9분 타임아웃 (10분 제한 - 1분 마진) |
| `temperature` | 0.3 | 일반 호출 (tool use) |
| `temperature` | 0.1 | 강제 답변 호출 (정확도 우선) |
| 결과 truncate | 12,000자 | CLI 출력이 긴 경우 잘라냄 |

### 3.4 시스템 프롬프트 구조 — L216~293

```mermaid
mindmap
  root((SYSTEM_PROMPT))
    Tool
      execute_cli_command
      병렬 호출 가능
    Command Reference
      Huawei/H3C
        display 계열 18개
      Cisco
        show 계열 14개
      H3C 차이점
        lldp neighbor-information
        arp all
    Problem Strategies
      TYPE 1 Topology
        LLDP 직접 조회
        이웃 노드 역방향 조회
        ARP fallback
      TYPE 2 Path
        hop-by-hop 추적
        routing table 분석
      TYPE 3 Fault
        라우팅 장애 6유형
        포트 장애 3유형
    Critical Rules
      효율성 - 병렬 배치
      중복 금지
      형식 준수
      설명 금지
      시간 인식
      에러 처리
      벤더 감지
    Output Format Rules
      답변만 출력
      프리앰블 금지
      형식별 규칙
```

### 3.5 배치 실행 (evaluate) — L472~533

```mermaid
sequenceDiagram
    participant CLI as CLI (__main__)
    participant Eval as evaluate()
    participant Agent as run_agent()
    participant CSV as result.csv
    participant Log as eval_detail.jsonl

    CLI->>Eval: input_file, output_dir, question_ids, fresh
    Eval->>CSV: 기존 결과 로드 (resume)

    loop 각 문제 (Q1~Q50)
        Eval->>Eval: skip if completed or filtered
        Eval->>Agent: run_agent(qid, question_text)
        Agent-->>Eval: {answer, tool_calls, duration_s, status}
        Eval->>CSV: append [id, prediction]
        Eval->>Log: append JSON detail
        Eval->>Eval: solved/failed 카운트
    end

    Eval->>CLI: 결과 요약 출력
```

## 4. 데이터 흐름

```mermaid
flowchart LR
    subgraph Input
        JSON["test.json<br/>50문제"]
        ENV2[".env<br/>API 키"]
    end

    subgraph Agent
        PROMPT2["System Prompt<br/>+ Question"]
        LLM2["Qwen3.5-35B-A3B<br/>(OpenRouter)"]
        PP["postprocess_answer"]
    end

    subgraph Tool_Server["Agent Tool Server"]
        API[":7860/api/agent/execute"]
        CACHE["102,886 CLI 출력<br/>(메모리 캐시)"]
    end

    subgraph Output
        CSV2["result.csv<br/>id,prediction"]
        LOG2["eval_detail.jsonl<br/>상세 로그"]
    end

    JSON --> Agent
    ENV2 --> Agent
    PROMPT2 --> LLM2
    LLM2 --> |"tool_calls"| API
    API --> CACHE
    CACHE --> |"CLI 결과"| LLM2
    LLM2 --> |"content"| PP
    PP --> CSV2
    PP --> LOG2
```

## 5. CLI 사용법

```bash
# 기본 실행 (OpenRouter, 전체 50문제)
python agent/agent.py

# 특정 문제만
python agent/agent.py --questions 1,2,7,39

# 프로바이더 변경
python agent/agent.py --provider local

# 새로 시작 (이전 결과 무시)
python agent/agent.py --fresh

# 입출력 경로 변경
python agent/agent.py -i data/test.json -o results/run1
```

## 6. 변경 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| **v1** | 2026-04-14 | 초기 구현. HF Inference(novita) + 단일 프로바이더. MAX_ITERATIONS=15 |
| **v2** | 2026-04-14 | 시스템 프롬프트 강화 (문제 유형별 전략). 빈 응답 복구 (3회 연속 시 강제 답변). MAX_ITERATIONS=30. 타임아웃 540초 후 강제 반환 |
| **v3** | 2026-04-14 | 멀티 프로바이더 지원 (openrouter/huggingface/dashscope/local). .env 파일 자동 로드. --provider CLI 옵션 |
| **v4** | 2026-04-14 | 출력 형식 정규화. `postprocess_answer()` 후처리 함수 추가. OUTPUT FORMAT RULES 프롬프트 섹션 추가 |
