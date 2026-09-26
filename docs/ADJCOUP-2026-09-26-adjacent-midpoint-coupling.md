已查地图：已跑 scripts/prework_map_check.sh K(10,1) 相邻中点 耦合 S(m) G_m ⟹ 执行自 `docs/L4AUDIT-2026-09-26-...md`（G_m 框架 ✓）＋ `docs/MIDSUP-2026-09-26-...md`（中点 injectivity ✓）；本档为**复核＋更正＋分类**（唐先生 2026-09-26 21:09 稿 K-1.15–K-1.24 ✓）；**含一次构造性验证**（反例 ✓）。
D0: 本档对象 = 相邻 `b=2` 非码字中点的耦合结构（既有对象）
D1: 0（产出为一处更正、三分分类、一条弱界与判定）

# ADJCOUP-2026-09-26 · 相邻 b=2 中点耦合（复核与三分分类）

## §0 结论（先给）

```
$$\boxed{\textbf{(Q-1 确认)}\ N_{G_{m'}}(k)=S(m),\ N_{G_m}(k)=S(m')\ ✓✓\ \text{—— 但它是}\ m'=m\oplus e_k\ \text{下的\textbf{恒等式}}（\text{非新约束}）\ ⚠️}$$
$$\boxed{\textbf{(Q-2 更正)}\ (K1.20/21)\ \text{“同一码字}\ c_i\ \text{同时覆盖}\ m,m'\text{”}\ ✗\ \textbf{假}\ ——\ \text{构造反例已验}\ ✓✓\ (c_i\ne m'+e_i,\ d(c_i,m')=2)}$$
$$\boxed{\textbf{(Q-3 分类)}\ |S(m)\cap S(m')|=0/1/2\ \text{三支\textbf{均无矛盾}}\ ✗\ \text{（逐支给几何）}}$$
$$\boxed{\textbf{(Q-4 弱新界)}\ \text{相邻中点度数}\ a(m)\le\mathbf 8\ ✓\ \Longrightarrow\ \text{相邻对}\le4|\mathrm{Mid}_2|\ ✗\ \text{（无碰撞力）}}$$
$$\boxed{\textbf{(Q-5 判定)}\ \text{耦合正确但恒等；分类无矛盾}\ ✗\ \text{—— 第 \textbf{10} 次同向汇合}\ ✓✓}$$
$$
$$
```

---

## §1 (Q-1) 耦合的复核：正确，但为恒等式

```
$$\text{设}\ m,m'\notin C,\ d(m,m')=1,\ b(m)=b(m')=2,\ m'=m\oplus e_k\ ✓;\quad S(m):=\{i:m\oplus e_i\in C\},\ |S(m)|=b(m)=2\ ✓$$
$$\textbf{恒等式}:\ \text{由}\ m'=m\oplus e_k\ \text{直接得}\quad m'\oplus e_k\oplus e_i=m\oplus e_i\ ✓\ \Longrightarrow\ \{i:m'\oplus e_k\oplus e_i\in C\}=\{i:m\oplus e_i\in C\}=S(m)\ ✓✓$$
$$\qquad\text{而}\ \{i:m'\oplus e_k\oplus e_i\in C\}\ \text{恰是}\ N_{G_{m'}}(k)\ （\text{因}\ G_{m'}\ \text{的边}=\{a,b\}\leftrightarrow m'\oplus e_a\oplus e_b\in C\ ✓）\ \Longrightarrow\ \boxed{N_{G_{m'}}(k)=S(m)}\ ✓$$
$$\qquad\text{反向同理}:\ N_{G_m}(k)=S(m')\ ✓✓$$
$$\textbf{性质}:\ \text{这是}\ m'=m\oplus e_k\ \text{的\textbf{直接改写}} \Longrightarrow \text{正确}\ ✓\ \text{但\textbf{不携带新约束}}\ ⚠️\ \text{（等价于"状态在相邻点间可读回"）}$$
$$\textbf{附带（由既有公式 ✓）}:\ x_k=m'\notin C\ \Longrightarrow\ b(m')=0+\deg_{G_m}(k)\ \Longrightarrow\ \boxed{\deg_{G_m}(k)=\deg_{G_{m'}}(k)=2}\ ✓\ \text{（亦为既有公式的直接取值）}$$
$$\qquad\text{语义}:\ m'\ \text{是}\ G_m\ \text{中过}\ k\ \text{的那对码字的中点}\ ⟺\ \text{“每个}\ b{=}2\ \text{非码字是其服务对的中点”}\ ✓\ \text{（既有 ✓）}$$
$$
$$
```

---

## §2 (Q-2) 更正：$c_i$ **不**同时覆盖 $m,m'$（构造反例 ✓）

```
$$\textbf{唐稿}:\ i\in S(m)\cap S(m')\ \Longrightarrow\ “\text{同一个码字}\ c_i\ \text{同时是}\ m,m'\ \text{的邻码字}"\ \Longrightarrow\ m-c_i-m'-c_j\ \text{为 4-cycle}\ ✗$$
$$\textbf{实情}:\ i\in S(m)\ \text{给}\ c_i:=m\oplus e_i\in C\ ✓;\quad i\in S(m')\ \text{给}\ c_i':=m'\oplus e_i\in C\ ✓;\quad \boxed{c_i\ne c_i'}\ ✓\ (c_i\oplus c_i'=e_k\ne0\ ✓)$$
$$\qquad d(c_i,m')=\big|\{i,k\}\big|=\mathbf 2\ \Longrightarrow\ c_i\ \textbf{不是}\ m'\ \text{的邻点}\ ✗✓$$
$$\textbf{构造反例（本档实测 ✓）}:\ n=10,\ m=e_3,\ m'=e_3\oplus e_4,\ C=\{e_3e_1,e_3e_2,e_3e_4e_1,e_3e_4e_2\}\ ✓$$
$$\qquad b(m)=b(m')=2\ ✓;\ S(m)=S(m')=\{1,2\}\ ✓;\quad c_1\ne m'\oplus e_1\ ✓;\ d(c_1,m')=2\ ✓;\ d(c_1,c_1')=1\ ✓$$
$$\qquad \text{四点}\ \{m,c_1,m',c_1'\}\ \text{非 4-cycle}\ ✓;\quad \textbf{而是 2-face}\（\text{由}\ e_k,e_i\ \text{张成}）\ ✓✓$$
$$\Longrightarrow\ \textbf{正确读法}:\ |S(m)\cap S(m')|=\#\{i:\ \text{由}\ e_k,e_i\ \text{张成的 2-face 的“对边”两端都是码字}\}\ ✓$$
$$\qquad\text{即}:\ m\oplus e_i,\ m'\oplus e_i\ \text{同时}\in C\ ✓\ \Longrightarrow\ \text{它们距 1}\ ✓\ \text{（一对匹配码字）}\ ✓$$
$$
$$
```

---

## §3 (Q-3) 三分分类（本档主产出 ✓）

```
$$\text{三支共同点}:\ k\notin S(m)\cup S(m')\ ✓\ (\text{因}\ m\oplus e_k=m'\notin C\ ✓);\quad \deg_{G_m}(k)=\deg_{G_{m'}}(k)=2\ ✓$$
$$\textbf{支 0}\ (S(m)\cap S(m')=\varnothing):\ S(m)=\{i,j\},\ S(m')=\{p,q\}\ \text{四坐标互异},\ k\ \text{为第五个}\ ✓$$
$$\qquad\text{四个服务码字}:\ m\oplus e_i,\ m\oplus e_j,\ m'\oplus e_p,\ m'\oplus e_q\ ✓\ \text{距离谱}:\ \text{对内}=2\ ✓,\ \text{跨对}=3\ ✓\ (|i,k,p|\ \text{三互异}\ ✓)$$
$$\qquad\text{其余坐标}\ (8-4-1=3\ \text{个}):\ \text{各}\ \deg\in\{1,2\}\ ✓\ (\text{覆盖条件}\ ✓)\ \Longrightarrow\ \text{无矛盾}\ ✗$$
$$\textbf{支 1}\ (|S\cap S'|=1,\ \text{共享}\ i):\ \text{2-face}\ \{m,m',m\oplus e_i,m'\oplus e_i\}\ \text{含恰 2 码字}\ (c_i,c_i'\ \text{距 1}\ ✓)\ ✓$$
$$\qquad m,m'\ \text{为该面的另一条对角（均非码字}\ ✓)\ \Longrightarrow\ \text{无矛盾}\ ✗$$
$$\textbf{支 2}\ (S(m)=S(m')=\{i,j\}):\ \text{两个 2-face}\ (e_k e_i,\ e_k e_j\ ✓)\ \text{各含 2 码字}\ ✓;\ \text{共 4 码字}\ ✓$$
$$\qquad\text{距离谱}:\ d(c_i,c_i')=d(c_j,c_j')=1\ ✓;\ d(c_i,c_j)=d(c_i',c_j')=2\ ✓;\ d(c_i,c_j')=d(c_j,c_i')=3\ ✓\ \Longrightarrow\ \text{无矛盾}\ ✗$$
$$\qquad(\text{与分支 A 匹配结构相容}:\ \text{每码字}\ d_1\le1\ ✓\ \text{恰由这两条匹配边满足}\ ✓)$$
$$
$$
```

---

## §4 (Q-4) 一条弱新界（本档正面产出 ✓）

```
$$\textbf{定义}:\ a(m):=\#\{k:\ m\oplus e_k\ \text{是}\ b{=}2\ \text{非码字}\}\ ✓\ (\text{相邻中点度})$$
$$\text{由 (Q-1)}:\ \text{每个这样的}\ k\ \text{满足}\ \deg_{G_m}(k)=2\ ✓\ \Longrightarrow\ \text{这些}\ k\ \text{全落在}\ \{\text{度 2 顶点}\}\ \text{中}\ ✓$$
$$\text{而度 2 顶点只能在}\ i\notin S(m)\ \text{的 8 个坐标里}\ ✓\ (\text{因}\ i\in S(m)\Rightarrow\deg\le1\ ✓)\ \Longrightarrow\ \boxed{a(m)\le\mathbf 8}\ ✓$$
$$\textbf{全局}:\ \sum_{m\in\mathrm{Mid}_2}a(m)=2\#\{\text{相邻}\ b{=}2\ \text{点对}\}\ \le\ 8|\mathrm{Mid}_2|\ \Longrightarrow\ \#\{\text{相邻对}\}\le4|\mathrm{Mid}_2|\ ✗\ \text{（与 4525 条超立方边比 ⟹ 无碰撞力）}$$
$$
$$
```

---

## §5 (Q-5) 判定与链状态（第 10 次同向汇合 ✓）

```
$$\textbf{本轮}:\ \text{① 耦合复核为正确但恒等}\ ⚠️\ \text{② (K1.20/21) 更正（构造反例 ✓）}\ ③\ \text{三分分类无矛盾}\ ✗\ ④\ \text{弱界}\ a\le8\ ✗$$
$$\Longrightarrow\ \text{十条机制}\ (\text{AMEND-30/GRAMSIGN/ISOB3/TCOLL/SCOL/HQ1/MIDSUP/K1AUDIT/L4AUDIT/ADJCOUP})\ \text{全部同向}\ ✓✓$$
$$
$$
```

**链状态**：

```
P0 119/Q=1 归约 ✓ ｜ P1 理论障碍 ★（未破）
 ├ 匹配 A₁≤59/60 ✓｜A₂=143−A₁ ✓｜Type III 排除 ✓｜强制点 50+7 ✓｜|C∩L₃|≤80 ✓
 ├ T-collision ✗｜SCOL 行闭合 ✓｜HQ1 STOP ✗｜MIDSUP STOP ✗｜K1AUDIT（层限制为假）✗
 ├ L4AUDIT：G_m 框架 ✓（4≤r≤9 ✓＋度数形 ✓＋语义 ✓）
 └ ADJCOUP：相邻耦合 = 恒等 ✗＋三分分类无矛盾 ✗＋a(m)≤8 ✗
P3 collision ✗ ← 缺口不变；**十条机制均不足**
```

---

## §6 建议（需唐先生拍板 ✓）

```
$$\textbf{M-1}:\ \text{十次同向已构成强证据}:\ \text{缺口属\textbf{类型缺失}（缺一条独立的算术/结构输入}）,\ \text{而非算力或技巧}\ ✓$$
$$\qquad\Longrightarrow\ \text{建议：把 L-4/相邻耦合一并记入归档（补 `K101-119-ARCHIVE` §2 第十条 ✓）}\ ✓$$
$$\textbf{M-2（唐先生 21:03 已定）}:\ \text{转 \textbf{L-2}：用}\ \texttt{fc research}\ \text{把 2024–2026 的 }K(10,1)\ \text{新界钉死（下界是否 }>107\text{、上界是否}<120\text{）}\ ✓✓$$
$$\textbf{M-3}:\ \text{若 L-2 仍无新界，则本线以"结构未闭合＋十类机制不足"正式封存，转新问题}\ ⚠️$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 的恒等性判定为**本档结论** ✓（$N_{G_{m'}}(k)=S(m)$ 与 $m'=m\oplus e_k$ 逐字等价 ✓）
- §2 的更正由**构造反例实测支撑** ✓（$c_1\ne m'\oplus e_1$ ✓；$d(c_1,m')=2$ ✓；非 4-cycle ✓；是 2-face ✓）
- §3 三分分类为**本档逐支推导** ✓（各支均给距离谱 ✓）；**未**主张任一支不可能 ✗
- §4 的 $a(m)\le8$ 为**本档新推导** ✓（用度 2 顶点的位置限制 ✓）；其弱性已标注 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓（仅 §2 构造性验证 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 相邻中点耦合恒等性判定 命中文件数=1    :: ./ADJCOUP-2026-09-26-adjacent-midpoint-coupling.md 
技术词 服务对共享的 2-face 读法 命中文件数=1    :: ./ADJCOUP-2026-09-26-adjacent-midpoint-coupling.md 
技术词 相邻中点度界 命中文件数=1    :: ./ADJCOUP-2026-09-26-adjacent-midpoint-coupling.md
```
- **本档新增**：相邻中点耦合恒等性判定、服务对共享的 2-face 读法、相邻中点度界（见上方命中数）
- **档案已有（引用，不列为提出）**：$G_m$ 定义、$b(x_i)$ 公式、$\mathrm{Mid}_2$

**构造性验证记录（本档唯一一次计算 ✓）**：$n=10,\ m=e_3,\ m'=e_3\oplus e_4,\ C=\{e_3e_1,e_3e_2,e_3e_4e_1,e_3e_4e_2\}$
⟹ $b(m)=b(m')=2$ ✓；$S(m)=S(m')=\{1,2\}$ ✓；$c_1\ne m'\oplus e_1$ ✓；$d(c_1,m')=2$ ✓；$d(c_1,c_1')=1$ ✓
⟹ 四点 $\{m,c_1,m',c_1'\}$ **非 4-cycle** ✓、**是 2-face** ✓ ⟹ 支持 §2 更正 ✓✓
