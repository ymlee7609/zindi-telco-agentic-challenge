# Track B Submissions Index

**단일 진실 원천** — 새 submission을 만들기 전 반드시 이 파일을 먼저 읽고 최신 serial을 확인한다.

## 명명 규칙

- **신규 submission**: `submission_NNN_YYYYMMDD_label.csv`
  - `NNN`: 3자리 단조 증가 serial (017부터, 기존 파일은 legacy로 보존)
  - `YYYYMMDD`: 생성일
  - `label`: 변경 내용 요약 (snake_case, 영문)
  - 예: `submission_017_20260424_fault_recheck.csv`

- **Legacy (기존 파일)**: 이름 변경 없이 보존. 아래 테이블에 serial을 매핑하여 참조.

## 현황 요약

- **현재 최고점**: **serial 018 = 0.48** (Track B 기준)
- **이전 최고**: serial 016 = 0.44 (+0.04 상승 확인)
- **017 상태**: **INVALID — 제출 금지**
- **019 상태**: 제출됨, 결과 0.48 (Q31/Q32 링크 추가 실패)
- **020/022/025/026/027 상태**: 제출됨, **모두 0.48 유지** (5개 독립 영역 probe 전부 실패)
- **021/023/024 상태**: 생성됨, **업로드 불필요** (같은 가설 영역, 020/024 실패로 의미 소진)
- **028 상태**: SANITY CHECK probe 생성 완료, **업로드 대기** ← **다음 행동**
- **이상 현상**: 5개 서로 다른 영역 probe 전부 0.48 유지 → 채점 시스템 재진단 필요
- **참고 문서**: `.moai/reports/track_b_scoring_anomaly_analysis.md`

**실행 매뉴얼**: `agent/track_b/submission/UPLOAD_MANUAL.md` 참조

## 제출 이력 (Zindi에 실제 제출된 것)

| Serial | File | 제출일 | Zindi (Track B) | 비고 |
|---|---|---|---|---|
| **028** | `submission_028_20260424_sanity_check.csv` | (대기) | (미제출) | **SANITY CHECK — Zindi 채점 엔진 진단용**. HIGH 확정 Traditional 3문제(Q1 Topology/Q7 Path/Q17 Fault) 를 의도적 오답으로 교체. 정상 채점 시 -0.06 예상. 0.48 유지 시 채점 미작동 확정. 020~027 5개가 모두 0.48 유지 → 이 probe 가 다음 결정적 진단 |
| 027 | `submission_027_20260424_pj_fault_group_a_prime02.csv` | 2026-04-24 | 0.48 | 제출 완료, 변화 없음. Group A node Prime-02 가설 실패 |
| 026 | `submission_026_20260424_pj_path_q34_q37_direct_l2.csv` | 2026-04-24 | 0.48 | 제출 완료, 변화 없음. Q34 direct L2 가설 실패 |
| 025 | `submission_025_20260424_pj_topo_q29_swap.csv` | 2026-04-24 | 0.48 | 제출 완료, 변화 없음. Q29 direction swap 가설 실패 |
| 022 | `submission_022_20260424_pj_fault_group_c_parent_trunk.csv` | 2026-04-24 | 0.48 | 제출 완료, 변화 없음. Eth-Trunk parent 가설 실패 |
| 020 | `submission_020_20260424_pj_fault_group_a_vxlan.csv` | 2026-04-24 | 0.48 | 제출 완료, 변화 없음. VXLAN configuration error 가설 실패 |
| 026 | `submission_026_20260424_pj_path_q34_q37_direct_l2.csv` | (대기) | (미제출) | base=018, Q34 path: 5-hop VXLAN overlay → 1-hop direct L2 (`Hermes-Prime-01->Hermes-Prime-02`). PJ Path native routing 가설. 성공 시 +0.02 (Q37도 같은 패턴이면 +0.04) |
| 025 | `submission_025_20260424_pj_topo_q29_swap.csv` | (대기) | (미제출) | base=018, Q29 방향 swap (target 왼쪽 → target 오른쪽). HIGH confidence인데 오답이면 포맷 방향성 이슈 가설. 성공 시 +0.02 (Q30~Q33 동일 적용 시 +0.10) |
| 024 | `submission_024_20260424_pj_fault_abd_bgp.csv` | (대기) | (미제출) | base=018, Group A+B+D (7문제) reason: missing static route → BGP configuration error. 020/021/023 모두 실패 시 최종 대안. EVPN은 BGP 기반. 성공 시 +0.14 |
| 023 | `submission_023_20260424_pj_fault_group_bd_vxlan.csv` | (대기) | (미제출) | base=018, Group B+D (Q40/Q41/Q47/Q48) reason: missing static route → VXLAN configuration error. 020 성공 시 확장 단계. 성공 시 +0.08 |
| 022 | `submission_022_20260424_pj_fault_group_c_parent_trunk.csv` | (대기) | (미제출) | base=018, Group C (Q44/Q45) port: Eth-Trunk2.60 → Eth-Trunk2 (parent). 모든 sub-IF down + parent도 down 상태. parent trunk shutdown 가설. 성공 시 +0.04 |
| 021 | `submission_021_20260424_pj_fault_group_a_l3vpn.csv` | (대기) | (미제출) | base=018, Group A (Q39/Q43/Q46) reason: missing static route → L3VPN configuration error. Demeter-Prime-01은 VPN-instance 7개 설정 (vpn1~6+lb-vpn). 020 실패 시 대안. 성공 시 +0.06 |
| 020 | `submission_020_20260424_pj_fault_group_a_vxlan.csv` | (대기) | (미제출) | base=018, Group A (Q39/Q43/Q46) reason: missing static route → VXLAN configuration error. PJ zone EVPN/VXLAN overlay 환경이라 native missing이 아닌 VXLAN 설정 이슈 가설. **첫 업로드 권장**. 성공 시 +0.06 |
| 019 | `submission_019_20260424_topo_eth_trunk.csv` | 2026-04-24 | 0.48 | base=018, Q31/Q32 Topology Tier 5 delta (raw description 교차확증 추가 링크). 점수 변화 없음 → Q31/Q32 둘 다 이미 오답 상태 시사 (PJ zone 전반 오답 가설 강화) |
| **018** | `submission_018_20260423_ground_truth.csv` | 2026-04-23 | **0.48** ✅ | **현재 최고** — base=016, Q25/Q28 HIGH Opus 답 교체. 예상 +0.04 정확 적중. Q25 (Alpha-Center-02 static route error), Q28 (Gamma-Axis-02 routing loop) 모두 정답 확정 |
| 017 | `submission_017_20260423_topo_newline_fix.csv` | — | **무효** | literal `\n` → 실제 개행 변환 시도 (포맷 위반). 제출 안 됨 |
| 016 | `submission_v12_topofault_rt.csv` | 2026-04-23 | 0.44 | 이전 baseline, 018 개선 시작점 |
| 이전 | (기록 없음 — 사용자 확인 후 추가 필요) | — | — | — |

## Zindi 공식 포맷 스펙 (중요)

`agent/common/submission_example.csv` 가 Zindi 공식 포맷 예시. Track B multi-line 답변 (TOPO 여러 링크, FAULT 여러 reason) 은 **literal `\n` (backslash + n 두 문자)** 을 구분자로 사용.

예 (example 507 line):
```
Atlas-Prime-01->Gaia-Node-01->Eon-Node-01\nAtlas-Prime-01\nGaia-Node-01->Demeter-Prime-01->Eon-Node-01
```

`\n` 이 실제 개행 문자가 아님. CSV 값 안에 literal backslash + n 이 저장됨.

**결론**: `submission_v12_topofault_rt.csv` 의 literal `\n` 포맷은 이미 정답 포맷이며, 017 의 "개행 변환" 은 오히려 포맷 위반.

## 로컬 산출물 (Zindi 미제출 포함)

제출 여부는 사용자 확인 필요. serial은 mtime 기반 가정.

| Serial | File | mtime | rows | track_b | Zindi 제출 | 점수 | 설명 |
|---|---|---|---|---|---|---|---|
| 001 | `submission_v6_full.csv` | 2026-04-21 23:33 | 550 | 49 | ? | ? | v6 첫 full 시도 |
| 002 | `submission_v6_full_v2.csv` | 2026-04-22 09:55 | 550 | 49 | ? | ? | v6 반복 |
| 003 | `submission_v6_full_v3.csv` | 2026-04-22 10:07 | 550 | 50 | ? | ? | v6 반복 |
| 004 | `submission_v6_full_v4.csv` | 2026-04-22 14:34 | 550 | 50 | ? | ? | v6 반복 |
| 005 | `submission_v6_full_v5.csv` | 2026-04-22 14:49 | 50 | 0 | ? | ? | 부분 파일 (Track B 비어있음) |
| 006 | `submission_v6_full_v6.csv` | 2026-04-22 14:58 | 50 | 0 | ? | ? | 부분 파일 |
| 007 | `submission_v6_full_v7.csv` | 2026-04-22 15:01 | 550 | 50 | ? | ? | v6 반복 |
| 008 | `submission_v6_full_v8.csv` | 2026-04-22 15:16 | 550 | 50 | ? | ? | v6 반복 |
| 009 | `submission_v6_full_v9.csv` | 2026-04-22 18:46 | 550 | 50 | ? | ? | v6 반복 |
| 010 | `submission_v6_full_v10.csv` | 2026-04-22 19:40 | 550 | 50 | ? | ? | v6 반복 |
| 011 | `submission_v6_full_v11.csv` | 2026-04-23 09:23 | 550 | 50 | ? | ? | v6 마지막 |
| 012 | `submission_v12_topo.csv` | 2026-04-23 11:44 | 550 | 50 | ? | ? | v12 topology 전용 |
| 013 | `submission_v12_det_full.csv` | 2026-04-23 12:04 | 550 | 50 | ? | ? | v12 deterministic + base |
| 014 | `submission_v12_final.csv` | 2026-04-23 14:26 | 550 | 50 | **N** | — | 로컬 최종본, 제출 아님 (PATH 10개가 Axis-01로 회귀됨) |
| 015 | `submission_v12_topo_fault.csv` | 2026-04-23 14:27 | 550 | 50 | ? | ? | topo + fault merged |
| 016 | `submission_v12_topofault_rt.csv` | 2026-04-23 14:27 | 550 | 50 | **Y** | **0.44** | **실제 Zindi 제출본, 현재 최고점** |

## Next Step 체크리스트

1. [ ] 새 submission 생성 전: 이 파일을 Read 하여 최신 serial 확인
2. [ ] 새 serial = 최신 + 1
3. [ ] 새 파일명 = `submission_{NNN}_{YYYYMMDD}_{label}.csv`
4. [ ] base 는 가능하면 Zindi 제출본(`016 = v12_topofault_rt.csv`) 을 시작점으로
5. [ ] 제출 후 Zindi 점수를 받으면 이 파일의 점수 컬럼 업데이트
6. [ ] `is_latest` 는 Zindi 실제 제출본 중 가장 최근 1개에만 Y

## 정책

- **과거 파일 rename 금지** — 기록 혼동 방지
- **인덱스가 사실의 원천** — 파일명이나 mtime만 보고 판단 금지
- **Zindi 제출 여부 불명 항목(`?`)** 은 사용자 확인 후 Y/N 로 업데이트

## 핵심 교훈 (2026-04-23)

`submission_v12_final.csv` 는 이름만 "final" 이지 Zindi 제출본이 아니다. PATH 10개가 topofault_rt 대비 Axis-01/Portal-01 로 회귀됨 — 제출 시 점수 하락 예상. 실제 Zindi 에 올린 것은 `v12_topofault_rt.csv`.
