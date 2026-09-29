# SOURCE（2026-09-29）—— **★ 方法源定位：Struik 1994 TU/e 博士论文第 2 章（档案内一直未开）**

> **性质**：**文献定位 ＋ 方法记录**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 20:05 ✓

**已查地图**：`sources/` 全目录（**此前从未按"方法描述"检索**）✓

D0: 本档对象 ＝ **档案已有**（coverig code 下界方法—经典 ✓）
D1: 0（产出＝**一处源定位 ＋ 方法逐字记录 ＋ 我方失误** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ★ 找到"方法描述"型源}:\ \texttt{sources/TUe-covering-codes-chapter-IR425174.pdf}}$$
$$\boxed{\text{② 该源 ＝ M. Struik (1994) TU/e PhD thesis \textbf{《Covering codes》}，123 页，DOI 10.6100/IR425174}}$$
$$\boxed{\text{③ 第 2 章为下界全谱}:\ Johnson／Van Wee／Zhang(\textbf{pair covering inequality})／Spheres\&Hyperplanes／Another Lower Bound}$$
$$\boxed{\text{④ ★ 扩展链已逐字给出}:\ Zhang\ \text{(pair)}\to\ \text{Zhang--Lo Part II (triple)};\ \text{且 BÖW 2004 属同族之再扩展}}$$
$$\boxed{\text{⑤ ⚠️ 我方失误}:\ \text{此档在 }sources/\ \text{内已久};\ \text{我们一直只找"那篇论文"，未按"}\textbf{方法描述}\text{"检索}✗}$$

## §1 章节全貌（✓ 逐字取自目录）

$$2.3\ \text{The Johnson Bound};\quad2.4\ \text{The Van Wee Bound}$$
$$2.5\ \text{An Improvement of the Van Wee Bound for Binary Linear Codes};\quad2.6\ \text{Implications}$$
$$2.7\ \text{The Zhang Bound};\quad2.8\ \text{Intersections of Spheres and Hyperplanes};\quad2.9\ \text{Another Lower Bound}$$
$$\text{第 3 章}:\ \text{covering radius }2/3\ \text{之线性码结构（One/Two-Level Constraints）};\quad\text{第 4 章}:\ \text{构造}$$

## §2 核心公式（✓ 逐字）

$$\textbf{(2.34)}:\ m_0=m_1+\varphi(1),\quad s:=\max\{k\ge1\}\ \text{（下确线之最大斜率）}$$
$$\textbf{(2.35)}:\ |C|\Bigl\{\sum_{i=0}^{t}\tbinom ni-\frac{\tbinom n{r+1}\bigl[\varphi(1)-(n{+}1{-}r)(n{-}r)\bigr]}{s+\varphi(1)}\Bigr\}\ \ge\ 2^n$$
$$\textbf{(2.36)}:\ \varphi(k):=f_C\bigl(n{+}1{-}kr,\ r{+}2,\ 2\bigr)\qquad(f_C=\text{covering design 数})$$
$$\text{逐字}:\ \text{"Equation (2.35) is called the \textbf{pair covering inequality}"};\quad\text{"originally proved by Zhang [89]"}$$
$$\text{逐字}:\ \text{"Both papers generalize methods developed earlier in [84]\ (=van\ Wee)"}$$

## §3 ★ 扩展链（✓ 逐字，关键）

$$\text{Zhang--Lo Part II [91]}:\ \text{以\ \textbf{三元} 替代 (2.30) 型 }\varphi:\quad A_{r+2}+A_{r+3}\ \ge\ \varphi\bigl(A_{r-2}+A_{r-1},\ A_r+A_{r+1}\bigr)$$
$$\therefore\ \textbf{族谱}:\ \text{van Wee (1988)}\to\text{Zhang pair (1991)}\to\text{Zhang--Lo triple (1992)}\to\text{Habsieger (1995/97)}\to\text{Habsieger--Plagne (2000)}\to\text{BÖW (2004)}$$
$$\text{与档案此前锁定之阶梯一致}:\ 103\to105\to107✓$$

## §4 诚实标注（⚠️）

$$\text{（甲）本档\ \textbf{未}解决 107};\ \text{它解决的是"方法}\textbf{在哪、长什么样}"✗$$
$$\text{（乙）该论著针对 }t[n,k]\ (\text{线性码})，与 }K(n,1)\ (\text{一般码})\ \text{接口待接}⚠️$$
$$\text{（丙）}sources/\ \text{内还有 }Haas2008\ \text{(excess method)}、CKMS1985、Graham-Sloane1985、Keri\ \text{史}\ ——\ \textbf{均未按方法检索}✗$$

## §5 边界（硬 ✓）

- **全部为文献定位与逐字摘录（含页码/公式号）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；**本方失误已如实记录** ✓

## §6 【技术词回查】（**提交前实跑，逐字粘贴**）

```
方法源定位 : 技术词 方法源定位    命中文件数=0    ::
pair covering inequality : 技术词 pair covering inequality 命中文件数=3    :: ./ASSETS-REGISTRY.md ./AUDIT-2026-09-28ac-moment-identities-verified-and-the-upstream-bound-gap.md ./AUDIT-2026-09-28z-K10-1-lower-bound-provenance-chain-locked.md
Struik论文 : 技术词 Struik论文   命中文件数=0    ::
```


---

## §7 ⚠️ 勘误（2026-09-29 20:08，自查）

$$\textbf{错误}:\ \S6\ \text{曾写 "pair covering inequality 命中 0"}✗\ \text{—— 属"先写后跑"违规（我预填了 }0\text{）}$$
$$\textbf{真值}:\ \text{命中数 }=\mathbf 3\ (\text{ASSETS-REGISTRY ＋ AUDIT-28ac ＋ AUDIT-28z，皆\ \textbf{本线已有}})✓$$
$$\therefore\ \text{该词应归入\ \textbf{"档案已有（引用，不列为提出）"}};\ \text{本档之新性仅在于"}"{方法源}\to\text{档案}"\text{这一条定位}$$
$$\text{（\S6 已按真值更正；教训与 TOOLS.md "先跑后写" 门一致）}$$
