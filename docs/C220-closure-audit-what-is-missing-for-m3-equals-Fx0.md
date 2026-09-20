已查地图（**先查后写**）：查 `C-219`（夹逼收尾）、`C-218`／`C-217`／`C-216`（四档）、`C-206`／`C-211`（局部刚性三件套）、`C-200`（T13-B2 的 M=2 完整模板）。回查见 §8 ✓

D0: 本档对象 = **数学闭合审计**：从"严格双侧夹逼"到"$m_3=F(x_0^*)$"之间究竟还缺什么 —— 关系 = 结构定位（下一阶段的路线图）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 唐先生的逻辑要点（必须先接受）

$$\boxed{\ \textbf{高精度夹逼【本身】不证明}\ x_0^*\ \text{是极小点}✗，\textbf{更不证明} \text{它是【唯一】全局极小构型}✗✗\ }$$
$$\qquad \text{夹逼只给出关于【数}\ m_3\ \text{】的括号}：m_3\in[0.7640811007458,\ 0.764081100745853885\ldots]✓$$
$$\qquad \textbf{这与"哪个构型取到极小"是两个独立问题}✓✓$$

## §1 已有资产（清点）

$$\textbf{① 双侧严格括号}✓（层 1）：0.7640811007458\le m_3\le0.76408110074585388514756267472105✓,\ \Delta=5.3885\times10^{-14}✓$$
$$\textbf{② 高精度 KKT 点}\ x_0^*\ ✓（\text{层 2}）：140\ \mathrm{dps}✓；\lambda=(0.815828\ldots,0.103702\ldots,0.054415\ldots,0.026054\ldots)✓,\ \min\lambda>0✓,\ \sum\lambda=1✓$$
$$\qquad \text{四个活跃}\ k=\{1,5,11,13\}\ \text{的}\ S_k\ \text{相等到}\ 141\ \text{位}✓；\text{非活跃最大者}\ k=6\ \text{gap}\approx0.0711✓$$
$$\textbf{③ 局部刚性三件套}✓（\text{层 2}）：c=0.540247961✓,\ \delta_A=9.269\times10^{-8}✓,\ \rho_{\rm lower}=1.7157\times10^{-7}✓,\ \rho_{\rm upper}=1.465756\times10^{-3}✓,\ R=169✓$$
$$\qquad \text{免容差自洽性审计通过}✓（\text{球内 50 万点采样 }＋\text{30 点下降均无更低点}✓）$$
$$\textbf{④ 与 KKT 解耦的上界证书}✓（\text{层 1}）：合法有理构型＋有向区间认证＋两条独立实现＋10^{-130}\ \text{slack}✓✓$$

## §2 逐步审计：要推出 $m_3=F(x_0^*)$ 还缺什么

$$\textbf{第 1 步 · 极小点存在性}：\textbf{免费}✓✓\ —— F_3\ \text{在紧集}\ [0,\pi]^3\ \text{上连续} \Longrightarrow \text{最小值【取到】}✓（\text{Weierstrass}✓）$$
$$\qquad \text{即}\ \mathcal M_3:=\arg\min\ \text{非空紧}✓；\text{故}\ m_3\ \text{是 min 而非仅 inf}✓$$

$$\textbf{第 2 步 · 识别极小点}：\textbf{缺}✗\ —— \text{需要【严格】包住真极小点}\ x_0\ \text{（而非只有高精度数值点}\ x_0^*✓）$$
$$\qquad \text{现状态}：x_0^*\ \text{是浮点／高精度解}✗，\text{没有严格包围盒}✗$$
$$\qquad \Longrightarrow \textbf{手段}：\text{对 KKT 六方程系统做}\ \textbf{interval Newton}✓✓（\text{标准技术}✓） \Longrightarrow \text{得严格盒}\ X_0\ni x_0✓$$
$$\qquad \qquad \text{KKT 六方程}=\{\sum_{k\in A}\lambda_k\nabla S_k=0\ (3)✓,\ S_{k_2}=S_{k_1},\ S_{k_3}=S_{k_1},\ S_{k_4}=S_{k_1}\ (3)✓\}✓$$

$$\textbf{第 3 步 · 局部刚性严格化}：\textbf{缺}✗\ —— \text{把层 2 的}\ (c,\text{gap})\ \text{变成区间版}✓（R=k^2\ \text{本就是解析严格}✓✓）$$
$$\qquad \text{① 活跃集隔离}：\text{gap 与 Lipschitz 的区间版}✓；\text{② 一阶凸包}：c\ \text{用区间 facet 法}✓（\text{须【含】containment 证书}\ \lambda>0\ ✓✓，\text{这是}\ \texttt{C-210}\ §4④\ \text{的教训}✓）$$
$$\qquad ⭐\ \textbf{关键红利}：\text{若在【严格盒}\ X_0\text{】上做，则}\ \delta_A=0✓✓\ —— \text{因 KKT 系统【含】相切方程}✓ \Longrightarrow \text{盒内任一点四值精确相等}✓✓$$
$$\qquad \qquad \Longrightarrow \text{内核缺口}\ (0,\rho_{\rm lower}]\ \textbf{自动消失}✓✓（\text{这正是}\ \texttt{C-215}\ §2\ \text{担心的那一层}✓）$$

$$\textbf{第 4 步 · 外侧 B\&B}：\textbf{缺}✗（\text{但便宜}✓） —— \text{在【盒外】以}\ T=F(x_0)\ \text{认证}✓$$
$$\qquad \text{难点}：T\ \text{【恰等于】极小值}✗ ⟹ \text{含极小点的箱永不可认证}✗；\text{但盒外点的}\ F>F(x_0)✓ ⟹ \text{足够深即可认证}✓$$
$$\qquad \qquad \text{（附注：}\texttt{C-216}\ \text{已证"箱数不爆、深度可控"✓ —— 此步预计仍是几千～几万箱}✓）$$

$$\textbf{第 5 步 · 唯一性}：\textbf{由第 4 步自动得到}✓✓\ —— \text{盒外}\ F\ge F(x_0)✓、\text{盒内}\ F>F(x_0)\ \text{除}\ x_0\ \text{本身}✓$$
$$\qquad \Longrightarrow \boxed{\mathcal M_3=x_0\ \text{的}\ S_3\ \text{轨道}}✓（\text{唯一到置换}✓；\text{注意}\ \varphi_j\mapsto\pi-\varphi_j\ \textbf{不是}对称✗，\text{因}\ S_k\mapsto(-1)^kS_k✓）$$

## §3 缺口清单（一句话版）

$$\boxed{\ \textbf{缺三件}：\text{(a) 极小点的【严格盒】（interval Newton on KKT}✓）；\text{(b) 盒内局部刚性的【区间版】（}c,\text{gap}✓）；\text{(c) 盒外}\ \text{B\&B}\ \text{以}\ T=F(x_0)✓\ }✓✓$$
$$\qquad \textbf{不缺}：\text{存在性（免费}✓）；\text{上界证书（已有}✓）；R\ \text{的严格性（解析}✓）；\text{数量级直觉（四档已验证}✓）$$
$$\qquad ⚠️\ \textbf{高精度夹逼对等式证明【没有直接贡献】}✗ —— \text{它只把"}\ m_3\ \text{是几"确定到}\ 10^{-14}✓，\text{不告诉我们"谁取到"}✗✓$$

## §4 与 M=2（T13-B2 成功模板）的对照

| 环节 | M=2（已完整 ✓） | M=3（现状） |
|---|---|---|
| 局部引理 | 精确等号集 $\{(\pi/3,\pi/2)\}$ ✓ | 层 2 三件套，待区间化 |
| 局部球内 | 两条 1-D 证书（$f_I,f_{II}\ge0$）✓ | 待建（interval Newton ＋ 区间 c） |
| 远场 | 网格 ＋ Lipschitz 证书 ✓ | 四档 B&B 已验证可行 ✓ |
| 等号集 | 单点（证明 ✓✓） | 未证 ✗ |

$$\Longrightarrow \text{M=2 的路线}\ \textbf{完全可移植}✓✓\ —— \text{差别只在 M=3 的局部结构是【非退化单纯形】而非 1-D 显式不等式}✓$$

## §5 本档边界

- 本档是**路线图／审计**✓，**不含**新定理 ✗；§2 的各项"缺"均为**待建**✓
- 第 2 步的 interval Newton、第 3 步的区间 $c$、第 4 步的外侧 B&B 均**未实施** ✗
- ⚠️ **不**声称 $m_3=F(x_0^*)$ ✗；**不**声称 $x_0^*$ 唯一极小 ✗
- ⚠️ 丙（全域 cover）**仍不开** ✓
- **未用** RH；**未改** 他档 ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 数学闭合审计 命中文件数=1    ::  ./C220-closure-audit-what-is-missing-for-m3-equals-Fx0.md
技术词 严格盒       命中文件数=1    ::  ./C220-closure-audit-what-is-missing-for-m3-equals-Fx0.md
技术词 相切方程     命中文件数=1    ::  ./C220-closure-audit-what-is-missing-for-m3-equals-Fx0.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 §0 要点复述（防误用）

$$\text{严格双侧夹逼}\ \neq\ \text{极小值定理}✗✗；\qquad \text{数值接近}\ \neq\ \text{等式证明}✗$$
$$\qquad \text{当前状态}：\text{全局下界数值推进}\to\textbf{证书收尾问题}✓（\text{已收尾}✓）；\ \text{等式／唯一性}\to{}\textbf{未开工}✗$$

## §8 建议的施工顺序（待唐先生定）

$$\textbf{(A)}\ \text{第 3 步先做}✓：\text{把层 2 三件套做成【区间版】}✗⟹✓ \Longrightarrow \text{层 1 增厚}✓（\text{风险低、可复用}✓）$$
$$\textbf{(B)}\ \text{第 2 步}：\text{interval Newton 求严格盒}\ X_0✓ \Longrightarrow \text{同时干掉}\ \delta_A\ \text{缺口}✓✓$$
$$\textbf{(C)}\ \text{第 4 步}：\text{盒外 B\&B @}\ T=F(x_0)✓ \Longrightarrow \text{唯一性一并到手}✓✓$$
$$\textbf{(D)}\ \text{合并} \Longrightarrow \boxed{m_3=F(x_0)✓,\ \mathcal M_3=x_0\ \text{的}\ S_3\ \text{轨道}}✓✓$$
