已查地图（**先查后写**）：`C-302`（Hecke 路关闭 ✓）、`C-301`（FSD 存在性审计 ＋ 五格口径 ✓）、`C-300`（FSD 资产登记 ✓）、`C-299`（核心闭环 ✓）。外部来源：Wikipedia Hilbert symbol ✓、Bristol notes ✓、Columbia notes ✓、Wikipedia Hasse principle ✓、Auel–Suresh（local-global failure）✓（均按不可信外部数据 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-303：失败机制存在性审计（方向② 二次型／二次互反）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条 ✓✓）

$$\textbf{① 方向② 命中}\ \textbf{现成机制}✓✓：\text{存在文献已定义的}\ \textbf{失败事件}＋\textbf{两个可交换传播}＋\textbf{非平凡兼容关系}✓（\text{即}\ \text{Hilbert symbol／Hilbert reciprocity}✓）$$
$$\textbf{② 但载体}\ \textbf{不 RH 相关}✗：\text{该机制栖息于}\ \text{局部-整体／互反理论}✓，\textbf{不}\ \text{直接与}\ RH\ \text{相关}✗ \Longrightarrow \textbf{不升级为 RH 候选}✗$$
$$\textbf{③ 关键收获}✓✓：\text{Hecke 所缺的}\ \textbf{「非平凡兼容关系」}✓\ \text{在此}\ \textbf{确实存在}✓，\text{其形态＝}\textbf{互反约束 ⟹ 失败不可孤立}✓✓$$

## §1 对象：Hilbert symbol ＋ Hilbert reciprocity（**文献现成**✓✓）

$$\textbf{定义}✓： (a,b)_v = +1 \iff z^2 = a x^2 + b y^2\ \text{在}\ \mathbb{Q}_v\ \text{上有非零解}✓；\text{否则}\ -1✓ \Longrightarrow \textbf{失败事件＝局部不可实现}✓（\text{文献定义}✓，\textbf{非我们构造}✓）$$
$$\textbf{双线性}✓✓： (a a', b)_v = (a,b)_v (a',b)_v✓ \Longrightarrow \textbf{两个自然乘法作用}✓（\text{第一宗量与第二宗量各一}✓）\textbf{且交换}✓ \Longrightarrow \textbf{Action 1／Action 2 均现成}✓$$
$$\textbf{非退化}✓：\text{若}\ (a,b)_v = 1\ \text{对一切}\ a，\text{则}\ b\ \text{为平方}✓（\text{文献定理}✓）$$
$$\textbf{互反律}✓✓： \prod_v (a,b)_v = 1✓；\text{Wikipedia 逐字}\ \text{「It is equivalent to the law of quadratic reciprocity.」}✓✓$$
$$\textbf{我方自含推论}✓✓：\text{因几乎处处为}\ 1✓\ \text{且每项为}\ \pm1✓ \Longrightarrow \textbf{(a,b)_v = -1 的位置数为偶}✓✓ \Longrightarrow \boxed{\textbf{失败不可孤立}}✓✓$$
$$\textbf{为何这是关键}✓✓：\text{该约束}\ \textbf{不是}\ \text{交换恒等式的改名}✗✓（\text{交换恒等式远弱于此}✓）\——\textbf{这正是 Hecke 所缺的那种非平凡约束}✓✓（\text{对照}\ C\text{-302 §3}✓）$$

## §2 五格表（✓✓，唐先生口径 ✓）

| 项 | Hilbert symbol／reciprocity 载体 | 判定 |
|---|---|---|
| **Failure** | 局部不可实现（`z^2 = a x^2 + b y^2` 在 `Q_v` 上无非零解 ✓） | **YES** ✓（文献定义 ✓） |
| **Action 1** | 第一宗量乘法（`a -> a x^2`，由双线性 ✓） | **YES** ✓ |
| **Action 2** | 第二宗量乘法（`b -> b y^2`，由双线性 ✓） | **YES** ✓ |
| **Compatibility** | 互反律 `prod_v (a,b)_v = 1` ⟹ 失败位置数为偶 ✓✓ | **YES** ✓（非平凡 ✓） |
| **Status** | 机制四格全通 ✓ —— **但载体不 RH 相关** ✗ | **YES（机制）／NO（RH 相关性）** ✓ |

- **出口判读** ✓：按唐先生规则「前三格任一非现成 ⟹ 停」——**本载体不停** ✓（三格皆现成 ✓）；但按**问句范围**（"RH 相关" ✓）⟹ **不合格** ✗✓
- **诚实标注** ⚠️：两个作用本身属**"乘平方"型** ✓，与"普通整数乘法"**贴近** ⚠️（repackaging 风险 ✓）—— 但**兼容关系非平凡** ✓，故**不算** repackaging ✗✓

## §3 判定（✓）

$$\textbf{① 机制层面}✓✓：\text{「failure ＋ 两可交换传播 ＋ 非平凡兼容」}\ \textbf{在文献中确实存在}✓\——\text{这}\ \textbf{加强了}\ C\text{-301 §3 的结构性观察}✓✓$$
$$\textbf{② RH 层面}✗：\text{载体＝局部-整体／互反理论}✓，\textbf{无}\ RH\ \text{接口}✗ \Longrightarrow \textbf{不进入}\ FSD\ \text{审计}✗；\textbf{不建}\ RH\ \text{bridge}✗$$
$$\textbf{③ 登记性质}✓：\text{作为}\ \textbf{「FSD 形机制存在」的独立证据}✓\ \text{登记}✓；\textbf{不}\ \text{作为}\ RH\ \text{候选}✗$$

## §4 与 Liouville 路线的亲缘（✓✓，唐先生预测被证实 ✓）

$$\textbf{共同点}✓✓：\text{二者最后一步都用}\ \textbf{二次互反}✓\——\text{Liouville artifact 的}\ \texttt{exists\_prime\_square\_below\_half}✓\ \text{与}\ \text{Hilbert reciprocity}✓\ \text{同源}✓$$
$$\textbf{差异}✓：\text{Liouville 侧失败来自}\ \textbf{加法表示缺失}✓（\texttt{noPP}✓）；\text{本侧失败来自}\ \textbf{局部不可实现}✓$$
$$\textbf{仍缺}✗：\text{本侧未见}\ \textbf{「失败 ⟹ 逐点符号量」}\ \text{的现成结构}⚠️（\text{Liouville 侧的}\ A(x),B(x)\ \text{角色}✓）$$

## §5 方向 ①③ 状态（✓，本刀未查 ✗）

- **① 零点/素数间隙的异常事件** ⚠️：**未查** ✗（注意避雷：不得掉回"显式公式 → 零点统计"旧墙 ✗✓）
- **③ 加法组合数论的局部禁形** ⚠️：**未查** ✗
- 纪律 ✓：**本档不扩展候选名词池** ✗；只记 ② 的结果 ✓

## §6 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：找到 RH 侧 FSD 机制 ✗；Hilbert 路可作 RH bridge ✗；本档关闭 ①②③ ✗（仅 ② 有结论 ✓）
- **本档新增词**：`失败不可孤立`／`互反兼容约束`（0 命中 ✓）
