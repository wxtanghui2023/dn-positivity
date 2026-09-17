已查地图：**未覆盖**（所查档：`RIGORIZATION-finitely-many-off-axis-reductio-boundary.md`（C-46）、`RIGORIZATION-EXTENSION-...-consolidated.md`（C-47）、`E4-palojarvi-finitely-many.md`、`contradiction-reductio-boundary.md`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`单向化`、`(H1) 上界`、`(H2) 速率分离`、`λ_n<0`、`E4`。结论：本档回答唐先生任务 1，不新增路线）

# 任务 1：把 C-46 的反证法经 **E4 框架**单向化 —— (H1) 自动成立、(H2) 不需要，但天花板不动

> **任务**：唐先生 2026-09-17 20:27「在 E4／乘子框架（符号朝向本来就对）里把 (H1) 上界与 (H2) 速率分离证出来，看能否把 E4 的检测单向化成 $\lambda_n<0$」。
> **结论**：**能单向化 ✓**，且代价比 C-46 小得多：**(H1) 在 E4 框架内自动成立**（$|G_n|$ 本就有上界）、**(H2) 完全不需要**（引擎施于**整个例外集**而非单个零点）✓ ✓；**但**"$n$ 随例外边际化而爆炸"的天花板**丝毫未动** ✗。

---

## §1 为何 E4 框架天然是单向的 `[严格]`

C-46 的缺陷源于：对"其余项"只有**下界**。E4 框架内不存在该问题，因为分解 (37) 的"好部分"**双向都有界**：
$$G_n\ \text{满足}\quad |G_n|\ \le\ \big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)n\log n\qquad\text{（}\textbf{上界}\ \checkmark\text{）}$$
⟹ 检测项为负时立刻得到**单向**结论：
$$\mathrm{Re}\,\lambda_F(n,\tau)=\mathrm{Re}\,G_n+\big(m'-R'^{\,n}\mathrm{Re}\textstyle\sum_jz_j^k\big)\ \le\ \big(K_{F,1}+K_{F,4}\big)n\log n+m'-cR^{\,n}$$
$$\Longrightarrow\quad \boxed{\ \mathrm{Re}\,\lambda_F(n,\tau)\ <\ -\big(K_{F,1}+K_{F,4}\big)n\log n\ }\qquad\text{（取 }cR^n>2(K_{F,1}+K_{F,4})n\log n+m'\text{）}$$
**⟹ (H1)：自动 ✓✓**（不需要另找上界）；**(H2)：不需要 ✓✓**（引擎施于整个例外集 $\{z_j\}$，无论其模长/速率分布）✓。

**⟹ 单向化后的准则**（$m'=1$、$\tau$ 固定）：
$$\exists n:\ \ \mathrm{Re}\,\lambda_F(n,\tau)<-\big(K_{F,1}+K_{F,4}\big)n\log n\qquad\Longleftrightarrow\qquad \exists\ \text{例外零点}$$
（⟹ 用引理 C／Montgomery ✓；⟸ 用 $|G_n|$ 上界 ✓。）这**就是** C-46 想要而未能给出的形式 ✓。

---

## §2 天花板：**未动** `[严格]`

| 量 | 行为 |
|:--|:--|
| 阈值 $R^n\ge4(K_{F,1}+K_{F,4})n\log n+2$（$m'=1$） | 需 $n\gtrsim\frac{8\gamma^2\log T}{\delta}$（$\delta=1-2\beta$，$\gamma$ 为**例外零点**高度）✓ |
| $R\to1^+$（例外"边际"，$|w|\to1$） | $N_m\propto\frac{\log C(m)}{\log R}\to\infty$ ✗ |
| 语义 | 例外的**边际程度**与所需 $n$ **同尺度互反** ⟹ 与 C-46 的"$n\sim2\gamma^2/\delta$"**同一堵墙** ✗ |

**⟹ 净结论**：任务 1 **达成**（$\lambda_n<0$ 单向形式在 E4 框架内成立，且不需要 (H1)(H2) ✓✓），**但没有换取任何新排除能力** ✗ —— 边际例外仍要求 $n$ 超出来源定理覆盖范围；这正是 C-46 §5 已定位的循环点 ✓。

---

## §3 边界 `[严格]`

- §1 两式为 E4 (37)＋$|G_n|$ 上界的直接推论，可逐行核 ✓；$(H1)$ 的"自动"仅**在 E4 框架内**（$|G_n|$ 有界是框架公理 (T2.1)/(T2.3) ✓），**对一般 $\zeta$ 不自动** ✗（C-46 需要引理 C 才造出上界 ✓）。
- §2 的天花板陈述为尺度级 ✓；**不声称**该反证法可成或不可成 ✓。
- **(H2)**：E4 框架不需要 ✓；但若把 E4 结论退回一般 $\zeta$ 情形（例外无限多），则 $|G_n|$ 有界本身失效 ⟹ (H2)（速率分离）仍会出现 ✓ —— 两框架的差别正在于此 ✓。
- 未使用 RH；未使用零点位置。
