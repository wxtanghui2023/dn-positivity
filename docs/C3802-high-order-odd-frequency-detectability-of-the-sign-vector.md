已查地图（**先查后写**）：`C-380-1`（**符号层入口** ✓✓；`\operatorname{dist}` NO-GO 纪律 ✓✓）、`C-380-0`（**多项式 NO-GO** ✓✓）、`C-372`（`\operatorname{dist}(E,\mathcal Z) > 0` ✓✓）、`C-349`（四阶 signed moment ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-2：符号向量的高阶奇频可检测性（注册）**，**零计算（唐先生指示暂不计算 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① } C\text{-}380\text{-}1\ \text{保持}\ \textbf{OPEN}✓✓；\ \textbf{暂时不继续计算}✓✓（\text{唐先生指示}✓） \ —— \ \text{本档为}\ \textbf{定位档}✓，\textbf{非}结果档✗✓$$
$$\textbf{② ⭐ 核心压缩（本档核心）}✓✓：\text{Bridge A}\ \text{现已压缩为}\ \boxed{\inf_{x \in E_{\mathrm{even}}}\min_{\sigma \in \mathcal S}\max_{0 \le r \le 12}\Big|\sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)\Big| > \tfrac12}✓✓$$
$$\textbf{③ ⭐ 本质区别}✓✓：\ \boxed{\text{零点分离}\ \ne\ \text{阈值传播}}✓✓ \ —— \ \mathcal Z \cap E_{\mathrm{even}} = \varnothing\ \textbf{已 CLOSED}✓✓，\ \textbf{但不够}✗✓$$
$$\qquad \text{需要的是}\ \textbf{更强的幅度传播}✓✓，\ \textbf{不是} \text{再证一次非零}✗✓$$
$$\textbf{④ 结构性变换}✓✓：\text{记}\ w_j := \sigma_j\sqrt{x_j}✓ \ \text{为}\ \textbf{带固定绝对值的符号向量}✓✓（|w_j| = \sqrt{x_j}✓）；\ \text{奇频测试族}\ \{R_0(x),\dots,R_{12}(x)\}✓$$
$$\qquad \Longrightarrow \ \text{问题变为}\ \boxed{\text{固定}\ |w_j| = \sqrt{x_j} \Longrightarrow \text{某个奇频测试函数必须检测到}\ w}✓✓$$
$$\textbf{⑤ 关键（\textbf{不是}再证}\ w \ne 0✗✓）✓✓：\text{须找}\ \textbf{统一的有限测试族}✓，\ \text{使}\ \textbf{对所有}\ 16\ \text{个符号层}\ \text{都有}\ \max_r|\langle w, R_r(x)\rangle| \ge \Psi(x)✓✓$$
$$\qquad \text{再证}\ \inf_{x \in E_{\mathrm{even}}}\Psi(x) > \tfrac12✓✓$$

## §1 退化检查（防循环 ✓✓）

$$\textbf{触发条件}✓✓：\textbf{若}\ \Psi\ \text{最终只是}\ \textbf{四个低阶 signed moments 的范数}✓ \Longrightarrow \textbf{立即检查} \text{是否退化成}\ C\text{-}372\ \text{的}\ \operatorname{dist}(E, \mathcal Z) > 0✓✓$$
$$\textbf{正面前提}✓✓：\textbf{只有当} \text{它能利用}\ \boxed{r > 3\ \text{的高奇频测试方向}}✓✓ \ \text{才算}\ \textbf{真正的新量}✓✓$$
$$\textbf{最危险的循环（明令禁止）}✓✓：\ \boxed{C\text{-}371 \to C\text{-}372 \to C\text{-}380 \to \text{重新证明}\ \mathcal Z \cap E = \varnothing}✗✓$$

## §2 出口（✓✓）

$$\textbf{A}✓✓：\text{找到}\ \textbf{高阶检测量}✓，\ \text{并能在}\ E_{\mathrm{even}}\ \text{上给出}\ > \tfrac12\ \text{的}\ \textbf{统一下界}✓✓ \Longrightarrow \textbf{Bridge A 真正前进}✓✓$$
$$\textbf{B}✓✓：\text{所有检测量最终}\ \textbf{等价于}\ m = 0,1,2,3\ \text{的 signed moments}✓ \Longrightarrow \textbf{又是}\ \mathcal Z\ \text{的重包装}✗✓ \Longrightarrow \textbf{NO-GO}✓✓$$
$$\textbf{C}✓：\text{只能得到数值分离} \Longrightarrow \textbf{DISCOVERY}✓，\ \textbf{不进主线}✗✓$$

## §3 第一问（✓✓）

$$\boxed{R_0, \dots, R_{12}\ \text{对}\ w = \sigma\sqrt{x}\ \text{是否存在一个超出}\ \textbf{四阶 signed-moment nullspace}\ \text{的统一检测不等式}}✓✓$$
$$\textbf{登记性质}✓✓：\text{本档只}\ \textbf{锁定问题}✓，\ \textbf{不给答案}✗✓；\ \text{任何}\ \Psi\ \text{均未构造}✗✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}1` ✓ | **OPEN（保持）** ✓✓ |
| `C\text{-}380\text{-}2` ✓ | **OPEN（本档注册）** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 阈值传播非零分离 命中文件数=0    :: 
技术词 高阶检测方向 命中文件数=0    :: 
技术词 防循环重证  命中文件数=0    :: 
```
- **零计算** ✗（注册档 ✓，遵唐先生"暂不计算"✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：Bridge A 已闭合 ✗；`\Psi` 已构造 ✗；高阶检测量已存在 ✗；`\mathcal Z \cap E = \varnothing` 重证即算进展 ✗；`H = \varnothing` 已证 ✗
