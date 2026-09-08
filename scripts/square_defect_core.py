#!/usr/bin/env python3
# 第三层（平方映射全局尺度缺陷——）第一轮数值检查
# K_s(a,b) = (a+b)^{-2s} - a^{-2s} - b^{-2s}
# 归一化核: K̃_s(a,b) = K_s(a,b) / sqrt(ab)
# 数值探索: Σ_{a,b≤N} K̃_s(a,b) 随 N 的行为（s=1/2 vs s=1/3——）
# 如果 s=1/2 是"临界"（收敛/发散分界——）——那就是 Re s=1/2 的结构性约束——

import numpy as np

def K_s(a, b, s):
    """K_s(a,b) = (a+b)^{-2s} - a^{-2s} - b^{-2s}"""
    return (a+b)**(-2*s) - a**(-2*s) - b**(-2*s)

def K_tilde(a, b, s):
    """归一化核"""
    return K_s(a, b, s) / np.sqrt(a*b)

def sum_K(N, s):
    """Σ_{a,b≤N} K̃_s(a,b)"""
    total = 0.0
    for a in range(1, N+1):
        inv_a = a**(-2*s)
        sqrt_a = np.sqrt(a)
        for b in range(1, N+1):
            inv_b = b**(-2*s)
            inv_ab = np.sqrt(a*b)
            total += ((a+b)**(-2*s) - inv_a - inv_b) / inv_ab
    return total

def sum_K_fast(N, s):
    """向量化版本——更快"""
    a = np.arange(1, N+1)
    b = np.arange(1, N+1)
    A, B = np.meshgrid(a, b, indexing='ij')
    inv_a = A**(-2*s)
    inv_b = B**(-2*s)
    inv_ab = np.sqrt(A * B)
    term = (A + B)**(-2*s) - inv_a - inv_b
    return np.sum(term / inv_ab)

print('=== 第三层第一轮：归一化核 Σ_{a,b≤N} K̃_s(a,b) 随 N ===')
print('（s=1/2（临界——） vs s=1/3（非临界——）——）')
print()
for s in [0.5, 0.333, 0.4, 0.6]:
    print(f'--- s = {s} ---')
    for N in [50, 100, 200, 400]:
        try:
            val = sum_K_fast(N, s)
            print(f'  N={N:>3}: Σ = {val:+.4f}')
        except Exception as e:
            print(f'  N={N:>3}: 错误 {e}')
    print()

print('=== 检查：s=1/2 的“临界性”——是否收敛/发散？===')
for N in [50, 100, 200, 400, 800]:
    try:
        val = sum_K_fast(N, 0.5)
        print(f'N={N:>3}: {val:+.4f}')
    except Exception as e:
        print(f'N={N:>3}: 错误 {e}')
        break
