# ⚔️ **D-GRAM-1 四刀审计**：(Z) 与「整数乘法能量型 HS」**不相容** ⟹ 卡点＝**parity barrier**（非 SUPPORT-1）

> 依唐先生 13:46 指令：只做 Dirichlet 多项式 Gram 型，不碰自己的 $M_T(s)$；四刀 A／B／C／D ✓
> **本档结果**：**C 判定成立** —— (c) 确有「不经素侧二阶矩」的实现 ✓✓（保留资产）；**但** (Z) 与它**不相容**，阻碍＝**parity barrier** ✓✓✓

---

## §1 A 刀（构造）：裸 Gram 丢 (Z)，intertwiner 必吞 $\Lambda$
$$\text{裸 Dirichlet Gram}：G_{mn}=\hat w\!\big(\log\tfrac nm\big) \Longrightarrow G=G^*,\quad a^*Ga=\int_{\mathbb R}w(t)\Big|\sum_{n\le N}a_nn^{it}\Big|^2dt\ge0✓$$
$$\Longrightarrow \boxed{G\succeq0 \Longrightarrow n_-(G)=0} \Longrightarrow \textbf{(Z) 丢失}✓✓\quad(\text{唐先生 13:46 §1 逐字成立})✓$$
$$\text{要 (Z) 须走}\ \tilde G=A^*JA：\ \text{而}\ A\ \text{的求值即}\ \textbf{显式公式的素侧} \Longrightarrow \textbf{必含}\ \Lambda✓✓$$
$$\qquad 📌\ \text{前沿自身的}\ \tilde G\ \textbf{就是} \text{素侧实现}（L100--L120：}\tilde G=P+Q\ \text{的}\ (Z)\ \text{由素侧给出}）✓✓$$

## §2 B 刀（trace）：**可用** ✓
$$\mathrm{tr}\tilde G=(1+o(1))N,\qquad N\ge s_1+2s_2+2p\quad(\text{RvM，}\textbf{无条件})✓✓$$
$$\qquad\Longrightarrow \textbf{B 刀不构成障碍}✓$$

## §3 ⭐⭐⭐ C 刀（HS，决定性）：两量**不相等**，且阻碍＝parity
$$\textbf{唐先生 13:46 §2--§4 已证（逐字采纳）}：\text{Dirichlet Gram 的 HS}\ \textbf{＝整数乘法能量}✓✓$$
$$\qquad \|G\|^2_{HS}=\sum_{m,n\le N}F\!\big(\log\tfrac nm\big)=:E_F(N),\qquad F=|K|^2,\ K=\hat w✓$$
$$\qquad \text{约数形式}：E_F(N)=\sum_{\substack{a,b\le N\\(a,b)=1}}\Big\lfloor\frac{N}{\max(a,b)}\Big\rfloor F\!\big(\log\tfrac ba\big)✓$$
$$\qquad \text{连续主项}：E_F(N)\sim N^2\!\!\int_{\mathbb R}\frac{F(u)}{1+e^{-|u|}}du \quad(\textbf{纯窗积分})\ ✓✓$$
$$\Longrightarrow \boxed{\text{(c) 确有}\ \textbf{"不经素侧二阶矩"}\ \text{的天然实现}}✓✓✓\quad(\textbf{本轮保留的正结果})✓$$

$$\textbf{但}：\text{带 (Z) 的}\ \tilde G\ \text{的 HS}\ \textbf{是} \text{Montgomery 素侧二阶矩}（前沿逐字 L107）：\|\tilde G\|^2_{HS}=(R(\psi)+o(1))N✓$$
$$\Longrightarrow \text{要 equate 两者} \Longrightarrow \text{须恒等式把}\ \boxed{\sum_{k,l}\Lambda(k)\Lambda(l)K\!\big(\log\tfrac kl\big)}\ \text{化为整数能量}✓✓$$
$$\Longrightarrow \boxed{\text{而这正是}\ \textbf{parity barrier}（\texttt{V254}／\texttt{V255}）\ \text{所阻断的方向}}✗✗✓$$
$$\qquad ⭐\ \text{故卡点}\ \textbf{不是 SUPPORT-1}（\text{素侧二阶矩的}\ X\le T\text{范围}），\ \text{而是}\ \boxed{\textbf{算术--零点 intertwiner}}✓✓✓$$

## §4 D 刀（rank–trace）：C 已定，不再代入；但记录
$$\text{方法本身天花板}\ \textbf{100\%}（前档逐字）⟹ \text{若 C 能过，D 有空间}；\ \text{但 C 不过} ⟹ \text{不代入}✓$$

## §5 判词与保留资产
$$\boxed{\text{D-GRAM}\ =\ \textbf{C（工具失效）}}✓$$
$$\qquad \textbf{卡点（精确）}：\boxed{\text{(Z)（零点块结构）与「整数乘法能量型 HS」}\ \textbf{不相容}}✓✓✓$$
$$\qquad \text{阻碍}：\textbf{parity barrier}（\text{不是 SUPPORT-1}）✓✓$$

$$\textbf{保留资产}：$$
$$\qquad\text{①}\ \textbf{(c) 的整数能量实现}：\ E_F(N)=\sum_{m,n}F(\log\tfrac nm)\ \text{与连续主项}\ N^2\!\int\frac{F(u)}{1+e^{-|u|}}du\ ——\ \textbf{可独立计算，非素侧}✓✓$$
$$\qquad\text{②}\ \textbf{不相容性的精确陈述}（\text{裸 Gram}\succeq0\Rightarrow n_-=0\Rightarrow (Z)\ \text{丢失}；\ \text{带 (Z)}\Rightarrow \text{HS 回素侧}）✓✓$$
$$\qquad\text{③}\ \textbf{obstruction 定位}：\text{intertwiner}\ A\ \text{必吞}\ \Lambda \Longrightarrow \text{parity barrier}✓✓$$

## §6 与唐先生预判的对照（逐条）
$$\text{唐先生 §8："若 realization 一构造出来就强制重新出现}\ \Lambda(p)\Lambda(q)\ \text{，则干净判死}" \Longrightarrow \boxed{\text{本档确认：正是如此}}✓✓$$
$$\text{唐先生 §2--§4 的 (c) 证据} \Longrightarrow \boxed{\text{成立且保留}}✓✓$$
$$\text{唐先生 §6 的"新障碍＝intertwiner"} \Longrightarrow \boxed{\text{成立，且已定位到 parity}}✓✓✓$$

## §7 边界
$$\text{(i)}\ §1／§3\ \text{逐字采纳唐先生 13:46 的推导；}\ §3\ \text{的 parity 定位为本档推论}✓\quad\text{(ii)}\ \textbf{未用 RH}；\ \textbf{零计算}✓$$
$$\text{(iii)}\ ⚠️\ \text{"parity barrier 阻断该恒等式"}\ \text{为}\ [\textbf{结构}] \text{级（}\texttt{V255}\ \text{自陈该接链目前不存在}）✓✓$$
