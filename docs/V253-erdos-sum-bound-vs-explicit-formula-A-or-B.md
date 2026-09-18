# V253 · **Erdős 和界 vs 显式公式：A/B 判定** —— ⭐⭐⭐ **关键恒等式（本档推导）**：$\frac{1}{a\log a}=\int_1^\infty a^{-s}ds$ ⟹ **Erdős 和 $=\int_1^\infty D_A(s)\,ds \Longrightarrow$ 它本质上是"$\boldsymbol{\sigma=1}$ 边界"对象** ✓✓✓；⭐⭐ **方法实际输入＝Mertens 型估计 ＋ 权次不变性 ＋ $\eta$ 单调性 ⟹ 全部在 $\sigma=1$／值面、全部不含零点信息** ⟹ **判定＝非 A，且强于 B**（该界**不被显式公式蕴含**，因为其输入**严格弱于**显式公式）✓✓✓；⭐⭐⭐ **更强：$\sigma=1$ 的位置不是技术偶然，而是被"尾和有限性"强制** —— 同一形状的 $\sigma=\frac12$ 版本**不存在**（尾和发散）⟹ **想把它搬到 $\frac12$ 必须引入抵消输入＝零点位置信息 ⟹ 正是 `V162`／`V219`／`V235`-A 那堵墙** ✓✓✓✓

> 委托 ✓ 唐先生 2026-09-15 21:59：**"继续"**（承接 V252 §4 唯一可查开口：**判定情形 A（被显式公式蕴含）还是情形 B（不被蕴含）**）✓✓
> 纪律 ✓ 未用 RH 作推导（只在"若把它搬到 1/2"处引用本项目已有结论 `V219`）✓；未跑 Lean ✓；**零数值** ✓；**本档含一处对 V252 §4 的自我措辞更正**（§8）✓｜编号 ✓ **V253**

---

## §1 待判问题（V252 §4 的精确化）

$$\text{设}\ E(A;x):=\sum_{\substack{a\in A\\ a>x}}\frac{1}{a\log a};\qquad \text{#1196 所证}：\sup_{A\ \text{primitive}}E(A;x)\le 1+O\!\left(\frac1{\log x}\right) ✓$$
$$\textbf{A}：\text{该界由显式公式（＋标准解析数论）}\textbf{蕴含} \Longrightarrow \text{`V188` 饱和} \Longrightarrow \text{无新信息} \Longrightarrow \text{封}$$
$$\textbf{B}：\text{不被蕴含} \Longrightarrow \text{新的无条件输入} \Longrightarrow \text{命中 `V201` 开口}$$
$$\text{⚠️ 但要判 A/B，须先问：}\textbf{该界"住在"}\ \sigma\ \textbf{平面的哪里？}$$

## §2 ⭐⭐⭐ **关键恒等式（本档推导）—— 它住在 $\sigma=1$**

$$\text{对}\ a>1：\qquad \int_1^\infty a^{-s}\,ds=\left[\frac{a^{-s}}{-\log a}\right]_{s=1}^{s=\infty}=\frac{a^{-1}}{\log a} \qquad\Longrightarrow\qquad \boxed{\frac{1}{a\log a}=\int_1^\infty a^{-s}\,ds} ✓✓✓$$
$$\Longrightarrow\ \text{（正项、Fubini 合法）}\qquad \sum_{a\in A}\frac{1}{a\log a}=\int_1^\infty\Big(\sum_{a\in A}a^{-s}\Big)ds=\boxed{\int_1^\infty D_A(s)\,ds}\quad\text{其中}\ D_A(s):=\sum_{a\in A}a^{-s} ✓✓✓$$
$$\Longrightarrow \textbf{Erdős 和 ＝ A 的 Dirichlet 级数在}\ [1,\infty)\ \textbf{上的积分} \qquad\Longrightarrow\qquad \textbf{它的临界下界是}\ \boxed{\sigma=1} ✓✓✓$$

$$\textbf{三点直接推论}：$$
$$\qquad \text{(i)}\ \text{权}\ \frac{1}{a\log a}\ \textbf{恰是}\ \sigma=1\ \text{边界的"临界权"}（\text{再降一点就发散} → \text{见 §6）} ✓$$
$$\qquad \text{(ii)}\ \textbf{von Mangoldt 权}\ \nu_\Lambda\ \text{的 Dirichlet 级数是}\ -\zeta'/\zeta,\ \text{其横坐标亦为}\ 1 ✓$$
$$\qquad \text{(iii)}\ \Longrightarrow \textbf{整条方法}\ \textbf{全在}\ \sigma=1\ \text{这一层} \text{——即本项目 `V235`-A 所称的}\ \textbf{"密度坐标"层} \text{（无条件、零知识）} ✓✓✓$$

## §3 方法**实际用到**的解析输入（原文所列，逐条核对）

$$\text{原文（arXiv:2605.00301，与 LeanMarathon 复述一致）}：\text{证明使用}\ \textbf{(a) doubly-harmonic 权在 von Mangoldt 链下的次不变性};\ \textbf{(b) Mertens 型估计};\ \textbf{(c) Dirichlet eta 函数的单调性} ✓✓$$
$$\qquad \textbf{(a)}\ \text{次不变性＝偏序上权的一条}\textbf{单边不等式}（\text{纯组合—测度内容，不含解析数论输入}）✓$$
$$\qquad \textbf{(b)}\ \text{Mertens 型}：\sum_{p\le x}\frac1p=\log\log x+B+O\!\left(\frac1{\log x}\right) \quad\Longrightarrow\quad \textbf{形状与本文误差}\ O(1/\log x)\ \textbf{完全同阶} ✓✓✓$$
$$\qquad \qquad ⚠️\ \text{Mertens 型定理}\ \textbf{等价于 PNT 的弱形式}，\ \textbf{无条件成立}，\ \textbf{与 RH 无关};\ \text{它是}\ \sigma=1\ \textbf{密度面} \text{的信息，}\textbf{不是零点位置信息} ✓✓$$
$$\qquad \textbf{(c)}\ \eta(s)=(1-2^{1-s})\zeta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}\ \text{在实}\ s>0\ \text{上的单调性} \Longrightarrow \text{纯}\ \textbf{实变—值面} \text{陈述} ✓$$
$$\Longrightarrow \textbf{全部三项输入：}\textbf{零零点侧数据};\ \textbf{全部是}\ \sigma=1\ \text{／值面材料} ✓✓✓$$

## §4 ⭐⭐ **判定：非 A，且强于 B**

$$\textbf{结论}：\boxed{\text{情形}\ \textbf{A}\ \text{不成立};\ \text{而且不是"恰好不被蕴含"，而是}\textbf{"输入严格弱于显式公式"}} ✓✓✓$$
$$\qquad \text{理由：显式公式的内容是}\ \textbf{零点位置}（\sum_\rho x^\rho/\rho\ \text{项}）;\ \text{而本方法}\ \textbf{连显式公式都不需要} \text{——它只需要 Mertens 级密度估计}$$
$$\qquad \Longrightarrow \text{若 A 成立（显式公式蕴含它）}，\text{则一个}\ \textbf{含零点信息的更强前提} \text{蕴含一个}\ \textbf{只靠密度信息就能证的东西};\ \text{这虽不矛盾，但}\ \textbf{方法本身已给出更弱的证明} \Longrightarrow \textbf{该界的正确"归属层"＝密度面（}\sigma=1\text{）} ✓✓$$
$$\qquad ⚠️\ \text{更准确的表述}：\textbf{该界不需要显式公式，故"是否被显式公式蕴含"对方法定位无意义};\ \textbf{有意义的是}\ \textbf{它住在哪一层} \text{——答案：}\sigma=1 ✓✓✓$$

## §5 ⭐⭐⭐ **为什么它不能携带 β（干净论证，不是通道分类）**

$$\textbf{论证}：\text{设某算术系统中}\ \zeta\ \text{有轴外零点}。\text{则}：$$
$$\qquad \text{(i)}\ \text{Mertens 型定理}\ \textbf{仍成立}（\text{等价于 PNT 弱形式};\ \text{PNT}\iff\text{无}\ \Re s=1\ \text{上的零点}，\ \textbf{无条件}）⟹ \text{不变} ✓$$
$$\qquad \text{(ii)}\ \text{常数}\ B\ \text{与 RH}\ \textbf{无关};\ \text{主项}\ \log\log x\ \textbf{不变} ✓$$
$$\qquad \text{(iii)}\ \eta\ \text{在实}\ s>0\ \text{的单调性}\ \textbf{与 RH 无关} ✓$$
$$\qquad \text{(iv)}\ \text{doubly-harmonic 权的次不变性}\ \textbf{是纯组合事实} ✓$$
$$\Longrightarrow \textbf{四项输入全部 RH-无关} \Longrightarrow \textbf{任何由它们导出的结论亦 RH-无关} \Longrightarrow \boxed{\text{该界在 RH 真/假两种情形下}\textbf{形状相同}} \Longrightarrow \textbf{零 β 分辨力} ✓✓✓$$
$$\qquad \text{对照（本项目内已有，非新证）}：\text{`V219` 的 Epstein 反例说明}\ \textbf{连 Euler 积＋FE 都不足以排除轴外零点};\ \text{本方法的输入}\ \textbf{比那更弱}（\text{无 Euler 积、无 FE 要求}）✓✓$$

## §6 ⭐⭐⭐⭐ **更强：$\sigma=1$ 不是偶然，是被"尾和有限性"强制 —— 且 $\frac12$ 版本不存在**

$$\text{一般化（同一恒等式）}：\text{对}\ c>0,\qquad \frac{1}{a^{c}\log a}=\int_c^\infty a^{-s}\,ds \qquad\Longrightarrow\qquad \sum_{a\in A}\frac{1}{a^{c}\log a}=\int_c^\infty D_A(s)\,ds ✓$$
$$\textbf{尾和有限性（决定性）}：$$
$$\qquad c=1：\quad \sum_{a>x}a^{-1}/\log a\ \textbf{收敛}（\text{权}\ 1/(a\log a)）⟹ \textbf{可有}\ 1+O(1/\log x)\ \textbf{型尾界} ✓$$
$$\qquad c=\tfrac12：\quad \sum_{a>x}a^{-1/2}/\log a\ \textbf{发散}（\text{积分检验}\ \approx 2\sqrt x/\log x\to\infty）\ \Longrightarrow \boxed{\text{同形状的}\ \sigma=\tfrac12\ \text{尾界}\ \textbf{不存在}} ✓✓✓$$
$$\Longrightarrow \textbf{结论}：\text{该方法的}\ \sigma=1\ \text{位置}\ \textbf{不是技术落后}，\ \text{而是}\ \textbf{"能以}\ 1+O(\cdot)\ \text{形式给出尾界"这一要求所}\textbf{强制} \text{的位置} ✓✓✓$$
$$\textbf{要把结论搬到}\ \sigma=\tfrac12：$$
$$\qquad \text{必须让}\ \sum_{a>x}a^{-1/2}\ \text{型发散的尾和}\ \textbf{出现抵消};\ \text{而}\ \textbf{抵消信息＝零点位置信息} \text{（这正是显式公式的机制）} ✓$$
$$\qquad \Longrightarrow \textbf{与 `V219` 的定理接通}：\ \mu_2=\beta_*=\tfrac12\iff\text{RH}\ \text{（`V219`：该链}\ \textbf{循环}，是 RH 等价式而非可推引理）✓✓$$
$$\qquad \Longrightarrow \text{再加上}\ \textbf{`V162`／A3}\ \text{的承重墙（需 support}>1\text{）与 `V235`-A（}\frac1r\ \text{密度坐标 vs 对称坐标）} \Longrightarrow \boxed{\textbf{同一堵墙}} ✓✓✓✓$$

## §7 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V253}：\text{判定＝}\textbf{非 A、且强于 B};\ \text{该界住在}\ \boldsymbol{\sigma=1}\ \text{密度面（输入严格弱于显式公式）};\ \textbf{输入四项全 RH-无关} \Longrightarrow \textbf{零 β 分辨力};\ \textbf{且}\ \sigma=\tfrac12\ \text{同形状版本}\textbf{不存在}（尾和发散）\Longrightarrow \textbf{迁移＝同一堵墙}} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| Erdős 和住在哪一层 | **$\sigma=1$** | ⭐ 本档恒等式 $\frac{1}{a\log a}=\int_1^\infty a^{-s}ds$ |
| 情形 A（被显式公式蕴含） | **不成立**（输入严格更弱） | §3 |
| 情形 B（新无条件输入） | **成立但降格**：**已知形状的、新证的无条件定理** | §8 措辞更正 |
| 是否携带 β | **否** | §5（四项输入全 RH-无关） |
| $\sigma=\frac12$ 同形状版本 | **不存在** | §6（尾和发散） |
| 迁移到 $\frac12$ 是否可能 | **只有引抵消输入＝零点位置 ⟹ 同一堵墙** | §6＋`V219`／`V162`／`V235`-A |
| 对 `V201` 开口的意义 | **不打开**（非新类型输入） | §7 |

$$\textbf{边界（诚实）}：$$
$$\qquad \text{§2 恒等式为}\ \textbf{初等（本档推导）}，\ \text{但}\ \textbf{"故整个方法在}\ \sigma=1\ \text{"是本档判断};\ \text{§3 的三项输入清单来自原文摘要＋LeanMarathon 复述，}\textbf{未逐行读完整 35 页} ⚠️;$$
$$\qquad \text{§5 的"RH-无关 ⟹ 无分辨力"}\ \textbf{是一个结构性论证，不是定理};\ \text{严格版应是"若输入在两类模型中相同则输出相同"}\ \textbf{（未做模型构造）} ⚠️;$$
$$\qquad \text{§6 的尾和发散是初等计算}（\text{积分检验}）✓;\ \text{§8 为对本档前一轮的}\textbf{自我更正} ✓$$
$$\qquad \textbf{未用 RH 作推导};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

## §8 ⚠️ 对 **V252 §4** 的自我措辞更正（诚实）

$$\text{我在 }\text{`V252`}\ \S4\ \text{写}：\text{"本文产出}\ \textbf{此前不存在的无条件算术不等式}\text{"} \qquad ⚠️\ \textbf{不准确} ✓$$
$$\qquad \text{事实}：\text{#1196／#1217／#164／Banks–Martin 都是}\ \textbf{此前已陈述的猜想}（\text{#1196 为 1966 年}）;\ \text{2026 年新的是}\ \textbf{证明与技术}，\ \textbf{不是不等式本身} ✓$$
$$\qquad \text{更正表述}：\textbf{"该类产出的是}\ \textbf{已知形状的、新证的无条件定理}\text{"};\ \text{它是否算 `V201` 所要求的"新无条件输入"，}\textbf{取决于 `V201` 的定义是否把"已知形状的新定理"计入} ⚠️$$
$$\qquad \Longrightarrow \text{本档 }\S7\ \text{判定：}\textbf{不打开 `V201` 开口}（\text{因为它是}\ \textbf{同类型} \text{信息的新定理，不是}\ \textbf{新类型} \text{的输入}）;\ \text{但}\ \textbf{这一点应作为 `V201` 判据的一处收紧登记} ✓$$

---

## §9 ⚠️ **勘误与最终版**（唐先生 2026-09-15 22:06；逐字采纳，共七条）

$$\textbf{T1（突出内生性 —— 单列）}：\boxed{\text{该方法的尺度 } c=1 \text{ 是由其收敛性}\textbf{内生决定} \text{的，而不是人为选择}} ✓✓✓$$
$$\qquad \text{（此点应从"}\sigma=1\ \text{密度面"的叙述中}\textbf{单独抽出} \text{，因为它是}\ \textbf{机制级} \text{事实}）$$

$$\textbf{T2（收紧"必须引入抵消"）}：\text{我原写"要把结论搬到}\ \tfrac12\ \text{就必须引入抵消——而抵消信息就是零点位置信息"，}\textbf{过强} ⚠️$$
$$\qquad \text{准确版本}：\boxed{\text{若}\ \textbf{保持同一正项尾和机制}，\text{则搬到}\ \tfrac12\ \textbf{必须改变机制}，\text{不能只改变权指数}} ✓✓✓$$
$$\qquad \text{理由：还有另一条路}\ \text{正项密度}\to\text{带符号／复权重}\to\text{条件抵消};\ \textbf{这种抵消可能携带比普通密度更多的信息} ✓$$
$$\qquad \qquad \text{但一旦它}\ \textbf{真能精确产生}\ \beta=\tfrac12，\ \text{就必须继续检查它是否}\ \textbf{偷偷进入} \text{显式公式／零点统计／等价 RH criterion} ⚠️$$
$$\qquad \Longrightarrow \text{V253 关闭的是}\ \boxed{\text{positive-density-tail transport}}，\ \textbf{不是所有可能的"密度}\to\text{临界线"机制} ✓✓✓$$

$$\textbf{T3（更强的数学表述 —— 可直接推出，本档采纳）}：\text{设}\ w_a\ge0\ \text{且不发生额外抵消},\ \text{则临界指数}\ \textbf{由收敛横坐标决定}：$$
$$\qquad \sigma_c=\inf\Big\{\sigma:\ \sum_a\frac{w_a}{a^\sigma\log a}<\infty\Big\} ✓$$
$$\qquad \text{要得到}\ c=\tfrac12\ \text{的}\ \textbf{同型有限尾}，\ \text{必须让权重本身满足}\ \textbf{足够强的衰减}：\ w_a\ll a^{-1/2+\varepsilon} ✓$$
$$\qquad \Longrightarrow \textbf{这不是"把密度面从}\ 1\ \text{搬到}\ \tfrac12\text{"}，\ \textbf{而是重新植入了一个新的}\ a^{-1/2}\ \textbf{尺度} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{若}\ \tfrac12\ \text{已经出现在权重中},\quad \tfrac12\ \text{是}\textbf{输入}，\ \textbf{不是输出}} \qquad（\text{与}\ \text{`V220`}\ \text{的 multiplier test 接上}）✓✓✓✓$$

$$\textbf{T4（V253 实际完成的是"三层封口" ＋ 三个逃逸入口）}：$$
$$\qquad \boxed{\text{正项密度}\ \longrightarrow\ \sigma=1\ \text{尾和}\ \longrightarrow\ \text{不能通过单纯改指数得到}\ \sigma=\tfrac12} ✓$$
$$\qquad \text{企图逃逸只有三种}：$$
$$\qquad \qquad \textbf{A. 改权重}\quad w_a\sim a^{-1/2}\ \Longrightarrow\ \tfrac12\ \textbf{已经进入输入} \Longrightarrow \text{`V220`／`V218` 型问题} ✓$$
$$\qquad \qquad \textbf{B. 引入符号抵消}\quad \sum_a\varepsilon_a a^{-s}\ \Longrightarrow\ \text{必须解释抵消的}\ \textbf{canonical arithmetic source} \Longrightarrow \textbf{进入 `V162`/A3 的真正承重墙} ✓$$
$$\qquad \qquad \textbf{C. 引入非局部相关}\quad \sum_{a,b}K(a,b)a^{-s}b^{-t}\ \Longrightarrow\ \text{必须证明该相关结构}\ \textbf{不是统计／显式公式的重新编码} \Longrightarrow \text{`V236`／`V241` 已把大部分自然候选压回} ✓✓$$

$$\textbf{T5（更正"非 A 且强于 B"）}：\text{该表述}\ \textbf{混淆了两个维度} ⚠️;\ \text{准确版}：$$
$$\qquad \boxed{\text{它不是 A 型新 RH 输入}};\qquad\qquad \boxed{\text{它提供了一个比 B 型"新无条件定理"}\textbf{更强的结构性排除}} ✓✓$$
$$\qquad \text{因为它不仅说"这个定理不够 RH"，而是}\ \textbf{解释"为什么整个正项尾和的尺度被锁在}\ \sigma=1\text{"} \Longrightarrow \textbf{这是"机制级"信息，不是"定理强弱"} ✓✓✓$$

$$\textbf{T6（最终压缩版 —— 逐字采纳）}：$$
$$\qquad \boxed{\begin{aligned}&\frac{1}{a^c\log a}=\int_c^\infty a^{-s}ds;\\ &\text{正项尾和的临界尺度由收敛半平面决定};\\ &c=1\ \text{给出有限尾量};\qquad c=\tfrac12\ \text{的同型正项尾发散};\\ &\therefore\ \text{不能靠指数替换把该机制迁移到}\ \tfrac12.\end{aligned}} ✓✓✓$$
$$\qquad \text{进一步}：\boxed{\text{若强行得到}\ \tfrac12,\text{ 必须增加}\ \textbf{权重}、\textbf{抵消} \text{或}\ \textbf{非局部相关}}$$
$$\qquad \qquad \text{其中：}\textbf{权重} \Longrightarrow \tfrac12\ \text{已进入输入};\qquad \textbf{抵消} \Longrightarrow \text{进入}\ \beta\text{-sensitive cancellation};\qquad \textbf{相关} \Longrightarrow \text{必须通过独立的 arithmetic bridge} ✓$$

$$\textbf{T7（链）}：\text{`V250`／`V251`／`V253` 连起来}：\boxed{\text{canonicality}\to\text{splitting}\to\text{phase}\to\text{density scale}} ✓$$
$$\qquad \text{目前}\ \textbf{所有自然结构都在把信息导向}\ \sigma=1，\ \textbf{而不是}\ \sigma=\tfrac12 ✓✓✓$$

$$\textbf{§9 判词（采纳唐先生）}：\boxed{\textbf{V253}＝\text{CLOSED（}\textbf{针对该正项密度／尾和机制}）,\ \textbf{不升级为"所有密度机制 CLOSED"}} ✓✓$$

$$\textbf{§9 登记（收紧后的真正硬问题 —— 本档最高优先）}：$$
$$\qquad \boxed{\textbf{有没有一个 canonical arithmetic source，能产生}\ \textbf{真正的、非输入式的} \text{ signed cancellation}，\ \text{并且其}\ \textbf{cancellation threshold 恰好锁定}\ \tfrac12\ \text{？}} ✓✓✓✓$$
$$\qquad \text{若}\ \textbf{没有} \Longrightarrow \text{这才会真正把}\ \text{`V162`/A3}\ \text{的承重墙从"目前最大障碍"推进到}\ \textbf{一个可证明的结构性障碍} ✓✓✓$$


---

## 【型标注】（`NEG-REGISTER-1`，2026-09-18 20:1x）

$$\text{本档定级}：\textbf{T-I}\ \text{（干净小结果：关键恒等式 ＋ `\sigma=1` 位置被尾和有限性强制）}✓$$
$$\qquad \text{硬内容（本档推导）}：\\frac{1}{a\\log a}=\\int_1^\\infty a^{-s}ds \Longrightarrow \text{Erdős 和住}\ \sigma=1✓$$
$$\qquad \Longrightarrow \sigma=\\tfrac12\ \text{版}\ \textbf{不存在}（\text{尾和发散}） \Longrightarrow \text{对该机制的定位}\ \textbf{干净、无隐藏前提}✓✓$$
$$\qquad ⚠️\ \text{可宣称}：\textbf{该机制} \text{无法移到}\ \\tfrac12;\ \textbf{不可} \text{宣称"一切带符号加权不可达"}✓$$
$$\textbf{引用纪律（本档确立）}：\text{引用本档时必须}\ \textbf{随引其型};\ \textbf{不得} \text{去条件化引用}✓✓$$
