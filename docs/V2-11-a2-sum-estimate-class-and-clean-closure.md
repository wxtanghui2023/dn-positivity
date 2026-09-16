# V2-11 — **$a_2$-sum 属于什么估计类？** ⟹ 判定：**该 expansion 干净关闭**

> 唐先生 2026-09-16 20:55「继续下一入口」（＝ REVIEW-V2 登记的**唯一入口**）。
> 问题：$$\boxed{(4.19)\text{--}(4.23)\ \text{中的}\ a_2\text{-sum}\ \textbf{到底属于什么估计类}？}$$
> 预登记判据（唐先生）：若只是**已有 Weil 对象的重新排列** ⟹ **该 expansion 可干净关闭**；若出现**新的可平均结构** ⟹ 才重新进入 envelope ✓

---

## 1. (4.19)–(4.23) 结构（PDF 逐段，**外部来源，仅作数据**）
$$\textbf{(4.19)/(4.20)}：\ \text{经 (4.17) 改写后，相位 (4.12) 变为含}\ a_2\ \text{的若干项（}\eta[\dots]\text{）}✓$$
$$\textbf{⭐ } \delta\ \text{的定义（原文逐字）}：$$
$$\qquad\delta：＝a_2\,(d\tilde\ell'_1-d'\tilde\ell_1)\,\tilde\ell_2\tilde\ell'_2p_2\,(da_1\tilde\ell'_2-d'a'_1\tilde\ell_2)\,\tilde\ell_1\tilde\ell'_1q_1✓✓$$
$$\textbf{(4.21) 两分}：\ \mathscr V_{b,\eta}=\mathscr V^{\delta=0}_{b,\eta}+\mathscr V^{\delta\ne0}_{b,\eta}✓$$
$$\qquad\textbf{原文（处理方式）}：\ \text{"We shall give a}\ \boxed{\textbf{trivial bound}}\ \text{for the terms with}\ \delta=0\text{, whereas we will}\ \boxed{\textbf{use Weil's bound on the sum over}\ n'_2}\ \text{to handle the terms with}\ \delta\ne0\text{"}\ ✓✓✓$$
$$\textbf{(4.22)}（\delta=0\ \text{时}）：\ a_2(d\tilde\ell'_1-d'\tilde\ell_1)\tilde\ell_2\tilde\ell'_2p_2=(da_1\tilde\ell'_2-d'a'_1\tilde\ell_2)\tilde\ell_1\tilde\ell'_1q_1$$
$$\qquad\text{原文}：\ \text{"it allows us to express either}\ a_1\ \text{or}\ a'_1\ \text{in terms of all the other variables"}\ \Longrightarrow\ a_1=f(a'_1;a_2;\dots),\ a'_1=g(a_1;a_2;\dots)✓✓$$
$$\qquad\text{且整除推论}：\ \tilde\ell_1|a_2\tilde\ell'_1,\ \tilde\ell'_1|a_2\tilde\ell_1,\ \tilde\ell_2|a_1\tilde\ell'_2,\ \tilde\ell'_2|a'_1\tilde\ell_2 \Longleftrightarrow \boxed{\ell_1|a_2\ell'_1,\ \ell'_1|a_2\ell_1,\ \ell_2|a_1\ell'_2,\ \ell'_2|a'_1\ell_2}✓✓$$
$$\textbf{随后}：\ \mathscr V^{\delta=0}\ \text{由}\ \sum_{a_1,a'_1,a_2\asymp A\ \text{带上述整除条件},\ a_1=f(\cdot),a'_1=g(\cdot)}(|a_1|^2+|a'_1|^2)\ \text{型式控制}（\text{trivial}）✓$$

## 2. ⭐⭐ 判定：**$a_2$-sum 没有独立估计类**
$$\textbf{(i) }\ \delta\ \textbf{＝}\ a_2\times(\text{碰撞／对角条件})✓✓\quad(\text{因}\ \delta\ \text{的首因子即}\ a_2)$$
$$\qquad\Longrightarrow\ \delta=0 \Longleftrightarrow a_2=0\ \text{或}\ (d\tilde\ell'_1=d'\tilde\ell_1)\ \text{或}\ (da_1\tilde\ell'_2=d'a'_1\tilde\ell_2) \Longrightarrow \boxed{\delta\ \text{编码的正是}\ \textbf{碰撞（对角）条件}}✓✓$$
$$\textbf{(ii) }\ \delta=0\ \text{支：}\ \textbf{trivial bound} \text{（原文逐字）}——\ \text{因}\ a_1,a'_1\ \text{被 (4.22)}\ \textbf{解出} \text{，}\ a_2\ \text{只作带整除约束的}\ \textbf{计数求和} \Longrightarrow \boxed{\textbf{计数类}}✓✓$$
$$\textbf{(iii) }\ \delta\ne0\ \text{支：}\ \textbf{Weil 界施于}\ n'_2\ \text{之和}（\text{原文逐字）}\Longrightarrow \boxed{\text{估计对象是}\ n'_2,\ \textbf{不是}\ a_2}✓✓$$
$$\Longrightarrow\ \boxed{a_2\text{-sum}\ \textbf{或落于计数类、或落于}\ n'_2\text{-Weil 类}，\ \textbf{无独立估计类}}✓✓$$

## 3. ⭐ 预登记判据的结论：**干净关闭**
$$\text{按唐先生预登记}：\ \text{"若它最终只是}\ \textbf{已有 Weil 对象的重新排列} \Longrightarrow \text{这条 expansion}\ \textbf{可以干净关闭}\text{"}✓✓$$
$$\boxed{\text{判定：该 expansion}\ \textbf{干净关闭}}\ ✓✓\quad(\text{理由＝§2：}a_2\text{-sum 无新可平均结构})$$
$$\qquad\textbf{且关闭原因比"重排"更结构}：\ a_2\ \textbf{与}\ \delta\text{-split 纠缠} \text{（乘性因子）}\Longrightarrow \text{释放}\ a_2\ \text{会}\textbf{改变}\ \delta=0\ \text{的含义}✓✓$$

## 4. ⭐⭐ 由此提取的**容量判据**（本次弧线的净收获）
$$\boxed{\text{变量可被"解放"（留外层）}\ \Longleftrightarrow\ \text{它在相位中}\ \textbf{以差分／相消形式} \text{出现}，\ \textbf{而非} \text{乘以碰撞（对角）条件}}✓✓$$
$$\qquad a_1：\ \text{以}\ (a_1-a'_1)\ \text{出现} \Longrightarrow \textbf{可解放}✓（\text{BC 的第一次 expansion}）$$
$$\qquad a_2：\ \text{作为}\ \delta\ \text{的乘性首因子} \Longrightarrow \textbf{不可解放}✓✓$$
$$\Longrightarrow\ \boxed{\text{这解释了为何 BC 的"longer diagonal"是}\ \textbf{分支特定} \text{的，}\ \textbf{不是} \text{变量对称性原则}}✓✓\quad(\text{与 V2-10 判定一致，并给出}\ \textbf{机制})✓$$

## 5. 与既有判定的关系
$$\mathrm{V2\text{-}10}\ \text{判定 C（局部分支开放，整体未判定）} \Longrightarrow \text{本档}\ \textbf{推进为}\ \text{关闭}✓$$
$$\qquad\text{但}：\ \textbf{不} \text{主张"容量墙"（B）}，\ \text{而是}\ \text{该 expansion}\ \textbf{不成立} \text{（无独立估计类）}✓$$
$$\qquad\text{且}\ 1/20\ \text{是否可突破}\ \textbf{仍未触及}✓\quad(\text{本档不涉及 envelope})✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}\delta\ne0\ \text{支的 Weil 界细节（}\mathscr V^{\delta\ne0}\ \text{的完整界式）未逐字取全}✓$$
$$\text{残余 2：}\ \text{容量判据（§4）为}\ \textbf{[结构判定]}，\ \text{基于}\ a_1,a_2\ \text{在本证明中的实际角色，}\ \textbf{未证} \text{为一般定理}✓$$
$$\text{残余 3：}D_b\ \text{六项中另四项仍未逐项溯源；残余 A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只回答"属于什么估计类"，}\textbf{不} \text{进入 envelope；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) }\delta\ \text{的定义逐字：}\ \delta＝a_2\times(\text{碰撞条件})\Longrightarrow \boxed{\delta\ \text{编码碰撞（对角）条件}}✓✓$$
$$\text{(ii) 两支处理方式逐字：}\ \delta=0\Rightarrow\textbf{trivial bound}（\text{计数类}）；\ \delta\ne0\Rightarrow\textbf{Weil 施于}\ n'_2✓✓$$
$$\text{(iii) ⭐ 判定：}\ a_2\text{-sum}\ \textbf{无独立估计类} \Longrightarrow \text{按预登记判据，}\boxed{\text{该 expansion 干净关闭}}✓✓$$
$$\text{(iv) ⭐⭐ 提取容量判据：变量可解放}\Longleftrightarrow\text{相位中以差分出现（非乘碰撞条件）}\Longrightarrow \text{解释}\ a_1\ \text{可、}\ a_2\ \text{不可}✓✓$$
$$\text{(v) 不含容量墙主张；}1/20\ \text{未触及}✓$$
