"""
(a)+(b): M 窗口残留的形状检验（Pearson）＋ N=1e9 数据点
模型 G（全局，1 参数）：lambda = C * S(D) * exp(-span/log x)
模型 S（逐跨度）：      lambda = C_s * S(D)     （每个跨度一个参数）
检验： Pearosn chi2 = sum (O-lambda)^2/lambda ; df = 型数 - 参数数
      若 chi2/df ~ 1  => 残差与多项/泊松噪声一致 => 无额外形状结构
      若 chi2/df >> 1 => 存在超出模型的形状依赖（仅定位，不解释）
流式分段筛，内存 O(段长)。
"""
import numpy as np, sys
from math import log

def base_primes(r):
    s = np.ones(r+1, bool); s[:2] = False
    for i in range(2, int(r**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def stream_primes(N, seg=10**7):
    bp = base_primes(int(N**0.5)+1)
    lo = 2
    while lo <= N:
        hi = min(lo+seg-1, N)
        s = np.ones(hi-lo+1, bool)
        if lo <= 2: s[:max(0, 3-lo)] = False
        for p in bp:
            if p*p > hi: break
            start = max(p*p, ((lo+p-1)//p)*p)
            if start <= hi: s[start-lo::p] = False
        idx = np.nonzero(s)[0].astype(np.int64) + lo
        if idx.size: yield idx
        lo = hi+1

def sing_tuple_int(D, QP):
    k = len(D); val = 1.0
    for p in QP:
        nu = len(set(d % p for d in D))
        if nu >= p: return 0.0
        val *= (1 - nu/p) / (1 - 1/p)**k
    return val

def run(N, M, span_max, QP):
    from collections import Counter
    cnt = Counter(); carry = np.empty(0, np.int64); npairs = 0
    for P in stream_primes(N):
        arr = np.concatenate([carry, P])
        if arr.size < M+1:
            carry = arr[-M:]; continue
        g = np.diff(arr)
        W = np.lib.stride_tricks.sliding_window_view(g, M)
        sp = W.sum(axis=1)
        sel = sp <= span_max
        Ws = W[sel]
        if Ws.size:
            key = np.zeros(len(Ws), np.int64)
            for j in range(M): key = key*64 + Ws[:, j]
            uk, uc = np.unique(key, return_counts=True)
            for k_, c_ in zip(uk.tolist(), uc.tolist()):
                pat = []
                for _ in range(M):
                    pat.append(k_ % 64); k_ //= 64
                cnt[tuple(reversed(pat))] += c_
            npairs += int(sel.sum())
        carry = arr[-(M):].copy()
    print(f"\n=== N={N:,}  M={M}  span<={span_max}  窗口数={npairs:,}  型数={len(cnt)} ===")
    pats = [(g, c) for g, c in cnt.items() if c >= 20]
    S = np.array([sing_tuple_int((0,)+tuple(np.cumsum(g)), QP) for g, _ in pats])
    O = np.array([c for _, c in pats], float)
    span = np.array([sum(g) for g, _ in pats], float)
    keep = S > 0; O, S, span = O[keep], S[keep], span[keep]
    pats = [p for p, k_ in zip(pats, keep) if k_]
    lx = log(N)
    # 模型 G：单参数
    base = S * np.exp(-span/lx)
    CG = O.sum()/base.sum(); lamG = CG*base
    # 模型 S：逐跨度单参数
    lamS = np.zeros_like(O)
    for s in np.unique(span):
        m = span == s
        Cs = O[m].sum()/S[m].sum(); lamS[m] = Cs*S[m]
    def rep(lam, name, dfoff):
        chi2 = ((O-lam)**2/lam).sum(); df = len(O)-dfoff
        print(f"  {name}: chi2={chi2:12.1f}  df={df:5d}  chi2/df={chi2/df:7.3f}")
        return chi2/df
    rG = rep(lamG, "模型G(奇异级数×跨度律,1参数)", 1)
    # 逐跨度模型的 df：每个跨度消耗 1
    nspan = len(np.unique(span)); rS = rep(lamS, f"模型S(逐跨度,{nspan}参数)", nspan)
    # 逐跨度内部残差
    print("  span  型数   chi2/df(模型S内)   log(O/P)均值   std")
    for s in np.unique(span):
        m = span == s
        if m.sum() >= 5:
            chi2 = ((O[m]-lamS[m])**2/lamS[m]).sum(); df = m.sum()-1
            lr = np.log(O[m]/lamS[m])
            print(f"  {int(s):4d} {int(m.sum()):5d}     {chi2/max(df,1):7.3f}        {lr.mean():+.4f}      {lr.std():.4f}")
    ratio = O/lamS; idx = np.argsort(ratio)
    print("  最被高估 4 型:", [(pats[i][0], round(float(ratio[i]),3)) for i in idx[-4:]])
    print("  最被低估 4 型:", [(pats[i][0], round(float(ratio[i]),3)) for i in idx[:4]])
    return rG, rS

qp = base_primes(100_000).tolist()
print(f"奇异级数截断素数={len(qp)}")
for N in (20_000_000, 100_000_000):
    run(N, 3, 40, qp)
run(1_000_000_000, 3, 40, qp)
