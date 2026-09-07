#!/usr/bin/env python3
"""
II 缺陷指数考古——乘性 dilation/卷积算子族
B_f: (B_f h)(k) = Σ_{d≥1} f(d) h(dk)——乘性 dilation
A_f: (A_f g)(n) = Σ_{d|n} f(d) g(n/d)——Dirichlet 卷积

关键观察：h(k) = k^{−s} 是 B_f 形式特征函数——特征值 F(s) = Σf(d)d^{−s}
- f = 1：F = ζ
- k^{−s} ∈ ℓ²(ℕ) ⟺ Re s > ½——谱边界 Re s = ½！

数值探索：有限截断 dilation 矩阵的特征值——大 N 结构
"""
import numpy as np

def dilation_matrix(N, f):
    """(B_f h)(k) = Σ_{d: dk≤N} f(d) h(dk)——k = 1..N"""
    B = np.zeros((N, N))
    for k in range(1, N+1):
        for d in range(1, N//k + 1):
            B[k-1, d*k-1] += f[d]
    return B

def main():
    print("="*70)
    print("II 考古：乘性 dilation 算子 B_f")
    print("="*70)
    
    # f = 1（除数 dilation——）——F(s) = ζ(s)
    N = 100
    f1 = np.ones(N+1)
    B = dilation_matrix(N, f1)
    
    # B 是上三角？（dk ≥ k——d ≥ 1——所以 B[k, dk]——列 ≥ 行——上三角——）
    # 上三角——特征值 = 对角 = B[k,k] = f(1) = 1——全 1？——平凡？
    ev = np.linalg.eigvals(B)
    print(f"B₁ (f=1——) 特征值: 全 1? {np.allclose(np.sort_complex(ev), 1)}——对角 = f(1) = 1")
    print("  → dilation 矩阵上三角（dk≥k——）——特征值 = f(1)——平凡——")
    
    # 需要非三角结构——用 f(d) = μ(d) 或变号——或——考虑"收缩"版本
    # 关键：B_f 上三角因为 d ≥ 1（dk ≥ k——）——特征值全 f(1)
    # 那缺陷指数从哪来？——无界算子（N→∞——）的定义域问题——不是有限矩阵谱
    
    print("\n关键认识：有限截断 dilation 是上三角（dk ≥ k——）——特征值 = f(1)——")
    print("缺陷结构来自无界（N→∞——）定义域——不是有限矩阵谱")
    print()
    print("形式特征函数分析：h_s(k) = k^{−s}——(B_f h_s)(k) = F(s)·k^{−s}")
    print("  F(s) = Σf(d)d^{−s}——f=1: F = ζ(s)")
    print("  h_s ∈ ℓ²(ℕ) ⟺ Re s > ½")
    print()
    print("缺陷方程：B_f h = ±i h——形式解 h = k^{−s}——ζ(s) = ±i（f=1——）")
    print("  ζ(s) = ±i 的根 Re s > ½？——ζ 无零点 Re > ½（若 RH——但无条件——）")
    print("  无条件：ζ 零点 Re ≤ 1——ζ(s) = ±i 与零点不同（ζ = ±i ≠ 0——）")
    
    # ζ(s) = ±i 的根在哪？
    print("\nζ(σ+it) = ±i 的根（数值扫描——）:")
    import mpmath as mp
    mp.mp.dps = 15
    # 扫 σ ∈ [0.5, 1.5], t ∈ [0, 30]——找 |ζ − i| 或 |ζ + i| 小——（不精确——粗扫——）
    found = []
    for sigma in [0.55, 0.6, 0.65, 0.7, 0.8, 0.9, 1.0, 1.1]:
        for t in np.arange(0, 30, 0.5):
            z = mp.zeta(sigma + 1j*t)
            if abs(z - 1j) < 0.5 or abs(z + 1j) < 0.5:
                found.append((sigma, t, abs(z-1j), abs(z+1j)))
    print(f"  粗扫找到 {len(found)} 个近根点（|ζ∓i|<0.5——）:")
    for f_ in found[:8]:
        print(f"    σ={f_[0]}, t={f_[1]:.1f}——|ζ−i|={f_[2]:.3f}——|ζ+i|={f_[3]:.3f}")

if __name__ == "__main__":
    main()
