已查地图（**先查后写**）：`C-380-5`（**勘误 ＋ 五维目标** ✓✓）、`C-380-4`（化简表 ✓✓）、`C-374`（32 层探针 ✓✓）、`C-378`（可行极值点 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-6：五维 odd-state 可逆性 ＋ 低频阈值预检**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① ⭐ 可逆性（本档核心，已证）}✓✓：\ \mathbf F^{(0:4)}_{\mathrm{odd}} = A\,\boldsymbol\mu✓，\ \boldsymbol\mu = (\mu_0, \mu_1, \mu_2, \mu_3, \mu_4)✓✓$$
$$\qquad A = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ -3 & 4 & 0 & 0 & 0 \\ 5 & -20 & 16 & 0 & 0 \\ -7 & 56 & -112 & 64 & 0 \\ 9 & -120 & 432 & -576 & 256 \end{pmatrix}✓✓ \ —— \ \textbf{下三角}✓，\ \textbf{对角} = 2^{2r}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\det A = 2^{20} = 1048576 \ne 0}✓✓ \Longrightarrow \ \textbf{可逆线性变换}✓✓（A^{-1}\ \text{显式已算出}✓）$$
$$\textbf{② ⭐ 低频阈值预检}✓✓：\text{三个}\ E_{\mathrm{even}}\ \text{点}\ \text{全部}\ \min_\sigma\max(|F_1|, |F_3|, |F_5|, |F_7|, |F_9|) > \tfrac12✓✓$$
$$\qquad V_2\ \text{极值}✓（even\text{-}max = 0.4945✓）：\ 1.365952✓✓；\ \Delta\ \text{极值}✓：\ 2.007323✓✓；\ C\text{-}342\ \text{最优}✓：\ 1.546954✓✓$$
$$\qquad \textbf{余量}\ 2.7 \times \sim 4.0 \times✓✓（\text{相对}\ \tfrac12✓） \Longrightarrow \ \textbf{明显非临界}✓✓$$
$$\textbf{③ ⭐ 稳定符号模式（新线索）}✓✓：\text{三点全部的最小}\ \sigma = (1, -1, 1, -1, -1)✓✓（\text{或其反相}✓，\text{由}\ \sigma \leftrightarrow -\sigma\ \text{同值}✓）$$
$$\qquad \Longrightarrow \ \text{可信度}\ \uparrow✓ \ —— \ \textbf{登记为候选结构}✓✓，\ \textbf{不}当作定理✗✓$$
$$\textbf{④ 判定}✓✓：\text{五维坐标化}\ \textbf{成功}✓✓；\ \text{低频五阶}\ \textbf{在已测点上足以} \text{超过}\ \tfrac12✓✓ \Longrightarrow \ \textbf{倾向出口 6A}✓✓$$
$$\qquad \textbf{但}⚠️✓：\text{仅}\ 3\ \text{点}✓ \Longrightarrow \ \textbf{不构成} \text{统一下界}✗✓$$
$$\textbf{⑤ 与既有结论的关系}✓✓：\boldsymbol\mu = A^{-1}\mathbf F^{(0:4)}_{\mathrm{odd}}✓ \Longrightarrow \ \mathcal Z = \{\boldsymbol\mu = 0\} = \{F_1 = F_3 = F_5 = F_7 = F_9 = 0\}✓✓$$
$$\qquad \Longrightarrow \ C\text{-}371\ \text{可精确重述为}\ \boxed{E_{\mathrm{even}} \cap \{F_1 = \dots = F_9 = 0\} = \varnothing}✓✓$$

## §1 矩阵与逆（✓✓）

$$A\ \textbf{显式}✓✓：\text{第}\ r\ \text{行} = R_r\ \text{的系数向量}✓（r = 0..4✓）；\ \text{对角}\ (1, 4, 16, 64, 256) = 2^{2r}✓✓$$
$$A^{-1}\ \textbf{显式}✓✓：\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 3/4 & 1/4 & 0 & 0 & 0 \\ 5/8 & 5/16 & 1/16 & 0 & 0 \\ 35/64 & 21/64 & 7/64 & 1/64 & 0 \\ 63/128 & 21/64 & 9/64 & 9/256 & 1/256 \end{pmatrix}✓✓$$
$$\textbf{含义}✓✓：\mu_m\ \text{可由}\ F_1, F_3, \dots, F_{2m+1}\ \text{显式线性表示}✓✓ \Longrightarrow \ \text{五维状态与五个低奇频}\ \textbf{同一信息}✓✓$$
$$\qquad \Longrightarrow \ \text{可把}\ \text{Bridge A}\ \text{改写成}\ \text{五个低奇频的}\ \textbf{联合} \text{问题}✓✓，\ \textbf{不必}先提\ \mu_m✗✓$$

## §2 阈值预检细节（✓✓）

$$\textbf{三点}✓✓：V_2\ \text{极值}\ (even\text{-}max\ 0.4945✓)：\min_\sigma\max = 1.365952✓，\ \text{该}\ \sigma\ \text{下}\ (F_1, F_3, F_5, F_7, F_9) = (-0.1874, 0.3440, 1.3660, 1.0212, -0.8305)✓✓$$
$$\qquad \Delta\ \text{极值}\ (even\text{-}max\ 0.2006✓)：2.007323✓，\ (F) = (-0.9120, 1.9384, 2.0073, -0.3162, 1.5881)✓✓$$
$$\qquad C\text{-}342\ \text{最优}\ (even\text{-}max\ 0.3254✓)：1.546954✓，\ (F) = (-1.5470, -0.6381, 0.6232, 0.2719, -0.6194)✓✓$$
$$\textbf{观察}✓✓：\text{最小值} \text{总在}\ \sigma = (1, -1, 1, -1, -1)✓ \ \text{处达到}✓ \ —— \ \textbf{三点一致}✓✓$$
$$\qquad \text{且}\ \text{三点中}\ \textbf{最大} \text{的}\ |F| \ \text{分别由}\ F_5, F_5, F_1\ \text{达到}✓✓（\text{非} \text{固定} r✓）$$

## §3 分叉（✓✓，唐先生口径 ✓）

$$\textbf{6A}✓✓：\text{若证}\ \inf_{E_{\mathrm{even}}}\min_\sigma\max_{0 \le r \le 4}|F_{2r+1}| > \tfrac12✓ \Longrightarrow \textbf{Bridge A 直接关闭}✓✓ \ —— \ \textbf{不需要}\ F_{11}, \dots, F_{25}✓✓$$
$$\textbf{6B}✓：\text{若存在}\ \max_{r \le 4}|F_{2r+1}| \le \tfrac12✓ \Longrightarrow \textbf{不}判死✗✓，\ \text{须利用}\ F_{11}, \dots, F_{25}\ \text{对}\ \textbf{同一五维状态} \text{的}\ \textbf{额外观测方向}✓✓$$
$$\qquad \textbf{关键}✓✓：\text{高频}\ \textbf{不}产生新自由变量✗，\ \text{而是在同一五维}\ \text{odd state 上}\ \textbf{增加观测}✓✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}3` ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}4`（`\mathcal Z` 上一维）✓ | **CLOSED（限定于 `\mathcal Z`）** ✓✓ |
| `C\text{-}380\text{-}5`（勘误 ＋ 五维修正）✓ | **CLOSED** ✓✓ |
| `\mu_4` 单独幅度路线 ✓ | **NO-GO** ✓✓ |
| 五维联合 odd-state ✓ | **OPEN（本档坐标化完成）** ✓✓ |
| 低频五阶阈值 `> \tfrac12` ✓ | **3 点通过（未证）** ⚠️✓ |
| `C\text{-}380\text{-}6` ✓ | **CLOSED（可逆性已证 ＋ 预检 3/3）** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 下一步（✓✓）

$$\textbf{唯一下一刀}✓✓：\text{证}\ \inf_{E_{\mathrm{even}}}\min_\sigma\max_{0 \le r \le 4}|F_{2r+1}| > \tfrac12✓（\textbf{6A}✓） \ —— \ \textbf{不}做优化✗、\textbf{不}随机搜索✗✓$$
$$\textbf{手段}✓✓：\text{先用}\ \textbf{稳定符号模式}\ \sigma^* = (1, -1, 1, -1, -1)✓✓ \ \text{作}\ \textbf{候选承诺}✓，\ \text{再证}\ \max_{r \le 4}|F_{2r+1}| > \tfrac12\ \text{on}\ E_{\mathrm{even}}✓✓$$
$$\textbf{若}\ 6A\ \text{失败}✓ \Longrightarrow \text{才进入}\ F_{11}, \dots, F_{25}\ \text{的}\ \textbf{五维额外观测}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 五维状态可逆 命中文件数=0    :: 
技术词 低频阈值预检 命中文件数=0    :: 
技术词 稳定符号模式 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（`A` 符号构造 ＋ `\det` ＋ `A^{-1}` ＋ 三点预检 ✓）
- **本档有计算**（符号＋数值，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：`\det A = 2^{20} \ne 0` 为**严格**（符号 ✓）；阈值预检仅 **3 点** ✗✓，**不构成**统一下界 ✓；稳定符号模式为**线索** ✓
- **不得**写成：Bridge A 已闭合 ✗；低频五阶阈值已证 ✗；`\sigma^*` 为定理 ✗；`H = \varnothing` 已证 ✗
