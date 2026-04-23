# Q07~Q16 PATH Batch Verdict (Q11 제외 — 별도 문서)

**작성**: Claude Opus 4.7 세션 분석
**대상**: v12_final과 v12_topofault_rt 간 regression된 10개 PATH scenario 중 9개
**Q11 참고**: `q11_answer.md` 에 단독 분석

## 공통 판정

**9개 scenario 전부 solver 답(Axis-02/Portal-02 계열)이 정답**. v12_final의 Axis-01/Portal-01 답변은 regression.

## 판정 근거 (공통 프레임)

### 근거 1: Destination Port의 LLDP peer

각 scenario의 destination port는 Axis-02 계열에 peer됨:

| qid | dst_node | dst_port | LLDP peer | 증거 강도 |
|---|---|---|---|---|
| Q07 | Gamma-Node-01 | GE1/0/2 | **Gamma-Axis-02** | HIGH |
| Q08 | Delta-Node-01 | GE1/0/2 | **Delta-Axis-02** | HIGH |
| Q09 | Delta-Node-03 | GE1/0/2 | **Delta-Axis-02** | HIGH |
| Q10 | Beta-Node-04 | GE1/0/2 | **Beta-Axis-02** | HIGH |
| Q12 | Gamma-Node-01 | GE1/0/2 | **Gamma-Axis-02** | HIGH |
| Q13 | Beta-Node-04 | GE1/0/4 | Beta-Node-03 (Node-to-Node) | MEDIUM |
| Q14 | Gamma-Node-02 | GE1/0/2 | **Gamma-Axis-02** | HIGH |
| Q15 | Delta-Node-01 | GE1/0/2 | **Delta-Axis-02** | HIGH |
| Q16 | Delta-Node-04 | GE1/0/2 | **Delta-Axis-02** | HIGH |

**Q13 보조 근거**: destination이 Beta-Node-04 자신이므로 ingress는 Beta-Axis-01 또는 Axis-02. Gamma → Beta inter-zone의 대칭 패턴(Q07/Q10 확인) 기반으로 Axis-02 경로.

### 근거 2: Gamma/Alpha/Delta 중심의 대칭 routing

Q07에서 상세 확인한 패턴:
- Gamma-Node-01 routing table: Beta zone 모든 prefix → GE1/0/2 (Gamma-Axis-02)
- 역방향(Beta → Gamma)도 대칭으로 Axis-02 경로

모든 scenario의 inter-zone traffic은 "Axis-02 line"을 사용하도록 정적 라우팅되어 있음.

### 근거 3: v12 내부 파일이 이미 정답 보유

| scenario | topofault_rt | final | 차이 |
|---|---|---|---|
| fff16260 (Q07) | Axis-02 | Axis-01 | regression |
| a4f0237a (Q08) | Axis-02 | Axis-01 | regression |
| 71073070 (Q09) | Axis-02 | Axis-01 | regression |
| 634b9b95 (Q10) | Axis-02 | Axis-01 | regression |
| 01455e30 (Q11) | Axis-02 | Axis-01 | regression |
| ae420b76 (Q12) | Axis-02 | Axis-01 | regression |
| f002adc4 (Q13) | Axis-02 | Axis-01 | regression |
| c03fb42a (Q14) | Axis-02 | Axis-01 | regression |
| c78207f0 (Q15) | Axis-02 | Axis-01 | regression |
| ccc12121 (Q16) | Axis-02 | Axis-01 | regression |

**해석**: `gen_v12_rollback_path.py`가 topofault_rt 결과를 특정 조건(아마 "Axis-02를 Axis-01로 fallback")으로 override했을 가능성.

## Reference Answers (9개)

### Q07
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q08
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

### Q09
```
Beta-Node-03->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-03
```

### Q10
```
Gamma-Node-01->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-04
```

### Q12
```
Beta-Node-01->Beta-Axis-02->Beta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-01
```

### Q13
```
Gamma-Node-02->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Beta-Portal-02->Beta-Axis-02->Beta-Node-04
```

### Q14
```
Delta-Node-02->Delta-Axis-02->Delta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-02
```

### Q15
```
Gamma-Node-04->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

### Q16
```
Beta-Aegis-02->Beta-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-04
```

## v13 제출 전략

### 단순 전략 (권장)
`submission_v12_topofault_rt.csv`의 10개 PATH 답변을 기존 final에 merge. 다른 필드(TOPO, FAULT)는 그대로 유지.

```python
# 의사 코드
final = load('submission_v12_final.csv')
rt = load('submission_v12_topofault_rt.csv')
path_sids = [Q07~Q16의 scenario_ids]
for sid in path_sids:
    final[sid] = rt[sid]
save('submission_v13.csv', final)
```

### 예상 점수 영향
- 현재 v12: 0.44 (Zindi)
- 10개 PATH 중 잘못된 답이 정답으로 교체 → PATH 점수 대폭 상승 예상
- 다른 유형(TOPO 11개, FAULT 24개)은 파일럿에서 검증된 대로 이상 없음
- 보수적 추정: +0.05~0.10 상승 가능 (PATH가 50문제 중 10~15개)

### 위험 요소
- Opus 분석이 **9/9 = 100% Axis-02 정답**이라는 점이 지나치게 강함
- 네트워크에 있는 다른 고려사항(BGP weight, traffic engineering, logical bonding) 가능성 배제 불가
- **미리 대비**: 원본 v12 final을 rollback-safe로 보관. v13 제출 결과 확인 후 전체 교체 또는 롤백 결정

### 최종 권장 사항
1. [ ] v13 submission 생성 스크립트 작성 (`gen_v13_submission.py`)
2. [ ] v12_final 백업 (`.bak` 생성)
3. [ ] Zindi 제출 → 점수 확인
4. [ ] 점수 개선 확인 후 TOPO/FAULT 추가 검증 (다음 단계)
5. [ ] 점수 하락 시 v12 복구 및 가설 재검토
