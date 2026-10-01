import os,re,json,collections
D='docs'
IDRE=re.compile(r'\b(?:E\d{3}|V\d{3,4}|C-?\d{2,3}|F[1-9]|R\d{2})\b')
# 假设抽取规则（紧签名，避免噪声）
RULES=[
 (re.compile(r'假设[:：]?\s*([^。；\n，]{2,36})'),                        lambda m: '假设:'+m.group(1).strip()[:32]),
 (re.compile(r'若\s*([^。；\n，]{2,24})\s*成立'),                        lambda m: '若'+m.group(1).strip()[:22]+'成立'),
 (re.compile(r'依赖\s*RH|假设\s*RH|在\s*RH\s*下'),                       lambda m: '★依赖RH(空间A专属)'),
 (re.compile(r'\bBÖW\b|Bertolo|全文不可得|拿不到|source unavailable'),   lambda m: '★原文不可得(BÖW类)'),
 (re.compile(r'代理定义|代理对象|proxy'),                                lambda m: '★代理定义'),
 (re.compile(r'单点|仅一次|仅 i=45|只验证了一处'),                        lambda m: '△单点验证'),
 (re.compile(r'Jensen'),                                                lambda m: '△Jensen松弛'),
 (re.compile(r'枚举穷尽|穷尽枚举|全枚举'),                                lambda m: '枚举穷尽性'),
 (re.compile(r'模\s*\(?[A-Z][^)\s]{0,6}\)?|condition\s*\(q\)'),          lambda m: '模条件'),
 (re.compile(r'条件性|conditional on'),                                  lambda m: '条件性'),
 (re.compile(r'数值|实测|测量'),                                          lambda m: '数值实测'),
]
nodes={}
cl=os.path.join(D,'ID-CLAIMS.tsv')
if os.path.exists(cl):
    for i,l in enumerate(open(cl,encoding='utf-8')):
        if i==0: continue
        f=l.rstrip('\n').split('\t')
        if len(f)>=3: nodes[f[0]]={'stream':f[1],'slug':f[2]}
files=[f for f in sorted(os.listdir(D)) if f.endswith('.md')]
mentions=collections.defaultdict(set)
own={}
for fn in files:
    txt=open(os.path.join(D,fn),encoding='utf-8',errors='ignore').read()
    ids=set(IDRE.findall(fn))|set(IDRE.findall(txt))
    for cid in ids: mentions[cid].add(fn)
    # 该文档自身的假设：仅取"含依赖线索之行"（收紧 ✓）
    CUE=re.compile(r'假设|依赖|基于|依据|在.{0,12}下|模\s*\(?[A-Z]|若.{1,20}成立|condition')
    BAD=re.compile(r'[\\$*_^{}`]|["]')
    asum=set()
    for ln in txt.splitlines():
        if not CUE.search(ln): continue
        for rx,f in RULES:
            for m in rx.finditer(ln):
                try:
                    v=f(m)
                    if len(v)<3 or len(v)>36 or BAD.search(v): continue
                    asum.add(v)
                except Exception: pass
    base=fn[:-3].split('-')[0]
    for cid in ids:
        if fn.startswith(cid) and cid not in own:
            own[cid]=sorted(asum)[:8]
for cid in mentions: nodes.setdefault(cid,{'stream':'?','slug':''})
reg=set()
for cid,d in nodes.items(): reg.update(own.get(cid,[]))
json.dump({'axioms':sorted(reg),
           'nodes':[{'id':c,'statement':['atom',(nodes[c]['slug'] or c)[:120]],'assumes':[['atom',a] for a in own.get(c,[])]} for c in nodes]},
          open('/tmp/om-ext/migrate.json','w'),ensure_ascii=False)
print(f"节点 {len(nodes)}｜假设字典 {len(reg)}｜带自身假设之断言 {sum(1 for c in nodes if own.get(c))}")
print("假设字典样例:", sorted(reg)[:12])
