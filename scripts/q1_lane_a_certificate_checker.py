## Q1 证书复核器（独立于生成脚本）：从 out/q1_lane_a.txt 重新认证 max / equality / d-不变性
import re,sys
rows=[]
for ln in open("out/q1_lane_a.txt"):
    m=re.match(r"n=\s*(\d+) d=\s*(\d+) q=\s*(\d+) sub=(\S+)\s+lA=\s*(\d+) lB=\s*(\d+) rho=([\d.]+)",ln)
    if m:
        n,d,q,sub,lA,lB=map(int,m.group(1,2,3)),None,None
        rows.append((int(m.group(1)),int(m.group(2)),int(m.group(3)),m.group(4)=="True",int(m.group(5)),int(m.group(6)),float(m.group(7))))
non=[r for r in rows if not r[3]]
print("总行数:",len(rows)," 非子域行数:",len(non))
print("(1) 双算法一致:",all(r[4]==r[5] for r in rows),"  不一致行:",[r[:3] for r in rows if r[4]!=r[5]])
mx=max(r[6] for r in non); eq=[(r[0],r[1],r[4]) for r in non if abs(r[6]-mx)<1e-12]
print("(2) rho_max = %.10f ; 8/21 = %.10f ; 相等? %s"%(mx,8/21,abs(mx-8/21)<1e-12))
print("(3) equality cases:",eq)
# ρ ≤ ρ_max 全域检查
viol=[r[:3] for r in non if r[6]>mx+1e-15]
print("(4) rho > rho_max 的违例数:",len(viol))
# 数值一致性 ρ = λ/d
badr=[r[:3] for r in non if abs(r[6]-r[4]/r[1])>1e-12]
print("(5) rho != lambda/d 违例:",len(badr))
# d-不变性（最小包含域引理的经验确认）
from collections import defaultdict
g=defaultdict(set)
for r in rows: g[r[1]].add(r[4])
multi={d:v for d,v in g.items() if len(v)>1}
print("(6) 同一 d 出现多个 n 的情形数:",len(multi))
bad=[(d,v) for d,v in multi.items() if len(v)>1]
print("    lambda 随 n 变化者:",bad if bad else "无（全部一致 => 与最小包含域引理一致）")
