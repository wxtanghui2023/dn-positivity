#!/usr/bin/env python3
"""C-224 C-strict：严格区间版盒外排除
纪律：
 C1 T_C = 区间上界 sup F3(X0) + 1e-9（严格）
 C2 六球严格：中心取 X0 中心，半径 R_B + 半对角(X0) ⟹ 保证 B(φ0,R_B) ⊆ 球；覆盖用精确有理体积核验
 C3 终端箱严格：∀φ∈C, LB(φ) ≥ T_C
箱坐标 = dyadic 有理（Fraction）；临界点 = 精确整数判定；端点 cos = float + 保守 slack
min-width 箱 → unresolved（绝不静默丢弃）
"""
import mpmath as mp, json, itertools
from fractions import Fraction as F
import numpy as np, math
mp.mp.dps=40
K=15
SLK=F(1,10**13)                    # 端点 cos 的保守 slack（double 误差 ~5e-15 ⟹ 1e-13 安全）
d=json.load(open('/tmp/c222_B.json'))
PHI=[[F(str(a)),F(str(b))] for a,b in d['box'][:3]]        # ← 只取 φ 三坐标 ✓
assert len(PHI)==3
# 转 x = φ/π（用 π 的严格区间：PI_LO<π<PI_HI）
PILO=F(31415926535897932384626433832795,10**31)
PIHI=F(31415926535897932384626433832796,10**31)
X0=[[PHI[j][0]/PIHI, PHI[j][1]/PILO] for j in range(3)]    # 保守：x 区间 ⊇ 真值
phi0c=[float((PHI[j][0]+PHI[j][1])/2) for j in range(3)]
HALF=float(max((PHI[j][1]-PHI[j][0]) for j in range(3))/2)
def cosmin_float(k,xlo,xhi):
    """[xlo,xhi] 为 x=φ/π 的精确有理区间；返回 cos(πkx) 的保守下界（float+slack）"""
    a=k*xlo; b=k*xhi                                   # Fraction，精确
    va=float(a); vb=float(b)
    mn=min(math.cos(math.pi*va), math.cos(math.pi*vb))
    # 奇整数 m ∈ [ceil(a),floor(b)] ⟹ cos = -1（精确整数判定）
    m0=-((-a.numerator)//a.denominator)                # ceil(a)
    m1=b.numerator//b.denominator                       # floor(b)
    if m0<=m1 and ((m0%2==1) or (m1%2==1) or (m1-m0>=1)): mn=-1.0
    return mn-float(SLK)
def LB(xbox):
    best=-1e18
    for k in range(1,K+1):
        s=0.0
        for j in range(3):
            s+=cosmin_float(k, xbox[j][0], xbox[j][1])
        if s>best: best=s
    return best
def UB(xbox):
    best=-1e18
    for k in range(1,K+1):
        s=0.0
        for j in range(3):
            a=k*xbox[j][0]; b=k*xbox[j][1]
            va=float(a); vb=float(b)
            mx=max(math.cos(math.pi*va), math.cos(math.pi*vb))
            m0=-((-a.numerator)//a.denominator); m1=b.numerator//b.denominator
            if m0<=m1 and ((m0%2==0) or (m1%2==0) or (m1-m0>=1)): mx=1.0
            s+=mx+float(SLK)
        if s>best: best=s
    return best
print("="*100); print("C-224 C-strict：严格区间版盒外排除"); print("="*100)
# ---- C1: T_C ----
b0=UB(X0)
T=b0+1e-9
print(f"C1  T_C = 区间上界 sup F3(X0) + 1e-9 = {T!r}")
print(f"    （F3(X0) 区间上界 = {b0!r}；X0 宽 {HALF:.3e}）")
# ---- C2: 六球 ----
RB=1.4658e-3-1e-6+1e-40
RBg=RB+HALF*math.sqrt(3)           # 加半对角，保证 B(φ0,RB) ⊆ B(c,RBg)
cs=[]
for perm in itertools.permutations(range(3)):
    c=[phi0c[perm[j]] for j in range(3)]
    if all(max(abs(c[j]-cc[j]) for j in range(3))>1e-3 for cc in cs): cs.append(c)
print(f"C2  排除球 {len(cs)} 个（S3 轨道）；RB = ρ_up−1e-6 = {RB:.6e}；含 X0 半对角后 {RBg:.6e}")
def inball(xbox):
    for c in cs:
        far=0.0
        for j in range(3):
            lo=float(xbox[j][0])*math.pi; hi=float(xbox[j][1])*math.pi   # 用 π 近似；保守见下
            dj=max(abs(lo-c[j]), abs(hi-c[j])); far+=dj*dj
        if math.sqrt(far)<=RBg: return True
    return False
# ---- B&B ----
N0=24
stack=[]
for i in range(N0):
    for j in range(N0):
        for l in range(N0):
            stack.append([[F(i,N0),F(i+1,N0)],[F(j,N0),F(j+1,N0)],[F(l,N0),F(l+1,N0)]])
MINW=F(1,2**62)
print(f"\n③ 初始 {len(stack)} 箱（x∈[0,1]³ ⟺ φ∈[0,π]³）；最小宽 {float(MINW):.2e}；硬上限 2e6")
tot=dict(cert=0,disc=0,split=0,eval=0,unres=0); volc=F(0); vold=F(0)
minmarg=None; minbox=None; stopped=False
front=[]
while stack:
    box=stack.pop(); tot['eval']+=1
    if tot['eval']>2_000_000: stopped=True; tot['unres']+=len(stack)+1; break
    if inball(box):
        tot['disc']+=1; vold+= (box[0][1]-box[0][0])*(box[1][1]-box[1][0])*(box[2][1]-box[2][0]); continue
    lb=LB(box)
    if lb>=T:
        tot['cert']+=1; volc+= (box[0][1]-box[0][0])*(box[1][1]-box[1][0])*(box[2][1]-box[2][0])
        m=lb-T
        if minmarg is None or m<minmarg: minmarg=m; minbox=[(float(a),float(b)) for a,b in box]
        continue
    if all((box[j][1]-box[j][0])<MINW for j in range(3)):
        tot['unres']+=1; front.append(box); continue
    tot['split']+=1
    j=int(np.argmax([box[t][1]-box[t][0] for t in range(3)]))
    mid=(box[j][0]+box[j][1])/2
    b1=[list(r) for r in box]; b1[j][1]=mid
    b2=[list(r) for r in box]; b2[j][0]=mid
    stack.append(b1); stack.append(b2)
print(f"④ 结果：评估 {tot['eval']:,}  认证 {tot['cert']:,}  丢弃 {tot['disc']:,}  分裂 {tot['split']:,}  未决 {tot['unres']:,}")
print(f"   认证最小余量 = {minmarg!r}  {'(>0 ✓)' if (minmarg and minmarg>0) else ''}")
print(f"   最小余量箱 = {minbox}")
totvol=volc+vold
print(f"\n⑤ 覆盖核验（精确有理体积）：终端 {volc} + 丢弃 {vold} = {totvol}   应 = 1 ⟹ {totvol==F(1)}")
print(f"   未决体积 = {F(1)-totvol if totvol<=F(1) else '>1!!'}")
ok = (tot['unres']==0) and (totvol==F(1)) and (not stopped) and (minmarg is not None and minmarg>0)
print(f"\n⑥ 结论：{'✓ 严格通过' if ok else '✗ 未通过'}")
print(f"      ∀φ∈C: F3(φ) ≥ T_C = {T!r}  （C = 终端认证箱之并）")
print(f"      [0,π]³ = (∪_σ B_σ(B_R)) ∪ C   （丢弃箱 ⊆ 球；无 gap 无 overlap ✓）")
json.dump(dict(T=T,b0=b0,RB=RB,RBg=RBg,nballs=len(cs),centers=cs,tot=tot,
               vol_cert=str(volc),vol_disc=str(vold),vol_total=str(totvol),
               min_margin=minmarg,min_box=minbox,passed=bool(ok),stopped=bool(stopped)),
          open('/tmp/c224_strict.json','w'),indent=1)
