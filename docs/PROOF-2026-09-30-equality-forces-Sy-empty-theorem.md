# PROOF-2026-09-30 — **定理：取等 $\Longrightarrow S_y=\varnothing$**（3 行证明 ✓✓）⟹ $(1,1)$ 型及一切 $|S_y|>0$ 之取等**皆被排除**；(甲) 子问题闭合

> 空间 B｜非 C 号｜唐先生 17:03「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 18:4x

**已查地图** ✓：`RESULT-2026-09-30-equality-case-rigidity…`（实测观察）／`…tight-per-y-pattern-inequality`（引理）／`…crosslevel-inequalities…`
D0: 本档对象 = **上一档实测观察之\ \textbf{证明}**（新定理 ✓）
D1: 0（产出 = **一条 3 行定理 ＋ 一条排除 ＋ 一条子问题闭合** ⚠️✓）

---

## §0 **定理（本档核心 ✓✓）**

$$\textbf{定理}.\quad \text{设 }C\subseteq\mathbb F_2^n\ (R{=}1)\ \text{covering},\ \text{块 }B\ (|B|{=}m),\ \text{层 }L_\sigma\subseteq\mathbb F_2^{n-m};\ \text{对 }y\in\mathbb F_2^{n-m}:$$
$$\qquad S_y=\{\sigma:y\in L_\sigma\},\quad U_y=\{\sigma:y\in N_1[L_\sigma]\},\quad T_y=N_1[S_y],\quad \delta_y=(m{+}1)|S_y|+|U_y|-2^m$$
$$\qquad \text{若 }\delta_y=0,\ \text{则}\ \boxed{S_y=\varnothing\ \text{（且 }|U_y|=2^m\text{）}}\ ✓✓$$

## §1 **证明（3 行 ✓）**

$$\textbf{(1)}\ \text{引理（既证）}:\ T_y\cup U_y=\mathbb F_2^m\ ✓\ (\text{§}0\ \text{之引理，前档已证})$$
$$\textbf{(2)}\ \text{取等 }\delta_y=0\ \Longrightarrow\ 2^m=|T_y\cup U_y|=|T_y|+|U_y|-|T_y\cap U_y|\ \text{且}\ 2^m=(m{+}1)|S_y|+|U_y|$$
$$\qquad\Longrightarrow\ |T_y|-|T_y\cap U_y|=(m{+}1)|S_y|\ ;\quad \text{又}\ |T_y|=|N_1[S_y]|\le(m{+}1)|S_y|\ \Longrightarrow\ |T_y\cap U_y|=0\ \Longrightarrow\ T_y\cap U_y=\varnothing\ ✓$$
$$\textbf{(3)}\ \text{包含关系（皆初等 ✓）}:\ S_y\subseteq T_y\ (\text{因 }\sigma\in N_1[\sigma])\ ;\quad S_y\subseteq U_y\ (\text{因 }y\in L_\sigma\Rightarrow y\in N_1[L_\sigma])$$
$$\qquad\Longrightarrow\ S_y\subseteq T_y\cap U_y=\varnothing\ \Longrightarrow\ \boxed{S_y=\varnothing}\quad\blacksquare$$

## §2 **推论**

$$\textbf{(i)}\ (1,1)\ \text{型（}m{=}2\text{）\ \textbf{不可能}} ✓✓\ \text{（前档列为“实测不出现、无独立证明”者，今已\ \textbf{证毕}}）;\ \text{更一般：一切 }|S_y|>0\ \text{之取等皆不可能} ✓$$
$$\textbf{(ii)}\ \text{取等之\ \textbf{精确刻画}}:\ \boxed{y\ \text{不属于任何层}\ (S_y{=}\varnothing)\ \text{且与}\ \textbf{每一层} \text{皆距离}\le1\ (|U_y|{=}2^m)}\ ✓\ \text{——与两码六层实测完全一致} ✓$$
$$\textbf{(iii)}\ \text{计数形式}:\ \#\{\text{取等 }y\}\cdot 2^m\ \le\ \sum_\sigma|N_1[L_\sigma]|\ ✓\ \text{（每个取等点对每层贡献恰 1 次“近含” ）}$$

## §3 **诚实：聚合后果仍平凡** ✗

$$\text{由 (iii) 与 }\sum_y\delta_y=(m{+}1)M+\sum_\sigma|N_1[L_\sigma]|-2^n\ (\delta_y\ge1\ \text{于非取等 })\ \text{得}\ 2^{nc}\le (m{+}1)M+2^{nc}\ \Longrightarrow\ \textbf{\text{恒真}} ✗$$
$$\therefore\ \text{定理之力量\ \textbf{仍只在逐点}};\ \text{其\ \textbf{全局化}（“取等刚性无法全局一致”）\ 仍属\ \textbf{研究级}} ✗$$

## §4 **本档之定位（诚实 ✓）**

$$\textbf{已完成}:\ (甲)\ \text{子问题“}(1,1)\ \text{型为何不出现”\ \textbf{已闭合}} ✓✓;\ \text{且原为\ \textbf{实测观察} 者今为\ \textbf{定理}} ✓;\ \text{取等结构获\ \textbf{精确刻画}} ✓$$
$$\textbf{未完成}:\ \text{由该刚性推出 }M\ \text{之新下界（需全局论证）} ✗\ ——\ \text{本线至此为\ \textbf{已定位、未闭合}} ✓$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 取等强制     命中文件数=2    :: RESULT-2026-09-30-tight-per-y-pattern-inequality… ＋ RESULT-2026-09-30-crosslevel-inequalities…
技术词 子问题闭合  命中文件数=1    :: 本档
```

$$\textbf{分类（三项如实 ✓）}:\ \text{(1) }\textbf{本档新增}：\text{“子问题闭合”} ⟹ \text{仅本档} ✓;\quad \text{(2) }\textbf{本会话已有（引用，不列为提出）}：\text{“取等强制”命中本会话前两档} ✗\ \text{故不主张其新性};\quad \text{(3) }\textbf{通用词（不计）}：\text{“闭合／定理”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{定理为 3 行初等证明（可复核 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
