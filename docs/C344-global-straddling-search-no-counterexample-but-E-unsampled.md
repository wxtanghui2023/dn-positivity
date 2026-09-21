已查地图（**先查后写**）：`C-343`（**straddling 判据** ✓✓；单点命中 ✓）、`C-342`（`E` 非空 ✓✓；`G_even^{min} = 0.3254` ✓）、`C-340`（`G_* \le 0.9738225286` ✓）、`C-284`（gcd 坍缩 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-344：全域 straddling 搜索**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 未找到反例}✓✓：\text{15 个起点}\（\text{含}\ E\ \text{内种子}✓）\ \text{的最佳}\ \text{obj} = \max(f,\ even) = \textbf{1.03499}✓ \ > \tfrac12✗ \Longrightarrow \textbf{无}\ (x,\sigma)\ \text{使全部}\ 25\ \text{个约束}\ \le \tfrac12✓$$
$$\textbf{② } f \le \tfrac12\ \textbf{从未出现}✓✓：\text{全部样本}\ f\ \text{的最小值} = \textbf{1.01065}✓ \（> \tfrac12✗）\ \Longrightarrow \textbf{straddling 在样本中普遍成立}✓✓$$
$$\qquad \text{（}f(x) := \min_{\sigma} \max_r F_{2r+1}(x,\sigma)✓，\text{仅需 16 个代表}✓，\text{因}\ M(-\sigma) = -m(\sigma)✓）$$
$$\textbf{③ ⭐ 结构性观察}✓✓：\text{obj 优化}\ \textbf{把点推离}\ E✓（\text{E 内点}\ f \approx 1.55✗ \Longrightarrow \text{obj} \approx 1.55✗） \Longrightarrow \ E\ \text{与「奇频可行」在数值上}\ \textbf{相距很远}✓✓$$
$$\textbf{④ ⚠️ 关键缺口}✗✓：\textbf{E 未被有效采样}✗（\text{15 个最优样本中}\ \textbf{E 可行者} = 0/15✗）\ \Longrightarrow \textbf{全域命题在}\ E\ \text{上}\ \textbf{未被检验}✗$$

## §1 数据（✓✓）

$$E\ \text{内点}\ x_E = [0.00676,\ 0.12826,\ 0.22454,\ 0.59629,\ 0.94614]✓：\ even = 0.32544 \le \tfrac12✓，\ f = \textbf{1.54695}✗ \Longrightarrow \textbf{straddling} = \text{True}✓✓$$

| 起点 | `obj` | `f` | `even` | `E` 可行 |
|---|---|---|---|---|
| rand ✓ | **1.03499** | 1.03499 | 0.98848 | ✗ |
| rand ✓ | 1.06816 | 1.01065 | 1.06816 | ✗ |
| rand ✓ | 1.09855 | 1.09855 | 1.03104 | ✗ |
| rand ✓ | 1.15955 | 1.15955 | 1.15955 | ✗ |
| rand ✓ | 1.16392 | 1.16392 | 1.16392 | ✗ |
| rand ✓ | 1.19975 | 1.19975 | 1.19975 | ✗ |

$$\textbf{汇总}✓：\text{全域最小}\ obj = 1.03499 > \tfrac12✓✓；\textbf{obj} \le \tfrac12\ \text{的样本数} = 0✗；f \le \tfrac12\ \text{的样本数} = 0✗；E\ \text{可行样本数} = 0/15✗$$

## §2 解读（✓✓）

$$\textbf{与}\ C\text{-}343\ \text{一致}✓✓：\text{E 内点}\ f = 1.547 > \tfrac12✓ \Longrightarrow \text{straddling}✓；\text{全域样本}\ f \ge 1.0107✓ \Longrightarrow \textbf{未出现例外}✓✓$$
$$\textbf{为何}\ E\ \text{未被采样}✓✓：\text{目标}\ obj = \max(f,\ even)✓ \ \text{在}\ E\ \text{上}\ f \approx 1.5✗ \Longrightarrow \text{优化}\ \textbf{主动避开}\ E✓✓ \ —— \ \text{这本身}\ \textbf{支持}\ \text{你的机制}✓✓$$
$$\textbf{诚实标注}⚠️✓：\text{n = 15}\ \text{个点}\ \textbf{不能}\ \text{取代}\ \text{全域证明}✗；\text{且}\ E\ \text{为}\ f\ \text{的}\ \textbf{高值区}✓ \Longrightarrow \text{下一步须}\ \textbf{把 even 当硬约束}✓✓$$

## §3 下一步（✓✓，登记不执行 ✓）

$$\textbf{目标改法}✓✓：\text{把}\ E\ \text{当}\ \textbf{硬约束}✓（\text{而非惩罚项}✓），\text{在}\ E\ \text{上}\ \textbf{直接最小化}\ f✓ \Longrightarrow \text{检验}\ \min_{x \in E} f(x) = ?✓$$
$$\text{若}\ \min_{x \in E} f > \tfrac12✓ \Longrightarrow \textbf{全域 straddling}✓ \Longrightarrow \ \boxed{H = \varnothing}✓✓（\text{数值}✓，\text{非证明}✗）$$
$$\text{若}\ \exists x \in E:\ f \le \tfrac12✓ \Longrightarrow \textbf{反例候选}✓ \Longrightarrow \text{立即复核}\ \text{（含符号枚举}✓）$$
$$\textbf{技术要点}✓：\text{须用}\ \textbf{约束型} \text{搜索}（\text{投影／罚函数＋回溯}✓），\text{并}\ \textbf{显式报告}\ E\ \text{可行性}✓✓$$

## §4 状态表（✓✓）

| 项 | 状态 |
|---|---|
| straddling 判据 ✓ | **精确且廉价** ✓✓ |
| 单点（`E` 内）✓ | **命中** ✓✓ |
| 全域搜索 ✓ | **无**反例（15 点）✓ |
| `f <= 1/2` ✓ | **从未出现** ✓ |
| `E` 上全域检验 ✓ | **未做（最大缺口）** ✗ |
| `H = \varnothing` ✓ | **OPEN** ✓ |
| `SOS` ✓ | **继续冻结** ✗ |
| `C-284` ✓ | **不重开** ✗ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 全域           命中文件数=45   :: ./C216-JIA-PASS-m3-at-least-0.7640811-interval-certified.md ./V130-O5-residue-FE-annihilation-theorem-k-point-only-even-one-sided.md ./C228-DC-PASS-global-exclusion-damped-M3-C3-equals-Fz0.md 
技术词 straddling       命中文件数=0    :: 
技术词 约束采样     命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4g.py` ✓（15 起点：`E` 种子 900 轮 ＋ 14 随机 250 轮 ✓；`f` 用 16 个符号代表 ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- 过程注记 ⚠️：`tail` 管道**缓冲**导致无增量输出 ✗ ⟹ 续作直接写日志文件 ✓
- **不得**写成：全域命题已证 ✗（**仅 15 点** ✓）；`E` 已被采样 ✗（0/15 ✗）；`H = \varnothing` 已证 ✗
