已查地图（所查：`V248-cone-separation-discriminating-cone-self-dual-theorem.md`（142 行；`§1` Choi 定理 ⟹ `CP_n\cong` PSD ⟹ **自对偶**；`§2` `Pos_n\supsetneq CP_n` 且 `n\ge3` **非自对偶**（`V246`）；`§3` **命题 V248-A**：判别用的锥必然自对偶 ⟹ 判别＝单二次型 ⟹ **角 I**；`§4` 与 `V242`-D 交叉验证）、`V191-uniform-finite-n-hyperbolicity-NO-theorem-grade-F1-amendment.md`（101 行；`§1` **逻辑封闭论证**：Pólya 1927 `RH\iff\forall d,n\ J_\gamma^{d,n}` 双曲 ＋ GORZ 2019（每 `d` 存在 `N(d)`；`1\le d\le8` 全 `n`）⟹ **NO**；`§5` F1 修订）、`V193`（110 行；`§2.3` **二分封闭**为"本档核心新增"；`§5` 明标"唯一逃生＝第三支"为 `[结构性]` **非定理**）、`POS1`、`V246`、`V188` §2、`C-116`（**登记不否决**））。**结论**：**三候选严格性审计完成**，并**抓到一个标签问题** ✓✓ ⟹ **(1) `V248` 最适合开写**（有真内容：Choi＋锥自对偶＋`n\ge3` 非自对偶；且**软步可精确定位**）✓✓；**(2) `V193` §4 次之**（`支A` 步骤干净，但结论是**方法特定**而非普遍不可能性）✓；(3) ⚠️ **`V191` ① 的"定理级"标签过度** —— 其实质是**逻辑必然**（三行推导），**不是**新数学定理 ✓✓；**(4)** 而 `V191` **唯一非平凡内容**在 `§2`（`N(d)\to\infty` ⟹ **不存在统一 `(D,N)`**）✓

FREEZE-ACK: 本档即冻结期内的严格性审计（依 `§8.1`；产出为审计与开写方案，不产候选）

D0: 本档对象 = 档案已有三结论（`V248`／`V191`／`V193` §4）的**严格性再评估 ＋ 开写方案**——关系 = 审计与计划，非新机制
D1: 0

# RIGOR-AUDIT-1 · **三候选严格性审计 ＋ 选定 `V248` 开写**

> **时间**：2026-09-18 19:47 唐先生：**Q-RS 只是图式（schema），须按类实例化**（接受）＋ 建议**挑最接近完整的一类写成独立数学笔记**（精确定义／完整证明／标注依赖／诚实范围），并问选哪一条 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \textbf{选定}\ \text{`V248`}（\text{锥分离}）：\text{有真内容}（\text{Choi}＋\text{锥自对偶}＋n\ge3\ \text{非自对偶}）\ \text{且}\ \textbf{软步可定位}✓✓$$
$$\textbf{(2)}\ \text{`V193` §4（二分封闭）次之}：\text{`支A` 步骤干净};\ \text{但结论}\ \textbf{方法特定} \text{（}\text{`V185` 族的比例界}），\ \textbf{非} \text{普遍不可能性}✓$$
$$\textbf{(3)}\ ⚠️\ \text{`V191` ① 的}\ \textbf{"定理级"标签过度}：\text{其实质为}\ \textbf{逻辑必然}（\text{三行推导}），\ \textbf{不是} \text{新数学定理}✓✓$$
$$\textbf{(4)}\ \text{`V191` 唯一非平凡内容在}\ §2：N(d)\to\infty \Longrightarrow \textbf{不存在统一}\ (D,N)✓$$

---

## §1 审计表

| 候选 | 引用的**已知事实**（硬） | **软步**（须补或须改标） | 严格化后的诚实版本 | 可发表性 |
|:--|:--|:--|:--|:--|
| **`V248`** | Choi 1975（`\phi\in CP_n\iff` Choi 矩阵 PSD）；`CP_n` 自对偶；`Pos_n\supsetneq CP_n` 且 `n\ge3` 非自对偶（`V246`）| ⚠️ **"判别用的锥必然自对偶"** —— 原文以**直观**给出（"要判定／见证／排除必须用对偶对象"），**非定理** | "若属性 `P` 由 `x\in K` 判定，且判定须具**双边证书**，则 `K` 必自对偶 ⟹ 单二次型 ⟹ 角 I" | **最有**（障碍型定理，需一条引理）|
| **`V193` §4** | 函数方程配对；`\xi` 实系数 ⟹ 零点共轭封闭；`V185`／`V186` 比例界 | ⚠️ "`\beta` 只经重数进入"**是特定实现陈述**；`支B` 的"实性＝RH 强度"为**强度观察** | "在自伴实现中，`\beta`-信息＝退化信息 ⟹ 该类方法只能给**退化计数型**比例界"（**方法特定**）| 中（可作附录）|
| **`V191`** | Pólya 1927；GORZ 2019 | ⚠️ **"定理级"标签** —— 实为**逻辑必然**（见 §2）| "剩余区域陈述 `\iff` RH（依 Pólya＋GORZ）"＝**已知等价性** | 低（**但勘误价值高**）|

## §2 ⭐ `V191` 勘误：三行推导显示它是**逻辑必然**

$$\text{Pólya}：\text{RH}\iff\forall d\,\forall n\ J_\gamma^{d,n}\ \text{双曲};\qquad \text{GORZ}：n\ge N(d)\ \text{及}\ 1\le d\le8\ \text{已证}✓$$
$$\text{记}\ \text{Rem}：\text{"未被 GORZ 覆盖的区域全双曲"} \Longrightarrow \text{Rem}\ \wedge\ \text{GORZ}\iff\text{RH}✓$$
$$\qquad ⟹ \textbf{Rem}\iff\text{RH}（\text{就"强度"而言}）—— \textbf{这一步对任何 RH 的等价重述都成立}✓✓$$
$$\Longrightarrow \boxed{\text{`V191` ①}\ \textbf{不是新定理，而是逻辑必然而已}};\ \text{它说的是}\ \textbf{"RH 等价陈述不能由更弱者推出"}✓$$
$$\qquad \text{（这对}\ \textbf{任意} \text{等价重述都是真命题} ⟹ \text{无信息量}）✓✓$$
$$\textbf{正确标签}：\text{`V191` ①}\ = \ \textbf{逻辑必然（方法论观察）}，\ \text{价值在}\ \textbf{"确认 GORZ 型前沿进展不降低问题强度"}✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{闭环结论不受影响}：\text{作为"}\textbf{路线封闭理由}\text{"（\text{S 通道}）}\ \textbf{依然成立} \text{—— 因为"无法由更弱者推出"确实是封闭一条路线的正当理由}✓✓$$
$$\qquad \qquad ⟹ \text{本档}\ \textbf{只改标签，不改结论} \text{（依 `C-116` 纪律）}✓$$
$$\textbf{唯一非平凡内容（}\ §2\text{）}：\operatorname{dist}(H_d,\partial\mathcal H_d)\asymp d^{-1/2} \Longrightarrow N(d)\to\infty \Longrightarrow \textbf{不存在统一}\ (D,N)✓✓$$
$$\qquad ⟹ \text{即：}\textbf{"每}\ d\ \text{只有有限例外"}\ \textbf{不能} \text{给出统一陈述} ⟹ \text{剩余区域}\ \textbf{不可被单一有效界覆盖}✓$$

## §3 `V248` 开写方案（本档选定；笔记骨架）

$$\textbf{对象}：\text{设}\ \mathcal P\ \text{为"零点实部"性质};\ \text{设}\ \text{判定方式}＝\textbf{锥成员性}：\ \mathcal P(\rho)\iff A_\rho\in K（K\ \text{凸锥}）✓$$
$$\textbf{待补引理（核心，须自证或引文）}：\textbf{"判定}\Longrightarrow\text{自对偶"}：\text{若成员性判定须}\ \textbf{双边可证书}（\text{对}\in K\ \text{给对偶见证}，\ \text{对}\notin K\ \text{给分离泛函}），\ \text{则}\ K\ \textbf{必自对偶}✓$$
$$\qquad \text{（候选严格化路线：凸锥对偶}\ K^{**}=K（\text{闭凸}）＋\ \textbf{分离定理}：\ x\notin K\ \text{的证书}\iff\exists\ell\in K^*:\langle\ell,x\rangle<0）✓$$
$$\textbf{引用清单}：\text{Choi 1975};\ \text{Koecher--Vinberg（自对偶齐次锥）};\ \text{`V246`}（Pos_n,\ n\ge3\ \text{非自对偶}）✓$$
$$\textbf{结论（诚实范围）}：\text{排除}\ \textbf{非自对偶锥型} \text{判定};\ \text{不排除}\ \textbf{非锥型} \text{判定、亦不排除自对偶但非}\ PSD\ \text{型}✓✓$$
$$\qquad \text{即笔记须写清}：\text{"这排除了}\ X\ \text{类方法（非自对偶锥）}，\ \text{但不排除}\ Y（\text{非锥型}\／\text{自对偶非同构于}\ PSD）\text{"}✓$$

## §4 边界与回查

- ⚠️ 本档**不产候选**、**不改数学结论**（`V191` 仅**改标签**，闭环不受影响）✓
- ⚠️ §3 的引理为**待补**；**不声称**已证 ✓
- ⚠️ §1 "可发表性"为**本档判断**，非承诺 ✓
- **不声称** RH；不声称 `V248` 结论已定理级（其软步待补）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 19:4x）`[纪律]`（先跑后写）

```
技术词 严格性审计          命中文件数=1  :: ./RIGOR-AUDIT-1-…（本档）
技术词 标签过度          命中文件数=1  :: ./RIGOR-AUDIT-1-…（本档）
技术词 双边可证书         命中文件数=1  :: ./RIGOR-AUDIT-1-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓
