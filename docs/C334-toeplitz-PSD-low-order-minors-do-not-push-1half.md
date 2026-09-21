已查地图（**先查后写**）：`C-333`（H 的联合约束已明确；PSD ≠ 单线性核不等式 ✓）、`C-332`（覆盖型证书 ＋ H 定义 ✓）、`C-186`（单模 Turán 常数 (M+1)/(20M) ✓，M=5 给 0.06 ≪ 1/2 ✓）、`C-272`（真反例 0 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-334：Toeplitz PSD 低阶主子式审计（P1／P2 首刀）**，**零计算（解析推演）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① P1 结果}✓：\text{低阶 Toeplitz 主子式}\ \textbf{未能} \text{把}\ \tfrac12\ \text{阈值推穿}✗（\text{逐阶说明见 §2}✓）$$
$$\textbf{② 关键结构发现}✓✓：\ \text{秩约束}\ \operatorname{rank}(F_{k-l}) \le 10✓（\text{因}\ \mu\ \text{至多}\ 10\ \text{原子}✓）\ \Longrightarrow \ \textbf{只在}\ n \ge 11\ \text{才真正咬住}✓✓$$
$$\textbf{③ 低阶为何不咬}✓✓：\text{当}\ F_0 = 5✓、|F_k|\ \text{不大时}✓，\text{Toeplitz 近似对角}✓ \Longrightarrow n \le 10\ \text{时}\ \text{PSD}\ \textbf{自动满足}✓（\text{如}\ 5I_n \succeq 0✓）$$
$$\textbf{④ P4 试探}✓：\text{两个对称候选均在}\ \textbf{小}\ k\ \text{处失败}✓（\text{见 §4}✓）\ \Longrightarrow \ \textbf{未找到}\ H\ \text{中的点}✗；\ H = \varnothing\ \textbf{仍 OPEN}✓$$
$$\textbf{⑤ 纪律}✓✓：\textbf{未}\ \text{引入}\ SOS✗；\textbf{未}\ \text{把}\ PSD\ \text{称作「Fejér 已解决」}✗✓；\textbf{不}\ \text{建新框架}✗$$

## §1 设定（✓✓）

$$\textbf{Toeplitz}✓：T_n := (F_{k-l})_{1 \le k,l \le n} \succeq 0✓；F_0 = 5✓；F_{-k} = F_k✓；F_k = \sum_{j=1}^{5} \cos(k\theta_j)✓$$
$$\textbf{约束}✓：F_k \le \tfrac12✓（k \le 25✓）；F_k \ge -5✓（下界自动✓）；\operatorname{rank} T_n \le 10✓（\text{至多}\ 10\ \text{原子}✓）$$
$$\textbf{可实现性（不是「已解决」）}✓✓：\ \text{PSD}\ \textbf{只是} \text{可实现性约束}✓；\text{真正的问题是}\ \text{PSD} ＋ \text{10 原子} ＋ \text{25 个统一上界}\ \text{是否矛盾}✓✓$$

## §2 P1：逐阶检验（✓✓）

$$\textbf{2 阶}✓：25 - F_1^2 \ge 0 \Longrightarrow |F_1| \le 5✓ \ —— \ \textbf{平凡，无信息}✗✓$$
$$\textbf{3 阶}✓：\det = 125 - 10F_1^2 + 2F_1^2 F_2 - 5F_2^2 \ge 0✓；\text{代入}\ F_1, F_2 \le \tfrac12✓ \Longrightarrow \text{右端} = 10F_1^2 + 5F_2^2 - 125 < 0✓ \Longrightarrow \text{约束}\ \textbf{可满足}✓（F_1, F_2\ \text{小时}\ \det \approx 125 > 0✓）\ \Longrightarrow \ \textbf{无矛盾}✗✓$$
$$\textbf{全 1 向量}✓：1^t T_n 1 = 5n + 2\sum_{d=1}^{n-1}(n-d)F_d \ge 0✓ \Longrightarrow \text{只给}\ \textbf{负向下界}✓（\text{迫使不会全是}\ -5✓），\text{与}\ F_k \le \tfrac12\ \textbf{同向相容}✗✓$$
$$\textbf{Fejér 权}✓：\sum_{k=-(n-1)}^{n-1} (1 - \tfrac{|k|}{n}) F_k = \int |\sum_{l=1}^{n} e^{il\theta}|^2 d\mu \ge 0✓ \Longrightarrow 0 \le \sum \lambda_k F_k \le 5 + \tfrac{n-1}{2}✓ \ \Longrightarrow \ \textbf{恒可满足}✗✓$$
$$\textbf{P1 判定}✓✓：\text{低阶}\ \textbf{不产生矛盾}✗，\text{因}\ \text{约束}\ \textbf{与}\ \text{「近似对角 PSD」} \text{相容}✓✓$$

## §3 ⭐ 关键结构发现：秩只在 `n >= 11` 咬（✓✓）

$$\text{若}\ F_k\ \text{全部很小}✓，\ 5I_n \succeq 0✓ \Longrightarrow n \le 10\ \text{时}\ \text{PSD}\ \textbf{自动成立}✓✓$$
$$\text{而}\ \operatorname{rank} T_n \le 10✓ \Longrightarrow n \ge 11\ \text{时}\ T_n\ \textbf{必奇异}✓✓ \Longrightarrow \textbf{此后}\ \text{PSD}\ \text{才携带}\ \textbf{方程型（非不等式）} \text{内容}✓✓$$
$$\Longrightarrow \textbf{攻击面应移到}\ n \ge 11✓（\text{即}\ 10\ \text{阶递推／秩约束}✓），\textbf{而非} \text{低阶不等式}✗✓$$

## §4 P4 试探：两个对称候选（✓，未找到反例 ✓）

$$\textbf{候选甲}✓：\theta = (0, \tfrac{\pi}{4}, \tfrac{\pi}{2}, \tfrac{3\pi}{4}, \pi)✓ \Longrightarrow F_1 = 0✓ \le \tfrac12✓，\text{但}\ F_2 = 1 ✗ > \tfrac12✓ \ \Longrightarrow \ \textbf{k=2 失败}✗✓$$
$$\textbf{候选乙}✓：\theta_j = \tfrac{j\pi}{6}✓（j = 1,\dots,5✓）\Longrightarrow F_1 = 0✓，F_2 = -1✓，F_3 = 0✓，F_4 = -1✓，F_5 = 0✓，\text{但}\ F_6 = 1 ✗ > \tfrac12✓ \ \Longrightarrow \ \textbf{k=6 失败}✗✓$$
$$\textbf{结论}✓✓：\text{对称候选}\ \textbf{在小}\ k\ \text{处即失败}✓ \Longrightarrow \textbf{未找到}\ H\ \text{中的点}✗；\text{与}\ C\text{-272 的}\ \textbf{真反例}\ 0✓\ \text{一致}✓✓$$

## §5 判死标准（保持 ✓✓）

$$\text{若找到合法单位圆五元组使}\ F_k \le \tfrac12✓（k \le 25✓）\ \Longrightarrow \ H \ne \varnothing✓ \Longrightarrow \boxed{\textbf{M=5 原命题为假}}✓$$
$$\textbf{当前状态}✓✓：\boxed{\ C\text{-}333:\ H\ \text{的联合约束已明确};\ H = \varnothing\ \textbf{仍 OPEN}\ }✓$$

## §6 下一步（P2／P4，唐先生口径 ✓）

$$\textbf{P2}✓：\text{低阶不够}\ \Longrightarrow \text{用}\ F_k = \sum_j T_k(c_j)\ \text{把}\ PSD\ \textbf{拉回}\ c\ \text{空间}✓（\text{Chebyshev}✓）$$
$$\textbf{P4}✓✓：\text{若各阶检验均留可行域}\ \Longrightarrow \textbf{实际构造}\ H\ \text{中的点}✓（\text{一旦找到即决定性反例}✓✓）$$
$$\textbf{P3}✓：\text{只有出现明确半代数矛盾时，才整理成}\ SOS／\text{Positivstellensatz}✗✓$$

## §7 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 主子式链     命中文件数=0    :: 
技术词 可实现性约束 命中文件数=0    :: 
技术词 大质量        命中文件数=0    :: 
```
- 本档新增 ✓：`主子式链`／`可实现性约束`（依上表判 ✓）
- **零计算** ✗（仅解析推演 ✓）；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：H = ∅ 已证 ✗；PSD 已解决该问题 ✗；低阶 PSD 已足够 ✗；已找到反例 ✗
