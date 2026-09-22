已查地图（**先查后写**）：`C3889`（**L0 定位：T1a 活／T1b 排除；矩空间嵌入** ✓✓）、`C3862`（**POLISH＋A1–A5；4 条偶频取等＋tie** ✓✓）、`C-3870`（**`c_* = 1/L`；六活跃方阵** ✓✓）、`C-380-26`（**two-level 模型；`(m,a) = (-0.25, 0.5592)`** ✓✓）、`C-380-45`（**`Q_1 = 4m`；边界点 `(-1/8, 7/16)`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-96：C-3890 —— 等式化门槛审计 ＋ T-system 回溯测试（two-level 已知结果）**（唐先生 2026-09-22 08:59 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 唐先生重排顺序（}\textbf{采纳}✓✓**）：\text{六门之中}\ \textbf{先做"能否重述为标准矩空间问题的边界"}✓✓,\ \textbf{而非}先查 T-system✗$$

$$\qquad \text{理由（唐先生）}✓✓：\text{经典 T-system／矩空间理论}\ \textbf{几乎全建立于}\ \textbf{等式约束}✓;\ \text{而 C-380 的}\ Q_1,\dots,Q_4 \le -\tfrac12\ \text{是}\ \textbf{不等式}✗,\ Q_5\ \text{是被优化目标}✓✓$$

$$\textbf{② ⭐ 等式化门槛：}\boxed{\textbf{有条件通过}}✓✓$$

$$\qquad \text{约束}\ \textbf{确实是不等式}✗;\ \text{但}\ \textbf{在极值点处它们变成等式}✓✓\ \text{（}\text{我们自己的}\ C\text{-}3862\ \text{已证}✓：$$

$$\qquad \qquad F_6 = F_8 = F_{14} = F_{18} = \tfrac12✓（\text{4 条偶频取等}✓）;\qquad F_{13} + F_{19} = 0✓（\text{tie}✓）$$

$$\qquad \Longrightarrow \boxed{\text{经典（等式型）矩空间理论}\ \textbf{只在极值点处适用}}✓✓ \Longrightarrow \textbf{范围条件}\ \text{须显式登记}✓✓$$

$$\textbf{③ ⚠️ 定理引用更正（我上一档引错}✗✓**）：\text{该用的}\ \textbf{不是}\ "principal representation 支撑}\ \le \lceil(n+1)/2\rceil\text{"}✗✓$$

$$\qquad \textbf{而是}✓✓：\boxed{\text{极值测度支撑} \subseteq \text{最小化多项式 } p \text{ 的零点集} \Longrightarrow \operatorname{supp} \le \deg p}✓✓$$

$$\qquad \text{本例}✓：p = \omega_{13}T_{13} + \omega_{19}T_{19} + \sum_{q \in \mathcal A}\lambda_qT_{2q}✓ \Longrightarrow \deg p \le 36✓✓ \Longrightarrow \boxed{\operatorname{supp} \le 36}\ ✗\ \textbf{完全无用}✗✓$$

$$\textbf{④ ⭐ 回溯测试（唐先生方案}✓✓**）：\text{用 T-system 框架倒推已证的 two-level}✓$$

$$\qquad \textbf{成功的一面}✓✓：\text{已知边界点}\ (m,s) = (-\tfrac18, \tfrac{7}{16})✓,\ a = \tfrac{3\sqrt3}{8}✓；\ \text{支撑值}\ y_{1,2} = m \pm a✓ \Longrightarrow$$

$$\qquad \qquad y_1y_2 = m^2 - a^2 = \mathbf{-\tfrac{13}{32}}✓,\qquad y_1 + y_2 = 2m = \mathbf{-\tfrac14}✓✓ \Longrightarrow$$

$$\qquad \qquad \boxed{p_2(y) = y^2 + \tfrac14y - \tfrac{13}{32}}✓✓\ \text{的零点}\ \textbf{恰为两个支撑值}✓✓ \Longrightarrow \textbf{短证书存在（两行）}✓✓$$

$$\qquad \qquad \text{且}\ p_2 = \tfrac12T_2 + \tfrac14T_1 + \tfrac12T_0 - \tfrac{13}{32}✓ \Longrightarrow \boxed{\textbf{次数 2 的 Chebyshev-张量元}}✓✓$$

$$\qquad \textbf{失败的一面}✗✓：\text{经典定理}\ \textbf{不能} \text{从约束结构}\ \textbf{推出} \text{该答案}✗；\ \text{次数界}\ 36 \gg 2✗；\ \text{Carathéodory 数给}\ \textbf{下界} \text{（方向相反）}✗✓$$

$$\qquad \Longrightarrow \text{回溯测试}\ \textbf{只能事后认证、不能前置推导}✗✓ \Longrightarrow \text{按唐先生判据：}\textbf{信号混合}⚠️✓$$

$$\textbf{⑤ T1 边界再精化}✓✓：$$

$$\qquad \textbf{T1a-}\beta\ \textbf{（值得小探针}✓**）：\boxed{\text{约束张量中是否存在}\ \textbf{低次} \text{消失元（零点 ⊇ 支撑、且}\ \textbf{零点数} \le 2\text{）}}✓✓$$

$$\qquad \textbf{T1b（排除，已确认}✗**）：\text{边界／principal 支撑下降}✗；\qquad \textbf{泛型支撑计数（排除}✗）：\lceil(n+1)/2\rceil\ \text{与 supp} \le \deg p\ \text{两条}\ \textbf{都给不出}\ 2✗✓$$

$$\textbf{⑥ 数值核验（本档）}✓✓：s = m^2 + a^2\ \text{✓}；p\ \text{展开＝}y^2 + y/4 - 13/32\ \text{✓}；\ \text{两零点}\ \in[-1,1]\ \text{✓}✓$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 方法论价值（✓✓）

$$\textbf{便宜且信息量大}✓✓：\text{回溯测试成本极低（答案已知）}✓,\ \text{但立刻暴露了}\ \textbf{经典界的量级错配（36 vs 2）}✓✓ \Longrightarrow \textbf{避免系统性学习整门理论却换不来所需界}✓✓$$

$$\qquad \Longrightarrow \text{这正是唐先生原则的应验}✓✓：\boxed{\text{先用最便宜的方式验证连接是否真实，再决定是否系统投入}}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 等式化门槛（先做的第一件事） ✓ | **有条件通过（仅极值点处）** ✓✓ |
| 经典定理引用 ✓ | **已更正（minimizing polynomial，非 principal）** ✓✓ |
| 回溯测试 ✓ | **混合：短证书成功／前置推导失败** ⚠️✓ |
| `p_2(y) = y^2 + y/4 - 13/32` ✓ | **显式得到并核验** ✓✓ |
| T1a-β（低次消失元） ✓ | **值得小探针** ✓✓ |
| T1b／泛型支撑计数 ✓ | **排除** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 T-system 理论已套用成功 ✓
- **不**声称回溯测试通过（它只给事后认证）✓
- **不**把 `p_2` 当作"经典定理推出的结果"（它是我从已知答案**构造**的）✓✓
- **不**声称 `\operatorname{supp} \le 36` 型界有用 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}修数学（除核验）✗；\ \textbf{不}发候选✗；\ \textbf{不}开四轨计算✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 等式化门槛  命中文件数=0    :: 
技术词 回溯测试     命中文件数=0    :: 
技术词 低次消失多项式 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① T1a-}\beta\ \textbf{小探针}✓✓：\text{在约束张量}\ \operatorname{span}\{T_{13},T_{19},T_{12},T_{16},T_{28},T_{36}\}\ \text{中求}\ \textbf{低次} \text{消失元}✓（\text{条件：零点} \supseteq \text{支撑}✓,\ \text{不同零点} \le 2✓）✓✓$$
$$\qquad \text{成本}✓：\text{线性代数 ＋ 根计数}✓,\ \textbf{无需} \text{学完整门理论}✓✓$$
$$\textbf{② M0 收尾}✓：\text{奇偶族 T-system 逐字判别 ＋ 精确定理号定位}✓$$
$$\textbf{③ T2／T3}✓：\text{按 } C3889\ \text{登记推进}✓✓$$
