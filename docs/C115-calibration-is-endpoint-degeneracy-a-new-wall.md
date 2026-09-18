已查地图（所查：`C-111`（`C6` 第一刀；`§0(1)` 目标重述 ＋ `§2` 微定理）、`CLOSED-ROUTES-MAP.md:228`（DBN 判词：`RH ⟺ Λ≤0`；`Λ≥0` 无条件（Rodgers–Tao）；上界 `0.22`（Polymath 15）；要证 `Λ≤0` 即证 RH ⟹ **循环**）、`POS1`（正性 ⟺ RH）、`V188` §2（线性饱和；反演到逐点需无界精度）、`V193` §④／§⑤／§⑥、`FZ-3` 二分、`C68-SPEC` `F1`–`F8`、`C-114`）。**结论**：唐先生 16:47 的**校准基本正确，本档接受**，但需把 `C-111` 里混着的**两件事分开**：**(A) 等价性层**：目标 `Λ≤0` **确实**⟺ RH（`Λ≥0` 为 Rodgers–Tao 定理 ⟹ 开放半边＝`Λ≤0`／`Λ=0`）——这一层**完全如唐先生所说**✓✓；**(B) 机制层**：`C-111` 的"端点退化"**不是**该等价性的重述，而是**局部解析结构**：碰撞处离线距离 `=√(2(Λ−t))` ⟹ **Hölder-1/2** ⟹ 导数 `≍(Λ−t)^{−1/2}` 发散 ⟹ **均匀转移不可能**✓✓；⟹ **作为"路线墙"，它确实不是新墙**（缩减为 `Λ≤0` ⟺ RH，与"正性 ⟺ RH"同墙异述）——**接受校准**；**`C-111` 的净保留＝技术级判据 `F3`**（检查临界事件是否 `Hölder-1/2` 分支），可复用但**不是新墙**✓；并**实质同意**唐先生的"结构性宿命"判断（其档案理由见 §3）✓✓

# C-115 · **校准检查：`C-111` 的"端点退化"是不是新墙**

> **时间**：2026-09-18 16:47 唐先生：**校准检查**——问 `C-111` 的"端点退化"判词是否**就是** `Λ≤0 ⟺ RH` 这件事；若是，则"`β` 可见但卡端点"＝**同一堵墙的另一表述**，而非新墙；并提"**结构性宿命**"判断 ✓

---

## §0 结论（先行）

$$\textbf{(A)}\ ⭐\ \textbf{目标读法：完全正确}✓✓$$
$$\qquad \text{`C-111` §0(1) 逐字}：\text{因}\ \Lambda\ge0\ \text{是定理（Rodgers--Tao）} \Longrightarrow \text{RH}\iff\boxed{\Lambda=0};\ \text{开放半边}＝\Lambda\le0✓$$
$$\qquad \Longrightarrow\ \text{唐先生的翻译}\ \textbf{正确}：\Lambda\ \text{确实"感知"}\ \beta（\text{定义即"跟踪零点是否在临界线上"}），\ \text{但证}\ \Lambda\le0\ \textbf{本身}\iff\text{RH}✓✓$$
$$\textbf{(B)}\ ⚠️\ \text{但"端点退化"}\ \textbf{不是} \text{该等价性的重述——它是}\ \textbf{机制}：✓$$
$$\qquad \text{碰撞处离线距离}=\sqrt{2(\Lambda-t)} \Longrightarrow \textbf{Hölder-1/2} \Longrightarrow \Bigl|\frac{d}{dt}\text{off}\Bigr|\asymp(\Lambda-t)^{-1/2}\to\infty \Longrightarrow \textbf{均匀转移不可能}✓✓$$
$$\qquad \Longrightarrow\ \text{即：它说的是}\ \textbf{"沿光滑形变的均匀估计到不了端点"}，\ \text{而}\ \textbf{不是} \text{"}\Lambda\le0\ \text{等价于 RH"}✓$$
$$\textbf{(C)}\ ⚠️\ \textbf{但作为"路线墙"，唐先生是对的：不是新墙}✓✓$$
$$\qquad \because\ \text{由 (B) 可推出}：\text{唯一两条路}＝\text{(i) 均匀光滑转移（(B) 已排除）};\ \text{(ii) 非微扰／检测分支的论证} \Longrightarrow \text{那}\ \textbf{就是}\ \Lambda\le0✓$$
$$\qquad \Longrightarrow\ \text{作为}\ \textbf{路线}，\ \text{缩减为}\ \Lambda\le0\iff\text{RH} \Longrightarrow \textbf{与"正性}\iff\text{RH"}\ \textbf{同墙异述}✓✓\ \textbf{接受校准}✓$$
$$\textbf{(D)}\ \text{`C-111` 的净保留}＝\textbf{技术级判据}（`F3`）：\text{检查临界事件是否}\ \textbf{Hölder-1/2 分支} \Longrightarrow \text{可复用，但}\ \textbf{不是新墙}✓$$
$$\textbf{(E)}\ ⭐\ \textbf{唐先生的"结构性宿命"判断：实质同意}（\text{结构性，非定理级}）✓✓\ \text{理由见 §3}✓$$

---

## §1 为什么两件事会被混在一起（`C-111` 的表述问题）

$$\text{`C-111` §0 同时写了}：\text{(1) 目标}＝\Lambda=0（\text{等价性层}）;\ \text{(2) 微定理（机制层）};\ \text{(3) "判词：}\text{`C6`}\ \text{在 DBN 实现上 DEAD"}✓$$
$$\qquad \text{而 §0(4) 又写"墙}＝\text{端点退化}，\textbf{不是}\ \beta\ \text{盲"} \Longrightarrow \text{这句}\ \textbf{措辞失当}：✓$$
$$\qquad \qquad \text{它}\ \textbf{只应} \text{指"}\textbf{机制上}\ \text{与}\ \beta\ \text{盲是两种不同的失败方式"};\ \text{而}\ \textbf{不应} \text{暗示"这是}\ \textbf{一堵新墙}"✓✓$$
$$\Longrightarrow\ \text{本档修正措辞}：\boxed{\text{DBN 路线的}\ \textbf{失败方式} \ne \beta\ \text{盲}\ \text{（机制不同）};\ \text{但其}\ \textbf{墙的内容} ＝ \Lambda\le0\iff\text{RH}\ \text{（与正性墙同一堵）}}✓✓$$

## §2 校准逐条

| 唐先生的判断 | 本档 |
|:--|:--|
| `Λ` 确实能感知 `β`（定义即跟踪零点是否在临界线上）| **同意** ✓ |
| 但证 `Λ≤0` 本身 ⟺ RH | **同意** ✓ |
| 故"`β` 可见但卡端点"＝同一堵墙的另一表述，非新墙 | **同意（作为路线）** ✓，但机制层须另记（§0(B)）|
| `C-114` §4"目标＝找第二种 `β` 可见输出类型" | **方向对但措辞不准**（见 §4）|
| 任何真正 `β` 可见的量，只要依赖精确／连续／非退化，几乎必然在某点等价于或蕴含 RH | **实质同意**（结构性；见 §3）|

## §3 ⭐ "结构性宿命"的档案理由（为什么几乎必然）

$$\text{`β` 可见} \Longrightarrow \text{该量}\ \textbf{非聚合}（\text{聚合只能读重数／计数} \Longrightarrow \text{撞}\ 0.6818287） \Longrightarrow \text{必须}\ \textbf{位置级}✓$$
$$\qquad \text{而}\ \text{`V188` §2}：\text{canonical 数据}\ \textbf{只给线性统计量}（\text{饱和}）;\ \textbf{反演到位置级需}\ \textbf{无界精度}✓✓$$
$$\qquad \qquad \Longrightarrow\ \text{位置级判定}\ \textbf{就是}\ S(T)\ \text{问题} \Longrightarrow \text{强度}＝\text{RH}✓✓$$
$$\Longrightarrow\ \boxed{\text{"}\beta\ \text{可见 ⟹ 非聚合 ⟹ 位置级 ⟹ 反演饱和数据 ⟹ RH 强度"}}\ \text{—— 即}\ \text{`FZ-3`}\ \text{②\ 从新方向到达}✓✓$$
$$\qquad ⚠️\ \textbf{但它是结构性判断，非定理};\ \text{唯一可能的例外形状}＝\text{`V193` §⑤ 残余}：✓$$
$$\qquad \qquad \boxed{\text{"}\beta\text{-敏感、但既非重数／指标、也非二次型、也非逐点"的算术对象}} \Longrightarrow \textbf{当前 0 例}✓✓$$
$$\qquad \Longrightarrow\ \text{若唐先生的判断被升为定理，则等价于：}\textbf{RH 不可由任何"}\beta\text{-忠实检测器型"方法证明}✓\（\text{这是一个强元陈述，目前只是结构性}）$$

## §4 措辞修正（`C-114` §4）

$$\text{原写}：\text{目标}＝\text{找}\ \textbf{第二种}\ \beta\ \text{可见输出类型}（\text{非形变参数}）✓$$
$$\text{应写}：\boxed{\text{目标}＝\text{找一个}\ \beta\ \textbf{可见}、\textbf{且其值可在不引入 RH 强度输入的前提下被证明} \text{的量}}✓✓$$
$$\qquad \Longrightarrow\ \text{这正是}\ \text{`C68-SPEC`}\ \text{的}\ \boxed{\text{F5}}（\text{含独立算术输入，不与 RH 等价}）✓✓$$
$$\qquad \Longrightarrow\ \textbf{结论}：\text{`F5` 是}\ \textbf{绑定约束};\ \text{与}\ \textbf{六次同址收敛}（\text{`C-30/31/32`}、\text{`C-61` §2C}、\text{`C-64/65`}）\ \textbf{同一条}✓✓$$

## §5 边界

- `[档案]` §3 的 `V188` §2、`V193` §⑤、`FZ-3` ② 与 §0 的 `:228` 均**逐字引用** ✓
- `[本档]` §0(C)(D)(E)、§1 的表述问题诊断、§4 的措辞修正为**本档工作** ✓
- **不声称**："结构性宿命"是定理 ✗（仅结构性）；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 16:5x）`[纪律]`（先跑后写）

```
技术词 同墙异述      命中文件数=1  :: ./C115-calibration-is-endpoint-degeneracy-a-new-wall.md
技术词 结构性宿命      命中文件数=1  :: ./C115-calibration-is-endpoint-degeneracy-a-new-wall.md
技术词 失败方式区分     命中文件数=1  :: ./C115-calibration-is-endpoint-degeneracy-a-new-wall.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓
