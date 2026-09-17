#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# md2pdf.py —— 通用 markdown(含 LaTeX) → PDF（A3 横向，CJK+符号字体回退）
# 用法： python3 scripts/md2pdf.py <input.md> <output.pdf> [标题]
# 依赖： weasyprint ✓ ＋ 文泉驿正黑 + DejaVu（逐字回退）✓；无 LaTeX 中文栈 ⟹ LaTeX 转 Unicode
import io, re, html, sys, datetime, os

src, out_pdf = sys.argv[1], sys.argv[2]
title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(src)
t = io.open(src, encoding='utf-8').read()
t = '\n'.join(L for L in t.split('\n') if not L.startswith('已查地图'))

GREEK = {'alpha':'α', 'beta':'β', 'gamma':'γ', 'delta':'δ', 'epsilon':'ϵ', 'varepsilon':'ε', 'zeta':'ζ', 'eta':'η', 'theta':'θ', 'vartheta':'ϑ', 'iota':'ι', 'kappa':'κ', 'lambda':'λ', 'mu':'μ', 'nu':'ν', 'xi':'ξ', 'omicron':'ο', 'pi':'π', 'varpi':'ϖ', 'rho':'ρ', 'varrho':'ϱ', 'sigma':'σ', 'varsigma':'ς', 'tau':'τ', 'upsilon':'υ', 'phi':'ϕ', 'varphi':'φ', 'chi':'χ', 'psi':'ψ', 'omega':'ω', 'Gamma':'Γ', 'Delta':'Δ', 'Theta':'Θ', 'Lambda':'Λ', 'Xi':'Ξ', 'Pi':'Π', 'Sigma':'Σ', 'Upsilon':'Υ', 'Phi':'Φ', 'Psi':'Ψ', 'Omega':'Ω'}
SYM = {r'\Longrightarrow':'⟹',r'\longrightarrow':'⟶',r'\Rightarrow':'⇒',r'\Leftrightarrow':'⇔',
 r'\Longleftrightarrow':'⟺',r'\iff':'⟺',r'\to':'→',r'\mapsto':'↦',r'\times':'×',r'\cdot':'·',
 r'\pm':'±',r'\mp':'∓',r'\le':'≤',r'\leq':'≤',r'\ge':'≥',r'\geq':'≥',r'\ll':'≪',r'\gg':'≫',
 r'\ne':'≠',r'\neq':'≠',r'\approx':'≈',r'\asymp':'≍',r'\sim':'∼',r'\simeq':'≃',r'\supseteq':'⊇',
 r'\subseteq':'⊆',r'\subset':'⊂',r'\supset':'⊃',r'\cup':'∪',r'\cap':'∩',r'\in':'∈',r'\notin':'∉',
 r'\forall':'∀',r'\exists':'∃',r'\infty':'∞',r'\equiv':'≡',r'\mid':'∣',r'\perp':'⊥',r'\setminus':'∖',
 r'\partial':'∂',r'\nabla':'∇',r'\sum':'∑',r'\prod':'∏',r'\int':'∫',r'\oint':'∮',r'\sqrt':'√',
 r'\dots':'…',r'\ldots':'…',r'\cdots':'⋯',r'\circ':'∘',r'\subsetneq':'⊊',r'\emptyset':'∅',
 r'\wedge':'∧',r'\vee':'∨',r'\neg':'¬',r'\lfloor':'⌊',r'\rfloor':'⌋',r'\lceil':'⌈',r'\rceil':'⌉',
 r'\langle':'⟨',r'\rangle':'⟩',r'\lVert':'‖',r'\rVert':'‖',r'\|':'‖',r'\Vert':'‖',r'\Box':'□',
r'\star':'⋆',r'\ast':'∗',r'\qquad':'   ',r'\quad':'  ',r'\oplus':'⊕',r'\otimes':'⊗'}
WORDS = ['tan','cot','log','ln','cosh','sinh','csc','sec','sin','cos','tanh','max','min','sup','inf',
         'exp','det','lim','arg','deg','gcd','Re','Im','dim','rank','Spec','tr']
SUP = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹','+':'⁺','-':'⁻','n':'ⁿ'}
SUB = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'}
SET = {r'\mathbb{C}':'ℂ',r'\mathbb C':'ℂ',r'\mathbb{R}':'ℝ',r'\mathbb R':'ℝ',r'\mathbb{Z}':'ℤ',
       r'\mathbb Z':'ℤ',r'\mathbb{N}':'ℕ',r'\mathbb N':'ℕ',r'\mathbb{Q}':'ℚ',r'\mathbb Q':'ℚ',
       r'\mathbb{T}':'𝕋',r'\mathbb H':'ℍ'}
def sup(s): return ''.join(SUP.get(c,c) for c in s)
def sub(s): return ''.join(SUB.get(c,c) for c in s)

KEEPARG = ('text','textrm','textit','textbf','texttt','textsf','textnormal','textup','mathrm','mathbf',
 'mathit','mathsf','mathtt','mathcal','mathbb','mathfrak','operatorname','emph','boldsymbol','mathnormal',
 'widehat','widetilde','hat','tilde','bar','overline','underline','vec','dot','ddot','boxed','overbrace',
 'underbrace','xrightarrow','stackrel','mathop')
DROP = ('left','right','bigl','bigr','Bigl','Bigr','biggl','biggr','big','Big','bigg','Bigg','displaystyle',
 'textstyle','scriptstyle','limits','nolimits','rm','it','bf','sf','tt','cal','mit','mathord','mspace','!')

def conv(s):
    s = re.sub(r'\\substack\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(begin|end)\{[^{}]*\}', '', s)
    # 迭代剥离：命令带参数（可嵌套一层）
    for _ in range(6):
        s2 = re.sub(r'\\(%s)\{([^{}]*)\}' % '|'.join(KEEPARG), r'\2', s)
        if s2 == s: break
        s = s2
    s = re.sub(r'\\(mathcal|mathbb|mathrm|mathbf|mathit|mathfrak|mathsf|mathtt|operatorname)\s*([A-Za-z])', r'\2', s)
    for k, v in sorted(SET.items(), key=lambda x: -len(x[0])): s = s.replace(k, v)
    for k, v in sorted(SYM.items(), key=lambda x: -len(x[0])): s = s.replace(k, v)
    for k, v in sorted(GREEK.items(), key=lambda x: -len(x[0])): s = re.sub(r'\\'+k+r'(?![a-zA-Z])', v, s)
    for w in sorted(WORDS, key=len, reverse=True): s = re.sub(r'\\'+w+r'(?![a-zA-Z])', w, s)
    for d in sorted(DROP, key=len, reverse=True): s = re.sub(r'\\'+d+r'(?![a-zA-Z])', '' if d!='left' and d!='right' else '', s)
    s = re.sub(r'\^\{([^{}]*)\}', lambda m: sup(m.group(1)), s)
    s = re.sub(r'\^(-?\w)', lambda m: sup(m.group(1)), s)
    s = re.sub(r'_\{([^{}]*)\}', lambda m: sub(m.group(1)), s)
    s = re.sub(r'_(-?\w)', lambda m: sub(m.group(1)), s)
    s = re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', s)
    s = re.sub(r'\\[dt]?frac\s*(\w)\s*\{([^{}]*)\}', r'(\1)/(\2)', s)
    s = re.sub(r'\\[dt]?frac\s*(\d)\s*(\d)', r'(\1)/(\2)', s)
    s = re.sub(r'\\[a-zA-Z]+', lambda m: m.group(0)[1:], s)   # 残余命令去反斜杠
    s = s.replace('{','').replace('}','').replace('$','').replace('\\','')
    return re.sub(r'[ \t]{2,}', ' ', s).strip()

ls = t.split('\n'); out = []; i = 0
def inline(s):
    s = re.sub(r'\$(.+?)\$', lambda m: conv(m.group(1)), s, flags=re.S)
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s
while i < len(ls):
    L = ls[i]
    if L.strip().startswith('$$'):
        buf = [L]
        while not (buf[-1].strip().endswith('$$') and len(buf[-1].strip()) > 2) and i+1 < len(ls):
            i += 1; buf.append(ls[i])
        out.append('<div class="dm">'+html.escape(conv(' '.join(buf).replace('$$','')))+'</div>'); i += 1; continue
    if L.strip().startswith('|') and i+1 < len(ls) and re.match(r'^\|[\s:|-]+\|$', ls[i+1].strip()):
        rows = []
        while i < len(ls) and ls[i].strip().startswith('|'):
            rows.append([c.strip() for c in ls[i].strip().strip('|').split('|')]); i += 1
        out.append('<table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
        for r in rows[2:]: out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in r)+'</tr>')
        out.append('</tbody></table>'); continue
    s = L.rstrip()
    if s.startswith('# '): out.append('<h1>'+inline(s[2:])+'</h1>')
    elif s.startswith('## '): out.append('<h2>'+inline(s[3:])+'</h2>')
    elif s.startswith('### '): out.append('<h3>'+inline(s[4:])+'</h3>')
    elif s.startswith('> '): out.append('<div class="q">'+inline(s[2:])+'</div>')
    elif s.startswith('---'): out.append('<hr/>')
    elif s == '': pass
    else: out.append('<p>'+inline(s)+'</p>')
    i += 1

CSS = '''@page{size:A3 landscape;margin:8mm 7mm;}
body{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif;font-size:7.8pt;line-height:1.42;color:#111;}
h1{font-size:13pt;margin:0 0 2mm;border-bottom:1.2pt solid #333;padding-bottom:1mm;}
h2{font-size:9.6pt;margin:3.4mm 0 1.2mm;background:#eef;padding:.9mm 1.6mm;border-left:2.6pt solid #335;page-break-after:avoid;}
h3{font-size:8.2pt;margin:2mm 0 1mm;}
p{margin:.7mm 0;} .q{color:#444;font-size:7.2pt;margin:.4mm 0;}
.dm{background:#f6f6fb;border-left:1.8pt solid #aab;padding:.9mm 1.6mm;margin:1mm 0;font-size:7.4pt;}
hr{border:0;border-top:.5pt solid #bbb;margin:2mm 0;}
table{width:100%;border-collapse:collapse;table-layout:fixed;margin:1mm 0;}
th,td{border:.35pt solid #99a;padding:.85mm 1mm;vertical-align:top;font-size:6.4pt;overflow-wrap:anywhere;}
th{background:#dde;font-size:6.8pt;} tbody tr:nth-child(even){background:#fafafd;}
tr{page-break-inside:avoid;}
code{font-family:"DejaVu Sans Mono","WenQuanYi Zen Hei Mono",monospace;}'''
h = ('<!DOCTYPE html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>'
     '<h1>'+html.escape(title)+'</h1>'
     '<div class="q">源档 '+html.escape(src)+' ｜ 生成 '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M')+'</div>'
     + '\n'.join(out) + '</body></html>')
io.open('/tmp/_md2pdf.html', 'w', encoding='utf-8').write(h)
print('HTML ok', len(h))
