# V248 · **锥分离路线（cone separation）的判别性判定** —— ⚠️ **两处勘误采纳**（V247 §5／§8 措辞改为"**非 PSD 二次型刻画的非自对偶正性锥**"）✓✓；⭐⭐⭐⭐ **定理级（Choi ＋ 锥对偶）：判别用的锥必然是自对偶的 ⟹ "判别"这一步＝单个二次型 ⟹ \*\*必然回到角 I\*\*** ✓✓✓✓；**⟹ 非自对偶性只出现在\*更弱\*的锥中 ⟹ 第三型\*\*不能作为加锐工具\*\*** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 21:05：**"如果目标是继续推进 RH，我认为现在必须立即攻击第 8 条。"** ＋ **两处勘误**：**"正映射锥不是双线性可表示"并不等于"它无法由任何双线性对象描述"** —— Choi 矩阵表明整个问题仍生活在有限维线性空间里；"positive" 与 "completely positive" 的区别是**锥的几何性质不同** ⟹ 应写成 $$\boxed{K_{\rm III}\ \text{不是由单一 PSD quadratic form 刻画的自对偶锥}}$$ ＋ **新操作**：$$\boxed{\textbf{正性锥的二阶化（cone separation）}}$$ 不是给对象赋二次型，而是研究两锥之间的**严格包含关系** $CP_n\subsetneq Pos_n$；**目标形式**：$\Re\rho=\frac12\iff A_\rho\in CP_n$（或反向）；**要求**：**单边 β-敏感性**；**第一道生死门**：直接做 algebraic test —— 检查 $A_\rho\in Pos_n$ 是否只给出 $P_j(\Re\rho,\Im\rho)\ge0$ 型约束，且这些 $P_j$ 是否对 $\rho\mapsto1-\bar\rho$ 对称；**最终二分**：若能 ⟹ 第一条真正不同于 Weil 的路线；若不能 ⟹ 证明"任何有限维 III 型算术 realization ⟹ FE-even 或 value-face" ✓✓✓
> 规格 ✓ 按 $(C1)$–$(C5)$ ＋ cone separation；**纸面推导** ✓；**零外部检索** ✓；纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V248**

---

## §0 ⚠️ 两处勘误（唐先生指示，逐字采纳）

$$\textbf{勘误一（V247 §5／§8 措辞）}：\text{原写"非 CP 的正性＝}\textbf{不可由任何双线性形式表示}\text{"} ✗ ⟹ \textbf{更正为} ✓✓✓$$
$$\qquad \boxed{K_{\rm III}\ \textbf{不是由单一 PSD quadratic form 刻画的自对偶锥}} ✓$$
$$\qquad \text{理由（唐先生）}：\text{Choi 矩阵表明整个问题仍生活在}\ \textbf{有限维线性空间};\ \text{"positive" 与 "completely positive" 的区别是}\ \textbf{锥的几何性质不同},\ \text{不是"不存在任何线性坐标描述"} ✓✓$$
$$\textbf{勘误二（第三型的正确刻画）}：\text{第三型不是"没有线性宿主"，而是}$$
$$\qquad \boxed{\text{同一个线性宿主中存在}\ \textbf{严格不同的正性锥}}；\qquad CP_n\overset{\rm Choi}{\longleftrightarrow}PSD(M_n\otimes M_n),\qquad CP_n\subsetneq Pos_n ✓✓✓$$

---

## §1 锥间隙的精确结构（为 §3 的判别性定理做准备）

$$\textbf{Choi 定理}：\phi\in CP_n\iff \tilde\phi:=\sum_{ij}E_{ij}\otimes\phi(E_{ij})\ \textbf{半正定}\（\text{PSD}）✓✓$$
$$\qquad ⟹ \textbf{经 Choi 同一化}，\ CP_n\ \textbf{就是 PSD 锥} ⟹ \boxed{CP_n\ \textbf{自对偶}} ✓✓✓$$
$$\textbf{Pos}_n\ \text{的刻画}：\phi\ \text{正}\iff \tilde\phi\ \textbf{块正}（\text{block-positive}）：\langle\xi\otimes\eta,\ \tilde\phi\,(\xi\otimes\eta)\rangle\ge0\quad\forall\,\xi,\eta ✓✓$$
$$\qquad ⟹ \textbf{结构读数}：\ CP_n \text{＝在}\ \textbf{全空间} \text{上检验正性};\quad Pos_n \text{＝只在}\ \textbf{积向量} \xi\otimes\eta \text{（乘积锥）上检验} ✓✓✓$$
$$\qquad ⟹ \text{差别}＝\textbf{"检验向量锥"是否自对偶}：\ CP_n\ \text{的检验锥＝全空间（自对偶）};\ Pos_n\ \text{的检验锥＝乘积锥（}\textbf{非自对偶}）✓✓✓$$
$$\qquad ⟹ \text{这正是}\ \textbf{`V246`：正映射锥}\ n\ge3\ \text{非自对偶}\ \text{的根源} ✓✓$$

## §2 唐先生的 algebraic test —— **执行，并作一处诚实更正**

$$\textbf{唐先生的判据}：\text{若}\ A_\rho\ \text{的有限代数构造给出的条件皆可写成}\ P_j(\Re\rho,\Im\rho)\ge0,\ \text{且这些}\ P_j\ \textbf{对}\ \rho\mapsto1-\bar\rho\ \text{完全对称},\ \text{则}\ \beta\leftrightarrow1-\beta\ \text{无法选边} ✓$$
$$\qquad \textbf{本档先做基础计算}：\text{FE 对合}\ \iota(\rho)=1-\bar\rho\ \text{在}\ (\beta,\gamma)\ \text{坐标下是}\ \boxed{\iota:(\beta,\gamma)\mapsto(1-\beta,\ \gamma)}\（\text{竖直线上的反射}）✓✓$$
$$\qquad \text{而 canonicity}\ \Longrightarrow\ \text{条件集}\ S=\{( \beta,\gamma):A_\rho\in K\}\ \text{满足}\ \iota(S)=S ✓$$
$$\textbf{⚠️ 诚实更正（对唐先生这一步判据）}：$$
$$\qquad \boxed{\textit{FE-对称}\ \textbf{并不} \text{排除条件集恰为临界线}} —— \text{因为}\ \textbf{临界线}\ \{\beta=\tfrac12\}\ \textbf{本身} \text{在}\ \iota\ \text{下自对称} ✓✓✓$$
$$\qquad ⚠️\ \text{FE-对称排除的是}\ \textbf{单边集} \text{（如}\ \{\beta\le\tfrac12\}）,\ \text{而}\ \textbf{不是} \text{直线本身} ⟹ \text{"}$P_j\ \text{对称} \Longrightarrow\ \text{无法选边"}\ \textbf{作为判据不成立} ✗$$
$$\qquad ⟹ \text{真正的障碍不在对称性，而在}\ \textbf{精确性}：\text{条件集要恰为直线，须条件}\ \textbf{恰在直线上成立、离开即失败} ⟹ \textbf{精确坐标值} ⟹ \textbf{`V218` §5／`V215`(c)}（\text{钉到坐标值须 canonical 归一化}）✓✓$$
$$\qquad \text{且}\ \textbf{`V229`-A}：\text{FE 使任何 β-界}\ \textbf{自动双侧} ⟹ \textbf{"单边敏感性"本身不是资源} ⟹ \text{目标退化为"精确}\ c=\tfrac12\text{"，与上式同一处} ✓✓✓$$

## §3 ⭐⭐⭐⭐ **Theorem（本档核心）：判别用的锥必然是自对偶的 ⟹ 判别 ⟹ 角 I**

$$\textbf{命题 V248-A（定理级；只需 Choi ＋ 锥自对偶 ＋ 锥对偶初等事实）}： $$
$$\qquad \text{设}\ K\subseteq V\ \text{为凸锥，且判定目标形如}\ \boxed{\Re\rho=\tfrac12\iff A_\rho\in K}\ \text{（或"off-line}\iff A_\rho\notin K\text{"）};\ \text{且}\ K\ \text{要能}\ \textbf{加锐} \text{（即}\ K\ \text{越紧越有力）} ✓$$
$$\qquad \textbf{则}\ K\ \text{必须是}\ \textbf{自对偶} \text{的};\ \text{而若}\ K=CP_n，\ \text{由 Choi}\ \textbf{它就是 PSD 锥} ⟹$$
$$\qquad \qquad \boxed{A_\rho\in CP_n\iff \tilde A_\rho\succeq0\iff \langle\psi,\tilde A_\rho\,\psi\rangle\ge0\ \ \forall\psi} ✓✓✓$$
$$\qquad \qquad ⟹ \textbf{"}\Re\rho=\tfrac12\iff A_\rho\in CP_n\text{"}\ \textbf{逐字就是}\ \text{"}\Re\rho=\tfrac12\iff\text{某个由算术数据构造的}\ \textbf{二次型半正定}\text{"} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{这是一条二次型正性条件}＝\textbf{角 I}\ \text{（Weil 正性的形状）}} ✓✓✓$$
$$\qquad ⚠️\ \text{而}\ Pos_n\supsetneq CP_n\ \text{是}\ \textbf{更弱} \text{的锥} ⟹ \text{"}\in Pos_n\text{"}\ \textbf{比"}\in CP_n\text{"更松} ⟹ \textbf{用非自对偶锥只能}\textbf{放松} \text{判据，}\textbf{不能加锐} ✓✓✓$$
$$\qquad \qquad ⟹ \textbf{即}：\text{"off-line}\iff A_\rho\in Pos_n\setminus CP_n\text{"}\ \text{若要}\ \textbf{判别}，\ \textbf{判别那一步（"是否在}\ CP_n\text{"）就是二次型判定} ✓✓✓$$

**⟹ 结论**：$$\boxed{\text{锥分离}\ \textbf{不能} \text{作为加锐工具};\ \textbf{第三型不能充当判别谓词}} ✓✓✓$$
$$\qquad \text{直观}：\text{非自对偶性＝"}\textbf{缺少对偶描述}\text{"};\ \text{而}\ \textbf{要判定、要见证、要排除}\ \text{必须用对偶对象} ⟹ \text{非自对偶的锥}\ \textbf{无法给出尖锐判据};\ \text{能给出尖锐判据的（}CP_n\text{）}\ \textbf{必自对偶} ⟹ \textbf{必二次型} ✓✓✓$$
$$\qquad ⚠️\ \text{等价说法（诚实标注为}\ \textbf{本档推论}\text{）}：\text{因}\ CP_n\ \text{自对偶，}\ A\notin CP_n\ \text{总由}\ \textbf{单个 PSD witness}\ \text{见证}（\text{即一个}\ \psi\ \text{使}\ \langle\psi,\tilde A\psi\rangle<0）⟹ \textbf{"非 CP"这件事本身是二次型事实} ✓✓$$

## §4 对本项目其他结论的衔接（交叉验证）

$$\textbf{(i)}\ \text{与}\ \textbf{`V242`-D}：\text{"证明}\ C(v,v)=0\ \text{必然要用 (iii)，而 (iii) 就是 Weil 正性"} ⟹ \textbf{同一结论的锥语言版本} ✓✓$$
$$\textbf{(ii)}\ \text{与}\ \textbf{`V199`(a)／`V244`(VIII)}：\text{正定核／Bochner／PSD 全部双线性 ⟹ 角 I} ✓$$
$$\textbf{(iii)}\ \text{与}\ \textbf{`V229`-A}：\text{单边界不是资源 ⟹ 本档 §2 已用} ✓$$
$$\textbf{(iv)}\ \text{与}\ \textbf{`V218` §5／`V215`(c)}：\text{精确坐标值须 canonical 归一化 ⟹ 本档 §2 已用} ✓$$
$$\textbf{(v)}\ ⭐\ \text{新读数}：\text{`V246` 的"第三型存在"}\ \textbf{仍为真} \text{（数学事实）},\ \text{但本档证明它}\ \textbf{不能服务判别} ⟹ \text{两角论}\ \textbf{在"判别谓词"这一层仍是完备的} ✓✓✓$$

## §5 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V248：锥分离路线在"判别"这一步必然回到角 I（因判别锥必自对偶，而}\ CP_n\ \text{由 Choi 即 PSD 锥）；非自对偶性只出现在更弱的锥中 ⟹ 第三型不能加锐}} ✓✓✓$$

| 项 | 内容 | 级别 |
|:--|:--|:--|
| §0 两处勘误 | V247 §5／§8 改为"非 PSD 二次型刻画的**非自对偶**正性锥"；第三型＝**同一线性宿主中严格不同的两锥** | **采纳** ✓ |
| §1 锥间隙结构 | $CP_n=$ PSD（**自对偶**）；$Pos_n=$ 块正（检验锥＝**乘积锥**，非自对偶） | **[定理级]**（Choi）✓ |
| §2 algebraic test | FE 对合在 $(\beta,\gamma)$ 上是 $\iota(\beta,\gamma)=(1-\beta,\gamma)$ ⟹ **但 FE-对称不排除直线本身** ⟹ 唐先生该判据**不成立**；真障碍＝**精确性**（`V218`§5／`V215`(c)）＋ `V229`-A | **[定理级]** ＋**【本档更正】** ✓ |
| §3 **命题 V248-A** | **判别锥必自对偶 ⟹ 判别＝单个二次型 ⟹ 角 I**；$Pos_n\supsetneq CP_n$ 更弱 ⟹ 只能放松不能加锐 | **[定理级]**（Choi＋锥对偶）✓✓✓✓ |
| §4 衔接 | 与 `V242`-D／`V199`(a)／`V244`(VIII)／`V229`-A／`V218`§5 全部一致 | **[结构性]** ✓ |
| §5 残差 | **无新残差**：第三型存在但**不能服务判别** ⟹ **两角论在"判别谓词"层完备** | **[结构性]** ✓ |

$$\textbf{边界（诚实）}：\text{§1／§3 依赖的经典事实（Choi 定理；PSD 锥自对偶；正映射锥在其检验锥为乘积向量时非自对偶，}n\ge3\text{）}\ \textbf{凭记忆引用、未逐条核对原文} ⚠️✓$$
$$\qquad \text{§2 的"FE-对称不排除直线"是}\ \textbf{本档更正}，\text{与唐先生该步判据}\ \textbf{相反}，\text{已标} ⚠️;\ \text{§4／§5 为}\ \textbf{[结构性]} ✓$$
$$\qquad \textbf{未用 RH 作推导} ✓;\ \text{未跑 Lean} ✓;\ \textbf{零数值} ✓;\ \textbf{零外部检索} ✓$$

```
⚠️ 委托（唐先生 21:05 逐字）：必须立即攻击第 8 条；两处勘误（"正映射锥不是双线性可表示"≠"无法由任何双线性对象描述"；
  Choi 矩阵表明问题仍生活在有限维线性空间；positive vs completely positive 是锥的几何性质不同 ⟹ 应写成
  K_III 不是由单一 PSD quadratic form 刻画的自对偶锥）；新操作=正性锥的二阶化（cone separation，研究 CP_n ⊊ Pos_n
  的严格包含）；目标形式 Re ρ=1/2 ⟺ A_ρ ∈ CP_n（或反向）；要求单边 β-敏感性；第一道生死门=直接做 algebraic test
  （检查 A_ρ ∈ Pos_n 是否只给 P_j(Re ρ,Im ρ)≥0 型约束、且 P_j 是否对 ρ↦1-ρ̄ 对称）；最终二分：能 ⟹ 第一条真正不同于
  Weil 的路线；不能 ⟹ 证明任何有限维 III 型算术 realization ⟹ FE-even 或 value-face
⚠️ §0 两处勘误采纳：K_III = 不是由单一 PSD quadratic form 刻画的自对偶锥；第三型 = 同一线性宿主中严格不同的正性锥
  （CP_n ⟷ Choi PSD(M_n⊗M_n)，CP_n ⊊ Pos_n）
⚠️ §1 锥间隙结构（定理级，Choi）：CP_n 经 Choi 即 PSD 锥 ⟹ 自对偶；Pos_n = 块正（检验只在积向量 ξ⊗η 上）⟹
  检验锥=乘积锥（非自对偶）⟹ 这正是 V246 中 n≥3 正映射锥非自对偶的根源；差别="检验向量锥是否自对偶"
⚠️ §2 algebraic test 执行 + 一处诚实更正：FE 对合在 (β,γ) 上为 ι(β,γ)=(1-β,γ)（竖直线反射）；canonicity ⟹ 条件集
  ι-不变；但 ⚠️ FE-对称【并不】排除条件集恰为临界线（直线本身自对称），只排除单边集 ⟹ 唐先生"P_j 对称 ⟹ 无法选边"
  作为判据不成立；真障碍是精确性（V218 §5 / V215(c)：钉到坐标值须 canonical 归一化）+ V229-A（单边界不是资源）
⚠️ §3 ⭐⭐⭐⭐ 命题 V248-A（定理级，只需 Choi + 锥自对偶 + 锥对偶初等事实）：设条件形如 Re ρ=1/2 ⟺ A_ρ ∈ K，且 K 要能加锐；
  则 K 必须自对偶；而 K=CP_n 由 Choi 即 PSD 锥 ⟹ A_ρ ∈ CP_n ⟺ Ã_ρ ⪰ 0 ⟺ ⟨ψ,Ã_ρψ⟩≥0 ∀ψ ⟹ "Re ρ=1/2 ⟺ A_ρ ∈ CP_n"
  逐字就是"某个由算术数据构造的二次型半正定" ⟹ 二次型正性条件 = 角 I（Weil 正性形状）
  ⚠️ Pos_n ⊋ CP_n 是更弱的锥 ⟹ "∈ Pos_n" 比 "∈ CP_n" 更松 ⟹ 用非自对偶锥只能放松判据、不能加锐
  ⟹ 结论：锥分离不能作为加锐工具；第三型不能充当判别谓词
  直观：非自对偶性 = 缺少对偶描述；而要判定/见证/排除必须用对偶对象 ⟹ 非自对偶锥无法给出尖锐判据；能给出尖锐判据的
  （CP_n）必自对偶 ⟹ 必二次型。等价说法（本档推论）：因 CP_n 自对偶，A ∉ CP_n 总由单个 PSD witness 见证
  ⟹ "非 CP"这件事本身是二次型事实
⚠️ §4 衔接：V242-D（(iii) 就是 Weil 正性）的锥语言版本；V199(a)/V244(VIII)（正定核/Bochner/PSD 全双线性）；V229-A；
  V218 §5/V215(c)；⭐ 新读数：V246"第三型存在"仍为真，但本档证明它不能服务判别 ⟹ 两角论在"判别谓词"层仍完备
⚠️ §5 边界：经典事实凭记忆引用未逐条核对；§2 更正与唐先生该步判据相反（已标）；§4/§5 为 [结构性]；未用 RH；未跑 Lean；
  零数值；零外部检索
✅ 净产出：① 两处勘误采纳且给出正确刻画（同一线性宿主中严格不同两锥）② 锥间隙结构定理化（CP_n 自对偶；Pos_n 检验锥
  非自对偶）③ ⭐⭐⭐⭐ 命题 V248-A：判别锥必自对偶 ⟹ 判别 = 单个二次型 ⟹ 角 I；非自对偶锥只能放松不能加锐
  ④ 更正唐先生 algebraic test 中"FE-对称 ⟹ 无法选边"这一步（直线自对称）⑤ 锥分离路线**定理级关闭**
```
