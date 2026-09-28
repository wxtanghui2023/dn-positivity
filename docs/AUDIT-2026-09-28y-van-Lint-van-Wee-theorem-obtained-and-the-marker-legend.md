# AUDIT-2026-09-28y — **van Lint–van Wee 1991 混合定理到手（只给 $103$）＋ Kéri 标记图例定源**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:00 ✓
> **唐先生令**：把 $107$ 之**来源层级**分清；**不再追 van Lint--van Wee** ✓

**已查地图**：★**命中既有档** —— `AUDIT-v`（H–P 2000）／`AUDIT-w`（$103$ 系 1991）／`AUDIT-x`（取法受阻）／`AUDIT-q`（van Wee 1988 原式）✓

D0: 本档对象 ＝ **档案已有**（$K(n,1)$ 下界族／标记——无新数学对象 ✓）
D1: 0（产出＝**祖公式取证 ＋ 一处猜测排除 ＋ 标记定源** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① van Lint--van Wee 1991 混合定理\ \textbf{已到手}（据唐先生），}\ t{=}0,b{=}10\Rightarrow\mathbf{102.4}\Rightarrow\boxed{103}\ ✓}$$
$$\boxed{\text{② ★一处猜测\ \textbf{正式排除}}:\ \text{"}107\ =\ \text{van Lint--van Wee 1991 代入}"\ ✗\ \text{（只给 }103\text{）}}$$
$$\boxed{\text{③ ★Kéri 标记图例定源}:\ \mathbf b{=}\text{van Lint--van Wee (1991)},\ \mathbf c{=}\text{Östergård--Hämäläinen (1997)},\ \mathbf d{=}\textbf{BÖW (2004)}}$$
$$\boxed{\text{④ 唯一缺口}:\ \textbf{BÖW 2004 之 general }R{=}1\ \text{theorem 正文}}$$

## §1 祖公式（**唐先生取证 ＋ 本档复核 ✓**）

$$\text{van Lint--van Wee 1991 混合 }R{=}1\ \text{定理}:\quad |C|\ \ge\ \frac{(2t+b)\,3^{t}\,2^{b}}{(2t+b)(1+2t+b)-b}\qquad(b\ \text{偶})$$
$$\textbf{代入}\ t{=}0,\ b{=}10\ (\text{偶}):\quad |C|\ \ge\ \frac{10\cdot2^{10}}{10\cdot11-10}=\frac{10240}{100}=\mathbf{102.4}\ \Longrightarrow\ \boxed{|C|\ge103}\ ✓✓$$
$$\text{（源}: \text{van Lint--van Wee 1991 之 Theorem 16（van Wee 1991 博士论文扫描页）✓\text{）}}$$

## §2 四路下界账（**定格 ✓**）

| 机制 | $n{=}10$ 之界 | 判定 |
|---|---|---|
| van Wee 1988（$2^n/n$，$n$ 偶） | $102.4\to\mathbf{103}$ | **已取原式 ✓** |
| **van Lint--van Wee 1991（混合）** | $102.4\to\mathbf{103}$ | **已取 ✓（本档）** |
| Habsieger/Honkala 型 excess/congruence | $\mathbf{94}$ | 已核 ✓ |
| **BÖW 2004（标记 $\mathbf d$）** | $\mathbf{107}$ | **正文未取** ⚠️ |

$$\therefore\ \boxed{103、94\ \text{皆不能解释 }107 \Longrightarrow\ \text{之前在\ \textbf{代错公式}}\ ⚠️}$$

## §3 ★ 猜测之正式排除（**本档核心 ✓✓**）

$$\textbf{原猜测}:\ "\text{BÖW 之 }107\ =\ \text{van Lint--van Wee 1991 generalized mixed bound 直接代入}"$$
$$\textbf{判定}:\ ✗\ \text{正式排除}\ \text{—— 该式在 }n{=}10\ \text{只给 }103;\ \text{且 Kéri 标记}\ \mathbf b\ (\text{1991})\ne\mathbf d\ (\text{2004})\ \text{为\ \textbf{两条独立机制}}\ ✓$$
$$\therefore\ \boxed{107\ \text{确系 BÖW 2004 之\textbf{新} lower-bound mechanism};\ \text{非旧式重代}}\ ✓$$

## §4 唯一缺口与下一步（**照唐先生 ✓**）

$$\boxed{\text{待取}:\ \textbf{BÖW 2004 §中 general lower bound 之具体 theorem/inequality}}$$
$$\text{取到后唯一代入}:\ (b,t){=}(10,0),\ R{=}1 \Longrightarrow \text{应为 }107;\ \text{再问 }F(10)\stackrel{?}{\ge}108$$
$$\textbf{本轮试取之结果}:\ \text{Östergård 主页（}\texttt{users.aalto.fi/\textasciitilde pat/}\text{）为\ \textbf{纯书目}（无 PDF 链接）} ✗;\ \text{搜索引擎仍全灭（432／402）} ✗$$
$$\therefore\ \text{可行取法退回（} \texttt{AUDIT-x}\ \S3\text{）}:\ \text{①装 pypdf 重抽 }\texttt{/tmp/keri.pdf}\ \text{（其表含 }\mathbf b/\mathbf c/\mathbf d\ \text{图例）};\ \text{②《Covering Codes》(1997) 相关章};\ \text{③引文反查 Haas 2002／Plagne 2009}\ ⚠️$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "vanLint-vanWee定理" "标记图例" "代错公式"
技术词 vanLint-vanWee定理 命中文件数=0    ::
技术词 标记图例        命中文件数=0    ::
技术词 代错公式        命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 唐先生取证 ＋ 本档算术复核 ＋ 档案引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** BÖW 公式 ✗（遵令 ✓）；**不主张** $108$ 可达 ✗（V290）
