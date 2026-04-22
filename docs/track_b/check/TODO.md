# Track B 검증 후속 과제 (TODO)

검증 작업 진행 중 발견된 후속 조사·개선 항목 모음.

---

## TODO-01 — Qwen 모델의 alias 사용 원인 분석 (우선순위 High)

**발견 일자**: 2026-04-22
**관련 파일**: `Q29_topology_PJ.md`, `agent/track_b/agent.py`
**관련 v8 정답**: Q29 (PJ Topology, Demeter-Prime-01 링크 복원)

### 현상

v8 제출본에서 PJ 영역 Topology 문제(Q29~Q33) 의 정답에 **`Spine1`/`Spine2` 같은 alias 라벨**이 사용됨.

```
# v8 Q29 prediction
Demeter-Prime-01(GE1/0/0)->Spine2(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Spine1(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->PC1(GE1/0/4)
```

PJ Area Network 의 Spine 위치 장비는 **`Janus-Prime` 계열** (사용자 확인). 즉 v8 모델이 **정확한 장비명 대신 토폴로지 다이어그램의 논리 alias**를 그대로 출력 — 채점 기준과 어긋남.

### 의문점

1. **장비명은 cli.py(NOC API) 로 정확히 조회 가능**한 상황이었음:
   - server.py 의 device 맵에 `Janus-Prime-01`, `Atlas-Prime-01` 등 정확 라벨 존재
   - LLDP/ARP/description 응답에도 정확한 장비명이 들어 있음
   - **그런데 왜 모델이 raw alias("Spine1/Spine2", "PC1") 를 그대로 출력했는가?**

2. **Qwen 모델의 답변 추출 경로** 어디에서 alias 가 발생했는가:
   - 모델이 토폴로지 도면(svg/d2)을 학습 데이터에서 본 적이 있어 그 라벨을 우선했을 가능성
   - prompt 또는 system message 에 토폴로지 다이어그램이 포함됐을 가능성
   - test.json 의 question 본문에 alias 가 등장했을 가능성

3. **에이전트 reasoning trace 확인 필요**:
   - `agent/track_b/results_v6_full/eval_detail.jsonl` 또는 동등 trace 파일에서 Q29~Q33 의 모델 reasoning 추출
   - 모델이 어느 단계에서 "Spine1" 이라는 라벨을 만들어냈는지 추적

### 조사 항목

- [ ] `agent/track_b/results_v6_full/` 의 Q29 eval_detail 에서 모델 reasoning + tool call 시퀀스 추출
- [ ] test.json 의 Q29~Q33 task.question 본문에 "Spine"/"PC" alias 가 포함됐는지 확인
- [ ] agent.py 의 prompt 구성 코드에서 어떤 컨텍스트가 모델에 전달되는지 점검 (특히 토폴로지 hint 부분)
- [ ] PJ 영역 외 다른 Topology 답(예: Q1~Q6 Big Data Zone) 에서도 alias 사용이 있는지 sample 확인
- [ ] Qwen 학습 데이터에 PJ 토폴로지 도면이 포함됐는지 (challenge 공개 자료 검토)

### 개선 후보

- agent prompt 에 **"답변에 사용하는 장비명은 반드시 NOC API 응답의 device_name 그대로 사용. 토폴로지 도면의 alias 사용 금지"** 명시
- 답변 후처리 단계에서 alias → 실제 장비명 매핑 적용 (예: `Spine1` → `Janus-Prime-01`) — 단, 매핑 표 확정 필요
- post-validation: 답변에 device 맵에 없는 노드명이 들어 있으면 reject + 재시도

---

## TODO-02 — 시뮬레이션 데이터 vs 토폴로지 정의 모순 해소 (우선순위 High)

**발견 일자**: 2026-04-22
**관련 파일**: `Q29_topology_PJ.md`, `docs/track_b/03-2_topology_pj.svg`

### 현상

PJ Spine 위치 장비에 대해 세 출처가 서로 다른 답을 가리킴:

| 출처 | Demeter-Prime-01 의 Spine peer |
|---|---|
| 사용자 정의 (PJ Area 토폴로지) | Janus-Prime 계열 |
| 시뮬레이션 ARP 데이터 (cli.py 추적) | Atlas-Prime-01/02 |
| v8 모델 출력 | Spine1/Spine2 (alias) |

### 조사 항목

- [ ] `docs/track_b/03-2_topology_pj.svg` 의 Demeter-Prime-01 peer 가 도면상 어느 위치/이름인지 시각 확인
- [ ] `data/Track B/devices_outputs/29/Demeter-Prime-01/display_current-configuration.txt` 의 GE1/0/0, GE1/0/1 interface description 확인
- [ ] 다른 PJ 문제(Q30~Q33)에서도 동일 모순 패턴인지 확인
- [ ] 모순 결론을 PJ 영역 attribute table 로 별도 기록 (도면 vs raw 데이터 alias 표)

---

## 진행 현황

| ID | 제목 | 우선순위 | 상태 | 결과 보고서 |
|---|---|---|---|---|
| TODO-01 | Qwen 모델의 alias 사용 원인 분석 | High | **완료** | `TODO-01_qwen_alias_audit.md` |
| TODO-02 | 시뮬레이션 데이터 vs 토폴로지 정의 모순 해소 | High | **완료** | `TODO-02_topology_audit.md` |
| TODO-03 | agent.py Topology hint 에 device whitelist 주입 (P0 코드 수정) | High | **완료** (commit 9ed4721) | — |
| TODO-04 | Q30~Q33 v8 정답 sample 검증 (PJ Topology alias 영향 범위) | Medium | **완료** | `TODO-04_q30_q33_audit.md` |
| TODO-05 | Topology hint 에 "답 라인 수 = UP 포트 수" 가드 + post-validation | Medium | 미착수 | — |
| TODO-06 | TODO-03 패치 후 PJ Topology Q29~Q33 재실행 (v9 제출본 생성) | Medium | 미착수 | — |

## 핵심 발견 요약 (2026-04-22)

- **Q29 의 alias 출력은 모델 잘못이 아님** — Demeter-Prime-01 의 description 자체가 alias (`To-Spine2-GE1/0/2`). 모델은 SYSTEM_PROMPT 의 "Never invent device names" 룰을 충실히 지켜 description 의 라벨을 정직하게 출력
- **근본 원인**: `agent/track_b/agent.py:412-437` 의 Topology hint 분기에 device whitelist 주입이 빠져 있음 (Path 분기에는 line 462-471 에 있음)
- **사용자 정의 "Spine = Janus-Prime"은 PJ Area 일반 truth 이지만 Q29 답과는 별개** — Demeter-Prime-01 의 직접 peer 는 Atlas-Prime (Leaf 계층). description 의 "Spine1/Spine2"는 운영자가 잘못 적은 alias
- **올바른 Q29 답** (도면 + ARP 양방향 검증): `Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)`, `(GE1/0/1)->Atlas-Prime-02(GE1/0/2)`, `(GE1/0/5)->Hermes-Prime-01(GE1/0/4)`
