# WITW2C-2026-09-28 — **119 ⟹ 9 维双色加权 2-覆盖**：链条核对 ＋ 跨色收紧 ＋ $K(9,1)$ 咬点

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:29 令 ✓）**：核对 fiber splitting 链条 → 推到"119 能否降成两个 9 维 almost-cover"；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-435／C-431／C-427，非新案 ✓）**
`docs/WITFIB-2026-09-28-…`（**精确等价 $U_b\subseteq P_{1-b}$／$|P_0\cap P_1|\le57$／$a,b\ge44$ ✓✓**）｜`docs/SUBSPACELP-2026-09-28-…`（**计数层 ≡ 体积界（封顶 ✓✓）**）｜`docs/C-427`（**文献区间 $107\le K\le120$／$K(9,1)=62$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** fiber-splitting／双色加权对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出双色精确条件（非"两个 light 邻点"）＋ 跨色 $e_2^{AB}$ 收紧 ＋ "H 永不可能是 9-cover"自动结论 ＋ $s{=}62$ 条件性矛盾** ✓）
**[RESEARCH]**

---

## §0 结论（**链条成立 ✓｜一处收紧✓✓｜自动结论 ✓✓｜$K(9,1)$ 咬点 ✓✓｜计数不咬 ⚠️**）

$$\text{记号 ✓}:\ C\subseteq\mathbb F_2^{10}\ \text{半径-1 覆盖},\ |C|=119✓;\ C_0,C_1\subseteq Q_9\ (=\mathbb F_2^9)✓;\ c_0:=\mathbf 1_{C_0},\ c_1:=\mathbf 1_{C_1},\ g:=c_0+c_1\in\{0,1,2\}✓;\ \textstyle\sum_xg(x)=119✓$$
$$A:=\text{$Q_9$ 邻接矩阵}✓;\quad H:=\{g=2\}\ (\text{heavy}✓),\quad L:=\{g=1\}\ (\text{light}✓),\quad A_\ast:=C_0\setminus C_1,\ B_\ast:=C_1\setminus C_0\ (\text{两"色"}✓)$$
$$\boxed{\textbf{(1) ★★逐点精确条件（本档收紧 ✓✓）}:\ \forall x\in Q_9:\quad \underbrace{c_0(x)+g(x)+(Ac_0)(x)\ge1}_{(x,0)\ \text{被覆盖}} \ \wedge\ \underbrace{c_1(x)+g(x)+(Ac_1)(x)\ge1}_{(x,1)\ \text{被覆盖}}\ ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（收紧！）}\ x\notin U:\ N(x)\cap C_0\ne\varnothing\ \wedge\ N(x)\cap C_1\ne\varnothing\ ✓✓\ \big(\text{唐先生的"两个 light 邻点"是\ \textbf{必要}\ 但\ \textbf{不充分}\ ✗：须\textbf{一色一个}✓}\big)$$
$$\qquad\Longrightarrow\ \text{该距离-2 对必须}\ \textbf{跨色}\ (A_\ast\ \text{一侧},\ B_\ast\ \text{另一侧}✓) \Longrightarrow \text{正确的量是}\ \boxed{e_2^{A_\ast B_\ast}(L)}\ \text{而非}\ e_2(L)\ ✓✓$$
$$\boxed{\textbf{(2) ★精确等价（双向 ✓，fiber 化 ＝ 精确重述，非归约 ✓）}:\ \text{119-cover of }Q_{10}\ \iff\ \text{对 }(C_0,C_1)\subseteq Q_9\ \text{逐点满足 §0(1)}\ ✓✓}$$
$$\boxed{\textbf{(3) ✓计数链全部成立（唐先生 §1–§10 ✓）}:\ s:=|U|\ge62✓;\quad |H|=119-s,\ |L|=2s-119✓;\quad s\le69\iff 9|H|\ge|U^c|✓}$$
$$\qquad s\ge70\Longrightarrow|X_L|\ \ge\ (512-s)-9(119-s)=\boxed{8s-559}\ ✓;\qquad |X_L|\le2e_2^{A_\ast B_\ast}\Longrightarrow \boxed{e_2^{A_\ast B_\ast}\ge\big\lceil(8s-559)/2\big\rceil}\ ✓$$
$$\boxed{\textbf{(4) ⚠️ 但这些界\ \textbf{全不咬}（本档核实 ✓）}:\ e_2^{A_\ast B_\ast}\le36\min(|A_\ast|,|B_\ast|)\le36\cdot59=2124\ ✗\ \text{vs 需求}\le197✓ \Longrightarrow \textbf{一阶/二阶计数全部耗尽}✗✓}$$
$$\boxed{\textbf{(5) ★★自动结论（新 ✓✓，只用 }K(9,1)\ge62\text{）}:\ |H|=119-s\le57<\mathbf{62}\ \Longrightarrow\ H\ \textbf{永不可能是 }9\text{-cover}\ ✓✓\ \Longrightarrow\ \exists y\notin N[H]✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{必有其一}:\ \textbf{(α)}\ \exists\ light\ \text{点与 }H\ \text{完全不相邻};\qquad \textbf{(β)}\ \exists\ \text{外部点 }y\notin U\ \text{无 heavy 邻点 (⟹ 需一 }A_\ast\text{-邻点}＋\text{一 }B_\ast\text{-邻点}✓)}✓✓$$
$$\boxed{\textbf{(6) ★★} s=62\ \text{端的\ \textbf{条件性矛盾}（新 ✓✓，$K(9,1)$ 唯一已知咬点）}:\ s=62\Rightarrow|H|=57,\ |L|=5,\ U\ \text{＝最优 62-cover}✓}$$
$$\qquad\textbf{若}\ \text{(i) 5 个 light 点皆有 }H\text{-邻点}\ \textbf{且}\ \text{(ii) }N(H)\supseteq U^c \Longrightarrow N[H]=\mathbb F_2^9 \Longrightarrow H\ \text{是 \textbf{57-词 9-cover}} \Longrightarrow \textbf{与 }K(9,1)=62\ \textbf{矛盾}✗✗$$
$$\qquad\Longrightarrow\ \boxed{s=62\ \text{时必有}\ \neg(i)\ \text{或}\ \neg(ii)}✓✓\ \textbf{缺件}:\ 62\text{-最优码的分类（switching class ✓）ⓘ 需文献/计算（登记未做 ✓）}$$

---

## §1 核对与收紧（**逐条 ✓**）

$$\textbf{(§1-2) ✓}:\ C_1^c\subseteq N[C_0]\ \wedge\ C_0^c\subseteq N[C_1]\ ✓\ \big(\text{＝C-435 §0(1) ✓}\big);\quad |N[C_0]|\le10a✓\Longrightarrow 10a\ge393+a\Longrightarrow \boxed{a,b\ge44}✓✓$$
$$\qquad\text{（唐先生本轮写 }a\ge44✓；\text{前一轮所写 40\ 系误 ✓ 此处已校正 ✓）}$$
$$\textbf{(§3-§5) ✓}:\ H_0=C_1\setminus N[C_0]✓,\ H_1=C_0\setminus N[C_1]✓;\ I=C_0\cap C_1=H✓,\ A_\ast,B_\ast\ \text{如上}✓;\ 119=|I|+|A_\ast|+|B_\ast|✓$$
$$\textbf{(§6-§8) ✓}:\ U\ \text{是 9-cover}\Longrightarrow s\ge62✓;\ |U|=119-t\Longrightarrow \boxed{t=|C_0\cap C_1|=|H|=119-s\le57}✓✓\ \big(\text{＝C-435 ✓}\big)$$
$$\textbf{(§10 的收紧 ✓✓)}:\ \text{唐先生写"至少两个 light 邻点"}\ ✗\ \text{应为"一 }A_\ast\text{-邻点 ＋ 一 }B_\ast\text{-邻点"}\ ✓\ \text{（否则 }(x,0),(x,1)\ \text{只有一侧被覆盖 ✗）}$$
$$\qquad\Longrightarrow\ \text{每个 }x\in X_L\ \text{产生一个\ \textbf{跨色距离-2 对}（}A_\ast\ni a\sim x\sim b\in B_\ast✓,\ d(a,b)=2✓\big)✓\ \Longrightarrow\ |X_L|\le2e_2^{A_\ast B_\ast}✓✓$$

## §2 为何计数不咬（**⚠️ 核实 ＋ 与 C-431 一致 ✓**）

$$e_2^{A_\ast B_\ast}\le36\min(|A_\ast|,|B_\ast|)✓\ \big(\text{每点 36 个距离-2 邻点}\ ✓\big);\quad |A_\ast|+|B_\ast|=2s-119\Longrightarrow\min\le s-60\le59✓$$
$$\qquad\Longrightarrow\ \text{容量}\le2124\ \text{vs 需求}\ \le197\ (s=119)\ ✗ \Longrightarrow \textbf{不咬}✓;\quad \text{且 }\sum_x\big[2g+Ag\big]=2\cdot119+9\cdot119=1309\ge2\cdot512✓\ \big(\text{＝体积界 }\tfrac{1024}{11}=93.09✓\big)$$
$$\Longrightarrow\ \textbf{与 C-431 同一现象 ✓}:\ \text{一切\ \textbf{聚合型} 推论都落回体积界}✗✓;\ \text{本轮的一阶/二阶 item 亦不例外}✓$$

## §3 $s=62$ 端：$K(9,1)$ 的咬点（**✓✓ 登记**）

$$s=62\Longrightarrow |H|=57✓,\ |L|=5✓,\ U\ \text{是 62-词最优 9-cover}✓;\quad |C_0|+|C_1|=119=2|H|+|L|✓$$
$$\textbf{条件性矛盾 ✓✓}:\ \text{(i) }L\subseteq N(H)\ \wedge\ \text{(ii) }U^c\subseteq N(H) \Longrightarrow N[H]=H\cup L\cup U^c=\mathbb F_2^9 \Longrightarrow |H|=57\ \text{是 9-cover}\ ✗\ \text{vs }K(9,1)=62✓✓$$
$$\Longrightarrow\ \boxed{\neg(i)\vee\neg(ii)}\ ✓;\quad \textbf{两条出路 ✓}:\ \neg(i)\ \text{＝某 light 点与 57 个 heavy 全不相邻}✓;\ \neg(ii)\ \text{＝某外部点无 heavy 邻点（⟹ 需跨色双邻 ✓）}✓$$
$$\textbf{（为何这是唯一咬点 ✓）}:\ \text{一般 }s\ \text{时 }|H|=119-s\ \text{更小} \Longrightarrow\ \text{H 更不可能覆盖} \Longrightarrow\ \text{自动结论 §0(5) 更强}\ ✓;\ \text{但 §0(5) 只给"存在性"，不给\textbf{数量}✓}$$
$$\qquad\Longrightarrow\ \text{要形成矛盾，须把 §0(5) 的"存在"升级为\textbf{计数}（如 }\neg(ii)\ \text{的点的最少个数}\ ✓\big):\ \text{一般下界 }|X_L|\ge\max(0,8s-559)✓\ \text{在 }s\le69\ \text{时为零}✗$$
$$\qquad\Longrightarrow\ \textbf{真正缺件 ✓}:\ 62\text{-最优码的结构/分类（含其 switching class ✓）} \Longrightarrow\ \text{判定 }\neg(i)/\neg(ii)\ \text{是否真的可能}\ ✓\ \big(\text{登记未做 ⚠️}\big)$$

## §3bis ★ 唐先生 §12 的目标形式（**$\mathcal L_9(U)$ 的确切地位 ✓**）

$$\textbf{定义 ✓}:\ \mathcal L_9(U):=\min_{\chi}\Big\{|C_0|+|C_1|:\ C_0\cup C_1\supseteq U,\ C_0^c\subseteq N[C_1],\ C_1^c\subseteq N[C_0]\Big\}\ ✓\ \big(\text{＝9 维\ \textbf{双色加权 2-覆盖} 的最轻配置 ✓}\big)$$
$$\textbf{119 问题 ⟺ ✓}:\ \exists\,9\text{-cover }U:\ \mathcal L_9(U)\ \le\ 119✓;\qquad \textbf{故等价目标}:\ \boxed{\forall\,9\text{-cover }U:\ \mathcal L_9(U)\ \ge\ 120}\ ✓✓$$
$$\textbf{（与 }K(9,1)=62\ \text{的关系 ✓）}:\ \mathcal L_9(U)\ge|U|\ge K(9,1)=62✓\ \text{仅是\ \textbf{第一层}；}\ \mathcal L_9\ \text{比 }K\ \text{多出的是"双色条件"的代价 ✓}$$
$$\textbf{（本档新增的一层 ✓）}:\ \mathcal L_9(U)\ \ge\ |U|+\big(\text{色分离代价}\big)✓\ \text{—— 由 §0(1) 的逐色条件，}\ C_0\setminus C_1\ \text{与}\ C_1\setminus C_0\ \text{不能同时为空 ✓}$$
$$\qquad\Longrightarrow\ \text{若 }|U|=62\ \text{且 §0(6) 的 (i)(ii) 皆真} \Longrightarrow U\ \text{本身\ 已\ 迫使矛盾}✗\ \big(\text{＝§0(6) ✓}\big);\quad \text{否则须逐 }s\ \text{做}=63,64,\dots\ ✓\ \big(\text{登记未做 ✗}\big)$$
## §4 状态（**不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 双色精确条件（§0(1)）};\ \text{② 精确等价（§0(2)）};\ \text{③ 计数链六条（§0(3)）};\ \text{④ 计数不咬的核实（§3）};\ \text{⑤ 自动二择（§0(5)）};\ \text{⑥ }s{=}62\ \text{条件性矛盾（§0(6)）}✓$$
$$\textbf{未确立 ✗}:\ 62\text{-最优码分类；}\neg(i)/\neg(ii)\ \text{的可实现性；矛盾本身}✗;\ \text{一般 }s\ \text{的"存在}\to\text{计数"升级}✗$$
$$\textbf{（与 cascade 路线的关系 ✓）}:\ \text{本路线\textbf{替代} cascade}✓\ \text{（唐先生 10:29 判 cascade 不值得继续 ✓）};\ \text{共同点：都停在"计数耗尽、需结构输入"}✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "双色加权" "跨色对" "e_2^{AB}" "条件性矛盾"
技术词 双色加权   命中文件数=0    ::
技术词 跨色对     命中文件数=0    ::
技术词 e_2^{AB}   命中文件数=0    ::
技术词 条件性矛盾 命中文件数=2    :: ./E168-PSF-density-vs-local-obstruction.md ./MASTER-STATUS-AND-CLOSURES.md
```
| 词 | 本线命中（空间 B） | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 双色加权 | 0 | 0 | 0（本档自造标签 ✓） |
| 跨色对 | 0 | 0 | 0（本档自造标签 ✓） |
| e_2^{AB} | 0 | 0 | 0（本档自造标签 ✓） |
| 条件性矛盾 | 0（2 命中属 `E168-*`／`MASTER-STATUS-*` ⟹ **属线未定 ⟹ 不计** ✗） | 2 | 0（既有词 ✓） |

- **本档新增**：**0** 个术语 ✓（`双色加权`／`跨色对`／`e_2^{AB}` 两空间皆 0 ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 核对与收紧 ＋ §2 不咬核实 ＋ §0(5)(6) 两定理 ＋ §3 缺件定位**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **$K(9,1)=62$ 为文献值** ✓（档级 ✓）；本档只用其**下界方向**（$|H|<62\Rightarrow$ 非 cover ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给核对、收紧、两定理与缺件；是否以 62-码分类为主攻由唐先生定 ✓
- **不声称** 119 已排除 ✗；**不声称** $s{=}62$ 必矛盾 ✗（已明示为**条件性** ✓）；不声称 P1 成立 ✗（V290）
