# E136 · ⭐ **归一化审计（①）：截断/权重扫描 —— $R$ 不稳定 ⟹ ① FAIL** ✗

> 委托 ✓ 唐先生 2026-09-14（"把 $3T$ 换成归一化审计 ✓"）
> 执行 ✓ 小灵｜内存安全 ✓（峰值 203 MB ✓；chunked，无稠密 Gram ✓）｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓
> **依据** ✓ `scripts/E136_normalisation_audit.py`／`.txt`（`T=1000`、$N=10^6$、$Y=T$ ✓）

## 0. 数据（✓）

| 权重/截断 | $M$ | $Q$ | $\sum\lvert A\rvert^2$ | $R=Q/\sum\lvert A\rvert^2$ |
|:--|--:|--:|--:|--:|
| $\gamma\le T$ | 649 | $3.216\times10^{-4}$ | $6.282\times10^{-4}$ | **0.512** |
| $\gamma\le3T$ | 2469 | $1.451\times10^{-3}$ | $1.886\times10^{-3}$ | **0.769** |
| $\gamma\le10T$ | 10142 | $1.544\times10^{-3}$ | $2.490\times10^{-3}$ | **0.620** |
| flat ($w{=}1$, $\le10T$) | 10142 | $1.544\times10^{-3}$ | $2.490\times10^{-3}$ | 0.620 |
| $\exp(-(\gamma/T)^2)$ | 10142 | $4.223\times10^{-4}$ | $3.643\times10^{-4}$ | 1.159 |
| $(1-(\gamma/T)^2)_+^2$ | 10142 | $1.891\times10^{-4}$ | $2.110\times10^{-4}$ | 0.896 |

尾部对角（$\sum_{\gamma>G}\lvert A_\gamma\rvert^2$）：$\gamma>3T$：$8.575\times10^{-4}$ ✓；$>10T$：$2.542\times10^{-4}$ ✓；$>300T$：$8.775\times10^{-6}$ ✓

## 1. 判定（✓）

$$\textbf{① FAIL ✓}：R：0.512\to0.769\to0.620\ \textbf{不稳定} ✗\ \text{（非纯 }1/\gamma\ \text{权重效应 ✓）}$$
$$\Delta\sum\lvert A\rvert^2\ (T\to3T)=1.26\times10^{-3}\quad\text{vs}\quad\Delta Q=1.13\times10^{-3}\ \Longrightarrow\ \textbf{新零点几乎【原封不动】进入 }Q ✗$$
$$\text{尾部对角占 }Q_{3T}\ \text{的}\ 59.1\%\ \checkmark\ \Longrightarrow\ \textbf{尾部不可先验丢弃 ✓}\qquad\bigl(\gamma>10T\ \text{仅占 16.5\% ✓；}>300T\ \text{才 }8.8\times10^{-6}\ ✓\bigr)$$
$$\Longrightarrow\ \boxed{T\lesssim\gamma\lesssim3T\ \textbf{是危险/不可删的频率带 ✓}}\qquad\qquad\text{（升级版 E137 续档进一步给出【非单调】✓）}$$
