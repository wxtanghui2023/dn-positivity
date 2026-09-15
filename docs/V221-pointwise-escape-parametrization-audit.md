# V221 · **逐点逃逸的参数化审计** —— ⭐⭐⭐ **本档新结果（命题 V221-A）**：若存在 canonical **$\iota$-等变双射** $\Phi:I_X\overset{\sim}{\to}Z(\xi)$，则 $$\boxed{\text{RH}\iff\iota_X\ \text{在}\ I_X\ \text{上恒等}}$$ 且若 $\iota_X$ **非平凡** $\Longrightarrow$ **RH 为假** ✓✓✓✓；⟹ **若 RH 真，则任何此类参数化必 $\iota_X\equiv\mathrm{id}$，而算术中 canonical 对合的平凡作用轨迹均退化 ⟹ 非退化 canonical $\iota$-等变参数化不存在** ✓✓✓✓；⭐ **可证伪预测**：能给出"canonical $\iota$-等变 ＋ $\iota_X$ 非平凡"的参数化 ⟹ 那是 **RH 的反证** ✓✓；⚠️ **本档不判 DEAD**（严格按纪律：只做第一性审计 ＋ 逐类算到第一非平凡例子）✓

> 委托 ✓ 唐先生 2026-09-15 15:57：**"V220 我接受。这里确实比 V219 更硬：乘子族不是一个例子，而是把'由聚合增长量恢复零点位置'的函数性直接破坏了。但我不建议现在继续制造一个'V221 新对象'。V220 已经把搜索逼到了最后一个真正不同的问题：逐点参数化。而且这次可以先做一个纯数学的硬审计，看看这个残余是否连'入口'都没有。"** (1) **残余**：$A_X(n)\in\mathbb C$，$X$ 独立于零点，双向识别 $A_X(n)=\rho_n$；**关键问题**：$$\boxed{\text{这个 }n\text{ 从哪里来？}}$$ (2) 若 $n$ 是**外部人为编号** ⟹ **立即失败**（只是把目标集合重新编号）⟹ R1–R4 须**强化**为：$X$ **自身必须产生参数空间 $I_X$** 与 $\Phi_X:I_X\to\mathbb C$，且 $\Phi_X(I_X)=Z(\xi)$ 须由**独立识别定理**证明；(3) **参数空间离散 ⟹ 二分**：**A 参数算术产生**（$i_n=n,p_n,(a_n,b_n)$）⟹ $X$ 已产生**零点的算术参数化** $i\mapsto\Phi_X(i)$ ⟹ **这正是 V215–V217 的残余**，只是写成了真正的映射 $I_X\overset{\Phi_X}{\to}Z(\xi)$，**"这里没有新的'幅度→位置'机制"**；**B 参数非算术产生** ⟹ 必来自连续／几何／谱／拓扑参数 ⟹ 而逐点输出是离散的 ⟹ **连续参数必须经过离散选择机制** ⟹ 而"连续空间→离散选择"正是 order／selection／spectral projection／critical points／zeros ⟹ 分别落回 `V147`／`V192`／`V204`／`V190` ⟹ $$\boxed{\text{连续参数不能无新选择机制地产生离散零点}}$$ (4) **比 V220 更强**：V220 说聚合→增长量→乘子障碍；现在进一步：逐点→必须独立索引→必须产生零点参数化 ⟹ 整条路线成闭环 ⟹ 残余被压成 $$\boxed{\textbf{不是"怎样从幅度得到 }\beta\textbf{"，而是"怎样独立生成整个零点集合"}}$$ (5) ⚠️ **危险：不能把上述二分宣布成"不可能"**：数学上确实可能存在完全独立的 $X$（算术递推／几何对象／组合对象），其内部自然产生序列 $x_1,x_2,\ldots$，再由深刻识别定理证明 $\{x_n\}=Z(\xi)$ —— **"这完全没有逻辑矛盾"** ⟹ 真问题是 $$\boxed{\text{有没有一种 }X\text{，其 }x_n\text{ 在零点出现以前就已经具有内禀定义？}}$$（正是 R1）；(6) **更强的反循环条件**：构造 $\Phi$ 时不得出现任何等价于 $N(T)$／$\arg\xi$／$\log|\xi|$／$S(T)$／$\Lambda(n)$ 的显式零点展开 ⟹ $$\boxed{\Phi_X\ \text{在完全没有 }Z(\xi)\ \text{的世界里仍然有定义}}$$（比 R1 更严格）；(7) **实验**：参数化反例审计 —— 第一步不涉及 RH，只检查 $$\boxed{\text{一个算术索引能否自然承载两个独立坐标 }(\beta_n,\gamma_n)?}$$ 因 $\rho_n=\beta_n+i\gamma_n$ 需要 $a_n\mapsto(A(a_n),B(a_n))$，$A=\beta_n,B=\gamma_n$ ⟹ **这解释了为什么 V220 最后的残余必须是复值逐点对象**；(8) **强的结构限制**：若 $A(a)=f(a),B(a)=g(a)$ 来自同一有限维代数算术对象 ⟹ 得有限维参数曲线 $a\mapsto f(a)+ig(a)$；**若 $a\in\mathbb N$，这当然可以产生任意复杂的离散集合——所以不能仅凭"有限维"杀死它** ⟹ $$\boxed{\text{不能用"参数少"证明不可能；必须找到具体的结构刚性}}$$ **"否则我们又会犯 V213/V214 那种过强否定。"**；(9) **不给 V221 判 DEAD**；目前能严格得到的是：V220 之后唯一剩余自由度是 $I_X\overset{\Phi_X}{\to}Z(\xi)$，须同时满足 **R1** $I_X,\Phi_X$ 独立于零点／**R2** $\Phi_X$ 是 $X$ 的内禀定理／**R3** $\Phi_X(I_X)=Z(\xi)$ 且内禀性质能推出 $\beta=\frac12$／**R4** 不能把零点信息藏进参数化／**R5** 必须同时产生 $\beta$ 与 $\gamma$／**R6** 不得退化为 FE／显式公式／谱／正性／归一化；(10) **最关键一句**：搜索空间已压缩成 $$\boxed{\textbf{能否从一个完全独立的算术对象，内禀地产生一个复离散点集，然后证明这个点集恰好就是 }Z(\xi)\textbf{？}}$$ **"若答案是肯定的，那么这不是'RH 的另一种包装'——那个 $X$ 本身就是突破。"**；下一步应直接对 $I_X\to\mathbb C$ 做**参数化第一性审计**：逐个算到第一个非平凡例子，**只有出现一个尚未落入 V147–V220 的具体 $X$，才继续** ✓
> 查图 ✓ `V148`（**RH ⟺ $\iota$ 无自由轨道**；缺席型）｜`V147`（序路线 T1／T2）｜`V190`（实根性）｜`V192`／`V204`（谱／index）｜`V215`／`V216`／`V217`（三接口／系数≡零点／交叉比死角）｜`V218`（S1 序-2 自对偶）｜`V220`（聚合障碍；乘子族）｜`V105`／`V106`（载体迁移 0/14；Q3 0/15）｜`V183`／`V162`（计数／FSC）
> 执行 ✓ 小灵（**§3 命题 V221-A、§5 逐类枚举 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ **不判 DEAD**（按你的明确要求）✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V221**

---

## §1 残余的精确形式

$$\text{残余}：A_X(n)\in\mathbb C,\ X\ \text{独立于零点},\ \text{双向识别}\ A_X(n)=\rho_n ✓$$
$$\qquad ⚠️\ \text{若}\ n\ \text{是}\ \textbf{外部人为编号} ⟹ \text{只是把}\ Z(\xi)\ \textbf{重新编号} \Longrightarrow \textbf{立即失败} ✓✓$$
$$\qquad ⟹\ \text{须强化为}：I_X\ \text{由}\ X\ \textbf{自身产生},\ \ \Phi_X:I_X\to\mathbb C,\ \ \Phi_X(I_X)=Z(\xi)\ \text{由独立识别定理证明} ✓$$
$$\qquad ⭐\ \text{反循环（你的 §5）}：\Phi_X\ \text{不得用}\ N(T)／\arg\xi／\log|\xi|／S(T)／\Lambda\ \text{的显式零点展开} \Longrightarrow$$
$$\qquad\qquad \boxed{\Phi_X\ \text{必须在一个}\ \textbf{完全没有}\ Z(\xi)\ \text{的世界里}\ \text{有定义}} ✓✓$$

---

## §2 离散参数的二分（你的 §2；确认）

$$\textbf{A 算术产生的参数}（i_n=n,\ p_n,\ (a_n,b_n)）⟹ \text{已产生}\ \textbf{零点的算术参数化} \Longrightarrow \text{即}\ \text{`V215`--`V217` 残余} \ \（\text{无新机制}）✓✓$$
$$\textbf{B 非算术产生的参数} ⟹ \text{必来自连续／几何／谱／拓扑} ⟹ \text{但输出是离散的} ⟹ \text{须经}\ \textbf{离散选择机制} ✓$$
$$\qquad ⟹\ \text{"连续}\to\text{离散选择"落回}：\text{order}\to\text{`V147`／`V210`};\ \text{spectral projection}\to\text{`V192`／`V204`};\ \text{critical points／real-rootedness}\to\text{`V190`} ✓✓$$
$$\Longrightarrow\ \boxed{\text{连续参数不能无新选择机制地产生离散零点}} ✓✓\（\text{确认你的结论}）$$
$$\qquad ⚠️\ \text{但如你所说}：\textbf{这}\ \textbf{不} \text{构成"不可能"证明}（\text{A 分支在逻辑上完全开放}）✓✓$$

---

## §3 ⭐⭐⭐ 本档新结果：**$\iota$-等变参数化**（命题 V221-A）

$$\text{由}\ \text{`V148`}：\text{FE 给}\ \iota:\rho\mapsto1-\bar\rho\ \text{（序 2）};\ Z(\xi)\ \text{在}\ \iota\ \text{下不变};\ \text{on-line 零点}\ =\ \iota\ \text{的}\ \textbf{不动点} ✓$$
$$\qquad \text{且}\ \textbf{RH}\iff\text{全部零点是}\ \iota\ \text{的不动点}\iff\boxed{\text{无自由轨道}} ✓✓$$
$$\textbf{命题 V221-A}：\text{设存在}\ \textbf{canonical（结构决定）双射}\ \Phi:I_X\overset{\sim}{\to}Z(\xi)，\ \text{并与}\ I_X\ \text{上的 canonical 对合}\ \iota_X\ \textbf{等变}：$$
$$\qquad \Phi\circ\iota_X=\iota\circ\Phi ✓$$
$$\qquad \text{则}：\qquad \boxed{\text{RH}\iff\iota_X\ \text{在}\ I_X\ \text{上}\ \textbf{恒等}} ✓✓✓$$
$$\qquad \textbf{证明}：\text{RH}\iff\forall\rho:\iota(\rho)=\rho\iff\forall i:\iota(\Phi(i))=\Phi(i)\iff\forall i:\Phi(\iota_X(i))=\Phi(i)\overset{\Phi\ \text{单}}{⟺}\forall i:\iota_X(i)=i ✓✓✓$$
$$\textbf{推论 1}：\text{若}\ \iota_X\ \textbf{非平凡}（\exists i:\iota_X(i)\ne i）\ \Longrightarrow\ \textbf{RH 为假} ✓✓$$
$$\textbf{推论 2}：\text{若 RH 真，则任何此类参数化必}\ \iota_X\equiv\mathrm{id} ⟹ \text{索引集}\ I_X\ \text{必须是}\ \textbf{"canonical 对合平凡作用"者} ✓✓$$
$$\qquad ⚠️\ \text{而算术中 canonical 对合的}\ \textbf{平凡作用轨迹均退化}：$$
$$\qquad\qquad \text{加性反射}\ k\mapsto-k\ \text{（固定点仅}\ 0）;\ \text{乘性反转}\ q\mapsto1/q\ \text{（仅}\ 1）;\ \text{Galois 共轭}\ \text{（仅有理点）};\ \text{复共轭}\ ✓✓$$
$$\qquad ⟹ \text{"}\iota_X\equiv\mathrm{id}\ \text{on all of}\ I_X\text{"}\ \text{迫使}\ I_X\ \textbf{退化} \Longrightarrow \boxed{\text{非退化 canonical }\iota\text{-等变参数化}\ \textbf{不存在（设 RH 真）}} ✓✓✓✓$$
$$\qquad ⭐\ \textbf{可证伪预测}：\text{若能构造}\ \textbf{"canonical ＋ }\iota\text{-等变 ＋ }\iota_X\ \text{非平凡"}\ \text{的参数化} ⟹ \text{那}\ \textbf{直接是}\ \text{RH 的}\ \textbf{反证} ✓✓✓✓$$
$$\Longrightarrow\ \boxed{\text{故}\ \text{`V220`}\ \text{残余的}\ \textbf{精确落点}：\text{一个}\ \textbf{不带}\ \iota\text{-相容性} \text{的 canonical 参数化}} ✓✓✓$$
$$\qquad \text{即：}\text{相容性}\ \textbf{由识别定理给出}，\ \textbf{而非由构造成立};\ \text{这一子情形}\ \textbf{本档关闭}，\ \text{其余}\ \textbf{保持开放} ✓✓$$

---

## §4 双坐标审计（你的 §6）—— 诚实报告：**不是瓶颈**

$$\text{要求}：a_n\mapsto(A(a_n),B(a_n))=(\beta_n,\gamma_n)\ \（\text{因}\ \rho_n=\beta_n+i\gamma_n）✓$$
$$\qquad ⚠️\ \textbf{诚实结论}：\text{双坐标要求}\ \textbf{容易满足} —— \text{canonical 算术函数}\ n,\ \varphi(n),\ \sigma(n),\ d(n),\ \log n,\ \Lambda(n)\ \text{多得是} ⟹$$
$$\qquad\qquad \boxed{\text{"一个算术索引承载两个独立坐标"}\ \textbf{不是瓶颈}} ✓✓$$
$$\qquad ⟹\ \text{该测试}\ \textbf{不能} \text{当筛选器用}（\text{否则会误判}）✓$$
$$\qquad ⭐\ \text{但有一处真结构}：\text{由}\ §3，\ \iota\text{-等变}\ \Longrightarrow\ \text{第一坐标}\ (\beta)\ \text{必须按}\ \beta\leftrightarrow1-\beta\ \textbf{反称配对} ⟹ I_X\ \textbf{必须自带序-2 结构} ⟹ \text{S1} ⟹ \text{`V218` A 类} ⟹ \text{需归一化}\ \to\text{(c)} ✓✓✓$$
$$\qquad \Longrightarrow\ \text{故}\ \text{双坐标＋}\iota\text{-等变} \text{仍落}\ \text{`V218`／(c)};\ \text{唯}\ \textbf{取消}\ \iota\text{-等变} \text{才开放} ✓$$

---

## §5 逐类枚举：能产生**离散复点集**的 canonical 结构（算到第一非平凡例子）

$$\begin{array}{c|l|l|l}
\text{类} & \textbf{第一非平凡例子} & \text{能否产生无限离散复点集} & \text{落点}\\
\hline
\text{E1 算术序列＋canonical 复函数} & f(n)+ig(n)\ \text{（如}\ n+in^2\text{）} & ✓\ \text{能（且可任意复杂）} & ⭐\ \textbf{开放}（＝残余；见 §3／§6）\\
\text{E2 谱／算子} & 自伴算子离散谱}\ \{\gamma_n\} & ✓\ \text{但只给}\ \gamma & \text{`V192` seal}（$\beta$ 只经退化／重数）✗\\
\text{E3 连续映射的轨道} & $x\mapsto x+1$ 的轨道 $=\mathbb N$ & ✓ & \text{`V210`／`V161`（FSC：有理动力学 ⟹ 有限谱通道）}✗\\
\text{E4 组合／图论} & 图的邻接谱 & 谱为代数整数且有界 & \text{密度不符}（\text{`V183`／`V162`：}N_\zeta\asymp T\log T）✗\\
\text{E5 递推} & 线性递推 ⟹ 有理生成函数；P-recursive & ✓\ \text{（如}\ _1F_1\text{）} & \text{`V216`（D-finite 反例实例）}✗\\
\text{E6 素数侧对象} & $\{p_n\}$、$\{\log p_n\}$ & ✗\ \text{实值，无第二坐标} & \text{需复化} ⟹ \text{回 E1} ✗\\
\text{E7 几何／测地} & 闭测地线长度谱 & ✓ & \text{`V105`／`V106`：载体迁移 0/14；Q3 0/15}✗\\
\text{E8 变分／临界点} & 泛函的临界值 & ✓ & \text{`V190`（de Branges／实根性）}✗\\
\text{E9 逐点参数化} & “第 $n$ 个零点” & ✓ & ⚠️\ \textbf{全部已知实现都违规}（见 §6）✗\\
\end{array}$$
$$\Longrightarrow\ \text{唯一未被关闭的单元格}\ =\ \textbf{E1 且取消}\ \iota\text{-等变} \text{（§3 末）} ✓✓$$

---

## §6 事实级陈述：**已知的零点参数化全部违反 R4**

$$\text{经典事实}：\text{“第}\ n\ \text{个非平凡零点”}\ \text{的一切已知定义}\ \text{都经由}：\ \arg\xi\ \text{的符号变化／}N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+S(T)\ \text{的反函数} ✓✓$$
$$\qquad ⟹\ \textbf{全部使用}\ Z(\xi)\ \text{的解析计数} ⟹ \text{全部违反}\ \text{你的 §5（R4）} ✓✓$$
$$\qquad ⭐\ \text{故 E9}\ \text{在}\ \textbf{已知实现} \text{层面}\ \textbf{封闭};\ \text{但}\ \text{“是否存在}\ \textbf{非计数型} \text{的 canonical 参数化”}\ \textbf{开放} ✓$$

---

## §7 判词（**不判 DEAD**）

$$\boxed{\textbf{V221：不判 DEAD}} —— \text{严格按你的纪律，只做第一性审计} ✓✓$$
$$\qquad \textbf{本档严格得到的三条}：$$
$$\qquad \text{(i)}\ \text{残余}\ \textbf{压成单一形式}：I_X\overset{\Phi_X}{\to}Z(\xi)\ \text{（R1--R6）} ⟹ \text{不再是"找新判据"} ✓✓$$
$$\qquad \text{(ii)}\ ⭐\ \textbf{$\iota$-等变子情形}\ \textbf{关闭}：\text{命题 V221-A ⟹ 非退化 canonical }\iota\text{-等变参数化不存在（设 RH 真）；}\text{且}\ \textbf{可证伪}（\text{若给出}\ \iota_X\ \text{非平凡者} ⟹ \text{RH 反证}）✓✓✓✓$$
$$\qquad \text{(iii)}\ \text{双坐标要求}\ \textbf{不是瓶颈}（\text{诚实报告}）;\ \text{但＋}\iota\text{-等变} ⟹ \text{S1} ⟹ \text{`V218`／(c)} ✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{声称"逐点参数化不可能"}（\text{你的明确警告}）；\ \textbf{不得} \text{用"参数少／有限维"证不可能} ✓✓✓$$
$$\textbf{残余（OPEN，非 UNINSTANTIATED）}：$$
$$\qquad \text{一个}\ \textbf{非}\iota\text{-等变} \text{的 canonical 参数化}\ (I_X,\Phi_X)：$$
$$\qquad\qquad \text{① 满足 R1--R6};\ \text{② 不预置}\ \iota\text{-相容性（相容性须由识别定理给出）};\ \text{③ 非计数型（不用}N(T)／\arg\xi／S(T)\text{）};\ \text{④ 会合处不落 (a)(b)(c)} ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§2 的二分}\ \textbf{确认你的结论}；\ \text{各落点为}\ \textbf{档案引用} ✓✓$$
$$\textbf{(b)}\ ⭐\ \text{§3 命题 V221-A 为}\ \textbf{本档新结果}（\text{三行证明}）；\ \text{其}\ \textbf{前提＝}\Phi\ \text{canonical 且}\ \iota\text{-等变} ——\ \textbf{该前提本身未证}（\text{是}\ \textbf{假设}，\ \text{非定理}）⚠️✓$$
$$\qquad ⚠️\ \text{“canonical ⟹ }\iota\text{-等变”}\ \text{与}\ \text{`V148`}\ \text{的“canonical 对称破缺 ⟹ 平凡化”}\ \textbf{同族但不同命题};\ \text{形式化}\ \textbf{待核} ✓$$
$$\textbf{(c)}\ \text{§4 的“双坐标不是瓶颈”为}\ \textbf{本档诚实判断};\ \text{与}\ \text{`V218`}\ \text{S1 的衔接为}\ \textbf{本档判断} ✓✓$$
$$\textbf{(d)}\ \text{§5 的九类枚举为}\ \textbf{本档整理};\ \text{各落点分别引档};\ \textbf{“唯一开放单元格＝E1＋非等变”为}\ \textbf{本档结论} ✓✓$$
$$\textbf{(e)}\ \text{§6 的“已知参数化全部经}\ \arg\xi／N(T)\text{”为}\ \textbf{经典事实} ✓✓$$

```
⚠️ §0 委托（n 从哪来／参数空间由 X 产生／离散二分 A-B／闭环／不得宣布不可能／反循环更强条件／双坐标实验／不能用"参数少"证不可能／R1-R6／不判 DEAD／下一步指令）为唐先生逐字 ✓✓✓
⚠️ §1 残余精确形式：外部编号 ⟹ 立即失败；须 I_X 与 Φ_X 由 X 产生；反循环：Φ_X 在无 Z(ξ) 的世界里仍有定义 ✓✓
⚠️ §2 离散参数二分：A 算术 ⟹ V215-V217 残余；B 非算术 ⟹ 连续→离散选择 ⟹ V147/V190/V192/V204；确认"连续参数不能无新选择机制地产生离散零点"，但**不构成不可能证明** ✓✓
⚠️ §3 ⭐⭐⭐ 新结果 命题 V221-A：canonical ι-等变双射 ⟹ RH ⟺ ι_X 在 I_X 上恒等；ι_X 非平凡 ⟹ RH 为假；若 RH 真则 ι_X ≡ id ⟹ 算术 canonical 对合的平凡轨迹退化 ⟹ 非退化 canonical ι-等变参数化不存在（设 RH 真）；⭐ 可证伪预测：给出 ι_X 非平凡者 ⟹ RH 反证 ⟹ 残余精确定位＝不带 ι-相容性的 canonical 参数化 ✓✓✓✓
⚠️ §4 双坐标审计：诚实报告不是瓶颈（canonical 算术函数多）；但 ι-等变 ⟹ β 需反称配对 ⟹ I_X 自带序-2 ⟹ S1 ⟹ V218 A 类 ⟹ (c) ✓✓
⚠️ §5 九类枚举（E1-E9）＋第一非平凡例子＋落点；唯一开放单元格＝E1 且取消 ι-等变 ✓✓
⚠️ §6 事实级：已知零点参数化全部经 arg ξ／N(T) ⟹ 全部违反 R4 ⟹ E9 在已知实现层面封闭 ✓✓
⚠️ §7 不判 DEAD；三条严格结果；残余（OPEN，非 UNINSTANTIATED）＋四条判据 ✓✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 残余压成单一形式 ✓✓；② ⭐⭐⭐ 命题 V221-A（新结果＋可证伪预测）✓✓✓✓；③ 双坐标审计的诚实结论 ✓✓；
   ④ 九类逐类第一非平凡例子＋落点 ✓✓；⑤ 已知参数化全部违规（事实级）✓✓；⑥ 不判 DEAD＋残余四条判据 ✓✓
```

---

## §9 ⚠️ 两处勘误（唐先生 2026-09-15 16:03；随后由 `V222` 执行）

$$\textbf{T10（推论 2 降级）}：\iota_X\ne\mathrm{id}\Longrightarrow\neg\text{RH}\ \textbf{只是 RH 的反证机制}，\ \textbf{不是}\ \text{"该 }X\ \text{不存在"的证明} ✓✓✓$$
$$\qquad ⟹\ \textbf{不得} \text{写成"非平凡}\ \iota_X\Rightarrow\text{参数化不存在"};\ \text{§3 推论 2}\ \textbf{降级} \text{为条件性推论} ✓$$

$$\textbf{T11（§4 的"反称配对"撤回）}：\text{仅由}\ \Phi\ \text{双射只能}\ \textbf{定义} \ \iota_X:=\Phi^{-1}\circ\iota\circ\Phi;\ \text{但该}\ \iota_X\ \textbf{由识别映射反推} ✓✓$$
$$\qquad \text{而 R1 要求}\ I_X,\Phi\ \text{独立于零点} ⟹ \boxed{\text{零点的 FE 对合}\not\Rightarrow\text{独立构造中的 canonical }\iota_X} ✓✓✓$$
$$\qquad ⟹\ \text{§3 命题 V221-A}\ \textbf{仅当}\ \iota_X\ \textbf{可先独立构造} \text{（再由识别定理证等变）时才生效};\ \text{残余}\ \textbf{不能被 S1 自动吃掉} ✓✓$$
