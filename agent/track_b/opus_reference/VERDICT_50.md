# Track B 50개 Opus Verdict (baseline = submission_v12_topofault_rt.csv, Zindi 0.44)

**생성일**: 2026-04-23
**Baseline serial**: 016

## 요약 (2026-04-23 수정)

| 유형 | 개수 | baseline vs solver | Opus 판정 | 조치 |
|---|---|---|---|---|
| TOPO | 11 | 내용 일치, 포맷 동일 (literal `\n`은 Zindi 공식 포맷) | **수정 불필요** | 017 폐기 |
| PATH | 15 | 완전 일치 | solver 신뢰 (Q11 증거 검증됨) | 유지 |
| FAULT | 24 | 21개 일치, 3개 solver 실패 | 21개 신뢰, 3개 후속 검증 | 일부 후속 |

## 017 무효 사유

`agent/common/submission_example.csv` 가 Zindi 공식 포맷 예시임을 확인. Track B multi-line 답변은 **literal `\n` (backslash + n)** 을 구분자로 사용하는 것이 정답 포맷. 017 의 "literal → 실제 개행" 변환은 포맷 위반이므로 제출 금지.

## 실제 개선 기회

0.44 baseline 에서 추가 점수 확보 가능 지점:
1. **FAULT Q25, Q28, Q50** (solver conf=L, suspects=[]): 3개 모두 정답 교체 시 최대 +0.06
2. **PATH Q34-Q38 (PJ area)**: 검증 미실시. 오답 있으면 해당 비중만큼 개선
3. **FAULT 21개 중 solver 맞춤 답**: cross-check 필요. 정답률 자체에 여지 있음
4. **scenario 전체 재검토**: 0.44 = 22/50 개 정답 = 28개는 실제 오답. solver == baseline 이라도 오답 가능.

## TOPO (11개) — 포맷 수정 대상

| qid | scenario_id | baseline 내용 | Opus verdict |
|---|---|---|---|
| Q01 | 535afb0d... | Gamma-Aegis-01 3 links | 내용 OK, `\n` literal |
| Q02 | 8ec59f8b... | Gamma-Axis-02 6 links | 내용 OK, `\n` literal |
| Q03 | e4e23bbb... | Beta-Aegis-02 3 links | 내용 OK, `\n` literal |
| Q04 | c2effbaf... | Beta-Portal-02 7 links | 내용 OK, `\n` literal |
| Q05 | 50bb98fe... | Delta-Node-01 3 links | 내용 OK, `\n` literal |
| Q06 | a4a771dd... | Delta-Axis-01 6 links | 내용 OK, `\n` literal |
| Q29 | dd11da6b... | Demeter-Prime-01 2 links | 내용 OK, `\n` literal |
| Q30 | dad1f1ad... | Atlas-Prime-01 4 links | 내용 OK, `\n` literal |
| Q31 | a346ef65... | Janus-Prime-01 5 links | 내용 OK, `\n` literal |
| Q32 | (생략) | Aegis-Prime-01 | 내용 OK, `\n` literal |
| Q33 | (생략) | Janus-Node-02 4 links | 내용 OK, `\n` literal |

**근거**: LLDP 직접 조회로 확인된 링크. Q01 파일럿 분석 완료. 나머지는 solver가 생성한 결과와 baseline이 완전 일치 (포맷 제외).

**Zindi 요구**: "each line represents one link, no extra whitespace characters before, after, or within each line"

**Hypothesis**: literal `\n` (2 chars: backslash + n)는 채점기가 "extra whitespace" 로 보고 오답 처리했을 가능성 높음.

## PATH (15개) — 모두 baseline = solver

| qid | src → dst | baseline | verdict |
|---|---|---|---|
| Q07 | Beta-Node-01 → Gamma-Node-01 GE1/0/2 | Axis-02 route | ✅ dst LLDP peer = Gamma-Axis-02 |
| Q08 | Gamma-Node-01 → Delta-Node-01 GE1/0/2 | Axis-02 route | ✅ Delta-Axis-02 peer |
| Q09 | Beta-Node-03 → Delta-Node-03 GE1/0/2 | Axis-02 route | ✅ Delta-Axis-02 peer |
| Q10 | Gamma-Node-01 → Beta-Node-04 GE1/0/2 | Axis-02 route | ✅ Beta-Axis-02 peer |
| Q11 | Beta-Node-03 → Alpha-Center-02 GE1/0/2 | Axis-02 route | ✅ Routing table 증거 (파일럿) |
| Q12 | Beta-Node-01 → Gamma-Node-01 GE1/0/2 | Axis-02 route | ✅ Gamma-Axis-02 peer |
| Q13 | Gamma-Node-02 → Beta-Node-04 GE1/0/4 | Axis-02 route | ✅ 대칭 패턴 |
| Q14 | Delta-Node-02 → Gamma-Node-02 GE1/0/2 | Axis-02 route | ✅ Gamma-Axis-02 peer |
| Q15 | Gamma-Node-04 → Delta-Node-01 GE1/0/2 | Axis-02 route | ✅ Delta-Axis-02 peer |
| Q16 | Beta-Aegis-02 → Delta-Node-04 GE1/0/2 | Axis-02 route | ✅ Delta-Axis-02 peer |
| Q34 | Hermes-Prime-01 → 10.1.1.20 (PJ) | solver 답 | ⚠️ PJ zone, Opus 심층검증 미실시 |
| Q35 | Hermes-Prime-01 → 20.1.1.10 (PJ) | solver 답 | ⚠️ 동상 |
| Q36 | Hermes-Node-01 → 10.1.1.10 (PJGFA) | solver 답 | ⚠️ 동상 |
| Q37 | Hermes-Node-01 → 20.1.1.20 (PJGFA) | solver 답 | ⚠️ 동상 |
| Q38 | Hermes-Prime-01 → 20.1.4.20 (PJ) | solver 답 | ⚠️ 동상 |

**Q07-Q16**: 파일럿에서 검증된 Axis-02/Portal-02 패턴. 베이스라인이 이미 올바름.
**Q34-Q38**: PJ area, 내부 검증 미실시. 다음 submission에서 Opus 심층 분석 대상.

## FAULT (24개)

### Baseline = solver, 의심 없음 (21개)
Q17-Q24, Q26, Q27, Q39-Q49 (총 21개).

**Q17 파일럿**: `Alpha-Center-02;192.168.70.22;missing static route` 완전 검증됨.

### solver conf=L, 의심 장비 미추출 (3개)
| qid | baseline | 주의점 |
|---|---|---|
| Q25 | `Beta-Node-01;192.168.70.70;static route error` | suspects=[], Opus 심층 재검증 필요 |
| Q28 | `Beta-Node-01;192.168.70.93;static route error` | 동상 |
| Q50 | `Hermes-Prime-01;10.1.1.20;ARP configuration error` | PJ zone, suspects=[] |

이 3개는 017 submission에서 제외 (baseline 유지). 018 이상에서 Opus 심층분석 후 반영 예정.

## 017 제출 후 기대 효과

- TOPO 11개가 "extra whitespace 로 인한 오답" 에서 "정답" 으로 전환 시 +0.22 (11/50)
- 최대 시나리오: 0.44 → 0.66
- 최소 시나리오: 0.44 (Zindi 채점기가 이미 `\n` 을 개행으로 해석하는 경우, 변화 없음)

## 다음 단계 (018 후보)

1. **Q25, Q28, Q50 FAULT 심층 재분석** — 이 3개가 오답이라면 +0.06 잠재
2. **Q34-Q38 PATH (PJ zone) Opus 검증** — PJ area 추가 확인
3. **FAULT baseline = solver 21개 샘플 재검증** — solver 자신감만으로는 부족, Opus cross-check

## 결론

이번 세션에서 50개 scenario 를 체계적으로 분류하고 베이스라인 대비 의심 지점을 식별했다. 가장 확실한 개선 기회(TOPO 포맷)는 017 에 반영 완료. 남은 개선 지점(FAULT 3개, PATH Q34-38)은 다음 submission 에서 다룬다.
