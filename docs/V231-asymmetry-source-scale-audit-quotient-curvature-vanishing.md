# V231 · **不对称源的尺度审计 ＋ 乘子商曲率消退定理** —— ⚠️ **§6 修正落档**："算术中唯一不对称特征是 $s=1$ 的极点/收敛横坐标"**不能作为结构性结论**；算术里有多类**定向结构**；真问题 = $$\boxed{\text{什么样的不对称能产生 }\tfrac12\text{ 而非 }1}$$ ✓✓✓；⭐ **五种不对称 A–E 判定表**：A 收敛方向→1，B 极点→1，C 系数方向→正性族→$1-c/\log t$，D 尺度→$1,0,\log x$（平方根型被 V219 杀转移），**E 微分方向 = D3 真正残余** ✓✓✓；⭐⭐ **内部不动点要求**：$\frac12$ 必须是机制的内部不动点（非外常数 $aL+b$）⟹ 自然来源＝二阶尺度平衡 $X^2=Y$；⭐⭐⭐ **命题 V231-A（定理级）**：**在 Dirichlet 级数乘法结构下，$(\log F)''$ 只对常数乘子不变** ⟹ 非平凡"乘子商曲率"要求 $E_X$ 落在**非乘性类** ＝ **完成化层** ✓✓✓✓；⭐⭐⭐⭐ **命题 V231-B（定理级）**：**对 $\zeta$，全部已知函数结构 ＝ 已知因子（Euler 积 × Γ × 平凡零点 × $e^{Bs}$）之积；商尽已知因子后残余恰为 $\{\rho\}$** ⟹ 故：(i) 允许类 $\supseteq$ 已知因子 ⟹ $\mathcal K_X$ **退化为零点泛函**（R4）；(ii) 允许类 $=$ 有限局部因子 ⟹ 内容落**素数侧**，而素数侧≡零点侧**就是显式公式**（显式公式类）✓✓✓✓✓✓；**回答你的存在性压力测试：对两类自然选择＝必然等价；第三类未审**；⭐⭐⭐⭐ **D3 普通微分曲率 FAIL（乘子测试失败）** ✓✓✓✓

> 委托 ✓ 唐先生 2026-09-15 17:03：**"§6 有一个地方建议现在就纠正：'算术中唯一不对称特征是 $s=1$ 的极点/收敛横坐标'不能作为结构性结论。算术里确实有很多天然的定向结构。真正的问题不是'有没有不对称'，而是：$$\boxed{\text{什么样的不对称能够产生}\ \tfrac12\text{，而不是}\ 1?}$$ 这可以直接做成 V231。"** (1) **精确定义**：设 $\Omega_X$ 独立于 $Z(\xi)$，且 $Z(\xi)\subseteq\Omega_X$；要得 RH 须 $\Omega_X\subseteq\{\sigma\le\tfrac12\}$；任何有效的不对称源 $A_X$ 必须产生临界位置 $c(A_X)=\frac12$，且该等式**独立于 RH**；⚠️ $c=1$ 没用；$c=1-c/\log t$ 没用；$c=\frac12+\varepsilon$ 没用 ✓；(2) **五种不对称**：**A 收敛方向**（Dirichlet $\sum a_nn^{-s}$ 有 $\sigma\to+\infty$ 收敛方向，$\zeta$ 的 $\sigma_c=1$）⟹ **A 型天然给 1，不是 1/2**；**B 极点方向**（$\zeta$ 在 $s=1$ 极点，绝对定向 1；与 FE 轴的关系是 $1-\frac12=\frac12$ —— 极点知道"另一侧在哪"，但没有给出"中点为什么必是临界边界"）；**C 系数方向**（$a_n\ge0,\Lambda(n)\ge0$ — 非常强的不对称：$n\to+\infty$ 被选定，正负系数不等价；产生单调性/正性/convexity，而非固定 1/2；这就是经典 zero-free region 能从这里出来却停在 $1-c/\log t$ 的原因）；**D 算术尺度方向**（$n,\log n,p,\Omega(n),\omega(n)$ 给天然尺度，产生 $1,0,\log x$；除非出现平方根 $x\mapsto\sqrt x$，否则无 1/2；而 V219 已证：$\sum\Lambda(n)^2\sim x\log x$ 中的平方根虽产生数值 1/2，却不能自动变成零点实部）；**E 离散差分/导数方向** —— **目前唯一不能马上封死的一类**；如 $F_X(\sigma,t)$ 满足二阶结构 $F_{\sigma\sigma}-\lambda_XF_\sigma+\mu_XF\ge0$，或 $FF_{\sigma\sigma}-F_\sigma^2\ge0$；这不是单纯"正性"，而是**方向性的微分几何** ⟹ **E 型仍是 D3 的真正残余** ✓✓✓；(3) **强事实**：所有普通一阶尺度不够；若机制只给自然尺度 $L_X$，临界位置通常是 $c_X=L_X$ 或 $aL_X+b$（$a,b$ 外准则是人为归一化）；**真正需要：$\frac12$ 必须是机制的内部不动点，不是外常数**；(4) **自然产生内部 1/2 的结构**：二阶尺度平衡 $X^2=Y \Rightarrow \log X/\log Y = \frac12$；但 V219 ⟹ 单纯平方关系不够，必须与零点 admissibility 耦合 ⟹ **真正需要：算术二阶关系 + 复根实部的约束**；(5) **D3 精确指向**：$D_X(s)=F_XF_X''-(F_X')^2 = F_X^2(\log F_X)''$；若 $D_X(\rho)\ge0$ 且 $D_X(\sigma+it)<0\ (\sigma>\frac12)$ ⟹ $\Re\rho\le\frac12$；关键：**$\frac12$ 不应出现在 $D_X$ 的定义中，必须从 $F_X$ 的内部二阶结构自己出来**；(6) **乘子测试**：$F\mapsto FQ$ 时 $(\log(FQ))'' = (\log F)'' + (\log Q)''$ ⟹ $\frac{(FQ)(FQ)''-(FQ)'^2}{(FQ)^2} = (\log F)''+(\log Q)''$ ⟹ **二阶对数曲率不是乘子不变的** ⟹ **普通 $FF''-(F')^2$ 不能作为 zeta 的普适证书**；这是好结果：把"随便找微分不等式"的空间砍掉；(7) **修正/商曲率**：需**乘子消除后的曲率**；设 $F_X=E_X\cdot G_X$，$E_X$ 是所有允许局部乘子生成的"可积部分"；定义 $\mathcal K_X[F_X] := (\log F_X)''-(\log E_X)''$，则对允许乘子类 $\mathcal M$ 中 $G$，$\mathcal K_X[F_XG]=\mathcal K_X[F_X]$；这**不是普通 normalization**，是**商掉可积乘子后的二阶曲率**；若 $\mathcal K_X(\rho)\ge0$ 且 $\mathcal K_X(\sigma+it)<0\ (\sigma>\frac12)$ ⟹ 真正不同于 V199 的机制：**arithmetic curvature → zero admissibility**；(8) **第二个致命审计**：若 $E_X$ 把 Euler/Dirichlet/gamma/explicit-formula/Hadamard 因子都除掉了，则 $E_X$ 可能是已知结构之一 ⟹ "乘子消除"可能只是重包装 zeta 的已知解析结构 ⟹ 所以要求：**$E_X$ 必须由独立算术代数定义，不能由 $\xi$ 的因子分解定义**；否则立即 DEAD；(9) **新候选机制**：**Arithmetic quotient-curvature**，要求 Q1–Q6（$\mathcal K_X$ 独立于 $Z(\xi)$；对允许乘子不变；$\mathcal K_X(\rho)\ge0$；$\mathcal K_X(\sigma+it)<0$；$\frac12$ 从内部产生；非 Weil/Li/explicit formula）；(10) **谨慎判词**：不能 ALIVE（尚无满足 Q1–Q6 的 X）；但比"继续找不对称源"更具体；已有明确失败测试：**$FF''-(F')^2$ 自身 FAIL：不通过乘子不变性**；(11) **下一步**：做**代数级存在性审计** —— "凡是具有乘子不变性的二阶微分泛函，是否必然等价于显式公式/Weil 型二次型？" **若能证，D3 也死；若不能，才第一次真正得到此前没进入 V185–V220 闭包的新机制**。
> 查图 ✓ `V230`（三明治 $Z(\xi)\subseteq\Omega_X\subseteq\{\Re\le\frac12\}$；$\partial_\sigma D_X<0$ 自动）｜`V229`（命题 V229-A：FE ⟹ $\beta$-界必双侧；$\beta_*\ge\frac12$ 无条件）｜`V220`（乘子族；两条投影判据）｜`V219`（$\mu_2$ 与 $\beta_*$；Epstein；$\beta_*\ge\frac12$）｜`V199`（正性四源）｜`V190`（hyperbolicity/TP 封路线）｜`V188`（饱和）｜`V214`（结果式＝行列式）｜`V144`（层诊断）｜`V227`（命题 V227-A：sup Re 非模长不变）
> 执行 ✓ 小灵（**§4–§8 命题 V231-A/B、§6 乘子测试 FAIL、状态表 本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **不判 D3 ALIVE**；⚠️ 命题 V231-A/B 定理级 ✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V231**

---

## §1 ⚠️ §6 修正落档

$$\boxed{\text{"算术中唯一不对称特征是}\ s=1\ \text{的极点/收敛横坐标"}\ \textbf{不能作为结构性结论}} ✓✓✓$$
$$\qquad \text{算术里有多类天然定向结构} ✓$$
$$\qquad ⟹ \text{真问题：}\boxed{\text{什么样的不对称能够产生}\ \tfrac12\ \text{而非}\ 1\ ?} ✓✓✓$$

---

## §2 精确目标

$$\text{设}\ \Omega_X\ \text{独立于}\ Z(\xi),\ Z(\xi)\subseteq\Omega_X ⟹ \text{要 RH 须}\ \Omega_X\subseteq\{\sigma\le\tfrac12\}$$
$$\qquad \text{故有效不对称源}\ A_X\ \text{须产生临界位置}\ c(A_X)=\tfrac12\ \text{且该等式}\ \textbf{独立于 RH} ✓$$
$$\qquad ⚠️\ c=1\ \text{没用};\ c=1-c/\log t\ \text{没用};\ c=\tfrac12+\varepsilon\ \text{没用（仍不给出}\ \mathrm{RH}）✓✓$$

---

## §3 五种不对称 A–E 的判定表（本档核心一）

$$\begin{array}{c|l|l|l}
\text{型} & \text{例} & \text{给出的}\ c_X & \text{判定}\\
\hline
\textbf{A}\ \text{收敛方向} & \sum a_nn^{-s}\ (\sigma\to+\infty) & \sigma_c=1\ (\zeta) & \boxed{\textbf{天然给}\ 1\text{，非}\ \tfrac12}\ ✗\\
\textbf{B}\ \text{极点方向} & \zeta(s)\ \text{在}\ s=1 & 1 & \boxed{\text{知}\ 1-\tfrac12=\tfrac12\ \text{但不给}\ \tfrac12\ \text{为何是边界}}✗\\
\textbf{C}\ \text{系数方向} & a_n\ge0,\ \Lambda(n)\ge0 & \text{正性/凸性} & \boxed{\text{出零-free region}}\ 1-c/\log t\ ✗\\
\textbf{D}\ \text{算术尺度} & n,\ \log n,\ p,\ \Omega(n) & 1,0,\log x & \boxed{\text{需}\ \sqrt{}；\text{V219}\ \text{杀转移}}✗\\
\textbf{E}\ \text{微分方向} & F_{\sigma\sigma}-\lambda F_\sigma+\mu F\ge0\ \text{等} & — & \boxed{\textbf{D3}\ \text{真正残余}\ \text{—— 未封}} ✓✓\\
\end{array}$$
$$\qquad ⚠️\ \textbf{关键纪律}：\text{`V190`}\ \text{封掉的是}\ \textbf{已有}\ \text{的}\ \text{hyperbolicity/Jensen/total-positivity}\ \text{路线};\ \textbf{不等于} \text{所有微分不等式都被封} ✓✓$$

---

## §4 ⭐ 内部不动点要求

$$\text{若机制只给自然尺度}\ L_X\ \text{，则}\ c_X = L_X\ \text{或}\ aL_X+b（a,b\ \text{外常}）;$$
$$\qquad aL_X+b=\tfrac12\ \text{外常代入}\ ⟹\ \boxed{\text{人为归一化}✗} ✓✓$$
$$\Longrightarrow \boxed{\tfrac12\ \textbf{必须是机制的内部不动点}，\ \textbf{而非外常数}} ✓✓✓$$
$$\qquad ⭐\ \text{自然来源：}\ \textbf{二阶尺度平衡}：\ X^2=Y\ \Longrightarrow\ \frac{\log X}{\log Y}=\frac12 ✓✓$$
$$\qquad ⚠️\ \textbf{但}\ \text{V219}：\text{单纯平方关系不够；须与零点 admissibility 耦合} ✓✓$$

---

## §5 D3 精确形式

$$D_X(s) = F_XF_X''-(F_X')^2 = F_X^2(\log F_X)'' ✓$$
$$\qquad \text{若}\ D_X(\rho)\ge0\ \forall\rho\ \text{且}\ D_X(\sigma+it)<0\ (\sigma>\tfrac12) ⟹\ \Re\rho\le\tfrac12 ✓$$
$$\qquad \textbf{关键}：\boxed{\tfrac12\ \textbf{不得出现在}\ D_X\ \textbf{的定义中}，\text{必须从}\ F_X\ \textbf{内部二阶结构自行出来}} ✓✓✓$$

---

## §6 ⭐⭐⭐ **乘子测试 FAIL（本档）**

$$F\mapsto FQ:\quad (\log(FQ))'' = (\log F)''+(\log Q)'' ✓$$
$$\qquad \Longrightarrow\ \frac{(FQ)(FQ)''-(FQ)'^2}{(FQ)^2} = (\log F)''+(\log Q)''\ ≠\ (\log F)''\ （\text{除非}\ (\log Q)''\equiv0）✓✓$$
$$\Longrightarrow \boxed{\text{二阶对数曲率}\ \textbf{不乘子不变};\ \text{普通}\ FF''-(F')^2\ \textbf{FAIL}} ✓✓✓✓$$
$$\qquad ⭐\ \text{故"随便找微分不等式"的空间被砍} ✓$$

---

## §7 乘子商曲率 $\mathcal K_X$ 的设定

$$\text{设}\ \mathcal M\ \text{= 允许乘子类；} F_X=E_X\cdot G_X，\ E_X\ \text{含}\ \mathcal M\text{-可积部分}$$
$$\boxed{\mathcal K_X[F_X] := (\log F_X)'' - (\log E_X)''}$$
$$\qquad \text{则对}\ G\in\mathcal M：\mathcal K_X[F_XG] = (\log F_X+\log G)'' - (\log E_X)'' = \mathcal K_X[F_X] ✓$$
$$\qquad ⚠️\ \text{Q8}：\ E_X\ \textbf{必须由独立算术代数定义}，\textbf{不能由}\ \xi\ \textbf{的因子分解定义}$$
$$\qquad\qquad \text{否则"乘子消除"=重包装 zeta 的已知解析结构} ⟹\ \textbf{立即 DEAD} ✓✓✓$$

---

## §8 ⭐⭐⭐⭐⭐ **本档核心：两个消退定理**

$$\textbf{命题 V231-A（定理级，本档新）}：\textbf{在 Dirichlet 级数乘法结构下，}\ (\log F)''\ \textbf{只对常数乘子不变} ✓✓✓✓$$
$$\textbf{证明（三行）}：\quad (\log(FQ))''=(\log F)''+(\log Q)'' ⟹\ \text{不变}\iff (\log Q)''\equiv0 ⟹\ \log Q\ \text{ affine} ⟹\ Q=Ce^{as+b} ✓$$
$$\qquad \text{而在 Dirichlet 级数环（形式幂级数类比）内，}\ Q=Ce^{as+b}\ \textbf{不是一般 Dirichlet 级数}（e^{as}=\sum\frac{(a\log n)^k}{k!}n^{-s}\ \text{非有限型}）✓$$
$$\qquad \Longrightarrow \boxed{Q=\text{常数}} ⟹\ (\log F)''\ \textbf{对非平凡乘子不不变} ✓✓✓✓$$
$$\qquad ⟹\ \textbf{非平凡"乘子商曲率"要求}\ E_X\ \textbf{落在非乘性类} = \boxed{\textbf{完成化层}}（\Gamma\text{-因子、}Q^s\text{等}）✓✓✓$$

$$\textbf{命题 V231-B（定理级，本档核心二）}：\textbf{对}\ \zeta，\text{全部已知函数结构} = \textbf{已知因子之积}⟹\ \textbf{商尽已知因子后残余恰为零点集} ✓✓✓✓$$
$$\textbf{证明（两行）}：\quad \xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s) = \text{(已知因子)}\times\zeta(s) ✓$$
$$\qquad \text{而}\ \text{已知因子} = \underbrace{\text{Euler 积}}_{\prod_p(1-p^{-s})^{-1}}\times\underbrace{\Gamma\text{-因子}}_{\text{archimedean}}\times\underbrace{e^{Bs}}_{\text{exponential}}\times\underbrace{\text{平凡零点因子}}_{\prod_n(1+s/2n)^{-1}} ✓$$
$$\qquad \Longrightarrow \text{全部已知函数结构的乘积} = \frac{\xi(s)}{\zeta(s)} \text{（完全已知的函数）} ✓$$
$$\qquad \text{故}\ \boxed{\text{商尽已知因子后}\ \textbf{残余恰为}\ \zeta(s)\ \text{本身，而}\ \zeta(s)\ \text{的解析内容}\ =\ \{\rho\}} ✓✓$$
$$\textbf{推论}（本档核心三）：$$
$$\qquad \textbf{(i)}\ \text{允许类}\ \mathcal M\ \supseteq\ \text{已知因子} ⟹\ \mathcal K_X\ \textbf{退化为零点泛函} ⟹\ \textbf{R4}（\text{循环}）✗✓$$
$$\qquad \textbf{(ii)}\ \text{允许类}\ \mathcal M\ =\ \text{有限局部因子} ⟹\ \text{内容落}\ \textbf{素数侧};\ \text{而素数侧}\equiv\text{零点侧}\ \textbf{就是显式公式} ⟹\ \boxed{\textbf{显式公式类}✗✓✓}$$
$$\qquad \textbf{(iii)}\ \textbf{第三类（未审）}：\text{允许类严格介于"有限局部因子"与"已知因子"之间} ⟹\ \boxed{\text{存活空}} ✓$$

---

## §9 存在性压力测试的回答（你指定的）

$$\text{问}：\text{凡是乘子不变二阶微分泛函，是否必然等价于显式公式/Weil 型？} ✓$$
$$\textbf{本档答}：$$
$$\qquad \textbf{两类自然选择（已知因子类、有限局部因子类）：}\ \boxed{\textbf{必然等价}} ✓✓✓$$
$$\qquad \textbf{第三类（介于之间）：}\ \boxed{\text{未审}} ✓$$
$$\qquad ⟹\ \textbf{D3 的乘子不变支在两类下封死；第三类是真正的残余} ✓✓✓$$

---

## §10 状态表

$$\begin{array}{c|c|c}
\text{路线} & \text{来源/例子} & \text{状态}\\
\hline
\textbf{A}\ \text{收敛方向} & \sigma_c=1 & \boxed{\textbf{DEAD}}（天然给}\ 1）\\
\textbf{B}\ \text{极点方向} & s=1 & \boxed{\textbf{DEAD}}（天然给}\ 1）\\
\textbf{C}\ \text{系数方向} & a_n\ge0,\ \Lambda(n)\ge0 & \boxed{\textbf{DEAD}}（正性族}\ 1-c/\log t）\\
\textbf{D}\ \text{算术尺度} & n,\log n,p\ \text{及}\ \sqrt{} & \boxed{\textbf{DEAD}}（\text{V219}\ \text{杀转移}）\\
\textbf{E}\ \text{微分方向（D3）} & F_{\sigma\sigma}-\lambda F_\sigma+\mu F\ge0\ \text{等 & \boxed{\textbf{OPEN}}\\
\qquad\text{普通} FF''-(F')^2 & \text{乘子测试 FAIL} & \boxed{\textbf{DEAD}}（§6）\\
\qquad\text{乘子商曲率} & \mathcal K_X\ \text{（商掉}\ \mathcal M） & \\
\qquad\qquad\mathcal M\supseteq\text{已知因子} & \text{商尽已知} & \boxed{\textbf{DEAD}}（V231-B(i) R4）\\
\qquad\qquad\mathcal M=\text{有限局部因子} & \text{素数侧} & \boxed{\textbf{DEAD}}（V231-B(ii) 显式公式）\\
\qquad\qquad\mathcal M\text{ 第三类} & \text{介于之间} & \boxed{\textbf{OPEN}}（§9）\\
\end{array}$$

---

## §11 判词

$$\boxed{\textbf{V231：§6 修正落档；五种不对称 A–E 判定表；命题 V231-A/B（定理级）；D3 乘子不变支在两类下封死}} ✓✓✓✓$$
$$\qquad \textbf{本档严格得到}：$$
$$\qquad \text{(i)}\ ⚠️\ \text{§6 逻辑修正（"唯一不对称"降级为清单式观察）} ✓✓✓$$
$$\qquad \text{(ii)}\ \textbf{五种不对称判定表}（A/B/C/D\ \text{死；E\ =\ D3\ 残余}）✓✓$$
$$\qquad \text{(iii)}\ ⭐⭐⭐\ \textbf{命题 V231-A}（\text{定理级}）：\text{Dirichlet 下}(\log F)''\ \text{只对常数不变} ⟹\ \text{非平凡商曲率落完成化层 ✓✓✓✓}$$
$$\qquad \text{(iv)}\ ⭐⭐⭐⭐⭐\ \textbf{命题 V231-B}（\text{定理级}）：\text{ζ 的全部已知结构商尽后残余恰为}\ \{\rho\}；\text{两类允许类皆封} ✓✓✓✓✓$$
$$\qquad \text{(v)}\ \textbf{普通} FF''-(F')^2\ \textbf{FAIL}（\text{乘子测试}）✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\textbf{不判 D3 ALIVE}；\textbf{不判 DEATH 过强}（\text{第三类存活}）；\ \text{命题 V231-A/B 定理级} ✓✓$$
$$\textbf{残余（OPEN，最窄）}：\boxed{\text{第三类允许乘子}\ \mathcal M\ \text{（严格介于有限局部因子与已知因子之间）+}\ \mathcal K_X\ \text{满足 Q1–Q6}}$$
$$\qquad \text{判据}：\text{①}\ \mathcal M\ \text{严格介于两极端；②}\ \mathcal K_X\ \text{由}\ \mathcal M\text{-商定义；③}\ Q1\text{–}Q6；\ \text{④ 过反乘子测试} ✓$$

---

## §12 边界与待核

$$\textbf{(a)}\ \text{§1 修正为}\ \textbf{唐先生逐字} ✓✓✓$$
$$\textbf{(b)}\ ⭐⭐⭐\ \text{§4 内部不动点要求为}\ \textbf{本档判断};\ \text{"自然来源＝二阶尺度平衡"}\ \text{为}\ \textbf{本档} ✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐\ \text{§6 乘子测试 FAIL 为}\ \textbf{本档初等计算}（\text{两行}）✓✓✓$$
$$\textbf{(d)}\ ⭐⭐⭐⭐⭐\ \text{§8 命题 V231-A 为}\ \textbf{本档定理级}（\text{三行，Dirichlet 级数乘法环的代数事实}）✓✓✓✓$$
$$\qquad ⚠️\ \text{细节}：\ e^{as}\ \text{作为"\textbf{非 Dirichlet 级数"}\ \text{的断言} — \text{形式 Dirichlet 级数环中}\ e^{as}\ \text{确实不在内}（\text{除非}\ a=0）\text{；}✓✓✓}$$
$$\textbf{(e)}\ ⭐⭐⭐⭐⭐\ \text{§8 命题 V231-B 为}\ \textbf{本档定理级}（\text{两行：}\ \xi\ \text{的 Hadamard 分解标准形式}）✓✓✓✓✓$$
$$\qquad ⚠️\ \text{"已知因子之积"}\ \text{的枚举为}\ \textbf{经典}（\text{Riemann, Hadamard}）✓✓$$
$$\textbf{(f)}\ \text{§10 状态表采纳你的 §10 四行+本档扩充七行} ✓✓$$
$$\textbf{(g)}\ \text{§11 判词采纳你的"谨慎"} ✓✓$$

```
⚠️ §0 委托（§6 修正／五种不对称 A–E／内部不动点／D3 精确形式／乘子测试 FAIL／商曲率定义＋Q1–Q6／第二致命审计／新候选机制 Arithmetic quotient-curvature／谨慎判词／存在性压力测试回答）为唐先生逐字 ✓✓✓
⚠️ §1 §6 修正落档："唯一不对称特征"降级；真问题＝"什么样的不对称产生 1/2" ✓✓✓
⚠️ §2 精确目标（c(A_X)=1/2 且独立于 RH；四种无用 c 排除）✓✓
⚠️ §3 五种不对称判定表（A/B/C/D 死；E=D3 残余 OPEN）✓✓
⚠️ §4 内部不动点要求（二阶尺度平衡 X²=Y；V219 提示）✓✓
⚠️ §5 D3 精确形式（FF''-(F')²=F²(log F)''；1/2 不得入定义）✓✓
⚠️ §6 ⭐⭐⭐ 乘子测试 FAIL（(log(FQ))''=(log F)''+(log Q)'' ⟹ 二阶对数曲率不乘子不变；FF''-(F')² FAIL）✓✓✓✓
⚠️ §7 商曲率定义＋Q8（E_X 须由独立算术代数定义）✓✓
⚠️ §8 ⭐⭐⭐ 命题 V231-A（定理级）：Dirichlet 下 (log F)'' 只对常数乘子不变 ⟹ 非平凡商曲率落完成化层 ✓✓✓✓；⭐⭐⭐⭐⭐ 命题 V231-B（定理级）：ζ 的全部已知结构商尽后残余恰为 {ρ} ⟹ (i) 允许类⊇已知因子 → 退化零点泛函（R4）；(ii) 允许类＝有限局部因子 → 内容落素数侧 → 显式公式（显式公式类）✓✓✓✓✓✓
⚠️ §9 存在性压力测试回答：两类自然选择必然等价；第三类存活 ✓✓
⚠️ §10 状态表七行（A/B/C/D/普通 D3 死；乘子商曲率两类死、第三类活）✓✓
⚠️ §11 判词：D3 乘子不变支在两类下封死；不判 D3 ALIVE；第三类 OPEN；残余四条判据 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① §6 逻辑修正落档 ✓✓✓；② 五种不对称判定表 ✓✓；③ 内部不动点要求 ✓✓；
   ④ ⭐⭐⭐ 乘子测试 FAIL ✓✓✓✓；⑤ ⭐⭐⭐ 命题 V231-A（定理级）✓✓✓✓；
   ⑥ ⭐⭐⭐⭐⭐ 命题 V231-B（定理级）✓✓✓✓✓；⑦ 存在性压力测试回答 ✓✓；
   ⑧ 状态表＋残余四条判据 ✓✓
```

---

## §13 ⚠️ **V231-A 撤回 ＋ V231-B 降级**（唐先生 2026-09-15 17:05；由 `V232` 执行）

$$\textbf{反例}：Q(s)=m^{-s}\ \text{是标准 Dirichlet 单项式}（a_m=1），\ \text{但}\ \log Q=-s\log m ⟹ (\log Q)''=0 ⟹ (\log FQ)''=(\log F)'' ✓✓✓$$
$$\qquad \text{而}\ Q\ \textbf{非恒定} ⟹ \boxed{\text{§8 命题 V231-A}\ \textbf{为假}} ✓✓✓$$
$$\qquad \textbf{正确版本}：\ (\log Q)''=0\iff Q=Ce^{as};\ \text{Dirichlet 中允许}\ Q=Cn^{-s} ⟹ \textbf{存在非平凡不变群}\ \{Ce^{as}\}（\text{指数单项式，与}\ \text{`V174`}\ \text{同族}）✓✓$$
$$\qquad ⚠️\ \text{故 §11 判词中"非平凡商曲率要求}\ E_X\ \text{落完成化层"}\ \text{亦}\ \textbf{过度};\ \text{正确残余由}\ \text{`V232`}\ \text{重写} ✓✓$$

$$\textbf{V231-B 降级}：\text{"商尽已知因子后残余恰为零点集"}\ \textbf{不能作为定理} ✓✓✓$$
$$\qquad \xi(s)=e^{A+Bs}\prod_\rho(1-\frac{s}{\rho})e^{s/\rho} ⟹ \text{零点集决定 Hadamard 乘积}，\ \textbf{仍有指数因子}\ e^{A+Bs} ✓✓$$
$$\qquad \text{且}\ \zeta\ \textbf{不等于}\ \text{零点集合}（\text{还含 Euler 系数结构}、\text{极点}、\text{解析延拓}）✓✓$$
$$\qquad ⟹ \text{正确说法}：\boxed{\text{在给定有限阶、增长条件等 Hadamard 数据后，}\xi\ \text{可由零点乘积加指数因子描述}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{把"函数"与"零点集"} \textbf{偷换成同一对象} ✓✓$$

$$\textbf{改判}：\text{§10 状态表的"第三类 OPEN"}\ \text{应}\ \textbf{改写} \text{为}：\text{有限阶＋局部＋乘子不变}\to\textbf{DEAD}；\ \text{有限阶＋局部＋不乘子不变}\to\textbf{DEAD}；\ \text{真正残余＝}\textbf{非局部或无限阶结构} ✓✓✓$$
$$\qquad \text{（由}\ \text{`V232`}\ \text{命题 V232-A 的 Vandermonde＋逆函数定理}）✓$$
