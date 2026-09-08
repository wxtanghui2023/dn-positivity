#!/usr/bin/env python3
# 平方线索第一轮：a+b=c 在 F₂ parity 层（v_p mod 2）上的转移律
# ε_p(n) = v_p(n) mod 2——数 (a,b) 的 (ε(a), ε(b), ε(a+b)) 分布——看尺度稳定不变量
import numpy as np

def eps(n, p):
    """v_p(n) mod 2"""
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v % 2

def parity_transfer(N, p):
    """数 (a,b) ∈ [1,N]² 按 (ε(a),ε(b),ε(a+b)) 分类——"""
    # 先算 ε(n) for n ≤ 2N
    e = [0]*(2*N+1)
    for n in range(1, 2*N+1):
        e[n] = eps(n, p)
    # 计数 8 类
    cnt = np.zeros((2,2,2))
    for a in range(1, N+1):
        ea = e[a]
        for b in range(1, N+1):
            cnt[ea, e[b], e[a+b]] += 1
    return cnt

print('=== p=2: a+b=c 的 parity 转移（ε₂(a),ε₂(b) → ε₂(a+b)——）===')
for N in [200, 400, 800, 1600]:
    cnt = parity_transfer(N, 2)
    total = N*N
    # 归一化：给定 ε(a),ε(b)——ε(c)=1 的比例
    print(f'\nN={N}:')
    for ea in [0,1]:
        for eb in [0,1]:
            s = cnt[ea,eb,0] + cnt[ea,eb,1]
            if s > 0:
                p1 = cnt[ea,eb,1]/s
                print(f'  ε(a)={ea} ε(b)={eb}: P(ε(c)=1) = {p1:.4f}（计数 {int(s)}——）')
print()
print('=== 检查：ε(c) 的条件分布是否 50/50（无偏置——）或偏置？ ===')
print('（乘法下 parity 线性 ε(ab)=ε(a)+ε(b)——加法下呢？——）')
