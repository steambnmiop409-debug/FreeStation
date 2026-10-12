# 09. 멀티모달 · 생성 모델 · 월드 모델

비전-언어 모델, 확산·플로우 기반 생성, 통합 멀티모달 모델, 음성·음악 생성, 그리고 환경의 동역학을 학습하는 월드 모델과 JEPA 계열 자기지도 학습.

> 수록 59편 · 검증(V) 23편 · 기억기반(M) 36편

## 목차

- **비전 표현과 자기지도 학습** (12편)
  - 1. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (2020)
  - 2. Learning Transferable Visual Models From Natural Language Supervision (2021)
  - 3. A Simple Framework for Contrastive Learning of Visual Representations (2020)
  - 4. Masked Autoencoders Are Scalable Vision Learners (2021)
  - 5. DINOv2: Learning Robust Visual Features without Supervision (2023)
  - 6. Segment Anything (2023)
  - 7. SAM 2: Segment Anything in Images and Videos (2024)
  - 8. Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (2023)
  - 9. Revisiting Feature Prediction for Learning Visual Representations from Video (2024)
  - 10. V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning (2025)
  - 11. V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning (2026)
  - 12. VL-JEPA: Joint Embedding Predictive Architecture for Vision-language (2025)
- **비전-언어 모델(VLM)과 통합 멀티모달** (17편)
  - 13. Flamingo: a Visual Language Model for Few-Shot Learning (2022)
  - 14. BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (2023)
  - 15. Visual Instruction Tuning (2023)
  - 16. Improved Baselines with Visual Instruction Tuning (2023)
  - 17. Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond (2023)
  - 18. Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution (2024)
  - 19. Qwen2.5-VL Technical Report (2025)
  - 20. Qwen3-VL Technical Report (2025)
  - 21. Qwen2.5-Omni Technical Report (2025)
  - 22. Qwen3-Omni Technical Report (2025)
  - 23. InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks (2023)
  - 24. Chameleon: Mixed-Modal Early-Fusion Foundation Models (2024)
  - 25. Emu3: Next-Token Prediction is All You Need (2024)
  - 26. Emu3.5: Native Multimodal Models are World Learners (2025)
  - 27. Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model (2024)
  - 28. Show-o: One Single Transformer to Unify Multimodal Understanding and Generation (2024)
  - 29. Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation (2024)
- **확산·플로우·자기회귀 이미지 생성** (16편)
  - 30. Denoising Diffusion Probabilistic Models (2020)
  - 31. Score-Based Generative Modeling through Stochastic Differential Equations (2020)
  - 32. Classifier-Free Diffusion Guidance (2022)
  - 33. High-Resolution Image Synthesis with Latent Diffusion Models (2021)
  - 34. Zero-Shot Text-to-Image Generation (2021)
  - 35. Hierarchical Text-Conditional Image Generation with CLIP Latents (2022)
  - 36. Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding (2022)
  - 37. Scalable Diffusion Models with Transformers (2022)
  - 38. SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis (2023)
  - 39. Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (2024)
  - 40. Flow Matching for Generative Modeling (2022)
  - 41. Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow (2022)
  - 42. Consistency Models (2023)
  - 43. Adding Conditional Control to Text-to-Image Diffusion Models (2023)
  - 44. MaskGIT: Masked Generative Image Transformer (2022)
  - 45. Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction (2024)
- **오디오·음성·범용 모델** (6편)
  - 46. Robust Speech Recognition via Large-Scale Weak Supervision (2022)
  - 47. AudioLM: a Language Modeling Approach to Audio Generation (2022)
  - 48. MusicLM: Generating Music From Text (2023)
  - 49. Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers (2023)
  - 50. Perceiver: General Perception with Iterative Attention (2021)
  - 51. Perceiver IO: A General Architecture for Structured Inputs & Outputs (2021)
- **월드 모델 · 물리 AI 플랫폼** (8편)
  - 52. World Models (2018)
  - 53. Mastering Diverse Domains through World Models (2023)
  - 54. GAIA-1: A Generative World Model for Autonomous Driving (2023)
  - 55. Genie: Generative Interactive Environments (2024)
  - 56. Cosmos World Foundation Model Platform for Physical AI (2025)
  - 57. Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning (2025)
  - 58. Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control (2025)
  - 59. World Simulation with Video Foundation Models for Physical AI (2025)

## 비전 표현과 자기지도 학습

### 09-01. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

- **식별자**: [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)
- **연도 / 저자·기관**: 2020 / Dosovitskiy et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ViT`, `vision-transformer`
- **요약**: 이미지를 16×16 패치 시퀀스로 보고 순수 Transformer를 적용한 ViT.

### 09-02. Learning Transferable Visual Models From Natural Language Supervision

- **식별자**: [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)
- **연도 / 저자·기관**: 2021 / Radford et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CLIP`, `contrastive`, `zero-shot`
- **요약**: 4억 개 이미지-텍스트 쌍으로 대조 학습해 제로샷 분류를 가능하게 한 CLIP.

### 09-03. A Simple Framework for Contrastive Learning of Visual Representations

- **식별자**: [arXiv:2002.05709](https://arxiv.org/abs/2002.05709)
- **연도 / 저자·기관**: 2020 / Chen et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SimCLR`, `contrastive`
- **요약**: 데이터 증강과 대조 손실만으로 시각 표현을 자기지도 학습하는 SimCLR.

### 09-04. Masked Autoencoders Are Scalable Vision Learners

- **식별자**: [arXiv:2111.06377](https://arxiv.org/abs/2111.06377)
- **연도 / 저자·기관**: 2021 / He et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MAE`, `masked-modeling`
- **요약**: 이미지 패치를 높은 비율로 가리고 복원하는 비대칭 오토인코더.

### 09-05. DINOv2: Learning Robust Visual Features without Supervision

- **식별자**: [arXiv:2304.07193](https://arxiv.org/abs/2304.07193)
- **연도 / 저자·기관**: 2023 / Oquab et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DINOv2`, `self-supervised`
- **요약**: 대규모 선별 데이터로 학습한 범용 시각 특징 추출기.

### 09-06. Segment Anything

- **식별자**: [arXiv:2304.02643](https://arxiv.org/abs/2304.02643)
- **연도 / 저자·기관**: 2023 / Kirillov et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SAM`, `segmentation`, `promptable`
- **요약**: 프롬프트 가능한 분할 과제와 10억 마스크 규모 데이터로 학습한 분할 파운데이션 모델.

### 09-07. SAM 2: Segment Anything in Images and Videos

- **식별자**: [arXiv:2408.00714](https://arxiv.org/abs/2408.00714)
- **연도 / 저자·기관**: 2024 / Ravi et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SAM2`, `video-segmentation`
- **요약**: 이미지와 비디오를 모두 다루는 프롬프트 가능한 분할 모델 SAM 2.

### 09-08. Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

- **식별자**: [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- **연도 / 저자·기관**: 2023 / Assran et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `I-JEPA`, `JEPA`
- **요약**: 픽셀이 아닌 표현 공간에서 가려진 영역을 예측하는 JEPA의 이미지 버전.

### 09-09. Revisiting Feature Prediction for Learning Visual Representations from Video

- **식별자**: [arXiv:2404.08471](https://arxiv.org/abs/2404.08471)
- **연도 / 저자·기관**: 2024 / Bardes et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `V-JEPA`, `video`, `feature-prediction`
- **요약**: 비디오에서 오직 특징 예측만으로 학습한 V-JEPA. 200만 공개 비디오로 학습한 ViT-H/16이 Kinetics-400 81.9%, SSv2 72.2%, ImageNet-1K 77.9%를 보고.

### 09-10. V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- **식별자**: [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)
- **연도 / 저자·기관**: 2025 / Assran et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `V-JEPA2`, `world-model`, `robot-planning`
- **요약**: 100만 시간 이상의 영상으로 행동 없는 JEPA를 사전학습하고 소량 로봇 상호작용 데이터로 예측·계획에 활용. SSv2 77.3%, Epic-Kitchens-100 행동 예측 recall@5 39.7을 보고.

### 09-11. V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

- **식별자**: [arXiv:2603.14482](https://arxiv.org/abs/2603.14482)
- **연도 / 저자·기관**: 2026 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `V-JEPA`, `dense-features`
- **요약**: V-JEPA 2의 후속으로 조밀한 지역 특징과 전역 의미를 결합하는 학습 레시피(검색 결과 기준).

### 09-12. VL-JEPA: Joint Embedding Predictive Architecture for Vision-language

- **식별자**: [arXiv:2512.10942](https://arxiv.org/abs/2512.10942)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `VL-JEPA`, `vision-language`
- **요약**: JEPA를 비전-언어로 확장한 연구(ID·제목만 확인).

## 비전-언어 모델(VLM)과 통합 멀티모달

### 09-13. Flamingo: a Visual Language Model for Few-Shot Learning

- **식별자**: [arXiv:2204.14198](https://arxiv.org/abs/2204.14198)
- **연도 / 저자·기관**: 2022 / Alayrac et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Flamingo`, `few-shot`, `VLM`
- **요약**: 사전학습된 비전·언어 모델을 교차 어텐션 층으로 연결해 이미지-텍스트 인터리브 입력으로 퓨샷 학습.

### 09-14. BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

- **식별자**: [arXiv:2301.12597](https://arxiv.org/abs/2301.12597)
- **연도 / 저자·기관**: 2023 / Li et al. (Salesforce)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BLIP-2`, `Q-Former`
- **요약**: 동결된 이미지 인코더와 LLM을 가벼운 Q-Former로 연결.

### 09-15. Visual Instruction Tuning

- **식별자**: [arXiv:2304.08485](https://arxiv.org/abs/2304.08485)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LLaVA`, `visual-instruction`
- **요약**: GPT-4로 생성한 시각 지시 데이터로 비전 인코더와 LLM을 미세조정한 LLaVA.

### 09-16. Improved Baselines with Visual Instruction Tuning

- **식별자**: [arXiv:2310.03744](https://arxiv.org/abs/2310.03744)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `LLaVA-1.5`, `baselines`
- **요약**: MLP 연결과 학술 과제 데이터 혼합 등 단순한 개선만으로 LLaVA의 성능을 크게 높인 후속.

### 09-17. Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond

- **식별자**: [arXiv:2308.12966](https://arxiv.org/abs/2308.12966)
- **연도 / 저자·기관**: 2023 / Bai et al. (Alibaba)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Qwen-VL`, `VLM`
- **요약**: 이해·위치 지정·문자 인식 등을 지원하는 비전-언어 모델.

### 09-18. Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution

- **식별자**: [arXiv:2409.12191](https://arxiv.org/abs/2409.12191)
- **연도 / 저자·기관**: 2024 / Wang et al. (Alibaba)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Qwen2-VL`, `dynamic-resolution`
- **요약**: 임의 해상도 입력을 동적으로 처리하는 Qwen2-VL.

### 09-19. Qwen2.5-VL Technical Report

- **식별자**: [arXiv:2502.13923](https://arxiv.org/abs/2502.13923)
- **연도 / 저자·기관**: 2025 / Bai et al. (Qwen)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen2.5-VL`, `document-parsing`, `video`
- **요약**: 동적 해상도 ViT와 윈도 어텐션을 쓰는 비전-언어 모델. 문서 파싱·객체 위치 지정·장시간 영상 이해를 강화했고, 72B가 MMBench-EN-V1.1에서 88.4%를 보고.

### 09-20. Qwen3-VL Technical Report

- **식별자**: [arXiv:2511.21631](https://arxiv.org/abs/2511.21631)
- **연도 / 저자·기관**: 2025 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `Qwen3-VL`, `VLM`
- **요약**: Qwen3 기반 비전-언어 모델 보고서(ID·제목만 확인).

### 09-21. Qwen2.5-Omni Technical Report

- **식별자**: [arXiv:2503.20215](https://arxiv.org/abs/2503.20215)
- **연도 / 저자·기관**: 2025 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `omni-modal`, `streaming-speech`
- **요약**: 텍스트·이미지·오디오·비디오를 이해하고 스트리밍 음성을 출력하는 옴니 모델(검색 결과 기준).

### 09-22. Qwen3-Omni Technical Report

- **식별자**: [arXiv:2509.17765](https://arxiv.org/abs/2509.17765)
- **연도 / 저자·기관**: 2025 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `omni-modal`
- **요약**: Qwen3 기반 옴니 모달 모델 보고서(ID·제목만 확인).

### 09-23. InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

- **식별자**: [arXiv:2312.14238](https://arxiv.org/abs/2312.14238)
- **연도 / 저자·기관**: 2023 / Chen et al. (OpenGVLab)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `InternVL`, `VLM`
- **요약**: 대형 비전 파운데이션 모델을 LLM과 정렬한 InternVL.

### 09-24. Chameleon: Mixed-Modal Early-Fusion Foundation Models

- **식별자**: [arXiv:2405.09818](https://arxiv.org/abs/2405.09818)
- **연도 / 저자·기관**: 2024 / Chameleon Team (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Chameleon`, `early-fusion`, `token-based`
- **요약**: 이미지와 텍스트를 모두 이산 토큰으로 바꿔 처음부터 하나의 Transformer로 학습하는 초기 융합 모델.

### 09-25. Emu3: Next-Token Prediction is All You Need

- **식별자**: [arXiv:2409.18869](https://arxiv.org/abs/2409.18869)
- **연도 / 저자·기관**: 2024 / Wang et al. (BAAI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Emu3`, `unified`, `next-token`
- **요약**: 이미지·텍스트·비디오를 이산 토큰화해 하나의 Transformer를 다음 토큰 예측만으로 학습. 확산이나 합성 구조 없이 SDXL·LLaVA-1.6을 능가한다고 보고.

### 09-26. Emu3.5: Native Multimodal Models are World Learners

- **식별자**: [arXiv:2510.26583](https://arxiv.org/abs/2510.26583)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Emu3.5`, `world-learner`
- **요약**: Emu3를 10조 토큰 이상 멀티모달 데이터로 확장한 후속(검색 결과 기준).

### 09-27. Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model

- **식별자**: [arXiv:2408.11039](https://arxiv.org/abs/2408.11039)
- **연도 / 저자·기관**: 2024 / Zhou et al. (Meta)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Transfusion`, `AR+diffusion`
- **요약**: 하나의 Transformer로 텍스트는 다음 토큰 예측, 이미지는 확산 손실로 함께 학습. 텍스트는 인과 마스크, 이미지는 양방향 어텐션 사용.

### 09-28. Show-o: One Single Transformer to Unify Multimodal Understanding and Generation

- **식별자**: [arXiv:2408.12528](https://arxiv.org/abs/2408.12528)
- **연도 / 저자·기관**: 2024 / Xie et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Show-o`, `unified`
- **요약**: 자기회귀와 이산 확산을 한 Transformer에서 결합한 통합 이해·생성 모델.

### 09-29. Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation

- **식별자**: [arXiv:2410.13848](https://arxiv.org/abs/2410.13848)
- **연도 / 저자·기관**: 2024 / Wu et al. (DeepSeek)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Janus`, `decoupled-encoder`
- **요약**: 이해와 생성에 서로 다른 시각 인코딩 경로를 쓰는 통합 모델.

## 확산·플로우·자기회귀 이미지 생성

### 09-30. Denoising Diffusion Probabilistic Models

- **식별자**: [arXiv:2006.11239](https://arxiv.org/abs/2006.11239)
- **연도 / 저자·기관**: 2020 / Ho et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DDPM`, `diffusion`
- **요약**: 잡음을 단계적으로 제거하는 확산 모델로 고품질 이미지 생성이 가능함을 보인 논문.

### 09-31. Score-Based Generative Modeling through Stochastic Differential Equations

- **식별자**: [arXiv:2011.13456](https://arxiv.org/abs/2011.13456)
- **연도 / 저자·기관**: 2020 / Song et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `score-SDE`, `diffusion`
- **요약**: 확산을 SDE 관점으로 통합하고 확률 흐름 ODE 등을 제시.

### 09-32. Classifier-Free Diffusion Guidance

- **식별자**: [arXiv:2207.12598](https://arxiv.org/abs/2207.12598)
- **연도 / 저자·기관**: 2022 / Ho & Salimans
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CFG`, `guidance`
- **요약**: 분류기 없이 조건부/무조건부 예측을 섞어 조건 충실도를 높이는 가이던스.

### 09-33. High-Resolution Image Synthesis with Latent Diffusion Models

- **식별자**: [arXiv:2112.10752](https://arxiv.org/abs/2112.10752)
- **연도 / 저자·기관**: 2021 / Rombach et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Latent-Diffusion`, `Stable-Diffusion`
- **요약**: 오토인코더의 잠재 공간에서 확산을 수행해 비용을 크게 줄인 Stable Diffusion의 기반.

### 09-34. Zero-Shot Text-to-Image Generation

- **식별자**: [arXiv:2102.12092](https://arxiv.org/abs/2102.12092)
- **연도 / 저자·기관**: 2021 / Ramesh et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DALL-E`, `autoregressive`
- **요약**: 텍스트와 이미지 토큰을 자기회귀 Transformer로 학습한 초기 DALL-E.

### 09-35. Hierarchical Text-Conditional Image Generation with CLIP Latents

- **식별자**: [arXiv:2204.06125](https://arxiv.org/abs/2204.06125)
- **연도 / 저자·기관**: 2022 / Ramesh et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DALL-E-2`, `unCLIP`
- **요약**: CLIP 임베딩을 사전 모델로 생성한 뒤 확산 디코더로 이미지를 만드는 구조.

### 09-36. Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

- **식별자**: [arXiv:2205.11487](https://arxiv.org/abs/2205.11487)
- **연도 / 저자·기관**: 2022 / Saharia et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Imagen`
- **요약**: 큰 텍스트 인코더가 이미지 확산 모델 품질에 중요함을 보인 Imagen.

### 09-37. Scalable Diffusion Models with Transformers

- **식별자**: [arXiv:2212.09748](https://arxiv.org/abs/2212.09748)
- **연도 / 저자·기관**: 2022 / Peebles & Xie
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DiT`, `diffusion-transformer`
- **요약**: 확산의 U-Net 백본을 Transformer로 대체한 DiT. 규모에 따라 성능이 개선됨.

### 09-38. SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis

- **식별자**: [arXiv:2307.01952](https://arxiv.org/abs/2307.01952)
- **연도 / 저자·기관**: 2023 / Podell et al. (Stability AI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SDXL`
- **요약**: 더 큰 U-Net과 이중 텍스트 인코더로 해상도·품질을 높인 Stable Diffusion XL.

### 09-39. Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

- **식별자**: [arXiv:2403.03206](https://arxiv.org/abs/2403.03206)
- **연도 / 저자·기관**: 2024 / Esser et al. (Stability AI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SD3`, `rectified-flow`, `MM-DiT`
- **요약**: 정류 플로우(rectified flow)와 텍스트·이미지 양방향 정보 흐름의 MM-DiT를 쓰는 Stable Diffusion 3의 논문.

### 09-40. Flow Matching for Generative Modeling

- **식별자**: [arXiv:2210.02747](https://arxiv.org/abs/2210.02747)
- **연도 / 저자·기관**: 2022 / Lipman et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `flow-matching`
- **요약**: 시뮬레이션 없이 연속 정규화 플로우를 학습하는 Flow Matching.

### 09-41. Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow

- **식별자**: [arXiv:2209.03003](https://arxiv.org/abs/2209.03003)
- **연도 / 저자·기관**: 2022 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `rectified-flow`
- **요약**: 두 분포를 잇는 직선 경로를 학습하는 정류 플로우.

### 09-42. Consistency Models

- **식별자**: [arXiv:2303.01469](https://arxiv.org/abs/2303.01469)
- **연도 / 저자·기관**: 2023 / Song et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `consistency-models`, `one-step`
- **요약**: 한 번(또는 소수)의 단계로 샘플링하도록 확산 궤적의 일관성을 학습.

### 09-43. Adding Conditional Control to Text-to-Image Diffusion Models

- **식별자**: [arXiv:2302.05543](https://arxiv.org/abs/2302.05543)
- **연도 / 저자·기관**: 2023 / Zhang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ControlNet`
- **요약**: 사전학습 확산 모델에 공간 조건(에지, 깊이 등)을 추가하는 ControlNet.

### 09-44. MaskGIT: Masked Generative Image Transformer

- **식별자**: [arXiv:2202.04200](https://arxiv.org/abs/2202.04200)
- **연도 / 저자·기관**: 2022 / Chang et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MaskGIT`, `masked-generation`
- **요약**: 이산 토큰을 병렬로 반복 복원하며 이미지를 생성.

### 09-45. Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction

- **식별자**: [arXiv:2404.02905](https://arxiv.org/abs/2404.02905)
- **연도 / 저자·기관**: 2024 / Tian et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `VAR`, `next-scale`, `NeurIPS-best-paper`
- **요약**: 래스터 순서 대신 저해상도→고해상도의 ‘다음 스케일 예측’ 자기회귀. ImageNet 256×256에서 FID와 IS를 크게 개선하고 추론이 약 20배 빠르며 거듭제곱 스케일링 법칙을 보고(NeurIPS 2024 최우수 논문).

## 오디오·음성·범용 모델

### 09-46. Robust Speech Recognition via Large-Scale Weak Supervision

- **식별자**: [arXiv:2212.04356](https://arxiv.org/abs/2212.04356)
- **연도 / 저자·기관**: 2022 / Radford et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Whisper`, `ASR`
- **요약**: 68만 시간의 약한 감독 음성 데이터로 학습한 다국어 음성 인식 Whisper.

### 09-47. AudioLM: a Language Modeling Approach to Audio Generation

- **식별자**: [arXiv:2209.03143](https://arxiv.org/abs/2209.03143)
- **연도 / 저자·기관**: 2022 / Borsos et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AudioLM`, `audio-tokens`
- **요약**: 오디오를 의미·음향 토큰으로 나눠 언어모델링하는 생성 방식.

### 09-48. MusicLM: Generating Music From Text

- **식별자**: [arXiv:2301.11325](https://arxiv.org/abs/2301.11325)
- **연도 / 저자·기관**: 2023 / Agostinelli et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MusicLM`, `text-to-music`
- **요약**: 텍스트 설명으로부터 고충실도 음악을 생성.

### 09-49. Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers

- **식별자**: [arXiv:2301.02111](https://arxiv.org/abs/2301.02111)
- **연도 / 저자·기관**: 2023 / Wang et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `VALL-E`, `zero-shot-TTS`
- **요약**: 오디오 코덱 토큰의 언어모델링으로 3초 프롬프트만으로 화자를 모사하는 TTS.

### 09-50. Perceiver: General Perception with Iterative Attention

- **식별자**: [arXiv:2103.03206](https://arxiv.org/abs/2103.03206)
- **연도 / 저자·기관**: 2021 / Jaegle et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Perceiver`, `cross-attention`
- **요약**: 잠재 배열에 교차 어텐션으로 입력을 읽어 입력 크기와 계산을 분리한 범용 구조.

### 09-51. Perceiver IO: A General Architecture for Structured Inputs & Outputs

- **식별자**: [arXiv:2107.14795](https://arxiv.org/abs/2107.14795)
- **연도 / 저자·기관**: 2021 / Jaegle et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Perceiver-IO`
- **요약**: 출력까지 질의 기반으로 확장한 Perceiver IO.

## 월드 모델 · 물리 AI 플랫폼

### 09-52. World Models

- **식별자**: [arXiv:1803.10122](https://arxiv.org/abs/1803.10122)
- **연도 / 저자·기관**: 2018 / Ha & Schmidhuber
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `world-model`, `VAE+RNN`
- **요약**: 환경의 압축 표현과 예측 모델을 학습해 그 ‘꿈’ 속에서 정책을 학습하는 월드 모델의 고전.

### 09-53. Mastering Diverse Domains through World Models

- **식별자**: [arXiv:2301.04104](https://arxiv.org/abs/2301.04104)
- **연도 / 저자·기관**: 2023 / Hafner et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `DreamerV3`, `world-model`
- **요약**: 하나의 설정으로 150개 이상 과제를 해결한 모델 기반 RL, DreamerV3.

### 09-54. GAIA-1: A Generative World Model for Autonomous Driving

- **식별자**: [arXiv:2309.17080](https://arxiv.org/abs/2309.17080)
- **연도 / 저자·기관**: 2023 / Hu et al. (Wayve)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GAIA-1`, `driving`, `world-model`
- **요약**: 영상·텍스트·행동을 입력으로 주행 장면을 생성하는 자율주행용 생성 월드 모델.

### 09-55. Genie: Generative Interactive Environments

- **식별자**: [arXiv:2402.15391](https://arxiv.org/abs/2402.15391)
- **연도 / 저자·기관**: 2024 / Bruce et al. (Google DeepMind)
- **검증 상태**: ✅ 검증(V)
- **태그**: `Genie`, `world-model`, `latent-action`
- **요약**: 라벨 없는 인터넷 영상에서 학습한 11B 규모 ‘파운데이션 월드 모델’. 시공간 비디오 토크나이저·자기회귀 동역학 모델·잠재 행동 모델로 프레임 단위 조작 가능한 세계를 생성(ICML 2024).

### 09-56. Cosmos World Foundation Model Platform for Physical AI

- **식별자**: [arXiv:2501.03575](https://arxiv.org/abs/2501.03575)
- **연도 / 저자·기관**: 2025 / NVIDIA
- **검증 상태**: ✅ 검증(V)
- **태그**: `Cosmos`, `world-foundation-model`, `physical-AI`
- **요약**: 물리 AI용 월드 파운데이션 모델 플랫폼: 비디오 큐레이션 파이프라인, 사전학습 모델(확산·자기회귀), 후속 학습 예시, 비디오 토크나이저를 오픈 라이선스로 공개.

### 09-57. Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning

- **식별자**: [arXiv:2503.15558](https://arxiv.org/abs/2503.15558)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Cosmos`, `embodied-reasoning`
- **요약**: 물리적 상식에서 구현 추론으로 이어지는 Cosmos 계열 모델(ID·제목만 확인).

### 09-58. Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control

- **식별자**: [arXiv:2503.14492](https://arxiv.org/abs/2503.14492)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `Cosmos`, `world-generation`
- **요약**: 적응형 멀티모달 제어로 조건부 세계 생성을 하는 Cosmos 계열(ID·제목만 확인).

### 09-59. World Simulation with Video Foundation Models for Physical AI

- **식별자**: [arXiv:2511.00062](https://arxiv.org/abs/2511.00062)
- **연도 / 저자·기관**: 2025 / NVIDIA
- **검증 상태**: ✅ 검증(V)
- **태그**: `Cosmos-Predict2.5`, `Cosmos-Transfer2.5`
- **요약**: Cosmos-Predict2.5와 Cosmos-Transfer2.5를 다루는 2025년 보고(검색 결과 기준).
