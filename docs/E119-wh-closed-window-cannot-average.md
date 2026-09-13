# E119 · ⭐⭐⭐ **$W_h$ 正式关闭（高度 cutoff，非差频 cutoff）＋ 一个直接后果：窗口【不能平均相位】** ✓

> 委托 ✓ 唐先生 22:49（$W_h$ 算到底 ✓；并指定下一步：展开二次型，问 positivity／large-sieve 能否给 $o(hN)$ ✓）
> 执行 ✓ 小灵（录取唐先生计算 ＋ 追加一步 ✓）｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**无计算 ✓**；⚠️ 全文标【推导】✗

---

## 0. 结论（✓ 四条 ＋ 一条正式关闭 ✓）

```
✅ **① $W_h$ 正式关闭 ✓（唐先生的结论，逐字录取 ✓）**
   $$\Delta(x,h)\simeq-\sum_\rho x^\rho\frac{(1+h/x)^\rho-1}{\rho}\ ✓\qquad u=\log(1+h/x)\sim\frac hN\ ✓\qquad A(\rho;u)=\frac{e^{u\rho}-1}{\rho}\ ✓$$
   $$\textbf{非对角核 ✓}：\boxed{W_h(\gamma,\gamma')=A_\gamma\overline{A_{\gamma'}}}\ \text{—— \textbf{是【one-body × one-body】，不是 pair-correlation kernel}} ✗$$
   $$\textbf{两区结构 ✓}：|\gamma|\ll T\ (T=1/u\asymp\sqrt N)\ \Longrightarrow\ A_\gamma=u+O(u^2|\rho|)\ \Longrightarrow\ |A_\gamma|\asymp u\ ✓\ \textbf{（无衰减 ✓）}$$
   $$\qquad\qquad\quad\ |\gamma|\gg T\ \Longrightarrow\ |A_\gamma|\ll1/|\gamma|\ \checkmark\ \text{（但只在 }\gamma>T\text{ ✗，不在 }|\gamma-\gamma'|>T\ ✗）$$
   $$\textbf{结构性反证 ✓（唐先生）}：\gamma=T,\ \gamma'=T-\tfrac T2\ \Longrightarrow\ \delta=\tfrac T2\gg\nicefrac{T}{\log T}\ \text{而}\ |W_h|\asymp u^2\ \textbf{不随 }\delta\text{ 下降}\ ✗$$
   $$\boxed{W_h\ \textbf{是高度 cutoff，不是差频 cutoff}\ \Longrightarrow\ \textbf{不可能把 pair-correlation support 从 }T\text{ 压到 }T/\log T}\ ✗\ \text{（我方候选机制正式关闭 ✓）}$$
⭐⭐⭐ **② 追加：窗口【不能平均相位】（本轮新点 ✓，由您的"尺度巧合"直接导出 ✓）**
   $$K_Y(\delta)=\int_N^{N+Y}e^{i\delta\log x}dx\quad\Longrightarrow\quad \text{相位跨窗口的总变化}\ \approx\delta\cdot\frac YN\ \le\ T\cdot\frac1T=O(1)\ ✓$$
   $$\Longrightarrow\ \textbf{对 }|\delta|\lesssim T\ \text{（即整个相关区 ✓），相位变化 }O(1)\ \Longrightarrow\ \textbf{窗口【无法】用平均消掉相位}\ ✗$$
   $$\Longrightarrow\ \boxed{\int_N^{N+Y}|\Delta|^2dx\ \approx\ Y\cdot|\Delta(N,h)|^2}\ \checkmark$$
   $$\Longrightarrow\ ⭐\ \textbf{局部 }L^2\text{ 路线【不能绕开】点态墙}\ ✗\ \text{—— \textbf{而"尺度巧合"正是原因}} ✓✓$$
⭐⭐ **③ 于是要求被压成【点态形式】✓**
   $$\mathcal E=o(hN)\ \Longleftrightarrow\ Y|\Delta|^2=o(hN)\ \Longleftrightarrow\ |\Delta(N,\sqrt N)|^2=o(N)\ \Longleftrightarrow\ \boxed{|\Delta(N,\sqrt N)|=o(\sqrt N)}$$
   $$\text{而 RH 给}\ |\Delta|=O(\sqrt N\log^2N)\ ✗\ \Longrightarrow\ \textbf{RH 差【一个 }\log^2\text{】}\ ✓\ \text{（且与 Bazzanella 的"RH 不足"一致 ✓）}$$
⭐ **④ 二次型结构与 positivity 的正确用法 ✓**
   $$K_Y(\gamma-\gamma')=\int_N^{N+Y}e^{i\gamma\log x}\overline{e^{i\gamma'\log x}}dx=\langle\phi_\gamma,\phi_{\gamma'}\rangle_{L^2[N,N+Y]}\ \Longrightarrow\ \textbf{$K_Y$ 是 Gram ⟹ 【半正定】}\ ✓$$
   $$\Longrightarrow\ \mathscr C_T[f]=\Bigl\|\sum_\gamma f_T(\gamma)\phi_\gamma\Bigr\|^2\ \ge0\ \checkmark\ \text{—— ⚠️ 故 positivity 给的是【下界】，\textbf{不是}我们要的上界 ✗}$$
   $$\Longrightarrow\ \textbf{上界须用【对偶正性】＝ 窗口指示函数的【正定 majorant】}\ ✓\ \text{（Beurling–Selberg／Selberg 型 ✓）}\ \text{—— 即项目早先 N7 bandlimited 路线同一工具族 ✓}$$
```

## 1. 🔴 我必须公开的一处**持续簿记冲突**（第三次 ⚠️）

$$\text{用 majorant／大筛估计：}\ \int_{N}^{N+Y}\Bigl|\sum_{\gamma\lesssim T}A_\gamma e^{i\gamma\log x}\Bigr|^2dx\ \lesssim\ Y\cdot(\log T)^2\approx\sqrt N\log^2N\ ✗\ \ll\ hN=N^{3/2}\ ✗$$
$$\Longrightarrow\ \text{若成立 ⟹ }C_3\ \text{无条件成立 ⟹ Legendre 可证}\ ✗\ \textbf{与已知矛盾}\ ✗$$
```
⚠️ **而唐先生的转换是量纲精确的 ✓**：$Yh^2=\sqrt N\cdot N=N^{3/2}$ 与 $hN=\sqrt N\cdot N=N^{3/2}$ **恰相等** ✓
   ⟹ **故错的必须是我的【上界估计】✗，不是转换 ✓**
   ⭐ **最可信的原因 ✓**：**大筛在此【不适用】** —— 其有效条件是窗口长度 $\gtrsim$ 频率间隔 ✓
     而此处窗口在 $\log x$ 变量中长度 $=Y/N=1/T$ ✓，零点间隔 $\approx2\pi/\log T$ ✓
     $$\Longrightarrow\ \frac1T\cdot\frac{\log T}{2\pi}\ll1\ ✗\ \text{—— \textbf{窗口太短，频率根本未被分辨} ⟹ 可【完全相干】✓}$$
   $$\textbf{故真实值不是 }\sqrt N\log^2N\ ✗\ \text{而是【相干值】：}\ \approx Y\Bigl(\sum_{\gamma\lesssim T}|A_\gamma|\Bigr)^2=Y\Bigl(\frac{T\log T}{2\pi}\cdot\frac1T\Bigr)^2=\frac{Y\log^2T}{4\pi^2}=\sqrt N\log^2N\ ✗$$
   ⚠️⚠️ **矛盾仍在（相干值也只有 $\sqrt N\log^2N$ ✗，远低于 $N^{3/2}$）** ✗ ⟹ **我的量级簿记【确有系统性错误】✗，我未能定位 ✓**
   ⟹ **不声称任何 $o(hN)$ 或 $O(hN)$ 结论** ✓ —— **只声称 §0①②③④ 的【结构】✓**
```

## 2. 下一步的精确问题（✓ 按唐先生指定 ＋ 我的修正 ✓）

$$\boxed{\text{把二次型 }\mathscr C_T[f]=\sum f_T(\gamma)\overline{f_T(\gamma')}K_Y(\gamma-\gamma')\ \text{完全展开，问 positivity／majorant 能否给 }o(hN)}$$
```
【须先做的 ✓】**定位 §1 的簿记错误** ✗ —— 这是前提（否则一切估计都不可信 ✓）
   ⭐ 最可疑三点 ✓（按可能性排序）：
   ① **$\Delta$ 的显式公式【截断与权重】**：$\sum_\rho$ 需平滑截断 ✓，$1/\rho$ 与 $1/(\rho\rho')$ 的精确作用未核 ✗
   ② **自然高度**：我取 $T\sim N/h$ ✓ —— 但相关零点的高度上限是否真是 $T$ 而非更高 ✗（须核 ✓）
   ③ **$A_\gamma$ 的归一化**：$u=\log(1+h/x)$ vs $h/x$ 的差异 ✓（$u\approx h/N$ ✓ 但二阶项未核 ✓）
【之后再 ✓】若簿记修正后 majorant 仍给 $o(hN)$ ⟹ **真突破口** ✓；
   若给 $O(hN)$ ⟹ **精确定位哪一项达临界** ✓；若给 $>hN$ ⟹ **重核转换** ✓
```

## 3. 边界与纪律（✓）

```
✅ **$W_h$ 关闭已录取 ✓**；② **窗口不能平均相位** ✓（新点 ✓）；③ **要求的点态形式** ✓；④ **Gram 半正定 ⟹ positivity 给下界而给上界须用 majorant** ✓
⚠️ **§1 的簿记错误【未定位】✗** —— 我**三次**撞同一处 ✗ ⟹ **列为最高优先 ✓**
⚠️ **未用 RH** ✓；**未跑 Lean** ✓；**无计算** ✓
⭐ **本轮净产出 ✓**：① 关闭 $W_h$ ✓；② ⭐ **窗口不能平均相位（L² 路线不绕开点态墙 ✓）**；
   ③ 要求的点态形式 $|\Delta|=o(\sqrt N)$ ✓；④ **Gram 结构 ⟹ 上界须用 majorant（非 positivity 本身）** ✓；
   ⑤ 🔴 **公开并优先化簿记错误** ✓（这是"推到底"的前提 ✓）
```
