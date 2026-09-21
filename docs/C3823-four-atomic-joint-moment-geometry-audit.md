已查地图（**先查后写**）：`C-380-22`（**多矩 pivot ＋ M1–M5** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）、`C-380-12`（**`E_0` 四节点问题** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-23：Four-Atomic Joint Moment Geometry Audit（注册＋23-A 核验）**，**有计算（数值采样，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 设定}✓✓：Q_k = \Re q_k = \sum_{j=1}^{4}\cos(k\phi_j)✓，\ w_j = e^{i\phi_j}✓；\ E_0\ \text{要求}\ Q_1, \dots, Q_6 \le -\tfrac12✓✓$$
$$\qquad \text{等价形式}✓✓：X_j = \cos\phi_j✓，\ Q_k = \sum_{j=1}^4T_k(X_j)✓✓$$
$$\textbf{② ⭐ 23-A 结果（本档第一个发现）}✓✓：\mathcal P_{r,s} = \{(Q_r, Q_s)\}✓ \ \textbf{全部} 15\ \text{组二维投影} \ \textbf{都可达} \text{目标象限}✓✓$$
$$\qquad \textbf{数值}✓✓：\min\max(Q_r + \tfrac12, Q_s + \tfrac12)\ \text{对一切}\ (r, s)\ \textbf{均} < 0✓✓（\text{幅度}\ -1.48 \sim -3.42✓）$$
$$\qquad \Longrightarrow \ \boxed{\textbf{二维投影不给任何 obstruction}}✗✓ \Longrightarrow ⭐ \textbf{有价值的负结果}✓✓：\ \boxed{\text{obstruction 必须是}\ \textbf{至少三／四阶联合的}}✓✓$$
$$\textbf{③ 六维同时（采样）}✓✓：4 \times 10^5\ \text{点}✓ \Longrightarrow \min\max_k(Q_k + \tfrac12) = \boxed{+0.0750 > 0}✓✓$$
$$\qquad \Longrightarrow \ \textbf{未发现} \text{同时满足六条件的配置}✓（\textbf{仅采样，非证明}✗✓）；\ \textbf{且} \text{极小值}\ \textbf{非常接近}\ 0✓ \Longrightarrow \textbf{边界很近}✓✓（\text{问题「几乎可行」}✓）$$
$$\qquad \Longrightarrow \ \text{结构}\ \textbf{精细}✓✓ \ —— \ \text{与}\ F_0 = \varnothing\ \text{相容}✓，\ \textbf{但不构成证明}✗✓$$
$$\textbf{④ 23-B 结构基线}✓✓：Q_1 = \sum_jX_j✓；\ Q_2 = 2\sum_jX_j^2 - 4✓✓ \Longrightarrow \text{Cauchy–Schwarz}\ \sum_jX_j^2 \ge \frac{(\sum_jX_j)^2}{4}✓$$
$$\qquad \Longrightarrow \ \boxed{Q_2 \ge \tfrac12Q_1^2 - 4}✓✓ \ —— \ \textbf{真正的非线性 moment 关系}✓✓，\ \textbf{但} \text{显然不足以排除}\ Q_1, Q_2 \le -\tfrac12✗✓$$
$$\qquad \Longrightarrow \ \text{作}\ \textbf{结构基线}✓✓，\ \textbf{不}作候选 obstruction✗✓$$
$$\textbf{⑤ ⭐ 23-C 新接口}✓✓：Q_k = \sum_jT_k(X_j)✓ \Longrightarrow \text{六条件} \iff \textbf{四点等权经验测度}\ \mu = \tfrac14\sum_{j=1}^4\delta_{X_j}✓ \ \text{满足}\ \boxed{\int T_k\,d\mu \le -\tfrac18,\quad k = 1, \dots, 6}✓✓$$
$$\qquad \Longrightarrow \ \textbf{新接口}\ \boxed{[-1,1]\ \text{上的四原子概率测度}}✓✓ \ —— \ \textbf{与}\ C\text{-}380\text{-}13\ \text{的「找一个正三角多项式」}\ \textbf{不是同一对象}✓✓$$
$$\textbf{⑥ ⭐ 23-D 防测度松弛偷换（关键）}✓✓：\textbf{必须分别记录}✓✓：\ \mathcal M_4 = \{\tfrac14\sum_{j=1}^4\delta_{X_j}\}✓ \ \text{与}\ \mathcal P([-1,1])✓（\text{任意概率测度}✓）$$
$$\qquad \textbf{若证松弛版空}✓ \Longrightarrow \text{当然足够强}✓✓；\ \textbf{但若} \text{松弛版有解而四原子等权没有}✓ \Longrightarrow \ \textbf{真正的 obstruction 必须利用}\ \boxed{\text{exactly 4 atoms} + \text{equal weights}}✓✓$$
$$\qquad \Longrightarrow \ \textbf{这恰好符合}「mechanism genuinely changes」✓✓$$
$$\textbf{⑦ P1–P5 硬验收（采纳）}✓✓：\textbf{P1}✓：\text{构造至少一个真正的联合关系}\ G(Q_r, Q_s) \ge 0✓（\text{或更高维}✓）；\ \textbf{P2}✓：\text{证明它来自}\ \textbf{四单位节点／四原子结构}✓✓，\ \textbf{而非} \text{仅来自某个正 Fourier polynomial}✗✓$$
$$\qquad \textbf{P3}✓：\text{证明}\ Q_k \le -\tfrac12\ \text{使}\ G < 0✓✓；\ \textbf{P4}✓：\text{反重包装}\ G \not\equiv C + \sum_k\lambda_kQ_k✓（\lambda_k \ge 0✓）；$$
$$\qquad \textbf{P5}✓：\text{若最终只得到}\ \text{① 一个恒等式；② 一个普通 moment inequality；③ 一个正线性支撑面；④ 一个放宽后的概率测度结果}\✓ \Longrightarrow \ \textbf{都}\ \textbf{不升 obstruction}✗✓$$
$$\textbf{⑧ 优先审计顺序}✓✓：\text{先}\ (Q_1, Q_2)✓、\ (Q_1, Q_3)✓、\ (Q_2, Q_4)✓、\ (Q_1, Q_2, Q_3)✓ \ —— \ \textbf{不}直接上六维数值优化✗✓$$

## §1 数值记录（✓✓）

$$\textbf{范围}✓（4 \times 10^5\ \text{采样}）✓：Q_1 \in [-3.838, +3.760]✓；\ Q_2 \in [-3.991, +3.647]✓；\ Q_3 \in [-3.988, +3.976]✓；\ Q_4 \in [-3.990, +3.962]✓；\ Q_5 \in [-3.969, +3.997]✓；\ Q_6 \in [-3.991, +3.980]✓✓$$
$$\textbf{15 组二维}✓✓：\text{全部}\ \min\max(Q_r + \tfrac12, Q_s + \tfrac12) < 0✓✓（\text{如}\ (1,2)：-1.4917✓；\ (2,6)：-3.4153✓；\ (5,6)：-3.2868✓）$$
$$\textbf{六维}✓✓：\min\max_k(Q_k + \tfrac12) = +0.0750✓✓ \Longrightarrow \textbf{采样未发现可行点}✓（\textbf{非}证明✗）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3` 支线 ✓ | **DERIVED／method-family CLOSED** ✓✓ |
| 二维投影 ✓ | **本档：全部可达 ⟹ 二维不足** ✗✓ |
| 三／四阶联合 ✓ | **NEXT（优先 `(Q_1,Q_2,Q_3)`）** ✓✓ |
| `\mathcal M_4` vs `\mathcal P([-1,1])` ✓ | **须分离（23-D）** ✓✓ |
| `\mathcal F_0` ✓ | **OPEN** ✓ |
| `F_4, p_5, p_6` ✓ | **SEALED** ✗✓ |
| 单一 Fourier certificate ✓ | **CLOSED via `C\text{-}380\text{-}13`** ✓✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{六维不可行已证}✗✓（\textbf{仅采样}✓）；\ \text{存在联合关系}\ G✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{有数值采样}✓（\textbf{非}证明✗）；\ 23\text{-A}\ \text{为}\ \textbf{负结果}✓✓；\ 23\text{-B/C/D}\ \textbf{均为结构登记}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}做六维全局优化✗；\textbf{不}碰\ F_4／p_5, p_6✗；\textbf{不}碰单一 Fourier certificate✗；\textbf{不}把测度松弛当结论✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（数值采样，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 四原子联合几何 命中文件数=0    :: 
技术词 二维投影负结果 命中文件数=0    :: 
技术词 等权测度约束 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（4e5 采样 × 15 组二维 ＋ 六维 ✓；手写 `T_k` 递推 ✓）
