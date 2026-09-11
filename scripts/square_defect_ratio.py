#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 第三层：平方映射缺陷——尺度商 x = a/b 上的归一化结构
# K_s(a,b) = (a+b)^{-2s} - a^{-2s} - b^{-2s}
# 用 x = a/b 归一化：K_s(a,b) / b^{-2s} = (x+1)^{-2s} - x^{-2s} - 1
# =: f_s(x) ——只依赖 x = a/b ——
# 分析说的 x <-> x^{-1} 反演对称：f_s(x) vs f_s(1/x)
# 检查：x=1（a=b）时——缺陷值——以及 f_s 的"形状"——

import numpy as np

def f_s(x, s):
    """归一化缺陷：f_s(x) = (x+1)^{-2s} - x^{-2s} - 1"""
    return (x+1)**(-2*s) - x**(-2*s) - 1.0

def f1_s(x, s):
    """另一种归一化：乘 x^{2s}——"""
    return (1 + 1/x)**(-2*s) - 1 - x**(2*s)

print('=== f_s(x) = (x+1)^{-2s} - x^{-2s} - 1 ===')
print('(仅依赖 x = a/b——无加卷积——保留 x <-> 1/x 对称——）')
print()
print('s=1/2 时 f_{1/2}(x)：')
for x in [0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 4.0, 10.0]:
    v = f_s(x, 0.5)
    print(f'  x={x:>5.2f}: f(x) = {v:+.6f}')
print()
print('s=1/3 时 f_{1/3}(x)：')
for x in [0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 4.0, 10.0]:
    v = f_s(x, 1/3)
    print(f'  x={x:>5.2f}: f(x) = {v:+.6f}')
print()
print('=== 检查 x <-> 1/x 对称 ===')
print('（若 f(1/x) = f(x)——则 x <-> 1/x 是自对偶——s=1/2 时？——）')
for s in [0.5, 1/3, 0.6]:
    print(f's={s}:')
    for x in [0.2, 0.5, 2.0, 5.0]:
        v1 = f_s(x, s)
        v2 = f_s(1/x, s)
        print(f'  x={x}: f({x})={v1:+.6f}  f(1/{x})={v2:+.6f}  差={abs(v1-v2):.2e}')
print()
print('=== 关键问题：x=1（a=b——）时 f_s 的值——及与 "零点约束" 的关系 ===')
for s in [0.5, 1/3, 0.6, 0.7]:
    v1 = f_s(1.0, s)
    print(f's={s}: f(1) = {v1:+.6f}')
