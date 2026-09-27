# P1-COV-2026-09-27 — **状态锁** ＋ **球面恒等式族（新，已核验）** ＋ 诚实判定：仍非新全局约束

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查已按空间分栏** ✓（照唐先生 23:12 令 ✓）。
> **范围（照唐先生 23:15 令 ✓）**：① 锁定 C-416／C-415 状态；② 试做 **covering-specific** 一步；零程序计算 ✓。

**已查地图：命中（接续 P1-D4b／P1-D4／P1-G2，非新案 ✓）**
`docs/P1-D4b-2026-09-27-…`（**P1-D4b ＝ YES／显式反例 $C_0$** ✓✓）｜`docs/P1-G2-2026-09-27-…`（**见证者分解／逃逸口** ✓✓）｜`docs/P1-D4-2026-09-27-…`（**球面覆盖恒等式 $k=3$／两类来源排除** ✓✓）｜`docs/P1-AVOID-2026-09-27-…`（**占用恒等式** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，**两空间皆 0**，见 §6）
D0: 本档对象 ＝ **档案已有** 球面覆盖对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 k=1..10 的球面恒等式族 ＋ 四例核验 ＋ "超额被度数完全决定"的判定** ✓）
**[RESEARCH]**

---

## §0 结论（**状态锁 ✓｜恒等式族 ✓✓｜诚实判定 ✗⚠️**）

$$\boxed{\textbf{(0) 状态锁（照唐先生 23:15 ✓）}:\ \textbf{C-415 LIVE};\ \text{原局部 P1 已\textbf{达自然极限}}✓;\ \text{下一步\textbf{必须换成 covering-specific 全局机制}✓}}$$
$$\qquad\textbf{（C-416 关闭的只是）}:\ \text{"用 avoidance 禁掉内部 weight-4"的\textbf{局部机制}}✓\ \textbf{—— 不是}关闭 119 本身 ✗,\ \textbf{不是}证明内部 weight-4 在 119-cover 中存在 ✗✓$$
$$\boxed{\textbf{(1) ★球面恒等式族（新，已核验 ✓✓）}:\ k=1,\dots,10:\ \boxed{(11-k)\,d_{k-1}(c)+d_k(c)+(k+1)\,d_{k+1}(c)=\binom{10}k+E_k(c)}\ ✓✓}$$
$$\qquad\big(E_k(c):=\sum_{x\in S_k(c)}\big(b(x)-1\big)\ge0✓;\ d_{11}\equiv0✓\big)$$
$$\boxed{\textbf{(2) 四例核验（}\mathbb F_2^{10}\ \text{满空间 sanity ✓✓）}:\ k=1{:}\ E_1=d_1+2d_2✓;\ k=2{:}\ 9d_1+d_2+3d_3=45+E_2✓;\ k=3{:}\ 8d_2+d_3+4d_4=120+E_3✓;\ k=4{:}\ 7d_3+d_4+5d_5=210+E_4✓}$$
$$\boxed{\textbf{(3) ✗ 诚实判定}:\ \text{该族把 }\{E_k(c)\}\ \textbf{完全决定}于局部度数}\ (d_j(c))\ \Longrightarrow\ \textbf{"球面超额"不携带超出度数的信息}✗\ \big(\text{与 C-409 同主题 ✓}\big)}$$
$$\boxed{\textbf{(4) ⚠️ 全局形式}:\ k=1\ \text{求和} \Longrightarrow 2N_1+4N_2=\sum_x\big(b(x)-1\big)d_1(x)\ ✓\ \text{—— 仍属 profile 级}✗;\ \textbf{未产生新全局约束}⚠️}$$

---

## §1 **恒等式族的推导**（**逐 $k$ 系数 ✓**）

$$\text{固定 }c\in C;\ \text{取球面 }S_k(c)=\{c\oplus u:|u|=k\}\ (\text{共 }\binom{10}k\ \text{点}✓);\ \text{对 }x\in S_k(c)\ \text{与 }w=c\oplus v\in C:\ d(x,w)=|u\oplus v|\le1✓$$
$$\text{奇偶性 ✓}:\ |u\oplus v|\equiv k+j\ (\mathrm{mod}\ 2)\ \big(j:=|v|✓\big) \Longrightarrow\ |u\oplus v|\le1\ \text{仅当}\ \begin{cases}k+j\ \text{奇}\ \Rightarrow\ =1✓\\ k=j\ \Rightarrow\ =0✓\end{cases};\ \text{其余}\ |u\oplus v|\ge2\ ✗✓$$
$$\Longrightarrow\ \text{仅 }j\in\{k-1,k,k+1\}\ \text{可贡献}✓;\ \text{系数 ✓}:\quad j=k-1:\ \#\{u:|u|=k,\ v\subset u\}=10-j=11-k✓;\quad j=k:\ \#\{u:u=v\}=1✓;\quad j=k+1:\ \#\{u:u\subset v\}=\binom{k+1}k=k+1✓$$
$$\text{两侧计数 ✓}:\ \sum_{x\in S_k(c)}b(x)=(11-k)d_{k-1}(c)+d_k(c)+(k+1)d_{k+1}(c)✓;\qquad \sum_{x\in S_k(c)}b(x)=\binom{10}k+E_k(c)✓ \Longrightarrow\ \textbf{§0 (1) 得证}✓✓$$

## §2 **核验**（**四例 ＋ 满空间 sanity ✓✓**）

$$\textbf{逐例 ✓}:\ k=1{:}\ 10d_0+d_1+2d_2=10+E_1\ \big(d_0=1✓\big)\Longrightarrow\ E_1(c)=d_1(c)+2d_2(c)✓✓$$
$$\qquad k=2{:}\ 9d_1+d_2+3d_3=45+E_2✓;\qquad k=3{:}\ 8d_2+d_3+4d_4=120+E_3✓\ \big(\text{＝P1-D4 §1 ✓}\big);\qquad k=4{:}\ 7d_3+d_4+5d_5=210+E_4✓$$
$$\textbf{满空间 sanity（}C=\mathbb F_2^{10},\ b\equiv11\Longrightarrow E_k=\binom{10}k\cdot10✓\big)}$$
$$\qquad k=1{:}\ 10+10+90=110=10+100✓\quad k=2{:}\ 90+45+360=495=45+450✓\quad k=3{:}\ 360+120+840=1320=120+1200✓\quad k=4{:}\ 840+210+1260=2310=210+2100✓$$
$$\qquad\Longrightarrow\ \textbf{四例两侧全等}✓✓\ \text{（其中 }k=1\ \text{为\textbf{精确恒等式}（无自由度 ✓）；}k\ge2\ \text{含 }E_k\ \text{项 ✓）}$$

## §3 **全局形式**（**⚠️**）

$$\sum_{c\in C}\big[(11-k)d_{k-1}+d_k+(k+1)d_{k+1}\big]=(11-k)\cdot2N_{k-1}+2N_k+(k+1)\cdot2N_{k+1}✓;\qquad \sum_{c\in C}\binom{10}k=119\binom{10}k✓$$
$$\sum_{c\in C}E_k(c)=\sum_{x}\big(b(x)-1\big)\cdot\#\{c\in C:d(x,c)=k\}=\sum_x\big(b(x)-1\big)d_k(x)✓$$
$$\Longrightarrow\ \boxed{2(11-k)N_{k-1}+2N_k+2(k+1)N_{k+1}=119\binom{10}k+\sum_x\big(b(x)-1\big)d_k(x)}\ ✓\ \big(k=1:\ 2N_1+4N_2+4N_0\ \text{项为 }0✓\big)$$
$$\qquad\Longrightarrow\ k=1:\ \boxed{2N_1+4N_2=\sum_x\big(b(x)-1\big)d_1(x)}\ ✓\ \big(\text{满空间核验：}10240+92160=102400=1024\cdot100✓✓\big)$$

## §4 **诚实判定**（**为何大概率不足 ✗⚠️**）

$$\textbf{① 该族是"超额} \leftrightarrow \text{度数"的\textbf{完备线性关系}✓}:\ \{E_k(c)\}_{k=1}^{10}\ \text{由 }\{d_j(c)\}_j\ \textbf{唯一决定}✓ \Longrightarrow\ \text{"超额"无独立自由度 ✗✓}$$
$$\qquad\Longrightarrow\ \text{因此\textbf{不能}用"超额} \ge0\text{"再榨出新约束（那只是重述度数关系 ✓）—— 与 C-409 的"占用预算与 }\{n_j\}\ \text{同源"✓\textbf{同一主题}✓✓}$$
$$\textbf{② 全局形式亦为 profile 级 ✗}:\ \S3\ \text{的 }k\ \text{型恒等式左侧是 }A\text{-data（}N_j✓\text{）、右侧含 }b(x)\ \text{与 }d_k(x)\ \text{的联合分布 ✓} \Longrightarrow\ \text{不构成独立 handle}✗✓$$
$$\textbf{③ 方向 ✗}:\ E_k\ge0\ \text{只给\textbf{下界}（与 P1-D4 §2 同 ✗）};\ \text{而 }d_k\ \text{的\textbf{上界}仍须外部来源}⚠️$$
$$\Longrightarrow\ \boxed{\text{本族是\textbf{新的、已验证的} covering-specific 结构 ✓，但\textbf{未产生新全局约束}✗⚠️\ —— 诚实落判 ✓}$$

## §5 状态锁与下一步（**诚实 ✓**）

$$\textbf{状态锁 ✓}:\ \text{① C-415 \textbf{LIVE}✓};\ \text{② 局部 avoidance 路线\textbf{自然极限已确认}✓};\ \text{③ C-416 只关闭\textbf{局部机制}（用 avoidance 禁内部 weight-4 ✓），\textbf{不}关闭 119 ✗，\textbf{不}证明该结构在真 119-cover 中存在 ✗✓};\ \text{④ 标签纪律：空间 A／B 严格分栏 ✓（已固化 ✓）}$$
$$\textbf{下一步（照唐先生 ✓）}:\ \text{必须用 \textbf{covering-specific information}；单纯 avoidance／}A\text{-profile／球面容量／局部 }K_4\ \text{已反复证明不足 ✗}$$
$$\textbf{（本档的净贡献 ✓）}:\ \text{把"球面超额"这一整类\textbf{显式判定为度数决定}✗ ⟹ \text{下一步搜索空间进一步压缩};\ \text{须找的量\textbf{不得}由 }\{d_j(c)\}\ \text{或 }\{N_j\}\ \text{决定}✓✓$$

## §6 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "球面恒等式族" "度数耦合" "球面超额"
技术词 球面恒等式族 命中文件数=2    :: ./P1-COV-2026-09-27-sphere-identity-family-and-degree-determination-verdict.md ./ASSETS-REGISTRY.md 
技术词 度数耦合     命中文件数=1    :: ./P1-COV-2026-09-27-sphere-identity-family-and-degree-determination-verdict.md 
技术词 球面超额     命中文件数=2    :: ./P1-COV-2026-09-27-sphere-identity-family-and-degree-determination-verdict.md ./ASSETS-REGISTRY.md 
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 球面恒等式族 | 2（**本档自身** ＋ `ASSETS-REGISTRY.md` ✓） | 0 | 0（本档自造标签 ✓） |
| 度数耦合 | 1（**本档自身** ✓） | 0 | 0（本档自造标签 ✓） |
| 球面超额 | 2（**本档自身** ＋ `ASSETS-REGISTRY.md` ✓） | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词的**本线命中均为本档自身 ＋ 注册表** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；**跨空间同名 0** ✓）
- **注 ✓**：本档实质＝**§1 恒等式族 ＋ §2 四例核验 ＋ §4 度数决定判定**（推导性 ✓）；**写入前**该三词在两空间皆 0 ✓，**写入后**命中仅本档 ＋ 注册表 ✓（符合"先跑后写"机械门 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§6 已分栏 ✓）
- **不声称** P1 成立 ✗（V290）；**不声称** 该族无用 ✗ —— 只写"**已验证 ✓ 但未产生新全局约束**" ✓
- **不声称** 119-cover 中存在内部 weight-4 ✗（$C_0$ 非覆盖码 ✓，照唐先生 23:15 分区 ✓）
- §2 的**满空间 sanity 必留** ✓（该族正确性的直接证据 ✓）
