已查地图：已跑 scripts/prework_map_check.sh K(10,1) 孤立码字 距离-2 度 双计数 packing ⟹ 执行自 `docs/PACKB-2026-09-26-...md`（匹配定理与 A₁≤59/60 ✓）＋ `docs/B2QUOTA-2026-09-26-...md`（b=2 名额 ✓）；本档为**纯推导**（唐先生 2026-09-26 19:57 指令「开 B-3，做 rI ≤ sA₂ 型双计数」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支孤立码字与距离-2 度的双计数（既有对象；非新对象）
D1: 0（产出为参数化修正、一条局部恒等式、一条新界与双计数退化判定）

# ISOB3-2026-09-26 · 孤立码字 ↔ 距离-2 度：双计数退化

## §0 结论（先给）

```
$$\boxed{\textbf{(C-0)}\ \text{用户参数化一处 off-by-one 已纠}:\ I=119-2A_1\ (A)\ ✓;\ \mathbf{I=120-2A_1}\ (B)\ \text{（非 121）}\ ✓}$$
$$\boxed{\textbf{(C-1)}\ \text{局部恒等式}:\ \forall c\in C:\ \sum_{y\in N(c)}(b(y)-1)\ =\ d_1(c)+2a_2(c)\ ✓\ \text{（}a_2(c):=\#\{c':d(c,c')=2\}\ ✓）}$$
$$\boxed{\textbf{(C-2)}\ \Longrightarrow\ \text{用户要的映射恰是 \textbf{2-to-1} 满射到距离-2 度}\ \Longrightarrow\ \textbf{双计数退化为恒等式}\ ✗\ \text{（不产不等式）}\ ✓✓}$$
$$\boxed{\textbf{(C-3 新界)}\ \text{隐私非负} \Longrightarrow\ \forall c:\ \mathbf{a_2(c)\ \le\ 5}\ ✓\ \Longrightarrow\ A_2\le\lfloor5M/2\rfloor=297\ ✗\ \text{（太弱）}}$$
$$\boxed{\textbf{(C-4)}\ \text{未获}\ A_1\ \text{下界}\ ✗;\ \text{但定位了"为什么这类双计数必然退化"}\ ✓✓}$$
$$
$$
```

---

## §1 参数化（含 off-by-one 修正）

```
$$\textbf{分支 A}:\ \text{非孤立} = 2A_1\ (\text{每对贡献 2})\ \Longrightarrow\ \boxed{I=119-2A_1}\ ✓\ (\textbf{必为奇数}\ ✓:\ 119\ \text{奇}）$$
$$\qquad A_1\le59\iff I\ge1\ ✓;\ A_1=59\Rightarrow I=1,\ A_1=58\Rightarrow I=3,\dots\ ✓$$
$$\textbf{分支 B}:\ z\ \text{有}\ d_1(z)=2\ \text{（角度 2）},\ \text{其余}\le1\ \Longrightarrow\ \#\{c\ne z:d_1=1\}=2A_1-2$$
$$\qquad\text{非孤立数} = \underbrace{1}_{z}+\underbrace{(2A_1-2)}=2A_1-1\ \Longrightarrow\ \boxed{I=119-(2A_1-1)=\mathbf{120-2A_1}}\ ✓✓$$
$$\qquad(\text{用户写}\ 121-2A_1\ ✗:\ \text{该式把}\ z\ \text{本身也算作孤立}\ ⚠️\ \text{已纠}\ ✓)$$
$$\qquad A_1\le60\iff I\ge0\ ✓;\ \textbf{分支 B 不强制}\ I\ge1\ ✗\ (A_1=60\Rightarrow I=0\ \text{允许}\ ✓)$$
$$
$$
```

---

## §2 (C-1) 局部恒等式（本档核心；由 §4 的隐私量反推 ✓）

```
$$\textbf{基础}:\ B_1(c)=\{c\}\cup N(c)\ ✓;\quad \sum_{y\in N(c)}1 = 10\ ✓;\quad \{y\in N(c):d(y,c')=1\}\ \text{按}\ c'\ \text{分类}$$
$$\textbf{对固定}\ c'\ne c:\ |N(c)\cap B_1(c')|=\begin{cases}1,&d(c,c')=1\\ 2,&d(c,c')=2\\ 0,&d\ge3\end{cases}\ ✓$$
$$\qquad(\text{由}\ |B_1(c)\cap B_1(c')|=(11,2,2,0)\ \text{减}\ [\![c\in B_1(c')]\!]\ ✓)$$
$$\Longrightarrow\ \sum_{y\in N(c)}(b(y)-1)=\sum_{c'\ne c}|N(c)\cap B_1(c')|\cdot 1=\boxed{d_1(c)+2a_2(c)}\ ✓✓$$
$$
$$
```

---

## §3 (C-2) 双计数为何退化为恒等式（诊断 ✓）

```
$$\textbf{用户的映射}:\ \text{孤立}\ c\ \text{的邻点}\ y=c+e_i\ \text{若}\ b(y)=2\ \Longrightarrow\ \text{唯一第二中心}\ c'=c+e_i+e_j\ (d(c,c')=2)\ ✓$$
$$\textbf{容量侧}:\ \text{距}\ c\ \text{为 2 的码字}\ c'=c+e_i+e_j\ \text{恰服务}\ c\ \text{的两个邻点}\ y_i,y_j\ \Longrightarrow\ \text{每}\ c'\ \text{至多服务 2 个}\ ✓$$
$$\textbf{需要侧}:\ k(c):=\#\{y\in N(c):b(y)=2\}\ ✓\ \text{而由 (C-1)}:\ \underbrace{k(c)+2[\![z\in N(c)]\!]}_{=\sum(b-1)\ \text{按重数}} = 2a_2(c)\ ✓$$
$$\qquad\Longrightarrow\ \boxed{k(c)=2a_2(c)-2[\![z\in N(c)]\!]}\ \Longrightarrow\ \text{需要侧与容量侧\textbf{常数比恰为 2}}\ \Longrightarrow\ r=2,\ s=2\ \Longrightarrow\ 2I\le2A_2\ \text{型恒等}\ ✗$$
$$\Longrightarrow\ \textbf{诊断}:\ \text{任何"孤立码字的}\ b{=}2\ \text{邻点"\ ×\ "距离-2 码字"的双计数，都被 (C-1) 钉成恒等式}\ ✗✓$$
$$
$$
```

---

## §4 (C-3) 新界 $a_2(c)\le5$（本档副作用，可复用 ✓）

```
$$\textbf{隐私量}:\ \#\mathrm{priv}(c):=\#\{y\in B_1(c):\ y\ \text{仅被}\ c\ \text{覆盖}\}\ ✓$$
$$\qquad=\ \underbrace{[\![d_1(c)=0]\!]}_{c\ \text{自身}}\ +\ \#\{y\in N(c):b(y)=1\}\ ✓$$
$$\qquad=\ [\![d_1=0]\!]+\Big(10-\sum_{y\in N(c)}(b(y)-1)\Big)+\underbrace{\#\{y\in N(c):b(y)=3\}}_{=[\![z\in N(c)]\!]\ \text{（唯一 }b{=}3\text{ 点）}}\ ✓$$
$$\qquad=\ [\![d_1(c)=0]\!]+10-d_1(c)-2a_2(c)+[\![z\in N(c)]\!]\ \ \ge\ 0\ ✓$$
$$\textbf{取两情形}:\ d_1=0:\ 11-2a_2(c)\ge0\Rightarrow a_2\le5.5\Rightarrow\mathbf 5\ ✓;\quad d_1=1:\ 9-2a_2(c)\ge0\Rightarrow a_2\le4.5\Rightarrow\mathbf 4\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\forall c:\ a_2(c)\le\mathbf 5}\ ✓✓\quad(\text{新，可复用；下界侧无非平凡界}\ ✗)$$
$$\Longrightarrow\ \sum_c a_2(c)=2A_2\ \le\ 5M=595\ \Longrightarrow\ A_2\le297\ ✗\ \text{（对}\ A_2\ge84\ \text{无碰撞力）}\ ✓\ \text{诚实标注为弱界}$$
$$
$$
```

**全局隐私计数（核验用 ✓）**：

```
$$\sum_c\#\mathrm{priv}(c)=I+10M-2A_1-4A_2+\#\{c:z\in N(c)\}=(119-2A_1)+1190-2A_1-4A_2+3$$
$$\qquad=1312-4(A_1+A_2)=1312-4\times143=\mathbf{740}\ ✓✓\quad\text{分支 B}:\ \sum_c[\![z\in N(c)]\!]=d_1(z)=2\ \Longrightarrow\ \text{亦得}\ \mathbf{740}\ ✓✓$$
$$\qquad\Longleftrightarrow\ \text{档案 Q=1 profile 的}\ \textbf{740}\times\{\delta=0\}\ \text{即私有点}\ ✓✓
$$
$$\textbf{诚实注}:\ \text{“私有点}\iff b=1\text{”\textbf{是定义等价的}\ ✓\ —— 故 740 并非新信息，本式仅作\textbf{恒等式自检}\ ✓✓$$
$$
$$
```

---

## §5 诚实判定（依唐先生 B-3 目标 ✓）

```
$$\textbf{目标}:\ rI\le sA_2\ \Longrightarrow\ \text{与}\ I=119-2A_1,\ A_2=143-A_1\ \text{联立得}\ A_1\ \text{下界}\ ✓$$
$$\textbf{实测}:\ r/s=2/2=1\ \text{（恒等式）}\ ✗\ \Longrightarrow\ \text{代入得}\ \sum a_2\le 5M\ \text{型弱界}\ ✗\ \text{无碰撞}\ ✗$$
$$\textbf{另一支（private capacity）}:\ 11I\le1309\Rightarrow I\le119\ ✗\ \text{（用户已指出，同样太松）}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{B-3 未获}\ A_1\ \text{下界}\ ✗}\ ——\ \text{与 GRAMSIGN／SUM-P1P4 的"incidence/矩层饱和"结论\textbf{第三次汇合}}\ ✓✓$$
$$
$$
```

---

## §6 本档真正的产出（供后续复用 ✓）

```
$$\textbf{① off-by-one 修正}:\ I(B)=120-2A_1\ ✓\ \text{（且分支 B 不强制}\ I\ge1\ ✓）$$
$$\textbf{② 局部恒等式 (C-1)}:\ \sum_{y\in N(c)}(b(y)-1)=d_1(c)+2a_2(c)\ ✓\ \text{（"c 周围 excess ＝ 内部度 ＋ 两倍距离-2 度"）}$$
$$\textbf{③ 新界}:\ a_2(c)\le5\ \forall c\ ✓;\ \text{等价形式}:\ \#\mathrm{priv}(c)=[\![d_1=0]\!]+10-d_1(c)-2a_2(c)+[\![z\in N(c)]\!]\ \ge0\ ✓$$
$$\textbf{④ 诊断（最有价值）}:\ \text{凡把"码字周围 excess"与"局部距离-2 度"配对的\emph{任何}双计数，必被 (C-1) 钉成恒等式}\ ✗✓$$
$$\qquad\Longrightarrow\ \textbf{下一步应换资源对}：不能再配 (excess, a_2)，须配\ \text{某对\emph{不被同一条恒等式联系}的量}\ ⚠️$$
$$
$$
```

---

## §7 候选的"未绑定资源对"（列出，未执行 ✓）

```
$$\textbf{P-1}:\ \text{中点（}b{=}2\ \text{非码字）} \times \text{距离-2 对}\ ——\ \text{但已由}\ 2A_2=3+(283-2A_1)\ \text{绑定}\ ✗$$
$$\textbf{P-2}:\ \text{私有点（}b{=}1\text{）} \times \text{码字度}\ ——\ \text{由 (C-1) 绑定}\ ✗$$
$$\textbf{P-3}:\ \text{局部 \textbf{三元/四元}结构（如 2 维面、贴面立方）} \times \text{层位置}\ ——\ \text{档案有 "square" 线（}4S_q\le Q_2\ ✓\ \text{在 (9,62) 线）}\ ⚠️\ \text{未在 119 线登记}$$
$$\textbf{P-4}:\ \text{z 的 3 个码邻的\emph{内部}关系（}e_1,e_2,e_3\ \text{两两距离 2）} \times \text{它们各自的匹配伙伴/度}\ ⚠️\ \text{未查}$$
$$
$$
```

---

## §8 边界（诚实标注）

- §1 的 off-by-one 修正为**本档新纠** ✓（分支 B：$I=120-2A_1$ ✓）
- §2 的 (C-1) 为**严格推导** ✓（用 $|B_1\cap B_1|=(11,2,2,0)$ 与 $|N(c)\cap B_1(c')|$ 的对应 ✓）
- §3 的退化判定为**本档结论** ✓（$r=s=2$ ✓）
- §4 的 $a_2\le5$ 为**本档新推导** ✓；其弱性已诚实标注 ✓；740 的核验 ✓ 与档案 profile 一致 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 孤立码字-距离2度双计数退化 命中文件数=1    :: ./ISOB3-2026-09-26-isolated-codewords-versus-distance-two-degree.md 
技术词 周围 excess 恒等式 命中文件数=1    :: ./ISOB3-2026-09-26-isolated-codewords-versus-distance-two-degree.md 
技术词 隐私量恒等式 命中文件数=1    :: ./ISOB3-2026-09-26-isolated-codewords-versus-distance-two-degree.md
```
- **本档新增**：孤立码字-距离2度双计数退化、周围 excess 恒等式、隐私量恒等式（见上方命中数）
- **档案已有（引用，不列为提出）**：$A_1+A_2=143$、$I$、740 profile
