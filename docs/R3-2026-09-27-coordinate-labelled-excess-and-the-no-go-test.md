# R3-2026-09-27 — **coordinate-labelled excess（逐坐标超额）** ＋ **NO-GO 检验**

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:03 令 ✓）**：**只做 R3**（把 $\delta\ge0$ 转成对 $\gamma(e_i\oplus e_j)$ 的**逐坐标**约束，并做"是否必然坍缩到 $A_i$"的 NO-GO 检验）；**零计算** ✓；不开新候选课题 ✗。

**已查地图：命中（★ 本线已有**无标号**二阶链；本档为其**逐坐标加标签**，非重造 ✓✓）**
所查：`docs/SECOND-ORDER-2026-09-25-near-pair-pressure-chain.md`（**无标号二阶链** ✓✓：$P=E+Q$、$P=2(A_1{+}A_2)$、$Q$ 奇、$A_1\le142$）｜`docs/ALIGN-2026-09-25-our-delta-field-vs-WuChen-excess-surfeit.md`｜`docs/P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md`｜`docs/R2-2prime-2026-09-27-…`（**$\gamma$ 框架** ✓✓）｜`docs/P1-2026-09-27-support-layer-screen-results.md`｜`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §7）
D0: 本档对象 ＝ **档案已有** 119 线二阶链的**逐坐标加标签**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次把 $\delta\ge0$ 逐坐标化**：得**平移超额恒等式**、**逐坐标上界**、**标号 Gram 正定性**，并完成 NO-GO 检验 ✓）
**[RESEARCH]**

---

## §0 结论（**三产出 ＋ NO-GO 检验结果 ✓**）

$$\boxed{\text{(R3-1 恒等式)}\ \sum_{x\in C\oplus e_i}\delta(x)=m+\mathrm{star}_i,\quad \mathrm{star}_i:=\gamma(e_i)+\sum_{j\ne i}\gamma(e_i\oplus e_j)\ ✓}$$
$$\boxed{\text{(R3-2 逐坐标上界)}\ 0\le\mathrm{star}_i\le 10m-1024\ \ (m{=}119{:}\ \le166)\ \Longrightarrow\ \boxed{N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83}\ ✓✓}$$
$$\boxed{\text{(R3-3 标号正定性)}\ G:=\big(\gamma(e_i\oplus e_j)\big)_{1\le i,j\le10}\ \succeq\ 0\ \ (\text{对角}=m,\ \text{非对角}=2q_{ij})\ ✓✓}$$
$$\boxed{\textbf{★NO-GO 检验：不坍缩 ✓}\ \text{——逐项 }\mathrm{star}_i\ \text{与 }G\ \text{的标号项**不能**由 }A_1,\dots,A_{10}\ \text{线性组合得到}}✓$$

---

## §1 记号与已有关键（**引用 ✓，不重复**）

$$b(x):=|C\cap B_1(x)|=1+\delta(x)\ge1\ ✓;\quad \sum_x b=11m\Longrightarrow \sum_x\delta=11m-1024\ (m{=}119{:}285)✓$$
$$F_i(x):=\mathbf 1[x\oplus e_i\in C]\ (i\le10),\quad F_0(x):=\mathbf 1[x\in C]\Longrightarrow b=\sum_{i=0}^{10}F_i\ ✓;\quad S(x)=\{i:x\oplus e_i\in C\}✓$$
$$\gamma_C(v):=|C\cap(C+v)|\ ✓;\qquad A_i=\sum_{|v|=i}\gamma(v)\ ✓;\qquad \gamma(e_i)=2N_1^{(i)};\quad \gamma(e_i\oplus e_j)=2q_{ij}✓$$
$$\text{★已有关键（无标号）}:\ P:=\sum_x\binom{b(x)}2=2(A_1+A_2),\quad P=E+Q\ (Q:=\sum_x\binom{\delta(x)}2)\Longrightarrow A_1+A_2=\tfrac{285+Q}2\ ✓$$

---

## §2 **R3-1｜平移超额恒等式**（**3 行证明 ✓✓**）

$$\sum_{x\in C\oplus e_i}\delta(x)\ \overset{x=c\oplus e_i}{=}\ \sum_{c\in C}\big[b(c\oplus e_i)-1\big]✓$$
$$b(y)-1=\mathbf 1[y\in C]+\#\{j:\ y\oplus e_j\in C\}\ \Longrightarrow\ \sum_{c\in C}\big[b(c\oplus e_i)-1\big]=\gamma(e_i)+\sum_{c\in C}\#\{j:\ c\oplus e_i\oplus e_j\in C\}✓$$
$$\sum_{c\in C}\#\{j:c\oplus e_i\oplus e_j\in C\}=\sum_j\#\{c\in C:c\oplus(e_i\oplus e_j)\in C\}=\sum_j\gamma(e_i\oplus e_j)=m+\sum_{j\ne i}\gamma(e_i\oplus e_j)✓$$
$$\Longrightarrow\ \boxed{\sum_{x\in C\oplus e_i}\delta(x)=m+\mathrm{star}_i}\ ✓✓\ \text{（\textbf{坐标 }i\ \text{的平移块上，超额总和 ＝ }m＋\text{该坐标差集星}}✓)$$
$$\text{对照（}i{=}0\text{）}:\ \sum_{c\in C}\delta(c)=\sum_{c\in C}d_1(c)=2N_1=\sum_i\gamma(e_i)=A_1\ ✓\ \text{（\textbf{无标号} ✗）}\Longrightarrow\ \textbf{标号内容只在 }i\ge1\ \text{出现}✓✓$$

---

## §3 **R3-2｜逐坐标上界**（**新形式 ✓✓**）

$$\delta\ge0\ \wedge\ C\oplus e_i\subseteq H\ \Longrightarrow\ 0\le\sum_{x\in C\oplus e_i}\delta(x)\le\sum_{x\in H}\delta(x)=11m-1024✓$$
$$\Longrightarrow\ \boxed{0\le\mathrm{star}_i\le 10m-1024}\quad(m{=}119:\ \mathrm{star}_i\le\mathbf{166})✓✓$$
$$\text{换成对计数（}m{=}119\text{）}:\ \mathrm{star}_i=2N_1^{(i)}+2\sum_{j\ne i}q_{ij}\ \Longrightarrow\ \boxed{N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83}\ ✓✓$$
$$\textbf{读法 ✓}:\ \text{每个坐标 }i\ \text{至多承载 83 个"二阶关联"}\ \Longrightarrow\ \text{距离-2 质量\textbf{不能过于均匀摊开}}✓\ \text{（对 }N_2\ \text{偏大的候选有咬合力 ⚠️）}$$
$$\text{（一致性 ✓）}:\ \sum_i\Big[N_1^{(i)}+\sum_{j\ne i}q_{ij}\Big]=N_1+2N_2\ \Longrightarrow\ \text{全求和给出 }N_1+2N_2\le830\ ✓\ \text{（弱，但为\textbf{真}约束 ✓）}$$

---

## §4 **R3-3｜标号正定性**（**Gram／PSD ✓✓**）

$$G_{ij}:=\langle \mathbf 1_{C\oplus e_i},\mathbf 1_{C\oplus e_j}\rangle=|(C{+}e_i)\cap(C{+}e_j)|=|C\cap(C{+}e_i{+}e_j)|=\gamma(e_i\oplus e_j)\ ✓$$
$$\Longrightarrow\ G=MM^{\mathsf T}\ (M\ \text{的列为 }\mathbf 1_{C\oplus e_i})\ \Longrightarrow\ \boxed{G\succeq0}\ ✓✓;\qquad G_{ii}=\gamma(0)=m;\quad G_{ij}=2q_{ij}\ (i\ne j)✓$$
$$\text{推论（二阶主子式 ✓）}:\ m^2-(2q_{ij})^2\ge0\ \Longrightarrow\ \boxed{q_{ij}\le m/2}\ \ (m{=}119{:}\ q_{ij}\le\mathbf{59})✓$$
$$\text{扩展（更细的标号正性 ⚠️）}:\ \text{取 }D_1:=\{0\}\cup\{e_i\}\cup\{e_i\oplus e_j\}\ (|D_1|=1{+}10{+}45=56)\ \Longrightarrow\ \big(\gamma(v\oplus w)\big)_{v,w\in D_1}\succeq0\ ✓\ \text{（含权 }\le4\ \text{的项）}$$

---

## §5 **★NO-GO 检验（照唐先生要求 ✓✓）**

$$\textbf{问题}:\ \text{逐坐标量是否必然坍缩到 }A_1,\dots,A_{10}\ \text{的线性组合？}$$
| 量 | 是否坍缩 | 依据 |
|---|---|---|
| $\sum_i\mathrm{star}_i$ | **坍缩 ✓** | $=\sum_i\gamma(e_i)+2\sum_{i<j}\gamma(e_i\oplus e_j)=A_1+2A_2$ ✓ |
| $\sum_i G_{ii}$、$\sum_{i<j}G_{ij}$ | **坍缩 ✓** | $=10m$、$=\sum_{i<j}2q_{ij}=2A_2$ ✓ |
| **单项 $\mathrm{star}_i$** | **不坍缩 ✓✓** | $A$ 只给 $\sum_i\gamma(e_i)=A_1$、$\sum_{i<j}\gamma(e_i\oplus e_j)=A_2$；单项 $i$ 的 $N_1^{(i)},\ q_{ij}$ **不可由 }A\text{ 决定** ✓（P12-PASS 见证：同 $A$、异 $\{q_{ij}\}$ ✓✓） |
| **矩阵 $G$ 的标号项** | **不坍缩 ✓✓** | 同上；且 $G\succeq0$ 是**标号级**约束（对角/非对角逐项 ✓） |
$$\Longrightarrow\ \boxed{\textbf{结论：不坍缩 ⟹ 二阶 coordinate-labelled 路线\textbf{未被 }A_i\ \text{吃掉}}\ ✓✓\ \text{（即：\textbf{不是}唐先生所设的 NO-GO 情形）}}$$
$$\text{⚠️ 但\textbf{诚实标注}}:\ \text{本档所得约束\textbf{目前偏弱}——尚无 }m{=}119\ \text{的矛盾 ✗};\ \text{路线\textbf{活着}但\textbf{未通} ✓}$$

---

## §6 与门②的距离 ＋ 下一步（**两条具体路径 ✓**）

$$\textbf{路径甲（使 R3-2 变紧）}:\ \text{需一个\textbf{逐坐标下界} }N_1^{(i)}+\sum_{j\ne i}q_{ij}\ \ge\ L_i;\ \text{若 }\exists i:L_i>83\ \Longrightarrow\ \textbf{118/119 直接证否}✓$$
$$\qquad\text{候选来源}:\ \text{固定坐标 }i\ \text{的"一维覆盖"局部论证（点 }c\oplus e_i\ \text{必须被覆盖 ⟹ 邻域结构的下界）⚠️}$$
$$\textbf{路径乙（三阶标号）}:\ \sum_x F_i(x)F_j(x)\delta(x)=\sum_{x\in C_i\cap C_j}\delta(x)\ ✓\ \text{—— 等价于 }|C_i\cap C_j\cap C_k|\ \text{型的二差相关 }\gamma^{(2)}(u,v)✓$$
$$\qquad\Longrightarrow\ \text{与 }T:=\sum_x\binom{b(x)}3=Q+\sum_x\binom{\delta(x)}3\ \text{（无标号 ✓）形成\textbf{标号/无标号对照}⟹\ \text{可望给出第三层约束}✓$$

---

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "坐标标记"
技术词 坐标标记        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "标号"
技术词 标号            命中文件数=16   :: ./S9-strict-and-D2-prescreen.md ./O3-mechanism-audit-and-ontology.md ./ID-ALLOCATION-PROTOCOL.md
$ bash scripts/tech_word_check.sh "星形"
技术词 星形            命中文件数=2    :: ./Q1-CENSUS-2026-09-25-profile-indicator-coupling.md ./SECOND-ORDER-2026-09-25-near-pair-pressure-chain.md
$ bash scripts/tech_word_check.sh "Gram 正定"
技术词 Gram 正定       命中文件数=3    :: ./theorem-status-audit.md ./p59-positivedefinite-audit.md ./local-state-geometry-line-2026-09-09.md
$ bash scripts/tech_word_check.sh "NO-GO 检验"
技术词 NO-GO 检验      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "平移超额"
技术词 平移超额        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`坐标标记`／`NO-GO 检验`／`平移超额` 命中 0 ⟹ 本档自造标签，作**结构命名**，不作新性主张 ✓；`标号`（16）／`星形`（2）／`Gram 正定`（3）为档案已有 ✓）
- **注** ✓：本档实质内容＝**§2 恒等式 ＋ §3 逐坐标上界 ＋ §4 标号 PSD**（**推导性** ✓），非术语级新性 ✓

## §8 边界（硬 ✓）

- **零计算** ✓；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **NO-GO 检验的结论**只针对"**二阶 coordinate-labelled 是否坍缩**"✓ —— **不**声称"该路线必然成功" ✗，也不声称"$K(10,1)\ge120$" ✗（V290 ✓）
- 已明确标注**约束偏弱、尚无矛盾** ⚠️（防止把"路线活着"读成"已得 P1" ✗）
- ★ 与 `SECOND-ORDER-2026-09-25` 的关系已写明 ✓：该档为**无标号**链，本档为其**逐坐标加标签**（非重复 ✓）
