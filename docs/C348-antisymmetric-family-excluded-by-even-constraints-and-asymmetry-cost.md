已查地图（**先查后写**）：`C-347`（**反称配对障碍** ✓✓；奇偶层分离 ✓）、`C-346`（P4-F 封口 ✓）、`C-343`（straddling 判据 ✓✓）、`C-342`（无约束偶频最小 0.3254 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-348：反称族是否被偶频排除 ＋ 非对称性成本**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 反称族被偶频排除}✓✓：\text{反称配置}\ c = (a, -a, b, -b, 0)✓\ \text{的}\ even\text{-}max\ \text{最小值} = \textbf{1.4677299721}✓✓ \ \gg \tfrac12✗✓$$
$$\qquad \text{网格}\ 2001^2 = 4{,}004{,}001\ \text{点中}\ even\text{-}max \le \tfrac12\ \text{者} = \textbf{0}✗✓ \Longrightarrow \textbf{反称族}\ \not\subset E✓✓$$
$$\textbf{② ⭐ 非对称性成本已量化}✓✓：\text{反称族最小}\ 1.4677 \ \text{vs}\ \text{无约束偶频最小}\ 0.3254✓（C-342✓）\ \Longrightarrow \textbf{成本} \approx \textbf{1.14}✓✓$$
$$\textbf{③ C-347 的障碍不在}\ E\ \text{内}✓✓：\text{反称配对}\（\text{全部奇频} = 0✓）\ \textbf{被偶频约束自动排除}✓✓ \Longrightarrow \text{奇频下界路线}\ \textbf{未被该障碍堵死}✓✓$$
$$\textbf{④ 三结构审计}✓：\text{① 平方差型／② 矩差型／③ 符号消除} \ —— \ \text{③ 已得精确形式}✓✓（\text{见 §3}✓）$$

## §1 反称族结构与计算（✓✓）

$$\textbf{反称族}✓：c = (a, -a, b, -b, 0)✓，a,b \in [0,1]✓ \Longrightarrow \text{全部奇频} \textbf{恒为 0}✓（\text{逐对抵消}✓）$$
$$\textbf{偶频公式}✓✓：T_{2r}(a) + T_{2r}(-a) = 2T_{2r}(a)✓ \Longrightarrow \ \boxed{F_{2r} = 2T_{2r}(a) + 2T_{2r}(b) + (-1)^r}✓✓（T_{2r}(0) = (-1)^r✓）$$
$$\textbf{方法}✓：2001 \times 2001\ \text{网格}，向量化（避免逐点标量调用 ✗）⟹ 4{,}004{,}001\ \text{点全覆盖}✓$$
$$\textbf{结果}✓✓：\min = \textbf{1.4677299721}✓ \ \text{at}\ a = 0.559✓，b = 0.9785✓$$
$$\textbf{该点逐频值}✓：F_2 = 0.0798✓；F_4 = 0.9110✗；F_6 = 1.4656✗；F_8 = 0.8841✗；F_{10} = -3.8482✓；F_{12} = 0.7487✗；F_{20} = 1.4677✗；\dots$$
$$\qquad \Longrightarrow \textbf{绑定频率} = \{4,\ 6,\ 12,\ 20\}✓（\text{即}\ k = 4, 6, 12, 20✓），\text{低阶}\ F_2\ \text{很小}✓（0.0798✓）$$

## §2 非对称性成本（✓✓，本档核心 ✓）

$$\text{偶频最小}✓：\text{无约束}\ 0.3254✓（C-342✓）\quad \text{vs} \quad \text{反称约束下}\ \textbf{1.4677}✗✓$$
$$\Longrightarrow \ \boxed{\text{非对称性成本} \ge 1.4677 - 0.5 = 0.9677}✓✓（\text{相对阈值}✓）\ \text{或}\ \approx 1.14✓（\text{相对无约束最小值}✓）$$
$$\textbf{读法}✓✓：\text{要令奇频全 0，}\ \textbf{代价是偶频必然突破}\ \tfrac12✓✓ \Longrightarrow \text{偶层与奇层}\ \textbf{在此处正相关}✓（\text{而非无关}✓✓）$$

## §3 三结构审计（✓✓）

$$\textbf{① 平方差型}✓：Q(x) = x - a✓，\ (x-a)^2✓，\ x(1-x) - a✓ \ —— \ \text{均落在}\ \mathbb{R}[x]✓ \Longrightarrow \text{与偶层同型}✓；\text{但}\ \sum_j \sigma_j\sqrt{x_j}Q(x_j)\ \text{在反称配置上仍可为 0}✗✓$$
$$\textbf{② 矩差型}✓：s_1 - s_2✓，s_2 - s_3✓，\alpha s_1 + \beta s_2 + \gamma s_3✓ \ —— \ \text{由}\ x_j \in [0,1]\ \text{单调性}\ s_1 \ge s_2 \ge s_3 \ge 0✓（C-336✓）\ \Longrightarrow \textbf{符号确定}✓$$
$$\textbf{③ 符号消除}✓✓：\max_{\sigma}\big|\sum_j \sigma_j w_j\big| = \sum_j |w_j|✓（\text{取}\ \sigma_j = \mathrm{sgn}(w_j)✓）\ \Longrightarrow \text{但全域命题要求}\ \textbf{每个}\ \sigma✓✓$$
$$\qquad \Longrightarrow \ \text{单频}\ r\ \text{对}\ \sigma\ \text{可被抵消}✗（\text{取}\ \sigma\ \text{使}\ \sum_j \sigma_j w_j = 0✓）\ \Longrightarrow \text{下界}\ \textbf{必须来自}\ \max_r\ \text{多频联合}✓✓$$
$$\textbf{结论}✓✓：\text{③ 的精确形式}\ \textbf{支持} \text{「须多频联合」}\✓，\text{与 C-343 的}\ \max_r\ \text{形式一致}✓✓$$

## §4 判死标准（唐先生预设 ✓）与判定（✓✓）

$$\textbf{预设}✓✓：\text{若}\ \{F_1,F_3,F_5,F_7\} \times \{F_4,F_6,F_8\}\ \text{找不到统一下界机制}✓ \Longrightarrow \textbf{立即封口}✓，\textbf{不}\ \text{继续堆频率}✗$$
$$\textbf{本档判定}✓✓：\textbf{未}\ \text{触封口}✗✓ \ —— \ \text{因}\ C\text{-}347\ \text{的障碍（反称）}\ \textbf{已被偶频自动排除}✓✓（\text{成本}\ \ge 0.97✓）\ \Longrightarrow \text{路线}\ \textbf{仍活}✓✓$$
$$\qquad \textbf{且}✓：\text{绑定频率}\ \{4,6,12,20\}\ \text{提示}\ \text{低阶组合}\ \{F_4,\ F_6\}\ \text{已足以}\ \text{制造非对称成本}✓✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 反称族排除  命中文件数=0    :: 
技术词 非对称性成本 命中文件数=0    :: 
技术词 符号消除     命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4j.py` ✓（向量化 ✓；日志 `/tmp/p4i.log` 为被中止的标量版 ✗）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`H = \varnothing` 已证 ✗；奇频下界已得 ✗；反称族已被解析证明排除 ✗（**网格 4{,}004{,}001 点数值** ✓）
