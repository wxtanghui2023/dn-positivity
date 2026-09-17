# 📚 **资产总表**（ASSETS REGISTRY）

> ## 🎯 **唐先生定位指令（2026-09-16 23:28 初版 ／ 23:33 修正为双轨）**
>
> $$oxed{	extbf{双轨制度}}$$
> $$	ext{(i)}\ 	extbf{突破级成果}\ \Longrightarrow\ 	extbf{可以发表论文}✓$$
> $$\qquad	ext{适用范围：LH／RH／GRH／哥德巴赫／孪生素数／}	extbf{任意其它素数猜想}	ext{／其它物理、数学模型}✓✓$$
> $$	ext{(ii)}\ 	extbf{过程性、价值不高的成果}\ \Longrightarrow\ 	extbf{自用资产}（	ext{登记即可，不发表}）✓$$
>
> **唐先生原话**：
> - 23:28：「我对这种小论文没啥兴趣，不用关注这种产出，但需要标记为我们自用的资产，
>   **这是我们在研究中比其他同行更强的地方**，包括以前的几篇论文，都是我们在后续可以引用的成果。」
> - 23:33：「LH, RH, GRH, 哥德巴赫，孪生素数，或者任何其它素数猜想，或者其它物理，数学模型，
>   **如果我们在研究中能够有突破，当然可以做论文发表**，但对于**过程中的价值不高的成果，作为自用资产就行**。」
>
> **性质**：本表是**自用资产登记册**；**突破级成果另行走发表流程**（二者不冲突）✓
> **用途**：后续工作中**引用**（"我们在 X 已建立 Y"），避免重复劳动 ✓

## 0. 登记纪律

$$\text{(1) 只登记}\ \textbf{我们自己的}（\text{非文献已有}）\ \text{且}\ \textbf{已核验／已定稿} \text{的条目}✓$$
$$\text{(2) 每条必须有}\ \textbf{可查位置}（\text{文件路径／DOI／commit}）✓$$
$$\text{(3) 状态须标}\ \textbf{已定稿／已核验／已封闭}，\ \text{不得写"已证明"若仅有结构判定}✓$$
$$\text{(4) 与既有索引交叉引用：}\ \texttt{B-SERIES-INDEX｜INDEX-BY-DIRECTION｜NOGO-registry}\ \text{｜}\texttt{CLOSED-ROUTES-MAP｜MASTER-STATUS-AND-CLOSURES｜PENDING-ITEMS-MASTER}✓$$

---

## A 类 · **已定稿论文资产**（外部可引用）

| ID | 资产 | 位置 | 内容（可引用表述） | 状态 |
|:--|:--|:--|:--|:--|
| **A-1** | **Li 系数线性范围** | `papers/li-range/` | $\lambda_n\ge0$ 对 $2\le n\le2T-O(1)$；$T$ ＝已验证高度；**无假设**；完全初等；含 **T-最优性 Remark**（范围上限由相位窗口须落在已验证区内决定；离轴项从不是瓶颈） | 已定稿（5 页，编译通过）✓ |
| **A-2** | **Brown Conjecture 3.2.7 经典情形** | `papers/brown-thm2-classical/` | $\tau=1$ 情形对**所有** $k\ge2,\ H>e$ 成立；**强于** Droll 的 $k\le2T^2\log T$；证明链＝六引理＋**Abel 含边界项**；**精确余量** $=\tfrac23\lvert b\rvert H^{-3}$（$b<0$ 是"燃料"；实测吻合 6 位且与 $k$ 无关） | 已定稿（5 页）✓ |
| **A-3** | **共享恒等式** | A-1／A-2 共用 | $\lvert1-\tfrac1\rho\rvert^2=1+\tfrac{1-2\beta}{\beta^2+\gamma^2}$（A 用相位窗口⟹正性；B 用 Abel⟹不等式；双向引用） | 已定稿 ✓ |
| **A-4** | **dn-positivity 定稿** | Zenodo **DOI 10.5281/zenodo.22044629** (v2.0.1) | $D_n>0$ 无条件正性；全常数解析化；作者 Hui Tang；ORCID 0009-0003-5745-4820 | 已发布 ✓ |
| **A-5** | **GitHub 公开仓库** | `wxtanghui2023/dn-positivity` (public) | A-4 的代码／论文 | 已发布 ✓ |
| **A-6** | **投稿包（备用）** | `submission/ANNALS-*`｜`release/paper-dn-positivity-{CN,EN}.*` | Annals 方案 A/B ＋检查清单；arXiv tex | 就绪未投 ✓ |
| **A-7** | **两条转换律 ＋ 突破点判据** | `papers/conversion-laws/main.md` | 「Two conversion laws for criteria equivalent to RH, and a criterion for where a breakthrough can occur」（Hui Tang, draft v1, 2026-09-12）。比较**六个** RH 等价判据的可达参数范围，观察到两条**转换律**：**T² 律**（系数型判据：可达指标 ＝ 已验证高度的平方）与 **log 律**（矩／阶／相位型：有效自由度 ~ log）；由此给出**突破点的可操作判据**：探针的"指标↔高度"对应 $h(n)$ 若慢于 $\sqrt n$ 增长，则可达范围优于目前的 T²；理想探针 $h(n)$ 应尽量接近常数。⚠️ 两律均为**跨方向经验观察，机制未证**；不主张 RH 真值 | 草稿 v1 ✓ |
| **A-8** | **GRH 配正性判据 ＋ 八模验证 ＋ GRH→哥德巴赫链** | `papers/grh-criterion/main.md` | 「A Pair-Positivity Criterion for the GRH, with Eight-Modulus Verification and the GRH→Goldbach Chain」（Hui Tang, draft v1, 2026-09-12）。**轨道恒等式** $Q_\chi-Q'_{RH,\chi}=\sum_{\rm orbits}m_\rho P_{\gamma_\rho}(\delta_\rho)$，$P_\gamma(\delta)=\delta^2M_2/(2U^2D_+D_-)$ 系数**全正**只要 $\gamma>1/\sqrt5$；而每个 L-零点有 $\gamma\ge6.02>1/\sqrt5$ ⟹ $Q_\chi=Q'_{RH,\chi}\iff$ 全零点在 $\Re s=\frac12$。**判据非证明**（等式未证，与 GRH 同难）。数值：模 3,4,5,7,8,9,11,13，最大相对偏差 $1.4\times10^{-10}$，$P_\gamma$ 按 $\gamma^{-6}$ 衰减。**先前一次无条件证明尝试记录为 broken，不再复活** | 草稿 v1 ✓ |
| **A-9** | **九条转换判据观察（N1–N9）** | `papers/notes/main.md` | 「Notes on conversion criteria and their obstructions」——九条自足短观察（结构恒等式／数值标定律／解释性二分／关于某具体路线的负面结果）。**明示：无一条是朝 RH 证明的进展**；每条或为经典事实的小实例核验，或为对已测路线的负面陈述；附档案诚实规则（**not found ≠ does not exist**）与四标签（核验／引用／推导／猜想） | 草稿 v1 ✓ |

> **⭐ A-2 的 Droll 关系（唐先生指定重点）**：`papers/brown-thm2-classical/` **正是 Droll 相关论文** ——
> $$\textbf{我们的 Theorem 1}\ 	extbf{强于}\ 	ext{Droll 已发表内容}：\text{[Dr12] Conjecture 1.7.10}\ 	extbf{限制}\ k\le2T^2\log T，\ 	ext{而我们覆盖}\ \textbf{所有}\ k\ge2,\ H>e✓✓$$
> $$\text{且}\ \texttt{docs/N2-chain-confirmed.md}：\ 	ext{Droll 原文明确}\ \textbf{Conjecture 3.2.7 就是 Brown Lemma 5 的修复}✓$$
> $$\text{取证档：}\ \texttt{docs/P8-DROLL-verbatim-reading.md}（逐字读）✓$$
> **诚实缺口（README §7 自述）**：① near 积分的**闭式界**；② **显式局部计数**；③ 原文被 paywall（未取得 Brown 2005 原文）✓
> **数值可复现**：每个数值声明均由归档脚本产生（`scripts/BL7_*`｜`BL10_*`｜`BL11_*`｜`BL14_*`｜`NB1_*`），按 `PROTOCOL-CODE-ARCHIVE.md` R1–R7，**无临时代码支撑的结论** ✓

---

## B 类 · **形式化资产（Lean）**

| ID | 资产 | 位置 | 内容 | 状态 |
|:--|:--|:--|:--|:--|
| **B-1** | **V316 变分闭合** | `~/lean-repro/zeta23-local/V316_kernel_bound.lean` ＋ `docs/V316_kernel_bound.lean` | **60 条声明**，ERROR_COUNT=0，**零 sorry／零 axiom**，**未用 RH**；kernel_bound→Q_pos→Bfun→弱 E–L 全链 | 已冻结为基线 ✓ |
| **B-2** | **Zeta23 三层审计** | `docs/V298`｜`V300`｜`V301/V302` | Ceiling.lean 三层审计（带宽仅从 validity 侧进入）；§5 off-diagonal 𝒪₁ 逐行核（MV 无 pair-correlation 内容 ⟹ $c^{\rm geom}$ 是普适几何常数） | 已完成 ✓ |

---

## C 类 · **技术观察**（关于已发表论文的具体、可核验事实）

| ID | 资产 | 位置 | 内容 | 状态 |
|:--|:--|:--|:--|:--|
| **C-1** | **$F_3$ branch-SHARP** | `docs/V2-28A` | BC §3 退化支（$a_1\ell_1=a_2\ell_2$）的**构造性 witness**：$D_b^{\rm deg}\asymp LM^{1-o(1)}$ ＝ BC 上界 ⟹ **§3 退化计数无幂次改进空间** | 已封闭 ✓ |
| **C-2** | **$L^5$ 逐幂分解** | `docs/V2-35C`｜`V2-35D`｜`V2-36` | $L^5=L_{\rm Weil}\cdot L_{\rm transition}\cdot L_{\ell_2,\ell_2'}\cdot L_u$ **（$1+1+2+1$）**，逐字溯源 (4.9)–(4.29)；每幂的数学来源已指名 | 已定位 ✓ |
| **C-3** | **反向 C–S 净幂次 $=0$** | `docs/V2-33/33b/33c/33d` | 单 $\ell$ 反向 C–S：$L^{-1}\times L\times L^{o(1)}=L^0$；机制＝**同指标相位共轭相消**（代数事实）⟹ 不产生新估计对象 | **CLOSED** ✓ |
| **C-4** | **$17/33\iff17r+t=8$** | `docs/V2-13`｜`LIE3A` | BCR 坐标下的精确边界线；$(9/20,7/20)$ 恰在线上；**17/33 是历史最优点，非架构天花板** | 已核 ✓ |
| **C-5** | **互反恒等式在 BC 中的角色** | `docs/V2-32` | 三变量两两互素：$\frac{\overline{\alpha\gamma}}\beta+\frac{\overline{\beta\gamma}}\alpha+\frac{\overline{\alpha\beta}}\gamma\equiv\frac1{\alpha\beta\gamma}$；BC **自己**用它把 $\tilde\ell\tilde\ell'$ 模逆元改写为分母型 | 逐字取证 ✓ |
| **C-6** | **$L^{5/2}$ 的产生机制** | `docs/V2-28B` | $L^5=L^4_{\ell\text{-count}}\times L_{PQ}$，经 C–S 开方；**绝对值化损失已被 BC 显式回收**；**Weil 不产生 $L$-幂**（Weil 在 $n_2'$ 上） | 已定 ✓ |
| **C-7** | ⭐⭐⭐ **BCR Appendix A · Proposition 4（Conjecture 1 的匹配下界）** | `external_refs/bettin_chandee_radziwill_1411.7764.txt` L3783+｜`docs/T1-2-*` | $A\ll(MN)^{1/2+\varepsilon}$ 时 $\max_{\alpha,\beta,\nu}|S_{A,M,N}|\gg(AMN)^{1/2-\varepsilon}(M+N)^{1/2}+A(M+N)^{1-\varepsilon}$；BCR 逐字自述 (1.4) **best possible, up to $\varepsilon$-powers** ⟹ **目标形态已证最优**（全部难度＝从 $(9/20,7/20)$ 走到 $(0,0)$）。方法：互反＋素数 $\equiv1,3\bmod4$ 极值系数＋Poisson→Ramanujan 和 | 已核 ✓ |
| **C-8** | ⭐⭐⭐ **BC 全文无谱理论**（引擎清单） | `docs/T1-3-*`｜`docs/ref-bc-ar5iv-plaintext.txt` | Kuznetsov／spectral／eigenvalue／Maass／Petersson／Poincaré／large sieve **全 0 命中**；`amplification` 仅 1 处且属 DFI 方法；$[DI]$ 仅 2 处（引言**背景对比**：DI 需权重特殊结构／DFI–BC 处理任意权重＋参考文献）⟹ **BC 引擎＝Weil 单点界（附录 A「Weil bound for incomplete Kloosterman sums」）＋Ramanujan 和＋整除计数＋C–S 变量选择** ⟹ **谱升级路线出局** | 已核 ✓ |
| **C-9** | ⭐⭐⭐ **DFI→BC 增量机制＝架构变更**（非估计改进） | `docs/T1-3-*` §5｜`docs/ref-bc-ar5iv-plaintext.txt` L98 | 增量 $\tfrac1{48}\to\tfrac1{20}$ 来自逐字 “we keep a **longer diagonal** when using the Cauchy-Schwartz inequality” ⟹ C–S 作用集由｛除 $\ell_1,\ell_2$ 外｝收缩到｛除 $d,a_1,\ell_1,\ell_2$ 外｝ ⟹ **下一次增量大概率同样需架构变更** | 已核 ✓ |
| **C-10** | ⭐⭐ **BCR Corollary 2：三阶矩正确阶无条件成立** | `external_refs/bettin_chandee_radziwill_1411.7764.txt` L233+ | $\int_T^{2T}|\zeta(\tfrac12+it)|^3dt\ll T(\log T)^{9/4}$；逐字 “Previously Corollary 2 was known **only on the assumption of the RH**”；§6.1 给出 $2k$ 矩（$k=1+1/n$）路径 ⟹ **T3 须重新定位** | 已核 ✓ |
| **C-11** | **BCR 的 [DI]/Watt 使用范围** | `docs/T1-3-*` §1 | BCR 中 `Deshouillers` 7 处**全部**在另一应用：$[DI84]\to$Proposition 2（Theorem 3 用）；$[DI83]$＋Watt$\to$Theorem 4/J（两多项式之积）⟹ **与 Theorem 2／(1.3) 无关** | 已核 ✓ |
| **C-12** | ⭐⭐⭐ **T2-1：fiber **饱和**（变量识别证明）** | `docs/T2-1-T2-2-*` | $\tilde\ell_1=\ell_1/\mathfrak q_1$、$\tilde\ell_2=\ell_2/\mathfrak p_2$（L216/L279 逐字）：**(4.26) 约束 $(d,d')$**（$\tilde\ell_2'd\equiv\tilde\ell_2d'$ 给定 $\ell$ 时确定 $d$）；**(4.27) 消去 $\tilde\ell_1$**（$\tilde\ell_1$ 只现于 LHS ⟹ 是未知量 ⟹ 可解性自动，$(\mathfrak p_1,u)\mid\mathfrak p_1(\cdots)=0$ 恒成立）⟹ **$(\ell_2,\ell_2')$ 只承担整除约束** ⟹ $N_2=L^{2+o(1)}$ **饱和**（三情形核对：同阶／同阶／保守）。**不是「$u<L$ ⟹ 有解」跳步** | 已证 ✓ |
| **C-13** | ⭐⭐⭐ **T2-2：divisor alignment 无幂次 saving** | `docs/T2-1-T2-2-*` | 计数增益 $(\mathfrak p_2\mathfrak q_2)^{-2}$ vs 分母 $\mathfrak p_2^{-3}\mathfrak q_2^{-1}$ ⟹ 差异仅单幂次 $\mathfrak p_2^{\pm1},\mathfrak q_2^{\pm1}$ ⟹ 求和 $=\log^{O(1)}L=L^{o(1)}$；$\mathfrak q_2=1$ 情形链的计数（$L^2/\mathfrak p_2$）**保守大于**实际（$L^2/\mathfrak p_2^2$）⟹ 无「已入分母又被重复兑现」；§4.1.4 逐字：非平凡除因子**只**在 $(\ell_1\ell_1',\ell_2\ell_2')=1$ 情形，此时四者全 $=1$ 自动坍缩 | 已关闭 ✓ |
| **C-14** | ⭐⭐⭐ **BC 架构级 closure（六条合成）** | `docs/T2-1-T2-2-*` §T2 最终判据 | (1) BCR Prop 4 目标形态已证最优；(2) BC 全无谱机器 ⟹ 无谱升级；(3) $F_3$ SHARP；(4) $L^5$ 四源审计全锁定；(5) $N_2$ 饱和（T2-1）；(6) divisor alignment 无幂次 saving（T2-2）⟹ **BC 路线在已审范围内形成干净的架构级 closure**（$17/33$ 与 $L^5$ ＝结构性成本，非粗估） | 已合成 ✓ |
| **C-15** | ⭐⭐⭐ **(4.19) 的相位结构（分母清单＋变量相消）** | `docs/T3-1B-2-*` §1–§2.1 | (4.19) 是**模 1 有理数**，四个分母显式：$\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'$／$b\tilde\ell_1\tilde\ell_1'\mathfrak p_1n_1'\mathfrak q_1\mathfrak q_2n_2'$／$b\mathfrak p_2$／$b$ ⟹ **不存在单一固定模数**（其中 $\tilde\ell_1\tilde\ell_1'\mathfrak q_1$ 是变量）。**逆元约定＝相对该分式之分母** ⟹ (4.11) 项 2 的逆元模数 $q=\mathfrak p_1n_1'$。**展开后变量因子恰相消**（$\Delta$ 的 $\tilde\ell_2\tilde\ell_2'$ 部分坍塌为常数 $\overline{C_0}$；另一部分乘逆元后得 $\overline{C_0}\tilde\ell_1\tilde\ell_1'\mathfrak q_1(da_1\overline{\tilde\ell_2}-d'a_1'\overline{\tilde\ell_2'})$，除以项 1 分母后变量因子消去）⟹ 固定分母须**逐式导出** | 已核 ✓ |
| **C-16** | ⭐⭐⭐ **T3-1B 判定 DEAD（定量理由）** | `docs/T3-1B-2-*` §5 | $X\asymp L/(\mathfrak p_2\mathfrak q_2)$（整除结构确定）；$q=\mathfrak p_1n_1'\asymp N/\mathfrak p_2$ ⟹ $\frac{X}{\sqrt q}\asymp\frac{L}{\mathfrak q_2\sqrt{\mathfrak p_2N}}$；最优情形 $\mathfrak p_2=\mathfrak q_2=1$ 需 $L\gg\sqrt N$。代入平衡最优 $L^*=\frac{M^{4/5}}{b^{1/5}A^{2/5}N^{7/10}}$，平衡区 $M\asymp N$ ⟹ $L^*\asymp N^{1/10}$ ⟹ $\frac{X}{\sqrt q}\asymp N^{-2/5}\ll1$ ⟹ **DEAD**（cancellation **存在但尺度不够**：$\ell$-区间太短） | 已判 ✓ |

---

## D 类 · **封闭判据／负面资产**（可引用为"此路已封"）

| ID | 资产 | 位置 | 内容 |
|:--|:--|:--|:--|
| **D-1** | **有限⟹无限（八类穷尽）** | `docs/V211` | 望远镜自击 ＋ 八类机制全部映射到已封类 ＋ **RH 自身是 $\Pi_1$** ⟹ 框架＝RH 的逻辑形状 |
| **D-2** | **极限交换** | `docs/V320-A`｜`V321`｜`V262` | 紧致＋连续 ⟹ $\varprojlim\ne\emptyset$；**非满射不制造空极限**；$\lim^1\ne0$ 只在有限阶段可见 |
| **D-3** | **层诊断（Archimedean）** | `docs/V144`｜`V145` | **ζ 零点不在 motive 层，在 Archimedean 层** ⟹ 所有 Frobenius／几何类比失败的根因＝**层错了** |
| **D-4** | **Buium $\delta$-几何 NO-GO** | `docs/gate10-*` | $\delta_p(x)\sim x^p/p$ ⟹ **Frobenius 尺度 ≠ RH 尺度** ⟹ P-Scale 双杀 |
| **D-5** | **自守输入关闭** | `docs/gate18-*` | 高阶自守陈述**包含** GL(1) 而非外部约束；尖点情形 ζ 不出现；诱导情形伴随因子同深度 |
| **D-6** | **单一缺口形式** | `CLOSED-ROUTES-MAP.md` | 【算术特异 ＋ 非 completion ＋ 非 $L$-测量 ＋ limit-seeing/finite-blind】 |
| **D-7** | **$\theta$ vs $\lambda$ 不等价** | `docs/HE-JIA1-K4-*` | mollifier 长度与 V316 变分载体**机制不等价** ⟹ "一堵墙" doctrine 的部分证伪 |
| **D-8** | **GM vs mollifier H3-A** | `docs/LIE1B-*` | GM 的 $N^{3/4}$ 大值机器**不攻击** mollifier 非对角墙（对象不同型） |
| **D-9** | **V316 三出口封闭** | `V316-FREEZE`｜`V317`｜`V318` | $\lambda>1$ 的已有来源（S1–S8／C1–C8／K1–K7）**全部 DEAD** |
| **D-10** | **理论类型不匹配** | `docs/V148` | RH ⟺ ι: $\rho\mapsto1-\bar\rho$ 无自由轨道（**缺席型**）；canonical symmetry-breaking ＝ torsor 平凡化（**局部选择型**） |

---

## E 类 · **方法论资产**（可复用工具，跨项目适用）

| ID | 资产 | 出处 | 用途 |
|:--|:--|:--|:--|
| **E-1** | **T10 勘误纪律** | 全项目 | 勘误**追加**于原档，绝不重写；错误留痕 |
| **E-2** | **四态标签** | MASTER §5 | ①不可能／②族内失败（**不移为①**）／③⟺RH（重述）／④未决 |
| **E-3** | **N1–N13 反升级清单** | 全项目 | 不得把"没找到"写成"不存在" |
| **E-4** | **净幂次账** | `docs/V2-33*` | 新自由度收益 × 代价 × 新增稀疏度，**三者同时看** |
| **E-5** | **反走私铁律** | `docs/E6-13` | 同一指数 $\ne$ 同一机制；形式复杂度 $\ne$ 幂次障碍 |
| **E-6** | **取证升级** | 本日 | **本地抓取＋剥标签＋grep** 远比定向抽取可靠（1.05 MB HTML 一次取到 (4.9)/(4.10) 全文） |
| **E-7** | **饱和 witness 优先** | `docs/V2-28A` | 判定"上界是否可改进"时，**先构造达到上界的 witness** |
| **E-8** | **定义层归一化** | 全项目 | 先证"搜索空间未被缩小"，再投入搜索 |

---

## F 类 · **早期数值／验证资产**（2026-09-11 登记，沿用）

| ID | 资产 | 状态 |
|:--|:--|:--|
| **F-1** | **Guinand 相位锁定**：$\sum_k\sin(\gamma_k\log p)=O(1)$ 机制＝Guinand/Weil 显式公式；微扰 $10^{-7}$ 即爆炸到 33000 | 已核验 ✓ |
| **F-2** | **Mellin 算子 β-提取**：由**素数单独构造**，读出前 ~500 零点 $\beta\approx1/2$（最大偏差 <0.1） | 已核验 ✓ |
| **F-3** | **经典核 Φ 的 TP₅ 失败**：TP₂–TP₄ 但非 TP₅；120 位复核＋Gaussian 对照 ⚠️（TP₅ 读数已于 09-12 撤回对象层面） | 数值成立 ✓ |
| **F-4** | **大规模负面地图**：数十处已定位停滞点，含外部独立验证的 $\beta$-墙 | 已审计 ✓ |

---


---

## 🚦 发表轨判定（按 23:33 双轨制度逐条标注）

$$	extbf{突破级判据}：	ext{(a) 解决／实质推进一个公开猜想（LH／RH／GRH／哥德巴赫／孪生／其它素数猜想）；}\ 	ext{(b) 或给出其它物理／数学模型的}	extbf{新定理}✓$$
$$	extbf{过程性判据}：	ext{封闭某条路线／给出负面判据／记录一个技术事实／建立方法论工具}✓$$

| 资产 | 判定 | 理由 |
|:--|:--|:--|
| **A-1** Li 系数线性范围 | **已发布轨**（Zenodo/GitHub）✓ | 具体、可证、无假设的定理 |
| **A-2** Brown Conj 3.2.7 经典情形 | **已发布轨**✓ | 强于 Droll，精确余量 |
| **A-3** 共享恒等式 | 随 A-1/A-2 附属✓ | 非独立 |
| **A-4/A-5** Zenodo／GitHub | **已发布轨**✓ | 定稿＋公开 |
| **A-6** 投稿包 | **待决**（等 A-1/A-2 定稿策略） | 非新成果 |
| **A-7** 两条转换律 | **过程性（但含可操作判据）** | 跨方向经验观察，机制未证；★ 但"$h(n)$ 慢于 $\sqrt n$ ⟹ 优于 T²"是**可操作的攻墙判据** |
| **A-8** GRH 配正性判据 | **过程性（判据类）** | 与 GRH 同难的等价重述；八模验证是有价值的具体核验；broken 纪录保留 |
| **A-9** 九条观察 | **过程性** | 明示非进展；负面结果与经典事实核验 |
| **B-1** V316 60 lemmas | **过程性**（形式化资产） | 工具，非猜想级结论 |
| **B-2** Zeta23 三层审计 | **过程性** | 审计 |
| **C-1** $F_3$ branch-SHARP | **过程性**（可升级为技术注记） | 关于 BC 论文的具体事实；★ 若与 C-2/C-3 合并，可成一篇针对该论文的技术注记 |
| **C-2** $L^5$ 逐幂分解 | **过程性**（同上） | 具体、可核验 |
| **C-3** 反向 C–S 净幂次 $0$ | **过程性**（同上） | 代数事实 |
| **C-4～C-6** | **过程性** | 观察 |
| **D-1～D-10** | **过程性**（负面判据，本项目的核心资产） | 封闭判据的价值在于**防止重投** |
| **E-1～E-8** | **过程性**（方法论工具） | 跨项目可复用 |
| **F-1～F-4** | **过程性**（数值／验证） | F-1 敏感性结果醒目，但非猜想级 |

$$	extbf{当前无}\ 	extbf{突破级} 	ext{条目}✓\quad\Longrightarrow\ 	ext{全部按}\ 	extbf{自用资产} 	ext{登记；}\ 	ext{突破级出现时}\ 	extbf{另行走发表流程}✓✓$$

$$	extbf{唯一"发表轨预备候选"}：\ oxed{	ext{C-1＋C-2＋C-3 合并为"关于 BC (Adv. Math. 328) }\S4.1.3	ext{ 的幂次账与技术注记"}}✓$$
$$\qquad	ext{定位：}\ 	extbf{技术注记／评论}，\ 	ext{非猜想级突破} \Longrightarrow\ 	ext{按唐先生标准仍属}\ 	extbf{过程性}✓\quad(	ext{登记即可，不必发})✓$$


---

## 🎯 待攻目标（战术轨）

> 唐先生 2026-09-16 23:47 裁定战略空间搜索完毕 ⟹ 转战术硬啃 ✓
> **详见**：`docs/TACTICAL-PLAN.md` ✓

| # | 目标 | 判据 | 状态 |
|:--|:--|:--|:--|
| **T1** | Kloosterman 分数指数路线（主攻） | $17r+t<8$ | **T1-1～T1-4 全部完成（2026-09-17）**；入口已逼至「需表述新 C–S／对角架构」 |
| **T2** | $F_5$ sharpness（副线） | 饱和 witness 或 $L^{-\delta}$ | ✅ **完成（2026-09-17）**：T2-1 饱和（变量识别）＋ T2-2 关闭 ⟹ 架构级 closure |
| **T3** | 三阶矩 | $X>T^{2/3-\varepsilon}$ | ⚠️ **须重定位**（BCR Cor 2 已给正确阶，见 C-10） |
| **T4** | 大值估计可移植性 | 族内推进 | 部分 |

## 维护规则

$$\text{(1) 新资产产生时}\ \textbf{当日登记} \text{（含路径＋状态＋可引用表述）}✓$$
$$\text{(2) 状态变化（如 OPEN→CLOSED）}\ \textbf{追加勘误}，\ \text{不覆盖原文}✓$$
$$\text{(3) 引用时}\ \textbf{引本表 ID}（\text{如 "见 C-2"}）✓$$
$$\text{(4) 与}\ \texttt{DIRECTION-LOOP-STOP-verdict-and-assets.md}\ \text{（09-11）}\ \text{并存：后者为当时的 A1–A5 快照，本表为}\ \textbf{统一总表}✓$$

---
*建档：2026-09-16 23:30｜修正：23:36（双轨＋发表轨）／23:46（补 A-7/A-8/A-9＋Droll）／23:49（增战术轨待攻目标）｜依据：唐先生 23:28／23:33／23:45／23:47 指令*
