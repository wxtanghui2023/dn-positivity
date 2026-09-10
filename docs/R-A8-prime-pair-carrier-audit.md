# R-A8 审计记录：Unconditional Prime-Pair Carrier（第一轮，唐先生执行）

**日期**：2026-09-10 13:34+ ｜ 协议：`PROTOCOL-R8-prime-pair-carrier.md` ｜ 预算：纸面，无代码
**裁决**：$$\boxed{\textbf{R8-B（当前）｜ R8-C 未证 ｜ R8-A 未证 ｜ R8-D 已排除}}$$

---

## Gate 0 — RH Contamination Audit（逐方向）

| 环节 | 标记结论 |
|---|---|
| **G0-1** $J(X,H)=\int_X^{2X}(\psi(x+H)-\psi(x)-H)^2dx$ 的定义 | **unconditional；RH=否；zero statistics=否** ✓ |
| ⚠️ 规范化附注 | 展开式 $\sum_{h\le H}(H-|h|)\sum_{n\sim X}\Lambda(n)\Lambda(n+h)$ **结构上成立**，但**公式层面必须规范化**（三角权、端点项、ψ 的连续平均）；不得写成未经处理的无条件精确恒等式 |
| **G0-2** prime-pair → $J$ | 展开平方、交换求和/积分 ⟹ **unconditional；不需 RH；不需 zero statistics；不需 HL；基本是等价转换；尚不能称为新 β-sensitive info** ⟹ **prime-pair 是 J 的真实 carrier** ✓ |
| **G0-3** $J\leftrightarrow$ zero pair correlation | **LPZ 明确描述 GM 定理为"在 RH 下"**；**Chan：strong pair correlation ⟺ 短区间素数两个二阶矩，under RH** ⟹ **不是已知的无条件独立桥** |
| **G0-4** Hardy–Littlewood 路线 | 短区间方差可由 HL 型素数对猜想导出 ⟹ **HL 本身即强未解决算术输入**，不是现成无条件 carrier |

**Gate 0 裁决**：
$$\boxed{\text{prime pairs}\overset{\text{代数}}{\longrightarrow}J\overset{\text{显式公式}}{\longleftrightarrow}\text{zero pair correlation}}$$
**右侧强等价目前带 RH 条件。未发现隐藏的"独立无条件 prime-pair → zeros"通道。**
⟹ R8-C 的"已等价于零点信息"**暂不能成立为定理**（只能说已知强结果落入该等价框架）。

---

## ⭐ Gate 1 — H↔λ 字典（本轮最有价值结果）

```
Montgomery pair correlation：X = T^λ
短区间长度：H = X^η
Goldston–Montgomery 参数对应：T ≍ X/H ⟹ T ≍ X^{1−η}
⟹ X = T^λ 给出
```
$$\boxed{\lambda=\frac{1}{1-\eta}\qquad\Longleftrightarrow\qquad \eta=1-\frac1\lambda}$$
**关键节点**：
$$\lambda=1\Longleftrightarrow\eta=0\ (H=X^{o(1)}\ \text{边界})$$
$$\lambda>1\Longleftrightarrow H=X^{\eta},\ 0<\eta<1$$
$$\boxed{\lambda=2\Longleftrightarrow H=X^{1/2}\ (\text{自对偶长度})}$$

**⟹ R8 的决定性问题被完全改写**：
$$\boxed{\lambda_\zeta\ge2\ \Longleftrightarrow\ \text{能否【独立无条件】获得 }H\sim\sqrt X\ \text{尺度的正确二阶素数方差？}}$$
**⚠️ 关键校正（唐先生）**：不能把"无条件几乎处处一阶素数计数可达 $H\ge X^{1/6+o(1)}$"当作 λ>1 的证据——
那是**一阶平均**（$\psi(x+H)-\psi(x)\sim H$ 对 almost all $x$），
而 R8 需要的是**二阶方差的精确主项**。**两个信息等级不可混淆。**

---

## 三箭审计

| 箭 | 内容 | 裁决 | 失败性质 |
|---|---|---|---|
| **箭 1** | prime-pair → $V/J$ | **PASS** | 纯算术恒等/展开层面；是真实 carrier，非重命名 |
| **箭 2** | $V/J\to\lambda_\zeta>1$ | **FAIL（当前）** | **不是 carrier 不存在，而是 carrier 的无条件二阶评价不足**——需在对应 $H=X^\eta$ 范围**均匀成立**的二阶主项；2024 综述明言此 variance asymptotic "very little is known unconditionally" |
| **箭 3** | $\lambda>1\to\lambda\ge2$ | **FAIL（当前）** | 需把独立控制推到 $H\sim\sqrt X$ 且达可识别正确二阶主项的精度；**目前不能称其"结构性等价于 RH"** |

## 三问裁决

```
Q1 独立性：**定义层 YES**（纯算术对象）；**已知强渐近层 NO independent unconditional source known**
          （GM 等价桥带 RH；BKS 明确一般缺乏可用 HL 型算术自相关输入）
   ⟹ 写成：**carrier 独立；所需精度的独立供给未知**
Q2 跨越性：λ>1 未实现；λ≥2 未实现（但**不等于不可能**）
Q3 非等价性：**定义层 non-encoding YES**；但**强渐近层**已有 RH 下的 $J\leftrightarrow$ pair correlation 等价定理
   ⟹ 准确表述：**carrier 非编码，但其"足够精确的统计律"可能进入与 zero statistics 等价的层级（未证）**
```

## R8.2 的登记新 R
$$\boxed{R_8^{(1)}:\ \lambda=\frac{1}{1-\eta},\quad H=X^\eta;\qquad \lambda>1\iff\eta>0;\qquad \lambda=2\iff H=\sqrt X}$$
把模糊的"prime-pair 数据能否推 support"变成**明确的尺度问题**：
$$\boxed{\text{能否在 }H=X^\eta\ (\eta>0)\ \text{的正幂尺度上，独立无条件地得到正确的二阶 prime variance？}\quad(\text{RH 强度目标：}H\sim\sqrt X)}$$

## 本轮研究判断
$$\boxed{\underbrace{\text{prime-pair carrier}}_{\text{真实、非编码}}\xrightarrow[\ \text{缺失}\ ]{\text{独立无条件二阶评价}}\lambda_\zeta>1\xrightarrow[\ \text{更大缺口}\ ]{}\lambda_\zeta\ge2}$$
**不做坐标跃迁；不宣布 R8-C。** 下一轮不再审"有没有 prime-pair 数据"（答案：有），
而是审 **R8.2：现有无条件技术的"精度缺口"究竟是什么**（见 `PROTOCOL-R8.2-precision-gap.md`）。
**R8-D 排除**：字典已建立 ⟹ 这次不是坐标混淆，而是**真正的算术精度缺口**。

## 诚实边界
```
· 第一轮结论为唐先生执行并签署；文献依据：LPZ (JMAA 2012)、Chan (JLMS)、BKS (ORA)、
  Montgomery–Soundararajan (PMC)、IMRN 2023 综述、Math. Z. 2024 综述 —— 均标【文献级】
· "未发现隐藏通道"是在所列文献范围内的判定，非穷尽性定理
· Gate 1 字典的推导（T ≍ X/H ⟹ λ = 1/(1−η)）为参数对应，须在执行 R8.2 时以原文参数约定核对
· 未写代码、未做数值
```

## 提交链
```
a0ecd28 R8 协议+勘误 → 本篇（R8 第一轮记录）
```
