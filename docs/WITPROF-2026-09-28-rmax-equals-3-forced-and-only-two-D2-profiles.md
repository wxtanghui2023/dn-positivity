# WITPROF-2026-09-28 — **$r_{\max}{=}3$ 被逼出；$D_2\in\{5,6\}$ 只剩两种 profile；P-3 被推翻**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:58 令 ✓）**：$P$-层二阶碰撞；**零程序计算**（仅整数/有限穷举核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-448／C-447／C-446，非新案 ✓）**
`docs/WITCODE-2026-09-28-…`（**$e(A){=}0$／$D_2\ge5$ 被强制／$D_2\le18$ ✓✓**）｜`docs/WITA0-2026-09-28-…`（**$d(A_0)\ge3$ ✓✓**）｜`docs/WITSAT2-2026-09-28-…`（**饱和仅 $t{=}12$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** $P$-层二阶碰撞／$r$-profile 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首证 $r_A(p)\le3$（$k^2\le12$）＋ $r_{\max}{=}3$ 被逼出＋$D_2\le6$＋$D_2\in\{5,6\}$ 恰两 profile（$3^3 2^1 1^1$／$3^4$）＋ 逼出"第二共同邻点封闭条件"＋ 推翻 P-3** ✓）
**[RESEARCH]**

---

## §0 结论（**$r_{\max}{=}3$ 被逼出 ✓✓✓｜$D_2\in\{5,6\}$ 两 profile ✓✓✓｜P-3 ✗✗推翻**）

$$\textbf{设定 ✓}:\ t=12\Rightarrow|A|=45,\ |U^c|=393✓;\ r_A|_{U^c}\equiv1✓;\ \sum_{y\in U}r_A(y)=12✓;\ e(A)=0✓\ \big(\text{C-448 ✓✓}\big)$$
$$\qquad N(P)\cap A_0=\varnothing✓\Longrightarrow \boxed{r_A(p)=|N(p)\cap A_1|=:r(p)\quad(p\in P)}✓✓\ \big(\text{$A_0$ 从 }P\text{-层彻底消掉 ✓}\big)$$
$$\qquad P:=N(A_1)\cap U✓;\quad n_j:=|\{p\in P:r(p)=j\}|✓;\quad \sum_j jn_j=12✓;\quad \boxed{2D_2=\sum_{p\in P}\binom{r(p)}2=\sum_j\binom j2n_j}✓✓$$
$$\boxed{\textbf{(1) ✗必改}:\ \text{唐先生 §1 的}\ D_2=\sum_P\binom{r_p}2\ \textbf{不对}\ ✗\ \text{（因子 2 又一次 ✗，同型第 3 次）}:\ \textbf{正确}\ 2D_2=\sum_P\binom{r_p}2✓✓}$$
$$\qquad\textbf{理由 ✓✓}:\ \text{距离-2 对有\ \textbf{恰好 2 个}}\ \text{共同邻点}\Longrightarrow\sum_{y\in V}\binom{r_A(y)}2=2D_2✓✓$$
$$\boxed{\textbf{(2) ✗✗唐先生 §2 的例子不可能（本档纠正其"纠正"）}:\ \text{型}\ (2,2,2,2,2,1,1):\ \sum r=12✓\ \text{但}\ \sum\binom r2=\mathbf 5\ \text{奇}\Longrightarrow2D_2=5\Longrightarrow D_2=2.5\ \textbf{非整数}\ ✗✗}$$
$$\qquad\Longrightarrow\ \text{该型\ \textbf{不存在} ✓✓};\quad \text{故 }D_2=5\ \textbf{必须}出现\ r\ge3\ ✓✓\ \big(\text{与唐先生 §2 结论相反 ✓}\big)$$
$$\boxed{\textbf{(3) ★★★$r_{\max}\le3$（新 ✓✓✓）}:\ \text{设}\ r(p)=k,\ \text{支撑}\ S\subseteq[9],\ |S|=k✓\ \big(\text{平移 }p\mapsto0✓\big)}$$
$$\qquad\text{则}\ \{e_i:i\in S\}\subseteq A_1✓\ \text{两两距离 2}\ ✓;\quad \text{对每对}\ i<j\ \text{其第二共同邻点}\ e_i\oplus e_j\in P✓\ \text{且}\ r\ge2✓✓$$
$$\qquad\qquad\boxed{\Rightarrow\ \sum_{p'\in P}r(p')\ \ge\ k\ +\ 2\binom k2\ =\ k^2}\ ✓✓\ \big(\text{被迫点与 }p\ \text{及 }k\ \text{个一阶点\ \textbf{互异} ✓✓}\big)$$
$$\qquad\qquad\Longrightarrow\ k^2\le12\Longrightarrow\boxed{k\le3}✓✓\ \big(k{=}3:9\le12✓;\ k{=}4:16>12\ ✗\big)$$
$$\boxed{\textbf{(4) ★★★$r_{\max}=3$ 被逼出 ⟹ P-3 \textbf{被推翻}（本档核心）}:\ \text{C-448 已证}\ D_2\ge5✓ \Longrightarrow\ \sum\binom r2\ge10✓}$$
$$\qquad\text{若}\ r_{\max}\le2:\ \sum\binom r2=n_2\ \text{且}\ \sum r=2n_2+n_1=12\Longrightarrow\boxed{D_2=\tfrac{n_2}2\le3}\ ✓✓\ \big(n_2=2D_2\Rightarrow n_1=12-4D_2\ge0✓\big)$$
$$\qquad\Longrightarrow\ \text{与 }D_2\ge5\ \textbf{直接矛盾}\ ✗✗ \Longrightarrow\ \boxed{\exists\,p\in P:\ r_A(p)\ge3}\ ✓✓\ \Longrightarrow\ \text{与 (3) 合}:\ \boxed{r_{\max}=3}\ ✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{唐先生 §9 的 Lemma P-3（}r(p)\le2\ \forall p\text{）\textbf{不可证且为假}}✗✗;\ \text{§6 的 Case II（}r_{\max}{=}2\text{）\textbf{为空}}✗;\ \textbf{Case I 是唯一分支}✓✓$$
$$\boxed{\textbf{(5) ★★★$D_2\in\{5,6\}$，恰两种 profile（本档穷举 ✓✓✓）}:\ \text{由 }k\le3:\ \sum\binom r2=3n_3+n_2✓\ \text{且}\ \sum r=3n_3+2n_2+n_1=12✓}$$
$$\qquad\Longrightarrow\ \sum\binom r2\le12\ \big(\text{极大 }3n_3=12⇔n_3{=}4✓\big)\Longrightarrow\boxed{D_2\le6}✓✓;\quad \text{而 }D_2\ge5\Longrightarrow\boxed{D_2\in\{5,6\}}✓✓$$
$$\qquad\qquad\boxed{D_2=5\iff (n_3,n_2,n_1)=(3,1,1)\iff\text{profile }3^32^11^1}✓✓$$
$$\qquad\qquad\boxed{D_2=6\iff (n_3,n_2,n_1)=(4,0,0)\iff\text{profile }3^4}✓✓$$
$$\qquad\Longrightarrow\ \text{搜索空间由 }D_2\in[5,18]\ \text{暴缩为\ \textbf{两种 profile}}\ ✓✓✓\ \big(\text{穷举核验 ✓}\big)$$
$$\boxed{\textbf{(6) ★★"第二共同邻点封闭条件"（新 ✓✓）}:\ \forall p\in P,\ \forall\ \{i,j\}\subseteq\operatorname{supp}(p)\ \big(=\{i:p\oplus e_i\in A_1\}✓\big):}$$
$$\qquad\boxed{p\oplus e_i\oplus e_j\ \in\ P\ \ \text{且}\ \ r(p\oplus e_i\oplus e_j)\ \ge\ 2}✓✓\ \big(\text{否则该对只有 1 个共同邻点}\ ✗\ \text{或 }r_A{=}1\ \text{矛盾 ✓}\big)$$
$$\qquad\Longrightarrow\ \text{每个 }r{=}3\ \text{点必生 3 个被迫点（各 }r\ge2\text{）}✓;\ \text{这是把 profile 与\ \textbf{几何}\ 绑死的唯一新接口 ✓✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓（除因子 2 ✗）}:\ \sum_P r(p)=12✓,\ 1\le r\le9✓,\ \text{载体干净 ✓✓};\ \textbf{但}\ D_2=\sum_P\binom{r_p}2\ ✗ \to 2D_2✓✓$$
$$\textbf{§2 ✗✗}:\ (2,2,2,2,2,1,1)\ \text{给}\ 2D_2=5\ ✗\ \text{非整数}\Longrightarrow\text{该型不存在 ✓✓};\ (3,2,2,2,1,1,1)\ \text{给}\ 2D_2=6\Longrightarrow D_2=3✓\ \text{（非 6 ✗）}$$
$$\qquad\Longrightarrow\ \text{唐先生"仅 }\sum r=12\ \text{不能得等价性"之\ \textbf{方法提醒正确} ✓✓，但\ \textbf{例子算错} ✗}$$
$$\textbf{§3 ✓（}s(p)=r(p)-1\text{）}:\ 2D_2=\sum s^2+\sum s✓✓\ \text{（核对：}\sum(s{+}1)s=\sum r(r{-}1)✓\big)$$
$$\textbf{§4 ✓（形式 ✓）}:\ \text{"}D_2=5\ \text{的 }r\le2\ \text{型＝}(2^5 1^2)\text{"}\ ✗\ \text{（见 §0(2)）；正确：}D_2{=}5\ \text{需 }r\ge3✓✓$$
$$\textbf{§5 ✓（}2^6\Longrightarrow D_2=3\text{）}:\ \sum\binom r2=6\Longrightarrow D_2=3✓\ \text{—— 故"六个 }r{=}2\text{"只给 }D_2{=}3✗\ \text{不能杀 }D_2{\ge}5✓\big)$$
$$\textbf{§6 ✓（二分 ✓）}:\ D_2\ge5\Rightarrow(n_2\ge5\ \vee\ \exists r\ge3)✓\ \text{—— 但由 (4)：}n_2\ \text{支为空}\ ✗✓$$
$$\textbf{§7 ✓✓}:\ r(p)\ge3\Longrightarrow A_1\ \text{含距离-2 三角形}\ ✓✓\ \big(\text{共同邻点 }p\Rightarrow d\le2✓;\ e(A_1){=}0\Rightarrow d\ne1✓\big)\ \text{—— 且现已}\ \textbf{被逼出必存在}\ ✓✓$$
$$\textbf{§8 ✗}:\ n_1=12-2|E_H|\ ✗ \to \textbf{正确}\ n_1=12-4D_2✓✓\ \big(\text{每距离-2 对有 2 个共同邻点}\Rightarrow n_2=2D_2✓\big)\Longrightarrow D_2\le3\ ✗\ \text{（非 }\le6✗\big)$$
$$\textbf{§9–§10 ✗（目标须换）}:\ \text{P-3 假}\ ✗✗;\ \text{正确链：}r_{\max}{=}3\ \text{被逼}\Rightarrow\ \text{仅两 profile}\ \Rightarrow\ \text{逐型攻封闭条件 ✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{r_A(p)\le3}\ \big(k^2\le12✓✓\big);\ \text{② }\boxed{r_{\max}=3}\ \text{被逼}✓✓✓;\ \text{③ }\boxed{D_2\le6}✓✓;\ \text{④ }\boxed{D_2\in\{5,6\}}\ \text{仅两 profile}✓✓✓;\ \text{⑤ 第二共同邻点封闭条件 ✓✓};\ \text{⑥ }A_0\ \text{可消（}r_A(p)=r_{A_1}(p)✓\big)✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{Lemma P-3（}r\le2\ ∀p\text{）✗✗};\ \text{Case II（}r_{\max}{=}2\text{）为空 ✗};\ \text{型 }(2^5 1^2)\ ✗;\ n_1=12-2D_2\ ✗;\ D_2=\sum_P\binom{r_p}2\ ✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ t{=}12\ \text{的关闭};\ \text{两 profile 之几何可行性（}3^32^11^1／3^4\text{）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 攻 profile }3^4\ \big(\text{4 个 }r{=}3\ \text{点、12 对、12 个被迫点须落回 }P\ \text{的封闭自洽 ✓}\big);\ \text{② 攻 profile }3^32^11^1;\ \text{③ 用 (6) 把 profile 转成 }A_1\ \text{上的 }F_2^3\text{-型立方结构 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "剖面" "封闭条件" "二阶碰撞剖面"
技术词 剖面       命中文件数=0    ::
技术词 封闭条件   命中文件数=0    ::
技术词 二阶碰撞剖面 命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 剖面 | 0 | 0 | 0（本档自造标签 ✓） |
| 封闭条件 | 0 | 0 | 0（本档自造标签 ✓） |
| 二阶碰撞剖面 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅整数与有限 profile 穷举 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（$2D_2$ 因子 ＋ §2 例子）与 **P-3 推翻** 已在 §0(1)(2)(4) 显式标注 ✓✓
- **$r_{\max}{=}3$ 与 $D_2\in\{5,6\}$ 必须同时引用** ✓✓（否则误得 $r\le2$ 分支 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $t{=}12$ 已关闭 ✗（V290）
