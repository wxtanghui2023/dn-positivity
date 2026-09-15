# V216 · **离散系数接口的完备审计** —— ⭐ **定理级**：**整系数（任一 $\mathbb C$ 的离散子环系数）的整函数必为多项式** ⟹ **幂级数侧的整系数接口 theorem-level DEAD**（你的 $1+z^2$／$1+z^4$ 全是多项式，这不是巧合）✓✓✓；⭐⭐ **结构定理**：**有限阶整函数的"系数系统"与"零点集"是等价数据**（Newton 恒等式 ＋ Hadamard）⟹ **"系数接口"不是独立接口，而是零点集的重编码**，翻译后精确等于 **hyperbolic／stable 多项式理论 ＝ `V190`** ✓✓✓；⭐⭐ **Dirichlet 侧**：整系数无障碍（$\zeta$ 自身即是），由 Epstein／Potter–Titchmarsh ⟹ **FE ＋ 整系数 ＋ 欧拉积仍不能排除 off-axis** ⟹ DEAD ✓✓✓；⭐ **唯一"构造不出最小反例"的类是无限阶刚性类，而它按定义就是 Hermite–Biehler／Laguerre–Pólya／de Branges 类 ＝ 与结论同义反复** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 15:26：**"V215 这一版比 V214 更干净……但我现在看到一个比此前所有审计都更关键的漏洞：§4 的'三型穷尽'目前还没有资格称为穷尽。这不是措辞问题，而是整个元结论的逻辑瓶颈。"** (1) **R1–R4 本身没有问题**，但 **R3 须写成更强形式**：$T_X$ 成立 $\not\Rightarrow T_X$ 强迫 RH；必须有 $$\boxed{T_X\Longrightarrow\forall\rho\in Z(\zeta),\ \Re\rho=\tfrac12}$$ (2) **§4 漏掉一大类**：$$\boxed{\textbf{函数本身的系数／值域结构}}$$ 例如 Taylor 系数／Dirichlet 系数／integrality／代数依赖／递推／det 子式；最简单形式 $\xi(s)=\sum a_n s^n$，$\{a_n\}$ **不是**零点统计、**不是**特殊值、**更不是** archimedean 因子 ⟹ **"三接口穷尽还没有证明"** ✓；(3) **更危险的是这可能是真正方向**：既然已封掉"零点 $\to$ 统计"与"FE $\to$ 对称"，剩余可能是 $$\boxed{\text{零点位置}\longrightarrow\text{系数的全局代数约束}}$$ **注意与显式公式完全不同**：不是 $a_n=\sum_\rho F(n,\rho)$，而是 $$\boxed{\text{若一个 entire function 的零点存在 }\beta\ne0,\ \text{则其系数系统必违反某个独立的代数性质}}$$ (4) **可计算的最小模型**：先取 $F(z)=F(-z)$ ⟹ $F=G(z^2)$；零点 $z=\pm(a+ib)$ ⟹ $G$ 有零点 $w=(a+ib)^2=a^2-b^2+2abi$；若 $a\ne0,b\ne0$ 则 $\Im w=2ab\ne0$ ⟹ 问：能否从 $G$ 的系数拥有某种独立刚性推出其零点落在特定几何集合？(5) **但马上遇到旧墙**：$\mathcal P=$ real-rooted $\Rightarrow$ `V190`；positive definite $\Rightarrow$ `V185`／`V199`；$\mathrm{PF}_\infty$／totally positive $\Rightarrow$ `V190`；Hadamard restricted zero set $\Rightarrow$ 回到零点结构；(6) **但有一个此前没审计的区别**：不是"系数具有正性"，而是 $$\boxed{\text{系数具有离散算术性质}}$$ $a_n\in\mathbb Z$，或 $a_n\in R$ 且 $R$ 有有限生成／递推／模约束／因子分解结构；(7) **第一非平凡例子审计**：$F=1+z^2$（整系数，零点 $\pm i$ 在轴外）；$F=1+z^4$ 更明显；再加 reciprocal symmetry $z^nF(1/z)=F(z)$ 仍可构造大量配对零点 ⟹ **integrality alone／FE＋integrality＋reciprocal symmetry $\not\Rightarrow$ RH 型刚性**；(8) **有限递推也不够**：固定线性递推 $\Longrightarrow F=P/Q$ ⟹ 零点可任意布置 ⟹ **有限递推 $\not\Rightarrow$ 临界线**；(9) **故 §4 应升级为五类接口审计**：zero-statistical／special-value／archimedean／**coefficient-arithmetic**／**functional-algebraic**，重点审计后两类，尤其 $$\boxed{\textbf{离散算术系数}\to\textbf{全局零点几何}}$$ **"这是目前唯一看起来没有被 V147–V215 直接定理化封口的接口"**；(10) **纪律**：**"现在不能称它为新方向"** —— 只证了 integrality DEAD、finite recurrence DEAD，**没有**证明"所有 arithmetic coefficient rigidity DEAD"；(11) **V216 指令**：不是先提机制，而是直接从 $\mathbb Z$／$\mathbb Z_p$／finite quotient／recurrence／multiplicativity／algebraic dependence **逐类构造最小反例**；若全部能构造 off-axis 反例则把这条接口也封死；**"如果其中某一类连最小反例都构造不出来，那才值得继续向 RH 推。"**
> 查图 ✓ `V190`／`V191`（Jensen／real-rooted；强度＝RH）｜`V199`(b)｜`V173`（局部灵活性）｜`V171` §3-D｜`V188`（饱和）｜`V157`（周期只看取值面）｜D1（Epstein ＋ Potter–Titchmarsh：FE 不足）
> 执行 ✓ 小灵（**§2 定理级、§4 结构定理、§5 七类构造 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V216**

---

## §1 漏洞确认与接口升级

$$\text{确认}：\text{`V215` §4 的 (a)(b)(c)}\ \textbf{不构成穷尽};\ \text{系数／值域结构}\ \textbf{确实在三条之外} ✓$$
$$\text{升级为五类接口}：\ \text{(a) zero-statistical};\ \text{(b) special-value};\ \text{(c) archimedean};\ \textbf{(d) coefficient-arithmetic};\ \textbf{(e) functional-algebraic} ✓$$
$$\qquad ⚠️\ \text{而}\ \text{`V215` §4 关于"三型皆单对象管道"的论证}\ \textbf{对 (d)(e) 无效} ⟹ \text{须单独审计}（\text{本档}）✓$$

---

## §2 ⭐ 定理级：**系数取值于离散环的整函数必为多项式**

$$\textbf{定理}：\text{设}\ R\subset\mathbb C\ \text{离散}（\text{无}\ \mathbb C\ \text{中聚点}），\ f(z)=\sum_{n\ge0}a_nz^n,\ a_n\in R,\ f\ \text{整} \Longrightarrow \boxed{f\ \text{为多项式}} ✓✓✓$$
$$\textbf{证明}：R\ \text{离散} \Longrightarrow \exists\delta>0:\ \forall r\in R\setminus\{0\},\ |r|\ge\delta;\ \text{若}\ a_n\ne0\ \text{则}\ |a_n|\ge\delta ✓$$
$$\qquad \Longrightarrow\ \limsup|a_n|^{1/n}\ge1 \Longrightarrow \text{收敛半径}\le1 \Longrightarrow f\ \text{整} \Longrightarrow \textbf{仅有有限个}\ a_n\ne0 ✓✓✓$$
$$\textbf{推论}：\text{整系数（或数域整环}\ \mathcal O_K／\mathbb Z[i]\ \text{等）的}\ \textbf{整函数必为多项式} ⟹ \textbf{零点有限} ⟹ \textbf{无法承载无限零集} ✓✓✓$$
$$\qquad ⚠️\ \text{同族经典}：\text{整系数幂级数的自然边界理论（Pólya--Carlson）};\ \text{本档}\ \textbf{直接给离散性论证}（\text{更短}）✓$$
$$\qquad ⭐\ \text{故你的例子}\ 1+z^2,\ 1+z^4\ \textbf{必为多项式}，\ \textbf{这不是巧合};\ \text{且}\ \textbf{轴外零点随便构造}（1+z^2\ \text{给}\ \pm i）⟹ \textbf{幂级数侧 integrality 接口 DEAD} ✓✓✓$$

---

## §3 ⭐⭐ Dirichlet 侧：整系数**不构成障碍**（$\zeta$ 自身即是）

$$\text{Setting II}：F(s)=\sum a_nn^{-s},\ a_n\in\mathbb Z\ \text{——}\ \textbf{§2 的论证不适用}（\text{收敛横坐标}\ne\text{系数增长}）✓$$
$$\qquad ⭐\ \zeta\ \text{本身}\ a_n\equiv1\in\mathbb Z ⟹ \textbf{整系数＋欧拉积＋FE 完全相容} ⟹ \text{整系数在此}\ \textbf{不产生任何约束} ✓$$
$$\qquad \text{而}：\text{Epstein}\ \zeta\ \text{有 FE}\ \textbf{却有 off-axis 零点}（\text{Potter--Titchmarsh}）⟹\ \text{D1 已录} ✓✓✓$$
$$\Longrightarrow\ \boxed{\text{FE ＋ 整系数 ＋ 欧拉积}\ \textbf{仍不能排除 off-axis}} ⟹ \textbf{DEAD} ✓✓✓$$
$$\qquad ⚠️\ \text{故}\ \text{"离散算术系数"接口在}\ \textbf{两个 setting 上都死}：\text{I 侧}\ \textbf{定理级};\ \text{II 侧}\ \textbf{经典反例级} ✓✓$$

---

## §4 ⭐⭐ 结构定理：**系数系统 ≡ 零点集**（本档核心一）

$$\text{对}\ \textbf{有限阶整函数}：\text{Hadamard}\ f=e^{A+Bs}\prod_\rho(1-s/\rho)e^{s/\rho} ⟹ \text{系数}\ \{a_n\}\ \textbf{由}\ \{\rho\}\ \text{决定} ✓$$
$$\qquad \text{反向}：\text{Newton 恒等式}\ \Longleftrightarrow\ \text{幂和}\ p_k=\sum\rho^{-k}\ \text{与初等对称函数}\ e_k\ \text{互定} ⟹ \{\rho\}\ \textbf{由}\ \{a_n\}\ \text{决定（差有限自由度）} ✓✓$$
$$\Longrightarrow\ \boxed{\text{有限阶情形下，"系数数据"与"零点集"是}\ \textbf{等价数据}} ✓✓✓$$
$$\qquad ⭐\ \text{故}\ \text{"系数接口"}\ \textbf{不是独立接口}，\ \text{它是}\ \textbf{零点集的重编码};\ \text{关于系数的陈述}\ =\ \text{关于零点的对称函数陈述} ✓$$
$$\qquad ⭐⭐\ \text{于是}\ \text{"系数刚性}\Longrightarrow\text{零点几何"}\ \textbf{精确翻译} \text{为}：$$
$$\qquad\qquad \boxed{\text{哪些（初等对称函数上的）条件迫使根全落在某条几何集合上}}$$
$$\qquad ⟹\ \text{而这}\ \textbf{就是} \text{实根性／hyperbolic／stable 多项式的}\ \textbf{经典理论}（Pólya--Schur--Lax、Hermite--Biehler、Jensen--Pólya、de Branges）⟹ \textbf{`V190`} ✓✓✓$$
$$\qquad ⚠️\ \text{故}\ \text{`V215` §4 的三型应}\ \textbf{修正为}：\text{系数接口}\ \textbf{归约为}\ \text{`V190` 通道}（\text{而非新增一型}）✓✓✓$$

$$\textbf{⭐ 你的最小模型（}F=F(-z)\text{）显式落地}：F(z)=\sum b_nz^{2n}=G(z^2) ✓$$
$$\qquad F\ \text{的零点}\ z=\pm\sqrt w\ \（w\ \text{为}\ G\ \text{的零点}）;\ \text{"}F\ \text{零点全在虚轴上（}a=0\text{）"}\iff \text{"}G\ \text{的零点全}\ <0\ \text{实"} ✓$$
$$\qquad \Longrightarrow\ \text{问题}\ \textbf{精确变成}：\text{"}G\ \text{的系数结构是否迫使}\ G\ \text{实根（且全负）"}\ =\ \textbf{实根性/LP 类问题} ⟹ \textbf{`V190`} ✓✓✓$$
$$\qquad ⚠️\ \text{验证}：G(w)=1+w ⟹ w=-1<0 ⟹ F=1+z^2\ \text{零点}\ \pm i\ \textbf{在轴上} ✓;\ G=1-w ⟹ w=1>0 ⟹ F=1-z^2\ \text{零点}\ \pm1\ \textbf{在轴外} ✓$$

---

## §5 逐类最小反例构造（你指定的六类 ＋ 一类）

$$\begin{array}{c|l|l}
\text{类} & \textbf{最小反例} & \text{结果}\\
\hline
(1)\ \mathbb Z／离散环 & \text{整函数} ⟹ \textbf{定理级为多项式}（\S2）;\ \text{多项式侧}\ 1+z^2\ \text{随便构造} & \textbf{定理级 DEAD}\ ✓✓✓\\
(2)\ \mathbb Z_p & \text{p-adic 整数性对 Dirichlet 系数自动成立（}\zeta\ \text{自身）};\ \text{有内容的 p-adic 对象是}\ \textbf{p-adic }L\text{（值的插值）} & \text{落 (b) 值通道}\ ✗\\
(3)\ \text{finite quotient／mod }p & \text{模}\ p\ \text{约化}\ \textbf{破坏解析对象}，只得形式数据;\ \text{Kummer 同余＝}\textbf{值}（}\zeta(1-n)\text{）} & \text{落 (b)}\ ✗\\
(4)\ \text{有限递推} & F=P/Q\ \text{（有理）} ⟹ \text{零点可任意布置} & \textbf{DEAD（你的 §8）}\ ✓\\
(5)\ ⭐\textbf{D-finite（多项式系数递推）} & \boxed{{}_1F_1(a;b;z)}\ \text{：}\textbf{整} ＋ \textbf{D-finite} ＋ \textbf{无限零点} ＋ \textbf{不在一条线} & \textbf{构造性 DEAD}\ ✓✓✓\\
(6)\ \text{乘法性／欧拉积} & \text{局部因子自由（`V173` 局部灵活性）} ⟹ \text{唯一性须全局约束} & \text{落 (c) archimedean}\ ✗\\
(7)\ \text{代数依赖／代数微分方程} & \text{落 (5) 族（D-finite 为其线性情形）};\ \text{且有限阶代数刚性不约束零点几何} & \text{DEAD}\ ✓\\
\end{array}$$
$$\qquad ⭐\ (5)\ \text{是最有分量的：}\textbf{有限阶代数/微分刚性}\ \textbf{不} \text{约束零点几何（解空间被参数化，不同参数把零点放到不同位置）} ✓✓✓$$
$$\qquad ⚠️\ \text{注意}：\text{"entire ＋ D-finite} \Longrightarrow \text{指数多项式"}\ \textbf{为假}（{}_1F_1\ \text{即反例}）⟹ \textbf{不得} \text{使用该断言} ✓$$

---

## §6 ⭐ 唯一"构造不出最小反例"的类（本档核心二）

$$\text{把条件加强到}\ \textbf{"强到能把所有零点钉到一条几何集合"}：\text{按定义}\ \text{它就是}\ \textbf{实根性型条件}:\ \Re=\text{const}\ \text{经旋转/平移等价于"根全实"} ✓$$
$$\qquad \text{而}\ \text{实根性型条件（对} \text{entire 函数）的}\ \textbf{完整经典刻画} = \textbf{Hermite--Biehler}／\textbf{Laguerre--Pólya 类}：$$
$$\qquad\qquad F(z)=e^{-az^2+bz+c}\prod_n\Bigl(1-\frac{z}{z_n}\Bigr)e^{z/z_n},\quad z_n\in\mathbb R,\ \sum|z_n|^{-2}<\infty ✓$$
$$\qquad \Longrightarrow\ \text{LP 类}\ \textbf{除指数因子外由其实零点决定} ⟹ \text{LP 类成员资格}\ \textbf{就是} \text{零点位置陈述} ✓✓$$
$$\Longrightarrow\ \boxed{\text{唯一能钉住零点几何的"无限阶系数刚性"＝LP/HB 类＝}\textbf{与结论同义反复}} \notin\ \text{新接口} ✓✓✓$$
$$\qquad \text{连接}：\text{`V190`／`V191`}\ \text{已确立该通道}\ \textbf{强度＝RH}（\text{不能由严格更弱的命题推出}）✓✓✓$$
$$\qquad \text{无限阶递推若钉零点到一条线，必落四者之一}：\text{hyperbolicity}／\text{positivity}／\text{spectral det}／\text{显式编码} ⟹ \textbf{皆旧墙（你的 §8 末）} ✓$$

---

## §7 判词与纪律

$$\boxed{\textbf{V216：DEAD} —— \text{系数／值域接口}\ \textbf{不构成独立接口}} ✓✓✓$$
$$\qquad \textbf{三条独立理由}：\text{(i)}\ \text{幂级数侧}\ \textbf{定理级}（\text{离散系数整函数必为多项式}）✓✓✓;\quad \text{(ii)}\ \text{Dirichlet 侧}\ \textbf{经典反例级}（\text{Epstein／Potter--Titchmarsh}）✓✓✓;\quad \text{(iii)}\ \textbf{结构定理}：\text{系数数据}\equiv\text{零点数据}，\ \text{归约为}\ \textbf{`V190` 实根性通道} ✓✓✓$$
$$\qquad \textbf{故}\ \text{`V215` §4}\ \textbf{应修正为}：\ \text{接口共五类，其中 (d)(e)}\ \textbf{经本档审计归约} \text{到 (a)(b)(c)＋`V190`} ⟹ \text{三型（＋归约后的两型）}\ \textbf{方为穷尽} ✓✓✓$$
$$\qquad ⚠️\ \textbf{纪律（唐先生）}：\textbf{不得} \text{声称"所有 arithmetic coefficient rigidity DEAD"};\ \text{本档实际证明的是三项（定理级／反例级／结构归约）};\ \textbf{不是} \text{全称否定} ✓✓$$
$$\qquad ⚠️\ \text{残余（UNINSTANTIATED）}：\text{一个}\ \textbf{既非 LP/HB 类、又能钉住零点几何} \text{的}\ \textbf{无限阶系数刚性};\ \text{本档未见实例};\ \text{判据}：\text{① 非实根性型};\ \text{② 非正性};\ \text{③ 非谱行列式};\ \text{④ 非显式编码} ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§2 的离散性论证为}\ \textbf{本档推导}（\text{两行}）;\ \text{与 Pólya--Carlson 同族} ✓✓✓$$
$$\textbf{(b)}\ \text{§3 的 Epstein／Potter--Titchmarsh 为}\ \textbf{经典}（\text{D1 已录}）✓✓$$
$$\textbf{(c)}\ \text{§4 的"系数}\equiv\text{零点"基于}\ \textbf{Hadamard ＋ Newton}（\text{有限阶}）✓✓;\ \text{无限阶或增长条件异常时}\ \textbf{待核} ⚠️$$
$$\textbf{(d)}\ \text{§5 的}\ {}_1F_1\ \text{反例为}\ \textbf{经典事实}（\text{entire、D-finite、无限零点}）✓✓✓$$
$$\textbf{(e)}\ \text{§6 的 LP／HB 刻画为}\ \textbf{经典}（Laguerre--Pólya 类）✓✓✓;\ \text{"LP}\equiv\text{零点位置陈述"为}\ \textbf{本档判断} ✓$$
$$\textbf{(f)}\ \text{§7 的"五类穷尽"仍是}\ \textbf{归约} \text{而非定理};\ \textbf{不} \text{升级为否定性全称} ✓$$

```
⚠️ §0 委托（R3 强化形式／§4 漏洞／系数结构／最小模型／旧墙／离散算术性质／第一非平凡例子／有限递推／五类升级／纪律／V216 指令）为唐先生逐字 ✓✓✓
⚠️ §1 确认 V215 §4 非穷尽；升级为五类接口；指出 V215 的"单对象管道"论证对 (d)(e) 无效 ✓✓
⚠️ §2 ⭐ 定理级：离散取值环系数的整函数必为多项式（两行证明）⟹ 幂级数侧 integrality 接口 DEAD ✓✓✓
⚠️ §3 ⭐⭐ Dirichlet 侧：整系数不构成障碍（zeta 自身）；Epstein/Potter-Titchmarsh ⟹ DEAD ✓✓✓
⚠️ §4 ⭐⭐ 结构定理：有限阶整函数"系数≡零点"（Hadamard+Newton）⟹ 系数接口＝零点重编码 ⟹ 精确翻译为实根性理论 ＝ V190；你的最小模型 F=F(−z) 显式落地 ✓✓✓
⚠️ §5 七类逐类最小反例：(1) 定理级；(2) ℤ_p ⟹ 值通道；(3) mod p ⟹ 值通道；(4) 有限递推 DEAD；(5) ⭐ ₁F₁ 构造性 DEAD；(6) 乘法性 ⟹ 局部自由 ⟹ archimedean；(7) 代数依赖 ⟹ DEAD；并纠正"entire+D-finite ⟹ 指数多项式"为假 ✓✓✓
⚠️ §6 唯一无最小反例者 ＝ 实根性型无限阶刚性 ＝ LP/HB 类 ＝ 与结论同义反复 ⟹ 非新接口 ✓✓✓
⚠️ §7 判词 DEAD（三条理由）；V215 §4 修正为五类；纪律：不得全称否定；残余（非 LP/HB 的无限阶刚性）✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 定理级封 Setting I（离散系数整函数必为多项式）✓✓✓；② 经典反例封 Setting II ✓✓✓；
   ③ 结构定理：系数接口＝零点重编码 ⟹ 归约 V190 ✓✓✓；④ 七类最小反例（含 ₁F₁）✓✓✓；
   ⑤ 指出唯一"构造不出反例"者即 LP/HB 类（同义反复）✓✓✓；⑥ 接口由三型修正为五类＋归约 ✓✓；⑦ 残余与判据 ✓
```
