# Track B 검증 결과 색인

검증 대상: `docs/track_b/03-3_problems.md` 및 v8 제출본 매핑 무결성
도구: `agent/track_b/cli.py` (`--exec` 단발 호출, `http://127.0.0.1:7860`)
검증 모델: claude-opus-4-7
시작 일시: 2026-04-22

## 작업 진행 흐름

1. **Q29 시범 검증**: PJ Topology Q29 한 문제를 cli.py 로 풀어 03-3 정답이 잘못된 노드(`Gamma-Aegis-01`) 의 토폴로지로 표시된 것을 발견 → `Q29_topology_PJ.md`
2. **v8 매핑 audit**: 50문제 전체에 대해 v8 CSV ↔ 03-3_problems.md 매핑 검증. **46/50 mismatch** 확인 → `v8_mapping_audit.md`
3. **자동 정정**: 03-3 의 모든 정답 코드 블록을 v8 의 해당 Q prediction 으로 교체. 백업: `docs/track_b/03-3_problems.md.bak`. 50/50 v8 일치 재검증 완료
4. **Q29 재비교**: 정정 후 v8 의 Q29 정답(`Spine2/Spine1/PC1`) 과 cli.py 도출(`Atlas-Prime-01/02/PC1`) 비교 → alias 가설 도출

## 비교 정책

- **엄격(strict)**: string-equal. 라인 순서·공백 차이도 불일치
- **의미(semantic)**: 순서·공백·trailing 무시한 set/multiset 동등성

## 결론 카테고리

| 카테고리 | 의미 |
|---|---|
| **일치** | strict + semantic 모두 일치 |
| **부분일치** | strict 불일치 + semantic 일치 (포맷 차이만) |
| **불일치** | 양 기준 모두 불일치 — 답 수정 권장 |
| **의심** | 도출한 답에 자신 없음 — 추가 검증 필요 |
| **검증 불가** | cache miss 다발 등으로 풀이 진행 불가 |

## 산출물

| 파일 | 종류 | 내용 |
|---|---|---|
| `INDEX.md` | 색인 | 이 파일 — 작업 흐름·결과 표·산출물 한눈에 |
| `TODO.md` | 색인 | TODO-01~10 진행 현황 + 완료 상세 + 미착수 조사 항목 |
| `v8_mapping_audit.md` | 보고서 | 50문제 매핑 진단 + 정정 절차 + 매핑 표 (commit `3487a3d`) |
| `Q29_topology_PJ.md` | 풀이 로그 | PJ Topology Q29 cli.py 시범 검증 + v8 비교 + 도면 truth |
| `TODO-01_qwen_alias_audit.md` | 보고서 | Qwen alias 원인 (description 자체 + Topology hint whitelist 누락) |
| `TODO-02_topology_audit.md` | 보고서 | 도면 vs ARP vs description, 도면 truth 확정 + alias 매핑 표 |
| `TODO-04_q30_q33_audit.md` | 보고서 | Q30~Q33 sample 검증 + 4가지 실패 패턴 분류 |
| `TODO-06_v9_rerun_audit.md` | 보고서 | v9 재실행 결과 + v8↔v9 라인별 비교 + 패치 효과 검증 |
| `TODO-07_q29_failure_audit.md` | 보고서 | Q29 v9 fail 원인 — forced_answer 분기 validation 부재, 신규 TODO-11/12/13 파생 |

코드 변경 (별도 보고서 없음, TODO.md §1 의 진행 결과 + commit 메시지 참조):

| commit | 변경 위치 | 요약 |
|---|---|---|
| `9ed4721` | `agent/track_b/agent.py:288, 412-465` | TODO-03 Topology hint whitelist + ALIAS WARNING + `_DEVICES_ROOT` 경로 버그 수정 |
| `5c748b1` | `agent/track_b/agent.py:438-499, 1373-1418` | TODO-05 `count_up_physical_ports` + `validate_topology_answer` + LINE COUNT GUARD + Topology retry |
| `a6bcec5` | `submission_v6_full_v9.csv` (신규), `03-3_problems.md` | TODO-06 v9 제출본 생성 + Q29(수동),Q31,Q32,Q33 답 갱신 |

## 결과 표

| Q | 유형 | 시나리오 | v8 결론 | v9 결론 | 비고 |
|---|---|---|---|---|---|
| Q29 | Topology | PJ | 불일치 (alias) | v9 fail → cli.py 수동 결과 채택 | 도면 + ARP MAC 양방향 검증으로 truth 확정 |
| Q30 | Topology | PJ | **일치** | **일치 (4/4 도면)** | description 정확명 |
| Q31 | Topology | PJ | 불일치 (6/6 alias) | **일치 (6/6 도면) ⭐** | TODO-03 패치로 alias·hallucination 모두 해소 |
| Q32 | Topology | PJ | 불일치 (1/3) | 부분 일치 (2/3) | Eon-Node-01 alias 미확인, GE1/0/2 누락 |
| Q33 | Topology | PJGFA | 불일치 (1/4 incomplete) | **일치 (4/4) ⭐** | TODO-05 LINE COUNT GUARD 효과 |

## 진행 현황

- v8 매핑 정정: **완료** (50/50 v8 일치 — 단, v8 정답 자체의 정확성은 별개)
- PJ Topology cli.py 검증: 5 / 5 (Q29~Q33) — sample 검증 완료
- TODO-03 (Topology hint whitelist + ALIAS WARNING): **완료**
- TODO-05 (LINE COUNT GUARD + validate_topology_answer): **완료**
- TODO-06 (v9 재실행): **완료** — Q31 alias 6/6 해소, Q33 incomplete 4/4 해소, Q29 fail (cli.py 수동 결과로 대체)
- v9 제출본 생성: `agent/track_b/submission/submission_v6_full_v9.csv` (Q29~Q33 만 갱신, 나머지 v8)
- 03-3_problems.md 갱신: Q29(수동), Q31, Q32, Q33 = v9 답으로 교체
- 후속: TODO-07 (Q29 fail 원인), TODO-08 (Eon-Node-01 alias), TODO-09 (description 잘림), TODO-10 (Zindi 제출)
