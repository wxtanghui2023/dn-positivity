已查地图（**先查后写**）：`C-3848`（**H1 数值：16 点／`min F_9 = +4`** ✓✓）、`C-3847`（**原始定义回填：r ≤ 12；证书在 r = 9 失败** ✓✓）、`C-375`／`C-342`（**`E_{\mathrm{even}}`：r = 1..12** ✓✓）、`C-380-21A`（**`E_0 = \bigcup_j\{x_j = 0\}`；S_5 对称 ⟹ WLOG `x_5 = 0`** ✓✓）、`C-380-12` §2（**若 `E_0` 关闭 ⟹ 资产 `x_j > 0`** ✓✓）、`C-380-22` M2 过滤器（**"单一非负线性组合 ⟹ C-380-13 已封"** ⚠️✓）、`C-3814`（**trig-dual sharp 封口 `\sigma \le 6c_0`** ⚠️✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-49：H1 刚性引理的证明（Fejér 核）＋ 边界层闭合（`E_0 \cap E_{\mathrm{even}} = \varnothing`）**（唐先生 2026-09-21 21:10 发令 H1-α）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① ⭐⭐⭐⭐ 定理（H1 刚性引理，已证）}✓✓：\text{设}\ z_1,\dots,z_4 \in S^1✓,\ F_r := \sum_{j=1}^{4}\Re z_j^r✓；\ \text{若}\ \boxed{F_r \le -\tfrac12,\quad r = 1,\dots,8}✓ \Longrightarrow$$

$$\qquad \boxed{z_j \in \mu_9 \setminus \{1\}\ \ \forall j}✓✓,\qquad \boxed{F_1 = \dots = F_8 = -\tfrac12}✓✓,\qquad \boxed{F_9 = +4}✓✓$$

$$\textbf{② 证明（六行，Fejér 核）}✓✓：\text{对}\ \psi \in \mathbb R\ \text{令}\ \boxed{K_9(\psi) := \tfrac19\Big|\sum_{k=0}^{8}e^{ik\psi}\Big|^2}✓✓ \ge 0✓\ \text{（Fejér 核，标准）}✓✓$$

$$\qquad (a)\ \text{展开}✓：K_9(\psi) = 1 + \tfrac29\sum_{r=1}^{8}(9-r)\cos(r\psi)✓✓;\qquad (b)\ \text{四节点求和}✓：\sum_jK_9(\psi_j) = 4 + \tfrac29\sum_{r=1}^{8}(9-r)F_r✓✓$$

$$\qquad (c)\ \text{约束}✓：F_r \le -\tfrac12 \Longrightarrow \sum_{r=1}^{8}(9-r)F_r \le -\tfrac12\sum_{r=1}^{8}(9-r) = -18✓✓\ \Longrightarrow\ \boxed{\sum_jK_9(\psi_j) \le 4 + \tfrac29(-18) = 0}✓✓$$

$$\qquad (d)\ K_9 \ge 0 \Longrightarrow \sum_jK_9 \ge 0✓\ \text{与 (c) 夹死} \Longrightarrow \sum_jK_9 = 0 \Longrightarrow \boxed{K_9(\psi_j) = 0\ \forall j}✓✓$$

$$\qquad (e)\ K_9(\psi) = 0 \iff \sum_{k=0}^{8}e^{ik\psi} = 0 \iff \boxed{e^{9i\psi} = 1,\ e^{i\psi} \ne 1}✓✓ \Longrightarrow z_j \in \mu_9\setminus\{1\}✓✓$$

$$\qquad (f)\ \text{回代 (c) 等号}✓：\text{每项}\ (9-r)(F_r + \tfrac12) \le 0\ \text{且和 = 0} \Longrightarrow \text{每项 = 0} \Longrightarrow F_r = -\tfrac12\ (r \le 8)✓✓;\quad F_9 = \sum_j\Re z_j^9 = 4✓✓\ \ \blacksquare$$

$$\textbf{③ ⭐⭐ 推论一：边界层闭合（`E_0 \cap E_{\mathrm{even}} = \varnothing`，证明级）}✓✓$$

$$\qquad \text{由}\ C\text{-}380\text{-}21A✓：E_0 = \bigcup_j\{x_j = 0\}✓,\ \text{WLOG}\ x_5 = 0✓ \Longrightarrow y_5 = -1✓ \Longrightarrow \sum_{j=1}^{4}T_{2r}(y_j) \le \tfrac12 - 1 = -\tfrac12✓✓$$

$$\qquad \text{取}\ z_j := e^{2i\theta_j}✓\ (y_j = \cos\theta_j✓) \Longrightarrow \Re z_j^r = \cos(2r\theta_j) = T_{2r}(y_j)✓✓ \Longrightarrow \text{四点问题满足}\ r = 1..12✓\ \text{（含}\ r \le 8✓）$$

$$\qquad \text{由定理}✓：\text{任何这样的点已有}\ F_9 = +4 > -\tfrac12✗\ \text{而}\ 9 \in \{1,\dots,12\}✓ \Longrightarrow \boxed{E_0 \cap E_{\mathrm{even}} = \varnothing}✓✓\ \text{（证明级）}$$

$$\qquad \Longrightarrow\ \text{`C-380-12` §2 的资产成立}✓✓：\boxed{x_j > 0\ \ \forall j,\ \forall x \in E_{\mathrm{even}}}✓✓;\ \ E_{\mathrm{even}} \subset [0,1]^5\ \text{闭 ⟹ 紧}✓ \Longrightarrow \boxed{\inf_j x_j > 0}✓✓$$

$$\textbf{④ ⭐ 推论二：极值集完全分类（精确）}✓✓：\text{定理给出}\ z_j \in \mu_9\setminus\{1\}✓;\ \text{八条取等}✓ \Longrightarrow \text{4-子集}\ S \subset \{1,\dots,8\}✓\ \text{恰 16 个}✓✓：$$

$$\qquad \boxed{S = \{s_1,s_2,s_3,s_4\},\quad s_k \in \{k,\ 9-k\}\ \ (k = 1,2,3,4)}✓✓\ \text{（每个共轭对}\ \{k,9-k\}\ \text{各取一个} ⟹ 2^4 = 16✓✓）$$

$$\qquad \text{数值验证}✓✓：\binom{8}{4} = 70\ \text{中恰 16 个满足八条}✓;\ \text{与"共轭对各取一"}\ \textbf{完全一致}✓✓;\ \text{全部八条}\ \textbf{精确取等}✓;\ F_9 = 4✓✓$$

$$\textbf{⑤ 唐先生要找的结构：非负组合确实存在}✓✓：\text{权重}\ \boxed{c_r = 9-r > 0}✓✓\ \Longrightarrow$$

$$\qquad \boxed{\sum_{r=1}^{8}(9-r)\Big(F_r + \tfrac12\Big) = \tfrac92\sum_{j=1}^{4}K_9(\psi_j) \ \ge\ 0}✓✓\ \text{（恒等式，数值残差}\ 7\times10^{-14}✓✓）$$

$$\qquad \text{等号条件恰为}\ F_r = -\tfrac12\ \text{且}\ K_9(\psi_j) = 0\ \text{即}\ z_j^9 = 1✓✓\ \text{—— 与唐先生设想的结构完全一致}✓✓$$

$$\qquad \text{另注}✓：\text{均匀权重（}c_r = 1\text{）}\ \textbf{正是失败的那把刀}✗✓\ \text{（`C-3848` §0⑥）}⟹\ \text{差别全部在}\ c_r = 9-r✓✓$$

$$\textbf{⑥ ⚠️ 与档案既有登记的冲突（须审计，本档不裁决）}⚠️✓：\ C\text{-}380\text{-}22\ \text{M2 写道"单一非负线性组合仍属 Fourier-dual ⟹ `C-380-13` 已 CLOSED／duplicate"}✓;$$

$$\qquad \text{而本档 (⑤) 恰给出一个}\ \textbf{单一非负线性组合}✓\ \text{且}\ \textbf{它有效}✓✓ \Longrightarrow\ \text{两者}\ \textbf{表面冲突}✗✓$$

$$\qquad \text{最可能的解释}✓（待核）：C\text{-}3814\ \text{的 sharp 封口是}\ \textbf{定量上界}\ \sigma \le 6c_0✓,\ \text{并非"线性对偶不能证空性"}✓;$$

$$\qquad \qquad \text{另可能}✓：M2 针对的是}\ \textbf{五项原子}＋\textbf{奇频目标}\ \text{的语境}✓,\ \text{而本档处理}\ \textbf{边界层空性}✓✓\ \text{—— 不同命题}✓$$

$$\qquad \Longrightarrow\ \textbf{登记为待审计项}✓✓：\text{读 `C-380-13`／`C-3814` 正文，判定 M2 的适用范围}✓\ \text{—— }\textbf{在核清之前不得声称 M2 有误}✗✓$$

$$\textbf{⑦ H1-α 的 α1／α2 被}\textbf{取代}✓✓：\text{定理}\ \textbf{坐标无关}✓、\ \textbf{零枚举}✓、\ \textbf{零浮点}✓ \Longrightarrow\ \text{70 组 active set 与退化分支}\ \textbf{均无需执行}✓✓$$

$$\qquad \text{唐先生五项验收标准在此路径下}\ \textbf{自动满足}✓✓（\text{精确证明}✓；\ \text{不依赖浮点聚类}✓；\ \text{分类为推论而非前提}✓）$$

$$\qquad \text{保留}✓：\text{精确组合分类（}C(8,4) = 70 \to 16✓）\ \text{已用}\ 50\ \text{位精度独立核验}✓✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 证明的边界（防越界 ✓✓）

$$\textbf{(i)}\ \text{本档只闭合}\ \textbf{边界层}\ E_0 \cap E_{\mathrm{even}}✓✓\ ——\ \textbf{不}闭合 Bridge A✗、\textbf{不}给奇频 discrepancy 界✗$$
$$\textbf{(ii)}\ \text{定理的假设是}\ r \le 8✓；E_0^{(12)}\ \text{含}\ r \le 12✓ \Longrightarrow\ \text{闭包成立}✓✓\ \text{（用更少的约束已足够）}$$
$$\textbf{(iii)}\ \text{定理对}\ \textbf{任意四点} \text{成立}✓\ \text{（不假设互异、不假设非退化）}✓✓$$
$$\textbf{(iv)}\ \text{碰撞层}（x_i = x_j）\ \text{状态不变}✓（`C-369` 已封）✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **H1 刚性引理** ✓ | **CLOSED（证明级：Fejér 核）** ✓✓ |
| **`E_0 \cap E_{\mathrm{even}}`** ✓ | **CLOSED：空（证明级）** ✓✓ |
| 资产 `x_j > 0`／`\inf_j x_j > 0` ✓ | **获得** ✓✓ |
| 极值集分类 ✓ | **`2^4 = 16`（共轭对各取一）** ✓✓ |
| H1-α α1／α2 ✓ | **被取代（无需执行）** ✓✓ |
| `E_0^{(12)} = \varnothing` ✓ | **CLOSED（证明级，由推论一）** ✓✓ |
| `C-380-13`／M2 适用范围 ✓ | **待审计（登记）** ⚠️✓ |
| Bridge A／奇频 discrepancy ✓ | **仍 OPEN** ✓ |
| Level 3 ✓ | **FROZEN** ✓✓ |
| `\Psi(\Delta_4)` ✓ | **DEAD** ✓✓ |

## §3 数字核验记录（数字驱动 ✓✓）

```
A 段（Fejér 恒等式，20000 随机四点）：max 残差 = 1.4e-14  ✓
A 段（加权恒等式，系数 9/2）：       max 残差 = 7.1e-14  ✓（修正前脚本误用 1.5 ⟹ 残差 81.75，已修）
B 段（精确组合分类，50 位）：70 个 4-子集中恰 16 个满足八条；全部精确取等；F_9 = 4.0 ✓
B 段（"共轭对各取一"）：16 个 ⟹ 与枚举结果完全一致 ✓
C 段（16 点上夹逼）：Σ(9-r)(F_r+1/2) ≈ ±5e-15，Σ_j K_9 ≈ 1e-30，F_9 = +4.000000000000 ✓
```
- 脚本 ✓：`scripts/c380_49_fejer_rigidity.py`✓；输出 ✓：`scripts/out_c380_49_fejer.txt`✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}做 70 组 active set 枚举✗（已被取代）✓；\ \textbf{不}碰 Bridge A／奇频✗；\ \textbf{不}裁决 C-380-13✗（只登记冲突）✓；\ \textbf{不}重开 Level 3✗✓$$

## §5 下一步（须唐先生发令 ✓）

$$\textbf{建议①}✓：\text{审计}\ C\text{-}380\text{-}13／C\text{-}3814\ \text{正文}✓,\ \text{判定 M2 过滤器适用范围}✓✓\ \text{（本档 §0⑥）}$$
$$\textbf{建议②}✓：\text{把资产}\ \inf_j x_j > 0✓\ \text{并入主线}✓\ \text{（`C-380-12` §2 的下游步骤）}✓✓$$
$$\textbf{建议③}✓：\text{Bridge A／奇频 discrepancy}\ \text{为下一承重墙}✓\ \text{（须唐先生令）}✓$$

## §6 【技术词回查】输出（**先跑后写** ✓）

```
技术词 Fejér        命中文件数=0    ::
技术词 Fejer        命中文件数=0    ::
技术词 共轭对       命中文件数=0    ::
技术词 等号分析     命中文件数=0    ::
技术词 双层夹逼     命中文件数=0    ::
```
