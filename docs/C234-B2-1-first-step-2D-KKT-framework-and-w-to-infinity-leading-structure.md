已查地图（**先查后写**）：查 `C-233`（B2/T13 回收，含审计条款与双边边界结果）、`C-193`（w=1 等号集＋w 表）、`C-199`/`C-200`（w=2 定理＋等号集）、`C-159`（鸽笼定理 $\kappa_N$）。主图无 T13/weighted 条目 ⟹ 未覆盖 ✓。回查见 §6 ✓

D0: 本档对象 = **B2-1 第一件：2 维 KKT/active-set 框架 ＋ $w\to\infty$ leading 结构**（解析，不做数值扫描）—— 关系 = 结构建立与开口定位
D1: 0
FREEZE-ACK: 本档即冻结期内的结构建立与登记（依 §8.1；不产候选结论）

---

## §0 对象的固定（承 `C-233` ✓）

$$\boxed{\ g_w\ :=\ g_w(10)\ =\ \inf_{(\varphi_1,\varphi_2)\in[0,\pi]^2}\ \max_{1\le k\le10}\ Z_k(\varphi_1,\varphi_2)\ }✓,\qquad Z_k:=w\cos k\varphi_1+\cos k\varphi_2✓,\quad w\ge1✓$$
$$\text{已知锚点}：g_1=\tfrac12✓,\quad g_2=1✓,\quad g_w=w\kappa_{10}+O(1)✓（\kappa_{10}=\cos\tfrac{2\pi}{11}✓,\ \text{双边已验证}✓）$$

## §1 ⭐ 2 维 KKT/active-set 框架（结构性事实 ✓）

$$\textbf{梯度}：\nabla Z_k=-k\bigl(w\sin k\varphi_1,\ \sin k\varphi_2\bigr)\in\mathbb R^2✓\qquad（\text{变量维数}\ d=2✓）$$
$$\textbf{Carathéodory}✓：\text{极小点处}\ 0\in\mathrm{conv}\{\nabla Z_k:k\in A\}✓ \Longrightarrow |A|\ge d+1=3✓✓$$
$$\textbf{每个三元组给一个 4×4 系统}✓：\text{未知量}\ (\varphi_1,\varphi_2,\lambda_1,\lambda_2)✓（\lambda_3=1-\lambda_1-\lambda_2✓）$$
$$\qquad \begin{cases}\sum_{k\in A}\lambda_k\nabla Z_k=0&\quad(2\ \text{方程}✓)\\ Z_{k_1}=Z_{k_2},\ Z_{k_2}=Z_{k_3}&\quad(2\ \text{方程}✓)\end{cases}\qquad\Longrightarrow 4\ \text{方程}/4\ \text{未知量}✓$$
$$\qquad \text{可行性}：\lambda_k\ge0✓ \Longrightarrow \text{三元组按可行性【筛选}】✓（\text{不需扫描}✓）$$

## §2 ⭐⭐ 关键观测：两个已知锚点都是【退化】的

| $w$ | $g_w$ | active set $A$ | $|A|$ | 是否 generic（$|A|=3$） |
|---|---|---|---|---|
| **1** | $\tfrac12$ ✓ | $\{1,4,5,7,8\}$ | **5** | ✗ **退化**（超定 2 个自由度） |
| **2** | $1$ ✓ | $\{1,5,6,7\}$ | **4** | ✗ **退化**（超定 1 个） |
| generic $w$ | ？ | 应为 3 元 | 3 | ✓（待证） |

$$\Longrightarrow \textbf{结构性假设 H1}✓：\text{【退化点】= 特殊权重}（w=1,2,\dots✓），\text{其常数取【代数特值】}（\tfrac12,1✓）；\text{两退化点之间为【generic 区间}】✓（|A|=3✓），\text{由某个 3 元约束系统控制}✓$$
$$\qquad \text{⚠️ 本档只登记 H1}✗，\textbf{不声称已证}✗$$

## §3 ⭐⭐ $w\to\infty$ 的 leading 结构（把渐近与数值接起来 ✓）

$$\text{第一坐标的 extremal}✓：\theta^*=\tfrac{2\pi}{11}✓\ \text{使}\ \max_{1\le k\le10}\cos k\theta^*=\kappa_{10}✓ \Longrightarrow \textbf{极值在}\ k=1\ \text{与}\ k=10\ \text{同时达到}✓✓$$
$$\qquad \text{因}\ \cos\tfrac{2\pi}{11}=\cos\tfrac{20\pi}{11}=\cos\bigl(10\cdot\tfrac{2\pi}{11}\bigr)✓（\text{因}\ 10\equiv-1\pmod{11}✓） \Longrightarrow \textbf{leading active set}\ \{1,10\}✓✓$$
$$\textbf{直觉上但【不严格】的说法}✗：g_w\stackrel{?}{=}w\kappa_{10}-1+\cdots✓\ \text{—— 仅在}\ \varphi_2=\pi\ \text{（}\cos k\varphi_2=-1\ \text{对所有 }k✓）\ \text{时才给}\ -1✓，\text{而}\ \varphi_2=\pi\ \text{会破坏 tie}✗$$
$$\textbf{真正的一阶问题}✓✓：\text{由 tie 方程}\ w\cos\varphi_1+\cos\varphi_2=w\cos10\varphi_1+\cos10\varphi_2✓ \Longrightarrow \text{写}\ \varphi_1=\theta^*+\delta✓\ \text{得}$$
$$\qquad w\bigl[\cos(\theta^*+\delta)-\cos(10\theta^*+10\delta)\bigr]=\cos10\varphi_2-\cos\varphi_2✓$$
$$\qquad \text{左端展开}：\cos(\theta^*+\delta)-\cos(10\theta^*+10\delta)\ \approx\ -\bigl(\sin\theta^*-10\sin10\theta^*\bigr)\delta+O(\delta^2)✓$$
$$\qquad \text{配合}\ \cos\theta^*=\cos10\theta^*=\kappa_{10}✓ \Longrightarrow \delta\ \asymp\ \frac{1}{w}✓ \Longrightarrow \boxed{\text{修正项}\ \delta\ \text{与第二分支的取值共同给出 }O(1)\ \text{修正}✓✓}$$
$$\textbf{待解的一维问题}✓：\text{令}\ \delta\to0\ \text{时 tie 退化为}\ 0=0✗ \Longrightarrow \text{需保留}\ \cos10\varphi_2-\cos\varphi_2\ \text{的】一阶信息}✓$$
$$\qquad \text{即：在}\ \{\varphi_1\ \text{由 tie 决定}\}\ \text{的约束下，求}\ \max\bigl[\cos\varphi_2\ \text{与}\ \cos10\varphi_2\ \text{的共同值}\bigr]\ \text{的最优点}✓$$
$$\qquad \Longrightarrow \text{这是一个【一维】问题}✓ \Longrightarrow \text{可望给出【精确的 }O(1)\ \text{修正}】✓✓（\text{这才是唐先生要的"新机制"✓}）$$

## §4 B2-1 的工作计划（解析优先，禁止扫描 ✓）

$$\textbf{Step 1}✓（本档）：\text{框架＋H1 登记}✓ \text{—— 完成}✓$$
$$\textbf{Step 2}✓：\text{三元组【可行性分类}】✓ —— \text{枚举} \binom{10}{3}=120\ \text{个三元组}✓，\text{按}\ 0\in\mathrm{conv}\{\nabla Z_k\}\ \text{与}\ \lambda\ge0\ \text{筛选}✓（\text{符号/代数，非扫描}✓）$$
$$\textbf{Step 3}✓：\text{对每个可行三元组，给出其控制区间}\ I_A\subset[1,\infty)✓ \text{的【判据}】✓（\text{比较竞争分支}✓）$$
$$\textbf{Step 4}✓：\text{定位相变点}\ w_j✓ \text{为【增广系统}】的解（\text{第 4 个分支追上}✓）$$
$$\textbf{Step 5}✓：\text{攻 }w\to\infty\ \text{的一维修正问题}✓（§3✓），\text{争取【精确}】✓$$
$$\textbf{禁止}✗：\text{先跑}\ w=1.01,1.02,\dots\ \text{的扫描}✗（\text{唐先生 18:49 明令}✓）$$

## §5 边界

$$\textbf{① 已确立}✓：d=2\Longrightarrow|A|\ge3✓（Carathéodory✓）；两锚点退化（|A|=5,4✓）；\kappa_{10}\ \text{的极值在}\ k=1,10\ \text{同时达到}✓；g_w=w\kappa_{10}+O(1)✓$$
$$\textbf{② 未证}✗：H1（相变点有限＋piecewise-KKT✓）；§3 的"一维修正问题"能给出精确值✓；\text{三元组筛选的完备性}✓$$
$$\textbf{③ 不做}✗：\text{数值扫描}✗；\text{不把古典 Turán--Cassels 当模板}✗（依 `C-233` 审计条款✓）$$
$$\textbf{④ 未用 RH}✓；\text{未改他档}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 退化锚点观测       命中文件数=1  ::  ./C234-B2-1-first-step-2D-KKT-framework-and-w-to-infinity-leading-structure.md
技术词 三元组可行性分类   命中文件数=1  ::  ./C234-B2-1-first-step-2D-KKT-framework-and-w-to-infinity-leading-structure.md
技术词 一维修正问题       命中文件数=1  ::  ./C234-B2-1-first-step-2D-KKT-framework-and-w-to-infinity-leading-structure.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
