# AUDIT-2026-09-29y — **$I(1)=10$ 为错（实测 $=2$）；修正后二阶 overlap 是\ \textbf{恒等式非约束}；附\ \textbf{三重预检}（此后一切候选必先过）**

> **性质**：**实测纠错 ＋ 框架归位 ＋ 方法纪律**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:4x ✓
> **唐先生令**：从 $K(10,1)\ge107$ 已知结论出发，**自行重建 106 不可能证明** ✓

**已查地图**：`AUDIT-29v`（Delsarte 可行）／`29w`（cell/Walsh 归位为 Habsieger）／`29x`（excess 逆趋势）✓

D0: 本档对象 ＝ **档案已有**（$\mu$／$N_i$／$A_i$／Krawtchouk——无新数学对象 ✓）
D1: 0（产出＝**一处系数纠错 ＋ 一处恒等式归位 ＋ 三重预检之固化** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗✗ }I(1)=10\ \textbf{为错}:\ \text{实测 }|N[c]\cap N[c']|=\mathbf{2}\ (\forall d\in\{1,2\}),\ 0\ (d\ge3)}$$
$$\boxed{\text{② ✗ 故你的式应为}\ \Sigma_x\tbinom{\mu(x)}2=\mathbf{2}N_1+\mathbf{2}N_2=M(A_1+A_2)\ (\text{非 }10N_1+2N_2,\ \text{非 }530A_1+106A_2)}$$
$$\boxed{\text{③ ✗ 且修正后此条是\ \textbf{恒等式}（非约束）}\Longrightarrow\ \text{框架}＝\text{经典 Delsarte／covering-LP（已封闭）}}$$
$$\boxed{\text{④ ⟹ 不能给出 }107\ (\text{该框架上限：球界 }94\ /\ \text{van Wee }103\ /\ \text{SDP-3 }105.2223)}$$

## §1 ① $I(d)$ 之实测（**✗✗**）

$$\textbf{实测（120-code，全部 }d\le3\ \text{之码字对）}:\quad (d,|N\cap N|)\to\text{计数}:\ (1,2){:}50,\ (2,2){:}149,\ (3,0){:}912✓$$
$$\therefore\ \boxed{|N[c]\cap N[c']|=2\ \text{对一切 }d\in\{1,2\};\ =0\ \text{对 }d\ge3}$$
$$\text{几何原因}:\ d{=}1\ \text{时交集}＝\{c,c'\}\ \text{两点};\ \text{不存在同时距二者为 }1\ \text{的第三点}（\textbf{Hamming 空间无三角形}）$$
$$\therefore\ \text{你写 }I(1)=10\ ✗\ ——\ \text{（}10\ \text{似为球内点数 }11\ \text{之误植，或与闭邻域混淆）}$$

## §2 ② 恒等式之正确形式（**✓✓ 精确相等**）

| 形式 | 值（120-code） | 判定 |
|---|---|---|
| $\Sigma_x\binom{\mu(x)}2$（实测） | $398$ | — |
| $10N_1+2N_2$（你的） | $798$ | ✗ |
| $\mathbf{2}N_1+\mathbf{2}N_2$（正确） | $\mathbf{398}$ | **✓✓ 完全相等** |
| $M(A_1+A_2)$（正确） | $398.0$ | ✓ |
| $530A_1+106A_2$（你的） | $704.9$ | ✗ |

$$\therefore\ \Sigma_x\tbinom{\mu(x)}2=2(N_1+N_2)=M(A_1+A_2)\quad(\textbf{亦}＝E+T_2,\ \text{见 }29\text{u})✓$$

## §3 ③ 为何它是恒等式而非约束（**✗ 关键**）

$$\Sigma_x\tbinom{\mu(x)}2\ \text{与}\ N_1+N_2\ \text{互为\ \textbf{同一定义}（两侧数同一批\"码字对 × 公共覆盖点\"）}$$
$$\therefore\ \text{它\ \textbf{不削减}可行域};\ \text{配合 }\Sigma A_i=M,\ A_0=1,\ \Sigma A_iK_k(i)\ge0\ \Longrightarrow\ \text{恰是\ \textbf{经典 Delsarte／covering-LP}}✓$$
$$\text{（你的 Krawtchouk 部分\ \textbf{写对了} ✓；120-code 实测通过 —— 但本会话已验：该 LP 对 }M{=}105/106/110/120\ \textbf{皆可行}）$$

## §4 ④ 该框架之已知上限（**本会话实测**）

$$\text{covering 在距离分布语言中之推论}:\ \text{球界 }94\ \big|\ \text{van Wee }103\ \big|\ \text{Zhang（非该语言）}105\ \big|\ \text{SDP-3 }105.2223\Rightarrow106$$
$$\therefore\ \boxed{\text{本框架\ \textbf{已封闭}；出不了 }107}✗$$

## §5 ★ 三重预检（**此后一切候选必先过 —— 本会话教训之固化**）

$$\textbf{P-a（数值预检）}:\ \text{候选之全部定义值、系数、恒等式\ \textbf{先实测};\ \text{任一不符即弃}$$
$$\text{（本会话因未先测而废者}:\ I(1){=}10\ \star\ \text{差因子 }2;\ d_2{+}q\le9d_1\ (49/120);\ (21{-}d_1);\ T_3{=}175;\ \text{等共 }6\ \text{处）}$$
$$\textbf{P-b（归位预检）}:\ \text{若候选可表为}\ (A_1,\ldots,A_{10})\ \text{之函数}\ \Longrightarrow\ \text{属结合方案层}\ \Longrightarrow\ \textbf{Delsarte 已覆盖}\ \Longrightarrow\ \text{无增益}✗$$
$$\textbf{P-c（燃料预检）}:\ \text{若候选之效力依赖\ \textbf{excess}}\ \Longrightarrow\ \textbf{逆趋势}\ (\text{excess 密度随 }M\ \text{递减}:\ 0.327\!\to\!0.155)\ \Longrightarrow\ \text{在 }M{=}106\ \text{处最弱}✗$$
$$\therefore\ \boxed{\text{三检皆过之候选，本会话\ \textbf{一个未见}};\ \text{亦未能在既有文献机制中找到（Zhang／Habsieger／van Wee 皆落 P-b 或 P-c）}}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "I(d)系数" "二阶恒等式非约束" "三重预检"
技术词 I(d)系数     命中文件数=0    ::
技术词 二阶恒等式非约束 命中文件数=0    ::
技术词 三重预检      命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量实测（$I(d)$ 与两式对比）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；**不主张**该课题不可做 ✓（仅陈述：已试诸框架皆落 P-b/P-c）
