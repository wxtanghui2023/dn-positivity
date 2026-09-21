已查地图（**先查后写**）：`C-380-21B`（**`F_3^(B)` 形式闭合** ✓✓）、`C-380-13`（**Fourier-dual CLOSED sharp** ✓✓）、`C-380-12`（**`E_0` 四节点问题** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-22：`E_0` Multi-Moment Feasibility Pivot（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 措辞精化（采纳，分两层）}✓✓：\textbf{Algebraic level}✓：F_3^{(A)} \equiv 0✓，\ F_3^{(B)} \equiv 0✓（\text{各自在自己的四单位节点模型中成立}✓✓）$$
$$\qquad \textbf{E0 level}✓：\text{若 exact lifted}\ R_0\ \text{是}\ x \mapsto y \mapsto \theta \mapsto w_j = e^{2i\theta_j}✓ \Longrightarrow R_0 \models F_3^{(B)} = 0✓✓$$
$$\qquad \qquad \textbf{但} \text{因档案}\ \textbf{并没有把}\ R_0\ \text{写成单独的 formal object}✗✓，\ \text{账本最好写成}✓✓：$$
$$\qquad \qquad \boxed{\text{F3 is a derived identity of the exact four-unit-node lift; hence it supplies no independent E0 cut}}✓✓$$
$$\qquad \qquad \textbf{而不要}过度声称已经证明了某个\ \textbf{尚未形式定义的 projected}\ R_0\ \text{满足它}✗✓（\textbf{该区别不影响结论方向}✓✓）$$
$$\textbf{② F3 分支正式封口}✓✓：\forall(w_1, \dots, w_4) \in (S^1)^4✓，\ q_k = \sum_jw_j^k✓ \Longrightarrow 6e_4\overline{q_1} = 2q_3 + q_1^3 - 3q_1q_2✓，\ |e_4| = 1✓ \Longrightarrow \boxed{F_3^{(B)} \equiv 0}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不是}「某些 E0 点满足的额外方程」✗✓，\ \text{而是}\ \textbf{整个四单位节点母空间上的恒等式}✓✓ \Longrightarrow \ \boxed{\text{F3 nonlinear-identity branch} = \textbf{DERIVED／REDUNDANT}}✓✓$$
$$\qquad \qquad \textbf{不需}再做任何优化或采样✗✓$$
$$\textbf{③ ⭐ E0 的独立问题}✓✓：\ \boxed{\mathcal F_0 = \{(w_1, \dots, w_4) \in (S^1)^4 : \Re q_k \le -\tfrac12,\ k = 1, \dots, 6\}}✓✓，\ \textbf{目标}\ \boxed{\mathcal F_0 = \varnothing}✓✓$$
$$\textbf{④ ⭐ 过滤器（关键）}✓✓：\text{任何}\ \textbf{单一非负线性组合}\ \sum_{k=1}^{6}\lambda_k\big(\Re q_k + \tfrac12\big)✓（\lambda_k \ge 0✓）\ \textbf{本质} \text{上仍是}\ \textbf{Fourier-dual certificate}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\text{single positive linear combination} \Rightarrow C\text{-}380\text{-}13}✓✓ \ \textbf{已 CLOSED}✓✓ \Longrightarrow \textbf{不能}下一步又去寻找一组漂亮的\ \lambda_k✗✓$$
$$\textbf{⑤ ⭐⭐ } C\text{-}380\text{-}22\ \text{核心问题（问题类型改变）}✓✓：\textbf{不是}「还能不能找到一个 nonlinear identity？」✗✓，\ \textbf{而是}✓✓：$$
$$\qquad \boxed{\text{六个同时成立的 moment inequalities，是否存在一个真正的「多约束相互作用」证书，而不是六个线性 Fourier 约束的加权重述}？}✓✓$$
$$\qquad \textbf{形式}✓✓：\ \bigcap_{k=1}^{6}\{\Re q_k \le -\tfrac12\} \cap (S^1)^4 = \varnothing✓，\ \textbf{但证书必须利用} \text{至少两个 moment 之间的}\ \textbf{非线性兼容关系}✓✓$$
$$\textbf{⑥ ⭐ M1–M5 硬反重包装过滤器（采纳）}✓✓：$$
$$\qquad \textbf{M1 genuinely joint}✓✓：\textbf{不能}只使用一个\ q_k✗✓；\ \text{必须真正利用}\ (q_r, q_s)\ \text{之间由四节点结构产生的兼容性}✓✓$$
$$\qquad \textbf{M2 non-Fourier-dual}✓✓：\textbf{不能}最终化成\ \sum_k\lambda_k\Re q_k + C \ge 0✓（\lambda_k \ge 0✓）；\ \textbf{否则立即} \rightarrow \boxed{C\text{-}380\text{-}13\ \text{CLOSED／duplicate}}✗✓$$
$$\qquad \textbf{M3 exact unit-circle mechanism}✓✓：\text{必须利用}\ |w_j| = 1✓ \ \text{与}\ \textbf{四节点有限秩／代数关系}✓✓，\ \textbf{而} \text{不是只利用}\ \Re q_k \le -\tfrac12✗✓$$
$$\qquad \textbf{M4 contradiction at the feasible-set level}✓✓：\text{最终必须推出}\ \mathcal F_0 = \varnothing✓ \ \text{或}\ \textbf{严格缩小}✓✓，\ \textbf{而} \text{不是仅仅得到另一个恒等式}✗✓$$
$$\qquad \textbf{M5 no identity farming}✓✓：\textbf{不允许}把\ F_3 = 0\ \text{换成}\ F_4 = 0, F_5 = 0, \dots\ \text{再重复一次本轮}✗✓$$
$$\textbf{⑦ ⭐ 最值得先审计的对象（联合 moment geometry）}✓✓：\ Q = (\Re q_1, \dots, \Re q_6)✓；\ E_0\ \text{要求}\ Q \in (-\infty, -\tfrac12]^6✓✓$$
$$\qquad \Longrightarrow \ \boxed{Q\big((S^1)^4\big) \cap (-\infty, -\tfrac12]^6 \stackrel{?}{=} \varnothing}✓✓ \ \Longrightarrow \ \textbf{真正的新接口}✓✓：\ \boxed{\text{image geometry of four-node power sums}}✓✓$$
$$\qquad \qquad \textbf{而} \text{不是单个 Fourier functional}✗✓；\ \textbf{若最后只得到某个支撑超平面}\ \lambda \cdot Q \ge -\tfrac12\sum\lambda_k✗ \Longrightarrow \textbf{又回到}\ C\text{-}380\text{-}13✗✓$$
$$\qquad \textbf{真正有价值}✓✓：\text{出现}\ G(Q_1, \dots, Q_6) \ge 0✓ \ \textbf{且}\ G\ \textbf{不可化为一个单独的线性 Fourier functional}✓✓，\ \text{并且}\ Q_k \le -\tfrac12✓\ \text{使}\ G < 0✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{这才是一个真正不同的 obstruction 类型}✓✓$$
$$\textbf{⑧ 路线}✓✓：\ \boxed{\textbf{下一阶段} = E_0\ \text{feasibility 本身}}✓✓ \ —— \ \textbf{不是}再开一条「代数恒等式」支线✗✓$$

## §1 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED sharp** ✓✓ |
| `F_3^{(A)}` ✓ | **DERIVED identity** ✓✓ |
| `F_3^{(B)}` ✓ | **DERIVED identity／method-family CLOSED** ✓✓ |
| 坐标冲突 ✓ | **CLOSED** ✓✓ |
| A2 objective ✓ | **CLOSED** ✓✓ |
| `E_0` branch symmetry ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}19` R3 ✓ | **永久不执行于 `F_3`** ✗✓ |
| `F_4, p_5, p_6` ✓ | **SEALED** ✗✓ |
| 单一 Fourier-dual certificate ✓ | **CLOSED via `C\text{-}380\text{-}13`** ✓✓ |
| `E_0` feasibility ✓ | **OPEN** ✓ |
| **Multi-moment interaction** ✓ | **NEXT** ✓✓ |

## §2 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{存在多矩证书}✗；\ \text{Bridge A 已闭合}✗✓；\ R_0\ \text{已形式定义}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ M1–M5\ \textbf{均为门槛}✓✓；\ \text{新接口}\ \textbf{未审计}✗✓$$

## §3 本档**不**做的事（✓✓）

$$\textbf{不}寻找\ \lambda_k✗（\text{已 CLOSED}✓）；\textbf{不}开\ F_4／F_5✗；\textbf{不}做数值搜索／优化✗✓$$

## §4 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 纪律（✓✓）

$$\textbf{第一道硬过滤器}✓✓：\ \boxed{\text{若候选最终只是正系数线性组合，就立即退回}\ C\text{-}380\text{-}13}✓✓$$
$$\textbf{符合路线}✓✓：\text{独立问题} \to \text{新接口} \to \text{RH relevance}✓✓，\ \textbf{而不是} \text{继续在}\ F_k\ \text{身上堆代数资产}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 多矩联合几何 命中文件数=0    :: 
技术词 反重包装过滤器 命中文件数=0    :: 
技术词 幂和像几何  命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh`✓
