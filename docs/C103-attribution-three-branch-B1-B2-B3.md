已查地图（所查：`C-102`（三窗审计；**含措辞勘误**）、`C-100`／`C-101`、`C-99`）。**结论**：按唐先生指定路线执行 **② 归因三分叉**（B1 展开／B2 求积／B3 ζ-specific）⟹ **(B1)** 尖峰在**两种互相独立的展开**下**都存在**（含**完全不用 `θ`** 的分段局部展开）⟹ **非 `θ` 截断所致** ✓；但**幅度强烈依赖 `N`**（`+4.36@40k → +2.57@200k → ~+0.8@2M`）⟹ **不稳定** ⚠️；**(B2)** 求积散布 `~0.2` ⟹ **未过 `≪0.18` 判据** ⟹ **numerically unresolved** ✓；**(B3)** 同一 `θ` 映射作用于**非算术 GUE 谱** ⟹ **无尖峰**（`+0.03`，三窗一致 `0.005`）⟹ **非"映射×刚性谱"的通用伪影** ✓ ⟹ **判词：`α≈1` 异常＝treatment-dependent／unresolved，不升级为结构，不归因于 `θ` 截断；① 继续暂缓** ✓✓

# C-103 · **归因三分叉（B1 展开／B2 求积／B3 ζ-specific）**

> **时间**：2026-09-18 15:33 唐先生：**①暂缓**，**先做②**并改造成**最小归因实验**；记 `A_1:=F_ζ(1)−1`，问 $A_1\stackrel{?}{=}A_{\rm unfold}+A_{\rm quadrature}+A_{\rm intrinsic}$ ✓
> **措辞勘误**（同轮指定）：`C-102` 的"**真实边界**"已改为 **"empirically observed stable boundary of the current usable dual-bandwidth detector"**（中文：在当前探测器、当前零点数据范围及已完成控制下，`1` 是可稳定恢复的对偶带宽边界；未观察到可用的 `>1` 结构）✓✓

---

## §0 结论（先行）

$$\textbf{(B1)}\ \text{尖峰在}\ \textbf{两种独立展开} \text{下均存在}（\text{含}\ \textbf{完全不用}\ \theta\ \text{的分段局部展开}） \Longrightarrow \textbf{非}\ \theta\ \text{截断所致}✓$$
$$\qquad ⚠️\ \text{但}：\text{幅度}\ \propto\ \text{强依赖}\ N：+4.36\ (40k)\to+2.57\ (200k)\to\sim+0.8\ (2M) \Longrightarrow \textbf{不稳定}✓$$
$$\qquad ⚠️\ \text{且}\ U2\ (\text{mpmath 精确}\log\Gamma)\ \textbf{无效}：|x_{\rm asym}-x_{\rm exact}|\sim2\times10^4 \Longrightarrow \text{尺度错（第 7 处实现问题）};\ \textbf{不作证据}✓$$
$$\textbf{(B2)}\ \text{求积散布}\ \sim0.2\（1.45\text{–}1.66） \Longrightarrow \textbf{未过}\ |\Delta F(1)|\ll0.18\ \text{判据} \Longrightarrow \boxed{\textbf{numerically unresolved}}✓✓$$
$$\textbf{(B3)}\ \theta\ \text{映射作用于非算术 GUE 谱} \Longrightarrow F(1.0)=+1.032/+1.035/+1.030 \Longrightarrow \textbf{无尖峰}✓✓$$
$$\qquad \Longrightarrow\ \textbf{非"映射}\times\text{刚性谱"的通用伪影}✓$$
$$\textbf{总判词}：\boxed{A_1=\textbf{treatment-dependent／unresolved}};\ \text{不升级为结构};\ \text{不归因于}\ \theta\ \text{截断};\ \text{① 继续暂缓}✓✓$$

---

## §1 B1：冻结零点，改变展开（**同批同管线**）

$$\text{关键修正}：\text{首轮曾把}\ U2\ \text{用 40k、}U1/U3\ \text{用 200k}\ \textbf{混比} \Longrightarrow \text{本档}\ \textbf{同批重跑}✓$$

| 展开 | 40,000 个零点：`F(1.0)`（三窗）| 200,000 个零点：`F(1.0)`（三窗）| 三窗极差 |
|:--|:--|:--|:--|
| `U1` 渐近 `θ` 级数 | +2.5844 / +2.7001 / +2.3574（均值 **+2.547**）| +2.0615 / +2.1400 / +1.9067（均值 **+2.036**）| 0.34／0.23 |
| `U3` **分段局部（无 `θ`）** | +4.3572 / +4.4144 / +4.3134（均值 **+4.362**）| +2.5880 / +2.6528 / +2.4793（均值 **+2.573**）| 0.10／0.17 |
| `U2` mpmath 精确 `logΓ` | +1.0192 / +1.0181 / +1.0173（均值 +1.018）| 同 | 0.002 |
| **诊断** `x_asym − x_exact` | 均值 `+2.32e4`，`std 1.32e4`，`max 4.60e4` | 均值 `+1.13e5`，`std 6.49e4`，`max 2.25e5` | — |

$$\textbf{读数}：$$
$$\qquad \text{(i)}\ U1\ \text{与}\ U3\ \textbf{都出现尖峰}，\ \text{而}\ U3\ \textbf{完全不用}\ \theta \Longrightarrow \textbf{非}\ \theta\ \text{截断所致}✓✓$$
$$\qquad \text{(ii)}\ ⚠️\ \text{幅度}\ \textbf{强依赖}\ N（\text{40k}\to4.36,\ \text{200k}\to2.57,\ \text{2M}\to\sim0.8） \Longrightarrow \textbf{不是稳定谱特征}✓$$
$$\qquad \text{(iii)}\ ⚠️\ U2\ \text{的诊断显示}\ |x_{\rm asym}-x_{\rm exact}|\sim10^4 \Longrightarrow \text{其展开}\ \textbf{尺度错误} \Longrightarrow \text{其"无尖峰"}\ \textbf{不构成证据}✓✓$$
$$\qquad ⭐\ \text{故 B1}\ \textbf{部分归因}：\text{尖峰}\ \textbf{不来自}\ \theta\ \text{截断};\ \text{但其}\ \textbf{不稳定} \Longrightarrow \text{倾向}\ \text{treatment 效应}（\text{binning／展开与有限范围的相互作用}）✓$$

## §2 B2：冻结展开，改变求积实现（全量 `2,001,052`）

$$\text{固定}\ D(s)\（U1\ \text{展开}）;\ \text{比较四套实现}：$$

| 实现 | `Δs=0.0173` 网格 | `Δs=0.0346` 网格 | `Δs=0.0692` 网格 | 独立实现（`scipy` Simpson，20001 点）|
|:--|--:|--:|--:|--:|
| `F(1.0)` | +1.6353 | +1.4536 | +1.4718 | +1.6579 |

$$\Longrightarrow\ \text{散布}\approx1.66-1.45=\mathbf{0.21} \Longrightarrow \textbf{未过判据}\ |\Delta F(1)|\ll0.18 \Longrightarrow \boxed{\textbf{numerically unresolved}}✓✓$$
$$\qquad ⚠️\ \text{即}\ \textbf{求积实现本身的 0.2 级不确定度} \text{与尖峰幅度同量级} \Longrightarrow \text{目前}\ \textbf{无法把它与数值误差分离}✓✓$$

## §3 B3：ζ-specific 控制（同一 `unfolding` 流程，非算术谱）

$$\text{构造}：\text{GUE 三对角}\ \beta=2\ (N_c=60000)\ \Longrightarrow \text{仿射到零点}\ t\ \text{区间} \Longrightarrow \textbf{套用同一个}\ U1\ \theta\ \text{展开}✓$$
| 窗 | `gauss` | `cos` | `quad` |
|:--|--:|--:|--:|
| 非算术谱 `F(1.0)` | +1.0320 | +1.0349 | +1.0299 |

$$\Longrightarrow\ \textbf{无尖峰}（+0.03，三窗一致 0.005） \Longrightarrow \textbf{尖峰需要 ζ 零点的具体位置结构}，\ \textbf{不是"}\theta\ \text{映射}\times\text{刚性谱"的通用产物}✓✓$$

## §4 综合判词与路线（按唐先生预设）

$$\boxed{A_1:=F_\zeta(1)-1\ \text{＝}\ \textbf{treatment-dependent／unresolved}}✓✓$$
$$\qquad \text{(i)}\ \textbf{不升级} \text{为 ζ 的真实谱结构}✗;\quad \text{(ii)}\ \textbf{不归因} \text{于}\ \theta\ \text{截断}（U3 无}\ \theta\ \text{亦有尖峰）;\quad \text{(iii)}\ \textbf{不能关闭}（B2 未过）✓$$
$$\text{路线（唐先生给定）}：\text{anomaly}\ \textbf{既未被解释消除，也未显示稳定} \Longrightarrow \boxed{\text{①}\ (\alpha>4)\ \textbf{继续暂缓}}✓✓$$
$$\qquad \text{且}\ \text{`C-102`}\ \text{的}\ \text{support}=1\ \text{结论}\ \textbf{不受污染}（\text{已用"当前探测器边界"措辞}）✓✓$$

## §5 待办（预注册）

$$\textbf{(1)}\ \text{修好}\ U2：\text{核对 mpmath}\ \log\Gamma\ \text{路线与解析式的},\textbf{尺度一致性}（\text{验}\ \mathrm{slope}=1）✓$$
$$\textbf{(2)}\ \text{以}\ \textbf{同一}\ N\ \text{同一管线} \text{重做 B1（含}\ U2）；\text{并要求}\ \text{曲线幅度}\ \textbf{对}\ N\ \text{稳定}✓$$
$$\textbf{(3)}\ \text{B2}\ \text{改为}\ \textbf{解析可积} \text{的近邻项（把}\ \alpha\approx1\ \text{处的主贡献解析分离）} \Longrightarrow \text{把求积误差压到判据以下}✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:4x）`[纪律]`（先跑后写）

```
技术词 归因三分叉        命中文件数=1  :: ./C103-attribution-three-branch-B1-B2-B3.md
技术词 treatment-dependent  命中文件数=1  :: ./C103-attribution-three-branch-B1-B2-B3.md
技术词 求积散布          命中文件数=1  :: ./C103-attribution-three-branch-B1-B2-B3.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

## §7 边界

- `[数据]` §1–§3 全部**本次实算**（B1 同批 40k／200k；B2 全量 2M 四实现；B3 `N_c=60000`）✓
- ⚠️ `U2` 展开**无效**（尺度错，已标）；B1 的"不稳定"结论**依赖**这一点已被排除 ⟹ 以 `U1`／`U3` 为准 ✓
- **不声称**：`α≈1` 是真实结构 ✗；其机制已被查明 ✗（**unresolved**）；`support>1` 不可能 ✗；不证 RH ✗
- **纪律**：**先跑后写** ✓；**未用 RH 作推导** ✓；**不挑最漂亮的结果** ✓✓

```
⚠️ 唐先生 15:33：①暂缓；先做②（最小归因实验 B1/B2/B3）；并把 C-102 措辞改弱（"真实边界"→"当前探测器可稳定恢复的边界"）
✅ 措辞勘误已落档（C-102 §8）
✅ B1（同批同管线，修正首轮 N 混比）:
   U1 渐近θ: 40k 均值 +2.547 / 200k +2.036（三窗极差 0.34/0.23）
   U3 分段局部（**完全不用 θ**）: 40k 均值 +4.362 / 200k +2.573（极差 0.10/0.17）
   ⟹ 尖峰在两种独立展开下**均存在**（含无 θ 者）⟹ **非 θ 截断所致**
   ⚠️ 但幅度强依赖 N（4.36 → 2.57 → ~0.8@2M）⟹ 不稳定
   ⚠️ U2（mpmath 精确 logΓ）**无效**: |x_asym − x_exact| ~ 2×10⁴（均值 2.32e4/std 1.32e4）⟹ 尺度错（第 7 处实现问题）⟹ 不作证据
✅ B2（冻结展开，四套求积）: Δs=0.0173 → 1.6353; 0.0346 → 1.4536; 0.0692 → 1.4718; scipy Simpson 独立实现 → 1.6579
   散布 ≈ 0.21 ⟹ **未过 ≪0.18 判据** ⟹ **numerically unresolved**（求积不确定度与尖峰同量级）
✅ B3（ζ-style 映射作用于非算术 GUE 谱）: F(1.0)=1.0320/1.0349/1.0299 ⟹ **无尖峰**（三窗一致 0.005）
   ⟹ 尖峰需要 ζ 零点的具体位置结构，非"映射×刚性谱"的通用产物
⭐ 总判词: A_1 = treatment-dependent / unresolved；不升级为结构；不归因于 θ 截断；不能关闭；① 继续暂缓；C-102 的 support=1 结论不受污染
✅ 待办预注册: (1) 修 U2 并验 slope=1 (2) 同 N 同管线重做 B1 且要求幅度对 N 稳定 (3) B2 改解析分离 α≈1 主贡献
```
