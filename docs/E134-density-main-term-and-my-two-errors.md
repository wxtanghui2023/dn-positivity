# E134 · 🔴🔴 **决定性：$A_\gamma$ **未正确中心化** —— 密度主项 ≈ $C\log T$ ＋ 推翻我 E130 的两处推理** ✗

> 委托 ✓ 唐先生 2026-09-14 10:47（"$S_{\rm dens}(T)$ 的精确渐近 ＋ 与 E130 实际 $A_\gamma$ 逐项对齐" ✓）
> 执行 ✓ 小灵｜**按协议先领号 ✓（E134 ✓）**｜内存安全 ✓（峰值 141 MB ✓）
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；⚠️ **本文推翻我自己 E130 §2 与 §④** ✗

---

## 0. 结论（✓ 四条，前两条是我的错 ✗）

```
🔴 **① 我的 E130 §2 【错】✗**：**$v_{\max}\neq\frac1{\sqrt M}\mathbf 1$** ⟹ **$Q\neq|\sum A_\gamma|^2$** ✗
   $$Q=\mathbf A^*G\mathbf A=\mathbf{4.655\times10^{-4}}\ ✗\qquad\Bigl|\sum_\gamma A_\gamma\Bigr|^2=\mathbf{4.002\times10^{-1}}\ ✗\qquad\textbf{相差}\ \mathbf{860}\ \text{倍}$$
   $$\text{若 }v_{\max}=\tfrac1{\sqrt M}\mathbf 1\ \text{则应有}\ |\langle \mathbf A,v_{\max}\rangle|^2=|\sum A|^2/M=6.17\times10^{-4}\ ✗\ \text{而实测 }7.19\times10^{-7}\ ✗\ \Longrightarrow\ \textbf{1}\perp v_{\max}\ ✗$$
   $$\Longrightarrow\ \textbf{Gram 的近秩一【不等于】常向量 ⟹ 其顶本征向量是某个【振荡型】向量 ✗}$$
🔴 **② 我的 E130 §④ 【错】✗**：$|S|\sim\sqrt M\,u$ **默认了"相位随机"** ✗ —— **而那正是必须证明的东西** ✗（唐先生指出 ✓）
   $$\text{实测 ✓}：|S_{\rm direct}|(G=T)=\mathbf{0.6326}\ ✗\qquad\sqrt M u=\mathbf{0.0255}\ \bigl(\textbf{差 25 倍 ✗}\bigr)\qquad\frac{\log T}{2\pi}=\mathbf{1.0994}\ ✓$$
★★★ **③ 密度主项【确实存在】✓ —— 且【定量吻合 ✓✓】（唐先生预测 ✓）**
   $$C=\frac1{2\pi}\int_0^1\frac{e^{iv}-1}{iv}dv=\mathbf{0.150574}\neq0\ ✓✓$$
   $$S_{\rm dens}(T)\ \text{（带 }\log(\gamma/2\pi)\ \text{权 ✓）}=\mathbf{0.607657}\ \Longleftarrow\ \textbf{与实测 }|S_{\rm direct}|=\mathbf{0.632644}\ \textbf{吻合到 4\%}\ ✓✓✓$$
   $$\Longrightarrow\ \textbf{判据属于唐先生的【情形 C ✗】：}A_\gamma\ \textbf{未正确中心化} ✓\ \text{—— 主项}\asymp C'\log T\ ✗$$
⭐ **④ 但要求的对象【不是】纯和 $S$，而是【窗口平均】$Q$ ✓（须分清 ✓）**
   $$\text{要求 ✓}：\int_N^{N+Y}\Delta^2=o(hN)\ ⟺\ Q=\mathbf A^*G\mathbf A=o(1)\ ✓\qquad Q=\mathbf{4.655\times10^{-4}}\ ⟹\ \textbf{余量 2148× ✓}$$
   $$\Longrightarrow\ \textbf{窗口平均【确实小】✓ —— 而纯和【不小】✗ ⟹ 二者的差【正是窗口相消】✓＝所缺输入 ✓✓}$$
```

## 1. 数值（✓ 可复跑 ✓）

| $G$ | $n$ 零点 | $\lvert S_{\rm direct}\rvert$ | $\lvert S\rvert^2$ | $\sqrt Mu$ | $\frac{\log T}{2\pi}$ |
|--:|--:|--:|--:|--:|--:|
| $T$ | 649 | **0.6326** | 0.4002 | 0.0255 ✗ | 1.0994 ✓ |
| $2T$ | 1517 | 1.3712 | 1.8803 | 0.0389 ✗ | 1.0994 |
| $5T$ | 4520 | 2.4700 | 6.1008 | 0.0672 ✗ | 1.0994 |
| $10T$ | 10142 | 3.0925 | 9.5637 | 0.1007 ✗ | 1.0994 |
| $100T$ | 138069 | 6.0203 | 36.244 | 0.3714 ✗ | 1.0994 |
| 数据上限 | 2001052 | **10.175** | 103.53 | 1.4139 | 1.0994 |

$$\Longrightarrow\ \textbf{纯和随 }G\ \text{增长（10}^4\to10^5\ \text{翻倍 ✓）⟹ 非 }o(1)\ ✗\ \text{—— 与密度模型一致 ✓}$$

## 2. 密度模型（✓ 逐项 ✓）

$$S_{\rm dens}(T)=\frac1{2\pi}\int_{u}^{1}\frac{e^{iv}-1}{iv}\log\frac{v}{2\pi u}\,dv$$
$$C=\frac1{2\pi}\int_0^1\frac{e^{iv}-1}{iv}dv=0.150574\neq0\ ✓\Longrightarrow\ \text{主项}\ \asymp C\log T\ ✗\ \bigl(\text{naive }C\log T=1.0401\ ✓\bigr)$$
$$\textbf{而带权的精确值 }0.6077\ \textbf{与实测 }0.6326\ \textbf{吻合 4\%}\ ✓✓\ \Longrightarrow\ \textbf{密度模型【正确描述纯和】✓}$$

## 3. 因此本线的**准确状态**（✓ 诚实 ✓）

```
✅ **① 要求的对象 ＝ 窗口平均 $Q=\mathbf A^*GA$ ✓**（不是纯和 ✗）—— $Q=4.66\times10^{-4}=o(1)$ ✓（$N=10^6$ ✓）
⭐ **② 但 $Q$ 小的【原因】不是"$|\sum A_\gamma|$ 小" ✗**（纯和其实不小 ✓ 含 $C\log T$ 主项 ✗）
   ⟹ $Q$ 小来自**【窗口内相消】✓** —— 即 $F(x)=\sum A_\gamma e^{i\gamma\log x}$ 在窗口上被平均掉 ✓
   $$\Longrightarrow\ \textbf{所缺输入【正确定位】：窗口级相消（不是纯和的相消 ✓）}$$
⚠️ **③ 我此前所谓"判据 ⟺$|\sum A_\gamma|=o(1)$"【错】✗** —— 正确判据是 $Q=\mathbf A^*GA=o(1)$ ✓（$Q$ 与纯和无此关系 ✗）
⚠️ **④ $v_{\max}$ 不是常向量 ✗** —— 故"近秩一 ⟹ 常向量"的直觉【不可用】✗（E129 的 $\lambda_{\max}\approx M$ 仍成立 ✓）
⭐ **⑤ 修正后，E130 的【数值结论】仍成立 ✓**（$Q=o(1)$ ✓ 余量 2148× ✓）；**但其【推理】已更正 ✓**
```

## 4. 边界与纪律（✓）

```
🔴 **本轮为【自我更正】✗**：E130 §2 与 §④ 皆错 ✓，已逐字更正 ✓
✅ **按协议操作 ✓**：先领号（E134 ✓）—— ⚠️ **并发现他们会话工具 bug ✗**：`id_claim.sh main` **误分配 E123** ✗
   （E123 已是台账 legacy-alias ✓，但工具**不把台账别名视为占用** ✗）⟹ **已撤销误领 ✓（删锁 ＋ 删行 ✓）**，
   并**上报他会话** ✓（建议：占用判定须加"台账内任何行"一条 ✓）
⚠️ **$N=10^6$ 单一尺度 ✓**；$M$ 上限 3000 ✓（Gram 部分 ✓；直接求和用全部 2e6 零点 ✓）
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **密度主项存在且定量吻合（0.6077 vs 0.6326 ✓）⟹ 情形 C ✓**；
   ② **推翻我 E130 两处推理 ✓**；③ **判据的正确形式（$Q=o(1)$ ✓）与所缺输入的准确定位（窗口级相消 ✓）**；
   ④ **发现并撤销一次工具误领 ✓，并上报工具 bug ✓**
