已查地图（**先查后写**）：`C-3858`（**α-2 首刀 VOID：无有效测试点** ✓✓）、`C-3857`（**单权重模型不足；次微分多重活跃结构** ✓✓）、`C-3856`（**两候选非极小；`0.876069` 为上界；该点近 binding 集 `{3:1.54e-4, 4:1.37e-3, 9:1.21e-2}`** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-59：B1-α-2b —— 从 `0.876069` 的带约束局部精修 ＋ 次微分 LP 审计**（唐先生 2026-09-21 22:25 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 档位}✓✓：\min_{\phi}\max_{r \le 12}|F_{2r+1}(\phi)|✓\ \text{s.t.}\ F_{2r}(\phi) \le \tfrac12✓（\textbf{显式约束}✓）；\ \text{起点}\ = C\text{-}3850\ \text{构型}✓；\ \textbf{不做}无约束全局搜索}✗✓$$

$$\qquad \text{实现}✓：\text{光滑 NLP}\ (\phi, t)✓：\min t✓\ \text{s.t.}\ |F_{2r+1}| \le t✓,\ F_{2r} \le \tfrac12✓；SLSQP✓,\ \text{每}\ \sigma\ 120\ \text{起点}✓✓$$

$$\textbf{② ⭐ 结果：}\textbf{本轮未改进}✗✓：\ \text{全部}\ \sigma\ \text{中最优}\ \boxed{g = 0.876060870}✓✓ \Longrightarrow \text{其}\ x\ \text{与起点}\ \textbf{逐位相同}✓✓$$

$$\qquad \Longrightarrow\ \boxed{\textbf{SLSQP 没有移动}}✓✓ \Longrightarrow \textbf{"SLSQP 成功退出"}\ \textbf{在此不等于 KKT}✓✓（\textbf{唐先生预警的陷阱}\ \textbf{现形}✓✓）$$

$$\textbf{③ 四项确认（唐先生规格）}✓✓$$

$$\qquad \text{(i)}\ g < 0.876069 + \epsilon✓\ \text{（成立，但仅为}\ \textbf{相等}✓，\ \textbf{非}改进}✗✓）$$
$$\qquad \text{(ii)}\ \text{偶频约束}\ \textbf{全部满足}✓✓（\text{最小余量}\ 1.545\times10^{-4}✓，据 `C-3856` 为}\ r = 3✓）$$
$$\qquad \text{(iii)}\ \text{活跃偶频集}\ \boxed{\mathcal A = \varnothing}✓✓\ \text{（容差}\ 10^{-6} < 1.5\times10^{-4}✓ \Longrightarrow \textbf{无偶频约束活跃}✓✓ \Longrightarrow \text{点}\ \textbf{严格在}\ E_{\mathrm{even}}\ \textbf{内部}}✓✓）$$
$$\qquad \text{(iv)}\ \text{奇频结构}✓：\textbf{单一} \text{活跃 index}\ r = 6✓（\text{频率}\ 13✓）,\ \textbf{无并列}✗✓$$

$$\textbf{④ 次微分 LP 审计}✓✓（\text{按}\ \alpha\text{-2 形式，三档容差}✓）$$

$$\qquad \forall \text{tol} \in \{10^{-7}, 10^{-6}, 10^{-5}\}✓：\ |\mathcal I| = 1✓,\ \mathcal A = \varnothing✓ \Longrightarrow \boxed{\text{subdiff-KKT} = \textbf{False}}✓✓$$

$$\qquad \text{（}\mathcal A = \varnothing\ \text{时}\ \text{LP}\ \text{要求}\ \operatorname{sgn}(F)\nabla F_{\text{odd}} = 0✓，\ \text{而}\ \nabla F_{\text{odd}} \ne 0✓ \Longrightarrow \text{必然失败}✓✓）$$

$$\textbf{⑤ 判词（按唐先生规格）}✓✓：\ \boxed{\textbf{未能定位 genuine KKT}}✓✓\ \text{（}\textbf{正式记录}✓；\ \textbf{不}判方法失败}✗✓）$$

$$\qquad \text{且}\ \text{本档}\ \textbf{不}进入 B1-}\beta✓（\text{入口条件未满足}✓）$$

$$\textbf{⑥ 诊断（登记）}✓✓：\text{最优点}\ \textbf{严格内部}✓（无活跃偶频约束}✓）\ ＋\ \text{奇频梯度}\ \textbf{非零}✓ \Longrightarrow \textbf{存在一阶可行下降方向}✓✓$$

$$\qquad \Longrightarrow\ \text{优化器}\ \textbf{未能沿其前进}✓ \Longrightarrow \text{后续须}\ \textbf{换更好的非光滑方法}✓（\text{或改标度／步长／许可迭代数}✓）；\ \text{这不是 KKT 存在性的证据}✗✓$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
起点：C-3850 构型 x = [0.801874, 0.561119, 0.703473, 0.627211, 0.869546]
最优（16 σ 全部）：g = 0.876060870，sigma* = (-1,1,1,-1,1)，r* = 6（频率 13），A = []，min margin = 1.545e-04
其余 σ 的最优 g 分布在 2.01 ~ 4.21 ⟹ 明显更差（说明该 σ 分支是唯一接近上界的）
次微分 LP：tol = 1e-7 / 1e-6 / 1e-5 全部 False
对照（C-3856）：该点近 binding 集 = {r=3: 1.54e-4, r=4: 1.37e-3, r=9: 1.21e-2}
```
- 脚本 ✓：`scripts/c380_59_B1alpha2b_refine.py`✓；输出 ✓：`scripts/out_c380_59_B1alpha2b.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 带约束局部精修 ✓ | **已做；未改进（优化器未移动）** ⚠️✓ |
| genuine KKT 点 ✓ | **未能定位（正式记录）** ✗✓ |
| 偶频活跃集（该点） ✓ | **空（严格内部）** ✓✓ |
| `0.876069` ✓ | **上界（不变）** ✓✓ |
| B1-β ✓ | **未进入（入口未满足）** ✗✓ |
| B1-α-3 ✓ | **下一刀（按既定顺序）** ✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 KKT 点不存在／方法失败 ✓
- **不**把"SLSQP 成功"当作 KKT（本档已明确其未移动）✓✓
- **不**声称 `0.876069` 是局部极小（LP 三档均 False）✓
- **不**用本次结果反驳次微分模型 ✓

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 未能定位genuineKKT 命中文件数=0    :: 
技术词 约束局部精修 命中文件数=0    :: 
技术词 优化器未动  命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{B1-}\alpha\text{-3}✓（\text{按既定顺序}✓）\text{：}|\mathcal A| \le 3\ \text{完整枚举}✓；\ \text{允许}\ \phi_j \to 0\ (x_j \to 1)✓；\ \textbf{interior／boundary KKT 分开登记}✓✓$$
$$\textbf{并附}✓：\text{换更强非光滑优化器}（\text{如多起点＋梯度束／子问题 LP 步}✓）\ \text{以真正前进}✓✓$$
$$\textbf{B1-}\beta✓：\ \text{仍须先有 genuine KKT}✗✓$$
