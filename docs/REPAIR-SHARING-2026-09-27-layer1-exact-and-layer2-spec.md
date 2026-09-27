已查地图：已跑 scripts/prework_map_check.sh repair-sharing 三均匀 覆盖需求 ⟹ 执行唐先生 17:37 指令（REPAIR-SHARING GATE ✓）；本档 = **第一层精确计数（强化 STOP ✓）＋ 第二层规范 ✓**。
D0: 本档对象 = ρ(J) 第一层精确刻画与第二层记账规范
D1: 3（**第一层精确刻画 ＋ 强化 STOP ✓✓**；**候选覆盖能力修正（weight-2 每词修 8 ✓）**；**第二层=唯一可能出口（须产生 excess ≥ 286 ✓）**）

# REPAIR-SHARING：第一层精确计数与第二层规范（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(VA-1 ⭐第一层需求集之精确刻画 ✓)}\ \text{固定 }0\notin C,\ C\cap B_1(0)=E_J=\{e_i:i\in J\},\ |J|=q\ge3\ ✓\ (\text{且 }C\ \text{无其它单位向量 ✓})}$$
$$\qquad\boxed{\mathcal T_J=\{y:\ \mathrm{wt}(y)=3,\ |\mathrm{supp}(y)\cap J|\ge2\}}\ ✓\qquad |\mathcal T_J|=\binom q2(n-q)+\binom q3\ ✓$$
$$\qquad\textbf{自检 ✓}:\ q{=}10\Rightarrow\binom{10}3{=}120\ ✓\ \text{（与唐先生 120 一致 ✓）};\ q{=}3\Rightarrow\binom32\!\cdot\!7{+}1{=}22\ ✓\ \text{（与唐先生 22 一致 ✓✓）}$$
$$\boxed{\textbf{(VB-1 ⭐候选覆盖能力（修正／加强 ✓）)}\ \text{能覆盖 }\mathcal T_J\ \text{的候选只有 weight }2,3,4\ \text{（无 weight-1 ✓ 因 }0\ \text{是洞 ⟹ }C\ \text{不含其它单位向量 ✓）}:}$$
$$\qquad\textbf{· weight-2 }e_p{+}e_q:\ \text{覆盖 }8\ \text{点 }\{p,q,m\}\ (m\notin\{p,q\}\ ✓),\ \text{其中属 }\mathcal T_J\ \text{者}=\#\{m\notin\{p,q\}:|\{p,q,m\}\cap J|\ge2\};\ \textbf{若 }p,q\in J\ \text{则全部 8 个 ✓✓}$$
$$\qquad\qquad\Longrightarrow\ \boxed{z_{ij}\in C\ \text{即用 \textbf{1 个 codeword 修掉整个 }Y_{ij}（8 点 ✓）}}\ \text{—— 这正是唐先生 §4 "weight-2 只覆盖一个点"之修正 ✓}$$
$$\qquad\textbf{· weight-3}:\ \text{仅自身 1 点 ✓};\qquad \textbf{· weight-4 }Q:\ \text{4 点 }T=Q\setminus\{m\}\ (|T\cap J|\ge2\ \text{者 ✓})$$
$$\qquad\Longrightarrow\ \boxed{\text{唐先生的下界 }\ge\lceil|\mathcal T_J|/4\rceil\ \text{成立但\textbf{偏松} ✗；真实 }\rho(J)\ \text{更小 ⟹ \textbf{第一层更远离 119} ✓（STOP 被\textbf{加强} ✓✓）}}$$
$$\boxed{\textbf{(VC-1 ⭐⭐第一层 STOP（强化版 ✓）)}\ \text{最乐观情形（所有 }z_{ij}\in C\ ✓）：第一层涉及点集 }\le Z_J\cup\mathcal T_J\ \text{，需要 codewords} \le q+\binom q2+\rho\ ✓}$$
$$\qquad\text{即使取最粗上界：}q+\binom q2\ \text{在 }q{=}10\ \text{时}=10+45=55\ \ll119\ ✓ \Longrightarrow \boxed{\text{第一层\textbf{不可能}产生 119 矛盾 ✗✓（与唐先生 §8/§9 同结论，且更强 ✓）}}$$
$$\boxed{\textbf{(VD-1 🔴第二层=唯一出口，且目标已精确化为 excess 记账 ✓)}\ \text{加入 repair codewords }R\ \text{后，每个 }c\in R\ \text{自带 }B_1(c)\ (11\ \text{点 ✓})，其壳须由更外层修 ⟹ \textbf{逐层记账} ✓}$$
$$\qquad\textbf{账本 ✓}:\ \text{总 incidence}=119\times11=1309\ ✓;\ \text{覆盖需求 }=1024\ ✓;\ \text{故 }\boxed{E=\sum_x(b(x)-1)=285}\ \text{（恒等式 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{第二层若能推出\ \textbf{excess}\ \ge286\ \text{（从覆盖假设出发 ✓）}\ \Longrightarrow\ \text{矛盾 ⟹ P1 ✓✓}}\ \text{（这正是"充分路线" ✓，非等价 ✗ —— 已按 16:xx 纠错口径 ✓）}$$
$$\qquad\textbf{STOP 条件 ✓}:\ \text{若第二层 union bound 又退化为 }A_1/A_2/N_k/\delta\text{-型 ⟹ STOP ✓（\textbf{不得}把退化当成功 ✓）}$$
$$
$$
```

## §1 第二层必须算的**精确**对象（**✓ 下一步 ✓**）

```
$$\text{对每个 }c\in R\ \text{（repair codeword）}:\ \text{计算 }B_1(c)\ \text{中\ \textbf{未被 }E_J\cup Z_J\cup R\ \text{覆盖}者} \Longrightarrow \text{新需求集 }\mathcal T^{(2)}\ ✓$$
$$\qquad\text{关键量 ✓}:\ \text{新需求是否强迫 }\sum_x\delta(x)\ \text{增长};\ \text{以及 }\mathcal T^{(2)}\ \text{中点的 }b\text{-值下界（}\ge2\ \text{即增 excess ✓）}$$
$$\qquad\textbf{判据 ✓}:\ \text{若 }\mathcal T^{(2)}\ \text{的强制 excess}\ +\ \text{第一层 excess}\ \ge286\ \Longrightarrow\ \textbf{P1 成立（本路线首次成功 ✓）};\ \text{否则 STOP ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{\text{本轮：第一层\textbf{判定为不足以产生 P1}（强化 ✓）；第二层规范已钉死（唯一出口 ✓）；}\textbf{未跑搜索 ✓};\ \text{不写禁止表述 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\mathcal T_J$ 之精确刻画与计数公式、候选覆盖能力修正（weight-2 修 8 点）、第一层强化 STOP、第二层 excess 记账规范
- **档案已有（引用，不列为提出）**：A-TRIPLE119-1、PROPAGATION 引理、FAILSET、21 条封口表、唐先生 §1–§9 推导


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 repair-sharing   命中文件数=1    :: ./REPAIR-SHARING-2026-09-27-layer1-exact-and-layer2-spec.md 
技术词 excess 记账    命中文件数=1    :: ./REPAIR-SHARING-2026-09-27-layer1-exact-and-layer2-spec.md
```
- **本档新增**：$\mathcal T_J$ 精确刻画与计数、候选覆盖能力修正、第一层强化 STOP、第二层 excess 记账（见上方命中数；0 命中者为自造语／内部标签 ✓）
