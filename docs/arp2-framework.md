# ARP-2——关系闭环/算术曲率（第二代——机制跃迁）

> 2026-09-07 17:40 · 唐先生：ARP-1 完成——ARP-2 = 关系闭环/算术曲率——非加复杂 kernel

## ARP-1 死亡升华（NO-GO 定理雏形——）
**若算术关系核可通过与 s 无关的正交/三角/因子格变换分解为非负平方和——则该正性不可能产生 Re s = ½ 的谱边界。**
- G_s = D_α·A_gcd·D_α——Möbius/Smith 分解——正性 ⊥ σ-定位
- 保留为结构性结论（非单候选失败——）

## ARP-2 机制跃迁
- 从"矩阵元素描述 m↔n 一条关系"→"正性描述**关系之间能否闭合**"
- graph kernel K(m,n) → triangle/cycle kernel K(m,n,r)
- **不是复活 Rédei**（Rédei 找三元不变量——这里找闭环缺陷的正性——）

## 候选空间（φ_s(m,n) 三条件——）
1. 反射：φ_{1−s̄}(m,n) = conj(φ_s(n,m))
2. 非可分离：φ_s(m,n) ≠ f_s(m)conj(f_s(n))
3. 有限算术关系定义

## 具体候选（差商 × gcd——乘法-加法耦合——）
φ_s(m,n) = Σ_{d|(m,n)} w(d)·Ψ_s(m/d, n/d, |m−n|/d)
- u, v, u−v 同时出现——非 additive convolution 非纯 Euler——中间点
- |m−n|/d 不能被写成 f(u)conj(f(v))

## 五关审计（A-E——）
- A 可分离性：φ_s = Σ f_j,s(m)conj(f_j,s(n))？→ 死
- B 因子格可对角化：s-无关 U 使 U*K_s U = D_s（符号固定算术权重）→ 死
- C cycle defect：Ω_s(m,n,r) = φ(m,n)φ(n,r)φ(r,m) − φ(n,m)φ(r,n)φ(m,r)——恒等 0 = flat → 死
- D 反射：Ω_{1−s̄} = conj(Ω_s)——无则不能锁 ½
- E σ-刚性：σ ≠ ½ 是否制造负方向——全 strip ≥ 0 → 死

## 元价值
若 ARP-2 全 flat/可分离/Hecke 化/退化 circle-sieve-Weil——强结论：
**所有 pairwise arithmetic positivity 若无不可消除 cycle curvature——无法产生 RH 型谱刚性**
⟹ 解释为什么前面路线死在同一处——回头处理 II（弱自伴——）

## R3 缺口精炼
coefficient positivity → pairwise relation positivity → ??? arithmetic curvature positivity → Re ρ = ½
