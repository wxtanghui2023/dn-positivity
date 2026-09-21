已查地图（**先查后写**）：`C-3867`（**40+ dps primal/dual 闭合；`\mu,\nu,c_{\mathrm{full}}`** ✓✓）、`C-3866`（**定量桥常数** ✓✓）、`C-3863`（**`\lambda,\omega` 基准** ✓✓）、`C-3862`（**A1–A5** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-68：C-3868 —— KKT → Farkas 比例同构审计（三层）**（唐先生 2026-09-21 22:43 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 档位}✓✓：\textbf{纯高精度／符号审计}✓✓；\ \textbf{不}重优化 primal✗；\ \textbf{不}改 β-2 LP✗；\ \textbf{不}加新优化问题}✗✓$$

$$\qquad \text{60 dps 重解}\ 10\times10\ \text{KKT 方阵}✓ \Longrightarrow \text{残差}\ 2.0\times10^{-59}✓✓ \Longrightarrow \text{拿到高精度}\ (\lambda, \omega)✓✓$$

$$\textbf{② LAYER A（偶频乘子归一化，}\textbf{四项逐列}✓✓）:\ } \mu_q \stackrel{?}{=} \lambda_q/L,\ L = \sum_q\lambda_q = 1.99676941227516035204325246457✓$$

$$\qquad \Delta\mu_3 = +1.83\times10^{-26}✓;\quad \Delta\mu_4 = +2.41\times10^{-26}✓;\quad \Delta\mu_7 = +4.38\times10^{-27}✓;\quad \Delta\mu_9 = +3.19\times10^{-27}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{LAYER A}\ \textbf{CLOSED}}✓✓\ \text{（残差}\ \sim10^{-26}✓\ \text{即}\ C\text{-}3867\ \text{输入精度的}\ \textbf{地板}✓,\ \text{非}\ \text{结构性残差}✓）$$

$$\textbf{③ LAYER B（odd 权重绝对尺度）}✓✓：$$

$$\qquad \nu_{13} = 0.4525900377602654099448385✓,\quad c_{\mathrm{full}}\omega_{13} = 0.4525900377602654099448385✓ \Longrightarrow \boxed{\Delta\nu_{13} = +4.84\times10^{-26}}✓✓$$
$$\qquad \nu_{19} = 0.04821891586877647564521381✓,\quad c_{\mathrm{full}}\omega_{19} = 0.04821891586877647564521381✓ \Longrightarrow \boxed{\Delta\nu_{19} = -4.16\times10^{-27}}✓✓$$

$$\qquad \text{比值}✓：\nu_{13}/\omega_{13} = \nu_{19}/\omega_{19} = 0.5008089536290418855900522657\ldots = c_{\mathrm{full}}✓✓ \Longrightarrow \boxed{\text{LAYER B}\ \textbf{CLOSED}}✓✓$$

$$\textbf{④ ⭐ LAYER C（尺度陷阱，}\textbf{单独检查}✓✓**）：$$

$$\qquad L \cdot c_{\mathrm{full}} = 1.99676941227516035204325246457 \times 0.500808953629041885590052265792 = \mathbf{1.0}✓✓$$

$$\qquad \boxed{L \cdot c_{\mathrm{full}} - 1 = 2.47\times10^{-31}}✓✓ \Longrightarrow \boxed{\text{LAYER C}\ \textbf{CLOSED}}✓✓\ \text{（}\textbf{30 位} \text{级}✓）$$

$$\textbf{⑤ ⭐⭐ 合并：}\textbf{三层全闭合} ⟹ \text{统一陈述}✓✓$$

$$\qquad \text{由}\ \mu = \lambda/L✓\ \text{与}\ L = 1/c_{\mathrm{full}}✓ \Longrightarrow \boxed{\mu = c_{\mathrm{full}}\,\lambda}✓✓;\qquad \text{由 B} \Longrightarrow \boxed{\nu = c_{\mathrm{full}}\,\omega}✓✓$$

$$\qquad \Longrightarrow \boxed{(\mu, \nu) = c_{\mathrm{full}}\,(\lambda, \omega)}✓✓ \Longrightarrow \textbf{Farkas 对偶证书 ＝ KKT 证书乘以桥常数}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{C3863 KKT geometry} \Longrightarrow \text{C3867 normalized Farkas certificate}}✓✓$$

$$\qquad \Longrightarrow \ c_{\mathrm{full}}\ \textbf{不是孤立的 LP 常数}✓✓,\ \text{而是}\ \textbf{KKT 乘子系统的共同尺度因子}✓✓$$

$$\textbf{⑥ 一致性核验}✓✓：\text{KKT 平衡残差} = 2.0\times10^{-59}✓✓（\text{自身高精度}✓）；\ \text{Farkas 平衡残差} = 2.5\times10^{-25}✓（\text{受}\ C\text{-}3867\ \text{输入的}\ 25\ \text{位限制}✓）$$

$$\qquad \text{两者在各自精度内}\ \textbf{一致}✓✓；\ \text{等式}\ \nu_{13}v_{13} + \nu_{19}v_{19} + \sum\mu_q\nabla F_{2q} = 0✓\ \text{与}\ \text{KKT 站性}\ \textbf{同构}✓✓$$

$$\textbf{⑦ 判词（按唐先生表格）}✓✓：\ \boxed{\text{A＋B＋C 全部闭合}}✓✓ \Longrightarrow \textbf{非常强的结构结果}✓✓;\ \ c_{\mathrm{full}}\ \text{为}\ \textbf{共同尺度}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
60 dps 重解 KKT 方阵：残差 2.0e-59
  omega_13 = 0.903717944...（30 位）; omega_19 = 1-omega_13
  lambda_3 = 0.837917064256959665845251945367
  lambda_4 = 0.989714055780433823538410896454
  lambda_7 = 0.0418531867977506525607285492544
  lambda_9 = 0.127285105440016210098861073496
  L = 1.99676941227516035204325246457
LAYER A: Delta_mu = +1.83e-26 / +2.41e-26 / +4.38e-27 / +3.19e-27  （四项）
LAYER B: Delta_nu13 = +4.84e-26 ; Delta_nu19 = -4.16e-27 ; ratios/omega = c_full（25 位）
LAYER C: L*c_full = 1.0 ; L*c_full - 1 = 2.47e-31
一致性: ||KKT balance|| = 2.02e-59 ; ||Farkas balance|| = 2.50e-25
```
- 脚本 ✓：`scripts/c380_68_C3868_kkt_farkas.py`✓；输出 ✓：`scripts/out_c380_68.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| LAYER A (`\mu_q = \lambda_q/L`) ✓ | **CLOSED（四项；~1e-26）** ✓✓ |
| LAYER B (`\nu = c_{\mathrm{full}}\omega`) ✓ | **CLOSED（~1e-26）** ✓✓ |
| **LAYER C (`Lc_{\mathrm{full}} = 1`)** ✓ | **CLOSED（2.5e-31）** ✓✓ |
| 合并结构 ✓ | **`(\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)`** ✓✓ |
| **判词** ✓ | **KKT 几何 ⟹ 归一化 Farkas 证书** ✓✓ |
| `c_{\mathrm{full}}` 的地位 ✓ | **KKT 乘子系统共同尺度因子** ✓✓ |
| C-3869 二阶敏感度 ✓ | **未开（唐先生建议暂缓）** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称全局最优／`V_\sigma` 真值 ✓
- **不**声称该结构已连到 arithmetic bridge ✓
- **不**把 `\sim10^{-26}` 残差解释为结构性残差（那是 25 位输入精度的地板）✓
- **不**声称二阶敏感度已做 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}加新优化问题✗；\ \textbf{不}重优化}\ c_{\mathrm{full}}✗；\ \textbf{不}做 box／二阶敏感度✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 比例同构     命中文件数=0    :: 
技术词 共同尺度因子 命中文件数=0    :: 
技术词 证书同构     命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 理论接口}✓✓（\text{唐先生指定}✓）：\textbf{为什么}\ β\text{-2 的最优分离常数恰好等于该 KKT 系统的共同尺度？}✓✓$$
$$\qquad \text{现有材料}✓：(\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)✓\ \text{＋}\ Lc_{\mathrm{full}} = 1✓ \Longrightarrow \text{可问}\ c_{\mathrm{full}}\ \text{是否由}\ \omega\ \text{与}\ \lambda\ \text{的}\ \textbf{归一化约定} \text{唯一决定}✓✓$$
$$\textbf{② C-3869}✓：\text{box 半宽／}\delta\ \text{二阶修正对}\ c_{\mathrm{full}}\ \text{的敏感度}（\text{暂缓}✓）$$
$$\textbf{③ 全局性}✓：V_\sigma\ \text{的全局最小证书}（\text{独立}✓）$$
