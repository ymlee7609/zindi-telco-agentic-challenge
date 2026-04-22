# Q38 Opus 에뮬레이션 + Qwen 개선 전략 플랜

## 1. Context

Zindi Track B Phase_1 에이전트 50문제 실행 결과 Q38만 미해결 상태.

- **Q38**: "PJ area, Hermes-Prime-01 addressing 20.1.4.20 path" (경로 추적)
- **v6_full 결과**: timeout_forced, 880.5 s, 빈 답
- **v6_retry 결과**: forced_answer, 38.3 s, `<tool_call>` XML 태그 오염으로 답 무효
- **핵심 단서**: `Hermes-Prime-01/display_ip_routing-table.txt` 첫 80줄에 **20.1.4.0/24 엔트리 없음**. default route 또는 BGP VPNv4/EVPN 재귀 탐색 필요.

사용자 요구: **Claude API 호출 없이** 현재 Claude Code 세션의 Opus 모델이 `data/Track B/devices_outputs/38/` 의 CLI 출력 파일을 **Read 도구로 직접 조회**해 NOC API를 에뮬레이션하고, 경로를 도출한 뒤 **Qwen3.5-35B-A3B** 가 동일 문제를 해결하도록 프롬프트·전략을 어떻게 바꿔야 하는지 분석·제안한다. 본 세션은 Opus 사고(reasoning)로 풀이하되, 결과는 Qwen 파이프라인에 역반영 가능한 형태로 정리한다.

## 2. 접근 방법

두 축을 병렬로 수행한다.

- **A. Opus DFS 에뮬레이션**: `agent.py` 가 NOC API(`localhost:7860`) 로 `execute_cli_command(device, command)` 하는 흐름을, `devices_outputs/38/<Device>/<command>.txt` 파일 Read로 치환하여 DFS 재귀 탐색을 수행.
- **B. Qwen 역추적 진단**: v6_full/v6_retry 로그와 Opus 성공 경로를 비교하여 Qwen 이 이탈한 단계와 원인을 특정하고, 개선 프롬프트·전략을 도출.

## 3. 단계별 실행 절차 (의사결정 트리)

### 3.1 루트 탐색 (Hermes-Prime-01)

1. Read `data/Track B/devices_outputs/38/Hermes-Prime-01/display_ip_routing-table.txt` 전체 → 20.1.4.20 longest-prefix match 탐색
2. match 없으면 default route(0.0.0.0/0) next-hop IP 채취
3. 보조 테이블 순회 (존재 시):
   - `display_bgp_vpnv4_all_routing-table.txt`
   - `display_bgp_evpn_all_routing-table.txt`
   - `display_ospf_routing.txt`
4. 20.1.4.0/24 을 광고하는 BGP peer / OSPF area / EVPN Type-5 route 식별

### 3.2 Next-hop IP → 장비명 매핑

우선순위:
1. 현재 장비의 `display_current-configuration.txt` 에서 next-hop IP 가 속한 interface 의 `description` 필드 (예: `description From_NodeA_GE1/0/2_To_NodeB_GE1/0/6`)
2. `display_lldp_neighbor_brief.txt` 로 물리 인접 장비 교차 확인
3. 실패 시 devices_outputs/38/ 전 장비의 `display_ip_interface_brief.txt` 를 Grep 으로 스캔해 next-hop IP 를 소유한 장비를 역탐색

### 3.3 DFS 재귀 탐색

- 방문 집합 `visited: set[str]` 관리, depth cap = 8
- 각 홉에서 다음 확인
  - 20.1.4.20/32 또는 20.1.4.0/24 가 Direct / UNR 상태인가 → Yes: 경로 종료
  - Loop 감지 (current ∈ visited) → 즉시 중단, ECMP 대안 탐색
- VPN instance / VRF 분기가 나오면 `display_ip_vpn-instance.txt` 로 RT/RD 확인 후 VRF routing-table 읽기
- SRv6 / L3VPN 이면 `display_srv6-te_policy.txt`, `display_segment-routing_ipv6_local-sid_end_forwarding.txt` 참조

### 3.4 경로 구성 및 evidence 수집

- 출력 포맷: `Hermes-Prime-01->...->TerminalDevice`
- 홉마다 단서 기록: `[hop_i] file=<basename>, prefix=<matched>, nexthop=<ip>, peer=<device>`
- 최종 경로의 내적 일관성 검증 (§6 참조)

### 3.5 Qwen 로그와 비교 진단

- `agent/track_b/results_v6_full/run.log`, `agent/track_b/results_v6_retry/run.log` 의 Q38 구간 tool call 시퀀스를 Opus 경로와 정렬
- 이탈 지점 특정:
  - Qwen 이 BGP VPNv4 / EVPN 테이블을 조회했는가?
  - Default route 채취 후 next-hop IP → 장비 매핑에서 환각 발생 여부?
  - Reasoning 12분 폭주의 입력 프롬프트 크기 추정

## 4. 위험 및 한계

- Ground truth 부재 → 경로 정답 보장 불가. 산출물은 "best-effort, unverified" 로 라벨링
- Control-plane next-hop 과 forwarding path (SRv6 SID) 가 다를 가능성 → evidence 에 둘 다 기록
- DFS 깊이 폭주 / ECMP 다중 경로 충돌 → depth cap 및 visited set 엄수
- 파일 직접 Read 는 `agent.py` 의 `[DUPLICATE-SKIPPED]`, `truncate 12000자` 같은 프로세싱이 적용되지 않음 → Qwen 환경과 엄밀히 동일하지 않을 수 있음을 주석 처리

## 5. 산출물

1. **Q38 best-effort 경로**
   - 단일 라인 답: `Hermes-Prime-01->...->X`
   - Evidence 체인: 홉별 파일·prefix·next-hop 표
2. **Qwen 실패 진단 리포트** (`docs/07_not_solved_recovery_strategy.md` §9 또는 §10 추가)
   - 빈 응답 원인 (reasoning 폭주 vs context overflow)
   - XML 오염 원인 (chat template · stop sequence 가설)
   - 영역 지식 누락 (BGP VPNv4 / EVPN 피벗 휴리스틱)
3. **Qwen 개선 프롬프트 제안**
   - `build_type_hint` Path 분기에 추가할 텍스트 (예: "If target prefix absent in local routing-table, IMMEDIATELY query display bgp vpnv4 all routing-table and display bgp evpn all routing-table before assuming default route.")
   - Stop sequence / output filter 로 `<tool_call>` 태그 차단 제안
   - Fallback: Q38 만 OpenRouter 의 `anthropic/claude-haiku-4-5` 또는 `openai/gpt-4o-mini` 로 재실행하는 전략 D 적용 조건
4. **Submission 반영 방침**
   - `agent/track_b/submission/submission_v6_full_v3.csv` 신규 생성 (v2 복사 후 Q38 만 교체)
   - `agent/track_b/submission/NOTES.md` 에 "Q38: Opus emulation best-effort, unverified" 주석
   - v2 는 안전 버전으로 보존

## 6. 검증 방법

- **홉 간 IP 일치**: hop_i 의 next-hop IP ∈ hop_{i+1} 의 interface IP 집합
- **LLDP 인접성**: hop_i 와 hop_{i+1} 이 서로의 `display_lldp_neighbor_brief.txt` 에 등장
- **목적지 도달성**: 최종 홉 routing-table 에서 20.1.4.20/32 또는 20.1.4.0/24 Direct/UNR
- **ECMP 대칭성**: 두 경로 후보 있으면 LLDP 일관성 더 높은 쪽 채택

## 7. 실행 체크리스트

- [ ] Hermes-Prime-01 routing + BGP VPNv4 + BGP EVPN 파일 Read
- [ ] 20.1.4.0/24 광고 소스 장비 식별
- [ ] DFS 재귀 (depth ≤ 8, visited set) 로 경로 홉 시퀀스 구성
- [ ] 홉 별 evidence 수집 (파일명, prefix, next-hop, peer)
- [ ] LLDP + routing 양방향 검증
- [ ] v6_full / v6_retry Qwen 로그와 비교해 이탈 지점 진단
- [ ] Qwen 개선 프롬프트 패치 초안 작성 (agent.py `build_type_hint` 파트)
- [ ] `docs/07_not_solved_recovery_strategy.md` 에 §9 Opus 에뮬레이션 결과 섹션 추가
- [ ] `agent/track_b/submission/submission_v6_full_v3.csv` 생성 (Q38 만 교체)
- [ ] `agent/track_b/submission/NOTES.md` 에 unverified 주석 기록

## 8. Critical Files

### 읽기 대상 (Q38 에뮬레이션 시 Read)

- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_ip_routing-table.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_bgp_vpnv4_all_routing-table.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_bgp_evpn_all_routing-table.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_ospf_routing.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_current-configuration.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_lldp_neighbor_brief.txt`
- `data/Track B/devices_outputs/38/Hermes-Prime-01/display_ip_interface_brief.txt`
- (DFS 재귀 확장) next-hop 장비 디렉토리 동일 파일군

### 분석 참조

- `agent/track_b/agent.py` — `build_type_hint` (line 340 부근), `_DEVICES_ROOT` (line 288)
- `agent/track_b/results_v6_full/run.log`, `eval_detail.jsonl` — Q38 구간
- `agent/track_b/results_v6_retry/run.log`, `eval_detail.jsonl` — Q38 구간
- `data/Track B/server.py` — command ↔ 파일명 매핑 규칙 확인

### 수정 대상 (실행 phase)

- (선택) `agent/track_b/agent.py` `build_type_hint` Path 분기에 BGP fallback 규칙 추가
- `docs/07_not_solved_recovery_strategy.md` — §9 Opus 에뮬레이션 결과 + Qwen 개선안 추가
- `agent/track_b/submission/submission_v6_full_v3.csv` — 신규 생성 (Q38 only override)
- `agent/track_b/submission/NOTES.md` — 신규 생성 (unverified 라벨)

## 9. 본 플랜의 범위 경계

- **포함**: Opus 에뮬레이션 실행 + Qwen 실패 진단 + 개선 프롬프트 제안 + submission v3 생성
- **제외 (후속 논의)**: 개선 프롬프트로 Qwen 재실행, ensemble(전략 F) 적용, reasoning-lite 모델(전략 D) 실행
