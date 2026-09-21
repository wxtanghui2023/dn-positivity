已查地图（**先查后写**）：`C-380-3`（**`r_* = 4` 首个不可约方向** ✓✓）、`C-349`（四阶 nullspace ✓✓）、`C-347`（`R_r` ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-4：`R_4..R_{12}` 模 `\mathbb R_{\le 3}[x]` 的化简 ＋ `\mu_4` 单一新量判定**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 商空间原理}✓✓：L_x(p) := \sum_j w_j\,p(x_j)✓（w_j = \sigma_j\sqrt{x_j}✓）；\ \text{nullspace 条件}\ L_x(1) = L_x(x) = L_x(x^2) = L_x(x^3) = 0✓✓$$
$$\qquad \Longrightarrow \ L_x(p)\ \text{只依赖}\ p\ \text{模}\ \mathbb{R}_{\le 3}[x]\ \text{的部分}✓✓ \ —— \ \text{故只需}\ R_r\ \text{的}\ \deg \ge 4\ \text{部分}✓✓$$
$$\textbf{② ⭐ 化简表（本档核心，符号确认 ✓✓）}✓✓：a_{r,r} = 2^{2r} \ne 0✓✓ \Longrightarrow \text{每个}\ r\ \text{引入}\ \mu_r\ \text{且系数非零}✓✓$$
$$\qquad r = 4✓：256\mu_4✓✓；\ r = 5✓：1024\mu_5 - 2816\mu_4✓；\ r = 6✓：4096\mu_6 - 13312\mu_5 + 16640\mu_4✓；\ \dots✓（\text{至}\ r = 12✓，\text{完整表见 §1}✓）$$
$$\textbf{③ } \mathfrak c_4 = 256\,\mu_4✓✓：R_4(x) = 256x^4 - 576x^3 + 432x^2 - 120x + 9✓✓ \Longrightarrow \deg \le 3\ \text{部分被吞}✓ \Longrightarrow \boxed{\mathfrak c_4 = 256\,\mu_4}✓✓$$
$$\textbf{④ ⭐ 半整数矩链}✓✓：\ \boxed{\mu_m := \sum_j \sigma_j\,x_j^{m+\frac12} = \sum_j w_j\,x_j^m}✓✓（m \ge 4✓） \ —— \ \textbf{首个未被}\ \mathcal Z\ \text{吞掉的量}✓✓$$
$$\qquad \Longrightarrow \ \mu_0, \mu_1, \mu_2, \mu_3\（\text{被}\ \mathcal Z\ \text{消掉}✓） \to \boxed{\mu_4} \to \mu_5, \mu_6, \dots✓✓$$
$$\textbf{⑤ ⭐⭐ 关键推论（比预期更强）}✓✓：\text{因}\ 5\ \text{节点}✓，\ (\mu_m)_m\ \text{满足}\ \textbf{5 项线性递推}✓✓（\text{特征根} = x_1,\dots,x_5✓）$$
$$\qquad \Longrightarrow \ \text{给定}\ (x, \mu_0, \dots, \mu_4)\ \text{后}\ \textbf{一切}\ \mu_m（m \ge 5）\ \text{被决定}✓✓；\ \text{在 nullspace 上}\ \mu_0 = \dots = \mu_3 = 0✓$$
$$\qquad \Longrightarrow \ \boxed{\text{整体由}\ \textbf{单一}\ \mu_4\ \text{决定}}✓✓ \ —— \ \textbf{不是} \text{无限新量阶梯}✗✓，\ \text{而是}\ \textbf{单一新量}✓✓$$
$$\textbf{⑥ ⚠️ 诚实标注}✓✓：\text{本档递推的}\ \textbf{数值校验代码有索引 bug}✗✓（\text{差}\ 3.88✓，\text{索引方向写反}✓）$$
$$\qquad \Longrightarrow \ \text{递推}\ \textbf{事实} \text{为标准}✓，\ \textbf{但本档未通过数值校验}✗✓ \Longrightarrow \textbf{不得}升格为已证✗✓$$
$$\textbf{⑦ 账本}✓✓：\text{见 §4}✓$$

## §1 化简表（✓✓，符号确认 ✓✓）

$$\textbf{r=0..3}✓：a_{r,r} = 1, 4, 16, 64✓；\ \deg \ge 4\ \text{贡献} = 0✓✓（\text{被 nullspace 吞}✓）$$
$$\textbf{r=4}✓：256\mu_4✓；\ \textbf{r=5}✓：-2816\mu_4 + 1024\mu_5✓；\ \textbf{r=6}✓：16640\mu_4 - 13312\mu_5 + 4096\mu_6✓$$
$$\textbf{r=7}✓：-70400\mu_4 + 92160\mu_5 - 61440\mu_6 + 16384\mu_7✓；\ \textbf{r=8}✓：239360\mu_4 - 452608\mu_5 + 487424\mu_6 - 278528\mu_7 + 65536\mu_8✓$$
$$\textbf{r=9}✓：-695552\mu_4 + 1770496\mu_5 - 2723840\mu_6 + 2490368\mu_7 - 1245184\mu_8 + 262144\mu_9✓$$
$$\textbf{r=10}✓：1793792\mu_4 - 5870592\mu_5 + 12042240\mu_6 - 15597568\mu_7 + 12386304\mu_8 - 5505024\mu_9 + 1048576\mu_{10}✓$$
$$\textbf{r=11}✓：-4209920\mu_4 + 17145856\mu_5 - 44843008\mu_6 + 76873728\mu_7 - 85917696\mu_8 + 60293120\mu_9 - 24117248\mu_{10} + 4194304\mu_{11}✓$$
$$\textbf{r=12}✓：9152000\mu_4 - 45260800\mu_5 + 146227200\mu_6 - 317521920\mu_7 + 466944000\mu_8 - 458752000\mu_9 + 288358400\mu_{10} - 104857600\mu_{11} + 16777216\mu_{12}✓$$
$$\textbf{校验}✓✓：a_{r,r} = 2^{2r}\ \text{对}\ r = 1,\dots,12\ \textbf{全部成立}✓✓$$

## §2 真实新量（✓✓）

$$\mu_m = \sum_j \sigma_j x_j^{m+\frac12}✓ \ —— \ \textbf{非多项式}✓✓（\text{含}\ \sqrt{x_j}✓，\text{与}\ C\text{-}380\text{-}0\ \text{的奇偶性结论}\ \textbf{一致}✓✓）$$
$$\textbf{结构}✓✓：\underbrace{\mu_0, \mu_1, \mu_2, \mu_3}_{\text{被}\ \mathcal Z\ \text{消掉}} \to \underbrace{\mu_4}_{\textbf{首个新量}} \to \mu_5, \dots✓✓$$
$$\textbf{若 ⑤ 成立}✓✓：\text{则}\ \text{奇频向量整体}\ \text{由}\ \mu_4\ \text{与}\ x\ \text{决定}✓✓ \Longrightarrow \ \text{幅度问题}\ \text{降为}\ \textbf{单参数问题}✓✓$$

## §3 下一步（✓✓）

$$\textbf{必做}✓✓：\text{① 修正递推校验的}\ \textbf{索引 bug}✓✓ \ \text{并复核}✓；\ \text{② 若复核通过}✓ \Longrightarrow \text{建立}\ \mu_m\ \text{的}\ \textbf{单参数} \text{表述}✓✓$$
$$\qquad \text{③ 再问}\ \text{幅度}✓：\inf_{x \in E_{\mathrm{even}}}\min_\sigma\max_{4 \le r \le 12}|F_{2r+1}| > \tfrac12\ ?✓✓（\textbf{最后一公里}✓）$$
$$\textbf{禁项}✓✓：\textbf{不}随机搜索✗；\textbf{不}优化✗；\textbf{不}在递推未复核时使用 ⑤✗✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}2`（四阶 nullspace）✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}3`（`r_* = 4`）✓ | **CLOSED** ✓✓ |
| `\mathfrak c_4` 是否统一 `> \tfrac12` ✓ | **OPEN** ✓ |
| 高阶方向是否压缩为半整数矩链 ✓ | **本档：是（化简表确认）；单一性（⑤）待复核** ⚠️✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \text{⑤ 已证}✗（\textbf{待}修正复核✓）；\ \mu_4\ \text{已给出}\ > \tfrac12\ \text{下界}✗；\ H = \varnothing\ \text{已证}✗$$
$$\textbf{诚实标注}⚠️✓：\text{化简表为}\ \textbf{符号确认}✓✓；\ \text{递推数值校验}\ \textbf{失败}（\textbf{本档 bug}✓）✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 半整数矩链  命中文件数=0    :: 
技术词 单一新量     命中文件数=0    :: 
技术词 商空间化简  命中文件数=0    :: 
```
- **本档有计算**（符号＋数值，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
