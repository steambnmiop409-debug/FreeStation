# 14. 이론 · 실험적 패러다임 · 비표준 구조

일반화 이론, 문맥 내 학습의 이론적 해석, 생물학·물리학에서 영감을 받은 신경망, 비표준 학습 알고리즘, 모델 병합, 작은 재귀 추론 모델처럼 주류 스케일링 노선 밖의 실험적 시도.

> 수록 32편 · 검증(V) 4편 · 기억기반(M) 28편

## 목차

- **학습·일반화 이론과 현상** (7편)
  - 1. Neural Tangent Kernel: Convergence and Generalization in Neural Networks (2018)
  - 2. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks (2018)
  - 3. Deep Double Descent: Where Bigger Models and More Data Hurt (2019)
  - 4. Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets (2022)
  - 5. What Can Transformers Learn In-Context? A Case Study of Simple Function Classes (2022)
  - 6. Transformers learn in-context by gradient descent (2022)
  - 7. Why Can GPT Learn In-Context? Language Models Implicitly Perform Gradient Descent as Meta-Optimizers (2022)
- **생물·물리에서 영감을 받은 신경망** (13편)
  - 8. Neural Turing Machines (2014)
  - 9. HyperNetworks (2016)
  - 10. Dynamic Routing Between Capsules (2017)
  - 11. Neural Ordinary Differential Equations (2018)
  - 12. Deep Equilibrium Models (2019)
  - 13. Liquid Time-constant Networks (2020)
  - 14. Closed-form Continuous-time Neural Models (2021)
  - 15. Hopfield Networks is All You Need (2020)
  - 16. The Forward-Forward Algorithm: Some Preliminary Investigations (2022)
  - 17. Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation (2021)
  - 18. Spikformer: When Spiking Neural Network Meets Transformer (2022)
  - 19. SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks (2023)
  - 20. KAN: Kolmogorov-Arnold Networks (2024)
- **메타 학습 · 생성 모델의 고전 · 탐색** (5편)
  - 21. Generative Adversarial Networks (2014)
  - 22. Auto-Encoding Variational Bayes (2013)
  - 23. Density estimation using Real NVP (2016)
  - 24. Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (2017)
  - 25. Neural Architecture Search with Reinforcement Learning (2016)
- **모델 병합 · 소형 재귀 추론 · 에너지 기반 접근** (7편)
  - 26. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time (2022)
  - 27. Editing Models with Task Arithmetic (2022)
  - 28. TIES-Merging: Resolving Interference When Merging Models (2023)
  - 29. Evolutionary Optimization of Model Merging Recipes (2024)
  - 30. Hierarchical Reasoning Model (2025)
  - 31. Less is More: Recursive Reasoning with Tiny Networks (2025)
  - 32. Energy-Based Transformers are Scalable Learners and Thinkers (2025)

## 학습·일반화 이론과 현상

### 14-01. Neural Tangent Kernel: Convergence and Generalization in Neural Networks

- **식별자**: [arXiv:1806.07572](https://arxiv.org/abs/1806.07572)
- **연도 / 저자·기관**: 2018 / Jacot et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `NTK`, `infinite-width`
- **요약**: 무한 너비 신경망의 학습이 커널 방법(NTK)으로 기술됨을 보인 이론.

### 14-02. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

- **식별자**: [arXiv:1803.03635](https://arxiv.org/abs/1803.03635)
- **연도 / 저자·기관**: 2018 / Frankle & Carbin
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `lottery-ticket`, `pruning`
- **요약**: 큰 네트워크 안에 단독으로 학습 가능한 희소 부분망이 존재한다는 가설.

### 14-03. Deep Double Descent: Where Bigger Models and More Data Hurt

- **식별자**: [arXiv:1912.02292](https://arxiv.org/abs/1912.02292)
- **연도 / 저자·기관**: 2019 / Nakkiran et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `double-descent`
- **요약**: 모델 크기·데이터·학습 시간에 따라 테스트 오류가 두 번 내려가는 현상.

### 14-04. Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets

- **식별자**: [arXiv:2201.02177](https://arxiv.org/abs/2201.02177)
- **연도 / 저자·기관**: 2022 / Power et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `grokking`
- **요약**: 훈련 오차가 0이 된 한참 뒤에 갑자기 일반화되는 현상을 소규모 알고리즘 데이터에서 관찰.

### 14-05. What Can Transformers Learn In-Context? A Case Study of Simple Function Classes

- **식별자**: [arXiv:2208.01066](https://arxiv.org/abs/2208.01066)
- **연도 / 저자·기관**: 2022 / Garg et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ICL`, `theory`
- **요약**: Transformer가 문맥 속 예시만으로 선형 함수 등을 학습할 수 있음을 통제된 설정에서 보임.

### 14-06. Transformers learn in-context by gradient descent

- **식별자**: [arXiv:2212.07677](https://arxiv.org/abs/2212.07677)
- **연도 / 저자·기관**: 2022 / von Oswald et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ICL`, `gradient-descent`
- **요약**: 선형 어텐션 층이 문맥 내 학습에서 경사하강 한 단계와 동등한 연산을 구현할 수 있음을 구성적으로 보임.

### 14-07. Why Can GPT Learn In-Context? Language Models Implicitly Perform Gradient Descent as Meta-Optimizers

- **식별자**: [arXiv:2212.10559](https://arxiv.org/abs/2212.10559)
- **연도 / 저자·기관**: 2022 / Dai et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ICL`, `meta-optimization`
- **요약**: 문맥 내 학습을 어텐션이 만드는 암묵적 경사하강으로 해석.

## 생물·물리에서 영감을 받은 신경망

### 14-08. Neural Turing Machines

- **식별자**: [arXiv:1410.5401](https://arxiv.org/abs/1410.5401)
- **연도 / 저자·기관**: 2014 / Graves et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `external-memory`
- **요약**: 외부 메모리를 읽고 쓰는 미분 가능한 신경망 구조.

### 14-09. HyperNetworks

- **식별자**: [arXiv:1609.09106](https://arxiv.org/abs/1609.09106)
- **연도 / 저자·기관**: 2016 / Ha, Dai, Le
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `hypernetwork`
- **요약**: 한 네트워크가 다른 네트워크의 가중치를 생성.

### 14-10. Dynamic Routing Between Capsules

- **식별자**: [arXiv:1710.09829](https://arxiv.org/abs/1710.09829)
- **연도 / 저자·기관**: 2017 / Sabour, Frosst, Hinton
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `capsule-networks`
- **요약**: 벡터 출력의 캡슐과 동적 라우팅으로 부분-전체 관계를 표현하려는 구조.

### 14-11. Neural Ordinary Differential Equations

- **식별자**: [arXiv:1806.07366](https://arxiv.org/abs/1806.07366)
- **연도 / 저자·기관**: 2018 / Chen et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `neural-ODE`
- **요약**: 은닉 상태의 연속적 변화를 ODE로 모델링하는 연속 깊이 신경망.

### 14-12. Deep Equilibrium Models

- **식별자**: [arXiv:1909.01377](https://arxiv.org/abs/1909.01377)
- **연도 / 저자·기관**: 2019 / Bai, Kolter, Koltun
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DEQ`, `implicit-layers`
- **요약**: 무한히 깊은 가중치 공유 네트워크의 고정점을 직접 구해 평가하는 암묵적 모델.

### 14-13. Liquid Time-constant Networks

- **식별자**: [arXiv:2006.04439](https://arxiv.org/abs/2006.04439)
- **연도 / 저자·기관**: 2020 / Hasani et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `liquid-neural-network`, `continuous-time`
- **요약**: 입력에 따라 시간 상수가 변하는 연속시간 순환 신경망.

### 14-14. Closed-form Continuous-time Neural Models

- **식별자**: [arXiv:2106.13898](https://arxiv.org/abs/2106.13898)
- **연도 / 저자·기관**: 2021 / Hasani et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CfC`, `continuous-time`
- **요약**: 연속시간 신경망의 ODE 풀이를 근사적 닫힌 형태로 대체해 계산을 빠르게 한 CfC.

### 14-15. Hopfield Networks is All You Need

- **식별자**: [arXiv:2008.02217](https://arxiv.org/abs/2008.02217)
- **연도 / 저자·기관**: 2020 / Ramsauer et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `modern-Hopfield`, `attention`
- **요약**: 현대 Hopfield 네트워크의 갱신 규칙이 Transformer 어텐션과 동등함을 보임.

### 14-16. The Forward-Forward Algorithm: Some Preliminary Investigations

- **식별자**: [arXiv:2212.13345](https://arxiv.org/abs/2212.13345)
- **연도 / 저자·기관**: 2022 / Hinton
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `forward-forward`, `backprop-free`
- **요약**: 역전파 대신 긍정/부정 데이터에 대한 두 번의 순전파로 층별 학습하는 대안 알고리즘.

### 14-17. Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation

- **식별자**: [arXiv:2106.04399](https://arxiv.org/abs/2106.04399)
- **연도 / 저자·기관**: 2021 / Bengio et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GFlowNet`
- **요약**: 보상에 비례한 확률로 다양한 후보를 순차 생성하는 GFlowNet.

### 14-18. Spikformer: When Spiking Neural Network Meets Transformer

- **식별자**: [arXiv:2209.15425](https://arxiv.org/abs/2209.15425)
- **연도 / 저자·기관**: 2022 / Zhou et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `spiking`, `transformer`
- **요약**: 스파이킹 신경망에 자기 어텐션을 도입한 구조.

### 14-19. SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks

- **식별자**: [arXiv:2302.13939](https://arxiv.org/abs/2302.13939)
- **연도 / 저자·기관**: 2023 / Zhu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `spiking`, `language-model`
- **요약**: 스파이킹 신경망 기반 생성형 언어모델.

### 14-20. KAN: Kolmogorov-Arnold Networks

- **식별자**: [arXiv:2404.19756](https://arxiv.org/abs/2404.19756)
- **연도 / 저자·기관**: 2024 / Liu et al. (MIT)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `KAN`, `learnable-activation`
- **요약**: 노드가 아닌 엣지에 학습 가능한 1변수 함수를 두는 신경망. 소규모 과학 문제에서 해석 가능성과 정확도를 주장했으나 대규모 효과는 논쟁 중.

## 메타 학습 · 생성 모델의 고전 · 탐색

### 14-21. Generative Adversarial Networks

- **식별자**: [arXiv:1406.2661](https://arxiv.org/abs/1406.2661)
- **연도 / 저자·기관**: 2014 / Goodfellow et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GAN`
- **요약**: 생성기와 판별기가 경쟁하며 학습하는 생성 모델.

### 14-22. Auto-Encoding Variational Bayes

- **식별자**: [arXiv:1312.6114](https://arxiv.org/abs/1312.6114)
- **연도 / 저자·기관**: 2013 / Kingma & Welling
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `VAE`
- **요약**: 변분 추론으로 잠재 변수 생성 모델을 학습하는 VAE.

### 14-23. Density estimation using Real NVP

- **식별자**: [arXiv:1605.08803](https://arxiv.org/abs/1605.08803)
- **연도 / 저자·기관**: 2016 / Dinh et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `normalizing-flow`
- **요약**: 가역 변환으로 정확한 우도를 계산하는 정규화 플로우.

### 14-24. Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks

- **식별자**: [arXiv:1703.03400](https://arxiv.org/abs/1703.03400)
- **연도 / 저자·기관**: 2017 / Finn et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MAML`, `meta-learning`
- **요약**: 소수 경사 단계로 새 과제에 적응하도록 초기 파라미터를 메타 학습.

### 14-25. Neural Architecture Search with Reinforcement Learning

- **식별자**: [arXiv:1611.01578](https://arxiv.org/abs/1611.01578)
- **연도 / 저자·기관**: 2016 / Zoph & Le
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `NAS`
- **요약**: 강화학습으로 신경망 구조를 탐색.

## 모델 병합 · 소형 재귀 추론 · 에너지 기반 접근

### 14-26. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time

- **식별자**: [arXiv:2203.05482](https://arxiv.org/abs/2203.05482)
- **연도 / 저자·기관**: 2022 / Wortsman et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `model-soup`, `weight-averaging`
- **요약**: 여러 미세조정 모델의 가중치를 평균하면 추론 비용 증가 없이 정확도가 향상됨.

### 14-27. Editing Models with Task Arithmetic

- **식별자**: [arXiv:2212.04089](https://arxiv.org/abs/2212.04089)
- **연도 / 저자·기관**: 2022 / Ilharco et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `task-vector`, `model-editing`
- **요약**: 미세조정 전후 가중치 차이(과제 벡터)를 더하고 빼서 모델 능력을 편집.

### 14-28. TIES-Merging: Resolving Interference When Merging Models

- **식별자**: [arXiv:2306.01708](https://arxiv.org/abs/2306.01708)
- **연도 / 저자·기관**: 2023 / Yadav et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `model-merging`
- **요약**: 파라미터 간 간섭을 줄이며 여러 모델을 병합하는 방법.

### 14-29. Evolutionary Optimization of Model Merging Recipes

- **식별자**: [arXiv:2403.13187](https://arxiv.org/abs/2403.13187)
- **연도 / 저자·기관**: 2024 / Akiba et al. (Sakana AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `evolutionary-merge`, `model-merging`
- **요약**: 진화 알고리즘으로 병합 레시피를 자동 탐색. 파라미터 공간과 데이터 흐름 공간 모두에서 작동하며 수학 추론이 가능한 일본어 LLM 등을 구성(Nature Machine Intelligence 2025로 인용됨).

### 14-30. Hierarchical Reasoning Model

- **식별자**: [arXiv:2506.21734](https://arxiv.org/abs/2506.21734)
- **연도 / 저자·기관**: 2025 / Wang et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `HRM`, `recurrent`, `small-model`
- **요약**: 느린 추상 계획 모듈과 빠른 세부 계산 모듈로 이루어진 약 27M 파라미터 순환 모델. 약 1,000개 예시로 학습해 Sudoku-Extreme와 30×30 미로를 풀고 ARC에서 큰 모델을 앞선다고 주장했으나 후속 비판 연구가 있다.

### 14-31. Less is More: Recursive Reasoning with Tiny Networks

- **식별자**: [arXiv:2510.04871](https://arxiv.org/abs/2510.04871)
- **연도 / 저자·기관**: 2025 / Jolicoeur-Martineau
- **검증 상태**: ✅ 검증(V)
- **태그**: `TRM`, `recursive-reasoning`, `ARC-AGI`
- **요약**: HRM을 단순화한 단일 2층 네트워크 TRM(7M 파라미터). 잠재 상태와 답을 재귀적으로 갱신하며 ARC-AGI-1 45%, ARC-AGI-2 8%를 보고.

### 14-32. Energy-Based Transformers are Scalable Learners and Thinkers

- **식별자**: [arXiv:2507.02092](https://arxiv.org/abs/2507.02092)
- **연도 / 저자·기관**: 2025 / Gladstone et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `EBT`, `energy-based`, `system-2`
- **요약**: 에너지를 경사하강으로 최소화하며 예측하는 에너지 기반 Transformer. 학습 스케일링이 Transformer++보다 최대 35% 빠르고 추론 시 추가 연산 이득이 언어 과제에서 29% 더 크다고 보고.
