已查地图：**命中且决定性**（所查档：`CLOSED-ROUTES-MAP.md:1496`（char-$p$ 对照与不可移植性 §4）、`V227-ARS-root-spectrum-audit-realpart-not-modulus-invariant.md`（**命题 V227-A，定理级**）、`V226`／`V227`、`F1-1-absolute-geometry-elementhood-analysis.md`、`ATTACK-PnQ-disjointness.md`、`MASTER-NOGO-AND-LIVE-PATHS.md`（L2／L3）、`D-GRAM-3`、`NEXT-ROUND-nonGram-*`、`MATH-STATEMENTS`、`AUDIT-WALLS-AND-DIFFICULTIES-20260917.md`（G18／G10／M1–M7））。**结论**：模板的形状可分解为**四件**；char $p$ 成功的**引擎是第 3 件（模长钉定）**，而 `V227-A` 证明**模长钉定对 $\beta$ 结构性无效** ⟹ **用模板形状 ⟹ 必须替换第 3 件** ⟹ "创建新算术"的**唯一内容**＝**一个 canonical 的实部钉定机制**（另三件为配套）

# C-68 · **规格**：用 char-$p$ 模板的形状造新算术 —— 4 交付物 ＋ 8 过滤器 ＋ 一处规格内部冲突

> **时间**：2026-09-17 23:48 唐先生指令：**"我们需要用这个唯一完整模板的形状，但是需要创建新的算术，确保复合实例不会塌陷回角 I 或者角 II。"**
> **本档**：把该指令转成**可验收的规格**（不写构想、不给"方向"）✓；**不声称可造** ✗

---

## §0 结论（先行）

$$\text{模板的形状}\ =\ \underbrace{\text{内禀半自同构}}_{(1)\ \text{旋转}}\ +\ \underbrace{\text{canonical 分级}}_{(2)\ \text{升维}}\ +\ \underbrace{\textbf{钉定机制}}_{(3)\ \text{引擎}}\ +\ \underbrace{\text{双向识别}}_{(4)\ \text{涌现}\to\text{构造}}$$
$$\textbf{char }p：\text{临界轨迹}＝\textbf{圆}\ \vert\alpha\vert=\sqrt q\ \text{（**模长**轨迹）}\ \Longrightarrow\ \text{极化＋Hodge 指标**恰好够用**}\ ✓✓$$
$$\textbf{char }0：\text{临界轨迹}＝\textbf{竖直线}\ \Re s=\tfrac12（\textbf{非}模长轨迹）\ \Longrightarrow\ \text{移植}\textbf{结构性失败}$$
$$\qquad ⭐\ \textbf{定理级（`V227-A`）}：\sup_{z\in R}\Re z\ \textbf{不是模长多重集的不变量}\ \Longrightarrow\ \boxed{\text{经典模长钉定机制（极化／Hodge 指标／正性）}\textbf{结构性无法钉定}\ \beta}\ ✓✓✓$$
$$\Longrightarrow\ \boxed{\text{用模板形状的唯一内容}＝\textbf{替换第 3 件};\ \text{所需物}\ ＝\ \textbf{一个 canonical 的"实部钉定机制"（钉点）}}\ ✓✓$$

---

## §1 模板四件套（逐字分解）

| # | char $p$（Weil／Deligne）| char $0$ 的对应物现状 | 依据 |
|:--:|:--|:--|:--|
| **(1) 内禀半自同构**（旋转）| Frobenius $F$，对象**自身**的自同构 | **无** —— char 0 确有闭包（Patterson–Sullivan／Selberg `1/4`／Ramanujan），但承载物皆"几何/群对象＋**内禀流**"，而 **`Spec ℤ` 无内禀流** | `L2` 逐字 |
| **(2) canonical 分级**（升维）| 上同调 $H^i$ ＋ 权重 | 需 canonical 分级（**不依赖测试函数/窗口选择**）；`V211` 类(8) 非交换极限＝显式公式内容 ⟹ 已封 | `V211` §2 |
| **(3) ⭐ 钉定机制**（引擎）| **模长钉定**：$\vert\alpha\vert=\sqrt q$（极化＋Hodge 指标＋Lefschetz）| **需要的是实部钉定**；经典实例**只有 FE**——而 FE **钉轴而非钉点** | `CLOSED-ROUTES-MAP:1496` 逐字 |
| **(4) 双向识别**（涌现→构造）| 零点＝$F$ 的特征值（**定义**关系 ✓）| ζ 的零点是**涌现性**的 ⟹ 需"涌现→构造"的转换 | `V227` §5 逐字；`V215` §5 残余 |

$$\textbf{Selberg 先例的诚实定位（`V227` §5 逐字）}：\text{它成功是因为}\textbf{构造性}（\text{零点由 Laplacian 特征值}\textbf{定义}），\ \text{而}\ \zeta\ \text{的零点是}\textbf{涌现性}\ \text{的} ⟹ \text{ARS 需"涌现→构造"的转换＝}\textbf{识别问题}$$
$$\qquad\Longrightarrow\ \text{第 (4) 件}\ \textbf{不是配套项，而是与第 (3) 件同等承重}\ ✓$$

## §2 两种塌陷的**结构根因**（不是运气）

$$\textbf{角 I（正性）}：\text{`V192` 逐字}：\text{正性给}\textbf{实谱}（\gamma\ \text{侧}），\ \beta\ \text{侧}\textbf{只经重数} \text{进入}\ \Longrightarrow\ \boxed{\textbf{正性根本不是}\ \beta\ \textbf{侧钉定}}\ ✗$$
$$\qquad \text{故任何靠正性的复合}\ \textbf{必} \text{塌回角 I};\ \text{且}\ \text{`POS1` 三分}：\text{sharp 正性}\iff\text{RH}（\text{消失轨迹恰在离临界}）✗$$
$$\textbf{角 II（绕数／坐标型）}：\text{`M4` 逐字}：\textbf{line gap}\Longrightarrow\textbf{Hermitianization}（\text{可经旋转消}）;\ \textbf{point gap}\Longrightarrow\mathbb Z\text{-绕数};\ \textbf{"线只在旋转下定义"}\ ✓✓$$
$$\qquad \Longrightarrow\ \text{任何}\textbf{坐标型} \text{判据必可被旋转吸收} \Longrightarrow \text{塌回角 I}\ ✗$$

## §3 **规格**：4 交付物 ＋ 8 过滤器

$$\textbf{交付（缺一不可）}：$$
$$D1\ \text{一个}\ \textbf{内禀半自同构}（\text{作用于}\ \textbf{对象自身}，\ \textbf{非} \text{坐标变换}）✓$$
$$D2\ \text{一个}\ \textbf{canonical 分级}（\text{不依赖窗/测试函数}）✓$$
$$D3\ ⭐\ \text{一个}\ \textbf{canonical 实部钉定机制}（\textbf{钉点}，\ \textbf{非模长型}，\ \textbf{非 FE}）✓✓$$
$$D4\ \text{一个}\ \textbf{双向识别}（\text{涌现}\to\text{构造}，\ \text{非单向编码}）✓$$

$$\textbf{过滤器（任一违反 ⟹ 立即判死，不进入下一轮）}：$$

| # | 过滤器 | 判据来源 |
|:--:|:--|:--|
| **F1** | **非正性型**（否则塌回角 I）| `V192`（正性只钉 $\gamma$ 侧）＋ `POS1` 第三行 ⟺ RH |
| **F2** | **非坐标型／非绕数型**（否则塌回角 II）| `M4` line gap⟹Hermitianization；"线只在旋转下定义" |
| **F3** | **钉点不钉轴**（否则＝FE，**只钉轴**）| `CLOSED-ROUTES-MAP:1496` |
| **F4** | **非模长型** | ⭐ `V227-A`（定理级）：$\sup\Re$ **不是**模长不变量 |
| **F5** | **含独立算术输入**（不与 RH 等价）| 6 次同址收敛（`C-30/31/32`、`C-61`§2C、`C-64/65`）|
| **F6** | **对算术见证盲** ⟹ 只能解析型 | `V150` W2（经 `V211` §6 S3）|
| **F7** | **过 Epstein 测试**（ζ 特有；FE＋Euler 积不充分）| `V219`／D1 反例 |
| **F8** | **过污染测试 ＋ 压力测试**（$P_N(z)=\sum_{n\le N}a_nz^n$ 型直接淘汰；$z^n-a$ ⟹ 根定位本身不产生 $\tfrac12$）| `V227` §4(5)(7) |

## §4 ⚠️ **一处规格内部冲突**（须唐先生裁决）

$$`F1\text{-}1`\ \text{逐字}：\text{【排除】升维到绝对几何／}F_1\ \text{以获取 canonical 元素与模长};\ \text{【保留】}\boxed{\text{唯一未被排除的升维作用＝提供一个}\textbf{正性可证}\text{的框架}}✓$$
$$\qquad\Longrightarrow\ \text{而}\ \textbf{F1}\ \text{要求"非正性"}\ ⟹\ \textbf{两条直接相撞}\ ⚠️$$
$$\textbf{唯一的两条出路（二选一）}：$$
$$\qquad \textbf{(i)}\ \textbf{正性但非 Weil 型}＝\text{`L3`（Q3：独立全局}\ \sqrt{\cdot}\text{-尺度正性）}：\text{否决判据逐字：}\text{"若正性来源可归入}\ \{\text{有限性},\ \text{Weil},\ \text{零点侧} L^2\}\ \text{或 height/log 型} \Longrightarrow \text{关闭}"✓$$
$$\qquad \textbf{(ii)}\ \textbf{非正性但零敏感}：＝\text{第四类不变量}／D\text{-GRAM 的}\ \textbf{(ZS)}：\text{"由显式公式可证}\ n_-\ge\#\{\text{window 内 off-line pairs}\}"✓$$
$$\Longrightarrow\ \text{无论走哪条，}\ \textbf{第 (4) 件双向识别}\ \text{都不可省}（\text{否则单向编码 ⟹ 归}\ V181）✓✓$$

## §5 三个候选形态 ＋ 各自**已登记杀手**

| 形态 | 内容 | 已登记杀手 |
|:--|:--|:--|
| **(甲) Deninger 型** | 上同调＋**内禀流**，供给规范化极化 | 缺 **canonical polarization**（`V145`）；`M6`：**Buium 同杀**（`G10`）、`ESC2` no common carrier、G9 尺度失败 |
| **(乙) ARS 根定位型** ⭐ | $X\to P_X\to\operatorname{Root}(P_X)\to\beta_X=\sup\Re$（**目前唯一通过形式逃逸的类**）| 杀手：**污染测试**（$P_N$ 型淘汰）、**压力测试**（$z^n-a$）、`ARS1`–`ARS6`；**且 ARS 自身所需＝一个"实部钉定机制"**（与 §3-D3 **同一物**）✓ |
| **(丙) canonical sign 接口** | 把 $U(1)$ phase 变成 canonical sign；**相位本体是 $U(1)$-torsor，无 canonical 基点** | 你自己定的**八条禁用**（取绝对值／取实部／averaging／character projection／人为 orientation／Hilbert 完备化／trace／现成 Weil positivity）|

$$\Longrightarrow\ \boxed{\text{三条路的交汇点＝}\textbf{同一个物}：\text{canonical 实部钉定机制（D3）＋双向识别（D4）}}✓✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 23:5x）`[纪律]`

```
技术词 实部钉定机制  命中文件数=3    :: ./V227-ARS-root-spectrum-audit-realpart-not-modulus-invariant.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md
技术词 内禀半自同构  命中文件数=0    ::
技术词 塌陷判据     命中文件数=0    ::
技术词 钉点而非轴  命中文件数=0    ::
```
**读数**：`内禀半自同构`／`塌陷判据`／`钉点而非轴`＝**0 档 ⟹ 本档新增** ✓；⚠️ `实部钉定机制`＝**3 档 ⟹ 档案已有**（`V227` 已命名）⟹ §3-D3 为**引用＋规格化**，**不列为本档提出** ✓

## §7 边界

- `[逐字]` §0–§2 的 char $p$ 对照、`V227-A`、`V192`、`M4`、`F1-1`、`L2`、`L3` 否决判据均**逐字引用** ✓
- `[本档]` §1 四件套分解、§2 塌陷根因的形式化、§3 规格（4＋8）、§4 冲突与两条出路、§5 交汇点 ✓
- **不声称**：新算术可造 ✗；ARS 存在 ✗；不判定任何候选 ALIVE／DEAD ✓；不证 RH ✗；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 指令（唐先生 23:48）：用唯一完整模板（char p）的形状，创建新算术，确保不塌回角 I／角 II
⚠️ 闸门命中（决定性）：CLOSED-ROUTES-MAP:1496 + V227（命题 V227-A 定理级）
⚠️ 核心读数：模板＝(1)内禀半自同构(旋转) + (2)canonical 分级(升维) + (3)钉定机制(引擎) + (4)双向识别
   char p 引擎＝模长钉定（极化/Hodge 指标）✓；char 0 临界轨迹是竖直线 ⟹ V227-A：sup Re 不是模长不变量
   ⟹ 用模板形状 ⟹ 必须替换第 3 件 ⟹ 新算术的唯一内容＝canonical 实部钉定机制（钉点，非模长、非 FE）
⚠️ 两种塌陷的结构根因：角 I＝V192（正性只钉 γ 侧）+POS1（sharp 正性⟺RH）；角 II＝M4（line gap⟹Hermitianization）
⚠️ 规格：4 交付（D1–D4）+ 8 过滤器（F1–F8）
⚠️ 规格内部冲突（须裁决）：F1-1"唯一存活升维形式＝内建正性" vs F1"非正性" ⟹ 二选一：(i) L3（正性但非 Weil 型，带独立算术输入）
   或 (ii) 第四类不变量/（ZS）零敏感非正性；两条都不可省 D4
⚠️ 三候选交汇于同一物：Deninger 型（杀手 G10/ESC2/G9）／ARS 型（杀手 污染+压力+ARS1–6）／canonical sign 接口（杀手 八条禁用）
✅ 净产出：①模板四件套分解 ✓；②塌陷根因形式化 ✓；③规格 4+8 ✓；④规格冲突与两条出路 ✓；⑤三候选交汇点 ✓
```
