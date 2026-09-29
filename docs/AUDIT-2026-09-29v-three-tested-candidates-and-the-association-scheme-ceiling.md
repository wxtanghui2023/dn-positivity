# AUDIT-2026-09-29v — **三项候选\ \textbf{已测}（按"先测再定"纪律）；常数纠错；以及\ \textbf{结合方案层的天花板}**

> **性质**：**实测判定 ＋ 纠错 ＋ 结构性结论**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:3x ✓
> **唐先生令**：「先提出一个可检验的二层局部命题 → 实测 → 通过才证明」✓

**已查地图**：`AUDIT-29u`（$(1)$ 之重复否证）／`29t`（Zhang 机制）／`29m`（全局计数可行域非空）✓

D0: 本档对象 ＝ **档案已有**（$d_1,d_2,q,m(y)$／2-面——无新数学对象 ✓）
D1: 0（产出＝**一处常数纠错 ＋ 三命题判定 ＋ 一层天花板之定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 常数纠错}:\ N_{\ge1}^{(m)}=d_1(10-d_1)+\tbinom{d_1}2=\frac{d_1(19-d_1)}2\ (\textbf{非}\ 21)\ ✓\text{实测全码字成立}}$$
$$\boxed{\text{② ✗ }(B)\ \text{亦假}:\ d_2\le\tfrac{d_1(19-d_1)}2\ \text{\textbf{仍} 49/120 违例（}d_1{=}0\Rightarrow 0\text{）}✓\ \text{你已自认}}$$
$$\boxed{\text{③ ✓ P1\ \textbf{真}（且可解释）}:\ q(c)=\#\{y\in S_2(c)\cap C:m(y)=2\}=\text{过 }c\ \text{之\textbf{满 2-面}数}}$$
$$\boxed{\text{④ ✓ P2\ \textbf{真但极松}:\ }E_2\ge 2F=Q/2\ (\text{120-code}:\ 149\ge2,\ \text{松 }147)✗}$$
$$\boxed{\text{⑤ ✓ P3\ \textbf{真但为同一性}:\ }\sum_{y\in S_2(c)\cap C}m(y)=\sum_{p\in S_1(c)\cap C}(d_1(p)-1),\ \text{两端同数 }\ G_1\ \text{之 2-路径}}$$

## §1 ① 常数纠错（**✓✓ 实测**）

$$\text{你写}:\ N_{\ge1}=d_1(10-d_1)+\tbinom{d_1}2=d_1(21-d_1)/2$$
$$\text{展开}:\ 10d_1-d_1^2+\frac{d_1^2-d_1}2=\frac{20d_1-2d_1^2+d_1^2-d_1}2=\frac{19d_1-d_1^2}2=\boxed{\frac{d_1(19-d_1)}2}$$
$$\text{实测（120 个码字全部）}:\ N_{\ge1}{=}\frac{d_1(19-d_1)}2\ ✓,\ \#\{m{=}2\}{=}\tbinom{d_1}2\ ✓,\ N_0{=}45-N_{\ge1}\ ✓$$
$$\text{（校验 }d_1{=}10:\ N_{\ge1}{=}45\Rightarrow N_0{=}0\ ✓;\ d_1{=}9:\ N_{\ge1}{=}45\Rightarrow N_0{=}0,\ N_2{=}36\ ✓）$$

## §2 ② $(B)$ 之否证（**✗ 双常数皆违例 49/120**）

$$d_2\le\frac{d_1(21-d_1)}2:\ \textbf{49/120}\ ✗;\qquad d_2\le\frac{d_1(19-d_1)}2:\ \textbf{49/120}\ ✗$$
$$\text{结构原因}:\ d_1{=}0\Rightarrow\ \text{右端}=0,\ \text{而 }d_2>0\ \text{常见}\ ⟹\ \text{该型界\ \textbf{方向即错}}✗$$
$$\therefore\ \text{你是对的：应\ \textbf{立即停掉}该链，不再修补}✓$$

## §3 ③④⑤ 三命题之实测判定（**按你的纪律**）

$$\textbf{P1:\ }q(c)=\#\{y\in S_2(c)\cap C:m(y)=2\}\ \textbf{真}✓\ \text{（几何义：过 }c\ \text{的满 2-面数）}$$
$$\text{（因 }q(c)\ \text{数}\ \{i,j\}\subseteq S(c)\ \text{使 }c\oplus e_i\oplus e_j\in C;\ \text{此点之两中点 }c\oplus e_i,c\oplus e_j\ \text{皆在 }C\Rightarrow m{=}2\ ✓）$$
$$\therefore\ \text{120-code 之}\ Q=\sum_c q(c)=\mathbf{4}\ \Longrightarrow\ \text{满 2-面数}\ F=Q/4=\mathbf{1}\ (\text{全码\ \textbf{仅一个满 2-面}})$$
$$\textbf{P2:\ }E_2\ge2F=Q/2:\ \textbf{真}✓\ \text{（每满面贡献 2 条对角距离-2 对，且对角对唯一确定该面）}\ \text{但}\ 149\ge2:\ \textbf{松 }147✗$$
$$\textbf{P3:\ }\sum_{y\in S_2(c)\cap C}m(y)=\sum_{p\in S_1(c)\cap C}(d_1(p)-1):\ \textbf{真}✓$$
$$\text{但两端皆数}\ G_1\ \text{中有序 2-路径（}c\!\to\!p\!\to\!y,\ d(c,y){=}2\ \text{自动）}\Longrightarrow\ \textbf{同一性，非约束}✗$$

## §4 ★ 结构性结论（**本会话最重要的定位之一 ✓✓**）

$$\text{上述全部量（}d_1,d_2,q,m,F,E_1,E_2\ \text{之任意线性组合、2-路径数、三角形数等）}$$
$$\textbf{皆由距离分布决定}\ \Longrightarrow\ \text{属\ \textbf{结合方案（association scheme）层}}$$
$$\therefore\ \boxed{\text{结合方案层\ \textbf{已被 Delsarte 完整覆盖}}（29m 已验证：Delsarte 对 }M{=}106\ \text{可行）⟹\ \text{层内再多恒等式亦无增益}}✗$$
$$\text{而 Zhang 之覆盖设计界\ \textbf{不是}\ 结合方案型（它是\ integrality／设计存在性）}\ \Longrightarrow\ \text{这才是唯一出过 }105\ \text{的非谱机制}✓$$
$$\therefore\ \boxed{\text{欲 }107:\ \text{须一个\ \textbf{非距离分布函数}之量};\ \text{层内（结合方案／2-路径／面）已耗尽}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "常数19非21" "满2面" "同义反复"
技术词 常数19非21  命中文件数=0    ::
技术词 满2面     命中文件数=0    ::
技术词 同义反复    命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **120-code 全量实测（三命题逐条判定）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；含**一处常数纠错**与**一处你之自认**之记录 ✓
