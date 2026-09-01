# P5.12-C2：纯调和分析——margin 对数退化（候选定理削弱）

> 2026-09-01 · 唐先生 P5.12-C2 指令 · 最后一次纯数学攻击 · 不解释成 RH 进展

## 核心框架（唐先生）
- **coercivity requires quantitative control of coherent accumulation of the difference spectrum**——inf_θ F(θ) > 0 要求差谱 Fourier modes 不能在某个 θ 协同产生足够大的负贡献
- **positivity ⇏ strict positivity ⇏ uniform coercivity**（F = 1−cos(Nθ) 反例——严格正但 inf=0）
- 论文主轴修改：density → difference-spectrum structure → uniform coercivity → exclusion——中间箭头未知

## 负偏离分析（P5.12-C2 核心）
**min_θ F = b₀ + min_θ Σ_{r≠0} b_r e^{irθ}——coercivity 需要"最大负偏离" < b₀**（正偏离可以任意大——不影响 inf）

| 配置 | 负偏离/b₀（J=200） | inf F/b₀（margin） |
|------|:--:|:--:|
| RvM | 0.956 | 0.044 |
| lattice(1.4 同密度) | 0.956 | 0.044 |
| 随机 | 0.920 | 0.080 |
| lattice(0.5 密) | 0.992 | 0.008 |

## ⭐ 决定性发现：margin 的 J 退化
**lattice(0.5 密)**：margin 0.012（J=100）→ 0.003（J=1200）——**→ 0（差频集中——坏谱确认）**

**RvM**：margin 0.044（J=200）→ 0.027（J=1600）——**margin×log J ~ 0.20-0.23（拟合良好）——对数退化——疑似 → 0（极慢）**

## 结论（候选定理削弱）
- **"RvM 密度 + 分离 ⟹ uniform coercivity"的候选定理被削弱**：数值 margin 对数退化（~0.2/log J——J → ∞ 时 → 0）——**即使 F 数值稳定（0.03-0.05）——margin 在收缩**
- **"差频非集中"是 coercivity 的机制**——但——RvM 的"非集中"只给对数 margin（弱）
- **随机（相位更随机）margin 更大（0.080）**——相位随机性增强 coercivity——但 RvM 的对数退化表明"密度本身"不够

## 诚实状态（唐先生框架）
- **P5.12-C2 纯调和分析**：差频集中（lattice）⟹ margin → 0（坏谱）——差频分散（RvM）⟹ margin 对数退化（弱 coercivity——疑似渐近破坏）
- **"uniform difference-spectrum rigidity"是缺失的层**（local regularity 不够——margin 退化）
- **如果 margin ~ 0.2/log J 严格（→ 0）**——"RvM ⟹ C_arith"不成立（渐近）——Rigidity Gap 定位到"uniform difference-spectrum rigidity"（比 local regularity 强）

## ⚠️ 需要谨慎
1. **数值 margin 是 θ 扫描（300 点——[0,60]——8 个周期）的有限下界**——真 inf（所有 θ）可能更小——**数值 margin 是"上估计"**
2. **对数退化的拟合（J 到 1600）**——需要更大 J + 理论确认（margin ~ c/log J 还是稳定）
3. **ζ 的 V(T) 需要"所有零点"（J = ∞）的 coercivity**——如果 margin → 0——C_arith 失败——**除非——"相位部分抵消"在 J → ∞ 留正余量（未确定）**

## 下一步（唐先生排序）
- P5.12-C3：RvM + separation + energy bound ⟹? coercivity（最终判定）
- **"uniform difference-spectrum rigidity"的形式化**——超越 local regularity 的条件
- 或——**构造满足 R₀-R₂ + 强差谱条件但 inf F → 0 的反例**——Rigidity Gap 精确化为"local regularity insufficient; uniform difference-spectrum rigidity required"
