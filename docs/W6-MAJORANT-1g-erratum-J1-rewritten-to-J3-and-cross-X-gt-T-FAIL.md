# ⚔️ W6-MAJORANT-1g · **勘误：(b) 分类反了 ⟹ J1 → J3 ⟹ 跨 $X>T$ 路线正式 FAIL**

> 依唐先生 12:53 指令（含对 1f §3 的实质纠错）✓
> **本档结果**：1f 的 (b) 判读**作废**；J1 改写为 **J3**；**W6-majorant-1 的 cross-$X>T$ 路线正式 FAIL** ✓✓

---

## §0 【勘误 T10】对 `1f §3` 的 (b)／(c)（**不覆盖上文**）

$$\text{1f 写"}(b)\ \text{光滑}\ \phi\Rightarrow\hat\eta\ \text{快衰}\Rightarrow\textbf{core 主导}" \ \textbf{作废}✓✗$$
$$\text{原因（唐先生）}：f=c^2\phi^4\ \textbf{本身就是完整函数}，\ \eta\ \textbf{承担的是 core 边界处}\ c^2\to0\ \text{的过渡}$$
$$\qquad\Longrightarrow\ \hat\eta\ \textbf{不是独立的"小尾项"}✓✗$$

### §0.1 反例（唐先生，逐字采纳）
$$f\in C_c^\infty(-L/2,L/2),\quad f=c^2\ \text{on core} \Longrightarrow \hat f(y)=\frac{1}{(iy)^N}\int f^{(N)}(x)e^{iyx}dx\ (\forall N)✓$$
$$\Longrightarrow\ |\hat f(y)|\ll_N|y|^{-N} \Longrightarrow y\asymp L：\boxed{|\alpha_n|\ll_N L^{-N}}\quad(\textbf{与}\ \tfrac1L\ \textbf{完全相反})✓✓✓$$
$$\Longrightarrow\ \boxed{\textbf{(b)}\ =\ \textbf{FALSE}}：\text{光滑}\ f\ \textbf{不} \text{让 core 主导，而是}\ \textbf{迫使}\ \eta\ \text{精确抵消 core 的}\ 1/y\ \text{尾部}✓✓$$

---

## §1 ⭐⭐ 抵消是**连续性强迫**的（回答 (c)）
$$\text{core 的}\ 1/y\ \text{尾部来自}\ x=\pm\ell\ \text{处}\ \textbf{人为制造的内边界}；\ \text{真实}\ f\ \text{在}\ x=\pm\ell\ \textbf{没有边界}（\text{连续进入 transition}）✓$$
$$\Longrightarrow\ \eta\ \textbf{必须} \text{提供恰好相反的边界贡献，否则完整}\ f\ \text{在}\ \pm\ell\ \text{产生跳跃}✓✓$$
$$\Longrightarrow\ \boxed{\text{core 的}\ 1/y\ \text{项与}\ \eta\ \text{的相应项}\ \textbf{不是"可能抵消"，而是}\ \textbf{强迫抵消}}✓✓✓$$
$$\Longrightarrow\ \boxed{\textbf{(c)}\ \textbf{不是唯一反例方向}；\ \text{1f 的 J1 归约}\ \textbf{须改写}}✓✓$$

---

## §2 硬公式（决定 J1 的真正变量）
$$\hat f(y)=-\frac{1}{iy}\!\int\!f'e^{iyx}\ (C^1,\ \text{外边界消失}) \Longrightarrow |\hat f|\le\frac{\|f'\|_1}{|y|}✓$$
$$\text{若}\ f'\ \text{绝对连续} \Longrightarrow |\hat f|\le\frac{\|f''\|_1}{y^2};\qquad f\in C_c^\infty \Longrightarrow |\hat f|\ll_N y^{-N}\ \forall N✓✓$$
$$\text{transition width}\ w=1 \Longrightarrow \|\partial_x^k(\phi^4)\|_1\asymp c^2\ (\text{常数依 cutoff 形状}) \Longrightarrow \boxed{|\alpha_n|\ll_k c^2(\log n)^{-k}}✓✓$$
$$\boxed{\text{真正决定 J1 的}\ \textbf{不是"core vs edge 谁大"}，\ \text{而是}\ \textbf{transition layer 的正则性}}✓✓✓$$

---

## §3 ⚠️ 但这**不救 W6**（不得因漂亮抵消宣布 ALIVE）
$$\frac{|O_1|}{D}\sim\frac{X}{T}(\log X)^{-N+O(1)} \xrightarrow{\ X=T^{1+\eta}\ }\ \boxed{\frac{T^\eta}{(\log T)^{N-O(1)}}}✓✓$$
$$\text{固定}\ N：\ T^\eta\gg(\log T)^N \Longrightarrow \boxed{\text{任何}\ \textbf{有限阶} \text{smoothness 都}\ \textbf{无法} \text{解决}\ X>T\ \text{的幂次障碍}}✓✓✓$$
$$\text{只有}\ \text{①cutoff 正则结构产生}\ \textbf{随}\ T\ \textbf{增长的有效阶数}；\ \text{或 ②真正}\ T^{-\eta}\ \text{级 suppression} \Longrightarrow \text{才可能跨墙}✓✓$$

---

## §4 J1 → **J3**（改写后的唯一闸门）
$$\boxed{\textbf{W6-J3}：\text{§5.2 的具体}\ \phi\ \text{是否给出}\ |\widehat{\phi^4}(y)|\le C_N|y|^{-N}\（\text{固定}\ N），\ \text{且这些 log-saving 是否仍不足以跨}\ X=T^{1+\eta}？}✓✓$$
$$\text{若论文只给}\ |\hat\phi(r)|\le\min\big(L,\tfrac2{|r|},\tfrac{C_\chi}{r^2}\big)\ \textbf{而未给导数／transition 正则性} \Longrightarrow \textbf{不能擅自使用}\ C^\infty \Longrightarrow \text{J3}\ ＝\ \textbf{真正的缺失输入}✓✓$$
$$\qquad \text{但}\ \textbf{无论 J3 给}\ 1/y^2／1/y^{10}／\text{任意固定阶}\ 1/y^N：\ \textbf{只能改 log budget，不能单独破}\ T^\eta✓✓✓$$

---

## §5 判定：**跨 $X>T$ 路线正式 FAIL**
$$\text{1f 的最后闸门"边缘层整段抵消 core"}\ \textbf{不存在}（\text{抵消是强迫的、非可构造的}）✓✓$$
$$\text{真正的最后闸门}＝\boxed{\text{是否存在由}\ \Phi\ \textbf{自身} \text{产生的}\ T^{-\eta}\ \text{级离散谱压制？}}✓✓$$
$$\text{若无额外机制} \Longrightarrow \boxed{\textbf{W6-majorant-1 的 cross-}X>T\ \textbf{路线正式 FAIL}}✓✓✓$$
$$\qquad(\text{仍}\ \textbf{不是} \text{W6 整体 FALSE：}\ \text{W6＝SUPPORT-1 墙本身不动}；\ \text{本档只封}\ \textbf{对偶正性 majorant 这条具体机制})✓✓$$

---

## §6 边界
$$\text{(i)}\ §0--§2\ \text{照录唐先生 12:53 的核心论证（分部积分反例／强迫抵消／硬公式）}✓$$
$$\text{(ii)}\ §3\ \text{为直接推论；§4--§5 判定照录唐先生}✓\quad\text{(iii)}\ \textbf{未用 RH／HL／pair correlation}；\ \textbf{零数值}✓$$
