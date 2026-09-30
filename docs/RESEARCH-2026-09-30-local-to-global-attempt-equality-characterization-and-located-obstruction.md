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


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{定理双向已证（可复核 ✓）；实测零违反};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
