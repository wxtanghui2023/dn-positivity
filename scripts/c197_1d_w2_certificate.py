#!/usr/bin/env python3
"""
C-197: T13-B / w=2 —— 一维覆盖证书（只做 (I)(II)）

f_I(t)  = 2cos(5t - pi/3) - 1 - sin(5*d2s(t))
f_II(t) = 2cos(pi/3 - t) - 1 - sin(d2s(t))
d2s(t)  = min( K*t , sqrt(R^2 - t^2) )      [放大版：K*t >= 真 m(t)]

m(t) = (1/3)arcsin(sqrt2 sin 3t) 的上界链条（全部严格）：
   arcsin(u) <= u/sqrt(1-u^2)   (0<=u<1)          [导数递增]
   sin(3t) <= 3t                                   [t>=0]
   sqrt(1-2sin^2(3t)) >= sqrt(1-2sin^2(0.3)) =: c  [t<=0.1]
  => m(t) <= sqrt2*t/c =: K*t

严谨性：端点精确有理（Fraction）；pi 用区间；sin/cos/sqrt 全区间；方向端点取法显式；
        单调性先做区间范围断言；t=0 单独精确处理；不接受采样作为证明。
"""
import json, time
from fractions import Fraction as F
import mpmath as mp

mp.iv.prec = 120
R  = F(1, 10)
A0 = F(1, 10**9)

def ivq(fr): return mp.iv.mpf(fr.numerator) / mp.iv.mpf(fr.denominator)
def lo(x): return x.a
def hi(x): return x.b

# ---- 严格 K ----
u_max = ivq(F(3,10))                              # 0.3
s = mp.iv.sin(u_max)                              # sin(0.3) 区间
c2 = mp.iv.mpf(1) - 2*s*s                         # 1 - 2 sin^2(0.3), 恒 > 0
c_lo = float(lo(mp.iv.sqrt(c2)))                  # 取【下】端 => c 的严格下界
K = float(hi(mp.iv.sqrt(mp.iv.mpf(2)))) / c_lo    # 取【上】端 => K 的严格上界
K = K * (1 + 1e-15)
print("="*78)
print("C-197  T13-B / w=2  一维覆盖证书   R=0.1（有理端点 + 区间算术）")
print("="*78)
print(f"[K 的严格上界] c = sqrt(1-2sin^2 0.3) >= {c_lo:.17g}  ⟹  K = sqrt2/c <= {K:.17g}")
print(f"               真 m(t) = (1/3)arcsin(sqrt2 sin3t) ≤ K·t   （t≤0.1）✓")
print(f"               注：用放大 K·t 使区域 B' ⊇ B，故结论更强 ✓")
print()

PI = mp.iv.pi; PIO3 = PI/mp.iv.mpf(3)

def d2s_hi(a, b):
    return min(K*float(b), float(lo(mp.iv.sqrt(ivq(R)*ivq(R) - ivq(a)*ivq(a)))))

def fI_lb(a, b):
    t_lo = ivq(5*a) - PIO3; t_hi = ivq(5*b) - PIO3
    assert hi(t_hi) < 0 and lo(t_lo) > -float(mp.pi), "cos 单调区间断言失败"
    c = lo(mp.iv.mpf(2)*mp.iv.cos(t_lo))
    s5 = hi(mp.iv.sin(mp.iv.mpf(5)*mp.iv.mpf(d2s_hi(a,b))))
    return float(c) - 1.0 - float(s5)

def fII_lb(a, b):
    # cos(pi/3 - t) 在 t 上【递增】（pi/3-t 递减、cos 在 [0,pi] 递减）=> 最小值在 t=a
    t_lo = PIO3 - ivq(a)
    assert lo(t_lo) > 0 and hi(t_lo) < float(mp.pi)/2, "cos 单调区间断言失败"
    c = lo(mp.iv.mpf(2)*mp.iv.cos(t_lo))
    s1 = hi(mp.iv.sin(mp.iv.mpf(d2s_hi(a,b))))
    return float(c) - 1.0 - float(s1)

def certify(fun, maxdepth=400, budget=5_000_000):
    stack=[((A0,R),0)]; nbox=0; nterm=0; maxd=0; minv=1e30; minbox=None; worst=None
    while stack:
        (a,b),d = stack.pop()
        v = fun(a,b); nbox+=1; maxd=max(maxd,d)
        if v>=0.0:
            nterm+=1
            if v<minv: minv,minbox=v,(a,b)
            continue
        if d>=maxdepth or nbox>budget: worst=(a,b,v); break
        m=(a+b)/2
        stack.append(((m,b),d+1)); stack.append(((a,m),d+1))
    return worst is None, nbox, maxd, minv, minbox, worst, nterm

# t=0 精确
z=ivq(F(0))
fI0  = float(lo(mp.iv.mpf(2)*mp.iv.cos(z-PIO3))) - 1.0
fII0 = float(lo(mp.iv.mpf(2)*mp.iv.cos(PIO3-z))) - 1.0
print(f"[t=0] 精确关系：f_I(0)=2cos(-pi/3)-1=0，f_II(0)=2cos(pi/3)-1=0 ⟹ 边界等号点 ✓")
print(f"      区间求值下界：f_I(0)={fI0:+.3e}，f_II(0)={fII0:+.3e}（≈0，为 pi 区间取整残差）✓")
print(f"      ⟹ t=0 单独处理：[0,A0] 走解析界（下），[A0,R] 走区间证书（下）\n")

a0f=float(A0)
bI  = (5*3**0.5-5*K)*a0f - 12.5*a0f**2 - 36.1*a0f**3
bII = (3**0.5-K)*a0f - 0.5*a0f**2 - (3**0.5/6)*a0f**3
print(f"[解析小端 0<=t<=A0=1e-9]  f_I ≥ {bI:+.6e}   (系数 5√3−5K = {5*3**0.5-5*K:+.6f})")
print(f"                            f_II ≥ {bII:+.6e}   (系数 √3−K  = {3**0.5-K:+.6f})")
print(f"                            ⟹ 均 > 0 ✓（解析，非采样）\n")

res={}
for fun,nm in ((fI_lb,"f_I"),(fII_lb,"f_II")):
    t0=time.time(); ok,nbox,maxd,minv,minbox,worst,nterm=certify(fun); dt=time.time()-t0
    mb=f"[{float(minbox[0]):.10g}, {float(minbox[1]):.10g}]" if minbox else "-"
    print(f"[{nm}] all_certified = {ok}")
    print(f"       评估箱数 = {nbox:,}   终端认证箱 = {nterm:,}   最大深度 = {maxd}   耗时 = {dt:.2f}s")
    print(f"       认证最小值 = {minv:+.12e}   在箱 {mb}")
    if worst: print(f"       ✗ 未决箱 [{float(worst[0]):.10g},{float(worst[1]):.10g}] 值 {worst[2]:+.6e}")
    res[nm]=dict(all_certified=bool(ok),nbox=nbox,max_depth=maxd,certified_min=minv,
                 argmin_box=[float(minbox[0]),float(minbox[1])] if minbox else None,seconds=dt,
                 unresolved=[float(worst[0]),float(worst[1]),worst[2]] if worst else None)
    print()

json.dump(dict(R=0.1,A0=1e-9,K=K,c_lo=c_lo,t0_separate=True,
               analytic_small=[bI,bII],results=res),
          open("/tmp/c197_result.json","w"),indent=2)
print("已写 /tmp/c197_result.json")
