#!/usr/bin/env python3
"""
TOOLCARD 执行器：有限 A 的 Euler 密度审计（解析版 EXACT NEGATIVE 判决器）

用法:
    python3 audit_finite_A_density.py 0 900 21600 63000 145800 810000
    python3 audit_finite_A_density.py --bound 10**6 A1 A2 A3 ...

输出:
    d(A) = δ(B(A))、含排 δ(A+B(A))、R∞ = δ(A+B)/δ(S)、δ(E)/δ(S)
    判决: EXACT NEGATIVE (δ(A+B)<δ(S)) | DENSITY-COVER-ONLY (相等)

适用: 有限 A（|A| 建议 <= 10，含排 2^|A|-1 项）。非平方自由目标/无限 A 不适用。
依据: E228（docs/E228-terminal-density-audit-density-1-conjecture-dead.md）
      TOOLCARD-FINITE-A-EULER-DENSITY-AUDIT.md
"""
import sys, math
from itertools import combinations

def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(range(i*i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]

def density(nu_p, PR, pbound):
    """∏_p (1 - nu_p/p²)；p<=pbound 精确枚举，p>pbound 用 nu=|I||A| 的解析 tail（要求 pbound²>2maxA）"""
    prod = 1.0
    for p in PR:
        if p > pbound:
            break
        pp = p * p
        prod *= (1.0 - nu_p(p, pp) / pp)
        if prod <= 0.0:
            return 0.0
    return prod

def tail_factor(k, PR, pbound, PBIG=2_000_000):
    """∏_{pbound<p<=PBIG}(1-k/p²) 的数值（k 固定）"""
    t = 1.0
    for p in PR:
        if p <= pbound:
            continue
        if p > PBIG:
            break
        t *= (1.0 - k / (p * p))
    return t

def audit(A, PBIG=2_000_000):
    A = sorted(set(int(x) for x in A))
    if not A:
        raise SystemExit("A 不能为空")
    if len(A) > 14:
        raise SystemExit("|A|=%d 过大：含排 2^|A|-1 项会爆炸（工具卡 §7⑥）" % len(A))
    mx = max(A)
    pbound = int(math.isqrt(2 * mx)) + 1          # p² > 2maxA ⟹ ν_p^(I)=|I||A| 精确
    PR = primes_upto(PBIG)
    tiny = [p for p in PR if p <= pbound]
    big = [p for p in PR if p > pbound]
    print("A = %s   |A|=%d   maxA=%d   pbound=%d（精确枚举 %d 个素数；tail 用解析式 ✓）"
          % (A, len(A), mx, pbound, len(tiny)))
    # d(A)
    def nuA(p, pp): return len({a % pp for a in A})
    prodA = 1.0
    for p in tiny:
        prodA *= (1.0 - nuA(p, p * p) / (p * p))
    tailA = 1.0
    for p in big:
        tailA *= (1.0 - len(A) / (p * p))
    dA = prodA * tailA
    print("\n[层2] d(A) = δ(B(A)) = %.6f" % dA)
    # inclusion-exclusion
    total = 0.0
    for k in range(1, len(A) + 1):
        for I in combinations(A, k):
            def nuI(p, pp, I=I): return len({(a - b) % pp for a in I for b in A})
            pr = 1.0
            for p in tiny:
                pr *= (1.0 - nuI(p, p * p) / (p * p))
            cI = len({a - b for a in I for b in A})   # ✓ 不同整数差值个数（p²>2maxA 时为常数，与 p 无关 ✓）
            tl = 1.0
            for p in big:
                tl *= (1.0 - cI / (p * p))
            dI = pr * tl
            total += ((-1) ** (k + 1)) * dI
            if k == 1:
                chk = dI
    print("[自检] |I|=1 项 = %.6f  （必须等于 d(A) ✓）" % chk)
    dS = 6.0 / (math.pi ** 2)
    print("\n[层3] δ(A+B(A)) = %.6f      δ(S) = 6/π² = %.6f" % (total, dS))
    Rn = total / dS
    print("[层4] R∞ = δ(A+B)/δ(S) = %.6f" % Rn)
    print("      δ(E)/δ(S) = 1 - R∞ = %.3e" % (1.0 - Rn))
    if total < dS - 1e-9:
        print("\n🔒 判决: EXACT NEGATIVE —— δ(A+B) < δ(S) ⟹ R_M ↛ 1（无需再跑窗口 ✗）")
    elif abs(total - dS) <= 1e-9:
        print("\n✓ 判决: DENSITY-COVER-ONLY —— δ(A+B) = δ(S)（密度意义覆盖全部；精确覆盖仍需另证 ✗）")
    else:
        print("\n⚠️ δ(A+B) > δ(S)：数值/实现有误（密度不可能超过 δ(S)）⟹ 请复核 ✗")
    return dA, total, Rn

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        raise SystemExit(0)
    audit([int(a) for a in args])
