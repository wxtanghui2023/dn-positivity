# ZBV-Existence Audit 第一轮（小灵执行）

**日期**：2026-09-10 13:58+ ｜ 预算：纸面，无代码 ｜ 纪律：**不预设 Z1–Z3 ⇒ automorphic**；主动找反例

---

## 1. 五门形式化（ZBV = Z1∩Z2∩Z3∩Z4∩Z5）

$$S_\Lambda(a,q;W,N)=\sum_{n\ge1}\Lambda(n)e(an/q)W(n/N)=M(a,q;W,N)+\mathcal D_q(a;W,N),\quad \mathcal D_q=\sum_m A_q(a,m)\widetilde W_q(m;N)$$
| 门 | 内容 | 要点 |
|---|---|---|
| **Z1** | Non-reencoding + 压缩性 | $A_q$ 由有限 arithmetic data 构成；对偶长度压缩（如 $m\lesssim q^2/N$） |
| **Z2** | Reciprocal phase | $e(an/q)\to e(\pm\bar a m/q')$（additive twist 转 reciprocal phase）——Kuznetsov 能接上的关键 |
| **Z3** | Local / CRT compatibility | $\mathcal R_{q_1q_2}\simeq\mathcal R_{q_1}\otimes\mathcal R_{q_2}$（局部可分解） |
| **Z4** | **Quadratic spectral closure（QSC）** | $A_q\times A_q\to$ Kloosterman/trace 核 $\to$ **闭合谱展开** |
| **Z5** | Zero-blindness | 整个 dual system 不显式/隐式依赖 $\{\rho\}$ |

**⭐ 唐先生的关键升级**：R8 需要的是 $\Lambda\times\Lambda$ 的二次相关 ⟹ 对每个因子做 ZBV 后必须发生
$$A\times A\ \to\ \text{Kloosterman-type kernel}\ \to\ \text{closed spectral expansion}$$
$$\boxed{\text{若 ZBV 要成为 R8 carrier，必须具有【二次谱闭合 QSC】且 }\operatorname{Spec}\cap\{\rho\text{-residue data}\}=\varnothing}$$
⟹ 这比"automorphic or nothing"严谨得多。

## 2. 反循环要求：IDC（独立对偶条件）
```
危险反例：直接令 A_q(a,m)=S_Λ(a,q;W,N)（m=1），否则 0 —— 可写出"伪 dualization"
⟹ 必须排除 re-encoding
```
$$\boxed{\text{IDC}:\ A_q\ \text{必须独立于目标 correlation }C(X,H)\text{，由 }\Lambda\text{ 的局部/全局算术律独立构造}}$$
（并入 Z1 的内容）

## 3. Λ 现状表（唐先生）
| 门 | Λ 当前状态 |
|---|---|
| Z1 non-reencoding | 可要求 ✓ |
| **Z2 reciprocal phase** | **未知** |
| Z3 CRT/local | 强约束，未知 |
| **Z4 QSC** | **未发现** |
| **Z5 zero-blind** | **标准路线失败** |

## 4. 标准 Mellin 分支：已关闭
$$-\frac{\zeta'}{\zeta}(s)=-\frac{\chi'}{\chi}(s)+\frac{\zeta'}{\zeta}(1-s)\ \Longrightarrow\ \text{contour shift 给}\ \sum_\rho\mathcal T(\rho)$$
$$\boxed{\text{ZBV-1（标准 Mellin 分支）= NO}}\quad\text{唯一活口 = 满足 Z2–Z5 的【新 }A_q\text{】}$$

---

## 5. ⭐⭐ L2 / L3 登记，以及 L3 的正确形式（本轮改写一处）

**L2（ZBV-QSC necessity，候选引理；近乎定义层可证）**：
$$\boxed{\text{若存在 zero-blind independent dualization }\Lambda\to A_q\text{ 且能产生 }\Lambda\times\Lambda\text{ 二阶主项，}\\
\text{则 }A_q\text{ 必满足 reciprocal phase + CRT-local compatibility + quadratic spectral closure}}$$

**L3（真正的生死线）**：这三种 compatibility 是否强到**迫使 $A_q$ 成为 automorphic/FE 型**？

**⚠️ 本轮改写（我的贡献）**：L3 的原形式用了"automorphic/**Euler**-FE 型"，但 **Kuznetsov 需要的是【谱可实现性/模性】，不是 Euler 乘性**：
$$\boxed{\text{ZBV 需要的性质 = 【modular/spectrally realizable】（可进谱分解），而非【Euler-multiplicative】}}$$
**⟹ L3 的正确形式**：
$$\boxed{\text{L3}^{\prime}:\ \text{reciprocity}+\text{CRT}+\text{QSC}+\text{Z5}\ \stackrel{?}{\Longrightarrow}\ \text{系数系统是 modular/谱可实现的？}}$$
**为什么这个改写重要**：Euler 乘性 ≠ 模性（存在"有函数方程但无 Euler 积"的对象，如 Epstein zeta/高阶格 theta 级数）
⟹ 若 ZBV 的准入门槛是**谱可实现性**而非乘性，则**潜在 ZBV 类比"自守 L 函数"更宽**（见 §6 反例表 (b)）。

---

## 6. ⭐ 反例猎捕（主动寻找 L3′ 的反例）

| 候选类 | reciprocity | CRT | QSC | Z5 | 判定 |
|---|---|---|---|---|---|
| **(a) 非自守 Voronoi 函数**（Chorge–Dixit：λ_Liou, μ, d²） | ✓ | ✓（乘法函数） | ✓ | **✗（公式显含 $\rho$ 级数）** | **被 Z5 吸收**；且它证明 **Voronoi ⇏ automorphic** |
| **(b) Epstein zeta / 高阶格 theta 级数** | ✓（FE） | 局部密度型 | ? | ? | **真正威胁**：有 FE 但**无 Euler 积** ⟹ 证明 FE ⇏ 乘性；须查其能否作 carrier（**待核实**） |
| **(c) 动力/几何谱展开**（Ruelle/Selberg、量子图、转移算子） | ✗ | ✗ | ✓ | ✓ | 被 Z2/Z3 吸收（缺算术 reciprocity/CRT 结构） |
| **(d) Kloosterman zeta 函数** $\sum_q S(a,b;q)q^{-2s}$ | ✓ | ✓ | ✓ | ? | **循环**：其解析理论由 Kuznetsov/自守输入建立（结构性） |
| **(e) Weil 表示 / theta** | ✓ | ✓ | ✓（二次性） | ✓ | 谱理论 = theta = 自守 ⟹ 被吸收 |

**反例猎捕结果**：
$$\boxed{\text{【未发现】未被吸收的反例；但得到一条经验二分：算术 reciprocity+CRT 类中，Z5 仅在 automorphic/FE 类被观察到}}$$
**⟹ L3′ 仍开放，但现已有【具名测试对象】**(b)（modular-但-非-Euler）与 (d)（循环性检查）。

---

## 7. 本轮判定
$$\boxed{\textbf{R8-C}^{\dagger}\ \to\ \textbf{L2 已可形式化，L3}^{\prime}\ \text{成为真正生死线}}$$
```
· 标准 Mellin 分支已关闭（ZBV-1 = NO）
· 唯一活口 = 满足 Z2–Z5 的新 A_q
· L3′ 若成立 ⟹ A_q 须 modular/谱可实现 ⟹ Λ（导数层，连 FE 都无）不匹配 ⟹ ZBV 在 QSC 类内不存在
· L3′ 若不成立 ⟹ 得到一个明确的新数学空间：
   【non-Euler-multiplicative, zero-blind, quadratically closed arithmetic duality】
   —— 这可能才是 R8 真正的活路
```
**下一刀（唯一）**：证明或否证 $\text{reciprocity}+\text{CRT-locality}+\text{QSC}\Rightarrow\text{modular/谱可实现？}$
**首选突破口 = 反例表 (b)**（Epstein/theta 类）：它同时触到"有 FE 无 Euler 积"与"谱可实现性"两条线。

## 8. 诚实边界
```
· §1/§3 的五门与状态表为唐先生本轮给出（结构性整理）
· §5 的 L3→L3′ 改写（乘性 vs 模性之辨）为本轮新增；其依据"Kuznetsov 需谱可实现性"为结构性判断
· §6 反例表的 (b) 标【待核实】（Epstein/theta 的 carrier 适用性未验）；(d) 的循环性为结构性；
  (a) 的 Z5 失败为文献级（Chorge–Dixit 摘要明言 zero sums 为 essential part）
· L2 为"近乎定义层可证"的候选引理，本轮未形式化写出证明
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 9. 提交链
```
82f885b L1″ → 本篇（ZBV-Existence Audit r1）
```
