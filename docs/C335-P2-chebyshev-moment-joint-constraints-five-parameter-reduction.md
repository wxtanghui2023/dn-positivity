已查地图（**先查后写**）：`C-334`（低阶 PSD 不咬；**秩只在 n>=11 咬** ✓✓）、`C-333`（H 联合约束；PSD ≠ 单线性核 ✓）、`C-153`（M=2：极小点处**精确代数** ＋ 其余 Lipschitz 的覆盖型证明 ✓✓）。回查见 §7 ✓

D0: 本档对象 = **C-335：P2 首刀 —— Chebyshev-moment 联立与五参数化**，**零计算（解析推演）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 陷阱已记}✓✓：\ \det T_{11} = 0\ \textbf{单独不构成强约束}✗（\text{任意五个互异}\ c_j\ \text{本就有低阶消灭多项式}✓）\ \Longrightarrow \ \textbf{秩 ＋ 矩上界} \text{才是核心}✓✓$$
$$\textbf{② 五参数化}✓✓：\text{全部}\ F_k\ \text{由}\ (m_1,\dots,m_5)✓（m_r := \sum_j c_j^r✓）\ \textbf{完全决定}✓✓ \Longrightarrow \ \text{问题降为}\ \textbf{5 维}✓$$
$$\textbf{③ 新增经典联合约束}✓✓：\ c_j\ \text{为实数}\ \Longrightarrow \ \textbf{Newton 不等式}✓（e_r^2 \ge e_{r-1} e_{r+1}✓）\ \text{＋ 实根判别式}✓ \ —— \ \textbf{这是递推之外的独立约束}✓✓$$
$$\textbf{④ 已导出的定量约束}✓：m_1 \le \tfrac12✓；m_2 \le 2.75✓；\text{计数推论}✓：\#\{j: c_j \ge 0.9\} \le 2✓，\#\{j: c_j \ge 0.7\} \le 3✓$$
$$\textbf{⑤ 本档判定}✓\ ⚠️：\textbf{未}找到矛盾 ✗；\textbf{未}找到反例 ✗；\textbf{P4 须先批准}✗✓$$

## §1 P2 的正确对象（✓✓）

$$\textbf{五节点消灭多项式}✓：\ \det T_{11} = 0 \iff \exists\, 0 \ne q = (q_0,\dots,q_{10})\ \text{使}\ \sum_{k=0}^{10} q_k e^{ik\theta_j} = 0\ (j = 1,\dots,5)✓$$
$$\qquad \text{等价实形式}✓：\ Q(\theta) = a_0 + \sum_{k=1}^{10} a_k \cos(k\theta)✓，Q(\theta_j) = 0✓$$
$$\textbf{但}✓✓：\text{该条件}\ \textbf{对任意五个互异节点自动成立}✗ \Longrightarrow \textbf{必须与外层矩上界联立}✓✓$$
$$\boxed{\text{五节点} \;+\; Q(c_j) = 0 \;+\; F_k = \sum_j T_k(c_j) \le \tfrac12✓}$$

## §2 五参数化（✓✓，本档关键结构 ✓）

$$\textbf{矩定义}✓：m_r := \sum_{j=1}^{5} c_j^r✓；e_r := e_r(c_1,\dots,c_5)✓（初等对称函数✓）$$
$$\textbf{决定关系}✓✓：\ T_k\ \text{为}\ k\ \text{次多项式}✓ \Longrightarrow F_k = \sum_j T_k(c_j)\ \text{是}\ (m_1,\dots,m_k)\ \text{的函数}✓；\text{而由 Newton／Girard}✓，\ m_r\ (r \ge 6)\ \textbf{由}\ m_1..m_5\ \text{决定}✓✓$$
$$\Longrightarrow \ \textbf{整条序列}\ (F_k)_{k \le 25}\ \textbf{由五参数完全决定}✓✓ \Longrightarrow \text{25 个不等式}\ \textbf{高度冗余}✓（与 C-333 的递推冗余一致 ✓✓）$$

## §3 显式低阶式（✓）

$$F_1 = m_1✓；\ F_2 = 2m_2 - 5✓；\ F_3 = 4m_3 - 3m_1✓；\ F_4 = 8m_4 - 8m_2 + 5✓；\ F_5 = 16m_5 - 20m_3 + 5m_1✓$$
$$\textbf{由此}✓：F_1 \le \tfrac12 \Longrightarrow m_1 \le \tfrac12✓；F_2 \le \tfrac12 \Longrightarrow 2m_2 - 5 \le \tfrac12 \Longrightarrow m_2 \le 2.75✓$$
$$\textbf{计数推论}✓✓：\text{若}\ r\ \text{个}\ c_j \ge a✓ \Longrightarrow m_1 \ge ra - (5-r)✓ \Longrightarrow r(a+1) \le 5.5✓ \Longrightarrow \ a = 0.9 \Rightarrow r \le 2✓；a = 0.7 \Rightarrow r \le 3✓$$

## §4 ⭐ 新增经典联合约束：Newton 不等式（✓✓）

$$\text{因}\ c_j \in \mathbb{R}✓ \Longrightarrow \text{特征多项式}\ \prod_j (x - c_j)\ \textbf{全实根}✓ \Longrightarrow \textbf{Newton 不等式}✓：\ e_r^2 \ge e_{r-1} e_{r+1}✓$$
$$\textbf{为何它是新东西}✓✓：\text{它}\ \textbf{不}\ \text{是 10 阶递推的推论}✗（\text{递推只反映「根在哪」，不反映「根是实且在一维区间」}✓✓）$$
$$\textbf{再加强}✓：c_j \in [-1,1]✓（\textbf{区间}，\text{非仅实数}✓）\ \Longrightarrow \text{全部根落在}\ [-1,1]✓ \Longrightarrow \text{可用 Sturm／判别式型条件表述}✓✓$$
$$\Longrightarrow \ \boxed{\text{约束系统} ＝ \text{25 个矩上界} ＋ \text{Newton 实根条件} ＋ \text{区间条件}}✓✓$$

## §5 本档判定（✓⚠️）

$$\textbf{未找到矛盾}✗：\text{逐项检验}\ \text{未产生}\ \text{「某}\ F_r > \tfrac12\ \text{被迫」 或}\ \text{「节点分布不可能」}✓$$
$$\textbf{结构性观察}✓✓：\text{自然极值构型}\（\text{等距／对称节点}✓）\ \textbf{在低阶}\ k\ \text{即失败}✓（C-334：k=2✓、k=6✓）\ \Longrightarrow \text{绑定约束}\ \textbf{大概率在低阶}✓ \Longrightarrow \text{问题实质是}\ \textbf{联合系统是否有解}✓（\text{而非高阶}✓）$$
$$\textbf{诚实标注}⚠️：\text{本档}\ \textbf{只}\ \text{建立约束系统与五参数化}✓，\textbf{不}\ \text{声称方向已通}✗$$

## §6 P4 纪律（✓✓）

$$\text{P4}\ \textbf{须先批准}✓✓（\text{唐先生纪律}✓）：\text{不得}\ \text{把数值探索偷偷变成证明}✗✓；\text{若批准，目标改为}\ \textbf{寻找}\ \max_{k \le 25} F_k\ \text{的低值极小构型}✓$$

## §7 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 五参数化     命中文件数=0    :: 
技术词 Newton           命中文件数=38   :: ./round2-index-status.md ./C92-item-by-item-audit-three-leaves-verification-depth-and-residual-risk-list.md ./TUR2-newton-baseline-and-excess-observable.md 
技术词 不等式        命中文件数=295  :: ./candidate-proof-v1.md ./C174-direct-check-hardest-point-framework-cannot-cover-period-gate-not-eps.md ./AUDIT-direction-depth.md 
技术词 节点消灭多项式 命中文件数=0    :: 
技术词 矩上界联立  命中文件数=0    :: 
```
- 本档新增 ✓：`五参数化`／`矩上界联立`（依上表判 ✓）
- **零计算** ✗（仅解析 ✓）；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：P2 已通 ✗；Newton 条件已足够 ✗；det T_11 = 0 是强约束 ✗；已找到反例 ✗
