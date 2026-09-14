# E135 · 🔴 **(a) 的判定：连续密度模型【不给】 $\log^2T$ —— 它与实际 $Q$ 【同量级】** ✗

> 委托 ✓ 唐先生 2026-09-14 10:51（(a)→(b) 连着做 ✓；§11 的 $T$-依赖检查 ✓）
> 执行 ✓ 小灵｜**按协议先领号 ✓（E135 ✓ —— 工具仍误给别名 E123 ✗，已改 ✓）**｜内存安全 ✓（峰值 377 MB ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；⚠️ **本文与您的预测不符 ✗，如实报 ✓**

---

## 0. 结论（✓ 四条，前三条与您的预测相反 ✗）

```
🔴 **① 密度模型【不给】$\asymp\log^2T$ ✗** —— 它反而【下降】✓
   | $T$ | $M$ | $Q_{\rm actual}$ | $Q_{\rm density}$ | $Q_{\rm act}/\sum\lvert A\rvert^2$ | $\log^2T$ | $Q_{\rm dens}/Q_{\rm act}$ |
   |--:|--:|--:|--:|--:|--:|--:|
   | 100 | 138 | $1.932\times10^{-2}$ | $2.543\times10^{-3}$ | 1.885 | 21.2 | **0.132** |
   | 316 | 607 | $3.072\times10^{-3}$ | $6.293\times10^{-3}$ | 0.668 | 33.1 | **2.05** |
   | 1000 | 2469 | $1.347\times10^{-3}$ | $2.160\times10^{-4}$ | 0.714 | 47.7 | **0.16** |
   $$\textbf{拟合 ✓}：\frac{d\log Q_{\rm density}}{d\log T}=\mathbf{-1.0714}\ ✗\qquad\frac{d\log Q_{\rm actual}}{d\log T}=\mathbf{-1.1566}\ ✓$$
   $$\Longrightarrow\ Q_{\rm density}\sim T^{-1.07}\ ✗\ \textbf{而非}\ \log^2T\ ✗\ \text{—— 密度模型本身就给【小】}Q\ ✓$$
🔴 **② 密度模型与实际 $Q$【同量级】✓（0.13／2.05／0.16 倍 ✗）** ⟹ **E130 的小 $Q$ 【不是】离散相消的奇迹** ✗
   $$\text{平滑密度替代序列已给出同样的量级 ✓ ⟹ 无需离散涨落的主项级抵消 ✗（与您 §3／§10 判断相反 ✓）}$$
🔴 **③ 您的 §9 重构【不成立】✗**：$Q/(\mathbf A^*\mathbf A)=0.67$–$1.89$ ✓ ⟹ **$\mathbf A$ 【不是】$G$ 的低能量向量** ✗
   $$\text{即 }\frac{\mathbf A^*G\mathbf A}{\mathbf A^*\mathbf A}\ \text{并不}\ \ll1\ ✗\ \Longrightarrow\ \textbf{$Q$ 的小来自【权重本身小】✓（}Q\approx0.7\sum|A_\gamma|^2\ ✓\text{）}$$
⭐⭐ **④ 由此暴露一个【必须解决的矛盾】✗（最重要 ✓）**：
   $$\text{若 }Q=o(1)\ \text{成立 ✓（实测 }Q\sim T^{-1.16}\to0\ ✓），\text{则要求}\ \int_N^{N+Y}\Delta^2=o(hN)\ \text{成立}$$
   $$\Longrightarrow\ \text{按 Bazzanella 转换 ⟹ 无反例 ⟹ }\textbf{Legendre 可证}\ ✗✗\ \text{—— 而它是开放问题 ✗}$$
   $$\Longrightarrow\ \boxed{\textbf{故我的化约或归一化【必有错】✗ —— 最可能是【零点和的锐截断】✓（正是您 §8 的怀疑 ✓）}}$$
```

## 1. $T$-依赖（✓ 您 §11 要求的检查 ✓）

$$Q_{\rm actual}(T)：1.932\times10^{-2}\ (T{=}100)\ \to\ 3.072\times10^{-3}\ (T{=}316)\ \to\ 1.347\times10^{-3}\ (T{=}1000)$$
$$\textbf{单调下降 ✓（指数 }-1.157\ ✓）\ \Longrightarrow\ \textbf{不是小-}T\ \text{偶然 ✓ —— }Q(T)\to0\ ✓\ \text{（若化约正确 ✓）}$$

## 2. 为什么 $Q$ 小（✓ 机制 ✓）

$$\sum_\gamma|A_\gamma|^2\approx\underbrace{M_{\rm head}u^2}_{\approx\frac{T\log T}{2\pi}\cdot\frac1{T^2}}+\underbrace{\sum_{\gamma>T}\frac1{\gamma^2}}_{\approx\frac{\log T}{2\pi T}}\approx\frac{\log T}{\pi T}\ \xrightarrow{\ T=1000\ }\ 2.2\times10^{-3}\ ✓$$
$$\text{实测 }\sum|A_\gamma|^2=Q/0.714=1.89\times10^{-3}\ ✓\ \text{（吻合 ✓）}\ \Longrightarrow\ \textbf{小来自【权重衰减】✓（}\sum|A|^2\ \text{收敛 ✓）}$$
$$\text{而密度模型给出同一量级的对角项 ✓ ⟹ 密度模型【已经】产生小 }Q\ ✓\ \text{—— 无需离散修正 ✓}$$

## 3. 待解矛盾与下一步（✓ 不含结论 ✓）

```
⚠️ **矛盾 ✓**：本计算链条（$\Delta\approx\sqrt x\,F$ ⟹ $\int|\Delta|^2=N Y Q$ ⟹ 要求 $\iff Q=o(1)$ ✓）
   推出 **Legendre 可证** ✗ —— **不可能 ✓** ⟹ 化约必有错 ✓
⭐ **最可疑处（按可能性 ✓）**：
   ① **锐截断** ✗：我用 $\gamma\le3T$ ✓，而显式公式需【平滑截断】✓；尾部 $\gamma>3T$ 的逐项贡献 $\approx2\sqrt x/\gamma$ ✓
      —— 虽在窗口内被平均 ✓，但**点态 $\Delta$ 的尾部约为 $\sqrt x\log(x/G_0)$** ✗ ⟹ **我的 $F$ 只含头部 ✗**
   ② **$A_\gamma$ 的精确形式** ✗：E130 用的是 $A=(e^{u\rho}-1)/\rho$ ✓ —— 是否等于显式公式的真正测试函数 ✗（须逐项对齐 ✓）
   ③ **$h$ 与 $Y$ 的关系** ✗：Bazzanella 的 $h(x)=2\sqrt x+1$ **随 $x$ 变** ✓，而我固定 $h=Y=\sqrt N$ ✓
   ④ **"反例 ⟹ 窗口异常"的量** ✗：单点反例只给测度零 ✗；须靠"区间无素数 ⟹ 附近 $\Delta\approx-h$"✓ —— 这一步**未严格核** ✗
```

## 4. 边界与纪律（✓）

```
🔴 **① 本文与您的预测（$Q_{\rm dens}\asymp\log^2T$）不符 ✗** —— 实测是【下降】✓；我如实报 ✓，**不为迎合而改数** ✓
✅ **② 按协议操作 ✓**（先领号 ✓）；⚠️ **工具 bug 再次复现 ✗**：`id_claim.sh main` 二次给出别名 E123 ✗ ⟹ 已改 E135 ✓
⚠️ **③ $M\le3000$（Gram 上限 ✓）**；$G=3T$ 截断 ✗（须按 §3① 复核 ✓）；$T$ 只测 3 点 ✓
⚠️ **④ "密度替代序列"用平滑计数反函数 ✓（rigid ✓）** —— 也可以改用随机替代 ✓（下一轮可补 ✓）
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **判定 (a)：密度模型不给 $\log^2T$ ✗**；② **$Q_{\rm dens}$ 与 $Q_{\rm actual}$ 同量级 ✓**；
   ③ **$\mathbf A$ 非低能量向量 ✗**；④ ⭐ **暴露"化约→Legendre 可证"的矛盾 ✗ 并列出四处可疑点 ✓**
