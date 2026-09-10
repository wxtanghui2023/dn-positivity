# ⚠️ 本文两处错误已撤回（见 FPCA2-generator-complexity-audit.md）

1. 输出信息量：应为 (x/log x)·log log x，不是 x/log x
2. “排除一切有限状态+有限规则机制”：无效（描述长度 ≠ 输出信息量）

P-Info 重定义为三量分离（I_state / I_rule / I_out）。

---

# FPCA：Future-Position Constraint Audit（纯纸面，无程序）

**日期**：2026-09-10 ｜ 唐先生指定七步 ｜ 结论：三个出口中①②被结构化封死，残余只剩分析通道

---

## 步 1：信息预算（定量封口 ①：sieve/CRT 的信息增益远远不够）

设状态 $X_N$ 描述长度为 $\ell(N)$ 比特；它至多能把"未来区间 $[x,2x]$ 的素数配置"
（共 $\pi(2x)-\pi(x)\sim x/\log x$ 个位置，配置数 $2^{\sim x/\log x}$）区分为
$$2^{\ell(N)}\ \text{个等价类}.$$

**局部（sieve/CRT）数据能给出多少约束？** 经典 Mertens 估计：
$$\prod_{p\le y}\Big(1-\frac1p\Big)\sim\frac{e^{-\gamma}}{\log y},\qquad y=\sqrt x .$$
即 sieve 把候选数从 $x$ 压缩到 $\sim x\cdot\frac{e^{-\gamma}}{\log\sqrt x}\sim\frac{2e^{-\gamma}x}{\log x}$。
$$\boxed{\text{压缩所需的信息量} = \log\frac{x}{x/\log x}\approx\log\log x\ \text{比特}}$$

$$\boxed{\text{而配置本身携带} \sim x/\log x\ \text{比特}}$$

$$\Longrightarrow\ \text{局部/CRT 数据的信息预算} = O(\log\log x)\ \ll\ x/\log x .$$

**⟹ 出口 ①（sieve/CRT）被【定量】封死**：不是"不好用"，而是信息量差一个 $x/\log x$ 量级。
这同时说明：任何真能约束具体位置的机制，必须携带 $\Omega(x/\log x)$ 级别的信息——
这已排除一切"有限局部规则 + 有限状态"的机制。

---

## 步 2：出口 ②（Euclid 型自生成）——形式事实，不是位置约束

$E_N=p_1\cdots p_k+1$ 给出 $\exists q\mid E_N,\ q\notin\{p_1,\dots,p_k\}$。
这个事实的证明只用：**有限积 + 单位 + 整除性** —— 在任何满足这些公理的半环中同样成立。
$$\boxed{\text{⟹ 它是【形式事实】⟹ 零模型可复现 ⟹ Arithmetic Null Separation 失败}}$$
且它只给**存在性**，不给位置：
$$\boxed{\text{new-prime existence}\ \neq\ \text{prime-position constraint}}$$
（$E_N$ 的最小素因子在已知结果下不可预测 ⟹ 同样不产生位置约束。）

## 步 3：出口 ②′（把分布定理当输入）——循环

若机制输出"$m$ 必须是素数/合数"靠引用 PNT/Dirichlet 等定理，则
$$\text{引用的定理}\supseteq\text{待证目标的一部分}\ \text{或}\ \text{本身就蕴含所需信息}\ \Longrightarrow\ \text{循环}$$
（已知例外：Bertrand 型"区间内存在素数"仍只是存在性，不是位置。）

## 步 4–6：排除清单（与既有门槛一致）
```
sieve/CRT         ⟹ 步1 定量封死
Euclid/Mullin     ⟹ 步2 形式事实 + 仅存在性
显式公式/零集重编 ⟹ 既有等价性判据（不变量能映射到 {γ} ⟹ 换皮）
```

## 步 7：残余是什么？（本轮最重要结论）

把所有机制类过滤掉之后，剩下的唯一通道是**分析通道**：
$$\boxed{\text{唯一能携带 } \Omega(x/\log x) \text{ 位未来配置信息的对象，是素数分布的解析数据}}$$
（计数函数的解析延拓 / 零点集 / 显式公式——三者等价。）

**故 FPCA 的结论不是"找到一个新机制"，而是：**
$$\boxed{\text{机制层的搜索空间【已穷尽】：第 7 步在"机制"层面无第四出口。}}$$

⟹ 剩余工作**必须**是分析通道内的**定理级**工作，而不是另造一个不变量/算子/曲率。
⟹ 并且回到本项目早先那个尚未回答的核心问题（现在有了信息论背书）：

$$\boxed{\text{是否存在一个【压缩、位置决定、但不与零点集等价】的状态？}}$$

---

## 新增标准前置条件（写死）

$$\boxed{\textbf{P-Info：任何候选必须申报其"信息预算"——它能钉住未来配置的多少比特？并给出与 sieve 的 }\log\log x\textbf{ 的比较。}}$$

不申报 ⟹ 不予审查。这条会自动淘汰一切"有限状态 + 有限规则"的提案。

## 登记册
```
出口① sieve/CRT        : 定量封死（信息差 x/log x 量级）
出口② Euclid 型        : 封死（形式事实 + 仅存在性）
出口②′ 分布定理当输入   : 封死（循环）
出口③ 零集/显式公式     : 既有等价性判据（换皮则死）
机制层第四出口          : 【本轮判定：无】
残余                    : 分析通道内的【定理级】工作
```

**未写程序。** 下一步若继续，只应针对"分析通道内是否存在非零点等价的压缩态"做纸面构造。
