已查地图（**先查后写**）：`C-3859`（**SLSQP 未移动；formal「未能定位 genuine KKT」；`SLSQP success ≠ KKT` 为硬规则** ✓✓）、`C-3858`（**α-2 VOID：无有效测试点** ✓✓）、`C-3857`（**次微分多重活跃结构** ✓✓）、`C-3856`（**该点严格内部；奇频单活跃** ✓✓）、`C-3855`（**对 σ 取 max ≈ 3.85 vs 取 min ≈ 0.88** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-60：B1-α-3 首刀 —— 切割平面多起点 ＋ interior／boundary 审计（VOID：无可行初始化）**（唐先生 2026-09-21 22:28 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 档位（含职责分离）}✓✓：\textbf{主刀} = \alpha\text{-3}\ \text{枚举}✓；\ \textbf{优化器只找对象、不判词}✓✓（\text{独立}\ \text{次微分 LP 才判}✓）；\ \text{实现}\ \textbf{切割平面／信赖域} \text{主问题}✓（LP 主问题 ＋ 真目标线搜索}✓）$$

$$\textbf{② ⚠️ 规格歧义（本档登记）}✗✓：\text{唐先生本轮写}\ \min_x\max_{r,\sigma}|F_{2r+1}^{(\sigma)}|✓；\ \text{但}\ B1\text{-}\alpha\ \text{既定顺序是}\ \boxed{\gamma^{(13)} = \min_{\sigma}\min_x\max_r}✓✓（\sigma\ \text{在外层取}\ \textbf{min}✓）$$

$$\qquad \text{两者}\ \textbf{不同}✓✓：`C-3855` 实测 —— 对}\ \sigma\ \text{取}\ \textbf{max} \Rightarrow \approx 3.85✓；\ \text{取}\ \textbf{min} \Rightarrow \approx 0.88✓✓$$

$$\qquad \Longrightarrow\ \text{本档}\ \textbf{按既定顺序}（\sigma\ \text{取 min}✓）\ \text{执行}✓✓；\ \text{差异}\ \textbf{登记待裁}✓$$

$$\textbf{③ ⚠️ 结果：}\textbf{VOID（本刀再次不作判词）}✗✓$$

$$\qquad \text{证据}✓：\text{全部}\ 16\ \sigma\ \text{的输出}\ \text{"feasible(margin=…)"}\ \textbf{为负}✓（-0.85 \sim -3.31✓）⟹ \max_r(F_{2r} - \tfrac12) > 0✓ \Longrightarrow \textbf{违反偶频约束}✗✗$$

$$\qquad \text{例}✓：\text{最优}\ \sigma = (1,-1,1,-1,1)✓,\ g = 0.947967464✓：\ \text{even margins}\ \text{含}\ -0.847／-0.779／-1.334✓ \Longrightarrow F_6 = 1.279✓,\ F_{12}=1.334✓\ \text{等}\ \textbf{越界}✗$$

$$\textbf{④ 根因（本刀核心诊断）}✓✓：\textbf{没有可行初始化}✗✓$$

$$\qquad \text{随机起点}\ \phi \in (0.02,\ \tfrac{\pi}{2}-0.02)^5\ \text{本身}\ \textbf{就可能违反}\ F_{2r} \le \tfrac12✓✓（\text{随机}\ \phi\ \text{极易超}✓）$$

$$\qquad \text{而线搜索接受条件} = \{\text{改进}\} \wedge \{F_{2r} \le \tfrac12\ \text{到}\ 10^{-12}\}✓ \Longrightarrow \textbf{从不可行起点永远迈不出一步}✗✓ \Longrightarrow \text{停在不可行点}✓✓$$

$$\qquad \Longrightarrow\ \text{本刀}\ \textbf{无有效检验对象}✓ \Longrightarrow \textbf{不产生 KKT 判词}✓✓（\text{既非"找到"亦非"未找到"✓}）$$

$$\textbf{⑤ 三出口分类（按唐先生，严格区分）}✓✓$$

$$\qquad \boxed{\text{(E1) genuine KKT}}✓；\qquad \boxed{\text{(E2) 未定位 genuine KKT}}✓；\qquad \boxed{\text{(E3) 某 active-set 分支}\ \textbf{代数不相容}}✓✓$$

$$\qquad \text{本刀状态}✓：\textbf{三者皆未达成}✗✓\ \text{（因对象无效}✓）\ \Longrightarrow \text{记为}\ \textbf{VOID}✓\ \text{而非 E2}✗✓$$

$$\textbf{⑥ interior／boundary 分离（已实现）}✓✓：\text{审计 LP 支持}\ \textbf{法锥项}✓：\text{boundary（}\phi_j = 0✓）\ \text{加入}\ -\mu_j e_j\ (\mu_j \ge 0)✓✓$$

$$\qquad \text{本轮}\ \text{boundary indices} = \varnothing✓ \Longrightarrow \text{全部为}\ \textbf{INTERIOR} \text{情形}✓（\text{但对象不可行，故仍无判词}✓）$$

$$\qquad \textbf{特别检查（唐先生第 4 条）}✓✓：\text{若}\ \mathcal A = \varnothing\ \text{且奇频单活跃} \Longrightarrow \text{KKT 退化为}\ \nabla F_{\text{odd}} = 0✓✓；\ \text{`C-3859` 该点}\ \textbf{不满足}✗✓$$

$$\textbf{⑦ 硬规则保留}✓✓：\ \boxed{\text{SLSQP／优化器"成功"}\ \ne\ \text{KKT}}✓✓\ \text{（`C-3859` 已证其未移动}✓）;\ \text{本档进一步}：\ \textbf{优化器不可行性}\ \ne\ \text{判词}✓✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
方法：切割平面/信赖域（LP 主问题：min t s.t. |F_r| + sgn(F_r)∇F_r·d <= t (r ∈ I)；
      F_2q + ∇F_2q·d <= 1/2；|d|_∞ <= Δ；phi+d >= 0）+ 真目标线搜索；每 σ 60 起点 × 70 外层迭代
每 σ 的最优 g：2.04, 1.01, 2.03, 1.07, 1.33, 1.03, 1.46, 1.88, 1.61, 1.34, 0.95, 1.98, 1.17, 2.00, 1.95, 2.58
可行性：全部 margin < 0（-0.85 ~ -3.31）⟹ 全部违反 F_2r <= 1/2 ✗✗
最好点（σ = (1,-1,1,-1,1)，g = 0.947967464）：even margins 含 -0.8465 / -0.7792 / -1.3341 ⟹ 越界
boundary indices = ∅ （全部 interior 情形）
次微分 LP：三档容差全部 False（但在不可行点上，判词无效）
诊断：无可行初始化 ⟹ 不可行起点 + 严格接受条件 ⟹ 方法停滞
```
- 脚本 ✓：`scripts/c380_60_B1alpha3_bundle.py`✓；输出 ✓：`scripts/out_c380_60_B1alpha3.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 切割平面／信赖域实现 ✓ | **已实现（含法锥项）** ✓✓ |
| 本刀对象可行性 ✓ | **全部不可行 ⟹ VOID** ✗✓ |
| 三出口（E1／E2／E3） ✓ | **皆未达成（对象无效）** ⚠️✓ |
| interior／boundary 分离 ✓ | **已实现（本轮全 interior）** ✓✓ |
| `SLSQP success ≠ KKT` ✓ | **保留为硬规则** ✓✓ |
| `0.876069` ✓ | **上界（不变）** ✓✓ |
| B1-β ✓ | **未进入** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 KKT 不存在（本刀 VOID）✓
- **不**把不可行点当极值证据 ✓
- **不**把本刀记为 E2（未定位）—— 对象无效，不是"找不到"✓
- **不**声称优化器已足够强 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}继续盲调优化器✗（\text{按唐先生第 7 条}✓）；\ \textbf{不}进入}\ \beta✓；\ \textbf{不}重开已封路线}✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 可行初始化  命中文件数=0    :: 
技术词 三出口分类  命中文件数=0    :: 
技术词 量词顺序登记 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 修可行初始化}✓✓：\text{起点改为}\ \textbf{可行点}✓（\text{如}\ 0.876069\ \text{构型}✓\ \text{或}\ C\text{-}3855\ \text{惩罚下降产出}✓），\ \text{或加}\ \textbf{可行性恢复相}（restoration}✓）$$
$$\textbf{② 若仍失败}✓：\text{按唐先生第 7 条} \Longrightarrow \text{审计}\ \boxed{\gamma^{(13)}\ \text{是否真在当前有限维参数化中取到极小}}✓✓ \Longrightarrow \text{审计}\ \textbf{min–max 交换／紧性结构}✓✓$$
$$\qquad \text{已知线索}✓✓：\sigma \leftrightarrow F^{(\sigma)}\ \text{有限}（16✓）；\ x \in [0,1]^5\ \text{紧}✓；\ E_{\mathrm{even}}\ \text{闭}✓ \Longrightarrow \text{每个}\ V_\sigma = \min_x\max_r|F^{(\sigma)}|\ \textbf{存在}✓✓ \Longrightarrow \gamma = \min_\sigma V_\sigma\ \textbf{存在}✓✓（\text{故}\ \textbf{紧性不缺}✓，\text{缺的是}\ \textbf{可定位性}✓）$$
