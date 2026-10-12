# 10. 로보틱스 · 구현형(Embodied) AI · 비전-언어-행동 모델

언어·비전 파운데이션 모델을 로봇 제어로 확장하는 VLA(Vision-Language-Action) 계열과, 로봇 데이터·모방 학습·휴머노이드 파운데이션 모델.

> 수록 13편 · 검증(V) 8편 · 기억기반(M) 5편

## 목차

- **초기 로봇 트랜스포머와 언어 접지** (6편)
  - 1. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (2022)
  - 2. RT-1: Robotics Transformer for Real-World Control at Scale (2022)
  - 3. PaLM-E: An Embodied Multimodal Language Model (2023)
  - 4. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (2023)
  - 5. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (2023)
  - 6. Open X-Embodiment: Robotic Learning Datasets and RT-X Models (2023)
- **오픈 VLA와 일반 로봇 정책** (7편)
  - 7. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation (2024)
  - 8. Octo: An Open-Source Generalist Robot Policy (2024)
  - 9. OpenVLA: An Open-Source Vision-Language-Action Model (2024)
  - 10. π0: A Vision-Language-Action Flow Model for General Robot Control (2024)
  - 11. π0.5: a Vision-Language-Action Model with Open-World Generalization (2025)
  - 12. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (2025)
  - 13. Gemini Robotics: Bringing AI into the Physical World (2025)

## 초기 로봇 트랜스포머와 언어 접지

### 10-01. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

- **식별자**: [arXiv:2204.01691](https://arxiv.org/abs/2204.01691)
- **연도 / 저자·기관**: 2022 / Ahn et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SayCan`, `affordance`, `planning`
- **요약**: LLM이 제안한 단계 중 로봇이 실제로 수행 가능한(affordance 값이 높은) 행동을 고르게 하는 SayCan.

### 10-02. RT-1: Robotics Transformer for Real-World Control at Scale

- **식별자**: [arXiv:2212.06817](https://arxiv.org/abs/2212.06817)
- **연도 / 저자·기관**: 2022 / Brohan et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RT-1`, `robot-transformer`
- **요약**: 13만 건 이상의 실제 로봇 에피소드로 학습한 Transformer 기반 다과제 제어 정책.

### 10-03. PaLM-E: An Embodied Multimodal Language Model

- **식별자**: [arXiv:2303.03378](https://arxiv.org/abs/2303.03378)
- **연도 / 저자·기관**: 2023 / Driess et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `PaLM-E`, `embodied`, `multimodal`
- **요약**: 센서 입력(이미지·상태)을 언어모델 입력 임베딩으로 통합해 로봇 계획과 시각-언어 과제를 함께 수행하는 구현형 멀티모달 모델.

### 10-04. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

- **식별자**: [arXiv:2307.15818](https://arxiv.org/abs/2307.15818)
- **연도 / 저자·기관**: 2023 / Brohan et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RT-2`, `VLA`
- **요약**: 웹 규모 시각-언어 데이터와 로봇 행동을 함께 학습해 행동을 토큰으로 출력하는 VLA의 대표 초기 사례.

### 10-05. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

- **식별자**: [arXiv:2303.04137](https://arxiv.org/abs/2303.04137)
- **연도 / 저자·기관**: 2023 / Chi et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `diffusion-policy`, `imitation-learning`
- **요약**: 로봇 행동 분포를 조건부 확산 모델로 표현하는 모방 학습 정책.

### 10-06. Open X-Embodiment: Robotic Learning Datasets and RT-X Models

- **식별자**: [arXiv:2310.08864](https://arxiv.org/abs/2310.08864)
- **연도 / 저자·기관**: 2023 / Open X-Embodiment Collaboration
- **검증 상태**: ✅ 검증(V)
- **태그**: `dataset`, `cross-embodiment`
- **요약**: 여러 기관·로봇 형태의 데이터를 모은 대규모 데이터셋과, 이를 이용한 교차 구현체(cross-embodiment) 학습 모델(RT-X).

## 오픈 VLA와 일반 로봇 정책

### 10-07. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation

- **식별자**: [arXiv:2401.02117](https://arxiv.org/abs/2401.02117)
- **연도 / 저자·기관**: 2024 / Fu, Zhao, Finn (Stanford)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Mobile-ALOHA`, `bimanual`, `imitation-learning`
- **요약**: 저비용 전신 원격조작 인터페이스로 양팔 이동 조작 데이터를 수집. 기존 정적 ALOHA 데이터와 함께 학습(co-training)하면 과제당 50개 시연으로 성공률이 최대 90% 향상된다고 보고(CoRL 2024).

### 10-08. Octo: An Open-Source Generalist Robot Policy

- **식별자**: [arXiv:2405.12213](https://arxiv.org/abs/2405.12213)
- **연도 / 저자·기관**: 2024 / Octo Model Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `Octo`, `generalist-policy`, `Open-X`
- **요약**: Open X-Embodiment의 80만 궤적으로 학습한 Transformer 기반 정책. 언어·목표 이미지 지시를 받고 새 센서 구성에도 미세조정 가능(RSS 2024).

### 10-09. OpenVLA: An Open-Source Vision-Language-Action Model

- **식별자**: [arXiv:2406.09246](https://arxiv.org/abs/2406.09246)
- **연도 / 저자·기관**: 2024 / Kim et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `OpenVLA`, `7B`, `open-source`
- **요약**: Llama 2 기반 7B 모델에 DINOv2·SigLIP 특징을 융합하고 97만 건의 실제 로봇 시연으로 학습한 오픈 VLA. 체크포인트·미세조정 노트북·코드를 공개.

### 10-10. π0: A Vision-Language-Action Flow Model for General Robot Control

- **식별자**: [arXiv:2410.24164](https://arxiv.org/abs/2410.24164)
- **연도 / 저자·기관**: 2024 / Black et al. (Physical Intelligence)
- **검증 상태**: ✅ 검증(V)
- **태그**: `pi0`, `flow-matching`, `action-expert`
- **요약**: 사전학습 VLM 위에 플로우 매칭으로 연속 행동을 생성하는 별도 ‘행동 전문가’를 얹고 다양한 교차 구현체 데이터로 학습. 빨래 개기, 상자 조립 같은 다단계 과제로 미세조정 가능.

### 10-11. π0.5: a Vision-Language-Action Model with Open-World Generalization

- **식별자**: [arXiv:2504.16054](https://arxiv.org/abs/2504.16054)
- **연도 / 저자·기관**: 2025 / Physical Intelligence
- **검증 상태**: ✅ 검증(V)
- **태그**: `pi0.5`, `open-world`
- **요약**: π0의 후속. 약 400시간의 이동 조작 데이터와 다른 로봇·실험실 데이터로 학습(검색 결과 기준, 본문 미검토).

### 10-12. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots

- **식별자**: [arXiv:2503.14734](https://arxiv.org/abs/2503.14734)
- **연도 / 저자·기관**: 2025 / NVIDIA (Bjorck, Zhu et al.)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GR00T-N1`, `humanoid`, `VLA`
- **요약**: 비전-언어 모듈과 확산 Transformer 행동 생성기를 결합한 2중 구조의 오픈 휴머노이드 파운데이션 모델. 실제 로봇 궤적·인간 영상·합성 데이터를 혼합해 학습하고 Fourier GR-1에 배치.

### 10-13. Gemini Robotics: Bringing AI into the Physical World

- **식별자**: [arXiv:2503.20020](https://arxiv.org/abs/2503.20020)
- **연도 / 저자·기관**: 2025 / Gemini Robotics Team (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Gemini-Robotics`, `VLA`, `embodied-reasoning`
- **요약**: Gemini 2.0 기반으로 로봇을 직접 제어하는 VLA(Gemini Robotics)와 공간·시간 추론을 담당하는 Gemini Robotics-ER. 미세조정으로 장기 정교 과제와 100개 내외 시연으로 새 과제를 학습.
