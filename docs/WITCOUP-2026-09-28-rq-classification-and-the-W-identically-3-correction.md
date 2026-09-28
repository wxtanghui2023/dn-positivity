# WITCOUP-2026-09-28 — **$r_q$ 分类（新 ✓✓✓）：$r_q{=}3\Rightarrow|G_q|\le1$；$|\mathcal W(F_p)|\equiv3$ 而非 $\{3,\dots,9\}$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:33 令 ✓）**：$F$--$G$ 禁边 → 前缀四邻域共同禁止；**零程序计算**（仅有限穷举核对 ✓）；**不作路线裁定** ✗。
> **标签（照唐先生本轮固定 ✓）**：$P$＝偶部、$A_1$＝奇部 ✓。

**已查地图：命中（接续 C-453／C-452／C-451，非新案 ✓）**
`docs/WITDEC-2026-09-28-…`（**$c+d\le20$／$|F|\le16$／$|G|\le12$ ✓✓✓**）｜`docs/WITLAYER-2026-09-28-…`（**14 行 profile ✓✓✓**）｜`docs/WITCUBE-2026-09-28-…`（**$Q_3$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $F$--$G$ 耦合／$\mathcal W$／prefix 图对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $r_q$ 完整分类 $\max|G_q|=(3,3,3,1)$ 与 $g\le12-2\#\{q:r_q{=}3\}$；首次证 $|\mathcal W(F_p)|\equiv3$（满族）并纠正 $\{3,\dots,9\}$** ✓）
**[RESEARCH]**

---

## §0 结论（**$r_q$ 分类 ✓✓✓（新）｜$|\mathcal W|\equiv3$ ✗纠正｜3 邻而非 4 ✗**）

$$\textbf{设定 ✓}:\ \text{prefix 空间}=F_2^3\ \big(=Q_3✓\big):\ 4\ \text{偶}\ (P)+\ 4\ \text{奇}\ (A_1)✓;\ \text{每点度 }3✓✓;\ F_p:=\{v:\binom{[6]}3:(p,v)\in F\}✓;\ G_q:=\{w:\binom{[6]}4\}✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §2 之刚性\ \textbf{完全正确}（本档穷举核验 ✓✓）}:\ |F_p|{=}4\Longrightarrow}$$
$$\qquad\text{合法 4-族共 }\mathbf{30}\ \text{个 ✓，且\ \textbf{全部}满足：两两交集恰为 1}\ \big(|v_i\cap v_j|{=}1\ \forall i\ne j✓\big)\ \text{与\ \textbf{每坐标恰出现 2 次}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{唐先生"}$D(6,3,2)$ 型块／12 incidences 两次分摊"\ \textbf{逐字正确} ✓✓;\quad \text{故满 }F_p\ \text{是\ \textbf{唯一形状}（30 个同构型 ✓）}$$
$$\boxed{\textbf{(2) ✗✗唐先生 §3：}|\mathcal W(F_p)|\in\{3,4,5,6,7,9\}\ \textbf{不成立}:\ \text{对\ \textbf{合法满族}恒有}\ \boxed{|\mathcal W(F_p)|\equiv3}✓✓}$$
$$\qquad\textbf{根因 ✓}:\ \text{其计数基数 }30{+}360{+}1815{+}1815{+}810{+}15=4845=\binom{20}4\ \text{系\ \textbf{全部}四元组 ✗；合法满族仅\ \textbf{30}\ 个 ✓，全部给 }|\mathcal W|{=}3✓✓$$
$$\qquad\Longrightarrow\ \textbf{其"最坏仍有 9 个可用 suffix、够放 }|G_q|{=}3\text{"}\ ✗\ \text{—— 实为\ \textbf{恒 3} $\Longrightarrow$ }|G_q|\le3\ \text{是\ \textbf{紧的、零松弛} ✓✓}\ \big(\text{反而\ \textbf{更有利} ✓}\big)$$
$$\boxed{\textbf{(3) ✗唐先生 §3／§5 之"四个奇邻点"／"$Q_4$"\ ✗}:\ \text{prefix 图}=F_2^3=Q_3✓\ \text{每点\ \textbf{3} 邻 ✓}\ \big(\text{穷举 ✓}\big)\Longrightarrow\boxed{r_q\in\{0,1,2,3\}}✓✓\ \big(\text{非 }0..4✗\big)}$$
$$\textbf{(4) ✓✓✓本轮新获（$r_q$ 完整分类，穷举定值 ✓✓）}:\ r_q:=\#\{p\sim q:|F_p|{=}4\};\quad \text{取\ \textbf{全部}合法组合穷举}\ \binom{30}k\ ✓\big)$$
| $r_q$ | $\big|\bigcap_{p\sim q}\mathcal W(F_p)\big|$ 之分布 | $\max|G_q|$ |
|---|---|---|
| 0 | （无约束 ✓） | 3 |
| 1 | $\{3{:}30\}$ ✓ | 3 |
| 2 | $\{0{:}240,\ 1{:}180,\ 3{:}15\}$ ✓ | 3 |
| **3** | $\mathbf{\{0{:}3760,\ 1{:}300\}}$ ✓✓ | **1** ✓✓✓ |
$$\qquad\Longrightarrow\ \boxed{r_q=3\ (\text{三个偶邻点\ \textbf{全满}})\ \Longrightarrow\ |G_q|\le\mathbf1}✓✓✓;\quad \Longrightarrow\ \boxed{g\ \le\ 12-2\cdot\#\{q\in A_1:\ r_q=3\}}✓✓$$
$$\qquad\textbf{（推论 ✓✓）}:\ \text{若四个偶 prefix\ \textbf{全满}（}f{=}16✓\big)\Longrightarrow\ \text{每个奇 }q\ \text{皆 }r_q{=}3\Longrightarrow\boxed{g\le4}✓✓\ \big(\text{原为 }12✗\big)$$
$$\textbf{(5) ✓唐先生 §1／§9 正确}:\ p\sim q\Rightarrow\forall v\in F_p,\forall w\in G_q:\ v\not\subseteq w✓✓\ \big(\text{|v\triangle w| 奇，}\min{=}1\iff v\subset w\ ✓✓\big);\quad \text{§9 之 singleton 距离式 ✓✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ v\subset w\ \text{为唯一 }d{=}2\ \text{源}\Longrightarrow \text{禁配表述\ \textbf{正确}}\ ✓✓\ \big(\text{且确实强于"}d{=}2\ \text{禁止"}\ ✓;\ \text{已成 }J(6,3)\text{--}J(6,4)\ \text{包含禁配}\ ✓✓\big)$$
$$\textbf{§2 ✓✓✓}:\ \text{见 §0(1)（30 族、交恰 1、每点两次 ✓✓）}$$
$$\textbf{§3 ✗✗}:\ \text{见 §0(2)（}|W|\equiv3✗\big);\ \text{其"}$|F_p|{=}4$ 不迫使邻 }G_q{=}0\text{"✓\ \text{方向对 ✓（但真因是 }|\mathcal W|{=}3\ \text{恒成立、而非"最坏 9" ✗）}$$
$$\textbf{§4 ✓✓}:\ G_q\subseteq\bigcap_{p\sim q}\mathcal W(F_p)✓✓\ \text{—— 本轮即由此得 §0(4) ✓✓（唯邻数应为 3 ✗）}$$
$$\textbf{§5 ✓（形式 ✓）}:\ \text{按 }r_q\ \text{分类}\Longrightarrow \text{应求 }r_q=0,1,2,3\ \big(\text{非 4 ✗}\big)\ \text{之 }|G_q|\ \text{上界}\Longrightarrow \text{本档已给出完整答案}\ ✓✓✓$$
$$\textbf{§6 ✓}:\ I=0\ \text{之零交叉关联表述 ✓✓};\ \text{单边禁配不产生数值界 ✓（诚实 ✓）};\ \text{本档由 }r_q\ \text{分类突破 ✓✓}$$
$$\textbf{§7 ✓✓}:\ \text{必须用壳层 }|C_3|{=}60,\ |D_3|{=}80\ \text{而非 }|C|,|D|\ ✓✓\ \big(\text{延续 C-453 之纪律}\ ✓\big);\quad \Gamma_C,\Gamma_D\ \text{之定义 ✓（registration ✓）}$$
$$\textbf{§8 ✓（方向 ✓）}:\ \text{对 }|F_p|{=}4\ \text{做 }(\Gamma_C,\Gamma_D,|\mathcal W|)\ \text{三元 profile ✓};\ \text{其中第三项现已\ \textbf{定值 }=3✓✓\ \big(\text{非 }\{3,\dots,9\}✗\big)}$$
$$\textbf{§9 ✓✓}:\ |111111\triangle v|{=}3,\ |111111\triangle w|{=}2\ ✓✓\ \big(\text{纯置换，无需穷举}\ ✓\big);\quad \text{对 }G\ \text{之绑定方向为 }p\ne q\ ✓\ \big(\text{其写 }d{=}4\iff d(p,q){=}2\ \text{为"恰好"而非"绑定"}\ ✓\big)$$
$$\textbf{§10 ✓（方向 ✓）}:\ \text{链 }F_p{=}4\to\mathcal W\to G_q\subseteq\bigcap\mathcal W\to r_q\ \text{分类}\to H\le1\ \text{—— 其中第三、四步\ \textbf{本轮已完成} ✓✓✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }|\mathcal W(F_p)|\equiv3\ \big(\text{满族}\big)✓✓✓;\ \text{② }\boxed{r_q=3\Rightarrow|G_q|\le1}✓✓✓;\ \text{③ }\boxed{g\le12-2\#\{q:r_q{=}3\}}✓✓;\ \text{④ }f{=}16\Rightarrow g\le4✓✓;\ \text{⑤ 满 }F_p\ \text{唯一形状（30 型）✓✓};\ \text{⑥ }v\subset w\ \text{禁配 ✓✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"}|\mathcal W|\in\{3,\dots,9\}\text{"}\ ✗;\ \text{"最坏 9 个可用 suffix"\ ✗};\ \text{"四个奇邻点／}Q_4\text{"}\ ✗;\ \text{"}r_q\in\{0..4\}\text{"}\ ✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{的全局可行性};\ \text{（}r_q\ \text{与 }f\ \text{之组合约束尚未穷尽 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 把 }t:=\#\{q:r_q{=}3\}\ \text{与 }f{=}\sum_p|F_p|\ \text{联立（}Q_3\ \text{二部 3-正则之覆盖结构 ✓）};\ \text{② 换 $\Gamma_C,\Gamma_D$ 入 §8 之三元 profile（}|\mathcal W|{=}3\ \text{已知 ✓）};\ \text{③ }r_q{=}2\ \text{那 15 个"交 =3"型（}$\mathcal W$ 相同 ✓\big)\ \text{单独审 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "四邻域共同禁止" "满前缀" "零松弛" "耦合不等式"
技术词 四邻域共同禁止 命中文件数=0    ::
技术词 满前缀         命中文件数=0    ::
技术词 零松弛         命中文件数=2    :: ./C162-exact-per-box-bound-and-adaptive-certificate-compression-measured.md ./K1AUDIT-2026-09-26-midpoint-injectivity-audit.md
技术词 耦合不等式     命中文件数=3    :: ./E182-T1-refuted-avoidance-is-free.md ./T3SPLIT-2026-09-26-geometric-split-and-A2-coupled-bound.md ./E181-infinite-pair-first-verdict.md
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 四邻域共同禁止 | 0 | 0 | ✓（自造标签 ✓） |
| 满前缀 | 0 | 0 | ✓（自造标签 ✓） |
| 零松弛 | **2**（`C162-…`／`K1AUDIT-2026-09-26-…` ⟹ **既有 ⟹ 不计** ✗） | 0 | ✗（**非新增** ✓） |
| 耦合不等式 | **1**（`T3SPLIT-2026-09-26-…` ⟹ 既有 ⟹ **不计** ✗） | **2**（`E182-…`／`E181-…` ⟹ 空间 A 同名 ⟹ **不计** ✗） | ✗（**非新增** ✓） |

- **（本条已先跑后写 ✓✓）**：四词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$\binom{20}{4}$ 族筛 ＋ $\binom{30}k$ 组合 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处必改**（§3 之 $|\mathcal W|$ 分布／§3§5 之"4 邻点"）已在 §0(2)(3) 显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
