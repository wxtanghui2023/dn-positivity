已查地图：**未覆盖**（所查档：`E4-palojarvi-finitely-many.md`、`E4-STATUS-AUDIT-...md`、`E4-ENGINE-1..5`、`C-46`／`C-47` 两份严格化、`V290`／`V291`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Theorem 2.3`、`K_{F,1}`、`M_F`、`at most one`、`至多 m`、`Lemma 2.2`。结论：本档做**源文逐字对齐**，含对既有框架的结构性校正）

# 源文逐字对齐（Palojärvi arXiv:1807.01506v3）：Theorem 2.1／2.3 的**真实**引擎结构 —— 与我方"至多 $m$"框架的差异

> **任务**：唐先生 2026-09-17 20:34「继续严格化，这个有限离轴零点的价值比我们其它研究成果更高」。
> **本档内容**：本地从 `docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf`（26 页）**逐字提取**，做 6 项校正 —— 其中 **(C1) 是结构性的**：我此前的"至多 $m$ 个例外"框架**不是**源文的引擎结构 ✗。

---

## §1 源文假设 (a)–(d)（逐字）`[原文]`

> "(a) **Location of the zeros, 1**：The function $F(s)$ does not have zeros $\rho$ with $\Re(\rho)>\tau$.
> (b) **Location of the zeros, 2**：The function $F(s)$ does not have a zero $\rho=\tau$.
> (c) **Number of the zeros**：Let $N_F(t)$ denote the number of the zeros $\rho$ of $F(s)$ with $0\le\Re(\rho)\le\tau$ and $0\le|\Im(\rho)|\le t$；similarly $N_F(t_1,t_2)$ … For some real numbers $A_F>0$ and $B_F$ and for a real number $T_0>0$ which is large enough：
> $$|N_F(T)-A_FT\log T-B_FT|<C_{F,1}(T_0)\log T+C_{F,2}(T_0)+\frac{C_{F,3}(T_0)}{T}\quad(T\ge T_0)\ (3)$$
> $$|N_F(T,2T)-A_FT\log T-(A_F\log4+B_F)T|<\dots\ (4)$$"

**⟹ 校正 C2**：常数记号是 $A_F,B_F,C_{F,j}(T_0),c_{F,j}(T_0)$，**不是我方文档写的 $K_{F,1},K_{F,4}$**（$K_{F,1}$ 是 Theorem 2.1 **推出的**界常数，$K_{F,4}$ 在本档提取范围内**未出现** ✗）⟹ 我方记号需重贴 ✗。

---

## §2 Theorem 2.1（逐字，$K_{F,1}$ **显式**）`[原文]`

> **Theorem 2.1.** Let $\tau>\frac1e$ and $T_0,A_F,B_F,c_{F,j}(T_0)$ ($j=1,2,3$) as in (c). Assume $n\ge\max\{e,\frac1{e\tau}T_0\}$ and $T(n):=ne\tau$. Furthermore let
> $$K_{F,1}(\tau):=\frac{2\tau}{3}\Big(e+\frac1e\Big)\big(A_F+|A_F\log(8e\tau)+B_F|\big)+\frac4{27}\Big(1+\frac1{e^2}\Big)\Big(\frac{c_{F,1}(T_0)}{3\log2}+c_{F,1}(T_0)\log(e^2\tau)+c_{F,2}(T_0)+\frac{2c_{F,3}(T_0)}{7e\tau}\Big)$$
> Then $\Big|\lim_{t\to\infty}\sum_{T(n)<|\Im(\rho)|\le t}\Re\big(1-(\frac{\rho}{\rho-\tau})^n\big)\Big|<K_{F,1}(\tau)\,n\log n$.

**⟹ 校正 C3**：$K_{F,1}(\tau)$ **是显式的** ✓✓（由 $A_F,B_F,c_{F,j}(T_0),\tau$ 完全决定）—— 我方"抽象引用"其实**可立即实例化** ✓。

---

## §3 Theorem 2.3（逐字）—— **本档最重要的发现** `[原文]`

> **Theorem 2.3.** Let $\tau>0$ and $T_0,A_F,B_F,C_{F,j}(T_0)$ ($j=1,2,3$) as in (c). Assume there is a real number $R>1$ such that there exists at least one zero $\rho$ with $|\frac{\rho}{\rho-\tau}|\ge R$. Furthermore define
> $$M_F:=B_F+\frac{C_{F,1}(T_0)}{e}+\frac{C_{F,2}(T_0)}{3}+\frac{C_{F,3}(T_0)}{9}$$
> and assume that for an integer $N$ it holds
> $$N\ \ge\ \Big\lceil\max\Big\{e,\ T_0,\ \frac{\tau}{\sqrt{R^2-1}},\ e^{\frac{1-15M_F}{15A_F}}\Big\}\Big\rceil$$
> Then $\Re\big(\sum_{|\Im(\rho)|\le N}(1-(\frac{\rho}{\rho-\tau})^n)\big)<\sum_{|\Im(\rho)|\le N}1-\frac1{20}R^n$ for some positive integer $n\in[N,\ 5N\,2(A_F\log N+M_F)]$ for which $N\mid n$.
> **Proof（逐字要点）**："…we can apply Lemma 2.2 since there exist only **finitely many** zeros $\rho$ with $|\Im(\rho)|\le N$. By formula (3) … there are at most $A_FN\log N+B_FN+C_{F,1}\log N+C_{F,2}+C_{F,3}/N\le N(A_F\log N+M_F)$ zeros $\rho$ with $|\Im(\rho)|\le N$. **Let these zeros be $\rho_1,\dots,\rho_M$**，where $M$ is a non-negative integer."

**⟹ 校正 C1（⚠️ 结构性）**：引擎施于的集合是
$$\{\rho:\ |\Im(\rho)|\le N\}\quad\text{（含在线、离轴，**全部**；}M=N_F(N)\text{ 由 (3) 界住}）$$
**不是**"至多 $m$ 个离轴例外" ✗✗。**"有限个"在此处是自动的** ✓（(3) 保证 $N_F(N)<\infty$ ✓），**不需要任何"至多 $m$"假设** ✓✓。
⟹ 我方 `C-46`／`C-47` 的 **"at most $m$ off-axis zeros" 框架是外加的、非源文结构** ✗ —— 必须重新论证：要么放弃该假设（用源文的自动有限性 ✓），要么说明它服务什么目的（`V290`／`A1-3` 的"至多一个 ⟹ 至多 $m$"是 **Theorem 4.1** 那条线，**不是** Theorem 2.3 这条 ✓）。

**⟹ 校正 C4**：引擎归一化＝取定 $|\frac{\rho_*}{\rho_*-\tau}|\ge R$ 的零点，令 $\max_j|z_j|=1$（$z_j$ 为 $w_j$ 的归一模），施 Lemma 2.2 ⟹
$$\Re\Big(\sum_{|\Im\rho|\le N}(1-w_\rho^{kN})\Big)\le M-\tfrac1{20}R^{kN}\qquad(k\le5M)$$
**窗口**：$n=kN$，$k\le5M\le5N(A_F\log N+M_F)$ ⟹ $n\in[N,\ 5N\cdot2(A_F\log N+M_F)]$ ✓ —— **不是我方写的 $[N,5mN_m]$** ✗。

---

## §4 Lemma 2.2（逐字，与我方引用**完全一致** ✓）`[原文]`

> **Lemma 2.2.** Let $M\ge1$ and $z_1,\dots,z_M$ complex with $\max_j|z_j|=1$. Then $\max_{1\le n\le5M}\Re\big(\sum_{j=1}^M z_j^n\big)\ge\frac1{20}$.

**⟹ 校正 C5**：我方引用的形式（含 $\max_j|z_j|=1$、窗口 $5M$、常数 $\frac1{20}$）**逐字正确** ✓✓（`E4-ENGINE-1` 的"数值判定引理成立且常数极宽松"因此**依然有效** ✓；我方引理 C 给出的 $\frac12$ 仍**强 10 倍** ✓）。

---

## §5 六项校正汇总

| # | 我方原表述 | 源文实际 | 级别 |
|:--|:--|:--|:--|
| **C1** | "至多 $m$ 个离轴例外"框架 | 引擎施于**全部** $|\Im\rho|\le N$ 零点；$M=N_F(N)$；**有限性自动** ✓ | ⚠️ **结构性** ✗ |
| C2 | 常数 $K_{F,1},K_{F,4}$ | 假设给 $A_F,B_F,C_{F,j},c_{F,j}$；$K_{F,1}$ 是 **Thm 2.1 的结论常数**；$K_{F,4}$ 未见于本次提取 | 记号 ✗ |
| C3 | $K_{F,1}$ "抽象引用" | **显式**（见 §2 公式）✓ | 可立即实例化 ✓ |
| C4 | 窗口 $[N,5mN_m]$、$N_m\mid n$ | $[N,\ 5N\,2(A_F\log N+M_F)]$、$N\mid n$ ✓ | 数值级 ✗ |
| C5 | Lemma 2.2 引用形式 | **逐字一致** ✓（$\max_j|z_j|=1$、$5M$、$\frac1{20}$）| ✓ |
| C6 | $N$ 的下界 | $N\ge\lceil\max\{e,T_0,\frac{\tau}{\sqrt{R^2-1}},e^{(1-15M_F)/(15A_F)}\}\rceil$ ✓ **显式** | 可实例化 ✓ |

---

## §6 对"价值更高"这一判断的技术含义（本档判断）

1. **好消息**：源文引擎**不需要"至多 $m$"** ✓ —— 检测对**任意**零点构型（只要计数满足 (3)）都成立 ⟹ 我方 C-46/C-47 若去掉该外加假设，**结论更强**（适用范围更广）✓✓。
2. **必须重做的部分**：C-46 的 (H1)(H2) 与"有限个"论述**建立在错误的假设之上** ✗ ⟹ 应以源文 §3 的机制**重写**（归一化＋Lemma 2.2＋计数界）✓。
3. **仍然真实的瓶颈**：阈值含 $R^{kN}$ 与 $\frac1{20}$；$R\to1^+$ 时 $N\ge\frac{\tau}{\sqrt{R^2-1}}\to\infty$ ✓ —— 与 C-46 §5 的循环点**同址** ✓（源文亦如此，故其定理 4.1 需要"至多一个"这类假设来补 ✓）。

---

## §7 边界

- `[原文]` §1–§4 全部逐字提取自本地 PDF（26 页，pypdf 抽取；公式排版有换行/空格噪声，本档已标注哪些是排版噪声）✓。
- `[校正]` C1 为**结构性**：我方框架≠源文结构 ⟹ **不得**再说"至多 $m$"是源文/档案的既定框架 ✗。
- **未做**（本档未覆盖，待续）：(i) Theorem 4.1 的逐字陈述与其"at most one"假设的确切作用；(ii) $\zeta$（或 $L(s,\chi)$）是否满足 (a)–(d) 及其实例化常数 $A_\zeta,B_\zeta,C_{\zeta,j}$；(iii) 按源文机制**重写** C-46/C-47 ✗。
- 未使用 RH；未使用零点位置。
