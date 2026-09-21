已查地图（**先查后写**）：`C-380-6`（**`\det A = 2^{20}` ＋ 预检 3/3** ✓✓）、`C-380-5`（**五维目标** ✓✓）、`C-371`（`\mathcal Z \cap E = \varnothing` ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-7：五个低奇频的全域可行性排除（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 证明纪律修正（采纳）}✓✓：\sigma_* = (1, -1, 1, -1, -1)✓ \ \textbf{只是候选极值层}✓✓，\ \textbf{不得承诺} \text{为全域最坏层}✗✓$$
$$\qquad \textbf{真正需证}✓✓：\ \forall x \in E_{\mathrm{even}}✓：\ \min_{\sigma \in \mathcal S}\max_{0 \le r \le 4}|F_{2r+1}(x, \sigma)| > \tfrac12✓✓$$
$$\qquad \textbf{不得}只证\ \max_{r \le 4}|F_{2r+1}(x, \sigma_*)| > \tfrac12✗✓ \ —— \ \text{因仍可能存在另一}\ \sigma\ \text{使 odd-max 更小}✗✓$$
$$\textbf{② 第一刀的正确用法}✓✓：\ \boxed{\text{先审计}\ \sigma_*\ \text{是否具有}\ \textbf{可证明的结构优势}}✓✓$$
$$\qquad \text{例如}：\text{能否从}\ E_{\mathrm{even}}\ \text{的约束推出某个}\ \textbf{固定频率} \text{满足}\ |F_{2r+1}(x, \sigma_*)| > \tfrac12✓✓$$
$$\qquad \textbf{若能}✓ \Longrightarrow \text{再问其余}\ 15\（\text{或}\ 8\ \text{对}✓）\ \text{个层是否可由}\ \textbf{对称性／排列／符号等价} \text{压缩}✓✓$$
$$\textbf{③ ⭐ C-380-7 最小目标（本档核心）}✓✓：\ \boxed{E_{\mathrm{even}} \cap \bigcap_{r=0}^{4}\big\{|F_{2r+1}| \le \tfrac12\big\} = \varnothing}✓✓$$
$$\qquad \textbf{等价形式}✓✓（\text{有限半代数可行性}✓）：\begin{cases} F_{2r}(x) \le \tfrac12✓, & r = 1, \dots, 12✓ \\ |F_{2r+1}(x, \sigma)| \le \tfrac12✓, & r = 0, \dots, 4✓ \end{cases}$$
$$\qquad \text{其中}\ x_j \in [0,1]✓，\ \sigma\ \text{仅}\ 16\（8\ \text{对}✓）\ \text{层}✓✓$$
$$\textbf{④ 收益}✓✓：\text{若证可行域为空}✓ \Longrightarrow \textbf{Bridge A 立即关闭}✓✓，\ \textbf{完全不需要}\ F_{11} - F_{25}✓✓$$
$$\textbf{⑤ 可用资产}✓✓：A\ \text{可逆}✓（\det = 2^{20}✓✓）；\ F_{2r}\ \textbf{只依赖}\ x✓✓；\ \text{奇频含}\ \sigma\sqrt{x}✓（\textbf{非多项式}✓✓）；\ \sigma \leftrightarrow -\sigma\ \text{成对}✓✓$$
$$\textbf{⑥ 纪律}✓✓：\textbf{不}随机搜索✗；\textbf{不}数值优化✗；\textbf{不}把\ \sigma_*\ \text{的三点稳定性升级为定理}✗✓；\textbf{不}提前用\ F_{11} - F_{25}✗✓$$

## §1 结构性观察（✓✓，可用于第一刀 ✓）

$$\textbf{偶层只依赖}\ x✓✓：F_{2r}(x) = \sum_j T_r(2x_j - 1)✓ \Longrightarrow E_{\mathrm{even}}\ \text{是}\ x\text{-空间} \text{中的}\ \textbf{紧集}✓✓（C-376 ✓）$$
$$\textbf{奇层结构}✓✓：F_{2r+1} = \sum_j c_jR_r(c_j^2)✓，\ c_j = \sigma_j\sqrt{x_j}✓ \Longrightarrow \text{对固定}\ x✓，\ \text{奇频是}\ \sigma\ \text{的}\ \textbf{线性函数}✓✓$$
$$\Longrightarrow \ \textbf{16 层可用线性代数处理}✓✓（\text{而非逐个数值}✗） \ —— \ \text{这是}\ C\text{-}380\text{-}7\ \text{最可利用的结构}✓✓$$
$$\textbf{拟用工具}✓✓：\text{对固定}\ x✓，\ \text{问题}\ \min_{\sigma \in \{\pm 1\}^5}\max_{0 \le r \le 4}|{\sum}_j \sigma_j v_{r,j}|✓ \ \text{是}\ \textbf{有限组合} \text{上的一致性极小极大}✓✓$$
$$\qquad （\text{与}\ C\text{-}373\ \text{的「32 层」同型}✓，\ \text{此处规模更小}✓✓）$$

## §2 分叉（✓✓）

$$\textbf{6A 成功}✓✓：\text{可行域空} \Longrightarrow \textbf{Bridge A 关闭}✓✓ \ —— \ \text{这是}\ \text{目前}\ M = 5\ \text{路线的}\ \textbf{最短闭合路径}✓✓$$
$$\textbf{6B}✓：\text{若存在}\ (x, \sigma)\ \text{使}\ \max_{r \le 4}|F_{2r+1}| \le \tfrac12✓ \Longrightarrow \textbf{不}判死✗✓，\ \text{才进入}\ F_{11} - F_{25}\ \text{的}\ \textbf{五维额外观测}✓✓$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}6` ✓ | **CLOSED** ✓✓ |
| `\sigma_*` 三点稳定性 ✓ | **线索（非定理）** ⚠️✓ |
| **`C\text{-}380\text{-}7`（5 低奇频全域排除）** ✓ | **OPEN ← 下一刀** ✓✓ |
| `F_{11} - F_{25}` ✓ | **暂不使用** ✗✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \text{可行域已证空}✗；\ \sigma_*\ \text{为定理}✗；\ \text{预检 3/3 ＝ 全域结论}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{目标}\ \textbf{未证}✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 有限半代数可行性 命中文件数=0    :: 
技术词 候选极值层非承诺 命中文件数=0    :: 
技术词 对称性压缩  命中文件数=0    :: 
```
- **零计算** ✗（注册档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
