# AUDIT-2026-09-29ze —— 孤立码字容量路线：$f(r)$ **次线性** ✗；$A_2\ge5n_0$ **实测假** ✗

> **性质**：**审计＋局部穷举**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 16:35 ✓

**已查地图**：`AUDIT-29zd`（$n_0$ 项）／`AUDIT-29zc`（$S_c/S_x$）✓

D0: 本档对象 ＝ **档案已有**（双重计数／图论—皆经典 ✓）
D1: 0（产出＝**两处否证**：$f$ 次线性 ＋ $5n_0$ 假 ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 局部几何}:\ c'{=}0,\ c{=}e_i{+}e_j\ (d{=}2)\ \text{覆盖}\ N(0)\ \text{中恰}\ \{e_i,e_j\}\ (\text{实测}✓)}$$
$$\boxed{\text{② ✗}:\ U(\mathcal F)=\bigcup_{S\in\mathcal F}S\ \Longrightarrow\ f(r)=\min\{k:\tbinom k2\ge r\}\sim\sqrt{2r}\ \textbf{次线性}}$$
$$\boxed{\text{③ ✗}:\ \sum_{\text{iso}}t(c)=A_2^{0+}+\#(\text{iso-iso})\ \ge A_2^{0+}\ (\text{非 }=)\Longrightarrow\ \text{只得}\ A_2\ge2.5n_0}$$
$$\boxed{\text{④ ✗ 实测}:\ A_2\ge5n_0\ \text{在 4 码中 2 例违反}\ (293{<}320,\ 322{<}385)}$$

## §1 局部几何（✓）

$$O(F):=\bigcup\nolimits_{\{i,j\}\in F}\bigl(N(e_i{+}e_j)\cap N(0)\bigr)=\bigcup\nolimits_{F}\{e_i,e_j\}$$
$$\therefore\ |U(F)|=|{\textstyle\bigcup}F|\ \Longrightarrow\ f(r)=\min_{|F|=r}|{\textstyle\bigcup}F|=\min\{k:\tbinom k2\ge r\}$$
$$\text{达者}:F=\tbinom{[k]}2\ (\text{整个 }K_k)\ \Longrightarrow\ \text{覆盖 }k\ \text{个顶点}$$

## §2 次线性（✗ 关键）

| $r$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $f(r)$ | $2$ | $3$ | $3$ | $4$ | $4$ | $4$ | $5$ | $5$ | $5$ | $5$ |
| $r/f$ | $0.5$ | $0.67$ | $1.0$ | $1.0$ | $1.25$ | $1.5$ | $1.4$ | $1.6$ | $1.8$ | $2.0$ |

$$\therefore\ \boxed{f(r)\sim\sqrt{2r}\ \textbf{次线性}\ \Longrightarrow\ \text{孤立码字\ \textbf{越多，平摊越少}\ \Longrightarrow\ \textbf{无容量冲突}}\ ✗}$$

## §3 $A_2\ge5n_0$ 之双重计数纠正（✓）

$$\text{每个孤立 }c\ \text{的 10 个邻点须由距离-2 码字覆盖，每个至多贡献 2}\ \Longrightarrow\ t(c)\ge5\ ✓$$
$$\text{但}\ \sum_{\text{iso}}t(c)=A_2^{0+}+\#(\text{iso-iso 距离2对})\ \ge\ A_2^{0+}\ (\textbf{非等号}\ ✗)$$
$$\text{又}\ \sum_{\text{iso}}t(c)\le2A_2\ \Longrightarrow\ \boxed{A_2\ \ge\ 2.5\,n_0}\ (\text{非 }5n_0)\ ✓$$

## §4 实测（✗ 否证 $5n_0$ 版）

| $M$ | $A_2$ | $n_0$ | $A_2/n_0$ | $2.5n_0$ | $5n_0$ | $5n_0$ 成立 |
|---|---|---|---|---|---|---|
| $148$ | $321$ | $62$ | $5.18$ | $155$ | $310$ | ✓ |
| $148$ | $321$ | $61$ | $5.26$ | $152$ | $305$ | ✓ |
| $145$ | $293$ | $64$ | $4.58$ | $160$ | $320$ | ✗ |
| $147$ | $322$ | $77$ | $4.18$ | $192$ | $385$ | ✗ |

$$\therefore\ \boxed{A_2\ge5n_0\ \textbf{假};\ A_2\ge2.5n_0\ \text{成立}\ ✓}$$

## §5 边界（硬 ✓）

- **实测（局部几何、$f(r)$ 穷举/构造、4 码 $A_2$-$n_0$）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本档仅**否证两候选** ✓
