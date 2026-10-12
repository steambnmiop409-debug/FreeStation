# 15. 후속 비판 · 재현 · 쟁점 논문

앞선 문서의 주요 주장에 대해 재현을 시도하거나 반론·보완을 제시한 연구. 심층 분석(docs/ai-papers/deep-dives)에서 ‘이 결과를 얼마나 믿을 수 있는가’를 판단하는 근거로 쓰인다. 요약은 검색에서 확인된 범위로 한정했고, ‘ID·제목만 확인’이라고 적은 항목은 내용을 보지 못했다.

> 수록 22편 · 검증(V) 22편 · 기억기반(M) 0편

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
