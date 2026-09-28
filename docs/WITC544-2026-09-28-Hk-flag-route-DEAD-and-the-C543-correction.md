# WITC544-2026-09-28 — **C-544：★$H_k$ flag 路线 = DEAD ＋ 对 C-543 之\ \textbf{更正}**

> **范围（照唐先生 2026-09-28 20:08 令 ✓）**：落档更正 ＋ 判定；**不作路线裁定** ✗。空间 B ✓

**已查地图**：承 C-543（WITSUB）／`FACE-2026-09-26`／`EXCESS-2026-09-25` ✓

D0: 本档对象 ＝ **档案已有**（$H_k$／覆盖条件／$\delta$——**无新数学对象** ✓）
D1: 1（**首次给出核心判据 $H_k(F)\equiv\sum_{x\in F}\delta(x)\ge0$（数值 24/24 核验 ✓✓）＋ 首次判定 $H_k$ flag 路线 = DEAD ✓✓ ＋ 首次更正 C-543 §2「变量独立 ≠ 约束独立」✓✓**）
[R]

---

## §0 ★核心判据（**本档立法 ✓**）

$$\boxed{H_k(F)\ \equiv\ \sum_{x\in F}\bigl(c_x-1\bigr)\ =\ \sum_{x\in F}\delta(x)\ \ge\ 0}$$

**数值核验（$K{=}135$ 码，$k{=}1..4$，24 组随机 $F$）：$H_k$ 之 slack $\equiv\sum_{x\in F}\delta(x)$，\textbf{24/24 全等} ✓✓**

$$\therefore\ \boxed{\text{即使 }a_F{=}|C\cap F|\ \text{为新变量坐标，}\ H_k(F)\ \textbf{亦无新数学内容}}\ ✓$$

**推理（一行 ✓）**：$k{=}0$ 时 $F{=}\{x\}$ ⟹ $H_0(F)\iff c_x\ge1$（逐点覆盖）；$k\ge1$ 时由 $k{=}0$ 逐点不等式**在 $F$ 上求和**即得 ⟹ $H_k\in\operatorname{span}(\text{覆盖条件})\ \subset\ \operatorname{span}(\mathcal F_{\rm old})$ ✓

## §1 ⚠️ **对 C-543 §2 之更正（自我纠错）**

| C-543 §2 主张 | 更正后 |
|---|---|
| $N_U,N_{U,1}\notin\operatorname{span}(A_i)$ ⟹ $k$-子空间覆盖不等式 $\notin\operatorname{span}(\mathcal F_{\rm old})$ ✗ | **仅证得\ \textbf{变量}独立**；$H_k$ 作为**约束**恒等于覆盖条件 ⟹ 约束层面**依赖** ✓ |

$$\boxed{\text{\textbf{变量独立}\ \not\Rightarrow\ \textbf{约束独立}}}\qquad(\text{本档核心教训 ✓})$$

**具体**：$\{H_k(F)\}_F$ 之可行集 ＝ 覆盖码占据向量之投影集 ⟹ **不产生新约束** ✗

## §2 判定

$$\boxed{\text{Haas }H_k\text{ flag route}\ =\ \textbf{DEAD}}\ ✗$$

**证明链必须明确分离两件事 ✓**：

$$\underbrace{\text{covering positivity}}_{\textbf{所有 }H_k\text{ 皆属此}}\quad\neq\quad\underbrace{\text{excess congruence}}_{\textbf{真正可能产生 }103\text{–}107}$$

$$\therefore\ \boxed{\text{下一步\ \textbf{不再碰} }H_k\text{／face occupancy／其 flag 化版本}}\ ✗$$

## §3 重定向（**唯一合理活口**）

$$103\to107\ \text{不可能来自 }H_k\ (\text{只给 }93.09)\ \Longrightarrow\ \text{必来自\ \textbf{同余层}}$$

$$\boxed{\text{搜索链}:\ \text{van Wee 1988}\ \to\ \text{Habsieger}\ \to\ \text{Haas 2013}}$$

**核心非新覆盖不等式，而是**

$$\boxed{\delta_i(x)\pmod p\ \text{与非负性、层间递推之耦合}}$$

**下一轮 P1 问题（唯一）**：

$$\boxed{n{=}10,\ |C|{=}119\ \text{下，同余约束能否与已得 }\delta\text{-profile／}A_i\text{／incidence 数据产生\ \textbf{真正新的整数碰撞}？}}$$

## §4 ⚠️ 阻塞（需唐先生提供原文）

$$\text{Haas 2002／2013 正文}\ \textbf{不可得}\ ✗\ (\text{ScienceDirect 403})$$

**若唐先生手头有 PDF，上传即可** ✓；收件后**只审计**其 congruence machinery ＋ 在 $n{=}10$ 之可用边界（不扩散 ✗）。**不从摘要反推** ✗。

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "覆盖正性" "同余层" "变量独立非约束独立"
技术词 覆盖正性      命中文件数=0    ::
技术词 同余层      命中文件数=0    ::
技术词 变量独立非约束独立 命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 有限穷举（$K{=}135$，24 组）＋ 一行代数论证 ✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- 本档**不主张**同余层必定给 120；仅为"唯一登记活口" ✓
