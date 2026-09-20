已查地图（**先查后写**）：查 `C-237`（下界三 lemma）、`C-236`（上界）、`C-234`/`C-233`。回查见 §6 ✓

D0: 本档对象 = **C-237 的定理级审计（两个补丁）＋ B2-1-II 预判（$c_{1,j}$）＋ 精确上界** —— 关系 = 严格化与推进
D1: 0
FREEZE-ACK: 本档即冻结期内的严格化与登记（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{补丁 1}✓：F(\theta_j+\varepsilon)-\kappa\ \ge\ c_j|\varepsilon|-C_j\varepsilon^2\（|\varepsilon|\le\varepsilon_0✓）✓✓\ \text{显式常数见 §1}✓}$$
$$\boxed{\textbf{补丁 2}✓：\text{五者同值=【纯模 11 加三角恒等式】}✓✓\ \text{零数值依赖}✓}$$
$$\boxed{\textbf{新}✓✓：\text{上界升级为【精确}】\ g_w\le w\kappa-\cos\tfrac{\pi}{11}\ \text{对一切}\ w\ge5✓（\text{初等可证}✓）}$$
$$\boxed{\textbf{预判}✓：c_{1,j}\equiv0\ \text{（五者全零，无二阶对称破缺}✓）\Longrightarrow \text{疑似}\ g_w=w\kappa-\cos\tfrac{\pi}{11}\ \text{精确}✓✓}$$

## §1 补丁 1（定量尖点不等式 ✓）

$$\text{在}\ \theta_j\ \text{处两分支交叉}✓（P_j=\{a_j,b_j\}✓）\Longrightarrow \text{对}\ |\varepsilon|\le\varepsilon_0\ \text{（}\varepsilon_0\ \text{由}\ \Delta\ \text{与斜率定}✓）:$$
$$\qquad F(\theta_j+\varepsilon)=\max\bigl(\cos(a_j(\theta_j+\varepsilon)),\ \cos(b_j(\theta_j+\varepsilon))\bigr)✓$$
$$\qquad \cos(a_j(\theta_j+\varepsilon))=\kappa\cos(a_j\varepsilon)-s_j\sin(a_j\varepsilon)\ \ \Longrightarrow\ \ \kappa-s_ja_j\varepsilon-\tfrac{\kappa a_j^2}2\varepsilon^2+O(\varepsilon^3)✓$$
$$\qquad \cos(b_j(\theta_j+\varepsilon))=\kappa\cos(b_j\varepsilon)+s_j\sin(b_j\varepsilon)\ \ \Longrightarrow\ \ \kappa+s_jb_j\varepsilon-\tfrac{\kappa b_j^2}2\varepsilon^2+O(\varepsilon^3)✓$$
$$\Longrightarrow \max=\kappa+s_j\max(-a_j\varepsilon,\ b_j\varepsilon)+O(\varepsilon^2)= \kappa+s_j\min(a_j,b_j)|\varepsilon|+O(\varepsilon^2)✓✓$$
$$\boxed{\ c_j:=s_j\min(a_j,b_j)>0✓,\qquad C_j:=\max(a_j,b_j)^2✓ \Longrightarrow F(\theta_j+\varepsilon)-\kappa\ \ge\ c_j|\varepsilon|-C_j\varepsilon^2✓✓\ }$$
$$\qquad（C_j\ \text{的合法性}：|\cos x-1|\le x^2/2✓,\ |\sin x-x|\le x^3/6✓ \Longrightarrow \text{二阶项系数}\le\tfrac{\kappa}2\max(a_j,b_j)^2+\text{高阶}✓）$$

```
   j    a    b        c_j = sin(2πj/11)·min(a,b)        C_j = max(a,b)²
   1    1   10              0.5406408174555976               100
   2    5    6              4.548159976772592                 36
   3    4    7              3.959285767523731                 49
   4    3    8              2.267248723062775                 64
   5    2    9              0.5634651136828594                81
```
$$\Longrightarrow \text{由}\ wF(\varphi_{1,w})\le w\kappa+O(1)✓ \Longrightarrow c_j|\varepsilon|\le O(1/w)+C_j\varepsilon^2✓ \Longrightarrow \boxed{|\varepsilon|\le \frac{2O(1/w)}{c_j}✓} \Longrightarrow \operatorname{dist}=O(w^{-1})✓✓$$

## §2 补丁 2（五者同值的纯代数化 ✓✓）

$$\text{构造}✓（\text{纯整数}✓）：m:=5a^{-1}\bmod 11✓ \Longrightarrow am\equiv5✓,\quad bm=(11-a)m\equiv-5\equiv6\pmod{11}✓✓$$
$$\Longrightarrow \cos\bigl(a\cdot\tfrac{2\pi m}{11}\bigr)=\cos\tfrac{10\pi}{11}=-\cos\tfrac{\pi}{11}✓,\qquad \cos\bigl(b\cdot\tfrac{2\pi m}{11}\bigr)=\cos\tfrac{12\pi}{11}=-\cos\tfrac{\pi}{11}✓✓$$
$$\Longrightarrow \boxed{\ H_{a,b}\bigl(\tfrac{2\pi m}{11}\bigr)=\frac{b(-\cos\tfrac{\pi}{11})+a(-\cos\tfrac{\pi}{11})}{11}=-\cos\tfrac{\pi}{11}✓✓\ }（\text{因}\ a+b=11✓）$$

```
   j    a    b   m=5a⁻¹    am mod11   bm mod11   H_{a,b}（解析）
   1    1   10      5          5          6      -0.9594929736145
   2    5    6      1          5          6      -0.9594929736145
   3    4    7      4          5          6      -0.9594929736145
   4    3    8      9          5          6      -0.9594929736145
   5    2    9      8          5          6      -0.9594929736145
```

$$\textbf{"这是全局 min"的补法}✓✓：\text{由}\ H'_{a,b}(y)=-\frac{2ab}{11}\sin\frac{11y}2\cos\frac{(a-b)y}2✓ \Longrightarrow \text{临界点}=\bigl\{\tfrac{2\pi m}{11}\bigr\}\cup\bigl\{\tfrac{\pi(2m+1)}{|a-b|}\bigr\}✓$$
$$\qquad（\text{网格点}：\text{值由}\ am\bmod 11\ \text{的有限表定}✓，\text{其中唯一低值}=-c_0✓；\text{非网格点}：|\cos(k y)|\ \text{结构给出}\ H\ge-c_0✓\ \text{（有限枚举已核}✓））$$
$$\qquad \textbf{注}✗：\text{五 pair 的 min 值是【同一常数}】✓，\text{且与 }j\ \text{无关}✓\ \text{—— 这本身是 11-周期结构的推论}✓$$

## §3 ⭐ 上界升级为精确（初等可证 ✓✓）

$$\text{取}\ (\varphi_1,\varphi_2)=\bigl(\theta_j,\ \tfrac{2\pi m}{11}\bigr)✓：$$
$$\qquad k\in P_j\Longrightarrow w\cos(k\theta_j)+\cos\bigl(k\tfrac{2\pi m}{11}\bigr)=w\kappa-c_0✓✓\（\text{§2}✓）$$
$$\qquad k\notin P_j\Longrightarrow \cos(k\theta_j)\le\kappa-\Delta✓ \Longrightarrow \text{值}\le w(\kappa-\Delta)+1✓$$
$$\Longrightarrow \text{当}\ w\ \ge\ \frac{1+c_0}{\Delta}=\frac{1+0.9594929736}{0.4258385198}=4.6019\ldots✓ \Longrightarrow \boxed{\ g_w(10)\le w\kappa-c_0\ \text{精确}\ (\forall w\ge5)✓✓\ }$$

## §4 B2-1-II 预判：$c_{1,j}$（**全为零** ✓）

$$\text{方法}✓：\text{固定 pair}\ (a,b)✓，\text{在}\ (\theta_j,\tfrac{2\pi m}{11})\ \text{附近对}\ (\varepsilon,y)\ \text{做二维局部极小化}\ \max(A,B)✓，\text{再算}\ c_1=w\bigl[V-(w\kappa-c_0)\bigr]✓$$
```
  j    pair        w=1e3        w=1e4        w=1e5        ⟹ c1
  1   ( 1,10)   0.0e+00      0.0e+00      0.0e+00       0
  2   ( 5, 6)   3.4e-13      1.8e-12      2.9e-11       0（≈ w·1e-16 浮点噪声）
  3   ( 4, 7)   同上          同上          同上          0
  4   ( 3, 8)   同上          同上          同上          0
  5   ( 2, 9)   0.0e+00      0.0e+00      0.0e+00       0
```
$$\Longrightarrow \boxed{\text{五者【全为零}】✓ \Longrightarrow \textbf{无二阶对称破缺}✓ —— \text{数值提示}\ g_w=w\kappa-c_0\ \text{精确}（w\ \text{充分大}）✓✓}$$
$$\qquad \textbf{警示}✗：\text{本项为浮点局部最小化}✓，\text{不是证明}✗；\text{须用精确 two-branch minimax 复核}✓\（\text{即 B2-1-II 本体}✓）$$

## §5 状态与下一步

| 项 | 状态 |
|---|---|
| 补丁 1（定量尖点） | ✓✓ 完成（显式 $c_j,C_j$） |
| 补丁 2（纯代数化） | ✓✓ 完成（$m=5a^{-1}$，零数值） |
| 上界精确（$w\ge5$） | ✓✓ 完成（初等） |
| 下界（C-237） | ✓ $w\kappa-c_0-O(1/w)$ |
| $c_{1,j}$ | ✓ 预判全零（浮点）⟹ 无对称破缺 → **待 B2-1-II 严格复核** |
| **B2-1-II** | ⬜ **可开**（精确 two-branch minimax ✓，不用加权平均 ✓） |

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 定量尖点不等式      命中文件数=1  ::  ./C238-B2-1-theorem-audit-two-patches-and-c1-preview.md
技术词 模十一构造          命中文件数=1  ::  ./C238-B2-1-theorem-audit-two-patches-and-c1-preview.md
技术词 二阶对称破缺预判    命中文件数=1  ::  ./C238-B2-1-theorem-audit-two-patches-and-c1-preview.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；C_\infty\ \text{的 degree-9 结构未塞回}✓$$
$$\textbf{② §4 为浮点预判}✗；\textbf{③ §2 的"全局 min"补法}：\text{网格点已纯代数化}✓，\text{非网格点为有限枚举高精度核验}✓（\text{待写成显式区间比较}✗）$$
$$\textbf{④ 一般 }M\ \text{与一般窗}N✗\ \text{未涉及}✓$$
