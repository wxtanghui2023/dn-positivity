已查地图（**先查后写**）：`C-342`（偶频可行 ✓；Hankel 秩 `m = 5` ✓）、`C-341`（偶频归约 ✓）、`C-339`（`m >= 6` ✓）、`C-275`（可分层面组合＝单-k ✓）。回查见 §5 ✓

D0: 本档对象 = **C-343：符号层审计 ＋ 跨越判据**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 单点命中}✓✓：\text{在 C-342 的偶频最优}\ x\（even\text{-}max = 0.32544✓ \le \tfrac12✓）\ \text{处，}\ \textbf{32 个符号全部失败}✗✗ \Longrightarrow \textbf{唐先生的机制首次具体实现}✓✓$$
$$\qquad \text{最佳符号}\ (\sigma = [-1,1,-1,1,1]✓)\ \text{的}\ odd\text{-}max = \textbf{1.54695}✗（> \tfrac12✗）；\text{最差}\ 4.34301✗；\text{满足}\ odd \le \tfrac12\ \text{的符号数} = \textbf{0}✗$$
$$\textbf{② 精确刻画（跨越判据）}✓✓：\ \sigma \to -\sigma\ \text{使全部奇频}\ F_{2r+1}\ \textbf{变号}✓、\text{偶频}\ \textbf{不变}✓ \Longrightarrow \text{存在可用符号} \iff \textbf{不跨越}\ \pm\tfrac12✓✓$$
$$\qquad \text{即}\ \ \text{可用} \iff \neg( \max_r F_{2r+1} > \tfrac12 \wedge \min_r F_{2r+1} < -\tfrac12 )✓✓$$
$$\textbf{③ 本点状态}✓：\ \max_r F_{2r+1} = 1.54695 > \tfrac12✓，\ \min_r F_{2r+1} = -3.89503 < -\tfrac12✓ \Longrightarrow \textbf{跨越}✓ \Longrightarrow \textbf{无符号可用}✓✓$$
$$\textbf{④ 全域未证}✗：\text{本档}\ \textbf{只}\ \text{验证}\ \textbf{一个}\ x✗✓ \Longrightarrow \ H = \varnothing\ \textbf{仍未证}✗$$

## §1 数据（✓✓）

$$\textbf{偶频侧}✓：even\text{-}max = 0.32544011✓ \le \tfrac12✓ \Longrightarrow \text{偶频约束满足}✓$$
$$\textbf{奇频侧}✓：\text{最佳}\ odd\text{-}max = 1.54695376✗；\text{最差}\ odd\text{-}max = 4.34300952✗；\text{合格符号数} = 0/32✗$$
$$\textbf{翻转配对检验}✓✓：\max_r F_{2r+1}(\sigma) = 1.546954✓，\ \max_r F_{2r+1}(-\sigma) = 3.895034✓，\text{且}\ \min_r F_{2r+1}(\sigma) = -3.895034✓$$
$$\qquad \Longrightarrow \ \max_r F_{2r+1}(-\sigma) = -\min_r F_{2r+1}(\sigma)✓✓ \Longrightarrow \textbf{翻转关系逐字成立}✓✓$$
$$\textbf{偶频不变}✓✓：even(-\sigma) = even(\sigma) = 0.32544011✓✓ \Longrightarrow \textbf{偶频与符号无关}✓（\text{即}\ x = c^2\ \text{层}✓）$$

## §2 机制刻画（✓✓，本档最有价值 ✓）

$$\textbf{结构性困难}✓✓：\text{奇频约束}\ F_{2r+1} \le \tfrac12\ \text{在}\ \sigma\ \text{与}\ -\sigma\ \text{下}\ \textbf{互为镜像}✓ \Longrightarrow \text{单靠翻转}\ \textbf{只能救一侧}✓✗$$
$$\Longrightarrow \ \text{当且仅当奇频和}\ \textbf{同时越过}\ \pm\tfrac12\（\text{即「跨越」}✓）\ \text{时，}\ \textbf{无符号可用}✓✓ \ —— \ \text{这正是}\ \text{「偶频允许 ＋ 奇频符号不相容」}\ \text{的精确形式}✓✓$$
$$\textbf{与唐先生表述的对应}✓✓：\text{唐先生：}\ F_{2r+1} = \sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)✓（\text{幅值层}\ \times\ \text{符号层}✓）\ \Longrightarrow \text{本档证实该分解}\ \textbf{可操作}✓✓$$
$$\textbf{关键量}✓：\ \text{只需两个标量}\ \ \max_r F_{2r+1}✓、\min_r F_{2r+1}✓ \Longrightarrow \textbf{跨越判据} \text{判别成本极低}✓✓$$

## §3 下一步（✓✓，登记不执行 ✓）

$$\textbf{目标}✓✓：\text{在偶频可行域}\ E := \{x : \max_r F_{2r}(x) \le \tfrac12\}✓ \ \text{上}\ \text{检验}\ \textbf{跨越是否处处发生}✓✓$$
$$\text{若}\ \forall x \in E:\ \max_r F_{2r+1} > \tfrac12\ \text{且}\ \min_r F_{2r+1} < -\tfrac12✓ \Longrightarrow \ \boxed{H = \varnothing}✓✓（\text{机制干净}✓）$$
$$\textbf{反之}✓：\text{若存在}\ x \in E\ \text{无跨越}✓，\text{则须进一步}\ \text{在其上枚举符号}✓（32\ \text{个}✓，\text{成本低}✓）$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{未}\ \text{证明全域}✗；\text{亦}\ \textbf{未}\ \text{排除}\ \text{存在}\ x \in E\ \text{无跨越}✗$$

## §4 状态表（✓✓）

| 项 | 状态 |
|---|---|
| 偶频子系统 ✓ | **可行（`G_even^{min} = 0.3254`）** ✓ |
| 偶频单证路线 ✓ | **CLOSED（仅该子路线）** ✗ |
| 符号层分解 ✓ | **可操作（幅值层／符号层）** ✓✓ |
| 跨越判据 ✓ | **精确且廉价** ✓✓ |
| 偶频最优点 ✓ | **奇频不相容（32/32 失败）** ✓✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |
| `SOS` ✓ | **继续冻结** ✗ |
| `C-284` ✓ | **不重开** ✗ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 符号层        命中文件数=2    :: ./number-field-prime-geometry-death.md ./E6-3-cross-system-incompressible-core-intersection-audit.md 
技术词 跨越判据     命中文件数=0    :: 
技术词 全局翻转     命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4f3.py` ✓（33 次求值 ✓）；**未**完成全域搜索 ✗（较重版本被中止 ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- 过程注记 ⚠️：`pkill -f "p4f.py"` **命中自身命令行** ⟹ 自杀 ✗（`TOOLS.md` 已记录同类坑 ✓）⟹ 续作须用**显式 PID** ✓
- **不得**写成：`H = \varnothing` 已证 ✗（**仅一点** ✓）；符号不相容是全域事实 ✗；偶频路线已死（一般）✗
