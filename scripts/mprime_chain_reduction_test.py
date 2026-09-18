"""
两体 vs 三体：链式归约检验（唐先生 18:02「继续」）
问题：M 个素数之间的记忆，是否**完全由两体（相邻间隙对）结构生成**？还是存在**真三体**？
方法：流式分段筛；统计
  m1[g]          单间隙边缘计数
  O2[g,g']       相邻间隙对计数
  O3[g1,g2,g3]   相邻间隙三元组计数
链式（二阶 Markov）预测（无需任何模型常数）：
  O3_pred(g1,g2,g3) = O2(g1,g2)*O2(g2,g3)/m1[g2]
  （即"三体结构＝两体链"，纯二阶；若成立 ⟹ 记忆是两体）
检验：chi2 = sum (O3-O3_pred)^2/O3_pred （只用 O3_pred>0 的格）
      若 chi2/df ~ 1 ⟹ 三体完全由两体链生成（记忆=两体）
      若 chi2/df >> 1 ⟹ **真三体记忆**
另给：条件独立性核对 P(g3|g2) vs P(g3|g1,g2) 的若干实例
"""
import numpy as np
from math import log
from collections import Counter

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
            st = max(p*p, ((lo+p-1)//p)*p)
            if st <= hi: s[st-lo::p] = False
        idx = np.nonzero(s)[0].astype(np.int64) + lo
        if idx.size: yield idx
        lo = hi+1

G = 40
def run(N):
    m1 = Counter(); O2 = Counter(); O3 = Counter()
    carry = np.empty(0, np.int64)
    for P in stream_primes(N):
        arr = np.concatenate([carry, P])
        if arr.size < 4: carry = arr[-3:]; continue
        g = np.diff(arr)
        gg = g[g <= G]
        for x in gg.tolist(): m1[x] += 1
        for i in range(len(g)-1):
            if g[i] <= G and g[i+1] <= G: O2[(int(g[i]), int(g[i+1]))] += 1
        for i in range(len(g)-2):
            if g[i] <= G and g[i+1] <= G and g[i+2] <= G:
                O3[(int(g[i]), int(g[i+1]), int(g[i+2]))] += 1
        carry = arr[-3:].copy()
    print(f"\n=== N={N:,} ===  m1型数={len(m1)} O2型数={len(O2)} O3型数={len(O3)}")
    O3p = {}
    for (a,b,c), o in O3.items():
        if m1.get(b,0) > 0:
            p = O2.get((a,b),0)*O2.get((b,c),0)/m1[b]
            if p > 0: O3p[(a,b,c)] = p
    keys = [k for k in O3 if k in O3p]
    o = np.array([O3[k] for k in keys], float); p = np.array([O3p[k] for k in keys], float)
    sc = o.sum()/p.sum(); p = p*sc
    keep = p >= 5
    o, p, keys = o[keep], p[keep], [k for k,kk in zip(keys,keep) if kk]
    chi2 = ((o-p)**2/p).sum(); df = len(o)-1
    print(f"  链式预测: 格数={len(o)}  chi2={chi2:,.1f}  df={df}  chi2/df={chi2/df:.3f}")
    r = o/p; idx = np.argsort(r)
    print("  链式高估最多的 5 型:", [(keys[i], round(float(r[i]),3)) for i in idx[-5:]])
    print("  链式低估最多的 5 型:", [(keys[i], round(float(r[i]),3)) for i in idx[:5]])
    # 条件独立性实例: P(g3|g2) vs P(g3|g1,g2)
    def pg3_given(g2, g1=None):
        tot = 0; cnt = Counter()
        for (a,b,c), v in O3.items():
            if b == g2 and (g1 is None or a == g1):
                tot += v; cnt[c] += v
        return {k: v/tot for k, v in cnt.items()} if tot else {}
    print("  条件独立性核对 (P(g3|g2) vs P(g3|g1,g2)):")
    for g2 in (2, 6):
        base = pg3_given(g2)
        for g1 in (2, 6, 12):
            cd = pg3_given(g2, g1)
            common = [c for c in sorted(set(base) & set(cd)) if base[c] > 0.02]
            if len(common) >= 2:
                dev = max(abs(cd[c]-base[c])/base[c] for c in common)
                print(f"    g2={g2:2d} g1={g1:2d}: 最大相对偏差={dev:.3f}  样本型数={len(common)}  "
                      f"(示例 g3=6: P|g2={base.get(6,0):.4f} vs P|g1,g2={cd.get(6,0):.4f})")
    return chi2/df

for N in (100_000_000, 1_000_000_000):
    run(N)
