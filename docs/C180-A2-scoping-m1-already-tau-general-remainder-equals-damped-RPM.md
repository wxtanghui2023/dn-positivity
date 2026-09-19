已查地图（**先查后写**）：`papers/palojarvi-constant/note.md`（§2 应用／§3 m≥2 缺口）、`docs/E4-ENGINE-2`（引理 C ＋ 常数改善）、`docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf`（Theorem 4.1 逐字）、`WORKPLAN-...` A2 行、`RPM-LEMMA-CONJECTURE-LEDGER`（`D2d`）、四层台账第 3 层 `3D`。关键词回查：`可做部分结案`=0、`依赖外部开放项`=0、`τ-一致性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 20:16「继续」）**：`A2 = T6` —— τ-Li／Palojärvi 显式无零区（一般 τ）。
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{A2 的"可做部分"}\ \textbf{早已完成}：\text{我方}\ m=1\ \text{的常数改进}\ \textbf{对一切}\ \tau>1/e\ \textbf{成立}✓✓$$
$$\qquad \text{源文 Theorem 4.1 本身就是}\ \textbf{一般}\ \tau>1/e\ \text{（逐字已核）}；\text{我方阈值}\ 4(K_{F,1}(\tau)+K_{F,2}hmm\ K_{F,4}(\tau))n\log n+2\ \text{逐字含}\ \tau✓$$
$$\qquad \text{改善}\ (40\to4；\text{去掉}\ 20n\log n)\ \textbf{与}\ \tau\ \textbf{无关} \Longrightarrow \text{注记的声明}\ \textbf{已是}\ \tau\text{-一致的}✓✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{A2 的真正剩余}\ \equiv\ \textbf{阻尼版}\ (\text{RP}_M)\ \equiv\ \text{Montgomery Lemma 2.2}\ \text{本体}✓$$
$$\qquad \text{即：}\max_j|z_j|=1\Rightarrow\max_{1\le n\le5M}\Re\sum_j z_j^n\ge\tfrac1{20}（\text{常数}）✓\ \text{—— 我方}\ \textbf{只做了单模情形}（|z_j|=1\ \forall j）✓$$
$$\qquad \Longrightarrow \text{该剩余}\ \textbf{不是新缺口}：\text{它}\ \textbf{就是} \text{台账}\ \text{`D2d`}\ \text{／第 3 层}\ \text{`3D`}\ \text{（阻尼情形最优常数，数值}\ 0.36\text{–}0.40）✓✓$$
$$\textbf{(三)}\ \Longrightarrow\ \textbf{处置}：A2\ \text{就"可做部分"}\ \textbf{结案}；\text{剩余}\ \textbf{依赖外部开放项}（\text{`D2d`}）✓$$
$$\qquad \text{不再为 A2 单独立项} ⟹ \text{避免同一缺口被重复计数}（\text{与地图纪律一致}）✓✓$$

FREEZE-ACK: 本档即冻结期内的范围核实与登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **A2 范围核实（m=1 已 τ-一致）＋ 剩余归并到阻尼 (RP_M)（=D2d）＋ 计划表处置** —— 关系 = 范围核实与归并，非新机制
D1: 0

# C-180 · A2 范围核实：`m=1` 已 τ-一致；剩余 = 阻尼 `(RP_M)`

> **唐先生 2026-09-19 20:16**：继续（A2）✓

---

## §1 源文 Theorem 4.1 的参数域（逐字已核）

$$\text{源文（本地 PDF，Theorem 4.1）}：\ "\text{Let}\ \tau>\tfrac1e\ \text{be a real number}\ \dots\ \text{Suppose that the function}\ F(s)\ \text{has}\ \textbf{at most one zero}\ \rho_1\ \text{with}\ |\rho_1/(\rho_1-\tau)|>1."✓$$
$$\Longrightarrow \text{源定理}\ \textbf{本身即一般}\ \tau\ \text{（}\tau>1/e\text{）}；\ \text{其阈值}\ N\ \text{的}\ 12\log(40(0.5+K_{F,1}(\tau)+K_{F,4}(\tau)))/\log R\ \text{槽位}\ \text{逐字含}\ \tau✓$$
$$\qquad \text{（PDF p.18–21 原文；Corollary 5.2 亦复述同式）✓$$

## §2 我方改进的 τ-一致性

$$\text{我方（}\text{`E4-ENGINE-2`}\ §2／注记 §2）}：\text{阈值}\ R^n\ \ge\ 4\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)n\log n+2✓$$
$$\qquad \text{推导只用到：}\text{引理 C（}\max_{k\le5}\Re z^k\ge\tfrac12\text{，}\textbf{无}\ \tau）＋|w_\rho|\le1\iff\Re\rho\le\tau/2✓$$
$$\qquad \text{常数改善}\ (40\to4；\text{省}\ 20n\log n)\ \text{全部来自}\ \tfrac1{20}\to\tfrac12\ \Longrightarrow \textbf{与}\ \tau\ \textbf{无关}✓✓$$
$$\Longrightarrow \text{注记的声明}\ \textbf{已覆盖一切}\ \tau>1/e \Longrightarrow \textbf{A2 的"可做部分"=\ 已完成}✓✓$$

## §3 真正剩余：阻尼 `(RP_M)`

$$\text{源文在}\ m\ge2\ \text{（多个例外零点）时需要的正是}\ \text{Montgomery Lemma 2.2}\ \textbf{的实部检测}：$$
$$\qquad \max_j|z_j|=1\ \Longrightarrow\ \max_{1\le n\le5M}\Re\sum_{j=1}^M z_j^n\ \ge\ \tfrac1{20}✓$$
$$\qquad \text{我方}\ (RP_M)\ \text{系列只覆盖}\ \textbf{单模}（|z_j|=1\ \forall j）✓；\textbf{阻尼}（允许\ |z_j|<1）\ \text{未证}✗$$
$$\Longrightarrow \text{该剩余}\ \textbf{与}\ \text{台账}\ \text{`D2d`}\ \text{／第 3 层}\ \text{`3D`}\ \textbf{是同一件事}（\text{数值}\ d_M\approx0.36\text{–}0.40\ \text{vs}\ \tfrac1{20}）✓✓$$
$$\qquad \text{注记}\ §3\ \text{已有的两条路线}：\text{(a) Fejér 权路线（需"模可比"假设）；\text{(b) 仍引 Montgomery}✓$$

## §4 处置与计划表更新

$$\textbf{①}\ A2\ \text{就"可做部分"}\ \textbf{结案}（m=1、一般 τ、常数改善均已在注记中）✓$$
$$\textbf{②}\ \text{剩余归并到}\ \text{`D2d`/`3D`}，\textbf{不重复立项}✓\（\text{避免同一缺口双计}）✓$$
$$\textbf{③}\ \text{注记可加一句明确}\ \tau\text{-一致性}（\text{建议措辞}："\text{the improvement is \tau-uniform for all}\ \tau>1/e,\ \text{as in the source}")✓$$
$$\textbf{④}\ \text{下一项按计划}：\text{A3}\ (=\text{T2 密度猜想})✓$$

## §5 边界

- ⚠️ §1／§2 均基于**逐字核对**（源文 PDF 与 `C-67` 式引用纪律一致）✓
- ⚠️ §3 的"剩余＝阻尼 (RP_M)"是**归并判断**（非新定理）：依据是源文在 `m\ge2` 处对实部检测的需求 ✓
- ⚠️ 本档**不声称**任何关于阻尼情形的新结论 ✓
- **未用** RH；**未改**注记正文（仅建议措辞，未落笔）✓
- **纪律**：先查后判 ✓（本档即为"先查"的产物：查完才发现可做部分早已完成）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 20:1x）`[纪律]`

```
技术词 可做部分结案   命中文件数=0 ::  ⟹ 本档新增
技术词 依赖外部开放项  命中文件数=0 ::  ⟹ 本档新增
技术词 τ-一致性      命中文件数=0 ::  ⟹ 本档新增
```
