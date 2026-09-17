# ⚔️ **W4-1e** · 盲读出实现：**频率坐标成功 ｜ 增长坐标落在第 3 档（不可分辨）**

> 依唐先生 13:28：做 ①，但改为**盲读出**（峰定位 → 频带投影 → 独立区间增长率拟合）＋ **null control**，判据三档 ✓
> **本档结果**：频率（$\gamma$）**盲定位成功** ✓✓；增长（$\beta-\tfrac12$）**落在第 3 档** ⟹ 谱泄漏／混频，**不得解释为 $\beta$** ✓✓✓

---

## §1 设计（全部按唐先生规格）
$$\text{阶梯}：u=\log T\ \text{上}\ 512\ \text{点均匀},\ T\in[10^3,\,10^9]\（\Delta u=0.027,\ \nu_{\max}=116.2,\ \text{全窗分辨率}\ 0.455）✓$$
$$\qquad \Lambda\ \text{由}\ \textbf{流式分块筛}（\text{内存}\ O(N)，\text{时间}\ 8.2\text{s}）✓✓$$
$$\text{盲定位}：\text{全窗 Hann 谱的高峰（}\nu>3，\ \text{阈值}=4\times\text{中位数}），\ \textbf{不使用已知}\ \gamma✓✓$$
$$C_j(u)：\textbf{三段不重叠窗口}（u_c=9.19/13.79/18.38）\ \text{内的频带投影，带宽}\ \pm2.05✓$$
$$\text{增长拟合}：|C_j(u)|\sim e^{\eta_ju} \Longrightarrow \eta_j=\beta_j-\tfrac12✓$$
$$\textbf{null control}：\text{①off-band（相邻峰中点）\ ②phase-randomized surrogate（同振幅谱、随机相位）}✓✓$$

## §2 ⭐ **盲定位成功**（不使用 $\gamma$ 输入）
$$\text{峰}：14.07,\ 20.88,\ 24.96,\ 30.41,\ 33.13,\ 40.85,\ 43.12$$
$$\text{对照已知}\ \gamma：14.135,\ 21.022,\ 25.011,\ 30.425,\ 32.935,\ 40.919,\ 43.327 \Longrightarrow \textbf{逐一对应}✓✓✓$$
$$\qquad(\text{注意}\ 20.88\ \text{vs}\ 21.022,\ 33.13\ \text{vs}\ 32.935：\text{偏}\ \approx0.15\!-\!0.2，\text{受带宽}\ \pm2.05\ \text{影响}）✓$$

## §3 ⚠️ **增长坐标 η 不稳定**

| 峰 $\nu$ | 三窗振幅 | $\eta(1\to3)$ | $\eta(1\to2)$ |
|:--|:--|:--|:--|
| 14.07 | 0.181 / 0.218 / 0.196 | $+0.0087$ | $+0.0399$ |
| 20.88 | 0.127 / 0.113 / 0.146 | $+0.0153$ | $-0.0257$ |
| 24.96 | 0.143 / 0.124 / 0.091 | $-0.0491$ | $-0.0309$ |
| 30.41 | 0.098 / 0.078 / 0.066 | $-0.0433$ | $-0.0515$ |
| 33.13 | 0.114 / 0.073 / 0.099 | $-0.0154$ | $-0.0966$ |
| 40.85 | 0.087 / 0.055 / 0.121 | $+0.0356$ | $-0.0994$ |
| 43.12 | 0.038 / 0.075 / 0.099 | $+0.1046$ | $+0.1497$ |

$$\Longrightarrow\ \eta_j\ \textbf{散布在}\ [-0.049,\,+0.105]，\ \text{且两套区间}\ \textbf{互相不一致}（\text{如}\ 33.13：-0.015\ \text{vs}\ -0.097）✗✗$$

## §4 ⭐⭐⭐ **三项对照不可区分** ⟹ 三档判据落第 3 档
$$\textbf{off-band}：\eta\in[-0.065,\,+0.069]\qquad\textbf{surrogate}：\eta\in[-0.081,\,+0.109]$$
$$\qquad\text{峰}\ \eta\in[-0.049,\,+0.105]$$
$$\Longrightarrow\ \boxed{\text{三组}\ \textbf{统计上不可区分}} ⟹ \boxed{\text{第 3 档}：\eta_j\ \text{随窗口／频带显著漂移} \Longrightarrow \textbf{谱泄漏／混频，不得解释为}\ \beta}✓✓✓$$

## §5 量化（与本项目既有结论一致）
$$\text{增长估计器的}\ \textbf{噪声地板}\ \approx\ \pm0.05\!-\!0.1，\ \text{与物理上感兴趣的范围}\ \textbf{同阶} \Longrightarrow \textbf{无法分辨}✓✗$$
$$\qquad ⭐\ \text{这与}\ \texttt{GAP-2}\ \text{测得的}\ \textbf{分辨率地板}\approx0.15\ \textbf{一致}✓✓\ \text{（两条独立路径同值）}✓✓$$

## §6 判定
$$\boxed{\text{频率坐标}＝\textbf{成功}（\text{可盲定位，}\Delta=0.15\!-\!0.2）\ \big|\ \ \text{增长坐标}＝\textbf{未落地（第 3 档）}}✓✓$$
$$\Longrightarrow\ \text{"frequency}\to\text{growth 双坐标读出机制"}\ \textbf{尚未成立}✓\qquad\boxed{\text{W4-1e}\ =\ \textbf{C（工具失效）}}$$
$$\qquad \text{卡点（精确）}：\ \boxed{\text{增长估计器的噪声地板}\ (\pm0.05\!-\!0.1)\ \textbf{与信号范围同阶}}✓✓$$

## §7 改进路径（量化，非空话）
$$\text{要令噪声地板}\ \ll0.05：\text{①}\ u\text{-范围再扩}\ \sim2\ \text{个数量级（}\text{须}\ T_{\max}\sim10^{11\!-\!12}）\ \text{②}\ T\ \text{点数增至}\ 10^4\ \text{级}✓$$
$$\qquad ⚠️\ \text{成本只与}\ T_{\max}\ \text{有关（流式筛，}\text{内存}\ O(N)），\ \text{故}\ ②\ \textbf{便宜}，\ ①\ \textbf{贵}✓✓$$

## §8 边界
$$\text{(i)}\ §2--§5\ \text{为本档实测（流式分块筛，}\Lambda\ \text{精确）}✓\quad\text{(ii)}\ \text{带宽}\ \pm2.05\ \text{偏宽}，\ \text{使}\ 20.88/33.13\ \text{定位偏}\ 0.15\!-\!0.2✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \gamma\ \text{仅作对照；全部有限整数计算}✓$$

---

# §9 【勘误 T10】对 §5 措辞（2026-09-17 13:33）
$$\text{原文写"与 GAP-2 的分辨率地板}\approx0.15\ \textbf{独立同值}" \Longrightarrow \textbf{应改为}：$$
$$\boxed{\text{两条独立实验路线给出}\ \textbf{同量级} \text{的 resolution floor}（\text{一为}\ 0.05\!-\!0.10，\text{一为}\approx0.15）}✓✓$$
$$\qquad(\text{意义是}\ \textbf{同一数量级的障碍}，\ \textbf{不是数值相等}）✓✓$$
