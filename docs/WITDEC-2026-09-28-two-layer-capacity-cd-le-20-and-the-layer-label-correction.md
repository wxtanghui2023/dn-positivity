# WITDEC-2026-09-28 — **$c+d\le20$ 成立（✓✓，替代 C-452 的 $d\le16$ 路线）＋ 层标签纠正 ＋ 修正 $|F|\le16$／$|G|\le12$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏 ✓（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:29 令 ✓）**：$d=3$／$d=4$ 两层容量与 per-prefix 界；**零程序计算**（仅 $512$ 点＋有限族穷举核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-452／C-451／C-450，非新案 ✓）**
`docs/WITLAYER-2026-09-28-…`（**14 行 profile 分解／$K_{4,4}{-}M$ ✓✓✓**）｜`docs/WITCUBE-2026-09-28-…`（**$Q_3$ 闭环 ✓✓✓**）｜`docs/WITPROF-2026-09-28-…`（**两 profile ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $d{=}3/4$ 层／per-prefix 族对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次核验 §1/§3 邻居 profile 分解（$C{:}2B{+}3C'{+}4$、$D{:}0B{+}3C'{+}3{+}3$、$F{:}3C{+}3D{+}3$、$G{:}4D{+}3{+}2$）＋ 确立 $c+d\le20$（替代 $d\le16$ 路线）＋ 纠正层标签并给出 $|F|\le16$／$|G|\le12$／$(6,6,6,8)$ 层 $\le1$** ✓）
**[RESEARCH]**

---

## §0 结论（**$c+d\le20$ ✓✓✓（关键）｜层标签 ✗✗｜$|F|\le16$／$|G|\le12$ ✓✓**）

$$\textbf{设定 ✓}:\ A_1=\{e_1,e_2,e_3,e_1{\oplus}e_2{\oplus}e_3\}✓;\ J=\{4,\dots,9\}\ (|J|{=}6✓);\ A_0\subseteq R,\ d(A_0)\ge3✓;\ x=(u,v)\in F_2^3\times F_2^6✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §1／§3 之邻居 profile 分解\ \textbf{全对}（本档穷举核验 ✓✓）}}$$
| 层 | 点数 | 其 9 个邻点之 profile 分解（穷举 ✓） |
|---|---|---|
| $C=(3,3,3,5)$ | 60 | $\mathbf{2}\times(2,2,2,4)+\mathbf{3}\times(2,4,4,4)+4\times(4,4,4,6)$ ✓✓ |
| $D=(3,5,5,5)$ | 80 | $\mathbf{0}\times(2,2,2,4)+\mathbf{3}\times(2,4,4,4)+3\times(4,4,4,6)+3\times(4,6,6,6)$ ✓✓ |
| $F=(4,4,4,6)$ | 80 | $\mathbf{3}\times(3,3,3,5)+\mathbf{3}\times(3,5,5,5)+3\times(5,5,5,7)$ ✓✓ |
| $G=(4,6,6,6)$ | 60 | $\mathbf{0}+\mathbf{4}\times(3,5,5,5)+3\times(5,5,5,7)+2\times(5,7,7,7)$ ✓✓ |
$$\textbf{(2) ✓✓✓}:\ \text{唐先生 §2 之}\ \boxed{c\le12,\ \ c+d\le20}\ \textbf{成立且严格}\ ✓✓\ \big(\text{本档确认，并\ \textbf{替代} C-452 之 }d\le16\ \text{路线}\ ✓✓\big)$$
$$\qquad\textbf{论证 ✓✓}:\ A_0\ \text{两点不可共享邻点（否则 }d\le2\ \text{违 }d\ge3✗\big)\Longrightarrow 2c\le|B|=24✓;\quad 3c+3d\le|(2,4,4,4)|=60⟹c+d\le20✓✓$$
$$\qquad\qquad\Longrightarrow\boxed{|A_0\cap\{d(A_1)=3\}|\le20}\ \wedge\ \boxed{|A_0|\ge33\Rightarrow\#\{d(A_1)\ge4\}\ge\mathbf{13}}\ ✓✓\ \big(\text{唐先生更正后之结论\ \textbf{现为严格} ✓✓}\big)$$
$$\boxed{\textbf{(3) ✓唐先生 §5 正确（且其自我警示 ✓✓）}:\ }\text{容量须用\ \textbf{壳层}（}C_3{=}60,\ D_3{=}80\text{）而非 }|C|,|D|✓✓\ \big(\text{唐先生自标"容易再次滑落"\ ✓✓\big)}$$
$$\qquad\Longrightarrow 3|F|\le|C_3|=60\Rightarrow\boxed{f\le20}✓;\quad 3f+4g\le|D_3|=80\Rightarrow\boxed{3f+4g\le80}✓✓$$
$$\boxed{\textbf{(4) ✗✗唐先生 §7 之"}$F$--$G$ 无禁止边"$\ \textbf{不成立}:\ \text{系基于错误 suffix 权重（其令 }G\ \text{之 }w=111111\ ✗\big)}$$
$$\qquad\textbf{真实 ✓✓}:\ F\ \text{层}=(\text{偶 prefix},\,|v|{=}3)✓;\quad G\ \text{层}=(\text{奇 prefix},\,|w|{=}4)✓\ \big(\text{由 }(r{+}1,\dots)\ \text{与}\ (r,\dots)\ \text{参数化定出 ✓}\big)$$
$$\qquad\Longrightarrow |v\oplus w|\in\{1,3,5,7\}\ \big(\text{奇 ✓}\big);\quad d(x,y)=d_{\text{prefix}}(p,q)+|v\oplus w|\ \big(\text{偶 ✓}\big)$$
$$\qquad\Longrightarrow \boxed{d(x,y)=2\ \text{可达（}d_{\text{pref}}{=}1\ \text{且}\ |v\oplus w|{=}1\text{）}\Longrightarrow \textbf{禁止}\ ✗✓}\ \big(\text{故该线\ \textbf{有约束、可用} ✓✓，非空 ✗}\big)$$
$$\textbf{(5) ✗✗}:\ \text{唐先生 §10／§11 之\textbf{层标签错位}（本档纠正}\ ✓✓\big):\ \text{weight-4 suffix 层}=(4,6,6,6)\ \big(\text{其"}\,G\,\text{"}\big)\ \text{而非 }F✗;\ \text{唯一 suffix 层}=(6,6,6,8)\ \text{而非 }G✗$$
$$\qquad\textbf{纠正后之正确界 ✓✓（穷举定值 ✓）}:\ \text{同 prefix、suffix 两两 }d\ge3\Longrightarrow$$
$$\qquad\qquad F\ \text{层（}weight\text{-}3,\ \text{需 }|v\cap v'|\le1\text{）}:\ \text{极大族}=\mathbf4\ \big(\text{＝Johnson }D(6,3,2)✓\big)\Longrightarrow\boxed{|F|\le4\times4=16}✓✓\ \big(\text{非 }12✗\big)$$
$$\qquad\qquad G\ \text{层（}weight\text{-}4,\ \text{需 }|w\cap w'|\le2\ \text{即补集不相交}\big):\ \text{极大族}=\mathbf3\Longrightarrow\boxed{|G|\le4\times3=12}✓✓\ \big(\text{非 }1✗\big)$$
$$\qquad\qquad (6,6,6,8)\ \text{层（唯一 suffix}\big):\ \text{四 prefix 两两距离 2}\Longrightarrow \text{至多选 1}\Longrightarrow\boxed{\le1}✓✓\ \big(\text{唐先生 §11 之论证\ \textbf{正确但作用层错} ✗✓\big)}$$
$$\qquad\Longrightarrow\ |A_0\cap\{d{=}4\}|\le16+12=28✓\ \big(\text{非 }13✗\big)\Longrightarrow\ \boxed{\text{"33 临界"}\ ✗\ \text{不成立}}\ \big(20+28=48>33✓\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓✓}:\ \text{见 §0(1) 之四行表（穷举逐点核 ✓✓）};\ \text{唐先生"每个 }C\text{-点 }2B{+}3C'\text{"与"每个 }D\text{-点 }0B{+}3C'\text{"\ \textbf{完全正确} ✓✓}$$
$$\textbf{§2 ✓✓✓}:\ c\le12\ \text{与 }c+d\le20\ \text{均严格 ✓✓};\ \text{且此路线\ \textbf{优于} C-452 之 }d\le16\ \big(\text{本档明示替代 ✓}\big)$$
$$\textbf{§3 ✓✓}:\ F{:}3C{+}3D;\ G{:}4D\ \text{均正确 ✓✓（穷举：}G\ \text{确为 4 个 }(3,5,5,5)\text{-邻 ✓）}$$
$$\textbf{§4 ✓✓（关键纪律）}:\ \text{不能拿 }|C|,|D|\ \text{当容量}\ \big(\text{邻点不必属 }A_0\ ✓\big)\Longrightarrow \textbf{完全正确}\ ✓✓\ \big(\text{本档予以确认并致意}\ ✓\big)$$
$$\textbf{§5 ✓}:\ \text{壳层容量 }f\le20,\ 3f+4g\le80✓✓$$
$$\textbf{§6 ✓（诚实）}:\ \text{四变量约束不足以杀 33 ✓✓（唐先生自陈 ✓）}$$
$$\textbf{§7 ✗✗}:\ \text{见 §0(4)（层权重错 ⟹ 结论反 ✓）}$$
$$\textbf{§8 ✓✓}:\ \text{同 prefix}\Longrightarrow d=d(v,v')✓;\quad \text{异 prefix}\Longrightarrow d=2+d(v,v')✓\ \big(\text{因 }P\text{-prefix 两两距离 2}\ ✓✓\big);\quad \text{且要求 }v\ne v'✓✓$$
$$\textbf{§9 ✓✓}:\ \text{weight-4 互距必偶 ⟹ }d\ge4\iff|S\cap S'|\le2✓✓;\ \text{补集 }T\ \text{为 2-子集 ⟹}|S\cap S'|=2+|T\cap T'|✓✓\ \big(\text{核对 ✓}\big)$$
$$\textbf{§10 ✗（层错）}:\ \text{论证正确（互不相交 2-子集}\le3✓\big)\ \text{但作用于 }G\ \text{层（}weight\text{-}4\big)\ \text{而非 }F✗\Longrightarrow|G|\le12✓✓\ \text{而非 }|F|\le12✗$$
$$\textbf{§11 ✗（层错）}:\ \text{"唯一 suffix ⟹ }\le1\text{"之论证正确 ✓ 但作用于}(6,6,6,8)\ \text{层 ✗（其 24 点 ✓）而非 }(4,6,6,6)✗$$
$$\textbf{§12–§13 ✗}:\ \text{由 }|F|\le12,|G|\le1\ \text{得 }13✗;\ \textbf{正确}:\ 16+12=28✓\Longrightarrow\ \text{不逼出 33 临界 ✗}$$
$$\textbf{§13 之 "}c{+}d{=}20,f{=}12,g{=}1\ \text{被迫"\ ✗}:\ \text{不被迫 ✓（}d\ge4\ \text{有 28 个槽位 ✓）};\ \textbf{唯 }c+d\le20\ \text{为硬约束 ✓✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 四层邻居分解（§0(1) ✓✓）};\ \text{② }\boxed{c\le12,\ c+d\le20}\ \big(\Rightarrow\ \ge13\ \text{点落 }d\ge4✓✓\big);\ \text{③ }f\le20,\ 3f+4g\le80✓;\ \text{④ }\boxed{|F|\le16},\ \boxed{|G|\le12}✓✓;\ \text{⑤ }(6,6,6,8)\ \text{层}\le1✓✓;\ \text{⑥ }F\text{--}G\ \text{有禁止边（}d{=}2✓）✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}F\text{--}G\ \text{无禁止边"\ ✗};\ \text{"}|F|\le12\text{"}\ ✗;\ \text{"}|G|\le1\text{"}\ ✗;\ \text{"}c+d\le20\ \text{来自 }d\le8\text{"}\ ✗\ \big(\text{正确来源＝两层容量 ✓✓}\big);\ \text{"33 临界"\ ✗}$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{之全局可行性};\ \text{（}c+d\le20\ \text{已为\ \textbf{目前最强} 的 }A_0\ \text{容量界 ✓✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 用 }\boxed{d(x,y)=2\ \text{禁止}}\ \text{联立 }F\text{--}G\ \big(\text{唐先生谓"空"}\ ✗\ \text{故可用 ✓✓}\big);\ \text{② }F\ \text{之 per-prefix 族（}weight\text{-}3,\ \text{交}\le1,\ \text{极大 4}\big)\ \text{与 }C_3/D_3\ \text{之碰撞 ✓};\ \text{③ }(6,6,6,8)\le1\ \text{之接入 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "壳层容量" "层标签错位" "per-prefix 界"
技术词 壳层容量     命中文件数=1    :: ./SHELLBUDGET-2026-09-26-shell-private-budget-and-square-count-bounds.md
技术词 层标签错位   命中文件数=0    ::
技术词 per-prefix 界 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 壳层容量 | **1**（`SHELLBUDGET-2026-09-26-…` ⟹ **既有 ⟹ 不计** ✗） | 0 | ✗（**非新增** ✓） |
| 层标签错位 | 0 | 0 | ✓（自造标签 ✓） |
| per-prefix 界 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条\ \textbf{已先跑后写} ✓✓**：三词均在**写入前**测得 ✓；与 C-451／C-452 之自击形成对照 ✓）

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅 $512$ 点邻居分解 ＋ 有限族极大性穷举 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **三处必改**（§7 层权重、§10／§11 层标签、§12 之 33）已在 §0(4)(5) 显式标注 ✓✓
- **本线最强 $A_0$ 界 ＝ $c+d\le20$** ✓✓（用其后续论证时须引用此形式 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
