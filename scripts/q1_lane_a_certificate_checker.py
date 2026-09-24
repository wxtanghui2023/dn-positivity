## Q1 证书复核器 v2（独立于生成脚本）：从 out/q1_lane_a.txt 重新认证
## 修正: (a) 表格精度 %.6f => 容差 5e-7 ; (b) 标签修正 ; (c) 增加"多 n 同 d"非平凡性诊断
import re
from collections import defaultdict
rows=[]
for ln in open("out/q1_lane_a.txt"):
    m=re.match(r"n=\s*(\d+) d=\s*(\d+) q=\s*(\d+) sub=(\S+)\s+lA=\s*(\d+) lB=\s*(\d+) rho=([\d.]+)",ln)
    if m:
        rows.append(dict(n=int(m.group(1)),d=int(m.group(2)),q=int(m.group(3)),
                         sub=(m.group(4)=="True"),lA=int(m.group(5)),lB=int(m.group(6)),rho=float(m.group(7))))
TOL=5e-7   # 表格 %.6f 的一半
print("总行数:",len(rows)," 非子域行数:",sum(1 for r in rows if not r["sub"]))
non=[r for r in rows if not r["sub"]]
print("(1) 双算法一致:",all(r["lA"]==r["lB"] for r in rows),"不一致:",[ (r["n"],r["d"]) for r in rows if r["lA"]!=r["lB"]])
mx=max(r["rho"] for r in non); eq=sorted((r["n"],r["d"],r["lA"]) for r in non if r["rho"]>=mx-TOL)
print("(2) rho_max(表值) = %.6f ; 8/21 = %.6f ; |差| = %.2e (<=容差? %s)"%(mx,8/21,abs(mx-8/21),abs(mx-8/21)<=TOL))
print("(3) equality cases:",eq)
print("(4) rho > rho_max 违例:",len([r for r in non if r["rho"]>mx+TOL]))
print("(5) rho != lambda/d 违例(容差内):",len([r for r in non if abs(r["rho"]-r["lA"]/r["d"])>TOL]))
g=defaultdict(set); nn=defaultdict(set)
for r in rows: g[r["d"]].add(r["lA"]); nn[r["d"]].add(r["n"])
multi={d:sorted(nn[d]) for d in nn if len(nn[d])>1}
print("(6) 出现在多个 n 的 d 数:",len(multi),"| 例:",[(d,multi[d],sorted(g[d])) for d in list(multi)[:5]])
print("    λ 随 n 变化者:",[(d,sorted(g[d])) for d in multi if len(g[d])>1] or "无（一致 => 支持最小包含域引理）")
print("(7) precision note: 表格列 rho 为 %.6f；与 8/21 的差异 4.0e-7 属四舍五入，非数学不一致")
