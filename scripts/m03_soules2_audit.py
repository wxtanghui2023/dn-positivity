#!/usr/bin/env python3
"""M03 E-型审计：Soules-2（Thm.10）在 Lambda_* 上。
保真判别器：Remark 3 的 sum d_i = sum lambda_i。
配置 = (m, k-list, l-list)，{k}∪{l} 划分 {3..n}；i-块 = 1..m（Remark 2）。
"""
from fractions import Fraction as F
import itertools, random

LAMSTAR=[F(1),F(12,25),F(12,25),F(-41,50),F(-41,50)]

def soules2(x, lam, m, klist, llist):
    n=len(x); x=[F(0)]+list(x); S=sum(t**2 for t in x[1:])
    iidx=list(range(1,m+1)); jidx=list(range(m+1,n+1))
    Si=sum(x[a]**2 for a in iidx); Sj=sum(x[a]**2 for a in jidx)
    d=[]
    # i-块
    for p in range(1,m+1):
        t1=x[p]**2*lam[0]/S
        t2=x[p]**2*Sj*lam[1]/(S*Si)
        t3=F(0)
        for t in range(p+1,m+1):
            pre=sum(x[a]**2 for a in iidx[:t-1]); cur=pre+x[iidx[t-1]]**2
            t3+=(x[p]*x[iidx[t-1]])**2*lam[klist[(m-t+1)-1]-1]*pre/cur
        pre_p=sum(x[a]**2 for a in iidx[:p-1]); cur_p=pre_p+x[p]**2
        t4=(pre_p*lam[klist[(m-p+1)-1]-1]/cur_p) if p>=2 else F(0)
        d.append(t1+t2+t3+t4)
    # j-块
    nj=n-m
    for q in range(1,nj+1):
        y=jidx[q-1]; xq=x[y]
        t1=xq**2*lam[0]/S
        t2=xq**2*Si*lam[1]/(S*Sj)
        t3=F(0)
        for t in range(q+1,nj+1):
            pre=sum(x[a]**2 for a in jidx[:t-1]); cur=pre+x[jidx[t-1]]**2
            t3+=(xq*x[jidx[t-1]])**2*lam[llist[(nj-t+1)-1]-1]*pre/cur
        pre_q=sum(x[a]**2 for a in jidx[:q-1]); cur_q=pre_q+xq**2
        t4=(pre_q*lam[llist[(nj-q+1)-1]-1]/cur_q) if q>=2 else F(0)
        d.append(t1+t2+t3+t4)
    return d

def configs(n=5):
    out=[]
    for m in range(1,n):
        rest=[i for i in range(3,n+1)]           # 3..n 的指标
        for ksz in [m-1]:
            for kk in itertools.combinations(rest,ksz):
                ll=tuple(sorted(set(rest)-set(kk)))
                out.append((m,tuple(sorted(kk)),ll))
    return out

print("=== 步骤1：保真判别（Remark 3: Σd_i = Σλ_i）===")
random.seed(11); bad=0; tot=0
for m,kk,ll in configs():
    for _ in range(20):
        lam=sorted([F(random.randint(-60,60),random.randint(1,12)) for _ in range(5)],reverse=True)
        if lam[0]<=0: continue
        x=sorted(F(random.randint(1,30),random.randint(1,10)) for _ in range(5))
        d=soules2(x,lam,m,kk,ll); tot+=1
        if sum(d)!=sum(lam): bad+=1
print(f"  配置×样本 = {tot}; Σd_i=Σλ_i 失败次数 = {bad}  -> {'PASS' if bad==0 else 'FAIL'}")

print("\n=== 步骤2：Λ_* 上搜索（三族，递增，有理）===")
halves=[F(1),F(3,2),F(2),F(5,2),F(3),F(4),F(5),F(6),F(8),F(10),F(12),F(15),F(20),F(25),F(30),F(40),F(50)]
hits=[]; best=None
for m,kk,ll in configs():
    for r in halves:
        for x in [(F(1),r,r,r,r)]:
            d=soules2(x,LAMSTAR,m,kk,ll)
            mn=min(d)
            if best is None or mn>best[0]: best=(mn,x,m,kk,ll,d)
            if mn>=0: hits.append((x,m,kk,ll,d))
    for r in halves:
        for s in halves:
            if s<r: continue
            for x in [(F(1),r,r,s,s)]:
                d=soules2(x,LAMSTAR,m,kk,ll); mn=min(d)
                if best is None or mn>best[0]: best=(mn,x,m,kk,ll,d)
                if mn>=0: hits.append((x,m,kk,ll,d))
    for r in halves:
        for s in halves:
            if s<r: continue
            for x in [(F(1),r,s,s,s)]:
                d=soules2(x,LAMSTAR,m,kk,ll); mn=min(d)
                if best is None or mn>best[0]: best=(mn,x,m,kk,ll,d)
                if mn>=0: hits.append((x,m,kk,ll,d))
print("  命中数:",len(hits))
for h in hits[:6]:
    print("   HIT x=",[str(t) for t in h[0]],"m=",h[1],"k=",h[2],"l=",h[3])
    print("       d=",[str(t) for t in h[4]])
print("  最优(最小 d 的最大者): min_d =",best[0],"=",float(best[0]))
print("     x =",[str(t) for t in best[1]],"m =",best[2],"k =",best[3],"l =",best[4])
print("     d =",[str(t) for t in best[5]])
