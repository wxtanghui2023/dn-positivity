# ⚔️ **UB-3A/B 执行**：绝对质量**增长**（修正一处）＋ **相干性压缩到 $H_k$** ⟹ 钉死两个结构量

> 依唐先生 15:39「直接开 UB-3A/B，不选具体 $\phi$」✓
> **本档结果**：① 修正"$\sum k^{-2}$ 收敛⟹不增长"（**含权重后改变幂次**）；② 相位差**只依赖 $H_k$**；③ 钉死：**每模式权重**＋**$H_k$-水平集多重度**；④ ⭐ 得到**可引判据** $|\phi'|\gg\log X$✓✓✓

---

## §0 采纳的三条修正（唐先生）
$$\text{(a)}\ \text{贡献须}\ \textbf{含权重}\ W：|\mathcal C_k|\asymp W(x(k))\,|\det H_k|^{-1/2}|\mathfrak B_k|,\quad W=\prod_ix_i=\frac{|C|^r}{\prod_i|k_i|}✓✓$$
$$\text{(b)}\ \textbf{不得} \text{做绝对值乘法}：\text{须算}\ \sum_k\mathcal C_k\ (\text{含}\ e^{i\Phi_k})\ \text{而非}\ \sum_k|\mathcal C_k|✓✓$$
$$\text{(c)}\ \text{相位差}\ \textbf{只依赖}\ H_k✓\qquad(\text{见}\ §2)✓✓$$

## §1 ⭐ UB-3A：绝对质量 —— **含权重后幂次改变 ⟹ 增长**（含一处修正）
$$\text{单模式（唐先生式）}：\boxed{|\mathcal C_k|\asymp\frac{|C|^{3r/2}}{\prod_i|k_i|^2}\Big|1+\frac{C\phi''(u)}{2\pi}\sum_i k_i^{-2}\Big|^{-1/2}|\mathfrak B_k|}✓✓\qquad(\text{本档复核}\ \textbf{成立})✓$$
$$\text{可行窗口}：x_i=\frac{C}{k_i}\in[L_i,2L_i] \Longleftrightarrow \boxed{|k_i|\in\Big[\frac{|C|}{2L_i},\ \frac{|C|}{L_i}\Big]}✓✓$$
$$\text{窗口求和（}\textbf{关键}）：\sum_{|k_i|\in\text{窗口}}\frac1{k_i^2}\asymp\int_{|C|/2L}^{|C|/L}\frac{dk}{k^2}=\frac{2L}{|C|}-\frac{L}{|C|}=\frac{L}{|C|}✓✓$$
$$\Longrightarrow \sum_k|\mathcal C_k|\asymp|C|^{3r/2}\prod_i\frac{L_i}{|C|}\,[\ldots]^{-1/2}|\mathfrak B|=\boxed{\prod_iL_i\,|C|^{r/2}}✓✓\ \textbf{（随}\ |C|\ \textbf{增长）}✓$$
$$\qquad ⚠️\ 🔧\ \textbf{修正一处}：\text{"}\sum k^{-2}\ \text{收敛}\Longrightarrow \text{不增长}"\ \text{在}\ \textbf{不含权重} \text{时成立}：$$
$$\qquad\qquad \sum_{k}\frac{|\det H|^{-1/2}\text{-部分}}{\prod k_i}\asymp\Big(\int_{|C|/2L}^{|C|/L}\frac{dk}{k}\Big)^{r}=(\log2)^r\ \textbf{（真收敛）}✓✓$$
$$\qquad\qquad \text{但}\ W=\prod x_i=\prod\frac{C}{k_i}\ \text{又贡献}\ \prod(C/k_i) \Longrightarrow \textbf{多出}\ |C|^{r}\prod k_i^{-1}\ \text{因子} \Longrightarrow \textbf{幂次改变}✓✓$$
$$\Longrightarrow \boxed{\text{"数量多}\Rightarrow\text{贡献多"的断点在}\ \textbf{权重} \text{，不在计数}}✓✓✓$$

## §2 ⭐⭐⭐ UB-3B：相位差**只依赖 $H_k$**（唐先生 (c) 成立，本档给出显式）
$$\Phi_k^{\rm stat}=\phi(u)+2\pi\sum_ik_ix_i=\phi(u)+2\pi rC\quad(\text{用}\ k_ix_i=C)✓✓$$
$$u=CH_k,\ H_k:=\sum_i\frac1{k_i} \Longrightarrow \boxed{\Phi_k^{\rm stat}=\phi(CH_k)+2\pi rC}✓✓✓$$
$$\Longrightarrow \boxed{\Delta\Phi=\phi(CH_k)-\phi(CH_{k'})} \Longrightarrow \textbf{多维非对角驻点压缩为}\ H_k\ \textbf{上的一维相位问题}✓✓✓$$
$$\text{有效}\ H_k\ \text{范围}：\frac1{k_i}\in\Big[\frac{L_i}{|C|},\frac{2L_i}{|C|}\Big] \Longrightarrow \boxed{\eta=H_k\in\Big[\frac{\sum_iL_i}{|C|},\ \frac{2\sum_iL_i}{|C|}\Big]},\ \ \text{宽度}\ \asymp\frac{\sum_iL_i}{|C|}✓✓$$
$$\text{相位跨范围变化}：\Delta\Phi\asymp|\phi'|\cdot|C|\cdot\Delta\eta=2\pi|C|\cdot\frac{\sum_iL_i}{|C|}\cdot|C|=2\pi|C|\sum_iL_i\ \gg1✓✓✓$$
$$\qquad ⭐\ \Longrightarrow \textbf{情形 I（强振荡）}\ ——\ \text{非对角模式之间}\ \textbf{发生额外 cancellation}✓✓✓$$
$$\text{水平集结构（本档新钉死）}：H_k=\sum_i\frac1{k_i}\ \text{的}\ \textbf{埃及分数表示数}；\ \text{分辨尺度}\ \frac{1}{Q^2},\ Q\asymp\frac{|C|}{L} \Longrightarrow \#\{\text{不同}\ \eta\}\asymp\frac{|C|}{L}✓✓$$
$$\qquad \Longrightarrow \boxed{\text{多重度}\ m_\eta\asymp\frac{\#\text{元组}}{\#\text{值}}\asymp\Big(\frac{|C|}{L}\Big)^{r-1}}✓✓\qquad(\text{簇}\Rightarrow\text{对称元组})✓$$

## §3 相干和的规模（Weyl／C–S）
$$\sum_k\mathcal C_k=\sum_\eta\Big(\sum_{k:H_k=\eta}a_k\Big)e^{i\phi(C\eta)}\ \text{-型}；\ \text{绝对}\ \asymp\Big(\frac{|C|}{L}\Big)^{r}；\ \text{振荡（Weyl／C--S）}\asymp\Big(\frac{|C|}{L}\Big)^{r-1}\Big(\frac{|C|}{L}\Big)^{1/2}✓✓$$
$$\Longrightarrow \boxed{\text{相干总质量}\ \asymp\Big(\frac{|C|}{L}\Big)^{r-1/2}}\qquad\text{相对绝对大小增益}\ \asymp\boxed{\Big(\frac{L}{|C|}\Big)^{1/2}}✓✓$$
$$\qquad ⚠️\ \text{但}\ \Big(\frac{|C|}{L}\Big)^{r-1/2}\ \textbf{仍随}\ |C|\ \textbf{增长} \Longrightarrow \textbf{乙不能就此关闭}✓✓\quad(\text{与唐先生"末步须具体}\ \phi"\ \text{一致})✓$$

## §4 ⭐⭐⭐ 判词 ＋ **可引判据**
$$\boxed{\text{① UB-3A}\ \textbf{完成}：绝对质量}\ \asymp\prod_iL_i|C|^{r/2}\ \textbf{增长；断点在权重}}✓✓$$
$$\boxed{\text{② UB-3B}\ \textbf{完成（结构部分）}：相位}\Rightarrow\ H_k\ \text{一维问题；跨范围变化}\ 2\pi|C|\sum L_i\gg1\Rightarrow\textbf{强振荡}✓✓}$$
$$\boxed{\text{③ 两个结构量已钉死}：\text{每模式权重}\ \frac{|C|^{3r/2}}{\prod k_i^2}\ \big|\ \text{水平集多重度}\ m_\eta\asymp\Big(\frac{|C|}{L}\Big)^{r-1}}✓✓✓$$
$$\boxed{\text{④ 乙}\ \textbf{未关闭}；\text{末步＝}\textbf{一个比较}：\Big(\frac{|C|}{L}\Big)^{r-1/2}\ \text{vs 一维 Type-II／}\sqrt X\ \text{预算}}✓✓$$
$$\Longrightarrow ⭐\ \boxed{\textbf{可引判据}：\text{危险}\iff\frac{|C|}{L}\gg1\iff\boxed{|\phi'|\gg\log X}}}✓✓✓$$
$$\qquad(\text{因}\ |C|=\frac{|\phi'|}{2\pi},\ L\asymp\log M\asymp\log X)✓$$
$$\qquad 📌\ \text{故：}\textbf{相位导数远大于对数尺度} \text{时，非对角相干质量才可能威胁一维预算}✓✓✓$$

## §5 边界
$$\text{(i)}\ §1\ \text{的窗口求和／}\ §2\ \text{的相位差为}\ \textbf{严格}（\text{初等}）✓✓；\ §2\ \text{的水平集计数为}\ [\textbf{结构}] \text{级（分辨尺度}\ 1/Q^2\ \text{为启发）}✓$$
$$\text{(ii)}\ §3\ \text{的相干和上界为}\ \textbf{标度级}（\text{未含}\ \mathfrak B_k\ \text{与层间相位细节}）✓；\ \text{未做：Airy 退化支线、}\mathfrak B_k\ \text{显式}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \textbf{不声称} \text{乙已关闭或已开启}✓✓$$
