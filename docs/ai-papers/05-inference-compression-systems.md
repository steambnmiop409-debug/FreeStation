# 05. 추론 가속 · 양자화 · 압축 · 학습 시스템 · 옵티마이저

대형 모델을 싸고 빠르게 학습·서빙하기 위한 기법. 저비트 양자화, 추측 디코딩, 가지치기·증류, 병렬화 시스템, 차세대 옵티마이저를 포함한다.

> 수록 34편 · 검증(V) 7편 · 기억기반(M) 27편

## 목차

- **양자화·저정밀** (9편)
  - 1. LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (2022)
  - 2. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (2022)
  - 3. SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models (2022)
  - 4. AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration (2023)
  - 5. QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks (2024)
  - 6. BitNet: Scaling 1-bit Transformers for Large Language Models (2023)
  - 7. The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (2024)
  - 8. FP8 Formats for Deep Learning (2022)
  - 9. Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding (2015)
- **추측 디코딩·디코딩 가속** (3편)
  - 10. Fast Inference from Transformers via Speculative Decoding (2022)
  - 11. Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads (2024)
  - 12. EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty (2024)
- **가지치기·증류** (5편)
  - 13. Distilling the Knowledge in a Neural Network (2015)
  - 14. SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot (2023)
  - 15. A Simple and Effective Pruning Approach for Large Language Models (2023)
  - 16. Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning (2023)
  - 17. Compact Language Models via Pruning and Knowledge Distillation (2024)
- **분산 학습 시스템** (7편)
  - 18. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism (2018)
  - 19. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism (2019)
  - 20. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (2019)
  - 21. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM (2021)
  - 22. Mixed Precision Training (2017)
  - 23. In-Datacenter Performance Analysis of a Tensor Processing Unit (2017)
  - 24. TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings (2023)
- **옵티마이저** (10편)
  - 25. Adam: A Method for Stochastic Optimization (2014)
  - 26. Decoupled Weight Decay Regularization (2017)
  - 27. Shampoo: Preconditioned Stochastic Tensor Optimization (2018)
  - 28. Symbolic Discovery of Optimization Algorithms (2023)
  - 29. Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training (2023)
  - 30. The Road Less Scheduled (2024)
  - 31. GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection (2024)
  - 32. Muon is Scalable for LLM Training (2025)
  - 33. Practical Efficiency of Muon for Pretraining (2025)
  - 34. Dion: Distributed Orthonormalized Updates (2025)

## 양자화·저정밀

### 05-01. LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale

- **식별자**: [arXiv:2208.07339](https://arxiv.org/abs/2208.07339)
- **연도 / 저자·기관**: 2022 / Dettmers et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `int8`, `outliers`, `quantization`
- **요약**: 대형 모델에서 나타나는 이상치(outlier) 특징을 분리 처리해 성능 손실 없는 8비트 추론을 가능하게 한 방법.

### 05-02. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

- **식별자**: [arXiv:2210.17323](https://arxiv.org/abs/2210.17323)
- **연도 / 저자·기관**: 2022 / Frantar et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GPTQ`, `PTQ`, `4-bit`
- **요약**: 2차 정보 기반 층별 양자화로 수십억~천억 파라미터 모델을 3~4비트로 압축.

### 05-03. SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

- **식별자**: [arXiv:2211.10438](https://arxiv.org/abs/2211.10438)
- **연도 / 저자·기관**: 2022 / Xiao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SmoothQuant`, `W8A8`
- **요약**: 활성화의 이상치 어려움을 가중치로 옮겨 가중치·활성화를 모두 8비트로 양자화.

### 05-04. AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

- **식별자**: [arXiv:2306.00978](https://arxiv.org/abs/2306.00978)
- **연도 / 저자·기관**: 2023 / Lin et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AWQ`, `weight-only`, `4-bit`
- **요약**: 활성화 분포로 중요한 가중치 채널을 보호하는 가중치 전용 저비트 양자화.

### 05-05. QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks

- **식별자**: [arXiv:2402.04396](https://arxiv.org/abs/2402.04396)
- **연도 / 저자·기관**: 2024 / Tseng et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `QuIP-sharp`, `2-bit`, `lattice`
- **요약**: 하다마드 비일관성 처리와 격자 코드북으로 2비트급 양자화 품질을 높인 방법.

### 05-06. BitNet: Scaling 1-bit Transformers for Large Language Models

- **식별자**: [arXiv:2310.11453](https://arxiv.org/abs/2310.11453)
- **연도 / 저자·기관**: 2023 / Wang et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BitNet`, `1-bit`
- **요약**: 가중치를 1비트로 학습하는 Transformer 구조.

### 05-07. The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits

- **식별자**: [arXiv:2402.17764](https://arxiv.org/abs/2402.17764)
- **연도 / 저자·기관**: 2024 / Ma et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BitNet-b1.58`, `ternary`
- **요약**: 가중치를 {-1,0,1} 삼진값으로 제한해 전정밀도 모델과 동등한 성능과 낮은 지연·에너지를 주장한 BitNet b1.58.

### 05-08. FP8 Formats for Deep Learning

- **식별자**: [arXiv:2209.05433](https://arxiv.org/abs/2209.05433)
- **연도 / 저자·기관**: 2022 / Micikevicius et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FP8`, `low-precision`
- **요약**: 딥러닝용 8비트 부동소수점(E4M3/E5M2) 형식 제안.

### 05-09. Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding

- **식별자**: [arXiv:1510.00149](https://arxiv.org/abs/1510.00149)
- **연도 / 저자·기관**: 2015 / Han et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `pruning`, `quantization`, `compression`
- **요약**: 가지치기·양자화·허프만 부호화를 결합한 고전적 신경망 압축 파이프라인.

## 추측 디코딩·디코딩 가속

### 05-10. Fast Inference from Transformers via Speculative Decoding

- **식별자**: [arXiv:2211.17192](https://arxiv.org/abs/2211.17192)
- **연도 / 저자·기관**: 2022 / Leviathan et al. (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `speculative-decoding`
- **요약**: 작은 초안 모델이 여러 토큰을 제안하고 큰 모델이 병렬 검증해 출력 분포를 바꾸지 않고 가속하는 방법.

### 05-11. Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads

- **식별자**: [arXiv:2401.10774](https://arxiv.org/abs/2401.10774)
- **연도 / 저자·기관**: 2024 / Cai et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Medusa`, `multi-head-decoding`
- **요약**: 별도 초안 모델 없이 여러 디코딩 헤드로 다음 여러 토큰을 병렬 예측.

### 05-12. EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty

- **식별자**: [arXiv:2401.15077](https://arxiv.org/abs/2401.15077)
- **연도 / 저자·기관**: 2024 / Li et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `EAGLE`, `speculative-sampling`
- **요약**: 특징(feature) 수준에서 초안을 예측하는 추측 샘플링으로 높은 수락률 달성.

## 가지치기·증류

### 05-13. Distilling the Knowledge in a Neural Network

- **식별자**: [arXiv:1503.02531](https://arxiv.org/abs/1503.02531)
- **연도 / 저자·기관**: 2015 / Hinton, Vinyals, Dean
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `knowledge-distillation`
- **요약**: 큰 모델의 소프트 출력으로 작은 모델을 학습시키는 지식 증류의 고전.

### 05-14. SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot

- **식별자**: [arXiv:2301.00774](https://arxiv.org/abs/2301.00774)
- **연도 / 저자·기관**: 2023 / Frantar & Alistarh
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SparseGPT`, `pruning`
- **요약**: 재학습 없이 한 번에 대형 모델을 50% 이상 희소화.

### 05-15. A Simple and Effective Pruning Approach for Large Language Models

- **식별자**: [arXiv:2306.11695](https://arxiv.org/abs/2306.11695)
- **연도 / 저자·기관**: 2023 / Sun et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Wanda`, `pruning`
- **요약**: 가중치 크기와 입력 활성화 노름을 곱한 점수로 간단히 가지치기(Wanda).

### 05-16. Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning

- **식별자**: [arXiv:2310.06694](https://arxiv.org/abs/2310.06694)
- **연도 / 저자·기관**: 2023 / Xia et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `structured-pruning`, `small-model`
- **요약**: 구조적 가지치기와 이어진 추가 학습으로 작은 모델을 효율적으로 얻는 방법.

### 05-17. Compact Language Models via Pruning and Knowledge Distillation

- **식별자**: [arXiv:2407.14679](https://arxiv.org/abs/2407.14679)
- **연도 / 저자·기관**: 2024 / Muralidharan et al. (NVIDIA)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Minitron`, `pruning`, `distillation`
- **요약**: 15B 모델을 가지치기·증류로 8B·4B로 줄이며 원 학습 데이터의 3% 미만만 사용. 처음부터 학습 대비 토큰을 최대 40배 절감하고 MMLU를 최대 16% 개선했다고 보고.

## 분산 학습 시스템

### 05-18. GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism

- **식별자**: [arXiv:1811.06965](https://arxiv.org/abs/1811.06965)
- **연도 / 저자·기관**: 2018 / Huang et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `pipeline-parallelism`
- **요약**: 마이크로배치로 파이프라인 병렬화를 효율화한 GPipe.

### 05-19. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism

- **식별자**: [arXiv:1909.08053](https://arxiv.org/abs/1909.08053)
- **연도 / 저자·기관**: 2019 / Shoeybi et al. (NVIDIA)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Megatron`, `tensor-parallelism`
- **요약**: Transformer 층 내부를 쪼개는 텐서 병렬화로 수십억 파라미터를 학습.

### 05-20. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models

- **식별자**: [arXiv:1910.02054](https://arxiv.org/abs/1910.02054)
- **연도 / 저자·기관**: 2019 / Rajbhandari et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ZeRO`, `DeepSpeed`, `memory`
- **요약**: 옵티마이저 상태·기울기·파라미터를 장치 간 분할해 메모리 중복을 제거.

### 05-21. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM

- **식별자**: [arXiv:2104.04473](https://arxiv.org/abs/2104.04473)
- **연도 / 저자·기관**: 2021 / Narayanan et al. (NVIDIA)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `3D-parallelism`
- **요약**: 데이터·텐서·파이프라인 병렬을 결합해 수천 GPU에서 효율적으로 학습하는 방법.

### 05-22. Mixed Precision Training

- **식별자**: [arXiv:1710.03740](https://arxiv.org/abs/1710.03740)
- **연도 / 저자·기관**: 2017 / Micikevicius et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FP16`, `loss-scaling`
- **요약**: FP16 학습에 손실 스케일링 등을 쓰는 혼합 정밀 학습.

### 05-23. In-Datacenter Performance Analysis of a Tensor Processing Unit

- **식별자**: [arXiv:1704.04760](https://arxiv.org/abs/1704.04760)
- **연도 / 저자·기관**: 2017 / Jouppi et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `TPU`, `hardware`
- **요약**: 1세대 TPU의 설계와 성능 분석.

### 05-24. TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings

- **식별자**: [arXiv:2304.01433](https://arxiv.org/abs/2304.01433)
- **연도 / 저자·기관**: 2023 / Jouppi et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `TPU-v4`, `optical-interconnect`
- **요약**: 광 회로 스위치 기반 재구성 가능한 상호연결을 갖춘 TPU v4 슈퍼컴퓨터.

## 옵티마이저

### 05-25. Adam: A Method for Stochastic Optimization

- **식별자**: [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)
- **연도 / 저자·기관**: 2014 / Kingma & Ba
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Adam`, `optimizer`
- **요약**: 적응적 모멘트 추정 기반의 표준 옵티마이저.

### 05-26. Decoupled Weight Decay Regularization

- **식별자**: [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)
- **연도 / 저자·기관**: 2017 / Loshchilov & Hutter
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AdamW`, `weight-decay`
- **요약**: 가중치 감쇠를 기울기 갱신과 분리한 AdamW.

### 05-27. Shampoo: Preconditioned Stochastic Tensor Optimization

- **식별자**: [arXiv:1802.09568](https://arxiv.org/abs/1802.09568)
- **연도 / 저자·기관**: 2018 / Gupta et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Shampoo`, `preconditioning`
- **요약**: 텐서 구조를 활용한 전처리 기반 2차 계열 옵티마이저.

### 05-28. Symbolic Discovery of Optimization Algorithms

- **식별자**: [arXiv:2302.06675](https://arxiv.org/abs/2302.06675)
- **연도 / 저자·기관**: 2023 / Chen et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Lion`, `program-search`
- **요약**: 프로그램 탐색으로 발견한 옵티마이저 Lion(부호 기반, 모멘텀만 저장).

### 05-29. Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

- **식별자**: [arXiv:2305.14342](https://arxiv.org/abs/2305.14342)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Sophia`, `second-order`
- **요약**: 대각 헤시안 추정을 사용하는 확장 가능한 2차 옵티마이저.

### 05-30. The Road Less Scheduled

- **식별자**: [arXiv:2405.15682](https://arxiv.org/abs/2405.15682)
- **연도 / 저자·기관**: 2024 / Defazio et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `schedule-free`, `optimizer`
- **요약**: 학습률 스케줄 없이 학습할 수 있는 Schedule-Free 최적화.

### 05-31. GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection

- **식별자**: [arXiv:2403.03507](https://arxiv.org/abs/2403.03507)
- **연도 / 저자·기관**: 2024 / Zhao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GaLore`, `low-rank-gradient`
- **요약**: 기울기를 저랭크로 투영해 전체 파라미터 학습의 메모리를 줄이는 방법.

### 05-32. Muon is Scalable for LLM Training

- **식별자**: [arXiv:2502.16982](https://arxiv.org/abs/2502.16982)
- **연도 / 저자·기관**: 2025 / Liu et al. (Moonshot AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Muon`, `optimizer`, `Moonlight`
- **요약**: Muon에 가중치 감쇠와 층별 갱신 크기 조정을 더해 AdamW 대비 약 2배의 연산 효율을 보고. 3B/16B MoE ‘Moonlight’를 5.7T 토큰으로 학습.

### 05-33. Practical Efficiency of Muon for Pretraining

- **식별자**: [arXiv:2505.02222](https://arxiv.org/abs/2505.02222)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Muon`, `pretraining`
- **요약**: Muon의 사전학습 실용 효율을 다룬 연구(ID·제목만 확인).

### 05-34. Dion: Distributed Orthonormalized Updates

- **식별자**: [arXiv:2504.05295](https://arxiv.org/abs/2504.05295)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `orthonormal-updates`, `distributed`
- **요약**: 직교정규화 갱신의 분산 구현을 다룬 연구(ID·제목만 확인).
