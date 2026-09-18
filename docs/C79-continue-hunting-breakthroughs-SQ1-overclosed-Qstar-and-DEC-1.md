已查地图：**关键词逐一实跑**（`双层分解重排`＝0｜`分解面`＝0｜`DEC-1`＝0｜`μ ∗ log`＝0｜`close pair`＝0｜`bounded gap`＝0｜`卷积分解`＝0｜`分解重排`＝0｜`上界需求`＝0 ；对照：`立足点`＝4（通用词）｜**`N1`＝239（标签已被占用 ⟹ 本档改名 `DEC-1`）**｜`Harper`＝9｜`Dirichlet 卷积`＝19｜`短区间`＝58｜`素数对`＝33｜`Maynard`＝39；并核 `p192-gate0.md` 的唯一 `Λ = μ` 命中＝**记法 `μ_Λ = μ₀`，非该恒等式**）。**结论**：① 发现一处**未登记面 `DEC-1`**（`Λ = μ ∗ log` 双层分解重排）；② ⚠️ **必须自我更正**：`C-78` 把 `SQ1` "关闭"得**过早**——`C-78` 只回答了"**一般 Hilbert 不等式的常数**"，**没有**回答"**实际稀疏算术权的算子范数**"；后者**仍开**，且是**真正的突破口候选** ✓✓

# C-79 · **继续寻找突破口**：`SQ1` 的过度关闭（自我更正）＋ 两个未登记面（`Q★`／`DEC-1`）

> **时间**：2026-09-18 12:47 唐先生「继续寻找突破口」
> **本档**：闸门实跑 ＋ **对 `C-78` 的一处自我更正** ＋ 两个候选面 ＋ 预注册 kill 判据 ✓

---

## §0 结论（先行）

$$\textbf{① ⚠️ 自我更正（对 `C-78` §3）}：\text{`C-78` 把 `SQ1` 判"关闭"}\ \textbf{过早};\ \text{它只回答了两层中的}\ \textbf{第一层}✗$$
$$\qquad \text{第一层（已答）}：\textbf{一般}\ \text{MV／Hilbert 不等式的}\ \textbf{尖锐常数} \Longrightarrow\ \text{余量}\ \lesssim1.5\ \text{倍（常数级）}✓$$
$$\qquad \text{第二层（}\textbf{仍开}）}：\textbf{对实际稀疏算术权} a_n=\Lambda(n)/\sqrt n（\text{支撑在素数幂}）\ \text{的}\ \textbf{算子范数}\ \text{是否}\ \ll L^2X\cdot T^{-c}？\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{若第二层为"是"}\ \Longrightarrow\ \text{对角支配在}\ X=T^{1.04}\ \text{成立} \Longrightarrow\ \textbf{无需 prime-pair 即可破 0.682}}✓✓✓$$
$$\textbf{② 未登记面 `DEC-1`}：\Lambda=\mu*\log\ \text{的}\ \textbf{双层分解重排}（\text{关键词 0 档}）✓$$
$$\textbf{③ 三视图同一簇}：Q★（权稀疏性）\ \big|\ \text{SQ3}（\Lambda\ \text{vs}\ \mu^2）\ \big|\ \text{DEC-1}（\text{分解重排}）\ \Longrightarrow\ \text{三者互为闸门}✓$$

---

## §1 闸门实跑记录（本档）

| 探针 | 关键词命中 | 判定 |
|:--|:--:|:--|
| **close-pair 项**（`\|log(n/m)\| ≲ 1/T` 部分）| `close pair`＝0｜`bounded gap`＝0 ｜（邻域 `短区间`＝58／`素数对`＝33／`Maynard`＝39 已重度工作）| **未登记**，但其**自然实现＝筛法** ⟹ 撞已登记 **parity barrier**（`V254`／`V255`）⟹ **关**；⚠️ **除下述"上界需求"空槽**（见 §2）|
| **`DEC-1`**（`Λ = μ ∗ log` 双层分解重排）| `双层分解重排`＝0｜`分解面`＝0｜`DEC-1`＝0｜`μ ∗ log`＝0｜`卷积分解`＝0｜`分解重排`＝0；唯一 `Λ = μ` 命中＝**记法**（非恒等式）| **未登记** ✓✓ |
| **`Q★`**（稀疏算术权的算子范数）| 属 `SQ1` 的第二层，`C-78` 未答 | **仍开** ✓✓ |
| ⚠️ 标签 | `N1`＝**239 档（已占用）** ⟹ 本档改用 **`DEC-1`** | 命名已规避冲突 ✓ |

## §2 ⭐ `Q★`：为什么"上界需求"可能不撞 parity（`[本档]`；`立足点`为通用词）

$$\text{已登记的 parity 结论（`V254`／`V255`）针对}\ \textbf{检测／渐近}：\text{筛法不能把素数从"几乎素数"中区分出来} \Longrightarrow \text{拿不到}\ \textbf{正确常数的主项}✓$$
$$\text{而我们的需求是}\ \textbf{上界}（\text{对角支配}\ |O_1|\ll D）,\ \text{不是主项渐近} ⟹ \textbf{parity 的登记范围不直接覆盖这一需求}⚠️$$
$$\qquad ⚠️\ \textbf{但立即要加一条限制（诚实）}：\text{若只得到}\ |O_1|\le C\cdot D（C\ \text{为常数}），\ \text{则}\ O_1=o(D)\ \textbf{不成立} \Longrightarrow \text{常数级上界}\ \textbf{不够};\ \text{必须是真的}\ \textbf{幂级节省}✓$$
$$\qquad\Longrightarrow\ \text{故}\ Q★\ \text{的唯一有出路形式是}：\textbf{利用}\ \Lambda\ \text{的}\ \textbf{稀疏支撑}（\text{素数幂，密度}\ \asymp X/\log X）\ \text{本身取得幂级节省——而不是改进 MV}✓✓$$

## §3 `DEC-1` 的精确形式与机制

$$\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d)\quad(\Lambda=\mu*\log)$$
$$\Longrightarrow\ \sum_{n\le X}\Lambda(n)n^{-1/2-it}\omega(n)\ =\ \sum_{\substack{dm\le X}}\mu(d)\log m\,(dm)^{-1/2-it}\omega(dm)$$
$$\qquad \text{二维区域}\ \{(d,m):dm\le X\}\ \text{上的}\ \textbf{分层重排}：\mu\ \text{与}\ \log\ \textbf{分离} \Longrightarrow \text{可按}\ d\ \text{（或}\ m）\ \text{分块，每块＝乘积结构}✓$$
$$\qquad ⭐\ \text{与档案认定的}\ \textbf{唯一无条件超}\sqrt{\cdot}\ \text{机制}\ \textbf{同型}：\text{振荡消解普查 §1(ii)}\ \textbf{结构化分解}\（\text{Harper：}\mu^2(n)=\sum_{d^2\mid n}\mu(d)）✓✓$$
$$\qquad \text{即：}\textbf{把指示／权重写成 Dirichlet 卷积 ⟹ 振荡分层重排 ⟹ 超}\sqrt{\cdot}\ \text{节省}\ \text{（无条件！）}✓$$

## §4 **预注册 kill 判据**（开工前钉死，避免又一轮同址收敛）

$$\textbf{K1}\ \text{若重排后退化回同一 MV／Hilbert 步} \Longrightarrow \text{仅常数级} \Longrightarrow \textbf{DEAD}$$
$$\textbf{K2}\ \text{若二维区域的分层与"对角"重合} \Longrightarrow \textbf{DEAD}$$
$$\textbf{K3}\ \text{若需要 RH 条件下输入} \Longrightarrow \textbf{DEAD}（\text{`R8` 教训：必须}\textbf{先证独立}）$$
$$\textbf{K4}\ \text{过}\ \text{`F1` 两问}：\text{F1a 携带显式公式／Weil 型}\textbf{之外} \text{的新信息？}\ \text{F1b 能以}\textbf{严格弱于 RH} \text{的输入无条件证明？}✓$$
$$\qquad ⚠️\ \text{任一条不过} \Longrightarrow \text{立即停，不进入 HS／数值阶段}✓$$

## §5 三视图的对应（执行序）

| 视图 | 内容 | 若"成功"意味着 | 若"失败"意味着 |
|:--|:--|:--|:--|
| **`Q★`** | 稀疏权 `a_n=Λ(n)/√n` 的算子范数 `≪ L²X·T^{−c}`？ | 无需 prime-pair 即破 `0.682` ✓✓ | 墙对**这个权**也是真的 |
| **SQ3** | `Λ` vs `μ²`（可分解 vs 不可分解）在同尺度下的 `\|O₁\|/D` | 障碍在"**素数抽取**" ⟹ 走 `DEC-1` | 障碍在**双体／close-pair 结构** ⟹ `DEC-1` 无用 |
| **`DEC-1`** | `Λ=μ∗log` 分层重排能否给幂级节省 | 直接攻破 ✓✓ | 回 `SUPPORT-1`（同址） |
$$\Longrightarrow\ \textbf{建议执行序}：\textbf{`Q★` 先}（最直接、不需新文献、判据清晰）\to\ \text{SQ3}（判别）\to\ \text{DEC-1}（若指示走这条）✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:5x）`[纪律]`

```
技术词 双层分解重排 命中文件数=0
技术词 上界需求    命中文件数=0
技术词 立足点     命中文件数=4   :: ./V191-uniform-finite-n-hyperbolicity-NO-theorem-grade-F1-amendment.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md
技术词 N1         命中文件数=239  :: （标签已占用 ⟹ 本档改用 DEC-1）
技术词 DEC-1       命中文件数=0
技术词 分解面      命中文件数=0
技术词 μ ∗ log     命中文件数=0
```
**读数**：`双层分解重排`／`上界需求`／`DEC-1`／`分解面`／`μ ∗ log`＝**0 档 ⟹ 本档新增** ✓；⚠️ `立足点`＝4 档（**通用词，引用**）；⚠️ **`N1`＝239 档 ⟹ 标签已被占用，本档改名 `DEC-1`**（命名冲突已规避）✓

## §7 边界

- `[本档]` §0 的自我更正、§1 闸门表、§2 的 parity 范围之辨、§3 `DEC-1` 形式、§4 kill 判据、§5 执行序 ✓
- `[逐字引用]` 振荡消解普查 §1(ii)（结构化分解＝唯一无条件超 √ 机制）／`V254`／`V255`（parity）／`C-29`（对角支配 `X ≪ TL`；缺改进因子）✓
- **不声称**：`Q★` 成立／不成立 ✗；`DEC-1` 有效 ✗；`SQ3` 结论 ✗；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓，且**先跑后写** ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 任务：唐先生 12:47「继续寻找突破口」
⚠️ ⭐ 自我更正（对 C-78 §3）：把 SQ1 判"关闭"过早 —— C-78 只回答了第一层（一般 Hilbert 不等式的尖锐常数：余量 ≲1.5×，常数级）；
   未回答第二层：**对实际稀疏算术权 a_n = Λ(n)/√n（支撑在素数幂）的算子范数是否 ≪ L²X·T^{−c}** ⟹ **仍开**，且若为"是"
   则对角支配在 X=T^{1.04} 成立 ⟹ 无需 prime-pair 即破 0.682 = 真突破口
⚠️ 两个未登记面：(1) Q★ = 上述第二层；(2) DEC-1 = Λ = μ ∗ log 的双层分解重排（关键词 双层分解重排/分解面/DEC-1/μ∗log 全 0 档；
   唯一 Λ=μ 命中是记法 μ_Λ=μ₀，非该恒等式）
⚠️ parity 适用范围之辨：已登记 parity（V254/V255）针对**检测/渐近**；我们的需求是**上界** ⟹ 不直接覆盖；但**立即加限制**：
   常数级上界不够（O₁ ≤ C·D 不给 o(D)），必须真的幂级节省 ⟹ Q★ 的唯一出路＝利用 Λ 的**稀疏支撑**本身
⚠️ DEC-1 与档案认定的"唯一无条件超 √ 机制＝结构化分解"（振荡消解普查 §1(ii)，Harper 型）同型 ⟹ 有机制先例
⚠️ 预注册 kill 判据 K1–K4（退化回 MV／分层与对角重合／需 RH 条件输入／过不了 F1 两问 ⟹ 立即停）
⚠️ 执行序：Q★ 先（最直接、无需新文献、判据清晰）→ SQ3（判别）→ DEC-1（若指示）
⚠️ 另：close-pair／bounded-gap 探针未登记，但其自然实现（筛法）撞 parity ⟹ 判关
✅ 净产出：①对 C-78 的自我更正（SQ1 分层）✓；②两个未登记面 Q★／DEC-1 ✓；③parity 范围之辨＋必要限制 ✓；④kill 判据 ✓；⑤执行序 ✓
```
