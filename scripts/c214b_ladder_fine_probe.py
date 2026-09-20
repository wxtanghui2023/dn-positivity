import numpy as np, json, time, itertools
K=15
PIF=3.141592653589793
def cosmin(a,b,k):
    if b<a: a,b=b,a
    lo=k*a; hi=k*b
    j0=int(np.ceil(lo/PIF)); j1=int(np.floor(hi/PIF))
    if j1>=j0:
        for j in range(j0,j1+1):
            if j%2!=0: return -1.0
    return float(min(np.cos(k*a), np.cos(k*b)))
def bb(T,maxdepth=90,guard=2_500_000):
    ts=time.time(); boxes=[(0.0,PIF,0.0,PIF,0.0,PIF,0)]; nterm=0; peak=1; surviv=[]
    while boxes:
        x1,x2,y1,y2,z1,z2,dep=boxes.pop()
        lb=max(cosmin(x1,x2,k)+cosmin(y1,y2,k)+cosmin(z1,z2,k) for k in range(1,K+1))
        if lb>=T: nterm+=1; continue
        if dep>=maxdepth: surviv.append(((x1+x2)/2,(y1+y2)/2,(z1+z2)/2,lb,dep)); continue
        w=[x2-x1,y2-y1,z2-z1]; j=int(np.argmax(w))
        if j==0: mid=(x1+x2)/2; boxes.append((x1,mid,y1,y2,z1,z2,dep+1)); boxes.append((mid,x2,y1,y2,z1,z2,dep+1))
        elif j==1: mid=(y1+y2)/2; boxes.append((x1,x2,y1,mid,z1,z2,dep+1)); boxes.append((x1,x2,mid,y2,z1,z2,dep+1))
        else: mid=(z1+z2)/2; boxes.append((x1,x2,y1,y2,z1,mid,dep+1)); boxes.append((x1,x2,y1,y2,mid,z2,dep+1))
        peak=max(peak,len(boxes))
        if len(boxes)>guard: return dict(T=T,ok=False,peak=peak,sec=time.time()-ts,nterm=nterm,surv=surviv,nfront=len(boxes))
    return dict(T=T,ok=True,peak=peak,sec=time.time()-ts,nterm=nterm,surv=surviv,nfront=0)
cl=json.load(open('/tmp/t13aeq_clusters.json'))['clusters']
x0=np.array(cl[0]['x'])
PERMS=list(itertools.permutations(range(3)))
def dS3(a,b): return min(float(np.linalg.norm(np.asarray(a)[list(p)]-np.asarray(b))) for p in PERMS)
print("  T              收敛   终端箱   峰值前沿  耗时s  未决箱  未决箱到 x0/镜像 的最小距离")
for T in (0.764081100,0.7640811005,0.7640811007,0.76408110074,0.76408110075):
    r=bb(T)
    dmin=None
    if r['surv']:
        ds=[]
        for (cx,cy,cz,lb,dep) in r['surv']:
            ds.append(min(dS3([cx,cy,cz],x0), dS3([cx,cy,cz],x0)))
        dmin=min(ds)
    print("  %-16.11f %-5s %8d %8d %7.1f %6d   %s" % (T,r['ok'],r['nterm'],r['peak'],r['sec'],len(r['surv']),
          ("%.3e" % dmin) if dmin is not None else "-"))
    if not r['ok']:
        print("      ⟹ 触前沿护栏（%d 未决）⟹ 这才是真墙的位置" % r['nfront']); break
