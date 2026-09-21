已查地图（**先查后写**）：`C-373`（**纤维不确定** ✗✓；`\delta_*` ✓）、`C-349`（**四阶 signed-moment** ✓✓）、`C-371`（`\mathcal Z \cap E = \varnothing` ✓✓）、`C-344`（**`\sigma \leftrightarrow -\sigma` 对称** ✓✓）、`C-342`（**偶频最优 `x`** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-374：`E`-纤维上的奇频传播审计（32 符号层）**，**有计算（数值探针，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 框架}✓✓：\text{偶频几何}\ x_j = c_j^2 \in [0,1]✓（\text{偶频}\ F_{2r} = \sum_j T_r(2x_j - 1)\ \textbf{仅依赖}\ x✓✓）；\ \text{奇频}\ F_{2r+1} = \sum_j w_j R_r(x_j)✓，\ w_j := \sigma_j\sqrt{x_j}✓$$
$$\qquad \Longrightarrow \ \text{问题天然分裂}✓✓：\underbrace{x_1,\dots,x_5}_{\text{偶频几何}} + \underbrace{\sigma \in \{\pm 1\}^5}_{\text{符号层（}\le 32✓）}✓✓$$
$$\textbf{② 两个版本}✓✓：\min_{\sigma}\max_{0 \le r \le 12}O_r(x,\sigma)✓；\ \textbf{更适合反证者}：\boxed{\min_{\sigma}\max_{0 \le r \le 12}|O_r(x,\sigma)|}✓✓$$
$$\textbf{③ ⭐ 首轮探针（本档核心）}✓✓：\ C\text{-}342\ \text{偶频最优}\ x✓：\ \min_\sigma \max_r |O_r| = \boxed{2.556}✓✓（\sigma = (1,1,1,-1,-1)✓）；\ even\text{-}max = 0.325✓$$
$$\qquad E_{\mathrm{even}}\ \text{采样最差点}✓（x = (0.0326, 0.7715, 0.3456, 0.9514, 0.6352)✓，\ even\text{-}max = \boxed{0.472}✓ \textbf{逼近}\ \tfrac12\ \text{边界}✓）：\ \min_\sigma\max_r|O_r| = \boxed{2.189}✓✓$$
$$\qquad \textbf{全部}\ > \tfrac12✓✓（\text{余量}\ \approx 1.69 \sim 2.06✓，\text{即}\ 4.4\times\ \text{规模}✓✓）$$
$$\textbf{④ 「奇频全}\ \le \tfrac12\text{」 搜索}✓✓：40000\ \text{个}\ x \times 32\ \text{层}✓ \Longrightarrow \textbf{命中 0}✓✓（\text{与 Bridge A 一致}✓，\textbf{非}证明✗✓）$$
$$\textbf{⑤ 结构观察}✓✓：\sigma \leftrightarrow -\sigma\ \text{给横同值}✓✓（\text{列表互见成对}✓） \Longrightarrow \textbf{16 个本质层}✓✓（与 C-344 一致✓）；\ E_{\mathrm{even}}\ \textbf{很薄}✓（60000\ \text{随机点仅}\ 4\ \text{个满足}✗✓）$$
$$\qquad \Longrightarrow \ \textbf{随机采样效率低}✗✓ \Longrightarrow \text{须从}\ C\text{-}342／C\text{-}345\ \text{偶频极小点} \textbf{定向采样}✓✓$$
$$\textbf{⑥ 对接点}✓✓：\ C\text{-}349\ \text{的}\ O_0 = O_1 = O_2 = O_3 = 0 \iff \sum_j w_j x_j^m = 0✓（m = 0,1,2,3✓） ＋ \ C\text{-}371\ \text{的}\ \mathcal Z \cap E = \varnothing✓$$
$$\qquad \Longrightarrow \ \text{问题}\ = \ \text{「在满足全部偶频约束的}\ x\ \text{空间里，16 个符号层距}\ \textbf{四阶 signed-moment nullspace}\ \text{有多远」}✓✓$$

## §1 公式与验证（✓✓）

$$R_r(x)\ \text{由}\ T_{2r+1}(c) = c\,R_r(c^2)\ \text{定义}✓ \Longrightarrow \ R_0 = 1✓，\ R_1 = 4x - 3✓，\ R_2 = 16x^2 - 20x + 5✓，\ R_3 = 64x^3 - 112x^2 + 56x - 7✓$$
$$\textbf{数值校验}✓✓：R_0(0.25) = 1✓；\ R_1(0.25) = -2 = 4(0.25) - 3✓✓（\text{与 C-347 表一致}✓）$$
$$O_r(x,\sigma) = \sum_{j=1}^{5}w_j R_r(x_j)✓，\ r = 0,\dots,12✓；\ \text{偶频}\ F_{2r} = \sum_j T_r(2x_j - 1)✓，\ r = 1,\dots,12✓$$

## §2 探针细节（✓✓）

$$\textbf{点 1}✓✓：\ C\text{-}342\ \text{最优}\ x = (0.00676, 0.12826, 0.22454, 0.59629, 0.94614)✓，\ even\text{-}max = 0.325440✓；\ \min_\sigma\max_r|O_r| = 2.555726✓✓$$
$$\textbf{点 2}✓✓：\ \text{采样最差}\ x = (0.032554, 0.771474, 0.345586, 0.951415, 0.635179)✓，\ even\text{-}max = 0.472416✓（\textbf{逼近}\ \tfrac12✓）；\ \min_\sigma\max_r|O_r| = 2.188963✓✓$$
$$\qquad \text{前六小层}✓：2.188963（\sigma = (-1,1,-1,1,1)✓ 与其反相✓）；2.307927✓；2.689779✓ \ —— \textbf{成对出现}✓✓（\sigma \leftrightarrow -\sigma✓）$$
$$\textbf{读法}✓✓：\ even\text{-}max\ \textbf{越接近}\ \tfrac12✓，\ \text{奇频余量}\ \textbf{仍}\ \ge 2.19✓✓ \Longrightarrow \ \text{与「偶频越紧、奇频越被迫放大」}\ \textbf{一致}✓✓$$

## §3 预注册出口（✓✓）

$$\textbf{出口 1}✓✓：\text{若}\ \forall x \in E_{\mathrm{even}}✓：\min_\sigma\max_r|O_r(x,\sigma)| > \tfrac12✓（\text{尤其}\ \textbf{一致正余量}✓） \Longrightarrow \textbf{Bridge A 关闭}✓✓$$
$$\textbf{出口 2}✓✓：\text{若某}\ (x,\sigma)✓ \ \text{使全部奇频}\ \le \tfrac12✓ \Longrightarrow \textbf{不能}靠简单符号层统一下界✗✓ \Longrightarrow \text{须更强}\ x\text{-几何耦合}✓✓$$
$$\textbf{出口 3}✓：\text{若}\ E_{\mathrm{even}}\ \text{上}\ \min_\sigma\max_r|O_r|\ \text{可}\ \to \tfrac12✓ \Longrightarrow \text{临界结构}✓（\text{须高精度定位}✓）$$

## §4 方法（✓✓）

$$\textbf{采样策略}✓✓：\textbf{不}用均匀随机✗（E_{\mathrm{even}}\ \text{薄}✗✓） \Longrightarrow \text{从}\ C\text{-}342／C\text{-}345\ \text{偶频极小点出发}✓ \ \text{沿}\ E_{\mathrm{even}}\ \text{边界}\（even\text{-}max = \tfrac12✓）\ \textbf{定向采样}✓✓$$
$$\textbf{层数}✓✓：32 \to 16✓（\sigma \leftrightarrow -\sigma\ \text{同值}✓） \Longrightarrow \text{每点仅}\ 16\ \text{次评估}✓✓（\text{极廉价}✓）$$
$$\textbf{纪律}✓✓：\textbf{不}把数值余量当定理✗✓；\textbf{不}跳步✗；\textbf{不}写\ H = \varnothing✗$$

## §5 账本（✓✓）

| 对象 ✓ | 状态 ✓ |
|---|---|
| `\mathcal Z \cap E` ✓ | **✓ 已完成** ✓✓ |
| `\delta_*` ✓ | **✓ 存在性（Stage 1）** ✓✓ |
| `E_{\mathrm{even}}` 上 `\min_\sigma\max_r\|O_r\|` ✓ | **数值余量 `\ge 2.19`（5 点）⚠️，未证** ✓ |
| Bridge A ✓ | **OPEN（唯一下一主线）** ✓✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 符号层        命中文件数=4    :: ./C346-P4F-sealed-wording-locked-and-next-phase-analytic-lower-bound.md ./C343-sign-layer-straddle-criterion-and-even-optimal-point-hit.md ./number-field-prime-geometry-death.md 
技术词 偶频几何     命中文件数=0    :: 
技术词 定向采样     命中文件数=0    :: 
技术词 弱目标余量  命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/c374.py`（`R_r` 递推 ＋ `32` 层枚举 ＋ `E_{\mathrm{even}}` 过滤 ✓）；`timeout 600` ✓
- **本档有计算**（数值探针，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：仅 **5** 个 `E_{\mathrm{even}}` 点（1 最优 ＋ 4 采样 ✓）⟹ **不构成证明** ✗✓；余量 `2.19 \sim 2.56` 为**观测** ✓，**非定理** ✗✓
- **不得**写成：Bridge A 已闭合 ✗；`\min_\sigma\max_r|O_r| > \tfrac12` 已证 ✗；`H = \varnothing` 已证 ✗
