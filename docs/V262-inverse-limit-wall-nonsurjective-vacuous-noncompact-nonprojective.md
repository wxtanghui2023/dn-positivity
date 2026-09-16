# V262 · **逆极限墙：「非满射」为空 ＋「紧致」不逃逸 ⟹ 四逃逸口收缩为两类（非紧致 ｜ 非投射）** —— ⭐⭐⭐⭐ **定理 V262-A（本档，可证、初等）**：$$\boxed{\text{有限非空 }X_n+\textbf{任意}\ \pi_n\ \Longrightarrow\ \varprojlim X_n\ne\varnothing}$$（**唐稿的"满射"条件可删** ✓✓）；⭐⭐⭐⭐ **定理 V262-B（紧致层，标准工具）**：$$\boxed{\text{紧致非空 }X_n+\textbf{任意连续}\ \pi_n\ \Longrightarrow\ \varprojlim X_n\ne\varnothing}$$；⭐⭐⭐⭐ **定理 V262-C′（有限见证，本档最锋利）**：$$\boxed{\text{紧致情形：}\ \varprojlim X_n=\varnothing\ \Longleftrightarrow\ \exists N:\ X_N=\varnothing}$$⟹ **紧致系统不存在"无限层才失败"的障碍**（唐稿"突然不兼容"直觉**被排除** ✗）；⭐⭐⭐⭐ **推论 V262-D（分类收缩）**：唐稿四逃逸口 $\{A\ \text{无限状态},B\ \text{非紧致},C\ \text{非满射},D\ \text{非有限谓词}\}$ ⟹ $A\cup C$ **并入 $B$** ⟹ **只剩两类**：$$\boxed{\text{非紧致}\ \mid\ \text{非投射（非有限判别）}}$$；⭐⭐⭐ **推论 V262-E（判据恒真 ⟹ 无选择力）**：$\mathfrak C:=$"$\varprojlim\ne\varnothing$" 在**任何**有限／紧致非空系统上**恒为 1、与局部数据无关** ⟹ **该形状不可作 RH 判据**（比唐稿担心的"人为编码"更强）；⭐⭐ **与 `V259`-A 互补**：`V259`-A ＝「**有限读**」墙（数据 ⟹ 判定）｜`V262` ＝「**紧装**」墙（约束 ⟹ 解存在）⟹ 逃逸必须**同时**非有限读、非紧装 ⟹ 形状 ＝ **非紧致 ＋ 非投射 ＋ RH-独立** ✓；⚠️ **不声称**：① **非**完整性定理（§E.4 仍开 ✗）；② **非**新数学（A／B 为标准事实的**转用与推论** ✓）；③ 收缩**以"兼容性 ＝ 逐层投射系统中的解存在"这一形式化为条件** ⚠️

> 委托 ✓ 唐先生 2026-09-16 09:21（`V260` 反向审计稿，全文逐节）＋ 本会话的**编号处置**（§0）✓
> 依据 ✓ `V259`（Horn 1／选择律审计／残余＝非聚合组合律）｜`V258`｜`V210`／`V215`／`V218`｜`V147`｜`V193`–`V198` ✓

---

## §0 ⚙️ 编号与来源处置（**先办的三件事**）

```
① 唐稿自标 `V260` ✓ —— 但 `V260`／`V261` **已被同夜"极坐标／应力张量路线"占用** ✓
   ⟹ 按 `ID-ALLOCATION-PROTOCOL` §3（撞车 ⟹ **后到者改号** ✓）登记为 **`V262`** ✓
② 台账痕迹（**关键**）✓：`docs/.idclaims/V262.lock`（2026-09-15 23:08:16）＋ `docs/ID-CLAIMS.tsv` 行 205
   （同刻，slug 含 `inverse-limit-wall-nonsurjective-noncompact-nonfinite-audit`）
   ⟹ **昨夜已领号，但 doc 从未落盘**（会话丢失 ✗，与 `b8efddde…` 同一教训）
   ⟹ 本档**执行该占位** ✓；`V263` 记入 `ID-ALIASES` 作别名 ✓
③ ⚠️ **唐稿第一段（"撤掉 V259-A 的过强解释"）已在本档案 `V259` §3 逐字存在** ✓：
   `V259` §3 明写「**V259-A 不能推出原始 Horn 1**（"纯局部／因子化机制不能产生 off-line collision"）」✓
   ⟹ 本档将其标为 **重复发现** ✓（锚页纪律 ①「先查先行者，再称新」／⑤「自曝重发现」）
   ⟹ **唐稿的净新内容 ＝ 兼容性形式化 ＋ 四逃逸口 ＋ independence gate**（§1–§5）✓，不重复计分 ✓
```

---

## §1 📋 唐稿要点（登记，不重复推导）

```
【唐稿 1】$F_\sigma\ne\zeta$ ⟹ `V259-A` 严格证明的是"有限局部数据不能在整个**对象类**上决定 off-line 性质"，
   **不是**"不能决定 $\zeta$ 本身" ⟹ 若 admissible class 受"必须是 $\zeta$"的**全局定义约束**，
   $F_\sigma$ 不入类 ⟹ **`V259-A` 不能单独证明 Horn 1** ✓ ——（＝ `V259` §3 已有 ✓，重复发现）
【唐稿 2】真正的问题 ⟹ $\mathfrak C(\mathcal A_\zeta)=1\iff RH$ 的 $\mathfrak C$ 是否只是**聚合泛函**
【唐稿 3 兼容性形式化】$X_n\xrightarrow{\pi_n}X_{n-1}$（第 $n$ 层允许状态），真全局状态 $X_\infty=\varprojlim X_n$，
   "$X_\infty\ne\varnothing$" ＝ 无限兼容 ✓
【唐稿 4 两刀】① 有限非空 ＋ **满射** ⟹ $X_\infty\ne\varnothing$（一行递归）✓
   ② 非满射 ⟹ $Y_{n-1}:=X_{n-1}\setminus\pi_n(X_n)$ ＝ 第 $n$ 层首次被淘汰状态 ⟹ 障碍可追到有限阶段的
   **extension obstruction**；若 $Y_{n-1}$ 由有限局部数据描述 ⟹ 又被 `V259-A` 捕获 ⟹ 真逃逸必须"**每层可延拓但无限失败**"
   ⟹ 而紧致有限离散 ＋ Kőnig 型论证又杀掉它 ✓
【唐稿 5 四逃逸口】要产生真 global compatibility failure，至少须放弃下列之一：
   A 有限状态｜B 紧致性｜C 满射延拓｜D 有限阶段可验证性 ✓
【唐稿 6 ⭐ independence gate（唐先生自加）】兼容性关系**本身**必须独立于 RH／零点定义 ✓
   理由：否则可人为定义 $X_n=\{0\}$（若第 $n$ 个 RH 检验未失败）／$\varnothing$，**能编码 RH 但不产生新数学** ✓✓
【唐稿 7 行动建议】先打 **non-surjective**：若"任何满足 G1–G3 的 canonical 非满射算术兼容性必然产生已有
   上同调障碍" ⟹ `V258` 墙从"经验归档"升级为**结构性封口** ✓；否则找出**非上同调的 canonical non-surjective bonding map** ✓
```

---

## §2 ⭐⭐⭐⭐ **定理 V262-A（有限层：满射条件可删）**

$$\textbf{设}\ X_n\ (n\ge1)\ \text{为非空}\ \textbf{有限}\ \text{集，}\ \pi_n:X_n\to X_{n-1}\ \text{为}\ \textbf{任意}\ \text{映射（\textbf{不要求满射}}）✓\qquad\text{则}\ \boxed{\varprojlim X_n\ne\varnothing} ✓✓$$

**证明**（有限 Mittag-Leffler／降链稳定，两行）：

```
① 固定 $n$，令 $I_{m,n}:=\pi_{m\to n}(X_m)\subseteq X_n$（$m\ge n$）✓
   $I_{m+1,n}\subseteq I_{m,n}$ ⟹ **递减非空有限集链** ⟹ **稳定**：$\exists M(n)$，$m\ge M(n)$ 时 $I_{m,n}=:Z_n\ne\varnothing$ ✓
② 断言 $\pi_{n+1\to n}(Z_{n+1})=Z_n$ ✓：取 $m\ge\max\{M(n),M(n+1)\}$，任 $z\in Z_n=I_{m,n}$
   ⟹ $z=\pi_{m\to n}(x)=\pi_{n+1\to n}\big(\pi_{m\to n+1}(x)\big)$ 且 $\pi_{m\to n+1}(x)\in I_{m,n+1}=Z_{n+1}$ ⟹ 满射 ✓
③ $Z_n$ 非空有限 ＋ $\pi_{n+1\to n}:Z_{n+1}\twoheadrightarrow Z_n$ ⟹ 取 $z_1\in Z_1$ 逐层提升 ⟹ $\varprojlim Z_n\ne\varnothing$
   ⟹ $\varprojlim X_n\ne\varnothing$ ∎
```

$$\Longrightarrow\ \boxed{\text{唐稿 §4① 的"满射 ⟹ 非空"}\ \textbf{是真命题，但满射条件多余} ✓}\qquad\Longrightarrow\ \boxed{\textbf{非满射本身从不制造空极限}\ \text{（有限层）}} ✓✓✓$$

$$\textbf{对照（唐稿 §4② 的修正）}：Y_{n-1}=X_{n-1}\setminus\pi_n(X_n)\ne\varnothing\ \text{只说明"该层有被淘汰状态"，}\ \textbf{不说明极限为空} ✓$$
$$\qquad \text{极限仍非空 —— 解只是被迫走}\ \pi_n(X_n)\ \text{这一支 ✓ ⟹ \textbf{"非满射 ＝ 全球障碍源"为假} ✗✗\ \text{（有限层；紧致层见 §3）}}$$

---

## §3 ⭐⭐⭐⭐ **定理 V262-B（紧致层：有限性可删）＋ 定理 V262-C′（有限见证）**

$$\textbf{设}\ X_n\ \text{为非空}\ \textbf{紧致 Hausdorff}\ \text{空间，}\ \pi_n\ \text{连续（\textbf{不要求满射}）}\qquad\text{则}\ \boxed{\varprojlim X_n\ne\varnothing} ✓✓$$

**证明**（Tychonoff ＋ 闭集 FIP，三行）：$\varprojlim X_n=\bigcap_n C_n$，其中 $C_n:=\{x\in\prod_m X_m:\pi_n(x_n)=x_{n-1}\}$ **闭** ✓；$\prod_m X_m$ **紧**（Tychonoff）✓；**有限交非空**：给定 $n_1<\dots<n_k$，令 $N:=n_k$，任取 $x_N\in X_N$，向下推 $x_j:=\pi_{j+1\to j}(x_{j+1})$（$j<N$）、$j>N$ 任取 ⟹ 所有 $j\le N$ 的相容条件满足（含全部 $n_i$）⟹ 有限交集非空 ✓ ⟹ 紧空间中闭集族具 FIP ⟹ 全交非空 ∎

$$\textbf{定理 V262-C′（本档最锋利）}：\text{紧致情形}\qquad \boxed{\varprojlim X_n=\varnothing\ \Longleftrightarrow\ \exists N:\ X_N=\varnothing} ✓✓✓✓$$
$$\qquad（\text{⇐ 显然；⇒ 为 V262-B 的逆否}）\ \Longrightarrow\ \boxed{\textbf{紧致系统里，空极限必有"有限见证层"}\ N\ \text{—— 不存在"每层都非空、却在无限处突然失败"}} ✓✓✓✓$$
$$\qquad \Longrightarrow\ \text{唐稿 §4②／§契 "突然不兼容"的机制}\ \textbf{在紧致情形是不可能事件} ✗✗$$

$$\textbf{同时杀掉唐稿逃逸口 A 的独立性}：\text{无限状态若不紧致（如}\ \mathbb R,\mathbb Q,\ \text{archimedean growth}\text{）才可能失败；}\ \textbf{紧致的无限状态不逃逸} ✓$$
$$\qquad（\text{例：profinite／}\mathbb Z_p\ \text{型状态空间}\ \varprojlim\ne\varnothing\ \text{自动} ✓）$$

---

## §4 ⭐⭐⭐⭐ **推论 V262-D：四逃逸口收缩为两类**

$$\boxed{A\ \text{无限状态}\ \Longrightarrow\ \text{仅在}\ \textbf{非紧致}\ \text{时起作用}\ \Longrightarrow\ A\subseteq B}\qquad\boxed{C\ \text{非满射}\ \Longrightarrow\ \text{有限层为空（§2）／紧致层也不逃逸（§3）}\ \Longrightarrow\ C\subseteq B} ✓✓$$

$$\Longrightarrow\ \boxed{\text{真障碍形状只剩两类：}\quad \textbf{非紧致}\ \mid\ \textbf{非投射（非有限判别）}} ✓✓✓✓$$

$$\textbf{② 类降为 ① 的机制（一句话）}：\text{非满射要"生效"，必须让像链}\ I_{m,n}\ \textbf{不稳定} \Longleftrightarrow \text{无降链条件／无有限性}$$
$$\qquad \Longrightarrow\ \text{那已经不是"有限／紧致阶段系统"}\ \Longrightarrow\ \text{或落非紧致（}B\text{），或落 } \lim^1\ne0\ \text{（非 ML）}$$
$$\qquad ⭐\ \text{而}\ \lim^1\ne0\ \text{正是上同调家族（Brauer／Selmer／Ш／class group）} \Longrightarrow\ \textbf{恰被 } G3\ \text{捕获} ✓✓\ \text{（唐稿 §4C 的判断正确，但"先打 non-surjective"应\textbf{改向} —— 该臂已空 ✗）}$$

$$\textbf{③ 第三种可能（唐稿未单列，本档补）}：\text{约束}\ \textbf{不是逐层投射（non-projective）} —— \text{如"全体素数同时满足}\Psi\text{"型条件} ✓$$
$$\qquad \text{则}\ \text{既不适用 §2（无有限层）也不适用 §3（无 }\varprojlim\text{ 结构）}\ \Longrightarrow\ \text{这正是唐稿逃逸口 } D ✓$$
$$\qquad \Longrightarrow\ \boxed{\text{最终归约}：\text{障碍}\ \Longleftrightarrow\ \text{非紧致}\ \text{或}\ \text{非投射}} ✓✓\ \Longrightarrow\ \text{唐稿"四层墙"图可改为\textbf{二层}: 有限读 ⊥ 紧装 ⊥ (非紧致 ｜ 非投射)}$$

---

## §5 ⭐⭐⭐ **推论 V262-E：存在性型判据恒真 ⟹ 无选择力**

$$\text{若}\ \mathfrak C:=\text{"}\varprojlim X_n\ne\varnothing\text{"}，\ \text{则对}\ \textbf{任何}\ \text{有限或紧致非空系统：}\qquad \boxed{\mathfrak C\equiv 1\ \text{（恒真，且与局部数据}\ \mathcal A\ \textbf{无关}）} ✓✓✓$$

$$\Longrightarrow\ \text{它}\ \textbf{不可能}\ \text{是 RH 的等价判据（RH 要求真值随对象变化）}\ ✗\ \Longrightarrow\ \boxed{\text{"存在无限兼容路径"这一形状\textbf{自动失效}} ✓✓}$$

$$\textbf{⭐ 唐稿 §危险处应升级为定理级}：\text{唐稿担心的是"可人为编码 RH（}X_n=\{0\}/\varnothing\text{）"这类风险；}$$
$$\qquad \textbf{更强的事实}：\text{在自然（紧）情形下}\ \mathfrak C\ \text{不依赖数据 —— 连"编码"的机会都没有} ✓✓$$
$$\qquad ⚠️ \text{且唐稿的编码例本身归 } D：\text{其}\ X_n\ \text{的定义引用 RH／零点 ⟹ \textbf{非局部、非投射}} ⟹ \text{它恰好示范"障碍只能靠非投射活着" ✓}$$

---

## §6 ⭐⭐ **与 `V259`-A 的关系：两面墙，方向不同，不矛盾**

$$\boxed{\textbf{`V259`-A ＝「有限读」墙}}\quad\text{数据}\ \mathcal L_{P,N}\Longrightarrow\text{判定}\ C_{P,N}\quad（\text{关于}\ \textbf{读}\text{：有限窗口看不全}）✓$$
$$\boxed{\textbf{`V262`-A/B/C′ ＝「紧装」墙}}\quad\text{约束}\ \{X_n,\pi_n\}\Longrightarrow\exists\ \text{全局解}\quad（\text{关于}\ \textbf{装}\text{：紧致系统必能装}）✓$$
$$\Longrightarrow\ \text{二者}\ \textbf{不矛盾且互补} ✓\ \text{（作用对象不同：}\mathcal L\text{-数据／}\varprojlim\text{-约束}）\ \Longrightarrow\ \boxed{\text{逃逸必须}\ \textbf{同时}\ \text{不是有限读、不是紧装}} ✓✓$$
$$\qquad \Longrightarrow\ \text{逃逸形状}\ =\ \textbf{非有限、非紧致、且 RH-独立的谓词／约束} ✓✓\ \text{—— 这是 `V259` §6"残余最锐形式"的\textbf{结构侧}对应物} ✓$$

---

## §7 📌 与既有地图对齐（**B 臂不是处女地**）

```
【B 臂 ＝ archimedean／order／size／normalization 通道】✓ 已被映射：
   `V210`（竞争性极限选择：Szpilrajn「唯一 admissible boundary ⟺ 全序」＋ T2 ⟹ 全序分支＝大小序 ⟹ DEAD ✓）
   `V215`（独立对象携带 $\beta$ 的"最小结构"R1–R4；**$\beta$ 携带目标三型**（零点统计／特殊值与周期／archimedean 完成化）**全封** ✓）
   `V218`（$\tfrac12$ 源三型 S1／S2／S3 皆 canonical ⟹ H0 字面为假 ⟹ "自对偶轴 ⟺ RH" ✓）
   ⟹ **B 臂上的"竞争性／序／大小"候选已逐类关闭** ✓ 但**不是**"B 臂全封" ✗（那是未证断言）
【C 臂"活化版"＝ $\lim^1\ne0$／上同调】⟹ G3 ✓：`V193`–`V198`／`V241` 家族 ✓
【与 `V259` §5 G1–G3 的一致性】✓：本档把 G1（"不是有限阶段可见"）**从假设升级为结构结论** ✓：
   有限阶段不可见的**唯一**两条活路 ＝ 非紧致 ｜ 非投射 ✓✓
【§E.4 关系】⚠️ 本档是**覆盖力增加**（四类 ⟹ 两类），**不是**完整性定理 ✗ —— "类表是否完整"仍开 ✓
```

---

## §8 ⚠️ 边界（本档不声称什么）

```
① V262-A／B **不是新定理** ✓ —— 有限 Mittag-Leffler／紧致 FIP 均为标准事实；本档是**转用 ＋ 推论** ✓
② 收缩（§4）**以形式化为条件** ⚠️：须"兼容性 ＝ 逐层投射系统（$X_n\xrightarrow{\pi_n}X_{n-1}$）的解存在" ✓
   若"兼容性"的定义本身不是投射系统 ⟹ 直接落 $D$ ✓（§4③）—— 结论不变，路径不同 ✓
③ §3 的 FIP 论证要求 $X_n$ **非空**（否则 $X_N=\varnothing$ 平凡致空）＋ Hausdorff／紧 ✓
④ §2 只对**有限**集成立；对无限非紧状态（$\mathbb R$ 等）**不适用** ✓ ⟹ §4 的 "A ⊆ B" 是就"逃逸能力"而言 ✓
⑤ §7 的对齐是**指针级**（未重读 `V215`／`V218` 全文 ⚠️）⟹ 不得当作"B 臂已封"的依据 ✗
⑥ 未用 RH ✓；未跑 Lean ✓；零数值 ✓；§4／§5 的"收缩／恒真"为 [结构性] 论证 ✓
```

---

## §9 ✅ 净产出 ＋ 下一步（唯一有内容的两个攻击面）

$$\boxed{①\ \text{逃逸口}\ C\ \textbf{（非满射）已被一行清空}} ✓\ \text{—— 唐稿"先打 non-surjective"应}\ \textbf{改向} ✗✓$$
$$\boxed{②\ \text{障碍形状收缩}：\text{非紧致}\ \mid\ \text{非投射}} ✓✓\ \text{（四类 ⟹ 两类）}$$
$$\boxed{③\ \text{存在性型判据恒真} \Longrightarrow \text{该类判据整族失效}} ✓✓$$
$$\boxed{④\ \text{`V259`-A（有限读）＋ `V262`（紧装）}＝ \text{两面互补的墙}} ✓✓$$

**下一步（两条，且只有两条）**：

```
【N1｜B 臂】⭐ 非紧致臂上是否还能给出 **非聚合、非上同调、携带 $\beta$** 的兼容性？
   —— 这条已被 `V210`／`V215`／`V218` 逐类关闭 ⟹ 要求的是**这些档案未枚举的新结构** ✓
   （不是"再找一个算子" ✗ —— 见 `V260` §7／`V261` §7 的两次毙掉）
【N2｜D 臂】⭐ 一个 **canonical 且 RH-独立（independence gate）** 的**非投射／非有限判定**谓词
   —— 要求：① 定义不引用零点／RH ✓；② 可判定性等级明确（$\Pi_1$／$\Sigma_1$／不可判定）✓；
   ③ 失败 ⟺ $\beta^\star=\tfrac12$ ✓；④ 非聚合、非上同调 ✓ （＝`V259` §6 残余 ＋ 唐稿 gate 合并）✓
【判死标准（沿用 `V259`）】若 N2 的谓词可写成 $\lim F_n$（每个 $F_n$ 有限局部聚合）⟹ 回 `V234`–`V236` ⟹ DEAD ✓
```

**归档**：`docs/V262-inverse-limit-wall-nonsurjective-vacuous-noncompact-nonprojective.md`（本档）＋ `CLOSED-ROUTES-MAP.md` §F.5dq ＋ `MASTER-STATUS-AND-CLOSURES.md` V262 行；`scripts/check_ids.py` ✓；`ID-ALIASES.tsv` 记 `V263` → `V262` 别名 ✓
**边界**：§2／§3 两定理为标准工具的标准转用（本档只作转用与推论）；§4／§5 的收缩与恒真是 [结构性] 论证；§7 对齐为指针级；未用 RH；未跑 Lean；零数值
