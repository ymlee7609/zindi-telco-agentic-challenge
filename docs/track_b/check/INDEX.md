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

| 파일 | 내용 |
|---|---|
| `v8_mapping_audit.md` | 50문제 매핑 진단 + 정정 절차 + 매핑 표 |
| `Q29_topology_PJ.md` | PJ Topology Q29 cli.py 풀이 + v8 정답 비교 + alias 가설 |

## 결과 표

| Q | 유형 | 시나리오 | 결론 | 비고 |
|---|---|---|---|---|
| Q29 | Topology | PJ | **부분일치 (alias 미확정)** | v8 정답 = `Spine2/Spine1/PC1`, 도출 = `Atlas-Prime-01/02/PC1` — Spine1/2 ↔ Atlas-Prime-* alias 가설. PC1 라인 일치 |

## 진행 현황

- v8 매핑 정정: **완료** (50/50 v8 일치)
- 개별 문제 cli.py 검증: 1 / 22 (Q29만 시범)
- 다음 단계 사용자 결정 대기:
  - (a) PJ 영역 alias 표 확정 + 나머지 PJ 22문제 검증 진행
  - (b) 정정만 완료하고 cli.py 풀이 검증은 별도 세션
  - (c) 매핑 정정 결과 commit + 다음 작업 별도 결정
