# E121 · ⭐⭐⭐ **重做：窗口自身会平均掉 $\gamma\gg T$ 项 ⟹ 有效范围回到 $\gamma\lesssim T$；您 §4 的缺口恢复** ✓

> 委托 ✓ 唐先生 22:54 "重做" ✓（在修正后的记账下重做 pair-correlation 的归一化与缺口 ✓）
> 执行 ✓ 小灵｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；⚠️ 全文标【推导】✗

---

## 0. 结论（✓ 四条，含对我自己 E120 的一处限定 ⚠️）

```
⚠️ **① 我的 E120 需加一条限定 ✓**：E120 的截断错误【对【点态值】成立 ✓】，**但对【窗口平均后的 $L^2$ 对象不一定成立** ✗
   $$\textbf{理由 ✓}：\text{窗口内单个零点的相位变化}\ \approx\gamma\cdot\frac YN=\frac\gamma T\ ✓$$
   $$\Longrightarrow\ \gamma\ll T：\text{变化}\lesssim1\ \text{（不被平均 ✗）}\qquad\qquad\gamma\gg T：\text{变化}\gg1\ \Longrightarrow\ \textbf{被窗口平均掉}\ ✓✓$$
   $$\Longrightarrow\ \boxed{\text{有效求和范围【回到】}\gamma\lesssim T\ ✓\ \text{（而 }\gamma\gg T\ \text{的尾部在窗口对象里被平均 ✓）}}$$
⭐⭐⭐ **② 重做后的绝对估计（相干界 ✓）**
   $$\int_N^{N+Y}\Bigl|\sum_\gamma A_\gamma e^{i\gamma\log x}\Bigr|^2dx\ \approx\ Y\Bigl(\sum_{\gamma\lesssim T}|A_\gamma|\Bigr)^2\approx Y\Bigl(\frac{\log T}{2\pi}\Bigr)^2\ ✓$$
   $$\int_N^{N+Y}\Delta^2dx\ \approx\ N\cdot Y\cdot\frac{\log^2T}{4\pi^2}=\frac{N^{3/2}\log^2T}{4\pi^2}\ ✗\qquad\text{要求}：o(hN)=o(N^{3/2})\ ✗$$
   $$\Longrightarrow\ \boxed{\textbf{需要一个【因子 }\frac{\log^2T}{4\pi^2}\ \text{的相消}\ ✗\ \text{—— 而相消只能来自零点对相关}\ ✓✓}}$$
⭐⭐ **③ 唐先生 §4 的缺口【恢复 ✓】，且现在有正确记账 ✓**
   $$\text{Montgomery 覆盖（归一化分离 }\le1\text{）}：|\gamma-\gamma'|\le\frac{2\pi}{\log T}\ ✓\qquad\text{需要}：|\gamma-\gamma'|\lesssim T\ ✗$$
   $$\Longrightarrow\ \boxed{\text{缺口因子 ＝ }T\cdot\frac{\log T}{2\pi}\ ✗\ \Longleftrightarrow\ \text{把 support 从 }T/\log T\ \text{推到 }T}\ ✓\ \text{（与您 §4 一致 ✓）}$$
⭐ **④ 于是【所需相消的量】已可写成具体数字 ✓**
   $$\text{（在 }x=10^6,\ T=10^3\text{）}\qquad \frac{\log^2T}{4\pi^2}=\frac{47.7}{39.5}\approx1.21\ ✗\ \text{（仅差 21\% ✓）}$$
   $$\text{（渐近）}\qquad \frac{\log^2T}{4\pi^2}\approx\frac{(\log N)^2}{16\pi^2}\to\infty\ ✗\ \Longrightarrow\ \textbf{渐近地【必须】有相消}\ ✓$$
```

## 1. 重做的三步（✓）

$$\textbf{步 1 ✓（有效范围）}：\sum_\gamma A_\gamma e^{i\gamma\log x}\ \text{在窗口上的平均}：\gamma\ll T\ \text{同相 ✓}，\gamma\gg T\ \text{自平均 ✓}\ \Longrightarrow\ \text{有效}\ \gamma\lesssim T\ ✓$$
$$\textbf{步 2 ✓（绝对界）}：\int_N^{N+Y}\Bigl|\sum_{\gamma\lesssim T}\Bigr|^2dx\le Y\Bigl(\sum_{\gamma\lesssim T}|A_\gamma|\Bigr)^2\approx Y\frac{\log^2T}{4\pi^2}\ ✓\ \text{（E120 已数值核 ✓：}\sum_{\gamma\le T}|A|=0.638\approx\log T/2\pi\ ✓）$$
$$\textbf{步 3 ✓（与要求比）}：\text{乘以 }\Delta\ \text{的 }x^{1/2}\ \text{因子（}\int|\Delta|^2\approx N\int|\sum|^2\ ✓）\ \Longrightarrow\ \frac{N^{3/2}\log^2T}{4\pi^2}\ \text{vs}\ N^{3/2}\ ✗\ \Longrightarrow\ \textbf{需相消}\ \frac{\log^2T}{4\pi^2}\ ✓$$

## 2. 相消从哪里来（✓ 这正是 pair correlation 进入处 ✓）

```
【相消只能在】$\gamma,\gamma'\lesssim T$、$|\gamma-\gamma'|\lesssim T$ 的【对角-近对角对】之间 ✓
   —— 因为：
   · 对角（$\gamma=\gamma'$）✓：$\sum|A_\gamma|^2Y\approx Y\frac{\log T}{2\pi T}\ll Y\frac{\log^2T}{4\pi^2}\ ✓$
     ⟹ **对角远小于绝对界** ⟹ **绝对界的绝大部分是【非对角】✗**
   · 非对角要相消到 $o(N^{3/2})$ ⟹ 需要零点之间【相位不相关】✓ —— **这正是 pair correlation 的内容 ✓**
⟹ ⭐ **故需要的相消 ＝ 需要 pair correlation 覆盖 $|\gamma-\gamma'|\lesssim T$、高度 $\lesssim T$** ✓✓
```

## 3. 与 Montgomery 的确切关系（✓ 归一化已重做 ✓）

$$\text{归一化变量 ✓}：\alpha_\gamma=\frac{\log\gamma}{2\pi}(\gamma-\gamma')\qquad\text{（}\log\gamma\ \text{而非 }\log T\ \text{✓ —— E120 的教训已用上 ✓）}$$
$$\text{在高度 }\gamma\lesssim T\ \text{内，需要覆盖 }\alpha\lesssim\frac{\log T}{2\pi}T\ ✗\qquad\text{Montgomery 无条件给 }\alpha\le1\ ✗$$
$$\Longrightarrow\ \textbf{缺的是【$\alpha$ 从 1 到 }\frac{T\log T}{2\pi}\text{（在高度 }T\text{ 处）】的 pair correlation}\ ✗$$
$$\text{（等价地说 ✓：}|\gamma-\gamma'|\ \text{从}\ \frac{2\pi}{\log T}\ \text{到}\ T\ ✓\ ——\ \text{即您 §4 的 }T/\log T\to T\ ✓✓）$$

## 4. 边界与纪律（✓）

```
⚠️ **① E120 的限定 ✓**：其"量级来自尾部 $\gamma\gg T$"对**点态**成立 ✓，对**窗口平均对象不成立** ✗（窗口自平均 ✓）
   ⟹ **故 E120 的结论须读作【点态】结论 ✓** —— 本文件补上此限定 ✓
⚠️ **② §1 的"窗口平均"是【机制论证】✗**（用 $\gamma Y/N$ 判据 ✓）；严格版本需核 $\sum_\gamma A_\gamma\sum_k(\cdots)$ 的振荡积分 ✗
⚠️ **③ 所需相消 $\log^2T/4\pi^2$ 是【绝对界／要求之比 ✓】，非"最优所需" ✗** —— 真实所需可能更小 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓；**无计算** ✓
⭐ **本轮净产出 ✓**：① 限定 E120 ✓；② **重做后的绝对估计与所需相消** ✓；③ **§4 缺口恢复且归一化正确 ✓**；
   ④ **所需相消的具体数值（$x=10^6$：1.21 倍 ✓；渐近 $\sim(\log N)^2/16\pi^2$ ✗）** ✓
```
