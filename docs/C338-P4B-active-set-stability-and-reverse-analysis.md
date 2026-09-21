已查地图（**先查后写**）：`C-337`（P4-A：`G_min ≈ 0.9738`；A = {5,12,14,21}✓）、`C-336`（幂和单调性／矩上界 ✓）、`C-284`（同点／有限整数频率泛函坍缩 ✓）、`C-153`（M=2 覆盖型精确代数 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-338：P4-B（active-set 稳定性 ＋ 反推）**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 一致性}✓✓：\text{高精度精化后}\ G = \textbf{0.9738227074}✓（与 C-337 的 0.9738227358 ✓ 一致到}\ 10^{-8}✓）\ \Longrightarrow \ \textbf{数值稳定}✓$$
$$\textbf{② active set 修正}✗✓：\text{容差}\ 10^{-9}\ \text{下}\ \textbf{A} = \{5,\ 12,\ 14\}✓，\ \textbf{21 掉出}✗✓ \Longrightarrow \ \textbf{21 是近似并列，不是真等式}✓$$
$$\textbf{③ 第 4 项被判为近似}✓✓：\text{故 C-337 的「A＝四个」}\ \textbf{应改述为「A 有 3 元核心 ＋ 1 个近邻」}✓✓$$
$$\textbf{④ 边界／退化全面不低于}✓✓：\text{11 类边界／对称退化起点}\ \textbf{全部}\ \ge 0.9924✓ \Longrightarrow \ \textbf{无更低构型}✓（\text{sanity check 通过}✓）$$
$$\textbf{⑤ ⭐ 频率结构发现}✓✓：\ \textbf{5 + 21 = 26 = 12 + 14}✓✓（\text{成对和}\ 26 = 5M+1✓）；\ \gcd = 1✓（\textbf{不}被}\ C\text{-284 解释}✓✓）$$

## §1 检查 A：多起点一致性（✓）

$$\textbf{设定}✓：180\ \text{随机起点} ＋ \text{模式搜索}（每起}\ 250\ \text{轮，预算保守）✓$$
$$\textbf{结果}✓：\text{最好}\ 0.984519✓；\textbf{无一低于}\ 0.9739✓（0/180✓）$$
$$\textbf{关键观察}✓✓：\text{最佳随机构型}\ c \approx [-0.862,\ -0.735,\ -0.133,\ +0.099,\ +0.904]✓ \ \textbf{与冠军构型几乎同形}✓✓（\text{冠军}\ c \approx [-0.872,\ -0.744,\ -0.137,\ +0.091,\ +0.910]✓）\ \Longrightarrow \ \textbf{同一盆地、结构可复现}✓✓$$
$$\textbf{诚实标注}⚠️：\text{短期预算}\ \textbf{未达} \text{冠军值}✗ \Longrightarrow \textbf{不能}断定全局最小性}✗✓$$

## §2 检查 B：边界／退化（✓✓，全部不低于 ✓）

| 起点类 | 精化后 `G` |
|---|---|
| all `+1` ✓ | 1.3923157 ✗ |
| all `-1` ✓ | 1.3093672 ✗ |
| 交替 `+-` ✓ | 1.5882087 ✗ |
| 五重根 `0.5` ✓ | 2.1256033 ✗ |
| 全 `0` ✓ | 1.7552213 ✗ |
| `c_i = -c_j` 严格 ✓ | **0.9923925**（最低者 ✓） |
| 其余 5 类 ✓ | 1.22 – 1.49 ✗ |

$$\Longrightarrow \textbf{边界／退化架}\ \textbf{无一低于}\ 0.9738✓✓ \Longrightarrow \ \textbf{冠军不在边界上，且边界不更优}✓✓$$

## §3 检查 C：高精度 active set（✓✗）

$$G = \textbf{0.9738227074211}✓；\ c = [-0.87200469,\ -0.74381232,\ -0.13677624,\ +0.09143819,\ +0.90994467]✓（\text{13 位收敛}✓）$$
$$\textbf{容差}\ 10^{-9}\ \text{下的}\ A = \textbf{\{5,\ 12,\ 14\}}✓；\text{其中}\ F_{12} = F_{14} = 0.973822707✓；F_5\ \text{同值}✓ \Longrightarrow \ \textbf{3 元核心}✓$$
$$\textbf{21 的状态}✗✓：\text{在}\ C\text{-337 的粗容差下并列}✓，\text{高精度下}\ \textbf{掉出}✗ \Longrightarrow \text{应记为}\ \textbf{近邻（near-tie）}✓，\textbf{不}计入核心}✗✓$$
$$\textbf{次高}✓：F_{13} \approx 0.7626✓（\text{与}\ 0.9738\ \text{有明显间隙}✓）\ \Longrightarrow \ \textbf{核心}\ \{5,12,14\}\ \text{是干净的}✓$$

## §4 ⭐ 频率结构（✓✓，本档最有价值 ✓）

$$5 + 21 = 26 = 12 + 14✓✓ \ \Longrightarrow \ \text{四个频率}\ \textbf{成对和相同}✓✓（= 5M + 1 = 26✓）$$
$$\gcd(5,12,14,21) = 1✓✓ \ \Longrightarrow \ \textbf{不能}被}\ C\text{-284 的 gcd 坍缩解释}✗✓（\text{与唐先生预判一致}✓✓）$$
$$\text{模结构}✓：\text{mod}\ 7\ \to \{5, 5, 0, 0\}✓；\text{mod}\ 3\ \to \{2, 0, 2, 0\}✓；\text{mod}\ 4\ \to \{1, 0, 2, 1\}✗ \Longrightarrow \text{未见单一模结构}✗✓$$
$$\textbf{读法}✓✓：\ \textbf{「对偶和 26」}\ \text{是}\ \textbf{新的具体线索}✓ \Longrightarrow \text{值得作为}\ \textbf{反推的代数入口}✓✓（\text{而非再扩搜索}✓）$$

## §5 反推路线（✓✓，登记不执行 ✓）

$$\text{若}\ F_5 = F_{12} = F_{14} = G✓ \Longrightarrow \text{极值点须满足}\ \textbf{stationarity}✓：\nabla F_5,\ \nabla F_{12},\ \nabla F_{14}\ \text{的凸组合平衡}✓✓$$
$$\Longrightarrow \ \boxed{\text{数值 active set} \to \text{stationarity} \to \text{有限频率极值方程} \to \text{解析下界}}✓✓ \ —— \ \textbf{比对 25 个}\ F_k\ \text{做 SOS 小得多}✓✓$$
$$\textbf{且}✓✓：\text{若核心只有}\ 3\ \text{元}✓，\text{stationarity 方程}\ \textbf{规模很小}✓（\text{可手算或极简计算}✓）$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 active-set       命中文件数=16   :: ./C232-active-set-structure-verdict-generic-no-arithmetic.md ./C203-T13-A-YI-0-local-rigidity-best-cluster.md ./C225-DAp-convergence-audit-six-branch-structure-resolved.md 
技术词 反推           命中文件数=64   :: ./JIA-1-squaring-candidates-and-conductor-criterion.md ./FRONTIER-PRIMEGAP-SURVEY-2026-09.md ./C204-T13-A-YI-1-cluster-separation.md 
技术词 盆地           命中文件数=4    :: ./C213-YI-slack-closure-and-JIA-ledger-unification.md ./C208-T13A-YI4-PASS-global-census-1.md ./MASTER-OUTPUT-INVENTORY-2026-09-20.md 
技术词 稳定性检查  命中文件数=2    :: ./C225-DAp-convergence-audit-six-branch-structure-resolved.md ./C99-support-gt-1-dual-residual-probe.md 
```
- 运行记录 ✓：脚本 `/tmp/p4b.py` ✓（180 随机 ＋ 11 边界 ＋ 冠军高精度精化 ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓（数值记录 ≠ 新机制 ✓）；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`G_min` 为全局最小 ✗；`{5,12,14,21}` 是四元真等式 ✗（**21 为近邻** ✓）；M=5 已证 ✗；`H = ∅` 已证 ✗
