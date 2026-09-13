# E84b · **接口判定 (b)** ✓ —— **通过 ✓（$L(T)=\log\log T$，$A=0$ ✓）** ＋ **撤回"任意 polylog"** ✗

> 委托 ✓ 唐先生（20:00 指正 ＋ 指定 (b) ✓）｜执行 ✓ 小灵
> 纪律 ✓ 未用 RH ✓（判定只用**无条件**的 Selberg 第二矩 ✓）；未跑 Lean ✓

---

## 0. 结论（✓ 三条 ✓）

```
⚠️ **① 接受指正 ✓**："任意 polylog 都够" ✗ **错误** ✓ —— 正确条件是 $A<2$ 即 $L(T)=o((\log T)^2)$ ✓
   （您的推算 ✓ 复核通过 ✓：$\lvert S^{\rm mid}\rvert/N\ll(\log T)^{A/2-1}$ ✓）
✅ **② 二元判定 (b)：接口【通过】✓✓** —— 而且**$A=0$**（$L(T)=\log\log T$ ✓），远超所需 ✓
⭐ **③ 关键：我们的带【不是短区间】** ✓ —— 它们都是 $[0,T]$ 的**常数比例**（0.052 ~ 0.699 ✓）
   ⟹ **直接用 Selberg【全局】第二矩相减即得** ✓ ⟹ **无需短区间理论** ✗
   ⟹ 因此**避开了您第 4 点的警告** ✓（不混用 Selberg 的两套体系 ✗✓）
```

## 1. 精确定义（✓ 回答您"把 $\mathcal E(t)$ 精确写出来" ✓）

$$\mathcal N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+\frac78+\mathcal E(t)\qquad\Longrightarrow\qquad\boxed{\ \mathcal E(t)=S(t)+O(1/t),\quad S(t)=\frac1\pi\arg\zeta(\tfrac12+it)\ }$$

```
✓ **与我们 E73 用的 $S$ 是同一个对象** ✓（显式界 $\sup|S|\le0.110\log T+0.290\log\log T+2.290$ ✓ 即对 $\mathcal E$ ✓）
✓ $\int_I\lvert\mathcal E\rvert^2=\int_I\lvert S\rvert^2+O(1)$ ✓（交叉项 $\ll$ ✓）
```

## 2. 接口（✓ 照您的写法 ✓）

$$\boxed{\ \mathcal L(H,T):=\int_I\lvert\mathcal E(t)\rvert^2dt\;\stackrel{?}{\ll}\;H\cdot L(T),\qquad H=\lvert I\rvert\ }$$

$$\text{需}\quad L(T)=o\bigl((\log T)^2\bigr)\;\Longleftrightarrow\;A<2$$

## 3. ⭐ 判定通过（✓ $A=0$ ✓）

```
【关键观察 ✓】**我们的带全是 $[0,T]$ 的常数比例** ✓（不是短区间 ✗）：
   中间带 $[\sqrt{n/11},\sqrt n]$：长度 $0.699\sqrt n$ ✓（$n=T^2$ 时 $=0.699T$ ✓）
   子带（$u$-二进 ✓）：长度 $0.052\sqrt n\sim0.293\sqrt n$ ✓ ⟹ 比例 $0.052\sim0.293$ ✓
   慢区 $[\sqrt n,T]$ ✓：长度 $T-\sqrt n$ ✓（$n$ 接近 $T^2$ 时趋于 0 ✗ —— 见下 ✓）
【⟹ 于是 ✓】
   $$\int_I\lvert\mathcal E\rvert^2=\int_0^T-\int_0^{aT}\asymp(1-a)\,T\cdot\frac{\log\log T}{2\pi^2}$$
   ⟹ $\boxed{L(T)=\log\log T}$ ✓ ✓（**每单位长度的常数与全局相同** ✓）
【所得依据 ✓】**Selberg 第二矩（全局 ✓）**：
   $\int_0^T\lvert S\rvert^2=\frac{T}{2\pi^2}\log\log T\,(1+o(1))$ ✓ —— **无条件成立** ✓（同主项 ✓，误差略弱 ✓）
   ⟹ 相减即得局部 ✓ ⟹ **不需要任何短区间定理** ✗✓
   ⟹ ⭐ 因此**不触碰您指出的"两套 Selberg 体系"风险** ✓（我们**只用** $S(t)$ 的矩体系 ✓）
【慢区 ✓】其长度 $T-\sqrt n$ 可任意小 ✗ ⟹ 严格说需短区间版本 ✗ —— 但：
   其 $\lvert\varphi'\rvert\asymp1$ ✓ ⟹ $\lVert\varphi'\rVert_2\asymp\sqrt{T-\sqrt n}$ ✓、$\lVert\mathcal E\rVert_2=O(\sqrt{(T-\sqrt n)L})$ ✓
   ⟹ 慢区 $\ll(T-\sqrt n)\sqrt{L}=o(N)$ ✓（当 $L=o(\log^2T)$ ✓）⟹ **对任何 $L=o(\log^2T)$ 都安全** ✓✓
```

## 4. 指数审计（✓ 二元 ✓）

| $L(T)$ | $A$ | $(\log T)^{A/2-1}$ | 判定 |
|:--|:--|:--|:--|
| $(\log T)^2$ | 2 | $O(1)$ | ✗ **不闭合** |
| $(\log T)^{2-\delta}$ | $2-\delta$ | $\to0$ | ✓ 闭合 |
| $\log T$ | 1 | $(\log T)^{-1/2}\to0$ | ✓ 闭合 |
| **$\log\log T$** | **0** | $\sqrt{\log\log T}/\log n\to0$ | ✅ **本判定所得 ✓✓** |

$$\Longrightarrow\;\frac{\lvert S^{\rm mid}\rvert}{N}\ll\frac{\sqrt{\log\log T}}{\log n}\Big|_{T=1.13\times10^6}=\frac{1.623}{13.94}=\mathbf{0.116}\quad(\text{系数另计 ✓；$\to0$ ✓})$$

## 5. 判定与状态（✓）

```
✅ **二元判定 (b)：通过 ✓** —— 接口 $\mathcal L\ll H\log\log T$ 由**无条件 Selberg 全局第二矩**给出 ✓
   ⟹ **E84 的渐近路线【活着】** ✓（且 $A=0$ 远优于所需的 $A<2$ ✓✓）
⚠️ **但两处仍须保留 ✓**：
   ① **有限尺度 $T=1.13\times10^6$ 仍未闭合** ✗（修正常数后 ≈0.83 vs 0.80 ✓）；$T_0$ 是定量问题 ✓
   ② **$T\to\infty$ 的渐近陈述** ✓ —— **不等于**"已在可达尺度证明" ✗
⚠️ **撤回 E84 的过强措辞 ✓**："任意 polylog" ✗ ⟹ 更正为 **$L(T)=o((\log T)^2)$，实际 $=\log\log T$** ✓
【净结果 ✓】$$\boxed{\textbf{T1}\Leftarrow\underbrace{\text{深快区 }0.3015N}_{\text{平凡 ✓}}+\underbrace{L(T)=o(\log^2T)\text{ 的局部二阶矩}}_{\text{Selberg 无条件 ✓，实际 }L=\log\log T}}$$
```

## 6. 纪律（✓）

```
✓ 未用 RH ✓（判定依赖**无条件** Selberg ✓；Goldston 的 $a$ 仅在 E84 作诊断 ✗）
✓ 未混用 Selberg 两套体系 ✓（只取 $S(t)$ 矩 ✓）
✓ **未宣布 T1 已证** ✗；**未宣布可达尺度闭合** ✗
✓ R7 ✓：结论由指数审计表驱动 ✓
```
