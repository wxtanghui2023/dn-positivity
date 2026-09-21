已查地图（**先查后写**）：`C-350`（**决定性等价 `\mathcal Z \cap E \ne \varnothing \Rightarrow H \ne \varnothing`** ✓✓；`Z` 未分类 ✓）、`C-348`（反称成本 1.4677 ✓）、`C-349`（抵消理想 ✓✓）、`C-336`（矩不等式 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-351：`\mathcal Z \cap E` 审计（三分裂）**，**零计算（解析）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 审计口径}✓✓：\text{只问}\ \mathcal Z \cap E\ \text{是否为空}✓；\text{按}\ 2+2／4+1／3+2\ \text{分裂}✓ \ —— \ \textbf{3+2 为唯一核心}✓✓$$
$$\textbf{② 2+2 分支}✓✓：\text{已证}\ \{a_1,a_2\} = \{b_1,b_2\}✓（C-350 §2✓）\ \Longrightarrow \textbf{即反称族}✓ \Longrightarrow \text{偶频成本}\ \ge 1.4677✗（C-348✓）\ \Longrightarrow \not\subset E✓✓$$
$$\textbf{③ 4+1 分支}✓✓：\text{单原子匹配四矩} \Longrightarrow \text{权重为 0}✓ \Longrightarrow \textbf{已排除}✓✓（C-350✓）$$
$$\textbf{④ 3+2 部分解析}✓：\text{已得两个可证结构（§3／§4}✓）\ \text{但}\ \textbf{统一偶频下界未得}✗✓$$
$$\textbf{⑤ 判定}⚠️：\textbf{未}\ \text{得到}\ \mathcal Z \cap E = \varnothing✓，\textbf{亦未}\ \text{找到反例}✗✓ \Longrightarrow \text{须}\ \text{显式参数化}\ 3+2\ \text{族}✓（\text{一维}✓）$$

## §1 三分裂框架（✓✓）

$$\text{非零}\ y_j := \sqrt{x_j} > 0✓，\text{按符号分}\ p + q = 5✓；\text{零奇矩条件}✓：\sum_{i=1}^{p} a_i^{2m+1} = \sum_{j=1}^{q} b_j^{2m+1}✓（m = 0,1,2,3✓）$$
$$\textbf{等价}✓：\sum_{i \le p} a_i^{r} = \sum_{j \le q} b_j^{r}✓（r = 1,3,5,7✓）\ \Longrightarrow \text{全部奇频}\ F_{2r+1} = 0✓✓$$
$$\textbf{偶频}✓：F_{2r} = \sum_{i \le p} T_{2r}(a_i) + \sum_{j \le q} T_{2r}(b_j)✓（\text{与符号无关}✓）$$

## §2 2+2 与 4+1（✓✓）

$$\textbf{2+2}✓✓：\text{两侧均二元}✓ \Longrightarrow \text{前四阶幂和相等} \Longrightarrow \textbf{多重集相等}✓✓ \Longrightarrow \text{反称族}✓ \Longrightarrow \text{成本}\ \ge 1.4677✗✓ \Longrightarrow \textbf{排除}✓✓$$
$$\textbf{4+1}✓✓：\text{四元对一元四矩匹配} \Longrightarrow \text{一元测度的矩必须重组出四阶结构}✓ \Longrightarrow \text{权重}\ 0✓ \Longrightarrow \textbf{排除}✓✓$$

## §3 3+2：两条可证结构（✓✓）

$$\textbf{结构一（Cauchy--Schwarz 下界）}✓✓：m := \sum_{i \le 3} a_i = \sum_{j \le 2} b_j✓（r = 1✓）；\text{则}\ \sum_{i \le 3} a_i^2 \ge \tfrac{m^2}{3}✓，\ \sum_{j \le 2} b_j^2 \ge \tfrac{m^2}{2}✓$$
$$\qquad \Longrightarrow \ \sum_j c_j^2 \ge \tfrac{5m^2}{6}✓ \Longrightarrow F_2 = 2\sum_j c_j^2 - 5 \ \ge \ \tfrac{5m^2}{3} - 5✓✓$$
$$\qquad \Longrightarrow \ F_2 \le \tfrac12\ \textbf{要求}\ m \le \sqrt{3.3} \approx \textbf{1.817}✓✓ \Longrightarrow \textbf{大质量直接出界}✓$$
$$\textbf{结构二（小原子极限被 }F_4\text{ 排除）}✓✓：a_i, b_j \to 0✓ \Longrightarrow \text{矩条件}\ 0 = 0✓\ \text{仍满足}✓，\text{但}\ F_{2r} \to 5(-1)^r✓$$
$$\qquad \Longrightarrow \ F_4 \to \textbf{+5}✗（> \tfrac12✗）\ \Longrightarrow \textbf{退化小原子极限不在}\ E✓✓ \ —— \ \text{这}\ \textbf{排除了} \text{「全小」逃逸}✓✓$$
$$\textbf{结构三（散布强制）}✓：\text{由}\ r = 3\ \text{匹配}✓：\sum_{j \le 2} b_j^3 = \sum_{i \le 3} a_i^3✓；\text{二元侧最大}\ m^3✓（\text{集中于一元}✓）\ \Longrightarrow \text{3+2 配置}\ \textbf{必然散布}✓✓$$

## §4 未闭合处（✗✓）

$$\textbf{缺口}✗✓：\text{3+2 族}\ \textbf{一维}✓（五未知、四条件✓），\text{但}\ \text{「散布」}\ \text{与}\ \sum_j c_j^2 \le \tfrac{11}{4}✓\ \text{是否矛盾} \ \textbf{未证}✗✓$$
$$\textbf{进一步}✗：\text{高偶频}\ F_6, F_8, \dots\ \text{的联合约束}\ \textbf{未纳入}✓ \ —— \ \text{仅用}\ F_2／F_4\ \text{不足}✗✓$$
$$\Longrightarrow \ \textbf{建议}✓：\text{显式参数化}\ 3+2\ \text{族}✓（\text{一维}✓）\ \text{并沿该族}\ \text{核算}\ \max_{r \le 12} F_{2r}✓ \ —— \ \text{这是}\ \textbf{定向结构计算}✓，\textbf{不是}\ \text{盲搜索}✗✓$$

## §5 判死标准（唐先生预设 ✓）

$$\textbf{若}✓：\text{3+2 上可得}\ \max_{r \le 12} F_{2r} \ge c_0 > \tfrac12✓ \Longrightarrow \mathcal Z \cap E = \varnothing✓✓ \Longrightarrow \textbf{比 Bridge A 强得多}✓✓（\textbf{不需}\ \text{知道}\ \mathcal Z\ \text{邻域形状}✓）$$
$$\textbf{若}✓：\text{连}\ 3+2\ \text{都无可控结构}✗ \Longrightarrow \text{再决定}\ \text{是否做}\ Bridge\ A✓$$
$$\textbf{禁止}✓✓：\textbf{不}\ \text{做成}\ Bridge\ A\ \text{再发现不需要}✗；\textbf{不}\ \text{扩频率}✗；\textbf{不}\ \text{拆}\ SOS✗；\textbf{不}\ \text{做全 25 频盲搜索}✗$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 分裂分类     命中文件数=0    :: 
技术词 幂均值        命中文件数=0    :: 
技术词 散布强制     命中文件数=0    :: 
技术词 质量下界     命中文件数=0    :: 
```
- **零计算** ✗（解析 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal Z` 已分类 ✗；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；3+2 已排除 ✗
