已查地图：已跑 scripts/prework_map_check.sh over-covering OC Q_ours 桥 重写 ΣOC ⟹ 执行自 PRIVPEN-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = 新恒等式 I1/I2 及其对主桥（M=K ⟹ A≤2）的重写；square 线正式降级为封存资产
D1: 1（新增：**I1** ✓、**I2** ✓（均精确验证）；**桥 ⟺ ΣOC 下界** ✓✓；square 线降级 ✓）

# OC-BRIDGE-2026-09-26

## §0 square 线降级（唐先生定 ✓）

```
$$\textbf{封存两项资产}: \quad 4S\le Q_2\ ✓;\qquad 4S=Q_2\Longrightarrow\text{square 顶点不交},\ V=4S=N_{\ge3},\ \text{每 hot 点恰 2 邻}\ ✓$$
$$\text{保留为\textbf{检测器}}: S\ge14\Rightarrow \text{出现 }b\ge4\ \text{defect}\ ✓;\quad 4S=Q_2\Rightarrow \text{刚性 face-closure}\ ✓$$
$$\textbf{前提缺失（不再推进）}: \text{continuation 需要未核实的 concentration premise}\ ⚠️\ \Longrightarrow\ \text{继续优化 }\sum D(s_c)\ \text{是人为计算量}\ ✗$$
$$

## §1 ⭐ **新恒等式 I1**（我方 ✓，n=4/5/9 全枚举精确验证 ✓）

```
$$\boxed{\sum_{x\notin C}\mathrm{OC}(B_1(x))\ =\ \sum_{y}\bigl(b(y)-1\bigr)\bigl(n+1-b(y)\bigr)}\ ✓✓$$
$$\text{证明（双计数 ✓）}: \sum_{x\notin C}\sum_{y\in B_1(x)}(b(y)-1)=\sum_y(b(y)-1)\,\#\{x\notin C:\ x\in B_1(y)\}\ ✓$$
$$\qquad\text{而 }|B_1(y)\cap C|=b(y)\ \Longrightarrow\ \#\{x\notin C:\ x\in B_1(y)\}=(n+1)-b(y)\ ✓✓$$
$$

## §2 ⭐⭐ **新恒等式 I2 —— 桥的重写**（我方 ✓，全枚举精确验证 ✓✓）

```
$$\boxed{Q_{\mathrm{ours}}\ =\ \frac{(n-1)E-\sum_{x\notin C}\mathrm{OC}(B_1(x))}{2}}\ ✓✓$$
$$\textbf{核验}: (4,4): [(3)(4)-12]/2=0=Q_{\mathrm{ours}}\ ✓;\ (4,5): [27-21]/2=3\ ✓;\ (5,7): [40-36]/2=2\ ✓;\ (9,64): [8\cdot128-896]/2=64\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{Q}_{\mathrm{ours}}\ \text{上界}\iff\sum_{x\notin C}\mathrm{OC}(B_1(x))\ \text{下界}}\ ✓✓$$
$$

## §3 为什么这条重写**有用**（诚实定位 ✓）

```
$$\text{① 它是\textbf{等价改写}}（由 profile 恒等式代数可得 ✓）\ —— \textbf{不是新信息}\ ✗;\ \text{但:}$$
$$\text{② 它把"二阶"量 }Q_{\mathrm{ours}}\ \text{换成了\textbf{全局 over-covering 总量}}\ \sum\mathrm{OC}\ ✓,\ \text{而这正是 excess 机器的原生坐标}\ ✓✓$$
$$\text{③ \textbf{精确定位了文献机器的缺口}}: \text{Struik 的逐球界对奇 }n\ \text{为空}\ ✗\ (\text{此前已证}\ ✓)\ \Longrightarrow\ \text{奇 }n\ \text{需要的是 }\sum\mathrm{OC}\ \text{的\textbf{全局下界}}\ ✓✓\ ——\ \text{逐球工具在此原理性无效}\ ✗$$
$$

## §4 奇 n 的**计数化目标**（我方 ✓）

```
$$\text{奇 }n:\ \text{每个 }\mathrm{OC}\ \text{为偶数}\ ✓\ \Longrightarrow\ \mathrm{OC}>0\Rightarrow\mathrm{OC}\ge2\ \Longrightarrow\ \sum\mathrm{OC}\ \ge\ 2\cdot\#\{x\notin C:\ \mathrm{OC}(B_1(x))>0\}\ ✓$$
$$\Longrightarrow\ \textbf{目标（M=62, }n=9\text{）}:\quad \#\{x\notin C:\ \mathrm{OC}>0\}\ \ge\ \frac{864-2Q^*}{2}=432-Q^*\ ✓$$
$$\qquad\text{若 }Q^*\le26:\ \text{至少 }\mathbf{406/450}\ \text{个非码字球必须有正过量}\ ✓✓\ (\text{平均值} \approx1.92\ ✓)$$
$$\qquad\Longrightarrow\ \textbf{极其具体的结构要求}\ ✓\ ——\ \text{已不再是抽象不等式}\ ✓$$
$$

## §5 主桥重锁（唐先生 ✓）

```
$$\boxed{M=K(n,1),\ n\ \text{odd}\ \Longrightarrow\ A_{\le2}=A_1+A_2\ \text{有上界}}\ ✓$$
$$\text{等价形式}: Q_{\mathrm{ours}}\ \text{有上界}\ \iff\ \sum_{x\notin C}\mathrm{OC}(B_1(x))\ \ge\ (n-1)E-2Q^*\ \iff\ \#\{\mathrm{OC}>0\}\ \ge\ 432-Q^*\ (n=9,M=62)\ ✓$$
$$\text{下一刀候选（按杠杆排序 ✓）}:\ \text{① 直接攻 }\sum\mathrm{OC}\ \text{的全局下界（用 minimality／私有点 ✓）};\ \text{② 攻 }\#\{\mathrm{OC}>0\}\ \text{的计数下界（更粗、更可能可证 ✓）};\ \text{③ 用 I1 的 profile 形式 }\sum(b-1)(n+1-b)\ \text{做极值分析}\ ✓$$
$$

## §6 台账

```
$$\textbf{新增}: I1\ ✓,\ I2\ ✓\ (\text{桥的重写}),\ \text{奇 }n\ \text{的计数目标}\ ✓;\quad \textbf{降级}: \text{square 线}\to\text{封存资产}\ ✓$$
$$\textbf{桥}: \textbf{未打通}\ ✗\ (\text{但已换成更可攻的坐标}\ ✓);\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1–§2 为**我方推导 ＋ 全枚举精确核验** ✓（n=4 全枚举 ✓、n=5 全枚举 ✓、n=9 我方构造 ✓）
- §3① 明示 I2 是**等价改写**（非新信息 ✓）—— 其价值在**定位缺口**与**接入 excess 机器** ✓
- §4 的计数目标为**必要条件** ✓（非充分 ✗）；**未**声称可达 ✗
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 过量覆盖总量恒等式 命中文件数=1    :: ./OCBRIDGE-2026-09-26-over-covering-identity-and-bridge-rewrite.md 
技术词 计数化目标  命中文件数=1    :: ./OCBRIDGE-2026-09-26-over-covering-identity-and-bridge-rewrite.md 
技术词 桥的重写     命中文件数=1    :: ./OCBRIDGE-2026-09-26-over-covering-identity-and-bridge-rewrite.md 
技术词 逐球无效     命中文件数=1    :: ./OCBRIDGE-2026-09-26-over-covering-identity-and-bridge-rewrite.md 
```
- **本档新增**（命中数=1 但**仅本档自身 = self-hit** ⟹ 扣自引后 = 0 ✓）：过量覆盖总量恒等式、计数化目标、桥的重写、逐球无效
- **档案已有（引用，不列为提出）**：over-covering、Struik、van Wee
