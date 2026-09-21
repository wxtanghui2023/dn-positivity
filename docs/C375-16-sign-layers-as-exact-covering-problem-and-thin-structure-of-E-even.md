已查地图（**先查后写**）：`C-374`（**32 层探针** ✓✓；`E_{\mathrm{even}}` **很薄** ✓✓）、`C-373`（**纤维不确定** ✓✓；`\delta_*` ✓）、`C-371`（`\mathcal Z \cap E = \varnothing` ✓✓）、`C-342`／`C-345`（**偶频极小／硬约束** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-375：`E_{\mathrm{even}}` 上的 16 符号层精确覆盖问题 ＋ 薄结构骨架审计**，**零计算（登记不执行 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① ⭐ 精确形式（本档核心）}✓✓：\ E_{\mathrm{even}} = \Big\{x \in [0,1]^5 : \sum_j T_r(2x_j - 1) \le \tfrac12,\ r = 1,\dots,12\Big\}✓；\ \mathcal S := \{\pm 1\}^5 / \{\pm I\}✓，\ |\mathcal S| = 16✓✓$$
$$\qquad G_\sigma(x) := \max_{0 \le r \le 12}\Big|\sum_{j=1}^{5}\sigma_j\sqrt{x_j}\,R_r(x_j)\Big|✓ \Longrightarrow \ \boxed{\min_{\sigma \in \mathcal S}\ \inf_{x \in E_{\mathrm{even}}}G_\sigma(x) > \tfrac12}✓✓（\text{Bridge A}✓）$$
$$\qquad \textbf{性质}✓✓：\text{有限符号层} \times \textbf{一个共同连续可行域} \Longrightarrow \textbf{全局证书问题}✓✓（\textbf{非} 随机探针✗✓）$$
$$\textbf{② 关键判断}✓✓：\textbf{不再}研究\ \mathcal Z✗✓；\textbf{不再}扩大随机采样✗✓；\ \text{而是研究}\ \boxed{E_{\mathrm{even}}\ \text{的}\ \textbf{薄结构}}✓✓$$
$$\textbf{③ 两层方法}✓✓：\text{Layer A}\ \textbf{发现并注册 active set}✓✓；\ \text{Layer B}\ \textbf{逐 active stratum 精确审计}✓✓（\text{见 §1／§2}✓）$$
$$\textbf{④ 直接出口}✓✓：\text{由}\ C\text{-}371✓，\ E_{\mathrm{even}} \cap \mathcal Z_\sigma = \varnothing\ \forall \sigma✓（\mathcal Z_\sigma\ \text{见 §3}✓） \Longrightarrow \text{若每个 stratum 有}\ \textbf{显式代数距离下界}✓ \Longrightarrow \ \text{可能直达 Bridge A}✓✓$$
$$\textbf{⑤ 三出口}✓✓：\text{A}\ \text{active strata 有限且可完整覆盖} \Longrightarrow \textbf{Bridge A 闭合}✓✓；\ \text{B}\ \text{新连续自由度} \Longrightarrow \textbf{须更强}\ x\text{-几何耦合}✓✓；\ \text{C}\ \inf G_\sigma \le \tfrac12 \Longrightarrow \textbf{找到 Bridge-A 障碍点}✓✓$$

## §1 Layer A：active set 发现与注册（✓✓）

$$\textbf{目标}✓✓：\text{对}\ x \in E_{\mathrm{even}}✓ \ \text{记录达到或逼近}\ \max_r F_{2r}(x)\ \text{的}\ \textbf{active frequencies}✓✓$$
$$\textbf{对象}✓✓：\text{回答}\ \boxed{E_{\mathrm{even}}\ \text{是否实际上被}\ \textbf{少数 active strata} \text{控制}}✓✓ \ —— \ \textbf{不是} \text{求定理}✗✓$$
$$\textbf{纪律}✓✓：\textbf{不}把某一次优化得到的\ \{r_1, r_2, r_3\}\ \textbf{直接当定理}✗✓（\text{C-339 的}\ \{5,12,14\}\ \text{前车之鉴}✓）$$

## §2 Layer B：逐 stratum 精确审计（✓✓）

$$\textbf{触发}✓✓：\text{若出现}\ F_{2r_1}, F_{2r_2}, F_{2r_3}\ \text{共同逼近}\ \tfrac12✓ \Longrightarrow \text{把该 stratum}\ \textbf{单独参数化}✓✓$$
$$\textbf{审计}✓✓：\text{对该参数化，对}\ 16\ \text{个}\ \sigma\ \text{检查}\ G_\sigma(x) > \tfrac12✓✓$$
$$\textbf{收益}✓✓：\text{把「薄的五维集合」压缩为}\ \textbf{低维代数分层}✓✓ \Longrightarrow \ \textbf{节省} \text{覆盖预算}✓✓（\text{不在}\ [0,1]^5\ \text{上浪费}✗✓）$$

## §3 直接代数出口（✓✓）

$$\mathcal Z_\sigma := \Big\{x : \sum_j \sigma_j\sqrt{x_j}\,x_j^m = 0,\ m = 0,1,2,3\Big\}✓✓（\text{即}\ C\text{-}349\ \text{的四阶 signed-moment nullspace}✓）$$
$$\textbf{C-371 的推论}✓✓：\ E_{\mathrm{even}} \cap \mathcal Z_\sigma = \varnothing\ \ \forall \sigma \in \mathcal S✓✓$$
$$\textbf{若能}✓✓：\text{在每个 active stratum 上得}\ \textbf{显式代数距离下界}✓：\ \max_{m=0}^{3}\Big|\sum_j \sigma_j\sqrt{x_j}\,x_j^m\Big| \ge \delta_{\mathrm{stratum}}✓✓$$
$$\qquad \text{再证}\ \textbf{四阶 signed moments 到高阶}\ O_r\ \text{的传播}✓✓ \Longrightarrow \ \textbf{可能直接形成 Bridge A}✓✓ \ —— \ \textbf{比} 重新寻找全局抽象\ \Phi\ \text{更具体}✓✓$$

## §4 三出口（✓✓）

$$\textbf{A}✓✓：\text{active strata}\ \textbf{有限且可完整覆盖}✓ \Longrightarrow \ \min_{\sigma, x \in E_{\mathrm{even}}}G_\sigma(x) > \tfrac12✓✓ \Longrightarrow \textbf{Bridge A 闭合}✓✓$$
$$\textbf{B}✓✓：\ E_{\mathrm{even}}\ \text{存在}\ \textbf{新的连续自由度}✓ \Longrightarrow \text{active-stratum 方法}\ \textbf{不闭合}✗✓ \Longrightarrow \text{转向}\ \textbf{更强的}\ x\text{-几何耦合}✓✓$$
$$\textbf{C}✓✓：\ \inf G_\sigma \le \tfrac12✓ \Longrightarrow \textbf{找到真正的 Bridge-A 障碍点}✓✓ \Longrightarrow \textbf{停止} \text{把}\ 2.19 \sim 2.56\ \text{的巨大余量}\ \textbf{外推成定理}✗✓$$

## §5 账本（✓✓）

| 对象 ✓ | 状态 ✓ |
|---|---|
| `\mathcal Z \cap E` ✓ | **✓ 完成** ✓✓ |
| `\delta_* > 0` ✓ | **✓ 存在性** ✓✓ |
| 16 符号层的 discovery ✓ | **✓ 完成（`2.19 \sim 2.56`，5 点）** ⚠️ |
| **`E_{\mathrm{even}}` 的完整几何覆盖** ✓ | **OPEN ← 下一档** ✓✓ |
| Bridge A ✓ | **OPEN（唯一下一主线）** ✓✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

$$\textbf{禁项}✓✓：\textbf{不}再用「随机探针扩大一点」当主路线✗✓；\textbf{不}研究\ \mathcal Z\ \text{本身}✗✓；\textbf{不}跳步✗；\textbf{不}写\ H = \varnothing✗$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 符号层覆盖问题 命中文件数=0    :: 
技术词 活跃分层注册 命中文件数=0    :: 
技术词 薄结构骨架  命中文件数=0    :: 
```
- **零计算** ✗（登记不执行 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：`E_{\mathrm{even}}` 的 active-stratum 结构**尚未探测** ✓；`2.19 \sim 2.56` 仍为**5 点观测** ✓，**非定理** ✗✓
- **不得**写成：Bridge A 已闭合 ✗；`E_{\mathrm{even}}` 薄结构已被完整覆盖 ✗；`H = \varnothing` 已证 ✗
