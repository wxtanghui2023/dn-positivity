# ⚔️ **B2-UB（乙）执行**：UB-1 **非空** ＋ ⭐⭐⭐ **非对角模式在数量上压倒对角** ⟹ **C2-b 的"仅对角"必须修正**

> 依唐先生 15:36「开（乙）」＋ B2-UB 三层规格（UB-1 可行性／UB-2 stationary phase 大小／UB-3 最终预算）✓
> **本档结果**：UB-1 **非空**（附显式可行条件）；UB-2 Hessian **精确算出**；⭐ 非对角点数 $\asymp\prod_i|C|/L_i$ **vs 对角 1 个** ⟹ **支配性反转**✓✓✓

---

## §0 采纳的纠正（唐先生）
$$\text{我在}\ \texttt{cc2e180}\ \text{写"仅对角}\ k\ \text{有驻定点"}\ \Longrightarrow \textbf{过快}✗$$
$$\text{正确驻定条件}：\frac{\phi'(u)}{x_i}=-2\pi k_i \Longrightarrow \boxed{k_ix_i=C},\qquad C:=-\frac{\phi'(u)}{2\pi}✓✓$$
$$\Longrightarrow \textbf{非对角}\ k\ \textbf{并非自动不存在}：\text{只需}\ x_i=\frac{C}{k_i}\in[L_i,U_i]\ \text{（dyadic 盒）}✓✓✓$$
$$\Longrightarrow \text{标量自洽}：u=C\sum_i\frac1{k_i} \Longrightarrow \boxed{2\pi u+\phi'(u)\,H_k=0},\qquad H_k:=\sum_i\frac1{k_i}✓✓\quad(\text{与唐先生同})✓$$

## §1 ⭐⭐ UB-1 可行性：**非空**（附显式条件）
$$\text{盒子可行性}：x_i=\frac{C}{k_i}\in[L_i,U_i]\ \forall i \Longleftrightarrow \boxed{|k_i|\in\Big[\frac{|C|}{U_i},\ \frac{|C|}{L_i}\Big]}\quad(\text{每个}\ i\ \text{一个区间})✓✓$$
$$\Longrightarrow \text{须同时}：\boxed{\max_i|k_i|L_i\ \le\ |C|\ \le\ \min_i|k_i|U_i}✓\qquad(\text{dyadic}\ U_i=2L_i \Longrightarrow |k_i|L_i\asymp|C|)✓✓$$
$$\text{标量方程}\ 2\pi u+\phi'(u)H_k=0：\text{对}\ u\ \textbf{给定}，\text{取}\ H_k=\frac{-2\pi u}{\phi'(u)}\ \text{即可（选}\ k\ \text{使}\ \sum k_i^{-1}\ \text{匹配）}✓✓$$
$$\Longrightarrow \boxed{\textbf{UB-1：}\mathcal K^{\rm off}_{\rm stat}\ne\varnothing\ \text{（非空）}}✓✓✓\qquad(\text{唐先生的纠正成立；"仅对角"不成立})✓$$
$$\qquad ⚠️\ \text{Poisson 权重给出上界}：|\hat g(k)|\ \text{快速衰减需}\ |k_i|\lesssim M_i \Longrightarrow \text{有效}\ k\ \text{满足}\ |C|/L_i\lesssim M_i\ \text{即}\ |C|\lesssim L_iM_i✓✓$$

## §2 ⭐⭐ UB-2：Hessian **精确**
$$\frac{\partial^2\Phi_k}{\partial x_i^2}=-\frac{\phi'(u)}{x_i^2}+\phi''(u),\qquad \frac{\partial^2\Phi_k}{\partial x_i\partial x_j}=\phi''(u)\ (i\ne j) \Longrightarrow \boxed{H=D+\phi''(u)\mathbf 1\mathbf 1^{\!\top}},\ D_{ii}=-\frac{\phi'(u)}{x_i^2}✓✓$$
$$\text{用驻定}\ \phi'(u)=-2\pi k_ix_i \Longrightarrow D_{ii}=\frac{2\pi k_i}{x_i}=\boxed{\frac{2\pi k_i^2}{C}}✓✓\qquad(\text{与唐先生同})✓$$
$$\text{矩阵行列式引理}：\boxed{\det H=\Big(\frac{2\pi}{C}\Big)^{r}\prod_ik_i^2\Big[1+\frac{C\phi''(u)}{2\pi}\sum_i\frac1{k_i^2}\Big]}✓✓\quad(\text{与唐先生同})✓$$
$$\qquad \text{退化条件}：1+\frac{C\phi''(u)}{2\pi}\sum_ik_i^{-2}=0 \Longrightarrow \text{须单做 Airy／高阶 stationary phase}✓✓$$

## §3 ⭐⭐⭐ 关键新结果：**每个驻点的贡献 + 驻点计数**
$$\text{用}\ |k_i|\asymp|C|/x_i：\prod_ik_i^2\asymp\frac{|C|^{2r}}{\prod_ix_i^2} \Longrightarrow \det H\asymp 2\pi^r\frac{|C|^{r}}{\prod_ix_i^2}\,[1+\ldots]✓$$
$$\Longrightarrow \boxed{|\det H|^{-1/2}\ \asymp\ \frac{\prod_ix_i}{|C|^{r/2}}\,[1+\ldots]^{-1/2}}✓✓\quad(\textbf{每驻点贡献：随}\ |C|\ \textbf{递减})✓$$
$$\text{盒内}\ k\ \text{计数}：|k_i|\in\Big[\frac{|C|}{U_i},\frac{|C|}{L_i}\Big] \Longrightarrow \#\asymp\frac{|C|}{L_i}\ \text{（每个}\ i\text{）} \Longrightarrow \boxed{\#\mathcal K\asymp\prod_i\min\Big(\frac{|C|}{L_i},\ M_i\Big)}✓✓$$
$$\qquad(\min\ \text{来自 Poisson 权重}\ |k_i|\lesssim M_i\ \text{的截断})✓$$
$$\Longrightarrow ⭐⭐⭐\ \boxed{\textbf{非对角点数}\ \asymp\prod_i\frac{|C|}{L_i}\ \ggg\ \textbf{对角点的}\ 1}✓✓✓$$
$$\qquad 📌\ \text{即：}\textbf{"对角塌缩"的图景不完整} —— \text{非对角模式在}\ \textbf{数量上压倒} \text{对角}✓✓✓$$

## §4 UB-3（部分）：总预算的标度（**$M_i\asymp M$、$L_i\asymp L$、$r$ 因子**）
$$\text{总贡献}\ \asymp\ \underbrace{\Big(\frac{|C|}{L}\Big)^{r}}_{\text{计数}}\times\underbrace{\frac{L^{r}}{|C|^{r/2}}}_{\text{每点}} \asymp\ L^{r}|C|^{-r/2}\min\Big(\frac{|C|}{L},M\Big)^{r}✓$$
$$\text{情形 (i)}\ |C|\le LM：\longrightarrow\ |C|^{r/2}\ \textbf{（随}\ |C|\ \text{递增）}✓$$
$$\text{情形 (ii)}\ |C|\ge LM：\longrightarrow\ \Big(\frac{LM}{|C|^{1/2}}\Big)^{r}\ \textbf{（递减）}✓$$
$$\Longrightarrow \boxed{\text{极大在交叉点}\ |C|\asymp LM \Longrightarrow \text{总贡献}\ \asymp\ (LM)^{r/2}}✓✓✓$$
$$\qquad ⚠️\ \text{故}\ \textbf{UB-3 未决}：\text{是否}\ (LM)^{r/2}\ \text{超出}\ \textbf{一维 Type-II／}\sqrt X\ \text{预算} \Longrightarrow \textbf{必须代入实际}\ \phi✓✓$$

## §5 判词
$$\boxed{\text{① UB-1}\ \textbf{非空}（\text{非对角驻点存在，条件显式}）⟹ \text{C2-b 的"仅对角"}\ \textbf{撤回}}✓✓✓$$
$$\boxed{\text{② UB-2}\ \textbf{完成}：\det H\ \text{精确}；\ \text{每点}\ \asymp\prod x_i/|C|^{r/2}；\ \text{计数}\ \asymp\prod\min(|C|/L_i,M_i)}✓✓$$
$$\boxed{\text{③ }\textbf{支配性反转}：\text{非对角点数}\ \asymp\prod|C|/L_i\ \textbf{压倒} \text{对角}\ 1\ \text{个}⟹ \textbf{对角塌缩图景不完整}}✓✓✓$$
$$\boxed{\text{④ UB-3}\ \textbf{未决}：\text{总贡献}\ \asymp(LM)^{r/2}\ \text{是否超一维预算}\ \textbf{须代入实际}\ \phi}✓$$

## §6 边界
$$\text{(i)}\ §1--§2\ \text{为}\ \textbf{初等微积分／线代}（\text{可逐行核}）✓✓；\ §3--§4\ \text{的}\ \asymp\ \text{为}\ \textbf{标度估计（未含常数）}✓；$$
$$\text{(ii)}\ ⚠️\ \textbf{未做} \text{：Poisson 权重的显式衰减率、Airy 退化支线、}\sum_{k}|{\det H_k}|^{-1/2}\ \text{的收敛性}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \text{"非空"}\ne\text{"有增益"}✓✓$$
