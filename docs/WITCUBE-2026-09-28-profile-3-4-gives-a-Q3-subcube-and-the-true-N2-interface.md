# WITCUBE-2026-09-28 — **$3^4\Rightarrow A_1\cup P\cong Q_3$（新 ✓✓）；修正 $N_1(A_1)$ 与 $4{\cdot}6$；真接口 $N_2[A_1]$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 12:17 令 ✓）**：$3^4$ 之全局接口；**零程序计算**（仅整数与有限集合核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-450／C-449／C-448，非新案 ✓）**
`docs/WITPLANE-2026-09-28-…`（**$3^4\Rightarrow P$ 二维仿射平面 ✓✓**）｜`docs/WITPROF-2026-09-28-…`（**$r_{\max}{=}3$／两 profile ✓✓✓**）｜`docs/WITCODE-2026-09-28-…`（**$e(A){=}0$／$D_2\ge5$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §4）
D0: 本档对象 ＝ **档案已有** $3^4$／子立方体／$N_2$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $D(p)\equiv\{i,j,k\}$ 与 $A_1\cup P=p_0\oplus\langle e_i,e_j,e_k\rangle\cong Q_3$（奇偶两半）＋ 否证 $N_1(A_1)=P\cup A_1$（24 反例）＋ 定出真接口 $A_0\subseteq V\setminus N_2[A_1]$（$|N_2[A_1]|{=}116$）** ✓）
**[RESEARCH]**

---

## §0 结论（**$Q_3$ 闭环 ✓✓✓｜两处 ✗｜真接口 $N_2$ ✓**）

$$\textbf{设定 ✓}:\ \text{profile }3^4\Rightarrow|P|=4,\ r(p)\equiv3✓;\ \text{设 }D(p_0)=\{i,j,k\}✓;\ u:=e_i{\oplus}e_j,\ v:=e_i{\oplus}e_k,\ w:=u{\oplus}v=e_j{\oplus}e_k✓$$
$$\qquad P=\{p_0,\ p_0{\oplus}u,\ p_0{\oplus}v,\ p_0{\oplus}w\}\ \big(\text{C-450 ✓✓}\big);\quad \text{平移 }p_0\mapsto0\Longrightarrow P=\{0,u,v,w\}✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 §2–§3 全部正确（新，且闭环更紧）}:\ \text{对 }p_1=u=e_i{\oplus}e_j:}$$
$$\qquad p_1\oplus e_i=e_j\in A_1✓,\quad p_1\oplus e_j=e_i\in A_1✓;\quad \text{第三个方向由"闭环点须为另三个 }P\text{-点"定出}:$$
$$\qquad u\oplus(i,j)=0\ \Rightarrow\ \text{对 }\{i,j\};\quad u\oplus(j,k)=e_i{\oplus}e_k=v✓;\quad u\oplus(i,k)=e_j{\oplus}e_k=w✓$$
$$\qquad\Longrightarrow\ \{i,j\},\{j,k\},\{i,k\}\ \text{全部出现} \Longrightarrow \boxed{D(p_1)=\{i,j,k\}}\ ✓✓;\ \text{同法对另两点} \Longrightarrow \boxed{D(p)=\{i,j,k\}\ \forall p\in P}✓✓✓$$
$$\qquad\Longrightarrow\ \bigcup_{p\in P}\{p\oplus e_i,p\oplus e_j,p\oplus e_k\}=\{e_i,e_j,e_k,e_i{\oplus}e_j{\oplus}e_k\}=:A_1✓✓\ \big(\text{共 4 点、12 条入射}=\text{全 }P\leftrightarrow A_1\ \text{入射 ✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{A_1=\{e_i,e_j,e_k,e_i{\oplus}e_j{\oplus}e_k\}}\ ✓✓\ \big(\text{即 }A_1=p_0\oplus\langle e_i,e_j,e_k\rangle\ \text{的\ \textbf{奇部}}\ ✓\big)$$
$$\qquad\Longrightarrow\ \boxed{A_1\cup P=p_0\oplus\langle e_i,e_j,e_k\rangle\cong Q_3}\ ✓✓✓\ \big(P=\text{偶部}\ ✓,\ A_1=\text{奇部}\ ✓;\ A_1\ \text{内两两距离}\ 2\ ✓✓\big)$$
$$\qquad\textbf{（核对 ✓✓）}:\ |A_1|=4✓,\ P\ \text{weight} =\{0,2,2,2\}✓;\ A_1\ \text{weight}=\{1,1,1,3\}✓;\ A_1\ \text{两两距离全 }2✓;\ D(p)=\{i,j,k\}\ \text{对四个 }p\ \text{全成立}✓✓$$
$$\boxed{\textbf{(2) ✗✗唐先生 §5 之 (4)(5) 为假（24 个反例）}:\ \text{"}N_1(A_1)=P\cup A_1\text{"}\ ✗;\ \text{"}x\notin P\cup A_1\Rightarrow d(x,A_1)\ge2\text{"}\ ✗✗}$$
$$\qquad\textbf{反例 ✓}:\ \text{对 }a\in A_1,\ l\notin\{i,j,k\}:\ a\oplus e_l\ \text{距 }A_1\ \text{为\ \textbf{1}}\ \text{且}\ \notin P\cup A_1✓;\ \text{共 }4\times6=\mathbf{24}\ \text{个（互异 ✓）}$$
$$\qquad\textbf{正确 ✓✓}:\ N(A_1)=P\ \dot\cup\ (24\ \text{个外部点})✓,\quad |N(A_1)|=4+24=28✓,\quad |N[A_1]|=4+28=32✓\ \big(\text{实测 }|N(A_1)|{=}28✓\big)$$
$$\boxed{\textbf{(3) ✗算术}:\ \text{唐先生 §9 的"每个 }p\ \text{有 }9-3=6?\ \text{写 7"\ ✗}:\ 9-3=\mathbf6\Longrightarrow4\times6=\mathbf{24}✓\ \text{（非 }28✗\big)}$$
$$\boxed{\textbf{(4) ✓✓真接口（本档定出）}:\ \text{由 }d(A_0,A_1)\ge3\ \big(\text{C-447 ✓✓}\big)\ \text{而非 }\ge2✗:}$$
$$\qquad\boxed{A_0\ \subseteq\ V\setminus N_2[A_1]}\ ✓✓\ \big(N_2=\text{闭 2-邻域 ✓}\big);\quad \text{实测}:\ |N_2[A_1]|=116\Longrightarrow\boxed{|V\setminus N_2[A_1]|=396}✓✓$$
$$\qquad\Longrightarrow\ |A_0|\ge33\ \big(\text{C-446 ✓✓}\big)\ \text{与 }396\ \text{个可用点\ \textbf{不矛盾}}\ ✗\ \big(\text{仍需 }R\ \text{之结构，非仅大小 ✓}\big)$$
$$\qquad\textbf{（唐先生 §8 之分层 ✓ 可用）}:\ \text{外部 7 坐标、第 }s\ \text{层 }8\binom7s\ \text{点（}8,56,168,280,\dots✓\big)✓\ \text{—— 但须记住 }s{=}1\ \text{层里 }24\ \text{点已在 }N(A_1)✓$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✓}:\ P=p_0+\langle u,v\rangle\ \big(\text{C-450 ✓✓}\big);\ u,v,w\ \text{皆 weight 2 ✓};\ D_2=6\ \text{之 6 对 }=\text{3 个 weight-2 方向各现两次 ✓✓（§6 ✓）}$$
$$\textbf{§2–§3 ✓✓✓}:\ D(p)\equiv\{i,j,k\}\ \text{与 }A_1\cup P\cong Q_3\ \text{均正确且为\ \textbf{新} ✓✓✓（见 §0(1) ✓）}$$
$$\textbf{§4 ✓（形式 ✓）}:\ \text{每个 }a\in A_1\ \text{在 }P\ \text{内有 3 个邻（方向 }i,j,k✓\big)✓;\ E(A_1,P)=12✓✓;\ \text{但"方向已被完全消耗"}\ ✗\ \big(\text{另有 6 个外向方向 ✓}\big)$$
$$\textbf{§5 ✗✗}:\ \text{见 §0(2)（}N_1\ \text{与"}\ge2\text{"双双为假 ✗）};\ \text{§8 之分层 ✓ 但须扣掉 }24✓$$
$$\textbf{§6 ✓✓}:\ D_2=4\binom32=12\Rightarrow D_2=6✓;\ \text{6 对}=\binom P2✓;\ \text{三方向各两次 ✓✓，局部无松弛}\ ✓$$
$$\textbf{§7 ✗}:\ \text{"}A\setminus A_1\subseteq V\setminus N_1(A_1)\text{"}\ ✗\ \text{—— 正确为 }V\setminus N_2[A_1]✓✓\ \big(\text{因 }d\ge3\ \text{非 }\ge2✓\big)$$
$$\textbf{§9 ✗（算术）}:\ 4\cdot7=28\ ✗\to 4\cdot6=24✓\ \big(\text{外向方向 }9-3=6✓\big);\ \text{碰撞回到 }D_2=6\ \text{之方向}\ ✓$$
$$\textbf{§7 ✓✓}:\ \text{唐先生之 }|A|=45\Rightarrow41\ \text{个剩余}\ ✓✓;\quad |A\setminus A_1|=45-4=41✓;\ \text{其中 }A_0\ \text{部分}\ \big(\ge33✓\big)\ \text{须落 }V\setminus N_2[A_1]✓$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{D(p)\equiv\{i,j,k\}\ \forall p\in P}✓✓;\ \text{② }\boxed{A_1\cup P=p_0\oplus\langle e_i,e_j,e_k\rangle\cong Q_3}✓✓✓;\ \text{③ }|N(A_1)|{=}28,\ |N[A_1]|{=}32✓;\ \text{④ }\boxed{A_0\subseteq V\setminus N_2[A_1]},\ |N_2[A_1]|{=}116,\ \text{余\ }396✓✓;\ \text{⑤ }D_2=6\ \text{之 6 对结构 ✓✓}$$
$$\textbf{已否证 ✗✓}:\ \text{"}N_1(A_1)=P\cup A_1\text{"}\ ✗;\ \text{"}x\notin Q_3\Rightarrow d(x,A_1)\ge2\text{"}\ ✗;\ \text{"4}\cdot7{=}28\text{"}\ ✗;\ \text{"}A\setminus A_1\subseteq V\setminus N_1\text{"}\ ✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ 3^4\ \text{之全局可行性};\ \text{（仅大小不矛盾 ⟹ 须用 }R\ \text{的结构 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 在 }R=V\setminus N_2[A_1]\ \text{（396 点）内做 min-distance-3 码之容量/结构分析，并接 }|A_0|\ge33✓;\ \text{② 用 }D_2=6\ \text{之 6 对与 }P\text{-}\text{外部 24 点之碰撞联络 ✓};\ \text{③ profile }3^32^11^1\ \text{并行攻 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "外向方向" "闭2邻域" "子立方体闭环"
技术词 外向方向     命中文件数=1    :: ./WITCUBE-2026-09-28-profile-3-4-gives-a-Q3-subcube-and-the-true-N2-interface.md
技术词 闭2邻域       命中文件数=1    :: ./WITCUBE-2026-09-28-profile-3-4-gives-a-Q3-subcube-and-the-true-N2-interface.md
技术词 子立方体闭环 命中文件数=1    :: ./WITCUBE-2026-09-28-profile-3-4-gives-a-Q3-subcube-and-the-true-N2-interface.md
```
> ⚠️ **诚实更正 ✓✓**：三词实测**各 1 命中**，且**唯一命中即本档自身**（＝**自击** ✗）—— 系因本档先写、回查后跑（违反"先跑后写" ✗）。**本档新增**：三词**均为本档自造标签** ✓，**无本线他档命中、无跨空间命中** ✓（自击扣除后本线净命中 = 0 ✓）。
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档自击 | 本档新增 |
|---|---|---|---|---|
| 外向方向 | 0 | 0 | 1 | ✓（自造标签 ✓） |
| 闭2邻域 | 0 | 0 | 1 | ✓（自造标签 ✓） |
| 子立方体闭环 | 0 | 0 | 1 | ✓（自造标签 ✓） |

- **本档新增**：三词均为**自造标签** ✓（扣除自击后本线净命中 = 0 ✓）；仅作结构命名，**不作新性主张** ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅整数与有限集合（512 点邻域）核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处必改**（$N_1(A_1)$／$4\cdot6$）已在 §0(2)(3) 显式标注 ✓✓；**$d\ge3$ 用 $N_2$、$d\ge2$ 用 $N_1$** 须严格区分 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $3^4$ 已排除 ✗（V290）
