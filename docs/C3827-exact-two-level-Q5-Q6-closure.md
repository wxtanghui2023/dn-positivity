已查地图（**先查后写**）：`C-380-26`（**two-level 前四可行／前六被 `Q_5` 杀（网格级）** ✓✓）、`C-380-25`（**四阶线索** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-27：Exact Two-Level `Q_5/Q_6` Closure（注册＋精确展开＋关键判定）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 参数化 ＋ 纪律}✓✓：X_1 = X_2 = m + a✓，\ X_3 = X_4 = m - a✓ \Longrightarrow Q_k = 2T_k(m + a) + 2T_k(m - a)✓✓$$
$$\qquad \textbf{纪律}✓✓：\text{这些展开式}\ \textbf{只是坐标化}✗✓，\ \textbf{不是}新的「identity branch」✗✓；\ \text{用途}\ \textbf{只有一个}✓：\ Q_k(m, a) \le -\tfrac12\ \text{的联合半代数可行性分析}✓✓$$
$$\textbf{② ⭐ 精确展开（含两处因子勘误）}✗✓：$$
$$\qquad \boxed{Q_1 = 4m}✓✓；\ \boxed{Q_2 = 8(m^2 + a^2) - 4}✗✓ \ —— \ \textbf{唐先生写}\ 4(m^2 + a^2) - 4✗✓（\textbf{差因子}\ 2✗）$$
$$\qquad \boxed{Q_3 = 16m^3 + 48ma^2 - 12m = 4m(4m^2 + 12a^2 - 3)}✗✓ \ —— \ \textbf{唐先生写}\ 8m(m^2 + 3a^2) - 12m✗✓（\textbf{三次项差因子}\ 2✗）$$
$$\qquad Q_4 = 4\big(8a^4 + 48a^2m^2 - 8a^2 + 8m^4 - 8m^2 + 1\big)✓✓$$
$$\qquad Q_5 = 4m\big(80a^4 + 160a^2m^2 - 60a^2 + 16m^4 - 20m^2 + 5\big)✓✓$$
$$\qquad ⭐ \ Q_6 = 4(2a^2 + 2m^2 - 1)\big(16a^4 + 224a^2m^2 - 16a^2 + 16m^4 - 16m^2 + 1\big)✓✓$$
$$\textbf{③ ⭐ 约束修正}✗✓：Q_1 = 4m \le -\tfrac12 \Longrightarrow \boxed{m \le -\tfrac18}✓✓（\text{对}✓）$$
$$\qquad Q_2 = 8(m^2 + a^2) - 4 \le -\tfrac12 \Longrightarrow \boxed{m^2 + a^2 \le \tfrac{7}{16}}✗✓ \ —— \ \textbf{唐先生写}\ \tfrac78✗✓（\textbf{差因子}\ 2✗）$$
$$\qquad \qquad \text{即}\ \text{two-level 可行域}\ \textbf{更紧}✓✓ \ —— \ \textbf{这对后续审计是}\ \textbf{有利}✓✓$$
$$\textbf{④ ⭐⭐ 关键判定（本档核心）}✓✓：\min_{Q_1..Q_4 \le -\frac12}Q_5 = \boxed{+2.6642}✓✓（\text{目标：}> -\tfrac12✓✓；\ \textbf{余量}\ 3.16✓✓）$$
$$\qquad \Longrightarrow \ \textbf{在 two-level 集合上，前四约束}\ \textbf{强烈} \text{推出}\ Q_5 > -\tfrac12✓✓ \Longrightarrow \ \textbf{Level 2 数值上强支持}✓✓$$
$$\qquad \textbf{最小值点}✓✓：(m, a) = (-0.125, 0.6495)✓，\ Q_1 = -0.5000✓✓（\textbf{恰好取等，约束活跃}✓），\ Q_2 = -0.5002✓✓（\textbf{近活跃}✓），\ Q_3 = -1.0624✓，\ Q_4 = -3.0312✓，\ Q_5 = +2.6642✓，\ Q_6 = +0.8363✓$$
$$\qquad \Longrightarrow \ \textbf{结构}✓✓：\ Q_5\ \text{的最小在}\ \textbf{「第一、二约束同时活跃」}\ \text{的边界上取到}✓✓$$
$$\textbf{⑤ ⭐ `Q_6` 因式结构（新发现）}✓✓：\ \boxed{Q_6 = Q_2 \cdot W(m, a)}✓✓（W = 16a^4 + 224a^2m^2 - 16a^2 + 16m^4 - 16m^2 + 1✓）$$
$$\qquad \Longrightarrow \ Q_6 \le -\tfrac12 \iff Q_2 \cdot W \le -\tfrac12✓ \Longrightarrow \text{在}\ Q_2 \le -\tfrac12\ \text{下，}\ Q_6\ \text{条件化为对}\ W\ \text{的}\ \textbf{下界要求}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{比单独处理}\ Q_6\ \textbf{干净}✓✓$$
$$\textbf{⑥ 27-D 修正}✗✓：\text{数值最优点在}\ \boxed{m = -\tfrac18}✓✓（\textbf{非}\ -\tfrac14✗✓ \ —— \ \textbf{唐先生猜测}\ m \approx -\tfrac14\ \text{应修正}✓✓）；\ \text{但}\ m = -\tfrac14\ \text{仍值得解析检查}✓✓$$
$$\textbf{⑦ 三级成功标准（采纳）}✓✓：$$
$$\qquad \textbf{Level 1（数值）}✓：\min_{\text{two-level}}\max_{k \le 6}(Q_k + \tfrac12) > 0✓ \Longrightarrow \text{只能记}\ \boxed{\text{two-level numerically infeasible}}✓✓$$
$$\qquad \textbf{Level 2（精确 two-level closure）}✓✓：\text{证明}\ Q_1, \dots, Q_4 \le -\tfrac12 \Longrightarrow Q_5 > -\tfrac12✓✓ \Longrightarrow \ \boxed{\textbf{Exact two-level obstruction}}✓✓$$
$$\qquad \textbf{Level 3（回到完整}\ \mathcal F_0✓）✓✓：\text{还须证}\ \text{一般四点若逼近}\ E_0\ \text{边界必有}\ \Delta_4 \to 0✓ \ \text{或}\ \Delta_4 \ge \delta(\text{dist})✓✓$$
$$\qquad \qquad \textbf{只有 Level 2 本身不能推出}\ \mathcal F_0 = \varnothing✗✓ \ —— \ \textbf{这点必须守住}✓✓$$
$$\textbf{⑧ 路线链}✓✓：\boxed{2\text{-moment} \times \text{FAIL} \to 3\text{-moment sampling-feasible} \to 4\text{-moment sampling-feasible}＋\Delta_4 \approx 0 \Longrightarrow \text{two-level boundary} \Longrightarrow Q_5 \Longrightarrow \text{exact two-level closure?}}✓✓$$

## §1 数值记录（✓✓）

$$\textbf{网格}✓：2001 \times 2001✓；\ \text{前四可行点数}\ 55281✓；\ \min Q_5 = +2.66418623✓✓ \Longrightarrow > -\tfrac12✓$$
$$\textbf{最优点}✓✓：(m, a) = (-0.125, 0.6495)✓；\ (Q_1, \dots, Q_6) = (-0.5000, -0.5002, -1.0624, -3.0312, +2.6642, +0.8363)✓✓$$
$$\textbf{⚠️ 诚实标注}✗✓：\textbf{局部精化（Nelder–Mead）六起点全部}\ \textbf{未通过} \text{严格可行性检查}✓ \Longrightarrow \textbf{未得精化结果}✗✓；\ \text{网格级结论}\ \textbf{有效}✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 2D／3D／4D ✓ | **INSUFFICIENT（采样级）** ✗✓ |
| `\Delta_4 \approx 0` 线索 ✓ | **KEY CLUE** ✓✓ |
| two-level 精确展开 ✓ | **本档完成（含两处勘误）** ✓✓ |
| `Q_6 = Q_2 W` ✓ | **新结构（已登记）** ✓✓ |
| `Q_5 > -\tfrac12` on 前四约束 ✓ | **本档：网格级强支持（余量 3.16）** ✓✓ |
| Level 2（解析） ✓ | **NEXT ← 唯一目标** ✓✓ |
| Level 3（稳定性） ✓ | **未开** ✗✓ |
| `\mathcal F_0` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Exact two-level obstruction 已证}✗✓（\textbf{网格级}✓）；\ \Delta_4 \ge \delta\ \text{已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{精确展开为}\ \textbf{符号级}✓✓；\ Q_5\ \text{判定为}\ \textbf{网格级}✓；\ \text{精化未成功}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}开一般五阶六维搜索✗✓；\textbf{不}造\ \text{identity}✗；\textbf{不}从「边界被杀」跳到「完整模型被杀」✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy ＋ 网格，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 两点级精确展开 命中文件数=0    :: 
技术词 因式结构     命中文件数=0    :: 
技术词 三级成功标准 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 精确展开 ＋ 2001² 网格 ＋ Nelder–Mead 尝试 ✓）
