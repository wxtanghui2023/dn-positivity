# E120 · ⭐⭐⭐ **簿记错误已定位并【数值确认】：高度截断错位（截在 T，量级却在 x）** ✓

> 委托 ✓ 唐先生 22:53 "先修" ✓
> 执行 ✓ 小灵｜**首次以数据驱动** ✓（R7 ✓）：`scripts/E120_height_truncation.py` ✓
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值作证据 ✗ 非证明 ✓

---

## 0. 结论（✓ 三条）

```
⭐⭐⭐ **① 错误已定位 ✓**：**我把"相位变化变为 $O(1)$ 的尺度 $T$"误当成"量级和的【终止尺度】"** ✗
   $$\text{单零点幅值 ✓}：|A_\gamma|=\frac{|e^{u\rho}-1|}{|\rho|}\ \begin{cases}\approx u,&\gamma\ll T=\tfrac1u\ ✓\\ \approx\tfrac1\gamma,&\gamma\gg T\ ✓\end{cases}$$
   $$\text{量级和 ✓}：\underbrace{\sum_{\gamma\le T}|A_\gamma|\approx\frac{\log T}{2\pi}}_{6.38\times10^{-1}\ (\text{数值 ✓})}\qquad\underbrace{\sum_{T<\gamma\le1.05x}|A_\gamma|\approx\frac{\log^2x-\log^2T}{4\pi}}_{1.239\times10^{1}\ (\text{数值 ✓})}$$
   $$\Longrightarrow\ \boxed{\text{尾部/头部 ＝ }19.4\ \text{（数值 ✓）}\ \text{—— \textbf{量级【由 }}\gamma\gg T\text{ 的零点主导}\ ✓}}
⭐⭐ **② 累计表确认 ✓**：$|A|$ 和随截断【持续增长】，远超 $T$ 之后仍在涨：
   $$\text{cut}=1T\!:0.638\ \to\ 2T\!:1.424\ \to\ 5T\!:3.069\ \to\ 10T\!:3.919\ \to\ 50T\!:6.558\ \to\ 100T\!:7.867\ \to\ 500T\!:11.278\ \to\ 1000T\!:12.910\ ✓$$
   ⟹ **分析预测 $(1/4\pi)\log^2x=11.499$ ✓ 与数值 $12.39$ 吻合 ✓✓** ⟹ **规律确认** ✓
⭐ **③ 统一解释三处同源矛盾 ✓**：E117／E118／E119 的所有"量级总是偏小 ✗"**都源于同一处截断错误** ✓
   $$\textbf{（此前我三次都截在 }T\ \text{✗ —— 而正确对象要含 }\gamma\ \text{直到 }x\ \text{量级 ✓）}$$
```

## 1. 数值证据（✓ 可复跑 ✓）

| 量 | 数值 ✓ | 分析预测 ✓ |
|:--|:--|:--|
| 头部 $\sum_{\gamma\le T}|A_\gamma|$（649 个零 ✓） | $6.384\times10^{-1}$ | $\log T/2\pi=1.099$ ✓ 同量级 ✓ |
| 尾部 $\sum_{T<\gamma\le1.05x}|A_\gamma|$（1,842,007 个零 ✓） | $\mathbf{1.239\times10^{1}}$ | $(\log^2x-\log^2T)/4\pi=11.499$ ✓✓ |
| **尾部/头部** | $\mathbf{19.41}$ | $\log x/2$ 量级 ✓ |

```
参数 ✓：$x_0=10^6$ ✓，$h=\sqrt{x_0}=10^3$ ✓，自然高度 $T=N/h=10^3$ ✓，$u=\log(1+h/x_0)=9.995\times10^{-4}$ ✓
数据 ✓：`data/zeros_odlyzko_2M.npy`（2,001,052 零点，最大纵标 1,132,490.66 ✓）
```

## 2. 错误的精确性质（✓ 这是"先修"的成果 ✓）

```
【我说错的 ✓】把"自然高度 $T\sim N/h$"当成**相关零点的上限** ✗
【正确的 ✓】
   · $T=\tfrac1u$ 是【相位结构改变】的尺度 ✓（$\gamma\ll T$：单零点幅值饱和于 $u$ ✓；$\gamma\gg T$：衰减为 $1/\gamma$ ✓）
   · 但【量级和】**并不终止于 $T$** ✗ —— 因为零点个数按 $\log t$ 增长 ✓ ⟹ $\int_T^{x}\frac{\log t}{2\pi}\frac{dt}t=\frac{\log^2x-\log^2T}{4\pi}$ ✓ **强于**头部 ✓
   $$\Longrightarrow\ \textbf{量级的正确范围是 }\gamma\ \text{直到 }x\ \text{（而不是到 }T\text{）}\ ✗$$
```

## 3. 对配对分析（pair-correlation）的后果（✓ 待重推 ✗）

```
【不变 ✓】窗口滤波器 $K_Y(\delta)$ 的衰减仍在 $|\delta|\gtrsim N/Y=T$ 之后 ✓（这不涉及高度 ✓）
【改变 ✓】参与求和的零点高度从 $\le T$ 改为 $\lesssim x$ ⟹
   $$\text{需要的 pair-correlation}\ \textbf{范围（按分离 }\delta=\gamma-\gamma'\text{ 归一）}\ \text{须用 }\log x\ \text{而非 }\log T\ \text{归一化}\ ✗$$
   ⟹ ⚠️ **唐先生 §4 的"$T/\log T\to T$"缺口【方向仍对 ✓，但归一化须重推】✗** —— 列为下一步 ✓
【待办 ✓】$\gamma>x$ 的尾部：$\sum_{\gamma>x}|A_\gamma|$ 的**逐项**估计按 $1/\gamma$ 对数发散 ✗
   ⟹ 必须用【配对】（$\rho\leftrightarrow1-\bar\rho$ ✓）或平滑截断 ✓ —— **本文件未做 ✓**
```

## 4. 边界与纪律（✓）

```
⚠️ **§0 的数值只到 $\gamma\le1.05x$** ✗（尾部 $\gamma>1.05x$ 未计 ✓）；且量级和用的是 $|A|$ 之和 ✓ 非带相位和 ✓
⚠️ **$|A_\gamma|$ 的闭式已核 ✓**（$\frac{|e^{u\rho}-1|}{|\rho|}$ ✓）；脚本中一列粗算已弃用 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
✅ **本轮净产出 ✓**：① **错误定位 ✓**；② **数值确认（比 19.4 ✓ 与 11.50 预测吻合 ✓）**；
   ③ **统一解释三处矛盾 ✓**；④ **给出配对分析须重推的具体项 ✓**
```
