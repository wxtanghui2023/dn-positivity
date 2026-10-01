#!/usr/bin/env python3
"""清洗并定标假设字典 -> docs/ASSUMPTIONS-LEXICON.tsv（词表）+ docs/ASSUMPTIONS.tsv（断言->假设 登记册）
登记册为机器可读之唯一真源；迁移脚本优先读它，不再靠正则猜。
"""
import os,re,json,collections
D='docs'
# 读上一步迁移产出的字典与归属
mig=json.load(open('/tmp/om-ext/migrate.json'))
raw=mig['axioms']
BAD=re.compile(r'[✓✗）()｜|「」【】]|⇒|⟹|\\\\|\$|\*|_|\^|\{|\}|`|"|\'')
GENERIC={'数值实测','条件性','模条件','枚举穷尽性','若局部化不成立','若该局部界成立'}
def clean(s):
    s=s.strip()
    s=re.sub(r'^假设[:：]\s*','',s).strip()
    s=re.sub(r'[\s。；，]+$','',s)
    return s
lex={}
for r in raw:
    c=clean(r)
    if len(c)<3 or len(c)>40 or BAD.search(c): lex[r]=('garbage',None); continue
    if c in GENERIC: lex[r]=('generic',c); continue
    cls='assumption'
    if c.startswith('★') or c.startswith('△'): cls='marked'
    lex[r]=(cls,c)
keep={r:v[1] for r,v in lex.items() if v[0] in ('assumption','marked','generic')}
os.makedirs(D,exist_ok=True)
with open(os.path.join(D,'ASSUMPTIONS-LEXICON.tsv'),'w') as f:
    f.write("raw\tclass\tcanonical\n")
    for r,(cls,c) in sorted(lex.items(),key=lambda x:(x[1][0],str(x[1][1]))):
        f.write(f"{r}\t{cls}\t{c or ''}\n")
# 断言 -> 假设（用清洗后标签）
rows=[]
for n in mig['nodes']:
    labs=[]
    for a in n.get('assumes',[]):
        raw_s=a[1]
        if raw_s in keep: labs.append(keep[raw_s])
    if labs: rows.append((n['id'],sorted(set(labs))))
with open(os.path.join(D,'ASSUMPTIONS.tsv'),'w') as f:
    f.write("id\tassumes\n")
    for i,l in sorted(rows): f.write(f"{i}\t{';'.join(l)}\n")
cnt=collections.Counter(v[0] for v in lex.values())
rep=collections.Counter()
for _,l in rows: rep.update(l)
print(f"字典 {len(raw)} 条 -> 保留 {len(keep)}：{dict(cnt)}")
print(f"登记册 {len(rows)} 条断言；标签频次 Top10：{rep.most_common(10)}")
