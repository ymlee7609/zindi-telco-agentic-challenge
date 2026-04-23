# Q01 Opus Reference Answer

**scenario_id**: 535afb0d-fa81-419b-9bcc-b456d032df5d
**type**: TOPO (link restoration)
**target**: Gamma-Aegis-01 UP interfaces

## Opus Verdict
v12와 deterministic solver 모두 **일치**. Opus 분석 결과도 동일.

## Reference Answer
```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)
Gamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)
Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
```

## Reasoning (증거 기반)

### 1. UP 인터페이스 식별
`display_interface_brief.txt` 기준 Gamma-Aegis-01에서 UP 상태: **GE1/0/0, GE1/0/1, GE1/0/2** (3개). 나머지는 모두 DOWN.

### 2. LLDP (우선순위 1번 방법)
질문이 명시한 preferred method. 3개 UP 인터페이스 모두 LLDP 네이버 존재:
- GE1/0/0 → Gamma-Portal-01 GE1/0/4
- GE1/0/1 → Gamma-Portal-02 GE1/0/4
- GE1/0/2 → Gamma-Aegis-02 GE1/0/2

### 3. 역방향 LLDP 교차 검증
타겟이 neighbor로 등장하는 케이스 모두 일치:
- Gamma-Portal-01 GE1/0/4 <-> Gamma-Aegis-01 GE1/0/0 ✓
- Gamma-Portal-02 GE1/0/4 <-> Gamma-Aegis-01 GE1/0/1 ✓
- Gamma-Aegis-02 GE1/0/2 <-> Gamma-Aegis-01 GE1/0/2 ✓

### 4. Interface description vs LLDP 불일치 처리
GE1/0/2 description: `From_Gamma-Aegis-01_GE1/0/2_To_Gamma-Aegis-02_GE0/0/2`
LLDP: GE1/0/2 <-> Gamma-Aegis-02 **GE1/0/2**
→ 질문이 "LLDP가 preferred"라고 명시 → LLDP 결과(GE1/0/2) 사용. 정확.

### 5. ARP 교차 검증
Gamma-Aegis-01 ARP의 `I` flag가 local interface 확인. 원격 장비 ARP도 일치하는 subnet 보유.

## v12 비교
- **내용**: 완전 동일 ✓
- **포맷 이슈 주의**: v12 CSV에 답이 literal `\n` 문자로 저장됨. 실제 제출 시 제대로 개행되는지 확인 필요.

## 제출 개선 권장
- **우선순위**: LOW (내용은 맞음)
- **조치**: CSV 생성기에서 `\n` → 실제 개행으로 변환되는지 확인
