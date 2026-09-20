已查地图（**先查后写**）：查 `C-197`（局部引理 PROVED）、`C-196`（归约）、`C-194`（w=2 结构）。回查见 §4 ✓

D0: 本档对象 = **T13-B w=2 的远场 margin 探针**（探索性测量，为远场证书的尺度选择提供依据）—— 关系 = 定位／工程判断（非新机制）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 ⚠️ 口径声明（唐先生指定）

$$\textbf{本档只回答一个工程问题}：\text{远场是否存在}\ F-1\ \text{极小的窄脊／边界层？}✓$$
$$\qquad \Longrightarrow \text{决定远场走}\ \textbf{一尺度 Lipschitz}\ \text{还是}\ \textbf{两尺度／解析分区}✓$$
$$\qquad ⚠️\ \textbf{普通网格最小值【不是】}\ \mu_{\rm far}\ \text{的证书}✗\ —— \text{本档全部数据为探索性}✓$$

$$F(\delta_1,\delta_2)=\max_{1\le k\le10}S_k✓,\qquad S_k=2\cos(k\tfrac\pi3+k\delta_1)+\cos(k\tfrac\pi2+k\delta_2)✓$$
$$D_{\rm far}=[-\tfrac\pi3,\tfrac{2\pi}3]\times[-\tfrac\pi2,\tfrac\pi2]\setminus B_{0.1}(0)✓\ （\text{全域}，\text{含唐先生子盒}\ [-\tfrac\pi3,\tfrac\pi3]^2✓）$$

## §2 探针结果（$2000\times2000$ 网格；全域与子盒**同答案**✓）

$$\text{粗略}\ \min F=1.021360266812✓\qquad \text{粗略 margin}=+2.136027\times10^{-2}✓$$
$$\qquad \text{最危险点}\ (\delta_1,\delta_2)=(+0.057072267,\ +0.087964594)✓\ ⟹\varphi/\pi=(0.3515,\ 0.5280)✓$$
$$\qquad \text{到}\ r=0.1\ \text{边界距离}=4.857\times10^{-3}✓\qquad \text{该点 active}\ k=\{5\}✓$$

## §3 ⭐ SLSQP 精修（约束 $\delta_1^2+\delta_2^2\ge0.01$，允许落在圆边界）

$$\textbf{精修}\ \min F=1.019482100537✓\qquad \textbf{精修 margin}=\boxed{+1.948210\times10^{-2}}✓✓$$
$$\qquad (\delta_1,\delta_2)=(+0.054225143,\ +0.084021627)✓,\qquad |\delta|=0.100000000✓\ —\ \textbf{恰在圆边界上}✓✓$$
$$\qquad \text{到}\ r=0.1\ \text{距离}=+8.88\times10^{-16}✓\qquad \textbf{active}\ k=\{5,6\}✓$$
$$\Longrightarrow \text{全局远场最小值是}\ \textbf{边界层现象}✓（\text{发生在}\ \partial B_{0.1}✓）\ ——\ \text{但 margin}\approx0.0195\ \textbf{不是近似等号}✓✓$$

## §4 危险区面积占比（全域内，$F-1\le\varepsilon$）

| $\varepsilon$ | 面积占比 | 点数 |
|---|---|---|
| $10^{-1}$ | 0.1863% | 7,436 |
| $3\times10^{-2}$ | 0.0076% | 302 |
| $10^{-2}$ 及以下 | 0.0000% | 0（网格分辨不到） |

$$\Longrightarrow \text{危险区}\ \textbf{极小}✓✓ \Longrightarrow \text{自适应 B\&B 成本将非常低}✓$$

## §5 逐 $k$ 梯度模（最危险点；$L_k=k\sqrt{4\sin^2+\sin^2}\le k\sqrt5$）

$$\qquad k=5:\ |\nabla S_5|=8.361142✓\ (\text{active})✓\qquad k=6:\ |\nabla S_6|=4.807551✓\ (\text{active})✓$$
$$\qquad \text{全局上界}\ L\le10\sqrt5=22.360680✓\ \Longrightarrow \textbf{active 分区可把局部}\ L\ \text{降到}\ 8.36✓（2.7\times）✓$$

## §6 工程分叉判断

$$\text{全域粗网格}：\text{margin}=2.136\times10^{-2}\Longrightarrow h\approx9.55\times10^{-4}✓,\ \text{均匀侧长}\approx2.19\times10^{3}✓ \Longrightarrow \text{点数}\approx4.8\times10^{6}✓$$
$$\text{精修}：\text{margin}=1.948\times10^{-2}\Longrightarrow h\approx8.71\times10^{-4}✓,\ \text{均匀侧长}\approx2.40\times10^{3}✓ \Longrightarrow \text{点数}\approx5.8\times10^{6}✓$$
$$\qquad \text{若按 active 局部}\ L=8.36：h\approx2.33\times10^{-3}✓ \Longrightarrow \text{点数}\approx2.1\times10^{6}✓✓$$

$$\boxed{\ \text{margin}\ \approx1.95\times10^{-2}\ \ggg\ 10^{-4}\ \Longrightarrow\ \textbf{一尺度 Lipschitz 可行}✓✓\ }$$
$$\qquad \textbf{不需要两尺度}✓✗（\text{原估的}\ 10^{12}\ \text{级网格不会出现}✓）$$
$$\qquad \text{且因危险区仅}\ 0.008\%✓，\text{实际用}\ \textbf{自适应 B\&B}（\text{分离箱下界}）\ \text{成本远低于均匀网格}✓✓$$
$$\qquad \text{三种分叉的第三种（}\mu\approx0\ \text{＋新结构族}）\ \textbf{未出现}✗\ ——\ \text{远场无第二等号机制}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 远场 margin 探针   命中文件数=1    ::  ./C198-T13-B-w2-farfield-margin-probe-one-scale-viable.md
技术词 边界层现象         命中文件数=1    ::  ./C198-T13-B-w2-farfield-margin-probe-one-scale-viable.md
```
⚠️ **实测为 1 命中，且就是本档自身**（本次检查在落档【之后】执行 ⟹ 必然自命中）✓
⟹ **扣除自身后为 0 命中** ⟹ 判定：两项**均本档首次命名** ✓（依 `C-168` §6 惯例 ✓）

⚠️ **自查记录**：初稿 §7 直接写"命中文件数=0"✗ —— 与实测不符 ✗。**先跑后写**纪律第 5 次同类失误 ✓，已按实测改正 ✓。

## §8 边界

- **本档全部为探索性数值**✗（粗网格 ＋ SLSQP 局部精修）⟹ **不是** $\mu_{\rm far}$ 的证书 ✓
- SLSQP 出发自粗网格前 20 个危险点 ＋ 其圆边界投影 ✓；**未**保证穷尽所有局部极小 ✗
- 粗网格（间距 $\sim1.6\times10^{-3}$）给出 $1.02136$，精修给出 $1.01948$ ⟹ 网格**高估**最小值，与预期一致 ✓
- **未用** RH；**未改**他档 ✓
