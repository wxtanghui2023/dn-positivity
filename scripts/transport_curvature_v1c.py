#!/usr/bin/env python3
"""算术运输曲率 v1（筛法加速版）
状态 S=(a,b,c), a+b=c
A-运输 T_A(a,b,c) = (b, c, b+c)
M-运输 T_M(S)     = u(S)·S, u(S)=rad(c)
曲率 Ω(S) = log[ W(T_M T_A S)·W(S) / ( W(T_A S)·W(T_M S) ) ]
"""
import math, statistics

MAXN = 12000
rad = [1]*(MAXN+1); rad[0] = 0
sieve = bytearray([1])*(MAXN+1)
for p in range(2, MAXN+1):
    if sieve[p]:
        for m in range(p, MAXN+1, p):
            sieve[m] = 0
            rad[m] *= p

def Om(S, scale_sensitive):
    a, b, c = S
    SA = (b, c, b+c)
    SM = (rad[c]*a, rad[c]*b, rad[c]*c)
    SAM = (rad[SA[2]]*SA[0], rad[SA[2]]*SA[1], rad[SA[2]]*SA[2])
    if scale_sensitive:
        W = lambda T: rad[T[0]]*rad[T[1]]*rad[T[2]]
    else:
        W = lambda T: (rad[T[0]]*rad[T[1]]*rad[T[2]])/(T[0]*T[1]*T[2])
    return math.log(W(SAM)*W(S)/(W(SA)*W(SM)))

N = 1200
print('=== v1 曲率扫描（a+b=c, c <= %d）===' % N, flush=True)
for name, ss in [('W1 = rad/(abc) 形状不变', False), ('W2 = rad(abc) 尺度敏感', True)]:
    nz = 0; tot = 0; mx = -1e9; mn = 1e9
    for a in range(1, N):
        for b in range(a, N-a+1):
            tot += 1
            v = Om((a, b, a+b), ss)
            if abs(v) > 1e-12:
                nz += 1
                mx = max(mx, v); mn = min(mn, v)
    print('  %s: 非零 %d/%d = %.6f' % (name, nz, tot, nz/tot)
          + ('  范围[%.6f, %.6f]' % (mn, mx) if nz else '   <= Omega === 0'), flush=True)

print()
print('=== 尺度敏感情形：Omega 是否完全由 rad 比解释 ===', flush=True)
data = []
for a in range(1, 400):
    for b in range(a, 400-a+1):
        S = (a, b, a+b); SA = (b, S[2], S[2]+b)
        data.append((Om(S, True), math.log(rad[SA[2]]/rad[S[2]])))
xs = [r for _, r in data]; ys = [o for o, _ in data]
mx_ = statistics.mean(xs); my = statistics.mean(ys)
cov = sum((x-mx_)*(y-my) for x, y in data)/len(data)
vx = sum((x-mx_)**2 for x in xs)/len(data); vy = sum((y-my)**2 for y in ys)/len(data)
cc = cov/math.sqrt(vx*vy); slope = cov/vx
res = [y-(my+slope*(x-mx_)) for x, y in data]
print('  n=%d  corr(Omega, log(rad(c+b)/rad(c))) = %.6f   斜率 = %.6f' % (len(data), cc, slope), flush=True)
print('  残差标准差 = %.3e   (约 0 则完全由 rad 比解释)' % statistics.pstdev(res), flush=True)

print()
print('=== 尺度分层（W2）===', flush=True)
for lo, hi in [(1, 200), (200, 400), (400, 600), (600, 800), (800, 1000)]:
    vals = [Om((a, b, a+b), True) for a in range(1, hi) for b in range(a, hi-a+1) if lo <= a+b < hi]
    if vals:
        print('  c in [%d,%d): n=%5d  均值=%9.6f  标准差=%9.6f'
              % (lo, hi, len(vals), statistics.mean(vals), statistics.pstdev(vals)), flush=True)

print()
print('=== 非交换端点是否同射线 ===', flush=True)
same = 0; tot2 = 0
for a in range(1, 400):
    for b in range(a, 400-a+1):
        S = (a, b, a+b)
        SA = (b, S[2], S[2]+b)
        SAM = (rad[SA[2]]*SA[0], rad[SA[2]]*SA[1], rad[SA[2]]*SA[2])
        SMA = ((rad[S[2]]*a) + (rad[S[2]]*b), rad[S[2]]*b, rad[S[2]]*c if False else rad[S[2]]*(S[2]+b))
        tot2 += 1
        if SAM[0]*SMA[1] == SMA[0]*SAM[1]:
            same += 1
print('  同射线比例 = %d/%d = %.6f' % (same, tot2, same/tot2), flush=True)
