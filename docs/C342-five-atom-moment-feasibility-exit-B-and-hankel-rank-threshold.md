已查地图（**先查后写**）：`C-341`（偶频归约 ✓；低阶矩链不足 ✓）、`C-340`（P4-D ✓）、`C-339`（`m >= 6` ✓）、`C-334`（**秩约束在阈值后才咬**（`n >= 11`）✓✓）、`C-336`（矩不等式 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-342：五原子 [0,1] 矩可行性审计（＋ Hankel 秩阈值）**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 出口判定}✓✓：\ \boxed{\textbf{出口 B 命中}}✓ \ —— \ \textbf{偶频系统存在五原子可行点}✓✓ \Longrightarrow \textbf{偶频路线本身不能完成证明}✗$$
$$\textbf{② 且余量巨大}✓✓：\ G_{even}^{min} \approx \textbf{0.32539}✓ \ \ll \tfrac12✓ \Longrightarrow \textbf{偶频约束很宽松}✓✓$$
$$\textbf{③ 点态证书（路线 A）在偶频侧} \textbf{死掉}✗✓：\text{因可行性余量}\ 0.17✓ \Longrightarrow \textbf{不存在} \text{可排除的 pointwise 组合}✗✓$$
$$\textbf{④ ⭐ Hankel 秩阈值}✓✓：\operatorname{rank} H_m \le 5\ \forall m✓；\text{且}\ \textbf{秩约束在}\ m = 5\ \text{才开始咬}✓✓（\text{size}\ 6\ \text{降到 rank}\ 5✓）\ —— \ \textbf{与 C-334 的}\ n \ge 11\ \textbf{同型}✓✓$$
$$\textbf{⑤ 下一步}✓：\text{须加入}\ \textbf{奇频约束}✓（\text{出口 B 后续}✓）；\text{完整系统}\ \textbf{即}\ H✓，\textbf{不}过该步不能收口✗$$

## §1 计算设定（✓✓）

$$\textbf{偶频子系统}✓：\text{仅取}\ k \in \{2, 4, \dots, 24\}✓（r = 1..12✓），\text{最小化}\ \max_{r \le 12} F_{2r}(c)✓，c \in [-1,1]^5✓$$
$$\textbf{方法}✓：40\ \text{随机起点} ＋ \text{模式搜索}（1500\ \text{轮}✓）✓$$
$$\textbf{恒等式}✓（C-341✓）：F_{2r} = 2\sum_j T_r(c_j)^2 - 5✓$$

## §2 可行性结果（✓✓）

$$\textbf{最优偶频构型}✓✓：\ G_{even}^{min} = \textbf{0.3253858939}✓ \ < \tfrac12✓✓（\text{余量}\ 0.1746✓）$$
$$\qquad \text{active}\（10^{-8}✓）：\{6,\ 8,\ 10\}✓ \ \text{等小集合}✓；\text{多个起点给}\ 0.45 \sim 0.47✓（\text{同样}\ < \tfrac12✓）$$
$$\qquad c_{sorted} \approx [-0.764,\ -0.616,\ +0.106,\ +0.285,\ +0.440]✓；\ x_j = c_j^2\ \text{排序} = [0.00676,\ 0.12826,\ 0.22454,\ 0.59629,\ 0.94614]✓$$
$$\textbf{矩}✓：s_0 = 5✓；s_1 = 1.90198✓；s_2 = 1.31766✓；s_3 = 1.07242✓；\dots；s_{12} = 0.51664✓ \ \Longrightarrow \textbf{全部落在低阶链允许范围内}✓$$
$$\textbf{结论}✓✓：\exists x \in [0,1]^5\ \text{使}\ F_{2r} \le \tfrac12\ \forall r \le 12✓✓ \Longrightarrow \ \boxed{\textbf{出口 B}}✓$$

## §3 路线 A（点态证书）的判定（✗✓）

$$\text{形态}✓：\exists \mu_r \ge 0✓，Q(x) = \sum_r \mu_r P_r(x)✓，\min_{[0,1]} Q > \tfrac{1}{5}\sum_r \mu_r \Longrightarrow \bot✓$$
$$\textbf{判定}✗✓：\text{因}\ G_{even}^{min} = 0.3254 \ll \tfrac12✓，\text{可行域}\ \textbf{非空且宽}✓ \Longrightarrow \textbf{不存在} \text{此类证书}✗✓$$
$$\textbf{读法}✓✓：\text{这}\ \textbf{印证唐先生的分层}✓ —— \text{路线 A 只是}\ \textbf{单变量 pointwise 问题}✗；\text{偶频侧它}\ \textbf{不给信息}✗✓$$

## §4 ⭐ Hankel 秩（✓✓，本档最有价值 ✓）

$$H_m := (s_{i+j})_{0 \le i,j \le m}✓；\ \text{五原子} \Longrightarrow \operatorname{rank} H_m \le 5✓；\ [0,1]\ \text{支撑} \Longrightarrow H_m \succeq 0✓ \ \text{且局部化}\ (s_{i+j} - s_{i+j+1}) \succeq 0✓$$
$$\textbf{实测秩}✓✓：m = 0 \to 1✓；1 \to 2✓；2 \to 3✓；3 \to 4✓；4 \to 5✓；\ \textbf{5 \to 5}✓✓；6 \to 5✓$$
$$\Longrightarrow \ \boxed{\text{秩约束在}\ m = 5\ \text{（即 size}\ 6\ \text{的 Hankel）才开始咬}}✓✓ \ —— \ \textbf{与 C-334 的「秩只在}\ n \ge 11\ \text{才咬」同型}✓✓$$
$$\textbf{共性}✓✓：\text{两类对象}\（\text{Toeplitz 系数矩阵／Hankel 矩矩阵}✓）\ \text{都出现}\ \textbf{「秩条件只在维数超过阈值后才产生方程型内容」}✓✓$$

## §5 出口与下一步（✓✓）

$$\textbf{出口 A（偶频矛盾）}✗：\textbf{未}\ \text{命中}✗；\textbf{出口 B（五原子可行）}✓✓：\textbf{命中}✓；\textbf{出口 C（一般测度可行、五原子不可行）}✗：\textbf{未}\ \text{出现}✗（\text{五原子本身可行}✓）$$
$$\textbf{下一步}✓（\text{唐先生出口 B 后续}✓）：\text{把}\ \textbf{奇频约束}\ F_{2r+1} \le \tfrac12✓（r = 0..12✓）\ \text{加入}✓ \Longrightarrow \text{即}\ \textbf{完整}\ H✓$$
$$\textbf{诚实标注}⚠️：\text{本档}\ \textbf{未}\ \text{缩小}\ H\ \text{本身}✗ \ —— \ \text{只是}\ \textbf{排除了偶频单独可证}✗✓，\text{并获得}\ \textbf{秩阈值结构}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 五原子矩证书 命中文件数=0    :: 
技术词 点态证书     命中文件数=0    :: 
技术词 秩阈值        命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4e.py` ✓（40 起点；Hankel 秩 `m = 0..6`；`m = 7` 处因 `s` 长度不足报错 ✗，不影响结论 ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：偶频已排除 ✗（**可行** ✓）；点态证书不可能存在（一般性）✗（仅**偶频侧** ✓）；`H` 已缩小 ✗
