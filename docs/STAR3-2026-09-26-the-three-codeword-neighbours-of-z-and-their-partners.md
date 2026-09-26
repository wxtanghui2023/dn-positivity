已查地图：已跑 scripts/prework_map_check.sh K(10,1) z 码邻 匹配伙伴 邻域交集 ⟹ 执行自 `docs/ISOB3-2026-09-26-...md`（(C-1) 恒等式 ✓）＋ `docs/PACKB-2026-09-26-...md`（匹配定理与 A₁≤59/60 ✓）＋ `docs/F14-DEDUP-2026-09-26-...md`（F 表 ✓）；本档为**纯推导**（唐先生 2026-09-26 20:00 指令「开 P-4，第一刀做 Type I/II/III 精确交集分类」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支中 `z` 的三个码邻及其匹配伙伴的局部构型（既有对象；非新对象）
D1: 0（产出为一处设定修正、Type 无关性定理、新强制量与新层界）

# STAR3-2026-09-26 · z 的三个码邻与匹配伙伴：Type 分类与新增强制量

## §0 结论（先给）

```
$$\boxed{\textbf{(D-0 设定修正)}\ \text{“}d_1(e_i)=1\text{”\textbf{不成立}}\ ✗:\ \text{由}\ Q=1\ \text{只能得}\ d_1(e_i)\in\{0,1\}\ ✓\ (\text{两分支})}$$
$$\qquad\text{故须分}\ \textbf{matched}\ (d_1=1,\ \text{伙伴}\ p_i)\ \text{与}\ \textbf{unmatched}\ (d_1=0,\ \text{孤立码字})\ ✓✓$$
$$\boxed{\textbf{(D-1)}\ \text{matched}\ \Longrightarrow\ p_i=e_i+e_j\ (j\ge4),\ \text{且}\ p_i\ \text{强制产生}\ \mathbf 6\ \text{个\textbf{全新}}\ L_3\ \text{非码字}\ ✓✓}$$
$$\boxed{\textbf{(D-2 Type 无关性定理)}\ \text{Type I/II/III 的“重合点”恰好全部落在既有}\ F_3\ (\text{可由 z 饱和推出})\ \Longrightarrow\ \textbf{三类新增量相同，均为 6/partner}\ ✓✓}$$
$$\boxed{\textbf{(D-3)}\ \text{新层界}\ |C\cap L_3|\le\mathbf{80}\ ✓;\ \text{强制非码字总数}\ 32\to\mathbf{50}\ ✓\ (\text{仍}\ll905\ ✗)}$$
$$\boxed{\textbf{(D-4)}\ \textbf{无}\ b=1\ \text{强制量}\ ✗\ \Longrightarrow\ \text{按唐先生预设判据：P-4 判弱}\ ✓\ (\text{但产出非定义性、是真新量}\ ✓)}$$
$$
$$
```

---

## §1 (D-0) 设定修正（用户 P-4.1 的一处非续推）

```
$$\textbf{用户}:\ \text{“}e_i\ \text{不能成为唯一}\ \delta{=}2\ \text{点}\ \Longrightarrow\ d_1(e_i)=1"\ ✗$$
$$\qquad\text{实情}:\ \delta(e_i)=d_1(e_i)\ ✓;\ \text{要}\ \delta=2\ \text{需}\ d_1=2\ ✗;\ \text{而}\ d_1=0\ \text{与}\ Q=1\ \text{完全相容}\ ✓✓$$
$$\textbf{故正确二分}:\ \begin{cases}\textbf{matched}:&d_1(e_i)=1,\ \text{唯一伙伴}\ p_i\ (d(e_i,p_i)=1)\ ✓\\ \textbf{unmatched}:&d_1(e_i)=0\ \Longrightarrow\ e_i\ \text{是孤立码字}\ ✓\ (\text{计入}\ I)\ ✓\end{cases}$$
$$\textbf{unmatched 情形的一个副产品}:\ \text{由 (C-1)}:\ \sum_{y\in N(e_i)}(b(y)-1)=0+2a_2(e_i)\ ✓\ \text{而}\ z\in N(e_i)\ \text{贡献 2}\ ✓$$
$$\qquad\Longrightarrow\ 2+(\text{其余 9 邻之和})\ \ge\ 2\ \Longrightarrow\ \boxed{a_2(e_i)\ \ge\ 1}\ ✓✓\ (\text{即使无伙伴，}e_i\ \text{仍有距离-2 码字邻}\ ✓)$$
$$
$$
```

---

## §2 (D-1) matched 情形的完整强制表（本档核心）

```
$$\textbf{伙伴位置}:\ p_i\ \text{与}\ e_i\ \text{距 1}\ ✓,\ p_i\ne z\ \Longrightarrow\ p_i\in\{e_i+e_j\}\ \cup\ \{e_i+e_j+e_l\}\ \text{型}\ ✓$$
$$\qquad\text{但}\ \{e_i+e_j:j\in\{1,2,3\}\setminus\{i\}\}=y_{ij}\ \textbf{已强制非码字}\ ✓\ (\text{① 表}\ ✓)\ \Longrightarrow\ \boxed{p_i=e_i+e_j,\ j\in\{4,\dots,10\}}\ ✓✓$$
$$\textbf{伙伴的度}:\ d_1(p_i)=1\ (\text{仅}\ e_i)\ \Longrightarrow\ b(p_i)=1+d_1=2\ \Longrightarrow\ B_1(p_i)\ \text{中恰 2 个码字}\ (p_i,e_i)\ ✓$$
$$\qquad\Longrightarrow\ \text{其余 9 点强制非码字}\ ✓:\quad B_1(p_i)=\{p_i\}\cup\underbrace{\{e_i,e_j\}}_{\text{2 点}}\cup\{e_i+e_j+e_l:l\notin\{i,j\}\}\ ✓$$
$$\qquad\Longrightarrow\ \underbrace{\{e_j\}}_{\text{① 已强制}}\cup\underbrace{\{e_i+e_j+e_l:l\notin\{i,j\}\}}_{8\ \text{点}}\ \text{全非码字}\ ✓$$
$$\textbf{其中 8 点的细分（关键）}:\ l\in\{1,2,3\}\setminus\{i\}\ (2\ \text{个})\ \text{给}\ y_{ii'}+e_j\ \in\ \textbf{既有}\ F_3\ ✓;\quad l\ge4,l\ne j\ (6\ \text{个})\ \text{给}\ \{i,j,l\}\ \textbf{全新}\ ✓✓$$
$$\qquad(\{i,j,l\}\ \text{含恰一个}\ \{1,2,3\}\ \text{元素}\ \Longrightarrow\ \textbf{必不在}\ F_3\ (\text{需}\ \ge2)\ ✓✓)$$
$$\Longrightarrow\ \boxed{\text{每个 matched}\ e_i\ \text{贡献}\ \mathbf 6\ \text{个全新}\ L_3\ \text{非码字}}\ ✓✓$$
$$
$$
```

---

## §3 (D-2) Type I/II/III 的精确交集 —— **三类同值**（本档最有价值的结构发现 ✓）

```
$$\text{记}\ S_i:=\{e_i+e_j+e_l:\ l\ge4,\ l\ne j\}\ (6\ \text{点},\ p_i=e_i+e_j\ ✓);\quad \text{外部坐标}\ j_i=\sigma(i)\in\{4,\dots,10\}\ ✓$$
$$\textbf{普适结论}:\ \text{对}\ i\ne i',\ S_i\cap S_{i'}=\varnothing\ \text{（\textbf{与 Type 无关}）}\ ✓✓$$
$$\qquad\text{证}:\ \text{设}\ \{i,j_i,l\}=\{i',j_{i'},l'\}\ ✓\ \text{则}\ i'\in\{i,j_i,l\}\ ✓;\ i'\ne i\ ✓;\ i'\ne j_i\ (\text{因}\ j_i\ge4>3\ge i')\ ✓\ \Longrightarrow\ i'=l\ ✗\ (\text{但}\ l\ge4>3\ge i')\ ✓✓$$
$$\textbf{而更早一步的 8 点集}\ \{e_i+e_j+e_l:l\notin\{i,j\}\}\ \text{的重合点}:\ \text{恰为}\ \{i,i',j\}\ (i'\ne i)\ ✓\ \text{且属于}\ F_3\ ✓$$
$$\qquad\text{证}:\ \{i,j_i,l\}=\{i',j_{i'},l'\}\ \text{同前推得}\ l=i',\ l'=i\ \Longrightarrow\ \{i,i',j_i\}=\{i,j_{i'},i\}\ \Longrightarrow\ j_i=j_{i'}\ ✓$$
$$\qquad\Longrightarrow\ \text{重合}\iff\sigma(i)=\sigma(i')\ ✓\ \text{且重合点}=\{i,i',j\}\ (\in F_3\ ✓)$$
$$\Longrightarrow\ \begin{array}{c|c|c|c}
\text{Type} & |S^8_1\cup S^8_2\cup S^8_3| & \text{其中}\ \in F_3 & \textbf{全新}\ \\ \hline
\text{I（全异）} & 24 & 6 & \mathbf{18}\\
\text{II（恰两个同）} & 24-1=23 & 5 & \mathbf{18}\\
\text{III（全同）} & 24-3=21 & 3 & \mathbf{18}\ (\text{该型由 §4 另行排除}\ ✓)\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{三类\textbf{全新量恒为}\ 18}\ (6\times3)\ ✓✓\ —— \text{Type 分类对计数\textbf{无影响}}\ ✓}$$
$$
$$
```

**⚠️ 诚实说明**：用户在 P-4.4 已预警「不能错误宣布 partner 坐标必须不同」 ✓ —— **该预警正确** ✓："
Three Type II 完全合法 ✓（Type III 由 §4 另行排除 ✓）；且本档证明其新增量与 Type I **同值（18）** ✓✓。

---

## §4 Type II/III 的一个真实结构后果（附带发现，可入账 ✓）

```
$$\textbf{Type II}（\sigma(1)=\sigma(2)=j\ne\sigma(3)=k\ ✓）:\ e_j\ \text{同时被}\ p_1,p_2\ \text{覆盖}\ ✓\ (d(e_j,p_i)=1\ ✓)\ \Longrightarrow\ b(e_j)\ \ge\ 2\ ✓$$
$$\qquad\text{而}\ e_j\ne z\ \Longrightarrow\ b(e_j)\le2\ \Longrightarrow\ \boxed{b(e_j)=2\ \text{恰等}}\ ✓✓$$
$$\qquad\Longrightarrow\ \{p_1,p_2\}\ \text{相距 2}\ (d(p_1,p_2)=2\ ✓)\ \text{且}\ e_j\ \text{是其中点}\ ✓;\ \text{另一中点}=\{1,2\}=y_{12}\ ✓$$
$$\qquad\Longrightarrow\ b(y_{12})=2\ ✓\ \text{与①表一致}\ ✓✓\ (\text{互相验证：中点结构自洽}\ ✓)$$
$$\textbf{Type III}（\sigma\ \text{全同}=j\ ✓）:\ b(e_j)\ge3\ \text{（被}\ p_1,p_2,p_3\ \text{覆盖）}\ \Longrightarrow\ b(e_j)\ge3\ \textbf{与}\ b\le3\ \text{及“唯一}\ b{=}3\ \text{点是}\ z"\ \text{相容}\iff e_j=z\ ✗\ (\text{不可})\ ✗✗$$
$$\qquad\Longrightarrow\ \boxed{\textbf{Type III 不可能}}\ ✓✓\ —— \text{即}\ \sigma(1)=\sigma(2)=\sigma(3)\ \text{被排除}\ ✓✓$$
$$
$$
```

**⟹ 这是一个真正的排除** ✓：**三个伙伴的外部坐标不可能全同** ✓（否则 $L_1$ 点 $e_j$ 会被三个码字覆盖 $\Rightarrow b\ge3$ $\Rightarrow$ 出现第二个 $b=3$ 点 $\Rightarrow$ 与 $Q=1$ 矛盾 ✓✓）。
⟹ 故实际只有 **Type I 与 Type II** ✓，且两者新增量相同（18 ✓）✓。

---

## §5 (D-3) 更新后的强制计数与层界

```
$$\textbf{分支 A（三个都 matched 时最大）}:\ \text{强制非码字} = 7(L_1)+3(L_2)+\underbrace{22}_{F_3}+\underbrace{18}_{\text{P-4}}\ =\ \mathbf{50}\ ✓\ (\text{原 32})$$
$$\qquad\Longrightarrow\ |C\cap L_3|\ \le\ 120-40\ =\ \boxed{\mathbf{80}}\ ✓\ (\text{新层界})$$
$$\textbf{条件性收紧（unmatched 数}\ u\ ✓）:\ I\ge u\ \text{且}\ I=119-2A_1\ \Longrightarrow\ 2A_1\le119-u\ \Longrightarrow\ \begin{cases}u=0,1:&A_1\le59\\ u\ge2:&\boxed{A_1\le58}\ ✓\end{cases}$$
$$
$$
```

---

## §6 (D-4) 判定（依唐先生预设判据 ✓）

```
$$\textbf{产出性质}:\ \text{新增 18 个强制非码字是\textbf{真新量}}（\text{非定义性、非 (C-1) 型恒等式}\ ✓）\ —— \text{比 ① 的表更进一步}\ ✓$$
$$\textbf{但}:\ \text{这 18 点的}\ b\ \text{值 ∈\{1,2\}\ 未被钉住}\ ✗\ \Longrightarrow\ \textbf{无 b=1 强制量}\ ✗$$
$$\textbf{故（用户判据）}:\ \text{“若只产生定义性计数或恒等式则判弱；若出现严格新增 }b{=}1\ \text{强制量则继续”}\ ✓$$
$$\qquad\Longrightarrow\ \text{P-4 落入}\ \textbf{判弱}\ ✗\ \text{（18}\ll\text{905};\ \text{与 }b{=}1\ \text{配额 620+2A}_1\ \text{无碰撞力）}\ ✓$$
$$\textbf{保留资产（不丢）}:\ \text{① Type III 不可能}\ ✓✓\ \text{② }p_i\in L_2\ \text{且}\ p_i=e_i+e_j\ (j\ge4)\ ✓\ \text{③ 每 partner 强制 6 个全新}\ L_3\ \text{点}\ ✓\ \text{④ }|C\cap L_3|\le80\ ✓\ \text{⑤ 条件界}\ A_1\le58\ (u\ge2)\ ✓$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 的修正为**本档新纠** ✓（用户 P-4.1 的"$d_1(e_i)=1$"为非续推 🔴）
- §2–§3 为**严格推导** ✓；(D-2) 的 Type 无关性为**本档定理** ✓ ✓；用户的 P-4.4 预警被证实正确 ✓
- §4 的 **Type III 排除**为**本档新结论** ✓✓（机制：$b(e_j)\ge3\Rightarrow$ 第二个 $b=3$ 点 ✓）
- §5 的计数为**逐层去重后**（跨层不交已证 ✓；层内重叠已按 §3 处理 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Type 无关性定理 命中文件数=1    :: ./STAR3-2026-09-26-the-three-codeword-neighbours-of-z-and-their-partners.md 
技术词 伙伴六点强制 命中文件数=1    :: ./STAR3-2026-09-26-the-three-codeword-neighbours-of-z-and-their-partners.md 
技术词 Type III 排除  命中文件数=1    :: ./STAR3-2026-09-26-the-three-codeword-neighbours-of-z-and-their-partners.md
```
- **本档新增**：Type 无关性定理、伙伴六点强制、Type III 排除（见上方命中数）
- **档案已有（引用，不列为提出）**：$F_3$ 表、$A_1\le59/60$、$b\le3$ 与唯一 $b{=}3$ 点
