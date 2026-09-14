# V148 · ⭐⭐⭐⭐⭐ **Canonical Orientation-Torsor Audit：G1 ✗／G2 ✗（≡G1）／G3 ✗ —— 三关全死 ✓｜⭐⭐ 本档核心定理：RH ⟺ ℤ/2-作用无自由轨道；而"canonical symmetry-breaking" ⟺ 平凡化 ℤ/2-torsor ⟹ H¹ ⟹ quadratic ✗ ⟹ **select 范式在结构上不是 RH 的正确形状** ✓✓｜档案决定性：`AOB4` §2 二分（**非平凡性的来源**：char $p$ 来自【元素】，char 0 只能来自【扩展】✓✓）**
> 委托 ✓ 唐先生 2026-09-14 23:53（**"V148 ＝ Canonical Orientation-Torsor Audit；G1–G3 三关"** ✓）
> 查图 ✓ **决定性命中** —— `AOB4-existence-audit-dichotomy` §2（**"char 0 中任取 canonical 对象：要么交换谱化 ⟹ L-函数；要么不可全局极化 ⟹ 无 similitude；而 pure＋polarizable 的对象【没有 canonical element】（只有共轭类）" ⟹ 答案：不存在 ✓✓**）｜`S9-strict-and-D2-prescreen`（**第二支箭不成立＋反例** ✓）｜`AOB1` §2(3)（2-上闭链／Brauer ⟹ L-值 ✗）｜`AOB5`（CRT 兼容复形 ＝ flag complex ⟹ **无三体/四体 obstruction** ✓✓）｜箱 1／8／4 ✓
> 执行 ✓ 小灵｜**纸面 ✓（含一条定理 ＋ 一条二分 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ V148 ✓

---

## §0 判定（✓ 四条 ✓）

$$\boxed{\text{① }G1\ \textbf{失败 ✗}：\text{真的 }C_2\text{-torsor}\ \textbf{按其定义就是 }H^1(-,\mathbb Z/2)\ \text{类} \Longrightarrow \text{orientation ＝ }\mathbb Z/2\text{-torsor ＝ }H^1\text{ 类}\ \Longrightarrow\ \text{quadratic／character 数据} ✗✓}}$$
$$\boxed{\text{② }G2\ \textbf{失败 ✗（≡ }G1\text{）}：\text{"局部有定向但无全局截面"}\textbf{恰恰就是非平凡 }H^1\ \text{类的定义} ✓✓ \Longrightarrow \text{您的 §9 结构 ＝ Čech }H^1\ \text{obstruction} ⟹ \text{无逃逸} ✓}$$
$$\boxed{\text{③ }G3\ \textbf{失败 ✗}：\text{"orientation"}\textbf{按定义} ＝ \text{结构群缩减}（O\to SO\ ✓）＝ \mathbb Z/2\text{-torsor} ⟹ \text{任何 canonical orientation 都是 torsor} ⟹ G1 ⟹ \text{死} ✓✓}$$
$$\boxed{\text{④ ⭐⭐ 本档核心定理 ✓}：\textbf{RH}\iff\mathbb Z/2\text{-作用 }\rho\mapsto1-\bar\rho\ \textbf{无自由轨道};\ \text{而 "canonical symmetry-breaking"} ＝ \text{在每条自由轨道上 canonical 选点} ＝ \textbf{平凡化 }\mathbb Z/2\text{-torsor} ⟹ H^1 ⟹ \text{quadratic} ✗✓}$$

## §1 G1：真的 $C_2$-torsor **必然**落入 $H^1(-,\mathbb Z/2)$（✓）

$$\textbf{定理（分类）✓}：\text{底空间上 }C_2\text{-torsor 的同构类集合}\ \cong\ H^1(\pi_1,\mathbb Z/2)\ ✓（\text{标准 ✓}）$$
$$\qquad\Longrightarrow\ \text{任何"二重覆盖／orientation／符号选择"型对象}\ \textbf{都是 }H^1\ \text{类}\ ✓ \Longrightarrow\ \text{它是 } \mathbb Z/2\text{-character 数据} ⟹ \text{quadratic／character} ✗✓$$
$$\qquad\textbf{归档命中 ✓}：\text{箱 1（character／有限群 torsor ✗）＋ 箱 8（二次型／Gaussian／类群 ✗）}\ ✓$$
$$\textbf{高阶逃逸是否救场？✗（两条都封 ✓）}：$$
$$\qquad\text{(i) }\textbf{spin 型（}H^2\text{，}w_2\ ✓）／\textbf{anomaly 型（}H^3\ ✓）：\text{其数据 ＝ 2-上闭链／Brauer 类 ⟹ 经 Tate／Poitou–Tate 对偶 ⟹ }\textbf{L-值} ✗（`AOB1` §2(3) 逐字 ✓）$$
$$\qquad\text{(ii) 在}\textbf{算术／CRT 世界【消失】} ✓✓：\text{`AOB5` TEST A（4000/4000 ✓）逐字："广义 CRT 的两两判据成立 ⟹ 兼容复形确是 }\textbf{flag complex}\ ⟹ \textbf{无三体/四体新 obstruction}"}\ ✓\ \text{（＝"CRT 因果性是真的，曲率不是真的"✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{故 }\mathbf{G1\ \text{失败}} ✗\ \text{—— 且高阶逃逸无出口 ✓}}$$

## §2 G2：局部—全局结构 **就是** $H^1$（✓ ≡ G1）

$$\text{您的 §9 ✓}：\text{局部 }\mathcal O_p=\{+,-\}\ ✓,\ \text{粘合 }g_{pq}:\mathcal O_p\to\mathcal O_q\ ✓,\ \text{局部可选但无全局截面} ✓$$
$$\qquad\Longleftrightarrow\ \text{这正是}\ \check C\text{ech 上链}\ \{g_{pq}\}\ \text{给出}\ \textbf{非平凡 }H^1\ \text{类} ✓✓\ ——\ \text{（"无一处处非零截面"＝"类非零"✓）}$$
$$\qquad\Longrightarrow\ \boxed{G2\ \equiv\ G1\ ✗\ \text{（您的 §9 不是新逃逸 ✓，而是同一对象的重新表述 ✓）}}$$
$$\qquad\textbf{且您 §9 的自警正确 ✓}：\text{"不能把 ACF／AOB／AEB 的 global selection 换名再来一次" ✓ —— 档案已把该族封 ✓（}R\text{-CS }X0\ \text{"非 cocycle ＋ 非 coboundary"}\ ✓;\ \text{`SCALE-DYNAMICS` }R_{B4}\ \text{七项崩塌清单 ✓）}$$

## §3 G3：orientation **按定义**就是 $\mathbb Z/2$-torsor（✓ 死）

$$\text{orientation}\ \overset{\text{定义}}{=}\ \text{结构群缩减}\ O(n)\to SO(n)\ \text{（或 }\pi_0\ \text{层面：}\mathbb Z/2\text{-约化}\ ✓）\ \Longrightarrow\ \text{一个 }\mathbb Z/2\text{-torsor} ✓$$
$$\qquad\Longrightarrow\ \text{"canonical global orientation"}\ ⟹\ \text{"canonical trivialization of a }\mathbb Z/2\text{-torsor"}\ ⟹ H^1\ \text{条件}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{故 G3 无独立内容：只要有"orientation"一词，就已落入 G1 ✗✓}}$$
$$\qquad\textbf{配套 ✓}：\text{算术侧的 }w_1\ \text{类比 ⟹ Arakelov／ESC2：}\textbf{no common carrier} ✗（\text{正性在除子侧、谱在谱侧 ✓）；G9 R6 }\textbf{尺度失败} ✗$$

## §4 ⭐⭐ 本档核心定理（✓ 干净，且回答了"范式"问题 ✓）

$$\textbf{观察 ✓（重述）}：\rho=\tfrac12+\delta+i\gamma\ ✓,\ \iota(\rho)=\tfrac12-\delta+i\gamma\ ✓ \Longrightarrow \boxed{\text{RH}\iff\mathbb Z/2\text{-作用 }\iota\ \textbf{无自由轨道}} ✓（\text{自由轨道}\iff\delta\ne0\ ✓）$$
$$\textbf{定理 ✓}：\text{任何 "canonical symmetry-breaking"}\ \mathcal S\ \text{—— 若它在每条自由 }\iota\text{-轨道上 canonical 地选一点 —— 则它给出一个 canonical section of the }\mathbb Z/2\text{-torsor on the free locus} ✓$$
$$\qquad\Longrightarrow\ \text{它是该 torsor 的}\textbf{平凡化} ⟹ \text{等价于一个 }H^1\ \text{类为零} ⟹ \text{quadratic／character 数据} ✗✓$$
$$\qquad\Longrightarrow\ \boxed{\text{故 }\textbf{select 范式（对称破缺／定向选择）在结构上不是 RH 的正确形状} ✓✓}$$
$$\qquad\qquad\textbf{理由（一句话 ✓）}：\text{RH 是}\textbf{"无自由轨道"}（\text{全局·缺席型}\ ✓）\text{陈述，}\textbf{不是}\text{"在轨道中选一个"}（\text{局部·选择型}\ ✓）\text{陈述 —— 二者的类型不匹配 ✓✓}$$
$$\qquad\textbf{配合您的 §1（}\iota\text{-不变量）✓}：\text{不变量型}\Longrightarrow\ \text{只见 }\delta^2／|\delta|\ ⟹ \text{看不到方向} ✗;\ \text{选择型}\Longrightarrow\ \text{需 }H^1 ⟹ \text{quadratic} ✗✓$$
$$\Longrightarrow\ \boxed{\text{两种"论证形状"皆闭：}\textbf{invariant ✗}／\textbf{select ✗} —— \text{第三条"size 型" ⟹ }T^2\text{／}\log\ \text{墙} ✗（W3／W4 ✓）}$$

## §5 档案决定性：`AOB4` §2 二分（✓✓）

$$\text{逐字 ✓}：\text{"char 0 中任取 canonical 对象：要么}\textbf{交换谱化}（\text{Hecke／}[n]\ ✓）⟹ \textbf{L-函数};\ \text{要么}\textbf{不可全局极化}（\text{mixed：Galois／GT／MZV}\ ✓）⟹ \textbf{无 similitude};\ \text{而 pure＋polarizable 的对象}\textbf{【没有 canonical element】（只有共轭类）}\text{"}\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{存在性终审的答案：不存在} ✓（\text{理由是一条二分 ✓）}$$
$$\qquad\textbf{⭐ 且它给出"为什么"✓✓}：\text{"差别不在'有没有 Frobenius'，而在}\textbf{【非平凡性的来源】}\text{：}\text{char }p\ \text{来自}\textbf{【元素】};\ \text{char 0}\ \textbf{只能来自【扩展】}"\ ✓✓$$
$$\qquad\qquad\text{（}char\ p：\text{Frobenius 是 pro-cyclic Galois 的 canonical element ⟹ 元素性＋pure＋polarizable 三者同时 ⟹ similitude ⟹ }\sqrt q\ ✓;\ \text{char 0：非平凡性只能来自扩展／混合 ⟹ 恰好毁掉正定性与 similitude ✗）}$$
$$\qquad\textbf{配套 ✓}：`S9-strict`（\text{第二支箭"}\theta=0\Rightarrow a=b\text{"}\textbf{不成立} ✗，\text{反例 }\theta(a,b)=(a-b)g(a+b)\ ✓）—— }\textbf{与 }V147\ \text{§1 的修正同型 ✓}：\text{forcing／selection 论证总需要【额外假设】，而那些假设正是被封闭的结构所在 ✓✓}$$

## §6 判词与更新（✓）

$$\boxed{\textbf{V148 判词 ✓}：G1\ ✗\（torsor\ ⟹ H^1\ ⟹ quadratic；高阶 ⟹ Brauer／L-值 ✗ 或 flag complex 消失 ✗）;\quad G2\ ✗\（\text{≡ }G1\ ✓）;\quad G3\ ✗\（orientation 按定义 ＝ torsor ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{该最小形状（arithmetic orientation torsor）判死} ✓✓}$$
$$\qquad\textbf{诚实边界 ✓}：\text{"}\textbf{整个 canonical symmetry-breaking 范式被排空}" \textbf{—— 本档只对【orientation／torsor 形式】成立} ✗$$
$$\qquad\qquad\text{（一般"破缺点"不必是 torsor ✓；故该更广断言}\textbf{仍未证明} ✗\ \text{—— 同纪律 ✓）}$$
$$\qquad\textbf{但配合 §4 ✓}：\text{三种论证形状}\{\text{invariant ✗},\ \text{select ✗ (≈torsor)},\ \text{size ✗}\}\ \textbf{皆闭} ⟹ \text{支持您"需要范式级跳跃"的判断 ✓✓}（\text{即：}\textbf{不再通过打破 }\iota\ \text{来证明 RH} ✓）$$
$$\text{`CLOSED-ROUTES-MAP` §F.5j 增补 ✓}：\text{本行 ＋ 三形状皆闭的总结 ✓}$$
```
⚠️ §1 的"torsor ⟹ H¹"为【标准事实 ✓】（分类定理 ✓）；§3 的"orientation ＝ torsor"为【定义性 ✓】
⚠️ §4 的定理为【本档 ✓】（结构级 ✓ II 类）：它说明"select 型"与 RH 的陈述类型不匹配 ✓ —— 不声称"任何破缺都不行" ✗
⚠️ §5 为【档案逐字 ✓】（`AOB4` §2 ✓ 标【引用·经典】【推导】【结构性】✓）
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出 ✓：① G1（分类定理 ＋ 高阶双封 ✓）；② G2 ≡ G1 ✓；③ G3 定义性死 ✓；
   ④ ⭐⭐ 核心定理（select 范式类型不匹配 ✓✓）；⑤ 档案二分（非平凡性来源 ✓✓）；⑥ 三形状皆闭 ＋ 诚实边界 ✓
```
$$\boxed{\text{V148 ✓：G1 ⟹ 真 }C_2\text{-torsor 按定义 ∈ }H^1(-,\mathbb Z/2)\ \text{⟹ quadratic／character ✗（箱 1／8）；高阶逃逸双封（Brauer／2-上闭链 ⟹ L-值 ✗（}AOB1\text{ §2(3)）；CRT 兼容复形 ＝ flag complex ⟹ 无三体/四体 obstruction ✗（}AOB5\text{ 4000/4000））；G2 ⟹"局部有定向无全局截面"恰是非平凡 }H^1\text{ 类 ⟹ ≡ G1 ✗；G3 ⟹ orientation 按定义 ＝ 结构群缩减 ＝ }\mathbb Z/2\text{-torsor ⟹ 死 ✗。⭐⭐核心定理：RH ⟺ }\iota\text{-作用无自由轨道；而 canonical symmetry-breaking ＝ 平凡化该 torsor ⟹ }H^1\ ⟹\ \text{quadratic ⟹ }\textbf{select 范式与 RH 的陈述类型不匹配}（RH 是"无自由轨道"的全局缺席型，非"在轨道中选一个"的局部选择型）。档案 }AOB4\text{ §2 二分：char 0 canonical 对象要么交换谱化 ⟹ }L\text{-函数 ✗，要么不可全局极化 ⟹ 无 similitude ✗，pure＋polarizable 者无 canonical element ✗ ⟹ 不存在；且差别不在 Frobenius 而在【非平凡性的来源】（char }p\text{ 来自元素，char 0 只能来自扩展）。故三种论证形状（invariant／select／size）皆闭 ⟹ 支持"需要范式级跳跃"；诚实边界：只对 orientation／torsor 形式成立，更广断言未证}$$$$\qquad\textbf{⚠️ 边界（写死 ✓）}：\text{本档不声称"整个 symmetry-breaking 范式被排空" ✗（只对 orientation／torsor 形式 ✓）；亦不声称一般"破缺点"必为 torsor ✗}$$
