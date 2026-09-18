已查地图 + **取回 Burnol 正文部分逐字**（所查：`ACTION-START-TABLE-W-D.md:32`（`D1` 行：Burnol 逐字＋`CONV2`/`CONV3` 撤回**并存**）、`AUDIT-WALLS-AND-DIFFICULTIES-20260917.md:34`（`D1` 逐字判词）、`C61-...:91`（`DOOR5e:64` 引用路径）、`CONV2-online-part-needs-no-dispersion.md` §0（"我说'缺在线相位分散界'是**错的**"）、`CONV3-conversion-is-provable.md` §5（"不需要零密度定理／分散界／均匀性（**全部撤回**）"）、`C-86`／`C-87`；**外取**：`arXiv:math/0103058`（Burnol **摘要逐字** ＋ **正文部分逐字**：下界式、`Theorem 1.4`、`Theorem 4.2`））。**结论**：接受唐先生三点改正——① **术语严格性**（写"归一化**候选**"与"**merge candidate**"，不写等价）；② ⚠️ **撤回 `C-87` 的第二箭头**（"离散测度 ⟹ 只能 √-cancellation"**不成立**；需新定理）；③ **改名 `UQRL`**；并**第一刀实取 Burnol**：其 uniformity 的极限参数是 **`λ→0`**（逼近参数），而 `C-87` 需要的是 **`sup_{n≲T₀²}`**（频率一致）⟹ **两者不是同一个 uniformity** ✓✓ ⟹ `D1(b)` **不能借 Burnol 关闭** ✓

# C-88 · **`C-87` 三处改正 ＋ Burnol Uniformity Ledger（第一刀）**

> **时间**：2026-09-18 13:27 唐先生：接受归一化方向但**术语要严格**；接受块法增益；**不同意**"离散测度 ⟹ 只能 √-cancellation"升级为定理；建议改名 `UQRL`；下刀＝Burnol Uniformity Ledger
> **本档**：三处改正 ＋ Ledger 骨架 ＋ 第一刀实取结果 ✓

---

## §0 三处改正（`[本档]`）

$$\textbf{(1)}\ \textbf{术语严格性}：\text{写}\ \boxed{\text{"W1 在当前攻击框架下}\textbf{可归一化到}\ W6\text{"}}\ \text{而}\ \textbf{不} \text{写"W1}\equiv\text{W6"};\ \text{除非}\ \textbf{双向 reduction 已构造}✓$$
$$\qquad \text{同理}\：D3\text{(b)}\to D1\text{(b)}\ \text{写}\ \boxed{\text{"结构归约成立}\textbf{方向}／\textbf{merge candidate}"},\ \textbf{不} \text{写等价}✓✓$$
$$\textbf{(2)}\ ⚠️\ \textbf{撤回 `C-87` 的第二箭头}（唐先生指正，接受）：\text{"离散测度}\Longrightarrow\text{只能}\ \sqrt{\cdot}\text{-级相消"}\ \textbf{不成立}✗$$
$$\qquad \text{第一箭头（}\dim_H\operatorname{supp}dS=0\Longrightarrow\textbf{无连续正则性红利}\text{）＝}\textbf{结构观察}✓$$
$$\qquad \text{第二箭头（}\textbf{不存在离散算术结构产生的超}\sqrt{N}\ \text{cancellation}\text{）}＝\textbf{需新定理}，\textbf{不能} \text{由 Hausdorff 维数推出}✗✗$$
$$\qquad \text{（反例风险：算术点集完全可能有}\ \bigl|\sum_{j\le N}e(\varphi(\gamma_j))\bigr|\ll N^\theta,\ \theta<\tfrac12\text{）}✓$$
$$\qquad \Longrightarrow\ \text{正确状态}：\boxed{D3\text{(b)}\to\textbf{quantitative discrete cancellation}}\ \text{而}\ \textbf{不是}\ D3\text{(b)}\to\text{parity}\to\text{DEAD}✓✓$$
$$\qquad \text{（否则重复"结构观察}\to\text{全局 NO-GO"老坑）}✓$$
$$\textbf{(3)}\ \textbf{改名}：\boxed{\textbf{UQRL}\ (\text{Uniform quantitative RL gap})}\ \text{取代笼统的"相位均匀性"}✓$$
$$\qquad \text{精确定义}：\boxed{\sup_{n\lesssim T_0^2}\bigl|\mathcal E(n,T_0)\bigr|\ \longrightarrow\ 0}\qquad（\text{避免被误认为普通 Weyl／ET 均匀分布}）✓$$

## §1 状态表更新（按唐先生给定）

| 项目 | 当前状态 |
|:--|:--|
| `W6` | **原子墙** |
| `W1` | **归一化候选** → `W6` |
| `D3(b)` | 局部 **smooth gap 已削弱**（块法，一阶消失矩）|
| `D3(b)` | **剩余 ＝ `UQRL`** |
| `D3(b) → D1(b)` | **结构归约成立方向；严格等价待证**（merge candidate）|
| `D1(b)` | **Burnol uniformity 原文审计** |
| `D10(a)` | 独立 |
| `W8(b)` | 独立 |

$$\Longrightarrow\ \text{可攻叶子}\ \boxed{4\to3}：\ D3\text{(b)}\leftrightarrow?D1\text{(b)}\ \big|\ D10\text{(a)}\ \big|\ W8\text{(b)}✓$$

## §2 **Burnol Uniformity Ledger**（骨架 ＋ 第一刀实取）

$$\text{七列}：\text{原文逐字}\ \big|\ \text{变量定义}\ \big|\ \textbf{极限顺序}\ \big|\ \text{uniform 参数范围}\ \big|\ \text{误差率}\ \big|\ \text{是否涉及 RH}\ \big|\ \textbf{能否覆盖}\ n\lesssim T_0^2✓$$

$$\textbf{〔摘要〕逐字}：\text{"We slightly improve the lower bound of Baez-Duarte, Balazard, Landreau and Saias in the}\ \textbf{Nyman--Beurling}\ \text{formulation of RH as an approximation problem. We construct}\ \textbf{Hilbert space vectors}\ \text{which could prove useful in the context of the so-called 'Hilbert--Polya idea'."}✓$$
$$\qquad ⚠️\ \textbf{摘要不含任何 uniformity 陈述}✗\（\text{亦不含 "as}\ A\to0\text{"}）✓$$
$$\textbf{〔正文〕逐字}：\text{下界}\ \frac{D(\lambda)}{\sqrt{\log(1/\lambda)}}\ \ge\ \sqrt{\sum_\rho\frac{m_\rho^2}{|\rho|^2}}\quad(\lambda\to0)✓$$
$$\qquad \text{逐字}：\text{"So the zeros are counted according to the}\ \textbf{square of their multiplicities}\text{"}✓$$
$$\qquad \textbf{Theorem 1.4（玩具模型）}：Q(z)=\prod_\alpha(1-\alpha z)^{m_\alpha},\ \text{根全在单位圆};\ E(N,P):=\inf_{\deg A\le N}\int_{S^1}|P-QA|^2\frac{d\theta}{2\pi};\ \lim_NE(N,P)=\sum_\alpha m_\alpha^2|P(\alpha)|^2✓$$
$$\qquad \textbf{Theorem 4.2}：\text{对每个}\ 0<\lambda\le1,\ \text{临界线上的}\ s,\ k\ge0,\ \text{向量}\ Y^\lambda_{s,k}:=\mathrm{l.i.m.}_{w\to s,\ \Re w<\frac12}V^{-1}Q_\lambda V(\psi_{w,k})✓$$
$$\qquad \qquad \text{标量积}：\lambda\le\theta\le1\Rightarrow(D_\theta(A),Y^\lambda_{s,k})=\bigl(-\tfrac{d}{ds}\bigr)^k\theta^{s-\frac12}Z(s)✓$$

$$\textbf{Ledger 前七格填写}：$$
| 列 | 结果 |
|:--|:--|
| 原文逐字 | ✓（摘要＋三处正文，见上）|
| 变量定义 | `λ∈(0,1]` 逼近参数；`D(λ)` 逼近距离；`s` 临界线零点；`k` 重数指标；`θ` 尺度参数 |
| **极限顺序** | ⭐ **`λ→0`**（**逼近参数**，非频率）|
| uniform 参数范围 | ⚠️ **待定**（正文未全文取得）|
| 误差率 | `√log(1/λ)` 级（**下界**）|
| 是否涉及 RH | 下界**无条件**；`inf D=0 ⟺ RH`（Nyman–Beurling 等价）|
| **能否覆盖 `n≲T₀²`** | ⚠️ **未见**（对象不同：`D(λ)` vs `Fluc(n)`）|

## §3 与 `CONV2`／`CONV3` **对质**（本档）

$$\text{`CONV2` 逐字}：\text{"我说'缺在线相位分散界'是}\textbf{错的}\ \text{"};\ \text{"}\textbf{在线部分不需要任何"分散界"}\text{"}\（\text{那一处撤回}）✓$$
$$\text{`CONV3` 逐字}：\text{"}\textbf{不需要零密度定理、不需要分散界、不需要均匀性}\text{"（全部撤回）}✓$$
$$\Longrightarrow\ \text{这两处撤回的是}\ \textbf{"该转换处不需要均匀性"};$$
$$\qquad ⚠️\ \text{而}\ \textbf{Burnol 处的 uniformity}\ \text{我们}\textbf{未能定位到确切定义}（\text{摘要不含；正文未全文取得}）⟹ \textbf{两处不能互相借力}✓✓$$
$$\qquad ⚠️\ ⚠️\ \textbf{另须登记}：\text{档案中"Burnol 原文（门⑤逐字）'What is essential nevertheless is the uniformity as }A\to0\text{'"这条}\ \textbf{引用}\ \textbf{本档未能复核}（\text{摘要无};\ \text{正文未全取}）$$
$$\qquad \Longrightarrow\ \text{按纪律}\ \textbf{不得当"已核"使用};\ \text{标}\ ⚠️\ \textbf{待核}✓✓\（\text{"同一个词}\ne\text{同一个数学命题"}）$$

## §4 下一轮搜索（三族关键词 ＋ 判据）

$$\boxed{\text{uniform Fourier decay of discrete measures}}\ \big|\ \boxed{\text{uniform exponential sums over zeros}}\ \big|\ \boxed{\text{large sieve / decoupling for zeta zero ordinates}}✓$$
$$\text{要查的}\ \textbf{唯一判据}：\boxed{\text{这些工具给的是}\ \textbf{n-uniform} \text{还是}\ \textbf{average-}n\ \text{的估计？}}✓✓$$
$$\qquad \text{若只能给}\ \int_1^{T_0^2}|E(n,T_0)|^2dn\ \text{而我们需要}\ \sup_{n\le T_0^2}|E(n,T_0)| \Longrightarrow \textbf{不能直接闭合}✓$$

## §5 拆解状态（对 `C-86`／`C-87` 的更正写法）

$$\text{可攻叶子}：4\to3\ \text{写为}\ \boxed{\{D3\text{(b)},\ D1\text{(b)}\}\ \text{＝}\textbf{merge candidate}}\ \big|\ D10\text{(a)}\ \big|\ W8\text{(b)}✓$$
$$\qquad ⚠️\ \text{不写等价}（\text{需}\ D1\text{(b)}\Rightarrow D3\text{(b)}\ \text{才可升级}）✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 13:2x）`[纪律]`（先跑后写）

```
技术词 UQRL                      命中文件数=0
技术词 merge candidate           命中文件数=0
技术词 Burnol Uniformity Ledger   命中文件数=0
技术词 归一化候选                  命中文件数=0
```
**读数**：四项**均 0 档 ⟹ 本档新增** ✓

## §7 边界

- `[逐字]` §2 摘要＋三处正文（Burnol）✓；§3 `CONV2`／`CONV3` ✓；`[本档]` §0 三处改正、§3 对质结论、§4 判据 ✓
- ⚠️ §2 Ledger 后两格（uniform 参数范围／能否覆盖 `n≲T₀²`）**待正文全文** ⟹ 标待核
- ⚠️ 档案中"门⑤逐字"那条 Burnol 引用**本档未能复核** ⟹ 登记为待核，**不得**当已核使用
- **不声称**：`D1(b)` 关闭 ✗ 或死 ✗；不声称 `UQRL` 不可解 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓；**零数值** ✓

```
⚠️ 唐先生 13:27 指令：①术语严格（写"归一化候选"/"merge candidate"，不写等价，除非双向 reduction 已构造）②接受块法增益（一阶消失矩＝具体数学增益）
   ③⚠️不同意"离散测度 ⟹ 只能 √-cancellation"升级为定理 ④改名 UQRL ⑤下刀＝Burnol Uniformity Ledger ⑥第一刀先判"Burnol 的 uniformity 是否就是 C-87 所需的同一个 uniformity"
✅ 已执行三处改正：①术语严格（W1→W6 写"可归一化"；D3(b)→D1(b) 写 merge candidate）②撤回 C-87 第二箭头（"离散测度 ⟹ 只能 √"不成立；
   第一箭头＝结构观察；第二箭头需新定理，不能由 Hausdorff 维数推出；正确状态 D3(b) → quantitative discrete cancellation，**不是** → parity → DEAD）
   ③改名 UQRL = sup_{n≲T₀²}|E(n,T₀)| → 0
⭐ Burnol Ledger 第一刀实取：摘要逐字（Nyman–Beurling 下界 + "Hilbert space vectors"）——**摘要不含任何 uniformity 陈述**；
   正文逐字：D(λ)/√log(1/λ) ≥ √(Σ_ρ m_ρ²/|ρ|²)（**λ→0**），"zeros are counted according to the **square of their multiplicities**"；
   Theorem 1.4 玩具模型（Q 根在单位圆，E(N,P) → Σ_α m_α²|P(α)|²）；Theorem 4.2（Y^λ_{s,k} = l.i.m._{w→s, Re w<1/2} V⁻¹Q_λV(ψ_{w,k})；
   标量积 (D_θ(A), Y^λ_{s,k}) = (−d/ds)^k θ^{s−1/2}Z(s), λ ≤ θ ≤ 1）
⭐ 第一刀判定：**Burnol 的极限参数是 λ→0（逼近参数），而 C-87 需要 sup_{n≲T₀²}（频率一致）⟹ 两者不是同一个 uniformity**
   ⟹ D1(b) **不能借 Burnol 关闭**；且其机器（Nyman–Beurling/Hilbert space vectors，标量积按重数）属**既有谱/Hilbert 结构**（与唐先生警告一致）；
   下界按**重数平方**计 ⟹ 重数通道（cf. V192）
⚠️ 与 CONV2/CONV3 对质：两处撤回的是"该转换处不需要均匀性"；而 Burnol 处的 uniformity 未能定位到确切定义 ⟹ **两处不能互相借力**；
   ⚠️ 且档案中"Burnol 原文（门⑤逐字）'the uniformity as A→0'"这条引用**本档未能复核**（摘要无、正文未全取）⟹ 登记待核，不得当已核使用
⚠️ 下一轮三族关键词：uniform Fourier decay of discrete measures / uniform exponential sums over zeros / large sieve·decoupling for zeta zero ordinates；
   唯一判据：给的是 **n-uniform** 还是 **average-n**？（若只有 ∫|E|² 而我们需 sup_n ⟹ 不能直接闭合）
✅ 净产出：①三处改正（术语/撤回第二箭头/UQRL）✓；②状态表更新 ✓；③Burnol Ledger 骨架＋第一刀实取 ✓；④与 CONV2/CONV3 对质（不能互借）✓；⑤下一轮搜索判据 ✓
```
