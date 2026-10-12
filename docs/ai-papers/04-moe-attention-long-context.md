# 04. 전문가 혼합(MoE) · 효율적 어텐션 · 장문 컨텍스트

활성 파라미터를 줄이는 희소 모델, 어텐션 연산·메모리를 줄이는 알고리즘과 하드웨어 최적화, 위치 인코딩 확장을 통한 긴 컨텍스트 처리 기술.

> 수록 36편 · 검증(V) 10편 · 기억기반(M) 26편

## 목차

- **전문가 혼합(MoE)** (9편)
  - 1. Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer (2017)
  - 2. GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding (2020)
  - 3. Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity (2021)
  - 4. ST-MoE: Designing Stable and Transferable Sparse Expert Models (2022)
  - 5. Mixture-of-Experts with Expert Choice Routing (2022)
  - 6. Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models (2023)
  - 7. DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models (2024)
  - 8. Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts (2024)
  - 9. OLMoE: Open Mixture-of-Experts Language Models (2024)
- **효율적 어텐션 알고리즘·하드웨어 최적화** (9편)
  - 10. Fast Transformer Decoding: One Write-Head is All You Need (2019)
  - 11. GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints (2023)
  - 12. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (2022)
  - 13. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning (2023)
  - 14. FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision (2024)
  - 15. Efficient Memory Management for Large Language Model Serving with PagedAttention (2023)
  - 16. Ring Attention with Blockwise Transformers for Near-Infinite Context (2023)
  - 17. Efficient Streaming Language Models with Attention Sinks (2023)
  - 18. Efficient Transformers: A Survey (2020)
- **희소·선형 근사 어텐션** (8편)
  - 19. Reformer: The Efficient Transformer (2020)
  - 20. Longformer: The Long-Document Transformer (2020)
  - 21. Linformer: Self-Attention with Linear Complexity (2020)
  - 22. Big Bird: Transformers for Longer Sequences (2020)
  - 23. Rethinking Attention with Performers (2020)
  - 24. LongNet: Scaling Transformers to 1,000,000,000 Tokens (2023)
  - 25. Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention (2025)
  - 26. MoBA: Mixture of Block Attention for Long-Context LLMs (2025)
- **위치 인코딩과 컨텍스트 확장** (7편)
  - 27. RoFormer: Enhanced Transformer with Rotary Position Embedding (2021)
  - 28. Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation (2021)
  - 29. Extending Context Window of Large Language Models via Positional Interpolation (2023)
  - 30. YaRN: Efficient Context Window Extension of Large Language Models (2023)
  - 31. LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens (2024)
  - 32. Qwen2.5-1M Technical Report (2025)
  - 33. A Comprehensive Survey on Long Context Language Modeling (2025)
- **장문 평가** (3편)
  - 34. Lost in the Middle: How Language Models Use Long Contexts (2023)
  - 35. RULER: What's the Real Context Size of Your Long-Context Language Models? (2024)
  - 36. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding (2023)

## 전문가 혼합(MoE)

### 04-01. Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

- **식별자**: [arXiv:1701.06538](https://arxiv.org/abs/1701.06538)
- **연도 / 저자·기관**: 2017 / Shazeer et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MoE`, `sparse-gating`
- **요약**: 희소 게이팅 MoE 층을 LSTM에 적용해 연산량 증가 없이 파라미터를 1000배 이상 늘릴 수 있음을 보인 현대 MoE의 출발점.

### 04-02. GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

- **식별자**: [arXiv:2006.16668](https://arxiv.org/abs/2006.16668)
- **연도 / 저자·기관**: 2020 / Lepikhin et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MoE`, `sharding`, `translation`
- **요약**: MoE Transformer를 자동 샤딩으로 6000억 파라미터까지 확장해 다국어 번역에 적용.

### 04-03. Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

- **식별자**: [arXiv:2101.03961](https://arxiv.org/abs/2101.03961)
- **연도 / 저자·기관**: 2021 / Fedus et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Switch`, `top-1-routing`
- **요약**: 토큰당 전문가 1개만 선택(top-1)하는 단순화된 라우팅으로 안정성과 효율을 높여 조 단위 파라미터까지 확장.

### 04-04. ST-MoE: Designing Stable and Transferable Sparse Expert Models

- **식별자**: [arXiv:2202.08906](https://arxiv.org/abs/2202.08906)
- **연도 / 저자·기관**: 2022 / Zoph et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MoE`, `stability`, `router-z-loss`
- **요약**: MoE 학습 불안정을 줄이는 라우터 z-loss 등 설계 지침과 전이 성능 분석.

### 04-05. Mixture-of-Experts with Expert Choice Routing

- **식별자**: [arXiv:2202.09368](https://arxiv.org/abs/2202.09368)
- **연도 / 저자·기관**: 2022 / Zhou et al. (Google)
- **검증 상태**: ✅ 검증(V)
- **태그**: `expert-choice`, `load-balancing`
- **요약**: 토큰이 전문가를 고르는 대신 전문가가 토큰을 고르게 해 부하 균형을 자동으로 맞추는 라우팅.

### 04-06. Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models

- **식별자**: [arXiv:2305.14705](https://arxiv.org/abs/2305.14705)
- **연도 / 저자·기관**: 2023 / Shen et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoE`, `instruction-tuning`
- **요약**: MoE 모델이 dense 모델보다 지시 튜닝으로 더 크게 이득을 본다는 실험 결과.

### 04-07. DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

- **식별자**: [arXiv:2401.06066](https://arxiv.org/abs/2401.06066)
- **연도 / 저자·기관**: 2024 / Dai et al. (DeepSeek)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DeepSeekMoE`, `fine-grained-experts`, `shared-experts`
- **요약**: 전문가를 세분화하고 일부를 공유 전문가로 분리해 전문화를 높이는 MoE 설계.

### 04-08. Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts

- **식별자**: [arXiv:2408.15664](https://arxiv.org/abs/2408.15664)
- **연도 / 저자·기관**: 2024 / Wang et al. (DeepSeek)
- **검증 상태**: ✅ 검증(V)
- **태그**: `load-balancing`, `bias-routing`
- **요약**: 보조 손실의 간섭 기울기 없이, 전문가별 편향을 사용 빈도에 따라 조정해 부하를 균형화(1B·3B MoE 실험에서 기존 방식보다 성능·균형 모두 우수).

### 04-09. OLMoE: Open Mixture-of-Experts Language Models

- **식별자**: [arXiv:2409.02060](https://arxiv.org/abs/2409.02060)
- **연도 / 저자·기관**: 2024 / Muennighoff et al. (AI2)
- **검증 상태**: ✅ 검증(V)
- **태그**: `OLMoE`, `open-MoE`
- **요약**: 총 7B·활성 약 1B의 완전 개방형 MoE. 5조 토큰으로 사전학습하고 가중치·데이터·코드·로그를 모두 공개.

## 효율적 어텐션 알고리즘·하드웨어 최적화

### 04-10. Fast Transformer Decoding: One Write-Head is All You Need

- **식별자**: [arXiv:1911.02150](https://arxiv.org/abs/1911.02150)
- **연도 / 저자·기관**: 2019 / Shazeer (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MQA`, `decoding`, `KV-cache`
- **요약**: 모든 헤드가 하나의 키·값을 공유하는 Multi-Query Attention으로 디코딩 시 메모리 대역폭 부담을 줄임.

### 04-11. GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

- **식별자**: [arXiv:2305.13245](https://arxiv.org/abs/2305.13245)
- **연도 / 저자·기관**: 2023 / Ainslie et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GQA`, `KV-cache`
- **요약**: MHA와 MQA 사이의 그룹 질의 어텐션. 기존 MHA 체크포인트를 적은 추가 학습으로 변환 가능해 널리 채택됐다.

### 04-12. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

- **식별자**: [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)
- **연도 / 저자·기관**: 2022 / Dao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FlashAttention`, `IO-aware`, `tiling`
- **요약**: GPU 메모리 계층(IO)을 고려한 타일링으로 정확한 어텐션을 더 빠르고 메모리 효율적으로 계산.

### 04-13. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

- **식별자**: [arXiv:2307.08691](https://arxiv.org/abs/2307.08691)
- **연도 / 저자·기관**: 2023 / Dao
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FlashAttention-2`, `GPU`
- **요약**: 작업 분할과 병렬화를 개선해 FlashAttention보다 약 2배 빠르게 만든 후속 구현.

### 04-14. FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

- **식별자**: [arXiv:2407.08608](https://arxiv.org/abs/2407.08608)
- **연도 / 저자·기관**: 2024 / Shah et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FlashAttention-3`, `Hopper`, `FP8`
- **요약**: Hopper GPU의 비동기 실행과 저정밀(FP8)을 활용한 최적화.

### 04-15. Efficient Memory Management for Large Language Model Serving with PagedAttention

- **식별자**: [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
- **연도 / 저자·기관**: 2023 / Kwon et al. (UC Berkeley)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `vLLM`, `PagedAttention`, `serving`
- **요약**: KV 캐시를 OS의 가상 메모리 페이징처럼 관리해 낭비를 줄이는 vLLM의 핵심 기법.

### 04-16. Ring Attention with Blockwise Transformers for Near-Infinite Context

- **식별자**: [arXiv:2310.01889](https://arxiv.org/abs/2310.01889)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Ring-Attention`, `distributed`, `long-context`
- **요약**: 블록 단위 계산과 장치 간 링 통신을 겹쳐 시퀀스 길이를 장치 수에 비례해 확장.

### 04-17. Efficient Streaming Language Models with Attention Sinks

- **식별자**: [arXiv:2309.17453](https://arxiv.org/abs/2309.17453)
- **연도 / 저자·기관**: 2023 / Xiao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `StreamingLLM`, `attention-sink`
- **요약**: 초기 몇 개 토큰이 ‘어텐션 싱크’ 역할을 한다는 관찰로, 유한 캐시만으로 무한 길이 스트리밍 생성을 가능하게 한 방법.

### 04-18. Efficient Transformers: A Survey

- **식별자**: [arXiv:2009.06732](https://arxiv.org/abs/2009.06732)
- **연도 / 저자·기관**: 2020 / Tay et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `survey`, `efficient-attention`
- **요약**: 효율적 Transformer 변형들을 분류·정리한 서베이.

## 희소·선형 근사 어텐션

### 04-19. Reformer: The Efficient Transformer

- **식별자**: [arXiv:2001.04451](https://arxiv.org/abs/2001.04451)
- **연도 / 저자·기관**: 2020 / Kitaev et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LSH-attention`, `reversible`
- **요약**: LSH 어텐션과 가역 층으로 긴 시퀀스의 메모리를 줄인 구조.

### 04-20. Longformer: The Long-Document Transformer

- **식별자**: [arXiv:2004.05150](https://arxiv.org/abs/2004.05150)
- **연도 / 저자·기관**: 2020 / Beltagy et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `sliding-window`, `global-attention`
- **요약**: 슬라이딩 윈도와 일부 전역 토큰을 조합한 선형 비용 어텐션.

### 04-21. Linformer: Self-Attention with Linear Complexity

- **식별자**: [arXiv:2006.04768](https://arxiv.org/abs/2006.04768)
- **연도 / 저자·기관**: 2020 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `low-rank`, `linear-attention`
- **요약**: 어텐션 행렬이 저랭크임을 이용해 키·값을 투영 압축.

### 04-22. Big Bird: Transformers for Longer Sequences

- **식별자**: [arXiv:2007.14062](https://arxiv.org/abs/2007.14062)
- **연도 / 저자·기관**: 2020 / Zaheer et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `sparse-attention`
- **요약**: 랜덤·윈도·전역 어텐션을 결합한 희소 어텐션과 이론적 표현력 분석.

### 04-23. Rethinking Attention with Performers

- **식별자**: [arXiv:2009.14794](https://arxiv.org/abs/2009.14794)
- **연도 / 저자·기관**: 2020 / Choromanski et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FAVOR+`, `linear-attention`
- **요약**: 랜덤 특성으로 소프트맥스 어텐션을 선형 시간에 근사(FAVOR+).

### 04-24. LongNet: Scaling Transformers to 1,000,000,000 Tokens

- **식별자**: [arXiv:2307.02486](https://arxiv.org/abs/2307.02486)
- **연도 / 저자·기관**: 2023 / Ding et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `dilated-attention`, `long-context`
- **요약**: 확장(dilated) 어텐션으로 이론상 10억 토큰까지 선형 비용을 주장한 구조.

### 04-25. Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

- **식별자**: [arXiv:2502.11089](https://arxiv.org/abs/2502.11089)
- **연도 / 저자·기관**: 2025 / Yuan et al. (DeepSeek)
- **검증 상태**: ✅ 검증(V)
- **태그**: `NSA`, `sparse-attention`, `hardware-aligned`
- **요약**: 거친 토큰 압축과 정밀 토큰 선택을 결합한 희소 어텐션. 하드웨어 정렬 커널과 종단간 학습 가능성으로 사전학습 연산도 줄인다(ACL 2025).

### 04-26. MoBA: Mixture of Block Attention for Long-Context LLMs

- **식별자**: [arXiv:2502.13189](https://arxiv.org/abs/2502.13189)
- **연도 / 저자·기관**: 2025 / Lu et al. (Moonshot AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoBA`, `block-attention`, `MoE-style`
- **요약**: 어텐션에 MoE식 게이팅을 적용해 질의가 관련 블록만 고르게 하는 ‘적은 구조’ 원칙의 장문 어텐션.

## 위치 인코딩과 컨텍스트 확장

### 04-27. RoFormer: Enhanced Transformer with Rotary Position Embedding

- **식별자**: [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)
- **연도 / 저자·기관**: 2021 / Su et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RoPE`, `positional-encoding`
- **요약**: 위치를 회전 행렬로 인코딩해 상대 위치 정보를 자연스럽게 반영하는 RoPE. 현대 LLM의 사실상 표준.

### 04-28. Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

- **식별자**: [arXiv:2108.12409](https://arxiv.org/abs/2108.12409)
- **연도 / 저자·기관**: 2021 / Press et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ALiBi`, `length-extrapolation`
- **요약**: 거리에 비례한 선형 편향으로 학습 길이보다 긴 입력에 외삽하는 ALiBi.

### 04-29. Extending Context Window of Large Language Models via Positional Interpolation

- **식별자**: [arXiv:2306.15595](https://arxiv.org/abs/2306.15595)
- **연도 / 저자·기관**: 2023 / Chen et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `position-interpolation`, `RoPE`
- **요약**: RoPE 위치를 보간해 짧은 추가 미세조정만으로 컨텍스트 창을 확장.

### 04-30. YaRN: Efficient Context Window Extension of Large Language Models

- **식별자**: [arXiv:2309.00071](https://arxiv.org/abs/2309.00071)
- **연도 / 저자·기관**: 2023 / Peng et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `YaRN`, `RoPE-scaling`
- **요약**: 주파수별로 보간 정도를 달리하는 RoPE 확장 기법.

### 04-31. LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

- **식별자**: [arXiv:2402.13753](https://arxiv.org/abs/2402.13753)
- **연도 / 저자·기관**: 2024 / Ding et al. (Microsoft)
- **검증 상태**: ✅ 검증(V)
- **태그**: `LongRoPE`, `context-extension`
- **요약**: RoPE의 비균일 재조정 탐색과 점진적 2단계 확장으로 약 1천 스텝 미세조정만에 2048k 토큰까지 확장(LLaMA2·Mistral 실험).

### 04-32. Qwen2.5-1M Technical Report

- **식별자**: [arXiv:2501.15383](https://arxiv.org/abs/2501.15383)
- **연도 / 저자·기관**: 2025 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen2.5-1M`, `long-context`
- **요약**: Qwen2.5를 100만 토큰 컨텍스트로 확장한 기술 보고서(ID·제목만 확인).

### 04-33. A Comprehensive Survey on Long Context Language Modeling

- **식별자**: [arXiv:2503.17407](https://arxiv.org/abs/2503.17407)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `survey`, `long-context`
- **요약**: 장문 컨텍스트 언어모델링 전반을 다룬 서베이(ID·제목만 확인).

## 장문 평가

### 04-34. Lost in the Middle: How Language Models Use Long Contexts

- **식별자**: [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `long-context`, `position-bias`
- **요약**: 관련 정보가 문맥 중간에 있을 때 성능이 크게 떨어지는 U자 패턴을 보인 분석.

### 04-35. RULER: What's the Real Context Size of Your Long-Context Language Models?

- **식별자**: [arXiv:2404.06654](https://arxiv.org/abs/2404.06654)
- **연도 / 저자·기관**: 2024 / Hsieh et al. (NVIDIA)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RULER`, `long-context-eval`
- **요약**: 단순 needle 검색을 넘어 다중 키·추적·집계 과제를 포함한 합성 장문 벤치마크. ‘주장된’ 컨텍스트 길이보다 실효 길이가 짧은 모델이 많음을 보였다.

### 04-36. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

- **식별자**: [arXiv:2308.14508](https://arxiv.org/abs/2308.14508)
- **연도 / 저자·기관**: 2023 / Bai et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `LongBench`, `benchmark`
- **요약**: 이중언어·다과업 장문 이해 벤치마크.
