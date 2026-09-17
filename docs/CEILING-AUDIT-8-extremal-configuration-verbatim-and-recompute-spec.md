# 🎯 **审前沿天花板（第八步）**：极值构型**逐字取到** ⟹ **自己重算的精确规格**

> 依唐先生 15:08「继续」；承接 `50a35bc`（审计数据侧闭环）✓
> **本档结果**：前沿把对抗极值构型**显式写出**；由此确定**重算＝证书侧上确界问题**✓✓✓

---

## §1 ⭐⭐⭐ 极值构型（`§7.2(b)` 逐字）
$$\text{"$\frac23N$ mutually orthogonal simple on-line zeros together with $\frac16N$ on-line doubles realise}\ \mathrm{tr}=N,\ \|\cdot\|^2_{HS}=\frac43N,\ s_1=\frac23N,\ N_d=\frac56N\ ——\ \text{the same extremal configuration as in Montgomery's RH argument."}✓✓$$
$$\text{"Replacing the doubles by off-line pairs of depth}\to0\ (\textbf{spectrally the same})\ \text{gives the extremal for Theorem A, with}\ s_1+s_2=\frac23N\text{"}✓✓✓$$
$$\Longrightarrow \textbf{对抗方机制}：\text{把"在线 double"换成"深度}\to0\ \text{的离线对"}——\ \textbf{谱不变} \text{（形状因子逐字相同）}\ \text{而}\ s_1\ \text{不变}✓✓$$
$$\qquad 📌\ \text{这正是}\ \textbf{谱盲性} \text{的对抗利用：}\textbf{保谱变换} \text{降低简单点比例}✓✓✓$$
$$\text{数值核对（本档）：}\mathrm{tr}=\tfrac23N+\tfrac16N\cdot2=N✓；\ \|\cdot\|^2_{HS}=\tfrac23N+\tfrac16N\cdot4=\tfrac43N✓✓；\ N_d=\tfrac23+\tfrac16=\tfrac56N✓✓$$

## §2 ⭐⭐ 由此确定证书的方向（关键推论）
$$\text{证书有效（逐字）}：c_0+\sum_js_jr(j/N)\le p \Longrightarrow v=c_0+\int_0^1rx\,dx\le p\ \textbf{对一切构型}✓✓$$
$$\Longrightarrow \text{最好证书的值}\ =\ \text{所有构型}\ \textbf{simple fraction 的下界}✓✓✓$$
$$\Longrightarrow \boxed{\text{真值}\ \in\ [\,0.6818287,\ 1\,]}\qquad(\text{RH}\iff\text{上端}=1)✓✓$$
$$\qquad ⚠️\ \text{而}\ \S7.2(b)\ \text{的极值给}\ \tfrac23=0.6667<0.6818287 \Longrightarrow \textbf{该极值不是证书的最优点}✓✓$$

## §3 ⟹ 自己重算的**精确规格**（证书侧上确界）
$$\boxed{\max_{c_0,\,r}\ \Big(c_0+\int_0^1rx\,dx\Big)\quad\text{s.t.}\quad c_0+\sum_{j}s_jr(j/N)\le p\ \ \forall\ \text{admissible}\ (s,p)}✓✓✓$$
$$\text{约束（全部逐字已知）}：\text{near-CUE rows}\ |NS(j)-j|\le\tau\ (\tau=3\times10^{-40})；\ |D(1)|\le d_1；s_j\ge0；\text{marks 几何}✓✓$$
$$\text{目标值应为}\ 0.6818287\quad\Longrightarrow\quad \text{能超过} \Longrightarrow \textbf{天花板被推翻}✓✓✓$$

## §4 可行性（可本地执行）
$$\text{离散化}：\text{取}\ r\ \text{为分段线性／样条（节点}\ M\ \text{个）}\ \Longrightarrow \text{全部约束}\ \textbf{线性于}\ (c_0,\text{节点值})✓✓$$
$$\Longrightarrow \text{问题变成}\ \textbf{标准 LP}（\text{可用单纯形／内点法）✓✓\qquad(\text{等价地：与包络盒作用后的有限约束})✓$$
$$\text{而}\ \text{marks 几何}\ \text{是唯一需从论文补的输入（}\S7.2(b)\ \text{已给极值样例）✓✓$$

## §5 边界
$$\text{(i)}\ §1\ \textbf{逐字}（\texttt{clean.txt}\ L1265--1272）✓✓\quad\text{(ii)}\ §1\ \text{的数值核对为本档算术}✓\quad\text{(iii)}\ §2--§4\ \text{为规格（}\textbf{未执行}）✓$$
$$\text{(iv)}\ \textbf{未用 RH}；\ \textbf{未取 JSON}；\ \textbf{不声称前沿有错}✓✓$$
