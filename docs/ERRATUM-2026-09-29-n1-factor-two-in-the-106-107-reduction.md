# ERRATUM-2026-09-29-n1 — `RESULT-29n` §3 的 **×2 漏因子**：`N≤2 ≥ Σδ` 应为 `N≤2 ≥ Σδ/2`

> 性质：**勘误**（门规则 1–4 豁免）｜空间 B｜**不主张 107**（V290）
> 触发：本会话恒等式 T 复算时，对该归约做**已知码反向验证** ⟹ **两个已知码双双违反** ⟹ 判定为漏因子 ✗ ✗
> 时间：2026-09-29 22:3x

## §0 结论

$$\boxed{\text{`RESULT-29n` §3 之}\ N_{\le2}\ge\Sigma\delta\ \textbf{错};\ \text{正确为}\ \boxed{N_{\le2}\ \ge\ \tfrac12\Sigma\delta}\ ✗✓}$$

## §1 原文与错误点

`RESULT-29n` §3 逐字：

> 由 E4：$N_{\le2} \ge (11M - \#\text{私有点})/2 \ge (1166-882)/2 = \mathbf{142}$

**代数化简**（代入 $\#\text{priv}=1024-\Sigma\delta=2048-11M$）：
$$(11M-\#\mathrm{priv})/2=(11M-2048+11M)/2=11M-1024=\Sigma\delta$$
⟹ 该式实为 $N_{\le2}\ge\Sigma\delta$ ⟹ **把 $2N_{\le2}=\Sigma_x\binom{\mu}2\ge\Sigma\delta$ 里的因子 2 丢了** ✗

**正确链条**（每步可核）：
$$\forall x:\ \mu(x)\ge1\ \Longrightarrow\ \binom{\mu}2\ \ge\ \mu-1\ \ \Bigl(\tfrac{(\mu-1)(\mu-2)}2\ge0\Bigr)$$
$$\Longrightarrow\ \Sigma_x\binom{\mu(x)}2\ \ge\ \Sigma\delta\ \ \text{而}\ \ \Sigma_x\binom{\mu(x)}2 = 2N_{\le2}\ \Longrightarrow\ \boxed{N_{\le2}\ \ge\ \tfrac12\Sigma\delta}$$

## §2 已知码反向验证（**本档实跑**）

| 码 | $M$ | $\Sigma\delta$ | $N_{\le2}$ | 正确式 $\ge\Sigma\delta/2$ | 档案式 $\ge\Sigma\delta$ |
|---|---|---|---|---|---|
| $n{=}9$ 62-码 | 62 | 108 | 73 | $\ge54$ ✓ | $\ge108$ **违反** ✗✗ |
| $n{=}10$ 120-码 | 120 | 296 | 199 | $\ge148$ ✓ | $\ge296$ **违反** ✗✗ |

（$n{=}9$ 一式用 $(10M-\#\mathrm{priv})/2=94$、$n{=}10$ 用 $(11M-\#\mathrm{priv})/2=259.5$ —— 两处均被实际值违反 ✓✓）
**旁证**：$2N_{\le2}=\Sigma_x\binom{\mu}2$ 两例逐字成立（$146=2\cdot73$；$398=2\cdot199$）✓

## §3 影响（**必须撤回/修正的**）

1. $M{=}106$ 处正确下界为 $N_{\le2}\ge\mathbf{71}$（**非 142**）✗
2. $\mu_{\max}\ge4$ 之**推论作废** ✗：由 $\Sigma\delta\ge4N_{\le2}/\mu_{\max}$ 与 $N_{\le2}\ge\tfrac12\Sigma\delta$ 仅得
   $$142\ \ge\ \frac{4\times71}{\mu_{\max}}\ \Longrightarrow\ \mu_{\max}\ \ge\ \mathbf2\ (\text{平凡})\ ✗$$
3. **「一格缺口」为假象** ✗：$N_{\le2}\ge143$ vs $142$ 应为 $143$ vs $\mathbf{71}$ ⟹ 真缺口 $\approx\mathbf{72}$（$N_{\le2}$ 单位）
4. 受影响档案：`RESULT-29n` §3／`HANDOVER` §2 (C) 之「$\mu_{\max}\ge4$ 推论」／§4 之「结构诊断」前提 ⚠️

## §4 仍然成立（**未受影响** ✓）

- 恒等式 $E1/E2/E3$、$E4$ 之**恒等式形式**（$\#\mathrm{priv}\ge1024-\Sigma\delta$）✓
- $M{=}106\iff\Sigma\delta=142$；**复现 107 $\iff$ 排除 $M{=}106$** ✓
- 恒等式 $T$（三点层：$\Sigma_x\binom{\mu}3=P+E$）✓
- 规避禁令之论证（`AUDIT-29e`：单条线性 $\le105.2223$）✓ ⟹ 必须走**三次/非松弛**层 ✓

## §5 本档顺带得到的**有效**新不等式（✓ 已验证）

$$\boxed{P\ \le\ 2A_2}\qquad(P=\Sigma_{y\in C}\binom{a_y}2,\ a_y=\#\{c:d(c,y)=1\})$$
来源：$\mu(y)=1+a_y$（$y\in C$）⟹ $\Sigma_{y\in C}\binom{\mu(y)}2=P+2A_1\le\Sigma_x\binom{\mu}2=2(A_1+A_2)$
验证：62-码 $6\le132$ ✓；120-码 $41\le298$ ✓
