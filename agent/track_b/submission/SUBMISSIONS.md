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

- **최신 Zindi 제출본**: `submission_v12_topofault_rt.csv` (serial 016, 점수 0.44)
- **017 상태**: **INVALID — 제출 금지**
- **018 대기**: `submission_018_20260423_ground_truth.csv` (Opus GROUND_TRUTH 기반, Q25/Q28 2건 교체)
- **다음 serial**: 019

## 제출 이력 (Zindi에 실제 제출된 것)

| Serial | File | 제출일 | Zindi 점수 | 비고 |
|---|---|---|---|---|
| 018 | `submission_018_20260423_ground_truth.csv` | 미제출 | — | base=016, Q25/Q28 HIGH 확정 답 (Opus routing 증거). 최대 +0.04 기대 |
| 017 | `submission_017_20260423_topo_newline_fix.csv` | — | **무효** | literal `\n` → 실제 개행 변환은 포맷 위반 |
| 016 | `submission_v12_topofault_rt.csv` | 2026-04-23 | **0.44** | 현재 최고점 (베이스라인) |
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
