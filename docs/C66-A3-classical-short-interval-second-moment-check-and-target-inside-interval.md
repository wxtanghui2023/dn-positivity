已查地图：**逐档核对**（所查档：`E118`／`E119`／`C64`／`C65`（本会话前档）、`SUPPORT-1-WALL-IDENTIFICATION-closure.md`、`V219-moment-exponent-vs-zero-exponent-retraction-and-bridge-is-RH.md`、`EXPLORATION-POINTS-REGISTER.md`；关键词 `Saffari`（**0 档**）、`log(X/h)`（**0 档**）、`二阶矩渐近`（1 档＝`V219`，**不同对象** ⚠️）、`相干上界`（1 档＝`C-64`，本会话前档））。**结论**：经典短区间二阶矩渐近**不在档 ⟹ 属新外部输入** ✓；文献核 2 次**未确认** ⟹ **不据此下结论** ✗；**但 A3 的目的已由内部达成**：修正后真值**落在区间内部**，且目标 `o(hN)` **严格落在该区间内部** ⟹ 由 pair-correlation 决定 ✓

# C-66 · **A3 执行**：经典二阶矩渐近的档案/文献核 ＋ **目标落在区间内部**（内部达成）

> **时间**：2026-09-17 21:5x 唐先生「结果？」⟹ 给 A3 的结果（不新开方向 ✓）

---

## §0 结果（三条）

$$\textbf{① 档案回查}：\text{短区间二阶矩渐近}\ \textbf{不在档}\ ✓\（\texttt{Saffari}=0\ \text{档};\ \texttt{log(X/h)}=0\ \text{档};\ \text{命中 1 档的}\ \texttt{二阶矩渐近}\ \text{属}\ V219\ \textbf{另一对象}\ ⚠️\text{）}\ \Longrightarrow\ \textbf{新外部输入}\ ✓$$
$$\textbf{② 文献核（2 次检索，按纪律停）}：\text{找到 Saffari–Vaughan 1977 框架与"短区间平均"类文献，但}\ \textbf{未能确认}\ hX\log(X/h)\ \text{型渐近的确切陈述与适用范围}\ ✗\ \Longrightarrow\ \textbf{不据此下结论}\ ✗$$
$$\textbf{③ ⭐ A3 的目的已由内部达成}：\text{修正后（}`C\text{-}65`\text{）真值}\ \mathfrak E\ \text{落在}$$
$$\qquad\boxed{\underbrace{\frac{N\log N}{4\pi}}_{\text{典型／随机相位}\ [\text{启发}]}\ \lesssim\ \mathfrak E\ \lesssim\ \underbrace{\frac{hN\log^2T}{4\pi^2}}_{\text{满相干上界}\ [\text{推导}]\ ✓}}\qquad\text{而目标}\ o(hN)\ \textbf{严格落在此区间内部}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{目标成立}\iff\text{满相干被压制}\iff\text{pair-correlation 跨 support }1}\ ✓\ \text{—— 第 4 次收敛到同一缺口（与 }SUPPORT\text{-}1\ \text{一致）}$$

## §1 为何**不需要**那条文献也能得结论

$$\text{只需"上界"}：\mathfrak E\lesssim hN\log^2T\ \Longrightarrow\ \text{得不出}\ o(hN)\ \Longrightarrow\ \text{无无条件结论}\ ✓\（C\text{-}65\ \text{§2 已给）}$$
$$\text{文献渐近只能帮我们}\ \textbf{定位真值在区间内的位置}\ \text{（偏"典型"还是偏"相干"）}，\ \textbf{不改变结论方向}\ ✓$$
$$\textbf{故}：\text{A2（majorant 能否给 }o(hN)\text{）的预判}\ \textbf{不变}：\text{能与否}\iff\text{能否给出}\ \le o(hN)\ \text{的对偶正性上界};\ \text{而}\ W6\text{-MAJORANT}\ \text{（今日 12:53）已 FAIL 其中一条具体机制}\ ✓$$

## §2 ⚠️ 一处**同名不同物**登记（第二处标签冲突，防未来混淆）

| 名称 | 出现处 | 对象 |
|:--|:--|:--|
| **短区间二阶矩** | `E118`／`E119`／`C-64`／`C-65`／本档 | $\mathfrak E=\int_N^{N+Y}\lvert\psi(x+h)-\psi(x)-h\rvert^2dx$（**本线**）|
| **"二阶矩渐近"** ⚠️ | `V219` | $M_2$ 的**矩指数**桥：$\beta_*=\mu_2\iff$ RH（$M_q$ 的幂指数 vs 零点横坐标）—— **不同对象** |
$$\textbf{注}：V219\ \text{与本线}\ \textbf{独立同向}：\text{它也判}\ \text{"矩指数}\to\text{零点支撑"}\ \textbf{无非显式公式型的桥}\ ⟹\ \text{同一缺口的另一入口}\ ✓$$
$$\textbf{建议（纪律）}：\text{本线一律写"短区间二阶矩"或}\ \mathfrak E\ \text{记号};\ \text{不写"二阶矩渐近"}\ ✓\ \text{（第一处标签冲突：}Problem\ A\ \text{的}\ SQ1\text{–}SQ3\ \text{vs}\ V326\ \text{的}\ SQ1\text{--}SQ8\text{）}$$

## §3 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-17 21:5x）`[纪律]`

```
技术词 二阶矩渐近  命中文件数=1    :: ./V219-moment-exponent-vs-zero-exponent-retraction-and-bridge-is-RH.md
技术词 相干上界     命中文件数=1    :: ./C64-E118-E119-bookkeeping-conflict-candidate-localization-window-weight.md
技术词 目标落在区间内部 命中文件数=0    ::
```
**读数**：`目标落在区间内部`＝**0 档 ⟹ 本档新增** ✓；⚠️ `二阶矩渐近`＝**1 档（`V219`）**、`相干上界`＝**1 档（`C-64`）** ⟹ 均为**引用／同物**，**不列为本档提出** ✓；§2 的"同名不同物"登记为本档新增 ✓

## §4 边界

- `[推导]` 上界 $\mathfrak E\lesssim hN\log^2T/4\pi^2$（承 `C-65` §2）✓；`[启发]` 典型下沿 $N\log N/4\pi$（随机相位）⚠️
- **不声称**：经典渐近的确切形式（**文献核未确认** ✗）；不给新路线 ✓；不证 RH ✗；不修改原档 ✓
- **纪律**：外部检索**按上限停**（2 次）✓；未用 RH 作推导 ✓；零数值 ✓

```
⚠️ 任务＝A3（核经典短区间二阶矩渐近）
⚠️ 结果：①档案无 ⟹ 新外部输入 ✓；②文献核 2 次未确认 ⟹ 不下结论 ✗（按纪律停）；
   ③⭐ 目的内部达成：真值 ∈ [N log N/(4π)（典型，[启发]）, hN log²T/(4π²)（相干上界，[推导]）]，
      目标 o(hN) 严格落在区间内部 ⟹ 成立 ⟺ 满相干被压制 ⟺ pair-correlation 跨 support 1（第 4 次同址）
⚠️ 顺带：A2 预判不变（给不出 o(hN)），与 W6-MAJORANT FAIL 同向
⚠️ 登记第二处"同名不同物"：本线"短区间二阶矩 𝓔" vs V219 的"二阶矩渐近 M₂ 矩指数桥"（独立同向）
✅ 净产出：①档案/文献核结论＋纪律停 ✓；②真值区间与"目标落内部"命题 ✓；③同名不同物登记 ✓
```
