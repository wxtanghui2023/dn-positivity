import random, sys
sys.argv=['x','5','none']
exec(open('exact_pack.py').read().split('def main()')[0])
PRIV={i:[v for v in range(1024) if owners[v]==[i]] for i in range(120)}
def greedy_pack(pts,target,banned=0):
    rem=pts&~banned; got=[]
    while len(got)<target and rem:
        v=(rem&-rem).bit_length()-1; got.append(v)
        t=rem; nxt=0
        while t:
            u=(t&-t).bit_length()-1; t&=t-1
            if (u^v).bit_count()>=3: nxt|=1<<u
        rem=nxt
    return got
random.seed(555)
hits=0
for _ in range(400):
    D=tuple(sorted(random.sample(range(120),4)))
    Xw=[WORDS[i] for i in D]; U=U_of(D)
    if U==0: continue
    pts=[v for v in range(1024) if (U>>v)&1]
    for xi in range(4):
        x=Xw[xi]; wt=D[xi]
        B1x=(1<<x)|sum(1<<(x^(1<<j)) for j in range(10))
        P=greedy_pack(U,3,banned=B1x)
        if len(P)<3: continue
        Cx=[v for v in pts if (B1x>>v)&1]
        Sa=[v for v in Cx if not any((v^p).bit_count()<=2 for p in P)]
        if Sa: continue
        hits+=1
        print(f"##### 存活=0 例 {hits} #####")
        print(f"D={D} 码字={Xw}  |U_D|={len(pts)}  |C_x|={len(Cx)}")
        print(f"  x={x} (下标 {wt})   P={P}   r=d(x,p)={[(x^p).bit_count() for p in P]}")
        # P 的锚（各自锚到哪个字）
        for p in P:
            print(f"    p={p}: 锚到 D 中位置 {[t for t,xx in enumerate(Xw) if (xx^p).bit_count()<=1]}")
        print(f"  x 的私有点={PRIV[wt]}  (在B1(x)内的={[v for v in PRIV[wt] if (B1x>>v)&1]})")
        print(f"  各 p 与 x 私有点的距离: {[[((v^p).bit_count()) for v in PRIV[wt]] for p in P]}")
        # 该 D 的完整 4-packing 存在性
        def pex(ppl,tgt):
            n=len(ppl)
            if n<tgt: return None
            adj=[0]*n
            for i in range(n):
                for j in range(i+1,n):
                    if (ppl[i]^ppl[j]).bit_count()>=3: adj[i]|=1<<j; adj[j]|=1<<i
            def rec(c,need,ch):
                if need==0: return ch
                if c.bit_count()<need: return None
                t=c
                while t:
                    v=(t&-t).bit_length()-1; t&=t-1
                    r=rec(c&adj[v],need-1,ch+[v])
                    if r: return r
                    c&=~(1<<v)
                    if c.bit_count()<need: return None
                return None
            return rec((1<<n)-1,tgt,[])
        pi=pex(pts,4)
        print(f"  该 D 的精确 α₂=4 见证: {[pts[i] for i in pi] if pi else '无'}")
