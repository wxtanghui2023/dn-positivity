已查地图：**未覆盖**（所查档：`SOURCE-ALIGNMENT-...md`（C-49）、`ZETA-INSTANTIATION-...md`（C-50）、`E4-palojarvi-finitely-many.md`、`V289`／`V290`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Theorem 4.1`、`formula (36)`、`at most one`、`McCurley`、`anchor`。结论：本档做源文逐字＋ζ 适用性判定）

# Theorem 4.1 逐字 ＋ $K_{F,4}$ = (36) ＋ **$\zeta$ 的适用性判定**（含对我方判断的纠正）

> **任务**：唐先生 2026-09-17 20:42「继续」＝开"Theorem 4.1 逐字"（第 3 项待补）。
> **结果**：① Theorem 4.1 与 $K_{F,4}(\tau)$ 逐字到手 ✓；② **$N$ 的三种情形逐字确认，与我方 E4 档写的完全一致** ✓；③ ⭐ 实例化后**纠正**我方两处判断：**(a) 边际 $R\to1^+$ 不是约束项**（被 $T_0/(e\tau)$ 压住）✗；**(b) 但"至多一个"假设对 $\zeta$ 不成立** ⟹ 准则**不无条件适用于 $\zeta$** ✗✗。

---

## §1 Theorem 4.1（逐字）`[原文]`

> **Theorem 4.1.** Let $\tau>\frac1e$ and $T_0,A_F,B_F,c_{F,j}(T_0),C_{F,j}(T_0)$, $j=1,2,3$, as in condition (c), $K_{F,1}(\tau)$ as in Theorem 2.1 and $K_{F,4}(\tau)$ **as in formula (36)**. Suppose that the function $F(s)$ has **at most one zero $\rho_1$ with $|\frac{\rho_1}{\rho_1-\tau}|>1$**. Furthermore, we also assume that if such a zero $\rho_1$ exists, then $R>1$ is a real number such that $|\frac{\rho_1}{\rho_1-\tau}|\ge R$. Let
> $$N=\Big\lceil\max\Big\{\frac1{e\tau}T_0,\ \exp\big(-W_{-1}\big(-\tfrac{2\log R}3\big)\big),\ \frac{12\log(40(0.5+K_{F,1}(\tau)+K_{F,4}(\tau)))}{\log R}\Big\}\Big\rceil\quad\text{if }R\le e^{\frac3{2e}},$$
> $$N=\Big\lceil\max\Big\{e,\ \frac1{e\tau}T_0,\ \frac{12\log(40(0.5+K_{F,1}+K_{F,4}))}{\log R}\Big\}\Big\rceil\quad\text{otherwise}.$$
> **The zero $\rho_1$ exists if and only if $|\Re(\lambda_F(n,\tau))|\ge(K_{F,1}(\tau)+K_{F,4}(\tau))n\log n$ for at least one integer $n\in[N,5N]$ where $N\mid n$.**

**⟹ 与我方 E4 档对照**：$N$ 的三项公式、窗口 $[N,5N]$、$N\mid n$、阈值 $(K_{F,1}+K_{F,4})n\log n$ —— **全部逐字一致** ✓✓（唯一此前漏掉的是 $R\le e^{3/(2e)}$ 的情形分叉 ✓，现已补）。

## §2 $K_{F,4}(\tau)$ = **formula (36)**（逐字）`[原文]`

$$K_{F,4}(\tau):=2\Big(A_Fe\tau\log(e^2\tau)+|B_F|e\tau+C_{F,1}(T_0)\log(e^2\tau)+\frac{C_{F,2}(T_0)}3+\frac{C_{F,3}(T_0)}{9e\tau}\Big)$$
**⟹ 校正（对我方 C-49 C2）**：$K_{F,4}$ **就在源文**（(36)），我此前记"未见"**系提取不全所致** ✗ —— 现已补齐 ✓。（$K_{F,1}$ 见 Thm 2.1 ✓，$K_{F,4}$ 见 (36) ✓，两者**都显式** ✓✓。）

## §3 $\zeta$ 的完整实例化 `[数值]`（$\tau=1$，$T_0=3.000175\times10^{12}$）

| 量 | 值 |
|:--|:--|
| $A_\zeta$ | $0.159155$ |
| $B_\zeta=-\frac{\log(2\pi e)}{2\pi}$ | $-0.451662$ |
| $C_{\zeta,1},C_{\zeta,2},C_{\zeta,3}$ | $0.14449,\ 3.385,\ 0.2$ |
| $c_{\zeta,1},c_{\zeta,2},c_{\zeta,3}$（由 $N(T,2T)$ 误差，本档估算）| $0.28945,\ 5.020,\ 0.4$ |
| $\mathbf{K_{\zeta,1}(1)}$ | $\mathbf{1.3788}$ |
| $\mathbf{K_{\zeta,4}(1)}$ | $\mathbf{7.0370}$ |
| 阈常数 $K_{\zeta,1}+K_{\zeta,4}$ | $\mathbf{8.4157}$ |
| $40(0.5+K_{\zeta,1}+K_{\zeta,4})$ | $356.63$ |
| $M_\zeta=B_\zeta+\frac{C_{\zeta,1}}e+\frac{C_{\zeta,2}}3+\frac{C_{\zeta,3}}9$ | $\mathbf{0.7520}$ |

**$N$ 的显式值**（$\tau=1$）：

| $R$ | $1/(e\tau)T_0$ | $12\log(40(\cdots))/\log R$ | $\tau/\sqrt{R^2-1}$ | $N$ |
|:--|:--|:--|:--|:--|
| $1+10^{-9}$ | $1.104\times10^{12}$ | $7.05\times10^{10}$ | $2.24\times10^{4}$ | $\mathbf{1.104\times10^{12}}$ |
| $1.01$ | $1.104\times10^{12}$ | $7.09\times10^{3}$ | $7.05$ | $1.104\times10^{12}$ |
| $2$ | $1.104\times10^{12}$ | $1.02\times10^{2}$ | $0.577$ | $1.104\times10^{12}$ |

⭐ **⟹ 纠正我方判断（a）**：我此前（C-46 §5、C-50 §4）把"$R\to1^+\Rightarrow N\ge\tau/\sqrt{R^2-1}\to\infty$"当作瓶颈 ✗ —— **对 $\zeta$ 不成立**：$N$ 被 $T_0/(e\tau)=1.1\times10^{12}$ **恒压住**（直到 $R\lesssim1+10^{-20}$ 才轮到 $\log R$ 项）✓✓。

## §4 ⚠️⚠️ **真正的障碍**：Theorem 4.1 的"至多一个"假设对 $\zeta$ **不成立** `[严格]`

$$\Big|\frac{\rho}{\rho-\tau}\Big|>1\iff\Re(\rho)>\frac\tau2$$
取 $\tau=1$：假设＝"**至多一个零点满足 $\beta>\tfrac12$**" ✗ —— 这**正是 RH 的近邻**，**无条件未知** ✗✗。更一般地 $\tau\in(\frac1e,2)$：假设＝"至多一个零点满足 $\Re\rho>\frac\tau2$"，而条件性已知的是**零密度**型
$$N(\sigma,T)\ll T^{A(1-\sigma)+o(1)}\quad(\text{数值}\gg1\ \text{当 }T\ \text{大})$$
⟹ 该假设**无法由已知无条件结果推出** ✗（**不是**"至多一个"，而是"$\gg1$ 个"的界）。

**源文自己的适用面**（逐字）："These kind of results are known, for example, **for Dirichlet L-functions**, as we have already mentioned (recall results (6),(7))" ✓ —— 即"至多一个零点在某区域外"是**对 Dirichlet $L$（在已知范围内）成立**的 ✓，**不是对 $\zeta$** ✗。

**⟹ 本档最重要的结论**：**准则对 $\zeta$ 不可以无条件使用** ✗✗ —— 不是常数问题、不是 $N$ 太大，而是**核心假设（至多一个例外零点）对 $\zeta$ 无锚** ✓ —— 这与档案 `V289`（合法类无锚／锚定困境）**完全一致** ✓✓。

## §5 对"至多 $m$"扩展线的重新定位 `[严格]`

| 项 | 结论 |
|:--|:--|
| 扩展**目标**（至多一个 ⟹ 至多 $m$） | **正当** ✓（Theorem 4.1 的假设就是"至多一个" ✓）—— 我 C-49 C1 的自我批评**需细化**：错在把引擎定理（Thm 2.3，无此假设）与准则定理（Thm 4.1，有此假设）混谈 ✗，**不在扩展目标本身** ✓ |
| 扩展**用途** | 适用于"**已知 $m$ 界**"的对象（如源文所指的 Dirichlet $L$ 已知范围 ✓）；对 $\zeta$ **仍无锚** ✗ |
| 我方 Li 线（首版论文） | 提供 $\zeta$ 的**无条件** $\lambda_n\ge0$ 至 $n\le2T$ ✓ —— 但那是**另一条**（Li 判据线），与 Thm 4.1 的"至多一个"假设**无关** ✓ |
| ⭐ 综合 | **两条线的交集**＝"若 $\lambda_n$ 的无条件下界能推到 $n\sim2\gamma^2/\delta$，则……" —— 而 $m$ 的锚定问题**独立存在**，无法由 Li 线解决 ✗ |

## §6 边界与待补

- `[原文]` §1／§2（Theorem 4.1、formula (36)）逐字取自本地 PDF ✓；§1 的 $N$ 公式与本档核对**逐字一致** ✓。
- `[数值]` §3 表为实际计算（mpmath dps=20）✓；$c_{\zeta,j}$ 为**估算**（由 $|S(T)|$ 界加倍）⟹ $K_{\zeta,1}$ 的次项**待独立核实** ⚠️。
- `[严格]` §4 的等价 $|w|>1\iff\Re\rho>\tau/2$ 是源文 (a) 前后的已知式 ✓；"$N(\sigma,T)\gg1$"为经典事实 ✓。
- **待补**：① $c_{\zeta,j}$ 逐字出处（(4) 式对 $\zeta$）✗；② Theorem 3.1／3.3 逐字（非等价条件那条线）✗；③ 按 C-49 重写 C-46／C-47 ✗。
- **不声称**：不证 RH；**不声称**准则可用于 $\zeta$ ✗；不修改任何原档 ✓。
