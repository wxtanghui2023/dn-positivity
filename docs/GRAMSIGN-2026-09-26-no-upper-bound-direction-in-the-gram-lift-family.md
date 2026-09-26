已查地图：已跑 scripts/prework_map_check.sh K(10,1) Gram-LIFT 上界方向 PSD 系数符号 ⟹ 执行自 `docs/GRAM-LIFT-2026-09-25-...md`（G_ij 族与系数表 ✓）＋ `docs/SUM-P1P4-2026-09-26-...md`（`LOCAL-AVG-GATE` ✓）；本档为**纯推导**（唐先生 2026-09-26 19:49 指令「检查 Gram-LIFT 二次恒等式中是否存在上界方向」✓）；**未跑程序** ✓。
D0: 本档对象 = `Gram-LIFT` 族的**系数符号结构**与上界可达性（既有对象；非新对象）
D1: 0（产出为一条符号定理、上界方向的不可能性结论与新的问题定型）

# GRAMSIGN-2026-09-26 · Gram-LIFT 族的上界方向检查

## §0 结论（先给）

```
$$\boxed{\textbf{定理（符号）}:\ Gram\text{-LIFT}\ \text{族每一成员皆形如}\ \sum_{r\ge1}w_rD_r\ \ge\ \text{const},\ w_r\ \ge\ 0\ \Longrightarrow\ \textbf{只给下界}\ ✗}$$
$$\boxed{\Longrightarrow\ \text{该族\textbf{不可能}产出}\ D_1+D_2\le143\ \text{（即}\ Q\le1\text{）所需的上界}\ ✗✓}$$
$$\boxed{\text{crux 的真类型}:\ \textbf{支撑刚性}（\text{至多一点}\ \delta=2\text{）}\ \text{而非矩不等式}\ ✓\ \Longrightarrow\ \text{工具箱不匹配}\ ✓}$$
$$
$$
```

---

## §1 族的一般成员与其系数结构（严格推导 ✓）

```
$$A_j(z):=\#\{c: d(z,c)=j\};\quad F_i:=A_i+(11-i)A_{i-1}+(i+1)A_{i+1}\ (\text{系数全非负}\ ✓);\quad \delta_i=F_i-\binom{10}{i}\ ✓$$
$$G_{ij}:=\sum_x\delta_i(x)\delta_j(x)=\underbrace{\sum_xF_iF_j}_{\text{(a)}}- \binom{10}{i}\sum_xF_j-\binom{10}{j}\sum_xF_i+2^{10}\binom{10}{i}\binom{10}{j}\ ✓$$
$$\textbf{(a) 的展开}:\ \sum_xF_iF_j=\sum_{a,b}\kappa_a^{(i)}\kappa_b^{(j)}\sum_xA_aA_b,\qquad \kappa^{(i)}\ge0\ \text{（因}\ F_i\ \text{系数非负}\ ✓）$$
$$\textbf{基础恒等式}:\ \sum_xA_aA_b=M\binom{10}{a}[\![a=b]\!]+2\sum_{r\ge1}D_rN_{ab}(r),\qquad N_{ab}(r)=\binom{r}{u}\binom{10-r}{a-u}\ \ge\ 0\ ✓$$
$$\Longrightarrow\ \boxed{G_{ij}=\underbrace{\Big[2\sum_{a,b}\kappa_a^{(i)}\kappa_b^{(j)}\sum_rN_{ab}(r)D_r\Big]}_{\text{D 系数}\ \ge0\ ✓}+\underbrace{\text{const}}_{\text{仅常数项}}\ }\ ✓✓$$
$$
$$
```

**⟹ 符号定理**：$G_{ij}\ge0$ 即 $\sum_r w_rD_r\ge\text{const}$，其中 $w_r=2\sum_{a,b}\kappa_a^{(i)}\kappa_b^{(j)}N_{ab}(r)\ \ge\ 0$ ✓✓
（负号只可能落在**常数项**上，绝不落在 $D_r$ 上 ✓）

---

## §2 逐条核验（与档案系数表逐字比对 ✓）

```
$$\begin{array}{c|c|c}
\text{不等式} & \text{D 系数} & \text{符号}\\ \hline
G_{00}\ (\Sigma\delta_0^2)\ \ge\ 0 & +4D_1+4D_2\ \text{（常数}\ -285\text{）} & \text{全正}\ ✓\\
L01:\ \Sigma\delta_0\delta_1\ge0 & +58D_1+8D_2+12D_3-13560 & \text{全正}\ ✓\\
L02:\ \Sigma\delta_0\delta_2\ge0 & +36D_1+86D_2+12D_3+24D_4-61020 & \text{全正}\ ✓\\
L03:\ \Sigma\delta_0\delta_3\ge0 & +144D_1+32D_2+106D_3+16D_4+40D_5-191280 & \text{全正}\ ✓\\
L11:\ G_{11}\ge0 & +112D_1+212D_2+24D_3+48D_4-124890 & \text{全正}\ ✓\\
\end{array}$$
（与档案 §2/§5 系数表**逐字一致** ✓ ⟹ 符号定理与实测吻合 ✓）
$$
$$
```

---

## §3 上界方向的**不可能性**（三种可用工具全查 ✓）

```
$$\textbf{工具 1（族内不等式的线性组合）}:\ \text{全为}\ \sum_r w_rD_r\ge c\ (w_r\ge0)\ ✓\ \Longrightarrow\ \text{任意非负组合仍是"正系数下界"}\ ✗$$
$$\qquad\text{唯一能"翻向"的方式}:\ \text{某成员含\emph{负}系数}\ ✓\ ——\ \text{符号定理排除了它}\ ✗✓$$
$$\textbf{工具 2（行和恒等式）}:\ \sum_jG_{0j}=E^2=81225\ \Longrightarrow\ G_{00}=81225-\sum_{j\ge1}G_{0j}$$
$$\qquad\text{而上式右端与}\ G_{00}\ \text{是同义反复}（\sum_{j\ge1}G_{0j}=E^2-G_{00}\ ✓）\ \Longrightarrow\ \textbf{零信息}\ ✗$$
$$\textbf{工具 3（Cauchy–Schwarz / PSD 子式）}:\ G_{0j}^2\le G_{00}G_{jj}\ \Longrightarrow\ G_{00}\ \ge\ G_{0j}^2/G_{jj}\ \Longrightarrow\ \textbf{仍为下界}\ ✗✓$$
$$
$$
```

**⟹ 结论**：族内**不存在**上界方向 ✓✓ —— $D_1+D_2\le143$ 不能由 $\{G_{ij}\ge0\}$ 及其线性/CS 组合产出 ✗。

---

## §4 ⭐ 当前区间的精确表述（本档给出最紧框架 ✓）

```
$$\textbf{下界（已有，最强）}:\ \text{整数凸性}\ \delta_0^2\ge\delta_0\ \text{于}\ G_{00}\ \text{上}\ \Longrightarrow\ G_{00}\ge\sum\delta_0=E\ \Longrightarrow\ \boxed{D_1+D_2\ \ge\ \mathbf{143}}\ ✓$$
$$\qquad\text{更强写法}:\ \delta\in\{0,1,2\}\ \text{整值}\ \Longrightarrow\ \sum\delta^2\equiv-E\equiv3\ (\!\!\bmod 4)\ \Longrightarrow\ \sum\delta^2\ge287\ \Longrightarrow\ \text{同值}\ ✓\ (\text{见 TRACE-287}\ ✓)$$
$$\textbf{上界（本档给出）}:\ \text{由}\ \delta\le2\ (\text{非}\ z\ \text{点})\ \Longrightarrow\ \delta^2\le2\delta\ \Longrightarrow\ \sum\delta^2\le2\sum\delta=570\ \Longrightarrow\ G_{00}\le570$$
$$\qquad\Longrightarrow\ 4(D_1+D_2)-285\le570\ \Longrightarrow\ \boxed{D_1+D_2\ \le\ \mathbf{213}}\ \text{（}\le213.75\ ⟹\ \text{整值}\ 213\ ✓）$$
$$\Longrightarrow\ \boxed{\mathbf{143}\ \le\ D_1+D_2\ \le\ \mathbf{213}}\qquad\textbf{缺口}:\ \text{需把上界从 213 压到 143}\ ✓✓$$
$$
$$
```

**⟹ 问题定型（本档最重要的产出 ✓）**：

```
$$\boxed{\text{crux}\ \Longleftrightarrow\ \text{"上界 213}\to143"\ \Longleftrightarrow\ \text{"}\delta\ \text{的支撑至多一点为}\ 2"\ \Longleftrightarrow\ Q\le1}$$
$$\qquad\Longrightarrow\ \text{这是\textbf{支撑（support）刚性}问题，\emph{不是}矩/二次型问题}\ ✗✓$$
$$\qquad\Longrightarrow\ \text{二次矩工具箱在\textbf{类型上}不匹配；继续在 Gram-LIFT 内找上界 = }\textbf{结构性徒劳}\ ✗$$
$$
$$
```

---

## §5 与 `LOCAL-AVG-GATE`（AMEND-30）的关系与今日两条剪枝的汇合

```
$$\textbf{今日两条剪枝（互补）}:\ \text{①}\ \text{线性局部界求和}\ \Longrightarrow\ \textbf{无码相关信息}（AMEND-30\ ✓）$$
$$\qquad\qquad\qquad\qquad \text{②}\ \text{二次 Gram 族}\ \Longrightarrow\ \textbf{只有下界方向}（本档\ \S 1\text{--}\S 3\ ✓）$$
$$\Longrightarrow\ \text{两条合起来排除}:\ \text{"在现有线性/二次族内找}\ D_1+D_2\le143"\ ✓✓\ ——\ \text{这是今天最有价值的负结果}\ ✓$$
$$
$$
```

---

## §6 下一步的真正候选口（本档列出，均未执行 ✓）

```
$$\textbf{口 A（支撑刚性）}:\ \text{直接攻}\ Q\le1\ \text{（至多一点}\ \delta=2\text{）}\ ——\ \text{需组合/forcing 手段，非矩手段}\ ✓$$
$$\qquad\text{已知}:\ \text{① 的 forced 只给 3 个 }b{=}2\ \text{点}\ ✗;\ \text{量级差 4 倍（见 AMEND-30 门槛）}\ ⚠️$$
$$\textbf{口 B（负系数不等式）}:\ \text{寻找含\emph{负}\ }D_r\ \text{系数的合法不等式}\ ——\ \text{可能来源}:\ \text{独立集/装填（packing）型界}\ ✓$$
$$\qquad\text{注意}:\ \text{装填型界通常给}\ M\ \text{的上界}\ ✗,\ \text{而我们需要}\ D_1+D_2\ \text{的上界}\ ——\ \text{接口未成}\ ⚠️$$
$$\textbf{口 C（混合符号高阶矩）}:\ \text{三阶/四阶矩中可能出现混合符号}\ ——\ \text{档案已记 "higher-order moment 反重复墙"（C3793）}\ ⚠️$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 的符号定理为**严格推导**（$G_{ij}$ 展开 ⟹ $D_r$ 系数 $=2\sum_{a,b}\kappa\kappa N_{ab}(r)\ge0$ ✓）；负号只能在常数项 ✓
- §2 与档案系数表**逐字核对一致** ✓（4 条全部通过 ✓）
- §3 三工具全部排查 ✓；结论"无上界方向"限于**族内及其线性/CS 组合** ✓；**未主张**更广族无上界 ✗
- §4 的 $D_1+D_2\le213$ 为本档新给（由 $\delta\le2$ ✓）；区间 $[143,213]$ 为**当前最紧框架** ✓
- §4/§5 的"问题定型为支撑刚性"为**本档判断** ✓（非定理）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 符号定理     命中文件数=2    :: ./GRAMSIGN-2026-09-26-no-upper-bound-direction-in-the-gram-lift-family.md ./EG-archive.md 
技术词 上界方向不可能性 命中文件数=1    :: ./GRAMSIGN-2026-09-26-no-upper-bound-direction-in-the-gram-lift-family.md 
技术词 支撑刚性定型 命中文件数=1    :: ./GRAMSIGN-2026-09-26-no-upper-bound-direction-in-the-gram-lift-family.md
```
- **本档新增**：符号定理、上界方向不可能性、支撑刚性定型（见上方命中数；「符号定理」若已存在则按档案已有处理）
- **档案已有（引用，不列为提出）**：$G_{ij}$ 族、$N_{ab}(r)$、$\delta_i=F_i-\binom{10}{i}$
