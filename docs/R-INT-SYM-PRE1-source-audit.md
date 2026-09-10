# R-INT-SYM-PRE1：内部对称的原生算术来源审计

**日期**：2026-09-10 15:00+ ｜ 依据：唐先生设定（不放 Λ；先来源分类，不枚举名词）｜ 预算：纸面（无代码）

**目标**：找 $(\theta,J,\mathcal A_X)$，使 $\sqrt X$ 是**内部对称的 fixed locus**，而非 reach 边界
$$\mathcal S(X,H,\theta),\qquad J(X,H,\theta)=(X,X/H,\theta'),\qquad J^2=1$$
$$\text{真 fixed locus}:\ H=\sqrt X\ \wedge\ \theta=\theta'\qquad\text{且}\ \boxed{\theta=\theta'\ \text{必须提供【独立于 }H=X/H\text{ 】的算术约束}}$$

---

## 0. 一条前置结构性观察（小灵）
```
要 θ=θ' 成为【非平凡】约束，θ 必须在 J 下【变到另一个值】（J-反协变）：
   若 J(θ)=θ 则 θ=θ' 自动成立 ⟹ 无约束（杀）
   若 θ 只由两支 reach 决定且 J-反协变 ⟹ θ 必为 reach 差的函数 ⟹ θ=0 ⟺ two reaches 相等 ⟹ N43
```
$$\boxed{\text{⟹ θ-A 类的结构性杀因（在枚举之前即已确定）}}$$
**⟹ θ 必须【不由两支 reach 决定】，而由两通道的【交互数据】决定**

---

## 1. θ-A：局部组合型（θ 描述两通道的兼容方式）

| 实例 | 内容 | 死因 |
|---|---|---|
| A1 | $\gcd(a,b)\cdot\operatorname{lcm}(a,b)=ab$ 的"增益" | **恒等式** ⟹ 障碍恒为 0（Integrability–Null Pincer 腿(i)） |
| A2 | reach 差的任何函数（如 $\log(a/b)$） | 由 §0：fixed locus = reach 重合 ⟹ **I3/I4 失败（N43）** |
| A3 | 平方因子缺陷 $\Omega(n)-\omega(n)=\sum_p(v_p(n)-1)$ | J-不变（无 reach 对换）⟹ **I2/I3 失败**（且 fixed locus = 无平方因子，与尺度无关） |
| A4 | 判别式型 $(a+b)^2-4ab=(a-b)^2$ | scale-invariant 且在 swapping 下**不变** ⟹ θ=θ' 自动成立 ⟹ **无约束** |

$$\boxed{\theta\text{-A}:\ \text{全部失败；结构性原因 = §0（J-反协变的 reach 函数必以重合点为零点）}}$$
**⟹ θ-A 需要一个【非 reach】的第三数据源；本轮无候选**

## 2. θ-B：相位/符号型

| 实例 | 内容 | 死因 |
|---|---|---|
| B1 | Legendre/Jacobi 符号 | **重命名的 Dirichlet character** ⟹ 违反禁止项（且 Kloosterman 封闭证据强） |
| B2 | **Gauss 和相位** $\tau(\chi)/\sqrt q$ | 确为加×乘共同生成 ✓；但 $|\tau(\chi)|=\sqrt q$ 来自**有限正交性**（Parseval）⟹ **= 门⑬"char 0 的无条件 √ 只来自有限性"** ⟹ 是【常数特征】而非 fixed locus ⟹ **I3 失败**（无尺度动力学） |
| B3 | Liouville/Möbius 符号 $(-1)^{\Omega(n)}$ | 纯乘法 ⟹ **Sym(ℙ)-协变** ⟹ 无绝对尺度（B1 死因模式）⟹ **I2 失败** |

$$\boxed{\theta\text{-B}:\ \text{全部失败；死因分三类：重命名 character ／ 有限性 }\\sqrt{\ }\text{ ／ Sym(ℙ)-协变}}$$
**⭐ B2 最具信息量**：它表明算术中"自然出现的 $\sqrt{}$"（Gauss 和模长）**恰恰是门⑬已登记的有限性来源**，不是尺度 fixed point。

## 3. θ-C：组合障碍型（"两个算术结构能否同时实现的内部 obstruction"）

**⭐⭐ 本轮关键识别**：算术中**最自然的"兼容性 obstruction"就是互反律符号**
```
二次互反： (a/b)(b/a) = (−1)^{((a−1)/2)((b−1)/2)}
⟹ 该符号【正是】"a 模 b 与 b 模 a 能否同时相容实现"的 obstruction ✓（完全符合 θ-C 的描述）
⟹ 由 (a mod 4) 与 (b mod 4) 生成 ⟹ **确为加×乘共同生成** ✓（非重命名 character）
```
**⚠️ 但它死于 I2（无尺度 reach）**：
```
互反对合交换 a↔b（labelling/class 层），【不携带 H 与 X/H 的 scale reach】
⟹ θ 的对称性作用在【素标号/类群侧】，无绝对尺度 ⟹ I2 失败（= B1/§8.28 死因模式）
```
**⭐ 且它已在本项目被关闭过（更深层的解释）**：P47-G2.5 **Pure Reciprocity Detector No-Go**
（Legendre/quartic 符号：R2 失败于 5+4i 反例；R3 no-go：纯互反探测器只分离类、不给精确代表元）
$$\boxed{\text{本轮在【内部对称】语境下重新解释该 no-go：互反 obstruction 落在标号侧，无尺度，故不可能供 }H\leftrightarrow X/H}$$

## 4. ⭐ 判决与结构性诊断

$$\boxed{\textbf{R-INT-SYM-PRE1}:\ \text{三类 }\theta\text{ 均无实例通过 I1–I5}}$$
| 类 | 死因 | 落点 |
|---|---|---|
| θ-A | §0 结构性：J-反协变的 reach 函数 ⟹ fixed locus = 重合点 | **N43 支** |
| θ-B | 重命名 character ／ 有限性 √（门⑬）／ Sym(ℙ)-协变 | **Sym(ℙ) 支 + 已关闭源** |
| θ-C | 互反 obstruction 在标号侧，无 scale reach | **Sym(ℙ) 支** |

**⭐⭐ 分叉预测【本轮被真正行使】且成立**
```
此前 B4 的两个对象在抵达分叉测试前即死 ⟹ 分叉预测未被行使（已诚实记录）
本轮三个 θ 类【全部落入二分的一支】：θ-A ⟹ archimedean/两范围支；θ-B(部分)/θ-C ⟹ Sym(ℙ)-协变支
⟹ 预测在 R_int_sym 语境下【获得一次有判别力的检验】（但仅 3 类少数实例，非穷尽性）
```
**⟹ 结构性诊断**：
$$\boxed{\text{θ 的对称性【容易找到】（互反、共轭、奇偶），但它总是作用在【标号/类】侧，而那里没有尺度 reach}}$$
$$\boxed{\text{要逃出，需要 } \theta\ \text{既【不是 reach 的函数】、又【不在标号侧】\ ——\ 目前无候选}}$$

## 5. 当前状态与必产 R
$$\boxed{\mathrm{R\_int\text{-}sym}:\ \textbf{仍活跃，但本轮未找到入口};\ \text{新的精确残余见下}}$$
$$\boxed{\text{残余形式：一个 }J\text{-反协变的内部变量 }\theta\text{，其数据源【既非两 reach，亦非标号/类】}}$$
**S 门汇总（本轮新增使用）**：S1–S8 全部投入实际预筛；**S8 未触发**（无单调 resolution 候选），§0 的观察实为**新门 S9**：
$$\boxed{\textbf{S9}:\ J\text{-反协变且仅由两支 reach 决定 } \Longrightarrow \text{ fixed locus = 重合点 } \Longrightarrow \text{ N43}}$$

## 6. 诚实边界
```
· 本轮的三个类别划分、I1–I5、S1–S8 检验要求为唐先生设定；实例枚举与判定为小灵
· §0 的观察为【严格推理片段】：J-反协变 + 仅依赖两 reach ⟹ 零点在重合处（可形式化，但尚未写成引理）
· §1 的 A1（恒等式）、A4（判别式在 swapping 下不变）为【初等事实】；A3 的 J-不变性为初等
· §2 的 B2（|τ(χ)|=√q 来自有限正交性）为【经典事实】，且与门⑬的登记【一致】
· §3 的互反符号公式为【经典事实】；"它 = θ-C 的规范实例"为小灵的【结构性识别】
· "分叉预测被行使且成立"限于【3 类少数实例】，**非穷尽性结论**
· 严格遵守"不放 Λ"：全文未出现 Λ 或 $\Lambda(n)\Lambda(n+h)$ 的设计用途
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 7. 提交链
```
e4c74db R-CS 受限封存 → 本篇（R-INT-SYM-PRE1）
```
