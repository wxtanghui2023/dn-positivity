# ASSESS-2026-09-29-SCALE — 「$n{=}10$ 极值分类计算」之**可行性规模评估**（结论：**不可行**）

> 空间 B｜非 C 号｜唐先生 23:38「继续」（要我先估成本再定做不做）｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:38（本机 00:3x）

**已查地图**：本会话 `INV1–INV5`／`INV4` §2（通用界对照）／`AUDIT-28q`（公式链）／`AUDIT-28ab`（历史更正：Habsieger 104）
D0: 本档对象 = **档案已有**（$K(n,1)$ 阶梯／分类法）之**成本量级**（新数学对象：无 ✗）
D1: 0（产出 = **三个量级 ＋ 一条可行性判定** ⚠️✓）

---

## §0 判定（先给）

$$\boxed{\text{「重做一线 }n{=}10\text{ 极值分类」在我方资源下\ \textbf{不可行}}:\ \text{穷举 }10^{147};\ \text{聚合案例 }8.4\times10^{7}\ \text{（每案例再现空间天文）};\ \text{松弛天花板 }105.2223}$$
$$\therefore\ \text{复现 }107\ \text{既不能靠穷举、也不能靠松弛};\ \text{只能靠\ \textbf{n-专属结构性定理}（五轮未现）}}$$

## §1 量级 1：穷举搜索空间

$$\#\{\text{码}\subseteq Q_{10},\ |C|\le106\}\ \approx\ \binom{1024}{106}\ =\ 10^{\mathbf{146.6}} \Longrightarrow \textbf{不可行}\ ✗$$

## §2 量级 2：聚合层（excess 分布）案例数

$$\Sigma\delta=11\cdot106-1024=142;\quad \text{把 142 个 excess 单位分给 1024 点（每点 }\le10\text{）}$$
$$\#\{\text{μ-剖面}\}\ =\ p_{\le10}(142)\ =\ \mathbf{84{,}218{,}903}\ \approx\ 10^{7.9}\ \Longrightarrow\ \textbf{案例列表本身已过大}\ ✗$$
$$\qquad\text{（且每案例仍含天文级"具体构型实现" ⟹ 总量级＝上述二者之积）}$$

## §3 量级 3：松弛/我方天花板（**阶梯全表**）

| 层 | 值 | 状态 |
|---|---|---|
| 球界（线性） | 93.09 | 自推 ✓ |
| **我方聚合/谱类最强** | **95** | 自达标定（连 $n{=}9$ 的 $M{=}61$ 都判可行） |
| van Wee 1988 | 102.4 → **103** | 自推 ✓（原式逐字） |
| Habsieger 1997 | 104 | 未复现（档案历史更正） |
| Zhang 1991/92 | 105 | 我方复现只到 103 |
| **SDP-3（Gijswijt–Polak 2025）** | 105.2223 → **106** | **我方已达 ✓（引用值）** |
| **BÖW 2004** | **107** | **目标；源不可得；五轮反解未果** |

$$\therefore\ \text{缺口 }106\to107\ \text{落在\ \textbf{整性} 里};\ \text{而整性之可行手段仅二：}\textbf{分类}（§1/§2 皆不可行）\ \text{或}\ \textbf{新定理}（未现）$$

## §4 附带：前五轮已排除之族（**不重复投入**）

$$\text{同余律（INV1）｜公式细节（INV2）｜parity/深层同余（INV3）｜}\gamma_2\text{ 约化（INV4/5）｜切片交叉（INV5）｜机制 C }\ge3\text{ 阶｜owner-conditioned 规则｜B-P1 碰撞｜D/E 紧量（四次）}$$

## §5 建议（**待唐先生定**）

$$\textbf{(甲) 收束归档（推荐）}:\ \text{保留 }K(10,1)\ge\mathbf{106}\ (\text{可复现});\ 107\ \text{记为"需 }n\text{-专属论证/计算"};\ \text{工具与九条 kill 全部入册} ✓$$
$$\textbf{(乙) 若仍要在无源条件下逼近 }107:\ \text{唯一未撞之墙＝找一个\ \textbf{n-专属结构定理};\ \text{但本晚五轮 ＋ 档案长史皆未现 ⟹ 期望值极低} ⚠️$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**成本评估**（不产生数学结果）✓
- 未取论文原文（R16–17）；未重攻已 kill 之族 ✓；未碰 RH ✓


## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "极值分类" "成本量级" "规模评估" "n-专属论证" "可行性规模"
技术词 极值分类     命中文件数=4    :: ./ASSESS-2026-09-29-SCALE-....md ./S2-BATCH-4-record-and-pool-reconciliation.md ./S2-30-PASS-1-record-and-partial-subtypes.md
技术词 成本量级     命中文件数=2    :: ./ASSESS-2026-09-29-SCALE-....md ./C271-M5-half-budget-not-closed-formal-record-and-failure-mode-precise-diagnosis.md
技术词 规模评估     命中文件数=1    :: ./ASSESS-2026-09-29-SCALE-....md
技术词 n-专属论证   命中文件数=1    :: ./RESULT-2026-09-29-INV4-slicing-lemma-reduces-K101-to-a-two-set-covering-in-Q9.md
技术词 可行性规模   命中文件数=1    :: ./ASSESS-2026-09-29-SCALE-....md
```

$$\text{分类}:\quad
\textbf{本档新增} = \varnothing;\quad
\textbf{档案已有（引用，不列为提出）} = \{\text{极值分类（}S2\text{-BATCH-4}／S2\text{-30-PASS-1}）,\ \text{成本量级（}C271\text{-M5}）\};\quad
\textbf{本晚已用} = \{n\text{-专属论证}（INV4）\}$$
$$\textbf{通用词（不计）} = \{\text{规模评估},\ \text{可行性规模}\} \Longrightarrow \textbf{本档不主张任何技术词首次命名} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
