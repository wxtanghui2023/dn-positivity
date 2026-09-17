已查地图：命中 `C-37`(台账 W1 行)｜`C-34`｜本档前身 `docs/ATTACK-CARD-W1-beta-wall.md` → 本档＝**S1 执行档**

# ⚔️ **S1 执行：Tsang 核／带宽路线 —— 判词 DEAD(移除路线) ＋ 活口(权衡曲线) ＋ ⭐W1⟺W6 统一**

> 唐先生 16:47 裁「**甲，乙**」：甲＝落实 W1 修正 B（已提交 `32a826b`）；乙＝开 **S1**（或 S2）✓
> **本档＝S1 首刀**：直取 `Lamzouri 2026`（arXiv:2609.02882v2）正文，定位 Tsang 核与带宽条件的**确切形式**✓

---

## §1 逐字取到的四条（一手，arXiv:2609.02882v2 正文）
$$\textbf{(T1)}\ \text{"...a kernel of Tsang whose real part is positive in a fixed horizontal strip. After rescaling by}\ \log T/(2\pi),\ \text{this positivity applies only if one assumes that all the non-trivial zeros with imaginary part in}\ [T,2T]\ \text{lie in a very narrow strip of the form}\ |\beta-1/2|\le c/\log T\ \text{"}✓$$
$$\textbf{(T2)}\ ⭐⭐⭐\ \text{"This restriction}\ \textbf{cannot be removed merely by searching for a better kernel}.\ \text{Indeed, for the above method to work without any information on the real parts of the zeros, one would require that the kernel}\ K\ \text{satisfies}\ \mathrm{Re}K(z)\ge0\ \text{for all}\ z\in\mathbb C.\ \text{However,}\ \textbf{no such nonconstant entire kernel exists}\ \text{"}✓✓✓$$
$$\textbf{(T3)}\ \text{"More precisely, they proved that if for all large}\ T,\ \text{all the zeros with}\ T<\gamma\le2T\ \text{satisfy}\ |\beta-\tfrac12|<\frac{b}{2\log T},\ \text{then at least}\ 2/3\ \text{of the zeros are simple and on the critical line when}\ b=0.3185,\ \text{while for}\ b=0.001\ \text{the corresponding proportion is at least}\ 0.6725\ \text{"}✓✓$$
$$\textbf{(T4)}\ \text{"extending earlier work of Gallagher and Mueller, Goldston, Lee, Schettler and Suriajaya showed that}\ \textbf{Montgomery's full Pair Correlation Conjecture, without assuming RH, implies that asymptotically}\ \textbf{100\%}\ \text{of the zeros are simple and on the critical line}\ \text{"}✓✓$$

## §2 S1 判词（两个子问题，分别判）
$$\textbf{S1-a（改进核以移除}\ \beta\text{-输入）}：\boxed{\textbf{DEAD}}\ ✓✓\quad\text{依据}\ \texttt{(T2)}\ \textbf{文献级}（\text{非我方猜测}）$$
$$\qquad \text{附我方补证（一行）}：\text{若}\ \mathrm{Re}K\ge0\ \text{于全}\ \mathbb C,\ \text{则}\ e^{-K}\ \text{有界且整} \Longrightarrow K\equiv\text{const}\ (\text{Liouville})⟹ \textbf{不存在非恒定整核}\ ✓✓$$
$$\textbf{S1-b（带宽}\ b\ \leftrightarrow\ \text{比例 的权衡曲线）}：\boxed{\textbf{ALIVE}}\ ✓✓\quad\text{依据}\ \texttt{(T3)}\ \text{已给两点}：b=0.3185\Rightarrow2/3,\ b=0.001\Rightarrow0.6725$$
$$\qquad \Longrightarrow \textbf{可算的单调权衡}：\textbf{越小}\ b \Longrightarrow \textbf{越好} \text{的常数}；\ \text{问题变为：}\ \textbf{曲线}\ b\mapsto\text{比例}\ \text{的最优形状}✓✓$$

## §3 ⭐⭐ 结构发现（本档新）：**W1（β-敏感）与 W6（support>1／对相关）是同一资源**
$$\text{证据链（全部一手）}：$$
$$\qquad \text{(i)}\ \texttt{(T3)}：\text{带}\ \beta\text{-信息（带宽}\ b\text{）}\Longrightarrow\ \text{常数随}\ b\ \text{单调改善}；$$
$$\qquad \text{(ii)}\ \texttt{(T2)}：\ \beta\text{-信息}\ \textbf{无法} \text{用"更好的核"替代（整核障碍）}；$$
$$\qquad \text{(iii)}\ \texttt{(T4)}＋\texttt{L1}：\text{换用}\ \textbf{无条件对相关} \text{（}Baluyot\ \text{等}\ \lambda 3.1\text{）即得}\ 88.76\%；\ \text{而}\ \textbf{全对相关猜想} \text{（不假设 RH）}\Longrightarrow\ \textbf{100\%}✓✓$$
$$\Longrightarrow \boxed{\ \beta\text{-信息（带宽）与 对相关信息 在此路线中}\ \textbf{互相替换} \text{，二者皆是"离线配对的定价"}}✓✓✓$$
$$\qquad ⚠️\ \text{对本项目意义}：\text{这给台账"}\textbf{三面一墙}\text{"（}\text{W3–W5}\text{）提供了一个}\ \textbf{独立的、文献锚定} \text{的支持}（\text{此前仅为}\ [\textbf{结构}]\ \text{级断言}）✓✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{不得} \text{外推为"所有路线都如此"}（\text{本档只覆盖：Tsang 核 ＋ 对相关 这一族}）✓$$

## §4 由 §3 派生的**具体可攻问题**（新，不重复档案）
$$\textbf{(Q1)}\ \textbf{权衡曲线的拐点}：\ b=0.3185\Rightarrow2/3\ \text{与}\ b=0.001\Rightarrow0.6725\ \text{之间}\ \textbf{比例如何增长}？$$
$$\qquad \text{若曲线在}\ b\to0\ \text{时}\ \textbf{饱和} \text{在}\ \sim0.6725 \Longrightarrow \text{与}\ \textbf{W12 的}\ 0.68185\ \text{天花板}\ \textbf{同址}✓✓$$
$$\qquad \text{若可越过}\ 0.68185 \Longrightarrow \textbf{新信息}✓$$
$$\textbf{(Q2)}\ \textbf{定价方程}：\text{把"}\beta\text{-带宽}\ b"\ \text{与"对相关加权因子的可处理性"写成}\ \textbf{同一资源的两条轴} \text{（}\text{这正是}\ \texttt{L1}\ \text{的 Prop 2.1 在做的事}）✓$$
$$\textbf{(Q3)}\ \textbf{反推}：\ \text{既然}\ \textbf{全对相关}\Longrightarrow100\%\ \text{（}\texttt{T4}\text{）}，\ \text{则}\ \textbf{任何阻碍}\ 100\%\ \text{的量}＝\text{对相关的}\ \textbf{缺口} \Longrightarrow \text{与}\ \texttt{W6}\ \text{合址确认}✓$$

## §5 边界
$$\text{(i)}\ \texttt{T1--T4}\ \text{为}\ \textbf{正文逐字}（\text{arXiv:2609.02882v2 检索片段}，\ \textbf{未读全文}）✓；\ \texttt{(T2)}\ \text{的"不存在非恒定整核"我方给出}\ \textbf{一行补证}✓✓$$
$$\text{(ii)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ §3\ \text{为}\ [\textbf{结构}]\ \text{级归纳}，}\ §4\ \text{为可攻问题清单（}\textbf{未执行}）✓$$
$$\text{(iii)}\ \textbf{S2}（A-2 接 de Bruijn–Newman 热流族）\ \textbf{尚未开}✓$$
