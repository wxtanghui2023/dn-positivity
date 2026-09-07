# Rédei 实现——Test B 确认 + 2-adic 规范化歧义（诊断点）

> 2026-09-07 · 唐先生 regression suite 执行——Test B ✓——normalization 进行中

## Test B 结果（确认唐先生诊断）
同一 (a,b,c)——不同 norm 解 β₁, β₂：
- 50 个多解样本——44 相同——**6 不同**（如 (3457,2081,3361)：β₁ 给 +1——β₂ 给 −1——）
- ⟹ **raw 符号依赖解的选择——需要 minimal-at-2 normalization** ✓

## Test A 状态
H_+ = H_-（两个 c-prime 同符号——）——之前验证过（38/38——）——通过

## 2-adic normalization 尝试——遇到歧义
实现"tβ 是模 4O 平方"检查（Prop 7.3(1)——对 a ≡ 1 mod 4——Δ(a) 奇——唯一 t ∈ {±1,±2}——）：
- 结果：t=2 与 t=−2 **同时**通过平方检查（系统性——22 例多 t 全 [2,−2]——）
- 期望：唯一 t（Prop 7.3(1)——）

### 可能的解释（待解决——）
1. 我的平方检查（穷举 p,q mod 4——）有缺陷？——−1 在 O/4O 非平方（应该——）——但 2 与 −2 的区分需要 norm 核（ββ' ≡ b ≡ 1 mod 4O——）
2. Stevenhagen 说"unique sign choice of β"——涉及 β 与共轭 β' 的组合（ker N——）——不只是单 β 的平方性——我的实现漏了共轭/范数条件
3. 需要：β 先 twist 成 2-单位（t=2 若 β 非单位——）——再检查平方性——两步

## 下一步
- 精读 Prop 7.3 证明（O/4O 群结构——2 分裂/惯性——norm 核——）实现正确的"唯一 t"
- 或——绕过 2-adic 细节——直接用"两个解给相同规范化符号"的经验规则（如果规范化的效果是乘 t 后再算符号——符号变化 = Legendre(t,c)——可以"补偿"？）
- 或——用路径 B（Frobenius——）交叉验证（但需 D₄ 映射——）

## 文件
- scripts/redei_testB.py——Test B（确认解依赖——）
- scripts/redei_normalize_test.py——normalization 尝试（歧义——）
