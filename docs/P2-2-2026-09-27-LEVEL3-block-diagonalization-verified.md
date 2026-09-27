已查地图：已跑 scripts/prework_map_check.sh Terwilliger 块对角化 同构 特征值 ⟹ 执行自 `P2-1-...-LEVEL1-PASS` ✓＋ 唐先生 11:29（Level 3 ✓）；本档 = **块对角化同构的零自由度审计通过** ✓✓。
D0: 本档对象 = Thm 3.x（Schrijver）同构 φ 与 PSD 等价式的数值验证
D1: 1（新增：**两处关键修正**（重数／归一化）＋ **特征值级等价验证** ✓✓）

# P2-2 · Level 3 块对角化已验证

## §0 结论（先给）

```
$$\boxed{\textbf{(NN-1 等价性验证通过)}\ \text{对\textbf{任意} }x\ (\text{随机 5 次}) \text{与 }n=4,6,7:\ \mathrm{spec}\Big(\sum x^t_{i,j}M^t_{i,j}\Big)=\biguplus_k m_k\cdot\mathrm{spec}(\widetilde B_k)\ \text{（机器精度 ✓✓）}}$$
$$\qquad n=4:\ \text{偏差 }7.1\times10^{-15}\ ✓;\quad n=6:\ 2.8\times10^{-14}\ ✓;\quad n=7:\ 1.1\times10^{-13}\ ✓$$
$$\boxed{\textbf{(NN-2 两处关键修正)}\ ✓:\ \text{① 重数 }m_k=\binom{n}{k}-\binom{n}{k-1}\ ✓;\ \text{② \textbf{归一同构}}\ \widetilde B_k\ \text{须乘 }\binom{n-2k}{i-k}^{-1/2}\binom{n-2k}{j-k}^{-1/2}\ ✓}$$
$$\qquad\text{维度自检}\ ✓:\ \sum_k m_k(n-2k+1)=2^n\ \text{（}n=4:16;\ n=6:64;\ n=7:128\ ✓✓\text{）}$$
$$
$$
```

---

## §1 验证的两条定理（论文原文 ✓）

```
$$\textbf{Thm (Sch05) 同构（}eq:stariso\text{）}:\quad \phi:\ \sum_{(i,j,t)}x^t_{i,j}M^t_{i,j}\ \mapsto\ \bigoplus_{k=0}^{\lfloor n/2\rfloor}\Big(\sum_t \binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k}x^t_{i,j}\Big)_{i,j=k}^{n-k}\ ✓$$
$$\textbf{PSD 等价（}eq:Mprimesymmetryreduction\text{）}:\quad \sum_{(i,j,t)}x^t_{i,j}M^t_{i,j}\succeq0\ \Longleftrightarrow\ \Big(\sum_t\beta^t_{i,j,k}x^t_{i,j}\Big)_{i,j=k}^{n-k}\succeq0\ \ \forall k\ ✓$$
$$\beta^t_{i,j,k}=\sum_{u=0}^n(-1)^{t-u}\binom{u}{t}\binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}\ ✓\ \text{（与作者代码 }\texttt{beta}\ \text{逐项一致 ✓：符号 }(-1)^{u-t}=(-1)^{t-u}\ ✓\text{）}$$
$$
$$
```

---

## §2 审计设计（零自由度 ✓，按唐先生要求 ✓）

```
$$\text{① 造 }M=\sum_{(i,j,t)\in I(2,n)}x^t_{i,j}M^t_{i,j}\ \text{（全 }2^n\times2^n\ ✓\text{）；② 按 }\phi\ \text{造归一化块 }\widetilde B_k\ \text{（尺寸 }n-2k+1\ ✓\text{）}$$
$$\text{③ 检验 }\mathrm{spec}(M)\ \mathop{=}\limits^{?}\ \biguplus_k m_k\,\mathrm{spec}(\widetilde B_k)\ \text{（多重集 ✓）—— 该式成立 }\Longrightarrow\ M\succeq0\iff\widetilde B_k\succeq0\ \forall k\ \text{（因 }\phi\ \text{为 }*\text{-同构 ✓）}$$
$$\text{④ 用\textbf{随机} }x\ \text{（5 次 ✓）——因同构对\textbf{任意} }x\ \text{成立 ⟹ 随机即强检验 ✓（不依赖 x 可行 ✓）}$$
$$
$$
```

---

## §3 失败与修正记录（诚实 ✓）

```
$$\text{首版失败 ①}: \text{块特征值总数 }9\neq16\ (n=4)\ ✗\ \Longrightarrow\ \text{漏\textbf{重数}};\ \text{修正 }m_k=\binom{n}{k}-\binom{n}{k-1}\ ✓$$
$$\text{首版失败 ②}: \text{加重数后偏差仍 }40/400/1800\ \text{级}\ ✗\ \Longrightarrow\ \text{漏\textbf{归一同构因子}}\ \binom{n-2k}{\cdot}^{-\frac12}\ ✓\ \text{（PSD 不受对角正缩放影响 ✓ 但\textbf{特征值}受影响 ✓✓）}$$
$$\Longrightarrow\ \text{修正后偏差 }10^{-13}\ \text{级 ✓✓ —— 两处\textbf{均为我实现层错误} ✗，非论文问题 ✓}$$
$$
$$
```

---

## §4 分级站位与下一步

```
$$\text{Level 0/1/2 ✓✓✓ ｜ \textbf{Level 3 主体（等价性）✓✓} —— 余下：}\textbf{reduced SDP 的数值最优值比对}\ ⚠️$$
$$\qquad\text{即：用\textbf{块 PSD}（Prop 4.3／4.5 ✓）实现 reduced SDP ⟹ 验证 }L_{\rm reduced}(n)=L_{\rm unred}(n)\ \text{在 }n=4,6,7\ ✓$$
$$\qquad\text{PASS 条件（唐先生 ✓）}:\ \text{目标差}<\varepsilon\ \wedge\ \text{对应块特征值吻合}<\varepsilon\ \wedge\ \text{约束残差}<\varepsilon$$
$$\text{Level 4（}n=10\to105.2223\text{）}:\ \text{仍 blocked ⚠️ —— \textbf{reduced 实现即为使能步 ✓}（}1024\times1024\ \text{全 PSD 不可行 ✗）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§1 为**本机数值验证** ✓（随机 5 次 × 三重 $n$ ✓，机器精度 ✓）；定理为**论文引用** ✓
- 审计验证的是**同构/等价性** ✓，**不含** SDP 最优值比对 ⚠️（下一步 ✓）
- **未**主张 Level 4 可及 ✗；**未**排除 119 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：零自由度审计（特征值并集）、块重数公式 $m_k$、归一同构因子核对
- **档案已有（引用，不列为提出）**：Terwilliger、Schrijver Thm、$\beta^t_{i,j,k}$、SDPA-GMP


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 零自由度审计 命中文件数=1    :: ./P2-2-2026-09-27-LEVEL3-block-diagonalization-verified.md 
技术词 块重数公式  命中文件数=1    :: ./P2-2-2026-09-27-LEVEL3-block-diagonalization-verified.md
```
- **本档新增**：零自由度审计（特征值并集）、块重数公式 $m_k$、归一同构因子核对（见上方命中数；0 命中者为自造语／内部标签 ✓）
