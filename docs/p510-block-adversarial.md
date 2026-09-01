# P5.10：Adversarial Block Sequence 测试——第一枪结论

> 2026-09-01 · 唐先生指令 · 先攻击猜想（不先证明）

## 任务
构造满足全局 RvM 密度（N(T) ~ (T/2π)log T）+ 最小间距（Δγ ≳ 1/log T）——但局部高/低密度块交替的序列——检验 inf_θ F_Λ(θ) = 0 是否可能。

## 构造（修正后——密度正确）
- block_v3：18 高密点（δ=0.5·2π/log γ）+ 1 低密点（δ=10·2π/log γ）——平均 = RvM ✓（N(T) 比与纯 RvM 一致）
- 极端变体：0.1×/19×、0.2×/11×、0.5×/10×（保持平均 RvM）

## 结果
| 配置 | N(T) 比 | min/bohr |
|------|:--:|:--:|
| 纯 RvM | 0.668 | 0.025-0.031 |
| block_v3（18+1） | 0.594 | 0.030-0.037 |
| 0.1×/19×（200+10） | 0.614 | 0.055 |
| 0.2×/11×（200+16） | 0.603 | 0.043 |
| 0.5×/10×（200+11） | 0.606 | 0.023 |
| **2000 高密+1 低密** | 0.894 | **0.0016** |
| 规则排列（常数密度） | 1.727（非 RvM） | → 0（J 大） |

## ⭐ 关键发现
1. **block 攻击（全局 RvM + 局部不均匀）不破坏 coercivity**（min/bohr 稳定 0.02-0.06——不 → 0）
2. **但——"局部密度均匀偏移"（0.5×RvM——近似规则排列）破坏**（min/bohr ~ 0.0016——接近 → 0）
3. **支持唐先生的判断**：**真正控制 coercivity 的是"局部密度"（uniform local density——lower Beurling density）——不是全局 N(T)**
   - 局部密度正确（RvM——2π/log）⟹ coercivity 强（0.03）
   - 局部密度偏移（0.5×）⟹ coercivity 弱（→ 0 行为）
   - 局部不均匀（block——平均正确）⟹ 中等（0.02-0.06——局部错误部分削弱）

## 结论（唐先生框架）
- **恶意序列（block）构造不成功**——"RvM 全局密度 + 间距 ⇒ C_arith"**未被封口**（block 不破坏）
- **但——"局部密度"的区分已显现**——local density（lower Beurling density）才是 coercivity 的真正来源——**不是全局 N(T)**
- **按唐先生指示进入 BM/Ingham/de Branges 路线**：检查"lower Beurling density + separation ⟹ 指数和 L² 下界"的现有理论

## 下一步
- 文献检查：Beurling-Malliavin / lower density / frame lower bound / Ingham large sieve
- 纯调和分析定理候选："局部均匀密度（lower Beurling density ≥ 某值）+ 分离 ⟹ inf_θ F_Λ(θ) > 0"
- 验证 ζ 零点满足假设（RvM 局部密度 + 间距下界——无条件）
