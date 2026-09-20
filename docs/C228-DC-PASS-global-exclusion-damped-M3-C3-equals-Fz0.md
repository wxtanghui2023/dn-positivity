已查地图（**先查后写**）：查 `C-227`（B5）、`C-226`（D-B）、`C-225`（D-A′）、`C-224`（T13-A C 严格模板）。回查见 §7 ✓

D0: 本档对象 = **甲 D-C：阻尼 M=3 的全局排除**（五维混合域 B&B ＋ 两点球覆盖）—— 关系 = 全局最小性认证
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与登记（依 §8.1；不产候选结论）

---

## §0 ⭐⭐⭐ 结论：链闭合

$$\boxed{\textbf{D-A′ PASS}\to\textbf{D-B PASS}\to\textbf{B5 PASS}\to\textbf{D-C PASS}}✓✓$$
$$\boxed{C_3=F(z_0)=0.3730918928958164248599364\ldots}✓✓\qquad \boxed{\mathcal M_3=\{z_0,\ \sigma z_0\}}✓（\text{两点的}\ C_2\ \text{轨道}✓）$$
$$\qquad \sigma:(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)\mapsto(r_3,r_2,\varphi_1,\varphi_3,\varphi_2)✓$$

## §1 ⭐ 对称结构的更正（重要 ✓）

$$\text{原设}：\text{"}S_3\ \text{只置换三个}\ \varphi_j\text{，不置换}\ r_2,r_3\text{"}\ ✗\ \text{被证否}$$
$$\textbf{数值反例}✓：F(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)=0.373091892895817\quad\neq\quad F(r_2,r_3,\varphi_2,\varphi_1,\varphi_3)=1.126876598534850$$
$$\qquad \text{差}\ 0.7538\ \text{⟹ 量级级证否}✓；\textbf{正确对称群}\ C_2\ \text{【配对互换}】✓：F(\sigma z_0)=F(z_0)✓（\text{实测相等}✓）$$
$$\textbf{原因}✓：r_1=1\ \text{由最大模归一化固定} \Longrightarrow (1\leftrightarrow2)\ \text{置换把}\ r_2<1\ \text{推到位置 1}✗，\text{再归一化后回到同一点}✓$$
$$\Longrightarrow \text{轨道在}\ \Omega\ \text{中只有 2 点}✓✓（\text{不是 6 点}✗） \Longrightarrow \text{D-C 只需排除 2 个球}✓$$

## §2 D-C 设置

$$\Omega=[0,1]^2\times[0,\pi]^3✓（5\ \text{维}✓，r_1=1✓）；\quad \mathcal C=\Omega\setminus\bigcup_{\sigma\in C_2}B_\sigma(\rho_{\rm up})✓,\quad \rho_{\rm up}=1.9782244\times10^{-3}✓$$
$$T_C=\sup F(X_0)+\varepsilon=0.373094479990555✓ > F(z_0)=0.373091892895817✓✓$$
$$\textbf{目标}：\forall X\subset\mathcal C\ \text{box}:\ \inf F(X)>T_C✓；\text{不能证明就只能 split}✓\（\text{unresolved}\neq\text{certified}✓）$$

## §3 ⭐ 两层结构（依 T13-A C 阶段惯例 ✓）

$$\textbf{C0 diagnostic}（float✓）：评估\ 472{,}988✓，认证\ 252{,}385✓，球内丢弃\ 493✓，分裂\ 220{,}110✓，\textbf{未决 0}✓，frontier\ 清零✓$$
$$\qquad \text{认证最小余量}=1.819877\times10^{-7}✓；\text{与历史 5 维运行（409k 箱）同量级}✓ \Longrightarrow \text{workload 可控}✓$$
$$\textbf{C1 strict}（\text{float 分区}＋\text{逐终端箱【区间复核}】✓）：$$
$$\qquad N_{\rm eval}=472{,}988✓\quad N_{\rm cert}=252{,}385✓\quad N_{\rm split}=220{,}110✓\quad N_{\rm disc}=493✓\quad \boxed{N_{\rm unresolved}=0}✓✓$$
$$\qquad \text{float 通过但区间不通过}=0✓✓（\text{即 float 分区未被区间层推翻}✓）$$
$$\qquad \min_X(\inf F(X)-T_C)=1.819877\times10^{-7}>0✓✓$$

## §4 42a 纪律的显式守护（本轮重点 ✓）

$$\textbf{被加项}：R_k(X)=r_2^k\cos(k\varphi_2)+r_3^k\cos(k\varphi_3)+\cos(k\varphi_1)✓$$
$$\qquad \text{按}\ \textbf{整体区间乘积}✓：\mathrm{iprod}([a_1,a_2],[b_1,b_2])=\big[\min(4\ \text{积}),\max(4\ \text{积})\big]✓；r^k\in[r_{\rm lo}^k,r_{\rm hi}^k]✓（\text{单调}✓）$$
$$\qquad \textbf{禁止}✗：\text{"}r^k>0\ \text{故分别取界再相加"\ ✗}（42a\ \text{曾致}\ \Delta_{\rm ref}=-0.522\ \text{假负}✗）$$
$$\textbf{实测}：C0/C1\ \text{均以整体乘积实现}✓；\text{未见异常全域下界}✓（C0\ \min\ \text{认证余量}=1.8\times10^{-7}>0✓）$$

## §5 球的精确角色（未混用 ✓）

$$\text{完全位于某球内} \Longrightarrow \text{由 B5 覆盖}✓（\text{计 493 箱}✓）$$
$$\text{完全位于所有球外} \Longrightarrow \text{进入 B\&B}✓$$
$$\text{与球边界相交} \Longrightarrow \textbf{一律 split}✗（\text{共 220{,}110 次分裂}✓；\textbf{无"整箱误丢"}✓）$$

## §6 ⚠️ 待补的两项**簿记**（不改变结论，但须写明 ✓）

$$\textbf{① 球心与精确根的位置差}：\text{球心取 D-B 盒中心（float✓），精确根}\ z_0^*\in X_0\ \text{距其}\sim10^{-8}✗$$
$$\qquad \text{B5 的增长引理对【参考盒内任一点】成立}✓ \Longrightarrow \text{对}\ z_0^*\ \text{亦成立}✓，\text{数学无缺口}✓；$$
$$\qquad \text{但\textbf{计算排除}用的是"以中心为心、半径}\rho_{\rm up}"✓，\text{与"以}\ z_0^*\ \text{为心"差}\sim10^{-8}\ \text{的薄片}✗ \Longrightarrow \text{正式版应排}\ \bigcup_{x\in X_0}B(x,\rho_{\rm up})✓$$
$$\textbf{② 体积精确核对}：\text{T13-A C 阶段做过有理数精确体积核对}✓；\text{本档未做}✗ \Longrightarrow \text{补做（partition 由满 tiling 起点构造且未决=0，故完备性由构造保证 ✓，体积核对仅为独立确认 ✓）}$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 配对互换唯二轨道   命中文件数=1    ::  ./C228-DC-PASS-global-exclusion-damped-M3-C3-equals-Fz0.md
技术词 薄片簿记           命中文件数=1    ::  ./C228-DC-PASS-global-exclusion-damped-M3-C3-equals-Fz0.md
技术词 整箱误丢           命中文件数=1    ::  ./C228-DC-PASS-global-exclusion-damped-M3-C3-equals-Fz0.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① }C_3=F(z_0)\ \text{现在可写}✓（\text{但数值仍为区间级：上界来自合法有理构型＋区间算术}✓）$$
$$\textbf{② 最小点集}=\{z_0,\sigma z_0\}✓（\text{两点不同}✓：r_2=0.79051\neq r_3=0.83021✓）$$
$$\textbf{③ 严格性层级}：\text{区间乘积＋有向舍入}✓；\text{facet 法向仍用 float SVD}⚠️（\text{与 B5 同，\varepsilon\sim0.2\gg10^{-15}✓）$$
$$\textbf{④ 未用 RH}✓；\text{未改他档}✓；\textbf{⑤ 本档不主张}：\text{任何关于无阻尼}\ m_3\ \text{或一般}\ M\ \text{的外推}✗$$
