已查地图：**未覆盖**（所查档：`SOURCE-ALIGNMENT-palojarvi-verbatim-...md`（C-49）、`E4-palojarvi-finitely-many.md`、`PAPER-v1-li-explicit-range.md`、`RIGORIZATION-*`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`(a)-(d)`、`Selberg class`、`Trudgian`、`A_F`、`C_{F,j}`、`Riemann zeta satisfies`。结论：本档做**源文实例化**，不新增路线）

# 任务 2：$\zeta$ 的实例化 —— 源文 (a)–(d) 逐条核对 ＋ 常数 $A_\zeta,B_\zeta,C_{\zeta,j}$

> **任务**：唐先生 2026-09-17 20:40「2」＝核 $\zeta$ 是否满足 (a)–(d) 及实例化常数。
> **结论**：**源文自己回答了这个** ✓✓ —— 原话："**The previous conditions are not very restrictive. For example, the Riemann zeta function satisfies these conditions. Furthermore, all Selberg class functions also satisfy these conditions**" ✓；并给出 Dirichlet $L$ 的**显式实例化 (38)** ✓。**故准则对 $\zeta$ 可落地** ✓（但见 §4 瓶颈）。

---

## §1 源文 (a)–(d) 四条（逐字）`[原文]`

| 条 | 逐字要点 |
|:--|:--|
| **(a)** | "Location of the zeros, 1: $F(s)$ does not have zeros $\rho$ with $\Re(\rho)>\tau$." |
| **(b)** | "Location of the zeros, 2: $F(s)$ does not have a zero $\rho=\tau$." |
| **(c)** | 计数：$|N_F(T)-A_FT\log T-B_FT|<C_{F,1}(T_0)\log T+C_{F,2}(T_0)+\frac{C_{F,3}(T_0)}T$ $(T\ge T_0)$ **(3)**；另有 $N_F(T,2T)$ 版本 **(4)** |
| **(d)** | "**Computation**: The numbers $\lambda_F(n,\tau)$ can be computed **without knowing the zeros** of $F(s)$." ＋ 源文注："**The previous conditions are not very restrictive. For example, the Riemann zeta function satisfies these conditions. Furthermore, all Selberg class functions also satisfy these conditions**" ✓✓ |

**源文对 $\tau=1,\ \zeta$ 的 (d) 实例（逐字）**：
$$\lambda_\zeta(n,1)=\frac1{(n-1)!}\frac{d^n}{ds^n}\big[s^{n-1}\log\xi(s)\big]_{s=1},\qquad \xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$$
（引 [10]）✓ —— 即 $(\mathrm{d})$ 对 $\zeta$ **有显式可计算形式** ✓。

---

## §2 $\zeta$ 的 (a)(b)(c) 逐条核对 `[引用]`

| 条 | $\zeta$（取 $\tau=1$） | 依据 |
|:--|:--|:--|
| **(a)** | $\zeta$ 在 $\Re s>1$ 无零点 ✓ | Euler 积（经典 ✓）|
| **(b)** | $\zeta(1)\ne0$（极点，非零点）✓ | 经典 ✓ |
| **(d)** | ✓ 见 §1（源文点名 ✓）| `[原文]` |
| **(c)** | $A_\zeta=\frac1{2\pi}$、$B_\zeta=-\frac{\log(2\pi e)}{2\pi}$（因 $N_\zeta(T)=\frac T{2\pi}\log\frac T{2\pi e}+\frac78+S(T)$）✓ | Riemann–von Mangoldt ✓ |
| (c) 误差项 | 由 $|S(T)|$ 显式界给出：$|S(T)|\le0.112\log T+0.278\log\log T+2.510+0.2/T$ ⟹ 取 $T_0$ 后把 $\log\log$ 并入 $\log T$：$C_{\zeta,1}\approx0.112+\frac{0.278\log\log T_0}{\log T_0}$，$C_{\zeta,2}\approx2.510+\frac78$，$C_{\zeta,3}\approx0.2$ | `[引用]` Trudgian 型 ✓ |

**$T_0=3.000175\times10^{12}$ 时的具体数**：$\log T_0\approx28.71$、$\log\log T_0\approx3.357$ ⟹ $C_{\zeta,1}\approx0.112+0.278\cdot\frac{3.357}{28.71}\approx\mathbf{0.1445}$，$C_{\zeta,2}\approx\mathbf{3.385}$，$C_{\zeta,3}\approx\mathbf{0.2}$ ✓ `[数值]`

**源文对 Dirichlet $L$ 的现成实例（逐字 (38)）**：$T\ge1$
$$\Big|N_F(T)-\frac T\pi\log T-\frac T\pi\log\frac q{2\pi e}\Big|<0.317\log T+0.317\log q+6.401$$
⟹ $A_F=\frac1\pi,\ B_F=-\frac1\pi\log\frac q{2\pi e},\ C_{F,1}=0.317,\ C_{F,2}=0.317\log q+6.401,\ C_{F,3}=0$ ✓✓ —— **这是源文自己对 (c) 的实例化** ✓（$q$ 为模）✓。

---

## §3 代入后的显式常数 `[数值]`

$M_F:=B_F+\frac{C_{F,1}}e+\frac{C_{F,2}}3+\frac{C_{F,3}}9$（源文 Thm 2.3 逐字 ✓）⟹ 对 $\zeta$（$T_0$ 如上）：
$$M_\zeta\approx-0.2651+\frac{0.1445}{2.7183}+\frac{3.385}{3}+\frac{0.2}{9}\approx-0.2651+0.0532+1.1283+0.0222\approx\mathbf{0.9386}$$
$$K_{\zeta,1}(\tau)=\frac{2\tau}3\Big(e+\frac1e\Big)\big(A_\zeta+|A_\zeta\log(8e\tau)+B_\zeta|\big)+\frac4{27}\Big(1+\frac1{e^2}\Big)\Big(\frac{c_{\zeta,1}}{3\log2}+c_{\zeta,1}\log(e^2\tau)+c_{\zeta,2}+\frac{2c_{\zeta,3}}{7e\tau}\Big)$$
（$\tau=1$：$A_\zeta=0.15915$、$|A_\zeta\log(8e)+B_\zeta|\approx|0.15915\cdot3.0820-0.26505|\approx0.2255$ ⟹ 首项 $\approx1.2710\cdot(0.15915+0.2255)\approx\mathbf{0.489}$；次项含 $c_{\zeta,j}$（$=c_{F,j}$ 的 $N(T,2T)$ 版本，本档**未提取** ✗）⟹ $K_{\zeta,1}(1)$ 的**第二项待补** ⚠️。）

**准则形式（$m'$ 无关，见 C-49 C1 ✓）**：
$$\exists n\in[N,\ 5N\cdot2(A_\zeta\log N+M_\zeta)],\ N\mid n:\quad \Re\lambda_\zeta(n,\tau)<\sum_{|\Im\rho|\le N}1-\tfrac1{20}R^n$$
$$N\ \ge\ \Big\lceil\max\Big\{e,\ T_0,\ \tfrac{\tau}{\sqrt{R^2-1}},\ e^{(1-15M_\zeta)/(15A_\zeta)}\Big\}\Big\rceil\qquad(T_0=3.000175\times10^{12}\ \text{可直接用 ✓})$$

---

## §4 ⚠️ 落地后的**真实瓶颈**（本档判断）

1. **$\tau$ 的选取**：例外集＝$\{\Re\rho>\tau/2\}$ ✓ —— 取 $\tau=1$ 时＝"$\beta>\tfrac12$ 的零点" ✓；$\beta<\tfrac12$ 由函数方程配对覆盖 ✓（$\zeta(\rho)=0\Leftrightarrow\zeta(1-\rho)=0$ ✓）。
2. **瓶颈＝$N\ge\frac{\tau}{\sqrt{R^2-1}}$** ✗：要检测**任意**离轴零点需 $R\to1^+$ ⟹ $N\to\infty$ ✗ —— 与 C-46 §5 的循环点**同址** ✓（源文亦然，这正是其 Thm 4.1 需"至多一个"类假设的原因 ✓）。
3. **换言之**：实例化后准则**可用** ✓（$T_0$ 现成、$A_\zeta,B_\zeta,C_{\zeta,1..3}$ 可算 ✓），但**"检测边际离轴零点"所需的 $n$ 仍无界** ✗ —— 这是**唯一的**卡点，且已定位清楚 ✓。

---

## §5 边界与待补

- `[原文]` §1 四条、(d) 的 $\zeta$ 实例、$(38)$、$M_F$、Thm 2.3 的 $N$ 下界均逐字取自本地 PDF ✓。
- `[引用]` $|S(T)|$ 显式界（Trudgian 型）；Riemann–von Mangoldt ✓；Euler 积 ✓ —— **未逐行复核** ⚠️。
- **待补（本档未做）**：① $c_{\zeta,j}$（即 (4) 式 $N(T,2T)$ 版本常数）⟹ $K_{\zeta,1}(1)$ 第二项 ✗；② $K_{F,4}$ 在源文中的**确切出处**（C-49 C2 已记其未见 ✗）；③ Theorem 4.1 逐字（"at most one"那条线）✗；④ 按 C-49 的源文机制**重写** C-46／C-47 ✗。
- 未使用 RH；未使用零点位置；不修改任何原档 ✓。
