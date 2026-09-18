# -*- coding: utf-8 -*-
# 仅用于离线数据分析（非研究结论）
import array, math
from collections import Counter

N = 20_000_000
sv = bytearray([1]) * (N + 1)
sv[0] = sv[1] = 0
i = 2
while i * i <= N:
    if sv[i]:
        sv[i*i::i] = bytearray(len(range(i*i, N+1, i)))
    i += 1
primes = array.array('l', [j for j in range(2, N + 1) if sv[j]])
del sv
n = len(primes)
gaps = array.array('l', (primes[k+1] - primes[k] for k in range(n - 1)))
m = len(gaps)
print(f"N={N:,}  素数个数={n:,}  间隙个数={m:,}")
print(f"最大间隙={max(gaps)}  平均间隙={sum(gaps)/m:.5f}  log(N)={math.log(N):.5f}")

# 1) 间隙分布（前若干值）
c = Counter(gaps)
tot = m
print("\n[1] 间隙分布（占比，随机模型=P(间隙=2k)=e^{-2k/log p}-e^{-(2k+2)/log p} 近似）")
for g in (2,4,6,8,10,12,14,16,18,20,30,50):
    print(f"   gap={g:3d}: {c.get(g,0)/tot:.6f}  ({c.get(g,0):,})")

# 2) 间隙自相关（滞后 1..4）
def corr(x, y):
    mx = sum(x)/len(x); my = sum(y)/len(y)
    sxy = sum((a-mx)*(b-my) for a,b in zip(x,y))
    sx = math.sqrt(sum((a-mx)**2 for a in x)); sy = math.sqrt(sum((b-my)**2 for b in y))
    return sxy/(sx*sy)
print("\n[2] 间隙序列自相关（Cramér 随机模型预测 = 0）")
for lag in (1,2,3,4):
    r = corr(gaps[:m-lag], gaps[lag:])
    se = 1/math.sqrt(m)
    print(f"   lag={lag}: r={r:+.5f}   (标准误≈{se:.5f};  |r|/se={abs(r)/se:.1f}σ)")

# 3) 条件分布 P(g_{n+1}=g' | g_n=g)
print("\n[3] 条件分布（行=g_n, 列=g_{n+1}）: P(g'|g) 与边际 P(g')")
small = (2,4,6,8,10,12)
marg = {g: c.get(g,0)/tot for g in small}
print("      " + "".join(f"{g:>9d}" for g in small))
for g in small:
    idx = [k for k in range(m-1) if gaps[k]==g]
    if len(idx) < 100: continue
    nxt = Counter(gaps[k+1] for k in idx)
    row = f"   {g:3d} n={len(idx):7d} " + "".join(f"{nxt.get(h,0)/len(idx):9.5f}" for h in small)
    print(row)
print("   边际 P(g')      " + "".join(f"{marg[h]:9.5f}" for h in small))

# 4) 残类转移：mod 3、mod 4、mod 10（末位）
def transitions(mod, allowed=None):
    P = primes[:n]
    cnt = Counter()
    for k in range(n-1):
        a, b = P[k] % mod, P[k+1] % mod
        cnt[(a,b)] += 1
    keys = allowed if allowed else sorted({a for a,_ in cnt})
    return cnt, keys

for mod, allowed, note in ((3, [1,2], "素数>3 只能 ≡1 或 2 (mod 3)"),
                           (10, [1,3,7,9], "素数>5 末位只能 1,3,7,9"),
                           (4, [1,3], "素数>2 只能 ≡1 或 3 (mod 4)")):
    cnt, keys = transitions(mod, allowed)
    tt = sum(cnt.values())
    print(f"\n[4] 连续素数残类转移 mod {mod}（{note}）；总计 {tt:,} 对")
    print("      " + "".join(f"{b:>11d}" for b in keys))
    for a in keys:
        row = f"   {a:>3d} " + "".join(f"{cnt.get((a,b),0)/tt:11.6f}" for b in keys)
        print(row)
    print("   边际 " + "".join(f"{sum(cnt.get((a,b),0) for a in keys)/tt:11.6f}" for b in keys))
    # 对角（同类）占比 vs 随机模型预测
    same = sum(cnt.get((a,a),0) for a in keys)/tt
    marg_same = sum((sum(cnt.get((a,b),0) for b in keys)/tt) * (sum(cnt.get((b2,a),0) for b2 in keys)/tt) for a in keys)
    print(f"   同类相邻占比={same:.6f}   随机(独立)模型预测={marg_same:.6f}   比值={same/marg_same:.4f}  ⟹ {'低于' if same<marg_same else '高于'}随机")
