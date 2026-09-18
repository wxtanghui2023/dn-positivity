"""
M 重素数窗口「记忆/关联」诊断（唐先生 2026-09-18 17:05 提案 2）
问题：M 个连续素数的「中间数字」（间隙型 g_1..g_M）是否携带超出
      (i) 可容许性（周期性，mod 小素数）+ (ii) Hardy–Littlewood 奇异级数
      之外的**关联结构**？
方法：筛到 N=2e7；对 M=3,4 枚举连续间隙型；算 HL 奇异级数 S(D)（截断素数 p<=1e5）；
      用单参数全局常数拟合（吸收归一化）后看 log(O/P) 的
      (a) 与总跨度 span 的相关性（局部效应），(b) 与形状的关系（额外结构）。
预注册判定：若 log(O/P) 只随 span 系统变化、且同 span 下形状间离散小 ⟹ 记忆=局部（可容许+HL）；
            若同 span 下仍有系统性形状依赖 ⟹ 存在额外关联（仅诊断，非证明）。
"""
import numpy as np

N = 20_000_000
print(f"=== 筛到 N={N:,} ===")
sieve = bytearray([1]) * (N + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2, N + 1) if sieve[i]]
print(f"素数个数 = {len(primes):,}")

# HL 奇异级数（截断）
QP = [p for p in primes if p <= 100_000]
print(f"奇异级数截断素数个数 = {len(QP)}")

def sing_tuple(D):
    """D: tuple of offsets (0 = first element). S(D)=prod_p (1-nu_p/p)/(1-1/p)^|D|"""
    k = len(D)
    val = 1.0
    for p in QP:
        nu = len(set(d % p for d in D))
        if nu >= p:
            return 0.0
        val *= (1 - nu / p) / (1 - 1 / p) ** k
    return val

def scan(M, span_max):
    from collections import Counter
    cnt = Counter()
    for i in range(len(primes) - M):
        g = [primes[i + j + 1] - primes[i + j] for j in range(M)]
        s = sum(g)
        if s <= span_max:
            cnt[tuple(g)] += 1
    return cnt

print()
for M, span_max in ((3, 36), (4, 32)):
    cnt = scan(M, span_max)
    pats = [(g, c) for g, c in cnt.items() if c >= 30]
    if not pats:
        print(f"M={M}: 无足够样本"); continue
    O = np.array([c for _, c in pats], float)
    S = np.array([sing_tuple((0,) + tuple(np.cumsum(g))) for g, _ in pats], float)
    keep = S > 0
    O, S, pats = O[keep], S[keep], [p for p, k in zip(pats, keep) if k]
    C = O.sum() / S.sum()          # 单参数全局归一化
    P = C * S
    ratio = O / P
    span = np.array([sum(g) for g, _ in pats], float)
    lr = np.log(ratio)
    print(f"=== M={M}（型数={len(pats)}，span<={span_max}）===")
    print(f"  归一化常数 C = {C:.6g}")
    print(f"  log(O/P): 均值={lr.mean():+.4f}  标准差={lr.std():.4f}  min={lr.min():+.3f} max={lr.max():+.3f}")
    print(f"  corr(log(O/P), span) = {np.corrcoef(lr,span)[0,1]:+.4f}")
    # span 分层：看同 span 内部的离散（形状效应）
    print("  span  型数  log(O/P)均值  log(O/P)标准差")
    for s in sorted(set(span)):
        m = span == s
        if m.sum() >= 4:
            print(f"  {int(s):4d} {int(m.sum()):5d}     {lr[m].mean():+.4f}        {lr[m].std():.4f}")
    # 极端型
    idx = np.argsort(ratio)
    print("  最被低估 3 型:", [(pats[i][0], round(float(ratio[i]),3)) for i in idx[:3]])
    print("  最被高估 3 型:", [(pats[i][0], round(float(ratio[i]),3)) for i in idx[-3:]])
    print()
