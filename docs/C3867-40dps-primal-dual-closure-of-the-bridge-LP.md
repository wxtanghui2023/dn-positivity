已查地图（**先查后写**）：`C-3866`（**β-2′：`c_{\mathrm{full}} = 0.500808953629`；求解器级 CLOSED** ✓✓）、`C-3864`（**`t^*_{\mathrm{full}} = 0` 交叉校验** ✓✓）、`C-3863`（**40-dps KKT 点；`\lambda,\omega` 基准** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-67：C-3867 —— 40+ dps primal/dual 闭合（高精度同值证书）**（唐先生 2026-09-21 22:42 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 模型不变}✓✓：\ \min_{h,c}c\ \text{s.t.}\ v_{13}h \le -1✓,\ v_{19}h \le -1✓,\ Wh - c\mathbf 1 \le 0✓✓\ \text{（}\textbf{不}重优化／\textbf{不}改归一化／\textbf{不}加二阶项}✗✓$$

$$\textbf{② 60 dps 重建全部系数（}\textbf{禁止双精度 LP 输出作输入}✗✓）}✓✓：\text{自}\ C\text{-}3863\ \text{点重新解}\ 5\times5\ \text{KKT 系统}✓ \Longrightarrow \boxed{\text{残差}\ 1.478\times10^{-60}}✓✓$$

$$\qquad x = (0.8009302155414330192645585,\ 0.5611431997255226913605271,\ 0.7024571606623587274758512,\ 0.6261014034243929958331771,\ 0.8688438905530294285224676)✓✓$$

$$\textbf{③ primal certificate}✓✓：\text{解顶点方阵}✓（v_{13}h = -1✓,\ v_{19}h = -1✓,\ b_q(h) = c\ (q \in \mathcal A)✓—— 六行全活跃}✓✓） \Longrightarrow$$

$$\qquad \boxed{c_p = 0.500808953629041885590052265792}✓✓\ \text{（30 位}✓）;\qquad h^* = (0.02440505,\ 0.01462050,\ -0.01841631,\ 0.02306044,\ 0.04896166)✓✓$$

$$\qquad \boxed{\|h^*\|_\infty = 0.04896166 < 1}✓✓ \Longrightarrow \textbf{box 严格 inactive}✓✓;\qquad \text{primal 残差} = 7.8\times10^{-62}✓✓$$

$$\textbf{④ 对偶 certificate（按数学 LP 写，}\textbf{不用 solver marginal}✗✓）}✓✓$$

$$\qquad \text{站性}✓✓：\nu_{13}v_{13} + \nu_{19}v_{19} + \sum_{q \in \mathcal A}\mu_q\nabla F_{2q} = 0✓（5 式}✓）;\qquad \sum_q\mu_q = 1✓✓$$

$$\qquad \mu = (0.4196363681784466232834694,\ 0.4956576606673542568951606,\ 0.02096045068622233460521499,\ 0.06374552046797678521615506)✓✓$$
$$\qquad \nu_{13} = 0.4525900377602654099448385✓,\qquad \nu_{19} = 0.04821891586877647564521381✓✓$$

$$\qquad \text{对偶可行}✓✓：\mu \ge 0✓,\ \nu \ge 0✓；\ \sum\mu - 1 = 0✓；\ \text{站性残差} = 6.2\times10^{-61}✓✓$$

$$\textbf{⑤ ⭐⭐ 高精度同值}✓✓：$$

$$\qquad c_d = \nu_{13} + \nu_{19} = \mathbf{0.500808953629041885590052265792}✓✓$$

$$\qquad \boxed{|c_p - c_d| = \mathbf{0.0}}✓✓\ \text{（60 位下}\ \textbf{逐位相同}✓✓）\ \Longrightarrow\ \textbf{远超}\ 10^{-30}\ \text{阈值}✓✓$$

$$\textbf{⑥ 互补松弛}✓✓：\text{六行全部取等}✓（v_{13}h + 1 = 0✓,\ v_{19}h + 1 = 0✓,\ b_q - c = 0✓）\ ⟹\ \text{CS 逐项成立}✓✓\ \text{（}\nu_{13},\nu_{19},\mu_q > 0✓）$$

$$\textbf{⑦ 判词}✓✓：\ \boxed{\text{C-3867 = }\textbf{CLOSED}}✓✓\ \text{（高精度 primal／dual 同值证书}✓✓） \Longrightarrow\ \text{β-2 由}\ \textbf{求解器级} \text{升级为}\ \textbf{可认证}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
step1 60 dps 重建：||residual|| = 1.478e-60 ；x 25 位稳定
step2 primal 顶点方阵（6 eqs/6 unknowns）：c_p = 0.500808953629041885590052265792
      ||h*||_inf = 0.04896165879（< 1，box 严格 inactive）
      primal 残差：v13h+1 = 0.0 ; v19h+1 = 7.8e-62 ; max_q(b_q - c) = 7.8e-62
step3 dual 方阵：mu = [0.4196363681784466232834694, 0.4956576606673542568951606,
                       0.02096045068622233460521499, 0.06374552046797678521615506]
      nu13 = 0.4525900377602654099448385 ; nu19 = 0.04821891586877647564521381
      对偶可行 True/True ; sum(mu)-1 = 0.0 ; 站性残差 6.223e-61
      c_d = nu13+nu19 = 0.500808953629041885590052265792 ; |c_p - c_d| = 0.0
```
- 脚本 ✓：`scripts/c380_67_C3867_highprec.py`✓；输出 ✓：`scripts/out_c380_67.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 模型不变 ✓ | **是** ✓✓ |
| 60 dps 系数重建 ✓ | **完成（残差 1.5e-60）** ✓✓ |
| primal certificate ✓ | **CLOSED（c_p 30 位；box inactive）** ✓✓ |
| dual certificate ✓ | **CLOSED（对偶可行 ＋ 站性 6e-61）** ✓✓ |
| `c_p` vs `c_d` ✓ | **`|c_p - c_d| = 0`** ✓✓ |
| 互补松弛 ✓ | **CLOSED** ✓✓ |
| **C-3867 判词** ✓ | **CLOSED** ✓✓ |
| C-3868 `(\lambda,\omega)` 审计 ✓ | **现才解锁（本档未做）** ✓ |

## §3 边界（不得声称 ✗✓）

- **不**在本档做 `(\lambda,\omega)` 比例审计（唐先生明令顺序）✓
- **不**声称该常数已连接到 arithmetic bridge ✓
- **不**声称全局性（仍为局部 KKT 点处的桥）✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}改模型／归一化✗；\ \textbf{不}加二阶项✗；\ \textbf{不}用 solver marginal 顶替数学对偶✗；\ \textbf{不}开 C-3868✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 原始LP对偶闭合 命中文件数=0    :: 
技术词 高精度对偶方阵 命中文件数=0    :: 
技术词 逐位相同     命中文件数=40   :: ./AUDIT-direction-depth.md ./addmul-defect-test-death.md ./APPRECIATION-AUDIT-2026-09-11.md
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{C-3868}✓✓（\text{现才允许}✓）：(\lambda,\omega)\ \text{比例审计}✓：\ \widehat\mu_q := \lambda_q/\sum_q\lambda_q\ \stackrel{?}{=}\ \mu_q✓✓;\quad \nu \stackrel{?}{=} c_{\mathrm{full}}\,\omega_{\mathrm{KKT}}✓✓$$
$$\qquad \text{若成立} \Longrightarrow \boxed{\text{KKT multiplier geometry} \Longrightarrow \text{Farkas separating certificate}}✓✓\ \text{（\textbf{非}"两个 LP 数字相近"}✗）}$$
$$\textbf{C-3869}✓：\text{二阶敏感度}（\text{唐先生已建议暂缓}✓）$$
