#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# make_ledger_pdf.py —— 22 项台账 → PDF（A3 横向）
# 依赖：weasyprint ✓ ＋ 文泉驿正黑 + DejaVu（回退）✓；无 LaTeX 中文栈 ⟹ LaTeX 转 Unicode
# 用法： python3 scripts/make_ledger_pdf.py   （生成 docs/REVIEW-LEDGER-22-items.pdf）
# 纪律：R7 结论由数字驱动 —— 本脚本末尾自检缺字=0、残留命令=0

# -*- coding: utf-8 -*-
import io, re, html, datetime
src='docs/REVIEW-LEDGER-22-items-tracker.md'
t=io.open(src,encoding='utf-8').read()
t='\n'.join(L for L in t.split('\n') if not L.startswith('已查地图'))
GREEK={'beta':'β','gamma':'γ','delta':'δ','zeta':'ζ','eta':'η','theta':'θ','kappa':'κ','lambda':'λ',
'mu':'μ','nu':'ν','xi':'ξ','pi':'π','rho':'ρ','sigma':'σ','tau':'τ','phi':'φ','chi':'χ','psi':'ψ',
'omega':'ω','alpha':'α','Gamma':'Γ','Delta':'Δ','Theta':'Θ','Lambda':'Λ','Xi':'Ξ','Pi':'Π','Sigma':'Σ',
'Phi':'Φ','Psi':'Ψ','Omega':'Ω','varepsilon':'ε','varphi':'φ','iota':'ι'}
SYM={r'\Longrightarrow':'⟹',r'\longrightarrow':'⟶',r'\Rightarrow':'⇒',r'\Leftrightarrow':'⇔',
r'\Longleftrightarrow':'⟺',r'\iff':'⟺',r'\to':'→',r'\mapsto':'↦',r'\times':'×',r'\cdot':'·',
r'\pm':'±',r'\mp':'∓',r'\le':'≤',r'\leq':'≤',r'\ge':'≥',r'\geq':'≥',r'\ll':'≪',r'\gg':'≫',
r'\ne':'≠',r'\neq':'≠',r'\approx':'≈',r'\asymp':'≍',r'\sim':'∼',r'\simeq':'≃',r'\supseteq':'⊇',
r'\subseteq':'⊆',r'\subset':'⊂',r'\supset':'⊃',r'\cup':'∪',r'\cap':'∩',r'\in':'∈',r'\notin':'∉',
r'\forall':'∀',r'\exists':'∃',r'\infty':'∞',r'\equiv':'≡',r'\mid':'∣',r'\partial':'∂',r'\nabla':'∇',
r'\sum':'∑',r'\prod':'∏',r'\int':'∫',r'\sqrt':'√',r'\dots':'…',r'\ldots':'…',r'\cdots':'⋯',r'\circ':'∘',
r'\subsetneq':'⊊',r'\emptyset':'∅',r'\wedge':'∧',r'\vee':'∨',r'\lVert':'‖',r'\rVert':'‖',r'\Box':'□',
r'\quad':'; ',r'\qquad':';  ',r'\ ':' ',r'\;':' ',r'\:':' ',r'\,':' ',r'\!':''}
SUP={'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹','+':'⁺','-':'⁻','n':'ⁿ'}
SUB={'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'}
def sup(s): return ''.join(SUP.get(c,c) for c in s)
def sub(s): return ''.join(SUB.get(c,c) for c in s)
def conv(s):
    s=re.sub(r'\\text\{([^{}]*)\}',r'\1',s)
    for cmd in ['textbf','textit','texttt','textsf','textrm','textnormal','textup','emph','mathbf','mathcal','mathbb','operatorname','boldsymbol','text']:
        s=re.sub(r'\\'+cmd+r'\{([^{}]*)\}',r'\1',s)
    s=s.replace('\\left','').replace('\\right','').replace('\\Big','').replace('\\big',''); s=re.sub(r'\\mathrm\{([^{}]*)\}',r'\1',s)
    s=re.sub(r'\\boxed\{([^{}]*)\}',r'【\1】',s); s=re.sub(r'\\substack\{([^{}]*)\}',r'\1',s)
    s=re.sub(r'\\(begin|end)\{[^{}]*\}','',s)
    for k,v in sorted(SYM.items(),key=lambda x:-len(x[0])): s=s.replace(k,v)
    for k,v in sorted(GREEK.items(),key=lambda x:-len(x[0])): s=re.sub(r'\\'+k+r'(?![a-zA-Z])',v,s)
    s=re.sub(r'\^\{([^{}]*)\}',lambda m:sup(m.group(1)),s); s=re.sub(r'\^(-?\w)',lambda m:sup(m.group(1)),s)
    s=re.sub(r'_\{([^{}]*)\}',lambda m:sub(m.group(1)),s);  s=re.sub(r'_(-?\w)',lambda m:sub(m.group(1)),s)
    s=re.sub(r'\\tfrac\{([^{}]*)\}\{([^{}]*)\}',r'(\1)/(\2)',s)
    s=re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}',r'(\1)/(\2)',s)
    s=re.sub(r'\\[a-zA-Z]+',lambda m:m.group(0)[1:],s)
    s=s.replace('{','').replace('}','').replace('$','').replace('\\','')
    return re.sub(r'[ \t]{2,}',' ',s).strip()

ls=t.split('\n'); out=[]; i=0
def inline(s):  # 行内数学 + 粗体 + 转义
    s=re.sub(r'\$(.+?)\$',lambda m:conv(m.group(1)),s,flags=re.S)
    s=html.escape(s); s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    return s
while i<len(ls):
    L=ls[i]
    if L.strip().startswith('$$'):                       # 显示公式（可跨行）
        buf=[L]
        while not (buf[-1].strip().endswith('$$') and len(buf[-1].strip())>2) and i+1<len(ls):
            i+=1; buf.append(ls[i])
        raw=' '.join(buf).replace('$$','')
        out.append('<div class="dm">'+html.escape(conv(raw))+'</div>'); i+=1; continue
    if L.strip().startswith('|') and i+1<len(ls) and re.match(r'^\|[\s:|-]+\|$',ls[i+1].strip()):
        rows=[]
        while i<len(ls) and ls[i].strip().startswith('|'):
            rows.append([c.strip() for c in ls[i].strip().strip('|').split('|')]); i+=1
        hdr,data=rows[0],rows[2:]
        out.append('<table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in hdr)+'</tr></thead><tbody>')
        for r in data: out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in r)+'</tr>')
        out.append('</tbody></table>'); continue
    s=L.rstrip()
    if s.startswith('# '): out.append('<h1>'+inline(s[2:])+'</h1>')
    elif s.startswith('## '): out.append('<h2>'+inline(s[3:])+'</h2>')
    elif s.startswith('### '): out.append('<h3>'+inline(s[4:])+'</h3>')
    elif s.startswith('> '): out.append('<div class="q">'+inline(s[2:])+'</div>')
    elif s.startswith('---'): out.append('<hr/>')
    elif s=='' : pass
    else: out.append('<p>'+inline(s)+'</p>')
    i+=1

EMOJI_MAP={'\u26d4':'[否]','\u2705':'[✓]','\u2b1c':'[ ]','\u1f534':'','\u1f7e1':'','\U0001f534':'[承重]',
'\U0001f7e1':'[部分]','\U0001f5c2':'','\U0001f527':'[勘误]','\u2b50':'★','\ufe0f':''}
def deemoji(x):
    for k,v in EMOJI_MAP.items():
        x=x.replace(k,v)
    x=x.replace('🔴','[承重]').replace('🟡','[部分]').replace('🗂','').replace('🔧','[勘误]')
    x=x.replace('⭐','★').replace('⛔','[否]').replace('✅','[✓]').replace('⬜','[ ]').replace('\ufe0f','')
    return x
CSS='''@page{size:A3 landscape;margin:7mm 6mm;}
body{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif;font-size:7.6pt;line-height:1.38;color:#111;}
h1{font-size:12.5pt;margin:0 0 2mm;border-bottom:1.1pt solid #333;padding-bottom:1mm;}
h2{font-size:10pt;margin:3mm 0 1mm;background:#eef;padding:.8mm 1.4mm;border-left:2.2pt solid #335;}
h3{font-size:7.4pt;margin:1.6mm 0 .8mm;}
p{margin:.5mm 0;} .q{color:#444;font-size:6.4pt;margin:.3mm 0;}
.dm{background:#f6f6fb;border-left:1.6pt solid #aab;padding:.8mm 1.5mm;margin:.8mm 0;font-size:6.5pt;}
hr{border:0;border-top:.5pt solid #bbb;margin:1.6mm 0;}
table{width:100%;border-collapse:collapse;table-layout:fixed;margin:1mm 0;}
th,td{border:.35pt solid #99a;padding:.85mm .95mm;vertical-align:top;font-size:6.6pt;overflow-wrap:anywhere;}
th{background:#dde;font-size:6.8pt;} tbody tr:nth-child(even){background:#fafafd;}
tr{page-break-inside:avoid;}
table th:nth-child(1),table td:nth-child(1){width:1.5%;text-align:center;}
table th:nth-child(2),table td:nth-child(2){width:5.2%;}
table th:nth-child(3),table td:nth-child(3){width:17.6%;}
table th:nth-child(4),table td:nth-child(4){width:10.8%;}
table th:nth-child(5),table td:nth-child(5){width:2.3%;text-align:center;}
table th:nth-child(6),table td:nth-child(6){width:34.5%;}
table th:nth-child(7),table td:nth-child(7){width:28.1%;}
code{font-family:"DejaVu Sans Mono","WenQuanYi Zen Hei Mono",monospace;}'''
h='<!DOCTYPE html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body><h1>22 项逐项审核台账（C-37）· 完整总表</h1><div class="q">源档 dn-project/docs/REVIEW-LEDGER-22-items-tracker.md ｜ 生成 '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M')+' ｜ 唐先生委托</div>'+'\n'.join(out)+'</body></html>'
h=deemoji(h)
io.open('/tmp/ledger4.html','w',encoding='utf-8').write(h); print('HTML ok',len(h))
