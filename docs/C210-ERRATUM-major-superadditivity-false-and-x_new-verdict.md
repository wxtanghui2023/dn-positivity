已查地图（**先查后写**）：查 `C-203`／`C-205`／`C-206`（局部刚性三档）、`C-207`（乙-4）、`C-209`（CENSUS-2）。回查见 §7 ✓

D0: 本档对象 = **重大勘误**（局部刚性推导中的假步骤）＋ **$x_{\rm new}$ 判定** ＋ 更正后的协议 —— 关系 = 勘误（附修正版陈述）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 ⚠️ 勘误 E1（重大）：局部刚性推导中的假步骤

$$\text{我在}\ \texttt{C-203}\ \text{／}\ \texttt{C-205}\ \text{／}\ \texttt{C-206}\ \text{中使用了：}\qquad \max_k(a_k+b_k)\ \ge\ \max_k a_k+\max_k b_k\qquad ✗✗\ \textbf{这是假的}✓$$
$$\qquad \textbf{正确}：\max\ \text{对和是【次可加】}✓：\ \max_k(a_k+b_k)\ \le\ \max_k a_k+\max_k b_k✓；\text{可用的下界是}\ \boxed{\max_k(a_k+b_k)\ \ge\ \min_k a_k+\max_k b_k}✓✓$$
$$\qquad \text{（证}：取\ k^*=\arg\max b\ \Longrightarrow\ a_{k^*}+b_{k^*}=a_{k^*}+\max b\ \ge\ \min a+\max b✓\ \blacksquare）$$

$$\textbf{数值反证}（x_{\rm new},\ A=\{2,7,10,15\},\ \delta=x_3-x_{\rm new}）:$$
$$\qquad \langle\nabla S_k(x_{\rm new}),\delta\rangle：k{=}2:+2.938913\times10^{-6}✓；k{=}7,10,15:\mathbf{-6.6488\times10^{-6}}✓$$
$$\qquad \max a+\max b=0.775540540481+2.939\times10^{-6}=0.775543479✓；\text{而实际}\ \max(a+b)=0.775533891735✓$$
$$\qquad \Longrightarrow \textbf{假步骤被直接推翻}✗✗（\text{差}\ 9.6\times10^{-6}✓）$$

$$\Longrightarrow \boxed{\ \texttt{C-203}\ \text{／}\ \texttt{C-205}\ \text{／}\ \texttt{C-206}\ \text{的刚性界【需更正】}✗✓\ }$$
$$\qquad \text{⚠️ 唐先生}\ §\text{C}\ \text{中【保留】的}\ \Delta_{A,j}\ \text{项（active-value mismatch）正是我错误丢掉的项}✓✓$$

## §1 ⭐ 更正后的局部刚性（正确陈述）

$$\text{设}\ A\ \text{为容差型 active 集（含 argmax）✓},\ \delta_A:=F(x)-\min_{k\in A}S_k(x)✓（\textbf{active spread}✓）,\ c\ \text{为 covering 常数}✓,\ R=\max_{k\in A}k^2✓$$
$$\text{则（对}\ \|\delta\|\le\rho_{\rm iso}✓\text{）：}$$
$$\qquad F(x+\delta)\ \ge\ \underbrace{F(x)-\delta_A}_{\min_{k\in A}S_k(x)}+\ c\|\delta\|\ -\ \tfrac R2\|\delta\|^2✓✓$$
$$\qquad \Longrightarrow \textbf{严格线性上升当}\ c\|\delta\|-\tfrac R2\|\delta\|^2\ >\ \delta_A✓ \Longleftrightarrow \|\delta\|\in(\rho_{\rm lower},\ \rho_{\rm upper}]✓$$
$$\qquad \text{其中}\ \rho_{\rm lower}=\frac{c-\sqrt{c^2-2R\delta_A}}{R}✓,\qquad \rho_{\rm upper}=\min\Big(\rho_{\rm iso},\ \frac cR\Big)✓$$

$$\textbf{与原文的差别}：\text{原声明}\ (0,\rho_{\rm upper}]\ \text{上严格上升}✗ \Longrightarrow \text{更正为}\ (\rho_{\rm lower},\rho_{\rm upper}]✓；\text{区间}\ (0,\rho_{\rm lower}]\ \textbf{未证}✗（\text{但该区间内}\ F\ \text{的跌幅被}\ \delta_A\ \text{控制}✓）$$

## §2 ⭐ 更正后的三实例

| 簇 | $A$ | $\delta_A$ | $\rho_{\rm lower}$ | $\rho_{\rm upper}$ | $c$ | $R$ |
|---|---|---|---|---|---|---|
| **0** | $\{1,5,11,13\}$ | $9.269\times10^{-8}$ | $1.716\times10^{-7}$ | $1.466\times10^{-3}$ | $0.540247961$ | 169 |
| **3** | $\{2,7,10,15\}$ | $1.603\times10^{-12}$ | $1.316\times10^{-12}$ | $2.050\times10^{-4}$ | $1.218503802$ | 225 |
| **5** | $\{1,3,13,15\}$ | $3.440\times10^{-12}$ | $4.584\times10^{-12}$ | $1.858\times10^{-3}$ | $0.750466653$ | 225 |

$$\textbf{数值验证}✓：\text{每簇 1500 个随机}\ \delta\ \text{（覆盖}\ \rho_{\rm upper}\ \text{内多个半径）} \Longrightarrow \textbf{违反 0 次}✓✓$$
$$\qquad \textbf{实质影响很小}✓：\rho_{\rm lower}\le1.7\times10^{-7}✓（\text{可忽略尺度}✓）；\delta_A\le9.3\times10^{-8}✓$$

## §3 ⭐ $x_{\rm new}=0.7755405405$ 的判定：**cluster 3 的未收敛副本** ✓✓

$$\text{四项核验}：$$
$$\textbf{①}\ d_{S_3}(x_{\rm new},x_3)=\mathbf{1.283971\times10^{-6}}✓,\qquad |\Delta F|=6.648785\times10^{-6}✓$$
$$\textbf{②}\ \text{active set 随容差变化}✗：\ \mathrm{tol}\le10^{-6}\Rightarrow A=\{7,10,15\}✓（|A|=3✓）;\ \mathrm{tol}=10^{-5}\Rightarrow A=\{2,7,10,15\}✓$$
$$\qquad \text{关键}：k{=}2\ \text{的 gap}：x_{\rm new}\ \text{为}\ 9.588\times10^{-6}✓\ \text{vs}\ x_3\ \text{为}\ \mathbf{0.000e+00}✓✓ \Longrightarrow k{=}2\ \text{在}\ x_{\rm new}\ \textbf{并非活跃}✗$$
$$\textbf{③}\ \text{KKT 重新证书}：\text{紧容差}\ A=\{7,10,15\}\ \text{下直接数值}\ c=\mathbf{-5.1737<0}✓ \Longrightarrow \textbf{存在下降方向}✗$$
$$\qquad （\text{容差}\ 10^{-5}\ \text{下的}\ \lambda>0\ \text{只是"人工四元组"的凸组合}✓，\text{不构成}\ F\ \text{的 KKT 条件}✗）$$
$$\textbf{④}\ \text{高精度重精修（9 次含抖动）}：\text{最低}\ F=0.775533933632✓,\ \text{到}\ x_3\ \text{距离}=\mathbf{3.442\times10^{-8}}✓✓ \Longrightarrow \textbf{回到 cluster 3}✓✓$$
$$\textbf{⑤ 自洽性检验（决定性）}：d=1.284\times10^{-6}<\rho_{\rm iso}=2.053\times10^{-4}✓ \Longrightarrow x_3\ \text{在}\ x_{\rm new}\ \text{的刚性球内}✓$$
$$\qquad \text{但}\ F(x_3)<F(x_{\rm new})✗ \Longrightarrow \textbf{与刚性矛盾}✗ \Longrightarrow x_{\rm new}\ \text{不是真局部极小}✓✓$$

$$\boxed{\ \textbf{判定}：x_{\rm new}\ \text{是}\ \text{cluster 3}\ \text{的【未收敛副本】}✓✓\ \Longrightarrow\ N_{\rm Type-A}=\mathbf{3}\ \text{已确认}✓;\ N_{\rm candidate}=4\ \text{（第 4 个已解决}✓）\ }$$

## §4 由此得到的【协议修正】（重要）

$$\textbf{① active 集取法}：\text{不得用固定}\ 10^{-5}\ \text{容差}✗；\text{容差须与【候选点收敛质量】匹配}✓（\text{否则未收敛点会被误标为}\ |A|=4✓✓）$$
$$\textbf{② 入口判据}：|A|=4\wedge\mathrm{rank}\Delta=3\wedge c>0✓ \Longrightarrow \text{须【追加】}\delta_A\ \text{项}✓，\text{且}\ \rho_{\rm lower}<\rho_{\rm upper}\ \text{才有效}✓$$
$$\textbf{③ 推荐的免容差判据}：\textbf{自洽性检验}✓（\text{若某点}\ y\ \text{满足}\ F(y)<F(x)\ \text{且}\ d(x,y)<\rho_{\rm upper}(x)✓ \Longrightarrow x\ \text{非极小}✓✓）$$
$$\qquad \text{该检验【与容差无关】}✓✓，\text{本档用它一举定案}✓$$
$$\textbf{④ 去重}：\text{多起点输出必须【轨道级去重】}✓（A\ \text{相同}＋d_{S_3}\ \text{小}＋重精修落点相同 ✓），\textbf{不能按}\ F\ \text{值计数}✗✓$$

## §5 对既有结论的影响面

$$\texttt{C-203}\ \text{／}\ \texttt{C-205}\ \text{／}\ \texttt{C-206}：\text{定量界更正}✗（\text{见 §2}✓）；\textbf{定性结论保留}✓（\text{三簇仍为严格局部极小，只是成立区间从}\ (0,\rho_{\rm upper}]\ \text{缩为}\ (\rho_{\rm lower},\rho_{\rm upper}]✓）$$
$$\texttt{C-207}\ \text{（连续族排除）}：\text{论证用}\ \max_{k\in A}\ \text{（容差型）}✗ \Longrightarrow \text{须改为}\ \textbf{精确 active 集}✓；\text{在【真极小点】处四项精确相等}✓ \Longrightarrow \text{论证有效}✓；\text{在【有理化点】处同等差}\sim10^{-10}✓ \Longrightarrow \text{结论不变但须注明}✓$$
$$\texttt{C-208}\ \text{／}\ \texttt{C-209}：\text{判据更正}✗（\text{§4}✓）；\textbf{四项硬输出不变}✓（\text{第 4 项为重复}✓✓）$$

## §6 边界

- §1 的更正陈述为**初等推导**✓（正确不等式 ✓）；§2 的数值验证是**检验**不是证明 ✓
- §3 的判定经**三条独立证据**支持 ✓（同 $A$／$d_{S_3}$／重精修落点 ✓＋自洽性矛盾 ✓）
- ⚠️ **不**声称 $m_3$ 精确值 ✗；**不**声称只有 3 个极小 ✗（$\texttt{C-209}$ 的协议内限定仍有效 ✓）
- **未用** RH；**未改** 他档原文（勘误以本档为准 ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 次可加更正   命中文件数=1    ::  ./C210-ERRATUM-major-superadditivity-false-and-x_new-verdict.md
技术词 active spread 命中文件数=1  ::  ./C210-ERRATUM-major-superadditivity-false-and-x_new-verdict.md
技术词 未收敛副本   命中文件数=1    ::  ./C210-ERRATUM-major-superadditivity-false-and-x_new-verdict.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 本档自我失误（第 28–29 次同类应验）

$$\textbf{① 假步骤}：\text{把}\ \max\ \text{当超可加}✗（\text{实为次可加}✓） \Longrightarrow \text{刚性界漏掉}\ \delta_A\ \text{项}✗✓\ \text{—— 唐先生原稿保留了该项，是我丢的}✓$$
$$\textbf{② 判据脆弱}：\text{用固定容差}\ 10^{-5}\ \text{定}\ |A|✗ \Longrightarrow \text{把未收敛点标为 Type-A}✗✓ \Longrightarrow \text{改用自洽性检验}✓✓$$
