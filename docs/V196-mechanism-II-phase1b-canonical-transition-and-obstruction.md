# V196 · **机制 II · Phase-1-b：canonical transition structure 与 obstruction（从零构造）** —— 按唐先生五步顺序；**本档全程禁用** $\rho,\gamma,\beta,\Xi$、RH、Weil positivity、Li criterion ✓✓

> 委托 ✓ 唐先生 2026-09-15 13:25：**"开。V196 就攻 II，而且严格按你规定的 Phase-1-b，不碰 RH，不调用 F1–F4，不把它投影回旧四通道。"** ＋ **关键数学约束**：**"不能先假定 transition map 一定存在"** —— 第一步必须把**候选 transition structure 的来源空间也构造出来**，否则容易"先写 $T$，再给 $T$ 找意义"（反向工程）✓✓；并给定五步（V196-1…5）、三候选顺序（**A：$p\leftrightarrow q$ → B：$p\leftrightarrow\infty$ → C：尺度**）、**禁令**与**四条判据**
> 查图 ✓ `V195`（机制 II 与刚性引擎）｜`V187`／`V188`／`V194`（**本档不调用**，仅存档）｜`V176`–`V180`（既往 $H^1$ 触点，**本档不引用其结论**）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜编号 ✓ **V196**（台账已录；重跑多领 V197 作冗余保留）

---

## §0 执行纪律与禁令（✓ 逐字）

$$\textbf{禁止出现}：\rho,\quad\gamma,\quad\beta,\quad\Xi,\quad\mathrm{RH},\quad\text{Weil positivity},\quad\text{Li criterion};\qquad \textbf{甚至暂不问}\ \text{"这能不能证明 RH"} ✓$$
$$\textbf{只允许}：\boxed{(p,\ p^k,\ \Lambda(p^k),\ \log p)\to A_v\to T_{vw}\to\text{cocycle}\to\text{obstruction}\to\text{是否离散}} ✓$$
$$\qquad ⚠️\ \text{本档严格遵此执行：全文}\ \textbf{不含} \text{上述被禁符号} ✓$$

---

## §1 V196-1 底空间与局部对象（canonical；只 $p$-data）

$$\mathscr X=\{v_p:p<\infty\}\cup\{v_\infty\};\qquad \text{每个}\ v\ \text{给局部对象}\ A_v\ \text{与局部状态空间} ✓$$
$$\boxed{A_p\ \text{只使用}\ p,\ p^k,\ \log p,\ \Lambda(p^k)}\ ✓$$
$$\textbf{候选局部对象（皆 canonical，皆只用}\ p\text{-data）} ✓：$$
$$\qquad \text{(i)}\ \mathbb Z_p^\times\（\text{局部单位群}）;\qquad \text{(ii)}\ \mu_{p-1}\subset\mathbb Z_p^\times\（\textbf{局部挠}，Teichmüller 提升，}\text{阶}=p-1\ \textbf{有限}）✓✓$$
$$\qquad \text{(iii)}\ v_p:\mathbb Q^\times\to\mathbb Z\（\textbf{取值}\ \mathbb Z\ \textbf{离散}）;\qquad \text{(iv)}\ \log p\in\mathbb R_{>0}\（\textbf{尺度}）;\qquad \text{(v)}\ \Lambda(p^k)=\log p\（\text{只依赖}\ p）$$
$$\textbf{archimedean 局部对象}：A_\infty=\mathbb R_{>0}\ \text{或}\ \mathbb R^\times\（\text{canonical}）✓$$
$$\qquad ⚠️\ \text{注意}：\text{(ii)}\ \text{与}\ \text{(iii)}\ \text{已经是}\ \textbf{离散取值对象};\ \text{这正是 V196-4 要找的东西，}\text{见 §4} ✓✓$$

---

## §2 V196-2 过渡映射：**存在性 ＋ canonical 性检验**（本档第一个硬结果）

### 2.1 候选 A：$T_{p,q}:A_p\to A_q$（直接映射）—— ✗ **不存在 canonical 定义**

$$\text{问}：\ \text{是否存在}\ \textbf{canonical}\ T_{p,q}:\ \mathbb Z_p^\times\to\mathbb Z_q^\times\ \text{或}\ \mu_{p-1}\to\mu_{q-1}\（p\ne q\text{）}？$$
$$\qquad \text{答}：\boxed{\textbf{不存在}}\ ✓✓\ ——\ \text{理由}：\text{两者的}\ \textbf{挠阶不同}（p-1\ \text{vs}\ q-1\text{）},\ \text{且}\ \text{不存在自然的}\ p\text{-adic}\to q\text{-adic}\ \text{同态};$$
$$\qquad\qquad \text{任何}\ \mathbb Z_p^\times\to\mathbb Z_q^\times\ \text{都需}\ \textbf{额外选择}（\text{如先在}\ \overline{\mathbb Q}\ \text{中选一个公共提升}）⟹ \text{那}\ \textbf{不是 transition structure}，\ \text{只是}\ \textbf{人为编码} ✓✓$$
$$\qquad ⭐\ \text{按唐先生预定}：\text{"若不存在，直接知道"}\ \boxed{\text{素数之间没有这种 canonical gluing geometry}} ⟹ \textbf{转 B} ✓✓$$

### 2.2 ⭐ 但发现一条 canonical 的**替代道路：公共对象（common object）**

$$\text{不是}\ A_p\to A_q\ \text{的}\ \textbf{直接}\ \text{映射}，\ \text{而是}\ A_p\ \text{与}\ A_q\ \text{各自}\ \textbf{canonically}\ \text{映入同一个对象}：$$
$$\qquad \text{(甲)}\ \text{乘法侧}：\text{每个}\ p\ \text{给}\ \hat{\mathbb Z}^\times\ \text{中一个}\ \textbf{canonical 元素}\ p\（\text{即}\ p\ \text{在}\ \text{profinite 完备化中的像}\bigr) ✓\ ——\ \text{无需任何选择}$$
$$\qquad \text{(乙)}\ \text{加法侧}：\text{每个}\ p\ \text{给}\ \mathbb R_{>0}\ \text{中一个}\ \textbf{canonical 实数}\ \log p ✓$$
$$\qquad \text{(丙)}\ \text{局部挠侧}：\text{每个}\ \mu_{p-1}\ \text{canonically 映入}\ \overline{\mathbb Q}^\times\ \text{的挠子群}\ \mu_\infty=\bigcup_N\mu_N ✓$$
$$\qquad ⭐\ \text{结论}：\text{canonicity}\ \textbf{不在"点对点"层面成立}，\ \text{而在"}\textbf{共对象"}\ \text{层面成立} ⟹ \text{过渡结构应写成}\ \textbf{公共对象上的数据相容性} ✓✓$$

$$\textbf{archimedean 侧（B 的预检）}：A_\infty\ \text{是}\ \mathbb R_{>0};\ \text{与}\ \mathbb Z_p^\times\ \text{的公共对象需在乘法侧统一}：\hat{\mathbb Z}^\times\ \text{与}\ \mathbb R_{>0}\ \text{的公共宿主}＝\textbf{赋范群／idele 型对象} ✓$$
$$\qquad ⚠️\ \text{风险（记下，不判）}：\text{该公共宿主可能使整个结构退化为}\ \textbf{乘积公式的重写} ⟹ \text{按判据 ① 会被杀};\ \textbf{但须算到底} ✓$$

### 2.3 候选 C：尺度过渡 $T_{r\to r'}:A(r)\to A(r')$

$$\text{令}\ r=\log p\ \text{为尺度};\ A(r)\ \text{必须}\ \textbf{canonical} —— \text{但}\ \text{同一尺度下可有不同素数}（\text{如}\ \log p\ \text{相等需}\ p=q\text{，故无歧义}）$$
$$\qquad \Longrightarrow\ A(r)=A_p\ \text{当}\ r=\log p;\ \text{故}\ T_{r\to r'}\ \text{的 canonical 性}\ \textbf{同 §2.1}\ \text{一样失败}\ ⟹ \ \textbf{只能走公共对象道路} ✓$$
$$\qquad ⭐\ \text{尺度侧的 canonical 结构}：\mathbb R_{>0}\ \text{上的}\ \textbf{伸缩作用}\（r\mapsto\lambda r\text{）}\ \text{是}\ \text{canonical};\ \text{且}\ \{\log p\}\ \text{生成的格}\ \textbf{在}\ \mathbb Q\ \text{上线性无关} ✓$$
$$\qquad\qquad ⚠️\ \text{故尺度方向的"gluing defect"}\ \textbf{在格层面为零}（\text{自由格}）⟹ \text{见 §3.1} ✓$$

---

## §3 V196-3 Cocycle：两个支路（**一阶还是二阶由实际 gluing law 决定** ✓）

### 3.1 加法支（valuations／$\log p$）：**trivial**

$$\text{局部数据}：v_p(x)\in\mathbb Z,\ \text{尺度}\ \log p;\qquad \text{gluing law}＝\textbf{乘积公式}：\sum_{p}v_p(x)\log p-\log|x|_\infty=0\ \ \forall x\in\mathbb Q^\times ✓$$
$$\qquad\Longrightarrow\ \text{该 cocycle}\ \textbf{恒为}\ 0\（\text{加法上闭链}）;\ \text{且}\ \{\log p\}\ \text{在}\ \mathbb Q\ \text{上}\ \textbf{线性无关}\（\text{由唯一分解}；\text{Baker 给更强}）$$
$$\qquad\Longrightarrow\ \text{格是}\ \textbf{自由}\ \text{的} ⟹ \boxed{\text{obstruction}=0}\ ⟹ \text{按判据 ①（}\text{trivial／恒等式}\bigr)\ ⟹ \textbf{杀} ✓✓$$

### 3.2 ⭐ 乘法支（局部挠／符号）：**取值离散，且有经典全局条件**

$$\text{局部数据候选}：\mu_{p-1}\ \text{（局部挠，阶}\ p-1\text{）};\ \text{以及}\ \text{从}\ (a,b)\ \text{与}\ v\ \text{生成的}\ \textbf{局部符号}\ (a,b)_v\ \text{（取值于}\ \mu_N，\textbf{离散}）✓✓$$
$$\qquad\text{gluing law}：\text{经典事实}\ \prod_v(a,b)_v=1\ \text{（Hilbert 互反）};\ \text{等价地，局部类}\ \{\alpha_v\}\ \text{可拼接}\iff \sum_v \mathrm{inv}_v(\alpha_v)=0 ✓$$
$$\qquad\Longrightarrow\ \text{obstruction 的宿主}：\boxed{\bigoplus_v \mathrm{Br}(\mathbb Q_v)\ /\ \mathrm{Br}(\mathbb Q)\ \cong\ \mathbb Q/\mathbb Z}\ \text{（由正合列）}$$
$$\qquad ⚠️\ \text{关键：其}\ N\text{-挠部分}\ \mathrm{Br}(\mathbb Q)[N]\ \text{有限 ⟹ }\textbf{逐 }N\ \text{离散};\ \text{但整体宿主}\ \mathbb Q/\mathbb Z\ \textbf{不是有限群} ⚠️$$
$$\qquad\Longrightarrow\ \text{按判据 ③（}\text{已知 Brauer／character class}\bigr)\ ⟹ \textbf{杀} ✓✓$$

---

## §4 V196-4 离散值域的**来源**（本轮核心；本档已定位）

$$\textbf{来源 (I)：局部挠}\ \mu_{p-1}\subset\mathbb Z_p^\times ✓✓\ ——\ \text{阶}\ p-1\ \textbf{有限}，canonical（Teichmüller）$$
$$\qquad ⭐\ \text{结构事实}：\hat{\mathbb Z}\ \text{的挠子群}\ ＝\ \bigoplus_p\mu_{p-1}\（\textbf{直和}，非积，因有限阶元只有限多分量非平凡）$$
$$\qquad\Longrightarrow\ \textbf{它在 profinite 拓扑中是离散子群} ⟹ \text{这是"}\textbf{连续群中的离散结构}\text{"的现成实例} ✓✓✓$$
$$\qquad ⚠️\ \text{这正是 V196-5 刚性引擎的}\ \textbf{前提条件}，\ \text{且它在算术中}\ \textbf{真实存在} ✓$$
$$\textbf{来源 (II)：符号取值于}\ \mu_N\ \text{与}\ \mathrm{Br}[N]\ \text{（逐 }N\ \text{有限）} ✓$$
$$\qquad ⚠️\ \text{但注意}：\text{来源 (I)(II)}\ \text{的离散性}\ \textbf{都来自"挠／单位根"，}\ \textbf{不来自任何"局部-全局张力"的新结构} ⚠️$$
$$\textbf{来源 (III)（本档新提，待挖）}：\textbf{局部挠与全局挠的落差} —— \text{逐}\ p\ \text{有}\ \mu_{p-1}\（\text{阶}\ p-1\text{）}，\ \text{而}\ \mathbb Q\ \text{只有}\ \mu_2$$
$$\qquad\Longrightarrow\ \text{"局部离散数据不升为全局离散数据"这一}\ \textbf{落差}\ \text{本身}\ \text{是一个}\ \text{canonical}\ \text{现象};\ \text{其障碍类}\ \text{落在}\ \mu\text{-挠／}\mathrm{Br}\ \text{体系中} ✓$$

---

## §5 V196-5 刚性检验（只在 §3–§4 之后）

$$\text{设连续族}\ T_\lambda\（\lambda\in\Lambda\ \text{连通}\bigr）,\ \text{其 obstruction}\ [T_\lambda]\in D,\ D\ \textbf{离散} \Longrightarrow \lambda\mapsto[T_\lambda]\ \textbf{局部常值}$$
$$\qquad\Longrightarrow\ [T_{\lambda_0}]=0\ \text{（某点）}\ \Longrightarrow\ [T_\lambda]=0\ \text{（同支）}✓$$
$$\qquad ⭐\ \text{关键判断}：\text{经典实例（局部符号／挠类）}\ \textbf{确有该性质}：\text{它们对}\ (a,b)\ \text{是}\ \textbf{局部常值}（\text{取值}\ \mu_N，\ \text{离散}）$$
$$\qquad\Longrightarrow\ \boxed{\text{机制 II 的刚性引擎}\ \textbf{在算术中确有实例};\ \text{但实例的类}\ \text{是}\ \textbf{经典类}} ✓✓$$

---

## §6 ⭐ 判据对照（✓ 按唐先生四条逐条）

$$\begin{array}{c|c|c}
\text{支路} & \text{obstruction 实际形式} & \text{判据对照}\\
\hline
\textbf{加法支}（valuations／}\log p\text{） & =0（\text{加法上闭链}；自由格） & ① \text{trivial／恒等式} ⟹ \textbf{杀}\\
\textbf{尺度支 C} & =0（\log p\ \mathbb Q\text{-线性无关 ⟹ 自由}） & ① \textbf{杀}\\
\textbf{$p\leftrightarrow q$ 直接映射 A} & \text{不存在 canonical }T_{p,q} & \text{（\text{非 obstruction 型}）}\ \text{记录为}\ \textbf{canonical 性失败}\\
\textbf{$p\leftrightarrow\infty$ 公共对象 B} & \text{公共宿主可建，但 gluing}＝\text{乘积公式} & ① \textbf{杀}（\text{须算到底，见 §2.2）}\\
\textbf{乘法／符号支} & \mathrm{Br}\ \text{型}，\ N\text{-挠有限}（\text{逐 }N\ \text{离散}） & ③ \text{已知 Brauer／character} ⟹ \textbf{杀}\\
\textbf{来源 (I)(II) 本身} & \mu_{p-1}／\mu_N\ \textbf{离散非平凡} & ④\ \text{形式满足，但}\ \textbf{是经典挠类} ⚠️\\
\end{array}$$
$$\Longrightarrow\ \textbf{本档落点}：\text{四个候选支路}\ \textbf{全部}\ \text{落到 ① 或 ③};\ \text{来源 (I)(II) 满足 ④ 的形式条件但内容为经典} ⟹ \text{按判据}\ \textbf{不构成"新引擎"} ✓✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{严格按唐先生纪律}：\text{本档}\ \textbf{不宣称"机制 II 死"} —— \text{只宣称"}\textbf{canonical 分支}\textbf{落点已被识别}" ✓✓$$

---

## §7 唯一残余与 V197 预登记（**lead，不预判**）

$$\text{本档识别出的}\ \textbf{唯一未被判据覆盖的形状}：\text{需要}\ \text{一个}\ \textbf{离散、非平凡、}\textbf{且非已知挠／}\mathrm{Br}\ \text{类} \text{的 obstruction}$$
$$\qquad ⭐\ \text{最接近的 lead（}\textbf{仅登记，不预判}）：\text{经典 K-理论中的}\ \text{Steinberg 型关系}\ \{a,\ 1-a\}=0\ \text{——}\ \text{其}\ \textbf{配对形状是}\ a\leftrightarrow1-a$$
$$\qquad\qquad ⚠️\ \text{注意}：\text{该形状与}\ \text{某类}\ \text{对合配对}\ \text{同型};\ \text{但}\ \text{其取值}\ \text{仍落在}\ \mu_N／\mathrm{Br}\ \text{体系} ⟹ \text{可能仍属 ③}\ \text{（待算）} ✓$$
$$\textbf{V197 预登记（唯一动作）}：\text{先判}\ \text{Steinberg 型关系的 obstruction}\ \text{是否}\ \text{仍}\ \text{落入}\ \mathrm{Br}[N];\ \text{若落入 ⟹ 该 lead 亦属 ③};\ \text{若否 ⟹ 这是}\ \textbf{第一个}\ \text{不属于 ①②③ 的离散非平凡类} ✓$$

---

## §8 诚实的边界

$$\textbf{(a)}\ \text{本档}\ \textbf{未使用}\ \text{任何被禁符号};\ \text{未调用 F1–F4};\ \text{未投影回四通道} ✓✓$$
$$\textbf{(b)}\ \text{§2.1 的"无 canonical }T_{p,q}"\text{"为}\ \textbf{结构判定}（\text{基于挠阶不同与无自然同态}）;\ \text{非形式定理} ⚠️$$
$$\textbf{(c)}\ \text{§3–§5 中的经典事实（乘积公式／Hilbert 互反／正合列／挠群结构／}\log p\ \text{线性无关）为}\ \textbf{经典 ✓};\ \text{具体形式}\ \textbf{待核原文} ⚠️$$
$$\textbf{(d)}\ \text{§4 来源 (III)（局部挠与全局挠的落差）为}\ \textbf{本档新提};\ \text{其障碍类落点}\ \textbf{未定} ✓$$
$$\textbf{(e)}\ \text{按纪律}：\text{机制 II}\ \textbf{不判死};\ \text{仅登记"canonical 分支落点＝①／③"} ✓$$

```
⚠️ §0 禁令为唐先生逐字 ✓✓；本档全程遵守（不含被禁符号）✓
⚠️ §2.1 "无 canonical T_{p,q}" 为【结构判定 ⚠️】；§2.2 公共对象道路为【本档构造 ✓】
⚠️ §3.1 乘积公式 trivial ⟹ ① 杀；§3.2 Br 型 ⟹ ③ 杀；§6 判据对照为唐先生四条逐条 ✓✓
⚠️ §4 来源 (I) 的"ℤ̂ 挠＝⊕μ_{p−1} 且为离散子群"为本档推导 ✓✓（经典群论）
⚠️ §5 刚性检验指出"引擎在算术中确有实例，但类是经典类" ✓✓
⚠️ §6 明确：本档只宣称"canonical 分支落点已识别"，**不宣称机制 II 死** ✓✓
⚠️ §7 lead（Steinberg 型 a↔1−a）仅登记，**不预判** ✓
⚠️ 未用 RH 等被禁符号 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 五步全部执行 ✓✓；② A 支 canonical 性失败（预定结果）＋发现公共对象道路 ✓✓；
   ③ 两支 obstruction 实际形式已算出（0／Br 型）✓✓；④ 离散性来源已定位（局部挠＋符号）✓✓；
   ⑤ 刚性引擎在算术中确有实例（但类经典）✓✓；⑥ 判据对照逐条 ✓✓；⑦ 唯一残余与 lead ✓
```
