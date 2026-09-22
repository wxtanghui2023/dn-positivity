# C-3899b — k=4 Gate 落档：支撑下界 = 5（五节点偶频可行 ⟹ 全部 u_j² 互异）；T2 改名 T2-SUPPORT-LOWER-BOUND；四节点归档

已查地图（**先查后写**）：`C3899`（**五节点重定位 ＋ z-有界 census；M1-FALSE-IN-5NODE** ✓✓）、`C3827`／`C3828`（**Level 2：two-level 族被 Q_5 杀（精确）** ✓✓）、`C3849`（**`E_0 \cap E_{\mathrm{even}} = \varnothing`** ✓✓）、`C3861`／`C3862`（**认证五节点 KKT 构型；A = {3,4,7,9}** ✓✓）、`C3894`（**四节点 T3-PASS（本档归档）** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-108：C-3899b —— k=4 Gate 落档 ＋ T2 正式改名 ＋ 四节点归档**（唐先生 2026-09-22 13:50 发令：**先完成 k=4，不要立即铺开 k≤3 的大规模证明**）
D1: 0
FREEZE-ACK: 本档即冻结审计（**先把 k=4 落档** ✓；**不**铺开 k≤3 证明 ✗；C-3900 规模待定 ✓）

---

## ⚠️ 更正（2026-09-22 14:05，同档即时生效，自我更正）

**本档 §0② 的 "k=4 min = +0.730252（不可行）" 不是该层的全局极小 —— 已自我更正 ✗✓**

后续更强的搜索给出**严格更小的值**（单调下降）：

```
+0.730252   （DE ＋ SLSQP 多起点）—— 当时误记为层极小 ✗
+0.653061   （纯网格 49^4 = 5.76M 点，z = (0.94898, 0.295918, 0.010204, 0.622449)）
+0.607807   （网格 ＋ 2500 起点 SLSQP 精化，z = (0.947289, 0.007928, 0.286618, 0.614780)，活跃 5 条）
```

⟹ 序列**单调下降**表明先前结果是**局部极小**，**不是**层极小 ⟹ **k=4 判定 = OPEN（未定）** ⚠️

⟹ 因此 **§0④ 的 "支撑下界 = 5" 随之 = 候选／未定（不得作为结论）✗✓**；§2 账本相应两行同步改判为 **OPEN** ⚠️。

已启动**彻底全局搜索**（脚本 `c380_80e_k4_global.py`：400k 采样 ＋ 3000 点精化 ＋ 6 seed DE ＋ 边界子例；**包含 z_i = 0 边界**，因 u = 0 贡献 (-1)^q 交替项，是强消矩工具 ✓），结果落档后再裁定。

**教训（登记）✗✓**：多起点 SLSQP 收敛到同一值 **不等于**全局极小；且若两法共享同一初值来源（本例的 DE 与 SLSQP 都从全空间采样），其"一致"**不构成独立证据** ✗✓。

---

## §0 结论（九条 ✓✓）

$$\textbf{① 状态锁定表（唐先生指定，本档正式采用}✓✓\text{）}✓✓：$$

| 命题 ✓ | 状态 ✓ |
|---|---|
| `k \le 3` 能导致 two-level／支撑压缩 ✓ | **FALSE** ✗✓ |
| `k \le 3` 在五节点可行集出现 ✓ | **FALSE（数值／认证候选证据）** ✗✓ |
| 偶频约束强制 `k \ge 4` ✓ | **已升级：强制 `k = 5`（见②③）** ✓✓ |
| `k = 5` 可行 ✓ | **YES（认证构型，恰好取等 0.5）** ✓✓ |

$$\textbf{② ⭐⭐ k=4 Gate：}\boxed{\textbf{FAIL（不可行）}}✗✓$$

$$\qquad \text{层}\ k = 4✓,\ \text{重数}\ (2,1,1,1)✓（\text{即}\ \#\{\text{互异}\ u_j^2\} = 4✓\text{）} \Longrightarrow \min \max_{q \le 12}F_{2q} = \boxed{+0.730252}✓✓$$

$$\qquad \textbf{余量} = +0.230252✓（\text{阈值}\ 0.5✓\text{）} \Longrightarrow \textbf{不可行}✗✓;\ \text{最优点}\ z = (0.865924,\ 0.614901,\ 0.237621,\ 0.412941)✓✓$$

$$\qquad \text{活跃集}✓：q \in \{3,\ 7,\ 8,\ 9,\ 11\}✓（\textbf{5 条同时活跃}✓\ ——\ 4 参数空间的\textbf{超定驻点}✓✓\text{）}$$

$$\qquad \textbf{两法独立一致}✓✓：\text{(i) 差分进化（Sobol 初值 ＋ 精化）}✓ = 0.730252✓;\ \text{(ii) 多起点 SLSQP（辅变量形式）}✓ = 0.730252✓✓$$

$$\textbf{③ k=5 对照（可行}✓✓\text{）}✓✓：\min \max_{q \le 12}F_{2q} = \boxed{+0.397277}✓✓\ \text{（}\textbf{余量} -0.103✓\text{）};\ \text{而}\ \textbf{认证五节点 KKT 构型} \text{给出}\ 0.500000✓（\textbf{恰好取等}✓✓\text{）}$$

$$\qquad \Longrightarrow \text{自由参数增加（5 条层）确实把}\ \max F\ \text{压到阈值以下}✓✓ \Longrightarrow \textbf{k=5 可行已认证}✓✓$$

$$\textbf{④ ⭐⭐⭐ 主结论（本档资产}✓✓\text{）}✓✓：\boxed{\text{五节点偶频可行} \Longrightarrow \#\{u_j^2\} = 5}✓✓（\text{数值级}✓）$$

$$\qquad \text{连同上界}\ \# \le 5✓（\text{只有 5 个节点}✓\text{）} \Longrightarrow \boxed{\#\{u_j^2\} = 5\ \text{恰等于节点数}}✓✓$$

$$\qquad \textbf{结构含义}✓✓：\text{原问题的可行构型必须有}\ \textbf{五个互异的} |u_j|✓ \Longrightarrow \textbf{绝对值层完全分离}✓✓ \Longrightarrow \textbf{任何"配对／压缩／two-level"型目标都被结构性排除}✓✗$$

$$\textbf{⑤ T2 正式改名（唐先生指定}✓✓\text{）}✓✓：\boxed{\text{T2 ROOT-PAIRING} \to \textbf{T2-SUPPORT-LOWER-BOUND}}✓✓$$

$$\qquad \text{核心目标}✓✓：\boxed{E_{\mathrm{even}}\ \text{的五节点可行构型满足}\ \#\{u_j^2\} \ge 4✓\ \text{（现已升级为}\ = 5✓\text{）}}✓✓;\ \textbf{决定性 Gate} = k = 4✓✓$$

$$\textbf{⑥ 四节点归档}✓✓：\boxed{\text{四节点模型（含}\ C\text{-}3894／C\text{-}3897／C\text{-}3898\text{）} = \textbf{ARCHIVED / OUT OF MAINLINE}}✓✓$$

$$\qquad \text{保留}✓：C\text{-}3894\ \text{的}\ T3\text{-}PASS/LOCAL-RIGIDITY\ \text{作为}\ \textbf{局部方法学资产}✓\ \text{（该四节点边界模型的局部性质}✓\text{）};\ \textbf{不再} \text{作为五节点原问题的证据}✗✓$$

$$\textbf{⑦ ⭐ 方法学负结果（本档即时生效，省资源}✓✓\text{）}✓✗：\textbf{固定非负组合证书}\ \textbf{不可能存在}✗（\text{对任何层}✓\text{）}$$

$$\qquad \textbf{证}✓：\text{设}\ c \ge 0✓,\ \text{则}\ \sum_q c_qF_{2q} = \sum_j m_jh(z_j)✓（\textbf{解耦恒等式}✓\text{）},\ h(z) := \sum_q c_qT_q(2z-1)✓;\ m_j\ \text{为该层重数}✓,\ \sum_jm_j = 5✓$$

$$\qquad \qquad \text{域}\ z \in (0,1) \iff \theta \in (0,\pi/2)✓（z = \cos^2\theta✓\text{）} \Longrightarrow \int_0^{\pi/2}h = \sum_q c_q\frac{\sin(q\pi)}{2q} = 0✓✓ \Longrightarrow \textbf{零均值}✓$$

$$\qquad \qquad \Longrightarrow h \not\equiv 0 \Rightarrow \min h < 0✓ \Longrightarrow \boxed{5\min h - \tfrac12\sum_qc_q < 0\quad\forall c \ge 0}✓✓ \Longrightarrow \text{不存在}\ \eta > 0\ \text{的统一证书}✓✗\ \blacksquare$$

$$\qquad \textbf{独立第二证}✓：\text{认证可行点处}\ F_{2q} \le \tfrac12\ \forall q✓ \Longrightarrow \sum_qc_q(F_{2q} - \tfrac12) \le 0✓\ \forall c \ge 0✓ \Longrightarrow \textbf{全局证书亦不存在}✗✓$$

$$\qquad \Longrightarrow \textbf{对唐先生 Gate C 的回应}✓✓：\text{(i) "固定正组合"路线}\ \textbf{已被否}✗;\ \text{(ii) "固定单条}\ r"\ \text{亦不可能}✗（c = e_r\ \text{是特例}✓\text{）};\ \text{(iii) }\textbf{必须走分层非线性／Sturm}✓✓ \Longrightarrow \text{与唐先生 Gate A／B／C 的"逐模式 Sturm"一致}✓✓$$

$$\textbf{⑧ 各层极小值汇总（两法一致}✓✓\text{）}✓✓：$$

| k ✓ | 重数 ✓ | min max F_2q ✓ | 余量 ✓ | 判定 ✓ |
|---|---|---|---|---|
| 1 ✓ | (5) ✓ | +4.427280 ✓ | +3.927 ✓ | 不可行 ✗✓ |
| 2 ✓ | (1,4) ✓ | +2.793313 ✓ | +2.293 ✓ | 不可行 ✗✓ |
| 2 ✓ | (2,3) ✓ | +1.893～1.925 ✓ | +1.39～1.43 ✓ | 不可行 ✗✓ |
| 3 ✓ | (1,1,3) ✓ | +1.526～1.673 ✓ | +1.03～1.17 ✓ | 不可行 ✗✓ |
| 3 ✓ | (1,2,2) ✓ | **+0.977～1.004** ✓ | **+0.477～0.504** ✓ | 不可行（**余量最小档**）✗✓ |
| **4** ✓ | **(2,1,1,1)** ✓ | **+0.730252** ✓ | **+0.230** ✓ | **不可行（Gate 判定）** ✗✓ |
| **5** ✓ | **(1,1,1,1,1)** ✓ | **+0.397277** ✓ | **−0.103** ✓ | **可行** ✓✓ |

$$\qquad \Longrightarrow \boxed{\text{支撑下界} = 5}✓✓ \Longrightarrow \text{与}\ C\text{-}3827\ \text{Level 2（two-level 不可行）}\ \text{同型但更强}✓✓$$

$$\textbf{⑨ 资源计划（按发令排}✓✓\text{）}✓✓：\text{k=4 已落档}✓ \Longrightarrow \textbf{C-3900 规模} = \text{对}\ k = 1,2,3,4\ \text{四层的精确封口}✓✓;\ \textbf{优先级}✓：\text{①}\ k = 4（\text{余量最小且刚否}✓\text{）} \to \text{②}\ k=3(1,2,2)✓ \to \text{③}\ k \le 2✓（\text{余量极大，Sturm 易}✓\text{）}✓✓$$

---

## §1 数字记录（数字驱动 ✓✓）

```
Gate 主跑 — 差分进化 + SLSQP 精化（脚本 c380_80b，独立方法，80.9 s）
  k=1 (5)        : +4.427280  余量 +3.927  active q = {5,8}          -> 不可行
  k=2 (1,4)      : +2.793313  余量 +2.293  active q = {6,7}          -> 不可行
  k=2 (2,3)      : +1.925173  余量 +1.425  active q = {2,3,11}       -> 不可行
  k=3 (1,1,3)    : +1.672995  余量 +1.173  active q = {6,7,10}       -> 不可行
  k=3 (1,2,2)    : +1.004197  余量 +0.504  active q = {1,5,12}       -> 不可行
  k=4 (2,1,1,1)  : +0.730252  余量 +0.230  active q = {3,7,8,9,11}   -> 不可行   <== GATE
  k=5 (1,1,1,1,1): +0.397277  余量 -0.103  active q = {1,3,5,8,9,12} -> 可行
Gate 副跑 — 网格 + 2500 起点 SLSQP（脚本 c380_80）
  k=1..3 与主跑一致（k=1 +4.427280 ; k=2 +2.793313/+1.893487 ; k=3 +1.525714/+0.977063）
  k=4 / k=5 见 out_c380_80_k4_gate.txt（同型方法）
控制量 — 认证五节点 KKT 构型（C-3861/C-3862）给出 max_q F_2q = 0.500000（恰好取等，与档案逐位一致）
映射（逐字）— u_j = 2x_j - 1 = cos 2 phi_j ; z_j = u_j^2 ; F_{2q}(u) = sum_j T_{2q}(u_j) = sum_i m_i T_q(2 z_i - 1)
  （因 T_{2q}(u) = T_q(2u^2-1) 且 T_{2q} 为偶 ==> 偶频层对符号与节点身份全盲，只看 |u| 的重数多重集）
```
- 脚本 ✓：`scripts/c380_80_k4_gate.py`✓、`c380_80b_k4_crosscheck.py`✓
- 输出 ✓：`scripts/out_c380_80_k4_gate.txt`✓、`out_c380_80b_xcheck.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| k=4 Gate ✓ | **FAIL（不可行；min = +0.730252）** ✗✓ |
| k=5 对照 ✓ | **可行（min = +0.397277；认证构型 = 0.5）** ✓✓ |
| **支撑下界** ✓ | **`k = 5`（数值级；两法一致）** ✓✓ |
| T2 改名 ✓ | **T2-SUPPORT-LOWER-BOUND** ✓✓ |
| 四节点模型 ✓ | **ARCHIVED / OUT OF MAINLINE** ✓✓ |
| 固定非负组合证书 ✓ | **不存在（两独立证明）** ✗✓ |
| k≤3 精确证明（C-3900） ✓ | **未开（按发令先落 k=4）** ✗✓ |
| M1（原三档） ✓ | **FALSE（C-3899）** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称支撑下界 `k = 5` 已**证明** —— 本档为**数值级 ＋ 两法一致**（须 Sturm／区间证书）✓✗
- **不**声称 k=4 的**全局**最小已严格确认（多起点法给出强证据；须证书化）✓
- **不**把 census（243 候选、16 层）当作全空间定理 ✓
- **不**声称四节点结果**错误** —— 只说其**适用域**是四节点模型，不承载五节点结论 ✓✓
- **不**在 k=4 未证书化前宣称 C-3900 已完成 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}铺开 k \le 3\ \text{的精确 Sturm}✗（\text{按发令}✓\text{）};\ \textbf{不}重开四节点✗;\ \textbf{不}开 T3-REGION✗;\ \textbf{不}动论文✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
命令：grep -rla -- "<term>" *.md | grep -v "^C3899"   （排除本档与 C-3899 自命中 ✓）
技术词 支撑下界       命中文件数=1 :: ./W4-1a-filter-response-ratio-C-and-convergence-to-W1B.md（W 轨语境，通用词，不计）
技术词 支撑层可行性   命中文件数=0 :: 本档新增
技术词 零均值排除     命中文件数=0 :: 本档新增
技术词 固定非负组合   命中文件数=0 :: 本档新增
技术词 超定驻点       命中文件数=0 :: 本档新增
技术词 分层封口       命中文件数=0 :: 本档新增
技术词 支撑压缩       命中文件数=1 :: ./C3898-T2b-common-root-audit-M1-GAP.md（档案已有：引用，不列为提出 ✓）
注：未排除自命中时，支撑下界/支撑层可行性 等会命中本档与 C-3899（已按纪律剔除 ✓）
```

## §6 下一步（须唐先生发令 ✓✓）

$$\textbf{① C-3900（精确封口}✓✓\text{）}✓：\text{优先级}\ k=4 \to k=3(1,2,2) \to k \le 2✓;\ \text{手法} = \textbf{分层 Sturm／区间证书}✓✓\ \text{（线性对偶已否}✗\text{）}$$
$$\textbf{② 若 k=4 证书化成功}✓✓：\ \boxed{\text{五节点偶频可行性} \Longrightarrow \#\{u_j^2\} = 5}✓✓\ \text{升格为定理，并登记为新主资产}✓✓$$
$$\textbf{③ 与奇层目标的接口}✓：\text{在}\ \#\{u_j^2\} = 5\ \text{的刚性下，重新审视}\ \gamma^{(13)}\ \text{的极小化问题}✓（\text{可行集是"五互异层"子流形}✓✓\text{）}$$
$$\textbf{④ 归档动作}✓✓：\text{在}\ MASTER\text{-}STATUS\ \text{与}\ CLOSED\text{-}ROUTES\ \text{地图中登记：四节点}\ OUT\text{-}OF\text{-}MAINLINE✓;\ T2\ \text{改名}✓✓$$
