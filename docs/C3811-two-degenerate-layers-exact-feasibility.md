已查地图（**先查后写**）：`C-380-10`（**同号／异号二分** ✓✓）、`C-380-9`（**`D(x)`** ✓✓）、`C-380-7`（**低奇频可行性** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-11：`E_0` 与 `E_{\mathrm{coll}}` 两类退化层的精确可行性审计（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}10\ \text{收档}✓✓：\textbf{STRUCTURAL CLOSED}✓✓ \ —— \ \textbf{未作任何未注册计算}✓✓$$
$$\textbf{② ⭐ 先打边界}\ E_0✓✓：\text{固定}\ x_5 = 0✓，\ \text{令}\ y_j = 2x_j - 1 \in [-1,1]✓（j = 1..4✓） \Longrightarrow S_r = F_{2r} = \sum_{j=1}^{4}T_r(y_j) + (-1)^r✓✓$$
$$\qquad \text{要求}\ \sum_{j=1}^{4}T_r(y_j) + (-1)^r \le \tfrac12✓（r = 1, \dots, 12✓） \Longrightarrow \textbf{奇偶交替}✓✓：$$
$$\qquad \begin{cases} r\ \textbf{偶}✓：\sum_{j=1}^{4}T_r(y_j) \le -\tfrac12✓✓（\textbf{负约束}✓） \\ r\ \textbf{奇}✓：\sum_{j=1}^{4}T_r(y_j) \le \tfrac32✓✓ \end{cases} \Longrightarrow \textbf{尤其}\ r = 2, 4, 6, \dots\ \text{给出一串}\ \textbf{四节点负约束}✓✓$$
$$\textbf{③ 判定标准}✓✓：\text{若能精确证}\ \boxed{E_{\mathrm{even}} \cap E_0 = \varnothing}✓✓ \Longrightarrow \textbf{非常有价值}✓✓ \ —— \ \text{随后可得}\ x_j > 0\ \text{on}\ E_{\mathrm{even}}✓✓$$
$$\qquad \text{再结合}\ E_{\mathrm{even}}\ \text{的闭性／紧性}✓ \Longrightarrow \textbf{才有资格} \text{进一步推}\ \textbf{显式}\ \varepsilon_0✓✓$$
$$\qquad \textbf{注意}✗✓：\textbf{仍不要}把「没有零点」\ \textbf{直接}写成已经有数值\ \varepsilon_0✗✓$$
$$\textbf{④ ⭐ 后打 collision}\ E_{\mathrm{coll}}✓✓：\text{固定}\ x_1 = x_2 = t✓ \ —— \ \textbf{直接使用}\ C\text{-}380\text{-}10\ \text{的精确二分}✓✓，\ \textbf{不要}重新枚举两符号层✗✓$$
$$\qquad \textbf{分支 C（同号}\ \sigma_1 = \sigma_2✓）✓✓：\text{奇频等价于一个权重}\ \pm 2\sqrt{t}\ \text{的节点}✓ ＋ \text{其余三节点}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{4 个有效节点}✓，\ \textbf{其中一个权重不是}\ \pm\sqrt{x}\ \textbf{而是}\ \pm 2\sqrt{t}✓✓$$
$$\qquad \textbf{分支 D（异号}\ \sigma_1 = -\sigma_2✓）✓✓：w_1 + w_2 = 0✓ \Longrightarrow \ \boxed{F_{2r+1} = \sum_{j=3}^{5}\sigma_j\sqrt{x_j}\,R_r(x_j)}✓✓\ \textbf{对一切}\ r = 0, \dots, 4\ \textbf{恒等成立}✓✓$$
$$\qquad \qquad \text{而 even 侧仍是}\ 2T_r(2t - 1) + \sum_{j=3}^{5}T_r(2x_j - 1) \le \tfrac12✓✓ \Longrightarrow \ \boxed{\text{3-node odd null-like structure} + \text{4-node weighted even constraints}}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{比原问题低维得多、但仍完整的 exact feasibility problem}✓✓$$
$$\textbf{⑤ 判定树}✓✓：\textbf{只允许四种结果}✓：\ \boxed{E_0 \cap E_{\mathrm{even}} = \varnothing}✓ \ \text{或}\ \boxed{E_0 \cap E_{\mathrm{even}} \ne \varnothing \Longrightarrow \text{直接关闭该边界层的 odd discrepancy}}✓✓$$
$$\qquad \text{collision 同理}✓，\ \textbf{但拆成}\ C_{\mathrm{same}}✓ \ \text{与}\ C_{\mathrm{opp}}✓✓ \ —— \ \textbf{尤其}✓✓：\ \boxed{C_{\mathrm{opp}} = \{x_1 = x_2,\ \sigma_1 = -\sigma_2\}}\ \textbf{应单独注册}✓✓$$
$$\qquad \textbf{不能}用「collision 已处理」一句话覆盖✗✓$$
$$\textbf{⑥ ⭐ 停止条件（采纳）}✓✓：\text{若} C_{\mathrm{opp}} \ne \varnothing✓ \ \textbf{且} \text{存在}\ \max_{0 \le r \le 4}|F_{2r+1}| \le \tfrac12✓ \Longrightarrow \textbf{立即登记}✓✓：$$
$$\qquad \boxed{C\text{-}380\text{-}7\ \text{在低奇频层}\ \textbf{确有退化障碍}}✓✓ \Longrightarrow \textbf{停止 Vandermonde／B1 路线}✗✓，\ \textbf{不再}继续研究\ \sigma_{\min}✗✓$$
$$\qquad \textbf{反之}✓✓：\text{若所有退化分支都被排除或直接得到}\ > \tfrac12✓ \Longrightarrow \text{才进入}\ E_{\mathrm{gen}} \Longrightarrow \text{是否存在定量}\ D(x) > 0\ ?✓✓$$
$$\textbf{⑦ 路线}✓✓：\ \boxed{C\text{-}380\text{-}11 \to \begin{cases} \text{退化层关闭}✓ \\ \text{退化层留下真实障碍}✓ \end{cases} \to \text{再决定 B1／B2}✓}✓✓$$

## §1 纪律（✓✓）

$$\textbf{本档只做}✓✓：\text{两个退化层的}\ \textbf{精确可行性／排除审计}✓✓$$
$$\textbf{不}计算\ D✗；\textbf{不}算\ \sigma_{\min}✗；\textbf{不}碰\ F_{11} - F_{25}✗✓；\textbf{不}随机搜索✗✓$$
$$\textbf{顺序}✓✓：\ \boxed{E_0\ \textbf{先于}\ E_{\mathrm{coll}}}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}7` ✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}8` ✓ | **REGISTERED** ✓✓ |
| `C\text{-}380\text{-}9` ✓ | **OPEN** ✓ |
| `C\text{-}380\text{-}10` ✓ | **STRUCTURAL CLOSED** ✓✓ |
| **`C\text{-}380\text{-}11`** ✓ | **NEXT ← 本档注册** ✓✓ |
| `E_{\mathrm{deg}} \cap E_{\mathrm{even}}` ✓ | **OPEN** ✓ |
| `\inf D` ✓ | **DEFERRED** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：E_0 \cap E_{\mathrm{even}} = \varnothing\ \text{已证}✗；C_{\mathrm{opp}} \ne \varnothing\ \text{已证}✗；\ \text{退化层已关闭}✗；\ \inf D > 0\ \text{已证}✗；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ \text{四结果}\ \textbf{均未取得}✗✓；\ \text{奇偶交替与异号恒等式为}\ \textbf{精确结构}✓✓（\text{非}数值✗）$$

## §4 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 边界（✓✓）

$$\textbf{承接纪律}✓✓：\text{凡引}\ C\text{-}358／C\text{-}361／C\text{-}368／C\text{-}380\text{-}10\ \text{的结论}✓，\ \textbf{必须}标明适用范围✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 退化层可行性判定树 命中文件数=0    :: 
技术词 异号三节点  命中文件数=0    :: 
技术词 停止条件登记 命中文件数=0    :: 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
