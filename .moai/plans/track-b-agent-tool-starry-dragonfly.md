# Track B Agent Tool Server CLI (라우터 SSH 비유)

## Context

Track B의 에이전트가 푸는 50문제는 모두 `POST /api/agent/execute` 단일 엔드포인트로 가상 라우터에 CLI 명령을 보내며 진행된다. 에이전트가 어떤 장비에 어떤 명령을 보냈고 서버가 어떻게 응답했는지를 사람이 직접 점검·재현하려면 현재는 `requests`로 임시 스크립트를 작성하거나 `agent/track_b/agent.py`의 통신 코드를 따로 떼어 실행해야 해서 비용이 크다.

이 작업은 **NOC 엔지니어가 SSH로 라우터에 접속해 명령을 치는 경험을 그대로 모사하는 단일 CLI**를 추가해 다음을 가능하게 한다.

- 에이전트 실행 결과를 같은 도구로 재현·검증 (예: "Q5에서 에이전트가 보낸 명령을 손으로 다시 치기")
- 권한 차단(403)·문법 오류(422) 같은 코너 케이스를 인터랙티브하게 탐색
- 새 SPEC 작성 전 토폴로지를 빠르게 둘러보기 (`display lldp neighbor brief` 등 hop-by-hop 추적)

## 조사 결과 요약

- **서버 진입점**: `data/Track B/server.py:451` (Flask, `0.0.0.0:7860`)
- **유일 엔드포인트**: `POST /api/agent/execute` (`server.py:313-438`)
  - 요청: `{device_name: str, command: str, question_number: int}`
  - 응답: `{status, device_name, vendor, command_executed, result, [reason]}`
  - 상태 코드: 200 / 400 / 403(권한) / 404 / 422(문법)
- **장비 맵**: `server.py:65-126` (Huawei 32 + Cisco 1)
- **권한 매트릭스**: `data/Track B/question_limits_config.json` — `question_number`별 차단 규칙
- **재사용 가능한 통신 패턴**: `agent/track_b/agent.py:657-659` (`requests.Session` 싱글톤, no-proxy)
- **기존 스택**: Python 3.13, `requests`, `argparse`, 표준 `logging` (rich 설치되어 있으나 미사용)

## 결정 사항 (사용자 확정)

| 항목 | 결정 |
|---|---|
| 동작 모드 | REPL + 단발 호출(`--exec`) 둘 다 |
| 장비 전환 | `connect <device>` / `disconnect` 세션 모델 |
| 권한 컨텍스트 | `--question N` 시작 인자, REPL 내 `set question N` 으로 변경 |
| 파일 위치 | `agent/track_b/cli.py` |

## 추가 설계 결정 (Plan 작성자 판단)

- **REPL 구현**: 표준 라이브러리 `cmd.Cmd` 사용 (history·편집은 `readline`이 자동 제공). `prompt_toolkit` 등 신규 의존성 추가 안 함.
- **HTTP**: `requests.Session` 1개 + `trust_env=False` (기존 agent.py와 동일 패턴, 사내 프록시 회피).
- **출력**: 서버 `result` 필드를 그대로 stdout에 출력(라우터 출력 그대로). 메타라인(`[OK] vendor=huawei, exec=display ip routing-table`)은 stderr 또는 dim 색.
- **컬러**: ANSI 이스케이프 직접 사용 + `--no-color` 플래그. `rich` 의존하지 않음(단일 파일 유지).
- **알 수 없는 장비/명령**: 클라이언트에서 사전 검증하지 않음. 서버 응답을 그대로 출력해 실제 라우터처럼 동작.

## 변경할 파일

| 경로 | 변경 내용 |
|---|---|
| `agent/track_b/cli.py` | **신규 생성** — REPL + 단발 호출 CLI 단일 파일 (~250 LOC 내외) |

다른 파일은 수정하지 않는다. `requirements.txt`도 변경 없음 (`requests`만 사용).

## CLI 인터페이스 사양

### 시작 인자

```
python agent/track_b/cli.py [OPTIONS]

OPTIONS:
  --server URL          기본 http://127.0.0.1:7860
  --question N          기본 0 (0 또는 미지정 = 권한 검증 우회)
  --device NAME         시작 시 자동 connect할 장비 (선택)
  --exec "COMMAND"      단발 모드. 1회 실행 후 종료. --device 필수.
  --timeout SEC         요청 타임아웃 (기본 30)
  --no-color            ANSI 컬러 비활성화
  -h, --help
```

### REPL 명령

| 입력 | 동작 |
|---|---|
| `connect <device>` | 장비 컨텍스트 진입. 프롬프트가 `[Q{n}] <device>` 로 변경. |
| `disconnect` | 장비에서 빠져나옴. 프롬프트가 `[Q{n}] noc>` 로 복귀. |
| `set question <N>` | `question_number` 변경. 0이면 우회 모드. |
| `show session` | 현재 server URL, question, device 표시. |
| `help` / `?` | 명령 도움말. |
| `quit` / `exit` / Ctrl+D | REPL 종료 (장비 connected 상태에서 `exit`은 disconnect로 동작). |
| 그 외 모든 입력 | 현재 connected 장비로 `command` 전송. 미연결 시 에러 안내. |

### 출력 포맷

```
[Q5] <Janus-Prime-01> display ip routing-table
<서버 result 그대로>
[OK] vendor=huawei, exec=display ip routing-table   (dim, 단발 모드에서는 stderr)
```

권한 거부 시:
```
[Q5] <Janus-Prime-01> display current-configuration
% Permission denied (403): No permission to perform the operation
```

서버 다운 시:
```
% Connection refused: http://127.0.0.1:7860 (Tool Server가 떠 있는지 확인하세요)
```

## 재사용 패턴

- HTTP 호출 패턴은 `agent/track_b/agent.py:657-659` 의 `requests.Session(); session.trust_env = False` 모델을 동일하게 적용.
- 에러 분류 분기는 `server.py:313-438`의 status 코드 매핑(200/400/403/404/422)을 1:1로 미러링.
- 명령어/벤더 정보는 클라이언트가 알 필요 없음 — 서버가 `vendor`, `command_executed` 응답에 포함.

## 모듈 구조 (단일 파일 내부)

```
agent/track_b/cli.py
├─ ToolServerClient          # requests.Session 래퍼, execute(device, cmd, qid) → dict
├─ format_response(resp)     # 응답 → 출력 문자열 (컬러 적용)
├─ NocShell(cmd.Cmd)         # REPL. do_connect / do_disconnect / do_set / do_show / default
├─ run_repl(args)            # REPL 진입점
├─ run_oneshot(args)         # --exec 단발 모드
└─ main()                    # argparse, 모드 분기
```

## 검증 방법 (End-to-End)

전제: Tool Server가 `python "data/Track B/server.py"` 로 기동되어 있다.

1. **REPL 정상 흐름**
   ```
   python agent/track_b/cli.py --question 1
   [Q1] noc> connect Janus-Prime-01
   [Q1] <Janus-Prime-01> display interface brief
   [Q1] <Janus-Prime-01> disconnect
   [Q1] noc> quit
   ```
   기대: 명령마다 서버 응답이 그대로 출력되고, vendor=huawei 메타라인 표시.

2. **권한 차단 케이스** — `question_limits_config.json` 에서 차단된 조합 선택
   ```
   [Q?] <Device> display current-configuration
   ```
   기대: `% Permission denied (403): ...` 출력 후 프롬프트 복귀(REPL 죽지 않음).

3. **문법 오류 케이스**
   ```
   [Q1] <Janus-Prime-01> display invalid foo
   ```
   기대: 서버의 `Unrecognized command found at '^' position` 출력 그대로.

4. **단발 모드**
   ```
   python agent/track_b/cli.py --question 1 \
       --device Janus-Prime-01 \
       --exec "display ip routing-table"
   echo $?   # 0 = success, 1 = 권한/문법/연결 실패
   ```

5. **서버 다운 케이스** — 서버를 끄고 1번 다시 시도
   기대: REPL이 죽지 않고 `% Connection refused` 출력 후 프롬프트 복귀.

6. **question 변경**
   ```
   [Q0] noc> set question 5
   [Q5] noc>
   ```

7. **에이전트 실행 결과 재현 시나리오**
   - `agent/submission/` 의 임의 결과에서 Q5의 명령 시퀀스를 추출
   - CLI에서 동일 device·동일 명령을 손으로 입력
   - 서버 응답이 에이전트 로그와 일치하는지 육안 확인

## 비범위 (Out of Scope)

- 명령 자동완성·history 검색 (readline 기본 기능에 의존, 별도 구현 안 함)
- 서버 측 변경 (`server.py` 손대지 않음)
- `agent.py` 통신 로직 리팩터링 (이번 작업은 신규 파일만)
- 결과를 파일로 자동 기록하는 기능 (필요 시 사용자가 `tee`로 처리)
- 다중 장비 동시 실행 (라우터 SSH 비유에 부합하지 않음)
