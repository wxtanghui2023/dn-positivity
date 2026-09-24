已查地图：命中（`HUNT-R2-OPEN-MATH-POOL-round1`／`HUNT-R3-screening-S1-S2-S3`／`TARGET-L9-CLOSURE-tau-consumed`／`II-D-CLOSED-and-why-RH-question`／`INDEPENDENT-PROBLEM-HUNT-round1`）⟹ 引用，不开新案
D0: 本档对象 = **研究层级 Pivot 落档**：`RH-centered → asset-centered independent-problem`；含技术资产逐项清单 ＋ 独立问题池（首批）＋ 五道新评价门
D1: 0 （[REVIEW] 轮次：层级登记与资产清点，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **Pivot：`RH-centered` → `asset-centered independent-problem`**

## §0 Pivot 内容（照录）

```
$$\boxed{\text{RH-centered search}\ \longrightarrow\ \text{asset-centered independent-problem search}}$$ ✓✓
**【目标式改写】** 研究资产 `\to` **独立数学问题**（**不是** 研究资产 `\to` RH 的另一个间接入口）✓
**【退出项（照录）】** `n=38`／`TARGET-L9`／`RH\ \text{bridge}` **退出下一轮的搜索入口**，**不再作为筛选目标** ✓✓
**【今日结果之重新解释（照录）】** `\tau` CLOSED ＋ `S1/S2/S3` 全 CLOSED 共同说明 $$\boxed{\text{RH 邻域的资产转化率已被连续实验验证为很低}}$$ —— **不是问题池为零** ✓✓
**【成功定义扩大（照录）】** 与 RH 无关的**新定理**／新组合结构**分类结果**／能解决某类有限约束问题的**新算法或新证书** —— **皆为成功**，只要不是简单重编码 ✓✓
```

## §1 ⭐ 技术资产逐项清点（附已验证证据）

```
**`A`｜有限几何 ＋ `\mathbb F_2` 结构**
　证据：`\mathrm{PG}(4,2)` 处理过（`31` 点／`155` 线）；`\mathrm{GL}(4,2)`（`20160`）完整轨道分解；`S_4`-归约（`330\to28`）；saturating set 判定；line-cover／cocycle 秩计算（`rank=104`、`516` 方程、`60` 维排除）✓
**`B`｜加法 × 乘法结构 ＋ 有限容量**
　证据：`EDS`／primitive divisor／rank of apparition（`r_q`）；`Z_S` 有限容量定理（`|Z_S|\le N_0+|S|`）；CAP 判定为 primitive-divisor 影子 ✓
**`C`｜机制审计体系**
　证据：`E-gate`／新量门／`SURVIVOR-5`／"忠实重编码检测"（`rank` 满秩判据）✓ —— 可迁移的**搜索过滤器** ✓
**`D`｜exact／证书机器**
　证据：盒覆盖全域证书（`118068` 箱、`0` 残差、独立校验器、`2^{96}` 体积记账、`9.73` 秒）＋ 大规模穷尽（`D(-3)`：`148` 边／`76` 三角／`#K_4=0`）＋ Lean 形式化（补齐 Mathlib 缺口）＋ 分钟级 shell 复现链 ✓
**`E`｜秩–迹／惯性机器**
　证据：`Lemma R`（`rank\ge2\mathrm{tr}P+4\mathrm{tr}Q-4b-\|P+Q\|^2`）；von Neumann 迹不等式次随机坐标 ＋ 三 gate 等号审计 ✓（注：其等号分类已判 prior art，**方法**仍在）✓
**`F`｜零点／素数数据处理**
　证据：解析数论数值工作（mpmath 高精度、零点定位、高斯/核方法、几乎周期与相位流分析）✓
**`G`｜跨尺度约束 ＋ 反例构造**
　证据：跨尺度"有限预算"判据；反例构造与地板分析（`14` missing incidences 型）；`H_m`／最近零点距离字典 ✓
**`H`｜新颖性审计纪律**
　证据：三层撞车模板（object／sign／application）；`tech_word_check.sh` 回查；pre-commit `NEWNESS` 门 ✓
```

## §2 ⭐ 新评价门（五道，照录您的顺序）

```
$$\text{Gate 1 独立性}\to\text{Gate 2 资产自然适配}\to\text{Gate 3 新数学量 }Q_{\rm new}\to\text{Gate 4 可出新结果}\to\text{Gate 5 RH（最后、可无）}$$ ✓✓
**Gate 2 的严格形式（照录）**：不是"这个问题也能写成 `\mathbb F_2`"，而是 $$\boxed{\text{我们已有的某个结构是否\textbf{自然成为该问题的核心变量}}}^{\vphantom{1}}$$ ✓✓
**Gate 3 的排除形式**：$$Q_{\rm new}\ \ne\ F(A,B,g,\tau,C)$$ ✓
```

## §3 独立问题池（首批 5 个，逐门判定）

| `#` | 独立问题 | 主场资产 | `G1` | `G2` | `G3` | `G4` | `G5` | 判定 |
|:--|:--|:--|:--:|:--:|:--:|:--:|:--:|:--|
| **`P1`** | **认证/审计型**：取一条**已发表的有限组合/数值断言**（缺机器可核证书），或给出**独立证书**，或**找出缺陷** | `D`＋`H` | ✓ | ✓ **核心法即其方法** | ✓（被认证的断言／缺陷） | ✓（证书或反例，**门允许**） | 可无 | **首选** ⚠️ 竞争：《wustep/maths》已在做同类"dent" |
| **`P2`** | 有限几何表缺口：`\mathrm{PG}(n,q)` 中 **saturating set／arc 小参数**精确值或分类 | `A`＋`D` | ✓ | ✓ **原生** | ✓（该参数值） | ✓（新值/分类） | 无 | **备选** ⚠️ **与 L9 同族文献**（同社区），撞车风险高 |
| **`P3`** | 结构矩阵族的**惯性/负指标界**：对某未研究族定 `n_-(M)` | `E`＋`D` | ✓ | ✓ 原生 | ✓（该族惯性界） | ✓（新界） | 无 | **备选** ⚠️ 需找**无 prior art 的族** |
| **`P4`** | Mathlib 缺口形式化 | `D` | ✓ | ✓ | ⛔ **`Q_{\rm new}` 不成立**（形式化不产生新量） | ✓ | 无 | **REJECT（`G3`）** |
| **`P5`** | "跨尺度约束算法"泛题 | `G` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 无 | **REJECT（过泛，无明确对象）** |

## §4 首攻与纪律

```
**【首攻】`P1`**：先做**30 分钟**定位——找一条**公开、有限、缺证书**的断言（候选域：有限组合分类、SAT/UNSAT 型穷尽断言、数值常数上界断言）✓
**【成功形态】** 独立可核证书 **或** 明确缺陷（后者本身即新反例）✓
**【⛔ 纪律】** 首攻阶段**只做外部断言定位与 30 分钟 prior-art/可得性核查**；**不碰** `n=38`／`TARGET-L9`／RH bridge／任何"能否帮 RH"的问题 ✓✓
【边界】 §0–§3 为**照录您的 Pivot 与资产判断** ＋ 本档清点；证据均取本线既有档（可核）；`P1`–`P3` 的撞车风险为**本档评估**（未做 30 分钟核查）；未制造候选／未启动搜索／未碰 RH。
