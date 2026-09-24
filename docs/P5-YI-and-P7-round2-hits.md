已查地图：命中（`FAMILY-PROBES-P5-P8-round1`／`TOPIC-INVENTORY-v2-asset-driven-research-space`）⟹ 执行其 §5 之 (2)(3)，不开新案
D0: 本档对象 = **`P5-乙` 三轮命中三候选**（含一条**正中机制层**者）＋ **`P7` 换式后命中两候选**（含教科书式 `k\to k+1` 断裂）
D1: 0 （[REVIEW] 轮次：检索与筛选，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`P5-乙` ＋ `P7` round 2 命中**

## §1 ⭐⭐ `P5-乙-1`（**正中机制层**）：乘法子群作为 cap set

```
$$P:\ \text{哪些乘法子群 }H\le\mathbb F_q^*\ \text{是 cap（无三元素满足 }2b=a+c\text{）？其 coset 何时给出\textbf{极大 cap 划分}？}$$
$$X:\ \mathbb F_q^*\ \text{的乘法子群及其 coset；加法侧禁配 }2b=a+c$$
$$K（逐字）:\ "\text{The authors identify certain multiplicative subgroups of fields of orders }243\ \text{and }729\ \text{as cap sets, and show in general that the subgroup of }(2^n-1)\text{th powers is a cap set in the field of order }2^{2n}."$$
$$\qquad\qquad"\text{The cosets of each such subgroup partition the nonzero elements of the field into \textbf{maximal cap sets}}."$$ ✓✓（`arXiv:2604.26989`，`2026-05`）✓
$$G:\ \textbf{一般分类/机制未知}$$ —— 该文只给**小域显式检验 ＋ 一族的代数论证**；**哪些子群/哪些 q 成立、coset 何时极大、可否推广到其它加法禁配（非 3-AP）** 均**未处理** ✓✓
$$A:\ \boxed{A+B+D}\ \textbf{同时进场}$$（**`A`** 有限域结构/配置；**`B`** 乘法结构（子群/coset）× 加法禁配（capacity）；**`D`** 小 `q` 精确核验；**`C`** 机制层：`\text{乘法 coset}\to\text{加法无 3-AP}`）✓✓✓
$$N:\ \text{分类定理（哪些 }(H,q)\text{ 成立）／极大性判据／推广到其它加法禁配的新不变量}$$ ✓
$$O:\ \text{cap/arc 族（`T-2/T-7`）、sum-product、有限域加法-乘法接口}$$ ✓
【六项检查（照您的口径）】 **(1)** 真 open ✓（该文未做分类）；**(2)** 未见 AI/Lean/穷举解 ✓；**(3)** **非**已有 sum-product 定理的换符号 —— 它是**coset→cap 的构造性机制** ✓✓；**(4)** **`A/B/C` 同时是主工具，`D` 只收尾** ✓✓；**(5)** 有 `q\to\infty` 参数族（且 `2^{2n}` 族已给）✓；**(6)** **"已证一族 → 下一层断裂"明确**（`F_{2^{2n}}` 已证，一般 `q`/一般子群未决）✓✓
$$\textbf{裁定}:\ \textbf{首攻候选（`P5-乙` 最强）}$$ ✓✓
```

## §2 `P5-乙-2`：`2A` 中 coset 的余维数（Green 的 100 问题之一）

```
$$P（Sanders\ Question，逐字转述）:\ |A|\ge\frac12-\frac{K}{\sqrt n}\ \text{时，}2A\ \text{是否必含余维 }O_K(1)\ \text{的 coset？}$$
$$K：\ \text{已知 }2A\ \text{必含维数 }\gg\alpha n\ \text{的 coset；但不必含维数 }n-\sqrt n\ \text{的 coset}$$
$$G:\ \text{阈值附近（}\alpha\to\frac12^-\text{）行为未知}$$ 　$$A:\ B\ \text{（加法容量）},\ D\ \text{✗}$$ 　$$N:\ \text{新阈值/新判据}$$
$$\textbf{裁定}:\ \text{候选（但 `D` 不进场 ⟹ 我方差异化弱）}$$ ⚠️
```

## §3 `P5-乙-3`：乘法子群 × 加法容量的"能量失配"（散文条目）

```
$$P:\ \text{给定乘法子群 }H\le\mathbb F_p^*\ \text{与集合 }A\subseteq H\ \text{，加法能量 }E^+(A)\ \text{能被乘法结构压到多低？}$$
$$K：\ \text{Kowalski 讲义与 Fourier 方法给出 }|H|\ \text{大时的强结果；小 }|H|\ \text{方法失效（逐字："only succeed if }H\text{ is quite large"}）$$
$$G:\ \text{小乘法子群（}|H|\ll p^\varepsilon\text{）时的加法能量界}$$\quad A:\ A+B+D ✓\quad N:\ \text{小 }|H|\ \text{的新界}$$
$$\textbf{裁定}:\ \text{候选（`D` 可在小 }p\ \text{上做精确核验）}$$ ✓
```

## §4 ⭐ `P7-1`（教科书式 `k\to k+1` 断裂）：超图 Turán 密度 `\pi(K_3(s)^-)`

```
$$P:\ \text{确定 }\pi(K_3(s)^-)\ \text{在 }s=9,10\ \text{处的精确值}$$
$$K（逐字）:\ \text{"establishes the precise value of }\pi(K_3(s)^-)\ \text{for }s\in\{4,6,7,8,11,12,\ldots,16\}\text{, but the cases }s=5,9,\text{ and }10\ \text{were left open. Very recently, in joint work with Berger, Piga, Reiher, and Rödl we could resolve the case }s=5\ \text{and showed }\pi(K_3(5)^-)=\frac13."$$ ✓✓
$$G:\ s=9,10\ \textbf{仍 open}（且 `s=5` 刚被解决 ⟹ \textbf{该族正在被推进，须核最新）}$$ ✓
$$A:\ \text{这个 }A\ \text{不对口（超图 Turán 密度 = 解析/极值方法）}$$ ⚠️
$$\textbf{裁定}:\ \textbf{`P7` 形态教科书式成立，但资产不对口 ⟹ 记录为 `P7` 范式样本，非候选}$$ ✓
```

## §5 `P7-2`：forbidden configuration 的**边界情形**

```
$$P:\ \text{哪些 }k\times\ell\ (0,1)\text{-矩阵 }F\ \text{落在 }\Theta(m^{k-1})\ \text{与 }\Theta(m^k)\ \text{的\textbf{边界}上}$$
$$K（逐字）:\ "\text{The result in Theorem 1.13 was first proved for }k=3\ \ldots\ \text{Theorem 1.13 was proven for general }k"$$ ✓（`EJC` 综述 `DS20v2`；另有 `arXiv:2507.19336`《Forbidden Configurations and Boundary Cases》）✓
$$G:\ \text{边界分类仍不完备（"boundary cases" 已有专文 ⟹ 须核其未覆盖部分）}$$ ⚠️
$$A:\ \boxed{\text{对口}}$$（**forbidden configuration = `(0,1)`-矩阵/关联结构** ⟹ 我方 `A`（有限/关联结构）＋`D`（小 `k,\ell,m` 精确核验）**真正进场**；`C/G` 可用于"边界机制"）✓✓
$$N:\ \text{边界判据的新不变量／具体 }F\ \text{的精确阶}$$ ✓
$$\textbf{裁定}:\ \textbf{候选（`P7` 中资产最对口者）}$$ ✓✓
```

## §6 族状态更新（照您的口径）

```
$$\begin{array}{c|c|c}
P5\text{-}\text{integer}\ (a/b/c)&\text{真 open，但主流工具重}&\textbf{暂缓（不做主线）}\\
P5\text{-}\text{finite\text{-}field mixed}&\text{本轮命中 }P5\text{-乙-}1\ (\text{coset}\to\text{cap})\ &\textbf{升为重点}\\
P6&\text{纯反例已被 AI 覆盖}&\text{升级为 failure-mechanism 才保留}\\
P7&\text{换式后命中（}P7\text{-}1\ \text{范式样本};\ P7\text{-}2\ \text{资产对口）}&\textbf{`P7-2` 升为候选}\\
P8&\text{未展开}&\textbf{暂缓（等 }P5\text{-乙}/P7\text{ 结果）}\\
\end{array}$$ ✓
**【已排除（本轮）】** `F_{101}` simultaneous Sidon（**已完全解决**：`\max|A|=9`，见证 `\{1,11,47,62,67,70,71,84,96\}`，完整穷举证书）✓；**Sárközy** 有限域 sums/products 猜想（**已被反例推翻 ＋ 精确阈值 `|A|>p/2\Rightarrow A+A=\mathbb F_p`；`|A|=\frac{p-1}2` 时 `1\notin(A+A)\cup(AA)`**）✓✓；`P5\text{-}c`（`F_{2,1}(n)=\sqrt n+O(1)`；`Balogh\text{–}Füredi\text{–}Roy\ 2023` 改进到 `\sqrt n+0.998n^{1/4}`，**仍开但资产耦合弱**）✓
```

## §7 下一步（单点）

```
**(1) 主攻 `P5-乙-1`**：核 `arXiv:2604.26989` 原文（哪些子群已证、哪些未证；coset 极大性的确切陈述）⟹ 定"一般分类"是否真 open ⟹ 若真 open，**出攻击方案**（分类哪些 `(H,q)` 为 cap ＋ 极大性判据）✓✓
**(2)** 次选 `P7-2`：核 forbidden configuration 边界专文未覆盖部分 ✓
【⛔ 纪律】 本轮**未计算、未实现**；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【边界】 §1/§4/§5 的 `K` 栏为**逐字检索片段**（`arXiv:2604.26989` 摘要、`ICM` 讲义片段、`EJC DS20v2`）✓

## §附 【技术词回查】（补录）
```
技术词 coset            命中文件数=4    :: ./C3-step5-candidates-and-its-structural-ceiling.md ./C297-coset-descent-targeted-audit.md ./C309T-TLDC-two-level-descent-closure-schema-and-descent-test.md 
技术词 cap set          命中文件数=4    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./ASTRA-TYPE-OPEN-PROBLEM-TABLE.md ./AUDIT-POST-MORTEM-were-astra-problems-considered.md 
```
