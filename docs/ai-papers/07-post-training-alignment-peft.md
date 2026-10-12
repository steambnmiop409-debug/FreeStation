# 07. 사후학습 · 정렬(Alignment) · 파라미터 효율 미세조정

사전학습된 모델을 지시 수행·선호 정렬·안전성 방향으로 다듬는 방법론과, 적은 파라미터만 학습하는 PEFT 기법.

> 수록 26편 · 검증(V) 4편 · 기억기반(M) 22편

## 목차

- **지시 튜닝과 데이터** (8편)
  - 1. Finetuned Language Models Are Zero-Shot Learners (2021)
  - 2. Multitask Prompted Training Enables Zero-Shot Task Generalization (2021)
  - 3. Scaling Instruction-Finetuned Language Models (2022)
  - 4. Self-Instruct: Aligning Language Models with Self-Generated Instructions (2022)
  - 5. WizardLM: Empowering Large Language Models to Follow Complex Instructions (2023)
  - 6. Orca: Progressive Learning from Complex Explanation Traces of GPT-4 (2023)
  - 7. LIMA: Less Is More for Alignment (2023)
  - 8. Tulu 3: Pushing Frontiers in Open Language Model Post-Training (2024)
- **선호 최적화 · RLHF · 헌법적 AI** (11편)
  - 9. Training language models to follow instructions with human feedback (2022)
  - 10. Constitutional AI: Harmlessness from AI Feedback (2022)
  - 11. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback (2023)
  - 12. Direct Preference Optimization: Your Language Model is Secretly a Reward Model (2023)
  - 13. A General Theoretical Paradigm to Understand Learning from Human Preferences (2023)
  - 14. KTO: Model Alignment as Prospect Theoretic Optimization (2024)
  - 15. ORPO: Monolithic Preference Optimization without Reference Model (2024)
  - 16. SimPO: Simple Preference Optimization with a Reference-Free Reward (2024)
  - 17. Self-Rewarding Language Models (2024)
  - 18. Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models (2024)
  - 19. Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback (2023)
- **파라미터 효율 미세조정(PEFT)** (7편)
  - 20. Parameter-Efficient Transfer Learning for NLP (2019)
  - 21. Prefix-Tuning: Optimizing Continuous Prompts for Generation (2021)
  - 22. The Power of Scale for Parameter-Efficient Prompt Tuning (2021)
  - 23. LoRA: Low-Rank Adaptation of Large Language Models (2021)
  - 24. Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning (2022)
  - 25. QLoRA: Efficient Finetuning of Quantized LLMs (2023)
  - 26. DoRA: Weight-Decomposed Low-Rank Adaptation (2024)

## 지시 튜닝과 데이터

### 07-01. Finetuned Language Models Are Zero-Shot Learners

- **식별자**: [arXiv:2109.01652](https://arxiv.org/abs/2109.01652)
- **연도 / 저자·기관**: 2021 / Wei et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FLAN`, `instruction-tuning`
- **요약**: 다양한 과제를 지시문 형태로 미세조정하면 미학습 과제에서의 제로샷 성능이 오른다는 FLAN.

### 07-02. Multitask Prompted Training Enables Zero-Shot Task Generalization

- **식별자**: [arXiv:2110.08207](https://arxiv.org/abs/2110.08207)
- **연도 / 저자·기관**: 2021 / Sanh et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `T0`, `multitask-prompts`
- **요약**: 여러 과제를 프롬프트 형식으로 다중 학습해 제로샷 일반화를 높인 T0.

### 07-03. Scaling Instruction-Finetuned Language Models

- **식별자**: [arXiv:2210.11416](https://arxiv.org/abs/2210.11416)
- **연도 / 저자·기관**: 2022 / Chung et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Flan-PaLM`, `CoT-data`
- **요약**: 지시 튜닝 과제 수·모델 크기를 늘리고 CoT 데이터를 포함하는 효과를 분석(Flan-PaLM/T5).

### 07-04. Self-Instruct: Aligning Language Models with Self-Generated Instructions

- **식별자**: [arXiv:2212.10560](https://arxiv.org/abs/2212.10560)
- **연도 / 저자·기관**: 2022 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Self-Instruct`, `synthetic-data`
- **요약**: 모델이 스스로 만든 지시·응답으로 지시 튜닝 데이터를 부트스트랩하는 방법.

### 07-05. WizardLM: Empowering Large Language Models to Follow Complex Instructions

- **식별자**: [arXiv:2304.12244](https://arxiv.org/abs/2304.12244)
- **연도 / 저자·기관**: 2023 / Xu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Evol-Instruct`
- **요약**: 지시문을 점진적으로 복잡하게 진화시켜 학습 데이터를 만드는 Evol-Instruct.

### 07-06. Orca: Progressive Learning from Complex Explanation Traces of GPT-4

- **식별자**: [arXiv:2306.02707](https://arxiv.org/abs/2306.02707)
- **연도 / 저자·기관**: 2023 / Mukherjee et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Orca`, `imitation`, `explanation-traces`
- **요약**: 강한 모델의 단계별 설명 흔적을 모방 학습해 작은 모델의 추론을 향상.

### 07-07. LIMA: Less Is More for Alignment

- **식별자**: [arXiv:2305.11206](https://arxiv.org/abs/2305.11206)
- **연도 / 저자·기관**: 2023 / Zhou et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LIMA`, `data-quality`
- **요약**: 단 1,000개의 정제된 예시만으로 정렬이 상당 부분 가능하다는 ‘표면적 정렬 가설’을 제시.

### 07-08. Tulu 3: Pushing Frontiers in Open Language Model Post-Training

- **식별자**: [arXiv:2411.15124](https://arxiv.org/abs/2411.15124)
- **연도 / 저자·기관**: 2024 / Lambert et al. (AI2)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Tulu-3`, `open-post-training`, `RLVR`
- **요약**: 공개 후처리 레시피(SFT·DPO·검증 가능한 보상 RL)와 데이터·평가·코드를 모두 공개해 개방형과 폐쇄형 사이 격차를 줄이려는 보고서. 부정적 결과도 공개.

## 선호 최적화 · RLHF · 헌법적 AI

### 07-09. Training language models to follow instructions with human feedback

- **식별자**: [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)
- **연도 / 저자·기관**: 2022 / Ouyang et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `InstructGPT`, `RLHF`
- **요약**: 지도 미세조정 후 인간 선호로 보상 모델을 만들어 PPO로 최적화한 InstructGPT. 1.3B 모델이 175B GPT-3보다 선호되었다.

### 07-10. Constitutional AI: Harmlessness from AI Feedback

- **식별자**: [arXiv:2212.08073](https://arxiv.org/abs/2212.08073)
- **연도 / 저자·기관**: 2022 / Bai et al. (Anthropic)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Constitutional-AI`, `RLAIF`
- **요약**: 사람이 쓴 원칙(헌법)을 바탕으로 AI가 스스로 비판·수정하고 선호를 생성해 무해성을 학습시키는 방법.

### 07-11. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback

- **식별자**: [arXiv:2309.00267](https://arxiv.org/abs/2309.00267)
- **연도 / 저자·기관**: 2023 / Lee et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RLAIF`
- **요약**: AI가 생성한 선호 라벨로 RLHF와 비슷한 결과를 내는지 검증한 연구.

### 07-12. Direct Preference Optimization: Your Language Model is Secretly a Reward Model

- **식별자**: [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)
- **연도 / 저자·기관**: 2023 / Rafailov et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DPO`, `preference-optimization`
- **요약**: 보상 모델·RL 루프 없이 선호 쌍에 대한 단순 분류형 손실로 정책을 직접 최적화하는 DPO.

### 07-13. A General Theoretical Paradigm to Understand Learning from Human Preferences

- **식별자**: [arXiv:2310.12036](https://arxiv.org/abs/2310.12036)
- **연도 / 저자·기관**: 2023 / Azar et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `IPO`, `theory`
- **요약**: RLHF·DPO를 통합하는 이론적 틀(ΨPO)과 과적합에 강한 IPO 제안.

### 07-14. KTO: Model Alignment as Prospect Theoretic Optimization

- **식별자**: [arXiv:2402.01306](https://arxiv.org/abs/2402.01306)
- **연도 / 저자·기관**: 2024 / Ethayarajh et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `KTO`, `prospect-theory`
- **요약**: 쌍 선호 대신 ‘좋음/나쁨’ 이진 신호만으로 전망 이론 기반 손실로 정렬.

### 07-15. ORPO: Monolithic Preference Optimization without Reference Model

- **식별자**: [arXiv:2403.07691](https://arxiv.org/abs/2403.07691)
- **연도 / 저자·기관**: 2024 / Hong et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ORPO`, `reference-free`
- **요약**: SFT 손실에 오즈비 항을 더해 기준 모델 없이 단일 단계로 선호 정렬.

### 07-16. SimPO: Simple Preference Optimization with a Reference-Free Reward

- **식별자**: [arXiv:2405.14734](https://arxiv.org/abs/2405.14734)
- **연도 / 저자·기관**: 2024 / Meng, Xia, Chen
- **검증 상태**: ✅ 검증(V)
- **태그**: `SimPO`, `reference-free`, `length-normalized`
- **요약**: 길이로 정규화한 평균 로그우도를 보상으로 써 기준 모델이 필요 없고, 목표 마진을 도입. AlpacaEval 2 등에서 DPO를 최대 6.4점 앞선다고 보고(NeurIPS 2024).

### 07-17. Self-Rewarding Language Models

- **식별자**: [arXiv:2401.10020](https://arxiv.org/abs/2401.10020)
- **연도 / 저자·기관**: 2024 / Yuan et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `self-rewarding`, `iterative-DPO`
- **요약**: 모델 자신이 LLM-as-a-judge로 보상을 만들어 반복 DPO로 자기 개선하는 방법.

### 07-18. Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models

- **식별자**: [arXiv:2401.01335](https://arxiv.org/abs/2401.01335)
- **연도 / 저자·기관**: 2024 / Chen et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SPIN`, `self-play`
- **요약**: 이전 버전 모델의 출력과 사람 데이터를 구분하도록 학습하는 자기 대국 미세조정.

### 07-19. Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback

- **식별자**: [arXiv:2307.15217](https://arxiv.org/abs/2307.15217)
- **연도 / 저자·기관**: 2023 / Casper et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLHF`, `limitations`, `survey`
- **요약**: RLHF의 보상 모델링·정책 최적화·피드백 수집 단계의 미해결 문제와 근본적 한계를 정리한 서베이.

## 파라미터 효율 미세조정(PEFT)

### 07-20. Parameter-Efficient Transfer Learning for NLP

- **식별자**: [arXiv:1902.00751](https://arxiv.org/abs/1902.00751)
- **연도 / 저자·기관**: 2019 / Houlsby et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `adapters`, `PEFT`
- **요약**: 사전학습 모델에 작은 어댑터 모듈만 추가해 학습하는 방법.

### 07-21. Prefix-Tuning: Optimizing Continuous Prompts for Generation

- **식별자**: [arXiv:2101.00190](https://arxiv.org/abs/2101.00190)
- **연도 / 저자·기관**: 2021 / Li & Liang
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `prefix-tuning`, `continuous-prompt`
- **요약**: 각 층에 학습 가능한 접두 벡터를 붙이는 방법.

### 07-22. The Power of Scale for Parameter-Efficient Prompt Tuning

- **식별자**: [arXiv:2104.08691](https://arxiv.org/abs/2104.08691)
- **연도 / 저자·기관**: 2021 / Lester et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `prompt-tuning`
- **요약**: 입력에 소프트 프롬프트만 학습하며, 모델이 커질수록 전체 미세조정과 격차가 줄어듦을 보임.

### 07-23. LoRA: Low-Rank Adaptation of Large Language Models

- **식별자**: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- **연도 / 저자·기관**: 2021 / Hu et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LoRA`, `low-rank`, `PEFT`
- **요약**: 사전학습 가중치를 고정하고 저랭크 행렬 갱신만 학습. 학습 파라미터와 메모리를 크게 줄이고 추론 지연이 없다.

### 07-24. Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning

- **식별자**: [arXiv:2205.05638](https://arxiv.org/abs/2205.05638)
- **연도 / 저자·기관**: 2022 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `IA3`, `T-Few`
- **요약**: 활성화를 학습된 벡터로 스케일링하는 (IA)³와 T-Few 레시피.

### 07-25. QLoRA: Efficient Finetuning of Quantized LLMs

- **식별자**: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- **연도 / 저자·기관**: 2023 / Dettmers et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `QLoRA`, `4-bit`, `NF4`
- **요약**: 4비트로 양자화한 기반 모델 위에 LoRA를 학습해 단일 GPU에서 대형 모델 미세조정을 가능하게 함.

### 07-26. DoRA: Weight-Decomposed Low-Rank Adaptation

- **식별자**: [arXiv:2402.09353](https://arxiv.org/abs/2402.09353)
- **연도 / 저자·기관**: 2024 / Liu et al. (NVIDIA)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DoRA`, `weight-decomposition`
- **요약**: 가중치를 크기와 방향으로 분해해 LoRA의 학습 능력 격차를 줄인 방법.
