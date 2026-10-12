# 00. AGI · 범용 지능 · 재귀적 자기개선 · AGI 안전

AGI(범용 인공지능)의 정의와 측정, 범용 에이전트와 개방형 학습, 자기개선·자동화된 연구, 인지구조 접근, 그리고 AGI 수준 시스템의 안전·정렬·위험평가를 다룬 논문. 이 분야는 ‘AGI 도달 여부’ 자체에 합의가 없고 정의에 따라 결론이 달라지므로, 각 항목의 요약은 논문이 실제로 주장하는 범위만 적었다. 자기개선·자동 연구 에이전트 일부(Darwin Gödel Machine, AI Scientist, ADAS, Absolute Zero 등)는 08·06번 문서에 수록되어 있다.

> 수록 54편 · 검증(V) 47편 · 기억기반(M) 7편

## 목차

- **AGI의 정의 · 측정 · 평가** (9편)
  - 1. Universal Intelligence: A Definition of Machine Intelligence (2007)
  - 2. On the Measure of Intelligence (2019)
  - 3. Levels of AGI: Operationalizing Progress on the Path to AGI (2023)
  - 4. Sparks of Artificial General Intelligence: Early experiments with GPT-4 (2023)
  - 5. Building Machines That Learn and Think Like People (2016)
  - 6. Have we built machines that think like people? (2023)
  - 7. Building Machines that Learn and Think with People (2024)
  - 8. On Benchmarking Human-Like Intelligence in Machines (2025)
  - 9. What the F*ck Is Artificial General Intelligence? (2025)
- **범용 에이전트 · 개방형 학습 · 지속 학습** (9편)
  - 10. A Generalist Agent (2022)
  - 11. Open-Ended Learning Leads to Generally Capable Agents (2021)
  - 12. Human-Timescale Adaptation in an Open-Ended Task Space (2023)
  - 13. Open-Endedness is Essential for Artificial Superhuman Intelligence (2024)
  - 14. On Creativity and Open-Endedness (2024)
  - 15. Boundless Socratic Learning with Language Games (2024)
  - 16. Dota 2 with Large Scale Deep Reinforcement Learning (2019)
  - 17. Overcoming catastrophic forgetting in neural networks (2016)
  - 18. Large Language Models as General Pattern Machines (2023)
- **재귀적 자기개선 · 자동화된 연구** (7편)
  - 19. Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements (2003)
  - 20. Large Language Models Can Self-Improve (2022)
  - 21. Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement (2024)
  - 22. AlphaEvolve: A coding agent for scientific and algorithmic discovery (2025)
  - 23. Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024)
  - 24. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops (2026)
  - 25. Self-Improvements in Modern Agentic Systems: A Survey (2026)
- **인지구조 접근 · 월드 모델 중심 설계** (2편)
  - 26. Cognitive Architectures for Language Agents (2023)
  - 27. A Path Towards Autonomous Machine Intelligence (2022)
- **AGI 안전 · 정렬 · 위험 평가** (25편)
  - 28. Concrete Problems in AI Safety (2016)
  - 29. AGI Safety Literature Review (2018)
  - 30. AI safety via debate (2018)
  - 31. Scalable agent alignment via reward modeling: a research direction (2018)
  - 32. Unsolved Problems in ML Safety (2021)
  - 33. The Alignment Problem from a Deep Learning Perspective (2022)
  - 34. Scaling Laws for Reward Model Overoptimization (2022)
  - 35. Measuring Progress on Scalable Oversight for Large Language Models (2022)
  - 36. Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision (2023)
  - 37. Model evaluation for extreme risks (2023)
  - 38. Evaluating Frontier Models for Dangerous Capabilities (2024)
  - 39. Sabotage Evaluations for Frontier Models (2024)
  - 40. Evaluating Frontier Models for Stealth and Situational Awareness (2025)
  - 41. Tell me about yourself: LLMs are aware of their learned behaviors (2025)
  - 42. An Overview of Catastrophic AI Risks (2023)
  - 43. Natural Selection Favors AIs over Humans (2023)
  - 44. Managing extreme AI risks amid rapid progress (2023)
  - 45. Frontier AI Regulation: Managing Emerging Risks to Public Safety (2023)
  - 46. An Approach to Technical AGI Safety and Security (2025)
  - 47. Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety (2025)
  - 48. Distributional AGI Safety (2025)
  - 49. The Singapore Consensus on Global AI Safety Research Priorities (2025)
  - 50. The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment (2024)
  - 51. Why do Experts Disagree on Existential Risk and P(doom)? A Survey of AI Experts (2025)
  - 52. The AI risk repository: A meta-review, database, and taxonomy of risks from artificial intelligence (2024)
- **기계 의식 · 도덕적 지위** (2편)
  - 53. Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (2023)
  - 54. Principles for Responsible AI Consciousness Research (2025)

## AGI의 정의 · 측정 · 평가

### 00-01. Universal Intelligence: A Definition of Machine Intelligence

- **식별자**: [arXiv:0712.3329](https://arxiv.org/abs/0712.3329)
- **연도 / 저자·기관**: 2007 / Legg & Hutter
- **검증 상태**: ✅ 검증(V)
- **태그**: `AGI-definition`, `universal-intelligence`
- **요약**: 전문가들의 지능 정의에서 공통 특징을 추려, 다양한 환경에서 목표를 달성하는 능력을 하나의 척도로 형식화한 고전. 보편적 최적 학습 에이전트(AIXI)와 연결한다(Minds & Machines 2007).

### 00-02. On the Measure of Intelligence

- **식별자**: [arXiv:1911.01547](https://arxiv.org/abs/1911.01547)
- **연도 / 저자·기관**: 2019 / Chollet
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ARC`, `skill-acquisition-efficiency`
- **요약**: 지능을 ‘이미 가진 기술의 양’이 아니라 사전지식·경험·난이도를 통제한 ‘기술 습득 효율’로 정의하고, 이를 재는 ARC 벤치마크를 제안.

### 00-03. Levels of AGI: Operationalizing Progress on the Path to AGI

- **식별자**: [arXiv:2311.02462](https://arxiv.org/abs/2311.02462)
- **연도 / 저자·기관**: 2023 / Morris et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AGI-levels`, `taxonomy`
- **요약**: 성능(깊이)과 일반성(폭) 두 축으로 AGI를 Emerging부터 Superhuman까지 단계화하고, 자율성 수준도 별도로 구분하는 분류 체계.

### 00-04. Sparks of Artificial General Intelligence: Early experiments with GPT-4

- **식별자**: [arXiv:2303.12712](https://arxiv.org/abs/2303.12712)
- **연도 / 저자·기관**: 2023 / Bubeck et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AGI`, `GPT-4`, `qualitative`
- **요약**: GPT-4 초기 버전을 수학·코딩·비전·심리 이론 등 다양한 과업으로 정성 평가하고 ‘AGI의 불씨’로 해석했다. 방법론의 엄밀성에 대한 비판이 있었다.

### 00-05. Building Machines That Learn and Think Like People

- **식별자**: [arXiv:1604.00289](https://arxiv.org/abs/1604.00289)
- **연도 / 저자·기관**: 2016 / Lake, Ullman, Tenenbaum, Gershman
- **검증 상태**: ✅ 검증(V)
- **태그**: `cognitive-science`, `causal-models`, `compositionality`
- **요약**: 딥러닝 시스템이 인간과 다른 점을 짚고 인과 모델, 직관 물리·심리 이론에 기초한 학습, 구성성(compositionality)과 학습하는 법 배우기를 통한 빠른 일반화를 제안(Behavioral and Brain Sciences).

### 00-06. Have we built machines that think like people?

- **식별자**: [arXiv:2311.16093](https://arxiv.org/abs/2311.16093)
- **연도 / 저자·기관**: 2023 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `human-likeness`, `evaluation`
- **요약**: 기계가 사람처럼 사고하는지 점검한 2023년 연구(ID·제목만 확인).

### 00-07. Building Machines that Learn and Think with People

- **식별자**: [arXiv:2408.03943](https://arxiv.org/abs/2408.03943)
- **연도 / 저자·기관**: 2024 / Collins et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `human-AI-collaboration`
- **요약**: ‘사람처럼’이 아니라 ‘사람과 함께’ 학습·사고하는 기계를 지향한 후속 논의(Nature Human Behaviour 2024로 인용됨).

### 00-08. On Benchmarking Human-Like Intelligence in Machines

- **식별자**: [arXiv:2502.20502](https://arxiv.org/abs/2502.20502)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `benchmarking`, `human-likeness`
- **요약**: 기계의 인간 유사 지능을 벤치마크로 재는 방식을 비판적으로 다룬 2025년 연구(ID·제목만 확인).

### 00-09. What the F*ck Is Artificial General Intelligence?

- **식별자**: [arXiv:2503.23923](https://arxiv.org/abs/2503.23923)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `AGI-definition`, `position`
- **요약**: AGI 개념 자체를 정리하는 2025년 글(ID·제목만 확인).

## 범용 에이전트 · 개방형 학습 · 지속 학습

### 00-10. A Generalist Agent

- **식별자**: [arXiv:2205.06175](https://arxiv.org/abs/2205.06175)
- **연도 / 저자·기관**: 2022 / Reed et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gato`, `generalist-agent`, `multi-task`
- **요약**: 하나의 Transformer와 같은 가중치로 게임, 이미지 캡션, 대화, 로봇 팔 제어 등 600여 과제를 수행한 Gato. 범용 에이전트의 초기 사례이나 개별 과제 전문 모델보다 우월하지는 않았다.

### 00-11. Open-Ended Learning Leads to Generally Capable Agents

- **식별자**: [arXiv:2107.12808](https://arxiv.org/abs/2107.12808)
- **연도 / 저자·기관**: 2021 / Open-Ended Learning Team (DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `XLand`, `open-ended-learning`, `generally-capable`
- **요약**: 절차적으로 생성되는 3D 세계·다인 게임 환경 XLand에서 학습 과제를 계속 바꾸는 개방형 학습으로, 사람이 풀 수 있는 모든 평가 레벨에서 보상을 얻는 에이전트를 만들었다. 고정 과제 분포의 단순 RL은 실패.

### 00-12. Human-Timescale Adaptation in an Open-Ended Task Space

- **식별자**: [arXiv:2301.07608](https://arxiv.org/abs/2301.07608)
- **연도 / 저자·기관**: 2023 / Adaptive Agents Team (DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AdA`, `in-context-RL`, `XLand`
- **요약**: 10^40개 이상의 가능한 과제를 가진 XLand 확장판에서 학습해, 보지 못한 손수 설계 과제에 사람과 비슷한 시간 척도로 적응하는 에이전트.

### 00-13. Open-Endedness is Essential for Artificial Superhuman Intelligence

- **식별자**: [arXiv:2406.04268](https://arxiv.org/abs/2406.04268)
- **연도 / 저자·기관**: 2024 / Hughes et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `open-endedness`, `ASI`, `position`
- **요약**: 참신성과 학습가능성에 기반한 개방형(open-ended) 정의를 제시하고, 초인적 지능에는 개방형 시스템이 필수적이라 주장하는 입장 논문. 파운데이션 모델 기반 경로와 안전 함의도 논의(ICML position).

### 00-14. On Creativity and Open-Endedness

- **식별자**: [arXiv:2405.18016](https://arxiv.org/abs/2405.18016)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `creativity`, `open-endedness`
- **요약**: 창의성과 개방형 진화의 관계를 다룬 2024년 논의(ID·제목만 확인).

### 00-15. Boundless Socratic Learning with Language Games

- **식별자**: [arXiv:2411.16905](https://arxiv.org/abs/2411.16905)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `self-play`, `language-games`
- **요약**: 언어 게임을 통한 경계 없는 소크라테스식 자기 학습을 다룬 2024년 논의(ID·제목만 확인).

### 00-16. Dota 2 with Large Scale Deep Reinforcement Learning

- **식별자**: [arXiv:1912.06680](https://arxiv.org/abs/1912.06680)
- **연도 / 저자·기관**: 2019 / Berner et al. (OpenAI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `OpenAI-Five`, `large-scale-RL`, `self-play`
- **요약**: 대규모 자기 대국 강화학습으로 Dota 2에서 인간 최상위권과 경쟁한 OpenAI Five 보고서. 장기 계획·팀 협동이 필요한 환경에서 RL의 확장성을 보였다.

### 00-17. Overcoming catastrophic forgetting in neural networks

- **식별자**: [arXiv:1612.00796](https://arxiv.org/abs/1612.00796)
- **연도 / 저자·기관**: 2016 / Kirkpatrick et al. (DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `continual-learning`, `EWC`
- **요약**: 이전 과제에 중요한 가중치의 학습을 늦추는 EWC로 순차 학습 시 파국적 망각을 줄임(MNIST, Atari 순차 학습으로 검증).

### 00-18. Large Language Models as General Pattern Machines

- **식별자**: [arXiv:2307.04721](https://arxiv.org/abs/2307.04721)
- **연도 / 저자·기관**: 2023 / Mirchandani et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `in-context-pattern`, `sequence-completion`, `robotics`
- **요약**: LLM이 무작위 토큰을 포함한 임의 시퀀스 패턴을 문맥 속에서 완성할 수 있음을 보이고 로봇 궤적 등으로 확장 가능성을 제시.

## 재귀적 자기개선 · 자동화된 연구

### 00-19. Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements

- **식별자**: [arXiv:cs/0309048](https://arxiv.org/abs/cs/0309048)
- **연도 / 저자·기관**: 2003 / Schmidhuber
- **검증 상태**: ✅ 검증(V)
- **태그**: `Godel-machine`, `self-reference`, `theory`
- **요약**: 자기 코드를 포함해 스스로를 재작성하되, 그 재작성이 유익함을 증명할 수 있을 때만 수행하는 자기참조적 문제 해결기의 이론적 구상(arXiv 등록 제목 기준. 2007년 책 챕터 제목은 ‘Fully Self-Referential Optimal Universal Self-improvers’). 이후 Darwin Gödel Machine류 연구의 개념적 원형.

### 00-20. Large Language Models Can Self-Improve

- **식별자**: [arXiv:2210.11610](https://arxiv.org/abs/2210.11610)
- **연도 / 저자·기관**: 2022 / Huang et al. (Google, UIUC)
- **검증 상태**: ✅ 검증(V)
- **태그**: `self-improvement`, `self-consistency`, `unlabeled`
- **요약**: 레이블 없는 질문에 대해 자기 일관성으로 고신뢰 CoT 답을 만들고 이를 다시 미세조정한다. 540B 모델에서 GSM8K 74.4→82.1%를 보고.

### 00-21. Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement

- **식별자**: [arXiv:2410.04444](https://arxiv.org/abs/2410.04444)
- **연도 / 저자·기관**: 2024 / Yin et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Godel-agent`, `recursive-self-improvement`
- **요약**: 실행 중 자기 코드를 읽고 몽키 패칭으로 고쳐 쓰는 자기참조 에이전트. 코딩·과학·수학에서 수작업 에이전트를 능가하는 지속 개선을 보고(ACL 2025로 인용됨).

### 00-22. AlphaEvolve: A coding agent for scientific and algorithmic discovery

- **식별자**: [arXiv:2506.13131](https://arxiv.org/abs/2506.13131)
- **연도 / 저자·기관**: 2025 / Novikov et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AlphaEvolve`, `evolutionary-coding`, `algorithm-discovery`
- **요약**: LLM이 코드를 편집하고 평가기 피드백으로 반복 진화시키는 에이전트. 데이터센터 스케줄링 개선과 4×4 복소 행렬을 48회 스칼라 곱으로 곱하는 절차 발견(해당 설정에서 56년 만의 Strassen 개선) 등을 보고.

### 00-23. Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

- **식별자**: [arXiv:2409.04109](https://arxiv.org/abs/2409.04109)
- **연도 / 저자·기관**: 2024 / Si, Yang, Hashimoto (Stanford)
- **검증 상태**: ✅ 검증(V)
- **태그**: `research-ideation`, `human-study`
- **요약**: NLP 전문가 100명 이상의 맹검 평가에서 LLM 아이디어가 사람 아이디어보다 참신하다고 평가됐지만 실현가능성은 약간 낮았다. LLM 자기평가와 아이디어 다양성에는 한계(ICLR 2025). 후속 연구는 실행 후 점수 하락을 보고.

### 00-24. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops

- **식별자**: [arXiv:2607.07663](https://arxiv.org/abs/2607.07663)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `recursive-self-improvement`, `survey`
- **요약**: 재귀적 자기개선을 다룬 2026년 연구(ID·제목만 확인, 내용 미검토).

### 00-25. Self-Improvements in Modern Agentic Systems: A Survey

- **식별자**: [arXiv:2607.13104](https://arxiv.org/abs/2607.13104)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `self-improvement`, `survey`
- **요약**: 현대 에이전트 시스템의 자기개선을 정리한 2026년 서베이(ID·제목만 확인).

## 인지구조 접근 · 월드 모델 중심 설계

### 00-26. Cognitive Architectures for Language Agents

- **식별자**: [arXiv:2309.02427](https://arxiv.org/abs/2309.02427)
- **연도 / 저자·기관**: 2023 / Sumers, Yao, Narasimhan, Griffiths
- **검증 상태**: ✅ 검증(V)
- **태그**: `CoALA`, `cognitive-architecture`, `memory`
- **요약**: 언어 에이전트를 정보 저장(작업·장기 기억), 행동 공간(내부·외부), 의사결정 절차 세 축으로 분류하는 CoALA 프레임워크(TMLR). 내부 행동을 검색·추론·학습으로 나눈다.

### 00-27. A Path Towards Autonomous Machine Intelligence

- **식별자**: [링크](https://openreview.net/forum?id=BZ5a1r-kVsf)
- **연도 / 저자·기관**: 2022 / LeCun
- **검증 상태**: ✅ 검증(V)
- **태그**: `world-model`, `JEPA`, `position`
- **요약**: 세계 모델, 비용 모듈, 계획 모듈 등을 갖춘 자율 지능 구조와 JEPA를 제안한 입장 문서(arXiv 논문이 아닌 OpenReview 게재본).

## AGI 안전 · 정렬 · 위험 평가

### 00-28. Concrete Problems in AI Safety

- **식별자**: [arXiv:1606.06565](https://arxiv.org/abs/1606.06565)
- **연도 / 저자·기관**: 2016 / Amodei et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AI-safety`, `reward-hacking`
- **요약**: 부작용 회피, 보상 해킹, 확장 가능한 감독, 안전한 탐색, 분포 변화 등 실용적 안전 문제 다섯 가지를 정리한 고전.

### 00-29. AGI Safety Literature Review

- **식별자**: [arXiv:1805.01109](https://arxiv.org/abs/1805.01109)
- **연도 / 저자·기관**: 2018 / Everitt, Lea, Hutter
- **검증 상태**: ✅ 검증(V)
- **태그**: `AGI-safety`, `survey`
- **요약**: AGI의 안전 문제 목록, 안전한 AGI 설계 아이디어, 공공 정책, 도래 시기 예측을 정리한 서베이(IJCAI 2018).

### 00-30. AI safety via debate

- **식별자**: [arXiv:1805.00899](https://arxiv.org/abs/1805.00899)
- **연도 / 저자·기관**: 2018 / Irving, Christiano, Amodei
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `debate`, `scalable-oversight`
- **요약**: 두 AI가 토론하고 사람이 판정하는 방식으로 인간이 직접 평가하기 어려운 과제를 감독하는 방법 제안.

### 00-31. Scalable agent alignment via reward modeling: a research direction

- **식별자**: [arXiv:1811.07871](https://arxiv.org/abs/1811.07871)
- **연도 / 저자·기관**: 2018 / Leike et al. (DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `reward-modeling`, `alignment`
- **요약**: 사용자 의도를 보상 모델로 학습하는 방식으로 에이전트를 정렬하는 연구 방향을 제시.

### 00-32. Unsolved Problems in ML Safety

- **식별자**: [arXiv:2109.13916](https://arxiv.org/abs/2109.13916)
- **연도 / 저자·기관**: 2021 / Hendrycks, Carlini, Schulman, Steinhardt
- **검증 상태**: ✅ 검증(V)
- **태그**: `ML-safety`, `roadmap`
- **요약**: 견고성, 모니터링, 정렬, 시스템적 안전(Systemic Safety) 네 영역의 연구 로드맵.

### 00-33. The Alignment Problem from a Deep Learning Perspective

- **식별자**: [arXiv:2209.00626](https://arxiv.org/abs/2209.00626)
- **연도 / 저자·기관**: 2022 / Ngo, Chan, Mindermann
- **검증 상태**: ✅ 검증(V)
- **태그**: `alignment`, `deceptive-alignment`, `power-seeking`
- **요약**: 현재와 같은 방식으로 학습된 AGI가 보상을 위한 기만, 학습 분포를 벗어나 일반화되는 잘못된 내부 목표, 권력 추구 전략을 학습할 수 있고 정렬된 것처럼 보일 수 있다고 논증(ICLR 2024, 2025년 초 증거까지 반영한 개정판).

### 00-34. Scaling Laws for Reward Model Overoptimization

- **식별자**: [arXiv:2210.10760](https://arxiv.org/abs/2210.10760)
- **연도 / 저자·기관**: 2022 / Gao, Schulman, Hilton
- **검증 상태**: ✅ 검증(V)
- **태그**: `reward-hacking`, `RLHF`, `scaling-law`
- **요약**: 골드 보상 모델이 사람 평가자를 대신하는 합성 설정에서, 프록시 보상을 과도하게 최적화할 때 골드 점수의 변화가 최적화 방식(RL 대 best-of-n)에 따라 다른 함수 형태를 보이며 계수는 보상 모델 크기에 따라 매끄럽게 변한다고 보고.

### 00-35. Measuring Progress on Scalable Oversight for Large Language Models

- **식별자**: [arXiv:2211.03540](https://arxiv.org/abs/2211.03540)
- **연도 / 저자·기관**: 2022 / Bowman et al. (Anthropic)
- **검증 상태**: ✅ 검증(V)
- **태그**: `scalable-oversight`, `evaluation`
- **요약**: 인간 전문가를 능가하는 모델을 감독하는 문제를 실험적으로 다루기 위한 설정 제안과 초기 실험.

### 00-36. Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision

- **식별자**: [arXiv:2312.09390](https://arxiv.org/abs/2312.09390)
- **연도 / 저자·기관**: 2023 / Burns et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `superalignment`, `weak-to-strong`
- **요약**: 약한 모델의 감독만으로 강한 모델의 능력을 어디까지 끌어낼 수 있는지 실험(예: GPT-2급 감독으로 GPT-4급 모델 학습). 초인간 모델 정렬의 유비 실험.

### 00-37. Model evaluation for extreme risks

- **식별자**: [arXiv:2305.15324](https://arxiv.org/abs/2305.15324)
- **연도 / 저자·기관**: 2023 / Shevlane et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `dangerous-capabilities`, `evaluation`
- **요약**: 위험 능력 평가(dangerous capability evaluations)와 해로운 쪽으로 쓰려는 성향 평가(alignment evaluations)를 극단적 위험 대응의 핵심으로 제안.

### 00-38. Evaluating Frontier Models for Dangerous Capabilities

- **식별자**: [arXiv:2403.13793](https://arxiv.org/abs/2403.13793)
- **연도 / 저자·기관**: 2024 / Phuong et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `dangerous-capabilities`, `Gemini`
- **요약**: 설득·기만, 사이버보안, 자기 증식, 자기 추론 4개 영역의 위험 능력 평가를 Gemini 1.0에 적용. 강한 위험 능력은 없으나 초기 경고 신호가 있고 설득·기만이 가장 성숙했다고 보고.

### 00-39. Sabotage Evaluations for Frontier Models

- **식별자**: [arXiv:2410.21514](https://arxiv.org/abs/2410.21514)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `sabotage`, `evaluation`
- **요약**: 프런티어 모델의 사보타주 능력 평가를 다룬 2024년 연구(ID·제목만 확인).

### 00-40. Evaluating Frontier Models for Stealth and Situational Awareness

- **식별자**: [arXiv:2505.01420](https://arxiv.org/abs/2505.01420)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `stealth`, `situational-awareness`
- **요약**: 은밀성과 상황 인식 능력을 평가한 2025년 연구(ID·제목만 확인).

### 00-41. Tell me about yourself: LLMs are aware of their learned behaviors

- **식별자**: [arXiv:2501.11120](https://arxiv.org/abs/2501.11120)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `self-awareness`, `introspection`
- **요약**: LLM이 자신이 학습한 행동을 인식하는지 시험한 2025년 연구(ID·제목만 확인).

### 00-42. An Overview of Catastrophic AI Risks

- **식별자**: [arXiv:2306.12001](https://arxiv.org/abs/2306.12001)
- **연도 / 저자·기관**: 2023 / Hendrycks, Mazeika, Woodside (CAIS)
- **검증 상태**: ✅ 검증(V)
- **태그**: `catastrophic-risk`, `overview`
- **요약**: 파국적 위험을 악의적 사용, AI 경쟁 구도, 조직적 위험, 통제 불능(rogue) AI 네 범주로 정리한 개관.

### 00-43. Natural Selection Favors AIs over Humans

- **식별자**: [arXiv:2303.16200](https://arxiv.org/abs/2303.16200)
- **연도 / 저자·기관**: 2023 / Hendrycks
- **검증 상태**: ✅ 검증(V)
- **태그**: `evolutionary-pressure`, `risk`
- **요약**: 경쟁 압력이 AI에 이기적 특성을 선택할 수 있다는 논증을 제시한 입장 논문.

### 00-44. Managing extreme AI risks amid rapid progress

- **식별자**: [arXiv:2310.17688](https://arxiv.org/abs/2310.17688)
- **연도 / 저자·기관**: 2023 / Bengio et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `governance`, `extreme-risk`
- **요약**: 극단적 AI 위험을 서술하고 기술 연구와 적응형 거버넌스를 병행하는 계획을 제안한 합의 논문(Science 2024).

### 00-45. Frontier AI Regulation: Managing Emerging Risks to Public Safety

- **식별자**: [arXiv:2307.03718](https://arxiv.org/abs/2307.03718)
- **연도 / 저자·기관**: 2023 / Anderljung et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `regulation`, `frontier-AI`
- **요약**: 프런티어 AI의 표준 설정, 등록·보고, 규정 준수 보장 등 규제 틀 제안.

### 00-46. An Approach to Technical AGI Safety and Security

- **식별자**: [arXiv:2504.01849](https://arxiv.org/abs/2504.01849)
- **연도 / 저자·기관**: 2025 / Shah et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AGI-safety`, `misuse`, `misalignment`
- **요약**: 위험을 오용, 오정렬, 실수, 구조적 위험으로 나누고 오용·오정렬 대응에 집중. 모델 수준(증폭된 감독, 견고한 훈련)과 시스템 수준(모니터링, 접근 제어) 이중 방어를 제시하는 연구 의제.

### 00-47. Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety

- **식별자**: [arXiv:2507.11473](https://arxiv.org/abs/2507.11473)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `CoT-monitoring`, `safety`
- **요약**: 사고 사슬 모니터링이 안전에 주는 기회와 그 취약성을 다룬 2025년 글(ID·제목만 확인).

### 00-48. Distributional AGI Safety

- **식별자**: [arXiv:2512.16856](https://arxiv.org/abs/2512.16856)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `AGI-safety`
- **요약**: 분포적 관점의 AGI 안전을 다룬 2025년 연구(ID·제목만 확인).

### 00-49. The Singapore Consensus on Global AI Safety Research Priorities

- **식별자**: [arXiv:2506.20702](https://arxiv.org/abs/2506.20702)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `safety-research-priorities`, `consensus`
- **요약**: 국제 AI 안전 연구 우선순위에 대한 합의 문서(ID·제목만 확인).

### 00-50. The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment

- **식별자**: [arXiv:2412.16468](https://arxiv.org/abs/2412.16468)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `superalignment`, `survey`
- **요약**: 초정렬(superalignment)을 종합한 서베이(ID·제목만 확인).

### 00-51. Why do Experts Disagree on Existential Risk and P(doom)? A Survey of AI Experts

- **식별자**: [arXiv:2502.14870](https://arxiv.org/abs/2502.14870)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `existential-risk`, `expert-survey`
- **요약**: 전문가 간 실존적 위험 판단 차이의 원인을 조사한 연구(ID·제목만 확인).

### 00-52. The AI risk repository: A meta-review, database, and taxonomy of risks from artificial intelligence

- **식별자**: [arXiv:2408.12622](https://arxiv.org/abs/2408.12622)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `risk-taxonomy`
- **요약**: AI 위험에 대한 메타리뷰·데이터베이스·분류 체계(ID·제목만 확인).

## 기계 의식 · 도덕적 지위

### 00-53. Consciousness in Artificial Intelligence: Insights from the Science of Consciousness

- **식별자**: [arXiv:2308.08708](https://arxiv.org/abs/2308.08708)
- **연도 / 저자·기관**: 2023 / Butlin, Long et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `machine-consciousness`, `indicator-properties`
- **요약**: 순환 처리, 전역 작업공간, 고차 이론, 예측 처리, 주의 도식 이론 등에서 계산적 ‘지표 속성’을 도출해 AI를 평가. 현재 AI는 의식이 없다고 결론짓되, 지표를 충족하는 시스템을 만들 명백한 기술적 장벽은 없다고 봄.

### 00-54. Principles for Responsible AI Consciousness Research

- **식별자**: [arXiv:2501.07290](https://arxiv.org/abs/2501.07290)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `machine-consciousness`, `ethics`
- **요약**: AI 의식 연구의 책임 있는 수행 원칙을 다룬 2025년 글(ID·제목만 확인).
