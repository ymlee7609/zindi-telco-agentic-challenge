#!/usr/bin/env python3
"""Track B Tool Server에 SSH로 접속한 듯이 명령을 보내는 CLI.

REPL 모드와 단발 호출(--exec) 모드를 모두 지원한다. NOC 엔지니어가 라우터에
원격 접속해 명령을 치는 흐름을 그대로 모사한다.

사용 예:
    python agent/track_b/cli.py --question 1
    python agent/track_b/cli.py --device Janus-Prime-01 --exec "display interface brief"
"""

from __future__ import annotations

import argparse
import cmd
import json
import os
import shutil
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import requests

# @MX:NOTE: Track B Tool Server (data/Track B/server.py) 와의 외부 통합 경계 파일.
# server.py 의 단일 엔드포인트 POST /api/agent/execute 만 호출한다.

# readline은 사용 가능한 환경(POSIX 등)에서만 자동 로드되어
# REPL 입력 편집·히스토리를 활성화한다. 없는 환경에서는 무시.
try:
    import readline  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError:
    pass


# ANSI 색상 코드 (no-color 모드에서는 빈 문자열로 대체)
class _Style:
    DIM = "\033[2m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @classmethod
    def disable(cls) -> None:
        cls.DIM = cls.RED = cls.YELLOW = cls.CYAN = cls.BOLD = cls.RESET = ""


# ===========================================================================
# Tool Server HTTP 클라이언트
# ===========================================================================


@dataclass
class ApiResult:
    """서버 응답 또는 통신 에러를 표현하는 단일 결과 객체."""

    status_code: int            # 0 = 통신 자체 실패(예: ConnectionError)
    body: dict                  # 서버 JSON 응답 (통신 실패 시 {})
    transport_error: Optional[str] = None  # 통신 실패 메시지

    @property
    def is_transport_error(self) -> bool:
        return self.status_code == 0

    @property
    def is_success(self) -> bool:
        return self.status_code == 200


class ToolServerClient:
    """data/Track B/server.py 의 /api/agent/execute 만 호출하는 얇은 래퍼.

    agent/track_b/agent.py:657-659 의 패턴(트러스트-env 비활성, 프록시 제거)을
    그대로 따라 사내 프록시 환경에서도 127.0.0.1 호출이 막히지 않도록 한다.
    """

    def __init__(self, base_url: str, timeout: float = 30.0) -> None:
        # 프록시 환경 변수가 잡혀 있으면 127.0.0.1 호출이 막히는 케이스가 있어 제거
        for key in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"):
            os.environ.pop(key, None)

        self._url = base_url.rstrip("/") + "/api/agent/execute"
        self._timeout = timeout
        self._session = requests.Session()
        self._session.trust_env = False

    def execute(self, device_name: str, command: str, question_number: int) -> ApiResult:
        try:
            resp = self._session.post(
                self._url,
                json={
                    "device_name": device_name,
                    "command": command,
                    "question_number": question_number,
                },
                timeout=self._timeout,
            )
        except requests.exceptions.ConnectionError as exc:
            return ApiResult(0, {}, transport_error=f"Connection refused: {exc}")
        except requests.exceptions.Timeout:
            return ApiResult(0, {}, transport_error=f"Timeout after {self._timeout}s")
        except requests.exceptions.RequestException as exc:
            return ApiResult(0, {}, transport_error=f"Request failed: {exc}")

        try:
            body = resp.json()
        except ValueError:
            body = {"raw": resp.text}
        return ApiResult(status_code=resp.status_code, body=body)


# ===========================================================================
# 명령어 레지스트리 (자동완성 / `?` 도움말 / `commands` 명령용)
# ===========================================================================


class CommandRegistry:
    """question_number 별로 cache 디렉토리를 스캔해 device → 명령어 목록 맵을 보관.

    데이터 출처: data/Track B/devices_outputs/{Q}/{Device}/*.txt
    파일명 → 명령어 변환은 server.py:360 의 역(`_` → 공백) 으로 수행한다.
    네트워크 CLI 명령어에는 보통 `_` 를 쓰지 않으므로 안전한 가정.
    """

    def __init__(self, cache_dir: Optional[Path]) -> None:
        self._cache_dir = cache_dir
        self._by_device: dict[str, list[str]] = {}
        self._loaded_question: Optional[int] = None

    @property
    def is_available(self) -> bool:
        return self._cache_dir is not None

    @property
    def cache_dir(self) -> Optional[Path]:
        return self._cache_dir

    def load(self, question_number: int) -> None:
        """question_number 의 cache 디렉토리를 다시 스캔. 없으면 'others' 로 fallback."""
        self._by_device.clear()
        self._loaded_question = question_number
        if self._cache_dir is None:
            return

        q_dir = self._cache_dir / str(question_number)
        if not q_dir.is_dir():
            q_dir = self._cache_dir / "others"
        if not q_dir.is_dir():
            return

        for dev_dir in q_dir.iterdir():
            if not dev_dir.is_dir():
                continue
            cmds = sorted({f.stem.replace("_", " ") for f in dev_dir.glob("*.txt")})
            if cmds:
                self._by_device[dev_dir.name] = cmds

    def devices(self) -> list[str]:
        return sorted(self._by_device.keys())

    def commands(self, device: str) -> list[str]:
        return list(self._by_device.get(device, []))

    def next_words(self, device: str, prefix: str) -> list[str]:
        """`prefix` 다음에 올 수 있는 단어들의 정렬된 목록.

        예: prefix="display ip" → ["routing-table", "interface", ...]
        prefix="display" → ["interface", "ip", "bgp", ...]
        """
        prefix_words = prefix.split()
        candidates: set[str] = set()
        for cmd in self._by_device.get(device, []):
            words = cmd.split()
            if len(words) <= len(prefix_words):
                continue
            if words[: len(prefix_words)] == prefix_words:
                candidates.add(words[len(prefix_words)])
        return sorted(candidates)

    def matching_commands(self, device: str, prefix: str) -> list[str]:
        """`prefix` 로 시작하는 전체 명령(완성형) 목록."""
        return [c for c in self._by_device.get(device, []) if c.startswith(prefix)]


def find_cache_dir(explicit: Optional[str]) -> Optional[Path]:
    """--cache-dir 인자 또는 합리적 기본 경로에서 cache 루트 탐색.

    탐색 순서: 명시 인자 → CWD/data/Track B/devices_outputs → CLI 파일 기준 상대.
    """
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.is_dir() else None

    candidates = [
        Path.cwd() / "data" / "Track B" / "devices_outputs",
        Path(__file__).resolve().parent.parent.parent / "data" / "Track B" / "devices_outputs",
    ]
    for p in candidates:
        if p.is_dir():
            return p
    return None


def find_question_file(explicit: Optional[str]) -> Optional[Path]:
    """`question` 명령의 데이터셋(.json) 파일 자동 탐지."""
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.is_file() else None

    candidates = [
        Path.cwd() / "data" / "Track B" / "data" / "Phase_1" / "test.json",
        Path(__file__).resolve().parent.parent.parent
        / "data" / "Track B" / "data" / "Phase_1" / "test.json",
    ]
    for p in candidates:
        if p.is_file():
            return p
    return None


# ===========================================================================
# Question 데이터셋
# ===========================================================================


class QuestionCatalog:
    """`data/Track B/data/Phase_1/test.json` 의 50개 질문을 1-based 인덱스로 노출."""

    def __init__(self, path: Optional[Path]) -> None:
        self._path = path
        self._items: list[dict] = []
        if path and path.is_file():
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(raw, list):
                    self._items = [it for it in raw if isinstance(it, dict)]
            except (json.JSONDecodeError, OSError):
                self._items = []

    @property
    def is_available(self) -> bool:
        return bool(self._items)

    @property
    def path(self) -> Optional[Path]:
        return self._path

    def __len__(self) -> int:
        return len(self._items)

    def question_text(self, n: int) -> str:
        if 1 <= n <= len(self._items):
            return self._items[n - 1].get("task", {}).get("question", "")
        return ""

    def scenario_id(self, n: int) -> str:
        if 1 <= n <= len(self._items):
            return self._items[n - 1].get("scenario_id", "")
        return ""

    def summary(self, n: int, max_chars: int = 90) -> str:
        """질문 첫 문장(또는 truncated) 형태의 한 줄 요약."""
        text = self.question_text(n).strip().replace("\n", " ")
        if not text:
            return "(empty)"
        # 첫 문장 (마침표 기준) — 너무 짧으면 그냥 truncate
        first = text.split(".")[0].strip()
        candidate = first if len(first) >= 20 else text
        if len(candidate) > max_chars:
            return candidate[: max_chars - 3].rstrip() + "..."
        return candidate


# ===========================================================================
# 페이징 유틸 (라우터 IOS `--More--` 비유)
# ===========================================================================


def _read_one_key() -> str:
    """터미널에서 한 키만 읽음 (POSIX). 비-TTY 또는 에러 시 빈 문자열."""
    if not sys.stdin.isatty():
        return ""
    try:
        import termios
        import tty
    except ImportError:
        return sys.stdin.readline()[:1]
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def paged_print(lines: list[str], header: Optional[str] = None) -> None:
    """라우터 IOS `--More--` 스타일 페이징.

    Space=다음 페이지, Enter=한 줄, q/Ctrl+C/Ctrl+D=중단.
    stdin 또는 stdout 이 TTY 가 아니면 페이징 없이 전체 출력.
    """
    if header is not None:
        print(header)

    interactive = sys.stdin.isatty() and sys.stdout.isatty()
    if not interactive:
        for line in lines:
            print(line)
        return

    rows = max(shutil.get_terminal_size().lines - 2, 5)
    if header is not None:
        rows -= 1  # header 차지분 만큼 첫 페이지 줄임

    advance = rows
    i = 0
    while i < len(lines):
        chunk_end = min(i + advance, len(lines))
        for line in lines[i:chunk_end]:
            print(line)
        i = chunk_end
        if i >= len(lines):
            break
        prompt = f"{_Style.DIM}--More-- (Space=next page, Enter=next line, q=quit){_Style.RESET}"
        sys.stdout.write(prompt)
        sys.stdout.flush()
        key = _read_one_key()
        # More 프롬프트 지우기 (커서 줄 시작으로 + 공백 덮기)
        sys.stdout.write("\r" + " " * (len(prompt) + 4) + "\r")
        sys.stdout.flush()
        if key in ("q", "Q", "\x03", "\x04", ""):  # q, Ctrl+C, Ctrl+D, 빈 입력
            break
        if key in ("\r", "\n"):
            advance = 1
        else:  # Space 외 다른 키도 다음 페이지로 간주
            advance = max(shutil.get_terminal_size().lines - 2, 5)


# ===========================================================================
# 응답 출력 포맷터
# ===========================================================================


def _normalize_eol(text: str) -> str:
    """캐시 파일에서 유래한 잉여 개행을 정리한다.

    1. CRLF/CR → LF 정규화 (\\r\\r\\n / \\r\\n / 단독 \\r 모두 처리)
    2. 비어 있거나 공백만 있는 줄을 모두 제거 (서버가 캐시 파일 읽을 때
       universal-newline 변환으로 빈 줄이 대량 삽입되는 케이스 대응)
    3. 끝부분의 잉여 개행 제거 (print 가 \\n 한 번 더 추가하므로)
    """
    if not text:
        return text
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line for line in text.split("\n") if line.strip())


def render_response(result: ApiResult) -> tuple[str, str, bool]:
    """응답을 (본문, 메타라인, 성공여부) 튜플로 변환.

    본문은 stdout, 메타라인은 dim 색으로 표시되며 단발 모드에서는 stderr로 보낸다.
    """
    if result.is_transport_error:
        body = f"{_Style.RED}% {result.transport_error}{_Style.RESET}"
        meta = f"{_Style.DIM}(Tool Server 가 떠 있는지 확인하세요){_Style.RESET}"
        return body, meta, False

    code = result.status_code
    payload = result.body

    # 200: result 필드에 prompt echo 포함된 라우터 출력이 들어 있음
    if code == 200:
        body_text = _normalize_eol(payload.get("result", ""))
        vendor = payload.get("vendor", "?")
        executed = payload.get("command_executed", "")
        meta = f"{_Style.DIM}[OK] vendor={vendor} exec={executed}{_Style.RESET}"
        return body_text, meta, True

    # 403: 권한 차단
    if code == 403:
        msg = payload.get("result") or payload.get("error", "permission denied")
        body = f"{_Style.RED}% Permission denied (403): {msg}{_Style.RESET}"
        return body, "", False

    # 422: 문법 오류 또는 시뮬레이션된 리소스 부재 (서버가 라우터 출력 형식으로 반환)
    if code == 422:
        body = _normalize_eol(payload.get("result", ""))
        reason = payload.get("reason")
        meta_bits = [f"[{code}]"]
        if reason:
            meta_bits.append(f"reason={reason}")
        meta = f"{_Style.YELLOW}{' '.join(meta_bits)}{_Style.RESET}"
        return body, meta, False

    # 404: 알 수 없는 장비 또는 cache miss
    if code == 404:
        msg = payload.get("error") or payload.get("result", "not found")
        return f"{_Style.RED}% Not found (404): {msg}{_Style.RESET}", "", False

    # 400: 클라이언트 요청 누락
    if code == 400:
        msg = payload.get("error", "bad request")
        return f"{_Style.RED}% Bad request (400): {msg}{_Style.RESET}", "", False

    # 그 외 상태 코드는 그대로 노출
    return f"{_Style.RED}% HTTP {code}: {payload}{_Style.RESET}", "", False


# ===========================================================================
# REPL
# ===========================================================================


HELP_TEXT = """\
사용 가능한 명령 (장비 미접속 상태):
  list [prefix]         접속 가능한 장비 목록 (cache 기반). prefix 로 필터 가능.
  connect <device>      장비 세션에 진입 (예: connect Alpha-Center-01)
  question [N]          질문 50개 목록 또는 N번 질문 본문 (페이징 지원)
  set question <N>      권한 컨텍스트 변경 (0 = 권한 검증 우회). cache 기반 자동완성도 갱신됨.
  show session          현재 server URL / question / device / cache_dir / question_file 표시
  help, ?               이 도움말
  quit, exit, Ctrl+D    REPL 종료

장비 접속 후 추가:
  commands [prefix]     현재 장비에서 응답 가능한 명령 목록 (cache 기반). prefix 로 필터 가능.
  help, ?               (인자 없이) commands 와 동일 — 실행 가능한 명령 목록
  disconnect            현재 장비에서 빠져나옴 (exit 도 동일)
  그 외 입력            현재 장비로 명령 전송

자동완성·도움말 (라우터 IOS 비유):
  <Tab>                 connect/list 뒤 장비명, 또는 장비 명령의 다음 단어 후보로 자동완성
  <Tab><Tab>            가능한 후보가 여럿이면 모두 나열
  ... ?<Enter>          줄 끝에 `?` 를 붙이고 Enter — 다음 단어 후보 또는 매칭 명령 나열
                        예) display ip ?  →  routing-table, interface, ...
"""


class NocShell(cmd.Cmd):
    """라우터 SSH 비유로 동작하는 REPL.

    - 장비 미접속: 프롬프트 `[Q{n}] noc>` — connect 명령만 의미 있음.
    - 장비 접속: 프롬프트 `[Q{n}] <Device>` — 모든 입력이 명령으로 전송됨.
    """

    intro = (
        f"Track B Tool Server CLI — 'help' 또는 '?' 로 도움말, Ctrl+D 로 종료\n"
    )
    doc_header = "명령"
    ruler = ""

    def __init__(
        self,
        client: ToolServerClient,
        question_number: int,
        server_url: str,
        registry: CommandRegistry,
        catalog: QuestionCatalog,
    ) -> None:
        super().__init__()
        self._client = client
        self._question = question_number
        self._device: Optional[str] = None
        self._server_url = server_url
        self._registry = registry
        self._catalog = catalog
        self._registry.load(question_number)
        self._refresh_prompt()

    # ---------- 프롬프트 ----------

    def _refresh_prompt(self) -> None:
        q = self._question
        if self._device:
            self.prompt = f"{_Style.CYAN}[Q{q}] <{self._device}>{_Style.RESET} "
        else:
            self.prompt = f"{_Style.CYAN}[Q{q}] noc>{_Style.RESET} "

    # ---------- REPL 명령 ----------

    def do_connect(self, arg: str) -> None:
        """connect <device-name> — 장비 세션 진입."""
        device = arg.strip()
        if not device:
            self._stderr("usage: connect <device-name>")
            return
        # 클라이언트는 장비 존재 여부를 검증하지 않는다 — 첫 명령에서 서버가 알려준다.
        self._device = device
        self._refresh_prompt()
        self._info(f"connected to {device} (서버 검증은 첫 명령에서 수행됨)")

    def do_disconnect(self, _arg: str) -> None:  # pyright: ignore[reportUnusedParameter]
        """disconnect — 현재 장비에서 빠져나옴."""
        if not self._device:
            self._stderr("not connected to any device")
            return
        self._info(f"disconnected from {self._device}")
        self._device = None
        self._refresh_prompt()

    def do_set(self, arg: str) -> None:
        """set question <N> — 권한 컨텍스트(question_number) 변경."""
        parts = arg.strip().split()
        if len(parts) != 2 or parts[0] != "question":
            self._stderr("usage: set question <N>")
            return
        try:
            self._question = int(parts[1])
        except ValueError:
            self._stderr(f"question 값이 정수가 아님: {parts[1]!r}")
            return
        self._registry.load(self._question)
        self._refresh_prompt()
        self._info(f"question_number = {self._question} (cache 갱신됨)")

    def do_show(self, arg: str) -> None:
        """show session — 현재 컨텍스트 출력."""
        if arg.strip() != "session":
            self._stderr("usage: show session")
            return
        device = self._device or "(none)"
        cache = str(self._registry.cache_dir) if self._registry.is_available else "(unavailable)"
        qfile = str(self._catalog.path) if self._catalog.is_available else "(unavailable)"
        print(
            f"server        = {self._server_url}\n"
            f"question_num  = {self._question}\n"
            f"device        = {device}\n"
            f"cache_dir     = {cache}\n"
            f"question_file = {qfile} (총 {len(self._catalog)}개)"
        )

    def do_question(self, arg: str) -> None:
        """question [N] — 인자 없으면 전체 50개 목록(페이징), N이면 해당 질문 본문."""
        if not self._catalog.is_available:
            self._stderr(
                "question 데이터셋을 찾을 수 없음 — --question-file 로 지정하거나"
                " 프로젝트 루트에서 실행하세요."
            )
            return

        arg = arg.strip()
        if arg:
            try:
                n = int(arg)
            except ValueError:
                self._stderr(f"question 번호가 정수가 아님: {arg!r}")
                return
            total = len(self._catalog)
            if not (1 <= n <= total):
                self._stderr(f"범위를 벗어남: 1..{total}")
                return
            sid = self._catalog.scenario_id(n)
            text = self._catalog.question_text(n)
            header = (
                f"{_Style.BOLD}Q{n}{_Style.RESET}"
                f" {_Style.DIM}(scenario {sid}){_Style.RESET}"
            )
            # 긴 paragraph 가 가로 화면을 넘기지 않도록 wrap (TTY 가로폭 - 2)
            width = max(shutil.get_terminal_size().columns - 2, 60)
            wrapped: list[str] = []
            for raw in text.split("\n"):
                if raw.strip():
                    wrapped.extend(textwrap.wrap(raw, width=width) or [raw])
                else:
                    wrapped.append("")
            paged_print(wrapped, header=header)
            return

        # 전체 목록
        lines = [
            f"  {_Style.BOLD}Q{i:>2}{_Style.RESET}  {self._catalog.summary(i)}"
            for i in range(1, len(self._catalog) + 1)
        ]
        paged_print(
            lines,
            header=f"{_Style.DIM}-- 총 {len(self._catalog)}개 질문 — 'question N' 으로 본문 조회 --{_Style.RESET}",
        )

    def do_commands(self, arg: str) -> None:
        """commands [prefix] — 현재 장비에서 응답 가능한 명령 목록."""
        if not self._device:
            self._stderr("장비 미접속 — 'connect <device>' 로 먼저 접속")
            return
        if not self._registry.is_available:
            self._stderr(
                "cache 디렉토리를 찾을 수 없음 — --cache-dir 로 지정하거나"
                " 프로젝트 루트에서 실행하세요."
            )
            return
        prefix = arg.strip()
        cmds = (
            self._registry.matching_commands(self._device, prefix)
            if prefix
            else self._registry.commands(self._device)
        )
        if not cmds:
            if not self._registry.commands(self._device):
                self._stderr(
                    f"장비 '{self._device}' 의 cache 가 question {self._question} 에 없음"
                )
            else:
                print("(매칭되는 명령 없음)")
            return
        for c in cmds:
            print(f"  {c}")
        print(f"{_Style.DIM}-- {len(cmds)}개 --{_Style.RESET}")

    def do_help(self, arg: str) -> None:
        """help [topic] — 인자 없이 호출되면 컨텍스트별 도움말 (장비 접속 시 = commands)."""
        if arg:
            super().do_help(arg)
            return
        if self._device:
            # 라우터 SSH 비유: 장비 접속 후 ? = 사용 가능한 명령 나열
            self.do_commands("")
            return
        print(HELP_TEXT)

    def do_list(self, arg: str) -> None:
        """list [prefix] — 장비 미접속 시 접속 가능한 장비 목록.

        장비 접속 상태에서는 안내 메시지만 출력 (라우터에는 list 명령이 없음).
        """
        if self._device:
            self._stderr(
                f"이미 {self._device} 에 접속됨 — 명령 목록은 'help', '?', 또는 'commands' 사용"
            )
            return
        if not self._registry.is_available:
            self._stderr(
                "cache 디렉토리를 찾을 수 없음 — --cache-dir 로 지정하거나"
                " 프로젝트 루트에서 실행하세요."
            )
            return
        prefix = arg.strip()
        devices = self._registry.devices()
        if prefix:
            devices = [d for d in devices if d.startswith(prefix)]
        if not devices:
            if not self._registry.devices():
                self._stderr(f"question {self._question} 에 cache 된 장비가 없음")
            else:
                print("(매칭되는 장비 없음)")
            return
        for d in devices:
            print(f"  {d}")
        print(f"{_Style.DIM}-- {len(devices)}개 --{_Style.RESET}")

    def do_quit(self, _arg: str) -> bool:  # pyright: ignore[reportUnusedParameter]
        """quit — REPL 종료."""
        return True

    def do_exit(self, arg: str) -> bool:
        """exit — 장비 접속 중이면 disconnect, 아니면 REPL 종료."""
        if self._device:
            self.do_disconnect(arg)
            return False
        return True

    def do_EOF(self, _arg: str) -> bool:  # pyright: ignore[reportUnusedParameter]
        print()  # Ctrl+D 후 개행
        return True

    def emptyline(self) -> bool:  # 빈 줄 입력 시 마지막 명령 반복하지 않도록 override
        return False

    def default(self, line: str) -> None:
        """매핑되지 않은 입력 = 현재 connected 장비로 명령 전송 (또는 `?` 도움말)."""
        # 줄 끝 `?` → 라우터 IOS 스타일 다음-단어 도움말
        stripped = line.rstrip()
        if stripped.endswith("?") and stripped != "?":
            self._show_next_words(stripped[:-1].rstrip())
            return

        if not self._device:
            self._stderr(
                "장비에 연결되어 있지 않음. 'connect <device-name>' 으로 먼저 접속하세요."
            )
            return
        result = self._client.execute(self._device, line, self._question)
        body, meta, _ = render_response(result)
        if body:
            print(body)
        if meta:
            print(meta)

    def _show_next_words(self, prefix: str) -> None:
        """`?` 트리거: 현재 장비에서 prefix 다음에 올 수 있는 단어들을 나열."""
        if not self._device:
            self._stderr("장비 미접속 — 'connect <device>' 로 먼저 접속")
            return
        if not self._registry.is_available:
            self._stderr(
                "cache 디렉토리를 찾을 수 없음 — --cache-dir 로 지정하거나"
                " 프로젝트 루트에서 실행하세요."
            )
            return
        words = self._registry.next_words(self._device, prefix)
        if words:
            print(f"{_Style.DIM}가능한 다음 단어:{_Style.RESET} " + ", ".join(words))
            return
        # 다음 단어가 없으면 = prefix 가 이미 완전 명령이거나 매칭 없음
        cmds = self._registry.matching_commands(self._device, prefix)
        if cmds:
            print(f"{_Style.DIM}매칭 명령:{_Style.RESET}")
            for c in cmds:
                print(f"  {c}")
        else:
            print(f"{_Style.YELLOW}(매칭되는 명령 없음){_Style.RESET}")

    # ---------- 자동완성 (readline / cmd 통합) ----------

    def complete_connect(  # pyright: ignore[reportUnusedParameter]
        self, text: str, _line: str, _begidx: int, _endidx: int
    ) -> list[str]:
        """connect <Tab> — 현재 question 의 cache 에 있는 장비명 자동완성."""
        return [d for d in self._registry.devices() if d.startswith(text)]

    def complete_list(  # pyright: ignore[reportUnusedParameter]
        self, text: str, _line: str, _begidx: int, _endidx: int
    ) -> list[str]:
        """list <Tab> — 장비명 prefix 자동완성."""
        return [d for d in self._registry.devices() if d.startswith(text)]

    # cmd.Cmd 의 base completedefault 는 *ignored 시그니처라 pyright 가
    # incompatible override 경고를 띄움 — 의도된 4-인자 시그니처이므로 무시.
    def completedefault(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, *args: object
    ) -> list[str]:
        """장비 명령의 다음 단어 자동완성. 장비 미접속 시 빈 결과."""
        if len(args) < 3 or not self._device or not self._registry.is_available:
            return []
        text, line, begidx = args[0], args[1], args[2]
        if not isinstance(text, str) or not isinstance(line, str) or not isinstance(begidx, int):
            return []
        prefix = line[:begidx].rstrip()
        words = self._registry.next_words(self._device, prefix)
        return [w for w in words if w.startswith(text)]

    # ---------- 보조 출력 ----------

    @staticmethod
    def _info(msg: str) -> None:
        print(f"{_Style.DIM}* {msg}{_Style.RESET}")

    @staticmethod
    def _stderr(msg: str) -> None:
        print(f"{_Style.YELLOW}! {msg}{_Style.RESET}", file=sys.stderr)


# ===========================================================================
# 실행 모드 진입점
# ===========================================================================


def run_repl(args: argparse.Namespace) -> int:
    client = ToolServerClient(args.server, timeout=args.timeout)
    cache_dir = find_cache_dir(args.cache_dir)
    registry = CommandRegistry(cache_dir)
    if cache_dir is None:
        print(
            f"{_Style.YELLOW}! cache 디렉토리를 찾을 수 없음 — 자동완성·`commands`·`?` 비활성{_Style.RESET}\n"
            f"{_Style.DIM}  --cache-dir 로 명시하거나 프로젝트 루트에서 실행하세요.{_Style.RESET}",
            file=sys.stderr,
        )
    qfile = find_question_file(args.question_file)
    catalog = QuestionCatalog(qfile)
    if not catalog.is_available:
        print(
            f"{_Style.YELLOW}! question 데이터셋을 찾을 수 없음 — `question` 명령 비활성{_Style.RESET}\n"
            f"{_Style.DIM}  --question-file 로 명시하거나 프로젝트 루트에서 실행하세요.{_Style.RESET}",
            file=sys.stderr,
        )
    shell = NocShell(
        client,
        question_number=args.question,
        server_url=args.server,
        registry=registry,
        catalog=catalog,
    )
    if args.device:
        shell.do_connect(args.device)
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        print()  # Ctrl+C 후 깔끔한 개행
    return 0


def run_oneshot(args: argparse.Namespace) -> int:
    if not args.device:
        print("--exec 사용 시 --device 가 필수입니다.", file=sys.stderr)
        return 2
    client = ToolServerClient(args.server, timeout=args.timeout)
    result = client.execute(args.device, args.exec, args.question)
    body, meta, ok = render_response(result)
    if body:
        print(body)
    if meta:
        print(meta, file=sys.stderr)
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="track_b/cli.py",
        description="Track B Tool Server 에 라우터 SSH 처럼 접속하는 CLI",
    )
    parser.add_argument(
        "--server",
        default="http://127.0.0.1:7860",
        help="Tool Server base URL (기본: http://127.0.0.1:7860)",
    )
    parser.add_argument(
        "--question",
        type=int,
        default=0,
        help="권한 컨텍스트로 사용할 question_number (기본 0 = 우회)",
    )
    parser.add_argument(
        "--device",
        help="REPL 시작 시 자동 connect 할 장비 (--exec 모드에서는 필수)",
    )
    parser.add_argument(
        "--exec",
        dest="exec",
        help="단발 모드: 1회 명령 실행 후 종료. --device 가 함께 필요.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP 요청 타임아웃 초 단위 (기본 30)",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="ANSI 컬러 비활성화",
    )
    parser.add_argument(
        "--cache-dir",
        dest="cache_dir",
        default=None,
        help="명령어 자동완성·`commands`·`?` 도움말에 사용할 cache 루트"
        " (기본: ./data/Track B/devices_outputs 자동 탐지)",
    )
    parser.add_argument(
        "--question-file",
        dest="question_file",
        default=None,
        help="`question` 명령에 사용할 질문 데이터셋 JSON"
        " (기본: ./data/Track B/data/Phase_1/test.json 자동 탐지)",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.no_color or not sys.stdout.isatty():
        _Style.disable()
    if args.exec is not None:
        return run_oneshot(args)
    return run_repl(args)


if __name__ == "__main__":
    sys.exit(main())
