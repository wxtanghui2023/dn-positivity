# AUDIT-2026-09-29zl — 查重：GPT 提的「$s(x)$ 开邻域 ＋ $C/C^c$ 分裂」方案**之前已测试过**

> 空间 B｜非 C 号｜唐先生问（22:51「这个方案之前测试过么？」）｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:1x

**已查地图**：`ASSETS-REGISTRY`（L745／L1897–1905）／`CLOSED-ROUTES-MAP`（L3272–3276）／`MASTER-FAILURE-MAP` §5（$r_q{=}2t_q$ 开邻域）／`RESULT-29o/29p`／今晚 `zg/zi/zh` ＋ `ERRATUM-n1`
D0: 本档对象 = **档案已有**（开邻域坐标／四恒等式）之**查重**（新数学对象：无 ✗）
D1: 0（产出 = **一份逐项对表 ＋ 一条结构判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{是 —— 该方案的核心 4 条恒等式与"开邻域坐标"均已被测试/登记};\ \text{唯一未跑过的一步（四变量凸包）\textbf{结构上不可能产生 gap}}}$$

## §1 逐项对表（**GPT 对象 ↔ 档案/今晚对象**，数值已双码核验）

| GPT 记号 | 等同对象 | 出处 | 数值核验 |
|---|---|---|---|
| $s(x)=\lvert C\cap S_1(x)\rvert$ | **开邻域码度**（档案 $t_x{=}OC(B_1(x))$ 族） | `RESULT-f`（$r_q{=}2t_q$）｜`CLOSED-ROUTES-MAP` L3272 | — |
| $W=\sum_{c\in C}\binom{s(c)}2=X_{112}$ | **我方 $P$**（$P=\sum_{y\in C}\binom{a_y}2$；$a_y{=}s(y)$） | 今晚 `SPEC-jia`／`ERRATUM-n1` F4 | 62-码 **6**／120-码 **41** 一致 ✓✓ |
| $X_{222}=\sum_x\binom{s(x)}3$ | **我方 $E$**（等边 (2,2,2) 三点组数；公共点**唯一**＝引理 T） | 今晚 `SPEC-jia` §2 | **42**／**97** 一致 ✓✓ |
| $W+H=2P_2$ | **我方 $F9$**：$2A_2=\sum_{x\notin C}\binom{\mu}2+P$ | 今晚 `AUDIT-zg` §6 | **132**／**298** 一致 ✓✓ |
| $\sum_x\binom{\mu}3=W+X_{222}$ | **恒等式 T** | `SPEC-jia` | **48**／**138** 一致 ✓✓ |
| $H\ge142-2P_1$ | $F7$ 之 $C^c$ 侧特化（$\binom s2\ge s-1$） | `ERRATUM-n1` | 成立 ✓ |
| $X_{222}^C,X_{222}^{\bar C}$ 分裂 | **我方 $F8$**：$E=\sum_{x\notin C}\binom{\mu}3+\sum_{y\in C}\binom{a_y}3$ | 今晚 `AUDIT-zg` §6 附 | **42=40+2**／**97=91+6** ✓✓ |
| 「112/222 独立，残差 12.83」 | **上一轮 `RESULT-29o/29p`**（三点构型计数独立于 $V_2$） | `HANDOVER` §2 (E)(F) | 逐字一致 ✓ |

$$\therefore\ \text{GPT 方案} = \underbrace{\text{今晚工作}}_{F4/F8/F9/恒等式T/引理T} + \underbrace{\text{档案已登记}}_{开邻域\ RESULT\text{-}f} + \underbrace{\text{上一轮}}_{29o/29p}$$

## §2 档案对"开邻域坐标"的既有判定（**关键**）

$$\text{`ASSETS-REGISTRY` L745}:\quad Q_2=\tfrac{(n-1)E-\sum_{x\notin C}OC(B_1(x))}2\ \text{—— 判定}:\ \textbf{「等价坐标转换，非新信息」}\ ✗$$
$$\text{`ASSETS-REGISTRY` L1899／L1904}:\ \text{「开邻域 incidence ＋ Walsh」}\ \Longrightarrow\ \textbf{STOP（已审计对象之第 3 次回潮）}\ ✗$$
$$\text{（复现守卫：任何 119/107-攻击\ \textbf{不可}再表为该已穷尽对象）}$$

## §3 唯一未跑过的一步：四变量"精确整数凸包" —— **实测无 gap**

$$\text{实跑（}M{=}106,\ P_1\in\{20,49,60,71\}\text{）}:\ \text{取}\ W{=}W_{\min},\ H{=}\max(H_{\min},142{-}2P_1),\ P_2{=}\tfrac{W+H}2,\ X^{C}_{222}{=}X^{C}_{222,\min},\ X^{\bar C}_{222}$$
$$\Longrightarrow\ \textbf{全部四例皆可行 ✓（无 gap）}$$
$$\boxed{\text{结构原因}:\ \text{该系统**全部约束方向皆为「≥」**（}H{=}2P_2{-}W\ \text{仅为定义式）} \Longrightarrow \text{取足够大的点即可满足} \Longrightarrow \textbf{不可能产生矛盾}}$$
$$\therefore\ \text{欲出 gap 须加\ \textbf{上界}（如 }P_2\le f(P_1)\ \text{或}\ W\le g(P_1)\text{）—— 那正是缺失的\ \textbf{实现层}}}

## §4 判定

- **是，已测试过** ✓（核心恒等式＝今晚；开邻域坐标＝档案 `RESULT-f`／已判"非新信息"；112/222 独立＝上一轮 29o/29p）
- **其"四变量凸包"一步**：结构上不可能出 gap（§3）
- **不是新机制**；与 `AUDIT-zj` 之类级标定（聚合/谱类连 $n{=}9$ 阈值都测不到）**一致**
- **仍然成立的一点**：GPT 指出"必须耦合"与"须有非聚合坐标"——**方向与今晚结论同向** ✓；但具体构造**已被覆盖**

## §5 边界（硬 ✓）

- **不主张** 107／任何新值 ✗；本档为**查重**（否定性），非新结果 ✓
- 数值核验皆在**已知码**上实跑（双码）✓；未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
