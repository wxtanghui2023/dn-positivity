# AUDIT-2026-09-30 — 研究地图收缩为 **两条主线**（OPEN-A／OPEN-B）＋ **新集合级不等式**（含新量 $I$）＋ **A↔B 对齐** ✓

> 空间 B｜非 C 号｜唐先生 20:29 全盘审计（来源→方法族→对象层级→已用信息→是否闭合→是否含 107）｜**不主张任何新值**（V290）

**已查地图** ✓：`ANALYSIS-2026-09-30-Keri-thesis-systematic-rescan…`／`AUDIT-2026-09-30-linear-inequality-route-…-STOP`／`RESULT-2026-09-30-PMER-stop-proved…`／`RESULT-2026-09-30-sqr-census…`／MASTER-FAILURE-MAP-107-LINE
D0: 本档对象 = **地图收缩登记 ＋ 一条新不等式（集合级）＋ 一次对齐**（新不等式 ✓）
D1: 0（产出 = **收缩地图 ＋ 新不等式 ＋ 对齐诊断** ⚠️✓）

---

## §0 **收缩后的地图（照录唐先生 §XVII–XIX ✓）**

$$\textbf{STOP（旧门，一律不再开）}:\ \text{sphere};\ \text{Delsarte LP};\ \text{van Wee};\ \text{Habsieger/Plagne};\ \text{Haas};\ \text{Zhang};\ \text{induced }Z{+}FM;\ \text{SDP-3};\ \text{Walsh/Fourier};\ \text{parity};\ Q_9\ \text{fiber profile};\ \text{PMER profile};\ \text{fixed }I{=}(10,40,4);\ \text{deletion/2-for-1};\ \text{ownership/private}$$
$$\textbf{OPEN-A}:\ \text{BÖW-2004 真实机制（general }R{=}1\ \text{bound，含计算型成分 ⚠️}）;\qquad \textbf{OPEN-B}:\ \text{residual set compatibility（集合级）}$$
$$\text{重要地图修正（唐先生 §XIX①）}:\ \text{BÖW-107 很可能\ \textbf{不是单一标量不等式}，而是\ \textbf{一般理论 ＋ 有限维局部状态 ＋ 计算/枚举}} ✓$$

## §1 **A ↔ B 之对齐（本档 ✓）**

$$\text{共同结构}:\ \text{两者皆＝}\boxed{\text{局部状态（子空间内 codeword 分布）}\ +\ \text{跨子空间补覆盖}} ✓✓\ ——\text{我方 }L_\sigma\ \text{即“子空间内分布”；}\Delta_\sigma\subseteq\bigcup_{\tau\sim\sigma}L_\tau\ \text{即“跨子空间补覆盖”} ✓$$
$$\text{分工之差别}:\ \text{(i) 作为\ \textbf{计算方法} → 规模墙（我方已\ \textbf{证明}：PMER 影子}=F_k\ \text{✗；坐标机器 }n{=}6\ \text{已超时 ✗）};\ \text{(ii) 作为\ \textbf{一般界} → 这才是 107 之出处 ✓，而它\ \textbf{不可得} ✗}$$
$$\therefore\ \boxed{\text{缺口不在“结构”（我方已有 ✓），而在同一结构的\ \textbf{符号化/一般化形式}（以 }M\ \text{及混合参数 }(b,t)\ \text{表述，而非枚举）}} ✓✓$$

## §2 **新集合级不等式（本档推导 ＋ 实测 ✓✓）**

$$\text{demand-capacity（利用“同一 }x\ \text{被多方要求”之冲突 ✓）}:\ \sum_\sigma|\Delta_\sigma|\ \le\ \sum_\sigma\Big|\bigcup_{\tau\sim\sigma}L_\tau\Big|\ \le\ \sum_\sigma\Big(\sum_{\tau\sim\sigma}m_\tau-\big|L_{\tau_1(\sigma)}\cap L_{\tau_2(\sigma)}\big|\Big)$$
$$\qquad\text{（第二式＝}\textbf{\text{并集次可加}}：两邻切片之\ \textbf{交集} 是被重复计算的容量 ✓）$$
$$k{=}2\ \text{时}:\ \sum_\sigma|L_{\tau_1}\cap L_{\tau_2}|=2I,\quad I:=|L_{00}\cap L_{11}|+|L_{01}\cap L_{10}|\ (\textbf{\text{对径切片之交}} ✓)$$
$$\Longrightarrow\ 2^n-\sum_\sigma q_\sigma\ \le\ kM-2I\quad\text{即}\quad\boxed{\sum_\sigma q_\sigma\ \ge\ 2^n-kM+2I}\ ✓✓$$
$$\textbf{实测（120-码，全部 }C(10,2){=}45\ \text{个 split）}:\ \textbf{\text{违反数 0/45}} ✓;\ \text{松弛 }(kM{-}2I)-(2^n{-}\Sigma q)\in[40,137];\ \Sigma q\in[834,933];\ \mathbf{I\in[0,13]}$$

## §3 **判定：该形式\ \textbf{量级不足}** ✗（诚实）

$$\text{排除 }M{=}106\ \text{需}:\ 812+2I\ >\ 954\ \text{（}\Sigma q\le9M\text{）}\ \Longrightarrow\ I>71;\quad \textbf{\text{实测 }I\le13} ✗\ \text{（相差 5 倍以上）}$$
$$\text{原因（可诊断 ✓）}:\ I\ \text{≈ 近随机水平（两切片各约 28–32 词于 256 点空间中，随机期望交 }28\cdot28/256\approx3\text{）} ⟹ \textbf{\text{对径切片几乎不交}} ✗ \Longrightarrow \text{冲突项}\ 2I\ \text{结构性偏小} ⚠️$$
$$\therefore\ \boxed{\text{OPEN-B 之\ \textbf{聚合形式}（含冲突修正）亦不足}} ✗;\ \text{唯一未耗者＝\ \textbf{逐 }\sigma\ \text{之精确集合条件}（松弛仅 10–15 ✓）}}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 地图收缩     命中文件数=1    :: 本档
技术词 对径切片     命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“收缩／切片”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{新不等式经 45/45 实测核验 ✓；}I\ \text{之量级如实报告 ✗};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
