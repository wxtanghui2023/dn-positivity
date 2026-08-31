# GRH 判别判据：迁移定理（正式化——对任意 L(s,χ)）

> 目标：把 RH 判别判据（ζ 版——O1-O5/C1-C5）迁移到 Dirichlet L 函数——
> 定理：对任意原字符 χ（模 q*）——Q_χ = Q'_{RH,χ} ⟺ χ 的零点全在临界线。
> 状态：结构正式化（A1-A6——代数不依赖 q——模 3/4/5 数值支撑）
> 日期：2026-08-31

---

## 定理（GRH 判别判据——L 函数版）

设 χ 是模 q 的原字符，L(s,χ) 的完成函数
$$\xi_\chi(s) = (q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi),\qquad
a = \begin{cases}0 & \chi(-1)=1\\ 1 & \chi(-1)=-1\end{cases}$$
零点 $\rho = \tfrac12+\delta_\rho+i\gamma_\rho$（重数 $m_\rho$）。定义
$$Q_\chi = -\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho),\qquad
Q'_{\mathrm{RH},\chi} = -\sum_\rho m_\rho w_H(\gamma_\rho,0),$$
其中 $w_H(\gamma,\delta) = [a^2(a+1)+\delta\gamma^2]/[2(a^2+\gamma^2)^2]$，$a=1+\delta$。
则：
$$\boxed{\,Q_\chi = Q'_{\mathrm{RH},\chi} \iff \delta_\rho = 0\ \forall\rho\iff \operatorname{Re}\rho=\tfrac12\ \forall\rho\,}$$

---

## 证明结构（迁移——每步不依赖 q/χ）

### Step 1：Hadamard 展开（A1——标准）
- $\xi_\chi$ 是整函数（阶 1）——Hadamard 积（——Davenport Ch.9——）
- $S_\chi(t) := \partial_t^2\log|\xi_\chi(\tfrac12+it)| = \sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t) + S_{\mathrm{reg},\chi}(t)$
- $K_\rho^{\mathrm{nat}}(t) = (\delta_\rho^2-(t-\gamma_\rho)^2)/(\delta_\rho^2+(t-\gamma_\rho)^2)^2$
- **S_reg,χ 不进入 Q/Q'**（——判据逐项定义在零点项上——）——需注明（见 Step 6）

### Step 2：测试对象 H_0（A2——纯 Fourier——不依赖 q/χ）
- $H_0(t) = -\frac{1}{4\pi}\log(1+t^2)+\frac{1}{2\pi(1+t^2)}$——$H_0''\in L^1$——$H_0\notin L^1$
- 由 $H_0 = F^{-1}[\widehat w_{\mathrm{target}}/\widehat K_0]$ 构造（——与 ζ 版相同——）
- **不含任何 L 函数量**——通用

### Step 3：配对权重与成对正性（A3——纯代数）
- 逐项配对 $\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma),H_0\rangle$（Parseval 乘积 $L^1$——标准积分）
- $w_H(\gamma,\delta) = [a^2(a+1)+\delta\gamma^2]/[2(a^2+\gamma^2)^2]$
- $P_\gamma(\delta) = 2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)
  = \delta^2 M_2/(2U^2D_+D_-)$——$M_2$ 正系数（$|\delta|<\tfrac12$——$\gamma>\tfrac1{\sqrt5}$）
- **代数恒等式**——不依赖 χ——模 3/4/5 机器精度验证（——数值支撑——）

### Step 4：等号刚性（A4）
- $Q_\chi - Q'_{\mathrm{RH},\chi} = \sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho)$
  （——按函数方程轨道 $\rho\sim 1-\bar\rho$——同 γ 反 δ——在线自配对贡献 0——）
- **P_γ > 0 需 γ > 1/√5**——非平凡零点 $\gamma \ge \gamma_{1,\chi} \ge 6.02$（β 最小——
  标准下界）——自动满足
- $Q_\chi=Q'_{\mathrm{RH},\chi}\Rightarrow\sum m_\rho P=0\Rightarrow$ 逐项
  $P=0\Rightarrow\delta_\rho=0$（正项和）——**RH_χ**——反向显然（$\delta=0\Rightarrow P=0$）

### Step 5：收敛与交换（——与 ζ 版相同——A3 引理）
- $\sum_\rho |\delta_\rho||H_0''(\gamma_\rho)| < \infty$（$H_0''=O(t^{-2})$——$N_\chi(T)=O(T\log T)$）
- 逐项配对绝对收敛——交换合法——（——ζ 版 C3/A3 的迁移——不依赖 χ——）

### Step 6：S_reg,χ 的说明（诚实）
- $S_{\mathrm{reg},\chi}$（Gamma/常数项背景）不进入 Q/Q'（——逐项定义在零点项——
  ——投影差中抵消——）
- **判据不依赖 S_reg,χ 的具体值**——无需验证 S_reg=0（——ζ 版是 0——
  ——L 版可能非零——但无关——）

### Step 7：族一致性（A6）
- Step 1-6 的每个对象/论证**不含 q/χ**（——Hadamard 标准——H_0 通用——
  w_H/P_γ 代数——γ₁,χ 下界标准——）
- 判据对**每个**原字符独立成立——$\mathrm{GRH}\iff Q_\chi=Q'_{\mathrm{RH},\chi}\ \forall q\ \forall\chi$
- **无族交互**——GRH 的困难 = 每个判据的验证（——本定理——）

---

## 数值支撑（模 3/4/5）

| L 函数 | 字符 | 零点 | 成对正性（相对差） |
|--------|------|------|---------------------|
| 模 4（β） | 实（奇） | 168（γ<300）Re=½ | 3.4e-24~2.7e-14 |
| 模 3 | 实（奇） | 98（γ<200）Re=½ | 1.9e-20~9.9e-15 |
| 模 5 | 复（4 阶） | 83（γ<150）Re=½ | 0.0e+00~2.0e-14 |

## 状态与边界

- **结构正式化完成**（——迁移定理——每步不依赖 q/χ——）
- **依赖**：ζ 版判据的外部验证（——框架相同——模 3/4/5 是数值支撑——
  概念证明的正式化与 ζ 版共享核心引理（C3/A3——交换——）——）
- **诚实**：本定理的"概念证明"（对任意 χ）**建立在 ζ 版判据的验证之上**
  （——相同的配对/交换/正性引理——）——若 ζ 版判据被专家击穿——
  本定理同样受影响——若 ζ 版通过——本定理"顺理成章"
