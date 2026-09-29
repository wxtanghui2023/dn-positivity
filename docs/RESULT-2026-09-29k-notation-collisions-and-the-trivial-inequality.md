# RESULT-k（2026-09-29）—— **三处记号冲突 ＋ 新不等式"真但极弱"**；slice 条件即 $\mathrm{Def}\le9a-406$（回到循环）

> **性质**：**记号核对 ＋ 实测**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:35 ✓

**已查地图**：`RESULT-j`（度数集中）／`RESULT-i`（$f$ 表）／`RESULT-c`（两来源恒等式）✓

D0: 本档对象 ＝ **档案已有**（profile／矩—经典 ✓）
D1: 0（产出＝**三记号冲突 ＋ 一恒真式否定 ＋ 一循环提醒** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ⚠️ 三处记号冲突（必钉）}:\ A_i^{\rm pair}\ne A_i^{\rm prof};\ T\ \text{两定义};\ A\ \text{非 packing}}$$
$$\boxed{\text{② 新不等式恒真但弱}:\ 2A_0+\sum_{i\ge3}\bigl(2+\tbinom i3\bigr)A_i^{\rm prof}<1430-9a\ \text{—— }25/25✓\ \text{但松弛 }4\text{--}7\ \text{倍}\ ✗}$$
$$\boxed{\text{③ }F(A)=\mathrm{Def}(A)=\sum_{i\ge1}(i-1)A_i^{\rm prof}\ ✓\ (\text{正确恒等式})}$$
$$\boxed{\text{④ slice 条件\ \textbf{即}}\ \mathrm{Def}\le9a-406;\ \text{随机子集仅 }12/25\ \text{满足}\ \Longrightarrow\ \text{约束来自互补性本身}✗}$$

## §1 三处记号冲突（⚠️ 必钉）

$$\textbf{（甲）}\ A_d^{\rm pair}:=\#\{\text{码字对，距离 }d\}\quad\ne\quad A_i^{\rm prof}:=\#\{x:\mu(x)=i\}$$
$$\text{关系}:\ 2\bigl(A_1^{\rm pair}+A_2^{\rm pair}\bigr)=\sum_i\tbinom i2A_i^{\rm prof}\ ✓\qquad\text{（不可混用）}✗$$
$$\textbf{（乙）}\ T=\sum_x\tbinom{\mu(x)-1}2\ (\text{我方，已核实})\ \ne\ \sum_x\tbinom{w_x}3\ ✗$$
$$\textbf{（丙）}\ A=P\cup Q\ \textbf{不是}\ 3\text{-packing}✗\ (\text{仅 }P\ \text{是};\ Q\ \text{之点距 }P\le2)$$
$$\therefore\ \text{"不同 }A\text{-点之半径 1 球互不相交"}\ \textbf{为假};\ \text{真恒等式}:\ \sum_i iA_i^{\rm prof}=10a✓$$

## §2 新不等式实测（✓ 恒真但弱）

$$2A_0+\sum_{i\ge3}\Bigl(2+\tbinom i3\Bigr)A_i^{\rm prof}\ <\ 1430-9a$$

| 目标 | $25$ 样本成立 |
|---|---|
| 上式 | $\mathbf{25/25}\ ✓$ |
| $\mathrm{Def}(A)>9a-406$ | $12/25$（随机子集不必为合法 slice） |

$$\text{LHS}\in[128,258]\quad\text{vs}\quad\text{RHS}\in[908,998]\ \Longrightarrow\ \textbf{松弛 4--7 倍}✗$$
$$\therefore\ \boxed{\text{恒真（}$A_0$\text{ 小、高重 }A_i\text{ 少）};\ \textbf{无信息量}\ (\text{类 2})}$$

## §3 正确恒等式与回归的循环（✓）

$$\boxed{F(A)=\mathrm{Def}(A)=\sum_{i\ge1}(i-1)A_i^{\rm prof}}\ ✓\quad(\text{由}\ \sum\tbinom\mu2-\sum\tbinom{\mu-1}2)$$
$$\text{slice 条件}\ \iff\ \mathrm{Def}(A)\le9a-406;\quad \text{实测随机子集 }12/25\ \text{满足}$$
$$\therefore\ \boxed{\text{起约束者 ＝ slice/互补性本身};\ \text{而 fiber 分解 ＝ 精确重述}✗\ \text{—— 与前几轮同型循环}}⚠️$$

## §4 边界（硬 ✓）

- **三记号冲突与实测（$25$ 样本、松弛倍数）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本文**判定该不等式无信息量**✗

## §5 【技术词回查】（**提交前实跑，逐字粘贴**）

```
记号冲突三处 : 技术词 记号冲突三处 命中文件数=0    ::
profile重参数化 : 技术词 profile重参数化 命中文件数=0    ::
真但极弱 : 技术词 真但极弱     命中文件数=0    ::
```
