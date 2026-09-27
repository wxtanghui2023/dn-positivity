已查地图：已跑 scripts/prework_map_check.sh Level 3B 装配 块 PSD 等价 Maschke Schur ⟹ 执行自 `IDX2-...-CLOSED`（(i) ✓）＋ 唐先生 11:55（(iv) ✓）；本档 = **Level 3B 装配（三命题 ＋ 诚实边界 ✓）**。
D0: 本档对象 = 块 PSD ⟺ 全 PSD 的逻辑拼接（$M'$ 部分）
D1: 1（新增：**三命题的精确陈述与依赖清单 ✓**；**"sl₂ 非充分解释"的澄清 ✓**）

# L3B · Level 3B 装配（2026-09-27）

## §0 三命题与最终陈述（先给）

```
$$\boxed{\textbf{(XX-1 分解命题)}\ V=\bigoplus_{k=0}^{\lfloor n/2\rfloor}\big(H_k\otimes W_k\big),\quad \dim H_k=m_k=\binom nk-\binom{n}{k-1},\ \dim W_k=n-2k+1\ ✓\ \text{（}\sum_km_k(n-2k+1)=2^n\ ✓\text{）}}$$
$$\qquad\text{等价同型形式}:\ V\cong\bigoplus_k\big(S^{(n-k,k)}\otimes W_k\big)\ ✓\ \text{（}S^{(n-k,k)}\ \text{在 }V\ \text{中重数}=n-2k+1\ ✓\text{）}$$
$$\boxed{\textbf{(XX-2 块识别命题)}\ M=\sum_{i,j,t}x^t_{i,j}M^t_{i,j}\in\mathcal A_{2,n}\ \Longrightarrow\ M\big|_k=I_{m_k}\otimes B_k,\quad (B_k)_{i,j}=\sum_t\Big[\tbinom{n-2k}{i-k}^{-\frac12}\tbinom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k}\Big]x^t_{i,j}\ ✓}$$
$$\boxed{\textbf{(XX-3 PSD 等价命题)}\ M\succeq0\iff B_k\succeq0\ \text{对所有 }k\ ✓\ \text{（因为 }\mathrm{spec}(I_m\otimes B)=m\cdot\mathrm{spec}(B)\ ✓\text{）}}$$
$$\boxed{\text{合起来}:\ \sum_{(i,j,t)}x^t_{i,j}M^t_{i,j}\succeq0\ \Longleftrightarrow\ \Big(\sum_t\beta^t_{i,j,k}x^t_{i,j}\Big)_{i,j=k}^{n-k}\succeq0\quad\forall k\ ✓\ \text{（}eq:Mprimesymmetryreduction\ ✓\text{）}}$$
$$
$$
```

---

## §1 命题一：分解（**依赖清单化 ✓**）

```
$$\text{输入 (a): 层分解 }V=\bigoplus_iV_i\ \text{＋}D/U\ \text{交换子（L2 ✓ 自足）}$$
$$\text{输入 (b): }H_k=\ker D_k,\ \dim H_k=m_k\ ✓;\ \text{链 }h_k,\ldots,h_{n-k}\ \text{长 }n-2k+1\ ✓;\ \text{不同层 ⟹ 无关（L2 ✓ 自足）}$$
$$\text{输入 (c): }V_k\ \text{的 }S_n\text{-模分解无重且成分为 }S^{(n-j,j)}\ (j\le\min(k,n-k))\ \text{（\textbf{经典表示论输入} ⏳ 本档\textbf{不证}）}$$
$$\text{输入 (d): }H_k\cong S^{(n-k,k)}\ \text{（由 (b) 的维数 }m_k\ \text{＋ (c) 的成分表比对得 ✓；\textbf{唯一引用点} ✓）}$$
$$\Longrightarrow\ \text{每层 }V_k=\bigoplus_{j\le\min(k,n-k)}\big(H_j\text{ 的在 }V_k\text{ 中的分量}\big);\ \text{把同一 chain 的层分量并起来 ⟹ }H_k\otimes W_k\ ✓\ \text{（}\dim W_k=n-2k+1\ ✓\text{）}$$
$$\qquad\text{直和性与正交性（唐先生 ✓）}:\ \text{不同 }k\ \text{的 isotypic 分量正交（Maschke：有限群在 }\mathbb R/\mathbb C\ \text{上完全可约 ⟹ 不变子空间有正交补 ✓，\textbf{初等} ✓）}$$
$$
$$
```

---

## §2 命题二：块识别（**引用 L4 链 ✓**）

```
$$\text{由 L1}:\ M\in\mathcal A_{2,n}=\mathrm{End}_{S_n}(V)\ ✓\ \text{（与 }S_n\ \text{交换 ✓）}\ \Longrightarrow\ \text{Schur ⟹ }M\ \text{在每块上为 }I_{H_k}\otimes B_k\ ✓$$
$$\text{由 L4-1}: h_i=(i-k)!\sum_{K\subseteq S}h(K)\ ✓\ \text{（显式链 ✓）}$$
$$\text{由 A-2}: \Omega_u|_{H_k}=(-1)^{k-u}\binom ku I\ ✓\ \text{（}\rho_u\ \text{定理 ✓，含消失引理 ＋ 双计数 ＋ 三角方程 ✓）}$$
$$\text{由 L5}: \|h_i\|^2/\|h\|^2=((i-k)!)^2\binom{n-2k}{i-k}\ ✓\ \text{（两条独立推导 ✓）}$$
$$\text{由 L4-5}: \widehat\beta=\frac{(j-k)!}{(i-k)!\binom{n-2k}{i-k}}\beta^{\rm paper}\ ✓\ \text{＋}\ \beta^{\rm paper}=[p^{i-k}q^{j-k}r^t](r-1)^k\alpha^{n-2k}\ ✓\ \text{（(i) 闭合 ✓）}$$
$$\Longrightarrow\ (B_k)_{i,j}=\sum_t\tbinom{n-2k}{i-k}^{-\frac12}\tbinom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k}x^t_{i,j}\ ✓\ \text{—— \textbf{系数由我们独立导出}（非数值相同 ✓）}$$
$$
$$
```

---

## §3 命题三：PSD 等价（**含唐先生的澄清 ✓**）

```
$$\text{由命题一}:\ V=\bigoplus_k(H_k\otimes W_k)\ \text{正交直和 ✓；由命题二}:\ M=\bigoplus_k(I_{H_k}\otimes B_k)\ ✓$$
$$\text{谱事实（初等 ✓）}:\ \mathrm{spec}(I_m\otimes B)=\underbrace{\mathrm{spec}(B)\uplus\cdots\uplus\mathrm{spec}(B)}_{m\ \text{次}}\ ✓\ \Longrightarrow\ I_m\otimes B\succeq0\iff B\succeq0\ ✓$$
$$\Longrightarrow\ M\succeq0\iff B_k\succeq0\ \forall k\ ✓$$
$$\textbf{唐先生的告诫（已落实 ✓）}:\ \text{PSD 等价的真正来源 = }\textbf{(1) Maschke 完全可约（有限群 ✓ 初等）＋ (2) Schur 引理（交换子结构）＋ (3) 谱事实};\ \textbf{不是 }sl_2\ \text{半单性本身 ✗}$$
$$\qquad sl_2\ (D/U)\ \text{的作用}:\ \text{构造/识别 }H_k\ \text{与链、并算出块系数（命题一/二的"发动机" ✓）—— 是\textbf{identification 工具}，非 equivalence 的充分解释 ✓}$$
$$
$$
```

---

## §4 最终陈述与适用范围（**诚实划线 ✓**）

```
$$\boxed{\textbf{Level 3B（}M'\text{ 部分）已装配}:\ \sum x^t_{i,j}M^t_{i,j}\succeq0\iff\Big(\sum_t\beta^t_{i,j,k}x^t_{i,j}\Big)_{i,j=k}^{n-k}\succeq0\ \forall k\ ✓}$$
$$\text{依赖}:\ \text{L1 ✓ 自足；L2 ✓ 自足（除 }V_k\ \text{无重分解这一\textbf{经典输入} ⏳）；L4 链 ✓ 自足（除上述同一经典输入 ⏳）；Maschke/Schur/谱事实 ✓ 初等}$$
$$\textbf{未覆盖（本档明确划出 ✓）}:\ \text{① }M''\ \text{与边框 }R(1-x^0_{0,0},M'')\ \text{的块（Prop 4.3 后半 ✓ \textbf{数值已核 R1a ✓，符号未写 ✗ ⏳}）；② Lasserre }N\ \text{的块（Prop 4.5 ✓ \textbf{数值已核 R1b ✓，符号未写 ✗ ⏳}）}$$
$$\qquad\Longrightarrow\ \text{完整 Level 3B（整个 SDP 的块 PSD ⟺ 全 PSD）}\ \textbf{尚未闭合} ✗\ \text{—— 尚缺 ①② 的符号版本（结构应同构，可复用本档三命题 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§3 为**装配与陈述** ✓（依赖逐条列明 ✓）；§4 明确划出未覆盖部分 ✓
- **未**声称完整 Level 3B 已完成 ✗（$M''/N$ 符号版未写 ✓）；**未**声称 formulation 等价已证 ✗
- **未**声称任何新数学结果 ✗（本档 = 论文定理的**独立证明**（模一处经典输入）✓，非新定理 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Level 3B 三命题装配、$sl_2$ 角色澄清、依赖清单
- **档案已有（引用，不列为提出）**：Maschke、Schur、Wedderburn、$\rho_u$、$\beta^{\rm paper}$、$eq:Mprimesymmetryreduction$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Level 3B 装配  命中文件数=1    :: ./L3B-2026-09-27-assembly-block-PSD-equivalence.md 
技术词 sl2 角色澄清 命中文件数=0    ::
```
- **本档新增**：Level 3B 三命题装配、$sl_2$ 角色澄清、依赖清单（见上方命中数；0 命中者为自造语／内部标签 ✓）
