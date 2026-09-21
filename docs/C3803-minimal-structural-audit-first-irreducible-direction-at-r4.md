已查地图（**先查后写**）：`C-380-2`（**高阶检测问题** ✓✓）、`C-349`（**四阶 nullspace** ✓✓）、`C-347`（`R_r` 表 ✓✓）、`C-378`（**可行点** `x` 互异 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-3：结构性最小审计（`r > 3` 是否产生不可约新方向）**，**零计算（纯代数 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 低阶基完备}✓✓：R_0 = 1✓，R_1 = 4x - 3✓，R_2 = 16x^2 - 20x + 5✓，R_3 = 64x^3 - 112x^2 + 56x - 7✓ \ —— \ \textbf{次数} \text{分别} 0,1,2,3✓，\ \textbf{首项非零}✓✓$$
$$\qquad \Longrightarrow \ \{R_0, R_1, R_2, R_3\}\ \text{是}\ \mathbb{R}_{\le 3}[x]\ \text{的一组}\ \textbf{基}✓✓ \Longrightarrow \ r \le 3\ \text{的奇频}\ \textbf{是四阶 signed moments 的线性组合}✓✓$$
$$\qquad \Longrightarrow \ \textbf{在四阶 nullspace 上}\（\sum_j w_jx_j^m = 0✓，m = 0,1,2,3✓）：\boxed{F_1 = F_3 = F_5 = F_7 = 0}✓✓（\text{与 C-349 一致}✓）$$
$$\textbf{② ⭐ 高阶新方向（本档核心）}✓✓：R_r\ \text{次数} = r \ge 4✓ \Longrightarrow \text{作为}\ \textbf{5 个互异节点} \text{上的函数}✓，\ \{1, x, x^2, x^3, x^4\}\ \textbf{线性无关}✓✓$$
$$\qquad （\text{Vandermonde 矩阵行列式} \ne 0✓） \Longrightarrow \ \boxed{R_4\ \text{不在}\ \operatorname{span}\{1, x, x^2, x^3\}\ \text{中}}✓✓ \Longrightarrow \ \textbf{不可由四阶 signed moments 线性表示}✓✓$$
$$\qquad \Longrightarrow \ \text{同理}\ \text{一切}\ r \ge 4✓ \Longrightarrow \ \boxed{r_* = 4\ \text{是第一个不可约新方向}}✓✓$$
$$\textbf{③ 判定}✓✓：\ \text{结构层面}\ \textbf{存在不可约新方向}✓✓ \Longrightarrow \ \textbf{出口 A（结构层面）}✓✓ \ —— \ \textbf{不是}\ \text{又一轮}\ \mathcal Z\ \text{重包装}✗✓$$
$$\textbf{④ 退化情形}⚠️✓：\text{若节点碰撞}（x_i = x_j✓） \Longrightarrow \text{秩下降}✗✓ \Longrightarrow \textbf{须单独处理}✓✓（E_{\mathrm{even}}\ \text{内极值点已核}\ x\ \text{互异}✓，\text{C-378}✓）$$
$$\textbf{⑤ ⭐ 重要限定}✓✓：\text{本刀}\ \textbf{只回答「是否存在新方向」}✓✓（\textbf{是}✓）；\ \textbf{不}回答\ \textbf{阈值幅度}✗✓ \ —— \ > \tfrac12\ \text{的}\ \textbf{统一下界仍未被证明}✗✓$$
$$\textbf{⑥ 候选（登记）}✓✓：\ \boxed{\mathfrak C_4(x,\sigma) = \sum_j \sigma_j\sqrt{x_j}\,R_4(x_j)}✓✓ \ —— \ \text{但}\ \textbf{须先} \text{检查它在}\ E_{\mathrm{even}}\ \text{上是否给出}\ \textbf{统一幅度下界}✓✓（\textbf{最后一公里}✓）$$

## §1 为什么 `r \le 3` 恒为零（✓✓）

$$\textbf{关键}✓✓：\text{四阶条件}\ \sum_j w_jx_j^m = 0\（m = 0,1,2,3✓）\ \text{恰为}\ \text{对}\ x^m\ \text{的}\ \textbf{测试}✓✓$$
$$\qquad \Longrightarrow \ \text{任何}\ \deg \le 3\ \text{的多项式}\ p✓：\sum_j w_j\,p(x_j) = 0✓✓ \ —— \ \text{因}\ p = \sum_{m \le 3}c_mx^m✓$$
$$\qquad \text{且}\ R_r\ \text{对}\ r \le 3\ \text{恰为}\ \deg \le 3✓✓ \Longrightarrow F_{2r+1} = 0\ \text{on}\ \mathcal Z_x✓✓（\text{四阶 nullspace}✓）$$
$$\textbf{意义}✓✓：\text{低阶奇频}\ \textbf{看不到} \text{nullspace 内的运动}✗✓ \ —— \ \text{这正是}\ C\text{-}380\text{-}2\ \text{所述「仅四阶即退化成」}\ \text{的结构根源}✓✓$$

## §2 为什么 `r \ge 4` 是新方向（✓✓）

$$\textbf{Vandermonde}✓✓：\text{对互异}\ x_1, \dots, x_5 \in [0,1]✓，\ \det\big(x_j^{k}\big)_{j,k=0..4} = \prod_{i<j}(x_j - x_i) \ne 0✓✓$$
$$\qquad \Longrightarrow \ \{1, x, x^2, x^3, x^4\}\ \text{在节点集上}\ \textbf{线性无关}✓✓ \Longrightarrow x^4 \notin \operatorname{span}\{1, x, x^2, x^3\}✓✓$$
$$\qquad \text{且}\ R_4 = 256x^4 + \cdots✓（\text{首项系数} 2^{8} = 256 \ne 0✓） \Longrightarrow R_4 \notin \operatorname{span}\{1, x, x^2, x^3\}✓✓$$
$$\textbf{推论}✓✓：\text{存在}\ w \in \mathcal Z_x\ \text{使}\ \sum_j w_jR_4(x_j) \ne 0✓✓ \Longrightarrow \ r = 4\ \text{方向}\ \textbf{不可约}✓✓$$

## §3 出口与账本（✓✓）

$$\textbf{出口 A（结构层面命中）}✓✓：\text{高阶方向}\ \textbf{确实} \text{超出四阶 nullspace}✓✓ \Longrightarrow \text{依 C-380-2 的约定}✓，\ \text{可进}\ \textbf{幅度审计}✓✓$$
$$\textbf{但}⚠️✓：\text{出口 A 的}\ \textbf{强形式}（\textbf{统一阈值传播}\ \max_{r > 3}|F_{2r+1}| > \tfrac12✓）\ \textbf{尚未}达成✗✓$$
$$\textbf{不构成}✗✓：\text{本刀}\ \textbf{不}证明\ \text{Bridge A}✗；\ \textbf{不}排除\ \text{幅度仍可能}\ \le \tfrac12✗✓$$

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}2` ✓ | **OPEN（保持）** ✓✓ |
| `C\text{-}380\text{-}3`（本刀）✓ | **CLOSED：`r_* = 4` 为首个不可约方向** ✓✓ |
| `\mathfrak C_4` 幅度审计 ✓ | **OPEN ← 最后一公里** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 下一步（✓✓）

$$\textbf{唯一下一刀}✓✓：\text{对}\ \mathfrak C_4(x,\sigma) = \sum_j \sigma_j\sqrt{x_j}R_4(x_j)✓ \ \text{问}\ \textbf{幅度}✓：\ \inf_{x \in E_{\mathrm{even}}}\min_{\sigma}\max_{r}|F_{2r+1}| > \tfrac12\ ?✓✓$$
$$\textbf{禁项}✓✓：\textbf{不}随机搜索✗；\textbf{不}优化✗（\textbf{先} \text{结构判断}✓）；\textbf{不}把\ \text{新方向}\ \text{当作阈值传播的证明}✗✓$$

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \text{阈值传播已证}✗；\ r_* = 4\ \text{给出}\ > \tfrac12\ \text{下界}✗；\ H = \varnothing\ \text{已证}✗$$
$$\textbf{诚实标注}⚠️✓：\text{本刀}\ \textbf{纯代数}✓（Vandermonde ＋ 次数）✓，\ \textbf{零计算}✓；\ \text{退化情形}（节点碰撞）\ \textbf{未}纳入✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 低阶基完备  命中文件数=0    :: 
技术词 范德蒙无关性 命中文件数=0    :: 
技术词 不可约新方向 命中文件数=0    :: 
```
- **零计算** ✗（纯代数 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
