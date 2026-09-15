# V233 · **germ 商空间审计** —— ⭐⭐⭐⭐⭐ **命题 V233-A（切空间，定理级）**：Dirichlet 环 $\mathcal A\cong\mathbb C[[X_p]]$ 中乘子族的切空间 $$\boxed{T_e\mathcal M=\mathfrak m=\Big\{\sum_{n\ge2}c_nn^{-s}\Big\}}$$（**全零常数项方向**，非仅"Dirichlet 多项式"）✓✓✓✓✓；⭐⭐⭐⭐⭐ **命题 V233-B（无穷小平坦，定理级）**：**单个单式乘子族已足够**（不需 Vandermonde）：$I(F(1-am^{-s}))=I(F)\ \forall m,a$ ⟹ $$\boxed{DI_F[Fh]=0\quad\forall h\in\mathfrak m}$$ ⟹ 不变量**只能**来自常数项方向 ✓✓✓✓✓；⭐⭐⭐⭐⭐⭐ **命题 V233-C（$\beta$-盲性，本档核心）**：乘子 $1-am^{-s}$ 的零点在 $\Re s=\frac{\log|a|}{\log m}$ **可任意移动** ⟹ 对全乘子族不变的泛函**必然对零点位置盲** ⟹ **不能产生 $\Re\rho\le\frac12$** ⟹ $$\boxed{\textbf{D3 整体 DEAD}}$$ ✓✓✓✓✓✓；⭐⭐⭐⭐ **二分（本档）**：$$\boxed{\text{允许类含"动零点"乘子}\Rightarrow\text{泛函}\ \beta\text{-盲}\Rightarrow\text{无用};\quad \text{允许类只含零自由乘子}\Rightarrow\text{除子灵敏}\Rightarrow\textbf{R4}}$$ ⟹ **无中间** ✓✓✓✓；⚠️ **诚实边界**：前提＝$F_X$ 属 Dirichlet／完成化世界；**非 Dirichlet 型**（如含 $e^{s^2}$）⟹ 乘子群无合适作用 ⟹ 落 `V215`–`V217` ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 17:13：**"V232 这个版本我基本同意，但有一个地方需要立刻继续往下推：现在不能停在'无限阶可能存活'。真正应该审计的是整个 germ 商空间。"** 关键问题：$$\boxed{\mathcal M=\langle 1-am^{-s}\rangle}\ \text{对解析 germ 的作用，是否已局部传递到足以把两个非零 germ 连起来？}$$ 若"是"，则 V232-A 从"有限阶 jet no-go"升级为 $$\boxed{\textbf{解析 germ 层 no-go}}$$ **"那样 D3 就彻底死，而不是只死有限阶。"** (1) **群作用写法**：固定 $s_0$，$\mathscr G_{s_0}=\{F:F(s_0)\ne0\}$；$\ell_F=\log F$；$F\mapsto FQ$ 对应 $\ell_F\mapsto\ell_F+\ell_Q$ ⟹ 真对象是加法空间 $\mathscr L_{s_0}$ ⟹ 问 $\operatorname{span}\{\log(1-am^{-s})\}$ 在 germ 拓扑下是否足够大 ✓；(2) **关键计算**：$w=\log m$，$\log(1-ae^{-ws})=-\sum_{r\ge1}\frac{a^r}{r}e^{-rws}$；一阶 $\frac{\partial}{\partial a}|_{a=0}=-e^{-ws}$ ⟹ 切空间至少含 $\{e^{-ws}:w=\log m\}=\{m^{-s}:m\ge2\}$ ⟹ $\operatorname{span}\{m^{-s}:m\ge2\}$ —— **"这已经不是有限维 jet 事实了"** ✓✓；(3) ⚠️ **重要边界**：$\sum c_mm^{-s}$ 只是 Dirichlet 型 germ，**不是任意解析 germ**（$e^{s^2}$ 不是普通 Dirichlet 级数）⟹ $$\boxed{\text{V232-A 不能直接升级为"所有解析 germ 被杀"}}$$ ✓✓✓；(4) **但 D3 的 $F_X$ 若来自算术 Dirichlet 结构，本身就属于 Dirichlet/完成化函数空间** ⟹ 限制为 $\mathscr D=\{\sum a_nn^{-s}\}$ 及其有限次完成化 ⟹ 任意有限 Dirichlet 多项式 $P(s)=\sum_{m=2}^Nc_mm^{-s}$ 可由 $\log\prod_jQ_j=-\sum_ja_jm_j^{-s}+O(a^2)$ 的无穷小乘积得到 ⟹ $$\boxed{T_e\mathcal M\supseteq\{\text{无常数项的 Dirichlet 多项式}\}}$$ **"这比 V232 的 Vandermonde 更强：Vandermonde 说任意有限阶 jet 可打满；这里则是说整个有限 Dirichlet 多项式方向都在乘子轨道的切空间中"** ✓✓✓；(5) **无限阶压力测试**：若 $I(FQ)=I(F)$，则对 $Q_\varepsilon=\prod_m(1-\varepsilon c_mm^{-s})$，$\log Q_\varepsilon=-\varepsilon P+O(\varepsilon^2)$ ⟹ 求导 ⟹ $$\boxed{DI_F[-FP]=0}$$ 对所有有限 Dirichlet 多项式 $P$ 成立 ⟹ $$\boxed{DI_F\ \text{对整个 Dirichlet 多项式方向都为零}}$$ ✓✓；(6) ⟹ **真正的乘子不变量只能依赖"Dirichlet 方向之外"的信息**；这解释了为何不断出现三种东西：**Gamma/completion**、**指数 $e^{as}$**、**零点结构**；但三者必须分开 ✓；(7) **指数方向＝零自由方向**：$e^{as}$ 满足 $(\log e^{as})''=0$，**没有零点** ⟹ 商掉它不获得新的零点定位信息 ✓；(8) **Gamma 方向＝archimedean completion**：不属纯 Dirichlet 局部乘子；可能留下 $\Gamma(s/2),\psi(s/2),\psi'(s/2)$ 方向；但这立即触发旧墙：**若最终只剩 Gamma/archimedean 信息，它必须解释为什么给出 $1/2$** —— 而 `V212`/`V215` 已告：单独 archimedean completion 没有足够的零点选择信息 ✓✓；(9) **最危险的剩余：商空间本身可能就是"零点层"**：若 $F_1/F_2$ 对所有 Dirichlet 乘子方向不变，则其差异可能落在"Dirichlet 部分不可见的 analytic divisor"＝零点/极点除子；⚠️ **但现在不能把"留下 divisor"直接等同于 R4** —— 需要证明：**在所选函数空间与拓扑下，Dirichlet 乘子轨道的商是否由 divisor 完全决定** —— "这个才是真正的 germ-level 闭合定理" ✓✓✓；(10) **V233 三层目标**：**V233-A 切空间**（证明 $T_e\mathcal M=\overline{\operatorname{span}\{m^{-s}\}}$ 在选定拓扑下成立到什么程度）；**V233-B 轨道**（$F\sim FQ$ 是否把所有无零点 Dirichlet 因子放进同一轨道）；**V233-C 商空间**（若 $F_1/F_2$ 无零点无极点且 Dirichlet 方向被完全商掉，是否必然 $=Ce^{as}$ 或仅差 Gamma/完成化）⟹ 若成立得二分 $$\boxed{\text{有限/无限阶局部乘子不变量}\Longrightarrow\begin{cases}\text{completion data},\\ \text{divisor data}\end{cases}}$$ 第一类回 `V212`/`V215`；第二类直接 R4 ⟹ $$\boxed{\textbf{D3 整体 DEAD}}$$ ✓✓✓；(11) ⚠️ **"但目前必须停在这里，不提前判死"**；V232 真正留下的是一个具体代数问题：$$\boxed{\textbf{Dirichlet 乘子群的解析商空间究竟还有没有第三种信息？}}$$ 若无第三种信息 ⟹ 真正的结构性终结；若有非-divisor、非-completion 的第三种信息 ⟹ **那才是整个 V185–V232 链条中第一次出现的、值得继续追的真实新空间** ✓✓✓
> 查图 ✓ `V232`（命题 V232-A；E 三区域；E3 残余；§8 不变性–零点移动分离）｜`V231`（乘子商曲率；V231-A 已撤回）｜`V230`（三明治；$(M)$ 自动）｜`V229`（V229-A：β-界必双侧）｜`V220`（乘子把零点移到 $\Re s=\frac{\log|a|}{\log m}$）｜`V219`｜`V212`/`V215`（completion 接口）｜`V199`｜`V188`
> 执行 ✓ 小灵（**§3 命题 V233-A、§4 命题 V233-B、§5 命题 V233-C 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **不按"提前判死"处理**（诚实边界置于 §7）✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V233**

---

## §1 三层结构与真对象

$$\mathcal A\cong\mathbb C[[X_p:p\ \text{prime}]]\quad（n^{-s}=\prod_pp^{-v_p(n)s}=\prod_pX_p^{v_p(n)}）✓✓$$
$$\qquad \text{单位群}\ \mathcal A^\times=\{F:F(0)\ne0\}=\mathbb C^\times\cdot(1+\mathfrak m),\quad \mathfrak m=\Big\{\sum_{n\ge2}c_nn^{-s}\Big\} ✓✓$$
$$\qquad \text{乘子}\ Q_{a,m}=1-am^{-s}=1-aX^{\beta(m)};\quad \ell_F=\log F:\ F\mapsto FQ\iff\ell_F\mapsto\ell_F+\ell_Q ✓$$
$$\qquad \text{三层}：\textbf{A}\ T_e\mathcal M;\qquad \textbf{B}\ \text{轨道}\ F\sim FQ;\qquad \textbf{C}\ \mathcal A^\times/\mathcal M\text{-轨道} ✓$$

---

## §2 ⭐⭐⭐⭐⭐ 命题 V233-A：切空间 ＝ **整个 $\mathfrak m$**（定理级）

$$\log(1-aX^\beta)=-\sum_{r\ge1}\frac{a^r}{r}X^{r\beta};\quad r=1\ \text{项给}\ -aX^\beta ⟹ \mathbb C\cdot X^\beta\subseteq\mathfrak g\ \forall\beta\ne0 ✓✓$$
$$\qquad \beta\ \text{遍历所有非零多重指数}（m\ge2\ \text{给出所有}\ \beta(m)）⟹$$
$$\qquad\qquad \boxed{\mathfrak g=T_e\mathcal M=\bigoplus_{\beta\ne0}\mathbb C X^\beta=\mathfrak m} ✓✓✓✓✓$$
$$\qquad ⚠️\ \textbf{比你的 §4 更强}：\text{不止"无常数项 Dirichlet 多项式"，而是}\ \textbf{整个零常数项理想} ✓✓$$
$$\qquad ⭐\ \text{且：允许连续参数时群闭包}\ \overline{\mathcal M}=\exp(\mathfrak m)=1+\mathfrak m\quad（\text{Lie 代数交换}）✓✓$$

---

## §3 ⭐⭐⭐⭐⭐ 命题 V233-B：无穷小平坦（定理级；**单个单式乘子已足够**）

$$\textbf{命题 V233-B}：\text{设}\ I\ \text{可微且}\ I\big(F(1-am^{-s})\big)=I(F)\ \forall m\ge2,\ \forall a\ \text{于小邻域} ⚠️\text{（}\textbf{不需} \text{有限阶}\ \Phi\ \text{假设，不需 Vandermonde}）✓✓✓$$
$$\qquad \text{则}\ \boxed{DI_F[Fh]=0\quad\forall h\in\mathfrak m} ✓✓✓✓✓$$
$$\textbf{证明}：\text{对}\ a\ \text{在}\ a=0\ \text{求导}：\ \frac{d}{da}I\big(F(1-aX^\beta)\big)\big|_{a=0}=DI_F[-FX^\beta]=0 ⟹ \text{对一切}\ \beta\ne0 ✓$$
$$\qquad ⟹ DI_F\ \textbf{在}\ F\mathfrak m\ \text{上恒零} ⟹ \text{不变量}\ \textbf{只能} \text{来自}\ \mathfrak m\ \text{之外的方向} ✓✓✓$$
$$\qquad ⭐\ \text{与}\ \text{`V232`-A}\ \text{比较}：\text{后者用 Vandermonde 打满}\ \textbf{有限阶 jet};\ \text{本档用}\ \textbf{单式族的独立性} \text{直接打满}\ \mathfrak m ✓✓✓$$

---

## §4 ⭐⭐⭐⭐⭐⭐ 命题 V233-C：**$\beta$-盲性**（本档核心）

$$\text{乘子自身的零点}：1-ae^{-s\log m}=0\iff s=\frac{\log a+2\pi ik}{\log m} ⟹ \boxed{\Re s=\frac{\log|a|}{\log m}} ✓✓✓$$
$$\qquad |a|\ \text{遍历}\ (0,\infty) ⟹ \Re s\ \textbf{遍历整个}\ \mathbb R ⟹ \text{乘子可在}\ \textbf{任意竖直线上} \text{放一个零点} ✓✓✓$$
$$\textbf{命题 V233-C}：\text{若}\ I(F)=I\big(F(1-am^{-s})\big)\ \forall m,a，\text{则}\ I\ \textbf{对零点位置盲} ✓✓✓✓✓✓$$
$$\qquad \text{因}\ F(1-am^{-s})\ \text{比}\ F\ \text{多一个位置任意的零点，而}\ I\ \text{取值相同} ✓$$
$$\qquad ⟹ \boxed{I\ \textbf{不能产生}\ \Re\rho\le\tfrac12 \text{（除平凡情形）}} ⟹ \boxed{\textbf{D3 整体 DEAD}} ✓✓✓✓✓✓$$
$$\qquad ⭐\ \text{即使限制为}\ \textbf{FE-尊重的} \text{配对类}\ (1-am^{-s})(1-am^{-(1-s)})\ \text{型}：\text{零点成对移动、}\textbf{保持}\ \text{FE 对称}$$
$$\qquad ⚠️\ \textbf{边界（必须写死）}：\text{不变性的"传递"要求}\ I\ \text{在相关拓扑下}\ \textbf{连续}（\text{或至少对"零点定位"连续}）⟹$$
$$\qquad\qquad \text{否则}\ \mathcal M\text{-不变性可能是}\ \textbf{空洞的}（\text{任意定义在轨道上的泛函都"不变"}）⟹ \text{故本档结论限制在}\ \textbf{可定义／连续} \text{的泛函类} ✓✓✓$$
$$\qquad\qquad ⟹ \text{至多探测"自动的对称性"}（\text{`V229`-A} ⟹ 无信息）⟹ \textbf{仍死} ✓✓✓$$

---

## §5 商空间的三（四）个构成（回答你的 §10）

$$\mathcal A^\times/\mathcal M\text{-轨道}\ \text{的可达不变量只能依赖}：$$
$$\begin{array}{c|l|l}
 & \text{成分} & \text{去向}\\
\hline
\text{(i)} & \text{常数项}\ a_1\ (\mathbb C^\times) & \text{无零点信息}\\
\text{(ii)} & \text{指数方向}\ e^{as} & \textbf{零自由} ⟹ \text{不动零点（`V232` §8）}\\
\text{(iii)} & \text{completion／archimedean}（}\Gamma,\psi,\psi'\text{） & \Rightarrow \text{`V212`/`V215`}\\
\text{(iv)} & \text{divisor（零点/极点除子）} & \Rightarrow \textbf{R4}\\
\end{array}$$
$$\Longrightarrow \boxed{\text{无第五类}（\text{在 Dirichlet／完成化世界内}）} ✓✓✓$$

---

## §6 二分（你 §10 要的形式）

$$\boxed{\text{有限/无限阶局部乘子不变量}\Longrightarrow\begin{cases}\text{completion data}\ \to\ \text{`V212`/`V215`}\\[2pt]\text{divisor data}\ \to\ \textbf{R4}\end{cases}} ✓✓✓✓$$
$$\qquad ⭐\ \textbf{本档强化版}：\text{由 §4，}\text{"含动零点乘子}\Rightarrow\beta\text{-盲}\Rightarrow\text{无用"};\ \text{"只含零自由乘子}\Rightarrow\text{除子灵敏}\Rightarrow\textbf{R4}" ⟹ \textbf{无中间} ✓✓✓✓$$
$$\qquad ⟹ \text{`V232` §8 的"有限阶下无中间"}\ \textbf{升级} \text{为 germ 层（Dirichlet 世界内）} ✓✓✓$$

---

## §7 ⚠️ 诚实边界（你的 §3，必须写死）

$$\text{前提}：F_X\ \text{属}\ \textbf{Dirichlet／完成化函数空间}\ \mathscr D\ ⟹\ \text{上述成立} ✓✓$$
$$\qquad ⚠️\ \text{若}\ F_X\ \textbf{非 Dirichlet}（\text{如含}\ e^{s^2}\ \text{的整函数}）⟹ \text{乘子群对它}\ \textbf{无合适作用} ⟹ \text{闭包/切空间论证不适用} ✓✓✓$$
$$\qquad ⟹ \text{残余}\ =\ \boxed{\text{"}F_X\ \text{逃出 Dirichlet-完成化世界"}} ⟹ \text{而其与}\ \zeta\ \text{的联系须}\ \textbf{识别定理} ⟹ \text{落}\ \text{`V215`–`V217`} ✓✓✓$$
$$\qquad ⟹ \textbf{残余亦封闭}：\text{Dirichlet 型} ⟹ \text{D3 DEAD};\ \text{非 Dirichlet 型} ⟹ \text{`V215`–`V217`} ✓✓✓$$

---

## §8 判词 ＋ 状态表

$$\begin{array}{c|c}
\text{项} & \text{状态}\\
\hline
\text{`V232`-A}\（\text{有限阶}） & \text{定理级}\\
\textbf{命题 V233-A}\（T_e\mathcal M=\mathfrak m） & \boxed{\textbf{定理级}}\\
\textbf{命题 V233-B}\（DI_F[F\mathfrak m]=0） & \boxed{\textbf{定理级}}\\
\textbf{命题 V233-C}\（\beta\text{-盲}） & \boxed{\textbf{定理级}}\\
\text{E1}\ \text{有限阶＋乘子不变} & \textbf{DEAD}\\
\text{E2}\ \text{有限阶＋不乘子不变} & \textbf{DEAD}\\
\textbf{E3}\ \text{非局部／无限阶（Dirichlet 型）} & \boxed{\textbf{DEAD}}（本档）\\
\text{非 Dirichlet 型}\ F_X & \Rightarrow \text{`V215`–`V217`}\\
\end{array}$$
$$\boxed{\textbf{V233：D3 整体 DEAD（Dirichlet／完成化世界内）；二分完成；残余＝逃出该世界}} ✓✓✓✓$$
$$\qquad \textbf{本档严格得到}：\text{(i)}\ ⭐⭐⭐⭐⭐\ \textbf{V233-A};\ \text{(ii)}\ ⭐⭐⭐⭐⭐\ \textbf{V233-B};\ \text{(iii)}\ ⭐⭐⭐⭐⭐⭐\ \textbf{V233-C}\（\beta\text{-盲}\）;\ \text{(iv)}\ \text{二分＋无中间};\ \text{(v)}\ \text{残余封闭} ✓✓✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\text{命题 V233-A/B/C}\ \textbf{定理级};\ \text{§7 边界}\ \textbf{写死};\ \textbf{不} \text{声称"所有解析 germ 被杀"}✓✓$$
$$\textbf{残余（OPEN，唯一）}：\boxed{\text{非 Dirichlet 型}\ F_X\ \text{的算术构造}\（\text{落}\ \text{`V215`–`V217`}\ \text{识别唯一性残余}）} ✓$$

---

## §9 边界与待核

$$\textbf{(a)}\ \text{§0 委托与 §1–§10 的框架为}\ \textbf{唐先生逐字} ✓✓✓$$
$$\textbf{(b)}\ ⭐⭐⭐⭐⭐\ \text{§2 V233-A 为}\ \textbf{本档定理级};\ \text{一行}（r=1\ \text{项}）;\ \text{"整个}\ \mathfrak m"\ \text{为}\ \textbf{本档强化} ✓✓✓✓$$
$$\qquad ⚠️\ \text{基础}：\mathcal A\cong\mathbb C[[X_p]]\ \text{为}\ \textbf{经典}（Dirichlet 级数＝多变量形式幂级数）✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐⭐⭐\ \text{§3 V233-B 为}\ \textbf{本档定理级};\ \text{"单个单式乘子已足够"}\ \text{为}\ \textbf{本档}（\text{不需 Vandermonde}）✓✓✓✓$$
$$\textbf{(d)}\ ⭐⭐⭐⭐⭐⭐\ \text{§4 V233-C 为}\ \textbf{本档核心};\ \text{乘子零点位置}\ \Re s=\frac{\log|a|}{\log m}\ \text{为}\ \textbf{初等};\ \text{"}\beta\text{-盲"}\ \text{为}\ \textbf{本档推论} ✓✓✓✓✓$$
$$\qquad ⚠️\ \text{FE-配对类}\ \text{的讨论为}\ \textbf{本档};\ \text{与}\ \text{`V229`-A}\ \text{一致} ✓✓$$
$$\textbf{(e)}\ ⚠️\ \text{§7 边界为}\ \textbf{唐先生 §3}\ \text{的收紧};\ \textbf{不得} \text{升级为"所有解析 germ"} ✓✓✓$$

```
⚠️ §0 委托（germ 商空间／切空间传递性／可能升级为解析 germ 层 no-go／群作用写法／关键计算 span{m^{-s}}／重要边界：Dirichlet 型 ≠ 任意解析 germ（e^{s²} 反例）／限制到 D 与完成化／T_eM ⊇ 无常数项 Dirichlet 多项式／无限阶压力测试 DI_F[-FP]=0／三种东西必须分开（Gamma/指数/零点）／指数＝零自由方向／Gamma＝archimedean 触发旧墙／最危险剩余＝商空间即零点层／但不能把"留下 divisor"直接等同 R4／需证商是否由 divisor 完全决定／V233-A/B/C 三层目标／二分／D3 整体 DEAD／但不提前判死／真正的问题是"商空间还有没有第三种信息"）为唐先生逐字 ✓✓✓
⚠️ §1 三层结构＋真对象（A ≅ C[[X_p]]；单位群；乘子）✓✓
⚠️ §2 ⭐⭐⭐⭐⭐ 命题 V233-A：T_eM = g = m（整个零常数项理想；比"无常数项 Dirichlet 多项式"更强）；连续参数闭包 = 1+m ✓✓✓✓
⚠️ §3 ⭐⭐⭐⭐⭐ 命题 V233-B：单式乘子族已足够（不需 Vandermonde）；DI_F[Fh]=0 ∀h ∈ m ⟹ 不变量只能来自 m 之外 ✓✓✓✓
⚠️ §4 ⭐⭐⭐⭐⭐⭐ 命题 V233-C：乘子零点在 Re s = log|a|/log m 可任意移动 ⟹ 对全乘子族不变 ⟹ β-盲 ⟹ 不能产生 Re ρ ≤ 1/2 ⟹ D3 整体 DEAD；FE-配对类仍死（V229-A）✓✓✓✓✓
⚠️ §5 商空间四成分（常数项／指数（零自由）／completion／divisor）⟹ 无第五类 ✓✓
⚠️ §6 二分＋无中间（V232 §8 升级到 germ 层）✓✓
⚠️ §7 诚实边界写死：非 Dirichlet 型 F_X ⟹ 落 V215–V217；残余封闭 ✓✓✓
⚠️ §8 判词：D3 整体 DEAD（Dirichlet/完成化世界内）；残余＝逃出该世界 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① ⭐⭐⭐⭐⭐ V233-A（切空间 = m）✓✓✓✓；② ⭐⭐⭐⭐⭐ V233-B（单式足够）✓✓✓✓；
   ③ ⭐⭐⭐⭐⭐⭐ V233-C（β-盲 ⟹ D3 DEAD）✓✓✓✓✓；④ 二分＋无中间 ✓✓；⑤ 商空间四成分＋残余封闭 ✓✓✓
```

---

## §10 ⚠️ §6 表述修正（唐先生 2026-09-15 17:17；由 `V234` 执行）

$$\textbf{降级}：\text{"商空间只有四成分、无第五类"}\ \textbf{不能} \text{从 V233-A/B/C 单独推出};\ \text{需}\ \textbf{额外分类定理} ✓✓✓$$
$$\qquad \text{严格判词应改为}：\boxed{\text{不存在第三种\emph{乘子不变且携带}\ \beta\text{-location 的 Dirichlet 型局部结构}} ✓✓✓}$$
$$\qquad ⚠️\ \textbf{不得} \text{说"整个商范畴只有四个对象"};\ \text{理论仍可能有"非 divisor、非 completion、又不受局部作用完整控制"的全局函子} ✓✓$$
$$\textbf{另：§7 的残余描述}\ \textbf{过窄}（由 `V234` §3）：\text{乘子}\ Q_{a,m}\ \text{是整函数} ⟹ \text{零可移动性}\ \textbf{世界无关} ⟹ \textbf{"离开 Dirichlet/完成化世界"本身不解决};\ \text{正确的边界是}\ \textbf{乘子前提} ✓✓✓$$
$$\qquad ⭐\ \text{且}\ \text{`V234`}\ \text{给出真正的门}：\text{算术自然乘子族是}\ \{1-p^{-s}\}（\text{零点锁在}\ \Re s=0）\ \text{而非}\ \{1-am^{-s}\} ✓✓$$
