已查地图（**先查后写**）：查 `C-201`（三簇分类与 λ_min）、`C-203`／`C-205`／`C-206`（局部刚性四层模块）、`C-199`／`C-200`（T13-B2 完整定理）。回查见 §6 ✓

D0: 本档对象 = **T13-A 乙-4**（Type-A 连续族排除）＋ **命名规范**（唐先生 11:21 指示）＋ **T13-B2 封存**—— 关系 = 结构定位 ＋ 命名/封存登记
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 命名与封存（唐先生 2026-09-20 11:21 指示，立即生效）

$$\textbf{① T13-A 正式命名}：\boxed{\ \textbf{"候选极小构型的刚性／连续族审计"}\ }✓✓\ —— \textbf{暂不叫"等号结构"}✗$$
$$\qquad \text{理由}：\text{当前只有}\ 0.76\le m_3\le0.764081100903\ldots✓ \Longrightarrow \textbf{不能} \text{写}\ F(x)=m_3✗，\text{更谈不上}"m_3\ \text{的等号集}"✗$$
$$\qquad \text{研究对象改为}\ \mathcal M_{\rm cand}=\{\text{数值搜索得到的局部极小 Type-A 构型}\}✓$$
$$\textbf{② T13-B2 封存为完整定理}：\qquad\boxed{\ g_2(10)=1✓,\qquad \mathrm{Eq}(g_2)=\{(\pi/3,\ \pi/2)\}\ }✓✓$$
$$\qquad \text{四步链条闭合}：\text{远场严格}>1✓（\texttt{C-199}，丢弃半径\ 0.098✓ \text{解决球面覆盖，实质改进}✓）\ \to\ \text{内层}\ F\ge1✓（\texttt{C-197} 两条 1-D 证书）\ \to\ \text{内层唯一取等}=\text{原点}✓（\texttt{C-200}）$$
$$\qquad \text{与 T13-A 的方法学分界}：\text{T13-B2 有【精确等号集】}✓；\text{T13-A 目前【只有刚性/连续族】}✓✓$$

## §1 ⭐ 乙-4 数据：Type-A 连续族排除

$$\Delta:=\Big[\nabla S_{k}-\nabla S_{k_1}\Big]_{k\in A\setminus\{k_1\}}✓（3\times3\ \text{差分矩阵}✓）$$

| 簇 | $A$ | 奇异值 $(\Delta)$ | $\det\Delta$ | $\mathrm{rank}$ | 条件数 | $\lambda$（KKT 权重） | $\min\lambda$ | 残差 $\|G^{\mathsf T}\lambda\|$ | $c$（facet） |
|---|---|---|---|---|---|---|---|---|---|
| **0** | $\{1,5,11,13\}$ | $(21.615,\ 13.894,\ 8.200)$ | $-2.462\times10^{3}$ | **3 ✓** | 2.64 | $(0.81583,\ 0.10370,\ 0.05442,\ 0.02605)$ | $2.605\times10^{-2}$ | $1.4\times10^{-16}$ | $0.540247961$ |
| **3** | $\{2,7,10,15\}$ | $(23.255,\ 17.143,\ 10.422)$ | $-4.155\times10^{3}$ | **3 ✓** | 2.23 | $(0.69347,\ 0.15418,\ 0.09586,\ 0.05648)$ | $5.648\times10^{-2}$ | $4.6\times10^{-16}$ | $1.218503802$ |
| **5** | $\{1,3,13,15\}$ | $(25.065,\ 18.925,\ 4.066)$ | $-1.929\times10^{3}$ | **3 ✓** | 6.17 | $(0.63767,\ 0.28608,\ 0.03808,\ 0.03817)$ | $3.808\times10^{-2}$ | $1.2\times10^{-16}$ | $0.750466653$ |

$$\textbf{三例均}：\mathrm{rank}\,\Delta=3=M✓（\ker\Delta=\{0\}✓）\Longrightarrow \text{四个活跃梯度【仿射张成}\ \mathbb R^3✓\text{】}\ \Longrightarrow \textbf{一阶可行集为单点}✓✓$$
$$\qquad \text{KKT 权重【唯一】}✓（4\ \text{方程}4\ \text{未知}✓，因}\ \mathrm{rank}\Delta=3✓）；\ \min\lambda>0✓ \Longrightarrow 0\in\mathrm{int}\,\mathrm{conv}\{\nabla S_k:k\in A\}✓✓$$
$$\qquad \textbf{交叉验证}✓：\text{本档线性求解的}\ \min\lambda=2.605\times10^{-2}／5.648\times10^{-2}／3.808\times10^{-2}✓\ \text{与}\ \texttt{C-201}\ \text{的 LP 结果【完全一致}✓✓\text{】}$$
$$\qquad \text{条件数}\ 2.2\sim6.2✓ \Longrightarrow \text{不退化}✓；\text{残差}\sim10^{-16}✓（\text{数值 KKT 几乎精确}✓）$$

## §2 ⭐ 连续族排除（严格论证）

$$\textbf{命题}：\text{若}\ 0\in\mathrm{int}\,\mathrm{conv}\{\nabla S_k:k\in A\}\ \text{且}\ c:=\min_{\|u\|=1}\max_{k\in A}\langle\nabla S_k,u\rangle>0✓，\text{则}\ \textbf{不存在过}\ x_j\ \text{的}\ F\ \text{等值曲线}✓✓$$

$$\textbf{证明}：\text{对任意}\ v\neq0：$$
$$\qquad \max_{k\in A}\langle\nabla S_k,\ v\rangle\ \ge\ c\|v\|\ >\ 0✓\qquad\text{且}\qquad \max_{k\in A}\langle\nabla S_k,\ -v\rangle\ \ge\ c\|v\|\ >\ 0✓$$
$$\qquad （\text{方向导数}\ F'(x_j;v)=\max_{k\in A(x_j)}\langle\nabla S_k,v\rangle✓\text{，用邻近点最大在}\ A\ \text{内}✓）$$
$$\qquad \Longrightarrow F\ \text{沿过}\ x_j\ \text{的【任意直线】两侧都严格上升}✓✓ \Longrightarrow \text{过}\ x_j\ \text{的}\ F\ \text{等值集孤立}✓ \qquad\blacksquare$$

$$\textbf{与}\ \texttt{C-206}\ \text{的拼接}：\text{把本档（}0\in\mathrm{int}\,\mathrm{conv}✓）\ \text{与}\ \texttt{C-206}\ \text{的二阶控制（}R✓）\ \text{合并} \Longrightarrow \textbf{局部孤立性}✓✓$$
$$\qquad \boxed{\ 0<\|\delta\|\le\rho_j\ \Longrightarrow\ F(x_j+\delta)\ \ge\ F(x_j)+\tfrac{c_j}2\|\delta\|\ >\ F(x_j)\ }✓（\rho_j\ \text{见}\ \texttt{C-206}\ §2✓）$$
$$\qquad \text{即}：x_j\ \text{是}\ \textbf{孤立严格局部极小}✓\ \text{且【无局部连续族】}✓✓$$

## §3 唐先生三问的当前回答

$$\textbf{问 1（有限性）}：\text{当前数值搜索得到【有限个】Type-A 轨道（}\ge3✓\text{）}✓；\textbf{但"只有有限个"未被证明}✗（\text{全局问题}✓）$$
$$\qquad \text{已排除的是【每个轨道的局部连续族】}✓✓ \Longrightarrow \text{不存在"一条连续极小族"}✓（\text{那将要求局部等值曲线}✓）$$
$$\textbf{问 2（局部刚性）}：\text{已给}✓（\texttt{C-203}／\texttt{C-205}／\texttt{C-206}）✓$$
$$\textbf{问 3（隐藏连续族／一维自由度）}：\text{已排除}✓✓ —— \mathrm{rank}\,\Delta=M=3✓ \Longrightarrow \text{切空间无零方向}✓；0\in\mathrm{int}\,\mathrm{conv}✓ \Longrightarrow \text{一阶可行集为单点}✓✓$$
$$\qquad \text{⚠️ 唐先生提示}：u^*=(0,0,1)\ \textbf{不升格为结构定律}✗✓（\texttt{C-206}\ §3\ \text{已证其为坏网格假象}✓✓）$$

## §4 边界

- 奇异值/行列式/条件数为**数值**✓；但 $\mathrm{rank}=3$ 是**离散判据**✓（奇异值最小者 $4.07$ ≫ 阈值 ✓ ⟹ 稳健 ✓）
- $c$ 取 `C-206` 的**区间 facet 法**结果 ✓（严格 ✓）
- ⚠️ 本档只给**局部**结论 ✗：**不**声称三个轨道是全部候选 ✗；**不**声称 $m_3$ 精确值 ✗；账本仍 $0.76\le m_3\le0.764081100903$ ✓
- **未用** RH；**未改** 他档 ✓（$\texttt{C-205}$ 的 $u^*$ 观察仅在 $\texttt{C-206}\ §3$ 标注推翻，原文保留 ✓）

## §5 命名规范落地

$$\text{此后 T13-A 相关新档统一用"}\textbf{候选极小构型}\text{"／"}\textbf{刚性}\text{"／"}\textbf{连续族}\text{"词汇}✓；\textbf{避免} \text{"等号结构"}✗（\text{除引用}\ \texttt{C-201}\ \text{旧题名时注明}✓）$$
$$\qquad \text{已有档名不改}✓（\text{项目惯例：不回溯改名}✓），\text{新档遵守新规范}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 连续族排除     命中文件数=1    ::  ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md
技术词 等值曲线       命中文件数=1    ::  ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md
技术词 一阶可行集     命中文件数=1    ::  ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 下一步（待唐先生定）

$$\textbf{(甲)}\ \boxed{\text{三孤立 Type-A 轨道是否为全部候选？}}✓ \Longrightarrow \text{这才是全局问题}✓（\text{唐先生明确指出}✓）$$
$$\qquad \text{可能路径}：\text{对}\ \mathcal M_{\rm cand}\ \text{做【穷尽性】论证}✓（\text{例如分区 ＋ 每区一个局部刚性}✓）\ ——\ \text{即}\ \texttt{C-207}\ \text{之后的"全局分区"✗（此前被你暂缓}✓）$$
$$\textbf{(乙)}\ \text{其余近极小数值簇批量过模块}✓（\texttt{C-206} 脚本已就绪，廉价}✓）\ \Longrightarrow \text{扩充}\ \mathcal M_{\rm cand}\ \text{清单}✓$$
$$\textbf{(丙)}\ \text{不动}：\text{账本冻结}✓ \Longrightarrow \text{等唐先生决定是否进全局}✓$$
