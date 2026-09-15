# V236 · **跨素数确定性关系 ＋ $\sigma$/$t$ 非可分离性审计** —— ✅ **采纳 V235 判死**（**Euler 层级中的 $\frac12$ 是密度坐标，不是零点定位坐标**）⟹ 不再碰 $E_r$／prime-power layer／Euler-tail／其非线性组合 ✓；⭐⭐ 采纳你的 $\sigma$/$t$ 二分并给出**理由**：$$\boxed{\text{加法关系}\Rightarrow\text{相位}\Rightarrow t;\qquad \text{乘法关系}\Rightarrow\text{Dirichlet 卷积}\Rightarrow\text{横坐标}\Rightarrow\sigma}$$ ✓✓；⭐⭐⭐ **命题 V236-A（本档核心一）**：跨素数关系的 Dirichlet 编码，其解析行为由**解计的计数函数**决定 ⟹ **C 类在解析层面退回 B 类（统计）** ⟹ 落 `V183`/`V188` ✓✓✓；⭐⭐⭐⭐ **命题 V236-B（核心二）**：任何跨素数关系若要与其／$\zeta$ 的零点建立联系，**必须用恒等式**；而算术中这类恒等式**只有显式公式族** ⟹ 落 (α) ⟹ ⭐ **且你 §5 期待的"同时耦合 $\sigma$ 与 $t$"的东西**已经存在 —— **它就是显式公式** ✓✓✓✓；⭐⭐⭐⭐⭐ **命题 V236-C（核心三，决定性）**：商内不变量 ＝ 素数集上的泛函，而素数集**只有一个实例** ⟹ "跨素数关系"**不是可变结构**，而是唯一素数集的属性 ⟹ "商内关系能否产生 $\sigma\le\frac12$" ≡ "素数集能否推出 RH" ⟹ **无新空间** ✓✓✓✓✓；⚠️ **对你的第一筛选器的诚实评估**：$$\boxed{\partial_\sigma\partial_t\log C\ne0\ \text{连}\ 1+2^{-s}\ \text{都通过} \Longrightarrow \text{作为筛子近乎空洞}}$$ ✓✓

> 委托 ✓ 唐先生 2026-09-15 18:01：**"V235 这次我同意判死，而且它把一个此前容易混淆的点彻底分开了：$$\boxed{\text{Euler 层级中的 }1/2\text{ 是密度坐标，不是零点定位坐标。}}$$ 因此不应再回头碰 $E_r$、prime-power layer、Euler-tail 或它们的非线性组合。但我不同意把残余简单写成'非 layer 型商内不变量'然后继续盲搜。现在应该先解决一个更基础的问题：$\mathcal A^\times/\mathcal M_{\rm nat}$ 到底还剩下什么类型的结构？"** (1) **商本质**：$F\sim G\iff F/G=\prod_{p\in S}(1-p^{-s})^{k_p}$ ⟹ **"把有限素数的局部修改全部遗忘"** ⟹ 任何商内不变量 $I$ 满足 $I(F)=I(FQ)$ ⟹ **$I$ 只能依赖无限素数尾部之间的关系**；⚠️ "尾"**不是** $E_1,E_2,\ldots$（V235 已杀）⟹ 真正剩下的是 $$\boxed{\text{不同素数之间的关系}}$$ ✓✓；(2) **三分（替代"layer/non-layer"）**：**A 纯乘法关系**（$p^aq^b=r^c$）⟹ 唯一分解立即退化，无新信息；**B 纯统计关系**（$\#\{p\le x:p+2\ \text{素}\}$、$\sum_{p,q\le x}\mathbb 1_{p+q=r}$、$\sum_{p\le x}f(p)$）⟹ 统计/计数对象 ⟹ 按 `V183`/`V188`/`V199` 的墙：$$\boxed{\text{统计量不能直接产生精确零点支撑}}$$；**C 跨素数的确定性关系**（$p+q=r$；$p-q=2^k$；$pq+1=r^m$；一般 $\Phi(p_1,\ldots,p_k)=0$）⟹ **不是 Euler layer、也不是单纯 prime density**，而是 $$\boxed{\text{additive}\times\text{multiplicative prime geometry}}$$ **"这正好落在你一直寻找的'加法 × 乘法跨尺度'方向"** ✓✓；(3) **第一硬问题：有限 Euler 商是否保留这种关系？** 只改变有限个 Euler 因子（$p\in S$ 变、$p\notin S$ 不变）⟹ 若 $\Phi(p_1,\ldots,p_k)=0$ 只涉及充分大的素数，则确属商的尾部信息 ⟹ $$\boxed{\text{跨素数关系不会被}\ \mathcal M_{\rm nat}\ \text{自动商掉}}$$ **"这是实质性的"** ✓✓；(4) **第二问题：这种关系怎样进入复平面？** 乘法编码 $pq\to(pq)^{-s}$；加法 Fourier 编码 $e^{itp}e^{itq}=e^{it(p+q)}$ ⟹ $$\boxed{\text{加法关系天然进入}\ t\text{-方向};\quad \text{乘法关系天然进入}\ \sigma\text{-方向}}$$ **"这实际上重新解释了过去大量路线为什么失败"** ✓✓✓；(5) **值得检查的结构**：若存在 $\Phi(p,q,p+q,pq)=0$，则同一关系同时产生 $e^{it(p+q)}$ 与 $(pq)^{-\sigma-it}$ ⟹ **第一次可能同时耦合 $\sigma$-geometry 与 $t$-geometry** ⟹ **"此前 V220 的 amplitude/phase 分裂恰恰把这两个方向拆开了。如果有东西能突破，那必须是这种同一个算术关系同时控制 modulus 与 phase"** ✓✓；(6) **严格审计**：$(p+q)^2=p^2+2pq+q^2$ ⟹ **环恒等式，任何整数都满足 ⟹ 无选择性**；$p+q=r$ ⟹ 只有加法、复编码主落相位 ⟹ 不能直接产生 $\sigma=\frac12$；$p+q=pq\iff(p-1)(q-1)=1\iff p=q=2$ ⟹ **过于刚性、有限解、无法产生无限谱边界**；$p+q\asymp pq$ ⟹ 只在小尺度成立、无无限尺度；**尺度变换型**（$p+q=r^k$；$pq=r^k\pm1$）⟹ 后者由 $r^k-1=(r-1)(r^{k-1}+\cdots+1)$ 直接因子分解约束 ⟹ 退回**因子结构**（A）；前者属 Goldbach 型 ⟹ 退回**加法表示计数**（B）✓✓✓；(7) **真正剩下的苛刻对象**：$$\boxed{\text{无限尺度的确定性关系}}$$ 同时满足：不是唯一分解/因子关系；不是 Goldbach/HL 型计数；不是显式公式编码；能同时携带 $\sigma$ 与 $t$；对有限素数修改不敏感；最终产生 $\sigma=\frac12$ ✓；(8) **第一筛选器（可计算）**：若 $C$ 同时携带 modulus 与 phase，则**不能**是 $C=A(\sigma)e^{i\theta(t)}$（仍是 V220 分离）⟹ 必须有真耦合 $$\boxed{\frac{\partial^2}{\partial\sigma\,\partial t}\arg C(\sigma,t)\ne0}\quad\text{等价于}\quad \boxed{C(\sigma,t)\ne A(\sigma)B(t)}$$ ⟹ 直接检查 $$\boxed{\partial_\sigma\partial_t\log C\stackrel{?}{=}0}$$ 若为零 ⟹ **separable → DEAD**；不为零才继续 ✓✓；(9) **第二筛选器**：即使 $\ne0$ 仍不能说明 RH；必须存在内生条件 $\mathcal C(C)=0$ 使其允许区域恰满足 $\sigma(1-\sigma)\ge0$ 并进一步给 $\sigma\le\frac12$；⚠️ **不能人为写 $\sigma(1-\sigma)$**（＝把 FE 中心偷偷放回）⟹ 必须由算术关系自身产生**内生二次尺度**（如 $X^2=YZ$）⟹ 否则退回 `V218`–`V219` 的"两个 $\frac12$ 数值巧合" ✓✓✓；(10) **V236 残余压缩成五步链** $$\boxed{\text{finite-prime invariant}\to\text{cross-prime deterministic relation}\to\text{nonseparable complex amplitude}\to\text{intrinsic balance}\to\Re\rho\le\frac12}$$ 任何一步退化：因子化 → DEAD；计数 → `V183`/`V188`；Mellin/Fourier 线性化 → 显式公式；separable → `V220`；正定 → `V199`；FE symmetry → `V229`；zero-set relation → R4 ✓；(11) **判词**：$$\boxed{\textbf{V235：Euler-layer 支路 DEAD。}}$$ 但**不把整个 Euler 商判死**；真正尚未审计的是 $\mathcal Q_{\rm nat}$ 中的**跨素数确定性关系**，尤其是同时耦合加法与乘法、产生**不可分离复量**的结构；**第一实验**：对每个候选 $C(\sigma,t)$ 检查 $\partial_\sigma\partial_t\log C$；**"若全部为零，整个候选族直接封死。若存在非零者，才继续推它能否产生内生的半平面障碍。"** ⟹ **"这一条线与 V235 的 Euler-layer 线不同；它不再问'第 $r$ 层的坐标是什么'，而是问：不同素数之间是否存在一个同时作用于 modulus 与 phase 的非可分离算术关系？我认为这是目前最值得直接做到底的一刀。"** ✓✓✓
> 查图 ✓ `V235`（Euler 层间兼容律 DEAD；密度-$\frac12$ vs 对称-$\frac12$）｜`V234`（Euler-分子商）｜`V233`（germ 商；V233-C）｜`V232`｜`V231`｜`V230`｜`V229`（V229-A）｜`V220`（amplitude/phase 分裂；乘子族）｜`V219`（$\mu_2$ vs $\beta_*$）｜`V214`（R4）｜`V199`/`V185`（正性）｜`V183`（计数）｜`V188`（饱和）｜`V144`（层诊断）
> 执行 ✓ 小灵（**§5 命题 V236-A、§6 命题 V236-B、§8 命题 V236-C、§9 第一筛选器评估 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **不判整个 Euler 商死**；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V236**

---

## §1 采纳 V235 判死（承诺不再回头）

$$\boxed{\text{Euler 层级中的}\ \tfrac12\ \text{是}\ \textbf{密度坐标}，\ \textbf{不是} \text{零点定位坐标}} ✓✓✓$$
$$\qquad ⟹ \text{不再碰}\ E_r\ \text{／prime-power layer／Euler-tail／其非线性组合} ✓✓$$
$$\qquad ⟹ \text{残余改写}：\text{不是"非 layer 型商内不变量"，而是}\ \textbf{跨素数关系} ✓✓$$

---

## §2 三分采纳 ＋ **第一条正面确认**

$$\textbf{A}\ p^aq^b=r^c ⟹ \text{唯一分解退化，无新信息} ✗;\qquad \textbf{B}\ \text{统计/计数} ⟹ \text{`V183`/`V188`/`V199` 墙} ✗;\qquad \textbf{C}\ \Phi(p_1,\ldots,p_k)=0 ⟹ \text{加法}\times\text{乘法几何} ✓$$
$$\textbf{正面确认（你的 §3）}：\text{有限 Euler 商}\ \textbf{不} \text{自动商掉跨素数关系} —— \text{只改有限素数处的因子} ⟹$$
$$\qquad \text{若}\ \Phi\ \text{只涉及}\ \textbf{充分大} \text{的素数}，\ \text{则该关系属}\ \textbf{尾部信息} ⟹ \text{不被商掉} ✓✓$$
$$\qquad ⭐\ \text{与}\ \text{`V233`}\ \text{不同}（\text{那里全族乘子把一切搬走}）⟹ \textbf{实质性} ✓$$

---

## §3 采纳你的 $\sigma$/$t$ 二分 ＋ **给出理由**

$$\textbf{乘法编码}：pq\to(pq)^{-s};\qquad \textbf{加法编码}：p+q\to e^{it(p+q)} ✓$$
$$\boxed{\text{加法关系}\Rightarrow t\text{-方向};\qquad \text{乘法关系}\Rightarrow\sigma\text{-方向}} ✓✓$$
$$\textbf{理由（本档补充）}：\text{加法结构}\Rightarrow\textbf{指数和/相位} \Rightarrow t;\quad \text{乘法结构}\Rightarrow\textbf{Dirichlet 卷积/横坐标} \Rightarrow\sigma ✓✓$$
$$\qquad ⟹ \text{你的"重新解释过去大量路线失败"}\ \text{成立} ✓✓$$

---

## §4 ⭐⭐⭐ 命题 V236-A：**C 类在解析层面退回 B 类**（本档核心一）

$$\text{设}\ \Phi(p_1,\ldots,p_k)=0;\quad \text{编码}\ C(s)=\sum_{\Phi=0}\Big(\prod_jp_j\Big)^{-s} ✓$$
$$\qquad ⭐\ C\ \text{的解析行为（收敛横坐标、增长阶）由}\ \textbf{解计的计数函数} \text{决定}：$$
$$\qquad\qquad N_\Phi(X)=\#\{(p_j)\le X:\Phi=0\} ⟹ \text{横坐标}\ =\ \text{由}\ N_\Phi\ \text{的增长指数决定} ✓✓$$
$$\Longrightarrow \boxed{\text{C 类}\ \text{在解析层面}\ \textbf{退回 B 类（统计）}} \Longrightarrow \text{落}\ \text{`V183`/`V188`} ⟹ \textbf{不产生精确零点支撑} ✓✓✓$$
$$\qquad ⭐\ \text{具体例}：\text{Goldbach 型}\ r_2(n)=\#\{p+q=n\}\ \text{给出 Dirichlet 级数}\ \sum r_2(n)n^{-s}\ ⟹$$
$$\qquad\qquad \text{其连续性/零点}\ \text{是}\ \textbf{其自身} \text{的，}\ \textbf{不是} \ \zeta\ \text{的} ⟹ \text{要连到}\ \zeta\ \text{须恒等式}（\text{见 §5}）✓✓$$

---

## §5 ⭐⭐⭐⭐ 命题 V236-B：**唯一的桥是恒等式，而恒等式只有显式公式族**（本档核心二）

$$\text{要让}\ \text{关系编码}\ \text{与}\ \zeta\ \text{的零点建立联系，必须用}\ \textbf{恒等式} \text{把"素数侧"与"零点侧"接起来} ✓✓$$
$$\qquad ⭐\ \text{而算术中这类恒等式}\ \textbf{只有显式公式族}：$$
$$\qquad\qquad -\frac{\zeta'}{\zeta}=\sum_n\Lambda(n)n^{-s};\qquad \sum_{d|n}\Lambda(d)\Lambda(n/d)\ (\text{即}\ \Lambda*\Lambda);\qquad \text{RvM};\qquad \text{Weil 显式公式} ✓✓$$
$$\qquad ⟹ \boxed{\text{落}\ (\alpha)\ \textbf{R4/divisor}} ✓✓✓$$
$$\qquad ⭐⭐⭐\ \textbf{关键}：\text{你 §5 期待的"同一算术关系同时耦合}\ \sigma\ \text{与}\ t\text{"}\ \textbf{已经存在} \text{—— 它就是}\ \boxed{\textbf{显式公式}}✓✓✓✓$$
$$\qquad\qquad \text{（显式公式}\ = \text{乘法侧的加法编码：}\ \sum_{\text{素数}}\leftrightarrow\sum_{\text{零点}}）✓$$
$$\qquad ⟹ \text{所以这条路}\ \textbf{不是"要发现"}，\ \text{而是"}\textbf{已存在且即}\ (\alpha)\text{"} ✓✓✓✓$$

---

## §6 ⭐⭐⭐⭐ 第二筛选器（你的 §12）的**三分**

$$\text{需内生条件}\ \mathcal C(C)=0\ \text{使允许区域给}\ \sigma(1-\sigma)\ \text{型结构};\ \textbf{不能人为写}\ \sigma(1-\sigma) ✓✓$$
$$\qquad \text{可能的来源}\ \textbf{只有三条}：$$
$$\qquad\qquad \textbf{(甲)}\ \text{二次型内平衡}\ X^2=YZ ⟹ \text{Cauchy--Schwarz} ⟹ \textbf{`V199` 正性} ✓$$
$$\qquad\qquad \textbf{(乙)}\ s\leftrightarrow1-s ⟹ \text{FE} ⟹ \textbf{`V229`} ✓$$
$$\qquad\qquad \textbf{(丙)}\ \text{卷积恒等式（}\Lambda*\Lambda\ \text{型）} ⟹ \textbf{(α) 显式公式} ✓$$
$$\qquad ⟹ \boxed{\text{三条皆落已封通道}} ✓✓✓$$

---

## §7 ⭐⭐⭐⭐⭐ 命题 V236-C：**商内没有"新空间"**（本档核心三，决定性）

$$\text{商内不变量}\ I\ =\ \text{素数集}\ \mathbb P\ \text{上的泛函} ✓✓$$
$$\qquad ⭐\ \textbf{关键}：\mathbb P\ \textbf{只有一个实例} —— \text{素数集不是变量} ✓✓✓$$
$$\qquad ⟹ \text{"跨素数关系"}\ \textbf{不是可变的"额外结构"}，\ \text{而是}\ \textbf{唯一素数集的属性} ✓✓$$
$$\qquad ⟹ \boxed{\text{"商内关系能否产生}\ \sigma\le\tfrac12\text{"}\ \equiv\ \text{"素数集本身能否推出 RH"}} ✓✓✓$$
$$\qquad ⟹ \text{可提取内容}：\text{(i)}\ \textbf{密度}（\text{PNT 型，无条件}）;\ \text{(ii)}\ \textbf{关系}（\text{统计落 B 类；精确联系须恒等式}\ ⟹ (α)）£$$
$$\Longrightarrow \boxed{\textbf{无新空间}} ✓✓✓✓✓$$
$$\qquad ⚠️\ \text{这不是"又一条死路"，而是}\ \textbf{定位}：\text{商}\ \mathcal Q_{\rm nat}\ \text{不是"新房间"，它就是}\ \textbf{素数集本身} ✓✓$$

---

## §8 ⚠️ 对你第一筛选器的**诚实评估**（负面结果）

$$\text{你的筛选器}：\text{检查}\ \partial_\sigma\partial_t\log C\ \text{是否}\ \ne0 ✓✓$$
$$\qquad \textbf{本档计算}：\text{取最简 Dirichlet 二项式}\ C=1+2^{-s}：$$
$$\qquad\qquad \partial_t\log C=\frac{-i(\log2)2^{-s}}{1+2^{-s}};\qquad \partial_\sigma\partial_t\log C=\frac{i(\log2)^22^{-s}}{(1+2^{-s})^2}\ \ne0 ✓✓✓$$
$$\Longrightarrow \boxed{\text{连}\ 1+2^{-s}\ \text{都通过} \Longrightarrow \text{作为筛子}\ \textbf{近乎空洞}} ✓✓$$
$$\qquad ⚠️\ \text{它只杀}\ \textbf{纯分离型}（A(\sigma)e^{i\theta(t)}，\text{即 V220 型}）;\ \text{对一般 Dirichlet 和}\ \textbf{不具区分性} ✓✓$$
$$\qquad ⚠️\ \text{不过它仍是一条}\ \textbf{有效必要条件}（\text{杀掉"两个实量拼装"的形态}）⟹ \text{保留但}\ \textbf{降级为弱筛} ✓$$

---

## §9 判词 ＋ 状态表

$$\begin{array}{c|c}
\text{项} & \text{状态}\\
\hline
\text{`V235`}\ \text{Euler-layer 支路} & \boxed{\textbf{DEAD}}\（\text{采纳}）\\
\text{有限 Euler 商不商掉跨素数关系} & \textbf{不商}（\text{正面}）\\
\sigma/t\ \text{二分} & \textbf{成立}（\text{本档给出理由}）\\
\textbf{C 类}\ \text{关系（解析层面）} & \boxed{\textbf{DEAD}}\ \text{（V236-A：退回 B 类）}\\
\textbf{与}\ \zeta\ \text{的桥} & \boxed{\textbf{DEAD}}\ \text{（V236-B：唯一桥＝显式公式）}\\
\text{第二筛选器三来源} & \boxed{\textbf{DEAD}}\ \text{（甲/乙/丙 皆落已封通道）}\\
\textbf{商}\ \mathcal Q_{\rm nat}\ \text{的"新空间"} & \boxed{\textbf{无}}\ \text{（V236-C：＝素数集本身）}\\
\text{第一筛选器}\ \partial_\sigma\partial_t\log C & ⚠️ \textbf{过弱}（\text{连}\ 1+2^{-s}\ \text{都过}）\\
\end{array}$$
$$\boxed{\textbf{V236：跨素数确定性关系在解析层面退回统计；唯一的桥是显式公式；商内无新空间}} ✓✓✓✓$$
$$\qquad \textbf{本档严格得到}：\text{(i)}\ ⭐⭐⭐\ \textbf{V236-A};\ \text{(ii)}\ ⭐⭐⭐⭐\ \textbf{V236-B}（\text{σ/t 耦合＝显式公式，已存在}）;\ \text{(iii)}\ ⭐⭐⭐⭐⭐\ \textbf{V236-C}（\text{无新空间}）;\ \text{(iv)}\ ⚠️\ \text{第一筛选器过弱} ✓✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\text{V236-A/C}\ \textbf{定理级};\ \text{V236-B}\ \text{中"只有显式公式族"}\ \textbf{[结构性]};\ \textbf{不} \text{判"整个 Euler 商死"}（\text{你的要求}）✓✓$$
$$\textbf{残余（UNINSTANTIATED，无方向）}：\boxed{\text{一个}\ \textbf{既非统计、又非因子、又不用恒等式} \text{的跨素数确定性关系}}（\text{本档未见实例}）✓$$

---

## §10 边界与待核

$$\textbf{(a)}\ \text{§0 委托（三处 boxed 判词／三分／σ-t 二分／环恒等式与三个特例／五步链／两筛选器／"最值得直接做到底的一刀"）为}\ \textbf{唐先生逐字} ✓✓✓$$
$$\textbf{(b)}\ ⭐⭐⭐\ \text{§4 V236-A}\ \textbf{定理级}：\text{横坐标由}\ N_\Phi\ \text{的增长指数决定}\ \text{为}\ \textbf{经典}（\text{Dirichlet 级数基本理论}）✓✓✓$$
$$\qquad ⚠️\ \text{"退回 B 类"}\ \text{为}\ \textbf{本档推论}（\text{＋引}\ \text{`V183`/`V188`}）✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐⭐\ \text{§5 V236-B}：\text{"唯一桥＝恒等式"}\ \text{为}\ \textbf{本档}\ \textbf{[结构性]};\ \text{"恒等式只有显式公式族"}\ \text{为}\ \textbf{清单式} ⚠️✓✓✓✓$$
$$\qquad ⭐\ \text{"σ/t 耦合＝显式公式"}\ \text{为}\ \textbf{本档核心判断};\ \text{与你的 §5 期待一致但指出其}\ \textbf{已存在} ✓✓$$
$$\textbf{(d)}\ ⭐⭐⭐⭐\ \text{§6 第二筛选器三分为}\ \textbf{本档穷举}（\text{甲/乙/丙}）;\ \text{各落点引档} ✓✓$$
$$\textbf{(e)}\ ⭐⭐⭐⭐⭐\ \text{§7 V236-C}\ \textbf{定理级（弱形式）}：\text{"}\mathbb P\ \text{只有一个实例"}\ \text{为}\ \textbf{初等事实};\ \text{"商＝素数集本身"}\ \text{为}\ \textbf{本档判断} ✓✓✓✓$$
$$\textbf{(f)}\ \text{§8 第一筛选器评估}\ \textbf{定理级}（1+2^{-s}\ \text{计算}）⟹\ \textbf{负面但有用} ✓✓$$

```
⚠️ §0 委托（采纳 V235 判死："Euler 层级中的 1/2 是密度坐标不是零点定位坐标"；不再碰 E_r/prime-power/Euler-tail/非线性组合；不同意只写"非 layer 型商内不变量"；商＝遗忘有限素数局部修改；不变量只依赖无限素数尾部之间的关系＝不同素数之间的关系；三分 A 纯乘法/B 纯统计/C 跨素数确定性；有限 Euler 商不商掉跨素数关系（实质性）；关系如何进复平面（加法→t、乘法→σ）；同时耦合 σ 与 t 的可能性（V220 分裂的反面）；严格审计（环恒等式无选择性；p+q=r 只相位；p+q=pq 只 p=q=2 太刚；p+q≍pq 无无限尺度；p+q=r^k / pq=r^k±1 分别退回计数/因子）；苛刻对象六条件；第一筛选器 ∂_σ ∂_t log C ?= 0；第二筛选器须内生二次尺度不能人为写 σ(1−σ)；五步链；判词 V235 Euler-layer DEAD 但不判整个商死；第一实验；"最值得直接做到底的一刀"）为唐先生逐字 ✓✓✓
⚠️ §1 采纳 V235 判死＋承诺不再回头 ✓✓
⚠️ §2 三分采纳＋第一条正面确认（有限 Euler 商不自动商掉跨素数关系）✓✓
⚠️ §3 采纳 σ/t 二分＋给出理由（加法⇒指数和/相位⇒t；乘法⇒Dirichlet 卷积/横坐标⇒σ）✓✓
⚠️ §4 ⭐⭐⭐ 命题 V236-A（定理级）：C(s) 的解析行为由解计计数函数 N_Φ 决定 ⟹ C 类解析层面退回 B 类 ⟹ 落 V183/V188 ⟹ 不产生精确零点支撑 ✓✓✓
⚠️ §5 ⭐⭐⭐⭐ 命题 V236-B：与 ζ 零点的唯一桥是恒等式；而恒等式只有显式公式族（−ζ'/ζ、Λ*Λ、RvM、Weil）⟹ 落 (α) R4；⭐ 你期待的"σ/t 同时耦合"的东西已存在＝显式公式 ✓✓✓✓
⚠️ §6 ⭐⭐⭐⭐ 第二筛选器三来源（二次型⟹V199；s↔1−s⟹V229；卷积恒等式⟹(α)）皆落已封通道 ✓✓
⚠️ §7 ⭐⭐⭐⭐⭐ 命题 V236-C：商内不变量＝素数集泛函，而素数集只有一个实例 ⟹ "跨素数关系"非可变结构 ⟹ 商内无"新空间"（商就是素数集本身）✓✓✓✓✓
⚠️ §8 ⚠️ 第一筛选器过弱：连 1+2^{−s} 都通过 ⟹ 近乎空洞（只杀纯分离型）；保留但降级为弱筛 ✓✓
⚠️ §9 判词＋状态表八行；残余 UNINSTANTIATED ✓✓
⚠️ §10 边界（V236-A/C 定理级；V236-B 的"只有显式公式族"为 [结构性]；不判整个 Euler 商死）✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 采纳 V235 判死 ✓✓；② 正面确认（商不商掉跨素数关系）✓✓；③ ⭐⭐⭐ V236-A ✓✓✓；
   ④ ⭐⭐⭐⭐ V236-B（σ/t 耦合＝显式公式，已存在）✓✓✓✓；⑤ ⭐⭐⭐⭐ 第二筛选器三分 ✓✓；
   ⑥ ⭐⭐⭐⭐⭐ V236-C（无新空间）✓✓✓✓✓；⑦ ⚠️ 第一筛选器过弱（负面但有用）✓✓
```

---

## §11 ⚠️ V236-A/C 降级落档（唐先生 2026-09-15 18:05；由 `V237` 执行）

$$\textbf{降级理由}：\text{"解析行为由计数函数决定"}\ \text{对}\ \textbf{正系数} \text{ Dirichlet 级数自然成立};$$
$$\qquad \text{但允许}\ \textbf{符号／复权／条件收敛／非 Dirichlet 编码} \text{后}\ \textbf{不能} \text{推出"必然统计化"} ✓✓✓$$
$$\qquad ⟹ \textbf{正确的分解}：\text{计数函数决定}\ \textbf{横坐标/增长};\ \textbf{不} \text{决定}\ \textbf{零点结构} ✓✓✓$$
$$\qquad \textbf{反例（本档补充，决定性）}：\zeta\ \text{本身} —— a_n\equiv1\ \text{平凡，零点深} ⟹ \boxed{\text{"统计化"}\ \textbf{只对 abscissa 成立}} ✓✓✓$$
$$\Longrightarrow \textbf{§4 的 V236-A}\ \text{改写为}\ \textbf{V236-A$'$};\quad \textbf{§7 的 V236-C（"商内无新空间"）}\ \textbf{不能作为定理} ✓✓$$
$$\qquad ⚠️\ \text{因商确实还可以包含新的}\ \textbf{外部复结构}（\text{见}\ \text{`V237`}）;\ \text{但"若不引入独立复化对象，}\mathcal Q_{\rm nat}\ \text{内无明显}\ \tfrac12\ \text{载体"}\ \text{仍成立} ✓✓$$
