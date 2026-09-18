已查地图：**逐档核对**（所查档：`E118-dyadic-offdiagonal.md`（**全文含 §4／§5**）、`E119-wh-closed-window-cannot-average.md`（全文）、`C64-...md`（本会话前档）、`EXPLORATION-POINTS-REGISTER.md` E118／E119 行、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`W6-MAJORANT-1g`）。**结论**：`E118` §2 的**七项逐一复核完毕** ⟹ `C-64` 的定位 **坐实**（不是推翻）✓；并发现更硬的形式：**`𝒩`（`E118` 定义的量）与 `𝓔`（窗口二次型）被混用，两者差因子 `N`（＝`x` 权）** ✓✓

# C-65 · **A 执行**：`E118` §2 逐项复核 —— 定位**坐实**（`𝒩` vs `𝓔` 混用，差因子 `x≈N`）

> **时间**：2026-09-17 21:5x 唐先生「先A」（逐项核 `E118` §2 全部系数 ＋ `F_T` 定义）。
> **本档**：只做**逐项核与坐实**；不改原档 ✓、不新增路线 ✓

---

## §0 结论（先行）

$$\textbf{两个不同量被混用}：\underbrace{\mathcal N=\sum_{\gamma,\gamma'}A_T(\gamma)\overline{A_T(\gamma')}F_T(\gamma-\gamma')}_{\text{E118 定义，}F_T=K_Y=\int_N^{N+Y}\!e^{i\delta\log x}dx\ \textbf{（无 }x\text{ 权）}}\qquad\text{vs}\qquad \underbrace{\mathfrak E=\int_N^{N+Y}|\Delta|^2dx}_{\text{真对象（带 }x\text{ 权）}}$$
$$\boxed{\mathfrak E=N\cdot\mathcal N\qquad(N=\text{窗上 }x\text{ 权重},\ \text{来自}\ |x^\rho|^2=x)}✓✓$$
$$\Longrightarrow\ \text{E118 §2 把}\ \textbf{$\mathcal N$ 的分层估计}（\sqrt N\log^2N）\text{与}\ \textbf{$\mathfrak E$ 的对角}（N\log N）\text{直接相比}\ ✗\ \Longrightarrow\ \textbf{差因子 }N\ ✓✓$$
$$\Longrightarrow\ \text{修正后}\ \mathcal N_{\rm off}\ \text{相干值}\times N=\frac{hN\log^2T}{4\pi^2}\ \gg\ hN\ \Longrightarrow\ \textbf{矛盾消失};\ \text{仍}\ \textbf{无突破}（\text{需 pair-correlation 输入}）✓$$

---

## §1 逐项复核表（`E118` §2 七项，逐字对照）

| # | `E118` §2 逐字 | 本档复核 | 判定 |
|:--:|:--|:--|:--:|
| 1 | 分层 $\vert\gamma-\gamma'\vert\sim2^k\frac T{\log T}$ | dyadic 分层合法 ✓ | ✓ |
| 2 | pair count $\approx N(T)\frac{\log T}{2\pi}\delta=\frac{T\log T}{2\pi}\cdot\frac{\log T}{2\pi}\delta$ | 零点密度 $=\frac{\log T}{2\pi}$ ✓（$N(T)\asymp\frac T{2\pi}\log T$）| ✓ |
| 3 | weight $\frac1{\vert\rho\vert\vert\rho'\vert}\approx\frac1{T^2}$ | $= \vert A_T(\gamma)\vert^2\approx u^2$，$u=\frac hN=\frac1{\sqrt N}=\frac1T$ ✓ | ✓ |
| 4 | $F_T\approx Y=T$，并自述 $\vert F_T\vert\ll\min(Y,\frac N{\vert\delta\vert})$ | 该形式**就是** $K_Y(\delta)=\int_N^{N+Y}e^{i\delta\log x}dx$ ⟹ **无 $x$ 权** ⚠️；**若为窗口二次型核则应为** $\int_N^{N+Y}x\,e^{i\delta\log x}dx\approx N K_Y$ | ✗ **分歧点** |
| 5 | $\mathcal N_k\approx\frac{T\log^2T}{4\pi^2}2^k$ | 复核 $=$ (pair count)·$\frac1{T^2}$·$Y=\frac{T\log T}{2\pi}\frac{\log T}{2\pi}\cdot\frac{2^kT}{\log T}\cdot\frac1{T^2}\cdot\sqrt N=\frac{2^k\sqrt N\log T}{4\pi^2}$ ✓（与逐字同，因 $Y=T=\sqrt N$）⟹ **该层用 $Y$（无 $x$ 权）** | ✗ |
| 6 | $\sum_k\mathcal N_k\approx\frac{T\log^2T}{4\pi^2}=O(\sqrt N\log^2N)$ | 几何比 2、顶层 $2^k\lesssim\log T$ ⟹ $\approx Y\frac{\log^2T}{4\pi^2}=\frac{\sqrt N\log^2N}{4\pi^2}$ ✓ ⟹ **同样无 $x$ 权** | ✗ |
| 7 | 对角 $\approx(\sqrt N\log N)\cdot\frac{h^2Y}N=N\log N$ | 复核 $\mathfrak E_{\rm diag}=(\int_N^{N+Y}x\,dx)\sum\vert A_T\vert^2=NY\cdot\text{count}\cdot\frac{h^2}{N^2}=\text{count}\cdot\frac{h^2Y}N$ ⟹ **逐字式即此** ⟹ **该式用 $NY$（带 $x$ 权）** | ✓ |

$$\Longrightarrow\ \boxed{\text{同一计算里，第 5／6 项用}\ Y\ \text{、第 7 项用}\ NY\ \Longrightarrow\ \textbf{内部不一致，差因子}N}\ ✓✓$$

## §2 定点订正（把 5／6 补上 $x$ 权）

$$\mathcal N_k^{\rm corr}=N\cdot\frac{2^k\sqrt N\log T}{4\pi^2}=\frac{2^kN^{3/2}\log T}{4\pi^2};\qquad \sum_k\mathcal N_k^{\rm corr}=\frac{N^{3/2}\log^2T}{4\pi^2}=\boxed{\frac{hN\log^2T}{4\pi^2}}$$
$$\text{与对角比较}\ \Bigl(\mathfrak E_{\rm diag}=\frac{N\log N}{4\pi}\Bigr)：\quad \text{非对角}\ \textbf{主导}\ ✗\ \Longrightarrow\ \mathfrak E\approx\frac{hN\log^2N}{4\pi^2}\ \Longrightarrow\ \textbf{得不出}\ o(hN)\ ✓✓$$
$$E119\ \text{§1 的两个数（majorant}\ \sqrt N\log^2N\ \text{、相干值}\ \sqrt N\log^2N\text{）}\ \textbf{同一漏因子}：\text{应为}\ \frac{hN\log^2N}{4\pi^2}\ ✓$$

## §3 三项复检（含对 `C-64` 的一处补强）

$$\textbf{(i) 点态自洽}：\mathfrak E\approx Y|\Delta|^2\ \Longrightarrow\ |\Delta|^2\approx\frac{hN\log^2N}{\sqrt N}=N\log^2N\ \Longrightarrow\ |\Delta|\approx\sqrt N\log N\ \checkmark\ \text{与 RH 的 }O(\sqrt N\log^2N)\ \textbf{同阶}\ ✓$$
$$\qquad\Longrightarrow\ \text{与}\ E119\ \text{③ 的「RH 差一个}\ \log^2\text{」}\ \textbf{一致}\ ✓$$
$$\textbf{(ii) 与承重墙一致}：o(hN)\equiv\text{"满相干被压制"}\equiv\text{pair-correlation 跨 support }1\ ✓\ \text{（}SUPPORT\text{-}1\ \text{＋}\ E118\ \text{⑤）}✓$$
$$\textbf{(iii) 定位更硬（本档补强）}：C\text{-}64\ \text{只指出"对角与非对角不同权"；本档进一步指出}\ \textbf{E118 §2 第 5 项与其自述的}\ F_T\ \textbf{定义本身就不匹配}（F_T=K_Y\ \text{无 }x\ \text{权}，而对角按带\ x\ \text{权计算}）✓✓$$

$$\textbf{⚠️ 一处订正（`C-64` 未及）}：E118\ \text{§2 称"相干增益}=\sqrt N/\log^3N"；\ \text{按本档修正，相干／典型}=\sqrt N\log N\ ✓$$
$$\qquad \Longrightarrow\ \textbf{量级}\ \sqrt N\ \textbf{一致}\ ✓\ \text{但}\ \textbf{log 幂次方向可疑}（\log^{1}\ \text{vs}\ \log^{-3}）⚠️\ \text{留待核，不据此下结论} ✓$$

## §4 判词与下一步

$$\boxed{\text{C-64 的定位}\ \textbf{坐实}（逐项核 7/7 ＋ 三项检验）；\ \text{修正式}=\mathcal N\to\mathfrak E=N\mathcal N;\ \text{矛盾消解};\ \textbf{不产生突破}}\ ✓$$
$$\text{与}\ W6\text{-MAJORANT-1}\ \text{（今日 12:53 FAIL）}\ \textbf{同向一致}\ ✓\ \text{（同一条 }\times N\ \text{的幻觉不存在）}✓$$
$$\textbf{下一步（供唐先生定）}：\text{(A2)}\ E119\ \text{§2 重做}：\text{修正后 majorant 能否给}\ o(hN)？\ \text{预判：}\textbf{给不出}\ \text{（与 MAJORANT FAIL 一致）};\ \text{(C)}\ SUPPORT\text{-}1\ \text{closure §7 新面};\ \text{(D)}\ \text{论文线} ✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 21:5x）`[纪律]`

```
技术词 定位坐实     命中文件数=0    ::
技术词 同权原则     命中文件数=0    ::
技术词 权重不统一  命中文件数=1    :: ./C64-E118-E119-bookkeeping-conflict-candidate-localization-window-weight.md
```
**读数**：`定位坐实`／`同权原则`＝**0 档 ⟹ 本档新增** ✓；`权重不统一`＝**1 档（`C-64`，本会话前档）** ⟹ **引用** ✓

## §6 边界（诚实）

- `[逐字]` §1 表内七项、§3(iii) 的 `F_T` 自述界、`E119` ③ 均**逐字取自原档** ✓
- `[本档]` §0 的 $\mathfrak E=N\mathcal N$、§1 的逐项复核、§2 的订正、§3(iii) 的补强、§3 的 log 幂次注 ✓
- **不声称**：冲突**彻底**解决（本档为**自洽性重算**，非独立第三方核验；若 `E118` 内部另有 $A_T$ 归一化约定与 §2 逐字不同，结论须按"同权"原则重述）✗；不证 RH ✗；不给新路线 ✓；不修改原档 ✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓；未跑 Lean ✓

```
⚠️ 任务＝唐先生「先A」：逐项核 E118 §2 全部系数 + F_T 定义
⚠️ 结果：7/7 项复核完毕 ⟹ C-64 定位**坐实**（非推翻）
   核心形式：两个量被混用 —— 𝒩（E118 定义，F_T=K_Y 无 x 权）与 𝓔（窗口二次型，带 x 权），𝓔 = N·𝒩
   ⟹ 第 5/6 项用 Y、第 7 项用 NY ⟹ 内部不一致，差因子 N（=x）
⚠️ 订正后：Σ_k 𝒩_k^corr = hN log²T/4π² ≫ hN ⟹ 得不出 o(hN) ⟹ 矛盾消失；非对角主导对角 ✓
⚠️ 三项复检：①点态自洽（|Δ|≈√N log N vs RH O(√N log²N) 同阶 ✓）；②与 SUPPORT-1 墙一致 ✓；
   ③定位更硬（第 5 项与 F_T 自身定义就不匹配）✓
⚠️ 订正 C-64 未及处：E118 §2 的"相干增益 √N/log³N" → 按修正为 √N log N（√N 级一致，log 幂次方向可疑 ⚠️）
✅ 净产出：①逐项核表（7/7）✓；②𝒩 vs 𝓔 混用的更硬形式 ✓；③定点订正与矛盾消解 ✓；④对 C-64 的补强与一处订正 ✓
```
