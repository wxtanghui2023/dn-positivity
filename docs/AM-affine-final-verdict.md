# A–M affine closure / prime-label symmetry：终审（定理式边界）

**日期**：2026-09-10 ｜ 唐先生给出证明，助手核验通过 ｜ 判决：关闭（定理式，非预期）

---

## 0. 对象与关系

$M_p(x)=px$，$A_m(x)=x+m$，$A_1(x)=x+1$，$A_p=A_1^{\,p}$。

$$\boxed{\;M_pA_1=A_1^{\,p}M_p\;}\tag{R}$$

（两边均为 $x\mapsto px+p$。）

## 1. 定理

设 $\phi$ 为满足下式的 prime-label 自同构：
$$\phi(M_p)=M_{\sigma(p)}\ (\sigma\in\operatorname{Sym}(\mathbb P)),\qquad \phi(A_1)=A_1 .$$
则
$$\boxed{\;\sigma(p)=p\quad\forall p\le N\;\Longrightarrow\;\boxed{G_N=\{1\}\quad\forall N}\;}$$

### 证明（唐先生）
对 (R) 施加 $\phi$：$\;M_{\sigma(p)}A_1=A_1^{\,p}M_{\sigma(p)}$ … (1)
而 $M_{\sigma(p)}$ 自身满足 (R)：$\;M_{\sigma(p)}A_1=A_1^{\,\sigma(p)}M_{\sigma(p)}$ … (2)
比较 (1)(2) 并右消去 $M_{\sigma(p)}$：$\;A_1^{\,p}=A_1^{\,\sigma(p)}$
由 $A_1^{\,r}(x)=x+r$ 得 $p=\sigma(p)$。∎

### 核验补充（三处严谨性前提，复核必看）
```
① (R) 对一切 n≥1 成立，故步骤 (2) 用于指标 σ(p) 合法。
② 右消去需要 M_{σ(p)} 单射 —— 即"乘 σ(p)"在 ℤ 上单射 ✓。缺此条则在一般半群中消去不成立。
③ 范围：φ 形如"置换 prime 生成元 + 固定 A_1"。
   一般仿射半群自同构不在覆盖内；但若允许移动 A_1，对象即不再是
   "素数位置压缩态"，而退化为抽象半群自同构分类 ⟹ 不能用于逃逸。
```

## 2. 判据表（终审）

| 判据 | 结果 |
|---|---|
| C1：破坏 $\operatorname{Sym}(\mathbb P)$ | 通过，且**精确到平凡群** |
| 是否需要 $A_m,\ m\to\infty$ | **不需要** |
| 是否需要 $A_1,\dots,A_K$ | **不需要，只需 $A_1$** |
| C2：产生新的 prime-order arithmetic rigidity | 否 |
| C3：随尺度产生新约束 | 否 |
| Arithmetic Null Separation | **失败** |
| 是否值得编程 | **否** |

⟹「$m\to\infty$ 分界」的答案：**不需要。逃生口关闭。**

## 3. 概念收获（本轮最重要的正面结论）

$$\boxed{\text{打破 }\operatorname{Sym}(\mathbb P)\;\not\Longrightarrow\;\text{素数位置被决定}}$$

破坏对称性的力量**完全来自后继结构** $x\mapsto x+1$（阿基米德序），
属"自由算术"⟹ 零模型可复现 ⟹ 不构成 Null Separation。
与元结论一致：**自由的算术 = 零模型能复现的部分。**

## 4. 下一轮硬前置条件（新增）

$$\boxed{\textbf{P1″：内部状态必须对某些【具体】素数位置产生约束，而不仅仅是消除抽象 prime label 的置换自由度。}}$$

## 5. 归档
```
对象：A–M affine closure / prime-label symmetry
状态：【关闭·定理式】
引用：docs/affine-word-death.md、docs/affine-crt-death.md（前置两次封档）
     + 本篇（自同构群终审）
提交：见 git log（本轮）
```

## 6. 登记册更新
```
rad/product curvature        : 关闭（C2-a 证书）
K₂ 非交换矩阵曲率             : 关闭（T4）
分配律/结合律 holonomy        : 关闭（钳形定理）
进位层 holonomy               : 关闭（coboundary / 历史硬编码 / CRT 独立）
A–M affine closure 自同构群   : 关闭·定理式（G_N={1}，只需 A_1）
新增前置条件                  : P1″（约束具体位置 ≠ 打破标签对称）
```
