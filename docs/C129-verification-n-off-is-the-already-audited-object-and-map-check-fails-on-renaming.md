已查地图（**本次是"事后核对"，本档的第一结论即：我此前四档未先查此图**）：所查 `RIGORIZATION-finitely-many-off-axis-reductio-boundary.md`（**逐字**：原档状态「**无穷多离轴 ⟹ 矛盾（无条件）** ⟹ 排除无穷多 ✓｜**单离轴（有限）**：`\lambda_n` 破坏在 `n\sim1/\varepsilon\sim2\gamma^2/(1-2\beta)` —— **需证明 `\lambda_n\ge0` 到那个 `n`**｜**但 `\lambda_n\ge0` 对所有 `n` ＝ Li 准则 ＝ RH —— 循环**」；**循环点**「要把定理 1 用成"排除单离轴"，需要 `\lambda_n\ge0` 到 `n\sim2\gamma^2\log T/\delta`；对 `\gamma\gtrsim\sqrt{T\delta/\log T}` 的零点，该 `n` **远超**首版论文的范围 `2T` ⟹ 超出部分**正是 Li 判据在长范围的情形 ＝ RH**」；**净结论**「这条反证法的**天花板被精确定位**为「**Li 系数在 `n>2T` 的无条件下界**」；在 `n\le2T` 内**完全等价于**已验证高度（无新信息）；在 `n>2T` 外**等于 RH**」；第 132 行「**本档的净结论恰是：这条反证法现在立不住**（循环点＝ Li 判据在 `n>2T`）—— **不是**"已证明离轴零点只能有限个"」）、`C-59`／`REFRAME`（`ISO` **为待建立目标**）、`C-62`／`C-63`（`ISO` 的两个输入**均判循环**）、`ASSETS-REGISTRY`／`C61`（`有限个离轴` 11 档）、`C-116`、`PRE-WORK MAP CHECK`（`AGENTS.md` 硬规矩）。**结论**：**唐先生 18:43 的核实成立，本档直接认领两处错误** ⟹ **(1)** `\exists C:n_{\rm off}(T)\le C` **与"离轴零点只有有限个"是同一命题**（`n_{\rm off}` 为非降整数值函数 ⟹ **有界 ⟺ 有限**，两种表述等价）✓✓，**而该对象已在** `RIGORIZATION-finitely-many-off-axis-reductio-boundary` **审过**，其**逐字结论**正是"该反证法在 `n>2T` 外＝RH（**天花板**）" ⟹ **`C-128` (2)(3) 是重新发明已审对象** ✓✓；**(2)** ⚠️ `C-128` (3) 的"`\exists C \iff \text{RH}`"**表述有误**——正确为 `\text{RH}\Longrightarrow\exists C`；**反向需 `ISO`**（"一⟹无穷多"），而 `ISO` **在本项目内未证**（`C-62`／`C-63` 已证其两输入循环）⟹ **裸陈述下"离轴零点有限"严格弱于 RH** ✓✓；**(3)** `C-128` (4) 的"**比例 vs 绝对**"**是有效诊断**（`rank`／`trace`／`inertia` 本体只能给占比），**但它不改变该对象的逻辑地位** ⟹ "找非秩型机制" ≡ "为（**渐近意义下 RH 等价**的）对象找新机制" ⟹ **无缩小**；唐先生判断正确 ✓✓；**(4)** ⭐ **根因是方法论失效**：**关键词地图检查在"我发明新名字"时结构性失效**——`grep` 用的是**我的新词**（`n_{\rm off}`、`绝对计数界`），**必返回 0 命中**，故**无法**捕捉对象级重复 ✓✓

# C-129 · **核实与勘误：`n_{\rm off}(T)\le C` 是已审对象的重新发明 ＋ 地图检查的方法论失效**

> **时间**：2026-09-18 18:43 唐先生：**核实三问**——(a) `n_{\rm off}(T)\le C` 是否＝"离轴零点只能有限个"？(b) 该命题是否已在本项目内被证明等价于 RH？(c) 若同，则"寻找证明它的新机制"是否＝"寻找证明 RH 的新机制"（无缩小）？✓

---

## §0 结论（直答三问）

$$\textbf{答 (a)}：\boxed{\textbf{是同一个命题}}✓✓$$
$$\qquad n_{\rm off}(T)\ \text{非降且整数值} \Longrightarrow \textbf{有界} \iff \textbf{有限}（\text{两种表述等价}）✓$$
$$\qquad \text{且该对象}\ \textbf{已审}：\text{`RIGORIZATION-finitely-many-off-axis-reductio-boundary`}✓✓$$
$$\textbf{答 (b)}：\text{分两层}——$$
$$\qquad \textbf{命题层}：\text{RH}\Longrightarrow\exists C；\qquad \textbf{反向需}\ \text{`ISO`}（\text{"一}\Longrightarrow\text{无穷多"}）✓$$
$$\qquad \qquad ⚠️\ \text{而}\ \text{`ISO`}\ \textbf{在本项目内未证}（\text{`C-62`／`C-63` 已证其两输入循环}） \Longrightarrow \textbf{裸陈述下"离轴零点有限"严格弱于 RH}✓✓$$
$$\qquad \textbf{路线层}：\text{`RIGORIZATION` 档已证"这条反证法的天花板＝Li 判据在}\ n>2T＝\text{RH}" \Longrightarrow \textbf{路线在渐近意义下 RH 等价}✓✓$$
$$\qquad \Longrightarrow \text{故唐先生的原话"}\textbf{在渐近意义下等价于 RH}\text{"}\ \textbf{成立}（\text{就路线而言}）✓$$
$$\textbf{答 (c)}：\boxed{\textbf{是，无缩小}}✓✓\ \text{诊断（比例 vs 绝对）}\textbf{不改变逻辑地位}✓$$
$$\textbf{并且}：\text{`C-128` 的 (3) 表述}\ \textbf{有误，须勘误}✓✓$$

---

## §1 逐字证据（`RIGORIZATION` 档）

$$\text{原档状态（本档逐字转载）}：\text{无穷多离轴}\Longrightarrow\text{矛盾（无条件）}\Longrightarrow\text{排除无穷多}✓;\ \text{单离轴（有限）}：\lambda_n\ \text{破坏在}\ n\sim\frac{2\gamma^2}{1-2\beta}✓$$
$$\qquad \textbf{需证明}\ \lambda_n\ge0\ \text{到那个}\ n;\quad \textbf{但}\ \lambda_n\ge0\ \text{对所有}\ n＝\text{Li}\ \text{准则}＝\text{RH} \Longrightarrow \textbf{循环}✓✓$$
$$\textbf{循环点}：\text{需}\ \lambda_n\ge0\ \text{到}\ n\sim\frac{2\gamma^2\log T}{\delta};\ \text{对}\ \gamma\gtrsim\sqrt{T\delta/\log T}\ \text{的零点}，n\ \textbf{远超}\ 2T✓$$
$$\qquad \Longrightarrow \text{超出部分}\ \textbf{正是}\ \text{Li}\ \text{判据在长范围的情形}＝\text{RH}✓✓$$
$$\textbf{净结论}：\text{天花板}＝\textbf{Li 系数在}\ n>2T\ \textbf{的无条件下界};\quad n\le2T\ \text{内}＝\textbf{已验证高度}（\text{无新信息}）;\quad n>2T\ \text{外}＝\textbf{RH}✓✓$$
$$\text{第 132 行}：\text{本档净结论}\ \textbf{恰是"这条反证法现在立不住"}——\ \textbf{不是} \text{"已证明离轴零点只能有限个"}✓$$

## §2 逻辑清算（三条，逐条分清）

$$\textbf{(i)}\ \text{RH}\Longrightarrow\exists C：\text{成立}（\text{RH ⟹ 离线集空}）；\ \text{且}\ \text{`ISO`}\ \text{本身} \text{RH}\Longrightarrow\ \text{（空集满足"非空}\Longrightarrow\text{无穷"）}✓$$
$$\textbf{(ii)}\ \exists C\Longrightarrow\text{RH}：\textbf{需}\ \text{`ISO`};\ \text{而}\ \text{`ISO`}\ \textbf{未证}✓✓$$
$$\qquad \Longrightarrow \textbf{裸陈述下，"离轴零点有限"与 RH 的关系是"被蕴含"而非"等价"}✓$$
$$\qquad \qquad \text{（直观：}\text{"恰有 2 个离轴零点"}\ \text{满足"有限"但不满足 RH}）✓$$
$$\textbf{(iii)}\ \text{但}\ \textbf{路线层}：\text{`RIGORIZATION` 档的逐字结论}\ \textbf{正是}\ \text{"该反证法在}\ n>2T\ \text{外}＝\text{RH}"✓✓$$
$$\qquad \Longrightarrow \text{故"寻找证明}\ \exists C\ \text{的新机制"}\ \textbf{与"寻找证明 RH 的新机制"} \text{在}\ \textbf{渐近意义} \text{下是同一件事}✓✓$$

## §3 勘误登记

| 档 | 原表述 | 勘误 |
|:--|:--|:--|
| `C-128` (3) | "`\exists C:n_{\rm off}(T)\le C \iff \text{RH}`（等价，但形状不同）" | ⚠️ **改为**：`\text{RH}\Longrightarrow\exists C`；反向**需 `ISO`（未证）**；**路线层**在 `n>2T` 外＝RH（`RIGORIZATION`）|
| `C-128` (2) | "候选形状（本档）" | ⚠️ **非本档发现**：该对象已在 `RIGORIZATION-finitely-many-off-axis-reductio-boundary` 审过 ⟹ **重新发明** |
| `C-127`／`C-126`／`C-125` | 沿革 | ⚠️ 结论**导向了**该已审对象；须并记 |

$$\Longrightarrow \text{本档}\ \textbf{认领两处错误}：\text{(1) 表述过强（(3) 的} \iff\text{）；(2) 对象重复（未先查已审档）}✓✓$$

## §4 ⭐ 根因：关键词地图检查在"发明新名字"时**结构性失效**

$$\text{我执行的"查地图"：}\text{grep}\ \textbf{我的新词}（\text{`n_{\rm off}`}、\text{`绝对计数界`}、\text{`一致计数界`}） \Longrightarrow \textbf{必 0 命中}✓✓$$
$$\qquad ⚠️\ \text{故该方法}\ \textbf{结构性无法} \text{捕捉"对象级重复"} \text{—— 因为重复恰好发生在}\ \textbf{对象层面}，\ \text{而我查的是}\ \textbf{命名层面}✓✓$$
$$\qquad \qquad \text{对照：}\text{档案里的词是}\ \textbf{"离轴零点有限个"}（11 档命中）；\ \text{我从未 grep 它}✓✓$$
$$\Longrightarrow \textbf{对策（本档确立）}：$$
$$\qquad \text{(1)}\ \text{提出任何"对象"前，先把}\ \textbf{对象定义} \text{译成}\ \textbf{档案最可能用的词}（\text{本例："离轴零点有限个"／"单离轴"}），\ \text{再 grep}✓✓$$
$$\qquad \text{(2)}\ \text{若}\ \text{grep}\ \text{到已审档} \Longrightarrow \textbf{直接引用其判词}，\ \text{不新开案}（\text{`PRE-WORK MAP CHECK` 的既有硬规矩}）✓$$
$$\qquad \text{(3)}\ ⚠️\ \text{自检签名}：\text{若某档出现"}\textbf{本档新增形状／新的表述}"\ \text{而}\ grep\ \text{只命中本档} \Longrightarrow \textbf{先怀疑是重命名}✓✓$$
$$\Longrightarrow \text{这与}\ \text{`C-116`}\ \text{的教训}\ \textbf{同族}：\text{两者都是}\ \textbf{"形式/命名层面的动作"被误当成"实质推进"}✓✓$$

## §5 保留与净产出（诚实）

$$\textbf{作废}：\text{`C-128` 的"候选形状"（已审对象的重命名）};\quad \text{`C-128`(3) 的} \iff \text{表述}✓$$
$$\textbf{保留（诊断级，非路线级）}：$$
$$\qquad \text{(i)}\ \textbf{比例 vs 绝对}：\text{`rank`／`trace`／`inertia` 本体只给占比} \Longrightarrow \textbf{解释了现有工具为何证不出}（\text{但不使对象更易证}）✓$$
$$\qquad \text{(ii)}\ \textbf{整数性机制}：\text{"计数＋整数性}\Longrightarrow\text{排除"}\ \text{是}\ \textbf{唯一不付精度尺度} \text{的通道（解释验证法为何 log-free）}✓$$
$$\qquad \text{(iii)}\ \text{`C-126` 的"有限 vs 渐近"修正（log-free 排除只在有限范围）}✓$$
$$\textbf{未推进}：\text{`C-125`–`C-129` 这五档}\ \textbf{未推进地图};\ \text{是把}\ \textbf{已有对象用新词汇重述了一遍}✓✓$$

## §6 边界与回查

- ⚠️ 本档为**核实性勘误**，**不新增路线**；**不**声称 `ISO` 成立或不成立 ✓
- ⚠️ **不声称** RH；**不**修改原档（`RIGORIZATION`／`C-61` 等仅**逐字引用**）✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓
- **新立规矩**（§4(1)(2)(3)）**即刻生效** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:5x）`[纪律]`（先跑后写）

```
技术词 对象级重复          命中文件数=1  :: ./C129-…（本档）
技术词 命名层面          命中文件数=1  :: ./C129-…（本档）
技术词 重命名           命中文件数=36 :: ./MASTER-NOGO-AND-LIVE-PATHS.md ./V106-L3-Q3-… 等（**已有**）
```
**读数（按实测）**：`对象级重复`／`命名层面`＝**1 档（仅本档）⟹ 本档新增** ✓；⚠️ `重命名`＝**36 档**（**已有**，且**数量大**本身佐证"重命名"是本项目**反复出现**的问题）✓✓

```
⚠️ 唐先生 18:43 核实三问 —— **核实成立，本档直接认领两处错误**
✅ 逐字证据(RIGORIZATION-finitely-many-off-axis-reductio-boundary): 原档状态「无穷多离轴⟹矛盾(无条件) ⟹排除无穷多 ✓ | 单离轴(有限): λ_n 破坏在 n~2γ²/(1−2β) —— 需证 λ_n≥0 到那个 n | 但 λ_n≥0 对所有 n = Li 准则 = RH —— 循环」
   循环点: 需 λ_n≥0 到 n~2γ²logT/δ; 对 γ≳√(Tδ/logT) 的零点, n **远超** 2T ⟹ 超出部分**正是 Li 判据在长范围 = RH**
   净结论: 天花板 = **Li 系数在 n>2T 的无条件下界**; n≤2T 内 = 已验证高度(无新信息); n>2T 外 = **RH**
   第132行: 净结论恰是"这条反证法现在立不住" —— **不是**"已证明离轴零点只能有限个"
✅ 答(a): **是同一个命题** —— n_off 非降整数值 ⟹ **有界 ⟺ 有限**; 且该对象已审(RIGORIZATION 档)
✅ 答(b): 分两层 —— 命题层: RH ⟹ ∃C; 反向**需 ISO**(未证; C-62/C-63 已证其两输入循环) ⟹ **裸陈述下"离轴零点有限"严格弱于 RH**;
   路线层: RIGORIZATION 已证天花板 = n>2T 外 = RH ⟹ **路线在渐近意义下 RH 等价**(唐先生原话就路线而言成立)
✅ 答(c): **是, 无缩小** —— 诊断(比例 vs 绝对)不改变逻辑地位
⚠️ 勘误两处: (1) C-128 (3) 的"∃C ⟺ RH"**表述有误**(须改为 RH ⟹ ∃C, 反向需 ISO); (2) C-128 (2) 的"候选形状(本档)"**非本档发现** = 重新发明(RIGORIZATION 已审)
⭐ 根因(方法论失效): 我执行的"查地图"是 grep **我的新词**(n_off/绝对计数界/一致计数界) ⟹ **必 0 命中** ⟹ **结构性无法**捕捉对象级重复(重复在对象层面, 我查的是命名层面);
   档案里的词是"**离轴零点有限个**"(11 档命中), 我从未 grep 它
   对策(即刻生效): (1) 提出对象前先把对象定义译成**档案最可能用的词**再 grep; (2) 若命中已审档则直接引用其判词不新开案(PRE-WORK MAP CHECK 既有硬规矩);
   (3) 自检签名: 若某档称"新增形状/新表述"而 grep 只命中本档 ⟹ **先怀疑是重命名**
   ⟹ 与 C-116 教训**同族**: 两者都是"形式/命名层面的动作"被误当成"实质推进"
⭐ 保留(诊断级, 非路线级): (i) 比例 vs 绝对(解释现有工具为何证不出, 但不使对象更易证); (ii) 整数性机制(唯一不付精度尺度的通道, 解释验证法为何 log-free); (iii) C-126 的"有限 vs 渐近"修正
⚠️ 未推进: C-125–C-129 五档**未推进地图**, 是把已有对象用新词汇重述了一遍
⚠️ 不新增路线; 不声称 ISO 成立或不成立; 不修改原档; 未用 RH 作推导
✅ 净产出: ①直答三问(含两层区分: 命题层 vs 路线层) ②逐字证据 ③两处勘误登记 ④根因=关键词地图检查在命名层面结构性失效 + 三条对策(即刻生效) ⑤诚实清账(保留 vs 作废)
```
