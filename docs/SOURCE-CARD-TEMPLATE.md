已查地图：命中（`E-20`／`E-22`／`E-23`／`AMEND-4/5/6` 本线自档）⟹ **引用，不开新案** ✓

# **`SOURCE CARD` 模板（候选进入实际计算前必写，仅五行）**

**依据**：`RESEARCH-CONSTITUTION` §8.1-AMEND-6（唐先生 2026-09-23 13:48 ✓）；⭐ 尤其 `STOP` 行 —— 当前最危险的不是漏掉候选，而是**不知不觉把一个来源又做成 `CAS`／`B`／`C` 的第四种实验** ✓

D0: 本档对象 = **`SOURCE CARD` 模板（执行纪律工具）**（引本线自档；**未开 bridge 案** ✓）
D1: 0 （`[REVIEW]` 轮次：模板登记，不主张新自由度 ✓）
FREEZE-ACK: D1=0 ✓
[REVIEW]

---

```
SOURCE:            <一句话：这个来源本身是什么数学对象/问题>

S1:                <脱离 RH 后，它本身是什么数学问题？>（须能独立成立：恒等式／组合计数／变换结构／递推／极值）
S2:                <它与 ζ/RH 的既有接口是什么？>（须是已有的、非人工制造的对应）
S3:                <第一笔计算的输入/输出是什么？>（⛔ 输入与一阶段输出都不得使用 β／rank／support／parity／majorant）
S4:                <若出现异常，什么"对象"可能被迫出现？>（须是对象级：如 Q_{m+1}=F(Q_m)／Q_m=0／Q_m=R_m·S_m；⛔ 只给常数/渐近律不合格）

STOP:              <什么结果立即证明该来源只是 CAS/B/C 的变体？>（照录：与"有限差分结构／算术双表示缺陷／算术↔零点表示"三类同型 ⟹ 立即 CLOSED）
```

**填写纪律**

```
① **不跑**：五行为空或含糊即视为不合格，⛔ 不得先跑再补 ✓
② **不合格样例（照录 `AMEND-6`）**：`S1` 专门为 RH 定义的量 ✗｜`S2` 算完再硬接 `\beta` ✗｜`S3` 一上来算 `rank`／`support`／`parity`／`majorant` ✗｜`S4` 只有 `Q(N)\sim cN^\alpha` ✗ ✓
③ **`S4` 为真瓶颈**：`Q_N=0` 未必够；须出现**非预先设计**、由计算逼迫出的结构 ✓
④ **0 号指标优先**：是否真的产生了新的数学对象？（`AMEND-5`）⟹ 0 号未过则不得进入 (1)-(4) 检查 ✓
⑤ ⛔ 不得以 parameter／order／window／matrix size 的变化替代 SOURCE 的变化 ✓
```

---

## §2 **`S4` 的 anti-post-hoc 声明（`AMEND-7`；⛔ 计算前必写，事后不得改写 ✓）**

```
【为什么】 $$\text{SOURCE 先验资格}\neq\text{候选机制资格}$$ ⟹ 进入研究轮的**唯一理由**＝**存在可预先声明的、可判定的 `S4` 对象生成检验** ✓
　（否则滑回"先算一堆数据，再从异常中找故事" ✗）
【模板追加行（写在 `S4` 之下）】
S4-PRE:            <预先声明：若出现何种结构，则何种"对象"被强迫出现？该检验如何判定？>
S4-ANTI-POST-HOC:  <四点自查（计算后填写，不得改写 S4-PRE）：
                    1) F 的形式不是预选来拟合数据的；
                    2) 至少第二层/第二尺度迫使同一结构；
                    3) F 不是既有恒等式/Euler–Dirichlet/有限差分缩放/稀疏支持的重命名；
                    4) F 有脱离本实验的定义域。>
【流程】 $$\text{SOURCE CARD}\to\text{S1–S4/STOP 审核}\to\text{第一笔最小计算}\to\text{结构判定}\to\begin{cases}\text{forced object}\Rightarrow\text{继续}\\\text{numerical pattern only}\Rightarrow\text{STOP}\\\text{CAS/B/C 型}\Rightarrow\text{STOP}\end{cases}$$ ✓
【状态】 `S4` ＝ **primary admission gate**；`STOP` **必须在计算前声明** ✓
```
