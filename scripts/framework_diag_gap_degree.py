#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 框架诊断: gap ↔ tuple 数 ↔ 多项式度的关系
# 已知数据点 (GPY/Maynard/Polymath/Stadlmann):
#   Maynard 600 (度 1 类 - 基础), Polymath 246 (度 27 - 50-tuple), Stadlmann 240 (度 21 - 49-tuple)
# 问题: 度增加 → gap 降多少? 有没有收益递减墙? 48/47-tuple 需要什么?
import numpy as np

print("=== 框架诊断: gap ↔ tuple ↔ 度 ===")
print()
print("已知数据点:")
print("  方法               度上限     tuple数     gap")
print("  Polymath 8b         27        50         246")
print("  Stadlmann           21        49         240")
print("  (Stadlmann 若度27   27        ?          ?)")
print()

# 最短可容许 k-tuple 的长度 (已知值):
# k-tuple 的可容许性: 最短可容许 k-tuple 长度 (记录)
# 已知 (Polymath wiki):
#   k=50: 246, k=49: 240, k=48: 234?, k=47: ?, ...
# 用已知的 H(k) 记录 (最短可容许 k-tuple 直径):
# 从 Polymath/文献: H(1)=0, H(2)=2 (孪生), H(3)=6?, ...
# 实际记录 (prime constellation / admissible tuples):
#   H(2)=2, H(3)=6, H(4)=8, H(5)=12, H(6)=16, H(7)=20, H(8)=26, ...
#   H(50)=246, H(49)=240 (Stadlmann 说), H(48)=?
# 近似: H(k) ~ k log k (素数定理启发)
print("最短可容许 k-tuple 长度 H(k) 的已知/估计:")
ks = [49, 48, 47, 46, 45, 40, 35, 30]
# Stadlmann 说 H(50)=246, H(49)=240 (最小可能改进 = 49-tuple)
# 估计 H(k) ~ k·log k + 修正 (用 H(49)=240, H(50)=246 校准)
# 粗略: 从 49→48, gap 可能降 ~6-10
for k in ks:
    # 近似 H(k) ~ k*log(k) (素数定理) 但可容许性更复杂
    # 用 H(49)=240 校准: 240/(49*log(49)) = 240/(49*3.89) = 1.26
    est = 1.26 * k * np.log(k)
    print(f"  H({k}) ≈ {est:.0f} (估计 - 实际需查记录)")
print()
print("关键: 每降一个 tuple 数 (50→49→48...), gap 降 ~6-8")
print("  246 (50) → 240 (49): 降 6")
print("  240 (49) → ? (48): 可能降 ~6-8 → ~232-234")
print()

print("=== 度的作用 (GPY 优化的精度) ===")
print("度 d 的基 (对称多项式 2a+b≤d) 越大 → 特征值优化越接近最优")
print("  度 27 (Polymath): 达到 50-tuple 的 246")
print("  度 21 (Stadlmann): 达到 49-tuple 的 240 (支撑更大!)")
print("  → 若度 27 + Stadlmann 支撑: 可能达到 48-tuple (~232-234?)")
print("  → 若度 33+ + 更大支撑: 47-tuple? 46-tuple?")
print()

print("=== 框架诊断: 墙在哪? ===")
print("1. tuple 数的墙: 每步降 ~6-8 - 线性收益 - 无墙 (但需要度/支撑)")
print("2. 度的墙: 计算量指数增长 (49变量积分 - 度21要几天) - 资源墙")
print("3. 奇偶性墙: 只影响精确孪生 (H(2)=2) - 不在 240 到 ~100 的路上")
print("4. EH/GEH 墙: θ=1 才能到 12/6 - 那才是大墙")
print()
print("结论: 240 → ~200 是'方法/资源'路 (可走 - 无原则墙)")
print("      ~200 → 12 需要 θ 大幅提高 (EH 类 - 难)")
print("      12 → 6 需要 GEH - 6 → 2 奇偶性墙")
print("框架诊断: 最值得攻 = 度27+支撑扩大 (240 → ~230) - 但计算资源是瓶颈")
