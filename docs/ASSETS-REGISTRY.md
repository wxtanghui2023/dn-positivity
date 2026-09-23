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

## 【定点更新·`NEG-REGISTER-1`】类级负面判定的统一定级 ＋ 引用纪律（2026-09-18 20:1x）

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
