已查地图（**先查后写**）：`C-380-24`（**三阶采样可行** ✓✓）、`C-380-23`（**二维全覆盖** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-25：Four-Moment Joint Geometry（注册＋25-A／C／D 核验）**，**有计算（数值采样，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 设定}✓✓：X_j = \cos\phi_j✓；\ Q_1 = S_1✓，\ Q_2 = 2S_2 - 4✓，\ Q_3 = 4S_3 - 3S_1✓，\ Q_4 = 8S_4 - 8S_2 + 4✓✓$$
$$\qquad \Longrightarrow \ E_0\ \text{前四条件}✓✓：\boxed{S_1 \le -\tfrac12✓,\ S_2 \le \tfrac74✓,\ S_3 \le \tfrac{3S_1 - \frac12}{4}✓,\ S_4 \le S_2 - \tfrac{9}{16}}✓✓$$
$$\qquad ⭐ \textbf{新结构}✓✓：\boxed{S_2 - \tfrac{9}{16}}\ \text{同时是}\ S_4\ \text{的上界}✓，\ \text{而}\ S_2\ \text{本身又被上界约束}✓✓ \Longrightarrow \textbf{首次出现二阶与四阶能量的直接耦合}✓✓$$
$$\textbf{② ⭐ 25-A 结果（本档核心）}✓✓：\min_{X_j \in [-1,1]}\max_{1 \le k \le 4}(Q_k + \tfrac12) = \boxed{-0.4662 < 0}✓✓ \Longrightarrow \textbf{四阶可达（采样级）}✓✓$$
$$\qquad \textbf{采样}✓✓：\text{同时满足四条件者}\ 1958／300000✓✓（\textbf{0.65\%}✓） \ —— \ \textbf{从三阶的}\ 2.7\%\ \textbf{降到}\ 0.65\%✓✓（\textbf{明显变稀}✓）$$
$$\qquad \textbf{最优样本}✓✓：X = (-0.834, -0.773, 0.298, 0.342)✓；\ S = (-0.966, 1.498, -0.974, 0.861)✓；\ Q = (-0.966, -1.005, -0.998, -1.095)✓✓$$
$$\qquad \Longrightarrow \ \boxed{4\text{-moment}\ \textbf{INSUFFICIENT／sampling-level feasible}}✓✓$$
$$\textbf{③ 账本措辞降级（采纳）}✓✓：\text{记}\ \boxed{INSUFFICIENT／sampling-level feasible}✓✓，\ \textbf{不}写绝对定理✗✓（\text{「至少四阶」为}\ \textbf{采样级排除}✓✓）$$
$$\textbf{④ 25-C sanity check}✓✓：S_4 \ge \tfrac{S_2^2}{4}✓（\text{Cauchy–Schwarz}✓） ＋ S_4 \le S_2 - \tfrac{9}{16}✓ \Longrightarrow \tfrac{S_2^2}{4} \le S_2 - \tfrac{9}{16}✓✓$$
$$\qquad \Longrightarrow \ \boxed{S_2^2 - 4S_2 + \tfrac94 \le 0}✓✓ \Longrightarrow \ \boxed{2 - \tfrac{\sqrt7}{2} \le S_2 \le 2 + \tfrac{\sqrt7}{2}}✓✓（\approx 0.6771 \sim 3.3229✓）$$
$$\qquad \qquad ⚠️ \textbf{勘误}✗✓：\text{唐先生写的}\ 2/3\ \text{与}\ 10/3\ \text{是}\ \textbf{四舍近似}✓✓，\ \textbf{精确值}\ \text{为}\ 2 \mp \tfrac{\sqrt7}{2}✓✓$$
$$\qquad \text{合并}\ S_2 \le \tfrac74✓ \Longrightarrow \ \boxed{0.677 \le S_2 \le 1.75}✓✓ \Longrightarrow \ \textbf{最粗的}\ S_2\text{-}S_4\ \text{inequality}\ \textbf{仍不杀} \text{四阶可行性}✓✓$$
$$\qquad \Longrightarrow \ \text{与}\ C\text{-}380\text{-}23／24\ \text{的经验一致}✓✓：\textbf{不能期待}一个漂亮的低阶二元不等式突然解决整个问题✗✓$$
$$\textbf{⑤ ⭐⭐ 25-D 观测（本档最有价值的线索）}✓✓：\text{最优候选}\ m = -0.2415✓，\ \mu_2 = 0.3161✓，\ \mu_3 = -0.0004✓✓（\textbf{几乎为零}✓），\ \mu_4 = 0.1008✓✓$$
$$\qquad \textbf{检验}\ \mu_4 \ge \mu_2^2✓：0.1008\ \text{vs}\ 0.0999✓ \Longrightarrow \text{比值}\ \boxed{1.009}✓✓ \ —— \ \textbf{极度贴近一般测度下界}✓✓$$
$$\qquad \mu_4 \le \mu_2\ \text{成立}✓（\text{因}\ |Y| \le 1✓，\ Y \in [-0.592, +0.583]✓）✓✓$$
$$\qquad ⭐ \Longrightarrow \ \textbf{线索}✓✓：\mu_4 = \mu_2^2\ \text{的等号由}\ \text{Cauchy–Schwarz}\ \text{「全部}\ |Y_j|\ \text{相等」}\ \text{时取到}✓✓ \Longrightarrow \textbf{最优点处}\ |Y_j|\ \textbf{近乎相等}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{四点等权 sharpening（若存在）在此处}\ \textbf{近乎饱和}✓✓ \Longrightarrow \ \text{候选方向}\ \boxed{\mu_4 \ge \mu_2^2 + \text{四原子修正项}}✓✓$$
$$\textbf{⑥ 25-B}✓✓：\text{四阶真正应该审计的}\ \textbf{不是}\ \text{Newton identity}✗✓，\ \text{而是}\ \boxed{S_4\ \text{vs}\ S_1, S_2}\ \text{的}\ \textbf{四点等权约束}✓✓$$
$$\qquad \textbf{须过}\ P2′✓✓：\text{证明它真正使用「4 atoms} + \text{equal weights」}✓✓；\ \text{若它对所有}\ \mu \in \mathcal P([-1,1])\ \text{都成立}✗ \Longrightarrow \textbf{仍只是一般 moment geometry}✗✓$$
$$\textbf{⑦ 判死／晋级纪律（采纳）}✓✓：$$
$$\qquad \text{四阶采样找到明显可行点} \Longrightarrow \boxed{4\text{-moment INSUFFICIENT}}✓✓（\textbf{本档命中}✓）；\ \text{四阶只在极窄边界附近} \Longrightarrow \text{局部精化，}\textbf{不}宣称空✗✓$$
$$\qquad \text{四阶采样完全不可达} \Longrightarrow \boxed{numerical\ candidate}✓ \Longrightarrow \text{寻找解析证书}✓；\ \text{找到一般 measure inequality} \Longrightarrow \textbf{降级}✗✓$$
$$\qquad \text{找到正线性组合} \Longrightarrow \textbf{退回}\ C\text{-}380\text{-}13✗✓；\ \text{找到真正}\ \textbf{4-atomic／equal-weight nonlinear compatibility} \Longrightarrow \boxed{\textbf{正式候选 obstruction}}✓✓$$
$$\textbf{⑧ 路线}✓✓：\boxed{2D \times \text{FAIL} \to 3D \times \text{sampling-feasible} \to \textbf{4D NEXT}}✓✓$$
$$\qquad \textbf{盯住}✓✓：\ S_2 \leftrightarrow S_4\ \text{与四原子等权结构的}\ \textbf{耦合}✓✓，\ \textbf{而不是}再生成一个\ F_4\ \text{型恒等式}✗✓$$

## §1 数值记录（✓✓）

$$\textbf{采样}✓：3 \times 10^5\ \text{点}✓；\ \min\max_{k \le 4} = -0.466191✓✓；\ \text{四条件同时}\ 1958／300000（0.65\%）✓✓$$
$$\textbf{单独极小}✓：\min Q_1 = -3.8667✓（\le -\tfrac12\ \text{占}\ 34.0\%✓）；\ \min Q_2 = -3.9925✓（75.9\%✓）；\ \min Q_3 = -3.9660✓（36.3\%✓）；\ \min Q_4 = -3.9916✓（44.0\%✓）$$
$$\textbf{可行例}✓✓：X = (-0.879, 0.404, -0.667, 0.123)✓，\ S = (-1.019, 1.396, -0.909, 0.822)✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3` ✓ | **DERIVED／method-family CLOSED** ✓✓ |
| all 2-moment ✓ | **INSUFFICIENT（覆盖级）** ✗✓ |
| 3-moment ✓ | **INSUFFICIENT／sampling-level feasible** ✗✓ |
| **4-moment** ✓ | **本档：INSUFFICIENT／sampling-level feasible（0.65\%）** ✗✓ |
| `\mu_4 \approx \mu_2^2` 线索 ✓ | **已登记（新方向）** ✓✓ |
| 5-moment／解析证书 ✓ | **NEXT（视线索）** ✓✓ |
| `\mathcal F_0` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{四阶不可达已证}✗✓（\textbf{采样级}✓）；\ \text{「至少五阶」为定理}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{有数值采样}✓（\textbf{非}证明✗）；\ \text{全部负结果}\ \textbf{均为采样级}✓✓；\ \mu_4 \approx \mu_2^2\ \text{为}\ \textbf{单点观测}✓✓（\textbf{非}定理✗）$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}做六维暴力✗；\textbf{不}造\ F_4\ \text{型恒等式}✗；\textbf{不}碰\ p_5, p_6✗；\textbf{不}把\ \text{一般 measure inequality}\ \text{当 obstruction}✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（数值采样，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 四阶联合几何 命中文件数=0    :: 
技术词 等号接近线索 命中文件数=0    :: 
技术词 采样级可行  命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（3e5 采样 ＋ 四阶计数 ＋ sympy 解二次不等式 ＋ 中心矩 ✓）
