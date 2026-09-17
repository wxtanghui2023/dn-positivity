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

---

## §7 【勘误 T10】（2026-09-17 20:24 唐先生逐条复核 ⟹ 三处修正）

> 唐先生原话要点：引理 B 对（＝Dirichlet 逼近，我漏署名）；引理 A 下界"我推得 $\delta/(8\gamma^2)$ 不是 $\delta/(4\gamma^2)$"；"定理 1 的证明方向可能反了"；以及"**文档自己的 §4/§5 直接推翻了上一条消息里说的话**"。**四条全部成立** ✓，修正如下。

### E1（署名）引理 B ＝ **一维 Dirichlet 联立丢番图逼近**（$k\le N$、$\|k\alpha\|\le\frac1{N+1}$，$N=5$）

$\|k\alpha\|\le\frac16\iff 2\pi k\alpha \bmod 2\pi\in[-60°,60°]\iff\cos(k\alpha\cdot2\pi)\ge\frac12$ ✓。
本档 §2 的五段区间覆盖**正是该定理的标准鸽笼证明** ✓；常数 $\frac12$（即 $\frac1{6}$）与 $N{=}5$ 均**最优**（$\theta=60^\circ$ 取等 ✓）。**原文漏提经典署名 ⟹ 补正** ✓。

### E2（**勘误：常数差一倍**）引理 A 下界应为 $c_\rho\ge\frac{\delta}{8\gamma^2}$

原文 §2 写 $c_\rho\ge\frac{\delta}{4\gamma^2}$ ✗。逐步重推（唐先生的推导正确 ✓）：
$$c_\rho=\tfrac12\log(1+x),\quad x=\frac{\delta}{\beta^2+\gamma^2};\qquad \log(1+x)\ge\frac x2\ (x\le1)\ \Longrightarrow\ c_\rho\ge\frac x4$$
$$\beta<\tfrac12\ \Longrightarrow\ \beta^2+\gamma^2\le 2\gamma^2\ \Longrightarrow\ x\ge\frac{\delta}{2\gamma^2}\ \Longrightarrow\ \boxed{c_\rho\ge\frac{\delta}{8\gamma^2}}$$
（原文把 $\frac12\log(1+x)\ge\frac{x}{2}$ 误当成 $\ge\frac x2$ 后未再除 2 ⟹ 差因子 2 ✓。）

**传导修正**：定理 1 的 $n$ 上界系数 $20\to\mathbf{40}$（$n=kN_*\le5N_*\le5\cdot\frac{\log(2(1+R_n))}{c_\rho}\le\frac{40\gamma^2\log(2(1+R_n))}{\delta}$ ✓）；推论 1 的禁闭改为
$$\gamma\ \gtrsim\ \sqrt{\frac{\delta\,T}{20\log T}}$$
（**结论不变**：仍 $\ll T$，故"从属于已验证高度、无新排除"的判定**不受影响** ✓。）

### E3（**勘误：不等号方向**）定理 1 的假设须改为**其余项的"上界"**

原文写"其余零点贡献 $\ge-R_n$"，随后却按上界使用 ⟹ **逻辑不成立** ✗（$\lambda_n\ge-2R_n$，推不出 $<0$）。**正确形式**：

**定理 1′**：设 $\rho_0=\beta_0+i\gamma_0$ 离轴（$\beta_0<\tfrac12$，$\delta_0:=1-2\beta_0$），且
**(H1) 上界**：$\displaystyle\sum_{\rho\ne\rho_0}\mathrm{Re}\big[1-w_\rho^{\,n}\big]\ \le\ U_n$（显式，**必须是上界** ✓；在野"有限个离轴"设定下可得：在线部分 $\le2N(T)+n^2B_T$（引理 C ✓）＋其余离轴零点**有限个** ⟹ 逐项 $\le1+|w|^n$ ✓，故 $U_n<\infty$ ⟺ **离轴零点有限**）
**(H2) 速率分离**：其余离轴零点的速率满足 $|w_j|<|w_{\rho_0}|$（否则它们的指数项与检测项同阶，无法分离）
则存在
$$n\ \le\ \frac{40\gamma_0^2\log\big(2(U_n+1)\big)}{\delta_0}\qquad\text{使}\quad \lambda_n\ <\ 0$$
**证明**（修正方向）：$c_0:=c_{\rho_0}\ge\frac{\delta_0}{8\gamma_0^2}$（E2 ✓）；取 $N_*=\big\lceil\frac{\log(2(U_n+1))}{c_0}\big\rceil$，由引理 B 取 $k\le5$ 使 $\cos(kN_*\varphi_0)\ge\frac12$，$n=kN_*$：
$$\mathrm{Re}\big[1-w_{\rho_0}^{n}\big]=1-|w_{\rho_0}|^{n}\cos(n\varphi_0)\le1-\tfrac12e^{nc_0}\le1-(U_n+1)=-U_n$$
$$\Longrightarrow\quad \lambda_n\ \le\ U_n+(-U_n)\ =\ 0\quad\text{再把 }N_*\to N_*+1\ \text{取严格裕度}\ \Longrightarrow\ \lambda_n<0\ ✓\ \square$$
**⚠️ 新增假设 (H1)(H2) 必须写进定理** —— 这是唐先生复核逼出的**真实加强条件**，原档与原文均缺 ✓。

### E4（**过度陈述的更正**）"无穷多离轴 ⟹ 无条件排除"**在本档中未被证明**

本档 §4 表中该行原已标 `[档案声称／本档未复证 ⚠️]` ✓；但**本档口头汇报（2026-09-17 20:0x）曾把该行当作既成事实转述（并打 ✓）** ⟹ **过度陈述，更正** ✗。
**准确状态**：
- "**无穷多离轴 ⟹ 矛盾**"：`[档案声称]`，**本档未证**，且需要一个把"无穷多个不同速率/相位的离轴项"一并控制的对消论证（本档未给出）✗；
- "**单离轴 ⟹ 矛盾**"：本档只给出**定理 1′**（在 (H1)(H2) 下），而把它用成"排除"需 $\lambda_n\ge0$ 到 $n\sim40\gamma^2\log T/\delta$；
- **故本档的净结论恰是：这条反证法现在立不住**（循环点＝ Li 判据在 $n>2T$）✗ —— **不是**"已证明离轴零点只能有限个" ✓。

### E5 与 C-47（E4 合并本）的关系

**C-47 不受 E2/E3 影响** ✓：它走**模量**朝向 $|\mathrm{Re}\lambda_F|\ge|E_n|-|G_n|$，其中 $|G_n|\le(K_{F,1}+K_{F,4})n\log n$ **本就是上界** ✓（符号朝向正确 ✓）；且不出现 $c_\rho$ 的下界 ✓。（C-47 §4.2 的 $c=\frac12$ 来自引理 C 的覆盖常数，与 E2 无关 ✓。）
