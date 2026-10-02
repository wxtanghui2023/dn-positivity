#!/usr/bin/env python3
"""命题检验 P-001: 「两区块共享恰 2 元素时作 2-switch，保持对(pair)多重集不变」
—— 在最小非平凡实例上穷举所有 2-switch，比较变换前后 (pairs(b1)+pairs(b2)) 多重集。
"""
import itertools
from collections import Counter
def prs(b): return Counter(itertools.combinations(sorted(b),2))
b1=(0,1,2,3,4,5); b2=(0,1,6,7,8,9)
inter=set(b1)&set(b2); assert len(inter)==2, inter
ri=[x for x in b1 if x not in inter]; rj=[x for x in b2 if x not in inter]
base=prs(b1)+prs(b2); total=0; changed=0; wit=None
for ab in itertools.combinations(ri,2):
    for cd in itertools.combinations(rj,2):
        ni=tuple(sorted(set(b1)-set(ab)|set(cd))); nj=tuple(sorted(set(b2)-set(cd)|set(ab)))
        new=prs(ni)+prs(nj); total+=1
        if new!=base:
            changed+=1
            if wit is None:
                gained=[p for p in (new-base).elements()]
                lost=[p for p in (base-new).elements()]
                wit=(ab,cd,ni,nj,gained,lost)
print(f"[P-001] 实例 b1={b1} b2={b2}（共享 {sorted(inter)}）")
print(f"        穷举 2-switch 总数 = {total}；**改变对多重集的 = {changed}**（若不保则应=0）")
print(f"        反例: 交换 {wit[0]} <-> {wit[1]}")
print(f"              b1'={wit[2]}  b2'={wit[3]}")
print(f"              新增对={wit[4]}  丢失对={wit[5]}")
print(f"        ⟹ 命题 P-001 判定 = **REFUTED** ✗（2-switch 并不保持 λ）")
