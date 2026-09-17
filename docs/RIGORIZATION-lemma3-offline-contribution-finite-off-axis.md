已查地图：**未覆盖**（所查档：`PAPER-v1-li-explicit-range.md`（本档对象）、`PAPER-li-range-ELEMENTARY.md`、`PARKED-2026-09-11-li-paper.md`、`RETRACTION-A1-li-range-2026-09-11.md`、`li-range/li-range.tex`、`E4-*`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`引理 3`、`离轴下界`、`B_T`、`有限离轴`、`1/(2γ²)`、`c_ρ`。结论：本档只对**既有引理**做严格化，不新增路线）

# 严格化：首版论文〔引理 3（离轴下界）〕—— **有限个离轴零点的贡献界**

> **任务**：唐先生 2026-09-17 20:03「我要的是严格化我们以前对于有限离轴零点的证明」。
> **对象**：`docs/PAPER-v1-li-explicit-range.md` §3 **【引理 3（离轴下界）已证+核验 ✓】**（首版论文 `li-range` 的三大引理之一）。原档该引理**只有 4 行梗概**；本档把它补成**完整严格证明**，并把"**有限个**"这一结构显式化。
> **证据等级**：`[原文]` 原档逐字 ｜ `[严格]` 本档给出完整证明 ｜ `[数值]` 本档实际跑出 ｜ `[缺口]` 未核

---

## §1 记号与"有限个"的确切位置 `[原文]`

原档冻结（§2 Notation 逐字）：
$$\lambda_n=\sum_\rho\big[1-(1-\tfrac1\rho)^n\big],\qquad
\text{在线 }\rho=\tfrac12+i\gamma:\ |1-\tfrac1\rho|=1,\ \ 1-(1-\tfrac1\rho)^n=1-e^{in\theta_\gamma},\ \ \theta_\gamma=\arctan\frac{\gamma}{\gamma^2-\frac14}$$
$$\text{离轴 }\rho\ (\beta\ne\tfrac12):\ |1-\tfrac1\rho|=e^{c_\rho},\qquad c_\rho=\tfrac12\log\Big(1+\frac{1-2\beta}{\beta^2+\gamma^2}\Big)$$
$$B_T:=\tfrac12\sum_{\gamma>T}\gamma^{-2}\qquad(T\ \text{为已验证高度})$$

**"有限个"在哪里**（本档显式化，原档未点明）：把 $\sum_\rho$ 分成三段
$$\underbrace{\sum_{\text{在线},\gamma\le T}}_{(\mathrm{I})}+\underbrace{\sum_{\text{在线},\gamma>T}}_{(\mathrm{II})}+\underbrace{\sum_{\text{离轴}}}_{(\mathrm{III})}$$
- $(\mathrm{I})$：**有限个**零点（$\le N(T)$，$N(T)<\infty$ ✓），且每项 $1-\cos n\theta_\gamma\ge0$ ✓ ⟹ 可**直接丢弃**（下界 $0$）✓
- $(\mathrm{II})$：每项仍 $\ge0$ ✓ ⟹ 同样丢弃 ✓（**这正是原档"无需 $\gamma>T$ 零点的位置"的含义** ✓）
- $(\mathrm{III})$：**需要上界其最坏（负）贡献** —— 这才是引理 3 的实质 ✓✓

**关键**：$(\mathrm{III})$ 的零点是**离轴**的（$\beta\ne\tfrac12$）。**若离轴零点为有限个**，$(\mathrm{III})$ 是有限和，逐项可控；**若无限**，则必须用 $B_T$ 型绝对收敛控制 —— 两者都要证明，本档给出**统一处理**（§3）✓。

---

## §2 引理 3 的严格陈述 `[严格]`

**引理 3（严格版）**。设 $n\ge2$，$T>1$，$n<2T$。记 $\mathcal{O}_T:=\{\rho:\ \beta\ne\tfrac12,\ |\Im\rho|>T\}$（离轴且高者）。则
$$\boxed{\ \sum_{\rho\in\mathcal{O}_T}\mathrm{Re}\big[1-(1-\tfrac1\rho)^n\big]\ \ge\ -\,n\,B_T\big(1+O(1/T)\big)\ }$$
且**显式形式**为
$$\sum_{\rho\in\mathcal{O}_T}\mathrm{Re}\big[1-(1-\tfrac1\rho)^n\big]\ \ge\ -\,n\,B_T\,e^{1/T}$$
（$O(1/T)$ 常数取 $1$，即 $e^{1/T}\le1+1.72/T$，$T\ge2$ ✓。）

---

## §3 证明 `[严格]`

**(i) 化到 $\beta<\tfrac12$（正贡献段）**。由函数方程配对，$\rho=\beta+i\gamma$ 与 $1-\rho$ 同为零点。若 $\beta>\tfrac12$，则 $(1-\rho)$ 的实部 $1-\beta<\tfrac12$ —— **故每一"对" $\{\beta,1-\beta\}$ 中恰有一个 $\beta<\tfrac12$** ✓。对 $\beta>\tfrac12$：
$$\Big|1-\frac1\rho\Big|^2=1+\frac{1-2\beta}{\beta^2+\gamma^2}<1\ \Longrightarrow\ \Big|1-\frac1\rho\Big|<1\ \Longrightarrow\ \mathrm{Re}\big[1-(1-\tfrac1\rho)^n\big]\ge 1-\Big|1-\frac1\rho\Big|^n>0$$
故 $\beta>\tfrac12$ 的项**贡献为正**，可从下界中丢弃 ✓。**同理**，$\beta<\tfrac12$ 且 $\gamma$ 与 $-\gamma$ 的共轭配对：取 $\rho=\beta+i\gamma$、$\bar\rho=\beta-i\gamma$，二者 $|1-\frac1\rho|$ 相同、贡献相等 ✓ 故只需对每对计一次并乘 2 ✓（$B_T$ 中已含 $2\cdot\tfrac12$ 因子 ✓）。

**(ii) 单项界**。设 $\beta<\tfrac12$，$\gamma>T$。由
$$\frac{1-2\beta}{\beta^2+\gamma^2}\ \le\ \frac{1}{\gamma^2}\qquad(\beta\ge0,\ \beta<\tfrac12)$$
及 $\log(1+x)\le x$：
$$c_\rho=\tfrac12\log\Big(1+\frac{1-2\beta}{\beta^2+\gamma^2}\Big)\ \le\ \frac{1-2\beta}{2(\beta^2+\gamma^2)}\ \le\ \frac{1}{2\gamma^2}\qquad\Longrightarrow\qquad \Big|1-\frac1\rho\Big|^n=e^{nc_\rho}\le e^{\,n/(2\gamma^2)}$$
（**注**：$\beta\ge0$ 由零点在临界带内 ✓；$\beta<0$ 由配对归结为 $1-\beta>1$ hmm —— 严格地说，$0\le\beta\le1$ 且配对后只需 $\beta\le\tfrac12$ ✓，而 $\beta<0$ 的情形由函数方程与 $\beta>1$ 对应、同样被 (i) 覆盖 ✓。）

于是单项的**负部**（可能为负的部分）满足
$$\mathrm{Re}\big[1-(1-\tfrac1\rho)^n\big]\ \ge\ 1-e^{\,n/(2\gamma^2)}\ \ge\ -\,\frac{n}{2\gamma^2}\,e^{\,n/(2\gamma^2)}$$
（用 $1-e^{x}\ge -xe^{x}$，$x\ge0$ ✓。）

**(iii) 求和与 $n/(2\gamma^2)<1/T$**。对 $\gamma>T$ 求和：
$$\sum_{\rho\in\mathcal{O}_T}\mathrm{Re}\big[1-(1-\tfrac1\rho)^n\big]\ \ge\ -\,\sum_{\beta<\frac12,\gamma>T}\frac{n}{2\gamma^2}e^{\,n/(2\gamma^2)}$$
因 $n<2T$、$\gamma>T$ 得 $\dfrac{n}{2\gamma^2}<\dfrac{1}{T}$ ✓，且 $x\mapsto e^x$ 单调 ⟹ $e^{n/(2\gamma^2)}\le e^{1/T}$ ✓，故
$$\ge\ -\ \frac{n}{2}\,e^{1/T}\sum_{\gamma>T}\gamma^{-2}\ =\ -\,n\,B_T\,e^{1/T}\qquad\Big(B_T=\tfrac12\sum_{\gamma>T}\gamma^{-2}\Big)$$
**注意**：求和**按重数**（$B_T$ 的定义即按重数计数 ✓），且 $\sum_{\gamma>T}\gamma^{-2}<\infty$ ✓（由 $N(T)\ll T\log T$）⟹ **级数绝对收敛** ⟹ 上式的重排/括号合法 ✓✓。$\square$

**(iv) 退化核对** `[原文]`：原档写 $\Sigma_{\text{离轴}}\ge-nB_T(1+O(1/T))$ ✓ —— 本档给出**显式**形式 $-nB_T e^{1/T}$，且 $e^{1/T}=1+O(1/T)$ ✓，与原档一致 ✓；原档的 $O(1/T)$ 常数未定，本档定为 $e^{1/T}$ ✓。

---

## §4 「有限个」两种情形的统一（本档补足）`[严格]`

原档未区分"离轴有限/无限"。本档说明**两者同一处理**：

| 情形 | 处理 | 是否用到 |
|:--|:--|:--|
| 离轴零点**有限个** | $(\mathrm{III})$ 为有限和 ⟹ 直接用 (ii) 的单项界逐项相加 ✓ | ✓ |
| 离轴零点**无限个** | 由 (iii) 的绝对收敛 + $e^{1/T}$ 一致界 ⟹ 同上界 ✓ | ✓ |

**故引理 3 对两种情形都成立**，且**不需要**知道离轴零点的位置或个数 ✓✓ —— 这正是原档"只上界其最坏贡献"的严格版本 ✓。

**⚠️ 反例防护（为何不能用人造离轴对象反驳本引理）**：$F_\sigma(s)=\zeta(s)(1-q^{\sigma-s})$ 等乘子族在 $\mathrm{Re}\,s=\sigma$ 上有整条零点线 ⟹ **无限多离轴零点**且其 $B_T$ 型和**发散**（$\sum\gamma^{-2}$ 失效，因该族零点不再是"$\gamma$ 离散"）⟹ **不在本引理假设内** ✗（本引理要求零点纵标可数且 $\sum_{\gamma>T}\gamma^{-2}<\infty$，即 $\zeta$-型 $N(T)\ll T\log T$ ✓）。此点与档案 `V259-A`／`V270-A` 一致 ✓。

---

## §5 数值核验 `[数值]`

| 核验项 | 结果 |
|:--|:--|
| 单项界 $c_\rho\le1/(2\gamma^2)$ | `[数值]` dps=80 复核：$\beta\in\{0,0.001,0.25,0.49\}$、$\gamma\in\{10^3,10^6,10^{12},10^{20}\}$ **全部成立 ✓**（数学上一行：$\beta=0$ 时 $c=\frac12\log(1+\gamma^{-2})\le\frac1{2\gamma^2}$，因 $\log(1+x)\le x$）。⚠️ **自查记录**：dps=25 时 $\beta=0,\gamma=10^{12}$ **误报** $c>1/(2\gamma^2)$（$1+10^{-24}$ 已到该精度边缘）⟹ **精度假象，非反例** ✓（已在 dps=80 下排除）|
| 负部系数 $1-e^x\ge-xe^x$ | $x\in[0,1/T]$ 区间上逐点核 ✓ |
| $e^{1/T}=1+O(1/T)$ | $T=1.13249\times10^6$：$e^{1/T}=1+8.83\times10^{-7}$ ✓ |
| $B_T$ 显式值 | 原档：$T=1.13249\times10^6$ ⟹ $B_T\le3.4015\times10^{-6}$；$T_0=3.000175\times10^{12}$ ⟹ $\le2.8531\times10^{-12}$ ✓（引理 4 已给） |
| ~~端点处的引理 3 项 vs 主项~~ | **本档撤回此条** `[自查]`：把原档 §5 的"余量"（相对阈值而言）误当作"主项" ⟹ 该比较**不成立**，已删（端点余量应以原档 `A(n)/n ≥ 1.154693×10^{-2}` 那套口径复算，本档未复算）✗ |

---

## §6 边界与诚实台账

| 项 | 状态 |
|:--|:--|
| (i) 配对化到 $\beta<\tfrac12$ | `[严格]` 本档给全 ✓（原档仅一句"$\beta>\tfrac12$ 贡献 $\ge0$"）|
| (ii) 单项界 $c_\rho\le1/(2\gamma^2)$、$|w|^n-1\le(n/2\gamma^2)e^{n/2\gamma^2}$ | `[严格]` 本档给全 ✓（$\log(1+x)\le x$、$1-e^x\ge-xe^x$）|
| (iii) 求和＋$e^{1/T}$＋绝对收敛 | `[严格]` 本档给全 ✓（原档只有 $O(1/T)$）|
| (iv) 显式常数 | 本档定为 $e^{1/T}$（原档未定）✓ |
| 仍然**引用**的 | 引理 4 的 $B_T$ 显式值（Trudgian 计数界 $R(T)$）✓；引理 2（Trudgian）✓；小 $n$ 段（Palojärvi/Coffey）✓ —— **均非本引理内容** |
| **未证** | 本档**不声称**证明 RH；引理 3 只是**下界**（离轴贡献的负部控制），是首版论文定理的一个部件 ✓ |

**与原档的关系**：原档标记"已证+核验 ✓"，本档确认其**结论正确**，并补上原档省略的**全部推导细节**（配对、单项界、求和、收敛性、显式常数）＋"有限/无限离轴"的统一处理 ✓。**原档不动**（本档为新增）✓。
