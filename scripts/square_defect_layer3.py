#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 第三层：平方映射缺陷——精确分析 K_s(a,b) = (a+b)^{-2s} - a^{-2s} - b^{-2s}
# 关键问题：s=1/2 时是否有特殊结构？

import numpy as np

def K(a, b, s):
    return (a+b)**(-2*s) - a**(-2*s) - b**(-2*s)

# 1. s=1/2 时 K 的精确形式
print('=== s=1/2 时 K_{1/2}(a,b) 的精确形式 ===')
print('K_{1/2}(a,b) = 1/(a+b) - 1/a - 1/b')
print('           = [ab - b(a+b) - a(a+b)] / [ab(a+b)]')
print('           = [ab - ab - b² - a² - ab] / [ab(a+b)]')
print('           = -(a² + ab + b²) / [ab(a+b)]')
print()
print('这不是零——是负值——检查其结构——')
print()

# 2. 用 x=a/b 归一化
print('=== 归一化形式 f_s(x) = K_s(bx, b) / b^{-2s} ===')
print('f_s(x) = (x+1)^{-2s} - x^{-2s} - 1')
print()
print('s=1/2 时 f_{1/2}(x) = 1/(x+1) - 1/x - 1 = -(x²+x+1)/[x(x+1)]')
for x in [0.5, 1.0, 2.0, 4.0]:
    exact = -(x**2 + x + 1) / (x * (x + 1))
    print(f'  x={x}: f(1/2) = {exact:.6f}')
print()

# 3. 检查 s=1/2 是否是"临界"——看 f_s 对 s 的导数
print('=== f_s(1) 随 s 的演化（a=b 情况——）===')
for s in [0.3, 0.4, 0.5, 0.6, 0.7]:
    v = (2)**(-2*s) - 2*1**(-2*s)  # f_s(1) = 2^{-2s} - 2
    print(f's={s:.1f}: f_s(1) = {v:+.6f}')
print()
print('结论：f_s(1) 单调——无 s=1/2 特殊——')
print()

# 4. 关键问题：K_s 的"谱"（对偶）是什么？
# 计算 K_s 在某种内积下的"范数"——看 s=1/2 是否特殊
print('=== K_{1/2} 在 [1,N]² 上的 L² 范数——看 N 标度——')
for N in [100, 200, 400, 800, 1600]:
    total = 0.0
    for a in range(1, N+1):
        for b in range(1, N+1):
            total += K(a, b, 0.5)**2
    # 期望：~ C * N^α log^β N
    print(f'N={N:>4}: ||K||² = {total:.1f}  (N²={N*N:>6} —— 比值={total/(N*N):.4f})')
print()
print('如果比值收敛到常数——则 ||K|| ~ N —— 尺度指数 1 ——')
print('如果发散——可能标度不同——')
