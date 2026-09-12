# P28-P33 正式封档：Moving-Edge Obstruction——算子论层级与 Problem I/II 拆分

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

> 2026-09-01 · 唐先生最终封档指令 · P28-P33 系列归档

## 一、层级表（已建立 / 尚未建立）

| 层级 | 已建立 | 尚未建立 |
|---|---|---|
| 有限截断 | n₋(K_N)=N | — |
| 块结构 | 对角块 ⪰ 0，负性来自 inter-block coherence | — |
| 临界机制 | λ_edge→0⁻、Γ→2⁺、r→1 | 渐近速率 |
| 深部谱 | O(1) 个 persistent directions | 更大 N 的严格谱估计 |
| 边缘谱 | N−O(1) 个 moving near-zero directions | 实际极限算子的严格描述 |
| 无限负指标 | 一致 nested embedding 下 n₋(K_N)=N ⟹ n₋(K)=∞ | 对实际 K_off 的证明 |
| uniform negative sector | 不能由 n₋(K_N)=N 推出 | 实际 K_off 是否存在 |
| uniform transfer | 未建立 | 需要新的 transfer theorem |

## 二、核心逻辑式

**n₋(K_N) = N ⇏ ∃ε>0: dim E_K((−∞,−ε)) = ∞**

**但在固定且一致 nested operator 框架中：n₋(K_N)→∞ ⟹ n₋(K)=∞**
（只要 K_N 是同一 K 的有限截面，且负子空间通过嵌入保持一致）

## 三、标准 2×2 模型——钉死区别

**K_j = [[1, −(1+1/j)],[−(1+1/j), 1]]——λ_j⁻ = −1/j → 0⁻**：
- n₋(K) = ∞
- 同时 inf_{||x||=1} −⟨Kx,x⟩ = 0

**⟹ Infinite negative index and uniform negative margin are logically independent.**

## 四、P28-P33 真正机制链

```
extensive finite inertia
⇓
inter-block generated negativity
⇓
Γ_j → 2⁺, r_j → 1
⇓
λ_j⁻ → 0⁻
⇓
extensive moving spectral edge
```
**而不是**：extensive inertia ⟹ extensive uniformly negative sector。
P31-P32 的 finite persistent core + extensive near-zero moving edge 解释了为什么后一箭头缺失。

## 五、Moving-Edge Obstruction（theorem-level statement）

**Moving-Edge Obstruction.**
Extensive growth of finite-section negative inertia does not, by itself, imply the existence of an infinite-dimensional uniformly negative sector. In a consistent nested realization, n₋(K_N)→∞ may indeed imply n₋(K)=∞, while all additional negative directions accumulate at the spectral edge 0, so that inf σ₋(K)=0 and no uniform negative-form margin exists.

**"finite-section data alone are insufficient"限定为 embedding/limit 未固定时的 statement——不再声称同一个 nested operator 可以产生有限和无限两种极限负指标。**

## 六、Problem I / II 拆分（P27 缺口的精确定位）

- **Problem I: n₋(K_off) = ∞ ?**——P28-P32 没有完成否定——且一致 nested framework 下甚至可能直接成立
- **Problem II: ∃ε>0, dim E_{(−∞,−ε)}(K_off) = ∞ ?**——P28-P32 给出很强的 moving-edge 反证型证据——但尚不是实际 K_off 的定理

P33 真正完成的不是"证明 n₋(K_off) 有限"——而是把 P27 的缺口精确拆成两个不同数学问题。

## 七、封档声明（唐先生最终确认版——2026-09-01 23:25）

### 最终数学主线（固定）
- **n₋(K_N)=N ⇏ ∃ε>0: dim E_K((−∞,−ε))=∞**
- **一致 nested realization：n₋(K_N)→∞ ⟹ n₋(K)=∞**
- **但完全可能同时：n₋(K)=∞——inf_{x∈H₋,||x||=1} −⟨Kx,x⟩=0**（moving-edge 模型展示的现象）

### 最终压缩链
```
n₋(K_N)=N
⇓
blockwise positivity + inter-block negativity
⇓
Γ_j→2⁺, r_j→1
⇓
λ_j⁻→0⁻
⇓
finite persistent core + extensive moving edge
⇓
no automatic uniform negative-form transfer
```
最后一步是 **obstruction**，不是对 n₋(K_off)=∞ 的否定。

### 正式术语（废弃"n₋(K_off)=∞ 无望"）
- **finite-section negative-index transfer is unproved**
- **uniform negative-form transfer is obstructed by the moving edge**

### Problem I / II（严格区分）
- **Problem I — Negative-index infinitude：n₋(K_off)=∞ ?**——P28-P33 没有完成否定
- **Problem II — Uniform negative sector：∃ε>0, dim E_{(−∞,−ε)}(K_off)=∞ ?**——P28-P33 提供强烈的 moving-edge obstruction evidence

### 下一阶段（P34 起点）
**Does the actual arithmetic operator K_off possess an infinite-dimensional uniformly negative sector?**
- 需要：K_off 的显式二次型、算术核结构、可构造的负测试向量族
- 脱离单纯有限截断谱学——进入实际算术结构

## 文件索引
- p28a-inertia-transfer.md —— P28-A（有限→无限惯性传递）
- p28b2-fixed-quadratic.md / p28b2c-schur.md —— P28-B2/C（Schur 审计）
- p28c1-schur-mpmath.md / p28c2a-direct.md / p28c2a-rerun-passage.md —— P28-C（direct compression——passage 确认）
- p28d-wm-dichotomy.md / p28d1-asymptotic.md / p28d2-n11n12.md —— P28-D（W_M 二分）
- p28e-interblock-coherence.md / p28e-eta-cross-coherence.md / p28e4-critical-coherence.md —— P28-E（inter-block coherence——η）
- p28uc-transfer-lemma.md —— P28-UC（必要条件审计）
- p29-qlevel-schur.md —— P29（q-Level Schur——Γ=2 确认）
- p30a-gamma-spectrum.md / p30b-near-critical-lemma.md / p30c-alignment-decomposition.md / p30d-joint-scaling.md —— P30（Γ_j 谱——near-critical lemma——η/c/r/Δ）
- p31-deep-sector-margin.md —— P31（deep sector 有限——情形 I）
- p32-deep-persistence.md —— P32（finite persistent core——σ_max≈1）
- p33-moving-edge-obstruction.md / p33b-moving-edge-strict.md / p33c-moving-edge-obstruction.md —— P33（Moving-Edge Obstruction 严格版）
