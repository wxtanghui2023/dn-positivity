# RESEARCH-2026-09-30 — 局部→全局尝试：**取等精确刻画（双向已证 ✓✓）** ＋ 一条新不等式 ＋ **定位到的障碍**

> 空间 B｜非 C 号｜唐先生 17:05「研究级，就研究！」｜**不主张任何新值**（V290）
> 时间：2026-09-30 18:5x

**已查地图** ✓：`PROOF-2026-09-30-equality-forces-Sy-empty-theorem`／`…tight-per-y-pattern-inequality`／`…crosslevel-inequalities…`／`…per-y-inequality-slack-distribution`
D0: 本档对象 = **取等刻画之完整证明 ＋ 局部→全局计数尝试**（新定理＋新不等式 ✓；结论为否 ✗）
D1: 0（产出 = **一条双向定理 ＋ 一条新不等式 ＋ 一条障碍定位** ⚠️✓）

---

## §0 **定理（双向，皆已证 ✓✓）**

$$\textbf{定理}.\quad \delta_y=0\ \Longleftrightarrow\ S_y=\varnothing\ \wedge\ |U_y|=2^m\ \Longleftrightarrow\ \boxed{y\ \in\ \bigcap_\sigma N_1[L_\sigma]\ \textbf{且}\ y\ \notin\ \bigcup_\sigma L_\sigma}\ ✓✓$$
$$\textbf{(⟹)}:\ \text{已证（前档 3 行）};\quad \textbf{(⟸)}:\ y\notin\cup L_\sigma\Rightarrow S_y=\varnothing;\ y\in\cap N_1[L_\sigma]\Rightarrow U_y=\mathbb F_2^m\Rightarrow|U_y|=2^m\Rightarrow\delta_y=0+2^m-2^m=0\ ✓$$
$$\textbf{实测（两码 × }m{=}1,2,3\text{）}:\ \text{刻画违反数}\ \mathbf 0\ \text{（120-码}\ 394/512,145/256,34/128;\ \text{62-码}\ 194/512,68/256,15/128）✓✓$$

## §1 **局部→全局之计数尝试（本档研究内容）**

$$\textbf{(a)}\ \text{取等点数}:\ \#\text{eq}=\Big|\bigcap_\sigma N_1[L_\sigma]\Big|-\Big|\bigcap_\sigma N_1[L_\sigma]\cap\bigcup_\sigma L_\sigma\Big|$$
$$\textbf{(b)}\ \text{非取等点 }\ge\ \sum_y\delta_y\ \text{（}\delta\ \text{为整数 }\ge1\text{）};\quad 2^{nc}-\#\text{eq}\ \le\ \sum_y\delta_y=(m{+}1)M+\sum_\sigma|N_1[L_\sigma]|-2^n\ \ (*)$$
$$\textbf{(c)}\ \#\text{eq}\le\Big|\bigcap_\sigma N_1[L_\sigma]\Big|\le\min_\sigma|N_1[L_\sigma]|\ \Longrightarrow\ \textbf{\text{新不等式}}:\ \boxed{(m{+}1)M+\sum_\sigma|N_1[L_\sigma]|+\min_\sigma|N_1[L_\sigma]|\ \ge\ 2^n+2^{nc}}\ ✓$$

## §2 **障碍定位（诚实 ✗）**

$$\text{求 }M\ \text{之下界需}\ \sum_\sigma|N_1[L_\sigma]|\ \text{之\ \textbf{上界}};\ \text{现有者仅 }\ \sum_\sigma|N_1[L_\sigma]|\le\sum_\sigma\min(2^{nc},(nc{+}1)|L_\sigma|)\le(nc{+}1)M\ ✓\ (\text{平凡})$$
$$\text{代入 §1(c)}:\ \text{得 }(n{+}2)M+\min_\sigma|N_1[L_\sigma]|\ge2^n+2^{nc};\quad M{=}106,n{=}10:\ 12{\cdot}106=1272\ \text{vs}\ 1024+2^{nc}\ \Longrightarrow\ \textbf{\text{仅当 }}2^{nc}\le248\ \text{时紧（}m\le3\ \text{时}\ 2^{nc}=128\ \text{可）} ⚠️\ \text{但不冲突} ✗$$
$$\therefore\ \boxed{\textbf{\text{障碍}}:\ \text{一切\ \textbf{聚合（求和）化} 皆丢掉了层间\ \textbf{耦合}};\ \text{要闭合必须引入}\ \textbf{\text{层间成对/多路交叠}} \text{之结构性上界} ——\ \text{而这又等价于\ \textbf{设计存在性}（＝原问题）} ✗✓}$$
$$\qquad\text{即}:\ \text{本节所得之定理与不等式\ \textbf{皆为真}} ✓,\ \text{但\ \textbf{不足以}\ 推出 }M\ \text{之新下界} ✗$$

## §3 **下一步之具体建议（有牙之方向 ⚠️）**

$$\textbf{唯一可能的出口}:\ \text{引入\ \textbf{成对层交叠量}}\ A_{\sigma\tau}:=|N_1[L_\sigma]\cap N_1[L_\tau]|\ \text{及其与 covering 之关系} ⚠️$$
$$\qquad\text{理由}:\ \#\text{eq}\ \text{之精确式（§1(a)）恰含这些交叠};\ \text{而层间交叠\ \textbf{不}\ 由 }(|L_\sigma|)\ \text{之边缘量决定}\ \Longrightarrow\ \text{此处\ \textbf{首次}\ 出现非聚合信息} ✓✓$$
$$\qquad\text{但}:\ \text{能否由此得界，\textbf{未知}} ⚠️\ (\text{须实算；本会话未及})$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 层间交叠     命中文件数=1    :: 本档
技术词 局部到全局  命中文件数=4    :: C298-q-prime-closure-and-commuting-defect-chain-audit.md ＋ V165-type-mismatch-diagnostic-toolcard.md ＋ TLDC-1-PhaseV1-mechanism-existence-screening-ten-candidates.md ＋ 本档
```

$$\textbf{分类（三项如实 ✓）}:\ \text{(1) }\textbf{本档新增}：\text{“层间交叠”} ⟹ \text{仅本档} ✓;\quad \text{(2) }\textbf{档案已有（引用，不列为提出）}：\text{“局部到全局”命中 3 档（空间 A 之 RH 线）} ✗\ \text{故不主张其新性};\quad \text{(3) }\textbf{通用词（不计）}：\text{“交叠／全局”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{“局部到全局”之既有命中属空间 A} ⟹ \text{标为**跨空间同名（不计）**} ✓$$


$$\text{【补记·回查 ✓】技术词“层间耦合”：命中 3 处 = 本档 ＋ }V235\text{-euler-layer-compatibility…（空间 A）＋ }CLOSED\text{-ROUTES-MAP} ⟹ \textbf{跨空间同名（不计）} ✗\ \text{（本档不主张该词之新性）}$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{定理双向已证（可复核 ✓）；实测零违反};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA

---

## §6 **层间交叠实算结果（120-码，$m{=}2$）＋ 同障碍之高阶版本** ✗

$$\text{层大小}:\ (|L_{00}|,|L_{01}|,|L_{10}|,|L_{11}|)=(28,32,32,28);\quad |N_1[L_\sigma]|=(207,210,210,207)\ ✓$$
$$\textbf{成对交叠}\ A_{\sigma\tau}=|N_1[L_\sigma]\cap N_1[L_\tau]|:\ \text{相邻对（}d{=}1\text{）}=\mathbf{162}\ (\times4);\quad \text{对角对（}d{=}2\text{）}=\mathbf{204}\ (\times2)\ ✓\ \text{——只依赖 }d(\sigma,\tau)\ ✓$$
$$\textbf{恒等式核验}\ ✓✓:\ |\bigcap_\sigma N_1[L_\sigma]|=156,\ |\bigcup_\sigma L_\sigma|=111,\ \#\text{eq}=156-11=\mathbf{145}\ \text{（与实测取等点数 145 完全一致 ✓✓）}$$
$$\textbf{但（关键 ✗）}:\ \text{Inclusion--exclusion}:\ 156=834-1056+(\text{triples})-(\text{quad})\ \Longrightarrow\ (\text{triples})-(\text{quad})=378\ \text{——\textbf{\text{高阶项巨大}}} ✗$$
$$\therefore\ \boxed{\text{成对交叠\ \textbf{不足}：须全部阶；即“层间耦合”之完整信息\ =\ 原问题}} ✗✓\ \text{——与 §2 障碍\ \textbf{同一性质}} ✓$$

## §7 **本会话研究尝试之诚实总结**

$$\textbf{已产（真 ✓）}:\ \text{块分层引理};\ \text{逐点模式不等式（健全、真码多处取等）};\ \text{跨层两不等式（超加性＋上界）};\ \textbf{\text{取等之双向精确刻画（定理 ★）}};\ \text{新不等式（§1c）};\ \text{等价的层间交叠实证} ✓$$
$$\textbf{未产（✗）}:\ M\ \text{之新下界};\ \text{“取等刚性不可全局一致”之证明} ✗\ ——\ \textbf{\text{障碍已定位两次（聚合化、成对交叠）}}，皆为“\textbf{\text{丢掉耦合}}” ✓$$
$$\textbf{定位结论}:\ \text{局部结构改写是\ \textbf{精确} 的（不含松弛）} ✓,\ \text{但一切\ \textbf{局部→全局} 的\ \textbf{聚合} 步骤所丢信息恰是\ \textbf{原问题的内容}} ✗ ⟹ \text{此线\ \textbf{已定位、未闭合}} ✓$$

---

## §8 **研究级续做（本轮新增三项，皆实测 ✓）**

$$\textbf{(8.1) 取等之\ \textbf{强化形式}} ✓✓:\ \delta_y=0\Longrightarrow S_y=\varnothing\ (\Rightarrow y\notin L_\sigma\ \forall\sigma)\ \text{且}\ y\in N_1[L_\sigma]\ \forall\sigma\ \Longrightarrow\ \forall\sigma\ \exists w\in L_\sigma:\ d(w,y)=\mathbf 1\ (\text{恰为 1，非 }\le1)$$
$$\qquad\textbf{实测}:\ \text{两码×三层}\ \textbf{\text{违反数}=0}\ ✓✓\ (120\text{-码 }m{=}1,2,3;\ 62\text{-码 }m{=}1,2,3)$$
$$\qquad\therefore\ \text{取等点被}\ \textbf{每一层} \text{以“距离恰 1”之码字\ \textbf{包围}};\ \text{且各层之该码字\ \textbf{互不相同}（层不同 ✓）}$$

$$\textbf{(8.2) 等价计数之上界} ✓:\ \text{每个 }(y,\sigma)\ \text{对（}y\in E,\ \sigma\in\mathbb F_2^m\text{）至少对应一个码字 }c=(\sigma,w)\ (w\sim y);\ \text{而一个码字最多服务 }nc\ \text{个 }y\ (\text{其 }nc\ \text{个补空间邻点})$$
$$\qquad\Longrightarrow\ \boxed{|E|\cdot 2^m\ \le\ M\cdot nc}\ \text{即}\ |E|\le\frac{M\,nc}{2^m}\ ✓\ \text{——}\textbf{\text{比前之}}\ \#\text{eq}\cdot2^m\le\sum_\sigma|N_1[L_\sigma]|\le(nc{+}1)M\ \textbf{\text{更紧}}（nc\ \text{vs}\ nc{+}1）$$
$$\qquad\textbf{实测}:\ 120\text{-码 }m{=}2:\ |E|{=}145\le240\ ✓;\ 62\text{-码 }m{=}2:\ |E|{=}68\le108.5\ ✓\ \text{（皆满足，未违 ✗）}$$

$$\textbf{(8.3) 全局矛盾检验（逐 }m\text{，判定式 }2^{nc}+2^n-(nc{+}1)M>M(m+1+\tfrac{nc}{2^m})\text{）} ✗$$
| $m$ | $nc$ | LHS | RHS | 判定 |
|---|---|---|---|---|
| 1 | 9 | 476 | 689.0 | 不矛盾 ✗ |
| 2 | 8 | 326 | 530.0 | 不矛盾 ✗ |
| 3 | 7 | 304 | 516.8 | 不矛盾 ✗ |
| 4 | 6 | 346 | 569.8 | 不矛盾 ✗ |
| 5 | 5 | 420 | 652.6 | 不矛盾 ✗ |

$$\therefore\ \boxed{\text{“取等计数 vs 码字容量”这一族全局化，\ 在}\ \textbf{每一个} \text{块大小 }m\in\{1..5\}\ \text{处\ \textbf{系统性失败}} ✗;\ \text{且差距是\ \textbf{因子 }\sim1.5\text{--}2}\ (\text{非“差一点”}) ⚠️}$$
$$\qquad\Longrightarrow\ \text{这不是“再加一个想法”可及；而是\ \textbf{\text{结构性缺口}} ✗\ ——\ \text{与 §2／§6 之两次定位\ \textbf{同性质}（聚合必丢耦合）✓}$$
$$\textbf{诚实}:\ \text{本轮未产 }M\ \text{之下界} ✗;\ “取等刚性无法全局一致”\ \textbf{\text{仍未证}} ✗;\ \text{但其\ \textbf{\text{失败幅度已量化}}（每 }m\ \text{皆因子 }1.5\text{--}2\ ✗）\ ✓$$

---

## §9 **反推（用户选项①）：缺口需要什么量？—— 答案＝取等点集之\ \textbf{覆盖数}\ $\gamma_1(E)$（min-型）** ✓，并已证 $M\ge2^m\gamma_1(E)$

$$\textbf{推导（新定理 ✓）}:\ E\subseteq N_1[L_\sigma]\ \forall\sigma\ (\text{§0 刻画之直接推论})\ \Longrightarrow\ L_\sigma\ \text{本身即覆盖 }E\ \text{之集合} \Longrightarrow\ |L_\sigma|\ge\gamma_1(E):=\min\{|A|:N_1[A]\supseteq E\}$$
$$\qquad\Longrightarrow\ \boxed{M=\sum_\sigma|L_\sigma|\ \ge\ 2^m\,\gamma_1(E)}\ ✓\ \text{（\textbf{\text{首次得到含 min-型非聚合量之精确不等式}}）}$$

$$\textbf{实测（120-码，参考点）}:\ \gamma_1(E)\ \text{之 LP 下界／贪心上界}:\ m{=}1:\ 50.23/70\ (|E|{=}394);\ m{=}2:\ 24.80/32\ (|E|{=}145);\ m{=}3:\ 10.60/12\ (|E|{=}34)$$
$$\qquad\text{层大小皆}\ge\gamma_1(E)\ ✓\ (\text{如 }m{=}2:\ |L_\sigma|=(28,32,32,28)\ge24.8 ✓);\quad M{=}120\ge2^m\gamma_1\ ✓\ \text{全部满足 ✗（未违）}$$

$$\textbf{排除 }M{=}106\ \text{之\ \textbf{具体靶（量化 ✓✓）}}:\ \text{需 }M<2^m\gamma_1(E)\ \text{即}\ \gamma_1(E)>\tfrac{106}{2^m}\ \Longrightarrow\ \boxed{\gamma_1(E)\ \ge\ 54\ (m{=}1);\ \ 27\ (m{=}2);\ \ 14\ (m{=}3)}$$
$$\qquad\text{与参考值对照（120-码）}:\ 50.2<54\ ✗;\ 24.8<27\ ✗;\ 10.6<14\ ✗\ \Longrightarrow\ \textbf{\text{目标皆\ \textbf{高于} 参考值，但仅高出 }\sim7\%\text{--}30\%}\ ⚠️$$

$$\textbf{诚实（✗）}:\ \text{单靠 }\gamma_1\ \text{与 }\gamma_1\ge|E|/(nc{+}1)\ \text{仍\ \textbf{复现旧界}} ✗\ (|E|\le\frac{(nc+1)M}{2^m}\ ✓)\ \Longrightarrow\ \text{要咬，必须给出\ \textbf{基于 }E\ \text{之\ \textbf{集合结构} 的 }\gamma_1\ \text{下界}} ⚠️$$
$$\qquad\text{即}:\ \text{需要关于 }E\ \text{之\ \textbf{额外结构事实}}（\text{如 }E\ \text{之最小距离／分布／“形状”}）\ ✓\ \text{——}\textbf{\text{这是本线首次出现的、带具体数值靶的非聚合目标}} ✓✓$$
$$\qquad\text{已知 }E\ \text{之结构事实（现仅有）}:\ E\subseteq\bigcap_\sigma N_1[L_\sigma],\ E\cap\bigcup_\sigma L_\sigma=\varnothing,\ \forall\sigma\ \exists w\in L_\sigma: d(w,y){=}1\ (\text{§8.1}) ⚠️\ ——\ \textbf{\text{尚不足以定 }\gamma_1}$$

---

## §10 **组装结果（本轮）：$\gamma_1$ 路线的完整不等式与其\ \textbf{结构上限}** ✓（含实测）

$$\text{四个分量}:\ \text{(1)}\ M\ge2^m\gamma_1(E)\ \text{（§9 已证）};\ \text{(2)}\ \gamma_1(E)\ge|E|/\lambda,\ \lambda:=\max_a|N_1[a]\cap E|\ \text{（标准：一覆盖点至多覆盖 }\lambda\ \text{个 }E\ \text{点）};$$
$$\qquad\text{(3)}\ |E|\ge2^{nc}-\Sigma\delta\ \text{（非取等点 }\delta\ge1\text{）};\ \text{(4)}\ \Sigma\delta\le(n{+}2)M-2^n\ \text{（}\Sigma\delta=(m{+}1)M+\Sigma_\sigma|N_1[L_\sigma]|-2^n\ \text{与 }|N_1[L_\sigma]|\le(nc{+}1)|L_\sigma|\text{）}$$
$$\Longrightarrow\ \boxed{M\ \ge\ \frac{2^m\,(2^{nc}+2^n)}{\lambda\ +\ 2^m(n+2)}}\ ✓\ \text{（\textbf{\text{新不等式族}}，含 min-型量之局部密度参数 }\lambda\text{）}$$

$$\textbf{实测（120-码）}:$$
| $m$ | $\|E\|$ | $\lambda$ | $\|E\|/\lambda$ | 组装式 |
|---|---|---|---|---|
| 1 | 394 | **9** | 43.78 | **93.09** |
| 2 | 145 | **7** | 20.71 | **93.09** |
| 3 | 34 | **4** | 8.50 | 92.16 |

$$\textbf{路线之上限（最佳 }\lambda{=}1\text{）}:\ m{=}1:\ 122.88\Rightarrow M\ge\mathbf{123}\ ✓;\ m{=}2:\ 104.49\Rightarrow105\ ✗;\ m{=}3:\ 96\ ✗;\ m{=}4:\ 91\ ✗$$
$$\textbf{关键读数}:\ \text{仅 }m{=}1\ \text{可能收口}——\text{需 }\lambda+2(n{+}2)<\tfrac{2(2^{n-1}+2^n)}{106}=28.98\ \text{即}\ \boxed{\lambda\le4};\ \text{而实测 }\lambda{=}9\ ✗\ \Longrightarrow\ \textbf{\text{未成立}} ✗$$

$$\textbf{诚实（第 4 次同障）}:\ \text{中间步骤 (3)(4) 仍为\ \textbf{聚合量}} ⟹ \text{与 §2／§6／§8.3 同性质：聚合必丢耦合} ✗$$
$$\Longrightarrow\ \textbf{\text{新靶（非聚合、可量化）}}:\ \boxed{\text{证明任意 }106\text{-covering 之 }m{=}1\ \text{取等点集满足}\ \lambda\le4}\ ⚠️\ \text{（即：无点 1-邻域内含 }>4\ \text{个取等点）}$$
$$\qquad\text{——}\textbf{\text{这是本线首个把“需要什么”写成具体数值命题者}} ✓✓;\ \text{其真假未知} ⚠️$$
