#!/usr/bin/env python3
"""CLAIM-GRAPH v0：由既有档案生成断言图 + 四项自动审计。
仅读，不写档案；输出 out/claim-graph.{json,mmd} 与 out/CLAIM-GRAPH-REPORT.md
"""
import os,re,json,collections,sys
DOCS='docs'; OUT='out'
os.makedirs(OUT,exist_ok=True)
IDRE=re.compile(r'\b(?:E\d{3}|V\d{3,4}|C-?\d{2,3}|F[1-9]|R\d{2})\b')
ASSUM=re.compile(r'假设|条件下|模\s*\(?[A-Z]|若\s*[^。]{0,20}成立|conditional|under\s+the\s+assumption')
PROVEN=re.compile(r'✓✓|已验证|已证|成立\s*✓|proven|verified')
DEAD=re.compile(r'\bDEAD\b|已封|NO-?GO|作废|撤回|已死|✗✗')
CONJ=re.compile(r'猜想|conjectur|推测|尚未证')
REFUTE=re.compile(r'反驳|否证|推翻|与.{0,6}矛盾|反例|refut')
nodes={};edges=[]
# 1) 节点：ID-CLAIMS.tsv（主索引）
p=os.path.join(DOCS,'ID-CLAIMS.tsv')
if os.path.exists(p):
    for i,l in enumerate(open(p,encoding='utf-8')):
        if i==0: continue
        f=l.rstrip('\n').split('\t')
        if len(f)>=3: nodes[f[0]]={'id':f[0],'stream':f[1],'slug':f[2],'doc':None,'status':'unknown','assumptions':[],'evidence':{'kind':'index','source':'ID-CLAIMS.tsv'}}
# 2) alias 边
p=os.path.join(DOCS,'ID-ALIASES.tsv')
if os.path.exists(p):
    for i,l in enumerate(open(p,encoding='utf-8')):
        if i==0: continue
        f=l.rstrip('\n').split('\t')
        if len(f)>=3:
            nodes.setdefault(f[0],{'id':f[0],'stream':'al','slug':'','doc':None,'status':'alias','assumptions':[],'evidence':{'kind':'alias','source':'ID-ALIASES.tsv'}})
            m=re.search(r'([A-Z]\d{2,4}|C-?\d{2,3}|F[1-9])',f[2])
            if m: edges.append((f[0],m.group(1),'supersedes'))
# 3) 扫文档：状态/假设/引用边
files=[f for f in sorted(os.listdir(DOCS)) if f.endswith('.md')]
for fn in files:
    txt=open(os.path.join(DOCS,fn),encoding='utf-8',errors='ignore').read()
    ids=set(IDRE.findall(fn))|set(IDRE.findall(txt))
    for cid in ids:
        nodes.setdefault(cid,{'id':cid,'stream':'?','slug':'','doc':None,'status':'unknown','assumptions':[],'evidence':{'kind':'mention','source':fn}})
    # 状态与假设（按文档级判定，便于 v0）
    st='unknown'
    if DEAD.search(txt[:4000]): st='DEAD'
    elif PROVEN.search(txt): st='proven'
    elif CONJ.search(txt): st='conjectured'
    asum=sorted(set(m.group(0)[:40] for m in ASSUM.finditer(txt)))[:5]
    for cid in ids:
        n=nodes[cid]
        if n['status']=='unknown' and st!='unknown': n['status']=st
        if asum and not n['assumptions']: n['assumptions']=asum
        if n['doc'] is None and fn.startswith(cid): n['doc']=os.path.join(DOCS,fn)
    # 边：仅同句 + 定向线索（v1：收紧 ✗粗共现）
    cue_dep=re.compile(r'据|由\s*[A-Z]|基于|依据|依赖|用到|引用|推出|导出|⟹|=>|得出')
    cue_ref=re.compile(r'反驳|否证|推翻|反例|矛盾|作废|撤回|DEAD|NO-?GO')
    for ln in txt.splitlines():
        ids_l=IDRE.findall(ln)
        if len(ids_l)<2: continue
        uniq=[]
        for x in ids_l:
            if x not in uniq: uniq.append(x)
        if len(uniq)<2: continue
        t='refutes' if cue_ref.search(ln) else ('derives' if cue_dep.search(ln) else 'references')
        if t=='references': continue          # v1：仅保留有线索之边
        for i in range(len(uniq)-1):
            edges.append((uniq[i],uniq[i+1],t))
# 4) 去重
edges=list(set(edges))
# 5) 审计
ins=collections.Counter();outs=collections.Counter();adj=collections.defaultdict(list)
refutes=set()
for a,b,t in edges:
    outs[a]+=1; ins[b]+=1; adj[a].append((b,t))
    if t=='refutes': refutes.add((a,b))
# A 循环：Tarjan 简化（只找 size>1 的 SCC）
idx={};low={};st=[];on=set();sccs=[];cnt=[0]
def strong(v):
    idx[v]=low[v]=cnt[0];cnt[0]+=1;st.append(v);on.add(v)
    for w,_ in adj.get(v,[]):
        if w not in idx: strong(w);low[v]=min(low[v],low[w])
        elif w in on: low[v]=min(low[v],idx[w])
    if low[v]==idx[v]:
        c=[]
        while True:
            w=st.pop();on.discard(w);c.append(w)
            if w==v: break
        if len(c)>1: sccs.append(c)
sys.setrecursionlimit(10000)
for v in list(nodes): 
    if v not in idx: strong(v)
# B 悬空：被引用且无出边且非 proven/axiom
# 支撑入边（仅 derives；refutes/references 不计）
sup_in=collections.Counter(); sup_out=collections.Counter()
for a,b,t in edges:
    if t=='derives': sup_in[b]+=1; sup_out[a]+=1
dangling=[n for n,d in nodes.items() if sup_in[n]>0 and sup_out[n]==0 and d['status'] not in ('proven','axiom','DEAD','NO-GO','alias')]
# C 未声明假设：有假设但状态 proven（即含条件却被当无条件）
_spec=lambda a:sum(1 for x in a if len(x)>2 and x not in ('假设','条件下','conditional'))
suspect=sorted([n for n,d in nodes.items() if d['assumptions'] and d['status']=='proven'],key=lambda n:-_spec(nodes[n]['assumptions']))
report=[f"# CLAIM-GRAPH 报告（自动生成，仅读）\n",
 f"节点 {len(nodes)}｜边 {len(edges)}｜docs {len(files)}\n",
 f"## A 循环支撑候选（SCC>1）：{len(sccs)} 组"]
for c in sccs[:15]: report.append("  - "+", ".join(sorted(c)[:12]))
report.append(f"\n## B 悬空断言（被 derives 支撑引用、但自身无出边支撑、且非已证/非死路）：{len(dangling)}")
for n in sorted(dangling,key=lambda x:-sup_in[x])[:15]: report.append(f"  - {n}（支撑引用 {sup_in[n]} 次，status={nodes[n]['status']}）")
report.append(f"\n## C 未声明/条件性假设风险（含假设词却被标 proven）：{len(suspect)}")
for n in suspect[:15]: report.append(f"  - {n}：假设={nodes[n]['assumptions']}")
report.append(f"\n## D 反驳边数（不得计入支撑）：{len(refutes)}")
open(os.path.join(OUT,'CLAIM-GRAPH-REPORT.md'),'w').write("\n".join(report))
json.dump({'nodes':nodes,'edges':edges,'sccs':sccs,'dangling':dangling,'suspect':suspect},open(os.path.join(OUT,'claim-graph.json'),'w'),ensure_ascii=False,indent=1)
# mermaid：只画度数高者，避免爆图
top=sorted(nodes,key=lambda n:-(ins[n]+outs[n]))[:60]
lines=["graph LR"]
for n in top:
    lab=f"{n}({nodes[n]['status'][:4]})"
    lines.append(f'  {n.replace("-","_")}["{lab}"]')
for a,b,t in edges:
    if a in top and b in top:
        ar = "-->" if t=='derives' else ("-.->" if t=='references' else "-.x")
        lines.append(f'  {a.replace("-","_")} {ar} {b.replace("-","_")}')
open(os.path.join(OUT,'claim-graph.mmd'),'w').write("\n".join(lines[:400]))
print("\n".join(report[:60]))
print(f"\n[写出] out/claim-graph.json, out/claim-graph.mmd, out/CLAIM-GRAPH-REPORT.md")
