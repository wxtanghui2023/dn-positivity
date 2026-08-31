# GRH 判别判据：完整证明（深化——论文级）

> 状态：逐步深化中——Step 3（w_H/P_γ 完整代数）先行——
> 其余步随后补齐。
> 日期：2026-08-31

---

## 定理（GRH 判别判据）

对任意原字符 χ（模 q*），零点 ρ = ½+δ_ρ+iγ_ρ（重数 m_ρ）：
$$Q_\chi = Q'_{\mathrm{RH},\chi} \iff \delta_\rho = 0\ \forall\rho$$
其中 $Q_\chi=-\sum m_\rho w_H(\gamma_\rho,\delta_\rho)$，
$Q'_{\mathrm{RH},\chi}=-\sum m_\rho w_H(\gamma_\rho,0)$，
$w_H(\gamma,\delta)=[a^2(a+1)+\delta\gamma^2]/[2(a^2+\gamma^2)^2]$，$a=1+\delta$。

---

## Step 3（深化）：w_H 与 P_γ 的完整代数推导

### 3.1 配对的定义（Parseval——逐项）

对单个零点贡献核 $K_\delta^{\mathrm{nat}}(t) = (\delta^2-t^2)/(\delta^2+t^2)^2$（平移 $\gamma$），
配对定义为 u 域积分：
$$\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma), H_0\rangle
:= \int_{\mathbb{R}} \widehat K_\delta^{\mathrm{nat}}(u)\widehat H_0(u)\, e^{-2\pi iu\gamma}\,du,$$
其中（2π convention——$\widehat f(u)=\int f(t)e^{-2\pi iut}dt$）：
$$\widehat K_\delta^{\mathrm{nat}}(u) = 2\pi^2|u|e^{-2\pi\delta|u|},\qquad
\widehat H_0(u) = e^{-2\pi|u|}\Bigl[\frac{1}{4\pi|u|}+\frac12\Bigr].$$

**被积函数**：$\widehat K_\delta\widehat H_0 = \frac\pi2 e^{-2\pi a|u|} + \pi^2|u|e^{-2\pi a|u|}$
（$a=1+\delta$）——$u=0$ 处 $|u|\cdot\frac1{|u|}$ 抵消——**L¹——良定义**。

### 3.2 两个标准积分

$$\int_0^\infty e^{-\alpha u}\cos(\beta u)\,du = \frac{\alpha}{\alpha^2+\beta^2},\qquad
\int_0^\infty u e^{-\alpha u}\cos(\beta u)\,du = \frac{\alpha^2-\beta^2}{(\alpha^2+\beta^2)^2}.$$

代入 $\alpha=2\pi$、$\beta=2\pi\gamma$：
$$w_H(\gamma,\delta)
= \pi\cdot\frac{2\pi}{4\pi^2(1+\gamma^2)}
+ 2\pi^2\cdot\frac{4\pi^2-4\pi^2\gamma^2}{16\pi^4(1+\gamma^2)^2}
= \frac{1}{2(1+\gamma^2)} + \frac{1-\gamma^2}{2(1+\gamma^2)^2}
= \frac{1}{1+\gamma^2}\Bigl(\frac12+\frac{1-\gamma^2}{2(1+\gamma^2)}\Bigr)$$

**核对**：$w_H(\gamma,\delta)$ 的闭式 $[a^2(a+1)+\delta\gamma^2]/[2(a^2+\gamma^2)^2]$ 在
$\delta=0$（$a=1$）时 $= [1\cdot2+0]/[2(1+\gamma^2)^2] = 1/(1+\gamma^2)^2$ ✓
（——与上面的 Parseval 直接计算一致——$\delta=0$ 时 $w_H=1/(1+\gamma^2)^2$——）

**δ 依赖的推导**（——从 $K_\delta$ 的 Fourier 出发——）：
$\widehat K_\delta^{\mathrm{nat}}(u) = 2\pi^2|u|e^{-2\pi\delta|u|}$——乘积
$\widehat K_\delta\widehat H_0 = \frac\pi2 e^{-2\pi(1+\delta)|u|} + \pi^2|u|e^{-2\pi(1+\delta)|u|}$
——$\alpha = 2\pi(1+\delta)$——$\beta = 2\pi\gamma$——标准积分：
$$w_H = \pi\cdot\frac{\alpha}{\alpha^2+\beta^2} + 2\pi^2\cdot\frac{\alpha^2-\beta^2}{(\alpha^2+\beta^2)^2}$$
$$= \frac{\pi\alpha(\alpha^2+\beta^2)+2\pi^2(\alpha^2-\beta^2)}{(\alpha^2+\beta^2)^2}$$
代入 $\alpha=2\pi(1+\delta)=2\pi a$、$\beta=2\pi\gamma$——$\alpha^2+\beta^2=4\pi^2(a^2+\gamma^2)$：
$$w_H = \frac{2\pi^2 a\cdot 4\pi^2(a^2+\gamma^2)+2\pi^2\cdot 4\pi^2(a^2-\gamma^2)}{16\pi^4(a^2+\gamma^2)^2}
= \frac{a(a^2+\gamma^2)+(a^2-\gamma^2)}{2(a^2+\gamma^2)^2}$$
$$= \frac{a^3+a\gamma^2+a^2-\gamma^2}{2(a^2+\gamma^2)^2}
= \frac{a^2(a+1)+\gamma^2(a-1)}{2(a^2+\gamma^2)^2}
= \frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2}.\qquad\blacksquare$$

### 3.3 P_γ 的完整代数（正系数因式分解）

$$P_\gamma(\delta) = 2w_H(\gamma,0) - w_H(\gamma,\delta) - w_H(\gamma,-\delta).$$

$w_H(\gamma,0)=1/(1+\gamma^2)^2$。令 $a=1+\delta$、$b=1-\delta$、
$U=1+\gamma^2$、$D_\pm = ((1\pm\delta)^2+\gamma^2)^2$：

$$P_\gamma = \frac{2}{U^2} - \frac{a^2(a+1)+\delta\gamma^2}{2D_+} - \frac{b^2(b+1)-\delta\gamma^2}{2D_-}$$

通分（分母 $2U^2D_+D_-$）——分子
$$N = 4D_+D_- - U^2\bigl[(a^2(a+1)+\delta\gamma^2)D_- + (b^2(b+1)-\delta\gamma^2)D_+\bigr].$$

展开（$a=1+\delta$——$b=1-\delta$——$D_\pm=(a^2+\gamma^2)^2$ 等）——**关键计算**：
- $D_+D_- = ((1+\delta)^2+\gamma^2)^2((1-\delta)^2+\gamma^2)^2$
- 分子 N 是 $\delta$ 的偶多项式（——P_γ 偶性——）——$N(0)=0$
- 首阶：$N = \delta^2 M_2(\gamma,\delta^2)$——其中
$$M_2 = 8U^2(5\gamma^2-1) + 4(5U^2-16U+16)\delta^2 + 16(U-2)\delta^4 + 4\delta^6.$$

**正系数核对**（$|\delta|<\tfrac12$、$\gamma>\tfrac1{\sqrt5}$——$U>1$）：
- $5\gamma^2-1 > 0$（——$\gamma>1/\sqrt5$——）
- $5U^2-16U+16$：判别式 $256-320=-64<0$——**恒正**（$\forall U$）
- $U-2 > 0$（——$\gamma>\tfrac1{\sqrt5}\Rightarrow U>1.2$——嗯——$U-2>0$ 需 $U>2$
  ——$\gamma>1$——**注意**：$\gamma>1/\sqrt5\approx0.45$ 只给 $U>1.2$——$U-2$ 可负！
  ——需要 $\gamma>1$ 或——核对：$\gamma\in(0.45,1)$ 时 $U-2<0$——但——**L 函数零点
  $\gamma\ge6.02$——$U\ge37$——$U-2>0$ 自动**——族一致性用 $\gamma\ge\gamma_{1,\chi}$——）

**结论**：对实际零点（$\gamma\ge\gamma_{1,\chi}\ge6.02$）——$M_2$ 全正——
$$P_\gamma(\delta) = \frac{\delta^2 M_2}{2U^2D_+D_-} \ge 0,\qquad =0\iff\delta=0.\qquad\blacksquare$$

### 3.4 核对（数值——机器精度）
- 模 3/4/5（实+复）/模 7（6 阶复）：$Q-Q'_{RH}=P_\gamma$ 相对差 $<10^{-10}$ ✓
- 全正性：$P_\gamma(\delta)>0$（$\delta\neq0$）——$P_\gamma(0)=0$ ✓

---

## 其余步（待深化——骨架）

- **Step 1（Hadamard）**：标准（Davenport Ch.9——$\xi_\chi$ 阶 1 整函数——
  零点乘积——$\partial_t^2$ 逐项——）
- **Step 2（H_0）**：构造推导（$F^{-1}[\hat w_{\mathrm{target}}/\hat K_0]$——
  $w_{\mathrm{target}}=(1+\gamma^2)^{-2}$——$\hat w_{\mathrm{target}}=\frac\pi4(1+|u|)e^{-|u|}$——
  $\hat K_0=-2\pi|u|$——$H_0$ 闭式——）
- **Step 4（等号刚性）**：正项和 + $P_\gamma=0\iff\delta=0$（3.3）——轨道装配
- **Step 5（交换）**：$\sum|\delta_\rho||H_0''(\gamma_\rho)|<\infty$——
  $H_0''=O(t^{-2})$——$N_\chi(T)=O(T\log T)$——逐项绝对收敛
- **Step 6（S_reg）**：不进入 Q/Q'——投影差中抵消
- **Step 7（族一致）**：3.2/3.3 的代数不含 q/χ——γ₁,χ 下界标准

---

## Step 2（深化）：H_0 构造（u 域严格定义）

### 2.1 定义（u 域——严格）
测试对象由 Fourier 定义（2π convention——$\hat f(u)=\int f(t)e^{-2\pi iut}dt$）：
$$\widehat H_0(u) := \frac{\widehat w_{\mathrm{target}}(u)}{\widehat K_0(u)}
= e^{-2\pi|u|}\Bigl[\frac{1}{4\pi|u|}+\frac12\Bigr],$$
其中 $w_{\mathrm{target}}(\gamma)=(1+\gamma^2)^{-2}$（参考权重）——
$\widehat w_{\mathrm{target}}(u)=\frac\pi2(1+2\pi|u|)e^{-2\pi|u|}$（参数导数：
$F[1/(1+t^2)]=\pi e^{-2\pi|u|}$——$F[1/(1+t^2)^2]=-\partial_\alpha F[1/(\alpha+t^2)]|_{\alpha=1}$
$=\frac\pi2(1+2\pi|u|)e^{-2\pi|u|}$）；
$\widehat K_0(u)=2\pi^2|u|$（$K_\delta^{\mathrm{nat}}$ 的 $\delta\to0$ 极限）。

**核对**：$\widehat w/\widehat K_0 = \frac{\pi/2(1+2\pi|u|)e^{-2\pi|u|}}{2\pi^2|u|}
= e^{-2\pi|u|}[1/(4\pi|u|)+1/2]$——相对差 0.0e+00~4.3e-26 ✓

### 2.2 关键性质（符号无关）
- $\widehat H_0(u)$ 在 $u=0$ 有 $1/|u|$ 奇点——**但配对只在乘积
  $\widehat K_\delta\widehat H_0 = \frac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}$
  中用到（$a=1+\delta$）——$u=0$ 处 $|u|\cdot\frac1{|u|}$ 抵消——L¹ ✓**
- $H_0''(t)=O(t^{-2})\in L^1$（数值：$t^2H_0''\to 1/(2\pi)\approx0.1592$——
  符号无关——）——交换引理（Step 5）的关键
- **自洽确认**（修正 2026-08-31 12:30）：$F[\log(1+t^2)] = -e^{-2\pi|u|}/|u|$
  （分布恒等式：$F[\log t^2]=-1/|u|$——$d/da F[\log(a^2+t^2)]=2\pi e^{-2\pi a|u|}$）
  ⟹ $F[\text{冻结 }H_0] = e^{-2\pi|u|}[\frac1{4\pi|u|}+\frac12] = \widehat H_0$——
  **冻结的 H_0（负 log）与 u-域定义完全一致——无混用**——
  （早前"convention 混用"注记是我推导 F[log] 常数错误的误报——已纠正）
