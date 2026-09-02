# P49-G2.7.3-P1-R1：多 N 扫描 + 新理论洞察（谱密度匹配）

> 2026-09-02 14:25 · g₋ 趋势未收敛 · odd f**f 正定偶性 · 谱密度匹配视角

## P1-R1 封口（唐先生判定：PASS / Odd-sector mechanism identified）
- 粗谱范数路线 CLOSED（too coarse——证明 P1 不能被逐项绝对值化）
- odd ground 数值 PASS（substantial negative coupling）——"odd = weakly coupled" REJECTED
- **新机制：oscillatory phase/correlation incompatibility**（odd 不能同时耦合——非不耦合）
- V₀ dominance strong numerical——uniform odd lower bound OPEN——**Odd Prime-Correlation Lemma THEOREM CANDIDATE**——full simple-even OPEN
- **对象**：m₋(λ,N) = λmin(Q_prime|E_N⁻)——q₀(λ) = Q_prime(V₀)——目标 m₋ > q₀ + uniform gap
- 下一步：先多 N 扫描（非 Riemann-Lebesgue——N→∞ 允许高频——⟨Tf,f⟩ 二次型非线性积分）

## 多 N 扫描结果
**λ=3（q₀ = −2.141）**：m₋：+0.21(N2) → −0.24(N3) → −0.54(N4) → −0.90(N6) → −1.05(N8) → −1.33(N10) → −1.47(N12) → −1.55(N15) → **−1.80(N20)**——g₋ = m₋−q₀：2.35 → 1.60 → 1.24 → 1.09 → 0.81 → 0.67 → 0.59 → **0.34(N20)**
**λ=4（q₀ = −3.467）**：m₋：0.46(N2) → −0.31(N4) → −0.57(N6) → −0.99(N8) → −1.20(N10) → −1.50(N15) → **−1.89(N20)**——g₋：3.92 → ... → **1.58(N20)**

## ⚠️ 关键观察
1. **g₋ 持续下降（未 plateau）**——λ=3: 2.35→0.34——**m₋ 向 q₀ 逼近？**——降速放缓（N=15→20: −1.55→−1.80——降 0.25）——**未收敛——需更大 N 或解析判断**
2. **odd ground 永远用最高可用模式**（N=20 用 o16,o19,o20——o_N 类）——M_high ≈ 1.0——**无自然频率截断迹象**
3. **⚠️ 风险**：若 trend 继续——m₋ → q₀（λ=3: N=20 已 −1.80 vs q₀ −2.14）——P1 失败——若频率有解析截断——m₋ 收敛 > q₀

## 新理论洞察（odd f 的 f**f 结构）
- **odd f 的 (f**f)(u⁻¹) = (f**f)(u)**（偶性——推导：f(1/(uv)) = −f(uv)——换元得 (f**f)(u⁻¹) = (f**f)(u)）——⟹ **⟨T(n)f,f⟩ = n^{−1/2}·2(f**f)(n)**（简化！）
- **(f**f) 是正定函数**（Fourier = |f̂|² ≥ 0——对实 f）——(f**f)(y) = ∫|f̂(t)|²e^{ity}dt/2π
- **odd f 的 f̂ 纯虚奇**（F(−x) = −F(x) ⟹ F̂(t) = −i∫F(x)sin(tx)dx——纯虚奇）——|f̂|² 偶
- ⟹ **问题 = 谱密度匹配**：最大化 ΣΛ(n)n^{−1/2}(f**f)(logn)（负方向）——需要 |f̂|² 集中匹配 {logn} 采样——受 ∫|f̂|² = 2π‖f‖² 约束
- **⚠️ 分叉**：若 odd 的 |f̂|² 可任意集中（匹配任意素数频率集）——m₋ → q₀（P1 失败）——若正定性 + odd 约束（f̂ 纯虚奇——|f̂|² 的额外结构）限制匹配——m₋ 收敛 > q₀（P1 成立）

## 判定
- **扫描显示风险**（g₋ 未收敛——持续降——odd 用最高频率）
- **理论洞察给出判断工具**（谱密度匹配——|f̂|² 与 {logn} 采样）——**正定性约束可能救 P1**（(f**f) 正定——不能任意匹配——类似 V₀ 的常数 |f̂|² = δ₀ 是唯一的"全匹配"——odd 的 |f̂|² 无 δ₀ 分量（f̂(0) = 0——odd）——可能给 gap）
- ⚠️ 诚实：未定论——需更大 N 或谱密度分析

## 下一步候选
- (a) 更大 N（λ=3: N=25,30,40——判断 g₋ 是否收敛/趋零）
- (b) 谱密度分析（odd 的 |f̂|² 约束——f̂(0)=0（odd）——正定函数匹配 {logn} 的上界——Odd Prime-Correlation Lemma 证明核心）
- (c) 唐先生指示
