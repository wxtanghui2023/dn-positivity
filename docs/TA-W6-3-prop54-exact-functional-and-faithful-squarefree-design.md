# ⚔️ W6-3 · **Prop 5.4 的精确泛函（逐字）＋ 平方自由实验的忠实形式**

> 承接 `TA-W6-2` ⑤（"$w(h)$ 与误差预算尚未与前沿 Prop 5.4 逐字对齐"）⟹ **本档解决** ✓
> 材料：`external_refs/zeta23_2608.13637.clean.txt` L839–L900（**逐字**）✓

---

## ① 前沿 **Proposition 5.4（Prime term）** 逐字
$$\textbf{Prop 5.4}：\ M[P_X,P_X]=\frac{T}{\pi}\sum_{n\le X}\frac{\Lambda(n)^2}{n}g(\log n)+O\big(\chi(L^2X)\big),\qquad g:=\phi^2\star\phi^2✓$$

$$\text{证明结构（逐字）}：P_X(\tau)=-\tfrac{1}{2\pi}\sum_na_n(n^{i\tau}+n^{-i\tau}),\ \ a_n=\Lambda(n)/\sqrt{n}✓$$
$$\qquad\text{代}\ \tau=\tau'+x，\ \text{"for fixed}\ x\ \text{the variable}\ \tau'\ \text{ranges over}\ I\cap(I-x),\ \textbf{which is empty for}\ |x|\ge T\ \text{and equals}\ [T+x_-,2T-x_+]\ \text{for}\ |x|<T"✓✓$$
$$M[P_X,P_X]=\frac{1}{2\pi^2}\mathrm{Re}\sum_{n,m}a_na_m\underbrace{\int_{-T}^{T}\Phi(x)^2n^{ix}\Big[\int_{T+x_-}^{2T-x_+}(n/m)^{i\tau'}d\tau'+\int(nm)^{i\tau'}d\tau'\Big]dx}_{=:\ \textbf{三个块}}✓$$
$$\qquad \boxed{D\ \text{（}n=m\ \text{的第一内积分）}\quad\big|\quad O_1\ \text{（}n\ne m\ \text{的第一内积分）}\quad\big|\quad O_2\ \text{（第二内积分全体）}}✓✓$$

## ② ⭐⭐⭐ **关键：bandwidth 限制是"烧进窗口"的**
$$\text{外层}\ x\ \text{积分}\ \textbf{只跑在}\ [-T,T]（\text{因}\ \Phi(x)^2\ \text{支撑于此}）⟹ \textbf{bandwidth}\le1\ \text{被}\ \textbf{烧进窗口}✓✓$$
$$\text{而对}\ |x|<T，\text{内层}\ \tau'\ \text{区间长度}\ \asymp T-|x| \Longrightarrow \text{离对角先验尺度}\ \frac{T}{|\log(n/m)|}✓✓$$
$$\Longrightarrow \boxed{\text{W6 所需的具体泛函}\ =\ \textbf{对}\ O_1\ \text{的控制}（n\ne m，\text{同一窗口，}\ X\ \text{与}\ T\ \text{的相对大小是关键参数}）}✓✓✓$$

## ③ ⭐ 平方自由实验的**忠实形式**（现在可以写准了）
$$\text{唯一改动}：\ \text{系数}\ a_n=\frac{\Lambda(n)}{\sqrt n}\ \to\ a_n^{(\square)}=\frac{\mu^2(n)}{\sqrt n}✓$$
$$\text{同样做}\ D／O_1\ \text{分块}，\ \text{同样窗口}\ \Phi\ \text{与}\ |x|<T\ \text{支撑}✓$$
$$\boxed{\text{判据}：\text{比较}\ |O_1|/D\ \text{随}\ X/T\ \text{的变化，两族对照}}✓✓$$
$$\qquad\textbf{(I)}\ \text{squarefree 的}\ |O_1|/D\ \text{在}\ X\gg T\ \text{仍有界，而 primes 无界} \Longrightarrow \text{墙}＝\boxed{\textbf{prime extraction}}✓✓$$
$$\qquad\textbf{(II)}\ \text{两族}\ |O_1|/D\ \text{皆无界} \Longrightarrow \text{墙在}\ \boxed{\textbf{二体结构本身}}✓✓$$
$$\text{忠实性}：\text{系数替换}\ \textbf{不改工程结构}（\text{同一}\ D／O_1／O_2\ \text{分块、同一窗口、同一支撑限制}）⟹ \text{两族}\ \textbf{可比}✓✓$$

## ④ 与既有登记的对接
$$\text{前沿 §7.2(a) 逐字}：\text{绑定性约束}\ L\asymp\log T\（\text{等价}\ X\le T\text{）来自}\ \textbf{Prop 5.4}；X\gg T\ \text{时离对角素和不被对角支配}⟹ \text{需}\ \textbf{prime pairs}✓$$
$$\Longrightarrow \text{故}\ \textbf{本档的}\ O_1\ \text{＝前沿 §7.2(a) 所指的那个对象}（\text{逐字对齐完成}）✓✓$$
$$\text{我方既有三分}（\texttt{HE-JIA1b}）：\text{(N) 近对角}\ \big|\ \text{(K) Farey／小分母}\to\text{Kloosterman}\ \big|\ \text{(G) 一般}\to\text{大筛}⟹ \text{可按此三分}\ \textbf{逐类攻}\ O_1✓✓$$

## ⑤ 判定与下一步
$$\text{本档}：\text{① Prop 5.4 泛函}\ \textbf{逐字入仓}；\text{② bandwidth 限制}\ \textbf{烧进窗口} \text{这一结构事实；③ 平方自由实验}\ \textbf{忠实形式确定}✓✓$$
$$\textbf{下一步}：\text{① 取窗口}\ \phi\ \text{的显式形式}（(5.1)--(5.3)：}\Phi=c\phi^2,\ g=\phi^2\star\phi^2,\ (L-2w-|y|)_+\le g\le A_\phi\le(L-|y|)_+\text{）}✓$$
$$\qquad\text{② 按}\ ③\ \text{跑两族}\ |O_1|/D\ \text{对照（含数值卫生）} \to \text{得 (I)／(II) 判定}✓✓$$

## ⑥ 边界
$$\text{(i)}\ §①--§②\ \textbf{逐字}（本地 PDF 抽取）；§③--§⑤\ \text{为}\ [\textbf{结构}]\ \text{级设计}✓$$
$$\text{(ii)}\ \text{本轮}\ \textbf{未跑计算}，\ \textbf{未用 RH}✓\quad\text{(iii)}\ \text{窗口}\ \phi\ \text{显式形式}\ \textbf{未取}（\text{下一步}）✓$$
