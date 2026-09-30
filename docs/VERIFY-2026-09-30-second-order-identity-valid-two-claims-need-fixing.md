# VERIFY-2026-09-30-2nd — 二阶 excess 恒等式 **成立 ✓✓**；另**两处需更正**（类型命名／$3A_3$ 上界）

> 空间 B｜非 C 号｜唐先生 10:00 之链（二阶 excess ＋ A2 配对 ＋ 权3 incidence）｜**不主张任何新值**（V290）

**已查地图**：承 `RESULT-P180`／`MULT{,2}`／`REFUTE-2026-09-30{,b}`／`DEFS-2026-09-29`
D0: 本档对象 = **档案已有**（$S,P,H,T_N,\delta$ 三型）之**核验**（新数学对象：无 ✗）
D1: 0（产出 = **一条新恒等式（已验） ＋ 两处更正** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① 新恒等式成立 ✓✓}:\quad 2S\ =\ E+P+T_N,\qquad S:=A_1{+}A_2,\ E:=11M{-}1024,\ T_N:=\sum_{x\notin C}\binom{e(x)}2}$$
$$\qquad\textbf{验证（120-码）}:\ 2S{=}398;\ E{+}P{+}T_N=296{+}41{+}61=398\ ✓✓;\ \text{等价形式}\ H{=}(E{-}2A_1){+}T_N\ (196{+}61{=}257\ ✓)$$
$$\boxed{\textbf{② 类型命名需更正}:\ \text{唐先生本轮称 }(a_1,a_2){=}(2,4)\ \text{为"A2"},\ \text{但前轮 A2}=(1,5)\ (261\text{ 处});\ \text{本轮之 }(2,4)\ \text{即前轮之 }\textbf B\ ✗}$$
$$\boxed{\textbf{③ }3A_3\ \text{之上界需更正}:\ \text{成立的应为 }|I_3|\le3N_3\ (N_3=\text{权3词数});\ \text{而 }3A_3\ \text{平凡（}3{\cdot}912\gg1051\text{）};\ \text{且 }3N_3\ \textbf{为假}\ (39<1051)\ ✗}$$

## §1 新恒等式（**本档净得 ✓**）

$$H=\sum_{x\notin C}\binom{\mu(x)}2=\sum_{x\notin C}\Bigl[e(x)+\binom{e(x)}2\Bigr]=(E-2A_1)+T_N\quad(\text{因 }E-2A_1=\sum_{x\notin C}e(x))$$
$$H+P=2A_2\ (F9)\ \Longrightarrow\ 2A_2=(E-2A_1)+T_N+P\ \Longrightarrow\ \boxed{2(A_1+A_2)=E+P+T_N}\ ✓✓$$
$$\text{意义}:\ S=71+\tfrac{P+T_N}2\ (M{=}106)\ \Longrightarrow\ S\ge71\ \text{且等号}\iff P=T_N=0\ (\text{即全 }Q_{10}\ \text{上 }e(x)\le1)\ ✓$$
$$\qquad\text{即原 }F7\ \text{之"71"＝二阶 excess 全零之基线} \Longrightarrow \text{比 }F7\ \text{更强之表述} ✓$$

## §2 类型命名（**须更正 ✗**）

| 轮次 | "A2" 之定义 | 实测（120-码） |
|---|---|---|
| 前轮（`REFUTE-b` 等） | $a_1{=}1,\ a_2{=}5$（excess 落非码字邻点 $x$） | **301** 个 |
| **本轮 §1** | $a_1{=}2,\ a_2{=}4$（excess 落 $v$ 自身）| **0** 个（120-码无此型） |

$$\therefore\ \text{本轮 §1–§2 所述"(2,4) 型"＝前轮之 }B;\ \text{而 120-码中 }B\ \text{型}\ =0 \Longrightarrow \text{其配对结构在 120-码上\ \textbf{无法实测}} ⚠️$$
$$\qquad\text{（此前实测：120-码 }(\delta,a_1)\ \text{分布}\ \{(1,1){:}338,\ (3,1){:}319,\ (3,2){:}97,\dots\}\ \text{无 }(1,2)\ \text{档} ✓）$$

## §3 权3 incidence 上界（**须更正 ✗**）

$$|I_3|=4n_{A1}+3n_{A2}\ (120\text{-码}: 4{\cdot}37+3{\cdot}301=1051);\qquad N_3=\#\{\text{权3词}\}=13;\qquad A_3=912$$
$$3A_3=2736\ \text{平凡成立（无用）};\qquad 3N_3=39\ \textbf{假}\ (1051\gg39)\ ✗$$
$$\therefore\ \text{正确定式需"以锚点为中心的距离-3 词"计数（}$N_3$ 是绝对重量 3 者，与锚点距离 3 者不同物）✗$$

## §4 与前轮 LP 结果之衔接

$$\text{`RESULT-P180' 已证：}P\le180\ \text{（真）};\ \text{但全部有效约束 }@M{=}106\ \textbf{仍可行}（\text{含 }P\le41）\ ✗$$
$$\therefore\ \text{本轮之新恒等式 }2S=E+P+T_N\ \text{虽真，但其为\ \textbf{恒等式级}\ （同 }F7\text{ 加强），\ 不产生新可行性约束} ⚠️$$

## §5 本档保留

$$\textbf{(i)}\ \boxed{2S=E+P+T_N}\ ✓\ (\text{新恒等式});\qquad \textbf{(ii)}\ \text{类型命名与 }3A_3/3N_3\ \text{之更正};\qquad \textbf{(iii)}\ \text{120-码无 }(2,4)\ \text{型点（0）} ✓$$
$$\textbf{(iv)}\ \text{前轮入册仍有效}:\ P\le180,\ A_1\le124,\ n_B\le H=2A_2-P,\ n_{A1}\le9q_1,\ n_{A2}\le8r_1,\ q_1\le2A_1-\tfrac29P$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**核验档**（一恒等式成立 ＋ 两处更正）✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
