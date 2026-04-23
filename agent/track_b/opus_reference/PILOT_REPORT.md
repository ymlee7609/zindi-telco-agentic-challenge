# Track B Opus Reference — 파일럿 리포트 (Q01/Q11/Q17)

**작성일**: 2026-04-23
**모델**: Claude Opus 4.7 (세션 직접 처리)
**대상**: 3 scenarios (TOPO/PATH/FAULT 각 1개)
**목적**: Opus reference answer로 v12 제출본 검증 → 제출 전 개선 포인트 선별

---

## 요약

| qid | type | v12 | solver | Opus | verdict | 개선 우선순위 |
|---|---|---|---|---|---|---|
| Q01 | TOPO | ✓ | ✓ | ✓ | 내용 일치 (포맷만 확인) | LOW |
| Q11 | PATH | ❌ | ✓ | ✓ | **v12 오답 발견** | **HIGH** |
| Q17 | FAULT | ✓ | ✓ | ✓ | 완전 일치 | NONE |

**파일럿 3개 결과**: 2개는 v12 정답, 1개(Q11)는 오답 확인.

---

## Q01 — TOPO (일치)

**질문**: Gamma-Aegis-01의 UP 인터페이스 링크 복원
**v12**: `Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4) ... Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)` (3개)
**Opus**: 동일

**조치**:
- 내용 검증 완료
- CSV의 `\n` literal이 실제 개행으로 제출되는지만 확인 필요

---

## Q11 — PATH (불일치, v12 오답)

**질문**: Beta-Node-03 → Alpha-Center-02 GE1/0/2 (192.168.74.13)의 addressing path

| 비교 | v12 | Opus / Solver |
|---|---|---|
| 경로 | Beta-Node-03 → Beta-Axis-01 → Beta-Portal-01 → Alpha-Center-02 | **Beta-Node-03 → Beta-Axis-02 → Beta-Portal-02 → Alpha-Center-02** |
| 근거 | (불명 — routing 미반영) | Beta-Node-03 routing: 192.168.65.2/32 → GE1/0/2 (Axis-02) |

### 핵심 증거
1. **Beta-Node-03 routing table** (`192.168.65.2/32`가 Alpha-Center-02 loopback):
   ```
   192.168.65.2/32  Static via 192.168.65.165 dev GE1/0/2
   ```
   → first hop = **Beta-Axis-02** (GE1/0/2의 LLDP neighbor)

2. **Destination port 매핑**:
   - Alpha-Center-02 GE1/0/2 = 192.168.74.13/30
   - 이 /30 링크의 반대편 = Beta-Portal-02 GE1/0/7 (192.168.74.14/30)
   - → GE1/0/2 목적지는 Portal-**02** 경유가 물리적으로 맞음
   - v12는 Portal-**01** 경유 (GE1/0/1 destination 경로)를 반환 → **목적지 포트 매핑 실수**

### 추정 원인 (v12)
- `gen_v12_path.py` 또는 `path_tracer.py`의 destination IP 추출/매핑 로직이 GE1/0/2 IP를 정확히 192.168.74.13으로 잡지 못함
- 혹은 Beta-Node-03 routing entry 탐색 시 GE1/0/1 우선 hit (tie-break 이슈)

### 개선 액션
- [ ] `agent/track_b/path_tracer.py`에서 dst_port → dst_ip 매핑 함수 점검
- [ ] Beta-Node-03 routing table 조회 시 prefix/ifindex 우선순위 로직 확인
- [ ] PATH 15개 전체를 Opus reference와 대조 → 동일 패턴 오류 있는지 스캔

---

## Q17 — FAULT (일치)

**질문**: Beta-Node-01 → Gamma-Node-01 GE1/0/2 통신 중단, suspects 3개
**v12**: `Alpha-Center-02;192.168.70.22;missing static route`
**Opus**: 동일

### 검증 증거
- Alpha-Center-02 routing table에 **192.168.70.x/30 경로 완전 부재**
- Forward path 첫 fail 지점 = Alpha-Center-02
- Beta-Axis-02, Beta-Portal-02는 inter-zone route 불필요 (다음 홉에서 라우팅)
- Port/log 이상 없음

**조치**: 없음

---

## 전체 50개 확장 전략 (파일럿 결론 기반)

### 발견한 패턴

**1. Deterministic solver의 신뢰도**
- 3개 중 3개 solver 결과 = Opus 결과 일치
- 현재 `agent/track_b/fault_analyzer.py`, `topology_parser.py`는 Opus 수준의 정확도
- **v12가 solver를 제대로 사용 중인지 의심**

**2. v12의 불일치 원인 가설**
- Q11처럼 solver 결과와 v12 최종 답이 다른 경우 존재
- 원인: gen_v12_*.py 파이프라인에서 solver 결과를 무시하거나 override?
- 확인 필요: 전체 50개 중 solver vs v12 diff

**3. 우선 액션 (제출 전)**
- [ ] 50개 전체에 대해 solver 결과 vs v12 답변 diff 생성 (빠르게 자동화)
- [ ] diff 있는 scenario만 Opus로 재검증 (~10~20개 추정)
- [ ] 확신도 높은 diff는 v12를 solver 결과로 교체 → 제출 v13 생성

### 권장 다음 단계

**Option A (권장)**: **Solver-v12 diff 자동 비교 먼저**
- 50개 scenario에 대해 `prepare_context.py` 유사 로직으로 solver output만 수집
- v12 답변과 diff
- diff 있는 건만 Opus session에서 검증 (10~20개)
- 비용/시간 효율적

**Option B**: 50개 전체 Opus 분석
- 완전한 reference dataset 구축
- 시간 많이 소요 (context window 주의)

**Option C**: Q11 같은 PATH 문제만 집중 분석 (15개)
- 가장 의심되는 유형부터 검증

---

## 생성된 산출물

```
agent/track_b/opus_reference/
├── prepare_context.py            # 재사용 가능한 context extractor
├── README.md                     # 사용법
├── PILOT_REPORT.md               # (본 파일)
├── contexts/                     # Opus에 제공한 context (Q01/Q11/Q17)
│   ├── q01_context.md   (5KB)
│   ├── q11_context.md   (8KB)
│   └── q17_context.md   (22KB)
└── answers/                      # Opus reference answers + reasoning
    ├── q01_answer.md
    ├── q11_answer.md
    └── q17_answer.md
```

## 결론

파일럿 성공. 3개 중 1개에서 실제 v12 오답을 발견 (Q11). 이는 다음을 시사:
- 제출 전 local reference answer로 검증하면 점수 개선 가능
- deterministic solver는 이미 Opus 수준 → v12 pipeline이 이를 제대로 반영 못하는 scenario 존재
- 가장 효율적 확장 경로는 **Option A (solver vs v12 diff 먼저)**
