已查地图：命中（`RESEARCH-CONSTITUTION` AMEND-27 空间 B ＋ `LJCR-A5-difference-sets-source-check.md` 目标锁定）⟹ 本档 = `B-LJCR-1` 收口 ＋ 批量 E4 审计
D0: 本档对象 = **`DS(243,121,60,[3,9,9])` 判 `No`**（双源定理）＋ **批量闭包审计**（同一上位定理一次判掉 74 格）
D1: 0（核验/状态纠正型；**无**新定理、**无**新构造、**无**新计算证书）
[REVIEW]

# **`B-LJCR-1` 收口：上位定理闭包命中 ＋ 批量审计**

## §1 定理（**双源逐字**）

**源①** —— B. Schmidt, *Difference Sets: an Update*（NTU 综述）**Theorem 4.4**：
> *“Let G be an abelian p-group, where p is a prime with p ≡ 3 mod 4, and write |G| = p^m, exp(G) = p^s. If G admits a skew Paley-Hadamard difference set and s ≥ 2, then s ≤ (m+1)/4.”*
> —— 并附：*“shows that Conjecture 4.3 is true for m ≤ 5”*

**源②** —— C. Ding, Z. Wang, Q. Xiang, *JCTA* **114** (2007) 867–887，**Theorem 1.1**（逐字）：
> *“Let D be a (v,k,λ) skew Hadamard difference set in an abelian group G. Then v is equal to a prime power p^m ≡ 3 (mod 4), and the quadratic residues modulo v are multipliers of D. Moreover, if G has exponent p^s with s ≥ 2, then s ≤ (m+1)/4. In particular, if v = p^3 or p^5, then G must be elementary abelian.”*
> （该定理在源②中归于 Johnsen／Camion–Mann／Chen–Xiang–Sehgal）

**两源一致** ✓✓；原始 CXS 1994（*Des. Codes Cryptogr.* **4** 313–317，DOI 10.1007/BF01388647）为付费墙 ⟹ **本档以两篇独立二手汇总为准**，并**记录此边界**。

## §2 目标格收口

```
$$\text{格}:\ \boxed{DS(243,121,60,[3,9,9])};\quad G=\mathbb Z_3{\times}\mathbb Z_9{\times}\mathbb Z_9$$
$$|G|=243=3^5\Rightarrow p=3\ (p\equiv3\bmod4)\ ✓,\quad m=5;\qquad \exp(G)=9=3^2\Rightarrow s=2$$
$$s=2\ \ge\ 2\ \Longrightarrow\ \text{必须}\ s\le\frac{m+1}{4}=\frac{6}{4}=1.5;\qquad \text{但}\ s=2>1.5\Longrightarrow\boxed{\text{矛盾}}$$
$$\text{参数亦完全匹配定理对象}:\ 243=4(61)-1,\quad 121=2(61)-1,\quad 60=61-1\ ✓$$
$$\Longrightarrow\ \boxed{DS(243,121,60,[3,9,9])=\textbf{No}}\quad(\text{该群不存在 skew Paley-Hadamard 差集})$$
$$\text{等价表述}:\ m\le5\ \text{时若存在，则 }G\ \textbf{必须初等阿贝尔}\Longrightarrow \text{非初等者一律 }No$$
$$\text{一致性自检}:\ Z_3^5=Yes\ (\text{唯一 }s=1)\ ✓;\quad v=27\ (m=3):\ Z_3{\times}Z_9=No\ ✓\ \text{与定理吻合} ✓✓$$
```

**账本记法（照先生 13:23 指定）**：
```
LJCR-B1-cell-243-[3,9,9] : RESOLVED → No
  数学状态           | No
  依据               | Chen–Xiang–Sehgal 1994；经 Schmidt Thm 4.4 与 Ding–Wang–Xiang 2007 Thm 1.1 双源确认
  新数学定理         | 无
  新构造             | 无
  新计算证书         | 无需
  实际产出           | 数据库 Open → No 的文献核验／状态纠正
  E4                 | PASS
  "先查文献再烧计算" | 直接实证（避免一轮无谓构造搜索）
```

## §3 **批量闭包审计**（本档升级部分）

```
$$\text{对 }\mathbf{102{,}719}\ \text{个 }Open\ \text{格筛选}:\quad \text{SHDS 型参数}\ (v,k,\lambda)=(4n-1,2n-1,n-1)\ \land\ G\ \text{为阿贝尔 }p\text{-群},\ p\equiv3\bmod4$$
$$\Longrightarrow\ \text{命中 }97\ \text{格};\quad \text{套用 Thm 4.4}\ (s\ge2\ \land\ s>\lfloor (m+1)/4\rfloor)\ \Longrightarrow\ \boxed{\mathbf{74}\ \text{格判 }No}$$
$$\text{其中 }m\le5\ (\text{先生所举 }p^3/p^5\ \text{情形})=\boxed{\mathbf{21}\ \text{格}}\ (\text{含 }243,\ 343,\ 1331,\ 6859,\ 12167,\ 16807\times4,\ 161051\times4,\ \ldots)$$
$$\text{分布}:\ (p,m,s)\ \text{集中于}\ p=3\ (m=5,7,9,11),\ p=7\ (m=3,5),\ p=11\ (m=3,5),\ \text{及一批 }p^3\ (p=19\ldots83)$$
$$\text{产物}:\ \texttt{work/ljcr/cxs\_resolved.json}\ (\text{逐格 }v,k,\lambda,G,p,m,s)\ ＋\ \texttt{cxs\_batch.py}\ (\text{可复现脚本，1.8 s 跑完})$$
$$\text{本审计的形态}:\ \boxed{\text{Open DB}\to\text{定理匹配}\to\text{批量 }No\to\text{记录遗漏引用／修正状态}}\ ——\ \text{即 AMEND-27 设想的空间 B 类型}$$
$$\qquad (\text{无需 RH、无需新定理，但产出可验证／可复现／可纠错的数据库资产})$$
```

## §4 纪律性结论（保留）

```
$$\boxed{\text{E4 不是形式流程，而是真的替我们避免了一轮完全不必要的构造搜索}}$$
$$\text{若不做 E4}:\ \text{我们会去为 }Z_3{\times}Z_9{\times}Z_9\ \text{寻找构造}\ ——\ \text{而它}\textbf{可证不存在};\ \text{白烧算力} ✓$$
$$\text{反之}\ \text{E4 成本}:\ \text{约 3 次抓取}\ ({\sim}2\ \text{分钟}),\ \text{产出}=74\ \text{格批量判定}$$
```

## §5 诚实边界（必须声明）

```
(i)\ \text{两源皆\textbf{二手汇总}（综述定理／论文转述）};\ \text{CXS 1994 原文}\textbf{未取得}\ (\text{Springer 付费墙}) \Longrightarrow \text{待补}
(ii)\ \text{判定为\textbf{机械适用性检查}}:\ \text{SHDS 型参数}\ +\ \text{阿贝尔 }p\text{-群}\ +\ (s\ge2\land s>\lfloor (m+1)/4\rfloor);\ \text{未逐格复核其它条件}
(iii)\ \text{74 格中可能存在数据库\textbf{本已另有依据}但未在 }comment\ \text{写明者};\ \text{本档只主张"按定理应为 }No""
(iv)\ \textbf{不声称}新定理／新构造;\ \text{不声称数据库"错了"（其 }Open\ \text{语义为"未见构造"）};\ \text{只主张}\ \boxed{Open\not\Rightarrow\text{Math Open}}
(v)\ \text{下一步（非本档）}:\ \text{扩展到其它定理族}\ (\text{Turyn 界／BRC／计数／Schützenberger／Ma–Schmidt／Arasu–Ma})\ \text{的批量匹配}
```

## §附 【技术词回查】（**先跑后写**）

```
$ bash scripts/tech_word_check.sh "Chen–Xiang–Sehgal" "skew Paley-Hadamard" "上位定理" "批量 E4"
技术词 Chen–Xiang–Sehgal 命中文件数=2    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md ./B-LJCR-1-E4-result-and-ledger-fix.md
技术词 skew Paley-Hadamard 命中文件数=2    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md ./B-LJCR-1-E4-result-and-ledger-fix.md
技术词 上位定理     命中文件数=1    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md
技术词 批量 E4        命中文件数=1    :: ./LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md
```
**三分类**（命中文件全部为本档／紧前档 ⟹ 回查前档案内为 0）：
- **本档新增**：`Chen–Xiang–Sehgal`、`skew Paley-Hadamard`、`上位定理`、`批量 E4`（命中皆为自身，回查前 = 0 档）
- **档案已有（引用）**：`E4`（AMEND-27 体系内既有）、`Open/No`（DB 语义）
- **通用词（不计）**：`批量`、`数据库`
- **⚠️ 新性边界**：本档结论**非数学新结果**；交付物属**第 ④ 类**（证明候选并非新结果／已知）。
