已查地图：已跑 scripts/prework_map_check.sh van Wee Lemma 8 Theorem 9 等号 b≤2 ⟹ 执行自 `ALG-VW-2026-09-27-equality-reformulation-...`（✓）＋ 唐先生 2026-09-27 12:56（给出等号链 ✓）；本档 = **等号链 source-verified ＋ 数值 8/8 审计 ＋ 全部推论** ✓✓。
D0: 本档对象 = $b\le2$ 的自足推导（van Wee 原文 ＋ 等号分析）
D1: 3（**链路自足化 ✓✓**；**数值审计 8/8×2 全过 ✓✓**；**推论集合（matching/二部结构）✓**）

# van Wee 等号链（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BL-1 ⭐链路 ✓✓)}\ \text{van Wee 原文已核（TU/e 仓储 8.28\,MB ✓）}:\ \text{Def 1（excess）＋ Lemma 1a（总 excess 恒等式）＋ Lemma 3b}（z\in Z\Rightarrow|B_R(z)\cap C|\ge2\text{）＋ }\textbf{Lemma 8}\text{（局部 excess）＋ Theorem 9（全局计数）＋ Corollary 1a/b} ✓✓}$$
$$\boxed{\textbf{(BL-2 等号分析 ✓✓)}\ M=2^n/n\ \Longrightarrow\ |A|=\sum_{a\in A}E(B_1(a))=(n-1)\sum_i i|Z_i|\ \Longrightarrow\ \textbf{每步取等}\ \Longrightarrow\ \boxed{b(x)\in\{1,2\}\ \forall x}\ ✓✓}$$
$$\boxed{\textbf{(BL-3 全部推论 ✓✓)}\ n=2^m\ (\text{vW 取等})\ \Longrightarrow\ d_1(c)\le1\ \text{（\textbf{matching}）};\ J_2=2A_1;\ J_3=J_6=0;\ \boxed{A_1+A_2=M/2};\ \text{＋\textbf{二部结构}}:\ \deg_A(a)=1,\ \deg_A(z)=n-1\ ✓✓}$$
$$\boxed{\textbf{(BL-4 P1-2 现状 ⚠️)}\ \text{低阶 5/7 分量已被强制固定};\ \textbf{剩余仅两}:\ \boxed{\Sigma_ia_i^2,\ J_7=\Sigma q_{ij}^2}\ ✓\ \Longrightarrow\ \text{P1-2 精确压缩到最后两个二阶集中度不变量，仍 \textbf{OPEN} ✓}$$
$$
$$
```

---

## §1 source-first：van Wee 原文锚点（**✓ 逐字，TU/e 353803.pdf**）

```
$$\text{Def 1}:\ E_C(V):=\sum_{c\in C}|B_R(c)\cap V|-\Big|\bigcup_{c\in C}B_R(c)\cap V\Big|\ ✓\ \text{（excess 定义）};\qquad \text{Lemma 1a}:\ E_C(\mathbb F_2^n)=|C|V(n,R)-2^n\ ✓$$
$$\text{Lemma 3b}:\ z\in Z\Longrightarrow|B_R(z)\cap C|\ge2\ ✓;\qquad \text{Lemma 4a/b（单调性/可加性）} ✓$$
$$\textbf{Lemma 8（逐字 ✓）}:\ d(x,C)=R\ \Longrightarrow\ E_C(B_1(x))\ \ge\ (R+1)\big\lceil\tfrac{n+1}{R+1}\big\rceil-n-1\ ✓;\qquad \text{证明用}|B_R(c)\cap B_1(x)|\in\{0,R+1\}\ ✓$$
$$\qquad R=1,\ n\ \text{偶}:\ \lceil\tfrac{n+1}{2}\rceil=\tfrac n2+1\ \Longrightarrow\ \boxed{E_C(B_1(a))\ge1\qquad\forall a:\ d(a,C)=1}\ ✓\ \text{（即 }a\notin C\ \text{——\textbf{这正是此前缺的局部非负量} ✓✓）}$$
$$\textbf{Theorem 9 的计数（原文 ✓）}:\ A:=\{a:d(a,C)=R\};\ |A|\ge2^n-|C|V_2(n,R-1)\ ✓;\ \forall z\in Z:\ |A\cap B_1(z)|\le|B_1(z)|-(R+1)\ \text{（由 Lemma 3b ＋ 原文 case 分析 ✓）}$$
$$\textbf{Corollary 1a/b（原文 ✓）}:\ K(n,1)\ge2^n/n\ \text{（}(15)\text{）};\qquad K(2^r,1)=2^{2^r-r}\ \text{（}(16)\text{）}\ \text{——}\textbf{即 }n=2^m\ \text{格} ✓✓$$
$$
$$
```

---

## §2 等号分析（**✓ 唐先生 12:56 给出，逻辑我逐步核过 ✓**）

```
$$\text{设 }R=1,\ n\ \text{偶},\ M=2^n/n\ ✓\ \Longrightarrow\ A=\mathbb F_2^n\setminus C\ \text{（覆盖 ⟹ 非码字 }d(\cdot,C)=1\ ✓）;\ |A|=2^n-M=\tfrac{n-1}{n}2^n\ ✓$$
$$\text{两层不等式}:\quad |A|\ \le\ \sum_{a\in A}\underbrace{E_C(B_1(a))}_{\ge1}\ \le\ \sum_{z\in Z}\delta(z)\underbrace{|A\cap B_1(z)|}_{\le n-1}\ \le\ (n-1)\sum_{i\ge1}i|Z_i|\ ✓$$
$$\text{由 Lemma 1a}:\ \sum_{i\ge1}i|Z_i|=M(n+1)-2^n=\tfrac{2^n}{n}=M\ \Longrightarrow\ (n-1)\sum_i i|Z_i|=(n-1)M=\tfrac{n-1}{n}2^n=\mathbf{|A|}\ \text{——\textbf{两端相等} ✓✓}$$
$$\Longrightarrow\ \text{所有 }"\le"\ \text{取等（各项非负 ✓）}\ \Longrightarrow\ \text{(i) }E_C(B_1(a))=1\ \forall a\notin C\ ✓;\quad \text{(ii) }|A\cap B_1(z)|=n-1\ \forall z\in Z\ ✓$$
$$\Longrightarrow\ b(z)=|C\cap B_1(z)|=(n+1)-(n-1)=2\ \forall z\in Z\ \Longrightarrow\ \boxed{b(x)\in\{1,2\}\ \forall x}\ ✓✓$$
$$
$$
```

---

## §3 数值审计（**✓✓ 8/8 × 2 码全过，本机 ✓**）

```
$$\begin{array}{c|c|c}
\text{推论（编号沿用唐先生 12:56）} & \text{Kéri }K\_8\_1 & H(7,4)\times\mathbb F_2\\
\hline
(20)\ b\in\{1,2\}\ \forall x & ✓✓ & ✓✓\\
(21)\ Z_i=\varnothing\ (i\ge2)\ \text{（三重覆盖点数}=0\text{）} & ✓\ (0) & ✓\ (0)\\
(22)\ |Z|=M & ✓\ (32=32) & ✓\ (32=32)\\
(16)\ \forall a\notin C:\ \sum_{B_1(a)}\delta=1 & ✓✓ & ✓✓\\
(18)\ \forall z\in Z:\ |A\cap B_1(z)|=n-1=7 & ✓✓ & ✓✓\\
(24)\ \text{二部}:\ |A|=(n-1)|Z| & ✓✓ & ✓✓\\
(26)\ d_1(c)\le1\ \forall c\ \text{（matching）} & ✓✓\ (d_1^{\max}=1) & ✓✓\ (d_1^{\max}=1)\\
(26)\ J_2=2A_1 & ✓\ (16=16) & ✓\ (32=32)\\
(28)\ A_1+A_2=M/2 & ✓✓\ (16=16) & ✓✓\ (16=16)\\
\end{array}$$
$$\textbf{判读 ✓✓}:\ \text{等号链的\textbf{每一个推论}在两个 }n=8\ \text{码上\textbf{精确成立}};\ \text{且两码 }A_1\ \text{不同}（8\ \text{vs}\ 16\text{）}\ \text{—— 恰是 }(A_1,A_2)\ \text{桶的分裂自由 ✓}$$
$$
$$
```

---

## §4 最后一个剩余推论（**新 ✓**）

```
$$\text{二部 incidence（}(23)(24)\text{）}:\quad \mathcal A\ \text{（非码字 ✓）}\ \longleftrightarrow\ Z=\{x:b(x)=2\}\ \text{（}|Z|=M\ ✓\text{）},\qquad \deg_{\!Z}(a)=1\ \forall a,\quad \deg_{\!\mathcal A}(z)=n-1\ \forall z\ ✓$$
$$\qquad\Longrightarrow\ \text{这是一个 }(n{-}1)\text{-正则二部图（}|\mathcal A|=(n-1)|Z|\ ✓\text{）}\ \text{——\textbf{强设计型结构} ✓✓（比 }b\le2\ \text{更强 ✓）}$$
$$\qquad\text{可用于}:\ \text{把 }\Sigma a_i^2\ \text{与 }\Sigma q_{ij}^2\ \text{的问题转化为该二部图的坐标投影问题 ✓（下一步候选 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为 **source-first 逐字**（van Wee 原文 TU/e 353803.pdf ✓，含 Lemma 8 与 Theorem 9 ✓✓）；§2 为**唐先生给出的等号链，逻辑我逐步核过 ✓**；§3 为**本机数值审计 ✓✓**；§4 为**新推论** ✓
- ⚠️ **归属**：局部引理（Lemma 8）＝ van Wee 1988 ✓；全局计数（Theorem 9）＝ van Wee 1988 ✓；**等号分析** ＝ 唐先生本轮给出 ✓（此前档案仅有 Lemma 3.18 黑箱 ✓）；推论 (20)–(28) ＋ 二部结构 ＝ 本轮 ✓
- **未**声称 P1-2 成立/失败 ✗（剩余两量仍 OPEN ✓）；**未**改动 119 UNKNOWN ✓；**未**跑 SAT ✓
- ⚠️ 注意 $n$ 偶 ≠ $n=2^m$：vW 取等需 $|C|=2^n/n$ ✓，而整数性要求 $n\mid2^n$ ⟹ $n=2^m$ ✓（故 [20][21] 的适用域是 $n=2^m$ ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：等号链（self-contained $b\le2$）、二部 incidence 结构、8/8 数值审计
- **档案已有（引用，不列为提出）**：van Wee 界、nearly-perfect、Lemma 3.18（现已可弃用 ✓）、$b$、$d_1$、$J$、matching 定理


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 等号链        命中文件数=1    :: ./CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md 
技术词 二部 incidence 结构 命中文件数=1    :: ./CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md
```
- **本档新增**：等号链（self-contained $b\le2$）、二部 incidence 结构、8/8 数值审计（见上方命中数；0 命中者为自造语／内部标签 ✓）
