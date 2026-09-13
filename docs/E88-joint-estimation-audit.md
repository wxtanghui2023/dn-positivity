# E88 · **联合估计审计** ⚠️ —— 结构结论成立 ✓；决定性数字需**无条件**原证明 ✗

> 委托 ✓ 唐先生（20:22 "把这个常数项推导出来"＋联合估计审计规格 ✓）｜执行 ✓ 小灵
> 纪律 ✓ 未用 RH ✓（RH 结果仅作诊断 ✗）；未跑 Lean ✓

---

## 0. 判定（✓ 三条 ✓）

```
⚠️ **① 标签更正 ✓（照您的谨慎标注 ✓）**：
   无条件：$\int_0^TS^2=\frac{T}{2\pi^2}\log\log T+O(T\sqrt{\log\log T})$ ✓
   RH 下：$\int_0^TS^2=\frac{T}{2\pi^2}\log\log T+O(T)$ ✓（**是否归因 Selberg 本人，待原文** ✓）
⚠️ **② 我的实质问题（自查 ✓）**：E87 抽出的"骨架"来自 arXiv:2006.08503 ＝ **RH 下**的 $S_n$ 精细计算 ✗
   ≠ 我们需要的**无条件 Thm 6/7** ✗ ⟹ **对象错位 ✓** ⟹ 联合优化**无法仅凭该脚手架完成** ✗
✅ **③ 但一条结构结论【成立】✓✓（正是您最后一点 ✓）**：
   **主项精确正比于带长** ✓ ⟹ "两个全局二阶矩相减"的人为损失**原则上可避免** ✓ ⟹ **接口 sharpen 方向正确** ✓
```

## 1. 结构结论（✓ 可确立 ✓）

$$S(t)=P_x(t)+R_x(t),\qquad P_x=\sum_{m\le x}c_mm^{-it},\quad c_m=\frac{\Lambda(m)}{\sqrt m\log m}f_0\Bigl(\frac{\log m}{\log x}\Bigr)$$

$$\int_a^bP_x^2=(b-a)\sum_{m\le x}|c_m|^2+\text{(off-diagonal)}$$

$$\sum_{m\le x}|c_m|^2=\sum_{p^k\le x}\frac{1}{k^2p^k}=\sum_p\frac1p+O(1)=\log\log x+O(1)$$

```
⭐ **主项 $\propto(b-a)$** ✓✓ —— 来自 Dirichlet 多项式的**对角项** ✓
   ⟹ 若对差值直接估计 ✓，则主项自动按带长缩放 ✓ ⟹ **无 $\sim T\sqrt{\log\log T}$ 的人为损失** ✓✓
· off-diagonal ✓：$m\ll(b-a)$ 时可控 ✓；我们的 $m\le x=T^\theta< T\approx(b-a)$ ✓ ⟹ 满足 ✓
```

## 2. 三条误差项的**联合优化**（✓ 框架 ✓）

```
【来自脚手架的形态 ✓（注意：为 RH 版 ✗）】
   $E_1\asymp x^2$ ✓｜$E_2\asymp\frac{\sqrt x\log T}{(\log x)^{n+1}}$ ✓｜$E_3\asymp\frac{x\log T}{(\log x)^{n+1}}$ ✓
【联合优化 ✓（您的第 3 点 ✓）】取 $x=T^\theta$ ✓：$E_1\asymp T^{2\theta}$ ✓、$E_2\asymp T^{\theta/2}\log T/(\log T)^{n+1}$ ✓、
   $E_3\asymp T^\theta\log T/(\log T)^{n+1}$ ✓ —— 三者随 $\theta$ **方向相反** ✓ ⟹ **最优 $\theta$ 存在** ✓
   目标量级 $T\cdot(\cdot)$ ✓ ⟹ 需 $2\theta\le1$ ✓ 且 $\theta\le1$ ✓ ⟹ $\theta\le1/2$ ✓ ⟹ **最优在 $\theta$ 边界附近** ✓
【但 ⚠️】**这三项的形态属于 RH 版** ✗ —— 无条件版的误差结构**不同且更松** ✗ ⟹ **不能据此定 $C$** ✗
```

## 3. 交叉项保留（✓ 您的建议 ✓）与所需 $\rho$

$$\int_a^bS^2=\int P_x^2+2\Re\int P_x\bar R_x+\int|R_x|^2,\qquad 2\Re\int P_x\bar R_x\le2\sqrt{\textstyle\int P_x^2\cdot\int R_x^2}$$

$$\eta\approx2\sqrt\rho+\rho,\quad \rho:=\frac{\int R_x^2}{\int P_x^2}\qquad\Longrightarrow\qquad\eta\le0.05\;\Longleftrightarrow\;\boxed{\rho\le6.3\times10^{-4}}$$

```
⟹ 若走"保留交叉项"路线 ✓，需**余项均方仅为主项的 0.06%** ⚠️（极苛刻 ✓）
⟹ 故**更可靠的是 band-direct** ✓（主项 $\propto(b-a)$ ✓ 且误差也按带长缩放 ✓）—— 但那需**原证明** ✓
```

## 4. 判定与生死判据（✓ 按您给的 ✓）

| 判据 | 结果 |
|:--|:--|
| 结构上人为损失可否避免？ | ✅ **可** ✓（主项 $\propto(b-a)$ ✓） |
| $C_{\min}^{\rm Selberg}\le0.05$？ | ⚠️ **未能判定** ✗（需**无条件** Thm 6/7 的逐步结构 ✓） |
| 窗口比 $C_{\rm allowed}/C_{\rm true}$ | **1.14** ✓ ⟹ **粗略取绝对值相加必败** ✓（您的判断 ✓） |

$$\boxed{\text{若能证明 band-direct 的误差亦 }\propto(b-a)\text{（或相对主项可控）}\Longrightarrow\textbf{路线可活}\ ✓;\ \text{否则封死}\ ✗}$$

## 5. 诚实标注（✓）

```
✓ **本轮是"审计框架 ＋ 一条结构结论"** ✓，**不是**常数结果 ✗
⚠️ **须优先解决的事 ✓**：拿到**无条件** Selberg Thm 6/7 的证明（Collected Papers vol.1 ✓ 或图书馆 ✓）
   —— 因为脚手架的误差形态是 **RH 版** ✗，不能用于我们的无条件需求 ✓
⚠️ **未宣布 $C\le0.05$** ✗；**未宣布路线已活/已死** ✗
✓ R7 ✓：结论由 $\sum|c_m|^2=\log\log x+O(1)$ 与 $\rho\le6.3e-4$ 的算式驱动 ✓
```
