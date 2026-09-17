# ⚫ **W5-DEAD**（正式关闭）· 第四类候选空间的结构性覆盖 ＋ **第四类收紧定义 (A)--(E)**

> 依唐先生 12:59 指令：**W5-DEAD**（升级自"工具失效"）；下一步**开 W4** ✓
> **已查地图** ✓（`V186`／`V187`／`V188`／`W5-1`／`K2-E''`／`C-29`／`C-30`）✓

---

## §0 判词
$$\boxed{\textbf{W5-DEAD}}✓✓\qquad\text{理由}\ \textbf{不是}"没想出第四类"，\ \text{而是}\ \textbf{完成了候选空间的一次结构性覆盖}✓✓$$

## §1 唯一像"第四类"的候选：**非线性主子式**
$$\text{取带限测试向量族}\ v_0,\dots,v_k，\ G_{ij}(T):=Q_T(v_i,v_j)✓$$
$$\boxed{\Delta_2(T)=G_{00}G_{11}-G_{01}^2}\qquad\text{或一般}\ \boxed{\Delta_k(T)=\det(G_{ij})_{0\le i,j\le k}}✓$$
$$\text{形式上满足三件事}：\textbf{非线性}（\text{非}\ Q_T\ \text{的线性组合}）\big|\ \textbf{多层}（k\ \text{可增}）\big|\ \textbf{selection-like}✓$$
$$\qquad(\text{文献背景}：\text{确有工作把}\ \det(L_{i+j})_{0\le i,j\le k}\ge0\ \text{作为 RH 的非线性条件}\ ——\ \text{唐先生引})✓$$

## §2 ⭐⭐⭐ 一行审计
$$G(T)=\sum_j\lambda_j(T)|\langle v,e_j\rangle|^2;\qquad \text{离轴对}\ \{\rho,1-\bar\rho\}\ \text{给}\ \lambda_+>0\ \text{与}\ \lambda_-<0 \Longrightarrow G=G_+-G_-✓$$
$$\boxed{\{\Delta_k\ge0\}_{k\ge1}\iff G\succeq0\iff n_-(G)=0\iff\text{Weil 正性}\iff\mathrm{RH}}✓✓✓$$
$$\Longrightarrow\ \text{撞}\ V187\ \text{的墙（}\textbf{inertia 通道}）✓✓$$

## §3 ⭐⭐ 它**不产生上界**
$$G=\operatorname{diag}(a,-b),\ a,b>0：\ \operatorname{tr}G=a-b\ \text{可能}>0（\text{看不见}）；\ \det G=-ab<0（\textbf{能看见}）✓$$
$$\qquad\text{但}\ \det G<0\ \text{只给}\ n_-\ge1，\ \textbf{不给}\ b\ll\varepsilon_T✓✗$$
$$\text{要}\ b\ll\varepsilon_T：\text{须}\ \text{①}\ a\ \text{的下界}（\text{正性／谱信息}）\ ＋\ \text{②}\ |\det G|\ \text{的上界}（\text{majorant／显式幅度}）✓$$
$$\Longrightarrow\ \boxed{\text{立刻回到}\ \textbf{W3}\ \text{或}\ \textbf{W6}}✓✓\quad(\text{与}\ \text{W5-1}\ \textbf{完全闭合})✓$$

## §4 ⭐⭐ 高阶 determinant **逃不出去**
$$G=U\operatorname{diag}(\lambda_1,\dots,\lambda_r)U^*：\ \text{全部 principal minors}\ge0\iff\lambda_j\ge0\ \forall j✓$$
$$\qquad\text{只要有一个}\ \lambda_-<0，\ \textbf{某个有限阶 minor 就暴露它} \Longrightarrow \boxed{\{\Delta_k\ge0\}_{k\ge1}\iff n_-=0}✓✓$$
$$\Longrightarrow\ \text{加层数}\ \textbf{不是加信息}，\ \text{而是把}\ \textbf{count／inertia}\ \text{逐渐完整恢复}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{"非线性"本身不是第四类}}✓✓✓$$

## §5 Fredholm determinant 同样被排除
$$D_T(\lambda)=\det(I+\lambda K_T)=\prod_j(1+\lambda\lambda_j);\quad \log D_T(\lambda)=\sum_{m\ge1}\tfrac{(-1)^{m+1}}m\lambda^m\operatorname{Tr}(K_T^m)✓$$
$$\qquad\text{看似多层，}\ \textbf{但仍把全部谱信息乘起来}；\ \text{排除负谱}\ \textbf{仍是在建"谱实性／正性／零点位置"的等价条件}✓$$
$$\Longrightarrow\ \boxed{\text{Fredholm determinant}\to\textbf{Deninger／HP determinant 墙}}，\ \text{不是新的 W5 通道}✓✓$$

## §6 ⭐ "第四类"的**收紧定义**（照录唐先生）
$$\boxed{\mathcal I_T\ \text{须同时满足}：\begin{cases}\text{(A)}\ \text{非线性／多层／范数型}\\\text{(B)}\ \textbf{不等价于}\ G_T\succeq0\\\text{(C)}\ \textbf{不需} \text{显式公式计算绝对幅度}\\\text{(D)}\ \textbf{有独立的算术上界／递推／压缩律}\\\text{(E)}\ \text{该律对}\ \beta>\tfrac12\ \text{给出 selection strength}\end{cases}}✓✓$$
$$\qquad\textbf{尤其 (D)}：\text{没有 (D)}\Longrightarrow\ \text{所谓"第四类"只是}\ Q\succeq0\to\det Q\ge0／\det_2Q\ge0／\|Q\|_p／\text{Hankel minors}$$
$$\qquad\Longrightarrow\ \text{即已明确拒绝的}\ \boxed{\textbf{POS 重写}}✓✓$$

## §7 候选空间覆盖（本档完成）
$$\begin{array}{c}\text{Gram determinant}\\\text{Hankel determinant}\\\text{total positivity}\\\text{Fredholm determinant}\\\text{Schatten／norm-type spectral quantities}\end{array}✓$$
$$\text{只要其"选择能力"来自}\ \textbf{谱负方向本身} \Longrightarrow \text{落}\ \textbf{inertia／count} ✓$$
$$\qquad\text{把 count 转成}\ n_-=0 \Longrightarrow \mathrm{RH}；\ \text{把负方向}\ \textbf{大小} \text{压下来} \Longrightarrow \text{须独立幅度控制} \to \textbf{W3}\ \text{或}\ \textbf{W6}✓✓$$
$$\Longrightarrow\ \text{与}\ \textbf{Input strength}\ne\textbf{selection strength}（K2\text{-E}''）\ \textbf{完全闭合}✓✓$$

## §8 边界
$$\text{(i)}\ §1\ \text{的文献引为唐先生提供（本档\textbf{未核原文}}）✓\quad\text{(ii)}\ §2--§5\ \text{为初等线性代数（可逐行核）}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
