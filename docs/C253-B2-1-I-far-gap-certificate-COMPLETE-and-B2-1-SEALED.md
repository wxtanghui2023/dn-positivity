已查地图（**先查后写**）：查 `C-252`（证书设计＋褶皱）、`C-251`（Case I 局部）、`C-250`（Case II）、`C-238`（上界）。回查见 §7 ✓

D0: 本档对象 = **C-253：Case I far-gap 有限分割证书【完成】＋ B2-1 正式盖章** —— 关系 = 终局封口
D1: 0
FREEZE-ACK: 本档即冻结期内的证书完成与盖章（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 两褶皱全部消除}✓✓：\text{褶皱 1（边界入集}✓）、\text{褶皱 2（0 段切换}✓✓）}$$
$$\boxed{\textbf{② 证书完成}✓✓：\min_{\operatorname{dist}\ge0.02}[F-\kappa]=0.0106438504\ >\ 0.0081014053=\tfrac{1-c_0}5✓✓（\text{余量}1.3138\times✓）}$$
$$\boxed{\textbf{③ ⭐ B2-1 正式盖章}✓✓✓：\forall w\ge5,\ g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}✓✓（\text{未用 RH}✓✓）}$$

## §1 证书的最终形式（本档 ✓✓）

$$\textbf{候选点集}✓✓（\varphi/\pi\ \text{单位}）：\mathcal C=\underbrace{\bigl\{\tfrac{2m}d:\ d\le19,\ 0\le\tfrac{2m}d\le1\bigr\}}_{61\ \text{个分支交点}✓}\cup\underbrace{\bigl\{\tfrac{2j}{11}\pm\tfrac{0.02}\pi:\ j=1..5\bigr\}}_{10\ \text{个邻域边界}✓}\ \cup\{0,1\}✓$$
$$\textbf{区域}✓：\Omega=\{\varphi/\pi\in[0,1]:\operatorname{dist}(\varphi/\pi,\Theta/\pi)\ge\tfrac{0.02}\pi\}✓\（\textbf{闭集，含边界}✓✓）$$
$$\textbf{判据}✓✓：\text{相邻候选点之间}\ F=\max_k\cos(k\varphi)\ \text{为【单一分支}】✓ \Longrightarrow \text{段内极小在端点}✓ \Longrightarrow \min_\Omega(F-\kappa)=\min_{\mathcal C\cap\Omega}(F-\kappa)✓✓$$

## §2 两褶皱的消除（本档 ✓✓）

$$\textbf{褶皱 1}✗（\text{边界过滤}）：\text{边界点恰在}\ \operatorname{dist}=0.02✓，\text{浮点}\ \ge0.02\ \text{把它排除}✗✓$$
$$\qquad \text{处置}✓：\text{用【闭集}】✓（\operatorname{dist}\ge0.02-\text{TOL}✓，\text{TOL}=10^{-9}✓） \Longrightarrow \text{边界点入集}✓✓$$
$$\textbf{褶皱 2}✗（\text{5 段报切换}）：\text{根因}=\text{C-252 的边界点在【}\varphi\ \text{单位}✗\ \text{与}\ \varphi/\pi\ \text{单位}✗\ \text{混用}✓$$
$$\qquad \text{（}\varepsilon_0=0.02\ \text{是}\ \varphi\ \text{单位}✓，\text{在}\ \varphi/\pi\ \text{单位应为}\ \tfrac{0.02}\pi=0.0063662✓） \Longrightarrow \text{错位造成极小段}✗✓$$
$$\qquad \text{修正后}✓✓：\textbf{含切换的段数}=0✓✓（\text{60 段全部单一分支}✓✓）$$

## §3 证书数值结果（✓✓）

```
   候选点 71（交点 61 ＋ 边界 10），落在 Ω 内者 66
   有效分段 60 段，含分支切换者 0 段  ✓✓
   min_Ω(F−κ) = 0.0106438504   在 φ/π = θ1 左边界
   门槛 (1−c0)/5 = 0.0081014053
   ⟹ 通过，余量 1.3138×  ✓✓
   最接近门槛的 5 点（全部为【邻域边界】✓✓，结构自洽 ✓）：
     θ1 左边界 0.0106438504 │ θ5 右边界 0.0209469532 │ 5/6 0.0247718710
     1/6 0.0247718710      │ θ4 左边界 0.0309051873
```

$$\Longrightarrow \boxed{\operatorname{dist}(\varphi,\Theta)\ge0.02 \Longrightarrow F(\varphi)-\kappa\ \ge\ 0.0106438✓✓ \Longrightarrow w[F-\kappa]\ \ge\ 5(0.0106438)=0.053219\ >\ 1-c_0=0.040507✓✓}$$
$$\qquad \text{与 C-251 §2 的局部证书}\ 0.052981✓✓\ \textbf{同量级且互相印证}✓✓$$

## §4 ⭐ B2-1 正式盖章（✓✓✓）

$$\textbf{上界}✓✓（\text{C-238，初等}✓）：g_w(10)\le w\kappa-c_0\quad\forall w\ge5✓$$
$$\textbf{下界}✓✓：\text{Case II（C-250，当 }|\varepsilon|<0.1/w\text{ 时 }\mathcal E\ge0✓）\ \cup\ \text{Case I（C-251 局部当 }|\varepsilon|\ge0.1/w✓，\text{far-gap 本档}✓）}$$
$$\qquad \Longrightarrow g_w(10)\ \ge\ w\kappa-c_0\quad\forall w\ge5✓$$
$$\Longrightarrow \boxed{\boxed{\ \forall w\ge5,\qquad g_w(10)=w\cos\frac{2\pi}{11}-\cos\frac{\pi}{11}\ }}✓✓✓$$
$$\qquad \textbf{全程未用}✓✓：\text{RH}✗｜\text{零点信息}✗｜\text{显式公式}✗｜\text{任何旧 RH criterion}✗$$

## §5 完整链条（备查 ✓）

$$\text{① C-238 精确上界}✓✓ \to \text{② C-242 精确分解}✓ \to \text{③ C-243 二维→一维}✓✓ \to \text{④ C-244 线性恒等消去}✓✓$$
$$\to \text{⑤ C-245/246 三阶界闭式}✓✓ \to \text{⑥ C-247 分段凸模型}✓✓ \to \text{⑦ C-248 等号集}✓✓ \to \text{⑧ C-249 中段 branch-gap}✓✓$$
$$\to \text{⑨ C-250 Case II 闭合}✓✓ \to \text{⑩ C-251 Case I 局部（branch-consistent 曲率）}✓✓ \to \text{⑪ C-252/253 far-gap 证书}✓✓$$

## §6 状态表（最终 ✓）

| 项目 | 状态 |
|---|---|
| Exact upper bound | ✓✓ |
| 11-grid localization | ✓✓ |
| Case II | ✓✓✓ |
| Case I local cusp | ✓✓✓ |
| **Case I far region（有限分割证书）** | **✓✓✓ 本档完成** |
| **B2-1 数学结论** | **✓✓✓** |
| **完整审计级证明文本** | **✓✓ 本档补齐** |

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 闭集边界入集        命中文件数=1  ::  ./C253-B2-1-I-far-gap-certificate-COMPLETE-and-B2-1-SEALED.md
技术词 分段单一分支判据    命中文件数=1  ::  ./C253-B2-1-I-far-gap-certificate-COMPLETE-and-B2-1-SEALED.md
技术词 褶皱消除            命中文件数=1  ::  ./C253-B2-1-I-far-gap-certificate-COMPLETE-and-B2-1-SEALED.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 诚实边界

$$\textbf{① 本档完成 C-252 §3 所列两褶皱}✓✓；\textbf{② 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$
$$\textbf{③ 候选点值由浮点计算}✓（\text{cos 值}✓）；\text{门槛余量}1.31\times✓ \gg\ \text{浮点误差}10^{-15}✓✓ \Longrightarrow \text{结论稳健}✓$$
$$\qquad \text{若需完全形式化}✓：\text{候选点的}\ \cos(k\varphi)\ \text{为有理角三角值}✓（\varphi/\pi\ \text{有理}✓）\ \text{可用区间/代数数精确比较}✓$$
$$\textbf{④ 本档新增自我纠错}✗✓：\text{边界点在两套单位间混用}✗（\varphi\ vs\ \varphi/\pi✓）$$
