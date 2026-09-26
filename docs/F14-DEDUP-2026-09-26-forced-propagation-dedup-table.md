已查地图：已跑 scripts/prework_map_check.sh K(10,1) Q=1 F₁→F₄ 去重传播 ⟹ 执行自 `docs/Q1-LOCAL-CLASSIFICATION-2026-09-25-forced-T-centers.md`（A/B 分支 forced 表原档 ✓）＋ `docs/TRACE-287-2026-09-26-...md`（287 溯源 ✓）；本档为**纯推导**（唐先生 2026-09-26 19:38 指令「接着做 ①，只做 F₁→F₄ 去重传播表，纯推导，不跑程序」✓）；**未跑程序** ✓；**不碰 A23／新 frontier／solver** ✓。
D0: 本档对象 = `Q=1` 分支的 `F₁→F₄` 强制传播（去重口径）＋ 层码字容量上界（既有对象；非新对象）
D1: 0（无新独立自由度；产出为去重表、跨层不交判定、层容量上界与恒等式对接）

# F14-DEDUP-2026-09-26 · F₁→F₄ 去重传播表（纯推导）

## §1 设定与两条禁忌（逐字随档案）

```
$$Q=1\ \text{分支}:\ \text{唯一}\ \delta\text{-2 点}\ z\ (\text{即}\ b(z)=3)\ ✓;\quad \forall x\ne z:\ b(x)\le2\ ✓;\quad |C|=119,\ n=10\ ✓$$
$$\text{层}: L_i:=L_i(z)=\{y: d(z,y)=i\};\ |L_1|{=}10,\ |L_2|{=}45,\ |L_3|{=}120,\ |L_4|{=}210\ ✓$$
$$\textbf{禁忌①}:\ \text{各层 forced 数\textbf{不得直接相加}}\ \text{（层间重叠会造假突破）};\qquad \textbf{禁忌②}:\ A/B\ \textbf{不得混算}\ ✓$$
$$
$$

## §2 传播的五条规则（本档显式化，便于去重记账）

```
$$\textbf{R1}:\ x\ne z\Longrightarrow b(x)\le 2;\quad b(z)=3\ ✓\qquad(\text{来自 }Q=1)$$
$$\textbf{R2}:\ \forall x:\ b(x)\ge 1\ ✓\qquad(\text{覆盖条件})$$
$$\textbf{R3}:\ c\in C\Longrightarrow \delta(c)=b(c)-1=\deg_C(c)\ ✓\qquad(\text{码字自身计入其球})$$
$$\textbf{R4}:\ c\in C,\ c\ne z\Longrightarrow \deg_C(c)\le 1;\quad \deg_C(z)=2\ ✓\qquad(\text{由 R1+R3})$$
$$\textbf{R5（饱和）}:\ b(x)=k\Longrightarrow |C\cap B_1(x)|=k\ \Longrightarrow\ B_1(x)\ \text{中恰}\ 11-k\ \text{点非码字}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{记账口径}:\ \text{强制的是「区内码字\textbf{至多}\ k\ 个」＝\textbf{容量型}约束，不是「某点必非码字」的\textbf{点名型}约束}\ ✓✓$$
$$
$$
```

**⚠️ 本档的关键口径判定（决定去重怎么做）**：

```
$$\text{R5 的直接后果不是"某点被点名”，而是"某个球内码字数有上界”}\ \Longrightarrow\ \text{同一非码字点会被}\ \textbf{多个球的容量}同时"排除”}\ ✓$$
$$\Longrightarrow\ \textbf{去重对象是"非码字点的\textbf{集合}”，而非"容量计数”}\ ✓;\ \text{容量型下界只能按\textbf{并集}清点}\ ✓✓$$
$$
$$
```

---

## §3 分支 A（$z\notin C$）：F₁→F₄ 表

**记号**：WLOG $z=\varnothing$；$N(z)\cap C=\{e_i,e_j,e_k\}=\{e_1,e_2,e_3\}$（$i,j,k$ 互异 ✓）。

| 层 | 点名型强制（distinct） | 计数 | 依据 |
|---|---|---|---|
| $F_1$ | $e_4,\dots,e_{10}$ | **7** | $b(z)=3$ ⟹ 其余 7 邻非码字 ✓ |
| $F_2$ | $y_{12},y_{13},y_{23}$（$y_{ab}:=e_a\oplus e_b$） | **3** | $\{e_a,e_b\}$ 距 2 ⟹ 公共中心仅 $z,y_{ab}$；$y_{ab}\in C\Rightarrow b\ge3\Rightarrow\delta=2$ 与唯一性冲突 ⟹ $y_{ab}\notin C$ ✓ |
| $F_3$ | $\{e_a\oplus e_b\oplus e_c\}$ 之并 | **22** | $b(y_{ab})=2$ 恰饱和（R5，$k=2$）⟹ 其另外 8 邻非码字；三组 $3\times8=24$，共同点 $e_1\oplus e_2\oplus e_3$ 三重计 ⟹ $24-3+1=\mathbf{22}$ ✓ |
| $F_4$ | — | **0** | 无点名型强制 ✗ |

$$\text{层内去重明细（此即"去重"的实质）}:$$
$$\quad \bigcup_{a<b}\{y_{ab}\oplus e_c: c\notin\{a,b\}\}\ =\ \underbrace{\{123\}}_{\text{三组公有}}\ \cup\ \underbrace{\{12c:c\ge4\}}_{7}\ \cup\ \underbrace{\{13c:c\ge4\}}_{7}\ \cup\ \underbrace{\{23c:c\ge4\}}_{7}\ =\ 1+21=\mathbf{22}\ ✓$$
$$
$$

## §4 分支 B（$z\in C$）：F₁→F₄ 表

**记号**：$\delta(z)=\deg_C(z)=2$ ⟹ 恰两码邻 $u=e_1,v=e_2$ ✓。

| 层 | 点名型强制 | 计数 | 依据 |
|---|---|---|---|
| $F_1$ | $e_3,\dots,e_{10}$ | **8** | $z$ 的其余 8 邻非码字 ✓ |
| $F_2$ | $w=e_1\oplus e_2$ | **1** | $\{u,v\}$ 距 2 ⟹ 公共中心 $z,w$；$w\in C$ 则 $\deg(w)\ge2$（$u,v$）⟹ $\delta(w)\ge2$ ✗ ⟹ $w\notin C$ ✓ |
| $F_3$ | $\{e_1\oplus e_2\oplus e_c: c\ge3\}$ | **8** | $b(w)=2$ 饱和（R5）⟹ 其余 8 邻非码字 ✓ |
| $F_4$ | — | **0** | 无 ✗ |

$$
$$

## §5 ✅ **跨层去重判定（禁忌①的实质检验）**

```
$$\textbf{结论}: \boxed{F_i\subseteq L_i\ \text{且}\ \{L_i\}\ \text{两两不交}\ \Longrightarrow\ \textbf{跨层零重叠}\ \Longrightarrow\ ①\ \text{下"直接相加"在本表内\textbf{安全}}\ ✓✓}$$
$$\qquad\text{理由}: d(z,\cdot)\ \text{是良定义的整数层函数, 每个点只属于一个}\ L_i\ ✓$$
$$\textbf{故本表的总强制（真并集）}: \text{分支 A} = 7+3+22+0 = \mathbf{32};\quad \text{分支 B} = 8+1+8+0 = \mathbf{17}\ ✓✓\ (\text{与档案一致}\ ✓)$$
$$\textbf{⚠️ 但禁忌①的真实风险在\textbf{第二代}（见 §6）：新产生的强制集合发生\textbf{同层多证}与\textbf{跨层回流}时，相加立刻失真}\ ✗$$
$$
$$
```

---

## §6 ⭐ **第二代的硬产物：$L_2$ 码字容量上界 ≤ 10**（本档新增推导 ✓）

```
$$\textbf{第二代机制}: F_1\ \text{的 7 个非码字}\ e_l\ (l\ge4)\ \text{本身受 R1/R2 约束}\ \Longrightarrow\ \text{其球内码字容量受限}\ ✓$$
$$\text{对}\ l\ge4:\ B_1(e_l)=\{e_l\}\cup\{z\}\cup\{\{l,m\}: m\ne l\}\quad(1+1+9=11\ ✓);\quad e_l\notin C,\ z\notin C\ (\text{分支 A}\ ✓)$$
$$\Longrightarrow\ b(e_l)=\#\{m:\{l,m\}\in C\}\ \le\ \mathbf 2\ \Longrightarrow\ \textbf{每行}\ l\ \text{至多 2 个"格点"}\{l,m\}\ \text{是码字}\ ✓$$
$$\textbf{同理}\ e_m\ (m\in\{1,2,3\})\in C\ \Longrightarrow\ \deg(e_m)\le1\ \Longrightarrow\ \text{每行}\ m\ \text{至多 1 个}\{m,l\}(l\ge4)\ \text{是码字}\ ✓$$
$$
$$
```

**清点 $L_2$ 的码字（45 点分三类）**：

```
$$\text{① }\{a,b\}\subseteq\{1,2,3\}\ (3\ \text{点}=y_{ab}):\ \textbf{全部非码字}\ ✓\ (\text{点名型}\ ✓)$$
$$\text{② }\{m,l\},\ m\in\{1,2,3\},\ l\ge4\ (21\ \text{点}):\ \text{每行 }m\ \text{至多 1}\ \Longrightarrow\ \le\mathbf 3\ \text{个码字}\ ✓$$
$$\text{③ }\{l,m\},\ l,m\ge4\ (21\ \text{点}):\ \text{每行}\ l\ \text{至多 2}\ \Longrightarrow\ \text{两侧计数}\ 2\#\le 7\times2\ \Longrightarrow\ \#\le\mathbf 7\ \text{个码字}\ ✓$$
$$\Longrightarrow\ |C\cap L_2|\ \le\ 0+3+7\ =\ \boxed{\mathbf{10}}\ ✓✓\qquad(\text{等价}: |F_2^{\text{真}}|\ \ge\ 45-10\ =\ \mathbf{35}\ \text{个非码字}\ ✓)$$
$$
$$
```

**分支 B 的对应清点**（$\deg(u)=\deg(v)=1$ 且其唯一邻居是 $z$ ⟹ 更强的行约束）：

```
$$u=e_1,v=e_2\ \text{的行}: \deg=1\ \text{已被}\ z\ \text{用尽}\ \Longrightarrow\ \{1,l\},\{2,l\}\ (l\ge3)\ \textbf{全部非码字}\ ✓\ (\text{点名型}\ )\ \Longrightarrow\ \text{21 点全非码字}\ ✓$$
$$\{l,m\},l,m\ge3\ (28\ \text{点}):\ \text{每行}\ l\ \text{至多 2}\ (b(e_l)\le2\ ✓)\ \Longrightarrow\ \#\le 8\times2/2=8\ \Longrightarrow\ |C\cap L_2|\le 0+0+8=\mathbf 8\ ✓$$
$$
$$
```

---

## §7 ⭐ **把强制计数与 census 精确对接（新恒等式，本档推导 ✓）**

```
$$\textbf{双层求和}:\ \sum_{x}b(x)=\sum_x|C\cap B_1(x)|=\sum_{c\in C}|B_1(c)|=11M=1309\ ✓$$
$$\text{而}\ \sum_{c\in C}b(c)=M+2A_1\ \Longrightarrow\ \sum_{x\notin C}b(x)=11M-M-2A_1=\boxed{10M-2A_1}\ ✓\ (M=119\Rightarrow \mathbf{1190-2A_1})$$
$$\textbf{非码字总数} = 2^{10}-M = 1024-119=\mathbf{905}\ ✓;\ \text{且每个非码字}\ b\in\{1,2\}\ ✓$$
$$\Longrightarrow\ \boxed{\#\{x\notin C:\ b(x)=2\}\ =\ (1190-2A_1)-905\ =\ \mathbf{285-2A_1}\ =\zeta\ \ge0}\ ✓✓\ (\text{即档案的 surfeit 型量}\ \zeta\ ✓)$$
$$\qquad\boxed{\#\{x\notin C:\ b(x)=1\}\ =\ 905-\zeta\ =\ \mathbf{620+2A_1}}\ ✓$$
$$
$$
```

**⟹ 强制计数与 census 的对接口**：$F_1\cup F_2\cup F_3$ 里的每一点都必须是 **$b=1$ 或 $b=2$ 的非码字** ✓ ⟹ 全部计入 $905$ ✓ 的被点名部分 ✓；
而 $b=2$ 的名额只有 $\zeta=285-2A_1$ 个 ✓ ⟹ **若某分支的点名型强制中"必为 $b=2$"者超过 $\zeta$，即得矛盾** ✓✓ —— **这是本档给出的、可直接检验的唯一闭合口** ✓。

```
$$\text{本表内"必为}\ b=2\text{"的点}: \text{分支 A 仅}\ y_{12},y_{13},y_{23}\ (3\ \text{个}\ ✓);\ \text{分支 B 仅}\ w\ (1\ \text{个}\ ✓)$$
$$\Longrightarrow\ \text{需}\ \zeta\ge3\ (\text{A})/\ \zeta\ge1\ (\text{B})\ \Longleftrightarrow\ A_1\le141\ (A)/\ A_1\le142\ (B)\ ✓\ ——\ \text{与已知}\ A_1\le142\ \text{相容}\ ✗\ (\text{不出矛盾})$$
$$
$$
```

---

## §8 诚实结论（不制造假上界 ✓）

```
$$\textbf{① 表已完成}: \text{分支 A}: 7/3/22/0\ (\text{并集 32});\ \text{分支 B}: 8/1/8/0\ (\text{并集 17})$$
$$\textbf{② 禁忌①}:\ \text{跨层零重叠（}\S 5\ \text{证}）\Longrightarrow\ \text{表内可加}\ ✓;\ \textbf{风险只在第二代}\ ✗$$
$$\textbf{③ 第二代硬产物}:\ |C\cap L_2|\le 10\ (\text{A})/\ \le 8\ (\text{B})\ ✓✓\ ——\ \text{这是\textbf{层容量上界}，方向正确（要证的是整体}\le119\ ✓)$$
$$\textbf{④ 仍未闭合}\ ✗:\ \text{局部点名型强制}\ 32/17\ \ll\ 905\ ✗;\ \text{容量上界单层也不足以压 119}（L_2\le10\ \text{对总分几乎无影响}）\ ✗$$
$$\textbf{⑤ 唯一可用闭合口（本档定位）}:\ \zeta=285-2A_1\ \text{的名额限制}\ \times\ \text{"必为 }b{=}2\text{" 的点数}\ \Longrightarrow\ \text{当前不够，需推广到第二代} ✓$$
$$
$$
```

---

## §9 下一步（按本档定位，未执行 ✓）

```
$$\textbf{①'} \text{把 §6 的行容量法推广到 } L_3,L_4,\dots:\ \text{由}\ \{b(x)\le2\}\ \text{对}\ \textbf{每个已点名非码字}\ \text{给出一行约束}\ \Longrightarrow\ \text{逐层码字容量上界表}\ ✓$$
$$\qquad\textbf{目标}: \sum_i |C\cap L_i|\ \text{的上界与}\ 119\ \text{对比}\ ——\ \text{若}<119\ \text{即闭合}\ ✓✓$$
$$\textbf{②'} \text{"必为 }b{=}2\text{" 的第二代清点}\ \times\ \zeta\ \text{名额}\ \Longrightarrow\ \text{对}\ A_1\ \text{的进一步上界}\ ✓$$
$$\textbf{禁忌重申}:\ \text{逐层容量\textbf{不得}直接相加成码字总数}\ ✗\ (\text{层间有覆盖重叠}\ ✓)\ ——\ \text{须按 ball 双重计数口径}\ ✓$$
$$
$$
```

---

## §10 边界（诚实标注）

- §3/§4 表为**逐条重推**（与原档逐字一致 ✓，且给出层内去重明细 ✓）
- §5 跨层不交为**证**（$F_i\subseteq L_i$ 且 $L_i$ 两两不交 ✓）⟹ **禁忌①在本表内不触发** ✓
- §6 的 $|C\cap L_2|\le10/8$ 为**本档新推导**（未程序验证 ✗，纯组合 ✓）
- §7 恒等式 $\sum_{x\notin C}b(x)=10M-2A_1$ 与 $\zeta=285-2A_1$ 为**本档新推导**（与档案 $\zeta=285-2A_1\ge0$ 一致 ✓，此处给出完整双重计数证明 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 去重口径判定 命中文件数=1    :: ./F14-DEDUP-2026-09-26-forced-propagation-dedup-table.md 
技术词 行容量法     命中文件数=1    :: ./F14-DEDUP-2026-09-26-forced-propagation-dedup-table.md 
技术词 名额闭合口  命中文件数=1    :: ./F14-DEDUP-2026-09-26-forced-propagation-dedup-table.md
```
- **本档新增**（三项各命中 1 文件 = 仅自引 ⟹ **扣自引后 0**）：去重口径判定、行容量法、名额闭合口
- **档案已有（引用，不列为提出）**：forced 表、$\zeta$、$A_1\le142$
