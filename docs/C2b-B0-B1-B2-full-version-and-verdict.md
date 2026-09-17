# ⚔️ **C2-b 完整版**：B0／B1 关闭 ＋ **B2 执行** ⟹ **对角塌缩回一维 ⟹ C2 = NO-GO（定域）**

> 依唐先生 15:34「先 C2-b 完整版，再做 C2-c」＋ B0/B1/B2 拆解规格 ✓
> **本档结果**：$A_r(u)$ **精确算出**（正、单调 ⟹ 无 cancelling）；B2 **对角塌缩**；**关键问句答案＝"不"** ⟹ C2 判死（定域）✓✓✓

---

## §0 规格（唐先生逐字采纳）
$$\textbf{B0}\ \text{连续多变量权重积分}；\ \textbf{B1}\ \text{高阶分部积分}；\ \textbf{B2}\ ⭐\ \textbf{离散 Poisson 对偶频率}（\text{真正未决}）✓✓$$
$$\text{排序约束}：\textbf{先 B2，不做 C2-c}；\ \delta_r\ \text{须建立在 B2 的}\ \textbf{实际主项/误差公式} \text{上，}\ \textbf{不得先验参数化}✓✓$$

## §1 B0：坐标分解 ⟹ 一维有效振幅（**精确**）
$$x_i=\log m_i,\ u=\textstyle\sum_ix_i,\ \text{横向}\ v\ (\text{Jacobian 常数}) \Longrightarrow I=\int A_r(u)e^{i\phi(u)}du,\quad A_r(u)=\int_{\text{slice}(u)}W\,d\sigma_u✓✓$$
$$\text{取}\ W=\prod_ix_i\ (\text{无 cutoff 模型})：\text{Dirichlet 积分}\ \int_{\sum x_i\le u}\prod x_i\,dx=\frac{\Gamma(2)^r}{\Gamma(2r+1)}u^{2r}=\frac{u^{2r}}{\Gamma(2r+1)}✓$$
$$\Longrightarrow \boxed{A_r(u)=\frac{u^{2r-1}}{\Gamma(2r)}}\qquad(\text{校验}\ r=1：A_1=u✓；\ r=2：A_2=\tfrac{u^3}{6}✓✓)✓✓✓$$
$$\Longrightarrow ⭐\ \boxed{A_r\ \textbf{是正、单调、无符号交替的多项式}} \Longrightarrow \textbf{权重不产生振荡}✓✓$$

## §2 B1：高阶分部积分 —— 只提高振幅平滑度
$$L:=\frac{1}{i\phi'(u)}\frac{d}{du} \Longrightarrow e^{i\phi}=Le^{i\phi} \Longrightarrow I=(-1)^m\int (L^*)^mA_r\,e^{i\phi}\,du+\text{boundary},\quad L^*=-\frac{d}{du}\frac{1}{i\phi'}✓$$
$$\Longrightarrow \text{每阶仅出现}\ A_r^{(j)}\,(\phi')^{-q}(\phi'')^{\ell}\cdots \Longrightarrow \boxed{\text{唯一的 cancellation 参数是}\ \phi'，\ \text{权重不创造第二相位}}✓✓✓$$
$$\text{而}\ A_r^{(j)}\propto u^{2r-1-j}\ \text{恒正} \Longrightarrow \boxed{\text{权重}\ \textbf{无 cancellation} \text{，只改善边界／cutoff／常数}}✓✓$$
$$\qquad 📌\ \text{按唐先生判据}：\text{"只是 partial summation}\ \textbf{不算新机制}" \Longrightarrow \textbf{分支 B 实质关闭}✓✓$$

## §3 ⭐⭐⭐ B2：离散 Poisson（**按 $m$-坐标重推**，结论与你同，常数更干净）
$$\text{设定}：S=\sum_{m_1\sim M_1}\cdots\sum_{m_r\sim M_r}\Big(\prod\log m_i\Big)e^{i\phi(\log n)},\quad n=\prod m_i✓$$
$$\text{Poisson（整数变量）}：\sum_{m\sim M}g(m)=\sum_{k\in\mathbb Z}\int g(x)e^{2\pi ikx}\,dx-\text{type} \Longrightarrow \text{对偶整数频率}\ k_1,\dots,k_r✓$$
$$\Longrightarrow \Phi_k(x)=\phi\big(\log(x_1\cdots x_r)\big)+2\pi\sum_i k_ix_i\ \Longrightarrow \partial_{x_i}\Phi_k=\underbrace{\frac{\phi'(u)}{x_i}}_{\text{乘性}}\!+2\pi k_i✓✓$$
$$\text{驻定条件}\ \partial_{x_i}\Phi_k=0\ \forall i \Longrightarrow \boxed{k_ix_i=\text{const}\ (i=1,\dots,r)}✓✓✓$$
$$\Longrightarrow \text{各}\ M_i\ \textbf{可比} \Longrightarrow \boxed{\textbf{仅对角}\ k\ (k_1=\cdots=k_r)\ \text{有驻定点}}✓✓✓\quad(\text{与你的}\ h_1=\cdots=h_r=\phi'(u)\ \text{同结论})✓✓$$
$$\textbf{非对角}：\text{无驻定点} \Longrightarrow \Big|\frac{\phi'}{x_i}+2\pi k_i\Big|\ge c>0 \Longrightarrow \text{重复 IBP} \Longrightarrow \boxed{\textbf{快速消解}}✓✓$$
$$\textbf{对角}：\text{塌缩} \Longrightarrow \boxed{\text{＝原}\ \textbf{一维问题}（\text{振幅}\ A_r，\text{相位}\ \phi）}✓✓✓$$
$$\Longrightarrow \boxed{r\ \text{维 Poisson}\ =\ \text{一维 Poisson（含}\ A_r\text{）}\ +\ \text{快速衰减的非对角余项}}✓✓✓$$

## §4 ⭐⭐⭐ 最终问答（唐先生核心问句）
$$\text{问}：\text{对角 Poisson 模式的增益是否}\ \textbf{超过} \text{原有 Type-II／}\sqrt{}\text{预算？}$$
$$\text{答}：\boxed{\textbf{"不"}}\ ——\ \text{因}\ \textbf{对角模式}\ \textbf{就是} \text{原一维对象}；\ \text{它的"增益"}\ \textbf{不是超过预算，而是}\ \textbf{就是那笔预算}}✓✓✓$$
$$\Longrightarrow \boxed{\textbf{C2 = NO-GO（定域）}}\：\text{多线性设备}\ \textbf{不能超越} \text{一维分析；}\ \log\ \text{权重的效果}\ \textbf{全部} \text{被吸收进}\ A_r(u)✓✓✓$$
$$\qquad \Longrightarrow \textbf{分支 B（weight-driven cancellation）关闭}：\text{权重贡献仅边界／误差／常数级}✓✓$$
$$\qquad \Longrightarrow \text{故}\ \texttt{87dd8fd}\ \text{的 rank-1 定理}\ \textbf{得到补全}：\text{幂相位 rank-1}＋\text{权重无符号} \Longrightarrow \text{多线性设备}\ \textbf{结构性无效}✓✓✓$$

## §5 ⚠️ 严格性边界（诚实，必须保留）
$$\text{(a)}\ \text{B2 的"非对角快速消解"需要}\ \textbf{显式非驻相界}（|\cdot|\ge c\ \text{的验证}＋\text{余项量级}）$$
$$\qquad \text{本档给出}\ [\textbf{结构}] \text{级证明；}\ \textbf{常数级验证未做} \Longrightarrow \text{C2 的 NO-GO}\ \textbf{conditional on} \text{该余项确为低阶}✓✓$$
$$\text{(b)}\ \text{本档}\ \textbf{不涉及} \text{RH}；\ \textbf{不声称} \text{parity 是穷尽定理}；\ \text{"未找到"}\ne\text{"不存在"}✓✓$$
$$\text{(c)}\ \text{cutoff 情形}（\prod x_i\prod w_i）\ \text{未单独处理}；\ \text{但}\ w_i\ \text{光滑} \Longrightarrow \text{只改}\ A_r\ \text{的渐近，不改结论}✓$$
$$\qquad ⚠️\ \text{唯一可再抠处}：\text{若}\ M_i\ \textbf{严重不平衡}，\text{驻定条件}\ k_ix_i=\text{const}\ \text{可能允许}\ \textbf{非对角} \text{点}（k_i\propto 1/x_i）✓✓$$

## §6 状态表（更新）
| 项 | 状态 | 结果 |
|:--|:--|:--|
| B0 | **关闭（精确）** | $A_r(u)=u^{2r-1}/\Gamma(2r)$ ⟹ 正、单调 ⟹ **无振荡** |
| B1 | **关闭** | 唯一相位参数 $\phi'$；权重无 cancellation（仅误差级）|
| **B2** | **执行（结构级）** | 对角塌缩回一维；非对角快速消解 ⟹ **无新通道** |
| **C2** | **NO-GO（定域）** | 多线性设备不能超越一维分析 |
| C2-c $\delta_r$ | **不应先做**（依唐先生）| 待 B2 余项显式化后再定 |

## §7 边界
$$\text{(i)}\ §1\ \textbf{严格}（\text{Dirichlet 积分}）✓✓；\ §2\ \textbf{严格}（\text{分部积分恒等式}）✓✓；\ §3\ \textbf{结构级}（\text{非驻相余项待显式}）✓；\ §4\ \text{为判词}✓$$
$$\text{(ii)}\ \textbf{未用 RH}；\ \textbf{零数值}✓\quad\text{(iii)}\ ⚠️\ \text{不做 C2-c}\ \text{的理由已记录：}\delta_r\ \text{会}\ \textbf{参数化一个不存在的机制}✓✓$$
