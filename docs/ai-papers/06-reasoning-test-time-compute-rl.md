# 06. 추론(Reasoning) · 테스트 시점 연산 · 강화학습

사고 사슬(CoT)에서 시작해 검증 가능한 보상 기반 강화학습(RLVR), 추론 시 연산 확장, 자기 개선·자기 대국으로 이어지는 추론 모델 연구 흐름.

> 수록 32편 · 검증(V) 14편 · 기억기반(M) 18편

## 목차

- **프롬프팅 기반 추론** (10편)
  - 1. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (2022)
  - 2. Large Language Models are Zero-Shot Reasoners (2022)
  - 3. Self-Consistency Improves Chain of Thought Reasoning in Language Models (2022)
  - 4. Least-to-Most Prompting Enables Complex Reasoning in Large Language Models (2022)
  - 5. Tree of Thoughts: Deliberate Problem Solving with Large Language Models (2023)
  - 6. Graph of Thoughts: Solving Elaborate Problems with Large Language Models (2023)
  - 7. Chain of Draft: Thinking Faster by Writing Less (2025)
  - 8. Large Language Models Cannot Self-Correct Reasoning Yet (2023)
  - 9. Self-Refine: Iterative Refinement with Self-Feedback (2023)
  - 10. Reflexion: Language Agents with Verbal Reinforcement Learning (2023)
- **검증기·프로세스 보상** (6편)
  - 11. Training Verifiers to Solve Math Word Problems (2021)
  - 12. Solving math word problems with process- and outcome-based feedback (2022)
  - 13. Let's Verify Step by Step (2023)
  - 14. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (2023)
  - 15. STaR: Bootstrapping Reasoning With Reasoning (2022)
  - 16. Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking (2024)
- **테스트 시점 연산 확장** (5편)
  - 17. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (2024)
  - 18. s1: Simple test-time scaling (2025)
  - 19. ARC Prize 2024: Technical Report (2024)
  - 20. ARC Prize 2025: Technical Report (2026)
  - 21. TTRL: Test-Time Reinforcement Learning (2025)
- **강화학습 기반 추론 모델** (11편)
  - 22. Proximal Policy Optimization Algorithms (2017)
  - 23. Deep Reinforcement Learning from Human Preferences (2017)
  - 24. Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs (2024)
  - 25. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (2024)
  - 26. DAPO: An Open-Source LLM Reinforcement Learning System at Scale (2025)
  - 27. Understanding R1-Zero-Like Training: A Critical Perspective (2025)
  - 28. SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild (2025)
  - 29. Absolute Zero: Reinforced Self-play Reasoning with Zero Data (2025)
  - 30. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning (2025)
  - 31. Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (2017)
  - 32. Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (2019)

## 프롬프팅 기반 추론

### 06-01. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- **식별자**: [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **연도 / 저자·기관**: 2022 / Wei et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CoT`, `prompting`
- **요약**: 중간 추론 단계를 예시로 보여주면 충분히 큰 모델의 산술·상식·기호 추론 성능이 크게 오른다는 사고 사슬 논문.

### 06-02. Large Language Models are Zero-Shot Reasoners

- **식별자**: [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)
- **연도 / 저자·기관**: 2022 / Kojima et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `zero-shot-CoT`
- **요약**: ‘단계별로 생각해 보자’ 한 문장만으로 예시 없이도 추론이 개선됨을 보인 연구.

### 06-03. Self-Consistency Improves Chain of Thought Reasoning in Language Models

- **식별자**: [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- **연도 / 저자·기관**: 2022 / Wang et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `self-consistency`, `sampling`
- **요약**: 여러 추론 경로를 샘플링해 다수결로 답을 고르는 방법.

### 06-04. Least-to-Most Prompting Enables Complex Reasoning in Large Language Models

- **식별자**: [arXiv:2205.10625](https://arxiv.org/abs/2205.10625)
- **연도 / 저자·기관**: 2022 / Zhou et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `least-to-most`, `decomposition`
- **요약**: 문제를 하위 문제로 분해해 순차 해결하는 프롬프팅.

### 06-05. Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- **식별자**: [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- **연도 / 저자·기관**: 2023 / Yao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ToT`, `search`
- **요약**: 추론을 트리로 탐색하고 평가·백트래킹하는 프레임워크.

### 06-06. Graph of Thoughts: Solving Elaborate Problems with Large Language Models

- **식별자**: [arXiv:2308.09687](https://arxiv.org/abs/2308.09687)
- **연도 / 저자·기관**: 2023 / Besta et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GoT`, `graph-reasoning`
- **요약**: 생각을 그래프로 표현해 결합·정제 연산을 허용하는 확장.

### 06-07. Chain of Draft: Thinking Faster by Writing Less

- **식별자**: [arXiv:2502.18600](https://arxiv.org/abs/2502.18600)
- **연도 / 저자·기관**: 2025 / Xu et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Chain-of-Draft`, `token-efficiency`
- **요약**: 각 추론 단계를 짧게(약 5단어 이내) 쓰도록 유도하는 프롬프팅. CoT와 비슷하거나 더 높은 정확도를 최소 7.6%의 토큰으로 달성한다고 보고(후속 연구는 어려운 과제에서 성능 저하를 지적).

### 06-08. Large Language Models Cannot Self-Correct Reasoning Yet

- **식별자**: [arXiv:2310.01798](https://arxiv.org/abs/2310.01798)
- **연도 / 저자·기관**: 2023 / Huang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `self-correction`, `limitations`
- **요약**: 외부 피드백 없는 내재적 자기 교정은 추론 성능을 개선하지 못하거나 오히려 해칠 수 있음을 보인 비판적 연구.

### 06-09. Self-Refine: Iterative Refinement with Self-Feedback

- **식별자**: [arXiv:2303.17651](https://arxiv.org/abs/2303.17651)
- **연도 / 저자·기관**: 2023 / Madaan et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `self-refine`
- **요약**: 모델이 스스로 피드백을 생성하고 반복 개선하는 방법.

### 06-10. Reflexion: Language Agents with Verbal Reinforcement Learning

- **식별자**: [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- **연도 / 저자·기관**: 2023 / Shinn et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Reflexion`, `verbal-RL`
- **요약**: 과거 실패에 대한 언어적 반성을 메모리에 쌓아 다음 시도를 개선하는 에이전트.

## 검증기·프로세스 보상

### 06-11. Training Verifiers to Solve Math Word Problems

- **식별자**: [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)
- **연도 / 저자·기관**: 2021 / Cobbe et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GSM8K`, `verifier`
- **요약**: GSM8K 데이터셋과, 여러 후보 풀이를 학습된 검증기로 순위화하는 방법.

### 06-12. Solving math word problems with process- and outcome-based feedback

- **식별자**: [arXiv:2211.14275](https://arxiv.org/abs/2211.14275)
- **연도 / 저자·기관**: 2022 / Uesato et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `process-supervision`
- **요약**: 최종 답만 보는 결과 감독과 단계별 과정 감독을 비교한 연구.

### 06-13. Let's Verify Step by Step

- **식별자**: [arXiv:2305.20050](https://arxiv.org/abs/2305.20050)
- **연도 / 저자·기관**: 2023 / Lightman et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `PRM800K`, `process-reward-model`
- **요약**: 단계별 인간 라벨로 학습한 과정 보상 모델이 결과 보상 모델보다 수학 풀이 선별에 낫다는 결과와 PRM800K 데이터.

### 06-14. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

- **식별자**: [arXiv:2312.08935](https://arxiv.org/abs/2312.08935)
- **연도 / 저자·기관**: 2023 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Math-Shepherd`, `automatic-PRM`
- **요약**: 사람 라벨 없이 몬테카를로 롤아웃으로 단계 보상을 자동 생성.

### 06-15. STaR: Bootstrapping Reasoning With Reasoning

- **식별자**: [arXiv:2203.14465](https://arxiv.org/abs/2203.14465)
- **연도 / 저자·기관**: 2022 / Zelikman et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `STaR`, `self-training`
- **요약**: 정답에 이른 자기 생성 추론 과정만 골라 재학습하며 추론 능력을 부트스트랩.

### 06-16. Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking

- **식별자**: [arXiv:2403.09629](https://arxiv.org/abs/2403.09629)
- **연도 / 저자·기관**: 2024 / Zelikman et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Quiet-STaR`, `implicit-reasoning`
- **요약**: 매 토큰마다 내부 사고(rationale)를 생성해 미래 텍스트 예측을 돕도록 학습. 지속 사전학습 후 제로샷으로 GSM8K 5.9→10.9%, CommonsenseQA 36.3→47.2%를 보고.

## 테스트 시점 연산 확장

### 06-17. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

- **식별자**: [arXiv:2408.03314](https://arxiv.org/abs/2408.03314)
- **연도 / 저자·기관**: 2024 / Snell et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `test-time-compute`, `compute-optimal`
- **요약**: 검증기 탐색과 출력 분포 적응 두 방식을 분석하고 문제 난이도에 따라 추론 연산을 배분하는 ‘연산 최적’ 전략이 best-of-N 대비 4배 이상 효율적이라고 보고.

### 06-18. s1: Simple test-time scaling

- **식별자**: [arXiv:2501.19393](https://arxiv.org/abs/2501.19393)
- **연도 / 저자·기관**: 2025 / Muennighoff et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `s1`, `budget-forcing`, `s1K`
- **요약**: 1,000개 문제(s1K)로 Qwen2.5-32B-Instruct를 미세조정하고 ‘Wait’ 삽입/종료 강제(budget forcing)로 사고 길이를 조절. AIME24 정확도 50→57%로 확장되며 o1-preview를 최대 27% 앞선다고 보고.

### 06-19. ARC Prize 2024: Technical Report

- **식별자**: [arXiv:2412.04604](https://arxiv.org/abs/2412.04604)
- **연도 / 저자·기관**: 2024 / Chollet et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `ARC-AGI`, `program-synthesis`, `test-time-training`
- **요약**: ARC-AGI 비공개 평가 최고 점수가 33%→55.5%로 상승. 딥러닝 유도 프로그램 합성과 테스트 시점 학습이 핵심 기법이었다.

### 06-20. ARC Prize 2025: Technical Report

- **식별자**: [arXiv:2601.10904](https://arxiv.org/abs/2601.10904)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `ARC-AGI`, `technical-report`
- **요약**: ARC Prize 2025 대회 기술 보고서(ID·제목만 확인).

### 06-21. TTRL: Test-Time Reinforcement Learning

- **식별자**: [arXiv:2504.16084](https://arxiv.org/abs/2504.16084)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `test-time-RL`
- **요약**: 정답 레이블 없이 테스트 시점에서 강화학습을 하는 접근(ID·제목만 확인).

## 강화학습 기반 추론 모델

### 06-22. Proximal Policy Optimization Algorithms

- **식별자**: [arXiv:1707.06347](https://arxiv.org/abs/1707.06347)
- **연도 / 저자·기관**: 2017 / Schulman et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `PPO`
- **요약**: 클리핑된 목적함수를 쓰는 정책 경사 알고리즘. RLHF의 표준 기반 알고리즘.

### 06-23. Deep Reinforcement Learning from Human Preferences

- **식별자**: [arXiv:1706.03741](https://arxiv.org/abs/1706.03741)
- **연도 / 저자·기관**: 2017 / Christiano et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RLHF`, `reward-model`
- **요약**: 인간의 쌍별 선호로 보상 모델을 학습해 RL에 쓰는 RLHF의 원형.

### 06-24. Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs

- **식별자**: [arXiv:2402.14740](https://arxiv.org/abs/2402.14740)
- **연도 / 저자·기관**: 2024 / Ahmadian et al. (Cohere)
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLOO`, `REINFORCE`
- **요약**: PPO의 복잡한 구성요소 없이 REINFORCE 계열(RLOO)이 더 단순하고 효과적일 수 있음을 보인 연구.

### 06-25. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- **식별자**: [arXiv:2402.03300](https://arxiv.org/abs/2402.03300)
- **연도 / 저자·기관**: 2024 / Shao et al. (DeepSeek)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GRPO`, `math`
- **요약**: 가치 함수 없이 그룹 상대 보상으로 정책을 갱신하는 GRPO를 제안하고 수학 특화 사전학습 데이터를 구축.

### 06-26. DAPO: An Open-Source LLM Reinforcement Learning System at Scale

- **식별자**: [arXiv:2503.14476](https://arxiv.org/abs/2503.14476)
- **연도 / 저자·기관**: 2025 / Yu et al. (ByteDance)
- **검증 상태**: ✅ 검증(V)
- **태그**: `DAPO`, `RLVR`, `GRPO-variant`
- **요약**: Decoupled Clip과 Dynamic Sampling 등 4가지 기법으로 Qwen2.5-32B 기반 AIME 2024 50점 달성. 소박한 GRPO는 30점에 그쳤고 원인은 엔트로피 붕괴·보상 잡음·불안정이라고 분석.

### 06-27. Understanding R1-Zero-Like Training: A Critical Perspective

- **식별자**: [arXiv:2503.20783](https://arxiv.org/abs/2503.20783)
- **연도 / 저자·기관**: 2025 / Liu et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Dr-GRPO`, `R1-Zero`
- **요약**: R1-Zero식 학습을 기반 모델과 RL 두 측면에서 분석. GRPO의 길이 편향(오답 응답이 길어짐)을 지적하고 Dr. GRPO를 제안, 최소 레시피로 AIME 2024 43.3%를 보고.

### 06-28. SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild

- **식별자**: [arXiv:2503.18892](https://arxiv.org/abs/2503.18892)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `zero-RL`, `base-models`
- **요약**: 다양한 기반 모델에서 ‘zero RL’ 학습을 조사한 연구(ID·제목만 확인).

### 06-29. Absolute Zero: Reinforced Self-play Reasoning with Zero Data

- **식별자**: [arXiv:2505.03335](https://arxiv.org/abs/2505.03335)
- **연도 / 저자·기관**: 2025 / Zhao et al. (Tsinghua)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Absolute-Zero`, `self-play`, `code-executor`
- **요약**: 하나의 모델이 스스로 과제를 제안하고 풀며 외부 데이터 없이 학습하는 패러다임. 코드 실행기로 검증 가능한 피드백을 얻는 AZR이 코딩·수학에서 ‘zero’ 모델들을 앞선다고 보고.

### 06-30. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning

- **식별자**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `self-play`, `zero-sum-games`
- **요약**: 제로섬 게임 자기 대국으로 추론을 유도하는 연구(ID·제목만 확인).

### 06-31. Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm

- **식별자**: [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
- **연도 / 저자·기관**: 2017 / Silver et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AlphaZero`, `self-play`
- **요약**: 바둑·체스·쇼기를 규칙만으로 자기 대국 학습하는 AlphaZero의 범용 알고리즘.

### 06-32. Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

- **식별자**: [arXiv:1911.08265](https://arxiv.org/abs/1911.08265)
- **연도 / 저자·기관**: 2019 / Schrittwieser et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MuZero`, `model-based-RL`
- **요약**: 환경 규칙 없이 학습된 모델로 계획하는 MuZero.
