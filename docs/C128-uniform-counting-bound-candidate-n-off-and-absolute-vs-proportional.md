已查地图（所查：`C-127`（破法＝在极限中存活的一致整数性／有限性界；`V259`；`V211` 残余）、`C-59`／`C-60`／`REFRAME`（**`ISO`：`\{\rho:\operatorname{Re}\rho\ne\tfrac12\}\ne\varnothing\Longrightarrow` 该集}\ \textbf{无穷}**、"一⟹无穷多"）、`V185`／`V186`（**rank／trace／inertia 型方法**只给**比例**上界：`N_0^s/N\ge2-R`，`0.6725`／`0.6828287`）、`V188` §2（聚合／逐点）、`V211` §5（**八类"有限层正常／无限层异常"机制，全落已封类；残余未实例化**）、`V150` W2，`C-116`（**登记不否决**））。**结论**：**(1)** 把"破法是否存在"形式化为：`\exists` 与 `T` 无关的一致计数界，对象为**整数计数**的算术量 ✓；**(2)** ⭐ **找到一个具体候选形状**：`n_{\rm off}(T):=\#\{\text{离线零点}:|\gamma|\le T\}`，问 `\exists C:\ n_{\rm off}(T)\le C\ \forall T`（＝"离线零点只有有限多个"）✓✓ —— 它同时具备**两个关键性质**：**(a) 整数计数** ⟹ **整数性机制适用**（`C-127` 唯一已知的"计数}\Rightarrow\text{排除"通道）；**(b) `log`-free 陈述**（不含间距尺度）⟹ **不在尺度墙的形态范围内** ✓✓；**(3)** 而由 `ISO`（一⟹无穷多）⟹ **`\exists C:n_{\rm off}(T)\le C` ⟺ RH**（**等价，但形状不同**）✓✓；**(4)** ⟹ 障碍被**精确重述**为：**无任何已知机制给出"绝对（非比例）"计数界** —— 已知界**全是比例型**（离线比例 `\le0.318`，来自 `0.682` 上限；且 `rank`／`trace`／`inertia` 型方法**本质上**只给比例）✓✓；**(5)** ⟹ 与 `V211` 残余对接：破法所需类型＝**绝对计数界**＝**非加性**，而 `V211` 残余（非加性／非上同调／非 `index`／非 `\Pi^1_1`／非选择的"有限\to\text{无限缺陷"）**正是该类型** ✓✓

# C-128 · **破法形式化：一致计数界 ＋ 候选形状 `n_{\rm off}(T)\le C` ＋ 障碍重述为"绝对 vs 比例"**

> **时间**：2026-09-18 18:36 唐先生：**「继续」** ⟹ 问破法的可能性：是否存在与 `T` 无关的一致计数界，其对象不是零点而是某个有限算术对象 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{形式化}：\text{破法}\iff\exists\ \text{与}\ T\ \textbf{无关} \text{的一致计数界};\ \text{对象须为}\ \textbf{整数计数}✓$$
$$\textbf{(2)}\ ⭐\ \textbf{候选形状（本档）}：n_{\rm off}(T):=\#\{\text{离线零点}:|\gamma|\le T\};\quad \text{问}\ \boxed{\exists C:\ n_{\rm off}(T)\le C\ \ \forall T}✓✓$$
$$\qquad \text{（即"离线零点只有有限多个"）—— 它同时具备：}✓$$
$$\qquad \qquad \textbf{(a)}\ \textbf{整数计数} \Longrightarrow \textbf{整数性机制适用}（\text{`C-127` 唯一已知的"计数}\Rightarrow\text{排除"通道}）✓✓$$
$$\qquad \qquad \textbf{(b)}\ \textbf{log-free 陈述}（\text{不含间距尺度}） \Longrightarrow \textbf{不在尺度墙的形态范围内}✓✓$$
$$\textbf{(3)}\ \text{而由}\ \textbf{`ISO`}（\text{一}\Longrightarrow\text{无穷多}） \Longrightarrow \boxed{\exists C:\ n_{\rm off}(T)\le C \iff \text{RH}}（\textbf{等价，但形状不同}）✓✓$$
$$\textbf{(4)}\ \Longrightarrow\ \text{障碍}\ \textbf{精确重述}：\boxed{\text{无任何已知机制给出"}\textbf{绝对（非比例）}\text{"计数界}}✓✓$$
$$\qquad \text{已知界}\ \textbf{全是比例型}：\text{离线比例}\ \le0.318（\text{来自}\ 0.682\ \text{上限}）;\ \text{且}\ rank／trace／inertia\ \text{型方法}\ \textbf{本质上} \text{只给比例}✓✓$$
$$\textbf{(5)}\ \Longrightarrow\ \text{与}\ \text{`V211` 残余对接}：\text{破法所需类型}＝\textbf{绝对计数界}＝\textbf{非加性}✓$$
$$\qquad \text{而}\ \text{`V211` 残余}（\text{非加性／非上同调／非 }index／\text{非}\ \Pi^1_1／\text{非选择的"有限}\to\text{无限缺陷"}）\ \textbf{正是该类型}✓✓$$

---

## §1 形式化

$$\text{`C-127` 破法}：\exists\ \text{一致有限性界}：\forall T:\ \#\{\text{区域内对象}\}\le C<1✓$$
$$\qquad ⚠️\ \text{但它默认"对象"可被}\ \textbf{一致界住};\ \text{本档追问}：\text{这样的对象}\ \textbf{存不存在}?\ \text{在哪一类里}?✓$$
$$\text{条件}：\text{(i) 对象由}\ \textbf{算术数据} \text{定义};\ \text{(ii) 计数为}\ \textbf{整数};\ \text{(iii) 界}\ \textbf{与}\ T\ \text{无关}✓$$
$$\qquad \text{（(ii) 是"计数}\Rightarrow\text{排除"的}\ \textbf{必要条件}：\text{非整数计数无法被}\ <1\ \text{界转化为排除}）✓✓$$

## §2 ⭐ 候选形状：`n_{\rm off}(T)\le C`

$$\text{定义}：n_{\rm off}(T):=\#\{\rho:\ \operatorname{Re}\rho\ne\tfrac12,\ |\operatorname{Im}\rho|\le T\}✓$$
$$\textbf{(a) 整数性}：n_{\rm off}(T)\ \text{是}\ \textbf{整数} \Longrightarrow \text{若}\ n_{\rm off}(T)<1\ \text{则}\ =0✓✓$$
$$\qquad \Longrightarrow \text{`C-127` 的机制}\ \textbf{直接适用}（\text{唯一不付精度尺度的通道}）✓✓$$
$$\textbf{(b) log-free}：\text{陈述}\ \exists C\ \forall T:\ n_{\rm off}(T)\le C\ \textbf{不含}\ \log T✓✓$$
$$\qquad \Longrightarrow \text{它}\ \textbf{不在} \text{`C-126`／`C-127` 的"逐点结论必含间距尺度"的}\ \textbf{形态范围} \text{内}✓✓$$
$$\qquad \qquad \text{（即：这是一个}\ \textbf{计数型} \text{的、}\ \textbf{可能避开尺度墙} \text{的 RH 表述}）✓✓$$

## §3 `ISO` 的作用：等价，但换形

$$\text{`ISO`（\text{`C-59`}／\text{`REFRAME`}）}：\{\rho:\operatorname{Re}\rho\ne\tfrac12\}\ne\varnothing \Longrightarrow \text{该集}\ \textbf{无穷}✓✓$$
$$\qquad \text{取逆否}：\text{离线集}\ \textbf{有限} \Longrightarrow \text{离线集}=\varnothing \Longrightarrow \text{RH}✓✓$$
$$\qquad \Longrightarrow \boxed{\exists C:\ n_{\rm off}(T)\le C\ \text{（有限）} \iff \text{RH}}✓✓$$
$$\qquad ⚠️\ \textbf{诚实}：\text{故这不是"更弱的一步"，而是}\ \textbf{另一种形状};\ \text{价值在}\ \textbf{形状}（\text{整数性机制可适用 ＋ log-free}）✓$$
$$\qquad \qquad \text{且}\ \text{`C-123` 教训一致：}\text{该变体}\ \textbf{钉在}\ \tfrac12 \Longrightarrow \text{按 `POS1` 型推理}\ \textbf{本就应等价}✓$$

## §4 ⭐ 障碍重述：**绝对 vs 比例**

$$\text{已知全部计数结果}：n_{\rm off}(T)\le(1-0.6828287)\,N(T)\ \text{型}\（\text{比例}）✓$$
$$\qquad \text{（}\text{`V185`／`V186`}：N_0^s/N\ge2-R（\psi），\ 0.6725（\psi_{MT}）;\ \text{上限}\ 0.68185／0.6828287）✓$$
$$\qquad \text{而}\ N(T)\sim\frac{T}{2\pi}\log T\to\infty \Longrightarrow \textbf{比例界}\ \textbf{永不给绝对界}✓✓$$
$$\textbf{结构理由}：rank／trace／inertia\ \text{型方法的本体是}\ \text{矩阵的}\ \textbf{秩／迹不等式}✓$$
$$\qquad \text{秩}\le r\ \text{给出的是}\ \textbf{"占比"} \text{型结论}（\text{如}\ \frac{N_0^s}{N}\ge2-R） \Longrightarrow \textbf{本质上比例}✓✓$$
$$\qquad \Longrightarrow \boxed{\text{要绝对界，须}\ \textbf{非秩／迹型} \text{机制} \Longrightarrow \textbf{非加性}}✓✓$$

## §5 与 `V211` 残余的对接 ＋ 边界

$$\text{`V211` 残余（逐字要点）}：\text{需要"}\textbf{非加性}／\text{非上同调}／\text{非 }index／\text{非}\ \Pi^1_1／\text{非选择的"有限}\to\text{无限缺陷"}✓$$
$$\qquad \Longrightarrow \text{本档的}\ \textbf{"绝对计数界"}\ \text{正是}\ \textbf{一个具体形状} \text{的该类对象}✓✓$$
$$\qquad \qquad \text{（因为"比例"＝可加型；"绝对"＝非加性）}✓$$
$$\Longrightarrow \text{故本档}\ \textbf{把 `V211` 的残余实例化了一格}：\boxed{\text{求一个}\ \textbf{非秩型} \text{的一致计数机制}}✓✓$$
- ⚠️ **不否决**（`C-116`）：本档**不**声称绝对计数界不可能；只登记"已知全为比例型"（**归纳级**）✓
- ⚠️ §3 的**等价性**（⟺ RH）**不**视为退步：形状价值已述 ✓
- **不声称**：绝对计数界存在或不存在 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导**（`ISO` 为**引用**）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:4x）`[纪律]`（先跑后写）

```
技术词 绝对计数界          命中文件数=1  :: ./C128-…（本档）
技术词 比例型           命中文件数=4  :: ./DOOR5c-DFMR-conversion-read.md ./CLOSED-ROUTES-MAP.md 等（**已有**）
技术词 非秩型           命中文件数=1  :: ./C128-…（本档）
```
**读数（按实测）**：`绝对计数界`／`非秩型`＝**1 档（仅本档）⟹ 本档新增** ✓；⚠️ `比例型`＝**4 档**（`DOOR5c`／`CLOSED-ROUTES-MAP` 等 **已有**）⟹ 本档为**沿用** ✓

```
⚠️ 唐先生 18:36「继续」⟹ 问破法可能性: 是否存在与 T 无关的一致计数界, 其对象不是零点而是某个有限算术对象
⭐ (1) 形式化: 破法 ⟺ ∃ 与 T 无关的一致计数界; 条件 (i) 算术定义 (ii) 计数为**整数** (iii) 界与 T 无关;
   (ii) 是"计数⇒排除"的必要条件(非整数计数无法被 <1 界转化为排除)
⭐⭐ (2) 找到具体候选形状: **n_off(T) := #{离线零点 : |γ| ≤ T}**, 问 **∃C: n_off(T) ≤ C ∀T**(即"离线零点只有有限多个")
   它同时具备: (a) **整数计数** ⟹ 整数性机制直接适用(C-127 唯一不付精度尺度的通道);
   (b) **log-free 陈述** ⟹ **不在尺度墙的形态范围内** —— 这是一个**计数型**的、**可能避开尺度墙**的 RH 表述
⭐ (3) ISO 的作用(C-59/REFRAME): 离线集非空 ⟹ **无穷**; 取逆否: 离线集有限 ⟹ 空 ⟹ RH
   ⟹ **∃C: n_off(T) ≤ C ⟺ RH**(等价, 但形状不同); 诚实: 不是更弱的一步, 而是另一种形状; 价值在形状(整数性机制可适用 + log-free)
   且与 C-123 教训一致: 该变体钉在 1/2 ⟹ 按 POS1 型推理本就应等价
⭐⭐ (4) 障碍精确重述: **无任何已知机制给出"绝对(非比例)"计数界**
   已知全部计数结果都是**比例型**(n_off(T) ≤ (1−0.6828287)N(T); V185/V186: N_0^s/N ≥ 2−R)
   而 N(T) ~ (T/2π)log T → ∞ ⟹ **比例界永不给绝对界**
   结构理由: rank/trace/inertia 型方法的本体是矩阵的秩/迹不等式; 秩 ≤ r 给出的是**"占比"**型结论(如 N_0^s/N ≥ 2−R) ⟹ **本质上比例**
   ⟹ **要绝对界须非秩/迹型机制 ⟹ 非加性**
⭐ (5) 与 V211 残余对接: V211 残余=需"非加性/非上同调/非 index/非 Π^1_1/非选择的有限→无限缺陷"
   ⟹ 本档的"绝对计数界"**正是该类的一个具体形状**(比例=可加型; 绝对=非加性)
   ⟹ **把 V211 的残余实例化了一格: 求一个非秩型的一致计数机制**
⚠️ 不否决(C-116): 不声称绝对计数界不可能, 只登记"已知全为比例型"(归纳级); §3 等价性不视为退步(形状价值已述); 不证 RH
✅ 净产出: ①破法形式化(一致计数界的三个条件) ②候选形状 n_off(T) ≤ C(整数性适用 + log-free, 可能避开尺度墙) ③ISO ⟹ 与 RH 等价(换形)
   ④障碍重述为"绝对 vs 比例"(含结构理由: 秩/迹型本质比例 ⟹ 需非加性) ⑤与 V211 残余对接: 绝对计数界=其一个具体形状
```
