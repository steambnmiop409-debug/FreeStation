# 03. 트랜스포머 이후의 아키텍처 (SSM · 선형 어텐션 · 순환 · 확산 언어모델 · 잠재 추론)

2^n 비용의 어텐션을 대체·보완하려는 상태공간모델, 선형 어텐션, 하이브리드, 테스트 시점 학습 메모리, 확산 기반 언어모델, 연속 잠재공간 추론 등 차세대 구조 연구.

> 수록 63편 · 검증(V) 37편 · 기억기반(M) 26편

## 목차

- **기준점** (4편)
  - 1. Attention Is All You Need (2017)
  - 2. Universal Transformers (2018)
  - 3. GLU Variants Improve Transformer (2020)
  - 4. Root Mean Square Layer Normalization (2019)
- **상태공간모델(SSM)과 Mamba 계열** (9편)
  - 5. HiPPO: Recurrent Memory with Optimal Polynomial Projections (2020)
  - 6. Efficiently Modeling Long Sequences with Structured State Spaces (2021)
  - 7. Hungry Hungry Hippos: Towards Language Modeling with State Space Models (2022)
  - 8. Hyena Hierarchy: Towards Larger Convolutional Language Models (2023)
  - 9. Mamba: Linear-Time Sequence Modeling with Selective State Spaces (2023)
  - 10. Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality (2024)
  - 11. MambaByte: Token-free Selective State Space Model (2024)
  - 12. Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model (2024)
  - 13. VMamba: Visual State Space Model (2024)
- **선형 어텐션·델타 규칙·순환 계열** (17편)
  - 14. Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention (2020)
  - 15. Linear Transformers Are Secretly Fast Weight Programmers (2021)
  - 16. RWKV: Reinventing RNNs for the Transformer Era (2023)
  - 17. Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence (2024)
  - 18. Retentive Network: A Successor to Transformer for Large Language Models (2023)
  - 19. Gated Linear Attention Transformers with Hardware-Efficient Training (2023)
  - 20. Simple linear attention language models balance the recall-throughput tradeoff (2024)
  - 21. Parallelizing Linear Transformers with the Delta Rule over Sequence Length (2024)
  - 22. Gated Delta Networks: Improving Mamba2 with Delta Rule (2024)
  - 23. DeltaProduct: Increasing the Expressivity of DeltaNet Through Products of Householders (2025)
  - 24. Jamba: A Hybrid Transformer-Mamba Language Model (2024)
  - 25. Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models (2024)
  - 26. xLSTM: Extended Long Short-Term Memory (2024)
  - 27. Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling (2024)
  - 28. Hymba: A Hybrid-head Architecture for Small Language Models (2024)
  - 29. Hybrid Architectures for Language Models: Systematic Analysis and Design Insights (2025)
  - 30. A Systematic Analysis of Hybrid Linear Attention (2025)
- **테스트 시점 학습(TTT)·장기 메모리** (14편)
  - 31. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context (2019)
  - 32. Compressive Transformers for Long-Range Sequence Modelling (2019)
  - 33. Memorizing Transformers (2022)
  - 34. Block-Recurrent Transformers (2022)
  - 35. Recurrent Memory Transformer (2022)
  - 36. Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention (2024)
  - 37. A Study of Infini-Attention in Small-Scale Pretraining (2025)
  - 38. Learning to (Learn at Test Time): RNNs with Expressive Hidden States (2024)
  - 39. Titans: Learning to Memorize at Test Time (2024)
  - 40. Titans Revisited: A Lightweight Reimplementation and Critical Analysis of a Test-Time Memory Model (2025)
  - 41. Atlas: Learning to Optimally Memorize the Context at Test Time (2025)
  - 42. Test-Time Training Done Right (2025)
  - 43. End-to-End Test-Time Training for Long Context (2025)
  - 44. The Surprising Effectiveness of Test-Time Training for Few-Shot Learning (2024)
- **정규화·어텐션 변형** (2편)
  - 45. nGPT: Normalized Transformer with Representation Learning on the Hypersphere (2024)
  - 46. Differential Transformer (2024)
- **확산(Diffusion) 언어모델** (9편)
  - 47. Structured Denoising Diffusion Models in Discrete State-Spaces (2021)
  - 48. Diffusion-LM Improves Controllable Text Generation (2022)
  - 49. Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution (2023)
  - 50. Simple and Effective Masked Diffusion Language Models (2024)
  - 51. Large Language Diffusion Models (2025)
  - 52. Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models (2025)
  - 53. Dream 7B: Diffusion Large Language Models (2025)
  - 54. LLaDA2.0: Scaling Up Diffusion Language Models to 100B (2025)
  - 55. LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning (2025)
- **잠재 공간 추론·토크나이저 없는 모델·적응형 깊이** (8편)
  - 56. MegaByte: Predicting Million-byte Sequences with Multiscale Transformers (2023)
  - 57. ByT5: Towards a token-free future with pre-trained byte-to-byte models (2021)
  - 58. Byte Latent Transformer: Patches Scale Better Than Tokens (2024)
  - 59. Large Concept Models: Language Modeling in a Sentence Representation Space (2024)
  - 60. Training Large Language Models to Reason in a Continuous Latent Space (2024)
  - 61. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach (2025)
  - 62. Mixture-of-Depths: Dynamically allocating compute in transformer-based language models (2024)
  - 63. Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (2025)

## 기준점

### 03-01. Attention Is All You Need

- **식별자**: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- **연도 / 저자·기관**: 2017 / Vaswani et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Transformer`, `self-attention`
- **요약**: 순환·합성곱 없이 어텐션만으로 구성한 Transformer를 제안한 논문. 이후 거의 모든 대형 모델의 기반 구조.

### 03-02. Universal Transformers

- **식별자**: [arXiv:1807.03819](https://arxiv.org/abs/1807.03819)
- **연도 / 저자·기관**: 2018 / Dehghani et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `recurrence`, `adaptive-depth`
- **요약**: 층을 공유해 반복 적용하고 토큰별로 계산 깊이를 조절하는 Transformer. 최근의 깊이 반복(recurrent depth) 연구의 선행 아이디어.

### 03-03. GLU Variants Improve Transformer

- **식별자**: [arXiv:2002.05202](https://arxiv.org/abs/2002.05202)
- **연도 / 저자·기관**: 2020 / Shazeer (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FFN`, `SwiGLU`
- **요약**: FFN에 게이트 선형 유닛(GLU) 변형을 쓰면 품질이 개선됨을 보인 짧은 논문. SwiGLU는 이후 LLM의 표준이 됐다.

### 03-04. Root Mean Square Layer Normalization

- **식별자**: [arXiv:1910.07467](https://arxiv.org/abs/1910.07467)
- **연도 / 저자·기관**: 2019 / Zhang & Sennrich
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RMSNorm`, `normalization`
- **요약**: 평균 제거 없이 RMS로만 정규화해 LayerNorm보다 간단하고 빠른 RMSNorm 제안. Llama 등이 채택.

## 상태공간모델(SSM)과 Mamba 계열

### 03-05. HiPPO: Recurrent Memory with Optimal Polynomial Projections

- **식별자**: [arXiv:2008.07669](https://arxiv.org/abs/2008.07669)
- **연도 / 저자·기관**: 2020 / Gu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SSM`, `memory`
- **요약**: 연속 신호의 과거를 다항식 기저로 최적 투영해 긴 기억을 유지하는 순환 메모리 이론. S4의 기반.

### 03-06. Efficiently Modeling Long Sequences with Structured State Spaces

- **식별자**: [arXiv:2111.00396](https://arxiv.org/abs/2111.00396)
- **연도 / 저자·기관**: 2021 / Gu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `S4`, `SSM`, `long-sequence`
- **요약**: 구조화된 상태공간 층(S4)으로 매우 긴 시퀀스를 효율적으로 처리한 논문. Long Range Arena 등에서 두각.

### 03-07. Hungry Hungry Hippos: Towards Language Modeling with State Space Models

- **식별자**: [arXiv:2212.14052](https://arxiv.org/abs/2212.14052)
- **연도 / 저자·기관**: 2022 / Fu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `H3`, `SSM`, `language-modeling`
- **요약**: 언어모델링에서 SSM이 부족했던 회상·비교 능력을 보강한 H3 층과 이를 위한 FlashConv 구현.

### 03-08. Hyena Hierarchy: Towards Larger Convolutional Language Models

- **식별자**: [arXiv:2302.10866](https://arxiv.org/abs/2302.10866)
- **연도 / 저자·기관**: 2023 / Poli et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Hyena`, `long-convolution`
- **요약**: 어텐션을 긴 합성곱과 게이팅으로 대체한 준2차 이하 비용의 연산자.

### 03-09. Mamba: Linear-Time Sequence Modeling with Selective State Spaces

- **식별자**: [arXiv:2312.00752](https://arxiv.org/abs/2312.00752)
- **연도 / 저자·기관**: 2023 / Gu & Dao
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mamba`, `selective-SSM`, `linear-time`
- **요약**: 입력에 따라 SSM 파라미터가 달라지는 선택적 상태공간 모델. 시퀀스 길이에 선형으로 확장되며 3B 모델이 같은 크기 Transformer를 능가하고 2배 큰 모델에 필적한다고 보고(언어·오디오·유전체).

### 03-10. Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

- **식별자**: [arXiv:2405.21060](https://arxiv.org/abs/2405.21060)
- **연도 / 저자·기관**: 2024 / Dao & Gu
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mamba-2`, `SSD`, `duality`
- **요약**: SSM과 마스킹된 어텐션 사이의 구조적 이중성(SSD)을 밝히고 이를 이용한 Mamba-2 층을 제안.

### 03-11. MambaByte: Token-free Selective State Space Model

- **식별자**: [arXiv:2401.13660](https://arxiv.org/abs/2401.13660)
- **연도 / 저자·기관**: 2024 / Wang et al. (Cornell)
- **검증 상태**: ✅ 검증(V)
- **태그**: `byte-level`, `tokenizer-free`, `Mamba`
- **요약**: Mamba를 원시 바이트 시퀀스에 적용한 토크나이저 없는 모델. 바이트 수준 모델 중 효율이 좋고 서브워드 Transformer와 경쟁한다고 보고.

### 03-12. Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model

- **식별자**: [arXiv:2401.09417](https://arxiv.org/abs/2401.09417)
- **연도 / 저자·기관**: 2024 / Zhu et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Vision-Mamba`, `SSM`, `vision`
- **요약**: 양방향 SSM을 이미지 패치 시퀀스에 적용한 비전 백본.

### 03-13. VMamba: Visual State Space Model

- **식별자**: [arXiv:2401.10166](https://arxiv.org/abs/2401.10166)
- **연도 / 저자·기관**: 2024 / Liu et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `VMamba`, `SSM`, `vision`
- **요약**: 2D 선택 스캔으로 이미지에 맞게 Mamba를 변형한 비전 백본.

## 선형 어텐션·델타 규칙·순환 계열

### 03-14. Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention

- **식별자**: [arXiv:2006.16236](https://arxiv.org/abs/2006.16236)
- **연도 / 저자·기관**: 2020 / Katharopoulos et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `linear-attention`, `RNN`
- **요약**: 커널 특성 맵으로 소프트맥스를 근사해 어텐션을 선형 시간 RNN 형태로 쓸 수 있음을 보인 논문.

### 03-15. Linear Transformers Are Secretly Fast Weight Programmers

- **식별자**: [arXiv:2102.11174](https://arxiv.org/abs/2102.11174)
- **연도 / 저자·기관**: 2021 / Schlag et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `fast-weights`, `delta-rule`
- **요약**: 선형 어텐션이 ‘빠른 가중치’ 프로그래머와 형식적으로 동등함을 보이고 델타 규칙 기반 갱신을 제안.

### 03-16. RWKV: Reinventing RNNs for the Transformer Era

- **식별자**: [arXiv:2305.13048](https://arxiv.org/abs/2305.13048)
- **연도 / 저자·기관**: 2023 / Peng et al. (RWKV)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RWKV`, `RNN`, `linear-time`
- **요약**: 학습은 Transformer처럼 병렬, 추론은 RNN처럼 상수 메모리로 할 수 있는 구조. 최대 14B 규모까지 확장.

### 03-17. Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence

- **식별자**: [arXiv:2404.05892](https://arxiv.org/abs/2404.05892)
- **연도 / 저자·기관**: 2024 / Peng et al. (RWKV)
- **검증 상태**: ✅ 검증(V)
- **태그**: `RWKV-5`, `RWKV-6`
- **요약**: RWKV를 행렬 값 상태(Eagle)와 데이터 의존적 순환(Finch)으로 개선한 후속 구조.

### 03-18. Retentive Network: A Successor to Transformer for Large Language Models

- **식별자**: [arXiv:2307.08621](https://arxiv.org/abs/2307.08621)
- **연도 / 저자·기관**: 2023 / Sun et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RetNet`, `retention`
- **요약**: 병렬·순환·청크 세 가지 계산 형태를 갖는 retention 메커니즘으로 학습 병렬성과 저비용 추론을 동시에 노린 구조.

### 03-19. Gated Linear Attention Transformers with Hardware-Efficient Training

- **식별자**: [arXiv:2312.06635](https://arxiv.org/abs/2312.06635)
- **연도 / 저자·기관**: 2023 / Yang et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `GLA`, `linear-attention`, `gating`
- **요약**: 데이터 의존 게이트를 갖는 선형 어텐션과 하드웨어 효율적 청크 병렬 학습 알고리즘.

### 03-20. Simple linear attention language models balance the recall-throughput tradeoff

- **식별자**: [arXiv:2402.18668](https://arxiv.org/abs/2402.18668)
- **연도 / 저자·기관**: 2024 / Arora et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Based`, `recall`, `linear-attention`
- **요약**: 선형 어텐션과 슬라이딩 윈도 어텐션을 결합해 회상 능력과 처리량의 균형을 맞춘 Based 모델.

### 03-21. Parallelizing Linear Transformers with the Delta Rule over Sequence Length

- **식별자**: [arXiv:2406.06484](https://arxiv.org/abs/2406.06484)
- **연도 / 저자·기관**: 2024 / Yang et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `DeltaNet`, `delta-rule`, `parallel-training`
- **요약**: 델타 규칙 기반 선형 Transformer(DeltaNet)를 시퀀스 길이 방향으로 병렬 학습하는 알고리즘을 제시해 중간 규모 언어모델링에 실용화.

### 03-22. Gated Delta Networks: Improving Mamba2 with Delta Rule

- **식별자**: [arXiv:2412.06464](https://arxiv.org/abs/2412.06464)
- **연도 / 저자·기관**: 2024 / Yang, Kautz, Hatamizadeh
- **검증 상태**: ✅ 검증(V)
- **태그**: `Gated-DeltaNet`, `gating`, `delta-rule`
- **요약**: 게이팅(빠른 망각)과 델타 규칙(정밀 갱신)을 결합한 구조. 언어모델링·상식추론·문맥 내 검색·길이 외삽에서 Mamba2와 DeltaNet을 앞선다고 보고(ICLR 2025).

### 03-23. DeltaProduct: Increasing the Expressivity of DeltaNet Through Products of Householders

- **식별자**: [arXiv:2502.10297](https://arxiv.org/abs/2502.10297)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `DeltaNet`, `expressivity`
- **요약**: DeltaNet의 표현력을 하우스홀더 행렬의 곱으로 확장하는 연구(ID·제목만 확인).

### 03-24. Jamba: A Hybrid Transformer-Mamba Language Model

- **식별자**: [arXiv:2403.19887](https://arxiv.org/abs/2403.19887)
- **연도 / 저자·기관**: 2024 / Lieber et al. (AI21)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Jamba`, `hybrid`, `MoE`
- **요약**: Transformer·Mamba 층과 MoE를 섞은 하이브리드 대형 모델. 긴 컨텍스트에서 메모리·처리량 이점을 강조.

### 03-25. Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models

- **식별자**: [arXiv:2402.19427](https://arxiv.org/abs/2402.19427)
- **연도 / 저자·기관**: 2024 / De et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Griffin`, `Hawk`, `recurrence`
- **요약**: 게이트 선형 순환(Hawk)과 지역 어텐션을 혼합한 Griffin. 같은 크기 대비 적은 학습 토큰으로 경쟁력 있는 성능을 보고.

### 03-26. xLSTM: Extended Long Short-Term Memory

- **식별자**: [arXiv:2405.04517](https://arxiv.org/abs/2405.04517)
- **연도 / 저자·기관**: 2024 / Beck et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `xLSTM`, `LSTM`
- **요약**: 지수 게이팅과 행렬 메모리(mLSTM) 등으로 LSTM을 현대적으로 확장한 구조.

### 03-27. Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling

- **식별자**: [arXiv:2406.07522](https://arxiv.org/abs/2406.07522)
- **연도 / 저자·기관**: 2024 / Ren et al. (Microsoft)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Samba`, `hybrid`, `sliding-window`
- **요약**: Mamba·슬라이딩 윈도 어텐션·MLP를 반복 적층한 하이브리드. 순환 상태로 시퀀스를 압축하면서 최근 토큰의 정확한 회상을 유지한다는 설계.

### 03-28. Hymba: A Hybrid-head Architecture for Small Language Models

- **식별자**: [arXiv:2411.13676](https://arxiv.org/abs/2411.13676)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Hymba`, `hybrid-head`, `small-model`
- **요약**: 소형 언어모델용 하이브리드 헤드 구조(ID·제목만 확인).

### 03-29. Hybrid Architectures for Language Models: Systematic Analysis and Design Insights

- **식별자**: [arXiv:2510.04800](https://arxiv.org/abs/2510.04800)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `hybrid`, `analysis`
- **요약**: 하이브리드 언어모델 구조의 체계적 분석과 설계 통찰을 다룬 2025년 연구(ID·제목만 확인).

### 03-30. A Systematic Analysis of Hybrid Linear Attention

- **식별자**: [arXiv:2507.06457](https://arxiv.org/abs/2507.06457)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `hybrid`, `linear-attention`, `analysis`
- **요약**: 선형 어텐션 하이브리드의 체계적 비교 분석(ID·제목만 확인).

## 테스트 시점 학습(TTT)·장기 메모리

### 03-31. Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

- **식별자**: [arXiv:1901.02860](https://arxiv.org/abs/1901.02860)
- **연도 / 저자·기관**: 2019 / Dai et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `segment-recurrence`, `long-context`
- **요약**: 세그먼트 수준 순환과 상대 위치 인코딩으로 고정 길이 문맥 한계를 넘은 모델.

### 03-32. Compressive Transformers for Long-Range Sequence Modelling

- **식별자**: [arXiv:1911.05507](https://arxiv.org/abs/1911.05507)
- **연도 / 저자·기관**: 2019 / Rae et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `memory`, `compression`
- **요약**: 오래된 기억을 압축해 보관하는 Transformer와 PG-19 장문 벤치마크.

### 03-33. Memorizing Transformers

- **식별자**: [arXiv:2203.08913](https://arxiv.org/abs/2203.08913)
- **연도 / 저자·기관**: 2022 / Wu et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `kNN-memory`, `external-memory`
- **요약**: 과거 (키, 값)을 외부 kNN 메모리에 저장해 추론 시 조회하는 어텐션 확장.

### 03-34. Block-Recurrent Transformers

- **식별자**: [arXiv:2203.07852](https://arxiv.org/abs/2203.07852)
- **연도 / 저자·기관**: 2022 / Hutchins et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `recurrence`, `long-context`
- **요약**: 블록 단위로 순환하며 상태를 전달하는 Transformer 층.

### 03-35. Recurrent Memory Transformer

- **식별자**: [arXiv:2207.06881](https://arxiv.org/abs/2207.06881)
- **연도 / 저자·기관**: 2022 / Bulatov et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `memory-tokens`
- **요약**: 메모리 토큰을 세그먼트 사이에 전달하는 순환 메모리 구조.

### 03-36. Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention

- **식별자**: [arXiv:2404.07143](https://arxiv.org/abs/2404.07143)
- **연도 / 저자·기관**: 2024 / Munkhdalai et al. (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Infini-attention`, `compressive-memory`
- **요약**: 지역 마스크 어텐션과 장기 선형 어텐션 메모리를 한 블록에 결합. 1M 토큰 패스키 검색과 50만 토큰 책 요약을 시험(1B·8B).

### 03-37. A Study of Infini-Attention in Small-Scale Pretraining

- **식별자**: [arXiv:2512.23862](https://arxiv.org/abs/2512.23862)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Infini-attention`, `negative-result`
- **요약**: Infini-attention의 소규모 사전학습 재검증. 검색 결과 기준 더 약한 결과가 보고됐다.

### 03-38. Learning to (Learn at Test Time): RNNs with Expressive Hidden States

- **식별자**: [arXiv:2407.04620](https://arxiv.org/abs/2407.04620)
- **연도 / 저자·기관**: 2024 / Sun et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `TTT`, `test-time-training`, `RNN`
- **요약**: RNN의 은닉 상태를 작은 모델로 보고 입력 시퀀스에서 직접 경사하강으로 갱신하는 TTT 층(ICML 2025).

### 03-39. Titans: Learning to Memorize at Test Time

- **식별자**: [arXiv:2501.00663](https://arxiv.org/abs/2501.00663)
- **연도 / 저자·기관**: 2024 / Behrouz, Zhong, Mirrokni (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Titans`, `neural-memory`, `long-context`
- **요약**: 추론 중에도 학습되는 장기 신경 메모리를 단기 어텐션과 결합한 Titans. 2M 토큰 이상 needle 과제에서 확장된다고 보고.

### 03-40. Titans Revisited: A Lightweight Reimplementation and Critical Analysis of a Test-Time Memory Model

- **식별자**: [arXiv:2510.09551](https://arxiv.org/abs/2510.09551)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Titans`, `reproducibility`
- **요약**: Titans를 재구현해 보면 청킹 때문에 항상 기존 기준선보다 낫지는 않으며, 공개 코드 부재와 설명의 모호함이 재현을 어렵게 한다고 지적.

### 03-41. Atlas: Learning to Optimally Memorize the Context at Test Time

- **식별자**: [arXiv:2505.23735](https://arxiv.org/abs/2505.23735)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Atlas`, `test-time-memory`
- **요약**: 테스트 시점 문맥 암기를 최적화하는 후속 연구(ID·제목만 확인).

### 03-42. Test-Time Training Done Right

- **식별자**: [arXiv:2505.23884](https://arxiv.org/abs/2505.23884)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `TTT`, `large-chunk`
- **요약**: TTT의 구현·청크 설계를 다룬 2025년 연구(ID·제목만 확인).

### 03-43. End-to-End Test-Time Training for Long Context

- **식별자**: [arXiv:2512.23675](https://arxiv.org/abs/2512.23675)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `TTT`, `long-context`
- **요약**: 장문 컨텍스트를 위한 종단간 테스트 시점 학습 연구(ID·제목만 확인).

### 03-44. The Surprising Effectiveness of Test-Time Training for Few-Shot Learning

- **식별자**: [arXiv:2411.07279](https://arxiv.org/abs/2411.07279)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `TTT`, `few-shot`, `ARC`
- **요약**: 퓨샷 과제에서 테스트 시점 학습의 효과를 보인 연구. ARC 계열 접근에 영향을 줬다.

## 정규화·어텐션 변형

### 03-45. nGPT: Normalized Transformer with Representation Learning on the Hypersphere

- **식별자**: [arXiv:2410.01131](https://arxiv.org/abs/2410.01131)
- **연도 / 저자·기관**: 2024 / Loshchilov et al. (NVIDIA)
- **검증 상태**: ✅ 검증(V)
- **태그**: `nGPT`, `hypersphere`, `normalization`
- **요약**: 임베딩·MLP·어텐션 행렬·은닉 상태를 모두 단위 노름으로 정규화해, 같은 정확도에 필요한 학습 스텝을 시퀀스 길이에 따라 4~20배 줄인다고 보고.

### 03-46. Differential Transformer

- **식별자**: [arXiv:2410.05258](https://arxiv.org/abs/2410.05258)
- **연도 / 저자·기관**: 2024 / Ye et al. (Microsoft)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Differential-Attention`, `noise-cancellation`
- **요약**: 두 소프트맥스 어텐션 맵의 차이로 어텐션을 계산해 무관한 문맥의 잡음을 줄인다. 장문 모델링·정보 검색·환각 감소·ICL 개선을 주장(ICLR 2025 구두).

## 확산(Diffusion) 언어모델

### 03-47. Structured Denoising Diffusion Models in Discrete State-Spaces

- **식별자**: [arXiv:2107.03006](https://arxiv.org/abs/2107.03006)
- **연도 / 저자·기관**: 2021 / Austin et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `D3PM`, `discrete-diffusion`
- **요약**: 이산 상태 공간에서의 확산 모델(D3PM)을 정식화해 텍스트 등 이산 데이터에 확산을 적용하는 토대를 마련.

### 03-48. Diffusion-LM Improves Controllable Text Generation

- **식별자**: [arXiv:2205.14217](https://arxiv.org/abs/2205.14217)
- **연도 / 저자·기관**: 2022 / Li et al. (Stanford)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Diffusion-LM`, `controllable`
- **요약**: 연속 임베딩 공간의 확산으로 구문·문법 등 세밀한 제어 생성을 가능하게 한 연구.

### 03-49. Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

- **식별자**: [arXiv:2310.16834](https://arxiv.org/abs/2310.16834)
- **연도 / 저자·기관**: 2023 / Lou et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SEDD`, `score-entropy`
- **요약**: 점수 엔트로피 손실로 이산 확산을 학습하는 SEDD. 당시 GPT-2급 비교에서 확산 LM의 격차를 크게 줄였다.

### 03-50. Simple and Effective Masked Diffusion Language Models

- **식별자**: [arXiv:2406.07524](https://arxiv.org/abs/2406.07524)
- **연도 / 저자·기관**: 2024 / Sahoo et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MDLM`, `masked-diffusion`
- **요약**: 마스크 기반 이산 확산을 단순한 목표로 학습해 확산 언어모델의 퍼플렉시티를 개선한 MDLM.

### 03-51. Large Language Diffusion Models

- **식별자**: [arXiv:2502.09992](https://arxiv.org/abs/2502.09992)
- **연도 / 저자·기관**: 2025 / Nie et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `LLaDA`, `masked-diffusion`, `8B`
- **요약**: 마스크 확산으로 처음부터 학습한 8B LLaDA. ICL이 LLaMA3 8B와 경쟁적이고 SFT 후 다중 턴 대화가 가능하며, 역전 시 완성 과제에서 GPT-4o를 앞섰다고 보고.

### 03-52. Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models

- **식별자**: [arXiv:2503.09573](https://arxiv.org/abs/2503.09573)
- **연도 / 저자·기관**: 2025 / Arriola et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `block-diffusion`, `KV-cache`, `flexible-length`
- **요약**: 블록 단위 자기회귀와 블록 내 확산을 보간하는 모델 계열. 가변 길이 생성, KV 캐시·병렬 샘플링을 가능하게 하고 확산 모델 중 최고 성능을 보고(ICLR 2025).

### 03-53. Dream 7B: Diffusion Large Language Models

- **식별자**: [arXiv:2508.15487](https://arxiv.org/abs/2508.15487)
- **연도 / 저자·기관**: 2025 / Ye et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Dream`, `diffusion-LM`, `AR-init`
- **요약**: AR 모델로 초기화한 7B 확산 LLM. 임의 순서 생성·채움(infilling)·품질-속도 조절이 가능하고 기존 확산 LM을 일관되게 앞선다고 보고.

### 03-54. LLaDA2.0: Scaling Up Diffusion Language Models to 100B

- **식별자**: [arXiv:2512.15745](https://arxiv.org/abs/2512.15745)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `LLaDA2.0`, `diffusion-LM`, `100B`
- **요약**: 사전학습된 자기회귀 모델을 변환해 확산 언어모델을 100B로 확장(검색 결과 기준).

### 03-55. LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning

- **식별자**: [arXiv:2505.16933](https://arxiv.org/abs/2505.16933)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `multimodal`, `diffusion-LM`
- **요약**: LLaDA에 시각 지시 튜닝을 더해 순수 확산 기반 멀티모달 모델을 구성한 연구.

## 잠재 공간 추론·토크나이저 없는 모델·적응형 깊이

### 03-56. MegaByte: Predicting Million-byte Sequences with Multiscale Transformers

- **식별자**: [arXiv:2305.07185](https://arxiv.org/abs/2305.07185)
- **연도 / 저자·기관**: 2023 / Yu et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `byte-level`, `multiscale`
- **요약**: 바이트를 패치로 묶어 전역·지역 모델로 나눠 백만 바이트 시퀀스를 다루는 다중 스케일 Transformer.

### 03-57. ByT5: Towards a token-free future with pre-trained byte-to-byte models

- **식별자**: [arXiv:2105.13626](https://arxiv.org/abs/2105.13626)
- **연도 / 저자·기관**: 2021 / Xue et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `byte-level`, `tokenizer-free`
- **요약**: 토크나이저 없이 바이트를 직접 입력으로 쓰는 T5 변형. 잡음·철자 변화에 강건.

### 03-58. Byte Latent Transformer: Patches Scale Better Than Tokens

- **식별자**: [arXiv:2412.09871](https://arxiv.org/abs/2412.09871)
- **연도 / 저자·기관**: 2024 / Pagnoni et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `BLT`, `byte-patches`, `dynamic-compute`
- **요약**: 다음 바이트의 예측 불확실성에 따라 가변 길이 패치를 구성하는 바이트 수준 모델. 8B·4T 바이트까지의 FLOP 통제 스케일링에서 토크나이저 기반 모델보다 낫게 확장된다고 보고.

### 03-59. Large Concept Models: Language Modeling in a Sentence Representation Space

- **식별자**: [arXiv:2412.08821](https://arxiv.org/abs/2412.08821)
- **연도 / 저자·기관**: 2024 / LCM team (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `LCM`, `SONAR`, `sentence-level`
- **요약**: 문장을 하나의 ‘개념’으로 보고 SONAR 임베딩 공간에서 다음 문장을 예측하는 모델. 1.6B(1.3T 토큰)와 7B(2.7T 토큰) 규모를 시험하고 요약·요약 확장 과제로 평가.

### 03-60. Training Large Language Models to Reason in a Continuous Latent Space

- **식별자**: [arXiv:2412.06769](https://arxiv.org/abs/2412.06769)
- **연도 / 저자·기관**: 2024 / Hao et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Coconut`, `latent-reasoning`, `continuous-thought`
- **요약**: 마지막 은닉 상태를 단어로 디코딩하지 않고 다음 입력으로 되돌리는 ‘연속 사고’ 방식(Coconut). 되돌아가기가 많은 계획 과제에서 CoT보다 적은 사고 토큰으로 우수하다고 보고.

### 03-61. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach

- **식별자**: [arXiv:2502.05171](https://arxiv.org/abs/2502.05171)
- **연도 / 저자·기관**: 2025 / Geiping et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `recurrent-depth`, `latent-reasoning`, `test-time-compute`
- **요약**: 순환 블록을 추론 시 더 많이 반복해 토큰을 늘리지 않고 연산을 늘리는 언어모델. 3.5B·8000억 토큰 규모 개념 증명 모델로 시연.

### 03-62. Mixture-of-Depths: Dynamically allocating compute in transformer-based language models

- **식별자**: [arXiv:2404.02258](https://arxiv.org/abs/2404.02258)
- **연도 / 저자·기관**: 2024 / Raposo et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mixture-of-Depths`, `conditional-compute`
- **요약**: 층마다 top-k 라우터가 처리할 토큰을 고르는 방식으로 정적 계산 그래프를 유지하며 연산을 동적으로 배분. 같은 성능에서 순전파 FLOP과 샘플링 시간을 줄인다고 보고.

### 03-63. Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

- **식별자**: [arXiv:2507.10524](https://arxiv.org/abs/2507.10524)
- **연도 / 저자·기관**: 2025 / Bae et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mixture-of-Recursions`, `parameter-sharing`, `adaptive-depth`
- **요약**: 파라미터를 공유한 재귀 Transformer에서 토큰마다 재귀 깊이를 라우팅하는 프레임워크(NeurIPS 2025).
