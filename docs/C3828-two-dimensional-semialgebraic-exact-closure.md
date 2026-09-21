已查地图（**先查后写**）：`C-380-27`（**精确展开 ＋ 网格判定** ✓✓）、`C-380-26`（**two-level 边界** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-28：二维半代数精确闭合（注册＋精确点核验＋松弛对照＋勘误）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（九条 ✓✓）

$$\textbf{① (m,s) 精确形式核验（全部正确）}✓✓：s = m^2 + a^2✓；Q_1 = 4m✓；Q_2 = 4(2s - 1)✓；Q_3 = 4m(-8m^2 + 12s - 3)✓✓$$
$$\qquad Q_4 = 4(-32m^4 + 32m^2s + 8s^2 - 8s + 1)✓✓；\ Q_5 = 4m(-64m^4 + 40m^2 + 80s^2 - 60s + 5)✓✓ \ —— \ \textbf{与唐先生逐项一致}✓✓$$
$$\qquad \Longrightarrow \ \textbf{全部问题压缩到}(m, s)\ \textbf{二维}✓✓ \ —— \ \textbf{比在}(m, a)\ \text{上做网格}\ \textbf{更有价值}✓✓$$
$$\textbf{② ⭐ 精确点核验（符号级）}✓✓：m = -\tfrac18✓，\ s = \tfrac{7}{16}✓ \Longrightarrow a^2 = \tfrac{27}{64}✓，\ a = \tfrac{3\sqrt3}{8} \approx 0.6495190528✓✓$$
$$\qquad Q_1 = -\tfrac12✓，\ Q_2 = -\tfrac12✓（\textbf{两约束同时活跃}✓✓）；\ Q_3 = -\tfrac{17}{16} = -1.0625✓；\ Q_4 = -\tfrac{97}{32} = -3.03125✓✓$$
$$\qquad \Longrightarrow \ \boxed{Q_5 = \tfrac{341}{128} = 2.6640625}✓✓ \ —— \ \textbf{符号验证通过}✓✓；\ \text{数值}\ 2.6642\ \textbf{指向该有理边界点}✓✓$$
$$\textbf{③ ⭐⭐ 数值判定（本档核心）}✓✓：\min_{\{Q_1 \dots Q_4 \le -\frac12\}}Q_5 = \boxed{+2.66406250}✓✓ \ —— \ \textbf{与}\ \tfrac{341}{128}\ \textbf{完全一致}✓✓$$
$$\qquad \textbf{argmin}✓✓：(m, s) = (-0.125, 0.4375) \equiv (-\tfrac18, \tfrac{7}{16})✓✓ \ —— \ \textbf{恰好落在该精确有理点}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\inf_{\text{two-level},\ Q_1 \dots Q_4 \le -\frac12}Q_5 = \tfrac{341}{128}}✓✓ \ \textbf{数值强支持}✓✓ \ —— \ \textbf{Level 2 解析证明的明确靶点}✓✓$$
$$\textbf{④ ⭐ 陷阱验证（关键，采纳唐先生警告）}✗✓：\textbf{仅}用\ Q_1, Q_2\ \text{约束时}\ \min Q_5 = \boxed{-3.9997}✗✗（\text{argmin}\ (m, s) = (-0.308, 0.095)✓）$$
$$\qquad \Longrightarrow \ \textbf{松弛后远低于}\ \tfrac{341}{128}✓✓ \Longrightarrow \ \boxed{Q_1, Q_2\ \textbf{单独远不足}}✗✓ \Longrightarrow \ \boxed{Q_3, Q_4\ \textbf{必须参与}}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不能}写\ Q_1, Q_2 \le -\tfrac12 \Longrightarrow Q_5 \ge \tfrac{341}{128}✗✓（\textbf{这是假的}✗✓）$$
$$\textbf{⑤ 可行域规模}✓✓：\text{四约束可行点数}\ 378211／3267508 \approx 11.6\%✓（\text{基区域}✓）$$
$$\textbf{⑥ Step A／B／C 路线（采纳）}✓✓：\textbf{Step A}✓ \text{消掉}\ a\ \text{用}\ (m, s)✓；\ \textbf{Step B}✓ \text{研究}\ Q_3, Q_4\ \text{对}\ s\ \text{的限制}✓✓（Q_3\ \text{关于}\ s\ \text{线性}✓，Q_4\ \text{二次}✓）$$
$$\qquad \textbf{Step C}✓✓：\text{在区域上证明}\ Q_5 > -\tfrac12✓ \ —— \ \text{可尝试}\ Q_5 + \tfrac12 = \sum_i A_i\cdot(Q_i + \tfrac12) + R✓（R > 0✓）$$
$$\qquad ⚠️ \textbf{防线（`C-380-13`）}✗✓：\textbf{不能}把它退化成\ \sum_k\lambda_kQ_k + C > 0✓（\lambda_k \ge 0✓），\ \textbf{否则} \text{又回到已 CLOSED 的单一正三角／Fourier-dual certificate}✗✓$$
$$\qquad \qquad \Longrightarrow \ \text{若用代数乘子，}\ \textbf{必须保持} \text{它是}\ \textbf{two-level 半代数域的非线性约束证书}✓✓$$
$$\textbf{⑦ }\ Q_6 = Q_2 \cdot W\ \text{备用刀（采纳）}✓✓：\text{因}\ Q_2 \le -\tfrac12 < 0✓ \Longrightarrow Q_6 \le -\tfrac12 \iff W \ge \tfrac{1}{-2Q_2} > 0✓✓$$
$$\qquad \textbf{优先级}✗✓：\textbf{低于}\ Q_5✓✓ \ —— \ \textbf{不要}因为出现漂亮因式分解就把证明目标从\ Q_5\ \text{转移掉}✗✓ \Longrightarrow \ \boxed{Q_5\ \text{是主矛；}Q_6 = Q_2W\ \text{是备用刀}}✓✓$$
$$\textbf{⑧ ⚠️ `C-380-26` 勘误（归因错误）}✗✓：\text{此前报的}「m = 0,\ a \approx 0.7075,\ Q_5 = +4」\ \textbf{不可能成立}✗✓：\text{因}\ m = 0\ \text{时}\ X = \{a, a, -a, -a\}✓，$$
$$\qquad \text{而}\ T_5\ \text{是奇函数}✓ \Longrightarrow \boxed{Q_5 = 0}✓✓ \ —— \ \text{该点实际}\ (Q_1 \dots Q_6) = (0, +0.00445, 0, -3.99999, 0, -0.01335)✓✓$$
$$\qquad \Longrightarrow \ \text{此前的}\ 0.5044\ \text{是}\ \boxed{Q_2}\ \text{在起作用}✓✓（0.00445 + \tfrac12 = 0.50445✓✓），\ \textbf{并非}\ Q_5✗✓；\ \text{真正的}\ Q_5 \approx +4\ \text{对应}\ m \approx -\tfrac14, a \approx 0.5592\ \text{那点}✓✓$$
$$\qquad \Longrightarrow \ \textbf{公式修正把旧数据异常解释干净}✓✓ \ —— \ \text{登记为}\ \textbf{归因勘误}✓✓（\text{不}改「two-level 前六不可行」的结论✓✓）$$
$$\textbf{⑨ 账本定性（采纳）}✓✓：\ \boxed{C\text{-}380\text{-}27 = \textbf{TWO-LEVEL NUMERICAL OBSTRUCTION — STRONG}}✓✓（\textbf{not CLOSED}✗✓）$$
$$\qquad \textbf{纪律}✓✓：\ \boxed{\text{Level 2 CLOSED} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓；\ \text{下一堵墙} = \boxed{\Delta_4 \to 0\ \text{或}\ \Delta_4 \ge \delta(\operatorname{dist}(\cdot, \mathcal T))}✓✓$$

## §1 数值记录（✓✓）

$$\textbf{网格}✓：3001 \times 3001✓（基区点数 3267508✓）；\ \text{四约束可行}\ 378211✓；\ \min Q_5 = +2.66406250✓✓ \ —— \ \text{与}\ \tfrac{341}{128}\ \text{差}\ 0.000e+00✓✓$$
$$\textbf{argmin}✓✓：(m, s) = (-0.125, 0.4375)✓；\ m = -\tfrac18\ \text{成立}✓；\ s = \tfrac{7}{16}\ \text{成立}✓✓$$
$$\textbf{松弛对照}✓✗：\text{仅}\ Q_1, Q_2 \Longrightarrow \min Q_5 = -3.99967114✗✗ \ —— \ \textbf{证明松弛不足}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}27` ✓ | **TWO-LEVEL NUMERICAL OBSTRUCTION — STRONG** ✓✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **本档：数值强支持（argmin 精确命中）** ✓✓ |
| Level 2（解析） ✓ | **NEXT ← 唯一目标（靶点已定）** ✓✓ |
| `Q_1, Q_2` 单独 ✓ | **不足（松弛到 −4）** ✗✓ |
| `Q_6 = Q_2W` ✓ | **备用刀（不抢主线）** ✓✓ |
| Level 3（稳定性） ✓ | **未开** ✗✓ |
| `\mathcal F_0` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓（\textbf{数值}✓）；\ \inf = \tfrac{341}{128}\ \text{已证}✗✓；\ \Delta_4 \ge \delta\ \text{已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{精确形式与精确点}\ \textbf{为符号级}✓✓；\ \inf\ \text{为}\ \textbf{网格级}✓（\textbf{argmin 精确命中}✓✓）；\ C\text{-}380\text{-}26\ \textbf{归因勘误已登记}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}把\ Q_1, Q_2\ \text{单独当证书}✗✓；\textbf{不}退化成\ \sum\lambda_kQ_k + C✓；\textbf{不}从「边界被杀」跳到「完整模型被杀」✗✓；\textbf{不}转\ Q_6\ \text{主线}✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy ＋ 3001^2 网格，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓（\textbf{勘误另记}✓）；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 二维半代数精确闭合 命中文件数=0    :: 
技术词 约束活跃结构 命中文件数=0    :: 
技术词 归因勘误     命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 核验 ＋ 3001² 双网格 ＋ 松弛对照 ✓）
