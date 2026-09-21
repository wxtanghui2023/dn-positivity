已查地图（**先查后写**）：`C-375`（**16 层覆盖问题** ✓✓）、`C-374`（`E_{\mathrm{even}}` **薄** ⚠️✓）、`C-342`（`x_j` 语言 ✓✓）、`C-336`（**幂和单调性** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-376：低阶 Chebyshev／矩约束 ⟹ 全局几何压缩审计**，**有计算（符号核验 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 幂矩改写核验通过}✓✓（symmetric exact✓）：\ y_j := 2x_j - 1 \in [-1,1]✓，\ p_m := \sum_j y_j^m✓，\ S_r := \sum_j T_r(y_j)✓$$
$$\qquad S_1 = p_1 \le \tfrac12✓；\ S_2 = 2p_2 - 5 \le \tfrac12 \Longrightarrow p_2 \le \tfrac{11}{4}✓✓；\ S_3 = 4p_3 - 3p_1 \le \tfrac12✓；\ S_4 = 8p_4 - 8p_2 + 5 \le \tfrac12 \Longrightarrow \boxed{p_4 \le p_2 - \tfrac{9}{16}}✓✓$$
$$\textbf{② ⭐ 精确 } p_2\ \textbf{夹逼}✓✓：p_4 \ge \tfrac{p_2^2}{5}✓（Cauchy✓） \Longrightarrow p_2^2 - 5p_2 + \tfrac{45}{16} \le 0✓ \Longrightarrow \text{根}\ \tfrac52 \pm \tfrac{\sqrt{55}}{4}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\tfrac{10-\sqrt{55}}{4} \le p_2 \le \tfrac{11}{4}}✓✓（\text{左端} = 0.645950378226084✓；\text{右根} = 4.3540 > \tfrac{11}{4}✓ \Longrightarrow \textbf{上端仍由}\ \tfrac{11}{4}\ \text{控制}✓✓）$$
$$\textbf{③ ⭐ 方差缺口恒等式（\textbf{精确}✓✓）}✓✓：\ \boxed{p_4 - \tfrac{p_2^2}{5} = \tfrac15\sum_{i<j}\big(y_i^2 - y_j^2\big)^2}✓✓（\text{符号差值} = 0✓） \ —— \ \textbf{五元}\ y_j^2\ \text{的不均匀度}✓✓$$
$$\textbf{④ } E_{\mathrm{even}}\ \text{给的窗口}✓✓：0 \le p_4 - \tfrac{p_2^2}{5} \le f(p_2) := p_2 - \tfrac{9}{16} - \tfrac{p_2^2}{5}✓✓；\ f\ \textbf{凹}✓，\ f' = 1 - \tfrac{2p_2}{5}✓ \Longrightarrow \text{驻点}\ p_2 = \tfrac52✓$$
$$\qquad f\big(\tfrac52\big) = \tfrac{11}{16} = 0.6875✓✓（\textbf{最大}✓）；\ f\big(\text{左端}\big) = 0✓✓；\ f\big(\tfrac{11}{4}\big) = \tfrac{27}{40} = 0.675✓$$
$$\textbf{⑤ ⭐ 端点强制}✓✓：p_2 = \tfrac{10-\sqrt{55}}{4} \Longrightarrow \text{缺口} = 0 \Longrightarrow \textbf{一切}\ y_j^2\ \text{相等}✓✓ \Longrightarrow \boxed{y_j = \pm c✓，\ c^2 = 0.129190075645217✓，\ |c| = 0.359430209700321}✓✓$$
$$\qquad \textbf{结构含义}✓✓：\textbf{单模双值} \text{构型}✓ \ —— \ \textbf{符号仍自由}✓ ⟹ \textbf{16 层的来源}✓✓（与 C-374 对接✓）$$
$$\textbf{⑥ 诚实结论}✓✓：\text{压缩是}\ \textbf{部分的}✓ \ —— \ gap \in [0, 0.6875]✓ \ \textbf{不}在整区间强制均匀✗✓ \Longrightarrow \textbf{「}E_{\mathrm{even}}\ \text{很薄」仍为}\ \textbf{数值观察}✗✓ \Longrightarrow \text{须}\ \textbf{更高阶} \text{约束}（r = 5,\dots,12✓）\ \text{或}\ S_3／p_3\ \text{链}✓✓$$

## §1 核验记录（✓✓）

$$\textbf{Chebyshev 幂矩式}✓✓：S_1 = p_1✓；\ S_2 = 2p_2 - 5✓；\ S_3 = 4p_3 - 3p_1✓；\ S_4 = 8p_4 - 8p_2 + 5✓（\text{核验差} = 0✓）$$
$$\textbf{倒二层恒等}✓✓：S_{2r} = 2\sum_j T_r(y_j)^2 - 5✓，\ r = 1,2,3,6\ \text{皆核验为} 0✓✓（\text{因}\ T_{2r}(y) = 2T_r(y)^2 - 1✓）$$
$$\textbf{推论}✓✓：S_{2r} \le \tfrac12 \Longrightarrow \sum_j T_r(y_j)^2 \le \tfrac{11}{4}✓；\ \text{与}\ S_r = \sum_j T_r(y_j) \le \tfrac12✓ \ \text{联立}✓（\text{待挖掘}✓）$$
$$\textbf{方差恒等}✓✓：\tfrac15\sum_{i<j}(y_i^2 - y_j^2)^2 - \big(p_4 - \tfrac{p_2^2}{5}\big) = 0✓✓$$

## §2 待挖掘链（✓✓，登记 ✓）

$$\textbf{链 1}✓：S_3 = 4p_3 - 3p_1 \le \tfrac12 \Longrightarrow p_3 \le \tfrac{\tfrac12 + 3p_1}{4}✓；\ \text{与}\ p_2\ \text{夹逼合并可再压}✓（\textbf{未展开}⚠️✓）$$
$$\textbf{链 2}✓：S_1 = p_1 \le \tfrac12✓ \ \text{与}\ p_2 \ge \tfrac{p_1^2}{5}✓（Cauchy✓） \Longrightarrow p_1 \le \sqrt{5p_2}✓（\text{在} p_2 \in [0.646, 2.75]\ \text{上为} 1.80 \sim 3.71✓，\textbf{不}紧✗✓）$$
$$\textbf{链 3}✓：\text{对每个}\ r✓：\sum_j a_j \le \tfrac12✓，\ \sum_j a_j^2 \le \tfrac{11}{4}✓，\ a_j = T_r(y_j) \in [-1,1]✓ \ \text{且}\ a_j\ \textbf{来自同一组}\ y_j✓✓（\textbf{非}自由变量✗✓）$$
$$\qquad \Longrightarrow \ \text{可尝试}\ S_{2r} \le \tfrac12 \Longrightarrow S_r \le c_r✓ \ \text{或反向}\ S_r \le c \Longrightarrow S_{2r} \ge \Psi_r(c)✓✓（\text{待审计}✓）$$

## §3 三出口（✓✓，唐先生口径 ✓）

$$\textbf{A 成功}✓✓：\text{证某组低阶矩／方差不等式} \Longrightarrow E_{\mathrm{even}} \subseteq \bigcup_{\nu=1}^{N}\mathcal S_\nu✓（\text{每个}\ \mathcal S_\nu\ \textbf{由已证必要条件得到}✓✓） \Longrightarrow \text{再进入}\ 16\ \text{层}✓✓$$
$$\textbf{B 部分成功}✓✓：\text{证}\ \max_j x_j - \min_j x_j \le C✓ \ \text{或}\ \sum_{i<j}(x_i - x_j)^2 \le C✓，\ \text{但}\ C\ \textbf{不足以} \text{形成有限 strata}✗✓$$
$$\qquad \Longrightarrow \ \text{Bridge A 转为}\ \boxed{\text{几何压缩} \to \text{signed moments} \to G_\sigma > \tfrac12}✓✓$$
$$\textbf{C 失败但有价值}✓✓：\text{若连}\ p_2, p_4\ \text{都不能显著压缩几何自由度}✗ \Longrightarrow \textbf{「}E_{\mathrm{even}}\ \text{很薄」是数值观察，非代数事实}✓✓$$
$$\qquad \Longrightarrow \ \textbf{须} \text{转向更强的}\ r = 1,\dots,12\ \text{Chebyshev／Hankel／矩约束}✓✓，\ \textbf{不}硬做 active-set 分类✗✓$$

## §4 禁项（✓✓）

$$\textbf{不}再跑\ 40000／100000\ \text{个随机}\ x✗✓；\ \textbf{不}从某个新优化点直接宣布\ \{r_1, r_2, r_3\}\ \text{为 active}✗✓（\text{C-339 教训}✓）$$
$$\textbf{不}直接启动\ 16\ \text{个五维 interval branch-and-bound}✗✓ \ —— \ \text{若}\ E_{\mathrm{even}}\ \text{尚无结构压缩，覆盖预算会变成纯计算工程}✓✓$$

## §5 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `\mathcal Z \cap E = \varnothing` ✓ | **CLOSED** ✓✓ |
| `\delta_* > 0` ✓ | **CLOSED（存在性）** ✓✓ |
| 16 sign layers ✓ | **DISCOVERY 完成** ✓✓ |
| `2.19 \sim 2.56` ✓ | **仅数值证据** ⚠️ |
| `E_{\mathrm{even}}` 完整几何结构 ✓ | **OPEN（本档给第一层压缩）** ✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 低阶矩压缩  命中文件数=0    :: 
技术词 方差缺口     命中文件数=0    :: 
技术词 单模双值构型 命中文件数=0    :: 
技术词 强制活跃链  命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 核验九项 ✓，`/tmp` 未留 ✓）
- **本档有计算**（符号核验，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：`p_2` 夹逼**只是二阶矩方向**的压缩 ✓，**不**构成薄到低维的证明 ✗✓；`f` 的窗口**宽达** `0.6875` ✓ ⟹ **未强制均匀** ✗✓
- **不得**写成：`E_{\mathrm{even}}` 已被压缩到有限 strata ✗；Bridge A 已闭合 ✗；`H = \varnothing` 已证 ✗；active set 已确定 ✗
