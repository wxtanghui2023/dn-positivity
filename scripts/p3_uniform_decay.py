#!/usr/bin/env python3
"""
P3 验证：自然观测类 O(A,k,B) 内的一致衰减
类 = {f : supp f ⊂ [e^{−A}, e^A], ||f||_{C^k} ≤ B}

预期：类内 |M[f](β+iγ)| ≤ C(A,k,B)·γ^{−k}——一致（Riemann-Lebesgue 一致版）

测试：
1. 固定 k——不同 f（同一类——）的衰减率一致性
2. k 增大——衰减加快（γ^{−k}——）
3. 类内 C(A,k,B) 的行为
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

# 一族测试函数（不同形状——同类——）
def make_family(A, k):
    """生成一族 C^k 紧支撑测试函数（支撑在 [e^{−A},e^A]——）"""
    fam = []
    # f1: (1−u²/A²)^{k+1} 型（C^k——）
    def f1(x):
        u = np.log(x)
        if abs(u) > A: return 0.0
        return max(0, (1 - (u/A)**2)**(k+1))
    # f2: 不同形状——sin 调制的
    def f2(x):
        u = np.log(x)
        if abs(u) > A: return 0.0
        v = 1 - (u/A)**2
        return max(0, v**(k+1) * (1 + 0.5*np.cos(np.pi*u/A)))
    # f3: 不对称
    def f3(x):
        u = np.log(x)
        if abs(u) > A: return 0.0
        return max(0, (1 - u/A)**(k+1) * (1 + u/A)**(k+1) * (1 + 0.3*u/A))
    return [f1, f2, f3]

def mellin_abs(f, sig, t):
    """|M[f](σ+it)| = |∫f(x)x^{σ+it−1}dx|——u=log x 坐标"""
    us = np.linspace(-25, 25, 40001)
    re = np.trapz([f(np.exp(u))*np.exp(sig*u)*np.cos(t*u) for u in us], us)
    im = np.trapz([f(np.exp(u))*np.exp(sig*u)*np.sin(t*u) for u in us], us)
    return np.hypot(re, im)

def main():
    print("="*70)
    print("P3：类内一致衰减验证")
    print("="*70)
    
    for A in [3, 5]:
        for k in [1, 2, 4]:
            fam = make_family(A, k)
            print(f"\nA={A}——k={k}:")
            # 对每个 f——测 γ 衰减
            gammas = [50, 100, 200, 400]
            for fi, f in enumerate(fam):
                vals = [mellin_abs(f, 0.6, g) for g in gammas]
                # 衰减指数估计：log(v1/v2)/log(g2/g1)
                if vals[0] > 1e-12:
                    expo = np.log(vals[0]/vals[-1])/np.log(gammas[-1]/gammas[0])
                    print(f"   f{fi+1}: |M| = {['%.2e'%v for v in vals]}——衰减指数 ~ {expo:.1f}（预期 {k}——）")
                else:
                    print(f"   f{fi+1}: |M| = {['%.2e'%v for v in vals]}——（数值底——）")
            # 类内一致性：max/min
            print(f"   类内最大响应（γ=50——）: {max(mellin_abs(f,0.6,50) for f in fam):.2e}")

if __name__ == "__main__":
    main()
