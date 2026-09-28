# AUDIT-2026-09-28ab — **历史纠偏（Habsieger 1997 只给 $104$）＋ 链之实测**

> **性质**：**审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:09 ✓
> **唐先生令**：把 Zhang 之 pair-covering inequality 写出来 → 追 BÖW 如何推广 → 算 $n{=}10$ 之 $107$ ✓

**已查地图**：接续 `AUDIT-aa`（Zhang 系列）／`AUDIT-z`（逐步出处）✓

D0: 本档对象 ＝ **档案已有**（$\delta$ 场／van Wee 链／$120$-code——无新数学对象 ✓）
D1: 0（产出＝**历史纠偏 ＋ 链之数值实测 ＋ 松余量诊断** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ★ 历史纠偏（唐先生取证）}:\ \textbf{Habsieger 1997 只给 }K(10,1)\ge104;\ \text{且原文自陈}\ \textbf{Zhang 之 }105\ \text{更强}}$$
$$\boxed{\text{② ⟹ 链为 }103\to105\to107\ \text{（}\textbf{非}"各种 excess 一路推到 107"\text{）}}$$
$$\boxed{\text{③ 本档实测 Habsieger 重建链（120-code）}:\ \text{两条不等式\ \textbf{皆成立但余量极松} ⟹ 只得 van Wee 级}}$$

## §1 ★ 历史纠偏（**唐先生取证，逐字 ✓✓**）

$$\text{Habsieger 原文（extended abstract）}:\ K(10,1)\ge\mathbf{104};\ \text{并紧接着述}\ "\text{对 }n{=}10,\ \text{当时最好之结果是 Zhang 的 }K(10,1)\ge\mathbf{105}"$$
$$\therefore\ \boxed{\text{Habsieger 1997 }(104)\ <\ \text{Zhang 1991/92 }(105)}$$
$$\therefore\ \text{修正后之链}:\ \underbrace{103}_{\text{van Wee 1988}}\to\underbrace{105}_{\textbf{Zhang pair ineq.}}\to\underbrace{107}_{\textbf{BÖW 2004}}\ ✓$$

## §2 Habsieger 之 van Wee 重建链（**逐字结构 ✓**）

$$S:=N_0+N_1-1;\qquad \text{覆盖}\iff S(x)\ge0;\qquad \sum_x S(x)=(n+1)|C|-2^n\ ✓$$
$$\text{偶 }n:\quad 2^n-|C|\ \le\ \sum_{x\notin C}(S_0+S_1)(x)\ \Longrightarrow\ \sum_y S(y)\,(n-S(y))\ \le\ (n^2-1)\,|C|\ \Longrightarrow\ |C|\ge\frac{2^n}{n}\ ✓$$

## §3 ★ 本档实测（**120-code，$n{=}10$，$K{=}120$ ✓✓**）

| 检验 | 实测 | 判定 |
|---|---|---|
| (i) $\sum_x S(x)=(n{+}1)K-2^n$ | $296=11\cdot120-1024$ | ✓ **恒等** |
| (ii) $\sum_y S(y)(n-S(y))\le(n^2{-}1)K$ | $2460\le11880$ | ✓ 成立，**余量 $9420$（极松）** |
| (iii) $2^n-K\le\sum_{x\notin C}(S_0{+}S_1)(x)$ | $904\le1100$ | ✓ 成立，**余量 $196$** |

$$\delta\ \text{分布}:\ \{0{:}801,\ 1{:}172,\ 2{:}36,\ 3{:}8,\ 4{:}7\};\qquad \sum\delta=296;\qquad \sum\delta^2=500$$
$$\therefore\ \boxed{\text{该链只能到 van Wee 级 }2^{10}/10{=}102.4\Rightarrow103 \Longrightarrow \textbf{不足以解释 }105,\ \text{更不足 }107}\ ⚠️✓$$
$$\text{（}= \text{与 `EXCESS-2026-09-25` 之 $\delta$-场结论一致}:\ \text{首阶 excess 不能区分 }106\ \text{与 }119\text{）}$$

## §4 ★ 上界 $120$ 之构造源（**唐先生取证 ✓**）

$$\mathbb F_4\times\mathbb F_2^7\ \text{之混合覆盖码（}60\ \text{codewords},\ R{=}1\text{）}\ \xrightarrow{\ \text{substitution}\ }\ \mathbb F_2^{10}\ \text{之 }120\text{-code}\ \Longrightarrow\ K_2(10,1)\le120\ ✓$$
$$\text{（＝ Östergård 1991，其当时新纪录；与本会话 }\texttt{AUDIT-r}\ \text{之 Kamenetsky 显式 }120\ \text{词一致 ✓）}$$

## §5 骨架图（**定稿 ✓**）

$$\boxed{94\ \xrightarrow{\text{sphere}}\ 96,97\ \xrightarrow{\text{excess/计数}}\ 103\ \xrightarrow{\text{van Wee}}\ 105\ \xrightarrow{\textbf{Zhang pair ineq.}}\ 107\ \xrightarrow{\textbf{BÖW general }R{=}1}}\qquad \text{上界 }120\ \text{（Östergård mixed + substitution）}$$

## §6 下一步（**照唐先生；目标已收敛 ✓**）

$$\textbf{①}\ \text{写出}\ \textbf{Zhang 1991 pair-covering inequality}\ \text{之原式};\quad \textbf{②}\ \text{追}\ \textbf{BÖW}\ \text{如何推广为 general }R{=}1;\quad \textbf{③}\ \text{算 }n{=}10\ \text{之 }107$$
$$\text{价值}:\ \text{若 BÖW 式可写成 }F(n,K,\text{excess/profile})\ge0,\ \text{则代 }K{=}106\ \text{可独立得 }K\ge107;\ \text{若 }K{=}106\ \text{时 slack 极小} \Longrightarrow \text{判断 }107\to108\ \text{是否同机制可达}\ ✓$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "历史纠偏" "链条实测" "松余量"
技术词 历史纠偏   命中文件数=0    ::
技术词 链条实测   命中文件数=0    ::
技术词 松余量    命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **本地实测**（120-code）＋ 唐先生取证 ＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $107\to108$ 可达 ✗（V290）
