# C-3894 — T3-PASS: Second-order F14 obstruction eliminates all nonzero tangent directions
# at the two-level point (m,a)=(-1/8, 3 sqrt3/8)

**状态：`T3-PASS / LOCAL-RIGIDITY`**

已查地图（**先查后写**）：`C3893`（**活跃集核对；`4P_3` 不迁移** ✓✓）、`C3892`（**`P_3` 分解；`(P_3,\Delta_4)` 双坐标** ✓✓）、`C-3862`（**活跃集 `\{3,4,7,9\}`** ✓✓）、`C-3856`（**`\phi`-坐标对角 Hessian** ✓✓）、`C-3876`（**远区 OPEN** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-101：C-3894 —— T3 二阶可行性（真实活跃集上，`T3-PASS`）**（唐先生 2026-09-22 09:35 令：立即执行 ③）
D1: 0
FREEZE-ACK: 本档即冻结审计

## §0bis 收紧后的最终陈述（唐先生 2026-09-22 09:38 令 ✓✓）

$$\boxed{\text{所有非零切向扰动在}\ F_{14}\ \text{上二阶立即出界}}✓✓\ \text{（}\textbf{不是}\text{"目标有正二阶曲率"}✗） \Longrightarrow \textbf{确实不需要}\ \text{KKT 对偶证书}✓✓$$

$$\text{固定}\ \sum Y_j = 0,\ \sum Y_j^2 = 4a^2✓;\ v = (v_1,-v_1,v_3,-v_3)✓;\ \dot P_3 = 0✓,\ \dot\Delta_4 = 0✓;\ P_3(t) = 6av_1^2t^2 - 6av_3^2t^2 + O(t^3)✓,\ \Delta_4(t) = 3a^2(v_1^2+v_3^2)t^2 + O(t^3) > 0\ (v \ne 0)✓✓$$

$$\rho := v_3^2/v_1^2 \in [0,\infty]✓（v_1 = 0\ \text{取}\ \rho = \infty✓） \Longrightarrow F_{14}''(\rho) = 70.842572 + 933.219928\rho > 0✓✓$$

$$\Longrightarrow F_{14}(t) = F_{14}(0) + \tfrac12F_{14}''(\rho)t^2 + O(t^3) > -\tfrac12\ \text{（充分小}\ t \ne 0✓） \Longrightarrow \textbf{违反原约束}\ F_{14} \le -\tfrac12✓✓$$

$$\boxed{T_{(m,a)}E_{\mathrm{even}} = \{0\}\quad\text{（在该固定球面约束下）}}✓✓$$

$$\textbf{精确措辞（替代旧句}✓✓**）：\textit{任意非零切向扰动}\ v \ne 0\ \textit{均使}\ F_{14}\ \textit{的二阶项严格增加，因此不存在保持全部原始偶频约束的一阶切向二阶可行曲线。}✓✓$$

$$\qquad （\textbf{理由}✓：\text{旧句把"切向量"与"two-level／非 two-level 点"混为一谈}✗；\text{新句只谈切向}✓）$$

$$\textbf{更强的实情}✓✓：P_3 = 0,\ \Delta_4 \ne 0\ \text{只是最纯的非 two-level 二阶方向（}\rho = 1✓）；\text{本档实际证明了}\ \rho \in [0,\infty)\ \textbf{的所有} \text{非零方向都被}\ F_{14}\ \text{杀掉}✓✓$$

$$\textbf{四条禁写（超出 C-3894 射程}✗✓**）：\text{(1) 全局 two-level collapse}✗；\text{(2) 全局}\ F_0 = \varnothing✗；\text{(3) 全局}\ \Delta_4 > 0\ \text{稳定性}✗；\text{(4) 已证全局最优点必须是该 two-level 点}✗✓$$

---

## §0 结论（七条 ✓✓）

$$\textbf{① 范围}✓✓：\text{仅用}\ \{F_6,F_8,F_{14},F_{18}\}✓（\text{指数}✓）＝\text{频率}\ \{12,16,28,36\}✓;\ \boxed{Q_k\ (k \le 6)\ \textbf{完全隔离}}✓✓$$

$$\textbf{② 坐标事实（本档确立}✓✓**）：$$

$$\qquad \text{切空间}✓：\sum v_j = 0✓,\ \sum Y_jv_j = 0✓ \Longrightarrow \boxed{v = (v_1,-v_1,v_3,-v_3)}✓✓（\textbf{恰 2 维}✓）$$

$$\qquad \boxed{\dot P_3 \equiv 0}✓✓（\sum Y_j^2v_j = a^2\sum v_j = 0✓） \Longrightarrow \textbf{P_3 是二阶量}✗✓ \Longrightarrow \textbf{修正 C3891 的阶数定性}✓：\text{"一阶损失} 4P_3\text{"}\ \textbf{实为二阶}✗✓$$

$$\qquad \textbf{四活跃约束一阶全平坦}✓✓：F_n' = T_n'(u_+) (v_1+v_2) + T_n'(u_-)(v_3+v_4) = 0✓ \Longrightarrow \textbf{全为二阶问题}✓$$

$$\textbf{③ }P_3／\Delta_4\ \textbf{二阶变分}✓✓**：P_3(t) = 3t^2\cdot 2a(v_1^2 - v_3^2) + O(t^3)✓;\qquad \boxed{\Delta_4(t) = 3t^2a^2(v_1^2+v_3^2) + O(t^3) > 0}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{纯}\ \Delta_4\ \text{方向}＝\rho := v_3^2/v_1^2 = 1}✓✓$$

$$\textbf{④ 二阶系数公式}✓✓：\boxed{F_n''(\rho) = 2T_n''(u_+) + 2T_n''(u_-)\rho + \frac{1+\rho}{a}\left[T_n'(u_-) - T_n'(u_+)\right]}✓✓\ \Longrightarrow \textbf{仿射于}\ \rho✓$$

$$\textbf{⑤ 判据：}\boxed{\textbf{T3-PASS}}✓✓（\text{最小代数证书：}\textbf{单条即足}✓）$$

$$\qquad \boxed{F_{14}''(\rho) = 70.842572 + 933.219928\,\rho > 0\quad \forall \rho \ge 0}✓✓$$

$$\qquad \Longrightarrow \textbf{每个非 two-level 切向都在二阶违反}\ F_{14}\ \text{（频率 28）}✓✓ \Longrightarrow \textbf{不存在二阶可行非配对方向}✓ \Longrightarrow \boxed{P_3 = 0,\ \Delta_4 \ne 0 \Longrightarrow \textbf{严格二阶损失}}✓✓$$

$$\qquad \text{纯}\ \Delta_4\ \text{方向（}\rho = 1\text{）余量}✓：F_{14}''(1) = \mathbf{+1004.0625}✓✓$$

$$\textbf{⑥ 逻辑澄清（回应唐先生警告}✓✓**）：\text{本判据是}\ \textbf{可行性障碍}✓ \Longrightarrow \textbf{单条被违反的活跃约束即足}✓✓,\ \textbf{不需要} KKT 对偶组合✗；\ \text{对偶组合只在证"}\textbf{目标严格改善}\text{"时必需}✓（\text{那时需}\ \textbf{全部} \text{约束非降}✓）$$

$$\textbf{⑦ 范围与不矛盾}✓✓：\text{结论}\ \textbf{局部} \text{于该 two-level 点}\ (m,a) = (-\tfrac18, \tfrac{3\sqrt3}{8})✓,\ \textbf{在固定}\ (m,\sum Y^2)\ \text{球面上}✓；\ \text{与档案}\ \textbf{全局} \text{最优}\ \Delta_4 \approx +0.000878 > 0\ \text{（另一个点}✓）\ \textbf{不矛盾}✓ \Longrightarrow \boxed{\text{局部刚性} \ne \text{全局坍缩}}✓✓$$

## §1 四张表（唐先生指定交付 ✓✓）

**表 1｜真实活跃集** ✓：`\{F_6, F_8, F_{14}, F_{18}\}`（指数）＝频率 `\{12,16,28,36\}`；`Q_k\ (k \le 6)` 隔离 ✓

**表 2｜切空间** ✓：`\sum v = 0`、`\sum Yv = 0` ⟹ `v = (v_1,-v_1,v_3,-v_3)`；`\dot P_3 \equiv 0`；`F_n' \equiv 0` ✓

**表 3｜`P_3`／`\Delta_4` 变分** ✓：`P_3 = 6at^2(v_1^2-v_3^2) + O(t^3)`；`\Delta_4 = 3a^2t^2(v_1^2+v_3^2) + O(t^3)` ✓

**表 4｜二阶系数（`\rho`-仿射）** ✓：

| `n` ✓ | `A_n` ✓ | `B_n` ✓ | `F_n''(1)` ✓ |
|---|---|---|---|
| 6 ✓ | -85.736515 ✓ | +85.736515 ✓ | 0.000000 ✓ |
| 8 ✓ | +64.568466 ✓ | -256.943466 ✓ | -192.375 ✓ |
| **14** ✓ | **+70.842572** ✓ | **+933.219928** ✓ | **+1004.0625** ✓ |
| 18 ✓ | -767.122713 ✓ | -1573.116789 ✓ | -2340.2395 ✓ |

$$\text{系数}✓：u_\pm = -\tfrac18 \pm \tfrac{3\sqrt3}{8}✓;\ \text{证书}\ \textbf{单约束}\ (n=14)✓ \Longrightarrow \forall \rho \ge 0:\ F_{14}''(\rho) > 0✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 真实活跃集隔离 ✓ | **完成** ✓✓ |
| 切空间（2 维） ✓ | **完成** ✓✓ |
| `\dot P_3 \equiv 0` ✓ | **完成（阶数更正）** ✓✓ |
| 二阶系数表 ✓ | **完成** ✓✓ |
| **判据** ✓ | **`T3-PASS`（单约束证书）** ✓✓ |
| 范围 ✓ | **局部（该点、固定 `(m,\sum Y^2)`）** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称全局坍缩（**仅局部刚性**）✓✓
- **不**把 `P_3` 说成"一阶损失"✓✗（**是二阶**）✓
- **不**声称 `\rho = 1` 是唯一非 two-level 方向 ✓
- **不**声称对偶组合已构造（**不需要**）✓✓
- **不**声称证书系数已达精确代数形式（数值余量大、符号稳健；**精确化待办**）⚠️

## §4 本档**不**做的事 ✓✓

$$\textbf{不}开 T2✗（按唐先生序 ①→③→②）;\ \textbf{不}重开 T1✗;\ \textbf{不}动论文✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 二阶可行性障碍 命中文件数=0    :: 
技术词 纯偏离方向  命中文件数=0    :: 
技术词 单约束证书  命中文件数=0    ::
```

## §6 下一步（按唐先生序 ✓✓）

$$\textbf{② （下一切）}✓✓：T2\ \text{根集成对}✓（\text{6 项稀疏性} ＋ \text{奇偶分拆}✓） \Longrightarrow M1\ \text{里程碑}✓$$
$$\textbf{附带}✓：\text{把本档证书系数}\ \textbf{精确化为代数数}✓（\text{符号已稳健}✓）；\ \text{并把局部刚性接入远区}\ (C\text{-}3876)\ \text{的 OPEN 状态}✓✓$$
