已查地图（**先查后写**）：`C-380-8`（**Vandermonde 分层** ✓✓）、`C-380-7`（**可行性** ✓✓）、`C-368`（**`\mathcal Z \cap E` 的 3+2 分支** ✓✓）、`C-358`（**边界降 2+2（限 `\mathcal Z`）** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-9：`E_{\mathrm{even}}` 到 Vandermonde 退化集的定量分离审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① ⭐ 档案措辞修正一（采纳）}✗✓：\textbf{「同源」} \text{成立}✓，\ \textbf{「已清除」} \text{不成立}✗✓ \ —— \ \text{因}\ x_i = x_j\ \textbf{只}意味\ |c_i| = |c_j|✗✓$$
$$\qquad \Longrightarrow \ \text{含两种情形}✓：c_i = c_j\ \textbf{或}\ c_i = -c_j✓✓ \ —— \ C\text{-}368\ \text{处理的是}\ \mathcal Z \cap E\ \text{中的 3+2 碰撞分支}✓，\ \textbf{并未}证\ E_{\mathrm{even}} \cap \{x_i = x_j\} = \varnothing✗✓$$
$$\qquad \text{同理}\ x_j = 0✓：C\text{-}358\ \text{的「边界降 2+2」}\ \textbf{是在}\ \mathcal Z\ \text{结构中得到的}✓，\ \textbf{不能}搬成整个\ E_{\mathrm{even}}\ \text{的边界排除}✗✓$$
$$\qquad \Longrightarrow \ \textbf{必须区分}✓✓：\ \boxed{\mathcal Z \cap E_{\mathrm{even}}\ \text{已闭}}✓ \ \textbf{与}\ \boxed{E_{\mathrm{deg}} \cap E_{\mathrm{even}}\ \textbf{尚未闭}}✗✓$$
$$\textbf{② ⭐ 修正二（uniform-margin 陷阱，采纳）}✗✓：\text{即使证}\ \sigma_{\min}(V(x)) > 0\（x \in E_{\mathrm{gen}}✓）\ \textbf{也不能}推出\ \inf_{E_{\mathrm{gen}}}\sigma_{\min} > 0✗✓$$
$$\qquad \text{因}\ \det V(x) = C(\prod_j\sqrt{x_j})\prod_{i<j}(x_j - x_i)✓✓ \Longrightarrow \text{只要}\ E_{\mathrm{even}}\ \text{可任意逼近}\ x_j = 0\ \text{或}\ x_i = x_j✓ \Longrightarrow \sigma_{\min} \to 0✓✓$$
$$\qquad \Longrightarrow \ E_{\mathrm{gen}}\ \text{是}\ \textbf{开层}✓ \Longrightarrow \inf_{E_{\mathrm{gen}}}\sigma_{\min}\ \textbf{很可能为零}✗✓（\text{即使每点满秩}✓），\ \textbf{且非}紧性技巧可自动解决✗✓$$
$$\textbf{③ ⭐ C-380-9 第一问题（本档核心）}✓✓：\ \text{定义退化量}\ \boxed{D(x) := \Big(\prod_{j=1}^{5}x_j\Big)\Big(\prod_{i<j}(x_i - x_j)^2\Big)}✓✓ \ \Longrightarrow \ \text{只问}\ \boxed{\inf_{x \in E_{\mathrm{even}}}D(x) > 0\ ?}✓✓$$
$$\qquad \textbf{性质}✓✓：\text{不是期待它成立}✗，\ \textbf{而是先判死／判活}✓✓$$
$$\textbf{④ 若}\ \inf D = 0✓✓：\text{则}\ \inf\sigma_{\min}(V) = 0\ \text{的可能性}\ \textbf{必须认真处理}✓✓ \Longrightarrow \textbf{简单 uniform-singular-value 证书应停止}✗✓$$
$$\qquad \Longrightarrow \ \textbf{直接转向}\ \min_\sigma\|V(x)\sigma\|_\infty\ \text{的}\ \textbf{discrepancy 型下界}✓✓$$
$$\textbf{⑤ ⭐⭐ 关键认识}✓✓：\ \boxed{\text{Bridge A}\ \textbf{不要求}\ V\ \text{可逆}}✓✓ \ —— \ \text{它只要求}\ \textbf{16 个符号点}\ V\sigma\ \textbf{全部} \text{远离}\ \ell_\infty\ \text{球}✓✓$$
$$\textbf{⑥ 两条证书}✓✓：\textbf{B1（Vandermonde-conditioned）}✓：\text{证}\ D(x) \ge d_0 > 0✓ \ \textbf{再}证\ \sigma_{\min}(V) \ge c_0 > \tfrac12✓✓（\textbf{最漂亮但要求极强}✓）；$$
$$\qquad \textbf{B2（直接 discrepancy）}✓✓：\textbf{不要求} V\ \text{可逆}✗✓，\ \text{直接证}\ \min_{\sigma \in \mathcal S}\|V(x)\sigma\|_\infty > \tfrac12\ \text{on}\ E_{\mathrm{even}}✓✓ \ —— \ \textbf{这才是真正对应}\ C\text{-}380\text{-}7\ \text{的原命题}✓✓$$
$$\textbf{⑦ } E_{\mathrm{deg}}\ \text{单独成精确分支}✓✓：E_{\mathrm{deg}} = E_0 \cup E_{\mathrm{coll}}✓；\ E_0 = \{x : \exists j,\ x_j = 0\}✓；\ E_{\mathrm{coll}} = \{x : \exists i < j,\ x_i = x_j\}✓✓$$
$$\qquad \text{分别问}\ E_{\mathrm{even}} \cap E_0 = \varnothing\ ?✓ \ \text{与}\ E_{\mathrm{even}} \cap E_{\mathrm{coll}} = \varnothing\ ?✓✓ \ —— \ \textbf{不能}用\ C\text{-}368\ \text{的}\ \mathcal Z \cap E\ \text{结论代替}✗✓$$
$$\qquad \textbf{若任一非空反而是好事}✓✓：\text{节点数下降／符号结构简化}✓ \Longrightarrow \text{可能直接得}\ \max_{r \le 4}|F_{2r+1}| > \tfrac12\ \text{的}\ \textbf{低维精确证书}✓✓$$

## §1 优先级（✓✓）

$$\boxed{E_{\mathrm{deg}} \ \longrightarrow\ \inf D(x) \ \longrightarrow\ \begin{cases} \text{uniform}\ \sigma_{\min}\ \text{路线}✓ \\ \text{直接 discrepancy 路线}✓ \end{cases}}✓✓$$
$$\textbf{而非} \text{现在就去算}\ \sigma_{\min}✗✓ \ —— \ \textbf{关键价值}✓✓：C\text{-}380\text{-}9\ \text{可能}\ \textbf{很快判死} \text{「uniform}\ \sigma_{\min}\text{」这条漂亮路线}✓✓$$
$$\qquad \Longrightarrow \ \textbf{避免} \text{又做一轮无效优化}✓✓；\ \text{若判活}✓ \Longrightarrow \text{才值得进入}\ \textbf{定量奇异值证书}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}7` ✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}8` ✓ | **REGISTERED** ✓✓ |
| **`C\text{-}380\text{-}9`（退化层／定量分离）** ✓ | **OPEN ← 下一刀** ✓✓ |
| `E_{\mathrm{deg}} \cap E_{\mathrm{even}}` ✓ | **尚未闭** ✗✓ |
| `\inf D(x)` ✓ | **OPEN（判死／判活）** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：E_{\mathrm{deg}} \cap E_{\mathrm{even}}\ \text{已闭}✗；\ \text{Bridge A 已闭合}✗；\ \inf D > 0\ \text{已证}✗；\ \text{uniform}\ \sigma_{\min}\ \text{路线可行}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{两处修正为}\ \textbf{措辞／逻辑收紧}✓✓；\ \inf D\ \textbf{未判定}✗✓$$

## §4 边界补充（✓✓）

$$\textbf{措辞纪律}✓✓：\text{以后凡引}\ C\text{-}358／C\text{-}361／C\text{-}368\ \text{的结论}✓，\ \textbf{必须} \text{标明}\ \text{「限定于}\ \mathcal Z\text{」}✓✓，\ \textbf{不得}写成\ E_{\mathrm{even}}\ \text{整体结论}✗✓$$

## §5 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 退化量定量分离 命中文件数=0    :: 
技术词 同源非已清除 命中文件数=0    :: 
技术词 奇异不阻碍歧差 命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
