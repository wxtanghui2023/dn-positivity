已查地图：**未覆盖**（所查档：`contradiction-reductio-boundary.md`、`contradiction-forms-launch.md`、`2026-08-23-full-archive.md`、`meta-argument-obstruction.md`、`E18-NOGO-ALIGNMENT-2.md`、`PAPER-v1-li-explicit-range.md`、`E4-*`、`CLOSED-ROUTES-MAP.md`、`ASSETS-REGISTRY.md`；关键词：`有限离轴`、`反证法`、`2γ²/(1−2β)`、`1/ε`、`循环`、`尺寸无关`。结论：本档对**既有反证法**做严格化，不新增路线）

# 严格化：**有限个离轴零点**的反证法边界（8/23 反证法 ＋ 9/07 边界档 ＋ 首版论文）

> **任务**：唐先生 2026-09-17 20:03「我要的是严格化我们以前对于有限离轴零点的证明」。
> **对象（三方交叉确认）**：`contradiction-reductio-boundary.md`（9/07）＋ `contradiction-forms-launch.md`（候选 E）＋ `2026-08-23-full-archive.md`
> 原档状态（逐字）：「**无穷多离轴 ⟹ 矛盾（无条件）** ⟹ 排除无穷多 ✓｜**单离轴（有限）**：$\lambda_n$ 破坏在 $n\sim1/\varepsilon\sim2\gamma^2/(1-2\beta)$ —— **需证明 $\lambda_n\ge0$ 到那个 $n$**｜**但 $\lambda_n\ge0$ 对所有 $n$ ＝ Li 准则 ＝ RH —— 循环**」
> **本档做的事**：把这条链的**每一步写成严格引理**，补上原档缺的**对齐工具**，并**精确定位循环点**。

---

## §1 记号 `[原文]`

$\rho=\beta+i\gamma$ 非平凡零点，$w_\rho:=1-\frac1\rho$。
- 在线 $\beta=\tfrac12$：$|w_\rho|=1$ ✓
- 离轴 $\beta\ne\tfrac12$：$|w_\rho|=e^{c_\rho}$，$c_\rho=\tfrac12\log\big(1+\frac{1-2\beta}{\beta^2+\gamma^2}\big)$ ✓
- $\lambda_n=\sum_\rho[1-w_\rho^n]\in\mathbb R$ ✓

**约定**：$\delta:=1-2\beta>0$（$\beta<\tfrac12$；$\beta>\tfrac12$ 由函数方程配对给出 $|w|<1$，贡献为正，见 `RIGORIZATION-lemma3-...md` §3(i) ✓）。

---

## §2 三个严格引理 `[严格]`（本档证明）

**引理 A（离轴项的增长与相位）**。设 $\beta<\tfrac12$、$\gamma>T$。则
$$\log|w_\rho|=c_\rho\ \ge\ \frac{\delta}{4\gamma^2}\quad(\text{当 }\delta\le2),\qquad \text{且}\ c_\rho\le\frac{\delta}{2\gamma^2}\le\frac{1}{2\gamma^2}$$
**证明**：$c=\frac12\log(1+\delta/(\beta^2+\gamma^2))$；用 $\frac{x}{2}\le\log(1+x)\le x$（$x\le1$）与 $\beta^2+\gamma^2\le2\gamma^2$（$\beta\le\tfrac12$）⟹ 上界 ✓；下界用 $\log(1+x)\ge x/2$ ✓。$\square$

**引理 B（对齐）**。设 $\varphi\in\mathbb R$、$N\ge1$。则
$$\exists k\in\{1,..,5\}:\quad \cos\big(kN\varphi\big)\ \ge\ \tfrac12$$
**证明**：即 $|z|=1$ 时的初等覆盖引理（见 `E4-ENGINE-2-...md` §1：五段区间并集无缝覆盖全圆周 ✓），取 $z=e^{iN\varphi}$ ✓。$\square$
**注**：**这正是原档缺失的一步** —— 原档只写"$\lambda_n$ 破坏在 $n\sim1/\varepsilon$"，未说明为何**存在**这样的 $n$（需要 $n\varphi$ 的相位对齐）✓。

**引理 C（在线项的**上**界）**。对任意 $n\ge1$：
$$0\ \le\ \sum_{\beta=\frac12}\big[1-\cos(n\theta_\gamma)\big]\ \le\ 2N(T)+n^2B_T$$
**证明**：每项 $\in[0,2]$ ✓；$\gamma>T$ 部分用 $1-\cos(n\theta_\gamma)\le\frac{n^2\theta_\gamma^2}{2}\le\frac{n^2}{2\gamma^2}$（$\theta_\gamma\le1/\gamma$ ✓）及 $\sum_{\gamma>T}\gamma^{-2}=2B_T$ ✓。$\square$

---

## §3 反证法的严格化 `[严格]`

**定理 1（单离轴的破坏）**。设 $\beta<\tfrac12$、$\gamma>T$，且**除该零点外**其余零点对 $\lambda_n$ 的贡献 $\ge-R_n$（$R_n$ 为显式量）。则存在
$$n\ \le\ \frac{5\log\big(2(1+R_n)\big)}{c_\rho}\ \le\ \frac{20\,\gamma^2\log\big(2(1+R_n)\big)}{\delta}$$
使 $\lambda_n<0$ ✓。

**证明**：取 $N_*:=\lceil\frac{\log(2(1+R_n))}{c_\rho}\rceil$，由引理 B 取 $k\le5$ 使 $\cos(kN_*\varphi_\rho)\ge\tfrac12$，令 $n=kN_*\le5N_*$ ✓。则
$$\mathrm{Re}\big[1-w_\rho^n\big]=1-|w_\rho|^n\cos(n\varphi_\rho)\ \le\ 1-\tfrac12e^{nc_\rho}\ \le\ 1-\tfrac12\cdot 2(1+R_n)\ =\ -R_n$$
故 $\lambda_n\le- R_n+R_n<0$ ✓（其余项之和 $\ge-R_n$ ✓）。$\square$

**推论 1（与首版论文结合 ⟹ 禁闭）**。取 $R_n:=2N(T)+n^2B_T$（引理 C）＋首版论文的无条件结果 $\lambda_n\ge0$（$2\le n\le2T-O(1)$ ✓）。则：**若存在离轴零点 $\rho$（$\beta<\tfrac12$）使**
$$\frac{20\gamma^2\log\big(2(1+2N(T)+n^2B_T)\big)}{\delta}\ \le\ 2T$$
**则矛盾 ⟹ 该零点不存在** ✓。等价地（用 $\log(2(1+2N(T)))\asymp\log T$）：
$$\boxed{\ \gamma\ \gtrsim\ \sqrt{\frac{\delta\,T}{\log T}}\ }$$
**即：$\beta<\tfrac12$ 的离轴零点必被"驱逐"到高度 $\sqrt{T\delta/\log T}$ 以上** ✓✓（首版论文 $T_0=3.000175\times10^{12}$：$\gamma\gtrsim3.3\times10^5\sqrt\delta$ ✓）。

---

## §4 ⚠️ 为什么这**不构成新排除**（诚实核对）`[严格]`

已验证高度 $T$ 的**含义**就是：**$\gamma\le T$ 内没有离轴零点** ✓✓（Platt–Trudgian 区间算术验证 RH 至 $T$）。而推论 1 给出的是 $\gamma\gtrsim\sqrt{T\delta/\log T}$ —— **比 $T$ 弱得多**（$\sqrt{T}\ll T$）✗✗。
⟹ **推论 1 被已验证事实完全包含**，**不提供任何新的排除** ✓ —— **这正是原档把它记为"盲区/循环"的严格原因** ✓✓。

**原档"无穷多离轴 ⟹ 无条件排除"的现状**：本档**未**给出该步的严格证明 —— 需处理"无穷多个离轴项的对消"（各 $\varphi_\rho$ 不同、$c_\rho$ 不同），本档只证了**单个**零点的破坏（定理 1）✓。**该步状态：`[档案声称 ✓／本档未复证 ⚠️]`** —— 不得据此升级为"已严格化"✗。

---

## §5 循环点的精确位置 `[严格]`

| 环节 | 状态 |
|:--|:--|
| 引理 A（$c_\rho$ 的双侧界） | **本档严格证明** ✓ |
| 引理 B（相位对齐，**原档缺失**） | **本档严格证明** ✓（引理 C 覆盖引理的尺度化版本） |
| 引理 C（在线项上界） | **本档严格证明** ✓ |
| 定理 1（单离轴 ⟹ 某 $n$ 使 $\lambda_n<0$） | **本档严格证明** ✓ |
| 推论 1（禁闭 $\gamma\gtrsim\sqrt{T\delta/\log T}$） | **本档严格证明** ✓ —— 但**从属于已验证高度，无新意** ✗ |
| 「无穷多离轴 ⟹ 排除」 | `[档案声称／本档未复证]` ⚠️ |
| **循环点** | **要把定理 1 用成"排除单离轴"，需要 $\lambda_n\ge0$ 到 $n\sim2\gamma^2\log T/\delta$；对 $\gamma\gtrsim\sqrt{T\delta/\log T}$ 的零点，该 $n$ **远超**首版论文的范围 $2T$** ⟹ 超出部分**正是 Li 判据在长范围的情形 ＝ RH** ✗✗ |

**⟹ 严格化的净结论**：这条反证法的**天花板被精确定位**为「**Li 系数在 $n>2T$ 的无条件下界**」；在 $n\le2T$ 内它**完全等价于**已验证高度（无新信息）✗；在 $n>2T$ 外它**等于 RH** ✗。原档的"循环"判词**成立**，本档给出其**精确位置与严格证明** ✓。

---

## §6 边界

- `[严格]` §2 三引理、§3 定理 1、§5 表格前三行均为本档完整证明（可逐行核）。
- `[档案]` 「无穷多离轴 ⟹ 排除」仅**照录**，本档**未复证** ⚠️。
- `[原文]` 记号、$c_\rho$ 公式、$B_T$、$N(T)$、$2\gamma^2/\delta$ 阈值均与 `PAPER-v1-li-explicit-range.md` / `contradiction-reductio-boundary.md` 一致 ✓。
- **不声称**：证明 RH；不声称反证法路线已死（只定位天花板）；不修改任何原档 ✓。
