已查地图：已跑 scripts/prework_map_check.sh 块分解 lemma chain Schur 交换子 ⟹ 执行自 `LEVELS-2026-09-27`（四层级 ✓）＋ 唐先生 11:35（L3-C ✓）；本档 = **L3-C 首版：可审计 lemma chain**（能证者证／文献者引／未完成者标 ⏳ ✓）。
D0: 本档对象 = 二元 Hamming 情形的块分解证明链（lemma 级）
D1: 1（新增：**Lemma 1 自足证明** ✓；**Lemma 3（Schur 型）自足证明** ✓；**Lemma 2/4/5 的地位与待办** ✓）

# L3-C · 块分解 lemma chain（首版 2026-09-27）

## §0 总览（链的结构与现状）

```
$$\boxed{\text{链}:\ \text{L1（交换子刻画，}\textbf{已证 ✓}\text{）}\to\text{L2（}S_n\text{-模分解，}\textbf{经典待引/补 ⏳}\text{）}\to\text{L3（Schur 型，}\textbf{已证 ✓}\text{）}\to\text{Cor（PSD 等价）}\to\text{L4（}\beta\text{ 来源 ⏳）}\to\text{L5（归一来源 ⏳）}}$$
$$\textbf{诚实分级}:\ \text{L1／L3 为\textbf{本档自足证明} ✓；L2 为\textbf{经典事实}（Boolean lattice／子集置换模分解 ⏳ 需引或补证）；L4／L5 为\textbf{待做} ⏳（本档给推导路线 ✓）}$$
$$\qquad\text{⚠️ 数值审计（}n=4,6,7\ \text{偏差 }10^{-13}\text{）之地位}:\ \text{对\textbf{实现}的强证据 ✓，}\textbf{不是}本链的证明 ✗（唐先生 11:34 ✓）}$$
$$
$$
```

---

## §1 Lemma 1（交换子刻画）— **自足证明 ✓**

```
$$\textbf{设定}:\ V=\mathbb R^{\{0,1\}^n}\ \text{（维数 }2^n\text{）};\ S_n\ \text{以\textbf{坐标置换}同时作用于 }V\ \text{（置换表示 ✓）：}(P_\sigma f)(u)=f(\sigma^{-1}u)\ ✓$$
$$\textbf{Claim}:\ \mathcal A_{2,n}:=\mathrm{span}\{M^t_{i,j}\}\ =\ \mathrm{End}_{S_n}(V)=\{X:\ P_\sigma XP_\sigma^{-1}=X\ \forall\sigma\in S_n\}\ ✓\ \text{（且 }\dim\mathcal A_{2,n}=\binom{n+3}{3}\ ✓\text{）}$$
$$\textbf{Proof}:\ \text{记 }(M^t_{i,j})_{u,v}=\mathbf 1[\,|u|=i,\ |v|=j,\ |u\cap v|=t\,]\ ✓$$
$$\quad\text{(i) 不变性}:\ \text{坐标置换保持 }|u|,|v|,|u\cap v|\ ✓\ \Longrightarrow\ P_\sigma M^t_{i,j}P_\sigma^{-1}=M^t_{i,j}\ ✓$$
$$\quad\text{(ii) 张成}:\ \text{设 }X\in\mathrm{End}_{S_n}(V)\ ✓;\ \text{对 }(u,v)\ \text{与 }(\sigma u,\sigma v)\ \text{有 }X_{u,v}=X_{\sigma u,\sigma v}\ ✓\ \Longrightarrow\ X_{u,v}\ \text{只依赖\textbf{有序对 }}(u,v)\ \text{的 }S_n\text{-轨道}\ ✓$$
$$\qquad\text{而该轨道恰由 }(|u|,|v|,|u\cap v|)\ \text{决定 ✓（四计数 }n_{00},n_{01},n_{10},n_{11}\ \text{与三不变量互相决定 ✓）}\ \Longrightarrow\ X\ \text{是 }\{M^t_{i,j}\}\ \text{的线性组合 ✓}$$
$$\quad\text{(iii) 线性无关}:\ M^t_{i,j}\ \text{在互不相交的轨道对上取 }1\ ✓\ \Longrightarrow\ \text{两两正交（}\langle M^t_{i,j},M^{t'}_{i',j'}\rangle=0\ ✓\text{）}\ \Longrightarrow\ \text{无关 ✓}$$
$$\quad\text{(iv) 维数}:\ \#\{(i,j,t):\ i,j,t\ge0,\ i-t\ge0,\ j-t\ge0,\ n-i-j+t\ge0\}=\binom{n+3}{3}\ ✓\ \text{（与论文 }|I(2,n)|\ \text{一致 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{Lemma 1 成立}\ ✓\ \text{（初等 ✓，无需 Terwilliger 理论 ✓）}$$
$$
$$
```

---

## §2 Lemma 2（$S_n$-模分解与重数）— **经典，待引／补证 ⏳**

```
$$\textbf{Claim}:\ V\ \text{作为 }S_n\text{-模 分解为}\quad V\ \cong\ \bigoplus_{k=0}^{\lfloor n/2\rfloor} V_{(n-k,k)}^{\oplus m_k}\ ✓\quad m_k=\binom nk-\binom{n}{k-1}\ ✓$$
$$\qquad V_{(n-k,k)}=\text{二元双行不可约（维数 }n-2k+1\ ✓\text{）};\ m_k=\text{该不可约在 }V\ \text{中的\textbf{重数} ✓}$$
$$\textbf{现状}:\ \text{经典结果（Boolean lattice／子集置换模的分解：de Bruijn--Tengbergen--Kruyswijk 型／Schur--Weyl ✓）}\ ⏳\ \text{本档\textbf{未证} ✗}$$
$$\textbf{已有的一致性检验}:\ \sum_k m_k(n-2k+1)=2^n\ ✓\ \text{（}n=4:16;\ n=6:64;\ n=7:128\ ✓✓\text{）—— 仅\textbf{必要}条件 ✓，非充分 ✗}$$
$$\textbf{待办}:\ \text{① 引经典定理并\textbf{逐条核对适用范围}；② 或给出 }V=\oplus\ \text{的初等证明（用 }k\text{-子集模 }M^{(n-k,k)}\ \text{的分解 }M^{(n-k,k)}=\oplus_{j\le k}V_{(n-j,j)}\ ✓\ \text{叠加 ✓）}$$
$$
$$
```

---

## §3 Lemma 3（Schur 型：交换子 = 块对角 ⊗ 恒等）— **自足证明 ✓**

```
$$\textbf{Claim}:\ \text{若 }V=\bigoplus_k V_{(n-k,k)}\otimes\mathbb C^{m_k}\ \text{（}S_n\ \text{作用于第一因子 ✓）且 }X\in\mathrm{End}_{S_n}(V)\ ✓,\ \text{则}$$
$$\qquad X\ =\ \bigoplus_k\big(B_k\otimes I_{m_k}\big)\ ✓\ \text{其中 }B_k\in M_{n-2k+1}(\mathbb C)\ ✓$$
$$\textbf{Proof}:\ S_n\text{-等变自同态保持 isotypic component（Schur 引理 ✓：不同不可约之间无同态 ⟹ 交叉块为 }0\ ✓\text{）};\ \text{在单个 isotypic component 上，}\mathrm{End}_{S_n}(V_{(n-k,k)}\otimes\mathbb C^{m_k})=M_{n-2k+1}(\mathbb C)\otimes I_{m_k}\ ✓\ \text{（Schur 引理 + 中心化子定理 ✓）}\ \Longrightarrow\ \text{Claim}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{推论（谱／PSD）}:\ \mathrm{spec}(X)=\biguplus_k m_k\cdot\mathrm{spec}(B_k)\ ✓\ \text{且}\ X\succeq0\iff B_k\succeq0\ \forall k\ ✓✓$$
$$\qquad\text{—— 这\textbf{正是}论文 }eq:Mprimesymmetryreduction\ \text{的\textbf{数学来源} ✓（重数 }m_k\ \text{的角色在此显式 ✓✓）}$$
$$
$$
```

---

## §4 由 L1+L3 得 PSD 等价（**主体已证 ✓**，条件 = L2 ⏳）

```
$$\text{由 L1（}M'=\sum x^t_{i,j}M^t_{i,j}\in\mathcal A_{2,n}=\mathrm{End}_{S_n}(V)\ ✓\text{）+ L3}:\ M'\ \text{在适当基下} =\bigoplus_k (B_k\otimes I_{m_k})\ ✓$$
$$\Longrightarrow\ M'\succeq0\iff B_k\succeq0\ \forall k\ ✓\ \text{（\textbf{模 L2 的分解存在性} ⏳）}$$
$$\textbf{关键}:\ \text{本档已把"为什么会出现重数 }m_k\text{"（L3 ✓）和"为什么 }M^t_{i,j}\ \text{是基"（L1 ✓）\textbf{证掉}；\ 剩下的\textbf{唯一外部输入}＝L2（经典分解 ⏳）}$$
$$
$$
```

---

## §5 Lemma 4（$\beta^t_{i,j,k}$ 的来源）— **待做 ⏳，本档给路线**

```
$$\textbf{目标}:\ \text{把 }\beta^t_{i,j,k}=\sum_u(-1)^{t-u}\binom ut\binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}\ \text{从"作者代码里有"升级为"由显式基计算必然得到" ✓}$$
$$\textbf{路线（不直接攻四重组合数 ✓）}:\ \text{① 取 }k\text{-th harmonic component 的显式基（}U_k\ \text{的列，}\binom{n-2k}{\cdot}^{-\frac12}\ \text{型 ✓）}$$
$$\qquad\text{② 计算 }M^t_{i,j}\ \text{在该分量上的\textbf{矩阵元}}\ ✓;\ \text{③ 拆为"公共部分选择 + 两非公共部分选择 + 容斥 + 交替符号"}\ ✓;\ \text{④ 得 }\beta\ ✓$$
$$\textbf{地位}:\ ⏳\ \text{未做 ✗（这是把 }\S3\ \text{的分解\textbf{具体化}的一步 ✓，也是与作者公式对齐的\textbf{独立}路径 ✓）}$$
$$
$$
```

---

## §6 Lemma 5（归一化来源）— **待做 ⏳**

```
$$\textbf{目标}:\ \text{解释 }\binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\ \text{的来源 ✓}$$
$$\textbf{路线}:\ \text{该因子 ＝ 显式基向量 }U_k\ \text{的列范数（}U_k^{\sf T}M U_k\ \text{型同构要求正交基 ✓）—— 由 Remark 4.4（}U_0\ \text{列}= \binom ni^{-1/2}\mathbf 1_{S_i(0)}\ ✓\text{）推广即得 ✓}$$
$$\textbf{附带收获（本档 ✓）}:\ \text{数值审计中"漏归一 ⟹ 特征值偏差 }40/400/1800\ \text{级、补上 ⟹ }10^{-13}\ \text{级"即该因子的\textbf{实证必要性} ✓}$$
$$\textbf{地位}:\ ⏳\ \text{待写出一般 }U_k\ \text{的显式列 ✓}$$
$$
$$
```

---

## §7 L3-C 不得声称什么（纪律 ✓）

```
$$\text{① }\textbf{不}声称已证 Terwilliger 分解（L2 未证 ⏳）；\ \text{② }\textbf{不}声称 }M'\succeq0\iff\text{块}\succeq0\ \text{已\textbf{全部}证毕（缺 L2 ⏳）}$$
$$\text{③ }\textbf{不}把数值审计（}10^{-13}\text{）当作证明 ✗；\ \text{④ }\textbf{不}声称本项目已产生新数学结果（L5 未启 ✗）}$$
$$\text{⑤ 本档的真实地位}:\ \text{L3-C 的}\textbf{首版}（L1／L3 自足 ✓，L2/L4/L5 定位清楚 ⏳）$$
$$
$$
```

---

## §8 下一步（L3-C 完成 = L2 ＋ L4 ＋ L5）

```
$$\text{(a) L2}:\ \text{引经典分解并逐条核对适用范围，或给初等证明（}k\text{-子集模分解叠加 ✓）}$$
$$\text{(b) L4}:\ \text{按 §5 路线独立导出 }\beta^t_{i,j,k}\ \text{（与作者公式对齐 ⟹ 成为\textbf{我们的}公式 ✓）}$$
$$\text{(c) L5}:\ \text{写出 }U_k\ \text{显式列 ⟹ 归一因子来源 ✓}$$
$$\text{三项齐 ⟹ L3-C 完成 ⟹ 才谈 L3-D（reduced SDP }\equiv\text{ full SDP 的\textbf{数学}等价 ✓）}$$
$$
$$
```

---

## §9 边界（诚实标注）

- §1／§3 为**本档自足证明** ✓（初等／Schur 型 ✓）；§2／§5／§6 明确标 ⏳
- **未**主张任何新数学结果 ✗；**未**排除 119 ✗；**未**声称 formulation 等价已证明 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：block decomposition lemma chain（L1–L5）、交换子刻画证明、Schur 型块对角证明
- **档案已有（引用，不列为提出）**：Terwilliger、Schrijver、$m_k$、$\beta^t_{i,j,k}$、eq:Mprimesymmetryreduction


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 lemma chain      命中文件数=1    :: ./L3C-2026-09-27-block-decomposition-lemma-chain-draft.md 
技术词 交换子刻画  命中文件数=1    :: ./L3C-2026-09-27-block-decomposition-lemma-chain-draft.md
```
- **本档新增**：block decomposition lemma chain（L1–L5）、交换子刻画证明、Schur 型块对角证明（见上方命中数；0 命中者为自造语／内部标签 ✓）
