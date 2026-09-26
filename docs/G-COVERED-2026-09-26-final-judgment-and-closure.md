已查地图：已跑 scripts/prework_map_check.sh COVERED AMEND-24 分类完备性 ⟹ 执行自 OBREVERSE-2026-09-26 档；本档为**终局裁定：G 靶心判 COVERED（唐先生 2026-09-26 18:23 裁定 ✓）**；未跑 solver ✓。
D0: 本档对象 = COVERED 判定（条件式）、覆盖链、provenance gate、保留资产 A1–A5、终局状态块、119 与一般 n 的隔离
D1: 1（新增：**终局 COVERED 判定** ✓✓；**provenance gate 单列** ✓✓；**资产 A1–A5 定名** ✓）

# G-COVERED-2026-09-26

## §1 ⚖️ **终局判定（唐先生裁定 ✓）**

```
$$\boxed{G_{\rm target}\ =\ \textbf{COVERED}}\ ✓\ (\text{判决干净，不留灰区}\ ✓)$$
$$\textbf{逻辑写成（严格口径 ✓）}: \textbf{COVERED, conditional on the completeness of the cited }(9,62)\ \textbf{classification and the stated switching invariant.}\ ✓$$
$$\qquad\textbf{不写}:\ \text{"已证明全部最优码 }N_4=10"\ ✗\ (\text{越界}\ ✗)$$
$$
$$

## §2 ✅ **覆盖链（四步 ✓）**

```
$$\text{(9,62) 完备分类}\ \Longrightarrow\ \text{全部最优码同一 switching class}\ \Longrightarrow\ b\text{-profile 不变量保持}\ \Longrightarrow\ N_4=10\ ✓$$
$$\textbf{关键（为何不是"只找到一例"）}: \text{使靶心 COVERED 的是三点合一}:\ \textbf{分类完备性}\ +\ \textbf{switching-class 归属}\ +\ \textbf{profile 不变量}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{满足 AMEND-24}: \text{"目标命题已有 achieved-result coverage"}\ ✓$$
$$
$$

## §3 ⚠️ **provenance gate（单列，待核 ✓）**

```
$$\boxed{\text{Gate-P}: \text{文献/数据库须明确在做 }\textbf{complete classification of optimal }(9,62)\ \text{codes}\ ✓}$$
$$\qquad\text{而\textbf{非}仅 "two representatives / known constructions"}\ ✗$$
$$\textbf{现有证据（强但非终局 ✓）}: \text{① Kéri CD 文件名 }K\_9\_1\_\textbf{classif}.txt\ \text{（125 行、两份 62 码）}\ ✓;\ \text{② ALCOMA10: "the two known codes attaining}$$
$$\qquad K(9,1)=62\ \text{belong to }\textbf{one switching class}\text{"}\ ✓;\ \text{③ 文献口径："the corresponding optimal codes have been classified"（n\le8 明说}\ ✓)$$
$$\textbf{待补}: \text{确认 (9,62) 的完备性表述（需 OB2001 正文或 Kéri 数据库说明}\ ⚠️)$$
$$
$$

## §4 ✅ **保留资产（A1–A5，定名 ✓✓）**

```
$$\textbf{A1. Layer-A/B 分离定理}\ ✓✓: \text{两 }62\ \text{码 }b(C_1)=b(C_2)\ \text{但 }y^{(m)}(C_1)\ne y^{(m)}(C_2)\ (\forall m)\ \Longrightarrow\ \textbf{Layer A 不能编码迫出该 profile 的刚性}\ ✓$$
$$\textbf{A2. fiber 尺寸定量}\ ✓✓: \log_2|\mathcal F(y)|\approx\mathbf{265}\ \text{bit}\ (m{=}1)\ \text{递减至 0}\ (m{=}9)\ ✓$$
$$\textbf{A3. M-covering 重建}\ ✓✓: A_{ii}=10-m,\ A_{ij}=\mathbf 1_{\{d=1\}}\ \text{闭式；两码 }m{=}1..4\ \text{全部验证}\ ✓;\ \text{收紧律 }1.21\to1.06\ ✓$$
$$\textbf{A4. 分类无关的结构诊断}\ ✓: T_3=\#K_3\ \text{普适}\ ✓;\ T_3\ge Q_2\ ✓;\ \sum p_2=\sum\binom b2-2A_1\ ✓;\ p\le9-d_1+[d_1{=}0]\ ✓;\ d(P_{10})\ge3\ ✓$$
$$\qquad\qquad\qquad\qquad\qquad\ \text{跨表示刚性 12 项}\ ✓✓;\ \text{否证 14 条}\ ✓$$
$$\textbf{A5. OB-2001 方法复原}\ ✓: \text{候选 LP 指纹表 ＋ 重建算法（isomorphism pruning / subcode enumeration / LP-based bounding）}\ ✓$$
$$
$$

## §5 📋 **终局状态块（唐先生指定格式 ✓）**

```
G = COVERED
reason = complete classification coverage
target = N4 ≥ 10 for optimal (9,62) binary radius-1 covering codes

Research value retained:
 A1. Layer-A/B separation theorem
 A2. quantitative fiber-size analysis
 A3. M-covering reconstruction
 A4. classification-independent structural diagnostics
 A5. OB-2001 method reconstruction

119 = UNKNOWN
No solver / LP / SAT required.
```

## §6 ⚠️ **两点严格隔离（防止过度声称 ✓）**

```
$$\textbf{① 一般 }n\ \text{的 pinning 问题}\ \textbf{未被覆盖}\ \text{（仅 }n=9\ \text{实例判 COVERED}\ ✓): \text{不得写 "pinning 已被解决"}\ ✗$$
$$\qquad\text{状态}: \text{一般 }n\ \text{仍 \textbf{UNKNOWN}}\ ✓\ \text{—— 但\textbf{不设为活跃靶心}}\ ✓$$
$$\textbf{② "分类无关的人类可读证明"}\ \text{（原乙方案）}: \ \textbf{不升级为新主靶心}\ ✗\ ——\ \text{可作\textbf{后续方法学项目}}\ ⚠️,\ \text{不得伪装成原开放问题}\ ✗$$
$$
$$

## §7 边界（诚实标注）

- §1–§4 为**裁定与资产登记**；§3 明确 **Gate-P 未关闭**（待文献完备性表述 ⚠️）；§6 为**防过度声称**条款 ✓
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 终局 COVERED 判定 命中文件数=1    :: ./G-COVERED-2026-09-26-final-judgment-and-closure.md 
技术词 provenance gate  命中文件数=1    :: ./G-COVERED-2026-09-26-final-judgment-and-closure.md 
技术词 资产定名     命中文件数=1    :: ./G-COVERED-2026-09-26-final-judgment-and-closure.md
```
- **本档新增**（扣自引后 = 0）：终局 COVERED 判定、provenance gate、资产定名 A1–A5
- **档案已有（引用，不列为提出）**：AMEND-24、switching class、Layer A/B
