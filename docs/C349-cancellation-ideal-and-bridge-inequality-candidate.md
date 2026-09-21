已查地图（**先查后写**）：`C-348`（反称族 `\not\subset E`✓；成本 ≈ 1.14✓）、`C-347`（奇偶层分离 ✓✓；反称障碍 ✓）、`C-343`（straddling ✓✓）、`C-341`／`C-336`（矩不等式 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-349：抵消理想 ＋ 桥不等式候选**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 逻辑锁死（采纳唐先生）}✓✓：\text{反称族}\ \not\subset E✓ \ \textbf{不}\ \text{等于「近反称配置有正奇频下界」}✗✓ \ —— \ \textbf{稳定性／量化}\ \text{仍缺}✗$$
$$\textbf{② ⭐ 抵消理想已精确化}✓✓：\text{全部奇频为}\ 0 \iff \sum_j w_j x_j^m = 0\ (m = 0,1,2,3)✓✓（w_j := \sigma_j\sqrt{x_j}✓）$$
$$\qquad \textbf{理由}✓✓：\{R_0, R_1, R_2, R_3\}\ \text{张成}\ \deg \le 3\ \text{的多项式空间}✓（\deg R_r = r✓）\ \Longrightarrow \text{四矩消失} \iff \text{低阶 Chebyshev 矩全消失}✓✓$$
$$\textbf{③ 等价形式（正负部）}✓✓：\ \sum_j w_j x_j^m = 0\ (m \le 3) \iff \mu_+ \ \text{与}\ \mu_- \ \text{的前四矩相等}✓✓（\mu_\pm\ \text{为}\ \sigma_j = \pm 1\ \text{的两部分}✓）$$
$$\qquad \text{总原子数}\ 5 \Longrightarrow (p, q) \in \{(1,4),\ (2,3),\ (3,2),\ (4,1)\}✓ \Longrightarrow r = 4 = p + q - 1✓✓ \ \textbf{恰为 Gauss 型边界}✓$$
$$\textbf{④ 桥命题形态（未证）}✗：\text{奇频小} \Longrightarrow \text{近抵消} \Longrightarrow \text{偶频成本}✓；\text{但}\ \textbf{量化版本} \text{未证}✗✓$$
$$\textbf{⑤ 判死标准（唐先生预设）}✓✓：\text{若桥不等式写不出}✓ \Longrightarrow \textbf{立即封口}✓，\textbf{不}\ \text{回到数值搜索循环}✗$$

## §1 A 路：偶层量与 `s` 表达式（✓✓）

$$F_2 = 2s_1 - 5✓；\ F_4 = 8s_2 - 8s_1 + 5✓；\ F_6 = 32s_3 - 48s_2 + 18s_1 - 5✓；\ F_8 = 128s_4 - 256s_3 + 160s_2 - 32s_1 + 5✓$$
$$\textbf{已有约束}✓：s_1 \le \tfrac{11}{4}✓；\ s_2 \le s_1 - \tfrac{9}{16}✓；\ s_2 \ge \tfrac{11}{12}✓；\ s_1 \ge s_2 \ge s_3 \ge s_4 \ge 0✓$$
$$\textbf{偶层量候选}✓：D_{\mathrm{asym}} := \sum_{j} \sum_{l} (x_j - x_l)^2✓（\text{「离加倍结构多远」}✓）\ \text{或}\ D' := \sum_j x_j(1-x_j)✓（= s_1 - s_2 \ge \tfrac{9}{16}✓）$$
$$\textbf{关键观察}✓✓：\text{反称族}\ x = (a^2, a^2, b^2, b^2, 0)✓ \ \text{是}\ \textbf{加倍＋含零} \text{结构}✓ \Longrightarrow \text{偶约束对}\ \textbf{该结构} \text{收费}\ \ge 1.4677✗（C-348✓）$$
$$\qquad \textbf{但}✗✓：\text{偶约束}\ \textbf{看不见符号}✓（\text{只依赖}\ x✓）\ \Longrightarrow \text{「离反称多远」}\ \textbf{不能} \text{由}\ x\ \text{本身单独度量}✗✓ \ —— \ \text{这正是}\ §0①\ \text{缺口的来源}✓✓$$

## §2 B 路：抵消的精确刻画（✓✓，本档核心 ✓）

$$\textbf{设定}✓：\text{固定}\ \sigma✓，w_j := \sigma_j\sqrt{x_j}✓，\ |w_j| = \sqrt{x_j}✓；\ \text{带号测度}\ \mu_\sigma = \sum_j w_j \delta_{x_j}✓$$
$$\textbf{奇频}✓：F_{2r+1} = \int R_r\, d\mu_\sigma✓（\text{由}\ T_{2r+1}(c) = c R_r(c^2)✓）$$
$$\textbf{假设（奇频全小）}✓：|F_{2r+1}| \le \tfrac12\ (r \le 12)✓ \Longrightarrow \text{特别}\ |\int R_r\,d\mu_\sigma| \le \tfrac12\ (r = 0,1,2,3)✓✓$$
$$\Longrightarrow \ \boxed{\text{奇频小} \Longrightarrow \mu_\sigma\ \text{的前四阶（Chebyshev／幂）矩}\ \textbf{≈ 0}}✓✓ \Longrightarrow \textbf{近似抵消}✓$$
$$\textbf{精确零情形}✓✓：\text{四矩恰为 0} \iff \mu_+ = \mu_-\ \text{前四矩}✓ \Longrightarrow \textbf{已知实例} = \text{反称族}✓（C-348✓）$$
$$\textbf{反向（待证）}✗：\text{四矩}\ \textbf{小} \Longrightarrow x\ \text{近加倍结构}✓ \Longrightarrow \text{偶频成本} > \tfrac12✓ \Longrightarrow x \notin E✓✓ \ —— \ \textbf{本档未给出该量化步}✗$$

## §3 桥不等式候选（✓，登记不执行 ✓）

$$\textbf{形态}✓✓：\ \exists\ \eta > 0✓：\ \max_{r \le 3} |F_{2r+1}| \le \tfrac12 \ \Longrightarrow \ \max_{r \le 12} F_{2r} \ge \tfrac12 + \eta✓ \quad（\text{对全部}\ \sigma✓）$$
$$\qquad \textbf{等价读法}✓：\text{奇频若被压到}\ \tfrac12\ \text{以下}✓，\text{则偶频}\ \textbf{必然} \text{突破}\ \tfrac12 + \eta✓ \Longrightarrow \textbf{二者不可兼得}✓✓$$
$$\textbf{为何比}\ Q_\sigma\ \textbf{更优}✓✓：\text{它}\ \textbf{显式} \text{使用}\ C\text{-}347\ \text{与}\ C\text{-}348\ \text{的逻辑关系}✓✓ \ —— \ \text{而非直接构造线性组合}✓$$
$$\textbf{关键中间步}✓（\text{须先证}✓）：\text{四阶矩小} \Longrightarrow \text{原子位置近加倍}✓ \ —— \ \text{可用}\ \textbf{矩问题稳定性}（\text{有限原子}\ \Rightarrow\ \text{矩映射的定量单射性}）✓✓$$
$$\textbf{另一路线}✓：\text{直接用}\ \textbf{Gauss 型边界条件}✓（p + q = 5✓，r = 4✓）\ \text{的分类}✓ \Longrightarrow \text{零矩配置的完全分类}✓✓（\text{只余有限自由度}✓）$$

## §4 状态表（✓✓）

| 项 | 状态 |
|---|---|
| 反称族 `\not\subset E` ✓ | **数值确认（4{,}004{,}001 点）** ✓ |
| 非对称性成本 ✓ | **≈ 1.14（数值）** ✓ |
| 抵消理想 ✓ | **精确化：前四矩为 0** ✓✓ |
| 正负部匹配 ✓ | **`r = p + q - 1` Gauss 边界** ✓✓ |
| 桥不等式 ✓ | **候选形态已写，未证** ✗ |
| 量化稳定性 ✓ | **未给（最大缺口）** ✗ |
| `H = \varnothing` ✓ | **OPEN** ✓ |
| `SOS`／数值循环 ✓ | **冻结／禁止** ✗ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 抵消结构     命中文件数=2    :: ./literature-level-repulsion.md ./laguerre-spectrum-path.md 
技术词 矩匹配        命中文件数=0    :: 
技术词 正负部        命中文件数=1    :: ./V185-paper-reading-notes-arXiv-2608-13637.md 
技术词 稳定抵消界  命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：桥不等式已证 ✗；非对称性成本是稳定性定理 ✗（**仅族级数值现象** ✓）；`H = \varnothing` 已证 ✗；反称已解析排除 ✗
