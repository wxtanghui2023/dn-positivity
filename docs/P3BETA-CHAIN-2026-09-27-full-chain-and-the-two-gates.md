已查地图：已跑 scripts/prework_map_check.sh β 链 support flatness gate ⟹ 执行自 `P3BETA-2026-09-27-scheme-and-first-shot-verdict`（✓）＋ 唐先生 13:38（把 β 核心链完整推出 ✓）；本档 = **β 完整链 ＋ 标量修正 ＋ 两道 gate 的逻辑地位 ＋ P2 靶点** ✓。
D0: 本档对象 = q-量化 → |S| → J → Type C 四级的闭环
D1: 2（**完整链 ✓**；**λ≠J 修正（第二次 ✓）＋ gate 逻辑地位 ＋ P2 = 通用性判据 ✓**）

# P3-β 完整链（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BU-1 β 链（五步闭环 ✓）)}\ \boxed{q_v\in\{0,\lambda\}}\ \Longrightarrow\ S=\mathrm{supp}(q)=(s+\mathrm{Im}f)\cap(\mathbb F_2^m\setminus\{0\})\ \Longrightarrow\ \boxed{|S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f]}}$$
$$\qquad\Longrightarrow\ \boxed{\sum_vq_v=A_2=\lambda|S|}\ \Longrightarrow\ \boxed{J=\sum_vq_v^2=\lambda^2|S|=\lambda A_2=\frac{A_2^2}{|S|}}\ ✓✓\ \text{（全链无新假设 ✓）}$$
$$\boxed{\textbf{(BU-2 ⚠️ 标量修正（第二次）)}\ \textbf{不是 }\lambda=J\ ✗\ \text{（唐先生 }\S1\text{）};\ \text{正确}:\ \boxed{\lambda=\rho=\frac{A_2}{|S|}=2^{\,11-d'}}\ ✓;\quad J=\lambda A_2\ ✓;\quad \sum_vq_v=A_2\ (\textbf{非 }A_2^2\ ✗)}$$
$$\qquad\textbf{数值核（}n{=}16,\ d'{=}4\text{）}:\ \lambda=128,\ |S|=15,\ A_2=1920,\ J=245760\ ✓\ \Longrightarrow\ \lambda\ne J\ ✗\ \text{但}\ \lambda=A_2/|S|\ ✓,\ J=\lambda A_2=J|S|...\ \text{即}\ J|S|=A_2^2\ ✓\ \text{（\textbf{该式本身对 ✓}）}$$
$$\qquad\textbf{注 ✓}:\ \text{唐先生 }\S6\text{ 的 }\rho=2^{11-d'}\ \textbf{正是正确的 }\lambda\ ✓\ \text{（与其 }\S1\text{ 的"}\lambda=J\text{"自相冲突 ✗）—— 以 }\S6\text{ 为准 ✓}$$
$$\boxed{\textbf{(BU-3 ⭐两道 gate 及其逻辑地位 ✓)}\ \text{Support gate}:\ S=\text{punctured linear/affine subspace};\quad \text{Flatness gate}:\ q_v=q_w\ \forall v,w\in S\ ✓}$$
$$\qquad\textbf{族内}:\ \text{二者\textbf{均为定理}（A-ALIGNTHM-1 ✓）⟹ 族内\textbf{无剪枝力} ✗（9 块全可实现 ✓）}$$
$$\qquad\textbf{族外}:\ \text{若有候选 NP1CC 违任一 gate} \Longrightarrow\ \textbf{该候选不属于 Theorem-13 形} \Longrightarrow\ \textbf{否证通用性} ✓✓\ \text{—— 这才是 gate 的真正用途 ✓}$$
$$
$$
```

---

## §1 完整链（**✓ 逐步，无跳步**）

```
$$\text{(1) 量化（定理 ✓）}:\ q_v=\lambda\cdot\mathbf 1[v\in S],\quad \lambda=2^{\,n-m-d'}\ ✓\ \text{（}n{=}2^m{-}1\ ✓\text{）}$$
$$\text{(2) 支撑（定理 ✓）}:\ S=(s+\mathrm{Im}f)\cap(\mathbb F_2^m\setminus\{0\})\ \Longrightarrow\ |S|=2^{d'}-\mathbf 1[s\in\mathrm{Im}f]\ ✓$$
$$\text{(3) 一次矩（定义 ✓）}:\ \sum_vq_v=A_2\ \text{（}q\ \text{计数距离-2 跨界对 ⟹ 总和 = 距离-2 对总数 ✓）}\ \Longrightarrow\ A_2=\lambda|S|\ ✓$$
$$\text{(4) 二次矩（定义 ✓）}:\ J=\sum_vq_v^2=\lambda^2|S|\ \text{（恒定值平方 × 支撑大小 ✓）};\ \text{由 (3)}:\ \lambda A_2=\lambda^2|S|\ ✓\ \Longrightarrow\ \boxed{J=\lambda A_2=\frac{A_2^2}{|S|}}\ ✓✓$$
$$\text{(5) Type C 特化（}s\in\mathrm{Im}f\ \Longrightarrow\ s+\mathrm{Im}f=\mathrm{Im}f\ ✓\text{）}:\ S=\mathrm{Im}f\setminus\{0\}\ ✓\ \Longrightarrow\ |S|=2^{d'}-1,\ \lambda=2^{11-d'},\ A_2=(2^{d'}-1)2^{11-d'},\ J=(2^{d'}-1)2^{22-2d'}\ ✓✓$$
$$
$$
```

---

## §2 Type C 四级表（**✓ 唐先生公式，全部整数 ✓**）

```
$$\begin{array}{c|c|c|c|c}
d' & |S|=2^{d'}-1 & \lambda=A_2/|S| & A_2=(2^{d'}-1)2^{11-d'} & J=(2^{d'}-1)2^{22-2d'}\\
\hline
1 & 1 & 1024 & 1024 & 2^{20}=1048576\\
2 & 3 & 512 & 1536 & 3\cdot2^{18}=786432\\
3 & 7 & 256 & 1792 & 7\cdot2^{16}=458752\\
4 & 15 & 128 & 1920 & 15\cdot2^{14}=245760\\
\end{array}$$
$$\textbf{判读 ✓}:\ \text{四块的}\textbf{全部标量条件}（整除性、}A_2\ \text{形式、}J\ \text{整数性 ✓）\textbf{全部满足} \Longrightarrow \textbf{标量层无剪枝} ✗\ \text{（唐先生 }\S7\text{ 判断一致 ✓）}$$
$$\qquad\textbf{层级律 ✓}:\ d'\to d'{+}1\ \text{时}\ |S|\ \text{翻倍、}\rho=A_2/|S|\ \text{减半 ✓}\ \text{（唐先生 }\S6\ ✓）$$
$$
$$
```

---

## §3 两道 gate（**✓ 定义 ＋ 逻辑地位**）

```
$$\textbf{Support gate}:\ q\ \text{的支撑必须是}\ d'\ \text{维线性/仿射子空间去 0（}n{=}16\ \text{时即 }\mathbb F_2^4\ \text{的子空间 ✓）} \Longrightarrow |S|\in\{2^{d'}-1,2^{d'}\}\ ✓$$
$$\textbf{Flatness gate}:\ q_v\ \text{在 }S\ \text{上必须恒定（共同值 }\lambda=2^{11-d'}\ ✓\text{）} \Longrightarrow \text{排除"支撑对但分布不均"的候选 ✓}$$
$$\textbf{逻辑地位（关键 ✓）}:\ \text{在 Theorem-13 族内这两条是\textbf{定理}（已证 ✓）} \Longrightarrow \text{族内候选无一可被排除 ✗（已于 }\S1\text{ 的 9 块可实现性独立确认 ✓）}$$
$$\qquad\textbf{因此 gate 的正确用法} =\ \text{对\textbf{族外}候选作检验} \Longrightarrow\ \text{违 gate} = \text{族外性的\textbf{证书}} ✓\ \text{—— 这直接连到通用性问题 ✓✓}$$
$$
$$
```

---

## §4 P2 靶点（**✓ 唐先生 }\S8\text{ 修正版 ＋ 诚实预期**）

```
$$\boxed{\text{P2}:\ \text{寻找一个候选分类对象，使}\ \big(|\mathrm{supp}\,q|=|S|\ \text{对}\ \big)\ \wedge\ \big(\text{支撑非仿射}\ \vee\ q\ \text{不平坦}\big)\ ✓}$$
$$\qquad\textbf{诚实预期 ✓}:\ \text{若该候选真是 NP1CC} \Longrightarrow \textbf{否证"Theorem-13 形 = 全部 NP1CC"（通用性）} ✓✓\ \text{—— 这是一个\textbf{well-posed 且高价值}的问题 ✓}$$
$$\qquad\text{若找不到（且族内全覆盖）} \Longrightarrow \text{通用性获得\textbf{正向证据}（非证明 ⚠️）} \Longrightarrow (d',s)\ \text{可升级为全体 NP1CC 的粗不变量 ✓（研究级 ⚠️）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

---

## §5 边界（诚实标注）

```
- §1–§2 为本档推导 ＋ 算术核验（无新计算 ✓，遵"先方案后一枪" ✓）；§3 为**逻辑地位判定** ✓；§4 为**靶点提案（未执行 ✓）**
- ⚠️ 本档**第二次**修正 }\lambda=J\ ✗\ \text{（第一处在 P3BETA 档 BT-2 ✓）；以 }\lambda=\rho=A_2/|S|\ \text{为准 ✓}$$
- **未**声称任何块被排除 ✗（9 块全可实现 ✓）；**未**声称 gate 有族内剪枝力 ✗；**未**涉 119 ✓
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：β 完整五步链、$\lambda=\rho$ 修正（第二次）、Support/Flatness 双 gate 的逻辑地位、P2 = 通用性判据
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-P3BETA-1、$q_v$、$|S|$、$J$、Type C 四级


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 完整五步链  命中文件数=1    :: ./P3BETA-CHAIN-2026-09-27-full-chain-and-the-two-gates.md 
技术词 双 gate 逻辑地位 命中文件数=0    ::
```
- **本档新增**：β 完整五步链、$\lambda=\rho$ 修正（第二次）、Support/Flatness 双 gate 的逻辑地位、P2 = 通用性判据（见上方命中数；0 命中者为自造语／内部标签 ✓）
