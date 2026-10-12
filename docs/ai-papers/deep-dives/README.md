# 심층 분석 (Deep dives)

카탈로그(`../README.md`)의 개별 항목은 한두 문장 요약이지만, 여기서는 **주제별로 논문들을 묶어** 문제 정의 → 핵심 메커니즘(수식) → 보고된 결과 → 한계·재현·비판 → 해석 → 열린 질문 순으로 파고듭니다.

> 용어: 본문에서 “NN번 문서”는 카탈로그 문서(`../NN-*.md`), “심층 NN”은 이 폴더의 문서를 가리킵니다.

## 근거 표기 — 모든 문장에 적용
| 표기 | 뜻 |
|---|---|
| **[A]** | 이번 작업에서 웹 검색으로 **확인한** 초록·본문 발췌. 2차 출처(인용 논문의 설명)에 의존한 경우 ‘2차 출처’라고 명시 |
| **[K]** | 제가 알고 있는 내용이지만 **이번에 원문과 대조하지 못함**. 인용 전 확인 필요 |
| **[유도] / [계산]** | 제가 직접 수식을 유도하거나 제시된 수치로 계산한 값 |
| **[J]** | 제 **해석·평가**. 사실 주장이 아니라 의견 |

## 중요한 한계
arXiv·ar5iv·Hugging Face·alphaxiv에 이 환경에서 접속할 수 없어(네트워크 정책), **논문 본문을 직접 읽지 못했습니다.** 따라서
- 표·그림·부록의 세부 수치, 하이퍼파라미터, 절제 실험은 대부분 다루지 못했습니다.
- 수식은 표준 정의를 기억에 따라 적은 것이므로 [K]입니다.
- 이 문서들은 “원문을 읽은 결과”가 아니라 “**확인된 초록 + 후속 연구의 인용 + 저자의 지식**을 종합한 분석”입니다. 본문 열람이 가능해지면 [K]를 [A]로 바꾸는 작업이 가장 가치 있습니다.

## 문서 목록
| # | 주제 | 핵심 질문 |
|---|---|---|
| 01 | [Mamba와 선택적 SSM](01-mamba-selective-state-space.md) | 입력 의존 파라미터가 무엇을 가능하게 했고 무엇을 못 하는가 |
| 02 | [델타 규칙·TTT·Titans](02-test-time-memory-delta-ttt-titans.md) | ‘상태=학습자’ 관점의 새로움은 어디서 나오나 (델타 규칙=한 스텝 경사하강 유도 포함) |
| 03 | [확산 언어모델](03-diffusion-language-models.md) | 마스크 확산이 자기회귀를 대체할 수 있는가 |
| 04 | [희소 어텐션·장문 컨텍스트](04-sparse-attention-long-context.md) | NSA·MoBA·Infini-attention의 증거 수준, 지원 길이 vs 유효 길이 |
| 05 | [스케일링 법칙 계보](05-scaling-laws-lineage.md) | Chinchilla 계수는 얼마나 믿을 만한가 (재현 결과 포함) |
| 06 | [RLVR·GRPO·R1](06-rlvr-grpo-r1-and-critiques.md) | RL은 새 능력을 만드는가, 기존 능력을 선택하는가 |
| 07 | [추론 시 연산·잠재 추론](07-test-time-compute-and-latent-reasoning.md) | 보이게 생각 vs 보이지 않게 생각 — 능력과 감시 가능성의 긴장 |
| 08 | [소형 재귀 추론기·ARC](08-small-recursive-reasoners-hrm-trm-arc.md) | 7M 모델이 LLM을 이겼다는 주장을 어떻게 읽을까 |
| 09 | [DPO와 선호 최적화 계열](09-preference-optimization-dpo-family.md) | DPO 유도, 변형들이 고친 것, 과최적화 |
| 10 | [AGI 정의 삼각측량](10-agi-definitions-triangulation.md) | 정의별로 무엇을 재고 무엇이 빠지는가, 주장 점검 체크리스트 |
| 11 | [재귀적 자기개선 계보](11-recursive-self-improvement-lineage.md) | Gödel Machine에서 DGM·AlphaEvolve까지 — 평가기가 병목 |
| 12 | [실증 안전 연구](12-empirical-safety-deception-misalignment-cot.md) | 정렬 위장·음모·창발적 오정렬·CoT 감시가 보이는 것/보이지 않는 것 |
| 13 | [정렬·감독 이론 계보](13-alignment-theory-and-oversight-lineage.md) | 명세 → 감독 → 일반화 → 시스템 통제로의 이동 |
| 14 | [월드 모델·JEPA 노선](14-world-models-jepa-line.md) | 예측 표현 vs 생성형 월드 모델 |
| 15 | [AGI 경로 다섯 가설 종합](15-agi-pathway-hypotheses-synthesis.md) | 각 가설의 증거·반증·검증 가능한 예측, 공통 병목 |

## 읽는 순서 제안
- AGI 중심: 10 → 15 → 11 → 12 → 13
- 차세대 구조 중심: 01 → 02 → 04 → 03 → 07 → 08
- 학습 방법 중심: 05 → 09 → 06 → 07
