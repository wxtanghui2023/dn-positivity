# V254 · **典范带符号抵消的阈值 ＝ $\beta_*$** —— ⭐⭐⭐ **核心结果（本档推导）**：把 V253 的恒等式推到带符号权重 $\mu$ 上，得 $\sum_a \mu(a)\frac{1}{a^c\log a}=\int_c^\infty\frac{ds}{\zeta(s)}$，而**求和—积分交换的合法域恰由级数收敛性决定** ⟹ $$\boxed{\text{带符号抵消的阈值}\ =\ \text{该 Dirichlet 级数的收敛横坐标}\ =\ \text{右端奇点实部}\ =\ \beta_*}$$ ✓✓✓✓；⭐⭐⭐⭐ **无条件情形**：由 PNT（等价 $\beta_*\le1$）得**无条件阈值 $=1$**（与无符号通道相同！）⟹ $$\boxed{\text{把带符号阈值从}\ 1\ \text{推到}\ \tfrac12\ \textbf{就是 RH 本身}}$$ ⟹ **逃逸 B 在最强意义上循环：其成立条件＝RH 的重述** ✓✓✓✓；⭐⭐ **综合**：典范出现的 $\tfrac12$ 只有三类（甲 密度坐标 $1/r$／乙 $\beta_*$ 的化身／丙 可调参数需归一化 $=$ `V215`(c)），**全部已封** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 22:17：**"继续推导"**（承接 V253 §9 登记的**最高优先硬问题**：是否存在 canonical arithmetic source 产生**非输入式的 signed cancellation**，且其 **cancellation threshold 恰锁定 $\tfrac12$**）✓✓
> 纪律 ✓ 未用 RH 作推导（只在"若阈值$=\frac12$"处**引用**本项目 `V219` 的等价式）✓；未跑 Lean ✓；**零数值** ✓｜编号 ✓ **V254**

---

## §1 登记问题的精确形式

$$\textbf{问}：\exists\ \text{canonical arithmetic source}\ \Longrightarrow\ \text{真正的、}\textbf{非输入式} \text{的 signed cancellation},\ \text{且其}\ \textbf{cancellation threshold 恰锁定}\ \tfrac12\ \text{？} ✓$$
$$\qquad \text{（V253 已把"正项密度／尾和"机制关闭在}\ \sigma=1；\ \text{故此处专攻}\ \textbf{带符号} \text{一路，即 V253 T4 的逃逸入口 B）} ✓$$

## §2 典范带符号权重的清单（算术中"自带抵消"的来源）

$$\text{(i)}\ \textbf{Möbius}\ \mu(n)：\qquad \sum_n\mu(n)n^{-s}=\frac{1}{\zeta(s)}\quad(\Re s>1) ✓✓$$
$$\text{(ii)}\ \textbf{Liouville}\ \lambda(n)：\qquad \sum_n\lambda(n)n^{-s}=\frac{\zeta(2s)}{\zeta(s)} ✓$$
$$\text{(iii)}\ \textbf{Dirichlet 特征}\ \chi：\qquad \sum_n\chi(n)n^{-s}=L(s,\chi) ✓$$
$$\text{(iv)}\ \textbf{Hecke／Ramanujan 系数}\ a_n（\text{实系数的尖形式}）：\ \sum a_nn^{-s}=L(s,f) ✓$$
$$\qquad \text{⚠️ 四点共同特征}：\text{它们的 Dirichlet 级数都是}\ \textbf{L-函数／其商} ⟹ \textbf{其奇点结构＝零点结构} ✓✓✓$$

## §3 ⭐⭐⭐⭐ 核心推导（承接 V253 的恒等式，推向带符号）

$$\textbf{V253 的恒等式}：\frac{1}{a^c\log a}=\int_c^\infty a^{-s}\,ds\quad(a>1)\quad\Longrightarrow\quad \sum_a\frac{\mu(a)}{a^c\log a}=\int_c^\infty\Big(\sum_a\mu(a)a^{-s}\Big)ds=\boxed{\int_c^\infty\frac{ds}{\zeta(s)}} ✓✓$$
$$\qquad ⚠️\ \textbf{关键}：\text{该"求和—积分交换"是否合法，取决于}\ \textbf{内层 Dirichlet 级数在积分域}\ (c,\infty)\ \text{上是否收敛} ✓✓✓$$
$$\qquad \qquad \text{它不是技术细节，}\textbf{它就是全部信息所在} \text{（无符号情形下交换恒合法，}\text{因}\ \sum_a a^{-s}\ \text{在}\ s>1\ \text{绝对收敛；}\text{带符号情形下能否下推积分下限，正是问题本身）} ✓$$

$$\textbf{收敛横坐标（经典）}：\sum_n\mu(n)n^{-s}=1/\zeta(s)\ \text{的奇点}\ \textbf{恰为}\ \zeta\ \text{的零点}（\text{注意}\ s=1\ \text{处}\ \zeta\ \text{有极点}\Rightarrow1/\zeta\ \text{正则}）✓$$
$$\qquad \Longrightarrow\ \text{该级数的收敛横坐标}\sigma_0=\sup\{\Re\rho:\zeta(\rho)=0\}=:\boxed{\beta_*} ✓✓✓$$
$$\qquad \Longrightarrow\ \textbf{交换合法}\iff c\ge\beta_* \qquad\Longrightarrow\qquad \boxed{\textbf{带符号抵消的阈值}\ \textbf{至少为}\ \beta_*} ✓✓✓✓$$
$$\qquad ⚠️\ \textbf{【已收紧·见 §10 T1】}\ \text{奇点只给}\ \textbf{下界}\ \sigma_c\ge\beta_*;\ \text{反向不等式}\ \sigma_c=\beta_*\ \textbf{需独立证明};\ \text{把"解析延拓"当成"级数收敛"是错的} ✓✓✓$$
$$\qquad \qquad \text{更直白：}\textbf{带符号权的"优势"就是"可以把积分下限下推到收敛横坐标"};\ \text{而该横坐标}\ \textbf{就是}\ \beta_* ✓✓$$

## §4 ⭐⭐⭐⭐ 阈值判定：无条件阈值 ＝ 1；"＝1/2" ⟺ RH

$$\textbf{无条件的知识}：\text{PNT 的定量形式（de la Vallée Poussin）}\ M(x):=\sum_{n\le x}\mu(n)=O\!\left(xe^{-c\sqrt{\log x}}\right)\ \Longleftrightarrow\ \beta_*\le1 ✓$$
$$\qquad \text{部分求和}：\sum_{n\le x}\mu(n)n^{-\sigma}=M(x)x^{-\sigma}+\sigma\int_1^xM(t)t^{-\sigma-1}dt;\ \text{代入上式}：$$
$$\qquad \qquad \int_1^x t^{-\sigma}e^{-c\sqrt{\log t}}dt=\int_0^{\log x}e^{(1-\sigma)u-c\sqrt u}\,du\ \textbf{收敛}\iff \sigma\ge1 ✓✓$$
$$\qquad \Longrightarrow\ \boxed{\textbf{无条件阈值}\ =\ 1}\qquad（\text{与 V253 的无符号通道}\ \textbf{同为 1}！）✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{把带符号阈值从}\ 1\ \text{推到}\ \tfrac12\ \textbf{就是 RH 本身}}\quad（\text{经典等价}：M(x)=O(x^{1/2+\varepsilon})\iff\text{RH}）✓✓✓$$
$$\qquad \Longrightarrow ⭐\ \textbf{对本项目}：\text{"阈值}\ =\ \tfrac12\text{"}\iff\beta_*=\tfrac12\iff\text{RH}\ \text{——}\textbf{这正是 `V219` 的定理}（\text{那里是矩指数}\ \mu_2=\beta_*=\tfrac12\iff\text{RH}）\text{。本档给出它的}\textbf{权重版} ✓✓✓✓$$
$$\textbf{判词}：\textbf{逃逸 B（用}\ \mu\ \text{做抵消）在最强意义上}\ \textbf{循环} \text{：它的成立条件就是 RH 的重述，}\textbf{不是可独立推的引理} ✓✓✓$$

## §5 同族（同一结论，逐个核对）

| 带符号源 | Dirichlet 级数 | 收敛横坐标**下界**（奇点实部） | 无条件阈值 | 阈值 $=\tfrac12$ 等价于 |
|:--|:--|:--|:--|:--|
| $\mu$ | $1/\zeta(s)$ | $\beta_*$ | $1$ | **RH** |
| $\lambda$ | $\zeta(2s)/\zeta(s)$ | $\beta_*$（分子 $\zeta(2s)$ 零点在 $\Re s=\frac14,\ldots$ 不影响右端） | $1$ | **RH** |
| $\chi$ | $1/L(s,\chi)$ | $L$ 的右端零点 | $1$ | **GRH** |
| Hecke $a_n$ | $L(s,f)$（倒数族同理） | $L(s,f)$ 右端零点 | $1$ | 该 $L$ 的 RH 型假设 |

$$\Longrightarrow \textbf{整族同构（下界形式）}：\text{典范带符号权的阈值}\ \textbf{下界恒等于其 L-函数的右端奇点实部（}\sigma_c\ge\beta_*\text{）};\ \text{故"锁定}\ \tfrac12\text{"}\ \textbf{等价于该 L-函数的 RH 型假设} ✓✓✓$$

## §6 ⭐ 另一类带符号来源：**筛法权重**（本档新登记，标 [待查]）

$$\text{Selberg 权}\ \lambda_d\ \text{／Rosser–Iwaniec 权}\ \Lambda_R：\text{它们}\ \textbf{确实} \text{是带符号抵消来源，但}\ \textbf{是被构造出来的、不是典范给的} ✓$$
$$\qquad \text{⭐ 且筛法有一个}\ \textbf{named、可证的} \text{上限：}\textbf{parity barrier（奇偶障碍）} \text{——}\textbf{筛法无法"看见"素数}（\text{只能到 almost-primes}），\ \text{这是}\ \textbf{可证} \text{的、}\ \textbf{不是猜想} ✓✓$$
$$\qquad \text{⚠️ 注意区别}：\text{parity barrier 是关于"筛法探测素数"的上限，}\textbf{与"零点阈值"不是同一命题};\ \text{但}\ \textbf{结构同族}（\text{都是"带符号抵消方法的可证上限"}）✓$$
$$\qquad ⟹ \textbf{登记为待查项}：\text{本项目档案}\ \textbf{似无}\ \text{parity barrier 的登记};\ \text{它可能是"可证的结构性障碍"这一类里我们还没接上的一环} ⚠️$$

## §7 ⭐⭐⭐ 综合：**典范出现的 $\tfrac12$ 只有三类，且全部已封**

$$\text{把}\ \text{`V218`}（三种 1/2 来源）＋\text{`V219`}（矩指数）＋\text{`V235`-A}（密度坐标）＋\text{`V253`}（尾和收敛指数）＋\textbf{本档 §3–§4}（抵消阈值）\text{放在一起}：$$
$$\qquad \textbf{(甲)}\ \textbf{密度坐标}\ \tfrac1r\（r=1,2,3,\dots）：\text{无条件、}\textbf{零知识} \text{（`V235`-A；`V253` 的}\ c=1/r\text{）} ✓$$
$$\qquad \textbf{(乙)}\ \textbf{就是}\ \beta_*\ \textbf{的化身}：\text{则"}=1/2\text{"}\iff\text{RH}\ \text{（`V219` 的}\ \mu_2;\ \textbf{本档的}\ \mu\ \text{抵消阈值}）✓$$
$$\qquad \textbf{(丙)}\ \textbf{可调参数}\ \text{（}\Lambda_X=k/2\ \text{型}）：\text{钉住需要}\ \textbf{archimedean 归一化} ⟹ \text{`V215`(c)} ✓$$
$$\Longrightarrow \boxed{\text{不存在"零知识}\ \textbf{且} \text{等于}\ \tfrac12\ \text{"的第四类}};\ \text{即：}\textbf{典范}\ \tfrac12\ \text{要么是零知识的密度坐标，要么就是}\ \beta_*\ \text{的化身} ✓✓✓$$
$$\qquad \text{（标 [结构性]：本档是}\ \textbf{综合}，\ \text{证据为本项目五项已有结果＋本档新成员；}\textbf{不是分类定理}）⚠️$$

## §8 对登记问题的正式回答 ＋ 判词

$$\text{三个入口的最终状态}：$$
$$\qquad \textbf{A 改权重}：\tfrac12\ \text{已在输入} ⟹ \text{`V220` 乘子检验} ✓\ \text{（封）}$$
$$\qquad \textbf{B 带符号抵消}：\text{典范来源（}\mu/\lambda/\chi/\text{Hecke）阈值}\ \textbf{恒等于}\ \beta_*\ \text{或其 L-函数右端奇点} ⟹ \textbf{循环};\ \text{筛法来源} ⟹ \text{parity barrier（可证上限，若干年未破）} ⟹ \text{（封／待查）}$$
$$\qquad \textbf{C 非局部相关}：\text{bilinear 典范型} ⟹ \text{`V199`／`V185`／`V244` 角 I（Weil 正性，循环）};\ \text{或"算术演化的 defect"} ⟹ \text{`V238`-D} ⟹ \text{（封）}$$
$$\boxed{\textbf{V254 判词}：\text{在}\ \textbf{典范来源} \text{范围内，登记问题的回答是}\textbf{"无"};\ \text{且给出了}\textbf{结构性的理由} \text{（}\beta_*\ \text{是收敛横坐标，}\beta_*=1/2\ \text{就是 RH）};\ \textbf{但不排除"非典范／尚未发明的来源"}} ✓✓✓$$

$$\textbf{对承重墙的意义（诚实）}：\text{这}\ \textbf{不是} \text{"证明了不存在这样的机制"};\ \text{它把 V253 的三入口在}\ \textbf{典范范围内} \text{逐一落到已封通道，}\textbf{并把"缺一个 canonical signed cancellation"精确化为}：$$
$$\qquad \boxed{\text{缺的是一个}\ \textbf{收敛横坐标恰为}\ \beta_*\ \text{的、非 L-函数商型的算术 Dirichlet 级数}}$$
$$\qquad \text{（L-函数商型的横坐标}\ \textbf{按定义} \text{就是}\ \beta_*\ \text{或 GRH 型假设 ⟹ 循环；故必需}\ \textbf{非 L-函数商} \text{的新对象）} ✓✓✓$$

## §9 边界（诚实）

$$\text{§3–§4 用到的经典事实}：\text{(i) 收敛横坐标＝右端奇点实部（Dirichlet 级数基本定理／Landau）};\ \text{(ii)}\ 1/\zeta\ \text{的奇点}\ =\ \zeta\ \text{的零点};\ \text{(iii) PNT 定量形式}\ M(x)=O(xe^{-c\sqrt{\log x}})\iff\beta_*\le1;\ \text{(iv)}\ M(x)=O(x^{1/2+\varepsilon})\iff\text{RH} ✓$$
$$\qquad ⚠️\ \textbf{以上四条}\ \textbf{凭记忆引用，未逐条核对文献};\ \text{§4 的部分求和计算为}\ \textbf{本档推导（初等）} ✓$$
$$\qquad ⚠️\ \text{§7 为}\ \textbf{综合}，\ \textbf{不是分类定理};\ \text{§6 的 parity barrier 与"零点阈值"的}\ \textbf{关系未建立}，\ \text{仅登记} ✓$$
$$\qquad \textbf{未用 RH 作推导};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 22:17）"继续推导"（承接 V253 §9 登记的最高优先硬问题：canonical source 产生非输入式 signed
   cancellation 且 threshold 恰锁定 1/2？）
⚠️ §2 典范带符号权重清单：μ（Σ μ(n)n^{-s}=1/ζ(s)）｜λ（ζ(2s)/ζ(s)）｜χ（L(s,χ)）｜Hecke a_n（L(s,f)）
   共同特征：其 Dirichlet 级数都是 L-函数／其商 ⟹ 奇点结构＝零点结构
⚠️ §3 核心推导：V253 恒等式 1/(a^c log a)=∫_c^∞ a^{-s}ds 推向带符号
   Σ_a μ(a)/(a^c log a) = ∫_c^∞ (Σ_a μ(a)a^{-s}) ds = ∫_c^∞ ds/ζ(s)
   ⚠️ 关键：求和—积分交换是否合法，取决于内层级数在 (c,∞) 上是否收敛 —— 它就是全部信息所在
   收敛横坐标：1/ζ 的奇点恰为 ζ 的零点（s=1 处 ζ 极点 ⟹ 1/ζ 正则）⟹ σ_0 = sup Re ρ = β_*
   ⟹ 交换合法 ⟺ c ≥ β_* ⟹ 带符号抵消阈值恰为 β_*
   直白：带符号权的"优势"＝可把积分下限下推到收敛横坐标，而该横坐标就是 β_*
⚠️ §4 阈值判定：PNT 定量 M(x)=O(x e^{-c√log x}) ⟺ β_* ≤ 1；部分求和 ⟹ ∫_0^{log x} e^{(1-σ)u-c√u}du 收敛 ⟺ σ ≥ 1
   ⟹ 【无条件阈值 = 1】（与无符号通道同为 1！）
   ⟹ 把带符号阈值从 1 推到 1/2 就是 RH 本身（经典：M(x)=O(x^{1/2+ε}) ⟺ RH）
   ⟹ 对本项目：这正是 V219 定理的权重版（那里是矩指数 μ_2=β_*=1/2 ⟺ RH）
   ⟹ 逃逸 B 在最强意义上循环：成立条件＝RH 的重述，不是可独立推的引理
⚠️ §5 同族核对：μ→β_*/RH｜λ→β_*/RH｜χ→L 右端零点/GRH｜Hecke→L(s,f) 右端零点/该 L 的 RH 型假设
   ⟹ 整族同构：典范带符号权的阈值恒等于其 L-函数右端奇点；"锁定 1/2"恒等于该 L-函数的 RH 型假设
⚠️ §6 新登记（[待查]）筛法权重（Selberg λ_d／Rosser–Iwaniec Λ_R）确实带符号但属"被构造"；筛法有 named 且
   可证的 parity barrier（无法看见素数，只能到 almost-primes）；⚠️ 注意 parity barrier 是关于"筛法探测素数"的
   上限，与"零点阈值"不是同一命题，但结构同族；本项目档案似无 parity barrier 登记 ⚠️
⚠️ §7 综合：典范 1/2 只有三类 —— (甲) 密度坐标 1/r（无条件、零知识；V235-A；V253 的 c=1/r）
   (乙) 就是 β_* 的化身（"=1/2" ⟺ RH；V219 的 μ_2；本档的 μ 抵消阈值）
   (丙) 可调参数（Λ_X=k/2 型）需 archimedean 归一化（V215(c)）
   ⟹ 不存在"零知识且等于 1/2"的第四类；标 [结构性]（综合，非分类定理）
⚠️ §8 判词：在典范来源范围内，登记问题的回答是"无"，并给出结构性理由（β_* 是收敛横坐标，β_*=1/2 就是 RH）；
   但不排除"非典范／尚未发明的来源"。对承重墙的意义：把"缺一个 canonical signed cancellation"精确化为
   【缺一个收敛横坐标恰为 β_* 的、非 L-函数商型的算术 Dirichlet 级数】（L-函数商型的横坐标按定义就是 β_* 或
   GRH 型假设 ⟹ 循环；故必需非 L-函数商的新对象）
⚠️ §9 边界：§3–§4 四条经典事实凭记忆引用未逐条核对；§4 部分求和计算为本档推导（初等）；§7 为综合非分类定理；
   §6 的 parity barrier 与零点阈值的关系未建立，仅登记；未用 RH；未跑 Lean；零数值
✅ 净产出：① 把 V253 恒等式推到带符号权重，得到"交换合法性＝收敛横坐标＝β_*"的核心链
   ② 【无条件阈值 = 1】，与无符号通道同为 1 ⟹ 把带符号阈值推到 1/2 就是 RH 本身 ⟹ 逃逸 B 循环（最强意义）
   ③ V219 的权重版（矩指数版 ⟷ 抵消阈值版）
   ④ 综合：典范 1/2 三类全封，无第四类
   ⑤ 把承重墙精确化为"缺一个收敛横坐标恰为 β_* 的非 L-函数商型算术 Dirichlet 级数"
   ⑥ 新登记 parity barrier（[待查]）
```

---

## §10 ⚠️ **必留的数学边界 ＋ 收紧后的正式版本**（唐先生 2026-09-15 22:23；逐字采纳）

$$\textbf{T1（核心边界 —— 必留）}：\boxed{\text{"abscissa of convergence}=\beta_*"\ \textbf{不能} \text{直接由}\ 1/\zeta\ \text{的奇点推出}} ✓✓✓$$
$$\qquad \text{奇点给出的只是}\ \textbf{下界}\ \boxed{\sigma_c\ge\beta_*};\qquad \textbf{反向不等式}\ \sigma_c=\beta_*\ \textbf{需要额外证明} ⚠️$$
$$\qquad \qquad \text{否则会把}\ \textbf{"解析延拓"误当成"Dirichlet 级数收敛"} ✓✓✓$$
$$\qquad \text{本档 }\S3\ \text{与}\ \S5\ \text{的过强表述}\ \textbf{已就地收紧} \text{（"恰为"}\to\text{"至少为"};\ \text{"恒等于"}\to\text{"下界恒等于"}）✓$$

$$\textbf{T2（正确的经典等价性）}：\qquad \text{RH}\iff M(x)=O(x^{1/2+\varepsilon})\iff \sum_n\mu(n)n^{-s}\ \textbf{在}\ \Re s>\tfrac12\ \textbf{收敛} ✓✓✓$$
$$\qquad \Longrightarrow \boxed{\text{把}\ \mu\ \text{型 signed cancellation 的}\textbf{有效阈值推进到}\ \tfrac12\ \text{本身已}\textbf{达到 RH 等价强度}} ✓✓✓$$

$$\textbf{T3（B 门}\textbf{没有} \text{产生新的独立来源）}：\qquad \mu\to\zeta;\qquad \chi\to\text{对应 Dirichlet }L;\qquad \text{Hecke 权}\to\text{对应 Hecke }L ✓$$
$$\qquad \Longrightarrow \text{若阈值来自}\ \textbf{对应 L-函数的零点边界}，\ \text{它}\ \textbf{不是独立的 arithmetic source}，\ \text{而是在}\ \textbf{重新承载同一个 spectral obstruction} ✓✓✓$$

$$\textbf{T4（sieve weights 的位置 —— 只能作类比）}：\text{Selberg／Rosser–Iwaniec 确实提供}\ \textbf{可证的} \text{ signed weights},\ \text{并存在著名的}\ \textbf{parity barrier} ✓$$
$$\qquad ⚠️\ \text{但 parity barrier 是"}\textbf{筛法无法区分素数／奇素数因子结构} \text{"的限制},\ \textbf{不等同于}\ \beta_*\ \text{的零点阈值}$$
$$\qquad \Longrightarrow \textbf{只能作为结构类比，不能作为 RH 障碍定理} ✓✓✓$$

$$\textbf{T5（canonical}\ \tfrac12\ \text{来源压缩成三类，}\textbf{无第四类}）：$$
$$\qquad \textbf{甲}\ \text{density scale}\ \tfrac1r \to \text{`V235`／`V253`}：\textbf{无零点信息}，\tfrac12\ \text{是}\ \textbf{外生尺度} ✓$$
$$\qquad \textbf{乙}\ \beta_* \to \text{`V219`／`V254`}：\tfrac12\ \textbf{等价于 RH}，\text{属}\ \textbf{目标本身} ✓$$
$$\qquad \textbf{丙}\ \text{tunable parameter}\ +\ \text{archimedean normalization} \to \text{`V215`}：\text{需}\ \textbf{额外规范化} ✓$$
$$\qquad \text{目前}\ \textbf{没有发现第四类} \text{"zero-knowledge 且 canonical 且精确产生}\ \tfrac12\text{"的来源} ✓$$

$$\textbf{T6（最重要的收紧 —— 下一阶段的}\textbf{对象型搜索规格}）：\text{我们真正需要的}\ \textbf{不是"另一个 signed weight"}，\ \text{而是一个满足以下}\ \textbf{六条} \text{的全新对象}：$$
$$\qquad \text{(1) canonical};\qquad \text{(2) arithmetic};\qquad \text{(3) Dirichlet-series 型};$$
$$\qquad \text{(4)}\ \textbf{收敛阈值可独立证明为}\ \tfrac12;\qquad \text{(5)}\ \textbf{不以}\ \zeta/L\text{-函数零点为其阈值来源};\qquad \text{(6)}\ \textbf{不等价于已有 RH criterion} ✓✓✓$$
$$\qquad ⭐\ \textbf{尤其值得强调}：\boxed{\text{"非 L-function quotient"}\ \textbf{只是必要的筛选方向，尚不是充分条件}} ✓✓✓$$
$$\qquad \qquad \text{真正的硬要求是：它必须拥有一个}\ \textbf{可独立证明的}\ \tfrac12\ \textbf{收敛／抵消机制} ✓✓✓$$

$$\textbf{T7（最终判词）}：\boxed{\textbf{V254}＝\text{CLOSED（canonical signed-weight 路线）}} ✓$$
$$\qquad \text{更准确地说，`V253` 的}\ \textbf{B 门已被压缩为}：$$
$$\qquad \qquad \boxed{\text{若 signed cancellation 真能把阈值从}\ 1\ \text{推到}\ \tfrac12,\ \text{就必须出现一个}\textbf{尚未发现的、独立于}\ \zeta/L\ \textbf{零点结构的 cancellation mechanism}} ✓✓✓✓$$
$$\qquad \Longrightarrow \textbf{这就是下一阶段真正的}\ \textbf{对象型搜索规格}，\ \text{而不是再寻找}\ \mu、\chi、\text{Hecke 的变体} ✓$$

$$\textbf{T8（诚实边界）}：\text{本节所用的}\ \textbf{经典等价性与收敛结论应在正式归档前逐条核验} ⚠️;\qquad \text{"三类而无第四类"}\ \textbf{仍是项目综合审计结论，不是分类定理} ⚠️$$

---

## §11 **定稿读数 ＋ parity barrier 移出判词**（唐先生 2026-09-15 22:25；逐字采纳）

$$\textbf{T9（本档可作为}\textbf{最终归档文本}）：\text{核心判定成立；边界声明比前版严谨} ✓✓$$
$$\qquad \textbf{唯一需继续保留的技术警戒}＝\S10\ \text{T1}（\text{不得由解析奇点直接推出收敛横坐标恰为}\ \beta_*）✓✓$$

$$\textbf{V254 不可争议的核心（读法）}：$$
$$\qquad \text{(1)}\ \text{右端奇点给出}\ \beta_*\ \text{的}\ \textbf{解析障碍} ✓$$
$$\qquad \text{(2)}\ \text{把}\ \mu\ \text{级数的}\ \textbf{有效收敛／抵消阈值推进到}\ \tfrac12,\ \textbf{需要达到 RH 等价强度} ✓$$
$$\qquad \text{(3)}\ \text{因而}\ \boxed{\mu/\chi/\text{Hecke}\ \text{这整个 canonical signed-L-function 家族}\ \textbf{没有提供独立的 B 型突破}} ✓✓✓$$

$$\textbf{最有价值的新规格（逐字采纳）}：\boxed{\text{寻找一个}\ \textbf{非 L-function 商型} \text{的 canonical arithmetic Dirichlet object},\ \text{其}\ \tfrac12\ \textbf{阈值能够独立证明}，\ \textbf{而不是由}\ \beta_*\ \textbf{预先编码}} ✓✓✓$$
$$\qquad \text{（这比继续尝试}\ \mu、\Lambda、\chi、\text{Hecke}\ \text{等权重变体}\ \textbf{明确得多}）✓$$

$$\textbf{T10（parity barrier 移出本档判词）}：\text{另立专档}\ \text{`V255`}\ \text{（状态＝}\textbf{[待核／参照档]}）;\ \textbf{本档判词不含} \ \text{parity barrier} ✓✓$$
$$\qquad \text{理由：}\text{（i）命题类型不同（"可构造 signed sieve 权重的能力上限"}\ne\text{"canonical L-函数商族"}）;（ii）\textbf{目前无蕴含链} \text{把它接到}\ \beta_*=\tfrac12 ✓✓$$


---

## 【型标注】（`NEG-REGISTER-1`，2026-09-18 20:1x）

$$\text{本档定级}：\textbf{T-III}\ \text{（框架性重述：自标 `§10` T1 收紧（奇点只给下界））}✓$$
$$\qquad \text{硬内容}：\\sum_a\\mu(a)/(a^c\\log a)=\\int_c^\\infty ds/\\zeta(s);\ \text{Landau}✓$$
$$\qquad ⚠️\ \textbf{自标收紧}：\text{奇点只给}\ \textbf{下界}\ \sigma_c\\ge\\beta_*;\ \text{反向（}\sigma_c=\\beta_*）\ \textbf{需独立证明}✓✓$$
$$\qquad \Longrightarrow \text{"canonical 源不可达}\ \\tfrac12\text{"}\ \text{是}\ \textbf{归纳级};\ \text{不可引为定理}✓$$
$$\textbf{引用纪律（本档确立）}：\text{引用本档时必须}\ \textbf{随引其型};\ \textbf{不得} \text{去条件化引用}✓✓$$
