已查地图：**未覆盖**（所查档：`RIGORIZATION-EXTENSION-...consolidated.md`（C-47）、`THM4.1-VERBATIM-...md`（C-51）、`THM3.1-3.3-...md`（C-52）、`E4-palojarvi-finitely-many.md`、`E4-ENGINE-2/3`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Theorem 4.1`、`at most m`、`Lemma 2.2`、`5mN`、`C(m)`。结论：本档把 C-47 按源文机制**重做**为定理 4.1-m，并修正 C-46 的方向/常数错误）

# 定理 **4.1-$m$**（严谨推广）：**至多 $m$ 个离轴零点**的判据

> **任务**：唐先生 2026-09-17 20:53「继续攻击，我需要严格化有限离轴零点，这是我们后期突破的方向」。
> **本档**：把源文 Theorem 4.1（$M=1$）推广为 $M=m$，**逐行照源文机制**；修正 C-46 的三处错误（**不等号方向** ✗、**常数因子 2** ✗、**过度陈述** ✗）；给出 $m=1$ 的**严格改进**（常数 ↓10 倍、免引 Montgomery）✓。
> **等级**：`[原文]` 源文逐字 ｜ `[引用]` 引已发表定理 ｜ `[严格]` 本档完整证明 ｜ `[缺口]` 未证

---

## §1 设定 `[原文]`

$F$ 满足源文条件 (a)–(d)（含 (c) 的计数界 (3)(4) ✓）；$\tau>\frac1e$；$w_\rho:=\frac{\rho}{\rho-\tau}$。
$$|w_\rho|\le1\iff\Re\rho\le\frac\tau2;\qquad \lambda_F(n,\tau)=\lim_{t\to\infty}\sum_{|\Im\rho|\le t,\,0\le\Re\rho\le\tau}(1-w_\rho^n)\ \ \text{（式 (2) ✓）}$$
$K_{F,1}(\tau)$ 见 Thm 2.1 ✓；$K_{F,4}(\tau)$ 见 (36) ✓；$M_F:=B_F+\frac{C_{F,1}}e+\frac{C_{F,2}}3+\frac{C_{F,3}}9$ ✓。

**假设 H$_m$**：$F$ **至多 $m$ 个**零点满足 $|w_\rho|>1$（$m\ge1$）；若存在，设 $R>1$ 使 $\max_j|w_j|\ge R$ ✓（$j$ 遍历这些零点 ✓）。

---

## §2 定理 4.1-$m$ `[严格]`

设 $C(m):=40\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)+20m$，并定义
$$N_m=\Big\lceil\max\Big\{\tfrac1{e\tau}T_0,\ \exp\big(-W_{-1}(-\tfrac23\log R)\big),\ \tfrac{12\log C(m)}{\log R}\Big\}\Big\rceil\quad(R\le e^{3/(2e)});\qquad N_m=\Big\lceil\max\Big\{e,\tfrac1{e\tau}T_0,\tfrac{12\log C(m)}{\log R}\Big\}\Big\rceil\ \text{否则}$$
（对照源文 Thm 4.1：$m=1$ 时 $C(1)=40(K_{F,1}+K_{F,4})+20=40(0.5+K_{F,1}+K_{F,4})$ ✓ **逐字一致** ✓✓）

**则：存在零点 $\rho$ 满足 $|w_\rho|\ge R$**  
$$\iff\quad\big|\Re\lambda_F(n,\tau)\big|\ \ge\ \big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)\,n\log n\qquad\text{对某个 }n\in[N_m,\ 5mN_m],\ N_m\mid n.$$

**$m=1$ 强化版**（本档，用引理 C 替代 Lemma 2.2）：把上式中的 $C(1)=40(K_{F,1}+K_{F,4})+20$ 换成
$$\boxed{C^*(1):=4\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)+2}\qquad\text{（阈值 $(K_1{+}K_4)n\log n$ 不变）}$$
窗口仍为 $[N,5N]$ ✓（因引理 C 的 $k\le5$ 与 Lemma 2.2 的 $5M$ 在 $M{=}1$ 时一致 ✓）。

---

## §3 证明 `[严格]`

### §3.1 分解（源文式 (37) 逐字）`[原文]`

由 H$_m$：除例外 $\rho_1,\dots,\rho_{m'}$（$m'\le m$）外，所有零点满足 $|w_\rho|\le1$ ⟹ $\Re\rho\le\frac\tau2$ ✓。故
$$\Re\lambda_F(n,\tau)=\underbrace{\lim_{t\to\infty}\!\!\sum_{\substack{T(n)<|\Im\rho|\le t\\0\le\Re\rho\le\tau/2}}\!\!\Re(1-w_\rho^n)}_{=:G_1(n)}+\underbrace{\sum_{\substack{|\Im\rho|\le T(n)\\0\le\Re\rho\le\tau/2}}\!\!\Re(1-w_\rho^n)}_{=:G_2(n)}+\underbrace{\sum_{j\le m'}\Re(1-w_j^n)}_{=:E(n)}$$
（$T(n):=ne\tau$ ✓；最后一项**存在当且仅当**例外存在 ✓。）

### §3.2 好部分的上界（**方向关键** ✓）`[引用]`＋`[严格]`

$$\big|G_1(n)\big|<K_{F,1}(\tau)n\log n\ \text{（Thm 2.1 ✓，逐字）};\qquad \big|G_2(n)\big|\le\sum_{\substack{|\Im\rho|\le T(n)\\0\le\Re\rho\le\tau/2}}2\le K_{F,4}(\tau)n\log n\ \text{（源文证法＋(36) ✓）}$$
$$\Longrightarrow\quad \boxed{\ \big|G_1+G_2\big|\ \le\ \big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)n\log n\ }\qquad(\textbf{上界，非下界}\ ✓)$$

### §3.3 (⟸) 方向：无例外 $\Rightarrow$ 不超阈值 `[严格]`

无例外 ⟹ $E(n)=0$ ⟹ $\Re\lambda_F(n,\tau)=G_1+G_2$ ⟹ 由 §3.2 得 $|\Re\lambda_F(n,\tau)|\le(K_{F,1}+K_{F,4})n\log n$ **对所有 $n$** ✓ ⟹ 其逆否即"阈值被达到 ⟹ 例外存在" ✓。

### §3.4 (⟹) 方向：例外存在 $\Rightarrow$ 某 $n$ 超阈值 `[严格]`（$m'=1$）

取 $N$（$=N_m$）、$n=kN$。设 $R':=\max_j|w_j|\ge R$，$z:=w_1^{N}/R'^{N}$（$|z|=1$ ✓）。
**引理 C**（初等覆盖引理，$=\,M{=}1$ 的 Dirichlet 逼近）：$\max_{1\le k\le5}\Re z^k\ge\frac12$ ✓。
取此 $k$（$n=kN\le5N$ ✓）：
$$E(n)=1-\Re(w_1^{n})=1-R'^{n}\Re z^{k}\ \le\ 1-\tfrac12R'^{n}\ \le\ 1-\tfrac12R^{n}$$
$$\Longrightarrow\ \Re\lambda_F(n,\tau)\le\big(K_{F,1}+K_{F,4}\big)n\log n+1-\tfrac12R^{n}\ \le\ -\big(K_{F,1}+K_{F,4}\big)n\log n$$
只要 $\tfrac12R^n\ge2(K_{F,1}+K_{F,4})n\log n+1$ ⟺ $R^n\ge4(K_{F,1}+K_{F,4})n\log n+2$ ✓（即 $C^*(1)$ ✓）。
$\Longrightarrow|\Re\lambda_F(n,\tau)|\ge(K_{F,1}+K_{F,4})n\log n$ ✓ ✓

### §3.5 (⟹) 方向：$m'\ge2$ `[引用]`

同样归一化 $z_j:=w_j^{N}/R'^{N}$（$\max_j|z_j|=1$ ✓）。**Lemma 2.2**（源文逐字 ✓）：$\max_{1\le k\le5M}\Re(\sum_{j\le M}z_j^k)\ge\frac1{20}$ ✓（取 $M=m'$ ✓）。
取此 $k$（$n=kN\le5m'N\le5mN$ ✓）：
$$E(n)=m'-\Re\Big(R'^{n}\sum_j z_j^{k}\Big)\le m-\tfrac1{20}R^{n}\ \Longrightarrow\ \Re\lambda_F(n,\tau)\le(K_{F,1}+K_{F,4})n\log n+m-\tfrac1{20}R^n\le-\big(K_{F,1}+K_{F,4}\big)n\log n$$
只要 $\tfrac1{20}R^n\ge2(K_{F,1}+K_{F,4})n\log n+m$ ⟺ $R^n\ge40(K_{F,1}+K_{F,4})n\log n+20m=C(m)$ ✓ ✓

### §3.6 $N_m$ 的来源 `[原文]`＋`[数值]`

三项分别来自：① $\frac1{e\tau}T_0$（$T(n)=ne\tau\ge T_0$ ⟹ (3) 可用 ✓）；② 域分叉 $R\le e^{3/(2e)}$ 时的 Lambert-$W$ 槽 ✓；③ $\frac{12\log C(m)}{\log R}$（源文的 $12$ **承重**：朴素 $\lceil\log C/\log R\rceil$ 在左端点失败 ✓）。窗口 $[N,5mN]$ 与 $N\mid n$ 同源文 ✓。

---

## §4 与源文 Theorem 4.1 的严格对照

| 项 | 源文（$m=1$） | 本档 |
|:--|:--|:--|
| 假设 | at most one with $\|w\|>1$ | **at most $m$** ✓ |
| 阈值常数 | $C(1)=40(K_{F,1}+K_{F,4})+20$ | $m\ge2$: $C(m)=40(K_1{+}K_4)+20m$ ✓；**$m=1$: $C^*(1)=4(K_1{+}K_4)+2$** ✓✓ |
| 窗口 | $[N,5N]$ | $[N,5mN]$ ✓（$m=1$ 时相同 ✓）|
| 引擎 | Lemma 2.2 ($M{=}1$) | **引理 C**（更初等、$10$ 倍强）✓；$m\ge2$ 用 Lemma 2.2 ✓ |
| $N$ 公式 | 三项 ✓ | 同（$C\to C(m)$）✓ |
| 等价性 | iff ✓ | iff ✓ |

**⟹ $m=1$ 是源文定理的严格改进** ✓✓（$C^*<C$ 恒成立：差 $\approx36(K_{F,1}+K_{F,4})+18>0$ ✓；且**免引 Montgomery** ✓）。

---

## §5 诚实台账与边界

| 环节 | 状态 |
|:--|:--|
| §3.1 分解 | `[原文]` (37) 逐字 ✓ |
| §3.2 上界（**方向** ✓）| `[引用]` Thm 2.1 ＋ `[严格]` $G_2$ 的 $\le2$ 计数 ✓（**这正是 C-46 出错处，本档已修正** ✓）|
| §3.3 (⟸) | `[严格]` ✓ |
| §3.4 (⟹) $m'=1$ | `[严格]` **自足** ✓✓（引理 C ✓）|
| §3.5 (⟹) $m'\ge2$ | `[引用]` Lemma 2.2（**与源文同等地位** ✓；正确性无缺口 ✓）|
| $N_m$ 三项 | `[原文]`＋`[数值]` ✓ |
| **适用性限制** `[缺口]` | H$_m$（至多 $m$ 个例外）对 $\zeta$ **无锚** ✗（C-51 §4：$|w|>1\iff\Re\rho>\tau/2$，$\tau{=}1$ 时＝RH 近邻；零密度给的是"$\gg1$ 个"✗）。**故本定理对 $\zeta$ 不可无条件使用** ✗ —— 适用对象＝**已知 $m$ 界者**（源文所指 Dirichlet $L$ 的已知范围 ✓）|
| **不要混淆** | 本档的引擎对象＝**例外集**（Thm 4.1 的第三项 ✓）；与 Thm 2.3 的"全部低零点"引擎**不同** ✓（C-49 C1 的教训 ✓）|

**本档不声称**：不证 RH；不声称对 $\zeta$ 可用；不声称 $m\ge2$ 免引 Montgomery ✗。**原档不动** ✓。
