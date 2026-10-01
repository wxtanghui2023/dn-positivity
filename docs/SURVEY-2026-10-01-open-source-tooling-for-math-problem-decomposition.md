# SURVEY-2026-10-01 — 数学课题**拆解/架构**类开源工具选型（唐先生 12:12 令）

结论: 已查地图：命中 3 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 工具链选型（非数学命题；不主张任何新值）
D1: 0

## §0 问题诊断（我方真实失效模式）

$$\text{昨夜到今晨之反复，\textbf{不是算力不足}，而是三层缺失}:\ \textbf{(a) 定义漂移}\ (L_q\ \text{错对象、}R/U\ \text{混用、}X_L\ \text{四次}) ✓;\ \textbf{(b) 无强制依赖结构}\ (\text{断言/路线未成 DAG} ✓);\ \textbf{(c) 无机器校验层} ✓$$
$$\Longrightarrow\ \text{故工具选型须**对症**这三层，而非"再找个更强的模型"}\ ✓$$

## §1 结构/依赖图类（对症 (a)(b) —— **最优先**）

| 工具 | 是什么 | 适配 | 代价 |
|---|---|---|---|
| **leanblueprint** (github.com/PatrickMassot/leanblueprint) | plasTeX 插件；LaTeX 里写 `\uses{}`/\leanok`，自动生成**定义/引理/定理依赖图 + 完成度** | **最贴合**；PFR(Tao)、Liquid Tensor(Scholze)、PrimesGapLib(Axiom) 均用 | 中：需把断言写成 LaTeX；**可脱离 Lean** ✓ |
| **plasTeX depgraph**（leanblueprint 之底层，非-Lean） | 通用 LaTeX 依赖图 | 若只想画图不碰 Lean ✓ | 低 |
| **LeanArchitect** (arXiv 2601.22554) | 从 Lean 代码直接抽取 blueprint 数据（声明式标注＋自动依赖＋LaTeX 同步） | 只在形式化后用 | 中 |
| **Lean Atlas** (arXiv 2604.16347) | 交互式 Web 依赖图；边分 **8 类**；**Lean Compass** 抽出"语义正确性会影响目标定理"的节点 | **对症 (c) 语义幻觉** ✓✓ | 中 |

## §2 证明分解/子目标智能体类（对症 (c)）

| 工具 | 是什么 | 适配 | 代价 |
|---|---|---|---|
| **QED** (arXiv 2604.24021) | **开源多智能体**，对**未解问题**产出自然语言证明，专家验证原创性 | **与我方场景最像**（非形式化、开放问题） | 高（读＋复现） |
| **ARIA** (arXiv 2510.04520) | 依赖图驱动的**两阶段 Graph-of-Thought** + RAG + AriaScorer；把命题拆成**层级依赖图** | **正是"拆解"** ✓✓ | 高 |
| **DeepSeek-Prover-V2** (github.com/deepseek-ai/DeepSeek-Prover-V2) | 递归**子目标分解** + RL；7B/671B 开源权重；MiniF2F 88.9% | 若形式化：论文级子目标拆分 | 中（API 可用；671B 本地不可行 ✗） |
| **Numina-Lean-Agent** (arXiv 2601.14027) | 开源通用 agentic 形式化系统；Putnam2025 全 12 题；支持 "vibe proving" | 交互式形式化助手 | 中 |
| **AxiomMath/IMO2026, putnam2025** | MIT 许可的**成果仓库**（含 blueprint） | 学其**方法论**（prover 本体闭源 ✗） | 低（只需读） |

## §3 论证/路线结构类（对症 (b)：我方 CLOSED-ROUTES-MAP / ASSETS / ID-CLAIMS）

| 工具 | 是什么 | 适配 |
|---|---|---|
| **Argdown** (github.com/christianvoigt/argdown) | markdown 式**论证图**语言（pro/con 关系 → 图）；VS Code 扩展＋CLI | **与我方 .md 档案天然兼容** ✓（把路线/断言画成论证图） |
| Argunet / Araucaria / OVA / AGORA-net / Kialo | 更老的论证图工具 | 一般（重、非 markdown） |

## §4 关键的**方法论**信号（比工具更重要 ✓✓）

$$\textbf{Axiom 的三段式（build 246 定理）}:\ \text{(1) 先写 blueprint —— 每个定义/引理/定理给\ \textbf{标签＋精确陈述＋依赖表} → 生成依赖图，**用来排序工作**};\ \text{(2) 多智能体生成 Lean};\ \text{(3) 人工复核＋整理为库} ✓$$
$$\Longrightarrow\ \text{**"先蓝图、后证明"** 正是唐先生所说"完整架构与逻辑"之形状}\ ✓✓\ \text{（我方档案已有雏形：ID-CLAIMS.tsv／ASSETS-REGISTRY／CLOSED-ROUTES-MAP ⟹ 缺的是\ \textbf{依赖边＋状态＋图}} ✓)$$

## §5 建议落地顺序（含代价与判据）

$$\textbf{P0（今天／零依赖）}:\ \text{把 107 线之断言（}C\text{-}/V\text{-}/F1\text{–}F9/\text{引理）写成 \textbf{blueprint 依赖图}（先用 plasTeX depgraph 或直接由 }ID\text{-}CLAIMS.tsv\ \text{生成 \textbf{mermaid/dot}}）⟹ \text{立刻可见\ \textbf{关键路径}＋哪些断言悬空} ✓$$
$$\textbf{P1（1–2 天）}:\ \text{装 \textbf{Mathlib}（Lean 4.33 已装 ✓）＋把\ \textbf{四步引理}与}e_{\max}\text{ 之定义\ \textbf{形式化}} ⟹ \text{机器校验，杜绝定义漂移} ✓$$
$$\textbf{P2（研究级）}:\ \text{按 \textbf{ARIA／QED} 架构搭"依赖图规划器＋RAG 接地＋评分器"之开放问题流程} ✓$$
$$\textbf{判据}:\ \text{若 P0 之依赖图能指出\ \textbf{悬空断言}（无上游支撑者）}\ge1\ \text{且与昨晚"需求侧未建立"一致 ⟹ 即刻验证工具价值} ✓;\ \text{否则工具只是装饰} ✗$$

## §6 边界与纪律

$$\textbf{(D1)}\ \text{不主张任何数学新值} ✓;\ \textbf{(D2)}\ \text{检索源为 Tavily（Firecrawl 额度耗尽 ✗，本地无数学类 Skill ✗）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## §7 【技术词回查】

```
技术词 依赖图        命中文件数=14   :: ./P2-COLLISION-2026-09-27-verified-counterexample-to-the-beta-shape.md ./ASSETS-REGISTRY.md ./STRATEGY-2026-09-16-break-the-wall-methodology.md 
技术词 蓝图台账     命中文件数=0    :: 
```
$$\textbf{分类}：\textbf{本档新增}：\text{"蓝图台账"若仅本档则为新} ✓;\ \textbf{档案已有}：\text{"依赖图"若多档则引用} ✓;\ \textbf{通用词（不计）}：\text{"开源／工具链"裸词} ✓$$
