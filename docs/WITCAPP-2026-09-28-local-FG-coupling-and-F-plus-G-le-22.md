# WITCAPP-2026-09-28 — **局部 $F$--$G$ 耦合（新 ✓✓✓）：$g_q{=}3\Rightarrow\Sigma\le8$；精确表 $\max(|F|{+}|G|)\le\mathbf{22}$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:36 令 ✓）**：$F$--$G$ 局部耦合；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。
> **标签（照唐先生固定 ✓）**：$P$＝偶部、$A_1$＝奇部。

**已查地图：命中（接续 C-455／C-453／C-452，非新案 ✓）**
`docs/WITCOUP-2026-09-28-…`（**$r_q$ 分类／$|\mathcal W|\equiv3$ ✓✓✓**）｜`docs/WITDEC-2026-09-28-…`（**$c+d\le20$／$|F|\le16$／$|G|\le12$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $F$--$G$ 耦合／$\partial^-G$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $F_i\cap F_j=\varnothing$ 与 $\partial^-G$ 联合之精确局部容量表（$g{=}0,1,2,3\Rightarrow\Sigma\le12,12,8,8$）＋ 精确表 $\max(|F|{+}|G|)\le22$** ✓）
**[RESEARCH]**

---

## §0 结论（**$\partial^-G$ 机制 ✓✓✓（新）｜容量比唐先生给得更强 ✓✓｜$\max(F{+}G)\le22$ ✓✓（新）**）

$$\textbf{设定 ✓}:\ \text{prefix 图}=F_2^3=Q_3✓\ \text{每点\ \textbf{3} 邻}\ ✗\big(\text{非 }Q_4/4\text{ 邻}\ ✗\big);\ F_p\subseteq\binom{[6]}3✓,\ G_q\subseteq\binom{[6]}4✓;\ s_q:=\sum_{p\sim q}|F_p|\le12✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §1 之 }F_i\cap F_j=\varnothing\ \textbf{成立（新，本档确认）}:\ \text{若 }v\in F_{p_i}\cap F_{p_j}\ (p_i\ne p_j\ \text{皆偶})\Longrightarrow}$$
$$\qquad d\big((p_i,v),(p_j,v)\big)=d_{\text{pref}}(p_i,p_j)=2\ \big(\text{偶 prefix 互距 2 ✓}\big)\Longrightarrow \text{违反 }d(A_0)\ge3\ ✗\ \Longrightarrow\ \boxed{F_i\cap F_j=\varnothing}✓✓$$
$$\boxed{\textbf{(2) ✓✓✓唐先生 §2 之 }\partial^-G\ \textbf{机制成立（新，且\ \textbf{严格} ✓✓）}:\ }\partial^-G:=\bigcup_{w\in G_q}\binom w3;\quad v\in F_{p}\ (p\sim q)\Longrightarrow v\not\subseteq w\ \forall w\in G_q$$
$$\qquad\big(\text{否则 }d=1+1=2\ ✗\big)\Longrightarrow \text{恰为}\ \boxed{F_p\cap\partial^-G=\varnothing}✓✓$$
$$\boxed{\textbf{(3) ✓✓✓精确局部容量（本档穷举定值；}\textbf{唐先生三条中两条更强} ✓✓）:}$$
| $g_q=\|G_q\|$ | $\|\partial^-G\|$ | 可用三集 | $\max\Sigma_{p\sim q}f_p$ （穷举 ✓） | 唐先生之值 |
|---|---|---|---|---|
| 3（两两交 2 ✓） | 12 | 8 | $\mathbf8$ ✓✓ | 8 ✓（**对** ✓） |
| 2 | 8 | 12 | $\mathbf8$ ✓✓ | 12 ✗（**更强** ✓） |
| 1 | 4 | 16 | $\mathbf{12}$ ✓✓ | 14 ✗（**更强** ✓） |
| 0 | 0 | 20 | $\mathbf{12}$ ✓✓ | 16 ✗（**$\le12$** ✓） |
$$\qquad\Longrightarrow\ \text{（因仅 3 邻 ⟹ }s_q\le12✓\big):\quad \boxed{s_q\le8\ \Longrightarrow\ g_q\le3;\qquad 9\le s_q\le12\ \Longrightarrow\ g_q\le1}✓✓✓$$
$$\qquad\textbf{注 ✓}:\ \text{唐先生第 4 行"}$g{=}0\Rightarrow\Sigma\le16$\ ✗\ \text{系源自 4 邻假设 ✗；真值 }\{0,1\},\{2,3\}\ \text{皆同 ⟹ 只需两档 ✓✓}$$
$$\boxed{\textbf{(4) ✗✗唐先生 §3／§5 之 }Q_4\text{／"四个偶邻"}\ \textbf{仍误}:\ }\text{每奇 }q\ \text{仅 3 偶邻（穷举 ✓）}\Longrightarrow s_q\le12\ \big(\text{非 }16✗\big)$$
$$\qquad\Longrightarrow\ \text{其表中 }s=13,\dots,16\ \text{三行\ \textbf{空置} ✗}\ \Longrightarrow\ \text{§8／§9 之"}|F|{=}15,16\Rightarrow|G|{=}0\text{"}\ ✗\ \text{不成立 ✓}$$
$$\qquad\textbf{（正确 ✓✓）}:\ s_q=|F|-f_{p(q)}\ \big(\text{每奇 }q\ \text{恰缺一个偶 prefix}\ ✓\big)\Longrightarrow |F|=16\Rightarrow s_q\equiv12\Rightarrow g_q\le1\Rightarrow\boxed{|G|\le4}✗\to✓\ \big(\text{非 }0✗\big)$$
$$\boxed{\textbf{(5) ✓✓唐先生 §11 之方法对，但系数错}:\ \text{若 }|G|=12\Rightarrow g_q\equiv3\Rightarrow s_q\le8\ \forall q\Longrightarrow \sum_q s_q\le32;\quad \sum_q s_q=3|F|\ \big(\text{每偶点 3 奇邻 ✓}\big)}$$
$$\qquad\Longrightarrow 3|F|\le32\ \big(\text{非 }4|F|✗,\ \text{亦非 }4\times8{=}32\Rightarrow F\le8✗\big)\Longrightarrow\boxed{|G|=12\Rightarrow|F|\le10}\Longrightarrow\boxed{|F|+|G|\le22}✓✓\ \big(\text{非 }20✗\big)$$
$$\boxed{\textbf{(6) ✓✓✓本档新获：精确 profile 优化（照唐先生 §13／§14）}:\ \text{穷举全部 }5^4=625\ \text{个 }(f_p)\ \text{profile}\ \big(\text{配 }\sum_q s_q=3|F|✓\big):}$$
$$\qquad\boxed{\max\big(|F|+|G|\big)\ \le\ \mathbf{22}}✓✓\ \big(\text{原为 }28\ ✗\big)\quad\text{（于 }(0,4,4,4):|F|{=}12,|G|\le10\ \text{与}\ (2,2,2,4):|F|{=}10,|G|\le12\ \text{取到 ✓）}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓（内容 ✓，图名 ✗）}:\ F_i\cap F_j=\varnothing\ \text{正确 ✓✓（见 §0(1) ✓）；唯"}$Q_4$/4 邻"\ ✗$$
$$\textbf{§2 ✓✓}:\ \partial^-G\ \text{之禁配 ✓✓（见 §0(2) ✓）；"所有 }F_i\ \text{须避开 }\partial^-G"\ \textbf{正确} ✓✓$$
$$\textbf{§3 ✓✓}:\ \text{三重交 ⟹ }\|\partial^-G\|{=}4\times3{=}12✓\ \big(\text{无重合：三集若重合须 }\subseteq w\cap w'\ \text{而 }\|w\cap w'\|{=}2✗\big)✓✓;\ g{=}3\Rightarrow\Sigma\le8\ ✓✓$$
$$\textbf{§4 ✓（算术 ✓）}:\ \|\partial^-G\|{=}4+4=8✓\ \big(\text{同因：两 quad 交 2 ⟹ 三集不重合 ✓}\big)✓;\ \text{但 }g{=}2\Rightarrow\Sigma\le\mathbf8\ \text{（本档穷举 ✓，比其 }12\ \textbf{更强} ✓✓）$$
$$\textbf{§5 ✗（方向对，数值弱）}:\ g{=}1\Rightarrow\Sigma\le\mathbf{12}✓✓\ \big(\text{非 }14✗\big);\quad \text{其"16 个剩余三集不能全塞进 3 个族"\ \textbf{结论对}}\ ✓✓\ \big(\text{本档穷举确认}\ ✓\big)$$
$$\textbf{§6 ✗}:\ g{=}0\Rightarrow\Sigma\le12\ ✗\big(\text{非 }16✗\big)\ \text{—— 因仅 3 邻，}\Sigma\ \text{上限即 }12✓$$
$$\textbf{§7 ✓（形式 ✓）}:\ \text{反向阈值表\ \textbf{形式正确} ✓✓；但 }s\ \text{只到 12 ⟹ 只需两档（}\le8\text{／}9..12\big)✓✓$$
$$\textbf{§8 ✗✗}:\ |F|{=}16\Rightarrow|G|{=}0\ ✗\ \text{（正确 }|G|\le4✓,\ \text{见 §0(4) ✓）}$$
$$\textbf{§9 ✗✗}:\ |F|{=}15\Rightarrow|G|{=}0\ ✗\ \text{（正确 }|G|\le4✓:\ n=15\ \text{时 }s_q\in\{11,12\}\Rightarrow g_q\le1\ \forall q✓\big)$$
$$\textbf{§10 ✗}:\ "G{>}0\Rightarrow F\le14"\ ✗\ \text{（不成立：}|F|{=}16\ \text{时 }|G|\le4{>}0\ \text{允许 ✓）}$$
$$\textbf{§11 ✓（方法 ✓）/ ✗（系数）}:\ \text{见 §0(5)（}3|F|\le32\Rightarrow|F|\le10✓,\ F{+}G\le22✓\big)$$
$$\textbf{§13–§14 ✓✓✓}:\ \text{profile 优化之提法\ \textbf{完全正确} ✓✓✓\ \big(\text{本档即照此执行 ✓，得 }22✓\big)；}"s_q=F_{\text{tot}}-\text{某两项补集}"\ \text{之直觉 ✓✓（精确为 }s_q=|F|-f_{p(q)}✓\big)$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }F_i\cap F_j{=}\varnothing\ ✓✓;\ \text{② }\partial^-G\ \text{禁配 ✓✓;\ \text{③ 局部表 }(s_q\le8\Rightarrow g_q\le3;\ 9..12\Rightarrow\le1)✓✓✓;\ \text{④ }\boxed{\max(|F|{+}|G|)\le22}✓✓;\ \text{⑤ }|G|{=}12\Rightarrow|F|\le10✓;\ |F|{\ge}15\Rightarrow|G|\le4✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"}|F|{=}15/16\Rightarrow|G|{=}0\text{"}\ ✗;\ \text{"}G{>}0\Rightarrow F\le14\text{"}\ ✗;\ \text{"}g{=}1\Rightarrow\Sigma\le14\text{"}\ ✗;\ \text{"}g{=}0\Rightarrow\Sigma\le16\text{"}\ ✗;\ \text{"}4|F|\le32\text{"}\ ✗;\ \text{"}Q_4\text{／4 邻"\ ✗}$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{全局可行性};\ \text{（}22\ \text{是否为该模型内的真极值亦未证 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 把 }|C|\le12,\ |D|\le12\ \text{与 }\boxed{|F|{+}|G|\le22}\ \text{联立（}d{=}3\ \text{与 }d{=}4\ \text{两层 ✓）};\ \text{② 用 }d(x,y){=}2\ \text{禁止联 }F\text{--}G\text{--}C_3/D_3✓;\ \text{③ }\Gamma_C,\Gamma_D\ \text{三元 profile ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "局部耦合引理" "禁三集容量" "互斥端点"
技术词 局部耦合引理 命中文件数=0    ::
技术词 禁三集容量   命中文件数=0    ::
技术词 互斥端点     命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 局部耦合引理 | 0 | 0 | ✓（自造标签 ✓） |
| 禁三集容量 | 0 | 0 | ✓（自造标签 ✓） |
| 互斥端点 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$\binom{15}3$ 组 $G$ ＋ 族回溯 ＋ $5^4$ profile ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **五处必改**（$Q_4$／$g{=}1,2,3$ 之数值／§8–§10 之端点／§11 系数）已在 §0(3)(4)(5) 显式标注 ✓✓
- **本线新最强 $d{=}4$ 层界 ＝ $\max(|F|{+}|G|)\le22$** ✓✓（引用须用此形式 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
