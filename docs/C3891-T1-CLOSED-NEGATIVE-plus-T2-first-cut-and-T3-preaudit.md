已查地图（**先查后写**）：`C3890`（**等式化门槛；回溯测试** ✓✓）、`C3889`（**L0 定位；T1a/T1b 分半** ✓✓）、`C3846`（**精确仿射分解：`Q_3-q_3=4P_3` 等** ✓✓）、`C-3862`（**4 条偶频取等 ＋ tie** ✓✓）、`C-3870`（**`c_* = 1/L`** ✓✓）、`C-380-45`（**边界点、`Δ_4` 与 `320m<0`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-97：C-3891 —— T1 否定结果正式化 ＋ T2 首刀（stationarity 次数）＋ T3 预审（最低非零变分符号）**（唐先生 2026-09-22 09:02 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① T1 正式判定（唐先生令：}\textbf{不得}用"有条件通过／混合信号"✗✓**）：$$

$$\qquad \boxed{\text{T1（矩空间／T-system 路线）审计完成；结论}＝\textbf{不适用}}✓✓$$

$$\qquad \textbf{原因（精确定位，三条}✓✓**）：$$

$$\qquad \qquad \text{(a)}\ \textbf{量级错配}✓：\deg p \le 36\ \text{vs 需求}\ \operatorname{supp} \le 2✓✓（36 > 4✓,\ \text{连原子数都不约束}✗）$$
$$\qquad \qquad \text{(b)}\ \textbf{方向相反}✓：Carathéodory 数只给}\ \textbf{下界}✗,\ \text{而需要}\ \textbf{上界}✓$$
$$\qquad \qquad \text{(c)}\ \textbf{无推导能力}✓：回溯测试中经典定理}\ \textbf{只能事后认证、不能前置推导}✗✓$$

$$\qquad \Longrightarrow \boxed{\text{T1 作为 Phase I 的}\textbf{正式产出（负结果）}}✓✓：\text{不是"再查查有没有更合适的定理"}✗$$

$$\qquad \qquad \text{价值}✓✓：\textbf{没有} \text{生搬硬套一个不合适的理论}✓,\ \text{而是}\ \textbf{精确定位} \text{"看起来匹配的经典机器为何啃不动本问题"}✓✓$$

$$\textbf{② T2 首刀（}\textbf{stationarity 多项式次数}✓✓**）：\text{在}\ c_j = \cos\phi_j\ \text{坐标（}\partial F_k/\partial c_j = \gamma_jT_k'(c_j)✓）：$$

$$\qquad \boxed{P(c) = -\omega_{13}T_{13}(c) + \omega_{19}T_{19}(c) + \sum_{q \in \mathcal A}\lambda_qT_{2q}(c)}✓✓ \Longrightarrow \text{支撑点满足}\ P'(c_j) = 0✓✓$$

$$\qquad ⚠️ \text{但}\ \deg P' \le 35✗ \Longrightarrow \textbf{朴素写法给不出}\ \deg \le 3✗✓（\text{与 T1 同型的无用界}✓）$$

$$\qquad ⭐ \textbf{真实结构收获}✓✓：\textbf{偶频约束只依赖}\ x_j = c_j^2✓（T_{2q}\ \text{是}\ c^2\ \text{的函数}✓） \Longrightarrow \textbf{偶频可行集对}\ c_j \to \pm c_j\ \text{与置换不变}✓✓$$

$$\qquad \qquad \text{而}\ F_{13}, F_{19}\ \text{是}\ c\ \text{的}\ \textbf{奇函数}✓ \Longrightarrow \textbf{符号信息全部由}\ \sigma\ \text{承担}✓✓ \Longrightarrow \boxed{\text{问题}＝\text{"}x\text{-多重集"}\times\text{"符号型"}}✓✓$$

$$\qquad \textbf{T2 真实目标（登记）}✓✓：\deg \le 3\ \textbf{不能} \text{由朴素 stationarity 得到}✗,\ \text{须用}\ \textbf{6 项稀疏性 ＋ 奇偶分拆（4 even ＋ 2 odd）} \text{证明}\ \textbf{根集成对}✓✓$$

$$\textbf{③ T3 预审（唐先生要求补上}✓✓**）：\text{用}\ C\text{-}3846\ \textbf{精确仿射分解}✓：$$

$$\qquad Q_3 - q_3 = 4P_3✓;\qquad Q_4 - q_4 = 32mP_3 + 32\Delta_4✓;\qquad Q_5 - q_5 = \left(160m^2 - 20 + \tfrac{40}{3}P_2\right)P_3 + 320m\Delta_4✓✓$$

$$\qquad \textbf{为何}\ \Delta_4\ \textbf{路线死}✓：m \le -\tfrac18 \Longrightarrow \boxed{320m\Delta_4 \le -40\Delta_4 < 0}✓✓ \Longrightarrow \text{非配对}\ \textbf{降低}\ Q_5（\textbf{有利}）✗ \Longrightarrow \textbf{无惩罚}✗✓$$

$$\qquad ⭐ \textbf{正确坐标是}\ P_3\ \textbf{而非}\ \Delta_4✓✓：\text{极值点处}\ \textbf{Q_3 = -\tfrac12 是活跃约束}✓,\ \text{而}\ Q_3 - q_3 = 4P_3\ \textbf{一阶线性}✓$$

$$\qquad \qquad \Longrightarrow \textbf{任何}\ P_3 > 0\ \text{一阶违反约束}✓ \Longrightarrow \boxed{\text{一阶损失} = 4|P_3|}✓✓ \Longrightarrow \textbf{T3 稳定性量应建于}\ P_3✓✓$$

$$\textbf{④ 资源调度（唐先生令}✓✓**）：\textbf{T1 已跑完并给否定结论}✓ \Longrightarrow \text{资源集中到}\ \textbf{T2}✓✓（\text{四轨中唯一"已有部分进展＋下一步明确＋难度渐进可控"}✓）；\ \textbf{T3 预审已完成}✓,\ \text{其结论}\ \textbf{直接决定 T3 是否值得投入}✓✓$$

$$\textbf{⑤ T4}✓：\text{维持}\ \textbf{辅助线}✓（不吞噬资源}✓）$$

$$\textbf{⑥ 账本（见 §2）}✓✓；\qquad \textbf{⑦ 边界（见 §3）}✓✓$$

## §1 四轨 scorecard（L3 机制 ✓✓）

| Track ✓ | 已得严格 lemma ✓ | 参数减少 ✓ | 文献对应 ✓ | 数值支持 ✓ | 当前障碍 ✓ | 判定 ✓ |
|---|---|---|---|---|---|---|
| **T1 Moment/T-system** ✓ | 事后证书 `p_2` ✓ | 0 ✓ | 高（但界无用）✓ | — ✓ | 量级错配（36 vs 2）＋方向相反 ✓ | **CLOSED-NEGATIVE** ✗✓ |
| **T2 KKT／代数几何** ✓ | `P(c)`、`P'` 显式 ✓；**奇偶分拆** ✓ | **中→高** ✓ | 中 ✓ | 高 ✓ | 需证根集成对 ✓ | **主攻** ✓✓ |
| **T3 稳定性** ✓ | **一阶损失 `4\|P_3\|`** ✓ | 中 ✓ | 中 ✓ | 中 ✓ | coercivity ✓ | **待 T2 后** ✓ |
| **T4 Majorization** ✓ | 0 ✓ | 低 ✓ | 中 ✓ | — ✓ | 同时保约束 ✓ | 辅助线 ✓ |

$$\textbf{周期问}✓✓：\boxed{\text{哪条线最近一次}\textbf{真正降低了问题复杂度}？} \Longrightarrow \textbf{T2}（奇偶分拆＋`P_3` 坐标）✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| T1 判定 ✓ | **不适用（CLOSED-NEGATIVE，Phase I 正式产出）** ✗✓ |
| T2 首刀 ✓ | **`P(c)`／`P'` 显式；奇偶分拆成立** ✓✓ |
| T2 里程碑 `deg \le 3` ✓ | **未达（须稀疏性＋成对性）** ✗✓ |
| T3 预审 ✓ | **完成：坐标应为 `P_3`（一阶），非 `\Delta_4`** ✓✓ |
| 资源调度 ✓ | **集中 T2** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**把 T1 记成"有条件通过／混合信号"（**已按唐先生令改为明确否定**）✓✓
- **不**声称 T2 的 `deg \le 3` 已得 ✓
- **不**声称 T3 稳定性已成立（只定出**坐标**）✓
- **不**把 `P_3` 的一阶损失当作完整稳定性定理 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}修数学（除显式化／符号核验）✗；\ \textbf{不}发新候选✗；\ \textbf{不}开 T3 计算✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 明确否定结果 命中文件数=0    :: 
技术词 奇偶分拆分解 命中文件数=0    :: 
技术词 一阶损失坐标 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① T2 主攻}✓✓：\text{用}\ \textbf{6 项稀疏性} \text{证明 stationarity 根集}\ \textbf{成对}✓（\text{目标}\ \deg \le 3\ \text{或直接}\ \textbf{支撑} \le 2✓）；\ \text{产出即}\ M1\ \text{里程碑}✓✓$$
$$\textbf{② T3}✓：\text{以}\ P_3\ \text{为一阶坐标，写"}\text{dist to two-level} \Longrightarrow 4|P_3|\ \text{损失"}✓；\ \text{先做}\ \textbf{coercivity 可行性预检}✓$$
