# TODO-09 결과 — description 잘림 / 저품질 케이스 처리

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 대상 | (초기 가설) Q32 Aegis-Prime-01 GE1/0/2 description 이 `to` 로 잘려 있음 |
| 결론 | **초기 가설 오인 정정** + `count_up_physical_ports` (10G) suffix 버그 수정 |

## 1. 초기 가설 재검토

TODO-04 / TODO.md 에서 기록:
> Q32 의 Aegis-Prime-01 GigabitEthernet1/0/2 의 description 이 `to` 로 잘려 있음

실제 확인:

```
data/Track B/devices_outputs/32/Aegis-Prime-01/display_current-configuration.txt:3363:
  description to Janus-Prime-01-GE1/0/5
```

→ **잘리지 않았음**. description 이 lowercase 로 `to Janus-Prime-01-GE1/0/5` 로 정상 존재. 초기 보고서가 오인.

추가 확인: GE1/0/2 는 `up / down` (PHY=up, Protocol=down) 으로 UP/UP 물리 포트가 아니므로 Topology 답에서 제외되는 것이 맞음.

## 2. 실제 발견된 버그 — `count_up_physical_ports` (10G) suffix

Q32 Aegis-Prime-01 에서 `count_up_physical_ports` 가 **0** 을 반환:

- 원인: `display_interface_brief.txt` 에서 `GigabitEthernet1/0/0(10G)   up    up` 같이 bandwidth suffix `(10G)` 가 붙음
- 기존 정규식: `r"^\s*(GE\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+)\s+(\S+)\s+(\S+)"` → suffix 뒤 `\s+` 가 `(10G)` 와 매칭 실패
- 결과: Q32 target 의 LINE COUNT GUARD 미작동 (0 ports → guard 비활성)

### 수정안

`agent/track_b/agent.py:428` 부근:

```python
# BEFORE
r"^\s*(GE\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+)\s+(\S+)\s+(\S+)"

# AFTER (TODO-09 패치)
r"^\s*(GE\d+/\d+/\d+|GigabitEthernet\d+/\d+/\d+)(?:\([^)]*\))?\s+(\*?down|up)\s+(\*?down|up)"
```

- `(?:\([^)]*\))?` : `(10G)`, `(1G)`, `(25G)` 등 optional suffix 허용
- `(\*?down|up)` : `*down` (admin down) 포함 정확한 token 매칭

### 검증 결과

| Q | target | 기존 count | 수정 count | expected (UP/UP 물리) |
|---|---|---|---|---|
| Q29 | Demeter-Prime-01 | 3 | 3 | 3 |
| Q30 | Atlas-Prime-01 | 4 | 4 | 4 |
| Q31 | Janus-Prime-01 | 6 | 6 | 6 |
| Q32 | Aegis-Prime-01 | **0 (버그)** | **3 (복구)** | 3 (GE1/0/3, GE1/0/0, GE1/0/1) |
| Q33 | Janus-Node-02 | 4 | 4 | 4 |

Q32 LINE COUNT GUARD 복구 → 모델이 반드시 3 라인 답 강제.

## 3. 부수 발견 — Q32 v9 답이 사실 3/3 정답

TODO-06 가 Q32 을 `2/3` 로 기록했지만, 재검증:

| 포트 | v9 답 | description | 역방향 확증 | 판정 |
|---|---|---|---|---|
| GE1/0/3 | Eon-Node-01 (GE1/0/1) | To-PJlAN-01-GE1/0/1 (alias) | Eon-Node-01 GE1/0/1 desc = To-Aegis-Prime-01-GE1/0/3 + LLDP log | 정답 (TODO-08) |
| GE1/0/0 | Janus-Prime-02 (GE1/0/5) | To-BorderLeaf2-GE1/0/5 (alias) | Janus-Prime-02 GE1/0/5 desc = To-Aegis-Prime-01-GE1/0/0 | **정답** |
| GE1/0/1 | Aegis-Prime-02 (GE1/0/1) | To-Aegis-Prime-02-GE1/0/1 | 역방향 일치 | 정답 |

→ Q32 v9 실제 **3/3 정답**. TODO-06 집계 정정 필요 (아래 §5).

## 4. description 짧음 fallback — 현재 불필요

Q29~Q33 에서 description 이 비정상적으로 짧은 (길이 < 5, 단어 1개) 케이스 없음. 모든 description 은 `To-` 또는 `to ` 접두사 + peer 장비명 형식.

향후 새 시나리오에서 description 이 빈 문자열 or 한 단어만 ("to", "-") 인 케이스가 발견되면, ALIAS WARNING 섹션에 "description 이 의미 있는 peer 이름을 포함하지 않으면 ARP/LLDP 로 직접 확인 필수" 조항을 추가할 수 있음. 현재는 보류.

## 5. 후속 조치

- [x] `count_up_physical_ports` 정규식 수정 (agent.py:428)
- [x] TODO-09 문서 (본 파일)
- [ ] TODO.md 의 Q32 집계 2/3 → 3/3 정정 (다음 커밋에서)
- [ ] description 잘림 fallback: **Low 유지** — 필요 시점에 추가

## 6. 시사점

1. 초기 가설 (description 잘림) 은 실제 파일 확인 없이 집계된 오인. 데이터 근거 없이 hypothesis 를 TODO 로 승격하는 건 위험.
2. `(10G)` bandwidth suffix 는 Huawei 표준 표시 — 시나리오마다 포함 여부가 달라 validation 규정은 suffix-agnostic 이어야 함.
3. alias 도 노드별 로컬. TODO-02 의 "영역 통일 매핑 불가" 원칙은 Q32 BorderLeaf2/PJlAN-01 사례에서 재확증.

상태: **완료** (코드 수정 1건, 문서 1건)
