已查地图：**未覆盖**（所查档：`E4-palojarvi-finitely-many.md`、`E4-ENGINE-1-...md`、`E4-ENGINE-2-...md`、`E4-STATUS-AUDIT-...md`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`可比性`、`modulus spread`、`Montgomery`、`实部引理`、`衰减`。结论：本档只做 C-41 §3 遗留项的收口）

# E4-引擎-3：衰减松弛 —— **消除"模长可比"假设**；残留缺口精确化为 Montgomery 实部引理

> **任务**：唐先生 2026-09-17 19:46 选 **②攻 $m\ge2$ 的模长参差情形**。
> **结果**：C-41 §3(甲) 提出的"模长可比"假设 **可以去掉** ✓（用 $N$ 的选取让非最大项几何衰减）；剩余缺口**精确地**落在"等模长子集上的**实部**引理"＝ Montgomery Lemma 2.2 本身（$r\ge2$）；$r=1$ 已由引理 C（初等）覆盖 ✓。

---

## §1 设定与目标 `[严格]`

设至多 $m$ 个例外零点，$w_j=\rho_j/(\rho_j-\tau)$，$|w_j|>1$，记 $R'\mathrel{:=}\max_j|w_j|\ge R>1$，$K\mathrel{:=}\{j:|w_j|=R'\}$，$r\mathrel{:=}|K|\ge1$。

检测（沿用源文 (37) 分解，$n=kN$，$z_j\mathrel{:=}w_j^{N}/R'^{N}$，$|z_j|\le1$、$\max|z_j|=1$）需要
$$\exists k\le 5m:\quad R'^{kN}\sum_{j\le m}\mathrm{Re}\,z_j^{k}\ \ge\ m+2\big(K_{F,1}+K_{F,4}\big)n\log n \tag{$\star$}$$

---

## §2 ⭐ 衰减松弛：非最大项可被 $N$ 压掉 `[严格]`

对 $j\notin K$ 有 $|z_j|=(|w_j|/R')^{N}\le\rho^{N}$，其中
$$\rho\mathrel{:=}\max_{j\notin K}\frac{|w_j|}{R'}\ <\ 1$$
（若 $j\notin K$ 不存在，取 $\rho=0$。）于是对任意 $k\ge1$：
$$\Big|\sum_{j\notin K}\mathrm{Re}\,z_j^{k}\Big|\ \le\ \sum_{j\notin K}|z_j|^{k}\ \le\ (m-r)\,\rho^{Nk}$$
**故只要**
$$Nk\ \ge\ \frac{\log\big(40\,(m-r)\big)}{\log(1/\rho)}\qquad(\text{取 }\eta=\tfrac1{40}\text{ 作裕度}) \tag{$\star\star$}$$
就有 $\big|\sum_{j\notin K}\mathrm{Re}z_j^k\big|\le\tfrac1{40}$，从而
$$\sum_{j\le m}\mathrm{Re}\,z_j^k\ \ge\ \sum_{j\in K}\mathrm{Re}\,z_j^k-\tfrac1{40}$$

**结论**：C-41 §3(甲) 的"模长可比（$\sum_jD_j>M(M-1)/2$）"**不再是必要假设** —— 只要把 $N$ 取大到满足 $(\star\star)$，非最大项自动衰减到可忽略 ✓✓。**代价**：$N_m$ 的定义需追加第 4 项
$$N_m\ \ge\ \Big\lceil\frac{\log(40(m-r))}{k_{\max}\log(1/\rho)}\Big\rceil,\qquad k_{\max}=5r$$
（$k$ 取 $\le5r$，故用 $k=k_{\max}$ 作最保守估计。）由于 $R>1$ 时 $R^{n}$ 增长快于 $n\log n$，**$N_m$ 变大不影响定理的成立性**（只让检测窗口起点后移）✓。

---

## §3 残留缺口：**恰是** Montgomery 实部引理（$r\ge2$）`[缺口]`

$(\star)$ 现只需等模长子集 $K$（$|z_j|=1$，$j\in K$）满足
$$\exists k\le 5r:\quad \sum_{j\in K}\mathrm{Re}\,z_j^{k}\ \ge\ \tfrac1{20}+\tfrac1{40}\quad\text{（或任何显式正常数）}\tag{$\star\star\star$}$$

| $r$ | 状态 |
|:--|:--|
| $r=1$ | **已自足** ✓ —— 由引理 C（初等覆盖，常数 $\tfrac12$）；此即 Palojärvi Theorem 4.1 本体 |
| $r\ge2$ | **仍等价于 Montgomery Lemma 2.2** ✗ —— 本档未能自足；`E4-ENGINE-1` 已记四条路线的确切堵点 |

**因此**：C-41 §3 里"模长参差"这条**不是**真缺口（本档已消）；**真缺口只有一个** —— 单位模 $r\ge2$ 个复数上的**实部**下界。

---

## §4 该缺口的现状与一条具体建议 `[复核]`

**数值事实**（本档与前档实测）：单位模 $M$ 个复数的最坏情形
$$\min_{\theta_j}\ \max_{k\le5M}\ \sum_j\cos(k\theta_j)\ =\ 0.500\ (M{=}1),\ 0.503\ (2),\ 0.817\ (3),\ 0.990\ (4),\ 1.272\ (5),\ \dots,\ 2.236\ (10)$$
⟹ 真值**随 $M$ 增长**，$M\ge1$ 时始终 $\ge\tfrac12$。故 Montgomery 的 $\tfrac1{20}$ 极其宽松，且**很可能存在一条初等证明给出 $\tfrac12$（对所有 $M$）**。

**具体建议**（本档提出的攻击形态，未执行）：
1. **推广覆盖论证**：$M=1$ 的证明形式是"$\bigcup_k\frac1k([-60°,60°]+360°\mathbb Z)$ 覆盖全圆周"。对 $M\ge2$ 需证明：存在**同一** $k$，使 $\sum_j\cos(k\theta_j)\ge\frac12$ —— 等价于"$M$ 个点的相位不能在全部 $k\le5M$ 上同时错开"。可能的工具：$k$ 的抽屉原理 + 各 $\theta_j$ 的覆盖集**交**结构；或对 $\sum_j$ 的 Fejér 测度做**峰-平均**分离。
2. **绕开实部**：若把检测量改为模型（$|\lambda_F|$），则 C-41 §3 的模版引理（$\sqrt{0.8M}$，严格可证）即可用 —— 但 (⟸) 方向的"无例外 ⟹ 上界"需要 $\lambda_F$ 的**复**值收敛性，源文只给了实部收敛 ⟹ 需先证明配对复和的收敛（`E4-ENGINE-2` §2 已注）。

---

## §5 边界

- `[严格]` §2 的衰减估计为初等不等式（$|z_j|^{k}\le\rho^{Nk}$）；$(\star\star)$ 为充分条件，取 $\eta=\frac1{40}$ 仅为留裕度。
- `[缺口]` §3 表明 $r\ge2$ 仍依赖 Montgomery；**不声称**已自足。
- `[复核]` §4 数值为实际运行（随机＋爬山）；**不声称** $\frac12$ 的普适最优性（仅 $M=1$ 有证明与数值双重确认）。
- 未使用 RH；未使用零点位置；不修改 `E4-palojarvi-finitely-many.md` 的上文（仅追加 §9）。
