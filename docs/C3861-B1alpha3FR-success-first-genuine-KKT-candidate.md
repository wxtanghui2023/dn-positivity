已查地图（**先查后写**）：`C-3860`（**α-3 首刀 VOID：无可行初始化（病因已定位）** ✓✓）、`C-3859`（**SLSQP 未移动；硬规则「优化器成功 ≠ KKT」** ✓✓）、`C-3856`（**该点近 binding `{3,4,9}`；`0.876069` 为上界** ✓✓）、`C-3850`（**`0.876069` 构型** ✓✓）、`C-3855`（**可行构型 `0.9878`／`max_r F_2r = 0.4928`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-61：B1-α-3-FR —— 可行初始化恢复（独立审计对象）＋ 逐 σ `V_\sigma` ＋ KKT 审计**（唐先生 2026-09-21 22:31 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① FR 作为独立审计对象}✓✓：\text{初始化优先级}✓（C\text{-}3850 \to C\text{-}3855 \to \text{recovery}✓）；\ \textbf{逐项真函数复核}✓✓\ \text{（\textbf{不以 penalty 代替认证}✗✓）}$$

$$\qquad \text{认证结果}✓✓：`C-3850`\ \text{种子}\ \max_r(F_{2r} - \tfrac12) = -1.543\times10^{-4} \le 10^{-12}✓✓；\ `C-3855`\ \text{种子}\ = -7.252\times10^{-3}✓✓ \Longrightarrow \textbf{两种子均认证}✓✓$$

$$\qquad \Longrightarrow\ \text{16 个}\ \sigma\ \textbf{全部} \text{有认证可行起点}✓✓ \Longrightarrow \textbf{本轮无需 recovery}✓（\text{recovery 已实现备用}✓：\Psi = \sum_r[\max(0,F_{2r}-\tfrac12)]^2✓）$$

$$\textbf{② ⭐ 逐 σ 的}\ V_\sigma\ ✓✓（\text{bundle／trust-region}✓，\ \textbf{每个接受步真函数重算 12 个偶频}✓✓）$$

$$\qquad \Longrightarrow\ \text{16 个}\ V_\sigma\ \text{全部得到}✓✓；\ \text{最好}\ \boxed{V_\sigma = 0.868850348}✓✓\ \text{于}\ \sigma = (-1,1,1,-1,1)✓（\text{另一符号类同值}✓）$$

$$\qquad \text{其余}\ V_\sigma \in [1.77,\ 4.10]✓ \Longrightarrow \text{赢家}\ \textbf{明显离群}✓✓ \Longrightarrow \boxed{\text{上界}\ 0.876069 \to 0.868850}✓✓$$

$$\qquad \textbf{量词顺序锁死}✓✓：\ \gamma^{(13)} = \min_{\sigma}\underbrace{\min_{x \in E_{\mathrm{even}}}\max_{r \le 12}|F_{2r+1}^{(\sigma)}|}_{V_\sigma}✓✓；\ \textbf{绝不} \text{实现为}\ \min_x\max_\sigma\max_r✗✓$$

$$\textbf{③ ⭐⭐ KKT 审计：三档容差}\textbf{全部 True}✓✓$$

$$\qquad \boxed{\text{tol} = 10^{-7}／10^{-6}／10^{-5}\ \text{三档一致：KKT} = \textbf{True}✓✓,\ (\text{INTERIOR})✓✓}$$

$$\qquad \text{活跃结构}✓✓：|\mathcal I| = \mathbf{2}✓（\textbf{两个并列活跃奇频}✓✓ —— 与 `C-3857` 的"多重活跃"预期\ \textbf{一致}✓✓）；\ \mathcal A = \mathbf{\{3,4,7,9\}}✓（\textbf{四个活跃偶频}✓✓）$$

$$\qquad \text{点}✓：x = [0.80093,\ 0.56114,\ 0.70246,\ 0.62610,\ 0.86884]✓；\ \text{最小偶频余量} = -9.98\times10^{-13}✓（\text{在}\ 10^{-12}\ \text{容差内}✓）$$

$$\textbf{④ 判词（严格按唐先生纪律）}✓✓：\ \boxed{\text{登记为}\ \textbf{候选 E1（数值级）}}✓✓$$

$$\qquad \textbf{不}登记 E1\ \text{成立}✗✓：\text{按规格，E1 还需}\ \textbf{独立高精度复核}✓✓（\text{真目标水平}✓、\text{活跃集正确}✓、\text{interior／boundary 分离}✓、\omega,\lambda,\mu \ge 0✓、\text{完整法锥平衡}✓、\text{complementarity}✓）$$

$$\qquad \text{且点}\ \text{最小余量} = -9.98\times10^{-13} < 0✓ \Longrightarrow \textbf{只是容差内可行}✓,\ \textbf{不是精确可行}✗✓ \Longrightarrow \text{须}\ \textbf{抛光}✓（\text{polish}✓）\ \text{后再认证}✓✓$$

$$\textbf{⑤ 三出口状态}✓✓：\text{由}\ \textbf{VOID}\ \text{推进到}\ \boxed{\text{候选 E1（数值）}}✓✓；\ E2／E3\ \text{不适用}✗✓$$

$$\textbf{⑥ 自检（本刀修复的病因）}✓✓：\text{{C-3860} 的失效原因是}\ \textbf{无可行初始化}✓✓ \Longrightarrow \text{本次}\ \textbf{从认证可行点起}✓ \Longrightarrow \text{方法立刻有效}✓✓$$

$$\qquad \text{硬规则保留}✓✓：\ \boxed{\text{LP 可行} \not\Rightarrow \text{真问题可行}}✓✓ \Longrightarrow \text{每接受步}\ \textbf{真函数复核}✓（\text{本刀已实现}✓）$$

$$\textbf{⑦ 边界（不得越界）}✗✓：\textbf{不}声称 }\gamma^{(13)}\ \text{的真值}✗✓（`0.868850` 只是}\ \textbf{更紧的上界}✓）；\ \textbf{不}声称 E1 已成立}✗✓；\ \textbf{不}声称该点是全局极小}✗✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
0) 认证：C-3850 种子 max(F_2r-1/2) = -1.543e-04 (认证✓，max F_2r = 0.499846，min margin = 1.543e-04)
        C-3855 种子 max(F_2r-1/2) = -7.252e-03 (认证✓，max F_2r = 0.492748，min margin = 7.252e-03)
2) 逐 σ V_σ（24 起点/支，均自认证点扰动）：最好 0.868850348；其余 1.7666 ~ 4.1006
3) γ 上界（本轮）= 0.868850348，σ = (-1,1,1,-1,1)
   点 x = [0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389]；min margin = -9.984e-13
4) KKT 审计（次微分 LP，interior/boundary 分离）：
   tol=1e-7 : |I|=2, A=[3,4,7,9], bnd=[] -> KKT=True (INTERIOR)
   tol=1e-6 : 同上 -> True
   tol=1e-5 : 同上 -> True
```
- 脚本 ✓：`scripts/c380_61_B1alpha3FR.py`✓；输出 ✓：`scripts/out_c380_61_FR.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| FR（独立审计对象） ✓ | **两种子认证；无需 recovery** ✓✓ |
| 逐 σ `V_\sigma` ✓ | **16 个全部得到** ✓✓ |
| `\gamma^{(13)}` 上界 ✓ | **0.868850（由 0.876069 改进）** ✓✓ |
| KKT 候选 ✓ | **候选 E1（数值级，三档容差一致）** ✓✓ |
| E1 正式登记 ✓ | **未（须独立高精度复核 ＋ 抛光）** ✗✓ |
| E2／E3 ✓ | **不适用** ✓ |
| B1-β ✓ | **未进入（先完成 E1 认证）** ✗✓ |

## §3 本档**不**做的事 ✓✓

$$\textbf{不}进入 B1-}\beta✗✓；\ \textbf{不}把}\ 0.868850\ \text{当真值}✗✓；\ \textbf{不}把 KKT=True（数值）登记为 E1✗✓$$

## §4 边界（不得声称 ✗✓）

- **不**声称 E1 已成立（须独立高精度复核）✓
- **不**声称该点精确可行（余量 −9.98e-13）✓
- **不**声称全局极小／真值 ✓
- **不**声称其他 σ 分支已充分优化（只作上界比较）✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 可行初始化认证 命中文件数=0    :: 
技术词 候选E1         命中文件数=0    :: 
技术词 高精度复核  命中文件数=4    :: ./p49-g273p1r3d-odd-penetration.md ./C356-execution-stratification-registration-not-a-new-framework.md ./C352-3plus2-parametrization-first-cut-square-system-and-logic-lock.md
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 抛光}✓✓：\text{把候选点}\ \textbf{修成精确可行}✓（\text{polish}✓：\text{在偶频约束下最小化违反}✓，\ \text{同时保持目标水平}✓）$$
$$\textbf{② 独立高精度复核（E1 六项）}✓✓：\text{真目标水平}✓、\text{活跃奇频集}✓、\text{活跃偶频集}✓、\text{interior／boundary}✓、\omega,\lambda,\mu \ge 0✓\ \text{与完整法锥平衡}✓、\text{complementarity}✓✓$$
$$\textbf{③ 通过后}✓：\text{登记}\ \textbf{E1 genuine KKT}✓✓ \Longrightarrow \text{方可进入}\ B1\text{-}\beta\ \text{（二阶奇→偶耦合}✓）$$
$$\textbf{④ 若复核失败}✓：\text{退回}\ E2✓（\text{有有效候选但无法建立 genuine KKT}✓）\ \text{或}\ E3✓$$
