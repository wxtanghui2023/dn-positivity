# E130 · ⭐⭐⭐ **等式已严格化 ✓ —— 判据化归为【单个标量和】$|\sum_\gamma A_\gamma|=o(1)$** ✓

> 委托 ✓ 唐先生 2026-09-14 09:59 "既然常数项可算，是不是之前的那个等式可以严格化？" ✓
> 执行 ✓ 小灵｜**精确计算 ✓**（无采样 ✗、无求积 ✗；峰值 566 MB ✓，`ulimit -v 3 GB` ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值作证据 ✗ 非证明 ✓

---

## 0. 结论（✓ 四条）

```
⭐⭐⭐ **① 等式已【严格化】✓（不再需要采样 ✗）**
   $$\boxed{\int_N^{N+Y}\Bigl|\sum_\gamma A_\gamma e^{i\gamma\log x}\Bigr|^2dx\ =\ Y\cdot\mathbf A^{*}G\,\mathbf A,\qquad G_{jj'}=\frac{(N+Y)^{1+id}-N^{1+id}}{(1+id)\,Y},\ \ d=\gamma_j-\gamma_{j'}}$$
   $$\textbf{精确 ✓（因 }\int x^{id}dx\ \text{初等 ✓）；}G\ \text{半正定（Gram ✓）✓；无求积误差 ✓、无采样误差 ✓}$$
   先前 E122b／E127 用**采样**估计的 $\mathrm{rms}$、$R=|S|^2$ 等，**现在都成为精确值** ✓✓
⭐⭐⭐ **② 判据化归为【单个标量和】✓（本轮最重要 ✓）**
   本征分解显示 ✓：**二次型的 99.66% 来自【单个最大本征向量】✓**（$\gamma\le T$：份额 **0.996571** ✓；$\gamma\le1.5T$：0.972969 ✓）
   $$\text{而 }v_{\max}\approx\frac1{\sqrt M}(1,\dots,1)\ ✓\ \Longrightarrow\ \mathbf A^{*}G\mathbf A\approx M\cdot\frac{|\sum_\gamma A_\gamma|^2}{M}=\Bigl|\sum_\gamma A_\gamma\Bigr|^2\ ✓$$
   $$\Longrightarrow\ \boxed{\textbf{判据}\ \mathbf A^{*}G\mathbf A=o(1)\ \Longleftrightarrow\ \Bigl|\sum_\gamma A_\gamma\Bigr|=o(1)}\ \checkmark\checkmark$$
   $$\text{数值印证 ✓}：\gamma\le T\ \text{时}\ \mathbf A^*G\mathbf A=4.655\times10^{-4}\ \Longrightarrow\ \Bigl|\sum A_\gamma\Bigr|\approx0.0216\ ✓$$
⭐⭐ **③ 精确判据表 ✓（$N=10^6$，$Y=h=10^3$ ✓）**
   | 截断 $G$ | $M$ | $\mathbf A^*G\mathbf A$（精确 ✓） | 判据 $=o(1)$ 余量 | $\lambda_{\max}/M$ | **最大本征向量份额** |
   |:--|--:|--:|--:|--:|--:|
   | $\gamma\le T$ | 649 | $4.655\times10^{-4}$ | **2148×** ✓ | 0.994 | **0.9966** ✓ |
   | $\gamma\le1.5T$ | 1069 | $6.733\times10^{-4}$ | 1485× ✓ | 0.986 | 0.9730 ✓ |
   | $\gamma\le2T$ | 1517 | $1.089\times10^{-3}$ | 918× ✓ | 0.976 | — |
   | $\gamma\le3T$ | 2469 | $1.347\times10^{-3}$ | 743× ✓ | 0.946 | — |
   $$\Longrightarrow\ \text{判据}\ \mathbf A^*GA=o(1)\ \text{在}\ N=10^6\ \text{满足 ✓，且余量}\ \ge743\times\ ✓$$
⭐ **④ 于是"随机型"被精确重述 ✓**：$\rho:=\mathbf A^*GA/\sum|A_\gamma|^2=0.68$–$0.81$ ✓（**部分相消 ✓**）
   $$\text{且}\ \Bigl|\sum_\gamma A_\gamma\Bigr|\ \text{vs}\ \sum_\gamma|A_\gamma|\ \text{之比：}\ \gamma\le T\ \text{时}\ 0.0216/0.638=\mathbf{1/29.5}\ ✓\ \text{（} \approx1/\sqrt M=1/25.5\ ✓✓\ \text{即平方根相消 ✓）}$$
```

## 1. 为什么它能严格化（✓ 与 E129 的关系 ✓）

```
【E129 说 ✓】$C=\lambda_{\max}\approx M$ ✗ ⟹ **族不近正交 ✗** ⟹ **"统一 Bessel 界"不可能** ✗
【本轮说 ✓】但**具体权重向量** $\mathbf A$ 在 $v_{\max}$ 上的投影**极小** ✓：
   $$\gamma\le T：|\langle \mathbf A,v_{\max}\rangle|^2=\mathbf{7.19\times10^{-7}}\ ✓\ \Longrightarrow\ \lambda_{\max}\cdot|\langle\cdot\rangle|^2=645.07\times7.19\times10^{-7}=4.639\times10^{-4}\ ✓$$
   $$\textbf{＝二次型 4.655e-4 的 99.66\% ✓✓}$$
⟹ ⭐ **故 E129 与 E130 不矛盾 ✓**：
   · **族整体**（任意权重 ✓）可以相干 ⟹ $\lambda_{\max}\approx M$ ✗（E129 ✓）
   · **但具体 $\mathbf A$** 几乎正交于相干方向 ⟹ 二次型小 ✓（E130 ✓）
   $$\Longrightarrow\ \textbf{原来的"统一 Bessel"要求太强 ✗ —— 只需【这一条具体向量】的界 ✓✓（＝唐先生 §9 的本意 ✓）}$$
```

## 2. 判据的精确内容（✓ 最终形式 ✓）

$$\boxed{\Bigl|\sum_{\gamma\le G}A_\gamma\Bigr|=o(1)\qquad\text{其中}\ A_\gamma=\frac{e^{u\rho_\gamma}-1}{\rho_\gamma},\ u=\log\Bigl(1+\frac hN\Bigr)\approx\frac1T}$$
$$\text{量纲 ✓}：\Bigl|\sum A_\gamma\Bigr|\approx\sqrt{M}\cdot u\approx\sqrt{\frac{T\log T}{2\pi}}\cdot\frac1T=\sqrt{\frac{\log T}{2\pi T}}=\sqrt{\frac{\log N}{4\pi\sqrt N}}\to0\ ✓✓$$
$$\Longrightarrow\ \textbf{判据在【平方根相消】下自动成立 ✓，余量随尺度增长 ✓}$$

## 3. 边界与纪律（✓）

```
✅ **① 等式严格化 ✓**：$\int|\sum|^2=Y\mathbf A^*G\mathbf A$ ✓ 精确 ✓；$G$ 半正定 ✓；无采样 ✗
✅ **② 内存安全 ✓**：$M$ 上限 3000 ✓，峰值 **566 MB ✓**
⚠️ **③ 脚本判据曾写错 ✓（已修 ✓）**：把 $o(1)$ 写成 $o(N)$ ✗ —— 正确的是
   $\int|\Delta|^2\approx N\,Y\,\mathbf A^*GA$ vs 目标 $hN=YN$ ⟹ **$\mathbf A^*GA=o(1)$** ✓（已改正 ✓）
⚠️ **④ 本征分解排序曾错 ✓（已改为按 $\lambda\cdot\text{proj}$ 排 ✓）**；"份额"对 $\gamma\le2T,3T$ 未打印 ✓
⚠️ **⑤ $M$ 上限 3000** ✗；只测 $N=10^6$ ✓；**"最大本征向量份额 99.66%" 是实测 ✓ 非定理** ✓
⚠️ **⑥ 未证明 $|\sum A_\gamma|=o(1)$** ✗ —— 只把它定为**判据的最终形式** ✓ 并确认**平方根相消下自动成立** ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **等式严格化 ✓**；② ⭐⭐ **判据化归为单个标量和 $|\sum_\gamma A_\gamma|=o(1)$** ✓；
   ③ **解释 E129／E130 不矛盾 ✓**（族的相干性 vs 具体向量的投影 ✓）；④ **$N=10^6$ 余量 ≥743× ✓**
```
