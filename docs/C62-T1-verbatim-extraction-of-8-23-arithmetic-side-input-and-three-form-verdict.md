已查地图：**逐档核对**（所查档：`contradiction-reductio-boundary.md`、`contradiction-forms-launch.md`（候选 E）、`2026-08-23-full-archive.md`、`APPRECIATION-AUDIT-2026-09-11.md`（S1【第一步】）、`E30-2-T2-mechanism.md`、`CONV1-li-conversion-assembled.md`、`DUP-ALERT-route2-obstacle-is-already-registered-T2-law.md`、`RIGORIZATION-finitely-many-off-axis-reductio-boundary.md`（C-46 §4/§5/E4）、`PAPER-v1-li-explicit-range.md`）。**结论：8/23「指数 vs 多项式」所用的"算术侧界"已逐字取出；其档案状态为「需证」，且比较**只在 `n ≤ cT₀²` 窗口内**成立 ⟹ 对"无穷多离轴"（高度无界）**永不适用** ⟹ 第二环不是"未复证"，而是**按现有输入不可达** ✗

# C-62 · **T1 执行**：逐字取出 8/23「指数 vs 多项式」的算术侧界 ＋ 三态判定

> **时间**：2026-09-17 21:29 唐先生「继续」⟹ 执行 `C-61` §3 的 **T1**（我建议的最低风险、可判定微任务）。
> **本档任务**：**只取出并判定那一步的输入**；不给新路线、不改原档 ✓

---

## §0 T1 结论（先行）

$$\boxed{\text{"多项式" }=\text{ 在线主项 }\tfrac12 n\log n;\quad\text{"指数" }=\text{ 离轴项 }-\tfrac{n}{2\gamma^2}e^{n/(2\gamma^2)};\quad\text{比较}\ \textbf{只在}\ n\le cT_0^2\ \textbf{窗口内成立}}$$
$$\boxed{\Longrightarrow\ \text{对"无穷多离轴"（}\gamma_j\to\infty\ \Longrightarrow\ n_j\approx\gamma_j^2/\delta\to\infty\text{）}\ \textbf{该比较永不适用}\ \Longrightarrow\ \text{8/23 第二环}\ \textbf{按现有输入不可达}\ ✗}$$
**修正 `C-61` §2(A)**：由「`[档案声称／本档未复证]`」**升级**为「**`[档案声称／现有输入不可达]`**」（**仍不断言其为假** ✗）

---

## §1 逐字取出（四处出处，均核对）

**(a) 命题所在**（`contradiction-reductio-boundary.md` 逐字）：
> 「**无穷多离轴 ⟹ 矛盾（无条件——）**：**指数 vs 多项式**（$\lambda_n$ 已知增长——）——排除无穷多 ✓」

**(b) ⭐ 输入所在**（`APPRECIATION-AUDIT-2026-09-11.md` S1【第一步】逐字）：
> 「用 **B–L 分解 + 阈值律** 重算：**需证 "离轴零点的贡献 $\ge-(n/(2\gamma^2))e^{n/(2\gamma^2)}$" 与"在线主项 $\ge\tfrac12n\log n-\dots$"的比较在 $n\le cT_0^2$ 时统一成立 ⟹ 求出最优 $c$ ✓」

**(c) 量级所在**（`E30-2-T2-mechanism.md` 逐字）：
> 「· $\lambda_n$ 的量级：$n\log n$（线性×对数 ✓）／· **平方来自【恒等式里 $\gamma$ 的平方】**，不是来自 $\lambda_n$ 的量级」

**(d) 在册引用**（`CONV1-li-conversion-assembled.md` §1 逐字）：
> 「Li 判据（$\lambda_n\ge0\ \forall n\iff$ RH）我们在册且深入研究过 ✓（$\lambda_n$、Maślanka、矩、$r(n)=\lambda_n-\tfrac12n\log n-cn$ ✓）」

$$\Longrightarrow\ \textbf{取出结果}：\text{"算术侧输入"}=\boxed{\text{在线主项}\ \ge\tfrac12n\log n-(\cdots)}\ \text{（下界型）};\ \text{且 (b) 自标}\ \boxed{\textbf{需证}}\ ✓$$

**⚠️ 归位**：该输入**不是**独立资产，而是 **T² 律／阈值律那条线的证明义务**（`DUP-ALERT-...-T2-law.md`：定理 4.1／3.1 的检测靠「指数增长 $R^n$ 击败多项式界 $(K_{F,1}+K_{F,4})n\log n$」）✓

---

## §2 判定（三条；后两条为本档新增）

### (i) **档案自标「需证」⟹ 不是既得定理** ✗
(b) 逐字含「**需证**」二字（S1 是"升值路径"提案，不是已得结果）⟹ 「$\lambda_n$ **已知**增长」这一措辞**在档案中并不成立**：它是**待证**的比较 ✗

### (ii) ⭐ **窗口空洞**（本档新增，最关键）✗✗
(b) 的成立范围被**明确限定**为 $n\le cT_0^2$（＝已验证高度的平方，即 T² 律范围）。而：
$$\text{无穷多离轴}\Longrightarrow \gamma_j\to\infty\Longrightarrow\ \text{检测阈值}\ n_j\approx\gamma_j^2/\delta\to\infty\Longrightarrow\ \textbf{终将超出任何固定窗口}\ cT_0^2$$
$$\Longrightarrow\ \boxed{\text{该比较在"无穷多离轴"情形下}\ \textbf{永不适用（窗口空洞）}}$$
⟹ 「无穷多 ⟹ 矛盾」**不能由该比较推出**；它若成立，必须另有机制（正是 `C-46` §4 逐字要求而**未给出**的"把**无穷多个不同速率/相位**的离轴项一并控制的对消论证"）✗

### (iii) **三形态皆不可用**（本档新增）✗
把该输入可能的三种严格形态逐一检验：
| 形态 | 后果 | 判定 |
|:--|:--|:--|
| **无条件上界** $\lambda_n\le C n\log n$ | 与单个离轴零点的指数项（`C-46` 引理 A：$\vert w_\rho\vert^n\ge e^{n\delta/(8\gamma^2)}$）冲突 ⟹ 该上界**本身即排除单个离轴零点** ＝ RH（不可能已成立）| ✗ |
| **无条件下界** $\lambda_n\ge\tfrac12n\log n-Cn$ | 同样与离轴指数负项冲突（`C-46` 引理 B 相位对齐 ⟹ $\exists n$ 击穿）⟹ 亦**RH 等价** ⟹ 用作输入＝**循环** | ✗ |
| **RH 下的渐近** $\lambda_n\sim\tfrac12n\log n$ | 直接**循环** | ✗ |
$$\Longrightarrow\ \boxed{\text{三种严格形态}\ \textbf{全不可用}\ \Longrightarrow\ \text{"指数 vs 多项式"这一步}\ \textbf{没有可用的算术侧输入}}\ ✗$$

---

## §3 对 (ISO) 合成链的影响

$$\text{(ISO) 的价值链}：\underbrace{\text{(ISO)}:\ \text{一个}\Longrightarrow\text{无穷多}}_{\text{未知（}C\text{-}59\text{ 已登记）}}\ +\ \underbrace{\text{无穷多}\Longrightarrow\text{矛盾}}_{\text{8/23，第二环}}$$
- 本档：**第二环的输入在无穷多情形下空洞 (ii)，且三形态皆不可用 (iii)** ⟹ 第二环**不是"待复证"，而是"按现有输入不可达"** ⟹ 需**新输入**（非重写、非组装）✗
- ⟹ **推论（重要）**：**(ISO) 的唯一用途（接 RH）当前不可用** —— 即便 (ISO) 被证，**也不得宣称得到 RH** ⚠️ ⟹ 该目标的**优先级应据此下调**；若仍要做，须先解决第二环 ✗
- ⚠️ **诚实**：本档**不**断言 8/23 为假 ✗（`contradiction-reductio-boundary.md` 的"无条件"标记本身可能基于**未落档的**别的论证）—— 本档只判定：**档案中可见的输入不足以支撑它** ✓

---

## §4 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 21:2x）`[纪律]`

```
技术词 算术侧输入  命中文件数=0    ::
技术词 窗口空洞     命中文件数=0    ::
技术词 在线主项     命中文件数=1    :: ./APPRECIATION-AUDIT-2026-09-11.md
技术词 三形态皆不可用 命中文件数=0    ::
```

**读数**：`算术侧输入`／`窗口空洞`／`三形态皆不可用`＝**0 档 ⟹ 本档新增** ✓；⚠️ `在线主项`＝**1 档（`APPRECIATION-AUDIT`）⟹ 档案已有** ✗ —— §1(b) 为**逐字引用**，**不列为本档提出** ✓

## §5 边界

- `[逐字]` §1(a)–(d) 四处引用均逐字 ✓；`[本档新增]` §2(ii) 窗口空洞、§2(iii) 三形态、§3 优先级推论 ✓
- **不声称**：8/23 为假 ✗；不声称 (ISO) 为假 ✗；不证 RH ✗；不给新路线 ✓；不修改任何原档 ✓
- **纪律**：先查后判（R-1 ✓）；未用 RH 作推导 ✓（仅出现在等价性引用中）；**零数值** ✓；未跑 Lean ✓

```
⚠️ 任务＝C-61 §3 的 T1（逐字取出 8/23「指数 vs 多项式」的算术侧界并判定其无条件性）
⚠️ 取出（逐字四处）：(a) 命题＝contradiction-reductio-boundary.md；(b) 输入＝APPRECIATION-AUDIT-2026-09-11.md S1
   「需证 '离轴项 ≥ −(n/(2γ²))e^{n/(2γ²)}' 与 '在线主项 ≥ ½n log n − …' 的比较在 n ≤ cT₀² 时统一成立」；
   (c) 量级＝E30-2-T2-mechanism.md「λ_n 的量级：n log n」；(d) 在册＝CONV1 §1
⚠️ 判定：①自标"需证"⟹ 非既得定理；②⭐窗口空洞：比较只在 n ≤ cT₀² 内 ⟹ 对 γ_j→∞ 永不适用；
   ③三形态皆不可用（无条件上界＝RH／无条件下界＝RH等价⟹循环／RH 下渐近＝循环）
⚠️ 影响：8/23 第二环＝[档案声称／现有输入不可达]（修正 C-61 §2(A)）⟹ (ISO) 接 RH 的用途当前不可用
   ⟹ 优先级应下调；不断言 8/23 为假
✅ 净产出：①算术侧界逐字取出（四处）✓；②窗口空洞 ✗✗；③三形态判定表 ✓；④C-61 §2(A) 修正 ✓；
   ⑤(ISO) 用途不可用的推论 ✓
```
