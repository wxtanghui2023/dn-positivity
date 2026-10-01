结论: 已查地图：命中 139 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 文献登记（前沿论文/AI 突破/跨领域方法）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (文献登记)

# LITERATURE-REGISTRY — 前沿文献总账（RH 线 ＋ 119 线 ＋ AI 突破 ＋ 跨领域方法）

> 唐先生 2026-10-01 14:11 指出：**这一层一直没归纳** ✗ ⟹ 本档补。
> 建档方式：**grep 全档**（arXiv 编号／引用键／期刊名）→ 抽上下文定题名与用途 → 归行。
> **诚实限定** ⚠️：本档为**首遍**（据 grep 证据）；每条之"我方结论"需逐档复核，未复核者标 `(待复核)`。

## §0 规模（grep 实测）

| 指标 | 数量 |
|---|---|
| arXiv 编号（去重） | **26+**（最高 `arXiv:2608.13637` **76 次**、`1807.01506` 29、`2607.04632` 23、`2410.03673` 18） |
| 引用键 `[Xxx00]` | **30+**（`[Bom00]` **31**、`[BGSTB24]` **28**、`[Bom03]`/`[Ary22]` 10） |
| 期刊/会议 | J. Combin.(17)｜J. Number Theory(13)｜Inventiones(6)｜Math. Ann.(5)｜**JAMS(4)**｜Duke(4)｜**IEEE TIT(7)**｜Acta Math.(1)｜Acta Arith.(1) |

## §1 RH 线（空间 A）：已研究之前沿

| 文献 | 类型/出处 | 我方用途 | 我方结论 |
|---|---|---|---|
| **arXiv:2608.13637** "More than two thirds of the zeta zeros are simple and on the critical line"（2026-08，21 页，**署名 Claude**，专家注 Alpöge–Furman） | 2026 前沿（AI 参与） | **全文精读**（§1.2/§1.6/§2.3/§4/§7.2/§B.3/§B.5）；`V184` 分诊＋`V185` 精读＋`V186` 反向拆解 | **0.6725/0.68185 天花板＝我方 0.682 同一堵墙** ✓；取胜动作＝(Z)分块＋(P)HS＋(L)rank–trace ✓ |
| **arXiv:1807.01506** Palojärvi, "Explicit zero-free regions and a τ-Li-type criterion"（v3, 26 页） | 期刊级；**PDF 已归档** | τ-Li 判据族；`E4`；Thm 2.1/2.3/4.1 逐字对齐 | 判据可用；**未见 $10^5$ 数值验证** ✗（纠错一处） |
| **arXiv:2607.04632** Turnage-Butterbaugh 综述 "A decades-long breakthrough in zero-density estimates…"（2026 JMM；BAMS 待刊） | **综述** | 零密度 SOTA；N(σ,T)≪T^{15(1−σ)/(3+5σ)+ε} | **新入口候选** ✓；L∞ vs 平均二分 ✓ |
| **arXiv:2602.04022** Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time"（42 页，J. Open Math. Problems 2(1) 2026） | 顶刊/综述 | 三轮读毕；Weil 二次型极值化；只用素数<13 ⟹ 前 50 零点 2.6e−55~1e−3 | 极值化路线；**我方纲领③模型对齐** 相关 ✓ |
| **arXiv:2606.06604** Connes–Consani, "On the Absolute Geometry of Spec Z"（30 页） | math.AG/math.NT | `V249` 分流＋`V250` 全文精读 | **canonicity 有真进展** ✓（模空间/泛性） |
| **arXiv:2410.03673** "Quasicrystal Scattering and the Riemann Zeta Function"（2024） | 跨领域（准晶体） | `E28`/`A5-1` 模型对齐 | 项目自认**唯一带 β 通道的构造** ✓；测量≠证明 ✗ |
| **arXiv:2411.16777** "2D Ising ⟺ ζ 零点分布" | 跨领域（统计物理） | `E39`/`E39b`/`B5` **全文审计** | **未建立其主张** ✗（用我方 TP₅ 负子式装置） |
| **arXiv:2306.04799** BGSTB "An unconditional Montgomery theorem for pair correlation"（= Acta Arith. 214(2024) 357–376） | 期刊 | 无条件对相关；有限阶 G(K)≤0 定理 | 有增益但**已饱和** ✗ |
| **arXiv:2501.14545** BGSTB "Pair correlation … I: proportions of simple zeros and critical zeros" | 预印本 | **直接前驱**（比例） | 无三阶/高阶矩 ✗ |
| **arXiv:2609.02882** Lamzouri 2026（17 页） | 2026 前沿 | 三阶矩；Tsang 核与带宽条件 | **新无条件证明** ✓ |
| `arXiv:2609.07918` Biao Wang｜`arXiv:2608.16034` Hua–Yang | 2026 后续 | 三篇 2608.13637 后续 | **全部仍停在 k=2/MT 常数** ✗ |
| 引用键 **[Bom00]/[Bom03]** Bombieri（×31/×10） | — | 有限逼近；**自曝重发现：P27 = Bombieri** ⚠️ | 经典机制 ✓ |
| 引用键 **[Mon73]** Montgomery｜**[RS96]** Rudnick–Sarnak｜**[IK04]** Iwaniec–Kowalski｜**[Nik95]**｜**[Yos92]**｜**[DFI95/97]**｜**[CCLM17]**｜**[CGdL20]**｜**[Ary22]**｜**[BS04]**｜**[DFMR13]** | 经典/期刊 | 对关联、谱理论、解析数论工具 | (待复核) |

## §2 119 线（空间 B）：已研究之前沿

| 文献 | 出处 | 我方用途 | 我方结论 |
|---|---|---|---|
| **arXiv:2608.12595** Sac Himelfarb–Schwartz, "On Nearly-Perfect Covering Codes Beyond Radius One"（2026） | 预印本 | **van Wee 原式（equ (5)）逐字来源**；n=10⟹103 | 免费可得 ✓；界面已在档（AUDIT-28q） |
| **arXiv:2203.16901** Wu–Chen, Discrete Math 347(2) 2024 | **期刊** | 外部权威读数：γ(Q_n)≥2^n/n（Van Wee 1988） | **只处理 n≡0 mod 6 ⟹ n=10 不在内** ✗ |
| **Gijswijt–Polak 2025（SDP-3）** | 2025 | 三阶松弛 ⟹ 105.2223⟹**106** | **是松弛** ⟹ 天花板，**不可能给 107** ✓✓ |
| **BÖW 2004**（J. Combin. Des. 12:157–176） | 期刊 | 混合码 general R=1 ⟹ **107** | **全文不可得** ⟹ 列为★假设 ✗ |
| **Zhang 1991/92**（IEEE TIT 37:573–582） | 期刊 | pair/triple 覆盖不等式 ⟹ 105 | 已被更精细法超越（仅 K(12,3)≥18 未破） |
| **Kéri 2009 博士论文**（匈牙利语，**全文在档** ✓） | 学位论文 | K(10,1) 阶梯＋坐标式构造算法 | 方法包络 $M\lesssim20$ ⟹ **不能产出 107** ✗ |
| **Haas 2008**（超量法，**全文在档** ✓）｜Haas 2000/2002/2013 | 学位/期刊 | 超量法上限；条件 (q)＋超量矩阵 | n=10 处**全部 ≤103** ✗ |
| **Östergård–Blass 2001**（IEEE TIT 47:2556） | 期刊 | 子空间分布＋LP ⟹ K(9,1)=62 | 适用但**n=10 不可行** ✗ |
| **van Wee 1988／Struik 1994**（IEEE TIT） | 期刊 | 超量法原式 ⟹ 103 | 我方自导 103 ✓ |
| **van Lint–van Wee 1991**（JCTA 57:130–143）｜**Palojärvi**（119 无关） | 期刊 | 混合码一般界 | (10,0)⟹102.4⟹103 ✗ |
| **LJCR / dmgordon 数据库**（difference sets、coverings） | 数据库 | DS(243,121,60) 空格；覆盖设计表 | 审计＝NO-GO 家族 ✓；DS243 降级归档 |
| 引用键 **[BGSTB24/25]**（同 §1）｜**[DFMR13]**｜**[Ary22]** | — | 交叉引用 | (待复核) |

## §3 近年 **AI 突破**（须单列 ✓）

| 系统 | 出处/年份 | 做了什么 | 我方相关性 |
|---|---|---|---|
| **AlphaProof / AlphaGeometry** | DeepMind 2024/25 | IMO 级形式化推理 | 竞品基线 |
| **AxiomProver**（Axiom Math） | 2026 | **246 素数间隙定理**形式化；Putnam 2025 全 12 题；三段式：**先 blueprint → 多智能体生成 Lean → 人工复核** | **方法论可借** ✓✓ |
| **QED**（arXiv 2604.24021，开源） | 2026 | plan–prove–verify–regulate；18 项目→5 原创（3 项达期刊难度） | **流程可借** ✓ |
| **DeepSeek-Prover-V2**（开源，arXiv 2504.21801） | 2025 | 递归子目标分解；MiniF2F 88.9% | 可 API 用 |
| **Seed-Prover 1.5**｜**Kimina-Prover**｜**Numina-Lean-Agent**（Putnam 全 12）｜**Aristotle**（Harmonic）｜**Aletheia** | 2025–26 | 形式化/自然语言证明 | 对比基线 |
| **AlphaEvolve / FunSearch** | DeepMind 2024/25 | 进化搜索发现构造（改进已知界） | "构造 ≠ 证明"之判例 |
| **Gijswijt–Polak SDP-3** | 2025 | 见 §2 | **直接决定我方 106 的机制** ✓✓ |
| **OpenMath**（zhuhaichao518，2 天龄） | 2026-09-29 | 证明图＋信任边界（四量分离／防循环自证） | 已 fork 三件 ✓ |

## §4 跨领域／顶刊方法来源

| 领域 | 文献/工具 | 借入之方法 |
|---|---|---|
| 统计物理 | arXiv:2411.16777（2D Ising） | 审计对象（未建立） |
| 准晶体散射 | arXiv:2410.03673 | β 通道模型对齐 |
| 超分辨/信号处理 | Gabor／STP 可辨识性；FRI／Blu–Urigüen；Kloos–Stöckler | 有限分辨率/盲类阈值 |
| 知识组织 | OMDoc／sTeX；Stacks Project（21,446 tags）；KnowTeX；leanblueprint／LeanArchitect／Lean Atlas | 依赖图／柔性形式化／零标注抽取 |
| 论证结构 | Argdown／Argunet／Araucaria | 路线论证图 |
| 智能体编排 | LangGraph／CrewAI／AutoGen | 可执行 DAG |

## §5 尚未归纳（诚实待办 ⚠️）

1. **题名待补**：`arXiv:2006.08503`、`2608.19872`、`2511.23257`、`2204.01036`、`2008.07206`、`2504.01932`、`1910.01227`、`1801.08442`、`2608.12315`、`2211.14918`、`2203.14950`…
2. **引用键 30+ 未逐条注**：`[DFMR13]`、`[CGdL20]`、`[CCLM17]`、`[DFI95/97]`、`[Yos92]`、`[RS96]`、`[IK04]`…
3. **"读过／未读"未标**：项目档内已有 `🔵 待资料／✗ 未读` 标记，本档**未逐条继承** ⟹ 待按档补
4. **每课题应各出一份**：本档为**总账**；`topics/<代号>/LITERATURE.md` 待随课题建档生成

## §6 边界与纪律

$$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{题名与用途取自 grep 上下文（可复核）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=DUPLICATE  <其余>=NEW

## §7 题名补齐（arXiv API 实取 ✓ 2026-10-01）

| 编号 | 题名 | 作者 |
|---|---|---|
| `arXiv:1801.08442` | Limit Operators, Compactness and Essential Spectra on Bounded Symmetric Domains | Raffael Hagger |
| `arXiv:1910.01227` | Jensen Polynomials for the Riemann Xi Function | Michael Griffin, Ken Ono, Larry Rolen et al. |
| `arXiv:2006.08503` | The second moment of $S_n(t)$ on the Riemann hypothesis | Andrés Chirre, Emily Quesada-Herrera |
| `arXiv:2008.07206` | Jensen polynomials are not a plausible route to proving the Riemann Hypothesis | David W. Farmer |
| `arXiv:2203.14950` | On the Montgomery--Vaughan weighted generalization of Hilbert's inequality | Wijit Yangjit |
| `arXiv:2204.01036` | From asymptotic to closed forms for the Keiper/Li approach to the Riemann Hypothesis | André Voros |
| `arXiv:2211.14918` | On the number variance of zeta zeros and a conjecture of Berry | Meghann Moriah Lugar, Micah B. Milinovich, Emily Quesada-Herrera |
| `arXiv:2504.01932` | Semidefinite lower bounds for covering codes | Dion Gijswijt, Sven Polak |
| `arXiv:2511.23257` | Quadratic Forms, Real Zeros and Echoes of the Spectral Action | Alain Connes, Walter D. van Suijlekom |
| `arXiv:2608.12315` | On the optimal constant in the Montgomery-Vaughan weighted Hilbert inequality | Brad Rodgers |
| `arXiv:2608.19872` | New upper and lower bounds on covering codes K_q(n,R) for alphabets of size 5 &lt;= q &lt;= 21 | Mark Marosi |

> 上表 11 条原为 §5-1 之待办 ⟹ 已补齐 ✓；§1/§2 表内其余编号题名取自档案上下文（可复核）。
