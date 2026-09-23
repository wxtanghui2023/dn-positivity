#!/usr/bin/env python3
# cas1_finite_order_anomaly_scan.py —— CAS-1 第一阶段：RH 相关对象的低阶有限差分异常扫描
# 【对象】 Z(t)=Riemann–Siegel 实值函数（零 = 临界线零点）；对照：C(t)=sum_{n<=N} cos(t log n)/sqrt(n)
# 【操作】 只允许 shift / finite difference（Δ_h^k），不引入任何目标导向系数
# 【记录】 六项：异常消失 / 整有理结构 / 稳定递推 / 跨尺度不变量 / 非平凡因子化 / 某阶后结构突变
# 【输出】 out/cas1/cas1_scan.txt ；结论由数字驱动（R7）
import mpmath as mp
mp.mp.dps = 25

def Zfun(t):
    t = mp.mpf(t)
    th = mp.im(mp.loggamma(mp.mpf('0.25') + 1j*t/2)) - (t/2)*mp.log(mp.pi)
    return mp.re(mp.e**(1j*th) * mp.zeta(mp.mpf('0.5') + 1j*t))

NC = 60
def Cfun(t):
    t = mp.mpf(t); s = mp.mpf(0)
    for n in range(2, NC+1):
        s += mp.cos(t*mp.log(n))/mp.sqrt(n)
    return s

def diff_coeffs(k):
    from math import comb
    return [(-1)**(k-j)*comb(k, j) for j in range(k+1)]

def scan(fun, T0, W, delta, h_mult, kmax=2):
    n = int(W/delta); offs = h_mult*kmax
    # 缓存一维求值
    cache = {}
    def f(t):
        key = int(round((t-T0)/delta))
        if key not in cache: cache[key] = fun(t)
        return cache[key]
    D = {k: [] for k in range(kmax+1)}
    c = {k: diff_coeffs(k) for k in range(kmax+1)}
    for j in range(n+1):
        t = T0 + j*delta
        for k in range(kmax+1):
            val = mp.mpf(0)
            for i, cf in enumerate(c[k]):
                val += cf*f(t + i*h_mult*delta)
            D[k].append(val)
    # Gram 矩阵 Q_kl = sum_j D_k D_l
    Q = [[mp.mpf(0) for _ in range(kmax+1)] for _ in range(kmax+1)]
    for j in range(n+1):
        for k in range(kmax+1):
            for l in range(kmax+1):
                Q[k][l] += D[k][j]*D[l][j]
    return Q

def report(tag, Q, kmax=2):
    # 归一化
    q00 = Q[0][0]
    M = [[Q[k][l]/q00 for l in range(kmax+1)] for k in range(kmax+1)]
    # 特征值（对称）
    try:
        ev = mp.eigsy(mp.matrix(M), eigvals_only=True)
        ev = sorted([float(e) for e in ev])
    except Exception:
        ev = None
    det = float(mp.det(mp.matrix(M)))
    print(f"  [{tag}] Q00={float(q00):.6e}")
    print(f"  [{tag}] 归一化 Gram: M11={float(M[1][1]):.9f}  M22={float(M[2][2]):.9f}  M12={float(M[1][2]):.9f}")
    print(f"  [{tag}] det={det:.9e}  特征值={['%.6e'%e for e in ev] if ev else 'NA'}")
    print(f"  [{tag}] 比值 M11/M22={float(M[1][1]/M[2][2]):.9f}")
    return M, ev, det

if __name__ == '__main__':
    delta = mp.mpf('0.05'); hm = 2
    print("=== CAS-1 第一阶段：低阶有限差分异常扫描（Z 与对照 C）===")
    res = {}
    for T0 in (500, 1000, 2000):
        print(f"--- 窗口 T0={T0}, W=100, delta={float(delta)}, h={hm}*delta ---")
        Qz = scan(Zfun, mp.mpf(T0), mp.mpf(100), delta, hm)
        Mz, evz, detz = report('Z', Qz)
        Qc = scan(Cfun, mp.mpf(T0), mp.mpf(100), delta, hm)
        Mc, evc, detc = report('C', Qc)
        res[T0] = (Mz, evz, detz, Mc, evc, detc)
    print()
    print("=== 跨尺度比较（Z 与 C 的 M11/M22 与 det）===")
    for T0 in (500, 1000, 2000):
        Mz, evz, detz, Mc, evc, detc = res[T0]
        rz = Mz[1][1]/Mz[2][2]; rc = Mc[1][1]/Mc[2][2]
        print(f"  T0={T0}: Z 比值={float(rz):.9f} det={detz:.6e} | C 比值={float(rc):.9f} det={detc:.6e}")
