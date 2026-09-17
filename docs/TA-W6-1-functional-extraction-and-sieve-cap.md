# ⚔️ W6-1 · **拆出所需二元泛函 ＋ sieve 武器的可证上限**

> 依唐先生 11:57（W6 优先）｜**已查地图** ✓（`CLOSED-ROUTES-MAP`／`MASTER-*`／`AUDIT2-tool-target-mismatch`／`V254`／`V255`／`AUDIT-local-vs-global-satisfiability`）✓

## §1 目标泛函（**拆出来**）
$$\text{W6 的真实缺口}：\ X>T\ \text{后，"离对角素数和不再被对角支配"}\Longrightarrow \text{需}\ \textbf{prime-pair} \text{信息}✓$$
$$\text{但}\ \textbf{我们不要求完整 HL}：\text{只需}\ \boxed{\Big|\sum_{|h|\le H}w(h)\Big(\#\{p:p,p+h\ \text{prime}\}-\mathfrak S(h)\tfrac{X}{\log^2X}\Big)\Big|\le\text{允许误差}}✓✓$$
$$\Longrightarrow\ \textbf{待攻对象＝一个}\ \textbf{加权线性泛函} \text{（非完整 pair correlation）}✓$$

## §2 三个候选武器（唐先生点名）＋ 地图给出的**先验**

$$\begin{array}{c|l|l}
\text{武器}&\text{形态}&\text{地图先验}\\ \hline
\text{(i) Selberg sieve bilinear remainder}&\lambda_d\ \text{权重＋双线性余项}&\textbf{C（parity barrier，`V255`）}\\
\text{(ii) dispersion 方法}&L^2\ \text{展开＋}\delta\text{-符号}&\text{未查到我方登记上限}\\
\text{(iii) divisor-switching}&d\ \text{↔ 因子角色互换}&\text{未查到我方登记上限}\\
\end{array}✓$$
$$\qquad\text{另有}\ \text{(iv) energy／(v) incidence／(vi) large-sieve duality／(vii) 幂平均}\ \text{（未逐条查上限）}✓$$

## §3 ⭐ 结果判定（本轮）＝ **C（工具失效）· 卡点＝parity**
$$\text{(i) sieve：}\texttt{V255}\ \text{逐字——sieve 权重有}\ \textbf{可证}\ \text{parity barrier（看不见素数，只能到 almost-primes）}✓$$
$$\qquad\Longrightarrow \text{它}\ \textbf{原则上不能} \text{提供"}\#\{p:p,p+h\ \text{prime}\}\text{"型信息} \Longrightarrow \boxed{\text{(i)}\ \textbf{失效}}✓✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{精确卡点} \text{待钉}：\texttt{V255 §5(b)}\ \text{[待核]}——\text{parity barrier 能否重述为"某 Dirichlet 级数的收敛横坐标上界"}\ \textbf{目前不存在}✓$$
$$\qquad \Longrightarrow \text{故本轮只能给}\ \textbf{结构性}\ \text{判定（}[\text{结构}]），\ \text{不能给"}\textbf{哪一条不等式}" \text{的逐行版本}✓$$

## §4 ⭐⭐ **平方自由实验——判据已被档案预答**
$$\text{squarefree}\ \text{有}\ \textbf{局部（模）描述}（\mu^2(n)：\text{无}\ p^2\ \text{整除}；\ \texttt{AUDIT-local-vs-global} \text{逐字：}S=\{n:\forall p,\ n\bmod p^2\in S_p\}）\Longrightarrow \textbf{sieve 可见}✓$$
$$\text{primes}\ \text{需}\ \textbf{奇偶性} \Longrightarrow \textbf{sieve 不可见}✓✓$$
$$\Longrightarrow \boxed{\text{若 squarefree 突破而 primes 坍塌} \Longrightarrow \text{墙的位置锁定在}\ \textbf{prime extraction}＝\textbf{parity barrier 位置}}✓✓✓$$
$$\qquad\text{反之若}\ \textbf{squarefree 也突破不了} \Longrightarrow \text{障碍}\ \textbf{比素数稀疏性更深} \Longrightarrow \text{墙在}\ \textbf{二体结构本身}✓✓$$

$$\textbf{这是一个}\ \textbf{可判定} \text{的二分实验}（\text{不依赖任何猜想}）✓✓\quad\text{—— 建议}\ \textbf{列为 W6 第一硬实验}✓✓$$

## §5 下一步（换武器路线，按"打不穿即换"纪律）
$$\text{① 先把}\ §1\ \text{的泛函}\ \textbf{写成完全显式}（w(h)\ \text{的具体形式、误差预算）}✓$$
$$\text{② 对 (ii) dispersion／(iii) divisor-switching 补做地图查上限（本轮未做）}✓$$
$$\text{③ 执行}\ §4\ \text{的平方自由实验（二分判定）}✓✓$$
$$\text{④ 若 (i) 完全失效且 (ii)(iii) 也卡}\ \Longrightarrow \text{按 D 记录（该类工具原则上不足）}✓$$

## §6 边界
$$\text{(i)}\ §3\ \text{为}\ [\textbf{结构}] \text{级（parity barrier 与我方所需泛函之间的}\ \textbf{蕴含链尚未建立}，}\texttt{V255 §5(b)}\ \text{自陈"目前不存在"）✓$$
$$\text{(ii)}\ \text{本轮}\ \textbf{未做逐行估计}，\ \textbf{未用 RH}，\ \textbf{零数值}✓\quad\text{(iii)}\ \text{新对象}\ \textbf{不得属"筛法权重类"}（\texttt{V254 T6}）✓$$
