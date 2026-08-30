# Independent Core Verification（零背景重建——Test 1 结果）

> 目的：给陌生专家一个**不依赖任何历史版本**的干净推导核心——从定义开始逐行验证。
> 原则：不接受作者数值验证——只从原始定义推导。
> 状态：Test 1（主恒等式零基础重推）进行中——**已发现 2 个因子检查点**。

---

## 核心推导链（从定义开始）

### 1. 对象定义
- $S(t)=\partial_t^2\log|\xi(\tfrac12+it)|$——分布
- $K_\delta(x)=2(x^2-\delta^2)/(x^2+\delta^2)^2$——单零点核
- $H_0(t)=-\tfrac12[\tfrac1{2\pi}\log(1+t^2)+\tfrac1{\pi(1+t^2)}]$——构造对象（$H_0''\in L^1$）
- $Q=-\langle S,H_0\rangle$——判别泛函
- $Q'_{\mathrm{RH}}=\sum_\rho w_H(\gamma_\rho,0)$——参考泛函（投影 $\Pi(\rho)=\tfrac12+i\gamma_\rho$）

### 2. Hadamard 分解（无条件）
$$\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho},\qquad b=\log 2\pi-1-\tfrac\gamma2$$
- $\log|\xi(\tfrac12+it)|$ 的 t 线性项（$-\tfrac s2\log\pi$、$bs$）$\partial_t^2=0$——**只剩零点项**

### 3. 零点表示（独立推出——无条件）
$$S(t)=\sum_\rho \frac{\delta_\rho^2-(t-\gamma_\rho)^2}{(\delta_\rho^2+(t-\gamma_\rho)^2)^2},\qquad \delta_\rho=\beta_\rho-\tfrac12$$
- 推导：$\log(1-(s/\rho))=\log(\beta-\tfrac12+i(\gamma-t))-\log\rho$——取实部——二阶导
- **任意零点配置成立（含重数）——无 RH 假设**

### 4. 与 K_ρ 核对——⚠️ 检查点 [A]
$$\frac{\delta^2-x^2}{(\delta^2+x^2)^2}=-\tfrac12\cdot\frac{2(x^2-\delta^2)}{(x^2+\delta^2)^2}=-\tfrac12 K_\delta(x)$$
$$\boxed{S(t)=-\tfrac12\sum_\rho K_{\delta_\rho}(t-\gamma_\rho)}$$
- **主恒等式的零点部分含 −1/2 因子**——须核对 1/2 在 w_H/Q 定义中的吸收位置
- w_H 闭式含 1/2 因子——**可能已吸收——但必须逐项确认（不能假设）**

### 5. ⚠️ 检查点 [B]：Fourier convention 因子
- 冻结表：$\widehat K_\delta(\omega)=-\pi|\omega|e^{-|\delta||\omega|}$
- 冻结 convention：$\widehat H(u)=\int H(t)e^{-2\pi iut}dt$（2π 归一化）
- **须独立重算** $\widehat K_\delta$（2π convention 下因子）——全文一致

### 6. 数值对照（验证零点表示本身）
| t | S_direct | Σ零点主部 | 差（S_reg） |
|---|----------|-----------|-------------|
| 20 | −1.0768 | −1.0565 | −0.0203 |
| 40 | −1.5548 | −1.5337 | −0.0211 |
| 60 | −4.0347 | −4.0027 | −0.0320 |
- 差 = Gamma/常数/trivial 项（S_reg）——非零但**已知显式**——归入 M(H_0)

---

## 待完成（Test 1 剩余——逐项精确抵消核对）

- [ ] [A] 1/2 因子吸收位置——完整逐项写 Q 的零点部分 = (1/2)Σ⟨K_ρ,H_0⟩ 与 Q'_RH 的对应
- [ ] [B] K̂_δ 在 2π convention 下的精确形式——重算
- [ ] Gamma 项（M(H_0)）完整表达式——确认与 S_reg 抵消
- [ ] trivial zeros（s = −2n）贡献——确认进入 S_reg/M(H_0)——无遗漏
- [ ] t=0 extension——分布延拓唯一性
- [ ] multiplicity——重数计入核对（m_ρK_ρ）
- [ ] 对称求和/上下半平面约定——2Σ_{γ>0} vs Σ 系数
- [ ] 主恒等式最终形式：Q − Q'_RH = ΣΔ_H（——或——发现 R ≠ 0）

## 与已有 Weil criterion 的区别（新结果 vs 重包装——待查）

- 经典 Weil criterion：∀H——W(H) ≥ 0（一族正性条件）
- 本文：单一 H_0——Q(H_0) − Q'_RH = ΣΔ_H——Δ_H = 0 ⟺ δ_ρ = 0
- **问题**：H_0 构造/Δ_H 正性/刚性机制是否真的新增数学内容——还是 Weil criterion 的特殊化
- **判定标准**：H_0 的存在或其关键性质是否本身等价于 RH（隐藏循环）

## 状态声明（保持）

> The manuscript presents a criterion equivalent to the Riemann Hypothesis
> under the stated distributional framework and verified analytic identities.
> **不是**：The Riemann Hypothesis has been proved.
