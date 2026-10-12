# 08. 에이전트 · 도구 사용 · RAG · 임베딩 · 자기 개선 시스템

LLM이 외부 도구·검색·메모리·다른 에이전트와 상호작용하며 작업을 수행하는 시스템 연구, 그리고 에이전트를 평가하는 벤치마크.

> 수록 65편 · 검증(V) 22편 · 기억기반(M) 43편

## 목차

- **검색 증강 생성(RAG)과 검색 모델** (21편)
  - 1. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)
  - 2. REALM: Retrieval-Augmented Language Model Pre-Training (2020)
  - 3. Improving language models by retrieving from trillions of tokens (2021)
  - 4. Atlas: Few-shot Learning with Retrieval Augmented Language Models (2022)
  - 5. Dense Passage Retrieval for Open-Domain Question Answering (2020)
  - 6. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT (2020)
  - 7. ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction (2021)
  - 8. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (2019)
  - 9. Unsupervised Dense Information Retrieval with Contrastive Learning (2021)
  - 10. Text Embeddings by Weakly-Supervised Contrastive Pre-training (2022)
  - 11. BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation (2024)
  - 12. Matryoshka Representation Learning (2022)
  - 13. Qwen3 Embedding (2025)
  - 14. Precise Zero-Shot Dense Retrieval without Relevance Labels (2022)
  - 15. Active Retrieval Augmented Generation (2023)
  - 16. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection (2023)
  - 17. Corrective Retrieval Augmented Generation (2024)
  - 18. Dense X Retrieval: What Retrieval Granularity Should We Use? (2023)
  - 19. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval (2024)
  - 20. From Local to Global: A Graph RAG Approach to Query-Focused Summarization (2024)
  - 21. Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (2025)
- **도구 사용과 에이전트 프레임워크** (15편)
  - 22. ReAct: Synergizing Reasoning and Acting in Language Models (2022)
  - 23. Toolformer: Language Models Can Teach Themselves to Use Tools (2023)
  - 24. WebGPT: Browser-assisted question-answering with human feedback (2021)
  - 25. Gorilla: Large Language Model Connected with Massive APIs (2023)
  - 26. ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs (2023)
  - 27. Executable Code Actions Elicit Better LLM Agents (2024)
  - 28. HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face (2023)
  - 29. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation (2023)
  - 30. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework (2023)
  - 31. ChatDev: Communicative Agents for Software Development (2023)
  - 32. CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society (2023)
  - 33. Mixture-of-Agents Enhances Large Language Model Capabilities (2024)
  - 34. Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial? (2025)
  - 35. A Survey on Large Language Model based Autonomous Agents (2023)
  - 36. The Rise and Potential of Large Language Model Based Agents: A Survey (2023)
- **장기 기억 · 시뮬레이션 · 컴퓨터 사용 에이전트** (5편)
  - 37. Generative Agents: Interactive Simulacra of Human Behavior (2023)
  - 38. MemGPT: Towards LLMs as Operating Systems (2023)
  - 39. Voyager: An Open-Ended Embodied Agent with Large Language Models (2023)
  - 40. UI-TARS: Pioneering Automated GUI Interaction with Native Agents (2025)
  - 41. UI-TARS-2 Technical Report (2025)
- **에이전트 벤치마크** (14편)
  - 42. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)
  - 43. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (2024)
  - 44. OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments (2024)
  - 45. WebArena: A Realistic Web Environment for Building Autonomous Agents (2023)
  - 46. Mind2Web: Towards a Generalist Agent for the Web (2023)
  - 47. GAIA: a benchmark for General AI Assistants (2023)
  - 48. AgentBench: Evaluating LLMs as Agents (2023)
  - 49. τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (2024)
  - 50. τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment (2025)
  - 51. BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents (2025)
  - 52. BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent (2025)
  - 53. MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering (2024)
  - 54. AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench (2025)
  - 55. RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts (2024)
- **자기 개선·자동 프롬프트·과학 에이전트** (10편)
  - 56. Large Language Models as Optimizers (2023)
  - 57. Eureka: Human-Level Reward Design via Coding Large Language Models (2023)
  - 58. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (2023)
  - 59. Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution (2023)
  - 60. Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation (2023)
  - 61. TextGrad: Automatic Differentiation via Text (2024)
  - 62. Automated Design of Agentic Systems (2024)
  - 63. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (2024)
  - 64. Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents (2025)
  - 65. Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025)

## 검색 증강 생성(RAG)과 검색 모델

### 08-01. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- **식별자**: [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- **연도 / 저자·기관**: 2020 / Lewis et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RAG`, `retrieval`
- **요약**: 생성 모델에 검색기를 결합해 외부 지식을 조회하며 답하는 RAG의 원형.

### 08-02. REALM: Retrieval-Augmented Language Model Pre-Training

- **식별자**: [arXiv:2002.08909](https://arxiv.org/abs/2002.08909)
- **연도 / 저자·기관**: 2020 / Guu et al. (Google)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `REALM`, `retrieval-pretraining`
- **요약**: 사전학습 단계에서부터 검색기를 함께 학습하는 언어모델.

### 08-03. Improving language models by retrieving from trillions of tokens

- **식별자**: [arXiv:2112.04426](https://arxiv.org/abs/2112.04426)
- **연도 / 저자·기관**: 2021 / Borgeaud et al. (DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `RETRO`, `retrieval`
- **요약**: 수조 토큰 규모 데이터베이스에서 이웃 청크를 검색해 교차 어텐션으로 쓰는 RETRO.

### 08-04. Atlas: Few-shot Learning with Retrieval Augmented Language Models

- **식별자**: [arXiv:2208.03299](https://arxiv.org/abs/2208.03299)
- **연도 / 저자·기관**: 2022 / Izacard et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Atlas`, `few-shot`, `retrieval`
- **요약**: 검색 증강 모델이 소수 예시로도 지식 집약 과제에서 매우 큰 모델과 경쟁함을 보인 연구.

### 08-05. Dense Passage Retrieval for Open-Domain Question Answering

- **식별자**: [arXiv:2004.04906](https://arxiv.org/abs/2004.04906)
- **연도 / 저자·기관**: 2020 / Karpukhin et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DPR`, `dense-retrieval`
- **요약**: 이중 인코더로 질문·문단을 임베딩해 BM25를 능가한 밀집 검색.

### 08-06. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT

- **식별자**: [arXiv:2004.12832](https://arxiv.org/abs/2004.12832)
- **연도 / 저자·기관**: 2020 / Khattab & Zaharia
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ColBERT`, `late-interaction`
- **요약**: 토큰 수준 임베딩의 후기 상호작용(MaxSim)으로 정확도와 효율을 절충한 검색.

### 08-07. ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction

- **식별자**: [arXiv:2112.01488](https://arxiv.org/abs/2112.01488)
- **연도 / 저자·기관**: 2021 / Santhanam et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ColBERTv2`, `compression`
- **요약**: 잔차 압축과 증류로 ColBERT의 저장 비용을 줄이고 품질을 높인 후속.

### 08-08. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

- **식별자**: [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- **연도 / 저자·기관**: 2019 / Reimers & Gurevych
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SBERT`, `sentence-embedding`
- **요약**: 시암 구조로 문장 임베딩을 효율적으로 얻는 SBERT.

### 08-09. Unsupervised Dense Information Retrieval with Contrastive Learning

- **식별자**: [arXiv:2112.09118](https://arxiv.org/abs/2112.09118)
- **연도 / 저자·기관**: 2021 / Izacard et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Contriever`, `unsupervised`
- **요약**: 레이블 없이 대조 학습으로 학습한 범용 밀집 검색기 Contriever.

### 08-10. Text Embeddings by Weakly-Supervised Contrastive Pre-training

- **식별자**: [arXiv:2212.03533](https://arxiv.org/abs/2212.03533)
- **연도 / 저자·기관**: 2022 / Wang et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `E5`, `embeddings`
- **요약**: 약한 감독의 대규모 텍스트 쌍으로 대조 사전학습한 범용 임베딩 E5.

### 08-11. BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation

- **식별자**: [arXiv:2402.03216](https://arxiv.org/abs/2402.03216)
- **연도 / 저자·기관**: 2024 / Chen et al. (BAAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `BGE-M3`, `multilingual`, `embedding`
- **요약**: 다국어·밀집/희소/다중벡터 검색·긴 입력을 한 모델로 지원하는 임베딩.

### 08-12. Matryoshka Representation Learning

- **식별자**: [arXiv:2205.13147](https://arxiv.org/abs/2205.13147)
- **연도 / 저자·기관**: 2022 / Kusupati et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Matryoshka`, `adaptive-embedding`
- **요약**: 앞부분 차원만 잘라 써도 성능이 유지되도록 다중 해상도로 학습하는 임베딩.

### 08-13. Qwen3 Embedding

- **식별자**: [arXiv:2506.05176](https://arxiv.org/abs/2506.05176)
- **연도 / 저자·기관**: 2025 / Qwen Team
- **검증 상태**: ✅ 검증(V)
- **태그**: `embedding`, `reranking`, `Qwen3`
- **요약**: Qwen3 기반 임베딩·리랭킹 모델 보고(검색 결과 기준 ID와 제목만 확인).

### 08-14. Precise Zero-Shot Dense Retrieval without Relevance Labels

- **식별자**: [arXiv:2212.10496](https://arxiv.org/abs/2212.10496)
- **연도 / 저자·기관**: 2022 / Gao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `HyDE`, `query-expansion`
- **요약**: 질문에 대한 가상 문서를 생성해 그 임베딩으로 검색하는 HyDE.

### 08-15. Active Retrieval Augmented Generation

- **식별자**: [arXiv:2305.06983](https://arxiv.org/abs/2305.06983)
- **연도 / 저자·기관**: 2023 / Jiang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `FLARE`, `active-retrieval`
- **요약**: 생성 중 불확실할 때 능동적으로 검색을 수행하는 FLARE.

### 08-16. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

- **식별자**: [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- **연도 / 저자·기관**: 2023 / Asai et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Self-RAG`, `reflection-tokens`
- **요약**: 검색 필요 여부와 생성 품질을 ‘반성 토큰’으로 스스로 판단하며 검색·생성하는 모델.

### 08-17. Corrective Retrieval Augmented Generation

- **식별자**: [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- **연도 / 저자·기관**: 2024 / Yan et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `CRAG`, `retrieval-evaluator`
- **요약**: 검색 결과의 품질을 평가해 부족하면 웹 검색으로 보정하는 CRAG.

### 08-18. Dense X Retrieval: What Retrieval Granularity Should We Use?

- **식별자**: [arXiv:2312.06648](https://arxiv.org/abs/2312.06648)
- **연도 / 저자·기관**: 2023 / Chen et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `retrieval-granularity`, `propositions`
- **요약**: 문서·문단 대신 ‘명제’ 단위로 색인하면 검색과 하류 성능이 개선됨을 보인 연구.

### 08-19. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

- **식별자**: [arXiv:2401.18059](https://arxiv.org/abs/2401.18059)
- **연도 / 저자·기관**: 2024 / Sarthi et al. (Stanford)
- **검증 상태**: ✅ 검증(V)
- **태그**: `RAPTOR`, `hierarchical-retrieval`
- **요약**: 청크를 임베딩·군집화·요약하는 과정을 재귀적으로 반복해 요약 트리를 만들고 여러 추상화 수준에서 검색(ICLR 2024).

### 08-20. From Local to Global: A Graph RAG Approach to Query-Focused Summarization

- **식별자**: [arXiv:2404.16130](https://arxiv.org/abs/2404.16130)
- **연도 / 저자·기관**: 2024 / Edge et al. (Microsoft)
- **검증 상태**: ✅ 검증(V)
- **태그**: `GraphRAG`, `knowledge-graph`, `community-summary`
- **요약**: LLM으로 지식 그래프를 만들고 커뮤니티별 요약을 색인으로 써 코퍼스 전체에 대한 질의에 답한다. 벡터 RAG 대비 포괄성·다양성이 개선됐다고 보고.

### 08-21. Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

- **식별자**: [arXiv:2503.09516](https://arxiv.org/abs/2503.09516)
- **연도 / 저자·기관**: 2025 / Jin et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `Search-R1`, `RL`, `agentic-search`
- **요약**: 추론 중 검색 질의를 스스로 생성하도록 순수 RL로 학습. 검색 결과 토큰 마스킹과 결과 기반 보상을 사용하며 7개 QA 데이터셋에서 기준선 대비 10~26% 개선을 보고(COLM 2025).

## 도구 사용과 에이전트 프레임워크

### 08-22. ReAct: Synergizing Reasoning and Acting in Language Models

- **식별자**: [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- **연도 / 저자·기관**: 2022 / Yao et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ReAct`, `tool-use`
- **요약**: 추론(Thought)과 행동(Action)을 번갈아 생성하며 외부 환경과 상호작용하는 프롬프팅 패러다임.

### 08-23. Toolformer: Language Models Can Teach Themselves to Use Tools

- **식별자**: [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)
- **연도 / 저자·기관**: 2023 / Schick et al. (Meta)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Toolformer`, `self-supervised-tool-use`
- **요약**: API 호출을 언제·어떻게 쓸지 자기지도로 학습하는 모델.

### 08-24. WebGPT: Browser-assisted question-answering with human feedback

- **식별자**: [arXiv:2112.09332](https://arxiv.org/abs/2112.09332)
- **연도 / 저자·기관**: 2021 / Nakano et al. (OpenAI)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `WebGPT`, `browsing`
- **요약**: 텍스트 기반 브라우저로 검색하고 출처를 인용하도록 인간 피드백으로 학습한 모델.

### 08-25. Gorilla: Large Language Model Connected with Massive APIs

- **식별자**: [arXiv:2305.15334](https://arxiv.org/abs/2305.15334)
- **연도 / 저자·기관**: 2023 / Patil et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Gorilla`, `API-calling`
- **요약**: 대규모 API 문서 기반으로 정확한 API 호출을 생성하도록 미세조정한 모델.

### 08-26. ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

- **식별자**: [arXiv:2307.16789](https://arxiv.org/abs/2307.16789)
- **연도 / 저자·기관**: 2023 / Qin et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ToolLLM`, `ToolBench`
- **요약**: 16,000개 이상의 실제 API를 다루는 도구 사용 데이터셋·프레임워크.

### 08-27. Executable Code Actions Elicit Better LLM Agents

- **식별자**: [arXiv:2402.01030](https://arxiv.org/abs/2402.01030)
- **연도 / 저자·기관**: 2024 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CodeAct`, `code-as-action`
- **요약**: 에이전트의 행동 공간을 실행 가능한 파이썬 코드로 통합하는 CodeAct.

### 08-28. HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

- **식별자**: [arXiv:2303.17580](https://arxiv.org/abs/2303.17580)
- **연도 / 저자·기관**: 2023 / Shen et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `HuggingGPT`, `orchestration`
- **요약**: LLM이 컨트롤러가 되어 다른 AI 모델들을 호출해 과제를 해결하는 구조.

### 08-29. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

- **식별자**: [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)
- **연도 / 저자·기관**: 2023 / Wu et al. (Microsoft)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AutoGen`, `multi-agent`
- **요약**: 여러 에이전트의 대화로 응용을 구성하는 프레임워크.

### 08-30. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

- **식별자**: [arXiv:2308.00352](https://arxiv.org/abs/2308.00352)
- **연도 / 저자·기관**: 2023 / Hong et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MetaGPT`, `SOP`
- **요약**: 소프트웨어 개발 역할(PM, 아키텍트 등)과 표준 작업 절차를 에이전트에 부여.

### 08-31. ChatDev: Communicative Agents for Software Development

- **식별자**: [arXiv:2307.07924](https://arxiv.org/abs/2307.07924)
- **연도 / 저자·기관**: 2023 / Qian et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `ChatDev`, `software-agents`
- **요약**: 가상 소프트웨어 회사 구조의 다중 에이전트 개발 시스템.

### 08-32. CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society

- **식별자**: [arXiv:2303.17760](https://arxiv.org/abs/2303.17760)
- **연도 / 저자·기관**: 2023 / Li et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `CAMEL`, `role-playing`
- **요약**: 역할극 기반 에이전트 간 자율 협업 프레임워크.

### 08-33. Mixture-of-Agents Enhances Large Language Model Capabilities

- **식별자**: [arXiv:2406.04692](https://arxiv.org/abs/2406.04692)
- **연도 / 저자·기관**: 2024 / Wang et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoA`, `ensemble`, `multi-LLM`
- **요약**: 여러 LLM 에이전트를 층으로 쌓고 각 층이 이전 층 출력을 참고해 응답하는 구조. AlpacaEval 2.0 등에서 GPT-4 Omni를 능가한다고 보고(버전별 수치 상이).

### 08-34. Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?

- **식별자**: [arXiv:2502.00674](https://arxiv.org/abs/2502.00674)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `MoA`, `analysis`
- **요약**: 서로 다른 LLM을 섞는 것이 이로운지 되묻는 MoA 재검토 연구(ID·제목만 확인).

### 08-35. A Survey on Large Language Model based Autonomous Agents

- **식별자**: [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)
- **연도 / 저자·기관**: 2023 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `survey`, `agents`
- **요약**: LLM 기반 자율 에이전트의 구성(프로필·메모리·계획·행동)과 응용을 정리한 서베이.

### 08-36. The Rise and Potential of Large Language Model Based Agents: A Survey

- **식별자**: [arXiv:2309.07864](https://arxiv.org/abs/2309.07864)
- **연도 / 저자·기관**: 2023 / Xi et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `survey`, `agents`
- **요약**: LLM 기반 에이전트의 두뇌·지각·행동 구조와 사회적 응용을 정리한 서베이.

## 장기 기억 · 시뮬레이션 · 컴퓨터 사용 에이전트

### 08-37. Generative Agents: Interactive Simulacra of Human Behavior

- **식별자**: [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)
- **연도 / 저자·기관**: 2023 / Park et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `generative-agents`, `memory`
- **요약**: 관찰·반성·계획 구조와 기억 스트림을 가진 에이전트 25명이 가상 마을에서 사회적 행동을 보인 연구.

### 08-38. MemGPT: Towards LLMs as Operating Systems

- **식별자**: [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- **연도 / 저자·기관**: 2023 / Packer et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `MemGPT`, `virtual-context`, `memory-hierarchy`
- **요약**: OS의 가상 메모리처럼 컨텍스트와 외부 저장소 사이를 오가며 제한된 컨텍스트 창을 확장.

### 08-39. Voyager: An Open-Ended Embodied Agent with Large Language Models

- **식별자**: [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)
- **연도 / 저자·기관**: 2023 / Wang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Voyager`, `Minecraft`, `skill-library`
- **요약**: 마인크래프트에서 코드로 된 기술 라이브러리를 축적하며 평생 학습하는 에이전트.

### 08-40. UI-TARS: Pioneering Automated GUI Interaction with Native Agents

- **식별자**: [arXiv:2501.12326](https://arxiv.org/abs/2501.12326)
- **연도 / 저자·기관**: 2025 / Qin et al. (ByteDance)
- **검증 상태**: ✅ 검증(V)
- **태그**: `UI-TARS`, `GUI-agent`, `computer-use`
- **요약**: 스크린샷만 입력으로 받아 키보드·마우스 행동을 출력하는 종단간 GUI 에이전트. OSWorld 24.6(50 스텝), AndroidWorld 46.6 등을 보고.

### 08-41. UI-TARS-2 Technical Report

- **식별자**: [arXiv:2509.02544](https://arxiv.org/abs/2509.02544)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `UI-TARS`, `GUI-agent`
- **요약**: UI-TARS의 후속 기술 보고서(검색 결과 기준 ID와 후속작 관계만 확인).

## 에이전트 벤치마크

### 08-42. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **식별자**: [arXiv:2310.06770](https://arxiv.org/abs/2310.06770)
- **연도 / 저자·기관**: 2023 / Jimenez et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SWE-bench`, `software-engineering`
- **요약**: 실제 GitHub 이슈를 저장소 수준에서 해결하는 능력을 평가하는 벤치마크.

### 08-43. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

- **식별자**: [arXiv:2405.15793](https://arxiv.org/abs/2405.15793)
- **연도 / 저자·기관**: 2024 / Yang et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `SWE-agent`, `ACI`
- **요약**: 에이전트에 맞게 설계된 컴퓨터 인터페이스(ACI)가 소프트웨어 엔지니어링 성능을 높임을 보인 연구.

### 08-44. OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

- **식별자**: [arXiv:2404.07972](https://arxiv.org/abs/2404.07972)
- **연도 / 저자·기관**: 2024 / Xie et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `OSWorld`, `computer-use`
- **요약**: 실제 운영체제 환경에서 멀티모달 에이전트를 평가하는 벤치마크.

### 08-45. WebArena: A Realistic Web Environment for Building Autonomous Agents

- **식별자**: [arXiv:2307.13854](https://arxiv.org/abs/2307.13854)
- **연도 / 저자·기관**: 2023 / Zhou et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `WebArena`, `web-agents`
- **요약**: 현실적인 웹사이트 환경에서 자율 에이전트를 평가하는 벤치마크.

### 08-46. Mind2Web: Towards a Generalist Agent for the Web

- **식별자**: [arXiv:2306.06070](https://arxiv.org/abs/2306.06070)
- **연도 / 저자·기관**: 2023 / Deng et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Mind2Web`, `web-agents`
- **요약**: 여러 도메인의 실제 웹사이트에서 수집한 작업 데이터셋.

### 08-47. GAIA: a benchmark for General AI Assistants

- **식별자**: [arXiv:2311.12983](https://arxiv.org/abs/2311.12983)
- **연도 / 저자·기관**: 2023 / Mialon et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `GAIA`, `general-assistant`
- **요약**: 사람에게는 쉽지만 AI에는 어려운 도구 사용형 질문으로 구성된 범용 비서 벤치마크.

### 08-48. AgentBench: Evaluating LLMs as Agents

- **식별자**: [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)
- **연도 / 저자·기관**: 2023 / Liu et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `AgentBench`, `evaluation`
- **요약**: 여러 환경(OS, DB, 웹 등)에서 LLM의 에이전트 능력을 평가하는 벤치마크.

### 08-49. τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **식별자**: [arXiv:2406.12045](https://arxiv.org/abs/2406.12045)
- **연도 / 저자·기관**: 2024 / Yao et al. (Sierra)
- **검증 상태**: ✅ 검증(V)
- **태그**: `tau-bench`, `pass^k`, `tool-use`
- **요약**: LLM이 시뮬레이션한 사용자와 도메인 API·정책을 가진 에이전트의 대화를 평가(소매·항공). 최종 DB 상태를 정답과 비교하고, 반복 시행 일관성을 재는 pass^k를 도입. gpt-4o급도 50% 미만 성공.

### 08-50. τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment

- **식별자**: [arXiv:2506.07982](https://arxiv.org/abs/2506.07982)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `tau2-bench`, `dual-control`
- **요약**: 사용자도 도구를 쓰는 이중 제어 환경으로 τ-bench를 확장(검색 결과 기준).

### 08-51. BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

- **식별자**: [arXiv:2504.12516](https://arxiv.org/abs/2504.12516)
- **연도 / 저자·기관**: 2025 / Wei et al. (OpenAI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `BrowseComp`, `browsing`
- **요약**: 찾기 어려운 정보를 끈질기게 검색해야 하는 1,266개 질문. 답이 짧아 채점이 쉽다.

### 08-52. BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent

- **식별자**: [arXiv:2508.06600](https://arxiv.org/abs/2508.06600)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `BrowseComp-Plus`, `deep-research`
- **요약**: 딥리서치 에이전트를 더 공정하고 투명하게 평가하려는 BrowseComp 확장(ID·제목만 확인).

### 08-53. MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

- **식별자**: [arXiv:2410.07095](https://arxiv.org/abs/2410.07095)
- **연도 / 저자·기관**: 2024 / Chan et al. (OpenAI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `MLE-bench`, `Kaggle`, `ML-engineering`
- **요약**: 75개 Kaggle 대회로 ML 엔지니어링 에이전트를 평가. o1-preview+AIDE가 16.9%의 대회에서 최소 동메달(ICLR 2025).

### 08-54. AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench

- **식별자**: [arXiv:2507.02554](https://arxiv.org/abs/2507.02554)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `MLE-bench`, `research-agents`
- **요약**: MLE-bench에서의 AI 연구 에이전트의 탐색·일반화를 분석한 연구(ID·제목만 확인).

### 08-55. RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts

- **식별자**: [arXiv:2411.15114](https://arxiv.org/abs/2411.15114)
- **연도 / 저자·기관**: 2024 / Wijk et al. (METR)
- **검증 상태**: ✅ 검증(V)
- **태그**: `RE-Bench`, `AI-R&D`, `human-baseline`
- **요약**: 7개 개방형 ML 연구 엔지니어링 환경과 61명 전문가의 71회 8시간 시도를 비교. 8시간 계산 예산에서 평균 전문가에 근접하나 최상위와는 격차가 있다고 보고(ICML 2025).

## 자기 개선·자동 프롬프트·과학 에이전트

### 08-56. Large Language Models as Optimizers

- **식별자**: [arXiv:2309.03409](https://arxiv.org/abs/2309.03409)
- **연도 / 저자·기관**: 2023 / Yang et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `OPRO`, `prompt-optimization`
- **요약**: LLM이 이전 해답과 점수를 보고 새 해답을 제안하는 최적화(OPRO)로 프롬프트를 개선.

### 08-57. Eureka: Human-Level Reward Design via Coding Large Language Models

- **식별자**: [arXiv:2310.12931](https://arxiv.org/abs/2310.12931)
- **연도 / 저자·기관**: 2023 / Ma et al. (NVIDIA)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Eureka`, `reward-design`
- **요약**: LLM이 로봇 강화학습 보상 함수 코드를 작성·개선해 인간 설계 보상을 능가.

### 08-58. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

- **식별자**: [arXiv:2310.03714](https://arxiv.org/abs/2310.03714)
- **연도 / 저자·기관**: 2023 / Khattab et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `DSPy`, `prompt-compilation`
- **요약**: LM 파이프라인을 선언적 모듈로 기술하고 프롬프트·예시를 자동 최적화하는 프레임워크.

### 08-59. Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution

- **식별자**: [arXiv:2309.16797](https://arxiv.org/abs/2309.16797)
- **연도 / 저자·기관**: 2023 / Fernando et al. (Google DeepMind)
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `Promptbreeder`, `evolution`
- **요약**: 프롬프트와 변이 프롬프트를 함께 진화시키는 자기 참조적 개선.

### 08-60. Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation

- **식별자**: [arXiv:2310.02304](https://arxiv.org/abs/2310.02304)
- **연도 / 저자·기관**: 2023 / Zelikman et al.
- **검증 상태**: 🔶 기억기반(M)
- **태그**: `STOP`, `recursive-self-improvement`
- **요약**: 스캐폴딩 프로그램이 자기 자신을 재귀적으로 개선하는 코드 생성 시스템.

### 08-61. TextGrad: Automatic Differentiation via Text

- **식별자**: [arXiv:2406.07496](https://arxiv.org/abs/2406.07496)
- **연도 / 저자·기관**: 2024 / Yuksekgonul et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `TextGrad`, `textual-gradient`
- **요약**: LLM의 자연어 피드백을 ‘기울기’처럼 역전파해 복합 AI 시스템의 구성요소를 최적화. GPQA에서 GPT-4o 제로샷 51→55% 등을 보고.

### 08-62. Automated Design of Agentic Systems

- **식별자**: [arXiv:2408.08435](https://arxiv.org/abs/2408.08435)
- **연도 / 저자·기관**: 2024 / Hu, Lu, Clune
- **검증 상태**: ✅ 검증(V)
- **태그**: `ADAS`, `meta-agent`, `agent-design`
- **요약**: 메타 에이전트가 코드로 새 에이전트를 설계·발견하는 연구 분야 제안. 발견된 에이전트가 수작업 설계를 코딩·과학·수학 과제에서 앞섰다고 보고.

### 08-63. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

- **식별자**: [arXiv:2408.06292](https://arxiv.org/abs/2408.06292)
- **연도 / 저자·기관**: 2024 / Lu et al. (Sakana AI)
- **검증 상태**: ✅ 검증(V)
- **태그**: `AI-Scientist`, `automated-research`
- **요약**: 아이디어 생성·문헌 조사·실험·논문 작성·동료 평가까지 ML 연구 전 과정을 자동화하는 프레임워크.

### 08-64. Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

- **식별자**: [arXiv:2505.22954](https://arxiv.org/abs/2505.22954)
- **연도 / 저자·기관**: 2025 / Zhang et al.
- **검증 상태**: ✅ 검증(V)
- **태그**: `DGM`, `self-modifying-agent`, `open-ended`
- **요약**: 증명 대신 경험적 검증으로 자기 코드를 수정·진화시키는 에이전트. 아카이브 기반 탐색으로 SWE-bench 성능을 20.0%→50.0%로 올렸다고 보고.

### 08-65. Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

- **식별자**: [arXiv:2510.21614](https://arxiv.org/abs/2510.21614)
- **연도 / 저자·기관**: 2025 / -
- **검증 상태**: ✅ 검증(V)
- **태그**: `HGM`, `self-improvement`
- **요약**: DGM을 이은 자기 개선 코딩 에이전트 연구. 검색 결과상 SWE-bench Verified·Polyglot에서 DGM을 앞선다고 인용됨.
