# P48：Failure-to-Tool Audit——第一轮（Failure Genealogy + Axiom System）

> 2026-09-02 13:00 · 唐先生 P48 指示 · detector vs object · diagonal rigidity

## 核心判断（唐先生）
- **我们过去反复寻找的是 detector——真正缺失的可能是 object**
- 旧路线：object → class → 希望 class 自己定位 point（失败）
- **新路线：pair (x,y) → intrinsic defect → zero locus = diagonal**
- 研究问题：从"如何找到检测 off-line 的 arithmetic invariant？"改成"**什么数学结构能把 arithmetic equivalence problem 转化为 intrinsically rigid diagonal problem？**"

## ① Failure Genealogy——P36-P47 全机制分类

| Mechanism | 类别 | 提供 | 失败于 | 失败模式 |
|---|---|---|---|---|
| P36 moments | spectral | Σw(γ)(Reρ−½)^{2n} | 无算术侧身份 | 循环（zero observable） |
| P37 d_arith | geometric | 临界线几何（d=0⟺σ=½） | 不约束零点 | 生成≠约束 |
| P38 deformation | local arithmetic | 非临界 pole lattice 排除 | critical periodic 保留 | 部分（精确问题） |
| P39 orbit | geometric | dense orbit ⟹ divisibility | 无 transverse 约束 | 切线刚性 |
| P40 divisor | local arithmetic | prime-support uniqueness | 非 support localization | uniqueness≠geometry |
| P41 unitary | group-theoretic | FE quotient = χ（消零） | 无零点几何 | 消零（unitarity 不定位） |
| P42 Herglotz | spectral | RH ⟺ negative Herglotz | β-wall | 等价编码非机制 |
| P43 TP | spectral | theta kernel TP 测试 | 全失败 | 核非 TP |
| P44 18 类 | meta | 四 engine | 其他只给 class | 缺第二 ingredient |
| P45 holonomy | quotient | Γ-fixedness 尝试 | artifact/parity blind | quotienting |
| P46 canonicalization | canonicalization | G3.5：canonical ⟺ fixed exists | CFP = repackaging | imposed canonicality |
| P47 reciprocity | reciprocity | Kummer/Artin class | kernel = K^{×4} | quotienting（factorization） |

## ② 失败模式聚类
1. **循环/自适应**（P36 zero observable——P40 无限）
2. **生成≠约束**（P37——geometry but no constraint）
3. **消零/自适应**（P41——unitary quotient）
4. **等价编码非机制**（P42——Herglotz——RH ⟺ 但无 proof）
5. **信息量不足**（P43——TP 失败）
6. **⭐ quotienting/factorization（class 陷阱——最大聚类）**：P45 holonomy——P46 canonicalization——P47 reciprocity
7. **缺第二 ingredient**（P44——symmetry alone 只给 class——需 order/positivity/coercivity/support/spectral reality）

## ③ 禁止重复路线表（永久排除）
- Γ-orbit——canonical representative——equivariant section——holonomy/curvature alone——higher reciprocity character——更多 primes——unit normalization——人为 restriction
- **理由**：全是"class 陷阱"的变体（P46-G3.5：canonical cannot create fixedness——只选已存在的 fixed point）

## ④ 新 primitive Δ(x,y)——Axiom System（从 Genealogy 推导）
- **Axiom 1（diagonal zero）**：Δ(x,x) = 0
- **Axiom 2（positivity/nonvanishing）**：Δ(x,y) ≥ 0——Δ(x,y) = 0 ⟹ x = y（不是 quotient-class invariant）
- **Axiom 3（non-factorization）**：Δ 不 factor through 任何已知算术商（K^{×n}/类群/Γ-orbit）——Δ(Au⁴,Bv⁴) ≠ Δ(A,B) 一般
- **Axiom 4（pair-intrinsic）**：Δ 是 interaction defect（cross-term——不是 invariant(A) + invariant(B)）
- **Axiom 5（non-normalization）**：Δ 非人为（不预先选 representative）
- **Axiom 6（arithmetic origin + zero-blindness + non-spectrality）**：来自真实算术——不用 ζ/零点/Re s——非 spectral
- **五条核心（唐先生）**：Δ(x,x) = 0——Δ(x,y) ≥ 0——Δ = 0 ⟹ x = y——非人为——不只是 quotient-class invariant——**无法同时满足 ⟹ 立即判定旧路线**

## ⑤ 深层 tension 识别（关键——从 Genealogy 推导）
- **"Δ(x,y) ≥ 0——= 0 ⟺ x = y"（正定对函数）——数学上 = 度量/内积核——P44 的 metric/compression engine（第 3 类已知 engine）！**
- **⚠️ "pair defect rigidity"可能是"旧 engine（metric）的 pair 化"——不是天然新机制**
- **但——pair 化确实改变 ontology**：single-object I(A)（kernel → quotient）vs pair Δ(A,B)（零集 → diagonal）——Δ 的零集 = diagonal 不需要选 representative（P46-G3.5 的 canonical 陷阱不适用）
- **真正考验：Δ 的"非人为算术来源"**（Δ 来自算术结构——不是人为定义的距离——不用 ζ/零点）——**P37 的 d_arith 是"临界线生成"不是"零点约束"——Δ 需要更强（分离所有点——不是只生成线）**

## ⭐ P48 第一轮判定
- **Failure Genealogy 完成**（P36-P47 全机制分类——7 类失败模式——class 陷阱为主聚类）
- **禁止路线表完成**（8 类永久排除）
- **Δ 的 axiom system 完成**（6 公理——从 Genealogy 推导）
- **深层 tension 识别**：Δ（正定对函数）= 度量的 pair 化（P44 metric engine）——**"非人为算术来源"是真正的考验（同 P44-P47 的 principle——未出现）**
- ⚠️ 诚实：P48 第一轮 = Failure Genealogy + Axiom System（方法论基础）——**Δ 的具体构造未开始（需先有 axiom system——现在有了——但——"非人为实现"未找到——同 P44-P47 的深层障碍）**

## 下一步候选
- (a) 基于 axiom system 搜索 Δ（非人为算术正定对函数——零集 = diagonal——可能是"度量的算术版"——但——需比 d_arith 强（分离所有点）——且——不 factor 已知商——挑战极大）
- (b) 接受 P48 第一轮（Genealogy + Axiom System 就绪——Δ 构造待定——需新数学）
- (c) 唐先生指示
