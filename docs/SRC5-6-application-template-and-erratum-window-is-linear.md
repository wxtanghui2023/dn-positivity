已查地图：**未覆盖**（所查档：`THM3.1-3.3-...md`（C-52）、`INTERFACE-CONDITION-...md`（C-53）、`ANCHOR-1-...md`（C-55）、`ROUTE-1-...md`（C-56）、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`Section 5`、`Table 1`、`q=100`、`window`、`linear`。结论：本档做 §5/§6 提取＋两项勘误）

# 源文 §5／§6 的**真实应用模式** ＋ **勘误：窗口是 $10N(A_F\log N+M_F)$（线性）** ✗

> **任务**：唐先生 2026-09-17 21:10「继续」＝提取 §5／§6 数值算例，看作者**实际怎么用**这些定理。

---

## §1 作者的数值算例（逐字）`[原文]`

对象：**Dirichlet $L$，primitive non-principal $\chi$ mod $q=100$**；$\tau=1$；$R=1.1$ 与 $1.01$。

| $\tau$ | $R$ | Thm 3.1 的 $N$ | Thm 3.1 的窗口 | Thm 4.1 的 $N$ |
|:--|:--|:--|:--|:--|
| 1 | 1.1 | **2228** | **142 795** | 217 838 |
| 1 | 1.01 | **21 335** | **14 730 585** | 8 027 |

**量级**：窗口 $\approx10^5$–$10^7$ 个 $\lambda_F$ 值 ⟹ **实际可算** ✓✓（对比我方 $\zeta$ 情形完全不同 ✗）

## §2 ⭐ 作者自己的**互补性**陈述（逐字）—— **印证 C-55 的判断** ✓✓

> "As it can be seen in Figure 2, **the results proved in Theorems 3.1 and 3.3 allow us to consider existence of the zeros which have real parts close to the line $\Re(s)=\frac12$** while **Kadiri's and McCurley's results consider zeros which real parts are close to the lines $\Re(s)=1$ and $\Re(s)=0$**. On the other hand, **Kadiri's and McCurley's results do not have upper bound for the absolute values of imaginary parts** of the zeros whereas **Theorems 3.1, 3.3 and 4.1 consider only zeros up to some height**. Kadiri's and McCurley's results also provide clear zero-free regions while the results proved in this article only provide some conditions to hold. Also, with the exception of Theorem 4.1, we do not give any if and only if statements." ✓

**⟹ 逐点对应 C-55**：
| C-55 的判定 | 作者自述 |
|:--|:--|
| 例外集（$\Re\rho>\tau/2$，靠近 $1/2$）| "zeros … real parts **close to the line $\Re(s)=1/2$**" ✓ |
| 经典锚（Siegel 区，靠近 $1$ 与 $0$）| "zeros … close to the lines $\Re(s)=1$ and $0$" ✓ |
| 形状不匹配（固定半平面 vs 收缩区）| "do not have upper bound for the imaginary parts"（经典）vs "only zeros up to some height"（本文）✓✓ |
| 且锚**不能**互换 | 二者被作者列为**互补**（Figure 2）✓ |

**⟹ C-55 的判断得到作者原文印证** ✓✓（不是我的误读）。

## §3 ⚠️ 勘误：窗口是 **$10N(A_F\log N+M_F)$（线性）** ✗

用 §1 的数值反推：$N=2228$、$A_F=\frac1\pi\approx0.318$、窗口 $=142795$。
- 若窗口 $=5N^2(A\log N+M)$：需 $A\log N+M=\frac{142795}{5\cdot2228^2}=0.00576$ ✗ **不可能**（$A\log N\approx2.45$ 已远超 ✗）
- 若窗口 $=5N\!\cdot\!2(A\log N+M)=10N(A\log N+M)$：需 $A\log N+M=\frac{142795}{22280}=6.41$ ⟹ $M\approx3.96$ ✓ **合理** ✓✓
- **核对**：$10\cdot2228\cdot(2.45+3.96)=22280\cdot6.41=142{,}815\approx142{,}795$ ✓✓ **吻合**

**⟹ 定论**：源文窗口为
$$\boxed{\ n\in\big[N,\ 10N\,(A_F\log N+M_F)\big]\ }\qquad(\textbf{线性于 }N\ ✗)$$
- **影响**：`C-52` §1 与 `C-53` §1 我写作 $5N^2(\cdots)$ ✗ —— **勘误** ✓
- **不影响**：`C-53` 的**结论**（不相容）✓ —— 用线性窗口重算：非平凡性需 $R-1\lesssim T_{\rm ver}^{-2}=1.1\times10^{-25}$ ⟹ $N\gtrsim12\log(20K_2)/\log R\approx1.9\times10^{27}$ ⟹ 窗口 $=10N(A\log N+M)\approx1.9\times10^{29}$ vs $2T=6\times10^{12}$ ⟹ **仍超约 $3\times10^{16}$ 倍** ✗✗（原写 $10^{42}$，系 $N^2$ 所致 ✗ —— 结论不变 ✓）
- **不影响** `C-54`（定理 4.1-$m$）：其窗口 $[N_m,5mN_m]$ 取自 **Thm 4.1** 与 **Lemma 2.2** ✓（非 Thm 3.1）✓

## §4 对 $\zeta$ 的可迁移模板（本档判定）`[严格]`

| 项 | Dirichlet $L$（$q=100$）| $\zeta$（$\tau=1$）|
|:--|:--|:--|
| 计数常数可用下界 $T_0$ | $\approx1$（(38) 对 $T\ge1$ ✓）| 同样可取 $T_0=1$ ✓（Trudgian 型界 ✓）—— **不必取 $T_{\rm ver}$** ✓（我 `C-50`/`C-53` 用 $T_{\rm ver}$ 是**选择**而非必须 ✓）|
| 所需 $N$ | $2228$–$21335$ ✓ | $12\log(20K_{\zeta,2})/\log R$ ⟹ 对 $R=1.1$ 约 $10^2$–$10^3$ ✓ |
| 窗口 | $10^5$–$10^7$ ✓ **可算** | $10^3$–$10^4$ ✓ **可算** |
| **但**结论是否强于已验证高度 | （$L$ 无此问题）| **否** ✗：要强于 $T_{\rm ver}$ 需 $R-1\lesssim10^{-25}$ ⟹ 窗口 $\approx10^{29}\gg2T$ ✗✗ |

**⟹ 净判断**：**模板可迁移**（$T_0=1$、窗口线性、$N$ 小 ✓），**但 $\zeta$ 的实质障碍不变** ✗ —— 不是窗口形状，而是"**要让结论超过已验证高度，$R$ 就必须贴到 1，而那使窗口爆掉**" ✓（$R$ 与窗口的对偶，本质＝ $m$ 的锚定/边际性问题 ✓）。

## §5 边界

- `[原文]` §1 表格、§2 整段均为逐字（§5／§6 提取）✓。
- `[数值]` §3 的反推与核对为实际计算 ✓；两处勘误（C-52、C-53 的窗口形状）✓。
- `[严格]` §4 的 $T_0=1$ 合法性、$R$-窗口对偶均可核 ✓。
- **不声称**：不证 RH；不声称模板迁移即得新结果 ✗；不修改任何原档 ✓。
