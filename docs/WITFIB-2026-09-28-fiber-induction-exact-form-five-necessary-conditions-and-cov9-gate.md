# WITFIB-2026-09-28 — **FIBER-INDUCTION：坐标分裂的精确形式 ＋ 五条必要条件 ＋ $\mathrm{cov}_9$ 活口**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:22 令 ✓）**：换范式 —— 攻击 **FIBER-INDUCTION**（坐标分裂 → 两个 9 维对象 → 用 $K(9,1)=62$）；**零程序计算** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-427／C-431／C-435 前身，非新案 ✓）**
`docs/C-427 registry`（**文献区间 $107\le K\le120$／$K(9,1)=62$ ✓✓）｜`docs/SUBSPACELP-2026-09-28-…`（**cell-LP ≡ 体积界（计数层封顶 ✓✓）**）｜`docs/HANDOFF-2026-09-27-119-…`（**$K(9,1)=62$ 基准码** ✓✓）｜`docs/ALIGN-2026-09-25-…`（**$\delta$／excess 对齐** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词**两空间皆 0**，见 §6）
D0: 本档对象 ＝ **档案已有** 坐标分裂／投影对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出坐标分裂覆盖条件的\*\*精确等价式\*\* ＋ 「$P_0\cup P_1$ 是 9-cover」＋ 分裂平衡下界 44 ＋ $905$ 负载式 ＋ $\mathrm{cov}_9$ 精确必要条件 ＋ 递归形式** ✓）
**[RESEARCH]**

---

## §0 结论（**精确等价 ✓✓｜$P_0\cup P_1$ 是 cover ✓✓｜平衡 ✓✓｜$\mathrm{cov}_9$ 活口 ✓✓｜无矛盾 ⚠️**）

$$\text{设 }C\subseteq\mathbb F_2^{10},\ |C|=119\ \text{是半径-1覆盖 ✓；取定末坐标，写 }(x,b)\ (x\in\mathbb F_2^9,\ b\in\{0,1\})✓$$
$$P_b:=\{x\in\mathbb F_2^9:(x,b)\in C\}✓;\quad a:=|P_0|,\ b:=|P_1|,\ a+b=119✓;\quad N_9[S]:=\text{闭半径-1邻域}✓$$
$$\boxed{\textbf{(1) ★★覆盖条件的精确等价（本档核心 ✓✓）}:\ \text{整码覆盖 } \iff \mathbb F_2^9=P_1\cup N_9[P_0]\ \wedge\ \mathbb F_2^9=P_0\cup N_9[P_1]}$$
$$\qquad\iff\ \boxed{U_0\subseteq P_1\ \wedge\ U_1\subseteq P_0}\ \big(\text{其中 }U_b:=\mathbb F_2^9\setminus N_9[P_b]=\text{"层 }b\ \text{的洞"}✓\big)\ ✓✓$$
$$\boxed{\textbf{(2) ★★} P_0\cup P_1\ \text{必是 }9\text{-cover（新 ✓✓）}:\ \mathbb F_2^9\subseteq N_9[P_0]\cup N_9[P_1]=N_9[P_0\cup P_1]✓ \Longrightarrow \boxed{|P_0\cup P_1|\ \ge\ K(9,1)=\mathbf{62}}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{|P_0\cap P_1|\ \le\ 119-62=\mathbf{57}}\ ✓✓\ \big(\textbf{＝唐先生所期望的 P1 ✓✓}\big)$$
$$\boxed{\textbf{(3) ★★分裂必须平衡（新 ✓✓）}:\ |U_0|=\mathbf{512}-|N_9[P_0]|\ \ge\ 512-10a\ \ \text{且}\ \ U_0\subseteq P_1 \Longrightarrow 512-10a\le b\ \Longrightarrow\ \boxed{a\ \ge\ 44}\ ✓✓\ \text{（对称得 }b\ge44✓\big)}$$
$$\boxed{\textbf{(4) ★负载式（新 ✓）}:\ |U_0|+|U_1|\le|P_1|+|P_0|=119 \Longrightarrow \boxed{\big|N_9[P_0]\big|+\big|N_9[P_1]\big|\ \ge\ 1024-119=\mathbf{905}}\ ✓✓\ \big(\text{＝唐先生的 }905✓\big)}$$
$$\boxed{\textbf{(5) ★★精确必要条件（新 ✓✓ ＝ P3 的正确形式）}:\ \text{设 }\mathrm{cov}_9(s):=\max_{|S|=s}\big|N_9[S]\big|\ ✓ \big(\text{"$K(9,1)=62$ 的\textbf{带 holes} 版本"}✓\big) \Longrightarrow}$$
$$\qquad\boxed{512-\mathrm{cov}_9(a)\ \le\ b\quad\wedge\quad 512-\mathrm{cov}_9(b)\ \le\ a}\ ✓✓\ \big(\text{用 }\mathrm{cov}_9(62)=512\ \text{即 }\mathrm{cov}_9\ \text{在 }62\ \text{处饱和 ✓}\big)$$
$$\boxed{\textbf{(6) ★递归形式（新 ✓）}:\ m\ \text{维分裂（左右两层大小 }s_1,s_2\text{）：} 2^m-(m+1)s_1\le s_2\ \text{且对偶成立};\ \text{逐层下降至 }m=1}$$
$$\boxed{\textbf{(7) ⚠️ 但计数层被封顶（诚实 ✓✓）}:\ \text{把 (3)(4)(5) 相加} \Longrightarrow (n+1)\cdot|C|\ge2^n\ \text{（＝体积界 }93.09\text{）}\ \text{—— 与 C-431 同一层} \Longrightarrow \textbf{计数路线到不了 }119\ ✗✓}$$

---

## §1 精确等价（**逐项 ✓✓**）

$$\text{点 }(x,0)\ \text{的覆盖者三类 ✓}:\ \text{① }(x,0)\in C\iff x\in P_0✓;\quad \text{② }(x{\oplus}e_j,0)\in C\ (1\le j\le9)\iff x\in P_0\oplus\{e_j\}✓;\quad \text{③ }(x,1)\in C\iff x\in P_1✓$$
$$\Longrightarrow\ (x,0)\ \text{被覆盖}\iff x\in P_0\cup\big(P_0\oplus\{e_j\}\big)\cup P_1=N_9[P_0]\cup P_1✓ \Longrightarrow \mathbb F_2^9=N_9[P_0]\cup P_1✓$$
$$\qquad\text{对称（对 }(x,1)\ \text{同法）}:\ \mathbb F_2^9=N_9[P_1]\cup P_0✓ \Longrightarrow \boxed{\text{§0(1)}✓✓\ \big(\text{即 }U_b\subseteq P_{1-b}✓\big)}$$
$$\textbf{读法 ✓}:\ \text{分层后"洞"（}U_0,U_1\big)\ \text{是唯一的缺陷量 ✓；}m(x)=0\ \text{的 fiber 中两点\textbf{各需邻层承担}✓（＝唐先生的}\;L(x)=2-m(x)\;\text{读法 ✓）}$$

## §2 两条强必要条件的证明（**✓✓**）

$$\textbf{(2) 的证明 ✓}:\ P_1\subseteq N_9[P_1]\ \wedge\ \mathbb F_2^9=N_9[P_0]\cup P_1 \Longrightarrow \mathbb F_2^9\subseteq N_9[P_0]\cup N_9[P_1]=N_9[P_0\cup P_1]✓ \Longrightarrow P_0\cup P_1\ \text{是 }9\text{-cover}✓$$
$$\qquad\Longrightarrow\ |P_0\cup P_1|\ge K(9,1)=62✓ \Longrightarrow |P_0\cap P_1|=a+b-|P_0\cup P_1|\le119-62=57✓✓$$
$$\textbf{(3) 的证明 ✓}:\ |N_9[S]|\le 10|S|✓\ \big(\text{每词覆盖自身＋至多 9 邻点}\ ✓\big) \Longrightarrow |U_0|=512-|N_9[P_0]|\ge512-10a✓;\ \text{又 }U_0\subseteq P_1\Longrightarrow|U_0|\le b✓$$
$$\qquad\Longrightarrow 512-10a\le119-a\Longrightarrow 9a\ge393\Longrightarrow a\ge\big\lceil\tfrac{393}9\big\rceil=\mathbf{44}✓✓\ \big(\text{故 }a\in[44,75]✓\big)$$
$$\textbf{(4) 的证明 ✓}:\ U_0\cap U_1\ \text{逐项相加}:\ |U_0|+|U_1|\le|P_1|+|P_0|✓ \Longrightarrow 1024-\big(|N_9[P_0]|+|N_9[P_1]|\big)\le119✓$$

## §3 $\mathrm{cov}_9$ 与递归（**✓✓ 活口**）

$$\mathrm{cov}_9(s):=\max\big\{|N_9[S]|:|S|=s\big\}✓;\qquad \mathrm{cov}_9(62)=512✓\ \big(K(9,1)=62✓\ \text{饱和}\ ✓\big);\quad \mathrm{cov}_9(s)\le10s✓$$
$$\text{由 }U_0\subseteq P_1\ \text{且 }U_1\subseteq P_0:\quad \boxed{\ 512-\mathrm{cov}_9(a)\le|U_0|\le b\ \wedge\ 512-\mathrm{cov}_9(b)\le a\ }✓✓$$
$$\textbf{读法 ✓✓}:\ \text{这是 }(a,b)\ \text{的\textbf{充要型必要条件}（用 }K(9,1)=62\ \text{的\ \textbf{holes 结构}而非仅计数 ✓）};\ \text{若 }\mathrm{cov}_9\ \text{在 }>57\ \text{处仍远离 }512\ \text{则 }a+b=119\ \text{被逼出矛盾 ⚠️}$$
$$\textbf{递归 ✓}:\ \text{对 }m\ \text{维、两层 }s_1,s_2\ (s_1+s_2=c✓\big):\ 2^m-(m+1)s_1\le s_2\ \wedge\ 2^m-(m+1)s_2\le s_1✓\ \big(\text{同法，每词覆盖 }1+m\ \text{点}\ ✓\big)$$
$$\qquad\Longrightarrow\ \text{逐层下降（}m=9\to8\to\cdots\to1✓\big)，\ \text{每层给一对不等式 ✓ ⟹ \textbf{分裂树}✓✓\ \big(\text{与 Östergård–Blass 的 subspace 递归同族 ✓，但用的是 }K\ \text{的 holes 而非 LP ✓}\big)}$$

## §4 为何仍无矛盾（**⚠️ 诚实 ＋ 与 C-431 的连接 ✓**）

$$\textbf{计数层封顶 ✓}:\ \text{把 (3) 的两式与 (4) 相加，即得 }(n+1)|C|\ge 2^{n}✓\ \big(n=10:|C|\ge93.09✓\big) \Longrightarrow \textbf{与 C-431 的"cell-LP ≡ 体积界"同层 ✗✓}$$
$$\qquad\Longrightarrow\ \textbf{任何只用 }|S|,|N[S]|\ \text{的计数式，都不可能超过 }93.09\ ✗\ \big(\text{不可能触及 }119✓\big)$$
$$\textbf{故唯一活口 ✓✓}:\ \mathrm{cov}_9(s)\ \text{的精确形状（}s\le61\ \text{时洞的结构），而非其计数上界} \Longrightarrow \textbf{＝唐先生的 P3"带 holes 的 }K(9,1)=62\text{"} ✓✓$$
$$\textbf{（诚实标注 ⚠️）}:\ \text{本档未证明 }\mathrm{cov}_9(s)\ \text{在 }s\le61\ \text{处足以产生矛盾 ✗；仅证明：若它足够强，则 }a+b=119\ \text{与之冲突 ✓（登记未做 ✓）}$$

## §5 状态（**不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 精确等价式（§1）};\ \text{② }P_0\cup P_1\ \text{是 }9\text{-cover}\Rightarrow|P_0\cap P_1|\le57✓;\ \text{③ }a,b\ge44✓;\ \text{④ }905\ \text{负载式}✓;\ \text{⑤ }\mathrm{cov}_9\ \text{必要条件}✓;\ \text{⑥ 递归形式}✓$$
$$\textbf{未确立 ✗}:\ \text{第二个"被迫 9-cover"对象（P2 —— \textbf{未找到}✗）；}\mathrm{cov}_9\ \text{的精确形状；矛盾 ✗}$$
$$\textbf{（P2 的诚实答复 ⚠️）}:\ \text{自然候选 }P_0\cap P_1,\ P_0\triangle P_1,\ P_0,\ P_1\ \text{皆\textbf{不}被迫覆盖}✗;\ N_9[P_0]\cup N_9[P_1]=\mathbb F_2^9\ \text{是覆盖条件本身（无新信息 ✓）} \Longrightarrow \text{尚无 }|P_0|+|P_1|\ge124\ \text{型冲突 ✗}$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "fiber-induction" "投影缺陷" "分裂平衡" "cov_9"
技术词 fiber-induction  命中文件数=0    ::
技术词 投影缺陷        命中文件数=0    ::
技术词 分裂平衡        命中文件数=0    ::
技术词 cov_9           命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| fiber-induction | 0 | 0 | 0（本档自造标签 ✓） |
| 投影缺陷 | 0 | 0 | 0（本档自造标签 ✓） |
| 分裂平衡 | 0 | 0 | 0（本档自造标签 ✓） |
| cov_9 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（四词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 精确等价 ＋ §2 两条强必要条件 ＋ §3 $\mathrm{cov}_9$／递归 ＋ §4 封顶诊断**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓（仅三处整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **$K(9,1)=62$ 为文献值** ✓（档级 ✓，非本档所证 ✓）；本档只用其**数值**（§2）与**holes 假设**（§3-活口 ⚠️）
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给框架与必要条件；是否以 $\mathrm{cov}_9$ 为主攻由唐先生定 ✓
- **不声称** 119 已被排除 ✗；**不声称** $\mathrm{cov}_9$ 路线必成 ✗；不声称 P1／P2 成立 ✗（V290）
