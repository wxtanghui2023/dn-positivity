# P49-G2.7.3-P1：Odd-Sector Exclusion Lemma——启动

> 2026-09-02 14:18 · 唐先生 P1 定义 · V₀ 主导 → prime variational gap → full-QW simple-even

## 状态升级（唐先生）
- **G2.7.3-R2c-R2: PASS — V₀-Dominated Prime-Sector Mechanism**——不封 simple-even（缺 uniform inequality）
- **关键结构**：λmin(Q_prime|E_N⁺) ≈ Q_prime(V₀) = −2Σ_{n≤λ²}Λ(n)n^{−1/2}(L−logn)/L——odd 无 V₀ 方向——**目标：inf_{f∈E_N⁻}Q_prime(f) > Q_prime(V₀) + controlled correction**
- **技术修正**：f(1)=0 不能直接作证明（Q_prime 涉及所有 T(n)——f(1)=0 只灭一个方向）——**需 |⟨T(n)f,f⟩| ≤ B_n‖f‖²（f odd）——ΣΛ(n)B_n < −Q_prime(V₀）或精细 Rayleigh 比较**
- **三层结构**：V₀ dominance（强数值 + 解析公式）→ **prime-sector variational gap（当前 theorem target）** → full-QW simple-even（perturbation estimate）
- **G2.7.3 OPEN 压缩**：证明 odd sector 无法通过 T(n) 加权组合弥补失去 V₀ 常数方向的 Rayleigh gap

## G2.7.3-P1：Odd-Sector Exclusion Lemma（五步）
1. T(n) 在 log 坐标的作用精确写出
2. Z₂-odd 条件的 u=1 消失 + 卷积对称性
3. sup_{‖f‖=1, f∈E_N⁻}|⟨T(n)f,f⟩| 的界
4. Λ(n) 加权求和
5. 与 V₀ Rayleigh quotient 比较——目标：λmin(Q_prime|E_N⁻) − Q_prime(V₀) ≥ c_{λ,N} > 0

## T(n) log 坐标结构（步骤 1-2 初步）
- T(n)：⟨f|T(n)g⟩ = n^{−1/2}[(f**g)(n) + (f**g)(n⁻¹)]——乘法卷积——log 坐标 = 加法卷积在 ±log n
- V_k 支撑 log u ∈ [−L/2, L/2]（κ 平移）——(V_k**V_m)(n) = e^{2πim·logn/L}(1−e^{2πi(k−m)logn/L})/(2πi(k−m))（前推导）
- odd f（f(u⁻¹)=−f(u)）：u=1（log u=0）消失——λ-坐标 x=L/2 处 f=0
- **⟨T(n)f,f⟩ = n^{−1/2}[(f**f)(n) + (f**f)(n⁻¹)]——odd 的卷积对称性待用**

## 数值验证计划（P1 步骤 3-4 数值版）
- B_n = ‖T(n)|_{E_N⁻}‖（odd 块谱范数——T(n) 自伴）
- 验证核心不等式：Σ_{n≤λ²}Λ(n)·B_n < −Q_prime(V₀)（= 2ΣΛ(n)n^{−1/2}(L−logn)/L）
- 若成立——定理目标的数值支持（V₀ 值主导 odd 总耦合）
