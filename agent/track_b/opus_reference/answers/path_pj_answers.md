# PATH PJ/PJGFA area 5개 Opus Ground-Truth (Q34-38)

**baseline**: submission_v12_topofault_rt.csv
**검증 한계**: PJ area 장비는 LLDP/routing table context 가 간소화되어 Opus 독립 검증 한계. solver 답의 일관성 + topology 대칭성으로 MEDIUM 확신도.

## 판정 요약

| qid | 경로 특성 | 길이 | Opus 판정 | baseline 일치 | 확신도 |
|---|---|---|---|---|---|
| Q34 | Hermes-Prime-01 → Hermes-Prime-02 (intra-Prime) | 5 hops | ✅ solver 신뢰 | Yes | MEDIUM |
| Q35 | Hermes-Prime-01 → Hermes-Node-01 (Prime→Node) | 11 hops | ✅ Q36 역방향 일관 | Yes | MEDIUM-HIGH |
| Q36 | Hermes-Node-01 → Hermes-Prime-01 (Node→Prime) | 11 hops | ✅ Q35 역방향 일관 | Yes | MEDIUM-HIGH |
| Q37 | Hermes-Node-01 → Hermes-Node-02 (intra-Node) | 5 hops | ✅ solver 신뢰 | Yes | MEDIUM |
| Q38 | Hermes-Prime-01 → Hermes-Node-02 (Prime→Node-02) | 11 hops | ✅ Q35 와 마지막 2-hop 다름 | Yes | MEDIUM |

**결론**: 5개 baseline 전부 maintain. PJ area 독립 검증 불가로 medium 확신도지만 경로 대칭성은 강한 증거.

## 경로 일관성 증거

### Prime zone topology (추정)
- Hermes-Prime-01/02 (edge)
- Demeter-Prime-01/02, Atlas-Prime-01/02 (core)
- Janus-Prime-01/02, Aegis-Prime-01/02 (upstream)
- Eon-Node-01 (boundary)

### Node zone (PJGFA) topology (추정)
- Hermes-Node-01/02 (edge)
- Demeter-Node-01/02, Atlas-Node-01/02 (core)
- Janus-Node-01/02, Aegis-Node-01 (upstream)
- Gaia-Node-01 (boundary)

### Cross-zone link
Eon-Node-01 ↔ Gaia-Node-01 (Prime ↔ Node zone gateway)

### Q35 ↔ Q36 대칭 검증
- Q35: `Hermes-Prime-01 → Demeter-Prime-01 → Atlas-Prime-01 → Janus-Prime-01 → Aegis-Prime-01 → Eon-Node-01 → Gaia-Node-01 → Janus-Node-01 → Atlas-Node-01 → Demeter-Node-01 → Hermes-Node-01`
- Q36: `Hermes-Node-01 → Demeter-Node-01 → Atlas-Node-01 → Janus-Node-01 → Gaia-Node-01 → Eon-Node-01 → Aegis-Prime-01 → Janus-Prime-01 → Atlas-Prime-01 → Demeter-Prime-01 → Hermes-Prime-01`
- 역방향으로 노드 순서 정확히 대응 ✅

### Q35 vs Q38 차이 검증
- Q35 (dst: Hermes-Node-01, IP 20.1.1.10): ...→ Demeter-Node-**01** → Hermes-Node-**01**
- Q38 (dst: Hermes-Node-02, IP 20.1.4.20): ...→ Demeter-Node-**02** → Hermes-Node-**02**
- Destination IP의 마지막 2 hop만 변경. 이전 9 hop 동일. 합리적 ✅

## Reference Answers (submission 포맷)

### Q34
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Demeter-Prime-02->Hermes-Prime-02
```

### Q35
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Janus-Prime-01->Aegis-Prime-01->Eon-Node-01->Gaia-Node-01->Janus-Node-01->Atlas-Node-01->Demeter-Node-01->Hermes-Node-01
```

### Q36
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Janus-Node-01->Gaia-Node-01->Eon-Node-01->Aegis-Prime-01->Janus-Prime-01->Atlas-Prime-01->Demeter-Prime-01->Hermes-Prime-01
```

### Q37
```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

### Q38
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Janus-Prime-01->Aegis-Prime-01->Eon-Node-01->Gaia-Node-01->Janus-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

## 의심 지점 (오답 가능성)

1. **intra-zone 짧은 경로 (Q34, Q37)**: 5 hops. topology 가 full-mesh 인 경우 더 짧은 경로 (3 hops) 가능성. 현 solver 답은 "모든 트래픽이 core (Atlas) 를 경유" 가정. 실제 routing table 이 shortcut 을 가질 수 있음.
2. **cross-zone 11 hops (Q35/Q36/Q38)**: hop 수가 많음. ECMP, BGP best-path, policy-based routing 이 다른 경로를 선택할 수 있음.
3. 우선순위: Zindi 점수 개선 기회가 있다면 Q34/Q37 (짧은 경로의 대안) 가 후속 조사 대상.
