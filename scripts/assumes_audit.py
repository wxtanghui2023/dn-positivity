#!/usr/bin/env python3
"""假设登记审计：覆盖率 + top-N 待补清单（按被引用次数）+ 写入即登记模板检查。
读：docs/ID-CLAIMS.tsv、docs/ASSUMPTIONS.tsv、out/claim-graph.json（或现扫文档）
写：docs/ASSUMES-BACKLOG.md
"""
import os,re,json,collections
D='docs'
ids=[]
p=os.path.join(D,'ID-CLAIMS.tsv')
for i,l in enumerate(open(p,encoding='utf-8')):
    if i==0: continue
    f=l.rstrip('\n').split('\t')
    if f and f[0]: ids.append(f[0])
reg={}
p2=os.path.join(D,'ASSUMPTIONS.tsv')
if os.path.exists(p2):
    for i,l in enumerate(open(p2,encoding='utf-8')):
        if i==0: continue
        f=l.rstrip('\n').split('\t')
        if len(f)>=3: reg[f[0]]=(f[1],f[2])
# 引用计数：优先用图缓存
ins=collections.Counter()
g=os.path.join('out','claim-graph.json')
if os.path.exists(g):
    d=json.load(open(g))
    for a,b,t in d.get('edges',[]): ins[b]+=1
else:
    IDRE=re.compile(r'\b(?:E\d{3}|V\d{3,4}|C-?\d{2,3}|F[1-9]|R\d{2})\b')
    for fn in os.listdir(D):
        if not fn.endswith('.md'): continue
        txt=open(os.path.join(D,fn),encoding='utf-8',errors='ignore').read()
        for cid in set(IDRE.findall(txt)): ins[cid]+=1
human={k:v for k,v in reg.items() if v[1]=='人工定标'}
todo=sorted([i for i in ids if i not in human],key=lambda x:-ins[x])[:50]
lines=["结论: 已查地图：命中 1 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案","D0: 本档对象 = 工具产物（待补假设清单）；非数学命题，不主张任何新值","D1: 0","",
 "# ASSUMES-BACKLOG — 待补假设登记清单（按被引用次数排序）","",
 f"- 登记册总数：{len(reg)}；其中**人工定标 {len(human)}**；ID-CLAIMS 断言 {len(ids)}",
 f"- 覆盖率（人工定标/ID-CLAIMS）：**{len(human)}/{len(ids)} = {100*len(human)/max(1,len(ids)):.1f}%**","",
 "| # | 断言 | 被引用次数 | 现有登记 | 状态 |","|---|---|---|---|---|"]
for k,cid in enumerate(todo,1):
    a=reg.get(cid)
    lines.append(f"| {k} | `{cid}` | {ins[cid]} | {(a[0][:34]+'…') if a else '—'} | {a[1] if a else '**未登记**'} |")
lines+=["","## 写入即登记（新断言模板）","","```markdown",
 "### <断言 id> — <一句话陈述>",
 "ASSUMES: <标签1> | <标签2>        # ★=不可得/未证/代理  △=单点验证",
 "DERIVES-FROM: <前提断言 id> ...   # 已立结论须走此列，不得进 ASSUMES",
 "```","",
 "**纪律**：未列入 ASSUMPTIONS.tsv 的假设不得使用（引擎 fail-closed）；`provenance` 非“人工定标”者视为待清洗。"]
open(os.path.join(D,'ASSUMES-BACKLOG.md'),'w').write("\n".join(lines)+"\n")
print(f"人工定标 {len(human)}／ID-CLAIMS {len(ids)} = {100*len(human)/max(1,len(ids)):.1f}%")
print("top-12 待补：")
for cid in todo[:12]: print(f"  {cid}  被引 {ins[cid]} 次  {'未登记' if cid not in reg else reg[cid][1]}")
