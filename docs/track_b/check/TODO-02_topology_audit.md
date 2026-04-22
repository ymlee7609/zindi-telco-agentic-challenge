# TODO-02 결과 — 시뮬레이션 데이터 vs 토폴로지 정의 모순 해소

| 항목 | 값 |
|---|---|
| 작업 일자 | 2026-04-22 |
| 트리거 | Q29 검증에서 ARP(Atlas-Prime) ↔ 사용자 정의(Janus-Prime=Spine) 불일치 |
| 결과 | **모순 해소 — 도면이 truth, ARP 데이터·도면 일치, description 의 alias 가 v8 의 alias 출력 원인** |

## 1. 핵심 결론

**Demeter-Prime-01 의 GE1/0/0, GE1/0/1, GE1/0/5 의 정확한 peer (도면 + ARP + 역검증 모두 일치)**:

| Local 포트 | Peer 장비 | Peer 포트 | description 의 alias |
|---|---|---|---|
| GE1/0/0 | **Atlas-Prime-01** | GE1/0/2 | `Spine2` |
| GE1/0/1 | **Atlas-Prime-02** | GE1/0/2 | `Spine1` |
| GE1/0/5 | **Hermes-Prime-01** | GE1/0/4 | `PC1` |

**v8 의 모든 라벨이 잘못됨**: description 의 alias 그대로 사용 → 도면의 정식 장비명으로 교체 필요.

## 2. 사용자 정보 재해석

사용자: "PJ Area Network 의 Spine 위치 장비 = Janus-Prime 계열"

→ **이 정보는 PJ Area 토폴로지의 일반 truth로 정확함** (도면 line 3-5, Spine layer 의 멤버는 Janus-Prime-01/02). 다만 Q29 의 정답과는 **별개의 사실**:

- Demeter-Prime-01 (VTEP/Leaf-Edge 층) 의 직접 peer 는 **Spine (Janus-Prime) 이 아니라 Leaf (Atlas-Prime)**
- description 에 적힌 `Spine2`/`Spine1` 은 운영자가 **잘못 적은 alias** — 도면의 Spine 계층(Janus-Prime) 을 의미하지 않고, 실제로는 Atlas-Prime-01/02(Leaf) 를 가리킴

즉 description 의 "Spine" 표기는 라벨링 오류 (계층 이름 혼동) 이며, v8 모델이 그 잘못된 alias 를 그대로 답에 옮긴 것.

## 3. 검증 증거

### 3-A. 도면 (`docs/track_b/03-2_topology_pj.d2`)

```d2
# 계층 정의 (line 3-22)
Spine: { Janus_Prime_01, Janus_Prime_02 }
Leaf:  { Atlas_Prime_01, Atlas_Prime_02, Aegis_Prime_01, Aegis_Prime_02 }
VTEP:  { Demeter_Prime_01, Demeter_Prime_02 }
Access: { Hermes_Prime_01, Hermes_Prime_02 }

# Demeter-Prime-01 의 직접 connection (line 51, 55-57)
Access.Hermes_Prime_01 -> VTEP.Demeter_Prime_01: GE1/0/4 -- GE1/0/5
VTEP.Demeter_Prime_01 -> Access.Hermes_Prime_01: GE1/0/5 -- GE1/0/4
VTEP.Demeter_Prime_01 -> Leaf.Atlas_Prime_01:    GE1/0/0 -- GE1/0/2
VTEP.Demeter_Prime_01 -> Leaf.Atlas_Prime_02:    GE1/0/1 -- GE1/0/2
```

### 3-B. cli.py ARP 양방향 검증

- Demeter-Prime-01 GE1/0/0 self IP `192.168.2.2`, MAC `3877-7111-0100`
- Atlas-Prime-01 ARP: `192.168.2.2 / 3877-7111-0100 / Dynamic / GE1/0/2` ← **MAC + IP 모두 매칭**
- Atlas-Prime-02 ARP: `192.168.2.10 / 3877-7111-0101 / Dynamic / GE1/0/2` ← Demeter-Prime-01 GE1/0/1 매칭
- Janus-Prime-01/02 ARP: 192.168.2.x 매칭 **없음**

→ ARP 데이터는 도면과 100% 일치. 이전 분석에서 "ARP 는 약한 증거" 라 본 것은 잘못 — 직접 link peer 의 IP 만 ARP 에 들어옴이 정상.

### 3-C. interface description 의 alias

```bash
python agent/track_b/cli.py --question 29 --device Demeter-Prime-01 \
    --exec "display current-configuration"
```
```
interface GE1/0/0
 description To-Spine2-GE1/0/2     ← "Spine2" alias = Atlas-Prime-01
interface GE1/0/1
 description To-Spine1-GE1/0/2     ← "Spine1" alias = Atlas-Prime-02
interface GE1/0/5
 description To-PC1-GE1/0/4         ← "PC1" alias = Hermes-Prime-01
interface GE1/0/3
 description To-Janus-Prime-02-GE1/0/3   ← 다른 인터페이스는 정확한 장비명 사용
interface GE1/0/4
 description To-Janus-Prime-02-GE1/0/4   ← 정확한 장비명 사용
```

→ **description 자체가 inconsistent**. 같은 노드에서 일부 포트는 alias 를, 다른 포트는 정확명을 사용. 데이터 생성/시뮬레이션 단계의 실수로 추정.

## 4. PJ 영역 alias 표 (description ↔ 실제 장비명)

Q29 의 Demeter-Prime-01 description 으로부터 확인된 alias:

| description 의 alias | 실제 장비명 | 도면 계층 | 검증 방법 |
|---|---|---|---|
| `Spine2` | Atlas-Prime-01 | Leaf (도면상) | ARP MAC + 도면 link |
| `Spine1` | Atlas-Prime-02 | Leaf (도면상) | ARP MAC + 도면 link |
| `PC1` | Hermes-Prime-01 | Access | 도면 link only (ARP 없음, L2 trunk) |

**주의**: description 의 "Spine1/Spine2" 는 도면의 Spine 계층(Janus-Prime) 을 의미하지 않음. 단순히 운영자가 잘못 적은 라벨.

다른 PJ 노드 (Q30~Q33 의 타겟) 도 동일 alias 패턴이 있을지 표본 검증 권장.

## 5. v8 정답 정정 권장

Q29 의 정답을 도면 기준 정확명으로 교체:

```
# v8 (현재 03-3, 잘못된 alias)
Demeter-Prime-01(GE1/0/0)->Spine2(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Spine1(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->PC1(GE1/0/4)

# 정정 후 (도면 truth)
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->Hermes-Prime-01(GE1/0/4)
```

단, 이 정정은 **채점 정답 표기 규칙**에 따름 — 채점이 description alias 도 허용한다면 v8 그대로도 통과 가능. 03-3-1_problems_detail.md 의 출력 포맷 명세에는 alias/정확명 구분이 없음.

## 6. 후속 (TODO-01 으로 이어짐)

- **Qwen 모델이 alias 를 그대로 출력한 원인 = description 자체에 alias 가 박혀 있고, 모델 prompt 에 alias→정확명 매핑 정보가 없음** (TODO-01 의 강한 가설)
- agent.py 의 `compress_tool_result` 가 current-configuration 에서 description 을 우선 추출하므로, alias description 이 모델 컨텍스트로 그대로 전달됨
- 개선: prompt 에 "도면 라벨이나 description 의 alias 가 아닌, server 에 등록된 정확한 device_name 을 사용" 명시 필요
