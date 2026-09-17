# ⚔️ **攻 $R$**：$R=1+$**离对角质量**$/$N；而 0.68185 只是**那一族**的天花板

> 依唐先生 14:20「继续」；承接 `32c9ec1`（墙＝一个数 $R$）✓
> **本档结果**：$R$ 的**结构分解**＋**关键开口**：前沿优化的是**调制窗族**；**换压缩族可能降低离对角质量**✓✓✓

---

## §1 $R$ 的结构分解（由块结构直接读出）
$$\text{在线单零点}：\text{特征值}\ +1\（\text{rank-one，trace}\ 1）\Longrightarrow \text{贡献}\ 1\ \text{于}\ \mathrm{tr}(\tilde G^2)✓$$
$$\text{离线对}\ \{\rho,1-\bar\rho\}：\text{signature}\ (1,1)\ \text{块，特征值}\ \mu_+>0>\mu_-，\ \text{trace}\ \mu_++\mu_-=2\（\text{归一化）}✓✓$$
$$\qquad \|\tilde G\|^2_{HS}\ \text{含}\ \mu_+^2+\mu_-^2=2+2t_\rho^2\（t_\rho:=\tfrac{\mu_+-\mu_-}{2}=\textbf{离线位移量}）✓✓$$
$$\Longrightarrow \boxed{\frac{\|\tilde G\|^2_{HS}}{N}\ =\ 1\ +\ \frac{2}{N}\sum_{\rm off}t_\rho^2\ +\ (\text{重数项})\ =\ 1\ +\ \text{（离对角质量}/N）}✓✓✓$$
$$\qquad ⭐\ \text{故}\ R-1\ =\ \textbf{压缩本身的代价} \Longrightarrow R=4/3\ \text{即}\ \tfrac{2}{N}\sum t_\rho^2=\tfrac13✓✓$$
$$\qquad ⚠️\ \text{关键}\：\text{这个}\ \tfrac13\ \textbf{不是} \text{离线零点的证据}，\ \text{而是}\ \textbf{窗／压缩的几何量}✓✓$$

## §2 前沿优化的是**哪一族**（逐字口径）
$$\text{前沿}\ \S1\ \text{逐字}：\text{"We restrict}\ W\ \text{to a family of}\ d\sim N(T,2T)\ \textbf{modulated copies of a fixed window}\ \psi\ \text{, equispaced through}\ [T,2T]"✓✓$$
$$\Longrightarrow \text{他们优化的是}\ \textbf{窗口选择}（\text{indicator}\to\text{Montgomery--Taylor}）：R(\psi_0)=\tfrac43,\ R(\psi_{MT})=c_{MT}^{-1}✓✓$$
$$\Longrightarrow \text{0.68185}\ =\ \textbf{该族} \text{（调制窗族）的天花板}✓✓\qquad(⚠️\ \textbf{不是} \text{一切压缩族的天花板})✓$$

## §3 ⭐⭐⭐ 由此得到的开口
$$\boxed{\text{开口}：\textbf{换压缩族}（\text{测试函数族／配对方式}），\ \text{目标}\ \mathrm{tr}(\tilde G^2)\ \text{更小}，\ \text{而输入仍只需}\ \text{support}\le1}✓✓✓$$
$$\text{理由}：R-1\ \text{是}\ \textbf{压缩的几何代价}；\ \text{前沿只在}\ \text{"固定窗的调制"}\ \text{这一族内最小化它}✓✓$$
$$\text{待答}：\text{是否存在压缩族使}\ \frac{2}{N}\sum t_\rho^2\ \text{无条件}<0.317\（\text{即}\ 2-R>0.68185）✓✓$$

## §4 ⭐⭐ 与今日 W6-majorant 的对接（两条线在此会合）
$$\mathrm{tr}(\tilde G^2)=\sum_{i,j}|\tilde G_{ij}|^2 \Longrightarrow \text{降低它}\ \textbf{＝控制压缩的}\ \textbf{离对角项}✓✓$$
$$\text{而今日 W6-majorant 的卡点}\ \textbf{正是} \text{"离对角素和的控制（MV 步）"}✓✓✓$$
$$\Longrightarrow \boxed{\text{两条线会合}：\ \text{SUPPORT-1}\ \text{的}\ R\text{-形态}\ \equiv\ \text{W6 的 MV-离对角控制}}✓✓✓$$
$$\qquad ⭐\ \text{这不是"又是同一堵墙"，而是}\ \textbf{两条独立路径指向同一可优化泛函}✓✓$$

## §5 攻击计划（可执行）
$$\text{① 参数化压缩族}：\text{测试函数}\ \{\psi_i\}\ \text{的}\ \textbf{一般族}（\text{非固定窗调制}）✓$$
$$\text{② 目标泛函}：\text{最小化}\ \mathrm{tr}(\tilde G^2)\ \text{的}\ \textbf{无条件上界}（\text{输入}\ \text{support}\le1\ \text{固定}）✓✓$$
$$\text{③ 判据}：\text{若能得}\ 2-R>0.68185 \Longrightarrow \textbf{前沿天花板被突破}✓✓✓$$
$$\qquad ⚠️\ \text{若证得"任何族都}\ \ge0.68185"\ \Longrightarrow \text{该天花板}\ \textbf{升级为定理}（\text{也是收获}）✓✓$$

## §6 边界
$$\text{(i)}\ §1\ \text{的分解用块结构}\ (Z)\ \text{与归一化}\ \mathrm{tr}\tilde G=N\ \text{（前沿逐字）}✓\quad\text{(ii)}\ §2\ \text{为前沿}\ \S1\ \text{逐字}✓$$
$$\text{(iii)}\ §3--§5\ \text{为本档}\ \textbf{开口假设}，\ \textbf{未证}✓✓\quad\text{(iv)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
$$\text{(v)}\ ⚠️\ \text{0.68185 的"仅该族"性质}\ \textbf{未逐字核}（\text{前沿}\ \S7.2\ \text{口径为"bandwidth-one certificate-class ceiling"，}\text{可能已含更广})✓$$
