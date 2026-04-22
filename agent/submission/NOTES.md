# Submission Notes

## Versions

| File | 생성 | 설명 |
|------|------|------|
| `submission_v6_full.csv` | 2026-04-21 | v6 full 실행 결과, 47 solved |
| `submission_v6_full_v2.csv` | 2026-04-21 | Q11, Q36 을 v6_retry 결과로 덮어쓰기 (48 solved + Q36 타당 forced) |
| `submission_v6_full_v3.csv` | 2026-04-22 | v2 베이스 + **Q38 Opus 에뮬레이션 경로** 반영 |
| `submission_v6_full_v4.csv` | 2026-04-22 | v3 베이스 + **PJ Path Q34~Q37 Opus 에뮬레이션 일괄 재작성** (5문제 모두 overlay 4홉/3홉 형식으로 통일) |

## v3 에서 변경된 항목

### Q38 (PJ Hermes-Prime-01 → 20.1.4.20)

- **이전 (v2)**: 빈 문자열 (v6_full timeout_forced)
- **변경 (v3)**: `Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-02->Hermes-Node-02`
- **도출 방법**: Claude Opus 세션에서 `data/Track B/devices_outputs/38/` CLI 출력 파일 직접 Read 로 경로 재구성
- **근거 요약**:
  1. Hermes-Prime-01 routing-table default route → 10.1.5.1 (Demeter-Prime-01 VRRP)
  2. Demeter-Prime-01 ↔ Hermes-Prime-01 LLDP adjacency 확인
  3. Demeter-Prime-01 vpn4 default → 1.1.5.1 VXLAN (overlay 경유)
  4. Demeter-Node-02 ↔ Hermes-Node-02 LLDP adjacency 확인
  5. Hermes-Node-02 Vlanif40 = 20.1.4.20 (목적지 소유 장비)
- **라벨**: **best-effort, UNVERIFIED**
- **상세**: `docs/07_not_solved_recovery_strategy.md` §9

## 검증되지 않은 항목 (unverified)

| Q | 상태 | 비고 |
|---|------|------|
| Q11 | retry solved | 답변 정상 포맷 |
| Q36 | retry forced_answer | 타당한 PJ 4홉 (`Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Hermes-Prime-01`) 이지만 ground truth 검증 불가 |
| Q38 | Opus 에뮬레이션 | overlay 4홉 경로. 평가자가 underlay 요구 시 대안 경로 필요 (07 §9.3) |

## 대안 경로 (Q38 underlay 버전)

평가자가 underlay 전체 홉 요구하는 경우 후보:
```
Hermes-Prime-01->Demeter-Prime-01->Atlas-Prime-01->Janus-Prime-01->Aegis-Node-01->Janus-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

## v4 에서 변경된 PJ Path 5문제 (Opus 에뮬레이션)

| Q | 경로 | 주요 근거 |
|---|------|-----------|
| Q34 | `Hermes-Prime-01->Demeter-Prime-01->Hermes-Prime-02` | Hermes-Prime-01 ARP: 10.1.1.20 via GE1/0/4 (Demeter-Prime-01 uplink). Hermes-Prime-02 Vlanif10 = 10.1.1.20 |
| Q35 | `Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-01->Hermes-Node-01` | default route 10.1.5.1 → Demeter-Prime-01. 대칭 overlay 경로. Hermes-Node-01 Vlanif10 = 20.1.1.10 |
| Q36 | `Hermes-Node-01->Demeter-Node-01->Demeter-Prime-01->Hermes-Prime-01` | default route 20.1.5.1 → Demeter-Node-01. 대칭 역방향. Hermes-Prime-01 Vlanif10 = 10.1.1.10 |
| Q37 | `Hermes-Node-01->Demeter-Node-01->Hermes-Node-02` | LLDP Hermes-Node-01 GE1/0/0 ↔ Demeter-Node-01. Hermes-Node-02 Vlanif10 = 20.1.1.20 |
| Q38 | `Hermes-Prime-01->Demeter-Prime-01->Demeter-Node-02->Hermes-Node-02` | (기존 v3 경로 유지) |

## 이전 Qwen 답변 vs v4 비교

| Q | Qwen status / answer | v4 Opus 답 | 개선 여부 |
|---|----------------------|-----------|----------|
| Q34 | solved `Hermes-Prime-01` (no arrow) | 3-hop 경로 | 형식 정상화 |
| Q35 | solved `Hermes-Prime-01->Hermes-Spine-01->Hermes-Leaf-01->20.1.1.10` (환각+IP) | 4-hop 실제 장비 | 환각 제거 |
| Q36 | retry forced `Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Hermes-Prime-01` | Demeter-Prime 경유로 수정 | 논리 보정 |
| Q37 | solved `Hermes-Node-01` (no arrow) | 3-hop 경로 | 형식 정상화 |
| Q38 | timeout 빈 답 / retry XML 오염 | 4-hop overlay | 답 생성 |

## 권장 제출

- **1차 권장**: `submission_v6_full_v4.csv` (PJ Path 5문제 전부 Opus 에뮬레이션 정제)
- **Fallback 1**: `submission_v6_full_v3.csv` (Q38만 교체, Q34/35/37은 Qwen 원본 유지)
- **Fallback 2 (가장 보수)**: `submission_v6_full_v2.csv` (Qwen 원본, Q38 빈 답)

## 한계

- Ground truth 검증 불가. 특히 Q35/Q36 중간 경유 (Demeter-Node ↔ Demeter-Prime) 는 물리적으로 직접 연결 아니며 실제는 Atlas/Janus spine 경유. Overlay 추상으로 표현 (Q38과 일관).
- 평가자가 underlay physical 홉을 요구하면 경로 확장 필요 (07 §9.3 참조).
