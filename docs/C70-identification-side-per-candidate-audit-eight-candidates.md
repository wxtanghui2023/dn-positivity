已查地图：**逐档核对**（所查档：`C69`（识别侧规格卡，本会话前档）、`V188` §2／§4、`V192` §①③、`V193` §③④、`V194` §I／§III／§V／§VI、`V215` §3–§5、`V227` §4(4)(7)、`V259`、`V186`／`V187`、`POS1`、`V283`（值面墙）、`E18-NOGO-ALIGNMENT-2`（#49 恒等通道／#84 加权零密度）、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`papers/brown-thm2-classical/main.md`（BGSTB24 引文））。**结论**：8 条识别侧候选中 **6 条死于同一条**（它们**不是"接口"**而是统计量／对象）；**2 条是接口形态**（ARS／逆谱几何），分别死于"无实例"与"缺桥" ⟹ **全部收敛到同一个物**：**一条能读出 `β_*` 的合法接口** ✓

# C-70 · **识别侧逐条审计**（8 候选 × 输入/输出/读出量/违反边界/要救它需要什么）

> **时间**：2026-09-18 11:17 唐先生「继续」（承接 `C-69` §5 的"逐条筛"授权）
> **本档**：只做识别侧审计；**不判任何候选 ALIVE／DEAD**（除原档已判者，逐字引用）✓；不动对象侧 ✓

---

## §0 审计总表

| # | 候选（识别侧）| 输入是否**独立于零点** | 读出的量 | 能否读出 `β_*` | **违反** | 判定（出处）|
|:--:|:--|:--:|:--|:--:|:--|:--|
| 1 | **显式公式** | ✓（算术侧）| 零侧**线性泛函** `Σ_ρ f̂(γ_ρ)` | 原理上编码，**提取需无界精度** | **B4**（`F1a`：无新信息）＋封口(a) | **饱和**（`V188` §2；`V194` §III）|
| 2 | **零密度 `N(σ,T)`** | ✓ | 计数 | 只能给上界/密度 | **B4** ＋封口(a)／(d) | **同层**（`E18`#84 逐字：加权零密度"不提供超越均匀 `N(σ,T)` 的新信息/新机制"）|
| 3 | **Weil／Li 正性** | ✓ | 二次型符号 | 是（但 ⟺RH）| **B4**（`F1b`：不能以严格弱于 RH 的输入证明）＋封口(b) | **⟺ RH**（`POS1` 第三行逐字）|
| 4 | **inertia／rank–trace** | ✓ | 负指标 `n₋`、rank | 经**重数/退化** | **B3 边缘**＋封口(d) | **撞 0.6818287**（`V192` §③：谱实现族 `β`-内容＝退化计数＝`N₀ˢ/N_d`）|
| 5 | **ARS 根定位型** | ✓（形式逃逸）| `sup_{P_X=0} Re z` | **可能**（若 `ARS4` 成立）| 无（**形式逃逸 ✓**）| **UNINSTANTIATED**（`V227` §4；缺"实部钉定机制"＝`C-68` D3）|
| 6 | **Hedenmalm（算子系统）** | ✓ | `Ξ` 的**实根**边值特征值 | **否**（只依赖 `γ`）| **B4**＋封口(c) | **干净封死**（`V192` §② 逐字：离轴对落在**非实**零点上 ⟹ 构造取不到，"与是否假设 RH 无关"）|
| 7 | **逆谱几何** | ✓（素数侧）| 谱的几何不变量 | 需 **intertwiner** | **B2 边缘**（纯表示变换）| **缺桥 · BRIDGE-ONLY**（`V193` §③：`𝒜_ℙ≠𝒜_{{γ_n}}`；Wu–Sprung 造了 `V_ζ` 与 `V_ℙ` **但无桥**）|
| 8 | **素数侧二阶矩** | ✓ | `‖·‖²_HS`／配对相关 | 仅 `support≤1` | **B4**（需新算术输入）| **SUPPORT-1 墙**（`SUPPORT-1` closure §6 逐字：`support>1 ⟺` prime-pair 信息；无条件版 BGSTB24 仅到 `support≤1`）|

---

## §1 单条细读（"要救它需要什么"）

$$\textbf{1. 显式公式}：\text{需}\ \textbf{把提取变成"稳定、有限复杂度、定量可逆的 support localization"}（`V194` §III 的出路）\ ⟹ \text{即}\ \text{从"饱和"到"可提取"} ✗\ \text{（无已知实现）}$$
$$\textbf{2. 零密度}：\text{需}\ \textbf{在}\ \sigma=\tfrac12\ \text{层}\ \text{做同样的事}——\text{而}\ \text{`V235`-A 逐字：方法全在}\ \sigma=1\ \text{层（密度坐标层）};\ \text{"要把结论搬到}\ \tfrac12\ \textbf{必须引入抵消＝零点位置信息"} ✗$$
$$\textbf{3. Weil／Li}：\text{需}\ \text{一个}\ \textbf{not-Weil 型} \text{正性}＝\text{`L3`};\ \text{否决判据逐字：正性来源可归入}\ \{\text{有限性, Weil, 零点侧}\ L^2\}\ \text{或 height/log 型}\ ⟹\ \text{关} ✗$$
$$\textbf{4. inertia}：\text{需}\ \text{把上限}\ 0.6818287\ \text{推过}——\text{而它对应}\ \textbf{support}>1\ ⟹\ \text{回到}\ \#8 ✗$$
$$\textbf{5. ARS}：\text{需}\ \text{① 独立构造的}\ P_X;\ \text{② 过污染测试（}P_N\ \text{型淘汰）};\ \text{③ 过压力测试（}z^n-a\ \text{型不产生}\ \tfrac12）;\ \text{④}\ \textbf{实部钉定机制} ✗$$
$$\textbf{6. Hedenmalm}：\text{需}\ \text{一个}\ \textbf{能取到非实零点} \text{的对象}——\text{而}\ \text{`V192` §② 判：这是}\ \textbf{对象类型} \text{不允许} ✗$$
$$\textbf{7. 逆谱几何}：\text{需}\ \text{一条}\ \textbf{算术 intertwiner}\ \mathcal A_{\mathbb P\to\zeta};\ \text{唯一已知＝显式公式，已被}\ \#1\ \text{饱和覆盖} \Longrightarrow \text{`F4②`：显式公式＋}\mathcal R＝\textbf{纯表示变换}\ ⟹\ \text{杀} ✗$$
$$\textbf{8. 素数侧二阶矩}：\text{需}\ \textbf{support}>1\ \text{的跨尺度 prime-pair 关联}＝\text{`SUPPORT-1` 外部墙};\ \text{目前}\ \textbf{无候选} ✗$$

## §2 结构性读数（本档的核心发现）

$$\textbf{(i)}\ \text{6/8 死于}\ \textbf{同一条}：\text{它们}\ \textbf{不是"接口"}\ \text{而是}\ \textbf{统计量／对象} \Longrightarrow \text{它们在}\ B4/F1a\ \text{处即停（不提供新信息通道）}$$
$$\textbf{(ii)}\ \text{仅}\ 2/8\ \textbf{是接口形态}：\#5\ \text{ARS（无实例）};\ \#7\ \text{逆谱几何（缺桥）} \Longrightarrow \text{两条}\ \textbf{收敛到同一个物}$$
$$\boxed{\text{所需物}＝\text{一条}\ \textbf{合法接口}：\text{能读出}\ \beta_*\ (\text{或}\ \sup\ \text{相等})，\ \text{且过}\ B1\text{–}B5\ \text{＋四条封口}}$$
$$\qquad \text{名（档案既有）}：\text{`V215` §5}\ \textbf{非 canonical 双向识别接口} \equiv \text{`V193` §③}\ \textbf{intertwiner 缺失} \equiv \textbf{BRIDGE-ONLY}✓$$
$$\textbf{(iii)}\ ⚠️\ \text{本条为本会话}\ \textbf{第 3 次} \text{独立入口收敛到同一缺口}（\text{前两次：}C\text{-}61\ \text{§2C 第四类不变量};\ C\text{-}64/65\ \text{簿记→}support>1）$$

## §3 由此得到的**唯一可判定动作**（不新开方向）

$$\text{把"合法接口"写成}\ \textbf{存在性命题}（而非搜索）：$$
$$\qquad \exists\ \mathcal I：\text{（输入）独立于零点的算术数据}\to\text{（输出）}\beta_*\ \text{的恒等识别}\quad\text{s.t.}\ B1\text{–}B5\ \text{全过}$$
$$\qquad \text{判死标准（}\text{`V259`}）：\text{若}\ \mathcal I\ \text{可写成}\ \lim F_n（F_n\ \text{有限局部聚合}）\Longrightarrow \textbf{DEAD}✓$$
$$\qquad \text{首筛（按本表）}：\text{凡输出为}\ \textbf{线性泛函／符号／计数／模长} \text{者，先排除；只剩"非先验实谱却对}\ \beta-\tfrac12\ \text{非退化敏感"的形态}（\text{`V194` §VI}）✓$$

## §4 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 11:2x）`[纪律]`

```
技术词 识别侧逐条审计 命中文件数=1    :: ./C70-identification-side-per-candidate-audit-eight-candidates.md
技术词 要救它需要什么 命中文件数=1    :: ./C70-identification-side-per-candidate-audit-eight-candidates.md
技术词 intertwiner      命中文件数=5    :: ./C69-identification-side-spec-card-legal-interface-four-bounds-and-inverse-problem.md ./D-GRAM-1-audit-Z-and-integer-energy-are-incompatible.md ./CLOSED-ROUTES-MAP.md ...
技术词 非先验实谱  命中文件数=3    :: ./C69-identification-side-spec-card-legal-interface-four-bounds-and-inverse-problem.md ./C70-identification-side-per-candidate-audit-eight-candidates.md ./MASTER-STATUS-AND-CLOSURES.md
```
**读数（按实测）**：`识别侧逐条审计`／`要救它需要什么`＝**均仅本档（1 档 ⟹ 本档新增）** ✓；⚠️ `intertwiner`＝**5 档**、`非先验实谱`＝**3 档** ⟹ **档案已有**（含本会话前档 `C-69`）⟹ **引用，不列为本档提出** ✓

## §5 边界

- `[逐字]` §0 表内 8 条的判定出处、§1 各条的"需要什么"均**逐字或直接引用** ✓
- `[本档]` §0 表的组织方式、§2 的结构性读数（6/8 非接口）、§3 的存在性命题与首筛 ✓
- **不声称**：接口存在 ✗；不判候选 ALIVE／DEAD（除原档已判者）✓；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 任务（承接 C-69 §5 授权）：识别侧 8 候选逐条审计 = 输入/输出/读出量/违反边界/要救它需要什么
⚠️ 结果：1 显式公式=饱和｜2 零密度=同层｜3 Weil/Li=⟺RH｜4 inertia=撞 0.6818287｜5 ARS=UNINSTANTIATED｜
   6 Hedenmalm=对象类型不允许(只依赖 γ)｜7 逆谱几何=缺桥｜8 素数侧二阶矩=SUPPORT-1 墙
⚠️ 核心读数：(i) 6/8 死于同一条 —— 它们不是"接口"而是统计量/对象，故在 B4/F1a 即停；
   (ii) 仅 2/8 是接口形态（ARS 无实例、逆谱几何缺桥）⟹ 两条收敛到同一个物：一条能读出 β_* 的合法接口
   (= V215 §5 非 canonical 双向识别接口 = V193 §3 intertwiner 缺失 = BRIDGE-ONLY)
   (iii) 本会话第 3 次独立入口收敛到同一缺口
⚠️ 唯一可判定动作：把"合法接口"写成存在性命题（输入独立于零点 → 输出 β_* 恒等识别），
   判死标准 V259（可写成 lim F_n 有限局部聚合 ⟹ DEAD）；首筛：输出为线性/符号/计数/模长者先排除
✅ 净产出：①8 条逐条审计表 ✓；②"6/8 非接口"的structural读数 ✓；③所需物命名统一 ✓；④存在性命题与首筛 ✓
```
