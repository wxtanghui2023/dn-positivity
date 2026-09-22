已查地图（**先查后写**）：`C3894`（**`T3-PASS / LOCAL-RIGIDITY`；单约束二阶证书** ✓✓）、`C3892`（**`(P_3,\Delta_4)` 双坐标** ✓✓）、`C3891`（**`P(c)`／`P'`；6 项稀疏性 ＋ 奇偶分拆** ✓✓）、`C3889`（**四轨架构；M0–M5** ✓✓）、`C3876`（**远区 OPEN** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-103：C-3895 —— T2 根集成对结构（登记；一般 two-level 候选点的 KKT/root-pairing）**（唐先生 2026-09-22 09:38 令）
D1: 0
FREEZE-ACK: 本档即冻结审计（**登记档；本轮不做证明**）

---

## §0 结论（七条 ✓✓）

$$\textbf{① 唐先生令}✓✓：\text{本刀转向}\ \textbf{T2}✓：\textbf{一般 two-level 候选点} \text{的}\ \textbf{KKT／root-pairing} \text{结构}✓✓;\ \textbf{保留}\ C\text{-}3894\ \text{为}\ \textbf{全局稳定性证明的局部刚性砖块}✓✓$$

$$\qquad ⚠️ \textbf{不再} \text{在该局部点继续榨 T3}✗（C-3894 已把此点能提供的信息拿完}✓✓）$$

$$\textbf{② 目标引理（本档登记，精确形式}✓✓**）：$$

$$\qquad \text{设极值构型的支撑为}\ \{c_j\}_{j=1}^4✓;\ \text{消去多项式}\ Q(c) := \prod_{j=1}^4(c - c_j)✓（\text{首一、次数 4}✓）$$

$$\qquad \boxed{\textbf{ROOT-PAIRING 引理（目标）}✓：\text{极值构型}\ \Longrightarrow Q(c) = \left[(c-m)^2 - a^2\right]^2}✓✓$$

$$\qquad \text{理由}✓：\text{two-level} \iff \text{支撑为}\ \{m+a,\ m+a,\ m-a,\ m-a\}✓ \iff \textbf{每个值重数}\ \ge 2✓ \iff \boxed{Q\ \text{是完全平方}}✓✓$$

$$\qquad \text{即}\ \boxed{Q = R^2\ (R\ \text{二次})}✓ \iff \text{全部根重数为偶}, \text{在 4 点 2 值情形} \Longrightarrow \text{重数}\ (2,2)✓✓$$

$$\textbf{③ 与 stationarity 的接口}✓✓：C\text{-}3891\ \text{已得}\ P(c) = -\omega_{13}T_{13}(c) + \omega_{19}T_{19}(c) + \sum_{q \in \mathcal A}\lambda_qT_{2q}(c)✓,\ \text{支撑点满足}\ P'(c_j) = 0✓✓$$

$$\qquad \Longrightarrow \boxed{Q \mid P'}✓（\text{次数}\ \deg P' \le 35✓） \Longrightarrow \text{两条路}✓：$$

$$\qquad \qquad \textbf{路 A}✓：\text{证}\ Q = R^2\ \text{由 KKT 系统}\ \textbf{强制}✓（\text{代数：把}\ Q \mid P'\ \text{与其余活跃条件联立}✓）；$$
$$\qquad \qquad \textbf{路 B}✓：\text{用}\ \textbf{6 项稀疏性 ＋ 奇偶分拆} \text{证明}\ P'\ \text{的根}\ \textbf{成对}✓（\text{即}\ P'\ \text{的结构迫使偶重数}✓）$$

$$\textbf{④ 奇偶分拆的可用形式（C-3891 已立}✓✓**）：\text{偶频约束只依赖}\ x_j = c_j^2✓ \Longrightarrow \textbf{偶频可行集对}\ c_j \to \pm c_j\ \text{与置换不变}✓;\ \text{而}\ F_{13}, F_{19}\ \text{为奇}✓ \Longrightarrow \textbf{符号信息全由}\ \sigma\ \text{承担}✓✓$$

$$\qquad \Longrightarrow \text{问题分解为}\ \boxed{\text{"}x\text{-多重集"} \times \text{"符号型"}}✓✓ \Longrightarrow \text{root-pairing}\ \text{更可能由}\ \textbf{偶部结构} \text{给出}✓✓$$

$$\textbf{⑤ 交付里程碑对应}✓✓：\text{成功即}\ \boxed{M1\ \text{里程碑}}✓（\text{支撑} \le 2✓）；\ \text{退一步亦可得}\ \deg \le 3\ \text{型中间结果}✓✓$$

$$\textbf{⑥ 与 C-3894 的关系}✓✓：C\text{-}3894\ \text{是}\ \textbf{局部（该点、固定球面）二阶刚性}✓;\ \text{C-3895 目标是}\ \textbf{一般点} \text{的结构性}✓ \Longrightarrow \textbf{两者互补，不重叠}✓✓;\ \text{全局证明将把 C-3894 当作砖块}✓$$

$$\textbf{⑦ 本档性质}✓✓：\textbf{登记档（无证明、无计算）}✓;\ \text{下一步按唐先生令再开计算}✓✓$$

## §1 交付物清单（✓✓）

| 编号 ✓ | 内容 ✓ | 状态 ✓ |
|---|---|---|
| T2-a ✓ | `Q \mid P'` 的显式代数条件 ✓ | **待做** ✓ |
| T2-b ✓ | 6 项稀疏性 ⟹ `P'` 根成对（路 B） ✓ | **待做** ✓ |
| T2-c ✓ | 奇偶分拆下偶部结构 ⟹ 偶重数 ✓ | **待做** ✓ |
| T2-d ✓ | 退化情形（重数 3+1／4）的处理 ✓ | **待做** ✓ |
| T2-e ✓ | M1 里程碑陈述（`支撑 \le 2` 或 `\deg \le 3`） ✓ | **待做** ✓ |

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| T3（本点） ✓ | **`T3-PASS / LOCAL-RIGIDITY`（已闭合）** ✓✓ |
| T2 目标引理 ✓ | **已登记（ROOT-PAIRING）** ✓✓ |
| T2 路 A／路 B ✓ | **已登记（未做）** ✓ |
| C-3894 定位 ✓ | **局部刚性砖块（保留）** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 ROOT-PAIRING 已证 ✓
- **不**声称 `M1` 已得 ✓
- **不**把 C-3894 说成全局结论 ✓✓
- **不**在本登记档内做计算 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}证明✗；\ \textbf{不}计算✗；\ \textbf{不}重开 T1／T3✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 根集成对引理 命中文件数=0    :: 
技术词 二次式平方判据 命中文件数=0    :: 
技术词 局部刚性砖块 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① T2-a}✓✓：\text{写出}\ Q \mid P'\ \text{的显式条件（含}\ \lambda／\omega\ \text{与}\ m,a\ \text{的关系}✓）；$$
$$\textbf{② T2-b／c}✓：\text{稀疏性 ＋ 奇偶分拆} \text{证根成对}✓✓；$$
$$\textbf{③ T2-d}✓：\text{退化分支（3+1／4）} \text{单独处理}✓✓$$
