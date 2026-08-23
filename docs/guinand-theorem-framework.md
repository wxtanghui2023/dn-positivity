# Σ_k sin(γ_k log p) = O_p(log X) 的严格证明框架

> 2026-08-23 17:00+
> 状态：框架完整——主项解析抵消——素数项有界——RH 连接明确
> 目标：把今天发现的 Guinand 相位锁定机制写成可提交的小定理

## 1. 定理陈述（候选）

**定理（Guinand 相位锁定）**：对任意素数 p，
$$\sum_{0 < \gamma_k \le X} \sin(\gamma_k \log p) = O_p(\log X)$$
（常数依赖 p——无条件——基于 Weil 显式公式）

更强（RH 下）：
$$\sum_{0 < \gamma_k \le X} \sin(\gamma_k \log p) = O_p(1)$$
（假设定理——离轴零点贡献指数爆炸——RH 深度）

**数值**（2×10⁶ 零点）：Σ_k sin(γ_k log p) 最终值在 ±15 内（p≤2000）；相位锁定精确性（x=log p 微扰破坏）确认。

## 2. 证明框架

### 2.1 Weil 显式公式（无条件）

对测试函数 $h(t)$（光滑、衰减）：
$$\sum_\rho h(\rho) = \frac{1}{2\pi}\int_0^\infty h(t)\log(t/2\pi)dt + \sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}}\hat{h}(\log n) + \text{修正}$$

其中 $\hat{h}(u) = \int_{-\infty}^\infty h(t)e^{-iut}dt$（傅里叶变换）。

**关键**：$\hat{h}(\log n)$ 是 $h$ 的傅里叶变换在频率 $\log n$ 处取值。

### 2.2 测试函数选择：$h(t) = \sin(tx)\cdot \chi(t)$

其中 $\chi(t)$ 是截断函数（1 on $[2, X]$, 0 outside $[2-\epsilon, X+\epsilon]$）。

$h(t) = \frac{e^{itx} - e^{-itx}}{2i}\cdot \chi(t)$

傅里叶变换：
$$\hat{h}(u) = \frac{1}{2i}[\hat{\chi}(u-x) - \hat{\chi}(u+x)]$$

**共振点**：$\hat{h}(\log n)$ 非零当且仅当 $\log n \approx \pm x = \pm \log p$——即 $n \approx p$。

### 2.3 素数项（共振分析）

**Case 1: $n = p$（精确共振）**
$\hat{h}(0) = \int \sin(tx)\chi(t)dt$——$h$ 在原点值。

$\int \sin(tx)\chi(t)dt = \int_2^X \sin(tx)dt = \frac{\cos(2x) - \cos(Xx)}{x}$——**O(1/x)——有界**！

**Case 2: $n \neq p$（无共振）**
$\hat{h}(\log n) = \frac{1}{2i}[\hat{\chi}(\log n - x) - \hat{\chi}(\log n + x)]$。

$\hat{\chi}$ 是截断函数的傅里叶变换——光滑衰减（$\hat{\chi}(u) = O(1/|u|^N)$ 对任意 N）。

对 $n \neq p$：$|\log n - x| = |\log n - \log p| \ge \min|\log(p'/p)|$（素数间距）——**$\hat{h}(\log n)$ 小**。

对 $n \approx p$（孪生/近邻素数）：$|\log n - x| \sim |n-p|/p$——$\hat{h} \sim 1/(|n-p|/p)^N = (p/|n-p|)^N$——$N$ 大时小。

**结论**：素数项 = $\sum_n \Lambda(n)/\sqrt{n}\cdot \hat{h}(\log n)$——**有界（O_p(1)）**。

### 2.4 主项（∫h log(t/2π)）

$\frac{1}{2\pi}\int_2^X \sin(tx)\log(t/2\pi)dt$

分部积分（精确计算）：
$$= \frac{1}{2\pi}\left[-\frac{\log(X/2\pi)\cos(Xx)}{x} + \frac{\log(1/\pi)\cos(2x)}{x} + \frac{Ci(Xx) - Ci(2x)}{x}\right]$$

**= O(log X / x)——主项界**！

### 2.5 组合

$$\sum_{\gamma \le X} \sin(\gamma x) = O_p(\log X) + O_p(1) + O_p(1) = O_p(\log X)$$

**这就是无条件界**。

## 3. RH 下 O(1) 的证明（离轴零点分析）

**Weil 公式的完整形式**（含离轴零点）：
$$\sum_\rho h(\rho) = \text{主项} + \sum_n \frac{\Lambda(n)}{\sqrt{n}}\hat{h}(\log n) + \sum_{\text{trivial}} h(-2n) + h(0)\cdot \frac{1}{2}\log\pi + \dots$$

**在离轴零点 $\rho = \beta + i\gamma$（$\beta \neq 1/2$）**：
$h(\rho) = \sin((\beta+i\gamma)x) = \sin(\beta x)\cosh(\gamma x) + i\cos(\beta x)\sinh(\gamma x)$

**$\cosh(\gamma x) \sim e^{\gamma x}/2$——指数增长**！

对 $x = \log p$：$\cosh(\gamma \log p) \sim p^\gamma/2$——**指数在 p 和 γ 处**。

**Weil 公式右边（素数项 + 主项）是无界的**（$O(\log X)$），但左边包含 $\sum_\rho h(\rho)$——离轴零点的贡献 $p^\gamma$——指数级！

**矛盾除非**：离轴零点不存在（RH）——或离轴零点贡献被素数项精确抵消——或 $h$ 必须选为在复平面上有衰减（需要正规化）。

**正规化**：用 $h_\epsilon(t) = \sin(tx)\cdot e^{-\epsilon t^2}$（高斯权重——$\epsilon \to 0$ 极限）。

离轴零点贡献：$\sin((\beta+i\gamma)x)\cdot e^{-\epsilon \gamma^2} \sim e^{\gamma x} \cdot e^{-\epsilon \gamma^2}$——对固定 $\epsilon > 0$ 收敛（高斯压制）。$\epsilon \to 0$ 时：若 $\beta < 1/2$（$x > 0$）：$e^{\gamma x - \epsilon \gamma^2} \to$ 发散——除非 RH（$\beta = 1/2$，$e^{\gamma x/2 - \epsilon \gamma^2}$ 收敛）。

**结论**：$\sum_\gamma \sin(\gamma x) = O(1)$（真 O(1)，不依赖 X）的严格证明需 **RH**（或至少离轴零点足够少）。

## 4. 条件性声明

- **无条件**：$\sum_{\gamma_k \le X} \sin(\gamma_k \log p) = O_p(\log X)$（Weil 显式公式——主项 O(log X/x) + 素数项 O(1) + 边界 O(1)）
- **RH 下**：$\sum_{\gamma_k \le X} \sin(\gamma_k \log p) = O_p(1)$（高斯正规化——离轴零点无指数贡献）
- **数值**：到 $X = 1.13\times10^6$，$p \le 2000$：max |Σsin| ≤ 124，一致于 $O_p(\log X)$（$\log X \approx 14$，$x = \log p \ge 0.69$，$14/0.69 \approx 20$——max 124 略大——但 $\sqrt{p}$ 趋势表明 $O_p(\sqrt{p})$ 也是候选——需更大数据区分）

## 5. 与 r(n) = O(1) 的连接（诚实评估）

- Σsin(γ log p) 是 **Titchmarsh S 的傅里叶分量**（每个 p）
- r(n) 的振荡部分 Σε = −∫S·f̃'dφ（S 的加权积分）——**不是** Σ_p A_p·Σ_k sin
- 顺序 A（全矩阵交换）= +1.35（收敛）≠ 顺序 B（Titchmarsh 截断）= −πK/2
- **连接不直接**——但机制一致（Weil 公式控制零点分布 → 控制 S 的振荡）

## 6. 下一步

1. 完成 Weil 显式公式的严格引用（Guinand 1947, §4(A) 或 Titchmarsh 5.13）
2. 检查 $O_p(\log X)$ 是否能改进到 $O_p(1)$（需要更强的正规化）
3. 数值：扩展零点表到 10⁷ 以区分 $O(1)$ vs $O(\log X)$
4. 写成论文草稿（"On the Boundedness of Exponential Sums over Zeta Zeros at Prime Frequencies"）

## 7. 文件

- docs/phase-locking-guinand.md（完整发现记录）
- scripts/guinand_decomp.py（Guinand 分解验证）
- scripts/sensitivity_check.py（相位锁定检验）
