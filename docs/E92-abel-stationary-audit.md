# E92 · ⭐⭐ **Abel 项的显式公式／驻相审计** ✓ —— 路线 A 渐近判死 ✓；**您的 §10 非共振机制跑出 44 倍余量** ✓✓

> 委托 ✓ 唐先生（20:47 更正 ＋ §10 推导指令 ✓）｜执行 ✓ 小灵
> 脚本 ✓ `scripts/E92_abel_stationary_audit.py` ＋ `.txt` ✓｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 结论（✓ 四条 ✓）

```
⛔ **① 我的归一化错误（接受更正 ✓）**：Abel 后 C–S 是 $|D_I|\le\lVert S\rVert_2\sqrt{E_\phi}$ ✓，**无 $1/\sqrt{2\pi}$** ✗
   ⟹ 我 E91 的 "$C\le0.33$" **是假象** ✗ **作废** ✓
   ⟹ 脚本复核 ✓：$D_{\rm CS}=\sqrt{1.055856e5}\sqrt{1.339467e7}=\mathbf{1.189237e6}$ ✓ —— 与您的 $1.19e6$ **完全一致** ✓✓
⛔ **② 路线 A【渐近判死】✓（不需 Karatsuba 常数 ✓）**：
   $$\frac{|D_I|}{H}\lesssim\sqrt{\frac{\Lambda_\infty}{2\pi^2}}\sqrt{\log\log T}=\mathbf{0.926199}\sqrt{\log\log T}\to\infty$$
   $\Lambda_\infty=\dfrac{11^{3/2}-1}{3(1-11^{-1/2})}=\mathbf{16.933166}$ ✓ —— **不随 $n$ 下降** ✓（**修正我"$T_0$ 小"的幻想** ✗）
   ⟹ C–S 把 $|\phi'|$ 当绝对值 ⟹ **丢掉了真正需要的振荡** ✓（您的诊断 ✓）
⭐⭐ **③ 您的 §10 机制【成功】✓✓（附一处更正 ⚠️）**：
   "−"支 $(\Phi_m^-)'=\phi'-\log m<0$ 恒负 ✓ **无驻点** ✓（**您正确** ✓）
   ⚠️ **但** $\sin(kt\log p)$ 展开后 "＋"支 $(\Phi_m^+)'=\phi'+\log m$ **有驻点** ✓（$\log p\in[1,11]$ ⟺ $p\in[e,e^{11}]$ ✓，**6047 个** ✓）
   $$\text{(A) 非驻相}=32.96\,;\quad\text{(B) 驻相}=2.3982\times10^{4}\,;\quad\textbf{合计 }2.4015\times10^{4}\ \text{vs 允许 }1.063\times10^{6}$$
   $$\boxed{\textbf{比值 }2.26\%\ \Longrightarrow\ \textbf{余量 44 倍}\ \checkmark\checkmark}$$
⚠️ **④ 但【剩余墙】= 显式公式的余项** ✗：$\lVert R\rVert_\infty\cdot\int_I|\phi'|=1\cdot2.62\times10^{6}$ ✗（超允许 2.5 倍 ✗）
   ⟹ 余项**也需自身相消** ✗ —— 但**同一非共振想法或可覆盖** ✓（余项频率 $\ge\log X=\log T=13.94>|\phi'|_{\max}=11$ ✓）
```

## 1. 路线 A 判死（✓ 数据 ✓）

| 量 | 值 |
|:--|:--|
| $\int_IS^2$ 主项（$T_0=1.13249\times10^6$） | $1.055856\times10^{5}$ |
| $E_\phi=\frac{11^{3/2}-1}{3}\sqrt n$ | $1.339467\times10^{7}$ |
| $H=(1-11^{-1/2})\sqrt n$ | $7.910319\times10^{5}$ |
| $\Lambda_I=E_\phi/H\to\Lambda_\infty$ | $\mathbf{16.933166}$ ✓（**不衰减** ✗） |
| $D_{\rm CS}$（误差取零 ✓） | $\mathbf{1.189237\times10^{6}}$ ✗（超允许 1.119 倍 ✗） |
| $\lvert D_I\rvert/H$ 渐近 | $0.926199\sqrt{\log\log T}\to\infty$ ✗ |

```
⭐ **故【不必】再抽 Karatsuba 的隐含常数** ✓（我上一轮的"下一步"作废 ✗）
   ⟹ 路线 A 的死因**不是精度** ✗ 而是 **C–S 本身把 $\phi'$ 当绝对值** ✓（您的原话 ✓）
```

## 2. ⭐ 您的 §10 推导：成功（✓ 附更正 ✓）

$$\text{显式公式}\quad S(t)=\frac1\pi\Im\sum_{m\le X}\frac{\Lambda(m)}{\sqrt m\log m}m^{-it}+R(t),\qquad X=T_0$$
$$D_I=\sum_m a_m\int_IK_n(t)m^{-it}dt\ \Longrightarrow\ \text{相位 }\Phi_m^\pm(t)=\phi(t)\pm t\log m$$

| 支 | 导数 | 驻点 | 贡献 |
|:--|:--|:--|:--|
| **"−"** | $\phi'-\log m<0$ 恒负 ✓ | **无** ✓（您的论断 ✓） | (A) $=32.96$ ✓ |
| **"＋"** ⚠️ | $\phi'+\log m$ | **有**（$\log m\in[1,11]$ ✓） | (B) $=2.3982\times10^{4}$ ✓ |

$$\boxed{\text{(A)+(B)}=2.4015\times10^{4}\qquad\text{vs 允许 }1.063\times10^{6}\qquad\Longrightarrow\qquad\textbf{比值 }2.26\%\ (\text{余量 }44\times)\ \checkmark\checkmark}$$

```
⭐ **这是今日第一个【不显然死】的机制** ✓ —— 且量级宽裕 ✓✓
· (A) 用积分分部 $\le2c_p/\min|\Phi'|$ ✓（$\min|\Phi'|=|\phi'|_{\min}+\log p$ ✓）
· (B) 用标准驻相 $c_p\sqrt{2\pi/|\Phi''(t_p)|}$ ✓，$t_p=\sqrt{n/\log p}$ ✓
· **(B) 由小素数主导** ✓（$p=3$ 约 $10^3$ ✓；大端 $p\approx6\times10^4$ 每项约 $1.28$ ✓）
· **素数总频与 chirp 相位在实轴上【不共振】** ✓（"−"支 ✓）—— 这正是您提出的 **frequency separation** ✓✓
```

## 3. 剩余墙（✓ 诚实标注 ✓）

$$\lVert R\rVert_\infty\int_I|\phi'|dt=1\cdot\sqrt n(\sqrt{11}-1)=2.62\times10^{6}\ >\ 1.063\times10^{6}\ \ ✗\ (\text{超 }2.5\times)$$

```
⚠️ **故余项 $R$ 若只按【点wise 界】处理，会吞掉全部收益** ✗
⭐ **但同一非共振思想【可能】覆盖它** ✓：余项频率 $\ge\log X=\log T=13.94>|\phi'|_{\max}=11$ ✓
   ⟹ 需要**余项的具体结构**（标准截断的零侧尾项 ✓）—— **这是下一轮的唯一任务** ✓
⚠️ **未宣布机制成立** ✗（余项未处理 ✓）；**未宣布路线活** ✗
```

## 4. 纪律（✓）

```
✓ **未用 RH** ✓（显式公式为无条件 ✓）；**未跑 Lean** ✓
✓ **自我更正 2 处** ✓：① C–S 多乘 $1/\sqrt{2\pi}$ ✗（废 $C\le0.33$ ✓）；② "无驻点"仅对 "−"支 ✗（"＋"支有 6047 个驻点 ✓）
✓ R1–R7 ✓：脚本入仓 ✓、输出入仓 ✓、头部 docstring ✓、`check_archive.py` ✓
```
