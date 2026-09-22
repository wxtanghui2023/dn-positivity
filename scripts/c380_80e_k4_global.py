# c380_80e_k4_global.py -- C-3900 Gate: THOROUGH global minimisation for the binding stratum k=4, pattern (2,1,1,1)
# plus the other <=4 patterns, over the CLOSED domain z in [0,1]^k.
# F_{2q}(z) = sum_i m_i T_q(2 z_i - 1) ; feasible iff min max_q F_2q <= 0.5.
# strategy: (1) 400k Latin-hypercube + boundary-biased random samples (vectorised), (2) polish top 3000,
#           (3) DE with 6 seeds, (4) explicit boundary sub-cases (one or two z_i pinned to 0 or 1).
import numpy as np, time, itertools, sys
from scipy.optimize import minimize, differential_evolution
def Tq(q,u): return np.cos(q*np.arccos(np.clip(u,-1,1)))
def gv(Z,m):
    out=np.full(Z.shape[1],-1e9)
    for q in range(1,13):
        v=np.zeros(Z.shape[1])
        for i,mi in enumerate(m): v+=mi*Tq(q,2.0*Z[i]-1.0)
        out=np.maximum(out,v)
    return out
def g(z,m): return float(gv(np.asarray(z,float).reshape(-1,1),m)[0])
def polish(z,m):
    k=len(m); z=np.asarray(z,float)
    cons=[{'type':'ineq','fun':(lambda Z,q=q: Z[k]-sum(m[i]*Tq(q,2.0*Z[i]-1.0) for i in range(k)))} for q in range(1,13)]
    try:
        r=minimize(lambda Z: Z[k], np.concatenate([z,[g(z,m)]]), method='SLSQP', bounds=[(0.0,1.0)]*k+[(None,None)],
                   constraints=cons, options={'maxiter':400,'ftol':1e-14})
    except Exception:
        return z, g(z,m)
    zp=np.clip(r.x[:k],0.0,1.0); return zp, g(zp,m)

def thorough(m, seed=0, n_rand=400000, n_polish=3000, de_seeds=6, tag=""):
    k=len(m); rng=np.random.default_rng(seed)
    t0=time.time(); best=(1e9,None)
    # (1) samples: 60% LHS-uniform, 40% boundary-biased (coordinates pushed to 0/1)
    U=np.column_stack([rng.permutation(n_rand) for _ in range(k)])/n_rand
    U+= rng.uniform(0,1/n_rand,size=U.shape)
    B=rng.uniform(0,1,size=(n_rand//2,k))
    mask=rng.random(size=B.shape)<0.35
    B=np.where(mask, np.where(rng.random(size=B.shape)<0.5,0.0,1.0), B)
    S=np.vstack([U,B]).T
    v=gv(S,m); order=np.argsort(v)[:n_polish]
    for j in order:
        zp,vv=polish(S[:,j],m)
        if vv<best[0]: best=(vv,zp)
    print("  [%s] sampling+polish : %+.6f at z=%s (%.0fs, %d samples, %d polished)"
          %(tag,best[0],np.round(best[1],8),time.time()-t0,S.shape[1],n_polish),flush=True)
    # (2) DE with several seeds
    for s in range(de_seeds):
        de=differential_evolution(lambda z: g(z,m),[(0,1)]*k,maxiter=2500,tol=1e-13,popsize=45,
                                  seed=seed+100+s,polish=False,init='sobol',mutation=(0.3,1.1),recombination=0.9)
        zp,vv=polish(de.x,m)
        if vv<best[0]:
            best=(vv,zp)
            print("  [%s] DE seed %d improved -> %+.6f at z=%s (%.0fs)"%(tag,s,best[0],np.round(best[1],8),time.time()-t0),flush=True)
    # (3) explicit boundary sub-cases: pin one coordinate to 0 or 1, optimise the rest
    for i in range(k):
        for pin in (0.0,1.0):
            free=[j for j in range(k) if j!=i]
            sub=[m[j] for j in free]
            def gg(w):
                z=np.empty(k); z[i]=pin
                for a,j in enumerate(free): z[j]=w[a]
                return g(z,m)
            de=differential_evolution(gg,[(0,1)]*(k-1),maxiter=1500,tol=1e-13,popsize=40,seed=seed+200+i,
                                      polish=True,init='sobol')
            z=np.empty(k); z[i]=pin
            for a,j in enumerate(free): z[j]=de.x[a]
            z,vv=polish(z,m)
            if vv<best[0]:
                best=(vv,z)
                print("  [%s] boundary z_%d=%g improved -> %+.6f at z=%s (%.0fs)"%(tag,i,pin,best[0],np.round(best[1],8),time.time()-t0),flush=True)
    return best

print("=== C-3900 Gate: thorough global search over the <=4 strata (closed domain) ===",flush=True)
print("  binding pattern is (2,1,1,1) [k=4]; others are cheaper",flush=True)
out={}
for m,tag in [((2,1,1,1),"k=4 (2,1,1,1)"), ((1,2,2),"k=3 (1,2,2)"), ((1,1,3),"k=3 (1,1,3)"),
              ((2,3),"k=2 (2,3)"), ((1,4),"k=2 (1,4)"), ((5,),"k=1 (5)")]:
    v,z=thorough(list(m), seed=len(m)*17+sum(m), tag=tag,
                 n_rand=400000 if len(m)==4 else 120000,
                 n_polish=3000 if len(m)==4 else 800,
                 de_seeds=6 if len(m)==4 else 3)
    out[tuple(m)]=(v,z)
    print("  ==> %s : min max_q F_2q = %+.8f | margin = %+.8f | z = %s -> %s"
          %(tag,v,v-0.5,np.round(z,8),"FEASIBLE" if v<=0.5 else "INFEASIBLE"),flush=True)
bl=min(out.values(),key=lambda t:t[0])
print("\n=== GATE SUMMARY ===",flush=True)
for m,(v,z) in sorted(out.items(),key=lambda kv:kv[0]):
    print("  pattern %s : %+.8f -> %s"%(list(m),v,"FEASIBLE" if v<=0.5 else "INFEASIBLE"),flush=True)
print("  best over all <=4 strata: %+.8f at z=%s"%(bl[0],np.round(bl[1],8)),flush=True)
print("  ==> support lower bound (numerical): k >= %s"%("5" if bl[0]>0.5 else "4"),flush=True)
print("DONE-K4-GLOBAL",flush=True)
