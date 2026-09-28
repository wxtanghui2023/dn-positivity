# WITROLE-2026-09-28 — **角色分算：近三桶容量 4,4,4／远桶 2–4 ⟹ $|D|\le14{\sim}16$（更正 C-466 之 $[10,14]$）｜$t$ 混淆（✗✗）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:02 令 ✓）**：Type-II 之 $G{\times}F$ 角色分算；**零程序计算**（有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-466／C-465／C-464，非新案 ✓）**
`docs/WITSHRINK-2026-09-28-…`（**状态空间 15/30 ✓✓✓**）｜`docs/WITBUD-2026-09-28-…`（**$11\le c{+}d\le18$ ✓✓✓**）｜`docs/WITG2D-2026-09-28-…`（**$G{\to}D$ 压力 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $R_q$／$D$-容量／$t$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次做角色分算：近三桶容量恒 $4,4,4$、远桶 $2{\sim}4$ ⟹ $|D|\le14{\sim}16$（更正 C-466 之 $[10,14]$）＋ 首次指出唐先生 §6–§8 之 $t$ 与 C-465 之 $t$ 为\ \textbf{两个不同量}** ✓）
**[RESEARCH]**

---

## §0 结论（**$t$ 混淆 ✗✗｜角色分算 ✓✓✓（更正 C-466）｜Type II 仍开 ⚠️**）

$$\boxed{\textbf{(1) ✗✗唐先生 §6–§8 之 }t\textbf{ 与 C-465 之 }t\textbf{ 是\ \textbf{两个不同量}}:\ }\text{唐先生 }t:=\#\{i:\ d_i\ge5\}\ \big(d_i{=}|D_{q_i}|\ \text{＝}D\text{-桶大小 ✓}\big)\ ✗$$
$$\qquad\text{C-465 之 }t:=\big|A_0\cap(d{\ge}5\ \text{profile 层})\big|\ \text{＝\ \textbf{高层的}\ \textbf{点数}}\ ✓\ \big(\text{如 }(5,5,5,7)\ \text{层之 }A_0\text{-点数 ✓}\big)$$
$$\qquad\Longrightarrow\ \text{区间 }[11-t,\ 18-t]\ \text{仅对\ \textbf{后者}成立 ✓}\Longrightarrow\ \text{§7–§8 之"死亡表"\ }\textbf{不成立}\ ✗✗\ \big(\text{无逻辑通道由 }d_i\ \text{推 }t✓\big)$$
$$\qquad\textbf{（正确的 }t\ \text{结构 ✓）}:\ t\ \text{受高层结构限：}(6,6,6,8)\ \text{与}\ (6,8,8,8)\ \text{各}\le1\ \big(\text{C-457 ✓✓}\big)\Longrightarrow t\le18\ \big(|A_0|\le40\ \text{减去 }22\big)\ ✓$$
$$\boxed{\textbf{(2) ✓✓✓角色分算（本档新；\textbf{更正 C-466 之 }[10,14]}）:\ }\text{近桶 }q_i\sim p_0\ \text{须避 }F_0\ \text{与}\ \partial^-G_{q};\ \text{远桶 }q_0\ \text{须避三个 }F_2✓$$
| 族数 | 近三桶容量 | 远桶容量 | $\sum\le$（$d$ 上界） |
|---|---|---|---|
| 5 | $(4,4,4)$ | 2 | **14** |
| 23 | $(4,4,4)$ | 3 | **15** |
| 2 | $(4,4,4)$ | 4 | **16** |
$$\qquad\Longrightarrow\ \boxed{|D|\le\mathbf{14}\sim\mathbf{16}}\ ✓✓\ \big(\textbf{C-466 之 }[10,14]\ \textbf{系过强} ✗\ \text{—— 彼时把 }F_0\ \text{错加于四桶全体 ✗}\big)$$
$$\qquad\textbf{（机制 ✓✓）}:\ \text{近桶仅需避 }F_0\ \text{之 4 个 triple}\ \big(20-12-4=4\ \text{可用 ✓ 且仍可满 packing ✓}\big)\Longrightarrow \text{近桶\ \textbf{无损} ✓✓};\ \text{压力全在远桶 ✓（}2{\sim}4\big)$$
$$\boxed{\textbf{(3) ⚠️预算相容性（更正后仍相容）}:\ }c\ge3\Longrightarrow c+d\le\min(18,\ 3{+}16)=18\Longrightarrow\boxed{[11,18]\ \text{相容} ⟹ \text{Type II 仍开}}\ ⚠️$$
$$\qquad\textbf{（含正确 }t\big):\ \text{若 }t{=}0\ \text{则区间 }[11,18]✓;\ \text{若 }t\ge2\ \text{则 }[9,16]\ \text{或更紧 ✓}\ \big(\text{但 }t\ge2\ \text{未被强制 ✗}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ 33\le|A_0|\le40\Rightarrow11\le c+d\le18✓✓;\ c\ge3\Rightarrow d\ge11-c✓✓\ \big(\text{联合 profile 之提法 ✓✓}\big)$$
$$\textbf{§2 ✓✓}:\ \text{角色标签（带标签四元组而非总和）✓✓ 正确 —— 本档即按此执行 ✓✓};\ |R_q|\in\{2,3,4\}✓$$
$$\textbf{§3 ✓✓✓}:\ \text{"四个 }D\text{-桶不对称：三个邻满桶、一个邻三普通桶"\ \textbf{完全正确} ✓✓✓\ \big(\text{C-466 §1(3) 已标 ⚠️，本档算实 ✓}\big)};\ d{=}d_{\text{near}}{+}d_{\text{far}}✓$$
$$\textbf{§4 ✗（须删）}:\ "c_{\min}(\sigma)"\ \text{之提法 ✗ —— 由 C-465 之更正，}C_p\ \text{可为\ \textbf{空}}\ ✓\Longrightarrow c\ \text{无此下界 ✗}\ \big(\text{仅 }|C_{p_*}|{=}3\Rightarrow c\ge3✓\big)$$
$$\textbf{§5 ✗（据 §4）}:\ "L_\sigma{+}U_\sigma<11\ \text{即死"\ 之框 ✗ —— }L_\sigma\ \text{不存在 ✗；正确可用的只有 }U_\sigma\ \text{与 }c+d\ge11✓\ \big(\text{即 }d\ \text{之\ \textbf{下}界由 }c\ \text{满足 ⟹ 不能单向杀 ✓}\big)$$
$$\textbf{§6–§8 ✗✗}:\ \text{见 §0(1)（}t\ \text{混淆 ⟹ 死亡表 ✗）}$$
$$\textbf{§9 ✓（形式 ✓）}:\ \text{六列表／逐门过滤之框架 ✓✓\ \big(\text{Gate 1 之 }d_q\in\{2,3,4\}\ \text{与 Gate 2 之角色区分 ✓ 皆正确 ✓；Gate 3–5 因 }t\ \text{混淆须改 ✗；Gate 6 无 }c_{\min}\ ✗\big)}$$
$$\textbf{§10 ✗}:\ "t\ge2\ \text{是否被强制"\ 之问 §\ \text{其 }t\ \text{非 }C-465\ \text{之 }t ✗；按正确 }t\ \text{（高层点数）其可 }=0✓\Longrightarrow\ \text{该 P2\ \textbf{不成立} ✗✓}$$
$$\textbf{✓（保留）}:\ \text{"不做 SAT、不做大规模搜索"\ ✓✓\ \text{与宪法一致 ✓}}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{|D|\le14\sim16}\ ✓✓\ \big(\text{角色分算；更正 C-466}\big);\ \text{② 近桶容量恒 4、压力全在远桶 ✓✓};\ \text{③ }11\le c+d\le18✓✓;\ \text{④ }|C|\ge3✓;\ \text{⑤ 状态空间 15/30 ✓✓};\ \text{⑥ Type I KILLED ✓✓✓};\ \text{⑦ }t\ \text{＝高层点数（与 }d_i\ \text{无关）✓};\ \text{⑧ 高层 }\le1{+}1\ \text{（两层）✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"死亡表（依 }t{=}\#\{d_i{\ge}5\}\text{）"}\ ✗✗;\ \text{"}c_{\min}\ \text{存在"}\ ✗;\ \text{"}t\ge2\ \text{被强制"}\ ✗;\ \text{C-466 之 }[10,14]\ ✗\ \big(\text{过强}\big)$$
$$\textbf{未确立 ⚠️}:\ \text{Type II 全局可行性};\ \text{Type III};\ a{=}45\ \text{的排除};\ M\ \text{之真值}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 按修正后之门（}d_q\in\{2,3,4\}✓\text{、角色 ✓、}11-t\le c+d\le18-t\ \text{含\ \textbf{正确} }t✓\big)\ \text{做\ \textbf{精确} $(c,d)$ profile 表};\ \text{② Type III（}|F|{=}3\ \text{类结构定理 ✓）};\ \text{③ 覆盖侧对 }|C|\ \text{之任何真实下界 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "角色分算" "近远桶" "t混淆"
技术词 角色分算 命中文件数=0    ::
技术词 近远桶   命中文件数=0    ::
技术词 t混淆    命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 角色分算 | 0 | 0 | ✓（自造标签 ✓） |
| 近远桶 | 0 | 0 | ✓（自造标签 ✓） |
| t混淆 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（有限穷举：15 桶／30 族／各桶 packing ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处必改**：$t$ 混淆（§6–§8）与 C-466 之 $[10,14]$（本档自纠 ✓）已在 §0 显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
