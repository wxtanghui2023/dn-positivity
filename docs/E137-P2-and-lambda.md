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

---

# E137 · (续) > 委托 ✓ 唐先生 2026-09-14 11:08（① 判 FAIL ✓；算 $Q_{\lambda=2}$ 与 $C_{\psi,2}$ ✓）
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

---

# E137（终）· 🔴 **$\psi/\vartheta$ 错位【判死 ✗】—— $P_2$ 只是低阶修正 ✓**

> 委托 ✓ 唐先生 2026-09-14 11:10（**算术尺度更正 ✓**：$N=p^2$ 必不含素数平方 ✗；改用 $N=q^2-\delta$ ✓；用闭式 ✓；报四量 ✓）
> 执行 ✓ 小灵｜内存安全 ✓（峰值 50 MB ✓）｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

## 0. 您的算术更正（✓ 我接受 ✓）

$$N=p^2,\ h=2\sqrt N\ \Longrightarrow\ \sqrt{N+Y+h}=\sqrt{p^2+3p}=p+\frac32+O(p^{-1})\ ✓\ \Longrightarrow\ \text{区间}\ (p,p{+}1.5]$$
$$\text{而奇素数 }p\ \text{的下一个候选是 }p+2\ (p+1\ \text{必偶 ✗})\ \Longrightarrow\ \textbf{必不含素数} ✗\ \Longrightarrow\ N=p^2\ \text{【永不】给出 }P_2\neq0\ ✗✓$$
$$\textbf{正确选点 ✓}：N=q^2-\delta,\ q\ \text{素数},\ 0<\delta<3q\ ✓\ \Longrightarrow\ \sqrt{N+Y+h}=q+\frac{3q-\delta}{2q}+O(q^{-1})\ ✓$$

## 1. 结果（✓ 十组：两个素数 × 五个位置 ✓）

| $q$ | $\delta/q$ | $y_0/Y$ | $Q_\psi$ | $Q_2$ | $2C_{\psi,2}$ | $Q_\vartheta$ | $Q_\vartheta/Q_\psi$ | $2C_2/Q_\psi$ |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 997 | 0.25 | $-1.750$ | $1.644\text{e-}3$ | $2.40\text{e-}5$ | $-6.15\text{e-}5$ | $1.729\text{e-}3$ | 1.052 | $-0.037$ |
| 997 | 1.00 | $-0.999$ | $3.036\text{e-}3$ | $2.40\text{e-}5$ | $-2.80\text{e-}5$ | $3.088\text{e-}3$ | **1.017** | $-0.009$ |
| 997 | 2.00 | $0.002$ | $4.932\text{e-}3$ | $2.40\text{e-}5$ | $2.375\text{e-}4$ | $4.718\text{e-}3$ | **0.957** | $0.048$ |
| 997 | 2.40 | $0.403$ | $4.142\text{e-}3$ | $1.44\text{e-}5$ | $2.043\text{e-}4$ | $3.952\text{e-}3$ | 0.954 | $0.049$ |
| 997 | 2.70 | $0.704$ | $2.676\text{e-}3$ | $7.13\text{e-}6$ | $1.182\text{e-}4$ | $2.565\text{e-}3$ | 0.958 | $0.044$ |
| 1009 | 0.25 | $-1.750$ | $4.886\text{e-}3$ | $2.35\text{e-}5$ | $-2.79\text{e-}4$ | $5.188\text{e-}3$ | 1.062 | $-0.057$ |
| 1009 | 1.00 | $-1.000$ | $3.781\text{e-}3$ | $2.35\text{e-}5$ | $7.97\text{e-}5$ | $3.725\text{e-}3$ | 0.985 | $0.021$ |
| 1009 | 2.00 | $0.002$ | $2.614\text{e-}3$ | $2.35\text{e-}5$ | $3.09\text{e-}4$ | $2.328\text{e-}3$ | **0.891** | $0.118$ |
| 1009 | 2.40 | $0.403$ | $2.553\text{e-}3$ | $1.41\text{e-}5$ | $1.869\text{e-}4$ | $2.380\text{e-}3$ | 0.932 | $0.073$ |
| 1009 | 2.70 | $0.704$ | $2.151\text{e-}3$ | $6.98\text{e-}6$ | $8.24\text{e-}5$ | $2.075\text{e-}3$ | 0.965 | $0.038$ |

## 2. 判定（✓ 依您的三条标准 ✓）

$$\textbf{① }Q_\vartheta/Q_\psi=0.891\text{–}1.062\ \textbf{（全部}\approx1\ ✓）\ \Longrightarrow\ \boxed{Q_\vartheta\approx Q_\psi\ \text{⟹}\ P_2\ \textbf{只是低阶修正} ✓}$$
$$\textbf{② }|2C_{\psi,2}|/Q_\psi\le0.118\ ✗\ \Longrightarrow\ \textbf{交叉项【不是】同尺度 ✗（您的第二条未触发 ✗）}$$
$$\textbf{③ }Q_2/Q_\psi\approx5\times10^{-3}\ ✗\ \Longrightarrow\ \textbf{二次项可忽略 ✓}$$
$$\Longrightarrow\ \boxed{\textbf{$\psi/\vartheta$ 错位【判死】✗ —— 它不是那个缺失的同尺度抵消项 ✓}}$$

## 3. 附带结构（✓）

$$\text{① }C_{\psi,2}\ \textbf{符号随 }q^2\ \text{在窗口中的位置翻转} ✓：y_0/Y<0\ (\text{平方在窗口内全程})\ ⟹ C<0\ ✗；y_0/Y>0\ (\text{跳变在窗内})\ ⟹ C>0\ ✓$$
$$\text{② }Q_\psi\ \textbf{随 }\delta\ \text{变化} \sim3\ \text{倍} ✗\ \text{（}1.64\text{e-}3\to4.93\text{e-}3\to2.68\text{e-}3\ ✓）\ \Longrightarrow\ \text{零点侧 }Q\ \textbf{本身对 }N\ \text{敏感} ✓\ \text{（与 E136 一致 ✓）}$$

## 4. 候选断点清单更新（✓）

```
✅ ② 权重/相位对齐：PASS ✓
🔴 ① 截断独立性：FAIL ✗（不可删频带 $T_{\rm eff}\lesssim\gamma\lesssim3T_{\rm eff}$ ✓）
✅ ③ 单点反例⟹窗口异常：PASS ✓
⚠️ ④ $h(x)=2\sqrt x$ vs 固定 $h$：**未做 ✗**
🔴 **⑤ $\psi\to\vartheta$：判死 ✗**（本轮 ✓）
✅ ⑥ $\lambda=1\to2$：PASS ✓（$\lambda=2$ 处 $Q=5.5\text{e-}3=o(1)$ ✓）
⚠️ ⑦ **零点和的条件收敛／配对**：**未做 ✗**
⟹ **七项中六项已判 ✓ ⟹ 剩下 ④ 与 ⑦ 两项未做 ✗ —— 而悖论仍在 ✗**
```

## 5. 边界与纪律（✓）

```
⚠️ **① $q\in\{997,1009\}$ 两个素数 ✓、$\delta/q$ 五点 ✓**（含 $y_0/Y<0$ 与 $>0$ 两类 ✓）
⚠️ **② $Q_\psi$ 用 $\gamma\le10T_{\rm eff}$ ✓**（chunked ✓）；$N\approx10^6$ 单尺度 ✓
⚠️ **③ 闭式用您的推导 ✓**（$P_2=\log q\,\mathbf 1_{y\ge y_0}$ ✓；（若窗口内含 >1 个平方素数则须修正 ✗ —— 本轮 $Y\ll$ 素数间隔尺度 ✓ 故单跳 ✓））
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **算术尺度更正 ✓**（$N=p^2$ 必失败 ✗）；② **$\psi/\vartheta$ 判死 ✗**（$Q_\vartheta/Q_\psi=0.89$–$1.06$ ✓）；
   ③ **交叉项符号结构 ✓**；④ **清单：仅剩 ④ 与 ⑦ 未做 ✗**
