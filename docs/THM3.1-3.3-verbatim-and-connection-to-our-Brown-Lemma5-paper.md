已查地图：**未覆盖**（所查档：`THM4.1-VERBATIM-...md`（C-51）、`SOURCE-ALIGNMENT-...md`（C-49）、`ZETA-INSTANTIATION-...md`（C-50）、`brown-thm2-classical`（论文 B）、`Droll2012-thesis`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Theorem 3.1`、`Theorem 3.3`、`Brown Theorem 3`、`Lemma 5`、`K_{F,2}`、`K_{F,3}`。结论：本档做源文逐字＋连接判定）

# Theorem 3.1／3.3 逐字 ＋ **与我方论文 B（Brown Lemma 5 修复）的直接连接** ＋ 几何读数警告

> **任务**：唐先生 2026-09-17 20:44「继续」＝开 3.1／3.3（唯一无条件可用且不需"至多一个"的门）。
> **本档**：① 两定理逐字 ✓；② ⭐ **连接发现**（源文点名 Brown Thm 3 与 Thm 2 的 Lemma 5 缺口＝我方论文 B 的对象 ✓）；③ ⚠️ **几何读数警告**（结论随高度放宽，非经典零-free 区域 ✗）。

---

## §1 Theorem 3.1（逐字）：**有限个系数 ⟹ 全部零点在 $|w|<R$ 内** `[原文]`

> **Theorem 3.1.** Let $R>1,\tau>\frac1e$，$T_0,A_F,B_F,c_{F,j},C_{F,j}$ $(j=1,2,3)$ as in (c), $M_F$ as in Theorem 2.3 and $K_{F,2}(\tau)$ **as in formula (12)**. Define
> $$N=\Big\lceil\max\Big\{\underbrace{\tfrac{\tau}{\sqrt{R^2-1}},\ T_0,\ e^{\frac{1-15M_F}{15A_F}}}_{\text{三项}},\ \underbrace{\exp\big(-W_{-1}\big(-\tfrac43(5\tau^2A_F+4)\log R\big)\big),\ \tfrac{12\log(20K_{F,2}(\tau))}{\log R}}_{\text{后两项（仅当 }R\le e^{\frac{3(5\tau^2A_F+4)}{4e}}\text{）}}\Big\}\Big\rceil$$
> （$R>e^{3(5\tau^2A_F+4)/(4e)}$ 时去掉第 4 项，并加 $e$。）
> **If all coefficients $\Re(\lambda_F(n,\tau))$ are non-negative for $n\in[N,\ 5N^2(A_F\log N+M_F)]$, where $N\mid n$, then all zeros $\rho$ satisfy $|\frac{\rho}{\rho-\tau}|<R$.** ✓

**⟹ 与 Brown 的关系（源文逐字）**："**F. C. Brown [2, Theorem 3] proved that if a finite number of the Li coefficients for a certain function $F(s)$ are non-negative, then the critical strip contains zero-free regions.**" ✓✓ —— **Theorem 3.1 即 Brown Thm 3 型** ✓

## §2 Theorem 3.3（逐字）：**一个负系数 ⟹ 存在零点在 $|w|\ge R$ 外** `[原文]`

> **Theorem 3.3.** … $K_{F,3}(T,\tau)$ **as in formula (23)**；let $T>\max\{T_0,\exp(-\frac{96B_F}{23A_F}),\exp(\frac{0.324B_F}{(e^2-1.296)A_F}),\frac{8c_{F,1}}{3A_F},\frac{8c_{F,2}}{3A_F}W_0(\cdot),\frac{96C_{F,1}}{23A_F},\frac{96C_{F,2}}{23A_F}W_0(\cdot),\sqrt{\frac{192C_{F,3}}{23A_F}W_0(\cdot)}\}$；let $R>1$ with $R\le\exp(4W_0(\sqrt{K_{F,3}(T,\tau)/(4e^2N_F(T))}))$；denote
> $$n_0=\max\Big\{1,\Big\lceil\frac{1}{2}-\frac{2}{\log R}W_0\big(-\tfrac{\log R}{2}\sqrt{\tfrac{N_F(T)}{K_{F,3}(T,\tau)}}e^{\log R/4}\big)\Big\rceil\Big\},\quad n_1=\min\Big\{\frac{T}{e\tau},\Big\lfloor\frac12-\frac{2}{\log R}W_{-1}(\cdots)\Big\rfloor\Big\}$$
> **If $\Re(\lambda_F(n,\tau))$ is negative for some $n\in[n_0,n_1]$, then there exists at least one zero $\rho$ with $|\frac{\rho}{\rho-\tau}|\ge R$.** ✓

**⟹ 与 Brown 的关系（源文逐字）**："…he also tried to show [2, **Theorem 2**] … **his proof of Lemma 5 contains two errors**. A. D. Droll investigated the errors in his thesis and was able to **fix one** of them. As a result of the other error **Brown's Theorem 2 is left unproved**." ✓✓

## §3 ⭐ **连接发现：我方论文 B 正是这条链缺的那一环** `[判定]`

| 源文/文献链 | 对应我方资产 |
|:--|:--|
| Brown [2] **Lemma 5** 有两处错误 | — |
| Droll 学位论文**修好其中之一** | 我方已归档 `Droll2012-thesis-*.pdf` ✓ |
| 另一处错误未修 ⟹ **Brown Thm 2 未证** | 我方**论文 B**：**Conjecture 3.2.7 的经典情形（$\tau=1$）对所有 $k\ge2$、$H>e$ 成立** ✓✓✓ |
| Theorem 3.3 ＝ Brown Thm 2 型（$\tau$-Li 版） | ⟹ **论文 B 直接作用于此谱系** ✓✓ |
| Theorem 3.1 ＝ Brown Thm 3 型（有限系数 ⟹ 区域） | ⟹ 与我方**首版论文**（$\lambda_n\ge0$ 至 $n\le2T$）**天然接口** ✓✓ |

**⟹ 这是本项目与前沿文献一次真实的接口** ✓（不是我方自造元语言 ✓）：论文 B 补的正是 Palojärvi 所引 Brown Thm 2 那条链的缺口 ✓。

## §4 ⚠️ 几何读数警告（**必须写清，否则会误判分量**）`[严格]`

$$\Big|\frac{\rho}{\rho-\tau}\Big|^2<R^2\iff\beta<\frac\tau2+O\big((R-1)\gamma^2\big)\qquad(\gamma\to\infty)$$
**推导（初等）**：$\beta=\frac\tau2+\delta$、$\gamma$ 大时 $|w|=\frac{|\rho|}{|\rho-\tau|}\approx1+\frac{\delta}{\gamma^2}\cdot\kappa$（对 $\tau=1$：$\kappa=1$，因 $(\frac12+\delta)^2-(\frac12-\delta)^2=2\delta$）✓。

⟹ **Theorem 3.1 的结论是"随高度放宽"的** ✗ —— 对高零点它**几乎不约束 $\beta$** ✗；它**不是**经典意义（$\beta<1-c/\log\gamma$ 型）的零-free 区域 ✗。
⟹ **故不得**把 Thm 3.1 说成"给出零-free 区域"而不加限定 ✗ —— 其有效内容限于 $\gamma\lesssim1/\sqrt{R-1}$ 的零点 ✓。
⟹ 同理 Thm 3.3 的结论 $|\rho/(\rho-\tau)|\ge R$ 对高零点亦弱 ✓。

## §5 结论与待补

| 项 | 状态 |
|:--|:--|
| Thm 3.1／3.3 逐字 | ✓ 到手（含 $N$ 五项、$n_0/n_1$、$K_{F,2}$=式(12)、$K_{F,3}$=式(23)）|
| **无需"至多一个"** | ✓✓ 故对 $\zeta$ **形式可用**（$\zeta$ 满足 (a)–(d) ✓）|
| 与论文 B 的连接 | ✓✓ **源文点名的正是因为论文 B 的对象** |
| 几何读数 | ⚠️ **结论随高度放宽**，非经典零-free 区域 ✗（§4）|
| **待补** | ① 式(12) $K_{F,2}$、式(23) $K_{F,3}$ 逐字 ✗；② $\zeta$ 实例化（$N$ 五项的实际数、所需 $n$ 区间）✗；③ 与首版论文 $\lambda_n\ge0\,(n\le2T)$ 的**对接条件**（$5N^2(A\log N+M)\le2T$ 是否可满足）✗ |

- 未使用 RH；未使用零点位置；不修改任何原档 ✓。
