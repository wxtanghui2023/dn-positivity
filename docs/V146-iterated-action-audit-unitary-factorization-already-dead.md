# V146 · ⭐⭐⭐⭐⭐ **Iterated Arithmetic Action（$F_N^2=N R_N$）审计：形式区分【真实 ✓】（显式反例 ✓）｜但包含方向相反 —— 迭代条件是旧条件的【推论】✗｜"$R_N$ 酉" 本身 ＝ 形式存在性条件 ⟹ 困难被【搬回】极化缺口 ✗✓｜⭐⭐⭐ 决定性命中：档案 `p41-g1-unitary-factorization`（2026-09-02）＝ 同类，已判死（**消零定理 ＋ 反例** ✓✓）⟹ **DEAD** ✓**
> 委托 ✓ 唐先生 2026-09-14 23:52（**"V145 → Iterated Arithmetic Action；核心 $F_N^2=N R_N$，$R_N^\dagger R_N=I$；含 6 条判据"** ✓）
> 查图 ✓ **决定性命中** —— `p41-g1-unitary-factorization`（**消零定理 ✓；"｜S(it)｜=1 不 ⟹ 极点在虚轴"反例 ✓；inner-outer 循环 ✓；Hardy 障碍 ✓；判词"与 β-wall 同深度"✓**）｜`SCALE-DYNAMICS-FINAL-BOUNDARY-MAP` §5（**SW6 ＝ genuinely different canonical involution ＋ "未证明为空"**✓）｜`V105` 第 6 行／箱 12 ✓｜`AOB4` §1 ✓
> 执行 ✓ 小灵｜**纸面 ✓（含一处显式反例构造 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ V146 ✓

---

## §0 判定（✓ 五条 ✓）

$$\boxed{\text{① 您的形式区分【真实 ✓】}：F^2=NR\ \text{与}\ F^\dagger F=NI\ \text{是}\textbf{不同条件} ✓\（\text{本档给显式反例 ✓，见 §1 ✓）}}$$
$$\boxed{\text{② 但包含方向相反 ✓✓}：F^\dagger F=NI\ \Longrightarrow\ F=\sqrt N\,U\（U\ \text{酉}\ ✓）\ \Longrightarrow\ F^2=N\,U^2\ \text{且}\ U^2\ \text{酉} ✓\ \Longrightarrow\ \textbf{迭代条件是【旧条件的推论】✗（更弱、非新形状 ✓）}}$$
$$\boxed{\text{③ ⭐ "}R_N\ \text{酉" 本身 ＝ 形式存在性条件 ✓✓：\text{酉性}\ \Longleftrightarrow\ \text{保持某个正定形式} \Longrightarrow \text{迭代路线把困难从"}\Phi\ \text{的极化"}\textbf{搬回}"R_N\ \text{的极化}" \Longrightarrow \textbf{同一缺口}\ ✗✓}$$
$$\boxed{\text{④ ⭐⭐⭐ 决定性 ✓}：\text{档案 }`p41\text{-}g1\text{-}unitary\text{-}factorization`\ \text{＝ 本形状的同类，}\textbf{已判死} ✓✓（\text{消零定理 ＋ 反例 ✓）}}$$
$$\boxed{\text{⑤ }C6／§9\ \text{的对应 ✓}：\text{"非交换交叉尺度律"}\ \textbf{＝ 档案的 SW6} ✓（\text{逐字："a genuinely different canonical involution"；}\textbf{未证明为空} ✓）}$$

## §1 您的形式区分：**真实** ✓（本档给显式反例 ✓）

$$\textbf{反例 ✓（证明二条件不同 ✓）}：F=\begin{pmatrix}0&N\\1&0\end{pmatrix}\ ✓$$
$$\qquad F^2=\begin{pmatrix}N&0\\0&N\end{pmatrix}=NI\ ✓\ \textbf{满足迭代条件};\qquad F^\dagger F=\begin{pmatrix}1&0\\0&N^2\end{pmatrix}\ne NI\ ✗\ \textbf{不满足 similitude} ✓✓$$
$$\qquad\Longrightarrow\ \boxed{F^2=NR\ \not\Longrightarrow\ F^\dagger F=NI\ ✓✓}\ \text{（您这一步在数学上完全正确 ✓）}$$
$$\qquad\Longrightarrow\ \text{且由 }F^2=NR\ \text{可得：本征值 }\lambda^2\in\operatorname{Spec}(NR)=N\cdot\operatorname{Spec}(R)\subset N\cdot S^1\ ⟹ |\lambda|=\sqrt N\ ✓✓\ \text{（}\textbf{自动} ✓，无需正规性 ✓）}$$
$$\qquad\textbf{故 }Gate\ B\ \text{确实"形式免费"} ✓\ \text{—— 但见 §3（代价在别处 ✓）}$$

## §2 ⭐ 但包含方向相反：迭代条件是**旧条件的推论** ✗

$$\text{设 }F^\dagger F=NI\ ✓\ \Longrightarrow\ F=\sqrt N\,U\（U\ \text{酉，}\ U:=F/\sqrt N\ ✓）\ \Longrightarrow\ F^2=N\,U^2\ ✓\ \text{且}\ (U^2)^\dagger(U^2)=I\ ✓$$
$$\qquad\Longrightarrow\ F^2=N\,R\ \text{with}\ R=U^2\ \textbf{酉} ✓✓\ \Longrightarrow\ \boxed{\text{similitude}\ \Longrightarrow\ \text{迭代条件}\ ✓}\ \text{（}\textbf{单向} ✓）$$
$$\qquad\text{配合 §1 的反例（反向不成立 ✓）}\ \Longrightarrow\ \boxed{\text{迭代条件}\ \textbf{严格弱于}\ \text{similitude}\ ✓\ \Longrightarrow\ \text{它不是新形状，而是旧形状的}\textbf{推论} ✗✓}$$
$$\qquad\textbf{（}\text{即：任何满足 similitude 的对象自动满足迭代条件 ✓ —— 故"迭代入口"不引入新的代数空间 ✗）}$$

## §3 ⭐⭐ 决定性结构点："$R_N$ 酉" 本身 ＝ **形式存在性条件**

$$\text{酉性}\ \Longleftrightarrow\ R_N\ \text{保持某个}\textbf{正定 Hermite 形式} ✓（\text{任何酉算子都是某正定形式下的等距 ✓，反之亦然 ✓}）$$
$$\qquad\Longrightarrow\ \text{要求} R_N\ \text{酉}\ \textbf{＝ 要求存在一个（正定）形式} ✓✓\ \text{—— 即}\ \textbf{迭代路线没有消除极化需求，只是把它从 }\Phi\ \text{搬到 }R_N\ ✗✓}$$
$$\qquad\textbf{配合档案 ✓}：`AOB4` §1 逐字"E＋D＋Z 需非刚性；P 需}\textbf{正定配对}（\text{＝ Hodge–Riemann；pure 极化 HS }\textbf{半单}\text{）⟹ char 0 中}\textbf{互斥}"}\ ✓；\ \text{箱 12 逐字"极化 ⊥ 元素性"}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{故 }Gate\ B\ \text{的"免费"是}\textbf{假象} ✗：代价 ＝ 一个正定形式的存在性 ⟹ 落在 }D_1\ \text{／char-0 canonical polarization 缺口} ✗✓}$$

## §4 ⭐⭐⭐ 决定性命中：档案的 **unitary factorization** 已判死（✓✓ 2026-09-02）

$$\text{档案 }`p41\text{-}g1\text{-}unitary\text{-}factorization`\ \text{逐字 ✓（四刀 ✓）}：$$
$$\textbf{① 消零定理 ✓（严格、新 ✓）}：S(w)=\frac{\zeta(\frac12-w)}{\zeta(\frac12+w)}\ \xrightarrow{\ FE\ }\ \chi(\tfrac12-w)\ ✓\ \text{（}\zeta(\tfrac12-w)=\chi(\tfrac12-w)\zeta(\tfrac12+w)\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{ζ 的零点在比值中【完全消掉】} ✗✓\ ——\ \text{"比值型 unitary"}\textbf{不可能携带零点} ✓;\ \text{其极点 }w=-2n-\tfrac12\ \text{与 RH 无关} ✓}$$
$$\qquad\text{数值 ✓}：S(w)\ \text{vs}\ \chi(\tfrac12-w)\ \text{差 }\sim10^{-22}\ ✓;\ |S(it)|=1\ ✓$$
$$\textbf{② 反例 ✓（决定性 ✓）}：S(w)=\frac{w-a}{w+a}\（a\ \text{实}\ ✓）：\ S(-w)=\frac1{S(w)}\ ✓,\ |S(it)|=1\ ✓\ \text{—— 但}\ \textbf{极点在实轴（不是虚轴）} ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{"酉模条件}\ |S(it)|=1\text{"}\ \textbf{不} \Longrightarrow\ \text{极点在虚轴} ✗✓✓}$$
$$\qquad\qquad\textbf{与您 §4 的判断构成【两个方向的对称】✓✓}：\text{您证：}J\text{-unitary}\ \not\Rightarrow\ \text{单位圆}\ ✓;\ \text{档案证：}\text{酉模}\ \not\Rightarrow\ \text{虚轴} ✓\ ——\ \textbf{两方向皆是"酉不约束位置" ✓✓}$$
$$\textbf{③ inner-outer 分解 ⟹ 循环 ✓}：\text{RH}\iff\text{inner 平凡}\ ✓;\ \text{Ingham 只给 }o(T)\ \text{密度} ✗;\ \text{"Euler 结构 ⟹ inner 平凡"需 Euler 延拓 ⟹ 循环} ✓$$
$$\textbf{④ Hardy 类障碍 ✓}：\Xi(w)=\xi(\tfrac12+w)\ \text{整 ✓ 但实轴增长（}\Gamma\ \text{因子}\ (x/2)^{x/2}\ ✓）\ \Longrightarrow\ \notin H^2\ ✗;\ \text{规范化需实轴模（含零点 ⟹ 循环）}✓$$
$$\qquad\Longrightarrow\ \textbf{P41-G1 判词逐字 ✓}：\text{"'unitary factorization' 第一轮 —— 与 }\beta\text{-wall}\ \textbf{同深度}（\text{比值消零／循环}）；\text{'global factorization rigidity'}\ \textbf{未出现}"}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{故您的 }F_N^2=NR_N\（R_N\ \text{酉}）\ \textbf{落在这个已判死的类里} ✗✓\（F/\sqrt N\ \text{酉}\ ⟹\ \text{它是"}\sqrt N\times\text{酉" 分解 ✓）}}$$

## §5 C6／§9 的对应：非交换交叉尺度律 ＝ **SW6**（✓ 档案已有其名与状态 ✓）

$$\text{您 §9 要求 ✓}：F_{mn}=\mathcal C(F_m,F_n)\ ✓,\ \mathcal C\ \text{非乘法／非卷积／非 cocycle／非 character ✓}$$
$$\qquad\Longleftrightarrow\ \textbf{档案 SW6} ✓（`SCALE-DYNAMICS` §5 逐字 ✓）}：\boxed{SW6=\text{a genuinely different canonical involution}}\ ✓$$
$$\qquad\textbf{且档案加粗保留 ✓}：\boxed{\textbf{SW6 尚未证明为空}}\ \text{（"整个终审中必须加粗的一句" ✓）}$$
$$\qquad\textbf{档案建议 ✓（§8）}：\textbf{不建议现在硬造 SW6} ✓\ ——\ \text{与本轮"先审形状"的做法一致 ✓}$$
$$\qquad\text{（前置候选已在档 ✓：}R\text{-CS }X0\ \text{"非 cocycle ＋ 非 coboundary"}\ ✓\ \text{—— 与您 §9 的禁列}\textbf{同形} ✓）$$

## §6 判词与更新（✓）

$$\boxed{\textbf{V146 判词 ✓}：\text{① 您的形式区分真实 ✓；② 但迭代条件 ＝ 旧条件的}\textbf{推论} ✗\（\text{更弱、非新形状 ✓）；③ }R_N\ \text{酉}\ \textbf{＝ 形式存在性条件} ⟹ \text{困难}\textbf{搬回极化缺口} ✗✓；④ 该形状 ＝ 档案 }\textbf{unitary factorization}\ \text{类，}\textbf{已判死（消零定理 ＋ 反例）} ✗✓} \Longrightarrow \boxed{\textbf{DEAD} ✓}（\text{按您 §"1–5 条有一条立即退化即 DEAD" ✓ —— 第 2 条即退化 ✓）}$$
$$\boxed{\text{未被否定的残余 ✓（与 }V145\ \text{一致 ✓）}：\text{① 非交换跨 }\ }N\ \text{兼容律 ＝ SW6 ⛔；② char-0 canonical polarization ⛔ —— 二者仍是 }R_{\rm residual}\ \text{的两半 ✓}}$$
$$\text{`CLOSED-ROUTES-MAP` §F.5h 增补 ✓}：\text{Iterated Arithmetic Action 行 ＋ 消零定理指针 ✓}$$
```
⚠️ §1 反例为【显式构造 ✓ 可验证 ✓】；§2 的蕴含为【一行代数 ✓ 严格 ✓】
⚠️ §3 为【结构性 ✓】："酉 ⟺ 正定形式存在"为标准事实 ✓（II 类 ✓）
⚠️ §4 的四刀为【档案既有 ✓ 逐字核对 ✓】（`p41-g1-unitary-factorization` ✓ 标"严格／新观察／反例／循环"✓）
⚠️ 本档【不】声称"任何含酉的对象都不行" ✗ —— 只声称：【(i) 迭代条件弱于 similitude；(ii) 比值／酉分解型结构已被消零定理与反例判死】✓
⚠️ 未用 RH ✓；未跑 Lean ✓
✅ 净产出 ✓：① 形式区分确认真实（含反例 ✓）；② 包含方向（旧 ⟹ 新 ✓）；③ "酉 ⟹ 形式" ⟹ 搬回极化缺口 ✓✓；④ ⭐⭐⭐ 档案命中（消零定理 ＋ 反例 ＋ 两方向对称 ✓✓）；⑤ SW6 对应 ✓
```
$$\boxed{\text{V146 ✓：①您的形式区分真实（}F^2=NR\not\Rightarrow F^\dagger F=NI\ ✓\text{，反例 }F=\begin{pmatrix}0&N\\1&0\end{pmatrix}\ ✓\text{，且 }F^2=NR\ \text{自动给 }|\lambda|=\sqrt N\ ✓\text{）；②但 }F^\dagger F=NI\Rightarrow F=\sqrt N U\Rightarrow F^2=N U^2\ ✓\ \text{⟹ 迭代条件严格弱于 similitude、是其推论 ✗；③}"R_N\ \text{酉" ⟺ \text{存在正定形式} ⟹ \text{困难搬回 char-0 canonical polarization 缺口（箱 12／}AOB4\ \text{§1）✗✓；④⭐⭐⭐档案 }p41\text{-}g1\text{-}unitary\text{-}factorization（2026-09-02）同形且已判死：消零定理}\ S(w)=\zeta(\tfrac12-w)/\zeta(\tfrac12+w)\overset{FE}{=}\chi(\tfrac12-w)\ \text{⟹ 比值型 unitary 零点完全消掉 ✗；反例 }S=(w-a)/(w+a)\ \text{（}a\ \text{实）酉模 }\ |S(it)|=1\ \text{但极点在实轴 ✗（与您的 }J\text{-unitary}\not\Rightarrow\text{单位圆构成两方向对称 ✓）；inner-outer 循环；Hardy 障碍 ⟹ "与 }\beta\text{-wall 同深度"}\ ✓\ \text{⟹ }\textbf{DEAD};\ \text{⑤非交换交叉尺度律 ＝ SW6（未证明为空 ⛔，不建议硬造 ✓）}$$
