已查地图（**先查后写**）：`C-352`（方系统方案 ✓ ；`0/40` 仅命中问题 ✓；**逻辑锁死** ✓✓）、`C-351`（三分裂 ✓✓）、`C-350`（**单向蕴含** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-353：`3+2` 存在性未决 ＋ 方系统精化 ＋ 三出口**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 存在性口径}✓✓：\ \boxed{3+2\ \text{existence}\ =\ \textbf{OPEN}}✓ \ —— \ \textbf{不是}\ 3+2 = \varnothing✗✓$$
$$\qquad \text{维数}\ 5 - 4 = 1\ \textbf{只是启发}✓，\textbf{不}能单独证明解支存在✗✓；\text{而}\ \text{「随机下降}\ 0/40」\ \textbf{更不能}拿来判空✗✓$$
$$\textbf{② 方系统写法精化}✓✓：\text{固定}\ \beta\ \Longrightarrow\ \textbf{有限维四元方程的解集}✓；\ \textbf{需进一步证明}\ \text{其在正象限中的局部离散性／分支结构}✓$$
$$\qquad \textbf{不得}预设 \text{每个}\ \beta\ \text{必有离散解}✗✓：\text{奇次幂矩方程的}\ \textbf{Jacobian 可能退化}✗✓ \Longrightarrow \text{须}\ \textbf{Newton ＋ 区间验证}✓✓（\text{先发现分支，再确认}✓）$$
$$\textbf{③ 逻辑方向画全}✓✓：\ H \ne \varnothing \ \not\Rightarrow\ \mathcal Z \cap E \ne \varnothing✓；\quad \mathcal Z \cap E \ne \varnothing \ \Longrightarrow\ H \ne \varnothing✓✓$$
$$\qquad \Longrightarrow \ H = \varnothing \Rightarrow \mathcal Z \cap E = \varnothing✓；\quad \boxed{\mathcal Z \cap E = \varnothing \ \not\Rightarrow\ H = \varnothing}✓✓$$
$$\textbf{④ 三出口}✓✓：\text{见 §3}✓（(a) 结构性负结果 ✓；(b) \textbf{精确候选} ✓✓；(c) \textbf{矩映射奇异性}✓✓）$$
$$\textbf{⑤ 纪律}✓✓：\textbf{不}提前做\ Bridge\ A✗；\textbf{不}把\ 0/40\ \text{或维数计数升级为存在性结论}✗✓$$

## §1 方系统的正确写法（✓✓）

$$\textbf{固定}\ b_1 = \beta✓ \Longrightarrow \text{四方程}✓：$$
$$\qquad a_1 + a_2 + a_3 - b_2 = \beta✓；\quad a_1^3 + a_2^3 + a_3^3 - b_2^3 = \beta^3✓；\quad a_1^5 + \cdots - b_2^5 = \beta^5✓；\quad a_1^7 + \cdots - b_2^7 = \beta^7✓$$
$$\textbf{未知}✓：(a_1, a_2, a_3, b_2) \in (0,1]^4✓ \ —— \ \text{四元四方程}✓$$
$$\textbf{退化风险}✓✓：\text{奇次幂映射}\ (a_1,a_2,a_3) \mapsto (\sum a^1, \sum a^3, \sum a^5, \sum a^7)✓ \ \text{的}\ \textbf{Jacobian 可能在}\ a_i\ \text{碰撞处退化}✗✓$$
$$\qquad \Longrightarrow \ \text{须}\ \textbf{分支追踪 ＋ 区间验证}✓✓，\textbf{不}把数值根当定理✗✓$$

## §2 逻辑方向（✓✓，本档核心 ✓）

| 命题 ✓ | 真值 ✓ |
|---|---|
| `\mathcal Z \cap E \ne \varnothing \Rightarrow H \ne \varnothing` ✓ | **真** ✓✓ |
| `H = \varnothing \Rightarrow \mathcal Z \cap E = \varnothing` ✓ | **真（逆否）** ✓ |
| `\mathcal Z \cap E = \varnothing \Rightarrow H = \varnothing` ✗ | **假** ✗✓ |
| `H \ne \varnothing \Rightarrow \mathcal Z \cap E \ne \varnothing` ✗ | **假** ✗✓ |

$$\Longrightarrow \ \textbf{故}\ C\text{-}352\ \text{的任务}\ \textbf{不是} \text{「证明}\ H\ \text{为空」}✗✓，\text{而是}\ \textbf{消灭最危险的一类精确奇频抵消反例}✓✓$$
$$\textbf{真正主线}✓✓：\text{小奇频} \Longrightarrow \text{接近}\ \mathcal Z \Longrightarrow \textbf{必须产生偶频代价}✓ \ —— \ \text{即后续}\ \textbf{Bridge A}✓$$

## §3 三出口（✓✓）

$$\textbf{出口 (a)}✓：\text{解支全部满足}\ \max_{1 \le r \le 12} F_{2r} > \tfrac12✓ \Longrightarrow \ \boxed{\mathcal Z \cap E = \varnothing}✓$$
$$\qquad \text{性质}✓✓：\text{这是}\ \textbf{有效的结构性负结果}✓✓，\ \textbf{但}不是\ H = \varnothing✗✓$$
$$\textbf{出口 (b)}✓✓：\exists\ \text{解支使}\ \max_{1 \le r \le 12} F_{2r} \le \tfrac12✓ \Longrightarrow \ \boxed{\mathcal Z \cap E \ne \varnothing}✓✓ \ \Longrightarrow\ H \ne \varnothing\ \text{的}\ \textbf{精确候选}✓✓$$
$$\qquad \text{处置}✓✓：\textbf{立即停止}\ \text{「证明}\ H = \varnothing」\ \text{方向}✗✓，\text{转}\ \textbf{高精度验证}✓✓$$
$$\textbf{出口 (c)}✓✓：\text{某}\ \beta\ \text{附近出现}\ \textbf{Jacobian 退化／分支合并／连续异常族}✓ \Longrightarrow \text{不能归为「数值失败」}✗✓$$
$$\qquad \Longrightarrow \ \text{登记为}\ \boxed{3+2\ \text{moment-map singularity}}✓✓ \ —— \ \textbf{恰可能是}\ Bridge\ A\ \text{的障碍所在}✓✓$$

## §4 主线结构（✓✓）

$$H \ne \varnothing \ \supset\ \mathcal Z \cap E \ne \varnothing✓ \quad \longrightarrow \quad \text{C-352}\ \text{方系统}\ \longrightarrow \quad \text{精确抵消型是否存在}✓$$
$$\text{若}\ \mathcal Z \cap E = \varnothing✓ \ \Longrightarrow\ \text{才进入}\ \textbf{真正困难的一步}✓✓：\text{近抵消} \to \textbf{moment-map stability} \to \text{偶频代价}✓✓$$
$$\textbf{比较}✓✓：\text{此路线}\ \textbf{比继续做}\ G_*\ \text{数值优化清楚得多}✓✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 存在性未决  命中文件数=0    :: 
技术词 分支结构     命中文件数=3    :: ./EG-test-results.md ./C240-B2-1-II-five-function-reduction-is-false-true-target-holds.md ./ABD-1p-future-branching.md 
技术词 矩映射奇异性 命中文件数=0    :: 
技术词 三出口        命中文件数=14   :: ./C319-directed-recheck-C272-pending-box-set-semantics-GAP-CONFIRMED.md ./C282-threshold-bridge-analytic-feasibility-threshold-bridge-identity-and-dissolution.md ./C320-directed-recheck-C273-v5-design-family-CLOSED-M5-question-OPEN.md 
```
- **零计算** ✗（口径与结构档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`3+2 = \varnothing` ✗；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；每β必有离散解 ✗
