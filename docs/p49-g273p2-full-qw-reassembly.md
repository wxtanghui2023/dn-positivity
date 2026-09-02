# P49-G2.7.3-P1-R3d 收档 + P2 定义（Full-QW High-Precision Sector Reassembly）

> 2026-09-02 14:45 · 唐先生判定 · prime dominance CLOSED · full-QW joint spectral 转向

## P1-R3d 收档（唐先生：PASS — Strong Numerical No-Go Candidate）
- **prime-sector uniform gap CLOSED**：N=120: m₋ = −2.164 < q₀ = −2.1407——有限维反例击穿 Q_prime(f) ≥ q₀+δ_λ
- **关闭的是"prime sector 本身产生 even-simple ground"——不是"CCM full QW 不可能有 even ground"**
- **coherence 机制**：m_LP 饱和 −1.874 vs m_exact 持续降——off-diagonal coherence = 穿透机制——问题升级：finite logarithmic sampling + coherent PSD spectral measure extremal
- **pointwise correlation deficit ⟹̸ quadratic-form gap**（审计结论——负定硬 gap 猜想不能作证明路线）
- **G2.7.3 分层**：Z₂ block ✓ CLOSED——divided-difference ⟹ even ✗ NO-GO——prime uniform gap ✗ CLOSED——V₀-dominance ✗ CLOSED——single-mode/sinc ✗ CLOSED——**full-QW even ground OPEN（真正核心）**——CCM simple-even OPEN
- **P1 正式收档 No-Go**——不再耗轮次于 prime exclusion lemma

## P2：Full-QW High-Precision Sector Reassembly（唐先生定义）
**三目标**：
1. 正确 w_n（von Mangoldt）和 W_{0,2} 规范重新构造完整矩阵
2. **W_∞ 不用粗 trapz——解析/振荡积分**（之前 trapz 精度不足——total 翻转可能伪影）
3. 扫描 N=20,40,60,80,100,120——记录 λ₊, λ₋, Δ_full, Δ_{0,2}, Δ_∞, Δ_prime
**关键量**：**R_N = (Δ_{0,2} + Δ_∞)/|Δ_prime|**
- R_N > 1+ε 稳定 → joint coercivity 路线可能
- R_N → 1 或 < 1 → full-QW even-simple ordering 也经历 degenerating cancellation
**警告**：不能只看 N=4,6（灾难性抵消 O(1)+O(1)→O(10⁻²)）——需 spectral stability test

## 执行状态
- P1-R3d 收档完成——P2 启动——W_∞ 高精度积分测试（trapz vs quad——total 翻转伪影检查）
- 结构：QW = W_{0,2}（±i/2 交叉——秩 2）+ W_∞（∂_tθ 乘子）+ Q_prime（von Mangoldt——修正）
- M2[k,m] = ∫f̂_k conj(f̂_m)·∂_tθ/π dt——f̂_k(t) = L^{−1/2}e^{itL/2}(1−e^{−itL})/(it−2πik/L)
