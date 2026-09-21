已查地图（**先查后写**）：`C-3850`（**Bridge A 首刀：奇型＝真新信息；M1–M5 过滤器** ✓✓）、`C-349`（**`F_{2r+1} = \int R_r\,d\mu_\sigma`；四矩小 ⟹ 近抵消** ✓✓）、`C-350`（**§0⑤：矩映射在权重趋零／碰撞处秩掉 ⟹ 统一常数不可得** ⚠️✓）、`C-369`（**碰撞层闭合：`\mathcal D_{\mathrm{coll}} \cap E = \varnothing`；⚠️措辞纪律：只能写「碰撞部分的 `\mathcal Z \cap E` 已排除」** ✓✓）、`C-3849`（**`\delta_* > 0` 资产** ✓✓）、`C-346`（**目标 `\inf\max_{r \le 12}|F_{2r+1}| > \tfrac12`** ✓✓）、`C-355／C-356`（**分层记号** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-51：Quantitative Odd-Moment Injectivity —— 首档只做 A（Jacobian rank）＋ B（uniform minor）**（唐先生 2026-09-21 21:23 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 档位（唐先生令）}✓✓：\text{C-3851 首档}\ \textbf{只做 A＋B}✗✓；\ \textbf{不}提前投入 C（定量逆）／D（Bridge B）✗✓；\ \text{A／B 若失败} \Longrightarrow \text{判该型 NO-GO}✓✓$$

$$\textbf{② ⭐ A（秩定理，精确成立）}✓✓：\ \text{令}\ c_j := \sqrt{x_j} > 0✓,\ \phi_j := \arccos c_j✓,\ \sigma \in \{\pm1\}^5✓,\ G_r = \sum_j\sigma_jT_{2r+1}(c_j)\ (r = 0..3)✓✓$$

$$\qquad \frac{\partial G_r}{\partial x_j} = \sigma_j\frac{(2r+1)U_{2r}(c_j)}{2c_j}✓✓\ \text{（数值核验：有限差分 vs 闭式}\ 6.9\times10^{-10}✓✓） \Longrightarrow\ \boxed{DG = \operatorname{diag}(\sigma)\,U^{\top}}✓✓$$

$$\qquad \text{记}\ U_{2r}(c) = Q_r(c^2)✓（Q_r\ \text{为}\ x\ \text{的}\ r\ \text{次多项式，首项系数}\ 4^r✓） \Longrightarrow\ \operatorname{rank}DG = \operatorname{rank}\big[Q_r(x_j)\big]✓✓$$

$$\qquad \Longrightarrow\ \boxed{\operatorname{rank}DG(x,\sigma) = \min\big(4,\ \#\{\text{distinct } x_j\}\big)}✓✓\ \text{（对一切}\ \sigma✓）$$

$$\qquad \textbf{理由}✓✓：\sum_r a_rQ_r(x)\ \text{为次数} \le 3\ \text{的多项式}✓ \Longrightarrow \text{它在}\ 4\ \text{个互异点消失} \iff a \equiv 0✓✓$$

$$\qquad \textbf{数值确认}✓✓：5\ \text{互异} \to \operatorname{rank}4✓；1\ \text{重}（4\ \text{互异}） \to \operatorname{rank}4✓；2\ \text{重}（3\ \text{互异}） \to \operatorname{rank}3✓✓\ \text{—— 与预测完全一致}✓✓$$

$$\qquad \Longrightarrow\ \boxed{\text{无碰撞} \Longrightarrow \operatorname{rank}DG = 4}✓✓\ \text{（C-350 §0⑤ 的"秩掉"障碍在无碰撞处}\ \textbf{不存在}✓✓）$$

$$\textbf{③ ⭐ B（闭式 ＋ 统一 minor，显式常数）}✓✓：\text{对任意}\ 4\ \text{列子集}\ \hat j \subset \{1..5\}✓,\ |\hat j| = 4✓：$$

$$\qquad \boxed{\big|\det DG_{\hat j}\big| = 105 \cdot 4096 \cdot \Big(\prod_{j \in \hat j}\frac{1}{2c_j}\Big) \cdot \Big|\prod_{\substack{i < j \\ i,j \in \hat j}}(x_i - x_j)\Big|}✓✓$$

$$\qquad \text{推导}✓✓：\prod_r(2r+1) = 1\cdot3\cdot5\cdot7 = 105✓（\textbf{本档第一版误写 210，已修}✓）、\ \prod_r\operatorname{lc}(Q_r) = 4^{0+1+2+3} = 4096✓✓、\ \text{而}\ \{Q_0..Q_3\}\ \text{为三角基} \Longrightarrow \det = \prod\operatorname{lc}(Q_r)\cdot\text{Vandermonde}✓✓$$

$$\qquad \textbf{精确性}✓✓：4000–6000\ \text{组随机样本上，}\ |\det|/\text{闭式} \in [1.000000000,\ 1.000000002]✓✓ \Longrightarrow \text{闭式}\ \textbf{精确}✓✓$$

$$\qquad \textbf{⭐ 与}\ \sigma\ \textbf{无关}✓✓：\sigma\ \text{只以}\ \prod\sigma_j = \pm1\ \text{进入}✓ \Longrightarrow \text{B 对}\ \textbf{全部 16 个符号类一致成立}✓✓\ \text{（Bridge A 要对}\ \sigma\ \text{一致，此点关键}✓✓）$$

$$\qquad \textbf{显式统一下界}✓✓：c_j \le 1 \Longrightarrow \frac{1}{2c_j} \ge \frac12✓；\ |x_i - x_j| = |c_i - c_j|(c_i + c_j) \ge 2\sqrt{\delta_*}\,\Delta✓✓\ (c_i + c_j \ge 2\sqrt{\delta_*})$$

$$\qquad \qquad \Longrightarrow\ \boxed{\max_{\hat j}\big|\det DG_{\hat j}\big| \ \ge\ 1{,}720{,}320\ \cdot\ \delta_*^{3}\,\Delta^{6}}✓✓,\qquad \Delta := \min_{i \ne j}|c_i - c_j|$$

$$\qquad \qquad \textbf{数值}✓✓：\max_{\hat j}|\det|\,/\,\big(1.72032\times10^{6}\delta_*^{3}\Delta^{6}\big)\ \ge\ \mathbf{626.79}✓✓ \Longrightarrow \text{下界成立且余量极大}✓✓$$

$$\textbf{④ ⭐ 障碍"兑现"（本档核心意义）}✓✓：\ C\text{-}350\ §0⑤\ \text{记载两个退化源}✓：$$

$$\qquad \textbf{(i) 权重塌缩}✓ \Longrightarrow \text{由}\ \delta_* > 0✓\ \text{排除}✓✓：\text{因子}\ 1/(2c_j) \le 1/(2\sqrt{\delta_*})✓\ \textbf{不发散}✓✓$$
$$\qquad \textbf{(ii) 原子碰撞}✓ \Longrightarrow \text{由}\ C\text{-}369\ \text{排除}✓✓：\ \mathcal D_{\mathrm{coll}} \cap E = \varnothing✓ \Longrightarrow \Delta > 0✓✓$$
$$\qquad \qquad ⚠️ \textbf{严守措辞}✓✓：\text{只写}\ \textbf{"碰撞部分的}\ \mathcal Z \cap E\ \text{已排除"}✓✓,\ \textbf{不}扩大成整个\ \mathcal Z \cap E✗✓（`C-369`\ \text{纪律}✓）$$
$$\qquad \Longrightarrow\ \text{在此两条输入下，}\ \operatorname{rank}DG = 4✓\ \text{且}\ \eta = 1.72032\times10^{6}\delta_*^{3}\Delta^{6} > 0✓✓$$

$$\textbf{⑤ 判词（首档）}✓✓：\ \boxed{\textbf{A：PASS（精确，含}\ \sigma\text{一致性）}}✓✓；\ \boxed{\textbf{B：PASS（显式常数}\ 1.72032\times10^{6}\delta_*^{3}\Delta^{6}\text{）}}✓✓$$

$$\qquad \Longrightarrow\ \textbf{该定量矩单射型}\ \textbf{不判 NO-GO}✓✓\ \Longrightarrow\ \text{允许（且仅允许）进入 C}✓✓$$

$$\textbf{⑥ ⚠️ 防循环条件（唐先生，强制登记）}✓✓：\ \text{若最终只得到}\ \operatorname{dist}(x,\mathcal Z) \le C\|G\|✓\ \textbf{而无} \text{新的}\ \mathcal Z \to \text{偶频矛盾机制}✗ \Longrightarrow \textbf{仍只是}\ C\text{-}350\ \text{的定量重述}✓✓,\ \textbf{不能升主线}✗✓$$

$$\qquad \Longrightarrow\ \text{C-3851 的}\ \textbf{真正出口是 D}✓✓：\ \boxed{\text{odd-small} \Rightarrow \text{near }\mathcal Z \Rightarrow \text{near-doubling} \Rightarrow F_{2r} > \tfrac12\ (\exists r \le 12)}✓✓$$

$$\textbf{⑦ 本档}\ \textbf{不}声称的东西}✓✓：\text{C（定量逆）}\ \textbf{未证}✗✓；\ \text{D（Bridge B）}\ \textbf{未证}✗✓；\ \Delta_*\ \text{的}\ \textbf{数值} \text{未给}✗✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 A／B 的推导（三行 ✓✓）

$$\textbf{(1) 可微性}✓：T_{2r+1}(c) = c\,R_r(c^2)✓,\ \frac{d}{dc}T_{2r+1} = (2r+1)U_{2r}✓ \Longrightarrow \partial_{x}T_{2r+1}(\sqrt x) = \frac{(2r+1)U_{2r}(\sqrt x)}{2\sqrt x}✓✓$$

$$\textbf{(2) 结构}✓：\text{第}\ r\ \text{行} = \sigma \odot \big[(2r+1)U_{2r}(c)/(2c)\big]✓ \Longrightarrow DG = \operatorname{diag}(\sigma)U^{\top}✓✓ \Longrightarrow \operatorname{rank}DG = \operatorname{rank}U✓✓$$

$$\textbf{(3) 秩与行列式}✓：U_{2r}(c) = Q_r(c^2)✓,\ \deg Q_r = r✓ \Longrightarrow \operatorname{rank}U = \min(4,\#\text{distinct})✓；\ \text{minor 行列式} = \prod_r(2r+1)\cdot\prod_{j \in \hat j}\frac{1}{2c_j}\cdot\det[Q_r(x_j)]✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **A：rank DG = 4（无碰撞）** ✓ | **PASS（精确）** ✓✓ |
| **B：统一 minor ≥ 1.72032e6 δ_*³ Δ⁶** ✓ | **PASS（显式常数）** ✓✓ |
| σ 一致性 ✓ | **成立（|det| 与 σ 无关）** ✓✓ |
| C：定量逆 ✓ | **未开（本档不做）** ✗✓ |
| D：Bridge B（𝒵 → 偶频成本） ✓ | **未开（真正出口）** ✗✓ |
| `\mathcal D_{\mathrm{coll}} \cap E = \varnothing` ✓ | **引用（限 `\mathcal Z \cap E` 语境）** ✓✓ |
| `\delta_* > 0` ✓ | **引用（存在性）** ✓✓ |
| 该定量矩单射型 ✓ | **首档通过，未判 NO-GO** ✓✓ |

## §3 数值记录（数字驱动 ✓✓）

```
A0：导数闭式 vs 有限差分        max 差 = 6.9e-10                      ✓
A ：rank：5 互异→4；1 重(4 互异)→4；2 重(3 互异)→3                  ✓ 与预测一致
B ：|det|/闭式 ∈ [1.000000000, 1.000000002]（6000 组）              ✓ 闭式精确
B2：max_jhat|det| / (1.72032e6 δ_*^3 Δ^6) ≥ 626.79                  ✓ 下界成立
   第一版脚本误写 ∏(2r+1)=210（应 105）⟹ 比值恒为 0.5，已修并重跑 ✓
```
- 脚本 ✓：`scripts/c380_51_c3851_AB_v2.py`✓（初版 `c380_51_c3851_AB_rank.py` 保留为审计痕迹 ✓）；输出 ✓：`scripts/out_c380_51_AB_v2.txt`✓

## §4 边界（不得声称 ✗✓）

- **不**声称 C（定量逆）已证／D（Bridge B）已证 ✓
- **不**声称 `\Delta_*` 有数值下界（只由 C-369 ＋ 紧性得**存在**）✓
- **不**把 C-369 的结论扩大成整个 `\mathcal Z \cap E` ✓
- **不**声称 A＋B 本身可升主线（防循环，见 §0⑥）✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 秩定理        命中文件数=1    :: ./V125-S1-completeness-audit-upgrade-fails-equals-E148.md（语境无关）
技术词 统一minor     命中文件数=0    :: （本档新用）
技术词 定量逆函数    命中文件数=0    :: （本档新用）
技术词 循环性防御    命中文件数=0    :: （本档新用）
技术词 VANDERMONDE   命中文件数=0    :: （本档新用）
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{C}✓：\text{定量逆}✓：\text{由}\ \textbf{统一 minor} ＋ \textbf{紧性／有限覆盖}✓ \Longrightarrow \operatorname{dist}(x,\mathcal Z_\sigma) \le C(\delta_*,\Delta_*)\|G(x,\sigma)\|✓✓\ \text{（标准路径}✓）$$
$$\textbf{D}✓：\ \textbf{Bridge B}✓：\text{近抵消} \Longrightarrow \text{近加倍结构}✓ \Longrightarrow \text{偶频成本} > \tfrac12✓✓\ \text{（}\textbf{真正出口，防循环}✓）$$
$$\textbf{注}✓：\text{D 若仍只回到偶频不等式重组} \Longrightarrow \textbf{判 repackaging 并封该型}✗✓（M2）$$
