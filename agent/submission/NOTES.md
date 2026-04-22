# Submission Notes

> **[최종 확정] 2026-04-22 — 공식 submission_example.csv 기반 포맷**
>
> 공식 예시 파일 `agent/submission/submission_example.csv` 확인 결과, 올바른 포맷은:
> - Header: **`ID, Track A, Track B`** (대문자 ID, 3-column)
> - 550 scenario rows (Track A: 501 + Track B: 50)
> - Track A 미참가 시 Track A 칸 공백, Track B 칸에 답 입력
> - Track A 전용 scenario: 두 칸 모두 공백
>
> 이전 오해:
> - v1~v4: `scenario_id, Track A, Track B` → `ID column missing` 에러 (header 이름 오류)
> - v5~v6: `id, prediction` 2-column → guideline.md 의 local-eval 포맷을 제출 포맷으로 오해
>
> **v7 이상만 제출 가능**.

## Versions

| File | 생성 | 설명 |
|------|------|------|
| `submission_v6_full.csv` | 2026-04-21 | v6 full 실행 결과, 47 solved |
| `submission_v6_full_v2.csv` | 2026-04-21 | Q11, Q36 을 v6_retry 결과로 덮어쓰기 (48 solved + Q36 타당 forced) |
| `submission_v6_full_v3.csv` | 2026-04-22 | v2 베이스 + **Q38 Opus 에뮬레이션 경로** 반영 |
| `submission_v6_full_v4.csv` | 2026-04-22 | v3 베이스 + **PJ Path Q34~Q37 Opus 에뮬레이션 일괄 재작성** (3-column, 제출 불가) |
| `submission_v6_full_v5.csv` | 2026-04-22 | **`id, prediction` 2-column 규격 준수** — Zindi 제출용. v6_full + Q11 retry + Q34~Q38 Opus v4 병합 |
| `submission_v6_full_v6.csv` | 2026-04-22 | v5 베이스 + **Q36/Q37 retry3 P0/P1/P2 개선 결과** (super-spine physical path) 로 덮어쓰기 |
| `submission_v6_full_v7.csv` | 2026-04-22 | **공식 example 포맷 준수** (`ID, Track A, Track B` 3-column, 550 rows) — Zindi 제출 최종본 |

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

- **제출**: **`submission_v6_full_v7.csv`** (유일한 올바른 포맷)
- v1~v6 는 포맷 미스매치로 제출 불가 (로컬 기록용)

## Submission 생성 Helper

`agent/submission/generate_submission.py` 사용.

```bash
# 기본 + override 병합
python agent/submission/generate_submission.py \
  --results agent/results_v6_full/result.csv \
  --override agent/results_v6_retry/result.csv \
  --override agent/results_v6_retry3/result.csv \
  --out agent/submission/submission_latest.csv
```

- 공식 `submission_example.csv` 의 550 row 순서 유지
- 입력 `id, prediction` 2-column CSV 를 scenario_id 매핑해 Track B 칸에 채움
- 중복 id 는 **후순위 override 가 승리**

## v5 vs v6 차이 (Q36/Q37)

| Q | v5 (Opus overlay) | v6 (retry3 physical) | 근거 |
|---|-------------------|----------------------|------|
| Q36 | `H-N-01->D-N-01->D-P-01->H-P-01` (4홉) | `H-N-01->D-N-01->A-N-01->J-N-01->G-N-01->E-N-01->Ae-P-01->H-P-01` (8홉) | LLDP BFS no-path, super-spine 경유 필요 |
| Q37 | `H-N-01->D-N-01->H-N-02` (3홉) | `H-N-01->D-N-01->A-N-01->D-N-02->H-N-02` (5홉) | BFS LLDP 검증 경로 |

Zindi 가 exact match 라면 한 쪽만 맞음. 평가자가 overlay/physical 어느 쪽 기대하는지 제출 결과로만 확인 가능.

## 제출 규격 (Zindi 공식)

출처: `agent/submission/submission_example.csv`

```csv
ID,Track A,Track B
80e3aa96-815d-4683-980c-16db42eab0ef,,<track B answer or blank>
...
535afb0d-fa81-419b-9bcc-b456d032df5d,,"Gamma-Aegis-01(GE1/0/0)->..."
```

- **Headers**: `ID, Track A, Track B` (대문자 ID, 정확히 3 columns)
- **ID**: scenario_id (UUID, test.json 의 `scenario_id`)
- **Track A**: Track A 참가 시 답변, 미참가 시 공백
- **Track B**: Track B 참가 시 답변, 미참가 시 공백
- **Total rows**: 550 (Track A: 501 + Track B: 50)
- multiline 답변은 `"..."` 로 quote

참고: `data/Track B/agent/evaluate_openclaw_guideline.md` 의 `id, prediction` 포맷은 **로컬 evaluate_openclaw.py 의 per-Q 기록용** 이며 Zindi 업로드 포맷이 아님.

## 한계

- Ground truth 검증 불가. 특히 Q35/Q36 중간 경유 (Demeter-Node ↔ Demeter-Prime) 는 물리적으로 직접 연결 아니며 실제는 Atlas/Janus spine 경유. Overlay 추상으로 표현 (Q38과 일관).
- 평가자가 underlay physical 홉을 요구하면 경로 확장 필요 (07 §9.3 참조).
