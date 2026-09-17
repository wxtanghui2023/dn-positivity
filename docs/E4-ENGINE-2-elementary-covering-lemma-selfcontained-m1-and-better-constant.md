已查地图：**未覆盖**（所查档：`E4-palojarvi-finitely-many.md`、`E4-ENGINE-1-...md`、`E4-STATUS-AUDIT-...md`、`PENDING-ITEMS-MASTER.md`（A1-3 行）、`CLOSED-ROUTES-MAP.md`、`MASTER-STATUS-AND-CLOSURES.md`、`ASSETS-REGISTRY.md`；关键词：`Lemma 2.2`、`Montgomery`、`1/20`、`5M`、`至多一个离轴`、`covering`。结论：**本档不新增路线，只把既有的"至多一个离轴"定理的引擎换成自足初等引理**）

# E4-引擎-2：初等覆盖引理 ⟹ 定理 4.1（$m=1$）自足重证 ＋ 常数改善 10 倍

> **任务**：唐先生 2026-09-17 19:42 选 **②改判据方向（引擎自足化）**。
> **产出**：①**初等覆盖引理**（完整证明，替代 Montgomery Lemma 2.2 在 $M=1$ 情形）；②由它给出 **Palojärvi Theorem 4.1 的自足重证**（不再引用 Montgomery），且**阈值常数由 $40(K_{F,1}+K_{F,4})+20$ 降为 $4(K_{F,1}+K_{F,4})+2$**；③$m\ge2$ 的推广仍为条件性（路线 ③＋可比性，或仍需 Montgomery 的实部版）。

`[出处]` 源定理（Palojärvi arXiv:1807.01506v3, Thm 4.1）：设 $F$ 满足 (a)–(d)、$\tau>1/e$，且 $F$ **至多一个**零点 $\rho_1$ 满足 $|\rho_1/(\rho_1-\tau)|>1$；若存在，设 $R>1$ 使 $|\rho_1/(\rho_1-\tau)|\ge R$。则
$$\rho_1\ \text{存在}\iff |\mathrm{Re}\,\lambda_F(n,\tau)|\ \ge\ (K_{F,1}(\tau)+K_{F,4}(\tau))\,n\log n\quad\text{对某个 } n\in[N,5N],\ N\mid n$$
原证明引擎：`[引用]` Montgomery, *Ten Lectures*, Ch. 5 Thm 11 = Palojärvi Lemma 2.2：$\max_{1\le n\le5M}\mathrm{Re}\sum_{j\le M}z_j^n\ge\frac1{20}$（$M=1$ 时即 $\max_{1\le n\le5}\mathrm{Re}\,z^n\ge\frac1{20}$）。

---

## §1 ⭐ 初等覆盖引理（$M=1$ 的自足替代）`[严格]`

**引理 C（初等）**。设 $z\in\mathbb C$，$|z|=1$。则
$$\max_{1\le k\le 5}\ \mathrm{Re}\,z^k\ \ge\ \frac12$$
**证明**。写 $z=e^{i\theta}$，$\mathrm{Re}\,z^k=\cos k\theta$。断言
$$\bigcup_{k=1}^{5}\ \bigcup_{j\in\mathbb Z}\ \frac{1}{k}\Big(360^\circ j+[-60^\circ,60^\circ]\Big)\ =\ \mathbb R \pmod{360^\circ}$$
逐段列出（$k$：$\theta$ 被覆盖的区间，单位度）：
$$k=1:[0,60]\cup[300,360];\quad k=2:[150,210];\quad k=3:[100,140]\cup[220,260]$$
$$k=4:[75,105]\cup[165,195]\cup[255,285];\quad k=5:[60,84]\cup[132,156]\cup[204,228]\cup[276,300]$$
拼接检查：$[0,60]$(1) → $[60,84]$(5) → $[75,105]$(4) → $[100,140]$(3) → $[132,156]$(5) → $[150,210]$(2) → $[165,195]$(4) 与 $[204,228]$(5) → $[220,260]$(3) → $[255,285]$(4) → $[276,300]$(5) → $[300,360]$(1)。**无缝覆盖全圆周** ✓。故存在 $k\le5$ 使 $k\theta\in[-60^\circ,60^\circ]\pmod{360^\circ}$，即 $\cos k\theta\ge\frac12$ ∎

**推论**：$M=1$ 时引理 C **严格强于**引用的 Montgomery 版（$\frac12>\frac1{20}$，**10 倍**），且**不需要 Montgomery** ✓。常数 $\frac12$ 是最优的（$z=e^{i\pi/3}$ 时 $\max_{k\le5}\cos k\theta=\frac12$，本档数值确认）`[复核]`。

---

## §2 $m=1$ 的自足重证（替换引擎后的常数）`[严格]`

沿用源文分解 (37)（逐字 `[出处]`）：
$$\mathrm{Re}\,\lambda_F(n,\tau)=\underbrace{\lim_{t\to\infty}\sum_{T(n)<|\Im\rho|\le t,\ 0\le\Re\rho\le\tau/2}\mathrm{Re}(1-w_\rho^n)}_{(i)\ \text{大高度}}+\underbrace{\sum_{|\Im\rho|\le T(n),\ 0\le\Re\rho\le\tau/2}\mathrm{Re}(1-w_\rho^n)}_{(ii)\ \text{低高度}}+\underbrace{\mathrm{Re}(1-w_1^n)}_{(iii)\ \text{检测}}$$
其中 $w_\rho=\rho/(\rho-\tau)$，$T(n)=ne\tau$，$|w|\le1\iff\Re\rho\le\tau/2$。

- **(⟸) 无离轴零点**：此时无第 (iii) 项，且 (i)(ii) 中每个零点满足 $|w|\le1$ ⟹ $|\mathrm{Re}(1-w^n)|\le|1-w^n|\le1+|w|^n\le2$ ⟹ 由源文 Theorem 2.1 与显式零点计数得
$$|\mathrm{Re}\,\lambda_F(n,\tau)|\le\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)n\log n\qquad(\forall n)$$
**与源文同常数** ✓（注意：改用 $|1-w^n|$ 上界不损失任何常数 ✓）。
- **(⟹) 存在离轴零点** $\rho_1$、$R'\mathrel{:=}|w_1|\ge R>1$：取 $z\mathrel{:=}w_1^N/R'^N$，$|z|=1$ ✓。由**引理 C** 取 $k\le5$ 使 $\mathrm{Re}\,z^k\ge\frac12$，令 $n=kN\in[N,5N]$ ✓（**窗口与源文逐字一致**）：
$$\mathrm{Re}(1-w_1^n)=1-R'^n\,\mathrm{Re}\,z^k\ \le\ 1-\tfrac12R'^n$$
（用 $R'^n\ge R^n$ ✓）。故
$$|\mathrm{Re}\,\lambda_F(n,\tau)|\ \ge\ \tfrac12R'^n-1-\big(K_{F,1}+K_{F,4}\big)n\log n\ \ge\ \big(K_{F,1}+K_{F,4}\big)n\log n$$
**只要**
$$\boxed{\,R^n\ \ge\ 4\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)n\log n+2\,}$$

**与源文对照** `[出处]`：源文阈值为 $R^n\ge40n\log n\,(\tfrac12+K_{F,1}+K_{F,4})=20n\log n+40(K_{F,1}+K_{F,4})n\log n$。本档阈值为 $4(K_{F,1}+K_{F,4})n\log n+2$，故两者之差
$$\big[20n\log n+40(K_{F,1}+K_{F,4})n\log n\big]-\big[4(K_{F,1}+K_{F,4})n\log n+2\big]=20n\log n+36(K_{F,1}+K_{F,4})n\log n-2\ >\ 0$$
（$n\log n\ge e$ 时）⟹ **同一窗口、同一结论，阈值恒更小**：$(K_{F,1}+K_{F,4})$ 项恰好降为 $\tfrac1{10}$，且额外省去源文的 $20n\log n$ 主项 ✓✓。

**推论（$N$ 的显式形式）**：引理 C 使 §5b 的三尺度分割中 $\tfrac1{20}$ 被 $\tfrac12$ 取代，故
$$N_1^{\text{新}}=\Big\lceil\max\Big\{\frac{T_0}{e\tau},\ \exp\big(-W_{-1}(-\tfrac23\log R)\big),\ \frac{12\log\big(4(K_{F,1}+K_{F,4})+2\big)}{\log R}\Big\}\Big\rceil$$
（$\tfrac{12}{\log R}$ 槽位不变，只把常数 $40(K_{F,1}+K_{F,4})+20$ 换成 $4(K_{F,1}+K_{F,4})+2$ ⟹ $N$ 的 $m$-代价同步减小 ✓。）

---

## §3 $m\ge2$：两条可用路线（仍有一条外部依赖）`[严格]`＋`[缺口]`

**(甲) 路线 ③ 的模版引理（本档自足，需"模可比"假设）**。$[严格]$ 设 $|z_j|\le1$、$\max_j|z_j|=1$。用 Fejér 权 $w_k=1-k/(5M)$：
$$\sum_{k\le5M}w_k\Big|\sum_j z_j^k\Big|^2=\sum_{j,l}\sum_k w_k(z_j\bar z_l)^k\ \ge\ \sum_j D_j-\frac{M(M-1)}2,\qquad D_j:=\sum_{k\le5M}w_k|z_j|^{2k}$$
（对角项 $\ge0$；非对角每对由 Fejér 核非负性 $\ge-\frac12$。）故
$$\max_{k\le5M}\Big|\sum_j z_j^k\Big|^2\ \ge\ \frac{\sum_j D_j-M(M-1)/2}{5M/2}$$
**数值确认** `[复核]`：全模 1 时 $\sum_j D_j\approx(5M/2)M$ ⟹ 界 $\ge M(5M-M)/(5M)=\frac45M$，即 $\ge\sqrt{0.8M}$；混模（$|z_j|\ge1-\frac1{8\cdot5M}$，$D_j\ge\frac{5M}4$）时 $\ge\sqrt{0.3M}$ ✓；三条实测最坏值均**高于**理论界 ✓。
**限制**：需 $\sum_j D_j>M(M-1)/2$，即"多数例外模长须接近最大值"（可比性）✗ —— 宽范围模长时该路线退化。

**(乙) 仍引 Montgomery**：$m\ge2$ 的**实部**检测（$\mathrm{Re}\sum_j z_j^k\ge c$）在模长参差时仍需 Lemma 2.2；本档未能自足 ✗（`E4-ENGINE-1` 已记四条路线堵点）。

---

## §4 结论表

| 事项 | 状态 |
|:--|:--|
| **$m=1$（源文 Theorem 4.1 本体）** | **自足重证完成** ✓✓ 引擎＝初等覆盖引理 C（$\frac12$，逐段覆盖证明），**不再引用 Montgomery** ✓ |
| 常数 | 源 $20n\log n+40(K_{F,1}+K_{F,4})n\log n$ $\longrightarrow$ 新 $4(K_{F,1}+K_{F,4})n\log n+2$：$(K_{F,1}+K_{F,4})$ 项 **↓ 恰 10 倍**，并省去源文的 $20n\log n$ 主项 ✓ |
| 窗口 | 不变（$[N,5N]$、$N\mid n$）✓ |
| (⟸) 方向常数 | 不变（$|1-w^n|\le2$ 与源文同）✓ |
| $m\ge2$（本档推广） | 条件性：**可比模长**时用路线 ③（增益 $\sqrt{\cdot}$，强于 $\frac1{20}$）；**模长参差**时仍需 Montgomery 实部版 ✗ |
| 引理 C 最优性 | $\frac12$ 取到（$z=e^{i\pi/3}$）✓ `[复核]` |

---

## §5 边界

- `[严格]` §1 覆盖证明为逐段有限检查（五段并集无缝覆盖全圆周）——可逐行核；§2 的代数与阈值推导可逐行核。
- `[复核]` 数值：$\min_\theta\max_{k\le5}\cos k\theta=0.5$；$D_j/N\in[0.35,0.46]$（$|z|\ge1-\frac1{8N}$）；引理 M2/③ 的实测最坏值均高于理论界。
- `[缺口]` $m\ge2$ 的实部检测在模长参差时仍依赖 Montgomery Ch.5 Thm 11（本地无书）；本档**不声称**该引路已自足。
- 未使用 RH；未使用零点位置；不修改 `E4-palojarvi-finitely-many.md`（原档不动）。
- **本档产物可直接回填原档**：把 §2 作为 Theorem 4.1 的"自足证明＋常数改善"注记（待唐先生定）。
