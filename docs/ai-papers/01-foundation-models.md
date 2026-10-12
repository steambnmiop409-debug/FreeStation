# 01. 파운데이션 모델과 기술 보고서

대규모 언어모델(LLM) 계보의 기준점이 되는 모델·기술 보고서 모음. 폐쇄형 모델의 보고서는 구조·데이터 공개 범위가 제한적이므로 요약에도 그 한계를 반영했다.

> 수록 38편 · 검증(V) 13편 · 기억기반(M) 25편

## 목차

- **초기 사전학습 모델 (2018–2022)** (10편)
  - 1. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)
  - 2. Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (2019)
  - 3. Language Models are Few-Shot Learners (2020)
  - 4. Scaling Language Models: Methods, Analysis & Insights from Training Gopher (2021)
  - 5. GLaM: Efficient Scaling of Language Models with Mixture-of-Experts (2021)
  - 6. LaMDA: Language Models for Dialog Applications (2022)
  - 7. PaLM: Scaling Language Modeling with Pathways (2022)
  - 8. OPT: Open Pre-trained Transformer Language Models (2022)
  - 9. BLOOM: A 176B-Parameter Open-Access Multilingual Language Model (2022)
  - 10. Pythia: A Suite of Models for Analyzing Large Language Models Across Training and Scaling (2023)
- **오픈 가중치 계열 (2023–2025)** (16편)
  - 11. LLaMA: Open and Efficient Foundation Language Models (2023)
  - 12. Llama 2: Open Foundation and Fine-Tuned Chat Models (2023)
  - 13. Mistral 7B (2023)
  - 14. Mixtral of Experts (2024)
  - 15. The Llama 3 Herd of Models (2024)
  - 16. Gemma: Open Models Based on Gemini Research and Technology (2024)
  - 17. Gemma 2: Improving Open Language Models at a Practical Size (2024)
  - 18. Gemma 3 Technical Report (2025)
  - 19. Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone (2024)
  - 20. Textbooks Are All You Need (2023)
  - 21. OLMo: Accelerating the Science of Language Models (2024)
  - 22. Yi: Open Foundation Models by 01.AI (2024)
  - 23. Qwen2.5 Technical Report (2024)
  - 24. Qwen3 Technical Report (2025)
  - 25. Qwen3-Coder-Next Technical Report (2026)
  - 26. MiMo-V2-Flash Technical Report (2026)
- **폐쇄형·프런티어 모델 보고서** (12편)
  - 27. GPT-4 Technical Report (2023)
  - 28. Gemini: A Family of Highly Capable Multimodal Models (2023)
  - 29. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context (2024)
  - 30. Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities (2025)
  - 31. OpenAI o1 System Card (2024)
  - 32. gpt-oss-120b & gpt-oss-20b Model Card (2025)
  - 33. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (2025)
  - 34. DeepSeek-V3 Technical Report (2024)
  - 35. DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model (2024)
  - 36. DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence (2024)
  - 37. Kimi k1.5: Scaling Reinforcement Learning with LLMs (2025)
  - 38. Kimi K2: Open Agentic Intelligence (2025)

## 초기 사전학습 모델 (2018–2022)

### 01-01. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- **식별자**: [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- **연도 / 저자·기관**: 2018 / Devlin et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `encoder`, `masked-LM`, `pretraining`
- **요약**: 마스크드 언어모델링으로 양방향 문맥을 사전학습한 인코더 모델. 사전학습 후 미세조정하는 방식을 NLP의 표준 절차로 만들었다.

### 01-02. Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

- **식별자**: [arXiv:1910.10683](https://arxiv.org/abs/1910.10683)
- **연도 / 저자·기관**: 2019 / Raffel et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `T5`, `text-to-text`, `C4`
- **요약**: 모든 NLP 과업을 텍스트 입력→텍스트 출력으로 통일하고, 사전학습 목표·구조·데이터를 체계적으로 비교한 T5 논문. C4 코퍼스를 함께 공개했다.

### 01-03. Language Models are Few-Shot Learners

- **식별자**: [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **연도 / 저자·기관**: 2020 / Brown et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GPT-3`, `in-context-learning`, `few-shot`
- **요약**: 1750억 파라미터 자기회귀 모델 GPT-3를 소개하고, 가중치 갱신 없이 프롬프트의 예시만으로 과업을 수행하는 few-shot 능력이 규모에 따라 커짐을 보였다.

### 01-04. Scaling Language Models: Methods, Analysis & Insights from Training Gopher

- **식별자**: [arXiv:2112.11446](https://arxiv.org/abs/2112.11446)
- **연도 / 저자·기관**: 2021 / Rae et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gopher`, `scaling`, `evaluation`
- **요약**: 2800억 파라미터 Gopher와 다양한 규모 모델의 비교 분석. 규모 확대가 독해·사실 지식에는 크게 도움이 되지만 논리·수학 추론에는 덜하다는 관찰을 담았다.

### 01-05. GLaM: Efficient Scaling of Language Models with Mixture-of-Experts

- **식별자**: [arXiv:2112.06905](https://arxiv.org/abs/2112.06905)
- **연도 / 저자·기관**: 2021 / Du et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MoE`, `sparse`, `efficiency`
- **요약**: 희소 활성 전문가 혼합(MoE) 구조로 dense 모델보다 적은 학습·추론 연산으로 비슷하거나 더 좋은 성능을 낸 초기 대형 MoE 언어모델.

### 01-06. LaMDA: Language Models for Dialog Applications

- **식별자**: [arXiv:2201.08239](https://arxiv.org/abs/2201.08239)
- **연도 / 저자·기관**: 2022 / Thoppilan et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `dialogue`, `safety`, `groundedness`
- **요약**: 대화에 특화된 LLM. 안전성·사실 근거성(groundedness)을 외부 도구 호출과 미세조정으로 높이는 방법을 다뤘다.

### 01-07. PaLM: Scaling Language Modeling with Pathways

- **식별자**: [arXiv:2204.02311](https://arxiv.org/abs/2204.02311)
- **연도 / 저자·기관**: 2022 / Chowdhery et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `PaLM`, `Pathways`, `540B`
- **요약**: Pathways 시스템으로 6144개 TPU v4에 학습한 5400억 파라미터 dense 모델. 다단계 추론 등에서 규모에 따른 급격한 향상(불연속 향상)을 보고했다.

### 01-08. OPT: Open Pre-trained Transformer Language Models

- **식별자**: [arXiv:2205.01068](https://arxiv.org/abs/2205.01068)
- **연도 / 저자·기관**: 2022 / Zhang et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `open-weights`, `replication`
- **요약**: GPT-3급 모델을 재현해 가중치와 학습 로그북까지 공개한 Meta의 오픈 모델군(최대 175B).

### 01-09. BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

- **식별자**: [arXiv:2211.05100](https://arxiv.org/abs/2211.05100)
- **연도 / 저자·기관**: 2022 / BigScience Workshop
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `multilingual`, `open-science`
- **요약**: 수백 명의 연구자가 공동 학습한 1760억 파라미터 다국어 오픈 액세스 모델.

### 01-10. Pythia: A Suite of Models for Analyzing Large Language Models Across Training and Scaling

- **식별자**: [arXiv:2304.01373](https://arxiv.org/abs/2304.01373)
- **연도 / 저자·기관**: 2023 / Biderman et al. (EleutherAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `checkpoints`, `interpretability`, `training-dynamics`
- **요약**: 동일 데이터·순서로 학습한 70M~12B 모델군과 학습 중간 체크포인트를 공개해 학습 동역학·암기·편향 연구를 가능하게 했다.

## 오픈 가중치 계열 (2023–2025)

### 01-11. LLaMA: Open and Efficient Foundation Language Models

- **식별자**: [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)
- **연도 / 저자·기관**: 2023 / Touvron et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LLaMA`, `open-weights`, `data`
- **요약**: 공개 데이터만으로 학습한 7B~65B 모델. 추론 비용을 고려해 모델을 작게 두고 토큰을 더 많이 학습하는 방향을 택했고, 이후 오픈 모델 생태계의 출발점이 됐다.

### 01-12. Llama 2: Open Foundation and Fine-Tuned Chat Models

- **식별자**: [arXiv:2307.09288](https://arxiv.org/abs/2307.09288)
- **연도 / 저자·기관**: 2023 / Touvron et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Llama-2`, `RLHF`, `safety`
- **요약**: 7B~70B 사전학습 모델과 RLHF로 다듬은 채팅 모델을 상업 이용이 가능한 라이선스로 공개하고, 미세조정·안전성 절차를 상세히 기술.

### 01-13. Mistral 7B

- **식별자**: [arXiv:2310.06825](https://arxiv.org/abs/2310.06825)
- **연도 / 저자·기관**: 2023 / Jiang et al. (Mistral AI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GQA`, `sliding-window`, `small-model`
- **요약**: 그룹 질의 어텐션(GQA)과 슬라이딩 윈도 어텐션을 써서 7B 규모로 더 큰 Llama 2 13B를 여러 벤치마크에서 앞선 모델.

### 01-14. Mixtral of Experts

- **식별자**: [arXiv:2401.04088](https://arxiv.org/abs/2401.04088)
- **연도 / 저자·기관**: 2024 / Jiang et al. (Mistral AI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MoE`, `sparse`, `open-weights`
- **요약**: 토큰마다 8개 전문가 중 2개를 선택하는 희소 MoE 모델. 총 파라미터 대비 활성 파라미터가 작아 추론 효율이 높다.

### 01-15. The Llama 3 Herd of Models

- **식별자**: [arXiv:2407.21783](https://arxiv.org/abs/2407.21783)
- **연도 / 저자·기관**: 2024 / Llama Team (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Llama-3`, `405B`, `dense`
- **요약**: 8B·70B·405B 규모의 Llama 3 계열 보고서. 최대 모델은 128K 컨텍스트의 dense Transformer이며 약 15.6T 토큰으로 사전학습, 다국어·코딩·추론·도구 사용을 지원한다.

### 01-16. Gemma: Open Models Based on Gemini Research and Technology

- **식별자**: [arXiv:2403.08295](https://arxiv.org/abs/2403.08295)
- **연도 / 저자·기관**: 2024 / Gemma Team (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gemma`, `open-weights`, `small-model`
- **요약**: Gemini 연구·기술을 바탕으로 한 경량 오픈 모델(2B·7B)의 기술 보고서.

### 01-17. Gemma 2: Improving Open Language Models at a Practical Size

- **식별자**: [arXiv:2408.00118](https://arxiv.org/abs/2408.00118)
- **연도 / 저자·기관**: 2024 / Gemma Team (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gemma-2`, `distillation`
- **요약**: 지식 증류와 지역-전역 어텐션 교차 등을 적용해 2B~27B 실용 크기에서 성능을 높인 Gemma 2 보고서.

### 01-18. Gemma 3 Technical Report

- **식별자**: [arXiv:2503.19786](https://arxiv.org/abs/2503.19786)
- **연도 / 저자·기관**: 2025 / Gemma Team (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Gemma-3`, `open-weights`
- **요약**: Gemma 3 기술 보고서. 이번 작업에서는 ID와 제목 일치만 확인했고 본문 세부는 검토하지 않았다.

### 01-19. Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone

- **식별자**: [arXiv:2404.14219](https://arxiv.org/abs/2404.14219)
- **연도 / 저자·기관**: 2024 / Abdin et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Phi-3`, `small-model`, `data-quality`
- **요약**: 고품질 필터링·합성 데이터로 학습해 휴대폰에서 구동 가능한 3.8B 모델이 훨씬 큰 모델에 근접한 성능을 낸다고 보고.

### 01-20. Textbooks Are All You Need

- **식별자**: [arXiv:2306.11644](https://arxiv.org/abs/2306.11644)
- **연도 / 저자·기관**: 2023 / Gunasekar et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `phi-1`, `synthetic-data`, `code`
- **요약**: ‘교과서 품질’ 데이터와 합성 교재·연습문제로 학습한 1.3B 코드 모델 phi-1. 데이터 품질이 규모를 일부 대체할 수 있다는 주장을 낳았다.

### 01-21. OLMo: Accelerating the Science of Language Models

- **식별자**: [arXiv:2402.00838](https://arxiv.org/abs/2402.00838)
- **연도 / 저자·기관**: 2024 / Groeneveld et al. (AI2)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `fully-open`, `reproducibility`
- **요약**: 가중치뿐 아니라 학습 데이터·코드·평가·체크포인트까지 전부 공개한 완전 개방형 언어모델.

### 01-22. Yi: Open Foundation Models by 01.AI

- **식별자**: [arXiv:2403.04652](https://arxiv.org/abs/2403.04652)
- **연도 / 저자·기관**: 2024 / 01.AI
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Yi`, `bilingual`, `data-engineering`
- **요약**: 영어·중국어 기반 6B·34B 모델과 데이터 정제 파이프라인을 보고한 01.AI의 기술 보고서.

### 01-23. Qwen2.5 Technical Report

- **식별자**: [arXiv:2412.15115](https://arxiv.org/abs/2412.15115)
- **연도 / 저자·기관**: 2024 / Qwen Team (Alibaba)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen2.5`, `open-weights`, `18T-tokens`
- **요약**: 0.5B~72B 규모의 오픈 가중치 모델을 포함한 시리즈. 사전학습 데이터가 18조 토큰으로 확대됐고, 독점 모델 Qwen2.5-Turbo/Plus는 GPT-4o-mini/GPT-4o와 견줘 소개된다.

### 01-24. Qwen3 Technical Report

- **식별자**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)
- **연도 / 저자·기관**: 2025 / Qwen Team (Alibaba)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen3`, `MoE`, `thinking-budget`
- **요약**: 0.6B~235B의 dense·MoE 모델군. 사용자가 추론 연산 예산을 조절하는 ‘thinking budget’ 메커니즘을 도입했고 지원 언어를 29개에서 119개로 늘렸다(Apache 2.0).

### 01-25. Qwen3-Coder-Next Technical Report

- **식별자**: [arXiv:2603.00729](https://arxiv.org/abs/2603.00729)
- **연도 / 저자·기관**: 2026 / Qwen Team (Alibaba)
- **검증 상태**: ✅ 검증(V)
- **태그**: `coding-agent`, `MoE`
- **요약**: 총 80B·활성 3B 파라미터의 코딩 에이전트용 모델 보고서(검색 결과의 설명 기준, 본문 미검토).

### 01-26. MiMo-V2-Flash Technical Report

- **식별자**: [arXiv:2601.02780](https://arxiv.org/abs/2601.02780)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `MiMo`, `technical-report`
- **요약**: ID와 제목 일치만 확인한 2026년 기술 보고서. 세부 내용은 원문 확인 필요.

## 폐쇄형·프런티어 모델 보고서

### 01-27. GPT-4 Technical Report

- **식별자**: [arXiv:2303.08774](https://arxiv.org/abs/2303.08774)
- **연도 / 저자·기관**: 2023 / OpenAI
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GPT-4`, `multimodal`, `predictable-scaling`
- **요약**: 이미지·텍스트 입력을 받는 GPT-4의 성능·안전성 평가 보고서. 모델 구조·규모·데이터는 공개하지 않았으며, 소규모 모델로 대형 모델 성능을 예측하는 ‘예측 가능한 스케일링’을 강조했다.

### 01-28. Gemini: A Family of Highly Capable Multimodal Models

- **식별자**: [arXiv:2312.11805](https://arxiv.org/abs/2312.11805)
- **연도 / 저자·기관**: 2023 / Gemini Team (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gemini`, `multimodal`
- **요약**: 텍스트·이미지·오디오·비디오를 처음부터 함께 학습한 Gemini 1.0 계열(Ultra/Pro/Nano) 보고서.

### 01-29. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context

- **식별자**: [arXiv:2403.05530](https://arxiv.org/abs/2403.05530)
- **연도 / 저자·기관**: 2024 / Gemini Team (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Gemini-1.5`, `long-context`, `multimodal`
- **요약**: 긴 문서·수 시간 분량 영상·오디오를 다루는 Gemini 1.5 Pro/Flash 보고서. 최소 1000만 토큰까지 99% 초과의 검색(retrieval) 정확도를 보고한다.

### 01-30. Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities

- **식별자**: [arXiv:2507.06261](https://arxiv.org/abs/2507.06261)
- **연도 / 저자·기관**: 2025 / Gemini Team (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Gemini-2.5`, `reasoning`, `agentic`
- **요약**: Gemini 2.5 계열 보고서. 이번 작업에서는 ID·제목 일치만 확인했다.

### 01-31. OpenAI o1 System Card

- **식별자**: [arXiv:2412.16720](https://arxiv.org/abs/2412.16720)
- **연도 / 저자·기관**: 2024 / Jaech et al. (OpenAI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `o1`, `reasoning`, `system-card`
- **요약**: 추론 모델 o1의 안전성 평가 시스템 카드. 모델 학습 세부는 공개하지 않으며, 평가 결과 중심으로 읽어야 한다.

### 01-32. gpt-oss-120b & gpt-oss-20b Model Card

- **식별자**: [arXiv:2508.10925](https://arxiv.org/abs/2508.10925)
- **연도 / 저자·기관**: 2025 / OpenAI
- **검증 상태**: ✅ 검증(V)
- **태그**: `gpt-oss`, `open-weights`, `MoE`, `MXFP4`
- **요약**: Apache 2.0 오픈 가중치 추론 모델 2종. 120b는 총 약 116.8B·활성 약 5.1B, 20b는 총 약 20.9B·활성 약 3.6B 파라미터이며 MoE 가중치를 MXFP4로 양자화했다.

### 01-33. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **식별자**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
- **연도 / 저자·기관**: 2025 / DeepSeek-AI
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `R1`, `GRPO`, `RLVR`, `reasoning`
- **요약**: 검증 가능한 보상 기반 강화학습만으로 긴 사고 사슬 추론이 출현함을 보인 R1-Zero와, 소량 콜드스타트 데이터를 더한 R1. 오픈 추론 모델 붐의 기점.

### 01-34. DeepSeek-V3 Technical Report

- **식별자**: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)
- **연도 / 저자·기관**: 2024 / DeepSeek-AI
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoE`, `MLA`, `FP8`, `multi-token-prediction`
- **요약**: 총 671B·토큰당 활성 37B의 MoE 모델. MLA와 DeepSeekMoE를 유지하고 보조 손실 없는 부하 분산과 다중 토큰 예측 목표를 도입했으며 14.8T 토큰, 약 278.8만 H800 GPU-시간으로 학습했다.

### 01-35. DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

- **식별자**: [arXiv:2405.04434](https://arxiv.org/abs/2405.04434)
- **연도 / 저자·기관**: 2024 / DeepSeek-AI
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MLA`, `MoE`, `KV-cache`
- **요약**: KV 캐시를 크게 줄이는 Multi-head Latent Attention(MLA)과 DeepSeekMoE를 결합한 236B(활성 21B) MoE 모델.

### 01-36. DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence

- **식별자**: [arXiv:2401.14196](https://arxiv.org/abs/2401.14196)
- **연도 / 저자·기관**: 2024 / Guo et al. (DeepSeek)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `code`, `repo-level`, `open-weights`
- **요약**: 저장소 수준 코드 데이터로 학습한 1.3B~33B 오픈 코드 모델군.

### 01-37. Kimi k1.5: Scaling Reinforcement Learning with LLMs

- **식별자**: [arXiv:2501.12599](https://arxiv.org/abs/2501.12599)
- **연도 / 저자·기관**: 2025 / Kimi Team (Moonshot AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `RL`, `long-CoT`, `multimodal`
- **요약**: 강화학습 기반 멀티모달 LLM의 학습 레시피 보고서. short-CoT 설정에서 AIME 60.8, MATH500 94.6, LiveCodeBench 47.3을 보고했다.

### 01-38. Kimi K2: Open Agentic Intelligence

- **식별자**: [arXiv:2507.20534](https://arxiv.org/abs/2507.20534)
- **연도 / 저자·기관**: 2025 / Kimi Team (Moonshot AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoE`, `MuonClip`, `agentic`
- **요약**: 총 1조·활성 320억 파라미터 MoE. MuonClip 옵티마이저로 15.5T 토큰을 손실 급등(loss spike) 없이 사전학습했고, 대규모 에이전트 데이터 합성과 통합 RL 단계를 거쳤다.
