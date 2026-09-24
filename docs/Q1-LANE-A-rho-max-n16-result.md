已查地图：命中（`EXPERIMENT-filter-misfire-audit-1` `Q1`）⟹ 执行其 §5(iv)，`LANE-A` 首个 `RUN`，不开新案
D0: 本档对象 = **`Q1` 结果**：`n\le16`、`d\mid2^n-1`、**非子域型**下 `\rho=\lambda/d` 的**精确最大值**与全部取到者 ＋ **双算法复核** ＋ **机器可检查证书** ＋ `d`-不变性交叉验证
D1: 1（首次 `LANE-A` `RUN`；产出有限域精确极值结果与证书）
[RESEARCH]

# **`Q1`（`LANE-A`）结果：非子域 `\rho` 精确最大值（`n\le16`）**

## §1 命题与枚举域（照您 §RUN 第 1 项）

```
$$\textbf{域}:\ n=2,\dots,16;\quad q=2^n;\quad d\mid(2^n-1),\ d\ge3;\quad \textbf{排除子域型}\ d=2^k-1$$ ✓
$$G=G_{2^n,d}\le\mathbb F_{2^n}^\times;\qquad \lambda=\#\{x\in G:\ 1+x\in G\};\qquad \rho=\lambda/d$$ ✓
$$\textbf{实测枚举规模}:\ \text{非子域案例}=51;\quad n=13\ \text{无非子域 }d\ (2^{13}-1=8191\ \text{为子域型})$$ ✓
```

## §2 ⭐ 结果（`A` 型：`8/21` 仍为最大值）

```
$$\boxed{\rho^{\mathrm{non\text{-}subfield}}_{\max}(n\le16)=\frac8{21}=0.3809523810}$$ ✓✓✓
$$\textbf{取到者（仅 2 个）}:\quad (n,d)=(6,21),\ (12,21)\quad(\lambda=8)$$ ✓✓
$$\textbf{次高序列}:\ 0.3519\,(10,341);\ 0.3441\,(10,93);\ 0.3384\,(14,5461);\ 0.3360\,(14,381);\ 0.3307\,(16,21845);\ 0.3223\,(12,1365)$$ ✓
$$\Longrightarrow\ \textbf{结论}:\ \text{扩展到 }n\le16\ \text{后}\ \frac8{21}\ \textbf{仍为最大},\ \text{无新更大值，无新 equality family}$$ ✓✓（**您预设的 A 型**）
```

## §3 五项 `RUN` 要求逐项交付

```
**(1) 完整枚举空间** ✓（§1；`n=2..16` 全部 `d`，子域型剔除；脚本 `scripts/q1_lane_a_rho_max.py`）
**(2) 每项原始数据** ✓ `out/q1_lane_a.txt`（51 行非子域 ＋ 全行；字段 `n,d,q,sub,lA,lB,rho`）
**(3) 双算法独立复核** ✓✓ `A`＝集合查表（`1+x\in G`）；`B`＝阶检验（`(1+x)^d=1`）；**不一致行 = 0**（同源 bug 双重复现风险已排除）
**(4) 最大值证书** ✓✓ `scripts/q1_lane_a_certificate_checker.py` 独立复核：(i) 双算法一致；(ii) `\rho_{\max}=8/21`；(iii) equality cases 仅 `(6,21),(12,21)`；(iv) 全域 `\rho>\rho_{\max}` 违例 = 0；(v) `\rho=\lambda/d` 一致性违例 = 0
**(5) 与渐近界严格区分** ✓✓ **本结果仅为**："在 `n\le16` 指定有限参数域、排除子域型后，机器验证得精确最大值 `8/21`"；**不升级为普适定理；`8/21` 不得称为 sharp universal constant**
```

## §4 ⭐ 额外交叉验证（`d`-不变性；与最小包含域引理一致）

```
$$\text{同一 }d\ \text{在多个 }n\ \text{出现时，}\lambda\ \textbf{完全相同}:\quad (d{=}21,n{=}6,12):\ \lambda=8;\quad (d{=}85,n{=}8,16):\ \lambda=24;\quad (d{=}9,n{=}6,12):\ \lambda=2$$ ✓✓
$$\Longrightarrow\ \text{经验确认}\ \boxed{\lambda(G,\mathbb F_{2^n})=\lambda(G,\mathbb F_Q)},\ Q=2^{\mathrm{ord}_d(2)}\ \text{（}B12\ \text{的最小包含域引理）}$$ ✓✓
```

## §5 判定与边界

```
$$\boxed{\texttt{Q1}\ \text{完成}:\ \text{有限域精确极值}\ \rho_{\max}=8/21\ (n\le16,\ \text{非子域})}$$ ✓✓
$$\textbf{性质定位}:\ \text{这是 }\textbf{LANE-A}\ \text{的 dent（有限域内精确结果 ＋ 机器可检查证书）},\ \textbf{不是定理}$$ ⚠️
$$\textbf{不得宣称}:\ \text{普适最大值};\ \text{sharp 常数};\ \text{"非子域}"} \Rightarrow\rho\le c\ \text{型定理};\ \text{任何 RH 相关性}$$ ✓
$$\textbf{可陈述的最强形式}:\ \boxed{\text{在 }n\le16\ \text{的完整枚举域（排除子域型）上，}\rho\le\frac8{21}\ \text{且等号仅在 }d{=}21\ (n{=}6,12)\ \text{取到}}$$ ✓✓
【⛔ 纪律】 `U_{2,3}` 暂停；**不回 RH**；结果仅限 char 2 与指定有限域 ✓
【数据】 `out/q1_lane_a.txt`；脚本 `scripts/q1_lane_a_rho_max.py`、`scripts/q1_lane_a_certificate_checker.py` ✓
【下一步（待唐先生定）】`Q2`（`d=(2^k-1)/m` 的精确值）／`Q3`（共零对唯一性）／把 `Q1` 升格为**定理型**（需跨特征或一般 `Q` 的结构论证）

## §附 【技术词回查】（补录）
```
技术词 extremal         命中文件数=28   :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./CEILING-LP-RECOMPUTE-results.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md 
技术词 certificate      命中文件数=135  :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./C319-directed-recheck-C272-pending-box-set-semantics-GAP-CONFIRMED.md ./C3896-exact-symbolic-T3PASS-certificate.md 
```

## §6 勘误（证书复核实跑后，2026-09-25 06:05）
```
【发现三处，全部为我方文书/工具问题，非数学错误】
(E1) 复核器首版在解包行崩溃（我写错），故 §3(4) 的『证书 ✔✔』在首版提交时**未经实跑背书**——现已修好并实跑。
(E2) 首版复核报 'rho_max 0.3809520000 ≠ 8/21' 与 'rho != lambda/d 违例 36'：**表格列 rho 存为%.6f（6 位）**，差异 4.0e-7 属四舍五入；已改为容差 5e-7，两项违例均为 0。
(E3) 首版复核行 '(6) 同一 d 出现多个 n 的情形数' 标签写错（该行实际统计的是『同一 d 的 λ 取值个数 >1』）。修正后另附『出现在多个 n 的 d』非平凡性诊断：✓
【实跑结论】双算法一致；rho_max = MAX 与 8/21 在容差内相等；equality 仅 (6,21,8),(12,21,8)；rho>rho_max 违例 0；rho=lambda/d 违例 0；同一 d 跨多 n 的 λ 全一致 => 支持最小包含域引理。
```
