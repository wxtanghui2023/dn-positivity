已查地图 + **外取逐字**（所查档：`C-78`（`SQ1` 判定与"余量 ≲1.5 倍"）、`C-79`（`Q★`／`DEC-1`）、`Hilbert 不等式`族档案记录（`E4-ENGINE-*`：`加权 Hilbert 不等式 ＝ [MV74, Thm 2]`）；**外取**：`Yangjit` 学位论文（`deepblue.lib.umich.edu` 全文 PDF）、`arXiv:2203.14950`（`scixplorer` 摘要）、`mathoverflow.net/questions/444337`（转述 `Preissmann` 与插值优化）、`arXiv:2608.12315`（Rodgers 摘要））。**结论**：接受唐先生的历史补正，但**需再收紧一格**——`Yangjit` 的 `3.19497` 是**方法族（parametric family）下界＝方法学障碍**（原文："this method … is **incapable of proving** `c₁ = π`"），**不是**"最优常数 `> π`"的证明；**后者确为 Rodgers 2026 首次严格给出** ✓✓

# C-80 · **历史链补正**：Schur → MV → Preissmann → **Yangjit（方法族下界）** → Rodgers

> **时间**：2026-09-18 12:49 唐先生指出 `Yangjit 2022`（`arXiv:2203.14950`）已给出 `3.19497` 下界、"无法达到猜想常数 `π`"，要求把完整历史写进综述笔记
> **本档**：逐字取回 ＋ 两层区分 ＋ 对 `C-78` 的两处精化 ✓

---

## §0 结论（先行）

$$\textbf{① 链条（本档逐字核实）}：\text{Schur 1911（经典 Hilbert 的}\ \pi\ \text{是 sharp）} \to \text{MV 1974（加权版**猜测**}\ \pi;\ C\le\tfrac32\pi）\to \text{Preissmann 1984（}\tfrac43\pi）$$
$$\qquad \to \textbf{Yangjit 2022/23}（\text{参数族**方法**到不了}\ \pi;\ \text{下界}\ \mathbf{3.19497}）\to \textbf{Rodgers 2026}（\textbf{严格证明最优常数}\ >\pi）✓✓$$
$$\textbf{② ⚠️ 需再收紧一格（比唐先生表述更紧）}：\text{Yangjit 的}\ 3.19497\ \text{是}\ \textbf{方法族下界}：\text{原文逐字"}\textbf{this method}\ \text{in its current form cannot achieve any value below}\ 3.19497,\ \text{so cannot achieve the conjectured constant}\ \pi\text{"}$$
$$\qquad \Longrightarrow\ \textbf{不是}"\text{最优常数}>\pi"\ \text{的证明},\ \text{而是}"\textbf{那条参数族路线}\ \text{证明不了}\ \pi"\ \text{（方法学障碍）}✓✓$$
$$\textbf{③ 附加发现（本档）}：\text{Yangjit 第 2 章还}\ \textbf{证明了带常数}\ \pi\ \text{的广义 Hilbert 不等式} \Longrightarrow \pi\ \text{在}\ \textbf{某个广义形式下可达}✓$$
$$\textbf{④ 对 `C-78` 的余量区间精化}：\text{MV}\ \tfrac32\pi\approx4.7124\ \big|\ \text{已知下界}\ 3.19497 \Longrightarrow\ \text{余量}\ \le1.475\times;\ \text{已证上界}\ 1.28\pi\approx4.0212\ \Longrightarrow\ \ge1.172\times\ ⚠️$$

---

## §1 逐字（三处）

$$\textbf{(1)}\ \text{Yangjit（学位论文／`arXiv:2203.14950` 摘要）}\ \textbf{逐字}：$$
$$\qquad\text{"…We consider an approach pursued by previous authors via a}\ \textbf{parametric family of inequalities}.\ \text{We obtain upper and lower bounds for the constants in inequalities in this family.}\ \text{A lower bound at}\ \alpha=\tfrac12\ \text{indicates that}\ \textbf{the method in its current form cannot achieve any value below}\ \mathbf{3.19497},\ \text{so cannot achieve the conjectured constant}\ \pi.\text{"}$$
$$\qquad\text{"From Theorem 1.2.10, we deduce that any upper bound for}\ c_1\ \text{obtainable by Theorem 1.2.6 cannot be smaller than}\ 3.19497.\ \text{It follows that}\ \textbf{this method of using Theorem 1.2.6 is incapable of proving}\ c_1=\pi.\ \text{In Chapter 2, we also prove a}\ \textbf{generalized Hilbert inequality with the constant}\ \pi.\text{"}$$
$$\textbf{(2)}\ \text{`mathoverflow 444337` 转述（}\textbf{非一手} ⚠️\text{）}：\text{Preissmann 证明可经插值优化为}\ \|B\|_{2,2}\le(3\|D\|_{3,3})^{1/2}\le(3\pi\|C\|_{2,2})^{1/3}\le\pi(1+(6/5)^{1/2})^{1/3}\le\mathbf{1.28\pi};\ \text{另有}\ \|C\|_{2,2}>\pi^2/3✓$$
$$\textbf{(3)}\ \text{Rodgers（`arXiv:2608.12315`）}\ \textbf{逐字}：\text{"…the optimal constant … is}\ \textbf{strictly greater than}\ \pi,\ \text{answering in the negative a question asked by Montgomery and Vaughan.}\ \text{The proof proceeds via an}\ \textbf{explicit limiting counterexample}.\text{"}✓$$

## §2 对 `C-78` 的两处精化

$$\textbf{(a)}\ \textbf{历史链}（`C-78` §1 只列了 MV／Preissmann／Rodgers）\ \Longrightarrow\ \text{补入}\ \textbf{Schur 1911} \text{与}\ \textbf{Yangjit 2022/23}✓$$
$$\textbf{(b)}\ \textbf{余量区间}（`C-78` §0(ii) 写"总余量\ \lesssim1.5\ \text{倍}"）\ \Longrightarrow\ \text{精确化为区间}：$$
$$\qquad \text{上端}：\text{MV}\ \tfrac32\pi=4.71239\ \text{vs 已知下界}\ 3.19497 \Longrightarrow\ \textbf{余量}\ \le1.475\times✓$$
$$\qquad \text{下端}：\text{MV}\ \tfrac32\pi\ \text{vs 已证最优上界}\ 1.28\pi=4.02124 \Longrightarrow\ \textbf{余量}\ \ge1.172\times\ ⚠️（1.28π 为 MO 转述，待一手核）✓$$
$$\qquad \Longrightarrow\ \text{结论不变}：\text{余量}\ \textbf{至多约 1.5 倍（常数级）} \Longrightarrow\ \text{补不了幂级缺口}✓✓$$

## §3 综述笔记的历史段落（供成文，按唐先生要求写全）

$$\text{①}\ \textbf{Schur (1911)}：\text{经典 Hilbert 不等式}\ \bigl|\sum_{r\ne s}u_r\bar u_s/(r-s)\bigr|\le\pi\sum|u_r|^2\ \text{的常数}\ \pi\ \textbf{sharp}✓$$
$$\text{②}\ \textbf{Montgomery–Vaughan (1974)}：\text{J. London Math. Soc. (2)}\ \mathbf 8,\ 73\text{--}82;\ \text{加权推广}\（\lambda_r-\lambda_s\ \text{核};\ \text{另有}\ \csc\ \text{版带}\ \delta^{-1}）;\ C\le\tfrac32\pi;\ \textbf{猜测最优}＝\pi✓$$
$$\text{③}\ \textbf{Preissmann (1984)}：\text{Enseign. Math.}\ \mathbf{30},\ 95\text{--}113;\ \text{改进到}\ \tfrac43\pi;\ \text{可经插值再优化（}\le1.28\pi\ ⚠️\text{）};\ \text{另 Preissmann--Leveque (2013) Pacific J. Math.}\ \mathbf{265},\ 199\text{--}219✓$$
$$\text{④}\ \textbf{Yangjit (2022/23)}：\text{arXiv:2203.14950 ＝ PAMS Series B}\ \mathbf{10}\ (2023)\ 439\text{--}454;\ \textbf{参数族方法的障碍}：\text{下界}\ 3.19497 \Longrightarrow \text{该路线证不了}\ \pi;\ \text{并给出带常数}\ \pi\ \text{的广义形式}✓$$
$$\text{⑤}\ \textbf{Rodgers (2026-08-12)}：\text{arXiv:2608.12315};\ \textbf{首次严格证明最优常数}\ >\pi（\text{显式极限反例}）✓$$
$$\qquad ⚠️\ \text{写法纪律}：\text{不得写成"Yangjit 已证最优常数}>\\pi"\ ✗;\ \text{必须写"}\textbf{方法族障碍／强证据}\text{"}✓✓$$

## §4 一处**层次澄清**（避免与 `C-79` 打架）

$$\text{唐先生说"`SQ1` 依然是死的"}\ \Longrightarrow\ \text{指}\ \textbf{第一层}（\text{一般 Hilbert 常数的余量＝常数级}）\ \checkmark\ \text{已闭}✓$$
$$\text{而 `C-79` 开的}\ \textbf{第二层}＝\text{"}\textbf{实际稀疏算术权}\ a_n=\Lambda(n)/\sqrt n\ \text{的算子范数是否}\ \ll L^2X\,T^{-c}\text{"}\ \Longrightarrow\ \textbf{仍开}✓✓$$
$$\qquad \Longrightarrow\ \text{两层}\ \textbf{不冲突}：\text{第二层问的不是"常数能否改进"，而是"}\textbf{这个权的真实大小}\ \text{是否远小于 MV 给的一般界}"✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 12:5x）`[纪律]`（先跑后写）

```
技术词 历史链     命中文件数=3    :: ./FRONTIER-PRIMEGAP-SURVEY-2026-09.md ./R-A8.4-err1-and-R8Cdag-first-cut.md ./REVIEW-20260916-from-one-wall-to-three-mechanism-classes.md
技术词 方法族下界  命中文件数=0
技术词 余量区间   命中文件数=0
技术词 Yangjit    命中文件数=0
```
**读数**：`方法族下界`／`余量区间`／`Yangjit`＝**0 档 ⟹ 本档新增** ✓；⚠️ `历史链`＝**3 档 ⟹ 档案已有**（通用词）⟹ 引用 ✓

## §6 边界

- `[逐字]` §1(1) Yangjit（学位论文 PDF ＋ 摘要）、§1(3) Rodgers ✓；§1(2) 为 **MO 转述** ⚠️（1.28π 待一手核）
- `[本档]` §0 的"方法族 ≠ 最优常数"区分、§2 精化、§3 历史段落、§4 层次澄清 ✓
- **不声称**：`Q★` 成立／不成立 ✗；1.28π 已核 ✗；不证 RH ✗；不修改原档（`C-78` 保留，精化另档）✓
- **纪律**：先查后判（R-1 ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 唐先生 12:49 补正：Yangjit 2022 (arXiv:2203.14950) 已给出 3.19497 下界、"无法达到猜想常数 π"，要求把完整历史写进综述笔记
⚠️ 逐字核实（Yangjit 学位论文 + 摘要）：**3.19497 是"参数族方法"的下界** —— 原文 "the method in its current form cannot achieve
   any value below 3.19497" / "this method of using Theorem 1.2.6 is **incapable of proving c1 = π**" ⟹ **方法学障碍**，
   不是"最优常数 > π"的证明（后者确为 Rodgers 2026 首次严格给出，且用显式极限反例）
⭐ 附加发现：Yangjit **第 2 章还证明了带常数 π 的广义 Hilbert 不等式** ⟹ π 在某个广义形式下**可达**
⚠️ 历史链（补正后）：Schur 1911（π sharp）→ MV 1974（猜测 π；C ≤ 3/2π）→ Preissmann 1984（4/3π；可插值优化至 ≤1.28π ⚠️MO 转述）
   → Yangjit 2022/23（参数族方法障碍；下界 3.19497）→ Rodgers 2026（严格证明最优 > π）
⚠️ C-78 余量区间精化：MV 3/2π=4.71239 vs 已知下界 3.19497 ⟹ ≤1.475×；vs 已证上界 1.28π=4.02124 ⟹ ≥1.172× ⟹ 结论不变（常数级，补不了幂级缺口）
⚠️ 层次澄清：唐先生"SQ1 依然是死的"＝第一层（一般常数余量，已闭）✓；C-79 开的第二层＝"实际稀疏权 a_n=Λ(n)/√n 的算子范数
   是否 ≪ L²X·T^{−c}" 仍开 ⟹ 两层不冲突（第二层问的不是"常数能否改进"，而是"这个权的真实大小是否远小于一般界"）
⚠️ 写法纪律：不得写成"Yangjit 已证最优常数 > π"；必须写"方法族障碍／强证据"
✅ 净产出：①历史链逐字补正 ✓；②"方法族下界 ≠ 最优常数"的收紧 ✓；③Yangjit Ch.2 的 π-可达发现 ✓；④余量区间精化 ✓；⑤层次澄清 ✓
```
