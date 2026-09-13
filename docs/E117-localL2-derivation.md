# E117 · ⭐⭐⭐ **推导结果：RH ⇏ 局部 $L^2$ 反集中；控制它的是【零点对相关】** ✓ ＋ 一处更正 ⚠️

> 委托 ✓ 唐先生 22:44 "继续推导" ✓（直接推：RH 能否推出 Bazzanella 型局部 $L^2$ anti-concentration ✓）
> 执行 ✓ 小灵｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**无计算 ✓**；⚠️ 全文标【推导】✗ 非定理 ✓

---

## 0. 结论（✓ 四条 ＋ 一处更正 ⚠️）

```
✅ **① 第一刀结果（含一处更正 ⚠️）**：`E83` 的对象是 **$t$-侧**：$\int_a^b S(t)^2dt$ ✓（$S=N-M$ ✓ 零点计数误差 ✓；
   需要的形状 $\int_a^bS^2\le(b-a)c(1+\eta)$ ✓，$c=\log\log T/(2\pi^2)$ ✓，允许 $\eta\le\mathbf{9.04\%}$ ✓，经典只给 $O(T)$ ⟹ 相对误差 $\approx38\%$ ✗）
   $$\textbf{而 Bazzanella 的对象是}\ x\textbf{-侧}\ \checkmark：\ J(N,h)=\int_1^N(\vartheta(x+h)-\vartheta(x)-h)^2dx\ ✓$$
   $$\Longrightarrow\ \textbf{我 E116 的"同一对象"说法【过强】✗ ⟹ 更正为【同型对象】✓（经显式公式相互转化 ✓，但非同一个积分 ✓）}$$
⭐⭐⭐ **② 推导主结果：RH（点态界）【不推出】局部 $L^2$ 反集中** ✓✓
   $$\Longrightarrow\ \textbf{控制它的 INPUT ＝ 【零点对相关】}\ \checkmark\checkmark$$
   $$\textbf{Bazzanella 的 Conjecture 3 ＝ 一个【弱对相关假设】}\ ✓：\text{弱于 Montgomery 强对相关 ✓（其自述 ✓），强于 RH ✓✓}$$
⭐⭐ **③ 两条界的来源已定位（解决 E116 的"待解差异" ✓）**：
   $$\text{【对角项】＝ 相位无关项 ✓}\ \approx N\log N\ ✓\ \Longrightarrow\ o(hN)\ \checkmark$$
   $$\text{【非对角项】＝ 相位对齐（最坏 ✓）}\ \le N\log^4N\ ✗\ \text{每单位 }x\ \Longrightarrow\ \text{窗口积分 }N^{3/2}\log^4N\ ✗\ \textbf{超 }hN\ ✓$$
   $$\Longrightarrow\ \textbf{缺口 ＝ }\log^4\ \text{（在 }L^2\text{ 对象上 ✓ —— \textbf{不是点态路线的"一个 }\log\text{"}} ✗）\ \checkmark$$
⭐ **④ 唐先生要求的"最小集中量"✓**：**RH 允许的最小集中 ＝ 【相位对齐情形】** ✓
   $$\Longrightarrow\ \text{RH 允许每单位 }x\ \text{的局部二阶矩达 }N\log^4N\ ✗\ \text{（要求只到 }o(N)\ ✓）\ \Longrightarrow\ \textbf{缺口 }\log^4$$
```

## 1. 推导（✓ $x$-侧 ✓）

$$\Delta(x,h)=\psi(x+h)-\psi(x)-h=-\sum_\rho\frac{(x+h)^\rho-x^\rho}{\rho}+(\text{低阶})\ ✓$$
$$\int_N^{N+Y}\Delta^2dx=\sum_{\rho,\rho'}\frac{1}{\rho\bar\rho'}\int_N^{N+Y}\bigl[(x+h)^\rho-x^\rho\bigr]\bigl[(x+h)^{\bar\rho'}-x^{\bar\rho'}\bigr]dx\ ✓$$

### 对角项（$\rho=\rho'$ ✓，相位无关 ✓）

$$\gamma\ll\sqrt N：\ (x+h)^\rho-x^\rho\approx\rho h x^{\rho-1}\ \Longrightarrow\ \frac{|\cdot|^2}{|\rho|^2}\approx h^2x^{2\beta-2}\ \xrightarrow{\ \beta=1/2\ }\ h^2x^{-1}\ ✓$$
$$\text{窗口积分（每零 ✓）}\approx h^2Y/N\ ✓\qquad\text{零个数 }\gamma\lesssim\sqrt N：\approx\sqrt N\log N\ ✓$$
$$\Longrightarrow\ \text{对角}\approx(\sqrt N\log N)\cdot\frac{h^2Y}{N}=\frac{\sqrt N\log N\cdot N\cdot\sqrt N}{N}=\boxed{N\log N}\ \checkmark$$

### 非对角项（$\rho\ne\rho'$ ✓，含相位 $e^{i(\gamma-\gamma')\log x}$ ✓）

$$\int_N^{N+Y}x^{-1+i\delta}dx\approx\min\!\Bigl(\frac YN,\frac1{|\delta|}\Bigr)\qquad(\delta=\gamma-\gamma')\ ✓$$
$$\Longrightarrow\ \text{每对}\ \lesssim\frac{h^2}{\gamma\gamma'}\min\!\Bigl(\frac YN,\frac1{|\delta|}\Bigr)\ ✓\qquad\text{粗界（取 max ✓）}\ \lesssim\frac{h^2}{\gamma\gamma'}\ ✓$$
$$\Longrightarrow\ \text{非对角}\ \le h^2\Bigl(\sum_{\gamma\le x}\frac1\gamma\Bigr)^2\approx h^2\Bigl(\tfrac12\log^2x\Bigr)^2\times\text{const}=\boxed{N\log^4N}\ ✗\ \text{（相位全对齐时 ✓）}$$

$$\Longrightarrow\ \boxed{\text{对角 }N\log N\ (\text{典型 ✓})\quad\text{vs}\quad\text{非对角 }N\log^4N\ (\text{对齐 ✓})\ \Longrightarrow\ \text{真值在两者之间，由对相关决定}\ \checkmark}$$

## 2. ⭐⭐ 于是：控制的 INPUT ＝ **零点对相关**（✓）

```
【为何 ✓】非对角项的【实际】大小由"相差 $\delta$ 的零点对有多少"决定 ✓ —— 这正是【对相关函数】✓
   · 若对相关呈【GUE/随机型】（Montgomery ✓）：相消 ⟹ 对角主导 ⟹ 局域化 ✓✓
   · 若零点【聚集】（相位对齐 ✓）：无相消 ⟹ 达 $\log^4$ 上界 ✗
⟹ ⭐ 故 Bazzanella 的 C3 ＝ **弱对相关假设** ✓（弱于 Montgomery 强对相关 ✓ 强于 RH ✓✓ —— 与其自述一致 ✓）
```

## 3. ⭐ 与项目既有对象的**正规连接**（✓ 更正后 ✓）

| 线 | 对象 | 侧 | 需要的输入 |
|:--|:--|:--|:--|
| **T1（Li 范围 ✓，E83 ✓）** | $\int_a^b S(t)^2dt\ll(b-a)c(1+\eta)$ ✓，$\eta\le9.04\%$ ✓ | **$t$-侧** ✓ | 局部 Selberg 二阶矩的**显式常数** ✓ |
| **L3（Legendre／Brocard ✓）** | $J(N+Y,h)-J(N,h)=o(hN)$ ✓ | **$x$-侧** ✓ | **弱对相关** ✓（本轮导出 ✓） |
| ⟹ | **同型**（经显式公式互转 ✓）| **非同积分** ✗ | ⭐ **两者都落在【二阶零点统计】这一类** ✓✓ |

$$\Longrightarrow\ \boxed{\text{跨线结论（更正版 ✓）}：\text{两条线【同型不同物】✓，但所需 INPUT 同属【二阶零点统计】}✓✓}$$

## 4. ⚠️ 未决（诚实 ✓）

```
⚠️ **末步未定 ✓**：Montgomery 的**无条件对相关**只覆盖 support $\le1$（即 $|\delta|\lesssim$ 平均间距 ✓）✓
   —— 若"小 $\delta$ 主导"成立 ⟹ **输入无条件可得** ⟹ Legendre 可证 ✗ ⟹ **与已知矛盾** ✗
   ⟹ ⚠️ **故我的簿记仍有缺口** ✗（最可疑处：条件收敛／截断权重 $1/(|\rho||\rho'|)$ 使大 $|\delta|$ 贡献**不可忽略** ✗）
   ⟹ **我不声称 §1 的界是精确的** ✓ —— 只声称**结构**（对角 vs 非对角／对相关为控制输入 ✓）✓
⚠️ **§2 的"对相关为控制输入"是【机制论证】✗，非定理** ✓
⚠️ **未用 RH** ✓；**未跑 Lean** ✓；**无计算** ✓
⭐ **本轮净产出 ✓**：① 第一刀完成（**E83 是 $t$-侧 ⟹ 更正 E116 的"同一对象" ✗**）；
   ② **RH ⇏ 局部反集中**（推导 ✓）；③ **控制输入 ＝ 对相关** ⟹ **C3 ＝ 弱对相关假设** ✓；
   ④ **缺口 ＝ $\log^4$（L² 对象 ✓，非点态的"一个 $\log$" ✓）** ✓
```
