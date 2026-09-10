#!/usr/bin/env python3
"""t*(w) 扫描：Ξ_w(t) 在 t∈[8,80] 内首次变零的位置
判定："对每个 w>0 是否都存在有限 t*(w)（即 w>0 正性必然破裂）"
"""
import mpmath as mp
mp.mp.dps = 40

def theta(x):
    s = mp.mpf(1)
    for n in range(1, 10):
        s += 2*mp.e**(-mp.pi*n*n*x)
    return s

def Z(w, s):
    w = mp.mpf(w); s = mp.mpc(s)
    out = -1/s + 1/(s-w)
    f = lambda u: (theta(u**(-2))**w - 1) * (u**(-s) + u**(-(w-s))) / u
    return out + mp.quad(f, [0, mp.mpf('1e-3'), mp.mpf('1e-2'),
                             mp.mpf('0.1'), mp.mpf('0.5'), 1])

def Xi(w, t):
    w = mp.mpf(w)
    s = mp.mpc(w/2, t)
    return (s*(s-w)/(2*w) * Z(w, s)).real

print('=== t*(w) 扫描（t ∈ [8,80]）===', flush=True)
TMAX = mp.mpf(80); STEP = mp.mpf('0.5')
results = {}
for w in ['0.01','0.02','0.03','0.04','0.05','0.0585']:
    wf = mp.mpf(w)
    t = mp.mpf(8); prev_t = t; prev_v = Xi(wf, t)
    found = None
    while t <= TMAX:
        v = Xi(wf, t)
        if v < 0:
            lo, hi = prev_t, t
            for _ in range(40):
                mid = (lo+hi)/2
                if Xi(wf, mid) < 0: hi = mid
                else: lo = mid
            found = (lo+hi)/2
            break
        prev_t, prev_v = t, v
        t += STEP
    results[w] = found
    if found is None:
        print(f'  w={w}: t≤80 内【未见变零】——末值 Ξ(80)={mp.nstr(Xi(wf,TMAX),6)}', flush=True)
    else:
        print(f'  w={w}: t* = {mp.nstr(found,8)}（Ξ(t*){mp.nstr(Xi(wf,found),4)}）', flush=True)

print()
print('=== 汇总 ===')
for w, f in results.items():
    print(f'  w={w}: t* = {"None(>80)" if f is None else mp.nstr(f,8)}')
