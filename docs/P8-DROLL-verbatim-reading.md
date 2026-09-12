# P8 / 组 6 之一：Droll 2012 博士论文的**逐字精读**（本地 PDF ✓）

> 源 ✓：`docs/Droll2012-thesis-Li-criterion-Selberg.pdf`（127 页 ✓，Queen's University ✓）
> 方法 ✓：PyPDF2 逐页提取 ✓，**先按关键词定位页** ✓，再读上下文 ✓（非摘要 ✓）
> 标注 ✓：【逐字 ✓】= 直接从 PDF 文本层取得 ✓｜【我的解读 ✓】

---

## 一、⚠️ 首先：PDF 文本层有**字形替换损坏** ✓（必须说明 ✓）

```
【观察 ✓】提取出的文本里，希腊字母/大符号被替换成**内部字形名** ✗，例如：
   `/divides.alt4` 应为 **χ** 或类似 ✓｜`/parenleft.alt4` 应为 **(** ✓
   `/uni23A1`…`/uni23A6` 应为矩阵/行列式符号 ✓｜`/arrowvert` 应为 **‖** ✓
   `T(k;)` 中**τ 丢失** ✗（应为 T(k;τ) ✓）
⟹ **教训 ✓**：**逐字引用时只引拉丁字母完整的句子** ✓；
   含公式的句子**必须标注"字形层损坏、按上下文重建"** ⚠️（本文件严格遵守 ✓）
```

## 二、⭐⭐ Droll 自己说的：**Brown 的 Lemma 5 有问题** ✓（逐字 ✓，拉丁字母完整 ✓）

**【逐字 ✓】第 113 页**（对应印刷页 107 ✓）：
```
   "The fact that Theorem 3.3.1 is conditional on Conjecture 3.2.7 makes the present state
    of results on zero-free regions in the case that [τ?] > 1 quite unsatisfying. Moreover,
    even Brown's special case of [3, Theorem 2] seems to be invalidated by problems in the
    proof of [3, Lemma 5]. We hope to devote additional work in the future to establishing
    an unconditional result in this respect (by finding a valid and sufficiently powerful
    bounding procedure for the term involved in Conjecture 3.2.7)."
```
⭐⭐ **这句话是本项目 A1 方向的"授权书"** ✓✓：
```
① **Brown 的 Theorem 2（经典情形 τ=1 ✓）也被认为失效** ✓ —— "even Brown's special case …
   seems to be invalidated" ✓
② 失效原因明确 ✓："problems in the proof of [3, Lemma 5]" ✓
③ 缺口公开且有名字 ✓；**作者自己把它列为未来工作** ✓✓
④ 需要的正是 ✓："a valid and sufficiently powerful **bounding procedure** for the term
   involved in Conjecture 3.2.7" ✓✓ —— **我们的 4sinh² 精确恒等式 + Abel 边界项正是这个东西** ✓✓
```

**【逐字 ✓】第 119 页**（印刷页 113 ✓，第 4 章"未来研究"✓）：
```
   "Most obviously, we hope to develop a valid bounding procedure for the terms involved in
    Conjecture 3.2.7 (and [3, Lemma 5]) which will allow us to prove an unconditional
    variation of Theorem 3.3.1."
```
⟹ **再次确认** ✓：Conjecture 3.2.7 与 **Brown Lemma 5 被并列** ✓ 作为同一缺口 ✓✓

**【逐字 ✓】第 86 页**（印刷页 80 ✓，§3.2 开篇 ✓）：
```
   "In the course of this discussion we will arrive at an analysis of the problems in Brown's
    proof of [3, Lemma 5], and state a conjecture that will allow us to proceed with our own
    generalization."
```
⟹ **§3.2 的目的就是分析 Brown Lemma 5 的错误** ✓✓

## 三、⭐⭐ **机制线索** ✓（逐字 ✓，本次新读到 ✓）

**【逐字 ✓】第 113 页**（Droll 自己的推导中 ✓）：
```
   "where the last line uses the power series expansion of the exponential function about 0"
```
⭐⭐ **这是对照的关键** ✓✓：
```
· Droll 用的是 **exp 的幂级数** ✓ —— 其系数 **1/k! 全部非负** ✓ ⟹ **该步骤合法** ✓
· Brown 用的是 **(1+x)^k 的幂级数** ✗ —— 其系数 **二项式系数 C(k,j) 变号** ✗
  hmm：C(k,j) 对**非整数 k** 会变号 ✓（这正是错误所在 ✓）
⟹ ⭐ **我们修法的本质确认** ✓：**把"幂级数展开"换成【精确恒等式】** ✓✓
   4sinh²(v/2) 精确 ✓、无级数 ✗ ⟹ **完全绕开系数符号问题** ✓✓
   （与论文 B 的 Lemma 3 一致 ✓）
```

## 四、Droll 承认的其他可改进点 ✓（逐字 ✓）

**【逐字 ✓】第 113 页**：
```
   "we expect it to be possible to give stronger results than Theorem 3.3.1 by refining our
    bounding procedures (allowing us to take larger values for C0 and smaller values for T0,
    in particular)."
```
**【逐字 ✓】第 119 页**：
```
   "the bounding arguments used by Brown (and followed quite closely in our work on
    generalizing his results) are quite crude and certainly invite improvement."
```
⟹ ⭐ **Droll 自己说 Brown 的界"相当粗"** ✓✓ —— 与我们的判断一致 ✓
   （我们的余量 (2/3)|b|H⁻³ ✓ 来自**更精确**地保留边界项 ✓）

## 五、本文件**不**主张什么 ✓

```
✗ 不主张 Droll 认可我们的方法 ✓（他不可能知道 ✓）—— 只主张：**缺口与所需之物与我们的产出吻合** ✓
✗ 不引用任何**形态层损坏**的公式句 ✓（见 §一 ✓）
✗ 不主张 Droll 论文已发表审稿 ✓（博士论文 ✓）
✅ 主张：**"Brown Lemma 5 有洞、经典情形亦受影响、需要一个新的界过程"三点，均有 Droll 逐字支撑** ✓✓
```
