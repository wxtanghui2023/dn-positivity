# E101 · ⭐⭐⭐ **purity 排除链的覆盖审计（③）** ✓ —— 先过 NO-GO 地图；结论：不是新坑，但**您的逻辑缺口成立** ✓

> 委托 ✓ 唐先生 21:23（"从③开始；**先看 NO-GO 地图，不希望重新掉坑**" ✓）
> 执行 ✓ 小灵｜依据 ✓：`MASTER-NOGO-AND-LIVE-PATHS.md` ✓、`CLOSED-ROUTES-MAP.md` ✓、`rct-four-layer-final.md` ✓、
> `AOB3/AOB4` 指针 ✓｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**本轮不做计算 ✓**

---

## 0. 结论（✓ 四条 ✓）

```
✅ **① 不是新坑 ✓**：您问的"char-0 Frobenius 本征值载体"**已在地图上** ✓
   —— 命中 **箱 6（谱/HP，无算术来源）** ✗ ＋ **箱 12（极化⊥元素性）** ✗
   —— 且地图有【直接的结构性理由】**F-4** ✓✓："**char p 的 Frobenius 是【元素】⟹ 可取本征值；
      char 0 只是【共轭类】⟹ 只能取 character/trace ⟹ L-函数** ⟹ 反复崩回 character 是**结构强制的**" ✓（[AOB3] ✓）
✅ **② 但您的逻辑缺口【成立】✓✓**：**F-4/F-5 排的是 class III（存在性/极化）✗**，
   **不排除 class II（archimedean/度量）✗** ⟹ $$\boxed{\textbf{"无 canonical similitude"}\ \not\Rightarrow\ \textbf{"无线性-}\varepsilon\text{ 载体"}}\ \checkmark$$
⭐⭐ **③ 地图 §E 已把这类问题的【性质】定性** ✓✓：**"在未枚举的无限空间上做否定 ＝ 每次删一个点 ⟹ 不收敛"** ✗
   —— **唯一能缩小范围的是【表征定理】** ✓✓ —— **您的问题【正是表征型】** ✓ ⟹ **方向正确** ✓
⭐⭐ **④ 于是 ③ 的正确形式 ＝ 攻【类表的完整性】** ✓（地图指定的唯一动作 ✓）：
   您的线性-$\varepsilon$ 载体属 **class II ∪ III** ✓ —— 两者**都已关** ✗ —— **但"类表是否完整"＝地图自己的 OPEN 问题** ✓✓
```

## 1. 先过地图（✓ 按 T1 关键词表 ＋ 四问 Q1–Q4 ✓）

| 检查 ✓ | 结果 |
|:--|:--|
| **关键词表（T1）** ✓ | 构想的词汇（Frobenius／carrier／**Spec ℤ candidates**／**谱流**／**canonical arithmetic duality**／**adelic positivity**／**ACD**／**AXD**／**τ-defect** ✓）**多在封闭表内** ✓ |
| ⚠️ **但关键词筛【不裁决】✗** | 关键词表是"**重命名检测**"（T1 ✓）—— 您的问题是**类级**的 ✗ ⟹ 须看**类表** ✓ |
| **Q1** 非 Euler 化？ | ✗ 若载体经 Euler 积 ⟹ **箱 2** ✗ |
| **Q2** 不变量非 character？ | ✗ 若只能给 character ⟹ **箱 1** ✗（此即 **F-4** 的结论 ✓） |
| **Q3** 谱/相位来自算术 canonical 算子？ | ± 若来自 ζ/零点反向定义 ⟹ **箱 5/6** ✗（**HP 陷阱** ✓） |
| **Q4** 依赖非 completion／非 L-值／非 generic？ | ✗ 否则 ⟹ **箱 3/4/12** ✗ |
| **P-Scale 筛** ✓ | ⚠️ 它只是**申报制**（申报尺度类型；height/log 型预筛淘汰 ✗）—— **【不排除】¬P-Scale 类** ✗ ⟹ **排除须由别处提供** ✓ |

## 2. ⭐ 地图上**直接针对**此问题的两条（✓ 逐字 ✓）

```
【F-4 ✓✓ 本轮关键 ✓】
   "char p 的 Frobenius 是【元素】⟹ 可取本征值；char 0 只是【共轭类】⟹ 只能取 character/trace ⟹ L-函数。
    ⟹ 全项目反复崩回 character 是【结构强制的】"                      [AOB3]
   ⟹ **这正是"char-0 Frobenius 本征值载体"的死因** ✓✓ —— **且是结构性的，不是"未找到"** ✓
【F-5 ✓】
   "极化 ⟂（元素性 + 动力学 + 相位）：E+D+Z 需非刚性；P 需正定"       [AOB4]
   ⟹ 即"**纯度载体的正定性**"与"**非平凡活动所需的非刚性**"互斥 ✓
【箱 12 ✓】"正定（Hodge–Riemann；pure 极化 HS 半单）与「非平凡活动」互斥｜存在性终审：char 0 无 canonical similitude" ✓
```

## 3. ⚠️ 您的逻辑缺口（✓ 我核对后【确认成立】✓）

$$\text{F-4/F-5 ⟹ 排除}\ \underbrace{\{A\ \text{带 canonical similitude}\ q^{-1}A^*QA=Q\}}_{\textbf{class III：存在性/极化}}\ ✗$$
$$\text{但【不】排除}\ \underbrace{\{|\alpha_\rho|-1\asymp\varepsilon\ \text{经 size/度量或非极化结构}\}}_{\textbf{class II：archimedean/度量}}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{"char 0 无 canonical similitude"}\ \not\Rightarrow\ \textbf{"char 0 无线性-}\varepsilon\text{ 载体"}}\ \checkmark$$

```
⚠️ **故地图现有排除是【分布式】的** ✗（箱 1／2／4／5／6／12 ＋ F-4/F-5 各管一段 ✓）
   —— **没有一条【覆盖式】论证** ✗ ⟹ 与您的判断一致 ✓
```

## 4. ⭐⭐ 地图 §E 已给出这种问题的**正确处置**（✓ 逐字 ✓）

$$\textbf{§E.2 ✓：}\boxed{\text{能真正缩小范围的只有【表征定理】——"一切候选都属于这 }N\text{ 类"（并给出证明）}}$$
```
§E.1 诚实诊断 ✓：约 25 轮 ⟹ 只建立约 12 个箱 ⟹ 后段多为【同一批箱的重复推导】✗
§E.3 类表 ✓（4 类 → 6 类 ✓）：I 不变性 ✗｜II archimedean/度量 ✗｜III 存在性 ✗｜
   V 极值/禁止模式 ✗（新 ✓）｜VI 可定义性/正则性 ✗（新 ✓）｜**IV 证明论 —— OPEN（只给可证性 ✗）**
§E.4 ⭐ **活的问题只剩一个** ✓：$$\textbf{这张类表【是否完整】？}$$
```
$$\Longrightarrow\ \boxed{\textbf{您这一问 ＝ 表征型问题 ＝ 地图指定的【唯一正确动作】}\ \checkmark\ \text{（不是"再加候选" ✗）}}$$

## 5. ⭐⭐ 把您的判据**落到类表**上（✓ 本轮实质产出 ✓）

$$\text{您的线性-}\varepsilon\text{ 载体（}\exists\Phi:\ |\Phi(\tfrac12+i\gamma)|=1,\ \partial_\sigma\log|\Phi|\asymp1\text{ 且 canonical 算术产生 ✓）}$$
$$\Longrightarrow\ \text{它只能落在}\ \textbf{class II（度量/size ✓）}\ \text{或}\ \textbf{class III（存在性/极化 ✓）}$$

| 若属 | 由谁排除 | 是否覆盖 |
|:--|:--|:--|
| **class III**（经极化/纯度 ✓） | **箱 12 ＋ F-5** ✗ | ✅ 覆盖 ✓ |
| **class II**（经度量/尺寸 ✓） | **箱 3（profinite/全不连通）＋ 箱 5（计数/熵/增长指数）** ✗ | ⚠️ **覆盖须逐一核** ✗ |

⟹ ⭐ **故 ③ 的尖锐形式（＝您 §10 的二分 ✓，用地图语言重写 ✓）**：
$$\boxed{\text{所有 canonical non-pure char-0 载体，是否都落入 class II ∪ III（⟹ 已有箱）？}}$$
$$\text{YES}\ \Longrightarrow\ \text{空间【真关】}\ ✗\qquad\text{NO}\ \Longrightarrow\ \textbf{出现表外新类}\ \checkmark\ \text{（结构性新方向 ✓）}$$

## 6. 不重复掉坑的**核对清单**（✓ 逐步 ✓）

```
□ 核对【箱 5】的覆盖力 ✓：其签名是"轨道计数／Lyapunov／谱半径／transfer operator／dynamical zeta" ✓
   —— 您的"metrics/size 型 ε-载体"是否**必然**属此？✗（**这是最可能的缺口位置** ⚠️）
□ 核对【箱 3】✓：其签名是"离散阶段逆极限／congruence／Stone" ✓ —— 是否覆盖"非 completion 的尺寸载体"？✗
□ 核对【VI 可定义性】✓：是否覆盖"canonical 构造 ⟹ 可定义"？✗（**新类往往从"不可定义"处漏出** ⚠️）
□ 核对【IV 证明论】✓（唯一 OPEN ✓，但只给可证性 ✗）
□ 核对 **F-4** 的完整推理链 ✓：**"共轭类 ⟹ trace ⟹ L-函数 ⟹ γ-依赖坐标 ⟹ ε/γ²"** ✓
   —— ⚠️ **最后两步"⟹ γ-依赖 ⟹ ε/γ²"在 AOB3 的存档里是否已写足？** ✗（**这是本轮该读的原文** ✓）
```

## 7. 边界与纪律（✓）

```
⚠️ **未宣布缺口真实** ✗ —— 只判"现有排除是分布式的、缺一条覆盖论证" ✓
⚠️ **未宣布 map 已错** ✗ —— F-4 是**结构性理由** ✓，我未找到与之矛盾的事实 ✓
✓ **本轮无计算** ✓（照您指示 ✓）；**未穷举 τ-Li／高阶 Li／$\xi^{(k)}$** ✗
✓ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **建议下一步 ✓**：读 **AOB3（F-4 的出处 ✓）＋ AOB4（F-5 的出处 ✓）原文** ✓，
   核对 F-4 的推理链是否**真的**把"共轭类"逼到"ε/γ²" ✗ —— 若中间有跳跃 ⟹ **缺口位置确定** ✓
```

---

## 8. ⭐⭐⭐ **F-4 出处原文核对（AOB3）** ✓ —— **缺口精确定位：真实** ✓

### 8.1 F-4 的逐字来源（AOB3 §1 ✓）

```
char p ✓：Gal(F̄_q/F_q) 是【pro-cyclic】⟹ 存在 canonical 生成元 Frobenius
          ⟹ 可对【元素】取【本征值】⟹ 本征值同时带【模】√q 与【辐角】θ ✓✓
char 0 ✗：Frobenius（在 p 处）只是 Gal(Q̄/Q) 的【共轭类】，不是元素
          —— 共轭类【不能】canonically 取本征值（代表元需选择 ⟹ 非 canonical ✗）
          —— 共轭类 canonically 可探测的【唯一】方式 = 【character / trace】（Chebotarev / Artin）
          ⟹ canonical 输出自动是 character 型 ⟹ L-函数 ⟹ **β-盲** ✓✓✓
```

### 8.2 AOB3 §2–§3：两条全局候选（✓ 逐字要点 ✓）

| 路线 | canonical 算子 | 结果 |
|:--|:--|:--|
| **(i) Galois 侧** | ✗（只是共轭类） | character/trace ⟹ L-函数 ⟹ **β-盲** ✗ |
| **(ii) 非 Galois 侧**（Deninger 型 flow／derivation，生成元**不是**共轭类 ✓） | ✓ **有** canonical 生成元 | **需 canonical polarization** $\Phi^{\dagger}Q\Phi=NQ$；**char 0 缺相交形式/正性** ✗ |
| **§2 ✓ 局部** | — | char 0 有【局部】similitude（Deligne／Ramanujan ✓）⟹ 给出 **Euler 因子** ✓ —— **但零点在窗口之外（$0\le\sigma\le1$）⟹ 局部 similitude 看不到零点** ✗（**算术断裂** ✓） |

### 8.3 ⭐⭐ 缺口定位（本轮实质产出 ✓✓）

$$\text{(α) Galois 侧 ⟹ }\textbf{β-盲}\ \checkmark\quad\text{（强 ✓：连 }\varepsilon\text{ 都看不见 ⟹ 覆盖 ✓）}$$
$$\text{(β) 非 Galois 侧 ⟹ 排除理由 ＝ 【缺 canonical polarization】✗}$$

$$\boxed{\textbf{关键区分 ✓}：\text{极化是【证明 RH】所需 ✓；而您的路线只需【线性 }\varepsilon\text{ 响应】✗}}$$

```
⭐ **故 (β) 封掉的是**"用极性一次性把谱压到圆上（$|\alpha|=\sqrt N$）"✗ ——
   **它未封掉**"一个 canonical 非 Galois 算子的谱，其模偏离按 $\varepsilon$ 线性（而非 $\varepsilon/\gamma^{2}$）" ✗✓
⟹ ⟹ **这是一个本项目从未问过的【更弱问题】** ✓：
   项目全部排除都瞄准"**直接证 RH**" ✓；您的载体只需服务一条**转换/检测定理** ✓
   ⟹ **更弱的需求从未成为排除目标** ✗ ⟹ **缺口真实** ✓✓
⚠️ **但缺口的内容是【开放的】** ✗ —— 不是"已证存在" ✓：
   · 须 canonical ＋ 算术特异 ✓（否则退化为平凡的 $\Phi=\exp(c(s-\frac12))$ ✗）
   · 须 $\partial_\sigma\log|\Phi|\asymp1$ ✓（即 $\neg$P-Scale ✓）
   · 须能看见 global zeros ✓（非仅 Euler 窗口 ✓ —— §2 的算术断裂是**最硬的一条** ⚠️）
```

### 8.4 ⚠️ 但**§2 的算术断裂**可能才是真正的墙（✓ 诚实标注 ✓）

```
AOB3 §2 ✓ 已记：**局部 similitude 只看得到 $\sigma>1$ 的 Euler 窗口** ✓
   ⟹ 任何**局部分解型**载体在 $\sigma\le1$ **结构性看不见零点** ✗
⟹ ⭐ 故 (β) 的**真正力量**可能不在"缺极化" ✗，而在**"缺全局性"** ✓：
   即：**非 Galois canonical 算子要"看见零点"就必须是【全局的】（非 Euler 因子型）** ✓
   —— 而这正是 Deninger 纲领的**无限维上同调 + 正性**停点 ✓（[已注册·本项目] ✓）
⟹ **故两条可能**：
   ① 若"看见 global zeros" ⟹ 必然已蕴含"global 正性/极化" ⟹ (β) **覆盖** ✓ ⟹ 缺口假 ✗
   ② 若存在"看见 global zeros"而**无需**极化的 canonical 全局算子 ⟹ **缺口真** ✓✓
⟹ ⭐⭐ **这正是 §6 清单里该核对的第一项** ✓ —— 也是**唯一真正的判定点** ✓
```

### 8.5 结论与边界（✓）

$$\boxed{\text{③ 的审计结论}：\textbf{现有排除（F-4/F-5/箱12）瞄准"直接证 RH"，未覆盖"线性 }\varepsilon\text{ 载体"这一更弱类}\ \checkmark}$$
```
⚠️ **未宣布缺口为"真"** ✗ —— 它**归结为**一个明确的二择一 ✓（§8.4 ✓）：
   "看见 global zeros" ⇒ 是否必然蕴含 global 正性/极化？
   YES ⟹ 覆盖 ✓ 缺口假 ✗｜NO ⟹ **表外新类** ✓ LIVE ✓
✓ **未重复掉坑** ✓：已过 T1 关键词表 ✓、四问 Q1–Q4 ✓、十二箱 ✓、F-1–F-8 ✓、§E 类表 ✓
✓ **本轮无计算** ✓；**未用 RH** ✓；**未跑 Lean** ✓
⭐ **下一步（唯一）** ✓：读 **AOB4**（F-5 的出处 ✓：E+D+Z 与 P 的互斥证明 ✓）
   ＋ 核 **"看见全局零点是否必然蕴含全局正性"** ✓ —— 即 §8.4 的二择一 ✓
```
