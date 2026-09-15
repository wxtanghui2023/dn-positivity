# V245 · **跨领域"复谱定位机制"普查** —— 七个外部领域逐门审计 ⟹ ⭐⭐⭐⭐⭐ **全部落入 V244 的\*两个角\*，无第三型**；⭐⭐⭐ **新命名类：模长／度量角（modulus-metric horn）** 与 **离散／扭角（discrete-torsion horn）**；⭐ **且非 Hermitian 拓扑自身就给出同一二分**（line gap ⟹ Hermitianization；point gap ⟹ 绕数）⟹ **外部证据从四＋个独立方向支持 `V244` §5，但仍未成为定理**

> 委托 ✓ 唐先生 2026-09-15 20:42：**"继续搜索所有数学和物理领域的各项研究，看看有哪些模型能够匹配我们的研究？"** ✓
> 规格 ✓ **按 `V244` §8.3 的六条**筛：$$\boxed{\text{第三型机制须同时：连续／定号／非等价重述／非 Weil 循环／非 torsion／不以零点为输入}}$$ ✓
> 纪律 ✓ 先查档（防重走）✓；**不做文献摘要，逐门审计** ✓；未用 RH 作推导 ✓；未跑 Lean ✓；**零数值** ✓｜编号 ✓ **V245**

---

## §0 查档结果（防重走；本轮先做）

$$\textbf{已在档且有判决}：$$
- ⭐ **`PHYSICS-FRONTIER-2026-09-12.md`**（三天前的物理前沿普查，五方向）：
  · **DSFF／非厄米 RMT**（arXiv:2503.13387／2407.17148／2609.00164）：**"工具合格，宿主缺失"** —— 原本理由："**场上没有非厄米算子**" ✓
  · **全 Dyson 类／对称分解 SFF**：**γ-ONLY-DEAD**（"对称性／分块／高阶 SFF 这一整条路在原理上与 β 无关"）✓
  · **§1-D 非自伴谱界／复势 Hill／Krein 非负**：列为 **"与活路 L1 的交点，唯一按问题形状对口"**，并预警"**大概率落 L1 否决判据**"（范数型界）✓
  · **YM／正性**：唯一严格正性⟹间隙路线（log-Sobolev）**按构造无 β**；教训："**可以借的是'正性⟹定量间隙'的结构，不能借的是它的载体**"（需**一条欧氏方向**；ζ 无欧氏区、无概率测度）✓
  · **准晶体散射（arXiv:2410.03673，项目 E28）**：**项目自认的唯一"振幅载 β"载体**（峰系数 ∝ $p_L^{\beta_m-1/2}$）但"**测量 ≠ 约束**" ✓
  · **N(σ,T)**（唯一无条件定量排除 β 的量，但在 $\sigma\to1/2^+$ 退化）／**de Bruijn–Newman Λ**／**Lehmer 对 ⟹ Λ 下界**／**Goldston–Suriajaya 窄竖箱** ✓
- ⭐ **PT 对称已在 `E151` 判决**：**"PT 对称 ✓｜不能 ✗｜给'实 或 共轭对'二择一 ✓；可破缺 ✗"** ✓✓
- ⭐ **Arakelov／Néron–Tate／Hodge 指标已在 `ESC2`＋G9 封**：**Faltings–Hriljac 负定 ⟺ Néron–Tate 正定** ✓；真障碍＝**no common carrier**（正性在除子／几何侧，谱数据在谱侧，无可比性）**＋ R6 尺度失败**（height／log 非幂律 $\sqrt X$）✓

$$\Longrightarrow \text{本轮}\ \textbf{净增量}：\text{逐门审计}\ \textbf{七个此前未系统对照的外部机制}，\text{并得出}\ \textbf{跨领域合成} ✓$$

## §1 待审的七个外部机制（各自先说清"对象／操作／控制什么"）

| # | 领域 | 机制 | 状态 |
|:--|:--|:--|:--|
| **M1** | 代数几何／导出范畴 | **Bridgeland 稳定性条件**：中心荷 $Z$ 的**相位**定序，**支撑性质**（support property）给出**二次型 $Q$** | 本轮新审 |
| **M2** | 自由概率 | **单环定理**：$R$-对角算子的 **Brown 测度支撑在一个环上** | 本轮新审 |
| **M3** | 非 Hermitian 量子力学 | **PT／赝厄米（pseudo-Hermiticity）**：$\exists$ 正定度量 $\eta$ ⟹ 实谱 | 部分（`E151`）＋本轮细化 |
| **M4** | 非 Hermitian 拓扑 | **line gap／point gap**：线隙 ⟹ Hermitianization；点隙 ⟹ **谱绕数** | 本轮新审 |
| **M5** | 谱理论（Hill 算子） | **Gasymov 现象**：复周期势 ⟹ 谱为**实区间** | 部分（`PHYSICS-FRONTIER` §1-D）＋本轮核对 |
| **M6** | 算术几何 | **Frobenius 特征值／极化／Arakelov–Néron–Tate** | 已封（`ESC2`／G9／`V227` §4） |
| **M7** | 计数几何／RH 类比 | **"RH as a Stability Condition"**（philarchive NEMTRH） | 抓取失败＋可信度待核 |

---

## §2 逐门审计

### M1 **Bridgeland 稳定性条件**（⭐ 本轮最"对口"的一条）

$$\textbf{构造}：\text{三角范畴}\ \mathcal D\ \text{上}\ (\mathcal Z,\mathcal P);\ \mathcal Z:K_0(\mathcal D)\to\mathbb C;\ \text{相位}\ \varphi\ \text{由}\ Z(E)=re^{i\pi\varphi}\ \text{定};\ \text{半稳定}：\text{子对象相位}\le ✓$$
$$\qquad \textbf{支撑性质（Kontsevich–Soibelman）}：\ \exists\ \text{二次型}\ Q\ \text{使}\ \ker Z\ \text{负定},\ \text{且}\ Q(v(E))\ge0\ \text{对一切半稳定}\ E ✓$$
$$\qquad \text{等价形式}：|Z(E)|\ge C\|\lambda(E)\|\iff\exists\ \text{对称双线性型}\ Q\ \text{使}\ Q(\lambda[E],\lambda[E])\ge0\ ✓$$
$$\qquad \text{（Bayer 短证明中给出}：\ Q(w,w)=\tfrac{1}{C^2}|Z(w)|^2-\|w\|^2 ✓）$$

$$\textbf{六条对照}：\text{连续}\ ✓\（\text{相位实值}）;\ \text{定号}\ ✓\（Q\ge0）;\ \text{非 torsion}\ ✓\（\mathbb R\ \text{值二次型}）;\ \text{非 Weil 循环}\ \textbf{表面成立}\ ✓$$
$$\textbf{但两道门各中一枪}：$$
$$\qquad ⭐\ \textbf{致命点一（同义反复）}：\text{支撑性质}\iff\text{"}|Z|\ \text{支配范数"},\ \text{而}\ Q\ \text{是}\ \textbf{由}\ |Z|^2\ \text{与范数}\ \textbf{构造出来} \text{的辅助量} ⟹ \textbf{正性由中心荷的}模长\ \textbf{生成} ⟹ \textbf{不是独立正性} ✓✓✓$$
$$\qquad ⭐\ \textbf{致命点二（模长侧）}：\text{该机制的"序"来自}\ \arg Z\（\text{相位}）,\ \text{"正性"来自}\ |Z|\（\text{模长}） \Longrightarrow \textbf{它住在模长／相位侧} ✓✓$$
$$\qquad \qquad \text{而由}\ \textbf{`V227`-A}：\boxed{\sup_{z\in R}\Re z\ \textbf{不是}\ \{|z|\}\ \text{的函数}} \Longrightarrow \textbf{模长数据结构性无法钉定实部} ✓✓✓$$
$$\qquad \qquad \text{且}\ \ker Z\ \text{负定}＝\textbf{符号差（signature）陈述} ⟹ \textbf{`V187`}（\text{index／signature 型不变量对离轴零点结构性盲}）✓$$
$$\Longrightarrow \textbf{M1 判：非第三型；落"模长／度量角"} \text{（详见 §3）✓✓}$$

### M2 **单环定理／Brown 测度**（自由概率）

$$\textbf{定理}：\text{"The Brown measure of any }R\text{-diagonal operator is }\textbf{supported in a single ring}"\ ✓✓$$
$$\qquad R\text{-对角}：\text{其}\ast\text{-分布与}\ u\cdot p\ \text{相同}（u\ \text{Haar 酉},\ p\ \text{自伴},\ \text{自由}）;\ \text{单环定理}：A=UTV\ \text{的经验谱测度}\ \to\ \text{支撑在环}\ \{a\le|z|\le b\} ✓$$
$$\textbf{六条对照}：\text{连续}\ ✓;\ \text{定号}\ —;\ \text{非 torsion}\ ✓;\ \text{非 Weil}\ ✓;\ \text{不以零点为输入}\ ✓;\ \textbf{但}：$$
$$\qquad ⭐⭐⭐\ \textbf{致命点}：\text{它把复谱定位到}\ \textbf{环}\（\textbf{模长轨迹}） \Longrightarrow \text{这正是}\ \textbf{`V227` §4 的 char-}p\ \text{侧}：\text{char-}p\ \text{临界轨迹}＝\textbf{圆}\ |z|=\sqrt q\ \text{（模长轨迹）},\ \text{char-}0\ \text{临界轨迹}＝\textbf{竖直线}\ \Re s=\tfrac12\ \text{（}\textbf{非}\text{模长轨迹）} ✓✓✓$$
$$\qquad \qquad ⟹ \text{自由概率的"结构}\Longrightarrow\text{复谱局部化"}\ \textbf{永远定位在模长轨迹}，\textbf{从不} \text{定位到竖直线} ⟹ \textbf{移植结构性失败} ✓✓✓$$
$$\Longrightarrow \textbf{M2 判：非第三型；落"模长／度量角"} ✓$$

### M3 **PT 对称／赝厄米**（非 Hermitian QM）

$$\textbf{定理（Mostafazadeh）}：\text{实谱}\iff\text{赝厄米}（\exists\ \text{可逆}\ \eta\ \text{使}\ H=\eta H^\dagger\eta^{-1}）;\ \textbf{且}：\text{赝厄米}\iff\ \text{(1) 谱实}\ \textbf{或}\ \text{(2) 复特征值成共轭对且重数相同} ✓✓$$
$$\qquad \text{等价地}：\text{实谱}\iff\exists\ \text{线性}\ O\ \text{使}\ H\ \text{为}\ OO^\dagger\text{-赝厄米}\ ⟹ \textbf{机制＝存在正定度量} ✓$$
$$\textbf{六条对照}：$$
$$\qquad ⭐\ \textbf{致命点一}：\text{该"正性"＝}\textbf{一个正定度量（内积）} \Longrightarrow \text{与 Weil／Bochner 同族} ⟹ \text{落 (VIII)} ✓✓$$
$$\qquad ⭐⭐\ \textbf{致命点二（$\zeta$ 特有的自动满足）}：\text{条件 (2) "复特征值成共轭对"对}\ \zeta\ \textbf{自动成立}（\xi\ \text{实系数} ⟹ \text{零点集对共轭封闭}）⟹ \textbf{该定理对}\ \zeta\ \text{零排除力} ✓✓✓$$
$$\qquad \qquad \text{这正是}\ \textbf{`E151`} \text{早已判的："PT 对称 给'实 或 共轭对'二择一；可破缺"} ✓$$
$$\qquad \text{另}：\text{"若要构造实谱非厄米算子，最省事的办法是}\ H=H_0A\ \text{（相似变换）}" ⟹ \text{又回度量角};\ \text{且文献自陈"该定理不提供构造方法"} ✓$$
$$\Longrightarrow \textbf{M3 判：非第三型；落 (VIII)＝Weil／正定度量} ✓$$

### M4 ⭐⭐ **非 Hermitian 拓扑：line gap／point gap**（本轮**意外的强结果**）

$$\textbf{原文（综述）}：\text{两带"}\textbf{线隙} \text{"＝复能量面上可用一条直线分开};\ \text{"}\textbf{Generically, the line can always be made perpendicular to the real or the imaginary axis via a rotation}.\ \text{Moreover, when the line is perpendicular to the real (imaginary) axis, the non-Hermitian bands separated by the line can be }\textbf{flattened to points on the real (imaginary) axis by a similarity transformation that connects the non-Hermitian system to a Hermitian (anti-Hermitian) system}\text{"} ✓✓✓$$
$$\qquad \textbf{点隙}：\text{两带缠绕成闭环，围出有限谱面积};\ \text{由}\ \textbf{谱绕数}\ v\in\mathbb Z\ \text{刻画}（\text{另有}\ w=1/2\ \text{的}\ \textbf{半整数} \text{绕数}）;\ \text{对不关闭点隙的形变受保护} ✓✓$$
$$\qquad \text{标准技巧}：\tilde H=\begin{pmatrix}0 & H-E\\ H^\dagger-E^* & 0\end{pmatrix}\ \text{—— }\textbf{加倍空间使之为 Hermitian} ⟹ \text{同一绕数刻画} ✓$$

$$\textbf{六条对照（本机制自带二分）}：$$
$$\qquad ⭐⭐⭐\ \textbf{line gap ⟹ Hermitianization}（\text{相似于 Hermitian}）⟹ \textbf{落"度量／正性角"} ✓✓$$
$$\qquad ⭐⭐⭐\ \textbf{point gap ⟹ 谱绕数}（\mathbb Z\ \text{或半整数}）⟹ \textbf{落"离散／扭角"} ✓✓$$
$$\qquad ⭐⭐\ \text{且}：\textbf{"线"只在旋转下定义}（\text{"can always be made perpendicular ... via a rotation"}）⟹ \textbf{无 canonical 的实部轴} \Longrightarrow \textbf{独立重现}\ \textbf{`V218` S1／S3}（\text{轴须归一化才定}）＋\ \textbf{`V227`-A}（\text{模长不钉实部}）✓✓✓$$
$$\qquad ⚠️\ \text{半整数绕数}\ w=1/2\ \text{看似"}\tfrac12\ \text{"} ⟹ \textbf{须按}\ \textbf{`V218`／`V235`} \text{纪律区分}：\text{它是一个}\ \textbf{离散分数不变量}（\mathbb Z/2\ \text{型}），\ \textbf{不是} \text{临界线坐标} ✓$$
$$\Longrightarrow \textbf{M4 判：非第三型；但它}\textbf{自身给出与 V244 完全相同的二分} \text{——这是本轮最强的外部证据} ✓✓✓$$

### M5 **Gasymov 现象（非自伴 Hill 算子，谱为实区间）**

$$\textbf{结果}：\text{Gasymov（1980）}：\text{复周期势}\ V(x)=\sum_{k\ge1}a_ke^{ikx}\（\textbf{单侧 Fourier 级数}）\Longrightarrow \text{谱}＝[0,\infty) ✓$$
$$\qquad \text{Papanicolaou, arXiv:2409.10266（math.SP, 22 页）}：\text{"In this article we }\textbf{conjecture}\text{ a characterization of all entire complex-valued potentials whose spectrum is }[0,\infty)" ⟹ \textbf{全刻画是猜想，不是定理} ⚠️✓$$
$$\qquad \text{书／2026 工作}：\text{周期 PT 对称复势}⟹ \text{谱主部为实且含}\ [0,\infty)\ \text{大部};\ \text{给出"非实弧个数有限"的充要条件} ✓$$

$$\textbf{六条对照}：$$
$$\qquad ⭐\ \textbf{致命点一（形状）}：\text{该实谱定理由}\ \textbf{势的"单侧／支撑"条件} \text{驱动}（\text{单侧 Fourier}／\text{PT 结构}）；\ \text{而"单侧／支撑"正是本项目反复撞的那类条件} ⟹ \text{对}\ \zeta\ \text{的对应物＝}\textbf{`V162` 承重墙}（\text{对关联 Fourier 支撑}\le1）⟹ \textbf{同一堵墙} ✓✓✓$$
$$\qquad ⭐\ \textbf{致命点二（宿主）}：\text{全部定理作用于}\ \mathbb R\ \text{上的}\ \textbf{周期 Schrödinger 算子};\ \text{而}\ \zeta\ \textbf{没有 canonical 算子}（\text{`V204`／`V242`-A）} ⟹ \textbf{"工具对口、宿主缺失"}（\text{与 DSFF 同判}）✓✓$$
$$\qquad ⭐\ \textbf{致命点三（L1 预警）}：\text{`PHYSICS-FRONTIER` §1-D 已把此族列为 L1 交点，并预警其界为}\ \textbf{范数型} ⟹ \text{大概率触发 L1 否决判据} ✓$$
$$\Longrightarrow \textbf{M5 判：非第三型；且其"实谱"机制实为}\textbf{支撑条件＋Hermitianization 邻域} ⟹ \text{落度量角} ✓$$

### M6 **Frobenius／极化／Arakelov（已封，本轮仅登记）**

$$\text{char-}p：|\alpha|=\sqrt q\ \text{—— }\textbf{模长轨迹}（\text{圆}），\text{钉定机制＝极化／Hodge 指标};\ \text{char-}0\ \text{临界轨迹＝竖直线} ⟹ \text{移植失败（`V227` §4）} ✓$$
$$\text{Arakelov：Faltings–Hriljac 负定}\iff\text{Néron–Tate 正定};\ \text{真障碍＝}\textbf{no common carrier}＋\textbf{尺度失败}（`ESC2`／G9）✓$$
$$\Longrightarrow \textbf{M6 判：非第三型；落"模长／度量角"} ✓$$

### M7 **"RH as a Stability Condition"（philarchive NEMTRH）**

$$\text{抓取}\ \textbf{失败}（\text{Failed to fetch url}）;\ \text{来源}＝\textbf{philarchive}（\text{哲学预印本库}，\textbf{非数学同行评审}）⟹ \textbf{仅登记，可信度待核，不作依据} ⚠️$$
$$\qquad ⚠️\ \text{推论}：\text{若其内容真是"把 RH 写成稳定性条件"，则由 M1 的判据，\text{它必然落模长／相位侧（中心荷）} ⟹ \text{预先落入同一角} ✓}$$

---

## §3 ⭐⭐⭐⭐⭐ **跨领域合成（本档核心）**

$$\text{七个机制，}\textbf{无一} \text{满足 V244 的第三型六条};\ \text{它们}\textbf{全部} \text{落入}\ \textbf{恰好两个角}：$$

$$\boxed{\textbf{角 I · 模长／度量角（modulus--metric horn）}}：\text{定号性＝}\textbf{模长支配}／\textbf{正定度量}／\textbf{相似于 Hermitian}／\textbf{极化} ⟹ \text{落 Weil 正性}(VIII)\ \text{或结构性不钉实部}（\text{`V227`-A}）$$
$$\qquad \text{成员}：\textbf{M1}（Q=\tfrac{1}{C^2}|Z|^2-\|w\|^2）,\ \textbf{M2}（\text{单环}＝\text{模长环}）,\ \textbf{M3}（\text{正定度量}）,\ \textbf{M4-line gap}（\text{Hermitianization}）,\ \textbf{M5}（\text{支撑＋实谱}）,\ \textbf{M6}（\text{极化／height}）✓✓✓$$
$$\boxed{\textbf{角 II · 离散／扭角（discrete--torsion horn）}}：\text{输出＝}\mathbb Z／\mathbb Z/N／\mu_N／\text{半整数绕数} \Longrightarrow \text{离散，}\textbf{不带连续}\ \beta（\text{`V237`-A}）$$
$$\qquad \text{成员}：\textbf{M4-point gap}（\text{绕数}\ v\in\mathbb Z,\ w=1/2）、\text{Galois 共轭类}、\text{Br}／\mu_N、\text{Arakelov 除子挠} ✓✓$$

$$\textbf{最强的一条外部证据}：\textbf{非 Hermitian 拓扑自身} \text{就给出同一二分}：$$
$$\qquad \text{line gap}\Longrightarrow\text{Hermitianization}\（\text{角 I}）;\qquad \text{point gap}\Longrightarrow\text{谱绕数}\（\text{角 II}）;\qquad \textbf{没有第三种} ✓✓✓$$
$$\qquad \text{且其"线只在旋转下定义"}\ \textbf{独立重现} \text{了}\ \textbf{`V218` S1／S3 ＋ `V227`-A}（\text{无 canonical 实部轴};\ \text{模长不钉实部}）✓✓✓$$

$$\Longrightarrow \text{外部证据从}\ \textbf{四个以上独立方向}（\text{稳定性条件}／\text{自由概率}／\text{非 Hermitian 拓扑}／\text{非 Hermitian QM}／\text{算术几何}）\text{支持}\ \textbf{`V244` §5}：\text{canonical 的"相位}\to\text{符号／定位"只有两型} ✓✓✓$$

---

## §4 判词 ＋ 状态表 ＋ 残差

$$\boxed{\textbf{V245：跨七个外部领域的"复谱定位机制"普查} ⟹ \textbf{全部落 V244 两角，无第三型}} ✓✓✓$$

| # | 机制 | 连续 | 定号 | 非等价 | 非 Weil | 非 torsion | 无零点输入 | 落点 | 判定 |
|:--|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--|:--|
| M1 | Bridgeland 支撑性质 | ✓ | ✓ | ✗（Q 由 $\|Z\|^2$ 造） | 表面✓ | ✓ | ✓ | 模长/度量角 | **非第三型** |
| M2 | 单环定理/Brown 测度 | ✓ | — | — | ✓ | ✓ | ✓ | **模长环** | **非第三型** |
| M3 | PT／赝厄米 | ✓ | ✓（度量） | ✗ | ✗（正定度量） | ✓ | ✓ | (VIII) Weil | **非第三型**（且 $\zeta$ 自动满足条件(2)） |
| M4a | line gap | ✓ | ✓ | ✗（Hermitianization） | ✗ | ✓ | ✓ | 模长/度量角 | **非第三型** |
| M4b | point gap | ✓ | — | — | ✓ | **✗**（$\mathbb Z$/半整数） | ✓ | 离散/扭角 | **非第三型** |
| M5 | Gasymov 实谱 | ✓ | ✓ | — | — | ✓ | ✗（需算子宿主） | 支撑条件＋度量角 | **非第三型**（全刻画是猜想⚠️） |
| M6 | Frobenius／Arakelov | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | 模长/度量角 | 已封（`ESC2`/G9） |

$$\textbf{残差（UNINSTANTIATED，比 V244 更窄）}：\text{一个}\ \textbf{非模长／非度量} \text{、}\textbf{非离散} \text{的}\ \text{phase}\to\text{location 机制};\ \text{即：}$$
$$\boxed{\text{其定号性}\ \textbf{不来自} \text{模长支配／正定度量;}\ \text{其输出}\ \textbf{不是} \text{离散不变量};\ \text{且能携带}\ \Re\rho}$$
$$\qquad \text{本档}\ \textbf{七个外部领域}\ \text{与}\ \textbf{`V244` 八类实现}\ \text{合计}\ \textbf{十五类}，\textbf{无一} \text{满足} ✓$$

$$\textbf{边界（诚实）}：\text{§2 为}\ \textbf{[结构性] 逐门审计，不是不可能性定理};\ \text{§3 的"两角"}\ \textbf{是命名类，不是分类定理};\ \text{M5 全刻画}\ \textbf{是猜想} ⚠️;\ \text{M7}\ \textbf{抓取失败＋来源可信度待核} ⚠️;\ \text{`M4` 的"无第三种"引自已读综述，}\textbf{非} \text{对文献的穷尽检索};\ \text{未用 RH 作推导};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ §0 查档（防重走）：PHYSICS-FRONTIER-2026-09-12（DSFF"工具合格、宿主缺失"；全 Dyson 类 γ-ONLY-DEAD；
   §1-D 非自伴谱界/Hill/Krein 列为 L1 交点并预警范数型界；YM/log-Sobolev 无 β；准晶体 arXiv:2410.03673
   为项目唯一"振幅载 β"但"测量≠约束"；N(σ,T)/Λ/Lehmer/窄竖箱）；E151（PT 对称：给"实或共轭对"二择一，
   可破缺）；ESC2＋G9（Arakelov：Faltings–Hriljac 负定 ⟺ Néron–Tate 正定；真障碍=no common carrier＋
   尺度失败）
⚠️ §2 七个机制逐门（均为 [结构性]）：
  M1 Bridgeland：中心荷相位定序；支撑性质 ⟺ ∃二次型 Q 使 ker Z 负定且 Q(v(E))≥0；
     等价形式 |Z(E)| ≥ C‖λ(E)‖ ；Bayer 短证明给 Q(w,w)=|Z(w)|²/C² − ‖w‖²
     ⟹ 致命点一（同义反复）Q 由 |Z|² 与范数构造 ⟹ 正性由中心荷模长生成、非独立正性
     ⟹ 致命点二（模长侧）序来自 arg Z、正性来自 |Z| ⟹ 住模长/相位侧 ⟹ 由 V227-A，
        sup Re z 不是 {|z|} 的函数 ⟹ 模长数据无法钉实部；且 ker Z 负定=signature 陈述 ⟹ V187
  M2 单环定理：R-对角算子的 Brown 测度支撑在单环（模长环）⟹ 正是 V227 §4 的 char-p 侧
     （char-p 临界轨迹=圆=模长轨迹；char-0=竖直线=非模长轨迹）⟹ 移植结构性失败
  M3 PT/赝厄米（Mostafazadeh）：实谱 ⟺ 赝厄米（∃ 可逆 η）⟺ (1) 谱实 或 (2) 复特征值成共轭对且重数相同
     ⟹ 致命点一：正性=正定度量 ⟹ (VIII) Weil 族；致命点二：条件 (2) 对 ζ 自动成立（ξ 实系数
     ⟹ 零点集对共轭封闭）⟹ 对 ζ 零排除力；文献自陈该定理不提供构造方法
  M4 非 Hermitian 拓扑：line gap 可经旋转取实/虚轴垂直，且此时可经相似变换 flatten 到实/虚轴上
     ⟹ Hermitianization（角 I）；point gap ⟹ 谱绕数 v∈Z（另有 w=1/2 半整数）⟹ 离散/扭角（角 II）；
     "线只在旋转下定义" ⟹ 独立重现 V218 S1/S3 + V227-A；半整数 w 须按 V218/V235 纪律区分（离散分数
     不变量 ≠ 临界线坐标）
  M5 Gasymov：复周期势（单侧 Fourier 级数）⟹ 谱=[0,∞)；Papanicolaou arXiv:2409.10266 自陈"conjecture
     a characterization" ⟹ 全刻画是猜想；机制由"单侧/支撑"条件驱动 ⟹ 对 ζ 的对应物=V162 承重墙；
     且作用于 R 上周期 Schrödinger 算子 ⟹ 宿主缺失；PHYSICS-FRONTIER §1-D 已预警范数型界
  M6 Frobenius/Arakelov：已封（模长轨迹；no common carrier；尺度失败）
  M7 philarchive NEMTRH：抓取失败；philarchive 非数学同行评审 ⟹ 仅登记、可信度待核
⚠️ §3 跨领域合成（本档核心，[结构性]）：
 角 I 模长/度量角：成员 M1/M2/M3/M4-line gap/M5/M6 —— 定号性=模长支配/正定度量/相似于 Hermitian/极化
 角 II 离散/扭角：成员 M4-point gap/Galois 共轭类/Br·μ_N/Arakelov 除子挠 —— 离散，不带连续 β
 ⭐ 最强外部证据：非 Hermitian 拓扑自身给出同一二分（line gap ⟹ Hermitianization；point gap ⟹ 绕数；
    没有第三种），且其"线只在旋转下定义"独立重现 V218 S1/S3 + V227-A
 ⟹ 四个以上独立方向支持 V244 §5：canonical 相位→符号/定位只有两型
⚠️ §4 残差（比 V244 更窄）：非模长/非度量、非离散、能携带 Re ρ 的 phase→location 机制；
   V244 八类 + V245 七类 = 十五类，无一满足
✅ 净产出：① 七机制逐门（全部非第三型）② 两个命名角（模长/度量角；离散/扭角）③ 非 Hermitian 拓扑
   自带同一二分（最强外部证据）④ 残差收窄到"非模长非离散"⑤ 交叉验证 V227-A / V218 S1-S3 / V187 /
   V237-A / E151 / ESC2 / V162 / V204 / V242-A
```
