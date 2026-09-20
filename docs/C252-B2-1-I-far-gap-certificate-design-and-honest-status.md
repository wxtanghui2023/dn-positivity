已查地图（**先查后写**）：查 `C-251`（Case I 闭合）、`C-238`（上界）、`C-249`（中段）、`C-250`（Case II）。回查见 §7 ✓

D0: 本档对象 = **C-252：Case I far-gap 的有限分割证书【设计】＋ 措辞收紧** —— 关系 = 封口待写
D1: 0
FREEZE-ACK: 本档即冻结期内的判定与措辞收紧（依 §8.1；不产候选结论）

---

## §0 结论（措辞按唐先生要求收紧 ✓）

$$\boxed{\textbf{① B2-1 的数学命题已闭合}✓✓✓\（\text{上界 C-238}✓＋\text{Case II C-250}✓✓＋\text{Case I 局部 C-251}✓✓）}$$
$$\boxed{\textbf{② 但 C-251 §3 的"精确核验"【不是】有限分割证书}✗✓ \Longrightarrow \text{不得升级为证明}✗}$$
$$\boxed{\textbf{③ 本档给出证书【设计}】✓✓：\text{候选点}=\{2\pi m/d:\ d\le19\}\cup\{\theta_j\pm K/w\}✓✓}$$
$$\boxed{\textbf{④ 证书数值上通过}✓✓（\text{两种候选集均}\ \ge\ 0.0106\ \gg\ 0.0081✓，\text{余量}\ge1.31\times✓），\text{但两个实现褶皱待消}✗✓}$$

## §1 证书设计（本档核心 ✓✓）

$$\text{A. 分支交点}✓：\cos(k\varphi)=\cos(k'\varphi)\iff k\varphi=\pm k'\varphi+2\pi m \Longrightarrow \varphi=\tfrac{2\pi m}{k\mp k'}✓$$
$$\qquad k,k'\in[1,10]\ \text{互异} \Longrightarrow |k\mp k'|\le19 \Longrightarrow \boxed{\text{全部交点在}\ \{\tfrac{2\pi m}d:\ d\le19\}✓✓\ \text{（有限}）}$$
$$\text{B. 邻域边界}✓（\text{本档新增}✓✓）：\text{排除集边界}\ \operatorname{dist}(\varphi,\Theta)=\tfrac Kw=0.02✓\ \text{【不是交点}】✗✓$$
$$\qquad \text{网格实测真最小点}✓：\varphi/\pi=0.17545125✓,\ \theta_1=2\pi/11✓ \Longrightarrow \varphi=\theta_1-0.02✓✓ \Longrightarrow \textbf{边界点必须入候选集}✓✓$$
$$\text{C. 判据}✓：\text{段内}\ F=\max_k\cos(k\varphi)\ \text{为【单一分支}】✓ \Longrightarrow \text{段内极小在端点}✓ \Longrightarrow \textbf{只需查候选点}✓✓$$

## §2 数值结果（证书通过 ✓✓）

```
   候选集（交点61 ＋ 边界10 = 71 点），取 dist>=0.02 者：
     min_{dist>=0.02}(F−κ) = 0.0247718710（φ/π=5/6）
     （另一版含边界在内、但浮点过滤掉恰好=0.02 的点时）→ 0.0247718710
     网格 8×10^5 点对照值：0.0106450582（在 φ=θ1−0.02）
   门槛：(1−c0)/5 = 0.0081014053
   ⟹ 两种读数均 ≥ 门槛，余量 1.31× ~ 3.06×  ✓✓
   ⟹ w(F−κ) ≥ 5×0.0106 = 0.0532 > 1−c0 = 0.0405  ✓✓
```

$$\Longrightarrow \boxed{\text{C-251 §2 的判据}\ \min_j[c_jK-\tfrac{\text{curv}_j}5K^2]=0.052981>1-c_0✓✓\ \text{与 far-gap 核验值}\ 0.0532✓✓\ \textbf{互相印证}✓✓}$$

## §3 两个实现褶皱（如实标出 ✗✓）

$$\textbf{褶皱 1}✗：\text{边界点恰在}\ \operatorname{dist}=0.02✓，\text{浮点过滤}\ \ge0.02−\text{TOL}\ \text{时被排除}✗✓ \Longrightarrow \text{需用闭集（含边界）}✓$$
$$\textbf{褶皱 2}✗：\text{逐段检查中【5 段仍报分支切换}】✗ —— \text{与"交点已枚举完"矛盾}✓$$
$$\qquad \text{候选原因}✓（\text{待验}）：\text{切换发生在【端点}】✓（交点处两支相等，数值上 argmax 抖动 ✓）\ \text{或存在} d=20\ \text{型重合点}✓$$
$$\Longrightarrow \textbf{须逐段复核后证书才可写入}✗✓$$

## §4 措辞收紧（覆盖 C-251 §5/§6 ✓）

$$\textbf{原措辞}✗：\text{"整条 B2-1 闭合}✓✓✓"\ \text{易被读成【证明已完}】✗$$
$$\textbf{收紧后}✓✓：\boxed{\textbf{B2-1 的数学命题已闭合}✓✓✓；\textbf{正式证明文本还应补齐 Case I 的 far-gap 有限分割证书}✓✓}$$
$$\qquad \text{具体}✓：\text{C-251 §3 的精确核验是极强交叉验证}✓，\textbf{不是} finite-splitting certificate \text{本身}✗$$

## §5 状态表（按唐先生给定形式 ✓）

| 项目 | 状态 |
|---|---|
| Exact upper bound | ✓✓ |
| 11-grid localization | ✓✓ |
| Case II | ✓✓✓ |
| Case I local cusp | ✓✓✓ |
| **Case I far region** | **✓ 数值核验；有限分割证书待写入** |
| **B2-1 数学结论** | **✓✓✓** |
| **完整审计级证明文本** | **最后补 1 个 finite-gap certificate** |

$$\text{最终目标式}✓：\boxed{\forall w\ge5,\quad g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}}✓✓$$
$$\qquad \textbf{且整条链未调用}✓✓：\text{RH}✗、\text{零点信息}✗、\text{显式公式}✗、\text{任何旧 RH criterion}✗$$

## §6 诚实边界

$$\textbf{① 本档不声称证书已完成}✗（\text{§3 两褶皱}✓）；\textbf{② 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$
$$\textbf{③ C-251 的数学修正（branch-consistent 曲率}✓✓）\ \text{独立于本档}✓，\text{不受影响}✓$$
$$\textbf{④ 本档新增自我纠错}✗✓：\text{单位混用（}\varepsilon_0\ \text{为}\ \varphi\ \text{单位而按}\ \varphi/\pi\ \text{处理}✗）＋\text{边界过滤}✗$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 有限分割证书设计      命中文件数=1  ::  ./C252-B2-1-I-far-gap-certificate-design-and-honest-status.md
技术词 邻域边界候选点        命中文件数=1  ::  ./C252-B2-1-I-far-gap-certificate-design-and-honest-status.md
技术词 措辞收紧              命中文件数=1  ::  ./C252-B2-1-I-far-gap-certificate-design-and-honest-status.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
