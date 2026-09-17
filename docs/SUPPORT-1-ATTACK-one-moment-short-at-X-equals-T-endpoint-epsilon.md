# ⚔️ **攻 SUPPORT-1（第一刀）**：墙的真实形态＝**「在 $X\asymp T$ 处差一个矩」，且只差 $\epsilon$**

> 依唐先生 14:18「我们不是在破墙么？为啥每次碰到墙就停」——**本档不停，直接打墙**✓
> **本档结果**：把 SUPPORT-1 从"support $>1$ 的猜想级障碍"**锐化为**：**「RS 第二矩范围必须达到端点 $X=T$」**，且**只差 $\epsilon$**✓✓✓

---

## §1 两段原文（逐字，本地全文）
$$\textbf{\S7.2(a)}\：\text{"The restriction}\ L\asymp\log T\ \text{(equivalently}\ \boxed{X\le T}\text{) comes from Proposition 5.4: for}\ X\gg T\ \text{the off-diagonal prime sum is no longer dominated by the diagonal, and its evaluation would require information on prime pairs (HL, or equivalently Montgomery's pair correlation for}\ \textbf{support}>1\text{)"}✓$$
$$\textbf{\S7.2(e)}\：\text{"The prime-side evaluation of}\ \mathrm{tr}\,\tilde G^k\ \text{by the diagonal method of Section 5 (multiplicative relations among}\ k\ \text{prime powers, MV for the rest) is available exactly in the}\ \textbf{Rudnick--Sarnak range}\ \boxed{X^k\le T^{2-\epsilon}}；\ \text{at}\ X\asymp T\ \text{this allows only}\ k=1.\ \text{Thus, unconditionally, higher moments add nothing."}✓✓$$

## §2 ⭐⭐ 对读 ⟹ 约束真正落在**哪个矩**上
$$\text{rank--trace 主链（}\S1\text{）需要两件}：\ \mathrm{tr}\tilde G\（\textbf{第一矩}）\quad\textbf{与}\quad\|\tilde G\|^2_{HS}\（\textbf{第二矩型}）✓✓$$
$$\text{第一矩}：\text{RS 给}\ X\le T^{2-\epsilon} \Longrightarrow \textbf{远够}\ ✓✓$$
$$\text{第二矩}：\text{RS 给}\ X^2\le T^{2-\epsilon} \Longrightarrow X\le T^{1-\epsilon/2} \Longrightarrow \boxed{\textbf{恰好不够}}\ ✓✗✓$$
$$\Longrightarrow \boxed{\text{SUPPORT-1 的绑定项}\ =\ \text{HS 范数（第二矩型），}\textbf{不是} \text{第一矩}}✓✓✓$$
$$\qquad ⭐\ \text{这与今日 D-GRAM 系列}\ \textbf{独立同结论}：\text{阻塞点是 HS 范数}✓✓✓$$

## §3 ⭐⭐⭐ 关键读法：**在端点 $X=T$ 处，$k=2$ 只差 $\epsilon$**
$$\text{取}\ X=T：\ T^k\le T^{2-\epsilon} \iff k\le 2-\epsilon \iff \textbf{整数}\ k=1\ \text{（}k=2\ \text{因}\ \epsilon\ \text{失败）}✓✓✓$$
$$\Longrightarrow \boxed{\text{墙}\ =\ \text{"在}\ X=T\ \text{处，第二矩范围}\ \textbf{仅差}\ \epsilon\ \text{失败"}}✓✓✓$$
$$\Longrightarrow ⭐\ \text{即 SUPPORT-1}\ \textbf{不是} \text{"support}>1\ \text{猜想级差距"，而是}\ \textbf{端点}\ \epsilon\ \text{级差距}✓✓✓$$
$$\qquad ⚠️\ \text{注意}：\text{这不意味着墙"容易"（}\epsilon\ \text{可任意小但必须}\ >0），\ \text{但}\ \textbf{形态} \text{与"猜想级"}\ \textbf{完全不同}✓✓$$

## §4 ⟹ 由此得到的**具体攻击目标（可命名）**
$$\boxed{\textbf{目标 S-1}^*\：\text{把}\ k=2\ \text{的 Rudnick--Sarnak 范围从}\ X\le T^{1-\epsilon}\ \text{推到端点}\ X\le T}✓✓✓$$
$$\qquad\text{等价改写}：\text{"}\mathrm{tr}\,\tilde G^2\ \text{在}\ X\asymp T\ \text{处的无条件求值"}✓✓$$
$$\qquad (\text{对照前沿自陈}：\text{at}\ X\asymp T\ \text{only}\ k=1\ \text{available; higher moments add nothing}\ \Longrightarrow\ \textbf{正是此处})✓✓$$

## §5 攻击路线（三条，按可行性排序）
$$\textbf{(甲)}\ \text{端点}\ \epsilon\text{-损失}\ \textbf{是否可消}？\ \text{检查 RS 范围推导里}\ \epsilon\ \text{的来源（}\text{是}\ \textbf{技术性}（\text{平滑／截断）}\ \text{还是}\ \textbf{结构性}（\text{素数分布输入}））✓✓$$
$$\qquad ⚠️\ \text{若为技术性}\ \Longrightarrow\ \text{可能是}\ \textbf{真开口}；\ \text{若为结构性}\ \Longrightarrow\ \text{即 prime pairs}✓$$
$$\textbf{(乙)}\ \text{绕开第二矩}：\text{rank--trace 不等式}\ \textbf{重排} \text{（用}\ \mathrm{tr}\tilde G^3\ \text{等更高矩？}\ \text{——}\S7.2(e)\ \text{说更高矩}\ \textbf{无益}✗）✓$$
$$\textbf{(丙)}\ \text{换不等式}：\text{当前用 Lemma 3.2（含}\ \|\cdot\|^2_{HS}）；\ \text{是否存在}\ \textbf{只用}\ \mathrm{tr}\ \text{与}\ n_+\ \text{的秩下界}？✓✓$$
$$\qquad(\text{若存在} \Longrightarrow \textbf{绕开 SUPPORT-1 的输入}）✓✓✓$$

## §6 边界
$$\text{(i)}\ §1\ \text{为本地全文逐字（行号见}\ \texttt{zeta23\_2608.13637.clean.txt}\ \text{L1247--1251／L1287--1291）}✓✓$$
$$\text{(ii)}\ §2--§4\ \text{为本档对读推论}✓\quad\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
$$\text{(iv)}\ ⚠️\ \text{"}\epsilon\ \text{为技术性"}\ \textbf{未核}；\ \text{本档只负责}\ \textbf{锐化目标}，\ \text{不声称已破}✓$$
