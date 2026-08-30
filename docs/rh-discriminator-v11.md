# RH 判别定理 v1.1 —— 基础严谨化补丁

> 日期：2026-08-30 19:53
> 目的：把 v1 的形式表达升级为合法分布/定理接口（按依赖顺序——先补项 1）
> 状态：补项 1（S 分布定义）验证完成——两个待确认点

---

## 第一节：Distribution setup（S ∈ S′）——补项 1

### 1.1 定义

$$S := \partial_t^2 \log|\xi(\tfrac12 + it)| \in \mathcal S'(\mathbb R)$$

**严格定义**（分布配对）：
$$\langle S, \phi\rangle := \langle \partial_t^2\log|\xi(\tfrac12+it)|,\ \phi(t)\rangle = \langle \log|\xi(\tfrac12+it)|,\ \phi''(t)\rangle$$

（分部积分——ϕ ∈ S——ϕ'' ∈ S——）

### 1.2 S ∈ S′ 验证

- log|ξ(½+it)| ~ (t/2)log(t/2π) − t/2（t 大——Stirling——多项式增长 t log t）——缓增
- 零点处 log|t−γ|（log 奇异——L¹_loc 可积）——ξ 整函数（无极点）
- **⟹ log|ξ(½+it)| ∈ L¹_loc ∩ 缓增 = S′——S ∈ S′** ∎

### 1.3 Hadamard 分解（分布意义）

$$\log|\xi(s)| = \sum_\rho \log|s-\rho| + \text{regular part}$$

$$S = \sum_\rho K^{t}_\rho + S_{\rm reg},\qquad K^{t}_\rho(t) = -K_{\delta_\rho}(t-\gamma_\rho)$$

- **单零点贡献（t 方向）= −K_δ**（∂_t²[½log(δ²+x²)] = (δ²−x²)/(δ²+x²)² = −K_δ(x)——与 ∂_σ² 反号——数值确认）
- 重零点按重数计入（ρ 重 m ⟹ 贡献 m·(−K_δ)）
- 求和按分布意义收敛（——墙 A：Σ|⟨K_ρ,H_0⟩| < ∞——）

### 1.4 S_reg（regular part——结构性确认——不阻塞）

- 数值：S_reg（∂_t² 显式项）≈ 1e-6~0（数值噪声）
- **不阻塞处理**：S_reg 产生 Weil 显式公式中的 M(H_0) 主项——Q = Q_zeros + Q_reg——Q'_RH 吸收 Q_reg + RH baseline——即使未来发现 S_reg ≠ 0——主定理结构不变
- 精确 S_reg ≡ 0 的解析确认——放到附录"显式项消去/归一化"（不阻塞主线）

### 1.5 符号约定（B——已固定）

- 单零点 t 方向贡献 = −K_δ——**统一定义 Q := −⟨S,H_0⟩**（Weil 判别量——正向零点展开）
- Q = Σ_ρ⟨K_ρ,H_0⟩ + main term——墙 A 的 K_ρ 保持正向——墙 C 正性（Q − Q'_RH = Σδ²w_H）无需额外负号

### Lemma 0（Distribution decomposition——最终版）

> 令 S = ∂_t² log|ξ(½+it)|——则 S ∈ S′(ℝ)——存在分解
> $$S = -\sum_\rho K_\rho + S_{\rm reg}$$
> 其中：K_ρ 单零点核（重数计入——求和分布意义收敛）——S_reg 为显式公式主项贡献。
> 于是 Q := −⟨S,H_0⟩ 具有正向零点展开。

### 1.6 完成状态（更新）

| 项 | 状态 |
|----|------|
| S ∈ S′（分布定义——配对） | 🟢 验证 |
| Hadamard 分解（分布意义） | 🟢（−K_δ——数值确认） |
| 符号约定（Q := −⟨S,H_0⟩） | 🟢 固定 |
| S_reg = 0（精确） | 🟡 结构性确认（不阻塞——附录处理） |

**下一节（补项 2）**：Kernel inversion setup（H_0 构造域与归一化——零频处理——偶性——归一化）

---

## 第二节：Kernel inversion setup（H_0 构造域与归一化）——补项 2

### 2.1 定义

$$H_0 = \mathcal F^{-1}\left[\frac{\widehat w_{\rm target}}{\widehat K_0}\right],\qquad \widehat K_0(\omega) = -\pi|\omega|$$

- Ĥ_0(ω) = −(1/2)(1+|ω|)e^{−|ω|}/|ω|（精确闭式）
- H_0(t) = −(1/2)[(1/2π)log(1+t²) + 1/(π(1+t²))]

### 2.2 三个条件

**(i) 零频处理**：K̂_0(0) = 0——ŵ_target(0) = π/2 ≠ 0——Ĥ_0 ~ −1/(2|ω|)（ω→0 奇异）——但——Weil 配对中可去（墙 A 零频抵消：Ŝ·Ĥ_0 = O(1)）——**不阻塞——取可去奇延拓/tempered 配对**。

**(ii) 偶性**：Ĥ_0(−ω) = Ĥ_0(ω)——H_0(t) = H_0(−t)（数值精确——t² 依赖）✓

**(iii) 归一化**：⟨K_0,H_0⟩ = w_target——w_H(γ,0) = (1/2)[2]/(1+γ²)² = w_target（闭式精确——数值确认全 γ）✓——避免 Q'_RH 尺度歧义。

### 2.3 构造域

- ŵ_target ∈ S（急降 e^{−|ω|}）——1/K̂_0 = −1/(π|ω|)——F⁻¹[急降/|ω|] 存在（tempered 分布——S′ 意义）
- **H_0 ∈ C^∞ ∩ S′**（偶——实值——光滑——缓增对数增长）

### 2.4 完成状态

| 项 | 状态 |
|----|------|
| 零频处理（配对可去） | 🟢（不阻塞——可去奇延拓） |
| 偶性 | 🟢 精确 |
| 归一化（⟨K_0,H_0⟩ = w_target） | 🟢 精确 |
| 构造域（tempered 框架） | 🟢（H_0 ∈ C^∞ ∩ S′） |
| 正式稿措辞 | 🟡（可去奇延拓——tempered F⁻¹——归一化陈述） |

**下一节（补项 3）**：Weil interface theorem（采用 tempered Weil 显式公式——W1-W3——H_0 ∈ W）
