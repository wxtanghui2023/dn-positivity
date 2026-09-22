# C-3897 — T2 first cut: parity decomposition of the stationarity polynomial and common-root factor audit

已查地图（**先查后写**）：`C3895`（**ROOT-PAIRING 登记** ✓✓）、`C3896`（**精确 T3 证书** ✓✓）、`C3894`（**二阶主导机制** ✓✓）、`C3891`（**`P(c)`；奇偶分拆** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-105：C-3897 —— T2 ROOT-PAIRING 第一刀（奇偶分解 ＋ 共同根因子审计）**（唐先生 2026-09-22 09:42 令：②优先，①暂缓）
D1: 0
FREEZE-ACK: 本档即冻结审计（**禁**大规模 resultant／数值猜根／直接宣称 two-level ✓）

---

## §0 结论（七条 ✓✓）

$$\textbf{① 纪律}✓✓：\text{第一刀}\ \textbf{只做} \text{奇偶分解 ＋ 共同根因子审计}✓;\ \textbf{禁} \text{大规模 resultant}✗、\textbf{禁} \text{数值猜根}✗、\textbf{禁} \text{直接宣称 two-level}✗✓$$

$$\textbf{② 核验事实（sympy，精确}✓✓**）：$$

| 频类 ✓ | 梯度 ✓ | 奇偶 ✓ |
|---|---|---|
| 活跃偶频约束 `q \in \{6,8,14,18\}` ✓ | `T'_{2q}(u)` ✓ | **奇** ✓（`T'_{2q}(-u) + T'_{2q}(u) = 0` ✓） |
| 奇频目标 `13, 19` ✓ | `T'_{13}(u)`, `T'_{19}(u)` ✓ | **偶** ✓（`T'_{n}(-u) - T'_{n}(u) = 0` ✓） |

$$\qquad \Longrightarrow \text{偶频约束（}\text{偶函数} T_{2q}\text{）的梯度为}\ \textbf{奇}✓;\ \text{奇频目标（}\text{奇函数} T_{13},T_{19}\text{）的梯度为}\ \textbf{偶}✓✓$$

$$\textbf{③ ⭐ 奇偶分解（唐先生指定形式}✓✓**）：\text{完整 KKT stationarity}✓：$$

$$\qquad \boxed{P(u) = \underbrace{\sum_{q \in \mathcal A}\lambda_qT'_{2q}(u) + \beta u}_{\textbf{奇}\ \Rightarrow\ uR_1(u^2)} + \underbrace{-\omega_{13}T'_{13}(u) + \omega_{19}T'_{19}(u) + \alpha}_{\textbf{偶}\ \Rightarrow\ R_2(u^2)}}✓✓$$

$$\qquad \Longleftrightarrow \boxed{P(u) = uR_1(u^2) + R_2(u^2)}✓✓,\quad \deg R_1 \le 17✓,\ \deg R_2 \le 18✓$$

$$\qquad \text{（来源归属}✓：\text{偶频约束} \to R_1✓;\ \text{奇频目标} \to R_2✓;\ \text{矩乘子}\ \beta u \to R_1✓,\ \alpha \to R_2✓✓）$$

$$\textbf{④ 由③立即得到的等式}✓✓：$$

$$\qquad (uR_1(u^2) + R_2(u^2) = 0\ \text{在支撑点}\ ✓) \Longrightarrow \text{置}\ z := u^2✓：\ (uR_1(z))^2 = R_2(z)^2 \Longrightarrow \boxed{zR_1(z)^2 - R_2(z)^2 = 0}✓✓$$

$$\qquad \Longrightarrow \text{每个支撑的}\ z\ \text{是}\ \textbf{同一个多项式}\ zR_1^2 - R_2^2\ \text{（次数} \le 36✓）\ \text{的根}✓✓$$

$$\textbf{⑤ ⚠️ 诚实审计结果：}\boxed{\text{奇偶分解}\ \textbf{不} \text{单独给出根集成对}}✗✓$$

$$\qquad \text{理由}✓：\text{给定}\ z✓,\ \text{条件}\ uR_1(z) = -R_2(z)\ \text{一般只被}\ \textbf{一个} \text{符号的}\ u = \pm\sqrt z\ \text{满足}✗✓$$

$$\qquad \qquad \text{（两侧要}\ \text{同时} \text{成立须}\ R_2(z) = 0\ \text{且}\ R_1(z) = 0\ \text{或}\ u = 0✓ \Longrightarrow \textbf{非一般情形}✗✓）$$

$$\qquad \Longrightarrow \text{支撑}\ \textbf{不是} \pm\text{配对}✗;\ \text{故}\ \textbf{根集成对必须来自"活跃等式"与③的联立}✓✓$$

$$\textbf{⑥ 共同根因子审计（唐先生指定}✓✓**）：\text{两不同根}\ u \ne v\ \text{给出两条方程}✓：uR_1(z_u) + R_2(z_u) = 0✓,\ vR_1(z_v) + R_2(z_v) = 0✓$$

$$\qquad \textbf{待查（下一刀}✓**）：\text{能否用四个活跃等式}\ F_{2q} = \tfrac12\ (q \in \mathcal A✓)＋矩约束，\text{从③中}\ \textbf{消去} R_1, R_2✓$$

$$\qquad \qquad \text{使}\ (u-v)(u+v)R(u,v) = 0\ \text{型}\ \textbf{低复杂度因子} \text{出现}✓✓;\ \textbf{候选机制}✓：\text{指数集}\ \{6,8,14,18\}\ \text{的差集}\ \{2,6,8,10,12\}\✓\ \text{与}\ U_n\ \text{乘积结构}✓$$

$$\textbf{⑦ 状态}✓✓：\textbf{T2-a 完成（分解形式已立）}✓;\ \textbf{M1 未达}✗（\text{尚未得"}\le 3\ \text{distinct"}✓）;\ \text{本刀只交付}\ \textbf{结构分解}✓✓$$

## §1 交付物清单（✓✓）

| 编号 ✓ | 内容 ✓ | 状态 ✓ |
|---|---|---|
| T2-a ✓ | 奇偶分解 `P(u) = uR_1(u^2) + R_2(u^2)` ✓ | **完成** ✓✓ |
| T2-a′ ✓ | 由分解得的方程 `zR_1(z)^2 = R_2(z)^2` ✓ | **完成** ✓✓ |
| T2-b ✓ | 稀疏性 ⟹ 根成对 ✓ | **未做** ✗ |
| T2-c ✓ | 偶部结构 ⟹ 偶重数 ✓ | **未做** ✗ |
| T2-d ✓ | 退化情形（3+1／4） ✓ | **未做** ✗ |
| T2-e ✓ | M1 里程碑 ✓ | **未达** ✗ |

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 奇偶核验（两频类） ✓ | **完成（精确）** ✓✓ |
| 奇偶分解 ✓ | **完成** ✓✓ |
| 根集成对 ✓ | **未得（已定位原因）** ✗✓ |
| 共同根因子 ✓ | **待做（已具体化）** ✓ |
| M1 ✓ | **未达** ✗ |

## §3 边界（不得声称 ✗✓）

- **不**声称根集成对已证 ✓
- **不**声称 M1 已得 ✓
- **不**声称 two-level ✓✓
- **不**用大规模 resultant／数值猜根 ✓
- **不**把"分解形式"当作支持压缩结论 ✓✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}做区域 T3（①）✗;\ \textbf{不}扩张 T3 stability✗;\ \textbf{不}动 T4✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 奇偶分解     命中文件数=1    :: ./C3801-non-polynomial-sign-layer-coupling-audit-registration.md 
技术词 共同根因子审计 命中文件数=0    :: 
技术词 支持压缩     命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 共同根因子（T2-b}✓✓**）：\text{用四活跃等式 ＋ 矩约束消去}\ R_1, R_2✓,\ \text{检验}\ (u-v)(u+v)R\ \text{型因子}✓✓$$
$$\textbf{② 三问审计}✓（唐先生指定）：\text{(i) 奇部是否自动低阶？}\ \text{(ii) 偶部能否唯一确定}\ u^2？\ \text{(iii) 两个不同绝对值能否同时满足 KKT？}✓✓$$
$$\qquad \Longrightarrow \text{若 (iii) 被排除} \Longrightarrow |u_i| = |u_j| \Longrightarrow \text{支撑} \subseteq \{+a,-a\}✓\ \text{（再合均值约束} \to two-level✓）✓✓$$
