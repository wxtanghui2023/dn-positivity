# 物理前沿侦察（2026-09-12）—— 五个方向的文献检索与机制审计

**任务**：为"从理论物理借思想"的 RH 研究计划做一次聚焦文献侦察，找出**可能携带 β（实部）信息的、可核验的机制**。
**纪律依据**：`00-ANCHOR-purpose-and-discipline.md`（要理解，不要战绩；要可核验；先查先行者）、
`DECLARATION-2026-09-11-AI-MISALIGNMENT.md`（体量 ≠ 理解）、`MASTER-NOGO-AND-LIVE-PATHS.md`（T1–T10 陷阱筛）。
**本项目立场**：最有价值的成果是**否定结果与结构律**；本轮同样以**诚实的负面结论**为主要交付。

---

## §0 本文件的自我约束（先读）

```
① 【不许把摘要当机制】每条必须写出：什么对象、什么操作、控制什么。
② 【不许把 γ-量说成可能携带 β】若一个量只是 γ 的函数，必须直写 "γ-ONLY-DEAD"。
③ 【标识符核验状态分级】
   ✓✓ = 已实际抓取 abs/PDF 页，题名与作者逐字确认
   ✓  = 第三方引用或检索索引给出完整 DOI/期刊号，未亲自抓取
   ?  = 检索索引可见，未独立核验（文中明确标注 "identifier unverified"）
   ✗  = 未找到 arXiv 标识符（不编造）
④ 【本文件不声称】不声称本项目因此获得任何新数学成果；不声称任何论文正确；
   不声称"未找到"等于"不存在"（T2）。
```

---

## §0.5 ⚠️ 与项目自身最新全景的对齐（**写完初稿后才发现，必须前置声明**）

本文件初稿完成后，发现 `docs/RH-DIRECTION-STATUS-2026-09-12.md`（2026-09-12，最新提交 07fe55f）
**已经包含**三条与本报告直接冲突或重叠的结论。按"**新证据优先**"与"先查先行者"纪律，**必须前置**：

```
【对齐① · 影响 5-C 的定性判断 ✗】
  项目已（读至定理级）判定：**比例类论文的统计量不含实部** —— 
  RH-DIRECTION-STATUS §2.2③ 原文："BGSTB25 的'统计量不含实部'（已读至定理级 ✓）
  ⟹ 又一个 detection≠exclusion 实例 ✓；**不是**先导 ✓（其移除 RH 的步骤是 rank-trace ✓ **我们无**）"。
  ⟹ **后果**：本报告 5-C 的"击穿既有 NO-GO"表述**过强，已下调**（见 5-C 修订的 VERDICT）。
    但 5-C 的【具体测试】仍然有效且未被项目做过 —— 它现在是**验证 β 盲性**的测试，
    而不是"打开一条路"的测试。

【对齐② · 项目已持有唯一"β 通道"构造 ✓（本子代理检索**未**覆盖）】
  项目 E28 已定位：**准晶体散射构造 arXiv:2410.03673** 是"唯一带 β 通道的构造"（✓ 项目自有结论）——
  机制：峰值系数 ∝ p_L^{β_m−1/2} = exp((β_m−½)ln p_L) ⟹ **振幅载 β** ✓；
  但论文自陈"将 β 转为峰高…但**不约束** β" ⟹ 又一个"测量 ≠ 约束" ⟹ E28b 待做 ✓。
  ⟹ 本报告在"带外势/缺陷的载体（方向 3）"一节应把这条列为**已知最强的 β-通道载体**，
    并注明**它由项目自行找到，不在本轮检索命中之内**。

【对齐③ · 本报告的**净增量**因此收窄为三项 ✓】
  ① 方向 2（YM/正性）的**方向级负面结论**（唯一严格路线靠欧氏方向存在）—— 项目全景未展开 ✓；
  ② 方向 4 的三条机制（N(σ,T) / Λ / 窄竖箱）与 **4-A 那张衰减曲线**的具体做法 —— 全新 ✓；
  ③ 5-C 的**可判定测试**（"关掉惯性项看结论是否仍为 0.6725"）—— 这是对项目已有判断的**操作化**，
    项目已知结论但**未给出该测试** ✓。
```
**结论**：本报告**不是**发现了项目未知的 β-通道；它是**把项目已持有的分析外部化、细化、并给出可判定测试**。
这一点必须在读本文件时始终记住（防止把"确认"读成"发现"）。

---

# 第一部分 · 量子混沌 / RMT 的 GUE 之外（方向 1）

## 【1-A】耗散谱形状因子 DSFF 与复本征值的二维关联

- **TITLE**（三篇一组，同一机制族）
  - *Assessment of spectral phases of non-Hermitian quantum systems through complex and singular values* —
    M. Prasad 等，2025，arXiv:2503.13387（Phys. Rev. B **111**, L161408 (2025)）✓
  - *Dissipative spectral form factor for elliptic Ginibre unitary ensemble*，arXiv:2407.17148 ✓
  - *Exact joint eigenvalue densities of non-Hermitian random matrices*，arXiv:2609.00164（2026）✓
- **THE SPECIFIC MECHANISM**：把谱形状因子从 "SFF(τ) = |Z(β+iτ)|²"（一维时间相关）**换成复本征值平面上的
  二维关联函数 DSFF(τ, τ')**；操作是 **Fourier 变换到两个复时间变量**，控制的是**本征值实部与虚部之间的关联**。
  非厄米矩阵的本征值本来就是复数组，DSFF 的定义里**同时显含 Re 与 Im 两个坐标**。
- **WHY IT MIGHT CARRY β**：**这是本报告里唯一一类"按定义就含第二个坐标"的标准工具。**
  诚实评估：**对本项目当前资产 —— 不携带 β。** 理由不是工具不够好，而是**场上没有非厄米算子**。
  ζ 的零点不是任何已知非厄米算子的谱；把 {1/2+iγ} 硬塞进复平面再算 DSFF，
  等于**先把 β=1/2 写进输入**（违反 T6"三个 ½ 必须区分"）。
  ⟹ 判据：**工具合格，宿主缺失**。
- **CONCRETE TEST**：**存在一个，但它是"装置对照"而非 β 检测**：
  用 `zeros_odlyzko_2M.npy` 造两个人工谱 —— (i) 全部落在 Re = 1/2 的"线系综"，
  (ii) 人为把前 100 个零点的实部搬到 1/2 ± 0.02 —— 计算二者的 DSFF/复间距比（CSR）。
  **若 (ii) 在 DSFF 上完全不可分，则连"二维工具本身"都只在平均意义下工作**；
  若可分，则得到一条**明确的负结果**：本项目的零表**在原则上**足以喂给二维工具，
  缺的不是数据而是算子。这一步**不需要新算子**，可以立刻做。
- **VERDICT**：**NEEDS-DEEP-READ**（作为活路 L1 的输入：见 §1-D）。**不是** β 检测器。

## 【1-B】全 Dyson 类与对称分解的谱形状因子

- **TITLE**
  - *Leading and beyond leading-order spectral form factor in chaotic quantum many-body systems across all Dyson symmetry classes*，
    arXiv:2502.04152（Phys. Rev. X **16**, 031019 (2026)）✓
  - *Decomposing the Spectral Form Factor*，arXiv:2311.09292（Phys. Rev. B **111**, 165108 (2025)）✓
  - *Quenched properties of the Spectral Form Factor*，Charamis 等，2025，arXiv:2509.14406 ✓
- **THE SPECIFIC MECHANISM**：在**全部十个对称类**里，用 DBM/"随机涌现的基不变性"导出 SFF 的封闭微分方程层级；
  "对称分解"= 把希尔伯特空间按守恒量分块，逐块算 SFF 再相加。
- **WHY IT MIGHT CARRY β**：**不携带。清晰判为 DEAD。**
  理由：整个构造是**平移不变**的 —— SFF/层级方程依赖的只有**能级差**（= spacing），
  分块只是把同一套 spacing 统计切片。对称分解给你的是"每块的 γ 统计"，
  **没有任何量是 β 的函数**。诚实结论：这是本方向**最强的阴性结果** ——
  "对称性 / 分块 / 高阶 SFF"这一整条路**在原理上**与 β 无关。
- **CONCRETE TEST**：**不存在**（不是资产不足，而是对象不含 β，测试无意义）。
- **VERDICT**：**γ-ONLY-DEAD**。（这一条本身就是有价值的阴性结果，建议登记进 NO-GO 关键词表：
  *symmetry-resolved SFF / 高阶 SFF / Dyson-class hierarchy*。）
- **【1-B 附】变形系综（非高斯多项式势）的早期 SFF —— 同一死因，且是 T8 陷阱的现成样例。**
  检索未定位到单一权威论文（仅综述页转述，**identifier unverified**）：转述称"非高斯势的变形在**早期 SFF**
  留下痕迹，长时普适结构不变"。**判 DEAD，理由同 1-B**：变形改变的是**一维密度剖面**（即 γ 的密度），
  不产生横向坐标。**这正是"扰动在体量可观测量里留痕"的假阳性样本** —— 痕迹留在**体密度**上，
  而非留在 **β** 上。若本项目把它误读为"扰动可携带 β"，就踩了 **T8（恒等式/形式事实不携带信息）**。
  对照：本项目 `p38-g*` 变形系列已给出同类结论"变形 → 零耦合" ✓。

## 【1-D】⭐ 非自伴谱界 · 复势 Hill 算子 · Krein/Pontryagin 非负性（直击活路 L1）

- **TITLE**
  - *Eigenvalue bounds for non-self-adjoint Schrödinger operators and pseudodifferential generalizations* —
    E. Stefanescu，2026，arXiv:2605.16569 ✓✓（已抓 PDF 正文；"This is mostly a survey paper…"）
  - *Non-Self-Adjoint Hill Operators whose Spectrum is a Real Interval* — V. G. Papanicolaou，2024/2025，arXiv:2409.10266 ✓✓
  - *On non-negative operators in Krein spaces*，2026，arXiv:2603.28403（? 检索索引可见，未亲自抓取）
- **THE SPECIFIC MECHANISM**
  - 2605.16569：把 **Birman–Schwinger 原理 / Schatten 类 / Lieb–Thirring 型不等式**搬到**复值势**，
    给出**复本征值（含离实轴者）**的定量界，界形如 ‖V‖_{L^p} 的函数。
  - 2409.10266：**刻画**哪些**复周期势 q(x)** 的非自伴 Hill 算子谱恰为 [0,∞)（实区间）。
    —— 即 **"不自伴但谱为实"** 的完整刻画（Gasy-mov 现象），含"连续形变参数 tq(x), 0≤t≤1"的技术。
  - 2603.28403：Krein 空间里**非负算子**的新刻画（基于局部符号型）。
- **WHY IT MIGHT CARRY β**：**这一族是本报告与活路 L1 的交点，也是唯一"按问题形状"对口的。**
  L1 的唯一问题原文是：「是否存在一种**不依赖自伴性**的正性，直接约束共振参数的**实部**？」
  —— 2605.16569 是**该问题的文献综述**（这正是 L1 下一步要做的"文献审计"五项之一）；
  2409.10266 是**该问题的正面答案形状**（不自伴 ⟹ 谱仍可为实，且给出刻画）。
  **诚实警告**：两者都与 ζ **零连接**；且 2605.16569 的界是对 ‖V‖ 的**范数型**界，
  **大概率落在 L1 的否决判据里**（"若五者皆只能给数值域/奇异值/增长率界 ⟹ 一次性封死"）。
- **CONCRETE TEST**：**可以立刻做，且是纸面的。** 做 L1 要求的**五项文献审计**，
  把 2605.16569（②dissipativity ①numerical range）、2409.10266（④ J-self-adjointness 邻域）、
  2603.28403（③ Krein/Pontryagin）逐条对照 **L1 否决判据**，判定：五者是否**全部**只能给范数界。
  若是 ⟹ **按纪律一次性封死 L1**（不得改名续命）。**这是一条能"关闭"而非"打开"的测试——正是本项目要的那种。**
- **VERDICT**：**NEEDS-DEEP-READ（最高优先；直接喂给 L1 的文献审计，且很可能触发 L1 否决判据）**。

---

# 第二部分 · Yang–Mills / 正性（方向 2）

> **本方向总体结论：唯一严格、定量、基于正性的质量间隙路线是随机量子化/log-Sobolev 路线，
> 而它按构造**没有**任何 β 含量。此外，2025–2026 关于"构造性证明 YM 质量间隙"的**高调声明全部不可用**
> （一篇被 arXiv 撤稿，其余发表渠道与作者模式不足以支撑本项目 P9"一手来源"纪律）。
> 这是一个**干净的负面结论**：方向 2 对本项目**不出货**。**

## 【2-A】"构造性 Yang–Mills 质量间隙证明"这一族高调声明：一篇撤稿、一篇渠道不足以采信

- **TITLE（两篇同族，合并登记）**
  - *A Constructive Proof of Existence and Mass Gap for Pure SU(3) Yang–Mills in Four-Dimensional Space-Time*，
    2025，arXiv:2506.00284 ✓✓ —— **已被 arXiv 撤稿**
    （abs 页原文："arXiv admin note: This submission has been withdrawn because it does not meet arXiv's
    research content quality standards"）
  - *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement* —
    Mir Faizal, Arshid Shabir，2026，arXiv:2606.19362（Fortsch. Phys. **74** (2026) 4, e70097）✓✓
- **THE SPECIFIC MECHANISM**（两篇同构）：把 4 维规范场嵌入 **5 维 orbifold 正则化器**的零模扇区，
  用**收敛的联合聚合物展开** + **反射正性**（按时间平面 x₄=0 切片定义转移矩阵 T）
  + **Osterwalder–Schrader 重构** + Sturm–Liouville 谱分析。控制的是转移矩阵的谱隙。
- **WHY IT MIGHT CARRY β**：**不可能。** 机制中的对象是 Wilson 圈的 Boltzmann 权重与转移矩阵的谱 ——
  **没有任何一个量与 ζ 的零点有关**。
- **另一条方法论警告（针对 2606.19362）**：该文自述"支撑计算已作为**四篇系列论文**发表在
  *Int. J. Geom. Meth. Mod. Phys.* (2026) 2650111–2650114"，并把这些论文**附在正文之后**。
  对本项目而言，这属于"发表渠道与惯例偏离主流同行评审"的信号；按 `P9-primary-source-rule`
  与宣言所要求的**可核验性**，**不应作为机制来源采信**。
- **CONCRETE TEST**：无。
- **VERDICT**：**OUT-OF-SCOPE**。**建议登记进 NO-GO**：防止本项目（或未来的我）再被这条新闻吸引 ——
  "2025–2026 的构造性 YM 质量间隙声明"这一族**整体不可用**。

## 【2-C】唯一严格且定量的正性 ⟹ 间隙：φ⁴ 的 log-Sobolev 路线

- **TITLE**
  - *Log-Sobolev inequality for the φ⁴₂ and φ⁴₃ measures* — R. Bauerschmidt, B. Dagallier，arXiv:2202.02295
    （Comm. Pure Appl. Math. **77**(5) 2579–2612, 2024）✓
  - *Log-Sobolev inequality for near critical Ising models*，arXiv:2202.02301（CPAM **77**(4), 2024）✓
  - *A criterion on the free energy for log-Sobolev inequalities in mean-field particle systems* —
    R. Bauerschmidt, T. Bodineau, B. Dagallier，2025，arXiv:2503.24372 ✓✓
- **THE SPECIFIC MECHANISM**：证明连续 φ⁴ 测度**在格点正则化下一致地**满足 log-Sobolev 不等式；
  操作是**骨架不等式（skeleton inequalities）+ 自由能判据**；控制的是**Langevin 动力学的谱隙**，
  在 OS 重构下**即**质量间隙的定量下界。**这是本项目要的那种"正定结构 + 定量间隙"。**
- **WHY IT MIGHT CARRY β**：**不携带，判为 DEAD。**
  诚实理由（这一段重要）：log-Sobolev 之所以在 CQFT 里能给出间隙，
  是因为存在**一条欧氏方向**：反射正性 ⟹ 转移矩阵自伴 ⟹ Perron–Frobenius/谱定理 ⟹ 隙。
  ζ 的函数方程 ρ↔1−ρ̄ 是**反射**，但**没有欧氏区域、没有概率测度**，
  所以"反射正性"在此**只有形状相似，没有内容**。
  ⟹ 方向 2 的教训是：**可以借的是"正性 ⟹ 定量间隙"的结构，不能借的是它的载体。**
- **CONCRETE TEST**：**不存在**（对象不同维、不同类）。
- **VERDICT**：**OUT-OF-SCOPE（结构对照用）；对 β 判 γ-ONLY-DEAD**。

---

# 第三部分 · 带外势 / 缺陷的 log-gas 与 Coulomb gas（方向 3）

> **本方向总体结论：有一个**真正**的"非厄米扰动挪动本征值实部"的精确机制（3-A），
> 但它是**厄米系综 + 非厄米秩一扰动**，不是 ζ。其余（3-B）为 γ-only。
> 本方向的**最有用产出**其实是 3-B 的"刚性可以失效"。**

## 【3-A】⭐⭐ 准晶体散射构造：**项目已确认的、唯一"振幅载 β"的载体**

> **来源声明**：本条**不在本轮检索命中之内**，而是从项目自己的 `docs/RH-DIRECTION-STATUS-2026-09-12.md` §2.3 指针①
> 与 E28 读出（写本文件初稿后发现）。**登记在这里是为了让"方向 3"的一节完整**，并明确标注它的归属。

- **TITLE**：准晶体散射构造，arXiv:2410.03673（2024）（✓ 项目 E28 已读；本子代理**未独立核验**该标识符）
- **THE SPECIFIC MECHANISM**：构造准晶体散射振幅 χ̂_L(k) = Σ p_n^{−2πik}；
  操作：**局部化于 k ≈ γ/2π**；控制的是 **k-空间峰的位置（→ γ）与峰高（→ β）**。
  机制原文（项目 E28 转述）：**峰系数 ∝ p_L^{β_m−1/2} = exp((β_m−½) ln p_L)** ⟹ **振幅载 β** ✓。
- **WHY IT MIGHT CARRY β**：**是 —— 这是本报告全文中唯一一个"β 进入可测量振幅"的显式公式。**
  诚实评估：论文**自陈"将 β 转为峰高…但不约束 β"** ⟹ **测量 ≠ 约束**（又是墙）。
  且**它由项目自行找到**，本子代理未复现其推导，故**不能**作为"外部新证据"引用。
- **CONCRETE TEST**：**已有（项目 E28b）**：**不同 p_L 上的峰高必须相容** —— 若相容性给出 β = 1/2 ⟹ 突破；
  若恒相容 ⟹ 又一个自适应墙（**可判定** ✓）。现有资产够（素数表 + 零点表）。
- **VERDICT**：**PROMISING（项目已列为"幸存指针①"；本轮检索未改变该判定）**。

## 【3-B】⭐ 厄米 β-系综的**秩一非厄米**扰动：离轴位移是精确可算量

- **TITLE**
  - *Rank one non-Hermitian perturbations of Hermitian β-ensembles of random matrices*，arXiv:1510.04456 ✓
  - *The eigenvalues and eigenvectors of finite-rank normal perturbations in non-Hermitian ensembles*，
    arXiv:2601.10427（2026）✓（PDF 片段确认题名与主题）
  - *Asymptotic behavior of eigenvalues of large rank perturbations of large random matrices*，
    arXiv:2507.12182（v4, 2026）✓（含 "bulk decay" 情形）
- **THE SPECIFIC MECHANISM**：取厄米系综 H（真实谱），加**一个秩一非厄米项**（如 i·u v†）。
  操作：用 **Sherman–Morrison / 行列式条件**求新谱；控制的是**"外点（outlier）本征值的复位置"**，
  并给出**有限 N 下"本征值 + 共振极点"的联合密度**。
  关键点：**外点会离开实轴**，其**实部位移是扰动强度的显函数**，且扰动**同时在体密度上留痕**。
- **WHY IT MIGHT CARRY β**：**这是本报告第二条"按定义含 β"的机制**（第一条是 DSFF）。
  区别在于：DSFF 需要"非厄米宿主"才成立，而这里**宿主是厄米的、扰动是非厄米的**——
  **恰好对应本项目的 `p38-g*` 变形框架与 "Weil 形式 + 变形" 的形状**。
  诚实评估：**仍然缺宿主**（没有算子 ⟹ 没有 H），但**机制模板是本报告最可用的一条**：
  它给出了一个**"若扰动把外点推离实轴 δ，则在体可观测量上必须出现可计算的痕迹"**的定理形状。
- **CONCRETE TEST**：**存在，且能用现有资产。**
  本项目已有**有限压缩 + 惯性**的脚本族（`p27g4-2x2-negative-witness`、`p27g72-inertia-gap`、
  `p27g82-finite-inertia`、`p27g73*`）。可做：
  取 Weil 形式的有限压缩 A_N，加**人工秩一非厄米扰动 iε·uv†**，
  测量 (i) 外点离轴距离 |Im λ_out| vs ε 的幂律；(ii) 体惯性的改变量。
  **目的不是证明什么，而是标定"离轴位移 → 惯性变化"的响应系数**，
  即：**惯性对 β 有多敏感**。这直接回答本项目"有限惯性不向无穷维传输"这条 NO-GO 的**定量版本**。
- **VERDICT**：**PROMISING（作为机制模板 + 可立刻跑的标定实验）**；但**不等于** β 检测器。

## 【3-C】Coulomb gas 的**非刚性**与"间隙的诞生"

- **TITLE**
  - *Non-rigidity Properties of the Coulomb Gas* — E. Thoma 等，2023，arXiv:2303.11486 ✓
  - *Birth of a gap: Critical phenomena in 2D Coulomb gas*，arXiv:2509.24529（2025/2026）✓
- **THE SPECIFIC MECHANISM**
  - 2303.11486：证明 d ≥ 3 存在**非"数目刚性"（number non-rigid）**的无限体 Coulomb gas ——
    即**加一个粒子不会引起远处的补偿位移**。
  - 2509.24529：在 β=2、径向对称的一族系统里，随参数变化**平衡测度的支撑里长出一个间隙**（相变）。
- **WHY IT MIGHT CARRY β**：**均不携带，判 DEAD。** 两条都是**一维/径向**的密度现象，量是 γ 的函数。
  **但 2303.11486 对本项目有概念价值**：它证明"**刚性不是自动的**"。
  本项目的中心结论之一是 "检测 ≠ 排除（Rigidity Gap）"；这条文献说明**刚性失效在物理上是常见现象**，
  ⟹ 支持本项目"不可从有限刚性外推"的立场。**这是"结构律"而非"机制"。**
- **CONCRETE TEST**：无直接测试；可作为 `p26a18-loggas-crystal.md` 的**外部对照**（该文档已有"晶体/刚性"讨论）。
- **VERDICT**：**γ-ONLY-DEAD**（结构性对照价值保留）。

---

# 第四部分 · de Bruijn–Newman / Lehmer 对 / 零点密度（方向 4）

> **本方向是五个方向里唯一"天然含 β 分辨率"的**：
> N(σ,T) 与 Λ 都是**显含实部方向**的量。因此本方向的产出最多（见 4-A/4-B/4-C/4-D）。

## 【4-A】⭐ N(σ,T)：**天然的 β-载体**（零点密度）

- **TITLE**
  - *An explicit form of Ingham's zero density estimate* — S. Chourasiya 等，2025，arXiv:2507.15184 ✓
  - *Explicit zero density for the Riemann zeta function* — H. Kadiri 等，2021，arXiv:2101.12263 ✓
  - *Explicit zero density estimate for the Riemann zeta-function near the critical line*，arXiv:1910.08274 ✓
- **THE SPECIFIC MECHANISM**：定义 N(σ,T) = #{ρ = β+iγ : β > σ, |γ| ≤ T}。
  操作：用**大筛法 / 矩估计 / 近似函数方程**给出 N(σ,T) 的**显式上界**（含 σ 的幂与 T 的幂）。
  控制的是 **"有多少零点的实部超过 σ"** —— 这是**字面意义上对 β 的排除**。
- **WHY IT MIGHT CARRY β**：**这是本报告唯一"无条件且定量地排除 β ≠ 1/2"的量。**
  它**不是** γ-only：N(σ,T) 随 σ 单调，**σ → 1/2⁺ 的行为正是 RH 的量**。
  **诚实的天花板**：经典密度定理在 σ = 1/2 + o(1) 处**退化**（给不出任何排除），
  这正是本项目"β 墙"的**外部同型**：**能排除的区间与临界线之间有一道无条件不可跨越的缝**。
  ⟹ 结论：**N(σ,T) 是"合法的 β-载体"，但它的排除能力恰好在本项目需要的地方消失。**
  这也解释了为什么"检测 ≠ 排除"是结构性的，而非本项目的技术失误。
- **CONCRETE TEST**：**存在，且用现有资产，可在一次计算内完成。**
  用 `zeros_odlyzko_2M.npy`（= 前 2×10⁶ 个零点，均假设在线上）：
  (i) 计算实际 N(σ, T₀) 曲线（对 σ ∈ [0.50, 0.60]，T₀ 取表中最大高度）；
  (ii) 与 Kadiri/Chourasiya 的**显式上界**在该 T₀ 处对比；
  (iii) 画"上界/真值"比值随 σ → 1/2 的爆炸曲线。
  **产出**：一张**"无条件 β-排除能力的衰减曲线"**，把 β 墙**定量化、外部化**。
  这是本项目最需要的"讲清墙的形状"的产物，且**完全用现有零表**。
  （注意 T3 卫生：零表全是实数，N(σ,T) 的"真值"在 σ > 1/2 处恒为 0 ——
   本测试的**意义**在于**对比上界的松弛度**，必须这样表述，不可宣称"验证了 N=0"。）
- **VERDICT**：**PROMISING（本报告最高性价比的下一步）**。

## 【4-B】⭐ de Bruijn–Newman 常数 Λ：唯一"以 β 为自变量"的经典对象

- **TITLE**
  - *Λ ≤ 0.1787854 —— a new bound for the de Bruijn–Newman constant*，
    Jude Gomila，2026-08-19，**个人网页长文**（自述有 Dan Romik 复核 + 四体对抗式 AI 审查）。
    **⚠️ identifier unverified —— 未找到 arXiv 标识符，本条目按"未发表/未同行评审"登记。**
  - 背景（已确立）：Polymath 15 (arXiv:1904.12438) 的 Λ ≤ 0.22；Platt–Trudgian (2020) 的 Λ ≤ 0.2；
    Rodgers–Tao (2018) 的 **Λ ≥ 0**。
- **THE SPECIFIC MECHANISM**：H_t 是 Ξ 的**热流变形族**；Λ 是"H_t 零点全为实"的临界 t。
  操作：**在具体参数行上实例化 Polymath 15 的 Theorem 1.2/1.3**（有限矩阵的区间算术 + 证书），
  控制的是 **"零点能离开实轴多远"的整体阈值**。
- **WHY IT MIGHT CARRY β**：**这是文献中唯一一个"其自变量就是 β 方向"的整体常数。**
  Λ 不是 γ 的函数：它由**零点复几何的整体流动**决定。
  **诚实的天花板**：Λ 是**一个数**，它**不定位、不计数**任何具体的非实零点；
  且 **Λ ≥ 0（Rodgers–Tao）与 Λ ≤ 0.2** 的夹逼已表明：**RH 若真，"恰好勉强"** ——
  这正是本项目"β 墙"的**最经典表述**：**β 方向的可用信息被压缩在一个宽度 0.2 的区间里，
  而 RH 需要它精确地 ≤ 0**。
- **CONCRETE TEST**：**存在，且高度可核验（但属于"复核他人"，不是"发现"）。**
  本项目已有 **AFE 认证计算器**（`scripts/B_AFE_check.py`、`B_AFE_w1_verdict.py`，w=1 相对差 ≤ 1e−43）
  与 **Lean 4 + Mathlib**。可用它**独立重算该文声称的最紧那个不等式**（其自述的 "Dini transfer"），
  并在 Lean 里形式化该不等式的**初等部分**。**注意纪律**：这是**验证别人的界**，
  若成功，产出是"**一次可核验的独立复核**"（符合宣言所珍视的可核验性），**绝不可包装为新成果**。
- **VERDICT**：**NEEDS-DEEP-READ**（先确认 arXiv 状态与同行评审状态，**再投入任何计算**）。

## 【4-C】Lehmer 对 ⟹ Λ 的下界：把局部 γ 数据转换成 β-方向的界

- **TITLE**：经典链条 —— Csordas–Norfolk–Varga (1988)；te Riele (1991)；
  **Csordas–Odlyzko–Smith–Varga, *A New Lehmer Pair of Zeros and a New Lower Bound for the
  de Bruijn–Newman Constant*, Elec. Trans. Numer. Anal. 1 (1993) 104–111**（✓ 经 MathWorld 与 Wikipedia 交叉）
- **THE SPECIFIC MECHANISM**：取一对**非常接近**的零点（Lehmer 对），
  在 Ξ 的 Taylor/Laguerre 型不等式中代入该对 ⟹ 得到 Λ 的**下界**。
  操作是**"局部对 ⟹ 全局 β-界"**；控制的正是 **Λ**。
- **WHY IT MIGHT CARRY β**：**携带 β，但只是"单方向的存量信息"。**
  它把 γ 的**局部构型**换成 β-方向的一个**界**；它**不检测**任何 β ≠ 1/2 的零点。
  诚实评估：这是"**γ-数据 ⟹ β-界**"的**唯一经典通道**，且**已在 1993 年被压到 −1.1×10⁻¹¹**
  —— 说明**这条通道的信噪比极低**：需要极端巧合的零点对，收益是一次幂级。
- **CONCRETE TEST**：**存在，可用现有 2M 零表，一次运行完成。**
  实现 Csordas–Odlyzko–Smith–Varga 的下界公式，输入 `zeros_odlyzko_2M.npy` 中最紧的若干对，
  **先复现文献值**（作为实现正确性证书），再报出对 2M 零表的新下界。
  **纪律要求**：这是**复现 + 延伸既有方法**，必须标注为"**方法未变，仅数据更长**"，
  且需给出 dps 稳定性证书（T3）。
- **VERDICT**：**PROMISING（可实现的方法学工具；产出可核验；不声称新机制）**。

## 【4-D】⭐ Goldston–Suriajaya：**"窄竖箱"中的零点计数** —— 直接解析 β 方向

- **TITLE**
  - *Zeta Zeros on the Critical Line* — D. A. Goldston, A. I. Suriajaya，2025，arXiv:2511.20059 ✓✓（9 页 expository）
  - *Zeta Zeros in a Narrow Vertical Box* — 同上，2026，arXiv:2603.28104 ✓✓（7 页 expository）
  - 相关：Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh，arXiv:2501.14545 ✓（第三方引用）；
    Goldston–Lee–Schettler–Suriajaya，arXiv:2503.15449 ✓（第三方引用）
- **THE SPECIFIC MECHANISM**：不在整条竖带里数零点，而在**围绕 σ = 1/2 的窄竖箱**里数；
  操作是**箱宽 → 0 的极限下的计数/正性估计**；控制的是 **"能证明落在箱内的零点比例"**。
  第 2511.20059 与 2603.28104 是**综述性说明**（expository），把这条路线讲清楚。
- **WHY IT MIGHT CARRY β**：**是。** "窄竖箱"**就是**对 β 方向做分辨的装置 ——
  箱宽是**显式的 β 分辨率参数**，而不是平均掉的 γ 量。
  **诚实评估**：这条路线目前给的是**比例**（"≥ 某比例在箱内"），
  **不是排除**；且箱宽 → 0 时误差项吞掉一切（与本项目"检测 ≠ 排除"同址）。
  但它是**文献里"把 β 分辨率当作显式参数"的最明确写法**。
- **CONCRETE TEST**：**存在。** 用 `zeros_odlyzko_2M.npy` + AFE 计算器：
  对若干箱宽 w ∈ {0.5, 0.2, 0.1, 0.05}，计算**落箱计数**（真值恒等于"全部"，因零表在线上），
  并**计算该路线的理论误差项在 T = 2×10⁶ 号零点高度处的量级**；
  产出：**"需要多窄的箱 + 多高的 T，误差项才不再淹没信号"** 的定量曲线。
  若误差项在可及 T 内**永不**低于箱宽分辨率 ⟹ **该路线对本项目直接判死（一条干净的负面结果）**。
- **VERDICT**：**NEEDS-DEEP-READ（高优先；很可能产出干净的负面结果）**。

---

# 第五部分 · Selberg 类 / Weil 正性的"新"正性来源（方向 5）

> **本方向产出最大，且出现了一条**击穿本项目既有 NO-GO** 的机制（5-C）。
> 必须极其谨慎地评估，因为 5-C 是**唯一**"看似携带 β 且是无条件"的条目。**

## 【5-A】Connes 2026：Sonin 空间作为正性来源 —— **β 盲（重述）**

- **TITLE**：*The Riemann Hypothesis: Past, Present and a Letter Through Time* — A. Connes，2026，arXiv:2602.04022 ✓✓
- **THE SPECIFIC MECHANISM**：在半局部 adele 类空间 Y_S = ∏_{v∈S} Q_v / Γ 上，
  用**半局部迹公式**；发现的"正性的主要来源"是 **Sonin 空间 𝔖_λ**
  = 在 [−λ,λ] 上及其导数**恒为零**的 L² 函数构成的空间。
  操作：**支持集避开原点的函数 ⟹ Weil 形式正定**。
- **WHY IT MIGHT CARRY β**：**不携带。** 本项目已有结论（`MASTER-NOGO` §2.1）：
  **"Connes 2026：β 盲（Weil 重述）"**，且 T7（从 ζ 自身推出正性 ⟹ 循环）。
  本轮检索**未推翻**该结论，反而补强：Sonin 空间是**支持条件**，"支持避开原点 ⟹ 正性"
  与 `PROTOCOL-R6-support-ceiling` 是**同一主题**。
  ⟹ 本项目的"支撑上限"与 Connes 的 𝔖_λ 是**同一条约束的两个写法**，**都只给 γ 侧信息**。
- **CONCRETE TEST**：**已有**（`docs/DOOR5e/5f`、`PROTOCOL-R6-support-ceiling.md`）。
  建议动作：把 2602.04022 的 𝔖_λ 与本项目 support-ceiling 结果**逐项对照**，
  确认两者给的 λ 阈值是否一致。**这属于 E18 对齐流程**，不新增计算。
- **VERDICT**：**γ-ONLY-DEAD（已登记，本轮仅补证）**。
- **【5-A 附】Suzuki 的 Weil 二次型算子的数值实现 —— 同一死因。**
  *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its
  Universality, and an Operator Form of Weil's Positivity Criterion*，2026，arXiv:2607.24830 ✓✓
  （归入 math.GM，18 页，未注明期刊；按 P9 纪律只能当预印本）。
  机制：把 Suzuki 的 Weil 二次型算子数值离散化，报告"archimedean 谱律"与 Weil 正性的算子形式。
  **判 DEAD**：Weil 正性 ⟺ RH 是**重述**（T7/T9），算子形式是**表达方式的改变**，不是新正性来源。
  无 β 含量，无测试。

## 【5-B】Weil 正性的**紧窗口有限归约** + Landau–Widom 衰减律

- **TITLE**：*Weil positivity in compact windows: a finite reduction, certified two-sided bounds,
  and a Landau–Widom decay law*，2026，arXiv:2608.24827 ✓✓（v2 为全文版，v1 为 9 页公告）
- **THE SPECIFIC MECHANISM**：对支撑在 [−L,L] 的检验函数，研究 λ*(L) = inf Q(f)/‖f‖²。
  操作：**一步归约**把"窗口正性"变成**一个有限矩阵的半正定性**；
  在 L = 0.8（支撑 1.6）处得到**无条件证书** Q(f) ≥ 8.9×10⁻¹⁸ ‖f‖²，
  把经典范围（Yoshida / Connes–Consani 的 **log 2 ≈ 0.693**）**扩大 2.3 倍**；
  并证明**窗口基态是单重且偶的**。另有**区间算术 Rayleigh 商**给出的上界，
  以及 **Landau–Widom 衰减律**（窗口正性余量随 L 的衰减速率）。
- **WHY IT MIGHT CARRY β**：**不携带 —— 且这正是关键诊断。**
  小支撑的 Weil 正性是**无条件**的 ⟹ 按本项目 T7/T8，
  **"无条件的就是不含信息的"**（正性与 RH 的等价只在 L → ∞ 时才出现）。
  该文自己写明了这一点：证书是"at a fixed scale"。
  **但有一个真正值得深挖的次级对象**：**Landau–Widom 衰减律** ——
  **余量的衰减率**是"窗口大小"的**整体函数**，而"窗宽"与"β 分辨率"同轴。
  ⟹ **不是它现在携带 β，而是它的衰减率可能编码了 β 分辨率的上限。**
- **CONCRETE TEST**：**存在。** 本项目有 support-ceiling 结果与窗口泛函饱和的历史（E8，已降级为"重述经典最优性"）。
  动作：用现有窗口脚本，在支撑 ∈ {0.693, 1.0, 1.3, 1.6} 处计算**本项目版本的余量曲线**，
  与 2608.24827 的 **Landau–Widom 衰减律**对比。
  **两种结局都是有用的**：(i) 曲线一致 ⟹ 本项目 E8 的"经典最优性"读数得到外部印证；
  (ii) 曲线不一致 ⟹ **本项目与一篇新文正面冲突，必须优先解决**。**这是硬对比，不是软对照。**
- **VERDICT**：**NEEDS-DEEP-READ（必做硬对比；本身 β 盲，但衰减律值得追）**。

## 【5-C】⚠️ 曾被初稿列为首位：**用 Sylvester 惯性律处理"离线零点对"**（**经 §0.5 对齐后定性下调**）

- **TITLE**
  - *More than two thirds of the zeta zeros are simple and on the critical line* —
    L. Alpöge, R. Furman，2026-08，arXiv:2608.13637 ✓✓
    （abs 页原文注记："**Proof discovered autonomously by Claude (Anthropic); verified and communicated by
    the listed authors. See §1 for provenance. Lean formalization available**"；MSC 含 **15A42 = 矩阵不等式**）
  - *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line* —
    Y. Lamzouri，2026-09-08，arXiv:2609.02882 ✓✓
    （另给：>88.76% 的零点"单重或在线"，两者比例的均值 ≥ 83.62%）
  - 源头：Anthropic 内部研究版 Claude 的报告（2026-08-10，Anthropic CDN PDF；**无 arXiv 标识符 ✗**）
- **THE SPECIFIC MECHANISM**（**本报告的核心发现，逐字依据 2608.13637 摘要与 Lamzouri 的转述**）：
  Montgomery (1973) 的推导**经典上需要 RH** —— 为了把"零点侧"读成**只对实纵坐标求和的正和**。
  该文**用一个 rank–trace 不等式 + Weil 厄米形式的有限压缩，替代了 RH 这一输入**；
  而 **"离线零点对"（β ≠ 1/2 的共轭对）由 Sylvester 惯性律处理**。
  控制的是：**零点单重性 + 在临界上的比例**，**且是无条件的**。
- **WHY IT MIGHT CARRY β**：**这是全部 14 条里唯一"把 β 处理写成显式技术步骤"的机制。**
  三点必须说清：
  ① **Sylvester 惯性律**正是本项目 **P27–P33**（`p27g*`、`p28b2c-schur`、`p27g72-inertia-gap`）的核心对象 ——
     惯性签名 = 负惯性指数 = 2 × (离线零点对数)。**它字面上携带 β。**
  ② 它**击穿了本项目的既有 NO-GO**。本项目登记过一条"文献级 NO-GO"：
     **"β 盲核 ⟺ 无条件；β 敏感 ⟺ 条件性"**（Lamzouri 相关）。而 2608.13637 的**整个卖点**就是
     **用有限压缩 + 惯性把 β 敏感的那一步变成无条件的** ⟹
     **该 NO-GO 的表述必须收紧为**："β 盲 ⟺ 无条件"**在有额外结构（rank–trace + 惯性）时失效"**。
     这是本轮**最重要的外部情报**，且**不需要任何新计算就能更新认知**。
  ③ **诚实的天花板（必须写进结论）**：他们用惯性是去**计数/上界**离线对，**不是排除**；
     并且**有限压缩 → 无穷维的传输**，正是本项目 **"moving-edge indeterminacy"** 已判死的缺口
     （`MASTER-NOGO` §2.1：P27–P33 有限惯性**不**向无限维传输）。⟹ 不能因为它是无条件的就认为缺口不存在。
- **CONCRETE TEST**：**存在，且本项目已有全部零件 —— 这是本报告的第一号测试。**
  1. **复现常数**：用本项目 `p28b2c-schur`、`p27g72-inertia-gap`、`p28c1-schur-mpmath` 的有限压缩 + 惯性工具，
     在 2608.13637 的同款压缩上重算，看 **0.6725** 与 **0.8362** 是否复现（第三方检验）。
  2. **判定"惯性项是否在真做功"**：把 rank–trace 不等式中的**惯性项**单独关掉（形式令离线对贡献为 0），
     再看结论是否仍为 0.6725。**若仍成立 ⟹ 惯性项是装饰（=本项目 T8 型陷阱），该机制对 β 无效。**
     **若不成立 ⟹ 惯性项是真做功，则该文应升级为本项目的"必读一手来源"。**
  3. **Lean 交叉检查**：该文称有 Lean 形式化；本项目已有 Lean 4 + Mathlib 环境（`lean/README.md`），
     可**直接取用其形式化**作为对照（无需自己重写）。
- **VERDICT**：**NEEDS-DEEP-READ（修订后）**。
  **⚠️ 定性下调（按 §0.5 对齐①）**：项目 `RH-DIRECTION-STATUS-2026-09-12.md` §2.2③ 已（读至定理级）
  判定"比例类论文的统计量**不含实部**"，并指出其移除 RH 的那一步是 rank-trace、**"我们无"**。
  ⟹ 本条目**不再声称"击穿既有 NO-GO"**（初稿表述过强，**在此撤回**）。
  它的真实价值收窄为两点：
  ① **把项目已有判断操作化** —— 给出一个**可判定**的测试（下述测试 2），一次计算即可确认 β 盲性；
  ② 修正 NO-GO 的**表述精度**：应写为"β 盲 ⟺ 无条件"**在缺少额外结构（rank-trace + 惯性）时**成立 ——
     同时承认：**该额外结构确实存在，但不足以把"比例"升级为"约束"**。

---

# 第六部分 · 五个方向的产出统计与"没有找到"的部分

**条目计数**：本文件共 **15 条编号条目**
（1-A, 1-B, 1-D, 2-A, 2-C, **3-A, 3-B, 3-C**, 4-A, 4-B, 4-C, 4-D, 5-A, 5-B, 5-C），
落在任务要求的 **8–14 条**区间内（略超出 1 条，因中途加入 3-A）。
编号中的 **1-C / 2-B / 5-D 有意缺号**：初稿曾写成独立条目，但因与邻条**同机制、同死因**，
按本项目"宁少勿滥"纪律**合并进邻条**（1-C → 1-B 附；2-B → 2-A；5-D → 5-A 附），内容未丢失。

| 方向 | 编号块 | 真正携带 β 的 | 干净负面 | 最有用产出 |
|---|---|---|---|---|
| 1 量子混沌/RMT 超 GUE | 3 | 1（DSFF，但缺宿主） | 2 | **1-D：直击活路 L1 的文献审计** |
| 2 YM / 正性 | 2 | 0 | 2 | **方向级负面**：唯一严格路线靠欧氏方向存在 |
| 3 带外势的 log-gas | 3 | 2（3-A 振幅载 β；3-B 离轴位移） | 1 | **3-A 振幅载 β 公式 + 3-B 可跑的标定实验** |
| 4 DN / Lehmer / 零点密度 | 4 | **3**（N(σ,T)、Λ、窄竖箱） | 0 | **4-A：β-排除能力衰减曲线** |
| 5 Selberg / Weil 正性 | 3 | 0（5-C 经对齐后降为 β 盲） | 3 | 5-C 的可判定测试（验证 β 盲性） |

**明确"没找到"的部分（同样是结果）**：
```
① 方向 1 中【量子疤痕（quantum scars）】：检索未发现任何与 β 相关的机制。
   疤痕文献全部围绕"本征态在相空间的反常重叠"，是**态**的判据，不是**谱的位置**判据。
   ⟹ 判 DEAD，来源：PMC "Genuine quantum scars in many-body spin systems"、PRX Quantum 2, 030349
   等（均为检索间接来源，未逐条核验）。建议登记进 NO-GO 关键词表。
② 方向 1 中【PT 对称 ⟹ 实谱】：本报告未找到 2024–2026 的**新机制**（仅 2023 年的
   arXiv:2309.01382 *A symmetry perspective of the Riemann zeros* 与 2017 年的 Bender–Brody–Müller，
   两者均被本项目/社区判为"对 ζ 无实质推进"）。⟹ **本子方向无新货。**
③ 方向 2 中【反射正性约束谱、且不等价于构造】：**未找到任何一篇。**
   唯一严格路线（2-C）的间隙来自欧氏方向的存在，不是来自"正性本身"。
   ⟹ 这是本报告最强的**方向级负面结论**：**"反射正性 ⟹ 间隙"这条类比无法迁移到 ζ。**
④ 方向 3 中【外势/缺陷使平衡测度被不对称扰动、且痕迹留在体量可观测量上】：
   只找到 3-A（非厄米秩一扰动）这一族，**未找到**"对称 log-gas 被不对称外势破坏"的近期专文。
   ⟹ 该子问题（"不对称 ⟹ 体痕迹"）在文献里**基本空白**。
```

---

# 三点总结

```
【一、哪个方向产出最多】
  方向 4（de Bruijn–Newman / Lehmer 对 / 零点密度）产出最多，且是唯一"天然含 β 分辨率"的方向。
  三条可用机制：① N(σ,T) 是**字面意义上对 β 的排除**（但排除能力恰在 σ→1/2 处退化 —— 即 β 墙的
  外部同型）；② Λ 是唯一以 β 为自变量的经典常数（但只有一个数，且夹逼宽度 0.2）；
  ③ 窄竖箱计数把 β 分辨率写成显式参数。
  **并列第一是方向 3** —— 因为对齐后（§0.5）发现项目**早已握有全文唯一"振幅载 β"的构造**：
  准晶体散射的峰系数 ∝ p_L^{β_m−1/2}（E28 / arXiv:2410.03673）。这是本报告全部条目里
  **唯一有显式 β 公式**的一条 —— 但它**不是本子代理发现的**，是项目自查的资产，此处仅做登记与归属澄清。
  方向 5 初看最有希望（5-C），**经对齐后下调为 β 盲**：项目已读至定理级并判定其统计量不含实部。

【二、哪个方向一无所获】
  方向 2（Yang–Mills / 正性）**干净落空**，且落空的形状很有信息量：
  · 2025 年高调的"构造性 SU(3) 质量间隙证明"**已被 arXiv 撤稿**（arXiv:2506.00284）；
  · 2026 年的 SU(N) 版本（arXiv:2606.19362）发表渠道不足以采信；
  · 唯一严格、定量的正性 ⟹ 间隙路线（Bauerschmidt–Dagallier 的 log-Sobolev）之所以成立，
    是因为存在**一条欧氏方向**；ζ 没有欧氏区域、没有概率测度 ⟹
    **"反射正性 ⟹ 定量间隙"只有形状相似，没有内容。**
  方向 1 的"量子疤痕"子方向与"PT 对称 ⟹ 实谱"子方向同样一无所获。

【三、下一步最具体的一个测试】
  做 4-A：**用 `zeros_odlyzko_2M.npy` 画出"无条件 β-排除能力的衰减曲线"** ——
  取前 2×10⁶ 个零点，计算 N(σ, T₀) 与 Kadiri/Chourasiya 显式上界的比值随 σ → 1/2⁺ 的爆炸曲线，
  并在同一图上叠上 2608.24827 的 Landau–Widom 衰减律与本项目 support-ceiling 的阈值。
  · 只需现有零表 + 现有脚本框架，1 轮计算；
  · **纪律强制**：必须明确写出"σ > 1/2 处真值恒为 0，本测试测的是**上界的松弛度**，
    不是"验证了没有离线零点"（T3/T6）；
  · 产出是**一张把 β 墙定量化、外部化的图** —— 正是本项目最该交付的那种产物（"讲清墙的形状"），
    而非又一次"接近证明"的幻觉。
  · **紧随其后的第二号测试**：5-C 的"关掉惯性项看结论是否仍成立" —— 一次计算即可判定
    Sylvester 惯性到底是**真做功**还是**装饰**（T8 筛）。这一步无论成败都是**干净结论**：
    **成立 ⟹ 惯性项是装饰，比例类论文的统计量确为 β 盲（与项目已有判断一致，外部确认）；
    不成立 ⟹ 惯性项真做功，则 "β 盲 ⟺ 无条件" 这条 NO-GO 的表述必须永久改写。**
  · 第三号（若时间允许）：3-A 的 E28b —— **检查不同 p_L 上的峰高是否恒相容**；
    若相容性给出 β = 1/2 ⟹ 真正的突破点；若恒相容 ⟹ 又一个自适应墙（**可判定**）。
    这是项目已列的"幸存指针①"，本轮检索**未改变**其地位。
```

---

**本文件不声称什么 ✗**
```
· 不声称任何被引论文正确（多数仅到摘要/片段级；引用状态已逐条标注 ✓✓/✓/?/✗）。
· 不声称本项目获得任何新数学成果。
· 不声称"未找到"等于"不存在"（T2）。
· 不声称 5-C 是"候选路线" —— 在 5-C 测试 2（关掉惯性项）的结论出来之前，它只是"必读一手来源"。
· 未修改任何既有文件；未提交（按任务要求）。
```
**检索工具**：tavily_search / tavily_extract / web_search（多次、按方向分组）。
**核验边界**：沙箱内**无直连网络**（arXiv API 经 curl 返回空），故所有标识符核验均经由检索工具抓取的
abs/PDF 页完成；标注为 "?" 的条目仅见检索索引。
