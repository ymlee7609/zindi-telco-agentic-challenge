# TOPO 11개 Opus Ground-Truth (Q01-06, Q29-33)

**baseline**: submission_v12_topofault_rt.csv (Zindi 0.44)
**검증 방법**: LLDP 직접 조회(Q01-06) + interface description/ARP 기반(Q29-33 PJ area는 LLDP 조회 불가)

## 판정 요약

| qid | target | UP ifaces | Opus 판정 | baseline 일치 | 확신도 |
|---|---|---|---|---|---|
| Q01 | Gamma-Aegis-01 | 3 | ✅ Opus = baseline | Yes | HIGH |
| Q02 | Gamma-Axis-02 | 6 | ✅ reverse LLDP 검증 | Yes | HIGH |
| Q03 | Beta-Aegis-02 | 3 | ✅ forward+reverse LLDP | Yes | HIGH |
| Q04 | Beta-Portal-02 | 7 | ✅ forward+reverse LLDP | Yes | HIGH |
| Q05 | Delta-Node-01 | 3 | ✅ forward+reverse LLDP | Yes | HIGH |
| Q06 | Delta-Axis-01 | 6 | ✅ forward+reverse LLDP | Yes | HIGH |
| Q29 | Demeter-Prime-01 | 2 phy | ⚠️ LLDP 없음, solver 신뢰 | Yes | MEDIUM |
| Q30 | Atlas-Prime-01 | 4 phy | ⚠️ LLDP 없음, solver 신뢰 | Yes | MEDIUM |
| Q31 | Janus-Prime-01 | 5 phy | ⚠️ LLDP 없음, solver 신뢰 | Yes | MEDIUM |
| Q32 | Aegis-Prime-01 | 2 trunk | ⚠️ LLDP 없음, solver 신뢰 | Yes | MEDIUM |
| Q33 | Janus-Node-02 | 4 phy | ⚠️ LLDP 없음, solver 신뢰 | Yes | MEDIUM |

**결론**: 11개 전부 baseline 답이 정답 (Q01-06 HIGH 확신, Q29-33 MEDIUM). 즉 baseline 의 TOPO 는 수정 불필요.

## 각 scenario 상세

### Q01 — Gamma-Aegis-01 (이전 q01_answer.md 참조)
```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)\nGamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)\nGamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
```

### Q02 — Gamma-Axis-02
Target 직접 LLDP 불가 (질문 명시). 9개 candidate 중 6개에서 역방향 LLDP 확인. UP 6개 모두 매핑.
```
Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)\nGamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)\nGamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)\nGamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)\nGamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)\nGamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
```

### Q03 — Beta-Aegis-02
UP 3개, LLDP 3개 매핑 (forward + reverse 일치).
```
Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)\nBeta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)\nBeta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE1/0/2)
```

### Q04 — Beta-Portal-02
UP 7개, 7개 LLDP 모두 forward+reverse 일치. 데이터 가장 풍부.
```
Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/6)\nBeta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/6)\nBeta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)\nBeta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE1/0/1)\nBeta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE1/0/1)\nBeta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)\nBeta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
```

### Q05 — Delta-Node-01
UP 3개, LLDP 3개 일치.
```
Delta-Node-01(GE1/0/1)->Delta-Axis-01(GE1/0/1)\nDelta-Node-01(GE1/0/2)->Delta-Axis-02(GE1/0/1)\nDelta-Node-01(GE1/0/3)->Delta-Node-02(GE1/0/3)
```

### Q06 — Delta-Axis-01
UP 6개, LLDP 6개 일치.
```
Delta-Axis-01(GE1/0/1)->Delta-Node-01(GE1/0/1)\nDelta-Axis-01(GE1/0/2)->Delta-Node-02(GE1/0/1)\nDelta-Axis-01(GE1/0/3)->Delta-Node-03(GE1/0/1)\nDelta-Axis-01(GE1/0/4)->Delta-Node-04(GE1/0/1)\nDelta-Axis-01(GE1/0/5)->Delta-Portal-01(GE1/0/1)\nDelta-Axis-01(GE1/0/6)->Delta-Portal-02(GE1/0/1)
```

### Q29 — Demeter-Prime-01 (PJ area)
LLDP context 비어있음 (PJ zone 장비는 `display lldp neighbor brief` 출력이 다름). solver 는 interface description + ARP 기반 추론. UP phy 인터페이스 2개 (GE1/0/0, GE1/0/1).
```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)\nDemeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
```
**Opus 주의**: LLDP 독립 검증 없음. baseline 신뢰. 오답 가능성 배제 못 함.

### Q30 — Atlas-Prime-01 (PJ area)
UP 4개 (GE1/0/0~3). solver 답은 Janus-Prime-01/02 와 Demeter-Prime-01/02 로 매핑.
```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)\nAtlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0)
```

### Q31 — Janus-Prime-01 (PJ area)
UP phy 5개 (GE1/0/0~5 중 일부). solver 5개 링크 매핑 (Atlas-Prime-01/02, PX1, Janus-Prime-02, Aegis-Prime-01).
```
Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)\nJanus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)\nJanus-Prime-01(GE1/0/2)->PX1(GE1/0/0)\nJanus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)\nJanus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
```
**의심**: PX1 은 "Public Cloud / PE" 같은 외부 장비로 추정. context 에 해당 장비 detail 없음.

### Q32 — Aegis-Prime-01 (PJ area)
UP 주로 Eth-Trunk. solver 답은 GE1/0/0, GE1/0/1, GE1/0/3 (Eth-Trunk 멤버 포트일 가능성).
```
Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)\nAegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)\nAegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
```

### Q33 — Janus-Node-02 (PJGFA area)
UP phy 4개 (GE1/0/2~5). solver 4개 링크.
```
Janus-Node-02(GE1/0/2)->Atlas-Node-01(GE1/0/2)\nJanus-Node-02(GE1/0/3)->Atlas-Node-02(GE1/0/2)\nJanus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)\nJanus-Node-02(GE1/0/5)->Janus-Node-01(GE1/0/5)
```

## 주의 사항

- **포맷**: 위 모든 답변은 submission CSV 입력용 포맷 (literal `\n` 구분자). 이 파일 자체는 Markdown 이므로 가독성을 위해 그대로 표시됨.
- **Q29-Q33 약점**: LLDP 검증 부재. baseline 답이 틀렸을 가능성 5~15%. PJ area 에서 Zindi 가 0.44 대비 손실이 있다면 이 구간이 후보.
