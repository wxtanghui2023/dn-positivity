已查地图 + **原档逐字**（所查：`PAPERA-block-method.md`（**周期块法全文 71 行**）、`PAPERA-quadratic-gap-located.md`（**缺口的名字**）、`PAPERA-deltaN-methods-survey.md`（`Fluc(n)` 对象定义与难点）、`OSCILLATION-CANCELLATION-TECHNIQUES-SURVEY-unconditional-vs-conditional.md`（三机制普查）、`AUDIT-WALLS-AND-DIFFICULTIES-20260917.md`（`D1`／`D3` 逐字）、`C-86`；**外查**：`MO 152126`（定量 Riemann–Lebesgue 与"衰减＝测度/函数正则性"））。**结论**：`D3(b)` 第一刀——**块法确实消解了"光滑主项"的端点障碍（真增益）**，但**只剩测度项**；而该测度项**归一化到 `D1`（相位均匀性）** ⟹ ⭐ **`D3(b)` 与 `D1(b)` 是同一个叶子** ⟹ 四个可攻叶子实际**收敛为 3 个** ✓✓

# C-87 · **`D3(b)` 第一刀：块法成立（光滑项），缺口归一化到 `D1`**

> **时间**：2026-09-18 13:22 唐先生「继续」（按 `C-86` §6 第一优先：核 `D3(b)`）
> **性质**：拆解／归约；**不声称严格界** ⚠️

---

## §0 结论（先行）

$$\textbf{(1)}\ \text{块法的增益}\ \textbf{属实}：\text{在一个完整相位周期上}\ \int_0^{2\pi}\cos u\,du=0\ \textbf{且}\ \int_0^{2\pi}u\cos u\,du=0 \Longrightarrow \text{只留曲率项}✓$$
$$\qquad \text{（对照：}\sin\ \text{的线性项}\ \int_0^{2\pi}u\sin u\,du=-2\pi\ne0 \Longrightarrow \textbf{sin 形式拿不到这个增益}✓）$$
$$\textbf{(2)}\ ⚠️\ \text{但它}\ \textbf{只覆盖光滑主项}：\text{`δN` 是}\textbf{测度}（\text{非光滑函数}）\ \text{且以}\ \sin\ \text{形式出现} \Longrightarrow \textbf{增益不适用}✓$$
$$\textbf{(3)}\ ⭐\ \text{剩下的测度项}\ \text{即}\ \texttt{Fluc}(n)\ \text{，其缺口}\ \textbf{有名字}：\boxed{\text{"Riemann--Lebesgue 的定量版"}}✓$$
$$\textbf{(4)}\ ⭐⭐\ \text{本档结构判定}：\text{`dS` 是}\ \textbf{离散测度} \Longrightarrow \text{Fourier 衰减只能来自}\ \textbf{点间相消} \Longrightarrow \text{可得增益＝}\textbf{√-级}；\text{而此项的一致性要求}\ \text{恰是}\ \text{`D1`}\ \textbf{相位均匀性}✓✓$$
$$\qquad \Longrightarrow\ \boxed{\text{`D3(b)`}\ \textbf{归一化到}\ \text{`D1`}：\text{四个可攻叶子}\ \textbf{收敛为 3 个}}✓✓$$

---

## §1 块法（逐字要点；源 `PAPERA-block-method.md`）

$$\text{对象}：I(n)=\int_0^{T_0}\cos(n\theta(t))\cdot\mathrm{main}'(t)\,dt✓$$
$$\text{路线}：\text{分部积分}\longrightarrow\ \text{留下}\ O(\mathrm{main}(T_0))\ \textbf{边界项}✗;\qquad \text{块法}\longrightarrow\ \text{按}\ \varphi=n\theta(t)\ \text{前推}\ 2\pi\ \text{分块},\ \text{换元}\ u=\varphi(t)✓$$
$$\textbf{关键恒等式}：\int_0^{2\pi}\cos u\,du=0\quad\text{（常数项}\to0）;\qquad \int_0^{2\pi}u\cos u\,du=[u\sin u+\cos u]_0^{2\pi}=0\quad（\textbf{线性项也}\to0）✓✓$$
$$\text{定量}：G\approx n\log(n/u)/(2\pi u^2),\ G''\approx c\,n/u^4,\ \text{块数}\approx n/2 \Longrightarrow |I(n)|\approx T_0^3/(6\pi n^2)✓$$
$$\qquad \text{在二次端点}\ n=T_0^2：|I|\approx1/(6\pi T_0)\ \text{vs 信号}\ 2N\approx(T_0/\pi)\log T_0 \Longrightarrow \textbf{可忽略}✓✓$$

## §2 ⚠️ 该档自述的三条保留（逐字）

$$\textbf{①}\ \text{末块（不完整周期）}：\text{须把截断选在}\ \sin\varphi=0\ \text{处}（\text{可控}）✓$$
$$\textbf{②}\ ⭐\ \text{`δN` 部分}\ \textbf{不能用块法}：\text{`δN` 是}\textbf{测度};\ \text{且对}\ \sin\ \text{线性项}\ \textbf{不消失} \Longrightarrow \text{`δN` 项需自己处理（上一轮撤回的那一步，仍未解决）}✗$$
$$\textbf{③}\ \text{数值验证}\ \textbf{未做}：\text{设计不可行}（\text{块数}\approx n/2\times400\ \text{点}\times200\ \text{次二分}\approx10^9）\ \text{须重设计}✓$$
$$\qquad ⚠️\ \textbf{档内自述（逐字）}：\text{"不主张块法已给出}\textbf{严格误差界} \text{"};\ \text{"不主张端点已完全解决"}✓$$

## §3 ⭐ 缺口的名字（源 `PAPERA-quadratic-gap-located.md` 逐字）

$$\text{源}：\text{Voros 2006（}\texttt{arXiv:math/0506326}\text{）}\textbf{逐字复述的 Oesterlé 论证}✓$$
$$\text{③逐字}：\text{"Now replace}\ N(T)\ \text{by its large-}T\ \text{form (16)}\ \textbf{neglecting}\ \delta N(T)\ \text{and other}\ O(\theta^{-\alpha})\ \text{terms}:\ \text{the error is}\ o(1)\ \textbf{by the Riemann--Lebesgue lemma}"✓$$
$$\qquad \Longrightarrow\ \boxed{\text{缺口的名字＝"}\textbf{Riemann--Lebesgue 的定量版}\text{"}}✓✓\（\text{即：}o(1)\ \text{不够，需}\ \textbf{定量速率}，\text{且要在}\ n\lesssim T_0^2\ \textbf{一致}）$$

## §4 对象（源 `PAPERA-deltaN-methods-survey.md` 逐字）

$$\texttt{Fluc}(n)=\int_0^{T_0}f(n\theta(t))\,dS(t),\qquad S(T)=N(T)-\mathrm{main}(T),\qquad \theta(t)=2\arctan\!\frac1{2t},\qquad f=1-\cos$$
$$\iff\ \texttt{Fluc}(n)=\sum_{\gamma\le T_0}f(n\theta_\gamma)-\int_0^{T_0}f(n\theta(t))\,d\mathrm{main}(t)$$
$$\text{需求}：|\texttt{Fluc}(n)|<\text{允许量}=N(T_0)-nB_{T_0}\quad(n\lesssim T_0^2)✓$$
$$\text{难点（逐字）}：\text{相位}\ n\theta(t)\ \text{的瞬时频率}\approx n/t^2;\ S\ \text{是素数频率}\ \log p^k\ \text{的正弦叠加} \Longrightarrow \textbf{共振点}\ t_{\rm res}\approx\sqrt{n/\log n}\ \text{落在}\ [0,T_0]\ \text{内}✓$$

## §5 ⭐⭐ 本档结构判定（`[本档]`）

$$\textbf{(i)}\ \text{`dS`}\ \textbf{是离散测度}（\text{支撑＝零点集，}\dim_H=0\text{）} \Longrightarrow \text{其振荡积分的衰减}\ \textbf{只能来自}\ \textbf{点间相消};\ \textbf{无"正则性"可借}✓$$
$$\qquad \text{（对照：一般测度的}\ \textbf{Fourier 衰减＝正则性}（\text{`MO 152126`}\ \text{逐字："the decay of the Fourier transform will measure the local regularity"}）⟹ \text{离散测度}\ \textbf{无此红利}✓✓）$$
$$\textbf{(ii)}\ \text{可得增益级别}＝\textbf{√-级相消};\ \text{而档案的振荡普查已判}：\text{唯一}\ \textbf{无条件超}\sqrt{\cdot}\ \text{机制}＝\textbf{结构化分解}（\text{Harper 型}）✓$$
$$\qquad \text{且}\ \textbf{素数缺可分解表示}（\text{parity}） \Longrightarrow \textbf{超}\sqrt{\cdot}\ \text{增益不可得}✓✓$$
$$\textbf{(iii)}\ \text{而该需求是}\ \textbf{对}\ n\ \text{一致} \text{的（}\text{共振点落入区间}） \Longrightarrow \text{这正是}\ \text{`D1`}\ \textbf{相位均匀性}✓✓$$
$$\Longrightarrow\ \boxed{\text{`D3(b)`}\ \textbf{归一化到}\ \text{`D1`};\ \text{两叶合一}}✓$$

## §6 拆解结果更新（对 `C-86` §3）

$$\text{可攻叶子}\ 4 \Longrightarrow \textbf{3}：\underbrace{D3(b)\equiv D1(b)}_{\text{合并}}\ \big|\ D10(a)\ \big|\ W8(b)✓$$
$$\qquad \text{其中}\ \textbf{已消解一半}：D3(b)\ \text{的光滑主项由块法处理}\ ✓;\ \text{剩}\ \textbf{测度项}＝\text{定量 Riemann--Lebesgue}＝\text{相位均匀性}✓$$
$$\qquad ⚠️\ \text{且}\ \text{`D1` 在档案里}\ \textbf{不是统一墙}：\text{在}\ \text{`CONV2`／`CONV3`}\ \text{处}\ \textbf{已撤回};\ \textbf{仅在 Burnol 型转换处仍为关键步}✓✓$$

## §7 下一步（下刀点）

$$\boxed{\text{读 Burnol（}\texttt{arXiv:math/0103058}\text{）的 uniformity 段逐字}，\text{与}\ \text{`CONV2`／`CONV3`}\ \text{撤回判词}\ \textbf{对质}}✓✓$$
$$\qquad \text{要判定的三件事}：\text{(1) 该 uniformity 的}\textbf{精确数学内容};\ \text{(2) 它是否}\ \textbf{真的} \text{是"定量 Riemann--Lebesgue"的等价物};\ \text{(3) 它是否}\ \textbf{真的} \text{不可用现有工具获得}✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 13:2x）`[纪律]`（先跑后写）

```
技术词 相位周期分块 命中文件数=2    :: ./C87-D3b-first-cut-block-method-works-smooth-part-gap-normalizes-to-D1.md ./PAPERA-block-method.md
技术词 定量版        命中文件数=10   :: ./C87-... ./REPORT-literature-and-feasibility-2026-09-13.md ./C86-...
技术词 两叶合一      命中文件数=1    :: ./C87-D3b-first-cut-block-method-works-smooth-part-gap-normalizes-to-D1.md
```
**读数（按实测）**：⚠️ `相位周期分块`＝**2 档 ⟹ `PAPERA-block-method` 已用** ⟹ 本档为**引用**（不列为首次命名）✗；⚠️ `定量版`＝**10 档 ⟹ 档案已有**（含 `REPORT-literature-and-feasibility-2026-09-13`）⟹ 引用 ✗；`两叶合一`＝**1 档（仅本档）⟹ 本档新增** ✓

## §9 边界

- `[逐字]` §1–§4 全部取自 `PAPERA-*` 三档 ✓；`[本档]` §5 结构判定（离散测度 ⟹ 无正则性红利 ⟹ √-级 vs 超-√ 级）与 §6 合并 ✓
- `[外查]` `MO 152126` 为**社区答复**（非论文），仅用于"衰减＝正则性"这一常识性表述 ⚠️
- **不声称**：块法已给严格界 ✗（档内自述亦如此）；不声称 `D3(b)` 已解决 ✗；不判 `D1` 结局 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 任务：按 C-86 §6 第一优先开 D3(b)（核 PAPERA 周期块法关键恒等式能否消解端点障碍）
✅ 结论（三点）：
   (1) 块法增益属实：完整相位周期上 ∫₀^{2π}cos u du = 0 且 ∫₀^{2π}u cos u du = 0（线性项也消失！）⟹ 只留曲率项；
       对照 sin：∫₀^{2π}u sin u du = −2π ≠ 0 ⟹ sin 形式拿不到该增益
   (2) ⚠️ 只覆盖光滑主项：δN 是测度（非光滑）且以 sin 形式出现 ⟹ 增益不适用（档内自述三条保留：末块/δN/数值未验；
       档内明确"不主张严格误差界"）
   (3) ⭐ 缺口有名字 = "Riemann–Lebesgue 的定量版"（PAPERA-quadratic-gap-located 逐字，源 Voros 2006 复述 Oesterlé 论证；
       "the error is o(1) by the Riemann–Lebesgue lemma" ⟹ o(1) 不够，需定量速率且在 n ≲ T₀² 一致）
⭐ 本档结构判定：dS 是**离散测度**（支撑＝零点集，dim_H = 0）⟹ 其振荡积分衰减**只能来自点间相消**（无"正则性"红利，
   对照 MO 152126：一般测度的 Fourier 衰减＝正则性）⟹ 可得增益＝**√-级相消**；而档案振荡普查已判：唯一无条件超 √ 机制＝
   结构化分解（Harper 型），素数缺可分解表示（parity）⟹ 超 √ 增益不可得 ⟹ 该需求是**对 n 一致**的（共振点 t_res ≈ √(n/log n) 落入 [0,T₀]）
   ⟹ 这正是 **D1 相位均匀性** ⟹ **D3(b) 归一化到 D1：两叶合一**
⚠️ 拆解结果更新（对 C-86 §3）：可攻叶子 4 ⟹ **3**：{D3(b) ≡ D1(b)} | D10(a) | W8(b)；且 D3(b) 的**光滑主项已消解**，
   剩测度项 ＝ 定量 Riemann–Lebesgue ＝ 相位均匀性
⚠️ D1 在档案里不是统一墙：CONV2/CONV3 处已撤回；**仅在 Burnol 型转换处仍为关键步**
✅ 下一步（下刀点）：读 Burnol（arXiv:math/0103058）uniformity 段逐字，与 CONV2/CONV3 撤回判词对质；判三件事：
   ① uniformity 的精确数学内容 ② 它是否真的是"定量 Riemann–Lebesgue"的等价物 ③ 它是否真的不可用现有工具获得
✅ 净产出：①块法增益与适用边界（逐字）✓；②缺口命名与对象（逐字）✓；③离散测度⟹√-级 vs 超-√ 的结构判定 ✓；④两叶合一 ✓；⑤下刀点 ✓
```
