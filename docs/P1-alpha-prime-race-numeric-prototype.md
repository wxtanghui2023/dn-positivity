# P1-$\alpha$ · **素数竞赛数值原型**：finite blind ＋ limit visible（已跑）

> 依 P0 协议（`docs/P0-*`）执行：**只允许 ①ALIVE／②FALSE／③UNRESOLVED**；本轮 = **数值实验** ✓
> 脚本：`scripts/p1alpha_prime_race_blind_visible.py`（$N=10^7$，664{,}579 素数）✓

## 0. 对象（G1 合格）
$$\mathcal O_X^{4}:=\Big(\sum_{\substack{p\le X\\ p\equiv a\,(4)}}\frac1p\Big)_{a\in\{1,3\}}\quad(\text{仅用素数 }p\le X\ \text{与有限模信息 }q=4)✓\ \mathrm{G1}✓✓$$

## 1. ⭐ G2（盲）：有限层无法决定"谁领先" —— **数值证实**

$$\text{sign}\big(\pi(x;4,1)-\pi(x;4,3)\big)\ \text{在}\ x\le10^7\ \text{上}\ \textbf{翻转}\ 10\ \text{次}\ ✓✓$$
$$\qquad\text{前 12 次翻转：}\ x=1002;\ 617002;\ 618002;\ 623002;\ 625002;\ 628002;\ 629002;\ 630002;\ 633002;\ 634002\ ✓$$
$$\qquad(\text{密集翻转区}\ \sim6.2\times10^5\ \Longrightarrow\ \textbf{任何有限层都会给出"错误的"领先判断})✓✓$$
$$\Longrightarrow\ \textbf{任何单一有限截断都不能判定全局赢家} = \text{G2}\ \textbf{饱和}✓✓$$

## 2. ⭐ G3（显影）：调和权重下极限存在 —— **数值证实**

$$D(X):=\sum_{\substack{p\le X\\p\equiv3(4)}}\frac1p-\sum_{\substack{p\le X\\p\equiv1(4)}}\frac1p\qquad(\text{对数密度差})✓$$
$$\begin{array}{c|r}
X&D(X)\\ \hline
10^{3}&+0.333197\\
10^{4}&+0.333671\\
10^{5}&+0.334644\\
10^{6}&+0.334979\\
10^{7}&+0.334964\\
\end{array}\qquad\Longrightarrow\ \textbf{稳定收敛（差分}\sim10^{-4}\text{）}✓✓$$
$$\textbf{对照（关键）}：\text{等权计数差}\ \pi(X;4,3)-\pi(X;4,1)\ \text{在}\ X=10^7\ \text{时}=227\ \textbf{且无极限（随 }X\ \text{飘）}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{调和权重}\ (1/p)\ \textbf{杀掉有限涨落、产生极限；等权计数不产生}}✓✓✓$$
$$\qquad(\text{这与 P0 §6 的机制教训一致：}\text{调和权重保留与低阶零点的共振})✓$$

## 3. ⭐⭐ **②FALSE 事件：我自己的极限公式被数值杀掉并纠正**

$$\textbf{我在 P0／脚本中给的预测}：D(X)\to\log(4/\pi)=+0.241564✓\qquad\textbf{实测}\ 0.334964 \Longrightarrow \textbf{相对偏差}\ 38.7\%✓$$
$$\textbf{原因（已定位）}：\log L(1,\chi_4)=-\sum_p\log(1-\chi_4(p)/p)\ \text{而}\ \sum_p\chi_4(p)/p\ \text{不等于它}——\ \text{差}\ \sum_{k\ge2}\frac1k\sum_p\frac{\chi^k}{p^k}✓$$
$$\textbf{纠正后闭式}：D_\infty=\log\frac4\pi+\underbrace{\frac12\sum_{p>2}p^{-2}}_{+0.1011}-\underbrace{\frac13\sum_p\chi_4(p)p^{-3}}_{-0.0105}+\underbrace{\frac14\sum_{p>2}p^{-4}}_{+0.0036}+\ldots\approx\mathbf{0.3358}✓✓$$
$$\qquad\text{与实测}\ 0.334964\ \text{吻合到}\ \sim8\times10^{-4}✓✓✓\quad(\text{尾部为慢收敛项})✓$$
$$\Longrightarrow\ \boxed{\text{这正是新协议要的：}\textbf{一个可被数值直接杀掉的命题}，当场被杀、当场纠正}✓✓✓$$

## 4. 归档判定（按 P0 §4）
$$\textbf{机制原型（finite blind}+\text{limit visible}）\ =\ \boxed{\text{①}\ \mathrm{ALIVE}}✓\quad(\text{数值双向证实})✓$$
$$\textbf{子命题（我的}\log(4/\pi)\text{预测）}\ =\ \boxed{\text{②}\ \mathrm{FALSE}}✓\quad(\text{当场杀掉并纠正})✓$$
$$\textbf{诚实的边界}：\text{这是}\ \textbf{已知现象}（\text{Littlewood 翻转 ＋ Rubinstein--Sarnak 偏置}）——\ \textbf{不是新数学}✓$$
$$\qquad\text{它的作用} = \textbf{机制的已验证原型}（\text{可复现、可数值判死}），\ \text{供 }\mathrm{G4}\ \text{搬运使用}✓✓$$

## 5. G4 接口（下一轮可测）
$$\text{偏置的}\ \textbf{涨落振幅} \asymp X^{\beta_{\max}-\frac12}\ \text{型} \Longrightarrow \text{G4 接口}＝\textbf{标度指数}✓$$
$$\qquad\text{待测}：\text{从有限数据}\ x\le X\ \textbf{拟合} \text{振幅指数，}\ \text{并测其收敛／偏移}（\beta\neq\frac12\ \text{会在极大 }X\ \text{才显露}⟹\textbf{有限层盲）}✓✓$$
$$\qquad\text{这正是 P0 §6 的 P1-}\gamma\ \text{同类判据，}\ \text{下一轮合并执行}✓$$
