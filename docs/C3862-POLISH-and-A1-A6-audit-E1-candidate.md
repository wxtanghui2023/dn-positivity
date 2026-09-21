已查地图（**先查后写**）：`C-3861`（**FR 成功；上界 `0.868850`；KKT 候选（数值）** ✓✓）、`C-3860`（**VOID（无可行初始化）已封闭** ✓✓）、`C-3857`（**多重活跃结构预测** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-62：B1-α-3-POLISH（等式化 active system）＋ A1–A6 独立复核**（唐先生 2026-09-21 22:36 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① POLISH（等式化主动系统）}✓✓：\text{固定}\ \sigma = (-1,1,1,-1,1)✓,\ \mathcal I = \{6,9\}✓,\ \mathcal A = \{3,4,7,9\}✓；\ \text{解}✓：$$

$$\qquad \boxed{F_{2q}(\phi) = \tfrac12\ (q \in \mathcal A)}✓✓,\qquad \boxed{s_1F_{13} = s_2F_{19}}✓（\text{等波纹}✓）,\qquad \boxed{\omega_1s_1\nabla F_{13} + \omega_2s_2\nabla F_{19} + \sum_{q \in \mathcal A}\lambda_q\nabla F_{2q} = 0}✓✓$$

$$\qquad 10 \times 10\ \text{方阵}✓（\phi\ 5 ＋ \omega\ 1 ＋ \lambda\ 4✓）,\ \text{Newton 自候选点}✓✓ \Longrightarrow \boxed{\text{残差}\ 1.155\times10^{-14}}✓✓$$

$$\textbf{② A1 真目标水平}✓✓：\ \boxed{t = 0.86885034832244940011}✓（\textbf{40 位}dps✓）；\ \text{待复核值}✓（\textbf{不是} \text{已认证的}\ \gamma^{(13)}✗✓）$$

$$\textbf{③ A2 活跃集（独立重扫，}\textbf{不预设}✗✓）✓✓：\ \mathcal I = \{6, 9\}✓（\text{两值差}\ 1.15\times10^{-16}✓）；\ \mathcal A = \{3,4,7,9\}✓（|F_{2q} - \tfrac12| \le 1.9\times10^{-15}✓✓）$$

$$\qquad \text{inactive 偶频}\ \textbf{最小余量} = \mathbf{4.768\times10^{-2}}✓✓ \Longrightarrow \textbf{严格正 slack}✓✓$$

$$\\textbf{④ A3 interior}✓✓：0 < \phi_j < \tfrac{\pi}{2}\ \text{逐项成立}✓ \Longrightarrow \boxed{\mu_j = 0}✓✓$$

$$\textbf{⑤ A4 完整次梯度平衡（直接计算，}\textbf{不用 LP 残差}✗✓）✓✓$$

$$\qquad \omega_1 = \mathbf{0.903717944}✓,\quad \omega_2 = \mathbf{0.096282056}✓\ (\text{均} \ge 0✓,\ \text{和} = 1✓)$$
$$\qquad \lambda = [\mathbf{0.83791706},\ \mathbf{0.98971406},\ \mathbf{0.04185319},\ \mathbf{0.12728511}]✓\ (\text{全} \ge 0✓✓)$$
$$\qquad \|\text{站性平衡}\|_\infty = \mathbf{1.155\times10^{-14}}✓✓$$

$$\qquad \textbf{法锥符号约定（唐先生要求显式检查）}✓✓：\text{约束} F_{2q} \le \tfrac12\ \text{取}\ +\lambda_q\nabla F_{2q}\ (\lambda_q \ge 0)✓✓；\ \text{boundary 才加}\ -\mu_j e_j✓；\ \text{本点为 interior} \Longrightarrow \mu = 0✓✓$$

$$\textbf{⑥ A5 complementarity}✓✓：\max_q|\lambda_q(F_{2q} - \tfrac12)| = \mathbf{3.846\times10^{-16}}✓✓；\ \text{inactive}\ \lambda = 0✓；\ \mu_j = 0✓$$

$$\textbf{⑦ A6 稳定性}✓✓（\textbf{一项待闭合}⚠️✓）$$

$$\qquad \textbf{(i) 精度层级}✓✓：\text{tol} = 10^{-7}／10^{-9}／10^{-11}\ \text{三档识别出的}\ (\mathcal I, \mathcal A)\ \textbf{完全一致}✓✓ = (\{6,9\},\ \{3,4,7,9\})✓$$

$$\qquad \textbf{(ii) 扰动测试}⚠️✓：40 次扰动（sd = 10^{-9}）\textbf{全部"跳变"}✓✗ \Longrightarrow \textbf{但这是容差人工产物}✓✓：\text{点的}\ |F_6| = |F_9|\ \text{是}\ \textbf{精确并列}✓（等波纹条件的一部分✓），\ 10^{-9}\ \text{扰动必然打破并列}✓，\ \text{而}\ \textbf{固定} 10^{-9}\ \text{容差} \text{就只识别出一个}✓ \Longrightarrow \textbf{不构成"active set 不稳定"}✗✓$$

$$\qquad \Longrightarrow\ \text{须改用}\ \textbf{相对扰动容差}（\text{如}\ 20\times\text{sd}✓）\ \text{重测}✓\ \Longrightarrow \textbf{登记为 A6 待闭合项}⚠️✓$$

## §1 数值记录（数字驱动 ✓✓）

```
step0（独立扫描）：t0 = 0.868850291888 ; I = [6, 9]（符号 -1, +1）; A = [3,4,7,9]
step1（POLISH 10x10 Newton）：残差 1.155e-14
   omega = 0.903717944（omega2 = 0.096282056）
   lambda = [0.83791706, 0.98971406, 0.04185319, 0.12728511]
   x = [0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389]
A1/A2：t = 0.868850348322 ; tied odd（1e-12）= [6,9] ; active even（1e-12）= [3,4,7,9] ;
       inactive 偶频最小余量 = 4.768e-02
A3：interior（phi>0 且 phi<pi/2）⟹ mu = 0
A4：||平衡||_inf = 1.155e-14 ; omega >= 0 ; lambda >= 0
A5：max|lambda_q (F_2q - 1/2)| = 3.846e-16
A6：精度层级三档一致 ; 扰动（sd=1e-9，固定容差 1e-9）40/40 跳变 ⟹ 容差人工产物，须改相对容差重测
40 dps 认证：max|F_2q - 1/2| = 1.937e-15 ; |F_13| - |F_19| = -1.1526e-16 ; t = 0.86885034832244940011
```
- 脚本 ✓：`scripts/c380_62_polish_audit.py`✓；输出 ✓：`scripts/out_c380_62_polish.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| POLISH（等式化 active system） ✓ | **完成（残差 1.2e-14）** ✓✓ |
| A1 真目标水平 ✓ | **CLOSED（40 dps）** ✓✓ |
| A2 活跃集（独立重扫） ✓ | **CLOSED** ✓✓ |
| A3 interior／boundary ✓ | **CLOSED（interior；μ = 0）** ✓✓ |
| A4 完整次梯度平衡 ✓ | **CLOSED（ω,λ ≥ 0；余量 1.2e-14）** ✓✓ |
| A5 complementarity ✓ | **CLOSED** ✓✓ |
| A6 稳定性 ✓ | **部分：精度层级 CLOSED；扰动-相对容差待闭合** ⚠️✓ |
| E1 判词 ✓ | **仍为 candidate（未登记 E1 成立）** ⚠️✓ |
| B1-β ✓ | **未进入** ✗✓ |

## §3 判词纪律（唐先生，严格保留）✓✓

$$\text{即使六项全过}✓ \Longrightarrow \textbf{只能} \text{得到}\ \boxed{\text{E1 = genuine KKT candidate}}✓✓;\ \textbf{不得} \text{写成}\ \gamma^{(13)} = 0.868850348✗✓,\ \textbf{更不得} \text{推出全局最优}✗✓$$

$$\qquad \text{升级链}✓✓：\text{candidate E1} \to \text{genuine KKT} \to \textbf{局部二阶审计} \to \boxed{\text{全局}\ V_\sigma\ \text{证书}}✓✓$$

## §4 边界（不得声称 ✗✓）

- **不**声称 `\gamma^{(13)}` 的真值 ✓
- **不**声称该点为全局极小 ✓
- **不**声称 A6 已完全闭合 ✓
- **不**在 A1–A6 全闭合前进入 B1-β ✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 等式化active系统 命中文件数=0    :: 
技术词 扰动容差人工产物 命中文件数=0    :: 
技术词 genuineKKT候选 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 闭合 A6}✓✓：\text{改}\ \textbf{相对扰动容差}（20\times\text{sd}✓）\ \text{重测}✓；\ \text{并补}\ \textbf{并列结构的退化方向审计}✓（|\mathcal I| = 2\ \text{的切锥}✓）$$
$$\textbf{② A1–A6 全闭合后}✓✓：\text{登记}\ \textbf{E1 genuine KKT}✓ \Longrightarrow \text{开}\ B1\text{-}\beta✓（\text{二阶奇}\to\text{偶耦合}✓：\text{两条 active odd ＋ 四条 active even}✓）$$
$$\textbf{③ 全局性控制}✓：V_\sigma\ \text{的全局最小证书}✓\ \text{（独立于局部 KKT}✓）$$
