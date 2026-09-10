# R8-C†-B1：Epstein/theta 反例审计（唐先生执行）

**日期**：2026-09-10 14:05+ ｜ 预算：纸面 ｜ 判定：**(b) 不是 L3′ 的反例，而是其正面证据**

---

## 1. 审计结果

### 1.1 已确认的两条
$$\boxed{\text{FE}\ \not\Rightarrow\ \text{Euler product}}\qquad\boxed{\text{zero-blind spectral duality}\ \not\Rightarrow\ \text{Euler multiplicativity}}$$
（一般二元正定二次型的 Epstein zeta 有完整函数方程而**无 Euler 积**；文献明确。）

### 1.2 Epstein FE 的来源 = **theta/Poisson**
$$\Theta_Q(t)=\sum_{x\in\mathbb Z^n}e^{-\pi tQ[x]}\ \xrightarrow{\text{Poisson}}\ \Theta_Q(t)=t^{-n/2}(\det Q)^{-1/2}\Theta_{Q^{-1}}(1/t)$$
Mellin 后：
$$\pi^{-s}\Gamma(s)Z_Q(s)=(\det Q)^{-1/2}\pi^{s-n/2}\Gamma(n/2-s)Z_{Q^{-1}}(n/2-s)$$
$$\boxed{\text{lattice}\to\text{Poisson}\to\text{dual lattice}\to\text{Mellin}\to\text{FE}}\qquad(\text{非神秘的非-Euler reciprocity})$$
**且**：适当的整数性/偶性/level 条件下，$\Theta_Q$ 是 modular form，或更一般地是 **Weil 表示下的 vector-valued modular form**
$$\boxed{\text{theta reciprocity}\ \subset\ \text{Weil/modular spectral mechanism}}$$

### 1.3 硬审计：Z2 / Z3 反而不通过
$$\boxed{\text{Poisson reciprocity}\ \neq\ \text{Kloosterman reciprocal-phase reciprocity}}$$
```
Poisson：kernel = e^{2πi⟨x,ξ⟩}（lattice Fourier 对偶，x↔ξ，t↔t⁻¹）
Kuznetsov 几何侧需要：S(m,n;c)=Σ_{d mod c}* e((md+n d̄)/c) —— 含 **d ↦ d⁻¹ mod c**（有限环单位群 reciprocity）
⟹ Epstein/Poisson 本身【不能自动填充 Z2】
```
$$\boxed{\text{Weil-locality}\ \neq\ \text{CRT-locality（Z3）}}$$
（Epstein 的天然结构是 lattice/discriminant-group 分解 $D=L^\#/L$ + Weil 表示，不等于 $R_{q_1q_2}\simeq R_{q_1}\otimes R_{q_2}$）

### 1.4 Z4 是最强处，但核不同
```
Epstein/theta：Θ →^S ρ(S)Θ，含 S²、(ST)³ 表示关系 ⟹ **QSC 强版本 ✓**
但 QSC ⇏ Kuznetsov：其谱核是 **theta/Weil 型**，不是 Kloosterman/Kuznetsov 型
```

## 2. 四象限表（唐先生）
| 机制 | Z2 | Z3 | Z4 | Z5 | modular/spectral |
|---|:-:|:-:|:-:|:-:|---|
| **Epstein/theta** | △ | △ | ✓ | ✓ | ✓ |
| Kuznetsov | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ruelle/量子图 | × | × | ✓/△ | ✓ | 非算术 |
| Λ 标准 Mellin | × | × | × | × | zero residues |

**⟹ (b) 的真实身份**：
$$\boxed{\text{non-Euler but modular/Weil-spectral example}}\qquad\text{而【非】"non-modular zero-blind QSC counterexample"}$$

## 3. L3′ → **L3″**（唐先生）与新未知空间

**为何 L3′ 原形式不能证明**：QSC 至少有两种**结构不同**的实现——
$$\text{Type I（Kuznetsov）}:\ \text{finite reciprocity}\to\text{Kloosterman}\to\text{Bessel}\to\text{automorphic spectrum}$$
$$\text{Type II（theta/Weil）}:\ \text{lattice Fourier duality}\to\text{theta}\to\text{Weil rep}\to\text{modular spectrum}$$
$$\boxed{\textbf{L3}^{\prime\prime}:\ Z2+Z3+QSC+Z5\ \Longrightarrow\ \text{representation-theoretic spectral realization？}}$$
分三支：Weil/theta 型 ｜ automorphic/Kuznetsov 型 ｜ **genuinely new 型**（Epstein 已填实第一支）
$$\boxed{\mathcal N=\{\text{zero-blind arithmetic QSC systems}\}\setminus\{\text{Weil/theta}\cup\text{automorphic}\}}$$
**对 Λ 的意义（唐先生）**：不是"没有 Euler 积也行，所以 Λ 有希望"，
而是"**没有 Euler 积完全不是障碍；关键是是否存在一个独立的 representation-theoretic reciprocity engine**"。
Epstein 的 engine = lattice duality/theta/Weil；**Λ 目前缺这一层次的对象**。

---

## 4. ⭐ 小灵补三点

### 4.1 把 Z2 的对偶类型命名（可检验的语言）
$$\boxed{\text{inversion reciprocity（乘法群反转 }d\mapsto\bar d\text{）}\quad\text{vs}\quad\text{Fourier duality（加法群特征对偶）}}$$
Kloosterman 建在**乘法群** $(\mathbb Z/q)^\times$ 的反转上；theta 建在**加法群**的字符对偶上。
⟹ 二者是**不同对偶类型**；候选第三类必须提供**第三种对偶类型**。

### 4.2 分类形状：局部域对偶的完整清单（结构性）
```
在 ℚ_p / ℝ 上可用的"对偶引擎"清单很短：
 ① 加法群 Pontryagin 自对偶（Fourier/Poisson）
 ② 乘法群特征论（反转 → Kloosterman/Gauss）
 ③ 二者的【综合】= Tate 的 adelic 局部-整体对偶 ← **其解析延拓产出 ζ 的零点**
⟹ 若 reciprocity engine 必须【由局部域结构装配】，则第三类候选 = ①②③ 之外
⟹ 唯一的已知"非对偶型"候选 = 算术微分（Buium δ 几何）——**门⑩已因尺度（p-adic/height）关闭**
```
$$\boxed{\text{（结构性）"genuinely new 型"若存在，须是【非对偶型】引擎；而已知非对偶候选类已在门⑩关闭}}$$

### 4.3 ⭐⭐ QSC 的"二次性"= GL₂-结构 ⟹ 与门⑰同一件事
```
Type I（Kuznetsov）：Kloosterman 来自 **GL₂**（2×2 矩阵 / 模群作用）
Type II（theta/Weil）：Weil 表示是 **GL₂ 的（metaplectic）表示**
⟹ **两种已知实现都是"GL₂-二次"结构** ⟹ QSC 很可能【正是】"要求 GL₂-型（metaplectic/automorphic）表示论"
⟹ 而对 GL(1) 对象（ζ / Λ），其二次提升 **Sym²(平凡)=平凡**
   ⟹ **无 GL₂-二次结构可用** = 门⑰（引擎平凡化）的同一现象
```
$$\boxed{\text{R8 的 QSC 条件 与 门⑰ 的"引擎平凡化"很可能是【同一件事】}}$$
（标【结构性论证】；若成立，则 L3″ 的形式可大幅收紧为"QSC ⟹ GL₂-结构"）

---

## 5. 下一刀（唐先生指定 + 我的具体化）
$$\boxed{\text{Z2 reciprocal phase}+\text{Z3 CRT factorization}+\text{Z4 quadratic closure}\ \stackrel{?}{\Longrightarrow}\ \text{某种有限 adelic/representation-theoretic kernel？}}$$
**分类目标**：$\text{finite arithmetic reciprocity}\to\{\text{Kloosterman/automorphic}\ |\ \text{Gauss/Weil/theta}\ |\ \textbf{? genuinely new}\}$
```
· 若第三类存在 ⟹ **R8 当前最值得追的活口**
· 若第三类不存在 ⟹ 得到有力度的受限 NO-GO：
    Z2+Z3+QSC+Z5 ⟹ Weil/automorphic representation-theoretic realization
  然后再检查 Λ 能否进入该 representation-theoretic envelope
```
**我的具体化建议**（结合 §4.2/§4.3）：先判"第三类是否必须为非对偶型"，若是，则第三类 = 已关闭的算术微分候选；
再判"QSC 是否即 GL₂-结构"，若是，则用门⑰的 Sym² 平凡化直接给出 Λ 的排除条件。

## 6. 诚实边界
```
· §1 的 Epstein FE/Poisson/Weil-modular 结论为唐先生核实（文献级）
· §2 四象限表为结构性整理；△ 表示"未通过完整入口测试"
· §4.1 的对偶类型命名为语言层面整理（可检验）
· §4.2 的"局部域对偶清单"为【结构性整理】，其完整性未证明
· §4.3 的"QSC = GL₂-结构"为【结构性论证】，未形式化；与门⑰的连接亦为结构性
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 7. 提交链
```
f115b44 ZBV audit r1 → 本篇（B1：Epstein/theta）
```
