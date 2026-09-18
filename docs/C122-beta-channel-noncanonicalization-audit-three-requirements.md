已查地图（所查：`C-121`（`β`-channel 审计；横向＝模长通道；`V254` 唯一开口）、`V254`（横坐标／奇点链条逐字：`\sum_a\mu(a)/(a^c\log a)=\int_c^\infty ds/\zeta(s)`；奇点＝`\zeta` 零点；`\sigma_c\ge\beta_*`；**反向需独立证明**；无条件阈值 `=1`）、`V253`（`\sigma=\tfrac12` 同形状版**不存在**）、`C-72`（密度链条：`A\Longrightarrow` 无零区域；`A\to0\Longrightarrow` 近 RH；**输入 `support\le1`**）、`TYPE-MATCH`（零密度 ⟺ Dirichlet 多项式大值）、`V255`／`V255-5b`（**parity barrier**；**类型判据**：系数侧→零侧须先构造转换，单类型不可）、`V188` §2（线性饱和）、`FZ-3`（canonical ⟹ `\beta` 盲）、`C-116`（**登记不否决**）、`V215` §5／`V193` §⑤（非典范双向识别界面）。**结论**：逐步审计完成 ⟹ **两条典范链条各恰有**一处 `canonical` 性依赖**与**一处输入限制**：链条 (A) 的 `canonical` 性在 **A4（奇点＝零点 ⟺ 须 Euler 乘性）**、输入限制在 **A6（`\sigma_c` 的上界＝全局抵消）**；链条 (B) 的 `canonical` 性在 **B3（零 ⟹ 大值"检测"步，须 Euler 型局部结构）**、输入限制在 **B7（`A` 的下界＝`support\le1`）**✓✓；⟹ **"非典范化"被形式化为三段要求** **(i) 算术（零-free）定义 ＋ (ii) 横向奇点集＝零点实部集 ＋ (iii) 右端奇点有可证的**上界** ⟹ 而**已知两种满足 (ii) 的方式恰好各违反一者**：**Euler 乘性满足 (i)(ii) 但违反 (iii)**（无条件横坐标 `=1`，推到 `\tfrac12` 就是 RH）；**显式公式满足 (ii)(iii) 但违反 (i)**（用零点）✓✓ ⟹ ⟹ **缺口＝(i)∧(ii)∧(iii) 同时成立**（与 `V254` 逐字"不排除非典范／尚未发明的来源"**同址**，但**要求已被精确定名**）✓✓

# C-122 · **`β`-channel 非典范化审计：(A)(B) 逐步分解 ＋ 三段要求**

> **时间**：2026-09-18 18:16 唐先生：**「开」** ⟹ 对 (A) 横坐标／奇点型、(B) 密度／大值型，逐条审计"哪一步用到了 `canonical` 性、去掉它需要什么"✓

---

## §0 结论（先行）

$$\textbf{链条 (A)}：\text{canonical 性用在}\ \boxed{A4};\ \text{输入限制在}\ \boxed{A6}✓$$
$$\textbf{链条 (B)}：\text{canonical 性用在}\ \boxed{B3};\ \text{输入限制在}\ \boxed{B7}✓$$
$$\textbf{"非典范化"形式化为三段要求}：$$
$$\qquad \textbf{(i)}\ \text{由}\ \textbf{算术数据} \text{定义}（\textbf{不用零点}）✓$$
$$\qquad \textbf{(ii)}\ \text{其}\ \textbf{横向（}\sigma\text{ 方向）奇点集}＝\text{零点实部集}\ \{\operatorname{Re}\rho\}✓$$
$$\qquad \textbf{(iii)}\ \text{右端奇点有}\ \textbf{可证的上界}（\text{不需零点信息}）✓$$
$$\textbf{已知两种满足 (ii) 的方式恰好各违反一者}：$$
$$\qquad \text{Euler 乘性}：\text{满足 (i)(ii)}，\ \textbf{违反 (iii)}（\text{无条件横坐标}\ =1;\ \text{推到}\ \tfrac12\ \textbf{就是 RH}）✓✓$$
$$\qquad \text{显式公式}：\text{满足 (ii)(iii)}，\ \textbf{违反 (i)}（\textbf{用零点}）✓✓$$
$$\Longrightarrow \boxed{\text{缺口}＝\text{(i)}\wedge\text{(ii)}\wedge\text{(iii)}\ \text{同时成立}}✓✓$$
$$\qquad ⚠️\ \text{与}\ \text{`V254`}\ \text{逐字"不排除非典范／尚未发明的来源"}\ \textbf{同址};\ \text{但}\ \textbf{要求已被精确定名}✓$$

---

## §1 链条 (A) 逐步审计：横坐标／奇点型

| 步 | 内容 | 依据 | 依赖类型 |
|:--|:--|:--|:--|
| `A1` | 取带符号算术权 `a_n`（`\mu/\lambda/\chi`／Hecke） | 局部可算 | **算术** ✓（可非典范）|
| `A2` | 造 Dirichlet 级数 `D(s)=\sum a_nn^{-s}`，取收敛横坐标 `\sigma_c` | 标准 | 算术 ✓ |
| `A3` | **Landau／Dirichlet 级数基本定理**：`\sigma_c` ＝右端奇点实部 | 经典 | **一般定理**（非典范无关）✓ |
| **`A4`** | ⭐ **奇点 ＝ `\zeta` 的零点** | `1/\zeta` 的奇点恰为 `\zeta` 的零点 | ⚠️ **须 Euler 乘性** ⟹ **canonical 性在此** ✓✓ |
| `A5` | ⟹ `\sigma_c\ge\beta_*`（**下界**方向） | `A3+A4` | 由 `A4` 继承 |
| **`A6`** | ⭐ 若证 `\sigma_c\le\tfrac12` ⟹ `\beta_*\le\tfrac12` ⟹ RH | `M(x)=O(x^{1/2+\varepsilon})\iff` RH | ⚠️ **须全局抵消** ⟹ **输入限制在此** ✓✓ |

$$\textbf{A4 的关键}：\text{要让奇点}\ \textbf{落在}\ \zeta\ \text{的零点上}，\ \text{级数必须"穿过"}\ \zeta\ \text{——}\ \text{而已知唯一的如此结构}＝\textbf{Euler 乘性}✓$$
$$\qquad ⚠️\ \text{或}\ \textbf{直接把零点当输入}（\text{显式公式}）⟹ \text{违反 (i)}✓$$
$$\textbf{A6 的关键}：\text{对}\ \textbf{乘性} \text{权}，\ \sigma_c\ \text{的上界}\iff\sum_{n\le x}a_n\ \text{的抵消} \iff \text{零点信息}✓✓$$
$$\qquad ⟹ \textbf{canonical 性同时是"指向}\ \beta_*\ \text{"的}\textbf{必要条件} \text{和"能给出上界"的}\textbf{阻碍}✓$$
$$\qquad \qquad ⚠️\ \text{这正是}\ \text{`FZ-3`}\ \text{二分在本通道的}\ \textbf{逐条实现}（\text{本档导出}）✓✓$$

## §2 链条 (B) 逐步审计：密度／大值型

| 步 | 内容 | 依据 | 依赖类型 |
|:--|:--|:--|:--|
| `B1` | `N(\sigma,T)=\#\{\rho:\operatorname{Re}\rho>\sigma,|\operatorname{Im}\rho|\le T\}`＝横向计数对象 | 定义 | **算术侧不可直接算**（定义用零点）⚠️ |
| `B2` | 与显式公式／RvM 挂钩 | 经典 | 用零点（⇒ 检测侧）|
| **`B3`** | ⭐ **零 ⟹ Dirichlet 多项式取大值**（"检测"步） | `TYPE-MATCH`（零密度 ⟺ 大值） | ⚠️ **须 Euler 型局部结构** ⟹ **canonical 性在此** ✓✓ |
| `B4` | 密度指数 `A`：`N(\sigma,T)\ll T^{A(1-\sigma)+o(1)}` | Ingham／Huxley；近年 `A=30/13`（Guth–Maynard） | 无条件（在 `support\le1` 内）|
| `B5` | `A\Longrightarrow` 无零区域 `\sigma>1-\frac{c}{A\log T}` | 标准转换 | ✓ |
| `B6` | `A\to0\Longrightarrow` 近 RH ⟹ **障碍＝`A` 的下界** | 等价链 | — |
| **`B7`** | ⭐ `A` 的下界由 **输入 `support\le1`** 决定 | `C-72` ｜ `SUPPORT-1` | ⚠️ **输入限制在此** ✓✓ |

$$\textbf{B3 的关键}：\text{"检测"＝从}\ \textbf{算术系数} \text{造出大值的 Dirichlet 多项式} \Longrightarrow \text{须}\ \textbf{局部（Euler）结构}✓$$
$$\qquad ⚠️\ \text{去掉它}（\text{非 Euler 检测器}）⟹ \textbf{parity barrier}（\text{`V255`／`V255-5b`}）;\ \text{且}\ \text{`V255-5b` 类型判据}：\text{系数侧}\to\text{零侧}\ \textbf{须先构造转换}，\ \text{单类型}\ \textbf{不可能}✓✓$$
$$\textbf{B7 的关键}：\text{无条件信息只到}\ support\le1 \Longrightarrow A\ \text{有}\ \textbf{正下界} \Longrightarrow \text{推不过去}✓$$
$$\qquad ⚠️\ \text{且}\ \text{`C-90`}\ \text{已实测：该处}\ \textbf{曲率／横截性} \text{假设}\ \textbf{不满足}（\text{二阶差分符号 50/50}）✓$$

## §3 合并：三段要求与两种已知实现

$$\textbf{要求 (i)}\ \text{算术（零-free）定义};\quad \textbf{(ii)}\ \text{横向奇点＝}\{\operatorname{Re}\rho\};\quad \textbf{(iii)}\ \text{右端奇点有可证上界}✓$$

| 实现 | (i) 零-free | (ii) 奇点＝零点实部 | (iii) 上界可证 | 结论 |
|:--|:--:|:--:|:--:|:--|
| **Euler 乘性**（`1/\zeta`、`\zeta'/\zeta` 等）| ✓ | ✓ | ✗（无条件 `=1`；到 `\tfrac12` ⟺ RH）| 满足 2/3 |
| **显式公式**（零点作输入）| ✗ | ✓ | ✓ | 满足 2/3 |
| **(i)∧(ii)∧(iii) 同时** | — | — | — | ⭐ **缺口（0 例）** |

$$\Longrightarrow \boxed{\text{缺口被精确定名}：\text{一个}\ \textbf{零-free 的算术构造}，\text{其横向奇点}\ \textbf{恰为} \text{零点实部}，\ \text{且右端奇点}\ \textbf{有可证上界}}✓✓$$
$$\qquad \text{为什么难}：\text{(ii) 要求"与}\ \zeta\ \text{绑定"，而已知绑定只有}\ \textbf{两条}：\text{Euler（乘性）};\ \text{显式公式（用零点）}✓$$
$$\qquad \qquad ⚠️\ \text{这是}\ \textbf{归纳级} \text{陈述（"已知只有两条"）};\ \text{按}\ \text{`C-116`}\ \textbf{登记不否决}✓$$

## §4 与档案残余的对接

$$\text{本档缺口} \equiv \text{`V254` 开口（非典范／尚未发明）} \equiv \text{`V215` §5 非典范双向识别界面} \equiv \text{`V193` §⑤ 残余}✓$$
$$\qquad \equiv \text{`C-110`}\ \text{的}\ \text{`C1`}（\text{非 canonical}）\cap\text{`C6`}（\text{定量稳定性}）✓$$
$$\text{但本档新增}：\textbf{三段要求 (i)(ii)(iii) 的逐条形式} ＋ \textbf{两张逐步审计表}（`A1`–`A6`／`B1`–`B7`）✓✓$$
$$\qquad \Longrightarrow \text{今后任何}\ \beta\ \text{通道候选}\ \textbf{可直接按这三条打分}（\text{比"是否非典范"更可操作}）✓$$

## §5 边界与回查

- ⚠️ **不否决**（`C-116`）："已知只有两条绑定"是归纳级；本档**不**声称 (i)∧(ii)∧(iii) 不可能 ✓
- ⚠️ `B1` 一行：`N(\sigma,T)` 的**定义**用零点，但其**估计**（`B4`）是无条件的 ⟹ 该行标"算术侧不可直接算"是**准确定位**，非判死 ✓
- **不声称**：缺口已被填 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:2x）`[纪律]`（先跑后写）

```
技术词 三段要求         命中文件数=1  :: ./C122-beta-channel-noncanonicalization-audit-three-requirements.md
技术词 非典范化审计       命中文件数=1  :: ./C122-beta-channel-noncanonicalization-audit-three-requirements.md
技术词 绑定只有两条       命中文件数=1  :: ./C122-beta-channel-noncanonicalization-audit-three-requirements.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 18:16「开」⟹ 对 (A) 横坐标/奇点型、(B) 密度/大值型 逐步审计"哪一步用到 canonical 性、去掉需要什么"
⭐ 链条 (A) 逐步: A1 取带符号算术权(算术 ✓ 可非典范); A2 造 Dirichlet 级数取收敛横坐标 σc; A3 Landau: σc = 右端奇点实部(一般定理);
   **A4 ⭐ 奇点 = ζ 的零点 —— 须 Euler 乘性 ⟹ canonical 性在此**; A5 ⟹ σc ≥ β*(下界方向); **A6 ⭐ 若证 σc ≤ ½ ⟹ RH —— 须全局抵消
   (M(x)=O(x^{1/2+ε}) ⟺ RH) ⟹ 输入限制在此**
   ⟹ A4 关键: 要让奇点落在 ζ 的零点上, 级数必须"穿过"ζ —— 已知唯一如此结构=Euler 乘性(或直接把零点当输入 ⟹ 违反 (i))
      A6 关键: 对乘性权, σc 的上界 ⟺ Σ_{n≤x} a_n 的抵消 ⟺ 零点信息
   ⟹ **canonical 性同时是"指向 β*"的必要条件和"能给出上界"的阻碍** = **FZ-3 二分在本通道的逐条实现(本档导出)**
⭐ 链条 (B) 逐步: B1 N(σ,T) 横向计数对象(定义用零点); B2 与显式公式/RvM 挂钩; **B3 ⭐ 零 ⟹ Dirichlet 多项式取大值(检测步)
   —— 须 Euler 型局部结构 ⟹ canonical 性在此**(TYPE-MATCH); B4 密度指数 A(30/13, Guth–Maynard); B5 A ⟹ 无零区域 σ>1−c/(A log T);
   B6 A→0 ⟹ 近 RH ⟹ 障碍 = A 的下界; **B7 ⭐ A 的下界由输入 support ≤ 1 决定 ⟹ 输入限制在此**
   ⟹ B3 关键: 去掉 Euler 结构(非 Euler 检测器) ⟹ parity barrier(V255/V255-5b: 系数侧→零侧须先构造转换, 单类型不可能)
      B7 关键: 无条件信息只到 support ≤ 1 ⟹ A 有正下界; 且 C-90 已实测该处曲率/横截性假设不满足(二阶差分符号 50/50)
⭐ **"非典范化"形式化为三段要求**: (i) 算术(零-free)定义 (ii) 横向奇点集 = 零点实部集 (iii) 右端奇点有可证上界
   表: Euler 乘性 → (i)✓ (ii)✓ (iii)✗(无条件=1, 到 ½ ⟺ RH) 满足 2/3; 显式公式 → (i)✗ (ii)✓ (iii)✓ 满足 2/3;
   **(i)∧(ii)∧(iii) 同时 = 缺口(0 例)**
   ⟹ 缺口精确定名: "一个零-free 的算术构造, 其横向奇点恰为零点实部, 且右端奇点有可证上界"
   为什么难: (ii) 要求"与 ζ 绑定", 而已知绑定只有两条: Euler(乘性) / 显式公式(用零点); ⚠️ 这是**归纳级**陈述 ⟹ 按 C-116 登记不否决
⭐ 与档案残余同址: ≡ V254 开口 ≡ V215 §5 ≡ V193 §⑤ ≡ C-110 的 C1∩C6; 但新增**三段要求的逐条形式 + 两张逐步审计表(A1–A6/B1–B7)**
   ⟹ 今后任何 β 通道候选可直接按三条打分(比"是否非典范"更可操作)
⚠️ 不否决: "已知只有两条绑定"为归纳级; 不声称 (i)∧(ii)∧(iii) 不可能; B1 的"算术侧不可直接算"是准确定位非判死; 不证 RH
✅ 净产出: ①链条 A 逐步审计表(6 步, 定位 A4/A6) ②链条 B 逐步审计表(7 步, 定位 B3/B7) ③三段要求 (i)(ii)(iii) + 两实现对比表 ⟹ 缺口精确定名 ④FZ-3 二分在该通道的逐条实现(本档导出)
```
