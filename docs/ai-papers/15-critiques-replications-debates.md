# 15. 후속 비판 · 재현 · 쟁점 논문

앞선 문서의 주요 주장에 대해 재현을 시도하거나 반론·보완을 제시한 연구. 심층 분석(docs/ai-papers/deep-dives)에서 ‘이 결과를 얼마나 믿을 수 있는가’를 판단하는 근거로 쓰인다. 요약은 검색에서 확인된 범위로 한정했고, ‘ID·제목만 확인’이라고 적은 항목은 내용을 보지 못했다.

> 수록 50편 · 검증(V) 50편 · 기억기반(M) 0편

## 목차

- **스케일링 법칙의 재현 · 재검증** (3편)
  - 1. Chinchilla Scaling: A replication attempt (2024)
  - 2. Reconciling Kaplan and Chinchilla Scaling Laws (2024)
  - 3. Evaluating the Robustness of Chinchilla Compute-Optimal Scaling (2025)
- **추론 RL(RLVR)의 한계 · 범위 논쟁** (7편)
  - 4. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (2025)
  - 5. ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (2025)
  - 6. On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models (2025)
  - 7. Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning (2026)
  - 8. It's Not That Simple. An Analysis of Simple Test-Time Scaling (2025)
  - 9. Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities? (2025)
  - 10. Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms (2024)
- **소형 재귀 추론 모델 검증** (3편)
  - 11. Hierarchical Reasoning Models: Perspectives and Misconceptions (2025)
  - 12. Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models (2026)
  - 13. Dissecting Hierarchical Reasoning Models: A Mechanistic Study (2026)
- **테스트 시점 학습 · JEPA 계열 검증** (3편)
  - 14. Test-Time Training with KV Binding Is Secretly Linear Attention (2026)
  - 15. Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning (2024)
  - 16. LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures (2025)
- **안전 연구의 후속 · 반례** (4편)
  - 17. Why Do Some Language Models Fake Alignment While Others Don't? (2025)
  - 18. Natural emergent misalignment from reward hacking in production RL (2025)
  - 19. Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability (2025)
  - 20. Reasoning Models Struggle to Control their Chains of Thought (2026)
- **평가 · 자동 연구의 재검증** (2편)
  - 21. The Ideation–Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas (2025)
  - 22. HLE-Verified (제목 일부 생략) (2026)
- **에이전트 · 장기 과업 평가의 후속** (9편)
  - 23. Measuring AI Ability to Complete Long Tasks (v4 제목: …Long Software Tasks) (2025)
  - 24. Are AI Capabilities Increasing Exponentially? A Competing Hypothesis (2026)
  - 25. BRIDGE: Predicting Human Task Completion Time From Model Performance (2026)
  - 26. The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason (2025)
  - 27. SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (2025)
  - 28. Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025)
  - 29. SWE-bench Goes Live! (2025)
  - 30. VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks (2024)
  - 31. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation (2025)
- **잠재 추론 · 구조 후속 연구와 비판** (16편)
  - 32. Revealing and Mitigating the Local Pattern Shortcuts of Mamba (2024)
  - 33. The Illusion of Superposition? A Principled Analysis of … (제목 일부 생략) (2026)
  - 34. Reasoning by Superposition: A Theoretical … (제목 일부 생략) (2025)
  - 35. Continuous Chain of Thought Enables Parallel Exploration and Reasoning (2025)
  - 36. Capabilities and Fundamental Limits of Latent Chain-of-Thought (2026)
  - 37. Latent Chain-of-Thought? Decoding the Depth-Recurrent … (제목 일부 생략) (2025)
  - 38. Teaching Pretrained Language Models to Think Deeper with Retrofitted Recurrence (2025)
  - 39. A Mechanistic Analysis of Looped Reasoning Language Models (2026)
  - 40. A Survey on Latent Reasoning (2025)
  - 41. Jamba-1.5: Hybrid Transformer-Mamba Models at Scale (2024)
  - 42. VideoNSA: Native Sparse Attention Scales Video Understanding (2025)
  - 43. Flash Sparse Attention: An Alternative Efficient Implementation of Native Sparse Attention Kernel (2025)
  - 44. Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models (2024)
  - 45. MoMa: Efficient Early-Fusion Pre-training with Mixture of Modality-Aware Experts (2024)
  - 46. What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation (2024)
  - 47. Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence (2025)
- **합성 데이터 · 모델 붕괴 논쟁** (2편)
  - 48. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)
  - 49. Position: Model Collapse Does Not Mean What You Think (2025)
- **arXiv 외 분석 자료** (1편)
  - 50. The Hidden Drivers of HRM's Performance on ARC-AGI (2025)

## 스케일링 법칙의 재현 · 재검증

### 15-01. Chinchilla Scaling: A replication attempt

- **식별자**: [arXiv:2404.10102](https://arxiv.org/abs/2404.10102)
- **연도 / 저자·기관**: 2024 / Besiroglu, Erdil, Barnett, You (Epoch AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Chinchilla`, `replication`, `scaling-law`
- **요약**: Hoffmann et al.의 세 번째 접근(파라메트릭 손실 적합)을 논문 그림에서 복원한 데이터로 재현 시도. 보고된 추정치가 앞의 두 접근과 불일치하고 복원 데이터에 잘 맞지 않으며, 보고된 신뢰구간이 너무 좁아 60만 회 이상의 실험이 필요한 수준(원 연구는 500회 미만으로 추정)이라고 지적. 원인으로 손실 스케일 선택 때문에 옵티마이저가 수렴 전 멈춘 점과 본문 수치의 반올림을 꼽았고, 재유도한 결과는 앞의 두 접근과 부합한다.

### 15-02. Reconciling Kaplan and Chinchilla Scaling Laws

- **식별자**: [arXiv:2406.12907](https://arxiv.org/abs/2406.12907)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Kaplan`, `Chinchilla`, `reconciliation`
- **요약**: Kaplan과 Chinchilla가 서로 다른 최적 배분을 낸 이유를 조화시키려는 연구(ID·제목만 확인).

### 15-03. Evaluating the Robustness of Chinchilla Compute-Optimal Scaling

- **식별자**: [arXiv:2509.23963](https://arxiv.org/abs/2509.23963)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Chinchilla`, `robustness`
- **요약**: Chinchilla 연산 최적 스케일링의 견고성을 평가한 연구. 검색 결과상 Besiroglu 등의 적합 코드를 재사용하고 80% 구간을 보고한다.

## 추론 RL(RLVR)의 한계 · 범위 논쟁

### 15-04. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

- **식별자**: [arXiv:2504.13837](https://arxiv.org/abs/2504.13837)
- **연도 / 저자·기관**: 2025 / Yue et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLVR`, `pass@k`, `base-model`
- **요약**: RLVR로 학습한 모델이 작은 k(예: 1)에서는 기반 모델을 앞서지만 k가 크면 기반 모델의 pass@k가 더 높다고 보고하며, 관찰된 추론 능력이 기반 모델에서 비롯되고 그에 의해 한정된다고 결론.

### 15-05. ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models

- **식별자**: [arXiv:2505.24864](https://arxiv.org/abs/2505.24864)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLVR`, `prolonged-RL`
- **요약**: 회의적 결론이 방법론적 제약에서 비롯될 수 있다고 보며, 충분히 오래 RL을 하면 기반 모델에 없던 새로운 풀이 경로를 발견할 수 있다고 주장(검색 결과 기준).

### 15-06. On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models

- **식별자**: [arXiv:2512.07783](https://arxiv.org/abs/2512.07783)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLVR`, `mid-training`
- **요약**: 검색 결과 기준, 분포 내 과제에서 RL은 pass@128 기준으로 기반 모델을 넘지 못하지만 기반 모델의 역량을 벗어난 더 어려운 과제에서는 pass@128을 일관되게 개선한다고 보고.

### 15-07. Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning

- **식별자**: [arXiv:2605.06241](https://arxiv.org/abs/2605.06241)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `RLVR`, `policy-selection`
- **요약**: RL이 새 능력을 학습하기보다 희소한 정책 선택을 한다는 관점의 2026년 연구(ID·제목만 확인).

### 15-08. It's Not That Simple. An Analysis of Simple Test-Time Scaling

- **식별자**: [arXiv:2507.14419](https://arxiv.org/abs/2507.14419)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `test-time-scaling`, `s1`, `analysis`
- **요약**: s1의 단순 테스트 시점 스케일링을 분석한 연구(ID·제목만 확인).

### 15-09. Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?

- **식별자**: [arXiv:2502.12215](https://arxiv.org/abs/2502.12215)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `test-time-scaling`, `o1-like`
- **요약**: o1류 모델이 실제로 테스트 시점 스케일링 능력을 갖는지 되묻는 연구(ID·제목만 확인).

### 15-10. Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms

- **식별자**: [arXiv:2406.02900](https://arxiv.org/abs/2406.02900)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `reward-overoptimization`, `DPO`, `scaling-law`
- **요약**: 명시적 프록시 보상 모델이 없는 직접 정렬 알고리즘으로 Gao et al.의 보상 과최적화 분석을 확장하고, GPT-4 승률을 골드 보상의 대용으로 사용.

## 소형 재귀 추론 모델 검증

### 15-11. Hierarchical Reasoning Models: Perspectives and Misconceptions

- **식별자**: [arXiv:2510.00355](https://arxiv.org/abs/2510.00355)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `HRM`, `critique`, `Sudoku`, `Maze`
- **요약**: 원 HRM의 설계 선택을 비판적으로 검토하고 Sudoku-Extreme·Maze-Hard에서 기존 보고치를 넘는 변형을 제시. v1 제목은 ‘A Critical Supplementary Material’이었다.

### 15-12. Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models

- **식별자**: [arXiv:2601.10679](https://arxiv.org/abs/2601.10679)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `HRM`, `mechanistic`
- **요약**: HRM이 실제로 추론하는지 추측하는지를 기계적으로 분석한 2026년 연구(ID·제목만 확인).

### 15-13. Dissecting Hierarchical Reasoning Models: A Mechanistic Study

- **식별자**: [arXiv:2609.22197](https://arxiv.org/abs/2609.22197)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `HRM`, `mechanistic`
- **요약**: 검색 결과상 HRM이 퍼즐별 해 상태를 반복적으로 정제한다고 논증하는 기계적 연구.

## 테스트 시점 학습 · JEPA 계열 검증

### 15-14. Test-Time Training with KV Binding Is Secretly Linear Attention

- **식별자**: [arXiv:2602.21204](https://arxiv.org/abs/2602.21204)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `TTT`, `linear-attention`, `equivalence`
- **요약**: KV 결합 방식의 테스트 시점 학습이 사실상 선형 어텐션이라는 재해석(제목 기준, 본문 미검토).

### 15-15. Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning

- **식별자**: [arXiv:2410.19560](https://arxiv.org/abs/2410.19560)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `JEPA`, `contrastive`
- **요약**: I-JEPA를 대조 학습과 연결하며, 붕괴 방지와 평균 패치 표현 측면의 한계를 지적(검색 결과 기준).

### 15-16. LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures

- **식별자**: [arXiv:2509.14252](https://arxiv.org/abs/2509.14252)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `JEPA`, `LLM`
- **요약**: JEPA 목표를 언어모델에 적용하려는 2025년 연구(ID·제목만 확인).

## 안전 연구의 후속 · 반례

### 15-17. Why Do Some Language Models Fake Alignment While Others Don't?

- **식별자**: [arXiv:2506.18032](https://arxiv.org/abs/2506.18032)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `alignment-faking`, `model-comparison`
- **요약**: 모델에 따라 정렬 위장이 나타나는 정도가 다른 이유를 다룬 2025년 연구(ID·제목만 확인).

### 15-18. Natural emergent misalignment from reward hacking in production RL

- **식별자**: [arXiv:2511.18397](https://arxiv.org/abs/2511.18397)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `emergent-misalignment`, `reward-hacking`
- **요약**: 상용 규모 RL에서 보상 해킹으로부터 자연스럽게 나타나는 창발적 오정렬을 다룬 2025년 연구(ID·제목만 확인).

### 15-19. Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability

- **식별자**: [arXiv:2510.19851](https://arxiv.org/abs/2510.19851)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `CoT-monitoring`, `obfuscation`
- **요약**: 추론 모델이 추론을 난독화할 수 있는지 사고 사슬 모니터링을 압박 시험한 연구(ID·제목만 확인).

### 15-20. Reasoning Models Struggle to Control their Chains of Thought

- **식별자**: [arXiv:2603.05706](https://arxiv.org/abs/2603.05706)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `CoT-controllability`
- **요약**: 추론 모델이 자신의 사고 사슬을 통제하기 어렵다는 2026년 연구(ID·제목만 확인).

## 평가 · 자동 연구의 재검증

### 15-21. The Ideation–Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas

- **식별자**: [arXiv:2506.20803](https://arxiv.org/abs/2506.20803)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `research-ideation`, `execution`
- **요약**: 43명의 전문가가 아이디어를 실제로 실행해 본 후속 연구. 실행 후 LLM 아이디어의 평가 점수가 사람 아이디어보다 더 크게 하락해 아이디어 단계의 격차가 사라졌다고 보고.

### 15-22. HLE-Verified (제목 일부 생략)

- **식별자**: [arXiv:2602.13964](https://arxiv.org/abs/2602.13964)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `HLE`, `verification`
- **요약**: Humanity's Last Exam에 문제 있는 문항이 상당수 있다는 커뮤니티 분석에 대응해 검증·개정 작업을 보고(검색 결과 기준, 정식 제목 일부 확인 못함).

## 에이전트 · 장기 과업 평가의 후속

### 15-23. Measuring AI Ability to Complete Long Tasks (v4 제목: …Long Software Tasks)

- **식별자**: [arXiv:2503.14499](https://arxiv.org/abs/2503.14499)
- **연도 / 저자·기관**: 2025 / Kwa et al. (METR)
- **검증 상태**: ✅ 검증(V)
- **태그**: `time-horizon`, `METR`, `long-horizon`
- **요약**: 사람 전문가가 걸리는 시간으로 과제 길이를 재고, 모델이 50% 성공률로 완수하는 과제 길이(50% 시간 지평)를 약 170개 과제에 로지스틱 모델로 적합. 2019–2025년 시간 지평이 지수적으로 증가했고 배가 시간은 약 7개월, 2023–2025는 약 20% 더 빠르다고 보고. 개정판에 따라 Claude 3.7 Sonnet 약 50분(v2) → o3 약 110분(v4). 소프트웨어·연구 과제에 한정된 측정이다.

### 15-24. Are AI Capabilities Increasing Exponentially? A Competing Hypothesis

- **식별자**: [arXiv:2602.04836](https://arxiv.org/abs/2602.04836)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `time-horizon`, `critique`
- **요약**: 시간 지평의 지수 증가 해석에 대한 대안 가설을 제시한 2026년 연구(ID·제목만 확인).

### 15-25. BRIDGE: Predicting Human Task Completion Time From Model Performance

- **식별자**: [arXiv:2602.07267](https://arxiv.org/abs/2602.07267)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `time-horizon`, `human-time`
- **요약**: 사람 소요 시간을 모델 성능으로 예측해 시간 지평 방식의 주석 비용 문제를 줄이려는 연구(검색 결과 기준).

### 15-26. The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason

- **식별자**: [arXiv:2506.12286](https://arxiv.org/abs/2506.12286)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `SWE-bench`, `memorization`, `contamination`
- **요약**: SWE-bench 성능이 추론이 아니라 암기를 반영할 수 있다는 문제를 제기한 연구(ID·제목만 확인).

### 15-27. SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

- **식별자**: [arXiv:2509.16941](https://arxiv.org/abs/2509.16941)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `SWE-bench`, `long-horizon`
- **요약**: 더 긴 호흡의 소프트웨어 엔지니어링 과제를 다루는 SWE-bench 계열 확장(ID·제목만 확인).

### 15-28. Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving

- **식별자**: [arXiv:2504.02605](https://arxiv.org/abs/2504.02605)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `SWE-bench`, `multilingual`
- **요약**: 다국어 이슈 해결 벤치마크(ID·제목만 확인).

### 15-29. SWE-bench Goes Live!

- **식별자**: [arXiv:2505.23419](https://arxiv.org/abs/2505.23419)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `SWE-bench`, `live`, `contamination`
- **요약**: 오염을 줄이기 위해 지속 갱신되는 SWE-bench 변형(ID·제목만 확인).

### 15-30. VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks

- **식별자**: [arXiv:2401.13649](https://arxiv.org/abs/2401.13649)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `web-agents`, `multimodal`
- **요약**: 시각 접지가 필요한 웹 과제로 WebArena를 확장(ID·제목만 확인).

### 15-31. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

- **식별자**: [arXiv:2510.11977](https://arxiv.org/abs/2510.11977)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `agent-evaluation`, `leaderboard`
- **요약**: 에이전트 평가 인프라를 다룬 2025년 연구(ID·제목만 확인).

## 잠재 추론 · 구조 후속 연구와 비판

### 15-32. Revealing and Mitigating the Local Pattern Shortcuts of Mamba

- **식별자**: [arXiv:2410.15678](https://arxiv.org/abs/2410.15678)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mamba`, `recall`, `shortcut`
- **요약**: Mamba의 선택 메커니즘이 회상 과제에서 국소 패턴 지름길을 만들 수 있으며 이는 제약된 Δ 파라미터와 관련된다고 지적(검색 결과 기준).

### 15-33. The Illusion of Superposition? A Principled Analysis of … (제목 일부 생략)

- **식별자**: [arXiv:2604.06374](https://arxiv.org/abs/2604.06374)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Coconut`, `superposition`, `critique`
- **요약**: Coconut의 ‘너비 우선 탐색/중첩’ 해석에 이의를 제기. 개체 수준 탐침으로 보면 모델이 잠재 토큰 없이도 질문 표현에서 직접 답을 추출하며, 같은 분석을 처음부터 학습한 모델에 적용하면 중첩 활용 징후가 나타난다고 보고(검색 결과 기준).

### 15-34. Reasoning by Superposition: A Theoretical … (제목 일부 생략)

- **식별자**: [arXiv:2505.12514](https://arxiv.org/abs/2505.12514)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `continuous-CoT`, `superposition`, `theory`
- **요약**: 연속 사고가 여러 탐색 경로를 중첩 상태로 유지한다는 이론적 논증(검색 결과 기준).

### 15-35. Continuous Chain of Thought Enables Parallel Exploration and Reasoning

- **식별자**: [arXiv:2505.23648](https://arxiv.org/abs/2505.23648)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `continuous-CoT`, `CoT2`
- **요약**: 연속 CoT가 병렬 탐색을 가능케 한다는 연구(ProsQA·ProntoQA류 탐색 과제에서 활용, 검색 결과 기준).

### 15-36. Capabilities and Fundamental Limits of Latent Chain-of-Thought

- **식별자**: [arXiv:2602.01148](https://arxiv.org/abs/2602.01148)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `latent-CoT`, `limits`
- **요약**: 잠재 CoT는 유연한 추론에는 강하나 정밀 계산에는 약하고 학습 커리큘럼에 민감하다는 취지로 인용되는 연구(검색 결과 기준).

### 15-37. Latent Chain-of-Thought? Decoding the Depth-Recurrent … (제목 일부 생략)

- **식별자**: [arXiv:2507.02199](https://arxiv.org/abs/2507.02199)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `depth-recurrence`, `analysis`
- **요약**: 깊이 순환 모델 분석. 순환 깊이를 늘려도 이득이 미미하고 추론 단계를 외부로 드러내는 모델에 크게 못 미친다고 인용된다(검색 결과 기준).

### 15-38. Teaching Pretrained Language Models to Think Deeper with Retrofitted Recurrence

- **식별자**: [arXiv:2511.07384](https://arxiv.org/abs/2511.07384)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `retrofitted-recurrence`
- **요약**: 사전학습 모델의 앞 층을 prelude로, 뒤 층을 순환 블록·coda로 개조하는 방법을 다룬 연구(검색 결과 기준).

### 15-39. A Mechanistic Analysis of Looped Reasoning Language Models

- **식별자**: [arXiv:2604.11791](https://arxiv.org/abs/2604.11791)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `looped-LM`, `mechanistic`
- **요약**: 루프 구조 추론 모델의 기계적 분석. 고정점에 도달하지 못한 모델은 학습하지 않은 순환 깊이에서 불안정해진다는 취지로 인용된다(검색 결과 기준).

### 15-40. A Survey on Latent Reasoning

- **식별자**: [arXiv:2507.06203](https://arxiv.org/abs/2507.06203)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `latent-reasoning`, `survey`
- **요약**: 잠재 추론 서베이(ID·제목만 확인).

### 15-41. Jamba-1.5: Hybrid Transformer-Mamba Models at Scale

- **식별자**: [arXiv:2408.12570](https://arxiv.org/abs/2408.12570)
- **연도 / 저자·기관**: 2024 / Jamba Team (AI21)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Jamba`, `hybrid`, `scale`
- **요약**: Jamba-1.5-Mini는 총 52B·활성 12B, Jamba-1.5-Large는 총 398B·활성 94B 파라미터(검색 결과 기준).

### 15-42. VideoNSA: Native Sparse Attention Scales Video Understanding

- **식별자**: [arXiv:2510.02295](https://arxiv.org/abs/2510.02295)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `NSA`, `video`
- **요약**: NSA의 3가지 가지 설계를 비디오에 적용. 게이트 분석에서 압축 가지가 모든 층에서 지배적이라고 보고(검색 결과 기준).

### 15-43. Flash Sparse Attention: An Alternative Efficient Implementation of Native Sparse Attention Kernel

- **식별자**: [arXiv:2508.18224](https://arxiv.org/abs/2508.18224)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `NSA`, `kernel`
- **요약**: NSA 커널의 대안 구현. 선택 어텐션 단계가 어텐션 오버헤드의 평균 약 65%를 차지한다고 보고(검색 결과 기준).

### 15-44. Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models

- **식별자**: [arXiv:2411.04996](https://arxiv.org/abs/2411.04996)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoT`, `multimodal`, `modality-sparsity`
- **요약**: FFN·어텐션 행렬·LayerNorm을 모달리티별로 분리하되 어텐션은 전역으로 유지. 연산 구조와 FLOP는 dense와 같고, Chameleon 7B 설정에서 텍스트·이미지 성능을 55.8% FLOP로 맞추고 음성 추가 시 37.2%, Transfusion 설정에서 이미지 성능을 1/3 FLOP로 맞춘다고 보고(TMLR 2025).

### 15-45. MoMa: Efficient Early-Fusion Pre-training with Mixture of Modality-Aware Experts

- **식별자**: [arXiv:2407.21770](https://arxiv.org/abs/2407.21770)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoMa`, `early-fusion`, `MoE`
- **요약**: Chameleon류 초기 융합 모델에 모달리티 인식 전문가를 적용. 복잡도 통제 실험에서 총 FLOP를 최대 3.7배 줄인다고 보고(검색 결과 기준).

### 15-46. What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation

- **식별자**: [arXiv:2404.07129](https://arxiv.org/abs/2404.07129)
- **연도 / 저자·기관**: 2024 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `induction-heads`, `training-dynamics`
- **요약**: 활성화 클램핑으로 유도 헤드 형성의 불연속적 도약을 만드는 세 하위 회로를 식별(검색 결과 기준).

### 15-47. Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence

- **식별자**: [arXiv:2505.16694](https://arxiv.org/abs/2505.16694)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `induction-heads`, `meta-learning`
- **요약**: 유도 헤드 설명은 답이 문맥에 이미 있을 때만 ICL을 설명하며, 메타 학습 설정에서는 여러 단계에서 각기 다른 회로가 나타난다고 주장(검색 결과 기준).

## 합성 데이터 · 모델 붕괴 논쟁

### 15-48. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data

- **식별자**: [arXiv:2404.01413](https://arxiv.org/abs/2404.01413)
- **연도 / 저자·기관**: 2024 / Gerstgrasser et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `model-collapse`, `synthetic-data`
- **요약**: 합성 데이터로 실제 데이터를 대체하지 않고 실제 데이터와 함께 누적하면 붕괴를 피할 수 있다고 주장해 ‘붕괴의 불가피성’에 반론(검색 결과 기준).

### 15-49. Position: Model Collapse Does Not Mean What You Think

- **식별자**: [arXiv:2503.03150](https://arxiv.org/abs/2503.03150)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `model-collapse`, `position`
- **요약**: ‘모델 붕괴’ 개념이 흔히 오해된다는 입장 논문(ID·제목만 확인).

## arXiv 외 분석 자료

### 15-50. The Hidden Drivers of HRM's Performance on ARC-AGI

- **식별자**: [링크](https://arcprize.org/blog/hrm-analysis)
- **연도 / 저자·기관**: 2025 / ARC Prize 팀
- **검증 상태**: ✅ 검증(V)
- **태그**: `HRM`, `ARC-AGI`, `ablation`
- **요약**: HRM 주장치를 대략 재현(ARC-AGI-1 준공개(Semi-Private) 세트 32%, ARC-AGI-2 2%)한 뒤 절제 실험으로 계층 구조의 기여가 작음(비슷한 크기 Transformer로 바꿔도 성능 차이 미미), 학습 중 외부 반복 정제 루프가 주된 동인이고, 과제 간 전이는 제한적이며 대부분의 점수는 평가 시점 과제의 해답 암기에서 나왔다고 결론(블로그, 2025-08-15).
