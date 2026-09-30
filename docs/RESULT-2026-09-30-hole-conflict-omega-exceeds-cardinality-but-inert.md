# RESULT-2026-09-30 — **第一刀（唐先生 §9）**：hole-conflict 团数 $\omega(G_H)$ **严格超过基数界**（32/32 ✓✓）但**无杠杆** ✗；近重叠修正版**逐切片近乎紧**（裕度 1–2 ✓）而**聚合不足** ✗

> 空间 B｜非 C 号｜唐先生 20:31 令：**不封 OPEN-B，降级为 OPEN-A 的内部实验对象**；只允许从逐 $\sigma$ 精确集合条件抽取**可符号化局部不等式**；若第一层只还原 $q\le2m$ 型松弛即封死｜**不主张任何新值**（V290）

**已查地图** ✓：`AUDIT-2026-09-30-map-shrinks-to-two-open-mainlines-…`（$I$ 不等式）／`STATE-2026-09-30-block-layer-decomposition…`（精确条件）／L1554
D0: 本档对象 = **精确条件之 hole 结构与两个新量（$\omega(G_H)$、$A$）**（新量 ✓；结论为否 ✗）
D1: 0（产出 = **一条结构性事实 ＋ 一条修正不等式 ＋ 两条量的实测** ⚠️✓）

---

## §0 **对象（照唐先生 §9）**

$$H_\sigma=Q_8\setminus N_1[L_\sigma];\quad \Gamma(x):=\{y:d(x,y)\le1\}\ (|\Gamma|{=}9);\quad \textbf{hole-conflict 图}\ G_H:\ x\sim_H y\iff\Gamma(x)\cap\Gamma(y)=\varnothing\ (\iff d(x,y)\ge3)$$

## §1 **★ 新非基数型量：$\omega(G_H)$ 超过基数界（32/32 ✓✓）**

$$\text{任一覆盖者至多覆盖 }G_H\ \text{中}\ \textbf{团} \text{的 1 个点} \Longrightarrow \gamma_1(H)\ \ge\ \omega(G_H)\ \text{（＝}H\ \text{内两两距离}\ge3\ \text{之最大子集）}$$
| $\|L\|$ | $\|H\|$ | $\|H\|/9$ | $\omega(G_H)$ | $A(\sigma)$ | 精确条件 |
|---|---|---|---|---|---|
| 28 | 49 | 5.44 | **14** | 14 | ✓ |
| 32 | 46 | 5.11 | **14** | 8 | ✓ |
| 28 | 32 | 3.56 | **14** | 28 | ✓ |
| 32 | 34 | 3.78 | **13** | 25 | ✓ |
| 32 | 32 | 3.56 | **12** | 28 | ✓ |

$$\therefore\ \textbf{32/32 切片皆}\ \omega(G_H)>|H|/9,\ \text{超出}\ [7.56,10.78]\ ✓✓\ \Longrightarrow \textbf{\text{确得非基数型量（非 profile、非纯 cardinality）}} ✓$$
$$\textbf{但}:\ m_{\tau_1}+m_{\tau_2}\ (\approx60)\ \ge\ \omega(G_H)\ (\approx14)\ \text{松弛巨大} ✗ \Longrightarrow \textbf{\text{该量无咬合力}} ✗$$

## §2 **近重叠修正版（逐切片近乎紧 ✓）**

$$x\in H_\sigma\Rightarrow d(x,L_\sigma)\ge2\ \Longrightarrow\ L_\tau\cap H_\sigma\subseteq H_\sigma;\quad |L_\tau\cap H_\sigma|=m_\tau-|L_\tau\cap N_1[L_\sigma]|\ \Longrightarrow$$
$$\boxed{|H_\sigma|\ \le\ (m_{\tau_1}+m_{\tau_2})-A(\sigma)},\quad A(\sigma):=|L_{\tau_1}\cap N_1[L_\sigma]|+|L_{\tau_2}\cap N_1[L_\sigma]|\ ✓$$
$$\text{实测}\ A(\sigma)\in[8,28];\ \textbf{\text{逐切片裕度仅 1--2}}:\ (|H|{=}49,A{=}14)\Rightarrow49\le64-14=50 ✓;\ (|H|{=}46,A{=}8)\Rightarrow46\le56-8=48 ✓$$
$$\Longrightarrow\ \textbf{\text{逐切片条件的确近乎紧}} ✓✓\ \text{（即：}\star\ \text{在此层几乎被用尽 ✓）}$$

## §3 **但聚合仍不足** ✗

$$\text{求和}:\ 2^n-\sum_\sigma q_\sigma\ \le\ kM-\sum_\sigma A(\sigma)\ \Longrightarrow\ \sum_\sigma q_\sigma\ \ge\ 2^n-kM+A,\quad A:=\sum_\sigma A(\sigma)\ ✓$$
$$\text{排除 }M{=}106\ \text{需}\ A>142\ (\text{由 }\Sigma q\le9M=954\text{)};\quad \textbf{\text{实测}\ A\approx60} ✗\ \text{（与上轮 }I\le13\text{ 同型结论 ✓）}$$
$$\therefore\ \boxed{\text{逐切片紧、聚合无余量}} ✗\ ——\textbf{\text{第 7 次同型}}（\text{per-point tight},\ \text{aggregate weak}）$$

## §4 **判定（按唐先生 §6／§9 之 STOP 条件）**

$$\text{第一刀\ \textbf{确实} 产出非基数型量（}\omega(G_H)\ \text{与}\ A\ ✓\ \text{，非 profile、非纯 cardinality ✓）},\ \text{但\ \textbf{两者皆无杠杆}} ✗\ (m_{\tau_1}{+}m_{\tau_2}\ge\omega\ \text{松弛巨大};\ \sum A\approx60<142)$$
$$\therefore\ \text{OPEN-B（降级为 BÖW-Auxiliary）\ \textbf{第一层未打通}} ✗;\ \text{其\ \textbf{唯一残余问题}}:\ \textbf{\text{能否给 }A\ \text{一个}>142\ \text{的下界}}（=\text{邻片近重叠之结构下界}）⚠️$$
$$\text{若不能 ⟹ 按令\ \textbf{封死该支线}，只追 BÖW general-state 公式} ✓$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 hole-conflict    命中文件数=1    :: 本档
技术词 近重叠修正  命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“团数／修正”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \omega\ \text{由 ILP 精确求（32 切片 ✓）；}A\ \text{为实测 ✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
