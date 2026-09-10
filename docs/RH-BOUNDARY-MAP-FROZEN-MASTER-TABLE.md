# RH Boundary Map — FROZEN MASTER TABLE

**状态**：**冻结基准**（2026-09-10）｜**用途**：以后任何新候选，先过此表，再谈构造
**范围限定**：本表刻画**本项目已审计的 architecture class**（两尺度 reach 构造），**不是"全部数学"**

---

## 0. 四态图例（严格分栏，禁止混读）

| 标记 | 含义 |
|---|---|
| **[证明]** | 定理级 / 精确验算（有记录可核） |
| **[结构性归约]** | 以论证确立"属于某类"；**不是定理** |
| **[经验性本体判断]** | 基于**已列举**原语的判断；**明确不是定理** |
| **[FROZEN GAP]** | 未证为空；**无生成原则**；重启须提交生成原则 |

---

## 1. 第一层商空间 $\mathfrak M_{\rm arithmetic}/\langle N1,\dots,N7\rangle$

| 编号 | 机制族 | 核心坍缩 | 状态 |
|---|---|---|---|
| **N1** | Reach / Boundary | $\Theta(H,X/H)$，固定点落到 $\sqrt X$ 的边界重合 | [结构性归约]（其中 $\Theta(r,r)=0$ 为 **[证明]**） |
| **N2** | Label / Symmetry | prime / residue / character / Galois 只作用于**标号** | [结构性归约] + [经验性本体判断] |
| **N3** | Existing Duality / Repackaging | Fourier / Mellin / FE / Poisson / trace / projection | [结构性归约] |
| **N4** | Associative Algebra | group / semigroup / operator / Hecke / composition | [结构性归约]（其中 associator $\equiv0$、Hecke $\Omega\equiv0$ 为 **[证明]**） |
| **N5** | Finite Norm / Orthogonality | $\sqrt q,\sqrt N$ 来自**有限范数/正交性** | [结构性归约] |
| **N6** | Canonicalization / Quotient | reduction / representative / normalization 制造**假 defect** | [结构性归约] |
| **N7** | Statistical / Observed Scaling | $1/2$、GUE、correlation、variance 仅是**观察到的**尺度 | [经验性本体判断] |

### 两轴判据（须**同时**逃逸）
$$\boxed{\text{Candidate}\xrightarrow{\text{sqrt source}}N1/N5/N7}\qquad\boxed{\text{Candidate}\xrightarrow{\text{involution source}}N2/N3/N4/N6}$$

---

## 2. 第二层：Native-operation ontology

$$\boxed{\text{三原语}=\text{additive translation}+\text{multiplicative scaling}+\text{label/Galois}}$$ [经验性本体判断]

| O 类 | 机制 | 当前状态 | 归宿 | 状态标记 |
|---|---|---|---|---|
| **O1** | binary composition | 已审 | N4 / N3 | [证明]（分配律退化、$(∗,\cdot)$ die）+ [结构性归约] |
| **O2** | correspondence | 已归入 | $N1\!-\!N7\cup O5$ | [结构性归约]（Correspondence Reduction Lemma） |
| **O3** | action / response | **class-closed** | N1/N2/N4/N5/S10 | [结构性归约] + [经验性本体判断]（A1–A5 本体清单） |
| **O4** | incidence / compatibility | 已审 | N1/N2/N4/N6 | [结构性归约]（FM1 为 [证明]） |
| **O5** | primitive higher-arity | **class-closed for independent SW6 mechanisms** | 目标耦合 / 独立入口无 | [结构性归约] + [经验性本体判断]（三体耦合=解析核心） |

---

## 3. 终止链

$$\boxed{\begin{aligned}\text{Arithmetic primitives}&\longrightarrow O1\cup O2\cup O3\cup O4\cup O5\\&\longrightarrow N1\cup\cdots\cup N7\\&\Longrightarrow \mathbf{G\!-\!SW6=CLOSED}\end{aligned}}$$
$$\boxed{R_{\rm 4th\text{-}irr}=\text{FROZEN GAP}}\quad(\text{不是 }R_{\rm 4th\text{-}irr}=\text{OPEN})$$

---

## 4. S-gates（只列具长期过滤价值者）

| Gate | 阻断 |
|---|---|
| **S1** | truncation boundary → N43 |
| **S2** | normalization / reduction → N6 |
| **S3** | projection → N3 |
| **S4** | holonomy → existing connection/trace machinery |
| **S5** | transportable reparameterization → associative / coboundary |
| **S6** | **non-multiplicativity $\neq$ non-associativity** |
| **S7** | operator composition → $\Omega\equiv0$ |
| **S8** | monotone resolution does not create $H\leftrightarrow X/H$ |
| **S9** | anti-covariance ⇒ diagonal fixed point |
| **S10** | linear involution ⇒ $\theta'=\pm\theta$ |
| **S11** | ordinary swap mechanisms → existing duality / label / group inverse |

**特别重要**：**S6、S7、S9、S10** —— 它们阻止把**表面上的非平凡性**误判为真正的新机制
（S7、S9 的支撑含 **[证明]**：operator composition associator $\equiv0$；$\Theta(r,r)=0$）

---

## 5. Six fundamental doors

$$\boxed{\begin{array}{ll}
D1&\text{Non-reencoding}\\
D2&\text{Target-independent construction}\\
D3&\text{Genuinely }J\text{-sensitive}\\
D4&\text{Non-associative / non-coboundary}\\
D5&\text{Intrinsic cross-scale coupling}\\
D6&\text{Independent }\sqrt X\text{ generator}
\end{array}}$$
$$\boxed{D6:\ \sqrt X\ \text{必须由【机制产生】，而不是由【数据观察】得到}}$$

---

## 6. Frozen gaps（单列，**不得**混入 NO-GO）

### $R_{\rm 4th\text{-}irr}$ — Fourth-class irreducibility
$$\boxed{\text{FROZEN}}$$
**含义**：**不是**证明不存在，而是**目前没有生成原则**，因此**禁止**继续以"寻找第四类对象"为名无限扩张搜索
**重启条件**：$\boxed{\text{必须提交【新的生成原则】}}$ —— 而不是提交另一个三元公式

### 其他保留残差
```
R_int-sym        restricted（内部对称：I1–I5 逃生规范留档，无入口）
R_A-ind / R_B4   inactive（受限封存）
SW6              CLOSED（不是 open）
Λ 耦合            FROZEN
```

---

## 7. ⚠️ 已冻结但**不得**误称为 NO-GO 的区域

$$\boxed{\text{Structural Closure}\neq\text{Impossibility Theorem}}$$
以下全部属于**结构性边界**，**非数学不可能性定理**：
```
① "三原语"本体论                      [经验性本体判断]
② O3 class-closure                    [结构性归约]
③ O5 independent-mechanism class-closure [结构性归约]
④ O2 Reduction Lemma 的六类穷尽        [结构性归约]
⑤ O4 的 preorder-directionality 判断   [结构性归约]
⑥ R_4th-irr                            [FROZEN GAP]
```

---

## 8. M-NOGO-1 证据链（**正式并入**；详见 `docs/M-NOGO-1-assembly.md`）

> 目的：把"每类为何死、死在哪一级证据"固化进冻结基准，**防止以后重新搜索时把"结构性归约"误升级成"不可能定理"**。

### §8.1 命题
$$\boxed{\forall i\in\{1,\dots,7\},\quad N_i\to\neg(A+C)\ \text{或}\ \text{FROZEN GAP}}$$

### §8.2 证据等级表

| 类别 | 死亡链 | 证据等级 |
|---|---|---|
| **N1** Reach/Boundary | $N1\to A_1$-fail（$H\cdot(X/H)=X$ 每尺度独立钉住 $\alpha=\tfrac12$） | **[证明]** |
| **N5** Finite Norm/Orthogonality | $N5\to A_1$-fail（$\lvert\tau(\chi)\rvert^2=q$ 每有限 $q$ 上 exact 给出 $\alpha=\tfrac12$） | **[证明]** |
| **N7** Statistical/Observed Scaling | $N7\to G_6$-fail 且 C 不可提供（与 $G_6$ 定义性排除**字面冲突**） | **[证明]** |
| **N2** Label/Symmetry | $N2\to$ C 不可提供（标签结构预编码答案，非 primitive 导出） | **[结构性归约]** |
| **N3** Existing Duality | $N3\to A_1$-fail（FE 对称点 $s=\tfrac12$ 是**单尺度**性质） | **[结构性归约]** |
| **N4** Associative Algebra | $N4\to A$-fail 或 C 不可提供（结构常数→单尺度；迭代率→无独立 C 来源） | **[结构性归约]** |
| **N6** Canonicalization/Quotient | $N6\to$ C 不可提供（规范化是约定，非 primitive 导出） | **[结构性归约]** |

**本轮 [FROZEN GAP]：无。**

### §8.3 逻辑边界（固定表述，随表引用）
$$\boxed{\text{absence of an independent C-rigidity source}\ \neq\ \text{proof that no such source exists}}$$
$$\boxed{\text{M-NOGO-1 只完成了 }N1\text{–}N7\text{ 内部装配，不构成对所有数学机制的否定}}$$

---

## §8.4 配套：候选筛检程序（长期研究纪律）
$$\boxed{\text{Candidate}\to\text{N-quotient}\to\text{O-class}\to\text{frozen-gap check}}$$
以后任何新候选，**第一问不再是"它能不能产生 $\sqrt X$？"**，而是：
（1）它属于哪个 native-operation class（O1–O5）？（2）是否已落入 N1–N7（两轴同时检查）？（3）若未落入，是否真正产生【新的 mechanism】？（4）若只是"第四类不可约性"且无新生成原则 ⟹ **冻结**（R_4th-irr）

---

## 9. ISRG 外部入口（下一阶段正门）

$$\boxed{\mathcal E_{\rm ISRG}=\left\{\mathfrak M\notin\bigcup_{i=1}^{7}N_i:\ A(\mathfrak M)\land C(\mathfrak M)\right\}}$$

**准入问句（任何候选必须【先回答】，才允许进入数学构造）**：

> **它究竟来自哪个 N1–N7 之外的 primitive generation principle？**

**⚠️ N8 规则**
$$\boxed{\text{N8 必须是【新的生成原则】，而不是【新的对象】}}$$
（不得再产生"给旧机制换名字"式的 N8）

**保留纪律**：G-SW6 停止；**不得**沿 SW6 做微调；**不得**从 O1–O5 内部再挖名字；下一条 RH 主线须从本边界图【外部】寻找机制；RH 线整体仍开放；**Λ 耦合继续冻结**。

---

## 10. 诚实边界
```
· 本表的骨架（0–7 节结构、两轴判据、S-gate 列表、D1–D6、frozen gap 约定、筛检程序、四态分栏要求）
  —— 均为唐先生指定
· 表内各处 [证明] / [结构性归约] / [经验性本体判断] / [FROZEN GAP] 标记为小灵按四态图例逐项归位
· 全部 [结构性归约] 与 [经验性本体判断] 条目【不得】作为定理引用；
  唯一可作定理/精确验算引用者为标 [证明] 的条目（Hecke 关联子 2744×5 权重、Θ(r,r)=0、
  (Δ,P) 双射、D1 精确恒等式、X6 范围对换、Gauss 和 |τ|=√q 等）
· §8 的三层结构（8.1 命题 / 8.2 证据等级表 / 8.3 逻辑边界）与 §9 的 𝓔_ISRG 入口 —— 为唐先生本轮指定
· §8.2 表中 [证明] 级三条各自依赖精确事实（H·(X/H)=X 恒等式 / 有限正交性 / G6 定义级禁列）；
  四个 [结构性归约] 条目中的 per-scale、非 primitive 导出、约定非机制等判断【均未形式化】
· "absence ≠ proof" 与 "M-NOGO-1 只完成内部装配" 两句为【固定表述】，随表引用
· 范围限定随表引用：本表刻画【已审计的 architecture class】，非全部数学
· 未写代码、未做数值；未引入 ζ 零点或谱算子；全文未使用 Λ
```

## 11. 提交链
```
41496e4 O2 归约 + G-SW6 CLOSED → 冻结基准总表
c3a4488 M-NOGO-1 装配（N1–N7 死亡链）→ 并入 §8 三层 + §9 ISRG 外部入口
本篇 → 追加 §10（D2-arith 收口 + 边界条件 + 下一阶段入口）
```
---

## 10. D2-arith 收口（**CLOSED**；详见 `docs/D2-arith-CLOSED.md`）

$$\boxed{\textbf{D2-arith} = \textbf{CLOSED}}$$
**不进微调分支**（不开 D2b / D2c / D2-solenoid-2）。

### §10.1 二分（D2 的核心机制被钉死）
| bonding | 极限行为 | 结果 |
|---|---|---|
| **满射**（solenoid / projective / 可除群 $\mathbb Q/\mathbb Z$） | 自由度**保留** | **无 rigidity**（只是把各层自由度忠实搬运到极限） |
| **非满射 / 过定约束**（$\widehat{\mathbb Z}$ 中 $n\mid x$、CRT 相容剩余） | 自由度**被消灭** | 可能 rigidity，但**通常离散/点式**（不产生临界指数） |

**关键区分**：$\varprojlim X_n\neq\varnothing$（非空）**不产生额外选择原则**；
D2 真正需要的是 $\boxed{\text{finite compatibility}\Longrightarrow\text{new global restriction}}$ —— **两者不是同一件事**。

### §10.2 D2 的"必要矛盾"（三条件）
```
D2-A：X = lim← X_n compact
D2-B：X 保留非平凡连续参数
D2-C：finite compatibility 在极限产生新的 uniform rigidity
solenoid（满射）  ⟹ A + B + ¬C
非满射/过定       ⟹ A + ¬B + C
⟹ 目前未见 A+B+C 的自然算术实例
```

### §10.3 ⚠️ 逻辑边界（固定表述，随表引用）
$$\boxed{\text{[结构性归约]}\ \text{D2-arith 的自然 inverse-limit 实例不能同时提供连续自由参数与由有限层兼容产生的新的 X-尺度刚性}}$$
**不得**写成" D2 形态在算术中无法产出 X-尺度指数 "——后者需**更一般的分类定理**方具 [证明] 资格。

### §10.4 余项 **R_D2-defect（FROZEN）**
存在逻辑第三类 bonding：**既非满射、也非"交越来越小"**：
$$\boxed{\text{non-surjective bonding}+\text{nontrivial fibers}+\text{scale-dependent defect accumulation}}$$
且须 $\boxed{\text{defect accumulation}\sim X^{\alpha}}$，**不是** $\log X,\ \log\log X,\ \rho(\log X)$。
**未证为空；不得再称"solenoid 路线"；重启须提交新生成原则**（不得作候选枚举场）。

### §10.5 DA-3 升级为一般事实
$$\boxed{\text{continuous endogenous parameter}+\text{canonical compatibility}\ \Longrightarrow\ \text{group-action tendency}}$$
$T_t=e^{tA}\Rightarrow e^{(t+s)A}=e^{tA}e^{sA}$ ⟹ 跨尺度 transport **落回已关闭的结合演化**。
⟹ D2 复活须找**非群型跨尺度演化**，且非群性**不得**来自截断/canonicalization/投影误差 ⟹ **与 SW6 死因独立交叉验证**。

### §10.6 G5 层次结论
$$\boxed{\text{算术局部约束的自然尺度}\ \neq\ \text{RH 所需要的 X-power scale}}$$
（算术 natural inverse-limit 尺度 = $\omega(n),\Omega(n),\log n,\log q$）
**层次区别**：N1–N7 = "已知机制的 1/2 无新生成资格"；D2 = "连有限层→无限层的极限刚性机制也天然倾向 log/离散压缩，而非幂律生成"。

### §10.7 ⭐⭐ 边界条件（下一阶段）
$$\boxed{\textbf{compression 本身不是 generator}}$$
$$\boxed{\text{有限层兼容 / 紧性负责【承载与收敛】；它本身【不是】临界幂律的生成器}}$$

### §10.8 边界图更新与下一阶段入口
```
N1–N7 → ISRG → D1 / D2 / D3 → 均不能提供 X-power critical generator
⟹ 下一阶段：power-law generation archaeology（从 limit/rigidity archaeology 转出）
硬条件：α = lim log L(X)/log X 必须是【动力学/组合机制的输出】，
        不得预埋在对象定义 / 归一化 / 边界条件 / 参数化 ⟹ 否则触发 PIM / C_NI
```

**诚实边界**：§10.1–§10.8 全部条目均为唐先生本轮指定（含二分表、三条件、措辞限制、R_D2-defect 规格、
DA-3 升级、G5 层次结论、边界条件句、下一阶段命名与硬条件）；[证明] 级仅限 DA-1..DA-4 的**solenoid 实例**，
一般形态与 G5/G6 均为 **[结构性归约]**；R_D2-defect 为 **FROZEN**（未证为空）。

