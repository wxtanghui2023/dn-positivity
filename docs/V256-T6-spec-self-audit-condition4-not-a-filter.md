# V256 · **T6 规格自身审计：条件 4 不是滤子** —— ⭐⭐⭐ **廉价反例族（本档）**：凡"系数只支撑在**完全平方**上"的 Dirichlet 级数，横坐标**可证恰为 1/2**，且**完全不涉及 $\zeta$ 零点**（$\zeta(2s)$、$1/\zeta(2s)$、$\zeta(2s)/\zeta(4s)$、$\prod_p(1+p^{-2s})^{\mp1}$…）⟹ **"横坐标可独立证明为 1/2"是免费的** ⟹ $$\boxed{\text{T6 条件 4 不是滤子}}$$ ✓✓✓；⭐⭐ **机制级统一**：$$\boxed{\text{算术中"免费的}\ \tfrac12\ \text{全都是}\textbf{折半}}$$（平方层把横坐标折半；自对合轴把阶折半）——**而折半是归一化，不是信息** ✓✓✓✓；⭐ **故 T6 须补第 7、8 条，而补完后残余回到识别界面 `V215`–`V217`**

> 委托 ✓ 唐先生 2026-09-15 22:28：**"继续"**（承接 V254 §11 T6 的**对象型搜索规格**）✓✓
> 纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；**零数值** ✓｜编号 ✓ **V256**

---

## §1 承接：先审规格本身

$$\text{V254 T6 给的六条}：\text{(1) canonical}\ \text{(2) arithmetic}\ \text{(3) Dirichlet 型}\ \text{(4)}\ \textbf{横坐标可独立证为}\ \tfrac12\ \text{(5)}\ \textbf{不以}\ \zeta/L\ \text{零点为来源}\ \text{(6)}\ \textbf{不等价于已有 RH criterion} ✓$$
$$\qquad \text{但在沿此规格}\ \textbf{搜索之前}，\ \text{必须先问}：\textbf{这六条是真滤子吗}（\text{条件 4 是否廉价？}）✓✓$$

## §2 ⭐⭐⭐ **廉价反例族（本档推导）：平方层给出免费的 1/2**

$$\textbf{引理（初等）}：\text{设}\ a_n=0\ \text{除非}\ n=k^2。\ \text{则}\ \sum_n a_n n^{-s}=\sum_k a_{k^2}\,k^{-2s} \Longrightarrow\ \textbf{横坐标＝（}\sum_k a_{k^2}k^{-\sigma}\ \text{的横坐标）}\textbf{折半} ✓✓✓$$

$$\textbf{具体成员（全部可证、全部无零点输入）}：$$
$$\qquad \text{(i)}\ \zeta(2s)=\sum_k k^{-2s}：\ \text{横坐标}\ \tfrac12 ✓$$
$$\qquad \text{(ii)}\ \frac{1}{\zeta(2s)}=\sum_k\mu(k)k^{-2s}：\ \text{横坐标}\ \tfrac12 ✓$$
$$\qquad \text{(iii)}\ \frac{\zeta(2s)}{\zeta(4s)}=\prod_p(1+p^{-2s})：\ \text{横坐标}\ \tfrac12 ✓$$
$$\qquad \text{(iv)}\ \frac{\zeta(4s)}{\zeta(2s)}=\prod_p(1+p^{-2s})^{-1}：\ \text{横坐标}\ \tfrac12 ✓$$
$$\qquad \text{(v)}\ \text{更一般}：\text{任何}\ \sum_{k}a_{k^2}k^{-2s}\ \text{型（}\sum_k|a_{k^2}|k^{-\sigma}\ \text{在}\ \sigma>1\ \text{收敛）}\ \text{横坐标恒为}\ \tfrac12 ✓$$

$$\Longrightarrow \boxed{\text{"算术 ＋ Dirichlet 型 ＋ 横坐标可独立证明为}\ \tfrac12\text{"}\ \textbf{是免费的}};\ \text{构造无穷多例，}\textbf{全不需要任何零点信息} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{T6 条件 4 不是滤子}：\text{它对}\ \textbf{整族} \text{密度型对象}\ \textbf{自动成立} ✓✓✓$$

$$\textbf{与本项目已有结果的一致性}：\ \text{`V235`-A：Euler 层}\ E_r\ \text{的自然横坐标为}\ \tfrac1r;\ \textbf{故}\ r=2\ \text{层＝平方层＝}\tfrac12\ \text{＝(甲) 密度坐标} ✓✓✓$$
$$\qquad \text{`V253`：}\ c=\tfrac1r\ \text{的尾和；}\ r=2\ \text{恰为}\ \tfrac12\ \Longrightarrow \textbf{两处独立推出同一格} ✓✓$$

## §3 ⭐⭐ 机制级统一（本档提炼）：**免费的 1/2 都是"折半"**

$$\text{把本项目所有"免费}\ \tfrac12\ \text{"的来源排一排}：$$
$$\qquad \text{`V218` S1}：\text{自对合轴}\ k/2；\ k=1\ \Longrightarrow\ \tfrac12 \qquad（\textbf{把阶折半}）✓$$
$$\qquad \text{`V218` S3}：\text{归一化中点}\ \Longrightarrow\ \tfrac12 \qquad（\textbf{把区间折半}）✓$$
$$\qquad \text{`V235`-A}：\text{Euler 层}\ \tfrac1r；\ r=2\ \Longrightarrow\ \tfrac12 \qquad（\textbf{把横坐标折半}）✓✓$$
$$\qquad \text{`V253`}：\text{尾和指数}\ c=\tfrac1r;\ c=\tfrac12\ \text{发散} \qquad（\text{同上}）✓$$
$$\qquad \textbf{本档 §2}：\text{平方层}\ \Longrightarrow\ \tfrac12 \qquad（\textbf{把横坐标折半}）✓✓✓$$
$$\Longrightarrow \boxed{\text{算术中所有"免费的}\ \tfrac12\ \text{"都是}\textbf{折半}（\text{对阶、对区间、对横坐标}）} ✓✓✓✓$$
$$\qquad \Longrightarrow \textbf{而"折半"是}\textbf{归一化}，\ \textbf{不是信息};\ \text{这与}\ \text{`V218` §5（1/2 可免费产生，钉到坐标值须 canonical 归一化）}\ \textbf{完全一致} ✓✓$$
$$\qquad ⚠️\ \text{对照}：\beta_*=\tfrac12\ \textbf{不是折半}，\ \text{而是一个}\ \textbf{谱陈述}（\text{右端零点的实部}）⟹ \textbf{两者数值相同、性质不同} ✓✓✓$$

## §4 T6 规格须补两条（本档修订）

$$\textbf{第 7 条}：\tfrac12\ \textbf{不得是平方层／}\tfrac1r\ \text{密度坐标}（\text{即：不得由}\ p^{-2s}\ \text{型局部因子产生}）✓✓$$
$$\textbf{第 8 条}：\textbf{必须存在一条与}\ \zeta\ \textbf{零点的非等价蕴含链}（\text{见 §5）} ✓✓✓$$
$$\Longrightarrow \text{修订后规格}＝\text{canonical}＋\text{arithmetic}＋\text{Dirichlet 型}＋\text{横坐标可证}\ \tfrac12＋\textbf{非 L-函数商}＋\textbf{非平方层密度}＋\textbf{非等价蕴含链} ✓$$

## §5 ⭐ 为什么第 8 条不可省（关键）

$$\text{即使找到}\ D\ \text{且}\ \textbf{独立证明} \text{其横坐标为}\ \tfrac12，\ \text{若}\ D\ \text{与}\ \zeta\ \text{零点}\ \textbf{无关联} ⟹ \textbf{对 RH 毫无作用} ✓✓$$
$$\qquad \text{（例：§2 的}\ 1/\zeta(2s)\ \text{横坐标}\ \tfrac12\ \textbf{可证}，\ \text{但它对}\ \beta_*\ \textbf{一句话也没说}）✓✓✓$$
$$\text{而"与}\ \zeta\ \text{的关联"在本项目已穷尽的通道里只有三条}：$$
$$\qquad \text{(i)}\ \textbf{显式公式}：\text{`V188` 饱和}（\text{线性统计已由显式公式＋算术侧联合决定}）⟹ \textbf{无新信息} ✓$$
$$\qquad \text{(ii)}\ \textbf{正性}：\text{`V199`／`V185`／`V244` 角 I}（\text{Weil／Li}）⟹ \textbf{循环} ✓$$
$$\qquad \text{(iii)}\ \textbf{identification}：\text{`V215`–`V217`} \text{（canonical 接口）}⟹ \textbf{唯一残余} ✓✓✓$$
$$\Longrightarrow \textbf{第 8 条一旦落实，就落回 (iii)} = \text{`V215`–`V217` 的识别界面} ✓✓✓$$

## §6 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V256}：\text{T6 条件 4}\textbf{不是滤子（廉价）};\ \text{须补第 7、8 条};\ \text{补完后残余}\ \textbf{回到识别界面};\ \text{并提炼出"免费}\ \tfrac12\ \text{＝折半"这一机制级统一}} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| T6 条件 4（可证 $\tfrac12$）是否为滤子 | ✗ **不是**（平方层免费给出） | 本档 §2 引理 |
| 免费 $\tfrac12$ 的机制 | ⭐ **折半**（阶／区间／横坐标） | 本档 §3 ＋ `V218`／`V235`／`V253` |
| $\beta_*=\tfrac12$ 是否折半 | ✗ **不是**（谱陈述） | 本档 §3 |
| 规格须补 | 第 7 条（非平方层）＋ 第 8 条（非等价蕴含链） | 本档 §4–§5 |
| 补完后残余 | **识别界面 `V215`–`V217`** | 本档 §5 |
| 是否打开新方向 | ✗ **否**（规格自审后收敛到已有残余） | 本档 §6 |

$$\textbf{边界（诚实）}：\text{§2 引理与五例}\ \textbf{为初等、本档推导}（\text{平方层折半}）✓;\ \text{§3 的"全部免费}\ \tfrac12\ \text{都是折半"是}\textbf{[结构性] 综合} \text{（\text{样本为本项目五项结果}），}\textbf{不是分类定理} ⚠️;\ \text{§5 的"只有三条通道"引用本项目结论} ✓;\ \textbf{未用 RH};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 22:28）"继续"（承接 V254 §11 T6 对象型搜索规格）
⚠️ §2 廉价反例族（本档初等推导）：设 a_n=0 除非 n=k²，则 Σ a_n n^{-s}=Σ_k a_{k²} k^{-2s}
   ⟹ 横坐标＝（Σ_k a_{k²}k^{-σ} 的横坐标）折半
   成员：ζ(2s)｜1/ζ(2s)｜ζ(2s)/ζ(4s)=∏(1+p^{-2s})｜ζ(4s)/ζ(2s)=∏(1+p^{-2s})^{-1}｜更一般 Σ_k a_{k²}k^{-2s}
   全部横坐标恒为 1/2，全部不需要任何零点信息
   ⟹ "算术 + Dirichlet 型 + 横坐标可独立证明为 1/2" 是免费的 ⟹ T6 条件 4 不是滤子
   一致性：V235-A（Euler 层 E_r 自然横坐标 1/r，r=2 层＝平方层＝1/2＝(甲) 密度坐标）；V253（c=1/r）
⚠️ §3 机制级统一（本档提炼，[结构性] 综合）：免费 1/2 的所有来源都是"折半"
   V218 S1（自对合轴 k/2，把阶折半）｜V218 S3（归一化中点，把区间折半）｜V235-A（1/r，把横坐标折半）
   ｜V253（c=1/r）｜本档（平方层，把横坐标折半）
   ⟹ 免费 1/2 都是折半；折半是归一化，不是信息（与 V218 §5 一致）
   ⚠️ 对照：β*=1/2 不是折半，是谱陈述（右端零点实部）⟹ 数值相同、性质不同
⚠️ §4 规格须补：第 7 条（1/2 不得是平方层/1/r 密度坐标）；第 8 条（必须存在与 ζ 零点的非等价蕴含链）
⚠️ §5 第 8 条不可省（关键）：即使独立证明 D 横坐标为 1/2，若 D 与 ζ 零点无关联则对 RH 毫无作用
   （例：§2 的 1/ζ(2s) 横坐标 1/2 可证，但对 β* 一句话也没说）
   "与 ζ 的关联"只有三条：(i) 显式公式＝V188 饱和（无新信息）(ii) 正性＝V199/V185/V244 角 I（循环）
   (iii) identification＝V215–V217（唯一残余）⟹ 第 8 条一旦落实就落回识别界面
⚠️ §6 判词：T6 条件 4 不是滤子（廉价）；须补第 7、8 条；补完后残余回到识别界面；并提炼"免费 1/2＝折半"
   状态表：条件 4 非滤子✗｜免费 1/2 机制＝折半｜β*=1/2 非折半（谱陈述）｜须补第 7/8 条｜残余＝识别界面｜
   是否打开新方向＝否（规格自审后收敛到已有残余）
⚠️ 边界：§2 引理与五例为初等本档推导；§3 为 [结构性] 综合非分类定理；§5 引用本项目结论；
   未用 RH；未跑 Lean；零数值
✅ 净产出：① 廉价的 1/2 反例族（平方层折半，五个具体成员）⟹ 证明 T6 条件 4 不是滤子
   ② 机制级统一："算术中所有免费的 1/2 都是折半；折半是归一化不是信息"
   ③ 对照：β*=1/2 不是折半而是谱陈述
   ④ 规格须补第 7、8 条 ⑤ 补完后残余回到识别界面 V215–V217
   ⑥ 结论：T6 规格自审后不打开新方向（省下沿该规格盲搜的代价）
```

---

## §7 ⚠️ **勘误与压缩**（唐先生 2026-09-15 22:31；逐字采纳）

$$\textbf{T9（§4 降级）}：\S4\ \text{的"与}\ \zeta\ \text{的关联只有三条（显式公式／正性／identification）"}\ \textbf{继续标为综合审计结论}，\ \textbf{不升级为数学分类定理} ✓$$
$$\qquad ⚠️\ \text{尤其：}\textbf{未来可能出现目前档案没有覆盖的 correspondence／interface} ✓✓$$

$$\textbf{T10（识别出}\textbf{伪约束} \text{—— 本档真正的价值）}：\text{V256 真正有价值的}\ \textbf{不是"又关掉一条路"}，\ \text{而是识别出搜索规格中的一个}\ \textbf{伪约束}：$$
$$\qquad \boxed{\text{"可证明得到}\ \tfrac12\ \text{"本身}\ \textbf{几乎没有筛选力}} ✓✓✓$$
$$\qquad \text{平方层已给出任意廉价的}\ \tfrac12\ \text{横坐标} \Longrightarrow \textbf{真正困难的从来不是制造数字}\ \tfrac12，\ \text{而是制造}：$$
$$\qquad \qquad \boxed{\text{非归一化的}\ \tfrac12\quad+\quad\text{canonical arithmetic origin}\quad+\quad\text{与}\ \zeta\ \text{零点的}\textbf{非循环连接}} ✓✓✓$$

$$\textbf{T11（T6 修正版 —— 压缩成四条硬条件）}：\text{新对象}\ D\ \text{必须}\ \textbf{同时} \text{满足}：$$
$$\qquad \text{(1)}\ \tfrac12\ \textbf{不是} \text{通过 halving／}\tfrac1r\text{／normalization 得到};\qquad \text{(2)}\ D\ \text{的}\ \tfrac12\ \text{性质}\ \textbf{可以独立于 RH 证明};$$
$$\qquad \text{(3)}\ D\ \textbf{不只是}\ \zeta/L\text{-函数的重新编码};\qquad \text{(4)}\ \text{存在从}\ D\ \text{到}\ \zeta\ \textbf{零点位置} \text{的}\ \textbf{严格、非循环、非显式公式、非纯正性} \text{识别链} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{(1)(2)(3) 解决"假的}\ \tfrac12\text{"};\qquad \textbf{(4) 解决"假的 RH 信息"} ✓✓✓$$

$$\textbf{T12（搜索目标的压缩 —— 结论）}：\boxed{\text{此后"寻找一个自然的}\ \tfrac12\ \text{阈值"}\ \textbf{不再是有效搜索目标}} ✓✓✓$$
$$\qquad \text{真正目标已被进一步压缩为}：\boxed{\text{寻找一种}\ \textbf{此前档案尚未覆盖} \text{的}\ \textbf{arithmetic}\to\textbf{zero-location identification interface}} ✓✓✓✓$$
$$\qquad \text{这与}\ \text{`V215`–`V217`}\ \text{的 residual interface}\ \textbf{相接};\ \text{但}\ \textbf{V256 本身没有证明该 residual interface 已经穷尽} ⚠️✓$$
