# P5.10 文献检查：Beurling/Ingham/Frame 理论——"密度 ⟹ coercivity"的理论支撑

> 2026-09-01 · 唐先生指示 · 恶意序列构造不出来——进入 BM/Ingham/de Branges 路线

## 文献核心结果

### 1. Beurling 经典定理（采样集）
**Λ ⊆ ℝ 分离 + lower Beurling density D⁻(Λ) > 1 ⟹ Λ 是 PW 空间的采样集**：
$$D^-(\Lambda) = \liminf_{R\to\infty} \inf_x \frac{\#(\Lambda \cap [x-R,x+R])}{2R}$$
**最坏位置最坏窗口**——⟹ Σ|F(λ_n)|² ≥ A||F||²（**正是我们需要的下界结构**）

### 2. Ortega-Cerdà（2000）——Fourier frame 完全刻画
频率序列 {λ_n} 生成 L²(−γ,γ) 的 Fourier frame ⟺ 分离 + Beurling density 条件——**密度是精确阈值**

### 3. Duffin-Schaeffer / Avdonin / Lindner（ADS 下界）
分离序列 + 有界偏移 ⟹ 指数系 frame——**显式 lower frame bound**（ADS——指数小的常数但 > 0）

### 4. Beurling-Malliavin 理论
**lower BM density 与 gap characteristics 的对应**——BM density 描述指数系统的 completeness radius——**比普通密度更精细**

## ⭐ 关键洞察：我们的情况是"超采样"（D⁻ = ∞）

**RvM 密度（log T 增长）⟹ lower Beurling density D⁻ = ∞**（每窗口点数随位置增长）：
- **"超采样"（远超临界密度）**——超采样通常给出**更强的稳定性**（更不容易相消）
- **与数值一致**：RvM 配置 coercivity 强（min/bohr ~ 0.03 稳定）——稀疏规则排列（常数密度——非 RvM）coercivity 弱（→ 0）

## 适配问题（为什么不是现成定理）
1. **标准理论（有限密度）不直接覆盖 RvM（D⁻ = ∞）**——需要适配（加权/半无限/增长密度）
2. **Paley-Wiener 对偶**：Beurling 是"采样"（Σ|F(λ_n)|²）——我们是"指数级数"（S(u) = Σ(1/ρ_j)e^{iγ_j u}——对偶）——需要转换
3. **固定系数 1/ρ_j**（不是任意系数）——**比 frame 下界（任意系数）更弱——更容易**——但——文献不直接覆盖

## 纯调和分析定理候选（P5.10 目标）
**"RvM 型密度（超采样——D⁻ = ∞）+ 分离 + 固定系数 1/γ_j ⟹ inf_θ F_Λ(θ) ≥ c·bohr"**——**新定理**（文献不直接覆盖——但——机制有经典支撑——Beurling 超采样稳定性 + Ortega-Cerdà 刻画）

## 验证路径（唐先生的逻辑顺序）
```
纯调和分析定理（RvM 密度 + 分离 + 固定系数 ⟹ F ≥ c·bohr）
→ 验证 ζ 零点满足假设（RvM 局部密度 + 间距下界——无条件——RvM/已知间距）
→ C_arith（liminf V(T)/T^{2β_max−2} > 0）
→ V(T) ≥ c(δ)·T^{2δ}——C2 ⟹ RH
```

## 诚实状态
- **数值证据**：RvM 型配置 coercivity 稳定（min/bohr ~ 0.03——J 到 4000）——block 攻击失败
- **理论机制**：有经典支撑（Beurling 超采样稳定性）——但——**"超采样 + 固定系数 ⟹ 级数下界"是新定理**——需要严格证明
- **文献不直接覆盖**：RvM 的 D⁻ = ∞（增长密度）——标准 frame 理论（有限密度）不适用——**这是新的工作**

## 下一步
- (a) 尝试证明纯调和分析定理（RvM 密度 + 分离 + 固定系数 ⟹ F ≥ c·bohr）
- (b) 检查"增长密度/加权 frame"的文献（可能部分已知）
- (c) 唐先生指示
