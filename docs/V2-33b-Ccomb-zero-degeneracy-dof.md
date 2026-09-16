# V2-33 第二刀 — **$C_{\rm comb}=0$ 退化集的自由度** ⟹ 判定 **倾向"净收益 ≤ 0"，仍 OPEN**

> 唐先生 2026-09-16 22:01「继续」；按 REVIEW-V2G §3 的**唯一入口**起手（不再重复 C--S／相位／$F_5$ 账本）✓
> 目标：$\boxed{\text{算}\ C_{\rm comb}=0\ \text{的自由度}}$✓

---

## 1. $\ast$ 精确写出退化条件（由 V2-32 第二层的 $C_{\rm comb}$）
$$C_{\rm comb}＝\frac{\Delta\tilde\ell_2\tilde\ell_2'}{\tilde\ell_1\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1'}-\frac{\Delta''\tilde\ell_2''\tilde\ell_2'''}{\tilde\ell_1''\tilde\ell_1'\mathfrak q_1\mathfrak p_1n_1''}（\text{两份副本，第二份取共轭}）✓$$
$$C_{\rm comb}=0 \iff \boxed{\Delta\,\tilde\ell_2\tilde\ell_2'\,\tilde\ell_1''\,n_1''\ =\ \Delta''\,\tilde\ell_2''\tilde\ell_2'''\,\tilde\ell_1\tilde\ell_1'\,n_1'}✓✓$$
$$\qquad（\text{已约去公共因子}\ \mathfrak q_1\mathfrak p_1；\ \Delta,\Delta''\ \text{各为互补因子与}\ a\ \text{型的多项式}）✓$$
$$\Longrightarrow\ \boxed{C_{\rm comb}=0\ \textbf{是一条多项式方程}}✓✓$$

## 2. ⭐⭐⭐ 结构判定一：**码维 1**（非可忽略）
$$\text{变量集}：(\Delta,\Delta'',\tilde\ell_1,\tilde\ell_1',\tilde\ell_1'',\tilde\ell_2,\tilde\ell_2',\tilde\ell_2'',\tilde\ell_2''',n_1',n_1'')＋\text{参数}✓$$
$$\qquad\textbf{仅一条方程} \Longrightarrow \text{解集}\ \textbf{码维 1} \text{（codimension 1）}✓✓$$
$$\Longrightarrow\ \text{解数}\ \asymp\ \text{ambient}\ /\ (\text{某一变量的取值范围}) \Longrightarrow \boxed{\text{退化集}\ \textbf{不是可忽略集}}✓✓$$
$$\qquad（\text{即：它比 ambient 少"一个变量量级"，}\ \textbf{而非} \text{指数级小}）✓$$
$$\qquad\Longrightarrow\ \text{与}\ \mathrm{V2\text{-}33}\ \text{第一刀所担心的情形}\ \textbf{一致}：\ \text{"大退化族"}✓$$

## 3. ⭐⭐⭐ 结构判定二：退化集**正是新 C–S 的"对角"**
$$C_{\rm comb}=0 \iff \text{两份副本的系数}\ \textbf{相消} \Longleftrightarrow \textbf{新 C--S 的对角（collision）条件}✓✓$$
$$\Longrightarrow\ \text{与 BC 自身结构}\ \textbf{同型}：\ \text{(4.20) 逐字}\ \text{"We shall give a}\ \boxed{\textbf{trivial bound}}\ \text{for the terms with}\ \Delta=0\text{"}✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{BC 自己对退化支（}\Delta=0\text{）的处理}\ =\ \textbf{平凡界／退回 counting}}✓✓$$
$$\qquad\qquad\textbf{且该切实}\ \textbf{确实进入}\ BC\ \text{的账本}（\text{即}\ \Delta=0\ \text{支不是被 Weil 吸收的）}✓✓$$
$$\Longrightarrow\ \boxed{\text{故新退化支（}C_{\rm comb}=0\text{）}\ \textbf{同样须退回计数}，\ \text{不会自动被 Weil 支吸收}}✓✓$$

## 4. ⭐⭐ 由此得到的定量含义
$$\text{Weil 支（}C_{\rm comb}\ne0\text{）}：\ \text{得}\ \sqrt q\ \text{型节省}✓\qquad\text{退化支（}C_{\rm comb}=0\text{）}：\ \textbf{无事可做} \Longrightarrow \text{退回}\ \textbf{counting}✓$$
$$\text{而}\ \mathrm{V2\text{-}33}\ \text{第一刀}：\ \text{收益}\ L^{-1}\ \text{已被}\ C_{\rm CS}\approx L\ \textbf{首阶抵消}✓$$
$$\Longrightarrow\ \boxed{\text{退化支的计数贡献}\ \textbf{再往上加}} \Longrightarrow \text{净幂次}\ \le\ L^{0}✓✓$$
$$\qquad\Longrightarrow\ \text{倾向}\ \boxed{\text{"收益恰被抵消"至"反而变差"之间}}✓✓\quad(\text{即}\ \mathrm A\ \text{净收益}=0\ \text{或}\ \mathrm{DEAD}\ \text{此架构})✓$$

## 5. 判定（唐先生四格）
$$\boxed{\begin{array}{c|c}\text{结果}&\text{判定}\\\hline\text{净得}\ L^{-\delta}&\mathrm{ALIVE}\\\text{收益恰被抵消}&\mathrm A，\text{净收益}=0\\\text{新增成本超过收益}&\mathrm{DEAD}（\text{仅此架构}）\\\text{无法确定}&\mathrm{OPEN}\end{array}}✓$$
$$\Longrightarrow\ \boxed{\textbf{倾向第 2--3 行}}：\ \text{退化集码维 1（非可忽略）＋ BC 自身对退化支用平凡界} \Longrightarrow \textbf{净收益}\le0✓✓$$
$$\qquad\textbf{但}：\ \text{须以}\ \textbf{显式平方后相位} \text{核实}\ C_{\rm comb}\ \text{的精确变量集} \Longrightarrow \text{记}\ \boxed{\textbf{倾向}\le0，\ \textbf{仍 OPEN}}✓✓$$

## 6. 残余（不得省略）
$$\text{残余 1（关键）：}\ \textbf{平方后相位未显式写出}（\text{V2-32 第二层残余 1}）\Longrightarrow C_{\rm comb}\ \text{的变量集为}\ \textbf{临时版}✓✓$$
$$\text{残余 2：退化支的}\ \textbf{计数界量级} \text{未算（须与 Weil 支同账比较）}✓$$
$$\text{残余 3：}\ n_1''\ \text{（第二副本）的来源与范围未核}✓\quad\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只算退化集自由度；}\quad\text{② }\textbf{不} \text{宣布 ALIVE／DEAD（除倾向）；}\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐ 退化条件写为}\ \textbf{一条多项式方程}：\Delta\tilde\ell_2\tilde\ell_2'\tilde\ell_1''n_1''=\Delta''\tilde\ell_2''\tilde\ell_2'''\tilde\ell_1\tilde\ell_1'n_1'✓✓$$
$$\text{(ii) ⭐⭐⭐ 结构判定一：}\ \textbf{码维 1} \Longrightarrow \text{退化集}\ \textbf{非可忽略}✓✓$$
$$\text{(iii) ⭐⭐⭐ 结构判定二：退化集}\ \textbf{＝新 C--S 的对角}，\ \text{与 BC 的}\ \Delta=0\ \text{同型；\ BC 对}\ \Delta=0\ \text{用}\ \textbf{trivial bound} \Longrightarrow \text{新退化支亦须退回 counting}✓✓✓$$
$$\text{(iv) ⭐⭐ 定量含义：退化支计数}\ \textbf{再叠加} \text{于已抵消的首阶} \Longrightarrow \text{净幂次}\le L^0✓✓$$
$$\text{(v) 判定}\ \boxed{\textbf{倾向}\le0，\ \textbf{仍 OPEN}} \text{（须显式平方相位核实）}✓$$
