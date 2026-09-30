# RESULT-2026-09-30 — 逐坐标构造机器**实现并校准通过 ✓✓**（首次以"穷举空集"证下界）；但**朴素标度爆炸** ✗（n≥7 不可行）

> 空间 B｜非 C 号｜唐先生 16:39「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 17:2x

**已查地图** ✓：`COMPARE-2026-09-30`（五维对比）／`FINGERPRINT-2026-09-30`（Kéri 第 9 章机理）／L3012（未做者 `Layer 2+`）
D0: 本档对象 = **档案已有**（Kéri Ch.9 机理）之**首个实现与校准**（新数学对象：无 ✗；新工具：`scripts/coord_search.py` ✓）
D1: 0（产出 = **一条实现验收 ＋ 一组标度数据 ＋ 一条可行性判定** ⚠️✓）

---

## §0 **实现验收（校准真值 ✓✓）**

| (n, M) | 真值 | 机器判定 | nodes | 用时 | 结论 |
|---|---|---|---|---|---|
| (4,3) | $K(4,1){=}4$ | **NO COVER ⟹ $K>3$** | 2 | 0.0 s | ✓ 正确（负对照） |
| (4,4) | 同上 | **COVER FOUND** | 87 | 0.0 s | ✓ **正对照通过** |
| (5,6) | $K(5,1){=}7$ | **NO COVER ⟹ $K>6$** | 264 | 0.3 s | ✓ 正确（负对照） |
| (5,7) | 同上 | **COVER FOUND** | 3205 | 4.9 s | ✓ **正对照通过** |
| (6,11) | $K(6,1){=}12$ | **TIMEOUT** ✗ | ≥65\,682 | 100 s | ✗ 未完成 |

$$\textbf{判定}:\ \boxed{\text{机器\ \textbf{可用}：以"穷举空集"证明下界}\ ✓✓\ ——\ \text{这是我方工具箱\ \textbf{第一次} 具备"非松弛"证书能力}}$$
$$\qquad(\text{正对照亦通过 ⟹ 机器\ \textbf{不会误报"无解"}} ✓✓\ ——\ \text{此点极关键})$$

## §1 ⚠️ **过程中的两个自查（纪律 ✓）**

$$\textbf{(i) 不健全剪枝（已修 ✓）}:\ \text{首版按\ \textbf{不同前缀} 计数} ✗\ ——\ \text{但\ \textbf{同前缀之不同码字} 延拓后覆盖\ \textbf{不同} 纤维部分}$$
$$\qquad\Longrightarrow\ \text{应以\ \textbf{重数} 计（}\text{union}\le\sum_{\text{码字}}\text{球}\ \text{方为健全上界}\ ✓）\ \text{否则会剪掉合法构型} ✗$$
$$\textbf{(ii) 该 bug 之发现途径 ✓}:\ n{=}5\ \text{首跑回报\ \textbf{"0 nodes"}} \Longrightarrow\ \text{结果荒谬} \Longrightarrow\ \text{即刻自查定位} ✓\ (\text{若不查即报，将得"K(5,1)>6"之\ \textbf{错误理由}} ⚠️)$$

## §2 **标度数据（可行性的答案 ✓）**

$$\text{nodes}: (4,3)=2;\ (5,6)=264;\ (6,11)\ge 65\,682\ (\text{未完成}) \Longrightarrow\ \textbf{每加一维约 ×130–250}\ ⚠️$$
$$\text{(6,11) 之分层状态数}: 1{:}2,\ 2{:}12,\ 3{:}343,\ 4{:}4151,\ 5{:}15252,\ 6{:}45922\ \text{（末层仍在增长 ✗）}$$
$$\therefore\ \boxed{\text{朴素外推}:\ n{=}7\sim10^7,\ n{=}8\sim10^9,\ n{=}9\sim10^{11},\ n{=}10\sim10^{13}\ ✗\ ——\ \textbf{且真目标之 }M\ \text{更大}（n{=}10\ \text{时 }M{\approx}106）\ ⟹ \text{远超可行}}$$
$$\text{另注}:\ \text{本实作只用\ \textbf{弱剪枝}（体积上界＋重数 ✓）与\ \textbf{弱同构约化}（}k\le5\ \text{全排列，}k{>}5\ \text{退化为排序 ✗）} \Longrightarrow \text{并非该法之最优形} ⚠️$$

## §3 **结论与下一步**

$$\boxed{\text{方向\ \textbf{原理上已验收}} ✓✓;\ \text{但\ \textbf{朴素实现不足以达 }n{=}10}\ ✗\ ——\ \text{与档案旧判（}n{=}10\ \text{状态爆炸}）一致 ✓}$$
$$\text{2004 年成功所需之工程}:\ \text{(a) }\textbf{\text{更强剪枝}}\ (\text{非仅体积界});\ \text{(b) }\textbf{\text{工业级同构约化}}\ (\text{nauty 型 canon});\ \text{(c) }\textbf{\text{归约}}\ ——\ \text{把 }M{=}106\ \text{之二元情形化归\ \textbf{小 }M\ \text{之混合 }(t,b;R)\ \text{情形}} ⚠️$$
$$\textbf{下一步（最便宜且最有信息量 ✓）}:\ \text{继续掘 Kéri\ \textbf{第 9 章}}（\text{逐步不等式之更强形、canon 手法、大 }M\ \text{之处置}\ ✓\ ——\ \text{我们持有全文} ✓）\ \text{而非先加大算力} ✗$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 穷举空集     命中文件数=1    :: 本档
技术词 标度爆炸     命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \text{两词仅本档命中} \Longrightarrow \textbf{本档新增} ✓;\quad \text{“标度爆炸”为首次命名 ✓}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓;\quad \text{通用词（不计）}:\ \text{“剪枝／上界”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓;\ \textbf{(D3)}\ \text{两处自查已录（不健全剪枝、0-nodes 荒谬判）} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
