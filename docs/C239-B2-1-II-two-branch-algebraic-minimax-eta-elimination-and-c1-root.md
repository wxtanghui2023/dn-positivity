已查地图（**先查后写**）：查 `C-238`（两补丁＋精确上界＋$c_1$ 预判）、`C-237`（下界三 lemma）、`C-236`（上界）。回查见 §7 ✓

D0: 本档对象 = **B2-1-II：精确 two-branch algebraic minimax**（II-a $\eta$ 消去、II-b 精确 tie、II-c 全局下界判定）—— 关系 = 推进＋诚实否定
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论（含两项否定 ✓）

$$\boxed{\textbf{II-a}✓✓：\text{tie 方程在}\ (\varepsilon,\eta)=(0,0)\ \textbf{处【恒等满足}】✓✓\ \text{—— 代数根源}：\sin(\pi j)=\sin(\pi m)=0✓}$$
$$\boxed{\textbf{II-b}✓✓：\eta=0\ \text{时除}\ \varepsilon=0\ \text{外，tie 的最近解距离}\ \ge0.127✓ \Longrightarrow \varepsilon=0\ \text{局部【唯一}】✓（\text{精确}✓）}$$
$$\boxed{\textbf{II-c}✓✓（数值强证据）：\text{局部 minimax 精确}=w\kappa-c_0✓，\text{极小点}\ (\varepsilon,\eta)=(0,0)✓，\text{五 pair}\times w\in\{10^2,10^3,10^4\}\ \text{【全部}】✓✓}$$
$$\boxed{\textbf{否定 1}✗：c_{1,j}\equiv0\ \text{不是"二阶相消"，而是【无渐近修正}】✓\ \text{—— 支持 exact finite-}w\ \text{extremizer}✓}$$
$$\boxed{\textbf{否定 2}✗✗：一条"漂亮"路线被排除}\ \max_jH_j(\varphi_1)\ge\kappa\ \text{为【假}】✗（\varphi_1=\tfrac\pi2\ \text{时仅}\ \tfrac7{11}✓）$$

## §1 II-a：tie 方程的恒等满足（关键代数判定 ✓✓）

$$\text{两 active branches}：A=w\cos(a\varphi_1)+\cos(a\varphi_2)✓,\quad B=w\cos(b\varphi_1)+\cos(b\varphi_2)✓,\quad a+b=11✓$$
$$\text{tie}\ A=B \Longleftrightarrow w\bigl[\cos a\varphi_1-\cos b\varphi_1\bigr]=\cos b\varphi_2-\cos a\varphi_2✓$$
$$\text{用}\ \cos X-\cos Y=-2\sin\tfrac{X+Y}2\sin\tfrac{X-Y}2✓：$$
$$\qquad \cos a\varphi_1-\cos b\varphi_1=-2\sin\tfrac{11\varphi_1}2\sin\tfrac{(a-b)\varphi_1}2✓,\qquad \cos b\varphi_2-\cos a\varphi_2=+2\sin\tfrac{11\varphi_2}2\sin\tfrac{(a-b)\varphi_2}2✓$$
$$\textbf{在}\ \varphi_1=\theta_j=\tfrac{2\pi j}{11}✓：\sin\tfrac{11\theta_j}2=\sin(\pi j)=0✓✓ \qquad \textbf{在}\ \varphi_2=y_0=\tfrac{2\pi m}{11}✓：\sin\tfrac{11y_0}2=\sin(\pi m)=0✓✓$$
$$\Longrightarrow \boxed{\text{tie 在}\ (\varepsilon,\eta)=(0,0)\ \text{两端【同时为零}】✓✓ \Longrightarrow \text{恒等满足}✓✓}$$
$$\qquad \textbf{这解释了 }c_1=0\ \text{的代数根源}✓：\text{不是 }1/w\ \text{系数的偶然相消}✓，\text{而是组合构型本身就是【精确 extremizer}】✓$$

## §2 II-b：$\eta=0$ 时的精确 tie 解集（$\varepsilon=0$ 局部唯一 ✓）

$$\eta=0\ \text{时 tie 退化为}\ \cos(a(\theta+\varepsilon))=\cos(b(\theta+\varepsilon)) \Longleftrightarrow \sin\tfrac{11(\theta+\varepsilon)}2\sin\tfrac{(a-b)(\theta+\varepsilon)}2=0✓$$
$$\text{解}(1)✓：\tfrac{11(\theta+\varepsilon)}2=\pi l \Longrightarrow \varepsilon=\tfrac{2\pi(l-j)}{11}✓（\text{11-格}✓）$$
$$\text{解}(2)✓：\tfrac{(a-b)(\theta+\varepsilon)}2=\pi l'\Longrightarrow \varepsilon=\tfrac{2\pi l'}{a-b}-\tfrac{2\pi j}{11}✓$$
$$\text{最近非零解距离}✓（\text{全部}\gg O(1/w)\ \text{局部窗口}✓）：$$
```
   j=1 (1,10]: 解(1) 0.5712  解(2) 0.1270        j=4 (3,8): 解(1) 0.5712  解(2) 0.2285
   j=2 (5,6) : 解(1) 0.5712  解(2) 1.1424        j=5 (2,9): 解(1) 0.5712  解(2) 0.1632
   j=3 (4,7) : 解(1) 0.5712  解(2) 0.3808
```
$$\Longrightarrow \boxed{\varepsilon=0\ \text{在局部【唯一解】}✓✓ \Longrightarrow \text{不存在}\ \varepsilon=\tfrac{\alpha}{w}+\cdots\ \text{型位移}✓✓ \Longrightarrow \text{即}\ \varepsilon_*(w)\equiv0✓}$$

## §3 II-c：精确恒等式的强证据（数值 ✓✓）

$$M_w(\theta_j,y_0)\ \text{vs}\ w\kappa-c_0✓（\text{50 位精度}✓）：w=5,10,100,1000,10^4\ \text{【全部逐位相等】}✓✓\ （\text{差}\sim10^{-47}✓）$$
```
  局部二维极小化 max(A,B)（五 pair）：
    w=100  : 全部 min = 83.165860309504 = wκ-c0，极小点 (ε,η)=(0,0) ✓
    w=1000 : 全部 min = 840.294039857567 = wκ-c0，极小点 (ε,η)=(0,0) ✓
    w=10000: 全部 min = 8411.575835338199 = wκ-c0，极小点 (ε,η)=(0,0) ✓
    （差 = 0 或浮点噪声 ~1e-12 ✓）
```
$$\Longrightarrow \textbf{强证据}✓✓：\text{局部 two-branch minimax 精确}=w\kappa-c_0✓，\textbf{无 }1/w\ \text{修正}✓✓$$
$$\text{全域粗查}✓（w=200✓，网格 4000^2✓）：\text{最小}\ 167.293269\ >\ w\kappa-c_0=167.291214✓（\text{高}+2.06\times10^{-3}✓，\text{即网格分辨率误差}✓）$$

## §4 ⭐ 新的有限化归约（本档建立 ✓）

$$\text{对任意两条分支}\ (a,b)✓，\max(A,B)\ge\tfrac{bA+aB}{a+b}✓ \Longrightarrow \text{对五个 }j\ \text{各得一条}✓：$$
$$\boxed{\ M_w\ \ge\ \max_{j=1,\dots,5}\bigl[w\,H_j(\varphi_1)+H_j(\varphi_2)\bigr]✓✓\ }\qquad H_j(y):=\frac{b_j\cos(a_jy)+a_j\cos(b_jy)}{11}✓$$
$$\qquad（\text{有限集}✓：\text{五个显式三角泛函}✓；\text{且同一下标 }j\ \text{同时出现在两项}✓ \Longrightarrow \text{耦合}✓）$$

## §5 ⚠️ 诚实否定：一条漂亮路线被排除 ✗✗

$$\text{若单取一个 }j\ \text{并配 Lemma 3}\ (H_j\ge-c_0✓) \Longrightarrow M_w\ \ge\ w\max_jH_j(\varphi_1)-c_0✓$$
$$\qquad \text{则只需}\ \boxed{\max_jH_j(\varphi_1)\ \ge\ \kappa}\ \text{—— 但这是【假的}】✗✗：$$
$$\qquad \varphi_1=\tfrac\pi2✓：H_1=\tfrac{-1}{11}✓,\ H_2=\tfrac{-5}{11}✓,\ H_3=\tfrac{7}{11}=0.6364✓,\ H_4=\tfrac3{11}✓,\ H_5=\tfrac{-9}{11}✓ \Longrightarrow \max_jH_j=\tfrac7{11}=0.6364<\kappa=0.8413✗$$
$$\Longrightarrow \textbf{该单-}j\ \text{路线只能给}\ w\cdot0.636-c_0✗（\text{远弱}✓） \Longrightarrow \text{必须使用 §4 的【耦合 max}】✓✓$$
$$\qquad \text{注}✗：\text{失败原因}＝\text{两个坐标项不能同时达到各自最小}✓（\varphi_1\ \text{与}\ \varphi_2\ \text{共用同一 }j✓）✓$$

## §6 状态与下一步

| 项 | 状态 |
|---|---|
| II-a（tie 恒等满足） | ✓✓ 完成（$\sin\pi j=\sin\pi m=0$） |
| II-b（$\varepsilon=0$ 局部唯一） | ✓✓ 完成（最近非零解 $\ge0.127$） |
| II-c 局部 minimax | ✓✓ 数值：精确 $=w\kappa-c_0$，极小点 $(0,0)$ |
| 精确上界（$w\ge5$） | ✓✓ 已证（C-238 初等） |
| 有限化归约 | ✓✓ 建立（五个耦合泛函的 max） |
| **全局下界 $M_w\ge w\kappa-c_0$** | ✗ **未证**（单-$j$ 路线已排除；须用耦合 max） |
| **exact identity** $g_w=w\kappa-c_0\ (w\ge5)$ | ⬜ 未证，但证据强 |

$$\textbf{C-239 核心读数}✓：\text{把"数值上 }c_1=0✗"\ \text{升级为【代数结构性事实}】✓✓：\text{tie 在构型处恒等满足}✓ \Longrightarrow \text{不存在渐近修正}✓ \Longrightarrow \text{问题已从"求 }1/w\ \text{系数"\ 变成【证明 exact 全局下界}】✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 恒等满足型tie      命中文件数=1  ::  ./C239-B2-1-II-two-branch-algebraic-minimax-eta-elimination-and-c1-root.md
技术词 精确极值构型       命中文件数=1  ::  ./C239-B2-1-II-two-branch-algebraic-minimax-eta-elimination-and-c1-root.md
技术词 耦合max归约        命中文件数=1  ::  ./C239-B2-1-II-two-branch-algebraic-minimax-eta-elimination-and-c1-root.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；C_\infty\ \text{的 degree-9 结构未塞回}✓；\textbf{② }c_{1,j}\ \text{的"全零"现已是【代数结论}】✓（\text{§1}✓），\text{非数值}✓$$
$$\textbf{③ 未证}✗：\text{全局下界}✓（\text{§4 的耦合 max 估计}✓）；\text{一般 }M／\text{一般窗 }N✗；\text{相变点 }w_1✗$$
$$\textbf{④ 数值层}：\text{§3 为浮点/50 位核验}✓，\text{已排除}\ (>w\kappa-c_0)\ \text{的构型}✓，\text{非证明}✗$$
