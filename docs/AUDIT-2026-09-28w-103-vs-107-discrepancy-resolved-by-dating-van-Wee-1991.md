# AUDIT-2026-09-28w — **$103$ vs $107$ 之冲突已定分：$103$ 系 van Wee **1991** 之值**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:56 ✓
> **唐先生令**：沿"$103$ 后有无针对 $n{=}10$ 之更强不等式"继续追 ✓

**已查地图**：接续 `AUDIT-v`（H--P 2000 ＋ $106$ 已排除）✓

D0: 本档对象 ＝ **档案已有**（$K(10,1)$ 下界史——无新数学对象 ✓）
D1: 0（产出＝**年代定分 ＋ 冲突消解** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{唐先生所引 }K_2(10,1)\ge103\ \text{之源 ＝ }\textbf{van Wee 1991 博士论文}\ \text{（TU/e, 1991-06-04 答辩）} \Longrightarrow \text{系}\ \textbf{1991 年之值}}$$
$$\boxed{\therefore\ \text{与 }107\ \textbf{不冲突}:\ \text{时间链 }103\ (1991)\ \to\ \mathbf{107}\ (\text{B\"OW 2004})\ \to\ 107\ (\text{K\'eri 表，2026})✓}$$
$$\boxed{\therefore\ \text{当前最佳已发表下界 ＝ }\mathbf{107} \Longrightarrow K{=}106\ \text{仍被排除（}107>106\text{）}\ ✓}$$

## §1 证据（**逐字 ✓✓**）

$$\textbf{源}:\ \texttt{pure.tue.nl/ws/files/1995874/353803.pdf}\ \text{之元数据逐字}:\ "\text{Wee, van, G. J. M. (1991). \textbf{Covering codes, perfect codes, and codes from algebraic curves}. [Dissertatie 1 (Onderzoek TU/e / Promotie TU/e)]}"$$
$$\qquad "\textbf{Document status and date}:\ \text{Gepubliceerd}:\ \mathbf{01/01/1991}"\ ✓$$
$$\qquad "\text{...in het openbaar te verdedigen op dinsdag }\mathbf{4\ juni\ 1991}"\ ✓$$
$$\therefore\ \text{文中}\ "\text{best lower bound known is }K_2(10,1)\ge103"\ \text{系}\ \textbf{1991 年之陈述}\ ✓$$

## §2 下界时间链（**本档定稿 ✓**）

| 年 | 值 | 源 |
|---|---|---|
| 1988 | $2^n/n$（$n$ 偶）$\Rightarrow102.4\to103$ | van Wee, IEEE TIT 34, 237--245 |
| **1991** | $\mathbf{103}$（**$n{=}10$ 之陈述**） | van Wee **博士论文**（本档取证 ✓） |
| 1997 | $105$ | Cohen--Litsyn--Lobstein--Mattson 综述 Table A（标 "j"） |
| **2004** | $\mathbf{107}$ | **BÖW 2004**（OEIS `%H` 逐字 `[a(10)>=107]`） |
| 2026-08 | $\mathbf{107}$ | Kéri 表（Recensorium 悬赏页逐字 `n=10 R=1 107 .. 120`） |

$$\therefore\ \boxed{\text{当前最佳下界 ＝ }\mathbf{107};\ \text{上界 }120\ (\text{Östergård 1991}\to\text{Kamenetsky 显式})} \Longrightarrow 107\le K\le120\ ✓$$

## §3 唐先生之其他结论之核验（**皆对 ✓**）

$$\textbf{(甲) H--P 2000 属 linear-inequality 族}:\ ✓\ \text{摘要逐字确认}\ ✓$$
$$\textbf{(乙) Habsieger/Honkala 之"直接"congruence 界在 }n{=}10\ \text{仅给 }94:\ \checkmark$$
$$\qquad f(10)=\frac1{10}\sum_{i=0}^{10}\binom{10}i=102.4 \Longrightarrow K\ge\left(1+\frac1{102.4}\right)\frac{1024}{11}=94.0\ \checkmark\ \text{（＝球界级）}$$
$$\textbf{(丙) 2000 论文之公式\textbf{不会}"神奇产生"107}:\ ✓\ \text{（$p{=}11>n$ 之通用式仅给 }94\text{）}$$
$$\textbf{(丁) 但}\ "\text{文献路线不能关闭 }106"\ ✗\ \text{——\ 请见 §2: 107 已关闭 }106\ ✓$$

## §4 建议下一步（**照唐先生之队列 ✓**）

$$\text{① 查针对 }n{=}10\ \text{之\ \textbf{专门} 更强不等式（}103\to107\ \text{之 4 步来源）}:\ \textbf{Haas 2000}（Discrete Math 219, 97--106）、\textbf{Blass--Litsyn 1998}（IEEE TIT 44, 1998--2002）、\textbf{Habsieger 1997}（Discrete Math 176, 115--130）、\textbf{Plagne 后续}}$$
$$\text{② 目标层次确认}:\ \text{下界端\ \textbf{可挖} ＝ }107\to108\ (\Leftrightarrow E\ge164);\quad \text{上界端 ＝ }120\to119$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "103是1991年值" "年代定分" "107当前"
技术词 103是1991年值  命中文件数=0    ::
技术词 年代定分     命中文件数=0    ::
技术词 107当前     命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 权威源直取（TU/e 元数据逐字）＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗
- §2 之 $107$ **依赖** BÖW 2004 归属（OEIS 2026-05 版 ＋ Kéri 表 2026-08 **两独立权威一致** ✓）；**BÖW 正文未核** ⚠️
