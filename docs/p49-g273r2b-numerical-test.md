# P49-G2.7.3-R2b：μ₊<μ₋ 数值结构测试——divided-difference parity 矩阵

> 2026-09-02 14:02 · 数值实验 · Section 5 结构 · even ground 非自动

## 设置
- Section 5 矩阵：τ_ij = a_i (i=j), (b_i−b_j)/(i−j) (i≠j)——a_{−j}=a_j, b_{−j}=−b_j
- γ(V_j) = V_{−j}——even = 对称组合 (V_k+V_{−k})/√2——odd = 反对称
- 测试：随机/参数化 b_n（奇）+ a_n（偶）——计算 μ₊ = min Spec(even block), μ₋ = min Spec(odd block)

## 结果
1. **Z₂ 块对角验证 ✓**（mix ~ 1e-17——修复正确）
2. **随机 parity divided-difference（300）：even ground 58%——odd ground 42%——结构不普遍给 μ₊<μ₋**
3. **衰减族测试**（a_n = 1）：
   - b~1/n：μ₊<μ₋ False（N=8: μ₊=−0.086, μ₋=−1.405——**odd ground——odd 更负**）
   - b~1/n²：False——b~logn/n：False——b~1/√n：False——b~sin-log：False——b~rand-decay：False
   - **b~alt（(−1)^k/k）：True（唯一全 N even ground）**

## ⭐ 关键发现
- **"divided-difference + parity"本身不保证 even ground——甚至单调衰减正 b_n（1/n 类）给出 odd ground（μ₋ < μ₊——odd 更负）**
- **CCM 数值观察的 even ground——需要 b_n 的特定符号/振荡结构（如 alt 型交替）或 a_n 的非 unit 结构**
- 真实 b_n = −(1/π)∫₀^L sin(2πny/L)D(y)dy——a_n = 2∫(1−y/L)cos(2πny/L)D(y)dy——D = log*(Ψ♯)——**even ground 是 Weil 分布 D 的具体性质——非 divided-difference 结构自动结果**
- **⚠️ 对 G2.7.3 的意义**：μ₊<μ₋ 的证明**不能**只靠 divided-difference/parity 结构——**需要 Weil 分布 D 的显式（或 b_n 的特定结构定理）**——这是"障碍证据"（结构不足）——精确化：CCM 的 even ground 依赖 D 的深层结构（与数值 10⁻⁵⁵ 精度一致——b_n 有非常特殊的形式）

## 判定
- **结构测试完成**：Z₂ + divided-difference ⟹̸ even ground（数值确认——单调 b_n 族 odd ground）
- **需 Weil 分布 D(y) 显式**（论文 Section 3——QW(f,g) = Ψ(f**g)——Ψ 分布）——才能测试真实 b_n/a_n 是否给 even ground
- **备选**：若真实 b_n 有"交替/振荡"结构（alt 型——测试唯一全 even）——可能给可证 Sector ordering——需 D 确认

## 下一步候选
- (a) 获取论文 Section 3 的 Ψ/D 显式——计算真实 b_n/a_n——测试 even ground（决定性）
- (b) 接受"结构不足"结论（μ₊<μ₋ 需 Weil 分布具体结构——G2.7.3 依赖 D 的显式——非纯结构定理）
- (c) 唐先生指示
