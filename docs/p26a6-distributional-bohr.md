# P26-A6：Level III——Distributional Bohr Spectrum（候选定理）

> 2026-09-01 · 唐先生 Level III 指令 · distributional Bohr spectrum——把 log p 纳入

## 唐先生 P26-A5 封存 + Level III 框架（采纳）
- **P26-A5 正式封存**：Theorem (Mean Reflection Rigidity)——Σ|b_p|²/p < ∞ + 临界线 B² 反射 ⟹ b_p = 0——RH-independent 纯 harmonic-analysis——**不能升级成 T_ζA_arith = {0}**（合法 deformation ⟶ B² boundary class 的左边箭头未证明）
- **修正措辞**：log p 不在"任何 ℓ²(p^{−α}) 类外"——α>1 时 Σ(log p)²/p^α < ∞——真正的边界是 α=1：log p ∉ ℓ²(p^{−1})
- 三层结构：Level I（ℓ¹(p^{−1/2})——✓）/ Level II（ℓ²(p^{−1}) + B²——✓）/ Level III（临界/更弱——含 log p——未解决）——**Level III 障碍：log p 型方向没有临界 B² 能量**
- **下一步：直接攻 Level III**——加权 Besicovitch / distributional Bohr spectrum——把 log p 纳入——保留"正负频率不能相等"的反射刚性

## P26-A6：Distributional Reflection Rigidity（候选定理）

### ⭐ 定理（Level III 候选）
**设 M_b(s) = Σ b_p/(p^s−1)（σ>1）——b_p 亚多项式（|b_p| = O(p^ε)）——假设临界线分布反射（弱*：w*-lim_{σ→½+} M_b(σ+it) = w*-lim_{σ→½+} M_b(σ−it)）——则 b_p = 0（所有 p）**

**证明**：
1. 弱*极限：⟨M_b(½+·), φ⟩ = Σ b_p p^{−k/2} φ̂(k log p)（φ̂ 快速衰减——压制亚多项式——收敛）
2. 分布反射：⟨M_b(½+·), φ⟩ = ⟨M_b(½+·), φ(−·)⟩——即 Σ b_p p^{−k/2} φ̂(k log p) = Σ b_p p^{−k/2} φ̂(−k log p)
3. 取 φ̂ 支撑在正频率 λ₀ = k₀ log p₀（{k log p} 离散——每区间有限——k ≤ x/log 2——可避开其他 ±k log p）
4. 左侧 = b_{p₀}p₀^{−k₀/2}φ̂(λ₀)——右侧 = 0（−k log p 负——不在正支撑）
5. 等式 ⟹ b_{p₀} = 0——所有 p——∎

**关键性质**：
- **覆盖 log p**（亚多项式——分布 well-defined——log p 不反射（数值差 5.98）——不被排除也不被允许——但"反射 ⟹ b=0"统一成立）
- **比 A5（B²——ℓ²）强**——不需要 B² 能量（log p 无临界 B² 能量——但分布意义正负分离仍成立）
- **原反射（延拓——逐点）⟹ 分布反射**——分布反射刚性（更弱假设 ⟹ b=0——更强）

### 数值
- ③ 分布反射（b≠0）：⟨M,φ⟩ = ⟨M,φ(−·)⟩ = 0.928——**⚠️ 小缺陷：φ = e^{−t²/2}cos(λ₀t) 是偶函数——φ(−t) = φ(t)——测不出反射——需奇/复测试函数**（理论论证不受影响——测试函数类需细化）
- ④ log p 分布频谱：−log 2 系数 = 0.3017 vs 理论 0.4573（σ=1.2——截断误差——方向正确）

## ⭐ P26-A6 判定
- **Distributional Reflection Rigidity 候选成形**（分布反射（弱*）⟹ b=0——任何亚多项式 b——包括 log p——正负分离（分布）——比 A5 强——不需要 B² 能量）
- **未决**：
  - (a) 分布反射的严格化（弱*框架——测试函数类——单频率支撑 φ̂ 存在性——{k log p} 离散的严格论证）
  - (b) 合法变形 ⟹ 亚多项式 b（变形的系数约束——FE/延拓对 b 的约束——未证明）
  - (c) 分布反射与原反射的精确关系（原反射 ⟹ 分布反射——反向不）
  - (d) 数值测试函数的奇/复选择（φ 偶函数测不出反射——需细化）

## 下一步
- (a) 严格化 Distributional Reflection Rigidity（弱*框架——测试函数——离散频率——正式定理）
- (b) 检查"合法变形 ⟹ 亚多项式 b"
- (c) 接受 Level III 候选（分布反射刚性——log p 纳入——正负分离保留——严格化未完成）
- (d) 唐先生指示
