#!/usr/bin/env python3
"""找出 Thm.10 的忠实实现约定：以 Remark 3 (Σd_i=Σλ_i) 为判别器，扫描约定组合。"""
from fractions import Fraction as F
import itertools, random

def build(x, lam, m, kk, ll, ord_k, ord_l, idx_k, idx_l):
    n=len(x); xs=[F(0)]+list(x); S=sum(t**2 for t in xs[1:])
    iidx=list(range(1,m+1)); jidx=list(range(m+1,n+1))
    Si=sum(xs[a]**2 for a in iidx); Sj=sum(xs[a]**2 for a in jidx)
    K=list(kk[::-1]) if ord_k=='desc' else list(kk)
    L=list(ll[::-1]) if ord_l=='desc' else list(ll)
    nk=len(K); nl=len(L)
    def lamK(t):            # t = 1..nk
        return lam[K[t-1]-1] if idx_k=='t' else lam[K[nk-t+1-1]-1]
    def lamL(t):
        return lam[L[t-1]-1] if idx_l=='t' else lam[L[nl-t+1-1]-1]
    d=[]
    for p in range(1,m+1):
        t1=xs[p]**2*lam[0]/S; t2=xs[p]**2*Sj*lam[1]/(S*Si); t3=F(0)
        for t in range(p+1,m+1):
            pre=sum(xs[a]**2 for a in iidx[:t-1]); cur=pre+xs[iidx[t-1]]**2
            t3+=(xs[p]*xs[iidx[t-1]])**2*lamK(m-t+1)*pre/cur
        pre_p=sum(xs[a]**2 for a in iidx[:p-1]); cur_p=pre_p+xs[p]**2
        t4=(pre_p*lamK(m-p+1)/cur_p) if p>=2 and 1<=m-p+1<=nk else F(0)
        d.append(t1+t2+t3+t4)
    nj=n-m
    for q in range(1,nj+1):
        y=jidx[q-1]; xq=xs[y]
        t1=xq**2*lam[0]/S; t2=xq**2*Si*lam[1]/(S*Sj); t3=F(0)
        for t in range(q+1,nj+1):
            pre=sum(xs[a]**2 for a in jidx[:t-1]); cur=pre+xs[jidx[t-1]]**2
            t3+=(xq*xs[jidx[t-1]])**2*lamL(nj-t+1)*pre/cur
        pre_q=sum(xs[a]**2 for a in jidx[:q-1]); cur_q=pre_q+xq**2
        t4=(pre_q*lamL(nj-q+1)/cur_q) if q>=2 and 1<=nj-q+1<=nl else F(0)
        d.append(t1+t2+t3+t4)
    return d

def configs(n=5):
    out=[]
    for m in range(1,n):
        rest=list(range(3,n+1))
        for kk in itertools.combinations(rest,m-1):
            ll=tuple(sorted(set(rest)-set(kk))); out.append((m,tuple(sorted(kk)),ll))
    return out

random.seed(5)
samples=[]
for _ in range(6):
    lam=sorted([F(random.randint(-60,60),random.randint(1,12)) for _ in range(5)],reverse=True)
    if lam[0]<=0: continue
    x=sorted(F(random.randint(1,30),random.randint(1,10)) for _ in range(5))
    samples.append((x,lam))
print("样本数:",len(samples))
best=[]
for ok in ('asc','desc'):
    for ol in ('asc','desc'):
        for ik in ('t','m-t+1'):
            for il in ('t','nj-q+1'):
                tot=0; bad=0
                for x,lam in samples:
                    for m,kk,ll in configs():
                        tot+=1
                        try:
                            d=build(x,lam,m,kk,ll,ok,ol,ik,il)
                        except Exception:
                            bad+=1; continue
                        if sum(d)!=sum(lam): bad+=1
                best.append((bad,tot,ok,ol,ik,il))
best.sort()
for b in best[:8]:
    print("bad=%d/%d  ord_k=%s ord_l=%s idx_k=%s idx_l=%s"%b)
