# SURVEY-2026-10-01b — **通用**数学课题分析/拆解开源项目（按类别；**非**课题专用）

> 前档 `SURVEY-2026-10-01-open-source-tooling...` 以我方 107 线为靶，**偏题** ✗；本档按唐先生 12:16 更正：面向**数学课题本身**之通用项目 ✓

结论: 已查地图：命中 108 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 通用工具/框架调研（非数学命题；不主张任何新值）
D1: 0

## §1 (A) 全形式化系统与库（全通用）

| 项目 | 说明 |
|---|---|
| **Lean 4 + Mathlib** (github.com/leanprover-community/mathlib4) | 现代主力；190 万行；模块＝DAG |
| **Isabelle + AFP** (isa-afp.org) | Archive of Formal Proofs：数千条目、可检索 |
| **Rocq/Coq + Mathematical Components** | ssreflect 风格 |
| **Mizar + MML** / **Metamath set.mm** / **HOL Light** | 老牌全形式库；MML 有完备依赖 |

## §2 (B) 语义/**柔性形式化**文档框架 ★最贴近"分析数学课题"★

| 项目 | 说明 |
|---|---|
| **OMDoc** (omdoc.org) | 数学知识之**语义标记格式**：theory/statement/proof 层＋**结构化依赖**（inclusion 之 `via`）＋元数据；**明确支持"柔性形式化"**："结构性质**逻辑无关**，无须承诺某一逻辑系统" ⟹ 半形式化即可获得知识管理服务 ✓✓ |
| **sTeX** (kwarc.info, Kohlhase) | LaTeX 前端 → OMDoc；语义宏 → 依赖图/术语表/柔性形式化 |
| **MathML / OpenMath** | 公式层标准（OMDoc 之上游） |
| SWiM 类**语义 wiki** | OMDoc 之上的协作式数学知识库 |

## §3 (C) 大型**非形式**数学体＋依赖图（可复制之范式）★

| 项目 | 说明 |
|---|---|
| **Stacks Project** (stacks.math.columbia.edu) | **21,446 tags**；每个定义/引理/命题/定理**有 tag**，证明中以 tag 互引；**官方 API 动态生成 tag 依赖图（d3.js）**，按类型着色、可只看"某结果所依赖之子图" ✓✓ ⟹ 证明"巨型非形式数学体＋自动依赖图"**可行** |
| **Kerodon**（Lurie） | Stacks 模式之类比 |
| **nLab** | 语义链接式 wiki |

## §4 (D) 蓝图/依赖图工具（通用）

**leanblueprint**（github.com/PatrickMassot/leanblueprint；plasTeX 插件，`\uses`/\leanok` → 依赖图＋完成度；**可脱离 Lean** ✓）｜**plasTeX depgraph**（通用 LaTeX 依赖图）｜**LeanArchitect**（arXiv 2601.22554）｜**Lean Atlas**（arXiv 2604.16347；边分 8 类＋Compass）

## §5 (E) LLM×数学 通用工具箱/智能体

| 项目 | 说明 |
|---|---|
| **LeanDojo / LeanDojo-v2** (leandojo.org) | **通用 Lean 交互＋数据抽取**：file deps、AST、proof states、tactics、**premises**；程序化交互；98,734 定理基准；v2 端到端（Pantograph、SFT/GRPO/Retrieval trainers、HF 微调、外部推理 API）✓✓ |
| **Pantograph** | Lean 4 交互接口（v2 用之） |
| **DSP / DSP+**（Draft-Sketch-Prove） | **子目标分解**范式（sketch → 各子目标独立攻 → 组装） |
| **ARIA** (arXiv 2510.04520) | **依赖图驱动**之 Graph-of-Thought 形式化＋RAG＋Scorer |
| **QED** (arXiv 2604.24021) | 开源多智能体，对**未解问题**产出自然语言证明 |
| **DeepSeek-Prover-V2** / **Goedel-Prover** / **Kimina-Prover** | 开源权重之 Lean 证明模型 |
| **神经符号通用框架** | LLM-Modulo、Logic-LM、SymbOLM/CLOVER、SatLM、SymbCoT（分解＋外部求解器校验） |

## §6 (F)(G)(H) 断言结构 / 编排 / 知识库

**Argdown**（markdown 论证图，CLI＋VS Code）｜Argunet／Araucaria／OVA／AGORA-net；
**LangGraph**（MIT，图状态机＋checkpoint＋human-in-the-loop）｜CrewAI｜AutoGen／MS Agent Framework；
**zbMATH Open**（开放 API）｜**OEIS**｜**LMFDB**｜**swMATH**｜**DLMF**

## §7 诚实判断（关键 ✓）

$$\textbf{\text{不存在现成的"通用数学课题分析器"}}\ ✗\ \text{；领域分两支}:\ \textbf{(形式支)}\ A/D/E\ \text{—— 需全形式化，机器可校验，成本高};\ \textbf{(柔性支)}\ B/C/F\ \text{—— **不要求全形式化**，只标注结构} ✓$$
$$\Longrightarrow\ \text{要"分析/拆解数学课题"（不先形式化），**只有柔性支**}\ ✓;\ \text{而其中\ \textbf{(B) OMDoc/sTeX}\ 与\ \textbf{(C) Stacks tag 图}\ 是真正通用且可复制者}\ ✓✓$$

## §8 与本线相关之三项通用工具（非课题专用 ✓）

$$\text{① **OMDoc/sTeX**}:\ \text{柔性形式化＋theory inclusion 依赖 ⟹ 可直接承载"断言-依赖"层};\quad \text{② **Stacks tag 图工具链**}:\ \text{验证"巨型非形式数学体＋自动依赖图"可行};\quad \text{③ **LeanDojo-v2**}:\ \text{若须机器校验关键引理，则通用 Lean 交互/训练/检索框架}\ ✓$$

## §9 边界与纪律

$$\textbf{(D1)}\ \text{不主张任何数学新值} ✓;\ \textbf{(D2)}\ \text{检索源 Tavily（Firecrawl 额度耗尽 ✗）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## §10 【技术词回查】

```
技术词 柔性形式化  命中文件数=0    :: 
技术词 知识表示     命中文件数=0    :: 
```
