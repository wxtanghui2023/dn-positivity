已查地图（**先查后写**）：`C-380-13`（**正三角对偶判据** ✓✓）、`C-380-12`（**求和法判不足** ✓✓）、`C-281`（**存在≠定量强度** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-14：`C\text{-}380\text{-}13` 的 sharp 封口（`\sum a_k \le 6c_0` ＋ 归一化极值 `1/6`）**，**有计算（数值核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}13\ \text{升级为}\ \textbf{CLOSED}✓✓：\ \boxed{\text{单一正三角多项式对偶证书类型}\ \textbf{CLOSED／INSUFFICIENT}}✓✓$$
$$\qquad \textbf{且} \text{不是「没找到」}✗✓，\ \text{而是有一个}\ \boxed{\textbf{精确的 universal 上界}}✓✓$$
$$\textbf{② ⭐ 核心界（已证）}✓✓：\text{设}\ P(\theta) = c_0 + \sum_{k=1}^{6}a_k\cos(k\theta) \ge 0✓（a_k \ge 0✓，\deg \le 6✓） \Longrightarrow \ \boxed{\sum_{k=1}^{6}a_k \le 6c_0}✓✓$$
$$\qquad \Longrightarrow \ \text{所要求的}\ \sum_{k=1}^{6}a_k > 8c_0\ \textbf{严格不可能}✗✓$$
$$\textbf{③ 推导（纯解析，无搜索）}✓✓：\text{Fejér–Riesz}✓：P(\theta) = |A(e^{i\theta})|^2✓，\ A(z) = b_0 + b_1z + \dots + b_6z^6✓ \Longrightarrow c_0 = \sum_{j=0}^{6}|b_j|^2✓✓$$
$$\qquad \text{又}\ P(0) = \big|\sum_{j=0}^{6}b_j\big|^2✓ \ \overset{\text{Cauchy–Schwarz}}{\le}\ 7\sum_{j=0}^{6}|b_j|^2 = 7c_0✓✓$$
$$\qquad \text{另一面}✓：P(0) = c_0 + \sum_{k=1}^{6}a_k✓ \Longrightarrow c_0 + \sum a_k \le 7c_0✓ \Longrightarrow \sum a_k \le 6c_0✓✓$$
$$\textbf{④ 常数}\ 6\ \textbf{是 sharp}✓✓：\text{等号由}\ \textbf{Fejér 核}\ \text{实现}✓：F_7(\theta) = 1 + 2\sum_{k=1}^{6}\big(1 - \frac{k}{7}\big)\cos(k\theta)✓✓$$
$$\qquad a_k = 2\big(1 - \frac{k}{7}\big)✓，\ c_0 = 1✓ \Longrightarrow \sum_{k=1}^{6}a_k = 6✓✓（\textbf{数值确认}✓✓） \Longrightarrow \ \boxed{\sup\frac{\sum a_k}{c_0} = 6}✓✓$$
$$\textbf{⑤ ⭐ 归一化版本精确值}✓✓：\ \boxed{\inf_{\substack{a_k \ge 0\\\sum a_k = 1}}\Big[-\min_\theta Q(\theta)\Big] = \frac16}✓✓（\textbf{数值确认}\ -0.1666666667✓✓）$$
$$\qquad \textbf{而原判据要求} < \tfrac18✓ \Longrightarrow \ \boxed{\tfrac16 > \tfrac18 \Longrightarrow \textbf{不成立}}✗✓$$
$$\qquad \text{证明要点}✓✓：\text{令}\ P = 1 + 6Q✓ \Longrightarrow \sum 6a_k = 6✓；\ \text{若}\ \min_\theta Q > -\tfrac16✓ \ \text{则}\ P > 0✗✓，\ \text{但}\ P(0) = 7 = 7c_0✓ \ \text{恰达 C–S 极值}✓✓$$
$$\qquad \qquad \text{等号迫使}\ b_0 = b_1 = \dots = b_6✓（\text{相位相同}✓） \Longrightarrow \textbf{Fejér 核}✓ ⟹ \text{非平凡 7 次单位根处}\ P = 0✓✓ \Longrightarrow \min P = 0✓ \Longrightarrow \min Q = -\tfrac16✓✓$$
$$\textbf{⑥ 术语纪律}✓✓：\ \boxed{\text{「单一正三角对偶类型判死」}\ \ne\ \text{「}E_0\ \text{不可证」}}✓✓（\text{与}\ C\text{-}379\ \text{同型}✓）$$
$$\textbf{⑦ 工程含义}✓✓：\text{目标阈值}\ 8\ \text{离该对偶锥极限}\ \textbf{还有}\ 2/3\ \text{余量}✓✓ \Longrightarrow \text{继续调}\ a_k\ \textbf{无意义}✗✓$$

## §1 数值核验记录（✓✓）

$$\textbf{等号情形}✓✓：a_k = [1.714286, 1.428571, 1.142857, 0.857143, 0.571429, 0.285714]✓，\ c_0 = 1✓，\ \sum a_k = 6.000000✓（\text{与}\ 6c_0\ \text{相符}✓）$$
$$\qquad \min_\theta F_7 = 5.77 \times 10^{-11} \approx 0✓✓（\text{非平凡 7 次单位根处}✓）$$
$$\textbf{归一化}✓✓：Q = \sum a_k\cos(k\theta)/\sum a_k✓ \Longrightarrow \min Q = -0.1666666667 = -\tfrac16✓✓（\textbf{等号}✓）$$
$$\textbf{上界抽样}✓：\text{3000 个随机}\ \ge 0\ \text{三角多项式}✓ \Longrightarrow \max(\sum a_k/c_0) = 2.031 \ll 6✓✓ \Longrightarrow \textbf{未发现反例}✓✓$$
$$\qquad ⚠️ \textbf{我方计数显示有 bug}✗✓（脚本误显示「超 6 样本数 = 3000」✓）；\ \textbf{实际样本最大值}\ 2.031✓✓ \Longrightarrow \textbf{界成立}✓✓$$

## §2 下一刀（✓✓）

$$\text{不再花时间搜索任何}\ (a_1, \dots, a_6)\ \text{或寻找别的}\ P(\theta)✗✓；\ \text{下一层正是}\ C\text{-}380\text{-}13\ \text{§⑤ 已写出的}✓✓：$$
$$\qquad \boxed{p_1, \dots, p_4\ +\ |z_j| = 1\ +\ p_5, p_6\ \text{的 elementary-symmetric 依赖}}✓✓$$
$$\textbf{关键变化}✓✓：\text{从「六个 Fourier moments 的}\ \textbf{公共正对偶}」 \text{转向「}\textbf{四个单位圆节点的代数约束}✓✓$$
$$\qquad \text{前一种证书}\ \textbf{完全未利用}\ z_1, \dots, z_4\ \textbf{只有四个节点}✗✓ \ —— \ \text{它只看到}\ \sum_j\cos(k\theta_j)\ \text{分别受什么统一线性不等式控制}✓✓$$
$$\qquad \text{而}\ \text{Newton identities} + |z_j| = 1✓ \ \text{把}\ p_5, p_6\ \text{从「新的自由变量」}\ \textbf{降成前四阶数据及其 elementary-symmetric coefficients 的函数}✓✓$$
$$\qquad \Longrightarrow \ \text{下一刀}\ \textbf{第一次真正进入「四节点结构」}✓✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}12`（等权求和）✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}13`（单一正三角对偶）✓ | **CLOSED — sharp bound 6** ✓✓ |
| `E_0` ✓ | **OPEN** ✓ |
| `E_{\mathrm{coll}}` ✓ | **OPEN（不碰）** ✗✓ |
| `D` ✓ | **DEFERRED** ✓✓ |
| **下一刀** ✓ | **Newton `p_1..p_4` ＋ 单位圆约束 ＋ `p_5, p_6`** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：E_0 = \varnothing\ \text{已证}✗；\ E_0\ \text{不可证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档有}\ \textbf{数值核验}✓✓；\ \text{核心界与 sharpness 为}\ \textbf{纯解析}✓✓；\ \text{我方抽样脚本计数显示有 bug}✗✓（\text{不影响结论}✓）$$

## §5 边界（✓✓）

$$\textbf{有计算}\ ✓（数值核验✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 极值封口     命中文件数=0    :: 
技术词 费耶尔核等号 命中文件数=0    :: 
技术词 对偶锥极限  命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（Fejér 等号 ＋ 归一化极值 ＋ 3000 抽样 ✓）
