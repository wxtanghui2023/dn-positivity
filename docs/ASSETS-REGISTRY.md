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
| **D-11** | 🆕 **C-α 组合刚性纯计数下降环的反例障碍 ＋ 继承规则** | `docs/C-alpha-ledger-lock-and-novelty-audit.md`｜`docs/C-alpha-rigidity-MAP-CHECK-and-13-gate-screen.md`｜commit `d4ec772` | **MAP-NEW ⟹ GAP-HOLD ⟹ DEAD**（一轮文献级 novelty audit）✓ ① 组合刚性在本 RH 地图**零覆盖**（`Laman`／`pebble` 仅自命中）⟹ **MAP-NEW** ✓ ② `(3,6)`-稀疏在 3D **仅必要不充分**（标准反例 **double banana**）⟹ 「**失败保持下降**」**被结构性排除** ⟹ **`C3/C4` 缺口由「尚未找到证明」升级为「当前纯计数机制下存在明确反例障碍」** ✓✓ ③ 对称刚性（轨道刚性矩阵／Fowler–Guest 特征公式／gain-sparsity 计数）与曲面刚性（Laman 型**充要**定理）**均已发表** ⟹ 本仓无新不变量 ✓ ④ ⭐ **继承规则**：**不能只换对象；必须同时换出一个尚未被现有理论吸收的新不变量** ✓✓ ⑤ ⚠️ **DEAD 针对本仓 C-α 候选，非对 rigidity 领域的价值判断** ✓。**状态＝已封闭** ✓ |
| **D-12** | 🆕 **「两个表示交互」生成器封死（CROSS-0）** | `docs/CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md` | **CROSS-0 = DEAD**（**三重触发**）✓ ① **已有同物**：加性×乘性交叉不变量＝**Gauss／Jacobi／Ramanujan sum**（**Mathlib 已形式化** `gaussSum χ ψ`）＋ **mixed energy**（Glibichuk 2011／Mudgal：逐字 `low arithmetic interaction`）✓ ② **直接重写**：上述对象**本身即** Gauss sum／混合能 ✓ ④ **第三关系已存在且经典**：**Hasse–Davenport 乘法关系**（1935，Gauss 乘法公式的函数域类比）＋ lifting／norm／Stickelberger／`explicit multiplicative relations between Gauss sums`；**余者皆不等式型**（sum–product、Tao 加性界、乘性乘积界）⟹ 按阶梯「只有不等式、没有新结构 ⟹ DEAD」✓ ⚠️ 唐先生所引 2026 预印本出处＝**viXra（非同行评审）**，不作权威证据；但「A×M 不相容」framing 本不新（**sum–product 即经典**）⟹ 结论不依赖该源 ✓ ⟹ **生成器级封死**：不再以「换两种表示／换交叉量名称」续命 ✓。**状态＝已封闭**（依唐先生 21:16 预告条款，条件已满足 ✓）|
| **D-13** | 🆕 **Representation-Gap 生成器封死** | `docs/REPRESENTATION-GAP-MAP-CHECK.md` | **R0 实质 DEAD ＋ R1 不成立**（第三条件失败）✓ ① 缺口确有明文（van Handel 逐字："for other problems where log-concavity has been conjectured, such a representation is not available"）——**但同段即给解法**：「**most combinatorial problems cannot be reformulated in terms of mixed volumes，却可**直接证明 AF 型不等式**，log-concavity 由**同一机制**产生**」（点名 **Chan–Pak**）✓✓ ② 统一机器存在且活跃：**Lorentzian／completely-log-concave 多项式**（Brändén–Huh, Annals 2020）＋ **Hodge·Kähler package**（Adiprasito–Huh–Katz, Annals 2018）＋ 表示理论仍在扩张（covolume／dually Lorentzian）✓ ③ 文献含**反向猜想**（Amini：存在凸体使 matroid log-concavity **由 mixed volume 解释**）⟹ 学界视为**可填缺口** ✓ ④ 著名实例已解：**Read–Hoggar**（Huh 2009/2012）／Heron–Rota–Welsh／Mason 超对数凹／Stanley-CFG；剩余开放者（Welsh Tutte 对角／Amelunxen–Bürgisser）属**主流活跃猜想** ⟹ 不构成未覆盖接口 ✓ ⟹ **generator 封死**（依唐先生 21:23 ⑥ 条件成立）✓。**状态＝已封闭** |
| **D-14** | 🆕 **KH-4 position→eigenvalue 窄口径 GAP（三载体已封）** | `docs/KH-4-POSITION-TO-EIGENVALUE.md`｜`docs/KH-4-EXPONENT-TO-SPECTRUM.md` | **状态 ＝ 窄口径 GAP（唐先生 23:01 定稿）**；⛔ **非数学不存在性结论** ✓ 缺口终局：`divisor symmetry ⟹ forced optimal position x^{1/2} ⟹【GAP】⟹ canonical non-relabeling eigenvalue 1/2` ✓ **三种自然转换载体均封**：① **边界条件型**（边界可编码位置参数，但未形成「位置被迫成为谱值」的独立机制）｜② **尺度共轭型**（共轭保持谱不变，至多改坐标表示）｜③ **自洽参数型**（未得到独立非平凡闭合方程；已知关系均经 `ζ²` 零点 ⟹ 循环）✓ 另封：`(T_rf)(t)=r f(x/t) ⟹ Spec={±r}` ＝ **人工谱编码（把答案乘进算子）**，不计入 survivor ✓ **已证不缺者**：算子（canonical，唯一诱导 ✓）＋ 位置参数（`1/2` 由除数对称优化强制，且成位置族 `1/k`，`k=2` ⟹ `1/2`）✓ ⟹ **不能把组合切割指数升级为谱临界指数** ✓。**继承纪律**：不再攻第 4／第 5 种载体；下一候选须为「本身有独立数学问题且有自己的非平凡可变参数」的算术对象，RH 仅作后置接口 ✓ |
| **D-15** | 🆕 **`KH-5` 整线收口：残差归 `W6` 原子墙（不可再分）；`S2-NONLOCAL-C` 精确封口** | `docs/KH-5-R8-B-S2-NONLOCAL-C.md`｜`docs/KH-5-R8-B-S2-NONLOCAL.md`｜`docs/KH-5-R8-B-S2.md`｜`docs/KH-5-PRIME-CORRELATION-ADMISSION.md` | **判定链**：`KH-5` 候选＝既有 `R8` 素数对 carrier 线（裁决 `R8-B`，瓶颈 `S2`）⟹ 三类候选 `A/B/C`＝`V294-A` §3 既有候选集 ⟹ **A 零点侧 `CLOSED`｜B 算术相关性 `SATURATED`（`arXiv:2306.04799`；§7.2(e)）｜C 非局部正性 `CLOSED（终点退化）`** ✓ ⭐ **`C1`**：`2/3` ＝ 既有**显式交换率** `N_0^s/N >= 2 - R(psi)` 在 **`R = 4/3`** 处取值（`window` 值 `0.6725` ⟹ `R ~ 1.3275`）✓；机制＝`indefinite form -> inertia -> rank -> counting`（不要求 `Q >= 0`）✓ ⭐ **`C2`**：`1/3` ＝ **`R(psi) - 1` 单一结构化项**；**`V186` §3 终点退化定理**：`n_-(Q_T)` 恰数离轴对 ⟹ `100% <=> n_- = 0` 对全族 ⟹ 半正定 ⟹ **Weil 正性 <=> RH** ⟹ 「inertia 路线不是 Weil 正性的替代，在消灭离轴零点这一步**退回正性**」◊ ⟹ 依令 ④（`1/3` 不可避免 sharp ⟹ 精确封口）**C 路线精确封口** ✓ ⭐ **残差归属**：`100%` 需 **support `> 1`** 输入 ⟹ ＝既有 **`W6` 原子墙**（三阶矩 ≡ prime-pair ≡ support>1，**不可再分**）⟹ **不得重开 `support>1`** ✓✓ **保留收获**：① 机制（新，入工具箱）② **转移原理**（二阶矩＋惯性 ⟹ 计数下界；`V182` 对偶面，入工具箱）✓。**状态＝已封闭（A 出口）**；⟹ ⭐ **依 `E-13` 五出口框架重标：A 出口封口；`E-11`／`E-12` 依 B/C/D/E 出口保留为候选工具，不作 DEAD** ✓ |
| **D-16** | 🆕 **搜索空间级负结果：在当前机制／反例模型／`N0′` 覆盖范围内，尚未发现新的 arithmetic distinction** | `docs/FCG-0-adversarial-models-and-failure-signatures.md`｜`docs/SEARCH-FIREWALL.md`｜`docs/GT-0-and-GT-STRATEGY-audit.md` | ⭐ **结构**：$$	ext{failure} 	o 	ext{adversarial models} 	o 	ext{separation requirement} 	o N0' 	o 	ext{no new dimension}$$ ✓ **三模型覆盖**：`M_loc`（需 global correlation ⟹ 已被 `S6` 局部性锁死＋第一断裂＋`W6` 原子墙覆盖）｜`M_stat`（需 β-敏感非零侧量 ⟹ 已被 β-盲＋`T7`＋`O1-1` 操作性 β-盲覆盖）｜`M_trans`（需 `Δ_rigidity` ⟹ 自然实现皆已有命名量 ⟹ `N0′` FAIL）⟹ `FCG-0.4 = NO` ✓ ⚠️ **措辞纪律**：写**尚未发现**，**不写不存在**（搜索结论 ≠ 不可能性证明）✓ ⭐ **性质定性与区别**：与 `C-380`／`GT`／`E-10` 的『逐个候选关闭』不同，本项是**元层面**负结果资产；状态定性＝『**当前这一整类方向已被搜索过滤器封到一个明确边界**』（**非**『没方向了』）✓ **纪律**：**不为『必须还有下一刀』而再造候选** ✓。**状态＝已登记（元层面负结果资产）** ⚠️ **2026-09-23 09:56 降级注记**：本项为**方法学级**，**不构成数学进展**（无新对象／新定理／新机制／新 RH 接口）；只是把已有 NO-GO 重新组织为三模型／过滤器 ⟹ **不得作为『研究进展』记入**；`FCG` 路线**已停** ✓ |
| **D-17** | 🆕 **`IP-1` 收口：`d_V`＝rank-flag complete；`extra_zeros`＝标准 Möbius 几何（无新机制）；`IP-2` 第一轮 exit 3** | `docs/IP-1-CLOSURE-and-IP-2-ENTRY.md` | ⛔ **收口结论**：`IP-1C1 = CLOSED`（**有价值的 CLOSED**：机制被精确剥离，但属**经典零点几何**）✓ ⭐ **决定性理由**：强制消失阶＝代数存在性；剩余根位置＝环境几何 ⟹ **代数—几何分离是 T-system 框架自带**（本仓 `M0` 已证零点计数在递增双射下拉回保持 ⟹ 位置必然落在几何里）⟹ **二分近乎定义式，非可搬运新机制** ✓✓ ⛔ **`IP-2` 第一轮 ＝ exit 3（立即 CLOSED）**：二分结构＝已有 T-system／alternation／interlacing ＋ 标准射影几何的重述；**无新定理、无新猜想资产** ✓ ⚠️ **HOLD**：`H5` 逆问题／处方可达性未被排除，但（i）本族平凡、（ii）一般情形需扩样而**扩样被令禁止** ⟹ **不可开** ✓ ⛔ **禁项**：扩样／开 `C2`／造新定理·新猜想／以 RH 相关性计成功 ✓。**状态＝已封闭（线级收口）** |
| **D-18** | 🆕 **`WALL-BREAK` 封存：`WB-A-1` CLOSED ／ `WB-B-1` CLOSED ／ `WB-B-2` FAIL；「封住 ≠ 不存在」三层界定** | `docs/WALL-BREAK-CLOSURE-and-the-honest-scope.md`｜`docs/WB-A-1-and-WB-B-2-firewall.md`｜`docs/WB-B-1-W6-KT-signed-cancellation-first-cut.md` | ⛔ **两个精确 obstruction（有内容 ✓）**：① **`β` 通道**＝只经**重数／退化**可见 ⟹ 退化计数**操作性 `β`-blind（RH 等价级）**，`β-sensitive ⟹̸ β-operational` ✓；② **`J3` 预算障碍**＝**任何固定阶衰减（含 sign 相消）只能改 log budget、不能破 `T^η`** ⟹ 跨越需**非 decay-based 机制** ✓ ⛔ **`WB-B-2` 入口 FAIL**：「非 decay-based coercion」是**否定式／类型描述**，过不了 `FCG-Sep`／`N0′`／`N2` ⟹ 登记为**准入规格**（`(α)` 具名具体机制｜`(β)` 独立问题＋真参数｜`(γ)` 至少一对已登记对抗模型的分离见证｜`(δ)` 一轮内可判定｜`(ε)` 过 `de-RH`）✓ ⭐ **三层界定（措辞纪律）**：搜索级结论**成立**（当前入口空间封到边界）｜两个 obstruction **成立**｜**数学级不可能性未成立**（无任何定理说『不存在桥』或『墙不可破』）⟹ ⛔ 只能说「未找到／封到边界」，⛔ 不得说「已彻底封住／不存在突破口」✓ ⚠️ **未闭合三处**：一般 `β`-object 未定义（定义型缺口）｜非 decay 机制仅准入规格｜`local`／`parity`／`correlation-defect`／`zero-statistics-rigidity` **本轮未攻（未知，非已闭）** ✓ 【纪律】`D1=2` **非许可信号**；⛔ 不得在 `WALL-BREAK` 内部找「第三刀」✓。**状态＝已封闭（线级封存）** |
| **D-19** | 🆕 **`WS-J1b` 边界收紧：`\sqrt x` 是通用平方根指数，非临界线 `1/2`；`x\leftrightarrow\zeta` 对应未建立 ⟹ 敏感性问法被禁** | `docs/WS-J1b-presupposition-free-symmetry-computation.md` §5（勘误＋边界＋门） | ✅ **保留的正面结构事实**：`S_x f(t)=\frac xt f(\frac xt)` ⟹ `S_x^2=x\cdot\mathrm{Id}`；基 `\{1,t^{-1}\}` 上矩阵 `\begin{pmatrix}0&1\\x&0\end{pmatrix}`（**本档订正：原写为转置** ✗）⟹ 特征值 `\pm\sqrt x` ✓ ⚠️ **核心边界**：`\sqrt x` 里的 `1/2` 是**平方根运算自带指数**（对**任意** `y>0`，`S_y` 同型给出 `\pm\sqrt y` ⟹ **通用**）≠ **临界线那个 `1/2`**；二者在 Lebesgue 归一化下**对齐但不同一** ✓ ⚠️ **机制**：`S_y=D_{1/y}\circ J` 中 `y` **恰好出现一次** ⟹ 平方得 `y^1` ⟹ 单次分到 `\sqrt y`＝"因子被两次操作平分"的必然 ⟹ **纯线性代数** ✓ ⛔ **门**：未建立 `x\leftrightarrow\zeta` 显式对应前，**不得问"对离轴是否敏感"**（**尚无具体对象可问**）✓ ⚠️ **与 RH 距离**：**不比**此前审计过的「`\beta` 可见但不可操作」候选**更近** ✓ **下一步合法动作（二择）**：**(a)** 建立 `x\leftrightarrow\zeta` 显式对应（可判定的具体任务）；**(b)** 收手记为档级资产 ✓。**状态＝已封闭（边界已收紧）** |
| **D-20** | 🆕 **`J-1` 终局：CLOSED ／ classical operator identity ／ no ζ-specific interface ／ 不升 `D_new`；并提高 `JAM-INVENTORY` 判准一档** | `docs/WS-J1b-presupposition-free-symmetry-computation.md` §7｜`docs/JAM-INVENTORY-concrete-blocked-steps.md` §4 | **四层审计（照录）**：算子事实 `S_x^2=x\cdot\mathrm{Id}`（谱 `\pm\sqrt x`）｜机制来源＝缩放因子在两次对合中的**平方根分配**｜**RH 特异性＝没有**（任意 `y>0` 同型）｜**RH 接口＝未建立** `x\leftrightarrow\zeta` 的非人为对应 ⟹ 不得提敏感性问题 ✓ ⭐ **降格表述**：$$	ext{一个正确而普适的算子论恒等式，不构成 RH 新机制}$$ ✓；**价值所在**＝完成"位置→谱"审计并把障碍定位为：$$\pm\sqrt x	ext{ 可一般性产生，但无任何东西说明 }x	ext{ 与零点算术数据有必需联系}$$ ✓ ⛔ **禁令**：不得再由 `S_x^2=x\cdot\mathrm{Id}` 派生"平方根—临界线"路线（＝**普适代数结构冒充 RH 特异机制**）✓ ⭐ **提高后的判准（`JAM-INVENTORY`）**：值得继续的 pen stop 须＝**具体算术计算中出现不可消除的结构缺口，且缺口本身携带算术信息**；按此**第一遍分档**（本仓判定，非裁定）：`J-1` ✗｜`J-2` ⚠️边界（设定算术、缺口解析型）｜`J-3` ⚠️边界（通道 RH 等价级）｜**`J-4` ✓ 形式上唯一合格**（缺口＝`1/3=R-1`，跨越需 `support>1` 算术输入）✓。**状态＝已封闭 ／ 不升 `D_new`** |
| **D-21** | 🆕 **`J-4` 严格一轮审 ＝ CLOSED ／ representation-level reformulation ／ no `D_new`；`JAM-INVENTORY ＋ WS-J1b` 整体归档** | `docs/J-4-STRICT-AUDIT-one-round.md`｜`docs/JAM-INVENTORY-concrete-blocked-steps.md`｜`docs/WS-J1b-presupposition-free-symmetry-computation.md` | **问 1（惯性）**：功能方程给 `(1,1)` block ⟹ $$n_-(Q)=\#\{\text{离轴对}\}=p;\ N\ge s_1+2s_2+2p;\ n_+(Q)\le p$$ ⟹ **不定度被算术量 `p` 精确计量** ✓ **问 2（是否仅表示障碍）**：`E-11`（indefinite → inertia → rank → counting）**不需 `Q\succeq0`** ⟹ **绕开 `V182`** ⟹ ⚠️ **缺平方根只阻断正性路线（⟺RH），不阻断计数路线** ✓ **问 3（缺口是否携算术量）**：`2/3 ⟺ R=4/3`；缺口 `1/3=R-1` **＝旧交换率账本**；`R>1` 所需＝**已登记 `support>1` 原子墙**（`C-25`：前沿 `2/3` 天花板 ＝ 我们 `0.682` ＝ 同一墙）⟹ ✗ 非新算术量 ✓ **问 4（外溢）**：(a) 破 `2/3` ✗（`2/3` **就是本机制产出**；`0.68185` 为同矩类已证天花板）｜(b) 有限离轴 ✗（`V186` §3 终点退化 ⟹ 退回正性）｜(c) 其他素数问题 ✗（`E-12` 仅后置接口）｜(d) 非素数猜想 ✗ ✓ ⛔ **硬出口未达** ⟹ 命中「反之」分支**逐字**：「不定性只是已有 inertia／support wall 的另一种表达；`R-1` 只是旧交换率账本；平方根不存在没有产生新的算术约束」✓ ⛔ **依令**：`JAM-INVENTORY ＋ WS-J1b` **整体归档**，**不再从 `J-4` 失败派生路线** ✓。**状态＝已封闭** |
| **D-22** | 🆕 **"哪里还可能出现新机制"回看：四未审计攻击点第一遍吸附检查，全部有落回旧账本的预兆；未找到未被覆盖的位置** | `docs/WHERE-CAN-NEW-MECHANISM-APPEAR-survey.md` | **七墙审计状态**：`\beta`-blind／majorant／`W6` 三点 **已本轮 CLOSED**；**local／parity／correlation／zero-statistics 四点未审** ✓ **吸附检查（第一遍）**：`local` ⟹ 落 **`V126` L3**（`A_2` 被封；`V276` 两角都落 L3 边界）｜`parity` ⟹ **42 档存量**（含 `C110`／`C122` 系统性审计）吸附风险最高｜`correlation` ⟹ 已有攻击动作登记（`TACTICAL-ATTACK-MODE` **`D3/D4` 稀疏主导 witness**；`W8` 信息量上界），但**每条自带已知 barrier（`cylinder barrier`）**｜`zero-statistics` ⟹ 落 **`O1-1`**「无两墙间稳定计数」锚定墙 ✓ ⛔ **结论**：在当前工具集与档案覆盖下，**未找到"还可能出现新机制的位置"**；⚠️ 但**不是"不存在"** —— 唯一未覆盖的合法形态是 **`E-20` 定义的"尚未被使用的具体数学计算"**（**是一个待出现的对象，不是一个位置**）✓ 【排序（仅指"已登记未执行"）】`correlation` 的 `D3/D4` 稀疏 witness 唯一在册未见执行，⚠️ 用之须先答 `E-20` 第 4 条 ✓。**状态＝已封闭（回看级）** |
| **D-23** | 🆕 **`C-1a` 三层隔离第一刀 ＝ CLOSED；`D`/`B`/`C` 三入口全部干净收口** | `docs/C-1a-three-layer-isolation-CLOSED.md`｜`docs/B-1-dual-representation-defect-CLOSED.md`｜`docs/CAS-1B-high-order-vanishing-scan-STOP.md` | 【`C-1a`】两侧**各自内部**扫描（不算差 ✓）：算术侧 `\mu` 无结构／`\lambda` 有**一次**精确消失（`M=7`, `det=0`）⚠️ 但 `\lambda` 是 `\zeta(2s)/\zeta(s)` 系数 ⟹ **旧账本**；零点侧（修正窗口 `k=14..50`）秩亏由**稀疏/阶梯支撑**解释，`det` 与**随机对照同阶** ⟹ **无 ζ 特异结构** ⟹ **命中 STOP ①/④/⑤** ⟹ `C-1a = CLOSED`，**`C-1b` 不进入**（跨侧无非平凡指纹相等）✓ ⚠️ **本档自查缺陷**：零点侧初版窗口 `k=1..26` 全在 `\gamma_1=14.13` 之下 ⟹ 退化/空转 ⟹ 已修正重跑，⛔ 未据缺陷结果下结论 ✓ 【三入口总收口】`D`＝`CAS-1`/`CAS-1B` **STOP**（全阶满秩、谱随 `k` 平滑、ζ 与对照差别仅尺度增长）｜`B`＝`B-1` **CLOSED（经典 Dickman 账本定量解释）**｜`C`＝`C-1a` **CLOSED（两侧无新结构）** ⟹ `D_{\rm new}` 仍为 **0** ✓ 【状态】回到 `AMEND-3/4`：**目标可留（RH）、渠道须换**；**唯一开放边界＝一个独立来源的具体计算（尚无候选）**。**状态＝已封闭（入口级）** |

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
| **E-9** | 🆕 **反向生成器：反例 → 不可见核 → 最小缺失信息** | `docs/REVERSE-0-counterexample-invisible-kernel-scan.md` | 方法论（跨项目适用）：把已证约束写成 `Φ: X→ℝ^m`；**反例族 ＝ 同一 `Φ` 值而 `P` 变化者** ⟹ **`ker Φ` 的显式见证**；继而求**最小缺失坐标**（使 `Φ+Ψ` 对 `P` 敏感的**最小复杂度** `Ψ`）⟹ 输出 **OPEN 攻击点**（而非 NO-GO）✓ **三硬问题**：G1 家族性／G2 不可见方向／G3 `P` 沿核变化 ✓ **首轮三族全部通过**：F1 β-blind（Hankel 矩 β-盲；缺失坐标＝**重数/退化**，`V192` 已点出）｜F2 C-380 近碰撞（`|δ| ≲ 8.8e-20`；缺失坐标＝**符号/相位**）｜F3 有限处局部数据恒等（缺失坐标＝**Archimedean 层**，`D-3`）⟹ **三处 OPEN** ✓ ⭐ 与传统过滤相反：**不要求文献已有成熟机制**，只要求「**反例迫使一个尚未被现有约束记录的量出现**」✓。**状态＝已登记·可用** |
| **E-10** | 🆕 **`KH-FRONTIER-SHAPE`（KH 系列前沿形状 ＋ 候选准入 N1–N7）** | `docs/KH-FRONTIER-SHAPE.md` | 把 `KH-2→KH-4` 已证结果压成**候选准入筛**：**已封闭 11 入口**（各附再开条件）＋ **正空间三要素**（prime-native 对象 ＋ 独立数学问题 ＋ 真正可变参数）＋ **禁止反向**（不得从 RH 的 `1/2` 反找算子）＋ **N1–N7 硬门**（⭐ **N4 ＝ 参数变化须改变 quantity 而非仅 representation**，为 `KH-4` 暴露之**核心漏洞**）✓ 与既有 `NOGO-registry-and-screens`（准入判据 ＋ 两筛）／`HOT-STATE`（交接）／`EXPLORATION-POINTS-REGISTER`（探索点）**并存互补，不替代** ✓ 核心句：**当前缺口已不再是「从哪里得到 1/2」，而是「找到一个独立的、参数真正改变其数学内容的算术对象，并让 RH 成为它的后置性质」** ⟹ 作 **Rule T ＋ SURVIVOR-5 联合入口** ✓。**状态＝已登记·可用** |
| **E-11** | 🆕 **新机制：indefinite form → inertia → rank → zero counting** | `docs/V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md`｜`docs/KH-5-R8-B-S2-NONLOCAL-C.md` | **来源**：`arXiv:2608.13637v2`（Weil Hermitian form 的有限压缩＋rank-trace＋Sylvester 惯性）✓。**机制**：不要求 `Q >= 0` ⟹ 绕开 `V182` 的困境（PSD 正性 ⟹ 无计数界）✓✓；**交换率**：`N_0^s/N >= 2 - R(psi)`，`2/3` ⟺ `R = 4/3` ✓；**终点退化**：`100% ⟺ n_- = 0` 对全族 ⟹ 半正定 ⟹ Weil 正性 ⟺ RH ⟹ 路线在「消灭离轴零点」步退回正性 ◊ ✓；**定位**：与直接 Weil 正性**不同的部分计数机制**，作为**独立工具资产**保留 ✓。**唐先生 2026-09-22 23:24 定：「不能把整条线简单记成 DEAD，须作为资产保留」✓。**状态＝已登记·可用** |
| **E-12** | 🆕 **转移原理：二阶矩 ＋ 惯性 ⟹ 计数下界** | `docs/V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md` §0④｜`docs/KH-5-R8-B-S2-NONLOCAL-C.md` §7 | **来源**：`V186` 判词逐字「**转移原理（二阶矩＋惯性 ⟹ 计数下界）—— 是 `V182` 的对偶面，应进工具箱**」✓✓。**定位**：未来若出现**完全不同的 global arithmetic object**，可**重新调用**（不是新主线，是后置接口）✓。**唐先生 2026-09-22 23:24 定：「须作为资产保留」✓。**状态＝已登记·可用** |
| **E-13** | 🆕 **五出口评价框架 ＋ 去 RH 化测试（`E-10` 正式准入标准）** | `docs/KH-FRONTIER-SHAPE.md` §9｜`docs/E-10-ROUND2-candidate-generation.md` §7 | ⭐ **原则升级**：新机制不得压成单一 `-> RH`；改为多出口 $$新机制 -> {RH 搭桥 | 零点比例 | 有限离轴零点 | 其它素数问题 | 其它猜想}$$ ✓ **五出口最低信号**：A `非等价、非显式公式搬运`｜B **`2/3+delta`**（严格区分五类：重证 `2/3`／仅改误差仍 `2/3`／**`2/3+delta`**／趋近 `1`／`1`；**只有第三类以后才算突破**）｜C **`N_off(T)=O(1)` 等结构性控制**（三种成果严格区分：有限高度计算性／**离轴零点有限＝结构性**／不存在＝RH）｜D `新量/新指数/新误差/新结构`｜E `独立猜想上的实质推进` ✓ ⭐ **战略变更**：**A 不成立 `≠>` DEAD**（B/C/D/E 任一有真新增益即保留为独立主线或强资产）✓ ⭐ **去 RH 化测试**：**即使 RH 从研究计划中删除，这个推导是否仍值得做？** —— 用以阻断「为找 RH 接口而把对象重包成 Weil／显式公式／零点谱／`1/2`」的旧循环 ✓✓ **重定位**：`KH-5` 的 A 出口封口，但 `E-11`／`E-12` 依 B/C/D/E 保留；⛔ 不问「`E-11` 能否证 RH」，⭐ 问「**`E-11` 在非 Weil 对象上能否产生新计数增益**」✓。**状态＝已登记·正式标准** |
| **E-14** | 🆕 **前置门 `N0′`「参数独立性」＋ `C-A` 校准负例** | `docs/E-10-C-A-N6-N7.md` §7｜`docs/E-10-ROUND2-candidate-generation.md` §8｜`docs/KH-FRONTIER-SHAPE.md` §10｜`docs/E-10-ROUND2.5-candidate-regeneration.md` | ⭐ **新增准入门（置于 `N1` 之前）**：`N0′ : θ ≢ 已有文献中的限制／权／扭曲／子集／尺度参数`（至少不能只是换名字）✓ **问法（`N6` 优先级前移）**：看到「自然参数」时**先问**『这个参数是不是早已作为某种限制／twist／子集／权／局部化／deformation 在文献中出现？』 —— **而不是先投入 `N5` 结构展开** ✓✓ ⭐ **正式准入顺序**：`N0′ → N1 → N2 → N3 → N4 → N5 → N6/N7` ✓ **校准负例（`C-A`）**：`N1–N5` 全过、`N7` 过，**但 `θ`（素数子集形变）＝已有命名对象 `D_S`**（Haukkanen 2019）⟹ **`N0′` FAIL ⟹ 不 Promote**；**`C-A = GAP/WATCHLIST`（非 DEAD；复活条件＝发现 `D_S` 框架外的新不变量）** ✓ **配套处置**：`C-B` ＝ `N0′` 快审 FAIL（参数为数字展开／自动机／数字和／受限数字／正规性理论的标准参数 ⟹ 不进 `N6/N7`）｜`C-C` ＝ 暂不优先（成熟度＋『已知周期→已知密度→变形→看似新参数』循环风险）✓ **战略纪律**：**宁可 `E-10` 暂停，也不要为保候选数量硬推** ✓。⭐ **`N0′` 门第 2 次命中（2026-09-23 08:56）**：`D-1`（整数复杂度＋代价模型）**`N0′` FAIL** —— `θ`（代价模型）＝已有链类参数化（**addition–multiplication chains**，*Discrete Math.* 308(4) 2008, 611–616）；且其 `N5` 项 `‖mn‖ ≤ ‖m‖+‖n‖` **系定义级平凡次加性**（自纠）⟹**`D-1 = GAP/WATCHLIST`**，**直接停、不做 `N1–N7`** ✓；⟹ 两样本（`C-A`／`D-1`）**全部倒在「参数已有命名对象」**上 ⟹ **`E-10` 正式冻结**（筛选器链条**两度验证、长期可复用**；出现参数非已有命名对象者可立即重启）✓。**状态＝已登记·正式标准（`E-10` 已冻结）** |
| **E-15** | 🆕 **`GT-STRATEGY`：transfer-principle-first 搜索模式（方法论）＋ `GT-0` 快审 FAIL** | `docs/GT-0-and-GT-STRATEGY-audit.md` | ⭐ **核心洞见**：『**真正的新东西未必是新的算术对象，也可能是「把已有强定理转移到新对象的机制」**』⟹ 可绕开『是不是只是 explicit formula／zero statistic／换 kernel／重新编码 β』✓ **`GT-0` 三问**：问 1（是否存在**非标准** prime-native quantity）＝ ⛔ **FAIL** —— 七项候选量**全部**为已有标准参数或我方已封条目： 相对密度 δ／majorant 与伪随机性条件（⚠️ 且我方 `W6-MAJORANT` 线 **`C-30` 已封存，正式 FAIL**）／Gowers `U^k` 范数／linear forms complexity（GTZ 的 `s(Ψ)`）／singular series（⚠️ 且我方 **`S6` 锁死**：奇异级数只记 local admissibility，不得作活口）／AP 长度 `k`／averaging dimension ⟹ **依令立即封，不进 Gowers／transference 技术细节**；问 2／问 3 未进入 ✓ **⭐ 诊断层交叉验证（非新 quantity，adjacent asset 级；⚠️ 2026-09-23 09:43 修正表述）**：**GT 框架对某些线性配置可转移**（如 AP），**而孪生素数等一参数模式仍受 sieve／parity／complexity 型障碍** —— ⛔ **不得**把 GT 无法解决孪生素数的**全部原因**归结为 **p=2 的局部不可容许性**；**三层须分开**：**local admissibility ≠ parity／sieve limitation ≠ configuration complexity** ✓ ⟹ ⟺ 我方 **parity barrier**（`D-11` 系）＋ **`S6` 锁死** ＋ **原子墙**（`W6`：三阶矩 ≡ prime-pair ≡ support>1，不可再分）✓ **`GT-STRATEGY` 定义**：`GT-1` 找出真正**不可替代**的 transfer mechanism｜`GT-2` 抽象 `A →T→ B`｜`GT-3` 是否有 **arithmetic analogue** 且产生**新 quantity**（⚠️ 本问即 `N0′` 门，不得绕过）｜`GT-4` 最后才问 RH ✓ **⚠️ 诚实限定三条**：① 档案**已有 `E-12`「转移原理」**（二阶矩＋惯性 ⟹ 计数下界）⟹ **概念层非新**（引用）｜② `transfer` 在多个领域皆为标准词 ⟹ **首刀只能是方法论审计**，不得当量｜③ **研究假设，非已存在的 RH 桥** ✓ ⭐ **定性（照录）**：**E-15 ＝ 方法论资产／candidate-generation principle（KEEP / METHODOLOGICAL）**；⛔ **不是**新数学机制／新 arithmetic quantity／RH bridge／live mainline ✓ ⭐ **新增硬门（transfer 专用）**：任何所谓 transfer mechanism **必须在 transfer 之后产生一个此前不存在的 arithmetic observable**；若只是已有 **majorant／Gowers／singular series／explicit-formula／positivity／zero statistic** 的**重新组织** ⟹ **立即 FAIL** ✓✓ ⭐ **硬限制**：**方法论可迁移 ≠ quantity 可迁移**（阻断把 transfer principle 本身再包装成新对象）✓ ⭐ **主线新形式**：`GT-STRATEGY → 寻找 transfer mechanism → N0′ → 新 quantity`（而非 `GT → Gowers → majorant → 再撞旧墙`）✓ ⚠️ **诊断层交叉验证 ≠ 机制同一性证明** ✓。**状态＝已登记·可用（方法论级）** |
| **E-16** | 🆕 **`FCG`（Failure + Counterexample Guided Search）搜索过滤器 ＋ 三 adversarial model ＋ failure-signature 表** | `docs/FCG-0-adversarial-models-and-failure-signatures.md` | ⭐ **核心转向**：『**先收集旧方法为什么失败 → 列出必须绕开的反例 → 构造满足这些约束的新量**』（failure-guided construction）✓ **流程**：`旧方法失败 → 提取失败条件 → 构造反例模型 → 要求新量区分反例 → N0′ → N1–N7` ✓ **第一条规则**：**一个候选量只有在能击穿至少一个既有 adversarial model 时，才值得进入 `N1`** ✓✓ **三模型**：`M_loc`（保留 local admissibility／破坏 global correlation／专杀 singular-series 型）｜`M_stat`（保留 zero statistics／破坏 arithmetic β-structure／专杀 zero-statistics·majorant 型）｜`M_trans`（保留 transfer 平均性质／破坏目标刚性相关／专杀『平均可迁移 ⇒ 一参数相关』）✓ **⭐ 硬门（正式登记）**：任何 transfer mechanism／候选量**必须在 transfer 后产生一个此前不存在的 arithmetic observable**；若只是已有 **majorant／Gowers／singular series／explicit-formula／positivity／zero statistic** 的**重新组织** ⟹ **立即 FAIL** ✓✓ **新增前置门 `FCG-Sep`**：须至少存在一个 adversarial pair `(M_i,M_j)` 使 `Q(M_i) ≠ Q(M_j)`，**且不得靠把目标编码进 `Q`** ✓ **⛔ 防循环**：**Counterexample separation ≠ target encoding** ✓ **⚠️ 概念纪律**：adversarial **test model** ≠ RH counterexample（不得用于证 RH 错／证模型存在）✓ **`FCG-0` 判定**：`0.1`（所需区分＝global correlation ⟹ 已被 `S6`／第一断裂／`W6` 覆盖）｜`0.2`（＝β-敏感非零侧量 ⟹ 已被 β-盲／`T7`／`O1-1` 覆盖）｜`0.3`（＝`Δ_rigidity` ⟹ 其自然实现皆已有 ⟹ `N0′` FAIL）｜⭐ `0.4 = NO` ⟹ **三模型全被现有墙覆盖**；⚠️ **核心结论正式措辞（须逐字沿用）**：『**在当前已登记机制、反例模型和 `N0′` 过滤器覆盖范围内，尚未发现一个此前不存在的 arithmetic observable，能够区分 `FCG-0` 的三个 adversarial model**』—— ⛔ **不得**改写为「不存在」／「根本上不可能」（**搜索结论 ≠ 数学不可能性证明**） ⟹ 『**当前搜索空间缺的不是新公式，而是一个全新的可区分维度**』✓✓ **状态＝已登记·可用（搜索过滤器级）** ⚠️ **2026-09-23 09:56 降级注记**：本项为**方法学级**，**不构成数学进展**（无新对象／新定理／新机制／新 RH 接口）；只是把已有 NO-GO 重新组织为三模型／过滤器 ⟹ **不得作为『研究进展』记入**；`FCG` 路线**已停** ✓ |
| **E-17** | 🆕 **`SEARCH-FIREWALL`：统一准入防火墙（平台化）** | `docs/SEARCH-FIREWALL.md` | ⭐ **门序（唯一入口）**：`FCG-Sep → N0′ → N1 → … → N7 → 五出口 → 去 RH 化测试`（外加 `FCG` 硬门 ＋ `E-9` 反向生成器）✓ **整理对象**：`E-9`（反向生成器）｜`E-11`／`E-12`（工具箱·后置接口）｜`E-13`（五出口＋去 RH 化测试）｜`E-14`（`N0′` 参数独立性）｜`E-15`（转移原理·方法论）｜`E-16`（`FCG` 过滤器）＋ `KH-FRONTIER-SHAPE` §9–§12（`N1`–`N7` 与门序）✓ **四行状态**：`GT-0 = FAIL`｜`E-15 = KEEP/METHODOLOGICAL`｜`FCG-0 = FAIL`｜`E-16 = KEEP/SEARCH FILTER`（**两个 `FAIL` 性质不同**：前者＝量来源失败；后者＝新 distinction 尚未出现，**信息量更大**）✓ **再启动条件（唯一）**：『**它带来了什么此前不存在的 arithmetic distinction？**』须给出 `D_new: M_i ↦ D_new(M_i)` 且**至少区分一个已有 adversarial pair** ⟹ 才重开 `FCG-1` ✓ **⛔ 立即 FAIL 清单**：更好的 correlation／新 rank／新 dimension／新 Gowers 型量／新 majorant／新 singular series／`β` 的另一种包装／zero-side statistic／existing transfer 的重新参数化 ✓ **用途**：**任何新想法先过此层**，以减少重入『漂亮公式 → 技术深挖 → 旧墙』的循环 ✓。**状态＝已登记·可用（平台级）** ⚠️ **2026-09-23 09:56 降级注记**：本项为**方法学级**，**不构成数学进展**（无新对象／新定理／新机制／新 RH 接口）；只是把已有 NO-GO 重新组织为三模型／过滤器 ⟹ **不得作为『研究进展』记入**；`FCG` 路线**已停** ✓ |
| **E-18** | 🆕 **`Independent-Problem Pivot`：评价函数更换（`P1`–`P5`）＋ 停止 `FCG`** | `docs/INDEPENDENT-PROBLEM-PIVOT.md` | ⚠️ **诚实降级**：`FCG-0` **没有增加新的数学对象／定理／机制／RH 接口** —— 只是把已有 NO-GO（β-blind＋local＋majorant＋correlation＋zero-statistics＋parity＋`W6`）重新组织为三模型 ⟹ **不是实质突破**；**我的错误 = 把方法学进展当成数学进展** ✓ ⛔ **停止 `FCG`**（递归危险：`NO-GO 地图 → 元 NO-GO 地图 → 更高层过滤器 → …` ⟹ 只得到越来越完善的**失败分类学**）✓ ⭐ **新问法**：『**有没有一个独立数学问题，本身要求一种我们目前没有的结构？**』（旧问法天然把搜索限制在 NO-GO 地图内部）✓ ⭐ **正确顺序**：`Independent Problem → new mechanism → arithmetic realization → RH`（⛔ 而非 `RH wall → 穿墙量`）✓ ⭐ **`Independent Problem Test`**：`P1` 独立问题（去 RH 仍非平凡）｜`P2` 未知机制（非 Gowers／rank／correlation／sieve dimension／explicit formula／majorant／spectral encoding 的重新包装）｜`P3` 真正的参数（改变问题本身非坐标）｜`P4` 可证伪（须有 conjecture／extremal law／recurrence／rigidity 可被击穿）｜⭐ `P5` **与 primes 的连接暂时可以没有**（允许 ⊉ RH、甚至 ⊉ primes）✓✓ ⭐ **理想结构**：`𝒫_θ: X_θ(n) ⇢ rigidity law` ⟹ 先得 Theorem/Conjecture A ⟹ 再发现算术实现 ⟹ 最后 RH interface ⟹ 才是**真 new mechanism** ✓ **sourcing 协议**：只从**某领域自身的开放问题**取材；⛔ 不得从本仓 NO-GO／过滤器／反例模型取材；先过 `P1`–`P4`；**若一轮 0 通过则如实报告**，不得为『必须有下一刀』造候选 ✓ **总纲**：**彻底停止从旧路的失败中生成候选** ✓。**状态＝已登记（新评价函数·sourcing 协议）** |
| **E-19** | 🆕 **`IP-1` 三资产 ＋ 二层分解失败模板（forced zeros / geometric residual roots）** | `docs/IP-1-CLOSURE-and-IP-2-ENTRY.md`｜`docs/IP-1-C1-residual-root-geometry.md`｜`docs/IP-1-G0b-v2-v3-verdict.md` | ⭐ **三资产**：`d_V` ＝ **B 强确认**（完全由 rank flag 决定；恒等式 8208/8208）｜`extra_zeros` ＝ **C 已解释**（不由 rank 决定，由**根位置**决定）｜`r(a)=(a-1)/(2a-1)` ＝ **显式结构资产**（**Möbius 对合**、无实不动点、`dr/da=(2a-1)^{-2}>0`）✓ **失败模板**：`rank flag → forced zeros + geometric residual roots` ✓ **区间律（本族 `q=1,r=2,S={-1,a}`）**：`ec=1 ⟺ a∈[-1,0]∪[2/3,1]`；`ec=0 ⟺ a∈(0,2/3)`（`a≠1/2`）；极点 `a=1/2` ＝ **flag 边界**（前缀已降秩 ⟹ `d_V=q+1`）✓ ⚠️ **判死门已命中**：`r(a)` 为 **Möbius／射影几何标准对象** ⟹ **不构成新机制**；⛔ 不得称为新 invariant ✓ ⚠️ **诚实边界**：阈值与显式形式**为本族专有**；**不声称**一般 `(q,r)` 律 ✓。**状态＝已登记·可用（资产级）** |
| **E-20** | 🆕 **下一项研究准入门槛（5 问）＋ `JAM-INVENTORY` 批次封存状态** | `docs/JAM-INVENTORY-concrete-blocked-steps.md` §5（账本＋批次状态）｜§6（5 问门槛）｜`docs/J-4-STRICT-AUDIT-one-round.md` | ⭐ **搜索定义**：下一项研究必须从一个**尚未使用的具体数学计算**出发，⛔ 而非从 RH 现有障碍出发 ✓ ⭐ **首次出现即须能答的 5 问**：**1** 算术对象是什么？｜**2** 现有运算在哪里**精确失效**？｜**3** 失效留下的**量**是什么？｜**4**（**现最关键**）该量是否**不是**已有 `rank`／`support`／`parity`／`majorant`／`\beta`-blind **账本的改写**？｜**5** 是否自然延伸到 **RH 之外的独立问题**？✓ ⚠️ **第 4 条校准反例**：`J-4` —— "缺口看起来带算术量"**还不够**，$$	ext{必须证明它不是旧账本换一种坐标后的同一个量}$$ ✓ **批次状态**：`JAM-INVENTORY = CLOSED ／ SEARCH BATCH EXHAUSTED ／ NO-DERIVATIVE REOPENING`；**`D_new` ＝ 0**；⚠️ **不是**"RH 搜索失败"（太强），准确＝**这一种"从具体卡点寻找被迫新对象"的四个已审入口全部没有产生新数学入口** ✓ ⛔ **重启**：须从**完全独立的新问题／新计算**进入，⛔ 不得从 `J-1…J-4` 残骸继续挖；⛔ 不得再抽象"更深的共同障碍"（重入 repackaging→obstruction→…循环）✓。**状态＝已登记·可用（门槛级）** |
| **E-21** | 🆕 **冻结语义精确化（`AMEND-3`）＋ 启动条件：换的是 discovery channel，不是 attack target** | `docs/RESEARCH-CONSTITUTION.md` §8.1-AMEND-3｜`docs/WHERE-CAN-NEW-MECHANISM-APPEAR-survey.md`（`D-22`） | ✅ **允许**：以 **RH 为最终目标**；使用**既有谱／算术／零点工具**；⭐ **新机制 `M` 接回原 RH 主链**：$$M\to\text{原有算术/谱框架}\to\text{RH}$$ ⟹ 【**新机制 ＋ 旧框架 ✓**】✓ ⛔ **禁止**：【**旧障碍 → 旧框架再包装 → 声称"新机制" ✗**】✓ ⭐ **原则**：$$\text{换的是 discovery channel，不是 necessarily attack target}$$ ✓ ⭐ **启动条件（严格）**：$$\text{先有具体计算，再有机制；不能先有机制名，再去找计算}$$ ✓ ⭐ **`D-22` 真正含义**：**不是"换方向"**，而是**暂时停止从旧方向的内部结构寻找新机制** ✓ **当前终态**：当前档案覆盖下**没有已知的合法新入口**；**未知空间仍然开放但尚无候选**；⚠️ 与"RH 方向全部封死"**是两个不同命题** ✓ ⛔ **`D3/D4` 不执行**："唯一未执行"**不是充分理由** ✓。**状态＝已登记·可用（协议级）** |
| **E-22** | 🆕 **「独立」＝发现来源独立（非对象与 RH 无关）＋ 合法发现通道 ＋ `\mathcal D_{\rm legal}` ＋ 四指标同步记账** | `docs/RESEARCH-CONSTITUTION.md` §8.1-AMEND-4 | ⭐ **合法通道**：$$\text{RH 相关对象}\overset{\text{具体计算}}{\to}\text{异常/新结构}\overset{\text{机制提炼}}{\to}M_{\rm new}\to\text{既有 RH 接口}\to RH$$ ✓ ⭐ **关键**：新结构**必须由计算"逼出来"**，⛔ 不能由旧 RH 墙"设计出来" ✓ ⭐ **搜索空间**：$$\mathcal D_{\rm legal}=\{\text{RH-connected}\}\setminus\{\text{old-wall-driven discovery}\}$$ ⟹ **`D-22` 并未把我们赶到 RH 之外** ✓ ✅ **启动逻辑**：先选 **RH 相关、但问题本身有独立数学内容**的具体量 → 算 `Q_1..Q_N` → 发现**未被账本描述**的规律 → 问"这规律**强迫**什么新对象" → **最后**才检查能否接 ①β-visibility ②coercivity ③zero exclusion ④prime problems ⑤other conjectures ✓ ⛔ **反序禁止**：「β 不可见 → 找 β-sensitive quantity → 造新符号」＝回到旧方向 ✓ ⭐ **四指标从第一笔计算起同步记账** ✓；⭐ **本仓提议的前置过滤**：现象须能**不用 `rank`／`support`／`parity`／`majorant`／`β`-blind 术语**描述（否则＝旧账本改写，`E-20` 第 4 条 FAIL）✓。**状态＝已登记·可用（协议级）** |
| **E-23** | 🆕 **来源筛选器 `S1–S4` ＋ 0 号指标（`D`/`B`/`C` 三入口收口后）** | `docs/RESEARCH-CONSTITUTION.md` §8.1-AMEND-5 | ⭐ **正确读法**：$$\text{D/B/C 三入口}\xrightarrow{\text{具体计算}}\text{无新结构}\Longrightarrow D_{\rm new}=0$$ ⛔ **不得**推出"RH 没有新攻击点" ✓ ⛔ **纪律**：不得建议 `D`/`B`/`C`-2；"更高 `k`／更大 `N`／更多零点／更多矩阵"**不自动获得研究资格**（＝**换参数**而非换 channel）✓ ⭐ **`S1`** 数学问题**先于 RH**（不谈 RH 也有明确内容：恒等式/组合计数/变换结构/递推/极值）｜**`S2`** **天然连接 RH**（已有非人工接口 `\mathcal P\leftrightarrow\zeta/L/\text{prime/zero}`）｜**`S3`** 第一笔计算**不用旧墙坐标**（输入与一阶段输出均不需 `\beta`/`rank`/`support`/`parity`/`majorant`）｜**`S4`**（最重）异常须**迫使对象**而非仅给常数（强：`Q_{m+1}=F(Q_m)`／`Q_m=0`／`Q_m=R_m\cdot S_m`）⟹ $$\text{计算结果迫使数学对象，而非仅给数值规律}$$ ✓ ⭐ **新增 0 号指标**：$$\text{是否真的产生了新的数学对象？}$$ —— **只有 0 号通过**才有资格查 (1) 在线零点比例 (2) 有限离轴排除 (3) 素数问题 (4) 其它猜想 ✓ ⭐ **状态板**：`D`/`B`/`C`-channel **全 CLOSED**；`D_{\rm new}=0`；**RH target = OPEN**；**discovery channel = WAITING FOR A NEW SOURCE**（`WAITING`≠停摆：**找一个有自身数学生命、又天然连接 RH 的问题，从其第一笔计算开始**）✓ ⭐ **正面意义**：三入口干净关闭**把宽搜索空间实际压缩掉了**；下一轮候选须在**来源**上与 `CAS`/`B`/`C` **明显区别**，⛔ 不能是其**第四种变体** ✓。**状态＝已登记·可用（协议级）** |
| **E-24** | 🆕 **`SOURCE 先验资格 ≠ 候选机制资格` ＋ `S4` anti-post-hoc 四条件（`AMEND-7`）** | `docs/RESEARCH-CONSTITUTION.md` §8.1-AMEND-7｜`docs/SOURCE-CARD-TEMPLATE.md` §2 | ⭐ **原则**：即使 `S1`–`S3` 全过，也**不得**因"看起来可能有用"就进入计算；进入研究轮的**唯一理由**＝$$\text{存在可预先声明的、可判定的 }S4\text{ 对象生成检验}$$ ✓ ⚠️ **`S4` 事后不得修改**：事前声明"若异常可能产生 `F`"，计算后**不得**改写为"我们发现了 `F`" ✓ ⭐ **anti-post-hoc 四条件**：(1) `F` 的形式**非预选拟合数据**；(2) **第二层/第二尺度迫使同一结构**；(3) `F` **非**已有恒等式/Euler–Dirichlet/有限差分缩放/稀疏支持的重命名；(4) `F` **有脱离本实验的定义域** ✓ ⭐ **流程**：`SOURCE CARD → S1–S4/STOP 审核 → 第一笔最小计算 → 结构判定 → {forced object 继续｜numerical pattern only STOP｜CAS/B/C 型 STOP}` ✓ ⭐ **状态**：`D`/`B`/`C`＝discovery channels **CLOSED**；`D_{\rm new}=0`；RH **OPEN**；`JAM` **ARCHIVED**；**`SOURCE` ＝唯一搜索自由度**；**`S4` ＝primary admission gate**；**`STOP` 必须计算前声明** ✓ 【工具层】`\xrightarrow` 转义属**工具执行层错误，不入研究账本**（raw string 修复即可）✓。**状态＝已登记·可用（协议级）** |
| **E-25** | 🆕 **`SOURCE` 候选盘点第 1 轮（4 候选，仅卡片零计算）＋ `AMEND-8` 零号 STOP** | `docs/SOURCE-CANDIDATE-INVENTORY-1.md`｜`docs/RESEARCH-CONSTITUTION.md` §8.1-AMEND-8 | ⭐ **`AMEND-8` 不蕴含式**：$$S1\!-\!S3\not\Rightarrow\text{RUN}$$；须 $$S1\!-\!S3+\mathrm{S4\text{-}PRE}+\mathrm{ANTI\text{-}POST\text{-}HOC}+\mathrm{STOP}\Rightarrow\text{RUN}$$ ✓ ⭐ **三层**：`SOURCE`（搜索对象）→ `OBJECT`（`S4` admission 后才允许）→ `MECHANISM`（更后）⟹ 正确方向 $$\text{SOURCE}\to\text{DATA}\to\text{FORCED OBJECT}\to\text{INTERFACE}\to\text{RH}$$ ✓ ⭐ **零号 STOP**：只写"可能和 RH 有关系"**不够**；须能写出"**若出现 `X` 则被迫引入对象 `F`，且 `F` 的定义域不依赖本实验**"，否则**连计算阶段都不进** ✓ **本轮 4 候选**（各含 `SOURCE`/`S1`/`S2`/`S3`/`S4-PRE`/`STOP`）：① 移位除数和 `\sum d(n)d(n+h)`｜② 最小二次非剩余序列 `n(p)`｜③ 虚二次类数 `h(-d)`｜④ 模形式系数 `\{a_p\}` ✓ **判定**：4/4 通过零号 STOP（均能写出"若 X 则被迫引入 F"）；⚠️ 但按 `AMEND-7`，**先验资格≠机制资格** ⟹ **均尚未获得计算资格**，`COMPUTATION` 仍 **LOCKED** ⟹ 状态＝$$\boxed{\text{NO ADMITTED NEW SOURCE YET}}$$ ✓ 【排除】`CAS`/`B`/`C` 变体；`P1-α` 素数竞赛（既有资产线）；Gauss 和型加性×乘性（`CROSS-0` DEAD）；`JAM` 四卡点（ARCHIVED）✓。**状态＝已登记·可用（候选清单级）** |
| **E-26** | 🆕 **`S4-PRE-EXACT` 统一钉死模板 `\mathcal T_{\rm pin}` ＋ 四卡可采性判定** | `docs/SOURCE-CARDS-S4-PRE-EXACT-completion.md` | ⭐ **模板**：`\mathcal X`＝整数阵列；`F=R_J`＝"阶 ≤ `J_0` 的整系数线性递推算子"；**第一层**在 `X_1` 成立、**第二层**须**同一组系数**在 `X_2` 成立（⛔ 禁止每尺度各拟合 ⟹＝anti-post-hoc (2) 的机械形式）；尺度 `X_1=10^6`／`X_2=10^7` **事前写死**；排除清单 8 项事前列出 ✓ **判定**：卡 1（移位除数和）✓ 可采｜卡 2（最小二次非剩余）✓ 可采｜**卡 3（虚二次类数）✗ 不可采**（属理论 `h=2^{t-1}\cdot`奇部 ＋ 类数公式**预先吸收**，检验在计算前即注定无法迫使**新**对象）｜卡 4（模形式系数）✓ 可采 ✓ **账本**：$$\text{SOURCE cards}=4;\ \text{S4-format}=4;\ \text{S4-exactly}=3;\ \text{COMPUTATION}=\text{LOCKED};\ D_{\rm new}=0$$ ✓ ⭐ **可采 ≠ 已跑**：`COMPUTATION` 仍 LOCKED；建议首跑 **卡 1**（`h\le40`、`X=10^6,10^7`，精确整数阵列）✓。**状态＝已登记·可用（门槛级）** |
| **E-27** | 🆕 **卡 1 `RUN` 前三项补钉（作用坐标／归一化／有限枚举规则）＋ 解释纪律** | `docs/SOURCE-CARDS-S4-PRE-EXACT-completion.md` §4 | ⭐ **① 作用坐标**：$$(R_JX)_h=\sum_{j=0}^{J}c_jX_{h+j},\ c_j\in\mathbb Z,\ J\le4$$ ✓｜**② 双尺度**：$$X^{(1)}_h=\sum_{n\le10^6}d(n)d(n+h),\ X^{(2)}_h=\sum_{n\le10^7}d(n)d(n+h),\ 0\le h\le40$$，要求**同一组** `(c_0..c_J)` 同时使 `R_JX^{(1)}=R_JX^{(2)}=0` ✓ ⭐ **③ 归一化**：首一 `c_J=1` ✓｜**④ 有限枚举规则**：⛔ 非"先找系数族再测试"；✅ 先定 `J\le4, c_j\in\mathbb Z`，再**完整确定**解空间 $$\{c:\begin{pmatrix}H_1\\H_2\end{pmatrix}c=0\}$$，实现＝**精确有理零空间 ＋ 整性检查 ＋ 首一归一**（有限完备，非抽样）✓ ⚠️ **⑤ 解释纪律**：若无 `R_J`，结论**只能**是"**在 `h\le40, X\in\{10^6,10^7\}, J\le4` 的预设实验域内未发现共同低阶整系数递推**"，⛔ 不得写成"除数相关不存在递推结构"，⛔ **更不得因预期负结果提前 CLOSED** ✓；若命中 ⟹ 才触发 `S4`：检查是否被 `\mathfrak S(h)`／已知卷积结构吸收，**只有无法被事前列出的旧结构解释**才进 `FORCED OBJECT` 审核 ✓ **卡 1 状态**：`S1`–`S4-PRE`–`S4-EXACT` 全 ✓（作用方向已补钉）；**`COMPUTATION`=LOCKED**；**`RUN`=尚未授权** ✓。**状态＝已登记·可用（可执行级，待授权）** |
| **E-28** | 🆕 **卡 1 执行层边界错位修正（`h=40,J=4` 需 `X_{44}`）＋ 判定口径改为首一整系数存在性** | `docs/SOURCE-CARDS-S4-PRE-EXACT-completion.md` §5 | ⚠️ **错位**：原写 `(R_JX)_h=\sum_{j=0}^Jc_jX_{h+j}`、`h\le40,J\le4` ⟹ `h=40,J=4` 需 `X_{40..44}`，而数据只到 `0\le h\le40` ⟹ **最后四个方程不存在** ✗ ✓ ✅ **方案 A（采纳）**：保持 `h\le40` 为**方程范围**，**数据扩展**为 $$0\le h\le44$$，对 `h=0..40` 完整构造方程；语义不变＝$$\text{固定 }h\le40\text{ 的 }41\text{ 个目标位置}$$（`h+J` 仅右侧数据）✓ ⭐⭐ **判定口径修正**：报告 $$\exists\,c\in\mathbb Z^{J+1}: Mc=0,\ c_J=1$$ ⛔ **而非**仅 `\dim_{\mathbb Q}\ker M>0`（非零有理零空间**不自动**给出首一整系数递推）；机械化：存在零空间向量 `v` 使 `v_J\neq0` 且 `v/v_J\in\mathbb Z^{J+1}` ⟹ 逐 `J` 报 `\dim\ker`＋是否存在首一整解＋显式 `c` ✓ **卡 1 状态**：`S1`–`S4-EXACT` ✓；execution-boundary **已修正**；**`COMPUTATION`＝LOCKED**；**`RUN`＝NOT YET AUTHORIZED** ✓；授权后 `RUN-1` 冻结范围＝$$X^{(1)},X^{(2)}\to M\to\ker_{\mathbb Q}M\to\text{首一整系数可行性}$$（⛔ 不加 `J`／不加尺度／不扩 `h`／不改 `S4`）✓。**状态＝已登记·可用（可执行级，待授权）** |
| **E-29** | 🆕 **`RUN-1`（卡 1）已执行：预设域内无低阶整系数递推（决定性负结果，无 `FORCED OBJECT`）** | `docs/RUN-1-card1-result.md`｜`scripts/run1_card1_shifted_divisor_recurrence.py`｜`out/run1/run1_raw.txt` | **冻结范围**：`X=10^6,10^7`｜数据 `0\le h\le44`｜方程 `h=0..40`｜`J=1..4`｜两尺度堆叠｜精确整数＋精确有理零空间 ✓ **结果（原始）**：`d(10^7)=64` ✓；`X^{(1)}[0..6]=[421094344,137253454,193727308,170526259,216481178,154136463,240214410]`；`X^{(2)}[0..6]=[6313765566,1827763836,2600743464,2291743963,2922630488,2069617445,3255918570]`；逐 `J`：`rank_{\mathbb Q}(M)=J+1`、`\dim_{\mathbb Q}\ker M=0`（`J=1,2,3,4`）⟹ $$\exists c\ (Mc=0,\ c_J=1)=\textbf{否}$$ ✓ **结论（只允许此句）**：$$\text{在 }h\le40,\ X\in\{10^6,10^7\},\ J\le4\ \text{的预设实验域内，没有发现共同低阶整系数递推}$$ ✓ ⛔ **禁止写法**："除数相关不存在递推结构"／因预期负结果写成"已证无结构" ✓｜**`S4` 未触发**（无 forced object）⟹ 卡 1 在本预设域内**耗尽**，不扩参不留尾巴 ✓ 【量级自查 ✓】`\sum_{n\le x}d(n)^2\sim x(\log x)^3/\pi^2`：`10^6` 预测 `2.7\times10^8` vs 实测 `4.21\times10^8`；`10^7` 预测 `4.2\times10^9` vs 实测 `6.31\times10^9` ✓。**状态＝已封闭（预注册单轮完成）** |
| **E-30** | 🆕 **`RUN-1` 审计收口：干净负结果（无尾巴）；卡 1 `CLOSED — RUN-1 NEGATIVE`；观测≠解释；四指标全不触发** | `docs/RUN-1-card1-result.md` §3／§5／§6／§7 | **核心判定成立**：`rank_{\mathbb Q}M_J=J+1` ⟹ $$\ker_{\mathbb Q}M_J=\{0\}$$（**强于**所要求的 `\exists c, c_J=1`）⟹ `S4` 触发条件全部失败 ⟹ `S4 = NOT TRIGGERED` ✓ ⭐ **无负结果漂移**：未提 `J`／未加第三尺度／未改 `h`／未改 `X`／未换统计量／未找"准递推"／未重定义 `F` ⟹ **无 post-hoc 对象** ✓ ⚠️ **观测 ≠ 解释**：观测＝`\ker_{\mathbb Q}M_J=0`；`\mathfrak S(h)` 乘性**仅作"为何不意外"的解释**，⛔ **不得**反写成"因 `\mathfrak S(h)` 乘性故已证不存在低阶递推" ✓ **四指标**：0 新对象 **否**｜1 在线零点比例 **未触发**｜2 有限离轴排除 **未触发**｜3 其他素数问题 **未形成新接口**（⛔ 不得因"除数和是素数相关对象"就算推进）｜4 其他猜想 **未形成新对象/接口** ⟹ $$\text{prime-problem benefit}=0$$ ✓ **卡 1 终态**：`CLOSED — RUN-1 NEGATIVE`；`S4 NOT TRIGGERED`；`forced object ∅`；`D_{\rm new}=0`；`tail run FORBIDDEN`；`parameter expansion FORBIDDEN`；⚠️ `CLOSED`＝**本卡预设实验的研究闭合**（⛔ 非全称命题）；限定 `h\le40, X\in\{10^6,10^7\}, J\le4` **保留在标题级** ✓ ⭐ **SOURCE-SEARCH 意义**：$$\text{经典算术相关性}+\zeta^2\text{ 接口}+\text{双尺度精确数据}\not\Rightarrow\text{低阶线性动力学对象}$$ ⟹ 下一合法动作＝**换 SOURCE，不换卡 1 参数** ✓ ⭐ **状态**：`D/B/C`=CLOSED；`JAM`=ARCHIVED；`Card 1`=CLOSED；`D_{\rm new}=0`；`RH`=OPEN ✓。**状态＝已封闭（干净负结果，无残留尾巴）** |
| **E-31** | 🆕 **`Card 2` vs `Card 4` SOURCE 级三问比较 ＋ `S4` 判据事前机械化（零计算）** | `docs/CARD2-VS-CARD4-SOURCE-level-comparison.md` | **`Q1`（可强迫性）**：卡 4 **强**（跨形式同系数关系既非 Hecke 也非密度蕴含，低先验判定性强）｜卡 2 **弱**（`n(p)` 取值普遍很小 ⟹ 计数向量高度集中 ⟹ "精确关系"易被 **Chebotarev 密度账本**吸收）✓ **`Q2`（对象域独立性）**：卡 4 **强**（潜在产物＝跨新形式不变量，定义域＝**新形式空间**，既有对象空间）｜卡 2 **弱**（产物为素数集上的统计关系，天然对象域不明显）✓ **`Q3`（RH 接口）**：⚠️ **两者均未超过卡 1**（卡 1 的 `\sum d(n)n^{-s}=\zeta(s)^2` 直连 `\zeta`；卡 2 经 `L(1,\chi_p)`/Siegel 零**条件性邻接**；卡 4 属 **GRH 族**，对 RH 更间接）⟹ **推进理由来自 `Q1`/`Q2`，不是 `Q3`** ✓ ⭐ **判据机械化（计算前写死）**：卡 2＝预固定子族 `p\equiv\pm1\ (4)`／分箱 `K`／双尺度，要求**4 路同系数**命中，且命中的关系 **∉ `\mathcal R_{\rm dens}`**（= 由 Chebotarev 密度恒等式生成的关系子空间，**须计算前算出**）｜卡 4＝预固定 `f,g`／双尺度，要求 4 路同系数，命中 ∉ `\mathcal R_{\rm Hecke}\cup\mathcal R_{\rm sym}` ✓ **建议**：让**卡 4** 进入下一次 `S4-PRE-EXACT` 审核（**不进入计算**）；卡 2 保留但须先解决密度蕴含空间排除 ✓ **状态**：`Card 1`=CLOSED；`Card 2,4`=SOURCE candidates；`Card 3`=CLOSED；`D_{\rm new}=0`；**`COMPUTATION`=LOCKED**（直至下一张卡通过 exact `S4`）；RH target=OPEN ✓。**状态＝已登记·可用（比较级）** |
| **E-32** | 🆕 **卡 4 `S4-PRE-EXACT` 预注册（三钉机械化）：`(f,g)` 事前固定／精确矩阵／`\mathcal R_{\rm old}` 吸收判别式** | `docs/CARD4-S4-PRE-EXACT-preregistration.md` | ⭐ **钉 1**：候选族＝水平 1 新形式权 `k\in\{12,16,18,20,22\}`（唯一归一化 Hecke 特征形式 `\Phi_k`，整数系数 ✓）；**候选对集合 `\mathcal P_{\rm pre}` 含全部 `10` 对**，⛔ 不挑选、**全部必检** ✓ ⭐ **钉 2**：坐标＝**素数下标**；`R_J(x)_h=\sum_{j=0}^{J}c_jx_{h+j}`；尺度 `X_1`＝素数 `\le10^4`（1229）、`X_2`＝素数 `\le2\times10^4`（2262）；方程 `h=0..1220` **两尺度一致**；四块堆叠 $$M=[M^{(f,X_1)};M^{(f,X_2)};M^{(g,X_1)};M^{(g,X_2)}]$$（`(4\times1221)\times(J+1)`）；判定 **与卡 1 逐字同一标准** $$\exists c\in\mathbb Z^{J+1}: Mc=0,\ c_J=1$$，`J\le4` ✓ ⭐ **钉 3（最大风险）**：`\mathcal R_{\rm old}` 机械化＝**逐序列核的并集吸收判别**：命中 `c` 被吸收 ⟺ $$c\in\bigcup_{x\in\mathcal L_{\rm old}}\ker_{\mathbb Q}H_x$$；`\mathcal L_{\rm old}` **事前写死**：Ⅰ 常序列／Ⅱ `h`／Ⅲ `p_h`／Ⅳ `\log p_h`／Ⅴ `\sqrt{p_h}`／Ⅵ `(-1)^h`／Ⅶ 库内其余形式的 `a_p`；**仅当 `c\notin\cup\ker`** 才登记 `FORCED OBJECT` 候选；⛔ 事后**不得增补** `\mathcal L_{\rm old}` ✓ **反事后四条件**（依 `AMEND-7`）：形式非预选／第二尺度同系数／非旧机制重命名（由吸收式机械化）／对象域＝**新形式空间** ✓ **状态**：`SOURCE qualification` ✓；`S4-format` ✓；**`S4-EXACT`=PENDING**（待第三方核可 ✓）；`computation`=**LOCKED**；`Card 1`=CLOSED；`Card 2`=HOLD；`D_{\rm new}=0` ✓；⚠️ **`Q3`「RH 接口更间接」保留在账本**，⛔ 不得包装成更强 ✓。**状态＝已登记·可用（预注册级）** |
| **E-33** | ⚠️ **卡 4 `S4-PRE-EXACT` 修补 A＋B：第二尺度退化（同前缀）＋ `\bigcup\ker` 非解释充分；`RUN` 不授权** | `docs/CARD4-S4-PRE-EXACT-repair-A-B.md` | ⚠️ **缺陷 1（致命）**：`x_h=a_{p_h}(f)` 且两尺度方程范围**都是** `h=0..1220` ⟹ 同一 `p_h` ⟹ $$M^{(f,X_1)}=M^{(f,X_2)}$$ ⟹ 堆叠退化为 `[M_f;M_f;M_g;M_g]` ⟹ **"四路同系数"实际只剩"两形式的同一条素数系数递推"** ✗；⛔ **"第二尺度机械满足"一句撤回** ✓ ✅ **修补 A**：改用两个**互不相交、事前固定**的素数窗口 `W`（`p\le10^4`）与 `W'`（`10^4<p\le2\times10^4`，1033 个素数），事前固定 `H_{\rm row}=600`，取各窗前 605 个素数；四块＝$$[M^{(f,W)};M^{(f,W')};M^{(g,W)};M^{(g,W')}]$$；判定不变 $$\exists c\in\mathbb Z^{J+1}:Mc=0,\ c_J=1$$；⭐ 反事后条件 (2) 改写为"**两个互不相交窗口复现同一结构**"（**语义变更 ⟹ 重新预注册**）✓ ⚠️ **缺陷 2**：`c∈\ker H_x` 只是**相容性必要条件**，非"来源解释" ⟹ $$\text{OLD-ANNIHILATOR}\neq\text{OLD-MECHANISM-EXPLANATION}$$ ✓；✅ **修补 B**：定义**生成关系空间** `\mathcal A_{\rm old}`，判定改 `c∈\mathcal A_{\rm old}?`；⛔ 不得预设 `\mathcal A_{\rm old}=\bigcup\ker` 等价 ✓ ⚠️ **本档纸面主张（待核）**：`\mathcal A_{\rm Hecke}=\mathcal A_{\rm sym}=\mathcal A_{\rm dens/log/sqrt}=\{0\}`（Hecke 为乘法性、自对偶平凡、素数分布为渐近型 ⟹ 不产生精确线性关系）⟹ 若核可则**吸收判别式为空判据**，反事后保护改由"四块高超定判定＋两独立窗口＋全部事前固定"承担；**核相交判别降级为诊断性报告** ✓ **状态**：`SOURCE qualification`✓｜`S4-format`✓｜`(f,g)`✓｜`J\le4`✓｜10 对全检✓｜exact criterion✓｜**真正独立第二尺度＝FAIL/PENDING**｜**`\mathcal R_{\rm old}` 解释充分性＝PENDING**｜**`S4-EXACT`＝NOT YET**｜**`COMPUTATION`＝LOCKED** ✓ ⭐ **准确状态（照录）**：$$	ext{Card 4}=	ext{S4-PRE-EXACT}，发现两个待修逻辑点；RUN 不授权}$$ —— **不是退回卡 4，也不是关闭卡 4**；⚠️ 若不修，其"跨形式×双尺度"检验**退化为纯跨形式共同递推检验**（仍可能是有价值的 SOURCE，但**已非 E-32 声称的那个 `S4`**）✓。**状态＝已登记（待核）** |
| **E-34** | ✅ **`B-EXACT`：`\mathcal A_{\rm old}^{(J\le4,W,W')}=\{0\}` 的形式化证明（三引理＋推论）；A=PASS 已核** | `docs/CARD4-B-EXACT-old-relation-space-is-zero.md` | ⭐ **`\mathcal A_{\rm old}` 正式定义**：Span of "为预注册旧机制**实际生成**"的关系；"生成"＝**由定义恒等式可推导**（⛔ 非"对所有对象为真"）⟹ 排除"核相交即解释"跳步 ✓ ⭐ **引理 1（Hecke＝0，严格）**：自由模型以 `\{a_p\}` 为独立变量，`a_{p^r}=P_r(a_p)` 且 `\deg P_r=r` ⟹ `a_n` 在变量 `a_p` 上的次数恰为 `\nu_p(n)` ⟹ **逐变量次数可复原 `n`** ⟹ `\{a_n\}` **`\mathbb Q`-线性无关** ⟹ 任何 `\sum_jc_ja_{m_j}=0`（`m_j` 互异）在 (M1)(M2) 模型**恒为假、不可推导** ⟹ `\mathcal A_{\rm Hecke}=\{0\}` ✓ ⭐ **引理 2（sym＝0）**：水平 1 ⟹ Fricke 平凡 ⟹ 对偶序列＝原序列；归一化只固定尺度；预注册清单**无**连接两形式的恒等式（已知**同余**如 `\tau(p)\equiv p^{11}+1\ (691)` 是**模 p 陈述**，非 `\mathbb Q`-精确恒等式且不在清单内）⟹ `\mathcal A_{\rm sym}=0` ✓ ⭐ **引理 3（dens/log/sqrt＝0）**：601 连续下标上 `J\le4` 常数系数递推 ⟹ 序列属**线性递推类** `\{\sum_i\lambda_i^hP_i(h)\}`；而 `p_h\sim h\log h`、`\log p_h\sim\log h`、`\sqrt{p_h}` 均**含 `\log` 因子** ⟹ **不属该型** ⟹ 三者贡献 `0`（单块核亦为零）✓ **推论**：$$\mathcal A_{\rm old}=\operatorname{Span}(\mathcal A_{\rm Hecke}\cup\mathcal A_{\rm sym}\cup\mathcal A_{\rm dens/log/sqrt})=\{0\}$$ ⟹ 该域内**吸收空间为空** ⟹ 命中 `c` 自动"非旧机制解释" ⟹ 进入 **`FORCED-OBJECT CANDIDATE`**（⛔ 非 `FORCED OBJECT`）✓ ⭐ **反事后保护的真实来源**＝(i) 四块同系数**高超定精确**判定 (ii) **两互不相交窗口** (iii) **全部事前固定** ✓；⚠️ **边界**：只证"**(M1)–(M5) 生成空间为零**"，⛔ 不证"不存在任何旧机制解释"；`\ker` 相交**仅作诊断** ✓ **状态**：A＝**PASS**（已核）；`\mathcal A_{\rm old}` 定义 **✓ 写死**；`\mathcal A_{\rm old}=\{0\}` 证明 **✓ 给出**；命名 **改为 `FORCED-OBJECT CANDIDATE`**；**`RUN`＝LOCKED**（待核可）✓。**状态＝已登记·可用（待核）** |
| **E-35** | 🔻 **`RUN-2`（卡 4）执行完毕：命中数 0（干净负结果）；`Card 4 = CLOSED — RUN-2 NEGATIVE`** | `docs/RUN-2-card4-result.md`｜`scripts/run2_card4_hecke_common_annihilator.py`｜`out/run2/run2_raw.txt` | **冻结范围**：`Φ_{12},Φ_{16},Φ_{18},Φ_{20},Φ_{22}`；10 对**全检**；`W`＝605 素数（2..4451）、`W'`＝605 素数（10007..15733）**互不相交**；`h=0..600`；`J=1..4`；判定 $$\exists c\in\mathbb Z^{J+1}:Mc=0,\ c_J=1$$ ✓ **结果**：**40 项全部满列秩** `rank_{\mathbb Q}(M)=J+1` ⟹ 连**非零有理解**都不存在 ⟹ **命中数 0** ⟹ `S4` **未触发**、**无 `FORCED-OBJECT CANDIDATE`** ⟹ 依预定**干净关闭、不追尾参数** ✓ ⭐ **管线验证（三次失败被自检拦下，未产出任何结论 ✓✓）**：① `τ` 递推**漏负号**；② 手挑模数**含非素数**；③ **CRT 逆元用错** —— 三次均被断言门终止；**第一次虽打印"命中数 0"但数据无效 ⟹ 已作废、未用于任何结论** ✓✓；通过后 `τ(2..7)` 与已知值完全一致、五形式在 `p=2,3` 均满足 **Hecke 递推** ⟹ 系数确为**真 Hecke 本征值** ✓ **四指标**：0 新对象 **否**｜1／2 未触发｜3／4 未形成新接口 ⟹ $$\text{prime-problem benefit}=0$$ ✓ ⭐ **SOURCE-SEARCH 含义**：$$\text{跨形式同系数}+\text{真 Hecke 特征值}+\text{两互不相交窗口}\not\Rightarrow\text{低阶线性动力学对象}$$ ⟹ 卡 4 不产生 `D_{\rm new}`；卡 2 仍 `HOLD`（密度蕴含空间排除未解决）✓ **状态**：`Card 1`=CLOSED；`Card 2`=HOLD；`Card 3`=CLOSED；`Card 4`=CLOSED（RUN-2 负）；`D_{\rm new}=0`；`COMPUTATION`=LOCKED（无待授权运行）；RH target=OPEN ✓。**状态＝已封闭（干净负结果）** |
| **E-36** | 🏛️ **负筛选对（`RUN-1`/`RUN-2`）＋ 递推通道（域内）耗尽 ＋ 下一张卡硬要求（治理级）** | `docs/SOURCE-SEARCH-negative-screening-pair-and-channel-exhaustion.md` | **证据链闭合**：$$\operatorname{rank}_{\mathbb Q}M=J+1\ (J=1..4)\ \text{对全部 }40\ \text{实例}\Longrightarrow\ker_{\mathbb Q}M=\{0\}\Longrightarrow\not\exists c\in\mathbb Z^{J+1}\setminus\{0\},\ Mc=0$$（**强于**预注册的 `c_J=1`）✓ **三次无效执行严格隔离**：链条＝$$\text{错误实现}\to\text{自检失败}\to\text{结果作废}\to\text{修正}\to\text{sanity checks}\to\text{正式 RUN}$$；独立复核 `\tau(2)=-24`、`a_{p^2}=a_p^2-p^{k-1}`（`p=2,3`）通过 ⟹ E-35 的"0 命中"与三次错误执行**严格隔离**（否则存在**污染风险**）✓ **域限结论**：$$\text{跨形式同系数}+\text{真 Hecke 特征值}+\text{两互不相交窗口}\not\Rightarrow\text{低阶线性动力学对象}$$（⛔ 非"模形式系数不存在任何新结构"）✓ **负筛选对**：Card 1（shifted divisor correlation／双尺度共同低阶递推／无／`S4` 未触发）｜Card 4（cross-form Hecke coefficients／双窗口共同低阶递推／无／`S4` 未触发）⟹ 可安全提炼 $$\text{"共同低阶线性递推"作为 SOURCE}\to\text{OBJECT 通道目前没有产出}$$ ✓ ⭐⭐ **治理结论**：两卡**非同一数学 SOURCE**，但**经同一筛选器** $$\text{SOURCE}\to\text{精确共同递推}\to\text{新对象}$$ 并在 `S4` 前置负分支退出 ⟹ 若下轮仍"换一批序列测共同递推"＝**discovery-channel repetition**（**比单卡关闭更重要**）⟹ **下一张合法卡硬要求**：$$\boxed{\text{改变 SOURCE 的数学来源}+\text{改变 OBJECT 类型}}$$ ✓ **账本**：Card 1＝CLOSED(RUN-1 negative)｜Card 2＝HOLD｜Card 3＝CLOSED｜Card 4＝CLOSED(RUN-2 negative)｜`D_{\rm new}=0`｜**linear-recurrence SOURCE channel = CLOSED/EXHAUSTED within registered cards**（⚠️ 限定＝**已注册的 Card 1+Card 4 通道**，⛔ 非"所有线性递推 SOURCE 数学上排除"）｜`COMPUTATION`＝LOCKED｜RH target＝OPEN ✓ ⛔ **不做** `Card 2` 的 `RUN`（`\mathcal R_{\rm dens}` 未机械化到足以授权计算）；$$\text{不要因两个负结果而降低 Card 2 的 admission 标准}$$ ✓。**状态＝已封闭（治理级）** |
| **E-37** | 🧱 **搜索形状冻结 ＋ 下一张卡 7 问协议 ＋ 四出口起点纪律（治理级）** | `docs/SEARCH-SHAPE-FREEZE-and-NEXT-CARD-PROTOCOL.md`｜`docs/SOURCE-CARD-TEMPLATE.md` §3 | ⭐⭐ **形状冻结**：$$\text{SOURCE}_{\rm new}\not\sim\text{sequence/correlation}\xrightarrow{\text{common low-order recurrence}}\text{OBJECT}$$ ⟹ 下卡**不得只是**"另一种算术序列→共同递推→F"（**即使换新算术来源，仍是同一 discovery channel**）；**下卡至少同时改变两件事**：$$\boxed{\text{SOURCE 的数学生成机制改变}+\text{OBJECT 的数学类型改变}}$$，⛔ 且第二项须**真正跳出线性动力学对象**（**不是**把递推写成矩阵／核／生成函数／差分算子等**改名**）✓ ⭐ **下一轮不 `RUN`**：只做 `SOURCE CARD` ＋ `S4-PRE-EXACT`，须先答 **7 问**：①`SOURCE` 自身是什么独立数学问题 ②要计算的 `Q_1..Q_N` ③被迫出现的 `OBJECT` 类型 ④为何**非**递推/秩/核/支撑/有限差分/Hecke/Chebotarev **换名** ⑤第二尺度/第二层是否仍被迫出现 ⑥是否有**实验域之外**的数学定义 ⑦结果平凡时**立即 `STOP`** 的明确条件 ✓ ⭐ **四出口**（online zero proportion／finite off-axis exclusion／other prime problems／other conjectures）**必须从 `OBJECT` 本身出发**，⛔ 不得计算后再找 RH 联系 ✓ ⭐ **最值得保护的资产**：$$\boxed{\text{不要再寻找"另一个会产生共同递推的 SOURCE"}}$$；`Card 2` **保持 HOLD**，⛔ **不得因 `Card 1`/`Card 4` 均为负结果而反向降低其 `\mathcal R_{\rm dens}` admission 标准** ✓ **账本**：`Card 1`=CLOSED(RUN-1 NEG)｜`Card 2`=HOLD｜`Card 3`=CLOSED(S4 exact absorption)｜`Card 4`=CLOSED(RUN-2 NEG)｜`linear-recurrence SOURCE`=CLOSED/EXHAUSTED（仅已注册 Card 1+4）｜`D_{\rm new}=0`｜`COMPUTATION`=LOCKED｜RH target=OPEN ✓。**状态＝已登记·可用（治理级）** |
| **E-38** | 🧭 **`SOURCE-SEARCH` 治理冻结基线：优先级升级（7 问>S4-PRE-EXACT>RUN）＋ anti-post-hoc 三联锁 ＋ 下一轮只提卡不计算** | `docs/E-38-PRECEDENCE-CHAIN-and-NEXT-ROUND-DISCIPLINE.md` | ⭐ **优先级**：$$\boxed{\text{7问准入}>\text{S4-PRE-EXACT}>\text{RUN}}$$（⛔ 替代旧的"SOURCE 候选→先算→再解释"）✓ ⭐⭐ **anti-post-hoc 三联锁（第 3∧4∧6 问）**：$$\boxed{\text{OBJECT 类型明确}+\text{非旧结构改名}+\text{实验域外定义存在}}$$ —— **只有三者同时成立**，"第二尺度/第二层复现"（第 5 问）**才有意义** ✓ ⭐ **真正开放的空间**：⛔ 非"还有哪些序列可以测"；✅ $$\boxed{\text{哪些独立数学问题能\textbf{自然产生}非线性递推型／非秩型／非核型／非支撑型的\textbf{新对象}？}}$$，且对象**产生后须自然拥有至少一个已有 RH 接口**（⛔ 不得为 RH **人为接线**）✓ ⭐ **下卡合法形状**：$$\text{独立 SOURCE}\to Q_1..Q_N\to\text{强结构异常}\to\underbrace{\text{新 OBJECT}}_{\text{非旧型}}\to\text{已有 RH interface}$$；**`D_{\rm new}` 闸门**：$$D_{\rm new}:0\to1$$ **仅当 `FORCED OBJECT` 真正出现**；此前任何"看起来有意思"的数值规律**只是 `SOURCE candidate`，不得升级成机制** ✓ ⭐⭐ **下一轮纪律**：**只允许提出新 `SOURCE CARD`，⛔ 不允许计算**；须**先过** $$\text{SOURCE change}+\text{OBJECT-type change}$$ **再**逐项答 `E-37` **7 问**；⛔ **任一问答不了 ⟹ 直接 `REJECT`/`HOLD`，不进计算** ✓ **状态**：旧 discovery channel **封存**；`Card 2` **HOLD**；`D_{\rm new}=0`；`COMPUTATION`＝**LOCKED**；RH target＝**OPEN**；⭐⭐ **措辞纪律**：⛔ **未把"目前没有候选"偷换成"数学上没有候选"** ✓。**状态＝已登记·可用（治理冻结基线）** |
| **E-39** | 🔍 **候选 `SOURCE` 扫描 1（六区域，零计算）：0 张合格卡；6／6 均在明确闸门处退出** | `docs/CANDIDATE-SCAN-1-mathematical-content-review.md` | **退出点逐一（照录）**：`A` 极值/变分 → **`SOURCE change`**（与已 CLOSED 的 `W1`/`BC` 极值-对偶线同源）｜`B` 几何/拓扑不变量 → **`OBJECT-type change`**（`\chi`/`\det`/`H` 在 `KH-2` 六死清单；`D-11` 吸收教训）｜`C` Diophantine 解空间 → **`SOURCE change`＋接口不可用**（`V196`–`V198` Brauer/K₂/H¹ 全封；第一断裂 ⟹ 函数域侧无失败对象）｜`D` 加法组合 GAP/Bohr → **`Q-2`/`Q-3`**（强制对象＝**经典 GAP/Bohr**；异常即 **polynomial Freiman–Ruzsa 主流开放**）｜`E` 随机矩阵谱测度 → **RH 接口单向性**（自然接口＝**已封**的 Montgomery–Odlyzko 统计/相关通道）｜`F` 动力系统熵/不变测度 → **RH 接口单向性**（自然接口＝**已封**的 `T7`/显式公式通道）✓ ⭐ **最有信息量**：仅候选 `D` 通过三硬筛（`OBJECT-type change` 真成立＋域外定义真存在），却在 `Q-2/Q-3` 退出 ⟹ **闸门链真正吃紧的一环＝"强制对象是否为新类型"，而非"能否写出 `O`"** ✓ ⚠️ **陷阱显式挡下**：把线性递推改成 `Q_{n+1}=F(Q_n,Q_{n-1})` 或二次/多项式关系，若 `F` 只是对**同一序列**的另一种拟合 ⟹ **同一 discovery channel** ⟹ 直接挡（`OBJECT-type change` 不成立）✓ **账本（不变）**：`D_{\rm new}=0`；`COMPUTATION`＝LOCKED；RH target＝OPEN；**回到 `WAITING`** ✓；⭐⭐ **措辞纪律**：⛔ **不把"扫描失败"解释成"没有新数学"** —— 结论**只**是"在所扫描六区域与该闸门链下，候选均在明确闸门处退出" ✓。**状态＝已封闭（扫描级）** |
| **E-40** | 🔬 **`D`-origin 反向审查（三问）：`Q1`/`Q2`/`Q3` 全 FAIL ⟹ `REJECT`；「加法组合→新对象」入口干净送回 `WAITING`** | `docs/D-ORIGIN-REVERSE-REVIEW-three-questions.md` | **`Q1`（SOURCE 独立性）FAIL**：SOURCE＝"小倍化 ⟹ 强制结构"，其内容＝假设＋结构定理结论 ⟹ **任何受迫对象只是该定理的结论形式** ⟹ SOURCE **与 PFR 通道同源**；换源即离开加性源，不换则只能产出 GAP/Bohr/陪集级数 ✗ **`Q2`（天然非 GAP 对象）FAIL**（逐一排查）：`A+A` 集合✗｜Freiman 同态✗｜大 Fourier 谱 `\Lambda`✗｜加性能量✗｜相消集✗｜**Kneser/Balog–Sands 周期子群 `H`（类型＝子群·定义内在·不依赖 GAP 参数 ✓）但为经典对象**✗｜Ruzsa 距离（准度量 ✓ 经典且是 PFR 工具）✗｜熵型（`KH-2` 六死）✗｜近似群（GAP 推广）✗｜素余数集加性结构 ⟹ Gauss/指数和（`CROSS-0`=`D-12` DEAD）✗ ⟹ **不存在**同时满足"受迫＋非旧类型＋非经典工具"者 ✓ **`Q3`（既有 RH 接口）FAIL**：加性组合通往 `\zeta` 的既有通道唯一形态＝$$\text{加性对象}\to\text{指数和}\to\text{Fourier}\to\text{显式公式/Weil}$$，**该通道已 CLOSED（`T7`）**；⛔ 依您的严格条件，**不得因"可编码进指数和/傅里叶/显式公式"而人为接线** ✓✓ **四出口（从 `O` 本身）**：online zeros ✗｜off-axis ✗｜prime problems ⚠️ 加性组合确对素数问题有真实贡献，但**经由该领域既有机器、未产生本线新对象** ⟹ 不计入本线增量｜non-prime conjectures：PFR 等**已是既有机器** ⟹ 不计入 ✓；⭐⭐ ⛔ **不因第四出口有真实价值就倒装为 RH 入口** ✓ **判定**：$$Q1/Q2/Q3\ \text{全 FAIL}\Longrightarrow REJECT$$；$$
| **E-41** | 🧠 **`META-GAP`：发现坐标系缺失 ＋ `DISCOVERY EXPERIMENT` 协议判定（可定位、**不可从内部闭合**）** | `docs/META-GAP-and-DISCOVERY-EXPERIMENT-PROTOCOL.md` | **三向不对称**：旧入口（大量 CLOSED）｜**负面约束很多**（"不能长什么样"）｜**正向特征缺失**（"应该长什么样"）⟹ 账本给的是**排除集**而非**搜索方向**；7 问第 3 问（要求计算前说出 `OBJECT` 类型）与我们**尚未建立正向类别空间**相冲突 ✓ ⭐⭐ **最重要修正（`A`/`B` 区分）**：`A` 可预注册＝**发现过程必须满足的性质**（SOURCE 独立／数据非人为设计／跨尺度稳定／域外定义／非旧结构重命名／独立数学意义／发现后可查接口）；⛔ `B` **不应**预注册"新机制必须属于 X 型对象"（＝**把未知空间提前压缩成已知语言** ⟹ constrained invention）⟹ **闸门第 3 问纠错**：预注册的是 $$OBJECT\text{ 的"被迫性判据"，不是 }OBJECT\text{ 本身}$$ ✓✓ ⭐ **`DISCOVERY EXPERIMENT` 形状**：$$\text{独立 SOURCE}\to\text{计算}\to\text{让结构自己暴露}\to\text{再定义 OBJECT}$$；三未知量 `(Q,\mathcal R,\mathcal D)`；⛔ **异常 ≠ 新对象**，须 $$\text{异常}+\text{非拟合性}+\text{跨尺度必然性}+\text{域外定义}\Rightarrow OBJECT$$ ✓ ⭐⭐ **内容级判定**：`T1` 跨尺度必然性（结构空间秩·维数在实例族上稳定）＋非拟合性（非预注册低复杂度族的最优拟合）**可机械化**；`T2` **域外定义不可由计算决定**（属领域判断）⟹ 被迫性判据约 **2/3 可机械化**，残余一步正是 post-hoc 风险所在；`T3` 唯一非平凡且不预设对象类型的模板＝**"预注册 nuisance 群 `G` 下的不变量空间"** `O:=\operatorname{Inv}_G(data)`（事前固定 `G,\mathcal I,\mathcal P` ⟹ 天然 anti-post-hoc）；`T4` ⭐ **`META-GAP` 不是逃生口**：`T3` 要求供给**自然**的 `(G,\mathcal I,\mathcal P)`，而"自然的"＝`SOURCE` 独立性 ⟹ $$\boxed{\text{META-GAP 无法从内部闭合，塌回 DISCOVERY SOURCE 缺口}}$$；`T5` 判定＝**可定位、不可内部闭合**（干净负结果）✓ **状态**：⛔ **不把 `META-GAP` 登记成新机制**；⛔ 不再找第 7／第 8 个候选；回到 `D_{\rm new}=0`／`COMPUTATION`=LOCKED／RH target=OPEN／`WAITING` ⟹ $$\boxed{\text{我们不是把所有路都走完了；而是把"寻找路的方法"也走到了边界}}$$（**≠ RH 无路可走**）✓。**状态＝已登记（状态级）** |
| **E-42** | 🌱 **`ZF` 母问题（有限离轴零点）缺口审计：`ZF-2` OPEN 且未被既有封锁覆盖（弱目标定理通道开放）** | `docs/ZF-MOTHER-PROBLEM-existing-theory-gap-audit.md` | **定位**：`N_off(T)=O(1)` **严格弱于 RH**（RH ⟹ 0 ⟹ 有限）；属**定量阶数问题**（`T^{1-c} -> O(1)`），**非找新 invariant** ⟹ **可绕开 `E-41` 的 `META-GAP`**；⚠️ 本线**不在冻结范围**（非 bridge-search、非 SOURCE-search）；**`LH` 分栏**：`LH` 不能推出有限离轴零点（仅 `Backlund` 型 `N(1/2+e;T,T+1)=o(log T)`）✓ **`ZF-0`（等价性）＝PENDING**：须先核"有限性是否 ⟺ RH"（`Speiser`／`BN`（`Lambda<=0` 且 `Lambda>=0` 已证）/`Li` 型等价警示 ⟹ 若等价则落入 `RH-EQUIVALENT-TOO-STRONG`，本线中止）✓ **`ZF-1`（density ⟹ `O(1)`）＝GAP**：障碍＝**近 `1/2` 区无一致幂次节省**（固定 `sigma` 的逐点 `T^{c(sigma)}` 在 `sigma->1/2` 无效；`N(sigma_0,T)=O(1)` 只排除固定距离者，**不能**排除越来越贴近 `1/2` 者）✓ ⭐⭐ **`ZF-2`（proportion＋inertia ⟹ 有限）＝OPEN**：本仓已有 `E-11`（不定型→惯性→秩→计数）＋交换率 `N_0^s/N >= 2-R(psi)`（100% ⟺ `R<=1` ⟺ support>1）＋终点退化（`n_-(Q_T)` 恰好计数离轴对，100% ⟺ `n_-=0` ⟺ Weil 正性 ⟺ RH）—— ⭐ **这些封锁针对"100%/比例"，而有限性严格弱于 100%** ⟹ $$\boxed{\text{既有封锁（}W6\text{/support}>1\text{、}\beta\text{-盲、终点退化）不自动封锁 }ZF}$$；可用结构：`n_-(Q_T)` 单调不减且 `N_off(T)=O(1) <=> sup_T n_-(Q_T)<∞` ⟹ 目标＝**惯性负指标的有界性论证**（⚠️ 非更强比例界）✓ **`ZF-3`（有限+受控分解）＝GAP**：`Hadamard` 分解 ⟹ 有限离轴 ⟺ `xi=`（有限因子）×（全实零点函数），但**纯增长/解析结构不足以界定计数**（order 1）⟹ **须算术输入**（与**第一断裂**/`S6` 同源）✓ **下一步建议**：① **`ZF-0` 文献级等价性核查**（前置门）② **`ZF-2` 单点深审**（把比例界换成惯性负指标的有界性论证）✓。**状态＝已登记·可用** |
| **E-43** | ⭐⭐⭐ **`ZF-0` 修正 ＋ `ZF-2` 升级为 OPEN（独立母问题）；增量负惯性→有限总质量加性上泛函；`LH` 降级** | `docs/ZF-MOTHER-PROBLEM-existing-theory-gap-audit.md` §6–§10 | **`ZF-0` 修正**：`Speiser` 是**零个**的等价；弱化成"`zeta'` 只有有限个左半侧零点"**不能**得 RH；`Li`/`BN` 是 RH 的精确等价 ⟹ 不能推 `finite off-axis <=> RH`；⚠️ `MathOverflow` 问"If RH fails, must it fail infinitely often?"**该问题本身开放** ⟹ "RH false ⟹ `N_off -> inf`" **不是已知定理** ⟹ $$\boxed{N_{\rm off}(\infty)<\infty\ \text{确实是真正弱于 RH 的独立目标}}$$；`ZF-0` 仍 PENDING 但**不得预设等价 RH** ✓ ⭐⭐⭐ **`ZF-2` 升级**：逻辑彻底分开 —— RH＝`n_-(Q_T)=0`（**零性问题**）vs 有限离轴＝`sup_T n_-(Q_T)<∞`（**统一有界性问题**）；`2/3` 比例墙只回答 `n_-/N -> 0`，而 `o(N(T))` **不蕴含** `O(1)`（甚至 `n_- ~ log log T` 满足前者而彻底失败后者）⟹ `W6`/support>1、`beta`-盲、终点退化、`2/3` 墙**都不能仅凭"封的是 100%"推出 ZF 已死** ⟹ **`ZF-2`＝OPEN ⭐⭐⭐** ✓ ⭐ **严格化**：只问 $$\boxed{\text{Can one prove }\sup_T n_-(Q_T)<\infty?}$$（**负惯性预算** `n_-(Q_T)<=B_0+B_1+...`，RHS **与 T 无关**）✓ ⭐⭐ **第一刀＝增量负惯性 ＋ 本档规范化**：窗口 `Q_[T_1,T_2]=Q_{T_2}-Q_{T_1}`，研究 `Delta n_-`；⛔ 目标**不是** `Delta n_-<=c<1`（**退化为比例估计**）；✅ 需 `sum_j Delta n_-(I_j)<=C` ⟹ **规范化＝寻找非负加性上泛函 `F`**：(i) `F(I)>=Delta n_-(I)`、(ii) 划分加性、(iii) `sup` 有限 ⟹ `sum Delta n_- <= sup F < inf`；**审计目标＝E-11 的 `Q_T` 是否允许这样的"有限总质量"泛函**；**失败模式＝唯一可用泛函是比例的（`propto N(T)`）⟹ 立即 CLOSED、不跑参数** ✓；⚠️ 须先核**惯性对算子和不加性** ⟹ 窗口量是否真等于窗口内离轴计数（E-11 恒等式能否局部化）✓ ⭐ **discovery-channel 判定**：ZF-2 思路**不是**提高比例／更强 majorant／`beta`-敏感量／新 spectral invariant ⟹ **未明显落入 `E-41` 旧墙** ✓ **`ZF-3` 旁支（⚠️ 档级）**：`Ki`（Proc. LMS 2005）对 **Epstein zeta 近似**证"除有限多个外零点简单且在临界线上"；`Gonek`（arXiv:0704.3448 有限 Euler 积）亦有同类结构 —— ⚠️ 对象**不是 `zeta` 本身**（正是**第一断裂**接缝）⟹ ⛔ 绝不能直接转移 ✓ **`LH` 降级为次级母问题**：`Backlund` ⟺ `LH` `<=>` `N(1/2+eps;T,T+1)=o(log T)`；ZF 要 `sum` 所有窗口有限；`o(log T)` 不蕴含可和 ⟹ $$\boxed{ZF-2>LH}$$（非因更近 RH，而因与**惯性—计数资产有精确量级接口**）✓ **状态**：`ZF-0` PENDING（不得预设等价）｜`ZF-1` GAP｜**`ZF-2` OPEN ⭐⭐⭐**｜`ZF-3` GAP｜`LH` 次级｜新 RH mechanism **继续冻结**｜**`ZF` computation 尚未授权** ✓；**下一刀＝`ZF-2` 单点深审**（不再扫文献）✓。**状态＝已登记·可用** |
| **E-44** | ❌ **`ZF-2` 第一刀（`Z1`–`Z4`）：该具体路线 CLOSED —— E-11 惯性结构「可计数但无有限总质量」** | `docs/ZF-2-first-cut-Z1-Z4-audit.md` | **前置（照录唐先生）**：先审**局部化**而非先找 `F`；⛔ **不要把「算子差的负惯性」当窗口负惯性**（$$n_-(A-B)\ne n_-(A)-n_-(B)$$，PSD 亦无简单解释 ⟹ 会凭不加性造**假窗口机制**）；⭐ 正确简化：$$\Delta n_-(T_1,T_2):=n_-(Q_{T_2})-n_-(Q_{T_1})$$，全局恒等式若严格则**立即**得窗口计数 ⟹ 算子差表述**删除** ✓ **`Z1`＝CONDITIONAL**：档案 `V186 §3` 为「恰好计数离轴对 **up to small trace-norm tail**」⟹ **不是无残项严格等式**；对有限性需 `tail(T)=O(1)`（**未证**）；对**比例**结论残项在相应范数下可控（档案已用）✓ **`Z2`＝PASS**：`n_-(Q_T)` **单调不减** ⟹ `Delta n_- >= 0` 且对划分**自动可加**（望远镜）⟹ 定义合法 ✓ **`Z3`＝FAIL（核心）**：取 `F:=Delta n_-` 只是**定义、非资源**；E-11 对 `n_-(Q_T)` 的**唯一原生上界**来自 **rank–trace／惯性不等式**，而 `tr Q_T`／`rank Q_T` **随压缩规模（约 `N(T)`）扩展性增长** ⟹ 机器原生只给**比例型控制** `n_-(Q_T) <= C N(T)` ⟹ **不存在可被现有结构界定的、具有限总质量的加性上泛函** ✓ ★ **挡下的伪突破**：`Delta n_-(I) <= C mu(I)` 且 `mu([0,T])->inf` **只是局部密度控制，不是 finite defect**；真需有限测度 `mu((0,inf))<inf` ✓ **`Z4`＝FAIL（依 `Z3` 立即触发判据）**：$$\boxed{ZF\text{-}2\ \text{CLOSED}：\text{现有 }Q_T\text{ 只提供 extensivity，而没有 finite-budget structure}}$$；⛔ **无第五步「寻找新 invariant」** ✓ ⭐⭐ **干净结论**：$$\boxed{\text{E-11 的惯性结构具有可计数性，但没有有限总质量；因此它不能把零点比例信息升级为有限离轴零点}}$$ ✓ ⭐⭐ **范围限制**：本 CLOSED **只封「E-11 惯性 → 有限预算」这一具体路线**，⛔ **不是**「`ZF` 不可能」；`ZF` **母问题仍 OPEN**（`ZF-1` GAP／`ZF-3` GAP）✓。**状态＝已封闭（具体路线）** |
| **E-45** | ❌ **`ZF-3` 最小算术输入审计：快速 CLOSED；`ZF` 缺口图成形（density GAP ＋ inertia CLOSED ＋ arithmetic-input GAP）** | `docs/ZF-3-minimal-arithmetic-input-audit.md`｜`docs/ZF-2-first-cut-Z1-Z4-audit.md` §7 | **免费改写（新增）**：$$ZF\iff\exists T_0:\ \text{所有 }|\gamma|>T_0\ \text{的零点都在临界线上}$$（解析性 ⟹ 有界区域零点有限）✓；⭐ **`ZF-0` 免费逻辑推论**：「有限 ⟹ RH」与「¬RH ⟹ 无限」**互为逆否** ⟹ 既然 MO 上后者**开放** ⟹ 前者**也不是已知定理**（=未被证明，非已被否证）✓ **输入类型过滤**：(1) zero-density ⟹ 只给比例 ⟹ FAIL｜(2) explicit formula/正性/Weil ⟹ 等价级、经惯性即 `E-11` ⟹ FAIL（`E-44` 已封）｜(3) 增长/order/Hadamard ⟹ `sum 1/|rho|^2 < inf` 不界定个数 ⟹ FAIL｜(4) 无零点区 ⟹ 管 `sigma` 近 1 ⟹ FAIL｜(5) 函数方程/自对偶 ⟹ 只给对称、属定义式 ⟹ FAIL｜(6) 乘法性/Euler 积 ⟹ 本仓已证**算术无内生动力学**（`D1=0`）＋**第一断裂** ⟹ FAIL（**此即缺口本身**）｜(7) 「有限有效数据」型压缩 ⟹ 已在封存族（`V294-A` 有限阶聚合 `G(K)<=0`；`V290`/`O1-1` 有限纤维分离）⟹ FAIL｜(8) ⚠️ 唯一未立即落入清单者＝**导数型判据的 finite-defect 弱化**（如 `zeta'` 在 `sigma<1/2` 只有有限个零点），但同族于 `Speiser` ⟹ 依判据归入 `RH-equivalent criterion` ⟹ CLOSED（⚠️ **待核指针**，不作为 survivor）✓ ⭐ **结构性发现**：已知 finite-defect 定理（`Ki` Epstein zeta **近似**；`Gonek` **有限** Euler 积）都活在**算术描述有限**的对象上；`zeta` 的 Euler 积是**无限**的 ⟹ 需要「无限 Euler 积 →（计数层面）→ 有限有效数据」的算术约束，而该类型已封 ⟹ `ZF-3` 快速 CLOSED；诚实措辞＝「**在所列输入类型族内未出现真正不同的离散算术约束类型**」（⛔ 非「不存在」）✓ ⭐⭐ **缺口图**：$$\boxed{ZF=\underbrace{\text{density GAP}}_{ZF\text{-}1}+\underbrace{\text{inertia CLOSED}}_{ZF\text{-}2}+\underbrace{\text{arithmetic-input GAP}}_{ZF\text{-}3}}$$；`ZF` **母问题仍 OPEN**（`ZF-0` PENDING）✓ **`E-44` §7 防重开条款**：$$n_-(Q_T)=N_{\rm off}(T)+\mathcal E(T)$$，档案仅有 trace-norm tail 控制 ⟹ **E-11 尚无无条件严格 finite-defect 计数器**；但**修复 `Z1` 不能救活 `ZF-2` 的 finite-budget 路线**（`Z3` 已证 rank–trace 机器只有 `O(N(T))` 型资源）⟹ ⛔ **不要重开 `E-11`** ✓。**状态＝已封闭** |
| **E-46** | 🅿️ **`ZF` 第一轮正式收口：困难收缩为「如何制造有限有效算术约束」；内部候选生成冻结；等独立问题** | `docs/ZF-3-minimal-arithmetic-input-audit.md` §5 | ⭐⭐ **核心收口**：$$\boxed{\text{ZF 的困难已从「如何计数」收缩为「如何制造有限有效算术约束」}}$$；⛔ 不再拆 `ZF-1`/`ZF-2`/`ZF-3`（三机器角色已清楚：density 只到 `o(N),T^{1-c}` 到不了 `O(1)`；inertia 可计数但只有 extensive budget；Hadamard/growth 解析上容许无限离轴、缺算术约束）⟹ 内部做变体**收益极低** ✓ ⭐ **`ZF-0` 逻辑核验**：令 `A=`RH、`B=`离轴有限 ⟹ `B⟹A` 的逆否即 `not A ⟹ not B`（即 ⟹离轴无限）⟹ **逻辑正确**；⚠️ **但仍保留 PENDING 直到一手文献核验**（`MathOverflow` 的「问题开放」是**强线索、非最终文献证明**）✓ ⭐⭐ **措辞纪律**：保留观察 $$finite\text{-}defect\ examples\leftrightarrow arithmetically\ finite\ objects$$，但 ⛔ **只是现象性关联、还不是机制**；⛔ **不能写**「无限 Euler product ⟹ 不能 finite-defect」；✅ **只能写**「目前找到的 finite-defect 类比对象 ⟹ 其算术描述具有有限性」，而 `zeta` **恰好缺少这一点** ⟹ 正合纪律：**gap 可定位，但不能把 gap 写成 impossibility theorem** ✓✓ ⭐ **暂停位置**：$$\text{FINITE OFF-AXIS}\Downarrow\text{eventual RH above some }T_0$$（真弱于 RH，**又不是简单 RH-equivalent criterion**）；已审机器一律 `density/inertia/growth` **都不给** `O(1)` ✓ ⛔ **不启 `ZF-4`**；⭐ 回到原则 $$\text{独立问题}>adjacent\ asset>\text{RH relevance}$$ ⟹ `ZF` **作为开放母问题留档，但不围着它继续造输入类型**；未来若启动须是 $$\text{独立数学问题}\to\text{先产生可证明新定理}\to\text{再查是否触及 }ZF/RH$$ ✓ ⭐⭐ **当前最健康状态**：$$\boxed{\text{ZF OPEN，但冻结其内部候选生成；RH SOURCE-SEARCH 仍冻结；等待独立问题}}$$ ⟹ 避开循环 `GAP → 新符号 → 新 invariant → 计算 → 旧结构 → CLOSED` ✓。**状态＝已封闭（第一轮）·母问题留档 OPEN** |
| **E-47** | ⭐⭐ **阶段锚点 ＋ `D_new` 彻底分离：`D_RH-discovery = 0` vs `D_independent problem` 完全开放；下一轮从独立问题母题启动** | `docs/ZF-3-minimal-arithmetic-input-audit.md` §6 | **状态箱**：$$\boxed{\text{ZF OPEN}\land\text{ZF-internal search FROZEN}\land\text{RH SOURCE-SEARCH FROZEN}}$$（分层：`ZF-1`/`ZF-2`/`ZF-3` CLOSED（本轮内部变体）｜`ZF-0` **PENDING**（只欠一手文献核验，**不应凭 MO 定案**）｜`ZF` 母问题 **OPEN**｜`ZF` 内部 candidate generation **FROZEN**｜RH SOURCE-SEARCH **FROZEN**）✓ ⭐ **背书修正**：✅「finite-defect examples ⟹ **目前已找到的例子具有算术有限性**」，⛔ **而非**「infinite Euler product ⟹ finite-defect impossible」（**越过证据允许范围**）✓ ⭐ **缺口分解**：$$\underbrace{\text{counting}}_{\text{已有}}+\underbrace{\text{analytic control}}_{\text{已有但不够}}+\boxed{\text{finite effective arithmetic constraint}}_{\text{缺失}}$$ ⟹ ZF **不缺新计数器**，缺的是**独立来源的算术有限性定理**（产生 `#{\rho:\Re\rho\ne1/2, |\Im\rho|<=T} <= C`，`C` **不随 T 增长**），与 `o(N(T))` **性质完全不同** ✓ ⭐ **搜索方向**：$$\boxed{\text{Independent Problem}\to\text{Theorem}\to\text{Spillover}\to ZF/RH}$$，⛔ 而非 `ZF → 找工具 → 新 invariant → CLOSED` ⟹ **下一轮研究对象不必以 RH 为名字出现** ✓ ⭐ **五条准入判据**：(1) 自身是有明确数学命题的问题；(2) **不需假设 RH** 才有意义；(3) 有**一轮内可证/可证伪**的具体子命题；(4) **首轮成功即产生独立数学价值**；(5) **只有定理产生后**才检查是否给出 finite defect／zero exclusion／prime consequence／other conjecture 之一 ⟹ 即使最终与 RH 无关，研究也不是废品 ✓ ⭐⭐ **关键分离**：$$\boxed{D_{\rm RH\text{-}discovery}=0}\quad\text{而}\quad\boxed{D_{\rm independent\ problem}\ \text{完全开放}}}$$ —— 两者**彻底分离**（`D_new=0` **不再意味着没有新数学可做**）✓ ⛔ **指令**：`E-46` ＝**当前阶段稳定锚点**；⛔ 不再加 `ZF-4/5/6`；**下次启动直接从「独立问题母题」开始，而非从 `ZF` 的 gap 开始** ✓。**状态＝已登记·锚点** |
boxed{\text{"加法组合}\to\text{新对象"入口：干净送回 }WAITING\text{（无参数尾巴）}}$$；账本不变（`D_{\rm new}=0`；`COMPUTATION`=LOCKED；RH target=OPEN）✓。**状态＝已封闭（审查级）** |


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
| C-91 | ⭐ **本会话收束台账（C-61–C-90）＋项目级四级地图** | `docs/C91-session-consolidation-ledger-C61-C90-project-level-map.md`（2026-09-18）| 结构＝**墙 → 叶子 → 技术族 → 剩余缺口**。①主图：`W6`＝**原子墙** → `{UQRL, D10(a), W8(b)}` → （`UQRL` 四族已关 ／ `D10(a)` 新对象未发现 ／ `W8(b)` 收敛到 `V199` 三源）。②`UQRL` 四族关闭表：`Burnol`＝α 参数失配；`FINT`＝α＋β；`large sieve`＝β（`L²`）；`decoupling`＝A＋B（对象／曲率）。③**B 门精确限定语**（不得写成"decoupling 原则不可能"）＝"在当前候选转换及当前曲率模型下，所需的非退化曲率条件没有得到满足；现有实测的二阶差分符号混合及 gap 跳变不能支持所需的标准曲率估计"。④两个 `≠` 升级：`UQRL` 开放 ≠ 不可解；四族已知工具关闭 ≠ 所有可能机制不存在。⑤**禁止重开条件（硬过滤器）**：`UQRL` 重开必须出现新对象或新机制；逐条禁止再换 exponential-sum theorem／再换 `L^p`／再写成 Dirichlet polynomial／再换 Fourier·Hilbert 表示／再把平均估计包装成 uniform estimate。⑥叶子性质四分：`W6` 原子墙／`UQRL` 定量墙／`D10(a)` 对象墙（候选数 0）／`W8(b)` 结构源墙。⑦含本会话勘误与引用完整性台账（`Burnol` 门⑤ 引用 ⚠️ 待核；`C-77` 漏提交已补；花括号 7 处已修）。**性质＝过程性/负面判据类（D 类自用资产），非突破级** ✓ | |


---

# 📌 【2026-09-18 定点更新 · 收束台账 `C-91`】项目级四级地图（墙 → 叶子 → 技术族 → 剩余缺口）

> 依据：唐先生 2026-09-18 13:41「直接开 (A)」；台账正本＝`docs/C91-session-consolidation-ledger-C61-C90-project-level-map.md` ✓

$$\text{主图}：\boxed{W6=\textbf{原子墙}}\ \longrightarrow\ \boxed{\{UQRL,\ D10(a),\ W8(b)\}}\ \longrightarrow\ \begin{cases}UQRL & \textbf{四族已关}\\ D10(a) & \textbf{新对象未发现}\\ W8(b) & \textbf{收敛到}\ V199\ \text{三源（逐源待核）}\end{cases}$$

## 一、四级结构（本会话固化）

| 级 | 对象 | 内容 |
|:--|:--|:--|
| ① 墙 | `W6` | **原子墙**（无条件三阶矩 at `X≍T` ≡ prime-pair ≡ support>1；不可再分）|
| ② 叶子 | `UQRL` / `D10(a)` / `W8(b)` | 定量墙 / 对象墙 / 结构源墙 |
| ③ 技术族 | `UQRL` 下 4 族 | `Burnol`／`FINT`／`large sieve`（＋频率正则性）／`decoupling` |
| ④ 剩余缺口 | 三者 | `UQRL` 命题开放（已知技术族穷尽）；`D10(a)` 候选数 0；`W8(b)` 逐源核验未做 |

## 二、`UQRL` 四族关闭表

| 技术族 | 关闭原因 |
|:--|:--|
| `Burnol` | **α 参数失配**（`λ→0` vs `n≲T₀²`；`C-88`）|
| `FINT` | **α＋β**（频率＝`log n`；定量内容＝框架／范数等价 `L²` 型；`C-89`）|
| `large sieve`（＋频率正则性）| **β**（天然 `L²`／平均；`C-89`）|
| `decoupling` | **A＋B：对象／曲率**（`C-90`）|

$$\textbf{B 门精确限定语（不得写成"decoupling 原则不可能"）}：\text{在}\ \textbf{当前候选转换及当前曲率模型}\ \text{下，所需的}\ \textbf{非退化曲率条件没有得到满足};\ \text{现有实测的二阶差分符号混合及 gap 跳变}\ \textbf{不能支持}\ \text{所需的标准曲率估计}✓$$

## 三、两个 `≠` 升级（必须保留）

$$UQRL\ \textbf{开放}\ \ne\ UQRL\ \textbf{不可解};\qquad \text{四族}\ \textbf{已知工具关闭}\ \ne\ \textbf{所有可能机制不存在}✓$$

## 四、禁止重开条件（硬过滤器）

$$UQRL\ \text{重新开案}：\boxed{\text{必须出现}\ \textbf{新的对象} \text{或}\ \textbf{新的机制}};\qquad \text{以下}\ \textbf{不构成} \text{理由}：$$
$$\qquad (1)\ \text{再换 exponential-sum theorem};\ (2)\ \text{再换}\ L^p;\ (3)\ \text{再写成 Dirichlet polynomial};\ (4)\ \text{再换 Fourier／Hilbert 表示};\ (5)\ \text{再把平均估计包装成 uniform estimate}✓$$

## 五、叶子性质区分（不可混类）

$$W6：\textbf{原子墙}（\text{结构承重点，非普通候选路线}）;\qquad UQRL：\textbf{定量墙}（\sup_{n\lesssim T_0^2}|E(n,T_0)|\to0）$$
$$D10(a)：\textbf{对象墙}（\text{须找}\ \text{`C-68` 四件套＋`ARS1`–`ARS6`}\ \text{要求的新对象};\ \#\{\text{候选}\}=0;\ \textbf{不得}\ \text{与"技术族失败"混为一类}）$$
$$W8(b)：\textbf{结构源墙}（\text{已收敛到}\ V199\ \text{三源};\ \text{下一步＝逐源最后核验，}\textbf{不是}\ \text{重新展开}\ W8\ \text{文献空间}）✓$$

*（本节为指针段，正本见 `C-91`；本文件其余内容不变 ✓）*

| C-92 | ⭐ **三叶子逐项审计 ＋ 核验深度四级 ＋ 残余风险清单** | `docs/C92-item-by-item-audit-three-leaves-verification-depth-and-residual-risk-list.md`（2026-09-18）| 逐项审计 3 叶子共 17 项，按**核验深度**分四级（A 逐字／B 定理级／C 推导型／D 推理·类比型）。关键：`W8(b)` 三源中 (b) 实根性/PF = **定理级但仅对该族**（`V191`），`V199` §3(b) 的族外推广是**推理型** ⟹ `R1`；(c) 耗散/熵 = **推理型**，只排除"需指数增长"者 ⟹ `R2`。`UQRL` 四族：2 逐字／1 推导／1 实测＋类比。`D10(a)`：7 项未实例化、候选数 0。**残余风险清单 `R1`–`R5`**（推理型关闭中尚未保守化者，含降调建议）。待办 `U1`–`U6`。 | |
| C-93 | ⭐ **`R1`：`𝓕_V191` 族外 PF/Newton 机制审计（bounded-family）＋对象级二分** | `docs/C93-R1-FV191-outside-family-audit-object-level-dichotomy.md`（2026-09-18）| `𝓕_V191` 精确边界：对象＝Ξ 的 Jensen 多项式 `J_γ^{d,n}`、公理＝双曲性；`Pólya 1927` RH ⟺ 全族双曲；`GORZ 2019` 覆盖 `n≥N(d)` 与 `1≤d≤8`；剩余区 `R` 上一致陈述 ≡ RH（只用 Pólya＋GORZ）⟹ `V191-①`=NO（定理级）。按对象枚举 6 族外候选：①乘子序列 ②Toeplitz 全正 ③变差递减核 ⟹ **经典等价 ⟹ 坍缩（`R1-B`）**；④Laguerre–Pólya 类 ⟹ 定义式；⑤序数测度 Hankel 矩 ⟹ `β`-盲；⑥Turán ⟹ 强度不足（`R1-C`）。`R1-A`=0、`R1-B`=3、`R1-C`=3、`R1-D` 适用。⭐**对象级二分**：Ξ-系数侧 ⟹ 坍缩（强度＝RH）；γ-序数侧 ⟹ `β`-盲 ⟹ 与项目既有"两面"结构**同址**。**不声称**族外空间已排除。 | |
| C-94 | ⭐ **`U1`–`U6` 证据链一次性清理 ＋ 硬规则「外部命中 ≠ 外部独立证明」** | `docs/C94-U1-U6-evidence-chain-cleanup.md`（2026-09-18，148 行）| `U1` `Burnol` 门⑤ 引语：外部检索（含摘要）**未核到逐字原句** ⟹ 降为 `[转述／待核]`（**不是**判定其命题为假）。`U2` Planat／MDPI（`Mathematics` 14(11):1884, 2026）：**definition-level normalization defect**（`M_n=∫Φ₁u^{2n}du` 少一个随 `n` 变化的 `n!` 因子 ⟹ 对象与 GORZ 不一致；`d=2` 的 `Δ<0` 与 GORZ `d≤8` **定义层冲突**）⟹ 三条结构性结论 **EXCLUDED**；S-channel **CLOSED 依据 `V191`**（非 Planat）；`HAL` Prop.9＝**corroboration candidate, independence unverified**。`U3` `1.28π` **算术自检通过**。`U4` vdC 常数 **待核但不承重**。`U5` 8/23 第二环：保留原档案事实 ＋ 结论加"**输入不可达**"限定（**不改写历史记录**）。`U6` **承重引用协议**＋优先复核清单。⭐硬规则：**「外部命中」≠「外部独立证明」**。 | |
| C-95 | ⭐ **`R2`：非双曲耗散机制审计（bounded-family）＋ 同根发现** | `docs/C95-R2-nonhyperbolic-dissipative-audit-same-root-as-R1.md`（2026-09-18）| 操作定义：耗散／熵／单调性且**不要求指数轨道增长**。⚠️ **核心项已被档案预注册关闭**：`p11-zero-flow-lyapunov.md` 第一轮判词逐字"Sobolev 耗散**不含 β**（无害）——'含 β 的耗散'**两难**（Φ 侧不含——零点侧循环）"。按对象枚举 8 候选：①DBN 热流（`CLOSED-ROUTES-MAP:228` 闭环为循环）②Sobolev/entropy/Fisher 耗散泛函 ③流上单调性 ④Mayer/Gauss 转移算子（`det=ζ`，但 `V239-D`：`Re s=1/2` 是 **Selberg 世界**）⑤抛物/非超曲内禀流（`L2` 否决）⑥⑦⑧ 残余（非一致双曲谱隙／曲率·熵凸／多项式轨道增长热力学）。`R2-A`=0、`R2-B`=2、`R2-C`=6、`R2-D` 适用。⭐**同根发现**：`R1` 二分 ≡ `R2` 两难 ⟹ **同一"两面"二分** ⟹ `C-92` 的"唯二合法入口"**实为同一结构**，均已 bounded-family 实质关闭。 | |


---

# 📌 【2026-09-18 14:01 定点更新 · `C-92`／`C-93`／`C-94`／`C-95`】`R1`、`R2` 双审计 ＋ 证据链清理

> 本段为**指针段**，正本见各档（`docs/C92-…`／`C93-…`／`C94-…`／`C95-…`）✓

## 一、`R1`（`C-93`）：`𝓕_V191` 族外 PF/Newton 机制 —— **bounded-family audit**

$$\text{`𝓕_V191` 精确边界（逐字）}：\text{对象}＝\Xi\ \text{的}\ \textbf{Jensen 多项式}\ J_\gamma^{d,n};\ \text{公理}＝\textbf{双曲性};\ \text{参数区}＝(d,n)✓$$
$$\text{Pólya 1927}：\text{RH}\iff\text{全族双曲};\quad \text{GORZ 2019}：n\ge N(d)\ \text{与}\ 1\le d\le8\ \text{无条件};\quad \mathcal R=\{d\ge9\}\times\{n\ \text{小}\}\ \Longrightarrow\ \mathcal R\ \text{上一致陈述}\equiv\text{RH}✓$$

| # | 对象 | 判定 |
|:--:|:--|:--|
| ① | 系数序列作乘子算子 | **坍缩（`R1-B`，经典等价）** |
| ② | Toeplitz `(γ_{k-l})` 全正 | **坍缩（`R1-B`，同链）** |
| ③ | 变差递减核 | **坍缩（`R1-B`，VD ⟺ TP）** |
| ④ | `Ξ ∈ Laguerre–Pólya` 类 | **门②失败（定义式＝RH）** |
| ⑤ | 序数测度 `μ_γ` 的 Hankel 矩 | **`β`-盲（门①②）** |
| ⑥ | Turán 不等式 | **强度不足（真实但弱于全族双曲）** |

$$R1\text{-A}=0;\quad R1\text{-B}=3;\quad R1\text{-C}=3;\quad R1\text{-D}=\textbf{适用}\ \Longrightarrow\ \text{降调为}\ \boxed{\text{bounded-family audit}}✓$$
$$\qquad ⭐\ \textbf{对象级二分（核心产出）}：\text{Ξ-系数侧} \Longrightarrow \textbf{坍缩（强度＝RH）};\qquad \gamma\text{-序数侧} \Longrightarrow \textbf{`β`-盲}✓✓$$

## 二、`R2`（`C-95`）：非双曲耗散机制 —— **bounded-family audit**

$$\textbf{操作定义}：\text{对象}＝\text{算术／动力学对象};\ \text{公理}＝\textbf{耗散／熵／单调性}\ \text{且}\ \textbf{不要求指数轨道增长};\ \text{结论}\supseteq\text{零点实部约束}✓$$
$$\textbf{档案预注册关闭（关键）}：\text{`p11-zero-flow-lyapunov.md` 第一轮判词逐字}：\text{"Sobolev 耗散}\ \textbf{不含}\ \beta\ \text{（无害）——}\textbf{"含}\ \beta\ \text{的耗散"}\ \textbf{两难}\（\Phi\ \text{侧不含——零点侧循环）}\text{"}✓✓$$

| # | 对象 | 判定 |
|:--:|:--|:--|
| ① | DBN 热流 | **`R2-C`**（`CLOSED-ROUTES-MAP:228`：形变型**闭环为循环**，`RH ⟺ Λ≤0`）|
| ② | Sobolev／entropy／Fisher 耗散泛函 | **`R2-C`**（`p11` 两难：Φ 侧不含 `β`）|
| ③ | 流上单调性（P11 框架 C）| **`R2-B/C`**（第一轮收口）|
| ④ | Mayer／Gauss 转移算子（`det = ζ`）| **`R2-C`**（`V239-D`：`Re s=1/2` 是 **Selberg 世界**；`V219`：同一个 `1/2` ≠ 同一个零点机制）|
| ⑤ | 抛物／非超曲内禀流 | **`R2-B`**（`L2` 否决判据：`Spec ℤ` 无内禀流）|
| ⑥⑦⑧ | 残余（非一致双曲谱隙／曲率·熵凸／多项式轨道增长热力学）| **`R2-C`**（统计型无谱正性／需算术凸性／动力学 ζ 非亚纯）|

$$R2\text{-A}=0;\quad R2\text{-B}=2;\quad R2\text{-C}=6;\quad R2\text{-D}=\textbf{适用}✓$$
$$\qquad ⭐\ \textbf{同根发现（核心产出）}：\text{`R1` 二分}\ \equiv\ \text{`R2` 两难} \Longrightarrow \textbf{同一"两面"二分};\ \text{`C-92` 的"唯二合法入口"}\ \textbf{实为同一结构}✓✓$$

## 三、`U1`–`U6` 证据链清理（`C-94`）

| 项 | 处置 |
|:--|:--|
| `U1` `Burnol` 门⑤ 引语 | **降为 [转述／待核]**（外部检索未核到逐字原句）；⚠️ **不是**判定其命题为假 |
| `U2` Planat／MDPI | **definition-level normalization defect** ⟹ 三条结构性结论 **EXCLUDED**；S-channel **CLOSED 依据 `V191`**（非 Planat）|
| `U3` `1.28π` | **算术自检通过**：`π(1+(6/5)^{1/2})^{1/3} = 1.2795π ≈ 4.0196` |
| `U4` `PAPERA` vdC 常数 | **待核但不承重**（`C-90` 依据＝定号假设实测失效）|
| `U5` 8/23 第二环 | 保留原档案事实 ＋ 给**结论**加"**输入不可达**"限定（**不改写历史记录**）|
| `U6` 转述风险面 | **承重引用协议**：承重必须逐字＋出处可查；非承重可转述但须标注 |

$$\textbf{硬规则（本档起适用）}：\boxed{\text{"\textbf{外部命中}"}\ \ne\ \text{"\textbf{外部独立证明}"}} \Longrightarrow\ \text{`HAL` Prop.9 与 Michalowski／Toeplitz}\ \textbf{均维持 pending verification}✓✓$$

## 四、叶子现状（收缩）

$$\boxed{W6\ \textbf{原子墙}\ +\ \begin{cases}UQRL & \textbf{四族已关}\\ D10(a) & \textbf{0 候选}\\ W8(b) & \textbf{`R1`、`R2` 已实质关闭}\end{cases}} \Longrightarrow\ \text{剩余可动}\：\ W6\ +\ UQRL\ +\ D10(a)✓$$

*（本节为指针段；本文件其余内容不变 ✓）*
---

## 【定点更新·`NEG-REGISTER-1`】类级负面判定的统一定级 ＋ 引用纪律（2026-09-18 20:13）

$$\text{触发}：\text{唐先生 20:03"}\text{类似}\ \text{`V248`}\ \text{这样的大类严格负面判定还有几个？一一严格写出来"}✓$$
$$\text{产出}：\text{`NEG-REGISTER-1-class-level-negative-verdicts-18-entries-and-six-types.md`}\ \text{（18 条，六型定级）}✓$$
$$\text{六型}：\text{T-I 干净小结果／T-II 逻辑必然／T-III 框架性重述（前提承重）／T-IV 分类穷尽性／T-V 诊断性判据／T-VI 方法特定封闭}✓$$

| # | 判定 | 型 |
|:--:|:--|:--:|
| 1 | `V248` 锥分离（判别锥必自对偶 ⟹ 回角 I）| **T-III** |
| 2 | `V191` Jensen–Pólya 强度 | **T-II** |
| 3 | `V193`§④／`V192`§③ 谱实现族二分封闭 | **T-VI** |
| 4 | `V188` 线性通道饱和 ＋ 四通道穷尽 | **T-IV** |
| 5 | `POS1`／`POS2` 正性完全二分／类级封口 | **T-V** |
| 6 | `V215` 三型全封 | **T-IV** |
| 7 | `V211` 有限→无限八类全落已封类 | **T-IV** |
| 8 | `V157` C6.6 内生零谱对应严格三分 | **T-IV** |
| **9** | **`V227`-A `sup Re z` 不是模不变量** | **T-I ✓** |
| 10 | `V226`／`V226`-A 算术复定位两型（已撤回）| **T-IV** |
| 11 | `V247` 第三型公理两刀 | **T-III？待核** |
| **12** | **`V253` Erdős 和界（`\sigma=1` 被尾和有限性强制）** | **T-I ✓** |
| 13 | `V254` 典范带符号阈值 ＝ `\beta_*` | **T-III** |
| 14 | `V255`／`V255-5b` parity barrier 型不匹配 | **T-V** |
| 15 | `V259` 有限局部不能判定离轴 | **T-V** |
| 16 | `W1` 刚性缺口（检测 ≠ 排除）| **T-V** |
| 17 | `FZ-1` 46 NO-GO ⟹ 6 母机制 ＋ 6 筛子 | **T-IV** |
| 18 | `FZ-3` canonical ⟹ `\beta` 盲／信息承载 ⟹ 循环 | **T-V** |

$$\text{分布}：N_{\rm T\text{-}I}=2\ |\ N_{\rm T\text{-}II}=1\ |\ N_{\rm T\text{-}III}=3\ |\ N_{\rm T\text{-}IV}=5\ |\ N_{\rm T\text{-}V}=5\ |\ N_{\rm T\text{-}VI}=2✓$$
$$\Longrightarrow \boxed{\text{18 条中}\textbf{干净小结果仅 2 条}（\#9\ \text{`V227`-A}，\#12\ \text{`V253`}）;\ \textbf{其余 16 条} \text{为条件性／分类性／诊断性}}✓✓$$
$$\textbf{⭐ 引用纪律（即刻生效）}：\text{引用上述任一条}\ \textbf{必须随引其型}✓✓$$
```
"V188 饱和(T-IV)"  ✗ 不得写成 "线性通道已穷尽"
"W1(T-V)"          ✗ 不得写成 "检测不可能排除"
"V248(T-III)"      ✗ 不得写成 "判别必回到正性"（须写明前提 P1–P3）
"V191(T-II)"       ✗ 不得写成 "定理级"
```
$$\text{根因}：\text{这 18 条中被当作}\ \textbf{无条件结论}\ \text{使用过的比例很高} \Longrightarrow \text{这正是"每轮都撞同一堵墙"的机制的一半}✓✓$$
$$\qquad \text{不是墙在重复，而是}\ \textbf{引用时把条件性结论升格成了无条件结论}✓$$
$$\text{已就近加型标注}：\text{`V248`（T-III）／`V191`（T-II）／`V188`（T-IV）／`AUDIT-WALLS-AND-DIFFICULTIES-20260917`（W1，T-V）}✓$$
$$\textbf{登记（资产）}：\text{`NEG-REGISTER-1`}\ \text{＝}\ \textbf{负结果语料的型化登记}（18 条 ＋ 六型 ＋ 引用纪律）✓$$
$$\qquad \text{价值}：\text{防止}\ \textbf{条件性结论被无条件引用} \text{—— 属}\ \text{`D-1`–`D-10` 型过程资产}✓✓$$
$$\qquad \text{关联改动}：\text{`V248`／`V191`／`V188`／`AUDIT-WALLS-AND-DIFFICULTIES-20260917` 四处已加【型标注】}✓$$



$$\text{⚠️ 分布勘误（`NEG-REGISTER-2` §4）}：\text{上表／上行的型分布}\ \textbf{算错};\ \text{正确（18 条表内）}＝T_{\rm IV}=6,\ T_{\rm VI}=1✓✓$$
$$\qquad \text{有效（移出 }\#10\ \text{`V226`，已撤回）}＝\mathbf{17}\ \text{条}：T\text{-I}=2,\ T\text{-II}=1,\ T\text{-III}=3,\ T\text{-IV}=5,\ T\text{-V}=5,\ T\text{-VI}=1✓✓$$
$$\qquad \text{口径}：\text{今后引用本表以}\ \textbf{17 条有效版本} \text{为准}✓$$

---

## 【定点更新·C-110–C-129 ＋ CREATE-SPEC-1～12 ＋ NEG-REGISTER-1～4】冻结期后的**规格级**收束（2026-09-18 22:3x）

$$\textbf{背景}：\text{唐先生 22:32「先 b」} \Longrightarrow \textbf{把 12＋ 份档案固化入主图}（\text{此前仅存于文件}）✓$$

### §1 本轮净结构（一句话）

$$\text{本轮}\ \textbf{未新增路线}，\ \text{但把"为什么各路线都死"从}\ \textbf{四次孤立见证} \text{升级为}\ \textbf{一份四条款规格 ＋ 三张候选表 ＋ 五条已证引理}✓✓$$

### §2 ⭐ 四条款规格（"被机制认可的对象"须同时满足）

$$\textbf{(i)}\ \text{算术的（非坐标）};\quad \textbf{(ii)}\ \text{无欧拉积仍可定义};\quad \textbf{(iii)}\ \text{极限恢复零结构（钉点）};\quad \textbf{(iv$'$)}\ \textbf{变形须移动对象自身的零点}✓✓$$
$$\qquad ⚠️\ \textbf{(iv) 的原表述（"作用于有零点的因子"）已被更正}：\text{欧拉积的局部因子}\ \textbf{本身零-free};\ \text{ζ 的零点}\ \textbf{涌现}（`V227` §5）✓$$
$$\textbf{张力三角}：\text{系数侧} \Longrightarrow \textbf{不能移零点}（\text{引理 L1}）;\ \ s\text{-空间} \Longrightarrow \textbf{坐标};\ \text{保乘性} \Longrightarrow \textbf{欧拉积回归}✓✓$$
$$\textbf{逐点通道三分}：\text{b1}\ F\ \text{乘性}\Rightarrow\text{欧拉积}; \quad \text{b2}\ \text{作用 ζ 自身系数}\Rightarrow\text{平凡}; \quad \text{b3}\ F\ \text{非乘性＋派生序列}\Rightarrow\textbf{唯一活口}✓✓$$

### §3 候选总表（各死于不同门／不同条款）

| 候选 | 内容 | 死在哪 |
|:--|:--|:--|
| **A** | 部分欧拉积 $\prod_{p\le y}$ | 门 1 `TESTABLE-1`（需局部因子，DH 无） |
| **B** | DBN 热流 $H_t$ | `F2`（坐标操作）＋ `F5`（$\Lambda\le0$ ⟺ RH）＋ 端点 ½ 阶分支 |
| **C** | 级数截断 $\sum_{n\le N}$ | `F3`（部分和零点不收敛） |
| **D** | 导子／$\Gamma$ 因子变形 | `F3`——**带证明**：$\Gamma$ 零-free ⟹ 保零集变换 |
| **E** | Dirichlet 卷积变形 | **＝ACPC 线 ＋ 乘性卷积线，两条已判死** |
| **M1** | 素数限制系数（$P(s)$） | 延拓必经 $\log\zeta$ ⟹ 值面 |
| **M2** | 除子卷积 | 引理 L1 所辖（只"借入"零点） |
| **M3** | 平滑／平均 | 截断类（需无界精度） |
| **M4** | $\Lambda$／极值型 | `F5` ＋ 端点；**唯一 F5 可满足者，其墙改为"上限 $c_\infty>0$"** |
| **M5** | ACPC 的 $C=A\cdot M$（系数侧 Hadamard 积） | ⚠️ **原"实验判死"已撤回**（探针 $\sigma=1/2$ 落在收敛半平面外，横标实测 $=2$）；改判 **结构性死**：求和集饱和（`CREATE-SPEC-10`) |

### §3A ⭐ **新增资产登记（本会话）**

| # | 资产 | 位置 | 性质 |
|:--|:--|:--|:--|
| **L1** | 整因子乘法不移零点 | `CREATE-SPEC-4` §2 | **已证（初等）** |
| **L2** | 常数系数逐点操作平凡 | `CREATE-SPEC-8` §2 | **已证（初等）** |
| **L3** | $F$ 乘性 ⟹ 乘性保持 | `CREATE-SPEC-8` §3 | **已证（初等）** |
| **T1** | 横标引理 | `CREATE-SPEC-11` §1 | **已证（初等）** |
| **T2** | $k$ 重部分和 $\sim X^k/k!$ | `CREATE-SPEC-11` §2 | **已证（PNT 归纳）** |
| **D-F3** | 完成化变形保零集 | `CREATE-SPEC-2` §2 | **已证（初等）** |
| **规格** | 四条款 (i)–(iv$'$) ＋ 张力三角 ＋ b1/b2/b3 | `CREATE-SPEC-1～8` | **规格（非定理）** |
| **字典** | 位置↔求和（Dirichlet 乘／加性卷积） | `CREATE-SPEC-10` §2 | 结构原理（Barnes 核待核） |
| **饱和** | 求和集饱和（$k\beta_*\le k$ 恒饱和） | `CREATE-SPEC-10` §3 | 结构论证（非定理） |
| **注记** | `zero-free-factor-lemma` / `cone-criteria-selfduality` | `papers/` | 说明性（**不得当成果引**） |
| **过滤器** | `TESTABLE-1` 前提／元问题卡 | `FILTER-TESTABLE-1` / `META-1` | 筛选门槛（非结果） |

### §4 本会话**已证**引理／定理（五条，均为初等且完整）

$$\textbf{L1}：\text{若}\ g\ \text{整，则}\ Z(fg)=Z(f)\cup Z(g) \Longrightarrow \textbf{乘性／完成化变形不移零点}✓✓$$
$$\textbf{L2}：a_n\equiv c \Longrightarrow \sum F(a_n)n^{-s}=F(c)\zeta(s) \Longrightarrow \textbf{作用 ζ 自身系数是平凡的}✓✓$$
$$\textbf{L3}：F(xy)=F(x)F(y)\ \text{＋}\ a_n\ \text{乘性} \Longrightarrow F(a_n)\ \text{乘性} \Longrightarrow \textbf{欧拉积回归}✓✓$$
$$\textbf{T1（横标引理）}：a_n\ge0,\ \sum_{n\le X}a_n\sim cX^k \Longrightarrow \sigma_c=k✓✓$$
$$\textbf{T2（}k\ \text{重部分和）}：\sum_{n\le X}A_k(n)\sim X^k/k! \Longrightarrow \sigma_c(A_k)=k✓✓$$
$$\qquad \textbf{另有}：\text{候选 D 的}\ F3\ \text{死（}\Gamma\ \text{零-free）亦为证明级}✓✓$$

### §5 **同址收敛清单**（本会话共 **10 次**）

$$\text{C-61 §2C（第四类不变量）／C-64-65（簿记→`SUPPORT-1`）／C-69（识别侧接口）／C-70／C-71（三入口定死）／C-72（第三通道→`SUPPORT-1`）／C-82（值 vs 界）／C-83（带号加权＝`V254` 类）／C-90（对象转换 III）／C-107（自由概率＝`V247/V248`）／CREATE-SPEC-2（完成化盲）／CREATE-SPEC-11（聚合→PNT 幂次节省）}✓✓$$

### §6 仍**未判死**的两处（活口，非候选）

$$\text{(甲)}\ \text{ACPC 的}\ L_1（\text{单闭环量}）\ \text{——原档自述"未判"，但仅"单块和"}✓$$
$$\text{(乙)}\ \textbf{b3 全类为空}（\text{"聚合保持定理"}）\ \text{——} \textbf{尚未证明};\ \text{其形态已缩为}：\text{"任何点逐＋加性卷积生成的序列，其 DS 零点信息必为聚合型或不存在"}✓✓$$
$$\qquad \Longrightarrow ⚠️\ \text{"聚合保持"}\ \textbf{已归约到经典障碍}（\text{PNT 幂次节省＝固定零-free 区}） \Longrightarrow \text{其地位＝经典开放问题，}\ \textbf{非新障碍}✓✓$$

### §7 两份独立小注记的状态（**不得误引**）

$$\text{`papers/cone-criteria-selfduality/note.md`}：\textbf{已停}（\text{定理初等 ＋ Lemma 2 属 folklore ＋ §6 前提 (P2) 可能 RH 强度}）⟹ \text{内部记录}✓$$
$$\text{`papers/zero-free-factor-lemma/note.md`}：\textbf{说明性}（\text{引理 folklore；文献检索已确认无具名来源}）;\ \text{已附可引文献缺口}（\text{Tao：反向"常数}\Rightarrow\text{零-free 区"可设想但未尝试，惟其自评"极低效"}）✓✓$$

### §8 引用纪律（新增两条，与 `NEG-REGISTER-1` 的"随引其型"并列）

$$\text{(1)}\ \textbf{成分级引用}：\text{混合档须引到成分}（\text{如"}\text{`V253`（T-I：恒等式／T-V：§5）}\text{"}）✓$$
$$\text{(2)}\ \textbf{四条款引法}：\text{今后任何"新对象／新变形"提案，须先声明}\ \textbf{如何通过 (i)–(iv$'$) 四条}，\ \text{并注明死于哪一条}✓✓$$
$$\qquad ⚠️\ \textbf{归纳不得获得否决权}（\text{`C-116`}）：\text{`F1`–`F8` ＋ 检验床为}\ \textbf{唯一前置门};\ \textbf{警示清单} \text{（如同址收敛 N 次、零实例）}\ \textbf{无否决权}✓✓$$

### 【定点更新·补充】C-96～C-109 ＋ CREATE-SPEC-12（**前段遗漏，本档补齐**）

$$\text{核查发现}：\text{`C-97`／`C-98`／`C-109`}\ \text{与}\ \text{`CREATE-SPEC-12`}\ \textbf{此前未入图} \Longrightarrow \text{本段补齐}✓$$

$$\textbf{(一) 经验线（M-窗口记忆／零点相关）}：$$
$$\qquad \text{`C-97`}：\text{素数间隙记忆（}N=2\times10^7\text{）——}\textbf{硬记忆＝可容许性（}\mathfrak S=0\ \text{精确对上）};\ \text{残类反重复（LS 2016，}\textbf{首次登记}）;\ \text{间隙负自相关}\ r_1=-0.0356（40\sigma）✓$$
$$\qquad \text{`C-98`}：\text{零点侧}\ r_1=-0.34889（493\sigma）;\ \text{配对相关合 GUE};\ \textbf{数方差平坦}\ 0.33\text{–}0.43（\text{有限范围饱和，}\textbf{措辞已降级}）✓$$
$$\qquad \text{`C-99`～`C-102`}：\text{support>1 对偶残差探针——}\textbf{三窗稳定性 ＋ 合成 GUE 对照（自校准）};\ \text{结论：}\textbf{1 是可稳定恢复的对偶带宽边界，未观察到可用的}\ >1\ \text{结构}✓$$
$$\qquad \text{`C-117`～`C-121`}：\text{M-窗口 ——}\textbf{纯跨度律}（\text{斜率}\to-1/\log x）;\ \textbf{非两体}（\text{链式归约被拒：}\chi^2/df\ 109.6\to855.3）;\ \text{标度律＝路线边界资产（未扩展）}✓✓$$

$$\textbf{(二) 机制提取线}：\text{`C-104`（五原语 vs `FZ-2`／`FZ-3`，无逃逸）／`C-105`（`M1-RH` 五门：Gate C ✓、Gate E ✓、Gate A ✗ ⟹ 有界类 DEAD）／`C-106`（`M2`＋赋值提升交叉，双半皆有关键点）／`C-107`（`FZ-2` 未测项 T1–T3 全 ✗，吸收目标精确化到 `V247`／`V248`）／`C-108`（三论文细节 D1–D7，6/7 已有）／`C-109`（七技术 S1–S7：3 在用／3 已覆／**1 新槽 S1**＝沿形变的算术 Poincaré 型不等式，落 DBN 循环线）}✓✓$$

$$\textbf{(三) `CREATE-SPEC-12`（突破口）}：\text{门槛 (a)–(d)}\ \text{＋}\ \textbf{五候选全败}（\text{B1/B2 循环};\ \text{B3 过强};\ \text{B4 边界定理不可变形};\ \text{B5 正项恒等式自动满足}）;\ \text{新增：}\textbf{四重对称} \Longrightarrow \text{离轴计数}\in4\mathbb Z \Longrightarrow \text{门槛放宽为}\ \le3✓✓$$
$$\qquad \Longrightarrow \textbf{突破口对象仍未被占据};\ \text{log-free 排除路线对已知机制仍封闭（}\text{`C-126` 的"渐近零例"细化到对象级}）✓✓$$

$$\textbf{(四) 纪律重申}：\text{以上各条}\ \textbf{不得} \text{去条件化引用};\ \text{`C-116`：归纳无否决权}✓$$

---

## 【定点更新·C-121–C-126】（2026-09-18 23:31，唐先生：「正式中止 B2-1，并把 §五 三条净产出登记进主图」）

**■ B2-1 状态 = `SUSPENDED / NEW-MATH-REQUIRED`（不是 DEAD）**

措辞关键区别（唐先生逐字）：**不是证明单构型不可能，而是证明【现有 envelope ＋ 当前可导出的 R-信息不足以关闭单构型】；要继续，必须引入【新的成对几何数学对象】。**

**■ 已关闭的子路（六条）**

| # | 子路 | 处置 |
|---|---|---|
| (i) | `|D(δ)| ≥ 128 ⇒ δ ∈ ℤ` | 错误，正式撤回 |
| (ii) | 更小 τ ⇒ 整数化 | 已定量否证（C-124 §4：间隙界真空，10^-650 ≪ τ） |
| (iii) | R1：255 个观测值给 R ≤ 191 | 做不到（无信息论约束） |
| (iv) | R2：Hankel／递推表示给 R 上界 | 做不到（需 R ≤ 191 ＋ 精确性，后者已废） |
| (v) | R3：正性给方向正确的界 | 只能给 R ≥ 128，**方向与所需上界相反** |
| (vi) | 继续收紧 envelope（B／M／box） | C-121-A 实测：无新的有效自由度 |

**■ 三条资产（登记）**

```
A1  R = #supp(μ*μ̃) = Hankel-rank(E_{j+k})
    —— 把 marks pairwise geometry 【代数化】

A2  R ≥ P ≥ 128
    —— 仅由 m_i ∈ {1,2}, Σ m_i = 256 的【整数结构】得到严格下界

A3  【条件性】若二阶能量中的交叉项不发生抵消，
    则存在 |δ| ≲ 8.8×10^-20 的近碰撞
    —— 比一阶和法则的 0.6034 收紧约 18 个数量级
    ⚠️ A3 必须明确标记 conditional，不得进入「定理资产」栏
```

**■ 主图结论：G3 当前真正缺口**

```
G3 缺口 ≠ envelope 精度
        ≠ PSD
        ≠ Toeplitz
        ≠ 更多 rows
        ≠ R 的简单计数
        ↓
  而是：【带相消控制的成对几何定理】

     "低秩／有限 pairwise complexity
      + ε-接近线性序列
      + 正系数单位圆指数和
      ⇒ 频率聚簇／几何刚性？"

  且已知：单靠「ε 极小」不能完成这个桥。
```

**■ 审计链（本轮干净结果）**

```
现有 envelope → PSD repackaging → mixture candidate
   → near-collision → R／Hankel → 【pairwise-cancellation wall】
（档：C-122 → C-123 → C-125 → C-124）
```

**■ 禁令**

- 禁止从当前 LP／envelope 继续迭代；
- `bounded implementation DEAD ≠ principle impossible`；
- 未用 RH；未改前沿档案；未覆盖其 JSON。

---

## 【定点更新·C-132／C-133】（2026-09-19 11:35）

**■ F3 攻击结果（C-132）**：F3 作为**不带额外假设**的一般命题**为假** —— 显式反例＝**窗口隐形测度**（ℤ/N 上均匀测度，窗口内 û≡0）；加 t·u 后窗口幅频偏差 ≈5×10⁻¹²（浮点噪声），而秩 47→256。缺的假设＝**整数性 ＋ 固定总量**（"minimal counterexample"形式）。

**■ 预检（C-133）**：**隐形能力 ⟺ 核维数 > 1 ⟺ W < N/2**；满窗口 W=255 ⟹ 核维数 = 1（恰为常数）⟹ **隐形技巧与约束空间互斥**（唯一隐形方向＝均匀平移，必然违反 marks∈{1,2} 与 Σm=256）。⟹ "用隐形技巧构造 p<p₀ 构型"（丙）**预检即死**。

**■ 反例引擎的跨线识别**：完整周期/幂等测度 ⟹ **KILL-2（素数直积因子化，`:1092`）** 同一物。

**■ 新分级登记**：该反例登记为 **T-I（干净小结果）**，与 `V227-A`／`V253` 并列（依 `NEG-REGISTER` 分级标准）。

**■ 四条线汇合于同一物**：`B2-1` 缺口 ＝ `C-131` F3 ＝ `C-125` pairwise geometry ＝ `C-132` 修正后真靶子（固定总量＋整数质量＋窗口幅频 ⟹ 秩有界？）。

---

## 【定点更新·C-135】（2026-09-19 11:40）**定位修正**

**■ F3 的机制＝经典**：唐先生核实 (iii) ⟹ 我们的"窗口隐形测度"**就是**有限创新率（FRI）／湮灭滤波器框架里**采样算子的零空间**（`dim ker = |Λ₁:Λ₀| ≡ N−2W`）。谱系：**Prony 1795 → 湮灭滤波器 → FRI 采样理论**（Vetterli–Marziliano–Blu, IEEE TSP **50**(6):1417–1428, 2002；Blu et al., IEEE SPM **25**(2):31–40, 2008）。

**■ 表述纪律（三条，即刻生效）**：①**禁止**主张"新隐形机制"；②引用**先 FRI 族谱、后我方应用**；③新颖性只能主张：**四要素框架 + 三例并列 + 与整数质量约束的对接方式**。

**■ 新增滤镜**：**零空间滤镜**（触发词：隐形方向／零空间／歧义核／不可见扰动／dim ker）⟹ **先查 FRI／Prony／湮灭滤波器族**；命中即标"经典机制的实例"。

**■ 分级修正**：`V227-A`＝**T-I(n)**（新机制）；`V253`＝**T-I(n)**；F3＝**T-I(c)**（经典机制）。

---

## 【定点更新·C-136／C-137】（2026-09-19 11:50）

**■ C-136（甲：FRI／超分辨率假设审计）**：文献假设三条（分离 `Δ≥2λ_c`／尖峰数 `≤n/4`／数据须为**复**样本含相位）。⭐ 承重注记（逐字）：**"There is no separation requirement if all $d_i$ are positive"** ⟹ **正性可替代分离**；Moitra '15：`Δ<λ_c` ⟹ 无估计量可区分（Rayleigh 极限对**复振幅**根本）。对质：我方**正性 ✓✓**（marks∈{1,2}>0，$w_c\ge0$）、数据**仅模长** ⟹ **判定：分离不是绑定缺口，相位是**。
**■ 更正**：`C-132` §5／`C-133` 的"缺失＝分离下界"**作废**；反例与核维数判据**不变**。
**■ C-137（甲2：support ≤ 1 内相位能否定秩）**：**NO，失败在【数据类型层】**。ζ 侧相位**只**出现在显式公式，而显式公式是**恒等式** ⟹ 逐字（`d7-boundary-audit`）："恒等通道只产生等式（自适应）——不产生不等式" ⟹ 相位**无法产生排除**。
**■ 缺口重写**：不是"相位是否存在"，而是**"能否把相位信息用于产生不等式"** ⟹ 与 `C-82`（值 vs 界）／F5／`V188` §2 **同址**。
**■ 统一读数**：两设定数据**都是模长型**；替代品 toy＝**整数性＋固定总量**（`C-133`），ζ＝**暂无**（需 support>1／`W6`）。

---

## 【定点更新·C-141】今日净产出卡（2026-09-19）

**■ 今日 12 档（`git log --since` 实测）**：线 A 形状检验（`C-130`／`C-131`）｜线 B F3 攻击（`C-132` 反例／`C-133` 预检＋T-I 登记／`C-135` 定位修正＝FRI 零空间）｜线 C 甲系列双条件审计（`C-136` FRI 假设／`C-137` 数据类型层／`C-138` 窗口完备性／`C-139` 共轭饱和／`C-140` 双条件归一）｜线 D 档案完整性（`C-134` 原理＋三 T-I 共同结构／C121–C128 重号勘误）。

**■ 净产出 9 项**：⭐ **T-I(c) 反例**（F3 假；窗口隐形测度；秩 47→256）｜既有 T-I(n)（`V227-A`／`V253`）｜**三条判据／滤镜**（核维数判据／可准入核 vs 实核维数／零空间滤镜）｜**两条原理**（局部隐形无意义／双条件归一）｜**一处精确定量**（共轭饱和 `W≥N/2`）｜**一条定位修正**（分离被正性替代；缺口＝相位）｜**一条正面机制定位**（相位→不等式＝`Z(t)` 符号＋整数性，且不付精度尺度）｜三次自我更正｜档案完整性（重号勘误＋编号硬规则）。

**■ ⭐ 单一汇合点**：`一致有限性界 ≡ support>1 ≡ W6 ≡ C-126 SUSPENDED ≡ C-128／C-129`。

**■ ⚠️ 未立档三问（复述型）**：ζ 的 `s` 归纳／素数间隙→RH／可迭代下降量 —— 均为档案既有判词的复述，无新内容。

## 【定点更新·C-231：资产 T13-Damped-M3 FROZEN】（2026-09-20）

| 资产 | 内容 | 位置 | 状态 |
|---|---|---|---|
| T13-Damped-M3（冻结） | 阻尼 M=3 常数的精确认定：C_3 = F(z_*) = 0.3730918928958164...，argmin_Omega = {z_*, sigma z_*} | `papers/damped-M3-theorem/main.tex` ＋ `main.pdf` ＋ `note.md` | FROZEN |
| 证书脚本组 | dB_krawczyk_11.py / dB5_local_growth_5d.py / dC2iv_strict.py / dC2par_parallel_iv.py | `scripts/` | 可复现 |
| 决策链文书 | C-224 → C-226 → C-227 → C-228 → C-229 → C-230 → C-231 | `docs/` | 已登记 |

- 定位：**自用数学资产**（非论文级突破；唐先生 2026-09-16 双轨定位之 (ii) 类）
- 价值：定理链完整、依赖 DAG 无循环、证书双层互验、边界与 caveat 如实
- 维护规则：仅数学错误才改动；改动须 append 勘误指针

【定点更新·C-254：B2-1 FROZEN/CLOSED】（2026-09-20）
∀w≥5, **g_w(10) = w·cos(2π/11) − cos(π/11)** ✓✓（C-238 上界 ＋ C-250 Case II ＋ C-251/C-253 Case I）。
数值：cos(2π/11)=0.8412535，cos(π/11)=0.9594930 ⟹ g_5(10)=3.2467747（与 C-233 数值表 g_5/w=0.649 一致）。
方法论模板：①错误的统一曲率界→branch-consistent 不对称曲率→全局门槛；②数值发现→有限分割证书。
审计 errata 5 项（ζ配对/η顺序/单位混用/空值短路/先提交后修正）全部纠正、无残留。
停止条件：不再优化常数，除非形式化或压缩证明文本。详 `C254`。

【定点更新·C-262/C-263：甲类收口与冻结】（2026-09-20）
**甲类：冻结，不再探索** ✓。四项均完成方法族级分类：
① 固定无零区域 ∃δ>0 —— ✗ 尺度墙（`C125`/`C126`/`C127`；`C124` 不与 RH 等价）
② Λ 上界 —— ✗ 定量资产（`C261`：天花板 c_∞>0；RH 接口＝端点等价）
③ 临界线占比 —— ✗ **结构性封口**（`C262`：κ*_M<1；机制＝β 只经重数；0.6818287 是【能力上界】的定量实例，
   ≠「Lean 已证明的 RH 常数」；`ceiling_law256` 依赖 `EnclOK`，后者不经内核）
④ support>1 —— ✗ 需新对象（`C-174`/`C-175`）
**C-263 形式化审计判定 GAP** ✓：承重链第一环「β 只经重数」目前是**机制解释**，还不是严格对象
（`V192` §③ 逐字）；档案真正精确且已形式化的是【带宽 ≤1 类】的天花板（`V184` §0① ＋ `Ceiling.lean`）。
⟹ 停在 GAP，不硬形式化；L1/L2/L3 连 L1 都暂不做。
**新前置筛选**（加在 Scale Gate 之前）✓：候选若仍属 zero-density／mollifier／moment／rank–trace 且未引入
新的 β-sensitive arithmetic channel ⟹ **直接筛掉**。
详 `C262`／`C263`。

【定点更新·C-268：E4 需求驱动的阶梯在 M=1 处闭合】（2026-09-20 23:02）
**结论**：E4 原定理（Palojärvi Thm 4.1，m=1）调用 Lemma 2.2 时用 **M=1**（`E4-palojarvi` §3 Locus C 逐字），
且【**已自足**】：`E4-ENGINE-2` 初等覆盖引理替代 Lemma 2.2 的 M=1 情形，常数改善 10 倍。
扩展侧（m≥2）残留 = `E4-ENGINE-3` §3 逐字：等模长子集 K，|K|=r≥2 需 ∃k≤5r: Σ_{j∈K} Re z_j^k ≥ 1/20+1/40 = **3/40**
（即 (RP_r) 于阈值 0.075）；**r=1..4 已被我方覆盖**（`C-159`／`C-193`／`T13-A`／`C-265`，余量 ≥6.7×）。
**判定**：M=6..11 **全部 STOP**（需求地图证明继续做没有启下）；M=5 身份改为【独立资产／交叉验证】，
结束不自动触发 M=6；「M≤11 定理表」计划正式撤销。
**新纪律**：**先证明下游需要，再允许计算扩大**；禁止反模式「工具能力反过来制造任务」（能算 ≠ 值得算）。
详 `C-268`／`PLAN-RPM-ladder-…` §9–§11。

【定点更新·C-300：外部独立算术机制资产 —— FSD（Failure → Symmetry → Descent）】（2026-09-21 13:13）
**登记判定（唐先生）**：从「审计对象」升级为「**独立算术机制资产**」✓；**性质＝外部资产**（**非**本项目成果 ✗）。
**来源**：公开 GitHub artifact `CaptainSude/Liouville-Goldbach` ✓；**provenance 未闭合** ✗（媒体归因 Astra ＝ provenance claim
≠ 仓库自证；证据链只到「公开 GitHub artifact」✓）。
**对象命题**：Shusterman 的 **Liouville 版**哥德巴赫（∀ 偶数 `N>2`，∃ 正 `a,b`：`a+b=N` ∧ `λ(a)=λ(b)=−1` ✓）；
**注意层级**：Liouville 版 ⟸ 经典版（单向 ✓），**不是**经典哥德巴赫 ✗。
**与 Mangerel 的关系**：Mangerel（`arXiv:2412.17199`）＝ **GRH 条件定理** ✓，承重点＝非主特征乘积 L-函数的一致零自由区
⟹ 短素数区间特征和抵消；本 artifact 走 **路线 B**（绕开 Dirichlet L／特征正交／GRH ✓）。
**审计级别**：语句级 ✓✓（主定理与目标命题逐字一致；用 Mathlib 的 `ArithmeticFunction.liouville`；假设仅 `Even N`＋`2<N`）｜
公理级 ✓✓（12 项关键声明只依赖 `propext`／`Classical.choice`／`Quot.sound`；无 `sorryAx`）｜路线审计 ✓（九项新组件全出现、
七项旧组件全缺席）｜**核心闭环 ✓✓**（`IntervalSigns` 四字段 → 非负／支撑 → 交换方阵 → `A=B` → `A=B=0` → `G(2x)=G(3x)=−G(x)`）｜
终局 ✓（`exists_prime_square_below_half` ＋ Mathlib 二次互反 ＋ `no_multiplicative_agreement`）。
**残余** ⚠️：`*_nat` 深层引理正文（`doubleReflection`／`upperBand`／`quarterBand`／`centralBand`）＋ `oddCompletion`／
`centralRepresentative` 构造正文；**独立复现未做** ✗。
**机制（标签，非框架 ✗）**：七步模板 ＋ **发动机＝4 个局部公理（sign／doubling／tripling／noPP）＋两个可交换作用** ✓。
**纪律（写死）**：不接 RH 主线 ✗；不照搬 ✗（把 λ 换成 RH 对象＝repackaging ✗）；不与 L／F／B／R 排序 ✗；
不声称已复现或已评审 ✗；provenance 与逻辑正确性分离 ✓；FSD 只作标签，不建新判据体系 ✗。
详 `C-300`／`C-299`／`C-298`／`C-297`／`C-296`／`C-295`／`C-294`／`C-291`。

---

## ZBALL-LOCAL 资产（2026-09-26 · 局部攻击弧封存时保留）

**来源**：NOGO-PACKAGE-2026-09-26-local-attack-arc-sealed（commit 3469377）

| 编号 | 资产 | 状态 | 复用条件 |
|------|------|------|----------|
| A1 | 零过量球结构引理：`t_x=0 ⟹ B_1(x) 全 b=1 ∧ 恰一个距离-1 码字 ∧ 其余 n−1 坐标完美匹配` | ✓ 验证（270/270） | 任何使用 `Z` 或 `OC` 的机制 |
| A2 | `Q_2 = [(n−1)E − Σ_{x∉C}OC(B_1(x))]/2`（桥的重写） | ✓✓ 全枚举精确 | 等价坐标转换，非新信息 ✗ |
| A3 | `18 ≤ Z ≤ 44`（n=9, M=62） | ✓ | 上界 44 是目标；下界 18 已得 |
| A4 | gadget 球两两不交（距离 3/4） | ✓✓ | 需 `t_x=0` 前提 |
| A5 | gadget 局部完美（对 E 贡献恒 0） | ✓✓ | 解释局部论证不可能性 |
| A6 | square：`4S ≤ Q_2` ＋等号分类（面不交、`V=4S=N_{≥3}`） | ✓✓ | 需 code 含 2-面；(9,64) 取等饱和 |
| A7 | **机制三要件判据**：global propagation ＋ minimality ＋ excess sensitivity | ✓✓ 战略 | 所有新机制候选的入门门 |

**已淘汰（7 类）**：见 CLOSED-ROUTES-MAP §ZBALL-LOCAL
**STATUS: 本支 PAUSED（资产保留为检测器 ✓）**

---

## A23-D4 — depth-4 local optimality of the 2969-word (23,6,10) incumbent

**Status**: `CLOSED / AUDITED ASSET` ✓ (2026-09-26)
**Type**: finite certificate theorem (not a global bound)
**Statement**: 对 C₀ = `a23.6.10.2969H`（2969 词）不存在 |D|≤4 的正增益交换 ⟹ C₀ 是 4-deletion local optimum
**Fills**: arXiv:2607.19550 明确标为 unresolved 的 depth-4 open problem
**Certificates**: 14,671-state table (`work/k10/a23/a23_d4_state_table.tsv`) + 独立 V1–V4 verifier (无 solver)
**Fingerprints**: sha256(C0)=f2cc5595…09cd ｜ sha256(table)=7de3407d…e8b4
**Key numbers**: max|S(D)|=6 ｜ max α=4 ｜ α 分布 {1:13, 2:746, 3:6787, 4:7125}
**Mechanism template**: global exchange → blocker hypergraph → small local state → α-certificate
**Docs**: `docs/A23D4-ARCHIVE-2026-09-26.md`, `docs/A23D4-CLOSURE-2026-09-26-depth-four-local-optimality-theorem.md`
**Boundary**: 限于 |D|≤4；不主张 A(23,6,10) 上下界


---

## A-DELSARTE-1 · Delsarte × covering-identity ⟹ A₁ 上界（2026-09-26 立 ✓）

**陈述**：设 `|C|=M`、覆盖半径 1，且已知 `Σ_x C(b(x),2) = 2(A₁+A₂)`（等价地已知 `b`-指纹或 `Q`-分支）。把 **Delsarte 不等式族** `M_r = Σ_j a_j K_r(j) ≥ 0`（`a_j`＝有序对比例，`Σ_j a_j = M`）与**覆盖恒等式**并联求解 LP，即得 `A₁` 的严格上界。
**本例**：`M=119`、`Q=1`（`a₁+a₂ = 286/119`）⟹ `max a₁ = 0.825236` ⟹ **`A₁ ≤ 49`**（三法一致 ✓；直测 `a₁≥0.8255` 不可行 ✓；去掉恒等式后上界崩到 429 ✓ ⟹ 该界为**联合产物** ✓）。
**可迁移**：任意 `(n, R=1)` 参数，只要掌握 `b`-指纹即可照搬；亦可作**快速筛选工具**（判某 `(n,R)` 的 `A₁` 窗）。
**细档**：`docs/DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md`
**同类**：`A-…`（本表其他条目）


---

## A-FACE-MULT-1 · 码字对-面多重度拆分（2026-09-26 立 ✓）

**陈述**：在 $\mathbb F_2^n$ 的 2-面（由坐标对 $\{i,j\}$ 与基点 $v$ 唯一确定）上，含给定码字对 $\{c,c'\}$ 的公共 2-面数**只依赖距离**：
`d(c,c') = 1 ⟹ n−1 个公共面`（对 $n=10$：9 个 ✓）；`d(c,c') = 2 ⟹ 恰 1 个`（对角唯一确定面 ✓）；`d ≥ 3 ⟹ 0`。
**推论**：$\sum_F inom{q_F}{2} = (n-1)A_1 + A_2$ ✓ —— 首次把 $A_1+A_2$ **按距离分开加权**（此前两者系数相同而不可分 ⚠️）。
**局限（诚实 ✓）**：与 $A_1+A_2=$ 常数联立后该量仍**由 $A_1$ 仿射决定** ⟹ 不独立收缩可行域 ✗；**登记为可迁移小工具**，不登记为 leverage ✓。
**细档**：`docs/FACE-2026-09-26-two-face-occupancy-audit.md`


---

## A-SUPPEX-1 · support–excess label determines Booleanity on Q₄（2026-09-27 立 ✓）

**陈述** ✓：在 $n=4$ 穷举（非负整数 $f$，$\Sigma f\in[4,9]$，$b\in[1,3]^{16}$，7860 解）中，标签 $(\mathrm{supp}\,f,\ \delta|_{\mathrm{supp}f})$ 经 $\mathrm{Aut}(Q_4)$（阶 384 ✓）规范化后 **完全决定 Booleanity** ✓：49 个规范轨道，**0 个**轨道内不定（纯非 Boolean 16；纯 Boolean 33 ✓）；同一标签亦决定 $D_0=\Sigma f(f-1)$ ✓。**标签不含 $f$** ✓。
**标签（强制 ✓）**：`P1-A mechanism: verified at n=4; no leverage on P1-B` ✓。
**边界** ⚠️：仅 $n=4$ 穷举（未外推 ✗）；**无载荷于规模下界** ✗；**不得**包装为 119 进展 ✗。
**细档**：`docs/SUPPVIS-2026-09-27-support-excess-determines-booleanity-and-its-irrelevance.md`


---

## A-DLP-HARNESS-1 · covering-code Delsarte-LP harness（2026-09-27 立 ✓，**已校准** ✓）

**内容** ✓：按 Gijswijt–Polak（arXiv:2504.01932 §1）公式实现的 LP：变量 `x_0..x_n ≥ 0`，目标 `min q^n x_0`，约束 (i) Krawtchouk 正性 ＋ (ii)(iii)（对每个有效不等式 `(λ,β)`、每个 `k=0..n`）✓；`α^k_{i,j}`（q=2）与 `P_k(i)` 逐字实现 ✓。
**校准证据** ✓：精确复现 `94.0197982166`／`101.0073567955`／`101.4081693983`（7 位小数 ✓✓）；关键参数 = Van Wee 读法 **`λ=(6,1,1,0,…,0)`, `β=6`** ✓（探针：`(1,6,5)`→21.62 ✗，`(1,6,1)`→58.62 ✗）。
**强制自检门** ✓：任何 LP/SDP 重建须满足 **LP ≤ 已知 SDP**（否则建模错，数值禁止入档 ✗）——本项目已连续两次靠它拦下无效值（110.03、170.67 ✓）。
**边界** ⚠️：仅线性层 ✓；**1B（SDP 逐组件消融）本机不可执行** ✗（无 SDP 求解器 ✓）。
**细档**：`docs/DLP1A-2026-09-27-validated-ablation-and-1B-blocker.md`


---

## A-SDP-HARNESS-1 · covering-code SDP harness（未约化 Thm 2.5）（2026-09-27 立 ✓，**Level 1 PASS** ✓✓）

**内容** ✓：按 Gijswijt–Polak（arXiv:2504.01932）**Theorem 2.5** 未约化实现的 SDP：变量 = 三点轨道 $\mathrm{orb}(u,v)=\mathrm{sort}(d(u,v),|u|,|v|)$ ✓；$M'=\sum_t x_tB_t$，$M''=\sum_t x_t(D_t-B_t)$，$N=\sum_t x_tH_t$（常数矩阵线性组合 ⟹ 避免表达式树爆炸 ✓）；约束 = Prop 2.1(ii)(iii) ＋ Prop 2.2（$M'\succeq0,M''\succeq0,R(1-x^0_{0,0},M'')\succeq0$）＋ Prop 2.4(i)(iii)(iv 四族)；目标 $2^n\sum_{u,v}M'_{u,v}$ ⟹ 界 $=(\cdot)^{1/3}$ ✓。
**验证证据** ✓✓：$n=6$：本机 **11.5980553** vs 论文 Table 4 **11.5980** ✓；$n=7$：本机 **16.0000000** vs **15.9999** ✓（残差 $\sim10^{-9}$／$10^{-13}$ ✓）。
**关键坑（必记 ✗）**：第 (iv) 族求和是 $\sum_{w\in S_\ell(v)}$ ✓ —— 误写成 $\sum_{w\in S_\ell(0)}$ 会使界偏低 **0.0820** ✗（正确转换 $w=v\oplus w_0$ ✓）。
**强制自检门** ✓：任何 LP/SDP 重建须满足 **LP ≤ 已知 SDP** 及 **锚点残差 ≪ 目标缺口**；违反 ⟹ 建模/mapping 有错，数值禁止入档 ✗。
**边界** ⚠️：未约化形式对 $n=10$（$1024\times1024$ PSD）不可行 ✗ ⟹ Level 4 须先做 Level 3（Terwilliger 块对角化 ✓）。
**细档**：`docs/P2-1-2026-09-27-LEVEL1-PASS.md`


---

## 资产性质更正 · A-SDP-HARNESS-1（2026-09-27 唐先生 11:34 ✓）

**性质 = 复现／验证 harness** ✓（**非**已证数学资产 ✗）：其证据属 **计算验证**（外部锚点 $n=6,7$ 命中 ＋ 特征值审计 $10^{-13}$ 级 ✓），**不含**数学证明 ✓。
**分级纪律** ✓：`文献复现 → 计算验证 → 数学证明 → 新数学结果` 四层**不得混写**；在 Level 3B（独立证明链：基／代数分解／重数／$eta$ 来源／归一来源 ⟹ PSD 等价）完成前，**禁止**写"已证明 formulation 等价" ✗。
**细档**：`docs/LEVELS-2026-09-27-four-tier-separation-and-3B-pending.md`


---

## A-BETA-GF-1 · $eta$ 的显式生成函数（2026-09-27 立 ✓，**(i) 闭合** ✓✓）

**内容** ✓：论文的 Terwilliger block 系数满足
$$\beta^{\rm paper}_{i,j,k,t}=[p^{i-k}q^{j-k}r^t]\,(r-1)^k\big(1+p+q+pqr\big)^{n-2k}\ ✓$$
**两条独立证明** ✓：(a) $\nu$-侧（$\alpha$-展开 ＋ $(r-1)^k$ 二项 ⟹ 逐项系数 ✓）；(b) $u$-侧（生成函数求和：$t$-和 $=(r-1)^u$ ✓、$i,j$-和 $=(1+p)^{n-k-u},(1+q)^{n-k-u}$ ✓、二项式收口 ✓）。**关键代数巧合** ✓：$(1+p)(1+q)+(r-1)pq=1+p+q+pqr=\alpha$ ✓。
**桥（raw ↔ Schrijver）** ✓：$\widehat\beta=[(j-k)!/((i-k)!\binom{n-2k}{i-k})]\,\beta^{\rm paper}$ ✓（$6$ 组 $501$ 组 $(i,j,t)$ 零不符 ✓）。
**边界** ⚠️：本式对 $\beta^{\rm paper}$（标准化 block 系数 ✓）成立；raw 链侧须经上述桥 ✓；Level 3B 的最终合并（(iv)）未做 ✗。
**细档**：`docs/IDX2-2026-09-27-u-side-generating-function-identity-CLOSED.md`、`docs/L45-...md`


---

## A-L3B-1 · Level 3B 三块统一装配（2026-09-27 立 ✓）

**总标签** ✓：**Level 3B: structurally assembled, symbolically complete except for 3 bookkeeping/classical lemmas.**
**内容** ✓：论文三处 PSD 条件（`eq:Mprimesymmetryreduction`／Prop 4.3 后半／Prop 4.5）的**独立符号重建**：$M',M'',N\in\mathcal A_{2,n}=\mathrm{End}_{S_n}(V)$ ⟹ 均形如 $I_{m_k}\otimes(\cdot)_k$，且 **border 只存在于 trivial $k=0$ 扇区**；PSD 等价来源 = Maschke ＋ Schur ＋ 谱事实（**非** $sl_2$ 半单性 ✗）。
**核心独立链** ✓：$D/U\to H_k\to\rho_u=(-1)^{k-u}\binom ku\to c_{k,i}=((i-k)!)^2\binom{n-2k}{i-k}\to\beta^{\rm paper}=[p^{i-k}q^{j-k}r^t](r-1)^k(1+p+q+pqr)^{n-2k}$（(i) ✓）。
**仍开三项** ⏳：(A) $V_k$ 无重 $S_n$-分解（**classical input**）；(B) $M''$ border 的 $D^{1/2}$ 归一化（convention lemma）；(C) $N$ 中 $\eta$ 的符号闭式。
**细档**：`docs/L3B-FINAL-2026-09-27-three-block-assembly-and-ledger.md`


---

## A-L3B-2 · Classical representation-theoretic input（2026-09-27 立 ✓，**非新资产** ✓）

**性质** ✓：**classical input**（经典引用 ✓），**不计入** N×L×G×D 的 D ✓。
**内容** ✓：$V_k=\mathbb C[\binom{[n]}k]\cong M^{(n-k,k)}\cong\bigoplus_{j=0}^{k}S^{(n-j,j)}$（各不可约**恰一次** ✓，$k\le\lfloor n/2\rfloor$ ✓）；$\dim V_k=\binom nk$ ✓；$H_k\simeq S^{(n-k,k)}$，$\dim=m_k=\binom nk-\binom{n}{k-1}$ ✓（hook-length 显式：$\dim S^{(n-k,k)}=\frac{n!(n-2k+1)}{(n-k+1)!k!}$ ✓）。
**引用** ✓：Young's rule ＋ 两行 Kostka 数 $=1$ ＋ hook-length formula（**不重证** ✓）。
**在 Level 3B 中的角色** ✓：提供层分解无重性、$H_k$ 的类型与维数；**不承担 PSD 等价** ✓（后者由 Maschke＋Schur＋谱事实 ✓）。
**数值核对** ✓：$n=4..10$ 全吻合 ✓；与 L2 的 $\dim\ker D_k$ 实算交叉一致 ✓。
**细档**：`docs/A-L3B-2-2026-09-27-classical-two-row-input.md`


---

## B-L3B-1 · $M''$ border normalization（2026-09-27 立 ✓，**关闭 normalization gap** ✓）

**性质** ✓：convention/normalization lemma（**不产生新数学资产** ✗ ✓）。
**内容** ✓：(1) $z\in W_0$ ✓；(2) $\langle b_i,b_j\rangle=\delta_{ij}\binom ni$ ⟹ $D_0=\mathrm{diag}\binom ni$（$\{b_i\}_{i=0}^{n}$，共 $n+1$ 个 ✓）；(3) $Q_0=E_0D_0^{-1/2}$ 列正交归一 ✓；(4) $\boxed{z_{\rm block}=D_0^{1/2}z_{\rm raw}}$ ✓（**reciprocal 陷阱**：**非** $D_0^{-1/2}$ ✗）；(5) 与论文 $D^{1/2}$ 形式一致（audit criterion = **先定义 $D$，再判平方根** ✓）；(6) 关闭 Level 3B 的 normalization gap ✓。
**独立交叉** ✓✓：与 R1a 数值审计（1e-13 级 ✓）中 $B_h$ 的构造**完全一致** ✓。
**细档**：`docs/B-L3B-1-2026-09-27-Mpp-border-normalization.md`


---

## C-L3B-1 · Lasserre $\eta$ coefficient closed form（2026-09-27 立 ✓）

**性质** ✓：closure/reconstruction（**非新数学资产** ✗ ✓）。
**内容** ✓：平移 $w$ 使原四类 (both, u-only, v-only, neither) 按 $w_x$ **互换**（both↔neither、u-only↔v-only）⟹ 记 $(c,a,b,d')$ 为四区域取 $w_x{=}1$ 的个数 ⟹
$$\eta^{(i,j,t)}_{(i',j',t'),d}=\sum_{c,d'}\binom tc\binom{i-t}a\binom{j-t}b\binom{n-i-j+t}{d'}\ ✓$$
**母函数** ✓：$G_\eta=(A+sD)^t(B+sC)^{i-t}(C+sB)^{j-t}(D+sA)^{n-i-j+t}$ ✓（$A{=}B{=}C{=}D{=}1\Rightarrow(1+s)^n$ ✓）。
**核对** ✓✓：暴力 η vs 闭式 $29$ 组零不符 ✓；暴力 vs $G_\eta$ 项数 $32{=}32,32{=}32,46{=}46$ 恒等 ✓；$N_k$ 接口与 R1b 谱级审计一致（$\sim10^{-13}$ ✓）。
**约定** ⚠️：论文 Prop 2.4(iii) 钉死 $d=|w|$ ✓；作者代码用 $\texttt{dist}=d(v,w)$ 另一参数化 ⚠️ ⟹ **最终钉死须 R2**（块式 SDP vs 已验 unreduced 锚点 $11.5980553/16.0000000$）⏳。
**细档**：`docs/C-L3B-1-2026-09-27-lasserre-eta-closed-form.md`


---

## A-ZETABOUND-1 · surfeit 诱导的显式 $A$ 上界（2026-09-27 立 ✓，**小资产** ✓）

**性质** ✓：显式有效界（**不计为机制** ✗）。
**内容** ✓：对任意 radius-1 覆盖码 $C\subseteq\{0,1\}^n$, $|C|=M$：$A_1+A_2\le\frac{(n+1)E}{4}=\frac{(n+1)(M(n+1)-2^n)}{4}$ ✓（2026-09-27 **更正** ✓：旧式 $n^2{+}2n{+}3$ 为笔误 ✗）。
**来源** ✓：$\zeta=M(n^2+2n+2)-(n+2)2^n-4(A_1+A_2)$ ✓（本机 6/6 精确验证 ✓）＋ $\zeta\ge-(2^n-M)$ ✓。
**比较** ✓：6/6 例强于纯 Delsarte LP 上界 ⟹ 不在 Delsarte 线性包络内 ✓；但高于实测 $3\times\sim8\times$ ⟹ **valid but non-leveraging** ✓。
**诚实备注** ⚠️：实质等价于 $\zeta\ge-(2^n-M)$ 的重写；文献是否已有未查 ✓。
**细档**：`docs/PHASE2-AUDIT-2026-09-27-surfeit-global-pair-collapse.md`


---

## A-BALLCOLLAPSE-1 · 球交叠塌缩定理 ＋ $(A_1,A_2)$ 分裂自由度（2026-09-27 立 ✓）

**性质** ✓：**结构性定理（一行 ✓）＋ 决定性数据** ✓（**非机制** ✗，但为"NO-GO 必然性"提供解释 ✓ = G-PROGRESS α ✓）。
**定理** ✓：$|B_1(c)\cap B_1(c')|=2\cdot\mathbf 1[d\le2]$ ⟹ 一切球交叠型量（excess、surfeit、$A_{\le2}$、$Q$、profile 矩、$\zeta$）**只能是** $A_1+A_2$ 的函数 ⟹ 其塌缩是**结构性必然** ✓✓。
**穷举刚性** ✓：$n=4$：40 个极小覆盖码；$n=5$：**320 个**，全部共享 $A=6$、profile $\{(1,24),(2,6),(3,2)\}$、$T_3=2$ 及全部布置统计量 ✓。
**决定性数据** ✓✓：$n=9,K=62$ 双码 —— profile／$A=73$／$T_3,T_4,S_2,S_{2b},H_H,P_2$ **全同** ✓，而 $(A_1,A_2)=(7,66)$ **vs** $(26,47)$ ⟹ **分裂自由度存在** ✓。
**细档**：`docs/PHASE2-KEY-2026-09-27-ball-collapse-theorem-and-the-A1-A2-split.md`
**数据源**：`work/k10/c62/K_9_1_classif.txt` ✓


---

## A-Q0-1 · Q0 二次展开判定（2026-09-27 立 ✓）

**结论** ✓：$\zeta+(2^n-M)=(n+1)E-4A=\sum_x\delta(x)(n-\delta(x))$ ✓（本机 6/6 精确 ✓）⟹ 码层内容 = **线性界** $A_1+A_2\lerac{(n+1)E}{4}$ ✓ ⟹ **Q0-a 与 Q0-b 双命中 ⟹ STOP，不上 SDP** ✓。
**登记类别** ✓：valid / non-profile-appearing quadratic constraint, but **no leverage beyond the linear bound** ✓。
**细档**：`docs/PHASE2-Q0-2026-09-27-quadratic-expansion-verdict.md`


---

## A-COVERCAP-1 · 覆盖侧二阶矩封顶定理 ＋ 缺口坐标（2026-09-27 立 ✓）

**定理 A** ✓：$\sum_xb=M(n+1)$、$\sum_xinom{b(x)}2=2(A_1+A_2)$ ⟹ $\sum_xb^2=M(n+1)+4(A_1+A_2)$ ⟹ **一切 $b$-二阶矩／球对交叠型不变量至多看到 $A_1+A_2$** ✓。
**定理 B（witness）** ✓：$n=9,K=62$ 两码 $I_1/I_2$ 统计量**逐项相同**，而 $D=A_1-A_2=-59$ **vs** $-21$ ✓ ⟹ 盲区非空 ✓。
**信息分层** ✓：$\mathcal I_1\subset\mathcal I_2\subset\mathcal I_3$；$\mathcal I_1,\mathcal I_2\Rightarrow A_1+A_2$ 但 $
ot\Rightarrow(A_1,A_2)$ ✓。
**缺口定理 ＋ β gate** ✓：下一轮必须构造 $J$ 使 $J(C_0)
e J(C_1)$ 且非 $(A_1,A_2)$ 的函数；测试集 = 两 witness ✓。
**细档**：`docs/CLOSURE-2026-09-27-covering-side-ceiling-and-gap-theorem.md`


---

## A-SEPPAIR-1 · $n=9,K=62$ separation pair ＋ 判据清单（2026-09-27 立 ✓✓）

**性质** ✓：**测试集资产**（下一阶段所有候选不变量必须先在两码上求值 ✓）。
**数据源** ✓：`work/k10/c62/K_9_1_classif.txt`；指纹：码#0 `3639c34b…`／码#1 `a2fed1d7…` ✓。
**关键量** ✓：$A=A_1{+}A_2=73$ **相同** ✓；$D=A_1{-}A_2=-59$ **vs** $-21$ ✓；(7,66) vs (26,47) ✓。
**盲区类（12 项 ⟹ 同值即 DROP ✓）**：profile、$\sum b$、$\sum b^2$、$A$、$T_3$、$T_4$、$S_2$、$S_{2b}$、$H_H$、$P_2$、$\sum\delta(n-\delta)$、$N_{\ge5}$ ✓。
**分离类（9 项 ✓）**：$A_1,A_2,D,N_2,N_3,N_4,I,S,\sum_F\binom{q_F}2$ ✓。
**方法学** ✓：quadratic appearance $\not\Rightarrow$ quadratic information ✓。
**细档**：`docs/CLOSURE-2026-09-27-Q0-STOP-and-the-separation-pair.md`


## A-VWEQCHAIN-1（2026-09-27）
**van Wee 等号链（self-contained $b\le2$）** —— 来源：van Wee 1988（TU/e 仓储 353803.pdf ✓ 原文核）Lemma 8 ＋ Theorem 9（$K(n,1)\ge2^n/n$ ✓、$K(2^r,1)=2^{2^r-r}$ ✓）；等号分析（唐先生 12:56 ✓）；数值审计 8/8×2 码 ✓✓。
产出：$n=2^m$ ⟹ $b\in\{1,2\}$ ✓、$d_1\le1$（matching）✓、$J_2=2A_1$、$J_3=J_6=0$、$A_1+A_2=M/2$ ✓、二部结构 $\deg_Z(a)=1$/$\deg_{\mathcal A}(z)=n-1$ ✓。
边界：不解决 P1-2（剩余 $\Sigma a_i^2$、$\Sigma q_{ij}^2$ 两量 OPEN ✓）；不涉 $n=10/119$ 判定 ✓。


## A-P12PASS-1（2026-09-27）
**P1-2 PASS（同 (A₁,A₂) 而 J 分叉）** —— Theorem-13 构造域（240 互异码，$S_7	imes\mathbb F_2^7$ 表示级去重 ✓）内发现：三个两两不等价最优 $(8,32)_1$ 码，$(A_1,A_2)=(0,16)$ 且**全距离分布相同**，$J_7=64/128/256$ ✓✓（双算法复核 ✓）。
结构事实：$A_1=k=|C_1\cap C_2|$ ✓；分叉仅见于 $k=0$（Type B）；机制 = 16 个跨半距离 2 对沿 $\{i,7\}$ 方向的集中度 ✓。
边界：限 $n=8$ Theorem-13 族 ✓；否证"$(A_1,A_2)$ 决定 support-2"的 collapse 假设 ✗；不涉 119 判定 ✓。


## A-ALIGNLAW-1（2026-09-27）
**Type-B alignment-profile 律（n=8 完整域）**：$q=rac{A_2}{|S|}\mathbf 1_S$，$J_7=A_2^2/|S|$，$|S|\in\{1,2,3,4,7\}$；$S$ 恒为 $\mathbb F_2^3$ 仿射几何集（点/直线/平面/全空间减 0）；数量分布 $7,21,7,1,7$ ✓。双计数给出 $H\leftrightarrow C_2$ 完美匹配（唯一）⟹ 覆盖几何对 $q$ 无方向约束 ✗；约束来源 = 完美码综合征算术 ✓。
边界：n=8 完整验证 ✓（非一般定理 ✗）；不涉 119 ✓。


## A-ALIGNTHM-1（2026-09-27）
**Alignment Quantization Theorem（已证 ✓，n=8）**：$H=\ker\sigma$ Hamming $[7,4,3]$，$C_2=\pi H+e$ 不交 ⟹ $q_i=\lambda\mathbf 1_{\{i:t_i\in s+\mathrm{Im}f\}}$，$\lambda=2^{4-d'}$，$|S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f]\le7$ ⟹ $A_2=\lambda|S|$，$J_7=A_2^2/|S|$ ✓✓。证明 = 初等线性代数（直方图 $n(x)=2^{4-d'}\mathbf 1[x\in\mathrm{Im}f]$ ✓）。七情形完整分类 ✓（$(3,ot)$ 不可达 ✓）；3840 表示数值全吻合 ✓。预测 $n=16$ 同型（$\lambda=2^{11-d'}$ ✓）。边界：限 Theorem-13 域与 $R=1$ ✓；不涉 119 ✓。

**升级（2026-09-27 P2）**：A-ALIGNTHM-1 升级为 **$2^m-1$ 族统一定理**（证明与维数无关 ✓）；$n=16$ 16 配置验证零反例 ✓✓（覆盖 $(d',|S|)=(0,0),(1,1),(2,3),(3,8),(4,15)$ ✓）；$(d'=m-1,s\notin\mathrm{Im}f)$ 不可达 ✓（$|S|=2^{d'}>n$ ✓）。$J$ 非单调（须看整结构 ✓）。自捉 $\pi^{-1}$ 方向 bug（$|S|$ 满时不可见 ✓）。未覆盖：非线性 $C_1$ ✓；$n\geq32$ 未验证 ✓。


## A-P3ALPHA-1（2026-09-27）
**P3-α 判定 = PASS**：文献（Boruchovsky–Etzion–Roth）距离/重量分布层**不能**蕴含 alignment 量子化。自足证明：三个 n=8 见证码全距离分布相同（0,16,160,176,64,48,32,0）而 $J_7\in\{64,128,256\}$ ⟹ $B
ot\Rightarrow q$ ✓✓。**归属更正**：完美匹配已在 §II Cor 14(2)（重推导，不新 ✗）；新增 = 量子化 ＋ 仿射支撑 ＋ $(d',s)$ 转移结构 ✓。文献无 syndrome 语言（命中 0 ✓）。arXiv:2605.12148（2026 统一重量分布）仍在 weight-distribution 层 ✓。边界：不涉 119 ✓。


## A-P3JIA-1（2026-09-27）
**P3-甲 = STOP**：Type A 不给出新 $q$ 层结构。理由 = 证明（非文献空白）：论文 Theorem 17 证明逐字 "no two codewords in $\mathcal C$ at distance 2 apart" ⟹ $A_2=0$ ⟹ $q\equiv0$ 空洞 ✓。§V 对象 = 伙伴对的坐标剖面（$a_v$ 型、且 Lemma 37 显示**刚性**）≠ $q_v$ ✓。**对照升级**：$(d',s)$ 分类细化 Type A/B/C——Type C 分 4 子类（$A_2=1024/1536/1792/1920$ ✓），论文重量分布层不可见 ✓（属我方定理推论，非文献结果 ✓）。边界：不涉 119 ✓。


## A-P3BETA-1（2026-09-27）
**P3-β 判定 = STOP-β**（算术层无剪枝力；9 块全可实现 ⟹ PASS-β 判据不可达 ✓）。**修正**：$\lambda=A_2/|S|$，$J=\lambda A_2$（非 $\lambda=J$ ✗）。**自我修正**：$(d',s)$ **不**与 $A_2$ 一一对应——四个 $ot$ 块共享 $A_2=2048=M/2,\ A_1=0$ 而 $J=2^{22-d'}$ 各异 ✓✓。**加强**：$ot$ 族 $J$ 分层数 $=m$（$n=8$ 三层、$n=16$ 四层 ✓）= P1-2 PASS 现象的升维版；文献 Type/重量分布层不可见 ✓。边界：通用性（Theorem-13 形 = 全部 NP1CC?）为研究级问题 ⚠️；不涉 119 ✓。


## A-P3BETACORE-1（2026-09-27）
**β-Core 修正与验证**：$q=\lambda\mathbf 1_{U\setminus\{0\}}$（$\lambda=A_2/|S|=2^{n-m-d'}$，**非** $J$ ✗，第三处修正 ✓）。**卷积修正（已验）**：$(q*q)(x)=\lambda(2^{d'}-2)q(x)+\lambda^2(2^{d'}-1)\delta_0(x)$ ⟹ 代数 $\mathrm{span}\{q,\delta_0\}$ 为 2 维（**非** $q*q=\mu q$ ✗）。**Fourier 修正（已验）**：$\widehat q\in\{A_2,-\lambda\}$（双值 ✓，**非** $\{0,\mu\}$ ✗）。**已验证结构 ✓**：加法闭合 $u
e v\in S\Rightarrow u+v\in S$ ⟹ $S\cong PG(d'-1,2)$（$n=16$：$d'=3$ 给 Fano 7 线、$d'=4$ 给 $PG(3,2)$ 35 线 ✓✓）。Gate 逻辑地位不变：族内为定理 ⟹ 剪枝力 = 检验族外候选（违 gate = 非 Theorem-13 形证书）✓。


## A-P2A-1（2026-09-27）
**P2-A 工具与正控**：内蕴差向量分布 $\nu$（仅用论文 §II 伙伴对划分 ⟹ 对任意 NP1CC 有定义 ✓）。**正控通过 ✓✓**：$n=16$ Type C 实例（$|C|=4096$、$k=256$、伙伴对 2048、$\nu=\{1:256,2:1792\}$）满足星性质（$\ell=15$ ✓）与 flatness（切片 $\equiv\lambda=256$ ✓）。**自纠**：$|Z|=M=4096$（非 $M/2$ ✗）。**缺失成分**：非线性半码 NP1CC（Vasil'ev 型）或 ENP1CC puncturing ✓。E3：非星 ∨ 非 flat ∨ 支撑非几何 ⟹ NP1CC ⊄ Theorem-13 β-shape ✓。警告：构造新 ≠ gate 新 ✓。


## A-PERFCOND-1（2026-09-27）
**系统形式完美码的判定条件（导出并双向验证 ✓）**：$C=\{(u,\psi(u))\}\subset\mathbb F_2^{15}$ 是完美 $[15,11,3]$ 码 $\iff$ $orall a$：$\{\psi(a+e_j)\oplus\psi(a)\}_{j=1}^{11}=W_2$（$W_2$ = $\mathbb F_2^4$ 中重量 $\ge2$ 的 11 个向量 ✓）。验证：线性 $\psi=A$（11 列 = $W_2$）违反 0/2048 ✓；朴素非线性 $\psi=A\oplus\varphi$ 违反 1984/2048 ✗。
**首次尝试失败记录**：$\psi=A\oplus\varphi$（$arphi$ 二次）⟹ 覆盖核验失败 ✗ ⟹ 非 NP1CC ⟹ 其 $\nu$ 的"非星"结论**无效**，不得记为 P2 collision ✓（纪律验证 ✓）。


## A-VASILEV-1 + A-E3-1（2026-09-27）
**实现 bug 更正（三处撤回 ✗）**：第三块未截单比特 ⟹ 生成字越界 ⟹ 撤回"六形状全失败"、"distance-aware 诊断"、以及对唐先生 $V_{15}$ 数据的"不复现"判定；更正后形状 A **确为完美码** ✓、$|C_1\cap V|=256$ **与其报告一致** ✓。
**已验证构造 ✓**：$V=\{(v,\,v+c,\,|v|\oplus\lambda(c))\}$（$\lambda(c)=c_0c_1$）⟹ $|V|=2048$、$\mathfrak B_1(V)=\mathbb F_2^{15}$（掩码＋暴力双验）、$V$ 非线性 ✓。
**E3 判定（NEGATIVE ✓）**：$C=(H_{15},0)\cup(V,1)$ 覆盖核验通过 ⟹ **NP1CC 确认** ✓；$\nu=\{1:256,2:1792\}$，$A_2=1792$，星性质 ✓、flatness ✓、$|S|=7$ ⟹ **首个家族外（非线性半码）NP1CC 仍满足全部 β-gate** ✓✓（单例证据，不得推广 ✗）。边界：119 不碰 ✓。


## A-P2COLLISION-1（2026-09-27）⭐
**已验证 P2 反例**：$C=(H_{15},0)\cup(V_\lambda,1)$，$V_\lambda=\{(x,x+c,p(x)\oplus\lambda(c))\}$，$\lambda=\mathbf 1[c\ne0]$ ⟹ (i) $V_\lambda$ 完美码（掩码＋修正版暴力 400 目标 0 未覆盖 ✓）；(ii) $C$ 为 NP1CC（$|C|=4096=2^{16}/16$、200 目标 0 未覆盖、$\max b=2$、$|Z|=M$ ✓）；(iii) **flatness 违反** ✗：$\nu=\{1:288,2:1760\}$，star ✓，切片 $q_v\in\{288,224\}$ 两值，$A_2/|S|=251.43\notin\mathbb Z$ ⟹ $\mathrm{NP1CC}\not\subseteq$ Theorem-13 β-shape ✓✓。逐坐标计数多重集 $\{288^3,224^4\}$ 为码不变量 ⟹ 不与族内码等价 ✓。对照：$\lambda\equiv0$ 与 $\lambda=c_0c_1$ 均通过 ✓ ⟹ **β-shape 依赖具体半码** ✓。**两处实现 bug**（第三块未截单比特；暴力检验目标写在生成式内）已更正 ✓。**A-ALIGNTHM-1 适用范围收紧**：只对线性半码族成立，不得作通用不变量 ✗。


## A-COSETLAW-1（2026-09-27）⭐
**145 例 $\lambda$ 扫描**（affine 16 + 二次 64 + 具名 5 + 随机 60）：**INVALID=0**；**star 145/145**；flat 89 / **非 flat 56**。**判据**：flat $\iff$ $|S|\mid A_2$（此时切片 $\equiv A_2/|S|$）。**精化律（详验 ✓✓）**：$\mathrm{supp}\,
u=(a+W)\setminus\{0\}\sqcup(b+W)$，$W=\mathrm{span}\{2,4\}=\{0,2,4,6\}$，且 $
u$ **在每个陪集上恒定**；flatness ＝ 两陪集值相等 ⟹ A-ALIGNTHM-1 为线性半码退化特例 ✓。**affine $\lambda$（16/16）全部 flat** ✓；$a=7$ 给单陪集 $|S|=3$、$A_2=1536$ 仍 flat ✓。十二结果类与 $J$ 已登记（见档 §1）。边界：非全部 $2^{15}$ 个 $\lambda$ ⚠️；$W$ 恒定性未证 ⚠️。


## A-CLOSEDFORM-1（2026-09-27）⭐
**ν 闭式（推导 ＋ 143 例验证 ✓）**：$q=X*C$，$X(x)=\alpha(x)\oplus\beta(x)\oplus15|x|$，$C(c)=\beta(c)\oplus15\lambda(c)$；**$X$-分布 $=\{0,2,4,6\}$ 各 32** ⟹ $X$ 在 $W=\mathrm{span}\{2,4\}$ 上均匀 ⟹ **陪集常值被强制**（非经验 ✓）。两陪集值 $=\mathbf{32s}$ 与 $\mathbf{32(16-s)}$ ⟹ **和恒 512 ✓**；**flat $\iff s=8$**（$q\equiv256$ ✓）；$A_2=2048-32s$ ⟹ $7\mid A_2\iff s\equiv1\pmod 7$，实测 $s\in\{2..14,16\}$ ⟹ 唯一 $s=8$ ⟹ **经验判据「flat $\iff|S|\mid A_2$」由此推导解释 ✓**。统计：flat 89 / 两值 54（54/54 和=512 ✓）/ 三值以上 **0** ✓。**两处实现层更正 ✓**（距离-2 对双重中点致重复计数；互补检验误用值列表）。余项：$s(\lambda)$ 纤维表达式 ⚠️、$s\notin\{0,1,15\}$ ⚠️、$W$ 恒定性 ⚠️。


## A-SUBSPACE-1（2026-09-27）⭐ 闭式完备
**四陪集一般律（唐先生修正）**：$W=\mathrm{span}\{2,4\}$，$q(z)=32\sum_{u\in W}C(z\oplus u)=32s([z])$ ⟹ $q$ 在每个 $W$-陪集内恒定，$\sum_i s_i=16$。**本族两陪集定理（证明 ✓✓）**：$V=\mathrm{span}\{2,4,9\}=\{0,2,4,6,9,11,13,15\}$（dim 3），$W\le V$、$15\in V$、$\beta(H_7)=\{0,4,11,15\}\subseteq V$ ⟹ $C=\beta(c)\oplus15\lambda(c)\in V$ 恒成立 ⟹ $s_1=s_2=0$，$\mathrm{supp}\,q=(W_0\setminus\{0\})\sqcup W_3$ 恰 7 坐标 ⟹ **star 与 $|S|=7$ 导出**。**闭式 ✓✓**：$s_0=8+(b-a)$（$a,b$ 为 $\lambda$ 两侧计数），$s_3=16-s_0$ ⟹ **512-互补为定理**；flat $\iff a=b$。**卷积恒等式**：16 syndrome 全验 $\max|\Delta|=0$ ✓✓（修正作者漏 $\beta(x)$ 之测量 bug）。$A_2=2048-32s_0$ ⟹ 经验判据「flat $\iff|S|\mid A_2$」被推导。余项：可实现 $(a,b)$ 刻画 ⚠️。


## A-SAGREE-1（2026-09-27）⭐ 更正
**$s$ = agreement number**：$C_\lambda=\beta(c)\oplus15\lambda(c)$，$\mathrm{im}\beta=U=\{0,4,11,15\}$（4/4/4/4），$r=\pi\circ\beta$（$\pi(0){=}\pi(4){=}0,\pi(11){=}\pi(15){=}1$；分布 $\{0:8,1:8\}$）⟹ $s=\#\{c:r(c)=\lambda(c)\}$ ⟹ $s\ge1$（$\lambda(0){=}0{=}r(0)$）、$s\in\{1,\dots,16\}$ **全可达** ✓。
**硬门验证 ✓✓**：$s{=}1$（$\lambda{=}1\oplus r$）、$s{=}15$（$r$ 翻一处）、$s{=}16$（$\lambda{=}r$）三例 $V$ 完美、$C$ 覆盖 **全部通过** ⟹ 皆为合法 NP1CC ✓。
**🔴 判据证伪 ✗✗**：「flat $\iff|S|\mid A_2$」双向证伪（$s{=}1$：$7\mid2016$ 但非 flat；$s{=}16$：flat 但 $7\nmid1536$）⟹ 上档 FINAL-CLOSEDFORM 之「flat $\iff s{=}8$ 由 $7\mid A_2$ 推出」**作废**，其前提 $s\in\{2..14,16\}$ 系抽样假象 ✗。**正确**：flat $\iff s{=}8$；$7\mid A_2\iff s\in\{1,8,15\}$。


## A-EXTGATE-1 + A-SPLIT37-1（2026-09-27）⭐
**(甲) External-Cover Gate = NO-GO**：覆盖性初等 ✓；**inclusion-minimality 本机实测 ✓✓**（$\lambda=\mathbf 1(s{=}9),1{\oplus}r(s{=}1),r$翻一$(s{=}15),r(s{=}16)$ 四例 $V$ 与 $\mathcal C$ 皆最小）⟹ **外部覆盖/最小性均不含 $s$-信息**，$s\in\{1,\dots,16\}$ 全可达 ⟹ 「NP1CC $\Rightarrow s\in$ 小子集」被 $s{=}1,15,16$ 击穿 ✓。
**(乙) 3/7 分裂定理 ✓✓**：$\mathrm{supp}$ 来自 $(W_0\setminus\{0\})$（3 列）$\sqcup\,W_3$（4 列）⟹ $1\le s\le15\Rightarrow|S|=7$；$s=16\Rightarrow|S|=3$；$A_2=2048-32s$ ✓。
**flat 再更正**：flat $\iff q$ 在 $\mathrm{supp}$ 上恒定 $\iff s\in\{8,\mathbf{16}\}$（上档"flat $\iff s=8$"漏 $s=16$ ✗）。


## A-STEP01-1（2026-09-27）⭐
**Step 0 闭合 ✓✓**：$s\in\{1,\dots,16\}$ 全可达；本机六例（$s{=}1,2,3,4,8,16$）逐项验证 $(A_1,A_2,J)=(32s,\,2048-32s,\,1024(3s^2+4(16-s)^2))$ **全命中**，硬门（$|V|{=}2048\wedge\mathfrak B_1(V)\wedge\mathfrak B_1(\mathcal C)$）全过 ✓ ⟹ $(A_1,A_2)$ 单参数线、$A_2=2048-A_1$。
**Step 1 族外池 ⚠️**：七个完美半码两两拼接共 28 对，**全部过覆盖门**；桶 $(A_1,A_2)$（去重后）：$(128,1920)\times2,(896,1152)\times2,(1024,1024)\times6,(1152,896)\times7,(1280,768)\times3,(2048,0)\times7$，**每桶 $J$ 唯一 ⟹ 未见 P1-2 分叉** ⟹ 单参数塌缩可能深于 Vasil'ev。边界：仍未触及 ENP1CC puncturing ⚠️。
**更正**：$A_1+A_2$ 曾=4096（双计 bug，距离-1/-2 对各有 2 公共中点）；配对去重后 = $M/2=2048$ ✓。


## A-YI-1（2026-09-27）⭐
**(乙) 判定**：**乙-1 否定普遍性 ✓**——不存在普遍恒等式 $J=f(A_1,A_2)$：$n=8$ 三见证码不等价、全距离分布相同 $(A_1,A_2)=(0,16)$ 却 $J_7\in\{64,128,256\}$ ✓（唯一普遍的是等号链 $A_2=M/2-A_1$）。**乙-2 机制（假设，强支持 ⚠️）**：$n=16$ 侧 $q=X*C$，$X$ 的像 $=W$（真子群，4 元）、纤维 32 ⟹ **平均化** ⟹ $W$-陪集常值 ⟹ 仅两个自由值 ⟹ $J$ 被 $s$ 钉住；$n=8$ 侧射线计数形状三变（$4\times4,\ 2\times8,\ 1\times16$）同 $A_2=16$ ⟹ 无强制 ⟹ **首次失去强制 = "陪集常值"这一步**。**乙-3 靶点**：ENP1CC puncturing 应刻意破坏"集中化/平均化"同时保留两完美半码与 $(A_1,A_2)$ 桶；可测指标 = $x$-部映射的像大小与纤维谱。边界：乙-2 在 $n=8$ 侧未用同一语言分解 ⚠️（待微步判定）。


## A-PHIDICH-1（2026-09-27）⭐
**(i) 微步：$\Phi$-像形态二分 ✓**（$\Phi=\sigma_{n-1}$ 限于第二半码）：$n=8$ 三见证码（桶 $(0,16)$）的像为**陪集**（$0
otin\mathrm{im}$，大小 $1/2/4$ 自由，纤维谱 $\{4{:}4\}/\{8{:}2\}/\{16{:}1\}$）✗；$n=16$ 对照（$\lambda=\mathbf 1,\ r$）的像 $\cup\{0\}$ **闭成子群**（$V$，8 元；或 4 元），纤维在 $W$-陪集上均匀 ✓。**两因素拆开**：①集中形态（是否"穿孔子群"形）②纤维均匀；$n=16$ 两者皆 ✓ ⟹ $J$ 被 $(A_1,A_2)$ 钉住；$n=8$ ①失败 ⟹ 支撑形状自由 ⟹ $J$ 分叉。判定：**机制 SUPPORTED ✓ → 转 (甲)**；边界：$n=16$ 必然给穿孔子群形态之证明仍缺 ⚠️。**(甲) 靶点**：破坏"像 = 穿孔子群"形态或纤维陪集均匀性，同时保留两完美半码与 $(A_1,A_2)$ 桶。


## A-JIA-1（2026-09-27）⭐⭐ P1-2 PASS at n=16
**(甲) ENP1CC puncturing**：半码池 = 3 原 Vasil'ev ＋ 45 个 "extend-by-parity → puncture" 所得（皆过 $\mathfrak B_1$ 硬门）⟹ 48 个皆为**合法 NP1CC** ✓。**J-分叉命中 ✓✓**：桶 $(A_1,A_2)=(128,1920)$ 内 $J\in\{638976,\mathbf{245760}\}$（前者为纯 Vasil'ev $s{=}4$ 支，后者为打孔来源 11 例）⟹ 同桶异 $J$ ⟹ **P1-2 PASS at $n=16$** ✓✓（$J$ 为等距不变量 ⟹ 必不等价 ✓）。**机制相关性 ✓**：$J{=}245760$ 者恰为 $|\mathrm{im}\,\Phi|{=}16{=}|G|$（全群、未集中）；$J{=}638976$ 者为集中支 ⟹ 支持"集中 ⟹ 刚性、非集中 ⟹ 自由"（机制仍 SUPPORTED ⚠️）。**方法学 ✓**：池内 7 桶皆无分叉 ⟹ **分桶必须跨构造** ✓。


## A-JIAPRIME-1（2026-09-27）⭐
**convention 钉死 ✓**：$J_{\rm int}=\sum_{i=1}^{15}q_i^2$（内蕴，= 伙伴对差集 $\sum\nu(D)^2$）与 $J_{\rm all}=\sum_{g}\rm fib(g)^2$ 差 $\rm fib(0)^2$；实测 $s{=}4$ 纯 Vasil'ev 给 $638976/655360$、$\mathrm P(\lambda{=}\mathbf 1,i{=}9)$ 给 $\mathbf{245760}/262144$ ⟹ **两约定下分叉皆稳健** ✓✓（本线统一用 $J_{\rm int}$）。
**48 码形态指纹 ✓**：池内**全部** $0\in\mathrm{im}\,\Phi$ 且 $\mathrm{im}\,\Phi$ 闭成子群（不出现 $H\setminus\{0\}$ 形 ✗）；谱型 7 种：$\{128^{16}\},\{256^8\},\{512^4\},\{224^4,288^4\},\{112^8,144^8\},\{16^8,240^8\},\{32^4,480^4\}$。
**关键更正 🔴**：「$J$ 由指纹决定」是恒等式（$J_{\rm int}=\sum_{\rm 非零列}\rm fib^2$）⟹ 真正内容 = **给定 $(A_1,A_2)$ 哪些谱可实现**；且 $|\mathrm{im}\,\Phi|$ **不足以**决定 $J$ ✗（$|\mathrm{im}\Phi|{=}8\Rightarrow J\in\{449536,458752,924672\}$；$16\Rightarrow\{245504,245760,462592\}$）。池内反向检验无反例 ✓；跨构造对照给同桶异谱 ⟹ 同桶异 $J$ ✓。判定 **SUPPORTED** ⚠️。


## A-FEAS-1（2026-09-27）⭐⭐ 纤维谱分类
**(甲″-i) 四档 gate**：**PASS-1 ✓** 可实现谱型全集 $\mathcal S=\{\bar m^{m}\}$（单级）或 $\{v^{m/2},(2\bar m-v)^{m/2}\}$（平衡两级），$m=|\mathrm{im}\,\Phi|$、$\bar m=2048/m$、两级和 $=2\bar m$、多重度等分；**PASS-2 ✓** 池内（$\lambda\in\{0,\mathbf 1,r,s{=}2..10\}$ ＋ 15 路打孔）全部落入；**PASS-4 ✓** $J_{\rm int}=\sum_j e_jm_j^2-v_0^2$（$v_0=A_1$），21 个互异谱型逐项命中 ✓✓；**PASS-3（部分）✓** 组合约束（$\sum e_j=m$、$\sum e_jm_j=2048$）不足以推出平衡结构 ⟹「平衡两级」是**额外代数条件**（观测，无证明 ⚠️）。**自由度维数 = 1 ✓**：$J=J(m,v_0,v_1)$。


## A-INVOL-1（2026-09-27）⭐⭐ 两级定理
**对合存在 ✓✓（48/48 实测）**：$I=\mathrm{supp}(f)$ **是子群**且 $[I{:}W]\in\{1,2\}$（$W$ = 周期）；两级时 $\tau(g)=g\oplus\eta$（任一非平凡陪集代表）满足 $\delta(\tau g)=-\delta(g)$ ⟹ 等价地 $\delta$ 是 $I/W\cong\mathbb F_2$ 上的**非平凡线性特征**（= 候选 3 ✓）。
**三结论推导 ✓✓**：$I$ 子群 ＋ $f$ 在 $W$-陪集恒定 ＋ $[I{:}W]{=}2$ ⟹ (i) 二级 $\{v_1^{m/2},v_2^{m/2}\}$、(ii) 多重度等分、(iii) $v_1+v_2=2\bar m$ —— 三者是同一陪集结构的三个面 ⟹ A-FEAS-1 的"额外条件"归约为 $I$ 子群 $\wedge[I{:}W]\le2$ ✓。
**状态**：Vasil'ev 支 **已推导**（$f=X*C$、$X$ 在 $W$ 上均匀 ⟹ $W$-不变 ✓）；打孔池 **观测** ⚠️。


## A-CHARSUM-1（2026-09-27）⭐⭐ 证伪 ＋ 精化
**(甲″-iii) 证伪成功 ✓**：两坐标 extend→puncture 池（去重 662 码，全部过硬门 ✓）中出现 **3 例 $[I{:}W]=4$** 与**三级谱 $\{96{:}4,128{:}8,160{:}4\}$**（$|I|{=}16$、$|W|{=}4$，陪集值 $[96,128,128,160]$）⟹ **A-INVOL-1 的 $[I{:}W]\le2$ 与 A-FEAS-1 的"单级／两级"二分均被限界** ✗（降级为**一坐标 pool 的规律**）。
**(CU-1) 精化律 ✓✓（662 码全中）**：$[I{:}W]{=}1\Rightarrow1$ 值（566 例）、$=2\Rightarrow2$ 值（93 例）、$=4\Rightarrow\mathbf 3$ 值（3 例）；陪集值成**等差数列**、多重度 $=C(k',\cdot)$（$1{:}2{:}1$）⟹ $\delta=f-\bar m$ 是 $k'{=}\log_2[I{:}W]$ 个**独立线性特征之和** ⟹ **两级律 $=k'{=}1$ 特例，单级 $=k'{=}0$**。$J=\sum_j e_jm_j^2-v_0^2$ 恒等式不变 ✓。


## A-CHARSUM-2（2026-09-27）⭐⭐ 模型 ＋ J 闭式
**特征和模型 ✓**：$\delta=f-\bar m=a\sum_{j=1}^{k'}\chi_j$（独立 $\mathbb F_2$-特征，等幅 ✓）⟹ $f_r=\bar m+(2r-k')a$、$e_r=\binom{k'}r|W|$ ⟹ $k'{=}0$ 单级、$k'{=}1$ 两级 $1{:}1$、$k'{=}2$ 三级 $1{:}2{:}1$ ✓（三级例 $\{96^4,128^8,160^4\}=128+32(-1,0,+1)$ ✓）。
**J 闭式 ✓**：$J_{\rm all}=|W|(2^{k'}\bar m^2+2^{k'}k'a^2)$，$J_{\rm int}=J_{\rm all}-A_1^2$ ✓（逐例手工核对：$\{128^{16}\}\to245760$ ✓、$\{112^8,144^8\}\to245504$ ✓、$\{96^4,128^8,160^4\}\to270336$ ✓）⟹ **$J$ 塌缩为单参数 $a$** ✓。
**推导状态**：$k'{=}1$（Vasil'ev 支）**已推导** ✓（$f=X*C$、$X$ 在 $W$ 上均匀 ⟹ $W$-不变；$C\subseteq V=W\sqcup(9{+}W)$ ⟹ 两级）；$k'{=}2$（两坐标打孔支）**观测** ⚠️。
**脚本 bug 更正 ✓**：检验脚本重复扣减 $f(0)^2$ 致假失败 0/662；手工核算全吻合 ✓。


## A-WALSH-1（2026-09-27）⭐⭐⭐ 原子命题成立
**商群 $Q=I/W$ 上的高阶 Walsh 审计 ✓✓**：对池内 **662 码**逐个计算，$N_{\ge2}=\#\{C:\exists S,|S|\ge2,\widehat F(S)\ne0\}=\mathbf 0$ ✓（分支 1 ✓）；**一阶等幅性 96/96 ✓** ⟹ $F=\bar X*c-\bar m=a\sum_{j=1}^{k'}\chi_j$ **恰好成立** ⟹ 二项式谱与 $J$ 闭式成为**模型内推论** ✓✓。
**剩余唯一待证命题 ✓**：从 **extend→puncture ＋ $X*C$** 的代数结构推出「$Q$ 上二阶及以上 Walsh 系数恒为 0 且一阶等幅」（等价：$c$ 的分布只含一阶 Fourier 分量）。
$k'$ 分布：$\{0{:}566,1{:}93,2{:}3\}$。


## A-PROOF-1（2026-09-27）⭐⭐
**已推导 ✓**：$\widehat X$ 支撑于 $W^\perp$ ⟹ $\mathrm{supp}\,\widehat f\subseteq W^\perp$ ⟹ $f$ 是 $W$-不变 ⟹ $f(g)=32\sum_{u\in W}c(g\oplus u)$。
**$k'{=}1$ 分支 = THEOREM ✓✓**：$\mathrm{supp}(c)\subseteq V=W\sqcup(9{+}W)$（由 $\beta(H_7)\subseteq V$ 与 $15\in V$）⟹ 两级、$v_1+v_2=512=2\bar m$、多重度 $m/2$ 各一 —— 完整推导 ✓。
**$k'{=}2$ 缺口 ⚠️**：annihilation（$\widehat c(S)=0,\ |S|\ge2$）未从构造推出；$N_{\ge2}=0/662$ 为经验证据。**判定**：A-WALSH-1 = **强 SUPPORTED**（$k'{=}1$ 已升 THEOREM），**不包装为定理** ✓（遵唐先生 STOP 条件）。


## A-H7WALSH-1（2026-09-27）⭐⭐
**基案 16 点 $c$-计算 ✓✓**：$\mathrm{supp}(c)=\beta(H_7)=\{0,4,11,15\}\subseteq V$；计数 $(5,4,4,3)=\mathbf{(4,4,4,4)+(+1,0,0,-1)}$ ⟹ 按 $W$-陪集聚合 $(9,7)$ ⟹ $f=(288,224)$ ✓（与实测一致）。
**$k'{=}2$ 反例同模式 ✓✓**：$W$-陪集值 $[96,128,128,160]$ ⟹ $c$-质量 $[3,4,4,5]=\mathbf{(4,4,4,4)+(-1,0,0,+1)}$ ⟹ **同一"均匀 ＋ 单个 $\pm1$ 扰动"** ⟹ $Q$ 上 Fourier 支撑 $\subseteq 2$ 个一阶特征 ⟹ **二阶 Walsh 恒零**。
**归约 ✓（本档最重要）**：原子命题被归约为 **16 点级命题**——"$c$ 在 $W$-陪集上的质量 = 均匀 ＋ 单个 $\pm1$ 扰动"（等价：$\lambda$ 对 $\beta$-纤维的扰乱恰等量相反）。边界：该命题**未证** ⚠️（仍标强 SUPPORTED；$k'{=}1$ 已 THEOREM）。


## A-H7CLOSED-1（2026-09-27）⭐⭐⭐ 单缺陷定理
**16 点闭式 ✓✓**：$\beta$ 线性、$\mathrm{im}\,\beta|H_7=\{0,4,11,15\}$ ⟹ $c(a)=n_a^0+n^1_{a\oplus15}$。
**单缺陷定理 ✓✓（16/16 验证）**：$\lambda=1-\delta_{u_0}\Longrightarrow c=(4,4,4,4)+\delta_{\beta(u_0)}-\delta_{\beta(u_0)\oplus15}$ ⟹ 「均匀 ＋ 单个 $\pm1$ 扰动」为**定理**（该类）。
**annihilation 的 Fourier 一步 ✓✓**：$\widehat{(\delta_a-\delta_{a\oplus15})}(\chi)=\chi(a)(1-\chi(15))$ ⟹ 支撑 $=\{\chi:\chi(15)=-1\}$ **恰 2 元** ⟹ $\widehat F(S)=0\ (|S|\ge2)$ ✓（$k'{=}2$ 即 4 点商群上恰 2 个一阶特征）。
**两案例同一机制 ✓✓**：基案 $\lambda=\mathbf 1\iff u_0{=}0\Rightarrow(5,4,4,3)$ ✓；$k'{=}2$ 反例之 $c$-质量 $[3,4,4,5]$ 恰为 $\beta(u_0){=}15$ 之单缺陷像 ✓。
**状态**：$k'{=}1$ = THEOREM；$k'{=}2$ = annihilation 已证**条件于单缺陷类** ＋ 类归属观测 ⚠️。


## A-RESTART119-1（2026-09-27）
**强制恒等式 ✓**：任意 $|C|=119\wedge B_1(C)=\mathbb F_2^{10}$ 有 $E=\sum_x(b(x)-1)=\mathbf{285}$ ⟹ 「$E\ge286$」**等价于**「119-码不存在」（＝P1 本身）。
**直击档案 ⚠️**：该路线已在 `PROPAGATION-2026-09-26`：传播引理**已证** ✓（$|C\cap S_2(m)|\ge\lceil(n-2)/2\rceil$）但 **ladder 被数值证伪** ✗，且——关键——**不聚合** ✗（不同中点可共享 $z$）⟹ 「二阶传播 ⟹ $E\ge286$」形状**不成立** ✗。
**可容许性判据 ✓**：$E$ 是 $\delta$-型泛函 ⟹ 被 profile 恒等式**钉死**（`SUM-P1P4`／`AMEND-30`／`GAPTHEOREM` 十类）⟹ 唯一可容许者 ＝ **支撑敏感（跨中心）**不等式（`FAILSET`／`SCOL` 二类）。
**状态**：$K(10,1)=119$ 保持 **UNKNOWN**；结构路线未闭合；**不写**禁止表述。


## A-TRIPLE119-1（2026-09-27）
**(119-甲)**：**星型约束 ✓**（$x_0$ 的覆盖者必在 $B_1(x_0)=\{x_0\}\cup\{x_0+e_j\}$ 内 ⟹ 距离型只有 $(1,1,2)$ 或 $(2,2,2)$）；**无共享强制 ✓**（$x_0\notin C$ 时邻居对 $(i,j)$ 强制互异点 $e_i\!+\!e_j$，各 $b\ge2$ ⟹ 本星强制 $\ge2+\binom b2$）。
**全局退化 ⚠️→STOP**：求和得 $\sum_{b\ge3}\binom b2\le\sum_{b\ge2}\binom b2$ —— 两端皆 $\delta$-型 ⟹ 被 profile 恒等式钉死 ⟹ **δ-type convergence → STOP**（**第 13 次同向收敛**）；与 `PROPAGATION`「不聚合」同根（sharing）。
**残件**：星内"无共享"为**坐标级身份数据**；唯一未退化方向 = 叠加 `SCOL` (F-1) 行闭合机制（支撑型、带坐标身份）。$K(10,1)=119$ 保持 **UNKNOWN**。


## A-SCOL0-1（2026-09-27）
**SCOL-0 = 否定（不可解耦）🔴**：(F-1) 拆两件 —— 件①"$e_l$ 的覆盖者 = 行 $l$ 权-2 码字" **Q=1-free 但平凡**（由 $d(c,e_l)\le1\iff \mathrm{wt}(c)\in\{0,1,2\}$ 直接给出）；件②"$b(e_l)\le2$"**才是全部内容**，而它在 SCOL 中来自 STAR3 的 **Type III 排除**（$Q{=}1$ 分支中唯一 $b{=}3$ 点 $z$ 的配置）⟹ **依赖 $Q{=}1$** ✗；一般 $M{=}119$ 时 profile 未定 ⟹ $b(e_l)$ 无一致上界 ✗。
**Q=1-free 残件 ✓**：普适对覆盖约束 $b(x)=2,\ W(x)=\{c,c'\}\Longrightarrow C\cap B_1(x)=\{c,c'\}$（即档案**中点引理**）。
**SCOL-1 叠加 → 退化 ⚠️→STOP**：用于星型点 $z_{ij}$ 即得 $|C\cap S_2(z_{ij})|\ge\lceil(n-2)/2\rceil=4$ ＝**档案传播引理**（不聚合、ladder 已证伪）⟹ 重述而非新障碍 ⟹ **第 14 次同向收敛**；建议 119 不再沿"局部强制→支撑禁制"形状推进。


## A-CONGRUENCE-1（2026-09-27）
**(a) 全局同余可达性审计 → 四层坍缩 ⟹ 第 15 次同向收敛 ✓**。
**前提纠正 ⚠️**：$|B_1(c)\cap B_1(c')|=2$ 对 $d\in\{1,2\}$、$0$ 对 $d\ge3$（档案 FAILSET §2 ✓）⟹ $\sum_x\binom{b(x)}2=2(A_1+A_2)$，故正确对象 $P:=A_1+A_2=\tfrac12\sum_x\binom b2$（不是"距离-2 对数"）。
**(HB-1) 模 2 平凡性引理 ✓（新）**：$\widehat b(\chi)=(11-2w(\chi))\widehat C(\chi)$，乘子 $11-2w$ 全为**奇数** ⟹ 模 2 全可逆 ⟹ **模 2 不产生新信息** ✓。
**G-I/G-III/G-IV 坍缩 ✗**：$\sum b$、$\sum\binom b2$、$\sum\binom b3$ 皆 profile 决定；profile 已知约束仅 $\{\sum N_k=1024,\sum kN_k=1309,N_1\ge M\}$；G-IV 的 $\sum_{\rm triples}|\cap B_1|$ 读法给出 **profile↔坐标耦合等式**（非对称于同余 ✗）。
**判定 = B（坍缩）**：全局整数/同余形状正式封口 ✓；边界："**未发现 ≠ 不存在**" ✓；$K(10,1)=119$ 保持 UNKNOWN。


## A-C3-1（2026-09-27）
**前提纠正 🔴（定理级）**：对三个互异码字，$|\cap_3|\in\{0,\mathbf 1\}$ —— **不可能为 3** ✗。证明：$\cap_3\subseteq B_1(0)\cap B_1(u)$（$|\cdot|\le2$），且那 2 点中至多一个落在 $B_1(v)$ 内（否则 $v=u$ ✗）。故用户提案 $T=3N_\square+N_{\triangle_2}$ **不成立**；档案已有正确版：$|\cap_3|\le1\Longrightarrow\sum_x\binom{b}3=|\mathcal T|$ **恰等** ✓。
**正确耦合 (C3′) ✓**：$\sum_kN_k\binom k3=\#\{\{c_1,c_2,c_3\}:\mathrm{wt}(u),\mathrm{wt}(v),\mathrm{wt}(u\!+\!v)\le2\}$（左 profile、右坐标几何）。
**三元组分类 ✓**：星型（$u{=}e_i,v{=}e_j$ 或 $u{=}e_i,v{=}e_i{+}e_j$，支撑并 $\le2$）／带状（$u{=}e_i{+}e_j,v{=}e_i{+}e_k$，支撑并 3）／**非可达**（不相交 2-集 ⟹ $\mathrm{wt}(u{+}v){=}4$ ⟹ 交 $\varnothing$，贡献 0）。
**判定 = 坍缩（第 16 次同向收敛）**：(C3′) 两侧由恒等式相连 ⟹ 右侧非独立量；自然独立界（三角计数）对相关 $T$ 值太松（$Q{=}1$ 时 $T{=}1$）⟹ 未得独立坐标不变量 ⟹ **封口** ✓。$K(10,1)=119$ 保持 UNKNOWN。


## A-INCIDENCE-1（2026-09-27）⭐⭐
**关系全表 ✓**：$A=T\,P_C$（$T=I+\sum_i\sigma_i$）；$b=A\mathbf 1_M=T\mathbf 1_C$；$\boxed{A^{\mathsf T}A=(n{+}1)I+2\mathrm{Adj}(G_{\le2}(C))}$（**纯码侧距离结构**）；$(AA^{\mathsf T})_{x,y}=|B_1(x)\cap B_1(y)\cap C|$；$\widehat T(\chi)=n{+}1{-}2|\chi|$ 无零 ⟹ $T$ 可逆（$n{=}10$：$\{11,9,7,5,3,1,-1,-3,-5,-7,-9\}$）。
**新定理 ⭐**：$0\in\sigma(A^{\mathsf T}A)\iff-\tfrac{n+1}{2}\in\sigma(\mathrm{Adj})$；$\mathrm{Adj}$ 整对称 ⟹ 特征值皆代数整数 ⟹ **$n$ 偶时 $A$ 列满秩 $=|C|$ ⟹ 映射 $C\mapsto b$ 单射（profile 决定码 ✓✓）**；对照：$n{=}1,C=\mathbb F_2$ 秩 1 < 2（故"偶"不可去）。
**定理级解释 ✓**：由满秩得 $\mathbf 1_C=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b$ **线性** ⟹ 唯一非线性 = Booleanity ⟹ **任何只用 $b$ 的证书自动等价原问题（不可松弛）** ⟹ 这解释了档案 M-1(CIRCULAR)／M-2A(CLOSED)／Fourier audit("坐标变换而非松弛") 三处封口。难处被定位为 **"哪些 $b$ 可实现"**（= P1-B BLOCKED 处）。


## A-INCIDENCE-FIX-1（2026-09-27）
**接受纠错 ✅**：$A_C$ 满列秩只给**固定 $C$ 内部**单射；反解 $\mathbf 1_C=(A_C^{\mathsf T}A_C)^{-1}A_C^{\mathsf T}b$ 需先知 $C$ ⟹ 原 §② 论证跳跃 ✗（抽象反例 $A{=}I,B{=}$ 交换阵 ✓）。
**校正定理 ⭐⭐**：$T=I+\sum_i\sigma_i$ 谱 $=\{n{+}1{-}2w\}$ ⟹ $0\in\sigma(T)\iff n$ 奇 ⟹ **$n$ 偶时 $\mathbf 1_C=T^{-1}b$ ⟹ $C\mapsto b$ 单射**（与 $A_C$、$|C|$ 无关 ✓，比原版更强）；$n$ 奇可塌（$n{=}1$ 反例 ✓）。
**Booleanity Gate 🔴 可证等价**：$T^{-1}$ 双射 ⟹ $\{b:T^{-1}b\in\{0,1\}^{1024},\sum{=}119\}$ 恰为像集 ⟹ **"$b$ 可实现" $\iff T^{-1}b$ Boolean，与原问题逐字等价（无松弛）** ✗（与档案 Fourier audit 判定一致）；自然松弛皆在档（M-1 CIRCULAR／能量条件 profile／Delsarte CLOSED）⟹ 该形状封口 **（第 18 次）**。


## A-A5-1（2026-09-27）
**A5 审计（$R_{xc}=f(c)\delta(x)$）**：**边际退化 ✗** —— $\sum_cR_{xc}=M\delta(x)$（$\delta$-型）、$\sum_xR_{xc}=285f(c)$（$f$-型），新信息只能藏在联合结构，而平移不变权重一平均即失。
**两条新恒等式 ✓**：$\boxed{\sum_{x\in C}\delta(x)=2A_1}$（由 $\sum_{x\in C}b=M+2A_1$）；$\boxed{\sum_x b\delta=4(A_1+A_2)}$（由 $\sum_{x\in B_1(c)}\delta=2(d_1(c)+d_2(c))$）⟹ **$\sum_x\delta^2=4(A_1+A_2)-285$**（surplus 二阶矩被钉死 ✗）。
**判定**：一切平移不变加权和退化为 $(M,A_1,A_2)$ 函数 ⟹ 无独立不变量 ⟹ **A5 封口（第 19 次）**；AMEND-35 第(3)问答不出 ⟹ STOP ✓。
**A2 预警 ⚠️**：仅放松 rank-1 而保留 $\{Y\succeq0,Y_{xx}=f_x\}$ 的松弛**为空**（任意 $f\ge0$ 取 $Y=ff^{\mathsf T}$）⟹ A2 须带坐标级条目约束（= Booleanity 回归）；下一步更适合直接审 **A4（局部一致性 = 真松弛 ✓）**。


## A-A4-1（2026-09-27）
**关键钉死 ⭐**：覆盖约束 $(Tf)(x)\ge1$ 涉及**整颗星 $B_1(x)$（11 点）** ⟹ 真正的局部对象＝**星边际**；星-星 overlap 仅在 $d\le2$ 且 $\le2$ 点。
**$k{=}2$ 理论封口 🔴**：成对边际的全部信息 $=\{$1-点密度$\}\cup\{d{=}1,2\ \text{成对相关}\}$ ⟹ 恰可定出 $(A_1,A_2,M)$ ⟹ 按 A4-GATE **STOP** ✓。
**$k\ge3$ 被支配 ⭐⭐**：$k$-窗口边际松弛 $\mathcal L_k$ 属 **Sherali–Adams 型**，而 $\mathrm{SA}_k\subseteq\mathrm{SOS/Lasserre}_{O(k)}$ ⟹ $\mathcal L_k\subseteq$Lasserre ⟹ 同阶 Lasserre 更强 ⟹ **A4 全族不能在 Lasserre 之外给新证书** ✗（档案实测 Delsarte+SDP = **105.2223** < 119 ✓）。
**真正收获 ✓**：定位唯一活口 = 档案 **L3B Level 4（$n{=}10$，$1024\times1024$ PSD）"BLOCKED pending reduced implementation"**，且**两个后台 run（tidal-glade／marine-nudibranch）从未轮询** ⚠️ —— 这是 119 线上唯一具体、未完成、可推进的对象（计算型）。


## A-LEDGER119-1（2026-09-27）
**(乙) 清账结论**：运行环境干净（仅 gateway ✓，无 python3 残留/core ✓）；**两个后台 run（tidal-glade／marine-nudibranch）无日志/产物 ✗**（work 树无 reduced-SDP/bmat/Terwilliger 产物）⟹ **低成本恢复路已尽，须重算** ✓。
**剩余项定位 ✓**：L3B 线今日 12:01–12:07 有进展（A-L3B-2 ✓／B-L3B-1 ✓／**C-L3B-1 Lasserre $\eta$ 闭式**，D1=0 纯重建）；**AC-5 ⚠️ 约定未钉死**（论文 $d=|w|$ vs 作者代码 $\texttt{dist}=d(v,w)$）⟹ 唯一剩余工程项 = **R2（块约化 SDP ＋ $(\eta,\lambda)$ 索引约定）**，且其 $\texttt{bmat}$ **border-assembly bug 已知**（$\texttt{cp.vstack}$ 尺寸 6 vs 5，$k{=}0$ bordered 块）。
**期望收益（诚实）**：完成 R2 ⟹ 关闭 **Level 3（复现/验证层）**；**不**直接产出 $\ge120$ 新界（档案 SDP = 105.2223 < 119）。


## A-P1REAUDIT-1（2026-09-27）
**E-陈述纠错 ✅**：$E=\sum_x(b(x)-1)=11|C|-1024$ 是 $|C|$ 的**纯函数**（与覆盖无关）⟹ 「$E\ge286$」$\iff |C|\ge120$ ⟹ **与「119-码不存在」不是同一命题** ✗（我此前"等价"用词错误）；正确用法=**充分**路线（覆盖 ⟹ $E\ge286$ ⟹ 矛盾 ⟹ 不存在）。
**模 11 定理 ⭐⭐**：$T$ 特征值 $11-2w$ ⟹ $\bmod 11$ 下 $\equiv-2w$ ⟹ 唯一零特征值 $w{=}0$ ⟹ $\boxed{\ker(T\bmod 11)=\mathrm{span}\{\mathbf 1\}}$ ⟹ $Tg\equiv0\iff g\equiv c\mathbf 1$。
**$g$-形审计 ⭐**：$f=\tfrac1{11}\mathbf 1+T^{-1}\delta$，$g=11T^{-1}\delta\in\{-1,10\}$；由模 11 定理 ⟹ **线性内容恰为整数/多重覆盖松弛 $\{f\in\mathbb Z^{1024}:Tf\ge1,\sum f{=}119\}$，其余=Booleanity** ⟹ **$g$-形不产生新必要条件**（路线 A 定理级封口，第 21 次）；且解释其成因。
**残余 ✗**：分数松弛在 119 可行（$1024/11$ ✓）；整数松弛 119-可行性本档**未判定** ⚠️（需计算）；故残余 = **不可约整数性** ⟹ 路线 B（高阶 Lasserre/SOS）为唯一同族残余。


## A-INTRELAX-1（2026-09-27）⭐⭐
**等价定理 ✓✓（三行）**：$f\in\mathbb Z_{\ge0},\ Tf\ge1$ ⟹ $\mathrm{supp}(f)$ 是 0-1 覆盖码且 $|\mathrm{supp}f|\le\sum f$ ⟹ $\boxed{\min\{\sum f\}=K(n,1)}$ ⟹ **整数松弛不是松弛** ✗；但给出**更宽的可搜索形式**（任一 $\sum f{=}119$ 解的支撑直接是 119-覆盖码 ✓✓）。
**小 $n$ 验证 ✓✓（HIGHS）**：ILP 最优 $\sum f$ = $4/7/12$ 对 $n{=}4/5/6$，**与 $K(n,1)$ 完全相等**，且**最优解恒为 0-1 值** ✓；$n{=}5$ 穷举 $C(32,6)$ 全部 6-子集**无一覆盖** ⟹ $\sum f{=}6$ 不可行 ✓。
**$n{=}10$**：ILP（1024 变量／1024 约束 ✓，HIGHS ✓，后台 setsid＋pyguard）已启动 ⏳；三结局：(i) $\le119$ ⟹ 取支撑得 119-码（正向突破）(ii) 不可行 ⟹ $K\ge120$ (iii) UNKNOWN。


## A-INTRELAX-REFILE-1（2026-09-27）✅ 改档
**A-INTRELAX-1 正式改档**：由「整数松弛」改为 **「整数覆盖的等价重参数化」（equivalent reparameterization）** —— 依据 $\min\{\mathbf 1^{\mathsf T}f:Tf\ge1,f\in\mathbb Z_{\ge0}\}=K(n,1)$ ⟹ 最优值相同、可行集对应 ⟹ **既不变弱也不变强** ⟹ **不得列入松弛族**（profile／$A_d$／local-SA／Lasserre ✗）；正确定位 = 面向 solver 的**重述**，服务同一决策问题 **P1：119 feasibility**。
**状态锁定 🔒**：唯一运行 = 该 ILP（HIGHS，后台，不轮询）；暂不做：第二 CP-SAT／Level-4 Lasserre／R2 修复／新 $\delta$ 恒等式／第 22 个候选机制。
**结果分叉**：$\sum f{=}119$ ⟹ 取支撑得 119-cover（正向突破）；证 optimum $=120$ ⟹ P1 完成；UNKNOWN ⟹ 才考虑 Level-4。
**验收协议**：若得 119，**不得**只采信目标值，必须取 $C=\mathrm{supp}(f)$ 并独立验证 $|C|{=}119\wedge\forall x:|C\cap B_1(x)|\ge1$ ✓。
**旁线审计**：变量域更宽（$\mathbb Z_{\ge0}$）⟹ 每 node LP 更松 ⟹ 通常更易解 ✓；但任一整数解 ⟹ $\mathrm{supp}(f)$ 即 0-1 覆盖码 ⟹ **不引入新对象类型**，且因 $K_{\mathbb Z}=K$ 也**不能给出更强证书** ⟹ 净价值 = **搜索效率**，非新信息源。


## A-PROJCUT-1（2026-09-27）
**投影割正确形式 ✓**：子立方 $S=\{x:x|_U=w\}$，$F(v)=\sum_{c:c|_U=v}f_c$ ⟹ $(1+|V|)F(w)+\sum_{i\in U}F(w\oplus e_i)\ge2^{|V|}$（有效 ✓，小 $n$ 全 $\le K$ ✓；首版错误形式已自查修正 ✗→✓）。
**投影割 = covering 约束之和 ⭐⭐**：$\sum_{x\in S}\sum_{c\in B_1(x)}f_c\ge|S|$，左端 $=(1+|V|)F(w)+\sum_iF(w\oplus e_i)$ ⟹ 逐项相同 ⟹ 投影割**不是新割** ✗。
**一般命题 ⭐⭐**：任何 $\lambda\ge0$ 的 $\sum_x\lambda_x(\text{covering at }x)$ 都是原约束正组合 ⟹ **恒被蕴含** ⟹ **全部正系数和式型割（投影／子立方／局部和式）先验上不可能改进 LP** ✗✓（解释 A4/SA 之无力为**结构性**）；有用割必须来自锥外（Boolean/整数性或 SOS 二次层）✓。
**实测**：$n{=}4..8$ 加割后 LP **完全不变**（+0.0000）✓。
**状态锁定**：ILP RUNNING ＋ projection-cut STOP；不增加 119 计算 ✗；ILP 若 UNKNOWN ⟹ 再启专用随机搜索（先做 source-first 算法核验 ✓）。


## A-MIPRUN-1（2026-09-27）
**bound 表述纠错 ✅（接受唐先生 ✓）**：$94.027>93.09=2^{10}/11$ ⟹ 当前 MIP 的节点松弛＋切割体系较裸 LP 提升约 $0.94$ ✓（**具体运行观察**）；但**不是**对任何 relaxation family 理论最优值的证明 ✗（有限时间 bound ≠ 族下确界 ✗）—— 撤回我"线性/对偶侧根本够不着 119"之过度主张 ✗。唯一可确认：$94.027\ll119$ ⟹ 本次运行未显示接近 P1 迹象 ✓。
**分叉锁定 🔒**：单次 exact MIP 跑满 900s（成本已付 ✓，无需截断 ✓）；终态后：① $\le119$ 整数解 ⟹ 取 $C=\mathrm{supp}(f)$ ＋ **独立验证** $|C|\le119\wedge\forall x:|C\cap B_1(x)|\ge1$ ⟹ P2 witness（方成立 ✓）；② BestBound 远低于 120 或 UNKNOWN ⟹ **MIP STOP** ⟹ **source-first 核验后转专用随机搜索** ✓。
**区分 ✓**：MIP = 证 feasibility/infeasibility；专用搜索 = **直接构造 119-word witness** ⟹ 后者属明确 **P2 construction attack**，非"换 solver 再赌" ✓。
**运行记录 ✓**：int10c.py（min Σf, Tf≥1, f∈{0,1}, f₀=1, HIGHS 1.15.1, 900s）—— 51.1s: bound 94.027/sol 150; 181.7s: bound 95.312/sol 139; 232.9s: bound 95.318/sol 139, gap 31.43% ✓（对称检测找到 10 生成元 ✓ 印证平移破缺 ✓）。


## A-MIPRUN-2（2026-09-27 16:36）⭐
**终态 ✅（分支 ② 执行 ✓）**：`int10c.py` 跑满 900.17s ⟹ **Status = Time limit reached**；Dual=99.0，Primal=138，Gap=28.26%，Nodes=3751 ⟹ 无 ≤119 解 ✗ → **MIP STOP ✓**（Dual 为有限时间 bound ⟹ 不得当作「119 不存在」之证明 ✗）。详 `MIPRUN2-2026-09-27-int10c-terminal-and-source-first-gate.md`。
**source-first 核验 ✓（4 项）**：① `kamenetsky120.txt` 独立复核 = 120 词 / 0 重复 / 覆盖 1024-1024 ✓（基线成立）；② **`code119_candidate.txt` ✗ 无效** —— 119 词但 **17 点未覆盖**（生成于 2026-09-24 22:59，此前从未独立验证 ⚠️）⟹ 「历史 n=10,R=1 最好 = 120」维持 ✓；③ `tabu_np.py` 崩溃（IndexError 92/92）⟹ `np120.log` 的 k<120 行全部作废 ✗；④ `cp119.py`（CP-SAT, min Σx, hint）3600s = UNKNOWN，档案已锁「不得表述为 119 不存在」✓。
**新增结构发现 ⭐**：120-码删去私有覆盖最少的词 ⟹ k=119, **unc=2**；余词私有覆盖数 ≥2 ⟹ 单字替换 loss≥2 而 gain≤2 ⟹ **unc=2 是 1-flip 平台**（除非两未覆盖点距离 ≤2）⟹ 单字局部搜索（v4 实测 40s/8147 it 停在 unc=2）与历史 tabu（k=120, best unc=92）一致 ⟹ 突破须 **2-opt/k-opt 或退火** ✓。
**P2 首轮**：`work/k10/p2_119k_search.py`（k=119 固定、权重 breakout、900s 后台、日志 `/tmp/p2k119.log`）；**不启动额外 exact 119 计算** ✗；未得 witness 前不得表述「119 不可达」✗。


## A-MIPRUN-2（2026-09-27 · int10c 终态 ✅）
**终态（900s 到期 ✓）**：`STATUS=Time limit reached`；**dual(BestBound)=99.0**；**primal(BestSol)=138**；gap=28.26%；nodes=3751；LP iterations=1305041（strong br. 392661／separation 36391／heuristics 274720）✓。
**内部自检 ✓**：最优解 `|C|=138`，**逐点最小覆盖数 = 1** ⟹ **是合法覆盖码 ✓**（但 138 > 已知上界 120 ✗ ⟹ **无记录改进** ✗）。
**双界读数 ✓**：LP 93.09 → 节点松弛＋切割 **99.0**（+5.9 ✓，真实但不接近目标）；**99.0 ≪ 119** ⟹ 与 P1 相距约 20 ✗（**诚实标注：有限时间 bound ✗ 不等于族最优证明 ✓**）。
**分叉执行 ✓（按 SB-1 ②）**：**MIP STOP** ⟹ 下一步 = **source-first 核验后转专用随机搜索**（P2 construction attack；先核验：目标函数／接受规则／repair／历史 n=10,R=1 结果是否确为 120 ✓）；**不新增 119 计算** ✗。


## A-P2SEARCH-1（2026-09-27）
**(甲) 结论采纳 ✓**：历史路线 = construction + **SA** + **tabu/local search**；文献明确 $K(10,1)\le120$ 是**上界**（SA 只给上界 ✗ 不证最优）⟹ **不可写 $K=120$** ✗；**119 为真 P2 construction target** ✓（Östergård 1991 已有 60-word mixed code 改进该参数 ✓）。
**规范四要素 ✓（可复现）**：① **targeted repair 邻域**：取 $y\in H$，新位置 $c'\in B_1(y)$；被替换者 $c^\ast=\arg\min_c\#\{z\in B_1(c):\mathrm{cnt}(z){=}1\}$（唯一覆盖数最小 ✓）；② **tabu tenure** $\tau\approx10$–20 防来回交换；③ **SA acceptance** $\Delta\mathcal E\le0$ 接受，否则 $\exp(-\Delta\mathcal E/T)$，几何降温＋周期升温；④ $|H|{=}0$ ⟹ **立即独立验证 1024 点**（$|S|{=}119\wedge\forall x:|S\cap B_1(x)|\ge1$）⟹ P2 成立 ✓✓。
**实测记录 ✗**：两半构造（two 62-codes）= **124 词合法覆盖但不可约**（贪心删 0 句 ✗）、局部搜索 25.4 万迭代零改进 ⟹ 两半结构僵死 ✓；裸 SA（anneal.py，$m{=}119$，无 targeted repair/tabu ✗）已被本规范取代 ✓。
**判据红线 🔴**：找到 119 ⟹ P2 成立（真实 upper-bound dent ✓）；找不到 ⟹ **仅启发式负证据 ✗，绝不升级为 P1** ✓。


## A-P2VAL-1（2026-09-27）🔴
**自检门失败（决定性 ✓）**：已知 $K(10,1)\le120$ ⟹ $m{=}120$ 必可解；实测（targeted repair＋tabu＋SA）六次 restart 的 $\mathrm{best\_unc}$ = 34/28/34/28/31/25 ✗ **全部远未到 0** ⟹ **机制太弱 ✗** ⟹ **不能对 $m{=}119$ 作任何判断** ✗✓。
**三条实现路径均未达文献水准 ✓**：裸 SA($m{=}119$) best_unc 24–27 ✗；两半构造 124 词合法但**不可约** ✗；本档 targeted repair($m{=}120$) 25–34 ✗。
**归因 ✓（非数学结论 ✗）**：速度够（$8\times10^3$–$2\times10^4$ 步/秒 ✓），缺口在**邻域与能量设计**（能量只用 $|H|$ 无二阶项 ✗；邻域未做精确 $\arg\min$ 评估 ✗；tabu/温度表未调参 ✗；无种群／重扰动 ✓）。
**下一步 ✓（reproduction 优先）**：先把 $m{=}120$ 搜到 $h{=}0$ 以**证明实现达文献水准** ✓；达标后才做 $m{=}119$ ✓；否则升级为文献级实现 ✓。


## A-REPAIRSHARE-1（2026-09-27）
**第一层精确刻画 ⭐**：$0\notin C$，$C\cap B_1(0)=E_J$（$|J|{=}q$；**$C$ 无其它单位向量** ✓）⟹ **需求集** $\mathcal T_J=\{y:\mathrm{wt}(y){=}3,\ |\mathrm{supp}(y)\cap J|\ge2\}$，$|\mathcal T_J|=\binom q2(n{-}q)+\binom q3$ ✓（自检：$q{=}10\Rightarrow120$ ✓、$q{=}3\Rightarrow22$ ✓ ✓）。
**候选修正 ⭐**：可覆盖者为 weight 2/3/4；**weight-2 $e_p{+}e_q$ 覆盖 8 点**（$p,q\in J$ 时全属 $\mathcal T_J$ ✓）⟹ **$z_{ij}\in C$ 用 1 词修整壳（8 点 ✓）** ⟹ 唐先生 $\lceil\cdot/4\rceil$ 下界成立但偏松 ✗，真实 $\rho(J)$ 更小 ⟹ **第一层 STOP 被加强** ✓✓（最粗上界 $q{+}\binom q2\le55\ll119$ ✓）。
**第二层 = 唯一出口 ✓**：repair codewords 自带 11-壳 ⟹ 逐层记账；**目标精确化**：从覆盖假设推出 **excess $\ge286$**（⟹ 与恒等式 $E{=}285$ 矛盾 ⟹ P1 ✓✓；口径遵循"充分非等价"纠错 ✓）；若第二层退化为 $A_1/A_2/N_k/\delta$-型 ⟹ STOP ✓。


## A-HANDOFF119-1（2026-09-27 18:18）
**交接档**：`docs/HANDOFF-2026-09-27-119-line-session-handoff.md` ✓（自包含：状态／21 条封口／等价重参数化／投影割／MIP 终态／搜索代际记录／卡点／定义／唯一动作／红线／文件命令／文献 ✓）。
**当前卡点 ✓**：要得 $124\to123$ 需存在 $|S|{=}124,h{=}0,R\ge1$ 的状态 ⟹ cleanup 立即给 123 ✓；现状只观测 $r{=}k{+}1$ ⟹ 瓶颈 = **repair 能否产出等基数带冗余的 124 码** ✓（非"能否删"——已证能删 ✓）。
**下一轮唯一动作**：四事件计数 ＋ 新增 **neutral 且 R≥1**（判定性事件 ✓）。
**阶段**：P2 reproduction（搜索实现未达文献水准 ⟹ 无 P1/P2 结论 ✓）。

## A-KOPT-SHIFTAUDIT-1（2026-09-27 18:47）
**位移能力审计档**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` ✓（D1=1：含一条小引理 ✓）
**仪器纠错 ✓**：kopt3 的 `maxR=0` 在 cleanup **之后**统计 ⟹ **恒等式假象** ✗；改为 cleanup **之前**测 $R$ ＋ 四事件拆分 ✓
**发现 ①（kopt4 读法作废 ✗）**：`distinct124 = 1` 在 **172,100** 次等基数 replacement 之上 ⟹ delete-refill repair ＝ **恒等算子** ⟹ "173k 次替换"**零位移** ⟹ kopt4 负结论强度 $\approx0$ ✗
**发现 ②（真实读数 ✓）**：冗余可产生，但只在 overshoot 层 —— `distinct125R = 63`（$|C|=125,R\ge1$），cleanup 删 1 词回落 124 ✓
**发现 ③（可证 ✓ 小引理）**：$|A_c|\ge3\Rightarrow\bigcap_{z\in H_c}B_1(z)=\{c\}$；本码 $\min|A_c|=3$ ⟹ **1-for-1 swap 不存在**（124/124 全刚性，候选总数 0 ✓）；配合计数 $P\ge684$（实测 757 ✓）⟹ 每词私有点均值 5.5（实测 6.10 ✓）
**发现 ④（k=2 亦不可动 ✓）**：`tries=68,794 ｜ moved=0 ｜ mobility=0.0000`（穷举判定 ✓）；推论：$d(c_1,c_2)\ge5\Rightarrow$ 不可动 ✓
**净结论**：三代数（A delete-refill／B 1-for-1／C k=2）在**基准码上全部零位移** ⟹ 基准 124 码**强局部刚性** ⟹ 位移须 **k$\ge$3 交换** 或 **多起点** ✓（**机制面**结论 ✗ 非码空间结论 ✗）
**唐先生原判定事件（$|C|=124,h=0,R\ge1$）仍未观测** ⟹ 但**未观测之原因已精确定位 ＝ 装置无法移动** ✓
**红线**：只记"该邻域未找到" ✗ 不推下界 ✗；120 是**上界** ✗；`/tmp/cov`＝design 搜索器分账 ✗

## A-KOPT-K3RIGID-1（2026-09-27 19:00）
**k=3 真交换【完备判定】**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §4.6／§5.5 ✓
**规格（唐先生 18:52 拍板 ✓）**：$C'=(C\setminus A)\cup D$，$|A|=|D|=3$，$A\subset C$，$D\subset\mathbb F_2^{10}\setminus C$（**严禁 delete-refill 伪装** ✗）；$m:=$ 覆盖空洞 $E$ 所需 $C$-外词最少个数 ⟹ $|C'|=121+m$；**只做 k=3，不扩 4,5** ✓
**完备读数 ✓**：`tries = 310,124 = C(124,3)` ⟹ **完备** ✓；可证豁免 286,317（任一对 $d\ge5$）；近距 23,807（三对全 $\le4$）**全部 immobile ($m\ge4$)**；`m0=m1=m2=m3=0`、**`moved=0`**、`R>0=0`、`distinct124=0`
**独立复核 ✓（换算法）**：`/tmp/kopt11_verify.py` 穷举 $\binom{\mathrm{pool}}{3}$（$|\mathrm{pool}|=110$–$151$）抽检 40 个（近距 20 ＋ 豁免 20）⟹ **40/40 "无 3-覆盖"** ✓（与主判定算法不同：$O(11^2)$ 逐层交集 vs 全枚举 ✓）
**强于 `moved=0` 的精确陈述 ✓**：$\forall A\subset C,|A|{=}3,\ \forall D\subset\mathbb F_2^{10}\setminus C,|D|\le3$：$(C\setminus A)\cup D$ **不是覆盖码** ⟹ 从基准码出发 $|C'|$ 不可能降到 $\le124$ ✓
⚠️ **约定**：$D\cap C=\varnothing$（不得把 $A$ 中的词放回 ✗，否则 $D{=}A$ 退化为恒等）
**局部刚性链闭合 ✓**：$k=1,2,3$ exchange 在基准码上**全部 `moved=0`**（1 可证／2 穷举 68,794／3 完备＋复核）
**本码距离直方图**（7626 对）：$d{=}1{:}40,\ 2{:}179,\ 3{:}1005,\ 4{:}1761,\ 5{:}1781,\ 6{:}1477,\ 7{:}942,\ 8{:}361,\ 9{:}75,\ 10{:}5$；$\min$ dist $=1$ ✓
**红线** 🔴：只归档为"**该 $k\le3$ 交换邻域中不存在位移**" ✗，**绝不**转译成 $K(10,1)>124$ ✗；未触及 120／119 任一端 ✓

## A-KOPT-K4PROBE-1（2026-09-27 19:11）
**k=4 压缩机制 ＋ 成本量化（探针阶段已冻结 ✓）**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §4.7／§5.6 ✓
**LB1 判废（有证明 ✓）**：$E\subseteq\bigcup_{a\in A}B_1(a)$ ⟹ 每半径-1 球簇至多 1 个两两 $d\ge3$ 的点 ⟹ $\mathrm{LB1}\le k$ ⟹ $k{=}4$ 时 $\le4<5$ **逻辑上不可能豁免** ✗（STOP ✓）
**LB2（簇不相交）**：$H_{a_i}$ 各需 $\ge2$ 词；不可共享簇词集不相交 ⟹ $\mathrm{LB2}=2t$ ✓（不优化 ✓）
**安全组合必要条件**（只可 false-positive ✓）：含 3 个两两 $d\ge5$ 的词 ⟹ 3 簇互不可共享 ⟹ $m\ge6>4$ ⟹ 豁免 ✓
**200,000 抽样（seed=20260927）✓**：三团豁免 101,701 (50.85%)｜LB2>=6 豁免 63,090 (31.50%)｜需真判 35,209 (17.60%) → 外推 ≈1.65e6｜**`moved=0`（仅抽样探针 ✗ 非完备结论）**｜**交叉一致性检查失败 0** ✓✓（`can_cover(E,3)` 恒 False ⟹ 与 k=3 完备互相一致 ✓，**不是**独立数学证明 ✗）
**exact 内核提速 ✓**：去 `used`（掩码已隐含排除）＋ fail-first ＋ $(E,\mathrm{depth})$ 记忆化 ⟹ 均 4,412→1,273µs、最大 110,709→3,556µs ✓
**读数分布**：$|E|$ 16→35（众数 24）；$|Q(E)|$ 122→198（众数 160）✓
⚠️ **算术更正**：$C(124,4)=9{,}381{,}251$（会话中的 9,307,766／9,183,626 均误 ✗）
**进行中**：kopt14 `full`（全 $9{,}381{,}251$ 四元组，单核 $\approx$34 分钟）⟹ 结果待补 ✓
**分叉 ✓**：$m_4=0$ ⟹ 归档"该基准码 $k\le4$ 真交换邻域零位移"；$m_4>0$ ⟹ **立即停批**，逐个审计 witness $(A,D)$／覆盖性／新状态／$R(C)$，且先问 $\texttt{moved}\Rightarrow R>0?$ ✓
**红线** 🔴：只命名"该 $k\le4$ 交换邻域中不存在位移" ✗；**绝不**推 $K(10,1)>124$ ✗

## A-KOPT-P3-INCIDENCE-1（2026-09-27 19:24）
**P0–P5 链审计 ＋ P3 机制方向 ✓**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §4.8／§5.7 ✓
**卡点定位 ✓（唐先生 19:23）**：**＝P3 collision（碰撞机制）**，**不是 P1** ✗；P0✅／P1❌（非当前目标）／P2✅（124 词 $h{=}0$）／**P3🔴**／P4-P5⏸
**P3 两层**：低阶等基数出口（$k\le3$ 已堵死 ＋ $k{=}4$ 收尾）vs **真正降基数出口**（$124\to123$）✓
**两个事件分开 ✓**：$\tau(E(A))\le4\Rightarrow124\to124$；$\tau(E(A))\le3\Rightarrow124\to123$ ⟹ **P3 应直接盯 $\tau\le3$** ✓
**k=2 【真完备】✓（kopt15）**：全 $C(124,2)=7,626$ 对枚举，$\tau\ge3$ **全部** ⟹ 无等基数也无降基数出口 ✓（**修正**：kopt9 的 68,794 是随机抽样 ✗ 非完备；现升级为真完备 ✓）
**下一项机制（拍板 ✓）**：**不再发明 LB1/LB2** ✗；改把 $E(A)$ 转成 **incidence hypergraph**（左：$x\in E(A)$；右：$z\notin C$；边 $x\sim z\iff d\le1$），$\tau$＝covering number ⟹ 找 **candidate-center 兼容性**／**高阶 certificate** ✓
**三情形 ✓**：A $\tau\ge5$ 全体 ⟹ $k{=}4$ 无 exchange（统一 certificate 优于纯计算）；B 某 $\tau{=}4$ ⟹ moved 无 descent；C 某 $\tau\le3$ ⟹ **$124\to123$**（停批＋1024 点验证）✓
**方向反转 ✓**：$k\le4$ 无出口时**不机械升 k** ✗，先问"为何如此局部刚性"；关键线索＝**$124\to$overshoot$\to125(R>0)\to$cleanup$\to124$** ⟹ 冗余可达但需**支付额外中心的"能量成本"**，等基数交换消不掉 ✓✓
⚠️ **两处更正**：① $C(124,4)=9{,}381{,}251$（**不是** 9,183,626／9,307,766 ✗，已验：$9{,}183{,}626\times24=220{,}407{,}024\ne225{,}150{,}024$）；② $d_{\min}=1$（**非**"所有词两两 $\ge5$" ✗）；③ k=2 由抽样升级为完备 ✓
**红线** 🔴：只命名邻域结论 ✗；**绝不**推 $K(10,1)>124$ ✗

## A-KOPT-P3-ATTACK-TREE-1（2026-09-27 19:33）
**P3 六层分解（攻击树）✓**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.8 ✓（唐先生 19:32）
**母问题 ✓**：$\tau_C(E(A))=\min\{|D|:D\subseteq Q(E),E\subseteq B_1(D)\}$；$\tau\le k{-}1\Rightarrow124\to123$｜$\tau{=}k\Rightarrow124\to124$｜$\tau>k\Rightarrow$ 无 exchange ✓
**六层**：L1 删除几何（$|E|,N_j,q(x),q(x,y)$）｜L2 单中心容量（$M_1,M_2,M_3$）｜**L3 中心兼容性**（交叠图＋容斥 ⟹ 兼容性证书 ⭐）｜L4 covering number（$\tau\le3$?）｜**L5 结构分类**（fingerprint ⟹ 计算资产→数学资产 ⭐）｜L6 overshoot 势垒（$\Phi$、$124\to125(R>0)\to124$）✓
**优先级（拍板 ✓）**：**L4 → L3 → L5 → L6**；**不机械升 $k$** ✗
⚠️ **定义等价（本轮补充 ✓）**：$M_r(E)<|E|\iff\tau(E)>r$ **等价，非更强证书** ✗ ⟹ **L4 已由本次 $k{=}4$ 运行完备解答** ✓：全部 residual 跑 `can_cover(E,3)`、`k3bad=0`；豁免类 $\tau\ge6$ ⟹ $\forall|A|{=}4,\tau\ge4$ ⟹ **$4\to3$ 降基数出口堵死** ✓（P3 层结论，强于"无 moved"）
**待命 ✓**：`/tmp/kopt17_L5fingerprint.py`（L1/L3/L5 统计器，零 CPU 就绪）
**红线** 🔴：只命名邻域／局部结论 ✗；**绝不**推 $K(10,1)>124$ ✗

## A-KOPT-L5-FINGERPRINT-1（2026-09-27 19:37）
**L4 封存（待运行收尾 ⚠️）**：全部 residual $A$ 均跑 `can_cover(E,3)` 且 `k3bad=0`；豁免类 $\tau\ge6$ ⟹ 收尾后得 $\forall|A|{=}4,\tau(E(A))\ge4$ ⟹ **不存在 $4\to3$ 局部降基数出口** ✓（P3 完整子结论；**运行中：1.25M/≈1.65M，MOVED=0，ETA≈19:46** ✓ 不提前结案 ✗）
**L5 三级指纹（冻结 ✓）**：$F_0=(|E|,N_1..N_{10})$；$F_1=(F_0,|Q(E)|,\text{degree\_hist})$ ⭐第一主指标；$F_2=(F_1,\text{pair\_intersection\_hist})$（仅 F1 显聚类才算）✓ **不存中心编号／完整矩阵** ✗
**τ 三态绑定 ✓**：`EXEMPT`($\tau\ge6$)｜`NO_3_COVER`($\tau\ge4$)｜`3_COVER`($\tau\le3$ ⟹ $124\to123$) ＋ 非豁免者 τ 桶 $4$/≥5
**STOP 条件 ✓**：STOP-1（F0 无压缩）｜STOP-2（F1 类/样本>0.5 ⟹ 停 L5 转 L3）｜STOP-3（同类异 τ ⟹ 指纹不足）｜**SURVIVOR**（少数类覆盖大多数 ⟹ 代表元＋统一证明 ⟹ 从 $F$ 推 $\tau\ge4$）✓
**路线 ✓**：L4 封存 → L5 压缩 → L3 兼容性 → L5 代表类证明 → L6 势垒；**不机械升 k** ✗
**脚本 ✓**：`/tmp/kopt17_L5fingerprint.py`（零 CPU 就绪）
**红线** 🔴：只命名邻域／局部结论 ✗；**绝不**推 $K(10,1)>124$ ✗

## A-KOPT-K4-COMPLETE-1（2026-09-27 19:47）
**k=4 完备判定 ✓ 已完成**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §4.9 ✓
**终态读数 ✓**：`A-count = 9,381,251`（= $C(124,4)$ ✓ 与更正后算术一致）；组合筛豁免 4,752,805 (50.66%)；LB2>=6 豁免 2,970,604；**需真判 1,657,842 (17.67%)**；**`moved = 0`** ✓✓；**k3 交叉一致性检查 0 失败** ✓✓；exact 均 1,269µs／中位 1,283µs／最大 132,723µs；总用时 2320.2s（单核）✓
**读数分布**：$|E|$ 15→35（众数 23–24）；$|Q(E)|$ 116→203（众数 ≈160）✓
**L4 【正式封存】✓**：豁免类 $\tau\ge6$；residual 类 `can_cover(E,3)=False` ⟹ $\tau\ge4$ ⟹ $\forall|A|{=}4,\tau(E(A))\ge4$ ⟹ **不存在 $4\to3$ 局部降基数出口** ✓（P3 完整子结论，强于"无 moved" ✓）
**真交换局部刚性链 $k\le4$ 全部闭合 ✓**：$k={1,2,3,4}$ 均 0（k=1 可证；k=2 全 7,626；k=3 全 310,124；**k=4 全 9,381,251**）✓
**红线** 🔴：仅限**该基准码的四删邻域** ✗ 不得推全局；**绝不**推 $K(10,1)>124$ ✗；**不机械升 $k$** ✗（转 L5 fingerprint → L3）

## A-KOPT-L5-STOP2-AND-TAUK1-1（2026-09-27 19:52）
**L5 首轮：STOP-2 触发（指纹无压缩）＋ 统一模式 $\tau\ge k+1$**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.10 ✓
**L5 取样 ✓**（100,000 个 $A$，seed=20260927，62.1s）：$F_0$ distinct=99,435 (0.9943)；$F_1$ distinct=99,437 (0.9944) ⟹ **F1 相对 F0 只多 2 类（候选度谱几乎无新信息）** ✓；最大类仅 4 个样本；singleton≈98.9%；同类异 τ：F0 1 例、F1 0 例 ✓
**⟹ STOP-2**（F1 类/样本 $0.9944>0.5$）⟹ **L5 停，转 L3** ✓；**F2 未计算**（按规格 ✓）
**τ 状态 ✓**：EXEMPT 82,380｜NO_3_COVER 17,620｜非豁免 τ 桶 = **仅 {>=5}**（无 τ=4 ✓）
**⭐⭐ 局部刚性模式（$k\le4$，基准 124-code；实验资产登记 ✓ 措辞已收紧）**：对**已完备检查的每个** $A\subset C,|A|=k,1\le k\le4$，均有 $\tau(E(A))\ge k+1$，**四个层级分别**由各自完备判定给出：k=1 引理应；k=2 全 7,626；k=3 全 310,124；k=4 全 9,381,251（`can_cover(E,3)` 与 `can_cover(E,4)` 双 False）✓
⚠️ **禁止写法**：$\forall k\le4,\tau\ge k+1$（仿佛统一定理）✗；正确表述＝「**四个已分别完备验证的层级共同呈现该模式**」✓；严格限于**该码的半径 $k\le4$ 删除—补充局部邻域**，**不推** $K(10,1)$ ✗
⟹ **该基准码 $k\le4$ 内不存在任何 $k\to k'$（$k'\le k$）交换** ✓✓
**下一站 ✓**：不做 F2，直进 **L3（候选中心兼容性）**
**红线** 🔴：仅限该码局部删除邻域 ✗；**绝不**推 $K(10,1)$ ✗

## A-KOPT-L3-DESIGN-1（2026-09-27 19:58）
**L3 设计（先设计后跑 ✓）**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.11 ✓
**核心对象**：$\mathcal H_E=(E,\{S_z:z\in Q(E)\})$；问「是什么结构阻止 $k$ 个 $S_z$ 覆盖 $E$」✓
**三级证书**：**C1 容量**＝$M_k$ 路线，**非新机制，仅 baseline** ✗ ｜ **C2 pair/triple 兼容性**（找局部不可兼容结构；⚠️ 普通容斥易退化成 $M_k$ ✗）｜ **C3 Hall／dual 证书 ⭐**（二部图 $z\sim x\iff x\in B_1(z)$；$|N(W)|<$ 所需资源 ⟹ 类 set-cover LP dual ⟹ 可读 obstruction）✓
**第一轮实验**：抽 $50$–$200$ representative（典型＋极端 $|E|$），统计 ①$|S_z|$ 分布 ②$|S_z\cap S_{z'}|$ 分布 ③candidate degree ④**最小 witness $W$**（提取 $W\subseteq E$ 使一切三中心选择都至少漏一点 ✓）
**判据**：witness 高度重复 ⟹ **L3 存活**；皆偶然 ⟹ **降级／STOP**；简单统一冲突 ⟹ **冻结为候选 P3 lemma** ✓
**操作化**：逐点删减到极小 $W$（维持 `can_cover(W,3)=False`）⟹ 比较 $W$ 的距离谱型 ⟹ 数不同型数 ✓
**脚本 ✓**：`/tmp/kopt18_L3probe.py`
**红线** 🔴：仅限该码局部删除邻域 ✗；**绝不**推 $K(10,1)$ ✗

## A-KOPT-L3-CAPACITY-CERT-1（2026-09-27 19:58）
**L3 首轮探针 ＋ ⭐⭐ 候选统一证书**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.12 ✓
**探针（84 representative，1.3s）✓**：$|S_z|$ 分布 [1:7726, 2:5846, 3:504, 4:195, 5:18, 6:4]（候选中心极弱）；$|S_z\cap S_{z'}|$ 分布 [0:1,119,823, 1:95,922, 2:1,107]（**几乎全不相交**, mean 0.1）；candidate degree 9/10；$|W|{=}4..7$（众数 5–6），distinct W 型 $58/84{=}0.690$（中间态）；τ 一致性复核 0 异常 ✓
**⭐⭐ 证书（严格 ✓）**：$\Sigma(\text{top4 }|S_z|)<|E|\Rightarrow M_4(E)<|E|\Rightarrow\tau(E)\ge5$
**抽样覆盖 ✓**（200,000 个 A，60.2s）：**199,998/200,000 = 0.99999**；未覆盖仅 2 例（均 gap=0）；gap 众数 11、典型 8–13（**大余量** ✓）；全局 $\max|S_z|{=}8$
**意义 ✓**：**非** $M_k$ 枚举，而是**静态求和上界**（一次排序即得、可读）⟹ **从逐个 A 的 SAT 到可读数学 obstruction 的转换点** ✓
**✅ 全 residual 完备审计完成 ✓**（650.7s）：residual $1{,}657{,}842$ ｜ **证书成立 $1{,}657{,}826$ ｜ 失败 16 ｜ 覆盖率 0.999990** ✓✓；例外 $|E|{=}17$–$20$ 且索引集中于 **92/94/108** ⟹ **debt 集中退化族**；这 16 例的 $\tau\ge5$ 已由 kopt14 精确判定覆盖，**但尚无可读证书** ✗ ⟹ **C2／C3 入口** ✓

## A-KOPT-L3-ALPHA-1（2026-09-27 20:13）
**L3-α：capacity-failure 的【交叠证书】✓✓**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.12 ✓
**读数（12 例，秒级；`/tmp/kopt21_L3alpha.py`）**：每例 $T=\Sigma_{\rm top4}=|E|$（正是 gap=0），**但 max union（枚举全部"满和"4-子集）= 9–13 $\ll$ $|E|=17$–$20$**；$I_2=8$–$12$、$I_3=0$–$4$、$I_4=0$–$1$ ⟹ **12/12 由交叠证书封口** ✓✓
**严格性 ✓**：任 4-子集 $D$，$|\bigcup_DS|\le\Sigma_D|S|\le s_1{+}s_2{+}s_3{+}s_4=T$；$\Sigma_D<T$ 者直接 $<|E|$；$\Sigma_D=T$ 只在"满和"子集发生 ⟹ **只需枚举满和子集**（1–15 个）✓
**机制 ✓**：非"容量不够"，而是**容量恰好够但候选中心被迫重叠**（$I_2\approx8$–$12$）⟹ union 远低于 $\Sigma$ ✓✓（＝唐先生预判的 top-4 equality + unavoidable overlap ✓；**真正的兼容性证书，不是容量证书的改写** ✓）
**完整 16 例回收 ⚠️**：`/tmp/kopt22_cert_full_v2.py`（修正 `fails[:12]` 截断 ✗）⟹ 写入 `/tmp/kopt22_fails.txt`，待补
**红线** 🔴：仅限该码局部删除邻域 ✗；**绝不**推 $K(10,1)$ ✗
**残余 ✓**：gap=0 的少数例需**容斥修正**（扣 $|S_{z_i}\cap S_{z_j}|$）＝ **C2 入口** ✓

## A-KOPT-LEMMA-A-1（2026-09-27 20:15）
**引理 A（index-free 对中心交叠）＋ residual 完整证书体系 ✓**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.13 ✓
**引理 A ✓**：F_2^n 中 $z\ne z'$：$|B_1(z)\cap B_1(z')|=2$ 若 $d\in\{1,2\}$；$=0$ 若 $d\ge3$ —— **全空间核验 $\binom{1024}{2}=523{,}776$ 对，反例 0** ✓✓（证明：$u=w\oplus z$，$\mathrm{wt}(u)\le1\wedge\mathrm{wt}(u\oplus\delta)\le1$，按 $\mathrm{wt}(\delta)=1/2/\ge3$ 三分类 ✓）
**应用 12 例 ✓**：`pred = I₂` **12/12 完全一致** ⟹ 交叠损失被引理 A 完全解释，**不依赖 index 92/94/108** ✓✓
**index-free 机制 ✓**：容量最大化中心两两 $d\le2$ ⟹ 每对丢 $\le2$ 点（4–6 对 ⟹ 丢 8–12）⟹ $|\bigcup S_z|\le\Sigma-8\le|E|-4<|E|$ ⟹ $\tau\ge5$ ✓；中心被迫聚集之根源＝**例外 A 是小直径集（$d\le4$ 两两）⟹ debt 集中（$|E|=17$–$20$）** ✓
**📋 证书体系 ✓**：证书 I 容量（$1{,}657{,}826$ 例）＋ 证书 II 交叠（$16$ 例）⟹ **residual 100% 可读封口**（待最后 4 例确认 ⚠️）
**进行中 ⚠️**：`/tmp/kopt22_cert_full_v2.py`（ETA ≈20:24；20:26 cron 自动收尾）
**红线** 🔴：仅限该码局部删除邻域 ✗；**绝不**推 $K(10,1)$ ✗

## A-KOPT-FIVESTEP-AUDIT-1（2026-09-27 20:16）
**五步核验（唐先生 20:15）＋ 分层结论 ✓**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.14 ✓
| # | 结论 |
|:--:|------|
| 1 近距＝$d\le2$ | ✓ **已证** |
| 2 每近距对强制 overlap = 恰 2（$d\ge3$ 则 0） | ✓ **已证**（引理 A）|
| 3 overlap $=2\cdot\mathbf 1_{d\le2}$（$d$ 的函数） | ✓ **已证** |
| 4 满和 4-子集必含此 pair | ⚠️ **未证**；经验 **86/86 含【有交叠】近距对，0 例外**（12 例，`kopt24_item4.py`）|
| 5 严格推出 union $<|E|$ | ✓ **给定 item 4 严格成立**（非满和 $\Sigma\le|E|{-}1$；满和丢 $\ge1$）|
**⚠️ item 4 定位 ✓**：与"满和情形 $\tau\ge5$"**本质等价**（满和＋两两 $\ge3$ ⟹ 由引理 A 相交为空 ⟹ union$=\Sigma=|E|$ ⟹ 即覆盖）⟹ **不能当独立证明步骤**（循环风险）✗
**🎯 正式措辞 ✓**：**引理 A ＝真数学资产**（可证、index-free、$523{,}776$ 对 0 反例）✓✓；**证书体系 ＝ 引理 A（已证）＋ 一条经验正则性（待证）** ✓；**不得**称 A-KOPT-L3-ALPHA-1 已升为纯数学引理 ✗；**item 4 登记为 G4 待审项** ✓
**红线** 🔴：仅限该码局部邻域机制 ✗；**绝不**外推 $K(10,1)$ ✗

## A-KOPT-FULLCERT-1（2026-09-27 20:18）
**overlap 证书升级为【完整有限验证】（不依赖 item 4 ✓✓）**：`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` §5.15 ✓
**两个已证结构事实 ✓**：(i) $Q(E)\subseteq\bigcup_{a\in A}B_2(a)$；(ii) $|S_z|\le2\deg_A(z)$（由引理 A）；核验 1509 个候选中心，**违反 0/0**，取等号 224（界紧）；$\deg_A$ 分布 $=[1{:}1188,2{:}283,3{:}36,4{:}2]$ ✓
**完整性论证 ✓**：任何覆盖必满足 $\Sigma_D|S_z|\ge|E|$；含 $|S_z|{=}1$ 者 $\Sigma\le s_1{+}s_2{+}s_3{+}1<|E|$（**12 例逐一核验 ✓**）⟹ 只需枚举 $P=\{|S_z|\ge2\}$（$|P|{=}29$–$42$）✓
**结果 ✓✓**：满足必要条件的四元组**仅 1–15 个/例**，max union $=9$–$13<|E|=17$–$20$ ⟹ $\tau\ge5$ **完整封口** ✓✓
**定位 ✓**：**item 4 降为 G4 观察项**（非证书依赖）✓；**证书体系 ＝ 引理 A（已证）＋ 完整有限枚举（1–15 个）** ✓
**状态定稿（三层，必须严格区分 ✓）**：**SURVIVOR / COMPLETE FINITE CERTIFICATE** ✓
- **数学引理**：Lemma A **已证** ✓
- **目标证书**：12（→16）个 capacity-failure $E$ 已由**穷尽候选四元组**得 $\tau(E)\ge5$ ✓
- **尚未得到**：对**所有 $A$／所有此类 124-code** 的**统一 theorem** ✗
**引理 A′（半径 2 ✓ 新算）**：$|B_2(z)\cap B_2(z')|=20$（$\delta\in\{1,2\}$）／$6$（$\delta\in\{3,4\}$）／$0$（$\delta\ge5$）⟹ **$B_2$ 相交 $\iff d\le4$**（tri-clique／LB2 豁免的定量根源 ✓）；三点交规模 $\le5$ ✓
**下一阶段 ✓**：把"高容量候选极少 ＋ candidate geometry 强制 overlap"压成**不需逐例枚举的统一 lemma**（Lemma B 蓝图见 doc §5.16）✓；**LP-dual 已失去优先级** ✗
**Lemma B 压缩结果 ✓（§5.17）**：$310{,}124$ 个三元组 $\to$ **56 个 δ 模式**；其中 **52/56：$|\bigcap B_2|=0$ 或 $\le5$ 且 diam $\le2$** ⟹ Lemma A 强制 overlap ✓✓；**仅 4 个紧簇模式**（$(2,2,4)$214、$(1,2,3)$111、$(2,2,2)$88、$(1,1,2)$37，共 **450 个三元组 = 0.145%**）待细分 ✓
**观察到的例外 A 所涉三元组全落"好"模式** ✓
**\"只打一刀\" 结果 ✓✓（§5.18）**：**Lemma A″（新，统一）**：$\nu(B_2(z)\cap B_2(z'))=2$ 对 $\delta=1,2,3,4$ 全部成立（$\nu$＝max 两两 $d\ge3$ 子集）⟹ 该交里**任意 3 中心必含一对 $d\le2$** ⟹ Lemma A 强制 overlap ✓；**4 个"坏"三点交模式亦 $\nu=2$** ✓✓ ⟹ **距离 1/2 的 pair 不改变 overlap 结构** ✓（答案：不制造分散候选集）
**鸽笼步（已证）**：覆盖需 $\Sigma\deg_A\ge9$ ⟹ 必有 $a_i$ 使 $D$ 中 $\ge3$ 中心落入 $B_2(a_i)$ ✓
**残余缺口（精确）**：鸽笼落到单个 $B_2(a_i)$；$\deg_A\ge2$ 者已由 A″ 封口，仅剩"多中心仅邻近同一 $a_i$"的退化情形 ⚠️
**判定**：4 个模式已统一处理 ✓，但推及全 code 的统一 theorem **未闭合** ✗ ⟹ 保留 **pattern-compressed finite certificate**；可迁移资产＝**Lemma A／A′／A″（可证、index-free）** ✓✓
**✅ 全 residual 封口 ✓✓（§5.19）**：kopt22 完成（**16 例全回收**，新增 $(92,94,108,109)/(92,94,108,118)/(94,97,108,109)/(94,108,109,118)$）；索引频次 **94(13)｜108(13)｜92(12)**｜67(4)｜97(3)｜109(3)…；含 $\{92,94,108\}$ 者 8/16；$|E|=17$–$20$
**kopt21 ＋ kopt26 均 16/16 封口 ✓✓**（满和子集 1–28；**候选四元组 1–124**；max union $=9$–$15$ ⟹ 余量 $\ge4$）
$$\Rightarrow\ \text{residual }1{,}657{,}842\ \text{的 100\% 均有可读证书}$$ ⟹ **L3-α ＝ COMPLETE FINITE CERTIFICATE（全 residual 覆盖）** ✓✓
**📒 收官账本 ✓（§5.20）**：$9{,}381{,}251=7{,}723{,}409\,(\tau\ge6)+1{,}657{,}826\,(\text{容量})+16\,(\text{完整交叠})$ ✓（恒等式已核验）
**L3-α 收官**：**不再优化本证书** ✗（唐先生 20:27 ✓）
**下一阶段唯一入口 ✓**：**从完整证书抽取可证明的统一机制**（不依赖具体 $A$、不依赖逐例枚举的结构定理）；素材＝Lemma A／A′／A″ ＋ 鸽笼步（已证）＋ δ-pattern 压缩（$310{,}124\to56\to4$，4 模式 $\nu{=}2$）✓；**精确残余**＝鸽笼落到单个 $B_2(a_i)$ 的退化情形 ⚠️
**🎯 残余压缩结果 ✓✓（§5.21）**：**可以**（且**不含循环**）——对 250 个候选 4-元组（16 例）：**全远候选 = 0/250**；$c(D)\ge2$、$L(D)\ge4$、excess $\le1$
$$\Longrightarrow\ |\bigcup S_z|=\Sigma-L\le|E|+1-4=|E|-3<|E|\ \Longrightarrow\ \tau(E)\ge5$$
三条事实均为**几何／尺寸陈述**，不涉"无覆盖"结论 ⟹ 单向必要链，**无循环** ✓✓；待证项＝三条定量事实（已 250/250 经验验证，余量 3 点）✓
**🎯 攻 $c\ge2$ 结果 ✓（§5.22）**：**远距四元组 $\max\Sigma|S_z|=\mathbf{16}<17\le|E|$** ⟹ $c(D)\ge2$ 定量形式**成立** ✓✓（$c\ge2$ 是 $\tau\ge5$ 的**弱形式**，不循环 ✓）
**但 (ii) 路线失败 ✗**：实测 $\max\Sigma\deg_A=11>8$；且 $\max(2\deg-|S_z|)=5$ ⟹ (ii) **松 5 点**，不足证 $\Sigma\le16$
**缺口精确 ✓**：$\Sigma|B_1(z)\cap E|$ 与 $E(A)$ 构造的**定量耦合**（＝唐先生预判的真瓶颈）⟹ $c\ge2$ **暂无 index-free 证明** ⚠️
**红线** 🔴：仅限该码局部邻域机制 ✗；**绝不**外推 $K(10,1)$ ✗

**🆕 C-381（2026-09-27 · OPEN CORE 精确核验 + §5.22 步修正）** ✓
- 【**修正**】§5.22 的「远距无候选 ⟹ $c(D)\ge2$」**有缺口** ⚠️：远距 ($c{=}0$) $\max\Sigma=16<17\le|E|$ 只给 **$c\ge1$**；而 $c\le1$ 的全局 $\max\Sigma$ 达 **18**（$>16$）⟹ 该步不是漏写一步，是**少了更强的一步** ✓；**补算**：逐例 $c\le1$ max$\Sigma$ $<|E|$（余量 $1\!\sim\!5$）✓✓ ⟹ 结论 $c\ge2$ **不变**，**依据替换** ✓
- 【**OPEN CORE**】$\Sigma_D|S_z|$ **只依赖四个权重** ⟹ $\max_D\Sigma=$ **top-4 权重和**（恒真化简）⟹ **无需枚举即精确判定** ✓✓；**16/16 例 top-4 $\le|E|+1$**（excess $\in\{0,1\}$，0 越界）；池内 **873,472** 四元组 excess>1 = **0 例**；excess$=1$ **确发生**（1 例）⟹ 界**紧至 1** ✓
- 【**恒等式**】$|\bigcup S_z|=|E|-U$ ⟹ 三条事实链净内容 ＝ **$U\ge3$**（实测 $U=6$–$8$）✓；⚠️ $L\ge4$ 与 $L-U\le1$ **严格强于**目标 ⟹ **换包装，非降难** ✓
- 【**结构**】距离型 **33** 种／含候选 **12** 型／达 excess$=1$ **5** 型；**型不决定 excess**（同型可取 $-1/0/1$）⟹ 型分析须配 $E$ 的 $A$-专有结构 ⚠️
- 档：`docs/CORE-2026-09-27-excess-verification-and-c2-precision-fix.md`｜脚本：`/tmp/kopt37b_core.py`、`/tmp/kopt38_types.py`
- 红线 🔴：**有限核验**（16 例，**非定理**）✗；不外推 $K(10,1)$ ✗；不改 L3-α 证书 ✗

**🆕 C-382（2026-09-27 · A-型最小分析：全距 2 型 ⟹ **STOP → B**）** ✓
- 【**形状二分**】取 $z_1=0$ ⟹ $z_2,z_3,z_4$ 权恰 2 且支撑两两交恰 1 元 ⟹ **仅两种形状**：**STAR**（$z_2=e_a{+}e_b$ 型：四球交 $=\{e_a\}$ 重数 4 ＋ 6 个配对中点）／**TRI**（$z_2=e_a{+}e_b,z_3=e_b{+}e_c,z_4=e_a{+}e_c$：无公共点，4 个 $n{=}3$ 角点）✓✓ —— **index-free 几何** ✓
- 【**重叠恒等式**】STAR：$L=3\cdot[y^\ast\in E]+\#\{\text{6 中点}\in E\}$；TRI：$L=2k$（$k$ 个角点 $\in E$）✓
- 【**命题 G1／G2（紧 ✓✓）**】G1：STAR $\wedge\ y^\ast\in E\Rightarrow L\ge3$（实测 1585 例 $\min L=\mathbf{3}$ **取等** ✓）；G2：TRI $\wedge\ \ge3$ 角点 $\in E\Rightarrow L\ge6$（实测 93 例 $\min L=\mathbf{6}$ **取等** ✓）
- 【**STOP → B 依据**】STAR $\wedge\ y^\ast\in E$ 时 $\min L=\mathbf{3}<4$ ✗ ⟹ **几何推不出 $L\ge4$**；第 4 个单位须用 $\Sigma\ge|E|$（742 个「特殊点 $\notin E$」四元组中候选 **0** 个）＝**尺寸条件** ⟹ 本质是 $A/E$ 具体结构 ⟹ **非 index-free** ⟹ STOP ✓
- 【**sharp 定位**】excess$=1$ 仅出现在 $A=(92,94,108,109)$（$|E|{=}18$）：STAR **4** 个（$L{=}7$，含 $n{=}4$ 公共点）＋ TRI **1** 个（$L{=}6$），均 $\ge6>4$ ✓
- 档：`docs/CORE-2026-09-27b-all-distance2-minimal-analysis-STOP-to-B.md`｜脚本：`scripts/CORE_all_distance2_analysis.py`、`scripts/CORE_all_distance2_forcing_probe.py`
- ⚠️ 方法自勘：上一档 §4 的「距离型」签名（各行距离三元组排序）**看不见** STAR／TRI（两者签名相同）✗ ⟹ 该签名不足支撑型分析 ✓（已修）

**🆕 C-383（2026-09-27 · **B 档收口定型**：T1–T5 ＋ 停止理由）** ✓
- 【**停止理由（唐先生 20:56 定稿 · 逐字保留）**】🔴
  > **STOP：纯几何层的统一 overlap 下界为 $L\ge3$，而目标 $L\ge4$ 的第 4 个单位依赖 $E(A)$ 的专有尺寸耦合；继续枚举不能产生新的机制资产。**
- 【**精确化（本档补 · 不改收口作用）**】仅形状 ⟹ $L\ge0$（取等）；形状 $+y^\ast\in E$ ⟹ $L\ge3$（1585 例**取等** ✓✓）；形状 $+k$ 角点 $\in E$ ⟹ $L\ge2k$（93 例**取等** ✓✓）⟹ 严格读法＝「**几何 ＋ $E$-成员假设** ⟹ $L\ge3$」，而 $E$-成员由尺寸条件 $\Sigma\ge|E|$ 提供（742 个「特殊点 $\notin E$」四元组中候选 **0** 个）⟹ **能力边界结论不变** ✓
- 【**T1–T5 定型**】T1 top-4 恒等式（免枚举）｜T2 sharp excess（$\Sigma-|E|\le1$ 且 $+1$ 实现）｜T3 Lemma A／A′／A″｜T4 **修正** $c\ge2$ 链（**弃** $c{=}0\Rightarrow\Sigma\le16$ ✗）｜T5 **STAR／TRI 形状二分＋overlap ledger**（本轮新增 · 最有价值）✓
- 【**关键结论**】$$\boxed{\text{geometry supplies }L\ge3,\quad\text{but the fourth unit requires }(A,E)\text{-specific coupling}}$$
- 【**sharp 双实现 ⟹ 收益削弱**】$A=(92,94,108,109)$：STAR（$L{=}7$，含 $n{=}4$ 公共点）×4 ＋ TRI（$L{=}6$）×1 ⟹ excess$=1$ **无唯一几何实现机制** ⟹ 纯 distance-type classification 收益削弱 ✓
- 【**本线完成的工作**】$9{,}381{,}251$ 个局部交换 → 逐层压缩 → 少数可复用几何不变量 ＋ **纯几何机制的能力边界**（精确）✓ ⟹ **B ＝ machine certificate ＋ transferable mechanism ＝ 正确收口**（**非失败转场** ✓）
- **不再行动** ✗：不扩枚举／不重扫 873,472／不优化 L3-α 证书／不重启 distance-type classification ✓
- 档：`docs/BFREEZE-2026-09-27-transferable-assets-T1-T5-and-stop-rationale.md`

**🆕 C-384（2026-09-27 · T-1 `z_L(5,5)` 归位 ＝ DROP；含门运行与门缺口）** ✓
- 【**门运行**】`scripts/closure_gate.py` ＋ `scripts/T1_CHECK_gate_candidates.json` ⟹ **T-1 ＝ ADMIT**（E4 五金齐 OPEN/PASS；无机器判定理、无指纹命中）；**阳性对照**（forbidden configuration 边界）＝ **BLOCKED** ⟹ **门本身工作正常** ✓（输出 `scripts/T1_CHECK_closure_gate.txt`）
- 【**仍 DROP · 三条独立依据**】① `Zarankiewicz-A3-source-check.md`（**09-24 22:33**，晚于 T-1"首攻"标记 13:39/13:52）已登记**记录型入口 #4**：`owner＝是`、`路线＝构造＋上界论证`、`判定 D` ＋ 预登记「**不在 Zarankiewicz 内部改参数救场**」✓；② `AMEND-21` 明文「**未覆盖 ≠ 未知**」禁令 ✓；③ **同形赛跑**（作者同文已对 5×3／5×4 做完整 extremal 枚举并置附录 ⟹ 5×5 为其下一步）＋ 独立第二组 `arXiv:2605.09926` 已给 $z_{3L}(5,5)\ge16$ ＋ `A3` 的 **E5 工业化**校准 ✓
- 【**三点 source 核验（已跑完 · zero-compute）**】① 定义**逐字锁定** ✓✓（`Symmetry 18(7):1076` §1/§2：1-edges／2-edges 四元组 $(i,j;k,l)$／非退化·行退化·列退化／禁 generalized $C_4$）；② **仍 open** ✓✓（`arXiv:2604.04111` 逐字：*"The exact value of $z_L(5,5)$ remains open; here a lower bound of 15 was established"*）＋**解库存疑点**：14＝前作下界、**15＝现下界** ✓；③ extremal $C_4$-free 5×5 **未被收割，但在跑** ⚠️
- 【**⚠️ 门缺口（只登记，不擅改门）**】**G-1** 无 owner／工业化（**E5**）前置问；**G-2** 未实现「未覆盖≠未知」禁令（"无人做"可伪装成 E4 的 OPEN）；**G-3** E4 五闸 evidence 可同源重复填 ⟹ 门会**放行项目已判除的条目** ⚠️（建议须唐先生批）
- 【**交棒**】**T-5 三点**：① 目标阶**图数**核实（库存"约 $10^4$"为估计）② 已知**完备阶数阈值** ③ **公开证书状态**（结果已解决 vs 仅有算法／部分族）；**不得预设 $n=8$ 首攻** ✓
- 档：`docs/T1-CHECK-2026-09-27-zL-5-5-three-point-source-verification-DROP-to-T5.md`、`docs/GATE-RUN-2026-09-27-T1-closure-gate-admits-but-preregistration-drops.md`｜脚本：`scripts/T1_CHECK_gate_candidates.json`、`scripts/T1_CHECK_closure_gate.txt`

**🔴 C-385（2026-09-27 · **ERRATUM + T-5 ＝ DROP**）** ✗
- 【**勘误（阈值 6 → 7）**】**inertia sets 完备阈值 ＝ $n\le7$**（**LAA 436(12), 2012-06-15, 4489–4502**，DOI 10.1016/j.laa.2011.08.026）逐字：> *"We term such graphs **atoms** and give the inertia sets for all atoms on at most seven vertices. **This can be used to compute the inertia sets for all graphs on at most seven vertices.**"* ✓✓ —— **库存旧记 $n\le6$（ELA 2010）为过期指纹** ✗（该 2010 文自称只到 6 阶，未追后继）
- 【**T-5 终局 ＝ DROP（对象级收割）**】① min rank $n\le8$（2025 ELA ✓）② max nullity $n\le8$（对偶 ✓）③ **inertia set $n\le7$（2012 LAA ✓）** ④ $n=8$ inertia **不判 open**（2012 文只称 can be applied to many graphs，**未**称全体 8 阶）⑤ inverse inertia 结构刻画已有成套 reduction ⟹ **不进 P1/P2** ✓
- 【**DROP 记录（唐先生 21:10 逐字 · 供直接引用）**】
  > **T-5 / graph inertia-set small-order classification — DROPPED: complete through $n=7$ (2012); min-rank/max-nullity through $n=8$ (2025). Do not treat $n=8$ absence of a table as evidence of openness.**
- 【**$\operatorname{mr}$ 与 $\mathcal I$ 不可互推 ✓**】$\operatorname{mr}(G)=\min_{(p,q)\in\mathcal I(G)}(p+q)$ ⟹ $\operatorname{mr}$ 是 $\mathcal I$ 的**投影**；2025 的 min rank/max nullity 完成**不**收割 $\mathcal I$ ✓
- 【**纪律收获**】**"未见表" ≠ "open"** ⟹ 新目标须**正面证据**（作者自述 open／明确未做）✓；与 T-1 对照：T-1 的 open 是**作者自述**（可用 ✓），T-5 的 $n=8$ 是**检索缺口**（不可用 ✗）
- 【**建议条款（只登记 · 不改门）**】**G-4**：阈值／缺口类事实**须追后继引用链**；目标 open **须有正面证据** ⚠️｜连同 **G-1/G-2/G-3** 一并**待宪章审批** ✓
- 【**为何比 T-1 更干净**】T-1 ＝ 预登记撞车（09-24 A3 判定 D）＋同形赛跑；**T-5 ＝ 对象指纹本身已被 2012 文献收割**（零赛跑风险）✓
- 档：`docs/ERRATUM-T5-2026-09-27-threshold-6-to-7-and-final-DROP.md`｜（勘误对象）`docs/T5-CHECK-2026-09-27-…-HOLD.md`（已加勘误横幅 ✓）

**🔴 C-386（2026-09-27 · T-6 `K_q(n,R)` 具体格子 ＝ **DROP**）** ✗
- 【**对象指纹锁定**】$K_q(n,R)=\min\{|C|:C\subseteq\mathbb Z_q^n,\ \text{覆盖半径}\le R\}$；cell ＝ $(q,n,R)$；"open" ＝ **上下界未重合**（整数问题，非分类）✓；**不可混**：混合码 $K_{q_1,q_2}$／重量受限／**saturating sets**（相邻但分账）／二元 $K_2(n,1)$（＝超立方体支配数 ⟹ **属已冻结的 $K(10,1)$ 邻域，严禁借 T-6 复活**）✗
- 【**后继链（逐字 ✓）**】Kéri 表（$q\ge3$）**last revised November 2011** ✓；`arXiv:2608.19872v3`（Marosi, BME, **2026-09**）：**84 例／83 格**被改（**26 上界** $5\le q\le15$ 显式码＋LNS；**58 下界** $6\le q\le21$ 由 **Gijswijt–Polak SDP** ＋多精度＋**精确有理证书**）✓；$K_6(10,4)$：$417$–$2952$ → **$441$–$2751$** ✓；**"every certificate is checked by a standalone program in exact arithmetic"**；**"codes, certificates, and checkers … ancillary files"** ✓⚠️；并行线：Wu–Chen 二元下界、**Florath 证明助手形式化** ⚠️
- 【**同形赛跑：全面撞上 ✗**】同参数／同等价／同构造族（显式码＋direct sum／product propagation＋SDP）／同作者群（Marosi｜**Kéri 表主**｜Haas–Halupczok–Schlage-Puchta｜Gijswijt–Polak｜Wu–Chen｜Florath）⟹ 依规则**先 DROP/HOLD，不进计算** ✓
- 【**严格 novelty gate：答不出 ⟹ DROP**】T1（删 4 码字的局部捕获账本）／T2·T4（$E$-专有耦合）／L3-α 证书 **均不适用**（全局极小 vs 局部修复）✗；T5 仅给**局部**重叠计数，**不**给全局下界 ✗ ⟹ 不可证明"T-6 能让 T1–T5 产新约束"；强行做即＝"把 $K(10,1)$ 局部证书**换参数再跑**"（禁止形态 ✗）
- 【**正面 open 证据 vs 检索缺口**】作者自述（2026-08 自检索）"$q\ge6$ 自 2011 无任一侧改进"＝**正面证据** ✓；但**同篇已收割 58 个 $6\le q\le21$ 下界** ⟹ 剩余"未见表"格属**检索缺口**，依 G-2/G-4 **不得当 open** ✗
- 【**唯一副产品（登记为可迁移资产观察 ⚠️ 档级 · 3 行可证 · 未跑）**】**Lemma A 的 $q$ 元推广**：$\mathbb Z_q^n$ 中 $|B_1(x)\cap B_1(y)|=2$（$d\in\{1,2\}$）／$0$（$d\ge3$）✓ —— 仅给**局部**重叠计数，**不**自动给全局下界 ⟹ 不足支撑 T-6 ✓
- 档：`docs/T6-CHECK-2026-09-27-fingerprint-successor-chain-race-check-DROP.md`｜库存已标 DROP：`TOPIC-DOSSIER-v1`、`CONCRETE-TOPIC-LIST-r2` ✓

**🔴 C-387（2026-09-27 · T-7 `PG(2,q)` minimal 1-saturating sets ＝ **DROP**）** ✗
- 【**资产隔离检查：失败** ✗（唐先生 21:15 专门要求）】$\ell_1(2,q)$（1-saturating set 最小尺寸）与 $K_q(n,1)$ 经**经典 parity-check／syndrome 桥**为**同一 functional** ⟹ 只是把 Hamming 空间的覆盖证书逻辑**换成射影平面的割线覆盖逻辑**；`TOPIC-DOSSIER-v1` T-7 **自陈**"与 T-6 **同机制**（syndrome 覆盖 ↔ saturating）" ✓ ⟹ 依规则**直接 DROP，不许进入计算** ✓
- 【**后继链（逐字 ✓）**】Pambianco 等 2003（Australas. J. Combin. 28:161–169）表基座；**分类已到 $q\le23$**（Bartoli–Marcugini–Milani–Pambianco, ACCT 2012；Bartoli–Davydov–Faina–Marcugini–Pambianco, *J. Geometry* 2013：*"the minimal 1-saturating sets of the smallest size in $PG(2,q)$ are classified for $16\le q\le23$"*）✓✓；上界线连续（arXiv:1505.01426、arXiv:1702.07939、Nagy 渐近界）；**2026 仍有新文**（**arXiv:2606.16669** 几何法广义覆盖半径）⚠️
- 【**同形赛跑：逐项撞上 ✗**】同参数／同等价／同构造族（割线覆盖构造）／**同作者血统**（Pambianco｜Bartoli｜Marcugini｜Davydov｜Faina｜Nagy，与 T-6 的 Kéri／Marosi 社区交叉）✓
- 【**P1/P2 novelty gate：答不出 ⟹ DROP**】T1（删 4 码字的局部捕获账本）／T2·T4（$E$-专有耦合）／T5（仅局部重叠计数）／L3-α（单码有限证书）**均不**对"全局最小尺寸"产生新约束 ⟹ 强行做＝**旧约束换参数／换表示**（禁止形态 ✗）
- 【**P3：deliverable 无法预先说清**】最可能产物＝"某 $q$ 的上界改进"或"小 $q$ 重算／形式化" ⟹ 两者均为唐先生**明确排除**者 ✗
- 【**⚠️ 阈值漂移（第二轮）**】库存 T-7"前沿"写 $q\le16$；实际**分类到 $q\le23$** ⟹ 同 T-5 的 $6\to7$ ⟹ 强化 **G-4**（阈值类须追后继链）✓
- 【**池级读数（本档真正产出 ⚠️）**】四连 DROP 三类死因：T-1 预登记撞车＋赛跑｜T-5 对象级收割＋阈值漂移｜T-6 赛跑全面＋证书链工业化｜T-7 **资产隔离失败**＋同族＋阈值漂移 ⟹ 池内**"表填空族 M1" 四格全落在"覆盖／支配／饱和"同一生态且已被工业化** ⚠️ ⟹ 建议（非决定）：**(a)** 对 M1 族做**族级判决**；或 **(b)** 转向**非同族**余项（**T-4** SNIEP $n=5$／**T-8** $\pm$-rank，属**方法族 M2：秩/惯性**，不涉覆盖证书）✓
- 档：`docs/T7-CHECK-2026-09-27-fingerprint-race-and-asset-isolation-DROP.md`｜库存已标 DROP：`TOPIC-DOSSIER-v1`、`CONCRETE-TOPIC-LIST-r2` ✓

**🔴 C-388（2026-09-27 · **M1 族级关闭**）** ✗
- 【**判定（精确形式 · 照唐先生）**】$$\boxed{\text{现有 T1–T5 资产}\not\Rightarrow\text{M1 的全局极小值问题产生新的 P1/P2}}\quad\boxed{\textbf{M1 ＝ CLOSED FOR THIS ASSET PACKAGE}}$$
  ⚠️ **仅资产—问题映射层** ✓ —— **不**声称"covering codes 无价值" ✗、**不**声称"该生态无 open problems" ✗
- 【**证据链（四样本三类死因）**】T-1 预登记撞车＋赛跑（**形式 open ≠ 可用入口**）｜T-5 对象级收割＋阈值漂移（**小阶分类阈值易滞后**）｜T-6 工业化赛跑＋novelty gate 答不出（**covering 本体已有证书/checker/形式化生态**）｜T-7 **资产隔离失败**（saturating ＝ covering/syndrome 同一 functional）✓
- 【**沉淀纪律** **(D-A)** "形式 open" ≠ "可用入口"；**(D-B)** "换个表示" ≠ "换个问题"（判据：证书逻辑是否同一 functional）✓
- 【**重开条件（登记 ✓）**】出现新资产 $X$ 使 M1 中某格产生新的 P1/P2（且非"旧约束换参数/换表示"）✓；**排除**：换 $(q,n,R)$／换几何表示／"库仍写 unknown"／重算或形式化 ✗
- 档：`docs/M1-FAMILY-CLOSURE-2026-09-27-closed-for-this-asset-package.md`

**🔴 C-389（2026-09-27 · T-4 SNIEP $n=5$ ＝ **DROP**（资产—问题映射层））** ✗
- 【**最硬依据：我方自己跑过并已判新性失败**】`M03-P2-SNIEP-FINAL-STAGE-REPORT.md` §0 逐字：*"P2-SNIEP 分支：**数学机制成功，独立新性失败** ⟹ 降级为「已知 SNIEP 区域的独立局部机制复核资产」"*；清单：独立新性 **否**／SNIEP 新结果 **否**／RH 桥接 **否**；Krawczyk 新性路线**关闭** ✓✓
- 【**区域层 FAIL（实测）**】`(3b)` ＝ **MECHANISM EXTENSION / NO REGION EXTENSION**；$W_{\rm PS}\subseteq\{$JMP-已排除$\}\cup\{$Loewy-已排除$\}$ ✓
- 【**同形赛跑**】我方研究族 $(1,t,t,-(q+\varepsilon),-(q+\varepsilon))$ **即** JMP 2017（LAA 512,129–135）之族（逐字：其 Thm 1 ≡ 我方 $u$-条件）✓；我方点被 **Marijuán 2023**（$a\le\frac{\sqrt5-1}4$ 恒可对称实现）与 **2026-05 WSU 学位论文**（充分区含 $1+4\lambda_2\lambda_5\ge0$）覆盖 ✓；最新 **arXiv:2608.19435**（Jin–Ke–Sui, **2026-08-19**, 45pp）**只加新不可能区域**（低迹；对角移位→临界高迹边界→加权五环），**未完成** $n=5$ ✓
- 【**关键区分**】**$n=5$ 数学上仍 open ✓；但我方资产对该问题的边际已实测为零（区域层 FAIL）** ⟹ 关闭的是**资产—问题映射**，不是问题 ✗✓
- 【**攻击面清点（全部已跑 ✓）**】线性层 已关闭｜Soules-1 解析定理（恒失败）｜Soules-2 **UNDECIDED**｜幂和 机制扩张/区域无扩张｜JMP 交错 CLOSED 无新排除｜Krawczyk 新性关闭 ✓
- 【**保留登记（非目标 ✓）**】残余靶区 $\{\frac49<t<\frac{15}{31},\ 4t-2<\varepsilon<\varepsilon_2(t)\}$（非空、$u>0,v>0$）⟹ **重开须**：新资产 ＋ **正面 open 证据**（本轮**未取到**，不得以"我未见表"充数 ✗，G-4）✓
- 【**池况提示（非决定 ⚠️）**】M1 四格 ＋ T-4 均在映射层关闭 ⟹ 池内剩余可查：**T-2**（$AG(7,3)$ 最大 cap）／**T-3**（疑似已解）／**T-8**（缺口未锁定）／**T-9**（已 REJECT）⟹ **待筛密度很低** ⚠️
- 档：`docs/T4-CHECK-2026-09-27-source-first-SNIEP-n5-DROP.md`

**🔴 C-390（2026-09-27 · T-2/T-3/T-8 终扫 ⟹ **旧池耗尽** ＋ **重新进货协议**）** ✓
- 【**T-2 $AG(7,3)$ 最大 cap ＝ DROP**】$AG(6,3)=112$ 且**仿射等价唯一**（Potechin）；上界 $2.756^n$（E–G）；新下界 $2.218^n$（`arXiv:2209.10045`）；$n\ge7$ 大小未知 ⟹ **资产接口弱**（全局极值/堆积型；档内自评"攻击点弱"）＋ 生态持续收割 ＋ 属"改进界"dent 型 ⟹ DROP ✗
- 【**T-3 最小 complete cap ＝ DROP（正面证据 ✓✓）**】Bishnoi 博客 **2026-03-10** 逐字：Grace–Voloch（`arXiv:2602.05254v1`）"an elegant algebraic construction of size $O(3^{n/2})$, **thus solving the problem**" ✓✓ ⟹ **有正面来源**（满足 G-4），非检索缺口 ✗
- 【**T-8 $\pm$-rank ＝ HOLD**】ILAS **2026** 报告（`indico.math.vt.edu/event/2/contributions/351/`）逐字："…'generalizes' the binary rank and the term rank… **We establish several inequalities**…" ⚠️ ⟹ **对象刚引入、缺口未锁定、无正面 open claim** ⟹ **HOLD**（复活条件＝精确对象＋参数＋正面 open 证据）✓
- 【**旧池耗尽判定 ✓**】T-1 DROP｜T-2 DROP｜T-3 DROP｜T-4 DROP｜T-5 DROP｜T-6 DROP｜T-7 DROP｜**T-8 HOLD**｜T-9 REJECT ⟹ **8 DROP ＋ 1 HOLD ＋ 1 REJECT ＝ 无可用入口** ✓
- 【**重新进货协议（把 M1／D-A／D-B／G-4 变成生成器）**】①**黑名单**：covering／domination／saturating／syndrome-covering 及一切经 parity-check functional 等价的变体（除**新资产**外不再进池）✗；②**问题先行**（frontier open problem ⇒ fingerprint ⇒ asset match ⇒ P1/P2；**严禁**"手里有资产 ⇒ 到处找相似问题"）✓；③**四问闸**：Q1 是否全局极值/覆盖型（→M1 ✗）｜Q2 证书逻辑是否同一 functional（→隔离失败 ✗）｜Q3 是否有**正面 open 证据**（仅"未见表"不可用 ✗）｜Q4 现有资产能否产生**新约束**（否 ⟹ 映射层关闭 ✗）✓；④目标生态：rank／spectral｜finite geometry（非覆盖型 ⚠️）｜extremal（堆积/Turán 型）｜additive combinatorial invariant｜certificate-driven classification ✓
- 【**首批扫描提案（round-1 ⚠️ · 非候选 · 下轮走全流程）**】B1 unicyclic／bicyclic 图 inertia（DMGAA）｜B2 树的 inverse eigenvalue（重数表／generalized stars）｜B3 spectral arbitrariness for trees（JCTA 2024）｜B4 Turán $(r+1,r)$-systems（2026-08-25 改进界）｜B5 $\pm$-rank 及 rank 不等式族（ILAS 2026，与 T-8 同源 ⚠️ HOLD）✓
- 【**本轮研究资产（比单个 $K(10,1)$ 结果更重要）**】$$\boxed{\text{无【对象指纹＋后继链＋资产隔离】的大候选池，会系统性产生\textbf{假开放问题}}}$$（五连 DROP ＋ T-4 ＋ M1 族级关闭为证 ✓）
- 档：`docs/POOL-SWEEP-2026-09-27-T2-T3-T8-final-cleanup-and-restock-protocol.md`

**📋 C-391（2026-09-27 · **RH 证明链逐环难点拆解**（重审 `CHAIN-AUDIT`））** ✓
- 【**难点的分布（核心结论）**】$$\boxed{\text{难点\textbf{不}均匀}:\ [C]\ \text{古典但循环};\ [A]\ \text{数十族已关闭＋算术接口负结果};\ [B]\ \text{唯一缺口}}$$ 且 **$[B]$ 内部 11 子难点在依赖图上收敛到 1–2 个节点** ⟹ **"很多难点"压成"一个对象 + 若干侧写"** ✓✓
- 【**该对象（精确形式）**】$$\boxed{\text{正性}P:\ \text{充分（非必要）}\wedge\text{算术内生（非重述）}\wedge\beta\text{-敏感（非盲）}\wedge\text{越过 support }1\text{（相位感知对相关）}}$$ 同时被 **W1／W5／W6／W12／W2** 从五侧封住 ✓
- 【**环 [A] $S$（5 条）**】A1 内生性（W3 值面墙）｜A2 非重述（零杠杆／T7）｜A3 $\tau$／相位双产（D10/AOB2，"寻找 $\tau$"已关闭）｜A4 对象防线（D8 三个 $\frac12$／D9 对象混淆）｜A5 已关闭候选数十族（§三关键词表＋G8–G20＋$c_p$ 线）✓
- 【**环 [B] $P$（11 条，四组）**】①合法性：**B1** 充分≠必要（Newton/Turán 必要非充分；RH 为 $\Pi_1$ ⟹ 有限验证不构成证明）｜**B2** 正性即循环（W5 已封／W2 承重墙）；②能力边界：**B3** $\beta$-盲（**W1，唯一数学残差**，"检测≠排除"）｜**B4** support $>1$（W6 合并登记／W12 $=\frac23$，我方 $0.682$）｜**B5** 非自伴谱刚性（W11／L1 NO-GO；虚 Airy 振子反例）｜**B6** 信息墙（W8）；③输入—选择力：**B7** K2-E″（只给大小界/可和性/截断 ⟹ NO-GAIN；V113/V114 两次确认）｜**B8** 相位感知聚合缺口（单频压制可行 $\delta_0=2.93993$／$C_0=23.6114$／增益 $1.11\times10^5$；但 $M_R=\sum|b_j|=\infty$ ⟹ 障碍＝谱系数**可和性**，与截断/坐标无关 ⟹ 需零点对相关；E117/E121 已关）；④转换处：**B9** 均匀性（D1：Burnol 原文"uniformity as $A\to0$"三次出现；但 CONV2/CONV3 多处**撤回** ⟹ **非统一墙**）｜**B10** 振荡项（D3：$M(T)=O(1)\iff$ Lindelöf 级）✓
- 【**环 [C] $P\Rightarrow Z$（2 条）**】**C1** 古典但零杠杆（$P$ 本身 ≡ RH）｜**C2** 有限⟹无限传输失败（D5 moving-edge；W10 散射钉住＝第二次总封口）✓
- 【**元环 [M]（3 条）**】**M1** 消解式模式（E160 逐字："audit-and-reduce：只能产出负结果与等价关系，**没有生成步**"⟹ **反复复发的元难题**）｜**M2** 墙体汇聚（W3–W5 **三面一墙**；W6／W12 **同一对象**；W4 限定 DEAD ⟹ 三墙汇合 ⟹ **结构性非执行性**）｜**M3** 实现级自查（8 次实现错误 ⟹ "结果异常先怀疑自己的分支"）✓
- 【**§6 同一性（最关键的拆解结果）**】$B3\equiv B4$（W6 合并：support>1 ⟺ prime-pair ⟺ $X\le T$ ⟺ bandwidth-one ceiling ⟺ $0.682$ ⟺ $\frac23$ ⟺ FSC/MV）｜$B2\equiv C1$｜$B5\Rightarrow C2$｜$B8\Rightarrow$ 需要 $B4$ ✓
- 【**§7 两周增量对链的影响**】**无任何一环被关闭或推进** ⚠️：C-380（完成＋关闭，**不得**当 RH 进展；新增一条 [A] 负结果）｜算术接口负结果（加强 A1/A5）｜TLDC 冻结（**PL 门整批排除聚合类** ⟹ 加强 [B] 无候选）｜model-first 生成器路线耗尽（再次落到 B3/B4）｜A/B 空间解耦｜本轮池级清扫属 B 空间（仅新增方法论纪律）✓
- 【**项目级"最小最不坏"提法**（E102 §8 靶1）】"$\zeta$ 零点能否**不经解析延拓**被素数数据 canonically 识别？" ⟹ 绕开 $P$ 的循环形态，**但仍需 $\beta$-敏感** ⟹ 落回 **B3** ✓
- 【**一句话**】链的难点**不在任一环节的技术细节**，而在"$[B]$ 要求一个既充分又不循环、且能穿透 $\beta$-盲与 support-1 天花板的正性"——**而这两道天花板本身就是同一道墙** ✓✓
- 档：`docs/CHAIN-REAUDIT-2026-09-27-per-link-difficulty-decomposition.md`（**纯审计 · 零新术语 · 未动算** ✓）

**📋 C-392（2026-09-27 · **119 链逐环难点拆解**（空间 B 专用））** ✓
- 【**空间隔离（唐先生 21:32 令）**】**本档＝空间 B（119 线）专用** ✓；**与 RH 链（空间 A）严格分账** ✗（两空间证据不得互挪／不得并入同一论证）；RH 档已加对应隔离横幅 ✓
- 【**结论：难点分三侧**】**构造侧（$P_2$）卡在“实现达标”**｜**证明侧（$P_1$）被现有技术堵死**｜**结构侧只剩一个核** ✓
- 【**链骨（12 环）**】$L_0$ 目标/边界 → $L_1$ 基准码 → $L_2$ 四代数×代际 → **$L_3$ 实现自检门** → $L_4$ 数据卫生 → $L_5$ 整数形＝等价重参数化 → $L_6$ MIP → **$L_7$ 21 机制封口** → $L_8$ L3-α 残余链 → **$L_9$ 精确卡点** → **$L_{10}$ 可容许类** → $L_{11}$ 第二层 excess 记账 ✓
- 【**$L_3$★自检门（决定性）**】$K(10,1)\le120$ 已知 ⟹ $m{=}120$ 解必存在；实测 best\_unc＝**34/28/34/28/31/25** ✗ ⟹ **FAIL** ⟹ **一切 $m{=}119$ 的“找不到”无效** ✓；归因＝**能力**（4 缺口：能量只用 $|H|$／邻域无精确 $\arg\min$／tabu 未调参／无重启扰动）；速度非瓶颈（$8{\times}10^3$–$2{\times}10^4$ 步/秒）✓
- 【**$L_4$ 数据卫生**】`code119_candidate.txt` ＝ 119 词但**仅 1007/1024** 覆盖 ⟹ **非 119-witness** ✗（09-24 生成，**从未独立验证**）⟹ “历史 $n{=}10,R{=}1$ 结果”**仍只能是 120** ✓；`tabu_np.py` 崩溃 ⟹ `np120.log` 低 $k$ 行全坏 ✗
- 【**$L_5$／$L_7$ 结构性**】整数覆盖形＝**等价重参数化**（非松弛）；投影割＝covering 约束之和 ⟹ **正锥内割先验无力**（A-PROJCUT-1）✓；**21 机制封口** ⟹ **irreducible core ＝ Boolean covering feasibility** ✓
- 【**$L_6$ MIP**】int10c 900s：Dual **99.0** ／ Primal **138** ／ Gap **28.26%** ／ Nodes 3751 ⟹ MIP STOP；**有限时间 bound ≠ “119 不存在”** ✗
- 【**$L_8$ L3-α**】$9{,}381{,}251$ 全 residual 覆盖（$\tau\ge6$＋容量＋完整交叠）⟹ **COMPLETE FINITE CERTIFICATE** ✓；三定量事实 ⟹ $\tau(E)\ge5$；**但纯几何只到 $L\ge3$，第 4 单位需 $(A,E)$ 专有耦合** ⟹ **STOP（BFREEZE）** ✓
- 【**$L_9$★精确卡点**】要 $124\to123$ 需存在 $|S|{=}124,\ h{=}0,\ R\ge1$ 的状态（**等基数但带冗余** ⟹ cleanup 立即给 123）；现状只观测 $r{=}k{+}1$（$|S|{=}125$）⟹ cleanup 只把 125 拉回 124 ⟹ **瓶颈＝repair 能否产出“等基数带冗余的 124 码”**（**不是**“能不能删”——已证能删 ✓）；**唯一未观测事件＝neutral $\wedge R\ge1$** ✓✓
- 【**$L_{10}$★可容许类（证明侧）**】$E=\sum_x\delta(x)=\mathbf{285}$ **无条件强制**（$119\cdot11-1024$）⟹ “$E\ge286$”$\iff$“119-码不存在”$\iff P_1$ 本身（**无弱化目标**）✗；传播引理成立 ✓ 但 **ladder 数值证伪** ✗，且**不聚合**（不同中点可共享同一 $z$）⟹ $\delta$-型泛函被 **profile 恒等式钉死**（SUM-P1P4／AMEND-30 LOCAL-AVG-GATE／GAPTHEOREM）⟹ **唯一可容许者＝支撑敏感（跨中心）不等式** ✓✓
- 【**$L_{11}$**】第一层 STOP（**强化**）：最乐观 $q+\binom q2$ 在 $q{=}10$ 时 $=55\ll119$ ⟹ **第一层不可能产生 119 矛盾** ✓；**第二层＝唯一出口**，目标精确化为 **excess 记账（须 $\ge286$）** ⟹ **与 $L_{10}$ 的支撑敏感不等式是同一难点** ✓
- 【**一句话**】构造侧卡在**能力＋一个未观测事件**；证明侧卡在**可容许类只剩一条、且该条＝直接证 $P_1$**；结构侧只剩 **Boolean covering feasibility** ✓
- 档：`docs/CHAIN-REAUDIT-119-2026-09-27-per-link-difficulty-decomposition.md`（**纯审计 · 零新术语 · 未动算 · 未改门** ✓）

**🎯 C-393（2026-09-27 · **119 线 P1 全局不变量普查（四方向）＋ 杠杆判定**）** ✓
- 【**P0（外部逐字 ✓✓）**】`arXiv:2203.16901`（Wu–Chen, Discrete Math **347**(2) 2024）: *"It is still an open problem to determine the domination number $\gamma(Q_n)$ for $n\ge10$ and $n\ne2^k,2^k-1$"* ✓；Van Wee (1988) $\gamma(Q_n)\ge2^n/n$（$n$ 为 6 的倍数）；Wu–Chen 用 **Habsieger (1997) 同余性质** 改进为 $\gamma(Q_n)\ge\frac{(n-2)2^n}{n^2-2n-2}$ —— **但只对 $n\equiv0\bmod6$**，**$n=10\equiv4$ 不在内** ⚠️（待 R2 核 ✓）
- 【**$2^m$ 族对照**】van Wee **Corollary 1b** $K(2^r,1)=2^{2^r-r}$ ⟹ $n=8{:}32$ **精确已知** ⟹ $2^m$ 族无待证问题 ✓；$n=10$ 最佳下界档案记 **107（BÖW 2004）** ⚠️（档级，R2 重钉）
- 【**四方向普查结果**】① 全局 excess ＝ **恒等式**（$E=11|C|-1024$，是 $|C|$ 的**纯函数**）⟹ 单用无杠杆；**措辞已纠**（"$E\ge286$"$\iff|C|\ge120$，**非**"119-码不存在"；仅作**充分**路线 ✓）｜② **ALIVE ✓✓**（见下）｜③ Fourier／谱 ＝ **线性内容恰是整数性，非线性＝Booleanity** ⟹ **无新必要条件** ✗（模 11 定理：$\ker(T\bmod11)=\mathrm{span}\{\mathbf 1\}$；BQP 提升亦循环 ⟹ 等于直接加 $x_u\le1$）｜④ 距离分布 $A_i$ ＝ **被否证** ✗
- 【**② 的核心资产（P1-2 PASS ✓✓✓）**】**存在三个两两不等价的最优 $(8,32)_1$ 码**：$(A_1,A_2)=(0,16)$ **相同**、**全距离分布亦相同** $A=(0,16,160,176,64,48,32,0)$，**而 $J_7=64/128/256$** ⟹ **距离分布不决定 support-2 fingerprint** ⟹ "collapse 假设"被否证 ⟹ **分离只在坐标支撑层 ＝ 全新可区分维度** ✓✓；机制：载体＝**Type B**（$k=0$，两半为不交完美码）⟹ $q_{ij}$ 只落 $\{i,7\}$ 型 ⟹ $J_7=\sum_{i=0}^6q_{i7}^2$（16 的分拆平方和）⟹ $4^2\!\cdot\!4$／$8^2\!\cdot\!2$／$16^2$ 全解释 ✓
- 【**结构性难点（本档核心拆解）**】$n=8$ 杠杆依赖 (i) $n=2^m$、(ii) **Theorem 13**（两半＝长 $2^r-1$ 的完美码）；$n=10$：长 9 完美码**不存在**（$9=2^t-1\Longrightarrow2^t=10$ 非 2 幂）⟹ **无 Theorem-13 型构造** ⟹ **杠杆不直接迁移** ⚠️；$n=10$ 三条工具全不可用（vW 等号／完美码构造／反例发生器）⟹ 只剩**一般覆盖码** ✓
- 【**杠杆判定（诚实）**】在**已普查四族内**未获作用于任意 119/120-cover 的 P1 杠杆 ✓；**措辞纪律**："未产生"≠"不存在" ✗（V290）✓
- 【**R2 攻击点候选（不计算）**】**R2-1** 同余路线在 $n\equiv4\bmod6$（含 $n=10$）是否未覆盖 ⚠️（须正面 open 证据 ✓）｜**R2-2** 构造性给出 $n=10$ 的"同 $(A_1,A_2)$ 而 $J$ 分叉"两码（若不可能 ⟹ 本身即"$A$ 决定 $J$"新定理 ✓）｜**R2-3** $n=10$／$|C|=120$（$E=296$）的 $b$-profile 对照锚（只读不算 ✓）｜**R2-4** van Wee 证明**内部**等号分析对 $n=10$ 的类比 ✓
- 档：`docs/119-ATTACK-R1-2026-09-27-P1-global-invariant-census-and-leverage-verdict.md`（**纯普查／拆解 · 零新术语 · 未动算 · 未改门** ✓）

**🔧 C-394（2026-09-27 · **P1-5：Van Wee 分解 @ $n=10$** ＋ **R2-1 ＝ DROP**（理由翻转））** ✓
- 【**R2-1 ＝ DROP（唐先生 21:42 修正 ✓✓）**】**不是**"$n=10$ 未被同余路线覆盖"，而是**恰恰相反** —— **Habsieger 原文（FPSAC 95）明确研究 $n\equiv5$ 与 $n\equiv2,4\bmod6$**（逐字 ✓），$n=10$ 给 $K(10,1)\ge104$、Zhang 提至 $\ge105$ ⟹ **已处理且距 119 有 14–15 缺口** ✓；Wu–Chen 2024 的新方法**只对 $6\mid n$** ✓（其论文仍把 $n=10$ 所在的一般问题列为 open ✓）
- 【**Habsieger 体系（本轮新取 source ✓✓）**】$F_i(x)=\sum_{y\in S_i(x)}F(y)$；Lemma 1（Krawtchouk 型复合）；$\delta=N_0+N_1-1\ge0$；$\|\delta\|=(n+1)|C|-2^n$；**层公式** $(4)$：$\delta_i=(n+1-i)N_{i-1}+N_i+(i+1)N_{i+1}-\binom ni$；**Lemma 2**：$p$ 奇素数 $|n+1\Longrightarrow\sum_{i=0}^{p-1}\delta_i\equiv p-1\bmod p$；另列 $p\in\{2,3,4,5\}$ 同余 ✓
- 【**逐步分解表（饱和判定）**】一阶 excess ＝ **已饱和**（$\|\delta\|=11|C|-1024$；$119\Rightarrow285$）｜局部 congruence ＝ **已使用且自动满足**（$n+1=11$ 素数；$285=11\cdot25+10\equiv10\bmod11$ ✓ 无剩余切割力）｜二阶 intersection ＝ **部分使用**（Zhang pair-covering ＋ van Wee Lemma 3b/8；产出 104/105/107）｜等号条件 ＝ **$n=10$ 不适用**（$n\ne2^m$ ⟹ 整条等号链不适用；`ALG-VW` 已定位缺口）｜整数性余量 ＝ **线性内容已吃尽**（模 11 定理；$g$-形线性内容＝整数性，非线性＝Booleanity）｜**coordinate/support ＝ 未被使用 ⟸ 自由度所在** ✓
- 【**★A 型输出（本档核心 ✓✓）**】**命题（2 行可自证）**：由 (4)，$\{\delta_i\}$ 与 $\{N_i\}$ **逐点互相决定** ⟹ 凡只用 $\{N_i\}/\{\delta_i\}$（及其层和、模 $p$ 同余、对 $x$ 的聚合）的判据**完全由距离层决定** ✓；**见证（P12-PASS）**：三个最优 $(8,32)_1$ 码**全距离分布相同**而 $\sum_{i<j}q_{ij}^2=64/128/256$ ⟹ **距离层判据不可能区分它们** ⟹ **坐标支撑层承载距离层之外的信息** ✓✓ ⟹ van Wee／Habsieger／Zhang／Wu–Chen 的**全部量**都只依赖 $(N_i,\delta_i)$ 或其局部几何 ⟹ **支撑层的 $m_{ij},q_{ij},J$ 在其体系内结构性不可见** ＝ **未被 excess／congruence 理论吃掉的结构性自由度** ✓✓
- 【**A 型的两个条件（必须随结论引用 ✗）**】① **存在性未定**：P12-PASS 见证在 $n=8$；**$n=10$ 是否也有"同距离分布、异 $J$"未知** ⟹ 归 **R2-2**（若不存在 ⟹ 落 **B**）｜② **不等式转换未完成**：有维度 ≠ 有约束，须写成对任意 119-cover 成立的不等式（不得只在构造族内成立 ✗）
- 【**R2 状态**】$\text{R2-1 }\textbf{DROP}\ |\ \text{R2-2 }\textbf{ALIVE（下一档）}\ |\ \text{R2-3 }\textbf{HOLD}\ |\ \text{R2-4 }\textbf{已执行（A 型出）}$ ✓
- 档：`docs/P1-5-2026-09-27-van-Wee-proof-decomposition-at-n10-and-R2-1-DROP.md`｜（R1 档已补 §12 更新 ✓）

**🧩 C-395（2026-09-27 · **R2-2：$n=10$ support 层分离** ⟹ **分支①成立（构造性）** ＋ **自由坐标引理**）** ✓
- 【**结论**】**$A\not\Rightarrow J$ 在 $n=10$ 成立 ✓✓（构造性、零计算）**：$C=C_1\times\mathbb F_2^2$、$C'=C_2\times\mathbb F_2^2$，$C_1,C_2$ ＝ P12-PASS 的 $n=8$ 见证 ⟹ 二者均为 $\mathbb F_2^{10}$ **半径 1 覆盖码**、$|C|=|C'|=\mathbf{128}$、$A(C)=A(C')$（全距离分布相同），但 **support 指纹（$q$-多重集）不同** ✓
- 【**提升引理（3 行 · index-free ✓✓）**】$\widetilde C:=C\times\mathbb F_2$：**(L-1)** 覆盖性 ✓、$|\widetilde C|=2|C|$；**(L-2)** $d((c,b),(c',b'))=d(c,c')+\mathbf 1[b\ne b']$ ⟹ $\boxed{A_i(\widetilde C)=2[A_i(C)+A_{i-1}(C)]}$ ✓（可逆 ⟹ 等价关系被提升）；**(L-3)** $q_{ij}(\widetilde C)=2q_{ij}(C)$（$i<j\le n$）、$\boxed{q_{i,n+1}(\widetilde C)=2m_i(C)}$、$m_i(\widetilde C)=2m_i(C)$、$m_{n+1}(\widetilde C)=2|C|$ ⟹ $q$-多重集 $\{q_{ij}(\widetilde C)\}=2(\{q_{ij}(C)\}\cup\{m_i(C)\})$ ✓
- 【**★★自由坐标引理（本档第二产出 · 决定适用边界 ⚠️）**】$C=D\times\mathbb F_2$ 覆盖 ⟹ $D$ 覆盖且 $|C|=2|D|\ge2K(n-1,1)$；取 $n=10$、$K(9,1)=\mathbf{62}$ ⟹ $\boxed{|C|\le123\Longrightarrow C\ \textbf{不可分（无自由坐标）}}$ ✓✓（$|D|\le61.5<62$ 矛盾 ⟹ **§3 分离必然落在分离族 $|C|=128$，与 P1 相关范围 119–120 不相交** ✗）
- 【**附赠初等级资产**】任何 $\le123$ 词的 $\mathbb F_2^{10}$ 覆盖码**坐标不可约** ✓（＝ $K(10,1)\ge2K(9,1)$ 的构造侧对偶 ✓）
- 【**与 P1 的两门（诚实）**】门① **近最优范围内的分离** ⚠️ 未决（须 **R2-2′** 另找构造）；门② **$J$ 进覆盖条件**（$|C|=119\Longrightarrow J\in\mathcal J_{\rm impossible}$）⚠️ 未决，**且须建立在门①之上**（否则约束只作用于 $|C|\ge124$ 族，对 119 无着力 ✗）
- 【**停判（照唐先生三分支）**】分支①成立 ⟹ "继续寻找 $J$ 的覆盖不等式"，**但须先补 R2-2′** ⚠️
- 【**边界**】零计算 ✓（构造性推导）；**未碰** excess／Habsieger／Van Wee／Fourier ✓；**未改门** ✓；只引 P12-PASS 见证 ＋ 档案基准 $K(9,1)=62$ ✓
- 档：`docs/R2-2-2026-09-27-n10-support-layer-separation-constructible-and-free-coordinate-lemma.md`｜（R1 档补 §13 ✓）

**🔗 C-396（2026-09-27 · **R2-2$'$：近最优不可约 support 分离的机制构造**）** ✓
- 【**结论**】分支落位 **③ HOLD（带具体机制）**：既未构造出 $[119,123]$ 的分离对，也未证明其不存在；**但机制已得**（机制 ≠ 缺口，**缺口＝存在性**）✓
- 【**框架（§2 ✓✓）**】$\gamma_C(v)=\#\{(a,b)\in C^2:a\oplus b=v\}$（自相关）；$A_i=\sum_{|v|=i}\gamma(v)$ ⟹ **$A$ 只固定 $\gamma$ 的层和**；**支撑层 ＝ $\gamma$ 限制在坐标向量 $\{e_i\}\cup\{e_i\oplus e_j\}$ 上** ✓（$q_{ij}=\frac12\gamma(e_i\oplus e_j)$ ✓）⟹ **分离问题 ⟺ $\gamma$ 在坐标向量上的取值可否变而层和不变** ✓✓
- 【**载体：平移对族（§3 ✓）**】$C=D\cup(D+x)$ ⟹ $|C|=2|D|\in\{120,122\}\subseteq[119,123]$ ✓（**不受**自由坐标引理排除 ✓）；$\gamma_C(v)=2\gamma_D(v)+2\gamma_D(v\oplus x)$ ⟹ $\boxed{A_i(C)=2[A_i(D)+A_i(D,x)]}$ ⟹ **$A(C)=A(C')\iff A_i(D,x)=A_i(D,x')\ \forall i$** ✓（把 $A$-等价归约为**移位剖面相等** ✓）；支撑 $q_{ij}(C)=\gamma_D(e_i\oplus e_j)+\gamma_D(e_i\oplus e_j\oplus x)$ ✓
- 【**★机制（§4，3 行可证 ✓✓）**】取等距 $\sigma$（permute coords ⋊ translate）使 $\sigma(D)=D\oplus t$，令 $x'=\sigma(x)$、$C'=D\cup(D+x')$（**同一 $D$**）⟹ **(i)** $A_i(D,x')=A_i(\sigma D,\sigma x)=A_i(D,x)$ ✓（$\sigma$ 等距＋平移不变性）⟹ **$A(C)=A(C')$ ✓**；**(ii)** $q_{ij}(C')-q_{ij}(C)=\gamma_D(e_i\oplus e_j\oplus x')-\gamma_D(e_i\oplus e_j\oplus x)$ **一般非零**（当 $\sigma$ 不保坐标向量集）⟹ **support 变 ✓** ⟹ **A 不变、J 变** ✓✓（与 $n=8$ 的"两半对齐 $(\pi,e)$"**同一机制、换载体** ✓）
- 【**缺口（§6）**】**存在性** ⚠️：需 $D$ ＋ $\sigma,t,x$ 使 $D\cup(D+x)$、$D\cup(D+x')$ **均覆盖** $\mathbb F_2^{10}$（且 $C$ **不可分**，须逐例核 ✓）；**奇偶观察** ✓：平移对族只给**偶数** $|C|$ ⟹ $|C|=119$（奇）须换载体（如 $D\cup(D+x)\cup\{y\}$，得 $121/123$ ✓）
- 【**门②接口（§7）**】把 $J$ 写成 $\gamma$ 在坐标向量上的线性/二次泛函 ⟹ 与 §4 的 $A$-不变方向**正交**；**$A$-纤维（固定层和的自相关族）内的 $J$-变化 ＝ 门②的作用域** ✓
- 【**边界**】零计算 ✓；**未开门②** ✓；**未改门** ✓；§4 为**充分**机制（逆不主张 ✗）；只用本线既有资产 ✓
- 档：`docs/R2-2prime-2026-09-27-near-optimal-irreducible-support-separation-mechanism.md`

**🎛️ C-397（2026-09-27 · **R3：coordinate-labelled excess ＋ NO-GO 检验**）** ✓
- 【**范围**】只做 R3（把 $\delta\ge0$ 逐坐标化）；零计算；不开新课题；未开门② ✓
- 【**★R3-1 平移超额恒等式（3 行可证 ✓✓）**】$$\boxed{\sum_{x\in C\oplus e_i}\delta(x)=m+\mathrm{star}_i,\qquad \mathrm{star}_i:=\gamma(e_i)+\sum_{j\ne i}\gamma(e_i\oplus e_j)}$$ 证明：$x=c\oplus e_i$ 代换 ＋ $b(y)-1=\mathbf 1[y\in C]+\#\{j:y\oplus e_j\in C\}$ ＋ 对 $j$ 计数 ⟹ $\sum_j\gamma(e_i\oplus e_j)$ ✓；**对照 $i=0$：$\sum_{c\in C}\delta(c)=2N_1=A_1$（无标号 ✗）⟹ 标号内容只在 $i\ge1$ 出现** ✓
- 【**★R3-2 逐坐标上界（新形式 ✓✓）**】$\delta\ge0\wedge C\oplus e_i\subseteq H$ ⟹ $0\le\mathrm{star}_i\le11m-1024$ ⟹ $m=119$：$\mathrm{star}_i\le\mathbf{166}$ ⟹ 换对计数：$$\boxed{N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83}$$ （每坐标至多承载 83 个二阶关联 ⟹ 距离-2 质量**不能过于均匀摊开**）✓；全求和给 $N_1+2N_2\le830$ ✓（弱但真）
- 【**★R3-3 标号正定性（Gram/PSD ✓✓）**】$G_{ij}:=\langle\mathbf 1_{C\oplus e_i},\mathbf 1_{C\oplus e_j}\rangle=\gamma(e_i\oplus e_j)$ ⟹ $$\boxed{G\succeq0}$$（对角 $=\gamma(0)=m$，非对角 $=2q_{ij}$）⟹ $q_{ij}\le m/2$（$m{=}119$：$\le\mathbf{59}$）✓；扩展：$D_1=\{0\}\cup\{e_i\}\cup\{e_i\oplus e_j\}$（$|D_1|=56$）上的 $(\gamma(v\oplus w))_{D_1}\succeq0$ ✓
- 【**★★NO-GO 检验（唐先生要求）**】逐坐标量是否必然坍缩到 $A_1,\dots,A_{10}$？**结论：不坍缩 ✓✓** —— $\sum_i\mathrm{star}_i=A_1+2A_2$ **坍缩** ✓，但**单项 $\mathrm{star}_i$ 与 $G$ 的标号项不坍缩** ✓（$A$ 只给 $\sum_i\gamma(e_i)=A_1$、$\sum_{i<j}\gamma(e_i\oplus e_j)=A_2$；单项 $i$ 的 $N_1^{(i)},q_{ij}$ 不可由 $A$ 决定 —— P12-PASS 见证同 $A$ 异 $\{q_{ij}\}$ ✓）⟹ **二阶 coordinate-labelled 路线未被 $A_i$ 吃掉**（**不是** NO-GO 情形 ✓）
- 【**⚠️ 诚实标注**】所得约束**目前偏弱**——尚无 $m=119$ 的矛盾 ✗；**路线活着但未通** ✓
- 【**下一步两路径**】**甲**：需逐坐标**下界** $N_1^{(i)}+\sum_{j\ne i}q_{ij}\ge L_i$；若 $\exists i:L_i>83$ ⟹ 118/119 直接证否 ✓（候选来源：固定坐标 $i$ 的一维覆盖局部论证 ⚠️）｜**乙**：**三阶标号** $\sum_x F_iF_j\delta=\sum_{x\in C_i\cap C_j}\delta$（＝ $|C_i\cap C_j\cap C_k|$ 型二差相关 $\gamma^{(2)}$），与无标号的 $T=\sum\binom b3=Q+\sum\binom\delta3$ 形成标号/无标号对照 ✓
- 【**与既有档的关系 ✓**】`SECOND-ORDER-2026-09-25` 为**无标号**二阶链（$P=E+Q$、$P=2(A_1{+}A_2)$、$Q$ 奇、$A_1\le142$）；**本档为其逐坐标加标签**（非重复 ✓）
- 档：`docs/R3-2026-09-27-coordinate-labelled-excess-and-the-no-go-test.md`

**🪣 C-398（2026-09-27 · **R3-甲：十坐标桶 — 决定性问题的符号解答（NO）**）** ✓
- 【**决定性问题的答案 ＝ NO（可证 ✓✓）**】"现有 $A_1,A_2$ 约束能否推出 $A_1+2A_2>1660$？" ⟹ **NO**：$$\boxed{A_1+2A_2\le\mathbf{1555}<1660}$$ ⟹ **"总量版本"死掉** ✗（slack ≥ 105）✓
- 【**3 步符号推导 ✓**】(1) R3：$\sum_i\mathrm{star}_i=A_1+2A_2$ ✓；(2) 无标号链：$A_1+A_2=\frac{285+Q}2$ ⟹ $\boxed{A_1+2A_2=285+Q-A_1}$ ✓；(3) $b(x)\le|B_1(x)|=11\Rightarrow\delta\le10$ 且 $\sum\delta=285$ ⟹ 集中化（凸性）$Q\le28\binom{10}2+\binom52=\mathbf{1270}$ ⟹ $A_1+2A_2\le285+1270=\mathbf{1555}$ ✓✓；下界侧 $A_1+2A_2\ge143+1=144$ ⟹ **可行区间 $[144,1555]$** ✓
- 【**R3-2 诚实降级（必写）**】$\sum_i\mathrm{star}_i\le1555<1660$ ⟹ "每桶 $\le166$"在 $m=119$ **被蕴含**（slack ≥ 105）⟹ **逐坐标上界单用无 P1 杠杆** ✗✓（死的是"用总量平均逼单桶超限"这一**最粗**用法；R3 的**十桶结构＋标号恒等式＋PSD** 价值不变 ✓）
- 【**十坐标桶（照唐先生框架）**】桶 $B_i:=N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83$ ✓；$\sum_iB_i=N_1+2N_2=\frac{A_1+2A_2}2\le\mathbf{777}$ ✓ ⟹ 容量 $10\times83=830$ ⟹ **slack ≥ 53** ⟹ **容量版不紧** ✗（不能单靠"装不下"证否）✓
- 【**真正战场（按令不计算 ✓）**】整数对称 $10\times10$ 矩阵 $G$：$G_{ii}=119$、$G_{ij}=2q_{ij}\ge0$、$G\succeq0$ ＋ 桶约束 ＋ $A$-区间 ⟹ **不可行 ⟹ $K(10,1)\ge120$（P1）**；**可行 ⟹ 二阶 coordinate-labelled（含 PSD）不足以攻 119 ⟹ 进三阶（乙）** ✓；**攻击顺序**：先符号化，符号走不通才考虑 PSD 可行性计算 ✗
- 【**定向查重 ✓**】"1660" 在档案中**无内容命中**（仅行号）；"十坐标桶"／"$Q\le$ 型上界"**无先例** ⟹ 本档 (i) $1555$ 上界、(ii) 甲总量版死亡判定、(iii) 容量 slack ≥ 53 为新增 ✓
- 【**边界**】未计算 ✓（纯符号）；未做 PSD 可行性计算 ✓（照令）；未开门② ✓；未改门 ✓；**不声称** $K(10,1)\ge120$ ✗（V290 ✓）
- 档：`docs/R3-A-2026-09-27-ten-coordinate-buckets-symbolic-verdict-total-version-dead.md`

**🧮 C-399（2026-09-27 · **R3-甲 P2/P3：十桶＋PSD＋整数性的压缩形式**）** ✓
- 【**判定确认**】**总量版 DROP** ✗（$A_1+2A_2\le1555<1660$ ✓）｜**十桶＋PSD＋整数版 ALIVE** ✓
- 【**系统清单（八条 ✓）**】$G\succeq0$｜$G_{ii}=119$｜$G_{ij}=2q_{ij}$｜$q_{ij}\in\mathbb Z_{\ge0}$｜$B_i:=N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83$｜$\sum_iB_i=\frac{A_1+2A_2}2\le777$｜$A_1+2A_2=285+Q-A_1$、$Q\le1270$、$Q$ 奇 ⟹ $[144,1555]$｜$A_1=2N_1,A_2=2N_2$ ✓
- 【**★压缩形式 I（矩阵/谱）：PSD 有牙 ✓✓**】$G=mI+2\tilde Q$（$\tilde Q$ 零对角、$\tilde Q_{ij}=q_{ij}$）⟹ $$\boxed{G\succeq0\iff\lambda_{\min}(\tilde Q)\ge-\tfrac m2=-59.5}$$ 而 **Gershgorin＋桶约束只给 $\lambda_{\min}\ge-83$** ⟹ **PSD 严格更强（差 23.5）** ✓✓；$\mathrm{trace}\,\tilde Q=0\Rightarrow|\lambda_{\min}|\le59.5$ ✓；$2\times2$ 给 $q_{ij}\le59$ ✓
- 【**★压缩形式 II（$\mu$-线性/谱测度）**】$\mu(u):=|\widehat C(u)|^2\ge0$，$\gamma(v)=\frac1{1024}\sum_u\mu(u)(-1)^{u\cdot v}$ ⟹ $q_{ij}=\frac1{2048}\sum_u\mu(u)(-1)^{u\cdot(e_i\oplus e_j)}$ ✓；**距离层 $A_i=\frac1{1024}\sum_u\mu(u)K_i(u)$（Krawtchouk 层泛函）** ⟹ **二阶量（$A$ 与 $q_{ij}$）皆为 $\mu$ 的线性泛函** ✓✓；约束 $\mu(0)=m^2$、$\sum_u\mu(u)=1024m$、$\mu(u)=(m-2k(u))^2$（$k(u)\in\mathbb Z\cap[0,m]$）✓
- 【**★压缩形式 III（符号/相位：covering 的完整重述，无松弛 ✓✓）**】$g=b=\sum_{i=0}^{10}\mathbf 1_{C\oplus e_i}$、$\widehat g(u)=(11-2|u|)\widehat C(u)$（即模 11 定理的乘子 $T$）⟹ covering ⟺ $g\ge1$；码 ⟺ $\mathbf 1_C=F^{-1}(\widehat C)\in\{0,1\}$ ⟹ $$\boxed{\text{完整重述}:\ \widehat C:\mathbb F_2^{10}\to\mathbb Z\ \text{使}\ (i)\ F^{-1}(\widehat C)\in\{0,1\};\ (ii)\ F^{-1}\big((11-2|u|)\widehat C\big)\ge1}$$ ✓✓ —— **三分读数**：距离层 $=A=\mu$ 的 Krawtchouk 层泛函｜支撑层 $=q_{ij}=\mu$ 的坐标泛函｜**covering $=\widehat C$ 的符号（$\mu$ 看不见 ✓）**
- 【**可行性问题的精确陈述（本档不跑 ✓）**】是否存在零对角非负整数 $\tilde Q$（$\sum_{i<j}q_{ij}=N_2$）满足 $\lambda_{\min}(\tilde Q)\ge-59.5$ 与桶约束 ✓；**不可行 ⟹ $K(10,1)\ge120$（真 P1 ✓，因任一 119-cover 必给可行点）**；**可行 ⟹ 只说明二阶（含 PSD）不足 ⟹ 进三阶（乙）** ✗（不推出 119 存在 ✓）
- 【**边界**】未跑可行性计算 ✓（照令）；零计算；未开门②；未改门；不写 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R3-A2-2026-09-27-ten-bucket-PSD-integer-compressed-form.md`

**🔧 C-400（2026-09-27 · **R3-A3：修正钉死 ＋ 行容量压缩失败 ＋ 必要系统松弛性判定**）** ✓
- 【**修正 1（trace，照唐先生）**】$\mathrm{tr}\,\tilde Q=0$ **单独不给** 59.5 ✗；正确：$\mathrm{tr}\,\tilde Q=0\wedge G\succeq0\Longrightarrow-59.5\le\lambda_{\min}\le0$ ✓（两个来源不同，须分开写 ✓）
- 【**修正 2（$2\times2$）**】$m^2-4q_{ij}^2\ge0\Longrightarrow q_{ij}\le59.5\overset{\mathbb Z}{\Longrightarrow}q_{ij}\le\mathbf{59}$ ✓
- 【**保留（PSD 谱压缩）**】$G=mI+2\tilde Q$ ⟹ $\lambda_{\min}\ge-59.5$；桶＋Gershgorin 只给 $-83$ ⟹ **结构压缩增量 $-83\to-59.5$** ✓；**表述保留**：PSD 不是"又一个上界"，而是把十桶之间的**全局谱耦合**加入问题 ✓
- 【**R3-P 精确定义（照唐先生）**】$q_{ij}\in\mathbb Z_{\ge0}$、$q_{ii}=0$、$\sum_{i<j}q_{ij}=N_2$、$\sum_{j\ne i}q_{ij}\le83$、$\lambda_{\min}(\tilde Q)\ge-59.5$ ✓；逻辑方向：真实 119-cover ⟹ R3-P 可行 ⟹ **R3-P 不可行 ＝ 真 P1 反证 ⟹ $K(10,1)\ge120$** ✓
- 【**⚠️ 判定 B（本档新发现，要紧）**】**$N_2$ 在 R3-P 中自由（仅上界 388）⟹ $q\equiv0$（或 $N_2{=}1$ 最小配置）即可行点** ⟹ **R3-P 平凡可行 ⟹ 不能单独给 P1** ✗ ⟹ 须保留 labelled 数据 ⟹ 本档提出**最小有用松弛 R3-P$^{\ast}$**（外加 $\sum_iN_1^{(i)}=N_1$、$B_i\le83$、pair 区域 $N_1+N_2\ge72$／$N_1+2N_2\le777$／$N_1\le71$、$Q$ 奇）✓
- 【**★判定 A：行容量压缩失败 ✗（反例族 ✓✓）**】取 $\tilde Q=w(J-I)$（$w\le59.5$）⟹ $\lambda_{\min}=-w\ge-59.5$ 成立而**行和 $9w\le535.5$** ⟹ **PSD 单独不能把 83 压小** ✗（83 是**标号桶**约束，非谱约束）；唯一可证新界 $\sum_{i<j}q_{ij}^2\le34445$（弱，被 $q_{ij}\le59$ 支配）✗；**失败的结构原因**：桶 ＝ **标号（坐标分解）**约束｜PSD ＝ **非标号（谱）**条件 ⟹ 改进容量须用**更高阶标号数据**（$D_1$ 扩展 PSD／三阶 $\gamma$）✓
- 【**★★松弛性判定 ＋ 收敛性发现（✓✓）**】在 R3-P$^{\ast}$ 取具体可行点（$N_1=60$ 每坐标 6、$N_2=100$ 均摊 $q\approx2.2$、$B_i\approx26\ll83$、$\lambda_{\min}\gtrsim-2.2$）⟹ **R3-P$^{\ast}$ 亦松弛：可行区域远未被 covering 逼紧** ⟹ **该层级（必要条件的任何弱化）都不能给 P1** ✓；逼紧只在**极端超额集中**（$Q\to1270\Longrightarrow\sum_iB_i\to777\Longrightarrow$ 平均桶 77.7 逼近 83），但那仍是**必要**条件 ✓；⟹ **收敛性发现**：本线（R3 链）与**档案独立路线**（$g$-形／模 11／21 机制封口）**结论一致——真约束在 Booleanity／符号层** ✓✓
- 【**边界**】零计算 ✓；未跑 SAT/SDP ✓（照令）；未开门②；未改门；**不**声称 $K(10,1)\ge120$ 不可得 ✗（V290）；§6 收敛性为**路线一致性陈述**，非定理 ✓
- 档：`docs/R3-A3-2026-09-27-row-capacity-compression-fails-and-necessary-system-slackness.md`

**🅿️ C-401（2026-09-27 · **R4-P1：private-point deficit 引理** ⟹ 前提修正 ＋ 精确局部公式 ＋ 可删性判据 ＋ 聚合界）** ✓
- 【**范围**】只做 R4-P1；**不碰** $\mu$／PSD／Gershgorin／Fourier／SAT／124-deletion ✓；零计算 ✓
- 【**⚠️ 前提修正（必须，有证明 ✓✓）**】$P:=\sum_cp(c)=\#\{x:b(x)=1\}=n_1$ ✓；而 $n_1=\mathbf{739}+\sum_{j\ge3}(j-2)n_j\ \ge\mathbf{739}$ ✓（2 行：$\sum n_j=1024$、$\sum(j-1)n_j=285$）⟹ **"$P\le118$" 不可得 ⟹ 唐先生原设想的 "$119\le P\le118$" 计数路线死** ✗✓；**且平均每码字私有 $\ge739/119\approx6.21$** ✓；**私有计数完全由 $b$-profile 决定** ⟹ 与 R3 的"$\delta$-型泛函被 profile 钉死"**同型** ✓
- 【**★新结果 1：精确局部公式 ✓✓**】两球交 $\ne\varnothing\iff d\le2$、$|B_1\cap B_1|=2$ ✓；距离-1 邻居给 $\{c,c\oplus e_i\}$ ✓、距离-2 邻居给 $\{c\oplus e_i,c\oplus e_j\}$ ✓ ⟹（**midpoint 共享**）非私有集 $=\{c\}\cup\{c\oplus e_i:i\in S(c)\cup V(H_c)\}$ ⟹ $$\boxed{p(c)=10-\big|S(c)\cup V(H_c)\big|}$$ （精确，无估计 ✓）
- 【**★新结果 2：可删性判据 ✓✓**】$c$ 可删（$p(c)=0$）$\iff|S(c)\cup V(H_c)|=10\iff$ **十个坐标方向全被局部占用** ✓（与档案 $U(c)=\varnothing$／$R(C)$ 一致 ✓）
- 【**★新结果 3：不可约 ⟹ 聚合界 ✓✓**】WLOG 不可约（若 $\exists c:p(c)=0$ 则 $|C|=119\Rightarrow118$-cover $\Rightarrow K\le118$，更早结束 ✓）⟹ $\forall c:|S\cup V(H)|\le9$ ⟹ $$\boxed{\sum_c|S(c)\cup V(H_c)|=1190-n_1=451-\sum_{j\ge3}(j-2)n_j\le\mathbf{451}}$$ ⟹ **平均 $\le451/119\approx\mathbf{3.79}$ 个方向/10** ✓✓ —— 即每个码字平均只在约 4 个坐标方向上"局部被看见"，其余约 6 方向**既无距离-1 也无距离-2 邻居** ✓
- 【**新轴：codeword-labelled（谁的重复）✓✓**】R3＝**坐标标号**（哪个坐标对承载距离-2 对）；R4＝**码字标号**（哪个码字的球被占）✓；精确关系：$\sum_c d_1(c)=2N_1$、$\sum_c d_2(c)=2N_2$（**总量无新息** ✗）✓，**但逐 $c$ 的 $(d_1(c),d_2(c),|S\cup V(H)|)$ 不被总量决定** ✓✓ —— 正对应唐先生"$Q=\sum\binom\delta2$ 把'谁造成重复'忘掉了" ✓
- 【**下一步 R4-P1′（本档不跑）**】目标改写（**避免 union bound 真空** ✗）：直接用 $\sum_c|S\cup V(H_c)|\le451$ 与**局部图 $H_c$** 结构耦合；两条攻击面：(a) 把 451 与 excess 恒等式（285）及 $n_j$ 分布耦合；(b) 证某全局计数迫使某 $c$ 的 $|S\cup V(H)|\ge10$ ⟹ 可删 ⟹ $\bot$ ✓；**若两条都证不出 ⟹ 登记"codeword-labelled 局部层同样松弛"** ✗（与 R3-A3 同型收束）✓
- 【**边界**】零计算；未开②；未改门；不声称 $K(10,1)\ge120$ ✗（V290）；451 为**必要条件**非矛盾 ✓
- 档：`docs/R4-P1-2026-09-27-private-point-deficit-lemma-and-codeword-labelled-occupancy.md`

**🔺 C-402（2026-09-27 · **R4-P1b：三点层 T1/T2/T3 符号筛选**）** ✓
- 【**T1 ✓（用户参数化逐式验证）**】$a=d_{12},b=d_{13},c=d_{23}$；四类型计数 $n_{00},n_{10},n_{01},n_{11}$ ✓；反解 $$n_{11}=\tfrac{a+b-c}2,\ n_{10}=\tfrac{a+c-b}2,\ n_{01}=\tfrac{b+c-a}2,\ n_{00}=10-\tfrac{a+b+c}2$$ ⟹ **充要条件：$a+b+c$ 偶 ∧ 三角不等式 ∧ $a+b+c\le20$** ✓（次之 $a,b,c\le10$ 自动 ✓）；非退化 ⟹ $a,b,c\ge1$ ✓
- 【**★T2：$\tau\in\{0,1\}$（本档推导 ✓✓）**】$$\boxed{\tau=[\max(a,b)\le1]+n_{11}[a\le2\wedge b\le2]+n_{10}[a\le2\wedge n_{01}=0]+n_{01}[a=0\wedge b\le2]}$$ ⟹ 非退化下第 1、2 项**互斥**（$n_{11}\ge1\Rightarrow a=b=1\Rightarrow c=0$ 退化 ✗）⟹ $\tau\in\{0,1\}$ ✓；**$\tau=1\iff\max(a,b,c)\le2\iff\{c_1,c_2,c_3\}$ 是 $G_2$ 的三角形** ✓；可达型**恰四**：$\mathrm{perm}(1,1,2)$ 与 $(2,2,2)$ ✓ ⟹ **三点张量 $T_{abc}$ 支撑仅四型（很薄的对象 ✓）**
- 【**★T3-a：单三元组 FAIL ✗（须修正框架）**】$\tau$ 只依赖坐标四类型 ⟹ **由 $(a,b,c)$ 完全决定**（三球对坐标置换不变 ✓）⟹ "同 pairwise profile 而异 $\tau$" 在**单个三元组内不可能** ✗；**自由度只出现在张量分布层面** ✓
- 【**★T3-b：张量层 PASS ✓（新信息量已识别）**】$$\boxed{\sum_x\binom{b(x)}3=\sum_{\text{unordered triples}}\tau=6\,T_3(G_2)}$$ 而 $T_3(G_2)$ **不被 $A$ 决定**（边数 $N_1+N_2$ 只给 $|E(G_2)|$；**同边数异三角形数**为初等图论事实 ✓）⟹ **三点层确有超出二阶计数的自由度，内容 ＝ 距离-≤2 图 $G_2$ 的三角形计数** ✓✓；与档案恒等式一致：$\sum\binom b3=Q+\sum\binom\delta3$ ✓ ⟹ **三点层 ＝ 覆盖轮廓三阶矩** ✓
- 【**⚠️ 诚实限界（照唐先生 §7）**】$A\not\Rightarrow T$ **不是** P1 ✗；须 $T\in\mathcal T_{\rm cover}=\varnothing$ 或存在不可兼容模式 ✓；更冷现实：$\sum\binom b3$ 是 $\delta$-型泛函，档案已立"十类 $\sum_xf(\delta(x))$ 全被 profile 指纹钉住"（GAPTHEOREM ✓）⟹ **真问题转为"$b$-profile $\{n_j\}$ 是否被 $A$ 决定"**（**开放** ⚠️，本档不判 ✓）
- 【**★耦合目标（本档提出，可证伪 ✓）**】资源候选：(i) 局部占用预算 $\sum_c|S(c)\cup V(H_c)|\le451$（R4-P1 ✓）；(ii) excess 285 ✓；**形态**：三角形 $(c_1,c_2,c_3)$ 处三码字的 $V(H)$ 各含一个 type-11 方向 ⟹ **三角形消耗局部占用** ⟹ 若 $T_3(G_2)$ 下界（covering 迫使）与 451 上界冲突 ⟹ $\bot$ ✓✓；形式化目标：$\exists K_\ast>K^\ast$ 使 $K_\ast\le T_3(G_2)\le K^\ast$ ✓
- 【**Terwilliger 位置**】本档已完成 T1/T2/T3 ⟹ **先不开 Terwilliger SDP** ✗；**开它的门槛**＝§6 耦合若给出"三角形质量 vs 局部预算"的 $\bot$ ✓
- 【**边界**】零计算（$11^3$ 由公式解析完成 ✓）；未上 Terwilliger；未碰 R3 线／$\mu$／PSD／SAT；未开②；未改门；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R4-P1b-2026-09-27-triple-layer-gates-T1-T2-T3-symbolic-screening.md`

**🔻 C-403（2026-09-27 · **R5：三点层可证伪实验（$U$ 值集 ＋ 全局恒等式 ＋ 强制三角形）＋ 诚实对照**）** ✓
- 【**★产出 1：$U(a,b,c)$ 精确值集**】$U:=|B_1(c_1)\cup B_1(c_2)\cup B_1(c_3)|=33-I_{12}-I_{13}-I_{23}+\tau$ ✓（$I_{ij}=2\cdot\mathbf 1[d_{ij}\le2]$ ✓、$\tau=\mathbf 1[\max\le2]$ ✓）⟹ $$\boxed{U\in\{\mathbf{28,29,31,33}\}}$$（三对皆 $\le2$：28；恰两对：29；恰一对：31；零对：33 ✓）⟹ **浪费 $33-U\in\{0,2,4,5\}$** ✓；**故"三球并集太小"在单三元组层面不产生矛盾** ✗（容量账 $1276\ge996$ 松 ✓）
- 【**★产出 2：精确全局恒等式（与 1024/1309/285 接上 ✓✓）**】$$\boxed{1024=1309-2(N_1+N_2)+T_3-T_4+T_5-\cdots}\quad\Longleftrightarrow\quad\boxed{E=285=2(N_1+N_2)-T_3+T_4-T_5+\cdots}$$ ✓✓（$T_k:=\sum_{k\text{-子集}}|\text{共同球交}|$ ✓；高阶项**有限自动截断**（$k>11$ 交为空）⟹ **精确** ✓）；**读数**：285 ＝ 二阶层贡献 $2(N_1+N_2)$ 被三阶及以上**交替修正** ⟹ **三层在同一恒等式上耦合** ✓✓
- 【**★产出 3：强制三角形（无条件 ✓✓）**】$Q=\sum_x\binom{\delta(x)}2$ **奇** ✓（档案链：$P=E+Q$ 且 $P=2(A_1+A_2)$ 偶 ⟹ $Q\equiv E\equiv1\bmod2$）⟹ $Q\ge1$ ⟹ $\exists x:b(x)\ge3$ ⟹ 其覆盖者中任取三者两两 $\le2$ ⟹ 三角形 ⟹ $$\boxed{T_3(G_2)\ge1}$$ ✓✓
- 【**★修正（本档自查发现，两档同步）**】$\sum_x\binom{b(x)}3$ 是**无序**三元组 ⟹ $$\boxed{\sum_x\binom{b(x)}3=T_3(G_2)=Q+\sum_x\binom{\delta(x)}3}$$ ✓✓（**不是** $6T_3$ ✗；R4-P1b 已同步修正 ✓）⟹ $T_3\ge Q\ge1$ ✓
- 【**⚠️ 诚实对照（必须与该恒等式同引 ✓）**】`FIBER-2026-09-26`：$\sum_xP(x)^2$ **不被二阶数据决定（带证人）** ⟹ 本档 T3-b **同型，不主张为新** ✗；`TERM-2026-09-27`：$n=4$ 全枚举 480 例 ⟹ triple **邻域结构零变化** ⟹ **封存三阶耦合** ✗（封的是"邻域"对象；$n=5$ **无数据，不得断言不存在** ✓）；`KOPT4-6` 有 STAR/TRI ✓
- 【**本档真实增量 ✓**】(i) $U$ 值集；(ii) **全局恒等式（组合解释，R3 只有同源 $\delta$-型恒等式 ✓）**；(iii) $T_3\ge1$ 与 **STAR-叉桥接**（三角形 ⟺ 两距离-2 邻居共享恰一坐标 ✓）；＝三点层的**计数表述**（此前只有"邻域表述" ✓）
- 【**缺口（具体 ✓）**】须两侧夹逼 $L\le T_3\le U$ 且 $L>U$ ✓：**上界来源** (a) R4-P1 局部占用预算 $\le451$ ✓、(b) 恒等式可行性 $N_1+N_2\in[143,459]$ ✓、(c) STAR-叉计数 ✓；**下界来源目前仅 $\ge1$（弱 ✗）—— 这是本路线真缺口** ✓
- 【**边界**】零程序计算 ✓（全解析）；未碰 $\mu$/PSD/SAT/124-deletion；未上 Terwilliger；未开②；未改门；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R5-2026-09-27-triple-union-exact-values-and-the-global-inclusion-exclusion-identity.md`

**🔺 C-404（2026-09-27 · **R4-T：$\tau$ 公式修正 ＋ triple-distribution closure test（T1/T2/T3）**）** ✓
- 【**★修正（决定性 ✗✓）**】唐先生公式 $\tau=\frac{a+b-c}2+\mathbf 1[a=b=1]$ **缺因子** $\mathbf 1[a\le2\wedge b\le2]$ ✓；**反例** $(a,b,c)=(2,4,4)$：$r=\frac{2+4-4}2=1>0$ 但 $x=c_1\oplus e_i\ (i\in D_{12}\cap D_{13})$ 有 $d(x,c_2)=a-1=1$ ✓ 而 $d(x,c_3)=b-1=\mathbf 3>1$ ✗ ⟹ $x\notin B_1(c_3)$；且 $a=2>1\Rightarrow c_1\notin B_1(c_2)$ ⟹ **真值 $\tau=0$**，唐先生式给 1 ✗✓；同型反例族：凡 $\max>2$ 而 $r>0$ 者（$(4,2,4),(2,3,3)$ 等）✓
- 【**★正确式 ✓✓**】$$\boxed{\tau=\mathbf 1[\max(a,b,c)\le2]\ \Big(=r\cdot\mathbf 1[a\le2\wedge b\le2]+\mathbf 1[a\le1\wedge b\le1]\Big)}$$、$\tau\in\{0,1\}$ ✓；非退化下两项**互斥**（$n_{11}\ge1\Rightarrow a=b=1\Rightarrow c=0$ 退化 ✗）✓；**$\tau>0\iff$ 三点构成 $G_2$ 三角形** ✓
- 【**★T1 ✓**】$\tau=1$ 可达型**恰 4**：$\{\mathrm{perm}(1,1,2),(2,2,2)\}$ ✓；admissible 条件（$a+b+c$ 偶 ∧ 三角不等式 ∧ $\le20$）**唐先生正确** ✓
- 【**★T2 ✓**】marginal 方程：$\sum_{abc}N_{abc}\cdot\#\{i\le3:d_i=k\}=(m-2)A_k^{(u)}$ ✓（每距离-$k$ 无序对属 $m-2$ 个三元组 ✓）；$\sum N_{abc}=\binom m3$ ✓；**不决定 $N_{abc}$** ⟹ 三阶自由度存在 ✓（**＝FIBER 同型，非新** ✗）
- 【**★T3（诚实边界）**】$\sum_{\{c_1c_2c_3\}}\tau=\sum_x\binom{b(x)}3=\frac16(\sum_x\delta^3-285)$ ✓✓（**唐先生 §6/§7 公式正确** ✓；与本档 R5 修正一致：$\sum\binom b3=T_3$ **不是** $6T_3$ ✓；$T_3=Q+\sum\binom\delta3\ge Q\ge1$ ✓）；**但 $T_3=\sum_j\binom j3n_j$ 是 $b$-profile 的函数** ⟹ **T3 本身不提供超出 profile 的覆盖耦合** ✗ ⟹ **真问题＝$b$-profile $\{n_j\}$ 是否被 $A$ 决定** ⚠️（**开放**，＝FIBER/TERM 同一边界 ✓）
- 【**空间隔离 ✓**】已核 `E58-triple-sum-collapse.md` 属**空间 A（RH）** —— **同名冲突，不引用、不合并** ✓✗
- 【**档案对照 ✓**】`FIBER-2026-09-26`（三阶不变量带证人 ⟹ 同型，非新 ✗）；`TERM-2026-09-27`（$n=4$ 邻域零变化 ⟹ **封存**，封的是**邻域**对象 ✗；$n=5$ 无数据 ✓）；`KOPT4-6`（STAR/TRI ✓）
- 【**本档增量 ✓**】$\tau$ 公式修正 ＋ 正确二分 ＋ closure test 的诚实边界定位 ✓
- 【**边界**】零程序计算；未上 SDP/Terwilliger；未碰 R3 线/$\mu$/PSD/SAT；不跨空间；未开②；未改门；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R4-T-2026-09-27-tau-formula-correction-and-triple-distribution-closure-test.md`

**🔷 C-405（2026-09-27 · **R6：$K_4$／共同球心兼容性 ＋ 可实现性亏空层级 ＋ 团级 cap**）** ✓
- 【**★$K_4$ 反例（自证 ✓✓）**】取 $c_1{=}0,c_2{=}e_1{+}e_2,c_3{=}e_2{+}e_3,c_4{=}e_1{+}e_3\in\mathbb F_2^{10}$ ⟹ **两两距离皆 2** ⟹ $K_4\subseteq G_2$ ✓；共同球心 $x$ 须 $\in B_1(0)=\{0\}\cup\{e_j\}$，逐点排除（$x=0:d(0,c_2)=2$ ✗；$x=e_1:d(e_1,c_3)=3$ ✗；$x=e_2:d(e_2,c_4)=3$ ✗；$x=e_3:d(e_3,c_2)=3$ ✗；$x=e_j,j\ge4:d=3$ ✗）⟹ $$\boxed{\text{4 个 pairwise-close 码字}\not\Rightarrow\text{共同 radius-1 球心}}$$ ✓✓ —— **本线第一个真正的兼容性缺口** ✓
- 【**★唯一性定理 ✓✓**】$x\ne y$ 同为共同球心 ⟹ $\{c_i\}\subseteq B_1(x)\cap B_1(y)$，而 $|B_1\cap B_1|\in\{0,2\}$ ⟹ $k\ge3$ 不可能 ⟹ $\big|\bigcap_iB_1(c_i)\big|\le1$ ✓（可实现性＝**二值** ✓）
- 【**★团级 cap（Kleitman 直径定理，档级引用 ✓）**】直径 $\le2$ 的 $Q_{10}$ 子集最大 $\sum_{i\le1}\binom{10}i=11$，等号 $\iff$ 球 $B_1(x)$ ⟹ $$\boxed{\text{任一 }G_2\text{-团}\le11\ \text{点};\ 11\ \text{点}\iff\text{团＝某球}\iff b(x)=11}$$ ✓✓（把"局部 cap $b(x)\le11$"升级为**团级定理** ✓）
- 【**★可实现性亏空层级（新对象 ✓✓）**】$\Delta_k:=\#\{k\text{-cliques of }G_2\}-\sum_x\binom{b(x)}k\ge0$ ✓（定义性 ✓）；**定理**：$\boxed{\Delta_3\equiv0}$（每个三角形都被实现 ✓）；**$\Delta_4$ 可 $>0$**（§1 构型即一个未实现 $K_4$ ✓✓）；$\Delta_k$ 随 $k$ **单调不减** ✓；**局部化问题**：给定团 $K_j$，被多少个 $x$ 实现为 $S(x)$？答案 $\in\{0,1\}$ ✓ ⟹ $\Delta_k$ ＝ 未实现 $k$-团计数 ✓；$k=2$ 全实现 ✓、$k=3$ 全实现 ✓、$k=4$ **首个真缺口** ✓✓
- 【**★矩系统 ＋ 一处新结论 ✓✓**】$\sum n_j=1024$、$\sum jn_j=1309$、$\sum j^2n_j=\mathbf{1879}+2Q$ ✓（**唐先生 §5 公式正确** ✓：$1024+2\cdot285+(285+2Q)$ ✓）；**新结论**：$Q$ **被 $A$ 钉死** —— 由 $\sum_x\binom{b(x)}2=2(N_1+N_2)=285+Q$ ⟹ $\boxed{Q=2(N_1+N_2)-285}$ ✓✓ ⟹ $m_2$ 亦被 $A$ 钉死 ⟹ **profile 自由度始于三阶** $\sum_x\binom{\delta(x)}3$（＝$T_3-Q$）✓✓（与 FIBER 证人一致 ✓）
- 【**⚠️ 耦合诚实评估**】已有：$T_3$ collapse（→profile ✗）、$U$ 值集、全局恒等式（**恒真无约束力** ✗）、$\Delta_3=0$、$\Delta_4$ 可正；**缺口**：尚未找到 $\Delta_4$（或 $\sum\binom\delta3$）与 119 必要条件的**夹逼** ⚠️（＝R5 §5 同一缺口）；**可证伪耦合目标**：$\exists L>U:\ L\le\Delta_4\le U$ ✓；上界候选：团级 cap ＋ $\sum_j\binom j4n_j$ 的 profile 钉死部分 ＋ $\sum_c|S(c)\cup V(H_c)|\le451$ ✓；下界候选：§1 四面体构型**是否被迫使**（未证 ⚠️）、$N_1+N_2\ge143$ 能否推 $\Delta_4$ 下界 ✓
- 【**边界**】零程序计算；未上 SDP/Terwilliger；未开②；未改门；不跨空间；Kleitman 为**档级引用** ✓；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R6-2026-09-27-K4-common-centre-compatibility-and-realizability-deficit-hierarchy.md`

**🧩 C-406（2026-09-27 · **R7：$K_4$ 结构定理确认 ＋ 形状目录修正 ＋ $T_4$ STOP 判定**）** ✓
- 【**★结构定理确认（含权混合补全 ✓✓）**】平移使 $0\in K$；其余顶点 $\mathrm{wt}\in\{1,2\}$；$W_1,W_2$ 定义；约束 (i) $u\supseteq W_1$ ✓、(ii) $W_2$ 两两相交 ✓；**情形 A** $|W_1|{=}0$：$k\ge5\Rightarrow|W_2|\ge4\Rightarrow$ 非 triangle $\Rightarrow$ star $\Rightarrow$ 共坐标 $i\Rightarrow x{=}e_i$ 实现 ✓；**情形 B** $|W_1|{=}1$：$x{=}e_i$ 实现 ✓；**情形 C** $|W_1|{=}2$：$|W_2|\le1\Rightarrow k\le4$，且 $k{=}4$ 即 **square**（无共同球心 ✗）；**情形 D** $|W_1|\ge3$：$W_2{=}\varnothing\Rightarrow x{=}0$ 实现 ✓ ⟹ $$\boxed{\Delta_3=0;\ \Delta_4\ge0\ \text{可正};\ \Delta_k=0\ (k\ge5)}$$ ✓✓（**Helly 型阈值恰在 4**）；**未实现者恰两型（情形 A-triangle 四面体、情形 C square），且皆极大团** ✓✓
- 【**★形状目录（修正后正确计数 ✓✓）**】4 型：**star** $=\frac{2^{10}\cdot10\binom93}4=215040$ ✓（四顶点两两距离 2、四者对称 ✓）｜**claw** $=2^{10}\binom{10}3=122880$ ✓（中心＋三叶，型 $\{1,1,1,2,2,2\}$ ✓）｜**square** $=\frac{2^{10}\binom{10}2}4=11520$ ✓（型 $\{1,1,1,1,2,2\}$ ✓）｜**tetrahedron** $=\frac{2^{10}\binom{10}3}4=30720$ ✓（型全 2 ✓）；**可实现**：star（球心 $\notin K$ ✓）与 claw（中心即球心 ✓）；**不可实现**：square ✗、tetrahedron ✗ ⟹ $$\#K_4(G_2(Q_{10}))=\mathbf{380160}$$ ✓✓
- 【**✗ 三处修正（唐先生 §2）**】(3-a) $245760=215040+30720$ **漏** claw(122880) 与 square(11520) ⟹ 正确总数为 **380160** ✓（唐先生"从 $x$ 的 10 邻点取 4"只数 $x\notin K$ 的 star 型 ⟹ 未数中心属于团者 ✗）；(3-b) "可实现总数＝245760"**无效** ✗（$\sum_x\binom{b}4$ 是 $C$ 的函数且只数落在 $C$ 内的四元组 ✓；245760 为全空间常数 ⟹ 无可比性 ✗）；(3-c) 恒等式 $\Delta_4=245760-\sum_x\binom b4$ **不成立** ✗；**正确关系**：$$\Delta_4=\#K_4(G_2(C))-\sum_x\binom{b(x)}4$$（首项**码相关** ✗；全空间 380160 只当 $C=Q_{10}$ 时相等 ✓）
- 【**附赠 ✓**】star 与 tetrahedron 的**距离型完全相同**（六距全 2 ✓）而可实现性不同 ⟹ **同型异实现性**，与 P12-PASS 的"同 $A$ 异支撑"同型 ✓✓
- 【**★★R7 STOP 判定（关键 ✓✓）**】$T_4=\sum_j\binom j4n_j$；profile 级上界：在 $\sum(j{-}1)n_j=285$、$j\le11$ 下集中化 ⟹ $T_4\le28\binom{11}4+\binom64=28\cdot330+15=\mathbf{9255}$ ✓（对应 $Q=1270$ 极端 ✓ 自洽 ✓）；profile 级下界：$T_4=0\iff$ 所有 $b\le3\iff n_3=Q,\ n_2=285-2Q\ge0\iff Q\le142$ ✓（**相容** ✗）⟹ $$\boxed{\text{profile ＋ }A\ \text{只给 }T_4\in[0,9255],\ \text{两端皆相容} \Longrightarrow \textbf{该层级无 }T_4\ \text{非平凡界}}$$ ✓✓ ⟹ **触发唐先生 §5 STOP 规则：R6/R7 机制本身（profile 级）不足** ✗✓；**唯一出路须是真几何约束**（非 profile 型 ✓）；几何候选登记：① 团级 cap 与实现型计数耦合；② §1 极大三角/方形**是否被迫出现**？；③ $\sum_c|S(c)\cup V(H_c)|\le451$ ✓
- 【**档案对照 ✓**】$|\cap_3|\in\{0,1\}$（唯一性）**已在 `C3-119-2026-09-27` IA-1** ⟹ **不重复主张** ✗（引用 ✓）
- 【**边界**】零程序计算；未上 SDP/SAT/Terwilliger；未开②；未改门；不跨空间；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R7-2026-09-27-K4-shape-catalog-correction-and-T4-profile-STOP.md`

**🔒 C-407（2026-09-27 · **R7 状态锁 ＋ $K_4$ 亏空接口恒等式**）** ✓
- 【**★状态锁 ✓✓**】$$\boxed{\textbf{R7 = PROFILE-LEVEL STOP};\qquad \textbf{STRUCTURAL }K_4\textbf{-DEFICIT REMAINS OPEN}}$$（**不判整个 R6 机制 CLOSED** ✗；照唐先生 ✓）
- 【**★★接口恒等式（本档核心 ✓✓）**】由唯一性（$|\cap_3|\le1$，档案 `C3-119` IA-1 ✓）⟹ $T_4=\sum_x\binom{b(x)}4$ 与"已实现 $K_4$"一一对应 ✓；已实现者按球心是否属于该团分两类（$x\in K\Rightarrow$ **claw**；$x\notin K\Rightarrow$ **star**）⟹ $$\boxed{T_4=N_{\rm claw}+N_{\rm star}}$$ ⟹ 四族构成 $G_2(C)$ 内全部 $K_4$ 的**划分** ⟹ $$\boxed{\Delta_4(C)=\#K_4(G_2(C))-T_4=N_{\rm square}+N_{\rm tetra}}$$ ✓✓ —— **profile 量被完全消去** ✓✓
- 【**★四族目录（钉死；并给更干净推导 ✓）**】固定球心 $x$：$B_1(x)$ 的 4-子集分**含 $x$**（$=\{x\}\cup$3 邻点 $=$ **claw**，每 $x$ 有 $\binom{10}3=120$ ✓）与**不含 $x$**（$=4$ 邻点 $=$ **star**，每 $x$ 有 $\binom{10}4=210$ ✓）⟹ **claw $=1024\cdot120=122880$**、**star $=1024\cdot210=215040$** ✓✓（**无需对称商** ✓）；**square** $=\frac{2^{10}\binom{10}2}4=11520$ ✓、**tetrahedron** $=\frac{2^{10}\binom{10}3}4=30720$ ✓ ⟹ $\#K_4(G_2(Q_{10}))=\mathbf{380160}$ ✓；实现性：**claw/star ✓**（球心存在）、**square/tetra ✗**；**恒等校验**：$\binom{10}3+\binom{10}4=330=\binom{11}4$ ✓
- 【**满图层亏空 ✓**】$C=Q_{10}$：$b\equiv11\Rightarrow T_4=1024\binom{11}4=\mathbf{337920}=N_{\rm claw}+N_{\rm star}$ ✓ ⟹ 亏空 $=380160-337920=\mathbf{42240}=11520+30720$ ✓
- 【**R7 STOP 的精确含义 ✓✓**】STOP 对象＝"仅凭 $(n,|C|,\sum b,b\le11,Q,$ 既有 profile moment$)\not\Rightarrow$ 非平凡 $T_4$ 界" ✓；上端 $T_4^{\max}=28\binom{11}4+\binom64=\mathbf{9255}$ ✓；下端 $T_4=0$（$b\le3$，$Q\le142$ 相容 ✓）⟹ $T_4\in[0,9255]$ **两端皆相容** ✓；**但结构亏空 $N_{\rm square}+N_{\rm tetra}$ 不是 profile 量 ⟹ 不被此 STOP 触及** ✓✓
- 【**★下一次回来的精确攻击点（P1 candidate ✓）**】$$\text{119-cover}\Longrightarrow N_{\rm tetra}>0\ ?\quad\text{或}\quad N_{\rm square}+N_{\rm tetra}\ge L>0\ ?$$ ✓ —— **本线第一个非 profile 型（真几何）对象** ✓✓；**诚实边界 ⚠️**：本档**无** $N_{\rm square}+N_{\rm tetra}$ 的下界 handle；已知仅 ① 二者皆**极大团**（不可延拓 ✓）、② 与 $b$-profile **无关** ✓；可攻接口：$\sum_c|S(c)\cup V(H_c)|\le451$／团级 cap 与实现耦合／$N_1+N_2\ge143$ 能否逼出 square/tetra ✓
- 【**档案对照 ✓**】$|\cap_3|\in\{0,1\}$（唯一性）**仅在 `C3-119` IA-1 交叉引用** ⟹ 不重复登记 ✗✓；$K_4$ 反例／亏空层级＝`R6` ✓；四族目录＝`R7` ✓；**本档新增＝接口恒等式 ＋ 干净计数 ＋ 状态锁** ✓
- 【**边界**】零程序计算；未上 SDP/SAT/Terwilliger；未开②；未改门；不跨空间；不声称 $K(10,1)\ge120$ ✗（V290）
- 档：`docs/R7-LOCK-2026-09-27-status-lock-and-the-K4-deficit-interface-identity.md`

**🎯 C-408（2026-09-27 · **P1 攻坚：$N_{\rm tetra}>0$ —— 几何刻画 ＋ 中点定理 ＋ 可达反证 ＋ 上界**）** ✓
- 【**(P1) 未证成（诚实落判 ✗）**】$N_{\rm tetra}>0$ **未能证明**，亦未找到矛盾 ✗；**不声称**它成立 ✓（V290）
- 【**★结果 1／2：几何刻画 ＋ 中点定理 ✓✓**】**square** $=\{v,v{+}e_i,v{+}e_j,v{+}e_i{+}e_j\}=v+\mathbb F_2^{\{i,j\}}$ ＝**完整 2 维仿射子空间** ✓（对角线中点落在其**内部** ✗）；**tetra** $=v+\big(\mathrm{span}(e_i,e_j,e_k)\big)_{\rm even}$ ＝ **3 维 coset 的偶部** ✓✓；**★中点定理**：tetra 六对的中点（12 实例）**集合恰为该 3-coset 的奇部** $\{v{+}e_i,v{+}e_j,v{+}e_k,v{+}e_i{\oplus}e_j{\oplus}e_k\}$ ✓✓，且**每奇点恰为 3 对的共同中点** ✓
- 【**★结果 3：$\Delta_4=0$ 可达（反证约束 ✓✓）**】球型码 $C=B_1(x)$（非覆盖码 ✓）：任两点 $d\le2\Rightarrow G_2=K_{11}\Rightarrow\#K_4=\binom{11}4=330$ ✓；$b(x)=11\Rightarrow\binom{11}4=330$ ✓、$b(x{+}e_i)=2\Rightarrow\binom24=0$ ✓、其余 $b\le1$ ⟹ $T_4=330=\#K_4$ ⟹ **$\Delta_4=0$** ✓✓ ⟹ **不存在"任何码都有 $\Delta_4>0$"的普适逼迫** ✗ ⟹ **P1 必须使用 covering／近最优性的特异信息** ✓
- 【**★结果 4：上界（新 ✓）**】tetra 偶部中恰 3 点与给定奇点 $o$ 相距 1（第 4 点距离 3 ✓）⟹ 该三点在 $S(o)$ 内 ⟹ $\#\{T:o\in{\rm odd}(T)\}\le\binom{b(o)}3$ ⟹ $\sum_o\binom{b(o)}3\ge4N_{\rm tetra}$ ⟹ $$\boxed{N_{\rm tetra}\le T_3/4}$$ ⟹ $T_3\le28\binom{10}3+\binom53=3370\Rightarrow N_{\rm tetra}\le\mathbf{842}$ ✓（**上界**；P1 所求为**正下界** ✗ —— 方向相反 ✓）
- 【**⚠️ §2 配对级修正（本档自查 ✓）**】claw（$3\times$距1$+3\times$距2）与 square（$4\times$距1$+2\times$距2）**配对谱不同** ✗ ⟹ "亏空整体配对不可见"一语**不成立** ✗✓；**但** star ≡ tetra（六距全 2 ✓）成立 ✓；且 $N_{\rm square},N_{\rm tetra}$ 是**团计数**，**不由** $(N_1,N_2)$ 或任何 profile 矩决定 ✓
- 【**P1 精确剩余任务 ✓**】证"任一 119-cover 恰含至少一个 square/tetra 型极大 $K_4$"；**必须**用到：① 覆盖性（每点 $b\ge1$）② 近最优（$|C|=119,\sum b=1309$）③ 局部占用预算 $\sum_c|S(c)\cup V(H_c)|\le451$ ✓
- 【**P2 预告（照唐先生 ✓）**】若 tetra 假设不矛盾 ⟹ 转向 $N_{\rm square}+N_{\rm tetra}$ 的**联合 cap**：找 $(S(c),H_c)$ 对四类 $K_4$ 的容量约束 ✓；**反例警示登记**：球型码 $\Delta_4=0$ ⟹ "局部密集"本身**不**逼出亏空 ⟹ 须找**覆盖强制**的局部形状，而非"密"本身 ✓
- 【**边界**】零程序计算；未碰 $T_4$／$n_j$／profile 极值（照令 ✓）；未上 SDP/SAT/Terwilliger；未开②；未改门；不跨空间；不声称 $N_{\rm tetra}>0$ ✗
- 档：`docs/P1-TETRA-2026-09-27-tetrahedron-geometry-midpoint-theorem-and-achievability-of-zero-deficit.md`

**🩹 C-409（2026-09-27 · **勘误 C-408 ＋ 占用恒等式 ＋ avoidance 反证接口**）** ✓
- 【**勘误（照唐先生 ✓）**】C-408 §4 的 $T_3\le28\binom{10}3+\binom53=3370$（及 $N_{\rm tetra}\le842$）**不是无条件** ✗ ✓；它**依赖 profile-concentration 前提**（$28\times10+5=285$ ＝把 $E=285$ 集中成 28 个 $\delta{=}10$ ＋ 1 个 $\delta{=}5$）✓；**仅凭 $b\le11$ 得不到** ✗；勘误后表述：**在既有 profile-concentration 框架下** $T_3\le3370$、$N_{\rm tetra}\le842$ ✓（结论不变：仍为**上界**，不产生 P1 lower bound，不改变 STOP ✓）
- 【**★★占用恒等式（本档核心 ✓✓）**】由 R4-P1：$p(c)=10-|S(c)\cup V(H_c)|$、$\sum_c p(c)=n_1$、$n_1=739+\sum_{j\ge3}(j-2)n_j$ ⟹ $$\boxed{\sum_c\big|S(c)\cup V(H_c)\big|=451-\sum_{j\ge3}(j-2)n_j\ \le\ 451}$$（**恒等式，非猜测** ✓✓）
- 【**⚠️ 方向性纠正（重要 ✗✓）**】占用量是**恒等式锁定**的，**不是自由预算** ⟹ "avoidance $\Longrightarrow\sum|\cdot|>451$" **逻辑上不可能成立** ✗（上界恒真）；**可用方向是下界**：avoidance $\Longrightarrow\sum|\cdot|\ge\mathbf{452}$（covering 平均 $451/119\approx3.7899$ ⟹ **只差一个单位** ✓）；**但**由恒等式该陈述 $\iff\sum_{j\ge3}(j-2)n_j\le-1$ **不可能** ⟹ **本接口＝P1 的\*\*重述\*\*，不是减弱** ✗✓（诚实标注；价值在"一个单位的定量缺口"形态 ✓）
- 【**★avoidance 的第一个几何推论（新 ✓）**】$N_{\rm square}=N_{\rm tetra}=0\iff\forall c:A(c)=B(c)=0$ ✓；$A(c)=0$ 且 $i,j\in S(c)\Longrightarrow c{\oplus}e_i{\oplus}e_j\notin C$ ⟹ 距离-2 邻居坐标对中**至多一个**属 $S(c)$ ⟹ $$\boxed{d_2(c)\le45-\binom{|S(c)|}2}$$ ✓✓；**求和弱** ✗：$N_2\le2671$（劣于既有 $N_2\le388$ ✗）⟹ 单靠此不足以逼近刀锋，**须更强推论** ⚠️；但它是**本线第一个由 avoidance 产生的真几何约束（非 profile 型 ✓）**
- 【**⚠️ 重要副结论（诚实）**】占用预算与 $\{n_j\}$ **同源** ⟹ **不是独立几何 handle** ✗ —— 与 R7 STOP 同一形态 ✓；用它作 handle 会重演 STOP ✓
- 【**下一步（登记未做 ✓）**】① 找**比 $d_2(c)\le45-\binom{|S(c)|}2$ 更强**的 avoidance 局部推论（尤其 $B(c)=0$ 对 $\sum|S\cup V|$ 的直接压制）⚠️；② **必须避免再落回 profile 量** ✗；③ 候选：把 $b\ge4$ 的点与 avoidance 的局部形状禁令对撞；或用 $|S\cup V|$ 的**逐 $c$ 分布**（而非只和）✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-AVOID-2026-09-27-erratum-occupancy-identity-and-the-avoidance-interface.md`

**🎛️ C-410（2026-09-27 · **P1-MICRO：固定 $c$ 局部结构 —— 内部子立方体排斥定理 ＋ covering 步失效**）** ✓
- 【**★(α) 内部子立方体排斥定理（新 ✓✓）**】$A(c)=0$（无含 $c$ 的 square）∧ 相异 $i,j,x\in S(c)$ ⟹ $$\boxed{c\oplus e_i\oplus e_j\oplus e_x\notin C}$$ ✓✓**证明**：反设 $w=c{\oplus}e_i{\oplus}e_j{\oplus}e_x\in C$，则四点 $K=\{c{\oplus}e_x,\ c{\oplus}e_i,\ c{\oplus}e_j,\ w\}\subseteq C$ ✓；以 $v=c{\oplus}e_x$ 为基，三差分为 $e_i{\oplus}e_x,\ e_j{\oplus}e_x,\ e_i{\oplus}e_j$（皆重 2 ✓，两两相交**但不共点** ⟹ **tetra 型** ✗）；六距全 2 ✓ ⟹ $K=v+\big(\mathrm{span}(e_i,e_j,e_x)\big)_{\rm even}$ ⟹ **tetra ⟹ 与 avoidance 矛盾** ✓✓
- 【**★(α′) 合并形式**】与 R4-P1 合读：**在内部子立方体 $c+\mathrm{span}(S(c))$ 内，除 $c$ 与 $\{c\oplus e_i\}_{i\in S(c)}$ 外别无 $C$ 点** ✓✓（即内部子立方体内 $c$ 是"孤点＋一阶星"）；**注**：仅依赖 $A(c)=0$；对 distance $\ge4$ 的内部点**不主张** ⚠️
- 【**✗(β) 诚实失效报告：covering 步失效**】原链条 $S(c)\xrightarrow{\text{no square}}\text{缺失 }d_2\xrightarrow{\text{covering}}\cdots$ 的**第 2 步不成立** ✗✓：缺失点 $m=c{\oplus}e_i{\oplus}e_j$ 被 $c{\oplus}e_i\in C$ **自动覆盖**（$d(c{\oplus}e_i,m)=|e_j|=1$ ✓）⟹ **covering 不产生新约束、不迫使 $d_3$** ✗；**教训**：缺失点天生被一阶邻居覆盖 ⟹ 该链条**不可能**产生 $\sum|\cdot|$ 型占用冲突 ✗
- 【**★(γ) 对偶新上界 ✓**】$d_3(c)\le\binom{10}3-\binom{|S(c)|}3=120-\binom s3$ ✓✓（与 R4-P1 的 $d_2(c)\le45-\binom s2$ 对偶 ⟹ "内部方向的 $\ell$-层点被逐个排除" ✓）；聚合：$2N_3\le119\cdot120-\sum_c\binom{d_1(c)}3$（弱 ✗，尚无矛盾 ⚠️）
- 【**缺口 ⚠️**】① 定理**只用 $A(c)=0$**，未用 $B(c)=0$；② 未找到任何反证；③ 聚合仍弱 ✗
- 【**下一步候选（登记未做 ✓）**】① 用 $B(c)=0$ 对**非内部**方向的约束（如 $c{\oplus}e_a{\oplus}e_b{\oplus}e_c$ 与 $c{\oplus}e_a{\oplus}e_b{\oplus}e_d$ 并存是否逼出 tetra？）⚠️；② 把 (α′) 与 covering 的**距离-1 层**对撞（内部"太空" ⟹ 外部须承担覆盖 ⟹ 能否压出 $\sum|\cdot|$ 型冲突而**不落回** $\{n_j\}$？）⚠️
- 【**边界**】零程序计算；**未求和**（照令 ✓）；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-MICRO-2026-09-27-inner-subcube-repulsion-theorem-and-covering-step-failure.md`

**🔗 C-411（2026-09-27 · **P1-TWO：两点交叉分析 ＋ 自动覆盖机制级否定**）** ✓
- 【**★(1) 定向引理（新 ✓）**】$c'=c\oplus e_a\oplus e_b\ (a\ne b)$ ⟹ $$\big[a\in S(c)\iff b\in S(c')\big]\ \wedge\ \big[b\in S(c)\iff a\in S(c')\big]$$ ✓（2 行：$a\in S(c)\iff c{\oplus}e_a\in C\iff c'{\oplus}e_b\in C\iff b\in S(c')$ ✓）；**推论**：$\{a,b\}\subseteq S(c)\Rightarrow\{a,b\}\subseteq S(c')\Rightarrow$ square $\{c',c'{\oplus}e_a,c'{\oplus}e_b,c\}\subseteq C$ ✗ 与 $A(c')=0$ 矛盾 ⟹ $\{a,b\}\not\subseteq S(c)$ 且 $\not\subseteq S(c')$ ✓
- 【**★(2) 两点刚性（新 ✓✓）**】取 $c'=c{\oplus}e_a{\oplus}e_b$ 且 $a\in S(c),\ b\notin S(c)$ ⟹（定向引理）$b\in S(c'),\ a\notin S(c')$；逐项判定：$c\notin U'$（$a\notin S(c')$ ✓）、$c'\notin U$（$b\notin S(c)$ ✓）、$c{\oplus}e_i\in U'\iff i=a$ ✓、$c'{\oplus}e_j\in U\iff j=b$ ✓ ⟹ $$\boxed{C\cap(U\cap U')=\{c\oplus e_a\}}$$ ✓✓（**唯一公共码字 ＝ 公共一阶邻居**；两子立方体不共享中心、不共享任何二阶点 ✓）
- 【**★★(3) 机制级否定（路线级，有证明 ✓✓）**】**自动覆盖原理**：rigidity／avoidance 分析涉及的点全部满足"是码字"或"到某码字距离 ≤ 1"——① 码字本身 ✓ ② 其一阶邻居 ✓ ③ **中点**（$c{\oplus}e_i{\oplus}e_j$ 对 $i\in S(c)$ ⟹ $d(c{\oplus}e_i,\cdot)=1$ ✓，即 P1-MICRO (β) ✓）④ 两点构型的公共邻居（§2 ✓）⑤ square/tetra 顶点 ✓ ⟹ $$\boxed{\text{covering 只在"到所有码字距离}\ge2\text{"的点上有约束力};\ \text{本文全部局部构型皆}\le1\ ⟹ \textbf{自动满足}}$$ ⟹ **任何仅由 distance $\le3$ 局部构型导出的刚性，都不可能通过 covering 产生矛盾** ✗✓ —— **路线级结论**（非"未找到" ✓）；**解释**了本线反复的"局部有结构、无法闭环"（P1-MICRO (β)／P1-AVOID §3／R7 STOP ✓）—— **不是技巧不足，是机制边界** ✓✓
- 【**未闭 ✗ ＋ 尺度判断 ✓**】local rigidity $\not\Rightarrow$ covering 矛盾（§3 说明在 $\le3$ 尺度上**不可能**）⟹ **必须换尺度** ⚠️；可换尺度（登记未做）：① **远点覆盖**（到所有码字距离 $\ge2$ 的点 —— covering 唯一"有牙"处 ✓）；② 全局计数（须避免落回 profile ✗，见 R7 STOP ✓）；③ distance $\ge4$ 的内部点（(α′) 未覆盖 ⚠️）
- 【**边界**】零程序计算；未求和（照令 ✓）；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）；§2 前提（$a\in S(c),b\notin S(c)$）须显式保留 ✓
- 档：`docs/P1-TWO-2026-09-27-two-point-cross-analysis-and-the-automatic-coverage-mechanism-no-go.md`

**📐 C-412（2026-09-27 · **P1-D3：$d=3$ 最小检查核验 ＋ 被迫高层码字定理 ＋ NO-GO 作用域修正**）** ✓
- 【**★(1) 最小检查核验通过 ✓✓**】$c=0$、$x=e_a{\oplus}e_b{\oplus}e_c$（$d=3$）⟹ $B_1(x)=\{$3 个 weight-2$\}\cup\{x\}\cup\{$7 个 weight-4$\}$ ✓（照唐先生 ✓）；且 $B_1(c)\cap B_1(x)=\varnothing$ ✓✓（$d(0,x)=3$；$d(e_i,x)=2$ 或 $4$ ⟹ 皆 $>1$ ✓）—— 与 $d=2$ 情形 $|B_1\cap B_1|=2$ **本质不同** ✓✓ ⟹ $x$ 及其 1-邻域的覆盖**不能**由 $c$ 的 radius-1 邻域自动补掉 ✓
- 【**★(2) 精化（本档 ✓）**】$A(c)=0$ **只排除支撑含于 $S(c)$ 的 weight-2 点** ✓ ⟹ 三类 weight-2 邻居$x{\oplus}e_i$ 全被排除的**充要条件是 $\{a,b,c\}\subseteq S(c)$** ✓✓（非自动 ✓）
- 【**★★(3) 被迫高层码字定理（新 ✓✓，本线第一个正强制）**】$$\{a,b,c\}\subseteq S(c)\ \Longrightarrow\ \exists\,i\notin\{a,b,c\}:\ c\oplus e_a\oplus e_b\oplus e_c\oplus e_i\in C$$ ✓✓ **证明**：由 §2 与 (α)（$x\notin C$ ✓）⟹ $C\cap B_1(x)$ 只能落在 7 个 weight-4 点中 ⟹ $x$ 的覆盖迫使某 weight-4 码字存在 ✓；**性质**：此前全部结果为**界**（上界为主），本定理为**存在性强制** ✓
- 【**★(4) $d_4$ 计数下界（新 ✓，本线第一个下界）**】一个 weight-4 码字 $w=c{\oplus}S$（$|S|=4$）与 $d=3$ 点 $x_T=c{\oplus}e_{(T)}$ 距离 1 $\iff T\subset S$ 且 $|S\setminus T|=1$ $\iff T$ 为 $S$ 的 3-子集 ⟹ 每个 $w$ 至多覆盖 $\binom43=4$ 个待覆盖 $T$ ⟹ $$\boxed{d_4(c)\ \ge\ \Big\lceil\tfrac14\binom{s(c)}3\Big\rceil}$$ ✓✓；聚合 $2N_4=\sum_cd_4(c)\ge\frac14\sum_c\binom{d_1(c)}3$ ✓；**类型**：与 $d_2,d_3$ 的**上界**相反，此为**下界** ⟹ 方向可用（若另有 $d_4$ 上界即可夹逼 ✓）
- 【**★(5) C-411 NO-GO 作用域修正（诚实 ✓✓）**】C-411 §3 的"本文全部局部构型的点皆 $\le1$"**只对该档研究的构型类**（square／tetra／中点／公共邻居 ✓，其点皆为码字或其 1-邻居）成立 ✓；**$d=3$ 点不在其作用域内** —— $x$ 与 $B_1(c)$ 不相交 ⟹ 覆盖责任**真实存在** ✓✓ ⟹ **$d=3$ 路线不是 C-410 的重复；唐先生判定正确** ✓（"自动覆盖"检查 **PASS，未关闭** ✓）；**NO-GO 的正确表述**：covering 只在"到所有码字距离 $\ge2$"的点上有约束力，而 $d=3$ 点**可能**远离一切码字 ⟹ 约束真实 ✓
- 【**边界**】零程序计算；**未进入 tetra 共存分析** ✓（照唐先生"先做最小检查" ✓）；未上 SDP/SAT；未开②；未改门；不跨空间；**不声称**已产生矛盾 ✗（"没有自动覆盖" $\ne$"已产生矛盾" ✓）；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-D3-2026-09-27-forced-high-layer-codeword-theorem-and-the-no-go-scope-correction.md`

**🔀 C-413（2026-09-27 · **P1-D3b：共享判据核验 ＋ $C(s,4,3)$ 方向纠正 ＋ 零改进判定**）** ✓
- 【**★(1) 共享判据核验通过 ✓✓**】$y=c\oplus S$（$|S|=4$）同时覆盖 $x_{T_1},x_{T_2}$ $\iff d(y,x_{T_i})=1\iff T_i\subset S$ 且 $|S\setminus T_i|=1$ $\iff T_1\cup T_2\subseteq S$（$|S|=4$）$\iff|T_1\cap T_2|\ge2$ ⟹ $$\boxed{\text{共用一 weight-4 码字}\iff|T_1\cap T_2|=\mathbf 2\ (\text{此时 }S=T_1\cup T_2\ \textbf{唯一})}$$ ✓（$|T_1\cap T_2|=0,1$ 不能共享 ✓）
- 【**★(2) 结构澄清（本档 ✓）**】4-集 $S$ 的四个 triples 两两交 2 ✓（＝ tetra 的**面**组合学 ✓）；对应四点 $x_T=c{\oplus}e_{(T)}$ 满足 $d(x_{T_1},x_{T_2})=|T_1\triangle T_2|=2$ ✓、$d(y,x_T)=1$ ✓ ⟹ 四点是 $y$ 的四个邻居 ⟹ 按 R7 四族目录为 **star（已实现，球心 $y$）** ✓✓ ⟹ **该结构计入 $T_4=N_{\rm claw}+N_{\rm star}$ 而非 $\Delta_4$** ✓（forced-$d_4$ 结构耦合到 realized 计数 ✓）
- 【**✗(3) 方向性纠正（关键）**】covering-design 框架**结构正确** ✓（$F_4(c)$ 须覆盖 $S(c)$ 的全部 3-子集 ✓），但 $$\boxed{d_4(c)\ge C(s(c),4,3)\ \textbf{未成立}}$$ ✗✓ —— **原因：混合块（$j=|S\cap S(c)|=3$，即 3 内＋1 外）未被任何已证约束禁止** ⚠️：$j=4$ 块计入 $\binom43=4$ 个待覆盖 $T$ ✓、$j=3$ 块仅计入 $\binom33=\mathbf 1$ ✓、$j\le2$ 计入 0 ✗ ⟹ 容混合块的族其**块数可少于 $C(s,4,3)$** ✓ ⟹ **有效下界仍是容量界 $\lceil\binom s3/4\rceil$** ✓；$C(s,4,3)$ 属**上界侧参考**（方向须颠倒才自洽 ✓）
- 【**★(4) 数值现实检查：零改进 ✗**】$s\equiv2,4\ (\mathrm{mod}\ 6)$ 时 Steiner 系 $S(3,4,s)$ 存在 ⟹ $C(s,4,3)=\binom s3/4$ **恰为容量界** ✓✓；**关键例**：$s=\mathbf{10}$：$C(10,4,3)=30=\lceil\binom{10}3/4\rceil$ ✓（Witt $S(3,4,10)$ ✓）；$s=8$：$14=14$ ✓（$\mathrm{SQS}(8)$ ✓）⟹ **最大情形下 covering-design 升级给出恰好零改进** ✗✗；只有 $s\not\equiv2,4\ (\mathrm{mod}\ 6)$ 才有小差额（如 $s=7$：容量 9 vs 无 Steiner ⟹ $>9$；具体值档级 ⚠️）
- 【**现状 ＋ 下一步（诚实 ✓）**】已确立：① 共享判据；② 共享结构 ＝ 已实现 star（入 $T_4$ ✓）；③ $d_4$ 有效下界 ＝ 容量界 ✓；④ $C(s,4,3)$ 不作下界 ✗；**仍缺**：**独立的 $d_4$ 上界**（用于夹逼 ⚠️），且须**非 profile 型**（见 R7 STOP／C-409 ✓）；**本档未产生矛盾** ✗
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）；$s=7$ 具体值标档级 ✓；Witt／SQS 存在性为档级引用 ✓
- 档：`docs/P1-D3b-2026-09-27-sharing-criterion-verified-and-the-covering-design-direction-correction.md`

**📶 C-414（2026-09-27 · **P1-D4：球面覆盖恒等式 ＋ 独立 $d_4$ 上界的\*\*两类来源排除\*\***）** ✓
- 【**★(0) C-413 状态锁（照唐先生 ✓）**】**LIVE / P1 incomplete** ✗（未 CLOSED ✗）；链条压缩形态：D3 forcing $\Rightarrow$ 3-subset coverage demand $\Rightarrow d_4\ge\lceil\binom s3/4\rceil$；缺 **independent upper bound on $d_4$** ✗
- 【**★(1) 球面覆盖恒等式（新 ✓✓）**】令 $S_3(c)=\{x:d(x,c)=3\}$（$|S_3|=120$ ✓）⟹ $$\boxed{8d_2(c)+d_3(c)+4d_4(c)=120+E_3(c)}$$ ✓✓（$E_3(c):=\sum_{x\in S_3(c)}(b(x)-1)\ge0$ ✓）；**证明（逐类阴影计数 ✓）**：覆盖 $x=c{\oplus}u$（$|u|=3$）者必为 $c{\oplus}(u{\oplus}e_i)$，$|u{\oplus}e_i|\in\{2,4\}$ ⟹ 只能取重量 2／3／4（$|u{\oplus}v|\ge||u|-|v||$ 排除 1／5 ✓）；weight-2 码字覆盖 $8$ 个球面点（$i\notin\mathrm{supp}(v)$ ✓）、weight-3 覆盖仅自身 $1$ 个（奇偶性排除距离 1 ✓）、weight-4 覆盖 $\binom43=4$ 个（$i\in\mathrm{supp}(v)$ ✓）
- 【**✗(2) 方向判定：只给下界**】$E_3\ge0$ ⟹ $8d_2+d_3+4d_4\ge120$（**下界** ✓）；与 forced-$d_4$ 下界**同向** ⟹ **无 squeeze** ✗✓（本档**未**产生 squeeze ✗）
- 【**✗(3) 聚合 ＝ profile 级恒等式**】$$16N_2+2N_3+8N_4=14280+\sum_x\big(b(x)-1\big)d_3(x)$$ ✓（新恒等式 ✓；因 $\sum_cE_3(c)=\sum_x(b(x)-1)d_3(x)$ ✓）；左＝$A$-data ✓、右含 $b(x)$ 与 $d_3(x)$ 的**联合分布** ⟹ 仍属**容量／profile 侧**（与 C-409 占用恒等式同族 ✓）⟹ **不构成独立 handle** ✗✓
- 【**★★(4) 两类来源排除（本档最重要 ✓✓）**】① **覆盖类**：covering 为 $b\ge1$ 型（**单调下型**）⟹ 其推论天然为**下界**，结构上不可能给 $d_4$ 上界 ✗✓（本档球面覆盖实测确认 ✓）；② **容量类**：上界只能来自容量／计数型恒等式，而 C-409 已证占用类量与 $\{n_j\}$ **同源** ✗✓（R7 STOP 同形态 ✓）⟹ $$\boxed{\text{独立 }d_4\ \text{上界不能来自"覆盖类"或"容量类"这两大来源}}$$ ✓✓ ⟹ 若要继续夹逼，须找**第三类**独立全局资源约束（既非 $b\ge1$ 型、也非度数／占用型）⚠️
- 【**未判死 ✓**】路线**未**判定为死 ✗（照唐先生判据：仅当"独立上界不可能"才判死 ✓；本档只排除**两类来源** ✓）；下一步候选（登记未做）：① 第三类全局资源（$d_4$ 与 $G_2(C)$ 团结构／极大团计数耦合 ✓）；② 用 $B(c)=0$ 给 $d_4$ 侧约束 ⚠️；③ 检验新恒等式是否与已知 $A$-data 界冲突 ✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间；C-413 ＝ LIVE/P1 incomplete ✓；不声称 P1 成立 ✗（V290）；不声称 D3→D4 线已死 ✗
- 档：`docs/P1-D4-2026-09-27-sphere-covering-identity-and-the-two-source-exclusion.md`

**🩹 C-415（2026-09-27 · **P1-G2：$G_2$／刚性耦合 —— 勘误 ＋ 见证者分解 ＋ 重量-4 逃逸定位**）** ✓
- 【**✗(1) 勘误（P1-D3b §2 断言有误 ✓）**】四个 forced 点 $x_T$（$T\subset S,|T|=3$）满足 $T\subseteq S(c)$ ⟹ 由 $(\alpha)$ 得 $x_T\notin C$ ⟹ **皆非码字** ⟹ **不构成 $G_2(C)$ 的团、不计入 $T_4$** ✗✓（原文"已实现 star／计入 $T_4$"**撤回** ✓，已在 P1-D3b 加勘误横幅 ✓）；**仍成立**：四点两两距离 2、共享 $y$、构成 $G_2(Q_{10})$（**全图**）$K_4$（star 型）—— 但属全图结构、与 $C$ 无关 ✓
- 【**★(2) 见证者分解（新 ✓）**】forced 三元 $T\subseteq S(c)$ 须 weight-4 见证 $y=c{\oplus}S$（$T\subset S,|S|=4$ ✓）；**情形 A（外见证 $S\not\subseteq S(c)$）**：$S=T\cup\{i\}$，$i\notin S(c)$ ⟹ 其四个三元中仅 $S\setminus\{i\}=T$ 含于 $S(c)$ ⟹ **恰覆盖 $\mathbf 1$ 个 forced 三元** ✓✓；**情形 B（内见证 $S\subseteq S(c)$）**：四个三元皆 $\subseteq S(c)$ ⟹ **恰覆盖 $\mathbf 4$ 个** ✓ ⟹ 总需求 $\binom{s}3\le\#A\cdot1+\#B\cdot4\le4d_4(c)$ ⟹ **容量界 $\lceil\binom s3/4\rceil$ 存续** ✗（无增强 ✗）
- 【**★★(3) 逃逸定位（关键 ✓✓）**】$(\alpha')$（P1-MICRO）的证明**只覆盖重量 2（$A(c)=0$）与重量 3（$(\alpha)$）** ✗；**重量 $\ge4$ 未证** ⚠️ ⟹ **情形 B（$S\subseteq S(c)$，即 $e_{(S)}\in\mathrm{span}(S(c))$）未被任何已证命题排除 ⟹ 它就是逃逸口** ✓✓；**同型逃逸三处**：① P1-D3b 的 $j=3$ 混合块 ✓ ② $C(s,4,3)$ 不作下界的原因 ✓ ③ 本档情形 B ✓ ⟹ 三者同一形态："**溢出／内部块打散计数**" —— 本线反复的真正障碍 ✓✓
- 【**★★(4) 锐化后的单一问题（P1-D4b ✓✓）**】$$\textbf{P1-D4b}:\ \text{是否存在 }c\oplus u\in C\ \text{与 }A(c)=0\ \text{共存，其中 }u\subseteq S(c),\ |u|=4\ ?$$ **不能** ⟹ $(\alpha')$ 扩至重量 4 ⟹ 情形 B 消失 ⟹ $\boxed{d_4(c)\ge\binom{s(c)}3}$（**较容量界强 4 倍** ✓✓）；**能** ⟹ 需显式构造 ✓（容量界即最优 ✗，**亦是明确结论** ✓）；**为何已证部分不覆盖**：含 $c{\oplus}u$ 的 square 其余顶点为重量 2／3（皆排除 ✓），含 $c{\oplus}u$ 的 tetra 其余顶点为重量 2／**6**（重量 2 排除 ✓，**重量 6 未排除** ✗）⟹ 需**新局部论证（重量 6 层耦合）** ⚠️
- 【**现状 ✓**】C-414 保持 **LIVE** ✓；第三类来源（图结构／刚性耦合）**确实咬合** ✓，但其咬合**被重量 4／6 逃逸口门控** ⚠️；已确立：外见证 1 对 1 ✓、容量界存续 ✓、逃逸口精确位置 ✓✓、三处同型逃逸 ✓；未确立：$d_4$ 上界 ✗、P1-D4b（未决 ⚠️）、无矛盾 ✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）；不声称 D3→D4 线已死 ✗；§1 勘误须与 P1-D3b 并列引用 ✓
- 档：`docs/P1-G2-2026-09-27-witness-decomposition-and-the-weight-4-escape-location.md`

**🧪 C-416（2026-09-27 · **P1-D4b ＝ YES 型（附显式反例）／内部 weight-4 逃逸合法**）** ✓
- 【**★★结论：P1-D4b ＝ YES** ✓✓】存在 $c\oplus u\in C$（$u\subseteq S(c),|u|=4$）与 $A(c)=0$ **共存** ⟹ **NO 型（$d_4(c)\ge\binom{s(c)}3$）不可得** ✗ ⟹ 容量界 $\lceil\binom s3/4\rceil$ ＝这条局部路线的**自然极限** ✓
- 【**★显式反例（12 点 ✓✓）**】$$C_0:=\{0\}\cup\{e_i:1\le i\le10\}\cup\{y:=e_1{\oplus}e_2{\oplus}e_3{\oplus}e_4\}$$ **逐项核验**：① $S(0)=[10]$ ⟹ $u=\{1,2,3,4\}\subseteq S(0)$ ✓；② $A(0)=0$ ✓（无重量 2 点）；③ $(\alpha)$ 在 0 成立 ✓（无重量 3 点）；④ $A(y)=0$ ✓（$S(y)=\varnothing$）；⑤ **全 avoidance** $N_{\rm square}=N_{\rm tetra}=0$ ✓✓（squares 需重量 2 点 ✗；tetras 需重量 2／3／5／6 ✗ ⟹ 逐基 0／$e_i$／$y$ 三类皆排除 ✓）；**允许的 $K_4$**：$\{e_1,e_2,e_3,e_4\}$ ＝ star（中心 $0\notin K$ ✓ 已实现 ✓）、$\{0,e_i,e_j,e_k\}$ ＝ claw（中心 $e_i\in K$ ✓ 已实现 ✓）⟹ 非 square／tetra ⟹ 不被 avoidance 禁止 ✓（与 R7 目录一致 ✓）
- 【**★推论 1：局部极限 ✓**】avoidance 层面无法改进容量界 ✗；照唐先生 YES 型判据：**这不是"证明失败"，而是明确证明内部块是合法逃逸机制** ✓✓
- 【**★推论 2：预期的 weight-6 强制不存在 ✓**】$C_0$ 含内部 weight-4 码字、满足全 avoidance，且**不含任何重量 5／6 点** ⟹ **局部层面不存在由内部 weight-4 码字强制的 weight-6 配置** ⟹ 该接口**不成立** ✗✓
- 【**★★推论 3：$(\alpha')$ 可证不能扩到重量 4 ✗✓**】若 $(\alpha')$ 扩至重量 4：$C_0$ 中 $\mathrm{span}(S(0))=\mathbb F_2^{10}$ ⟹ 断言应为 $C_0\subseteq\{0\}\cup\{e_i\}$ ✗，而 $y\in C_0$ ⟹ **矛盾** ⟹ **重量-4 扩张被显式反例证否** ✓✓（解释 C-415 §3 逃逸口**不能被修补** ✓；且与全 avoidance 相容 ✓）
- 【**⚠️ 诚实边界 ✓**】$C_0$ **不是覆盖码** ✗（如 $e_1{\oplus}e_2{\oplus}e_5$ 到一切码字距离 $\ge2$ ✓）⟹ **covering 特异性未被触及** ⚠️ —— 本反例只证明"**avoidance 层面**"逃逸合法，**不**证明 119-cover 中存在此构型 ✗
- 【**合读 ✓**】下界侧（容量界）到顶 ✓；上界侧被单调性挡住（P1-D4 §4 ✓）⟹ **D3→D4 夹逼在局部层面关闭** ✓；**全局层面未决** ⚠️；**无矛盾** ✓；C-415 保持 **LIVE** ✓（P1-D4b ＝ YES 已决 ✓）
- 【**🔖 空间纪律（照唐先生 23:12 令 ✓）**】`tech_word_check.sh` 输出跨空间 ⟹ 本档回查节**按空间分栏**：`显式反例` 命中 19（本线 **1** ＝ `R6-…` ✓／空间 A 18 **不计** ✗）、`逃逸口` 命中 38（本线 **1** ＝ `P1-G2-…` ✓／空间 A 37 **不计** ✗）、`重量6层`／`局部极限`／`合法逃逸` 皆 0 ⟹ 本档新增 **0** ✓；规则已固化 `TOOLS.md` ✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间；不声称 P1 成立 ✗（V290）；不声称线已死 ✗
- 档：`docs/P1-D4b-2026-09-27-internal-weight-4-escape-is-legal-explicit-counterexample.md`

**🔵 C-417（2026-09-27 · **P1-COV：状态锁 ＋ 球面恒等式族 ＋ 度数决定判定**）** ✓
- 【**★(0) 状态锁（照唐先生 23:15 ✓）**】**C-415 LIVE** ✓；原局部 P1 **已达自然极限** ✓；下一步**必须换成 covering-specific 全局机制** ✓；**C-416 关闭的只是**"用 avoidance 禁掉内部 weight-4"的**局部机制** ✓ —— **不是**关闭 119 本身 ✗，**不是**证明内部 weight-4 在 119-cover 中存在 ✗✓
- 【**★★(1) 球面恒等式族（新，已核验 ✓✓）**】$k=1,\dots,10$：$$\boxed{(11-k)\,d_{k-1}(c)+d_k(c)+(k+1)\,d_{k+1}(c)=\binom{10}k+E_k(c)}$$（$E_k(c):=\sum_{x\in S_k(c)}(b(x)-1)\ge0$ ✓、$d_{11}\equiv0$ ✓）；**推导**：$|u\oplus v|\equiv k+j\ (\mathrm{mod}\ 2)$ ⟹ 仅 $j\in\{k-1,k,k+1\}$ 贡献 ✓；系数 $11-k$／$1$／$k+1$（分别由 $v\subset u$、$v=u$、$u\subset v$ ✓）
- 【**★(2) 四例核验（满空间 sanity ✓✓）**】$k=1$：$E_1(c)=d_1(c)+2d_2(c)$ ✓（**精确恒等式** ✓）；$k=2$：$9d_1+d_2+3d_3=45+E_2$ ✓；$k=3$：$8d_2+d_3+4d_4=120+E_3$ ✓（＝P1-D4 §1 ✓）；$k=4$：$7d_3+d_4+5d_5=210+E_4$ ✓；**满空间** $C=\mathbb F_2^{10}$（$b\equiv11$ ⟹ $E_k=\binom{10}k\cdot10$ ✓）：$110=110$ ✓、$495=495$ ✓、$1320=1320$ ✓、$2310=2310$ ✓ —— **四例两侧全等** ✓✓
- 【**✗(3) 度数决定判定（诚实 ✓）**】该族把 $\{E_k(c)\}_{k=1}^{10}$ **完全决定**于局部度数 $\{d_j(c)\}$ ⟹ **"球面超额"无独立自由度** ⟹ 不能用"$E_k\ge0$"再榨新约束（那只是重述度数关系）⟹ 与 C-409 的"占用预算与 $\{n_j\}$ 同源"**同一主题** ✓✓
- 【**⚠️(4) 全局形式 ✗**】$2(11-k)N_{k-1}+2N_k+2(k+1)N_{k+1}=119\binom{10}k+\sum_x(b(x)-1)d_k(x)$ ✓；$k=1$：$2N_1+4N_2=\sum_x(b(x)-1)d_1(x)$ ✓（满空间核验 $10240+92160=102400=1024\cdot100$ ✓✓）；**左侧 $A$-data、右侧含 $b$ 与 $d_k$ 联合分布** ⟹ **profile 级、不构成独立 handle** ✗ ⚠️；**未产生新全局约束** ⚠️
- 【**净贡献 ✓✓**】把"**球面超额**"这一整类**显式判定为度数决定** ✗ ⟹ 搜索空间进一步压缩：**下一步须找的量不得由 $\{d_j(c)\}$ 或 $\{N_j\}$ 决定** ✓✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间（回查已按空间分栏 ✓）；不声称 P1 成立 ✗（V290）；不声称 119-cover 中存在内部 weight-4 ✗
- 档：`docs/P1-COV-2026-09-27-sphere-identity-family-and-degree-determination-verdict.md`

**🚦 C-418（2026-09-27 · **C-418 预筛门（机械可执行）＋ 首轮过门筛**）** ✓
- 【**★★(1) C-418 预筛门（照唐先生 23:17 ✓✓）**】**候选量 $Q$ 若由逐位置度数多重集 $\{(d_1(c),\dots,d_{10}(c))\}_{c\in C}$ 或其任何聚合（$\{N_j\}$／$\{n_j\}$）决定 ⟹ 直接 STOP** ✗；**附注**：由 C-417 恒等式族，$\{E_k(c)\}$ 已由逐位置度数决定 ⟹ **球面超额族被强读法即拦下** ✓✓；C-409 占用族亦同 ✓；**正向必需判据**（至少其一）：① 交叉结构 ② 关联结构（二阶/高阶关联矩阵、共同邻居分布）③ 谱/特征值 ④ 覆盖映射非均匀性（witness 重叠拓扑）⑤ 全局拓扑/同调类 ✓
- 【**门的三步 ✓**】S1：仅依赖 $\{(d_j(c))\}$／$\{N_j\}$／$\{n_j\}$ ⟹ STOP ✗；S2：依赖**排列方式／交叠模式／谱数据** ⟹ PASS 门 ✓；S3：PASS 后仍须过**范围闸**（近最优区间 $119\le|C|\le123$ 是否可达，受**自由坐标引理**限制 ✓）
- 【**已确认被拦下的族 ✓**】① $b$-profile 族（含 $b$ 矩、球面超额 ✓）；② 占用/度数族（$\sum_c|S(c)\cup V(H_c)|$、$d_j(c)$ 聚合 ✓）；③ 球面超额族（C-417 ✓）；④ 距离分布族（$\{N_j\}$ 及其线性函数 ✓）⟹ **"再做一次球面/占用/profile 型计数"已被结构性排除** ✓✓
- 【**★首轮过门筛 ✓**】① **内部见证计数** $N_{\rm int}(c):=\#\{T\subseteq S(c):|T|=3,\ \text{其见证含于 }S(c)\}$（P1-G2 §2 情形 B ✓）：依赖"哪些三元组被内部块覆盖"⟹ **排列级、非度数决定 ⟹ PASS 门** ✓✓ 且**直接绑定 C-415 逃逸口**（最自然的下一个量 ✓）② **码字交图 $G_2(C)$ 的谱**：$N_1,N_2$ 只给边数、**不能定谱 ⟹ PASS** ✓（P12-PASS 的三例同 $A$ 异 $J_7$ 正是谱型分离 ✓）③ $q_{ij}$ 支撑指纹：**PASS 门**（已证非 $A$-data 决定：P12-PASS $n=8$ ✓、R2-2 提升引理可升 $n=10$ ✓）**但被范围闸拦** ✗ —— 自由坐标引理：$C=D\times\mathbb F_2$ 型分解 ⟹ $|C|\ge2K(9,1)=124$ ⟹ **近最优区间 $119$–$123$ 不可达** ✗✓ ⟹ STOP（范围）④ $\sum_{w\in C}\binom{b(w)}2$：$b(w)=1+d_1(w)$ ⟹ 由逐位置 $d_1$ 多重集决定 ⟹ **被门拦下** ✗✓（**示范**：看似"二阶共同邻居总数"实为度数函数 —— 门有效 ✓✓）⑤ **同调类**：须先给出 119-cover 特异的复形（见证超图／码字交复形 ✓）⟹ 过门前不成立 ⚠️
- 【**短名单（登记未做 ✓）**】优先级：① $N_{\rm int}(c)$（PASS 门 ✓ 绑定逃逸口 ✓）② $G_2(C)$ 谱（PASS ✓，须找与 119 约束的接口 ⚠️）③ 见证超图同调（待建 ⚠️）；**通用纪律**：任何新候选**先过门**，不得先推导再发现只是 profile 恒等式 ✗（照唐先生 23:17 ✓）
- 【**定位与边界 ✓**】C-418 为**筛查判据**、**非新数学命题** ✓；**本档未产生新约束** ✗（诚实 ✓）；零程序计算；未上 SDP/SAT；**未改** closure gate／nogo gate（若唐先生要求可并入，须显式批准 ⚠️）；不跨空间；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-SCREEN-2026-09-27-C418-pre-screen-gate-and-first-pass.md`

**🧷 C-419（2026-09-27 · **P1-NINT：$N_{\rm int}$ micro-check —— 折衷关系（新）＋ 独立性闸 PASS**）** ✓
- 【**★★(2) 折衷关系（新 ✓✓）**】块级分类：$y=c{\oplus}S_y$（$|S_y|=4$）按 $j:=|S_y\cap S(c)|$ 分类，$b_j:=\#\{y:j\}$ ✓；每块覆盖的 forced 三元数 $=\binom j3$（$0,0,0,1,4$ ✓）⟹ $$\boxed{b_3+4b_4\ \ge\ \binom{s(c)}3}\ \Longrightarrow\ \boxed{d_4(c)\ \ge\ \max\Big(b_4,\ \binom{s(c)}3-3b_4\Big)}$$ ✓✓（**本线第一条排列级下界** ✓）；**一致性核验 ✓**：该式**蕴含**容量界 $\lceil\binom s3/4\rceil$ ✓（$b_4\le\binom s3/4$ 时 $\binom s3-3b_4\ge\binom s3/4$ ✓；否则 RHS $=b_4>\binom s3/4$ ✓）
- 【**★(3) 独立性闸 PASS ✓**】$b_4,b_3$ 属**排列级**（度数信息只含 $d_4(c)=\sum_jb_j$ 的**总数**、**不含分裂** ✓）⟹ **非 degree-profile 函数** ⟹ 同时过 **C-418 门** ＋ **独立性闸** ✓✓；**注**：$s(c)=10$ 时分裂**退化**（一切 weight-4 块皆 $b_4$ ✓）⟹ 门的咬合只在 $s<10$ 生效 ✓
- 【**⚠️(4) 诚实边界（关键 ✓）**】关系本身**不是**度数的函数 ✓（故**未触发**"可由账本恢复 ⟹ STOP"✓）；但它**悬空** ✗ —— 使用须有 $b_4$（或 $b_3$）的输入 ⚠️，而两条来源皆不提供：① **avoidance 侧**：内部块**合法**（P1-D4b 显式反例 ✓）⟹ 不能用 avoidance 界 $b_4$ ✗✓；② **容量／度数侧**：与 $\{n_j\}$ 同源（C-409 ✓）⟹ 不给排列级信息 ✗✓ ⟹ **门 PASS ＋ 关系成立，但"对 119-cover 的新数学约束"仍未获得** ⚠️
- 【**★(5) 状态锁（照唐先生 23:19 ✓）**】**C-418 ＝ 筛选器已成立** ✓；**$N_{\rm int}$ ＝第一候选** ✓；**尚无新数学约束** ✗；**119 主问题仍完全 LIVE** ✓；**不**把任何短名单项提前升级成 closure／NO-GO ✗（照令 ✓）；**未改** closure gate／nogo gate ✗；**优先级**：$N_{\rm int}(c)\to G_2(C)$ 谱接口 $\to$ 见证超图 ✓（每项须先过 C-418 门 ＋ 独立性闸 ✓）
- 【**边界**】零程序计算；未上 SDP/SAT；未开门②；未改门；不跨空间（回查已分栏 ✓）；**本档未产生对 119 的新数学约束** ✗（诚实 ✓）；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-NINT-2026-09-27-witness-count-tradeoff-relation-and-independence-gate.md`

**🧱 C-420（2026-09-27 · **P1-B4：$b_4$ 独立控制 micro-check —— 新局部事实 ＋ avoidance 侧无界 ＋ 三来源汇总**）** ✓
- 【**★★(1) 新局部事实（本档 ✓✓）**】内部块 $y=c{\oplus}u$（$u\subseteq S(c),|u|=4$ ✓）⟹ $$\boxed{S(y)\cap u=\varnothing}\ \Longrightarrow\ \boxed{d_1(y)\le10-4=6}$$ ✓✓ **证明 3 行**：$i\in u\Rightarrow y{\oplus}e_i=c{\oplus}e_{(u\setminus i)}$（重量 3、支撑 $\subseteq S(c)$ ✓）$\overset{(\alpha)}{\Longrightarrow}\notin C\Rightarrow i\notin S(y)$ ✓；**性质**：**纯排列级**、非 degree-profile 函数 ⟹ 过 C-418 门 ＋ 独立性闸 ✓；**注**：此前局部事实皆"以 $c$ 为中心"，本事实是**以内部块为中心**的第二条（第一条 ＝ P1-D4b 的 $C_0$ ✓）
- 【**★★(2) avoidance 侧：$b_4$ 无界（$\le\binom{10}4=210$ ✓✓）**】显式族 $$C_1:=\{0\}\cup\{e_i\}\cup\{e_u:u\in\mathfrak U\},\quad \mathfrak U\subseteq\binom{[10]}4\ \text{任意},\ b_4(0)=\#\mathfrak U$$ **逐类核验 ✓**：① 无重量 2／3／5／6 点 ⟹ $A(0)=0$ ✓、$(\alpha)$ 在 0 成立 ✓；② **无 square**（2-coset 需重量 2／3／5 点 ✗）；③ **无 tetra**（3-coset 偶部需重量 2／1／3／2／6 点 ✗；$v=e_u$ 情形按 $|u|$ 落入数细分：全在内⟹重量 2 ✗、1 在外⟹一对重量 2 ✗、2 在外⟹重量 6 ✗、3 在外⟹全重量 6 ✗）；④ $A(y)=0$ 空真 ✓ ⟹ **$C_1$ 满足全 avoidance** ✓✓，取 $\mathfrak U=\binom{[10]}4$ 得 $b_4(0)=210$（**上界可达** ✓）⟹ **在 avoidance 层面 $b_4$ 可任意大** ⟹ **"$N_{\rm int}$ 路线自然极限"支获明确支持** ✓✓（**但 $C_1$ 非覆盖码** ✗，不证明 119-cover 中可大 ✗）
- 【**⚠️(3) 三来源汇总（皆不给独立控制 ✓）**】① avoidance ✗（$C_1$ ✓）；② degree／profile ✗（只见 $d_4=\sum_jb_j$ 总数 ✓）；③ covering ✗（只给 $b_3+4b_4\ge\binom s3$，需求型、不能上界 ✓）；④ 新事实 §1 ⚠️ 部分（约束 $d_1(y)$、不直接界 $b_4$ ✓）⟹ **尚无任何已证机制能独立压低 $b_4$** ⟹ **C-419 折衷式暂不能产生实质 squeeze** ✗
- 【**★(4) 状态锁（照唐先生 23:21 ✓）**】C-419：**PASS ＋ 新排列级关系，未闭合** ✓；**下一攻击点 ＝ 独立控制 $b_4$** ✓；**无理由 CLOSED** ✗、**无理由 NO-GO** ✗；**HOLD** ✓；未升级短名单项 ✗；**未改** closure gate／nogo gate ✗；119 主问题仍完全 LIVE ✓
- 【**下一步两出口（登记未做 ✓）**】① 找新机制界 $b_4$（如用 §1 的 $d_1(y)\le6$ 做全局计数 ⚠️）；② 若在 119-cover 中 $b_4$ 可大 ⟹ 明确记为 natural limit ✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开门②；未改门；不跨空间（回查已分栏 ✓）；不声称 119-cover 中 $b_4$ 可大 ✗；不声称折衷式无用 ✗
- 档：`docs/P1-B4-2026-09-27-internal-block-local-fact-and-avoidance-side-unboundedness.md`

**5️⃣ C-421（2026-09-27 · **P1-D5：缺失邻居坐标结构 —— 结构恒等式（layer-5 接口）＋ 缺失集无新信息 ＋ 存在侧自由**）** ✓
- 【**★★(1) 精确结构恒等式（新 ✓✓）**】内部块 $y=c{\oplus}u$（$u\subseteq S(c),|u|=4$ ✓）⟹ $$\boxed{d_1(y)\ =\ \#\{i\notin u:\ c\oplus e_u\oplus e_i\in C\}}$$ ✓✓ **证明**：$i\in u\Rightarrow y{\oplus}e_i=c{\oplus}e_{(u\setminus i)}$（重量 3、支撑 $\subseteq S(c)$）$\overset{(\alpha)}{\Longrightarrow}\notin C$ ✓（不计数）；$i\notin u\Rightarrow y{\oplus}e_i=c{\oplus}e_u{\oplus}e_i$（**重量 5** ✓）⟹ 计数当且仅当在 $C$ ✓ ⟹ **内部块的全部一阶邻居恰是重量 5 码字** ⟹ **本线第一次把 layer-5 接入** ✓✓；含 C-420 的 $d_1\le6$ 作为系 ✓
- 【**✗(2) 缺失集无新信息**】$\mathrm{miss}(y):=[10]\setminus S(y)\supseteq u$ 的内容**就是** $u\subseteq S(c)$（经 $(\alpha)$ 解释 ✓）⟹ **等价于 $b_4$ 的定义条件**（"哪些 $u$ 是内部块"✓）⟹ 单靠缺失集不产生新量 ✗（再走一步即退回 C-417／C-419 同源链 ✓）
- 【**⚠️(3) 存在侧自由（真正接口）**】自由部分是 $S(y)\cap([10]\setminus u)=\{i\notin u:c{\oplus}e_u{\oplus}e_i\in C\}$（§(1) 的**生成集** ✓）；**不受** $(\alpha)$（只覆盖重量 2／3 ✓）与 $A(c)=0$（只管重量 2 ✓）约束 ⟹ **接口处无 demand > capacity** ✗⚠️；**但接口本身有价值**：把"内部块"与**重量 5 层**绑定 ⟹ 若将来能对重量 5 层建独立（非 avoidance／非容量）约束，则直接回传到 $b_4$ ✓
- 【**★(4) 状态锁（照唐先生 23:24 ✓）**】$$\textbf{avoidance: STOP}\ ✗\quad\textbf{profile/capacity: STOP}\ ✗\quad\textbf{内部 block 的邻接结构: LIVE}\ ✓$$ C-419 **HOLD** ✓；C-420 结论（$C_1\Rightarrow b_4$ 可达 210）保留 ✓；**本档未形成新全局约束** ✗（诚实 ✓）
- 【**下一步（登记未做 ⚠️）**】① 对 weight-5 层建**排列级**约束（非 avoidance／非容量 ✓）；② 用"生成集"定义新的 global 量（$\sum_u|\{i\notin u:c{\oplus}e_u{\oplus}e_i\in C\}|$ 的排列敏感函数 ✓）；③ 检验其是否与 119 的覆盖需求碰撞 ⚠️
- 【**边界**】零程序计算；未上 SDP/SAT；未开门②；未改门；不跨空间（回查已分栏 ✓）；不声称 119-cover 中 $b_4$ 可大 ✗；不声称重量 5 层路线有效 ✗；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-D5-2026-09-27-missing-neighbour-structure-and-the-layer5-interface.md`

**🖐️ C-422（2026-09-27 · **P1-L5：内部 4-面判定定理 ＋ 精细 layer-5 容量（排列级，首个非平凡界）**）** ✓
- 【**★★(1) 分类定理（新 ✓✓）**】$w=c{\oplus}e_v$（$v\in M_5(c)$ ✓）的 4-面 $u_i:=v\setminus\{i\}$（$i\in v$）是**内部 block** $$\iff\boxed{i\in S(w)\ \textbf{且}\ v\setminus\{i\}\subseteq S(c)}$$ ✓✓（**证明**：⟸ $i\in S(w)\Rightarrow w{\oplus}e_i=c{\oplus}e_{u_i}\in C$ ✓；⟹ 由 $w{\oplus}e_i\in C$ 与 $u_i\subseteq S(c)$ ✓；**关键** $v\setminus\{i\}\subseteq S(c)\iff(v\setminus S(c))\subseteq\{i\}$ ✓）
- 【**★(2) 三情形推论（按 $a:=|v\setminus S(c)|$ ✓✓）**】$a=0$（$v\subseteq S(c)$）：内部面数 $=|v\cap S(w)|\le5$ ✓；$$\boxed{a=1\Rightarrow\#\le\mathbf 1}$$ ✓✓（**唯一性现象**：设 $v\setminus S(c)=\{j\}$，唯一候选面 $u_j$，成为内部 block $\iff j\in S(w)$ ✓）；$a\ge2\Rightarrow\#=0$ ✓
- 【**★★(3) 精细容量不等式（新，排列级 ✓✓）**】$$\boxed{I(c)\ \le\ 5\,|M_5^{(0)}|\ +\ 1\,|M_5^{(1)}|}\qquad\big(M_5^{(k)}:=\{v\in M_5(c):|v\setminus S(c)|=k\}\ ✓\big)$$ 对照**平凡界** $I(c)\le5|M_5(c)|$ ✓ —— 精化来自 $a\ge1$ 的**位置敏感压制** ✓✓；**过 C-418 门** ✓（依赖 $v$ 相对 $S(c)$ 的**位置** ⟹ 非 degree/profile ✓）
- 【**$I(c)$ 三重表达（接口恒等式 ✓）**】$I(c)=\sum_{u\in M_4(c)}|E_5(u)|=\sum_{u\in M_4^{\rm int}}d_1(c{\oplus}e_u)=\sum_{v\in M_5(c)}\#\{\text{内部 4-面 of }v\}$ ✓ ⟹ **双层接口 $M_4\to I\leftarrow M_5$** ✓（本档补上右侧第一次精化 ✓）；**注**：非内部 $u$ 时 $d_1(c{\oplus}e_u)=|E_5(u)|+\#\{i\in u:c{\oplus}e_{(u\setminus i)}\in C\}$（不可省项 ✓）
- 【**⚠️(4) 诚实：下界不可得**】内部 block 可满足 $E_5(u)=\varnothing$（即 $d_1(c{\oplus}e_u)=0$，**孤立内部块** ✓）⟹ $A(c)=0$ 与 $(\alpha)$ 皆不禁 ✓ ⟹ $I(c)$ **只有上界（本档）＋平凡下界 0** ✗ ⟹ **无法夹逼、尚不能形成 collision** ⚠️；**另一条下界通道（未做）**：若能把 C-419 需求 $b_3+4b_4\ge\binom s3$ 与 $I(c)$ 相连 ⟹ 方可碰撞 ⚠️
- 【**★(5) 状态锁（照唐先生 23:27 ✓）**】avoidance／missing-set **STOP** ✗；degree／profile／capacity **STOP** ✗；$4\to5$ 精确邻接接口 **LIVE** ✓；C-419 $b_3/b_4$ tradeoff **HOLD** ✓；**新的全局碰撞尚未形成** ⚠️；**C-421 不 CLOSED** ✗，是合格 **LIVE interface**、**尚不是攻击点本身** ✓（本档为其补上"右侧第一次精化" ✓）
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间（回查已分栏 ✓）；不声称 $I(c)$ 路线有效 ✗；不声称 119-cover 中存在内部块 ✗（$C_1$ 非覆盖码 ✓）；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-L5-2026-09-27-internal-4face-criterion-and-refined-layer5-capacity.md`

**🌉 C-423（2026-09-27 · **P1-BRIDGE：局部无需求引理 ＋ 无桥定理 ＋ 生死关判据**）** ✓
- 【**★★(1) 局部无需求引理（新 ✓✓）**】内部块 $y=c{\oplus}e_u$ 的 6 个 layer-5 点 $c{\oplus}e_{u\cup\{i\}}$（$i\notin u$）**全部在 $B_1(y)$ 内** ✓（$d(y,c{\oplus}e_{u\cup\{i\}})=|e_i|=1$ ✓）⟹ **已被 $y$ 覆盖** ⟹ $$\boxed{\text{covering 对它们\textbf{零需求}}}$$ ✓✓ 即：$$\boxed{\text{layer-5 点被覆盖}\ \not\Rightarrow\ \text{layer-5 码字存在}}$$ ✓✓（照唐先生 23:30 ✓，本档给证明 ✓）；与 $C_1$ 对照：$E_5(u)=\varnothing$ 与全 avoidance 兼容 ⟹ 非漏洞、是结构允许 ✓
- 【**★★(2) 无桥定理（局部层面 ✓✓）**】内部块产生的**局部需求的全部对象都是 weight-3 点**（4 个面 ✓，且 $y$ 自身覆盖它们 ✓）；**没有任何局部需求以 layer-5 为对象** ✗ ⟹ 两链在**局部**无方向正确的桥：需求链 $b_4\to(\text{weight-3 demand})$ 与接口链 $b_4\to M_4^{\rm int}\to I(c)\to M_5$ ✓ ⟹ **这解释了"下界自然缺失"的\*\*原因\*\*** ✓✓（比"暂无下界"更强 ✓）；**推论**：任何桥都必须是**全局的** ⟹ 与 C-409／C-417 风险同源 ⚠️（须过 C-418 门 ✓）
- 【**★(3) 生死关判据（精确 ✓）**】**(a) 继续**：若证 covering $\Longrightarrow E_5(u)\ne\varnothing$（某内部块有 layer-5 邻接码字 ✓）；**(b) STOP**：若给出**覆盖兼容机制**使某内部块 $E_5(u)=\varnothing$ ⟹ 此路线在此 STOP ✓；**现状**：(a) 在**局部被排除** ✓（§1）、(b) **未给出** ✗ ⟹ **HOLD ＋ 精确理由** ✓（照唐先生：**不关闭** C-422 ✗、**不升级**为 collision ✗）
- 【**★(4) 方向性观察（结构 ✓）**】添加 layer-5 码字会引入其**自身需求**（成本 ✓），而 $E_5(u)=\varnothing$ **无成本** ✓ ⟹ 该路线的自然方向**与 forcing 相反** ✓
- 【**★(5) 定位（照唐先生 23:30 ✓）**】C-421 ＝ 发现 $4\to5$ 接口 ✓；C-422 ＝ 发现该接口的 $0/1/5$ 面数分类及精细容量 ✓；**C-422 ＝ 新的排列级上界／结构分类、尚不是 P1** ✓（**保留**、**不关闭**、**不升级** ✓）；**下一关** ＝ covering 能否给该接口制造**正需求** ✓
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间（回查已分栏 ✓）；不声称 $4\to5$ 路线死 ✗（须 (b) 才 STOP ✓）；不声称 119-cover 中存在内部块 ✗；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-BRIDGE-2026-09-27-local-zero-demand-lemma-and-the-no-bridge-theorem.md`

**🌐 C-424（2026-09-27 · **P1-GLOBAL：状态锁 ＋ 跨中心三重相关恒等式（过 C-418 门）＋ 覆盖侧仍缺**）** ✓
- 【**★(1) 状态锁（照唐先生 23:33 ✓）**】$$\text{local layer-5 forcing: STOP}\ \Big|\ \text{local missing-set: STOP}\ \Big|\ \text{profile/capacity bridge: STOP}\ \Big|\ \textbf{global }4\leftrightarrow5\text{ incidence: HOLD}\ \Big|\ \text{C-422 structural asset: LIVE}$$（前两项依据 C-423 §1／C-421 §2 ✓、第三项依据 C-409／C-417 ✓）；**不**把整个方向 CLOSED ✗；**最关键新增信息 ＝ C-423 零需求证明** ⟹ $M_4^{\rm int}\ne\varnothing\not\Rightarrow M_5\ne\varnothing$ ✓，且 $E_5(u)=0$ 与局部覆盖职责**完全兼容** ✓
- 【**★★(2) 跨中心全局恒等式（新 ✓✓）**】$$\boxed{\sum_{c\in C}I(c)\ =\ \sum_{u\subset v,\,|u|=4,|v|=5}\big|C\cap(C\oplus e_u)\cap(C\oplus e_v)\big|}$$ ✓✓ **推导**：$I(c)=\#\{u\subset v:c{\oplus}e_u\in C,c{\oplus}e_v\in C\}$ ⟹ 交换求和 ✓；**读法**：右侧 ＝ 对 $\binom{10}4\cdot6=1260$ 个 $(u\subset v)$ 对求**三重相关** ✓（**跨中心**：$c$ 跑遍 $C$ ✓）
- 【**★★(3) 过 C-418 门（✓✓ 正面答复唐先生）**】该量是**三重相关级**（排列级 ✓），依赖"哪些 $u$ 是内部块"与"哪些码字在何处" ⟹ **非 degree/profile 函数** ⟹ S1 否／S2 是／S3 定义于任意 119-cover ⟹ **PASS** ✓✓ ⟹ **"过门的全局对象"确实存在** ✓（**同一对象三形态**：$\sum_cI(c)$／三重相关之和／$\sum_c\sum_{u\in M_4^{\rm int}(c)}d_1(c{\oplus}e_u)$（配 C-421 ✓））
- 【**⚠️(4) 覆盖侧仍缺（诚实 ✓）**】C-423 零需求引理 ⟹ **无局部覆盖下界** ✓；全局亦然：covering 是"逐点 $\ge1$"（单调下型 ✓）⟹ 只产生**下层**（覆盖需求）结论，而 $\sum_cI(c)$ 统计的是**码字邻接 incidence（上层）** ⟹ **对象不同（C-423 §2 无桥 ✓）** ⟹ 覆盖侧不等式仍无 ✗ ⟹ **HOLD** ✓（**照判据**：若找不到"过门 **且** 有覆盖侧独立不等式"的全局量 ⟹ 此 $4\to5$ 线应 STOP ✗；现状＝**对象过门 ✓、覆盖侧缺 ✗** ⟹ 既未 STOP、也未 P1）
- 【**★(5) 唯一剩余形态（登记未做 ⚠️）**】要形成碰撞须经**跨中心**约束：① 119 的**全局最小性**能否约束三重相关 $\sum_{u\subset v}|C\cap(C\oplus e_u)\cap(C\oplus e_v)|$？② 若能且证明**不是** C-409／C-417 型 profile 重包装（过 C-418 ＋ 独立性闸 ✓）⟹ 真正的新 P1 ✓；③ 若不能 ⟹ 照判据 **STOP** 此线、**不再堆 layer identities** ✓（照唐先生 23:33 ✓）
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间（回查已分栏 ✓）；不声称 $4\to5$ 线已死 ✗；不声称三重相关路线有效 ✗；不声称 P1 成立 ✗（V290）
- 档：`docs/P1-GLOBAL-2026-09-27-status-lock-and-cross-centre-triple-correlation-identity.md`

**🛑 C-425（2026-09-27 · **P1-DELETE：incidence 不迫使独占覆盖 ⟹ **STOP $4\to5$ 线**（路线级）**）** ✓
- 【**★(1) 精确分解（本档补 ✓）**】$T(C)=\sum_{c\in C}\big[\sum_{u\in M_4^{\rm int}(c)}d_1(c{\oplus}e_u)\ (\text{C-421 适用 ✓})+\sum_{u\in M_4(c)\setminus\mathrm{int}}|E_5(u)|\ (\text{非内部部分 ✓})\big]$ ✓ —— C-424 §0(3) 只列了**内部部分**，此处补齐 ✓
- 【**★★(2) incidence 的精确内容（新 ✓✓）**】三重 $(c,y=c{\oplus}e_u,z=c{\oplus}e_v)$（$u\subset v$，$v=u\cup\{i\}$）$$\iff\boxed{i\in S(y)}$$ ✓✓ **读法**：incidence 的全部内容 ＝ "$y$ 有一个方向 $i\notin u$ 的一阶邻居" ⟹ **无额外跨中心信息** ⚠️；$T(C)$ 的"全局性"**仅来自对 $c$ 求和** ✓（＝逐中心局部数据的求和 ✓）
- 【**★(3) 窄问题答案：无 forcing（✗✓）**】incidence 仅钉住 $i\in S(y)$；而 $y$ 的**不可删性** ⟺ $|S(y)\cup V(H_y)|\le9$（R4-P1 ✓）；**二者无关** ⟹ $|S(y)\cup V(H_y)|=10$（每坐标被触及 ⟹ $y$ **可删**）与 incidence **兼容** ⟹ **incidence 不迫使独占覆盖** ✗✓；**构造性支持**：$C_1$ 型族中两极端（可删／不可删）皆与 incidence 相容 ✓ ⟹ **该 witness 机制不存在** ✓
- 【**★(4) 案例分裂（诚实必需 ✓）**】"119 最小性"**不可无条件假设** ✗：**Case A** $K(10,1)=119$ ⟹ 最小性可用 ✓；**Case B** 存在 119-cover 含可删字 ⟹ $\exists$118-cover ⟹ $K(10,1)\le118$ ✓（**更强的上界、独立成果** ✓）⟹ 最小性是**条件假设**（Case A），**本档 STOP 判定不依赖它** ✓
- 【**★★(5) STOP 判定（照唐先生硬判据 ✓）**】**建议 STOP 此 $4\to5$ incidence 线** ✓（**路线级 STOP** ✓ —— **不**是对 119 的断言 ✗（V290 ✓））；**不再向 layer 6／7 堆叠** ✓；**证据四行**：① covering 侧**零输入** ✓（C-423 ✓）② $T(C)$ ＝局部数据的**求和** ✓ ③ incidence **无局部 forcing 内容** ✗ ④ 唯一可行推导形态 ＝ 逐 $c$ 用 C-422 的**上界**再求和 ⟹ **只得上界** ✗（无法与 C-419 的**下界需求**碰撞 ✓）
- 【**★(6) 为何是"方向不匹配"而非"缺一个恒等式" ✓✓**】上层 incidence 需要**下界**输入来碰撞 C-419 的**下界**需求；而所有覆盖侧输入都是**下层**（单调下型 ✓）⟹ **方向系统性错配** ✓✓
- 【**保留项（✓✓ 不得随 STOP 废弃）**】① C-421 接口恒等式 ✓ ② C-422 精细容量（排列级上界 ✓）③ C-423 零需求引理（防错 ✓）④ C-424 三重相关恒等式（对象层 ✓）⑤ C-419 折衷关系（HOLD ✓）
- 【**边界**】零程序计算；未上 SDP/SAT；未开②；未改门；不跨空间（回查已分栏 ✓）；**STOP 为路线级** ✗ 非对 119 的断言 ✓；不声称 P1 成立／不成立 ✗（V290）；CLOSED-ROUTES-MAP 的 119 段**未改动** ⚠️（若需登记路由 STOP 须唐先生显式批准 ✓）
- 档：`docs/P1-DELETE-2026-09-27-incidence-does-not-force-exclusive-coverage-STOP.md`

**📉 C-426（2026-09-27 23:44 · **D-LP 状态锚点（唐先生提供）＋ "为何 119 无攻击点"的定量诊断**）** ✓
- 【**D-LP 状态锚点（唐先生 23:44 提供 ✓；与档案核对一致 ✓）**】数值链：**sphere 93.090909 → Delsarte LP 94.0197982 → Van Wee 101.0073568 → combined classical LP 101.4081694 → 2025 strengthened SDP 105.2223** ✓；**档案核对 ✓**：`DLP1A-2026-09-27` 已**独立复现前三个锚点（7 位小数命中 ✓）**；`DLP1B-2026-09-27` 记录**工具已解阻**（cvxpy 1.9.3 ＋ scs 3.3.1 实跑通过 ✓）、§2 装置（$M/M'/M''$＋Prop 2.1 ✓）已抽，**Theorem 2.5／4.9 待抽** ✓；提交 `10be95d` ✓
- 【**状态区分（照唐先生 ✓，两道不可混）**】$$\text{D-LP-0 主数值链：基本完成 ✓}\ \Big|\ \text{classical LP ablation（1A）：完成 ✓}\ \Big|\ \text{2025 SDP = 105.2223：已核实 ✓}\ \Big|\ \textbf{SDP 组件归因（1B）：OPEN}✗\ \Big|\ \text{119 排除：尚未得到}✗$$
- 【**★★"为何 119 无攻击点"的定量诊断（本档 ✓✓）**】
 ① **通用机器与目标\*\*不同量级\*\* ✓✓**：$105.2223$ 距 $120$ 尚差 $\mathbf{14.7777}$ ✓；而 **2025 SDP 相对经典 LP 的\*\*全部\*\*增益 ＝ $105.2223-101.4082=\mathbf{3.8141}$** ✓ ⟹ **"同类工具再做一次"的典型收益 ≈4 单位，而缺口 ≈15 单位** ⟹ **改进型不变量整类在\*\*数量级\*\*上到不了窗口** ✓✓ —— 这正是"每个局部引理都对、却永远差得远"的机制 ✓
 ② **局部类已被\*\*证明\*\*耗尽 ✓**：C-417（球面超额 $\equiv$ 度数决定 ✓）／C-425（incidence 需**上界**输入、covering 只给**下界** ⟹ **方向错配** ✓）⟹ 不是"没找到"，而是**已证明这一类找不到** ✓
 ③ **故"没有攻击点"＝三道筛的\*\*成果\*\* ✓**（C-418 预筛门 ＋ 独立性闸 ＋ 方向检验）⟹ **空列表是结论，不是停滞** ✓✓
- 【**★★剩余的真攻击点（不同种类 ✓）**】① **D-LP-1B 组件归因**（唐先生已定 ✓）：把 $3.8141$ 拆开 ⟹ 定出"新不变量必须超过的标杆" ✓；② **构造／认证路线**（**档案自证**：已知 $120$ 可行，而我们的搜索 best_unc $24$–$34$ ⟹ **实现低于文献水平** ✓）—— **可测、可修**的工程缺口 ✓；③ **全新类型的不变量**（排列级、非 profile、**带覆盖侧不等式** ✓）—— 目前**一个都没有** ✗
- 【**★RH 与 119 的不对称（诊断结论 ✓）**】RH 缺攻击点⟸**数学深**；119 缺攻击点⟸**工具类与问题类型错配**（有限全局极小值 ✓）：最后 $\approx15$ 单位靠的是**构造原则／认证搜索**，而非"再精炼一个不变量" ✓；**建议**：**停止**在 layer 6／7 堆恒等式（C-425 已判 STOP ✓），先做 1B 归因 ＋ 构造/证书路线 ✓
- 【**边界 ✓**】本档为**状态记录 ＋ 诊断**（非新数学命题 ✓）；锚点数值**归属唐先生／档案 1A ✓**（$105.2223$ 记为唐先生已核实值 ✓）；零程序计算；未改门；不跨空间；不声称 P1 成立／不成立 ✗（V290）
- 档：本条目（registry-only；如需独立档须唐先生指示 ✓）

**🧭 C-427（2026-09-27 23:49 · **事实修正 ＋ 两候选 P0 审计（私邻/Hall ⟹ 坍缩；excess 同余 ⟹ HOLD）**）** ✓
- 【**✗ 事实修正（照唐先生 ✓）＋ C-426 勘误**】公开区间为 $$\boxed{107\le K(10,1)\le120}$$ ✓（OEIS A000983 列 $a(10)=107$–$120$ ✓；**与档案一致** ✓：`HANDOFF-2026-09-27-119-line…` 行 62 记"下界侧：107（BÖW 2004）远低于 119；LP 93.09、SDP 105.2、本 MIP 99.0 ⟹ 证明侧被现有技术堵死" ✓）⟹ **我们复现的 SDP $105.2223$ \*\*低于\*\* 文献下界 $107$ ✗** ⟹ **C-426 用"$105.2223\to120=14.7777$"作缺口是错的** ✗✓（**勘误**：正确缺口 $=120-107=\mathbf{13}$ ✓）；**但同一诊断结论仍成立** ✓：同类工具（SDP 增益 $3.81$）相对缺口（$13$）**仍差一个量级** ✓
- 【**★★战略后果（新 ✓✓）**】**可达的一侧是\textbf{上界侧}** ✓：文献 UB $=120$（已知构造 ✓，唐先生 ✓）⟹ **当前直接目标 ＝ 做出 $119$-cover（把 120 压 1 ✓）** ✓；而**本线此前是从我们自己的 $124$（加倍型）出发** ✗（HANDOFF 亦记"$m=120$ 自检门 FAILED：已知 120 可行而 best_unc 24–34 ⟹ **实现低于文献水平**" ✓）⟹ **具体下一步：取文献已知 $120$-cover 作起点，再向 119 攻击** ✓✓（登记，未执行 ✓）
- 【**★P0 审计 #1：私邻／Hall 障碍 ⟹ \*\*坍缩\*\* ✗✓（档案内推理，未搜网 ✓）**】
 ① **私邻集两两不交 ✓✓（3 行）**：$\mathrm{PN}(c):=\{x\in N[c]:N[x]\cap C=\{c\}\}$ ✓；若 $x\in\mathrm{PN}(c)\cap\mathrm{PN}(c')$ 则 $N[x]\cap C=\{c\}=\{c'\}\Rightarrow c=c'$ ✗ ⟹ **不交** ✓
 ② ⟹ $|\mathrm{PN}(X)|=\sum_{c\in X}p(c)$ ✓ ⟹ **Hall 条件 $\iff \min_c p(c)\ge1\iff$ 无可删码字 $\iff C$ inclusion-minimal** ✓✓ ⟹ **"私邻/Hall"形式\*\*恰好等价于\*\*最小性，无额外内容** ✗✓
 ③ **经典私邻/irredundance 理论对立方体只给平凡界** ✗：Ore（无孤立点图 $\gamma\le n/2$ ✓）⟹ $Q_{10}$：$\le512$ ✗ 平凡 ✓；且档案实测 $\sum_cp(c)=n_1\ge\mathbf{739}$ ✓（**每码字平均私有 $\ge6.21$** ✓，见 C-401 ✓）⟹ 私有球点**远多于所需** ⟹ **不存在 Hall 障碍** ✗✓
 ④ **（更干净的等价陈述 ✓）** 在"证 $K\ge120$"的反证设置中，取**最小**覆盖即 automatic minimal ✓ ⟹ 所有 $p(c)\ge1$ ✓ ⟹ 该路线**给不出任何界** ✗
 $$\Longrightarrow\ \textbf{P0 结论：候选 #1 归约到\ \textbf{已登记}的可删性路线（C-411／C-425／R4-P1 ✓）⟹ \textbf{非新路线}✗✓}$$
- 【**★P0 审计 #2：结构子集 excess 同余 ⟹ HOLD ✓（含一处对唐先生前提的\*\*纠正\*\*）**】
 ① **唐先生前提"$n=10$ 无同余机制"需纠正** ✗✓：**Habsieger 1997 的机制\*\*已覆盖\*\* $n=10$** ✓（奇数素数 $p\mid n+1$ ⟹ $\sum_{i<p}\delta_i\equiv p-1\ (\mathrm{mod}\ p)$ ✓；$n=10\Rightarrow p=11$ ✓）—— 档案已分析并记为 **R2-1 = DROP** ✓，理由正是"Habsieger 已覆盖 $n\equiv2,4\ (\mathrm{mod}\ 6)$"✓（给 $\ge104/105$ ✓ ⟹ **低于文献下界 107** ✗）
 ② ⟹ **同余机制存在但弱** ✓；故唐先生所提"先在 $n=10$ 建独立同余机制"**已被回答**：**它存在，且只到 ~104/105** ✗✓
 ③ **真正新的部分 ＝ "$\mathrm{structured}\ S$ 而非完整层"** ⚠️：须与 (a) Habsieger 的**层同余** ✓ 与 (b) **C-417 的层坍缩** ✓ **皆不同** ⟹ 需**新的证明机制**（Habsieger 的证明依赖层/湮灭多项式结构 ✓）⟹ **HOLD** ✓
- 【**状态 ✓**】候选 #1（私邻/Hall）：**STOP（归约 ⟹ 非新 ✓）**；候选 #2（结构子集同余）：**HOLD** ✓；**战略更新**：**上界侧可达**（$120\to119$ ✓）、起步用文献 120 ✓；本档零程序计算；未改门；不跨空间；不声称 P1 成立／不成立 ✗（V290）
- 档：本条目（registry-only ✓）

**🔁 C-428（2026-09-27 23:52 · **两候选 P0：fort ⟹ STOP；开邻域+Walsh ⟹ STOP（＝已审计对象第 3 次回潮）＋ 复现守卫**）** ✓
- 【**✗候选 A：fort transversal ⟹ STOP**】① 唐先生已自证：**纯 fort-transversal ＝ domination 本身**（$D\cap N(v)\ne\varnothing$ 就是 domination ✓）⟹ 无新下界 ✓；② **本档补**：minimum fort 刚性（$d\ne4$ ⟹ 最小 fort 皆 open neighbourhoods $N(v)$ ✓）⟹ "击中全部 $N(v)$" 的条件 $=$ **全支配（total domination）** ✓✓ ⟹ **与 domination 是\*\*不同参数\*\*** ✗（支配集 $D$ 不必全支配：孤立码字 $c$ 有 $N(c)\cap D=\varnothing$ ✓）⟹ **不存在"119-支配 ⟹ fort-transversal 性质"的交叉不等式** ✗✓；③ 且零强迫参数与 domination 仅在**维数为 2 的幂**时等同 ✓（$10\ne2^k$ ✗，照唐先生 ✓）
- 【**★★候选 B：开邻域 incidence ＋ Walsh 谱 ⟹ STOP（＝已审计对象 ✓✓）**】
 ① **对象同一性 ✓✓**：$m=A\mathbf 1_D=b-f$（**派生量** ✗，因 $b=m+f$ ✓）；覆盖条件 $A\mathbf 1_D+\mathbf 1_D\ge\mathbf 1\iff Tf\ge1$，$T:=A+I$ ✓ —— **这正是档案 `P1-REAUDIT-2026-09-27` 的 OB-1 模 11 定理对象** ✓✓（$T=I+\sum_{i=1}^{10}\sigma_i$ ✓ 被 Walsh 基对角化、特征值 $\mathbf{11-2w}$ ✓）
 ② **档案已审且结论为\*\*否定\*\* ✓**：OC-1 ⟹ **线性内容 $=\{f\in\mathbb Z^{1024}:Tf\ge1,\ \sum f=119\}$（整数/多重覆盖松弛 ✓）**；**非线性内容 ＝ 二值性 ＝ Booleanity** ⟹ **"$g$-形不产生新必要条件"** ✗✓（与 A-INCIDENCE-FIX-1 的 Booleanity 等价判同 ✓）
 ③ **自测判据（唐先生 ✓）逐条触发** ✗：(i) $\|Af\|^2=10|D|+4N_2=1190+4N_2$ ⟹ **完全由 $|D|$ 与 profile（$N_2$）决定** ✗；(ii) 谱质量 $\sum_{|u|=j}\hat f(u)^2$ ＝ 距离分布的 **Krawtchouk 变换** ⟹ profile ✓✗；(iii) "平均值 $1190/1024\approx1.1621$ 很低" ≡ **excess 恒等式**（$E=11|D|-1024=285$ ✓）⟹ profile ✗
 ⟹ **按唐先生自己的 STOP 判据：立即 STOP** ✓（未出现"无法由 profile 恢复的 eigenspace mass／sign 约束" ✗）
- 【**★★★复现守卫（本档新增 ✓✓，可复用）**】该对象（$T=A+I$ ＋ Walsh 对角化 ＋ mod-11 ＋ Booleanity）现 **第 3 次**独立回潮：**R3 坐标标记 excess（dda3630 ✓）→ C-417 层坍缩（682bffb ✓）→ 本次开邻域+Walsh（C-428 ✓）** ⟹ **登记守卫**：$$\boxed{\text{任何 119-攻击须同时满足：① 过 C-418 预筛门；② \textbf{不可}表为算子 }T=A+I\ \text{的 Walsh/谱形式（已穷尽 ✓）}}$$ ✓✓ —— 该守卫**解释了"为何第 3 次又回到同一对象"**，并把"新不变量"的定义收紧为"**必须携带 $T$ 之 Walsh 谱看不到的信息 ⟺ Booleanity 之外的排列/交叠结构**" ✓✓
- 【**状态表（更新 ✓）**】private-neighbor／Hall：**DOWNGRADE**（核心机制老旧 ✓ 照唐先生 ＋ C-427 P0 已证其 Hall 形式＝最小性 ⟹ 无额外内容 ✗）；excess congruence：**HOLD** ✓；fort transversal：**STOP** ✗；**开邻域+Walsh：STOP（本档，＝已审计 ✓）** ✗；**上界侧（文献 120 → 119）**：**LIVE ✓✓**（C-427 战略更新 ✓）；D-LP-1B：**OPEN** ✓
- 【**战略不变 ✓**】可达一侧仍是**上界侧**：起点用**文献已知 120-cover**（非我们的 124 ✓），目标 119 ✓；且**先做 D-LP-1B 归因**（定"新不变量必须超过的标杆" ✓）
- 【**边界 ✓**】本档为 P0 审计（非新数学命题 ✓）；零程序计算；未改门；不跨空间；不声称 P1 成立／不成立 ✗（V290）；谱/Krawtchouk 对应为标准事实（档级 ✓）
- 档：本条目（registry-only ✓）

**🧩 C-429（2026-09-27 23:55 · **subspace distribution ＋ conditional LP：P0 已在档案（2026-09-26 三档）＋ n=10 系统推广（新）**）** ✓
- 【**★P0 状态：已做完（2026-09-26 ✓✓，勿重做）**】档案三档已给出 source-first 拆解：
 ① `PROVENANCE-2026-09-26-how-62-was-proved-and-the-diagnosis.md` ✓：**2001 摘要逐字**——"possible **distributions of codewords in subspaces** are refined until each subspace is of **dimension zero**… Repeatedly, a **linear programming problem** is solved considering only **inequivalent distributions**. A connection between this approach and **weighted coverings** is also presented" ✓✓ ⟹ **62 的证明类型 ＝ 计算机辅助的分类／LP 细分** ✓（非解析局部不等式 ✓）
 ② `OBREVERSE-2026-09-26-…` ✓：**引文网络（OB2001 被引 21 篇 ✓）**＋ **候选 LP 指纹表**＋ **重建算法**（节点 LP 不可行 ⟹ 剪枝；可行 ⟹ 按 inequivalent refinements 分支；至 cell 维 0 ⟹ 精确 IP／certificate ✓）＋ **审计发现：目标很可能已被分类文献覆盖** ⚠️✓
 ③ `MCOVER-2026-09-26-…` ✓：**精确重建 binary $n=9$, $R=1$ 的 level-$m$ M-covering system** ✓✓：固定前 $m$ 坐标 ⟹ $t=2^m$ cells、每 cell $s=2^{9-m}$ 词 ✓；$y_i=|C\cap C_i|$ ✓；$$\boxed{A_{ii}=10-m;\quad A_{ij}=\mathbf 1_{\{d(p_i,p_j)=1\}};\quad A_{ij}=0\ (d\ge2)};\qquad \sum_jA_{ji}y_j\ \ge\ 2^{9-m}\ (\forall i)$$ ✓✓（推导一行 ✓）；实测**逐层收紧律 $1.21\to1.09$** ✓；$m=9$ 极限 ＝ 覆盖条件本体 ✓
- 【**★★n=10 系统推广（本档新 ✓✓，一行推导）**】同样"固定 $m$ 坐标"分区 ⟹ $t=2^m$ cells、每 cell $s=2^{10-m}$ ✓；$y_i=|C\cap C_i|$、$\sum_i y_i=|C|\le119$ ✓；$$\boxed{A_{ii}=\mathbf{11-m}\ \big(=1+(10-m)\ ✓\big);\qquad A_{ij}=\mathbf 1_{\{d(p_i,p_j)=1\}};\qquad A_{ij}=0\ (d\ge2)};\qquad \sum_jA_{ji}y_j\ \ge\ 2^{10-m}\ (\forall i)$$ ✓✓ —— **即"对角线 $=n+1-m$"的一般化** ✓（$n=9$ 档的 $10-m$ ✓ → $n=10$ 的 $11-m$ ✓）；该 LP 家族＝OB 机制的**可执行形式** ✓
- 【**★P0→P1 桥（登记未跑 ⚠️）**】把**我们自己的剪枝引理**作为节点级附加约束：① **自由坐标引理**（$C=D\times\mathbb F_2\Rightarrow|C|\ge124$ ⟹ **任何 $\le123$-cover 必须坐标不可约** ✓，C-422／R2-2 ✓）—— 顶层最强的分区剪枝 ✓✓；② $(\alpha)(\alpha')$ 内部子立方体排斥 ✓（最细层可用 ✓）；③ C-419 折衷关系 $b_3+4b_4\ge\binom s3$ ✓；**据此的 P1 形态**：顶层 $m=1$ 的 $n=10$ LP ＋ 上述约束 ⟹ **问是否不可行** ✓
- 【**STOP 判据（两条 ✓）**】① 若 $n=10$ 各级 LP **在加入我们的约束后仍全可行** ⟹ 分支无增益 ⟹ **STOP** ✗；② **新颖性闸（AMEND-21／24 ✓）**：`OBREVERSE` 已自查"目标**很可能已被分类文献覆盖**" ⚠️（含 [2009] Linderoth–Margot–Thain：isomorphism pruning ＋ subcode enumeration ＋ LP bounding ✓；[2003] Östergård：无 balanced 码达 $K(9,1)=62$ ✓）⟹ **方法可借用（LANE-A 合规 ✓），但不得声称"新机制"** ✓✓
- 【**⚠️ 规模警告（诚实 ✓）**】$n=9$ 的缺口 $57\to62=\mathbf 5$ ✓；$n=10$ 的缺口 $107\to120=\mathbf{13}$ ✓（≈2.6 倍 ✓）且状态空间远大于 $n=9$ ✓；档案实测收紧律仅 $1.21\to1.09$（**温和** ✓）⟹ **很可能瓶颈在规模而非强度** ⚠️（与唐先生猜测一致 ✓，但须实跑方能断言 ✗）
- 【**⚠️ 命名碰撞提醒（纪律 ✓）**】`P2-α`（2026-09-26 ✓）里的"$N_4\le9$"是**当时另一条线的刚性命题** ✓，**与**本线 C-419 的 $N_4$（距离-4 对数 ✓）**不是同一对象** ✗ —— 引用时必须显式区分 ✓
- 【**边界 ✓**】本档＝**档案核对 ＋ 一行推广**（非新数学命题 ✓）；零程序计算（**未跑 solver** ✓）；未改门；不跨空间；不声称 P1 成立／不成立 ✗（V290）
- 档：本条目（registry-only ✓；源档三份见上 ✓）

**🧮 C-430（2026-09-27 23:58 · **P1-WIT：见证系统冗余夹逼（新）＋ $b_4$ 的首个独立上界**）** ✓
- 【**★★(1) 见证系统冗余夹逼（新 ✓✓）**】对 $T\subseteq S(c),|T|=3$ 定义 $W(T):=\{x\notin T:c\oplus e_{T\cup\{x\}}\in C\}$、$m_T:=|W(T)|\ge1$ ✓ ⟹ $$\boxed{\binom{s(c)}3\ \le\ 4b_4+b_3\ =\ \sum_Tm_T\ \le\ \binom{s(c)}3+E_3(c)}$$ ✓✓ 其中 $E_3(c)=8d_2(c)+d_3(c)+4d_4(c)-120$ ✓（C-417 $k=3$ 恒等式 ✓）；**左端＝C-419 的不等式 ✓；本档把 $4b_4+b_3$ 证明为\*\*恒等式\*\* $\sum_Tm_T$ ✓，并补出\*\*上界\*\* ✓**
- 【**★★(2) 见证星结构（新 ✓✓，非 profile ✓）**】固定 $T$ 时，其 $m_T$ 个见证码字 $c\oplus e_{T\cup\{x\}}$ **全部落在同一球 $B_1(p_T)$ 内** ✓✓（$d(p_T,\cdot)=1$ ✓、两两距离 $2$ ✓），且球心 $$p_T:=c\oplus e_T\ \textbf{非码字}\ ✓\ \big(\text{由 }(\alpha)✓\big)$$ ⟹ **"见证星"** ✓
- 【**★(3) $b_4$ 的首个独立上界（新 ✓）**】$$\boxed{b_4\ \le\ \big(\tbinom{s(c)}3+E_3(c)\big)/4}$$ ✓（＝C-419 所缺"输入"的**上界侧一半** ✓）；同得 $b_3\le\tbinom s3+E_3$ ✓、冗余 $4b_4+b_3-\tbinom s3\in[0,E_3]$ ✓
- 【**⚠️(4) 诚实：与 C-419 联用\ \textbf{不改善}容量界 ✗**】$E_3\ge0\Longrightarrow d_4\ge\tbinom s3-3b_4\ge\frac{\tbinom s3-3E_3}4\le\frac{\tbinom s3}4$ ✓ ⟹ **该组合仍只回到容量界** ✗✓（本引理**单独不加强下界** ✓）
- 【**★★(5) 精确剩余缺口（C-419"缺输入"的锐化 ✓✓）**】要超过容量界，**只需其一**：**(i)** $b_4<\tbinom{s(c)}3/4$ ✓（⟹ $d_4\ge\tbinom s3-3b_4>\tbinom s3/4$ ✓）；**(ii)** $b_4>\tbinom{s(c)}3/4$ ✓（⟹ $d_4\ge b_4>\tbinom s3/4$ ✓）⟹ **真正缺的输入 ＝ 把 $b_4$ 相对 $\tbinom{s(c)}3/4$ \textbf{定位}** ✓✓；本档上界与目标只差 $\mathbf{E_3/4}$ ✓（**若能把上界再压 $E_3/4$ 即成功** ✓）
- 【**（登记未做 ✓ 后续可攻点）**】① 用"见证星"共享同一球心 $p_T$ 的**互斥性**（两星是否不交？✓）收紧；② 用 $p_T$ 间的距离结构（$|T\cap T'|$ 决定 $d(p_T,p_{T'})$ ✓）建**第二计数** ⚠️
- 【**边界 ✓**】**零程序计算** ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不做路线决定** ✓（照唐先生 23:54 令 ✓：本档只给结果与缺口，STOP／切换由唐先生裁定 ✗）；不跨空间（回查已分栏 ✓）；不声称 P1 成立 ✗（V290）；不声称与 C-419 联用已获增强 ✗（§3 已标注 ✓）
- 档：`docs/P1-WIT-2026-09-27-witness-redundancy-sandwich-and-first-independent-b4-bound.md`

**🧪 C-431（2026-09-28 00:0x · **SUBSPACELP：level-$m$ 系统 LP 松弛 ≡ 体积界（零增益）＋ 引擎定位**）** ✓
- 【**★★等号定理（新 ✓✓）**】对 binary $R=1$、任意 $n$、任意 $1\le m\le n$：$$\boxed{L(m)=\frac{2^n}{n+1}\ \textbf{恰好等号}}$$ ✓ ① 聚合 $t$ 约束 ⟹ $(n+1)\sum_iy_i\ge2^n$ ⟹ $L(m)\ge\frac{2^n}{n+1}$ ✓；② **均匀解** $y_i\equiv\frac{2^{n-m}}{n+1}$ 可行（每列和 $=\sum_iA_{ji}=|B_1(c)|=n+1$ ✓，且 $\le s$ ✓）⟹ $L(m)\le\frac{2^n}{n+1}$ ✓ ⟹ 等号 ✓✓
- 【**★★零增益实测 ✓✓**】$n=9$：$L(m)\equiv\mathbf{51.200000}$（$m=1..9$ ✓）；$n=10$：$L(m)\equiv\mathbf{93.090909}$（$m=1..10$ ✓）⟹ **refinement 增益 ＝ 0** ✗✓（含 $m=n$ 即覆盖条件本体层 ✓）
- 【**★★引擎定位（诊断 ✓✓）**】**OB 机制的引擎不是 LP** ✗，而是**整性 ＋ 不等价分布分类 ＋ 递归** ✓✓；**LP 的真实角色 ＝ 剪枝／校验** ✓（其松弛**恰好只给体积界** ✓）；**全部强度必来自整性约束 + 分支** ✓
- 【**结构原因 ✓**】系统**双重平衡**（每列和 $=|B_1(c)|=n+1$ ✓、每行同值 $s$ ✓）⟹ **均匀分数解恒最优** ⟹ 松弛恒等于体积界 ✓✓
- 【**与基线对照 ✓**】$93.090909$（体积界 ✓）$<$ $94.0197982$（Delsarte LP ✓）$<$ $101.0073568$（Van Wee ✓）$<$ $101.4081694$（combined classical ✓）$<$ $105.2223$（SDP ✓）$<$ $107$（文献下界 BÖW 2004 ✓）$<$ $120$（文献上界 ✓）⟹ **本 cell-LP 严格弱于关联方案 LP** ✓
- 【**★Test C 下一步（登记未跑 ⚠️，照唐先生 ✓）**】既然 LP 层零增益 ⟹ 直接测**整层**：$\#\big\{y\in\mathbb Z_{\ge0}^{2^m}:A^Ty\ge s\mathbf 1,\ 0\le y\le s,\ \sum_iy_i=M\big\}$ 的**码等价轨道数** ⟹ 即唐先生要的 **branch factor** ✓；$m\le4$（$t\le16$）可枚举 ✓，更大需 DP/母函数 ⚠️；**进一步可挂**：① 自由坐标引理（顶层剪枝 ✓）② $(\alpha)(\alpha')$ ✓ ③ C-419／C-430 折衷 ✓ ④ 有效 120-码 `work/k10/kamenetsky120.txt` 的对称/切换模式对比 ✓
- 【**产物**】`scripts/SUBSPACE_LP_2026-09-28_level_m_bound.py` ＋ `scripts/SUBSPACE_LP_2026-09-28_level_m_bound.txt`（逐字输出 ✓；经 `pyguard.sh 800` ✓ 单线程 ✓）；档 `docs/SUBSPACELP-2026-09-28-level-m-lp-relaxation-equals-volume-bound.md`
- 【**边界**】有计算（小 LP ✓）；未上 SDP/SAT；未改门；**不作路线裁定** ✗（照 23:54 令 ✓）

**🌟 C-432（2026-09-28 00:0x · **WITSTAR：见证星交叠精确分类 ＋ 私/公二分 ＋ Johnson 恒等式**）** ✓
- 【**★★精确分类（sharp，无条件 ✓✓）**】对 $T,T'\subseteq S(c)$、$|T|=|T'|=3$：$$\boxed{\big|W(T)\cap W(T')\big|=\mathbf 1_{\{|T\cap T'|=2\}}\cdot\mathbf 1_{\{c\oplus e_{T\cup T'}\in C\}}}\quad(\in\{0,1\}✓)$$ ✓✓ 特别：$|T\cap T'|\le1\Rightarrow W(T)\cap W(T')=\varnothing$ ✓（＝唐先生所写 ✓）；$|T\cap T'|=2\Rightarrow\le1$ ✓✓（**严于唐先生的 $\le2$** ✓）
- 【**★★锐化理由（无条件 ✓✓）**】两球心 $p_T,p_{T'}$ 在 $d=2$ 时确有 2 个公共邻点，但**只有一个可达见证**：$c\oplus e_{T\cap T'}$（距离 2 ✓ **非见证** ✗）与 $c\oplus e_{T\cup T'}$（距离 4 ✓ 唯一候选 ✓）⟹ 因**见证必为距离-4 码字** ✓ 故 $\le1$ ✓（无需 $A(c)=0$ ✓）
- 【**★★私/公二分（新 ✓✓）**】按 $|S_y\cap S(c)|$ 分类距离-4 见证：**b_3 型**（$=3$）**只属于一个星**（私有 ✓）；**b_4 型（内部块）**（$=4$）**恰属于 $\binom43=4$ 个星**（公有 ✓）$$\Longrightarrow\ \boxed{\sum_Tm_T=4b_4+b_3}\ \text{的系数 }4,1\ \textbf{由此而来}✓✓\ \big(\text{由计数整理升为结构事实}✓\big)$$
- 【**★★精确 Johnson 恒等式（新 ✓✓）**】$$\boxed{\sum_T\binom{m_T}2=\sum_{y<y'\in D_4(c)}\binom{|S_y\cap S_{y'}\cap S(c)|}3}=\#\{\{y,y'\}:d(y,y')=2,\ S_y\cap S_{y'}\subseteq S(c)\}=E_J+E_{\rm cross}$$ ✓✓（Johnson 边 ＋ 交叉对 ✓）
- 【**★纪律（照唐先生 §3 ✓）**】保持 $4b_4+b_3$ 口径 ✓；**不得**偷换为 $4d_4(c)$ ✗（$\binom{|S_y\cap S(c)|}3=0$ 当 $\le2$ ✓ ⟹ $4d_4(c)$ 会**高估** ✗）
- 【**评估（照判据 ✓，不做裁定 ✗）**】① **过门 ✓✓**：$\sum_T\binom{m_T}2$ 取决于 4-集**成对交叠** ✓，非 profile 量 ⟹ **未落入 STOP** ✓（属 C-417／C-425 之外**第三种** ✓）；② ⚠️**下界侧为空** ✓（$\sum_Tm_T=\binom s3$ 时 $\forall T:m_T=1$ ⟹ 二阶量 $=0$ ✓，凸性不给正下界 ✗）；③ ⚠️**上界侧＝唯一活口** ✓（登记未做 ✗；可用局部界：$E_J\le2b_4(s-4)$ ✓、$E_{\rm cross}\le b_3b_4$ ✓）
- 【**不碰 $E_3$** ✓（照唐先生 §7 刹车 ✓）】；**零程序计算** ✓；**不作路线裁定** ✗；档 `docs/WITSTAR-2026-09-28-witness-star-overlap-classification-private-public-and-johnson-identity.md`

**⚖️ C-433（2026-09-28 10:1x · **WITCOV：$R=0$ 两处修正 ＋ 强制高层覆盖定理（新）**）** ✓
- 【**✗修正一（算术滑落）**】$b_3=\binom s3-4b_4$ 代入 $b_4\le\frac14\binom s3$ **只给 $b_3\ge0$** ✗；唐先生所写 $b_3\ge\frac12\binom s3$ **不成立** ✗✓（该数字恰是错代换产物 ✓）。**整数核对**（$s=0..10$）：$b_3$ 下界依 $s$ 为 $0,0,0,1,0,2,0,3,0,0,0$ ✓（非 $\frac12\binom s3$ ✓）
- 【**✗修正二（packing 界用错对象）**】正确界涉及 **$S$ 内部的 pair** ✓：$$b_3\le(10-s)\Big\lfloor\tbinom{s}{2}/3\Big\rfloor$$ ✓（因同外部坐标 $x$ 下的 $B_3$ triples 两两至多共享 1 点 ⟹ 每 pair 至多用一次 ⟹ $3|\mathcal B_x|\le\binom s2$ ✓）—— **非** $\binom t2$ ✗（与上一轮 (20) 一致 ✓）
- 【**结论 ✗**】**"$R=0\Rightarrow s\le4$" 不成立** ✗✓：修正后**无 $s$ 上界** ✓；$R=0$ 在**所有 $s$** 存活 ✓（$s=10$ 反而极紧：$b_3\le0\Rightarrow b_3=0\Rightarrow b_4=30$ ✓，无矛盾 ⚠️）
- 【**★★(3) 强制高层覆盖定理（新 ✓✓，一般形式，\textbf{不需} $R=0$）**】$$u\subseteq S(c),\ |u|=4,\ c\oplus e_u\notin C\ \Longrightarrow\ \exists\,i\notin u:\ c\oplus e_{u\cup\{i\}}\in C$$ ✓✓ **证明 3 行**：点 $c\oplus e_u$ 须被覆盖 ✓；其 1-邻点两类 —— $c\oplus e_{u\setminus i}$（$|u\setminus i|=3$、$\subseteq S(c)\overset{(\alpha)}{\Longrightarrow}\notin C$ ✗）与 $c\oplus e_{u\cup i}$（$|u\cup i|=5$ ✓）⟹ **唯一出路 ＝ 距离-5 码字** ✓✓（＝档案 P1-D3"被迫高层码字"的**对偶层** ✓✓）
- 【**★(4) 计数形式（新 ✓）**】$$\binom{s(c)}4-b_4\ \le\ \sum_{w\in C,\,d(c,w)=5}\binom{|S_w\cap S(c)|}4\ =\ 5c_5+c_4$$ ✓（$c_j:=\#\{w:d(c,w)=5,\ |S_w\cap S(c)|=j\}$ ✓；$j=5$ 贡献 5 ✓、$j=4$ 贡献 1 ✓、$j\le3$ 贡献 0 ✗）
- 【**★(5) 级联（新 ✓✓，登记未做 ⚠️）**】$k\ge4$：若某 $k$-子集 $W\subseteq S(c)$ 的**全部** $(k-1)$-子集皆缺失 ⟹ $\exists$ weight-$(k{+}1)$ 码字 $\supseteq W$ ✓（同法 ✓）；$R=0$ 时 $B_4$ 稀疏（$4b_4\le\binom s3$）⟹ 大量缺失 ⟹ **强制塔**上行 ✓✓ ⟹ **必在 weight $\le10$ 终止 ⟹ 终止层即潜在矛盾位置** ⚠️
- 【**★(6) $s=4$ 两刚性模型（分类仍成立 ✓）**】$(b_4,b_3)\in\{(1,0),(0,4)\}$ ✓（只用 $b_4\le\frac14\binom43=1$ ✓）；**Model A** $B_4=\{S\}$：单 4-子集自覆盖 ⟹ 无强制 ✓；**Model B** $B_4=\varnothing,B_3=\binom S3$ ⟹ $c\oplus e_S\notin C$ ⟹ **强制 weight-5 码字 $c\oplus e_{S\cup\{i\}}$（$i\in S^c$）** ✓✓（须 $s\le9$ ✓）
- 【**状态 ✓**】**$R=0$ 未被排除** ✓（§3 明示其在所有 $s$ 存活 ✓）；新定理为"$B_4\to$ layer-5"接口的**正确形式** ✓ 且**一般成立**（非 $R=0$ 专属 ✓）；级联为下一步 ⚠️（**登记未做，唐先生裁定 ✗**）
- 【**依赖 ✓**】§0(3) 依赖 $(\alpha)$（即 $A(c)=0$ ✓）—— 引用须与 C-410 同引 ✓；**零程序计算**（仅一处整数核对 ✓）；**不作路线裁定** ✗（照 23:54 令 ✓）
- 档：`docs/WITCOV-2026-09-28-r0-two-corrections-and-forced-high-layer-covering-theorem.md`

**🌊 C-434（2026-09-28 10:2x · **WITCASC：无条件级联引理 ＋ $k{=}10$ 终止二择 ＋ 为何仍无矛盾**）** ✓
- 【**★★(1) 一般级联引理（新 ✓✓，\textbf{无条件}、不需 $(\alpha)$、不需 $R{=}0$）**】$W\subseteq[10]$、$4\le|W|=k\le9$：$$c\oplus e_W\notin C\ \wedge\ \forall i\in W:\ c\oplus e_{W\setminus i}\notin C\ \Longrightarrow\ \exists\,j\notin W:\ c\oplus e_{W\cup j}\in C$$ ✓✓ **证明 4 行**：点 $p=c\oplus e_W$ 须被覆盖；其 1-邻点恰两类（$j\in W$：$c\oplus e_{W\setminus j}$ —— 被假设排除 ✗；$j\notin W$：$c\oplus e_{W\cup j}$ ✓）＋ $p$ 自身（亦被排除 ✗）⟹ **唯一出路** ✓（权 $\le10$ ⟹ 须 $k\le9$ ✓）
- 【**★★(2) 终止二择（新 ✓✓，对\ \textbf{每个} $c\in C$）**】$k=10$ 无 $j\notin W$ ⟹ 若 $c\oplus e_{[10]}\notin C$ 且 $\forall i:\ c\oplus e_{[10]\setminus i}\notin C$ 则该点**未被覆盖** ✗ ⟹ $$\boxed{\text{或 }c\oplus e_{[10]}\in C\ \text{（weight-10）};\ \text{或}\ \exists i:\ c\oplus e_{[10]\setminus i}\in C\ \text{（weight-9）}}$$ ✓✓（对任一 119-cover 的任一码字成立 ✓）
- 【**★★(3) 与 witness 系统统一（新 ✓✓）**】$k=3$ 的同类式（"下邻"＝weight-2 点）由 $A(c)=0$ **自动排除** ⟹ 得**强制 weight-4 witness** ✓✓ ＝ **见证系统**（C-419／C-430／C-433 ✓）⟹ **见证系统 ＝ 级联的 $k{=}3$ 层** ✓✓；级联 ＝ 其 $k\ge4$ 自然延拓 ✓（"迫使高层"是同一机制的连续谱 ✓）
- 【**★(4) $(\alpha)$ 假设已核（引用纪律 ✓）**】原文（P1-MICRO 行 17-18）：$(\alpha)$ 依赖 **全局 tetra-avoidance**（$N_{\rm tetra}=0$，即 P1-AVOID 案前提 ✓）**而非仅 $A(c)=0$** ✗✓；**级联引理本身不需 $(\alpha)$** ✓（与 WITCOV §0(3) 恰相反 —— 那条**需要** ✓）
- 【**★(5) $s=10$ 强制塔定量（新 ✓）**】$R=0\Rightarrow b_3=0,b_4=30\Rightarrow$ 缺失 4-子集 $=180$ ⟹ $\boxed{c_5+c_4\ge36}$ ✓；"全 4-子集缺失"的 5-子集 $=252-30\cdot6=72$（**两 $B_4$ 块交 $\le2$ ⟹ 不可共处 5-集 ✓**）⟹ $\boxed{c_6\ge12}$ ✓；合计 $\ge48\ll118$ ✓
- 【**★(6) 层-5 覆盖者共享规则 ✓**】两个缺失 $u,u'$ 可共享覆盖者 $\iff|u\cap u'|=3\ \wedge\ c\oplus e_{u\cup u'}\in C$ ✓（Johnson 式 ✓）
- 【**⚠️(7) 为何仍无矛盾（三条精确原因 ✓）**】① **禁层只有 weight 2／3** ✓（$(\alpha)$ 与 $A(c)=0$ 只排 $\le3$ ✓；weight $\ge4$ 内部码字**完全无约束** ✗，与 P1-D4b 的 $C_0$ 显式反例一致 ✓）；② **容量充裕** ✓（层-5 需 $\ge36$ vs 可用 $252$ ✓；层-6 需 $\ge12$ vs $210$ ✓，每层差一个数量级 ✓）；③ **顶端仅给二择、不给否证** ✗✓（唯一无出口处是 $k=10$ ✓）⟹ **级联 ＝ forced tower ✓；\textbf{不能}判死 $R{=}0$** ✗✓（照唐先生判据 ✓）
- 【**★(8) 要产生矛盾需要什么（登记 ✗）**】① 层 $\ge4$ 的**禁配置**（$k\ge4$ 的 $(\alpha)$-类比 —— 目前**不存在** ✗）；② 或**容量冲突**（各层差一个数量级 ⟹ 需真正的全局计数 ✗）
- 【**边界 ✓**】零程序计算 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗（照 23:54 令 ✓）；$(\alpha)$ 依赖已精确标注 ✓（防误引 ✓）；不声称 $R=0$ 已排除 ✗；不声称 P1 成立 ✗（V290）
- 档：`docs/WITCASC-2026-09-28-cascade-lemma-termination-dichotomy-and-why-no-contradiction.md`

**🧬 C-435（2026-09-28 10:3x · **WITFIB：FIBER-INDUCTION 精确形式 ＋ 五条必要条件 ＋ $\mathrm{cov}_9$ 活口**）** ✓
- 【**设定 ✓**】$C\subseteq\mathbb F_2^{10}$、$|C|=119$、半径-1 覆盖 ✓；取定末坐标 $(x,b)$ ✓；$P_b:=\{x:(x,b)\in C\}$、$a=|P_0|$、$b=|P_1|$、$a+b=119$ ✓；$N_9[\cdot]$＝9 维闭半径-1 邻域 ✓
- 【**★★(1) 覆盖条件的精确等价（本档核心 ✓✓）**】$$\text{整码覆盖}\iff \mathbb F_2^9=N_9[P_0]\cup P_1\ \wedge\ \mathbb F_2^9=N_9[P_1]\cup P_0\iff\boxed{U_0\subseteq P_1\ \wedge\ U_1\subseteq P_0}$$ ✓✓（$U_b:=\mathbb F_2^9\setminus N_9[P_b]$ ＝ "层 $b$ 的洞" ✓；$m(x)=0$ 的 fiber 两点**各需邻层承担** ✓ ＝ 唐先生的 $L(x)=2-m(x)$ 读法 ✓）
- 【**★★(2) $P_0\cup P_1$ 必是 9-cover（新 ✓✓）**】$\mathbb F_2^9\subseteq N_9[P_0]\cup N_9[P_1]=N_9[P_0\cup P_1]$ ⟹ $$\boxed{|P_0\cup P_1|\ge K(9,1)=62}\ \Longrightarrow\ \boxed{|P_0\cap P_1|\le\mathbf{57}}$$ ✓✓（**＝唐先生期望的 P1，成立 ✓✓**）
- 【**★★(3) 分裂必须平衡（新 ✓✓）**】$|U_0|\ge512-10a$ 且 $U_0\subseteq P_1$ ⟹ $512-10a\le b$ ⟹ $$\boxed{a\ge\big\lceil 393/9\big\rceil=\mathbf{44}}$$ ✓✓（对称 $b\ge44$ ⟹ $a\in[44,75]$ ✓）
- 【**★(4) 负载式（新 ✓）**】$|U_0|+|U_1|\le a+b=119$ ⟹ $$\boxed{|N_9[P_0]|+|N_9[P_1]|\ge\mathbf{905}}$$ ✓✓（＝唐先生的 $905$ ✓，现为**必要式** ✓）
- 【**★★(5) 精确必要条件（新 ✓✓ ＝ 唐先生 P3 的正确形式）**】$\mathrm{cov}_9(s):=\max_{|S|=s}|N_9[S]|$ ✓（**"$K(9,1)=62$ 的带 holes 版本"**）$$\boxed{512-\mathrm{cov}_9(a)\le b\ \wedge\ 512-\mathrm{cov}_9(b)\le a}$$ ✓✓（$\mathrm{cov}_9(62)=512$ ✓ 饱和点 ✓）
- 【**★(6) 递归形式（新 ✓）**】$m$ 维分裂（两层 $s_1,s_2$）：$2^m-(m+1)s_1\le s_2$ 且对偶 ✓ ⟹ **分裂树**，逐层下降至 $m=1$ ✓（与 Östergård–Blass 的 subspace 递归**同族**，但用 $K$ 的 **holes** 而非 LP ✓）
- 【**⚠️(7) 但计数层被封顶（诚实 ✓✓）**】由 (3)＋(4) 相加即得 $(n+1)|C|\ge2^n$ ⟹ $|C|\ge93.09$ ⟹ **与 C-431"cell-LP ≡ 体积界"同一层** ✓ ⟹ **任何只用 $|S|,|N[S]|$ 的计数式都到不了 119** ✗✓
- 【**★★活口 ✓✓**】唯一可用 ＝ $\mathrm{cov}_9(s)$ 的**精确形状**（$s\le61$ 时洞的结构 ✓），而非计数上界 ⟹ **＝唐先生 P3** ✓；**未证明**它在 $s\le61$ 处足以产生矛盾 ✗（登记未做 ✓）
- 【**⚠️ P2 的诚实答复（未找到 ✗）**】第二个"被迫 9-cover"对象：自然候选 $P_0\cap P_1$、$P_0\triangle P_1$、$P_0$、$P_1$ **皆不被迫覆盖** ✗；$N_9[P_0]\cup N_9[P_1]=\mathbb F_2^9$ 是覆盖条件本身（无新信息 ✓）⟹ **尚无 $|P_0|+|P_1|\ge124$ 型冲突** ✗
- 【**边界 ✓**】零程序计算 ✓（三处整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗（照 23:54 令 ✓）；$K(9,1)=62$ 为**文献值**（档级 ✓）；不声称 119 已排除 ✗；不声称 $\mathrm{cov}_9$ 路线必成 ✗（V290 ✓）
- 档：`docs/WITFIB-2026-09-28-fiber-induction-exact-form-five-necessary-conditions-and-cov9-gate.md`

**🎨 C-436（2026-09-28 10:4x · **WITW2C：119 ⟹ 9 维双色加权 2-覆盖；跨色收紧 ＋ $K(9,1)$ 咬点**）** ✓
- 【**★★(1) 逐点精确条件（本档收紧 ✓✓）**】$\forall x\in Q_9$：$$c_0(x)+g(x)+(Ac_0)(x)\ge1\ \wedge\ c_1(x)+g(x)+(Ac_1)(x)\ge1$$ ✓✓（$c_0,c_1$ ＝ 两层指示、$g=c_0+c_1$、$A$ ＝ $Q_9$ 邻接矩阵 ✓）⟹ **收紧**：$x\notin U$ 时须 **$N(x)\cap C_0\ne\varnothing$ 且 $N(x)\cap C_1\ne\varnothing$** ✓✓ —— 唐先生所写"两个 light 邻点"**必要但不充分** ✗（须**一色一个** ✓）⟹ 距离-2 对必须**跨色** $\Longrightarrow$ 正确的量是 $\boxed{e_2^{A_\ast B_\ast}(L)}$ **而非** $e_2(L)$ ✓✓
- 【**★★(2) 精确等价（双向 ✓）**】119-cover of $Q_{10}$ $\iff$ 对 $(C_0,C_1)\subseteq Q_9$ 逐点满足 (1) ✓✓ ⟹ **fiber 化 ＝ 精确重述（非归约 ✓）**，但把问题变成 **9 维双色加权 2-覆盖** ✓
- 【**✓(3) 计数链全成立（唐先生 §1–§10 ✓）**】$s=|U|\ge62$ ✓；$|H|=119-s$、$|L|=2s-119$ ✓；$s\le69\iff9|H|\ge|U^c|$ ✓；$s\ge70\Longrightarrow|X_L|\ge\boxed{8s-559}$ ✓；$|X_L|\le2e_2^{A_\ast B_\ast}\Longrightarrow\boxed{e_2^{A_\ast B_\ast}\ge\lceil(8s-559)/2\rceil}$ ✓
- 【**⚠️(4) 但这些界全不咬（本档核实 ✓）**】$e_2^{A_\ast B_\ast}\le36\min(|A_\ast|,|B_\ast|)\le2124$ vs 需求 $\le197$ ✗；且 $\sum_x[2g+Ag]=1309\ge1024$ ＝ **体积界 $93.09$** ✓ ⟹ **与 C-431 同一现象：一切聚合型推论落回体积界** ✗✓ ⟹ 一阶/二阶计数**耗尽** ✓
- 【**★★(5) 自动结论（新 ✓✓，只用 $K(9,1)\ge62$）**】$|H|=119-s\le57<\mathbf{62}\Longrightarrow H$ **永不可能是 9-cover** ✓✓ ⟹ $\exists y\notin N[H]$ ⟹ $$\boxed{\text{必有其一}:\ \textbf{(α)}\ \exists\ light\ \text{点与 }H\ \text{完全不相邻};\quad \textbf{(β)}\ \exists\ \text{外部点 }y\notin U\ \text{无 heavy 邻点（⟹ 需一 }A_\ast\text{-邻点}＋\text{一 }B_\ast\text{-邻点）}}$$ ✓✓
- 【**★★(6) $s=62$ 端的条件性矛盾（新 ✓✓，$K(9,1)$ 唯一已知咬点）**】$s=62\Rightarrow|H|=57,|L|=5$、$U$ ＝ 最优 62-cover ✓；**若** (i) $L\subseteq N(H)$ **且** (ii) $U^c\subseteq N(H)$ $\Longrightarrow N[H]=\mathbb F_2^9$ $\Longrightarrow$ $H$ 是 **57-词 9-cover** $\Longrightarrow$ **与 $K(9,1)=62$ 矛盾** ✗✗ ⟹ $\boxed{s=62\ \text{时必有}\ \neg(i)\vee\neg(ii)}$ ✓✓ **缺件**：62-最优码的分类（switching class ✓）⟹ 需文献/计算 ⚠️（登记未做 ✓）
- 【**★(7) 唐先生 §12 的目标形式 ✓**】$\mathcal L_9(U):=\min_\chi\{|C_0|+|C_1|:\ C_0\cup C_1\supseteq U,\ C_0^c\subseteq N[C_1],\ C_1^c\subseteq N[C_0]\}$ ✓（＝9 维**双色加权 2-覆盖**最轻配置 ✓）⟹ **119 问题 ⟺ $\exists$ 9-cover $U$：$\mathcal L_9(U)\le119$** ✓；**等价目标**：$\forall$ 9-cover $U$：$\mathcal L_9(U)\ge120$ ✓✓；与 $K(9,1)=62$ 的关系：$\mathcal L_9\ge|U|\ge62$ 仅**第一层** ✓，多出的是**双色条件的代价** ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗（照 23:54 令 ✓）；$K(9,1)=62$ 文献值（档级 ✓，只用其下界方向 ✓）；不声称 119 已排除 ✗；不声称 $s{=}62$ 必矛盾 ✗（**条件性**已明示 ✓）；不声称 P1 成立 ✗（V290）
- 档：`docs/WITW2C-2026-09-28-two-colour-weighted-2-cover-cross-colour-tightening-and-K91-bite.md`

⚠️ **[勘误指针]** C-437 §0(3) 的 $\sum q_{ab}\ge|U^c|\ge450$ 一步**已作废** ✗ ⟹ 见 **C-438**（正确形式 $\ge|X_L|$ ✓）；C-437 其余部分仍有效 ✓。

**🔷 C-437（2026-09-28 10:5x · **WITSAT：精确条件锐化 ＋ $q_{ab}$ 恒等式 ＋ 饱和事件无局部上界**）** ✓
- 【**范围 ✓**】**不攻 62-码完整分类** ✓（照唐先生 10:32 源核查：公开资料只确认"两个已知构造同属一个 switching class" ✓，未给全分类 ✗；且 2001 证明本身是**计算辅助子空间分解＋LP** ✓）；改攻 $(\alpha)/(\beta)$ 的 $q_{ab}$／$n_2$ 问题 ✓
- 【**★★(1) 精确条件最锐形式（新 ✓✓）**】$$\textbf{119-cover of }Q_{10}\iff \boxed{U^c\ \subseteq\ N(C_0)\cap N(C_1)}$$ ✓✓（**外部点必须"双色邻接"** ✓）⟹ 与 C-435 形式 $U_b\subseteq P_{1-b}$ **严格等价** ✓✓（双向证明已给 ✓）
- 【**✗(2) 修正（本档 ✓）**】两色要求**只落 $U^c$，不落 $D$** ✗✓（唐先生 §1"对任意 $x\in D$"**过强** ✗）。**理由 3 行**：$g(x)\ge1\Longrightarrow$ 整条 fibre $\{(x,0),(x,1)\}$ **自覆盖** ✓✓（$x\in C_0$ 时 $(x,0)\in C$ 覆盖自身与 $(x,1)$ ✓）⟹ **约束只对 $g(x)=0$ 出现** ✓；故 $D\cap A$、$D\cap B$ 的点**无任何覆盖要求** ✓
- 【**★★(3) $q_{ab}$ 精确恒等式（新 ✓✓）**】$q_{ab}:=|U^c\cap N(a)\cap N(b)|\in\{0,1,2\}$ ✓（距离-2 对恰两共同邻点 ✓）$$\boxed{\sum_{a\in A,b\in B}q_{ab}\ =\ \sum_{x\in U^c}|N(x)\cap A|\cdot|N(x)\cap B|\ \ge\ |U^c|\ \ge\ 450}$$ ✓✓（**左＝pair 侧、右＝点侧乘积** ✓；因每个 $x\in U^c$ 贡献 $|N_A|\cdot|N_B|\ge1$ ✓ ⟹ 反过来说明 $q_{ab}$ **不是** $e_2^{AB}$ 的重复计数 ✗✓）
- 【**✓(4) 饱和 ＝ square（唐先生 §6 成立 ✓）**】$q_{ab}=2\iff$ 两中点皆 $\in U^c$ ✓（＝承担一个完整 4-cycle ✓）
- 【**⚠️(5) 诚实判定：$n_2$ 无局部上界（✗✓）**】**原因 ✓✓**：若 $q_{ab}=2$，则两中点的**两色要求已被 $\{a,b\}$ 自动满足** ✓✓（中点 $\in A$：有 $B$-邻 $b$ ✓；$\in B$：有 $A$-邻 $a$ ✓；$\notin U$：两者兼有 ✓）⟹ **饱和情形不产生任何新禁配** ✗ ⟹ **局部禁配路线无法给出 $n_2\le F$** ✗✓（＝唐先生 §7 所设想的 $n_2\le F(|H|)$ **不可由局部构型得到** ✓）
- 【**★(6) 局部模型（✓ 说明饱和可规模化 ⚠️）**】$A\ni0$ ✓、$B\supseteq\{e_i\oplus e_j:1\le i<j\le9\}$（36 个 ✓）、$U^c\supseteq\{e_1,\dots,e_9\}$ ✓ ⟹ 每个 $(i,j)$ 给 $q_{ab}=2$ ✓ ⟹ $$\boxed{n_2\ \ge\ 36}$$ ✓；**规模核对**：$|A|+|B|=37=2s-119\Longrightarrow s=78$ ✓（$|H|=41$、$|U^c|=434$ ✓ 落在允许区间 ✓）；**⚠️未检**：全局完成性 ✗（434 个外部点覆盖、$|C|=119$ 与 $H$ 相容 ✓ 未验 ✓）⟹ 本模型只证"局部禁配不存在" ✗，**不**证 119-cover 存在 ✗（V290 ✓）
- 【**状态 ✓**】已确立：① 最锐精确条件；② 约束只落 $U^c$；③ $q_{ab}$ 恒等式；④ 饱和＝square＋自足 ✓。已**否证**：局部禁配 $\Rightarrow n_2$ 上界 ✗✓。仍开：全局相容性、$n_2$ 的**全局**上界（须非局部输入）、一般 $s$ 的"存在→计数"升级 ⚠️
- 【**边界 ✓**】零程序计算 ✓（仅整数/逻辑核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗（照 23:54 令 ✓）；不声称 119 已排除 ✗；不声称 §5 构型可全局完成 ✗；不声称 P1 成立 ✗（V290）
- 档：`docs/WITSAT-2026-09-28-sharp-exact-condition-qab-identity-and-saturation-has-no-local-bound.md`

**🧷 C-438（2026-09-28 11:0x · **ERRATUM：C-437 §0(3) 勘误 ＋ 两条新结论**）** ✓
- 【**✗勘误（自查、当日发出 ✓）**】C-437 §0(3) 所写 $\sum_{a\in A,b\in B}q_{ab}\ \ge\ |U^c|\ \ge\ 450$ **不成立** ✗✓。**出错点**：该步需"每个 $x\in U^c$ 同时有 $A$-邻与 $B$-邻" ✗；**实际只对无 $H$-邻的点成立** ✓✓（$x\in U^c$ 且有 heavy 邻 ⟹ 两色要求可由**同一个** $h\in H$ 满足 ⟹ 可完全无 $A$-邻或无 $B$-邻 ⟹ 对 $q_{ab}$ 零贡献 ✗）
- 【**✓✓正确形式**】$$\sum_{a\in A,\,b\in B}q_{ab}\ \ge\ \big|X_L\big|,\qquad X_L:=U^c\cap D=\{x\notin U:\ N(x)\cap H=\varnothing\}$$ ✓✓（**恒等式本身不受影响** ✓：$\sum q_{ab}=\sum_{x\in U^c}|N(x)\cap A|\cdot|N(x)\cap B|$ ✓ 纯计数 ✓）
- 【**★新必要条件 1（✓✓）**】$x\in X_L\Longrightarrow|N(x)\cap A|\ge1\wedge|N(x)\cap B|\ge1$ ⟹ $$\boxed{|X_L|\ \le\ 72\min(|A|,|B|)}$$ ✓✓（每个距离-2 对承载 $\le2$ 个 $X_L$-点 ✓，而 $A$-$B$ 距离-2 对 $\le36\min(|A|,|B|)$ ✓）
- 【**★新必要条件 2（✓✓）**】$|X_L|\ \ge\ (512-s)-9|H|=\boxed{\max(0,8s-559)}$ ✓✓（重容量 ✓）
- 【**组合核对 ✓**】$8s-559\le36(2s-119)\iff s\ge58.2$ ✓ **平凡** ⟹ **修正后链条无矛盾** ✓（与 C-436 §9 一致 ✓）
- 【**★★新结论 3（局部模型不可完成 —— ⚠️升级为\ \textbf{定理}）**】C-437 §5 构型（$s=78,|A|=1,|B|=36,|U^c|=434$）⟹ $9|C_0|=9(41+1)=378<434=|U^c|$ ⟹ **违反 $U^c\subseteq N(C_0)$** ✗✗ ⟹ $$\boxed{\text{该局部模型不可全局完成}}$$ ✓✓ ⟹ **饱和事件的局部可构造性 ⟹ 不蕴含全局可行性**；**局部 vs 全局的真实缺口被显式量化** ✓✓
- 【**★二择（✓✓ 与 C-436 §6 一致）**】① $U^c\subseteq N(H)\Longrightarrow s\le69$ **且** $\exists\ell\in L:N(\ell)\cap H=\varnothing$（否则 $H$ 成 cover $\Rightarrow|H|\ge62\Rightarrow s\le57$ 矛盾 ✗）；② 否则 $X_L\ne\varnothing$ ✓
- 【**教训（已入档 ✓）**】上一步漏掉"存在 heavy 邻点"这一**替代路径** ✗ ⟹ **凡"每点 $\ge1$"型断言，须先列出该点的\ \textbf{全部}满足路径** ✓✓（同型失误本线已多次 ✓）
- 【**影响范围 ✓**】受影响：仅 C-437 §0(3) 该步 ✗（registry 已加勘误指针 ✓）；**不受影响**：C-437 的精确条件／修正／饱和自足／局部模型 ✓；**C-437 的"$n_2$ 无局部上界"结论仍成立** ✓（该论证只用局部结构 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；本档须与 C-437 同引 ✓；不声称 P1 成立 ✗（V290）
- 档：`docs/ERRATUM-2026-09-28-WITSAT-qab-bound-correction.md`

**🧮 C-439（2026-09-28 11:1x · **WITCAP：42/77 分支容量杀死条件（分支级 NO-GO）＋ 去特化等价性**）** ✓
- 【**✓(1) 链条在前提下逐位成立（本档核验 ✓）**】设 $|C_0|=42,|C_1|=77$ ⟹ $|H|=119-s$、$|A|=s-77$、$|B|=s-42$ ✓；则 $$|X_L|\ \ge\ (512-s)-9|H|=8s-559\ \le\ 9|A|=9s-693\ \Longrightarrow\ \boxed{s\ge134}$$ ✓（逐位核对：$s{=}77,100,119$ 皆越界 ✗；$s{=}134$ 恰好 $513\le513$ ✓）；配合 $s\le|C_0|+|C_1|=119$ ⟹ **矛盾** ✓✓
- 【**✗(2) 但前提来源 ＝ 我方\ \textbf{已死}分支（必标 ✓✓）**】$|C_0|=42,|C_1|=77$ **不是 119-cover 的一般事实** ✗✓：该组数字出自 **C-437 §5 的局部最小模型**（$A\ni0$、$|B|=36$、$|H|=41$ ✓），而该模型已在 **C-438 §3 被证不可全局完成** ✗✓ ⟹ 本链条是**分支内**的矛盾 ⟹ **重证该分支死亡 ✓，但不给 119 问题的一般 NO-GO** ✗✓
- 【**★★(3) 去特化（本档核心 ✓✓）**】不设 $|C_0|=42$、保留 $|A|=|C_0|-(119-s)$ ⟹ $$8s-559\le9|A|\iff \boxed{9|C_0|+s\ge512}\iff\boxed{|U^c|\le9|C_0|}$$ ✓✓（与 $U^c\subseteq N(C_0)$ 的**度数界同一式** ✓）⟹ 因 $s\le119$：$9|C_0|\ge393$ ⟹ $\boxed{|C_0|\ge44}$ ✓✓ ＝ **C-435 的 $a\ge44$（逐字同一界）** ✗✓
- 【**⚠️(4) 强度判定（诚实 ✓）**】本回合**不产生新界** ✗✓（＝C-435 的 $44$）；但给出：① 该分支的**独立重导** ✓；② $|U^c|\le9|C_0|$ 这一**去特化形式**比 $a\ge44$ **更直白** ✓（"外部点必须全部被 $C_0$ 的 9-邻接吃下" ✓）
- 【**★(5) 登记（照唐先生 §8 ✓）**】$$\boxed{\text{42/77 分支：GLOBAL CAPACITY NO-GO}}$$ ✓（**等效于 C-435 $a\ge44$** ✓）；**不得升级**为整个 119 问题的 NO-GO ✗✓；**方法价值**：首次在**分支层面**把"重亏空＋轻侧容量"接成闭环 ✓，且**不需要 $q_{ab}$／$e_2^{AB}$／square／$n_2$／$B$** ✓✓（比 $q_{ab}$ 路线简洁 ✓）
- 【**★(6) 一般 kill 需要什么（登记 ⚠️）**】一般情形 $8s-559\le9|A|$ **不矛盾**（$|A|$ 随 $s$ 增长 ✓）；仅知 $|A|\le2s-119\Longrightarrow-47\le2s$ **平凡** ✗✓（与唐先生 §9 一致 ✓）；$|U^c|\le9|C_0|$ 的**强化版恰是** $\mathrm{cov}_9(|C_0|)\ge|U^c|$ ✓✓ ＝ **C-435 §0(5) 的 $\mathrm{cov}_9$ 闸门** ⟹ **本回合路线汇入已知闸门** ✓（登记未做 ✓）
- 【**阈值表 ✓**】$|C_0|=42\Rightarrow s\ge134$ ✓；$44\Rightarrow s\ge116$ ✓；$50\Rightarrow s\ge62$ ✓；$60\Rightarrow s\ge-28$（空 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称获得新界 ✗✓；不声称 42/77 为普适分支 ✗；不声称 119 已排除 ✗（V290）
- 档：`docs/WITCAP-2026-09-28-branch-42-77-capacity-no-go-and-despecialization-equivalence.md`

**📐 C-440（2026-09-28 11:2x · **WITGATE：容量闸门的精确形式（交界点 $393/8$、$\mathrm{min\_excess}_9$ 重述、$s\le61$ 为空之更正）**）** ✓
- 【**✓(1) 参数化形式与表复核通过**】$$\boxed{s\ \ge\ 512-9a}\ (a:=|C_0|✓)$$ ✓ 逐位：$a{=}42\Rightarrow134$｜$43\Rightarrow125$｜$44\Rightarrow116$｜$45\Rightarrow107$｜$50\Rightarrow62$｜$51\Rightarrow53$｜$56\Rightarrow8$｜$57\Rightarrow-1$（自动 ✓）
- 【**★★(2) 交界点的精确来源（新 ✓✓）**】第二条约束 $H\subseteq C_0\Longrightarrow|H|=119-s\le a\Longrightarrow\boxed{s\ge119-a}$ ✓（此前只用于 $|A|\ge0$，**从未与容量并列** ✗）；交界 $512-9a=119-a\iff393=8a\iff\boxed{a=393/8=49.125}$ ✓✓ ⟹ $$\boxed{a\le49\ \text{容量主导};\quad a\ge50\ \text{由 }H\subseteq C_0\ \text{主导}\ (a{=}50:69>62✓)}$$ ✓✓ ＝ **唐先生"转折点在 50"的精确原因** ✓✓；容量闸门**有效作用域 ＝ $a\le49$** ✓
- 【**★★(3) 闸门的精确重述（新 ✓✓）**】$$\mathrm{cov}_9(a)\ge512-s\iff\boxed{9a-\mathrm{cov}_9(a)\ \le\ 9a+s-512}\iff\boxed{\text{「}C_0\ \text{的强制重叠损失}\le\text{滑动余量」}}$$ ✓✓；等价形式 $\boxed{s\ \ge\ \mathrm{min\_excess}_9(a):=512-\mathrm{cov}_9(a)}$ ✓✓（＝ **C-435 §0(5) 的 $\mathrm{cov}_9$ 闸门 ＝ 同一物** ✓）
- 【**★(4) 致密度事实（新 ✓）**】$\mathrm{cov}_9(m)=9m\iff m\le A(9,3)=40$ ✓✓（最小距离 $\ge3$ 集合无重叠 ⟹ **度数界在此紧**）；$m\ge41\Longrightarrow\mathrm{cov}_9(m)<9m\ \wedge\ \mathrm{min\_excess}_9(m)>512-9m$ ✓✓ ⟹ **容量界不再是紧的**，闸门自 $a\ge41$ 起才有"额外牙齿" ✓
- 【**✗✗(5) 更正：$s\le61$ 分支为空** ✓✓】$U$ 是 9-cover（C-435 §0(2) ✓）$\Longrightarrow s\ge K(9,1)=62$ **恒成立** ⟹ 唐先生"若已有独立的 $s\le61$"**该前提不存在** ✗；故"切掉 $|C_0|\le50$"**不再需要**（空分支 ✓）；**但方法论要点仍成立** ✓✓：$a\le50$ 区域由容量切掉 ⟹ 一般 NO-GO 只剩 **$a\ge51$ 侧的 $\mathrm{cov}_9$ 精确形状** ⚠️
- 【**★★(6) 完整 NO-GO 路线（登记 ⚠️，不需新机制）**】求 $\mathrm{min\_excess}_9(a)$（$a\in[44,59]$）；若 $\exists a:\ \mathrm{min\_excess}_9(a)>119\Longrightarrow$ 该 $a$ 不可行 ✓；若 $[44,59]$ 全排除 ⟹ 矛盾（因 $|C_0|,|C_1|\ge44$ 且和为 119 迫使 $|C_0|\in[44,59]$ ✓✓）—— **只用**「$U$ cover $\Rightarrow s\ge62$」＋ 9 维极值函数 ✓✓；**依赖** $\mathrm{min\_excess}_9$ 的值/强下界 ✗（文献/计算 ⚠️）
- 【**★(7) 档案接口 ✓**】① MCOVER／OBREVERSE（Östergård–Blass 子空间＋LP ✓）＝本类极值函数的标准工具 ✓；② DLP1A/1B（Delsarte LP／SDP ✓）＝$K(9,1)$ 侧锚点 ✓；③ C-435 的 $\mathrm{cov}_9$ 闸门 ＝ 此处 $s\ge\mathrm{min\_excess}_9$ ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 119 已排除 ✗；不声称 $\mathrm{min\_excess}_9$ 路线必成 ✗（V290）
- 档：`docs/WITGATE-2026-09-28-capacity-gate-crossover-49-125-and-min-excess-restatement.md`

**⚙️ C-441（2026-09-28 11:3x · **WITEFF：有效容量闸门 $L_A\le9a+s-512$ ＋ 双侧合并式修正 ＋ 边界刚性**）** ✓
- 【**✗必改一（重复陷阱，第 3 次）**】前提**不是** $U^c\subseteq N[A]$ ✗，而是 $X_L\subseteq N(A)$ ✓✓（$U^c\subseteq N(C_0)=N(H\cup A)$ ✗；仅当 $x$ 无 $H$-邻（$x\in X_L$）才有 $N(x)\cap C_0\subseteq A$ ✓）⟹ **规则化**：本线凡"每个外部点"型断言，**一律先问是否仅对 $X_L$ 成立** ✓✓（同源：C-437 §0(3)／C-438 §1 ✗）
- 【**✓(2) 精化恒等式（本档核验 ✓✓）**】$\sum_{x\in X_L}r_A(x)=|X_L|+T_A\le\sum_{x\notin A}r_A(x)=9|A|-2e(A)$ ⟹ $$\boxed{|X_L|\le9|A|-2e(A)-T_A}$$ ✓✓（① $X_L\cap A=\varnothing$ ✓；② $x\in X_L\Rightarrow r_A(x)\ge1$ ✓；③ $\sum_V r_A=9|A|$、$\sum_A r_A=2e(A)$ ✓）
- 【**★★(3) 精化闸门（本档核心 ✓✓）**】记 $L_A:=2e(A)+T_A$ ✓（"有效容量损失"）⟹ $$\boxed{L_A\ \le\ 9a+s-512}\quad\iff\quad\boxed{9a+s\ \ge\ 512+L_A}$$ ✓✓（＝C-439 闸门 ＋ **层 $A$ 的内部结构项** ✓✓）
- 【**✗必改二（双侧合并式算术）**】唐先生所写 $16s+L_A+L_B\le2189$ **不成立** ✗（用了 $a+b=119$ 代入，而界施于 $|A|,|B|$ ✓）；**正确**：$|A|+|B|=2s-119$ ⟹ $$\boxed{L_A+L_B\ \le\ 2s+47}$$ ✓✓；取 $L\ge2e$ 得 $$\boxed{e(A)+e(B)\ \le\ s+23}$$ ✓✓（**新且更紧**：唐先生版给 $s\le136.8$ 空转 ✗）
- 【**★★(5) 边界刚性（新 ✓✓）**】$L_A\le9a+s-512$ 在 $a{=}44,s_{\min}{=}116$ 处给 $L_A\le0$ ⟹ $$\boxed{e(A)=0\ \wedge\ T_A=0}$$ ✓✓（$|A|=41$ ✓）⟹ **首次出现对"层内部几何"的必要条件** ✓✓（比纯容量多一层结构 ✓；但**尚非矛盾** ✗：独立集可达 256 ✓）；最紧处 $a\in\{44,46,49\}$（$L_A\le0$ 型 ✓）
- 【**✓(6) $\rho_A$ 已核（唐先生 §7–§9 ✓）**】$|X_L|\le\sum_{a\in A}\rho_A(a)$、$\rho_A(a):=\#\{i:\exists j\ne i,\ a\oplus e_i\oplus e_j\in B\}\le9$ ✓（选择函数给单射 ✓）⟺ $\rho_A$ 是 $9|A|$ 的**方向级分解** ✓（与 (2) 的 $L_A$ 同族 ✓）
- 【**⚠️(7) 为何仍不自动矛盾（诚实）**】$L_A$ 可为 $0$ ✗（取 $A$ 独立集且每个 $x\in X_L$ 恰一 $A$-邻 ✓）；$e(A)>0$ **不被强制** ✗（$a{=}59,s{=}62\Rightarrow|A|{=}2$ ✓）；⟹ 精化的作用 ＝ 把闸门**参数化到层内部几何** ✓；**唯一活口** ＝ 证明某 $(a,s)$ 区域强制 $L_A$ 超余量 ✗（需 $e(A)$／$T_A$ 下界 —— **目前无** ⚠️）
- 【**与 C-440 的关系 ✓**】互补：C-440 的 $\mathrm{min\_excess}_9$ 闸门管 $|U^c|$ 可覆盖量（$a\le49$ 主导 ✓）；本文 $L_A$ 闸门管层内部几何 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $L_A$ 有正下界 ✗；不声称 119 已排除 ✗（V290）
- 档：`docs/WITEFF-2026-09-28-effective-capacity-gate-LA-bound-and-boundary-rigidity.md`

**🏁 C-442（2026-09-28 11:5x · **WITB45：边界刚性 ⟹ $|C_0|\ge45$（$a{=}44$ 全灭）；改进 C-435**）** ✓
- 【**✓(1) 核验通过（唐先生 §1–§8 ✓✓）**】度数恒等式 $9|A|=2e(A)+|E(A,H)|+|E(A,X_L)|+|E(A,R)|$ ✓✓（$X_L=U^c\setminus N(H)$ ✓、$R=N(H)\setminus(A\cup H)$ ✓）；$|E(A,X_L)|=|X_L|+T_A$ ✓ ⟹ $$\boxed{9|A|=L_A+|X_L|+\mathrm{leak}}\ \Longrightarrow\ \boxed{L_A+\mathrm{leak}\le\Delta_A}$$ ✓✓（＝C-441 之锐化 ✓）
- 【**✓边界刚性（$a{=}44,s{=}116$ ✓✓）**】$\Delta_A=0\Rightarrow L_A=\mathrm{leak}=0\Rightarrow e(A)=T_A=0$ ⟹ **$N(A)=X_L$** ✓、$|X_L|=369$ ✓、$|A|=41$ ✓、**$d(A)\ge3$** ✓✓（两点距离 2 ⟹ 共同邻点 $\in N(A)=X_L$ ⟹ $r_A\ge2$ 与 $T_A=0$ 矛盾 ✓）、**$N[A]$ 完美 packing（$|N[A]|=410$ ✓）、$N[A]\cap N[H]=\varnothing$** ✓✓
- 【**★(2) 积分性事实（新 ✓✓）**】$2D_2(A)=\sum_{y\in V}\binom{r_A(y)}2$ ⟹ $$\boxed{T_A\ne1}$$ ✓✓（$T_A=1$ 会使 $2D_2=1$ 非整数 ✗）
- 【**★★(3) 迭代判据（新 ✓✓）**】坏对 $\beta:=e(A)+D_2(A)$ ⟹ 移除 $\le\beta$ 点即得最小距离 $\ge3$ ⟹ $$\boxed{|A|\le A(9,3)+\beta}$$ ✓✓；配合 $2e+T_A+\mathrm{leak}\le\Delta_A$ 给出 $\mathrm{Bmax}(\Delta_A)$（$\Delta{=}0,1,2,3\Rightarrow0,0,1,3$ ✓）⟹ **排除判据**：$a+s-119>A(9,3)+\mathrm{Bmax}(\Delta_A)$ ⟹ 该 $(a,s)$ 不可能 ✓✓
- 【**★★★(4) $a=44$ 全灭 ⟹ $|C_0|,|C_1|\ge45$（新，改进 C-435 的 44 ✓✓✓）**】$|C_0|=44$ 四情形逐一：$s{=}116$（$|A|{=}41>40$ ✗）｜$117$（$42>40$ ✗）｜$118$（$43>41$ ✗）｜$119$（$44>43$ ✗）⟹ **全部矛盾** ⟹ $|C_0|\ne44$ ⟹ **与 C-435 的 $a\ge44$ 合得 $|C_0|,|C_1|\ge45$** ✓✓✓
- 【**★★$A(9,3)=40$ 来源核实（承重事实 ✓✓）**】Brouwer「Table of general binary codes」（`aeb.win.tue.nl/codes/binary-1.html` ✓ HTTP 200 ✓）表中 $n{=}10,d{=}4$ 取值 **40** ✓，经表内恒等式 $A_2(n{-}1,2e{-}1)=A_2(n,2e)$ ⟹ $A(9,3)=40$ ✓✓；**单一数值（非区间）⟹ 已定精确值** ✓；旁证 $n{=}11,d{=}4{:}72$、$n{=}12,d{=}4{:}144$ 与 Östergård–Baicheva–Kolev 1999 一致 ✓
- 【**★(5) 迭代框架与下一靶（⚠️ 登记）**】规律 $\Delta_A=(|A|-40)+(8a-353)$ ✓ ⟹ **仅 $a=44$ 裕量为负**（$-1$ ✓）——这解释了为何只有它被此机制杀死 ✓；$a=45$（$s\ge107$、$|A|\ge33$、$\mathrm{Bmax}(12)=6\Rightarrow|A|\le46$ ✓）**不矛盾** ✗ ⟹ 需新论证 ✓（登记未做 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅整数/有限情形核对 ✓＋一处文献取证 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 119 已排除 ✗（V290）
- 档：`docs/WITB45-2026-09-28-boundary-rigidity-kills-a44-and-yields-C0-ge-45.md`

**🎯 C-443（2026-09-28 12:0x · **WITRMAX：$a=45$ 的 $t$-参数化 ＋ $r_{\max}$ 三分类（三处因子 2 修正；Case I＝硬核）**）** ✓
- 【**✓(1) $t$-参数化核验（唐先生 §1 ✓）**】$a=45$：$|A|=s-74$ ✓；$t:=s-107=\Delta_A=9a+s-512$ ✓；$s\in[107,119]\Rightarrow t\in[0,12]$ ✓；预算 $L_A+\mathrm{leak}\le t$ ✓；判据 $|A|=33+t\le40+\beta\Rightarrow\boxed{\beta\ge t-7}$ ✓✓；**战场确为 $t\ge8$** ✓✓（$t\le7$：$|A|\le40$ 自动 ✓ — 唐先生表逐位无误 ✓）
- 【**✗✗(2) 三处因子 2 修正（必标 ✓）**】核心恒等式 $2D_2(A)=\sum_{y\in V}\binom{r_y}2$ ✓（唐先生 §7 写对 ✓）；**①** §5 的 $D_2\ge T_A$ **不对** ✗ ⟹ 应为 $$\boxed{D_2\ge\tfrac12T_A}$$ ✓✓；**②** §6 表给的是 $\sum\binom{r_y}2$ 而非 $D_2$ ✗ ⟹ $T_A{=}2,3,4\Rightarrow\boxed{D_2\le1,3,5}$ ✓✓（非 $3,6,10$ ✗）；**③** §9 之"桥"缺 $1/2$ ✗ ⟹ $$\boxed{\beta=\tfrac12L_A+\tfrac12\sum_{X_L}\tfrac{(r_y-1)(r_y-2)}2+\tfrac12\sum_{V\setminus X_L}\binom{r_y}2}\ \Longrightarrow\ \boxed{\beta\ge\tfrac12L_A}$$ ✓✓
- 【**✓✓(3) 三分类精确内容（唐先生 §12 ✓）**】**Case I**（$r_{\max}{=}1$）：$T_A{=}0\Rightarrow L_A{=}2e$ ✓，$\beta=e+\tfrac12\sum_{V\setminus X_L}\binom{r_y}2$ ✓；**Case II**（$r_{\max}{=}2$）：$\sum_{X_L}\binom{r_y}2=T_A$ ⟹ $\beta=e+\tfrac12(T_A+\sum_{V\setminus X_L}\binom{r_y}2)$ ✓（唐先生 §12 之 $\beta=L_A-e$ 需 $D_2=T_A$ ✗，仅当无外部贡献 ✓）；**Case III**（$r_{\max}\ge3$）：局部三角结构 ✓✓（§11 已核：$\{e_i,e_j,e_k\}$ 两两距离 2 ✓，三对共同邻点 $(0,e_i{\oplus}e_j),(0,e_i{\oplus}e_k),(0,e_j{\oplus}e_k)$ ✓）⟹ $$\boxed{D_2\ge3}$$ ✓✓（$2D_2\ge\binom32+3=6$ ✓）
- 【**★★(4) 硬核判定（本档 ✓✓）**】Case I 的 $\beta=\tfrac12L_A$ 是同一预算下的**最小值** ✗✓ ⟹ **排除 $a=45$ 必须\textbf{结构性排除 Case I}** ✓✓；**预算相容性核对**：$2e\le L_A\le t\Rightarrow e\le t/2$ ⟹ $t{=}8$：需 $e\ge1\le4$ ✓；$t{=}12$：需 $e\ge5\le6$ ✓ ⟹ **预算不排除 Case I** ✗✓
- 【**★★(5) 命题式二分（新 ✓✓）**】$t\ge8\Longrightarrow$ 或 $e(A)+\tfrac12\sum_{V\setminus X_L}\binom{r_y}2\ge t-7$（Case I ✓），或 $r_{\max}\ge2$ ✓；**锐化**：Case I 时 $T_A=0\Rightarrow$ 每个 $x\in X_L$ 恰有一个 $A$-邻 ⟹ $X_L$ 与 $A$ **近似一一对应** ＝ 最容易满足判据的退化结构 ✓✓
- 【**⚠️(6) 状态**】已确立：$t$-参数化／三修正／三分类内容／$D_2\ge\tfrac12T_A$ 与 $\beta\ge\tfrac12L_A$／Case III 之 $D_2\ge3$／命题式二分 ✓；已否证："Case I 由预算排除" ✗、"$D_2\ge T_A$" ✗、"$D_2\le3,6,10$" ✗；**未确立**：$a=45$ 的排除、Case I 的结构性排除（须证 $T_A=0\Rightarrow|A|\le40$）、$r\ge3$ 局部相容性分类 ⚠️
- 【**★(7) 下一靶（登记）**】① 证 $T_A=0\ (\text{Case I})\Rightarrow|A|\le40$（可杀 $t\ge8$ 之 Case I ✓）；② 或分类 $r=3,4,\dots$ 的局部构型与互斥 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称 Case I 不可行 ✗（V290）
- 档：`docs/WITRMAX-2026-09-28-a45-t-parametrisation-rmax-trichotomy-and-case-I-hard-core.md`

**📦 C-444（2026-09-28 12:2x · **WITCAR：Case I 载体修正（$V\setminus X_L=U\cup N(H)$）＋ 否证 $t{=}12$ 之杀 ＋ 集中化修好**）** ✓
- 【**✓(1) §1–§2 成立（一处记号 ✓）**】$T_A=0\Rightarrow r_A\equiv1$ on $X_L$ ✓ $\Rightarrow|E(A,X_L)|=|X_L|$ ✓；$9|A|=2e+|E(A,H)|+|X_L|+|E(A,R)|$ ✓（唐先生写 $9a$ 应为 $\boxed{9|A|}$ ✗ 记号；仅 $t{=}12$ 时二者重合 ✓）$\Rightarrow 2e+\mathrm{leak}=9|A|-|X_L|\le t\Rightarrow\boxed{e(A)\le t/2}$ ✓✓；$\beta=e+\tfrac12\sum_{V\setminus X_L}\binom{r_A}2$ ✓✓
- 【**✗必改一（载体错位）**】唐先生 §3 的 $V\setminus X_L=N(H)$ **不对** ✗（系把 $X_L$ 误作 $V\setminus N(H)$ ✓）；**正确**：$$X_L:=U^c\setminus N(H)\Longrightarrow\boxed{V\setminus X_L=U\cup N(H)}$$ ✓✓ ⟹ 坏对见证可落在**整个 $U$（含全部 $B$，至多 75 点）** ⟹ §4 的 $2D_2=\sum_{N(H)}\binom{r_y}2$ ✗、§5 的"由至多 4 个 $H$-球承载" ✗；**正确**：$2D_2(A)=\sum_{y\in U\cup N(H)}\binom{r_A(y)}2$ ✓✓、§8 的 $M$ 应为 $U\cup N(H)$ ✓
- 【**✗✗必改二（结论级）**】**"$(a,s)=(45,119)$、$T_A=0$ 直接不可能" 不成立** ✗✗。**病根**：$H=\varnothing$ 时 $X_L=U^c$ **而非 $V$** ✗（唐先生 §10 写"此时 $X_L=V$" ✗）⟹ $T_A=0$ 只要求每个 $x\in U^c$ 恰一个 $A$-邻 ✓。**实际核对**：$t{=}12$：$|A|{=}45$、$|X_L|{=}512-119=\mathbf{393}\le9|A|=\mathbf{405}$ ✓ **可满足**；且 $2e(A)+|E(A,R)|=405-393=12=t$ ✓ 与预算相容 ✓ ⟹ **$t{=}12$ 的 Case I 未被关闭** ✗✓
- 【**★★(2) 集中化直觉可修好（新 ✓✓）**】载体虽**大**（$U\cup N(H)$ 可至 119 点 ✓），但其 **A-入射预算极小**：$$\boxed{\sum_{y\in V\setminus X_L}r_A(y)=2e(A)+\mathrm{leak}\ \le\ t\ \le\ 12}\ \Longrightarrow\ \boxed{D_2(A)\le\tfrac12\binom t2}$$ ✓✓ ⟹ $\beta\le\tfrac t2+\tfrac12\binom t2$（$t{=}8{\Rightarrow}18$、$10{\Rightarrow}27$、$12{\Rightarrow}39$）而所需仅 $\beta\ge t-7\le5$ ⟹ $$\boxed{\text{Case I 的计数层对全部 }t\in[8,12]\ \text{存活}}$$ ✗✓（**必须结构论证** ✓）
- 【**★(3) 第 4 次同型陷阱（制度 ✓✓）**】$X_L$ 约定再次被误用 ✗（首次 C-437 §0(3)、二次 C-438 §1、三次 C-441 §0(1)、**本档第四次**）⟹ **规则强化**：凡涉及 $X_L/V\setminus X_L$ 的等式，**一律先写出 $V\setminus X_L=U\cup N(H)$ 再继续** ✓✓（已同步 TOOLS.md ✓）
- 【**⚠️(4) 下一靶（登记）**】① 在**载体入射预算 $\le t$** 约束下求 $A$ 的可行性（＝带预算的码问题 ✓）；② 或攻 $A(9,3)=40$ 的**带缺陷版**：$|A|=41+t'$ 且允许 $\beta$ 个坏对时是否可行 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITCAR-2026-09-28-case-I-carrier-correction-and-t12-refutation.md`

**🔬 C-445（2026-09-28 12:4x · **WITSH：singleton-$H$ 分离引理（新 ✓✓）＋ 载体第 5 次 ＋ §12 重犯**）** ✓
- 【**★★(1) singleton-$H$ 分离引理（新 ✓✓，唐先生 §2 内核之严格化）**】设 $h\in H$、$\{u,v\}\subseteq A$、$d(u,v)=2$ ⟹ **两个共同邻点不可能同时落在 $N(h)$** ✓✓，即每对距离-2 至少一个见证 $\in U\cup(N(H)\setminus N(h))$ ✓✓。**证明**：平移 $h\mapsto0$ ✓；$u=z\oplus e_i,\ v=z\oplus e_j$ ⟹ 共同邻点 $=\{z,\ z\oplus e_i\oplus e_j\}$ ✓；若二者皆 weight-1（$\in N(0)$）则 $z=e_p$、$z\oplus e_i\oplus e_j=e_q$，$e_p\oplus e_q=e_i\oplus e_j\Rightarrow\{p,q\}=\{i,j\}$ ⟹ $\{u,v\}=\{0,e_i\oplus e_j\}\ni0=h\notin A$ ✗ 矛盾 ✓✓
- 【**（穷举核验 ✓✓）**】$Q_9$ 全部 $(z,i,j)$ 上验证：共同邻点 $\equiv\{z,z\oplus e_i\oplus e_j\}$ ✓；"二者皆 weight-1" 之 **72 例**中 $u,v$ 皆非 0 者 ＝ **0** ⟹ **零反例** ✓✓
- 【**✗✗(2) 载体错误第 5 次复发**】唐先生 §1 的 $X_L=V\setminus N(H)$ ✗、§2 的"共同邻点必属于 $N(H)$" ✗ ⟹ §1 的"$\forall y\notin N(H):r_A(y)\le1$" ✗（仅对 $y\in X_L$ 成立 ✓）；**§2 的 $D_2(A)=0$ 未被证出** ✗（正确载体：$V\setminus X_L=U\cup N(H)$ ✓，C-444 ✓）
- 【**✗✗(3) §12 重犯 C-444 §0(3) 已否证之断言**】"(45,119), $T_A{=}0$ 不可能" ✗ —— **一行否证 ✓✓**：$$\sum_{y\in V}r_A(y)=\sum_{a\in A}|N(a)|=9|A|=\mathbf{405}\ \text{（恒真 ✓✓）}$$ ⟹ 唐先生 §12 的 "$\sum_y r_A(y)=512$" 对任何 $|A|=45$ 都不可能 ✗（$512\ne405$ ✓）；$T_A=0$ 只约束 $X_L$ 上的 $r_A$ ✓
- 【**✓(4) 条件链（在 $D_2=0$ 前提下）**】$|A|-\tau(G_1(A))\le A(9,3)=40\Rightarrow\tau\ge4\Rightarrow e(A)\ge4$ ✓；与 $e\le5$ 合 ⟹ $$\boxed{e(A)\in\{4,5\}}$$ ✓✓；$e{=}4\Rightarrow\mathrm{leak}\le3$、$e{=}5\Rightarrow\mathrm{leak}\le1$ ✓；$e{=}4\Rightarrow A=C\sqcup T$、$|C|=40$、$d(C)\ge3$（**极值 $(9,3)$ 码核心** ✓✓）
- 【**✓(5) §9 纤维结构（正确且有用 ✓✓）**】$T_A=0\Rightarrow f:X_L\to A$ 良定义、纤维 $F_a$、$|F_a|\le9$、$\sum_a|F_a|=|X_L|$ ✓；且 $d(a,b)=2\Rightarrow F_a\cap N(b)=\varnothing$ ✓✓（否则该点 $r_A\ge2$ 与 $T_A=0$ 矛盾 ✓）
- 【**⚠️(6) 无杀（诚实）**】取消 $D_2=0$ 后 $t{=}11$ 只需 $e+D_2\ge4\wedge2e+\mathrm{leak}\le11$ ⟹ 可行例 $(4,0)$、$(0,4)$ ⟹ **无矛盾** ✗；**真正缺口** ＝ $|H|=1$ 时 $D_2=0$ 是否成立 ⚠️
- 【**★(7) 下一靶**】① 攻 $|H|{=}1\Rightarrow D_2=0$（或用分离引理做"每对至少耗一个 $U\setminus N(h)$ 见证"的定量版 ✓）；② 条件式的极值延拓分类（40-码 ＋ 4 点 ＋ singleton $H$ ✓）；③ $A(9,3)=40$ 极值码分类**不在档案** ✗（须文献 ✓）
- 【**条件旗标 ✓**】§0(4)、§1 的 §3–§7、§13–§14 均为**条件式**（在 $D_2=0$ 下）⟹ 不得脱旗引用 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ＋ 引理穷举验证 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称 $D_2=0$ 成立或失败 ✗（V290）
- 档：`docs/WITSH-2026-09-28-singleton-H-separation-lemma-and-the-fifth-carrier-slip.md`

**📐 C-446（2026-09-28 13:0x · **WITSAT2：饱和仅 $t{=}12$（$9a/9|A|$ 第 2 次滑落）＋ $\#\{d_U{=}0\}\ge33$（全 $t$ ✓✓）**）** ✓
- 【**✗✗必改（第 2 次同型）**】唐先生 §1 的 $\mathbf{405=|X_L|+S_A}$ **不对** ✗ —— 系 $9a$ 与 $9|A|$ 之滑落 ✗；**正确**：$9|A|=9(33+t)=297+9t$ ✓ ⟹ $$\boxed{S_A=297+9t-|X_L|\le t}$$ ✓✓（即 C-444 的 $S_A\le t$ 之重述 ✓）；$405=9a$ **仅 $t{=}12$** 时与 $9|A|$ 重合 ✓
- 【**✓✓(1) 饱和恰在 $t{=}12$ 成立（本档判定）**】$|X_L|\le|U^c|=405-t$ ✓ 与 $|X_L|\ge297+8t$ ✓ 同取等 $\iff9t=108\iff\boxed{t=12}$ ✓✓（$t\le11$ 时区间非退化：$t{=}11{:}[385,394]$ ✓）⟹ **仅 $t{=}12$**：$\boxed{|X_L|=|U^c|=393}$（故 $X_L=U^c$ ✓）、$\boxed{S_A=t=12}$（预算饱和 ✓✓）、$N(H)=\varnothing\subseteq U$ ✓（空真 ✓）
- 【**★★(2) 新结果 $\#\{a\in A:d_U(a)=0\}\ge|A|-t=\mathbf{33}$（对全部 $t\in[8,12]$ 成立 ✓✓）**】证明：$\sum_{a\in A}d_U(a)=\sum_{y\in U}r_A(y)\le S_A\le t$ ⟹ $\#\{d_U\ge1\}\le t$ ⟹ $\#\{d_U=0\}\ge33$ ✓✓ ⟹ **至少 33 个 $A$-点的全部 9 个邻点都在 $U^c$** ✓✓
- 【**✓(3) $t{=}12$ 格：唐先生 §6–§9、§12 全部成立（逐条核 ✓✓）**】① $r_A\equiv1$ on $U^c\Rightarrow N(a)\cap N(a')=\varnothing$（$a\ne a'\in A$）✓；② $2D_2=\sum_{y\in U}\binom{r_A(y)}2$、$\sum_U r_A=12$ ✓✓；③ 容量封顶 $t=9q+r\Rightarrow2D_2\le36q+\binom r2$ ⟹ $t{=}12\Rightarrow D_2\le\mathbf{19}$ ✓；④ $\boxed{2e(A)+e(A,B)=12}$ ✓✓；⑤ $\ge33$ 完整球两两不交 ⟹ $|\bigcup_{A_0}B_1(a)|=330\le393$ ✓（slack 63 ✓）⟹ **无矛盾** ✗
- 【**⚠️(4) 无杀（诚实）**】$\beta\le\lfloor t/2\rfloor+\tfrac12\binom t2$（$t{=}12{:}25$、$t{=}8{:}18$）而所需仅 $\beta\ge t-7$ ⟹ **全部 $t$ 仍可行** ✗✓（与 C-444 一致 ✓）
- 【**★(5) 记号对照（防第 3 次滑落 ✓✓）**】$t{=}8..12$：$9|A|=369,378,387,396,\mathbf{405}$；$|U^c|=397,396,395,394,393$；$|X_L|\ge361,369,377,385,\mathbf{393}$ ⟹ **规则**：$a=45$ 时一律写 $9|A|=297+9t$，$405=9a$ 仅 $t{=}12$ 重合 ✓
- 【**✓(6) 已否证**】"$405=|X_L|+S_A$"（全 $t$）✗；"饱和对全 $t$" ✗；"$t{=}12$ 直接不可能"（**第三次** ✗）
- 【**★(7) 下一靶（登记）**】① $\mathbf{33\ \text{完整球 packing}}＋\le t$ 污染点共存（唐先生 §13–§14 ✓）；② $t{=}12$ 之干净命题（去 $H$）：$|A|=45$、外部每点恰一 $A$-邻、$A$-外部入射 $=12$ ⟹ $|A|\le40$？✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称 $t{=}12$ 已关闭 ✗（V290）
- 档：`docs/WITSAT2-2026-09-28-saturation-only-at-t12-and-the-33-zero-U-degree-bound.md`

**🧩 C-447（2026-09-28 13:2x · **WITA0：两处假前提 ＋ $d(A_0)\ge3$ 结构（新 ✓✓）＋ wedge 闭包（新 ✓✓）**）** ✓
- 【**✗✗假前提一（$t{=}12$）**】"$A$ 是最小距离 $\ge3$ 的码 $\Rightarrow$ 球两两不交 $\Rightarrow|\bigcup_aB_1(a)|=450$" **不成立** ✗✗（$|A|=45>40=A(9,3)$ ⟹ $A$ 必有距离 $\le2$ 的对 ✓，正是 $e,D_2>0$ 之本意 ✓）⟹ "所有不等式取等" ✗ 与"精确分割 $393+45+12+62$" ✗ 均不成立；**正确**：$d\in\{1,2\}\Rightarrow|B_1(a)\cap B_1(a')|=\mathbf2$ ⟹ $|\bigcup_aB_1(a)|=450-2(A_1{+}A_2)+\text{三重修正}$ ✓；$|N(A)\cap U|\le12$ ✓（非 $=12$ ✗）、$|U\setminus(A\cup P)|\ge62$ ✓（非 $=62$ ✗）
- 【**✗✗假前提二（$|H|{=}1$）**】"$h,u,v\in C_0$ 且 $C_0$ 最小距离 $3$" **不成立** ✗✗（$A=C_0\setminus\{h\}$、$|A|=44>40$ ⟹ $C_0$ 含距离 $\le2$ 的对 ✗）⟹ 定位到 $S_2(h)$ **不成立** ✗（$d(h,u)\in\{1,2\}$ 皆可能 ✓）；**但** "$z\in N(h)$ 为中点 $\Rightarrow d(h,u),d(h,v)\le2$" ✓✓ 正确 ✓
- 【**✓✓(1) 修正后的锋利版（新）**】$A_0:=\{a\in A:d_U(a)=0\}$ ⟹ $$\boxed{d(A_0)\ge3}$$ ✓✓（**对全部 $t$ 成立**）：$d\le1\Rightarrow a'\in N(a)\subseteq U^c$ 而 $a'\in A\subseteq U$ 矛盾 ✗；$d{=}2\Rightarrow$ 共同邻点 $\in N(a)\subseteq U^c$ 且 $r_A\ge2\Rightarrow\notin X_L=U^c$ 矛盾 ✗ ⟹ **三推论**：① $A_0$ 球两两不交 ✓；② $|N[A_0]|=10|A_0|$ ✓；③ $\boxed{d(A_0,A_1)\ge3}$ ✓ ⟹ $|A_0|\in[33,40]$ ✓✓、$|A_1|\in[5,12]$ ✓、$\sum_{a\in A_1}d_U(a)=12$ ✓✓（全部 $U$-入射由 $A_1$ 承担 ✓）
- 【**✓✓(2) wedge 闭包（新，$|H|{=}1$）**】$\{i,j\},\{i,k\}\in E_h$（即 $e_i{\oplus}e_j,e_i{\oplus}e_k\in A\cap S_2(h)$）⟹ 中点 $=\{e_i,e_j{\oplus}e_k\}$ ✓；$e_i$ weight-1 $\in N(h)$ ✓、$e_j{\oplus}e_k$ 距 $h$ 为 2 $\Rightarrow\notin N(h)$ ✓、$r_A\ge2\Rightarrow\notin X_L$ ✓ ⟹ $$\boxed{e_j{\oplus}e_k\in U\setminus N(h),\ r_A\ge2}$$ ✓✓ ⟹ 每楔耗 $\ge2$ 预算 ⟹ $$\boxed{\#\{\text{被迫中点}\}\le\lfloor t/2\rfloor}$$ ✓✓（$t{=}11\Rightarrow\le5$ ✓）
- 【**✓(3) 其他正确项**】两点距离 2 $\iff$ $K_9$ 两边相邻 ✓✓；$|H|{=}1$ 载体与中点类型排除（引理 C-445 ＋ $T_A{=}0$）✓✓；$t{=}12$ 的 $A\leftrightarrow P\leftrightarrow W$ 与 $N(A)\cap W=\varnothing$ ✓✓
- 【**⚠️(4) 推测（非结果）**】唐先生提议之 "$D_2>0\Rightarrow2e(A)+\mathrm{leak}\ge12$" **未被推出** ✗（wedge 仅给 $\ge2$ ✓）⟹ 登记为**猜想** ✓
- 【**⚠️(5) 无杀**】全部 $t$ 仍可行 ✓；两处假前提之否证不带来新界 ✗（但 (1)(2) 为新结构资产 ✓✓）
- 【**★(6) 下一靶**】① $t{=}12$：$A_0$（33–40 点、球不交、$d(A_0,A_1)\ge3$）＋ $A_1$（$\le12$）＋ $P$（$\le12$）共存 ✓✓；② $|H|{=}1$：用 wedge 闭包 $\#\le5$ 与 $D_2\ge t-7-e$ 对撞 ✓；③ 猜想之证否／证成 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称猜想成立 ✗（V290）
- 档：`docs/WITA0-2026-09-28-two-false-premises-and-the-clean-centre-structure.md`

**🏆 C-448（2026-09-28 13:5x · **WITCODE：$t{=}12\Rightarrow e(A)=0$（新 ✓✓）＋ 判死 $A(9,3)$ 路线（$D_2\ge5$ 被强制）**）** ✓
- 【**✓✓(1) 新结果 $t{=}12\Rightarrow e(A)=0$（对全部 $q=|A_1|\in[0,12]$ 成立）**】链条：① $d(A_0)\ge3\Rightarrow e(A_0)=0$（C-447 ✓）；② $d(A_0,A_1)\ge3$ ✓（**本档更简洁证明**：$d{=}1\Rightarrow b\in N(a)\subseteq U^c$ 而 $b\in A\subseteq U$ ✗；$d{=}2\Rightarrow$ 共同邻点 $r_A\ge2\Rightarrow\notin X_L{=}U^c\Rightarrow\in U$，**但** $y\sim a$ 且 $a\in A_0\Rightarrow y\in N(a)\subseteq U^c$ ✗ —— **不需** $|A_1|{=}12$ ✓✓）；③ $$\boxed{U^c=N(A_0)\ \dot\cup\ (N(A_1)\cap U^c)}$$ ✓✓；④ 集合大小 $|N(A_1)\cap U^c|=393-9|A_0|=9q-12$ ✓✓；⑤ 入射计数 $E(A_1,U^c)=9q-2e(A_1)-12$ ✓；⑥ 比较得 $$\boxed{e(A_1)=0}$$ ✓✓ ⟹ **$e(A)=0$** ✓✓；且 $N(A_1)\cap U^c$ 每点恰一个 $A_1$-邻 ✓
- 【**✓✓(2) 配套新结果**】① $$\boxed{N(P)\cap A_0=\varnothing}$$ ✓✓（$P:=N(A_1)\cap U$；$p\sim a_0,a_1\Rightarrow d\le2$ 违 ②）；② $\boxed{\mathrm{leak}=|E(A,B)|=t=12}$ ✓✓（$2e+\mathrm{leak}=t$ 且 $e=0$）；③ $A_1\subseteq R:=Q_9\setminus(A_0\cup N(A_0))$、$|R|=512-330=\mathbf{182}$ ✓✓
- 【**✗✗(3) 最后一步不成立 —— 本档判死该路线**】"$e(A)=0\Rightarrow d(A)\ge3\Rightarrow45\le A(9,3)=40\Rightarrow\bot$" **无效** ✗✗：$e(A)=0$ **只排除距离-1 对** ✗；$A_1$ 内部距离-2 对未被排除 ✓；而 $\beta=e+D_2=D_2\ge t-7=5$ ✓✓ ⟹ $$\boxed{D_2(A)\ge5>0\ \text{被强制}}\Longrightarrow\boxed{A\ \text{可证不是最小距离}\ge3}$$ ⟹ **$A(9,3)$ 路线封闭** ✗✓（**必须与 $e(A)=0$ 同时引用**，否则误得矛盾 ✓✓）
- 【**✓(4) $D_2$ 窗口锐化（新）**】所有 $A$ 的距离-2 对之两共同邻点皆 $\in P$ ✓（$\notin X_L{=}U^c$ ✓、$\notin A$ 因 $e(A){=}0$ ✓、$\notin W$ 因 $W\cap N(A){=}\varnothing$ ✓）⟹ $2D_2=\sum_{p\in P}\binom{r_A(p)}2$ ✓、$\sum_P r_A=12$ ✓、$r_A(p)\le9$ ⟹ $$\boxed{D_2\le18}$$ ✓✓（锐于 C-446 的 19 ✓）⟹ $$\boxed{D_2\in[5,18]}$$ ✓；**杀 $t{=}12$ 只需 $D_2\le4$** ✗
- 【**✓(5) 其他正确项**】§6–§7 的 $U^c$ 二分割与 $E(P,A_0)=0$ ✓✓；§8–§9 的 $e(A_1)=0$ 推导 ✓✓；§12 的 $A_1$ 内距离-2 对见证在 $P$ ✓
- 【**✗(6) 已否证**】"球不交／450"（二次 ✗）；"$|P|=12$" ✗（仅 $\le12$ ✓）；"$e(A)=0\Rightarrow$ 码矛盾" ✗✓；"$A_1$ 内距离-2 对另一中点必在 $U^c$" ✗（$t{=}12$ 时 $X_L{=}U^c$ 已饱和 ⟹ 两中点皆在 $P$ ✓）
- 【**★(7) 下一靶**】① 证 $D_2\le4$（等价排除"六个 $r{=}2$ 的 $P$-点"最小缺陷构型 ✓）；② $A_1\subseteq R\ (q\le12,\ |R|{=}182)$ 局部分类 ✓；③ 用 $N(P)\cap A_0=\varnothing$ 做二部禁邻计数 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称 $t{=}12$ 已关闭 ✗（V290）
- 档：`docs/WITCODE-2026-09-28-zero-internal-edges-at-t12-and-the-closure-of-the-code-bound-route.md`

**💎 C-449（2026-09-28 14:2x · **WITPROF：$r_{\max}{=}3$ 被逼出 ＋ $D_2\in\{5,6\}$ 仅两 profile ＋ P-3 被推翻**）** ✓
- 【**✗必改（因子 2，同型第 3 次）**】唐先生 §1 的 $D_2=\sum_P\binom{r_p}2$ **不对** ✗；**正确** $$2D_2=\sum_{p\in P}\binom{r_p}2=\sum_j\binom j2n_j$$ ✓✓（距离-2 对有**恰好 2 个**共同邻点 ✓）
- 【**✗✗§2 例子不可能（纠正其"纠正"）**】型 $(2,2,2,2,2,1,1)$：$\sum r=12$ ✓ 但 $\sum\binom r2=\mathbf5$ 奇 ⟹ $2D_2=5$ ⟹ $D_2=2.5$ **非整数** ✗✗ ⟹ **该型不存在**；故 $D_2=5$ **必须出现 $r\ge3$** ✓✓（与其 §2 结论相反 ✓）；其"$\sum r=12$ 不能得等价性"之**方法提醒正确** ✓✓
- 【**★★★(1) $r_{\max}\le3$（新）**】设 $r(p)=k$、支撑 $S$；则 $\{e_i:i\in S\}\subseteq A_1$ 两两距离 2 ✓，且每对 $i<j$ 的第二共同邻点 $e_i\oplus e_j\in P$ 且 $r\ge2$ ✓✓ ⟹ $$\sum_{p'\in P}r(p')\ \ge\ k+2\binom k2=k^2$$ ✓✓（被迫点与 $p$ 及 $k$ 个一阶点**互异** ✓）⟹ $k^2\le12$ ⟹ $$\boxed{k\le3}$$ ✓
- 【**★★★(2) $r_{\max}=3$ 被逼出 ⟹ P-3 被推翻（核心）**】若 $r_{\max}\le2$：$\sum\binom r2=n_2$、$\sum r=2n_2+n_1=12$ ⟹ $n_2=2D_2$ ⟹ $$n_1=12-4D_2\ge0\Longrightarrow\boxed{D_2\le3}$$ ✓✓ ⟹ 与强制的 $D_2\ge5$ **直接矛盾** ✗✗ ⟹ $$\boxed{\exists p:r_A(p)\ge3}$$ ✓✓ ⟹ 与 (1) 合：$$\boxed{r_{\max}=3}$$ ✓✓✓ ⟹ **Lemma P-3 不可证且为假** ✗✗；**§6 的 Case II（$r_{\max}{=}2$）为空** ✗；**Case I 是唯一分支** ✓✓
- 【**★★★(3) $D_2\in\{5,6\}$，恰两 profile（穷举核验 ✓）**】由 $k\le3$：$\sum\binom r2=3n_3+n_2\le12$（极大 $n_3{=}4$ ✓）⟹ $$\boxed{D_2\le6}$$ ✓✓ ⟹ $$\boxed{D_2\in\{5,6\}}$$ ✓✓✓；且 $$\boxed{D_2=5\iff\text{profile }3^32^11^1},\quad \boxed{D_2=6\iff\text{profile }3^4}$$ ✓✓（搜索空间由 $[5,18]$ 暴缩为**两种** ✓✓）
- 【**★★(4) 第二共同邻点封闭条件（新）**】$\forall p\in P,\ \forall\{i,j\}\subseteq\operatorname{supp}(p)$：$$\boxed{p\oplus e_i\oplus e_j\in P\ \text{且}\ r(p\oplus e_i\oplus e_j)\ge2}$$ ✓✓ ⟹ 每个 $r{=}3$ 点必生 3 个被迫点（各 $r\ge2$ ✓）；这是把 profile 与**几何**绑死的唯一新接口 ✓✓
- 【**✓(5) 其他正确项**】§3 的 $2D_2=\sum s^2+\sum s$ ✓；§7 的 $r\ge3\Rightarrow A_1$ 含距离-2 三角形 ✓✓（且现已**被逼出必存在** ✓）；$A_0$ 可消（$r_A(p)=r_{A_1}(p)$）✓✓
- 【**✗(6) 已否证**】P-3 ✗✗；Case II（$r_{\max}{=}2$）✗；型 $(2^5 1^2)$ ✗；$n_1=12-2D_2$ ✗（应为 $12-4D_2$ ✓）；$D_2=\sum_P\binom{r_p}2$ ✗
- 【**★(7) 下一靶**】① 攻 profile $3^4$（4 个 $r{=}3$ 点、12 对、12 个被迫点须落回 $P$ 的**封闭自洽** ✓）；② 攻 profile $3^32^11^1$；③ 用封闭条件把 profile 转成 $A_1$ 上的 $F_2^3$-型立方结构 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数与有限 profile 穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITPROF-2026-09-28-rmax-equals-3-forced-and-only-two-D2-profiles.md`

**🔷 C-450（2026-09-28 14:5x · **WITPLANE：$3^4\Rightarrow P$ 是二维仿射平面（新 ✓✓）；闭环不排除 $3^4$（显式局部模型 ✗）**）** ✓
- 【**✗✗系统性混淆（本档澄清）**】唐先生 §1 设 $S(p):=\operatorname{supp}(p)$（**坐标支撑**）且 $k=|S(p)|=r(p)$ **不对** ✗✗：$$r(p)=\big|\{i:p\oplus e_i\in A_1\}\big|\ \ \text{（\textbf{方向集} }D(p)\text{）}\ \ne\ \operatorname{supp}(p)=\{i:p_i=1\}$$ ✓ 二者**一般无关**；反例：$p=e_1{\oplus}\cdots{\oplus}e_5$（weight 5）而 $D(p)=\{7,8,9\}$ 完全可能 ✓ ⟹ §2 的"$|q|{=}k{-}2$"、§3–§5 的"weight-3 $\Rightarrow$ 三个单位向量入 $P$"、§4 的"2-交 3-一致族"、§6 的 (6)(7)、§8–§9 的型 A／型 B **全部不成立** ✗✗
- 【**✓✓(1) 纠正后的闭环更强（新）**】$p\in P$、$i\ne j\in D(p)$：$p\oplus e_i,p\oplus e_j\in A_1$ 皆与 $p$ 距离 1 ⟹ 共同邻点 $=\{p,\ p\oplus e_i\oplus e_j\}$ ⟹ $$\boxed{q:=p\oplus e_i\oplus e_j\in P,\ r(q)\ge2}$$ ✓✓；且 $e_i\oplus e_j$（$i<j$）互异 ⟹ **闭环点互异** ✓✓
- 【**★★(2) profile $3^4$ 的精确结构（新 ✓✓）**】每个 $p_a$ 的 $\binom32=3$ 个闭环点与 $p_a$ 合为 **4 点 = $P$** ⟹ $$\boxed{P=\{x,\ x\oplus u,\ x\oplus v,\ x\oplus(u\oplus v)\}}\ \big(u{=}e_i{\oplus}e_j,\ v{=}e_i{\oplus}e_k,\ u{\oplus}v{=}e_j{\oplus}e_k✓\big)$$ ⟹ $\{0,u,v,u\oplus v\}$ 对 XOR 封闭 ⟹ $$\boxed{P\ \text{是 }Q_9\ \text{中的二维仿射平面}}$$ ✓✓
- 【**⚠️(3) 但闭环\ \textbf{不排除} $3^4$（显式局部模型 ✓）**】$A_1=\{e_i,e_j,e_k,e_i{\oplus}e_j{\oplus}e_k\}$（4 点，$e(A_1){=}0$ ✓）、$P=\{0,e_i{\oplus}e_j,e_i{\oplus}e_k,e_j{\oplus}e_k\}$ ⟹ $r(p)=\mathbf{(3,3,3,3)}$ ✓、$\sum r=12$ ✓、$2D_2=12$ ⟹ $D_2=6$ ✓✓ ⟹ **闭环条件不排除 $3^4$** ✗✓（但**全局**可完成性未验 ⚠️：须 $|A|{=}45$、$|U|{=}119$、其余 $N(A_1)$ 点落 $U^c$ ✓）
- 【**✓(4) 其他正确项**】§11 的 $2D_2=\sum_P\binom{r_p}2=4\binom32=12\Rightarrow D_2=6$ 饱和等号 ✓✓；$r_{\max}\le3\Rightarrow D_2\le6$ ✓（C-449 ✓）
- 【**★(5) 新纪律 ✓✓**】凡使用 $\operatorname{supp}$／支撑类论证，**必须先显式声明是"坐标支撑"还是"方向集"** ✓✓（防第 5 次同型混淆 ✓）
- 【**★(6) 下一靶】① $3^4$：由"$P$ 二维仿射平面 ＋ $A_1$ 四点结构"做**全局**计数 ✓；② $3^32^11^1$：$r{=}2$ 点（1 个闭环点 ✓）与 $r{=}1$ 点（无闭环 ✓）之相容 ✓
- 【**边界 ✓**】零程序计算 ✓（仅整数与有限结构核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗；不声称 $3^4$ 已排除 ✗（V290）
- 档：`docs/WITPLANE-2026-09-28-profile-3-4-forces-an-affine-plane.md`

**🧊 C-451（2026-09-28 15:2x · **WITCUBE：$3^4\Rightarrow A_1\cup P\cong Q_3$（新 ✓✓✓）；修正 $N_1(A_1)$／$4{\cdot}6$；真接口 $N_2[A_1]$**）** ✓
- 【**✓✓✓(1) 唐先生 §2–§3 全部正确（新）**】$p_1=u=e_i{\oplus}e_j$：$p_1{\oplus}e_i=e_j\in A_1$ ✓、$p_1{\oplus}e_j=e_i\in A_1$ ✓；第三个方向由"闭环点须为另三个 $P$-点"定出 $\{i,j\},\{j,k\},\{i,k\}$ 全现 ⟹ $$\boxed{D(p)\equiv\{i,j,k\}\ \ \forall p\in P}$$ ✓✓✓ ⟹ $$\boxed{A_1=\{e_i,e_j,e_k,e_i{\oplus}e_j{\oplus}e_k\}}$$ ✓✓ ⟹ $$\boxed{A_1\cup P=p_0\oplus\langle e_i,e_j,e_k\rangle\cong Q_3}$$ ✓✓✓（$P$＝偶部、$A_1$＝奇部；$A_1$ 内两两距离全 2 ✓）—— **本线首个完整 $Q_3$ 局部闭环** ✓✓
- 【**✗✗(2) 唐先生 §5 之 (4)(5) 为假（24 个反例）**】"$N_1(A_1)=P\cup A_1$" ✗、"$x\notin P\cup A_1\Rightarrow d(x,A_1)\ge2$" ✗✗：对 $a\in A_1$、$l\notin\{i,j,k\}$，$a\oplus e_l$ 距 $A_1$ 为 **1** 且 $\notin P\cup A_1$ ✓，共 $4\times6=24$ 个（互异 ✓）⟹ **正确**：$$N(A_1)=P\ \dot\cup\ (24\ \text{外部点}),\quad |N(A_1)|=4+24=28,\quad |N[A_1]|=32$$ ✓（实测 $|N(A_1)|{=}28$ ✓）
- 【**✗(3) 算术**】唐先生 §9 写"每个 $p$ 有 7 个外向点" ✗ ⟹ $9-3=\mathbf6$ ⟹ $4\times6=\mathbf{24}$ ✓（非 28 ✗）
- 【**✓✓(4) 真接口（本档定出）**】由 $d(A_0,A_1)\ge3$（**非** $\ge2$ ✗）：$$\boxed{A_0\ \subseteq\ V\setminus N_2[A_1]}$$ ✓✓；实测 $|N_2[A_1]|=116$ ⟹ $$\boxed{|V\setminus N_2[A_1]|=396}$$ ✓✓ ⟹ 与 $|A_0|\ge33$ ✓ **不矛盾** ✗（仅大小不够 ⟹ 须用 $R$ 之结构 ✓）
- 【**✓(5) 其他正确项**】§1／§6：$P$ 二维仿射平面 ✓、$D_2=6$ 之 6 对＝3 个 weight-2 方向各两次 ✓✓、局部无松弛 ✓；§4：每个 $a\in A_1$ 在 $P$ 内 3 邻、$E(A_1,P)=12$ ✓；§7：$|A\setminus A_1|=41$ ✓✓
- 【**✗(6) 已否证**】"$N_1(A_1)=P\cup A_1$" ✗；"$x\notin Q_3\Rightarrow d\ge2$" ✗；"$4\cdot7=28$" ✗；"$A\setminus A_1\subseteq V\setminus N_1$" ✗
- 【**⚠️(7) 诚实**】$3^4$ **未被排除** ✗（真接口为 $N_2$、$396$ 点充裕）；**新纪律**：$d\ge3$ 用 $N_2$、$d\ge2$ 用 $N_1$，**须严格区分** ✓✓
- 【**⭐(8) 词回查自击更正 ✓✓**】三词实测**各 1 命中且唯一命中＝本档自身**（＝**自击**，因档先写、回查后跑 ✗）⟹ 已在 §3 写出**真实输出** ＋ 自击说明 ✓（本线他档命中 = 0 ✓）
- 【**★(9) 下一靶**】① 在 $R=V\setminus N_2[A_1]$（396 点）内做 min-distance-3 码之容量/结构分析，接 $|A_0|\ge33$ ✓；② $D_2=6$ 之 6 对与 24 个外部 $N(A_1)$-点之碰撞联络 ✓；③ profile $3^32^11^1$ 并行 ✓
- 【**边界 ✓**】零程序计算 ✓（仅 512 点邻域有限核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITCUBE-2026-09-28-profile-3-4-gives-a-Q3-subcube-and-the-true-N2-interface.md`

**🗂️ C-452（2026-09-28 15:5x · **WITLAYER：$R$ 之 14 行 profile 分解（✓✓✓ 全对）＋ $c\le12$（✓）＋ 修正 §7 的 $d\le8\to d\le16$**）** ✓
- 【**✓✓✓(1) 唐先生 §2 之 profile 分解全对（本档穷举核验）**】全 $512$ 点分 **14 行**（多重集 profile ✓）：$(0,2,2,2){:}4$｜$\mathbf{(1,1,1,3){:}4}$（**唐先生表遗漏 ✗ —— 此即偶部 $P$ 自身 ✓**）｜$(1,3,3,3){:}24{=}E_1$｜$(2,2,2,4){:}24{=}E_2$｜$(2,4,4,4){:}60$｜$(3,3,3,5){:}60$｜$(3,5,5,5){:}80$｜$(4,4,4,6){:}80$｜$(4,6,6,6){:}60$｜$(5,5,5,7){:}60$｜$(5,7,7,7){:}24$｜$(6,6,6,8){:}24$｜$(6,8,8,8){:}4$｜$(7,7,7,9){:}4$ ⟹ $$|N_2[A_1]|=116,\quad |R|=396$$ ✓✓（与 C-451 实测一致 ✓）；参数化 $u\in A_1\Rightarrow(r,r{+}2,r{+}2,r{+}2)$、$u\in P\Rightarrow(r{+}1,r{+}1,r{+}1,r{+}3)$ ✓✓
- 【**✓✓(2) §3–§4 正确**】固定 $\ell\in J$：$E_1(\ell),E_2(\ell)$ 间为 **3-正则二部图**（穷举：边数 12、左度全 3 ✓）⟹ 补图＝完美匹配 ⟹ $$\boxed{K_{4,4}-M}$$ ✓✓，$\ell$ 取 6 值 ⟹ 6 个同构块 ✓✓；$D_2$ 闭合 $\binom42\times12=72=24\times\binom32$ ✓✓
- 【**✓✓(3) §6 之 $c\le12$ 正确**】穷举支持：60 个 $(3,3,3,5)$ 点**每点恰 2 个 $E_2$-邻** ✓✓；由"$A_0$ 两点不可共享邻点（否则 $d\le2$ 违 $d\ge3$ ✗）"⟹ $2c\le|E_2|=24\Longrightarrow c\le12$ ✓✓
- 【**✗✗(4) §7 之 $d\le8$ 太强（本档修正为 $d\le16$）**】其"任意两个共 $y$ 的 $D$-点距离恰为 2" ✗ —— 可以是 **4** ✓。**正确**：$y=a\oplus e_\ell$，与之距离 2 的 $D$-点为 $x=a\oplus v$（$\ell\in v$、$|v|{=}3$、$v\subseteq J$ ✓，层内共 $\binom52=10$ ✓）；$A_0$ 内 $d\ge3\Longrightarrow|v\setminus v'|\ge2\Longrightarrow P_v\cap P_{v'}=\varnothing$（$v=\{\ell\}\cup P_v$、$|P_v|{=}2$、$P_v\subseteq J{\setminus}\{\ell\}$ 为 5 元 ✓）⟹ 互不相交 2-子集 $\le\lfloor5/2\rfloor=\mathbf2$ ⟹ $$\boxed{\text{每 }E_1\text{-点至多服务 2 个 }D\text{-点}}\Longrightarrow 3d\le48\Longrightarrow\boxed{d\le16}$$ ✓✓（非 8 ✗）
- 【**✓(5) 修正后的结论**】$c+d\le12+16=28$ ⟹ $$|A_0|\ge33\Longrightarrow\#\{x\in A_0:d(x,A_1)\ge4\}\ \ge\ \mathbf5$$ ✓✓（**非 13 ✗**；仍优于"396 容得下"之无结构论证 ✓，但强度弱于唐先生所期 ⚠️）
- 【**⚠️(6) 标签纪律**】唐先生本轮令 $P=\{100,010,001,111\}$（**奇部**）✗ 与 C-450 之约定（$P$＝偶部、$A_1$＝奇部）冲突 ✗ ⟹ **纪律**：凡用 $P/A_1$ 须**逐次显式声明奇/偶** ✓✓（同 C-450 之 supp 纪律 ✓）
- 【**✗(7) 已否证**】"共 $y$ 之 $D$-点距离恰 2" ✗；"$d\le8$" ✗；"$c+d\le20$" ✗；"$\ge13$" ✗；标签混用 ✗
- 【**⚠️(8) 自曝纪律（第二次）**】§3 词回查系**写入后才跑** ✗；**真输出**：`profile 分层`＝1（自击 ✗）、`服务数`＝1（自击 ✗）、`碰撞层`＝**25（既有 ⟹ 不计 ✗，非本档新增** ✗）⟹ 已在 §3 如实回填 ✓✓
- 【**★(9) 下一靶**】① **统一 incidence packing**：逐层算"每点可服务数 × 层大小"反推 $A_0$ 容量 ✓✓（本档已示范两层 ✓）；② 压 $4^3 6^1\,(80)$ 与 $4^1 6^3\,(60)$ 层之 per-point 界 ✓；③ 与 $D_2{=}6$ 之 72 计数联立 ✓
- 【**边界 ✓**】零程序计算 ✓（仅 512 点有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITLAYER-2026-09-28-R-profile-decomposition-and-the-d-le-16-correction.md`

**📊 C-453（2026-09-28 16:2x · **WITDEC：$c+d\le20$ 成立（✓✓✓ 替代 C-452 的 $d\le16$ 路线）＋ 层标签纠正（$|F|\le16$／$|G|\le12$／$(6,6,6,8)\le1$）**）** ✓
- 【**✓✓✓(1) 唐先生 §1／§3 邻居 profile 分解全对（穷举核验）**】$C=(3,3,3,5)$：$2\times(2,2,2,4)+3\times(2,4,4,4)+4\times(4,4,4,6)$ ✓✓；$D=(3,5,5,5)$：$0+3\times(2,4,4,4)+3\times(4,4,4,6)+3\times(4,6,6,6)$ ✓✓；$F=(4,4,4,6)$：$3\times(3,3,3,5)+3\times(3,5,5,5)+3\times(5,5,5,7)$ ✓✓；$G=(4,6,6,6)$：$0+4\times(3,5,5,5)+3+2$ ✓✓
- 【**✓✓✓(2) $$\boxed{c\le12,\ c+d\le20}$$ 成立且严格（本档确认，并替代 C-452 之 $d\le16$ 路线）**】$A_0$ 两点不可共享邻点（否则 $d\le2$ 违 $d\ge3$ ✗）⟹ $2c\le|(2,2,2,4)|=24$ ⟹ $c\le12$ ✓；$3c+3d\le|(2,4,4,4)|=60$ ⟹ $c+d\le20$ ✓✓ ⟹ $$|A_0\cap\{d(A_1){=}3\}|\le20,\quad |A_0|\ge33\Rightarrow\#\{d(A_1)\ge4\}\ge\mathbf{13}$$ ✓✓（唐先生更正后结论**现为严格** ✓✓；**本线目前最强 $A_0$ 容量界** ✓✓）
- 【**✓(3) §4／§5 正确（含其自我警示 ✓✓）**】容量须用**壳层**（$C_3{=}60$、$D_3{=}80$）而非 $|C|,|D|$ ✓✓（唐先生自标"容易再次滑落" ✓✓）；$f\le20$、$3f+4g\le80$ ✓
- 【**✗✗(4) §7 之"$F$--$G$ 无禁止边"不成立**】系基于错误 suffix 权重（其令 $G$ 之 $w{=}111111$ ✗）；**真实**：$F$ 层＝(偶 prefix, $|v|{=}3$ ✓)、$G$ 层＝(奇 prefix, $|w|{=}4$ ✓) ⟹ $|v\oplus w|\in\{1,3,5,7\}$（奇 ✓）⟹ $d(x,y)=d_{\text{pref}}+|v\oplus w|$（偶 ✓）⟹ $$\boxed{d(x,y)=2\ \text{可达}\Longrightarrow\textbf{禁止}\ ✗✓}$$ ⟹ **该线有约束、可用** ✓✓（非空 ✗）
- 【**✗✗(5) §10／§11 层标签错位（本档纠正）**】weight-4 suffix 层＝$(4,6,6,6)$（其"$G$"）而非 $F$ ✗；唯一 suffix 层＝$(6,6,6,8)$ 而非 $G$ ✗。**纠正后正确界（穷举定值 ✓）**：$F$ 层（weight-3，需 $|v\cap v'|\le1$）：极大族 $=\mathbf4$（＝Johnson $D(6,3,2)$ ✓）⟹ $$\boxed{|F|\le16}$$ ✓✓（非 12 ✗）；$G$ 层（weight-4，需 $|w\cap w'|\le2$ ⟺ 补集不相交）：极大族 $=\mathbf3$ ⟹ $$\boxed{|G|\le12}$$ ✓✓（非 1 ✗）；$(6,6,6,8)$ 层（唯一 suffix；四 prefix 两两距离 2）⟹ $$\boxed{\le1}$$ ✓✓（唐先生 §11 论证**正确但作用层错** ✗✓）
- 【**⟹ 修正后**】$|A_0\cap\{d{=}4\}|\le16+12=28$ ⟹ **"33 临界" ✗ 不成立**（$20+28=48>33$ ✓）；§13 之"$c{+}d{=}20,f{=}12,g{=}1$ 被迫" ✗（$d\ge4$ 有 28 槽位 ✓）
- 【**✓(6) 其他正确**】§8 之"同 prefix $\Rightarrow d{=}d(v,v')$、异 prefix $\Rightarrow d{=}2+d(v,v')$" ✓✓；§9 之 weight-4 互距必偶 ⟹ $d\ge4\iff|S\cap S'|\le2$、补集公式 $|S\cap S'|=2+|T\cap T'|$ ✓✓
- 【**✗(7) 已否证**】"$F$--$G$ 无禁止边" ✗；"$|F|\le12$" ✗；"$|G|\le1$" ✗；"$c+d\le20$ 来自 $d\le8$" ✗（正确来源＝两层容量 ✓✓）；"33 临界" ✗
- 【**★(8) 下一靶**】① 用 $\boxed{d(x,y){=}2\ \text{禁止}}$ 联立 $F$--$G$ ✓✓（唐先生谓"空" ✗ 故可用 ✓）；② $F$ 之 per-prefix 族（weight-3、交 $\le1$、极大 4）与 $C_3/D_3$ 之碰撞 ✓；③ $(6,6,6,8)\le1$ 之接入 ✓
- 【**边界 ✓**】零程序计算 ✓（仅 512 点邻居分解 ＋ 有限族极大性穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已\ \textbf{先跑后写} ✓✓**（`壳层容量` 1 命中既有 ⟹ 不计 ✗；余两词 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITDEC-2026-09-28-two-layer-capacity-cd-le-20-and-the-layer-label-correction.md`

**🔗 C-455（2026-09-28 12:4x · **WITCOUP：$r_q$ 分类（新 ✓✓✓）$r_q{=}3\Rightarrow|G_q|\le1$；$|\mathcal W(F_p)|\equiv3$（纠正 §3）**）** ✓
- 【**✓✓✓(1) 唐先生 §2 之刚性\ \textbf{完全正确}（穷举核验）**】$|F_p|{=}4$ 的合法 4-族共 **30** 个，且**全部**满足：两两交集**恰为 1** ✓ 与**每坐标恰出现 2 次** ✓✓ ⟹ "12 incidences 两次分摊"逐字正确 ✓✓；满 $F_p$ 是唯一形状（30 同构型 ✓）
- 【**✗✗(2) 唐先生 §3 之 $|\mathcal W(F_p)|\in\{3,4,5,6,7,9\}$ 不成立**】对**合法满族恒有** $$\boxed{|\mathcal W(F_p)|\equiv3}$$ ✓✓。根因：其基数 $30{+}360{+}1815{+}1815{+}810{+}15=4845=\binom{20}4$ 系**全部**四元组 ✗；合法满族仅 30 个 ✓，全部给 $|\mathcal W|{=}3$ ✓✓ ⟹ 其"最坏仍有 9 个可用、够放 $|G_q|{=}3$" ✗ —— 实为**恒 3** ⟹ $|G_q|\le3$ 是**紧的、零松弛** ✓✓（反而更有利 ✓）
- 【**✗(3) "四个奇邻点"／"$Q_4$" ✗**】prefix 图 $=F_2^3=Q_3$ ✓ 每点 **3** 邻 ✓ ⟹ $r_q\in\{0,1,2,3\}$ ✓（非 $0..4$ ✗）
- 【**✓✓✓(4) 本轮新获：$r_q$ 完整分类（穷举定值）**】| $r_q$ | $\big|\bigcap_{p\sim q}\mathcal W(F_p)\big|$ | $\max|G_q|$ ||---|---|---|| 0 | — | 3 || 1 | $\{3{:}30\}$ | 3 || 2 | $\{0{:}240,1{:}180,3{:}15\}$ | 3 || **3** | $\mathbf{\{0{:}3760,1{:}300\}}$ | **1** ✓✓✓ | ⟹ $$\boxed{r_q=3\Rightarrow|G_q|\le\mathbf1}$$ ✓✓✓ 与 $$\boxed{g\le12-2\cdot\#\{q:r_q{=}3\}}$$ ✓✓
- 【**✓✓(5) 推论**】四个偶 prefix **全满**（$f{=}16$）⟹ 每个奇 $q$ 皆 $r_q{=}3$ ⟹ $$\boxed{g\le4}$$ ✓✓（原为 12 ✗）
- 【**✓(6) 其他正确**】§1 之 $v\not\subseteq w$ 禁配 ✓✓（$|v\triangle w|$ 奇、$\min{=}1\iff v\subset w$ ✓；已成 $J(6,3)$–$J(6,4)$ 包含禁配 ✓）；§4 之 $G_q\subseteq\bigcap\mathcal W$ ✓✓；§6 之 $I{=}0$ 零交叉关联 ✓；§7 之壳层纪律（$C_3{=}60$／$D_3{=}80$）✓✓；§9 之 singleton 距离式（$|111111\triangle v|{=}3$、$|111111\triangle w|{=}2$ ✓✓）
- 【**✗(7) 已否证**】"$|\mathcal W|\in\{3,\dots,9\}$" ✗；"最坏 9 个可用" ✗；"四个奇邻点／$Q_4$" ✗；"$r_q\in\{0..4\}$" ✗
- 【**★(8) 下一靶**】① $t:=\#\{q:r_q{=}3\}$ 与 $f{=}\sum_p|F_p|$ 联立（$Q_3$ 二部 3-正则覆盖结构 ✓）；② $\Gamma_C,\Gamma_D$ 入 §8 三元 profile（$|\mathcal W|{=}3$ 已定值 ✓）；③ $r_q{=}2$ 之 15 个"交 $=3$"型（$\mathcal W$ 相同 ✓）单独审 ✓
- 【**边界 ✓**】零程序计算 ✓（仅有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`零松弛` 2 既有、`耦合不等式` 1 既有 + 2 空间 A 同名 ⟹ 均不计 ✗）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITCOUP-2026-09-28-rq-classification-and-the-W-identically-3-correction.md`

**🧩 C-456（2026-09-28 12:5x · **WITCAPP：局部 $F$--$G$ 耦合（新 ✓✓✓）；精确表 $\max(|F|{+}|G|)\le\mathbf{22}$**）** ✓
- 【**✓✓✓(1) 唐先生 §1 之 $F_i\cap F_j=\varnothing$ 成立（新）**】$p_i\ne p_j$ 皆偶 ⟹ $d_{\text{pref}}(p_i,p_j){=}2$（偶 prefix 互距 2 ✓）⟹ 若共享 suffix $v$ 则距离 $=2$ 违 $d(A_0)\ge3$ ✗ ⟹ $$F_i\cap F_j=\varnothing$$ ✓✓
- 【**✓✓✓(2) 唐先生 §2 之 $\partial^-G$ 机制成立（新，且严格 ✓✓）**】$\partial^-G:=\bigcup_{w\in G_q}\binom w3$；$v\in F_p$（$p\sim q$）⟹ $v\not\subseteq w$（否则 $d{=}1{+}1{=}2$ ✗）⟹ 恰为 $F_p\cap\partial^-G=\varnothing$ ✓✓
- 【**✓✓✓(3) 精确局部容量（本档穷举定值；唐先生两条更强）**】| $g_q$ | $\|\partial^-G\|$ | 可用 | $\max\Sigma_{p\sim q}f_p$ | 唐先生 ||---|---|---|---|---|| 3 | 12 | 8 | **8** ✓✓ | 8 ✓ |
|| 2 | 8 | 12 | **8** ✓✓ | 12 ✗（更强 ✓）|| 1 | 4 | 16 | **12** ✓✓ | 14 ✗（更强 ✓）|| 0 | 0 | 20 | **12** ✓✓ | 16 ✗ | ⟹（仅 3 邻 ⟹ $s_q\le12$）$$\boxed{s_q\le8\Rightarrow g_q\le3;\quad 9\le s_q\le12\Rightarrow g_q\le1}$$ ✓✓✓
- 【**✗✗(4) 唐先生 §3／§5 之 $Q_4$／"四个偶邻"仍误**】每奇 $q$ 仅 **3** 偶邻（穷举 ✓）⟹ $s_q\le12$（非 16 ✗）⟹ 其表 $s{=}13..16$ 三行**空置** ✗ ⟹ §8／§9 之"$|F|{=}15,16\Rightarrow|G|{=}0$" ✗ 不成立。**正确**：$s_q=|F|-f_{p(q)}$（每奇 $q$ 恰缺一个偶 prefix ✓）⟹ $|F|{=}16\Rightarrow s_q\equiv12\Rightarrow g_q\le1\Rightarrow$ $$\boxed{|G|\le4}$$（非 0 ✗）
- 【**✓✓(5) 唐先生 §11 方法对、系数错**】$|G|{=}12\Rightarrow g_q\equiv3\Rightarrow s_q\le8\ \forall q\Rightarrow\sum_q s_q\le32$；而 $\sum_q s_q=3|F|$（每偶点 3 奇邻 ✓）⟹ $3|F|\le32$（**非** $4|F|$ ✗，亦非 $F\le8$ ✗）⟹ $$\boxed{|G|=12\Rightarrow|F|\le10}\Longrightarrow\boxed{|F|+|G|\le22}$$ ✓✓（非 20 ✗）
- 【**✓✓✓(6) 本档新获：精确 profile 优化（照 §13／§14）**】穷举全部 $5^4{=}625$ 个 $(f_p)$ profile ⟹ $$\boxed{\max(|F|{+}|G|)\le\mathbf{22}}$$ ✓✓✓（原 28 ✗；于 $(0,4,4,4)$：$|F|{=}12,|G|\le10$ 与 $(2,2,2,4)$：$|F|{=}10,|G|\le12$ 取到 ✓）
- 【**✗(7) 已否证**】"$|F|{=}15/16\Rightarrow|G|{=}0$" ✗；"$G{>}0\Rightarrow F\le14$" ✗；"$g{=}1\Rightarrow\Sigma\le14$" ✗；"$g{=}0\Rightarrow\Sigma\le16$" ✗；"$4|F|\le32$" ✗；"$Q_4$／4 邻" ✗
- 【**✓(8) 其他正确**】§3 之 $\|\partial^-G\|{=}12$ ✓✓（无重合：三集重合须 $\subseteq w\cap w'$ 而 $|w\cap w'|{=}2$ ✗）；§4 之 $\|\partial^-G\|{=}8$ ✓；§7 反向阈值形式 ✓；§13／§14 profile 提法 ✓✓✓（本档即照此执行 ✓）
- 【**★(9) 下一靶**】① $|C|\le12$、$|D|\le12$ 与 $\boxed{|F|{+}|G|\le22}$ 联立（$d{=}3$ 与 $d{=}4$ 两层 ✓）；② $d(x,y){=}2$ 禁止联 $F$--$G$--$C_3/D_3$ ✓；③ $\Gamma_C,\Gamma_D$ 三元 profile ✓
- 【**边界 ✓**】零程序计算 ✓（仅有限穷举：$\binom{15}3$ 组 $G$ ＋ 族回溯 ＋ $5^4$ profile ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITCAPP-2026-09-28-local-FG-coupling-and-F-plus-G-le-22.md`

**🏛️ C-457（2026-09-28 12:4x · **WITCEIL：$|A_0|\le A(9,3)=40$ 支配层和（$42$／$41$ 不可达）；两层各 $\le1$**）** ✓
- 【**✓✓✓(1) 经典天花板支配（本档关键）**】$A_0$ 是 $Q_9$ 上最小距离 $\ge3$ 之码 ⟹ $|A_0|\le A(9,3)=\mathbf{40}$ ✓✓（经典值，C-442 已核 ✓）⟹ $$\boxed{c+d+f+g\ \le\ |A_0|\ \le\ 40}$$ ✓✓✓ ⟹ 唐先生 §1 之"独立相加 $=42$" **一出现即被支配** ✗✗（两层界 $20+22$ 非独立 ✓）；其 §11 所拟"$41$" **亦不可达** ✗✓；直接推论 $$c+d=20\Rightarrow f+g\le\mathbf{20}$$ ✓✓（唐先生猜 $\le21$ ✓ 成立但理由平凡 ✗）；$c+d=19\Rightarrow f+g\le21$；$c+d=18\Rightarrow f+g\le22$ ✓
- 【**✓(2) 跨层机制（唐先生 §5）成立**】$z\in C_3\cup D_3$、$v\in F\cup G$、$d(z,v)=2\Longrightarrow$ 不存在 ✓✓（因 $d(A_0)\ge3$ ✓，即既有约束之跨层实例 ✓）。**但 ⚠️**：欲得 $|F|+|G|\le22-\delta$ 须先求**精确极值** $\max\{c+d+f+g:\ d\ge3\}$ —— 本档仅得**构造下界 $25$**（贪心多重启 ✓）与上界 $40$ ⟹ **该极值未定 ⚠️（登记）**。贪心 $25$ 之 profile $=\{(3,3,3,5){:}8,(3,5,5,5){:}5,(4,4,4,6){:}6,(4,6,6,6){:}6\}$ ⟹ $c{=}8,d{=}5,f{=}6,g{=}6$ ✓
- 【**✓✓(3) 本档新小事实**】$(6,6,6,8)$ 层与 $(6,8,8,8)$ 层**各仅 4 点、两两距离 2** ⟹ $$\boxed{\text{各}\le1}$$ ✓✓（同 C-453 之 singleton 论证 ✓）⟹ $d\ge5$ 诸层（116 点 ✓）中至少两层各 $\le1$ ✓
- 【**✗(4) 已否证**】"$42$ 可达" ✗；"$41$ 可达" ✗；"$C{+}D{=}20\Rightarrow F{+}G\le21$ 为紧" ✗；"两层界独立" ✗
- 【**✓(5) 其他正确**】§2 之局部函数引用 ✓✓；§3 之 $|G|{=}12\Rightarrow|F|\le10$ ✓（留 2 单位 $s_q$-slack ✓）；§4 之两端点 $(12,10)$／$(10,12)$ ✓；§6 之 $(s_q,g_q,r_q)$ 提法形式 ✓；§7–§8 之三元 $\mathcal W$ 分类 ✓（$|Q_3|{=}8$、自同构小、单/双/三重覆盖之分 ✓✓）；§10 之"$c{+}d{=}20$ 时不能任取 $F{+}G$" ✓✓（精确形式 $f+g\le20$ ✓✓）
- 【**★(6) 下一靶**】① 精确求 $\max\{c{+}d{+}f{+}g\}$（须机制化，非贪心 ✗）—— 若 $<40$ 则天花板再降 ✓；② **更重要 ✓：转向覆盖侧** —— $|A_0|\ge33$ 与 119 覆盖条件之联合（层容量侧已近耗尽 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅有限集合构造 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITCEIL-2026-09-28-classical-ceiling-dominates-the-layer-sum.md`

**⚖️ C-458（2026-09-28 12:5x · **WITPARITY：extremal 恰 3 类（✓✓✓）；跨层 $d{=}2$ 机制为空（奇偶性 ✗✗）**）** ✓
- 【**✓✓✓(1) 唐先生 §2 之 extremal 三型完全正确**】穷举 $5^4{=}625$ profile：$\max(|F|{+}|G|){=}22$ ✓，达标 profile **14 个** ✓；按 $Q_3$ 自同构（$S_3\times V_4$，阶 24）合并 ⟹ $$\boxed{\text{恰 3 类}}$$ ✓✓✓：Type I $f{=}(0,4,4,4)$ $|F|{=}12$ $s{=}(12,8,8,8)$ $k{=}1$ $|G|\le10$（轨道 4）；Type II $f{=}(2,2,2,4)$ $|F|{=}10$ $s{=}(8,8,8,6)$ $k{=}0$ $|G|\le12$（轨道 4）；**Type III $f{=}(2,2,3,3)$** $|F|{=}10$ $s{=}(8,8,7,7)$ $k{=}0$ $|G|\le12$（轨道 6）✓✓
- 【**✓(2) 推理与 active bucket 全对**】$|G|\le12-2k$ ✓（$k{=}\#\{q:s_q\ge9\}$ ✓）；$s_q{=}|F|-f_{p(q)}$ ✓；Type I/II 之 $|A|{=}3$、Type III 之 $|A|{=}2$ ✓✓（穷举确认 ✓）
- 【**✗✗(3) 但跨层 $d{=}2$ 机制为空（本档推翻，含证明）**】跨层（$d{=}3$ 层 ↔ $d{=}4$ 层）之 prefix 奇偶**必相反** ⟹ $d_{\text{pref}}$ 奇；又 $|\triangle|$ 偶 ⟹ $$\boxed{d\ \text{恒为奇}}$$ ⟹ $d{=}2$ 不可能 ✗✗。**穷举印证**：$C_3$–$F$ $d{\in}\{1,3,5,7\}$（$d{=}1$ 240 对 ✓）；**$C_3$–$G$ $d{\in}\{3,5,7,9\}$（最小 3，$d{=}1$ 亦 0）** ✓✓；$D_3$–$F$、$D_3$–$G$ 同（$d{=}1$ 各 240 ✓）；而层内 $F$–$G$ 有 $d{=}2$ 720 对 ✓、$C_3$–$C_3$ 有 $d{=}2$ 660 对 ✓ ⟹ $$\boxed{C_3\ \text{禁掉 0 个 }G\text{-点}}$$ ✓✓（唐先生之 $|\partial^-G_q\setminus N_2(w)|$ 提法在 $C_3$ 侧**无对象** ✗）
- 【**✓✓(4) 真接口**】跨层唯一约束为 **$d{=}1$**（各 240 对 ✓）：$C_3$–$F$、$D_3$–$G$、$D_3$–$F$ 皆"同/邻 prefix ＋ 子集（等式）"型 ✓✓
- 【**✗(5) 已否证**】跨层 $d{=}2$ 禁配机制 ✗；$C_3$ 禁 $G$-点 ✗；§13 之 P1 机制（三元 profile 击穿 $g_q{=}3$）✗；"$42/41$ 可达" ✗（C-457 ✓）
- 【**✓(6) 其他正确**】§3/§4/§6：Type II/III 皆 $G{=}12\Rightarrow g_q{\equiv}3$、$s_q\le8$ ✓✓；$|\partial^-G_q|{=}12$ ✓；"2-for-1"（$s_q:8\to9\Rightarrow g_q:3\to1$）✓✓；Type I 之 $g{=}(3,3,3,1)$ ✓✓；§8 之"禁配位置数 $\ne$ 最大可选 $g_q$"之自警 **完全正确** ✓✓；§10 之鸽笼（$9/4>1\Rightarrow\exists m_q\ge3$）✓
- 【**★(7) 下一靶**】① $d{=}1$ 型跨层约束的精确容量式 ✓；② **更重要：转覆盖侧**（C-457 已示层容量侧封顶 40 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅有限穷举：$5^4$ profile ＋ 全部层对距离分布 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITPARITY-2026-09-28-extremal-three-classes-and-the-empty-cross-layer-d2.md`

**🔍 C-459（2026-09-28 12:5x · **WITAUDIT：对象审计 —— $N$＝普通 Hamming 邻域；$d(A_0)\ge3$ 只属 $A_0\subseteq C_0$（§9 之"冲突"＝混淆 ✗✗）**）** ✓
- 【**✓✓✓(1) 对象口径（逐字引档）**】$C\subseteq F_2^{10}$ 半径-1 覆盖、$|C|{=}119$ ✓（C-436 ✓）；$C_0,C_1\subseteq Q_9{=}F_2^9$ 为 $P_b{:=}\{x:(x,b)\in C\}$、$a{+}b{=}119$ ✓、**$N_9[S]$＝闭半径-1 邻域** ✓（**WITFIB 第 18 行 ✓✓✓**）；$N(C_0)\cap N(C_1)$ 为**开**邻域之交（$U^c$ 须"双色邻接" ✓，**WITSAT §0(1) ✓✓**）；两式等价 ✓；**$A=C_0\setminus\{h\}$** ✓（**WITA0 第 22 行 ✓✓✓**）；$A_0=\{a\in A:d_U(a)=0\}$ ✓（WITA0 第 24 行 ✓✓）⟹ $$\boxed{N=Q_9\ \text{中普通 Hamming-1 邻域}}$$ ✓✓（非 quotient／投影／owner-set ✗）
- 【**✗✗(2) §9 之"立即冲突"为\ \textbf{混淆}（本档消解）**】其设 $C_0,C_1\subseteq A_0$ ⟹ $d(u,v)\ge3\Rightarrow N(u)\cap N(v)=\varnothing$ ✗✗。**真相**：① $d(A_0)\ge3$ 只属 $A_0\subseteq A=C_0{\setminus}\{h\}\subseteq C_0$ ✓（WITA0 ✓），**不属** $C_0$ 本身、**亦不属** $C_0\times C_1$ ✗✓；② $|C_0|\ge45>A(9,3)=40$（C-442 ✓✓）⟹ $$\boxed{C_0\ \text{必含距离}\le2\ \text{之对}}$$ ✓✓（WITA0 已作**假前提**否证 ✓）；③ 覆盖条件**需要**距离-2 对（$u\in C_0,v\in C_1$ 有共同邻 $\iff d(u,v){=}2$ ✓）⟹ $$\boxed{\text{无冲突}}$$ ✓✓；其第 10 点"若为普通邻域则冲突" ✗（前提①错 ⟹ 不成立 ✓）
- 【**✓✓(3) §8 之 owner-pair 双计数＝档案已有 $q_{ab}$ 恒等式**】$q_{ab}{:=}|U^c\cap N(a)\cap N(b)|$ ✓（C-437 ✓✓）；$\sum_{a,b}q_{ab}{=}\sum_{x\in U^c}|N(x)\cap A||N(x)\cap B|$ ✓✓；**但按 C-438 之勘误**须写 $\ge|X_L|$ 而**非** $\ge|U^c|$ ✗（$X_L{:=}U^c\setminus N(H)$ ✓）
- 【**✓(4) §2–§3 之 deficit 重参数化正确**】$\alpha{:=}20-(c+d)$、$\beta{:=}22-(f+g)$ ⟹ $|A_0|{=}42-(\alpha+\beta)$ ✓；$|A_0|\le40\Rightarrow\alpha+\beta\ge2$ ✓；$|A_0|\ge33\iff\alpha+\beta\le9$ ✓；$|A_0|{=}40\Rightarrow(c+d,f+g)\in\{(20,20),(19,21),(18,22)\}$ ✓✓。**⚠️一处须改**：其 §1 之 $M{=}\max\{|A_0|:A_0\ \text{满足 119 覆盖条件}\}$ ✗ —— $A_0$ **单独**不载覆盖条件 ✗；正确形式：$A_0\subseteq C_0$ ∧ $(C_0,C_1)$ 满足 $U^c\subseteq N(C_0)\cap N(C_1)$ ✓✓
- 【**✓(5) 其他正确**】§4（$f+g{=}22\Rightarrow f$ 在三 extremal 族，C-458 ✓✓）；§5（$40\times10{=}400\le512$ ✓，宜慎言"完美码" ⚠️）；§6（$|N(C_0)\cap N(C_1)|\ge|U^c|$ ✓＝C-437 ✓）；§7（点数→owner-pair 数 ✓✓）；§11–§13（先攻 $|A_0|{=}40$ 三分配 ✓✓ 可执行）
- 【**★(6) 下一靶**】① 以**联合形式**重写 P1：$\big(A_0\subseteq C_0,\ (C_0,C_1)$ 满足 $U^c\subseteq N(C_0)\cap N(C_1)\big)$ ✓；② $|A_0|{=}40$ 三分配分支之 $C_0$ 结构分类 ✓；③ $q_{ab}$ 恒等式之夹逼（上界 $q_{ab}\le2$ ✓ 与 $\sum\le72\min(|A|,|B|)$ ✓（C-438 ✓）；下界 $\ge|X_L|$ ✓）
- 【**边界 ✓**】零程序计算 ✓（本档为引档审计 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`对象审计` 1 本线＋5 空间 A 同名 ⟹ 不计 ✗；余两词 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITAUDIT-2026-09-28-neighbourhood-nesting-audit-A0-vs-C0.md`

**🎯 C-460（2026-09-28 12:5x · **WITD1：跨层 $d{=}1$ 四机制（✓✓✓）；$M_C$ 精确表；$\tau_3(6){=}6$ 须改为"必要不充分"（✗✗）**）** ✓
- 【**✓✓✓(1) 唐先生 §1 之四条跨层公式全部正确**】$C_3{=}(p,S),|S|{=}2,p\in E$；$D_3{=}(q,S),|S|{=}3,q\in O$；$F{=}(r,V),|V|{=}3,r\in E$；$G{=}(s,W),|W|{=}4,s\in O$ ✓ ⟹ | 对 | $d$ 式 | $d{=}1$ 唯一条件 ||---|---|---|| $C$–$F$ | $d(p,r){+}5{-}2\|S\cap V\|$ ✓ | $\boxed{p{=}r\wedge S\subset V}$ ✓（240 对 ✓）|| $D$–$F$ | $d(q,r){+}6{-}2\|S\cap V\|$ ✓ | $\boxed{d(q,r){=}1\wedge S{=}V}$ ✓（240 ✓）|| $D$–$G$ | $d(q,s){+}7{-}2\|S\cap W\|$ ✓ | $\boxed{q{=}s\wedge S\subset W}$ ✓（240 ✓）|| $C$–$G$ | $d(p,s){+}6{-}2\|S\cap W\|\in\{3,5,7,9\}$ ✓ | $\boxed{\text{无}}$ ✓✓ | ⟹ $$\boxed{C{\to}F\ (\text{内含})\mid D{\to}F\ (\text{等式})\mid D{\to}G\ (\text{内含});\quad C\not\to G}$$ ✓✓（与 C-458 穷举一致 ✓✓）
- 【**✓✓✓(2) $M_C$ 精确定值表（穷举，＝唐先生 P1 ✓✓）**】合法 packing（两两 $|\cap|\le1$）共 **270** 个（$1{:}20,2{:}100,3{:}120,4{:}30$ ✓），无约束最大 $=\mathbf4$ ✓：| $m$ | 最坏 | 最好 ||---|---|---|| 0–1 | 4 | 4 || 2–3 | 3 | 4 || 4 | **2** | 3 || 5 | **1** | 3 || **6** | **0** | **3** ✗✗ || 7–9 | 0 | 2 || 10–12 | 0 | 1 || 13–15 | 0 | 0 |
- 【**✗✗(3) 唐先生 §6 之门槛须改**】$\tau_3(6){=}6$ 作为**最小值**正确 ✓（Turán $\mathrm{ex}(6,K_3){=}9\Rightarrow|\mathcal P|\ge6$ ✓）；**但"$|C_p|\ge6\Rightarrow F_p{=}\varnothing$"为假** ✗✗（穷举：$m{=}6$ 时最好情形仍有 $M_C{=}\mathbf3$ ✓✓）⟹ **正确**：$$F_p{=}\varnothing\iff P^c\ \text{无三角形}\iff P\ \text{含某 }K_{3,3}\ \text{划分之补}$$ ✓✓（最小杀尽集恰为 $P^c\cong K_{3,3}$，10 个划分 ✓）⟹ $$\boxed{F_p{=}\varnothing\Rightarrow|C_p|\ge6}$$（**必要 ✓，非充分 ✗**）；**方向②更强**：$$|F_p|{=}4\Rightarrow|C_p|\le\mathbf3$$ ✓✓（**非** $\le5$ ✗✗）；$|F_p|{=}3\Rightarrow|C_p|\le6$ ✓；$|F_p|{=}2\Rightarrow|C_p|\le9$ ✓
- 【**✓(4) 其他正确**】§3（$S\not\subset V$ 之 packing 约束 ✓✓）；§4（一 $C$-点杀同 bucket 恰 **4** 个 $F$-候选 ✓✓，$6{-}2{=}4$ ✓）；§5（情形分类 ✓；"pair-cover ⟹ $F_p{=}0$"方向正确 ✓）；§8（$D{\to}F$ 为**精确删点**：$(q,S)$ 杀 $(p,S)\ \forall p\sim q$ ✓✓，至多 3 bucket ✓）；§9（删除 $N_2$ 路线 ✓✓，P1 本档已完成 ✓✓）
- 【**✗(5) 已否证**】"$|C_p|\ge6\Rightarrow F_p{=}0$" ✗✗；"$|F_p|{=}4\Rightarrow|C_p|\le5$" ✗；跨层 $d{=}2$ ✗（C-458 ✓）
- 【**★(6) 下一靶**】① **P2**：$\bigcup_{q\sim p}\mathcal D_q$ 叠加后之四 bucket 联合容量 ✓；② **P3**：三 extremal（$(0,4,4,4),(2,2,2,4),(2,2,3,3)$）配 $|C_p|\le3$（$|F_p|{=}4$ 所需 ✓）之可行性 ✓；③ $|C|\le12$ 与 $\sum_p|C_p|$ 之预算分配 ✓
- 【**边界 ✓**】零程序计算 ✓（仅有限穷举：$2^{15}$ 个 $P$ × 270 packing ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITD1-2026-09-28-cross-layer-d1-four-mechanisms-and-the-MC-threshold-table.md`

**🧩 C-461（2026-09-28 12:5x · **WITP2：$|F_p|{=}4\Rightarrow C_p$ 是 $K_6$ 完美匹配（新 ✓✓✓）；但 $D$ 杀不掉该边界（✗✗）**）** ✓
- 【**✓✓✓(1) 完美匹配定理（本档新）**】$$\big(|F_p|{=}4\ \wedge\ |C_p|{=}3\big)\Longrightarrow\boxed{C_p\ \text{是 }K_6\ \text{的完美匹配}}$$ ✓✓✓。穷举：$\binom{15}3{=}455$ 个 3-pair $C_p$ 中**仅 15 个**容 $|F_p|{=}4$ ✓，且这 15 个**恰是** $K_6$ 的 15 个完美匹配 ✓✓（逐一核对 ✓）；每个完美匹配恰容 **2 个** 4-packing（$15{\times}2{=}30$ 个 $(C_p,F)$ 对 ✓）⟹ $F_p{=}4$ 是**极稀有构型** ✓✓
- 【**✗✗(2) 唐先生 §7 所期"$D$ 杀掉边界"不成立**】对**全部 30 个** $(C_p,F)$ 对，三个相邻 $D_q$ 的最大 packing **皆 $=4$** ✓✓ ⟹ $$|D(p)|{=}|D_{q_1}|{+}|D_{q_2}|{+}|D_{q_3}|\ \text{可达}\ 12$$ ✓✓（兼容 $|F_p|{=}4$ ✓）⟹ $D$ **不施压** ✗✓
- 【**✓✓(3) 跨 $D_q$ 之唯一约束（更正 §4 之"自动成立" ✗）**】$q\ne q'$ 皆奇 ⟹ $d_{\text{pref}}{=}2\Longrightarrow d{=}2{+}|S\triangle S'|\ge3\iff\boxed{S\ne S'}$ ✓✓ —— 故**非"不相交"**，而是**仅需相异** ✓（$S{=}S'$ 时 $d{=}2$ 仍禁 ✓）
- 【**✓✓(4) $C$-预算之直接后果（新构型约束）**】由 (1)：$|F_p|{=}4$ 要求 $C_p$ 为完美匹配 ⟹ **Type I** $(0,4,4,4)$：三满 bucket ⟹ $|C_{p_1}|{=}|C_{p_2}|{=}|C_{p_3}|{=}3$ ⟹ $$\boxed{|C|\ge9}$$ ✓✓（第四 bucket $\le3$ ⟹ $|C|\le12$ ✓）；**Type II** $(2,2,2,4)$：唯一满 bucket ⟹ $|C|\ge3$ ✓；**Type III**：无此约束 ✓
- 【**✓(5) 其他正确**】§1 反向界表 ✓✓（C-460 直读 ✓）；§2 之 $M(C_p,\mathcal D(p))$ 定义 ✓✓；§3（每 $p$ 只见三个 $D_q$ ✓）；§4 之"同 $q$ 内为 packing ⟹ $|S\cap S'|\le1$" ✓✓；§5（270 packing 过滤之提法 ✓，本档已执行 ✓）；§6/§8 路线方向 ✓✓
- 【**✗(6) 已否证**】"$D$ 杀边界 $(|F_p|{=}4,|C_p|{=}3)$" ✗✗；"不同 $q$ 之间自动 $d\ge4$" ✗（须 $S\ne S'$）；"$|C_p|\ge6\Rightarrow F_p{=}0$" ✗（C-460 ✓）
- 【**★(7) 下一靶**】① Type I 之三完美匹配 ＋ 第四 bucket 之联合可行性（$|C|\le12$）✓；② Type II 之 $|C_{p_4}|{=}3$ 与其余三 bucket 之相容 ✓；③ $|F_p|{=}3$ 类（$|C_p|\le6$）之结构定理（完美匹配之推广 ✓）
- 【**边界 ✓**】零程序计算 ✓（仅有限穷举：$2^{15}$ 个 $C_p$ × 270 packing × 30 对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`联合容量` 3 本线既有 ⟹ 不计 ✗；余两词 0 ✓）；**不作路线裁定** ✗；不声称 $a=45$ 已排除 ✗（V290）
- 档：`docs/WITP2-2026-09-28-perfect-matching-threshold-and-the-D-does-not-bite.md`

**🧊 C-462（2026-09-28 12:5x · **WITP3：完美匹配 $\to Q_3$ 候选立方体 $\to$ 两奇偶类（✓✓✓）；Type-I 可行（390 组）且"对面桶" $D$-容量 $4\to2$（✓✓ 新）**）** ✓
- 【**✓✓✓(1) 唐先生 §1 之结构表述完全正确**】$|C_p|{=}3\wedge|F_p|{=}4\iff C_p$ 为 $K_6$ 完美匹配 ✓✓✓；取 $C_p{=}\{\{1,2\},\{3,4\},\{5,6\}\}$ ⟹ 避 pair 之 triple＝每匹配边取一点（$2^3{=}8$ ✓）**恰成 $Q_3$** ✓✓；**packing $\iff$ 立方体内 Hamming 距离 $\ge2\iff$ 同奇偶类** ✓✓ ⟹ $$\boxed{\text{两个 4-packing ＝ 两个奇偶类}}$$：$F^{(0)}{=}\{135,146,236,245\}$、$F^{(1)}{=}\{136,145,235,246\}$ ✓✓（与唐先生逐字一致 ✓）；$15\times2=30$ 个**互异** $F$ ✓✓
- 【**✓✓(2) 唐先生 §2 正确**】跨 $D_q$ 之条件＝**suffix 集两两不相交** ✓✓（源自 $S{=}S'\Rightarrow d{=}2$ ✗；**非** triple 集不相交 ✗）；$|D(p)|\le12$ ✓✓；**无 $D$-侧坍缩** ✓✓（C-461 ✓）
- 【**✓✓✓(3) Type-I 三满桶\ \textbf{可行}（新，含计数）**】三偶桶皆 $|F|{=}4$ 且两两不相交之**无序三元组数 ＝ 390** ✓✓（有序 2340 ✓）⟹ Type I $(0,4,4,4)$ **未被排除** ✗✓
- 【**✓✓✓(4) 真正的多桶耦合（新）**】Type-I 中与"空桶"相对之奇 $q^*$（其三偶邻恰为三满桶）：$\bigcup_{p\sim q^*}F_p{=}F_1{\cup}F_2{\cup}F_3$（12 个 ✓）⟹ 可用 $=8$ ⟹ $$\boxed{\max|D_{q^*}|=\mathbf2}$$ ✓✓（其余三奇桶各邻 2 满桶 ⟹ 可用 12 ⟹ $\max|D_q|{=}4$ ✓）⟹ $$\boxed{\text{Type-I }D\text{-容量谱}=(2,4,4,4)}\Longrightarrow\sum_q|D_q|\le\mathbf{14}$$ ✓✓（原一律 16 ✗）—— **"三个 $F{=}4$ 桶共享一个对面奇桶"之结构 ⟹ 该桶被三满桶禁配夹住 ⟹ 容量减半** ✓✓
- 【**✓(5) 其他正确**】§3 $F$-profile $\to C$-profile 表 ✓✓（C-461 ✓）；Type I $\Rightarrow|C|\ge9$ ✓✓、Type II $\Rightarrow|C|\ge3$ ✓；§4 之"多完美匹配耦合"为正确靶点 ✓✓，且 $Q_3$ 中偶点三元组由 $V_4$ 平移**互相等价**（故 390 组已覆盖全部 ✓）
- 【**⚠️(6) 一处须补**】Type-II 之三个 $|F_p|{=}2$ 桶**不由 $C_p$ 单独确定** ✗（只知 $|C_p|\le9$）⟹ 其 $D$-耦合需额外输入 ✓（登记 ✓）
- 【**✗(7) 已否证**】"$D$ 杀 $(|F_p|{=}4,|C_p|{=}3)$" ✗；"Type-I 三满桶被排除" ✗；"$\sum_q|D_q|\le16$ 为紧" ✗（实 14）
- 【**★(8) 下一靶**】① $C$-侧：三完美匹配 ＋ 第四桶之联合可行性（$|C|\le12$）✓；② $D$-侧：由 $(2,4,4,4)$ 谱反推四桶联合预算 ✓；③ Type-II 之 $|F_p|{=}2$ 桶结构分类（须新输入 ✓）
- 【**边界 ✓**】零程序计算 ✓（有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITP3-2026-09-28-typeI-three-full-buckets-390-and-the-opposite-bucket-pressure.md`

**💥 C-463（2026-09-28 12:5x · **WITP4：P3 成立 —— Type I $(0,4,4,4)$ 被排除（纯结构，不依赖 $D$）；Type II 有显式见证**）** ✓
- 【**✓✓✓(1) 唐先生 P3 成立（本档穷举确认）**】30 状态 $(M,\epsilon)$ 之兼容图：**每个状态恰 8 个兼容** ✓✓、边数 **120** ✓✓、$$\boxed{\text{三角形数}=\mathbf0}$$ ✓✓✓ ⟹ 不存在三个两两兼容之 $(M_i,\epsilon_i)$ ⟹ $$\boxed{\text{Type I }(0,4,4,4)\ \textbf{不可行}}$$ ✓✓✓ —— **完全不依赖 $D$** ✓✓。两条件：$C_{p_i}\cap C_{p_j}{=}\varnothing\iff M_i\cap M_j{=}\varnothing$ ✓（同 pair ⟹ $d{=}2$ ✗）；$F_{p_i}\cap F_{p_j}{=}\varnothing$ ✓（同 triple ⟹ $d{=}2$ ✗）
- 【**✗✓(2) C-462 之 390 须加条件（本档更正）**】390 系"**仅** $F$ 两两不相交"之计数 ✓（当时未加 $M\cap M'{=}\varnothing$ ✗）；**二条件叠加后 $=\mathbf0$** ✓✓ ⟹ C-462 之 $\sum_q|D_q|\le14$ 等结论仅对 $F$-不相交情形成立 ✓，而**该情形现已不可达** ✗✓
- 【**✓✓(3) Type-II 有显式可行构型（本档构造）**】满桶 $M_0{=}\{(0,1),(2,3),(4,5)\}$、$F_0{=}\{(0,2,4),(0,3,5),(1,2,5),(1,3,4)\}$（$\epsilon{=}0$ ✓）；三 $|F|{=}2$ 桶 $F_{p_2}{=}\{(0,1,2),(0,3,4)\}$、$F_{p_3}{=}\{(0,1,3),(0,2,5)\}$、$F_{p_4}{=}\{(0,1,4),(0,2,3)\}$（两两不交且避 $F_0$ ✓）；$C$ 取 $\{0,5\},\{0,4\},\{1,2\}$（两两相异、避 $M_0$、不 $\subset$ 本桶 $F$ ✓）⟹ $|C|\ge6\le12$ ✓✓、$|F|{=}10$ ✓ ⟹ $$\boxed{\text{Type II 局部未被排除}}$$ ✗（**全局与 $D$-侧耦合尚未查** ⚠️）
- 【**✓(4) 现状**】三 extremal ⟹ $$\boxed{(0,4,4,4)\ \textbf{KILLED}}$$ ✓✓✓；(2,2,2,4) 局部可行 ✓；(2,2,3,3) **未查** ⚠️
- 【**★(5) 下一靶**】① Type II：纳入 $D$-侧（对面桶压力之类比 ✓）与 $|C|\le12$ 判定全局可行性 ✓；② Type III：无 $F{=}4$ ⟹ 须另找结构性 P2（$|F|{=}3$ 类结构定理 —— C-461 已登记 ✓）；③ **若 II 亦排除 ⟹ $F{+}G\le21$** ✓（直接改进 C-456 ✓）
- 【**边界 ✓**】零程序计算 ✓（有限穷举 ＋ 局部构造 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`三角形判据` 0 ✓；`状态图` 5、`局部见证` 3 皆空间 A 同名 ⟹ 不计 ✗）；**不作路线裁定** ✗（V290）
- 档：`docs/WITP4-2026-09-28-typeI-eliminated-by-the-triangle-criterion.md`

**🔄 C-464（2026-09-28 12:5x · **WITG2D：$G{\to}D$ 侧压力（新 ✓✓）$|D|\le13$（最坏 8，改进 16）；§6 之"贡献"为恒等式（✗✗）**）** ✓
- 【**✗✗(1) 唐先生 §6–§7 之"单 triple 跨桶贡献 $\le1$ lemma"为恒等式（无信息）**】$s_q{:=}\sum_{p\sim q}f_p$ 是 **triple 计数**（C-456 ✓）⟹ $r_{ij}{=}f_{p_j}{=}\mathbf2$ **恒成立** ⟹ $r_{ij}{=}2$ **自动取等** ⟹ 其"equality case"**无条件成立**，不构成新约束 ✗✓（但"跨桶耦合"之**方向正确** ✓✓，只需换对象 ✓）
- 【**✓✓✓(2) 真正的跨桶压力在 $G{\to}D$（本档新）**】由 C-458/C-460：$(q,S)\in D_q$、$(q,W)\in G_q$、$S\subset W\Longrightarrow d{=}1$ ✗ 禁 ✓✓ ⟹ 每个 $D_q$ 的 triple 须避 $\partial^-G_q{:=}\bigcup_{W\in G_q}\binom W3$（$|\partial^-G_q|{=}\mathbf{12}$ ✓ 穷举 ✓）**及**相邻偶桶之 $F$-triple ✓✓。**穷举定值**：纯 $G$ 约束下每桶 $\max|D_q|{=}\mathbf4$（可用 8 ✓）；叠加相邻 $F$ 后（精确版，只禁相邻桶）：分布 $\{(2,2){:}1,\ (3,2){:}5,\ (4,2){:}2,\ (3,3){:}5,\ (4,3){:}2\}$（前者＝缺满桶之 $q$，后者＝其余三 $q$ 之最坏）⟹ $$\boxed{|D|\le\mathbf{13}\ \text{（最坏 8）}}$$ ✓✓（**改进平凡界 16** ✗）。**读法**：$G$ 满载（$g_q{\equiv}3$）⟹ 每奇桶被 12 个 triple 占住 ⟹ $D$ 之可用面缩半 ✓✓
- 【**⚠️(3) 但 Type II 仍未被杀（诚实）**】C-463 之局部见证（$|F|{=}10$、$|C|\ge6$）与 $|D|\le13$ 相容 ✓；$|C|+|D|\le20$ ✓；$|A_0|\le40$ ✓ ⟹ **无矛盾** ⟹ Type II 全局可行性**仍开** ⚠️
- 【**✓(4) 其他正确**】§1（$f,s$ profile／$|F|{=}10$／$|G|{=}12$／$S_6$ 对称固定 $M_0$ ✓✓）；§2（须跨桶耦合 ✓✓）；§3（$3f_{p_*}{=}12$、$24$、余 $12$ ✓✓）；§5（$F_{p_*}\in\{\mathcal P_0,\mathcal P_1\}$／普通桶落 16 个剩余 ✓✓）；§8（$|C_{p_*}|{=}3\Rightarrow|C|\le12$ ✓✓；"$C$ 越满载 ⟹ $D$ 越低"✓✓ ＝ 本档 $G{\to}D$ 之镜像 ✓）；§9–§10（Type II 优先、III 后置 ✓✓；唯链中"六贡献取等"一环应换为 $G{\to}D$ 压力 ✓）
- 【**✗(5) 已否证**】"单 triple 贡献 $\le1$ lemma" ✗；"六贡献取等为刚性" ✗（自动成立）；"$|D|\le16$ 为紧" ✗
- 【**★(6) 下一靶**】① $G{\to}D$ 压力 × $C$-预算（$|C|+|D|\le20$）× $|A_0|\le40$ 三方联立 ✓；② Type II 之四桶 $G$-结构（$W$-族）全局一致性 ✓；③ 若 II 排除 ⟹ $F{+}G\le21$ ✓
- 【**边界 ✓**】零程序计算 ✓（有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITG2D-2026-09-28-G-to-D-pressure-and-the-contribution-identity.md`

**📐 C-465（2026-09-28 12:5x · **WITBUD：Type-II 对称预算区间 $11\le c{+}d\le18$（✓✓✓）；"$C\ge6$"为见证非界（✗✗）**）** ✓
- 【**✓✓✓(1) 唐先生 §1 正确**】Type II：$|F|{=}10$、$|G|{=}12$ ⟹ $|F|{+}|G|{=}22$；$|A_0|{=}c{+}d{+}22{+}t\le40$ ⟹ $$\boxed{c+d\le\mathbf{18}}$$ ✓✓✓（改进 C-453 之 $20$ ✓；精确为 $c{+}d\le18-t$，$t{:=}|A_0\cap(d{\ge}5\ \text{诸层})|$ ✓）
- 【**✓✓✓(2) 但真正有力的是下界（本档新，构成对称区间）**】$|A_0|\ge\mathbf{33}$（C-446 ✓✓✓）⟹ $22{+}c{+}d{+}t\ge33$ ⟹ $$\boxed{c+d\ \ge\ \mathbf{11}-t}$$ ✓✓✓ ⟹ $$\boxed{\mathbf{11}\ \le\ c+d\ \le\ \mathbf{18}}$$ ✓✓✓（含 $t$ 则整体移位 $[11-t,18-t]$ ✓）—— **Type II 之两层预算被\ \textbf{双向}夹住**：太少则 $|A_0|{<}33$ ✗，太多则 $|A_0|{>}40$ ✗ ✓✓
- 【**✗✗(3) 唐先生 §2 之"$|C|\ge6$"为见证非下界**】C-463 之构造**给出**一个 $|C|{=}6$ 之**可行样本** ✓（存在性 ✓），但 $C_p$ 可为**空** ✓（空 $C_p$ 不施约束 ✓）⟹ 不能推出 $|C|\ge6$ ✗；故 $|D|\le12$ **亦不成立** ✗✓。**仅有的 $|C|$ 下界**：$|C_{p_*}|{=}3$（C-461 完美匹配 ✓）⟹ $$\boxed{|C|\ge3}$$ ✓
- 【**✓✓(4) 唐先生 §5 之 $|R_q|\in\{2,3,4\}$ 正确**】$R_q{:=}\binom{[6]}3\setminus(\Sigma_q\cup\bigcup_{p\sim q}F_p)$ ✓、$\Sigma_q{:=}\bigcup_{W\in G_q}\binom W3$、$|\Sigma_q|{=}12$ ✓；**本档新增**：跨桶 $G$-quad 须**两两相异**（$q\ne q'$ 皆奇 ⟹ $d{=}2{+}|W\triangle W'|\ge3\iff W\ne W'$ ✓✓）⟹ 四个奇桶共 12 个 $W$ 互异 ✓（弱约束，但为全局一致性之必要项 ✓）
- 【**✓(5) 其他正确**】§3（"求 $D$ 下界而非上界"之方向 ✓✓，唯其据 $|D|\le12$ ✗ 不成立）；§5（四桶 $G$ **非独立** ✓✓，共享同一 6-点 universe ✓）；§6（$\sum_q|R_q|\le12$ 之问 ✓）；§7（归一化 $M_0$ ＋枚举 $F{=}2$ 桶／$G_q$／$R_q$／$D$ 之流程 ✓✓ 可执行）；§8（临界层 $(6,12),(7,11),(8,10)$ 之提法 ✓，唯 $C{=}6$ 之临界性依赖 §2 ✗）
- 【**✗(6) 已否证**】"$|C|\ge6$" ✗；"$|D|\le12$" ✗；"单 triple 贡献 lemma" ✗（C-464 ✓）
- 【**★(7) 下一靶**】① 按 §7 流程做小规模有限枚举，记录 $(|C|,|D|)$ 之可行 profile ✓；② 求 $|C|$ 之**真实**下界（覆盖侧或 $F$-侧强制 ✓）；③ Type III（$|F|{=}3$ 类结构定理 ✓）
- 【**边界 ✓**】零程序计算 ✓（整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITBUD-2026-09-28-typeII-budget-interval-and-the-witness-is-not-a-bound.md`

**📉 C-466（2026-09-28 13:0x · **WITSHRINK：$G$-family 状态空间收缩（合法桶 15、跨桶四元组 30）；$|D|\in[10,14]$ ⟹ Type II 仍开**）** ✓
- 【**✓✓✓(1) 有限状态空间（本档穷举）**】| 对象 | 计数 ||---|---|| 合法 $G_q$（3 quad、桶内两两交 **2**） | **15** ✓✓ || 跨桶 $W$ 互异之四桶组合 | **30** ✓✓ | ⟹ **Type-II 之 $G$-侧自由度仅 30 族** ✓✓✓（$C$-侧／$F$-侧并入后仍为极小有限集 ✓）
- 【**✓✓(2) $|D|$ 上界与预算之相容性（抽样 400 族）**】每桶 $D$-容量（$R_q$ 之 max packing）：$\min\in\{2,3\}$、$\max\in\{3,4\}$；四桶容量和分布：$10{:}2,\ 11{:}10,\ 12{:}13,\ 13{:}4,\ 14{:}1$ ⟹ $$|D|\le10\sim14$$（依赖 $G$-族 ✓）；与 $c\ge3$（C-461 ✓）联立 ⟹ $c+d\le\min(18,3{+}14)=17$ ⟹ $$\boxed{\text{预算区间 }[11,18]\ \text{与之相容}}\Longrightarrow\boxed{\text{Type II 仍开 ⚠️}}$$（本档无杀伤 ✓）
- 【**⚠️(3) 须记**】本档 $D$-容量按"邻满桶＋两普通桶"之**统一最坏**处理 ✗（Type II 中仅三个 $q$ 如此，第四个邻三普通桶 ✓）⟹ 上界 $[10,14]$ 为**指示性** ✓（精确值须按 $F$-配置逐 $q$ 分算 ✓ 已登记 ✓）
- 【**✓(4) 状态记法（照唐先生）**】$$\boxed{\text{Type I KILLED}}\ ✓✓✓;\quad \boxed{\text{Type II OPEN}}\ ⚠️;\quad 11\le c+d\le18✓,\ |R_q|\in\{2,3,4\}✓,\ W\ \text{跨桶互异}✓$$
- 【**★(5) 下一靶**】① 逐个（30 族 × $F$-配置）做**精确** $(c,d)$ 可行 profile 表（含 $t$ 之 $[11{-}t,18{-}t]$）✓；② 求 $|C|$ 之**真实下界**（覆盖侧强制 ✓）；③ Type III（$|F|{=}3$ 类结构 ✓）
- 【**边界 ✓**】零程序计算 ✓（有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`预算相容` 2 本线既有 ⟹ 不计 ✗；余两词 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITSHRINK-2026-09-28-G-family-state-space-30-and-budget-compatibility.md`

**🎭 C-467（2026-09-28 13:0x · **WITROLE：角色分算（近三桶 4,4,4／远桶 2–4）⟹ $|D|\le14{\sim}16$（更正 C-466 之 $[10,14]$）；$t$ 混淆（✗✗）**）** ✓
- 【**✗✗(1) 唐先生 §6–§8 之 $t$ 与 C-465 之 $t$ 是两个不同量**】唐先生 $t{:=}\#\{i:d_i\ge5\}$（$d_i{=}|D_{q_i}|$＝**$D$-桶大小** ✗）vs C-465 之 $t{:=}|A_0\cap(d{\ge}5\ \text{profile 层})|$（**高层点数** ✓）；区间 $[11-t,18-t]$ **仅对后者成立** ⟹ §7–§8 之"**死亡表**"**不成立** ✗✗（无通道由 $d_i$ 推 $t$）。正确的 $t$ 结构：$(6,6,6,8)$ 与 $(6,8,8,8)$ 各 $\le1$（C-457 ✓）⟹ $t\le18$
- 【**✓✓✓(2) 角色分算（新；更正 C-466 之 $[10,14]$）**】近桶 $q_i\sim p_0$ 须避 $F_0$ 与 $\partial^-G_q$；远桶 $q_0$ 须避三个 $F_2$：| 族数 | 近三桶容量 | 远桶 | $d$ 上界 ||---|---|---|---|| 5 | $(4,4,4)$ | 2 | **14** || 23 | $(4,4,4)$ | 3 | **15** || 2 | $(4,4,4)$ | 4 | **16** | ⟹ $$\boxed{|D|\le\mathbf{14}\sim\mathbf{16}}$$ ✓✓（**C-466 之 $[10,14]$ 系过强** ✗——彼时把 $F_0$ 错加于四桶全体 ✗）。机制：近桶仅需避 $F_0$ 之 4 个 triple（$20-12-4=4$ 可用 ✓ 且仍可满 packing ✓）⟹ **近桶无损 ✓✓，压力全在远桶（$2{\sim}4$）**
- 【**⚠️(3) 预算相容性（更正后仍相容）**】$c\ge3\Rightarrow c+d\le\min(18,3{+}16)=18$ ⟹ $[11,18]$ **相容** ⟹ $$\boxed{\text{Type II 仍开}}$$（含正确 $t$：$t{=}0$ 时 $[11,18]$ ✓；$t\ge2$ 时更紧 ✓，**但 $t\ge2$ 未被强制 ✗**）
- 【**✓(4) 其他正确**】§1（$33\le|A_0|\le40\Rightarrow11\le c+d\le18$；$c\ge3\Rightarrow d\ge11-c$ ✓）；§2（**带角色标签**四元组 ✓✓ —— 本档即按此执行 ✓）；§3（四桶不对称 ✓✓✓ —— C-466 §1(3) 已标 ⚠️，本档算实 ✓）；§9（六列框架 ✓，Gate 1/2 ✓ 正确）
- 【**✗(5) 已否证／须删**】"$c_{\min}(\sigma)$ 存在" ✗（C-465 更正：$C_p$ 可为空 ⟹ $c$ 无此下界；仅 $|C_{p_*}|{=}3\Rightarrow c\ge3$ ✓）；"$L_\sigma{+}U_\sigma<11$ 即死" ✗；"$t\ge2$ 被强制" ✗；**C-466 之 $[10,14]$** ✗（本档自纠 ✓）
- 【**★(6) 下一靶**】① 按修正后之门（$d_q\in\{2,3,4\}$ ✓、角色 ✓、$11-t\le c+d\le18-t$ 含**正确** $t$ ✓）做**精确** $(c,d)$ profile 表；② Type III（$|F|{=}3$ 类结构定理 ✓）；③ 覆盖侧对 $|C|$ 之**真实**下界
- 【**边界 ✓**】零程序计算 ✓（有限穷举 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITROLE-2026-09-28-role-split-near-4-4-4-far-2-4-and-the-t-conflation.md`

**🌉 C-469（2026-09-28 13:0x · **WITBRIDGE1：层间距离-2 表（69 零对）；双覆盖配对约束（桥第一块）**）** ✓
- 【**✓✓✓(1) 层间距离-2 存在性表（穷举 14×14）**】$Q_9$ 按 $A_1$ 之 profile 分 **14 层**（大小 $4,4,24,24,60,60,80,80,60,60,24,24,4,4$ ✓）；**零对共 69 个** ✗；非零者由**奇偶性**决定 ✓✓（$d{=}d_{\text{pref}}{+}|\text{suffix}\triangle|$，两部分之奇偶性决定 $d$ 之奇偶 ⟹ $d{=}2$ 仅当两皆偶且和为 2 ✓）。$A_0$ 诸层间之零对（**不可**互相提供双覆盖）：$(3,3,3,5)$×$\{(4,4,4,6),(4,6,6,6),(5,7,7,7),(6,6,6,8),(6,8,8,8),(7,7,7,9)\}$ ✗；$(3,5,5,5)$×$\{(4,4,4,6),(4,6,6,6),(6,6,6,8),(6,8,8,8),(7,7,7,9)\}$ ✗；$(4,4,4,6)$×$\{(5,5,5,7),(5,7,7,7),(6,8,8,8),(7,7,7,9)\}$ ✗；$(4,6,6,6)$×$\{(5,5,5,7),(5,7,7,7),(7,7,7,9)\}$ ✗；等 ✓
- 【**✓✓(2) 双覆盖配对约束（新，桥第一块）**】由 $U^c\subseteq N(C_0)\cap N(C_1)$：$\forall x\in U^c$ 有两个邻 $u\in C_0,v\in C_1$ ⟹ $d(u,v)\in\{0,2\}$ ⟹ $$\boxed{\text{双覆盖必由一对\ \textbf{距离-2} 的 }(u,v)\ \text{提供}}$$ ✓✓ ⟹ 若 $C_0,C_1$ 之层集为 $\Lambda_0,\Lambda_1$ 则须 $\exists L\in\Lambda_0,L'\in\Lambda_1:\mathrm{D2}(L,L')>0$ ✓✓（否则 $N(C_0)\cap N(C_1)=\varnothing\Rightarrow U^c=\varnothing$ ✗ 与 $|U|\le119<512$ 矛盾 ✓）
- 【**✓✓(3) $C_3$ 层之允许配对清单**】$(3,3,3,5)$ 仅与 $\{(1,1,1,3){=}P,\ (1,3,3,3){=}E_1,\ (3,3,3,5),\ (3,5,5,5){=}D_3,\ (5,5,5,7)\}$ 有距离-2 对 ✓ ⟹ 若 $A_0$ 之 $C_3$-点在覆盖中承担角色，则 $C_1$ 须在上述层之一有点 ✓✓
- 【**⚠️(4) 只给定性约束**】桥之**定量**下界（$c\ge L$）仍未得 ⚠️；须把 $q_{ab}$ 恒等式（C-437/438 ✓）按层细化，联立 $|U^c|{=}512{-}s$ 与层配对表 ✓
- 【**★(5) 下一靶**】① $q_{ab}$ 之层细化：$\sum_{\text{pair}}q_{ab}=\sum_{x\in U^c}|N(x)\cap C_0||N(x)\cap C_1|$ 之下界 $|U^c|$ × 层配对表 ⟹ 对距离-2 对**数量**之下界 ⟹ 对层占用之下界 ⟹ 或可及 $c$ ✓；② Type III ✓
- 【**边界 ✓**】零程序计算 ✓（有限穷举 14×14 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITBRIDGE1-2026-09-28-layer-distance-2-table-and-double-coverage-pairing.md`

**🗺️ C-470（2026-09-28 13:1x · **WITMAP：五栏证明状态图（C-448→C-469）＋ 桥之定量核心恒等式**）** ✓
- 【**✓✓✓(1) 精确恒等式（本档）**】$$\sum_{x\in U^c}|C_0\cap N(x)|\cdot|C_1\cap N(x)|=\sum_{(u,v)\in C_0\times C_1}|N(u)\cap N(v)\cap U^c|$$ $$\Longrightarrow\ \boxed{\sum_{h\in H}|N(h)\cap U^c|+r\ \ge\ |U^c|}\quad\Big(r:=\sum_{u\ne v,\ d(u,v)=2}|N(u)\cap N(v)\cap U^c|\Big)$$ 结构：heavy 项 $\le9|H|$ ✓；$r\le2\#\{$距离-2 对$\}$ ✓（$Q_9$ 中 $d{=}2$ 恰有两个共同邻 ✓）；$|H|{=}119-s{=}|U^c|-393$ ✓
- 【**✗✗(2) 必改：heavy 项不可省**】唐先生写"$u\ne v\Rightarrow d(u,v){=}2$"**对 $U^c$ 全体不成立** ✗✗：$h\in H=C_0\cap C_1\ne\varnothing$（$|H|{=}|U^c|-393$ ✓）⟹ $u{=}v{=}h$ 可单独完成双覆盖 ⟹ $d{=}0$ ✗ 非 $2$。正确定义（＝C-438 修正 ✓✓）：仅对 $X_L:=U^c\setminus N(H)$ 才强制 $d{=}2$ ✓，即 $r$ 项只服务 $X_L$ ✓
- 【**✓✓(3) 粗界之真空/非真空分界（本档）**】用 $\sum_H\le9|H|$：$s{=}62$（$|U^c|{=}450$、$|H|{=}57$、$9|H|{=}513$）**真空** ✗；$s{=}80$（432/39/351）**有约束**（须 $r\ge81$ ✓）；$s{=}100$（412/19/171）（须 $r\ge241$）；$s{=}119$（393/0/0）（须 $r\ge393$，全由距离-2 对承担 ✓）⟹ 定量目标：$$\boxed{r\ \ge\ |U^c|-9|H|\ =\ 8|U^c|-3537}$$ 须与 $q_{ab}$ 之层上界冲突 ✓
- 【**✓✓(4) 层细化接口**】$q_{ab}:=\#\{(u,v)\in C_0^{(a)}\times C_1^{(b)}:d(u,v){=}2\}$ ✓；$r\le2\sum_{a,b}q_{ab}$ ✓；且 $q_{ab}{=}0$ 对 C-469 之 **69 零层对** ✓✓
- 【**✓(5) 五栏状态图（本档 §0）**】P0 结构 ✓闭｜F/G 局部：**I KILLED ✓✓✓／II ○／III ○**｜D 侧 $|D|\le14{\sim}16$ ✓天花板（暂停）｜C 局部 $c_{\min}{=}0$ ✓已排除｜**覆盖桥 ○ 唯一主攻口** ✓
- 【**✓(6) 其他核验**】唐先生之 $q_{ab}$ 定义（含层上标）✓；"共同邻恰 2" ✓；$Q(C_0,C_1){=}2q$ ✓；"目标应攻 $c{+}d$ 预算而非 $c$ 本身" ✓✓（$c{+}d{<}11$ 即死 ✓）；⚠️ 其"$|A_0|{=}22{+}c{+}d$"仅在 $t{=}0$ 时 ✓（通式 $|A_0|{=}22{+}c{+}d{+}t$ ✓）
- 【**★(7) 正式靶题（照唐先生）**】$$\boxed{\text{Type II covering bridge}:\ (F,G,D)\Longrightarrow\text{共同邻点容量上界}\Longrightarrow c+d\le10\ ?}$$ 第一步：把 $r$ 下界按层分裂、与 $q_{ab}$ 层上界（含 69 零对）冲突；第二步：$q_{ab}$ 精确层矩阵（14×14 可穷举）；第三步：Type III
- 【**边界 ✓**】零程序计算 ✓（符号/整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITMAP-2026-09-28-proof-state-map-and-the-bridge-quantitative-core.md`

**🔤 C-471（2026-09-28 13:1x · **WITUOBJ：$U$ 对象声明（$|U|\le119$ 为构造性恒等式）；①②确认；桥之干净形式 $X_L\to q$**）** ✓
- 【**✓✓(1) 唐先生 §① 正确（$X_L$ 版本）**】$H{:=}C_0\cap C_1$、$X_L{:=}U^c\setminus N(H)$ ⟹ 仅对 $x\in X_L$ 可排除 $d(u,v){=}0$ ⟹ $$x\in X_L\Rightarrow\exists u\in C_0,v\in C_1:\ d(u,v){=}2$$ ✓✓（＝C-438 ✓；**C-469 之层距离-2 表真正约束的是 $X_L$** ✓）
- 【**✓✓(2) 唐先生 §② 正确（全空间恒等式）**】$$\sum_{x\in\mathbb F_2^9}r_0(x)r_1(x)=9|H|+2q$$ ✓✓（$r_b{:=}|C_b\cap N(x)|$，$q{:=}\#\{(u,v)\in C_0{\times}C_1:d{=}2\}$；证明：展开 $=\sum_{(u,v)}|N(u)\cap N(v)|$，对角 $u{=}v{=}h\in H$ 给 $|N(h)|{=}9$，非对角非零 iff $d{=}2$ 且给 2 ✓✓）⟹ 限制到 $X_L$ 时 heavy 项消失（$X_L\cap N(H){=}\varnothing$）⟹ $$|X_L|\le\sum_{X_L}r_0r_1\le2q$$ ✓✓
- 【**✗✗(3) 唐先生 §③ 须定向更正：$|U|\le119$ 是构造性恒等式，非待证输入**】档案定义（C-435/C-436 ✓）：$U{:=}P_0\cup P_1$（两层投影之并）；$|C|{=}|C_0|{+}|C_1|{=}|P_0|{+}|P_1|{=}119$ **恒等式** ✓ ⟹ $H{=}P_0\cap P_1\Rightarrow|U|{=}119-|H|\le119$ ✓✓ **平凡成立**；且 $U$ 是 9-cover（$\mathbb F_2^9{=}N[U]$ ✓）⟹ $|U|\ge K(9,1){=}62$ ✓✓ ⟹ $$\boxed{62\le|U|\le119}$$ 两端**皆已成立** ⟹ **撤回 $|U^c|\ge393$ 与 $q$ 下界属误撤** ✗✗
- 【**✓✓(4) §③ 之根因：$U$ 之对象两义**】唐先生之 $U{=}\bigcup_{a\in A_0}N(a)$（**球并**，$|{\cdot}|\le10|A_0|\le400$ ✗）与档案之 $U{=}P_0\cup P_1$（**层并**，$62\le|U|\le119$ ✓）**不同** ⟹ **纪律（第 6 次同类混淆 ✓）**：凡用 $U/H/X_L/C_0/C_1/N/A_0$ 须**先声明对象** ✓✓
- 【**✓(5) 桥之干净形式（照唐先生）**】$$\text{Type II}\to U\to H\to X_L{=}U^c\setminus N(H)\to q\to\text{层容量}$$ (A) $62\le|U|\le119$ ✓；(B) $|X_L|\ge|U^c|-9|H|{=}8s-559$ ✓；(C) $$\boxed{q\ge\lceil(8s-559)/2\rceil}$$ ✓（仅 $s\ge70$ 生效）；(D) 层允许矩阵（69 零格删 ✓ C-469）；(E) $Q_{\max}$ **未求** ⚠️；(F) 预算 $11\le c{+}d\le18$、$d\le16$ ✓。数值：$s{=}70{\to}1$、$80{\to}41$、$100{\to}121$、$119{\to}\mathbf{197}$ ✓（**197 即 $s{=}119$ 特例** ✓）
- 【**★(6) 下一轮唯一靶点（照唐先生）**】$$\boxed{\text{Type II}\to(|U|,|H|,|X_L|)\to q_{\min}\ \text{vs}\ q_{\max}^{\text{layer}}}$$ 先问 Type II 全体合法状态之 $Q_{\max}{=}\max q$ 与 $L_{\rm cov}{=}\min|X_L|$；若 $L_{\rm cov}{>}2Q_{\max}$ ⟹ Type II 死 ✓；否则须进精细分配（共同邻落 $U$ vs $X_L$）⟹ **不依赖 197 ✓**
- 【**边界 ✓**】零程序计算 ✓（符号/整数核对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITUOBJ-2026-09-28-U-object-declaration-and-the-clean-bridge-XL-to-q.md`

**🅿️ C-472（2026-09-28 13:2x · **WITPOBJ：$P{:=}P_0\cup P_1$ 命名固化；Test 1/2 执行 ⟹ $q$-桥**不能**杀 Type II（$Q_{\max}\approx1339\gg197$）；单调下界障碍**）** ✓
- 【**✓✓(1) 命名固化（照唐先生令）**】$$\boxed{P:=P_0\cup P_1}\quad(|P|{=}119-|H|,\ |P^c|{=}512-s)$$ **硬纪律**：$$\boxed{U_{\rm ball}:=\bigcup_{a\in A_0}N(a)\ \text{不得再进入任何 }U/P\ \text{记法}}$$（防第 7 次同型混淆 ✓）。同时并存之两个 $C$ 义须声明：$C_0,C_1$＝半侧投影；$C_3:=A_0\cap(3,3,3,5)$＝层计数 ✗ 同符号不同物
- 【**✓✓(2) Test 1：Type II 层数据几乎约束不到 $q$**】Type II 之约束对象 $=A_0\subseteq A=C_0\setminus\{h\}$，$|A_0|\le40$，$|C_0|\ge45$ ⟹ $C_0\setminus(A_0\cup\{h\})$ 至少 **4** 点无约束；$C_1$（$\ge45$）**完全无约束** ⟹ **Type II 至多触及 41/119 个半侧点** ⟹ $Q_{\max}^{\rm layer}$ 几无压缩 ⚠️。自由上界：平凡 $q\le36\min(|C_0|,|C_1|)\le\mathbf{2124}$；Cauchy–Schwarz 精化 $q\le\frac{45\sqrt{|C_0||C_1|}}{2}\approx\mathbf{1339}$（据 $\sum_x r_S^2=9|S|+2A_2(S)\le45|S|$）
- 【**✓✓(3) Test 2：无 $s$ 区间被杀**】$q_{\min}(s)=\lceil(8s-559)/2\rceil\le\mathbf{197}$（$s{=}119$）；供给端 $Q_{\max}\gtrsim1339\gg197$ 对所有 $62\le s\le119$ 成立 ⟹ $$\boxed{\text{无 }s\ \text{区间被杀}\Longrightarrow q\text{-桥不能杀 Type II}}$$ ⚠️
- 【**✓✓(4) 障碍定位（本档）：单调下界障碍**】覆盖条件 $P^c\subseteq N(C_0)\cap N(C_1)$ 是**逐点 $\ge1$ 型** ⟹ 只给 $\sum_x r_0r_1$ 的**下**界（$8s{-}559$ 线之来源 ✓）⟹ $$\boxed{\text{覆盖条件永远给不出 }q\ \text{的上界}}$$ ✗（＝C-425 已记"covering inputs are monotone-down" ✓✓）；$q$ 之上界须来自**距离分布／LP 型**输入 ⟹ 当前资产池**无**此类工具 ✗
- 【**✗(5) Test 3（shielding）之预判**】其拆分（$X_L$ 项＋$P\setminus N(H)$ 项）提法正确 ✓，但两式为**同一恒等式**之拆分 ⟹ 拆分本身不产生新上界 ✗；shielding 项只给下界 ⟹ **Test 3 as stated 亦不能闭合** ⚠️
- 【**★(6) 可选方向（登记，不作裁定 ✗）**】① 引入距离分布／LP 型上界工具（$q$ 上界之源）；② 回 Type III（$|F|{=}3$ 类结构定理）；③ 重审 $C_0,C_1$ 之整体约束（覆盖侧是否存在**上界型**输入 ✗）
- 【**边界 ✓**】零程序计算 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`自由上界` 1 命中属**空间 A** ⟹ 标"空间 A 同名，不计" ✓；余两词 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITPOBJ-2026-09-28-P-convention-and-Test12-no-kill-monotone-lower-bound-obstruction.md`

**🔺 C-473（2026-09-28 13:3x · **WITT3：Type III P1 审计 —— $|F_p|{=}3$ 有刚性（$J(6,3)$-三角形）但**惰性**（无碰撞）；触达率 $\approx5\%$ ⟹ P1 未形成**）** ✓
- 【**✓核实(1) $n{=}6/7$**】档案（`DLP1B-2026-09-27`）**仅有论文表 5 之锚点**：$n{=}6\to\mathbf{11.5980}$、$n{=}7\to\mathbf{15.9999}$；原文"先在小 $n$ 上复现，才谈 $n{=}10$" ⟹ **复现未做** ✗；Theorem 2.5 完整陈述仍标"待抽" ✗；**工具已备**（cvxpy 1.9.3 + scs 3.3.1 实测可用 ✓）⟹ ① **卡在抽取，不卡在工具** ✓
- 【**✓✓✓(2) Gate 2（刚性 vs 枚举）：刚性成立**】穷举 $\forall|C_p|\in\{0,1,2,3\}$ 之**全部** $|F_p|{=}3$ 配置，交模式**无一例外**为：$$\boxed{\text{三 triple 两两恰交 }\mathbf1\ \wedge\ \text{三交}\ \mathbf0\ \wedge\ \text{并}\ \mathbf{=[6]}}$$（即 $J(6,3)$-三角形 ✓）；配置数：$m{=}0$:120、$m{=}1$:720、$m{=}2$:720、$m{=}3$:**120**（每桶 8 ✓）⟹ 刚性 ✓✓ 但**不含 $C_p$（自足）** ✗（对比 C-461：$|F_p|{=}4\iff C_p$ 完美匹配**有耦合** ✓✓）
- 【**✗(3) Gate 1（触达率）低**】Type III $f{=}(2,2,3,3)$ ⟹ $|F_p|{=}3$ 之桶 2 个、$F$-点 6（$|F|{=}10$）⟹ $\rho_C\approx6/119\approx\mathbf5\%$（与 Type II 之 41/119 同病 ✗）
- 【**✗(4) Gate 3 ＋ 碰撞测试：惰性**】方向 ✓✓（三角形刚性＝**排除型／上限型**约束，恰为 Type II 所缺者 ✓）但**碰撞测试全通**：全部 16 组 $(m_1,m_2)$ **皆可共存**（不可者 $=0$ ✗）；特别 $(3,3)$（皆完美匹配）105/105 可共存 ✗ ⟹ $$\boxed{\text{刚性但不产生任何碰撞} ⟹ \textbf{惰性}}$$（＝唐先生之**第四种**情形：非"枚举"，亦非"刚性+碰撞"）
- 【**⟹ 判定（依唐先生停止条件）**】"rigid＋collision ⟹ 继续；仅枚举 ⟹ 停；仍只有下界 ⟹ 停" —— 本档属第四种（rigid but inert）⟹ **P1 未形成** ✗；且三角形刚性系 $J(6,3)$ 之**经典自足事实**（与码无关）⟹ 新性亦弱 ✗
- 【**★(5) 三方向当前读数（登记，不作裁定 ✗）**】① LP/距离分布：**卡在 Theorem 2.5 抽取**（非工具 ✗✓）；② Type III：**刚性惰性 ⟹ P1 未形成**（本轮读数 ✗）；③ $C_0/C_1$ 整体上界型输入：**覆盖侧无此类**（C-472 ✓）
- 【**边界 ✓**】有限穷举 ✓（$J(6,3)$ ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITT3-2026-09-28-typeIII-P1-audit-rigid-but-inert-and-the-n6-n7-status.md`

**📜 C-474（2026-09-28 13:3x · **WITTHM：Theorem 2.5 ＋ 4.9 完整抽取（含全部依赖命题）；锚点核实；★战略发现：$n{=}10$ 之 SDP $=105.2223<107\le K(10,1)$，距 120 尚远 ⟹ ① 不能供给 $q$ 上界**）** ✓
- 【**✓✓✓(1) Theorem 2.5 完整陈述**】设定 $\mathbb E=[q]^n$、$C$ covering radius $r$、$M,M',M''$ 之 $\mathrm{Aut}$-平均（式 (6)）；**Prop 2.1**（对称＋四条基本不等式）；**Prop 2.2**（$M',M''\succeq0$；$R(1-M'_{\mathbf 0\mathbf 0},M'')\succeq0$，$R(c,A)=\begin{pmatrix}c&(\diag A)^*\\ \diag A&A\end{pmatrix}$）；**Prop 2.3**（$|C|=q^nM'_{\mathbf 00}$、$|C|^2=q^n\sum_{\mathbf u}M'_{\mathbf uu}$、$|C|^3=q^n\sum_{\mathbf u,\mathbf v}M'_{\mathbf u\mathbf v}$ ✓✓）；**Prop 2.4**（$N$ 之定义 (7)；$R(c,N)\succeq0$，$c=\sum_\ell\lambda_\ell|S_\ell(\mathbf 0)|M'_{\mathbf 00}-\beta$；$N_{\mathbf u\mathbf v}=-\beta M_{\mathbf u\mathbf v}+\sum_\ell\lambda_\ell\sum_{\mathbf w\in S_\ell(\mathbf 0)}M'_{\mathbf u-\mathbf w,\mathbf v-\mathbf w}$；四条 matrix cut 不等式 ✓）；**Theorem 2.5**：$$\boxed{K_q(n,r)^3\ge\min_{M,M',M'',N}q^n\sum_{\mathbf u,\mathbf v}M'_{\mathbf u\mathbf v}}$$（约束＝Props 2.1/2.2/2.4 ✓）。**Remark 2.2**：变量可仅取 $M'$ ✓✓（降维起点）；**Remark 2.3**：立方根式最紧；**Remark 2.1**：(i)–(iii) 来自 **Lasserre 层级**，(iv) 来自 **matrix cut 不等式** ✓
- 【**✓✓✓(2) Theorem 4.9 完整陈述（$q{=}2$ 对称约化）**】$I(2,n)=\{(i,j,t):0\le t\le i,j,\ i+j\le n+t\}$ ✓；$\mathbf 1_{S_i(\mathbf 0)}(\mathbf 1_{S_j(\mathbf 0)})^{\mathsf T}=\sum_t M^t_{i,j}$ ✓；$\mathcal A_{2,n}$（Terwilliger 代数 ✓）；Lemma 4.1（$M,M''$ 由 $x$ 表出 ✓）；$$\boxed{K_2(n,r)^3\ge\min_x 2^n\sum_{(i,j,t)\in I(2,n)}\binom{n}{i-j+t,j-t,t}x^t_{i,j}}\ (30)$$约束＝Props 4.2/4.3/4.5/4.8 ✓；Lasserre 系数 $\lambda^{i,j,t}_{j',t'}=\sum_d\lambda_d\alpha^{(i,j,t)}_{(i,j',t'),d}$ ✓；**复杂度：变量数与块尺寸平方和皆 $O(n^3)$** ✓✓✓ ⟹ $n{=}6,7,10$ 皆可算 ✓
- 【**✓✓(3) 链条与"谁加了什么"（照唐先生 §B）**】$$\text{Delsarte LP}\subset\text{Thm 2.5（SDP）}\subset\text{Thm 4.9（对称约化）}$$ 论文逐字："LP 约束被 Theorem 2.5 之 SDP 约束蕴含" ⟹ SDP 相对 LP 之**真实增益**＝(a) $M',M''$ **分别** PSD ＋ $R(1-M'_{\mathbf 00},M'')\succeq0$；(b) Lasserre 约束 $R(c,N)\succeq0$；(c) matrix cut 之**全族** ✓。4.9 非新约束而是**块对角化**（可算性）✓；计算所用 $(\lambda,\beta)$ ＝**球覆盖 ＋ Van Wee** 两族（论文逐字 ✓）
- 【**✓✓(4) 锚点核实（逐字出处）**】`l2txt.txt` 第 1510–1511 行（＝arXiv:2504.01932v2 Appendix A Table 5, $q{=}2$）：`| 6 | 11.5980 | X ...|`、`| 7 | 15.9999 | X ...|` ⟹ **为 $K_2(n,1)$ 之界值（非立方值 ✓，立方根 2.26 不符 ⟹ 确为界值 ✓）**。对照真值：$n{=}6$: 11.5980 vs **12**（shortened Hamming，差 0.402）；$n{=}7$: 15.9999 vs **16**（perfect Hamming，差 **0.0001** ✓✓ 近乎精确）；$n{=}10$: **105.2223** vs $\ge\mathbf{107}$（差 −1.78 ✗）
- 【**★★(5) 战略性发现（本档核心）**】目标任务需 $\ge120$（或排除 119-cover）；而本体 SDP 在 $n{=}10$ 仅给 **105.2223** ⟹ $$\boxed{\text{① 抽取成功，但该工具在 }n{=}10\ \textbf{不能}供给 Type II 所需之 }q\ \text{上界}$$（距 120 越 14.8，且低于已知 107 ✗）—— 与 C-426（"同工具再算撞不到窗口"）、C-427（"105.2223 低于 107，真实缺口 $=120-107=13$"）**完全一致** ✓✓
- 【**✓(6) 复现计划（可行但只验证实现）**】$O(n^3)$ ⟹ $n{=}6{:}\sim216$、$n{=}7{:}\sim343$ 变量（cvxpy+scs 已可用 ✓）；**尚缺**：§3 之 Terwilliger 连结系数 $\alpha$（未抽 ✗）与 $M^t_{i,j}$ 显式定义 ⟹ **复现门**：$n{=}6,7$ 独立复现 ⟹ 同值 ⟹ 才谈 $n{=}10$（复现不过，$n{=}10$ 不开 ✓）；**但**即使复现成功，$n{=}10$ 仍为 105.2 级 ⟹ 应视作**工具审计**而非主攻路线 ✓
- 【**✓(7) 抽取源已归档**】`sources/GijswijtPolak-2025-arXiv2504.01932v2-EXTRACT-S2-full.txt`（31,316 B）；`sources/GijswijtPolak-2025-arXiv2504.01932v2-EXTRACT-full-html2txt.txt`（168,069 B）
- 【**边界 ✓**】文献直读＋抽取 ✓（非计算 ✓）；未上 SDP 求解 ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITTHM-2026-09-28-theorem-2-5-and-4-9-full-extraction-and-the-n10-sdp-reading.md`

**🔗 C-475（2026-09-28 13:3x · **WITINT：② 共同邻域容量路线**归约到 C-472 同一不等式**（✗ 非新方向）；$h$ 依赖被抵消；朴素容量界不碰撞**）** ✓
- 【**✗✗(1) 归约（本档补证）**】$x\in N(C_0)\cap N(C_1)$（开邻域）⟹ $\exists u\in C_0\cap N(x),v\in C_1\cap N(x)$ ⟹ $d(u,v)\in\{0,2\}$ ⟹ 二分：(a) $d{=}0$（$u{=}v\in H$）⟹ $x\in N(H)$；(b) $d{=}2$ ⟹ $x$ 为该对之共同邻 ✓ ⟹ $$N(C_0)\cap N(C_1)\ \subseteq\ N(H)\cup\{\text{距离-2 对之共同邻}\}\ \Longrightarrow\ \boxed{|\cap|\le 9h+2q}$$ ✓✓ ⟹ 覆盖需求 $|\cap|\ge|P^c|{=}393+h$ 化为 $$\boxed{2q\ge393-8h=8s-559}$$ ⟹ **② 与 C-470/471/472 是同一对象** ⟹ **非新信息方向** ✗✗
- 【**✗(2) 朴素容量界不能碰撞**】$|\cap|\le\min(9a,9b)\le9\times59=\mathbf{531}$ vs 需求 $|P^c|\le393+57=\mathbf{450}$ ⟹ $531>450$ ⟹ **不排除碰撞** ✗（唐先生之 P1"证 $|\cap|<393+h$"无平凡证法 ✓）
- 【**✓✓(3) 新数据（随机抽样 5 组）**】$(|C_0|,|C_1|){=}(60,59)$：$|N(C_0)|{=}343{\sim}355$；$|N(C_1)|{=}327{\sim}355$；$$\mathbf{|\cap|=222{\sim}258}$$；$h{=}7{\sim}13$；$|P|{=}106{\sim}112$；需求 $|P^c|{=}400{\sim}406$ ⟹ **皆不满足** ✗（约 240 vs 400）⟹ 覆盖条件是**强**条件 ⟹ ② 之问真开放但难 ✗。**自纠**：本人先前猜"generic 对给 $\cap\approx500$"**错** ✗（实测 $\approx240$）
- 【**✓✓(4) $h$ 非新自由度**】容量侧亦随 $h$ 增长（$9h$ 项）⟹ $393+h\le9h+2q\iff393\le8h+2q$ ⟹ $h$ **越大越宽松**（$9>1$）⟹ 最紧端＝$h$ 最小（$h{=}0\iff s{=}119$）—— 与 C-472 表一致 ✓✓
- 【**✓(5) 逐条核验**】$|P^c|{=}393+h$ ✓；两者共覆盖同一 $P^c$ ✓；$|\cap|{=}|N(C_0)|{+}|N(C_1)|{-}|\cup|$ ✓；"找不依赖 $A_0$ 之全局结构"方向 ✓（但 ② 恰落回同一不等式 ✗）；$N(C)$ 容量只有 $9|C|$ 粗界 ✓（达界需 min-dist $\ge3$ 而 $A(9,3){=}40$ ✗）
- 【**★(6) 三路线同归一个缺口**】$$\boxed{q\ \text{之上界源}＝①\ \text{之缺口}＝②\ \text{之缺口}＝\text{C-472 之缺口}\ \text{—— 三者同一}}$$ ⟹ 可选方向（登记，不裁定）：(a) 换问题（119 之其他等价形）；(b) 找**真正新类型**之上界输入（等周/谱/距离分布 —— 但文献 SDP 已达 $105.2<107<120$ ✗）；(c) 暂挂本线转他线
- 【**边界 ✓**】有限穷举＋随机抽样 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`等价归约` 1 命中属本线 registry ⟹ **不计** ✗；余两词 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITINT-2026-09-28-intersection-capacity-route-reduces-to-C472.md`

**⚖️ C-476（2026-09-28 13:4x · **WITPAR：奇偶路线审计 —— $\lambda_{\min}(\frac12Q_{10}){=}\mathbf{-5}$ 非 $-3$ ✗✗ ⟹ 谱下界失效（$a{=}44/45$ 未被杀）；上界侧有效；确为**新对象**）** ✓
- 【**✗✗(1) $\frac12Q_{10}$ 之完整谱（本档计算）**】特征值 $=K_2(|S|)$，$|S|{=}0..5$ 模补（偶类上 $\chi_S{=}\chi_{S^{\mathsf c}}$ ✓）：$$\{45,\ 27,\ 13,\ 3,\ -3,\ \mathbf{-5}\}$$ 数值核对：512 顶点、度 45（min=max ✓）、`eigvalsh` 最小特征值 $=\mathbf{-5.0000}$ ✓✓ ⟹ $$\boxed{\lambda_{\min}(\tfrac12Q_{10})=\mathbf{-5}\ \text{而非}\ -3}$$ ✗✗（唐先生本轮用 $-3$ ✗）
- 【**✗✗(2) ⟹ 谱下界失效**】Hoffman 型 $p_E(s)\ge\frac12\big(45\frac{s^2}{512}+\lambda_{\min}s(1-\frac s{512})\big)$：用正确 $\lambda{=}-5$：$s{=}44\Rightarrow\mathbf{-15.47}$（**无信息** ✗）；$s{=}45\Rightarrow\mathbf{-13.62}$（无信息 ✗）；$s{=}50\Rightarrow-2.93$（无信息 ✗）；$s{=}60\Rightarrow25.78$；$s{=}74\Rightarrow82.38$ ⟹ **谱界仅在 $s\gtrsim55$ 起为正** ⟹ 于 $a{=}44,45$ **给不出下界** ✗✗ ⟹ 唐先生之"$p(44)\ge25$"、"$p(45)\ge28$"、"$a{=}44$ 不可能"、"$28\le p_E\le30$" **均不成立** ✗✗
- 【**✓✓(3) 上界侧有效（逐条确认）**】$10b\ge512-a\Rightarrow\boxed{44\le a,b\le75}$ ✓；$L_E:=10a-|N(C_E)|\le9a-393$ ✓；$L_O\le9b-393$ ✓ ⟹ $$\boxed{L_E+L_O\le285}$$ ✓（$9\cdot119-786{=}285{=}$excess ✓ 数值巧合为真 ✓）；$\sum_y\binom{k_y}2=2p_E$ ✓（$\sum_y k_y{=}10a$ ✓）；$\binom k2\le5(k-1)$（$k\le10$ ✓）⟹ $$\boxed{p_E\le\tfrac52L_E}$$ ✓ ⟹ $a{=}44$: $L_E\le3\Rightarrow p_E\le7$ ✓；$a{=}45$: $L_E\le12\Rightarrow p_E\le30$ ✓（**仅上界** ✗ 无配对下界 ✗）。另：$\sum_x\binom{m_x}2{=}2(n_1{+}n_2)$ ＋凸性 ⟹ $\boxed{n_1{+}n_2\ge143}$ ✓；$|\pi_i(C)|{=}119-e_i\ge62\Rightarrow\boxed{e_i\le57}$、$|E(C)|\le570$ ✓
- 【**✓(4) 与 C-472 为\ \textbf{不同对象}（唐先生判断 ✓✓）**】$q$＝**跨半侧**距离-2 对（按末坐标分半）；$p_E$＝**同奇偶侧**距离-2 对 ✓ 不同 ✓；且本路线上界侧健全 ✓（$L\to p$ 机制 ✓ 新资产）唯**下界工具用错参数** ✗
- 【**⚠️(5) 正确下界之工具（登记，未建立 ✗）**】① $\alpha(\frac12Q_{10}){=}A(10,4){=}40$ 仅给 $p_E\ge1$ ✗（$|S|-40=4$ 之平凡推论）；② 组合下界（极大独立集 $\oplus$ 4 点之加边数）—— 未建立 ✗。粗略估计（非定理 ✗）：40 点 (10,4)-码 $I$ ＋ 4 点：$\sum_{x\notin I}|N(x)\cap I|{=}40\cdot45{=}1800$ 摊于 472 点 ⟹ 均 $\approx3.8$ ⟹ 4 点约添 12–16 边 ⟹ 若真值 $\ge8$ 则 $a{=}44$ 确实死 ✓✓ 但**需严格下界** ✗
- 【**✓(6) 唐先生之裁定**】$$\boxed{\text{119 线 ＝ SUSPENDED（no current P1 source）}}$$ 复活条件＝新资产须提供此前没有的 **P1 上界／排斥机制** ✓✓；本档补充：奇偶路线之**上界侧**即一类新资产（$L\to p$ 机制 ✓），其**下界侧**仍缺 ✗ ⟹ 复活条件**尚未满足** ✓（但与"整体无攻击点"不同 ✓）
- 【**边界 ✓**】有限穷举＋谱计算 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITPAR-2026-09-28-parity-route-lambda-min-is-minus-5-not-minus-3.md`

**📏 C-477（2026-09-28 13:5x · **WITM44：$m(44)$ 审计 —— 启发式远未达极值结构 ⟹ 数值定不了 $m(44)\ge8$；关键算术（极大码外部度均值 3.814）；P1 真而定量核未决**）** ✓
- 【**✗✗(1) 启发式能力不足（本档实测 $\frac12Q_{10}$，512 点／度 45）**】纯贪心＋有限 1-交换之最大独立集仅达 **29** 点（真值 $A(10,4){=}40$ ✗✗）；44 点最少边局部搜索（增量＋候选采样）仅达 **18–21** 条边（目标 $\le7$ ✓）⟹ **距目标 10+ 条边** ⟹ $$\boxed{\text{数值无法判定 }m(44)\ge8}$$ ⟹ 本档**不能**证实亦**不能**否证 P1 ⚠️（与唐先生 §10"不要现在就 SAT"之谨慎一致 ✓）
- 【**✓✓(2) 关键算术（不依赖搜索）**】$I$ 为**极大** $(10,4)$-码（$|I|{=}40$）⟹ $\sum_{x\notin I}|N(x)\cap I|{=}40\cdot45{=}\mathbf{1800}$ 摊于 472 点 ⟹ $$\boxed{\text{外部度均值}=3.814}$$ ⟹ "40-码 ＋ 4 外部点"之边数 $=\sum(\text{4 点外部度})+(\text{4 点间边})$ ⟹ **分岔**：若 $\min$ 外部度${=}1$ ⟹ 4 点至少 4 边（$\le7$ 可达 ⟹ **P1 死** ✗）；若 $\min\ge2$ ⟹ 至少 8 边（⟹ 该族**支持** P1 ✓）⟹ $$\boxed{\text{P1 之真否}\iff\text{"极大码之最小外部度"}}$$ ✗（未定 ⚠️）。对照：29-码外部度 $\{1{:}32,2{:}151,3{:}231,4{:}67,5{:}2\}$（均值 2.702）⟹ 度-1 外部点在**非极大**码上大量存在 ✓（极大码未知 ✗）
- 【**✓(3) P1 性质审计**】$$\text{P1-A}:\ m(44)\ge8\iff|S|{=}44,\ e(S)\le7\Rightarrow\alpha(S)\ge41$$ 与 $\alpha{=}A(10,4){=}40$ 冲突 ⟹ $a{=}44$ 死 ✓✓。**⚠️ 性质**：$m(44)$ 是关于**一切** 44-点集之断言 ⟹ 蕴含"不存在 $a{=}44$ 之 119-cover" ✓——即原问题之一**真子案** ⟹ 难度同阶 ⚠️（档案反复教训：攻缺口＝攻墙）；唯本路线上界侧健全 ✓（C-476），故**形态**优于 C-472 ✗
- 【**✓(4) 可达工具（登记）**】① 极大 $(10,4)$-码之**结构**（文献可取 ⟹ 再作 blocking/extension 引理）；② min-edge 之 **Delsarte-LP**（新 LP，未建 ✗）；③ 更强搜索（退火／精确，本档未做 ✗）。**风险**：若某极大码存在 4 个**两两相距 $\ge4$ 且外部度 1** 之点 ⟹ $m(44)\le7$ ⟹ **P1 死** ✗✓
- 【**✓(5) 状态（接受唐先生之修正 ✓✓）**】奇偶分层 ✓；$44\le a,b\le75$ ✓；$L_E,L_O$ 上界 ✓；$p_E,p_O$ 恒等式 ✓；其上界 ✓；$\lambda_{\min}{=}-5$ 之谱下界 ✗（废弃）；$m(44)\ge8$ **OPEN**；$m(45)\ge31$ **OPEN**；blocking/extension 引理 **OPEN** ⟹ $$\boxed{\text{P1 已形成，但 quantitative lower bound 尚未形成}}$$ ✓（与"整体无攻击点"不同 ✓）
- 【**边界 ✓**】有限穷举／局部搜索 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITM44-2026-09-28-m44-audit-heuristics-fall-short-and-the-key-arithmetic.md`

**📋 C-478（2026-09-28 13:5x · **HANDOFF-2026-09-28：C-448→C-477 单页交接（checkpoint）＋ 两处新推导：✗ 顶点覆盖缺口 ｜ ✓✓ $A_{\rm even}(10,4){=}A(9,3){=}40$**）** ✓
- 【**✓✓(1) 单页交接**】当前接口 $\boxed{m(44){=}\min_{|S|{=}44,\ S\subseteq E(Q_{10})}e_2(S)}$；奇偶分裂 $a{=}|C_E|,b{=}|C_O|,a{+}b{=}119$；$L_E\le9a-393\Rightarrow p_E\le\frac52L_E\Rightarrow a{=}44: p_E\le7$ ⟹ $m(44)\ge8\Rightarrow a{=}44$ 无 119-cover。**已闭**：C-472（单调下界）／C-475（② 归约）／SDP（$n{=}10$ 仅 105.2223）／谱下界（$\lambda_{\min}{=}-5$，废弃 ✗✗）／Type I KILLED ✓✓✓／Type III INERT ✗／Type II 无 P1 ⚠️。**有效**：$44\le a,b\le75$／$L_E{+}L_O\le285$／$2p_E{=}\sum_y\binom{k_y}2$／$p_E\le\frac52L_E$／$n_1{+}n_2\ge143$／$e_i\le57,|E(C)|\le570$／与 $q$ 为不同对象 ✓
- 【**✗✗(2) 新推导①：P1 链有顶点覆盖缺口（本档）**】唐先生之"$e(S)\le7\Rightarrow\alpha(S)\ge41$" ✗：取每条边一端 ⟹ 顶点覆盖 $\le7$ ⟹ $S\setminus T$ 独立、$\ge44-7{=}\mathbf{37}$ ⟹ $37\le40$ **不矛盾** ⟹ $\alpha$ 路线**给不出** $m(44)\ge8$ ✗；$\alpha$ 仅给 $\tau\ge4\Rightarrow e(S)\ge4$（弱 ✗）⟹ 须由**直接极值论证**（§5 blocking 方向仍成立 ✓，唯须删 $\alpha$ 环节 ✗）
- 【**✓✓(3) 新推导②：$A_{\rm even}(10,4)=A(9,3)=40$**】① 上界：偶重量 $(10,4)$-码删一位 ⟹ 长度 9、距离 $\ge3$ ⟹ $|C|\le A(9,3){=}40$；② 下界：$(9,3)$-码 $D$（$|D|{=}40$）⟹ $C{=}\{(d,\mathrm{parity}(d))\}$ 为偶重量 $(10,4)$-码、$|C|{=}40$ ⟹ $$\boxed{A_{\rm even}(10,4)=A(9,3)=40}$$ 意义：确认 $\alpha(\frac12Q_{10}){=}40$ ✓；与 C-442 之 $A(9,3){=}40$ 同源 ✓
- 【**✓(4) P1 状态与主攻量**】$$\boxed{\text{119-cover：LIVE}}\quad\boxed{\text{P1：real structural attack point}}\quad\boxed{m(44)\ge8:\ \textbf{OPEN}}$$ **下一轮唯一主攻量**＝$$\boxed{\text{极大 }(10,4)\text{-码的外部点 blocking／degree-1 结构}}$$ 已定事实：$I$ 极大（$|I|{=}40$）⟹ $\forall x\notin I: d_I(x)\ge1$ ✓；$\sum d_I{=}1800$、均值 $3.814$ ✓；**切点**：若存在 4 个 pairwise $d\ge4$ 且 $d_I{=}1$ 之外部点 ⟹ $m(44)\le4$ ⟹ **P1 死** ✗；若一切极大码 $\min d_I\ge2$ ⟹ "40＋4"族 $\ge8$ 边 ⟹ 支持 P1 ✓。三支：P1-A 极大码结构（文献优先）／P1-B Delsarte-LP 直排 $e_2\le7$／P1-C 具体码之 $D_1(I)$ 之 $\alpha_{\ge4}$
- 【**✓(5) 禁止事项（照唐先生）**】① 继续随机/退火搜 $m(44)$（实测：独立集仅 29 vs 40；44 点最少边仅 18–21 ✗）；② 直接上大型 SAT；③ 把"未找到 $e\le7$"当下界；④ 由**非极大** 29-码之外部度分布推断 40-码 ⟹ **下次启动条件：先做极大 $(10,4)$-码结构／外部 blocking，再决定是否入 LP 或精确搜索** ✓✓
- 【**边界 ✓**】零新增搜索 ✓（仅符号推导 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/HANDOFF-2026-09-28-119-line-C448-C477-one-page-checkpoint.md`

**🏅 C-479（2026-09-28 13:5x · **WITBEST：Best 码验算 ✓✓（外部度谱 $\{3{:}160,4{:}240,5{:}72\}$、$\min{=}3$ ⟹ $D_1{=}D_2{=}\varnothing$）；删点追踪（$r{=}1$ 唯一谱 ⟹ 封 ✓✓；$r{\ge}2$ OPEN）；Branch A $\ge12$ ✓✓**）** ✓
- 【**✓✓(1) Best 码独立验算**】$I{=}\{4$ 基词之全部循环移位$\}$（`0100000011`, `0011111101`, `1100101100`, `0001010111`）：$|I|{=}\mathbf{40}$ ✓；**全奇重量** ✓；$\min d{=}\mathbf4$ ✓；自固定码字之距离分布 $=\mathbf{\{4{:}22,\ 6{:}12,\ 8{:}5\}}$ ✓✓（＝唐先生引文之 22/12/5 ✓）
- 【**✓✓(2) 外部度谱（同奇偶层内）**】$=\big\{\mathbf{3{:}160,\ 4{:}240,\ 5{:}72}\big\}$ ✓✓（点数 472 ✓、总和 1800 ✓）⟹ $$\boxed{\min_{x\notin I}d_I(x)=\mathbf3}\Longrightarrow\boxed{D_1(I)=D_2(I)=\varnothing}$$ ✓✓ ⟹ 唐先生之关键结构事实**成立** ✓（"degree-1 外部点"于 40-码**不存在** ✓✓）。**✓校准**：须限定**同奇偶层**（码字全奇 ⟹ 异层点度数恒 0 ✓；引文数字正是同层值 ✓）
- 【**✓✓(3) Branch A（$\alpha(S){=}40$）**】$S\supseteq I$、$|S|{=}44$ ⟹ $X{=}S\setminus I$、$|X|{=}4$ ⟹ $$e_2(S)=0+\sum_{x\in X}d_I(x)+e_2(X)\ge4\cdot3=\mathbf{12}$$ ✓✓（余量 4）；**✓修正**：此界**不需要 $X$ 独立** ✗（唐先生多设此条件，结论更强 ✓）
- 【**✓✓(4) 删点追踪（新数据）**】删 $r$ 码字得 $I_r$：$S\supseteq I_r$、$|S|{=}44$ ⟹ $e_2(S)\ge\sum_{x\in R}d_{I_r}(x)$，$|R|{=}4{+}r$。$$r{=}1:\ \text{40 个删除\ \textbf{唯一谱}}\ \{0{:}1,2{:}12,3{:}172,4{:}225,5{:}63\}\Longrightarrow5\ \text{最小度和}=\mathbf8\ \Longrightarrow\ \textbf{封住}\ ✓✓$$（473 点 ✓；**强刚性** ✓✓）｜$r{=}2$（780 对）：**4 种谱**，6 最小度和 $\in\{6,7,8\}$ ✗ **未封**（样例 $\{0{:}2,1{:}1,2{:}25,3{:}181,4{:}209,5{:}56\}$ ⟹ **度-1 点再现** ✗）｜$r{=}3$（2000 抽样）：20 种谱，7 最小度和 $\in\{4..8\}$ ✗
- 【**⚠️(5) 决定性小问题（下一轮）**】$r{\ge}2$ 支中"低度点能否**两两相距 $\ge4$**" ⟹ 能 ⟹ $m(44)\le6$ **P1 死** ✗；不能 ⟹ 该支封住 ✓。**本档贪心**：要求两两 $\ge4$ 时，全部 $r\in\{0,\dots,4\}$ 之可达 $e_2$ **皆 $=12$** ⟹ **未发现 $e_2\le7$ 之构造** ✓（P1 未被推翻 ✓）；**但贪心非最优** ✗ ⟹ $r{=}2$ 支真值 $\in[\mathbf6,\mathbf{12}]$ 未定 ✗
- 【**⚠️(6) 引用纪律**】Litsyn–Vardy 1994 之**唯一性**为**外部文献**（本档**未能离线核验** ✗）⟹ 标"外部引用，未核实" ✓；本档所验者为**该具体 40-码**之结构（独立 ✓）⟹ 若唯一性成立则升级至全体 ✓
- 【**✓(7) P1 新形态**】由"全部 44-点集"缩为 $$\boxed{r\ge2\ \text{支}\ \cup\ \text{不可延拓之 39-码}}$$ ✓ **显著变窄** ✓✓ 但**未闭合** ✗；已封：Branch A（$\ge12$ ✓）、$r{=}1$（$\ge8$ ✓）；OPEN：$r\ge2$、不可延拓 39-码、$\alpha(S)\le38$ 一般情形 ⚠️
- 【**边界 ✓**】有限穷举 ✓（40 字/512 点/780 对/2000 三元组 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITBEST-2026-09-28-best-code-verification-and-deletion-tracking.md`

**🧩 C-480（2026-09-28 14:0x · **WITOWNER：删点阶梯三级封死（$r{=}0{:}\ge12$／$r{=}1{:}\ge8$／$r{=}2{:}\ge8$ ✓✓）；blocking identity 全量成立（780 对，反例 0 ✓✓）；owner 超图资产**）** ✓
- 【**✓✓✓(1) blocking identity 全量成立**】$\forall D(|D|{=}2),\ \forall x\in D_1,\ \forall y\in E_2$：$$\boxed{d(x,y){=}2\ \vee\ d(y,c_1){=}2\ \vee\ d(y,c_2){=}2}$$ 实测：存在"兼容 degree-2 点"之对数 $=\mathbf0/780$ ✓✓（最大计数 0 ✓）；$(|D_1|,|E_2|)$ 分布 $=\{(1,25){:}160,(2,23){:}160,(0,28){:}120,(0,24){:}340\}$ ✓ ⟹ 唐先生 §6 断言**完全成立** ✓✓（＝owner 超图对 2-subset $D$ 之局部 blocking ✓）
- 【**✓✓✓(2) $r{=}2$ 支封死（$e_2\ge8$）**】$S\supseteq I_{38}$、$|S|{=}44$ ⟹ $R{=}S\setminus I_{38}$、$|R|{=}6$；$e_2(S)=\sum_{x\in R}d(x)+e_2(R)$。**危险模式唯二**：用两个 degree-0（被删码字）时 $\sum\le7\iff(0,0,1,2,2,2)$（$=7$）或 $(0,0,1,1,2,2)$（$=6$）——**两者皆需一个 degree-2 点与某 degree-1 点及 $c_1,c_2$ 两两不相邻** ✗（由 §0(1) 不存在 ✓✓）⟹ 取之则 $e_2(R)\ge1$ ⟹ $e_2\ge8$ ✓✓。其余模式 $(0,0,2,2,2,2)$ 给 $\sum{=}8$ ✓；不用 degree-0 点则 $\sum\ge10$ ✓（$(2,23)$ 支 $1{+}1{+}2{\cdot}4{=}10$ ✓）⟹ $$\boxed{r{=}2\ \text{（Best 子码之 38-码）}\ e_2\ge8\ \text{封死}}$$
- 【**✓✓(3) 删点阶梯（三级皆封）**】$r{=}0$：谱 $\{3{:}160,4{:}240,5{:}72\}$ ⟹ $e_2\ge\mathbf{12}$ ✓✓；$r{=}1$：唯一谱 $\{0{:}1,2{:}12,3{:}172,4{:}225,5{:}63\}$ ⟹ $e_2\ge\mathbf8$ ✓✓；$r{=}2$：4 种谱（如 $\{0{:}2,1{:}1,2{:}25,3{:}181,4{:}209,5{:}56\}$）⟹ $e_2\ge\mathbf8$ ✓✓（本档）
- 【**✓(4) $r{=}3$（抽样 400 三元组）**】低度谱 20 种；"兼容伙伴 $\ge2$"之情形数 $=\mathbf0$ ✓✓（同型 blocking 延续 ✓）；局部搜索最小 $e_2=\mathbf{12}$ ✓；唯**严格**封死须更多情形分析 ✗（未做完 ⚠️）
- 【**✓✓(5) 新资产：owner 超图（唐先生 §9 框架）**】$\mathcal H_{\rm Best}:=\{O(x)\}$ ＝40 顶点上 **472 条超边**（大小 3/4/5 ✓，160/240/72 ✓）；$d_{I_{40}\setminus D}(x)=|O(x)\setminus D|$ ⟹ 低度点 $\iff$ $O(x)$ 与 $D$ 高交 ✓✓（把 $Q_{10}$ 几何压成有限超图 ✓）
- 【**✓(6) 逐条核验**】§1（同层 512／472／度 45／距离分布 ✓）；§2（外部谱 $\min{=}3$、$\ge12$ ✓）；§4（$r{=}1$ 谱与 $\ge8$ ✓✓）；§5（$r{=}2$ 谱 ✓；**本档补强**："唯一危险模式"应扩为两种（含 $(1,1,2,2)$，160 对含**两个** degree-1 点），**两者皆被 kill** ✓✓）；§8–§10（owner 集／超图框架 ✓✓）
- 【**⚠️(7) 关键警告（唐先生 ✓✓）**】Litsyn–Vardy 证的是 $(10,40,4)$ 之**唯一性** ✗ 非"任意 $(10,39,4)$ 可延拓" ✓ —— 本档 §0(2) 之封死**仅覆盖 Best 子码** ✓
- 【**★(8) 下一轮唯一靶：Extension Lemma（P1-A）**】$$\boxed{\alpha(S)\ge38\Longrightarrow S\ \text{之最大 }(10,4)\text{-码可延拓至 Best 40-code}}$$ 若成立 ⟹ §0(3) 三级计算**立刻升级为正式证明**（$\alpha(S)\ge38\Rightarrow e_2(S)\ge8$ ✓），余 $\alpha(S)\le37$ 另杀 ✓。**诚实评估** ⚠️：该引理**不**由唯一性蕴含 ✗；须独立论证（LP／距离分布优先 ✓）；难度未知 ⚠️
- 【**边界 ✓**】有限穷举＋局部搜索 ✓（780 对全量 ✓；$r{=}3$ 抽样 400 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（三词均 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITOWNER-2026-09-28-deletion-ladder-three-levels-and-blocking-identity.md`

**🏁 C-481（2026-09-28 14:0x · **WITR2CLOSE：$r{=}2$ 支\ \textbf{严格封闭}（$\alpha(G_R){=}2$ 全 780 对 ＋ \textbf{结构证明} ✓✓）；$r{=}3$ \textbf{未封} ⚠️（新障碍：额外零点 160／9880、度 $\le2$ 集可分离 10 点）**）** ✓
- 【**✗笔误更正**】唐先生写 $d_S(x){=}|\{c\in S:d(x,c){=}\mathbf1\}|$ ✗ —— **同奇偶层内距离皆偶** ⟹ 恒为 0 ✗；应为 $d(x,c){=}\mathbf2$ ✓✓
- 【**✓✓✓(1) 精确证书（全 780 对）**】$\|L_R\|$ 分布 $=\{2{:}460,3{:}160,4{:}160\}$ ✓（$\le4$ ✓✓）；$L_R$ 度多重集 $=\{(0,0){:}460,(0,0,1){:}160,(0,0,1,1){:}160\}$ ✓；$$\boxed{M_R{=}\alpha(G_R)=\mathbf{\{2{:}780\}}}$$ ✓✓✓（远低于击穿所需之 6 ✓✓）；$d(a,b)$ 分布 $=\{4{:}440,6{:}240,8{:}100\}$ ✓
- 【**✓✓✓(2) 结构性证明（本档，非枚举）**】由 C-479 之 $\min d_{I_{40}}{=}3$ ✓✓：删 $D{=}\{a,b\}$ ⟹ $d_S(x)\ge3-2=1$ ✓（除 $a,b$ 外无 degree-0 ✓，与度多重集一致 ✓）；degree-1 点：$|O(x)\cap D|=d_{I_{40}}(x)-1\ge2$ 而 $\le2$ ⟹ $d_{I_{40}}(x){=}3$ 且 $D\subseteq O(x)$ ⟹ $d(x,a){=}d(x,b){=}\mathbf2$ ⟹ **$x$ 于 $G_R$ 中同时邻接 $a,b$** ✓；又 $d(a,b)\in\{4,6,8\}$ ⟹ $a,b$ 不相邻 ⟹ $$\boxed{\alpha(G_R){=}2,\ \text{唯一最大独立集}=\{a,b\}}$$ ✓✓。**副产品**：degree-1 点**只在 $d(a,b){=}4$ 时出现** ✓（与 (1) 之分类一致 ✓）
- 【**✓✓(3) $r{=}2$ 之严格封闭（$e_2\ge8$）**】度型枚举（用 $a,b$）：$(1,1,1,1){=}4$／$(1,1,1,2){=}5$／$(1,1,2,2){=}6$／$(1,2,2,2){=}7$／$(2,2,2,2){=}8✗$；前两者需 $\ge3$ 个 degree-1 点而 $|D_1|\le2$ ⟹ **不可能** ✗✓；后两者需 degree-2 点与某 degree-1 点及 $a,b$ 两两不相邻 ⟹ 与 C-480 之 blocking **冲突** ✗；不用 $a,b$：$\sum\ge1{+}1{+}2\cdot4=10>7$ ✓ ⟹ $$\boxed{r{=}2\ \text{支}\ e_2\ge8\ \text{（严格封闭）}}$$
- 【**⚠️⚠️(4) $r{=}3$ 诚实状态：未封**】**(a)** blocking 延续 ✓：全 9880 三元组之"可用 degree-2 伙伴"最大计数 $=\mathbf0$ ✓✓；**(b)** ✗**新障碍一**：外部 degree-0 点数分布 $=\{0{:}9720,\mathbf1{:}160\}$ ⟹ **160 个三元组有额外零点**（除 $a,b,c$ 外 ✗）；**(c)** ✗**新障碍二**：度 $\le2$ 集之贪心最大分离度可达 $\mathbf{10}$ ✗（度 $\le1$ 集仅达 3 ✓ 但大小可达 8 ✓）⟹ "纯低度点两两拉开"之逃逸**未被排除** ✗。本档局部搜索（7-子集）最小 $e_2{=}12$ ✓（提示 P1 存活）但**非证明** ✗ ⟹ $r{=}3$ **OPEN** ⚠️ —— **此处正是 P1 可能真正断裂的格子** ✗
- 【**✓(5) 阶梯／逐条核验**】$r{=}0$（$\ge12$）／$r{=}1$（$\ge8$）／$r{=}2$（$\ge8$，**本档严格化** ✓✓）／$r{=}3$ **OPEN** ⚠️；唐先生之"危险度型唯二"✓✓、"$\min d_I{=}3$ 之关键作用"✓✓、"不要马上打 $r\ge3$"✓✓、$\Sigma_7\le7$ 之 profile 方向 ✓✓ **皆正确** ✓
- 【**★(6) 下一靶（照唐先生）**】**Lemma E1**：$|S|{=}39,d_{\min}\ge4\Longrightarrow$ 可延拓为 $(10,40,4)$；**Lemma E2**（较弱 ✓）：仅须"可能产生 $e_2\le7$ 之 39-码"可延拓 ✓。**逻辑区分必须保持** ✓✓：Best 唯一 $\not\Rightarrow$ 每个 39-码可延拓 ⟹ 本档封闭**仅覆盖 Best 子码** ✗
- 【**边界 ✓**】有限穷举＋局部搜索 ✓（780 对 ＋ 9880 三元组全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查已先跑后写 ✓✓**（`严格封闭` 之 1 命中属**空间 A** ⟹ 标"空间 A 同名，不计" ✗✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITR2CLOSE-2026-09-28-r2-strictly-closed-and-the-r3-honest-status.md`

**🔗 C-483（2026-09-28 14:0x · **WITEQ：$d{=}0$ 引理之等价形式（可加⟺$d_S{=}0$ ⟹ "可延拓"$\iff$"极大"）；⚠️校正"$d{=}1\Rightarrow\exists d{=}0$"实为极大性命题；⭐$\alpha{=}39$ ⟹ 残点 $d\ge1$ ⟹ $r{=}1$ 支升级为 $e_2\ge\mathbf{10}$ ✓✓**）** ✓
- 【**✓✓(1) $d{=}0$ 引理之等价形式**】同层 $x\notin S$：$$\boxed{d_S(x){=}0\iff d(x,S)\ge4\iff x\ \text{可加入 }S}$$（两向皆一行 ✓）⟹ $$\boxed{\text{"无同层 degree-0 外点"}\iff\text{"极大（不可延拓）"}}$$ ✓✓
- 【**⚠️(2) 校正（本档）**】唐先生之"$d_S(x){=}1\Longrightarrow\exists y:d_S(y){=}0$"**并非自动** ✗ —— 其等价形式为"极大 39-码不含 degree-1 外点" ✗，**既不显然也无现成依据** ⟹ **不能作免证前提** ✓✓
- 【**⭐⭐(3) 新约束（一行）**】设 $S_{44}\supseteq I_{39}$、$|S_{44}|{=}44$、$\alpha(S_{44}){=}39$；若残点 $x$ 有 $d_{I_{39}}(x){=}0$ 则 $I_{39}\cup\{x\}$ 是 40-码 $\subseteq S_{44}$ ⟹ $\alpha\ge40$ ✗ 矛盾 ⟹ $$\boxed{\forall x\in S_{44}\setminus I_{39}:\ d_{I_{39}}(x)\ge1}\ ✓✓$$（残点度下界由 $\ge0$ 升为 $\ge1$ ✓）
- 【**✓✓(4) $r{=}1$ 支升级**】由 C-479 之唯一谱 $\{0{:}1,2{:}12,3{:}172,4{:}225,5{:}63\}$：唯一 degree-0 点＝$a$ 自身 ✓；由 (3) $a\notin S_{44}$ ✓（否则 $I_{39}\cup\{a\}{=}I_{40}\Rightarrow\alpha{=}40$ ✗）⟹ 残点度 $\ge\mathbf2$ ⟹ $$\boxed{e_2(S_{44})\ge5\cdot2=\mathbf{10}>7}$$ ✓✓（**C-479 之 $\ge8$ 升级为 $\ge10$** ✓✓）
- 【**⚠️(5) $d{=}1$ 真形态**】于 $\alpha{=}39$ 之 44-集：残点度 $\ge1$（一般 39-码）／$\ge2$（Best 型）⟹ 要 $e_2\le7$ 须 $\sum$ 残点度 $\le7$ 且残点内部几无距离-2 边 ⟹ 度型极窄 ✓。**唐先生"owner 双重计数"**（$x$ 侧 $N_2(x)\cap S{=}\{a\}$ ／ $a$ 侧 $O(a)\setminus\{x\}$）**采纳为下一靶** ✓✓。**诚实边界** ⚠️：一般 39-码（非 $\alpha{=}39$ 之 44-集）之 $d{=}1$ 支**仍 OPEN** ✗；但 P1 只需 $\alpha{=}39$ 情形 ⟹ (3) 是**正确接口** ✓✓
- 【**✓(6) 逐条核验**】唐先生之"统一机制（$O_I(x){=}D$、$d(x,S){=}4$）"✓✓、"$S\cup\{x\}$ 确为 38-码"✓✓（本档给完整刻画 ✓）、"先隔离 $d{=}1$"✓✓ **皆正确**；唯 (2) 之命题性质须校正 ✗✓
- 【**流程 ✓✓**】本轮**已恢复"先跑后写"** ✓✓（四词皆写入前测得 0 ✓）—— 修正 C-482 之流程瑕疵 ✓；E2 之 $e_2$ 口径亦已澄清（须指环境 44-集 ✓）
- 【**边界 ✓**】有限穷举＋一行证明 ✓；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**不作路线裁定** ✗（V290）
- 档：`docs/WITEQ-2026-09-28-d0-equivalence-residual-degree-bound-and-the-r1-upgrade.md`

**🚫 C-484（2026-09-28 14:1x · **WITD1EMPTY：命题 P（Best 家族 39-码无 degree-1 外点，一行证明 ✓✓）⟹ $r{=}1$ 支强化为 $e_2\ge\mathbf{10}$ ✓✓；✗自我更正 Family B$=\{p,q\}$**）** ✓
- 【**✓✓命题 P**】$I_{39}{=}I_{40}\setminus\{a\}$ 无同层 degree-1 外点。**证明（两情形）**：$d_{I_{39}}(x){=}d_{I_{40}}(x)-|O(x)\cap\{a\}|$；情形 1（$a\notin O(x)$）：$d_{I_{39}}{=}d_{I_{40}}\ge3$ ✗；情形 2（$a\in O(x)$）：$\ge3-1=2$ ✗ ⟹ **不存在 $=1$** ✓✓。**数值复核**：40 个 39-码合并外形度分布 $=\{0{:}40,2{:}480,3{:}6880,4{:}9000,5{:}2520\}$，degree-1 总数 $=\mathbf0$ ✓✓
- 【**✓✓$r{=}1$ 强化**】由 C-483 之 $a\notin S_{44}$ ＋ 命题 P ⟹ 残点 5 点度 $\ge2$ ⟹ $$e_2(S_{44})\ge5\cdot2=\mathbf{10}>7$$ ✓✓；唐先生之 5 个危险型（$(1,1,1,1,1)\dots(1,2,2,2,2)$）**全部需 $\ge3$ 个 degree-1 点 ⟹ 结构性不可能** ✓✓ ⟹ case-split **退化**
- 【**✗自我更正**】对话中称"Family B（删 2 补 1）为空" ✗ **错误**：构造循环以 $x\notin I_{40}$ 为条件而**排除了码字自身** ✗✓。**正确**：$O(v)=\varnothing$ 对一切 $v\in I_{40}$（$d_{\min}{=}4$）⟹ 可补点 $=\{p,q\}$ ✓✓ ⟹ $$\boxed{|D|<3\Longrightarrow\text{除 }D\text{ 自身外无补点}}$$ ✓（唐先生 §owner 阈值之正确形态 ✓）；与 C-482 之 $r{=}3$ 零点门槛**一致** ✓
- 【**⚠️不可达性**】非 Best 之 39-码**构造不出** ✗（60 次贪心极大独立集最大仅 $\mathbf{32}$ ✗，真值 40 ✓）⟹ $d{=}1$ 支**无法被触发** ✗ ⟹ 须转 38-码（C-485 ✓）

**🎯 C-485（2026-09-28 14:1x · **WITINC38：38-码 $A_x/B_x$ incidence 实验 —— $A_x$ \textbf{定义性为空} ✗；兼容池三重常数（$\le2$ 恒 $0$／$\le3$ 恒 $\mathbf{128}$／$\le4$ 为 $318,319$）✓✓**）** ✓
- 【**✗$A_x$ 定义性为空**】唐先生之 $A_x:=O_{I_{40}}(c)\cap S$（$c\in S$）**恒空** ✗：实测 $|O(v)\cap I_{40}|{=}\mathbf0$ 对一切 $v\in I_{40}$ ✓✓ —— 因 $d_{\min}{=}4$ ⟹ **码字间无距离-2** ⟹ $O(v)\cap I_{40}{=}\varnothing$ ✓ ⟹ $A_x\times B_x$ incidence **退化** ✗（**定义问题，非数据问题** ✓）。**正确局部对象**：$O_{I_{40}}(x)=\{p,q,c\}$ ✓✓（实测 $|O(x)|{=}3$ 对全 480 点 ✓）
- 【**✓✓修正后局部量**】$B_x:=\{y\notin S:y\ne x,d(x,y){=}2\}$ ⟹ $|B_x|{=}\mathbf{42}$ ✓✓（**全 480 点同值**）：$C(10,2){=}45$ 减 3 个在码中之邻点 $\{p,q,c\}$ ⟹ $42$ ✓✓
- 【**✓✓兼容池（新数据）**】$P_t(x):=\#\{y\notin S:y\ne x,d_S(y)\le t,d(x,y)\ne2,d(y,p)\ne2,d(y,q)\ne2\}$：$t{=}2$：$\{0{:}480\}$ **恒 0** ✓✓（＝C-480 blocking 之重述 ✓）；$t{=}3$：$\{\mathbf{128{:}480}\}$ **恒 128** ✓✓（**新常数**）；$t{=}4$：$\{318{:}160,\ 319{:}320\}$ ✓ ⟹ 若 $x$ 为残点，其余 4 残点度 $\ge3$ ⟹ $\sum\ge1{+}12=\mathbf{13}$ ✓✓（须加 $p,q$ 条件 ✓；由 C-483 最多其一可入 $S_{44}$ ✓）
- 【**✓无 injection**】$|B_x|{=}42\gg|A_x|{=}0$ ⟹ " $B_x\hookrightarrow A_x$ " **不成立**且无意义 ✗ ⟹ **injection 路线废弃** ✓；局部容量之正确载体＝**兼容池 $P_t(x)$** ✓✓（照唐先生"让数据定方向" ✓✓）
- 【**★新现象**】$P_3(x)\equiv128$ 之**恒定**极不寻常 ✓✓ ⟹ 疑为 $\frac12Q_{10}$ 之强对称性／$|D|{=}2$ 之均匀性所致（**下一靶** ✓）
- 【**边界 ✓**】有限穷举 ✓（780 对 ＋ 480 点全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查**：本档与 C-484 各有三词**自命中**（写后才跑 ✗，已据实记过 ✓✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITD1EMPTY-2026-09-28-best-family-has-no-degree1-and-the-familyB-correction.md` ｜ `docs/WITINC38-2026-09-28-Ax-is-empty-by-definition-and-the-compatible-pool-constants.md`

**🔢 C-486（2026-09-28 14:1x · **WITP3128：$P_3(x)$ 之包含排除分解 —— 命题 Q（$d{=}6,8$ 类\ \textbf{为空}，一行 ✓✓）；$d{=}4$ 类 $P_3\equiv\mathbf{128}$ ✓✓；✗\textbf{非仿射}（$Q_7$ 否证）；profile 17 类且计数皆 $160$ 之倍数 ✓✓**）** ✓
- 【**✓✓命题 Q（一行）**】degree-1 ⟹ $|O(x)|{=}3$ ∧ $|O(x)\setminus D|{=}1$ ⟹ $|O(x)\cap D|{=}2$ ⟹ $D\subseteq O(x)$ ⟹ $d(x,p){=}d(x,q){=}2$ ⟹ $d(p,q)\le4$，又 $\ge d_{\min}{=}4$ ⟹ $$\boxed{d(p,q)=\mathbf4}$$ ✓✓ ⟹ **$d(p,q){=}6,8$ 两类为空** ✗（实测 480 实例**全在 $d{=}4$** ✓✓）⟹ 唐先生之三分类实验之**正确答案＝后两类不存在**（非 $\equiv128$ ✗）
- 【**✓✓(2) $P_3(x)\equiv128$**】全 480 实例（皆 $d{=}4$）成立 ✓✓
- 【**✓✓(3) 包含排除精确分解（两型）**】$(|L_3|,|L_3\cap X|,|L_3\cap P|,|L_3\cap Q|,|\cap XP|,|\cap XQ|,|\cap PQ|,|\cap XPQ|)$：**A 型** $(206,36,37,37,15,15,6,4)$ ×**320** ⟹ $110-36+4{=}78$，$206-78{=}\mathbf{128}$ ✓✓；**B 型** $(207,35,38,38,15,15,6,4)$ ×**160** ⟹ $111-36+4{=}79$，$207-79{=}\mathbf{128}$ ✓✓。三球**二重交 $(15,15,6)$、三重交 $4$** 两型皆同 ✓
- 【**✗(4) 仿射性否证**】抽 **40** 实例检验（平移含 0 后对 $\oplus$ 封闭 ⟺ 7 维仿射子空间 ⟺ $|{\cdot}|{=}2^7$）⟹ $$\boxed{\text{40/40 全 }\mathbf{False}}$$ ⟹ $P_3(x)$ **不是** 7 维仿射子空间 ⟹ 唐先生之 $Q_7$ 双射设想**否证** ✗（$128{=}2^7$ 仅为**大小**巧合 ✗）；但仍**刚性** ✓（17 类 profile 每型恒定 ✓）
- 【**✓✓(5) profile 分解（17 类）**】总 $61440=480\times128$ ✓✓；类与计数：$(4,4,4,3){:}9280$／$(6,6,6,3){:}9280$／$(4,4,6,3),(4,6,4,3),(6,4,6,3),(6,6,4,3)$ 各 $6080$／$(8,6,6,3){:}4640$／$(8,6,8,3),(8,8,6,3)$ 各 $2560$／$(4,6,6,3),(6,4,4,3)$ 各 $1600$／$(6,4,8,3),(6,8,4,3)$ 各 $1440$／$(6,6,8,3),(6,8,6,3)$ 各 $960$／$(10,8,8,3){:}480$／$(8,8,8,3){:}320$ ✓。**关键**：全部计数皆 $\mathbf{160}$ 之倍数 ⟹ **A 型/B 型各自 profile 恒定** ✓✓（极强刚性）；另：全部 $d_S(y){=}\mathbf3$（无一例外 ✓）
- 【**★(6) 下一靶**】① $128$ 之**真正来源**（非仿射 ⟹ 疑为**轨道大小**／一条计数恒等式 ✓）；② 求 $P_3(x)$ 之**稳定子**／轨道（$\text{Aut}$ 之某子群 ✓）：$128=|\mathrm{Orb}|$? ✓；③ $r{=}3$ profile ✗
- 【**✓(7) 符号纪律**】本档**不再使用** $A_x$（C-485 已证定义性为空 ✗）；局部对象一律围绕 $O_{I_{40}}(x){=}\{p,q,c\}$ ＋ 三球 $X,P,Q$ ✓✓
- 【**边界 ✓**】有限穷举 ✓（480 实例全量 ✓；40 例仿射检验 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查\ \textbf{确已先跑后写}} ✓✓**（四词皆写入前测得 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITP3128-2026-09-28-inclusion-exclusion-and-the-affine-disproof.md`

**🌐 C-487（2026-09-28 14:2x · **WITMUCONST：四层全通 —— $c$-incidence $\equiv\mathbf5$；$\mu(y)\equiv\mathbf{384}$（\textbf{双计数恒等式} $160{\times}384{=}480{\times}128$）；✓✓✓\textbf{自对偶性} $Y{=}X$（$v{=}160,k{=}r{=}128$）；码字度数 $\equiv12$；owner 三元组皆\textbf{等边} $(4,4,4)$**）** ✓
- 【**✓✓层 0：实例归一**】$\mathcal S:=\{u\notin I_{40}:|O(u)|{=}3\}$、$|\mathcal S|{=}\mathbf{160}$ ✓（＝C-479 谱 $\{3{:}160\}$ ✓）；degree-1 实例 $(x,\{p,q\})$ 共 $\mathbf{480}{=}160\times3$ ✓（每 $x$ 对应其 owner 三元组内 3 个对 ✓）
- 【**✓✓(1) $c$-incidence**】$$\forall x\in\mathcal S:\ |\{y\in P_3(x):c\in O(y)\}|=\mathbf5$$ ✓✓（480/480 同值 ✓）—— **与唐先生猜 64 不符** ✗✓（实值更小更刚 ✓）⟹ $128\neq64+64$ ✗
- 【**✓✓(2) $\mathcal T_x$ 层**】$y\mapsto T_y{=}O(y)$ **单射** ✓✓（160/160 True ✓）；$|T_y|{=}3$ 恒成立 ✓；$|\mathcal T_x|{=}128$ ✓；**码字度数**：$\forall j\in I_{40}:\#\{u\in\mathcal S:j\in O(u)\}{=}\mathbf{12}$ ✓✓（$480/40{=}12$ ✓）⟹ **新刚性**：每特殊点之 owner 三元组两两距离型恒为 $\boxed{(4,4,4)}$ ✓✓ —— **等边三元组** ✓✓
- 【**✓✓(3) 交分布**】$\{|T_y\cap T_z|\}=\{0{:}1028429,\ 1{:}254025,\ 2{:}18026\}$ ✓（总 $1300480{=}160\binom{128}2$ ✓）
- 【**✓✓✓(4) $\mu$ 双计数**】被覆盖之 $y$ 全 $\mu(y){=}\mathbf{384}$ ✓✓ ⟹ $$\boxed{160\times384=61440=480\times128}$$ ✓✓✓ —— **唐先生所期之双计数恒等式成立** ✓✓；等价形式：每 $y$ 恰含于 $\mathbf{128}$ 个 $P_3(x)$ 中 ✓✓
- 【**✓✓✓(5) 自对偶性（本档核心）**】$Y:=\bigcup_{x\in\mathcal S}P_3(x)$ 满足 $$\boxed{Y=\mathcal S}$$ ✓✓ —— 同一批 160 点 ⟹ 160 点上存在**正则自对偶入射结构** $v{=}160,k{=}128,r{=}128$ ✓✓（互补块 $32$ ✓）；**注意** $\lambda{=}128\cdot127/159$ 非整数 ⟹ **不是 BIBD** ✗（但仍极正则 ✓）
- 【**✓✓(6) $128$ 之新解释**】$$\boxed{128=160-32}$$ ✓✓（$\mathcal S$ 自对偶 ⟹ 问题化为"**被排除的 32 个是谁**" ✓✓）；C-486 之仿射否证仍立 ✓（$128$ **不是**仿射大小 ✗）
- 【**✓(7) $(d_p,d_q,d_c)$ 表**】28 个三元组 ✓；$d(y,c)$ 分布 $=\{2{:}2400,4{:}23520,6{:}29760,8{:}5760\}$ ✓；最大者 $(6,6,6){:}7200$ ✓
- 【**★(8) 下一靶**】① **被排除 32 集 $E_x:=\mathcal S\setminus P_3(x)$** 之结构 ✓（**最优先** ✓）；② 160 个等边 $(4,4,4)$ 三元组之设计（$v{=}40$、$b{=}160$、每码字 12 次 ✓）；③ $c$-incidence ${=}5$ 之由来 ✓
- 【**✓(9) 逐条核验**】唐先生 §1（旗标／纯 degree-3 层 ✓✓）、§3（0/1 二分／期待常数 ✓✓ 唯数不符 ✗✓）、§4（四问全执行 ✓✓）、§7（$\mu$ 双计数 **命中要害** ✓✓）**皆正确**；**其未提之自对偶性为本档新发现** ✓✓
- 【**边界 ✓**】有限穷举 ✓（480 实例 ＋ 160 点全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（`特殊点集` 之 1 命中属**空间 A（`ZF-*`：DIM/CAN 门）** ⟹ 标"空间 A 同名，不计" ✗✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITMUCONST-2026-09-28-four-layer-probe-and-self-duality.md`

**🔺 C-488（2026-09-28 14:2x · **WITEX32：C-488 四项全常数 —— $|E_x|{=}32$ 之 $j$-分解 $(5,24,2,1)$；$P_3(x)$ 之 $j$-分解 $(123,5)$；$n_0,n_1,n_2{=}\mathbf{128,29,2}$ 对全部 160 个 $T$ \textbf{恒定}（正则三角关联结构 ✓✓✓）；$\lambda_{uv}$ 分布 $(460,160,160)$**）** ✓
- 【**记账校正（照唐先生 ✓✓）**】$\mu$ 之 $384$ 为**实例计数**（含每 $x$ 的 3 个 owner-pair 实例 ✓）；正确关系 $$\boxed{\#\{x:y\in P_3(x)\}=\mathbf{128}}$$ ✓ ⟹ 「$v{=}160,k{=}r{=}128$ 自对偶」**降级**为 $$\boxed{\text{160 点}\leftrightarrow\text{160 等边三元组之\ \textbf{自然双射}}}$$ ✓（除非构造保持 incidence 之对合 ✗）
- 【**(A) ✓✓$E_x$ 完整 profile**】$E_x=\mathcal S\cap(N_2(x)\cup N_2(p)\cup N_2(q))$ ✓✓（$x\in E_x$ ✓）；16 类（总 $5120{=}160\times32$ ✓）；全部 $d_x\in\{2,4\}$、$d_S\in\{2,3\}$ ✓；首类 $(2,4,4,4,3){:}\mathbf{800}{=}5\times160$ ✓✓（**与 $c$-incidence $\equiv5$ 同位** ✓）；$d_x{=}2$ 占 $59.4\%$ ✓（唐先生"距离-2 排除层"之判断**部分应验** ✓）
- 【**(B) ✓✓$j(y){=}|T_y\cap T_x|$ 分解（两区域皆常数）**】$P_3(x)$：$(j{=}0{:}19680,\ j{=}1{:}800,\ 0,\ 0)$ ⟹ $(123,5,0,0)$/实例 ✓✓；$E_x$：$(800,3840,320,160)$ ⟹ $$\boxed{(5,24,2,1)}$$ ✓✓（合计 32 ✓）；$j{=}3\iff y{=}x$ ✓✓（恰 $160{=}1\times160$ ✓）。**唐先生猜想之判定**：$E_x$ **非纯交型** ✗（含 5 个 $j{=}0$），**但分解恒定** ✓✓
- 【**(C) ✓✓✓$n_i(T)$ 对全部 160 个 $T$ 恒定**】$$\boxed{n_0{=}\mathbf{128},\quad n_1{=}\mathbf{29},\quad n_2{=}\mathbf{2}}$$（$128{+}29{+}2{=}159$ ✓）⟹ **正则三角关联结构**（160 顶点／每个对应等边 $K_3$／$n_i$ 全同）✓✓✓ —— 唐先生所期 association structure **到手** ✓✓ ⟹ **此时谈 stabilizer／轨道顺序正确** ✓
- 【**(D) ✓✓pair multiplicities**】$\lambda_{uv}\in\{0,1,2\}$ ✓✓ 分布 $=\{0{:}460,\ 1{:}160,\ 2{:}160\}$（$\Sigma\lambda{=}480$ ✓）⟹ 比"非均匀（$\lambda{=}8/13$ 非整数）"**更精确**：仅取 0／1／2 三值 ✓
- 【**★(E) 下一靶**】① **由 (C) 求稳定子／轨道**（此时顺序正确 ✓）；② 由 (D)：160 个"重数 2"pair 与 160 个"重数 1"pair 之结构（是否与 $\mathcal S$ 之 160 自然对应 ✓）；③ $E_x$ 之 $j{=}0$ 恰 5 个 ⟹ 与 $c$-incidence $\equiv5$ 是否**同一恒等式之两面** ✓
- 【**✓(F) 逐条核验**】唐先生 §2（$E_x$ profile ✓✓）、§3（$j$ 四分 ✓✓）、§5（$(160,3,12)$ 正则 3-均匀超图／非 Steiner ✓✓）**皆正确**；§4 之"$E_x\stackrel{?}{=}\{T_y\cap T_x\ne\varnothing\}$"**不成立** ✗（但三细分皆常数 ✓✓）
- 【**✓(G) 记账与命名纪律**】$\mu$ 一律标"实例计数"；结构陈述一律用 $\#\{x:y\in P_3(x)\}{=}128$ ✓；「自对偶」**停用** ✗，改用**自然双射** ✓
- 【**边界 ✓**】有限穷举 ✓（160 点 × 全量 ＋ 780 对 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（四词皆 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITEX32-2026-09-28-E-set-j-split-and-regular-triangle-incidence.md`

**🎯 C-489（2026-09-28 14:3x · **WITLAM40：C-489 四项全中 ＋ 交叉正则 —— signature $\equiv(1,2,2)$；$r_{\rm dist}\equiv4$；$H_1,H_2$ 皆 160 边 8-正则 ＋ 三角形自由；交叉正则 $\equiv2$；非 association scheme ✗（部分正则 ✓）**）** ✓
- 【**(A) ✓✓✓签名定理**】$\forall T{=}\{a,b,c\}$：$(\lambda_{ab},\lambda_{ac},\lambda_{bc})$ 排序 $\equiv\boxed{(1,2,2)}$ ✓✓（**160/160** ✓）；推导照唐先生：$n_2{=}2\wedge\lambda{\le}2\Rightarrow\sum(\lambda{-}1){=}n_2{=}2$ ⟹ 三对中恰 2 对 $\lambda{=}2$、1 对 $\lambda{=}1$ ✓✓ ⟹ **唯一区分顶点（distinguished vertex）** ✓✓（唐先生之 $(T,c)$ 标记 **成立** ✓）
- 【**(B) ✓✓✓$r_{\rm dist}\equiv\mathbf4$**】$\forall v$：$r_{\rm dist}(v){=}\mathbf4$ ✓✓（40/40）⟹ $$\boxed{40\times4=160}$$ ✓✓（与 C-487 之码字度数 $\equiv12$ 并列：每码字 4 次区分 ＋ 8 次普通 ✓）
- 【**(C) ✓✓✓$H_2$**】$|E(H_2)|{=}\mathbf{160}$ ✓；$$\text{度数}\equiv\mathbf8\ (40/40)$$ ✓✓✓（唐先生预测 **命中** ✓）；共同邻居分布 $=\{0{:}360,2{:}320,4{:}80,8{:}20\}$；**对角线 $|N_2\cap N_2|{\equiv}\mathbf0$** ⟹ **三角形自由** ✓✓（新）
- 【**(D) ✓✓✓$H_1$**】$|E(H_1)|{=}\mathbf{160}$ ✓；度数 $\equiv\mathbf8$ ✓✓；共同邻居分布与 $H_2$ **完全相同** ✓✓ ⟹ $|N_1\cap N_1|{\equiv}\mathbf0$ ⟹ **亦三角形自由** ✓✓ ⟹ $$\boxed{K_{40}=H_0\sqcup H_1\sqcup H_2,\ H_1,H_2\ \text{双双 8-正则／160 边／三角形自由}}$$
- 【**(E) ✓✓✓交叉正则（新发现）**】$\forall uv\in H_1$：$|N_{H_2}(u)\cap N_{H_2}(v)|{=}\mathbf2$ ✓✓；对称地 $\forall uv\in H_2$：$|N_{H_1}(u)\cap N_{H_1}(v)|{=}\mathbf2$ ✓✓ ⟹ **$H_1$ 与 $H_2$ 互为"共同邻居数为 2"之对偶** ✓✓
- 【**(F) ✗否证：非完全 association scheme**】对角交点对 $H_0$ 对之分布 $=\{6{:}40,12{:}640,14{:}240\}$ ✗ **不恒定**；而 $i{=}1$：$\boxed{(14,0,2)}$ ✓✓ 恒、$i{=}2$：$\boxed{(14,2,0)}$ ✓✓ 恒 ⟹ 结构为**部分正则** ✓，**非 3-类 association scheme** ✗（唐先生"识别 SRG／distance-regular"之期待 ⟹ **否证** ✗）
- 【**★(G) 下一靶**】① $H_1,H_2$ 之**谱**（少数整数 ✓？与 $\mathcal T$ 之谱相合 ✓？）；② $r_{\rm dist}{=}4$ ＋ 度数 $12$ ⟹ 是否诱导 $(40,4,12)$ 设计 ✓；③ $H_1\cong H_2$ ✓（参数全同，是否同构／互补 ✓）
- 【**✓(H) 逐条核验**】唐先生 §A／§B／§C／§D **全中** ✓✓✓；其"降维"判断（$Q_{10}$ 之 160 点 ⟹ 40 码字上两个 160-边图）**成立** ✓✓；唯"SRG／distance-regular"之期待**否证** ✗
- 【**✓(I) 记账**】「自对偶」继续停用 ✗；用**自然双射** ✓；$\mu{=}384$ 标"实例计数" ✓
- 【**边界 ✓**】有限穷举 ✓（160 三元组 ＋ 40 顶点 ＋ 780 对 ＋ 对角交点全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（四词皆 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITLAM40-2026-09-28-signature-theorem-and-the-two-8-regular-pair-graphs.md`

**🔗 C-490（2026-09-28 14:3x · **WITCHOICE：$\mathcal T\cong E(H_1)$ ✓✓；$|W_e|\equiv2$ 且 $w(e)\in W_e$ ✓✓；\textbf{闭环} $r_w{\equiv}\mathbf4$、$r_{\bar w}{\equiv}\mathbf4$、$r_w{+}r_{\bar w}{\equiv}\mathbf8{=}d_{H_1}{=}d_{H_2}$ ✓✓✓；✗ 不能仅由 $H_1$ 重建**）** ✓
- 【**(0) ✓✓✓$\mathcal T\cong E(H_1)$ 双射**】160 triple ↔ 160 条 $H_1$-边（$\lambda{\equiv}1$ 之边只属一个 triple ⟹ **单射** ✓✓）⟹ $$\boxed{X\leftrightarrow\mathcal T\leftrightarrow E(H_1)}$$ ✓✓ ⟹ 每特殊点 $x$ 可视为 $H_1$ 之一条边 ⟹ $P_3(x)$ **可重读为 128 条 $H_1$-边之子集** ✓✓（唐先生之展望 **已可正确定义** ✓）
- 【**(1) ✓✓✓两候选结构**】$W_e{=}N_{H_2}(u)\cap N_{H_2}(v)$ ⟹ $|W_e|\equiv\mathbf2$ ✓✓（160/160）；$w(e)\in W_e$ ✓✓（160/160 True）⟹ "两候选 ⟹ 实选一" **完全成立** ✓✓
- 【**(2) ✓✓✓闭环恒等式**】$$\forall v:\ r_w(v){=}\mathbf4,\quad r_{\bar w}(v){=}\mathbf4$$ ✓✓（各 40/40）；$\sum r_w{=}\sum r_{\bar w}{=}160$ ✓ ⟹ $$\boxed{r_w(v)+r_{\bar w}(v)\equiv\mathbf8=d_{H_1}(v)=d_{H_2}(v)}$$ ✓✓✓ —— 唐先生之"4+4=8 闭环" **精确成立** ✓✓（每码字 8 个"第三点角色"＝8 度 ✓）
- 【**(3) ⚠️$H_1$-边对之 $H_2$-关系表**】共端点 $(480,640,\mathbf0)$／距离 2 $(3920,1280,1280)$／不相交 $(3200,640,1280)$；合计 $\binom{160}2{=}12720$ ✓。**观察**：共端点者**绝不**处 $H_2$-距离 2 ✓（0 例）；但同关系下计数**不恒定** ✗ ⟹ 选择映射 $w$ **不能仅由 $H_1$ 关系重建** ✗（需 $H_2$ 或更多数据 ✓）
- 【**★(4) 下一靶**】① 将 $P_3(x)$ 经 $X\leftrightarrow E(H_1)$ 重读为 **128 条边之子集** 并求**边关系刻画** ✓（是否 $d_{H_1}$／$H_2$-共同邻点条件 ✓）；② $r_w{\equiv}r_{\bar w}{\equiv}4$ ⟹ $w$ 是否诱导 8-正则结构；$H_1\cong H_2$? ✓；③ $H_1,H_2$ 之**谱** ✓
- 【**✓(5) 逐条核验**】唐先生"triple ＝ 一条 $H_1$-边 ＋ 一个共同 $H_2$-邻点"✓✓、"$r_w{=}r_{\bar w}{=}4$\ 双预测"✓✓✓、"$X\leftrightarrow\mathcal T\leftrightarrow E(H_1)$"✓✓"皆中**；唯 §③"少数固定值"⟹ **不成立** ✗（同关系下 $d_{H_2}$ 计数不恒定 ✓）
- 【**边界 ✓**】有限穷举 ✓（160 三元组 ＋ 160 边 ＋ $\binom{160}2$ 边对全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（四词皆 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITCHOICE-2026-09-28-two-candidates-actual-choice-and-the-closed-loop.md`

**🧮 C-491（2026-09-28 14:3x · **WITEDGE：$P_3(x)$ 之边缘级刻画\ \textbf{唯一型}（$\|e_x\cap e_y\|{\equiv}\mathbf0$，128/128 ✓✓✓）；$H_1\cong H_2$ ✓✓✓；$\boxed{A_1A_2{=}A_2A_1}$（\textbf{对易} ✓✓✓）；谱 $=\{8,4^5,(2\sqrt5-2)^2,0^{25},-4^5,(-2\sqrt5-2)^2\}$**）** ✓
- 【**(1) ✓✓✓边缘级刻画（唯一型 × 160）**】对全部 160 个 $x$、全部 $y\in P_3(x)$：计数型**完全相同** ✓✓（仅 1 型 ✓）。$$\boxed{\forall y\in P_3(x):\ e_y\cap e_x=\varnothing}\ ✓✓✓$$（|e_x∩e_y| = 0 于 128/128 ✓）；$w(e_y)\in e_x$ 从不 ✓；$w(e_y)=w(e_x)$ 恰 1 次 ✓；$T_y\cap T_x=\varnothing$ 123、$\ne\varnothing$ 5 ✓（与 C-487 $j$-分解一致 ✓）。**对照 $E_x$**：与 $e_x$ 共端点之 $H_1$-边 $2(8{-}1){=}14$ 条全落 $E_x$ ✓（＋$e_x$ 自身 ⟹ 15 ✓）；$E_x$ 另含 **17 条不相交边** ✓ ⟹ "不相交"为**必要非充分** ✓✓
- 【**(2) ✓✓✓$H_1\cong H_2$**】显式同构 $\phi$ 求出（networkx VF2 ✓）；$\phi$ 把 $H_1$-边映为 $H_2$-边 ✓✓（$\lambda{=}2$，160/160 ✓）；**但 $\phi$ 不保 $w$** ✗（$\phi(w(e))$ 非 $\phi(e)$ 之 $H_2$-共同邻点，0/160 ✗）⟹ 唐先生告诫 **正确** ✓✓
- 【**(3) ✓✓✓谱（完全相同 ＋ 干净代数数）**】$\text{Spec}=\{8^1,\ 4^5,\ (-2{+}2\sqrt5)^2,\ 0^{25},\ (-4)^5,\ (-2{-}2\sqrt5)^2\}$ ✓✓（涉 $\sqrt5$ ✓，疑与五边形几何相关 ✓）
- 【**(4) ✓✓✓矩阵关系 ＋ 对易**】$(A_1^2)_{H_2}{\equiv}2$、$(A_2^2)_{H_1}{\equiv}2$、$(A_1^2)_{H_1}{\equiv}0$、$(A_2^2)_{H_2}{\equiv}0$、对角 ${\equiv}8$ ✓✓ ⟹ $A_2^2{=}8I{+}2A_1{+}B_0$、$A_1^2{=}8I{+}2A_2{+}B_0'$（支集 $\subseteq H_0$ ✓）；**✗否证**：$B_0$ 在 $H_0$ 上取值 $\{0{:}400,2{:}320,4{:}160,8{:}40\}$ **不恒定** ⟹ 非标量 ✗；$B_0\neq B_0'$ ✗。$$\boxed{A_1A_2=A_2A_1}\ ✓✓✓\ \big(\text{可同时对角化 ✓}\big)$$ 且 $(A_1A_2)_{uv}\in\{0,2\}$ ✓（2 于 $1280{=}40\times32$ 位置 ✓ ⟹ **每顶点 32 个乘积位置**，与 $128{=}160{-}32$ 之 32 呼应 ✓）
- 【**★(5) 下一靶**】① 由对易＋同谱 ⟹ 求**同时对角化基／商代数**；$A_2=P(A_1)$? ✓；② **17 条"不相交却在 $E_x$"之边之判据** ⟹ **128 之真正来源所在** ✓✓（最优先）；③ 是否存在保 $w$ 之第二同构 $\phi'$ ✓
- 【**✓(6) 逐条核验**】唐先生 §3（三分／14 条共端点 ✓✓✓）、§2（有限关系型 ⟹ **成立** ✓✓✓）、§6（$H_1\cong H_2$ ⟹ **是** ✓✓✓）、§7（$A^2$ 形式 ✓✓ 唯 $B_0$ 非标量 ✗）**皆中**；顺序锁定（edge-level → 同构 → 谱 → 矩阵关系）**已照办** ✓✓
- 【**边界 ✓**】有限穷举 ✓（160×128 ＋ 780 对 ＋ VF2 同构 ＋ 40×40 谱 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（`共同谱` 之 3 命中属**空间 A** ⟹ 标"空间 A 同名，不计" ✗✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITEDGE-2026-09-28-edge-level-characterization-and-the-commuting-algebra.md`

**🔪 C-493（2026-09-28 14:3x · **WIT17：disjoint-17 精确分解 —— $32{=}15{+}17$ ✓✓✓；$(k_1,k_2)$ 4 格 P₃-only／2 格 E-only；\textbf{完整 signature 228/229 纯} ✓✓✓（仅 1 类混合 ✗）；$k_2{=}3\Rightarrow$ 必属 $E_x$ ✓✓**）** ✓
- 【**✓✓✓精确重写（照唐先生）**】$$32=\underbrace{15}_{e_y\cap e_x\ne\varnothing}+\underbrace{17}_{e_y\cap e_x=\varnothing,\ y\notin P_3(x)}$$ ✓✓✓；$E_{\rm disj}$ 总计 $2720=160\times\mathbf{17}$ ✓
- 【**✓✓(1) $(k_1,k_2)$ 分布**】$k_i{:=}\#\{(a,b)\in e_x\times e_y:R(a,b){=}i\}$：**P₃-only** $(1,0),(1,1),(2,0),(2,1)$ ✓✓；**E-only** $(0,3),(1,3)$ ✓✓；混合 $(0,0),(0,1),(0,2),(1,2)$ ✗ ⟹ $$\boxed{k_2{=}3\Longrightarrow\text{必属 }E_x}\ ✓✓;\quad k_1{\ge}1\wedge k_2{=}0\Longrightarrow\text{必属 }P_3✓✓$$
- 【**✓✓(2) $(k_1,k_2,j)$**】13 格中 **9 格纯** ✓✓（含 $(2,0,0),(2,0,1),(2,1,0)$ 等 P₃-only ✓；$(0,3,1),(1,3,1)$ 为 E-only ✓✓）；$P_3$ 仅 $j\le1$ ✓；$E$ 含 $j{=}2,3$ ✓
- 【**✓✓✓(3) 完整 signature**】$\Sigma{=}(R(p,u),R(p,v),R(q,u),R(q,v);R(c,u),R(c,v);R(z,p),R(z,q);R(c,z))$ ⟹ **229 类，228 纯** ✓✓✓（**99.6% 分离** ✓✓）⟹ 唐先生之"有限局部判据"**几乎达成** ✓✓。**唯一混合类** $\Sigma_0{=}(0,0,0,0;2,2;2,2;0)$：$E{=}160$、$P_3{=}480$ ✗（每 $x$ 贡献 3 实例 ✓）
- 【**✓✓(4) 17 之完全分解**】$(0,0){:}1,\ (0,1){:}4,\ (0,2){:}2,\ (0,3){:}4,\ (1,2){:}2,\ (1,3){:}4$ ✓ ⟹ $$\boxed{17=1+4+2+4+2+4}$$ ✓✓（**17 已拆成 6 个局部型** ✓✓）
- 【**✓✓(5) 记账纪律**】唐先生之警示**正确** ✓✓：**不得**把 $E_x$ 之 32 点 $j$-分布与 17 边直接相减 ✗（须保持 C-490 对应 ✓）；本档严守 ✓ 且实测自洽 ✓
- 【**★(6) 下一靶**】① 拆 $E_{\rm disj}$ 之 6 型与 $x$ 之几何关系 ✓；② **唯一混合类 $\Sigma_0$ 之细分**（加**距离-2 球三重交**或 $\mathrm{Aut}$ 轨道 ✓）；③ 若 17 全定 ⟹ 目标升级为 $128{=}145{-}17$ 之 **P1 结构定理** ✓✓
- 【**✗(7) 余留**】唯一混合 signатуре 表明单凭 $H_0/H_1/H_2$ 之九元关系**不足以完全分离** ✗ —— 须再加一量（疑为环境 $Q_{10}$ 量 ✓）
- 【**边界 ✓**】有限穷举 ✓（160×145 ＋ 229 类全量 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（`交叉型`(`E183-*`)／`判别表`(`p28b2c-*`) 皆**空间 A** ⟹ 不计 ✗✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WIT17-2026-09-28-disjoint-17-decomposition-and-the-signature-separation.md`

**📐 C-494（2026-09-28 14:4x · **WITSIGMA0：四二阶标量容量\ \textbf{全不分离} ✗；$\Pi$-profile\ \textbf{完全分离 $\Sigma_0$} ✓✓✓（共同类 0；$E$ 一类、$P_3$ 三类）；⟹ \textbf{229 类全判别}**）** ✓
- 【**✗(1) 四标量全不分离**】$\Sigma_0$ 之 640 实例（$E{=}160,P_3{=}480$ ✓，每 $x$：$E{:}1,P_3{:}3$）：$T_0{\equiv}\mathbf4$、$T_c{\equiv}\mathbf0$、$T_z{\equiv}\mathbf1$、$T_{cz}{\equiv}\mathbf0$ —— **四量皆纯常数 ⟹ 判别力饱和** ✗（唐先生之顺序"先四标量、混再做 $\Pi$" **正确** ✓✓）
- 【**✓✓✓(2) $\Pi$-profile 完全分离**】$\pi(w){=}(d(w,c),d(w,z),d(w,u),d(w,v))$，$w\in B$，$\Pi$ 为 4 元多重集：**$E$ 唯一类** $\Pi_E{=}\big((4,2,6,6),(4,4,\mathbf6,\mathbf6),(4,4,\mathbf6,\mathbf6),(4,6,6,6)\big)$（**中间两点对称** ✓）；**$P_3$ 三类**（中间两点**不对称** ✗）：P1 $(6,4)/(6,8)$、P2 $(4,8)/(8,4)$、P3 $(4,6)/(8,6)$（各 160 ✓）⟹ $$\boxed{\text{共同 profile}=\mathbf0/4\ ⟹\ \Sigma_0\ \text{被 }\Pi\ \text{完全分离}}$$ ✓✓✓（**3:1** ✓ —— 唐先生 §8 之"3:1 疑三重对称来源" **得强支持** ✓✓）
- 【**✓✓✓(3) 总判据完备**】229 类中 228 类由**一阶 signature** 分离（C-493 ✓✓✓）；余 $\Sigma_0$ 由**二阶 $\Pi$** 分离 ✓ ⟹ $$\boxed{\text{全部 229 类均可有限局部判别}}$$ ✓✓✓ —— **P1-S0 目标达成** ✓✓；且**无需 $\mathrm{Aut}$**（唐先生 §7 之顺序前两层内已解决 ✓✓）
- 【**★(4) 下一靶**】① 由 $\Pi_E$ 之**对称性**（中间 $(6,6),(6,6)$）与 $P_3$ 三类之**不对称**求其**组合意义**（疑：$u,v$ 交换对应一对合 ⟹ 3:1 为轨道结构 ✓✓）；② 由全判别争取 $128{=}145{-}17$ 与 $17{=}1{+}4{+}2{+}4{+}2{+}4$ 之**结构定理** ✓✓；③ 15 之机制是否同样由 $\Pi$ 型刻画 ✓
- 【**边界 ✓**】有限穷举 ✓（640 实例 ＋ 全 $\Pi$ ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（四词皆 0 ✓）；**不作路线裁定** ✗（V290）
- 档：`docs/WITSIGMA0-2026-09-28-second-order-capacity-saturation-and-the-Pi-profile-separation.md`

**🌉 C-495（2026-09-28 14:4x · **WITBRIDGE：桥之三步 ✓✓（$23200{=}160{\times}145$；$128/17$ 每 $x$ 恒定；类内 0 混合）＋ ✗✗\textbf{重要更正}：判据\textbf{不可迁移}（留出验证 320 错／2.76%）；C-494 之"完全分离"实为 \textbf{census 级}**）** ✓
- 【**✓✓(1) 桥之第一步（集合恒等，逐 $x$ 精确）**】disjoint 总数 $\mathbf{23200}{=}160\times145$ ✓；$P_3{=}\mathbf{20480}{=}160\times128$ ✓；$E_{\rm disj}{=}\mathbf{2720}{=}160\times17$ ✓；$$\forall x:\ |P_3(x)\cap\text{disjoint}|{=}\mathbf{128},\ |E_{\rm disj}(x)|{=}\mathbf{17}$$ ✓✓（160/160 无例外）⟹ $$\boxed{145=128+17}$$ 逐 $x$ 成立 ✓✓
- 【**✓✓(2) 类内纯度（全集）**】以 $(\text{sig},\Pi_{\rm full})$ 为 key：类数 $\mathbf{7332}$、**混合类 $\mathbf0$** ✓✓✓；但 $\Pi_{\rm full}$ 含**实例特有距离值** ✗
- 【**✗✗(3) 可迁移性检验（本档核心否证）**】留出验证（前 80 个 $x$ 建映射、后 80 个检验）：$(\text{sig},\Pi_{\rm full})$：$\mathbf{3167}$ 错（$\sim73\%$ ✗✗）；粗判据（九元 signature ＋ 对称型）：$\mathbf{320}$ 错（$97.24\%$ ✗）⟹ $$\boxed{\text{判据\ \textbf{不可迁移}}}$$ ✗✗。错量读法：$320{=}2\times160$ ⟹ 每 $x$ 恰 2 处，**集中于 $\Sigma_0$** ✓（其分辨**未**由粗型完成 ✗）
- 【**✗✓(4) 对 C-494 之重要更正**】C-494 称"$\Sigma_0$ 被 $\Pi$ 完全分离" ⟹ **须限定**：所用 $\Pi$ 含实例特有值 ✓；**粗型（对称型）下 $\Sigma_0$ 仍混合** ✗✓：混合类 $=((0,0,0,0;2,2;2,2;0),\text{"sym"})$ 同时含 $E$ 与 $P_3$ ✗ ⟹ "中间两点对 $(u,v)$ 对称" **不**等价于 $E$ ✗ ⟹ C-494 之"229 类全判别"**降级为 census 级纯类** ✗✓ —— 是**精确普查** ✓，尚**非**可迁移之**局部判据** ✗。唐先生"不要偷步"之警告 **正中** ✓✓✓
- 【**✓✓(5) 桥之四步状态**】① $17$ 类恰对应须扣除对象 ✓✓（$1{+}4{+}2{+}4{+}2{+}4{=}17$）；② 无遗漏 ✓✓（23200 精确）；③ 无重复 ✓✓（六型 $(k_1,k_2)$ 互异 ⟹ 两两不交）；④ 分类 ⟹ 全局关系 **未达成** ✗（不可迁移 ⚠️）⟹ **局部"门"已过 ✓✓，桥④未搭** ✗（与唐先生判断一致 ✓✓）
- 【**★(6) 下一路线**】① 以 $\Pi$ 之**配对型**（$(c,z)$ 距离与 $(u,v)$ 距离之配对模式）替代原值 ✓；② 引入 $A_3/H_3$ 边级关系（C-492 ✓）；③ 三重 $N_2$ 之**粗多重集**（取型不取值 ✓）；④ 或承认 $P_3$ 定义依赖环境 $Q_{10}$ ⟹ 桥④须以**环境量**立论 ✓
- 【**边界 ✓**】有限穷举 ＋ 留出验证 ✓（23200 全量 ＋ 11600 检验 ✓）；未上 SDP/SAT ✗；未开门② ✓；未改门 ✓；**词回查确已先跑后写 ✓✓**（`判据更正` 之 3 命中属**空间 A** ⟹ 不计 ✗✓）；**不作路线裁定** ✗；**明确否认** $145{-}17{=}128$ 已是 P1 定理 ✗✓（V290）
- 档：`docs/WITBRIDGE-2026-09-28-bridge-three-steps-and-the-transferability-correction.md`
