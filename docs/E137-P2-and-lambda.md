# E137 · ⭐ **$\psi\to\vartheta$ 审计 ＋ $\lambda=h/Y$ 扫描：两处皆非断点 ✗，但 $\lambda$ 带来一个结构性事实** ✓

> 委托 ✓ 唐先生 2026-09-14 11:00（先算 $P_2$ 的二次贡献与与 $F$ 的交叉项 ✓；并核 $\lambda=h/Y$ ✓）
> 执行 ✓ 小灵｜**按协议领号 ✓（工具第三次误给别名 E123 ✗，见 §4）**｜内存安全 ✓（峰值 51 MB ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 结论（✓ 三条）

```
⭐⭐ **① $P_2$ 在 $\lambda=1$（E130 口径）【恒为 0 ✓ —— 结构性结果 ✓】**
   $$\text{平方项 }p^2\in(N,N{+}Y{+}h]\ \text{要求}\ p\in(\sqrt N,\sqrt{N+Y+h}]\ ✓\qquad\textbf{该区间长度}\approx\frac{h}{2\sqrt N}=\frac{\lambda}{2}\ ✓$$
   $$\lambda=1\ \Longrightarrow\ \text{长度}=0.5<1\ ✓\ \Longrightarrow\ \textbf{区间内【无整数】✓ ⟹ 无素数平方 ✓ ⟹ }P_2\equiv0\ ✓✓$$
   $$\text{实测 ✓}：P_2\ \text{max}=0\ ✓\ \text{nonzero fraction}=0\ ✓\ \Longrightarrow\ \text{两个新项【皆为 0 ✓】}$$
   ⭐ **故 $\psi\to\vartheta$ 在 $\lambda=1$ 处【无贡献 ✓】—— 而 $\lambda=2$ 时区间长度恰好}=1\ ✓\ \text{（临界 ✓）}$$
⭐ **② 在 $\lambda=2$（Legendre ✓）处，$P_2$ 项【仍小 ✓】**
   $$\text{期望素数个数}\approx\frac1{\log\sqrt N}=\frac{2}{\log N}=0.145\ ✓\ \Longrightarrow\ \frac1{hN}\int P_2^2\approx\frac{0.145\cdot(6.9)^2}{2N}\approx3.5\times10^{-6}\ ✓$$
   $$\text{交叉项}\approx\frac{2}{h\sqrt N}\cdot0.145\cdot Y\cdot\mathrm{rms}(F)\cdot6.9\approx5\times10^{-5}\ ✓\ \Longrightarrow\ \textbf{皆}\ o(1)\ ✓$$
   $$\Longrightarrow\ \boxed{\textbf{$\psi\to\vartheta$ 【不是】断点 ✗ (与您 §4 的担心相反 ✓)}}$$
⭐⭐ **③ $\lambda$-扫描（本轮最有价值的数）✓**：$Q$ 随 $\lambda$ **增长** ✓
   | $\lambda=h/Y$ | 0.5 | 1.0 | **2.0（Legendre ✓）** | 3.0 |
   |:--|--:|--:|--:|--:|
   | $Q=\frac1Y\int\lvert F\rvert^2$ | $4.159\times10^{-4}$ | $1.452\times10^{-3}$ | $\mathbf{5.130\times10^{-3}}$ | $9.575\times10^{-3}$ |
   | $\mathrm{rms}\lvert F\rvert$ | $2.039\times10^{-2}$ | $3.810\times10^{-2}$ | $7.162\times10^{-2}$ | $9.785\times10^{-2}$ |
   $$\Longrightarrow\ Q\propto\lambda^{1.8}\ ✓\ \text{且【}\lambda=2\ \text{时仍}\ Q=5.13\times10^{-3}=o(1)\ ✓\ ✗}$$
   $$\Longrightarrow\ \boxed{\textbf{换到 Legendre 的 }}\lambda=2\ \textbf{也【不】能解决悖论 ✗}}$$
```

## 1. 已审计的候选断点清单（✓ 全部通过 ✗）

```
| 候选断点 | 依据 | 判定 |
|:--|:--|:--|
| ② 权重/相位对齐 | $N^{1/2}$ 公共 ✓、$N^{i\gamma}=e^{i\gamma\log N}$ 即相位 ✓ | ✅ **通过对齐 ✓**（您的 ② 已撤回 ✓） |
| ① 零截断 | E136：$R=Q/\sum\lvert A\rvert^2$ 在 $G=T/3T/10T$ 下为 $0.512/0.769/0.620$ ✓ **稳定** ✓；尾部对角 $8.6\times10^{-4}$ ✓ | ✅ **非断点 ✓** |
| ③ 单点反例 ⟹ 窗口异常 | $h=2n$ 时 $Yh^2=8n^3>hN=2n^3$ ✓ | ✅ **转换成立 ✓** |
| ④ $h(x)=2\sqrt x$ vs 固定 $h$ | 相对差 $O(N^{-1/2})$ ✓ | ⚠️ 未逐项写差额 ✗（低危 ✓） |
| ⑤ $\psi\to\vartheta$ | 本轮 ✓ | ✅ **非断点 ✓** |
| ⑥ $\lambda=1\to2$ | 本轮 ✓ | ✅ **非断点 ✓（仍 $o(1)$）** |
| ⑦ 零点和的**条件收敛/配对** | — | ⚠️ **唯一未做 ✗（下一刀候选 ✓）** |
⟹ **七项中五项目通过 ✓、两项未做 ✗ ⟹ 悖论仍在 ✗**
```

## 2. 边界与纪律（✓）

```
⚠️ **① $P_2$ 只在 $\lambda=1$ 数值验证（恒 0 ✓）**；$\lambda=2$ 的估算是【解析量纲 ✓】非数值 ✗
⚠️ **② $Q(\lambda)$ 用 $\gamma\le3T$ 截断 ✓**（$M$ 小 ✓ 便于扫描 ✓）—— 与 E136 同口径 ✓
⚠️ **③ 窗口 $Y=\sqrt N$ 固定 ✓，只变 $h$ ✓**；$N=10^6$ 单尺度 ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① ⭐ **$P_2\equiv0$ 于 $\lambda=1$（结构性 ✓）**；② **$\psi\to\vartheta$ 非断点 ✓**；
   ③ ⭐ **$Q\propto\lambda^{1.8}$，$\lambda=2$ 处仍 $o(1)$ ✓**；④ **候选断点清单：五项通过、两项未做 ✓**
```

## 3. 结论：悖论仍在，但**唯一未审的**只剩一项 ✓

$$\boxed{\textbf{⑦ 零点和的【条件收敛／配对】✗ —— 这是唯一未做的审计 ✓}}$$
$$\text{依据 ✓}：\text{逐项 }|B_\gamma|\approx2\sqrt x/\gamma\ (\gamma\gg T)\ ⟹ \sum_{\gamma>G}\ \textbf{逐项对数发散}\ ✗\ \text{（E120 ✓）}$$
$$\text{而显式公式的零点和【仅条件收敛】✓（靠 }\rho\leftrightarrow1-\bar\rho\ \text{配对 ✓）⟹ \textbf{锐截断的尾项须按配对处理 ✗（我此前未做 ✓）}}$$
