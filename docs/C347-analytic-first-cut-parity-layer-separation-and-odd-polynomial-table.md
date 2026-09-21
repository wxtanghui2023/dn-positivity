已查地图（**先查后写**）：`C-346`（**P4-F 封口** ✓；解析下界为下一阶段 ✓）、`C-343`（straddling 判据 ✓✓）、`C-341`／`C-342`（偶频归约／矩 ✓）、`C-336`（`s_1 <= 11/4` ✓）。回查见 §6 ✓

D0: 本档对象 = **C-347：解析首刀（奇偶层分离 ＋ 低阶奇多项式表）**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 奇偶层分离（形式化）}✓✓：\text{偶层}\ F_{2r} = \sum_j P_r(x_j)✓，P_r \in \mathbb{R}[x]✓；\text{奇层}\ F_{2r+1} = \sum_j \sigma_j \sqrt{x_j}\, R_r(x_j)✓，R_r \in \mathbb{R}[x]✓$$
$$\qquad \Longrightarrow \ \boxed{\text{偶层控制}\ \mathbb{R}[x]✓ \quad\text{而} \text{奇层落在}\ \sqrt{x}\,\mathbb{R}[x]✓} \ \Longrightarrow \textbf{奇偶矩错配}✓✓$$
$$\textbf{② 低阶奇多项式表（逐字核对）}✓✓：R_0 = 1✓；R_1 = 4x - 3✓；R_2 = 16x^2 - 20x + 5✓；R_3 = 64x^3 - 112x^2 + 56x - 7✓（\text{与唐先生清单一致}✓✓）$$
$$\textbf{③ ⭐ 反称配对障碍（结构性）}✓✓：\text{若}\ \text{配置满足}\ c \leftrightarrow -c\ \text{配对}✓ \Longrightarrow \textbf{全部奇频恒为 0}✓✓ \Longrightarrow \text{任何奇频下界}\ \textbf{必须} \text{用到}\ \ge 2\ \text{阶偶约束}✓（F_4,\ F_6,\dots）$$
$$\textbf{④ 最低阶单独不足}✗✓：\text{仅}\ F_2 \le \tfrac12\ \text{给}\ \sum_j x_j \le \tfrac{11}{4}✓；\text{Cauchy--Schwarz}\ (\sum_j c_j)^2 \le 5\sum_j x_j \le \tfrac{55}{4}✓ \Longrightarrow |F_1| \le \tfrac{\sqrt{55}}{2} \approx 3.71✗ \ —— \ \textbf{无下界}✗✓$$
$$\textbf{⑤ 本档判定}⚠️：\textbf{未}\ \text{找到可用低阶不等式链}✗；\textbf{但}\ \text{已（a）形式化奇偶错配}✓，\text{（b）核对低阶表}✓，\text{（c）定位必要条件（须用}\ \ge 2\ \text{阶偶约束）}✓✓$$

## §1 奇偶层分离（✓✓）

$$\textbf{偶层}✓：F_{2r} = \sum_{j=1}^{5} P_r(x_j)✓，x_j := c_j^2 \in [0,1]✓；P_r\ \text{次}\ r✓ \Longrightarrow \text{只依赖}\ s_m = \sum_j x_j^m\ (m \le r)✓$$
$$\textbf{奇层}✓：\text{由}\ T_{2r+1}(c) = c\,R_r(c^2)✓ \Longrightarrow F_{2r+1} = \sum_{j=1}^{5} \sigma_j \sqrt{x_j}\, R_r(x_j)✓$$
$$\textbf{结构含义}✓✓：\text{偶层}\ \textbf{无符号}✓（\sigma_j^2 = 1✓）；\text{奇层}\ \textbf{符号线性}✓ \Longrightarrow \text{奇层}\ \text{在}\ \sigma\ \text{上是}\ \textbf{线性泛函}✓✓$$

## §2 低阶奇多项式（✓✓）

| `r` | `F_{2r+1}` ✓ | `R_r(x)` ✓ |
|---|---|---|
| 0 ✓ | `F_1` ✓ | `1` ✓ |
| 1 ✓ | `F_3` ✓ | `4x - 3` ✓ |
| 2 ✓ | `F_5` ✓ | `16x^2 - 20x + 5` ✓ |
| 3 ✓ | `F_7` ✓ | `64x^3 - 112x^2 + 56x - 7` ✓ |

$$\textbf{说明}✓：R_r\ \text{的根} \text{在}\ (0,1)\ \text{内交替}✓；R_r(1) = 1✓（\text{因}\ T_{2r+1}(1) = 1✓）；R_r\ \text{的系数}\ \textbf{交替}✓$$

## §3 ⭐ 反称配对障碍（✓✓，本档最有价值 ✓）

$$\text{取}\ \text{成对配置}\ c = (a, -a, b, -b, 0)✓ \Longrightarrow \textbf{全部奇频}\ F_{2r+1} = 0✓✓（\text{逐项抵消}✓）$$
$$\textbf{推论}✓✓：\text{任何形式为}\ \sum_j \sigma_j\sqrt{x_j}\,(\text{偶函数}) \ \text{的量}\ \textbf{在对称配置上恒为 0}✓ \Longrightarrow \textbf{奇频下界} \text{必须}\ \textbf{借助}\ \ge 2\ \text{阶偶约束}✓✓$$
$$\textbf{另一必要观察}✓✓：\sigma\ \text{的整体翻转}\ \sigma \to -\sigma\ \text{使}\ \text{全部奇频变号}✓（\text{C-343}✓）\Longrightarrow \text{下界须对}\ |F_{2r+1}|\ \text{或}\ \max_r\ \text{形式陈述}✓✓$$

## §4 最低阶估计（✗✓）

$$\textbf{仅用}\ F_2✓：\sum_j x_j \le \tfrac{11}{4}✓；\ \sum_j |\sigma_j\sqrt{x_j}| = \sum_j \sqrt{x_j} \le \sqrt{5 \cdot \tfrac{11}{4}} = \tfrac{\sqrt{55}}{2} \approx 3.708✗$$
$$\Longrightarrow |F_1| = |\sum_j c_j| \le 3.708✗ \ —— \ \textbf{只有上界，无下界}✗✓ \Longrightarrow \text{须引入}\ F_4／F_6\ \text{等高阶偶约束}✓✓$$
$$\textbf{且}✓：\text{单点结构：}c = (1, -1, a, -a, 0)✓ \ \text{使}\ F_1 = F_3 = F_5 = 0✓（\text{反称}✓）\ \text{并可调}\ \sum x_j = 2 + 2a^2✓ \Longrightarrow \text{该族}\ \textbf{精确杀掉}\ \text{全部奇频}✓✓$$

## §5 下一步（✓✓，登记不执行 ✓）

$$\textbf{目标形态}✓✓：\ \exists\ \lambda_r \ge 0✓（\text{或}\ |\cdot|\ \text{组合}✓）\ \text{使}\ Q_\sigma(x) := \sum_{r \in R} \lambda_r F_{2r+1}(x,\sigma)✓ \ \text{可被}\ E\ \text{的矩约束}\ \textbf{直接控制}✓✓$$
$$\textbf{优先序}✓✓：\text{先审最低阶组合}\ \{F_1,\ F_3,\ F_5,\ F_7\}✓ \times \{F_4,\ F_6,\ F_8\}✓（\text{因 §3 的必要条件}✓）；\text{不成功再上更高}\ r✗✓$$
$$\textbf{纪律}✓✓：\textbf{不}\ \text{做}\ SOS✗；\textbf{不}\ \text{做数值搜索}✗（\text{唐先生口径}✓）；\textbf{不}\ \text{扩频率}✗；\textbf{不}\ \text{追}\ G_*✗$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 奇偶层分离  命中文件数=0    :: 
技术词 反称配对     命中文件数=4    :: ./V221-pointwise-escape-parametrization-audit.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md 
技术词 低阶不等式链 命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：低阶链已找到 ✗；`H = \varnothing` 已证 ✗；奇频下界已得 ✗；反称配对已排除 ✗（仅指出**必要条件** ✓）
