# WITLAYER-2026-09-28 — **$R$ 的 profile 分解全对（✓✓）＋ $c\le12$（✓）＋ $d\le16$（修正 §7 的 $\le8$）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 12:25 令 ✓）**：$R$ 之 profile 分层与 $A_0$ 攻击；**零程序计算**（仅 512 点有限穷举核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-451／C-450／C-449，非新案 ✓）**
`docs/WITCUBE-2026-09-28-…`（**$Q_3$ 闭环／$N_2$ 接口／$|N_2[A_1]|{=}116$ ✓✓**）｜`docs/WITPLANE-2026-09-28-…`（**二维仿射平面 ✓✓**）｜`docs/WITPROF-2026-09-28-…`（**两 profile ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词亦**先跑** ✓，见 §4）
D0: 本档对象 ＝ **档案已有** $R$-profile／$E_1,E_2$／$A_0$-层对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次核验 $R$ 之 14 行 profile 分解（含被遗漏之 $(1,1,1,3)$＝偶部 4 点）＋ $E_1\!\leftrightarrow\! E_2$ 之 $K_{4,4}{-}M$ 结构＋ $c\le12$ 之确认＋ 修正 $d\le8$ 为 $d\le16$（$\le2$ per $E_1$-点）** ✓）
**[RESEARCH]**

---

## §0 结论（**profile 分解 ✓✓✓｜$c\le12$ ✓｜$d\le16$ ✗（非 8）**）

$$\textbf{设定 ✓}:\ A_1=\{e_i,e_j,e_k,e_i{\oplus}e_j{\oplus}e_k\}\ \big(i,j,k=1,2,3✓\big);\ J=\{4,\dots,9\}\ (|J|{=}6✓);\ A_0\subseteq R,\ d(A_0)\ge3✓$$
$$\qquad\textbf{profile}(x):=\big(d(x,a)\big)_{a\in A_1}\ \text{（多重集 ✓）};\quad x=(u,v)\in F_2^3\times F_2^6,\ r:=|v|✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §2 之 profile 分解\ \textbf{全对}（本档穷举核验 ✓✓）}:\ \text{全 }512\ \text{点分 14 行 ✓✓}}$$
| profile | 点数 | $\min$ | 归层 |
|---|---|---|---|
| $(0,2,2,2)$ | 4 | 0 | $A_1$ |
| $\mathbf{(1,1,1,3)}$ | **4** | 1 | $N_2$（**唐先生表遗漏 ✗ —— 此即偶部 $P$ 自身 ✓**） |
| $(1,3,3,3)$ | 24 | 1 | $N_2$（$=E_1$ ✓） |
| $(2,2,2,4)$ | 24 | 2 | $N_2$（$=E_2$ ✓） |
| $(2,4,4,4)$ | 60 | 2 | $N_2$ |
| $(3,3,3,5)$ | 60 | 3 | $R$ |
| $(3,5,5,5)$ | 80 | 3 | $R$ |
| $(4,4,4,6)$ | 80 | 4 | $R$ |
| $(4,6,6,6)$ | 60 | 4 | $R$ |
| $(5,5,5,7)$ | 60 | 5 | $R$ |
| $(5,7,7,7)$ | 24 | 5 | $R$ |
| $(6,6,6,8)$ | 24 | 6 | $R$ |
| $(6,8,8,8)$ | 4 | 6 | $R$ |
| $(7,7,7,9)$ | 4 | 7 | $R$ |
$$\qquad\Longrightarrow\ \boxed{|N_2[A_1]|=116},\quad \boxed{|R|=396}✓✓\ \big(\text{与 C-451 之实测一致 ✓}\big);\quad \text{参数化 ✓}:\ u\in A_1\Rightarrow(r,r{+}2,r{+}2,r{+}2)✓;\ u\in P\Rightarrow(r{+}1,r{+}1,r{+}1,r{+}3)✓$$
$$\boxed{\textbf{(2) ✓✓唐先生 §3–§4 正确}:\ }\text{固定 }\ell\in J:\ E_1(\ell)=\{a\oplus e_\ell\},\ E_2(\ell)=\{q\oplus e_\ell\}\ \big(|{\cdot}|{=}4✓\big)\ \text{间为\ \textbf{3-正则二部图 ✓✓}}$$
$$\qquad\text{（穷举核 ✓）}:\ \text{边数 }12✓,\ \text{左度全 3✓}\Longrightarrow \text{补图为完美匹配}\Longrightarrow E_1(\ell)\!\leftrightarrow\! E_2(\ell)\cong\boxed{K_{4,4}-M}✓✓;\quad \ell\ \text{取 6 值}\Longrightarrow\text{6 个同构块 ✓✓}$$
$$\qquad D_2\ \text{闭合 ✓✓}:\ \binom42=6\ \text{对}\times(2\times6=12)=72=24\times\binom32=72✓✓\ \big(\text{每个 }E_2\text{-点恰距 3 个 }A_1\text{-点 ✓}\big)$$
$$\boxed{\textbf{(3) ✓✓唐先生 §6：}c:=|A_0\cap(3,3,3,5)|\Longrightarrow\boxed{c\le12}}\ ✓✓\ \big(\text{穷举核：60 个 }(3,3,3,5)\ \text{点\ \textbf{每点恰 2 个} }E_2\text{-邻 ✓✓}\big)$$
$$\qquad\textbf{论证 ✓✓}:\ x,y\in A_0\ \text{不可共享邻点（否则 }d(x,y)\le2\ \text{违 }d(A_0)\ge3✗\big)\Longrightarrow 2c=|{\cdot}|\le|E_2|=24\Longrightarrow c\le12✓✓$$
$$\boxed{\textbf{(4) ✗✗唐先生 §7 之 }$d\le8$\textbf{ 太强（本档修正）}:\ \text{其"任意两个共 }y\ \text{的 }D\text{-点距离恰为 2"}\ ✗\ \text{—— 可以是\ \textbf{4}}\ ✓\big)}$$
$$\qquad\textbf{正确 ✓✓}:\ y=a\oplus e_\ell\in E_1;\ \text{与之距离 2 的 }D\text{-点为}\ x=a\oplus v\ \big(\ell\in v,\ |v|{=}3,\ v\subseteq J✓\big)✓;\ \text{共 }\binom52=10\ \text{个（层内 ✓）}$$
$$\qquad\qquad\text{但 }A_0\ \text{内两两 }d\ge3\Longrightarrow|v\oplus v'|=2|v\setminus v'|\ge3\Longrightarrow|v\setminus v'|\ge2\Longrightarrow|v\cap v'|\le1\Longrightarrow P_v\cap P_{v'}=\varnothing✓$$
$$\qquad\qquad\big(\text{记 }v=\{\ell\}\cup P_v,\ |P_v|{=}2,\ P_v\subseteq J\setminus\{\ell\}\ (5\ \text{元})\ ✓\big)\Longrightarrow\ \text{互不相交 2-子集}\le\lfloor5/2\rfloor=\mathbf2✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{每个 }E_1\text{-点至多服务 \textbf{2} 个 }D\text{-点}}\Longrightarrow 3d\le2\cdot24=48\Longrightarrow\boxed{d\le16}✓✓\ \big(\text{非 }8✗\big)$$
$$\boxed{\textbf{(5) ✓修正后的结论}:\ c+d\le12+16=28\Longrightarrow\boxed{|A_0|\ge33\Longrightarrow\ \#\{x\in A_0:d(x,A_1)\ge4\}\ \ge\ 33-28=\mathbf5}\ ✓✓\ \big(\text{非 13 ✗}\big)}$$
$$\qquad\textbf{（诚实 ✓）}:\ \text{仍\ \textbf{优于"396 容得下"之无结构论证} ✓（把 }33\ \text{点逼出 }R\ \text{之次层 ✓），但强度弱于唐先生所期 ✓}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓（除标签 ✗）}:\ \text{prefix-distance profile }(r,r{+}2,r{+}2,r{+}2)\ \text{与}\ (r{+}1,r{+}1,r{+}1,r{+}3)\ ✓✓;$$
$$\qquad\textbf{但标签与 C-450 冲突 ✗✗}:\ \text{唐先生此轮令 }P=\{100,010,001,111\}\ \text{（\textbf{奇部}）}\ ✗;\ \text{C-450 之约定为 }P=\text{偶部（}\{0,e_i{\oplus}e_j,\dots\}\text{）}✓,\ A_1=\text{奇部}✓$$
$$\qquad\Longrightarrow\ \textbf{纪律 ✓✓}:\ \text{凡用 }P/A_1\ \text{须\ \textbf{逐次显式声明奇／偶}}✓\ \big(\text{同 C-450 之 supp 纪律 ✓}\big)$$
$$\textbf{§2 ✓✓（+1 遗漏行）}:\ \text{14 行全对 ✓✓};\ \text{唯漏}(1,1,1,3)\ (4\ \text{点},\ \text{即偶部}\ P✓);\ \text{其"}+4\text{"之 4 即此 4 点（非 }A_1✗\big)✓$$
$$\textbf{§3 ✓✓}:\ K_{4,4}-M\ \text{穷举确认 ✓✓};\ \text{"3 个 }E_2\text{-邻"（每 }E_1\text{-点）✓✓}$$
$$\textbf{§4 ✓✓}:\ 72=72\ \text{双计数 ✓✓};\ \text{"24＝六个 }D_2\text{ 对之三重碰撞层"}\ ✓✓$$
$$\textbf{§5 ✓}:\ A_0\subseteq R✓;\ C,D\ \text{之定义 ✓};\ \text{"唯二与 }N_2\ \text{一步邻接之层"}\ ✓✓\ \big((3,3,3,5)\ \text{与}\ (3,5,5,5)\ \text{确实分别邻 }E_2,E_1✓\big)$$
$$\textbf{§6 ✓✓}:\ c\le12\ \text{正确 ✓✓（穷举支持：每 }(3,3,3,5)\text{-点恰 2 个 }E_2\text{-邻 ✓）}$$
$$\textbf{§7 ✗✗}:\ \text{"一个 }E_1\text{ 点至多服务一个 }D\text{ 点"}\ ✗;\ \text{正确为\ \textbf{至多 2}}✓✓\ \big(\text{见 §0(4) ✓}\big);\ \text{故}\ d\le16\ \text{而非 }8✗$$
$$\textbf{§8 ✗}:\ c+d\le20\ ✗\to 28✓;\ \ge13\ \text{个高层点}\ ✗\to\ \ge5✓$$
$$\textbf{§9 ✓（方向 ✓）}:\ \text{统一 incidence packing lemma\ \textbf{是好提法} ✓✓（本档即为其特例 ✓）};\ \text{但须先修 §7 ✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 14 行 profile 分解（含偶部行 ✓）✓✓✓};\ \text{② }K_{4,4}{-}M\ \text{结构与 }72=72✓✓;\ \text{③ }c\le12✓✓;\ \text{④ }\boxed{d\le16}✓✓;\ \text{⑤ }|A_0|\ge33\Rightarrow\ge5\ \text{点落 }d\ge4✓$$
$$\textbf{已否证 ✗✓}:\ \text{"共 }y\ \text{之 }D\text{-点距离恰 2"}\ ✗;\ "d\le8"\ ✗;\ "c+d\le20"\ ✗;\ "\ge13"\ ✗;\ \text{label 混用（}P=\text{奇部}\big)\ ✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{之全局可行性};\ \text{（}c,d\ \text{之联合 packing 仍未出矛盾 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 统一 incidence packing：对每层算"每点可服务数"×层大小，反推 }A_0\ \text{之容量 ✓✓（本档已示范两层 ✓）};\ \text{② 继续压 }4^3 6^1\ (80✓)\ \text{与 }4^1 6^3\ (60✓)\ \text{之 }\le k\ \text{per point 界 ✓};\ \text{③ 与 }D_2=6\ \text{之 }72\ \text{计数联立 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "profile 分层" "服务数" "碰撞层"
技术词 profile 分层 命中文件数=1    :: ./WITLAYER-2026-09-28-R-profile-decomposition-and-the-d-le-16-correction.md
技术词 服务数       命中文件数=1    :: ./WITLAYER-2026-09-28-R-profile-decomposition-and-the-d-le-16-correction.md
技术词 碰撞层       命中文件数=25   :: ./C3899h-T1-closure-and-gamma13-M1-seven-wall-screening.md ./C368-erratum-and-audit-response-double-collision-emptiness-justified-by-two-steps.md …
```
| 词 | 本线他档命中 | 跨空间／属线未定（**不计** ✗） | 本档自击 | 本档新增 |
|---|---|---|---|---|
| profile 分层 | 0 | 0 | 1 | ✓（自造标签 ✓） |
| 服务数 | 0 | 0 | 1 | ✓（自造标签 ✓） |
| 碰撞层 | 0 | **25**（既有 ⟹ **不计** ✗） | 0 | ✗（**非新增** ✓） |

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅 512 点有限穷举核对 ✓ —— 用于验证 profile 表、$K_{4,4}{-}M$、$c\le12$ 之"每点 2 邻"、$D$-层服务数分布 ✓）
- **未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（$d\le8\to d\le16$）已在 §0(4) 显式标注 ✓✓；**标签纪律**（$P$ 奇/偶须声明）已在 §1 标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $3^4$ 已排除 ✗（V290）
