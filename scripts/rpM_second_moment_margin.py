import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def Q(th, M):
    K=5*M; k=np.arange(1,K+1)[:,None]; C=np.cos(k*th[None,:]); f=C.sum(axis=1)
    return float((f**2).sum())
print(" M | K=5M |  K/4  | min Σf² (对抗) | 比值 | 该配置的 max f")
for M in range(1,12):
    K=5*M; best=None
    for trial in range(60):
        x0=rng.uniform(0,2*np.pi,M)
        r=minimize(Q,x0,args=(M,),method='Nelder-Mead',
                   options={'maxiter':4000,'xatol':1e-10,'fatol':1e-12})
        if best is None or r.fun<best.fun: best=r
    th=best.x; K_=K
    k=np.arange(1,K+1)[:,None]; f=np.cos(k*th[None,:]).sum(axis=1)
    print(f"{M:2d} | {K:4d} | {K/4:5.2f} | {best.fun:14.4f} | {best.fun/(K/4):5.2f} | {f.max():7.4f}")
