# E128 · ⭐⭐⭐ **(i) 可证形式 ＝ Bessel 型二次型界（$C=O(1)$）＋ (ii) 三尺度实测稳定** ✓

> 委托 ✓ 唐先生 2026-09-14 09:52 "i, ii" ✓
> 执行 ✓ 小灵｜**内存安全 ✓**（分块 200k ＋ `ulimit -v 2 GB` ✓，峰值 **171 MB** ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值作证据 ✗ 非证明 ✓

---

## 0. 结论（✓ 四条）

```
⭐⭐⭐ **① (i)【可证形式已写出 ✓】—— 一条 Bessel 型二次型界**
   $$\boxed{\Bigl\|\sum_\gamma A_\gamma\phi_\gamma\Bigr\|^2_{L^2[N,N+Y]}\ \le\ C\sum_\gamma|A_\gamma|^2\|\phi_\gamma\|^2,\qquad \phi_\gamma(x)=e^{i\gamma\log x},\quad \textbf{需 }C=O(1)}$$
   $$\Longrightarrow\ \textbf{若成立 ✓}：\int_N^{N+Y}\Delta^2dx\ \le\ C\cdot N Y\sum|A_\gamma|^2=C\,N\cdot T\cdot\frac{\log T}{2\pi T}\approx\frac{C\,N\log T}{2\pi}=o(hN)\ \checkmark$$
   $$\Longrightarrow\ \boxed{\textbf{Bessel}(C=O(1))\ \Longrightarrow\ C_3\ \Longrightarrow\ \text{Legendre／Brocard}}\ ✓✓$$
⭐⭐⭐ **② (i)【通用工具给不出 $C=O(1)$ ✗ —— 差距量化 ✓】**
   $$\text{大筛（频率数 }M=\text{零点数 }N(T)\approx\tfrac{T\log T}{2\pi}\text{ ✓，对偶区间长 }L=\tfrac YN=\tfrac1T\ ✓）：C\approx L+M\approx\mathbf{N(T)\approx\frac{T\log T}{2\pi}}\ ✗$$
   $$\text{实测 ✓}：C\approx1.2\ ✓✓\ \Longrightarrow\ \textbf{差距 ＝ 一个因子 }N(T)\approx\frac{T\log T}{2\pi}\ ✗$$
   $$\Longrightarrow\ \textbf{故所需的算术内容【恰好就是】"这个族接近正交"}\ ✓\ \text{（通用不等式无法给出 ✓）}$$
⭐⭐ **③ (ii) 三尺度实测：随机律【尺度稳定】✓**
   $$\text{三尺度 rms}|S|\ \text{与}\ \sqrt{\sum|A_\gamma|^2}\ \text{之比}：0.911,\ 0.921,\ 0.996\ ✓✓\ \Longrightarrow\ \textbf{随机律稳定}\ ✓$$
   $$\text{要求比值 }R=|S|^2：1.332\times10^{-2}\to5.832\times10^{-3}\to2.722\times10^{-3}\ ✓\ \Longrightarrow\ \textbf{单调降 ⟹ 余量随尺度增长}\ ✓✓$$
   $$\text{余量}：75\times\to171\times\to367\times\ ✓\qquad\max/\mathrm{rms}\ \text{恒}\approx2.0\ ✓\ \text{（轻尾稳定 ✓）}$$
⭐ **④ 与项目既有发现的连接 ✓**：$C\approx1$ 的机制 ＝ 零点间距的**涨落（gap noise ✓）破坏相干** ✓
   —— 与 **E74** 实测的"二阶差分被间隙噪声支配、符号混合"✓ **同一现象** ✓（**杀死 vdC 的原因，在这里反而是使 $C\approx1$ 的原因** ✓✓）
```

## 1. (ii) 三尺度表（✓ 可复跑 ✓）

| $N$ | $T=\sqrt N$ | $\mathrm{rms}\lvert S\rvert$ | $\sqrt{\sum\lvert A\rvert^2}$ | 比 | $\max/\mathrm{rms}$ | $R=\lvert S\rvert^2$ | $\frac{\log T}{2\pi T}$ |
|--:|--:|--:|--:|--:|--:|--:|--:|
| $10^4$ | 100.0 | $1.154\text{e-}1$ | $1.267\text{e-}1$ | **0.911** ✓ | 1.97 | $1.332\text{e-}2$ | $7.33\text{e-}3$ |
| $10^5$ | 316.2 | $7.637\text{e-}2$ | $8.290\text{e-}2$ | **0.921** ✓ | 2.10 | $5.832\text{e-}3$ | $2.90\text{e-}3$ |
| $10^6$ | 1000.0 | $5.217\text{e-}2$ | $5.238\text{e-}2$ | **0.996** ✓ | 1.98 | $2.722\text{e-}3$ | $1.10\text{e-}3$ |

$$\textbf{关键 ✓}：R=|\cdot|^2\ \text{【就是】要求比}\ \int|\Delta|^2/(hN)\ ✓\ \text{（因窗口与短区间皆}=\sqrt N\ ✓）\ \Longrightarrow\ R\ll1\ ⟹\ \text{余量 }1/R\ ✓$$
$$\text{拟合指数}\ d\log R/d\log T=-0.690\ ✓\ (\text{预测}-1\ ✗)\ \text{—— 偏慢因量表实测 }\sum|A|^2\approx2\cdot\frac{\log T}{2\pi T}\ ✓\ \text{（头＋尾各半 ✓）}$$

## 2. (i) 的等价形式与状态（✓）

$$\textbf{等价形式 ✓}：\mathcal C_{\rm off}:=\sum_{\gamma\ne\gamma'}A_\gamma\bar A_{\gamma'}K_Y(\gamma-\gamma')=o\Bigl(Y\sum_\gamma|A_\gamma|^2\Bigr)\ \checkmark\ \text{（非对角 }=o\text{(对角)} ✓）$$
```
⭐ **这【严格弱于】"support 到 $T$ 的完整 $R_2(\alpha)$"** ✓（唐先生 §9 ✓）：
   因为只需【二次型】层面的 $o(\cdot)$ 界 ✓，不需 $R_2(\alpha)$ 的【逐点】行为 ✓
⚠️ **但通用工具给不出** ✗：大筛 $C\approx N(T)$ ✗；Cauchy–Schwarz 给 $C=M$ ✗
⟹ **故所需的算术内容 ＝ "零点族 $\{e^{i\gamma\log x}\}$ 在窗口上接近正交" ✗** —— 这是**未证**的 ✓
```

## 3. 边界与纪律（✓）

```
✅ **内存安全 ✓**：分块 ＋ `ulimit -v 2 GB` ✓；峰值 **171 MB ✓**（旧版 9.6 GB ✗）
⚠️ **① $C\approx1.2$ 是【实测】✗ 非定理 ✓**；② 大筛形式 $C\approx L+M$ 是我按标准型**手写**的 ✗（须核精确常数 ✓）
⚠️ **③ 小 $T$ 时尾部被数据上限 $1.13\times10^6$ 截断** ✗（解释 R 的偏大与指数偏慢 ✓）；只测 3 个尺度 ✓
⚠️ **④ 未声称 Bessel 界成立** ✗ —— 只写出【它 ⟹ $C_3$】的蕴含 ✓，并确认通用工具不足 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① ⭐ **可证形式（Bessel，$C=O(1)$）已写出 ＋ 蕴含链 ✓**；② **通用工具差距量化（$N(T)$ 倍 ✗，实测 $1.2$ ✓）**；
   ③ **三尺度随机律稳定 ＋ 余量增长 ✓**；④ **与 E74 gap-noise 的机制连接 ✓**
```
