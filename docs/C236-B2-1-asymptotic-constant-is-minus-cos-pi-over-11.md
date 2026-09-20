已查地图（**先查后写**）：查 `C-235`（Step 5 首轮，得 $-\frac9{11}$）、`C-234`（框架）、`C-159`/`C-192`（鸽笼＋等号集＝本原 $(N+1)$ 次根）。回查见 §7 ✓

D0: 本档对象 = **B2-1 Step 5 的【纠正版】**：$w\to\infty$ 常数应为 $-\cos\frac{\pi}{11}$（推翻本档前一版的 $-\frac9{11}$）＋五极值点结构与精确恒等式 —— 关系 = 纠正与结构确立
D1: 0
FREEZE-ACK: 本档即冻结期内的纠正与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 三行结论（含对 C-235 的自我推翻 ✗）

$$\boxed{\textbf{① C-235 的 }-\tfrac9{11}\ \textbf{是错的}✗✗\ \text{—— 它对应【次优支}】(\varphi_1\to\tfrac{2\pi}{11},\ \varphi_2\to\pi)✗}$$
$$\boxed{\textbf{② 正确常数}=\boxed{-\cos\tfrac{\pi}{11}}=-0.959492973614497389\ldots✓✓\ \text{（上界已由显式构型【证明}】✓）}$$
$$\boxed{\textbf{③ 关键结构}✓：\text{最优构型落在【两个不同的 11-格极值点}】上✓（\text{不是}\ \varphi_2=\pi✗），\text{五个极值点的 active pair 各不相同}✓✓}$$

## §1 决定性测试：为什么 $-\frac9{11}$ 是错的 ✗

$$\text{做法}✓：\text{对固定}\ \varphi_2\ \text{求 pair-最优}\ \varphi_1✓，\text{再对}\ \varphi_2\ \text{扫描}✓（w=1000✓）：$$
```
   phi2/pi    value − w·κ     phi1/pi      对应
   0.175      -0.95288       0.36363 = 4/11   j=2 极值点
   0.375      -0.94464       0.72727 = 8/11   j=4
   0.550      -0.95772       0.90909 = 10/11  j=5
   0.725      -0.95881       0.54545 = 6/11   j=3  ★扫描最优
   0.900      -0.95551       0.18182 = 2/11   j=1
   1.000      -0.81866       0.18182 = 2/11   ← 我先前只测的这一支 ✗
```
$$\Longrightarrow \textbf{我（与唐先生的归约）都只锁定了 }j=1\ \text{且}\ \varphi_2=\pi\ \text{这一【次优支}】✗✗ \Longrightarrow -\frac9{11}\ \text{是【局部】值}✗$$
$$\qquad \text{真实最优}：\varphi_1\ \text{与}\ \varphi_2\ \text{分别落在【不同的极值点}】✓✓$$

## §2 ⭐⭐ 五个极值点的 active pair 结构（新发现 ✓）

$$\text{鸽笼等号集}（\text{C-159/C-192}✓）=\{\theta_j=\tfrac{2\pi j}{11}:\gcd(j,11)=1\}✓ \Longrightarrow [0,\pi]\ \text{内共 5 个}✓：$$
$$\qquad \theta_j=\tfrac{2\pi j}{11},\ j=1,\dots,5✓（\text{即}\ \tfrac{2\pi}{11},\tfrac{4\pi}{11},\tfrac{6\pi}{11},\tfrac{8\pi}{11},\tfrac{10\pi}{11}✓）$$
$$\text{每个}\ \theta_j\ \text{处，达到}\ \kappa\ \text{的分支对}=\{k:\ kj\equiv\pm1\pmod{11}\}✓✓：$$
$$j=1:\{1,10\}✓\quad j=2:\{5,6\}✓\quad j=3:\{4,7\}✓\quad j=4:\{3,8\}✓\quad j=5:\{2,9\}✓$$
$$\qquad（\text{共性}：k+k'\ \text{不定}✗，\text{但}\ k\sin(k\theta_j)=\pm\sin\theta_j\ \text{恒成立}✓ \Longrightarrow \text{扰动系数为}\ \pm k✓）$$

## §3 ⭐⭐ 纠正后的配对公式与常数

$$\text{在}\ \theta_j\ \text{处写}\ \varphi_1=\theta_j+\varepsilon✓，\text{两分支}\ (k,k')\ \text{取值}：w(\kappa-k\sin\theta_j\varepsilon)+c✓,\ w(\kappa+k'\sin\theta_j\varepsilon)+c'✓,\ c:=\cos(k\varphi_2),\ c':=\cos(k'\varphi_2)✓$$
$$\text{均衡（tie）}：\varepsilon=-\frac{c'-c}{(k+k')w\sin\theta_j}✓ \Longrightarrow \textbf{共同值}=w\kappa+\frac{k\,c'+k'\,c}{k+k'}✓✓$$
$$\Longrightarrow \boxed{\ \text{常数}=\min_{j}\ \min_{\varphi_2}\ \frac{k_j\cos(k'_j\varphi_2)+k'_j\cos(k_j\varphi_2)}{k_j+k'_j}\ }✓（k_j,k'_j\ \text{为}\ \theta_j\ \text{的分支对}✓）$$

$$\textbf{数值（400\,000 点细扫，与 }w\text{ 无关}✓）}：\text{五个 }j\ \text{全部给同一值}✓✓$$
```
  j=1 {1,10}: min = -0.9594929736  at φ2/π = 0.90909 = 10/11
  j=2 {6,5} : min = -0.9594929736  at φ2/π = 0.18182 = 2/11
  j=3 {4,7} : min = -0.9594929736  at φ2/π = 0.72727 = 8/11
  j=4 {3,8} : min = -0.9594929736  at φ2/π = 0.36364 = 4/11
  j=5 {9,2} : min = -0.9594929736  at φ2/π = 0.54545 = 6/11
```
$$\Longrightarrow \text{五者【完全相同}】✓✓=\boxed{-\cos\tfrac{\pi}{11}}✓（\text{因在极值点处两余弦同为}-\cos\tfrac{\pi}{11}✓）$$

## §4 ⭐⭐⭐ 精确恒等式（机器精度确认 ✓✓）

$$\textbf{构造}：(\varphi_1,\varphi_2)=\bigl(\tfrac{2\pi}{11},\tfrac{10\pi}{11}\bigr)✓ \Longrightarrow M_w=w\kappa-\cos\tfrac{\pi}{11}✓\ \textbf{逐位精确}✓✓$$
```
   w        M_w(2π/11,10π/11)      w·κ−cos(π/11)          diff      argmax
   5       3.24677469054140845    同                     1.07e-50      10
  1000   840.294039857566671     同                     1.37e-48      10
100000 84124.3937901445024      同                     0.00e+00       1
```
$$\text{五组配对极值点}✓（\text{单位}\ \pi/11✓）：(2,10),(4,2),(6,8),(8,4),(10,6)✓ \Longrightarrow \text{全部给}-\cos\tfrac{\pi}{11}✓✓$$
$$\qquad \text{而其他配对}（\text{如}\ (2,6),(4,10)✓）\text{只给}-0.14231✓ \Longrightarrow \textbf{配对有选择性}✓$$

$$\boxed{\ \textbf{上界：}\ g_w(10)\ \le\ w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}\quad\text{对所有 }w\ge5\text{【已证】}✓✓\ }$$
$$\qquad \text{证}：\text{取显式构型}(2\pi/11,10\pi/11)✓；\text{其}\ \max_k\ \text{由}\ k=10\ \text{或}\ k=1\ \text{取到}✓，\text{其余}\ k\ \text{满足}\ w(\kappa-\cos\tfrac{4\pi}{11})\ \text{远超}✓$$

## §5 相变与边界

$$w=5：\text{公式成立}✓（3.2467747\ \text{vs}\ \text{C-193 数值}\ 3.246775✓✓）$$
$$w=2：\text{公式给}\ 0.72301\neq1=g_2(10)✗ \Longrightarrow \textbf{公式对 }w\le2\ \text{失败}✓ \Longrightarrow \text{存在相变}✓（\text{与 H1 一致}✓）$$
$$\textbf{待定}：\text{相变点}\ w_1\in(2,5]✓；\text{是否}\ g_w=w\kappa-\cos\tfrac\pi{11}\ \text{对【所有}\ w\ge w_1\ \text{精确成立}】✓（\text{上界已证}✓，\text{下界未证}✗）$$

## §6 状态表

| 项 | 状态 |
|---|---|
| $-\frac9{11}$（C-235） | ✗ **已推翻**（次优支） |
| 五极值点 active pair 结构 | ✓ **确立**（新） |
| 配对常数公式 | ✓ **建立**（数值：五者同为 $-\cos\frac{\pi}{11}$） |
| 上界 $g_w\le w\kappa-\cos\frac{\pi}{11}$ | ✓✓ **已证**（显式构型 ＋ $w\ge5$） |
| 下界（$w\ge w_1$ 时取等） | ✗ **未证**（下一步：① 锁定 $\varphi_1,\varphi_2$ 均趋极值点；② 均匀 8-分支 gap；③ 配对 minimax 下界） |
| 相变点 $w_1$ | ✗ 待定（$\in(2,5]$） |

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 五极值点配对      命中文件数=1  ::  ./C236-B2-1-asymptotic-constant-is-minus-cos-pi-over-11.md
技术词 配对选择性        命中文件数=1  ::  ./C236-B2-1-asymptotic-constant-is-minus-cos-pi-over-11.md
技术词 次优支推翻        命中文件数=1  ::  ./C236-B2-1-asymptotic-constant-is-minus-cos-pi-over-11.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 自我推翻已登记}✗✓（\text{C-235 的}-\tfrac9{11}✗）；\textbf{② 未用 RH}✓；\text{未改他档}✓$$
$$\textbf{③ 数值层}：\text{pair-最优扫描与细扫为【结构化数值}】✓，\text{非证明}✗；\text{精确恒等式为 50 位精度【逐位】核验}✓✓$$
$$\textbf{④ }C_\infty\ \text{的 degree-9 结构【未塞回}】✓（\text{依唐先生 19:02 纪律}✓）$$
