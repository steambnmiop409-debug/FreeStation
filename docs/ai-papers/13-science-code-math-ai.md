# 13. 과학 · 코드 · 수학을 위한 AI

기상·의학·단백질·재료 같은 과학 분야 파운데이션 모델, 코드 생성 모델, 수학·정리 증명 모델. 자동 과학 에이전트(AI Scientist, AlphaEvolve)는 08·00번 문서 참조.

> 수록 21편 · 검증(V) 11편 · 기억기반(M) 10편

## 목차

- **기상·지구과학** (4편)
  - 1. GraphCast: Learning skillful medium-range global weather forecasting (2022)
  - 2. Pangu-Weather: A 3D High-Resolution Model for Fast and Accurate Global Weather Forecast (2022)
  - 3. GenCast: Diffusion-based ensemble forecasting for medium-range weather (2023)
  - 4. Aurora: A Foundation Model of the Atmosphere (2024)
- **의학 · 과학 언어모델** (6편)
  - 5. Galactica: A Large Language Model for Science (2022)
  - 6. Large Language Models Encode Clinical Knowledge (2022)
  - 7. Towards Expert-Level Medical Question Answering with Large Language Models (2023)
  - 8. Highly accurate protein structure prediction with AlphaFold (2021)
  - 9. Accurate structure prediction of biomolecular interactions with AlphaFold 3 (2024)
  - 10. Scaling deep learning for materials discovery (2023)
- **코드 생성 모델** (5편)
  - 11. Evaluating Large Language Models Trained on Code (2021)
  - 12. Competition-Level Code Generation with AlphaCode (2022)
  - 13. StarCoder: may the source be with you! (2023)
  - 14. Code Llama: Open Foundation Models for Code (2023)
  - 15. Qwen2.5-Coder Technical Report (2024)
- **수학 · 정리 증명** (6편)
  - 16. Solving Quantitative Reasoning Problems with Language Models (2022)
  - 17. Llemma: An Open Language Model For Mathematics (2023)
  - 18. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement (2024)
  - 19. DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition (2025)
  - 20. Mathematical discoveries from program search with large language models (2023)
  - 21. Solving olympiad geometry without human demonstrations (2024)

## 기상·지구과학

### 13-01. GraphCast: Learning skillful medium-range global weather forecasting

- **식별자**: [arXiv:2212.12794](https://arxiv.org/abs/2212.12794)
- **연도 / 저자·기관**: 2022 / Lam et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GraphCast`, `weather`, `GNN`
- **요약**: 그래프 신경망으로 전 지구 중기 일기예보를 수 분 안에 생성하는 모델.

### 13-02. Pangu-Weather: A 3D High-Resolution Model for Fast and Accurate Global Weather Forecast

- **식별자**: [arXiv:2211.02556](https://arxiv.org/abs/2211.02556)
- **연도 / 저자·기관**: 2022 / Bi et al. (Huawei)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Pangu-Weather`, `3D-transformer`
- **요약**: 3차원 Transformer 기반 전 지구 기상 예측 모델.

### 13-03. GenCast: Diffusion-based ensemble forecasting for medium-range weather

- **식별자**: [arXiv:2312.15796](https://arxiv.org/abs/2312.15796)
- **연도 / 저자·기관**: 2023 / Price et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GenCast`, `diffusion`, `ensemble`
- **요약**: 확산 모델로 앙상블 기상 예측을 생성하는 GenCast.

### 13-04. Aurora: A Foundation Model of the Atmosphere

- **식별자**: [arXiv:2405.13063](https://arxiv.org/abs/2405.13063)
- **연도 / 저자·기관**: 2024 / Bodnar et al. (Microsoft)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Aurora`, `foundation-model`, `weather`
- **요약**: 100만 시간 이상의 다양한 기상·기후 데이터로 학습한 13억 파라미터 대기 파운데이션 모델(3D Swin Transformer + Perceiver 인코더·디코더). 5일 대기오염과 10일 고해상도 기상 예측을 1분 이내에 수행한다고 보고.

## 의학 · 과학 언어모델

### 13-05. Galactica: A Large Language Model for Science

- **식별자**: [arXiv:2211.09085](https://arxiv.org/abs/2211.09085)
- **연도 / 저자·기관**: 2022 / Taylor et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Galactica`, `scientific-LLM`
- **요약**: 과학 문헌·수식·단백질 서열로 학습한 과학용 LLM. 공개 직후 환각 문제로 데모가 중단된 사례로도 알려짐.

### 13-06. Large Language Models Encode Clinical Knowledge

- **식별자**: [arXiv:2212.13138](https://arxiv.org/abs/2212.13138)
- **연도 / 저자·기관**: 2022 / Singhal et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Med-PaLM`, `medical-QA`
- **요약**: 의학 질의응답 벤치마크(MultiMedQA)와 지시 프롬프트 튜닝을 거친 Med-PaLM 보고.

### 13-07. Towards Expert-Level Medical Question Answering with Large Language Models

- **식별자**: [arXiv:2305.09617](https://arxiv.org/abs/2305.09617)
- **연도 / 저자·기관**: 2023 / Singhal et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Med-PaLM-2`
- **요약**: 미국 의사면허시험(USMLE)식 문제에서 전문가 수준 성능을 주장한 Med-PaLM 2.

### 13-08. Highly accurate protein structure prediction with AlphaFold

- **식별자**: [링크](https://doi.org/10.1038/s41586-021-03819-2)
- **연도 / 저자·기관**: 2021 / Jumper et al. (DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AlphaFold2`, `protein-structure`
- **요약**: 아미노산 서열에서 단백질 3차원 구조를 높은 정확도로 예측한 AlphaFold 2(Nature, arXiv 논문 아님).

### 13-09. Accurate structure prediction of biomolecular interactions with AlphaFold 3

- **식별자**: [링크](https://doi.org/10.1038/s41586-024-07487-w)
- **연도 / 저자·기관**: 2024 / Abramson et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AlphaFold3`, `biomolecules`
- **요약**: 단백질뿐 아니라 핵산·리간드 등 생체분자 복합체의 구조를 예측(Nature, arXiv 논문 아님).

### 13-10. Scaling deep learning for materials discovery

- **식별자**: [링크](https://doi.org/10.1038/s41586-023-06735-9)
- **연도 / 저자·기관**: 2023 / Merchant et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GNoME`, `materials`
- **요약**: 그래프 네트워크로 수백만 개의 새로운 안정 결정 후보를 예측한 GNoME(Nature, arXiv 논문 아님).

## 코드 생성 모델

### 13-11. Evaluating Large Language Models Trained on Code

- **식별자**: [arXiv:2107.03374](https://arxiv.org/abs/2107.03374)
- **연도 / 저자·기관**: 2021 / Chen et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Codex`, `HumanEval`
- **요약**: GitHub 코드로 미세조정한 Codex와 코드 생성 평가 벤치마크 HumanEval 제안.

### 13-12. Competition-Level Code Generation with AlphaCode

- **식별자**: [arXiv:2203.07814](https://arxiv.org/abs/2203.07814)
- **연도 / 저자·기관**: 2022 / Li et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AlphaCode`, `competitive-programming`
- **요약**: 대량 샘플링과 필터링·군집화로 프로그래밍 대회 문제를 푸는 AlphaCode.

### 13-13. StarCoder: may the source be with you!

- **식별자**: [arXiv:2305.06161](https://arxiv.org/abs/2305.06161)
- **연도 / 저자·기관**: 2023 / Li et al. (BigCode)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `StarCoder`, `open-code-LLM`
- **요약**: 허가형 라이선스 코드로 학습한 15B 오픈 코드 모델.

### 13-14. Code Llama: Open Foundation Models for Code

- **식별자**: [arXiv:2308.12950](https://arxiv.org/abs/2308.12950)
- **연도 / 저자·기관**: 2023 / Rozière et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Code-Llama`, `infilling`
- **요약**: Llama 2를 코드로 추가 학습하고 중간 채우기·긴 컨텍스트를 지원하는 코드 모델.

### 13-15. Qwen2.5-Coder Technical Report

- **식별자**: [arXiv:2409.12186](https://arxiv.org/abs/2409.12186)
- **연도 / 저자·기관**: 2024 / Hui et al. (Qwen)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Qwen2.5-Coder`, `code-LLM`
- **요약**: Qwen2.5 기반 코드 특화 모델 시리즈 보고서.

## 수학 · 정리 증명

### 13-16. Solving Quantitative Reasoning Problems with Language Models

- **식별자**: [arXiv:2206.14858](https://arxiv.org/abs/2206.14858)
- **연도 / 저자·기관**: 2022 / Lewkowycz et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Minerva`, `STEM`
- **요약**: 수학·과학 텍스트로 추가 학습한 Minerva로 정량적 추론 성능을 높임.

### 13-17. Llemma: An Open Language Model For Mathematics

- **식별자**: [arXiv:2310.10631](https://arxiv.org/abs/2310.10631)
- **연도 / 저자·기관**: 2023 / Azerbayev et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Llemma`, `math-LLM`
- **요약**: 수학 코퍼스로 Code Llama를 추가 학습한 오픈 수학 모델.

### 13-18. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement

- **식별자**: [arXiv:2409.12122](https://arxiv.org/abs/2409.12122)
- **연도 / 저자·기관**: 2024 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen2.5-Math`, `self-improvement`
- **요약**: 자기 개선을 통해 수학 전문 모델을 만든 Qwen2.5-Math 기술 보고서.

### 13-19. DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition

- **식별자**: [arXiv:2504.21801](https://arxiv.org/abs/2504.21801)
- **연도 / 저자·기관**: 2025 / Ren et al. (DeepSeek)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Lean`, `theorem-proving`, `subgoal`
- **요약**: DeepSeek-V3로 증명을 하위 목표로 분해하고 강화학습을 적용하는 형식 증명 모델. 671B 모델에서 RL을 하고 7B는 증류 후 RL(검색 결과 기준).

### 13-20. Mathematical discoveries from program search with large language models

- **식별자**: [링크](https://doi.org/10.1038/s41586-023-06924-6)
- **연도 / 저자·기관**: 2023 / Romera-Paredes et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `FunSearch`, `program-search`
- **요약**: LLM으로 프로그램을 진화시키고 평가기로 걸러 수학적 새 구성(예: cap set 문제)을 발견한 FunSearch(Nature, arXiv 논문 아님).

### 13-21. Solving olympiad geometry without human demonstrations

- **식별자**: [링크](https://doi.org/10.1038/s41586-023-06747-5)
- **연도 / 저자·기관**: 2024 / Trinh et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AlphaGeometry`, `neuro-symbolic`
- **요약**: 합성 증명 데이터로 학습한 언어모델과 기호 엔진을 결합해 올림피아드 기하 문제를 해결(Nature, arXiv 논문 아님).
