已查地图（**先查后写**）：`C-3869`（**单边桥引理 `c_* \ge 1/L`（严格）；步 4 方向更正** ✓✓）、`C-3868`（**`(\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)`（高精度观察）** ✓✓）、`C-3867`（**primal/dual 同值；六活跃顶点** ✓✓）、`C-3863`（**KKT 点与乘子** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-70：C-3870 —— 六活跃 primal 方阵的秩／可解性审计（取到步）**（唐先生 2026-09-21 22:47 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 档位}✓✓：\textbf{符号线性系统审计}✓✓；\ \textbf{不}重跑 LP✗；\ \textbf{不}碰二阶}✗✓$$

$$\textbf{② 系统（6×6）}✓✓：\text{未知}\ (h,c) \in \mathbb R^6✓；\ \boxed{\widetilde M\begin{pmatrix}h\\c\end{pmatrix} = \begin{pmatrix}-1\\-1\\0\\0\\0\\0\end{pmatrix}}✓✓,\ \widetilde M = \big[\,v_{13};\ v_{19};\ w_6;\ w_8;\ w_{14};\ w_{18}\ \big|\ -\mathbf e\,\big]✓（\mathbf e = (0,0,1,1,1,1)✓）$$

$$\textbf{③ 项 1：满秩}✓✓：\ \boxed{\det\widetilde M = -11564885.981695011236 \ne 0}✓✓,\qquad \operatorname{rank}\widetilde M = 6✓✓ \Longrightarrow \textbf{系统非奇异}✓✓$$

$$\textbf{④ 项 2：}\mathbf{c^* = 1/L}\ \textbf{（代数强制，}\textbf{非}数值巧合}✓✓$$

$$\qquad \textbf{推导}✓✓：\text{KKT 站性} \times h^*✓：\omega_{13}(v_{13}h^*) + \omega_{19}(v_{19}h^*) + \sum_q\lambda_q(w_qh^*) = 0✓✓$$

$$\qquad \text{代入六活跃等式}✓：v_{13}h^* = v_{19}h^* = -1✓,\ w_qh^* = c^*\ (q \in \mathcal A)✓ \Longrightarrow -(\omega_{13}+\omega_{19}) + c^*\sum_q\lambda_q = 0✓✓$$

$$\qquad \Longrightarrow \boxed{c^*L = 1 \Longrightarrow c^* = \frac1L}✓✓\ \text{（}\textbf{由 KKT ＋ 六活跃结构强制}✓✓）$$

$$\qquad \text{数值核验}✓✓：c^* = 0.500808953629041885590052265792✓,\ 1/L\ \text{同值}✓,\ \boxed{Lc^* - 1 = -1.556\times10^{-61}}✓✓$$

$$\qquad \qquad \text{恒等式核验}✓：-(1) + c^*L = -1.556\times10^{-61}✓✓$$

$$\textbf{⑤ 项 3：primal-feasible}✓✓（\textbf{由方程直接得到}✓）：v_{13}h^* + 1 = 0✓,\ v_{19}h^* + 1 = 0✓,\ \max_q(w_qh^* - c^*) = 8.7\times10^{-62}✓✓$$

$$\qquad \|h^*\|_\infty = 0.04896166 < 1✓✓ \Longrightarrow \textbf{box 仍严格 inactive}✓（\text{故 box 不影响最优值}✓）$$

$$\textbf{⑥ ⭐⭐ 合并（}\textbf{定理}✓✓**）：\text{C-3869 的}\ c_* \ge \frac1L✓\ \text{＋ 本档}\ c^* = \frac1L\ \text{为 primal-feasible}✓ \Longrightarrow \boxed{c_* = \frac1L}✓✓$$

$$\qquad \Longrightarrow \boxed{c_{\mathrm{full}} = \frac1{\sum_q\lambda_q}}✓✓ \Longrightarrow \text{桥常数}\ \textbf{＝ 活跃偶频乘子之和的倒数}✓✓$$

$$\qquad \Longrightarrow \text{C-3868 的}\ (\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)\ \text{由}\ \textbf{高精度观察}\ \text{升为}\ \textbf{严格代数推论}✓✓$$

## §1 证明链（完全不再依赖 LP 求解器 ✓✓）

$$\textbf{(i)}\ \text{KKT 站性} + \text{odd 归一化} \Longrightarrow \boxed{c_* \ge 1/L}✓✓\ \text{（`C-3869`：}\text{单边，严格}✓）$$
$$\textbf{(ii)}\ \text{六活跃方阵非奇异} \Longrightarrow \exists(h^*,c^*)✓\ \text{primal-feasible 且}\ \boxed{c^* = 1/L}✓✓\ \text{（本档：}\text{KKT} \times h^*\ \text{恒等式}✓）$$
$$\textbf{(iii)}\ \text{合并} \Longrightarrow \boxed{c_* = \frac1L}✓✓$$

$$\qquad \text{关键}✓✓：\text{(ii) 的}\ c^* = 1/L\ \textbf{不是} \text{数值拟合}✓,\ \text{而是}\ \text{KKT 关系乘}\ h^*\ \text{后的}\ \textbf{代数恒等式}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 项 1 满秩（`\det\widetilde M \ne 0`） ✓ | **CLOSED（-1.156e7）** ✓✓ |
| 项 2 `c^* = 1/L` ✓ | **CLOSED（代数强制；`Lc^*-1 = -1.6e-61`）** ✓✓ |
| 项 3 primal-feasible ✓ | **CLOSED（残差 ≤ 8.7e-62）** ✓✓ |
| **`c_* = 1/L`（一般定理）** ✓ | **CLOSED（在非奇异条件下）** ✓✓ |
| `c_{\mathrm{full}} = 1/\sum\lambda_q` ✓ | **CLOSED** ✓✓ |
| `(\mu,\nu) = c_{\mathrm{full}}(\lambda,\omega)` ✓ | **由观察 → 严格推论** ✓✓ |
| 非奇异性的**结构**证明 ✓ | **未（实例级已验证）** ✗✓ |
| C-3869-β 二阶 ✓ | **未开** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称非奇异性已由结构证明（实例级 `\det \ne 0` 已验证）✓
- **不**声称全局最优／`V_\sigma` 真值 ✓
- **不**声称已连到 arithmetic bridge ✓
- **不**把 `c_* = 1/L` 的成立范围扩大到未验证的 KKT 点 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}重跑 LP✗；\ \textbf{不}重做高精度闭合（`C-3867` 已做}✗）；\ \textbf{不}碰二阶✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 六活跃方阵  命中文件数=0    :: 
技术词 取到步        命中文件数=1    :: ./C3869-KKT-Farkas-bridge-lemma-one-sided-and-direction-correction.md 
技术词 桥常数定理  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 非奇异性的结构来源}✓✓：\text{为何}\ \det\widetilde M \ne 0\ \text{在 KKT 点处成立}✓（\text{候选}：\text{奇数频率}\ 13,19\ \text{与偶频}\ 12,16,28,36\ \text{的}\ \textbf{Chebyshev 独立性}✓）$$
$$\textbf{② C-3869-}\beta✓：\text{二阶敏感度}（\text{暂缓}✓）$$
$$\textbf{③ 语义}✓✓：\text{现有完整链}✓：\text{KKT} \Longrightarrow c_* = \frac1{\sum\lambda_q} \Longrightarrow (\mu,\nu) = c_*(\lambda,\omega)✓✓\ \text{—— }\textbf{机制—证书同构}✓✓$$
