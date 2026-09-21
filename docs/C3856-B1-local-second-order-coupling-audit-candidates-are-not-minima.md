已查地图（**先查后写**）：`C-3855`（**A：内部极值信号；`\gamma^{(13)} \le 0.876`** ✓✓）、`C-3854`（**靶与硬门槛** ✓✓）、`C-3853`（**退化轨迹已封** ✓✓）、`C-3850`（**`0.876069` 候选点** ✓✓）、`C-380-13`（**线性对偶封口** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-56：B1 —— 内部极值的局部二阶耦合审计（只做局部，不开全局证书）**（唐先生 2026-09-21 22:11 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 档位}✓✓：\text{只做}\ \textbf{局部一／二阶展开}✓✓；\ \textbf{不开} \text{Fejér／Chebyshev 全局证书工程}✗✓（遵令）$$

$$\textbf{② ⭐ 精确一／二阶恒等式（}\phi\ \textbf{坐标）}✓✓：\text{记}\ c_j = \cos\phi_j✓,\ x_j = c_j^2✓,\ \gamma_j = 1\ (\text{偶})／\sigma_j\ (\text{奇})✓ \Longrightarrow$$

$$\qquad F_k(\phi) = \sum_j \gamma_j\cos(k\phi_j)✓✓ \Longrightarrow \boxed{\partial_{\phi_j}F_k = -k\gamma_j\sin(k\phi_j)}✓✓,\qquad \boxed{\partial^2_{\phi_j\phi_l}F_k = -k^2\gamma_j\cos(k\phi_j)\,\delta_{jl}}✓✓$$

$$\qquad \Longrightarrow \boxed{F_k(\phi+h) = F_k - k\sum_j\gamma_j\sin(k\phi_j)h_j - \frac{k^2}{2}\sum_j\gamma_j\cos(k\phi_j)h_j^2 + O(\|h\|^3)}✓✓$$

$$\qquad \Longrightarrow\ \textbf{所有}\ F_k\ \text{的 Hessian 在}\ \phi\ \text{坐标下}\ \textbf{对角}✓✓\ \text{（可分离}✓） \Longrightarrow \text{二阶结构}\ \textbf{完全显式}✓✓\ \text{（\textbf{不用}数值 Hessian}✗✓）$$

$$\textbf{③ ⭐⭐ 审计结果（本档核心，两个候选点）}✓✓$$

$$\qquad \textbf{候选 1}✓（`C-3850`，g = 0.876069）：\text{偶频余量全部} > 0✓；\ \text{近 binding 集} = \{(3,\ 1.54\times10^{-4}),\ (4,\ 1.37\times10^{-3}),\ (9,\ 1.21\times10^{-2})\}✓✓$$

$$\qquad \qquad \text{active 奇频：}\sigma^* = (-1,1,1,-1,1)✓,\ r^* = 6✓（\text{频率}\ 13✓）;\qquad \boxed{\|\nabla F_{\text{odd}}\| = 20.73}✓✓$$

$$\qquad \textbf{候选 2}✓（`C-3855` 细调，g = 0.9878）：\text{近 binding 仅}\ \{(4,\ 7.25\times10^{-3})\}✓;\ \ r^* = 11✓（\text{频率}\ 23✓）;\qquad \boxed{\|\nabla F_{\text{odd}}\| = 41.82}✓✓$$

$$\qquad \Longrightarrow\ \textbf{两候选的全部偶频余量}\ > 0✓ \Longrightarrow \text{一阶扰动}\ \textbf{全部可行}✓✓ \Longrightarrow \boxed{\text{存在一阶改善的可行方向}}✓✓ \Longrightarrow \boxed{\textbf{两个候选都不是局部极小}}✓✓$$

$$\qquad \Longrightarrow\ \boxed{0.876\ \textbf{只是上界，不是}\ \inf}✓✓\ \text{（\textbf{重要更正}：}\gamma^{(13)}\ \text{的真值}\ < 0.876\ \text{极可能}✓）$$

$$\textbf{④ KKT 检验}✓✓：\text{用近 binding 偶频梯度试解}\ \nabla F_{\text{odd}} + \sum_r\lambda_r\nabla F_{2r} = 0✓ \Longrightarrow \text{残差}\ = 20.03／41.80✓✓ \Longrightarrow \textbf{两候选都不是 KKT 点}✗✓$$

$$\textbf{⑤ 机制的正确提法（本档修正）}✗✓：\text{唐先生的"奇频一阶} \Rightarrow \text{偶频二阶成本"，其检验对象}\ \textbf{必须} \text{是}\ \textbf{KKT 点}✓✓；\ \text{在非极小点上检验}\ \textbf{不合法}✗✓$$

$$\qquad \Longrightarrow\ \boxed{\text{不判"该局部机制不足"}}✓✓\ \text{（因为检验对象无效}✓） \Longrightarrow\ \text{下一刀}\ = \textbf{求 KKT 点}✓✓$$

$$\qquad \textbf{KKT 系统（有限代数）}✓✓：\ \boxed{\nabla F_{2r^*+1} + \sum_{r \in \mathcal A}\lambda_r\nabla F_{2r} = 0✓,\quad \lambda_r \ge 0✓,\quad F_{2r} = \tfrac12\ (r \in \mathcal A)}✓✓$$

$$\textbf{⑥ 二阶成本的精确形式（可直接检验）}✓✓：\text{偶频}\ F_{2r}\ \text{沿}\ h\ \text{的二阶变化} = -\frac{(2r)^2}{2}\sum_j\cos(2r\phi_j)h_j^2✓✓$$

$$\qquad \Longrightarrow\ \text{要}\ \textbf{消耗}\ F_{2r}\ \text{的余量（即抬升}\ F_{2r}\text{）}\ \text{须}\ \boxed{\sum_j\cos(2r\phi_j)h_j^2 < 0}✓✓\ \text{—— 一个}\ \textbf{显式二次型条件}✓✓$$

$$\textbf{⑦ 结构观察（登记）}✓✓：\text{候选 1 的近 binding 集是}\ \{3,4,9\}✓、\ \textbf{不是单一}\ F_8✗✓ \Longrightarrow \text{与唐先生"不要假定}\ F_8\ \text{唯一 active"的纪律}\ \textbf{一致}✓✓；$$

$$\qquad \Longrightarrow\ \text{真极值的 active 集}\ \textbf{预期含多个偶频}✓✓ \Longrightarrow \text{KKT 系统应为}\ \textbf{多约束平衡}✓✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
候选1（C-3850 点 x = [0.801874,0.561119,0.703473,0.627211,0.869546]）：
   g = 0.876060 ; sigma* = [-1,1,1,-1,1] ; r* = 6（频率 13）
   偶频余量 = [3.1879, 1.0435, 0.000154, 0.001372, 0.031594, 1.860644, 0.03909, 0.376705,
               0.012103, 1.034159, 0.159045, 1.837178]
   近 binding（<0.02）= r=3 (1.54e-4), r=4 (1.37e-3), r=9 (1.21e-2) ; min margin = 1.54e-4
   grad F_odd（phi 坐标）= [-3.6709, -0.1448, -12.1296, 10.0751, 12.9455] ; ||grad|| = 20.73
   KKT 试解（用 r=3,4,9 的梯度）：lambda = [0.0855, 0.3666, 0.0378]，残差 20.03
候选2（C-3855 细调点）：
   g = 0.987800 ; sigma* = [-1,-1,1,-1,1] ; r* = 11（频率 23）
   近 binding = r=4 (7.25e-3) ; ||grad F_odd|| = 41.82 ; KKT 试解 lambda = [-0.1086]（负 ⟹ 不合法），残差 41.80
```
- 脚本 ✓：`scripts/c380_56_B1_local_coupling.py`✓；输出 ✓：`scripts/out_c380_56_B1.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 精确一/二阶恒等式 ✓ | **完成（Hessian 对角）** ✓✓ |
| 候选 1／2 的偶频余量表 ✓ | **完成（多频率近 binding）** ✓✓ |
| 候选是否局部极小 ✓ | **否（一阶改善可行方向存在）** ✗✓ |
| `0.876` 的地位 ✓ | **上界（非 inf）—— 更正** ✓✓ |
| KKT 点 ✓ | **未找到（下一刀目标）** ✗✓ |
| 局部二阶机制 ✓ | **未判定（检验对象无效）** ⚠️✓ |
| 全局证书工程 ✓ | **未开（遵令）** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 `\gamma^{(13)}` 的极值点已定位（本档只做局部审计）✓
- **不**声称局部二阶机制成立或不成立（须在 KKT 点上检验）✓
- **不**把 `\|\nabla F_{\text{odd}}\|` 的大小解释为"机制失效"✓
- **不**用数值 Hessian 作为证明（只用精确恒等式）✓

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 局部二阶耦合 命中文件数=0    :: 
技术词 KKT平衡        命中文件数=0    :: 
技术词 对角Hessian    命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{B1-}\alpha✓：\ \textbf{求 KKT 点}✓✓：\text{解}\ \nabla F_{2r^*+1} + \sum_{r \in \mathcal A}\lambda_r\nabla F_{2r} = 0✓,\ \lambda \ge 0✓,\ F_{2r} = \tfrac12✓\ \text{（有限代数}✓，可用 Newton ＋多起点}✓）$$
$$\textbf{B1-}\beta✓：\ \text{在 KKT 点上检验}\ \textbf{二阶耦合}✓✓：\text{奇频改善方向}\ h\ \text{是否必然满足}\ \sum_j\cos(2r\phi_j)h_j^2 < 0✓✓\ \text{（即抬高某偶频}✓）$$
$$\textbf{B1-}\gamma✓：\ \text{若}\ \beta\ \text{给出正二阶成本}\ \Longrightarrow\ \text{继续局部定量化}✓；\ \text{若成本可被一阶方向消掉}\ \Longrightarrow\ \text{判该局部机制不足}✓✓\ \text{（唐先生规则}✓）$$
