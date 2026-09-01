# P34-D2″：三无量纲测试——(I) normalized Gram 中等相关——(II)(III) 截断

> 2026-09-02 · 唐先生 D2″ 指令 · 无量纲测试 · feature divergence 耦合

## (I) normalized Gram——max_{K<k,l≤2K, k≠l}|R_X(k,l)|
| X | K=5 | K=10 | K=20 | K=40 |
|---|---|---|---|---|
| 2000 | 0.207 | 0.207 | 0.533 | 0.533 |
| 50000 | 0.171 | 0.171 | 0.460 | 0.460 |
| 10⁶ | 0.158 | 0.158 | 0.424 | 0.424 |

- **⭐⭐ max|R| 中等（K=20: 0.42-0.53）——非近对角（<0.3——系数符号主导）——非高度相关（>0.7——feature 几何主导）——"两者均显著"（混合机制——真 operator-level cancellation）**
- **K 增大时相关度升**（K=5: ~0.2 → K=20: ~0.5——高 k 模态更相关——cancellation 的 feature 几何成分随 k 增大——⚠️ 对 R1-O 不利（高 k 的 φ_k 非正交——cancellation 更依赖系数符号））
- **X 增大时略降**（X=2000: 0.533 → X=10⁶: 0.424——K=20）

## (II) renormalized operator tail——T_K(X)/log log X——截断（未显示）
## (III) double-limit——L1(K) vs L2(X)——截断（未显示）

## ⭐ 初步判定
- **cancellation 机制：混合（系数符号 + feature 几何都显著——"真 operator-level cancellation"——唐先生三机制表的第三种）**
- **高 k 相关度升（K=5→20）——高 k 模态非正交——"cancellation 更依赖系数符号振荡"——R1-O 的难度在高 k**
- **feature norm 发散（||φ_k||² ~ ½log log X → ∞）——"feature-map divergence remains"（唐先生状态——✓）**

## ⚠️ 诚实边界
- (II)(III) 截断（输出进程结束）——需补
- Kmax=100——X≤10⁶——尾部 k>100 未计
- "R1-O 倾向"不能宣称（唐先生修正——feature divergence 耦合）

## ⭐ 状态（唐先生）
**P34-D2'：OPEN——partial cancellation, but feature-map divergence remains**
- absolute tail control: ❌
- operator-level cancellation: ✓ 部分确认
- T_K(X) 数值下降: ✓
- T_K → 0 uniformly in X: ❌ 未证明
- feature-map boundedness: ❌（||φ_k||² ≍ log log X → ∞）
- canonical infinite-dimensional operator: ❌ 未建立
- R1 (K^ren → 0): ❌ 不能宣称
- R2 (nonzero infinite-rank): ❌ 尚未排除
- R3 (high-mode obstruction): OPEN

## 下一步
- (a) 补 (II)(III)（renormalized tail——double-limit——L1 vs L2 稳定性）
- (b) 唐先生指示
