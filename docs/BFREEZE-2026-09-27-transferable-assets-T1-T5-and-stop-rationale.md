# BFREEZE-2026-09-27 — B 档收口：可迁移资产 T1–T5 ＋ 停止理由（定稿）

**已查地图：未覆盖（本档＝既有资产之收口，非新案）**
所查：`docs/CLOSED-ROUTES-MAP.md`（关键词 `excess`｜`STOP`）｜`docs/MASTER-STATUS-AND-CLOSURES.md`｜`docs/ASSETS-REGISTRY.md`
⟹ 本档为 `CORE-2026-09-27` ＋ `CORE-2026-09-27b` 的**收口定型**（唐先生 2026-09-27 20:56 定稿）✓

D0: 本档对象 ＝ **档案已有**资产（T1–T5：`CORE-2026-09-27`／`CORE-2026-09-27b`／更早 Lemma A 档）的**收口定型**（重命名：否 ✗；新对象：无 ✗）
D1: 独立自由度 ＝ **0**（无新对象／新自由度；仅定型与登记 ✓）

---

## §1 停止理由（registry 用 · 唐先生 20:56 定稿 · **逐字保留**）

> **STOP：纯几何层的统一 overlap 下界为 $L\ge3$，而目标 $L\ge4$ 的第 4 个单位依赖 $E(A)$ 的专有尺寸耦合；继续枚举不能产生新的机制资产。**

**⚠️ 精确化登记（本档补 · 不改变上句的收口作用）** ✓
| 输入 | 可得下界 | 紧？ |
|---|---|---|
| **仅形状**（STAR／TRI，无 $E$ 信息） | $L\ge\mathbf{0}$ | 取等（全体 $\min L=0$ ✓） |
| **形状 ＋ $y^\ast\in E$**（STAR） | $L\ge\mathbf{3}$ | **取等**（1585 例 $\min L=3$ ✓✓） |
| **形状 ＋ $k$ 个角点 $\in E$**（TRI） | $L\ge 2k$ | **取等**（$\ge3$ 角点：93 例 $\min L=6$ ✓✓） |
⟹ 严格说法：**「几何 ＋ $E$-成员假设 $\Rightarrow L\ge3$」**；而 $E$-成员假设本身由**尺寸条件** $\Sigma\ge|E|$ 提供（742 个"特殊点 $\notin E$"四元组中候选 **0** 个）✓
⟹ 上句"纯几何层"应读作"**几何层（含其强制的 $E$-成员）**"，其**能力边界**结论不变 ✓✓

---

## §2 可迁移资产定型 T1–T5（lock ✓）

| 资产 | 内容 | 状态 |
|---|---|---|
| **T1** top-4 恒等式 | $\max_{|D|=4}\Sigma_D\|S_z\|=w_{(1)}{+}w_{(2)}{+}w_{(3)}{+}w_{(4)}$ ⟹ **excess 检验不再需要四元组枚举** | ✓ 已归档 |
| **T2** sharp excess | $\Sigma_D-\|E\|\le1$，且 $+1$ **确实现**（$A=(92,94,108,109)$）⟹ **sharp，非人为留余量** | ✓ 已归档 |
| **T3** Lemma A／A′／A″ | $\|B_1(z)\cap B_1(z')\|=2$（$d{=}1,2$）／$0$（$d\ge3$）＋ $Q(E)\subseteq\cup_{a}B_2(a)$ ＋ $\|S_z\|\le2\deg_A(z)$ | ✓ 已有 |
| **T4** 修正后的 $c\ge2$ 链 | **弃用** $c{=}0\Rightarrow\Sigma\le16$ ✗；改直用 $c\le1\Rightarrow\max\Sigma<\|E\|\Rightarrow c\ge2$ | ✓ 已归档 |
| **T5** STAR／TRI 形状二分 ＋ overlap ledger | $L_{\mathrm{STAR}}=3\cdot 1_{\{y^\ast\in E\}}+\#\{\text{6 中点}\in E\}$；$L_{\mathrm{TRI}}=2k$；纯几何统一仅到 $L\ge3$（经 $E$-成员）**不能**升到 $L\ge4$ | ✓ **本轮新增（最有价值）** |

---

## §3 最关键研究结论（boxed · 逐字定型）

$$\boxed{\text{geometry supplies }L\ge3,\quad \text{but the fourth unit requires }(A,E)\text{-specific coupling}.}$$

**读法** ✓：继续追求 index-free $L\ge4$ **会越过当前资产真正能提供的信息边界** ✓ —— 这不是"型分析做不下去"，而是**"为何做不下去"被提炼成了结构性结论** ✓✓

---

## §4 sharp 情形的双实现 ⟹ 削弱 distance-type classification 的收益 ✓

- excess$=1$ **仅**出现在 $A=(92,94,108,109)$（$|E|{=}18$）
- 该情形**同时**出现 **STAR（$L{=}7$，含 $n{=}4$ 公共点）×4** 与 **TRI（$L{=}6$）×1**
⟹ **excess$=1$ 无唯一几何实现机制** ✓ ⟹ 继续做纯 distance-type classification **收益削弱** ✓（支持收口）✓

---

## §5 本线完成的工作（压缩链陈述）

**$9{,}381{,}251$ 个局部交换 → 逐层压缩 → 少数可复用几何不变量 ＋ 纯几何机制的精确能力边界** ✓
（证书层：$9{,}381{,}251=7{,}723{,}409(\tau\ge6)+1{,}657{,}826(\text{容量})+16(\text{完整交叠})$；$\delta$-pattern $310{,}124\to56\to4$ —— 均见 `KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md` ✓，本档**不重述数字**）

**B ＝ machine certificate ＋ transferable mechanism ＝ 正确收口** ✓（**不是失败转场** ✓）

**不再行动** ✗：不扩枚举 ✗｜不重扫 873,472 ✗｜不优化 L3-α 证书 ✗｜不重启 distance-type classification ✗

---

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "overlap"
技术词 overlap          命中文件数=25   :: ./BFREEZE-2026-09-27-transferable-assets-T1-T5-and-stop-rationale.md ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md ./DELSARTE-2026-09-26-krawtchouk-route-and-the-a1-bound.md
$ bash scripts/tech_word_check.sh "overlap ledger"
技术词 overlap ledger   命中文件数=1    :: ./BFREEZE-2026-09-27-transferable-assets-T1-T5-and-stop-rationale.md
```
- **本档新增**：**0** 个术语 ✓（`overlap ledger` 命中 **1 档＝本档** ⟹ 仅为**标签级**首次使用，**不作新性主张** ✓ 紧签名原则 ✓）
- **档案已有（引用，不列为提出）**：`overlap`（25 档，其中 24 档为上游）｜`STAR`（27 档）｜`全距 2 型`（2 档）✓
- **通用词（不计）**：`excess`／`shape` ✓

## §7 红线

- 结论**仅限**该码（$n{=}10$、$C$＝124 词、该 16 例 $A$）✗；不外推 $K(10,1)$ ✗
- 不写"不存在／方向已死" ✗（V290）；只写"**本资产能提供的信息边界**" ✓
- 本档为**收口定型**（无新计算）✓；任何数值均引上游档，不新增 ✗
