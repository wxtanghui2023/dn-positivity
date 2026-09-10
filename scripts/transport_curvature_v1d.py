#!/usr/bin/env python3
"""算术运输曲率 v1（最终修正版）
A-运输 T_A(a,b,c) = (b, c, b+c)
M-运输 T_M(S)     = u(S)·S,  u(S)=rad(c)
两个端点：
  SAM = T_M(T_A S) = rad(b+c)·(b, c, b+c)
  SMA = T_A(T_M S) = rad(c)·(b, c, b+c)      ⟹ 必在同一条射线上（结构事实）
曲率 Ω(S) = log[ W(SAM)·W(S) / ( W(S_A)·W(S_M) ) ]
"""
import math, statistics

LIM = 10**6
rad = [1]*(LIM+1); rad[0] = 0
sieve = bytearray([1])*(LIM+1)
for p in range(2, LIM+1):
    if sieve[p]:
        for m in range(p, LIM+1, p):
            sieve[m] = 0
            rad[m] *= p

def Om(a, b, scale_sensitive):
    c = a + b
    SA = (b, c, b + c)                       # T_A
    u = rad[c]
    SM = (u*a, u*b, u*c)                     # T_M
    u2 = rad[b + c]
    SAM = (u2*b, u2*c, u2*(b + c))           # T_M∘T_A
    if scale_sensitive:
        W = lambda T: rad[T[0]]*rad[T[1]]*rad[T[2]]
    else:
        W = lambda T: (rad[T[0]]*rad[T[1]]*rad[T[2]])/(T[0]*T[1]*T[2])
    return math.log(W(SAM)*W((a, b, c))/(W(SA)*W(SM)))

N = 400
print('=== v1 曲率扫描（a+b=c, c <= %d）===' % N, flush=True)
for name, ss in [('W1 = rad/(abc)  形状不变', False),
                 ('W2 = rad(abc)   尺度敏感', True)]:
    nz = 0; tot = 0; mx = -1e9; mn = 1e9
    for a in range(1, N):
        for b in range(a, N-a+1):
            tot += 1
            v = Om(a, b, ss)
            if abs(v) > 1e-12:
                nz += 1; mx = max(mx, v); mn = min(mn, v)
    print('  %s : 非零 %d/%d = %.6f' % (name, nz, tot, nz/tot)
          + ('   范围[%.6f, %.6f]' % (mn, mx) if nz else '   <= Omega === 0'), flush=True)

print()
print('=== 尺度敏感情形：Omega 是否完全由 rad 比解释 ===', flush=True)
data = []
for a in range(1, 200):
    for b in range(a, 200-a+1):
        data.append((Om(a, b, True), math.log(rad[a+2*b]/rad[a+b])))
xs = [r for _, r in data]; ys = [o for o, _ in data]
mx_ = statistics.mean(xs); my = statistics.mean(ys)
cov = sum((x-mx_)*(y-my) for x, y in data)/len(data)
vx = sum((x-mx_)**2 for x in xs)/len(data); vy = sum((y-my)**2 for y in ys)/len(data)
cc = cov/math.sqrt(vx*vy); slope = cov/vx
res = [y-(my+slope*(x-mx_)) for x, y in data]
print('  n=%d  corr(Omega, log(rad(c+b)/rad(c))) = %.6f  斜率 = %.6f' % (len(data), cc, slope), flush=True)
print('  残差标准差 = %.3e  (约 0 则 Omega 完全由 rad 比解释)' % statistics.pstdev(res), flush=True)

print()
print('=== 尺度分层（W2）===', flush=True)
for lo, hi in [(1, 100), (100, 200), (200, 300), (300, 400)]:
    vals = [Om(a, b, True) for a in range(1, hi) for b in range(a, hi-a+1) if lo <= a+b < hi]
    if vals:
        print('  c in [%d,%d): n=%5d  均值=%9.6f  标准差=%9.6f'
              % (lo, hi, len(vals), statistics.mean(vals), statistics.pstdev(vals)), flush=True)
