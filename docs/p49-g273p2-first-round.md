# P49-G2.7.3-P2：第一轮——W_∞ 精度瓶颈暴露（total 重建不可信）

> 2026-09-02 14:48 · W_∞ 积分精度致命 · total 翻转伪影候选 · 需解析积分

## P2 定义（唐先生）
- Full-QW High-Precision Sector Reassembly——三目标：①正确 w_n/W_{0,2} 规范 ②W_∞ 解析/振荡积分（非粗 trapz）③N 扫描记录 λ₊λ₋Δ_full/Δ_{0,2}/Δ_∞/Δ_prime
- 关键量：R_N = (Δ_{0,2}+Δ_∞)/|Δ_prime|——>1+ε = joint coercivity 可能——→1/<1 = degenerating cancellation
- 警告：不能只看 N=4,6（灾难性抵消）——需 spectral stability test

## P1-R3d 收档（前轮）
- prime-sector uniform gap CLOSED（N=120: m₋ < q₀——odd 穿透）——coherence 机制——P1 正式 No-Go
- G2.7.3 核心转 full-QW even ground（OPEN）

## ⚠️⚠️ P2 第一轮——W_∞ 精度瓶颈（决定性发现）
1. **trapz vs mpmath quad 差 1e-2~1e-3**：M2[1,1]: 0.461 vs 0.475（差 1.4e-2）——M2[2,2]: 差 2.3e-3——**对 O(1e-2) 的 total Δ 致命**
2. **M2[0,0] 不稳定**：两次 trapz（同 dt=0.005/tmax=150）给 −2.72 和 −1.14——**不收敛/依赖细节**
3. **quad 对 t=0 奇点 nan**（f̂₀ 的 (it−0) 分母——可去但 quad 失败）
4. **∂_tθ 变号**（t=0: −½logπ = −0.57 < 0——大 t: ~½log(t/2π) > 0）——W_∞ 非正定乘子——M2 对角可负
5. **⟹ total 翻转（N=4 even +0.003/N=6 odd −0.018）不可信——可能是 W_∞ 积分误差伪影**

## 判定
- **P2 目标 1（w_n/W_{0,2} 规范）基本完成**（q₀ 与直接矩阵一致）
- **P2 目标 2（W_∞ 解析/振荡积分）未达成——当前瓶颈**——trapz 精度不足——quad t=0 失败
- **total Δ/R_N 的任何结论推迟**——直到 W_∞ 高精度

## W_∞ 解析路径（下一轮核心）
- M2[k,m] = ∫f̂_k f̂_m̄·∂_tθ/π dt——f̂_k f̂_m̄ = (2/L)(1−cos(tL))/[(it−a_k)(−it−a_m)]
- 分解：(1−cos(tL)) 项——∫∂_tθ/[(it−a_k)(−it−a_m)]（缓变——quad 可行）——∫cos(tL)∂_tθ/[...]（振荡——围道/留数——∂_tθ = −½logπ + ½Imψ(¼+it/2)——ψ 极点）
- 或：sin²(tL/2) 周期平均 + 近极点精确修正（半周期技术）

## 下一步候选
- (a) W_∞ 解析积分（围道/留数——ψ 极点结构——或半周期平均+修正——P2 目标 2 核心）
- (b) 用 mpmath 高精度逐元 quad（避开 t=0——分区间——慢但 N 小可行——验证 trapz 误差量级）
- (c) 唐先生指示
