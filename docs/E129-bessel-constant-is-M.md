# E129 · 🔴 **推翻 E128：Bessel 常数 $C\approx M$（不是 $O(1)$）—— 正交/近正交路线【死】** ✗

> 委托 ✓ 唐先生 2026-09-14 09:56 "继续 a, b" ✓（(a) 核大筛形式＋找零点族 Bessel 界；(b) 求 $C$ 下界／反例 ✓）
> 执行 ✓ 小灵｜**直接精确计算** ✓（Gram 本征值 ✓；**峰值 563 MB ✓**，`ulimit -v 3 GB` ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；⚠️ **本轮是【负面/更正】结果 ✓**

---

## 0. 结论（✓ 四条，含对 E128 的推翻 ✗）

```
🔴 **① E128 的核心主张【被推翻 ✓】**：$C=O(1)$ **不成立** ✗ —— **实测 $C\approx M$** ✗
   $$C:=\lambda_{\max}\Bigl(\frac1Y\int_N^{N+Y}e^{i(\gamma_j-\gamma_{j'})\log x}dx\Bigr)\quad\textbf{（就是 Bessel 界的最优常数 ✓）}$$
   | 频率集合 | $M$ | $\lambda_{\max}$ | 比值 $\lambda_{\max}/M$ |
   |:--|--:|--:|--:|
   | 真实零点 $\gamma\le T$ | 649 | **645.07** | **0.994** ✗ |
   | 真实零点 $\gamma\le1.5T$ | 1069 | 1054.34 | 0.986 ✗ |
   | 真实零点 $\gamma\le2T$ | 1517 | 1480.06 | 0.976 ✗ |
   | 真实零点 $\gamma\le3T$ | 2469 | 2336.18 | 0.946 ✗ |
   $$\Longrightarrow\ \boxed{C\approx M\ ✗\ \text{—— \textbf{族【根本不接近正交】✗}}}$$
⭐⭐⭐ **② 原因极干净 ✓（秩一 ✓）**：$\gamma\le T$ 时窗口内相位变化 $\le\gamma Y/N=\gamma/T\le1$ ✓
   $$\Longrightarrow\ \phi_\gamma=e^{i\gamma\log x}\approx1+i\gamma(\log x-\log N)\approx\textbf{常数}\ ✓\ \Longrightarrow\ \text{Gram}\approx\textbf{全 1 矩阵}\ ⟹\ \lambda_{\max}=M\ ✓$$
   $$\Longrightarrow\ \textbf{族几乎是【同一个函数】（秩一）✗ —— 故"近正交"路线从结构上不可能}\ ✗✓$$
⭐⭐ **③ (b) 的答案 ✓：$C$ 是【结构性】的，不是算术的 ✓**
   | 替代集合 | $M$ | $\lambda_{\max}$ | 比值 |
   |:--|--:|--:|--:|
   | **RIGID**（等间距 ✓） | 649 / 1500 / 2629 | 610.6 / 1411.4 / 2473.9 | **0.941** ✗ |
   | **RANDOM**（随机间距 ✓） | 649 / 1500 / 2629 | 612.2 / 1418.8 / 2465.9 | **0.938–0.946** ✗ |
   $$\textbf{真实 }0.99\ ✗\qquad\text{RIGID }0.94\ ✗\qquad\text{RANDOM }0.94\ ✗\ \Longrightarrow\ \textbf{三者同量级 ⟹ }C\approx M\ \text{是【结构的】✓ 非算术的 ✗}$$
   $$\Longrightarrow\ \textbf{故 }C=O(1)\ \text{不仅未证 ✗，而且【不可能】✗（相位变化}\le1\ \text{时必 }C\sim M\ ✓）$$
⭐⭐ **④ (a) 的答案 ✓：大筛形式【确认】✓**
   $$\text{我手写的形式 }C\approx L+M\ ✓\ \text{（}L=\tfrac YN=\tfrac1T\ ✓,\ M=\text{频率数}\ ✓）\ \Longrightarrow\ C\approx M\ ✓$$
   $$\textbf{与直接精确计算一致 ✓✓}（0.99M\ \text{vs}\ M\ ✓）\ \Longrightarrow\ \textbf{通用工具与精确值同阶 ✓，没有"通用工具不足"的缺口 ✗}$$
   $$\Longrightarrow\ \textbf{E128 §2 的"差距 ＝ 因子 }N(T)\text{"【不成立】✗ —— 因为精确值【就是】}M\ \text{量级 ✓}$$
```

## 1. 对 E128 的更正（✓ 逐条 ✓）

$$\textbf{E128 说 ✓}：\text{"通用工具给 }N(T)\ ✗\ \text{而实测 }1.2\ ✓\ ⟹\ \text{差距 }N(T)"}\ ✗\qquad\textbf{实际 ✓}：\text{精确 }C=0.99M\ ✓\ \text{＝ 通用工具的量级 ✓}$$
```
⚠️ **E128 混淆了两件事 ✗**：
   · **无权 Gram 的 $\lambda_{\max}$（＝ $C$ ✓）**：$\approx M$ ✗ —— **这是"族能否相干"的度量** ✓（答案：能 ✓ 因相位变化 $\le1$ ✓）
   · **A-加权和的大小（E122b 测的 ✓）**：$\approx\sqrt{\sum|A_\gamma|^2}$ ✓ —— **这是【具体权重向量】的性质 ✗，不是族的正交性 ✓**
   $$\Longrightarrow\ \textbf{E128 用后者去论证前者 ✗ —— 逻辑错误 ✓（本轮更正 ✓）}$$
```

## 2. 剩下什么（✓ 诚实 ✓）

```
⭐ **A-加权和确实小 ✓（E122b 实测 ✓，$R\ll1$ ✓）** —— 但其**来源不是**族的正交性 ✗（本轮证否 ✓）
   而是：【权重】$A_\gamma\approx u$（$\gamma\ll T$ ✓ 近似实常数 ✓）＋【无权和的平方根相消】✓
   $$\Bigl|\sum_{\gamma\le T}A_\gamma e^{i\gamma\log x}\Bigr|\approx u\Bigl|\sum_{\gamma\le T}e^{i\gamma\log x}\Bigr|\approx u\sqrt M\ ✓\qquad\sqrt{\sum|A_\gamma|^2}\approx u\sqrt M\ ✓\ \text{（一致 ✓）}$$
⟹ ⭐ **故真正的输入是【无权零点和的平方根相消】✗**：$\sum_{\gamma\le G}e^{i\gamma\log x}=O(\sqrt G)\ √$ hmm——
   而由**显式公式**，此类零点 X 素数侧 ✓ —— **即回到了显式公式／素数分布** ✓
⟹ ⚠️ **故本线【未获得新东西】✗** —— 但它**排除了一条错误路线（Bessel/近正交 ✓）**，并把内容**归位**到零点和的相消 ✓
```

## 3. 边界与纪律（✓）

```
🔴 **本轮为【负面/更正】✓**：E128 的中心主张被推翻 ✓；Bessel／近正交路线【死】✗
✅ **内存安全 ✓**：矩阵 $O(M^2)$ ✓，$M$ 上限 3000 ✓，峰值 **563 MB ✓**（`ulimit -v 3 GB` ✓）
⚠️ **① $M$ 上限 3000** ✗（全 2e6 零点矩阵不可行 ✓：$4\times10^{12}$ 项 ✗）；② 只测 $N=10^6$ 一个尺度 ✓
⚠️ **③ $\lambda_{\min}\approx-1\text{e-}10$ ✓**（数值零 ✓，与 PSD 一致 ✓）
⚠️ **④ RIGID／RANDOM 代理【未匹配真实零点密度分布** ✗（等间距／指数间距 ✓）—— 但三者同量级已足够说明结构性 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **推翻 $C=O(1)$** ✗；② **秩一机制解释 ✓**；③ **(a) 大筛形式与精确值一致 ✓**；
   ④ **(b) $C$ 是结构性的（RIGID／RANDOM／真实三者同阶 ✓）**；⑤ **更正 E128 的逻辑错误 ✓**
```
