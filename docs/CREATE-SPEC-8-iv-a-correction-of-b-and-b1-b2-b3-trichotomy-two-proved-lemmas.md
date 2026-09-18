已查地图（**先查后写**）：`CREATE-SPEC-4`（四条款＋引理：乘性变形不移零点＋张力三角；§4 三子类划分 **(a)(b)(c)**）、`CREATE-SPEC-5`（第四子类五成员：M1 素数限制／M2 除子卷积／M3 平滑／M4 Jensen／**M5＝ACPC 的 `C`**）、`CREATE-SPEC-6`（**M5 判死**：三档对照，去趋势后局部极大 `d_C=0` vs `d_Λ=50`）、`acpc-minimal-test.md`（C＝逐点积）、`V254`（典范带符号加权阈值＝`β_*`）、**`C-77`**（RS Lemma 3.5：以 C–S ＋ Rankin–Selberg 绝对收敛区证 `\Sigma\Lambda(n)^2/n^{2\sigma}` 型；该收敛区问题＝`SQ1`／支 `x\le T` ＝ `SUPPORT-1`）。关键词回查：`逐点操作三分类`／`常数系数平凡性`／`乘性保持`＝**0 档** ⟹ 本档新增 ✓。**结论**：⚠️ **本档首先纠正我自己上一轮的过度陈述**：**(b)"逐点非线性保持乘性"是\ \textbf{假的}** ✓✓（反例：`\mu\mapsto\mu+1`，`n=10` 处 `0\cdot0\neq2`）；正确形态是 **b1／b2／b3 三分**——**b1（`F` 乘性）⟹ 乘性保持 ⟹ 欧拉积回归 ✗(ii)**（新引理，已证）；**b2（作用于 ζ 自身系数）⟹ 平凡（常数系数）✗**（新引理，已证）；**b3（`F` 非乘性作用于"派生序列"）** ⟹ **唯一活口**，但**已知两实例均已被钉住**（ACPC 实验判死；`\Sigma\Lambda^2 n^{-s}` 落 `C-77`／`SUPPORT-1` 轨道）✓✓ ⟹ ⭐ **"第四子类为空"仍未证**（与上一轮答复一致：不能靠"再找不到"得到不可能）✓✓

FREEZE-ACK: 本档即冻结期内的方向攻击与结构定理骨架（依 `§8.1`；不产候选结论）

D0: 本档对象 = **对 (b) 的纠正**（b1／b2／b3 三分 ＋ 两条新引理）—— 关系 = 自我纠错与结构细化，非新机制
D1: 0

# CREATE-SPEC-8 · **(iv-a)：纠正 (b)，并给出 b1／b2／b3 三分（两条新引理已证）**

> **时间**：2026-09-18 21:55 唐先生：**「继续」** ⟹ 开 (iv-a)（证明 (b)）✓

---

## §0 结论（先行）

$$\textbf{(b) 作为原陈述为}\ \textbf{假}：\text{"逐点非线性}\Longrightarrow\text{乘性保持"}\ \textbf{不成立}✓✓$$
$$\qquad \textbf{反例}：a_n=\mu(n),\ F(x)=x+1 \Longrightarrow n=10=2\cdot5:\ F(\mu(2))F(\mu(5))=0\cdot0=\mathbf0,\quad F(\mu(10))=\mathbf2✓✓$$
$$\textbf{正确形态＝三分}：$$
$$\qquad \text{b1}\ F\ \text{乘性}（F(xy)=F(x)F(y)） \Longrightarrow \textbf{乘性保持} \Longrightarrow \text{欧拉积回归}\ ✗(ii)\quad\textbf{（新引理 L3，已证）}$$
$$\qquad \text{b2}\ \text{作用于}\ \zeta\ \textbf{自身系数} \Longrightarrow \textbf{平凡}（\text{常数系数}）✗\quad\textbf{（新引理 L2，已证）}$$
$$\qquad \text{b3}\ F\ \text{非乘性}\ +\ \textbf{派生序列}（\ge2\ \text{个不同值}） \Longrightarrow \textbf{唯一活口}✓\ \text{但已知实例}\ \textbf{全被钉住}$$
$$\Longrightarrow ⭐\ \text{由}\ (iv\text{-a})\ \textbf{未能} \text{证得"第四子类为空"} \Longrightarrow \textbf{与上轮答复一致}：\text{"再找不到"}\ \textbf{不给不可能}✓✓$$

---

## §1 纠错（本档第一件事）

$$\text{我上一轮写的 (b)}：\text{"逐点非线性}\ (a_n\mapsto a_n^2\ \text{等})\ \text{保持乘性} \Longrightarrow \text{欧拉积回归}"✓$$
$$\qquad ⚠️\ \textbf{此陈述不成立}：\text{乘性保持要求}\ F(a_{mn})=F(a_m)F(a_n),\ \text{而}\ a_{mn}=a_ma_n\ \text{仅给}\ F(a_ma_n)✓$$
$$\qquad \Longrightarrow \text{故需}\ F\ \textbf{本身乘性}（F(xy)=F(x)F(y)）;\ \text{否则}\ \textbf{乘性被破坏}✓✓$$
$$\qquad \text{反例（完整）}：\mu(2)=\mu(5)=-1,\ \mu(10)=1;\ F=x+1 \Longrightarrow F(\mu(2))F(\mu(5))=0,\ F(\mu(10))=2 \Longrightarrow \textbf{非乘性}✓✓$$
$$\Longrightarrow \text{故 (b) 须}\ \textbf{条件于}\ F\ \text{的乘性};\ \text{这正是以下三分}✓✓$$

## §2 引理 L2：作用在 ζ 自身系数上是平凡的（已证）

$$\textbf{引理 L2}：\text{若}\ a_n=c\ \forall n\（\text{如}\ \zeta\ \text{的系数全为 1}）,\ \text{则任意逐点}\ F\ \Longrightarrow\ \sum_nF(a_n)n^{-s}=F(c)\,\zeta(s)✓$$
$$\textbf{证明}：F(a_n)=F(c)\ \text{为常数} \Longrightarrow \text{级数}\ =F(c)\sum n^{-s}\quad\blacksquare✓$$
$$\Longrightarrow \textbf{推论}：\text{对}\ \zeta\ \textbf{本身}，\ \text{逐点操作}\ \textbf{只重标度} \Longrightarrow \text{由引理 1（乘性变形不移零点）}\ \textbf{零集不变}✗(iv')✓✓$$
$$\qquad \text{故"逐点非线性"要非平凡，}\ \textbf{必须先派生} \text{一个非常数序列}（\Lambda,\ A\ \text{等}）⟹ \text{进入}\ b3✓$$

## §3 引理 L3：F 乘性 ⟹ 乘性保持 ⟹ 欧拉积回归（已证）

$$\textbf{引理 L3}：\text{若}\ F(xy)=F(x)F(y)\ \text{于所涉值集},\ \text{且}\ a_n\ \text{乘性} \Longrightarrow F(a_n)\ \textbf{乘性}✓$$
$$\textbf{证明}：(m,n)=1\Longrightarrow F(a_{mn})=F(a_ma_n)=F(a_m)F(a_n)\quad\blacksquare✓$$
$$\textbf{实例（两例均验证）}：$$
$$\qquad \text{(i)}\ F(x)=x^2,\ a_n=\mu(n) \Longrightarrow F(a_n)=\mu(n)^2 \Longrightarrow \sum\mu^2n^{-s}=\frac{\zeta(s)}{\zeta(2s)}\ \textbf{有欧拉积}✓✓$$
$$\qquad \text{(ii)}\ F(x)=x^2,\ a_n=\chi(n) \Longrightarrow F(a_n)=\chi^2(n)\ \text{（特征）} \Longrightarrow L(s,\chi^2)\ \textbf{有欧拉积}✓✓$$
$$\Longrightarrow \text{b1}\ \textbf{必然} \text{回到欧拉积} \Longrightarrow \text{违 (ii)} \Longrightarrow \textbf{b1 死，且此死因}\ \textbf{已证}✓✓$$

## §4 b1／b2／b3 三分与判定表

| 子类 | 条件 | 结论 | 依据 |
|:--|:--|:--|:--|
| **b1** | $F$ 乘性（$xy\mapsto F(x)F(y)$） | 乘性保持 ⟹ 欧拉积回归 ⟹ ✗(ii) | **新引理 L3（证）** |
| **b2** | 作用于 $\zeta$ 自身系数（常数序列） | 平凡（重标度）⟹ 零集不变 ⟹ ✗(iv′) | **新引理 L2（证）** |
| **b3** | $F$ 非乘性 ＋ 派生序列（$\ge2$ 值） | **唯一活口** | 待实例 |

$$\textbf{b3 的两已知实例均被钉住}：$$
$$\qquad \text{(i)}\ \text{ACPC 的}\ C=A\cdot M（\text{逐点积}） \Longrightarrow \textbf{实验判死}（\text{`CREATE-SPEC-6`}：\text{去趋势后局部极大}\ d_C=0\ \text{vs}\ d_\Lambda=50）✗$$
$$\qquad \text{(ii)}\ \text{逐点平方作用于}\ \Lambda \Longrightarrow \sum\Lambda(n)^2n^{-s} \Longrightarrow \text{其解析区问题}\ \textbf{正是}\ \text{`C-77`}（\text{RS Lemma 3.5}／\text{`SQ1`}：绝对收敛区） \Longrightarrow \text{落}\ \textbf{`SUPPORT-1` 轨道}✓✓$$

## §5 本次 (iv-a) 的净结果（诚实）

$$\textbf{得到}：\text{一条纠错（b 为假）}＋\textbf{两条已证引理}（L2／L3）＋\textbf{三分表} ⟹ \text{点逐通道}\ \textbf{不再是黑箱}✓✓$$
$$\textbf{未得到}：\text{"第四子类为空"}\ \textbf{仍未证} ⟹ \text{b3}\ \textbf{是否为空未决}✓✓$$
$$\qquad \text{要证 b3 为空，须证}：\text{"任何}\ F\ \text{非乘性}\ +\ \text{派生序列}\ \text{的组合}\ \text{要么落}\ \text{值面}\（\text{显式公式}\）,\ \text{要么落}\ \text{已判死类}"——\ \textbf{这是一条真正的结构定理，尚未有}✓$$
$$\qquad ⚠️\ \text{而}\ b3\ \textbf{不需要} F\ \text{非线性}：\text{逐点}\ \textbf{线性} \text{非乘性操作（如}\ \text{加性卷积后逐点乘}\text{）}\ \text{同属}\ b3 ⟹ \text{范围比"非线性"更宽}✓✓$$

## §6 边界与回查

- ⚠️ L2／L3 为**初等且完整证明** ⟹ 本会话**第三、四条证明级产物**（前两条：候选 D 的 `F3` 死；乘性变形不移零点的引理）✓✓
- ⚠️ 本档**纠正的是我自己的上一轮陈述**（(b)），**不改** `CREATE-SPEC-4` 的 (a)(c) ✓
- ⚠️ §4 的"b3 两实例被钉住"：ACPC 为**实验判死**；`\Lambda^2` 为**归约判断**（`[结构性]`，非实验）✓
- ⚠️ 本会话**第四次**同型纠错（`n=2` 引用错、`V191` 标签过强、"机制不可能"过强、今 (b) 为假）⟹ **纠错机制在正常工作** ✓✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:5x）`[纪律]`（先跑后写）

```
技术词 逐点操作三分类    命中文件数=0  ⟹ 本档新增
技术词 常数系数平凡性     命中文件数=0  ⟹ 本档新增
技术词 乘性保持        命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
