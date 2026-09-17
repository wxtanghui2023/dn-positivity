# P1-alpha: 有限层盲 + 极限显影 的数值判据
# 对象 O_X^4 = ( sum_{p<=X, p=a mod 4} 1/p )_{a=1,3}
# G2(盲): sign(pi(x;4,1)-pi(x;4,3)) 的翻转
# G3(显影): 调和差 D(X)=sum_{p=3(4)}1/p - sum_{p=1(4)}1/p  →  log(4/pi)
import numpy as np, sys
N = 10**7
s = np.ones(N+1, dtype=bool); s[:2] = False
for i in range(2, int(N**0.5)+1):
    if s[i]: s[i*i::i] = False
pr = np.nonzero(s)[0].astype(np.int64)
p1 = pr[pr % 4 == 1]; p3 = pr[pr % 4 == 3]
print(f"N={N}  #primes={len(pr)}  #(1 mod 4)={len(p1)}  #(3 mod 4)={len(p3)}")

# ---- 有限层盲：符号翻转 ----
step = 1000
xs = np.arange(2, N+1, step, dtype=np.int64)
c1 = np.searchsorted(p1, xs, side='right'); c3 = np.searchsorted(p3, xs, side='right')
d = c1 - c3; sg = np.sign(d)
idx = np.nonzero(np.diff(sg))[0]
flips = xs[idx+1]
print(f"[G2 盲] sign(pi(x;4,1)-pi(x;4,3)) 在 x<=1e7 上翻转 {len(flips)} 次")
print("        前 12 次翻转 at x =", flips[:12])
# 有限层"谁领先"的比例
print(f"[G2 盲] 有限层上 3mod4 领先的采样点比例 = {np.mean(d<0):.4f}")

# ---- 极限显影：调和差 ----
h1 = np.cumsum(1.0/p1); h3 = np.cumsum(1.0/p3)
print("[G3 显影] D(X)=sum_(p=3 mod4)1/p - sum_(p=1 mod4)1/p :")
for X in [10**3,10**4,10**5,10**6,10**7]:
    i1 = np.searchsorted(p1, X, side='right')-1
    i3 = np.searchsorted(p3, X, side='right')-1
    D = h3[i3]-h1[i1]
    print(f"         X={X:>9}   D(X)={D:+.6f}")
print(f"         极限预测 log(4/pi) = {np.log(4/np.pi):+.6f}   (相对偏差 {abs((h3[-1]-h1[-1])-np.log(4/np.pi))/np.log(4/np.pi):.2e})")

# ---- 对照：朴素(等权)计数差的"极限"不存在 ----
print(f"[对照] 等权计数差 pi(X;4,3)-pi(X;4,1) 在 X=1e7 时 = {int(c3[-1]-c1[-1])}  (无极限, 随 X 飘)")
