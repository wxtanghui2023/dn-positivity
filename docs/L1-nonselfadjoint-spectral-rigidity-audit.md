# L1 审计：Non-Selfadjoint Spectral Rigidity（文献审计，不写代码/不做数值）

**日期**：2026-09-10 ｜ 起点 `f31779c`（研究操作系统封版点）｜ 结论：**L1 = NO-GO**，但理由比"未找到"精确

---

## 0. 审计的唯一问题（唐先生指定）
$$\exists\,\mathcal P(A)\ge0\ \text{（}A\neq A^*\text{）}\quad\text{使}\quad \mathcal P(A)\Longrightarrow \Re\operatorname{ResSpec}(A)=c$$
且：不自伴化、不把 resonance 重定义为自伴算子本征值、不依赖 ζ 零点位置、不退化为 Weil / boundary unitarity / 函数方程配对 / 迹公式 / numerical range 描述性包含。

## 1. 文献中的理论族（**存在**）
```
① numerical range (Hausdorff–Toeplitz)：σ(A) ⊂ W(A)（凸）——但见 §2 的反证
② accretive / m-sectorial：Re⟨Ax,x⟩ ≥ 0 ⟹ σ ⊂ 右半平面（扇形同理）
③ quadratic numerical range（块算子矩阵）：可给出【不含谱的竖条】(vertical strip free of spectrum)
④ Krein / Pontryagin 空间 + definitizable 算子（Krein–Langer）：
   A 为 J-自伴且 ∃ 多项式 p 使 [p(A)x,x] ≥ 0 ⟹ 【非实谱至多有限个】
⑤ J-self-adjointness / 相似于自伴（R-S 算子）类：谱实 + 完备性判别
```

## 2. ⭐ 硬信息一：非自伴情形下 numerical range 包含可以是**空的**
文献明载（Prague 讲义 §1.2.1）：
```
· "no variational replacement of this type is available in the non-self-adjoint case"
· m-sectorial ⟹ σ ⊂ Num(H)，但"such estimates are typically very rough and not useful"
· 反例：imaginary Airy oscillator −d²/dx² + ix 在最大定义域上【谱为空集】，
        而 numerical range = 整个右半平面
· 且 W(T) 内部可有巨大 resolvent 范数（伪谱）⟹ numerical range 不是可靠定位器
```
$$\boxed{\text{⟹ "正性/numerical range ⟹ 位置" 在非自伴情形【原则上不可靠】}}$$

## 3. ⭐ 硬信息二：最强的正性→定位定理，其输出几何**不是** RH 所需
`definitizable`（Krein–Langer）给出最强的正性定位结论：
$$\boxed{\text{J-自伴 + definitizable}\ \Longrightarrow\ \text{非实谱【至多有限个】}}$$
$$\boxed{\text{其输出 = "谱实（Im}=0\text{）除有限例外"，而不是"谱落在指定竖直线（Re}=c\text{）"}}$$
**关键**：要把"谱实"翻译成 $\Re\rho=\frac12$，必须先把谱参数**识别为 $\gamma$**：
$$\text{Re spectrum}\ + \ (\text{spectrum}=\{\gamma_n\})\ \Longrightarrow\ \rho=\tfrac12+i\gamma_n$$
**而这正是 Hilbert–Pólya 的设定** ⟹ 命中 **S 级 N0**（循环）✗

## 4. 硬信息三：竖条型结论只给"无零点区"强度
quadratic numerical range 可给出**不含谱的竖条** ✓ ——几何正确（竖条），但**方向相反**：
它排除一条竖条，等价于**零自由区**，不是把谱钉在一条线上。
$$\boxed{\text{⟹ 该家族最强形态 ≈ 经典无零点区强度，不是 RH 强度}}$$
**独立印证**：这与本项目早先（⑰关对应表）的结论一致——
$$\text{已知部分结果同型：}\ \lambda_1\ge 975/4096\ \longleftrightarrow\ \beta\ge1-c/\log q$$
即两侧都只到"无零点区/半平面"强度；**"线钉住"强度 = RH 强度，无文献来源** ✓

## 5. 验收判定

| 条件 | 结果 |
|---|---|
| 存在非自伴理论族 | ✓ 存在（①②③④⑤） |
| 正性能约束谱位置 | ✓ 但仅半平面/扇形/**实轴**/竖条空集 |
| 能给出**竖直线**（Re=c）作为输出几何 | **✗** 无（除非谱已被识别为 γ ⟹ HP） |
| 不退化/不循环 | **✗** §3、§4 |
| 可作为 RH 路径 | **✗** |

$$\boxed{\text{⟹ L1 = NO-GO（作为 RH 路径）}}$$

## 6. 为什么这不是"强行进入 L2"
```
L1 的合法输出形式是【实谱（Im=0）】，其转译必须经过"谱参数 = γ" ⟹ S 级 N0 命中
L1 的竖条形态只给零自由区强度 ⟹ 与已知部分结果同型
⟹ 该方向无剩余自由度（A 级结构性关闭）；正确产出就是 NO-GO，不是造模型 ✓
```

## 7. 诚实边界
```
· 本审计为【文献级】，依据为检索到的摘要/讲义片段（未逐篇通读全文）⟹ 标注为"文献级"
· "不存在这样的机制"仍为【未找到】，非不存在定理（宪法纪律）
· 覆盖范围：classical 非自伴谱理论五族；非标准/新近专题可能有未覆盖者
· 未写代码；未做数值；RH 本身未动
```

## 8. 结论与状态更新
```
L1 : NO-GO（非自伴谱刚性作为 RH 路径：输出几何与目标几何不匹配，转译必过 HP）
L2 : 保持开放（⑯–⑲：char 0 载体存在，需空间+流；ζ 在散射侧）
L3 : 保持开放（Q3：独立全局 √-尺度正性，对角尺度 X）
⟹ 活路表收缩为 L2 / L3 两项；且两者都需【先过宪法 A–H】再谈构造
```
