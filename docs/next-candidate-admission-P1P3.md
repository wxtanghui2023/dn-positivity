# 下一候选准入规范（P1′–P3′）与对 𝒫_X 提案的预筛

**日期**：2026-09-10 ｜ 前置：Integrability–Null Pincer 已固化（见 arithmetic-relation-holonomy-first-round.md）

---

## 0. 唐先生定的原始门槛（P1–P3）

```
P1 Prime injection   ：素数分布在哪里第一次进入？
P2 Irreducibility    ：为何不能被局部 CRT/组合/形式零模型复制？
P3 Propagation       ：如何跨尺度传播，而非只出现一次？
```
并明确禁止以"因为用了素数"作答；同时指出"素数分布"本身不足，
必须是 **prime distribution + 一个新的刚性关系**。

---

## 1. 结构性修正：P1「injection」是错误框架 → 改为 P1′「self-generation」

**理由**：素数集在 $(\mathbb Z,+,\times)$ 中**可局部定义**：
$$n\ \text{是素数}\iff \nexists\, d,\ 1<d<n,\ d\mid n .$$
⟹ 素数序列是**整除数据的导出对象**，不是新的算术输入。
∴ "把素数分布注入机制" = 把**待约束的目标**当作输入 ⟹ 自证（vacuous）。

$$\boxed{\text{P1′（Self-generation）：什么【强制】素数必须处于其实际位置？}}$$

这与本项目既有结论一致：*生成 ≠ 约束*；*检测 ≠ 排除*。

## 2. P2′／P3′（改写后）

```
P2′ Irreducibility：零模型必须保留全部【局部】统计
     （素数密度、间隙分布、CRT 局部数据），只改变【全局排列】。
     机制必须对这一改变有反应；若其刚性仅来自"排列被给定" ⟹ 平凡（死）。
P3′ Propagation：约束必须【尺度闭环】——X→cX 的更新由机制自身给出，
     而非外部重新读取素数表。
```

---

## 3. 对 𝒫_X 提案的预筛（纸面，未做计算）

$$\mathcal P_X=(p_1,\dots,p_{\pi(X)}),\qquad \mathcal R(\mathcal P_X)\longrightarrow \mathcal R(\mathcal P_{cX})$$

**预判**：若 $\mathcal R$ 是"素数表上的函数"、其跨尺度更新仅"重新读取新区间内素数"，则
$$\mathcal R(\mathcal P_{cX})-\mathcal R(\mathcal P_X)=\Phi\big(\#\{\text{新区间素数}\}\big)$$
即**势函数差（coboundary）** ⟹ 与进位计数版同型 ⟹ Integrability–Null Pincer 第一腿命中
⟹ 不变量/holonomy 恒为平凡。

**唯一逃逸条件**：
$$\boxed{\mathcal R\ \text{的更新律本身约束素数排列（给定 }\mathcal R\text{ 值 ⟹ 排列被部分确定）}}$$
而不是从排列读取 $\mathcal R$。

## 4. 可操作判据（一句话）

$$\boxed{\textbf{该机制是【约束】素数排列，还是仅仅【读取】它？}}$$

- **读** ⟹ 死（注入答案 / coboundary）
- **约束** ⟹ 进入 P2′ 零模型检验 ⟹ 再进 P3′ 尺度闭环 ⟹ 才允许写程序

## 5. 执行纪律（唐先生定）
```
先写出 P1′（谁强制素数位置）
→ 再证明逃离 Arithmetic Null Model（P2′）
→ 再给尺度闭环（P3′）
三者未齐 ⟹【不写程序】
```
