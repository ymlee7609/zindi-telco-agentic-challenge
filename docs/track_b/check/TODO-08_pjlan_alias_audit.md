# TODO-08 결과 — Eon-Node-01 / PJlAN-01 alias 매핑 확인

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 대상 | Q32, Aegis-Prime-01 GE1/0/3 description `To-PJlAN-01-GE1/0/1` |
| 결론 | **PJlAN-01 = Eon-Node-01 의 alias 확정**. v9 답 `Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)` 은 도면 truth 와 일치 |

## 1. 조사 배경

TODO-04 Q30~Q33 검증에서 Q32 v9 답:

```
Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
```

- description 출력은 `To-PJlAN-01-GE1/0/1` (alias)
- 모델이 whitelist 의 Eon-Node-01 로 매핑 → 근거가 약한 추정이거나 실제 alias 인지 확인 필요

## 2. 증거 수집

### 2.1 Aegis-Prime-01 쪽 description

```
data/Track B/devices_outputs/32/Aegis-Prime-01/display_current-configuration.txt:3370:
  interface GigabitEthernet1/0/3
    description To-PJlAN-01-GE1/0/1
    eth-trunk 1

data/Track B/devices_outputs/32/Aegis-Prime-01/display_interface_description.txt:54:
  GE1/0/3(10G)   up   up   To-PJlAN-01-GE1/0/1
```

### 2.2 Eon-Node-01 쪽 역방향 description

```
data/Track B/devices_outputs/32/Eon-Node-01/display_interface_description.txt:35:
  GE1/0/1   up   up   To-Aegis-Prime-01-GE1/0/3
```

→ Eon-Node-01 GE1/0/1 의 description 이 Aegis-Prime-01 GE1/0/3 로 정확히 되돌아옴.

### 2.3 LLDP logbuffer (가장 강력한 증거)

```
data/Track B/devices_outputs/32/Eon-Node-01/display_logbuffer.txt:105 외 다수:
  Interface=GE1/0/1,
  RemotePortId=GigabitEthernet1/0/3,
  RemoteSystemName=Aegis-Prime-01
```

→ Eon-Node-01 의 LLDP 가 이웃 장비를 `Aegis-Prime-01`, 원격 포트를 `GigabitEthernet1/0/3` 으로 인식. 3중 교차 검증 성립.

## 3. 결론

| 항목 | 값 |
|---|---|
| PJlAN-01 정체 | Eon-Node-01 의 운영자 alias |
| Q32 v9 답 (GE1/0/3 라인) | **정답 — 도면 truth 일치** |
| 모델의 매핑 근거 | whitelist 에 Eon-Node-01 만 남아서 guess 한 것이 아니라, ARP/LLDP 결과와 description 역방향 검증으로 해결 (ALIAS WARNING 가드 효과) |

## 4. 추가 체크 — 다른 스코프에서도 PJlAN-01 == Eon-Node-01 인가?

Q32 외 다른 scenario 에서 `PJlAN` 패턴이 나오는지 확인:

```bash
grep -rn "PJlAN" data/"Track B"/devices_outputs/ 2>/dev/null
```

결과: Q32 내부에만 존재 (Aegis-Prime-01 2회). 다른 scenario 로 번지지 않음 → scenario-local alias.

## 5. 시사점

- ALIAS WARNING (TODO-03) + HIGH-ALIAS 가드 (TODO-13) 가 예상대로 작동: alias label 만 보고 답하지 않고 whitelist + ARP/LLDP 로 실제 장비 매핑.
- 이 alias 는 **Q32 local** — Q31 의 "Spine1"/"Spine2" 처럼 scenario 마다 다른 장비를 가리킬 수 있음.
- agent.py 코드 수정 필요 없음 — 현재 가드가 올바르게 동작.

## 6. 후속 조치

- [x] TODO-08 문서화 (본 파일)
- [x] TODO.md 에 결과 반영

상태: **완료** (추가 코드 변경 없음, Q32 v9 답 유지)
