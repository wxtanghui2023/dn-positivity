# P5.12：Additive-Energy R₃——实证对应 + Anti-circularity 检查

> 2026-09-01 · 唐先生 P5.12 指令 · R₃ = difference-set nonresonance / additive-energy control

## R₃ 定义（唐先生升级——替换 phase regularity）
**E_Λ(H) = #{ (j,k,ℓ,m) : |γ_j−γ_k−γ_ℓ+γ_m| ≤ H^{-1} }**——差集共振（四元组计数）
- 控制负贡献的不是 {γ_j} 本身——而是**差集 ΔΛ = {γ_j−γ_k}**
- **真正的 rigidity variable 候选："零点差集的不共振性"**（不是"位置的不规则性"）

## P5.12-B：三个模型 + 真实 ζ 零点（J=200）
| 配置 | E_Λ(200) | F/bohr | 归一化间距 std |
|------|:--:|:--:|:--:|
| 规则排列（lattice） | **5.33e6** | **0.0097（坏谱）** | 0.032 |
| RvM 模型 | 1.01e5 | 0.0548 | 0.000 |
| 随机扰动 | 1.10e5 | 0.1037（最强） | 0.167 |
| **真实 ζ 零点** | **9.67e4** | — | **0.541（GUE 类）** |

## ⭐ 关键发现
1. **E_Λ 与 F_Λ 反相关**（E 大 ⟹ F 小）：
   - lattice（E=5.3e6）⟹ F=0.0097（坏谱）
   - 随机（E=1.1e5）⟹ F=0.104（coercivity 强）
   - **R₃（additive-energy）与 coercivity 有明确实证对应——不是人为定义**
2. **真实 ζ 零点 additive energy 低**（9.7e4——与 RvM/随机同量级——规则排列的 1/55）——**ζ 零点差集低共振（实证——2M 数据）**
3. **E_Λ(H) 的尺度依赖**：lattice 恒定（完全退化）——RvM/随机随 H 增大下降（低共振）

## Anti-circularity 检查（唐先生警告）
**⚠️ ζ 零点的 additive energy 上界——无条件性未知**：
- **pair correlation（二阶）**：Montgomery——RH 级/部分无条件——真实 ζ 归一化间距 std=0.541（GUE 类——非平凡统计）
- **additive energy（四阶）**：更精细——**很可能 RH 级**
- **如果 R₃ 需要"ζ 零点 additive energy 无条件上界"——而这个上界等价于对关联/GUE——R₃ 只是 RH 换名字——循环**

## 结论（唐先生的两种结果）
**如果 R₃ 能由无条件事实推出**：unconditional theorem ⟹ R₃ ⟹ C_arith ⟹ RH——**真正突破**
**如果 R₃ 需要 RH 级信息**：**Rigidity Gap 精确定位到 additive-energy/difference-set 层**——**比"phase cancellation"强得多的负结果**

## 下一步（唐先生排序）
- P5.12-C：寻找纯调和分析定理（**difference-set nonresonance ⟹ inf_θ F_Λ(θ) > 0**——完全脱离 ζ）
- P5.12-D：最后才接 ζ（Riemann zeros 是否无条件满足 R₃）
- ⚠️ 每一步做 anti-circularity 审计（R₃ follows from unconditional facts? / R₃ ⟹? RH）
