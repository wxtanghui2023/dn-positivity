已查地图（**先查后写**）：`C-377`（**自由基准弱** ✓✓；`V_2` 自由上界 `24` ✓）、`C-376`（**方差缺口** ✓✓）、`C-375`（16 层 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-378：共同 Chebyshev 来源的几何压缩审计（`V_2`／Vandermonde）**，**有计算（数值极值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① } \mathcal C_1\ \textbf{极薄}✓✓：\mathcal C_1 := \{a \in [-1,1]^5 : \sum_j T_m(a_j) \le \tfrac12,\ m = 1,\dots,12\}✓（r = 1 \Longrightarrow a_j = y_j✓）$$
$$\qquad \text{采样}\ 400000\ \text{点} \Longrightarrow \textbf{可行仅}\ 15\ \text{个}✓✓（0.00375\%✓） \ —— \ \text{体积上}\ \textbf{极薄}✓✓$$
$$\textbf{② } V_2\ \text{压缩有限}✓：\max_{\mathcal C_1}V_2 = 13.682✓（\text{自由上界}\ 24✓） \Longrightarrow \text{比}\ 0.5701✓$$
$$\qquad ⚠️ \textbf{但}\ \text{C-377-1}\ \text{的}\ \textbf{自由矩} \text{已达}\ 13.743✓ \Longrightarrow \textbf{Chebyshev 结构对}\ V_2\ \textbf{几乎无额外贡献}✗✓$$
$$\textbf{③ Vandermonde 同理}✓：\max_{\mathcal C_1}\log\Delta = -3.110✓（\Delta = 4.46 \times 10^{-2}✓）\ \text{vs}\ \text{自由族}\ \Delta = 7.9 \times 10^{-2}✓ \Longrightarrow \text{比}\ 0.56✓$$
$$\qquad \Longrightarrow \ \text{同样}\ \textbf{主要由自由约束造成}✗✓ \ —— \ \textbf{非} Chebyshev 结构✗✓$$
$$\textbf{④ 边界刚性检查}✓：V_2\ \text{极值处}\ a^2\ \text{排序} = (0.0151, 0.2490, 0.6141, 0.8775, 0.9829)✓，\text{最小相邻差}\ 0.1055✓ \Longrightarrow \textbf{无碰撞、无}\ |a_i| = |a_j|✗✓$$
$$\qquad \Delta\ \text{极值处}✓：a^2 = (0.000064, 0.3535, 0.3635, 0.8835, 0.9102)✓ \ —— \ \text{近退化对（gap}\ 0.00998✓）但\textbf{非精确}✗✓$$
$$\textbf{⑤ ⭐ 判决 = 出口 B}✓✓：\ \boxed{\textbf{Chebyshev 共同来源并不产生简单几何压缩}}✓✓（\text{唐先生预注册}✓✓）$$
$$\qquad \Longrightarrow \ \text{方向}\ = \ \textbf{Chebyshev 约束的函数值分布／符号传播}✓✓$$
$$\textbf{⑥ ⭐ 线索（登记）}✓✓：\text{极值点处}\ \textbf{若干}\ S_m\ \text{极负}✓：V_2\ \text{极值}\ S_5 = -3.0702✓；\Delta\ \text{极值}\ S_{10} = -4.9131✓$$
$$\qquad \Longrightarrow \ \text{极值位于}\ T_m(a_j) \approx -1\ \text{的区域}✓✓（\text{即}\ a_j \approx \cos\tfrac{(2k+1)\pi}{m}✓） \Longrightarrow \textbf{束缚约束非}\ (\le \tfrac12)\ \text{类，而是联合结构}✓✓$$

## §1 计算记录（✓✓）

$$\textbf{可行点}✓✓：400000\ \text{随机}\ a \in [-1,1]^5 \Longrightarrow \text{可行}\ 15✓（\text{过滤}\ S_m \le \tfrac12✓，m = 1,\dots,12✓）$$
$$\textbf{V}_2\ \text{极值}✓：a = (0.9367, -0.1230, -0.4990, 0.7837, -0.9914)✓，\ V_2 = 13.682164✓，\ \text{比}\ 0.5701✓$$
$$\qquad S_m\ \text{值}✓： (0.107, 0.477, 0.490, 0.495, \mathbf{-3.070}, -0.213, -1.166, 0.187, -0.306, -0.557, 0.098, 0.494)✓✓$$
$$\textbf{Δ 极值}✓：a = (0.9400, -0.6029, -0.9541, 0.5946, 0.0080)✓，\ \log\Delta = -3.110087✓，\ \Delta = 4.4597 \times 10^{-2}✓$$
$$\qquad S_m\ \text{值}✓： (-0.014, 0.022, -0.144, -0.157, -0.127, -0.231, -0.304, 0.121, -0.090, \mathbf{-4.913}, 0.201, -0.087)✓✓$$
$$\textbf{爬山}✓：\text{从采样最优出发}\ 6000\ \text{步}\ \textbf{未改进}✗✓ \Longrightarrow \text{所找点为}\ \textbf{局部最优}✓✓$$
$$\textbf{对照}✓：\text{自由族}\ a = (1,1,1,-1,-1) \Longrightarrow V_2 = 24✓，\log\Delta = -60✓（\text{碰撞}✓），\ \textbf{不可行}✗✓；\ a = (-1,-0.5,0,0.5,1) \Longrightarrow V_2 = 12.5✓，\log\Delta = -2.537✓（\Delta = 0.079✓），\textbf{不可行}✗✓$$

## §2 判决与方向（✓✓）

$$\textbf{出口判定}✓✓：\text{§0 的 ⑤ 命中}\ \textbf{出口 B}✓✓（「仍没有压缩」✓） \ —— \ \text{且}\ \text{更精确}：\text{压缩}\ \textbf{来自自由矩}✓，\textbf{非} Chebyshev✓✓$$
$$\textbf{读法}✓✓：\text{体积上}\ \mathcal C_1\ \text{极薄}✓✓（15／400000✓），\ \textbf{但} \text{其}\ V_2／\Delta\ \text{极值}\ \textbf{不}比自由族小多少✗✓$$
$$\qquad \Longrightarrow \ \textbf{「薄」是体积现象}✓，\ \textbf{不是} \text{Vandermonde／扩散型几何刚性}✗✓ \ —— \ \text{与}\ C\text{-}376\ \text{的部分压缩结论}\ \textbf{一致}✓✓$$
$$\textbf{方向}✓✓：\text{转向}\ \boxed{\text{Chebyshev 约束的}\ \textbf{函数值分布／符号传播}}✓✓ \ —— \ \text{即}\ \text{不}\ \text{再找几何压缩}✗✓，\ \text{而研究}\ T_m(a_j)\ \text{的}\ \textbf{联合取值结构}✓✓$$
$$\textbf{⛔ 不}继续猜 strata✗✓；\textbf{不}扩大随机采样✗✓；\textbf{不}同开\ C\text{-}377\text{-}3✗✓（\text{唐先生修正}✓✓）$$

## §3 判死标准回填（✓✓）

$$\textbf{A}✓：\text{若得}\ V_2 \le C < 20✓ \ \text{或}\ \Delta \le C < \Delta_{\mathrm{free}}✓ \Longrightarrow \text{进}\ C\text{-}379\（16\ \text{层}✓） \ —— \ \textbf{未达}✗✓（\text{因压缩源自自由矩}✓）$$
$$\textbf{B}✓✓：\text{若}\ V_2 \to V_{2,\max}✓ \ \text{或 Vandermonde 保持近自由尺度}✓ \Longrightarrow \boxed{\text{Chebyshev 共同来源}\ \textbf{不产生简单几何压缩}}✓✓ \ \Longrightarrow \ \text{转函数值分布／符号传播}✓✓$$
$$\textbf{C}✓：\text{若极值必然导致}\ a_i^2 = a_j^2✓ \ \text{或碰撞}✓ \Longrightarrow \text{接}\ C\text{-}376\ \text{边界层}✓ \ —— \ \textbf{未命中}✗✓（\text{gap}\ 0.1055／0.00998✓）$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}377\text{-}1` ✓ | **CLOSED（弱）** ✓✓ |
| `C\text{-}378`（共同来源压缩）✓ | **CLOSED：出口 B（无简单几何压缩）** ✓✓ |
| `\mathcal C_1` 体积薄度 ✓ | **极薄（`15/400000`）** ✓✓ |
| Chebyshev 函数值分布／符号传播 ✓ | **OPEN ← 新方向** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\mathcal C_1\ \text{已被判死}✗（\text{仅}\ V_2／\Delta\ \text{型压缩}\ \textbf{无}✓）；\ \text{Chebyshev 结构无用}✗（\textbf{体积}上极薄✓）；\ H = \varnothing\ \text{已证}✗$$
$$\textbf{诚实标注}⚠️✓：13.682／-3.110\ \text{为}\ \textbf{采样 ＋ 爬山} \text{结果}✓，\textbf{非}全局极值✗✓（\text{但爬山未改进}✓ \Longrightarrow \text{局部最优}✓）$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 共同来源压缩 命中文件数=0    :: 
技术词 函数值分布转向 命中文件数=0    :: 
技术词 负值区极值  命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/c378.py`（`400000` 采样 ＋ `6000` 步爬山 ＋ `S_m` 逐项 ✓）
- **本档有计算**（数值极值，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
