已查地图（**先查后写**）：`C-380-23`（**二维全覆盖 ⟹ 二维不足** ✓✓）、`C-380-22`（**M1–M5** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-24：Three-Moment Joint Obstruction Audit（注册＋可达性判定）**，**有计算（数值采样，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 设定（固定}\ (Q_1, Q_2, Q_3)✓✓）✓✓：S_1 = \sum_jX_j✓，\ S_2 = \sum_jX_j^2✓，\ S_3 = \sum_jX_j^3✓ \Longrightarrow Q_1 = S_1✓，\ Q_2 = 2S_2 - 4✓，\ Q_3 = 4S_3 - 3S_1✓✓$$
$$\qquad \Longrightarrow \ E_0\ \text{前三条件}✓✓：\ \boxed{S_1 \le -\tfrac12✓,\quad S_2 \le \tfrac74✓,\quad S_3 \le \tfrac{3S_1 - \frac12}{4}}✓✓$$
$$\qquad \Longrightarrow \ \text{问题变为}\ \boxed{[-1,1]\ \text{上的四点等权幂和可行性问题}}✓✓$$
$$\textbf{② ⭐⭐ 可达性判定（本档核心）}✓✓：\min\max(Q_1 + \tfrac12, Q_2 + \tfrac12, Q_3 + \tfrac12) = \boxed{-0.5938 < 0}✓✓ \Longrightarrow \textbf{三阶可达}✓✓$$
$$\qquad \textbf{采样}✓✓：\text{同时满足三条件者}\ 5409／200000✓✓（\approx 2.7\%✓，\ \textbf{不稀有}✗✓） \ —— \ \text{如}\ X = (-0.932, 0.246, 0.103, -0.807)✓，\ (Q_1, Q_2, Q_3) = (-1.391, -0.818, -1.107)✓✓$$
$$\qquad \textbf{最优样本}✓✓：X = (-0.556, 0.340, -0.997, 0.119)✓，\ Q_1 = -1.0938✓，\ Q_2 = -1.1355✓，\ Q_3 = -1.2016✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{three-moment obstruction absent}}✓✓ \ —— \ \textbf{P5′ 触发}✓✓$$
$$\textbf{③ ⭐ 联合结论（本档最有价值）}✓✓：\textbf{2 阶不足}✓（C\text{-}380\text{-}23✓）＋ \textbf{3 阶不足}✓（本档✓） \Longrightarrow \ \boxed{\text{obstruction 必须}\ \textbf{至少是 4 阶联合的}}✓✓$$
$$\textbf{④ 中心矩视角}✓✓：m = \tfrac{S_1}{4}✓，\ Y_j = X_j - m✓，\ \sum_jY_j = 0✓✓（\text{数值}\ 4.4 \times 10^{-16}✓）$$
$$\qquad \textbf{最优点}✓✓：m = -0.273✓，\ \textbf{二阶中心矩}\ 1.133✓，\ \textbf{三阶中心矩}\ -0.109✓✓ \Longrightarrow \ \textbf{三阶耦合弱}✓✓（\text{与「三阶不足」一致}✓✓）$$
$$\textbf{⑤ P1′–P5′ 硬验收（采纳）}✓✓：\textbf{P1′}✓：\text{必须至少出现}\ \textbf{三变量耦合}\ G(Q_1, Q_2, Q_3) \ge 0✓✓$$
$$\qquad \textbf{P2′}✓✓：\text{证明该}\ G\ \textbf{不是}\ \text{所有 probability measures 的普遍 moment inequality}✗✓，\ \text{而是来自}\ \textbf{四点等权结构}✓✓；\ \text{或至少证明四点结构使其}\ \textbf{严格加强}✓✓$$
$$\qquad \textbf{P3′}✓：\text{在}\ Q_1, Q_2, Q_3 \le -\tfrac12\ \text{下推出}\ G < 0✓✓；\ \textbf{P4′}✓：\text{排除}\ G = C + \lambda_1Q_1 + \lambda_2Q_2 + \lambda_3Q_3✓✓ \ \text{及其非负线性组合形式}✓$$
$$\qquad \textbf{P5′}✓✓：\text{若发现前三阶仍可行}✓ \Longrightarrow \ \textbf{不要}马上做六维暴力搜索✗✓，\ \text{把结果升级为}\ \boxed{\text{three-moment obstruction absent}}✓✓，\ \textbf{然后才} \text{进入四阶联合}✓✓$$
$$\textbf{⑥ 核心目标（一句话）}✓✓：\ \boxed{\text{Does the four-point equal-weight moment cone impose a genuinely nonlinear compatibility among}\ (Q_1, Q_2, Q_3)\ \text{that excludes}\ (-\infty, -\tfrac12]^3\ ?}✓✓$$
$$\qquad \textbf{本档答案}✓✓：\textbf{否}✗✓（\text{前三阶仍可行}✓，\ \text{数值判定}✓）$$
$$\textbf{⑦ 与}\ C\text{-}380\text{-}23\ \text{的关系}✓✓：\text{两者}\ \textbf{同为负结果}✓✓：\text{二维全覆盖}✓；\text{三阶可达}✓ \Longrightarrow \text{搜索空间}\ \textbf{进一步收窄}✓✓$$
$$\qquad \textbf{清理效果}✓✓：\textbf{现在没有理由}再浪费计算量寻找某个神奇的二阶／三阶组合✗✓$$
$$\textbf{⑧ 下一步}✓✓：\textbf{四阶联合}\ (Q_1, Q_2, Q_3, Q_4)✓✓ \ —— \ \textbf{仍}不上六维暴力✗✓$$

## §1 数值记录（✓✓）

$$\textbf{采样}✓：2 \times 10^5\ \text{点}✓；\ \min\max(\cdot) = -0.593821✓✓ \Longrightarrow \textbf{可达}✓✓$$
$$\textbf{单独极小}✓：\min Q_1 = -3.7928✓，\ \min Q_2 = -3.9886✓，\ \min Q_3 = -3.9807✓✓（\text{三者}\ \textbf{单独} \text{可近}\ -4✓，\ \text{但同时受限时需折中}✓）$$
$$\textbf{三条件同时}✓✓：5409／200000✓✓ \Longrightarrow \textbf{可行集非空}✓（\textbf{数值，非证明}✗✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3` ✓ | **DERIVED／method-family CLOSED** ✓✓ |
| all 2-moment projections ✓ | **INSUFFICIENT** ✗✓ |
| 3-moment `(Q_1, Q_2, Q_3)` ✓ | **本档：INSUFFICIENT（可达）** ✗✓ |
| 4-moment ✓ | **NEXT** ✓✓ |
| `\mathcal F_0` ✓ | **OPEN** ✓ |
| `F_4, p_5, p_6` ✓ | **SEALED** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{六维不可行}✗✓；\ \text{存在四阶联合}\ G✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{有数值采样}✓（\textbf{非}证明✗）；\ \text{三阶负结果为}\ \textbf{采样级}✓✓（\text{非}定理✗）$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}做六维暴力搜索✗；\textbf{不}碰\ F_4／p_5, p_6✗；\textbf{不}碰单一 Fourier certificate✗；\textbf{不}把测度松弛当结论✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（数值采样，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 三阶联合不足 命中文件数=0    :: 
技术词 中心矩偏斜  命中文件数=0    :: 
技术词 四阶联合     命中文件数=1    :: ./C3823-four-atomic-joint-moment-geometry-audit.md 
```
- 运行记录 ✓：`python3 -`（2e5 采样 ＋ 三条件计数 ＋ 中心矩 ✓）
