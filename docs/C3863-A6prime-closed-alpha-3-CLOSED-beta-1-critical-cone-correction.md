已查地图（**先查后写**）：`C-3862`（**POLISH ＋ A1–A5 CLOSED；A6 部分** ✓✓）、`C-3861`（**FR；上界 `0.868850`** ✓✓）、`C-3857`（**多重活跃结构** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-63：A6′（精确并列稳定性审计）＋ α-3 CLOSED ＋ β-1 首刀（临界锥表述修正）**（唐先生 2026-09-21 22:34 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 锁死的并列结构}✓✓：\ \boxed{\mathcal I = \{6,9\}}✓,\ \text{即频率}\ \boxed{k = 13,\ 19}✓✓,\ \text{符号}\ (-1,+1)✓；\ \text{基点 tie}\ \textbf{精确}✓$$

$$\qquad ⚠️ \textbf{索引纪律}✓✓：\text{本档起}\ \textbf{一律以频率}\ k\ \text{书写}✓（r = 6 \leftrightarrow k = 13✓）；\ \text{首版脚本混淆二者}\ \Longrightarrow \textbf{该版数据全部作废}✗✓$$

$$\textbf{② A6′-(1) 基点 tie 精度（40 dps）}✓✓：$$

$$\qquad F_{13} = \mathbf{-0.86885034832244968202}✓,\qquad F_{19} = \mathbf{+0.86885034832244832887}✓✓ \Longrightarrow \boxed{\Delta_{\mathrm{tie}} = 1.353\times10^{-15}}✓✓$$

$$\qquad \Longrightarrow\ \Delta_{\mathrm{tie}}\ \text{处于}\ \textbf{浮点表示地板}✓ \Longrightarrow \text{与}\ \textbf{精确并列} \text{一致}✓✓\ \text{（不是数值近似}✗✓）$$

$$\textbf{③ A6′-(2) 相对扰动测试（}\textbf{不用固定容差}✗✓）✓✓：$$

$$\qquad \Delta_{\mathrm{odd}}\ \text{随}\ \text{sd}\ \textbf{线性缩放}✓✓：\ 5.84\times10^{-7}／6.22\times10^{-5}／7.39\times10^{-3}／6.33\times10^{-1}\ \text{（sd} = 10^{-8}/10^{-6}/10^{-4}/10^{-2}✓）$$

$$\qquad \text{主导分支}\ \textbf{自由翻转}✓✓：144／145／129／159\ \text{（每 300 次抽样，期望} \approx 150✓） \Longrightarrow \boxed{\text{与精确基点 tie 一致}}✓✓$$

$$\qquad \Longrightarrow\ \text{唐先生判断成立}✓✓：\text{普通扰动后}\ |F_{13}| \ne |F_{19}|\ \textbf{完全正常}✗✓,\ \textbf{不能} \text{以此否定原 KKT 点}✗✓$$

$$\textbf{④ A6′-(3) }\omega\ \textbf{是结构性的，不是 tie-break}✓✓：$$

$$\qquad \omega = (0.903717944,\ 0.096282056)✓ \Longrightarrow \text{残差}\ 1.5\times10^{-9}✓,\ \lambda = [0.8379, 0.9897, 0.0419, 0.1273] \ge 0✓✓$$

$$\qquad \text{单支}\ \omega = (1,0)✓ \Longrightarrow \text{残差}\ \mathbf{0.4816}✗✓（\textbf{单支不足以平衡}✓）；\quad \omega = (0.5,0.5)／(0,1) \Longrightarrow \text{残差}\ 2.02／4.52✓\ \text{且}\ \lambda\ \textbf{出现负值}✗✓$$

$$\qquad \Longrightarrow\ \boxed{\text{两支凸组合是必需的}}✓✓ \Longrightarrow \omega\ \text{由几何决定}✓\ \textbf{不依赖} \text{数值 tie-break}✓✓$$

$$\textbf{⑤ A6′ 判词}✓✓：\textbf{CLOSED}✓✓（\text{三项全过}✓；\ \textbf{不判失败}✗✓） \Longrightarrow \boxed{\text{B1-}\alpha\text{-3} = \textbf{CLOSED}}✓✓\ \text{（按唐先生指令}✓）$$

$$\textbf{⑥ 该}\ \sigma\ \textbf{分支的数值候选值}✓✓：\ \boxed{V_\sigma \le 0.86885034832244940011}✓✓\ \text{（}\sigma = (-1,1,1,-1,1)✓）$$

$$\qquad ⚠️ \textbf{仍不写}\ V_\sigma = \cdots✗✓：\text{KKT 是}\ \textbf{必要条件}✓,\ \textbf{不是} \text{全局最优证书}✗✓$$

$$\textbf{⑦ β-1 首刀（临界锥表述须修正）}⚠️✓$$

$$\qquad \text{本次取}\ \textbf{活跃偶频梯度矩阵零空间}✓：\text{SVD 四个奇异值}\ (69.05,\ 41.25,\ 28.93,\ 14.05)\ \textbf{全非零}✓ \Longrightarrow \text{零空间}\ \text{1 维}✓$$

$$\qquad \text{但叠加}\ \textbf{tie 保持条件}✓ \Longrightarrow \boxed{\text{临界锥退化为}\ \{0\}}✗✓\ \text{（}h_0\ \text{上两奇频一阶变化}\ -0.4816\ \text{vs}\ +4.5208✓,\ \textbf{不满足 tie 保持}✗✓）$$

$$\qquad \Longrightarrow\ \text{该锥过小，}\ \textbf{二阶账本无对象}✗✓ \Longrightarrow \textbf{须修正临界锥表述}✓✓：\text{应含}\ \nabla F_{2q}\cdot h \le 0\ （\text{严格内移}✓）\ \text{与}\ s_1\nabla F_{13}\cdot h = s_2\nabla F_{19}\cdot h \le 0✓✓$$

$$\qquad \Longrightarrow\ \textbf{这不构成"机制失败"}✗✓,\ \text{而是}\ \textbf{首刀表述待修}⚠️✓$$

$$\qquad \text{（\textbf{有用的副产品}✓：}h_0\ \text{上奇频最大值}\ \textbf{双向增大}✓ \Longrightarrow \text{该}\ 1\ \text{维子空间内点}\ \textbf{是局部极小}✓✓）$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
基点恢复（5x5：四条 active 偶频等式 + tie）：残差 ~1e-16；x = [0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389]
A6'-(1)：F_13 = -0.86885034832244968202 ; F_19 = +0.86885034832244832887 ; Delta_tie = 1.353e-15（40 dps）
A6'-(2)：sd=1e-8/1e-6/1e-4/1e-2 -> max delta_odd = 5.84e-7 / 6.22e-5 / 7.39e-3 / 6.33e-1（线性缩放）
         主导分支计数（每 300）：144 / 145 / 129 / 159
A6'-(3)：omega=(0.903717944, 0.096282056) -> 残差 1.5e-9, lambda=[0.83791706,0.98971406,0.04185319,0.12728511] >= 0
         omega=(1,0) -> 残差 0.4816（lambda >= 0 但不可平衡）；omega=(0.5,0.5) -> 2.02 且 lambda 有负；
         omega=(0,1) -> 4.52 且 lambda 有负
β-1：活跃偶频梯度矩阵奇异值 [69.05, 41.25, 28.93, 14.05]；零空间 1 维 h0 = [0.6975,0.3410,0.4024,0.3358,0.3500]
     一阶奇频变化 s1 dF13.h0 = -4.816e-01 ; s2 dF19.h0 = +4.521e+00 ; omega 加权 = -1.5e-9（与 KKT 一致 ✓）
     叠加 tie 保持 -> 临界锥 = {0} ⟹ 二阶账本无对象（表述待修）
（首版脚本 r/频率 混用 -> 全部作废；已由内建 KKT 平衡一致性检查捕获 ✓）
```
- 脚本 ✓：`scripts/c380_63_A6prime_beta1_v2.py`✓（作废版 `c380_63_A6prime_beta1.py` 保留为审计痕迹 ✓）；输出 ✓：`scripts/out_c380_63_A6p_beta1.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| A6′（三项） ✓ | **CLOSED** ✓✓ |
| **B1-α-3** ✓ | **CLOSED（唐先生指令）** ✓✓ |
| `V_\sigma \le 0.86885034832244940011` ✓ | **数值候选值（非等式）** ✓✓ |
| E1 genuine KKT（局部） ✓ | **已建立（A1–A6′ 全过）** ✓✓ |
| 全局 `V_\sigma` 证书 ✓ | **未（KKT 仅必要）** ✗✓ |
| β-1 ✓ | **首刀：临界锥表述待修** ⚠️✓ |
| 奇/偶二阶账本 ✓ | **未成立（无对象）** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 `V_\sigma = 0.868850…`（只 `\le`）✓
- **不**声称全局最优 ✓
- **不**把 β-1 的锥退化当机制失败 ✓
- **不**引用首版（r/频率混用）的任何数字 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}重跑\ \alpha\text{-3}✗；\ \textbf{不}重找 KKT}✗；\ \textbf{不}开全局 Fejér／Chebyshev✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 精确并列审计 命中文件数=0    :: 
技术词 临界锥退化  命中文件数=0    :: 
技术词 结构性权重  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{β-1 修正版}✓✓：\text{临界锥改为}\ \{\nabla F_{2q}\cdot h \le 0\ (\forall q \in \mathcal A)\} \cap \{s_1\nabla F_{13}\cdot h = s_2\nabla F_{19}\cdot h \le 0\}✓✓$$
$$\qquad \text{在此锥上做}\ \textbf{二阶账本}✓：k = 13,19\ \text{对}\ k = 12,16,28,36\ \text{（即}\ F_6, F_8, F_{14}, F_{18}✓）$$
$$\qquad \textbf{硬条件}✓✓：\beta\ \text{必须同时使用}\ F_6, F_8, F_{14}, F_{18} \le \tfrac12✓；\ \text{若删除偶频约束后仍成立} \Longrightarrow \textbf{非 gamma 机制}✗✓$$
