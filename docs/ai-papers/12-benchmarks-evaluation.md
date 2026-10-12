# 12. 벤치마크 · 평가 방법론

모델 능력을 측정하는 주요 벤치마크와 평가 방법. 에이전트 평가(SWE-bench, OSWorld, τ-bench 등)는 08번, ARC 계열은 00·06번, AGI 위험 능력 평가는 00번 문서에 수록.

> 수록 16편 · 검증(V) 2편 · 기억기반(M) 14편

## 목차

- **지식 · 추론 · 수학 벤치마크** (11편)
  - 1. Measuring Massive Multitask Language Understanding (2020)
  - 2. Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (2022)
  - 3. Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (2022)
  - 4. Holistic Evaluation of Language Models (2022)
  - 5. TruthfulQA: Measuring How Models Mimic Human Falsehoods (2021)
  - 6. Measuring Mathematical Problem Solving With the MATH Dataset (2021)
  - 7. GPQA: A Graduate-Level Google-Proof Q&A Benchmark (2023)
  - 8. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark (2024)
  - 9. MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI (2023)
  - 10. Humanity's Last Exam (2025)
  - 11. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI (2024)
- **지시 수행 · 사실성 · 코드 · 인간 선호 평가** (5편)
  - 12. Instruction-Following Evaluation for Large Language Models (2023)
  - 13. Measuring short-form factuality in large language models (2024)
  - 14. LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (2024)
  - 15. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (2023)
  - 16. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference (2024)

## 지식 · 추론 · 수학 벤치마크

### 12-01. Measuring Massive Multitask Language Understanding

- **식별자**: [arXiv:2009.03300](https://arxiv.org/abs/2009.03300)
- **연도 / 저자·기관**: 2020 / Hendrycks et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MMLU`, `knowledge`
- **요약**: 57개 학문 분야 객관식 문제로 구성된 지식·문제해결 평가.

### 12-02. Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models

- **식별자**: [arXiv:2206.04615](https://arxiv.org/abs/2206.04615)
- **연도 / 저자·기관**: 2022 / BIG-bench authors
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BIG-bench`, `diverse-tasks`
- **요약**: 협업으로 구성한 200여 개의 다양한 과제 모음.

### 12-03. Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them

- **식별자**: [arXiv:2210.09261](https://arxiv.org/abs/2210.09261)
- **연도 / 저자·기관**: 2022 / Suzgun et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BBH`, `CoT`
- **요약**: BIG-bench에서 당시 모델이 인간 평균에 못 미친 23개 과제(BBH)와 CoT의 효과 분석.

### 12-04. Holistic Evaluation of Language Models

- **식별자**: [arXiv:2211.09110](https://arxiv.org/abs/2211.09110)
- **연도 / 저자·기관**: 2022 / Liang et al. (Stanford CRFM)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `HELM`, `holistic-eval`
- **요약**: 정확도뿐 아니라 보정·견고성·공정성·효율 등 다지표로 모델을 비교하는 HELM.

### 12-05. TruthfulQA: Measuring How Models Mimic Human Falsehoods

- **식별자**: [arXiv:2109.07958](https://arxiv.org/abs/2109.07958)
- **연도 / 저자·기관**: 2021 / Lin et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `TruthfulQA`, `truthfulness`
- **요약**: 인간의 흔한 오해를 모방해 거짓을 말하는지 측정. 큰 모델일수록 덜 진실한 경향을 보고.

### 12-06. Measuring Mathematical Problem Solving With the MATH Dataset

- **식별자**: [arXiv:2103.03874](https://arxiv.org/abs/2103.03874)
- **연도 / 저자·기관**: 2021 / Hendrycks et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MATH`, `competition-math`
- **요약**: 경시대회 수준 수학 문제 12,500개로 구성된 MATH 데이터셋.

### 12-07. GPQA: A Graduate-Level Google-Proof Q&A Benchmark

- **식별자**: [arXiv:2311.12022](https://arxiv.org/abs/2311.12022)
- **연도 / 저자·기관**: 2023 / Rein et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GPQA`, `expert-level`
- **요약**: 전문가가 작성한 대학원 수준 과학 문제로, 웹 검색으로도 풀기 어렵게 설계.

### 12-08. MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark

- **식별자**: [arXiv:2406.01574](https://arxiv.org/abs/2406.01574)
- **연도 / 저자·기관**: 2024 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MMLU-Pro`
- **요약**: MMLU의 선택지를 늘리고 추론 비중을 높인 확장판.

### 12-09. MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI

- **식별자**: [arXiv:2311.16502](https://arxiv.org/abs/2311.16502)
- **연도 / 저자·기관**: 2023 / Yue et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MMMU`, `multimodal`
- **요약**: 대학 수준의 멀티모달 전문 지식·추론을 평가하는 벤치마크.

### 12-10. Humanity's Last Exam

- **식별자**: [arXiv:2501.14249](https://arxiv.org/abs/2501.14249)
- **연도 / 저자·기관**: 2025 / Phan et al. (CAIS, Scale AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `HLE`, `frontier-benchmark`
- **요약**: 인류 지식 최전선을 겨냥한 멀티모달 폐쇄형 학술 벤치마크. 초기 판은 3,000문항이었으나 개정판은 2,500문항으로 기술되며, 문제 오류에 대한 후속 검증 연구(HLE-Verified)가 있다.

### 12-11. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI

- **식별자**: [arXiv:2411.04872](https://arxiv.org/abs/2411.04872)
- **연도 / 저자·기관**: 2024 / Glazer et al. (Epoch AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `FrontierMath`, `research-math`
- **요약**: 수학자들이 새로 쓴 미공개 문제로 구성해 오염을 방지한 고난도 수학 벤치마크. 학부~연구 수준의 난이도 계층을 가진다.

## 지시 수행 · 사실성 · 코드 · 인간 선호 평가

### 12-12. Instruction-Following Evaluation for Large Language Models

- **식별자**: [arXiv:2311.07911](https://arxiv.org/abs/2311.07911)
- **연도 / 저자·기관**: 2023 / Zhou et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `IFEval`, `instruction-following`
- **요약**: 검증 가능한 지시(예: 단어 수 제한)로 지시 수행 능력을 자동 채점하는 IFEval.

### 12-13. Measuring short-form factuality in large language models

- **식별자**: [arXiv:2411.04368](https://arxiv.org/abs/2411.04368)
- **연도 / 저자·기관**: 2024 / Wei et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SimpleQA`, `factuality`
- **요약**: 정답이 하나로 명확한 짧은 사실 질문으로 환각·사실성을 평가하는 SimpleQA.

### 12-14. LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

- **식별자**: [arXiv:2403.07974](https://arxiv.org/abs/2403.07974)
- **연도 / 저자·기관**: 2024 / Jain et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LiveCodeBench`, `contamination-free`
- **요약**: 지속적으로 새 대회 문제를 수집해 학습 데이터 오염을 줄이는 코드 평가.

### 12-15. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

- **식별자**: [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)
- **연도 / 저자·기관**: 2023 / Zheng et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LLM-as-a-judge`, `MT-Bench`
- **요약**: 강한 LLM을 평가자로 쓸 때 인간 선호와 80% 이상 일치하며 위치·장황함 편향이 있음을 분석한 연구, MT-Bench 제안.

### 12-16. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference

- **식별자**: [arXiv:2403.04132](https://arxiv.org/abs/2403.04132)
- **연도 / 저자·기관**: 2024 / Chiang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Chatbot-Arena`, `Elo`, `human-preference`
- **요약**: 사용자들이 익명 모델 두 개를 비교 투표하는 크라우드소싱 평가 플랫폼과 순위 산정 방법.
