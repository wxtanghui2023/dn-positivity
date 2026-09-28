# AUDIT-2026-09-28r — **$120$-code 删点实验：单删 $0/120$、2-for-1 穷举 $0/7140$（皆负）**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:25 ✓
> **唐先生令**：上界路线——取 Kamenetsky 之 $120$-code 做删点/小改实验 ✓

**已查地图**：接续 `AUDIT-p/q`（真值定位／公式链）✓ ｜ 源：OEIS `A000983/a000983.txt`（Kamenetsky, 2020-07-27）✓

D0: 本档对象 ＝ **档案已有**（$120$-code／覆盖重数／私有域——无新数学对象 ✓）
D1: 0（产出＝**单删 ＋ 2-for-1 之穷举负结果 ＋ 一处独立验证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 单删（}120\ \text{次）}:\ \mathbf{0/120}\ \text{可删} \Longrightarrow 120\ \text{为\ inclusion-minimal}\ ✓}$$
$$\boxed{\text{② 2-for-1（删 2 加 1，}\mathbf{7140}\ \text{对\ \textbf{穷举}}）:\ \mathbf{0/7140}\ \text{可行} \Longrightarrow \text{本 }120\text{-code}\ \textbf{不能}降到 119 ⚠️}$$
$$\boxed{\text{③ ★独立验证}:\ \text{覆盖重数分布与档案 }120\text{-code 校准数据\ \textbf{逐项一致}} ✓✓}$$

## §1 源数据（**逐字核 ✓**）

$$\text{OEIS}\ \texttt{A000983/a000983.txt}:\ \text{Dmitry Kamenetsky, "Best known solutions for }n\le11",\ \textbf{27/07/2020};\ \textbf{a(10)<=120}\ ✓$$
$$\text{解析}:120\ \text{个 }10\text{-bit 串};\ \text{去重后}|C|=\mathbf{120};\ \text{覆盖核验}\ \mathbf{1024/1024}\ \checkmark$$

## §2 excess 核验（**与唐先生算术一致 ✓**）

$$\sum_x\big(a(x)-1\big)\ \overset{\textbf{实测}}{=}\ \mathbf{296}\ =\ 11\times120-1024\ \checkmark$$

## §3 ★ 覆盖重数分布（**独立验证 ✓✓**）

$$\text{实测}\ a(x)\ \text{之分布}:\ \big\{(1,801),\ (2,172),\ (3,36),\ (4,8),\ (5,7)\big\}$$
$$\text{档案}\ \texttt{EXCESS-2026-09-25}\ \text{所存之 }120\text{-code 校准数据}:\ \delta\ \text{分布}\ \{0{:}801,\ 1{:}172,\ 2{:}36,\ 3{:}8,\ 4{:}7\}\ \checkmark$$
$$\boxed{\text{逐项一致} \Longrightarrow \text{档案当日所存者即此 Kamenetsky 构造}}\ ✓✓$$

## §4 ① 单删实验（$\mathbf{0/120}$ ✓）

$$\forall c\in C:\ \text{删 }c\ \text{后失覆盖} \Longrightarrow \exists\ \text{私有域点};\quad \Sigma\,priv=801,\quad \min_c priv(c)=\mathbf 2,\quad \max=11$$
$$\text{无私有域之 codeword 数}=\mathbf{0}/120 \Longrightarrow \boxed{120\ \text{为\ inclusion-minimal}}\ ✓$$

## §5 ② 2-for-1 实验（**穷举 7140 对 ✓✓**）

$$\text{判据}:\ \text{删 }\{c_1,c_2\}\ \text{后失覆盖集 }U=\{x:own(x)\subseteq\{c_1,c_2\}\};\ \text{可行}\iff\exists p:\ U\subseteq B_1(p)$$
$$\textbf{实测}:\ \text{穷举 }C(120,2)=7140\ \text{对} \Longrightarrow \textbf{0 对可行}\ ✗$$
$$\text{私有域大小分布}:\ \{(2,2),(3,4),(4,3),(5,10),(6,52),(7,11),(8,20),(9,12),(11,6)\}$$
$$\text{失覆盖集大小（随机 }20000\ \text{对}）:\ \min=\mathbf 4\ \text{（}\le11\ \text{本可行）但皆非\ \textbf{球相容}}}\ ⚠️$$

## §6 ★ 结构性读数（**本档要点 ✓**）

$$\boxed{U\ \text{从不是"球相容集"——}\nexists p:\ U\subseteq B_1(p)}\quad\big(|U|\ \text{可小至 }4\ \text{而仍无共同中心}\big)$$
$$\therefore\ \text{阻力非"数量不足"（}|U|\le11\ \text{常成立），而是\ \textbf{局部几何}（无共同中心）}\ ✓$$
$$\text{与旧档案之"球交"结构一致（球交}\le2\big)\ ⚠️$$

## §7 判定与建议（**待唐先生定 ✓**）

$$\boxed{\text{上界路线（此码）:\ 单删 ＋ 2-for-1 皆负} \Longrightarrow \text{该 }120\text{-code 在局部尺度上\ \textbf{已紧}}}\ ✓$$
$$\textbf{未做（候选）}:\ \text{① 3-for-2 ／一般 }k\text{-for-}(k-1)\ \text{穷举（组合爆炸）};\ \text{② 换\ \textbf{其他} }120\text{-code};\ \text{③ 非局部构造（从零构造 }119\big)}\ ⚠️$$
$$\textbf{诚实}:\ \text{本结果\ \textbf{只}针对此码};\ \text{\textbf{不}排除他码可降} ✗$$

## §8 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "删点实验" "两换一" "球相容集"
技术词 删点实验   命中文件数=0    ::
技术词 两换一    命中文件数=0    ::
技术词 球相容集   命中文件数=0    ::
```

## §9 边界（硬 ✓）

- 有限穷举（$120$＋$7140$ 次覆盖核验）＋ 外部文件（Kamenetsky）＋ 档案交叉验证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**不主张** 119 不存在 ✗（V290）
- §7 之候选**未做** ✗；**不主张**上界路线已死 ⚠️
