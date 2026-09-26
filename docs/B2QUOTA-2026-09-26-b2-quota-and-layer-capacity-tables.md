已查地图：已跑 scripts/prework_map_check.sh K(10,1) Q=1 b=2 名额 δ_k 层预算 ⟹ 执行自 `docs/F14-DEDUP-2026-09-26-...md`（① 去重表 ✓）＋ `docs/GRAM-LIFT-2026-09-25-...md`（δ_i(x) 层式 ✓）＋ `docs/Q1-CENSUS-2026-09-25-...md`（Q=1 census ✓）；本档为**纯推导**（唐先生 2026-09-26 19:43 指令「做 ①′，第一优先级是 b=2 名额」✓）；**未跑程序** ✓；**不碰 A23／新 frontier／solver** ✓。
D0: 本档对象 = `Q=1` 分支的 **b=2 名额分布**（跨层耦合）＋ 层容量上界表（既有对象；非新对象）
D1: 0（无新独立自由度；产出为精确定理 #(b=2)=283、A₁ 下界改进、双表与耦合恒等式定位）

# B2QUOTA-2026-09-26 · ①′ b=2 名额 × 层容量（纯推导）

## §0 本档三条硬结论（先给结论 ✓）

```
$$\boxed{\textbf{(T1)}\ \#\{x:\ b(x)=2\}\ =\ \mathbf{283}\ \text{（A/B 两分支皆然，且与}\ A_1\ \text{无关）}}\ ✓✓\quad\text{（精确，已证）}$$
$$\boxed{\textbf{(T2)}\ \text{分支 A}:\ \#\{x\notin C:b(x)=2\}=283-2A_1\ \ge3\ \Longrightarrow\ \mathbf{A_1\le140}\ \text{（改进档案 142）}\ ✓✓}$$
$$\boxed{\textbf{(T3)}\ \text{跨层耦合的正确载体}:\ \sum_k\delta_k(z)=E=285\ ✓\ \Longrightarrow\ \textbf{b=2 名额被强制点远未耗尽}\ (283\gg3)\ \Longrightarrow\ \textbf{本路线不闭合}\ ✗}$$
$$
$$
```

---

## §1 (T1) $\#(b=2)=283$ 的证明（两分支通用 ✓）

```
$$\text{记}\ z\ \text{为唯一}\ b=3\ \text{点（A:}\ z\notin C;\ \text{B:}\ z\in C\ ✓\ \text{——两分支都有}\ b(z)=3\ ✓）;\ \forall x\ne z:\ b(x)\le2\ ✓$$
$$\text{全覆盖（R2）}\Longrightarrow \forall x:\ b(x)\ge1\ \Longrightarrow\ x\ne z\Rightarrow b(x)\in\{1,2\}\ ✓$$
$$\sum_x b(x)=\sum_x|C\cap B_1(x)|=\sum_{c\in C}|B_1(c)|=11M=11\times119=\mathbf{1309}\ ✓$$
$$\Longrightarrow\ \sum_{x\ne z}b(x)=1309-3=1306\ \text{（共 1023 个点，每个}\ b\in\{1,2\}\ ✓）$$
$$\text{设}\ n_2:=\#\{x\ne z:b(x)=2\}\ \Longrightarrow\ 2n_2+1\cdot(1023-n_2)=1306\ \Longrightarrow\ \boxed{n_2=\mathbf{283}}\ ✓✓$$
$$
$$
```

**⚠️ 与档案独立一致 ✓**：档案 Q=1 profile 写「$283\times\{\delta=1\}+1\times\{\delta=2\}+740\times\{\delta=0\}$」✓ ——
因 $\delta=b-1$：$\delta=1\Leftrightarrow b=2$ ✓ ⟹ **逐数字吻合** ✓✓（本档给出的是**证明** ✓）。

---

## §2 (T2) 名额分解与 $A_1$ 下界改进（本档新 ✓）

```
$$\textbf{分解}:\ \underbrace{\#\{c\in C:b(c)=2\}}_{\text{码字侧}}\ +\ \#\{x\notin C:b(x)=2\}\ =\ 283\ ✓$$
$$\textbf{码字侧}:\ b(c)=1+d_1(c)\ ✓;\ \text{分支 A}\ \forall c\in C:\ d_1(c)\le1\ \Longrightarrow\ \#\{c:d_1(c)=1\}=\sum_c d_1(c)=\mathbf{2A_1}\ ✓$$
$$\qquad\Longrightarrow\ \text{分支 A}:\ \#\{x\notin C:b(x)=2\}=\mathbf{283-2A_1}\ \ge\ 0\ \Longrightarrow\ A_1\le141\ ✓$$
$$\textbf{再用①的点名型强制}:\ y_{12},y_{13},y_{23}\ \text{是}\ b=2\ \text{的\textbf{非码字}}（\text{球内恰含}\ e_a,e_b\ \text{两个码字}\ ✓）\ \Longrightarrow\ 283-2A_1\ \ge\ \mathbf 3$$
$$\qquad\Longrightarrow\ \boxed{\mathbf{A_1\le140}}\ ✓✓\ \text{（档案此前为}\ A_1\le142\ ✓\ \text{——本档改进 2）};\quad A_1+A_2=143\ \Longrightarrow\ \boxed{\mathbf{A_2\ge3}}\ ✓\ (\text{档案}\ \ge1\ ✓)$$
$$\textbf{分支 B}:\ \text{码字侧}=\#\{c\ne z:d_1(c)=1\}=2A_1-2\ (\text{因}\ d_1(z)=2\ ✓)\ \Longrightarrow\ \#\{x\notin C:b=2\}=285-2A_1\ \ge1\ \Longrightarrow\ A_1\le142\ ✓\ (\text{无改进})$$
$$
$$
```

---

## §3 表一：逐层 $|C\cap L_k|$ 上界

```
$$\begin{array}{c|c|c|c}
L_k & \text{分支 A} & \text{分支 B} & \text{依据}\\ \hline
L_1 & \mathbf 3\ (\text{精确}) & \mathbf 2\ (\text{精确}) & N(z)\cap C\ \text{恰为 3/2 个（}\ b(z)=3\ ✓）\\
L_2 & \le\mathbf{10} & \le\mathbf 8 & \text{① §6 行容量法（每行}\ b(e_l)\le2\ ✓;\ \deg(e_m)\le1\ ✓）\\
L_3 & \le 9\ (\text{全坐标}\ \ge4\ \text{子类}) & — & \text{见 §4（部分）}\\
L_4 & \text{未定} & \text{未定} & —\\
\end{array}$$
$$
$$
```

**$L_3$ 的（部分）上界推导**（行容量法第二代 ✓）：

```
$$\text{① 的 22 个点名非码字中，}\ \{l,m\}\ (l,m\ge4)\ \text{类共}\ \ge14\ \text{个被点名}\ ✓\ \Longrightarrow\ \text{每个给一行约束}\ “\text{其 8 个}\ L_3\ \text{邻居中码字}\le2”\ ✓$$
$$\text{而}\ L_3\ \text{的"全坐标}\ge4"\ \text{点}\ \{l,m,c\}\ \text{恰落在 3 个此类行内（}\{l,m\},\{l,c\},\{m,c\}\ ✓）$$
$$\Longrightarrow\ 3\#\{\text{全坐标}\ge4\ \text{的}\ L_3\ \text{码字}\}\ \le\ 2\times14=28\ \Longrightarrow\ \#\ \le\ \lfloor 28/3\rfloor=\mathbf 9\ ✓$$
$$
$$
```

---

## §4 表二：$\text{forced }b=2$ 点数（本档核心表 ✓）

```
$$\begin{array}{c|c|c|c}
L_k & \text{分支 A} & \text{分支 B} & \text{依据}\\ \hline
L_1 & 0 & 0 & e_l\ (l\ge4)\ \text{仅被钉"}\le2\text{"，非"}=2\text{"}\ ✗\\
L_2 & \mathbf 3 & \mathbf 1 & y_{ab}\ \text{球内恰含}\ e_a,e_b\ ✓;\ w\ \text{球内恰含}\ u,v\ ✓\\
L_3 & \mathbf 0 & \mathbf 0 & \text{球内已知码字}\ \le1\ (\text{其余全为}\ \textbf{未知}\ \text{或点名的非码字}\ ✓)\\
L_4 & \mathbf 0 & \mathbf 0 & \text{同上}\ ✗\\
\end{array}$$
$$\textbf{跨层去重后总数}:\ \text{分支 A}=\mathbf 3;\quad \text{分支 B}=\mathbf 1\ ✓\ (\text{层间不交}\ ✓\ \text{——① §5 已证}\ ✗\ \text{无重叠}\ ✓)$$
$$
$$
```

---

## §5 ⭐ **跨层耦合的正确载体（本档定位，避免"逐层相加"陷阱 ✓）**

```
$$\textbf{错的做法}:\ \sum_k U_k\le119\ ✗\ (\text{层容量源于不同 witness 的邻域 ⟹ 覆盖对象会重复}\ ✓)$$
$$\textbf{正确载体}:\ \text{层式缺陷恒等式（GRAM-LIFT ✓）}:\ \delta_k(z)=\sum_{x\in L_k}(b(x)-1)=A_k(z)+(11-k)A_{k-1}(z)+(k+1)A_{k+1}(z)-\binom{10}{k}\ ✓$$
$$\qquad\text{且（档案）}\ \sum_{k=0}^{10}\delta_k(z)=E=\mathbf{285}\quad\forall z\ ✓✓$$
$$\Longrightarrow\ \#\{x\in L_k:b(x)=2\}=\delta_k(z)\ -2\cdot[\![\,z\in L_k\,]\!]\ ✓\ \Longrightarrow\ \sum_{k\ge1}\#\{b=2\ \text{in}\ L_k\}=285-2=\mathbf{283}\ ✓✓\ (\text{与 (T1) 吻合 ✓})$$
$$
$$
```

**⟹ 三点含义**：

```
$$\text{① b=2 名额是}\ \textbf{层预算}\ \text{的一部分，不是独立新约束}\ ✓\ \text{——但}\ \delta_k(z)\ge\#(\text{点名}b=2\ \text{in}\ L_k)\ \text{给出\textbf{局部下界}}\ ✓$$
$$\text{② 总数}\ 283\ \text{vs 强制}\ 3\ \Longrightarrow\ \textbf{名额远未耗尽}\ ✗\ \Longrightarrow\ \text{靠 b=2 名额撞矛盾，当前机制强度差两个量级}\ ✗$$
$$\text{③ 真正可用的副产品（本档给出）}:\ \delta_2(z)=A_2(z)+3A_3(z)-18\ \ge\ 3\ \Longrightarrow\ \boxed{A_2(z)+3A_3(z)\ \ge\ \mathbf{21}}\ ✓✓\ (\text{局部层剖面约束，新})$$
$$
$$
```

---

## §6 诚实结论（按唐先生"若数量仍很小则停"指令 ✓ —— 现即停 ✓）

```
$$\textbf{① (T1) 精确定理}:\ \#(b=2)=283\ ✓✓\ \text{（两分支通用，与}\ A_1\ \text{无关）—— 本档最有价值产物}$$
$$\textbf{② (T2) 真下界改进}:\ \text{分支 A}\ A_1\le140,\ A_2\ge3\ ✓✓\ (\text{档案}\ 142/1\ ✓)\ ——\ \textbf{这是"名额}>forced"\ \text{的第一次实际兑现}\ ✓$$
$$\textbf{③ 双表已出}:\ |C\cap L_k|\ (\text{A: 3,}\le10,\le9,\dots)\ ✓;\ \text{forced}\ b{=}2\ (\text{A: 0,3,0,0})\ ✓$$
$$\textbf{④ 未闭合}\ ✗:\ \text{forced}\ b{=}2\ \text{总数}\ 3/1\ \ll\ \text{名额}\ 283/285\ ✗;\ \text{差}\ \sim 100\ \text{倍};\ \text{机制强度不足，非计数口径问题}\ ✓$$
$$\textbf{⑤ 唯一新增可用杠杆}:\ A_2(z)+3A_3(z)\ge21\ (\text{局部}) \times A_1\le140\ (\text{全局})\ \text{联立}\ ✓$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 为**证**（用 $\sum_x b(x)=11M$ 与 $b\le3$、$b(z)=3$ ✓）；与档案 Q=1 profile **逐数字吻合** ✓
- §2 的 $A_1\le140$、$A_2\ge3$ 为**本档新推导** ✓（依赖 ① 的 $y_{ab}$ 点名结果 ✓）；**分支 B 无改进** ✓
- §3 的 $L_2\le10/8$ 承 ① ✓；$L_3\le9$ 为**子类**上界（非全层）✓
- §4 的 forced 表为**逐层清点**（跨层不交已证 ✓ ⟹ 可加 ✓）
- §5 的 $\delta_k$ 恒等式承 GRAM-LIFT ✓（本档仅作耦合定位 ✓）；$A_2(z)+3A_3(z)\ge21$ 为**本档新推导**（未程序验证 ✗）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 b=2 名额       命中文件数=1    :: ./B2QUOTA-2026-09-26-b2-quota-and-layer-capacity-tables.md 
技术词 层预算耦合  命中文件数=1    :: ./B2QUOTA-2026-09-26-b2-quota-and-layer-capacity-tables.md 
技术词 局部层剖面约束 命中文件数=1    :: ./B2QUOTA-2026-09-26-b2-quota-and-layer-capacity-tables.md
```
- **本档新增**：b=2 名额、层预算耦合、局部层剖面约束（见上方逐字命中数）
- **档案已有（引用，不列为提出）**：$\delta_k(z)$、层式缺陷恒等式、surfeit
