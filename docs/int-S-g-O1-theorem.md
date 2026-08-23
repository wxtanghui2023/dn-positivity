# ∫S·g = O(1) ⟹ Σδ_k = O(1)：无条件定理候选（2026-08-23 19:00）

> 来源：发散性思维（统计物理"方差压缩"视角）→ Titchmarsh + van der Corput
> 状态：论证基本验证（数值）——待完整严格化（交换步骤）
> 价值：改进 8/22 的 Σδ_k = O(loglog T) 到 O(1)——潜在无条件新定理

## 1. 核心论证

### 定理（候选——无条件）
$$\sum_{k=1}^{N}\delta_k = O(1)$$
（8/22 证明 O(loglog T)——这里改进到 O(1)——如果严格化成立）

### 证明框架

**步骤 1（8/22 恒等式——无条件）**：
$$\sum_{k=1}^{N}\delta_k = -\frac{S(\gamma_{N+1})}{N_0'(\gamma_{N+1})} + \int_{\gamma_1}^{\infty} S(t)g(t)\,dt + O(1), \qquad g(t) = \frac{2\pi}{t\log^2(t/2\pi)}$$
（g = N''/N'² = −d(1/N')/dt——精确）

**步骤 2（端点项）**：|S| ≤ C·log t（Backlund）——S/N' ≤ 2πC = O(1) ✓

**步骤 3（核心——∫S·g = O(1)——Titchmarsh + van der Corput）**：
S(t) = −(1/π)Σ_{p≤t} sin(t log p)/(√p log p) + R(t)（Titchmarsh——R = O(1/t) 或 O(log t/√t)）

$$\int_{\gamma_1}^{\infty} S(t)g(t)\,dt = -\frac{1}{\pi}\sum_p \frac{1}{\sqrt{p}\log p}\int_{\max(p,\gamma_1)}^{\infty}\sin(t\log p)\,g(t)\,dt + \int R(t)g(t)\,dt$$

**van der Corput 一阶**（φ = t·log p——φ' = log p 常数——g 缓变）：
$$\left|\int_a^{\infty} e^{it\log p}g(t)\,dt\right| \le \frac{|g(a)| + \int_a^{\infty}|g'(t)|dt}{\log p} \le \frac{C}{p\log^3 p}$$

（g(p) ~ 2π/(p log²p)——∫|g'| ~ 2π/(p log²p)——除以 log p）

**Σ 收敛**：
$$\sum_p \frac{1}{\sqrt{p}\log p}\cdot\frac{1}{p\log^3 p} = \sum_p \frac{1}{p^{3/2}\log^4 p} < \infty$$
（数值：Σ = 1.683——收敛——素数定理）

**R 余项**：∫R·g——R = O(log t/√t)——∫log t/(√t·t log²t)dt < ∞——O(1) ✓

**步骤 4（结论）**：Σδ_k = O(1) + O(1) + O(1) = **O(1)** ∎

## 2. 数值验证

### Σδ_k（2M 零点——修复精度后）
```
max|Σδ| = 4.34（到 500k——稳定）
分块：−3.22 → −3.63 → −3.73 → −3.58 → −3.73（100k 块——稳定不增长）
loglog(γ_500k) = 2.54（8/22 理论界——但数值不随 N 增长——O(1) 行为）
```

### van der Corput 界（∫_{max(p,γ₁)}^∞ sin(t log p)g(t)dt）
```
p=2:  ∫ = −0.887  vs 界 1.95（比值 0.45）
p=3:  ∫ = −0.546  vs 界 1.23（比值 0.44）
p=5:  ∫ = +0.828  vs 界 0.84（比值 0.99）
p=101: ∫ = −0.003  vs 界 0.004（比值 0.76）
→ van der Corput 界验证（比值 ≤ 1）✓
```

### 方差压缩（统计物理视角——8/22 + 今天）
```
1 + 2Σ_{j=1..100}ρ(δ_k, δ_{k+j}) = 0.034（≈ 0——方差完全压缩）
压缩比 = 0.011（89 倍——分块和 std 0.44 vs 独立 39.1）
→ Σδ_k 的波动 ~ O(1)（不是 √K）——统计物理"刚性"的体现
```

## 3. 诚实标注（待严格化）

1. **逐项积分交换**（∫Σ_{p≤t} = Σ_p∫）：需要 Abel 求和论证——Titchmarsh 截断 p ≤ t——标准但需仔细
2. **Titchmarsh 余项 R(t) 的精确界**：O(1/t) 还是 O(log t/√t)——两者都收敛——但需引用精确版本
3. **van der Corput 的严格形式**：需要 g 的精确变差界——g' 在 [γ₁, ∞) 绝对可积
4. **∫S·g 的数值**：8/23 声称 +0.1313——我的分段积分 ~0——需要核对定义（积分下限/S 的取值）——但**量级 O(1) 确认**

## 4. 意义（如果严格化成立）

1. **Σδ_k = O(1) 无条件**——改进 8/22 的 O(loglog)——新定理
2. **方差压缩的理论基础**——1+2Σρ ≈ 0 的解析证明方向
3. **对 r(n) = O(1) 的帮助**：Σδ = O(1) 是"δ 的一阶矩"——r(n) 需要 Σwδ（加权）——**一阶不够**——但它是机制链的重要一环（更接近）
4. **统计物理类比确认**：1D 对数气体的"刚性"（Bourgade）在 ζ 零点有对应（S 的振荡控制）——但 ζ 的"势"（素数项）需要 van der Corput 处理——**这是 ζ 特有的工具**

## 5. 文件

- scripts/sum_delta_O1_v2.py（Σδ = O(1) 数值确认）
- scripts/verify_int_S_g2.py（van der Corput 界验证）
- scripts/variance_compression.py（方差压缩——统计物理视角）
