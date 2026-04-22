ㅎ# Q29 — Topology (PJ area)

| 항목 | 값 |
|---|---|
| 문제 ID | Q29 |
| 유형 | Topology (Link restoration) |
| 시나리오 | PJ area |
| 검증 일시 | 2026-04-22 |
| Tool Server | http://127.0.0.1:7860 |
| 검증 모델 | claude-opus-4-7 |

## 1. 문제 요약

`Demeter-Prime-01` 의 planning data가 삭제됨. 이 노드의 **UP 상태 인터페이스의 링크 연결**을 복원해야 함.

- 직접 쿼리: 명세상 "아니오" — 라우터 자체에는 권한이 있지만 LLDP 응답이 비어 있음
- 출력 포맷: `Demeter-Prime-01(포트)->원격노드(포트)` (라인당 1개)
- 우선순위: link neighbor 직접 조회 → 불가 시 interface description + ARP 조합

## 2. 풀이 단계

### Step 1 — Demeter-Prime-01 의 LLDP / interface 상태 확인

```bash
python agent/track_b/cli.py --question 29 --device Demeter-Prime-01 \
    --exec "display lldp neighbor brief"
```
응답 핵심: **빈 결과** (LLDP 비활성/미수집).

```bash
python agent/track_b/cli.py --question 29 --device Demeter-Prime-01 \
    --exec "display interface brief"
```
UP 포트 식별:
```
GE1/0/0   up  up
GE1/0/1   up  up
GE1/0/5   up  up   (+ subinterface .1~.7)
```

해석: 복원 대상은 GE1/0/0, GE1/0/1, GE1/0/5 세 포트.

### Step 2 — Demeter-Prime-01 의 IP 정보 + ARP 자기 IP 추출

```bash
python agent/track_b/cli.py --question 29 --device Demeter-Prime-01 \
    --exec "display ip interface brief"
```
```
GE1/0/0   192.168.2.2/30   up  up
GE1/0/1   192.168.2.10/30  up  up
```
GE1/0/5 는 L2 trunk(IP 없음).

ARP 에서 자기 MAC 확인:
```
192.168.2.2   3877-7111-0100  I  GE1/0/0   ← Demeter-Prime-01 GE1/0/0 MAC
```

### Step 3 — PJ 영역 이웃들의 ARP 에서 192.168.2.x peer 역추적

```bash
for dev in Demeter-Node-01 Demeter-Node-02 Aegis-Prime-01 Aegis-Prime-02 \
           Atlas-Prime-01 Atlas-Prime-02 Hermes-Prime-01 Hermes-Prime-02 \
           Janus-Prime-01 Janus-Prime-02 Demeter-Prime-02; do
  python agent/track_b/cli.py --question 29 --device "$dev" \
      --exec "display arp" | grep "192\.168\.2\."
done
```

매칭 결과:
- **Atlas-Prime-01 / GE1/0/2**: self `192.168.2.1`, peer `192.168.2.2` (MAC `3877-7111-0100` Dynamic) → **Demeter-Prime-01 GE1/0/0 의 MAC 과 일치**
- **Atlas-Prime-02 / GE1/0/2**: self `192.168.2.9`, peer `192.168.2.10` (MAC `3877-7111-0101` Dynamic) → Demeter-Prime-01 GE1/0/1 IP `192.168.2.10` 와 매칭

### Step 4 — Demeter-Prime-01 GE1/0/5 (L2 trunk) — description 기반

```bash
python agent/track_b/cli.py --question 29 --device Demeter-Prime-01 \
    --exec "display current-configuration" | grep -B 1 -A 8 "interface GE1/0/5$"
```
```
interface GE1/0/5
 description To-PC1-GE1/0/4
 undo shutdown
 port link-type trunk
```

해석: peer 는 description 의 `PC1(GE1/0/4)`. PC1 은 cache 디렉토리에 부재(가상 endpoint) 이므로 역방향 ARP 검증 불가, **description 단서만 신뢰**.

## 3. 도출한 답

```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->PC1(GE1/0/4)
```

근거:
- L1, L2: ARP MAC 매칭(Step 3) — 상호 검증된 양방향 증거
- L3: interface description 단서(Step 4). PC1 은 가상 endpoint 라 역검증 불가하지만 description 외에 단서 없음

## 4. 정답 후보 비교

### 4-A. 03-3_problems.md 정정 전 (잘못된 매핑)

```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)
Gamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)
Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE0/0/2)
```

→ Q29 의 타겟(`Demeter-Prime-01`)과 무관. **v8 CSV 의 Q1 정답**이 03-3 Q29 슬롯에 잘못 들어가 있었음. 정정 작업 완료 — `v8_mapping_audit.md` 참조.

### 4-B. v8 CSV 의 Q29 prediction (정정 후 03-3 의 정답)

```
Demeter-Prime-01(GE1/0/0)->Spine2(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Spine1(GE1/0/2)
Demeter-Prime-01(GE1/0/5)->PC1(GE1/0/4)
```

## 5. 비교 결과 (도출한 답 vs v8 정답)

- **엄격(string-equal)**: ❌ 불일치 (라인 1·2 의 노드 이름 상이, 라인 3 일치)
- **의미(순서·공백 무시)**: 일치성 보류 — 노드 alias 여부 확인 필요

### 차이 상세 — Spine1/Spine2 ↔ Atlas-Prime-01/02 가능성

| 라인 | 도출한 답 (cli.py 검증) | v8 정답 |
|---|---|---|
| L1 | `Atlas-Prime-01(GE1/0/2)` | `Spine2(GE1/0/2)` |
| L2 | `Atlas-Prime-02(GE1/0/2)` | `Spine1(GE1/0/2)` |
| L3 | `PC1(GE1/0/4)` | `PC1(GE1/0/4)` ✓ |

**가설**: PJ 영역에서 `Atlas-Prime-01/02` 가 토폴로지 다이어그램(03-2_topology_pj.svg) 상의 `Spine1/Spine2` 의 alias 일 가능성. 검증 결정적 증거:
- ARP MAC 매칭으로 Demeter-Prime-01(GE1/0/0) ↔ Atlas-Prime-01(GE1/0/2) 양방향 확인됨 — Atlas-Prime-* 는 cache 에 실재
- v8 의 `Spine1/Spine2` 라벨은 cache 디렉토리에 부재 — 즉 v8 은 토폴로지 도면의 논리명을 사용

확인 필요: 03-2_topology_pj 도면의 Spine1/Spine2 가 Atlas-Prime-01/02 와 동일 위치인지 비교

## 6. 사용자 확인 (2026-04-22 추가) — v8 의 Spine1/Spine2 는 잘못된 alias

**PJ Area Network 의 Spine 위치 장비 = `Janus-Prime` 계열** (사용자 확인).
따라서 v8 의 `Spine1/Spine2` 라벨은 채점 기준 표기와 어긋난 잘못된 alias 사용 — **v8 Q29 정답은 틀림**.

### 데이터 vs 토폴로지 정의 충돌 (미해결)

cli.py 로 추가 검증 결과 (2026-04-22):

```bash
# Janus-Prime-01, Janus-Prime-02 의 ARP 에 Demeter-Prime-01 의 MAC(3877-7111-0100)
# 또는 192.168.2.x peer 가 있는지
for dev in Janus-Prime-01 Janus-Prime-02; do
  python agent/track_b/cli.py --question 29 --device "$dev" --exec "display arp" \
      | grep -E "192\.168\.2\.|3877-7111-010[01]"
done
# → 둘 다 매칭 없음
```

```bash
# Demeter-Prime-01 의 peer MAC(3877-7111-0100) 이 어느 장비에 등록돼 있는지
# → Atlas-Prime-01 의 ARP 에서만 Dynamic 엔트리로 발견됨
# → Atlas-Prime-02 도 Demeter-Prime-01 의 GE1/0/1 peer 로 등장
```

| 출처 | Demeter-Prime-01 GE1/0/0 peer | GE1/0/1 peer |
|---|---|---|
| 사용자 정의 (PJ Spine = Janus-Prime) | Janus-Prime 계열 | Janus-Prime 계열 |
| v8 모델 출력 | `Spine2` (잘못된 alias) | `Spine1` (잘못된 alias) |
| cli.py ARP 추적 (시뮬레이션 raw 데이터) | `Atlas-Prime-01(GE1/0/2)` | `Atlas-Prime-02(GE1/0/2)` |

**모순**: 사용자 정의로는 Janus-Prime 이지만, 시뮬레이션 ARP 데이터는 Atlas-Prime 을 가리킴. 세 가능성:
1. 03-2_topology_pj 도면의 Atlas-Prime-* 위치가 사실은 Janus-Prime 으로 라벨링되어야 하는데 도면 작성에 오류
2. PJ Area 안에 여러 Spine 계층이 있고 Demeter-Prime-01 의 직속 peer 는 다른 그룹의 Spine
3. 시뮬레이션 데이터(ARP cache 파일) 자체가 정답 채점 기준과 다르게 생성됨 (challenge 의도된 trap)

도면 `docs/track_b/03-2_topology_pj.svg` + Demeter-Prime-01 의 `display current-configuration` interface description 추가 검증 필요.

## 7. 결론 (갱신)

- **v8 정답 Q29 는 틀림** (Spine1/Spine2 alias 사용 — 채점 정답은 Janus-Prime 계열 표기)
- cli.py 검증 결과(Atlas-Prime-01/02) 도 사용자 정의(Janus-Prime)와 불일치 — **시뮬레이션 데이터 vs 토폴로지 정의 모순** 미해결
- L3 (PC1) 만 양쪽 일치 — 부분 의심 해소

권장 액션:
1. **즉시**: 03-2_topology_pj 도면에서 Demeter-Prime-01 의 직접 peer 가 Janus-Prime 인지 Atlas-Prime 인지 확정
2. v8 정답 자체가 잘못된 사실을 반영해 03-3_problems.md 의 Q29 (및 동일 패턴인 Q30~Q33) 재검토
3. Qwen 모델이 alias 를 사용한 원인 분석 — 별도 TODO 항목으로 등록 (`TODO.md` 참조)
