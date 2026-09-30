# RESULT-2026-09-30 — $\tau_v$ 恒等式族**逐项核验**：四项全零 ✓✓；并**自查出我方因子 2 错误** ✗

结论: 已查地图：命中 256 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 方法/核验类（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 **核验结果（随机图，{=}8,9,10,11$ 各 300 张 ✓）**

$$\text{四项违背计数}: r{=}8,9,10,11\ \text{皆}\ \mathbf{0} ✓✓$$

| # | 恒等式 | 状态 |
|---|---|---|
| (i) | $\tau_v=\lvert E(N(v))\rvert$（$ 处三角形数＝其邻域图之边数） | ✓（构造性双射） |
| (ii) | $\sum_v\tau_v=3m$ | ✓ 核验全零 |
| (iii) | $\tau_v\le\binom{d_v}2$ | ✓ 核验全零 |
| (iv) | =\sum_{vw\in E}\binom{\lvert N(v)\cap N(w)\rvert}2$（对**无序**边求和） | ✓ 核验全零 |

## §1 **自查出的错（我方 ✗）**

$$\text{前档}\ \texttt{DIAGNOSIS-2026-09-30}\ \S3\ \text{写" }2h=\sum_{vw\in E}\binom{\lvert N(v)\cap N(w)\rvert}2\text{"\ \textbf{多了因子 }2} ✗$$
$$\text{正确}: t_{vw}=\lvert N(v)\cap N(w)\rvert\ ✓\ (\text{边 }vw\ \text{上三角形数＝公共邻点数})\ \Longrightarrow\ h=\sum_{vw\in E}\binom{t_{vw}}2\ \text{对无序边一次} ✓$$

## §2 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{随机图 300×4 核验} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §3 【技术词回查】

```
技术词 邻域图边数 命中文件数=0
技术词 tau_v核验  命中文件数=0
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词 0 命中 ⟹ 新} ✓;\ \textbf{通用词（不计）}：\text{"核验／恒等式"裸词} ✓$$
