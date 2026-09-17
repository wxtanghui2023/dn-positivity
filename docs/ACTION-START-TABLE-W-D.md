# 🎯 **行动起点表：W1–W12／D1–D10 逐项五列**

> 依唐先生 12:19 指令（此表＝后续行动起点）✓｜**已查地图** ✓（`CLOSED-ROUTES-MAP`／`MASTER-*`／`WALLS-DIFFICULTIES-LEDGER` C-27）
> **五列**：难点 ｜ 突破点 ｜ 目前进展 ｜ 文献最新进度位置 ｜ 目前技术手段的局限
> **证据等级**：`[原]` 逐字原文｜`[档]` 我方档案｜`[未核]` 未核 ⟹ 不得当事实引用

---

## A. 墙体 W1–W12

| # | 难点 | 突破点 | 目前进展 | 文献最新进度位置 | 技术手段局限 |
|:--|:--|:--|:--|:--|:--|
| **W1** $\beta$墙 | 检测 $\ne$ 排除；含 $\beta$ 的量要么循环、要么自适应 | ①**反证＋整数性**：造 $A(X)=M(X)+E_\rho(X)\in\mathbb Z_{\ge0}$，$\beta>\frac12\Rightarrow A\notin\mathbb Z_{\ge0}$；②**增长率**替代位置：同一量既有纯算术上界又有离线零点下界 | ⚠️**勘误**："$\beta$ 盲"措辞过强 ⟹ 正确＝**线性通道饱和＋提取需无界精度/一致性**（`CLOSED-ROUTES-MAP:883` 自查勘误）`[档]`；Rigidity Gap 已定位 | Lamzouri（$\beta$ 盲核$\iff$无条件／$\beta$ 敏感$\iff$条件性）`[档]`；Robin ⟹ RH 是 $\Pi_1$ ⟹ 有限见证 `[档]`；Connes 2026（$\beta$-盲）`[档]` | $E_\rho$ **不得**以显式公式定义（否则循环）；整数性约束常被局部条件吸收；上/下界需**独立**来源 |
| **W2** 承重墙 V181 | $T\log T$ ＋ Weil 正性；局部算术 $\not\Rightarrow$ 全球谱定位 | 找 $\Phi$ **同时避开 E1–E4**（＝`V211 §5` UNINSTANTIATED） | STRATEGY §1 断言"四者同一道墙三面" ⟹ **已降级为待核（未证）**；E1–E4 四封锁线建成 `[档]` | Weil 显式公式族；Bombieri 2000；Connes 2026 `[档]` | 唯一已知桥＝显式公式 ⟹ 值面；正性路线循环 |
| **W3** 值面墙 V283 | 桥必经值面（未证）；arg principle ⟹ 全素数求和＋archimedean | ①Track II 完备性证明；②**泛函分析有界性**：找 $\|Tf\|_Y\le C\|f\|_X$ 使 $\beta>\frac12\Rightarrow\|Tf_\beta\|_Y=\infty$ | E1–E4 判据建成；**7 类候选对表 ⟹ 无逃逸者**（`V292` 步骤 3）`[档]` | `[未核]`（需专门检索算子有界性/插值文献） | 易落入已有正性判据（换语言）；$T$ 须由整数构造（不得塞 RH 判据） |
| **W4** A-leak V172 §5a | archimedean 项 ⟹ 需**全体素数** | **离散差分滤波**：$\Delta_h^kA_{\rm ar}$ 快衰而有限素部分不衰 ⟹ $\Delta_h^kA=$ 纯有限算术信号$+o(1)$ | `V172 §5a` 定位 `[档]`；`E119` 逐字：窗口**不能平均相位**（相位跨窗变化 $O(1)$）⟹ 局部 $L^2$ 不能绕开点态墙 `[档]` | `[未核]`（有限差分/小波/vanishing moments 文献） | Mellin 分解已试；archimedean 与零点信息纠缠 |
| **W5** 正性循环 | Weil 正性 $\iff$ RH | **SOS／Gram／完全正分解**：直接问"离线零点能否制造负方向" $Q(a)<0$ | POS1/POS2 封 `[严格]`；CCLM17 Cor.14 ⟹ $c_1^*=0.7532960$ **最优饱和**；V316 冻结 `[档]` | CCLM17；Conrey–Ghosh；Bombieri 2000；Weil 1952 | ⭐ `E119 §④`：$K_Y$ 是 Gram ⟹ 半正定 ⟹ positivity 只给**下界**；**上界须对偶正性**（Beurling–Selberg 型 majorant）`[档]` |
| **W6** SUPPORT-1 | $\text{support}>1\iff$ prime-pair；$X>T$ 后离对角不被对角支配 | ①**只打短差**＋特定加权泛函；②**平方自由实验**（二分判定）；③**对偶正性 majorant** | ⭐**Prop 5.4 泛函逐字入仓**：$D／O_1／O_2$ 分块、$a_n=\Lambda(n)/\sqrt n$、**bandwidth 烧进窗口** $|x|<T$ `[原]`；五项武器判定：**筛＝C(parity)｜色散＝C(方向错)｜大筛＝C(已用尽)｜divisor-switching＝未定｜对偶正性＝唯一方向正确** `[档]`；平方自由忠实设计完成 | Zeta23/Alpöge–Furman 2026 §7.2(a)(e) `[原]`；**GM 2026 Annals** 大值 Thm 1.1（窗口 $N^{7/10}\lesssim V\lesssim N^{8/10}$）`[原]`；Montgomery 1973／GM87（support$>1$）；DFI97→BC18（$1/48\to1/20\to17/33$）；Tril I/II（Wright 2026，range-local）；2601.00292 **已撤回** | 三项武器已判 **C**；唯一活口＝**对偶正性 majorant**；parity barrier→横坐标的接链**不存在**（`V255 §5(b)`） |
| **W7** 相位墙 ACA1 | 单尺度平均相位盲 | **离散 discrepancy**：证任何异常 $\beta$ 需同时满足一组**无法同时满足**的相位区间条件 | ⑫关修正：真墙但**不在 RH 路径** `[档]` | `[未核]`（Erdős–Turán／discrepancy 文献） | 判决可能误杀（需复核）；与 W6 边界须分清 |
| **W8** 信息墙 FPCA | 有限算术数据 vs 全局信息 | **信息量上界**＋**非-cylinder witness**（仍须有限算术规则可算） | cylinder barrier（V271-A）；FPCA **撤回**（输出信息量应为 $(x/\log x)\log\log x$）；parity barrier 登记 `V254`／`V255` `[档]` | Selberg／Rosser–Iwaniec parity barrier `[档]` | "非-cylinder"与"有限可算"张力 ⟹ 可能**不存在**该类 witness |
| **W9** 复杂度墙 | （原假设：素性难判） | — | ⚪**已撤回（不成立）**：AKS／筛法 ⟹ 低复杂度位置决定器 `[档]` | AKS 2002 | 无 |
| **W10** 散射钉住 G20 | 四线全不足；非自伴共振 ⟹ 无 $\mathrm{Re}\,\rho$ 夹逼 | **resolvent growth ＋ pseudospectrum ＋ commutator**：找 $[T,T^*]=C$ 具严格符号；争取双向 resolvent 障碍 | 第二次总封口；G17 查明 Selberg $1/4$ 来源（自对偶参数化＋谱定理＋算术输入）；G19 $\zeta=$ 散射行列式 $\phi(s)$ `[档]` | `[未核]`（Lax–Phillips／散射理论） | 非自伴无谱定理；**虚 Airy 反例**表明数值域与谱可完全脱钩 |
| **W11** L1 非自伴谱刚性 | 五族只给半平面／扇形／实轴／**竖条空集** | 第六族？（⚠️ 开案前必查 G11／G12 防重） | **L1 = NO-GO**（2026-09-10 文献审计完成）；硬反例：虚 Airy $-d^2/dx^2+ix$ `[档]` | numerical range／Krein–Pontryagin／J-self-adjoint 五族 `[档]` | 转译 $\mathrm{Re}\,\rho=\frac12$ 必先令谱参数 $=\gamma$ ⟹ **HP 循环** |
| **W12** $2/3$ 与 $0.682$ | bandwidth-one 证书类天花板 | —（**＝W6**，不再单独开案） | 已并入 W6；Montgomery–Taylor window ⟹ $0.6725$；$0.7532960$ 最优饱和 `[档]` | Zeta23 §7.2 `[原]`（**自用词 "bandwidth-one ceiling"**；"certificates ≈ 0.682"） | 常数优化不改变结构（`STRATEGY §6①` 明文不做） |

---

## B. 难题 D1–D10

| # | 难点 | 突破点 | 目前进展 | 文献最新进度位置 | 技术手段局限 |
|:--|:--|:--|:--|:--|:--|
| **D1** 相位均匀性 | 转换的关键步是否需要"均匀性 $A\to0$" | **逐处核清**：哪些转换仍需要、哪些已撤回 | Burnol 逐字 "What is essential nevertheless is **the uniformity as $A\to0$**"（三次独立出现）`[档]`；`CONV2` **局部撤回**（"在线部分不需要任何分散界"）；`CONV3` **进一步撤回**（"不需要零密度定理／分散界／均匀性"）`[档]` | Burnol `[档]` | 撤回与出现**并存** ⟹ 必须逐处核，不能整体判死或整体采信 |
| **D2** 灾难消解 | 方法层：**消解式模式**（只产出负结果与等价关系，无生成步） | **生成步从哪来**（今日结论：不能靠继续审计） | 数值层已解（float 灾难性抵消 $\to$ 高精度）`[严格]`；`E160` 诊断 `[档]`；与今日 `Audit≠Discovery` **同一条** | — | 审计机器**不能**生产路线；"消解式"是复发模式 |
| **D3** 振荡项消解 | $\gamma$ 层振荡项；**端点障碍** | ①**稀疏主导 witness**（$|S|\ll T^\epsilon$ 但已超其余项上界）；②NS 式受控终止；③周期块法 | $M(T)=O(1)\iff$ **Lindelöf 级**；`E119`：窗口不能平均相位 ⟹ 化为**点态** $|\Delta(N,\sqrt N)|=o(\sqrt N)$，而 **RH 只给 $O(\sqrt N\log^2N)$ ⟹ 差一个 $\log^2$**（与 Bazzanella 一致）`[档]`；PAPERA 四步：①④完成、②消解、③两区制 `[档]` | Bazzanella（RH 不足）；Hejhal 1994（**RH 条件**）；RS 1996；Montgomery 1973 | 局部 $L^2$ **不能**绕开点态墙；所需增益为 $\log^2$ 级（RH 本身不足） |
| **D4** 相位感知聚合缺口 | 谱系数**不可和** $M_R=\sum|b_j|=\infty$ | 相位感知聚合（**可能 $\iff$ support$>1$**） | `E123` 量化第二证明 `[档]`；`E117`／`E121` 已关；**与 W6 同址** | — | 需零点对相关 ⟹ **回到 W6**（不必单独开案） |
| **D5** moving-edge | 有限惯性**不**向无限维传输 | **跨尺度符号不变性**：嵌套窗 $[X,2X]／[2X,4X]／[4X,8X]$，使 $F(2X)-F(X)$ 有**严格符号** | P27–P33 定位 `[档]` | — | 需跨尺度符号不变性，**尚未构造** |
| **D6** K2-E″ | "是而空"型：只提供大小界／可和性／截断界而**不改覆盖秩** | 找**能改秩**的输入类型 | 两次独立确认（`V113`／`V114`）⟹ **Input strength $\ne$ selection strength** `[档]` | — | 尚未找到"改秩"输入 ⟹ 大量候选被判 NO-GAIN |
| **D7** 负结果三关 | 负结果的有效性判据 | — | 三关建成：**Gate 1 方向／Gate 2 秩／Gate 3 截断** `[档]` | — | 三关是否**穷尽**未证 |
| **D8** 三个 $\frac12$ | 代数中点／函数方程中心／RH 刚性不得混用 | — | 纪律项已立（陷阱 T6）`[档]` | — | 混用是本项目高发错误 |
| **D9** 对象混淆 | Selberg zeta 零点 $\ne$ 散射共振 $\ne$ ζ 零点；$\mathrm{GL}(n)$ $L\ne$ ζ | — | 纪律项已立（陷阱 T5）`[档]` | — | 同上 |
| **D10** $\tau$／相位来源缺口 | char 0 尺度动力学需**同时**产生 modulus 与 phase | **极化 Hodge 结构／period domain**（"极化后剩余的 unitary 自由度"＝period point） | 关闭"寻找 $\tau$" `[档]`；`AOB2` 登记约束（不借用显式公式／Weil／HP；**无 $\frac12$ 输入**）；`DISCOVERY-R3` 判定 **"算术无内生动力学" ⟹ D1=0** `[档]`；`ABD-1` 等式吸引子已实算（含先杀判据）`[档]` | Hodge 理论／period domain `[档]` | 算术**无内生动力学** ⟹ 路径依赖只能来自**观察者压缩**；$1/2$ 来源问题（P2-1：乘法流阈值＝1，$1/2$ 来自 completion） |

---

## C. 由本表直接得到的**优先行动序**（TACTICAL ATTACK）

$$\boxed{\text{W6}（\text{唯一活口＝对偶正性 majorant}）\to \text{W5}（\text{同族工具}）\to \text{W4}（\text{离散差分，自足}）\to \text{W8}（\text{信息上界，可判}）\to \text{W1}\to \text{W10/11}}✓$$
$$\text{并行}：\text{D3}（\text{稀疏 witness}）\ \big|\ \text{D5}（\text{跨尺度符号}）\ \text{—— 两者}\ \textbf{自足可算}✓✓$$
$$\text{须先补的文献位}（本表标}\ `[未核]`\text{）}：\text{W3 算子有界性}／\text{W4 有限差分}／\text{W7 discrepancy}／\text{W10 散射理论}✓$$
