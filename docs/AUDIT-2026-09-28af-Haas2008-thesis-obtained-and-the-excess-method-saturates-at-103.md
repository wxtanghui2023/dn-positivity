# AUDIT-2026-09-28af — **Haas 2008 专著到手（83 页）＋ ★excess 方法在 $n{=}10$ 于 $103$ \textbf{饱和}；$107$ \textbf{不}出自该族**

> **性质**：**审计（取证 ＋ 否证）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:33 ✓
> **唐先生令**：恢复 BÖW 2004 general $R{=}1$ 之母不等式 ✓

**已查地图**：接续 `AUDIT-ab`（链实测）／`AUDIT-aa`（Zhang 系列）／`AUDIT-z`（逐步出处）✓

D0: 本档对象 ＝ **档案已有**（excess 方法／$K(n,1)$——无新数学对象 ✓）
D1: 0（产出＝**专著取证 ＋ $R{=}1$ 定理逐条代入 ＋ ★否证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 取得 Haas 2008 专著}:\ "\text{The covering excess method in the theory of covering codes}",\ \textbf{83 页／98{,}379 字符}（Freiburg）}✓✓$$
$$\boxed{\text{② ★ 该族之 }R{=}1\ \text{定理在 }n{=}10\ \textbf{上限为 }103;\ \text{逐条代入皆不达 }107}✓✓$$
$$\boxed{\text{③ ★★ 否证}:\ \text{该 2008 专著\ \textbf{完全未引} Bertolo／Weakley} \Longrightarrow \textbf{107 不}\text{出自经典 excess 方法}}$$

## §1 ★ 三条 $R{=}1$ 定理之逐字与代入（**本档核心 ✓✓**）

$$\textbf{Thm 24（Habsieger [9], Honkala [16]）}:\ n\equiv-1\ (\mathrm{mod}\ p),\ p\ \text{奇素数}\ \Longrightarrow\ K(n,1)\ \ge\ \left(1+\frac1{g(n)}\right)\frac{2^n}{n+1},\quad g(n)=\frac{\binom{n}{p-1}}{(p-2)p-1}+\sum_{i=0}^{p-2}\frac{\binom ni}{i+1}$$
$$\text{代入 }n{=}10,\ p{=}11:\ g(10)=\frac1{98}+186=186.0102\ \Longrightarrow\ K\ \ge\ 1.005376\cdot93.0909=\mathbf{93.59}\ \Longrightarrow\ \boxed{94}\ ✓$$
$$\qquad\text{（与唐先生之 }94\ \textbf{完全一致} ✓）$$
$$\textbf{Thm 52（van Wee [29]）}:\ K(n,R)\ \ge\ \frac{(n-R+\epsilon)2^n}{(n-R)V(n,R)+\epsilon V(n,R-1)},\qquad \epsilon=(R+1)\left\lceil\frac{n+1}{R+1}\right\rceil-(n+1)$$
$$\text{代入 }n{=}10,R{=}1:\ \epsilon=2\cdot6-11=1\ \Longrightarrow\ K\ \ge\ \frac{10\cdot1024}{9\cdot11+1}=\frac{10240}{100}=\mathbf{102.4}\ \Longrightarrow\ \boxed{103}\ ✓✓$$
$$\qquad\text{（★此即唐先生所给之"van Lint--van Wee"式 —— }\textbf{同一式} ✓）$$
$$\textbf{Thm 54（Haas 之改进）}:\ R\ge1,n\ge2R+1\ \Longrightarrow\ K(n,R)\ \ge\ \frac{(n-2R+2\epsilon)2^n}{(n-2R+\epsilon)V(n,R)+\epsilon V(n,R-1)}$$
$$\text{代入 }n{=}10,R{=}1\ (\epsilon{=}1{=}R):\ \frac{10\cdot1024}{9\cdot11+1}=\mathbf{102.4}\Longrightarrow\boxed{103}\ \text{（专著自陈：}\epsilon{=}R\ \text{时与 van Wee }\textbf{重合}\ ✓）$$
$$\textbf{Thm 57}:\ \text{前提 }2\le R<n\ \Longrightarrow\ \textbf{对 }R{=}1\ \text{不适用}\ ✗$$

$$\therefore\ \boxed{\text{excess 方法族（van Wee／Habsieger／Honkala／Haas）在 }n{=}10\ \text{之上确界} ＝ \mathbf{103}}$$

## §2 ★★ 否证：$107$ 不出自 excess 方法（**本档关键 ✓✓**）

$$\text{档内关键词命中}:\ \textbf{Bertolo }0,\ \textbf{Weakley }0;\qquad \text{Habsieger }26,\ \text{van Wee }40,\ \text{Honkala }30,\ \text{Blass }13,\ \text{Litsyn }14,\ \text{Zhang }5$$
$$\text{该专著系 excess 方法之\ \textbf{权威总结}（2008，晚于 BÖW 2004）}\ \Longrightarrow\ \text{若 }107\ \text{属该族，必被引} ✗$$
$$\therefore\ \boxed{\textbf{107 不}\text{出自经典 excess 方法};\ \text{其出处 BÖW 2004 属\ \textbf{混合码}\ }K_{2,3}(b,t;R)\ \text{之 general }R{=}1\ \text{界}}✓✓$$
$$\text{（佐证}:\ \text{BÖW 主对象为 }b+t\le13\ \text{之 mixed codes},\ \text{非纯二进 excess}）$$

## §3 层之划定（**四层，定稿 ✓**）

| 机制族 | $n{=}10$ 之界 | 出处 |
|---|---|---|
| sphere covering | $94$ | 平凡 |
| **excess 方法**（van Wee／Habsieger／Honkala／**Haas 2008**） | $\mathbf{103}$（**饱和**） | Thm 24 / 52 / 54 |
| **线性不等式**（Zhang 1991 pair；Zhang–Lo 1992 triple） | $\mathbf{105}$ | IEEE TIT 37/38 |
| **混合码 general $R{=}1$**（BÖW 2004） | $\mathbf{107}$ | J. Combin. Des. 12 |

$$\therefore\ \boxed{\text{唐先生之"}\text{Habsieger/Honkala}\to\text{Zhang/Haas}\to\text{H-P}\to\text{BÖW}"\ \text{层级模型}\ \textbf{成立};\ \text{但 excess 层止于 }103}✓$$

## §4 新的候选机制（**专著所载，LIVE ✓**）

$$\textbf{① radii-two 球 excess}:\ \text{专著附录逐字"Lower-bounding }K(n,R)\ \text{with the use of a covering excess in spheres with }\textbf{radius two}\text{"（Honkala [14]；q-ary 见 Chen--Honkala [3]）}⚠️$$
$$\textbf{② }q\text{-ary 推广}:\ \text{Thm 52 之 }q\text{-ary 形式（Chen--Honkala [3]、van Wee [30]）}⚠️$$
$$\textbf{③ Blass--Litsyn }n\equiv5\ (\mathrm{mod}\ 6)\ \text{定理}:\ \text{专著书目 }[1]\ \text{即此};\ n{=}10\equiv4\ \textbf{不适用}\ ✗\ \text{（与唐先生之排除一致 ✓）}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "excess方法饱和" "Radii-two候选" "混合码机制"
技术词 excess方法饱和  命中文件数=0    ::
技术词 Radii-two候选  命中文件数=0    ::
技术词 混合码机制     命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **专著直取 ＋ 逐条代入实测** ＋ 档案交叉 ✓；已存 `sources/Haas2008-covering-excess-method.pdf` 及 `EXTRACT.txt` ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** BÖW 公式 ✗；**不主张** $107\to108$ 可达 ✗（V290）
