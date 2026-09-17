# 📚 **资产总表**（ASSETS REGISTRY）

> ## 🎯 **唐先生定位指令（2026-09-16 23:28 初版 ／ 23:33 修正为双轨）**
>
> $$\boxed{\textbf{双轨制度}}$$
> $$\text{(i)}\ \textbf{突破级成果}\ \Longrightarrow\ \textbf{可以发表论文}✓$$
> $$\qquad\text{适用范围：LH／RH／GRH／哥德巴赫／孪生素数／}\textbf{任意其它素数猜想}\text{／其它物理、数学模型}✓✓$$
> $$\text{(ii)}\ \textbf{过程性、价值不高的成果}\ \Longrightarrow\ \textbf{自用资产}（\text{登记即可，不发表}）✓$$
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
> $$\textbf{我们的 Theorem 1}\ \textbf{强于}\ \text{Droll 已发表内容}：\text{[Dr12] Conjecture 1.7.10}\ \textbf{限制}\ k\le2T^2\log T，\ \text{而我们覆盖}\ \textbf{所有}\ k\ge2,\ H>e✓✓$$
> $$\text{且}\ \texttt{docs/N2-chain-confirmed.md}：\ \text{Droll 原文明确}\ \textbf{Conjecture 3.2.7 就是 Brown Lemma 5 的修复}✓$$
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
| **C-17** | ⭐⭐⭐ **T3-1C 全支 DEAD ＋ 聚合账** | `docs/T3-1C-0-C-1-*`｜`docs/T3-1C-2-*` | **T3-1C-0**：$\text{C--S 施于}\ T\ \text{重复补集}\ S$；BC 重复 $\{d,a_1,\ell_1,\ell_2\}$（四对带撇），DFI 只重复 $\{\ell_1,\ell_2\}$ ⟹ **"longer diagonal" 精确含义＝被重复集扩大**。**T3-1C-1 DEAD**：$(d,\tilde\ell_2)$-$(d',\tilde\ell_2')$ 处可用联合关系穷举＝互素（用尽）＋行列式（$u,v$ 已用）＋$\Delta$（已用）⟹ 任何 partial diagonal 必为 $u,v,\Delta$ 函数（C2 失败）⟹ 坍缩点＝行列式类 ⟹ **BC 的 longer diagonal 已含此层**。**T3-1C-2 DEAD**（见 C-18） | 已判 ✓ |
| **C-18** | ⭐⭐⭐ **新判据：门槛由模数决定，聚合无效** | `docs/T3-1C-2-*` §3–§4 | 情形 (a) 同轴聚合：$K_{\max}\lesssim\mathfrak p_2\mathfrak q_2$，最有利点 $O(1)\ll N^{2/5}$ ⟹ DEAD。情形 (b) 跨轴相位格映射：C4-1 **通过**（相位对 $(d,\overline{\tilde\ell_2})$ 双线性 $=\frac{\alpha}{q}d\overline{\tilde\ell_2}$；完整双和 **恒为零** ⟹ 真实相消存在），但 gain $\asymp L^{1/2}N^{-1/4}$ ⟹ 阈值仍 $L\gg N^{1/2}$（**与 T3-1B 同一阈值**）；$L=N^{1/10}$ ⟹ gain $=N^{-1/5}\ll1$，shortfall $=\frac{\sqrt N}{L}=N^{2/5}$。**结构结论（不依赖具体界）**：两轴同尺度下相消只能来自 $\sqrt q$，而聚合 **不改变模数** $q=\mathfrak p_1n_1'$ ⟹ 阈值不变。⟹ **要降门槛必须改变相位模数，而非聚合同一模数下的项**（新判据，直接决定 T3-1A 形式） | 已判 ✓ |
| **C-19** | ⭐⭐⭐ **T3-1A-1 DEAD：Weil 的 $\sqrt q$ 是 conductor-level barrier ＋ 四层淘汰总账** | `docs/T3-1A-1-*` | **A1**：$(\ell_1,n_1'n_2'b\vartheta)=1$（(4.10) 逐字）＋ $\mathfrak p_1\mid\ell_1$ ⟹ $(\mathfrak p_1,n_1')=1$ ⟹ $q=\mathfrak p_1n_1'$ 为两互素因子之积（CRT 干净）。**A2**：$\overline{\tilde\ell_2}$ 是单位 mod $q$ ⟹ 每局部因子非平凡，除非 $q_r\mid\alpha_{\rm tot}\Rightarrow q_r\mid d$；故唯一候选 $q_0\approx(q,d)$，而 $q_0\mid d\asymp L$ ⟹ $q_0\ll L^{o(1)}$ ⟹ **仅次幂**。**A3**：相位可分 ⟹ CRT 分解 $\ne$ 模数下降（每 $q_r$ 皆单位型非平凡）。**A4**：三个假 ALIVE 全识破（①正是本例；②$\mathfrak p_1=1$ 只是参数情形；③$q/u$ 禁止＝重复兑现 $u$）⟹ **所有局部 conductor 非平凡** | 已判 ✓ |
| **C-20** | ⭐⭐⭐ **搜索空间大幅坍缩（四层淘汰）** | `docs/T3-1B-2-*`｜`T3-1C-1-*`｜`T3-1C-2-*`｜`T3-1A-1-*` | **(1)** fiber cancellation（单 $\ell_2$-fiber 逆元振荡）DEAD（$X/\sqrt q\asymp N^{-2/5}$）；**(2)** cross-fiber aggregation DEAD（模数不变 ⟹ 阈值不变）；**(3)** partial diagonal DEAD（坍缩为行列式类 $=u,v,\Delta$）；**(4)** conductor-reducing Weil DEAD（局部 conductor 全非平凡）⟹ **在 $\mathfrak p_1n_1'$ 模数层的一切「振荡侧」改造已被逐一排除** | 已判 ✓ |
| **C-21** | ⭐⭐⭐ **T3 CLOSURE（严格限定作用域）＋ 五段总账** | `docs/T3-CLOSURE-fixed-q-scope.md` | $\mathrm{T3\ Closure}=\mathrm{DEAD}_{\mathrm{fixed\text{-}q}}+\mathrm{R2,R3,R4\ residuals}$。四命题：**C1**（$\frac{X}{\sqrt q}\asymp\frac{L}{\mathfrak q_2\sqrt{\mathfrak p_2N}}\ll N^{-2/5}$，单纤维失败）｜**C2**（aggregation $\ne$ conductor reduction）｜**C3**（partial diagonal $\subseteq\sigma(u,v,\Delta,\text{coprimality})$）｜**C4**（CRT factorization $\ne$ conductor reduction；未找到 $q_0\gg N^\delta$）。**五段**：T1 无谱引擎｜T2 无固定幂 slack｜T3 振荡四层 DEAD ⟹ BC 原架构内部改造空间基本封闭 | 已收口 ✓ |
| **C-22** | ⭐⭐⭐ **（甲)-1／（甲)-2 全关闭（BC 内部改 conductor 路线穷尽）** | `docs/JIA-1-*`｜`docs/JIA-2-*`｜`docs/JIA-2-R1R2-*` | **（甲)-1**：$q=\mathfrak p_1n_1'=\frac{n_1}{(\ell_2,n_1)}$ ⟹ 规则（[结构判定]）$q=\frac{\text{modulus}}{(\text{被求逆变量},\text{modulus})}$；降幅 $\le$ 被求逆变量尺度 ⟹ 需 $q_0\gg N^{4/5}$，而可用 $\le L=N^{1/10}$ ⟹ shortfall $N^{7/10}$ **DEAD**。**（甲)-2**：$\ell_1n_1\equiv\ell_2n_2(\bmod m)$ 的**互补除子** $d$ 消 $m$（除子对换＋reciprocity）⟹ **消 $m$ 本身就是 conductor 降阶**（$N^2\to N$）⟹ 「保留 $m$」无条件合法路径不存在；$S_1$ DEAD、$S_2$ GAP。**R1＋R2 终刀**：$A\le N^2T^{-1+\varepsilon}$，$\theta<\tfrac{17}{33}$ ⟹ $A\lesssim N^{1/17}$（需 $A\gg N^{4/5}$，shortfall $N^{63/85}$）；$g\lesssim AN\le N^{18/17}\ll N^{9/5}$ ⟹ large-$g$ 层**为空** ⟹ **同因 FAIL** ⟹ **（甲）整体关闭** | 已判 ✓ |
| **C-23** | ⭐⭐⭐ **三条独立链条同向：BC 架构内降 conductor 路线穷尽** | 同上 | **(1)** T3-1A-1 局部 conductor 全非平凡（Weil 的 $\sqrt q$ 是 conductor-level barrier）｜**(2)** （甲)-1 降幅 $\le$ 被求逆变量尺度（尺度上界锁死）｜**(3)** （甲)-2/R1R2 应用区间 $A\lesssim N^{1/17}$（既不给 conductor gain，也不给 large-$g$ 层）⟹ 机制不同、结论一致。**作用域**：固定 $q$／BC 原 C–S 组织／BCR 应用参数——**非**「BC 不可能改进」 | 已判 ✓ |
| **P-1** | ⭐⭐⭐ **（丙）协议 ＋ finite-blind→limit-visible 原型（数值已跑）** | `docs/P0-*`｜`docs/P1-alpha-*`｜`scripts/p1alpha_*.py` | **P0 协议**：$\text{Audit}\ne\text{Discovery}$；生成条件 G1--G4；验收只允许 ①ALIVE／②FALSE／③UNRESOLVED。**P1-$\alpha$ 数值原型**（$N=10^7$）：G2 盲——$\text{sign}(\pi(x;4,1)-\pi(x;4,3))$ 在 $x\le10^7$ 翻转 **10 次**（密集区 $\sim6.2\times10^5$）⟹ 任何有限层都给出错误的领先判断；G3 显影——$D(X)=\sum_{p\equiv3}\frac1p-\sum_{p\equiv1}\frac1p\to0.334964$ **稳定收敛**，而等权计数差 $=227$ **无极限** ⟹ **调和权重杀掉有限涨落、产生极限**。**②FALSE 事件**：我给的 $D_\infty=\log(4/\pi)=0.2416$ 被数值杀掉（偏差 38.7%），纠正为 $\log\frac4\pi+\frac12\sum_{p>2}p^{-2}-\frac13\sum\chi_4(p)p^{-3}+\ldots\approx0.3358$，与实测吻合 $\sim8\times10^{-4}$。**定位**：已知现象（Littlewood／Rubinstein–Sarnak），作用是**机制原型**（可复现、可数值判死），供 G4 搬运 | 已跑 ✓ |
| **P-2** | ⭐⭐⭐ **③-A 有限数据证书化边界（整合性）** | `docs/P3-A-*` | 三层延拓类必须分开：**(a)** 无约束类 ⟹ 平凡无界；**(b)** 算术类 ⟹ 由乘法子 $F_\sigma=\zeta(s)(1-q^{\sigma-s})$（合法 Euler 积、与前 $P$ 个局部因子一致）得仍无界（V259-A，类层面结果；单体 $\{\zeta\}$ 逃出，V270-B）；**(c)** 规则确定对象 ⟹ 规则＋有限数据**已唯一确定** $\zeta$，故数据量不是问题 ⟹ **正确二分是「可有限核验 vs 不可有限核验」**（V271-A cylinder barrier）⟹ 缺口 $\ne$ 更多数据／更好拟合 $=$ **arithmetic rigidity**；且「拟合→证书」**绝不可能** | 已判 ✓ |
| **P-3** | ⭐⭐⭐ **③-B 跨尺度缺陷系统（结构性二分 ＋ 临界指数来源全堵）** | `docs/P3-B-*`｜`docs/P3-B2-*` | **缺陷可利用来源只有两类，均被 rule 6 判死**：**(i)** 精确算术恒等式（整数性／乘法／Möbius 型，如 $\sum_{n\le X}\mu(n)\lfloor X/n\rfloor=1$）⟹ $\Delta\equiv0$ ⟹ 无选择（**S2 FALSE**）；**(ii)** 把 $\Delta$ 定义为误差型 ⟹ 三分性**由定义塞入**（$X^{1/2}$ 手写）⟹ **S1 FALSE**。**③-B-2 搬运到 $\zeta$**：构造 $\mathcal O_X=\int_1^X\frac{\psi(t)-t}{t^2}dt$（良定义、算术生成、逼近率 $\asymp X^{\beta_{\max}-1}$ 确实读出 $\beta_{\max}$），但三条同时失败（无盲性／阈值靠插入／指数来源已封闭）⟹ **②FALSE**。⭐ **统一的负面洞察**：临界指数 $\tfrac12$ 的算术来源**恰好是那些已知／已封闭的来源**（归一化＝插入；函数方程＝completion 同墙 E4-1 S1；显式公式＝已知判据）⟹ **新规格：$1/2$ 必须作为自洽方程／流的临界指数动态导出 ⟹ 精确指向 P2**（算术流＋被强制的不动点＋临界指数 $=\beta_{\max}-\tfrac12$ 且不靠显式公式） | 已判 ✓ |
| **C-24** | ⭐⭐⭐ **GM 大值定理 ＋ 改进窗口的独立推导（（i）无条件聚合的地基）** | `docs/PI-1-*`｜`external_refs/guth_maynard_2405.20552.txt` | **GM Thm 1.1（逐字）**：$\sum_{N}^{2N}b_nn^{it_r}$ 在 $R$ 个 $1$-分离点上 $\ge V$ ⟹ $R\le T^{o(1)}(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4})$；经典对照 (1.1) $R\le T^{o(1)}(N^2V^{-2}+T\min(NV^{-2},N^4V^{-6}))$。**⭐ 本档推导**：GM 两项新贡献的交叉点为 $V=N^{4/5}$（无 $T$ 项）与 $V=N^{7/10}$（含 $T$ 项）⟹ **改进窗口恰为 $N^{7/10}\lesssim V\lesssim N^{8/10}$**（与 GM 自述逐字吻合；交点上两端项均为 $TN^{-2/5}$／$N^{2/5}$）。**靶子**：无条件求值 $\mathrm{tr}\tilde G^3$ 于 $X\asymp T$（＝把 form factor 支撑从 1 推到 >1），缺口 $T^{1/3}$。**精确待查**：$\mathrm{tr}\tilde G^3@X\asymp T$ 的 $(N,V)$ 是否落在 GM 窗口内 | 已入仓 ✓ |
| **C-25** | ⭐⭐⭐⭐ **前沿一手原文：$\tfrac23$ 天花板 ＝ 我们的 $0.682$ ＝「support$>1$」同一堵墙** | `docs/PI-2-*`｜`external_refs/zeta23_2608.13637.*` | 载入前沿原文（Alpöge–Furman，arXiv:2608.13637，21 页）。**§7.2(a) 逐字**：绑定性约束 $L\asymp\log T$（等价 $X\le T$）来自 **Proposition 5.4**；$X\gg T$ 时离对角素数和不再被对角支配，其求值需要 **prime pairs**（Hardy–Littlewood，或等价地 **Montgomery 配对相关 support$>1$**）。**§7.2(e) 逐字**：对角法（$k$ 个素幂乘法关系＋Montgomery–Vaughan）**恰在 RS 范围 $X^k\le T^{2-\varepsilon}$** 可用；$X\asymp T$ 时只允许 $k=1$。**§5 引擎**：Lemma 2.2 MV 双线性型，$\lambda_r=\log n$（$n\le X$ 素幂），$\delta_n^{-1}\le2n$ ⟹ 只用 $\ell^2$ 权、**不含配对相关内容**（与 V300 一致）。**⟹ 判定**：$T^{1/3}$ 缺口所需＝**配对相关 support$>1$**，与 GM 的（单多项式大值频率，窗口 $N^{7/10}\lesssim V\lesssim N^{8/10}$）**对象型不同** ⟹「搬运 GM」不成立；且前沿 **自用词「bandwidth-one ceiling of §7.2」＋ 0.682**（L71／L1608／L1651）⟹ **前沿 $\tfrac23$ 天花板 ＝ 我们的 0.682 ＝ 同一个「support$>1$」墙**（与 V162／V181 FSC／MV support 墙、V316 $\lambda\le1$ 同址） | 一手确认 ✓ |
| **C-26** | ⭐⭐⭐⭐ **SUPPORT-1 WALL IDENTIFICATION（合并封存）** | `docs/SUPPORT-1-WALL-IDENTIFICATION-closure.md` | **(i) 正式封存，标题＝SUPPORT-1 WALL IDENTIFICATION**（不是「GM 路线 DEAD」）。**核心对应（一手文本支撑）**：$\text{support}>1\iff$ prime-pair／pair-correlation information；$\lambda\le1\equiv X\le T\equiv$ bandwidth-one ceiling $\equiv$ 我方 $0.682$ ceiling。**三条记录**：①位置 $X\le T$／support$\le1$；②越墙所需＝prime pairs／Montgomery 配对相关 support$>1$；③现有引擎**类型不匹配**（GM 的 single-polynomial large-value information 不能直接提供）。**措辞收紧**：不写「等价于某猜想」，改写「所需**信息强度至少进入** HL／Montgomery 配对相关型信息层级」。**战略**：不再把 support$>1$ 当待优化技术参数 ⟹ 定位为「需要**新的 prime-pair arithmetic input**」。**合并登记**：$0.682$／$2/3$／$\lambda\le1$／$X\le T$／FSC-MV support 墙（V162／V181）／V316 ⟹ **今后不再分别开案**。**（丙）外部墙定义**＝prime-pair correlation beyond support 1；要问的是「有没有新算术机制，不直接证明 pair correlation，却能提供 support$>1$ 所需的那一小块结构？」；与 P2 交叉：尺度流／固定点 $\leftrightarrow$ 跨尺度 prime-pair correlation | 已封存 ✓ |
| **C-27** | 📒 **墙体与难题台账（逐项讨论用·独立存档）** | `docs/WALLS-DIFFICULTIES-LEDGER.md`｜`docs/AUDIT-WALLS-AND-DIFFICULTIES-20260917.md` | **总账**：墙体 **W1–W12**（独立承重**仅两根**：**W1** $\beta$-盲性／检测$\ne$排除；**W6** SUPPORT-1 WALL ＝ support$>1$）；难题 **D1–D10**（0 项独立承重，全部归并 W1/W6 或已撤回）；已关闭机制类 34 关键词；G 箱 13 条（G8–G20）；活路 L1 已封／L2／L3＋项目级唯一靶 1 条。每项格式＝**定义／证据等级／位置／状态／待议点**。要点：W3–W5 三面一墙；W6＝W12；W11 已封（虚 Airy 硬反例）；W9 已撤回；**D1 相位均匀性＝不是统一墙**（Burnol 逐字三次出现，但 CONV2 局部撤回／CONV3 进一步撤回）；**D2 灾难消解**方法层（E160 消解式模式）与今日 Audit$\ne$Discovery 同一条；**D3 振荡项消解**部分完成（M(T) 线撞 Lindelöf；PAPERA 端点障碍未全线闭合）；**D4 相位感知聚合缺口与 W6 同址**。议程建议：第 1 轮 W6→D4→W1｜第 2 轮 D1｜第 3 轮 D3＋D2 方法层｜第 4 轮结构关系复核 | 已存档 ✓ |
| **C-28** | 🎯 **行动起点表：W1–W12／D1–D10 五列** | `docs/ACTION-START-TABLE-W-D.md` | 唐先生 12:19 指定「此表＝后续行动起点」。**五列**：难点／突破点／目前进展／文献最新进度位置／技术手段局限；证据等级 `[原]`/`[档]`/`[未核]`。**要点**：**W6** 唯一活口＝**对偶正性 majorant**（五项武器三项已判 C）；**W1** 勘误（"$\beta$ 盲"→"线性通道饱和＋提取需无界精度"）；**W2** "三面一墙"已降级为待核；**W5/W10** 共用正性工具族；**D3** 化为点态 $|\Delta(N,\sqrt N)|=o(\sqrt N)$ 而 RH 差 $\log^2$；**D4 与 W6 同址**；**D10** 算术无内生动力学（D1=0）。标 `[未核]` 的文献位 4 处（W3/W4/W7/W10） | 已建 ✓ |
| **C-29** | ⚔️ **W6-MAJORANT-1 弧线（卡点定位 ＋ 乘子计算 ＋ 对称化带限）** | `docs/W6-MAJORANT-1-*`｜`W6-MAJORANT-1b-*`｜`W6-MAJORANT-1c-*` | **1a**：Prop 5.4 原式逐字 ＋ **卡点精确定位＝Montgomery–Vaughan（Lemma 2.2）步**（四个 $\sum_{n\ne m}x_nz_m/(y_n-y_m)$ 型双线性形式）；天花板算术 $D\asymp\frac T\pi\frac{L^3}6$、$|O_1|\ll L^2X$ ⟹ 对角支配 $\iff X\ll TL$ ⟹ $X\lesssim T\log T$；推到 $X\gg T$ 须改进因子 $\asymp X/(TL^3)$。**1b**：$K_T$ 相位记账 ⟹ 四项 $p\in[T,2T]$、$-q\in[T,2T]$，乘子＝四个 $\Phi^2$ 抹平的**平移 sign**，平移 $\Omega\in[T,2T]$。**1c** ⭐：$\alpha_n^-=\overline{\alpha_n^+}$ ＋ 对称化 ⟹ $K^{\rm sym}=\frac{\sin(3Tt/2)}{t}[\cdots]$ ⟹ **(a) 奇点被消**（$t\to0$ 括号 $\to0$）；**(b) 严格带限** $[-3T/2,3T/2]$；**(c) 带外＝精确 0** ⟹ **裸 Hilbert 障碍在 $K_T$ 上不成立**；⚠️ 修正：$M_T$ 是**带限卷积×对角权**（二变量符号），**不得**当单变量乘子；初步读数比值 $\asymp X/T=T^\eta$ **恰合所需量级**，但 $\alpha$ 权携 $L$ 因子、$\ell^2$ 归一化**未复核** ⟹ **FALSE 理由已移除；局部 ALIVE 候选（待归一化复核）** | 进行中 ✓ |
| **C-30** | ⚔️ **W6-majorant 路线封存（cross-$X>T$ FAIL）＋ J3 唯一残留闸门** | `docs/W6-MAJORANT-1g-*` | **勘误**：1f 的「光滑 $\phi$ ⟹ core 主导」**作废**（$f=c^2\phi^4$ 本身完整，$\eta$ 承担 core 边界过渡，$\widehat\eta$ **非**独立小尾项；反例 $f\in C_c^\infty$ 且 $f=c^2$ on core ⟹ $|\hat f(y)|\ll_N|y|^{-N}$）。⭐⭐ **抵消由连续性强迫**：core 的 $1/y$ 尾部来自 $x=\pm\ell$ 的**人为内边界**，真实 $f$ 无边界 ⟹ $\eta$ 必须提供恰好相反贡献 ⟹ 非「可能抵消」而是**强迫抵消** ⟹ **(c) 不是唯一反例方向**。硬公式 $\hat f=\frac1{(iy)^N}\int f^{(N)}$ ⟹ 决定 J1 的是 **transition layer 正则性**。**但** $\frac{|O_1|}{D}\sim\frac{T^\eta}{(\log T)^{N-O(1)}}$，固定 $N$ 时 $T^\eta\gg(\log T)^N$ ⟹ **任何有限阶 smoothness 都不能破 $X>T$ 幂次障碍**。**J1 → J3**：§5.2 是否给出 $|\widehat{\phi^4}(y)|\le C_N|y|^{-N}$？（若论文未给导数／transition 正则性 ⟹ **真正缺失输入**）。**判定**：**W6-majorant-1 的 cross-$X>T$ 路线正式 FAIL**（**不是** W6 整体 FALSE：SUPPORT-1 墙本身不动）。唯一残留闸门＝**是否存在由 $\Phi$ 自身产生的 $T^{-\eta}$ 级离散谱压制** | 已封存 ✓ |
| **C-31** | ⚫ **W5-DEAD（正式关闭）＋ W4-1a（C）＋ 三墙同一缺口** | `docs/W5-DEAD-closure-and-fourth-class-tightening.md` ｜ `docs/W4-1-charter-discrete-filtering-with-selective-attenuation.md` ｜ `docs/W4-1a-filter-response-ratio-C-and-convergence-to-W1B.md` | **W5-DEAD**：唯一像第四类的候选＝非线性主子式 $\Delta_k=\det(G_{ij})$；一行审计 $\{\Delta_k\ge0\}\iff G\succeq0\iff n_-=0\iff$ Weil 正性 $\iff$ RH（撞 `V187` inertia 墙）；$\det G=-ab<0$ 只给 $n_-\ge1$，**不给** $b\ll\varepsilon_T$ ⟹ 回 W3／W6；高阶与 Fredholm determinant 同样落 inertia／Deninger 墙；**第四类收紧定义 (A)--(E)**，尤其 **(D) 独立算术上界**（无 (D) 即 POS 重写）。**W4-1a**：$y$-卷积型滤波因**平移不变性**一律无效（$\mathcal R\to1$）；支撑须 $\Delta y\gtrsim1/(\beta-\tfrac12)$；判别力 $\mathcal R\lesssim X^{\beta-1/2}$ **幂次级**；但**比值 ≠ 选择**（大比值可来自模态自身增长）⟹ 须**同一量的独立算术上界** ⟹ 与 (D) 同一缺口；⭐ **W4 与 W1-战术B 收敛**。**三墙（W4／W5／W6）独立收敛到同一缺口** | 已登记 ✓ |
| **C-32** | ⚫ **W4 限定 DEAD（全部线性滤波受同一上界）＋ 三墙汇合** | `docs/W4-1b-all-linear-filters-bounded-scoped-DEAD.md` | **核心结构**：$m_\beta(n)=w(n)m_0(n)$，$w=n^{\beta-1/2}>0$ 光滑乘性（离轴模态＝在线模态×光滑正权）⟹ 任意线性泛函 $\mathcal R\lesssim e^{(\beta-1/2)\Delta y}\le X^{\beta-1/2}$ ⟹ **$y$-卷积限制不需要**；四保留类（$y$-非平稳／网格耦合／整数差分／乘性卷积）**逐项落入同界** ⟹ 保留口闭合；非线性滤波判据**退化**（比值≠选择）⟹ 需 (D)。**判定：W4 = DEAD（限定）**。**三墙汇合**：W6（缺独立幅度控制）／W5（缺 (D)）／W4（缺同一上界）⟹ 与 **W1-战术B 同形** ⟹ 对台账「三面一墙」栏＝**结构性经验支持**（非定理） | 已登记 ✓ |
| **C-33** | ⭐ **W4-1d：第二尺度层存在且频率可分** | `docs/W4-1d-second-scale-layer-exists-frequency-separable.md` | $\delta_T(s)=-\sum_\rho\frac{T^{\rho-s}}{\rho(\rho-s)}+\ldots$ ⟹ 每项 $=T^{\beta-1/2}e^{i(\gamma-t)u}$（$u=\log T$）⟹ **u-频率＝$\gamma-t$（零点位置）｜u-增长率＝$\beta-1/2$（零点偏移）**。实测（256 点 log-uniform，$T\in[10^5,2\times10^8]$，$s=1/2$）：谱上**两层分开** —— $\nu=0$ 背景层 $A=1.688$、$\nu=0.823$ 趋势层 $0.854$，以及 $\nu=\gamma$ 处的**零点峰层**（最好匹配 $\nu=32.936$ vs $\gamma=32.935$，$\Delta=0.001$；另 $30.466/30.425$、$94.692/94.651$、$60.932/60.832$）；**动态范围 30–80×** ⟹ **频率可分**（标量 $|\delta_T|$ 里两层混在一起，故只能一步滤波）。＝**Guinand 相位锁定（A-1）的谱形式** ⟹ 修正 W4-1c「限一步」：可改用**频带选择滤波** ⟹ 可累积（但只恢复可分性，非 β 判据）。下一步＝每 $\gamma$ 峰增长率测量（每零点 β 探针） | 已建 ✓ |
| **C-34** | 🎯 **缺口直攻弧线：GAP 规范形式 → GAP-② 数值判定 → $C_0$ 精确陈述与紧性 → $\Lambda_1$ 攻证伪** | `docs/GAP-direct-attack-canonical-form-and-A2-handle.md` ｜ `docs/GAP-2-numeric-verdict-II-is-log-level-not-power.md` ｜ `docs/GAP-C0-precise-statement-and-single-lemma.md` ｜ `docs/GAP-Lambda1-impossibility-attack-reduces-to-Dprime-and-Dprime-is-false.md` | **① GAP 规范形式**：六项归约（W6／W5／W4／W1-B／W3／W8）全部落到 $\mathfrak G$；抓手＝A-2 的 $M_T(s)$（纯算术有限和）。**② 数值判定**：$|\delta_T|\asymp(\log T)^{1.00}$（log 级，**非**幂次级）；分辨率地板 $\beta-\tfrac12\gtrsim0.15$；⟹ $\mathfrak G$＝重述（③）。**③ $C_0$ 精确陈述**（三条件）＋ $C_0\iff C_0^*$（`V276`）＋两侧唯一引理 $\Lambda_1$／$\Lambda_2$；**P3 四类退化查覆盖**⟹ 未被覆盖但归约到**锚定困境**（`V289`）⟹ $\boxed{C_0\ \textbf{是紧的}}$（无独立子问题）⟹ 攻缺口与攻两侧墙在此点重合。**④ $\Lambda_1$ 攻证伪**：不可能性＝**条件定理**（条件 (D′)）；**(D′) 作为全称陈述为假**（Mertens 定理反例）⟹ $\Lambda_1$ **仍 OPEN**，「实质封闭」**仍 informal**；捎带回答 `V322`：五个闭合依赖的「可有限呈现」前提**在全称形式上不成立** ⟹ 五闭合＝**条件结论** | 已建 ✓ |
| **C-35** | 🆕 **换手段弧线：rank–trace／惯性＋D-GRAM-1/2 ⟹ 新墙 GRAM-INDEFINITENESS** | `docs/NEW-MEANS-ranktrace-inertia-method-and-V187-correction.md` ｜ `docs/D-GRAM-1-audit-Z-and-integer-energy-are-incompatible.md` ｜ `docs/PARITY-BREAKER-five-conditions-incompatible-Re-s-blindness.md` ｜ `docs/D-GRAM-2-complex-s-Gram-FE-reflection-is-a-positive-multiplier.md` | **① 引入前沿工具**（非我们审计逻辑）：**(Z)** 分块＋**(P)** $\|\tilde G\|^2_{HS}$＋**(L)** rank–trace 不等式 $r\ge 2\mathrm{tr}P+4\mathrm{tr}Q-4b-\|P+Q\|^2_{HS}$；逐字「**the inertia bound replaces the positivity**」。**② 纠 `V187`**：inertia／rank 型有**两种用法** —— (i) $n_-=0\Rightarrow\mathrm{RH}$（循环，`V187` 只看这种）｜(ii) **rank–trace ⇒ 无条件计数界**（非循环）⟹ `V187` 的「形式存在、实质封闭」**对该实例为假** ⟹ **六类类表不完备**。**③ 方法天花板＝100%**（逐字），卡点在**输入**。**④ D-GRAM-1**：(c) 可有**整数乘法能量**实现（$E_F=\sum_{m,n}F(\log\frac nm)$，连续主项 $N^2\!\int\frac{F(u)}{1+e^{-|u|}}du$）✓✓；但带 (Z) 的 HS 回 Montgomery 素侧 ⟹ **C（工具失效）**。**⑤ PARITY-BREAKER**：五项互斥；parity barrier 真内容＝$\Re s$-盲性 ⟹ 归约 $W3$；**导出** SUPPORT-1 的 $X\le T$ 为唯一相容点。**⑥ D-GRAM-2**：复-$s$ Gram (I) $\Re s$-敏感 ✓、(III) **HS＝整数能量 ✓✓**（$\tilde G_{mn}=n^{-1}H(\log\frac mn)$）；**(V) (1,1) ✗✗** —— 关键恒等式 $J_x\phi_n=n^{2x}\phi_n$（$n^{2x}>0$，**正乘子／基对称**，非符号）⟹ 仍 PSD ⟹ **(A)⊥(B) 被加强（适用范围扩到一切正测度 Gram）** ⟹ 新墙正名 $\boxed{\textbf{GRAM-INDEFINITENESS}}$（$(1,1)$ 是 Weil 型／显式公式性质，**不是 Gram 性质**） | 已建 ✓ |
| **C-36** | 🆕 **天花板 0.6818287 的重算：对偶退化 ＋ 目标身份 ＋ 无界性定理** | `docs/CEILING-LP-RECOMPUTE-results.md` ｜ `lean-frontier-audit/lp/ceiling_lp_recompute.py` ｜ `lp/ceiling_lp_recompute_out.json` ｜ `lp/lp_run_log.txt` | 依唐先生 09-17 15:11 指派；**判词＝未能求解**（不推翻／不确认）。**① 目标身份**：$0.6818287$ ＝ `LawN256.lean` 文件头逐字记录的 $p_0=1-a_N=10909258999421303588095230195816054408197/16\times10^{39}=0.681828687463832$（舍入上取，余量 $1.254\times10^{-8}$；$0.6818287-\tfrac23=0.0151620<0.016$ ✓）⟹ **目标是显示性输入，不是 Lean 输出**。**② 数据侧**：行条件实测 $1.836710\times10^{-40}(=1/2^{132})\le3\times10^{-40}$ ✓；盒最坏 $D(1)=0.82395316071284$ vs $d_1=0.82395317$ ✓。**③ 无界性定理**：任务所给 LP 规格在 $r\equiv-\lambda$ 方向**无界**，增量恰 $=d_1|r(1)|$ ⟹ band-limited（$r(\pm1)=0$）**由 LP 自身强迫**（与前沿散文逐字一致）。**④ 对偶侧**：盒松弛 $\delta_{\rm box}=2.085368\times10^{-5}(B=8.2)$、$=2.5431315\times10^{-6}=1/(6N^2)(B=1)$，**与 $M$ 无关**（$M=20/50/100$ 同值）⟹ 对偶值 $\equiv p_{\min}+\delta_{\rm box}$，**证书侧只是重述**。**⑤ Parseval 刚性**：整数位置律被锁死（$p=0.6760$／$1.4980$）⟹ 最优律必为非整数有理位置 ⟹ **marks 几何不在 Lean／本地**。**⑥ 与 E45 张力**：E45 细网格已有 $p\approx0.0231$ 的精确斜坡律 ⟹ 前沿有限程序**必含额外结构**（只在外部 JSON，sha256 `cc3de991…4eb8`）。**⑦ 勘误 1**：首版 $W$ 用 `quad` 致 $\sum W_i=0.50993\ne\tfrac12$ ⟹ 伪造出 $M$ 依赖 $\delta_{\rm box}$（up to 1.336）✗；改闭式权重后 $\sum W_i=0.5$ ✓。**未用 RH；未取 JSON；不声称前沿有错** | 已建 ✓ |
| **C-37** | 🗂️ **22 项逐项审核台账（审核／验证／攻击）** | `docs/REVIEW-LEDGER-22-items-tracker.md`｜源档 `docs/WD-FOURWAY-BREAKDOWN-all-22-items.md` | 依唐先生 16:26 立。**三阶段协议**：审核（核对原文／标出 `[未核]`）／验证（可复算证据）／攻击（A通过·B修正·C推翻·D未决）。**禁令**：攻击失败≠定理；未找到反例≠不存在（`N1/N2`）。**22 行台账**：W1–W12／D1–D10，逐项列「待审点／验证手段／攻击方向／状态」；状态全 ⬜。**优先序**：第 0 轮 4 处 `[未核]` 文献位（W3/W4/W7/W10）→ 第 1 轮承重 W1/W6 → 第 2 轮 D4/D3 → 第 3 轮其余。**工具注意**：闸门关键词须具体（≥3 字且含专名／编号） | 已建 ✓ |

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

$$\textbf{突破级判据}：\text{(a) 解决／实质推进一个公开猜想（LH／RH／GRH／哥德巴赫／孪生／其它素数猜想）；}\ \text{(b) 或给出其它物理／数学模型的}\textbf{新定理}✓$$
$$\textbf{过程性判据}：\text{封闭某条路线／给出负面判据／记录一个技术事实／建立方法论工具}✓$$

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

$$\textbf{当前无}\ \textbf{突破级} \text{条目}✓\quad\Longrightarrow\ \text{全部按}\ \textbf{自用资产} \text{登记；}\ \text{突破级出现时}\ \textbf{另行走发表流程}✓✓$$

$$\textbf{唯一"发表轨预备候选"}：\ \boxed{\text{C-1＋C-2＋C-3 合并为"关于 BC (Adv. Math. 328) }\S4.1.3\text{ 的幂次账与技术注记"}}✓$$
$$\qquad\text{定位：}\ \textbf{技术注记／评论}，\ \text{非猜想级突破} \Longrightarrow\ \text{按唐先生标准仍属}\ \textbf{过程性}✓\quad(\text{登记即可，不必发})✓$$


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

---

## 🔒 **CLOSED_scoped** · BC Internal 线（2026-09-17 冻结，唐先生裁定）

$$\boxed{\text{BC Internal}\ =\ \text{T1／T2／T3}\ +\ (\text{甲})\text{-1}\ +\ (\text{甲})\text{-2}\ =\ \mathrm{CLOSED}_{\rm scoped}}✓✓$$

### 结论（**严格限定作用域**）
$$\text{在既定 BC／BCR 应用架构内，}\ \textbf{固定幂级出口未找到}✓$$

### ⭐ **R1／R2 同因 FAIL**（本 closure 的核心，比普通 NO-GO 更干净）
$$A\ \lesssim\ N^{1/17}\quad\text{同时导致}\quad A\not\gg N^{4/5}\quad\text{与}\quad g\ \lesssim\ AN\ \le\ N^{18/17}\ \ll\ N^{9/5}✓$$
$$\Longrightarrow\ \text{这不是"某个估计不够强"，而是}\ \boxed{\text{唯一潜在 conductor-rescue 层在实际应用参数区间中}\ \textbf{根本不存在}}✓✓$$
$$\qquad(\text{不是"某候选被排除"，而是}\ \text{BC 这条线从多个独立入口}\ \textbf{压缩到一个清晰的 scoped closure})✓$$

### 🚫 四条**明确不声称**（绑定本 closure，不得解绑）
$$\text{(1)}\ \textbf{不声称} \text{BC 普适不可改进}✓$$
$$\text{(2)}\ \textbf{不声称}\ 17/33\ \text{是普适硬墙}✓$$
$$\text{(3)}\ \textbf{不声称} \text{所有可能的 C--S 重组已经数学上穷尽}✓$$
$$\text{(4)}\ \text{结论}\ \textbf{仅针对} \text{当前 BC／BCR 参数与已审计的 transformation families}✓$$

### 📌 （丙）**入场判据**（下次进入时先过此关）
$$\boxed{\text{新外部结构必须改变}\ \ \underbrace{\text{conductor 形成机制}}_{\text{BC 已封闭}}\ \ \text{或}\ \ \underbrace{\text{finite-scale}\to\text{global-scale 的桥接机制}}_{\text{RH 真正缺口}}}✓✓$$
$$\qquad\text{否则}\ \text{容易只是换一个名字重新回到 Weil／C--S／conductor 这条}\ \textbf{已关闭的轨道}✓$$

### 状态
$$\boxed{\text{停在此处（2026-09-17）}\ ——\ \text{不以"再找一个能给}\ N^{-\delta}\ \text{的估计"作为（丙）的起点}}✓$$

| C-38 | **严格化重做：反证链 $D=0\Rightarrow$RH（首版论文期）** | `docs/RIGORIZATION-candidate-proof-v1-D0-implies-RH.md`（2026-09-17）| 提取 `candidate-proof-v1.md`（2026-08-31，首版论文 `rh-discriminator-v28.tex` 同期）并逐引理严格化：**定理 A**（轨道正性，自推闭式 $P_\gamma(\delta)=\frac{2N}{(1+\gamma^2)^2W^2}$，$N\ge\delta^2(10\gamma^6+18\gamma^4+6\gamma^2-2)>0$）、**定理 B**（轨道分解＋绝对收敛，$P\asymp20\delta^2\gamma^{-6}$）、**定理 C**（$\sum_\rho[1-(\rho-\frac12)^2]^{-2}=C_1$ 无条件，Hadamard＋偏分式，$B=L(0)$ 相消，全部绝对收敛）、**定理 D/E**（$D=S_\gamma-C_1$ 且无条件 $S_\gamma\ge C_1$）、**定理 F**（判据：RH$\iff S_\gamma=C_1\iff D=0$）、**定理 H$_m$**（离轴轨道至多 $m$ 个 $\Rightarrow D=\sum_{j\le m}P_{\gamma_j}(\delta_j)$ 有限显式正项和；推论 H$_m'$ 定量检测下界 $\kappa(\delta_0,\Gamma)>0$）｜**唯一缺口**＝原引理 F，且 F$\iff$RH（严格双向）⟹ 原链为判据非证明，与 `A13-2b` 记"失败的尝试"一致且此处给出严格理由｜原档 4 漏洞处置：关闭 3、消解 1｜数值：$C_1=7.3772455e$-5、偏分式精确、前 300 零点 $2\sum=7.376929e$-5（差=尾部估计）、$P$ 渐近吻合｜不声称 RH；与 v2.8 判据同一；`E30-2` 视角属"机械×输入"型，与 W6/SUPPORT-1 同址 |
| C-39 | **E4（Palojärvi 推广）状态审计** | `docs/E4-STATUS-AUDIT-what-closed-means-and-the-two-remaining-gaps.md`（2026-09-17）| 对象 `E4-palojarvi-finitely-many.md`（"至多一个离轴 ⟹ 有限多个"）。**结论**：E4 的"已闭合"＝**常数级闭合＋骨架**（本档独立重跑 `E4b_palojarvi_constant.py` exit 0：$m=1$ 退化精确、全窗最差 log-ratio $+32.1289$、$m$ 代价对数级、12 承重 ⟹ `E4 gap CLOSED`），**非**自足严格。**两块真实剩余**：①引擎 Lemma 2.2（Montgomery *Ten Lectures* Ch.5 Thm 11）**证明未读**——本档数值检验其陈述很安全（$M\le12$ 最坏 $\max_{n\le5M}\mathrm{Re}\sum z_j^n\ge0.5\gg1/20$；$M=1$ 解析 $0.5$），但引用状态未变；②假设 $m$（$\Re\rho>\tau/2$ 的零点数）**无法供给**（Dirichlet $L$ 函数：$m=1$ 经典可得；一般 $F$ 无显式界）⟹ **条件性检测定理，对 RH 无杠杆**。另**措辞级精确化**：$R^n\ge40(K_{K,1}+K_{F,4})n\log n+20m$ 与 $R^n\ge n\log n\,C(m)$ **非严格等价**（差 $20m(n\log n-1)\ge0$），后者更强、蕴含前者（原档同句已注明 $n\log n\ge1$，无数学错误）。与 `C-38` 对照：**前者循环、后者条件**，均非 RH 证明 |
| C-40 | **E4-引擎-1：引理 2.2 自足化尝试（四条路线＋确切堵点）** | `docs/E4-ENGINE-1-selfcontainment-attempt-four-routes-and-precise-jam.md`（2026-09-17）| 目标：把 E4 的引擎（Palojärvi Lemma 2.2 ← Montgomery *Ten Lectures* Ch.5 Thm 11：$\max_{n\le5M}\mathrm{Re}\sum_j z_j^n\ge\frac1{20}$）自足化。**数值判定**：引理成立且引用常数**极宽松**——结构化族（等分根／6 次根／反相）峰值恒为 $M$（无对消），爬山最坏值 $M=1{:}0.500\to M=10{:}2.236$（随 $M$ 增长），$M=1$ 解析 $0.5$ ⟹ 余量 $\ge10$ 倍。**四条路线及堵点**：①Fejér 全局加权（每项下界 $-\frac12$ 与 $M$ 成正比 ⟹ 空不等式）；②实部二阶矩（非对角损失 $M^2$ 吞掉对角收益 $NM$ ⟹ $N=5M$ 时下界变负）；③模二矩**成功**（全模 1 情形 $\max_{n\le5M}\|\sum_j z_j^n\|\ge\sqrt{0.8M}$，**严格可证的新引理**）但模 $\ne$ 实部（旋转可改 Re 不改模）⟹ 不传导；④单项相位鸽笼（$m=1$ ✓，$m\ge2$ 时其余项可抵消 ⟹ 正是引理内容）。**判定**：证明未获取 ⟹ E4 仍＝条件性检测定理＋引擎引用件。**三条下一步**：(1)取得 Montgomery Ch.5 证明；(2)**改判据方向**：检测量由 $\mathrm{Re}\lambda_F$ 换成模型量 ⟹ 路线③严格引理即可用（**本档最有希望接口**）；(3)维持现状存档 | |
| C-41 | **E4-引擎-2：初等覆盖引理 ⟹ 定理 4.1（m=1）自足重证＋常数↓10倍** | `docs/E4-ENGINE-2-elementary-covering-lemma-selfcontained-m1-and-better-constant.md`（2026-09-17）| 产出**初等覆盖引理 C**：$|z|=1\Rightarrow\max_{1\le k\le5}\mathrm{Re}z^k\ge\frac12$（证明＝五段区间并集无缝覆盖全圆周，逐段列出；常数 $\frac12$ 最优，$z=e^{i\pi/3}$ 取到，数值 $0.500009$）——**严格强于引用的 Montgomery Lemma 2.2（$\frac1{20}$）10 倍且完全自足**。由它给出 **Palojärvi Theorem 4.1（至多一个离轴零点）的自足重证**：(⟸) 方向常数不变（$|1-w^n|\le2$）；(⟹) 方向用引理 C 得新的更弱阈值 $R^n\ge4(K_{F,1}+K_{F,4})n\log n+2$，而源文为 $20n\log n+40(K_{F,1}+K_{F,4})n\log n$ ⟹ $(K_{F,1}+K_{F,4})$ 项**恰降 10 倍**并省去源文 $20n\log n$ 主项；窗口 $[N,5N]$ 与 $N\mid n$ 不变；$N_1$ 显式形式同步更新（$40(K_1+K_4)+20\to4(K_1+K_4)+2$）。$m\ge2$ 仍为条件性：模长可比时用路线③（Fejér 二阶矩，$\max_k\|\sum_j z_j^k\|^2\ge[\sum_j D_j-M(M-1)/2]/(5M/2)$，全模 1 给 $\sqrt{0.8M}$，混模(≥$1-\frac1{40M}$)给 $\sqrt{0.3M}$，数值均成立）；模长参差时仍需 Montgomery 实部版（缺口保留）| |
| C-42 | **E4-引擎-3：衰减松弛 —— 消除"模长可比"假设；残留＝Montgomery 实部引理（$r\ge2$）** | `docs/E4-ENGINE-3-decay-relaxation-removes-comparability-residual-is-Montgomery-RP.md`（2026-09-17）| 收口 C-41 §3 遗留项。**主结果**：C-41 提出的"模长可比"（$\sum_jD_j>M(M-1)/2$）**不是必要假设** —— 设 $K=\{j:|w_j|=R'\}$、$r=|K|$、$\rho=\max_{j\notin K}|w_j|/R'<1$，则 $|z_j|\le\rho^{N}$ 使非最大项**几何衰减** $\big|\sum_{j\notin K}\mathrm{Re}z_j^k\big|\le(m-r)\rho^{Nk}$；取 $Nk\ge\log(40(m-r))/\log(1/\rho)$ 即可压到 $\tfrac1{40}$ 以下 ⟹ 检测归约到等模长子集。代价：$N_m$ 追加第 4 项（$N_m\ge\lceil\log(40(m-r))/(5r\log(1/\rho))\rceil$），因 $R>1$ 时 $R^n$ 快于 $n\log n$ 故**不影响定理成立性**。**残留缺口精确化**：只剩"单位模 $r$ 个复数的**实部**下界"——$r=1$ 已自足（引理 C，$\tfrac12$）✓；$r\ge2$ 仍等价于 Montgomery Lemma 2.2 ✗。**数值**：最坏值 $M{=}1{:}0.500,2{:}0.503,3{:}0.817,\dots,10{:}2.236$（随 $M$ 增长，恒 $\ge\tfrac12$）⟹ 真值远宽于 $\tfrac1{20}$，**很可能存在初等证明给出 $\tfrac12$（对所有 $M$）**。**建议攻击形态**：推广覆盖论证（需证存在**同一** $k\le5M$ 使 $\sum_j\cos k\theta_j\ge\tfrac12$；工具：各 $\theta_j$ 覆盖集的**交**结构）；或改检测量为模量（需先证配对复和收敛）| |
| C-43 | **E4-引擎-4：覆盖论证推广 —— 三条工具＋数值证据＋开放状态** | `docs/E4-ENGINE-4-covering-generalization-tools-numerics-and-honest-open-status.md`（2026-09-17）| 目标 $(RP_M)$：$|z_j|=1\Rightarrow\exists k\le5M:\sum_j\mathrm{Re}z_j^k\ge\frac12$（若证成则 $r\ge2$ 也自足，E4 完全免引 Montgomery）。**数值判定**（退火 60k×8–20 重启）：$\min\max_{k\le5M}\sum_j\cos k\theta_j=0.506(2),0.769(3),0.839(4),0.987(5),1.041(6),1.399(8)$ ⟹ **无反例，$\frac12$ 看来普适饱和**；结构对抗族（等分根/无理 AP/反相）全 $\ge5.5$ ⟹ Montgomery 的 $\frac1{20}$ 比真值宽 10 倍以上。**极值配置**：$M=1$ ⇒ $60^\circ$（6 次根，恰饱和）；$M=2$ ⇒ $(60.06^\circ,90.02^\circ)$ 且 $k=1,4,5$ 上同时卡 $\approx0.5$（多重饱和）。**三条可证工具**：①Fejér 平均：$\max_k\sum_j\cos k\theta_j\ge[\sum_jF_K(\theta_j)-M]/(K-1)$（近栅格时有效）；②覆盖引理可缩放（$\forall\nu,\exists k\in[\nu,5\nu]$）；③鸽笼共点（某 $k^*\le5$ 被 $\ge M/5$ 个 $j$ 共享，但其余项可同时 $\approx-1$ ⟹ 只给负界）。**缺口定位**：缺"把 $\ge M/5$ 对齐项优势从其余项 $-1$ 中救出"这一步（$M=1$ 无其余项故闭合）。**⭐实用澄清**：$m\ge2$ 的缺口**只是自足性缺口、非数学缺口**——Montgomery Ch.5 Thm 11 是已发表定理，照引即正确；且 $\frac1{20}$ 已足够 ⟹ $(RP_M)$ 属"数学漂亮、工程非必需"目标 | |
| C-44 | **E4-引擎-5：二阶矩族对 $(RP_M)$ 可证不足（$M\gtrsim12$）＋极值结构解剖＋窗口放大线索** | `docs/E4-ENGINE-5-second-moment-family-provably-insufficient-for-large-M.md`（2026-09-17）| 继续攻 $(RP_M)$。**新严格结果**：①精确二阶矩恒等式 $\sum_{k\le K}f(k)^2=\frac12\sum_{j,l}[D_K(\theta_j-\theta_l)+D_K(\theta_j+\theta_l)]$（$f=\sum_j\cos k\theta_j$，$D_K=\sum_{k\le K}\cos k\varphi$）；②**方法级负面结果**：整个二阶矩族（Fejér 平均／RMS 路线／模二矩）受同一 $M^2\log K$ 损失支配，相容区间为 $\log(5M)\gtrsim2.5\Leftrightarrow M\gtrsim12$ ⟹ **$M\gtrsim12$ 时该族完全失去分辨力**，$(RP_M)$ 必须换机制（如利用 $\theta_j$ 的丢番图结构或非二次型正性）✗。**极值结构**：$M{=}1$ 极值 $60^\circ$（6 次根恰饱和）；$M{=}2$ 极值 $(60.06^\circ,90.02^\circ)$ 且 $k{=}1,4,5$ 同时卡 $0.5$、$k{=}6$ 处 $+1$ 与 $-1$ 对消 ⟹ 对手策略＝"**一项对齐、一项反相**"；$M{=}3,4,5$ 极值相邻差反复出现 $\approx2\pi/5$ ⟹ 与窗口因子 5 呼应。**窗口放大线索（实测）**：$\min_\theta\max_{k\le qM}$ 随 $q$ 上升（$M{=}2$：$q{=}5{:}0.512\to q{=}6{:}0.706\to q{=}8{:}0.999\to q{=}10{:}1.175$；$M{=}3,4,5$ 同趋势但非严格单调）⟹ 打破对手 5 阶错位 ✓，代价＝E4 的 $N$ 乘 $q$ 因子且 Montgomery 的 $5M$ 需改 $qM$ 重证；**证明仍缺**。**E4 状态不受影响**（$m\ge2$ 照引 Montgomery 即正确，$\frac1{20}$ 已足够） | |
| C-45 | **严格化：首版论文〔引理 3（离轴下界）〕** | `docs/RIGORIZATION-lemma3-offline-contribution-finite-off-axis.md`（2026-09-17）| 原档该引理只有 4 行梗概。本档补成完整证明：①配对化到 $\beta<\tfrac12$（$\beta>\tfrac12$ 贡献为正可弃；共轭对乘 2）；②单项界 $c_\rho\le\frac1{2\gamma^2}$、$e^x\ge1+x$ 型下界 $1-e^x\ge-xe^x$；③求和＋$n/(2\gamma^2)<1/T$ ⟹ $\Sigma_{\text{离轴}}\ge-nB_Te^{1/T}$（**显式常数**，原档仅 $O(1/T)$）；④绝对收敛性（按重数，$\sum\gamma^{-2}<\infty$）；⑤**有限/无限离轴统一处理**（原有档未区分）。**自查两处**：dps=25 时 $\beta{=}0,\gamma{=}10^{12}$ 误报 $c>1/(2\gamma^2)$＝**精度假象**（dps=80 排除，精确差 $2.5\times10^{-49}$）；撤回一条我算错的"端点比较"（把原档"余量"误当主项）| |
| C-46 | ⭐ **严格化：有限个离轴零点的反证法边界** | `docs/RIGORIZATION-finitely-many-off-axis-reductio-boundary.md`（2026-09-17）| 对象＝`contradiction-reductio-boundary.md`（9/07）＋候选 E（9/07）＋8/23 反证法。**补上原档缺失的关键一步**＝**引理 B（相位对齐）**：$\forall\varphi,N\ \exists k\le5:\cos(kN\varphi)\ge\tfrac12$（初等覆盖引理的尺度化版本）。**三个严格引理**：A（$c_\rho$ 双侧界 $\frac{\delta}{4\gamma^2}\le c_\rho\le\frac1{2\gamma^2}$）／B（对齐）／C（在线项上界 $0\le\sum(1-\cos n\theta_\gamma)\le2N(T)+n^2B_T$）。**定理 1**：单离轴 $\Rightarrow$ 存在 $n\le\frac{20\gamma^2\log(2(1+R_n))}{\delta}$ 使 $\lambda_n<0$。**推论 1**：与首版论文 $\lambda_n\ge0\,(n\le2T)$ 结合 ⟹ 离轴零点必 $\gamma\gtrsim\sqrt{\delta T/\log T}$；**⚠️诚实核对：该结论比已验证高度 $T$ 弱（$\sqrt T\ll T$）⟹ 被完全包含，无新排除**。**循环点精确定位**＝需 $\lambda_n\ge0$ 到 $n\sim2\gamma^2\log T/\delta$，超 $2T$ 部分即 RH。**原档"循环"判词成立**，本档给出其严格证明与精确位置。「无穷多离轴⟹排除」仅照录、**本档未复证** ⚠️ | |
| C-47 | ⭐ **严格化（合并本）：至多 $m$ 个离轴零点的检测定理 —— A1-3／E4 全线** | `docs/RIGORIZATION-EXTENSION-at-most-m-off-axis-zeros-consolidated.md`（2026-09-17）| 把 C-39～C-44 合并为**一份完整证明**。**定理 E4-$m$**：$F$ 至多 $m$ 个零点满足 $\|w_\rho\|>1$ ⟹ ①无例外 $\Rightarrow\|\mathrm{Re}\lambda_F\|\le(K_{F,1}+K_{F,4})n\log n\ \forall n$（**用模 $\|1-w^n\|\le2$，与源文同常数，不损**）；②有例外且 $\max\|w_j\|\ge R$ $\Rightarrow$ 存在 $n\in[N_m,5mN_m]$、$N_m\mid n$ 使 $\|\mathrm{Re}\lambda_F\|\ge$ 阈值。**证明结构**：分解 (37)＋检测不等式＋引擎＋$N_m$ 四项显式。**⭐引擎 $m'=1$ 完全自足**（引理 C：初等五段区间覆盖 $\Rightarrow\max_{k\le5}\mathrm{Re}z^k\ge\frac12$，常数最优，数值 $0.500009$）⟹ 阈值 $4(K_{F,1}+K_{F,4})n\log n+2$，**比源文 $20n\log n+40(K_1+K_4)n\log n$ 恰降 10 倍且不再引 Montgomery** ✓✓。$m'\ge2$：**主路线引 Montgomery Lemma 2.2**（正确性无缺口，阈值 $40(K_1+K_4)n\log n+20m$）＋两条自足路线（A 模＋可比性 Fejér 二阶矩；B **衰减松弛**消除可比性）**但归约终点仍是该引理**，且（C-44）二阶矩族在 $M\gtrsim12$ **可证不足** ⟹ 自足性为**开放加分项** ✗。**$N_m$ 四项**：$T_0/(e\tau)$／Lambert-$W$ 槽／$12\log C(m)/\log R$（**12 承重**）／$\log(40(m-r))/(5r\log(1/\rho))$（本档新增）。**§5 关键**："至多 $m$"起作用处＝检测项为**有限和**且 $C(m)$ **线性于 $m$**——若例外无限，$m$ 无界 ⟹ 无满足阈值的 $n$ ⟹ 定理不适用（$F_\sigma=\zeta(s)(1-q^{\sigma-s})$ 因**无限多**例外而非反例）。数值：$m=1$ 退化精确（相对差 0）、60 格点全过、最差 log-比 $+32.1289$、最小值在左端点 | |
| C-48 | ⭐ **任务1：经 E4 框架把反证法单向化 —— (H1) 自动、(H2) 不需要，天花板不动** | `docs/E4-ONESIDED-reductio-via-E4-framework-H1-automatic-H2-unneeded.md`（2026-09-17）| 回答唐先生任务 1（"符号朝向本来就对"的框架里能否单向化成 $\lambda_n<0$）。**结论：能 ✓✓** —— E4 框架的好部分**双向有界**（$\|G_n\|\le(K_{F,1}+K_{F,4})n\log n$ 是**上界** ✓），故 $\mathrm{Re}\lambda_F\le(K_1{+}K_4)n\log n+m'-cR^n<-\,$阈值 ⟹ **单向**：$\exists n:\mathrm{Re}\lambda_F(n,\tau)<-(K_1{+}K_4)n\log n\iff\exists$ 例外零点 ✓。⟹ **(H1) 自动成立**（不需另找上界 ✓）、**(H2) 完全不需要**（引擎施于**整个例外集**，与模长/速率分布无关 ✓）。**天花板未动 ✗**：阈值仍需 $n\gtrsim8\gamma^2\log T/\delta$，且 $R\to1^+$（边际例外）时 $N_m\propto\log C(m)/\log R\to\infty$ ⟹ 与 C-46"$n\sim2\gamma^2/\delta$"**同一堵墙**。**两框架差别精确定位**：(H1) 的"自动"仅在 E4 框架内（(T2.1)/(T2.3) 公理 ✓）；退回一般 $\zeta$（例外可能无限）则 $\|G_n\|$ 有界本身失效，(H2) 仍出现。**任务 3 附带**：C-47 §4.1/§4.2 朝向逐行复核**正确** ✓（无同类缺陷）；但 §4.3"自足路线 A"**过度陈述**（Fejér 二阶矩只给模、不传导实部）已被勘误 ✗ | |
| C-49 | ⚠️ **源文逐字对齐：Theorem 2.3 的真实引擎结构 ⟹ 我方"至多 $m$"框架**不是**源文结构** | `docs/SOURCE-ALIGNMENT-palojarvi-verbatim-thm2.1-2.3-and-my-at-most-m-framing-is-not-the-source-structure.md`（2026-09-17）| 从本地 PDF（26 页）逐字提取，6 项校正。**C1（结构性 ✗）**：Theorem 2.3 的引擎施于 $\{\rho:\|\Im\rho\|\le N\}$ 的**全部**零点（$M=N_F(N)$，由 (3) 界住；**有限性自动** ✓），**不是**"至多 $m$ 个离轴例外" ⟹ C-46/C-47 的"at most $m$"是**外加假设**、非源文结构 ✗（"至多一个⟹至多 $m$"属 **Theorem 4.1** 那条线，非 Thm 2.3）；**好消息**：去掉该假设后结论**更强**（任意满足 (3) 的构型均适用）✓✓。**C2**：常数记号是 $A_F,B_F,C_{F,j}(T_0),c_{F,j}(T_0)$；$K_{F,1}$ 是 Thm 2.1 的**结论常数**，$K_{F,4}$ 本次提取**未见** ✗。**C3**：$K_{F,1}(\tau)$ **显式**（$=\frac{2\tau}{3}(e+\frac1e)(A_F+\|A_F\log(8e\tau)+B_F\|)+\frac4{27}(1+\frac1{e^2})(\frac{c_{F,1}}{3\log2}+c_{F,1}\log(e^2\tau)+c_{F,2}+\frac{2c_{F,3}}{7e\tau})$）✓。**C4**：窗口 $[N,5N\cdot2(A_F\log N+M_F)]$、$N\mid n$（非 $[N,5mN_m]$）✗。**C5**：Lemma 2.2 引用**逐字一致** ✓（$\max_j\|z_j\|=1$、$5M$、$\frac1{20}$）。**C6**：$N\ge\lceil\max\{e,T_0,\frac{\tau}{\sqrt{R^2-1}},e^{(1-15M_F)/(15A_F)}\}\rceil$ 显式 ✓（$M_F=B_F+\frac{C_{F,1}}e+\frac{C_{F,2}}3+\frac{C_{F,3}}9$）。**待续**：Thm 4.1 的"at most one"确切作用／$\zeta$ 是否满足 (a)–(d) 及实例化常数／按源文机制**重写** C-46・C-47 ✗ | |