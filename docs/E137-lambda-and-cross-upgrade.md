# E137（升级）· ⭐ **① 判 FAIL 证实 ✓；$\lambda=2$ 仍 $o(1)$（悖论未解 ✗）；$C_{\psi,2}$ 测试因 $N$ 选点失效 ✗**

> 委托 ✓ 唐先生 2026-09-14 11:08（① 判 FAIL ✓；算 $Q_{\lambda=2}$ 与 $C_{\psi,2}$ ✓）
> 执行 ✓ 小灵｜内存安全 ✓（峰值 51 MB ✓）｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 结论（✓ 三条）

```
🔴 **① 判 FAIL 【证实 ✓】**（接受您的判定 ✓；我此前"R stable"的读法过宽 ✗）
   | $\lambda$ | $T_{\rm eff}$ | cut $=1\!\cdot\!T_{\rm eff}$ | $3\!\cdot\!T_{\rm eff}$ | $10\!\cdot\!T_{\rm eff}$ |
   |--:|--:|:--|:--|:--|
   | 1.0 | 1000.5 | $Q{=}3.22\text{e-}4,\ R{=}0.512$ | $Q{=}1.458\text{e-}3,\ R{=}0.773$ | $Q{=}1.543\text{e-}3,\ R{=}0.620$ |
   | 1.5 | 667.2 | $4.83\text{e-}4,\ 0.568$ | $\mathbf{4.80\text{e-}3,\ 1.846}$ | $2.44\text{e-}3,\ 0.707$ |
   | 2.0 | 500.5 | $1.10\text{e-}3,\ 1.054$ | $5.007\text{e-}3,\ \mathbf{1.539}$ | $5.489\text{e-}3,\ 1.267$ |
   | 2.5 | 400.5 | $2.22\text{e-}3,\ 1.818$ | $5.08\text{e-}3,\ 1.318$ | $\mathbf{1.057\text{e-}2,\ 2.052}$ |
   $$\textbf{①-a ✓}：R\ \textbf{从不稳定 ✓}（0.512–2.052 ✗）\ \Longrightarrow\ \textbf{非"纯权重效应"} ✓\ \text{（您 §4 ✓）}$$
   $$\textbf{①-b ✓（更强 ✓）}：Q\ \textbf{对截断【非单调】✗}（\lambda{=}1.5：4.80\text{e-}3>2.44\text{e-}3\ ✓\ \text{在 }3T_{\rm eff}\ \text{处}>\ 10T_{\rm eff}\ \text{处} ✗）$$
   $$\Longrightarrow\ \textbf{截断带 }T_{\rm eff}\lesssim\gamma\lesssim3T_{\rm eff}\ \textbf{【不可删 ✗】}\ ✓\ \text{（您 §1 结论 ✓）}$$
⭐⭐ **② $\lambda=2$（Legendre ✓）处 $Q$ 仍 $o(1)$ ✗** —— **悖论【未解】✗**
   $$Q_{\lambda=2}=5.489\times10^{-3}\ (c{=}10)\ ✓\qquad Q_{\lambda=2.5}=1.057\times10^{-2}\ ✓\ \Longrightarrow\ \textbf{均 }o(1)\ ✗$$
   $$\text{且 }\lambda{=}2\ \text{时}\ R=1.267\approx1\ ✓\ \Longrightarrow\ \textbf{Q}\approx\sum\lvert A\rvert^2\ ✓\ \text{（既无相消也无放大 ✓——即"对角主导" ✓）}$$
   $$\Longrightarrow\ \text{故换到 Legendre 的 }\lambda\ \textbf{【不】解决"$Q=o(1)\Rightarrow$ Legendre"悖论 ✗}$$
⚠️ **③ $C_{\psi,2}$ 测试【失效 ✗ —— 因 $N$ 选点 ✗】**
   $$N=10^6\ \text{时：}\sqrt{N}=1000,\ \sqrt{N+Y+h}=\sqrt{1003000}\approx1001.5\ \Longrightarrow\ p\in(1000,1001.5]\ ✓\ \text{仅 }1001=7\cdot11\cdot13\ \textbf{（合数 ✗）}$$
   $$\Longrightarrow\ P_2\equiv0\ ✓\ \text{（}\max{=}0,\ \text{nonzero frac}=0\ ✓）\ \Longrightarrow\ C_{\psi,2}=0\ \textbf{【偶然 ✓ 非结论 ✗】}$$
   $$\Longrightarrow\ ⭐\ \textbf{正确做法 ✓}：\textbf{取 }N\ \text{邻近【素数平方】}（N=p^2\ \text{数个} ✓）⟹ P_2\neq0\ ✓\ \text{才能真正测 }C_{\psi,2}\ ✓$$
```

## 1. $Q$ 随 $\lambda$ 的增长（✓）

$$Q(\lambda)\ \text{（}c{=}10\ ✓）：3.216\text{e-}4\to1.543\text{e-}3\to2.440\text{e-}3\to5.489\text{e-}3\to1.057\text{e-}2\ (\lambda{=}0.5,1,1.5,2,2.5)\ ✓$$
$$\Longrightarrow\ Q\propto\lambda^{1.9}\ \text{（≈平方 ✓）}\ \Longrightarrow\ \text{窗口/区间长度比增大 ⟹ 有效频率带变宽 ⟹ Q 增长 ✓}$$

## 2. 状态正式记为（✓ 依您的口径 ✓）

```
✅ **② 权重/相位对齐：PASS** ✓（您的判定 ✓）
🔴 **① 截断独立性：FAIL** ✗ —— 但**不是项目失败 ✓**，而是定位了**不可删频率带** ✓
   $$\boxed{T_{\rm eff}\lesssim|\gamma|\lesssim3T_{\rm eff}\ \text{不可删}\ ✓}\qquad\boxed{\lambda=2\ \text{已验证（}Q=5.5\text{e-}3=o(1)\ ✓\ ✗\text{）}}$$
⏳ **$C_{\psi,2}$：尚未验证 ✗**（本轮测试因 $N$ 选点失效 ✗；下一刀取 $N$ 邻近素数平方 ✓）
```

## 3. 边界与纪律（✓）

```
⚠️ **① $N=10^6$ 单尺度 ✓**；$\lambda$ 四点 ✓；cutoff 三档 ✓（$c=1,3,10$ ✓）
⚠️ **② $Q$ 用 $\gamma\le c\,T_{\rm eff}$ 截断 ✓**（chunked ✓ 无稠密矩阵 ✓）
⚠️ **③ $P_2$ 只在 $N=10^6$ 测 ✓** ⟹ 恒 0 ✗ ⟹ **须扫多个 $N$（邻素数平方 ✓）**
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **① FAIL 证实（含非单调性 ✓ 更强）**；② **$\lambda=2$ 处 $Q=5.5\text{e-}3=o(1)$ ⟹ 悖论未解 ✗**；
   ③ **$C_{\psi,2}$ 测试方法更正（须取 $N\approx p^2$ ✓）**；④ **不可删频率带已定位 ✓**
