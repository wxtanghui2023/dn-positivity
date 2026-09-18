已查地图（**先查后写**）：`M4-C6-REFINAL`（门序：`TESTABLE-1` → `F1–F8` → 端点分支；`F5` 判据）、`FILTER-TESTABLE-1`（`TESTABLE-1` 前提：候选定义须能在**无欧拉积**的函数上写出）、`C-110` `C6` 六条件、`C-122` 三要求、`C-111`（端点 `\tfrac12` 阶）、`C-115`（`\Lambda\le0` ⟺ RH；同墙异述）、`CLOSED-ROUTES-MAP:228`（DBN 线已登记闭合）、`V159`／M6（"运动来自我们的坐标选择"）、`V188` §2（聚合／逐点）。**结论**：⭐ 按唐先生 21:07「**我们需要的就是创建这么一个新的，机制能够认可的东西**」⟹ **造三个候选并跑门**：**候选 A（算术变形＝部分欧拉积）死在 `TESTABLE-1`**（DH 上无法定义）; **候选 B（坐标变形＝DBN 热流）死在 `F2`**（坐标选择）＋`F1` 风险; **候选 C（Dirichlet 级数截断）死在 `F3`／M2**（极限不恢复零结构）⟹ **三者各死于不同门** ⟹ ⭐⭐ **门序由此反推出一个三条件规格**：缺的对象必须是 **(i) 算术的（非坐标）+ (ii) 无欧拉积仍可定义 + (iii) 其极限恢复零结构且钉住 `\beta_*`** ⟹ 附：**对 `M4-C6-REFINAL` §2 的一处诊断修正**——`\Lambda` 线的 `F5` 其实**可满足**（有限验证＝独立输入），其墙是**上界天花板**（`c_\infty>0`）而非 `F5` ✓✓

FREEZE-ACK: 本档即冻结期内的构造尝试与门序反推（依 `§8.1`；不产候选结论，仅登记规格）

D0: 本档对象 = **三个构造候选的门序结果** ＋ **由门序反推的三条件规格** —— 关系 = 构造尝试与规格化，非新机制成立
D1: 0

# CREATE-SPEC-1 · **造三个候选，跑门序，反推出"能被机制认可"的三条件规格**

> **时间**：2026-09-18 21:07 唐先生：**「目前肯定是找不到，不然就不会有RH问题了。我们需要的就是创建这么一个新的，机制能够认可的东西」** ✓✓

---

## §0 结论（先行）

$$\text{唐先生把任务从"}\textbf{找}\text{"改成"}\textbf{造}\text{"}，\ \text{并给出验收标准}：\textbf{让候选跑我们的门序}✓✓$$
$$\textbf{结果}：\text{造了 3 个，}\ \textbf{各死于不同的门}：$$
$$\qquad \textbf{候选 A}（\text{算术变形＝部分欧拉积}\ \prod_{p\le y}\text{）} \Longrightarrow \textbf{死于 `TESTABLE-1`}\（\text{DH 上无法定义}）✗$$
$$\qquad \textbf{候选 B}（\text{坐标变形＝DBN 热流}\ H_t\text{）} \Longrightarrow \textbf{死于 `F2`}\（\text{坐标选择}）＋`F1` 风险✗$$
$$\qquad \textbf{候选 C}（\text{Dirichlet 级数截断}\ \sum_{n\le N}\text{）} \Longrightarrow \textbf{死于 `F3`／M2}（\text{极限不恢复零结构}）✗$$
$$\Longrightarrow ⭐⭐\ \textbf{门序反推出三条件规格}：\boxed{\text{缺的必须是}\ \text{(i)}\ \textbf{算术的}（\text{非坐标}）\ +\ \text{(ii)}\ \textbf{无欧拉积仍可定义}\ +\ \text{(iii)}\ \textbf{极限恢复零结构且钉住}\ \beta_*}✓✓$$

---

## §1 验收标准（"机制能够认可"＝ 通过门序）

$$\text{门 1}\ \text{`TESTABLE-1`}：\text{定义须能在}\ \textbf{无欧拉积} \text{的函数（DH／Epstein）上写出}✓$$
$$\text{门 2}\ \text{`F1`–`F8`}：\text{非正性／非坐标／钉点／非模长／}\textbf{独立输入}／\text{解析型}／\textbf{报火}（\text{DH／Epstein}）／\text{非污染}✓$$
$$\text{门 3}\ \text{端点分支}：\text{临界事件}\ \textbf{不得}\ \text{是 Hölder}\ \tfrac12\ \text{阶分支（否则一致转移不可能）}✓$$
$$\text{附}\ \text{`D0`／`D1` ＋ 型标签 ＋ 引用纪律}✓$$

## §2 三个候选与各自的门序结果

### 候选 A：**算术变形**（部分欧拉积 `\prod_{p\le y}`）

$$\text{对象}：\zeta_y(s):=\prod_{p\le y}(1-p^{-s})^{-1};\quad \text{变形参数}\ y＝\textbf{素数截断}（\textbf{算术的！}）✓$$
$$\qquad \text{已知等价（经典）}：\text{欧拉积在}\ \operatorname{Re}s>\tfrac12\ \text{的收敛}\iff\zeta\ \text{在}\ \operatorname{Re}s>\tfrac12\ \text{无零点}\iff\text{RH}✓✓$$
$$\qquad \Longrightarrow \text{其}\ \textbf{收敛边界＝}\beta_*：\ \text{`F3` 钉点}\ ✓;\ \text{变形参数算术}\ \Longrightarrow \text{`F2` 通过}\ ✓✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{DH 没有局部因子} \Longrightarrow \prod_{p\le y}\ \text{在 DH 上}\ \textbf{无法定义} \Longrightarrow \boxed{\textbf{死于 `TESTABLE-1`}}✗$$
$$\qquad \Longrightarrow \text{按 `FILTER-TESTABLE-1` §3：}\textbf{不予受理} \text{（无法判断它报火还是盲）}✗$$

### 候选 B：**坐标变形**（DBN 热流 `H_t`）

$$\text{对象}：\Lambda(f)=\inf\{t:f*G_t\ \text{零点全实}\};\quad \text{变形参数}\ t＝\textbf{流时间（坐标！）}✓$$
$$\qquad \textbf{门 1 通过}：\text{只需"实整函数＋热半群"，}\ \textbf{不需欧拉积} ⟹ \text{可写在 DH 上}✓✓$$
$$\qquad \textbf{门 2：`F7` 报火} ✓（\Lambda_{\rm DH}\neq\Lambda_\zeta）;\ \textbf{但 `F2` 命中} ✗（\text{`V159`／M6："运动来自我们的坐标选择"}）;\ `F1` 风险 ⚠️$$
$$\qquad \Longrightarrow \boxed{\textbf{死于 `F2`}}✗$$

### 候选 C：**级数截断**（`\sum_{n\le N}n^{-s}`）

$$\text{对象}：\zeta_N(s)=\sum_{n\le N}n^{-s};\quad \text{变形参数}\ N＝\textbf{级数截断}（\text{算术可数}）✓$$
$$\qquad \textbf{门 1 通过} ✓（\text{DH 亦有 Dirichlet 系数}）;\ \textbf{`F2` 通过} ✓（\text{截断非坐标}）✓✓$$
$$\qquad ⚠️\ \text{但部分和的零点}\ \textbf{不收敛到}\ \zeta\ \text{的零点} \Longrightarrow \textbf{`F3` 不钉点}✗;\ \text{且"截断＋取极限"}\ \in\ \text{M2 类} \Longrightarrow \text{需}\ \textbf{无界精度}（\text{`V188` §2}）✗✗$$
$$\qquad \Longrightarrow \boxed{\textbf{死于 `F3`／M2}}✗$$

## §3 ⭐⭐ 门序反推出的三条件规格（本档核心产出）

$$\text{三个失败}\ \textbf{恰好各缺一条}：$$
$$\qquad \text{A 缺 (ii)}：\text{算术}\ ✓、\text{钉点}\ ✓，\ \text{但}\ \textbf{无欧拉积就定义不了}✗$$
$$\qquad \text{B 缺 (i)}：\text{可测}\ ✓、\text{钉点}\ ✓，\ \text{但}\ \textbf{变形是坐标}✗$$
$$\qquad \text{C 缺 (iii)}：\text{可测}\ ✓、\text{算术}\ ✓，\ \text{但}\ \textbf{极限不恢复零结构}✗$$
$$\Longrightarrow \boxed{\text{被机制认可的对象}\ ＝\ \text{同时满足}\ \text{(i)}\ \textbf{算术的（非坐标）}\ +\ \text{(ii)}\ \textbf{无欧拉积仍可定义}\ +\ \text{(iii)}\ \textbf{极限恢复零结构且钉住}\ \beta_*}✓✓$$
$$\qquad \text{这三条}\ \textbf{分别由 A／B／C 三次失败}\ \text{逐条"见证"} \Longrightarrow \ \text{不是凭空拟定的清单}✓✓$$

## §4 ⚠️ 一处诊断修正（对 `M4-C6-REFINAL` §2 的 `F5` 行）

$$\text{原文说}\ M4\ \textbf{"`F5` 处死"}；\ \textbf{更准确的说法}：$$
$$\qquad \Lambda\ \text{线的}\ \textbf{输入是独立的}（\text{有限验证（\text{Platt–Trudgian}）＝非 RH 强度的真输入};\ \text{2026-08-19 的}\ \Lambda\le0.1787854\ \textbf{正只消耗此输入}）✓✓$$
$$\qquad \Longrightarrow \text{其墙}\ \textbf{不是 `F5`（输入）}，\ \text{而是}\ \textbf{天花板}（c_\infty>0：\text{方法族的可达上限，}\ 0.22\to0.2\to0.1788\ \text{而}\ \to0\ \text{未达}）✓✓$$
$$\qquad \Longrightarrow \textbf{这是"}\textbf{可满足 `F5`}\text{"的}\ \textbf{唯一一例};\ \text{其失败已转移到}\ \textbf{定量天花板} \text{—— 而天花板是}\ \textbf{定量对象}，\ \text{理论上可由更好的证书／屏障移动}✓✓$$
$$\qquad ⚠️\ \text{但 `C-115` 已判定：}\Lambda\le0\ \textbf{与 RH 同墙};\ \text{故此为}\ \text{诊断细化}，\ \textbf{不改闭合}✓$$

## §5 边界与回查

- ⚠️ 本档**未造出**被认可的对象；产出＝**三条件规格 ＋ 一次诊断修正** ✓
- ⚠️ 候选 A 的"经典等价"（欧拉积收敛域 ⟺ 无零点域）**依记忆**⟹ 标 `[经典·本档未逐字核]`✓
- ⚠️ 候选 C 的"部分和零点不收敛到 ζ 零点"**依记忆**⟹ 标 `[待核]`✓
- ⚠️ §3 三条规格为**门序反推**（本档做法），\ \textbf{非定理}；且"三个候选各缺一条"为**构造性观察**，非穷尽性主张 ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:0x）`[纪律]`（先跑后写）

```
技术词 构造尝试          命中文件数=13 :: ./C110-… ./R-CS-PRE1-… 等（**已有**）
技术词 门序反推          命中文件数=1  :: ./CREATE-SPEC-1-…（本档）
技术词 保测试性的算术变形    命中文件数=1  :: ./CREATE-SPEC-1-…（本档）
```
**读数（按实测）**：`门序反推`／`保测试性的算术变形`＝**1 档（仅本档）⟹ 本档新增** ✓；⚠️ `构造尝试`＝**13 档**（**已有**）⟹ 本档为**沿用** ✓
