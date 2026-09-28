# WITPARITY-2026-09-28 — **extremal 恰 3 类（✓✓✓ 确认）｜但跨层 $d{=}2$ 机制\ \textbf{空}（奇偶性 ✗✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:42 令 ✓）**：extremal 分类与跨层接口；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-457／C-456／C-453，非新案 ✓）**
`docs/WITCEIL-2026-09-28-…`（**$|A_0|\le40$ 支配层和 ✓✓✓**）｜`docs/WITCAPP-2026-09-28-…`（**$\max|F|{+}|G|\le22$ ✓✓✓**）｜`docs/WITDEC-2026-09-28-…`（**$c+d\le20$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** extremal profile／跨层距离对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次确认 extremal 恰 3 轨道（$4,4,6$）＋ 首次证明跨层 $d{=}2$ 机制为空（奇偶性）：$C_3\!\leftrightarrow\! G$ 最小距离 $=3$、$d{=}1$ 亦 0 对** ✓）
**[RESEARCH]**

---

## §0 结论（**3 类 extremal ✓✓✓｜跨层 $d{=}2$ 空 ✗✗｜真接口是 $d{=}1$ ✓**）

$$\textbf{设定 ✓}:\ A_0\subseteq R\ \big(396✓\big),\ d(A_0)\ge3✓;\ C_3{=}(3,3,3,5)\ (60✓),\ D_3{=}(3,5,5,5)\ (80✓),\ F{=}(4,4,4,6)\ (80✓),\ G{=}(4,6,6,6)\ (60✓)✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §2 之 extremal 三型\ \textbf{完全正确}（本档穷举 ＋ 自同构合并确认 ✓✓✓）}}$$
$$\qquad\text{穷举全 }5^4{=}625\ \text{个 profile：}\max(|F|{+}|G|)=22✓,\ \text{达标 profile }\mathbf{14}\ \text{个}✓\ \Longrightarrow\ \text{按 }Q_3\ \text{自同构}\ \big(S_3\times V_4,\ \text{阶 }24✓\big)\ \text{合并}\Longrightarrow\boxed{\text{恰 3 类}}✓✓✓$$
| 型 | $f$ | $\|F\|$ | $s$-profile | $k$ | $\|G\|_{\max}$ | 总量 | 轨道大小 |
|---|---|---|---|---|---|---|---|
| I | $(0,4,4,4)$ | 12 | $(12,8,8,8)$ | 1 | 10 | 22 | 4 |
| II | $(2,2,2,4)$ | 10 | $(8,8,8,6)$ | 0 | 12 | 22 | 4 |
| III | $\mathbf{(2,2,3,3)}$ | 10 | $(8,8,7,7)$ | 0 | 12 | 22 | 6 |
$$\qquad\textbf{（推理 ✓✓）}:\ |G|\le(12-2k)✓\ \big(k{=}\#\{q:s_q\ge9\}✓\big);\quad s_q=|F|-f_{p(q)}\ ✓\ \big(\text{每奇 }q\ \text{恰缺一个偶 prefix}\ ✓\big)$$
$$\qquad\textbf{active bucket}✓:\ \text{Type I}: |A|{=}3\ (s{=}8);\quad \text{Type II}: |A|{=}3;\quad \text{Type III}: |A|{=}2\ ✓✓$$
$$\textbf{(2) ✗✗但跨层 }d{=}2\ \textbf{机制为空（本档推翻；奇偶性证明）}:\ \text{唐先生 §5／§8／§13 之"}$C_3\cup D_3$ 对 $F\cup G$ 的 $d{=}2$ 禁配"$\ \textbf{不存在}\ ✗✗$$
$$\qquad\textbf{证明 ✓✓}:\ C_3,D_3\ \text{为偶 prefix}\oplus|\cdot|{=}2\ \text{或奇 prefix}\oplus|\cdot|{=}3;\ F,G\ \text{为偶 prefix}\oplus|\cdot|{=}3\ \text{或奇 prefix}\oplus|\cdot|{=}4$$
$$\qquad\qquad\text{跨层（}d{=}3\ \text{层与 }d{=}4\ \text{层）之 prefix 奇偶必\ \textbf{相反} ⟹ }d_{\text{pref}}\ \text{奇};\ \text{又 }|\triangle|\ \text{偶（}2{\leftrightarrow}4\big)\ \text{或偶（}3{\leftrightarrow}3\big)\Longrightarrow\boxed{d\ \text{恒为\ \textbf{奇}}}\Longrightarrow d{=}2\ \text{不可能}✗✗$$
$$\qquad\textbf{穷举印证 ✓✓（逐对全算 ✓）}:$$
| 层对 | 距离分布 | 最小 | $d{=}2$ 对 | $d{=}1$ 对 |
|---|---|---|---|---|
| $C_3$–$F$ | $1{:}240,\ 3{:}1440,\ 5{:}2400,\ 7{:}720$ | 1 | **0** ✗ | 240 ✓ |
| $\mathbf{C_3}$–$\mathbf{G}$ | $\mathbf{3{:}1080,\ 5{:}1800,\ 7{:}660,\ 9{:}60}$ | **3** | **0** ✗ | **0** ✓✓ |
| $D_3$–$F$ | $1{:}240,\ 3{:}2240,\ 5{:}2880,\ 7{:}960,\ 9{:}80$ | 1 | **0** ✗ | 240 ✓ |
| $D_3$–$G$ | $1{:}240,\ 3{:}1440,\ 5{:}2400,\ 7{:}720$ | 1 | **0** ✗ | 240 ✓ |
| $F$–$G$（层内 ✓） | $2{:}720,\ 4{:}2400,\ 6{:}1440,\ 8{:}240$ | 2 | **720** ✓ | 0 |
| $C_3$–$C_3$（层内 ✓） | $0{:}60,\ 2{:}660,\ 4{:}1800,\ 6{:}1080$ | 0 | **660** ✓ | 0 |
$$\qquad\Longrightarrow\ \boxed{C_3\ \text{禁掉\ \textbf{0 个} }G\text{-点}}\ ✓✓\ \big(\text{唐先生之 }|\partial^-G_q\setminus N_2(w)|\ \text{提法在 }C_3\ \text{侧\ \textbf{无对象} ✗}\big)$$
$$\qquad\textbf{（真接口 ✓✓）}:\ \text{跨层唯一约束为 }d{=}1\ \big(\text{各 240 对 ✓}\big):\ C_3\text{--}F\ \text{与 }D_3\text{--}G\ \text{与 }D_3\text{--}F\ \text{皆"同/邻 prefix ＋ 子集(等式)"型 ✓✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ |G|\le12-2k✓✓;\quad k=\#\{q:s_q\ge9\}✓;\ \text{本地界 }h(s)✓\ (\text{C-456 ✓})$$
$$\textbf{§2 ✓✓✓}:\ \text{三型全对 ✓✓✓}\ \big(\text{含 Type III }(2,2,3,3)✓\big);\quad \text{本档穷举确认轨道数}=3✓,\ \text{轨道大小 }4/4/6✓✓$$
$$\textbf{§3 ✓✓}:\ \text{Type II／III 皆 }G{=}12\Rightarrow g_q{\equiv}3✓✓;\ \text{且 }s_q\le8\ \forall q✓✓;\ |\partial^-G_q|{=}12✓✓\ \text{（对的三重交 ✓）}$$
$$\textbf{§4 ✓✓}:\ \text{Type II 之 }s{=}(8,8,8,6)✓✓\ \big(s_q{=}10-f_{p(q)}✓\big);\quad \text{"}2\text{-for-}1"\ \big(s_q:8\to9\Rightarrow g_q:3\to1✓\big)\ ✓✓$$
$$\textbf{§5 ✓（结构 ✓）}:\ \text{Type III 之 }s{=}(8,8,7,7)✓✓;\ \text{两个临界桶 ✓（}s{=}8\ \text{共 2 个 ✓）}$$
$$\textbf{§6 ✓✓}:\ \text{Type I 之 }g{=}(3,3,3,1)✓✓;\ \text{"跨层落点不同 ⟹ 损失不同"\ ✓✓（且其对"计数对象混淆"之自警 ✓✓）}$$
$$\textbf{§7 ✓（形式 ✓）}:\ \text{active bucket 定义 ✓;\ }|A|{=}3/3/2✓✓\ \text{（穷举确认 ✓）}$$
$$\textbf{§8 ✗✗}:\ \text{其 }N_2(w)\ \text{禁 }\partial^-G_q\ \text{之提法}\ ✗\ \text{—— 跨层无 }d{=}2\ ✗✓;\ \text{唯"禁配位置数}\ne\text{最大可选 }g_q\text{"之警告 ✓✓\ \textbf{完全正确}（本档认同 ✓）}$$
$$\textbf{§9–§11 ✗✗}:\ \text{三元 }\mathcal W\ \text{之 }Q_3\ \text{命中矩阵提法形式 ✓，但\ \textbf{其输入（跨层 }d{=}2\big)\ }\textbf{为空}\ ✗✗\Longrightarrow\ \text{§13 之 P1 目标须\ \textbf{重构} ✗✓}$$
$$\textbf{§10 ✓（纯计数 ✓）}:\ \sum_qm_q=\sum_w|\Gamma(w)|✓;\ 9/4>1\Rightarrow\exists m_q\ge3✓✓\ \text{（鸽笼 ✓，但前提 }\Gamma\ \text{存在 ✗）}$$
$$\textbf{§13–§14 ✗}:\ \text{其 P1}\ \big(\text{三元 profile 击穿 }g_q{=}3\big)\ \text{之机制为空}\ ✗;\quad \textbf{另}:\ \text{总量侧已被 }|A_0|\le40\ \text{支配（C-457 ✓）}\Longrightarrow\ \text{该路线上限即 }40\ ✓$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① extremal 恰 3 类（}4/4/6\big)✓✓✓;\ \text{② }s\text{-profiles }(12,8,8,8),(8,8,8,6),(8,8,7,7)✓✓;\ \text{③ }|G|\le12-2k✓✓;\ \text{④ active bucket }3/3/2✓✓;\ \text{⑤ }\boxed{\text{跨层 }d{=}2\ \text{不存在}}\ ✓✓✓;\ \text{⑥ 跨层唯一约束＝}d{=}1\ \text{（子集／等式型 ✓）}$$
$$\textbf{已否证 ✗✓}:\ \text{跨层 }d{=}2\ \text{禁配机制}\ ✗;\ C_3\ \text{禁 }G\text{-点}\ ✗;\ \text{§13 之 P1 机制}\ ✗;\ \text{"}42/41\ \text{可达"}\ ✗\ \big(\text{C-457 ✓}\big)$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{全局可行性};\ \text{（}d{=}1\ \text{型跨层约束尚未用于压低 }22✓\big)$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① }d{=}1\ \text{型跨层约束（}C_3\text{--}F,\ D_3\text{--}G,\ D_3\text{--}F\ \text{各 240 对 ✓）之精确容量式 ✓；}\ \text{② }\textbf{更重要}：\text{转覆盖侧（}C-457\ \text{已示层容量侧封顶 40 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "奇偶阻断" "跨层奇性" "空机制"
技术词 奇偶阻断 命中文件数=0    ::
技术词 跨层奇性 命中文件数=0    ::
技术词 空机制   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 奇偶阻断 | 0 | 0 | ✓（自造标签 ✓） |
| 跨层奇性 | 0 | 0 | ✓（自造标签 ✓） |
| 空机制 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$5^4$ profile ＋ 全部层对距离分布 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（跨层 $d{=}2$ 为空）已在 §0(2) 显式标注并给**证明** ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
