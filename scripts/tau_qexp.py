#!/usr/bin/env python3
"""
生成 τ(n)（Δ 的系数——）到 N——用 q-展开
Δ(q) = q·Π_{n≥1}(1−qⁿ)²⁴ = Σ τ(n) qⁿ
方法：先算 η(q) = Π(1−qⁿ) 的系数（欧拉五边形数定理——稀疏——）
然后 24 次方（用 log/exp 或迭代卷积——）
"""
import numpy as np

def eta_coeffs(N):
    """η(q) = Π(1−qⁿ) 系数到 N——五边形数定理：系数 ±1 稀疏"""
    c = np.zeros(N+1, dtype=np.int64)
    c[0] = 1
    for k in range(1, int(np.sqrt(N))+2):
        for sgn, exp in [(1, k*(3*k-1)//2), (-1, k*(3*k+1)//2)]:
            if exp <= N:
                c[exp] += (-1)**(k+1) if sgn == 1 else (-1)**k
            else:
                break
        if k*(3*k-1)//2 > N and k*(3*k+1)//2 > N:
            break
    return c

def pow24_fft(eta, N):
    """eta^24——FFT 卷积——"""
    try:
        from scipy.signal import fftconvolve
    except ImportError:
        print("scipy 不可用——")
        raise
    def conv(a, b):
        out = fftconvolve(a, b)[:len(a)]
        return np.round(out).astype(np.int64)
    e2 = conv(eta, eta)
    e4 = conv(e2, e2)
    e8 = conv(e4, e4)
    e16 = conv(e8, e8)
    e24 = conv(e16, e8)
    return e24

def main():
    N = 200000
    print(f"生成 τ(n) 到 {N}——")
    eta = eta_coeffs(N)
    nz = np.nonzero(eta)[0]
    print(f"η 非零系数: {len(nz)} 个（五边形数——）")
    e24 = pow24_fft(eta, N)
    # τ(n) = e24[n-1]（Δ = q·η^24——）
    tau = np.zeros(N)
    tau[1:] = e24[:N-1]
    # 验证已知值
    known = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830, 6: -6048, 7: -16744, 8: 84480}
    ok = True
    for n, v in known.items():
        match = tau[n] == v
        if not match:
            ok = False
            print(f"  τ({n}) = {tau[n]}——期望 {v}——错！")
    print(f"验证: {'全部通过 ✓' if ok else '有错——'}")
    if ok:
        np.save('/home/node/.openclaw/workspace/dn-project/data/tau_200k.npy', tau)
        print(f"已保存 data/tau_200k.npy——τ(1..{N})")

if __name__ == "__main__":
    main()
