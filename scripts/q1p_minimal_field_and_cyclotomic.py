## Q1' 第一刀: (a) 压缩到最小包含域 Q=2^{ord_d(2)}; (b) 指数 m=(Q-1)/d; (c) 指数3 -> 经典三次分圆数公式核验
import re
from math import gcd
def ord2(d):
    o=1;x=2%d
    while x!=1: x=x*2%d;o+=1
    return o
rows=[]
for ln in open("out/q1_lane_a.txt"):
    m=re.match(r"n=\s*(\d+) d=\s*(\d+) q=\s*(\d+) sub=(\S+)\s+lA=\s*(\d+) lB=\s*(\d+) rho=([\d.]+)",ln)
    if m: rows.append((int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(5))))
# 去重：同一 d 只在最小包含域算一次
uniq={}
for (n,d,q,lam) in rows:
    uniq.setdefault(d,(2**ord2(d),lam,n))
print("去重后最小包含域案例数:",len(uniq))
from collections import Counter
idx=Counter()
match=0;tot3=0;details=[]
def solve_AB(Q):
    # 4Q = A^2 + 27 B^2, A ≡ 1 mod 3
    best=None
    B=0
    while 27*B*B<=4*Q:
        rem=4*Q-27*B*B
        A=int(rem**0.5)
        for AA in (A-1,A,A+1):
            if AA*AA==rem:
                for cand in (AA,-AA):
                    if cand%3==1 or (cand%3==1%3):
                        if (cand-1)%3==0:
                            best=(cand,B);break
                if best: break
        if best: break
        B+=1
    return best
for d,(Q,lam,n) in sorted(uniq.items()):
    m=(Q-1)//d
    idx[m]+=1
    if m==3:
        tot3+=1
        AB=solve_AB(Q)
        if AB:
            A,B=AB; pred=(Q-8+A)//9
            ok=(pred==lam)
            match+= 1 if ok else 0
            details.append((d,Q,A,B,lam,pred,ok))
print("\n指数 m=(Q-1)/d 分布:",dict(idx))
print("指数3 案例数:",tot3," 经典公式 λ=(Q-8+A)/9 命中:",match)
print("\n指数3 明细 (d, Q, A, B, 实测λ, 预测λ, 命中):")
for z in details: print("   ",z)
# 报告 8/21 案例的最小包含域
for d in (21,):
    Q,lam,n=uniq[d]; print("\n★ d=%d: 最小包含域 Q=2^%d=%d, 指数 m=%d, λ=%d, ρ=%.6f"%(d,ord2(d),Q,(Q-1)//d,lam,lam/d))
