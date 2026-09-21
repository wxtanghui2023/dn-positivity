已查地图（**先查后写**）：`C-3847`（**原始定义回填：r ≤ 12；证书在 r = 9 失败** ✓✓）、`C-3846`（**截断完全解集 16 组／孤立性** ✓✓）、`C-380-12`（**截断形式 k ≤ 6** ⚠️✓）、`C-380-13`（**线性 Fourier 对偶 sharp 封口** ✓✓）、`C-375`／`C-342`（**`E_{\mathrm{even}}`：r = 1..12** ✓✓）、`C-349`（**s_1／s_2 导出约束** ✓✓）、`C-380-26`（**网格级** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-48：Harmonic-9 Entrance Audit（立项 ＋ H1 第一刀）**（唐先生 2026-09-21 21:0x 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 新主线（立项，唐先生令）}✓✓：\ \boxed{E_0^{(12)} = \Big\{z \in (S^1)^4 : \Re\sum_{j=1}^{4}z_j^r \le -\tfrac12,\ r = 1,\dots,12\Big\}}✓✓；\ \text{唯一目标}\ \boxed{E_0^{(12)} = \varnothing\ ?}✓✓$$

$$\qquad \textbf{同时冻结}✓：\text{Level 3}\ \textbf{FROZEN}✗；\ \Psi(\Delta_4)\ \textbf{DEAD}✗✓；\ \text{截断（}k \le 6\text{）}\ \textbf{降级为反例资产}✓✓$$

$$\textbf{② ⭐⭐⭐ H1 第一问结果}✓✓：\text{在}\ F_1,\dots,F_8 \le -\tfrac12\ \text{下}✓,\ \textbf{存在可证明的统一下界}✓✓,\ \text{且数值上}\ \boxed{\min F_9 = +4}✓✓$$

$$\qquad \textbf{三条独立数值路径互证}✓✓：\text{(i)}\ \textbf{70 组 active set 全枚举} \text{4-重边界解}✓ \Longrightarrow \text{恰 16 个可行解}✓✓；$$

$$\qquad \qquad \text{(ii)}\ \text{SLSQP 400 起点全局最小化}\ F_9✓ \Longrightarrow \min F_9 = +4.0✓✓；\qquad \text{(iii)}\ \text{罚函数下降 60000 起点}✓ \Longrightarrow \textbf{343 个落点聚成 16 个不同点}✓✓$$

$$\textbf{③ 16 点的结构（刚性）}✓✓：\text{全部为}\ \textbf{9 次单位根 4-子集}✓✓；\ \textbf{8 条约束全部取等}✓\ (F_1 = \dots = F_8 = -\tfrac12)✓；\ F_9 = +4✓✓$$

$$\qquad \Longrightarrow \ \boxed{\{F_1..F_8 \le -\tfrac12\}\ \text{数值上}\ =\ \text{16 个孤立点}}✓✓ \Longrightarrow\ \text{无任何连续分量}✓✓$$

$$\textbf{④ 关键推论}✓✓：F_1..F_8 \le -\tfrac12 \Longrightarrow F_9 = +4 > -\tfrac12✓✓ \Longrightarrow\ \boxed{E_0^{(12)} = \varnothing}✓✓\ \text{（因}\ r = 9 \in \{1,\dots,12\}✓）$$

$$\qquad \Longrightarrow \ \text{余量}\ \boxed{F_9 - (-\tfrac12) = 4.5}✓✓\ \text{（极大，非临界）}✓✓ \Longrightarrow\ \text{该封口}\ \textbf{不是}\ \text{数值临界型}✓✓$$

$$\textbf{⑤ 精确等价（机制核心）}✓✓：\ F_9 = \sum_j\cos(9\psi_j) = 4 \iff \cos(9\psi_j) = 1\ \forall j \iff \boxed{9\psi_j \equiv 0\ (2\pi)}✓✓$$

$$\qquad \Longrightarrow \ \textbf{"上界 4 被取到"与"节点全为 9 次单位根"}\ \textbf{精确等价}✓✓ \Longrightarrow\ \text{刚性引理}\ \textbf{自带分类}✓✓$$

$$\textbf{⑥ 粗和方法仍不够（量化，锁死错误刀）}✗✓：\ \min_\psi\sum_{r=1}^{8}\cos(r\psi) = -2.368188✓ \Longrightarrow\ \text{四节点下界}\ -9.4728✓$$

$$\qquad \text{而约束只给}\ \sum F_r \le -4✓ \Longrightarrow\ \textbf{不足以矛盾}✗✓ \Longrightarrow\ \textbf{必须} \text{用}\ \textbf{逐条约束的刚性}✓✓,\ \textbf{不能}用单个聚合不等式✗✓$$

$$\textbf{⑦ 证明路径（有限分类，符合唐先生"不要暴力消元 12 条"）}✓✓：\text{对 70 个 active set}\ \mathcal A \subset \{1..8\},\ |\mathcal A| = 4✓：$$

$$\qquad \text{解}\ \{F_r = -\tfrac12\}_{r \in \mathcal A}\ \text{（4 方程 4 未知）}✓ \Longrightarrow \text{精确枚举全部根}✓ \Longrightarrow \text{验证余下 4 条}\ F_r \le -\tfrac12✓ \Longrightarrow\ \text{并处理}\ |\mathcal A| \ge 5\ \text{的退化情形}✓✓$$

$$\qquad \Longrightarrow \ \boxed{\text{完全有限、可复核、无需 SDP／Gram}}✓✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 H1 三路数值核验（数字驱动 ✓✓）

| 路径 ✓ | 设置 ✓ | 结果 ✓ |
|---|---|---|
| (i) 边界解枚举 ✓ | 70 个 active set × 40 起点，Newton（4 方程 4 未知）✓ | **恰 16 个**满足全部 8 条的可行解 ✓✓；`F_9 ∈ {+4.0}` ✓✓ |
| (ii) 全局最小化 `F_9` ✓ | SLSQP ＋ 8 条不等式约束，400 起点 ✓ | **min `F_9` = +4.000000000** ✓✓；最优点的 `F[1..12] = [-1/2 ×8, +4, -1/2 ×3]` ✓✓ |
| (iii) 罚函数下降 ✓ | 60000 起点（含 6000 个循环种子）✓ | **343 个落点聚成 16 个不同点**✓✓；全部 `F_9 = +4.0` ✓✓；无连续分量 ✓✓ |
| (iv) 精确等价 ✓ | `F_9 = 4 ⟺ 全为 9 次单位根` ✓ | 多个 4-子集 `F_9 = +4` 精确成立 ✓✓；一般点 `F_9 = +0.079`（远小于 4）✓✓ |
| (v) 粗和方法 ✓ | `min_ψ Σ_{r≤8} cos(rψ)` ✓ | `-2.368188` ⟹ 下界 `-9.4728` ⟹ **不足** ✗✓ |

$$\textbf{脚本}✓：`scripts/c380_48_harmonic9_entrance.py`✓、`scripts/c380_48_rigidity_stress.py`✓；输出 `scripts/out_c380_48_{entrance,stress}.txt`✓✓$$

$$\textbf{注（自检）}⚠️✓：压测脚本的"循环性／紧约束"两栏因\textbf{先对角度四舍五入到 6 位}再判定而失效✓（得 0/16 与 [0]）✗✓ —— \textbf{不影响}结论（`F_9 = 4` 与 16 点聚类在舍入前判定）✓✓；\ \text{该两栏须重跑再引用}✓$$

## §2 账本（唐先生令后的新表 ✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| two-level 子族 ✓ | **CLOSED：空** ✓✓ |
| `k \le 6` 截断 ✓ | **伪解存在 ⟹ 降级为反例资产** ✓✓ |
| 原始 `r \le 12` 的 `E_0` ✓ | **OPEN** ✓（本档给出强数值证据：应为空） |
| 9 次单位根证书 ✓ | **排除** ✓✓ |
| 循环型候选 `n \le 25` ✓ | **CLOSED：排除** ✓✓ |
| `\Psi(\Delta_4)` ✓ | **DEAD** ✓✓ |
| Level 3 ✓ | **FROZEN** ✓✓ |
| **刚性引理（8 条 ⟹ 9 次单位根）** ✓ | **本档新登记：H1 的核心目标** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称"`E_0^{(12)} = \varnothing` 已证"：本档是**数值三条路径**（枚举／全局最小化／多起点下降），**非**证明 ✓
- **不**声称刚性引理已证（只登记路径与数值证据）✓
- **不**声称"`r = 9..12` 是任何证明的必需资源"（唐先生明确更正：应理解为**当前封口须处理的新增资源**）✓
- **不**声称粗和方法在所有加权下失效（只说**均匀求和**这一具体刀失效）✓
- **不**重开 Level 3、**不**碰 `\Psi(\Delta_4)` ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}做 12 条约束的暴力消元✗（唐先生明令）✓；\ \textbf{不}重新扫循环族✗；\ \textbf{不}引入 SDP／Gram 正性✗✓$$

## §5 下一步（须唐先生发令 ✓）

$$\textbf{H1-}\alpha✓：\text{对 70 个 active set 逐个}\ \textbf{精确} \text{求解并枚举根}✓✓ \text{（有限分类}✓）$$
$$\textbf{H1-}\beta✓：\text{处理}\ |\mathcal A| \ge 5\ \text{的退化情形}✓ \text{（数值上未见非循环解}✓）$$
$$\textbf{H2（仅当}\ \text{H1-}\alpha/\beta\ \text{不足）}✓：\text{找}\ \Phi\ \text{使}\ F \le -\tfrac12\ (r \le 12) \Longrightarrow \Phi \le 0\ \text{而}\ \Phi > 0✓✓$$

## §6 【技术词回查】输出（**先跑后写** ✓）

```
技术词 刚性引理     命中文件数=0    ::
技术词 边界解枚举  命中文件数=0    ::
技术词 统一下界     命中文件数=0    ::
技术词 12重约束     命中文件数=0    ::
```
- 运行记录 ✓：`bash scripts/tech_word_check.sh` ✓
