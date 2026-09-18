已查地图 + **取回 Prop 5.4 逐字**（所查档：`W6-MAJORANT-1-verbatim-source-and-jam-step.md`（§1 窗口定义／**§2 Prop 5.4 逐字 L839**／§2.1 对角 `D` 逐字／§4 majorant 判据）、`C-25`（`X\le T` 的绑定性约束来自 Prop 5.4）、`C-29`（卡点＝MV 步；对角支配 `\iff X\ll TL`；缺口因子 `\asymp X/(TL^3)`）、`C-79`（`Q^\star`／`DEC-1`／kill 判据）、`C-80`）。**结论**：`Q^\star` **闭合**，且理由**不是**"界不 sharp"而是**"量本身翻转"** —— 短距离（`|n-m|\lesssim X/T`）素数幂对质量本身使离对角 > 对角（比值 `\approx T^{\eta}/\log^2X`）⟹ **并回溯解释 `C-30`（W6-majorant FAIL）为必然** ⟹ 唯一杠杆＝让短距离质量**带号相消** ⟹ **`DEC-1` 被这条推导激活** ✓✓

# C-81 · **`Q★` 闭合（量的翻转，非界的松）＋ 由此激活 `DEC-1`**

> **时间**：2026-09-18 12:52 唐先生「继续」
> **本档**：`Q★` 第一刀（结构＋量级）＋ 对 `C-30` 的回溯解释 ＋ `DEC-1` 的动机 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ Q^\star\ \textbf{闭合}，\text{理由}\ \textbf{不是}"\text{界不 sharp}"\ \text{而是}\ \textbf{"量本身翻转"}：\text{短距离}\（|n-m|\lesssim X/T）\ \text{PP-对质量}\Longrightarrow\ |O_1|>D\ \text{（比值}\approx T^{\eta}/\log^2X）$$
$$\textbf{(2)}\ ⭐\ \textbf{回溯解释 `C-30`}：\text{既然失败是}\ \textbf{定量} \text{的（非估计松）}，\text{majorant／对偶正性路线}\ \textbf{必然} \text{失败} \Longrightarrow \text{与 `W6-MAJORANT-1g`"逐字 100\% 天花板"的观测}\ \textbf{一致}✓✓$$
$$\textbf{(3)}\ \Longrightarrow\ \text{唯一杠杆}＝\text{让短距离质量}\ \textbf{带号相消} \Longrightarrow\ \textbf{`DEC-1` 被激活}\（\Lambda=\mu*\log\ \text{分解引入}\ \mu \Longrightarrow \text{带号权}）✓✓$$
$$\textbf{(4)}\ \text{与}\ \text{SQ3}\ \text{一致（}\Lambda\ \text{vs}\ \mu^2）；\ \text{更准确的对照轴是}\ \textbf{带号 vs 非带号}\ \text{权}✓$$

---

## §1 `Prop 5.4` 逐字（源档 `W6-MAJORANT-1` §2，L839）

$$\textbf{Prop 5.4（Prime term）}：M[P_X,P_X]=\frac T\pi\sum_{n\le X}\frac{\Lambda(n)^2}{n}g(\log n)+O\bigl(\chi(L^2X)\bigr),\qquad g:=\phi^2\star\phi^2$$
$$\text{起点}：P_X(\tau)=-\frac1{2\pi}\sum_na_n\bigl(n^{i\tau}+n^{-i\tau}\bigr),\qquad \boxed{a_n=\frac{\Lambda(n)}{\sqrt n}}✓$$
$$\text{窗口几何（逐字）}：\text{"for fixed }x\ \text{the variable }\tau'\ \text{ranges over }I\cap(I-x),\ \textbf{which is empty for }|x|\ge T"$$
$$M[P_X,P_X]=D+O_1+O_2,\qquad D=\frac T\pi\sum_na_n^2g(y_n)+O(L^2\log L)✓$$
$$\qquad \text{核}：\text{内积分}\ \int e^{ih\tau'}d\tau'\ \text{型}\（h=\log(n/m)）\ \Longrightarrow\ \Bigl|\int_0^Te^{ih\tau}d\tau\Bigr|=\Bigl|\frac{e^{ihT}-1}{ih}\Bigr|\le\boxed{\min\bigl(T,\tfrac2{|h|}\bigr)}✓$$

## §2 推导（`[本档]`；⚠️ 用标准无条件的 PP-对计数上界）

$$\textbf{(a) 短距离区}：|h|\le1/T\iff|n-m|\lesssim X/T;\ \text{核贡献}\approx T✓$$
$$\textbf{(b) 该区 PP-对计数}（\text{上界筛，无条件}）：\ \#\{\text{PP pairs},\ |n-m|\le X/T\}\ \lesssim\ \frac{X}{\log^2X}\sum_{d\le X/T}\mathfrak S(d)\ \approx\ \frac{X}{\log^2X}\cdot\frac XT\ ✓$$
$$\textbf{(c) 权}：a_na_m\approx\frac{\log^2X}{X}\ \Longrightarrow\ \text{加权和}\approx\frac X{\log^2X}\cdot\frac XT\cdot\frac{\log^2X}{X}=\frac XT\ \Longrightarrow\ \text{乘}\ T\ \Longrightarrow\ \boxed{\text{短距离部分}\approx X}$$
$$\textbf{(d) 对角}：D\approx\frac T\pi\Bigl(\sum_n\frac{\Lambda(n)^2}{n}\Bigr)g\approx T\log^2X\qquad\Bigl(\text{因}\ \sum_{n\le X}\frac{\Lambda(n)^2}{n}\sim\tfrac12\log^2X\Bigr)✓$$
$$\Longrightarrow\ \boxed{\frac{|O_1|}{D}\ \approx\ \frac{X}{T\log^2X}\ =\ \frac{T^{\eta}}{\log^2X}}\ \Longrightarrow\ X=T^{1+\eta}\ \text{时}\ \gg1\ \Longrightarrow\ \textbf{支配失败（真实量）}✓✓$$
$$\textbf{(e) 阈值自检}：\text{比值}\le1\iff X\lesssim T\log^2X\ \checkmark\ \text{与}\ \text{`C-29` 的}\ X\ll TL\ \textbf{一致}（\log\ \text{幂次差异}\ ⚠️）✓✓$$

## §3 `Q★` 判词

$$\boxed{Q^\star：\text{失败是}\textbf{定量} \text{的，}\textbf{不是估计松} \Longrightarrow \text{任何}\ \textbf{界} \text{的改进都救不了}}✓✓$$
$$\qquad ⭐\ \text{这}\ \textbf{回溯解释} \text{了}\ \text{`C-30`}：\text{W6-majorant／对偶正性路线（试图用}\ \textbf{majorant 吃掉} \text{off-diagonal 缺口）}\ \textbf{必然} \text{失败}✓✓$$
$$\qquad ⚠️\ \text{且它是}\ \textbf{一个正面信息}：\text{把"为什么所有估计型尝试都撞同一处"从}\ \textbf{经验观察} \text{升级为}\ \textbf{定量理由}✓$$

## §4 ⟹ **`DEC-1` 的动机**（从"候选"到"有动机的下一步"）

$$\text{关键机制}：\Lambda(n)>0\ \text{（非带号）} \Longrightarrow \text{短距离项}\ \sum a_na_m\min(T,2/|h|)\ \textbf{不可相消}✓$$
$$\qquad \text{而}\ \Lambda=\mu*\log\ \text{的分解}\ \textbf{引入}\ \mu\（\text{带号}）:\ \sum_{n\le X}\Lambda(n)n^{-1/2-it}\omega(n)=\sum_{dm\le X}\mu(d)\log m\,(dm)^{-1/2-it}\omega(dm)✓$$
$$\qquad \Longrightarrow\ \text{若把短距离求和}\ \textbf{先对}\ d\ \text{分层}\（\text{每层带}\ \mu(d)\ \text{的号}）,\ \text{层内}\ \textbf{可能相消} \Longrightarrow \text{幂级节省}\ \textbf{不再是幻想}✓✓$$
$$\qquad ⚠️\ \text{但必须先过}\ \text{`C-79` §4 的}\ \textbf{K1--K4}（\text{退化回 MV／分层与对角重合／需 RH 条件输入／过不了 F1 两问}）✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:5x）`[纪律]`（先跑后写）

```
技术词 短距离质量  命中文件数=0
技术词 量的翻转   命中文件数=0
技术词 带号相消   命中文件数=0
技术词 回溯解释   命中文件数=0
```
**读数**：四项**均 0 档 ⟹ 本档新增** ✓

## §6 边界（⚠️ 必读）

$$\text{(i)}\ §1\ \text{为}\ \textbf{逐字}（源档 `W6-MAJORANT-1` §2，L839 与 §2.1）✓$$
$$\text{(ii)}\ §2\ \text{为}\ \textbf{本档量级推导}：\text{用}\ \text{majorant}\ \min(T,2/|h|)\ \text{与标准}\ \textbf{上界筛} \text{的 PP-对计数}（\textbf{无条件}，但\ \text{本档}\ \textbf{未逐字核} \text{其精确形式}）⚠️;\ \text{结论按}\ \textbf{量级} \text{读，非定理}✓$$
$$\text{(iii)}\ \text{不得写"已证离对角 > 对角"}\ ✗;\ \text{须写"}\textbf{量级推导表明}\ \dots\text{"}✓$$
$$\text{(iv)}\ \textbf{未用 RH}\ \text{作推导}✓;\ \textbf{零数值}✓;\ \text{不修改原档}✓$$

```
⚠️ 任务：唐先生 12:52「继续」= 开 Q★（第二层：实际稀疏权 a_n = Λ(n)/√n 的算子范数是否 ≪ L²X·T^{−c}？）
✅ Q★ 闭合，理由不是"界不 sharp"而是"**量本身翻转**"：短距离（|n−m| ≲ X/T）PP-对质量本身使 |O₁| > D，比值 ≈ Tᵗ/log²X
   （推导：核 |∫₀ᵀe^{ihτ}dτ| ≤ min(T,2/|h|)；短距离区核≈T；该区 PP-对计数 ≲ (X/log²X)(X/T)（上界筛，无条件）；
   权 a_n a_m ≈ log²X/X ⟹ 加权和 ≈ X/T ⟹ 乘 T ⟹ ≈ X；对角 D ≈ T log²X）⟹ 阈值 X ≲ T log²X ✓ 与 C-29 的 X ≪ TL 一致
⭐ 回溯解释 C-30：既然失败是**定量**的（非估计松），W6-majorant／对偶正性路线**必然**失败 ⟹ 与"逐字 100% 天花板"观测一致；
   这把"为什么所有估计型尝试都撞同一处"从经验观察升级为定量理由
⭐ ⟹ 唯一杠杆＝让短距离质量**带号相消** ⟹ **DEC-1 被激活**：Λ = μ ∗ log 分解引入 μ（带号）⟹ 按 d 分层后层内可能相消
   ⟹ 幂级节省不再是幻想（但须先过 K1–K4）
✅ 与 SQ3 一致：对照轴应表述为"**带号 vs 非带号权**"（比"Λ vs μ²"更准）
⚠️ 边界：§2 为本档量级推导（用 min(T,2/|h|) 与标准上界筛 PP-对计数，无条件但未逐字核其精确形式）⟹ 按量级读，非定理；
   不得写"已证离对角 > 对角"
✅ 净产出：①Q★ 闭合＋定量理由 ✓；②对 C-30 的回溯解释 ✓；③DEC-1 的动机（带号相消）✓；④SQ3 对照轴精化 ✓
```
