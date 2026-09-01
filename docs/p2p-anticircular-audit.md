# P2′：Riemann ζ 谱实现候选的反循环审计

> 2026-09-01 · 唐先生指示 · 系统性反循环审计（先于 Mayer）

## 独立性分层（P2′ 标准）
- **Level 0（直接循环——淘汰）**：定义直接使用 {ρ}——H = H(ρ₁, ρ₂, ...)——或 det(I−H_s) = ξ(s) 但 H 构造依赖零点
- **Level 1（间接循环——危险）**：H = H(explicit formula)——显式公式含 Σx^ρ——零点信息已进入构造
- **Level 2（算术构造——谱约束未知）**：H = H(ℤ, {p}, geometry, dynamics)——不输入零点——然后独立证 H=H†——再证 Spec↔{γ_ρ}——三步严格分开
- **Level 3（真正物理突破）**：先有独立物理系统 P（Hilbert space/Hamiltonian/unitary evolution/BC/scattering）——得谱函数 Z_P(s)——最后才发现 Z_P = ξ（或其零集严格对应）——physics→spectrum→zeros

## 六候选家族审计

### ① Hilbert–Pólya / self-adjoint operator
- **输入依赖**：无独立构造（D3 已审计——de Branges 循环——graph 谱不匹配）
- **谱约束来源**：自伴性无独立来源（是"期望"不是"证明"）
- **最后一步**：Spec(H) = {γ_ρ} 从未建立（无 H）
- **判定：Level 0/1——淘汰**

### ② Berry–Keating（H ~ xp）
- **输入依赖**：H ~ xp 本身不输入零点——**但**——量子化/边界条件/正则化——**边界条件是否为匹配零点而反向选择？**——是（原始 BK 谱是近似的——精确化需要调边界）
- **谱约束来源**：xp 自伴（合适 BC）——但 BC 反向选择——✗
- **最后一步**：Spec ≈ γ_ρ（近似）——非 C 级
- **判定：Level 1——边界条件反向选择——淘汰**

### ③ Connes / adelic / noncommutative geometry
- **输入依赖**：adelic 构造算术独立（不直接输入零点）——**但**——谱解释发生在 trace formula 层——**trace formula 复制显式公式**（含 Σx^ρ）——Level 1
- **关键区分**：trace formula reproduces explicit formula（真——但自适应）≠ independent self-adjoint spectrum forces RH（未证明）
- **谱约束来源**：site spectral——自伴性未独立证明（依赖零点对应——循环）
- **判定：Level 1——trace formula 复制显式公式——淘汰（除非自伴独立）**

### ④ Bost–Connes
- **输入依赖**：算术系统（ℤ 乘性——adelic）——**独立**（不输入零点）——Level 2 候选 ✓
- **谱约束来源**：KMS 状态——时间演化 automorphism——**有独立结构**——但——KMS 给"平衡态存在/唯一"——不是"谱实"
- **最后一步**：spectral data ↔ 零点——**未建立**（partition function = ζ(s)——但不是谱行列式——零点不是谱）
- **判定：Level 2 候选——独立构造 ✓——但——谱-零点对应缺失——且可能根本没有对应**

### ⑤ Mayer / transfer operator ⭐（最有希望）
- **输入依赖**：动力系统 → L_s → det(1−L_s) → zeta——**Selberg 情形成功**（模群双曲曲面测地线流——Ruelle 算子——独立于零点）——Level 2 候选 ✓
- **但——对 Riemann ζ 必须重新检查**：
  - 有没有不以零点为输入的动力系统？——**待查**（Mayer 对 ζ 的尝试可能是"形式"的——为匹配 ζ 定制——Level 1 风险）
  - L_s 有没有足够强的谱对称/自伴结构？——**待查**（Selberg 情形有——与 Laplace 谱联系——Riemann 情形未知）
- **最后一步**：对 Selberg——det(1−L_s) = Z(s)——零点 = 1∈Spec(L_s)——谱实（Laplace 自伴）⟹ Re(s)=½——**C 级成功**——对 Riemann——待查
- **判定：Level 2 候选（唯一）——需要独立性 + 谱性质检查**

### ⑥ Scattering / S-matrix
- **输入依赖**：任何"由 ζ 定义"的 S——Level 0/1（循环）——需要**独立散射系统**——未知
- **谱约束来源**：unitarity——若系统独立存在——有独立约束——但系统不存在
- **最后一步**：极点 ↔ ρ——未建立（无系统）
- **判定：Level 0/1（现有候选）——独立散射系统未知——淘汰（待找）**

## 三张表

### 表 A：输入依赖
| 候选 | 输入零点 | 输入显式公式 | 输入 RH | 独立 |
|------|:--:|:--:|:--:|:--:|
| Hilbert–Pólya | 是 | 是 | 隐含 | ✗ L0/1 |
| Berry–Keating | 否(H~xp) | 否 | 边界反向 | ✗ L1 |
| Connes | 否(adelic) | 是(trace formula) | 隐含 | ✗ L1 |
| Bost–Connes | 否 | 否 | 否 | ✓ L2（谱-零点缺失） |
| Mayer | 否(动力系统) | 否(det(1−L_s)) | 待查 | ? L2 候选 |
| scattering | 是(ζ定义S) | 是 | 隐含 | ✗ L0/1 |

### 表 B：谱约束来源
| 候选 | 自伴/单位性来源 | 独立？ |
|------|----------------|:--:|
| Hilbert–Pólya | 无（期望） | ✗ |
| Berry–Keating | 边界条件（反向选择） | ✗ |
| Connes | 未独立证明 | ✗ |
| Bost–Connes | KMS/时间演化（独立）——但不给谱实 | 部分 |
| Mayer | L_s 谱性质（Selberg 有——Riemann 待查） | ? |
| scattering | unitarity（若系统独立） | ? |

### 表 C：最后一步（Spec ↔ ρ）
| 候选 | 级别 | 资格 |
|------|:--:|:--:|
| Hilbert–Pólya | 从未建立（无 H） | ✗ |
| Berry–Keating | 近似（非 C） | ✗ |
| Connes | trace formula 复制（非独立） | ✗ |
| Bost–Connes | 未建立（无谱对应） | ✗ |
| Mayer | Selberg 是 C——Riemann 待查 | ? |
| scattering | 未建立（无系统） | ✗ |

## P2′ 判定

**核心发现**：六个候选中——**五个落入 Level 0/1**（HP/BK/Connes/scattering 明确——Bost-Connes 独立但缺谱-零点对应）——**Mayer 是唯一 Level 2 候选**（动力系统独立——Selberg 模板成功）。

**这印证了唐先生的判断**：
> 现有谱实现路线**普遍把 RH 信息预先编码进对象**（Level 0/1）——只有 Mayer 可能是例外（待查）。

**P2′ 结果**：
- 大多数候选：P2′ FAIL（缺 (I)/(II)/(III) 中至少一条）
- Mayer：**通过独立性门槛待查**——需要检查 (I) L_s 不以零点为输入 (II) L_s 谱对称/自伴 (III) det(1−L_s) = ξ 的谱-零点对应非 RH 重述

## 战略变化（唐先生）
- 之前：从已有 ζ 结构推出 RH
- 现在：**先构造一个不认识 RH 的对象——再问它为什么认识 ζ**（逻辑箭头相反）
- 若 P2′ 证明所有主要候选落入 Level 0/1——强结果：谱实现路线也普遍预编码 RH——届时去 Mayer 可精确针对缺失环节设计
