# AUDIT-2026-09-29j — **parity 属于『球 excess』，\ \textbf{不是}『点 excess』：你的 §8 那一步错，且方向恰好相反**

> **性质**：**实测核验 ＋ 纠错**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:3x ✓
> **唐先生令**：「继续往下核」✓

**已查地图**：接续 `AUDIT-29i`（Thm 5 ≡ Thm 16 → 103；余量 360）／`29h`（Habsieger 逐字）✓

D0: 本档对象 ＝ **档案已有**（$\delta$／excess／deep holes——无新数学对象 ✓）
D1: 0（产出＝**一处 parity 归属纠错 ＋ 方向反证 ＋ 校正后之 P1 陈述** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 你 }\S1\text{--}\S7\ \text{之退化还原与 }103\text{ 临界点：\textbf{全部正确}}（已对原文）}$$
$$\boxed{\text{② ✗✗ }e(x):=\mu(x)-1\ \textbf{不恒偶}:\ \text{实测深洞上分布 }\{0{:}746,1{:}136,2{:}13,3{:}2,4{:}7\};\ \mathbf{138/904}\ \text{为奇}}$$
$$\boxed{\text{③ ✓ 真正成立之 parity 属\ \textbf{球 excess} }E(B(x,1)):\ \text{全奇}\ (904/904)\ ⟹\ \ge1}$$
$$\boxed{\text{④ ★ 而且方向相反}:\ \text{该 parity 给出的是\ \textbf{上界} }(M{=}106{:}\ m\le180),\ \text{非下界}}✗$$

## §1 ② 纠错：点 excess 之 parity（**实测 ✗**）

$$\text{你的 }\S8:\ "\text{Habsieger }\delta_{N[x]}\equiv1\Rightarrow e(x)\equiv0\ (\mathrm{mod}\ 2)"$$
$$\textbf{问题}:\ \text{Habsieger 之同余对象是}\ \boxed{\delta_{N[v]}=\sum_{y\in N[v]}\bigl(\mu(y)-1\bigr)}\ (\text{球内 excess 之和}),\ \textbf{非}\ \mu(v)-1$$
$$\textbf{实测（120-code，deep holes）}:\ e(x)=\mu(x)-1\ \text{之分布}\ \{0{:}746,\ 1{:}136,\ 2{:}13,\ 3{:}2,\ 4{:}7\}$$
$$\therefore\ \boxed{\text{有 }\mathbf{138}\ \text{个深洞其 }e\ \text{为奇数} \Longrightarrow "e\in2\mathbb Z_{\ge0}"\ \textbf{为假}}✗✗$$
$$\therefore\ \text{你的}"\sum e/2=71"\ \textbf{不成立}\ (\text{因 }\sum_{e\ \text{奇}}e\ \text{非 0 mod 2 之源被误消});\ \text{该计数链\ \textbf{断裂}}$$

## §2 ③ 真正之 parity（**✓ 实测**）

$$E(B(x,1)):=\sum_{y\in B_1(x)}\bigl(\mu(y)-1\bigr)\qquad(x\notin C)$$
$$\textbf{实测}:\ \text{奇偶分布}\ \{1{:}\mathbf{904}\}\ \Longrightarrow\ \textbf{全奇}\ ✓✓\ (\text{Habsieger }n{=}11\ \text{奇})$$
$$\text{（与 }\texttt{AUDIT-29g/29h}\ \text{之}\ \varepsilon{=}1\ \text{一致};\ \text{亦即 van Wee 之关键事实）}$$

## §3 两条聚合恒等式（**✓ 实测，供后续**）

$$\boxed{\sum_{x\in V}\sum_{y\in B_1(x)}e(y)\ =\ 11E}\qquad(120\text{-code}:\ 3256=11\cdot296\ ✓)$$
$$\boxed{\sum_{x\in C}\sum_{y\in B_1(x)}e(y)\ =\ 4(N_1{+}N_2)}\qquad(796=4\cdot199\ ✓)$$
$$\therefore\ \sum_{x\notin C}(\text{球 excess})\ =\ 11E-4(N_1{+}N_2)\qquad(120\text{-code}:\ 2460\ ✓)$$

## §4 ★ ④ 方向反证（**本档核心 ✗**）

$$\text{由李二项：}\ \text{球 excess}\ \ge1+2\cdot\mathbb 1[\text{球 excess}\ge3]\quad(\text{奇且}\ \ge1)$$
$$\therefore\ |A|+2m\ \le\ \sum_{x\in A}(\text{球 excess})\ \le\ 9E\qquad(A=\{x\notin C\},\ m=\#\{x\in A:\text{球 excess}\ge3\})$$
$$M{=}106:\quad 918+2m\ \le\ 9\cdot142=1278\ \Longrightarrow\ \boxed{m\ \le\ 180}\ (\text{上界})$$
$$\therefore\ \boxed{\text{parity ＋ 计数给出的是\ \textbf{上界}（球 excess 集中度有上限），\textbf{不是}下界}}$$
$$\text{而你 }\S8\text{--}\S9\ \text{所要的是\ \textbf{下界}（"至少 72 个点有 }e\ge2"\text{）} \Longrightarrow \textbf{方向相反}✗$$

## §5 校正后之 P1（**保留你的靶，去掉错的前提 ✓**）

$$\text{你的靶（}\S9\text{）本不需 parity}:\ \boxed{\text{若某 }M{=}106\ \text{码有}\ \ge72\ \text{个点满足}\ e(x)\ge2\ (\text{即 }\mu\ge3),\ \text{则}\ \sum_xe\ge144>142=E\Longrightarrow\bot}✓$$
$$\therefore\ \text{该靶\ \textbf{依然有效}（充分条件）；但其\ \textbf{前提不得由 parity 得出}（见 }\S1\text{）}$
$$\text{且\ \textbf{不能}由纯计数得出}:\ \text{若仅 }k\le71\ \text{点有 }e\ge2\ \text{而其余 }e\le1,\ \text{则}\ \sum e\le10k+(1024-k)=1024+9k\ \text{可远超 }142\ \Longrightarrow\ \textbf{计数不约束}$$
$$\therefore\ \boxed{\text{须\ \textbf{几何}论证（球交叠／深洞邻接结构），非 parity／非计数}}$$

## §6 点 excess 之真实结构（**✓ 替代 }\S8**）

$$\sum_x\binom{e(x)}2\ =\ \sum_x\binom{\mu(x)-1}2\ =102\ (120\text{-code});\qquad \#\{x:e(x)\ge2\}=51$$
$$\text{且}\ \sum_x\binom{\mu(x)}2=2(N_1{+}N_2)\ (\text{已证});\ \boxed{\sum_x\binom{e(x)}2=2(N_1{+}N_2)-E}\ ✓$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "点excess非偶" "球excess为奇" "方向相反"
技术词 点excess非偶   命中文件数=0    ::
技术词 球excess为奇   命中文件数=0    ::
技术词 方向相反     命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **120-code 全量实测 ＋ 逐字对原文** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
