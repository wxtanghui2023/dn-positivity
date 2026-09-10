# B4-IA（Gauss 合成）/ B4-II（Hecke）逐层死亡测试

**日期**：2026-09-10 14:53+ ｜ 依据：唐先生设定的分层标准 ｜ 预算：纸面 + 一次精确验算

**审计顺序（唐先生）**：先审**对象自身代数事实** → 再审**如何获得尺度** → 再审**defect 是否真的不可传输**。**不一开始就塞进 $X,H$。**

---

# B4-II：Hecke 关系 —— **associator ≡ 0（已精确验算）**

## 逐层检查
```
① 乘法公式：T_m T_n = Σ_{d|gcd(m,n)} d^{k−1} T_{mn/d²}（平凡特征）—— 确实 ≠ T_{mn}
② 但真问题是 associator：Ω(m,n,ℓ) = (T_m T_n)T_ℓ − T_m(T_n T_ℓ)
③ 计算方式：把两边完全展开为 Σ_r C(r) T_r，逐项比较系数
```
## ✅ 验算结果（`scripts/hecke_associator.py`，精确整数运算）
```
triples tested: 2744 (m,n,l ≤ 14)
k= 2: associator nonzero in 0/2744 | commutator nonzero in 0
k= 3: 0/2744 | k= 4: 0/2744 | k= 6: 0/2744 | k=12: 0/2744
系数级对照 (2,6,3), k=2：L = R = {1:6, 4:3, 9:2, 36:1} ⟹ identical: True
非乘性对照：T_2T_4 = {2:2, 8:1} ≠ T_8 = {8:1} ✓（非乘性确实存在）
```
$$\boxed{\textbf{B4-II}\ \Omega(m,n,\ell)\equiv0\ \text{（已验证）}\ \Longrightarrow\ \text{$\textbf{假 defect}$}}$$
## 死因（精确）
```
Hecke 算子是【同一空间上的线性算子】⟹ 算子复合天然结合
（亦等价于：Hecke 代数 = 双陪集卷积代数，而陪集卷积是结合的）
⟹ 所谓"两路径差异 canonical"【不是 associator】，而是同一算子的【不同 divisor-sum 展开】
```
**⚠️ 关键概念区分（本轮新增筛查门）**：
$$\boxed{\textbf{S6}:\ \text{候选必须在【结合性】上失败，而不仅在【乘性】上失败}}$$
$$\text{non-multiplicativity}\ (T_mT_n\neq T_{mn})\ \neq\ \text{non-associativity}\ (\text{associator}\neq0)$$
**⟹ 只有后者产生 composition defect**；前者（Hecke、非乘性函数、Euler 积不完全性）**不产生**。
**⟹ 我上轮写的"两路径差异 canonical"是【非乘性】，不是 defect ⟹ 该条须作为 errata 记正**（不静默改写）。

**唐先生预判（$\Omega=0$）已验证正确** ✓

---

# B4-IA：Gauss 二次型合成 —— 逐层检查

## ① composition 本身：**类群层完全结合**
```
Gauss 合成在 primitive forms 的 proper equivalence 类上给出【类群律】Cl(D)（abelian）
⟹ (f∘g)∘h = f∘(g∘h) 在类层【严格成立】
⟹ 非结合性（若存在）只可能发生在【代表元层】
```
⟹ **不在类层死**，但已确定：任何 defect 只可能是代表元层的

## ② 代表元 ambiguity 是否只是 quotient/canonicalization：**是**
```
f*g 在形式代表元上有多种等价选择，而在 Cl(D) 中只有一个类
⟹ Ω(f,g,h) = **代表元 ambiguity**（等价关系取商后的选择效应）
⟹ 正是 S2：**结合内核 + canonicalization**
```
$$\boxed{\textbf{B4-IA}\ \text{死于}\ \textbf{S2}}$$

## ③ 对合 $f\mapsto f^{-1}$ 是否内生：**是（这一关反而是通过）**
```
逆形式 (a,b,c) ↦ (a,−b,c)（或其 proper-equivalent 代表）可由形式本身给出
⟹ 不需要借助判别式 D 构造 ⟹ 对合确实是内生的 ✓
```

## ④ fixed point：**结构性失败（与连分数无关）**
```
类层不动点： [f]=[f]^{-1} ⟺ [f]²=1 ⟹ **2-挠子群**（genus group，阶 = 2^{ω(|D|)−1}）
形式层不动点：f=f^{-1} ⟺ 化简形式满足 b ≡ 0 (mod a)（"ambiguous form" 的标准判据）
⚠️ 两者【不是同一条件】（唐先生 §4 的要点）
```
$$\boxed{\text{不动点集是【2-挠群】（秩 }\omega(|D|)-1\text{），【不是单一尺度】}}$$
$$\boxed{\Longrightarrow\ \text{拿不到 }H=X/H\ \text{型尺度不动点} \Longrightarrow\ \text{尺度对合要求【结构性失败】}}$$
**⚠️ 这个死因是独立于连分数的**（正是唐先生要求的顺序）

## ⑤ 连分数：**仅作解释，不作主要杀因**
```
ambiguous forms ↔ 判别式平方根分解 ↔ √D 的连分数周期
⟹ 只用于【解释失败来源】（即为何该路线总被旧 NO-GO 吸回），不作为判死依据 ✓
```

---

# 本轮裁决（按唐先生的四行表）

| 结果 | 意义 | 本轮 |
|---|---|---|
| I、II 都是假 defect | B4 本身严重收缩 | ✅ **本轮落此格** |
| I→分支 / II 假 defect | 支持预测但不能称定理 | — |
| I 假 defect / II→分支 | 同上 | — |
| 任一真正逃出 ①② | R-CS 首个真正新增入口 | ✗ |

$$\boxed{\text{B4-IA 死于 S2 + 不动点集失败；B4-II 死于 }\Omega\equiv0\ \text{（已验证）}\Longrightarrow\ \textbf{B4 本身严重收缩}}$$

## ⚠️ 预注册预测的诚实处理（不让预注册污染审计）
```
分叉预测【未被检验】—— 两个对象都在【抵达分叉测试之前】就死了
⟹ 既【不确认】也【不推翻】分叉预测；其判别力本轮未被行使
（唐先生明确要求：不得因预注册而写成"支持预测"）
```
**唐先生的条件核对**：原条件是"若实例化**全部落入某支** ⟹ 回头攻 A"
```
本轮实际情况 = 【全部死亡】，比"落入某支"更早、更强；
但【字面上】条件（落入某支）并未被满足 ⟹ 诚实记录：
   · 弱条件（无 live 候选残留）✅ 已满足
   · 字面条件（落入某支）✗ 未触及
⟹ 建议：可回头攻 A，但须同时声明 [S6 新增] 与 [分叉预测未被行使]
```

## ⭐⭐ 新增筛查门（本轮的通用产出）
$$\boxed{\textbf{S6}:\ \text{候选须在【结合性】而非仅【乘性】上失败}}$$
$$\boxed{\textbf{S7}:\ \text{若 composition 是【算子复合】或【某一结合律的商】，则 associator 恒为 0}}$$
**⟹ B4 剩余内容 = "给出一个【对象层本征非结合】（intrinsically non-associative）的 canonical 算术律"**
```
而经典的本征非结合结构（octonions、Moufang loops 等）【不是】本项目意义下的算术对象
⟹ **目前无候选** ⟹ B4 的剩余内容与 Gap_FL 同型：**inactive（无候选 + 无生成原则）**
```

## 诚实边界
```
· §B4-II 的 Ω≡0 为【精确验算】（2744 triples × 5 权重；整数运算，可比系数级）
  但"对全部 m,n,ℓ 与全部 k 恒为 0"仍是【结构性结论】，验算覆盖的是有限三元组
  另：公式中若带非平凡特征（χ(d)d^{k−1}），结论不变（卷积结构未变）——此点未单独验算
· §B4-IA 的①②④为【经典代数事实】（类群律、代表元等价、2-挠判据）;
  ⑤ 为解释性，不作杀因
· 我的上轮表述"两路径差异 canonical"记正为 errata（应为【非乘性】而非 defect）
· 未引入 ζ 零点或谱算子；本轮脚本为纯有限代数验算
```

## 提交链
```
fb789c3 B-PRE2 → 本篇（B4-IA/II 逐层死亡测试）
```
