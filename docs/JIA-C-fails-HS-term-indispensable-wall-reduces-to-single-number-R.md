# ⚔️ **攻 (丙)**："只用 $\mathrm{tr}$ 与 $n_+$ 的秩下界" —— **不存在**；但墙被压成**一个数 $R$**

> 依唐先生 14:19「继续」；承接 `957187e` §5(丙) ✓
> **本档结果**：(丙) **不成立**（HS 项不可去掉）；但**副产品极硬**：主链的 $2/3$ **完全来自一个数** $R=\|\tilde G\|^2_{HS}/N$ ✓✓✓

---

## §1 为什么 (丙) 不成立：$\mathrm{tr}$ 与 $n_+$ **不足以排除极端构型**
$$\text{可用数据}：\mathrm{tr}\tilde G=(1+o(1))N,\qquad N\ge s_1+2s_2+2p,\qquad n_+(Q)\le p✓$$
$$\text{恒等式}：N=s_1+2s_2+2p\ \text{（归一化后）} \Longrightarrow s_1=N-2s_2-2p✓$$
$$\text{而}\ p\ \text{最大可达}\ N/2\ \text{（}\textbf{极端构型：全部为离线对}）\Longrightarrow \text{只用}\ \mathrm{tr},n_+\ \text{只能给}\ s_1\ge0✗✗$$
$$\Longrightarrow \text{前沿}\ \S7.2(a)\ \textbf{自陈}：\text{"in the extreme hypothetical configuration in which all zeros are off-line pairs, Prop 4.1 gives}\ \mathrm{rank}P=0,\ n_+(Q)\le N/2,\ \text{while Lemma 3.2}\ \textbf{would then force}\ \|\tilde G\|^2_{HS}\ge2N>\tfrac43N\ \text{；the contradiction shows only that at least two thirds of the zeros are not of this kind"}✓✓✓$$
$$\Longrightarrow \boxed{\text{HS 项是}\textbf{唯一} \text{的排除者} \Longrightarrow \text{(丙)}\ \textbf{不成立}}✓✓✓$$

## §2 ⭐⭐⭐ 但由此得到极硬的副产品：**$2/3$ 完全来自一个数**
$$\text{主链}：Ns_0+o(N)\ge\mathrm{rank}P_1\ge4\,\mathrm{tr}\tilde G-2N-\|\tilde G\|^2_{HS}✓✓$$
$$\text{代入}\ \mathrm{tr}\tilde G=N\ \text{与}\ \|\tilde G\|^2_{HS}=(R+o(1))N：\qquad \frac{s_0}{N}\ \ge\ 4-2-R\ =\ \boxed{2-R}✓✓✓$$
$$\text{前沿两个窗}：R(\psi_0)=\tfrac43\Longrightarrow 2-\tfrac43=\boxed{\tfrac23}；\ R(\psi_{MT})=c_{MT}^{-1}\Longrightarrow \boxed{0.6725}✓✓$$
$$\Longrightarrow \boxed{\text{整个方法的输出}\ =\ \textbf{一个数}\ 2-R\ ——\ \text{全部难度落在}\ R\ \text{上}}✓✓✓$$

## §3 ⭐⭐ $R$ 是什么：**离线平方质量**
$$\|\tilde G\|^2_{HS}=\mathrm{tr}(\tilde G^2)=\sum_i\lambda_i^2 \Longrightarrow \text{在线单零点贡献}\ \sum 1=s_1；\ \text{离线对贡献}\ \sum(\pm\lambda_\rho)^2=2\sum_{\rm off}\lambda_\rho^2✓✓$$
$$\Longrightarrow \boxed{\|\tilde G\|^2_{HS}\approx s_1+2\!\sum_{\rm off}\lambda_\rho^2} \Longrightarrow \text{墙}\ =\ \boxed{\text{无条件估计离线对平方质量}\ \sum\lambda_\rho^2}✓✓✓$$
$$\qquad ⭐\ \text{这是}\ \textbf{两体量}（\text{prime-pair 型}） \Longrightarrow \text{与}\ \S7.2(a)\ \text{的"need prime pairs"}\ \textbf{逐字吻合}✓✓$$

## §4 ⟹ 墙的最终形态（比"support>1"硬得多）
$$\boxed{\textbf{SUPPORT-1}\ \Longleftrightarrow\ \text{"无条件得到}\ R=\|\tilde G\|^2_{HS}/N\ \text{的更好上界"}}✓✓✓$$
$$\qquad\text{三条已知出路}：$$
$$\qquad\text{(i)}\ \text{输入 support}>1 \Longrightarrow \text{prime pairs} \Longrightarrow \text{已封}✗$$
$$\qquad\text{(ii)}\ \text{换窗改善}\ R \Longrightarrow \text{前沿已优化到 ceiling}\ 0.68185\ ✗$$
$$\qquad\text{(iii)}\ \text{换型使}\ \|\cdot\|^2_{HS}\ \text{只含在线部分} \Longrightarrow \text{D-GRAM 已封（Gram}\Rightarrow PSD\text{）}✗$$
$$\Longrightarrow ⚠️\ \text{三条都封；但}\ \textbf{墙现在是一个数}，\ \text{不是一团机制}✓✓✓$$

## §5 边界
$$\text{(i)}\ §1\ \text{的极端构型引前沿}\ \S7.2(a)\ \text{逐字}✓\quad\text{(ii)}\ §2\ \text{的}\ 2-R\ \text{为本档代数（}\mathrm{tr}=N\ \text{代入）}✓$$
$$\text{(iii)}\ §3\ \text{的}\ \mathrm{tr}(\tilde G^2)\ \text{分解为初等线代}✓\quad\text{(iv)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
$$\text{(v)}\ ⚠️\ R\ \text{的定义式含}\ o(1)\ \text{与归一化细节，}\ \text{本档未逐项核}✓$$
