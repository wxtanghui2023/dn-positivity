已查地图 + **DEC-1 第一刀**（所查档：`C-79`（`DEC-1` 形式与 `K1--K4` 预注册判据）、`C-81`（`Q★` 闭合：短距离 PP-对质量；核 `\min(T,2/|h|)`）、`W6-MAJORANT-1`（`Prop 5.4` 逐字、`a_n=\Lambda(n)/\sqrt n`）、`V254`／`V255`（parity barrier）、`振荡消解普查` §1(ii)（结构化分解＝唯一无条件超 `\sqrt\cdot` 机制）、`V310`（`值不变性`））。**结论**：`DEC-1` **DEAD** —— 一击两点：**(i)** `\Lambda=\mu*\log` 作用于短距离双线性和后产生**四重和＋配对计数核**（约束 `|dm-d'm'|\le h` **耦合** `d,d'`）⟹ **不分解** ⟹ `K1` 命中；**(ii)** 即便退一步只求"带号相消"，可用**无条件** `\mu`-相消只有 `x^{-o(1)}` 型（`\exp(-c(\log x)^{3/5})`，Korobov--Vinogradov）⟹ **远弱于所需的固定幂级 `T^{\eta}`** ⟹ `K3` 等价位命中 ✓✓

# C-82 · **`DEC-1` 第一刀：DEAD**（不分解 ＋ 可用相消只有 `x^{-o(1)}`）

> **时间**：2026-09-18 12:56 唐先生「继续」（承接 `C-81` §4 的 `DEC-1` 激活与 `K1--K4`）
> **本档**：第一刀执行；**结构性论证**，非定理 ⚠️

---

## §0 结论（先行）

$$\textbf{(i)}\ \textbf{不分解}：\Lambda=\mu*\log\ \text{代入短距离双线性和} \Longrightarrow \text{四重和}\ \sum_{d,d'}\mu(d)\mu(d')\sum_{\substack{m,m'\\|dm-d'm'|\le h}}\!\!\!\frac{\log m\log m'}{\sqrt{dd'mm'}}$$
$$\qquad \text{约束}\ |dm-d'm'|\le h\ \textbf{把}\ d\ \text{与}\ d'\ \textbf{耦合} \Longrightarrow \text{内层}\ \textbf{不可分离} \Longrightarrow \text{层和＝}\textbf{双变量}\ \mu\text{-相关}\ \sum_{d,d'}\mu(d)\mu(d')K(d,d')⟹ \textbf{命中 `K1`}✓✓$$
$$\textbf{(ii)}\ \textbf{相消强度不够}：\text{即便退一步，可用}\ \textbf{无条件}\ \mu\text{-相消}＝x^{-o(1)}\ \text{型}\ \bigl(\exp(-c(\log x)^{3/5}(\log\log x)^{1/5})\bigr)$$
$$\qquad ⚠️\ \text{而所需}＝\text{固定幂级}\ T^{\eta}\（\eta\ge0.04）\ \text{（`C-29`：缺口因子}\asymp X/(TL^3)）⟹\ \boxed{\exp(-c(\log T)^{3/5})\ \gg\ T^{-\eta}} \Longrightarrow \textbf{不够}✓✓$$
$$\Longrightarrow\ \boxed{\text{DEC-1}\ \textbf{DEAD}};\ \text{且与}\ \text{parity barrier（`V254`／`V255`）}\ \textbf{一致}✓✓$$

---

## §1 第一刀逐步（`[本档]`）

$$\textbf{Step 1（形式）}：\Lambda(n)=\sum_{d\mid n}\mu(d)\log\frac nd \Longrightarrow a_n=\frac1{\sqrt n}\sum_{d\mid n}\mu(d)\log\frac nd✓$$
$$\textbf{Step 2（短距离和的替换）}：\text{由 `C-81`，短距离核}\approx T\ \text{（常数化）},\ \text{故关键量为}$$
$$\qquad S_h:=\sum_{\substack{n\ne m\\|n-m|\le h}}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}},\qquad h\asymp\frac XT✓$$
$$\textbf{Step 3（代入）}：\ S_h=\sum_{d,d'}\mu(d)\mu(d')\!\!\sum_{\substack{m,m'\\|dm-d'm'|\le h}}\!\!\frac{\log m\log m'}{\sqrt{dd'\cdot mm'}}✓$$
$$\textbf{Step 4（分解测试＝`K1`）}：\text{Harper 型机制的前提＝}\textbf{分层后内层可分离（一变量、可分解）};\ \text{此处内层约束}\ |dm-d'm'|\le h\ \textbf{含}\ d,d'\ \text{的乘积耦合}⟹ \textbf{不可分离}✗$$
$$\qquad ⚠️\ \text{唯一的"分离"可能性}：\text{若}\ d=d'\ \text{（对角层）则约束退化为}\ |m-m'|\le h/d;\ \text{但对角层的}\ \mu(d)^2\ \text{与"层"的数目都不改变总量}（\text{见 §2}）✓$$
$$\textbf{Step 5（强度测试＝`K3` 等价位）}：\text{所需＝固定幂级}\ T^{\eta};\ \text{可用无条件}\ \mu\text{-相消}＝x^{-o(1)}⟹ \text{不够}✓✓$$

## §2 一个更基本的理由（`[本档]`，比 Step 4/5 更强）

$$\Lambda=\mu*\log\ \text{是}\ \textbf{恒等式} \Longrightarrow \text{任何重排必须给出}\ \textbf{同一个总和};\ \text{层和}\ L_D\ \text{满足}\ \sum_DL_D=S_h✓$$
$$\qquad \text{故重排}\ \textbf{只能改"界"，不能改"值"};\ \text{而 `C-81` 已指出障碍在}\ \textbf{量／值} \text{一侧（短距离质量）}✓✓$$
$$\Longrightarrow\ \boxed{\text{凡以}\ \textbf{重排／分层／majorant} \text{为手段的攻击，在}\ \textbf{原理上}\ \text{不能修复一个"值"的问题}}✓✓$$
$$\qquad ⭐\ \text{这条}\ \textbf{不只是关掉 `DEC-1`}：\text{它同时}\ \textbf{回溯解释}\ \text{`C-30`（W6-majorant FAIL）／`SQ1` 第一层（常数无能为力）／`C-78`／"7 次同址"}\ \text{的模式}✓✓$$
$$\qquad\qquad \Longrightarrow\ \text{统一理由}：\textbf{障碍是"值的性质"，不是"界的性质"}✓✓✓$$

## §3 `K1--K4` 判定表

| 判据 | 判定 | 依据 |
|:--|:--:|:--|
| **K1**（退化／不分解）| ✗ **命中（杀）** | Step 4：四重和＋耦合约束 ⟹ 不可分离 |
| **K2**（分层与对角重合）| ⚠️ 部分 | 仅 `d=d'` 层可分离，但其不改变总量（§2）|
| **K3**（需 RH 条件输入）| ✗ **等价位命中** | Step 5：需幂级相消，而可用仅 `x^{-o(1)}` |
| **K4**（`F1` 两问）| ✗ | 重排不携带显式公式之外的新信息 ⟹ `F1a` 不成立 |

## §4 残余（唯一可能的方向，`[本档]`）

$$\text{既然"重排不能改值"，唯一出路是}\ \textbf{换量} \text{（不是换算法）}：$$
$$\qquad \text{即放弃}\ S_h\ \text{本身，改问}\ \textbf{另一个}\ \text{携带带号信息的算术量}\ \text{（＝`SQ3` 的"带号权"版本，}\textbf{但那是另一个对象}）✓$$
$$\qquad ⚠️\ \text{且}\ \text{`C-81` 的教训提示}：\text{新量仍须过}\ \textbf{幂级强度} \text{测试} ⟹ \text{回到}\ \text{`V215` §5 残余（非 canonical 双向识别接口）／第四类不变量}✓✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 13:0x）`[纪律]`（先跑后写）

```
技术词 值不变性     命中文件数=1    :: ./V310-section4-admissible-class-restored-and-quantifier-gap.md
技术词 重排不变     命中文件数=0
技术词 值的性质     命中文件数=0
技术词 家族 closure  命中文件数=0
```
**读数**：`重排不变`／`值的性质`／`家族 closure`＝**0 档 ⟹ 本档新增** ✓；⚠️ `值不变性`＝**1 档 ⟹ 档案已有**（`V310`）⟹ 引用 ✓

## §6 边界（⚠️ 必读）

$$\text{(i)}\ §1--§2\ \text{为}\ \textbf{结构性论证}：\text{Step 4 的"不可分离"为}\ \textbf{未见分离方式} \text{（非不存在性定理）}⚠️;\ \text{Step 5 的强度比较为}\ \textbf{量级比较}✓$$
$$\text{(ii)}\ \text{不得写"已证重排不可能"}\ ✗;\ \text{须写"}\textbf{本刀未见可行的分离／强度不足}\text{"}✓$$
$$\text{(iii)}\ \textbf{未用 RH}\ \text{作推导}✓;\ \textbf{零数值}✓;\ \text{不修改原档}✓$$

```
⚠️ 任务：唐先生 12:56「继续」= 开 DEC-1 第一刀（检验 Λ=μ∗log 分层重排能否在短距离区产生真实相消；按 K1–K4）
✅ 结论：DEC-1 **DEAD**，两点一击：
   (i) **不分解**：代入后为四重和 Σ_{d,d'} μ(d)μ(d') Σ_{|dm−d'm'|≤h} log m log m'/√(dd'mm')；约束耦合 d,d' ⟹ 内层不可分离
       ⟹ 层和＝双变量 μ-相关 ⟹ K1 命中；仅 d=d' 层可分离，但不改变总量
   (ii) **相消强度不够**：所需＝固定幂级 T^η（η≥0.04；C-29 缺口因子 ≍ X/(TL³)）；可用无条件 μ-相消＝x^{−o(1)}
       （exp(−c(log x)^{3/5}(loglog x)^{1/5})，Korobov–Vinogradov）⟹ exp(−c(log T)^{3/5}) ≫ T^{−η} ⟹ 不够 ⟹ K3 等价位命中
⭐ 更强的理由（§2）：Λ = μ∗log 是**恒等式** ⟹ 任何重排必须给出**同一个总和**；层和 Σ_D L_D = S_h ⟹ 重排**只能改界、不能改值**；
   而 C-81 已指出障碍在**量/值**一侧 ⟹ **凡以重排/分层/majorant 为手段的攻击，在原理上不能修复"值"的问题**
   ⟹ 这条**不只是关掉 DEC-1**：它同时回溯解释 C-30（W6-majorant FAIL）、SQ1 第一层（常数无能为力）、C-78、"7 次同址"模式
   ⟹ 统一理由：**障碍是"值的性质"，不是"界的性质"**
⚠️ 残余（唯一方向）：既然重排不能改值，唯一出路是**换量**（不是换算法）——放弃 S_h 本身，改问另一个携带带号信息的算术量
   （＝SQ3 的"带号权"版本，但是另一个对象）；且新量仍须过**幂级强度**测试 ⟹ 回到 V215 §5 残余 / 第四类不变量
⚠️ 边界：Step 4 的"不可分离"是"未见分离方式"（非不存在性定理）；Step 5 是量级比较；不得写"已证重排不可能"
✅ 净产出：①DEC-1 判死（两点理由）✓；②K1–K4 判定表 ✓；③"重排不能改值"的一般性理由（关掉整家族）✓；④残余方向 ✓
```
