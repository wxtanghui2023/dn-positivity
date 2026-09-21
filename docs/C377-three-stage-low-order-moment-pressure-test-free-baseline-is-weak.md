已查地图（**先查后写**）：`C-376`（**方差缺口 ＋ 端点强制** ✓✓）、`C-375`（16 层覆盖 ✓✓）、`C-336`（幂和单调性 ✓✓）、`C-341`（矩链 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-377：三段式低阶矩压力测试（`C\text{-}377\text{-}1／2／3`）**，**有计算（数值基准，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① ⭐ C-377-1 结论（本档核心，决定性）}✓✓：\text{自由五点约束}\ a_j \in [-1,1]✓，\sum a_j \le \tfrac12✓，\sum a_j^2 \le \tfrac{11}{4}✓$$
$$\qquad \text{最大}\ \textbf{spread}\ \sum_{i<j}(a_i - a_j)^2 = \boxed{13.743}✓✓（\text{闭式上界}\ 5 \cdot \tfrac{11}{4} = 13.75✓ \Longrightarrow \textbf{几乎饱和}✓✓）$$
$$\qquad \text{最大直径}\ \max_j a_j - \min_j a_j = \boxed{1.9994}✓✓（\text{对照}\ 2 = \textbf{完全未压}✓） \Longrightarrow \ \boxed{\textbf{自由约束对几何压缩几乎无用}}✗✓$$
$$\textbf{② 关键推论}✓✓：\ \boxed{\text{任何真正的压缩}\ \textbf{必须} \text{来自 Chebyshev 结构}}✓✓ \ —— \ a_j = T_r(y_j)\ \textbf{来自同一组}\ y_j✓✓$$
$$\qquad \Longrightarrow \ \text{「}\textbf{共同来源}\text{」}\ \text{是}\ \textbf{承重的}✓✓；\ \text{单看}\ (S_r, S_{2r})\ \textbf{不足}✓✓（\text{与唐先生预判一致}✓）$$
$$\textbf{③ C-377-2 登记}✓✓：a_j = T_r(y_j)✓，\ T_{mr}(y_j) = T_m(a_j)✓ \Longrightarrow \text{若}\ r, 2r, 3r, \dots \le 12✓ \Longrightarrow \textbf{局部 Chebyshev 链}\ \sum_j T_m(a_j) \le \tfrac12✓✓$$
$$\qquad r = 1\ \text{时}\ a_j = y_j✓ \Longrightarrow \text{回到}\ \textbf{五点 Chebyshev 矩问题}✓✓（m = 1,\dots,6✓）$$
$$\textbf{④ C-377-3 登记}✓✓：\ \sum_j(y_j^2 - \lambda y_j)^2 \ge 0✓ \ \text{对}\ \lambda\ \text{最优} \Longrightarrow \boxed{p_3^2 \le p_2p_4}✓✓；\ \text{与}\ p_4 \le p_2 - \tfrac{9}{16}✓ \Longrightarrow \boxed{|p_3| \le \sqrt{p_2\big(p_2 - \tfrac{9}{16}\big)}}✓✓$$
$$\textbf{⑤ 判死标准}✓✓：\text{只答一问题}\ \boxed{\text{低阶}\ S_1,\dots,S_4 + \text{矩 PSD}\ \text{能否产生}\ \textbf{真正的全局几何压缩}}✓✓；\ \text{三出口见 §4}✓$$

## §1 C-377-1 计算记录（✓✓）

$$\textbf{随机搜索}✓：400000\ \text{点}✓ \Longrightarrow \text{最大 spread}\ 13.743328✓（\text{于}\ a = (0.4654, -0.9464, 0.4490, 0.8223, -0.8717)✓，\sum a = -0.081✓，\sum a^2 = 2.7500✓）$$
$$\textbf{结构型扫描}✓：a = (t,t,t,-u,-u)✓（801 \times 801✓） \Longrightarrow \text{最大 spread}\ 13.748634✓（\text{于}\ t = 0.59875✓，u = 0.915✓）✓✓$$
$$\textbf{直径搜索}✓：300000\ \text{点}✓ \Longrightarrow \text{最大直径}\ 1.999384✓（\text{于}\ (-0.4395, -0.6161, 0.9998, -0.1314, -0.9996)✓）$$
$$\textbf{读法}✓✓：\text{约束是}\ \textbf{单侧}（\le✓） \Longrightarrow \text{允许}\ \text{近乎完全展开}✓✓；\ \text{对照}\ a = (1,1,-1,-1,0)✓\ \text{不可行}（\sum a^2 = 4 > 2.75✗✓）\ \text{但不影响直径}✓$$
$$\textbf{结论}✓✓：\ \boxed{C\text{-}377\text{-}1 = \textbf{弱}}✓✓ \Longrightarrow \text{低阶矩}\ \textbf{单独不足以} \text{压缩}✓✓$$

## §2 C-377-2 结构（✓✓，登记 ✓）

$$\textbf{核心}✓✓：\text{不是把}\ a_j\ \text{当五个自由变量}✗✓，\ \text{而是利用}\ a_j = T_r(y_j)\ \text{的}\ \textbf{共同来源}✓✓$$
$$\textbf{链}✓✓：T_{2r}(y_j) = 2a_j^2 - 1✓（C-376 已用✓）；T_{mr}(y_j) = T_m(a_j)✓ \Longrightarrow \text{在}\ mr \le 12\ \text{范围内}\ \sum_j T_m(a_j) \le \tfrac12✓✓$$
$$\textbf{目标}✓✓：\text{从这组约束推出节点结构}✓，\ \text{如}\ \sum_{i<j}(a_i - a_j)^2 \le C✓ \ \text{或}\ \text{更高阶}\ \textbf{Vandermonde 型量} \text{的界}✓✓ \Longrightarrow \textbf{真正的几何压缩}✓✓$$

## §3 C-377-3 可行域（✓✓）

$$\mathcal P := \Big\{(p_1, p_2, p_3, p_4) : p_1 \le \tfrac12✓;\ p_2 \in \big[\tfrac{10-\sqrt{55}}{4}, \tfrac{11}{4}\big]✓;\ p_4 \le p_2 - \tfrac{9}{16}✓;\ p_3^2 \le p_2p_4✓;\ 4p_3 - 3p_1 \le \tfrac12✓\Big\}✓✓$$
$$\textbf{关键待答}✓✓：\mathcal P\ \text{若仍很大}✗ \Longrightarrow \text{低阶 moment route 已接近}\ \textbf{信息极限}✓✓ \Longrightarrow \text{须转向}\ p_5, p_6, \dots✓ \ \text{或高阶 Chebyshev}✓$$
$$\qquad \text{若突然压出很窄区域}✓ \Longrightarrow \text{继续向}\ p_5, p_6, \dots\ \text{推}✓✓$$
$$\textbf{⚠️ 警告}✓✓：p_3^2 \le p_2p_4\ \textbf{只是必要条件}✗✓，\ \textbf{不得}误读为新强约束✗✓$$

## §4 三出口（✓✓）

$$\textbf{出口 1}✓✓：\text{能产生真正的全局几何压缩} \Longrightarrow C\text{-}378\ \text{才进入高阶}\ S_5, \dots, S_{12}\ \text{的递推}✓✓$$
$$\textbf{出口 2}✓✓：\text{不能}✗ \Longrightarrow \textbf{明确关闭「低阶矩继续压缩」路线}✓✓，\ \text{转向}\ \textbf{高阶 Chebyshev 约束}✓✓$$
$$\textbf{出口 3}✓✓：\text{出现边界刚性}✓ \Longrightarrow \textbf{优先审计边界层与 16 sign layers 的精确连接}✓✓（\text{接 C-376 端点强制}✓）$$

## §5 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}377\text{-}1`（自由基准）✓ | **完成：弱（`13.743`／直径 `1.9994`）** ✓✓ |
| `C\text{-}377\text{-}2`（共同来源）✓ | **OPEN ← 关键** ✓✓ |
| `C\text{-}377\text{-}3`（矩 PSD 联立）✓ | **OPEN** ✓✓ |
| `E_{\mathrm{even}}` 完整几何结构 ✓ | **OPEN** ✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 自由五点基准 命中文件数=0    :: 
技术词 共同来源承重 命中文件数=0    :: 
技术词 矩判死标准  命中文件数=0    :: 
技术词 局部切比雪夫链 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（`400000` 随机 ＋ `801^2` 结构型 ＋ `300000` 直径 ✓，`/tmp` 未留 ✓）
- **本档有计算**（数值基准，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：`13.743`／`1.9994` 为**搜索所得** ✓（`13.75`／`2` 为闭式上界 ✓）；**未**做 `\mathcal P` 的精确可行域刻画 ✗✓
- **不得**写成：低阶矩路线已判死 ✗（**只**是自由基准不足 ✓）；Bridge A 已闭合 ✗；`E_{\mathrm{even}}` 已压缩 ✗；`H = \varnothing` 已证 ✗
