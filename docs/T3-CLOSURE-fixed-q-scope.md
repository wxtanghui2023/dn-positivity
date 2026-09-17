# T3 **CLOSURE** · 固定相位模数层下的 $\ell_2$-侧振荡改造（**严格限定作用域**）

> 依唐先生 2026-09-17 09:51 指令：**不写成"绝对穷尽"**，而写成**严格限定作用域的 closure**，以免日后一句"你漏了某个 conductor/gcd 情形"就推翻全部 ✓
> 归档形式：$\boxed{\mathrm{T3\ Closure}=\mathrm{DEAD}_{\mathrm{fixed\text{-}q}}+\mathrm{R2,R3,R4\ Audit\ Residuals}}✓$（**而非** $\mathrm{T3}=\mathrm{DEAD\ absolutely}$）✓✓

---

## 0. ⭐ 作用域（scope，**逐字**）

$$\boxed{\text{在保持 BC 的}\ (4.10)\text{--}(4.29)\text{、原 C--S 组织以及}\ q=\mathfrak p_1n_1'\ \text{这一固定相位模数层的前提下，}}$$
$$\boxed{\text{不存在来自}\ \ell_2\text{-侧重新组织的固定幂级增益。}}✓✓✓$$

$$\textbf{等价表述（更准确）}：\ \text{不是"BC 再也不可能改进"，而是}$$
$$\qquad\boxed{\text{在}\ \textbf{不改变"平方所作用的变量"}、\textbf{不改变相位模数}\ q=\mathfrak p_1n_1'、\textbf{不引入新外部算术结构} \text{的前提下，}}$$
$$\qquad\boxed{\ell_2\text{-侧四种主要振荡改造路径}\ \textbf{已经没有固定幂级出口}}✓✓$$

---

## 1. T3-C1 · **单纤维振荡失败**

$$X\asymp\frac{L}{\mathfrak p_2\mathfrak q_2},\qquad q=\mathfrak p_1n_1'\asymp\frac{N}{\mathfrak p_2}\quad(\text{由}\ \mathfrak p_1\mathfrak p_2n_1'\in\mathcal N)✓$$
$$\Longrightarrow\ \frac{X}{\sqrt q}\asymp\frac{L}{\mathfrak q_2\sqrt{\mathfrak p_2N}}\qquad\xrightarrow{\text{balanced/optimal}\ L^*\asymp N^{1/10}}\qquad \frac{X}{\sqrt q}\ll N^{-2/5}✓✓$$
$$\Longrightarrow\ \text{单纤维 Weil 型平方根抵消}\ \textbf{不能} \text{提供所需固定幂增益}✓\quad(\shortfall=\tfrac{\sqrt N}{L}=N^{2/5})✓$$

## 2. T3-C2 · **同模数聚合失败**

$$\text{同}\ \ell\text{-轴聚合}：K_{\max}\lesssim\frac LX=\mathfrak p_2\mathfrak q_2\ \Longrightarrow\ \text{最有利点}\ O(1)\ll N^{2/5}✓$$
$$\text{二维 phase-lattice 聚合（}d\ \text{与}\ \tilde\ell_2\text{）}：(\text{4.19})\ \text{相位对}\ (d,\overline{\tilde\ell_2})\ \textbf{双线性}，\ \text{完整双和}\ \textbf{恒为零} ⟹ \text{真实相消}\ \textbf{存在}✓$$
$$\qquad\text{但}\ \text{gain}\asymp L^{1/2}N^{-1/4}\ \Longrightarrow\ \text{阈值仍}\ L\gg N^{1/2}✓$$
$$\Longrightarrow\ \boxed{\text{aggregation}\ \ne\ \text{conductor reduction}}✓✓\quad\text{（聚合改变的是}\ \textbf{项数组织}，\ \text{不是 conductor}）✓$$

## 3. T3-C3 · **预先 partial diagonal 没有新自由度**

$$\text{所有可从}\ (d,\tilde\ell_2,d',\tilde\ell_2')\ \text{之间提取的联合算术关系，最终都落入已存在的一层}：$$
$$\qquad \tilde\ell_2'd-\tilde\ell_2d'\quad\big|\quad u\quad\big|\quad v\quad\big|\quad\Delta✓$$
$$\Longrightarrow\ \boxed{\text{partial diagonal}\ \subseteq\ \sigma\big(u,\ v,\ \Delta,\ \text{existing coprimality}\big)}✓✓$$
$$\qquad\text{（}\textbf{比"partial diagonal DEAD"更严谨}：\ \text{若"新"partial diagonal 只是这些量的重新分类，则}\ \textbf{未产生新的 C--S 可用约束}）✓$$
$$\qquad\text{坍缩点逐字}：\ \text{partial diagonal}\iff\text{行列式的类}\iff u,v\ (\text{或}\ \Delta)\ \text{的类} \Longrightarrow \textbf{BC 的 longer diagonal 已含此层}✓$$

## 4. T3-C4 · **真正降 conductor 的路线失败**（**最关键一层**）

$$\text{在}\ q=\mathfrak p_1n_1'\ \text{且}\ \boxed{(\mathfrak p_1,n_1')=1}（\text{A1 已证：由}\ (\ell_1,n_1'n_2'b\vartheta)=1\ \text{与}\ \mathfrak p_1\mid\ell_1\text{）之后}：$$
$$\qquad\text{CRT 分解}\ \textbf{本身} \text{不会降低 conductor}✓$$
$$\text{只有出现某个}\ q_0\mid q,\ q_0\gg N^\delta\ \text{使}\ \textbf{联合相位在}\ q_0\ \text{上真实退化}，\ \text{才可能得到}\ \sqrt q\to\sqrt{q/q_0}✓$$

$$\textbf{A1--A4 的审计}\ \textbf{没有找到} \text{这样的}\ q_0：$$
$$\qquad\boxed{\text{CRT factorization is not conductor reduction}}✓✓$$
$$\qquad\boxed{\text{所有已发现的}\ q_0\ \text{要么}\ \le L，\ \text{要么只是特殊参数情形}（\mathfrak p_1=1），\ \text{要么就是已由}\ u\ \text{支付的约束}}✓✓$$

$$\text{（}\textbf{注意}：\ \text{此处}\ \textbf{只写}\ q_0\le L，\ \textbf{不写}\ q_0\ll L^{o(1)}\text{——后者}\ \textbf{未证}，\ \text{见 R2}）✓✓$$

---

## 5. ⚠️ **审计残项**（R2/R3/R4，**明确未证，独立于主结论**）

$$\textbf{R2（唯一可能直接动摇 C4 的逻辑节点，}\textbf{最值得补}）$$
$$\qquad\text{C4 的}\ q_0\ \text{上界}\ \textbf{不能} \text{由}\ q_0\le L\ \text{推到}\ L^{o(1)}；\ \text{须证}\ \gcd(d,\mathfrak p_1n_1')\ll L^{o(1)}\ \text{（在有效求和域上）}✓$$
$$\qquad\Longrightarrow\ \textbf{若存在允许的}\ d\ \text{使}\ \gcd(d,q)\asymp L^\eta\ (\eta>0)\ \text{则}\ \textbf{C4 须重审}✓✓$$

$$\textbf{R3}：\ a_1,\ \vartheta\ \text{与}\ q\ \text{的}\ \textbf{完整} \text{互素条件未核}✓$$

$$\textbf{R4}：\ (4.10)\ \text{的}\ \textbf{全部} \text{coprimality／divisibility 条件未逐条穷举}✓$$

$$\textbf{其余（沿用）}：\ \text{R1}\ (\mathfrak p_1,n_1')=1\ \text{的推导已核}✓；\ \textbf{未用 RH；零数值}✓$$

---

## 6. 五段总账（BC 原架构内部改造空间状态）

$$\begin{array}{c|l|l}
&\text{段}&\text{结论}\\
\hline
\text{T1}&\text{没有现成更强的 spectral engine}&\text{BC 全无谱机器（Kuznetsov／Maass／Petersson／大筛 全 0 命中）}\\
\text{T2}&\text{现有 counting／divisor ledger 无固定幂 slack}&N_2=L^{2+o(1)}；divisor alignment 无幂次 saving\\
\text{T3-1B/C/A}&\ell_2\text{-侧振荡无法制造新的 fixed-power gain}&4\ \text{层逐一 DEAD（固定}\ q\text{）}\\
\end{array}✓✓$$

$$\Longrightarrow\ \boxed{\text{BC 原架构}\ \xrightarrow{\ T1,\ T2,\ T3\ }\ \textbf{内部改造空间基本封闭}}✓✓$$

---

## 7. 下一步：**(甲) 已具备意义**

$$\text{问题已从}\ \boxed{\text{"还能不能在 BC 里面抠一点}\ L^\delta\text{？"}}\ \text{变成}\ \boxed{\text{如果不改变估计本身，}\ \textbf{改变什么对象被平方}？}✓✓$$
$$\text{这与}\ \text{DFI}\to\text{BC}\ \text{的历史性}\ \tfrac1{48}\to\tfrac1{20}\ \text{的机制}\ \textbf{正好对应}：\ \text{真正可能产生新指数之处}\ =\ \textbf{C--S 的变量组织}，\ \text{而非继续榨 Weil}✓✓$$

$$\textbf{建议顺序}：\ \text{先（甲）——在 BC 内部做一次真正的架构变换实验；}\ \text{只有（甲）也被证明必须退化回已审机制，才有充分依据转向（丙）离开 BC}✓$$
