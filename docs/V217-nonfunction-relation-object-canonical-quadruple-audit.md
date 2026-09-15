# V217 · **非函数关系对象的类型审计（canonical quadruple／correspondence／moduli invariant）** —— ⭐ **交叉比的双重死角**：(K1) **纯 Möbius 不变数据无法钉住任何固定直线**（定理级：$\mathrm{PGL}_2$ 可把任意直线移到任意直线）✓✓✓；(K2) 要钉住必须先引入**归一化**（极点 $s=1$／欧拉积收敛），而归一化＝`V215` 的 **(c) archimedean／完成化接口** ⟹ 已封 ✓✓✓；⭐ **纤维三分 的 case III 的七种可实现形式全部映射到已封类** ✓✓✓；⭐ **canonical quadruple 三情形审计：结构决定 ⟹ CR 为常数；含零点 ⟹ 违反 R1；外部 X ⟹ 仍须识别箭头** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 15:30：**"V216 这次把一个真正的缝补上了……把 $\beta$ 藏进系数系统，本质上仍然是在描述零点几何。但我认为现在不能继续直接去找'另一种无限阶系数刚性'。那会非常容易再次掉进 LP/HB 的同义反复。"** 新任务：审计**"非函数对象的关系不变量"** —— 到 V216 为止 $X$ **最终都是函数 $F_X(s)$**，于是不可避免地落入"零点 $\leftrightarrow$ Hadamard $\leftrightarrow$ 系数 $\leftrightarrow$ 零点几何"⟹ 这解释了为什么搜索不断闭环；**但外部对象不一定是函数**：(1) **真正尚未测试的是二元关系**：$\mathcal R_X\subset X\times\mathbb C$ 或 correspondence $\Gamma_X:X\dashrightarrow\mathbb C$，关键区别 $\Gamma_X\ne\{\text{某函数零集}\}$ ⟹ **Hadamard／Newton／LP 那条链第一步就不适用**；(2) 须满足 R1–R4：$X$ 完全不用 $\zeta,\rho$；$X$ 自身有定理 $T_X$；识别定理 $\rho\in Z(\zeta)\iff(\rho,X)\in\Gamma_X$；$T_X\Longrightarrow\Gamma_X\subset\{\Re s=\frac12\}$；(3) **纤维三分**：I 纤维由方程定义 ⟹ 消去 $x$ ⟹ 回 `V214`；II 纤维由谱关系定义 ⟹ `V192`／`V204`；**III 纤维既非方程亦非谱** ＝ 真正新情况，须有**集合论／几何／范畴论意义上可验证的关系** ⟹ 具体问题：$$\boxed{\text{有没有一种非方程、非谱的 correspondence，可以把独立对象与 }\zeta\text{ 零点双向识别？}}$$ (4) **交点形式候选**：$A_X\cap B_X\leftrightarrow Z(\zeta)$ ⟹ RH 变成"某种独立几何交点只能位于固定 locus"；但若该刚性来自 positivity$\to$`V199`／hyperbolicity$\to$`V190`／self-adjointness$\to$`V192`／symmetry-fixed-point$\to$`V148`／index$\to$`V204` 又死 ⟹ 真正需要 $$\boxed{\text{非正性、非谱、非对合、非 index 的交点刚性}}$$ (5) **具体候选：交叉比／模空间刚性** —— $\beta$ 是横向位置参数；交叉比 $[z_1,z_2;z_3,z_4]$ **对 Möbius 变换不变**，因此**不是坐标、不是零点统计、不是系数、也不是谱值**；(6) 但不能停在这里：对 FE 配对 $\rho,1-\bar\rho$ **随便取两个辅助点**，交叉比当然可以人为制造 $\beta$ ⟹ 违反 R1／R4 ⟹ 真正的问题是 $$\boxed{\text{是否存在一个完全 canonical 的四元组，由外部对象 }X\text{ 自身产生？}}$$ **"如果没有，死。如果有，再算。"** (7) **V217 应做严格的 canonical quadruple audit**：找 $(Q_1,Q_2,Q_3,Q_4)$，$Q_i=Q_i(X)$ 完全不含任何 $\rho$；$\mathrm{CR}_X=[Q_1,Q_2;Q_3,Q_4]$ 满足 $X$ 自身已成立的刚性 $T_X(\mathrm{CR}_X)$；然后才问 $\rho\in Z(\zeta)\iff\mathrm{CR}_X=\Phi(\rho)$（若 $\Phi$ 只是人为把 $\rho$ 塞进去，立即 DEAD）；**"这一轮不要预设它能成功"**；**"我们现在是在测试一个数学对象类型：relation／correspondence／moduli invariant，而不是随意发明一个机制。"** **"如果 canonical quadruple 第一非平凡例子都不存在，就立即封掉这一整类。"**
> 查图 ✓ `V216`（系数≡零点）｜`V214`（消元）｜`V192`／`V204`（谱／index）｜`V148`（canonical 定向 ⟹ 平凡化）｜`V190`（LP/HB）｜`V199`｜`V166`（o-minimal 障碍）｜`V150`／`V211`｜`V200`｜`V196`（O3：morphism 型 ⟹ module 层）｜`V147`／`V210`（序路线）
> 执行 ✓ 小灵（**§2 七形式映射、§3 交叉比死角、§4 四元组三情形 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V217**

---

## §1 定位：这一轮测的是**对象类型**，不是机制

$$\text{前几轮}：X\ \text{都是函数} F_X(s) \Longrightarrow \text{零点}\leftrightarrow\text{Hadamard}\leftrightarrow\text{系数}\leftrightarrow\text{零点几何}\ \textbf{闭环}（\text{`V216` §4}）✓$$
$$\text{本档}：X\ \text{是}\ \textbf{关系／对应／模不变量};\ \text{须重新走 R1--R4};\ \text{关键是}\ \Gamma_X\ne\{\text{零集}\}\ \textbf{第一步就不适用} ✓$$
$$\qquad ⚠️\ \text{纪律}：\textbf{不预设成功};\ \text{若第一非平凡例子不存在}\ \Longrightarrow \textbf{封掉整类} ✓$$

---

## §2 ⭐ 纤维三分 ＋ **case III 的七种可实现形式**（本档核心一）

$$\text{你的三分}：\text{I 方程型}\to\text{`V214`};\ \text{II 谱型}\to\text{`V192`／`V204`};\ \textbf{III 既非方程亦非谱} ✓$$
$$\text{问}：\text{III 的"可验证关系"}\ \textbf{在数学上可能是什么}？\ \text{穷举其可实现形式}：$$
$$\begin{array}{c|l|l}
\text{形式} & \text{纤维的定义方式} & \text{落点}\\
\hline
\text{(i)}\ \text{definability} & \text{纤维在某个结构／语言中}\ \textbf{可定义} & \text{`V166`}\ \textbf{o-minimal 障碍}（\text{无法定义无限离散集}）；\ \text{余者→类 VI}（`V149` 封闭）\\
\text{(ii)}\ \text{measure} & \text{由测度论条件定义（}\textbf{满测度／典型}） & \text{`V188` 三层波动}＋\text{`V200` canonical 测度因子化}\\
\text{(iii)}\ \text{categorical} & \text{纤维是}\ \textbf{函子／态射关系} & \text{`V196` O3：}\textbf{native 作用皆 morphism 型} ⟹ \text{module 层（N4＋S10）}\\
\text{(iv)}\ \text{order} & \text{由序关系／极值定义} & \text{`V147`（T1／T2）＋`V210`（序／边界选择二分）}\\
\text{(v)}\ \text{combinatorial} & \text{图／组合结构性质} & \text{`V209`（改写复形饱和）＋`V200`（关联因子化）}\\
\text{(vi)}\ \text{homotopy} & \text{由同伦型（非 index）条件定义} & ⭐\ \text{零集／纤维}\ \textbf{是离散集} ⟹ \text{其同伦型}\ \textbf{由基数决定} ⟹ \textbf{退化为计数} ⟹ \text{`V188`／`V183`};\ \text{非离散纤维则落 index} ⟹ \text{`V204`}\\
\text{(vii)}\ \text{model-theoretic} & \text{在某模型中可定义} & \text{`V150`（WF 吸收）／`V211`（紧致性／选择）}\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{case III}\ \textbf{非空}，\ \text{但其七种可实现形式}\ \textbf{全部映射到已封类}} ✓✓✓$$

---

## §3 ⭐⭐ 交叉比候选的**双重死角**（本档核心二）

$$\textbf{(K1) 定理级}：\text{Möbius 不变数据}\ \textbf{不可能} \text{钉住任何}\ \textbf{固定} \text{直线} ✓✓✓$$
$$\qquad \text{理由}：\forall M\in\mathrm{PGL}_2(\mathbb C)\ \text{可把任一（广义）直线映到任一直线};\ \text{而 CR}\ \textbf{在}\ M\ \text{下不变} ✓$$
$$\qquad \Longrightarrow\ \text{若约束集}\ \mathcal C\ \text{是 Möbius 不变的且非空，则}\ M(\mathcal C)=\mathcal C ⟹ \text{若}\ M\ \text{把}\ \{\Re s=\tfrac12\}\ \text{移开，约束}\ \textbf{不能推出"在临界线上"} ✓✓✓$$
$$\qquad ⚠️\ \text{注意}：\text{CR}\in\mathbb R\iff\text{四点共圆} \text{是}\ \textbf{Möbius 不变} \text{的}\ \textbf{对构型的约束}（\text{可以紧}）;\ \text{但它紧的是}\ \textbf{圆}，\ \text{不是}\ \textbf{某条固定的直线} ✓$$

$$\textbf{(K2) 要钉住固定直线，必须先引入}\ \textbf{归一化} \Longrightarrow \text{落}\ \text{`V215` (c)} ✓✓✓$$
$$\qquad \text{临界线}\ \Re s=\tfrac12\ \textbf{不是模不变量}（\text{依赖坐标选择}）⟹ \text{钉它须}\ \textbf{破坏 Möbius 不变性} ✓$$
$$\qquad \text{算术中唯一 canonical 的 Möbius-破缺数据} ＝ \textbf{归一化}：\text{极点}\ s=1、\text{欧拉积收敛横坐标}\ \Re s=1 ✓✓$$
$$\qquad ⟹\ \text{而"归一化／完成化"}\ \textbf{就是}\ \text{`V215` 的}\ \textbf{(c) archimedean／完成化接口} ⟹ \textbf{已封} ✓✓✓$$

$$\textbf{(K3) 特例}：\text{若把直线}\ \textbf{定义为}\ \iota\ \text{的不动轨迹}（\text{FE 反演}），\ \text{则约束＝}\iota\text{-对称} ⟹ \textbf{自动成立} ⟹ \textbf{无信息} ✓✓✓$$
$$\qquad （\text{`V148`／`V212`(c)：canonical 定向 ⟹ 平凡化；}\iota\text{-对称是零集的本有属性}）✓$$

---

## §4 ⭐⭐ **canonical quadruple 审计**（你 §7 指定的核心任务）

$$\text{要求}：Q_i=Q_i(X)\ \textbf{完全不含}\ \rho;\ \ \mathrm{CR}_X=[Q_1,Q_2;Q_3,Q_4]\ \text{满足}\ T_X(\mathrm{CR}_X);\ \ \text{再问}\ \rho\in Z(\zeta)\iff\mathrm{CR}_X=\Phi(\rho) ✓$$
$$\begin{array}{c|l|l}
\text{情形} & \text{四元组来源} & \text{结果}\\
\hline
\text{A} & \textbf{结构决定的点}（\iota\ \text{的不动点、极点}\ s=1、s=0、\infty\ \text{等）} & \text{四点由}\ \zeta\ \text{的粗结构定死} ⟹ \mathrm{CR}\ \textbf{为常数} ⟹ \textbf{无}\ \beta\text{-信息}\ ✗\\
\text{B} & \text{四元组}\ \textbf{含零点位置} & \textbf{违反 R1}（\text{非独立构造}）⟹ \textbf{循环}（`V213`）\ ✗\\
\text{C} & \text{四元组来自}\ \textbf{外部}\ X（\text{不含}\ \zeta） & \mathrm{CR}_X\ \text{与零点}\ \textbf{无关系}，\ \text{除非识别定理挂钩} ⟹ \text{仍须经}\ \text{`V215`}\ \textbf{接口} ⟹ \text{未逃逸}\ ✗\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{canonical quadruple：A 为常数、B 循环、C 仍须接口}} ⟹ \textbf{第一非平凡例子不存在} ✓✓✓$$
$$\qquad ⭐\ \text{一般化（比 quadruple 更强）}：\text{任何}\ \textbf{结构决定的}\ \text{有限点集，其 Möbius 不变量都是}\ \textbf{常数};\ \text{含零点的既违反 R1} ✓✓$$

---

## §5 ⭐ 交点表述（你 §4）的归约

$$\text{设}\ A_X\cap B_X\leftrightarrow Z(\zeta);\ \text{RH 变成"交点只能位于固定 locus"} ✓$$
$$\qquad \text{"交点在固定 locus 内"}\ \text{的等价形式} ＝ \text{交点集}\ \textbf{被某个群作用的不动轨迹包含} ✓$$
$$\qquad \text{canonical 的此类作用} ＝ \text{FE 反演}\ \iota，\ \text{其不动轨迹}\ \textbf{就是临界线} ⟹ \text{条件是}\ \iota\text{-对称} ⟹ \textbf{自动} ⟹ \textbf{无信息} ✓✓✓$$
$$\qquad \text{其余五类来源（positivity／hyperbolicity／self-adjoint／index／symmetry）⟹}\ \text{`V199`／`V190`／`V192`／`V204`／`V148`} ⟹ \textbf{全封} ✓✓$$
$$\Longrightarrow\ \text{交点表述}\ \textbf{不构成新接口} ✓$$

---

## §6 ⭐ 元观察（本档的结构性收获）

$$\boxed{\text{`V215`--`V216` 的接口分类是}\ \textbf{关于"会合点"} \text{的，}\ \textbf{不是关于"对象类型"} \text{的}} ✓✓✓$$
$$\qquad \therefore\ \text{换对象类型（函数}\to\text{关系}\to\text{对应}\to\text{模不变量）}\ \textbf{不改变会合处} \text{的性质} ✓✓$$
$$\qquad \therefore\ \text{只要还要"与}\ \zeta\ \text{双向识别"，}\ \text{必然在某条 canonical 管道会合} ⟹ \text{接口分类照旧适用} ✓✓✓$$

---

## §7 判词与纪律

$$\boxed{\textbf{V217：DEAD} —— \text{非函数关系对象这一类}\ \textbf{在第一非平凡例子处即失败}} ✓✓✓$$
$$\qquad \textbf{三条独立理由}：\text{(i)}\ \text{case III 七种形式全落已封类（§2）};\ \text{(ii)}\ \text{交叉比双重死角（§3，K1 定理级＋K2 落 (c)）};\ \text{(iii)}\ \text{canonical quadruple 三情形（§4）} ✓✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\textbf{不得} \text{声称"任何关系型对象都不可能"};\ \text{本档证的是}\ \textbf{七形式的映射}＋\textbf{交叉比死角}＋\textbf{四元组三情形};\ \textbf{非全称否定} ✓✓$$
$$\qquad \textbf{残余（UNINSTANTIATED）}：\text{一个}\ \textbf{既非方程、非谱、非可定义、非测度、非范畴、非序、非同伦、非模型论} \text{的"可验证关系"};\ \text{本档未见实例};\ \text{判据}：\text{① 满足 R1--R4};\ \text{② 不属于上述任一形式};\ \text{③ 会合处不落 (a)(b)(c)} ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§2 的七形式枚举为}\ \textbf{本档归纳};\ \text{各映射分别引}\ \text{`V166`／`V188`＋`V200`／`V196`／`V147`＋`V210`／`V209`＋`V200`／`V204`＋`V183`／`V150`＋`V211`} ✓✓$$
$$\textbf{(b)}\ \text{§3(K1) 为}\ \textbf{定理级}（\mathrm{PGL}_2\ \text{作用可移直线}）✓✓✓;\ \text{(K2) 的"唯一 canonical Möbius 破缺＝归一化"为}\ \textbf{本档判断} ⚠️$$
$$\textbf{(c)}\ \text{§4 的 A／B／C 三情形为}\ \textbf{本档审计};\ \text{C 情形"仍须接口"依赖}\ \text{`V215` 分类} ✓✓$$
$$\textbf{(d)}\ \text{§6 元观察为}\ \textbf{结构性}，\ \textbf{非定理} ✓$$

```
⚠️ §0 委托（§1-§7 全部分点）为唐先生逐字 ✓✓
⚠️ §2 纤维三分 ＋ case III 七种可实现形式（definability/measure/categorical/order/combinatorial/homotopy/model-theoretic）全部映射到已封类 ✓✓✓
⚠️ §3 ⭐⭐ 交叉比双重死角：(K1) 定理级 —— Möbius 不变数据无法钉住固定直线；(K2) 钉住须归一化 ⟹ V215 (c) archimedean 接口；(+K3 若定义为 ι 不动轨迹 ⟹ 自动 ⟹ 无信息) ✓✓✓
⚠️ §4 ⭐⭐ canonical quadruple 三情形：A 结构决定 ⟹ CR 常数；B 含零点 ⟹ 违反 R1；C 外部 X ⟹ 仍须接口 ⟹ 第一非平凡例子不存在 ✓✓✓
⚠️ §5 交点表述归约为 ι-对称（自动）＋五类旧墙 ⟹ 非新接口 ✓✓
⚠️ §6 元观察：接口分类是关于"会合点"而非"对象类型" ⟹ 换类型不逃逸 ✓✓✓
⚠️ §7 判词 DEAD（三条理由）；纪律：不得全称否定；残余（八非形式）＋三条判据 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 纤维三分＋七形式映射 ✓✓✓；② 交叉比双重死角（K1 定理级）✓✓✓；③ canonical quadruple 三情形 ✓✓✓；
   ④ 交点表述归约 ✓✓；⑤ 元观察（会合点而非对象类型）✓✓✓；⑥ 残余与判据 ✓
```
