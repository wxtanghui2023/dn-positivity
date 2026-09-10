# External Mechanism Pre-Screen（E1–E5）

**日期**：2026-09-10 15:40+ ｜ 依据：唐先生指定（优先 E3）｜ 预算：纸面

---

## 0. 登记：外部过表预筛

**搜索逻辑已改变**：
$$\boxed{\text{不是寻找"可能证明 RH 的方法"，而是寻找能提供此前缺失的 }D6\text{ 机制的数学结构}}$$
$$\boxed{\text{什么数学结构能够在不落入 }N1\!-\!N7\text{ 的情况下，原生地产生 }\sqrt X？}$$
**纪律**：E1–E5 **不是** 新的 O6–O10，只是**外部候选入口**；每类最多留**一个机制原型**（禁止 $E1.1,E1.2,\dots$ 墓碑森林）

**六问（Q3 为硬门）**：
```
Q1 它的 primitive 是什么？｜Q2 它如何作用于整数/素数算术？｜**Q3 其 √X 从哪里产生？（硬门）**
Q4 为什么不是 N1–N7？｜Q5 为什么不是已冻结的 Λ/显式公式/谱实现？｜Q6 能否形成可计算的 exact invariant？
```

---

## 1. ⭐⭐ E3：重整化 / 尺度递归（重点审）

**要求（唐先生）**：存在原生尺度变换 $\mathcal R$ 具临界不动点
$$\mathcal R(X^\alpha)=X^{f(\alpha)},\qquad f(\alpha_*)=\alpha_*,\qquad \boxed{\alpha_*=\tfrac12\ \text{由算术结构【唯一强制】}}$$
**与 N1 的本质区别**：N1 是 $H\leftrightarrow X/H$；E3 要的是 **scale transformation itself has a universal arithmetic critical exponent**

### 1.1 ⭐ 反作弊门 A：affine 情形（初等验算）
设 $\mathcal R:\alpha\mapsto a\alpha+b$（$a\neq1$）。不动点：
$$\alpha_*=\frac{b}{1-a}\qquad\Longrightarrow\qquad \alpha_*=\tfrac12\iff a+2b=1$$
$$\boxed{\text{对任意 }a\neq1\ \text{都可取 }b=\tfrac{1-a}{2}\ \text{使 }\alpha_*=\tfrac12\ \Longrightarrow\ \tfrac12\ \text{是【自由选择】，非【被强制】}}$$
⟹ **affine $\mathcal R$ 永远无法"强制" 1/2，只能"规定" 1/2** ⟹ 撞**人为 1/2 插入**陷阱 ⟹ **死**

### 1.2 反作弊门 B：reach / 对数反射
若 $\mathcal R$ 最终只是 $H\mapsto X/H$ 或对数坐标反射 $u\mapsto-u$ ⟹ **N1** ⟹ 死

### 1.3 ⭐ 非仿射算术尺度变换的清单（唯一合法入口）
| 原生尺度变换 | 归纳 |
|---|---|
| 乘法反转 / reach 反射 | **N1**（1.2） |
| 除数自对偶（双曲线型） | **N1 / N43** |
| **Gauss 映射** $x\mapsto\{1/x\}$（连分数重整化） | **Euclid 线已 STOPPED** |
| **筛法 / Mertens 型密度递归** | ⭐ 见 1.4（产生 $\sqrt{\log X}$） |
$$\boxed{\text{非仿射原生候选已全面落 N1 或被 STOPPED；唯一新入口 = 筛法/Mertens 递归}}$$

### 1.4 ⭐⭐⭐ 本轮核心发现：**两个 1/2 活在不同变量里**
```
筛法/Mertens 型递归的自然临界指数：
   密度 ∏(1−1/p)~e^{−γ}/log z ⟹ 自然阈值出现在【log 变量】中：
   PNT 级误差尺度 = X·e^{−c√(log X)}   ⟹ **这里的 1/2 是 √(log X) 的 1/2，不是 √X 的**
而 √X 是【L² 尺度】（已注册：ACA-1 审计 Step 2/4）
⟹ **从 √(log X) 到 √X 的跃迁 = 已注册的 ACA-1「L²→L∞ 转移墙」**
   （不是估计问题，而是 transfer/rigidity 定理问题）
```
$$\boxed{\text{E3 的自然临界指数住在【log 变量】里（}\sqrt{\log X}\text{）；}\sqrt X\text{ 是 L² 尺度；}\\
\text{把前者变成后者正是已注册的 ACA-1 墙 —— 故 E3 不提供独立的 }D6}$$
$$\boxed{\textbf{E3}=\textbf{NO-GO}}\qquad(\text{精确理由：两个 1/2 分属不同变量，其跃迁是已注册的转移墙而非新机制})$$

---

## 2. E2：离散–连续临界机制

**反作弊标准（唐先生）**：
$$\boxed{\sqrt X\ \text{必须在【进入 }\zeta\text{ 理论之前】就已经存在}}$$
（若推导中出现 $\Gamma,\zeta,\text{FE},\text{显式公式}$，而 $\sqrt X$ 只是函数方程的对称点 ⟹ **N3**）
| 规范装置 | 归纳 |
|---|---|
| Poisson / Tate 对偶 | 其产物正是 FE ⟹ 对称点非独立 ⟹ **N3** |
| theta / Gauss 自对偶 | $\lvert\tau(\chi)\rvert=\sqrt q$ ⟹ 有限正交性 ⟹ **N5** |
| 数的几何（Minkowski 型体积阈值） | 体积/测度 ⟹ **N5 / N7** |
$$\boxed{\textbf{E2}=\textbf{NO-GO}}\qquad(\text{无候选满足"}\sqrt X\text{ 先于 }\zeta\text{ 理论存在"这一标准})$$

---

## 3. E1：非交换算术几何

| 规范实例 | 状态 |
|---|---|
| Connes 非交换几何 / 迹-投影机器 | **已审 ⟹ N3**（Connes 2026 审计、P49） |
| 量子群 / Hopf 代数型算术结构 | **N4 / N3** |
| Bost–Connes 系统 | **已关闭**（C-BC 的 D3 审计：模谱真实 ⟹ 只给实尺度） |
| Hilbert–Pólya 重命名 | **禁止项** |
$$\boxed{\textbf{E1}=\textbf{NO-GO}}\qquad(\text{规范实例恰为已审的 duality/projection/representation 与 BC 系统})$$

---

## 4. E4：几何测度 / 熵刚性

**只留下一种情形（唐先生）**：$\tfrac12$ 必须是 **exact rigidity threshold**，而非统计指数
| 自然出现的 1/2 | 判定 |
|---|---|
| Erdős–Kac 型 CLT 归一化（$\sqrt{\log\log n}$） | **统计 ⟹ N7** |
| 维数公式中的 1/2 | Jarník 型 $\dim=2/\tau$；取 $\dim=\tfrac12$ 需 $\tau=4$（**非规范参数**）；<br>而**规范的临界指数是 $\tau=2$，对应维数 $=1$（非 1/2）** ⟹ 无 canonicity |
| norm / 能量 | **N5** |
$$\boxed{\textbf{E4}=\textbf{NO-GO}}\qquad(\text{未发现 }1/2\ \text{的规范级 exact rigidity threshold；出现者或为统计归一化、或为参数依赖维数值})$$

---

## 5. E5：范畴/高阶结构之外的"原生约束"

```
Q1（primitive 是什么？）——【无法回答】：该类未指定任何原生 primitive
⟹ 未通过【入口要求】
⟹ 且其内容【正是】R_4th-irr = FROZEN GAP（第四类不可约性）
```
$$\boxed{\textbf{E5}=\textbf{NO-GO at entry level}}\qquad(\text{注意：不是"被否证为机制"，而是"无生成原则故不予受理"——与 }R_{\rm 4th\text{-}irr}\text{ 同状态})$$

---

## 6. 结果表与后续

| External class | 状态 | 精确理由 |
|---|---|---|
| E1 非交换算术几何 | **NO-GO** | 规范实例 = 已审 N3/N4 + BC 已关 |
| E2 离散–连续临界 | **NO-GO** | 无候选满足"√X 先于 ζ 理论存在" |
| **E3 重整化/尺度递归** | **NO-GO** | **两个 1/2 分属不同变量；跃迁 = 已注册 ACA-1 墙** |
| E4 几何测度/熵刚性 | **NO-GO** | 无规范级 exact rigidity threshold at 1/2 |
| E5 范畴外原生约束 | **NO-GO（入口层）** | 无法指定 primitive ≙ R_4th-irr FROZEN |

$$\boxed{E1\cup E2\cup E3\cup E4\cup E5\ \subset\ N1\cup\cdots\cup N7\quad(\text{本轮预筛范围内})}$$
$$\Longrightarrow\ \boxed{\text{触发唐先生预设的出口：须提出【meta-NO-GO】问题}}$$

### ⭐ meta-NO-GO 问题（正式登记为下一层问题）
$$\boxed{\textbf{M-NOGO}:\ \text{为什么所有【已知】数学结构都只能通过 }N1\!-\!N7\text{ 产生 }\sqrt X？}}$$
```
性质：这不是 RH 攻击，而是一个【分类纲领】——需要分类"一切能产生 √X 的数学结构"
注意：它与 G-SW6 的同型风险 = "没有生成原则的候选搜索会退化为名字生成"
⟹ 故 M-NOGO 必须【先给出问题形式化】（"什么是 √X 的产生机制"），不得直接开始枚举结构
```

## 7. 诚实边界
```
· 第一部分（搜索逻辑改变、Q1–Q6、E1–E5 母类与各自风险/初筛、E3 优先、各反作弊门、E4 只留 exact rigidity 一种情形、
  E2 的"√X 先于 ζ 理论"标准、E5 谨慎、每类最多一个原型、失败则提 meta-NO-GO）——均为唐先生本轮
· §1.1 affine 计算（α*=b/(1−a)，a+2b=1）为【初等严格】
· §1.4 "两个 1/2 分属不同变量"为核心发现，依据已注册的 ACA-1 审计（PNT 尺度 X·e^{−c√log X} vs RH 的 L² 尺度 √X）
  ⟹ 为【结构性论证 + 既有登记引用】，非新定理
· §1.3 清单、§2/§3/§4 各实例归纳、§5 的 E5 判定为【结构性预筛】，非穷尽性 NO-GO
· §4 的 Jarník 型维数公式（dim=2/τ，规范临界 τ=2 ⟹ dim=1）为【经典事实】；"无 canonicity"为结构性判断
· M-NOGO 为登记的问题，尚未形式化；须防其退化为无生成原则的枚举
· 未写代码、未做数值；未引入 ζ 零点或谱算子；全文未使用 Λ
```

## 8. 提交链
```
53ca61c 冻结基准总表 → 本篇（External Pre-Screen E1–E5）
```
