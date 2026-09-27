# R4-P1b-2026-09-27 — **三点层 T1/T2/T3 符号筛选**（admissible 三元组 ｜ $\tau$ ｜ 分离性）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:27 令 ✓）**：只做 T1/T2/T3 的**符号层筛选**（$11^3$ 规模，非计算攻击 ✓）；**不上 Terwilliger SDP** ✗；**不碰** R3 线 ✗。

**已查地图：命中（接续 R4-P1 与 KOPT4-6 的 STAR/TRI 分析，非新案 ✓）**
所查：`docs/R4-P1-2026-09-27-private-point-deficit-lemma-and-codeword-labelled-occupancy.md`（**$S(c)\cup V(H_c)$／451** ✓✓）｜`docs/SECOND-ORDER-2026-09-25-near-pair-pressure-chain.md`（**$T=\sum\binom b3=Q+\sum\binom\delta3$** ✓✓）｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`（**STAR/TRI** ✓✓）｜`docs/R3-2026-09-27-…`｜`docs/ASSETS-REGISTRY.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §8）
D0: 本档对象 ＝ **档案已有** 三点层对象的**符号筛选（T1/T2/T3）**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $\tau$ 的精确公式与 $\tau\in\{0,1\}$ 二分 ＋ 识别出三点层的新信息量 ＝ 三角形计数 ✓**）
**[RESEARCH]**

---

## §0 结论（**T1 ✓｜T2 $\tau\in\{0,1\}$｜T3 分层：单三元组 FAIL ✗／张量 PASS ✓**）

$$\boxed{\textbf{T1}:\ \text{admisible 条件 }\ a+b+c\equiv0\ (\!\!\bmod2),\ \text{三角不等式},\ a+b+c\le20\ \ \textbf{正确}✓\ (\text{用户四类型参数化已逐式验证}✓)}$$
$$\boxed{\textbf{T2}:\ \tau(c_1,c_2,c_3):=|B_1(c_1)\cap B_1(c_2)\cap B_1(c_3)|\ \in\ \{0,1\}\ (\!\!\text{不同中心}\!\!)\ ✓;\quad \tau=1\iff\max(a,b,c)\le2✓✓}$$
$$\boxed{\textbf{T3-a（单个三元组）}:\ \textbf{FAIL}✗\ \text{—— }\tau\ \text{由 }(a,b,c)\ \text{完全决定（见 §1）};\ \textbf{自由度不在单个三元组内}}$$
$$\boxed{\textbf{T3-b（张量/聚合）}:\ \textbf{PASS}✓\ \text{—— }\textstyle\sum_x\binom{b(x)}3=\sum_{\text{unordered triples}}\tau=T_3(G_2)\ \text{不被 A 决定}✓✓}$$
$$\boxed{\text{三点层的新信息量被}\textbf{精确识别}✗:\ \equiv\ \textbf{覆盖轮廓的三阶矩}\ \textstyle\sum_x\binom{b(x)}3\ (\text{＝}Q+\sum\binom\delta3)✓}$$

---

## §1 T1：admissible 三元组（**用户参数化 ✓ 逐式验证**）

$$\text{固定 }c_1,c_2,c_3;\ a:=d_{12},\ b:=d_{13},\ c:=d_{23};\ \text{相对 }c_1\ \text{的坐标四类型计数 }n_{00},n_{10},n_{01},n_{11}✓$$
$$a=n_{10}+n_{11},\quad b=n_{01}+n_{11},\quad c=n_{10}+n_{01},\quad \sum n_{\bullet\bullet}=10✓$$
$$\Longrightarrow\ \boxed{n_{11}=\tfrac{a+b-c}2,\ n_{10}=\tfrac{a+c-b}2,\ n_{01}=\tfrac{b+c-a}2,\ n_{00}=10-\tfrac{a+b+c}2}✓✓\ \text{（用户公式\textbf{全部正确}✓）}$$
$$\text{完备性 ✓}:\ \text{四式非负整数 ⟺ }a+b+c\ \text{偶}\ \wedge\ \text{三角不等式}\ \wedge\ a+b+c\le20✓;\ \text{（次之 }a,b,c\le10\ \text{自动 ✓）}$$
$$\textbf{非退化}✓:\ \text{中心两两不同}\Longrightarrow a,b,c\ge1✓\ (\text{故 }(1,1,1)\ \text{奇和 ✗ 排除},\ (0,\cdot,\cdot)\ \text{排重 ✗})$$

## §2 T2：$\tau$ 的**精确公式**（**本档推导 ✓✓**）

$$\text{取 }c_1\ \text{为基};\ B_1(c_1)=\{c_1\}\cup\{c_1\oplus e_i\} \Longrightarrow \tau=[\,c_1\ \text{被 }c_2,c_3\ \text{共覆盖}\,]+\#\{i:\ c_1\oplus e_i\ \text{同时邻 }c_2,c_3\}✓$$
$$\text{逐类型（四类型 ⟹ 三点皆在 }\le2\ \text{内 ⟹ 置换不变 ✓）}:\qquad \text{type-11}:\ d(e_i,c_2)=a-1,\ d(e_i,c_3)=b-1✓;\quad \text{type-10}:\ d=a-1,\ d=\tfrac{b+c-a}2+1✓$$
$$\qquad \text{type-01}:\ d=a+1,\ d=b-1✓;\qquad \text{type-00}:\ d=a+1\ (\text{通常 }\ge2\ ✗)✓$$
$$\Longrightarrow\ \boxed{\tau=[\,\max(a,b)\le1\,]+n_{11}[\,a\le2\wedge b\le2\,]+n_{10}\big[\,a\le2\wedge n_{01}=0\,\big]+n_{01}[\,a=0\wedge b\le2\,]}✓$$
$$\textbf{二分 ✓✓}:\ \text{非退化下第 1 与第 2 项\textbf{互斥}（}n_{11}\ge1\Longrightarrow a=b=1\Longrightarrow c=0\ \text{退化 ✗）; 第 4 项需 }a=0\ ✗ ⟹ \boxed{\tau\in\{0,1\}}✓✓$$
$$\textbf{可达型 ✓（全部）}:\ \tau=1\iff\max(a,b,c)\le2\iff\{c_1,c_2,c_3\}\ \text{是 }G_2\ \text{的三角形}✓✓;\ \text{型恰好四：}\text{perm}(1,1,2)\ \text{与}\ (2,2,2)✓$$
$$\textbf{重要副产 ✓}:\ \text{整个三点张量 }T_{abc}\ \textbf{支撑仅在那四型上} ⟹ \text{三点距离内容 ＝ 四个计数（很\textbf{薄}的对象 ✓）}$$

## §3 T3-a：单个三元组层面 **FAIL ✗**（**必须修正框架 ✓**）

$$\tau\ \text{只依赖坐标四类型 }(n_{00},n_{10},n_{01},n_{11})\ \text{—— 因三个球对坐标置换不变 ✓} \Longrightarrow \tau\ \text{是 }(a,b,c)\ \text{的函数}✓$$
$$\Longrightarrow\ \boxed{\text{"同 pairwise profile 而 }\tau\ \text{不同"在\textbf{单个三元组}内\textbf{不可能}}✗✓}$$
$$\text{故自由度只能出现在}\textbf{张量分布}\ \text{层面（即哪些三元组出现）✓ —— 见 §4}$$

## §4 T3-b：张量/聚合层面 **PASS ✓**（**新信息量已识别**）

$$\text{由 §2 }\tau\equiv\mathbf 1[\text{三角形}]:\qquad \sum_x\binom{b(x)}3=\#\{(x;\{c_1,c_2,c_3\}):x\in B_1(c_1)\cap B_1(c_2)\cap B_1(c_3)\}=\sum_{\text{unordered triples}}\tau=T_3(G_2)✓✓$$
$$\textbf{而 }T_3(G_2)\ \text{不被 }A\ \text{决定 ✓}:\ \text{边数 }N_1+N_2\ \text{只给 }|E(G_2)|;\ \textbf{同边数异三角形数} \text{是初等图论事实 ✓✓（如三角形 vs 三边路径 ✓）}$$
$$\Longrightarrow\ \boxed{\textbf{三点层确有超出二阶计数的自由度}✓✓\quad\text{（即 }A\not\Rightarrow T\ \text{成立，且内容 ＝ }T_3(G_2)✓）}$$
$$\textbf{与档案恒等式一致 ✓}:\ \sum_x\binom{b}3=Q+\sum_x\binom\delta3\ (\text{SECOND-ORDER §1(6)}✓)\ \text{—— 故三点层 ＝ 覆盖轮廓的三阶矩 ✓}$$

## §5 诚实的限界（**照唐先生 §7 告诫 ✓**）

$$\text{⚠️ }A\not\Rightarrow T\ \textbf{不是} P1\ ✗;\ \text{甚至 }A\not\Rightarrow\tau\ \text{也不够 ✗};\ \text{须}:\ T\in\mathcal T_{\rm cover}=\varnothing\ \text{或}\ \exists\ \text{不可兼容模式}✓$$
$$\text{⚠️ 更冷的现实 ✓}:\ \sum\binom{b}3\ \text{是 }\delta\text{-型泛函}; \text{档案已立 }\boxed{\text{十类 }\sum_xf(\delta(x))\ \text{全被 profile 指纹钉住}}\ \text{（GAPTHEOREM）✓}$$
$$\qquad\Longrightarrow\ \textbf{真问题转为}:\ b\text{-profile }\{n_j\}\ \text{是否被 }A\ \text{决定}？\ ⚠️\ \textbf{开放}✓\ \text{（本档不判）}$$

## §6 与 covering 的**耦合目标**（本档提出；下一步可攻 ✓）

$$\textbf{资源候选（照唐先生 §7 清单 ✓）}:\quad \textbf{(i)}\ \text{局部占用预算（R4-P1 ✓）}:\ \sum_c|S(c)\cup V(H_c)|\le\mathbf{451}✓;\quad \textbf{(ii)}\ \text{excess }285✓$$
$$\textbf{耦合形态 ✓（可证伪 ✓）}:\quad \text{三角形 }(c_1,c_2,c_3)\ \text{处，三码字的 }V(H)\ \text{各含一个 type-11 方向} \Longrightarrow \text{三角形消耗\textbf{局部占用} ✓} \Longrightarrow \text{若 }T_3(G_2)\ \text{下界与 451 上界冲突 ⟹ }\bot✓✓$$
$$\qquad\text{（形式化目标}:\ \exists\ \text{常数 }K_\ast:\ T_3(G_2)\ \ge\ K_\ast\ \text{（covering 迫使）}\ \wedge\ T_3(G_2)\le K^\ast\ \text{（451 迫使）}\ \wedge\ K_\ast>K^\ast\big)✓$$

## §7 Terwilliger 的位置（**照唐先生 ✓**）

$$\text{本档已完成 T1/T2/T3 ⟹ \textbf{先不开 Terwilliger SDP} ✗✓};\ \text{开它的\textbf{门槛}:\ §6 的耦合若给出"三角形质量 }\bot\ \text{局部预算"，才值得上 §6 描述的三阶 Terwilliger PSD slack}✓$$

## §8 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "三点张量"
技术词 三点张量        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "三元交叠"
技术词 三元交叠        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "三角形计数"
技术词 三角形计数      命中文件数=1    :: ./M03-SPEC-CLOSURE-and-N5-first-assembly.md
$ bash scripts/tech_word_check.sh "admissible 三元组"
技术词 admissible 三元组 命中文件数=1    :: ./redei-implementation-progress.md
$ bash scripts/tech_word_check.sh "覆盖资源"
技术词 覆盖资源        命中文件数=1    :: ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md
```
- **本档新增**：**0** 个术语 ✓（`三点张量`／`三元交叠` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注** ✓：本档实质＝**§2 $\tau$ 精确公式与二分 ＋ §4 新信息量识别 ＋ §6 耦合目标**（推导性 ✓）

## §9 边界（硬 ✓）

- **零计算** ✓（$11^3$ 由公式**解析**完成，未跑枚举程序 ✓）；**未上 Terwilliger** ✗；**未碰** R3 线／$\mu$／PSD／SAT ✓；**未开门②** ✓；**未改门** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** 三点层必然破局 ✗ —— 只写"**新信息量 ＝ $T_3(G_2)$**"＋"**其与 covering 的耦合仍开放**" ✓
- §5 的"$\delta$-型泛函被 profile 钉住"为**档案结论引用** ✓，本档**未**重证 ✓
