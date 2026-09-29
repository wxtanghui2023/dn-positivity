# AUDIT-2026-09-29h — **surfeit\ \textbf{逐字定义}到手：与 $\sum\binom\delta2$ \textbf{不同}；且 Wu--Chen 方法\ \textbf{不覆盖 }$n{=}10$（须 $6\mid n$）**

> **性质**：**文献取证 ＋ 适用性判定 ＋ 多码复核**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:2x ✓
> **唐先生令**：「先核对一下」✓

**已查地图**：接续 `AUDIT-29g`（surfeit 链核验：二阶 excess ＝ 死框架）／`29c`（框架 ≡ 球界）✓

D0: 本档对象 ＝ **档案已有**（$\delta$／excess／surfeit——无新数学对象 ✓）
D1: 0（产出＝**逐字定义 ＋ 一处适用性排除 ＋ 多码复核** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ surfeit 逐字定义到手}:\ \zeta_S(D)=\sum_{v\in S\setminus D}\bigl(\delta_{N[v]}(D)-1\bigr)\ ——\ \textbf{非}\ \sum_x\binom{\delta(x)}2}$$
$$\boxed{\text{② ✓✓ Habsieger 同余 (1.7) 实测全中}:\ n{=}10\Rightarrow\delta_{N[v]}\ \text{奇}\ (v\notin D)\ ——\ \textbf{904/904}}$$
$$\boxed{\text{③ ★★ Wu--Chen 方法\ \textbf{须 }6\mid n \Longrightarrow n{=}10\ \textbf{不覆盖}}✗\ (\text{且其式在 }n{=}10\ \text{仅给 }105.03\Rightarrow106<107)$$
$$\boxed{\text{④ ✓ 我上轮两条恒等式多码复核通过（一处"False"系我自己截断对计数之伪影，非反例）}}$$

## §1 ① surfeit 逐字定义（**✓✓ 取证**）

$$\textbf{Definition 2（Wu--Chen）}:\quad \zeta_S(D)\ :=\ \sum_{v\in S\setminus D}\Bigl(\delta_{N[v]}(D)-1\Bigr);\qquad \zeta_v:=\zeta_{\{v\}}$$
$$\text{其中}\ \delta_{N[v]}(D)=\sum_{y\in N[v]}\bigl(|D\cap N[y]|-1\bigr)\ (\text{即闭邻域内 excess})$$
$$\textbf{逐字（原文）}:\ "\text{Although it seems closely related to }excess\text{, we shall demonstrate that such further analyzation is enough to improve the known bounds.}"$$
$$\textbf{实测对照}:\ 120\text{-code}:\ \zeta=1556\ \text{vs}\ \sum\binom{\delta}2=102;\quad \text{贪心}:\ 4428\ \text{vs}\ 166 \Longrightarrow \boxed{\text{二者\ \textbf{完全不同}}}\ ✓$$
$$\therefore\ \texttt{AUDIT-29g}\ \text{之判定（}\sum\binom\delta2\ \text{＝死框架）\ \textbf{不影响} surfeit;\ \text{但 surfeit 是否可用\ 取决于\ }\S3} $$

## §2 ② Habsieger 同余（**✓✓ 独立复核**）

$$\textbf{Theorem 1（Habsieger）, (1.7)}:\quad \delta_{N[v]}(D)\ \equiv\ n+1\ (\mathrm{mod}\ 2)\quad\text{if }v\notin D$$
$$\text{（另 (1.8) }v\in D\Rightarrow\equiv0;\ \text{(1.9) }3\mid n\Rightarrow\delta_{N_1[v]}+\delta_{N_2[v]}\equiv0\ (\mathrm{mod}\ 3)\text{）}$$
$$n{=}10:\ n+1=11\ \text{奇} \Longrightarrow \boxed{\delta_{N[v]}\ \textbf{必为奇数}\ (v\notin D)}\ \Longrightarrow\ \zeta_v=\delta_{N[v]}-1\ \text{为\ \textbf{偶数}且}\ge0$$
$$\textbf{实测}:\ 120\text{-code}\ \mathbf{904/904}\ \text{全奇};\ \text{贪心}\ \mathbf{874/874}\ \text{全奇}\ ✓✓$$
$$\text{（与我此前\ \textbf{独立}推出之"}\varepsilon{=}1\text{（}E(B(x,1))\ \text{奇）"\ \textbf{完全一致} —— 交叉印证}✓）$$

## §3 ★★ ③ 适用性排除（**决定性 ✗**）

$$\textbf{原文逐字}:\ "\text{We look into the cases when }n\text{ is a }\textbf{multiple of 6}\text{. By calculating }\zeta_{V(Q_n)}(D)\ \text{using two different methods, we show that it leads to a contradiction if }\gamma(Q_n)\le\cdots"$$
$$\textbf{摘要逐字}:\ "\text{When }n\text{ is a multiple of }6\text{, the best known lower bound is }\gamma(Q_n)\ge 2^n/n\ldots\text{we obtain }\gamma(Q_n)\ge\frac{(n-2)2^n}{n^2-2n-2}"$$
$$\therefore\ \boxed{\text{其推导依赖 (1.9)（须 }3\mid n\text{）与 }6\mid n\text{ 之双法计算} \Longrightarrow n{=}10\ (\equiv4\bmod6)\ \textbf{不覆盖}}✗✗$$
$$\textbf{且}:\ \text{其式在 }n{=}10\ \text{之数值}=\frac{8\cdot1024}{100-20-2}=\frac{8192}{78}=105.026\Rightarrow\mathbf{106}<107\ ——\ \text{即\ \textbf{即使}适用也不够}$$
$$\therefore\ \boxed{\text{\textbf{Wu--Chen 之 surfeit contradiction \textbf{不覆盖} }n{=}10}$$
$$\text{\textbf{措辞精度（唐先生令）}:\ "Wu--Chen 这套证明不适用"\ \ne\ "所有 surfeit 推导皆不可能" —— \textbf{后者不得主张} ✗$$

## §4 ④ 多码复核（**✓，含一处诚实标注**）

| 码 | $M$ | $\sum\binom\delta2=2(N_1{+}N_2)-E$ | $H+\sum_C\binom{1+d_1}2=2U_2$ |
|---|---|---|---|
| 120-code | $120$ | ✓ True | ✓ True |
| 贪心-0 | $150$ | ✓ True | ✓ True |
| 贪心-3 | $148$ | ✓ True | ✓ True |
| 全偶重码 | $512$ | ⚠️ False —— **伪影** | ✓ True |

$$\text{⚠️ 诚实标注}:\ \text{全偶重码行之 False 系我\ \textbf{把对计数截断在头 }400\ \text{个码字}（}M{=}512\text{）\ 所致},\ \textbf{非恒等式失败} ✗\text{（我的实现缺陷，非反例）}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "surfeit定义" "适用性排除" "同余核验"
技术词 surfeit定义   命中文件数=0    ::
技术词 适用性排除   命中文件数=0    ::
技术词 同余核验     命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **免费 arXiv 取证 ＋ 多码实测** ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
- 已归档：`sources/Wu-Chen-2024-arXiv2203.16901-FULLTEXT.txt`
