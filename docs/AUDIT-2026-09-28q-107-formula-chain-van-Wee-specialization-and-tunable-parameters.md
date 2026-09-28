# AUDIT-2026-09-28q — **$107$ 公式链：van Wee 原式 ＋ $n{=}10$ 代入 ＋ 可调参数表**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:22 ✓
> **唐先生令**：**停止"119"**；把 $107$ 的**原式**拆开；找**可调参数**；**不得编造假证明** ✓

**已查地图**：接续 `AUDIT-p`（$107$ 来源）✓ ｜ Tavily 432 ⟹ Firecrawl ✓

D0: 本档对象 ＝ **档案已有**（van Wee 界／excess／$K(n,1)$——无新数学对象 ✓）
D1: 0（产出＝**公式链 ＋ $n{=}10$ 代入 ＋ 参数表** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① van Wee(1988) 原式已取（}\texttt{arXiv:2608.12595}\ \text{equ (5) 逐字）};\ \text{② }n{=}10\ \text{代入}\Rightarrow\mathbf{103}\ \text{（算术已核 ✓✓）}}$$
$$\boxed{\text{③ 链}:\ \frac{2^n}{n+1}{=}93.09\to\boxed{\text{van Wee}}\to\frac{2^n}{n}{=}102.4\to\boxed{\text{Zhang/Habsieger/Haas}}\to\mathbf{107}\to\boxed{?}\to119}$$
$$\boxed{\text{④ 诚实}:\ \mathbf{103\to107}\ \text{ 之原式\ \textbf{尚未取得}（Zhang 1991/92、Habsieger 1997、BÖW 2004 正文皆付费墙）} ⚠️}$$

## §1 van Wee 原式（**逐字引 ✓**）

$$\text{（源}:\ \texttt{arXiv:2608.12595},\ \text{引 van Wee 1988／Struik 1994）对一切 }(n,M,d)R\ \text{码}:$$
$$M\left(\sum_{i=0}^{R}\binom ni-\frac{\binom nR}{\lceil\frac{n-R}{R+1}\rceil}\left(\left\lceil\frac{n+1}{R+1}\right\rceil-\frac{n+1}{R+1}\right)\right)\ \ge\ 2^n\qquad\textbf{(5)}$$

### $n{=}10,\ R{=}1$ 代入（**本档计算 ✓✓**）

$$\sum_{i=0}^{1}\binom{10}{i}=11;\quad \binom{10}{1}=10;\quad \left\lceil\frac{10-1}{2}\right\rceil=5;\quad \left\lceil\frac{11}{2}\right\rceil-\frac{11}{2}=6-5.5=0.5$$
$$\text{修正项}=\frac{10}{5}\times0.5=1 \Longrightarrow \text{分母}=11-1=\boxed{10} \Longrightarrow K(10,1)\ge\frac{1024}{10}=102.4 \Longrightarrow \boxed{\mathbf{103}}\ ✓$$
$$\textbf{一般式（}n\ \text{偶）}:\ \left\lceil\frac{n-1}{2}\right\rceil=\frac n2,\ \left\lceil\frac{n+1}{2}\right\rceil-\frac{n+1}{2}=\frac12 \Longrightarrow \text{分母}=n \Longrightarrow \boxed{K(n,1)\ge\frac{2^n}{n}}\ ✓$$
$$（\text{与 }\texttt{arXiv:2203.16901}\ \text{摘要逐字一致}:\ "\gamma(Q_n)\ge\frac{2^n}{n}\ \text{given by Van Wee (1988)}"\ ✓✓）$$

## §2 后续改进之来源（**已验证者 ✓**）

$$\textbf{Zhang (1991, 1992)}:\ \text{Habsieger 摘要逐字称其改进"the lower bounds for }K(n,1)\ \text{given by Zhang (1991,1992)}"\ \checkmark$$
$$\textbf{Habsieger (1997)}\ \text{（Discrete Math 176, 115--130）摘要逐字}:\ \text{"covering condition expressed as a system of linear inequalities. The \textbf{excesses} then have a natural interpretation that makes \textbf{congruence properties} clear."}$$
$$\qquad \textbf{★且逐字}:\ \text{"We study more specifically the cases }n\equiv5 \bmod 6\ \text{and}\ n\equiv2,4 \bmod 6"\ \Longrightarrow\ \boxed{n{=}10\equiv\mathbf4 \bmod 6\ \text{恰在其内}}\ ✓✓$$
$$\qquad \text{其新下界例}:\ K(14,1)\ge1172,\ K(20,1)\ge52456\ ✓$$

## §3 excess 算术（**唐先生算 ✓，本档复核 ✓**）

$$a(x)=|C\cap B_1(x)|,\quad e(x)=a(x)-1\ge0,\quad \sum_x e(x)=11K-1024$$
$$K{=}107\Longrightarrow \mathbf{153};\qquad K{=}119\Longrightarrow \mathbf{285};\qquad K{=}120\Longrightarrow \mathbf{296}\ ✓$$
$$\therefore\ \text{纯 excess 总量\ \textbf{不能}解释 }107\to119;\ \text{增益来自\ excess\ \textbf{分布} 之算术（同余）约束}\ ✓$$

## §4 ★ 可调参数表（**唐先生所求 ✓**）

| 原证明参数 | $n{=}10$ 取值 | 对下界之贡献 | 可否加强 |
|---|---|---|---|
| 体积项 $\frac{2^n}{n+1}$ | $93.09$ | 基线 $\to94$ | **否**（精确） |
| van Wee 修正 $\frac{\binom nR}{\lceil\cdot\rceil}(\ldots)$ | $\frac{10}{5}\times0.5=1$ | $93.09\to102.4$ | **否**（$n$ 偶时精确 $\Rightarrow\frac{2^n}{n}$） |
| 取整/整性 | — | $102.4\to\mathbf{103}$ | **否** |
| **同余/excess 分布约束**（Zhang／Habsieger；$n\equiv4 \bmod 6$） | ? | $103\to\mathbf{107}$（$+4$） | ★**未知** |
| **$107\to119$ 之剩余** | ? | $+12$ | ★**未知**（$22$ 年无人推进） |

$$\boxed{\text{结论}:\ \text{已知部分（体积＋van Wee＋取整）\ \textbf{已饱和}（皆精确）};\ \text{全部"可调空间"\ \textbf{压在同余/excess 分布层}}\ ⚠️}$$

## §5 ⚠️ 诚实边界（**唐先生特别要求 ✓**）

$$\textbf{未取得}:\ \text{Zhang (1991,1992)、Habsieger (1997)、BÖW (2004)}\ \text{正文之\ \textbf{具体定理式}};\ \text{Wiley/ScienceDirect 正文付费}\ ✗$$
$$\therefore\ \textbf{本档不给出"}$107{=}\text{某显式公式}$"\ \text{之陈述} ✗\ \text{（遵令：不得编造）}$$
$$\textbf{下一步候选（未做）}:\ \text{①经 }\texttt{secemp9/arxiv-complete}\ \text{全文检索 Habsieger/Haas 之定理式};\ \text{②经馆际/作者主页取 BÖW 2004};\ \text{③从 Zhang 1991/92 起追} ⚠️$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "下界公式链" "可调参数表" "vanWee代入"
技术词 下界公式链   命中文件数=0    ::
技术词 可调参数表   命中文件数=0    ::
技术词 vanWee代入  命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **权威源直取**（arXiv HTML 逐字）＋ 本档算术代入 ＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗（V290）
- $\S4$ 之"可否加强"栏之★项为**未知**，**非**"不可加强" ✗；**不主张** $\Phi$ 新量存在 ⚠️
