已查地图（所查：`C-122`（三段要求 (i)(ii)(iii)；"已知绑定只有两条"）、`POS1`（正性三分：消失太多＝空洞／太少＝只回避不排除／恰好在离临界 ⟺ RH）、`POS3` §4（**等值判据族**：Weil 正性／Li／Robin／Nicolas／Lagarias／**Nyman–Beurling**）、`V150` W2（Robin 判据：`\sigma(n)<e^\gamma n\log\log n`，`n>5040`）、`V254`（`M(x)=O(x^{1/2+\varepsilon})\iff` RH）、`V253`（Erdos–Selberg 型只到 `\sigma=1`）、`C-76`（Beurling 型 off-line 实例）、`V193` §⑤／`V215` §5、`C-116`（**登记不否决**）、`FZ-3`）。**结论**：扫描现有数学中"零-free 定义 ＋ `\beta`-跟踪"的对象 ⟹ **`C-122` 的一处表述必须勘误**：**(i) 零-free 并**不**强制 `canonical` 性**，且"已知绑定只有两条"**是错的** —— 实际存在**至少五类零-free 且能跟踪 `\beta_*` 的构造**（`1/\zeta` 型乘性商／**Nyman–Beurling–Báez-Duarte 距离判据**／**Robin–Nicolas–Lagarias 初等等值判据**／Mertens 型／Beurling 广义素数实验台）✓✓；⟹ **普遍卡点不在 (i) 也不在 (ii')，而在 (iii)："决定性步可在不引入 RH 强度输入下证明"** —— 其理由正是 `POS1` 三分（**任何单向一致余量的成立 ⟺ RH**）＋ `F5` 空 ✓✓；⟹ **地图修正**：**缺的不是"构造"，而是"余量可证性（strength）"** ✓✓

# C-123 · **扫描：零-free `\beta`-跟踪对象 ＋ `C-122` 勘误 ＋ 卡点定位到 (iii)**

> **时间**：2026-09-18 18:23 唐先生：**「继续」** ⟹ 按三段要求扫描现有数学；若扫不到则把"只有两条绑定"推向更强表述 ✓

---

## §0 结论（先行）

$$\textbf{(1)}\ ⚠️\ \textbf{`C-122` 勘误（自我更正）}：\text{我写"}\text{为什么难}：\text{(ii) 要求与}\ \zeta\ \text{绑定，已知绑定}\ \textbf{只有两条} \Longrightarrow \textbf{该句为假/过强}✓✓$$
$$\qquad \text{实际}：\textbf{(i) 零-free}\ \textbf{不强制} \text{canonical 性};\ \text{且存在}\ \textbf{至少五类} \text{零-free 且能跟踪}\ \beta_*\ \text{的构造}✓✓$$
$$\textbf{(2)}\ ⭐\ \textbf{普遍卡点在 (iii)}：\text{不在 (i)（零-free），也不在 (ii')（}\beta\text{-跟踪机制）}✓✓$$
$$\qquad \textbf{(iii)}\ \text{决定性步可在}\ \textbf{不引入 RH 强度输入} \text{下证明} \Longrightarrow \text{全部已知实现}\ \textbf{皆失败}✓✓$$
$$\qquad \text{理由}：\text{`POS1` 三分}（\textbf{任何单向一致余量的成立}\ \Longrightarrow\text{RH}）＋ \text{`F5` 空}（\text{独立算术输入}）✓✓$$
$$\textbf{(3)}\ ⭐\ \textbf{地图修正}：\boxed{\text{缺的是}\ \textbf{余量可证性（strength）}，\ \textbf{不是构造}}✓✓$$

---

## §1 扫描表：零-free `\beta`-跟踪候选类

$$\textbf{要求（本档更精确的版本）}：\textbf{(i)}\ \text{零-free 定义};\quad \textbf{(ii')}\ \textbf{β-跟踪机制}（\text{奇点位置／密度指数／距离衰减／正性余量，}\textbf{任一}）;\quad \textbf{(iii)}\ \text{决定性步可证（无 RH 强度输入）}✓$$

| # | 类 | 代表 | (i) 零-free | (ii') 跟踪 `\beta_*` | (iii) 决定性步可证 | 结论 |
|:--|:--|:--|:--:|:--:|:--:|:--|
| 1 | **乘性商／奇点** | `1/\zeta`、`\zeta'/\zeta`、L-商 | ✓ | ✓（奇点＝零点）| ✗（无条件横坐标 `=1`；到 `\tfrac12` ⟺ RH）| 2/3 |
| 2 | **显式公式** | 零点作输入 | ✗ | ✓ | ✓ | 2/3 |
| 3 | ⭐ **Nyman–Beurling／Báez-Duarte** | 距离 `d_n\to0`；**分数部分／余切和** | ✓✓ | ✓（判据 ⟺ RH）| ✗（证极限＝RH）| **2/3** |
| 4 | ⭐ **初等等值判据族** | Robin `\sigma(n)`；Nicolas；Lagarias；Mertens `M(x)` | ✓✓ | ✓（各自 ⟺ RH）| ✗ | **2/3** |
| 5 | **Erdős–Selberg 双线性** | 初等 PNT | ✓ | ✗（只到 `\sigma=1`）| ✓（但太弱）| 2/3 |
| 6 | **Beurling 广义素数** | 由计数函数定义 | ✓✓ | ⚠️ **实验台**（可造离轴实例，但**不是** `\zeta`）| — | 非 `\zeta` |
| 7 | **Weil 正性** | 素数侧二次型 | ✓ | ✓（⟺ RH）| ✗（`POS1` 第三行）| 2/3 |
| 8 | **Li 判据** | `\lambda_n\ge0` | ✓ | ✓（⟺ RH）| ✗ | 2/3 |

$$\Longrightarrow \boxed{\text{零-free 且能跟踪}\ \beta_*\ \text{的构造}\ \textbf{至少 5 类}（\#3,\#4,\#5,\#7,\#8）;\ \text{而}\ \textbf{无一} \text{通过 (iii)}}✓✓$$
$$\qquad \Longrightarrow \text{故"}\textbf{零-free}\ \Longrightarrow\ \text{必须 canonical}\text{"为}\ \textbf{假};\ \text{且"绑定只有两条"}\ \textbf{作废}✓✓$$

## §2 ⭐ 为什么 (iii) 是普遍卡点

$$\text{上述}\ \#3,\#4,\#7,\#8\ \text{的}\ \textbf{决定性步}\ \text{都是}\ \textbf{单向余量型} \text{陈述}：$$
$$\qquad \text{Robin}：\sigma(n)<e^\gamma n\log\log n\（n>5040）;\quad \text{Li}：\lambda_n\ge0\ \forall n;\quad \text{NB}：d_n\to0;\quad \text{Weil}：Q\succeq0✓$$
$$\qquad \Longrightarrow \text{每一式都}\ \textbf{等价于 RH}（\text{`POS3` §4 等值判据族}）✓✓$$
$$\text{`POS1` 三分（逐字要点）}：\text{消失太多}\Rightarrow\textbf{空洞};\ \text{消失太少}\Rightarrow\textbf{只回避不排除};\ \text{恰好消失在离临界配置}\Rightarrow\iff\text{RH}✓✓$$
$$\qquad \Longrightarrow \boxed{\text{任何}\ \textbf{一致余量} \text{的单向陈述，其成立}\ \iff\text{RH}} \Longrightarrow \textbf{(iii) 必失败}✓✓$$
$$\text{等价表述}：\text{`F5`（含独立算术输入，不与 RH 等价）}\ \textbf{空}✓✓$$

## §3 与既有残余的对接（同址 ＋ 本档新增）

$$\text{本档定位} \equiv \text{`F5` 空} \equiv \text{`V193` §⑤ 残余} \equiv \text{`V215` §5} \equiv \text{`V254` 开口} \equiv \text{`C-110` 的}\ \text{`C1`}\cap\text{`C6`}✓$$
$$\textbf{本档新增}：\text{(a) 勘误（(i) 不强制 canonical）};\ \text{(b) 具体证据：}\textbf{5 类零-free β-跟踪构造};\ \text{(c) 卡点}\ \textbf{统一到 (iii)}✓✓$$
$$\qquad \Longrightarrow \text{今后问句应改为}：\boxed{\text{是否存在}\ \textbf{一个}\ \beta\text{-跟踪构造，其决定性余量可在无 RH 强度输入下证明？}}✓✓$$

## §4 地图修正的含义（本档最重要的推轮）

$$\text{旧读法}：\text{"找不到对象／构造"} \Longrightarrow \text{在构造空间里搜}✓$$
$$\text{新读法}：\boxed{\text{构造空间}\ \textbf{不空}（\ge5\ \text{类}）;\ \text{空的是}\ \textbf{余量强度空间}}✓✓$$
$$\qquad \Longrightarrow \text{攻击点}\ \textbf{不是"找新对象"}，\ \text{而是"}\textbf{让既有对象的决定性余量可证}\text{"}✓✓$$
$$\qquad \qquad \text{而这正是}\ \text{`C-110`}\ \text{的}\ \text{`C6`}（\text{定量稳定性}）\ \text{与}\ \text{`C-111`}\ \text{的}\ \text{`F3`}（\text{端点分支}）\ \text{所处理的对象}✓✓$$
$$\qquad \Longrightarrow \text{故本档}\ \textbf{把两条线合并}：\text{构造侧}\ \textbf{已足};\ \text{唯缺}\ \textbf{余量侧}✓✓$$

## §5 边界与回查

- ⚠️ **勘误的性质**：本档**更正自己**（`C-122` 的"为什么难"一句）；**不改变** `C-122` 的三段要求框架（仅把 (ii) 放宽为 (ii')）✓
- ⚠️ **不否决**（`C-116`）：本档**不**声称 (iii) 不可能；只登记"全部已知实现皆失败"（归纳级）✓
- ⚠️ `#6` Beurling 行标"非 `\zeta`"：它是**实验台**，**不**提供 `\zeta` 的 `\beta_*` ✓
- **不声称**：扫描完备 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导**（仅在"判据 ⟺ RH"处**引用**）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 18:2x）`[纪律]`（先跑后写）

```
技术词 余量强度空间         命中文件数=1  :: ./C123-…（本档）
技术词 五类零-free 构造      命中文件数=1  :: ./C123-…（本档）
技术词 卡点统一到           命中文件数=1  :: ./C123-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

```
⚠️ 唐先生 18:23「继续」⟹ 按三段要求扫描现有数学; 若扫不到则把"只有两条绑定"推向更强表述
⭐ 扫描**一开始就抓到我自己 C-122 的一处过度陈述** ⟹ 必须先勘误
⚠️ C-122 勘误: 我写"为什么难: (ii) 要求与 ζ 绑定, 已知绑定只有两条" ⟹ **该句为假/过强**
   实际: **(i) 零-free 不强制 canonical 性**; 且存在**至少五类**零-free 且能跟踪 β* 的构造
⭐ 扫描表(要求: (i) 零-free; (ii') β-跟踪机制(奇点/密度/距离/正性余量任一); (iii) 决定性步可证):
   #1 乘性商/奇点(1/ζ, ζ'/ζ, L-商): (i)✓ (ii')✓ (iii)✗(无条件横坐标=1, 到 ½ ⟺ RH) → 2/3
   #2 显式公式(零点作输入): (i)✗ (ii')✓ (iii)✓ → 2/3
   #3 ⭐Nyman–Beurling/Báez-Duarte(距离 d_n→0; 分数部分/余切和): (i)✓✓ (ii')✓(判据 ⟺ RH) (iii)✗(证极限=RH) → 2/3
   #4 ⭐初等等值判据族(Robin σ(n)/Nicolas/Lagarias/Mertens M(x)): (i)✓✓ (ii')✓(各自 ⟺ RH) (iii)✗ → 2/3
   #5 Erdős–Selberg 双线性(初等 PNT): (i)✓ (ii')✗(只到 σ=1) (iii)✓(但太弱) → 2/3
   #6 Beurling 广义素数(由计数函数定义): (i)✓✓ (ii')⚠️实验台(可造离轴实例, 但不是 ζ) → 非 ζ
   #7 Weil 正性: (i)✓ (ii')✓(⟺RH) (iii)✗(POS1 第三行) → 2/3
   #8 Li 判据 λ_n≥0: (i)✓ (ii')✓(⟺RH) (iii)✗ → 2/3
   ⟹ **零-free 且能跟踪 β* 的构造至少 5 类(#3,#4,#5,#7,#8); 而无一通过 (iii)**
   ⟹ 故"零-free ⟹ 必须 canonical"为**假**; "绑定只有两条"**作废**
⭐ 为什么 (iii) 是普遍卡点: #3/#4/#7/#8 的决定性步都是**单向余量型**陈述(Robin: σ(n)<e^γ n loglog n; Li: λ_n≥0 ∀n; NB: d_n→0; Weil: Q⪰0)
   ⟹ **每一式都等价于 RH**(POS3 §4 等值判据族); POS1 三分: 消失太多=空洞; 太少=只回避不排除; 恰好在离临界 ⟺ RH
   ⟹ **任何一致余量的单向陈述, 其成立 ⟺ RH** ⟹ (iii) 必失败; 等价表述: **F5 空**
⭐ 地图修正(本档最重要推轮): 旧读法="找不到对象/构造"(在构造空间里搜);
   新读法=**构造空间不空(≥5 类); 空的是余量强度空间** ⟹ 攻击点不是"找新对象", 而是"**让既有对象的决定性余量可证**"
   而这正是 C-110 的 C6(定量稳定性)与 C-111 的 F3(端点分支)所处理的对象 ⟹ **两条线在此合并: 构造侧已足, 唯缺余量侧**
⚠️ 勘误性质: 本档更正自己(C-122 的"为什么难"一句); 不改变 C-122 的三段要求框架(仅把 (ii) 放宽为 (ii'))
⚠️ 不否决(C-116): 不声称 (iii) 不可能; 只登记"全部已知实现皆失败"(归纳级); #6 Beurling 是实验台不提供 ζ 的 β*
✅ 净产出: ①C-122 勘误((i) 不强制 canonical; "只有两条绑定"作废) ②扫描表 8 行(5 类零-free β-跟踪构造) ③卡点统一到 (iii) 及其理由(POS1 三分 + F5 空) ④地图修正: 缺余量强度而非构造; 与 C-110/C-111 合并
```
