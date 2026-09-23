已查地图：命中（`W6-MAJORANT-1{a..g}`／`C-263`／`C-264`／`C-98`／`C-102`／`E4-0` 等既有档）⟹ **引用，不开新案** ✓

# **`WALL-BREAK` 线登记**：`RH bridge-search` 冻结／**墙攻击重新开放**；`WB-A`／`WB-B` 两根墙

**唐先生裁示（2026-09-23 12:07）**：
① ⭐ **修正冻结对象**：$$\boxed{\text{冻结的是"继续找 RH bridge"；\textbf{不冻结}的是"攻击两面墙本身"}}$$ ✓✓
　（理由：前面的"冻结"只回答"**现有入口能不能搭桥**"，**没有回答"墙本身能不能被打穿"** ✓）
② **七墙逐墙破墙审计** ⟹ 找出**真正尚未被打穿**的核心障碍 ⟹ **压缩成 1–2 个根难点** ⟹ 对根难点**强攻或迂回** ✓
③ ⛔ **不再注册 `IP-3`／`IP-4` 类候选**；直接建 **`WALL-BREAK` 实验**：**`WB-A` Arithmetic Visibility**｜**`WB-B` Global Coercivity**；第一轮**必须可算、可判死** ✓
④ ⭐ **`WB-B` 优先从 `W6` 的完整 `K_T` 入手**（有具体公式、已定位失败点、**明确的相消可能性**），**不从抽象概念重新发明对象** ✓

D0: 本档对象 = **`WALL-BREAK` 线登记（七墙状态 ＋ 两根墙 ＋ 首刀定义）**（引既有档；**未开 RH bridge 案** ✓）
D1: 0 （本档为 [REVIEW] 轮次：登记／审计；首刀执行时另建 [RESEARCH] 轮次 ✓）
FREEZE-ACK: D1=0（本档为 [REVIEW]）（依 §8.1-AMEND-1 ✓）
[REVIEW]

---

## §1 **七墙状态表（照录 ✓✓）**

| 墙 | 当前状态 | 真正攻击点 |
|:--|:--|:--|
| **`β`-blind** | **OPEN** | **`β` 的高阶／组合可见性**（不是"`β` 如何等价 RH"）✓ |
| **local** | **OPEN** | **local → forbidden global configuration**（不要求 local 单独定谱）✓ |
| **parity** | **OPEN** | **构造 parity 不作用的 quantity**（离开 parity observable，而非破解 parity principle）✓ |
| **majorant** | **粗路线 CLOSED** | **signed／structured majorant** ✓ |
| **correlation** | **统计路线 CLOSED** | **correlation defect／signed witness** ✓ |
| **zero-statistics** | **单独路线 CLOSED** | **rigidity → forbidden configuration**（统计须升级为全局一致性约束）✓ |
| **`W6`** | **generic majorant FAIL** | **`K_T` cancellation／cross-scale structure** ✓ |

## §2 ⭐ **压缩：两根墙（照录 ✓✓）**

```
【根墙 A：Arithmetic Visibility】 涉及 **`β`-blind ＋ local ＋ parity**；共同问题：
　$$\boxed{\text{arithmetic 信息到底以什么形式进入一个最终能够约束 global object 的 quantity？}}$$ ✓
　（三者分别表现为：`β` **看不见**｜local **看得到但只在局部**｜parity **看得到但信息被筛掉** ✓）
　⟹ 母问题：**怎样构造一个 arithmetic-visible、跨尺度、非 parity-blind 的 quantity？** ✓
【根墙 B：Global Coercivity】 涉及 **majorant ＋ correlation ＋ zero-statistics ＋ `W6`**；共同问题：
　$$\boxed{\text{已有的 global／谱信息，如何从"平均·统计·正性·检测"升级成"对坏配置的强制排除"？}}$$ ✓
　（四者同一断裂：majorant **控制不够强**｜correlation **有相关无排除**｜zero-statistics **检测到结构但非 pointwise exclusion**｜`W6` **cross-scale coercivity 在 `O_1` 处断掉** ✓）
　⟹ 母问题：**能否构造 signed／structured／cross-scale coercive quantity，使 off-line configuration 自动产生不可容忍的缺陷？** ✓
```

## §3 **档案核验：`K_T` 的已知结构（`WB-B` 的起点 ✓✓）**

```
【`W6-MAJORANT-1b` 逐字】 「实际 `K_T`：**乘子＝四个被 `\Phi^2` 抹平的平移 sign，全部跳变落在 `[T,2T]`**」⟹
　$$\boxed{\text{唐先生②的裸 Hilbert 障碍在 }K_T\text{ 上不存在}}$$ ✓✓（`1c` 复述为"**彻底不成立**" ✓）
【`1e` 逐字】 `\|K_T\|\gtrsim\frac{X}{\log X}`；两侧 `a_n` 精确纳入后**整体 bilinear 尺度 `O(X)`** ✓
【`1g` 逐字】 **cross-`X>T` 路线 FAIL**（`J1` 勘误改写为 **`J3`**）✓；残留闸门 `J3`：**离散 `\log n` 网格采样密度 `\asymp X` 不消失**；**任何有限阶 smoothness 只给 log-saving** ⟹ 破不了幂次障碍 ✓
【⟹ 由此得到的精确问题（本档 ✓✓）】 $$K_T\text{ 的 four-sign 结构，能否给出 \textbf{signed estimate} 以绕开 }|K_T|\ \text{majorant 的损耗？}$$
　$$\text{还是说：残留障碍 }J3\ \text{（离散采样密度）对 sign 结构\textbf{是盲的}？}$$ ✓✓
```

## §4 **首刀定义（`WB-B`，可算可判死 ✓✓）**

```
【`WB-B` 首刀（最窄，一轮内可判定）】 对 `K_T=\sum_{\epsilon\in\{\pm\}^4}` 四个平移 sign 分量，
　**显式写出其两两配对／相消结构**，判定下列二者之一：
　**(α) 存在可证恒等式／不等式**：使 `|\langle K_T f,g\rangle|` 的界**严格优于** `\|K_T\|\cdot\|f\|\cdot\|g\|` 型 absolute-value 界（＝真 `signed estimate` ✓）
　**(β) 或证明**：`J3`（离散 `\log n` 网格密度 `\asymp X`）**对 sign 结构盲** ⟹ 相消**无法**改善幂次 ⟹ **`WB-B` 在 `K_T` 上 CLOSED（有内容）** ✓
【判死规则（预先登记 ✓）】 若首刀只能重述"取绝对值 → MV/Hilbert → Cauchy" ⟹ **立即 CLOSED**（依令：generic majorant 无需再做 ✓）
【`WB-A` 首刀（次优先）】 判定「**是否存在一个 single-point `β`-blind、但在 pair／higher-order 上 `β`-visible 的 invariant**」⟹
　可算形式：在既有 pair/correlation 对象上检查 **`β` 可见性**（若已登记为 `β`-blind ⟹ 记 CLOSED；否则构造显式 witness ✓）
【与冻结协议一致性 ✓】 两首刀均属「**一轮内可判定的识别型问题**」⟹ 符合 §8.1-AMEND-1 唯一重开接口 ✓
```

## §5 边界与合规

```
✗ 未计算／未证 RH／未接 ζ｜⛔ 未把 localization／transport／realization 当候选机制 ✓
【本轮次分类】 `[REVIEW]`（登记）；`WB-B` 首刀执行时另建 `[RESEARCH]` ✓
【钩子合规】 已查地图 ✓｜`D0:`／`D1:` ✓｜无"新"性主张（若首刀宣称新性 ⟹ 将附【技术词回查】）✓
```
