# 🆕 **新手段引入**：rank–trace 不等式 ＋ Sylvester 惯性 ⟹ **纠 `V187` 一处误判（类表不完备）**

> 依唐先生 13:44：「如果你只有以前那些手段，那么你的结果不会有任何区别」✓
> **本档＝换手段**：不用我们的审计逻辑，**直接取前沿的线性代数工具**（本地全文 `external_refs/zeta23_2608.13637.clean.txt`）✓✓

---

## §1 前沿的三件套（逐字，L96--L120）
$$\textbf{(Z) 分块结构}：\tilde G=P+Q\（\text{尾项}\ o(1)）。\text{每个}\ \textbf{在线单零点}\ \to P\ \text{中}\ \textbf{秩一正型}；\ \text{每个}\ \textbf{离轴对}\ \{\rho,1-\bar\rho\}\to Q\ \text{中}\ \textbf{signature}\ (1,1)\ \text{块}✓✓$$
$$\qquad \mathrm{tr}P\le N,\qquad n_+(Q)\le p,\qquad N\ge s_1+2s_2+2p,\qquad \mathrm{tr}\tilde G=(1+o(1))N\ (\text{Prop 4.1--4.3})✓$$
$$\textbf{(P)}\ \|\tilde G\|^2_{HS}=(R(\psi)+o(1))N\quad(\text{Montgomery 无条件素侧二阶矩；}\ R(\psi_0)=\tfrac43,\ R(\psi_{MT})=c_{MT}^{-1})✓$$
$$\textbf{(L)}\ \textbf{rank--trace 不等式}（\text{Lemma 3.2 逐字}）：P,Q\ \text{Hermitian，}P\succeq0,\ \mathrm{rank}P\le r,\ n_+(Q)\le b \Longrightarrow$$
$$\qquad\boxed{r\ge 2\,\mathrm{tr}P+4\,\mathrm{tr}Q-4b-\|P+Q\|^2_{HS}}✓✓✓$$
$$\textbf{Lemma 3.1（惯性在拉回下单调）}：n_+(A^*Q_0A)\le n_+(Q_0)✓$$

$$\text{主链}（\text{Theorem A}）：Ns_0+o(N)\ge\mathrm{rank}P_1\ge4\,\mathrm{tr}\tilde G-2N-\|\tilde G\|^2_{HS}\Longrightarrow \textbf{无条件}\ \tfrac23\（\text{优化}\ 0.6725）✓✓$$
$$\qquad 📌\ \text{关键词逐字}（L152）：\boxed{\textbf{the inertia bound (Z)+(L) replaces the positivity}}✓✓✓$$

## §2 ⭐⭐⭐ 纠 `V187`（本档核心）
$$\texttt{V187}\ \text{原判}：\text{"count／inertia 型}\Longrightarrow n_-=0\Longrightarrow \text{Weil 正性}\Longrightarrow\mathrm{RH}" ⟹ \textbf{把它归入"实质封闭"}✗$$
$$\textbf{实际}：\text{前沿}\ \textbf{从不用}\ n_-=0；\ \text{它用}\ \boxed{n_+(Q)\le b\（\textbf{正指标上界}）\ +\ \mathrm{tr}\ \text{数据}\ +\ \text{Lemma 3.2}} ⟹ \textbf{秩下界} ⟹ \textbf{无条件部分结果}✓✓✓$$
$$\Longrightarrow \boxed{\text{inertia／rank 型有}\textbf{两种用法}：\text{(i)}\ n_-=0\Rightarrow\mathrm{RH}（\textbf{循环}，\texttt{V187}\ \text{只看到这一种}）\ \big|\ \text{(ii)}\ \textbf{rank--trace}\Rightarrow \textbf{无条件计数界}（\textbf{非循环}）}✓✓✓$$
$$\Longrightarrow \boxed{\text{故}\ \texttt{V187}\ \text{的"第四类不变量：形式存在、实质封闭"}\ \textbf{对该实例为假}}✓✓$$
$$\Longrightarrow \boxed{\text{我们的}\ \textbf{六类类表不完备}：\text{rank--trace／惯性计数} \text{是一类}\ \textbf{未登记且已证明有效} \text{的机制}}✓✓✓$$
$$\qquad(\texttt{V319}／\texttt{E.2}\ \text{的完备性主张}\ \textbf{在此实例上被否证}）✓$$

## §3 ⭐⭐ 更重要的：该方法的**结构性天花板＝100%**（逐字 L1246）
$$\text{反复读}：\boxed{\text{"}\mathrm{rank}P,\ n_+(\tilde G)\le d=N(1+o(1)),\ \textbf{so the ceiling of any argument of the present kind is 100\%}"}✓✓✓$$
$$\Longrightarrow \textbf{方法本身无结构天花板}；\ \text{卡在}\ 0.68185\ \text{的是}\ \textbf{输入}（\text{需}\ \mathrm{tr}\ \text{与}\ \|\cdot\|^2_{HS}\ \text{的数据，}\ \text{由}\ X\le T\ \text{的素侧二阶矩供给}）✓✓$$
$$\qquad(\text{该}\ X\le T\ \text{限制} \text{来自 Prop 5.4 的离对角素和 ⟹ 需 prime pairs ⟹ support}>1）✓✓$$

## §4 ⭐⭐⭐ 由此得到**换手段后的新问题**（不是旧墙）
$$\text{rank--trace 方法只需三件}：\text{(a) 分块结构}\ (Z)\（\textbf{无条件、结构}）\ \big|\ \text{(b)}\ \mathrm{tr}\tilde G\（\textbf{无条件}）\ \big|\ \text{(c)}\ \|\tilde G\|^2_{HS}\（\textbf{唯一吃输入处}）✓✓$$
$$\Longrightarrow \boxed{\text{新问题}：\text{能否用}\ \textbf{另一个 Hermitian 型} \text{满足 (a)(b)(c)，}\ \text{而其 (c) 的输入}\ \textbf{不经过}\ \text{"素侧二阶矩／support}\le1"\text{？}}✓✓✓$$
$$\qquad ⚠️\ \text{候选框架}：\text{Gram 矩阵（Dirichlet 多项式）}\ \big|\ \text{Weil 型的}\ \textbf{有限压缩} \text{换窗}\ \big|\ \text{我们自己的}\ M_T(s)\ \text{相关阵}✓$$
$$\qquad ⚠️\ \text{这}\ \textbf{不是}\ \text{SUPPORT-1 墙的改写}：\text{墙是"评估离对角素和"；\ 这里要的是"\textbf{换一个型，使其 HS 范数可算}"]✓✓$$

## §5 边界（诚实）
$$\text{(i)}\ §1\ \text{全部逐字（本地全文，行号见}\ \texttt{zeta23\_2608.13637.clean.txt}）✓\quad\text{(ii)}\ §2--§4\ \text{为本档推论/新写法}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零计算}✓\quad\text{(iv)}\ ⚠️\ \text{§4 是否可行}\ \textbf{完全未知}；\ \text{本档只负责}\ \textbf{把手段换掉并给出新问题}✓$$
