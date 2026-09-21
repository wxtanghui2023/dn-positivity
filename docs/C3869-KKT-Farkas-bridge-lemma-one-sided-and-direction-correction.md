已查地图（**先查后写**）：`C-3868`（**`(\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)`；`Lc_{\mathrm{full}} = 1`（残差 2.5e-31）** ✓✓）、`C-3867`（**primal/dual 逐位同值；顶点方阵 6×6** ✓✓）、`C-3864`（**`t^*_{\mathrm{full}} = 0`；control `+1`** ✓✓）、`C-3863`（**KKT 点与乘子** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-69：C-3869 —— KKT → Farkas 桥引理的五步逐行审计（含方向更正）**（唐先生 2026-09-21 22:45 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 档位}✓✓：\textbf{纯代数审计}✓✓；\ \textbf{不}跑优化✗；\ \textbf{不}用新数值✗；\ \textbf{不}碰二阶✗✓$$

$$\textbf{② 记号}✓✓：v_i = s_i\nabla F_i\ (i = 13,19)✓;\ w_q = \nabla F_q\ (q \in \mathcal A = \{6,8,14,18\})✓;\ L := \sum_q\lambda_q✓✓$$

$$\qquad \text{KKT}✓✓：\omega_{13}v_{13} + \omega_{19}v_{19} + \sum_q\lambda_qw_q = 0✓,\ \omega_{13} + \omega_{19} = 1✓,\ \omega,\lambda \ge 0✓✓$$

$$\textbf{③ 步 1（}\textbf{有效}✓✓）：全文除以}\ L✓ \Longrightarrow \frac{\omega_{13}}Lv_{13} + \frac{\omega_{19}}Lv_{19} + \sum_q\frac{\lambda_q}Lw_q = 0✓ \Longrightarrow$$

$$\qquad \boxed{\nu_i = \frac{\omega_i}L,\quad \mu_q = \frac{\lambda_q}L}✓✓\ \text{为}\ \textbf{dual-feasible}✓（\sum_q\mu_q = 1✓,\ \nu,\mu \ge 0✓）;\qquad \text{对偶值} = \nu_{13} + \nu_{19} = \frac{\omega_{13}+\omega_{19}}L = \boxed{\frac1L}✓✓$$

$$\qquad \text{与}\ C\text{-}3867\ \text{对照}✓✓：\mu_q\ \text{逐项相符到}\ 20\ \text{位}✓✓；\ \nu_i\ \text{需用}\ 60\ \text{dps 的}\ \omega\ \text{（本档审计中我先用了 9 位}\ \omega✓,\ \text{故}\ \nu_{13}\ \text{仅}\ \sim10\ \text{位相符}⚠️✓,\ C\text{-}3868\ \text{已用高精度}\ \omega\ \text{确认}✓✓）$$

$$\textbf{④ 步 2（}\textbf{有效}✓✓）：对任意 \textbf{primal-feasible}\ h✓（v_{13}h \le -1✓,\ v_{19}h \le -1✓）：$$

$$\qquad \omega_{13}(v_{13}h) + \omega_{19}(v_{19}h) \le -(\omega_{13} + \omega_{19}) = -1✓✓\ \text{（}\omega \ge 0\ \text{且归一化}✓）$$

$$\qquad \text{代入 KKT}✓：\omega_{13}v_{13} + \omega_{19}v_{19} = -\sum_q\lambda_qw_q✓ \Longrightarrow \boxed{\sum_q\lambda_qw_qh \ge 1}✓✓$$

$$\textbf{⑤ 步 3（}\textbf{有效}✓✓）：由}\ w_qh \le \max_r w_rh✓\ \text{与}\ \lambda \ge 0✓ \Longrightarrow L\max_qw_qh \ge \sum_q\lambda_qw_qh \ge 1✓ \Longrightarrow \boxed{\max_qw_qh \ge \frac1L}✓✓$$

$$\textbf{⑥ ⚠️ 步 4（}\textbf{方向更正}✗✓**）：$$

$$\qquad \text{弱对偶方向}✓✓：\text{primal}\ \min c✓\ \text{的}\ \text{对偶为}\ \textbf{最大化}✓ \Longrightarrow \text{dual-feasible 证书给}\ \boxed{c_* \ge \nu_{13} + \nu_{19} = \frac1L}✓✓$$

$$\qquad \Longrightarrow \text{唐先生原文"显式 dual certificate 给出}\ c_* \le \frac1L\text{"}\ \textbf{方向反}✗✓;\ \text{步 2／3（primal 侧）与步 1（dual 侧）给的是}\ \textbf{同一个下界}✓✓$$

$$\qquad \textbf{步 4 正确表述}✓✓：\ \boxed{c_* \ge \frac1L\ \text{（单边严格}✓）};\ \text{要得}\ c_* \le \frac1L\ \text{需}\ \textbf{取到上界步}✗✓：$$

$$\qquad \qquad \text{即}\ \text{构造一个 primal-feasible}\ h\ \text{使}\ \max_qw_qh = \frac1L✓✓ \Longleftrightarrow \textbf{顶点方阵可解}✓（v_{13}h = -1✓,\ v_{19}h = -1✓,\ w_qh = c\ (q \in \mathcal A)✓,\ 6\times6✓）$$

$$\textbf{⑦ 步 5（}\textbf{实例级等号成立；一般定理尚缺取到步}⚠️✓**）：$$

$$\qquad \text{数值}✓✓：\frac1L = \mathbf{0.500808953629041885590052265792}✓,\ \left|\frac1L - c_{\mathrm{full}}\right| = 1.8\times10^{-31}✓✓ \Longrightarrow \boxed{c_{\mathrm{full}} = \frac1L\ \text{（30 位}✓）}$$

$$\qquad \text{且}\ C\text{-}3867\ \text{在}\ 60\ \text{dps 下确实解出该}\ 6\times6\ \text{顶点方阵}✓✓ \Longrightarrow \textbf{该 KKT 点处等号成立}✓✓$$

$$\qquad ⚠️ \textbf{一般定理缺口}✗✓：\text{顶点方阵的可解性＝}\textbf{非退化／秩条件}✓✓,\ \text{尚未证明}✓\ \text{（实例级已验证到 30 位}✓）$$

## §1 修正后的引理陈述（✓✓）

$$\textbf{引理（}\textbf{单边 KKT → Farkas 桥}✓✓，\textbf{严格已证}✓）}：\text{设}\ (\phi,\omega,\lambda)\ \text{满足 KKT 站性}✓,\ \omega_{13} + \omega_{19} = 1✓,\ \omega,\lambda \ge 0✓,\ L = \sum_q\lambda_q > 0✓$$

$$\qquad \text{记}\ c_* = \inf\{\max_qw_qh\ :\ v_{13}h \le -1,\ v_{19}h \le -1\}✓✓ \Longrightarrow \boxed{c_* \ge \frac1L}✓✓$$

$$\qquad \text{且证书}\ (\nu,\mu) = (\omega/L,\ \lambda/L)\ \text{dual-feasible}✓,\ \text{对偶值}\ 1/L✓✓$$

$$\textbf{推论（实例级）}✓✓：\text{在}\ C\text{-}3863\ \text{的 KKT 点处}✓,\ c_* = \frac1L = 0.500808953629041885590052265792✓✓\ \text{（}\text{因顶点方阵可解}✓）$$

$$\qquad \Longrightarrow \text{这解释了}\ C\text{-}3868\ \text{的}\ \textbf{同构}✓✓：\text{不是"两个 LP 数字巧合"✓,\ 而是}\ \textbf{KKT 射线的归一化必然给出}\ 1/L✓✓$$

## §2 账本（✓✓）

| 步骤 ✓ | 审计结论 ✓ |
|---|---|
| 1 KKT ÷ L ⟹ dual-feasible 证书 ✓ | **有效（$\mu$ 逐项到 20 位）** ✓✓ |
| 2 primal-feasible $h$ ⟹ $\sum\lambda_qw_qh \ge 1$ ✓ | **有效** ✓✓ |
| 3 ⟹ $\max_qw_qh \ge 1/L$ ✓ | **有效** ✓✓ |
| 4 dual 证书 ⟹ $c_* \le 1/L$ ✓ | **⚠️ 方向更正为 $c_* \ge 1/L$** ✗✓ |
| 5 $c_{\mathrm{full}} = 1/L$ ✓ | **实例级成立（30 位）；一般定理缺"取到步"** ⚠️✓ |
| 单边桥引理 ✓ | **CLOSED（严格）** ✓✓ |
| 取到／秩条件 ✓ | **未证（实例级已验证）** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 $c_* = 1/L$ 已升为**一般定理**（缺取到／秩步）✓
- **不**声称全局最优／$V_\sigma$ 真值 ✓
- **不**把 $c_* \ge 1/L$（严格）与 $c_* = 1/L$（实例）混为一谈 ✓
- **不**声称已连到 arithmetic bridge ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}跑优化✗；\ \textbf{不}用新数值✗；\ \textbf{不}碰二阶敏感度✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 单边桥引理  命中文件数=0    :: 
技术词 方向更正     命中文件数=2    :: ./E47-E30-2b-criteria-classification.md ./V103-archive-tension-resolution.md 
技术词 取到上界步  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 补"取到步"}✓✓：\text{证}\ 6\times6\ \text{顶点方阵}\ (v_{13}h = -1,\ v_{19}h = -1,\ w_qh = c)\ \textbf{可解}✓✓ \Longrightarrow \text{把}\ c_* = 1/L\ \text{升为}\ \textbf{一般定理}✓$$
$$\qquad \text{候选路线}✓：\text{秩条件}\ \operatorname{rank}[v_{13};v_{19};w_q] = 5✓\ \text{＋}\ \text{相容性}（\text{KKT 射线的}\ \textbf{非退化}✓）$$
$$\textbf{② 语义}✓：\text{若①成立} \Longrightarrow \boxed{\text{KKT 站性} + \text{odd 归一化} + \text{even 对偶归一化} \Longrightarrow c = \frac1L}✓✓\ \text{（\textbf{非} ray-alignment 假设}✓）$$
$$\textbf{③ C-3869-}\beta✓：\ \text{二阶敏感度}（\text{暂缓}✓）$$
