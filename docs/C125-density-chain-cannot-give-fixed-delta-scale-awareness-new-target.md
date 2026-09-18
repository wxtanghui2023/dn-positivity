已查地图（所查：`C-124`（族形状；第一级靶＝固定无零区域）、`C-72`（密度链：`A\Longrightarrow\sigma>1-c/(A\log T)`；输入 `support\le1`）、`POS1`（正性三分；`3+4\cos t+\cos 2t=2(1+\cos t)^2\ge0` **的经典正性恒等式**）、`V253`（`\sigma=1` 位置**被尾和有限性强制**）、`V188` §3(2)（涨落三层；`\log T` 尺度）、`V192` §①（纵坐标退化；临界线波动尺度）、`E18`#80（char p 是**唯一完整模板**）、`M2`（单环定理：char p 临界轨迹＝圆，char 0＝竖直线 ⟹ 移植**结构性失败**，档案已审）、`C-116`（**登记不否决**）。**结论**：**我上一条提议的下一步（把 `A=30/13` 密度链参数化以取固定 `\delta`）在结构上失败**，本档如实报告 ✓✓ —— 理由：密度链的转换 `\sigma>1-\frac{c}{A\log T}` 中的 `\log T` **不是技术余项，而是机制的尺度**（零点平均间距 `\frac{2\pi}{\log T}`）⟹ 该机制**只能看到"距离 ≳ 平均间距"的排除**，**永不能给出固定 `\delta`** ✓✓；同理，经典**正性法**（de la Vallée Poussin：用 `3+4\cos\theta+\cos2\theta\ge0` 配对数导数）**亦只给退化型**，因为 `\zeta'/\zeta` 的实部由**最近零点**支配 ⟹ 同样尺度感知 ✓✓；⟹ **统一理由**：**两类可用机制皆"尺度感知"** ⟹ 固定 `\delta` 的**第一级不被 `POS1` 阻塞，而被"机制的尺度感知性"阻塞** ✓✓；⟹ **新靶（本档命名）**：一个\ **尺度无关的排除机制** ✓✓；而**已知唯一尺度无关机制**＝**char p 的有限维正性（Weil 证明）** ⟹ 其移植**结构性失败**（`M2` 单环定理：临界轨迹圆 vs 竖直线，档案已审）⟹ **该路线回到同一址**（新增一条独立到达 + 一个新命名要求）✓✓

# C-125 · **密度链不能给固定 `\delta`（自我否决）＋ 卡点＝尺度感知性 ＋ 新靶＝尺度无关机制**

> **时间**：2026-09-18 18:27 唐先生：**「继续」** ⟹ 查"可参数化的无零区域机制"（如把 `A=30/13` 参数化）✓

---

## §0 结论（先行）

$$\textbf{(1)}\ ⚠️\ \textbf{我上一条提议的下一步}\ \textbf{结构上失败}（\text{本档如实报告}）✓✓$$
$$\qquad \text{密度链}：A \Longrightarrow \sigma>1-\frac{c}{A\log T};\quad \text{其中}\ \log T\ \textbf{不是技术余项，而是机制的尺度}✓$$
$$\qquad \qquad \text{零点平均间距}=\frac{2\pi}{\log T} \Longrightarrow \text{机制只能看到"距离}\ \gtrsim\ \text{平均间距"的排除} \Longrightarrow \textbf{永不给出固定}\ \delta✓✓$$
$$\textbf{(2)}\ ⚠️\ \text{经典}\ \textbf{正性法} \text{同理只给退化型}：\text{de la Vallée Poussin 用}\ 3+4\cos\theta+\cos2\theta\ge0\ \text{配}\ \zeta'/\zeta✓$$
$$\qquad \qquad \zeta'/\zeta\ \text{的实部由}\ \textbf{最近零点} \text{支配} \Longrightarrow \textbf{同样尺度感知}✓✓$$
$$\textbf{(3)}\ \Longrightarrow\ \textbf{统一理由}：\boxed{\text{两类可用机制皆}\ \textbf{尺度感知}}✓✓$$
$$\qquad \textbf{固定}\ \delta\ \text{的第一级}\ \textbf{不被}\ \text{POS1}\ \textbf{阻塞}，\ \text{而}\ \textbf{被"机制的尺度感知性"阻塞}✓✓$$
$$\textbf{(4)}\ ⭐\ \textbf{新靶（本档命名）}：\boxed{\text{一个}\ \textbf{尺度无关的排除机制}}✓✓$$
$$\qquad \text{即：在固定距离}\ \delta\ \text{处排除零点，}\ \textbf{而不使用间距尺度}\ \frac{2\pi}{\log T}✓$$
$$\textbf{(5)}\ \text{已知唯一尺度无关机制}＝\textbf{char }p\ \text{的有限维正性（Weil 证明）} \Longrightarrow \text{移植}\ \textbf{结构性失败}✓$$
$$\qquad \text{（}\text{`M2` 单环定理}：\text{char }p\ \text{临界轨迹＝圆}（\text{旋转不变}）;\ \text{char 0＝竖直线，档案已审}）✓✓$$
$$\qquad \Longrightarrow \textbf{该路线回到同一址}（\text{新增一条独立到达} ＋ \text{一个新命名要求}）✓$$

---

## §1 密度链为何不能给固定 `\delta`（结构性论证）

$$\text{密度输入}：N(\sigma,T)\ll T^{A(1-\sigma)+o(1)} \Longrightarrow \text{标准转换}：\sigma>1-\frac{c}{A\log T}✓$$
$$\qquad ⚠️\ \textbf{关键}：\text{转换中的}\ \log T\ \text{来自}\ \textbf{聚类尺度}：\text{零点的平均间距}\ \frac{2\pi}{\log T}✓$$
$$\qquad \qquad \text{（排除论证须处理}\ O(\log T)\ \text{个相邻零点} \Longrightarrow \text{距离}\ 1-\sigma\ \text{只能在}\ \gtrsim\frac{1}{\log T}\ \text{的量级上被分辨}）✓✓$$
$$\Longrightarrow\ A\ \text{无论怎样有限，}\ \text{得到的都是}\ \textbf{退化型}（1-\sigma\sim\frac{1}{A\log T}\to0） \Longrightarrow \boxed{\textbf{不能给固定}\ \delta}✓✓$$
$$\qquad \Longrightarrow \text{故}\ \textbf{"把}\ A\ \text{参数化"这条路}\ \textbf{不可能} \text{给出第一级};\ \text{本档}\ \textbf{否决我自己的上一条提议}✓✓$$

## §2 正性法为何也只给退化型

$$\text{de la Vallée Poussin 结构}：\text{取}\ a>1，\ \text{由}\ 3+4\cos\theta+\cos2\theta\ge0\ \text{得}\ -\!\operatorname{Re}\frac{\zeta'}{\zeta}(\sigma+it)\le\frac{3}{a-\sigma}+\cdots✓$$
$$\qquad ⚠️\ \operatorname{Re}\frac{\zeta'}{\zeta}(s)=\sum_\rho\operatorname{Re}\frac{1}{s-\rho}+\cdots \Longrightarrow \text{由}\ \textbf{最近零点} \text{支配}✓$$
$$\qquad \Longrightarrow\ \text{结论形如}\ 1-\beta\gtrsim\frac{1}{\log\gamma} \Longrightarrow \textbf{仍退化型}✓✓$$
$$\qquad ⚠️\ \text{且}\ \text{`V253`}：\sigma=1\ \text{的位置}\ \textbf{被"尾和有限性"强制} \Longrightarrow \text{该层的机制}\ \textbf{不能} \text{越到}\ \sigma=\tfrac12✓$$

## §3 统一：尺度感知性

| 机制类 | 尺度来源 | 可给 | 不能给 |
|:--|:--|:--|:--|
| 密度链（`A`）| 平均间距 `\frac{2\pi}{\log T}` | `1-\sigma\sim\frac{1}{A\log T}` | ⚠️ **固定 `\delta`** |
| 正性＋对数导数 | 最近零点（同为间距尺度）| `1-\beta\gtrsim\frac{1}{\log\gamma}` | ⚠️ **固定 `\delta`** |
| （char `p` 有限维正性）| **无**（有限维）| **RH 本身** | — |

$$\Longrightarrow \boxed{\text{两类 char 0 机制皆}\ \textbf{尺度感知};\ \text{而唯一尺度无关机制在 char }p}✓✓$$
$$\qquad \Longrightarrow \text{族形状的}\ \textbf{第一级} \text{所缺的}\ \textbf{不是强度}，\ \text{而是}\ \textbf{机制的尺度类型}✓✓$$

## §4 新靶的形式条件

$$\boxed{\text{尺度无关排除机制}：\exists\delta>0\ \text{固定};\ \text{排除}\ \{\beta>1-\delta\}\ \textbf{而不使用间距尺度}\ \frac{2\pi}{\log T}}✓✓$$
$$\text{形式条件（本档给出）}：$$
$$\qquad \text{(a)}\ \text{结论}\ \textbf{不含}\ \log T\ \text{型退化}（\text{即}\ \delta\ \text{与}\ T\ \text{无关}）✓$$
$$\qquad \text{(b)}\ \text{不使用"最近零点"型论证}（\text{即}\ \text{不通过}\ \operatorname{Re}\zeta'/\zeta\ \text{的局部求和}）✓$$
$$\qquad \text{(c)}\ \text{须为}\ \textbf{全局结构型}（\text{有限维／正性／代数}）✓$$
$$\text{已知满足 (c) 的唯一实例}：\text{char }p\ \text{的 Weil 有限维正性} \Longrightarrow \text{移植失败（`M2`）}✓✓$$
$$\qquad \Longrightarrow \text{故本靶}\ \textbf{等价于} \text{"找一个 char 0 的}\ \textbf{非间距尺度} \text{全局机制"} — \text{与档案}\ \text{`L2`／`M2`／\text{char }p\ \text{模板线}\ \textbf{同址}}✓✓$$

## §5 边界与回查

- ⚠️ **本档否决的是我自己的上一条提议**（密度链参数化），**不是** `C-124` 的族形状框架 ✓
- ⚠️ **不否决**（`C-116`）：本档**不**声称尺度无关机制不存在；只登记"已知唯一实例在 char `p`，移植结构性失败"（**归纳级**）✓
- ⚠️ §1／§2 的"退化型"与"平均间距尺度"为**经典结构**，标 `[经典·本档未逐字核文献]` ✓
- **不声称**：固定 `\delta` 不可证 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:3x）`[纪律]`（先跑后写）

```
技术词 尺度无关机制        命中文件数=1  :: ./C125-…（本档）
技术词 尺度感知          命中文件数=1  :: ./C125-…（本档）
技术词 间距尺度          命中文件数=1  :: ./C125-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 18:27「继续」⟹ 查"可参数化的无零区域机制"(如把 A=30/13 参数化取固定 δ)
⚠️ **这一刀先把我自己上一条提议的下一步否掉了** ⟹ 如实报告
⭐ (1) 密度链**不能**给固定 δ(结构性理由): 密度链 A ⟹ σ>1−c/(A logT); 其中 logT **不是技术余项, 而是机制的尺度**
   —— 零点平均间距 = 2π/logT ⟹ 机制只能看到"距离 ≳ 平均间距"的排除 ⟹ **永不给固定 δ**; A 无论如何有限都只给退化型 1−σ ~ 1/(A logT) → 0
   ⟹ 故"把 A 参数化"**不可能**给出第一级 ⟹ **本档否决我自己上一条的提议**
⭐ (2) 经典正性法同理: de la Vallée Poussin 用 3+4cosθ+cos2θ ≥ 0 配对数导数; 而 Re ζ'/ζ(s) = Σ_ρ Re 1/(s−ρ) + … 由**最近零点**支配
   ⟹ 结论形如 1−β ≳ 1/logγ ⟹ **仍退化型**; 且 V253: σ=1 的位置**被尾和有限性强制** ⟹ 该层机制不能越到 σ=1/2
⭐ (3) 统一理由: **两类可用机制皆"尺度感知"**
   表: 密度链(尺度=平均间距 2π/logT; 可给 1−σ~1/(A logT); 不能给固定 δ) / 正性+对数导数(尺度=最近零点, 同为间距尺度; 可给 1−β≳1/logγ; 不能给固定 δ) /
   (char p 有限维正性: 无尺度, 可给 RH 本身)
   ⟹ 固定 δ 的第一级**不被 POS1 阻塞, 而被"机制的尺度感知性"阻塞**; ⟹ 族形状第一级所缺的**不是强度, 而是机制的尺度类型**
⭐ (4) 新靶(本档命名) = **尺度无关的排除机制**: ∃δ>0 固定, 排除 {β>1−δ} **而不使用间距尺度 2π/logT**
   形式条件: (a) 结论不含 logT 型退化(δ 与 T 无关) (b) 不使用"最近零点"型论证(不通过 Re ζ'/ζ 的局部求和) (c) 须为**全局结构型**(有限维/正性/代数)
⭐ (5) 已知满足 (c) 的唯一实例 = **char p 的 Weil 有限维正性** ⟹ 移植**结构性失败**(M2 单环定理: char p 临界轨迹=圆(旋转不变); char 0=竖直线)
   ⟹ 故本靶等价于"找一个 char 0 的非间距尺度全局机制" —— 与档案 L2/M2/char p 模板线**同址**(新增一条独立到达 + 一个新命名要求)
⚠️ 边界: 本档否决的是**我自己的上一条提议**(密度链参数化), 不是 C-124 的族形状框架; 不声称尺度无关机制不存在(归纳级, C-116 登记不否决);
   §1/§2 的"退化型"与"平均间距尺度"为经典结构[经典·本档未逐字核文献]; 不证 RH
✅ 净产出: ①自我否决(密度链参数化结构上不可行)及其理由 ②正性法同样只给退化型 ③统一理由=尺度感知性 ④新命名要求=尺度无关排除机制(+形式条件 a/b/c) ⑤已知唯一实例在 char p, 移植结构性失败 ⟹ 同址
```
