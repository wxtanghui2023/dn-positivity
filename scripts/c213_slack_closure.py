#!/usr/bin/env python3
"""C-213：乙-2 收尾 —— 显式舍入余量（两条独立实现交叉验证）
impl A: 均值形式 + 显式误差 a*δπ/2 + 显式舍入 slack
impl B: mpmath.iv 区间算术（π 用较宽的有理区间）
"""
import mpmath as mp
from fractions import Fraction
mp.mp.dps = 220; mp.iv.prec = 500
K=15; q=10**50
p=[11584425719970138111302019914351820661654470725898,
   33188742342310058637970140459146751137826049502861,
   73557643674102601539804692683823470483211051045378]
PI_STR="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
PI_LO=Fraction(int(PI_STR),10**100); PI_HI=PI_LO+Fraction(1,10**100)
# 为吃掉端点->mpf 转换误差，实际使用更宽区间
WIDEN=Fraction(1,10**150)
LO=PI_LO-WIDEN; HI=PI_HI+WIDEN
print("π 使用区间宽度 = %.2e （原 1e-100，另放宽 2e-150）" % float(HI-LO))

SLACK_PER_TERM = mp.mpf(10)**-130     # 显式逐项舍入余量（保守）
def implA(k):
    lo=mp.mpf(0); hi=mp.mpf(0)
    for pj in p:
        a=Fraction(k*pj,q); am=mp.mpf(a.numerator)/mp.mpf(a.denominator)
        mid=mp.cos(am*mp.mpf(PI_STR)/mp.mpf(10)**100)
        err=am*mp.mpf(float(HI-LO))/2 + SLACK_PER_TERM
        lo+=mid-err; hi+=mid+err
    return lo,hi
def implB(k):
    s=mp.iv.mpf(0)
    for pj in p:
        a=Fraction(k*pj,q)
        lo_hp=mp.mpf(PI_STR)/mp.mpf(10)**100 - mp.mpf(10)**-150
        hi_hp=mp.mpf(PI_STR)/mp.mpf(10)**100 + mp.mpf(10)**-100 + mp.mpf(10)**-150
        arg=mp.iv.mpf(a.numerator)/mp.iv.mpf(a.denominator)*mp.iv.mpf([lo_hp,hi_hp])
        s+=mp.iv.cos(arg)
    return mp.mpf(s.a), mp.mpf(s.b)

print("\n  k   implA U_k(含slack)            implB U_k(区间)                 |A-B|        A_wid      B_wid")
A_u={}; B_u={}
for k in range(1,K+1):
    la,ua=implA(k); lb,ub=implB(k)
    A_u[k]=ua; B_u[k]=ub
    print("  %2d  %-26s %-26s %.2e  %.1e  %.1e" % (k, mp.nstr(ua,22), mp.nstr(ub,22),
          float(abs(ua-ub)), float(ua-la), float(ub-lb)))
print("\n逐项 slack 已含 1e-130/项（3 项 ⟹ ~3e-130）")
UA=max(A_u.values()); UB=max(B_u.values())
print("  U_new^safe(A) = %s  (k=%d)" % (mp.nstr(UA,30), max(A_u,key=A_u.get)))
print("  U_new^safe(B) = %s  (k=%d)" % (mp.nstr(UB,30), max(B_u,key=B_u.get)))
Use=max(UA,UB)
print("\n★ 取两者较大者为最终安全上界：")
print("  U_new^safe = %s" % mp.nstr(Use,34))
TARGET=mp.mpf('0.7640811007458538851475626748')
print("  是否 < 0.7640811007458538851475626748 ?  %s  （裕量 %.3e）" % (Use<TARGET, float(TARGET-Use)))
OLD=mp.mpf('0.76408110090337578')
print("  对照旧认证上界 0.76408110090337578 ⟹ 改进 %.3e" % float(OLD-Use))
print("\n★ 最终账本：0.76 ≤ m_3 ≤ %s" % mp.nstr(Use,34))
open('/tmp/c213_U.txt','w').write(mp.nstr(Use,40))
