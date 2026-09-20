已查地图（**先查后写**）：查 `C-203`（乙-0）、`C-204`（乙-1）、`C-205`（乙-2）、`C-197`（区间模块范式）、`C-189`（facet 法先例）。回查见 §6 ✓

D0: 本档对象 = **T13-A 乙-3**：把三实例提升为**严格区间局部刚性模块**（四层 A/B/C/D 抽象命题 ＋ 三实例常数）—— 关系 = 新构造（可复用证明模块）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 四层结构（唐先生规定的分层，本档严格执行）

$$\textbf{A. active 隔离}：k\notin A\Rightarrow S_k(x_j)\le F(x_j)-\Delta_j✓,\ \text{配 Lipschitz}\ L_{j,\rm non}\Rightarrow\rho_{j,\rm iso}\le\Delta_j/L_{j,\rm non}✓$$
$$\textbf{B. 一阶凸包}：\exists\lambda_k\ge0,\ \sum\lambda_k=1,\ \Big\|\sum\lambda_k\nabla S_k\Big\|\le\varepsilon_j✓ \Longrightarrow c_j>0✓\ ——\ \textbf{定理写成允许}\ \varepsilon_j\ \text{的形式}✓✓$$
$$\textbf{C. 二阶}：\|\nabla^2S_k\|_2\le R_j✓（\text{用最粗界}✓）$$
$$\textbf{D. 拼接}：\rho_j\le\min(\rho_{j,\rm iso},\ c_j^{\rm cert}/R_j)✓ \Longrightarrow 0<\|\delta\|\le\rho_j\Rightarrow F(x_j+\delta)\ge F(x_j)+\tfrac{c_j^{\rm cert}}2\|\delta\|>F(x_j)✓✓$$

## §1 ⭐ 抽象命题（可复用模块）

$$\text{设}\ S_k(x)=\sum_{j=1}^{M}\cos(kx_j)✓,\ F=\max_{1\le k\le K}S_k✓,\ x\in\mathbb R^M✓。\text{若在}\ x_0\ \text{处}：$$
$$\textbf{(A)}\ \exists A\subseteq\{1,\dots,K\}：\Delta:=\min_{k\in A}S_k(x_0)-\max_{k\notin A}S_k(x_0)>0✓,\ L_{\rm non}:=\max_{k\notin A}k\sqrt M✓,\ L_{\rm act}:=\max_{k\in A}k\sqrt M✓$$
$$\textbf{(B)}\ c:=\min_{\|u\|=1}\max_{k\in A}\langle\nabla S_k(x_0),u\rangle>0✓\qquad\textbf{(C)}\ R:=\max_{k\in A}k^2✓$$
$$\text{则}\ 0<\|\delta\|\le\rho:=\min\Big(\frac{\Delta}{L_{\rm non}+L_{\rm act}},\ \frac{c}{2R}\Big)\ \Longrightarrow\ \boxed{\ F(x_0+\delta)\ \ge\ F(x_0)+\frac c2\|\delta\|\ >\ F(x_0)\ }✓✓$$

$$\textbf{证明骨架}（\text{四步，均为初等}）：$$
$$\text{①}\ \|\delta\|\le\rho_{\rm iso}\Rightarrow\max_k S_k(x_0+\delta)=\max_{k\in A}S_k(x_0+\delta)✓（\text{由}\ |S_k(x_0+\delta)-S_k(x_0)|\le k\sqrt M\|\delta\|✓\text{与}\ \Delta>0✓）$$
$$\text{②}\ \max_k[a_k+b_k]\ge\max_k a_k+\max_k b_k✓（\text{max 超可加}✓）\Longrightarrow\max_{k\in A}[S_k(x_0)+\langle\nabla S_k,\delta\rangle]\ge\max_{k\in A}S_k(x_0)+\max_{k\in A}\langle\nabla S_k,\delta\rangle✓$$
$$\text{③}\ \text{Taylor}：S_k(x_0+\delta)\ge S_k(x_0)+\langle\nabla S_k,\delta\rangle-\tfrac{R}2\|\delta\|^2✓$$
$$\text{④}\ \text{合并}：F(x_0+\delta)\ge\max_{k\in A}S_k(x_0)+c\|\delta\|-\tfrac{R}2\|\delta\|^2✓；\text{又}\ \max_{k\in A}S_k(x_0)=F(x_0)✓（\text{由}\ \Delta>0\ \text{保证 argmax}\in A✓）$$
$$\qquad \|\delta\|\le c/(2R)\Rightarrow c\|\delta\|-\tfrac R2\|\delta\|^2\ge\tfrac c2\|\delta\|✓ \qquad\blacksquare$$

$$\textbf{允许}\ \varepsilon\ \text{的形式}（\text{唐先生要求}）：\text{若只有}\ \big\|\sum\lambda_k\nabla S_k(x_0)\big\|\le\varepsilon✓，\text{则对任意}\ \|u\|=1：$$
$$\qquad \max_{k\in A}\langle\nabla S_k,u\rangle\ \ge\ \sum_k\lambda_k\langle\nabla S_k,u\rangle\ \ge\ -\Big\|\sum_k\lambda_k\nabla S_k\Big\|\ \ge\ -\varepsilon✓ \Longrightarrow c\ \text{的有效下界}=c_{\rm num}-\varepsilon✓✓$$
$$\qquad \text{本档实测}\ \varepsilon=0✓（\text{数值 KKT 残差}\sim3\times10^{-16}✓），\text{但模块**不假设**它为零}✓✓$$

## §2 ⭐ 三实例（严格区间，facet 法）

| 簇 | $A$ | $\vert A\vert$ | $\Delta$ | $L_{\rm non}$ | $L_{\rm act}$ | $\rho_{\rm iso}$ | $c$（区间下端点） | $R$ | $\rho_{\rm fin}$ | $c^{\rm cert}=c/2$ |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | $\{1,5,11,13\}$ | 4 | $7.1085\times10^{-2}$ | $10.3923$ | $22.5167$ | $1.4658\times10^{-3}$ | $0.540247961$ | 169 | $\mathbf{1.4658\times10^{-3}}$ | $0.270123980$ |
| **3** | $\{2,7,10,15\}$ | 4 | $1.0298\times10^{-2}$ | $20.7846$ | $25.9808$ | $2.0502\times10^{-4}$ | $1.218503802$ | 225 | $\mathbf{2.0502\times10^{-4}}$ | $0.609251901$ |
| **5** | $\{1,3,13,15\}$ | 4 | $9.3350\times10^{-2}$ | $20.7846$ | $25.9808$ | $1.8585\times10^{-3}$ | $0.750466653$ | 225 | $\mathbf{1.6677\times10^{-3}}$ | $0.375233327$ |

$$\text{三实例结论}：$$
$$\qquad \text{簇 0}：0<\|\delta\|\le1.4658\times10^{-3}\Rightarrow F\ge F(x_0)+0.27012398\|\delta\|✓$$
$$\qquad \text{簇 3}：0<\|\delta\|\le2.0502\times10^{-4}\Rightarrow F\ge F(x_3)+0.60925190\|\delta\|✓$$
$$\qquad \text{簇 5}：0<\|\delta\|\le1.6677\times10^{-3}\Rightarrow F\ge F(x_5)+0.37523333\|\delta\|✓$$
$$\qquad \text{三例均}\ 0\in\mathrm{int}\,\mathrm{conv}\{\nabla S_k:k\in A\}=\texttt{True}✓；\text{面数}=4✓$$

$$\textbf{严格性来源}：\text{候选点为【有理点】}x_i=\pi p_i/10^{10}✓；\text{仅}\ \pi\ \text{带不确定度}✓（\text{均值形式传播：}|\cos(a\pi)-\cos(a\pi_{\rm mid})|\le a\cdot\delta\pi✓）$$
$$\qquad c\ \text{用}\ \textbf{区间 facet 法}✓：c=\min_{\text{面}}\mathrm{dist}(0,\text{面平面})✓（=|p|/\|n\|✓，\text{全区间}✓）；\text{grid 法连极点覆盖都不可靠}✗（\text{见 §4}）✓$$

## §3 旁支核验：$u^*$ 是否轴对齐（**结论：否**）

| 簇 | $u^*$ | $c$（facet） | 判定 |
|---|---|---|---|
| 0 | $(-0.5515,\ 0.2751,\ -0.7875)$ | $0.540247961$ | **非**轴对齐 ✗ |
| 3 | $(-0.3296,\ 0.7746,\ 0.5398)$ | $1.218503802$ | **非**轴对齐 ✗ |
| 5 | $(-0.7743,\ -0.6194,\ 0.1300)$ | $0.750466653$ | **非**轴对齐 ✗ |

$$\textbf{⚠️ 推翻} \texttt{C-205}\ \text{的观察}：\text{"}u^*=(0,0,1)\ \text{三者相同"是}\ \textbf{坏网格的假象}✗✗（\text{网格配对顺序错}⟹\text{零向量混入}✓，\text{argmin 落在轴上}✓）$$
$$\qquad \Longrightarrow \textbf{幸好唐先生指示"不进定理"}✓✓；\text{本档只声称}\ \inf_{\|u\|=1}\max_{k\in A}\langle\nabla S_k,u\rangle>0✓$$

## §4 本档抓到并修掉的五处自我失误

$$\textbf{① 球面网格配对顺序错}✗：\texttt{np.outer(cos(TS), RR).ravel()}（t,z 序）与 \texttt{np.repeat(ZS,n\_t)}（z,t 序）不匹配 \Longrightarrow 生成非单位向量，含【零向量】$u=0$✓$$
$$\qquad \Longrightarrow \text{网格最小值恒}=0✗ \Longrightarrow c_{\rm num}=0✗（\text{假失败}✓）$$
$$\textbf{② 网格 + Lipschitz 修正在极点不可靠}✗：极点附近【最大弦距】=\sqrt{2\delta z}\approx0.088✓，\text{不是}\ \delta z\approx0.0039✓ \Longrightarrow \text{修正量严重低估}⟹ \text{不严格}✗✗$$
$$\qquad \Longrightarrow \text{改用}\ \textbf{区间 facet 法}✓（\text{精确、廉价、可区间化}✓✓）$$
$$\textbf{③ mpf × iv 零宽区间报错}✗（\texttt{can only create mpf from zero-width interval}）\Longrightarrow \text{标量包成区间}✓$$
$$\textbf{④ active 集贪心判据错}✗：\text{用"}\Delta>0\ \text{即停"}\Longrightarrow A=\{1\}\ \text{单元素}✗ \Longrightarrow \rho_{\rm iso}\sim10^{-11}✗（\text{因有理化点上各活跃值不精确相等，相差}\sim10^{-9}✓）$$
$$\qquad \Longrightarrow \text{正确取法}：A=\{k:S^{\rm hi}_k\ge T-\mathrm{tol}\}\ \textbf{强制含 argmax 候选}\ C\subseteq A✓，\text{并验证}\ \Delta>0✓✓；\text{（约束下} A\ \text{越大}\ c\ \text{越优}✓）$$
$$\textbf{⑤ 此前}\ u^*=(0,0,1)\ \text{为假象}✗（\text{见 §3}）$$
$$\qquad \Longrightarrow \text{①–⑤ 全为实现/取法错，非数学错}✓（\text{第}\ 20\text{–}24\ \text{次同类应验}）✓$$

## §5 边界

- **实例的候选点是数值搜索找到的**✓（但证书中对它们是**精确有理点**✓ ⟹ 结论是**关于这些具体有理点**的严格陈述 ✓）
- ⚠️ **不**声称任一 $x_j$ 是全局极小 ✗；**不**声称 $m_3=F(x_j)$ ✗；账本仍 $\ 0.76\le m_3\le0.764081100903$ ✓
- 严格性依赖：① $x_i=\pi p_i/10^{10}$ 为精确有理 ✓；② 均值形式 $+1\times10^{-80}$ 舍入余量 ✓；③ `mpmath.iv` 的 `sin/cos/sqrt` 正确性 ✓（与 `C-176`／`C-195`／`C-199` 同类假设 ✓）
- $A$ 的**取法**是启发式（tol）✓，但**证书条件**（$C\subseteq A$ 且 $\Delta>0$）是严格验证的 ✓✓
- **未用** RH；**未改** 他档 ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 局部刚性模块   命中文件数=1    ::  ./C206-T13-A-YI-3-rigorous-interval-local-rigidity-module.md
技术词 允许误差形式   命中文件数=1    ::  ./C206-T13-A-YI-3-rigorous-interval-local-rigidity-module.md
技术词 区间facet法    命中文件数=1    ::  ./C206-T13-A-YI-3-rigorous-interval-local-rigidity-module.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 下一步（待唐先生定）

$$\textbf{(甲)}\ \text{把 §1 命题正式写成论文片段}✓（\text{可作为}\ \texttt{rpM}\ \text{稿的"局部刚性模块"一节}✓）$$
$$\textbf{(乙)}\ \text{扩展实例}：\text{对}\ M=3\ \text{其余候选簇批量跑模块}✓（\text{廉价}✓）$$
$$\textbf{(丙)}\ \text{与账本挂接}：\text{用三簇的}\ F(x_j)\ \text{与下界}0.76\ \text{组合出更强的排除性陈述}✗（\text{需要球外覆盖}✗ ⟹ \text{回到丁/全局}）$$
