已查地图：已跑 scripts/prework_map_check.sh SCOL-0 解耦 Q=1 依赖 行闭合 ⟹ 逐字读 `SCOL-2026-09-26-...`（§0/§1 ✓）、`STAR3-2026-09-26-...`（Type III 排除 ✓）、`PROPAGATION-2026-09-26-...`（中点引理＋传播引理 ✓）；本档 = **SCOL-0 判定：不脱离 Q=1（负结果 ✓）→ SCOL-1 叠加后退化为在档传播引理 ⟹ STOP**。
D0: 本档对象 = (F-1) 行闭合引理的 Q=1 依赖审计
D1: 2（**(F-1) 的 capacity 内容来自 Q=1（否定其可解耦 ✓）**；**(F-1) 的 Q=1-free 残件＝在档中点/对覆盖事实 ⟹ 叠加即退化 ⟹ STOP ✓**）

# SCOL-0：解耦审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(GA-1 🔴SCOL-0 = 否定（不可解耦）)}\ \text{(F-1) 拆成两件，逐件标记 Q=1 依赖性 ✓}:}$$
$$\qquad\textbf{件 ①（身份等式）}:\ \text{"}e_l\ \text{的覆盖者集 = 行 }l\ \text{的权-2 码字集"}:\ \text{对任意码均成立 ✓（因 }d(c,e_l)\le1\iff \mathrm{wt}(c)\in\{0,1,2\}\ \text{且 }l\in c\ \text{或 }c{=}0\ ✓\text{）} \Longrightarrow \textbf{Q=1-free ✓ 但\textbf{平凡}}（定义性 ✓）$$
$$\qquad\textbf{件 ②（容量上界）}:\ \text{"}b(e_l)\le2"\ \text{—— \textbf{这才是 (F-1) 的全部内容 ✓}（有它则行饱和 ✓）}; \text{而在 SCOL 中它来自 }STAR3\ \text{的 \textbf{Type III 排除} ✓}$$
$$\qquad\Longrightarrow\ \textbf{Type III 排除是关于\textbf{唯一 }b{=}3\ \text{点 }z\ \text{的配置 ✓（}\sigma(1){=}\sigma(2){=}j\ \text{型、}z\ \text{的三码字邻及其伴侣 ✓）} \Longrightarrow \textbf{依赖 }Q{=}1\ ✗✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{SCOL-0 = 否定}:\ \text{(F-1) 作为"容量-2 定理"\textbf{不}可脱离 }Q{=}1\ ✗}\ \text{（一般 }M{=}119\ \text{时 profile 未知 ⟹ }b(e_l)\ \text{无一致上界 ✗）}}$$
$$\boxed{\textbf{(GB-1 ⭐SCOL-0 的 Q=1-free 残件（唯一可回收物 ✓）)}\ \text{件 ① 可提炼为\textbf{普适对覆盖约束}:\ \boxed{b(x)=2,\ W(x)=\{c,c'\}\Longrightarrow C\cap B_1(x)=\{c,c'\}}\ ✓✓\ \text{（}Q{=}1\text{-free ✓）}}$$
$$\qquad\text{（因 }|B_1(c)\cap B_1(c')|\le2\ \text{对 }d(c,c')\le2\ ✓\text{，且 }d(c,c')>2\ \text{时无公共邻 ✗）} \Longrightarrow\ \text{此即档案}\ \textbf{中点引理}（PROPAGATION\ §3 已核实 ✓）$$
$$\boxed{\textbf{(GC-1 🔴SCOL-1 叠加后退化（STOP ✓）)}\ \text{把 (GB-1) 用于星型强制点 }z_{ij}\ (b(z_{ij})\ge2\ ✓):\ \text{若 }b(z_{ij}){=}2\ \text{则 }C\cap B_1(z_{ij})=\{c_i,c_j\}\ ✓ \Longrightarrow\ \text{其 }n{-}2{=}8\ \text{个"其余邻点"须由 }S_2(z_{ij})\ \text{的码字覆盖 ✓}$$
$$\qquad\Longrightarrow\ |C\cap S_2(z_{ij})|\ \ge\ \lceil (n-2)/2\rceil=4\ ✓\ \text{—— \textbf{这恰是档案传播引理（已证 ✓）}} \Longrightarrow\ \text{不同 }z_{ij}\ \text{可\textbf{共享} }S_2\ \text{码字 ✗ ⟹ \textbf{不聚合}（PROPAGATION 已证伪其 ladder ✗）}$$
$$\qquad\Longrightarrow\ \boxed{\text{叠加结果 = 档案已有材料的重述 ✗ ⟹ \textbf{STOP}（按唐先生判据：未产生 support-level 禁制关系 ✓，退化为在档引理 ✓）}}$$
$$
$$
```

---

## §1 逐条依据（**✓**）

```
$$\text{(1) 件 ① 的推导（Q=1-free ✓）}:\ d(c,e_l)=\mathrm{wt}(c)+1-2[l\in c]\le1 \iff (\mathrm{wt}(c){=}0)\vee(\mathrm{wt}(c){=}1\wedge l\in c)\vee(\mathrm{wt}(c){=}2\wedge l\in c)\ ✓$$
$$\qquad\Longrightarrow\ B_1(e_l)\cap C=\Bigl([0\in C]\{0\}\Bigr)\cup\{c:\mathrm{wt}(c){=}1,l\in c\}\cup\{\{l,m\}\in C\}\ ✓\ \text{—— 故"行 }l\ \text{饱和"与"}\mathrm{coverer}\ \text{集"同义 ✓（定义性 ⟹ 无信息 ✗）}$$
$$\text{(2) 件 ② 的 Q=1 依赖 ✓}:\ SCOL\ §1\ \text{逐字}: "由 STAR3 §4（Type III 排除）:\ n_l\le2\ ✓"；而 STAR3\ \text{的 Type III 是} Q{=}1\ \text{分支中 }z\ \text{（唯一 }b{=}3\ \text{点）的三码字邻结构 ✓ ⟹ 依赖 }Q{=}1\ ✓$$
$$\text{(3) 一般 }M{=}119\ \text{的反例风险 ✓}:\ \sum\delta{=}285\ \text{只给平均 }\bar b\approx1.278\ ✓;\ \text{profile }(N_k)\ \text{未定 ⟹ 某 }e_l\ \text{可有 }b(e_l)\ge3\ ✓ \Longrightarrow \text{件 ② 失效 ✗✓}$$
$$
$$
```

---

## §2 状态与封口（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{SCOL-0 为\textbf{否定}结果 ✗};\ \text{SCOL-1 退化为在档引理 ⟹ \textbf{本路线封口} ✓};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{累计同向收敛}:\ \text{本档为第 }\mathbf{14}\ \text{次 ✓（新对象最终落回在档引理／恒等式 ✓）} \Longrightarrow\ \text{建议：119 主线不再沿"局部强制→支撑禁制"形状推进 ✓（该形状已被 }PROPAGATION\text{＋本档双重封口 ✗）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：SCOL-0 解耦否定（件①平凡、件② Q=1 依赖）、Q=1-free 残件＝普适对覆盖约束、SCOL-1 退化为在档传播引理之判定
- **档案已有（引用，不列为提出）**：SCOL-2026-09-26、STAR3-2026-09-26、PROPAGATION-2026-09-26（中点引理＋传播引理＋ladder 证伪）


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 解耦否定     命中文件数=1    :: ./SCOL0-2026-09-27-decoupling-audit-negative.md 
技术词 对覆盖约束  命中文件数=1    :: ./SCOL0-2026-09-27-decoupling-audit-negative.md
```
- **本档新增**：SCOL-0 解耦否定（件①平凡、件② $Q{=}1$ 依赖）、$Q{=}1$-free 残件＝普适对覆盖约束、SCOL-1 退化为在档传播引理之判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
