已查地图（**先查后写**）：`C-3863`（**A6′ CLOSED；α-3 CLOSED；`V_\sigma \le 0.86885034832244940011`；β-1 首刀锥表述待修** ✓✓）、`C-3862`（**POLISH ＋ A1–A5** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-64：B1-β-1′ —— 正确临界锥 ＋ 二阶账本 ＋ 成对 control（删偶频约束）**（唐先生 2026-09-21 22:36 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 规格（只以频率}\ k\ \text{书写}✓✓）:}\ \sigma = (-1,1,1,-1,1)✓;\ \mathcal I = \{13,19\}✓\ (s_{13} = -1,\ s_{19} = +1✓);\ \mathcal A = \{6,8,14,18\}✓✓$$

$$\qquad \text{（即偶频}\ F_6, F_8, F_{14}, F_{18}✓\ ——\ \text{对应频率}\ 12,16,28,36✓）$$

$$\textbf{② 正确临界锥（}\textbf{含不等式，不强制取等}✓✓）:\ }\ \mathcal C = \{h:\ \nabla F_6h \le 0,\ \nabla F_8h \le 0,\ \nabla F_{14}h \le 0,\ \nabla F_{18}h \le 0,\ - \nabla F_{13}h \le 0,\ + \nabla F_{19}h \le 0\}✓✓$$

$$\textbf{③ ⭐ 完整问题：}\textbf{不存在严格一阶下降方向}✓✓:\ \text{LP}\ \max t\ \text{s.t. 六条} \le -t✓,\ |h|_\infty \le 1✓ \Longrightarrow \boxed{t^* = 0}✓✓（\text{最优}\ h = 0✓）$$

$$\qquad \Longrightarrow\ \text{当前 KKT 点}\ \textbf{通过一阶检验}✓✓\ \text{（不是 C1／B1}✗□ \text{即}\ \textbf{不是"非局部极小"}\ ✗✓）$$

$$\textbf{④ ⭐⭐ Control（删掉偶频约束）:\ }\textbf{严格下降存在}✓✓:\ \boxed{t^*_{\mathrm{control}} = +1.000000}✓✓,\ h = (-1,-1,-1,1,1)✓$$

$$\qquad \Longrightarrow\ \boxed{t^*_{\mathrm{full}} = 0\ \ \text{vs}\ \ t^*_{\mathrm{control}} = +1}✓✓ \Longrightarrow \textbf{成对 control 发生实质改变}✓✓$$

$$\qquad \Longrightarrow\ \text{障碍}\ \textbf{只在加入}\ F_6,F_8,F_{14},F_{18} \le \tfrac12\ \textbf{后出现}✓✓,\ \text{删去即消失}✓✓ \Longrightarrow \boxed{\text{出口}\ \textbf{B3（一阶形式）}}✓✓$$

$$\qquad \Longrightarrow\ \textbf{偶频约束是唯一障碍源}✓✓ \Longrightarrow \text{这是}\ \textbf{第一次}\ \text{拿到}\ \text{odd}\to\text{even}\ \text{桥的}\ \textbf{直接证据}✓✓$$

$$\qquad \text{（\textbf{anti-circularity 硬门}\ \textbf{通过}✓✓：若删偶频后结论相同} \Longrightarrow \text{非 gamma 机制}✗□；\ \text{实测}\ \textbf{不同}✓✓）$$

$$\textbf{⑤ 基线方向}\ h_0\ \text{的诊断}✓✓:\ h_0 = [0.6975, 0.3410, 0.4024, 0.3358, 0.3500]✓$$

$$\qquad \text{偶频一阶}\ \nabla F_{2q}\cdot h_0 \approx 0✓\ \text{（全}\ \approx 0✓,\ \textbf{在偶频切空间内}✓）;\qquad \text{奇频一阶} = (-0.4816,\ +4.5208)✓$$

$$\qquad \Longrightarrow\ h_0\ \textbf{不在}\ \mathcal C\ \text{内}✓（\text{第二支}\ +4.5208 > 0✗） \Longrightarrow \text{按唐先生要求：}\textbf{不称其为 critical direction}✗✓,\ \textbf{仅作基线}✓✓$$

$$\textbf{⑥ 二阶账本}⚠️✓:\ \text{锥}\ \mathcal C\ \textbf{退化}✓：60\,000\ \text{个随机单位方向中}\ \textbf{0 个} \text{满足六条不等式}✓✓ \Longrightarrow \text{锥}\ \textbf{几乎只有}\ \{0\}✓ \Longrightarrow \textbf{二阶对象不存在}✗✓$$

$$\qquad \Longrightarrow\ \text{本档}\ \textbf{不}给出}\ Q_k(h)\ \text{的判词}✗✓\ \text{（}\textbf{不是"没有方向"}✗□，\ \text{而是}\ \textbf{锥退化}\ ⟹\ \textbf{无合法二阶对象}，\ \text{登记为}\ \textbf{VOID（二阶部分）}⚠️✓）$$

$$\qquad \text{（副产品}✓：锥退化本身}\ \textbf{强化} \text{局部极小性}✓：\text{连}\ \textbf{一阶} \text{下降都不可能}✓✓）$$

$$\textbf{⑦ 出口分类}✓✓:\ \boxed{\text{B3（一阶形式）}}✓✓\ \text{—— 唯一障碍源是偶频约束}✓；\ \text{B1／B2}\ \textbf{不成立}✗□；\ \text{二阶部分}\ \textbf{VOID}⚠️✓$$

## §1 数值记录（数字驱动 ✓✓）

```
点恢复（5x5）：残差 1.6e-15 ; x = [0.80093022,0.5611432,0.70245716,0.6261014,0.86884389]
1) 完整 LP：t* = -0.000000e+00（最优 h = 0）-> 无严格一阶下降
2) Control LP（删四条偶频）：t* = +1.000000e+00，h = (-1,-1,-1,1,1) -> 严格下降存在
   成对差异：0 vs +1 -> 实质改变 = True
3) h0：偶频一阶 [-0,0,-0,-0]（≈0）；奇频一阶 [-0.481644, +4.520807] -> 不在锥内（第二支 > 0）
4) 锥采样：60 000 单位方向中 0 个满足六条不等式 -> 锥退化；未发现二阶下降方向
```
- 脚本 ✓：`scripts/c380_64_beta1prime.py`✓；输出 ✓：`scripts/out_c380_64_beta1p.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 正确临界锥（不等式版） ✓ | **已实现** ✓✓ |
| 完整问题一阶检验 ✓ | **通过（t* = 0）** ✓✓ |
| 成对 control ✓ | **实质改变（0 vs +1）** ✓✓ |
| **出口** ✓ | **B3（一阶形式）** ✓✓ |
| 二阶账本 ✓ | **VOID（锥退化，无对象）** ⚠️✓ |
| anti-circularity 硬门 ✓ | **通过（删偶频后结论不同）** ✓✓ |
| 全局 `V_\sigma` 证书 ✓ | **未** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 odd→even 桥已定量化（本档只给**一阶**障碍源）✓
- **不**声称二阶机制成立（锥退化）✓
- **不**把"锥退化／无方向"写成"没有方向"的判词（VOID）✓
- **不**引用作废版（r/频率混用）数字 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}重跑}\ \alpha\text{-3}✗；\ \textbf{不}改}\ V_\sigma\ \text{的}\ \le\ \text{记号}✗；\ \textbf{不}开全局 Fejér／Chebyshev✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 成对control    命中文件数=0    :: 
技术词 一阶障碍源  命中文件数=0    :: 
技术词 临界锥退化  命中文件数=1    :: ./C3863-A6prime-closed-alpha-3-CLOSED-beta-1-critical-cone-correction.md
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{β-2}✓✓：\textbf{定量化一阶桥}✓：\text{把}\ \text{"奇频下降}\ \delta\ \Longrightarrow\ \text{某偶频必须上升}\ \ge c(\delta)"\ \text{写成显式不等式}✓✓$$
$$\qquad \text{工具}✓：\ \text{六个一阶量的}\ \textbf{Farkas 对偶}✓（\text{锥退化}\ ⟹\ \text{存在非负组合}\ \sum \mu_q\nabla F_{2q} + \sum \nu_k s_k\nabla F_k = 0✓\ \text{即 KKT}✓✓）$$
$$\textbf{注意}✓：\text{本档的}\ B3\ \text{是}\ \textbf{一阶} \text{结论}✓；\ \text{二阶（若需）}\ \text{须先把锥表述扩展到}\ \textbf{等号面}✓$$
