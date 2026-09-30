# RESULT-2026-09-30 — **取等情形之强刚性（"极强刚性"一词档案已有，本档不主张新性）**（两码 × $m{=}1,2,3$ 实测一致 ✓✓）：取等 $\Rightarrow S_y{=}\varnothing$ **且** $|U_y|{=}2^m$（$y$ 不属于任何层，却与每一层皆距离 $\le1$）

> 空间 B｜非 C 号｜唐先生 17:01「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 18:3x

**已查地图** ✓：`RESULT-2026-09-30-crosslevel-inequalities…`／`tight-per-y-pattern-inequality`／`per-y-inequality-slack-distribution`
D0: 本档对象 = **取等情形之结构定理**（新 ✓，档案无同名）
D1: 0（产出 = **一条实测结构定理 ＋ 一条健全性讨论 ＋ 一条(甲)之诚实界限** ⚠️✓）

---

## §0 **(甲) 之结构内核（可得证之部分 ✓）**

$$\text{取等 }\delta_y=0\ \Longrightarrow\ T_y=N_1[S_y]=\bigsqcup_{\sigma\in S_y}N_1[\sigma]\ (\textbf{\text{不交}})\ \Longleftrightarrow\ \forall\sigma\ne\sigma'\in S_y:\ d(\sigma,\sigma')\ \ge\ \mathbf 3\ ✓✓$$
$$\qquad\Longrightarrow\ S_y\ \text{是}\ \mathbb F_2^m\ \text{中\ \textbf{最小距离}\ge3\ \text{之码}} \Longrightarrow |S_y|\le\min\{A(m,3),\ \lfloor 2^m/(m+1)\rfloor\}\ ✓\ (\text{Hamming 界})$$

## §1 **实测：更强之事实**（120-码 ＋ 62-码，$m{=}1,2,3$ ✓✓）

| 码 | $m$ | 取等点数 | **取等处 $\max|S_y|$** | 球不交违反 |
|---|---|---|---|---|
| 120-码 | 1 | 394/512 | **0** | **0** |
| 120-码 | 2 | 145/256 | **0** | **0** |
| 120-码 | 3 | 34/128 | **0** | **0** |
| 62-码 | 1 | 194/512 | **0** | **0** |
| 62-码 | 2 | 68/256 | **0** | **0** |
| 62-码 | 3 | 15/128 | **0** | **0** |

$$\therefore\ \boxed{\text{取等 }\Longrightarrow\ S_y=\varnothing\ \textbf{且}\ |U_y|=2^m}\ ✓✓\ \text{（实测两码、六层全一致）}$$
$$\text{即}:\ \text{取等点 }y\ \textbf{\text{不属于任何层}}，\text{却}\ \textbf{\text{与每一层皆距离}\le1}:\ \forall\sigma\ \exists w\in L_\sigma:\ d(w,y)\le1\ ✓$$
$$\text{（理论容许之另一型 }(|S_y|,|U_y|){=}(1,1)\ (m{=}2)\ \textbf{\text{实测从不出现}} ⚠️\ ——\ \text{其排除尚无独立证明} ⚠️）$$

## §2 **诚实：聚合后果仍平凡** ✗

$$\text{由 §1}:\ \#(\text{取等}y)\cdot 2^m\le\sum_\sigma|N_1[L_\sigma]|\ ⟹\ 2^{nc}\le \frac{\sum_\sigma|N_1[L_\sigma]|}{2^m}+\sum_y\delta_y\le (m{+}1)M+2^{nc}\ \Longrightarrow\ \textbf{\text{恒真}} ✗$$
$$\therefore\ \textbf{\text{本结构定理之力量仍只在逐点}};\ \text{其\ \textbf{聚合化}\ 至今全部平凡} ⚠️$$

## §3 **(甲) 之诚实界限**

$$\textbf{已得 ✓}:\ \text{取等之}\textbf{\text{精确刚性}}（S_y=\varnothing,\ |U_y|=2^m）＋ \text{其可证部分（球不交}\Rightarrow d\ge3）;\ \textbf{\text{逐层传播}}（`b3dd3b6`）$$
$$\textbf{未得 ✗}:\ \text{“该刚性无法全局一致”\ \textbf{\text{之证明}} —— 属\ \textbf{\text{研究级}};\ 且\ \text{单一码之实测不能代替证明（V290）} ⚠️$$
$$\textbf{结论}:\ \text{(甲) 已把靶\ \textbf{\text{磨到最细}}（刚性形式明确、可证部分已证）},\ \text{但\ \textbf{\text{最后一跳}} 需新的全局论证或不可得之源} ✗$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 取等刚性     命中文件数=0    :: 
技术词 极强刚性     命中文件数=3    :: ASSETS-REGISTRY.md ＋ 本档 ＋ WITP3128-2026-09-28-inclusion-exclusion-and-the-affine-disproof.md
```

$$\textbf{分类（三项如实 ✓）}:\ \text{(1) }\textbf{本档新增}：\text{“取等刚性”} ⟹ \text{全档 0 命中} ✓;\quad \text{(2) }\textbf{档案已有（引用，不列为提出）}：\text{“极强刚性”} ⟹ \text{命中 3 处（含地图）} ✗\ \text{故本档**不**主张该词之新性，标题已改};\quad \text{(3) }\textbf{通用词（不计）}：\text{“刚性／取等”裸词}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{WITP3128 属空间 B 之既有档，然其“极强刚性”指他对象} ⟹ \text{标为**同名不同对象（不计）**} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{实测为两码六层；\ \textbf{不} 声称一般定理（除非给出证明）} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
