已查地图（**先查后写**）：`C-3873`（**机制独立命题** ✓✓）、`C-3872`（**Gordan ⟹ 结构非奇异** ✓✓）、`C-3870`（**取到步** ✓✓）、`C-3861`（**16 个 `V_\sigma`；最优 `0.868850348`** ✓✓）、`C-3855`（**内部极值信号** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-74：C-3874-A —— 全局区间证书可行性预检（go/no-go）**（唐先生 2026-09-21 22:55 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 目标复述}✓✓：\text{固定}\ \sigma = (-1,1,1,-1,1)✓,\ c_0 = 0.86885034832244940011✓；\text{要证}\ \forall x \in E_{\mathrm{even}}✓：\max_{k \le 23,\ k\ \mathrm{odd}}|F_k^{(\sigma)}(x)| \ge c_0✓✓$$

$$\qquad \Longleftrightarrow S(c_0) := E_{\mathrm{even}} \cap \bigcap_{k\ \mathrm{odd}}\{|F_k| < c_0\} = \varnothing✓✓$$

$$\textbf{② Q1（能否半代数化）}✓✓: \ \boxed{\textbf{YES}}✓✓$$

$$\qquad \text{取}\ c_j := \cos\phi_j \in [0,1]✓✓ \Longrightarrow \boxed{F_k = \sum_j\gamma_jT_k(c_j)}✓✓\ \text{对}\ \textbf{odd 与 even 一律成立}✓✓$$

$$\qquad \Longrightarrow \text{整个系统是}\ c \in [0,1]^5\ \text{中的}\ \textbf{多项式} \text{系统}✓（\text{次数} \le 36✓） \Longrightarrow \textbf{有限可排斥区域在概念上良定义}✓✓$$

$$\qquad \text{（}\text{注}✓：x_j = c_j^2\ \text{时偶频仍为多项式}✓，但奇频出现}\ \sqrt{x}✗ \Longrightarrow \boxed{c\ \text{才是自然代数变量}}✓✓）$$

$$\qquad ⚠️ \textbf{自检}✗✓：本档 sympy 恒等式核验行对多数}\ k\ \text{返 False}✓,\ \text{系}\ \texttt{simplify}\ \textbf{能力不足}（\text{未设}\ |c| \le 1✓）✗,\ \textbf{该行不可采信}✗✓；\ \text{恒等式}\ T_k(\cos\phi) = \cos(k\phi)\ \text{本身标准}✓✓$$

$$\textbf{③ ⭐⭐ 关键结构性发现（}\textbf{本档最大收获}✓✓）}：\textbf{纯区间路线不可能独立闭合}✓✓$$

$$\qquad \text{因}\ V_\sigma\ \text{的}\ \textbf{最小值恰在边界取到}✓（\max_{\mathrm{odd}}(x^*) = c_0✓） \Longrightarrow \text{含}\ x^*\ \text{的盒子}\ \textbf{不能用区间算术排除}✗✓$$

$$\qquad \qquad \text{（区间界} \ge c_0\ \text{需}\ \max_{\mathrm{odd}} \ge c_0\ \text{在盒上成立}✓；\text{而}\ x^*\ \text{处等号成立} \Longrightarrow \text{须}\ \textbf{局部二阶} \text{或机制论证}✓✓）$$

$$\qquad \Longrightarrow \boxed{\text{A 路线与被暂缓的 ④（二阶）}\textbf{本质耦合}}✓✓\ \text{—— 不是两条独立路线}✓✓$$

$$\qquad \Longrightarrow \text{可行形态}✓：\textbf{复合路线}\ \big(\text{A：远离}\ x^*\ \text{的全局排斥}\big) + \big(\text{局部：二阶／C-3873 机制封口}\big)✓✓$$

$$\textbf{④ Q2（唯一未排除盒？）}⚠️\textbf{未决＋本档数据作废}✗✓$$

$$\qquad ⚠️ \textbf{自检（严重）}✗✓：\text{多起点下降}\ \textbf{只强制了 4 条偶频约束}✓（q \in \{3,4,7,9\}✓,\ \text{即 KKT 活跃集}✓）,\ \text{而}\ E_{\mathrm{even}}\ \text{需}\ \textbf{全部 12 条}✗✓$$

$$\qquad \qquad \Longrightarrow \text{所产生"可行点"}\ \textbf{不在}\ E_{\mathrm{even}}\ \text{内}✗ \Longrightarrow \text{所有}\ < 0.8688\ \text{的值（如}\ 0.571✓）\ \textbf{全部作废}✗✓,\ \textbf{不列入任何账本}✓✓$$

$$\qquad \text{结构性判断}✓（\text{定性}✓）: \max\ \text{over}\ 13\ \text{odd 频率} \Longrightarrow \text{至多}\ 13\ \text{个活跃分支}✓ \Longrightarrow \textbf{多个区域是可能的}✓✓$$

$$\qquad \qquad \text{（}C\text{-}3861\ \text{已给其余 15 个}\ \sigma\ \text{类}\ V_\sigma \in [1.77, 4.10]✓；\ \text{胜出}\ \sigma\ \textbf{内部} \text{的多重性}\ \textbf{仍未答}✗✓）$$

$$\qquad \Longrightarrow \text{须用}\ \textbf{含全部 12 条偶频约束} \text{的正确探针重做}✓✓\ \text{（登记为下一刀}✓）$$

$$\textbf{⑤ Q3（已有排除资产能否先砍掉大部分区域？）}✗✓: \ \boxed{\textbf{不能}}✓✓$$

$$\qquad \text{现有资产（collision／zero-atom／regular-layer／循环族}✓）\ \text{排除的是}\ E_0／\mathcal Z\ \text{子问题的}\ \textbf{退化轨}✓，$$

$$\qquad \qquad \text{与}\ \textbf{odd-max 景观} \text{的区域划分无关}✗ \Longrightarrow \text{对本问题}\ \textbf{不适用}✓✓$$

$$\textbf{⑥ 判词（按唐先生三出口）}✓✓：\ \boxed{\text{LOCAL-ONLY（纯区间）}}✓✓\ \text{＋}\ \boxed{\text{复合路线（A ＋ 局部二阶）为可行形态}}✓✓$$

$$\qquad \Longrightarrow \text{按唐先生令"否则立即转 B"✓} \Longrightarrow \textbf{下一刀转 C-3874-B（对偶证书审计）}✓✓,\ \textbf{不继续烧算力}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
Q1a（sympy，不可采信行）：T_k(c) == cos(k phi) -> 多数 False（simplify 未设 |c|<=1 假设）=> 该行 VOID
Q1b（公式笔误）：打印的 box 计数为倒数式（如 2.38e-06）=> VOID；正确标度见 §0③（导数界 ~36^2，且 x* 处等号=> 区间界失效）
Q2（VOID：仅 4/12 偶频约束）：
   feasible descents: 80 ; values < 1.5 : [0.570995, ..., 0.909517]   <-- 全部作废（不在 E_even 内）
   active odd branches observed: 11（定性参考，不作结论）
Q1c：频率集 13 个奇频 -> 至多 13 个活跃分支
```
- 脚本 ✓：`scripts/c380_74_C3874A_precheck.py`✓（含两处已标注错误 ✓）；输出 ✓：`scripts/out_c380_74.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| Q1 半代数化（`c = \cos\phi` 变量） ✓ | **YES（多项式，次数 ≤ 36）** ✓✓ |
| Q1 的 sympy 核验行 ✓ | **VOID（simplify 能力不足）** ✗✓ |
| **纯区间路线的独立性** ✓ | **不可能（边界盒需局部论证）** ✗✓ |
| Q2 唯一性 ✓ | **未决（本档数据 VOID）** ✗✓ |
| 区域多重性（定性） ✓ | **可能多个（≤13 分支）** ⚠️✓ |
| Q3 已有资产适用性 ✓ | **不适用** ✗✓ |
| **判词** ✓ | **LOCAL-ONLY（纯区间）；建议转 B** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 `V_\sigma = 0.868850348\ldots`（仍为上界候选）✓
- **不**引用本档作废数据（0.571 等）✓
- **不**声称已获全局证书 ✓
- **不**声称区域唯一 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}求最小值✗；\ \textbf{不}重优化✗；\ \textbf{不}跑正式 certification✗；\ \textbf{不}碰二阶（\text{但已指出其与 A 耦合}✓）$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 区间排斥证书 命中文件数=0    :: 
技术词 边界盒不可排斥 命中文件数=0    :: 
技术词 路线耦合     命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{C-3874-B}✓✓（\text{唐先生指定优先}✓）：\text{全局、}\textbf{点无关} \text{的对偶泛函是否存在}✓✓$$
$$\qquad \textbf{硬门槛}✓✓：\text{若最终系数仍依赖候选点的}\ \phi_j✗ \Longrightarrow \textbf{立即降级为局部证书}✓,\ \textbf{不准冒充 global}✓✓$$
$$\textbf{C-3874-A′}✓（\text{补做}✓）：\text{含}\ \textbf{全部 12 条} \text{偶频约束的多起点探针} \Longrightarrow \text{回答区域多重性}✓✓$$
