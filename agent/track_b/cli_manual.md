# Track B Tool Server CLI 사용 매뉴얼

`agent/track_b/cli.py` — Track B Agent Tool Server에 SSH로 라우터에 접속하듯 명령을 보내는 CLI. 에이전트 실행 결과 재현·인터랙티브 점검·코너 케이스(권한 차단·문법 오류) 탐색에 사용한다.

---

## 1. 사전 요구

- **Python 3.13+**
- **`requests`** (이미 프로젝트 의존성에 포함)
- **Tool Server 실행 중** — 기본 `http://127.0.0.1:7860`
  ```bash
  python "data/Track B/server.py"
  ```
  서버는 Flask 기반이며 단일 엔드포인트 `POST /api/agent/execute`를 노출한다.

---

## 2. 빠른 시작

### REPL 모드 (라우터 SSH 비유)

```bash
python agent/track_b/cli.py --question 1
```

```
Track B Tool Server CLI — 'help' 또는 '?' 로 도움말, Ctrl+D 로 종료

[Q1] noc> connect Alpha-Center-01
* connected to Alpha-Center-01 (서버 검증은 첫 명령에서 수행됨)
[Q1] <Alpha-Center-01> display interface brief
<Alpha-Center-01> display interface brief
PHY: Physical
...(라우터 출력 그대로)
[OK] vendor=huawei exec=display interface brief
[Q1] <Alpha-Center-01> disconnect
* disconnected from Alpha-Center-01
[Q1] noc> quit
```

### 단발 모드 (스크립팅용)

```bash
python agent/track_b/cli.py \
    --question 1 \
    --device Alpha-Center-01 \
    --exec "display interface brief"
echo $?   # 0 = 성공, 1 = 실패(권한·문법·연결 오류)
```

---

## 3. CLI 옵션

| 옵션 | 기본값 | 설명 |
|---|---|---|
| `--server URL` | `http://127.0.0.1:7860` | Tool Server base URL |
| `--question N` | `0` | 권한 컨텍스트로 사용할 `question_number` (0 = 권한 우회) |
| `--device NAME` | — | REPL 시작 시 자동 connect할 장비 (`--exec` 모드에서는 필수) |
| `--exec "CMD"` | — | 단발 모드: 1회 명령 실행 후 종료 |
| `--timeout SEC` | `30` | HTTP 요청 타임아웃 |
| `--no-color` | off | ANSI 컬러 비활성화 (파이프·로그 저장 시 권장) |
| `--cache-dir PATH` | 자동 탐지 | 자동완성·`commands`·`?` 도움말의 데이터 출처. 미지정 시 CWD 또는 CLI 파일 기준 `data/Track B/devices_outputs/` 자동 탐지 |
| `--question-file PATH` | 자동 탐지 | `question` 명령의 질문 데이터셋. 미지정 시 `data/Track B/data/Phase_1/test.json` 자동 탐지 |
| `-h, --help` | — | 도움말 |

**Exit code (단발 모드)**: `0` 성공, `1` 실패(403·404·422·연결 오류), `2` 사용법 오류.

---

## 4. REPL 명령어

**미접속 상태 (`[Q1] noc>`)**

| 입력 | 동작 |
|---|---|
| `list [prefix]` | 접속 가능한 장비 목록 (cache 기반). prefix 로 필터 가능. |
| `connect <device>` | 장비 세션 진입. 프롬프트가 `[Q{n}] <Device>`로 변경. |
| `question` | 50개 질문 한 줄 요약 목록 (페이징 지원). |
| `question <N>` | N번 질문 본문 (1..50, 가로 자동 wrap + 페이징). |
| `set question <N>` | 권한 컨텍스트 변경 (0 = 우회). cache 자동 갱신. |
| `show session` | 현재 server URL / question / device / cache_dir / question_file 출력. |
| `help`, `?` | REPL 명령 도움말. |
| `quit`, `exit`, Ctrl+D | REPL 종료. |

**접속 상태 (`[Q1] <Device>`)**

| 입력 | 동작 |
|---|---|
| `commands [prefix]` | 현재 장비의 실행 가능한 명령 목록. prefix 로 필터. |
| `help`, `?` (인자 없이) | `commands` 와 동일 — 실행 가능한 명령 목록 (라우터 SSH `?` 비유). |
| `help <명령>` | 해당 REPL 명령의 docstring. |
| `question [N]` | 미접속 상태와 동일하게 동작 (질문 데이터셋 조회). |
| `disconnect`, `exit` | 장비에서 빠져나옴 (프롬프트 `[Q{n}] noc>` 복귀). |
| `quit`, Ctrl+D | REPL 종료. |
| `list` | 접속 중에는 비활성 — 안내 메시지 출력. |
| 그 외 입력 | 현재 장비로 명령 전송. |

**프롬프트 해석**

- `[Q1] noc>` — Q1 컨텍스트, 장비 미접속
- `[Q1] <Alpha-Center-01>` — Q1 컨텍스트, 해당 장비에 접속됨
- `[Q5] <Alpha-Center-01>` — `set question 5` 후, 같은 장비에 그대로 접속됨

**히스토리·편집**: `readline`이 자동 활성화되어 ↑/↓로 이전 명령 호출, Ctrl+A/E·Ctrl+R 검색이 동작한다.

---

## 4-1. 자동완성과 다음 단어 도움말 (라우터 IOS 비유)

`--cache-dir` 로 지정된(또는 자동 탐지된) `data/Track B/devices_outputs/{Q}/{Device}/` 의 cache 파일명을 단어 트리로 만들어 다음 세 가지 도움말을 제공한다. cache 가 없으면 비활성화되며 시작 시 안내가 나온다.

### Tab 자동완성

- `connect <Tab>` / `list <Tab>` — 현재 question 의 cache 에 존재하는 장비명 자동완성
  ```
  [Q1] noc> connect Alph<Tab>
  Alpha-Center-01  Alpha-Center-02
  ```
- `<command-prefix> <Tab>` — 다음 단어 후보로 자동완성. 후보가 1개면 즉시 확장, 2개 이상이면 두 번째 Tab 에서 나열.
  ```
  [Q1] <Alpha-Center-01> display ip rou<Tab>     →  display ip routing-table
  [Q1] <Alpha-Center-01> display <Tab><Tab>      →  alarm  arp  bfd  bgp  current-configuration ...
  ```

### `?` 도움말 (라우터 IOS 스타일)

줄 끝에 `?` 를 붙이고 Enter — 다음 단어 후보 또는 매칭 명령을 즉시 나열한다.

```
[Q1] <Alpha-Center-01> display ?
가능한 다음 단어: alarm, arp, bfd, bgp, current-configuration, eth-trunk, interface, ip, ipv6, lldp, ...

[Q1] <Alpha-Center-01> display ip ?
가능한 다음 단어: interface, pool, routing-table, vpn-instance

[Q1] <Alpha-Center-01> display invalid ?
(매칭되는 명령 없음)
```

### `list` 명령 — 접속 가능한 장비 목록 (미접속 상태 전용)

```
[Q1] noc> list
  Alpha-Center-01
  Alpha-Center-02
  Beta-Aegis-01
  ...
  PSS
-- 33개 --

[Q1] noc> list Beta
  Beta-Aegis-01
  Beta-Aegis-02
  Beta-Axis-01
  ...
-- 10개 --
```

### `question` 명령 — 50개 질문 목록·본문 조회 (페이징)

```
[Q1] noc> question
-- 총 50개 질문 — 'question N' 으로 본문 조회 --
  Q 1  The link planning data of Gamma-Aegis-01 within the Big Data Zone has been...
  Q 2  The planning data of Gamma-Axis-02 within the Big Data Zone has been accidentally...
  ...
--More-- (Space=next page, Enter=next line, q=quit)

[Q1] noc> question 1
Q1 (scenario 535afb0d-...)
The link planning data of Gamma-Aegis-01 within the Big Data Zone has been
accidentally deleted, and it is necessary to restore the link connections of
the interfaces whose status is UP on the Gamma-Aegis-01 node.
...
```

**페이징 키 바인딩** (TTY 환경에서만 활성화)

| 키 | 동작 |
|---|---|
| `Space` (또는 임의 키) | 다음 페이지 |
| `Enter` | 한 줄만 더 |
| `q`, `Ctrl+C`, `Ctrl+D` | 페이징 중단 |

`stdin` 또는 `stdout` 이 TTY 가 아니면(파이프·리다이렉트) 페이징 없이 전체 출력. 본문은 터미널 가로폭에 맞춰 자동 wrap 된다.

### `commands` 명령 — 전체 또는 prefix 필터 목록

```
[Q1] <Alpha-Center-01> commands
  display alarm active
  display arp
  ...
  display vxlan tunnel
-- 74개 --

[Q1] <Alpha-Center-01> commands display ip
  display ip interface brief
  display ip pool
  display ip routing-table
  display ip vpn-instance
-- 4개 --
```

### 동작 원리와 한계

- **데이터 출처**: 캐시 파일명을 그대로 명령으로 역변환(`_` → 공백). 따라서 **실제로 응답이 캐시된 명령만** 후보에 포함된다(서버 화이트리스트의 모든 패턴이 아님).
- **question 별로 다름**: `set question N` 으로 변경하면 cache 가 자동 재로딩되어 후보가 갱신된다.
- **일부 변수 명령**: `display stp interface GE1-0-0` 처럼 인터페이스 이름이 `_`(공백 변환) 가 아닌 `-`로 저장된 경우 그대로 표시된다. 실제 명령으로 보낼 때는 라우터 문법(`GE1/0/0`)을 사용해야 할 수 있다.

---

## 5. 자주 쓰는 시나리오

### 5-1. 에이전트 실행 결과 재현

`agent/submission/` 의 결과에서 특정 문제의 명령 시퀀스를 골라 손으로 다시 친다.

```bash
python agent/track_b/cli.py --question 5
```
```
[Q5] noc> connect Beta-Aegis-01
[Q5] <Beta-Aegis-01> display ip routing-table
... (next-hop 확인)
[Q5] <Beta-Aegis-01> disconnect
[Q5] noc> connect Beta-Node-02
[Q5] <Beta-Node-02> display interface brief
```

### 5-2. 권한 차단(403) 탐색

`data/Track B/question_limits_config.json` 의 차단 조합을 확인 후 실행한다.

```
[Q?] <Device> display current-configuration
% Permission denied (403): Error: No permission to perform the operation
```
REPL은 죽지 않고 프롬프트가 그대로 복귀한다.

### 5-3. 문법 오류(422) 확인

```
[Q1] <Alpha-Center-01> display invalid foo
<Alpha-Center-01> display invalid foo
                          ^
Error: Unrecognized command found at '^' position.
[422]
```

### 5-4. 단발 모드로 결과를 파일에 저장

```bash
python agent/track_b/cli.py --no-color --question 1 \
    --device Alpha-Center-01 \
    --exec "display ip routing-table" > q1_alpha_routes.txt
```
`--no-color` 와 stdout 리다이렉션을 함께 쓰면 ANSI 코드가 섞이지 않는다 (CLI는 `stdout`이 TTY가 아니면 자동으로 컬러를 끈다).

### 5-5. 다른 호스트의 서버에 접속

```bash
python agent/track_b/cli.py --server http://10.0.0.5:7860 --question 1
```

---

## 6. 출력 포맷

### 정상(200)
```
<DeviceName> <command>
<라우터 명령 결과 — 빈 줄 제거 후>
[OK] vendor=huawei exec=<command>
```
서버가 `result` 필드에 라우터 prompt echo + 결과를 한 덩어리로 반환한다. 캐시 파일이 `\r\r\n` (CR+CRLF) 로 저장되어 있어 응답 텍스트에 빈 줄이 대량 삽입되는 경우가 있어 CLI 가 자동으로 빈/공백 줄을 제거하고 출력한다. 따라서 의미 있는 단락 구분 빈 줄도 함께 사라진다 — 라우터 raw 출력을 그대로 보고 싶다면 `--exec` 단발 모드 + `requests` 직접 호출이 필요하다.

### 권한 거부(403)
```
% Permission denied (403): <서버 메시지>
```

### 문법 오류·리소스 부재(422)
```
<DeviceName> <command>
                ^
Error: ...
[422] reason=<있다면>
```

### 알 수 없는 장비·캐시 미스(404)
```
% Not found (404): <서버 메시지>
```

### 잘못된 요청(400)
```
% Bad request (400): <서버 메시지>
```

### 통신 실패(0)
```
% Connection refused: ...
(Tool Server 가 떠 있는지 확인하세요)
```

---

## 7. 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| `% Connection refused` | Tool Server 미기동 또는 포트 충돌 | `python "data/Track B/server.py"` 실행 후 `ss -tlnp \| grep 7860` 으로 확인 |
| 정상 명령인데 `% Not found (404)` | 해당 question_number의 cache 디렉토리에 명령 출력 파일 없음 | `ls "data/Track B/devices_outputs/<N>/<Device>/"` 로 사용 가능한 명령 목록 확인 |
| 명령이 통과되는데 `% Not found (404): No permission to perform the operation` | 서버 측 cache miss 메시지가 권한 거부와 동일 텍스트로 반환됨 (server.py 동작) | 메시지가 아닌 HTTP status로 판단. 404 = cache miss, 403 = 실제 권한 거부 |
| REPL이 응답이 없음 | 서버 hang / 30초 미경과 | `--timeout 5` 로 짧게 재시도, 서버 로그(`agent_errors.log`) 확인 |
| 사내 프록시로 인해 127.0.0.1 호출 실패 | `HTTP_PROXY` 환경변수가 잡혀 있음 | CLI가 자동으로 `*_proxy` 변수를 비우고 `requests.Session.trust_env=False` 로 우회한다 — 별도 조치 불필요 |
| 시작 시 `! cache 디렉토리를 찾을 수 없음 ...` 경고 | CWD 가 프로젝트 루트가 아님 | 프로젝트 루트(`zindi_telco_agentic_challenge/`) 에서 실행하거나 `--cache-dir "data/Track B/devices_outputs"` 명시 |
| `commands` 가 비어 있음 | 해당 question 디렉토리에 그 device 캐시가 없음 | `set question N` 으로 다른 문제 번호 시도, 또는 `ls "data/Track B/devices_outputs/"` 로 사용 가능한 question 확인 |

---

## 8. 알려진 한계

- 자동완성·`?`·`commands` 는 **cache 에 실제로 저장된 명령만** 알 수 있다. 서버 화이트리스트(`SUPPORTED_COMMANDS`) 의 모든 패턴(예: `ping -a \S+ \S+`)은 후보에 포함되지 않으므로, 직접 입력해야 한다.
- 다중 장비 동시 실행은 지원하지 않는다 (라우터 SSH 비유에 부합하지 않음).
- 실행 로그를 자동 기록하는 기능은 없다 — 필요 시 `tee` 사용:
  ```bash
  python agent/track_b/cli.py --question 1 2>&1 | tee q1_session.log
  ```

---

## 9. 참고

- 서버 구현: `data/Track B/server.py` (단일 엔드포인트 `POST /api/agent/execute`)
- 권한 매트릭스: `data/Track B/question_limits_config.json`
- 장비 목록: `data/Track B/server.py:65-126` (Huawei 32대, Cisco `PSS` 1대)
- 에이전트의 동일 호출 패턴: `agent/track_b/agent.py:657-674` (`call_noc_api`)
- 설계 문서: `.moai/plans/track-b-agent-tool-starry-dragonfly.md`
