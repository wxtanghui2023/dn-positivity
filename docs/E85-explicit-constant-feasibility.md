# E85 · **显式化可行性判定** ⚠️ —— **$T=1.13\times10^6$ 处不可能闭合（所需上界是假的 ✗）；但 $T_0\approx1.5\times10^7$ 处可能有救** ✓

> 委托 ✓ 唐先生（20:07 选 (a) ＋ 限定：不得用未显式的 $O$ 直接算 $T_0$ ✓）｜执行 ✓ 小灵
> 纪律 ✓ 未用 RH ✓（Goldston 的 $a$ 仅在**诊断**中用 ✗，不进证明链 ✓）；未跑 Lean ✓

---

## 0. 结论（✓ 三条 ✓）

```
⛔ **① $T=1.13\times10^6$ 处【不可能】闭合** ✗ —— 不是"常数不够"✗，而是**所需上界本身是假的** ✗：
   允许 $\delta\le18.9\%$ ✓，而**真值** $\delta_{\rm true}=53.5\%$ ✗ ⟹ 任何显式化都救不了 ✓
⚠️ **② 但阈值 $T_0$ 不大** ✓：$\delta_{\rm allowed}\propto(\log T)^2$ ✓ ⟹ $T_0\approx\mathbf{1.5\times10^7}$ ✓
   （$\log T\approx16.5$ ✓）⟹ **远低于已验高度 $3.0\times10^{12}$** ✓ ⟹ **路线在原理上可用** ✓
⚠️ **③ 但②依赖一条很紧的无条件显式常数** ✗：需 $C\le0.034$ ✓（真值对应 $C_{\rm true}\approx0.029$ ✓ —— **刚够** ⚠️）
   ⟹ **E85 的实质是"显式常数工程"，而且窗口很窄** ⚠️
```

## 1. 文献现状（✓ 照您的信息 ✓）

$$M(T)=\int_0^T|\mathcal E|^2=\frac{T}{2\pi^2}\log\log T+O\!\bigl(T\sqrt{\log\log T}\bigr)\qquad(\textbf{Selberg 1946 ✓ 无条件 ✓})$$

```
✓ **无条件 ✓**（不需 RH ✓）；但 ⚠️ **$O$-常数在文献中【未显式】** ✗ ⟹ **不能据此直接算 $T_0$** ✗（照您限定 ✓）
✓ Goldston 的二阶项（$aT/\pi^2$ ✓）是 **RH 下**结果 ✓ ⟹ **不进证明链** ✗，仅作**真值诊断** ✓
```

## 2. 允许的 $\delta$（✓ 由账本反解 ✓，$T=1.13\times10^6$）

$$\text{中间带 }974500\sqrt{1+\delta}\;\le\;0.8N-\underbrace{N(0.3015T)}_{\text{deep}=538184}=1.06266\times10^6\;\Longrightarrow\;\boxed{\delta\le18.9\%}$$

## 3. 与真值比较（✓ 决定性 ✓）

$$\delta_{\rm true}=\frac{2a}{\log\log T}\qquad(a\approx0.7,\ \log\log T=2.63)\;\Longrightarrow\;\delta_{\rm true}=\mathbf{53.5\%}$$

$$\boxed{53.5\%>18.9\%\;\Longrightarrow\;\textbf{所需形状的上界【为假】}\;\Longrightarrow\;\textbf{该尺度上此路线封闭}}\ ✗$$

```
⭐ **重要 ✓**：这不是"常数优化不够" ✗ —— 而是**真实二阶项已超出账本允许** ✓
   ⟹ 除非**改变账本**（例如深快区不再用平凡界 ✗ —— 但那正是 E75–E79 已封的路 ✓），否则 $1.13\times10^6$ 处无解 ✓
```

## 4. ⭐ 阈值 $T_0$（✓ 粗略量级 ✓）

```
【关键 ✓】$\delta_{\rm allowed}(T)$ 随 $T$ **增长** ✓：
   中间带系数固定 ✓，而 $N\propto\sqrt n(\log n)/2$ ✓，深快比 $\to0.3015$ ✓
   ⟹ $\delta_{\rm allowed}\asymp\bigl(\tfrac{0.5\,(\\log n/2-2.838)}{2\pi A}\bigr)^2-1\ \propto\ (\log T)^2$ ✓
   而 $\delta_{\rm true}\asymp2a/\log\log T$ ✓ ⟹ **两者必然相交** ✓✓
【交点 ✓】$\delta_{\rm true}=\delta_{\rm allowed}$ ⟹
   $$T_0\approx1.5\times10^7\qquad(\log T\approx16.5,\ \log\log T\approx2.80,\ \delta\approx0.50\sim0.60)\ \checkmark$$
【对比 ✓】$T_0\approx1.5\times10^7\;\ll\;$ **已验高度 $3.0\times10^{12}$** ✓✓ ⟹ **若显式常数达标，路线可用** ✓
【但 ⚠️】**换算成无条件显式常数** ✓：$O(T\sqrt{\log\log T})$ 的常数 $C$ 需满足
   $$\delta=17.3C\le0.595\;\Longrightarrow\;\boxed{C\le0.034}\quad(\text{真值对应 }C_{\rm true}\approx0.029\ \text{—— 余量仅 15\%})$$
```

## 5. 判定与状态（✓）

| | 内容 |
|:--|:--|
| **$T=1.13\times10^6$** | ⛔ **不可能闭合** ✗（所需上界为假 ✓） |
| **$T\gtrsim1.5\times10^7$** | ⚠️ **可能有救** ✓ —— 但需无条件显式常数 $C\le0.034$ ✗ |
| **渐近（$T\to\infty$）** | ✅ **闭合** ✓（E84b ✓ 且对任何 $C$ 稳健 ✓） |
| **E85 性质** | **显式常数工程** ✓（**非**机制问题 ✓ —— 与 E69–E82 有本质区别 ✓），**窗口很窄** ⚠️ |

```
⚠️ **诚实标注 ✓**：
   · $T_0$ 为**量级估计**（$\log T\approx16$ ✓ 附近 ✓），非精确值 ✗
   · $\delta_{\rm true}$ 与 $C_{\rm true}$ 是 **RH 下**的真值诊断 ✗ ⟹ **无条件**下可能更差 ✗
   · **未宣布 T1 已证** ✗；**未宣布可达尺度闭合** ✗
✅ **净结果 ✓**：由 E84b 的渐近闭合 ＋ E85 的可行性判定，得到
   $$\boxed{\textbf{T1}\Leftarrow\text{深快区 }0.3015N+\text{一条显式无条件的 }L(T)=O(\log\log T)\text{ 型局部二阶矩（常数 }C\le0.034)}$$
```

## 6. 纪律（✓）

```
✓ 未用 RH ✓（Goldston 仅诊断 ✗）；未用 pair correlation／GUE ✓；**未跑 Lean** ✓
✓ **未据未显式的 $O$ 直接算 $T_0$** ✗（照您限定 ✓）—— 本轮的 $T_0$ 是**由账本反解**得到 ✓
✓ R7 ✓：结论由 $\delta$ 的两种计算驱动 ✓
```
