# AUDIT-2026-09-29l — **第三次同型误读：Habsieger 之 parity 管的是\ \textbf{球 excess}，非\ \textbf{点计数} $|D\cap\Gamma(x)|$**

> **性质**：**实测核验 ＋ 纠错（第三次同型）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 11:1x ✓
> **唐先生令**：「继续」✓

**已查地图**：接续 `AUDIT-29j`（同型误读第二次）／`29h`（Habsieger 逐字 (1.7)(1.8)）✓

D0: 本档对象 ＝ **档案已有**（$\mu$／$r(x)$／$s(c)$／球 excess——无新数学对象 ✓）
D1: 0（产出＝**两处 parity 前提否证 ＋ 恒等式全部证实 ＋ 同型警示** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗✗ (A) 假}:\ x\notin D\ \text{时}\ \mu(x)=r(x)\ \textbf{非恒奇};\ \text{实测 }\mu\in\{1,2,3,4,5\},\ \mathbf{138/904}\ \text{为偶}}$$
$$\boxed{\text{② ✗✗ (B) 假}:\ c\in D\ \text{时}\ s(c)\ \textbf{非恒奇};\ \text{实测 }s\in\{0,1,2,3\},\ \mathbf{78/120}\ \text{为偶}}$$
$$\boxed{\text{③ ✗ 故 }A_1\ge53\ \textbf{为假}（实测 }A_1=50\text{）};\ \text{"18 预算"与 }A_2\ge27\ \textbf{随之崩}}$$
$$\boxed{\text{④ ✓✓ 你的恒等式与 (N)\ \textbf{全部正确}}（逐条实测）;\ \text{唯有那两条 parity 前提须换对象}}$$

## §1 ①② 两处前提之实测否证（**✗✗**）

$$\textbf{Habsieger (1.7)(1.8) 之真对象}:\quad \delta_{N[v]}(D)\ :=\ \sum_{y\in N[v]}\bigl(|D\cap N[y]|-1\bigr)\quad(\textbf{球内 excess 之和})$$
$$\text{（逐字旁证}:\ \texttt{Wu–Chen}\ \text{之}\ \delta_{V(Q_n)}(D)=(n+1)|D|-|V(Q_n)|\ \text{恰给出此定义}\ ✓）$$

| 断言 | 实测（120-code） | 判定 |
|---|---|---|
| (A) $x\notin D\Rightarrow\mu(x)$ 奇 | $\mu$ 分布 $\{1{:}746,2{:}136,3{:}13,4{:}2,5{:}7\}$；**偶者 $138/904$** | ✗✗ |
| (B) $c\in D\Rightarrow s(c)$ 奇 | $s$ 分布 $\{0{:}55,1{:}36,2{:}23,3{:}6\}$；**偶者 $78/120$** | ✗✗ |

$$\text{（}\sum_c s(c)=100=2A_1\ ✓\ \text{—— 该恒等式本身正确）}$$

## §2 ④ 真正成立之 parity（**✓✓ 实测 100%**）

$$\boxed{c\in D\ \Longrightarrow\ \delta_{N[c]}(D)\ \text{偶}\ (n{=}10\Rightarrow\equiv0\bmod2)}\qquad\textbf{实测 }120/120\ ✓$$
$$\boxed{x\notin D\ \Longrightarrow\ \delta_{N[x]}(D)\ \text{奇}\ (\equiv11\equiv1\bmod2)}\qquad\textbf{实测 }904/904\ ✓$$
$$\therefore\ \text{parity 之对象是\ \textbf{球 excess}（邻域求和），\textbf{不是}点计数 }|D\cap\Gamma(x)|\ \text{或其特例 }\mu(x),\ s(c)$$

## §3 ③ 崩塌链（**✗**）

$$(B)\Rightarrow 2A_1=\sum_cs(c)\ge106\Rightarrow A_1\ge53\quad\text{—— (B) 假 ⟹\ \textbf{无从推出}}✗$$
$$\textbf{实测}:\ A_1=\mathbf{50}<53\ ✗\ \text{（且 }A_1\le71\ \text{才为真：由}\ \sum_{x\notin D}r(x)=10M-2A_1\ge1024-M\ \Longrightarrow\ A_1\le(9M+1024)/2\big|_{M=106}\!\!=71\ ✓）$$
$$\therefore\ \text{"18 预算"}(A_1{-}53)+(71{-}A_1)=18\ \text{与}\ A_2\ge27\ \text{皆\ \textbf{建在假前提上}}✗$$

## §4 ④ 你的恒等式（**✓ 逐条实测，全部正确**）

$$\boxed{\sum_{x\notin D}r(x)=10M-2A_1}\quad(120\text{-code}:\ 1100=1100\ ✓)$$
$$\boxed{E_{\rm out}=\sum_{x\notin D}(\mu(x)-1)=E-2A_1}\quad(196=296-100\ ✓)$$
$$\boxed{\sum_x\binom{\mu(x)}2=2(A_1+A_2);\quad \sum_{c\in D}\binom{\mu(c)}2=2A_1+\sum_c\binom{s(c)}2}\quad(398=2\cdot199\ ✓)$$
$$\boxed{\text{(N) }9A_1+A_2+3A_3\ \ge\ \tfrac{45M}{2}}\quad(120\text{-code}:\ 3335\ge2700\ ✓;\ M{=}106:\ \ge2385\ ✓)$$
$$\therefore\ \text{你的}\ \S1\text{--}\S7\ \text{之账本与 (N) 皆可保留};\ \text{唯一须弃者为 (A)(B) 及其下游}$$

## §5 ★ 同型警示（**第三次 ✗✗✗**）

$$\text{第一次}:\ \texttt{AUDIT-29h}\ \text{— 把}\ \sum\binom\delta2\ \text{与 surfeit}\ \delta_{N[v]}\ \text{混}\ (29g/29h)$$
$$\text{第二次}:\ \texttt{AUDIT-29j}\ \text{— 把球 excess 之 parity 用到点 excess}\ \mu-1$$
$$\text{第三次}:\ \textbf{本档}\ \text{— 把球 excess 之 parity 用到点计数}\ |D\cap\Gamma(x)|\ (\text{即 }\mu,\ s)$$
$$\therefore\ \boxed{\text{凡引 Habsieger parity，\ \textbf{必先写出}\ \delta_{N[v]}=\sum_{y\in N[v]}(|D\cap N[y]|-1)\ \text{再往下}}✓✓$$
$$\text{（即：parity 是\ \textbf{一阶邻域的求和量}，任何"某点的邻域计数"皆不得直接套）}$$

## §6 校正后之 106-specific 系统（**✓ 只留真者**）

$$\boxed{A_1\le71;\quad 9A_1+A_2+3A_3\ge2385;\quad 2(A_1+A_2)=\sum_x\binom{\mu(x)}2;\quad \sum_{x\notin D}r(x)=1060-2A_1\ge918}$$
$$\text{（另}\ \sum_{x\in A}(\text{球 excess})=1562-4(N_1{+}N_2)\ge918\Rightarrow N_1{+}N_2\le161\ \text{—— 见 }\texttt{AUDIT-29k}）$$
$$\therefore\ \text{缺口不变}:\ \text{须一条在 }M{=}106\ \text{失效之不等式};\ \text{本档未提供}$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "点计数非奇" "球excess才有parity" "第三次同型"
技术词 点计数非奇     命中文件数=0    ::
技术词 球excess才有parity  命中文件数=0    ::
技术词 第三次同型     命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **120-code 全量实测** ＋ 逐字对原文 ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）
