已查地图（**先查后写**）：查 `C-230`（最终闭合）、`C-229`（勘误＋覆盖修补）、`papers/damped-M3-theorem/note.md`（审计档）、`papers/damped-M3-theorem/main.tex`（英文正式版）。回查见 §6 ✓

D0: 本档对象 = **甲线冻结登记**（T13-Damped-M3: FROZEN）—— 关系 = 状态登记，非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的状态登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 冻结论断

$$\boxed{\textbf{T13-Damped-}M3:\ \textbf{FROZEN}}✓✓$$
$$\qquad \text{冻结依据}：\textbf{定义}\to\textbf{Lemma 1--5}\to\textbf{Theorem A}\ \text{已闭合}✓,\ \text{依赖 DAG 已审计}✓,\ \text{英文正式版已编译通过}✓$$

## §1 冻结资产清单

| 资产 | 路径 | 状态 |
|---|---|---|
| 英文正式版（Theorem A ＋ Lemma 1–5 ＋ 复现 ＋ caveat） | `papers/damped-M3-theorem/main.tex` | ✓ 9 页，`pdflatex` 0 错误 0 未定义引用 |
| 编译产物 | `papers/damped-M3-theorem/main.pdf` | ✓ 305 KB |
| 自洽审计档（定义逐字／DAG／证书表） | `papers/damped-M3-theorem/note.md` | ✓ 373 行 |
| 论文 A 并入（§8.2 ＋ 结果表行 7 ＋ §9 复现表） | `papers/rpM-window-cosines/main.md` | ✓ 595 行 |
| 证书脚本（4 个） | `scripts/dB_krawczyk_11.py`／`dB5_local_growth_5d.py`／`dC2iv_strict.py`／`dC2par_parallel_iv.py` | ✓ |
| 决策链文书 | `C-224`→`C-226`→`C-227`→`C-228`→`C-229`→`C-230` | ✓ |

## §2 冻结后的措辞铁律（防口径混淆 ✓）

$$\textbf{禁止}✗：\text{"The }S_3\text{-orbit consists of two minimizers."}$$
$$\textbf{必须}✓：\text{"The minimizer set in the normalized domain }\Omega\text{ consists of the two points }z_*,\sigma z_*.\ \text{The corresponding raw permutation orbit contains six configurations, whose images under the normalization map }\mathcal N\text{ reduce to these two points."}$$
$$\qquad \text{依据}：**Remark 1.1 ＋ Proposition 8.1**（主文 ✓）＋ **Remark 8.2**（审计档 ✓）$$

## §3 冻结后的两条“不可删”公式（唐先生 2026-09-20 18:00 指定 ✓）

$$\textbf{① 扩展形式}✓（解释 Lemma 1 的 tie 是 Lemma 4 的唯一逻辑消费点 ✓）：$$
$$\qquad F(x+\delta)\ \ge\ F(x)-\delta_A(x)+c_X\|\delta\|-\tfrac R2\|\delta\|^2✓\qquad（\text{主文}\ \eqref{eq:spreadform}✓）$$
$$\qquad \delta_A(z_*)=0✓\ \text{来自 Lemma 1 的唯一性} \Longrightarrow \text{条件式无条件化}✓$$
$$\textbf{② 自洽条件}✓（把 reference-ball 自洽从实现细节升为【证明条件】✓）：$$
$$\qquad \rho_{\rm data}\ \ge\ \rho_g+\hd(X_0)✓\qquad（\text{主文}\ \eqref{eq:selfcons}✓）$$
$$\qquad \text{本例}：2.05\times10^{-3}\ge1.9782244\times10^{-3}+10^{-21}✓；\text{并如实记录初稿违反该条件被弃}✓$$

## §4 冻结后的维护规则

$$\textbf{① 仅在发现【数学错误】时才改动}✓（\text{措辞润色、格式调整不在其列}✓）$$
$$\textbf{② 不得因后续路线需要而回改甲线结论}✓（\text{若后续需要更弱/更强版本，另立新档并显式引用甲线}✓）$$
$$\textbf{③ 任何改动须留勘误指针}✓（\text{append 而非覆盖}✓，依项目协议 ✓）$$
$$\textbf{④ 未决项（不改结论）}：\text{facet 法向 float SVD}⚠️（10^{-15}\ll\varepsilon_{\rm pert}\approx0.203✓）；\text{体积精确核对（可选）}✓$$

## §5 下一刀候选（本档只登记，不启动 ✓）

$$\text{唐先生 18:00 指定方向}✓：\textbf{由 }M=3\ \text{的六路 active-set 结构抽象出的结构性猜想/引理}✓（\text{不机械算 }M=4✓）$$
$$\qquad \textbf{留下的新数学信息不是小数 }0.3730918928958164\ldots✓，\text{而是}：$$
$$\qquad \boxed{\text{5 个构型自由度}\quad\longrightarrow\quad\text{6 个正权 active branches}}✓\qquad（\text{即 }|A|=n+1\ \text{的单纯形签名}✓）$$
$$\qquad \text{以及与【全局最小化】、【归一化商结构】之间的关系}✓$$

## §6 边界

$$\textbf{① 本档为登记}✓，\text{不含新数学}✓；\textbf{② 未用 RH}✓；\textbf{③ 未改他档}✓（\text{主图指针见 §7}✓）$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 冻结登记           命中文件数=1  ::  ./C231-T13-Damped-M3-FROZEN-registration.md
技术词 单纯形签名推广     命中文件数=1  ::  ./C231-T13-Damped-M3-FROZEN-registration.md
技术词 措辞铁律           命中文件数=1  ::  ./C231-T13-Damped-M3-FROZEN-registration.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
