已查地图（**先查后写**）：查 `C-159`（鸽笼定理 κ_N 闭式）、`C-191`（κ_N 与 N 无关）、`C-173`（λ_max）、`CLOSED-ROUTES-MAP.md`（关键词：等号集｜本原根｜最小间距刚性）。回查见 §4 ✓

D0: 本档对象 = **新引理（κ_N 的等号集 = 本原 (N+1) 次单位根）** ＋ 完整初等证明 —— 关系 = 新构造（把 `C-159` 的"锐"升级为"锐 + 等号集已知"）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 引理（新）

$$\textbf{引理}：\text{设}\ \kappa_N=\inf_\theta\max_{1\le m\le N}\cos(m\theta)=\cos\tfrac{2\pi}{N+1}✓（\texttt{C-159}）✓\ \text{则等号集为}$$
$$\qquad \boxed{\ \theta\ \text{使}\ \max_{1\le m\le N}\cos(m\theta)=\cos\tfrac{2\pi}{N+1}\iff\theta\equiv\frac{2\pi k}{N+1}\ (k=1,\dots,N,\ \gcd(k,N+1)=1)\ }✓✓$$
$$\text{即：等号点}\ \textbf{恰为本原 (N+1) 次单位根}✓\ —— \text{离散、有限，共}\ \varphi(N+1)\ \text{个（Euler 函数）}✓$$

## §2 证明（完整，全初等）

$$\textbf{① 关键恒等式}：\text{对}\ m\le N\ \text{有}\ \cos(m\theta)=\cos\big(2\pi\|m\theta/2\pi\|\big)✓（\text{cos 偶 ＋}\ 2\pi\ \text{周期}）✓$$
$$\qquad \Longrightarrow\ \max_{1\le m\le N}\cos(m\theta)=\cos\Big(2\pi\cdot\min_{1\le m\le N}\big\|m\theta/2\pi\big\|\Big)✓$$
$$\qquad （\text{因在}\ [0,\tfrac12]\ \text{上}\ \cos(2\pi x)\ \text{严格减}✓，\text{而}\ \min\|m\theta/2\pi\|\le\tfrac1{N+1}\le\tfrac12✓）$$
$$\textbf{② 最小间距刚性（经典）}：\text{把} N+1\ \text{个点}\ \{0,\theta,\dots,N\theta\}\ \text{排在圆周上}✓。\text{其最小相邻间距}$$
$$\qquad g:=\min\{\text{相邻间距}\}\le\frac{2\pi}{N+1}✓\qquad\textbf{且等号}\iff N+1\ \text{点}\ \textbf{等距}✓$$
$$\qquad （\text{等距}：\text{否则间距不全相等}⟹\text{必有间距}<\text{平均}✓）$$
$$\textbf{③ 点差就是}\ m\theta：\text{任意两点差为}\ m\theta\ (1\le m\le N)✓ \Longrightarrow \min_{m\le N}\|m\theta/2\pi\|=\frac{g}{2\pi}✓$$
$$\textbf{④ 合并}：\text{取等}\iff g=\frac{2\pi}{N+1}\iff N+1\ \text{点等距}\iff (N+1)\theta\equiv0\ (\mathrm{mod}\ 2\pi)✓$$
$$\qquad \qquad\ \text{且}\ \theta\ \text{的轨道大小为}\ N+1\iff\theta=\frac{2\pi k}{N+1}✓,\ \gcd(k,N+1)=1✓$$
$$\textbf{⑤ 推论（无理情形）}：\theta\ \text{无理}\Longrightarrow\text{永不取等}✗✓（\text{因等距要求}\ (N+1)\theta\in2\pi\mathbb Z✓）$$

## §3 数值印证

$$N=3：\text{等号点}\ \theta/2\pi\in\{0.25,0.75\}=\{1/4,3/4\}✓\ \text{恰为}\ \gcd(k,4)=1✓✓$$
$$N=4：\theta/2\pi\in\{0.2,0.4,0.6,0.8\}=\{1/5,2/5,3/5,4/5\}✓\ \text{恰为}\ \gcd(k,5)=1\ (\text{全部})✓✓$$
$$\qquad ⚠️\ N=3\ \text{的}\ k=2\ \text{处}\ \theta=\pi/2\ \text{是等号点}✓，\text{但}\ \theta=0\ \text{处}\ \max=1\ne0✗（\text{非等号}）✓\ —— \text{与"gcd 条件"完全一致}✓✓$$

## §4 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 等号集        命中文件数=0    ::
技术词 本原根        命中文件数=0    ::
技术词 最小间距刚性  命中文件数=0    ::
```
⟹ 三项**均本档首次命名** ✓（检查在落档前执行 ✓；若事后重跑会自命中本档 1 次，依 `C-168` §6 惯例扣除 ✓）

## §5 边界

- 引理**完整证明**（五步，全初等 ✓）；②中的"最小间距刚性"是经典事实（N+1 点圆周最小间距 ≤ 平均间距 ✓），本档给出其应用与装配 ✓
- 数值（§3）仅作印证 ✓，未用作证明 ✓
- 本档把 `C-159` 的"锐"升级为"**锐 ＋ 等号集已知**"✓；**未**声称该等号集结论在文献中不为人知（Turán 族的等号构型是经典主题 ✓，待核 ✓）
- **未用** RH；**未改**他档 ✓
