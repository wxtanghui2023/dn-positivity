# c380_82_dense_grid.py -- C-3900 Gate backbone: dense systematic grid scan (table-lookup, no random sampling)
#   pattern m (sum 5): F_q(z) = sum_i m_i T_q(2 z_i - 1), q = 1..12 ; minimise max_q F_q over z in [0,1]^k.
#   also: reduced z_i = 0 sub-problems for the binding pattern (2,1,1,1).
import numpy as np, time
from scipy.optimize import minimize
def Tq(q,u): return np.cos(q*np.arccos(np.clip(u,-1,1.0)))
def gz(z,m): return max(sum(m[i]*Tq(q,2.0*z[i]-1.0) for i in range(len(m))) for q in range(1,13))
def Fv(z,m): return np.array([sum(m[i]*Tq(q,2.0*z[i]-1.0) for i in range(len(m))) for q in range(1,13)])
def polish(z,m):
    k=len(m); z=np.asarray(z,float)
    cons=[{'type':'ineq','fun':(lambda Z,q=q: Z[k]-sum(m[i]*Tq(q,2.0*Z[i]-1.0) for i in range(k)))} for q in range(1,13)]
    r=minimize(lambda Z: Z[k], np.concatenate([z,[gz(z,m)]]), method='SLSQP', bounds=[(0.0,1.0)]*k+[(None,None)],
               constraints=cons, options={'maxiter':600,'ftol':1e-15})
    zp=np.clip(r.x[:k],0.0,1.0); return zp, gz(zp,m)

def dense(m, N, pinned=None):
    """pinned: dict {index: value} of coordinates fixed (they stay in the sum but are not searched)"""
    m=list(m); k=len(m); pinned = pinned or {}
    free=[j for j in range(k) if j not in pinned]
    ax=np.linspace(0.0,1.0,N)
    Tab=np.array([[Tq(q,2.0*x-1.0) for q in range(1,13)] for x in ax])   # (N,12)
    base=np.zeros(12)
    for j,pv in pinned.items(): base += m[j]*np.array([Tq(q,2.0*pv-1.0) for q in range(1,13)])
    best=(1e9,None)
    for i1 in range(N):
        g=None
        for qi in range(12):
            acc=np.full((N,)*(len(free)-1), base[qi]+m[free[0]]*Tab[i1,qi])
            for a in range(1,len(free)):
                shp=[1]*(len(free)-1); shp[a-1]=N
                acc=acc+m[free[a]]*Tab[:,qi].reshape(shp)
            g=acc if g is None else np.maximum(g,acc)
        idx=np.unravel_index(int(g.argmin()), g.shape); v=float(g[idx])
        if v<best[0]:
            z=np.empty(k); z[free[0]]=ax[i1]
            for a,j in enumerate(free[1:]): z[j]=ax[idx[a]]
            for j,pv in pinned.items(): z[j]=pv
            best=(v,z)
    return best

print("=== C-3900 Gate: dense systematic grids (fully deterministic) ===",flush=True)
t0=time.time(); out={}
for m,N in [((5,),20001), ((4,1),2001), ((3,2),2001), ((3,1,1),401), ((2,2,1),321), ((2,1,1,1),97), ((1,1,1,1,1),29)]:
    v,z=dense(m,N)
    z2,v2=polish(z,m)
    if v2<v: v,z=v2,z2
    out[tuple(m)]=(v,z)
    act=[q for q in range(1,13) if abs(Fv(z,m)[q-1]-v)<1e-7]
    print("  m=%-14s grid N=%5d (%s pts) : min max_q F_2q = %+.8f | margin = %+.8f | active q=%s | z=%s | %s"
          %(str(list(m)),N,"%.0e"%(N**len(m)),v,v-0.5,act,np.round(z,8),"FEASIBLE" if v<=0.5 else "INFEASIBLE"),flush=True)
    print("      F_2q = %s"%np.round(Fv(z,m),6),flush=True)
print("  elapsed %.0f s"%(time.time()-t0),flush=True)

print("\n=== reduced boundary sub-problems: one coordinate pinned at z = 0 (binding pattern (2,1,1,1)) ===",flush=True)
for pin_idx in range(4):
    for label,pv in (("z=0",0.0),("z=1",1.0)):
        v,z=dense([2,1,1,1],161,{pin_idx:pv})
        z2,v2=polish(z,[2,1,1,1]); z2[pin_idx]=pv; v2=gz(z2,[2,1,1,1])
        if v2<v: v,z=v2,z2
        print("  pin z_%d=%s : min max_q F_2q = %+.8f | margin = %+.8f | z = %s -> %s"
              %(pin_idx,label,v,v-0.5,np.round(z,8),"FEASIBLE" if v<=0.5 else "INFEASIBLE"),flush=True)
print("\n=== gate summary ===",flush=True)
bmin=min(out.items(),key=lambda kv:kv[1][0]) if True else None
for m,(v,z) in sorted(out.items(),key=lambda kv:kv[1][0]):
    print("  pattern %-14s : %+.8f -> %s"%(str(list(m)),v,"FEASIBLE" if v<=0.5 else "INFEASIBLE"),flush=True)
print("  best over all patterns: %s -> %+.8f"%(str(list(bmin[0])),bmin[1][0]),flush=True)
print("  ==> numerical support lower bound : k >= %s"%("5" if all(v>0.5 for v,_ in out.values() if len(v)<=4) else "?"),flush=True)
print("DONE-DENSE",flush=True)
