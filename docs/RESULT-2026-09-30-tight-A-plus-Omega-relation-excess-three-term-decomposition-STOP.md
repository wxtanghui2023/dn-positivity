# RESULT-2026-09-30 — **最后一击**：紧关系 $A+\Omega\le E$（松弛 0–10、**0 可达** ✓✓）⟹ **excess 三项分解**；但仍**不能排除 106** ✗ ⟹ **按令封线** ✓

> 空间 B｜非 C 号｜唐先生 20:35「继续」（攻 $A$ 下界＝该支线最后出口）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-hole-conflict-omega-exceeds-cardinality-but-inert`（$A(\sigma)$、$\omega(G_H)$）／`AUDIT-2026-09-30-map-shrinks-to-two-open-mainlines-…`（$I$）／`STATE-2026-09-30-block-layer-decomposition…`
D0: 本档对象 = **新关系式（$A+\Omega\le E$）与 excess 三分解**（新 ✓）
D1: 0（产出 = **一条紧关系 ＋ 一条分解 ＋ 一条封线判定** ⚠️✓）

---

## §0 **推导（链式 ✓）**

$$\text{精确条件}:H_\sigma\subseteq L_{\tau_1}\cup L_{\tau_2}\ \Longrightarrow\ |H_\sigma|\le\sum_i|L_{\tau_i}\cap H_\sigma|\ \Longrightarrow\ |H_\sigma|\le(m_{\tau_1}+m_{\tau_2})-A(\sigma),\ A(\sigma):=\sum_i|L_{\tau_i}\cap N_1[L_\sigma]|$$
$$\text{求和（}\Sigma_\sigma\Sigma_{\tau\sim\sigma}m_\tau=kM,\ \Sigma_\sigma|H_\sigma|=2^n-\Sigma_\sigma q_\sigma\text{）}:\ 2^n-\Sigma q\ \le\ kM-A\ \Longrightarrow\ A\ \le\ kM-2^n+\Sigma q$$
$$\Longrightarrow\ \boxed{A+\Omega\ \le\ E},\qquad \Omega:=9M-\Sigma_\sigma q_\sigma,\quad E=11M-2^n\ ✓\quad(\text{等价于 }A+\Omega=E-\text{slack},\ \text{slack}\ge0)$$

## §1 **实测（120-码，全部 45 个 split ✓✓）**

$$\textbf{违反 }A+\Omega\le E\ \text{之 split 数}=\mathbf{0/45}\ ✓✓;\quad A+\Omega\in[286,\mathbf{296}]\ \text{vs}\ E=296;\quad \textbf{松弛}\in[0,\mathbf{10}],\ \textbf{且 0 可达} ✓✓$$
$$A\in[44,143];\quad \Omega\in[147,246];\quad \text{slack}=E-(A+\Omega)=(kM-A)-(2^n-\Sigma q)\ (\text{并集界之余量}\ ✓)$$
$$\therefore\ \boxed{E\ =\ \underbrace{A}_{\text{跨片“近重叠”浪费}}\ +\ \underbrace{\Omega}_{\text{片内重叠亏损}}\ +\ \underbrace{\text{slack}}_{\text{hole 恰一次覆盖之余量}}}\ ✓✓\ \text{——}\textbf{\text{excess 的三项分解（本档新）}}$$

## §2 **但方向不对（诚实 ✗）**

$$\text{排除 }M{=}106\ \text{需}\ A+\Omega>\mathbf{142};\quad \text{而该式给的是\ \textbf{上界} }A+\Omega\le E\ ✗$$
$$\text{可证下界}:\ A\ge0\ (\text{显然});\ \Omega=9M-\Sigma q\ge0;\ \text{更细者（由 }A(8,3){=}20\text{）：}\Omega\ \gtrsim\ (M-4\cdot20)/9\approx3\ ✗\ \text{——远不足 142}$$
$$\therefore\ \text{支线之最后出口（}A\ \text{之}>142\ \text{下界}）\ \textbf{\text{不可得}} ✗;\ \text{且该式在真码上\ \textbf{近饱和（}A+\Omega\approx E\text{）}} ⟹ \textbf{\text{不含可用余量}} ✗$$

## §3 **判定：按令封线** ✓（OPEN-B／BÖW-Auxiliary）

$$\textbf{净收获（保留 ✓）}:\ \text{(i) 紧关系 }A+\Omega\le E\ \text{（真码上松弛 0--10、0 可达 ✓✓）};\ \text{(ii) excess 三分解 }E=A+\Omega+\text{slack};\ \text{(iii) }\omega(G_H)>|H|/9\ \text{（32/32 ✓）};\ \text{(iv) }A(\sigma)\in[8,28]\ \text{与近重叠修正式}$$
$$\textbf{净不足（✗）}:\ \text{无任何} >142\ \text{之下界};\ \text{一切可及推论在真码处近饱和} ⟹ \textbf{\text{第 8 次同型（逐点紧/聚合饱和）}}$$
$$\therefore\ \text{按唐先生 §6／§9 之令}:\ \textbf{\text{封死 BÖW-Auxiliary 支线}} ✓;\ \text{研究地图只剩}\ \textbf{\text{OPEN-A}}（\text{BÖW general-state 公式}）✗\ ——\ \text{其获取需外部正文（不在手 ✗）} ✓$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 三项分解     命中文件数=8    :: ./V181-… ./LEDGER-119-2026-09-27-… ./V180-…
技术词 封线判定     命中文件数=1    :: 本档
```

$$\textbf{分类（AMEND-27）}:\ \textbf{本档新增}：\text{“封线判定”仅本档} ✓;\quad \textbf{空间 A／他线同名（不计 ✗）}：\text{“三项分解”命中 8 档（V181、V180 属空间 A；LEDGER-119 属 119 线）} \not\Rightarrow \text{新性};\quad \textbf{通用词（不计）}：\text{“分解／松弛”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{关系式 45/45 实测核验 ✓；方向与不足如实报告 ✗};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
