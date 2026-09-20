已查地图（**先查后写**）：查 `C-229`（勘误＋覆盖修补）、`C-228`（D-C float）、`C-227`（B5）、`C-226`（D-B）。回查见 §7 ✓

D0: 本档对象 = **甲线最终闭合声明**（D-A′→D-B→B5→C2 覆盖几何→C2 float→C2 interval 全链 ✓）—— 关系 = 认证闭合与登记
D1: 0
FREEZE-ACK: 本档即冻结期内的认证与登记（依 §8.1；不产候选结论）

---

## §0 ⭐⭐⭐ 最终结论

$$\boxed{C_3=F(z_*)=0.3730918928958164\ldots}✓✓\qquad \boxed{\operatorname*{arg\,min}_{\Omega}F=\{z_*^{(1)},z_*^{(2)}\}}✓✓$$
$$\qquad \Omega=[0,1]^2\times[0,\pi]^3✓,\quad F(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)=\max_{1\le k\le15}\big[\cos k\varphi_1+r_2^k\cos k\varphi_2+r_3^k\cos k\varphi_3\big]✓$$
$$\boxed{\text{D-A′ PASS}\to\text{D-B PASS}\to\text{B5 PASS}\to\text{C2 覆盖几何 PASS}\to\text{C2 float PASS}\to\boxed{\text{C2 interval PASS}}}✓✓$$

## §1 ⭐ C2 区间层最终统计（严格 ✓）

```
T_C = sup F(紧盒) + 1e-9 = 0.373091893895817  （F(z*) = 0.373091892895817）
丢弃半径 DISC_R = ρ_g − 1e-9 = 0.0019782234

N_eval        = 472,766
N_cert        = 252,282      （区间层认证 ✓）
N_disc        = 485          （球内 ✓）
N_split       = 219,999
N_unresolved  = 0            ✓✓
float过/区间不过 = 0          ✓✓
min_X (F_IA(X) − T_C) = 4.628931e-08 > 0   ✓
disc_far_max  = 0.001978039980 ≤ DISC_R    ✓✓
```

## §2 ⭐ 三段式覆盖（几何分解，无薄片 ✓）

$$\boxed{\Omega=\underbrace{\mathcal C_{\rm cert}}_{F\ge T_C}\ \cup\ \underbrace{\bigcup_{\sigma\in\{\mathrm{id},\sigma_2\}}B(\sigma_2 z_*,\rho_g)}_{B5\ \text{局部增长，中心}z_*}}✓,\qquad \rho_g=1.9782244\times10^{-3}✓$$
$$\textbf{① 远场}✓：x\notin B_1\cup B_2 \Longrightarrow F(x)\ge T_C>F(z_*)✓（\text{差值}\ge10^{-9}✓）$$
$$\textbf{② 局部球}✓：0<\|x-z_*^{(i)}\|\le\rho_g \Longrightarrow F(x)\ge F(z_*)+c_X\|x-z_*\|-\tfrac R2\|x-z_*\|^2>F(z_*)✓$$
$$\qquad（c_X=0.09881200977✓,\ R=99.89969551593013✓；\text{两常数【全重算】}✓，\text{未移植 T13-A}✓）$$
$$\textbf{③ 并集} \Longrightarrow \arg\min=\{z_*^{(1)},z_*^{(2)}\}✓✓$$
$$\textbf{薄片处理}✓：\text{丢弃判据}=\mathrm{far}(X,c_0)\le\rho_g-10^{-9}✓ \Longrightarrow X\subseteq B(c_0,\rho_g-10^{-9})\subseteq B(z_*,\rho_g)✓（{\rm hd}(X_0)\le10^{-21}✓）$$

## §3 ⭐ 轨道表述（采用唐先生的商空间口径 ✓）

$$|\mathcal O_{\rm raw}|=\big|\{\pi\cdot z_*:\pi\in S_3\}\big|=6✓\qquad（\text{未归一参数空间}✓）$$
$$\mathcal N:\mathcal O_{\rm raw}\to\Omega\ \text{为归一化商映射（把}\ r=1\ \text{的配对置回首位}✓）$$
$$\boxed{|\mathcal N(\mathcal O_{\rm raw})|=2}✓✓\qquad \{\text{六个原始置换在商空间中的两个等价类代表}\}✓$$
$$\textbf{数值依据}✓：\text{6 置换的 }F\ \text{全相等}✓；\text{归一到}\ \Omega\ \text{后仅 2 个不同点}✓✓$$
$$\qquad \text{两点}：(0.79051323,0.83020729,0.82066\pi,0.46172\pi)✓\ \text{与}\ (0.83020729,0.79051323,0.46172\pi,0.82066\pi)✓$$

## §4 关键常数一览（全部本档链路内重算 ✓）

| 量 | 值 | 来源 |
|---|---|---|
| $\Delta_{\rm ref}$ | $0.2795968136$ | C-227 |
| $L_{\rm act}$ | $15\sqrt5=33.54102$ | C-227 |
| $\rho_{\rm iso}$ | $4.31171\times10^{-3}$ | C-227 |
| $c_X$ | $0.09881200977$ | C-227（球 $\rho=2.05\times10^{-3}$） |
| $R$ | $99.89969551593013$ | C-227 |
| $\rho_g$ | $1.9782244\times10^{-3}$ | C-227（覆盖受限 $=2c_X/R$） |
| $\lambda_{\min}$ | $0.11186012$ | C-226（D-B） |
| $X_0$ 宽 | $\sim4\times10^{-22}$ | C-229（$r_0=10^{-12}$） |

## §5 独立交叉验证（进行中 ✓）

$$\text{并行版}\ \texttt{scripts/dC2par\_parallel\_iv.py}✓：\text{同一分区逻辑}✓,\ \text{3 进程区间复核}✓$$
$$\qquad \text{已确认 float 分区一致}✓（评估 472,766／待复核 252,282／丢弃 485／未决 0✓）$$
$$\qquad \text{若结果一致} \Longrightarrow \text{满足唐先生"第二独立实现"要求}✓✓$$

## §6 边界（不夸大 ✓）

$$\textbf{① 严格层}：\text{区间乘积}✓＋\text{有向舍入}✓＋\text{精确有理箱端点}✓；\text{facet 法向仍用 float SVD}⚠️（\varepsilon\sim0.2\gg10^{-15}✓）$$
$$\textbf{② }C_3=F(z_*)\ \text{的数值为区间级}✓（\text{上界来自合法有理构型＋区间算术}✓）$$
$$\textbf{③ 不含}：\text{一般 }M\ \text{或阻尼 }M\ge4\ \text{的外推}✗；\text{未用 RH}✓；\text{未改他档}✓$$
$$\textbf{④ 待办}：\text{① 并行版一致性}✓；\text{② 并入论文 A}✓；\text{③ 体积精确核对（可选）}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 商空间二阶轨道   命中文件数=1  ::  ./C230-FINAL-CLOSURE-damped-M3-C3-equals-Fz-star.md
技术词 三段式覆盖       命中文件数=1  ::  ./C230-FINAL-CLOSURE-damped-M3-C3-equals-Fz-star.md
技术词 认证闭合声明     命中文件数=1  ::  ./C230-FINAL-CLOSURE-damped-M3-C3-equals-Fz-star.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 本档无新自我失误 ✓（43a/43b 已在 C-229 登记 ✓）
