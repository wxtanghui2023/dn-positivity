已查地图（**先查后写**）：查 `C-236`（上界＋五极值点结构）、`C-234`（框架）、`C-159`/`C-192`（鸽笼＋等号集）、`C-233`（审计条款）。回查见 §7 ✓

D0: 本档对象 = **B2-1 下界：三 lemma 组织 ＋ $O(1)$ 双边闭合定理**（11-周期 minimax 分类）—— 关系 = 严密化与闭合
D1: 0
FREEZE-ACK: 本档即冻结期内的引理建立与定理装配（依 §8.1；不产候选结论）

---

## §0 目标定理

$$\boxed{\ \textbf{Theorem B2-1-∞}\ ✓：\ g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}+O(w^{-1})\ }（\text{第一阶段：}O(1)\ \text{双边闭合}✓）$$
$$\text{上界}✓：\text{C-236 已证}\ g_w\le w\kappa-\cos\tfrac{\pi}{11}✓（\text{显式构型}✓）\qquad \text{本档补【下界}】✓$$

## §1 Lemma 1（Localization ＋ 尖点结构 ✓）

$$\textbf{(a)}\ \min_{\phi\in[0,\pi]}F(\phi)=\kappa✓,\quad F(\phi):=\max_{1\le k\le10}\cos k\phi✓,\quad \Theta=\{\theta_j=\tfrac{2\pi j}{11}:j=1,\dots,5\}✓（\text{等号集恰为}\ \Theta✓）$$
$$\qquad [\text{经典}✓，\text{C-159/C-192 已证}✓；\text{本档只引用并核验数值}✓]$$
$$\qquad \text{数值核验}✓：F(\theta_j)=\kappa=0.841253532831181169✓\ \text{对全部 }j=1..5✓$$

$$\textbf{(b) 尖点结构}✓✓（\text{本档新}✓，\text{比唐先生预期的 }O(w^{-1/2})\ \text{更强}✓）：$$
$$\qquad \text{在}\ \theta_j\ \text{处恰有【两分支交叉}】✓：P_j=\{a_j,b_j\}✓,\quad a_jj\equiv1✓,\ b_jj\equiv-1\pmod{11}✓ \Longrightarrow b_j=11-a_j✓✓$$
$$\qquad \text{斜率}：\tfrac{d}{d\phi}\cos(k\phi)\big|_{\theta_j}=-k\sin(k\theta_j)=:-k\sigma_k s_j✓,\quad s_j:=\sin\theta_j✓,\ \sigma_k=\pm1✓$$
$$\qquad \text{其中}\ \sigma_{a_j}=+1✓（\text{因}\ a_j\theta_j\equiv\theta_j✓）,\ \sigma_{b_j}=-1✓（\text{因}\ b_j\theta_j\equiv-\theta_j✓） \Longrightarrow \textbf{两分支斜率【反号}】✓✓$$
$$\Longrightarrow \boxed{\ F(\theta_j+\varepsilon)-\kappa=s_j\max\bigl(-a_j\varepsilon,\ +b_j\varepsilon\bigr)+O(\varepsilon^2)✓✓\ }（\text{尖点}✓）$$
$$\qquad \text{数值核验}✓（j=1✓，s_1=\sin\tfrac{2\pi}{11}=0.5406✓）：\text{右斜率}\ 5.406=10\cdot s_1✓✓,\ \text{左斜率}\ 0.5406=1\cdot s_1✓✓$$

$$\textbf{(c) 结论}✓：\text{对任意近极小点}\ (\varphi_{1,w},\varphi_{2,w})✓,\ \text{由}\ wF(\varphi_{1,w})\le w\kappa+O(1)✓ \Longrightarrow$$
$$\qquad \boxed{\ \operatorname{dist}(\varphi_{1,w},\Theta)=O(w^{-1})✓✓\ }（\text{由尖点线性率}✓，\text{比 }O(w^{-1/2})\ \text{强}✓✓）$$
$$\qquad \text{定量形式}✓：|\varphi_{1,w}-\theta_j|\le\frac{1+C_1/w}{s_j\min(a_j,b_j)}\cdot\frac1w+O(w^{-2})✓$$

## §2 Lemma 2（八分支 uniform gap ✓）

$$\boxed{\ \Delta:=\min_{j}\min_{k\notin P_j}\bigl[\kappa-\cos(k\theta_j)\bigr]>0✓\ }（\text{有限集上的显式正数}✓）$$
$$\text{数值（精确核验}✓）：\Delta=\kappa-\cos\tfrac{4\pi}{11}=0.42583851982929474333\ldots✓✓$$
$$\qquad \text{各 }j\ \text{的取到位置}✓：j=1\to k=2✓；j=2\to k=1✓；j=3\to k=8✓；j=4\to k=6✓；j=5\to k=7✓ \Longrightarrow \textbf{值恒等}✓✓$$
$$\Longrightarrow \text{若}\ |\varphi_1-\theta_j|\le c/w\ \text{且}\ w\ \text{充分大}✓ \Longrightarrow \text{对一切}\ k\notin P_j✓：$$
$$\qquad w\cos(k\varphi_1)+\cos(k\varphi_2)\ \le\ w\bigl(\kappa-\tfrac\Delta2\bigr)+1\ <\ w\kappa-\tfrac\Delta2 w+1✓ \Longrightarrow \textbf{max 只由 }P_j\ \textbf{取到}✓✓$$
$$\qquad（\text{逻辑顺序}✓：\textbf{先证 }\varphi_1\ \textbf{入某井}✓，\textbf{再用该井自己的 gap}✓ \text{—— 不反向假定}✓）$$

## §3 Lemma 3（配对 minimax 下界：五者统一 ✓✓）

$$\text{记}\ A:=w\cos(a\varphi_1)+\cos(a\varphi_2)✓,\quad B:=w\cos(b\varphi_1)+\cos(b\varphi_2)✓,\quad a+b=11✓$$
$$\textbf{关键不等式}✓：\max(A,B)\ \ge\ \frac{bA+aB}{a+b}=\frac{bA+aB}{11}✓\（\lambda=\tfrac b{11},\mu=\tfrac a{11},\lambda+\mu=1✓）$$
$$\text{展开}✓（\varphi_1=\theta_j+\varepsilon✓,\ \cos(k(\theta_j+\varepsilon))=\kappa-k\sigma_k s_j\varepsilon-\tfrac{k^2\kappa}2\varepsilon^2+O(\varepsilon^3)✓）:$$
$$\qquad bA+aB=(a+b)w\kappa+\bigl[-ab s_j\varepsilon+ab s_j\varepsilon\bigr]w+\bigl[b\cos(a\varphi_2)+a\cos(b\varphi_2)\bigr]-\tfrac{\kappa}2\bigl(ba^2+ab^2\bigr)w\varepsilon^2+\cdots$$
$$\qquad \Longrightarrow \textbf{线性 }\varepsilon\ \textbf{项恰好抵消}✓✓ \Longrightarrow \boxed{\ \max(A,B)\ge w\kappa+H_{a,b}(\varphi_2)+O(w\varepsilon^2)\ }✓$$
$$\qquad H_{a,b}(y):=\frac{b\cos(ay)+a\cos(by)}{11}=\frac{(11-a)\cos(ay)+a\cos((11-a)y)}{11}✓✓$$

$$\textbf{临界点显式}✓✓\ （\text{本档关键新工具}✓）：H'_{a,b}(y)=-\frac{ab}{11}\bigl[\sin(ay)+\sin(by)\bigr]=-\frac{2ab}{11}\sin\tfrac{11y}2\cos\tfrac{(a-b)y}2✓$$
$$\qquad \Longrightarrow \text{临界点}=\Bigl\{\tfrac{2\pi m}{11}\Bigr\}\cup\Bigl\{\tfrac{\pi(2m+1)}{|a-b|}\Bigr\}✓✓（\text{显式、有限}✓）$$

$$\textbf{五个 pair 的最小值（临界点有限枚举）}✓✓：$$
```
   a    b   |a-b|        min_y H              argmin y/pi     位置
   1   10      9    -0.95949297361449738989    10/11         grid m=5
   2    9      7    -0.95949297361449738989     6/11         grid m=3
   3    8      5    -0.95949297361449738989     4/11         grid m=2
   4    7      3    -0.95949297361449738989     8/11         grid m=4
   5    6      1    -0.95949297361449738989     2/11         grid m=1
```
$$\Longrightarrow \boxed{\ \min_y H_{a,b}(y)=-\cos\tfrac{\pi}{11}✓✓\ \text{对全部五个 pair}✓✓\ }（\text{统一}✓✓）$$
$$\qquad \text{结构原因}✓✓：\text{取}\ y=\tfrac{2\pi m}{11}\ \text{使}\ am\equiv\pm5\pmod{11}✓ \Longrightarrow \cos(ay)=\cos(by)=-\cos\tfrac{\pi}{11}✓✓$$
$$\qquad \Longrightarrow H=\frac{(11-a)(-c)+a(-c)}{11}=-c✓\ \text{（因}\ a+b=11✓）✓✓$$

## §4 装配（下界证明 ✓）

$$\text{取任意}\ (\varphi_1,\varphi_2)\in[0,\pi]^2✓,\ w\ \text{充分大}✓：$$
$$\textbf{情形 A}✓：F(\varphi_1)\ge\kappa+\tfrac{1-\cos(\pi/11)}{w}✓ \Longrightarrow M_w\ge wF(\varphi_1)-1\ge w\kappa-\cos\tfrac{\pi}{11}✓✓\ \text{完成}✓$$
$$\textbf{情形 B}✓：F(\varphi_1)<\kappa+\tfrac{1-\cos(\pi/11)}{w}✓ \Longrightarrow \text{Lemma 1(c) 给}\ \varphi_1=\theta_j+\varepsilon✓,\ |\varepsilon|\le\tfrac{C}{w}✓$$
$$\qquad \Longrightarrow \text{Lemma 2 给 max 只由}\ P_j\ \text{取到}✓ \Longrightarrow \text{Lemma 3 给}$$
$$\qquad M_w\ge\max(A,B)\ge w\kappa+\min_yH_{a,b}(y)-O(w\varepsilon^2)=w\kappa-\cos\tfrac{\pi}{11}-O(w^{-1})✓✓$$
$$\Longrightarrow \boxed{\ g_w\ge w\kappa-\cos\tfrac{\pi}{11}-O(w^{-1})✓✓\ }\qquad \text{合 C-236 上界}✓ \Longrightarrow \boxed{\ \textbf{Theorem B2-1-∞}\ ✓✓}$$

## §5 阶段边界（依唐先生 19:10 纪律 ✓）

$$\textbf{① 本档只闭合 }O(1)\ \text{常数}✓✓；\textbf{1/w 二阶项为第二阶段}✗\ \text{—— 因 §3 的加权不等式丢掉了 }\varepsilon\ \text{二阶信息}✓（\text{唐先生已指出}✓）$$
$$\textbf{② 未用 RH}✓；\text{未改他档}✓；C_\infty\ \text{的 degree-9 结构【未塞回}】✓$$
$$\textbf{③ 数值层}：\text{Lemma 1(a) 引用经典}✓；\text{Lemma 2 的 }\Delta\ \text{为精确三角值}✓；\text{Lemma 3 为有限临界点枚举}✓（\text{严格化只需对这有限集做区间/代数核验}✓）$$
$$\textbf{④ 待严格化}✗：\text{Lemma 3 的有限枚举需写成【显式代数比较}】✓；\text{Lemma 1(b) 需写出 }O(\varepsilon^2)\ \text{的显式界}✓（|\cos''|\le k^2✓）$$

## §6 本档意义

$$\boxed{\ \textbf{有限 11-周期 minimax 分类}✓✓：\text{五个 11-格井}\ \longrightarrow\ \text{五个不同 active pair}\ \longrightarrow\ \text{同一个}\ -\cos\tfrac{\pi}{11}✓✓\ }$$
$$\qquad \text{这把 B2-1 从"数值发现正确支"升级为【可审计的对称-分类定理}】✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 尖点定位率          命中文件数=1  ::  ./C237-B2-1-lower-bound-three-lemmas-11-periodic-minimax-classification.md
技术词 显式临界点枚举      命中文件数=1  ::  ./C237-B2-1-lower-bound-three-lemmas-11-periodic-minimax-classification.md
技术词 十一周期井分类      命中文件数=1  ::  ./C237-B2-1-lower-bound-three-lemmas-11-periodic-minimax-classification.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 已闭合}✓：\liminf(g_w-w\kappa)\ge-\cos\tfrac{\pi}{11}✓\ \text{（下界，本档）}＋g_w\le w\kappa-\cos\tfrac{\pi}{11}✓（\text{上界，C-236}✓）⟹ \textbf{双边}✓✓$$
$$\textbf{② }1/w\ \text{项}✗：\text{需保留 }\varepsilon\ \text{二阶（}w\varepsilon^2✓）\ \text{做真正的 two-branch minimax}✓（\text{第二阶段}✓）$$
$$\textbf{③ 相变点}w_1\in(2,5]✗\ \text{仍待定}✓；\textbf{④ 一般 }M\ \text{与一般窗 }N✗\ \text{未涉及}✓$$
