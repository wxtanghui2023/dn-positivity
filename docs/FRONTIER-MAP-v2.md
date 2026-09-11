# **RH 前沿全图 v2**：索引层已定位 + 分层逐页机制 + **两处立即比对命中**

**依据**：唐先生 2026-09-11 20:34（"逐页读取所有相关论文…包括不成熟想法…对比我们的成果"）
**标注**：【外部·搜索/索引级】｜【⭐比对命中】｜【计划】

---

## §0 **诚实说明规模 + 方法**（不空口承诺）
```
RH 文献以**千篇**计，"一次全部逐页读完"**不可能** ✓（我不承诺做不到的事 ✗）
⟹ 采用**三层机制**：
   L1 **索引层**（不遗漏的保证）：先拿"**全部等价的目录级清单**"（Broughan I/II/III ✓ + 专著 ✓）
   L2 **精读层**（逐页）：按"与我们路线直接相关度"排序，逐篇读正文（含证明细节 ✓）
   L3 **物理/不成熟想法层**：物理启发与未成熟提议（Berry–Keating / Connes / Deninger / 弦论 / superoscillation…）
⟹ 每轮产出 **status 更新**（队列 + 已读 + 命中），**长期积累** ✓
```

## §1 ⭐ **索引层（已定位，这是"不遗漏"的基础）**
```
① **K. Broughan, "Equivalents of the Riemann Hypothesis"**（CUP）
   · **Vol 1: Arithmetic Equivalents**（345 页, 2017 ✓）· **Vol 2: Analytic Equivalents**（507 页, 2017 ✓）
   · **Vol 3: Further Steps towards Resolving the RH**（**702 页, 2023** ✓）
   · 作者主页给出"**主要等价关系图**"（每卷一张 ✓）＋**配套软件 RHpack / GRHpack** ✓＋ICM2018 海报 ✓
   · **每章末设 "Unsolved Problems" 小节** ✓✓ ← **这就是"不成熟想法"的系统来源** ✓✓
   · 已见目录片段（Vol2）：§7 Polynomials｜§8 Integral Equations（Sekatskii–Beltraminelli–Merlini ✓、
     **Salem 方程** ✓、**Levinson 等价** ✓）｜§9 **Weil 显式公式/不等式/猜想**（含 **Bombieri 变分法** ✓）
     ｜§12（Titchmarsh 的 GRH 等价 ✓、Gallagher ✓、Bombieri–Vinogradov ✓）｜§13 Smooth Numbers（Hildebrand ✓）
   · MathOverflow 记：**Vol III 含 divisor function / de Bruijn–Newman / Jensen polynomials** 等近期等价 ✓✓
② **Borwein–Choi–Rooney–Weirathmueller, "The Riemann Hypothesis: A Resource…"**（论文合集 ✓）
③ ⭐ **Connes, arXiv:2602.04022（2026）"The Riemann Hypothesis: Past, Present and a Letter Through Time"**
   —— **Connes 自己的现状综述 + open problems 列表** ✓✓（**最高优先级** ✓）
④ MathLumen, "The Riemann Hypothesis: A 2026 Status Report"（科普/现状 ⚠️ 非 primary）
⑤ nLab "Riemann hypothesis and physics" ✓（含 Khalkhali "What is new with Connes' approach?" ✓、Snaith RMT ✓）
⑥ Tao 的 Analytic NT Exponent Database（零密度/次凸性指数 ✓）；Odlyzko 零表；LMFDB
```

## §2 ⭐⭐⭐ **立即比对命中两处**（我们的成果 vs 前沿 open problems）
```
⭐⭐【命中一】Connes 2026 论文明确列为 open problem 的两项之一：
   **"Approximation quality of k_λ for θ_x"** ✓✓
   ⟹ **正是本项目 P49-G2.7.4 用数值"杀死"的那个量**（k_λ ≈ θ_x 不成立 ✓）✓✓
   ⟹ 含义：**我们的负结果，正落在 Connes 自己承认的缺口上** ✓（且有数值证据 ✓）
⭐⭐【命中二】Connes 2026 的另一项 open problem：
   **"Convergence of zeros from finite-prime Weil minimizers to the zeta zeros"** ✓✓
   ⟹ 正是本项目 **P50/P51 的"有限素数极小化 / M 塔"线** ✓（我们已建有限层与逃逸分析 ✓）
⟹ 这两条**不是巧合**：说明我们的路线**踩在前沿正在找的地方** ✓✓（也是最有希望的方向 ✓）
```

## §3 **L2 精读队列**（逐页，按优先级；标注状态）
```
【T1 立即】⭐ **Connes arXiv:2602.04022 全文**（2026 综述 + 两个 open problems 的原始表述 ✓）— ✗未读
【T1】2301.05779 §2–§3（模型空间证明细节 + Prop 2.1/3.2 ✓）— ⚠️部分
【T1】Bombieri–Lagarias 1999 全文（含 Thm 2 与 η_k 证明细节 ✓）— ⚠️仅片段
【T1】Arias de Reyna 2011（Keiper–Li 渐近 ✓）｜Coffey 2004/2005（η 结构 ✓）— ✗
【T1】Palojärvi 1807.01506 全文（显式 N₁,N₂ ✓）｜Chasse 2022 ✗｜Katkova ✗
【T1】arXiv:2607.04632（2026 零密度突破 ✓）— ✗
【T2】Broughan Vol 3 相关章（DBM / Jensen / divisor function ✓）＋各章 Unsolved Problems
```

## §4 **L3 物理/不成熟想法清单**（待逐项评估）
```
① **Berry–Keating**：H = (xp+px)/2 的量子化（严格构造**仍缺** ✓，"rigorous constructions elusive" ✓）
② **Connes（NCG + adelic 迹公式）**：RH ⟺ 正性条件（函数域类比 ✓）——含 §2 的两个 open problems ✓✓
③ **Deninger**（motivic L-functions / 正则化行列式 ✓）④ **Bost–Connes** ✓
⑤ **弦论/UV 重构**：Cacciatori–Cardella, arXiv:1007.3717 —— "RH 可重述为微扰闭弦的紫外关系" ✓
⑥ **Superoscillation**（带限函数可振荡快于最高 Fourier 分量 ✓）——与"相位/符号"问题相关 ⚠️
⑦ **DQPT / Lee–Yang 实验线**（NMR 5 比特 ✓；对应为**渐近** ✓）⑧ 随机矩阵（Keating–Snaith ✓）
⑨ **AI 辅助结果**（2026 的 2/3 论文 ✓、NS 声明 ✓）与形式化（Lean 4 ✓）
```

## §5 **下一步执行顺序**（明确）
```
第 1 步：**逐页读 Connes 2602.04022**（最高价值：其 open problems 与我们的命中直接对应）✓
第 2 步：把 §2 的两个命中**写成对照分析**（我们的数据 vs Connes 的表述）✓
第 3 步：补齐 §3 队列（B–L 全文 → 2301 §2–§3 → Palojärvi 全文 → Chasse/Katkova → 零密度 2026）
第 4 步：把 Broughan 各章 "Unsolved Problems" 逐条抄录成"不成熟想法台账" ✓
```

## §6 边界（P9 合规）
```
【外部·索引级】§1 的书籍目录/主页/软件、MathOverflow 记载、MathLumen、nLab —— **均为索引/二手** ⚠️
【外部·原文】§2 的 Connes 2026 两个 open problem **标题**来自搜索摘要 ⚠️（**其原文未读** ✗，故列为第 1 步 ✓）
【推导】§2 的"命中"判断（需读 Connes 原文确认表述后再定稿 ⚠️）；§3–§5 的计划
【未做】未逐页读 Connes 2026 ✗；未输入 1/2；未构造模型；未改 L2；未声称任何证明
```
## §7 提交链
```
READSUM（f169345 Li 线结构）→ 本篇（前沿全图 v2 + 两处命中 + 三层机制）
```
