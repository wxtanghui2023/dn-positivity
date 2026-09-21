已查地图（**先查后写**）：`C-380-34`（**Branch C CLOSED** ✓✓）、`C-380-29`（**`A(m)` 精确解** ✓✓）、`C-380-30`（**B 支 6 次分子** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-35：Branch B（临界支 ＋ 多项式降维）（注册）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 设定}✓✓：\text{Branch B}：s = A(m) = \frac{3 + 8m^2 - \frac{1}{8m}}{12}✓✓（Q_3 = -\tfrac12\ \text{激活}✓）；\ t = -m \ge \tfrac18✓✓$$
$$\textbf{② ⭐ B 支可行窗口}✓✓：\text{可行点}\ 7281✓；\ \boxed{m \in [-0.284250, -0.125000]}✓✓ \Longrightarrow \boxed{t \in [\tfrac18,\ 0.284250]}✓✓$$
$$\qquad s \in [0.328745, 0.343750]✓（\textbf{窄}✓）；\ \text{右端}\ t = \tfrac18\ \text{恰好触到}✓✓$$
$$\textbf{③ ⭐⭐ 临界性（本档核心发现）}✓✓：\boxed{\min_{\text{B 支}}Q_5 = \tfrac{89}{32} = 2.78125}✓✓（\text{at}\ m = -\tfrac18✓，s = \tfrac{11}{32}✓）$$
$$\qquad \Longrightarrow \ \boxed{Q_5 - \tfrac{341}{128} = \tfrac{15}{128} = +0.1171875}✓✓ \ —— \ \textbf{小但精确为正}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{B 支是临界支}}✓✓ \ —— \ \text{与 A 支（等号点）相邻，}\ \textbf{一致性良好}✓✓$$
$$\qquad ⚠️ \textbf{重要发现}✗✓：\boxed{Q_5 > 3\ \textbf{在 B 支不成立}}✗✓（\tfrac{89}{32} = 2.781 < 3✓） \ —— \ \textbf{与 A／C 支不同}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{B 支必须证}\ Q_5 > \tfrac{341}{128}\ \text{本身}✓✓，\ \textbf{不能}用\ Q_5 > 3\ \text{的便捷路线}✗✓$$
$$\textbf{④ 纯 t 形式（精确）}✓✓：\boxed{A(-t) = \frac{64t^3 + 24t + 1}{96t}}✓✓（\text{与}\ C\text{-}380\text{-}29\ \text{一致}✓✓）$$
$$\qquad \boxed{Q_5(-t,\ A(-t)) = \frac{16384t^6 - 15360t^4 - 640t^3 + 2880t^2 + 120t - 5}{144t}}✓✓ \ —— \ t = \tfrac18\ \text{给}\ \tfrac{89}{32}✓✓（\textbf{核验}✓）$$
$$\textbf{⑤ ⭐ 线性化（多项式降维）}✓✓：\boxed{Q_5 - \tfrac{341}{128} = \frac{P_B(t)}{1152t}}✓✓，$$
$$\qquad \boxed{P_B(t) = 131072t^6 - 122880t^4 - 5120t^3 + 23040t^2 - 2109t - 40}✓✓；\ \boxed{P_B(\tfrac18) = \tfrac{135}{8}}✓✓（\textbf{精确}✓）$$
$$\qquad \Longrightarrow \ \text{分母}\ 1152t > 0✓（t > 0✓） \Longrightarrow \ \textbf{符号} = \operatorname{sign}P_B(t)✓✓ \ —— \ \textbf{降为单变量多项式正性}✓✓$$
$$\qquad \qquad ⭐ \textbf{比 C 支更干净}✓✓：\textbf{无平方根}✓✓，\ \textbf{无消元}✓✓，\ \textbf{单变量}✓✓$$
$$\textbf{⑥ ⭐ 闭合路线（本档建立）}✓✓：\text{端点值}✓✓：P_B(\tfrac18) = \tfrac{135}{8} \approx 16.875✓✓；\ P_B(0.2845) \approx 371.5✓✓（\textbf{皆正}✓）$$
$$\qquad \text{导数符号}✓✓：P_B'(\tfrac18) \approx 2475 > 0✓✓；\ P_B'(0.2845) \approx -97 < 0✓✓ \Longrightarrow \ P_B\ \textbf{升后降}✓✓$$
$$\qquad \Longrightarrow \ P_B\ \text{的最小值在}\ \textbf{端点}✓✓ \Longrightarrow \ \boxed{P_B \ge \tfrac{135}{8} > 0}✓✓ \Longrightarrow \ \boxed{Q_5 > \tfrac{341}{128}}✓✓$$
$$\qquad \textbf{待补}✗✓：P_B'\ \text{在窗口内}\ \textbf{恰有一个根} \text{的严格证明}✓✓（\text{Sturm／单调性}✓） \ —— \ \textbf{这是 B 支封口的唯一剩余技术步骤}✓✓$$
$$\textbf{⑦ 账本（含措辞采用）}✓✓：\text{见 §2}✓；\ \boxed{\text{Branch C}：\textbf{conditional analytic closure} + \textbf{residual window-origin gap}}✓✓（\text{采纳唐先生措辞}✓）$$
$$\textbf{⑧ 纪律}✓✓：\textbf{不回头修 C}✗✓；\ \textbf{不启动 Level 3}✗✓；\ \boxed{\text{two-level closure} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓$$
$$\qquad \textbf{不}对整个\ t \ge \tfrac18\ \text{证明}✗✓（A\ \text{支教训}✓✓：\text{多项式在不可行区域可能变号}✓✓）；\ \textbf{优先用}\ Q_2, Q_4\ \text{排除危险根}✓✓$$

## §1 数值记录（✓✓）

$$\textbf{窗口}✓：扫\ 40001\ \text{个}\ m✓；\ \text{可行}\ 7281✓；\ m \in [-0.284250, -0.125000]✓✓；\ s \in [0.328745, 0.343750]✓✓$$
$$\textbf{最小值}✓✓：\min Q_5 = +2.7812500000✓✓ \ \text{at}\ m = -0.125✓，\ s = 0.34375 = \tfrac{11}{32}✓✓；（\text{与}\ \tfrac{89}{32}\ \textbf{核验一致}✓）$$
$$\textbf{邻域对照}✓：m = -0.13 \Longrightarrow Q_5 = 2.8610✓；\ m = -0.14 \Longrightarrow 3.0116✓；\ m = -0.2 \Longrightarrow 3.6650✓；\ m = -0.3 \Longrightarrow 3.7141✓✓$$
$$\qquad \Longrightarrow \ \textbf{越往左越大}✓✓，\ \text{最小值确在右端}\ t = \tfrac18✓✓$$
$$\textbf{分母符号}✓✓：1152t > 0✓；\ \text{分子在}\ t = \tfrac18\ \text{处} = \tfrac{135}{8} \ne 0✓✓（\text{故 B 支}\ \textbf{无}等号点✗✓ \ —— \ \text{与 A 支唯一等号点相容}✓✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED（解析）** ✓✓✓ |
| **Branch C** ✓ | **CLOSED（conditional；residual window-origin gap）** ✓✓ |
| **Branch B** ✓ | **本档：临界支；降为单变量 `P_B > 0`；闭合路线建立，单点待补** ✓✓ |
| Level 2 ✓ | **OPEN（仅剩 B 的单点证明）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **尚未完成全局解析证明** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓；\ \textbf{Branch B CLOSED}✗✓（\textbf{单点待补}✓）；\ \text{B 支}\ Q_5 > 3✗✓（\textbf{不成立}✓）$$
$$\textbf{诚实标注}⚠️✓：\text{窗口／}t\text{-形式／线性化}\ \textbf{精确}✓✓；\ \textbf{临界性发现}✓✓；\ P_B'\ \text{单根}\ \textbf{未证}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}回头修 C✗✓；\textbf{不}启动 Level 3✗✓；\textbf{不}对全\ t \ge \tfrac18\ \text{硬证}✗✓；\textbf{不}用\ Q_5 > 3\ \text{路线}✗✓；\textbf{不}上\ SOS／Gram✗$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy ＋ 40001 点扫描，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 临界支        命中文件数=0    ::
技术词 余量细小     命中文件数=0    ::
技术词 单变量多项式正性 命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy `A(-t)`／`Q_5` 纯 `t` 形式／`P_B` 因式 ＋ 40001 点窗口扫描 ✓）
