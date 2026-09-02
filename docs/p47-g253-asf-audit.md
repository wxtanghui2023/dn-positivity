# P47-G2.5.2-R2 收档 + G2.5.3 审计——5+4i 决定性反例

> 2026-09-02 12:55 · 唐先生 P47-G2.5.2-R2 指示 · quartic single FAIL · ASF

## ① 5+4i 反例验证（数值确认）
- π = 5+4i——π̄ = 5−4i——N = 41——π, π̄ 都是 primary Gaussian primes——**π/π̄ = (9+40i)/41——不是 unit——π ≁ π̄ ✓**
- **(π/π̄)₄ = 1——(π̄/π)₄ = 1（数值确认唐先生解析：10¹⁰ ≡ 1 mod 41）**
- **T(π,π̄) = 1 但 π ≁ π̄——⭐ R2 FAIL 确认（真实 Galois 模型——ℚ(i) + 复共轭 + 四次互反）——严格 counterexample 收档**

## ② 更深结构——单符号信息量不足
- T(A,A∨) 只有 μ₄ 值（4 状态）——压缩巨量算术信息——fixedness 是极高分辨率——**除非特殊定理保证 q∨^{-1}(1) = Fix(∨)——否则必然"非固定 → q∨(A) = 1"——5+4i 正是这种情况**

## ③ 升级——向量值 T + R2*
- S 有限——仍有限值——pigeonhole 碰撞——**需 Arithmetic Separation Family (ASF)：∀A≠A∨, ∃v: T_v(A,A∨) ≠ 1——不是把 fixedness 写进定义——可证伪的 separation theorem**

## ④ ASF 结构审计
- 无限族（所有高斯素数 π 的四次符号）——(A/π)₄ = 1 ∀π ⟺ A 四次幂（Hecke 类）——"A/Ā 四次幂"（A = Ā·B⁴）
- **⚠️ "四次幂类"≠"精确固定"（B ≠ unit）——R3 墙：ASF 给"四次幂类分离"——不是 fixed-point wall——realization rigidity 仍缺**

## ⭐ 判定
- **5+4i 反例确认（数值）——单 quartic symbol FAIL——R2 在真实 Galois 模型 FAIL——收档**
- **G2.5.3（ASF）第一轮审计**：无限族给"四次幂类分离"（Hecke——算术 wall 精细版）——不是精确固定——有限族 pigeonhole——**"ASF 精确分离（= Fix）"未找到——multi-local separation OPEN——realization rigidity OPEN**

## 状态表（唐先生）
Legendre FAIL——norm pairing on ℚ(i) FAIL(trivial)——quartic single FAIL——**Galois conjugation 仍有结构价值**——**multi-local separation OPEN——realization rigidity OPEN**

## 下一步候选
- (a) ASF 深化（"四次幂类分离"⟹ realization rigidity?——或——"unit 约束"（B 的额外结构——使四次幂类 = unit 类——需新定理））
- (b) 接受审计（单符号 FAIL 收档——multi-local OPEN——P47-G2.5.3 待定）
- (c) 唐先生指示
