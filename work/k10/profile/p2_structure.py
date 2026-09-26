#!/usr/bin/env python3
"""P2 第一刀: C62 的结构度量 + 降码操作可行性
(a) |Aut(C)|  (b) p(c) 分布  (c) delete-2-add-1 (⟹61 码) 可行性扫描"""
import itertools
from collections import Counter, defaultdict
n=9; N=512
BALL=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
FULL=(1<<N)-1
def load():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
def analyse(C,tag):
    Cs=set(C); cov=0
    for c in C: cov|=BALL[c]
    print(f"[{tag}] |C|={len(C)} 覆盖={cov==FULL}")
    # (a) 自同构群: 平移+坐标置换 (B_n)
    Bn=set()
    for sh in range(N):
        for perm in [(0,1,2,3,4,5,6,7,8)]:
            pass
    # 简化: 只测平移稳定子 + 与坐标置换的复合(抽样检验): 用码的自同构数
    # 全 B_n 太大(512*362880); 改测: 平移自同构数 + 记录
    tauto=[sh for sh in range(N) if set(x^sh for x in C)==Cs]
    print(f"   平移自同构数 = {len(tauto)} (含 0) ⟹ 平移稳定子阶 {len(tauto)}")
    # 坐标置换自同构: 枚举 9! 太大; 用码的"坐标度数"比对, 只做快速筛选
    degs=[sum(1 for c in C if (c>>i)&1) for i in range(n)]
    print(f"   坐标方向度数 = {degs} (和={sum(degs)})")
    # (b) p(c)
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    p={c:sum(1 for x in range(N) if b[x]==1 and (BALL[c]>>x)&1) for c in C}
    print(f"   p(c) 分布 = {dict(sorted(Counter(p.values()).items()))} | Σp={sum(p.values())}=N1")
    # (c) delete-2-add-1 扫描: 找 {c1,c2} 使 holes ⊆ 某球
    worst=10**9; found=0; ex=None
    for c1,c2 in itertools.combinations(C,2):
        # holes = 仅被 c1,c2 (可含两者) 覆盖的点
        holes=[x for x in range(N) if (BALL[c1]>>x)&1 or (BALL[c2]>>x)&1]
        holes=[x for x in holes if sum(1 for c in (c1,c2) if (BALL[c]>>x)&1)==b[x]]
        if len(holes)>10: continue
        worst=min(worst,len(holes))
        # 是否存在 w 使 holes⊆B1(w)
        ok=None
        for w in range(N):
            if all((BALL[w]>>x)&1 for x in holes): ok=w; break
        if ok is not None:
            found+=1
            if ex is None:
                ex=(format(c1,'09b'),format(c2,'09b'),len(holes),format(ok,'09b'))
    print(f"   **delete-2-add-1 扫描**: 可行的 (c1,c2) 数 = {found} | 最小 |holes| = {worst} (>10 表跳过的忽略)")
    if ex: print(f"      ✗✗ 发现可行例: {ex} ⟹ 将给出 61 码（与 K(9,1)=62 冲突！需复核）")
    else: print(f"      ⟹ 无可行的 2→1 压缩 ✓（与 K(9,1)=62 一致 ✓）")
    return p
for i,c in enumerate(load(),1): analyse(c,f"(9,62)=K 码#{i}")
