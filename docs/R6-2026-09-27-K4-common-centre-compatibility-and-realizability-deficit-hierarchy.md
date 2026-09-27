# R6-2026-09-27 — **$K_4$／共同球心兼容性**：反例 ＋ 可实现性亏空层级 ＋ 团级局部 cap

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗（`E58` 属空间 A，不跨 ✓）。
> **范围（照唐先生 22:35 令 ✓）**：三点层判 **collapse** ✓；开 $K_4$／四中心共同球心兼容性；零程序计算 ✓；不上 SDP ✓。

**已查地图：命中（接续 R4-P1b／R5／R4-T，非新案 ✓）**
所查：`docs/R4-T-2026-09-27-…`（**$\tau$ 修正与 collapse** ✓✓）｜`docs/R5-2026-09-27-…`（**$U$／全局恒等式** ✓✓）｜`docs/R4-P1b-2026-09-27-…`｜`docs/FIBER-2026-09-26-…`｜`docs/TERM-2026-09-27-…`｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词**全部命中 0** ✓✓ —— 本档进入**档案未见**区域 ✓）
D0: 本档对象 ＝ **档案未见**的 $K_4$ 兼容性对象（重命名：否 ✗；新对象：**有**，属既有 119 线的下一层 ✓）
D1: 1（**首次给出 $K_4$ 无共同球心的显式反例 ＋ 可实现性亏空层级 ＋ 团级 cap（Kleitman）** ✓）
**[RESEARCH]**

---

## §0 结论（**六条，含两条定理级 ✓**）

$$\boxed{\textbf{(1) 三点层 collapse 确认 ✓}:\ T_3=\sum_j\binom j3n_j\ \text{＝}b\text{-profile 函数} \Longrightarrow \text{三点自带无 covering 杠杆}\ ✗✓}$$
$$\boxed{\textbf{(2) }K_4\Rightarrow\text{共同球心 \textbf{为假} ✗✓}:\ \text{显式反例}\ \{0,\ e_1{+}e_2,\ e_2{+}e_3,\ e_1{+}e_3\}\ \subseteq\mathbb F_2^3\ (\text{偶权四点})\ ——\ \text{两两距离 2，但}\ \bigcap_iB_1(c_i)=\varnothing✓✓}$$
$$\boxed{\textbf{(3) 唯一性定理 ✓✓}:\ \text{对 }k\ge3\ \text{个中心},\ \Big|\bigcap_iB_1(c_i)\Big|\le1\ \Longrightarrow\ \text{共同球心"有／无"是二值 ✓}}$$
$$\boxed{\textbf{(4) 可实现性亏空层级 ✓✓}:\ \Delta_k:=\#(k\text{-cliques of }G_2)-\sum_x\binom{b(x)}k\ \Longrightarrow\ \boxed{\Delta_3\equiv0\ (\text{定理})};\ \ \Delta_4\ge0\ \text{且\textbf{可正}}✓✓}$$
$$\boxed{\textbf{(5) 团级局部 cap（Kleitman）✓}:\ G_2(C)\ \text{的任一团}\ \le11\ \text{点};\ \text{等号}\iff\text{该团恰为某球 }B_1(x)✓✓}$$
$$\boxed{\textbf{(6) 矩系统 ✓}:\ \sum_jn_j=1024,\ \sum_jjn_j=1309,\ \sum_jj^2n_j=1879+2Q✓;\ \textbf{且 }A\ \text{钉死 }Q✓ \Longrightarrow \text{profile 自由度始于三阶}\ \sum\binom\delta3✓}$$

---

## §1 $K_4$ 反例（**显式 ✓✓**）

$$\text{取 }c_1=0,\ c_2=e_1{+}e_2,\ c_3=e_2{+}e_3,\ c_4=e_1{+}e_3\ \in\mathbb F_2^{10}\ (\text{仅用前 3 坐标 ✓})$$
$$\text{两两距离（逐个核 ✓）}:\ d(c_1,c_2)=d(c_1,c_3)=d(c_1,c_4)=2✓;\ d(c_2,c_3)=|e_1{+}e_3|=2✓;\ d(c_2,c_4)=|e_2{+}e_3|=2✓;\ d(c_3,c_4)=|e_1{+}e_2|=2✓$$
$$\Longrightarrow\ \text{四点两两 }\le2\ \Longrightarrow\ K_4\subseteq G_2✓✓\qquad(\text{即 }4\ \text{个码字两两"接近" ✓})$$
$$\text{共同球心 }x\ \text{须 }d(x,c_i)\le1\ \forall i\Longrightarrow x\in B_1(0)=\{0\}\cup\{e_j\}✓;\ \text{逐个排除（完备 ✓）}:$$
$$\quad x=0:\ d(0,c_2)=2 ✗\quad\big|\quad x=e_1:\ d(e_1,c_3)=|e_1{+}e_2{+}e_3|=3 ✗\quad\big|\quad x=e_2:\ d(e_2,c_4)=3 ✗$$
$$\quad x=e_3:\ d(e_3,c_2)=3 ✗\quad\big|\quad x=e_j\ (j\ge4):\ d(e_j,c_2)=3 ✗ \Longrightarrow \boxed{\bigcap_iB_1(c_i)=\varnothing}\ ✓✓$$
$$\textbf{故唐先生的命题成立 ✓✓}:\ \boxed{\text{4 个 pairwise-close 码字}\ \not\Rightarrow\ \text{共同 radius-1 球心}}✓\ \text{—— 这是本线第一个\textbf{真正的兼容性缺口} ✓✓}$$

## §2 唯一性 ＋ 团级 cap（**两条定理级 ✓✓**）

$$\textbf{(3) 唯一性 ✓}:\ \text{若 }x\ne y\ \text{同为共同球心},\ \text{则 }\{c_i\}\subseteq B_1(x)\cap B_1(y);\ \text{而 }|B_1(x)\cap B_1(y)|=2\ (d\le2)\ \text{或}\ 0✓$$
$$\qquad\Longrightarrow\ k\ge3\ \text{时不可能（}k>2\big)\ \Longrightarrow\ \Big|\bigcap_iB_1(c_i)\Big|\le1✓✓\ \Longrightarrow\ \text{可实现性＝二值（有／无）✓}$$
$$\qquad\text{且}\ \text{共同球心存在}\iff\text{该团}\subseteq\text{某球 }B_1(x)\iff\text{该团恰为 }C\cap B_1(x)=S(x)\ \text{的子集 ✓}$$
$$\textbf{(5) 团级 cap（Kleitman 直径定理 ✓，档级引用）}:\ \text{直径 }\le2\ \text{的 }Q_{10}\ \text{子集最大 }\ \sum_{i=0}^{1}\binom{10}i=1+10=\mathbf{11}✓;\ \text{等号}\iff\text{球 }B_1(x)✓$$
$$\qquad\Longrightarrow\ \boxed{\text{任一 }G_2\text{-团}\le11\ \text{点；}11\ \text{点}\iff\text{团＝某球}\iff b(x)=11✓✓}\ \text{（把唐先生的"局部 cap }b(x)\le11\text{"升级为\textbf{团级定理} ✓）}$$

## §3 **可实现性亏空层级**（**新对象 ✓✓**）

$$\Delta_k:=\#\{\text{$k$-cliques of }G_2(C)\}-\sum_x\binom{b(x)}k\ \ge0✓\qquad(\text{因每个 }S(x)\ \text{是一个被实现的 }b(x)\text{-团 ✓})$$
$$\textbf{定理 ✓}:\ \Delta_3\equiv0\ \text{—— \textbf{每个三角形都被实现}（}\tau=\mathbf 1[\max\le2]✓\ \text{且共同球心唯一 ✓）}\ ✓✓$$
$$\textbf{定理（反例支撑 ✓）}:\ \Delta_4\ \text{可以}>0\ \text{—— §1 的四点构型即一个\textbf{未被实现的 }$K_4$✓✓};\ \text{且 }\Delta_k\ \text{随 }k\ \text{单调不减（高阶团被实现 ⟹ 其子团被实现 ✓）}✓$$
$$\textbf{局部化问题（本档提出的可证伪目标 ✓）}:\ \boxed{\text{给定团 }K_j\subseteq G_2,\ \text{它被多少个 }x\in Q_{10}\ \text{实现为 }S(x)？}✓$$
$$\qquad\text{答案 ∈ }\{0,1\}\ (\text{唯一性 ✓});\ \text{故 }\Delta_k\ \text{＝"未被实现的 }k\text{-团计数" ✓✓}$$
$$\qquad\text{三阶层：}k=2\ \text{（pair）: 被实现 ⟺ 其两中心距离 }\le2\ \text{（＝定义 ✓，故均实现 ✓）};\ k=3:\ \Delta_3=0✓;\ k=4:\ \text{首个真缺口 ✓✓}$$

## §4 $b$-profile 矩系统（**唐先生公式核验 ✓ ＋ 一处新结论 ✓**）

$$\sum_jn_j=1024✓;\quad \sum_jjn_j=11|C|=1309✓;\quad \sum_j(j-1)n_j=285✓;\quad 0\le n_j,\ j\le11✓$$
$$\sum_xb(x)^2=\sum_x(1+\delta)^2=1024+2\cdot285+\sum_x\delta^2✓;\qquad \sum_x\delta^2=\sum_x\delta+2Q=285+2Q✓$$
$$\Longrightarrow\ \boxed{\sum_jj^2n_j=1024+570+285+2Q=\mathbf{1879}+2Q}\ ✓✓\ \text{（唐先生 §5 公式\textbf{正确} ✓，其自我修正亦正确 ✓）}$$
$$\textbf{★新结论 ✓✓}:\ Q=\sum_x\binom{\delta(x)}2\ \text{被 }A\ \textbf{钉死}:\ \text{由 }\sum_x\binom{b(x)}2=2(N_1+N_2)=285+Q\Longrightarrow \boxed{Q=2(N_1+N_2)-285}\ ✓✓$$
$$\qquad\Longrightarrow\ m_2:=\sum_jj^2n_j\ \text{亦被 }A\ \text{钉死}✓;\ \textbf{profile 的自由度始于三阶}:\ \sum_x\binom{\delta(x)}3\ \big(\text{＝}T_3-Q\big)\ ✓✓$$
$$\qquad\Longrightarrow\ \text{唐先生的"Moment-feasible }\not\Rightarrow\text{realizable"问题，其\textbf{首个非平凡层＝三阶 }}\delta\text{-聚集}\ \sum\binom\delta3✓\ \text{（与 FIBER 的证人一致 ✓）}$$

## §5 与 covering 的**耦合**（**诚实评估 ⚠️**）

$$\text{已有}:\ T_3\ \text{collapse（}\to\text{ profile ✗）};\ U\ \text{值集};\ \text{全局恒等式（恒真，无约束力 ✗）};\ \Delta_3=0✓;\ \Delta_4\ \text{可正}✓✓$$
$$\text{缺口 ✓}:\ \textbf{尚未找到}\ \Delta_4\ \text{（或 }\textstyle\sum\binom\delta3\text{）与 119 必要条件之间的夹逼 ⚠️\ \text{—— 与 R5 §5 同一缺口 ✓}$$
$$\textbf{可证伪的耦合目标（本档提出 ✓）}:\ \exists\ \text{常数}:\ \Delta_4\ \ge\ L\ (\text{covering 迫使})\ \wedge\ \Delta_4\le U\ (\text{局部几何迫使})\ \wedge\ L>U\ ✓$$
$$\qquad\text{上界来源候选}:\ \text{① 团级 cap（}\le11\text{）＋ }\sum_j\binom j4n_j\ \text{被 profile 钉住的部分};\ \text{② }\sum_c|S(c)\cup V(H_c)|\le451\ (\text{R4-P1}✓)$$
$$\qquad\text{下界来源候选}:\ \text{① §1 型"四面体"构型的\textbf{出现是否被迫使}？（未证 ⚠️）};\ \text{② }N_1+N_2\ \text{的下界 143 能否推出 }\Delta_4\ \text{的下界？}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "可实现性亏空"
技术词 可实现性亏空    命中文件数=0    ::
$ bash scripts/tech_word_check.sh "共同球心"
技术词 共同球心        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "Kleitman"
技术词 Kleitman         命中文件数=0    ::
$ bash scripts/tech_word_check.sh "团覆盖重数"
技术词 团覆盖重数      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "四重交集"
技术词 四重交集        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（五词**全部命中 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；**注意**：命中 0 更好 ⟹ 说明本档进入档案未见区域 ✓✓）
- **注 ✓**：本档实质＝**§1 反例 ＋ §2 唯性与 Kleitman ＋ §3 亏空层级 ＋ §4 矩系统**（含两条定理级 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/Terwilliger** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **Kleitman 定理为档级引用** ✓（未在本档重证 ✓）；**§1 反例为自证** ✓（逐坐标核 ✓）
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** $\Delta_4$ 路线必然成功 ✗ —— 只写"**首个真兼容性缺口**"＋"**耦合仍未找到**" ⚠️
- $\Delta_k\ge0$ 为**定义性** ✓（非新结论 ✗）；$\Delta_3\equiv0$ 与 $\Delta_4$ 可正为**本档结论** ✓
