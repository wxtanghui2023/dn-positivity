已查地图：**逐档核对**（所查档：`E118-dyadic-offdiagonal.md`（全文）、`E119-wh-closed-window-cannot-average.md`（全文）、`EXPLORATION-POINTS-REGISTER.md` 的 E118／E119 行、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`W6-MAJORANT-1`／`1b`–`1g`、`AUDIT-WALLS-AND-DIFFICULTIES-20260917.md`、`MASTER-NOGO-AND-LIVE-PATHS.md`、`V266-current-front-state-card-five-legal-entries.md`、`MATH-STATEMENT-A-offdiagonal-second-moment-beyond-support-1.md`）。**结论**：`E119` §6 的「最高优先＝**定位簿记错误**」经回查**仅见于 E118／E119／登记表三处**，**此后无档解掉** ⟹ 仍为活结 ✓；本档给出**候选定位（窗权重不统一：对角 `∫x dx`、非对角 `∫dx`，差因子 `x≈N`）**＋ 三项一致性检验 ＋ 冲突消解 ✗

# C-64 · **E118/E119 簿记冲突的候选定位** —— 窗权重不统一（差因子 `x≈N`）

> **时间**：2026-09-17 21:5x 唐先生「继续」⟹ 承接 W6 侧（我排的第 1 位），执行 `E119` §6 自称**最高优先**的那一项。
> **本档**：**定位候选 ＋ 三项一致性检验**；**不**宣称彻底解决 ✗、**不**新增路线 ✓

---

## §0 结论（先行）

$$\text{同一条 }L^2\text{ 量}\ \mathfrak E=\int_N^{N+Y}|\Delta(x,h)|^2dx\ \text{在}\ E118\ \text{§2／}E119\ \text{§1 中被用了}\ \textbf{两种窗权重}：$$
$$\textbf{对角}：\int_N^{N+Y}x\,dx\approx NY=\sqrt N\cdot N=N^{3/2}\ \checkmark\qquad\textbf{非对角／相干}：\int_N^{N+Y}dx\approx Y=\sqrt N\ ✗$$
$$\Longrightarrow\ \boxed{\text{簿记错误（候选）＝窗权重不统一，差因子}\ x\approx N\ =\ \text{`E119` §6 可疑点①（权重 1/(\rho\rho') 精确作用）的具体化}}✓✓$$
$$\textbf{修正后}：\text{非对角全相干值}\ \approx hN\log^2N\ \gg\ hN\ \Longrightarrow\ \textbf{矛盾消解（不再"离无条件结果只差 }\sqrt N\text{"）}✓✓\ \text{且}\ \textbf{不产生突破}（\text{仍需 pair-correlation 输入}）✓$$

---

## §1 对象与记号 `[逐字取自 E118 §0②／E119 §0①]`

$$\Delta(x,h)\simeq-\sum_\rho x^\rho\frac{(1+h/x)^\rho-1}{\rho}\qquad(h\ll x)\ ✓;\qquad u=\log\Bigl(1+\frac hx\Bigr)\sim\frac hN\ ✓$$
$$\textbf{尺度（E118 ④"尺度巧合"逐字）}：x\sim N,\quad h=\sqrt N,\quad Y=\sqrt N,\quad T:=\frac1u\sim\frac Nh=\sqrt N\ \checkmark$$
$$\textbf{关键恒等式（本档显式化）}：\rho=\tfrac12+i\gamma\ \Longrightarrow\ \boxed{x^\rho=x^{1/2}\cdot x^{i\gamma}}\ \Longrightarrow\ |x^\rho|^2=x$$
$$\Longrightarrow\ |\Delta(x,h)|^2=x\cdot\Bigl|\sum_{|\gamma|\lesssim T}B_\gamma\,x^{i\gamma}\Bigr|^2,\qquad B_\gamma:=\frac{e^{\rho u}-1}{\rho}\quad(|B_\gamma|\asymp u\ \text{当}\ |\gamma|\lesssim T\ ✓)$$
$$\boxed{\mathfrak E=\int_N^{N+Y}|\Delta|^2dx=\int_N^{N+Y} x\cdot\Bigl|\sum_{|\gamma|\lesssim T}B_\gamma x^{i\gamma}\Bigr|^2dx}\qquad\text{目标}：\mathfrak E=o(hN)=o(N^{3/2})\ ✓$$

## §2 逐项重算（**对角 ✓ 自洽；非对角 ✗ 差因子 N**）

$$\textbf{对角（}\gamma=\gamma'\text{）}：\mathfrak E_{\rm diag}=\Bigl(\int_N^{N+Y}x\,dx\Bigr)\sum_\gamma|B_\gamma|^2\approx NY\sum_\gamma|B_\gamma|^2$$
$$\text{零点数}\ N_\gamma(\lesssim T)\approx\frac{T\log T}{2\pi}\ ✓;\quad |B_\gamma|^2\approx u^2=\frac{h^2}{N^2}\ \Longrightarrow\ \sum_\gamma|B_\gamma|^2\approx\frac{T\log T}{2\pi}\cdot\frac{h^2}{N^2}=\frac{h\log T}{2\pi N}$$
$$\Longrightarrow\ \mathfrak E_{\rm diag}\approx NY\cdot\frac{h\log T}{2\pi N}=\frac{Yh\log T}{2\pi}=\frac{\sqrt N\cdot\sqrt N\log N}{2\pi}=\boxed{\frac{N\log N}{2\pi}}\ \checkmark$$
$$\qquad\textbf{与 E118 §2 逐字「对角}\approx N\log N\ ✓\text{」一致}\ ✓\ \Longrightarrow\ \textbf{对角确实带 }x\text{ 权}\ ✓$$

$$\textbf{非对角（全相干上界）}：\Bigl|\sum_{|\gamma|\lesssim T}B_\gamma x^{i\gamma}\Bigr|^2\le\Bigl(\sum_\gamma|B_\gamma|\Bigr)^2\approx\Bigl(\frac{T\log T}{2\pi}\cdot u\Bigr)^2=\Bigl(\frac{\log T}{2\pi}\Bigr)^2$$
$$\Longrightarrow\ \text{正确窗权重}\ \int_N^{N+Y}x\,dx\approx N^{3/2}\ \Longrightarrow\ \mathfrak E^{\rm coh}_{\rm off}\approx N^{3/2}\frac{\log^2T}{4\pi^2}=\boxed{\frac{hN\log^2T}{4\pi^2}}$$
$$\textbf{而 E118 §2／E119 §1 给的是}\ \sqrt N\log^2N/4\pi^2\ \checkmark\ \Longrightarrow\ \boxed{\text{相差恰为因子}\ N\approx x}\ ✗✗$$

## §3 三项一致性检验（都指向同一结论）

$$\textbf{检验 1（内部一致）}：\text{同一}\ \mathfrak E\ \text{的对角与非对角必须同权}\ ✓;\ E118\ \text{§2 对角用}\ \int x\,dx\ \text{、}\ \Sigma_k\mathcal N_k\ \text{与 E119 §1 相干值用}\ \int dx\ \Longrightarrow\ \textbf{不一致}\ ✗$$
$$\textbf{检验 2（与点态形式一致）}：E119\ \text{③ 要求}\ |\Delta|=o(\sqrt N)\ ✓;\ \text{由}\ \mathfrak E\approx Y|\Delta|^2\ \text{与修正值}\ \mathfrak E^{\rm coh}_{\rm off}\approx hN\log^2N：$$
$$\qquad|\Delta|^2\approx\frac{hN\log^2N}{Y}=N\log^2N\ \Longrightarrow\ |\Delta|\approx\sqrt N\log N\ \checkmark\ \text{—— 与 RH 的}\ O(\sqrt N\log^2N)\ \textbf{同阶（差一个 }\log\text{）}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{相干值}\approx\text{点态界（自洽）}\ ✓\ \text{而修正前它比点态界小}\ \sqrt N\ \text{倍}\ ✗\ \text{（不自洽）}$$
$$\textbf{检验 3（与承重墙一致）}：\text{修正后}\ o(hN)\ \textbf{恰好}\equiv\text{"满相干值被压制"}\ \equiv\ \text{需 pair-correlation 跨 support }1\ ✓$$
$$\qquad\text{与}\ E118\ \text{⑤「需把 pair correlation 从}\ T/\log T\ \text{推到}\ T\text{」＋}\ \text{`SUPPORT-1-WALL`}\ \textbf{完全一致}\ ✓✓$$

## §4 冲突消解（**并说明它不产生突破**）

$$\text{修正前}：\mathfrak E\approx N\log N=o(N^{3/2})\ \Longrightarrow\ C_3\ \text{无条件}\ \Longrightarrow\ \text{Legendre}\ \Longrightarrow\ \text{与已知矛盾}\ ✗$$
$$\text{修正后}：\mathfrak E_{\rm off}^{\rm coh}\approx hN\log^2N\ \gg\ hN\ \Longrightarrow\ \textbf{得不出}\ o(hN)\ \Longrightarrow\ \textbf{矛盾消失}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{同一条 }\sqrt N\ \text{级"看似到手的便宜"}\textbf{不存在};\ \text{要求}\ o(hN)\ \text{仍是真要求（需新输入）}}\ ✓$$
$$\qquad ⭐\ \text{顺带解释}\ \text{`W6-MAJORANT-1}`\ \text{今日 12:53 的 FAIL}\ ✓：\text{die 的}\Phi\text{-majorant 也带同一权问题};\ \text{统一后它同样给不出}\ o(hN)\ ✓\ \text{（不冲突，方向一致）}$$

## §5 与 `E119` §6 三疑点的归位

| 疑点（E119 §6 逐字排序）| 本档判定 |
|:--|:--|
| ① 「$\Delta$ 的显式公式**截断与权重**，$1/\rho$ 与 $1/(\rho\rho')$ 的精确作用未核」 | ⭐ **本档定位＝此点的具体化**（差因子 $x$，来自 $\vert x^\rho\vert^2=x$）✓ |
| ② 「**自然高度**：$T\sim N/h$ 是否即相关零点的高度上限」 | 本诊断**不依赖** ✓（若上限更高则更多零点参与，量级只会更大 ⟹ 结论方向不变）⚠️ 仍建议核 |
| ③ 「$A_\gamma$ 的**归一化**：$u=\log(1+h/x)$ vs $h/x$ 的二阶项」 | 本诊断**不依赖** ✓（$u\approx h/x$ 的主项足矣；二阶项只改常数）⚠️ |

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 21:5x）`[纪律]`

```
技术词 x-权            命中文件数=0    ::
技术词 簿记错误定位 命中文件数=0    ::
技术词 窗权重        命中文件数=0    ::
```
**读数**：三词均 **0 档 ⟹ 本档新增** ✓（`x-权`／`窗权重`／`簿记错误定位` 三种表述均为本档提出）✓

## §7 边界（诚实）

- `[逐字]` §1 的 $\Delta$ 表达式、$u$、尺度巧合、$W_h$ 关闭、E118 ⑤、E119 ③ 与 §6 三疑点均**逐字引用** ✓
- `[本档]` §1 的 $x$-权显式化、§2 的逐项重算、§3 三项检验、§4 修正与消解 ✓
- ⚠️ **未做**：未逐项核 `E118` §2 的**全部系数**与 $F_T$ 的**内部精确定义**（本档取 §2 逐字「$F_T\approx Y=T$」与「对角 $\approx(\sqrt N\log N)\cdot h^2Y/N$」两条作读数 ⟹ 若其内部定义与此不同，结论需按同一原则（同权）重述 ✓）
- **不声称**：冲突已**彻底**解决（只给出一致的候选定位＋三项检验）✗；不证 RH ✗；不给新路线 ✓；不修改任何原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值**（仅初等量级比较）✓；未跑 Lean ✓

```
⚠️ 任务＝W6 侧第一刀：E119 §6 自称"最高优先"的「定位簿记错误」（三次重现、此后无档解掉 ⟹ 活结 ✓）
⚠️ 定位候选：同一 𝓔=∫|Δ|²dx 用了两种窗权重 —— 对角 ∫x dx≈N^{3/2} ✓、非对角/相干 ∫dx≈√N ✗ ⟹ 差因子 x≈N
   （根：|x^ρ|²=x；即 E119 §6 疑点①「权重 1/(ρρ') 精确作用」的具体化）
⚠️ 三项检验：①内部同权 ✗；②与点态形式自洽（修正后 |Δ|≈√N log N，与 RH 的 O(√N log²N) 同阶 ✓）；
   ③与 SUPPORT-1 墙一致（o(hN) ≡ 满相干被压制 ≡ 需 pair-correlation 跨 support 1 ✓）
⚠️ 冲突消解：修正后非对角相干 ≈ hN log²N ≫ hN ⟹ 得不出 o(hN) ⟹ 矛盾消失 ✓；不产生突破 ✓
   顺带解释 W6-MAJORANT-1（12:53 FAIL）同向一致 ✓；疑点②③ 本诊断不依赖 ✓
⚠️ 边界：未逐项核 E118 §2 全部系数与 F_T 内部定义；不断言彻底解决；未用 RH；零数值
✅ 净产出：①簿记错误候选定位（x-权/窗权重不统一）✓；②三项一致性检验 ✓；③冲突消解 ✓；
   ④对 W6-MAJORANT FAIL 与 SUPPORT-1 的一致性解释 ✓；⑤E119 §6 三疑点归位 ✓
```
