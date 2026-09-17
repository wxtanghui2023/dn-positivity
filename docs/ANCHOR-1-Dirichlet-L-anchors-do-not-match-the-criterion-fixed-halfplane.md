已查地图：**未覆盖**（所查档：`THM4.1-m-...md`（C-54）、`THM4.1-VERBATIM-...md`（C-51）、`ZETA-INSTANTIATION-...md`（C-50）、`E4-palojarvi-finitely-many.md`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`McCurley`、`Kadiri`、`Brown Cor 1`、`Siegel`、`fixed half-plane`、`anchor`。结论：本档做方案 1（换锚）的判定）

# 方案 1（换锚）：Dirichlet $L$ 的经典"至多一个"锚 **与判据假设不匹配** ✗

> **任务**：唐先生 2026-09-17 20:59「先1，后2」＝先把 H$_m$ 落到**已知 $m$ 界**的对象上（源文所指 Dirichlet $L$）。
> **结果**：**锚到手了，但几何不匹配** ✗ —— 经典结果是**随高度收缩的 Siegel 区**（$\Re s\ge1-c/\log(q|t|)$，至多一个例外 ✓），而判据 C-54 的例外集是**固定半平面** $\Re\rho>\tau/2$ ✗✗ ⟹ **锚无法直接供给 H$_m$** ✓。

---

## §1 源文所指的三个锚（逐字）`[原文]`

**(6) McCurley [13, Theorem 1]**（$F$ ＝ primitive non-principal $\chi$ mod $q$ 的 Dirichlet $L$）：
$$\text{"$F(s)$ has no zeros in the region }\ \Re(s)\ \ge\ 1-\frac1{9.645908801\log(\max\{q,\,q|\Im(s)|,\,10\})}\ \text{ to the exception of \textbf{at most one zero}}\text{"}\ ✓$$

**(7) Kadiri [8, Theorem 1.1.1]**（$3\le q\le400000$）：
$$\text{"does not vanish in the region }\ \Re(s)=1-\frac1{5.60\log(q\max\{1,|\Im(s)|\})}\text{"}\quad(\textbf{无例外})\ ✓$$

**Brown [2, Corollary 1]**：$$\text{"for every }k\ge2\text{ there is \textbf{at most one} primitive Dirichlet character of conductor dividing }k\text{ such that the completed function … has a zero }\rho\text{ with }\Re(\rho)\ge1-\frac1{48\log k}\text{ and }|\Im(\rho)|\le\frac1{48\log k}\text{"}\ ✓$$
（且"若存在则为实、$\rho\in\mathbb R$、simple" ✓ —— 即**Siegel 零点**的经典形态 ✓）

---

## §2 ⚠️ 几何不匹配（**本档的核心判定**）`[严格]`

| 项 | 形状 |
|:--|:--|
| **判据（C-54／源文 Thm 4.1）的例外集** | $\{|\frac\rho{\rho-\tau}|>1\}=\{\Re\rho>\frac\tau2\}$ —— **固定半平面**（$\tau$ 固定，$\tau\in(\frac1e,2)$）✓ |
| **经典锚** | $\Re s\ge1-\frac{c}{\log(q\,|t|)}$ —— **随 $\lvert t\rvert$ 收缩**的区 ✗ |

**逐点核对**：设 $\tau=2-\varepsilon$ ⟹ 例外集 $=\{\Re\rho>1-\frac\varepsilon2\}$ ✓。McCurley 的区在高度 $|t|$ 处宽 $c/\log(q|t|)$ ✓：
- 若 $c/\log(q|t|)\ge\varepsilon/2$（即 $|t|\le T_\varepsilon$）：该区**包含**我们的半平面 ⟹ "至多一个"**可用** ✓
- 若 $c/\log(q|t|)<\varepsilon/2$（即 $|t|>T_\varepsilon$）：该区**窄于**我们的半平面 ⟹ **对我们的例外集无信息** ✗✗
- 而**零点的存在性**：由标准零-free 区（Kadiri 型）$c'/\log(q|t|)<\varepsilon/2$ ⟹ 允许 $\Re\rho\in(1-\frac\varepsilon2,\ 1-\frac{c'}{\log(q|t|)})$ 内的零点**存在** ✗ ⟹ 大高度处例外**个数无界** ✗

**⟹ 结论**：$\{\Re\rho>\frac\tau2\}$ 内的零点**不能**被经典结果限制为"至多 $m$ 个" ✗ —— 除非把 $\tau$ 取成**随高度变化**（判据不允许 ✗）。

---

## §3 为何不能"只控制低高度"（排除一条绕法）`[严格]`

能否把例外集改成 $\{|\frac\rho{\rho-\tau}|>1,\ |\Im\rho|\le T_\varepsilon\}$（McCurley 可覆盖 ✓）？**不行** ✗ —— 判据的分解 (37) 要求
$$\Re\lambda_F(n,\tau)=G_1(n)+G_2(n)+\sum_{j\le m'}\Re(1-w_j^n)$$
其中 $G_1,G_2$ **只含** $\Re\rho\le\frac\tau2$ 的零点 ✓（Thm 2.1／(36) 的适用范围 ✓）。因此**任何** $|w|>1$ 的零点**必须**进第三项 ✓；若大高度处还有（未受控的）$|w|>1$ 零点，第三项变成**无界和** ⟹ $G_1/G_2$ 的界与检测项**同时失效** ✗✗。

## §4 结论与含义

| 项 | 结论 |
|:--|:--|
| 三个锚是否到手 | ✓ 到手（(6)(7)＋Brown Cor 1 逐字）|
| 能否供给 H$_m$ | **不能** ✗ —— 固定半平面 vs 收缩 Siegel 区，**几何不匹配** |
| 对 $\zeta$ | 同样不能（C-51：$|w|>1\iff\beta>\frac12$，RH 近邻）✗ |
| **一般性判断** | H$_m$（"固定半平面内例外零点至多 $m$ 个"）**既无锚也与现有无条件结果形态不一致** ✗；它**不是** RH 的弱推论（RH ⟹ $m=0$ ✓），但**现有工具给不出它** ✗ |
| 源文的说法 | 源文称此类结果"known for Dirichlet L-functions（recall (6),(7)）" ✓ —— 但 (6)(7) 的**区域随高度收缩**，与 Thm 4.1 的**固定半平面**不是同一形状 ✗ ⟹ **该处的适用性说明需要打折扣**（本档记录，不据此指责源文：可能作者另有 $\tau$ 随区域的用法，本档未找到）⚠️ |

## §5 边界

- `[原文]` §1 三条锚、(6)(7)、Brown Cor 1 均逐字取自本地 PDF ✓。
- `[严格]` §2 的逐点核对（$T_\varepsilon$ 分界）、§3 的分解适用范围论证均可逐行核 ✓。
- `[缺口]` 本档**未做**：是否可用**随高度变化的 $\tau$** 重写判据（＝改框架，非严格化）✗。
- **不声称**：不指责源文有误（§4 末 ⚠️）；不证 RH；不修改任何原档 ✓。
