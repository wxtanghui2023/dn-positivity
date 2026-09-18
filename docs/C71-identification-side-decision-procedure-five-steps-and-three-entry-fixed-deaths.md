已查地图：**逐档核对**（所查档：`C69`／`C70`（本会话前档）、`V215` §3（R1–R4＋反循环检查）、`V227` §4(4)(5)(7)（右边界弱化／压力测试／污染测试）、`V194` §I（F1 两问）／§III（饱和判据）／§V（四通道）／§VI（第四类严格定义）、`V259`（非聚合组合律）、`V193` §③（intertwiner）、`V192` §①③、`POS1`、`E18`#84、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`）。**结论**：流程可为；跑完 `#5`／`#7` 得到一个 **meta 读数**——"**接口**" ≠ "**统计量**" ≠ "**对象**" ≠ "**变换**"，而 8 条候选**全部属后三类** ⟹ 这是它们全部落空的**形式原因**；"接口"类**目前是空集**，其空集的名字就是 `BRIDGE-ONLY` ✓✓

# C-71 · **识别侧判定流程**（5 步）＋ 两个示例 ＋ **三类入口的固定死法**

> **时间**：2026-09-18 11:20 唐先生「继续」（承接 `C-70` 末的授权）
> **本档**：流程为**本档新造**（成分全部档案逐字）；示例为**已有候选**；**不判 ALIVE／DEAD**（除原档已判）✓

---

## §0 结论（先行）

$$\textbf{流程可为}\ ✓;\ \textbf{跑完两个示例后得到一个 meta 读数}：$$
$$\boxed{\text{"接口"}\ne\text{"统计量"}\ne\text{"对象"}\ne\text{"变换"};\qquad 8\ \text{条候选}\ \textbf{全部属后三类}}$$
$$\qquad \Longrightarrow\ \textbf{这就是它们全部落空的形式原因};\ \text{"接口"类}\ \textbf{目前＝空集};\ \text{其空集的名字＝}\textbf{BRIDGE-ONLY}\ ✓✓$$

---

## §1 流程（Step 0–5，每步附 kill 规则）

$$\textbf{Step 0（入口分类）}：\text{候选属}\ \{\text{统计量},\ \text{对象},\ \text{变换／映射},\ \textbf{接口}\}\ \text{哪一类？}$$
$$\qquad \text{（"接口"定义：}\underbrace{\text{独立于零点的算术数据}}_{\text{输入}}\to\underbrace{\beta_*\ \text{或}\ \sup\ \text{相等}}_{\text{输出}}\text{，且是}\ \textbf{识别} \text{而非变换）}$$
$$\textbf{Step 1（输入审查）}：\text{输入是否}\ \textbf{预设} \text{零点集（或等价信息）？}\ \text{是}\ \Longrightarrow\ \textbf{DEAD（B1 循环）}$$
$$\qquad \text{变换类：须检查}\ \textbf{intertwiner} \text{是否存在};\ \text{若唯一 intertwiner＝显式公式}\ \Longrightarrow\ \text{转 Step 2 即 DEAD}✓$$
$$\textbf{Step 2（输出类型筛＝四条封口）}：\text{输出属}\ \{\text{线性／迹}\ (a)\mid\text{二次型／符号}\ (b)\mid\text{模长}\ (c)\mid\text{计数／重数}\ (d)\}\ \Longrightarrow\ \textbf{DEAD}$$
$$\qquad \text{其余须是"}\textbf{非先验实谱、却对}\ \beta-\tfrac12\ \text{非退化敏感}\text{"（}\text{`V194` §VI 第四类型}）✓$$
$$\textbf{Step 3（非聚合判据）}：\text{可否写成}\ \lim F_n（F_n\ \textbf{有限局部聚合}）？\ \text{可}\ \Longrightarrow\ \textbf{DEAD（`V259`）}$$
$$\textbf{Step 4（合法性 B1–B4）}：\text{非循环（反循环检查}\ \rho\to X_\rho\to\rho）\mid\text{非编码（污染测试；}P_N\ \text{型淘汰）}\mid\textbf{刚性强制（R3，不得"恰好相等"）}\mid\text{F1 两问}✓$$
$$\textbf{Step 5（压力／独立）}：\text{过}\ z^n-a\ \text{型压力测试（形状吻合}\ \textbf{不产生}\ \tfrac12）\mid\text{过}\ \textbf{ARS4}（\beta_X=\beta_*\ \textbf{可独立证明}）✓$$
$$\Longrightarrow\ \text{判定：}\textbf{DEAD（第几步）}／\textbf{待核}／\textbf{合法}✓$$

## §2 示例 A：`#5` ARS 根定位型（逐步）

| 步 | 结果 |
|:--|:--|
| Step 0 | **对象 + 识别组合**（其识别部分为 `sup_{P_X=0}Re z = β_*`）⟹ **接口形态** ✓（三类中唯一的）|
| Step 1 | 输入 `P_X` **独立于零点** ✓（不循环）|
| Step 2 | 输出＝`sup Re`；**不属四类** —— 且这正是 **`V227-A`（定理级）** 的内容：`sup Re` **不是模长多重集的不变量** ⟹ **通过** ✓✓（＝"**形式逃逸**"的技术含义）|
| Step 3 | 非聚合判据：**待核** ⚠️（对 ARS 未做）|
| Step 4 | B1 ✓；**B2 ✗**（污染测试**未过**：尚无独立于零点定义的 `P_X` 实例）；B3／B4 待核 |
| Step 5 | **压力测试 ✗**（`z^n-a` 已证："存在算术根定位"**本身完全不产生 `1/2`**）⟹ 需"**边界内生锁定**" |
$$\Longrightarrow\ \textbf{判定}：\textbf{形态合法（唯一通过 Step 1–2 者）／实质未实例化};\ \text{卡在}\ \textbf{B2 ＋ Step 5}$$
$$\qquad \text{下一件事}：\text{给出一个}\ \textbf{具体的}\ P_X\ \text{候选}，\text{并过 B2 ＋ Step 5}✓$$

## §3 示例 B：`#7` 逆谱几何（逐步）

| 步 | 结果 |
|:--|:--|
| Step 0 | **变换**（谱 → 几何）—— 不是接口 |
| Step 1 | 输入须为 **ζ 侧**谱；若用素数侧 ⟹ `V193` §③ 逐字：`𝒜_ℙ ≠ 𝒜_{{γ_n}}` ⟹ **须 intertwiner**；而唯一已知 intertwiner＝**显式公式** ⟹ 转 Step 2 |
| Step 2 | 显式公式＝**线性** ⟹ 封口 (a) ⟹ **DEAD**（且 `F4②`：显式公式＋`ℛ`＝**纯表示变换** ⟹ 杀）|
$$\Longrightarrow\ \textbf{判定}：\text{不补桥 ⟹ Step 1 不闭合};\ \text{补桥 ⟹ Step 2 DEAD} \Longrightarrow \boxed{\textbf{BRIDGE-ONLY（ALIVE BUT UNINSTANTIATED）}}✓$$

## §4 ⭐ **三类入口的固定死法**（本档 meta 读数；本会话新增）

| 入口类 | 固定死在 | 原因（逐字／定理）|
|:--|:--:|:--|
| **统计量** | **Step 2** | 输出类型必落在四封口之一（线性＝饱和／二次型＝⟺RH／模长＝`V227-A`／计数＝`0.6818287`）|
| **对象** | **Step 5** | **形状吻合是廉价的**（`z^n-a`：模长-辐角耦合 ✓、计算可做 ✓，但 `β` 可任意移动 ⟹ 不产生 `1/2`）|
| **变换／映射** | **Step 1**（缺 intertwiner）或补桥后 **Step 2** | `𝒜_ℙ≠𝒜_{{γ_n}}`；唯一已知桥＝显式公式 ⟹ 落线性封口 |
| **接口** | —— | ⚠️ **目前空集**；空集的名字＝`BRIDGE-ONLY`（`V193` §③＋`V215` §5）|
$$\Longrightarrow\ \boxed{\text{8 条候选全部属前三类} \Longrightarrow \text{这是"全部落空"的}\textbf{形式原因};\ \text{要往前，必须}\textbf{造第四类入口＝接口}}✓✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 11:2x）`[纪律]`

```
技术词 判定流程     命中文件数=3    :: ./RESEARCH-CONSTITUTION.md ./V198-mechanism-II-closure-gate-executable-restart-criteria.md ./GPS-generation-principle-specification.md
技术词 固定死法     命中文件数=0
技术词 三类入口     命中文件数=0
技术词 接口.*统计量.*对象.*变换 命中文件数=0
```
**读数**：`固定死法`／`三类入口`／"接口≠统计量≠对象≠变换"＝**0 档 ⟹ 本档新增** ✓；⚠️ `判定流程`＝**3 档 ⟹ 档案已有**（通用词）⟹ **引用，不列为本档提出** ✓

## §6 边界

- `[逐字]` §1 各步的判据来源（B1–B5／四条封口／`V259`／`V227-A`／`V193` §③／`V194` §VI）、§2–§3 的判定均**逐字或直接引用** ✓
- `[本档]` 五步流程的**编排**、§2／§3 的逐步执行、§4 的三类入口固定死法 ✓
- **不声称**：流程完备（它只是 B1–B5＋四封口的可执行化）✗；接口存在 ✗；不判 ALIVE／DEAD（除原档已判）✓；不证 RH ✗
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 任务（承接 C-70 授权）：把 B1–B5 + 四条封口 写成可执行判定流程，并用 #5/#7 跑示例
⚠️ 流程：Step 0 入口分类 → Step 1 输入审查（预设零点 ⟹ DEAD）→ Step 2 输出类型筛（四封口）→
   Step 3 非聚合（V259）→ Step 4 合法性 B1–B4 → Step 5 压力测试 + ARS4 ⟹ DEAD(第几步)/待核/合法
⚠️ 示例 A（#5 ARS）：通过 Step 1–2（形式逃逸的技术含义＝sup Re 不属四类，V227-A 定理级）；
   卡在 B2（污染测试未过）+ Step 5（压力测试未过，z^n-a）⟹ 形态合法／实质未实例化
⚠️ 示例 B（#7 逆谱几何）：Step 0 判为"变换"；不补桥 ⟹ Step 1 不闭合；补桥（唯一＝显式公式）⟹ Step 2 DEAD
   ⟹ BRIDGE-ONLY（ALIVE BUT UNINSTANTIATED）
⚠️ ⭐ Meta 读数：统计量→死 Step 2；对象→死 Step 5；变换→死 Step 1/2；而"接口"类＝空集
   ⟹ 8 条候选全部属前三类 = "全部落空"的形式原因
✅ 净产出：①五步判定流程 ✓；②两个逐步示例 ✓；③三类入口固定死法 ✓；④"接口类空集"的形式原因 ✓
```
