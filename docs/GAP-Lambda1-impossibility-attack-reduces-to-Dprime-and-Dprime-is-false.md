# 🎯 **攻 $\Lambda_1$**：不可能性证明的精确形式 ⟹ **它归约到 (D′)**，而 **(D′) 是假的**

> 依唐先生 13:37「继续」；承接 `GAP-C0 §7.5`（$C_0$ 紧 ⟹ 直接攻 $\Lambda_1$ 或 $\Lambda_2$）✓
> **本档结果**：$\Lambda_1$ 的**证伪**（即把"实质封闭"升级为定理）**可写成条件定理**，**条件为 (D′)**；而 **(D′) 作为全称陈述是假的** ⟹ $\Lambda_1$ **仍 OPEN**，"实质封闭"**仍是informal** ✓✓

---

## §1 $\Lambda_1$ 重述（要证伪的目标）
$$\Lambda_1：\exists\ \text{非-}\zeta\text{-local 不变量}\ \mathcal I\ \text{满足 (A)--(E)}：$$
$$\qquad\text{(A) 非线性／多层／范数型}\ \big|\ \text{(B) 不等价于}\ G\succeq0\ \big|\ \text{(C) 不需显式公式算绝对幅度}$$
$$\qquad\text{(D)}\ \textbf{有独立算术上界}\ \big|\ \text{(E) 该上界／律对}\ \beta>\tfrac12\ \text{给出 selection strength}✓$$

## §2 不可能性论证的骨架（三段）
$$\textbf{第 1 段}\（\text{由 (D)}）：|\mathcal I(F)|\le B(F)，\ B\ \textbf{由整数性／乘性／计数} \text{可证}✓$$
$$\textbf{第 2 段}\（\text{由 (C)}）：B\ \textbf{不得} \text{经由显式公式／零点幅度} \Longrightarrow B\ \text{只能看见}\ \textbf{有限层（局部）数据}✓$$
$$\qquad\Longrightarrow\ B\ \text{的水平集是}\ \textbf{cylinder}（\texttt{V271-A}）✓✓$$
$$\textbf{第 3 段}\（\text{由}\ \texttt{V259-A}／\texttt{V270-A}）：\text{乘子}\ \textbf{F}_\sigma(s)=\zeta(s)(1-q^{\sigma-s})\ \text{与}\ \zeta\ \text{在}\ p\le P\ \text{层}\ \textbf{局部相同，却有}\ \mathrm{Re}\,s=\sigma\ \text{上的零点}✓$$
$$\qquad\Longrightarrow\ \text{任何}\ \textbf{cylinder 泛函} \text{对离轴对}\ (1,1)\ \textbf{中性} \Longrightarrow \text{与 (E) 矛盾} \Longrightarrow \boxed{\textbf{第 2 段是关键}}✓✓$$

## §3 ⭐⭐ 第 2 段的缺口：(D′) 必须显式假设
$$\text{第 2 段的推理}\ \textbf{缺一步}：\text{"(D) 由算术可证"}\ \textbf{不自动} \text{推出"(D) 是 cylinder"}✓✗$$
$$\qquad\text{因为一个界可以}\ \textbf{由算术内容＋极限论证} \text{证明，}\ \textbf{而不由任何单个有限层决定}✓✓$$
$$\Longrightarrow\ \text{须补假设}\ \boxed{\textbf{(D′)}：\text{界}\ B\ \text{是}\ \textbf{cylinder 泛函}（\text{由某有限层决定}）}✓✓$$
$$\Longrightarrow\ \boxed{\text{条件定理}：\ \textbf{(A)--(E)＋(D′)} \Longrightarrow \Lambda_1\ \text{假}}✓✓\quad(\text{即"实质封闭"可升级为定理}\ \textbf{当且仅当}\ (D′))✓$$

## §4 ⭐⭐⭐ (D′) 作为**全称陈述是假的**（给出反例）
$$\textbf{反例}：\textbf{Mertens 定理}（\text{初等可证，}\textbf{不用}\ \zeta）：\sum_{p\le x}\frac{\log p}{p}=\log x+O(1)✓✓$$
$$\qquad\text{它}\ \textbf{由算术可证}（\text{初等，}\text{Chebyshev／Mertens}）✓\quad\text{但它是}\ \textbf{极限型陈述}，\ \textbf{不由任何单个有限层决定}✗✗$$
$$\qquad\Longrightarrow\ \boxed{\text{(D′)}\ \textbf{假}}（\text{至少存在一个算术可证的非-cylinder 界}）✓✓✓$$
$$\qquad(\text{同类：}\ \text{Chebyshev}\ \psi(x)\asymp x；\ \text{Brun 筛上界}\ \text{——皆为初等／算术可证，皆非单层条件})✓$$

## §5 ⭐ 结论（对 $\Lambda_1$ 的诚实判定）
$$\text{① 不可能性}\ \textbf{可写成条件定理}，\ \text{条件是}\ (D′)✓$$
$$\text{②}\ (D′)\ \textbf{作为全称陈述是假的} \Longrightarrow \text{不可能性}\ \textbf{不能} \text{无条件获得}✗$$
$$\Longrightarrow\ \boxed{\Lambda_1\ \textbf{仍 OPEN}；\ \texttt{V187}\ \text{的"形式存在、实质封闭"}\ \textbf{仍是 informal}，\ \text{不能写成定理}}✓✓✓$$
$$\qquad ⚠️\ \text{这也修正了项目内一个隐含读法}：\text{"实质封闭"}\ \textbf{不是} \text{已证结论，}\ \text{而是}\ \textbf{在}\ (D′)\ \text{下的结论}✓✓$$

## §6 与既有层的对接（不退化为墙审计）
$$\text{(D′)}\ =\ \text{项目自己标记的}\ \textbf{"可有限呈现（finitely-presentable）"前提}（\texttt{V322}／\texttt{E.3}：\text{五个闭合全部依赖该隐藏前提}）✓✓$$
$$\Longrightarrow\ \text{本档把}\ (D′)\ \text{从"隐藏前提"}\ \textbf{升级为一条具名命题}，\ \text{并}\ \textbf{给出它的反例}✓✓✓$$
$$\Longrightarrow\ ⭐\ \text{这正面回答了}\ \texttt{V322}\ \text{的悬挂问题}：\text{该隐藏前提}\ \textbf{在全称形式上不成立}⟹ \text{五个闭合}\ \textbf{不是} \text{定理，}\ \text{而是}\ \text{条件结论}✓✓$$

## §7 边界
$$\text{(i)}\ §2\ \text{三段骨架为本档写法（综合}\ \texttt{V271-A}／\texttt{V259-A}／\texttt{V270-A}）✓\quad\text{(ii)}\ §4\ \text{的 Mertens 反例为经典事实}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零计算}✓\quad\text{(iv)}\ ⚠️\ (D′)\ \text{的"cylinder"须用}\ \texttt{V271-A}\ \text{的确切定义（\text{本档沿用}）}✓$$
