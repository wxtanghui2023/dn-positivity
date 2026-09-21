已查地图（**先查后写**）：`C-326`（Littlewood 跨对象：恒等式级资产 ✓）、`C-325`（Barker 跨对象 ✓）、`C-313`（LR 四格：**归一化型对称** ✓，**本轮不重审** ✓）、`C-292`（LR 深审回执：**约定映射表** ＋ 等价清单 ＋ Bedert 2025 下界 ＋ 小 n 文献 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-327：Lonely Runner 跨对象机制本体审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条 ✓✓）

$$\textbf{① 出口}✓：\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{操作级}✓）$$
$$\textbf{② 核心审计点答案}✓✓：\text{「速度组} \to \text{torus flow／orbit」}\ \textbf{是}\ \textbf{定义级／等价级重述}✓，\textbf{不是}\ \textbf{第二操作}✗✓（\text{见 §3}✓）$$
$$\textbf{③ 资产}✓✓：\text{LR 拥有三者中}\ \textbf{最丰富的等价网络}✓（\text{view-obstruction／flow／chromatic／zonotope／Bohr／Diophantine}✓）\ —— \textbf{仍是等价级}✗✓，\textbf{不}计为兼容律}✗$$

## §1 ① 精确定义（✓✓，防混淆 ✓）

$$\textbf{速度组}✓：V = \{v_1,\dots,v_n\}✓（互异正整数✓）；\text{距离}\ \|t v_i\|✓（\text{到最近整数}✓）$$
$$\textbf{常数}✓：\delta_n := \inf_{V} \max_t \min_i \|t v_i\|✓（\text{min-max 对象}✓）$$
$$\textbf{时间集合}✓✓：\textbf{good-time} G(V) := \{t : \forall i,\ \|t v_i\| \ge 1/(n+1)\}✓；\textbf{bad-time} ＝ \text{其补}✓$$
$$\textbf{约定必须并列}✓✓（C\text{-292 表}✓）：\text{总人数}\ n \leftrightarrow 1/n✓；k+1\ \text{人} \leftrightarrow 1/(k+1)✓；\text{移动者}\ m \leftrightarrow 1/(m+1)✓ \Longrightarrow \textbf{不}自行归一化✗✓$$
$$\textbf{严格分开}✓：\text{小}\ n\ \text{已证结果}✓（n = 4\ \text{直至}\ 13✓，\text{含计算辅助}✓）\ \ne\ \text{一般}\ n\ \text{猜想}✗✓$$

## §2 ② 关系性质分层（✓✓，逐项标 ✓）

| 关系 | 性质 |
|---|---|
| 小 `n` 已证 ✓ | **定理** ✓（含计算机辅助 ✓） |
| **Bedert 2025** ✓：`\delta_n \ge 1/(2n) + 1/n^{5/3+o(1)}` ✓ | **下界（当前最好）** ✓ |
| **view-obstruction**（Wills 1967／Cusick 1974 ✓） | **等价** ✓✓（**不得**误写成新机制 ✗✓） |
| **同步 Diophantine 逼近／nowhere-zero flow／distance-graph chromatic 数／格 zonotope 覆盖半径（Henze–Malikiosis ✓）／Bohr 集覆盖／谱形式（Giri–Kravitz ✓）** | **均为已有等价** ✓✓ ⟹ **等价级** ✓ |
| 临界对／极值配置分析 ✓ | **极值构造／结构分析** ✓ |
| LRC 一般 `n` ✓ | **猜想** ✓ |
| 被否证的加强猜想（Kravitz loneliness spectrum ✓） | **已否证** ✓ |
| 计算辅助个案（Rosenfeld／Trakulthongchai／Sungkawichai–Trakulthongchai ✓） | **计算证据／定理** ✓ |

$$\textbf{防误写}✓✓：\textbf{「某个等价 formulation」} \ne \textbf{「新机制」}✗✓（\text{唐先生指定}✓）$$

## §3 ③ 跨对象操作（✓✓，**核心审计点** ✓）

$$\textbf{入口}✓：V \mapsto \text{torus 轨道}\ t \mapsto (t v_1,\dots,t v_n) \bmod 1✓（\text{单参数子群轨道}✓，已有结构}✓）$$
$$\textbf{关键判定}✓✓：\text{该映射}\ \textbf{由}\ V\ \text{完全决定}✓，\text{且}\ G(V)\ \textbf{由该流定义}✓ \Longrightarrow \textbf{定义级重述}✗✓，\textbf{不是}\ \textbf{第二独立操作}✗✓$$
$$\qquad \textbf{判据}✓：\text{要成为第二操作，须存在}\ T_2: X \to X\ \textbf{与}\ T_1\ \text{独立}✓；\text{此处}\ T_1\ \text{与}\ T_2\ \text{实为同一动力系统的两种语言}✗✓$$
$$\textbf{其它跨对象对应}✓：\text{轨道} \to \text{view-obstruction／覆盖}✓；\to \text{格／zonotope}✓；\to \text{同步 Diophantine 逼近}✓；\to \text{间距／谱对象}✓ \Longrightarrow \text{均属}\ \textbf{等价级}✓✓$$
$$\textbf{排除}✗✓：V \mapsto aV✓（\text{归一化／重参数化}✓，C\text{-312}／C\text{-313 已判 ✓）；t \mapsto t + s✗$$

## §4 ④ compatibility（✓✓）

$$\textbf{所求}✓：\text{文献中已成立的}\ \textbf{跨两独立对象／结构的非平凡操作级兼容律}✓$$
$$\textbf{候选一}⚠️：\text{轨道} \leftrightarrow \text{torus 表述}✓ \Longrightarrow \textbf{定义等价}✗✓，\textbf{不算}✗$$
$$\textbf{候选二}⚠️：\text{距离恒等式／Fourier 表示}✓ \Longrightarrow \textbf{恒等式级}✗✓，\textbf{不算}✗$$
$$\textbf{候选三}⚠️：\text{谱对象}\ \kappa\ \text{结构（Giri–Kravitz}✓）\ \text{附于}\ V✓，\text{但未见与第二独立结构的}\ \textbf{兼容律}✗$$
$$\textbf{结论}✓✓：\textbf{未见}\ \textbf{操作级兼容律}✓ \Longrightarrow \boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓$$

## §5 出口、资产与纪律（✓✓）

$$\textbf{资产登记}✓✓：\text{LR 内部跨对象资产}＝\textbf{最丰富的}\ \textbf{等价级网络}✓（\text{view-obstruction／flow／chromatic／zonotope／Bohr／Diophantine}✓）\ —— \textbf{等价级} \ne \textbf{操作级}✗✓，\textbf{不}触碰 RH✗✓$$
$$\textbf{三者横向对照}✓✓：\text{Barker＝恒等式级联合约束}✓；\text{Littlewood＝恒等式级联合约束}✓；\text{LR＝等价级网络}✓ \Longrightarrow \textbf{无一达操作级}✗✓$$
$$\textbf{队列}✓：\text{C-325 Barker} \to \text{C-326 Littlewood} \to \text{C-327 LR}✓ \Longrightarrow \textbf{候选池三档全部审计完毕}✓$$
$$\textbf{M=5}✓：\textbf{继续}\ \textbf{OPEN/AUDIT}✓，\textbf{不与}\ C\text{-327 混线}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 跨对象机制层 命中文件数=1    :: ./C326-Littlewood-cross-object-mechanism-ontology-audit.md 
技术词 等价级资产  命中文件数=0    :: 
技术词 操作级兼容  命中文件数=2    :: ./C326-Littlewood-cross-object-mechanism-ontology-audit.md ./C325-Barker-cross-object-mechanism-ontology-audit.md 
```
- 本档新增 ✓：`等价级资产`／`跨对象机制层`（依上表判 ✓）
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：LR 已有操作级兼容律 ✗；等价 formulation＝新机制 ✗；LR 可升格为 RH bridge ✗
