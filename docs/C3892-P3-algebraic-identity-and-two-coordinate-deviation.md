已查地图（**先查后写**）：`C3891`（**T1 否定；T2 奇偶分拆；T3 `P_3` 坐标** ✓✓）、`C3846`（**精确仿射分解** ✓✓）、`C-380-26`（**`\Delta_4 = \mathrm{Var}(Y^2) \ge 0`；two-level 族** ✓✓）、`C-3862`（**活跃集** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-98：C-3892 —— `P_3` 代数身份（分解恒等式）＋ 双坐标偏离刻画（T3 结构）**（唐先生 2026-09-22 09:04 问）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 唐先生之问}✓✓：P_3\ \text{的代数定义是什么？"}\ P_3 > 0\ \text{方向一阶损失"}\ \text{是否覆盖偏离 two-level 的}\ \textbf{全部} \text{自由度？}✓✓$$

$$\textbf{② ⭐ }P_3\ \textbf{的代数身份（本档新引理}✓✓**）：Y_j := X_j - m✓,\ \sum_jY_j = 0✓,\ P_3 = \sum_jY_j^3✓✓$$

$$\qquad \textbf{分解恒等式}✓✓（三变量}\ a^3+b^3+c^3 = 3abc\ \text{的四变量版}✓）：\qquad \boxed{P_3 = 3(Y_i+Y_j)(Y_i+Y_k)(Y_i+Y_l)}✓✓\ \text{（任一固定}\ i\ \text{皆成立}✓）$$

$$\qquad \Longrightarrow \boxed{P_3 = 0 \iff \exists\ \text{一对}\ Y_i = -Y_j}✓✓ \Longrightarrow \textbf{几何含义}✓：\boxed{\text{存在关于}\ m\ \text{对称的点对}}✓✓$$

$$\qquad \text{（two-level 族}\ \textbf{落在其中}✗:\ Y = (a,a,-a,-a)\ \text{有}\ Y_1 = -Y_3✓,\ \text{但}\ P_3 = 0\ \text{的集合}\ \textbf{更大}✗✓）$$

$$\textbf{③ 回答（}\textbf{部分覆盖}✗✓**）：Q_3 - q_3 = 4P_3\ \text{的一阶损失}\ \textbf{只惩罚"对称点对消失"这一模式}✗✓$$

$$\qquad \textbf{不覆盖}✗：\text{"对称点对仍在、但构型不是 two-level"的偏离}✓✓ \Longrightarrow P_3\ \textbf{单独不是完整坐标}✗✓$$

$$\textbf{④ ⭐ 补上}\ \Delta_4\ \textbf{后恰好完整（双坐标刻画，本档手证}✓✓**）：\Delta_4 = \mathrm{Var}(Y^2) \ge 0✓,\ \Delta_4 = 0 \iff |Y_j|\ \text{全相等}✓✓$$

$$\qquad \text{在固定}\ (m,\ \sum Y^2 = 4a^2)\ \text{的球面上}✓：P_3 = 0 \Longrightarrow \exists\ \text{配对}\ Y_1 = -Y_3✓,\ Y_2 = -Y_4✓（\text{重排后}✓）$$

$$\qquad \qquad \Delta_4 = \tfrac{P_2^2}{16} - e_4 = 0✓,\ e_4 = Y_1Y_2Y_3Y_4 = Y_1^2Y_3^2✓ \Longrightarrow \text{置}\ u := Y_1^2,\ v := Y_3^2✓：u + v = 2a^2✓,\ uv = a^4✓$$

$$\qquad \qquad \Longrightarrow (u-v)^2 = (u+v)^2 - 4uv = 4a^4 - 4a^4 = 0✓ \Longrightarrow u = v = a^2✓✓ \Longrightarrow \boxed{\text{即 two-level（至多差符号型）}}✓✓$$

$$\qquad \Longrightarrow \boxed{(P_3,\ \Delta_4)\ \text{为两个独立坐标，且}\ \text{偏离 two-level} \iff P_3 \ne 0 \vee \Delta_4 \ne 0}✓✓ \Longrightarrow \textbf{正是唐先生预测的"至少两个独立坐标"}✓✓$$

$$\textbf{⑤ 惩罚结构（T3 的真实形态}✓✓**）：$$

$$\qquad \textbf{P_3 方向}✓：\textbf{一阶}损失\ 4P_3✓（\text{来自}\ \textbf{活跃约束}\ Q_3✓） \Longrightarrow \text{可用一阶论证}✓✓$$

$$\qquad \textbf{\Delta_4 方向}✗✓：\text{一阶只现于}\ Q_4\ (+32\Delta_4✓)\ \text{与}\ Q_5\ (-|320m|\Delta_4✓,\ \textbf{有利}✗) \Longrightarrow \textbf{须二阶处理}✗\ \text{或换另一条活跃约束}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{T3 结构}＝\text{一个一阶方向}\ (P_3)＋\text{一个需二阶的方向}\ (\Delta_4)}✓✓$$

$$\textbf{⑥ 数值核验（本档}✓✓**）：\text{分解恒等式对}\ i = 1,2,3,4\ \textbf{全部成立}✓✓（sympy 核验}✓）；\ \text{且}\ (u+v)^2 - 4uv = 4a^4 - 4a^4 = 0✓✓$$

$$\textbf{⑦ 立即可检验的下一点}✓✓：\text{在}\ \textbf{真实极值点} \text{处，}\ Q_3\ \text{与}\ Q_4\ \text{哪些}\ \textbf{活跃}✓\ \text{（须区分}\ C\text{-}3846\ \text{截断系统的}\ Q_k\ \text{与}\ C\text{-}3861\ \text{的}\ F_{2q}\ \text{活跃集}✗✓,\ \textbf{不得混用}✗）$$

## §1 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `P_3` 分解恒等式 ✓ | **CLOSED（sympy 全验证）** ✓✓ |
| `P_3 = 0 \iff` 存在对称点对 ✓ | **CLOSED** ✓✓ |
| 单一 `P_3` 覆盖全部自由度 ✓ | **否（只覆盖一类模式）** ✗✓ |
| `(P_3, \Delta_4)` 双坐标完整性 ✓ | **CLOSED（手证 ＋ 核验）** ✓✓ |
| 惩罚结构分类 ✓ | **`P_3` 一阶／`\Delta_4` 二阶** ✓✓ |
| 真实极值点活跃集 ✓ | **待查（含索引警示）** ⚠️ |

## §2 边界（不得声称 ✗✓）

- **不**声称 T3 稳定性已成立（只**分解**出方向）✓
- **不**声称 `(P_3,\Delta_4)` 在**任意** `(m,P_2)` 下完整（本档只处理**固定** `(m, \sum Y^2)` 的球面）✓✓
- **不**混用 `C-3846` 的 `Q_k` 与 `C-3861` 的 `F_{2q}` 活跃集 ✓
- **不**声称 `\Delta_4` 方向已封 ✓

## §3 本档**不**做的事 ✓✓

$$\textbf{不}修数学（除恒等式与手证）✗；\ \textbf{不}开 T2／T3 计算✗✓$$

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 对称点对判据 命中文件数=0    :: 
技术词 双坐标刻画  命中文件数=0    :: 
技术词 一阶二阶分支 命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{① 活跃集核对}✓✓：\text{在真实极值点确定}\ Q_3／Q_4\ \text{的活跃性}✓（\textbf{索引警示}✓），\ \text{据此判定}\ P_3\ \text{一阶论证是否可闭}✓✓$$
$$\textbf{② T2 主攻}✓：\text{用}\ \textbf{6 项稀疏性 ＋ 奇偶分拆} \text{证根集成对}✓✓$$
$$\textbf{③ T3}✓：\text{对}\ \Delta_4\ \text{方向做}\ \textbf{二阶} \text{展开，求"是否有正惩罚"}✓✓$$
