# RESULT-2026-09-30 — 闭合证书之\ \textbf{朴素提法被推翻} ✗✓：even-load 配置闭合**就是完全图**；真正的机制＝**超饱和（density↔triangle-count）** ✓

结论: 已查地图：未覆盖（关键词: 闭合证书|超饱和|诱导三角形）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/机制类（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 实验

| $r$ | $m$ | $v_{\rm hyp}$（超图贪心） | 闭合后 $m_G$ | 多出三角形 | 闭合后 $h_G$ |
|---|---|---|---|---|---|
| 8 | 20 | 36 | **56** | **+36** | 420 |
| 8 | 30 | 102 | **56** | +26 | 420 |
| 8 | 40 | 200 | **56** | +16 | 420 |
| 8 | 56 | 420 | 56 | +0 | 420 |
| 9 | 15 | 9 | **84** | **+69** | 756 |
| 9 | 40 | 144 | **84** | +44 | 756 |
| 9 | 84 | 756 | 84 | +0 | 756 |

## §1 读数

$$\boxed{m_G=\binom r3\ \text{恒成立}}\ \Longrightarrow\ \textbf{\text{even-load 超图最优之闭合＝完全图}}\ ✗\ (\text{最彻底的不可实现} ✓)$$

## §2 机制（本档核心 ✓✓）

$$\text{even-load}\ \Rightarrow\ \text{用边多}\ \Rightarrow\ \text{闭合后诱导三角形暴涨}\ \Rightarrow\ \begin{cases}\text{若 }m<m_{\max}:\ \text{不可实现} ✗\ \text{可实现者必\ \textbf{边稀疏}} \Rightarrow \text{载荷集中} \Rightarrow h\ \text{升高} ✓\end{cases}$$
$$\therefore\ \textbf{\text{支配约束＝边数与诱导三角形数的\ \textbf{超饱和关系}}}\ ✓\ \Longrightarrow\ \textbf{\text{这是 }}\Delta>0\ \textbf{\text{ 的机制性来源}}\ ✓✓\ (\text{可证 }\Phi\ \text{之新落点} ✓)$$

## §3 恒等式裁决（唐先生要求"写对"✓）

$$\text{随机图实测}:\ \sum_v\tau_v=\mathbf{3m}\ ✓✓\ (r{=}8,9,10,11\ \text{各 300 张，0 违背});\quad \textbf{\text{非 }}3h\ ✗$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{表为实测；机制为\ \textbf{待证命题}}\ ⚠️;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §5 【技术词回查】

```
技术词 超饱和      命中文件数=1
技术词 闭合证书    命中文件数=1
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{通用词（不计）}：\text{"闭合／证书"裸词} ✓$$
