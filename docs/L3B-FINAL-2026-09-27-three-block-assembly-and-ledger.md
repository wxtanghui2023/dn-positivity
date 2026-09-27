已查地图：已跑 scripts/prework_map_check.sh Level 3B 最终合并 三块 ledger 红线 ⟹ 执行自 `L3B-N-...`（② ✓）＋ 唐先生 11:59（最终合并 ✓）；本档 = **Level 3B 三块统一最终陈述 ＋ 状态账（红线标注 ✓）**。
D0: 本档对象 = Level 3B 的最终陈述与其状态分层
D1: 1（新增：**三块统一表 ✓**；**论文逐条对应表 ✓**；**CLOSED／open 三层账 ✓**）

# Level 3B · 三块统一最终陈述（2026-09-27）

## §0 最终陈述（先给）

```
$$\textbf{设定}:\ V=\mathbb C^{\{0,1\}^n},\quad \mathcal A_{2,n}=\mathrm{End}_{S_n}(V)\ \text{（L1 ✓）}$$
$$\boxed{\text{harmonic 分解}:\ V\simeq\bigoplus_{k=0}^{\lfloor n/2\rfloor}\big(H_k\otimes W_k\big),\quad \dim H_k=m_k=\binom nk-\binom{n}{k-1},\ \dim W_k=n-2k+1\ ✓}$$
$$\boxed{\forall X\in\mathcal A_{2,n}:\ X\simeq\bigoplus_k I_{m_k}\otimes X_k\ \Longrightarrow\ X\succeq0\iff X_k\succeq0\ \forall k\ ✓}$$
$$\textbf{逻辑来源 ✓}:\ \text{Maschke（有限群完全可约）＋ Schur（交换子结构）＋ 谱事实 —— }\textbf{非 }sl_2\ \text{半单性 ✗}$$
$$
$$
```

---

## §1 $M'$ block

```
$$\boxed{(B'_k)_{ij}=\sum_t\frac{\beta^t_{i,j,k}}{\sqrt{\binom{n-2k}{i-k}\binom{n-2k}{j-k}}}\,x^t_{i,j}\ ✓;\qquad M'\simeq\bigoplus_kI_{m_k}\otimes B'_k;\qquad M'\succeq0\iff B'_k\succeq0\ \forall k\ ✓}$$
$$\beta^{\rm paper}\ \text{来源（\textbf{独立导出} ✓）}:\ D/U\to H_k\to\rho_u=(-1)^{k-u}\binom ku\to c_{k,i}=((i-k)!)^2\binom{n-2k}{i-k}\to\boxed{\beta^{\rm paper}=[p^{i-k}q^{j-k}r^t](r-1)^k\alpha^{n-2k}}\ ✓\ \text{（(i) ✓）}$$
$$
$$
```

---

## §2 $M''$ ＋ border

```
$$\boxed{M''=M^{(d)}-M'\in\mathcal A_{2,n}\ ✓\ \Longrightarrow\ M''\simeq\bigoplus_kI_{m_k}\otimes B''_k,\quad B''_k=B^{(d)}_k-B'_k\ ✓}$$
$$\boxed{R_{M''}\simeq\begin{pmatrix}1-x^0_{00}&z^{\sf T}\\ z&B''_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes B''_k\ ✓\ \text{（border 仅在 }k=0\ ✓）}$$
$$R_{M''}\succeq0\iff B''_k\succeq0\ (k\ge1)\ \wedge\ \begin{pmatrix}1-x^0_{00}&z^{\sf T}\\ z&B''_0\end{pmatrix}\succeq0;\ \text{奇异}:\ B''_0\succeq0,\ z\in\mathrm{Ran}(B''_0),\ 1-x^0_{00}-z^{\sf T}(B''_0)^{+}z\ge0\ ✓$$
$$\textbf{未写全者}:\ z\ \text{的 }D^{1/2}\ \text{归一化符号 lemma ⏳ ——\textbf{不影响}上述 block 分解的结构性结论 ✓}$$
$$
$$
```

---

## §3 Lasserre $N$ ＋ border

```
$$\boxed{N\in\mathcal A_{2,n}\ ✓\ \text{（逐项证 ✓）};\quad T_w=P_w(\cdot)P_w^{-1}\ \text{无隐藏 scalar} ✓\ \text{（}P_wXP_w^{-1}\leftrightarrow X_{u\oplus w,v\oplus w}\ ✓\text{）}}$$
$$\boxed{N\simeq\bigoplus_kI_{m_k}\otimes N_k,\qquad (N_k)_{ij}=\sum_t\beta^t_{i,j,k}\Big(\text{Lasserre 内层组合}-\beta x^0_{d,0}\Big)\ ✓}$$
$$\boxed{R_N\simeq\begin{pmatrix}c&z_N^{\sf T}\\ z_N&N_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes N_k\ ✓;\quad R_N\succeq0\iff N_k\succeq0\ (k\ge1)\ \wedge\ \begin{pmatrix}c&z_N^{\sf T}\\ z_N&N_0\end{pmatrix}\succeq0\ ✓}$$
$$\text{奇异}:\ N_0\succeq0,\ z_N\in\mathrm{Ran}(N_0),\ c-z_N^{\sf T}N_0^{+}z_N\ge0\ ✓$$
$$
$$
```

---

## §4 三块统一 ＋ 论文逐条对应

```
$$\boxed{\begin{array}{c|c|c}
\text{对象}&k\ge1&k=0\\
\hline
M'&I_{m_k}\otimes B'_k&B'_0\\
M''&I_{m_k}\otimes B''_k&\begin{pmatrix}1-x^0_{00}&z^{\sf T}\\ z&B''_0\end{pmatrix}\\
N&I_{m_k}\otimes N_k&\begin{pmatrix}c&z_N^{\sf T}\\ z_N&N_0\end{pmatrix}
\end{array}}\ ✓$$
$$\Longrightarrow\ \boxed{\text{global PSD}\iff\text{有限族 harmonic blocks PSD}}\ ✓;\qquad\textbf{border 只存在于 trivial }k=0\ \text{扇区}\ ✓$$
$$\boxed{\begin{array}{c|c}
\text{论文位置}&\text{我们的证明资产}\\
\hline
\texttt{eq:Mprimesymmetryreduction}&M'\simeq\bigoplus_kI_{m_k}\otimes B'_k\ ✓\\
\text{Prop.\ 4.3 后半}&M''+\text{border 的 block 分解}\ ✓\\
\text{Prop.\ 4.5}&N+\text{border 的 block 分解}\ ✓
\end{array}}$$
$$\text{与论文的差别} ✓:\ \text{其中核心 }\beta\text{-系数链已\textbf{从 }D/U\ \text{独立重建}（非引用 ✓）}$$
$$
$$
```

---

## §5 状态账（**红线：不得写"Level 3B 全部 CLOSED" ✗**）

```
$$\boxed{\text{总标签}:\ \textbf{Level 3B: structurally assembled, symbolically complete except for 3 bookkeeping/classical lemmas.}}$$
$$\textbf{已 CLOSED ✓}:\ \boxed{M'\ \text{assembly}}\ \boxed{M''\ \text{assembly}}\ \boxed{N\ \text{invariant/block assembly}}\ \boxed{k=0\ \text{border 的结构与 PSD 条件}}\ \boxed{L4\text{-}5\ +\ (i)}$$
$$\qquad\text{另有（此前 ✓）}:\ L1\ |\ L2\ \text{主体}\ |\ L3\ |\ L4\text{-}1\ |\ A\text{-}1\ |\ A\text{-}2\ |\ L5\ |\ \text{因式分解引理}$$
$$\textbf{仍开三项（分层 ✓）}:$$
$$\qquad\text{(A) }V_k\ \text{无重 }S_n\text{-分解}（V_k\simeq S^{(n-k,k)},\ \text{重数 }n-2k+1）\Longrightarrow \textbf{classical input}\ \text{标法 ✓（非新资产、非漏洞 ✓）}$$
$$\qquad\text{(B) }M''\ \text{border 的精确 }D^{1/2}\ \text{归一化}\ \Longrightarrow \textbf{convention/normalization lemma}$$
$$\qquad\text{(C) }N\ \text{中 }\eta\ \text{的符号闭式}\ \Longrightarrow \text{结构＋数值已定 ✓；把 Lemma 4.6 的 }\alpha\text{-恒等式按 (i) 的生成函数方法写成正式符号证明 ⏳}$$
$$\text{真正的数学主干}:\ \textbf{已无新的 block-structure 问题} ✓$$
$$
$$
```

---

## §6 下一步（**不做大规模计算 ✓；成本最低优先 ✓**）

```
$$\boxed{V_k\ \text{classical input}\ \to\ M''\ \text{border normalization}\ \to\ N\ \eta\ \text{identity}\ \to\ \textbf{Level 3B final closure}}$$
$$\text{(A) 只需引经典定理并\textbf{逐条核对适用范围}（或给 }V_k\ \text{无重性的初等证明：}k\text{-子集模 }M^{(n-k,k)}=\oplus_{j\le k}S^{(n-j,j)}\ \text{型 ✓）}$$
$$\text{(B) 复用 L5 的范式（正交链范数 ✓）写出 border vector 的 }D^{1/2}\ \text{因子来源 ✓}$$
$$\text{(C) 复用 (i) 的生成函数法：对 Lemma 4.6 的 }\alpha\text{-恒等式做同样的母函数求和 ✓}$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1–§4 为**已证内容的汇总** ✓（逐条指向各自细档 ✓）；§5 为**状态分层** ✓（红线遵守 ✓）
- **未**声称 Level 3B 已完整闭合 ✗；**未**声称 formulation 等价已证 ✗；**未**声称新数学结果 ✗
- 本档性质 ✓ = 论文三处 PSD 条件的**独立符号重建 ＋ 明确标注的经典外部输入**（非数值复现 ✓，亦非新定理 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Level 3B 三块统一表、论文逐条对应表、三层状态账
- **档案已有（引用，不列为提出）**：Maschke、Schur、$\beta^{\rm paper}$、$\rho_u$、$c_{k,i}$、$\eta$、Schur 补、Prop 4.3/4.5


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三块统一表  命中文件数=2    :: ./L3B-N-2026-09-27-Lasserre-N-symbolic-assembly.md ./L3B-FINAL-2026-09-27-three-block-assembly-and-ledger.md 
技术词 三层状态账  命中文件数=1    :: ./L3B-FINAL-2026-09-27-three-block-assembly-and-ledger.md
```
- **本档新增**：Level 3B 三块统一表、论文逐条对应表、三层状态账（见上方命中数；0 命中者为自造语／内部标签 ✓）
