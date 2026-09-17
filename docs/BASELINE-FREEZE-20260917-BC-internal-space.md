# 🧊 **BASELINE FREEZE** · BC 原架构内部改造空间（2026-09-17）

> 依唐先生 2026-09-17 09:53 指令：**下一轮必须从一个已经冻结的基线开始**；本轮**不再产出新概念** ✓
> $$\boxed{\text{T1}+\text{T2}+\text{T3}\ \Longrightarrow\ \text{BC 原架构内部的既有改造空间}\ \textbf{基本封闭}}✓✓$$

---

## 0. 基线声明（frozen）

$$\boxed{\begin{array}{ll}
\textbf{作用域}&\text{在保持 BC 的}\ (4.10)\text{--}(4.29)\text{、原 C--S 组织、}\ q=\mathfrak p_1n_1'\ \text{固定相位模数层的前提下}\\
\textbf{结论}&\ell_2\text{-侧}\ \textbf{不存在} \text{固定幂级增益（四层逐一 DEAD）}\\
\textbf{性质}&\text{限定作用域的 closure，}\ \textbf{不是} "BC 再也不可能改进"\\
\end{array}}✓✓$$

$$\mathrm{T3\ Closure}=\mathrm{DEAD}_{\mathrm{fixed\text{-}q}}+\mathrm{R2,R3,R4\ residuals}✓\quad(\text{继承 } \texttt{docs/T3-CLOSURE-fixed-q-scope.md})✓$$

---

## 1. 基线内容（**可引用清单**）

### 1.1 已证／已核（**可引用为已建立**）

| 段 | 命题 | 出处 |
|:--|:--|:--|
| T1 | **BCR Appendix A · Prop 4**：目标形态 $(1.4)$ **best possible up to $\varepsilon$-powers**（匹配下界） | `T1-2-*`／C-7 |
| T1 | **BC 全文无谱机器**（Kuznetsov／spectral／Maass／Petersson／大筛 全 0 命中）；引擎＝**Weil 单点界（附录 A）＋Ramanujan 和＋计数＋C–S 变量选择** | `T1-3-*`／C-8 |
| T1 | **DFI$\to$BC 增量 $\tfrac1{48}\to\tfrac1{20}$ ＝架构变更**（"we keep a **longer diagonal**"）…**非估计改进** | C-9 |
| T1 | (1.3) 双参数族；$\theta<\tfrac12+\tfrac{0.5-r}{1+2(r+2t)}$；DFI$(\tfrac{23}{48},\tfrac12)$／BC$(\tfrac9{20},\tfrac7{20})$ | C-7 |
| T2 | $N_2=\#\{(\ell_2,\ell_2')\}=L^{2+o(1)}$（**变量识别**证明：$(4.26)$ 约束 $(d,d')$、$(4.27)$ **消去** $\tilde\ell_1$） | C-12 |
| T2 | **divisor alignment 无幂次 saving**（差异仅 $\mathfrak p_2^{\pm1},\mathfrak q_2^{\pm1}\Rightarrow\log^{O(1)}L$） | C-13 |
| T2 | $L^5=L_{\rm Weil}L_{\rm transition}L_{\ell_2,\ell_2'}L_u$；$F_3$ **SHARP** | C-2／C-1 |
| T3 | **C1**：$\frac{X}{\sqrt q}\asymp\frac{L}{\mathfrak q_2\sqrt{\mathfrak p_2N}}\ll N^{-2/5}$（$L^*\asymp N^{1/10}$；shortfall $=N^{2/5}$） | `T3-CLOSURE` |
| T3 | **C2**：**aggregation $\ne$ conductor reduction**（聚合不改模数 $\Rightarrow$ 阈值不变） | 同上／C-18 |
| T3 | **C3**：partial diagonal $\subseteq\sigma(u,v,\Delta,\text{coprimality})$ | 同上／C-17 |
| T3 | **C4**：**CRT factorization is not conductor reduction**；$(\mathfrak p_1,n_1')=1$；未找到 $q_0\gg N^\delta$ | 同上／C-19 |
| T3 | 现有 C–S 的**重复结构**：施于 $\{n_1,n_2,a_2,p,q,c\}$ ⟹ 重复 $\{d,a_1,\ell_1,\ell_2\}$（DFI 只重复 $\{\ell_1,\ell_2\}$） | C-17 |

### 1.2 ⚠️ 残项（**未证，不得引用为已证**）

$$\textbf{R2（最关键）}：\ q_0\mid d,\ d\asymp L\ \textbf{只给}\ q_0\le L；\ \text{推不出}\ q_0=L^{o(1)}；\ \text{须证}\ \gcd(d,\mathfrak p_1n_1')\ll L^{o(1)}✓$$
$$\qquad\Longrightarrow\ \textbf{唯一可能直接动摇 C4 的逻辑节点}✓\quad(\text{值得优先补})✓$$
$$\textbf{R3}：a_1,\vartheta\ \text{与}\ q\ \text{的完整互素条件}✓\qquad\textbf{R4}：(4.10)\ \text{全部 coprimality／divisibility 条件穷举}✓$$

### 1.3 🚫 明确**未主张**（防越界）

$$\text{(i)}\ \textbf{不主张} \text{"BC 不可能改进"}；\quad\text{(ii)}\ \textbf{不主张}\ \mathrm{T3}=\mathrm{DEAD\ absolutely}✓$$
$$\text{(iii)}\ \textbf{不主张} \text{"}17/33\ \text{是硬墙"}；\quad\text{(iv)}\ \textbf{不主张} \text{"}\lambda>1\ \text{是 RH 普适必要条件"}✓$$

---

## 2. 基线坐标（**下一轮的出发点**）

$$\text{(i)}\ \textbf{现有 C--S 分区}：T=\{n_1,n_2,a_2,p_1,p_2,q_1,q_2,c\}\ \text{被平方} \Longrightarrow \textbf{重复集}\ \mathcal S=\{d,a_1,\ell_1,\ell_2\}✓$$
$$\text{(ii)}\ \textbf{diagonal}：x=x'\ \big(x=(d,a_1,\ell_1,\ell_2)\big)；\ \text{近对角}\ \mathcal V^*；\ \text{其余}\ \mathcal V\ \text{由}\ \Delta=0/\!\ne0\ \text{与}\ u\ \text{控制}✓$$
$$\text{(iii)}\ \textbf{phase modulus}：q=\mathfrak p_1n_1'（\mathfrak p_1=(\ell_1,n_1)，n_1=\mathfrak p_1\mathfrak p_2n_1'）✓$$
$$\text{(iv)}\ \textbf{有效振荡变量}：\tilde\ell_2\ (\text{范围}\ X\asymp L/(\mathfrak p_2\mathfrak q_2))；\ \text{Weil 作用于}\ n_2'✓$$
$$\text{(v)}\ \textbf{五段账}：\text{T1 无谱引擎｜T2 无固定幂 slack｜T3 振荡四层 DEAD}✓$$

---

## 3. （甲）第一刀 —— **形式化**（本轮只形式化，不执行）

### 3.1 核心问题（**逐字**）
$$\boxed{\textbf{改变什么对象被平方，才能}\ \textbf{同时} \text{改变}\ \textbf{有效重复集} \text{与}\ \textbf{最终 conductor？}}✓✓$$

### 3.2 方法：**候选枚举 ＋ 五段管线**（唐先生给定）
$$\text{先枚举}\ \textbf{C--S 可平方对象的候选集合}\ \{\mathcal C_j\}，\ \text{逐一计算}：$$
$$\boxed{\textbf{重复集}\ \longrightarrow\ \textbf{diagonal constraint}\ \longrightarrow\ \textbf{剩余振荡变量}\ \longrightarrow\ \textbf{phase modulus}\ \longrightarrow\ \textbf{最终}\ L,N\ \textbf{指数}}✓✓$$
$$\textbf{结构联系（本档登记）}：\ \mathcal S\mapsto\big(\text{diagonal},\ \text{振荡变量},\ q(\mathcal S)\big)\ \text{——}\textbf{重复集决定 conductor}✓✓$$
$$\qquad(\text{因}\ \mathfrak p_i,\mathfrak q_i\ \text{皆由}\ \ell\text{-变量与}\ n\text{-变量的 gcd 生成} \Longrightarrow \text{换重复集}\Rightarrow\text{换 gcd 结构}\Rightarrow\text{换}\ q)✓$$

### 3.3 判据（**预登记**，下一轮直接执行）

$$\mathrm{ALIVE}\iff\boxed{\text{新重复结构}\ +\ \text{新模数层／新约束}\ +\ \text{固定幂收益}}\quad(\textbf{三者齐备})✓✓$$
$$\mathrm{DEAD}\iff\boxed{\text{只是把现有}\ \{d,a_1,\ell_1,\ell_2\}\ \textbf{换个排列}} \Longrightarrow \textbf{reparameterization／第一刀即判 DEAD}✓✓$$
$$\qquad(\text{即}\ \mathcal S'=\pi(\mathcal S)\ \text{的置换型改动}\ \textbf{不计} \text{新架构}；\ \text{须}\ \mathcal S'\ne\pi(\mathcal S)\ \text{型}\ \textbf{结构性} \text{改变})✓$$

### 3.4 第一刀**不做**的事（防退化）
$$\text{(i)}\ \textbf{不从} \text{"换一种 C--S"自由发挥；\quad(ii) 不推长估计（先过三判据）}✓$$
$$\text{(iii)}\ \text{不接受"新符号／新命名"作为新架构；\quad(iv) 不重跑 V2-7--V2-11 已审族}✓$$

---

## 4. 下一轮执行清单（first actionable step）

$$\textbf{(甲)-1.1}\ \text{列出全部变量（}d,a_1,\ell_1,\ell_2,n_1,n_2,a_2,p_1,p_2,q_1,q_2,c,m\ \text{等）与可能阶段（第一／第二／额外 C--S）}✓$$
$$\textbf{(甲)-1.2}\ \text{对每个候选}\ \mathcal C_j\ \text{跑五段管线，填表（重复集／对角约束／振荡变量／}\ q\ \text{／指数）}✓$$
$$\textbf{(甲)-1.3}\ \text{三判据筛选：新重复结构？新模数层？固定幂收益？}✓$$
$$\textbf{(甲)-1.4}\ \text{仅对三判据齐备者继续推导；其余判 reparameterization／DEAD}✓$$

$$\Longrightarrow\ \textbf{（甲）-1 的产出格式}：\ \text{一张候选表 ＋ 每行的三判据打钩／判死理由}✓$$
