# AUDIT-2026-09-28z — **$K(10,1)$ 下界演进之逐步出处锁定（Kéri 档 ＋ `pypdf` 抽取）**

> **性质**：**审计（取证）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:04 ✓
> **唐先生令**：继续追 BÖW；若无 PDF 则从公开镜像／引文反追 ✓

**已查地图**：接续 `AUDIT-y`（van Lint--van Wee 只给 $103$）／`AUDIT-x`（取法）✓

D0: 本档对象 ＝ **档案已有**（下界史／文献——无新数学对象 ✓）
D1: 0（产出＝**逐步出处锁定 ＋ 一条关键机制定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① }\texttt{pip install pypdf}\ \text{成功抽出 Kéri 档（}191\ \text{页／}423{,}136\ \text{字符）}}✓✓$$
$$\boxed{\text{② ★}\ K(10,1)\ \text{下界演进之\ \textbf{逐步出处} 全部锁定（§2）}}✓✓$$
$$\boxed{\text{③ ★}\ 105\ \text{之来源 ＝ }\textbf{Zhang 1991「Pair covering inequalities」}\ \text{（线性不等式族之祖）}}✓✓$$

## §1 Kéri 档之逐字（**匈牙利文 ✓✓**）

$$\textbf{逐字}:\ "107\ \le\ K(10,\ 1)\ \le\ 120.\ \text{Prompt felső korlát }128.\ \text{A felső korlát javítása }120\text{-ra }[58,\ 64].\ \text{Prompt alsó korlát}:\ 94.\ \text{Az alsó korlát javítása }96\text{-ra }[18],\ 97\text{-re }[46],\ 103\text{-ra }[52],\ 105\text{-re }[67],\ 107\text{-re }[130]."$$
$$\text{（译：平凡下界 }94;\ \text{改进至 }96\,[18],\ 97\,[46],\ 103\,[52],\ 105\,[67],\ \mathbf{107}\,[130]\text{）}$$
$$\qquad\text{另逐字}:\ \text{"Totókód }120\ \text{kódszóval}:\ \text{Fagioli C. (1975)}"\ \Longrightarrow\ \text{上界 }120\ \text{另有一源} ⚠️$$

## §2 ★★ 逐步出处（**全部锁定 ✓✓**）

| 下界 | 编号 | **文献** |
|---|---|---|
| $94$ | — | 平凡（sphere-covering） |
| $\mathbf{96}$ | $[18]$ | **Stanton \& Kalbfleisch (1968)**, "Covering problems for dichotomized matchings", Aequationes Math. **1**, 94--103 |
| $\mathbf{97}$ | $[46]$ | **Cohen, Lobstein \& Sloane (1986)**, "Further results on the covering radius of codes", IEEE TIT **32**, 680--694 |
| $\mathbf{103}$ | $[52]$ | **van Wee (1988)**, "Improved sphere bounds on the covering radius of codes", IEEE TIT **34**, 237--245 ✓（**本会话已取原式并复核 $2^{10}/10{=}102.4\Rightarrow103$ ✓ 完全一致**） |
| $\mathbf{105}$ | $[67]$ | ★★ **Zhang (1991)**, "**Linear inequalities for covering codes: Part I --- Pair covering inequalities**", IEEE TIT **37**, 573--582 |
| $\mathbf{107}$ | $[130]$ | **Bertolo, Östergård \& Weakley (2004)**, J. Combin. Des. **12**, 157--176 |

$$\text{上界}:\ 128\ (\text{平凡})\to120:\ [58]\ \text{Wille (1990) 模拟退火};\ [64]\ \textbf{Östergård (1991)},\ \text{IEEE TIT 37, 179--180}\ ✓$$

## §3 ★ 机制定位（**本档关键读数 ✓✓**）

$$\boxed{105\ \text{之来源 Zhang 1991\ ＝\ pair covering inequalities（线性不等式族）}}\ ✓$$
$$\text{链之机制层}:\ \underbrace{94}_{\text{球界}}\to\underbrace{96,97}_{\text{excess／计数}}\to\underbrace{103}_{\text{van Wee 球修正}}\to\underbrace{105}_{\textbf{Zhang 线性不等式}}\to\underbrace{107}_{\textbf{BÖW 一般 }R{=}1\ \text{界}}$$
$$\text{与本会话已知之\textbf{重叠}:\ Habsieger 1997 摘要逐字谓其改进"the lower bounds for }K(n,1)\ \text{given by }\textbf{Zhang (1991, 1992)}" \Longrightarrow \textbf{Zhang 系＝线性不等式族之祖}}\ ✓$$
$$\text{（本线档案 }\texttt{SPHERELP}\text{·}\texttt{HQ1}\text{·}\texttt{M2B}\ \text{涉"线性不等式族"——\ \textbf{同族} ⚠️）}$$

## §4 缺口与下一步（**更新优先级 ✓**）

$$\boxed{\text{仍缺}:\ \textbf{① Zhang 1991 pair covering inequality 原式（}\to105\text{）};\quad \textbf{② BÖW general }R{=}1\ \text{（}\to107\text{）}}$$
$$\text{取法}:\ \text{①二者同族，}\textbf{Zhang 之式更可能被免费引用};\ \text{②本会话已下载 Kéri 档（}\texttt{sources/}\text{）};\ \text{③}\texttt{pypdf}\ \text{路数已通} ✓$$
$$\therefore\ \text{优先}:\ \textbf{Zhang 1991}\to\textbf{BÖW 2004};\ \text{取到任一即可做唯一代入 }(b,t){=}(10,0),R{=}1$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "来源链锁定" "逐步出处" "Zhang配对不等式"
技术词 来源链锁定     命中文件数=0    ::
技术词 逐步出处      命中文件数=1    :: ./C74-verification-receipt-...（空间 A 同名，不计）
技术词 Zhang配对不等式 命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **本地抽文**（`pypdf`，191 页）＋ 逐字引证 ＋ 档案交叉 ✓；已存 `sources/Keri-covering-code-history.pdf` 与 `...-Hungarian-EXTRACT.txt` ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $107\to108$ 可行 ✗（V290）
