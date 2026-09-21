已查地图（**先查后写**）：`C-380-11`（**`E_0` 先于 `E_{\mathrm{coll}}`** ✓✓）、`C-358`（**限 `\mathcal Z`** ⚠️✓）、`C-349`（**signed moment** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-12：四节点单位圆幂和负半平面可行性审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① ⚠️ 求和法不能关闭}\ E_0\ \textbf{（提前锁死）}✗✓：\text{六项余弦和的}\ \textbf{全局下界严格大于}\ -2✓✓ \Longrightarrow \text{四点相加}\ > -8✗✓$$
$$\qquad \textbf{不足以}与\ -3\ \text{矛盾}✗✓ \Longrightarrow \textbf{这条最粗的求和法}\ \textbf{不能}直接关闭\ E_0✗✓ \ —— \ \textbf{提前锁死}✓✓，\ \text{避免}\ \textbf{假证书}✗✓$$
$$\textbf{② } E_0\ \text{层的精确形式}✓✓：x_5 = 0✓，\ y_j = 2x_j - 1 = \cos\theta_j✓ \Longrightarrow T_{2k}(y_j) = \cos(2k\theta_j)✓✓ \Longrightarrow \text{偶频约束}\ \sum_{j=1}^{4}\cos(2k\theta_j) + 1 \le \tfrac12✓$$
$$\qquad \Longrightarrow \ \boxed{\sum_{j=1}^{4}\cos(2k\theta_j) \le -\tfrac12,\qquad k = 1, \dots, 6}✓✓$$
$$\textbf{③ ⭐ 正确刀（本档核心）}✓✓：\text{令}\ z_j = e^{2i\theta_j}✓ \Longrightarrow \text{条件成为}\ \boxed{\Re\sum_{j=1}^{4}z_j^k \le -\tfrac12,\qquad k = 1, \dots, 6}✓✓$$
$$\qquad \Longrightarrow \ \textbf{四点单位圆幂和问题}✓✓：\textbf{只有 4 个节点}✓，\ \textbf{却要求前 6 个幂和全部落在同一}\ \textbf{严格负半平面}✓✓$$
$$\textbf{④ } C\text{-}380\text{-}12\text{-}A\ \text{（第一目标）}✓✓：\text{精确审计}\ \boxed{\{z_1, \dots, z_4 \in S^1 : \Re\sum_jz_j^k \le -\tfrac12,\ k = 1, \dots, 6\} = \varnothing\ ?}✓✓$$
$$\qquad \textbf{若成立}✓✓ \Longrightarrow \ \boxed{E_{\mathrm{even}} \cap E_0 = \varnothing}✓✓ \ —— \ \textbf{完全独立于}\ C\text{-}368\ \text{的}\ \mathcal Z\text{-分支}✓✓$$
$$\qquad \Longrightarrow \textbf{不再}发生\ \text{「把}\ \mathcal Z\ \text{上的边界结论搬到整个}\ E_{\mathrm{even}}\text{」}\ \text{的问题}✗✓$$
$$\textbf{⑤ ⭐ Newton 四阶递推}✓✓：p_k = \sum_{j=1}^{4}z_j^k✓ \Longrightarrow \text{从}\ p_1, p_2, p_3, p_4\ \text{起满足}\ \textbf{四阶线性递推}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不是}任意六维不等式系统✗✓ \ —— \ \text{背后只有}\ \textbf{4 个单位圆节点}✓✓ \Longrightarrow \text{比直接对}\ y_1, \dots, y_4\ \text{做半代数消元}\ \textbf{更有结构性}✓✓$$
$$\textbf{⑥ ⭐ 纪律（关键）}✗✓：\textbf{不要把「幂和递推只有四个自由节点」本身当成矛盾}✗✓ \ —— \ \textbf{它只是把问题压缩了}✓✓$$
$$\qquad \Longrightarrow \ \textbf{真正的矛盾仍需精确推出}✓✓$$
$$\textbf{⑦ } E_{\mathrm{coll}}\ \textbf{暂时不碰}✓✓：\text{只在}\ E_0\ \text{得明确判定后}✓ \text{再进入}\ x_1 = x_2✓✓；\ \text{继续保持}\ C\text{-}380\text{-}11\ \text{锁死的二分}✓✓$$
$$\qquad \textbf{尤其}✗✓：\textbf{不能}因\ E_0\ \text{若被关闭}\ \textbf{就顺手声称所有退化层都关闭}✗✓$$
$$\textbf{⑧ 工具优先级}✓✓：\ \boxed{\text{单位圆幂和} \to \text{Newton 四阶递推} \to \text{精确不等式}}✓✓ \ \textbf{而非} \text{随机搜索／优化／}\sigma_{\min}／D(x)✗✓$$

## §1 求和法的失效（✓✓，锁死细节）

$$\textbf{六项余弦和}✓✓：\sum_{k=1}^{6}\cos(k\phi) = \frac{\sin(13\phi/2)}{2\sin(\phi/2)} - \frac12✓✓（\textbf{不是}\ -\tfrac12\ \text{作下界}✗✓）$$
$$\qquad \text{其}\ \textbf{全局下界严格大于}\ -2✓✓ \Longrightarrow \text{对}\ \phi = 2\theta_j✓：\sum_{k=1}^{6}\cos(2k\theta_j) > -2✓✓$$
$$\qquad \Longrightarrow \text{四节点相加}\ \sum_{j=1}^{4}\sum_{k=1}^{6}\cos(2k\theta_j) > -8✗✓ \ \textbf{不足以}与\ -3\ \text{矛盾}✗✓$$
$$\textbf{教训}✓✓：\text{「看似漂亮但常数不够」}\ \text{的证书}\ \textbf{必须提前排除}✗✓$$

## §2 收益（✓✓）

$$\textbf{若}\ E_0\ \text{成功关闭}✓✓ \Longrightarrow \ \text{马上获得实质资产}\ \boxed{x_j > 0\ \ \forall j,\quad x \in E_{\mathrm{even}}}✓✓$$
$$\qquad \Longrightarrow \textbf{随后才有资格} \text{讨论紧性给出的}\ \textbf{正距离}✓✓，\ \text{并继续处理}\ \textbf{真正困难的 collision 层}✓✓$$
$$\textbf{注意}✗✓：\text{「}\ x_j > 0\ \text{在}\ E_{\mathrm{even}}\ \text{上成立」}\ \ne\ \text{「}\ \inf x_j > 0\ \text{已量化」}✗✓（\text{后者须紧性论证}✓）$$

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}7` ✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}10` ✓ | **STRUCTURAL CLOSED** ✓✓ |
| `C\text{-}380\text{-}11` ✓ | **REGISTERED／OPEN** ✓✓ |
| **`C\text{-}380\text{-}12`** ✓ | **NEXT ← 本档注册** ✓✓ |
| `E_0` ✓ | **OPEN（求和法已判不足）** ⚠️✓ |
| `E_{\mathrm{coll}}` ✓ | **OPEN（暂不碰）** ✗✓ |
| `\inf D` ✓ | **DEFERRED** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §4 边界（✓✓）

$$\textbf{不得}写成✗：E_{\mathrm{even}} \cap E_0 = \varnothing\ \text{已证}✗；\ \text{求和法给出证书}✗；\ \text{四节点自由度为矛盾}✗；\ \text{所有退化层已关闭}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{四节点系统}\ \textbf{未判定}✗✓；\ \text{求和法失效为}\ \textbf{已定位}✓✓$$

## §5 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 四节点幂和  命中文件数=0    :: 
技术词 负半平面可行性 命中文件数=0    :: 
技术词 求和法不足  命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
