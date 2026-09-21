已查地图（**先查后写**）：`C-375`（**`E_{\mathrm{even}}` 精确定义：r = 1..12** ✓✓）、`C-342`（**偶频子系统 k ∈ {2,4,…,24}，即 r ≤ 12** ✓✓）、`C-380-20A` (a)（`E_{\mathrm{even}}` 再述 ✓✓）、`C-380-21A`（**`E_0 = \bigcup_j\{x_j = 0\}` ＋ 坐标 A／B 冲突** ✓✓）、`C-350`（**`\mathcal Z` = 零矩流形（Bridge 用）** ✓✓）、`C-358／361／368`（**限 `\mathcal Z`** ⚠️✓）、`C-380-11`（**`E_0` 先于 `E_{\mathrm{coll}}`** ✓✓）、`C-380-12`（**截断形式 k = 1..6** ⚠️✓）、`C-3846`（**9 次单位根证书；本档修正其判词** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-47：原始 `E_0` 定义逐条回填 ＋ 9 次单位根证书的归属判定 ＋ 判词更正**（唐先生 2026-09-21 20:57 委托）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（九条 ✓✓）

$$\textbf{① 原始定义（回填完成）}✓✓：\ \boxed{E_{\mathrm{even}} = \Big\{x \in [0,1]^5 : \sum_{j=1}^{5} T_{2r}(2x_j - 1) \le \tfrac12,\ r = 1,\dots,12\Big\}}✓✓$$

$$\qquad \text{（`C-375` §0①、`C-342`、`C-380-20A` (a) ✓✓）};\qquad \boxed{E_0 = \bigcup_{j=1}^{5}\{x_j = 0\}}✓✓\ \text{（`C-380-21A` §0③ ✓✓）}$$

$$\qquad \Longrightarrow \ \text{WLOG}\ x_5 = 0\ \text{（`C-380-21A` A3 ✓✓）} \Longrightarrow \ \text{四点松弛约束} = \boxed{\Re \sum_{j=1}^{4} z_j^r \le -\tfrac12,\quad r = 1,\dots,12}✓✓$$

$$\qquad \Longrightarrow \ \textbf{12 条约束}✓✓\ ——\ \textbf{而非}\ C\text{-}380\text{-}12\ \text{所写 6 条}✗✓\ \Longrightarrow\ \textbf{`C-380-12` 的形式是截断式}✓✓$$

$$\textbf{② ⚠️⭐ 判词更正（本档核心）}✓✓：\ \text{9 次单位根证书在}\ \boxed{r = 9}\ \text{处}\ \textbf{失败}✗✗：\ \Re \sum_{j \in S} z_j^{9} = +4 \gg -\tfrac12✓✓$$

$$\qquad \Longrightarrow \ \boxed{\text{证书} \notin \text{原始}\ E_0}✓✓ \Longrightarrow\ C\text{-}3846\ §0①\ \text{的 "}\mathcal F_0 \ne \varnothing\text{"}\ \textbf{与}\ §0⑦\ \text{的}\ \textbf{NO-GO}\ \textbf{均撤回}✓✓$$

$$\qquad \Longrightarrow \ \text{按唐先生判定树}\ \textbf{第二支}✓✓：\ \boxed{\text{连续频率松弛非空，但原始}\ E_0\ \textbf{尚未被反驳}}✓✓ \Longrightarrow\ \boxed{E_0\ \text{路线}\ =\ \textbf{暂不判 NO-GO}}✓✓$$

$$\textbf{③ 证书仍有效的部分}✓✓：\text{它落在}\ \textbf{截断松弛}（k \le 6）\ \text{内}✓，\ \text{且为}\ \textbf{孤立点}✓、\ \textbf{非 two-level}✓✓$$

$$\qquad \Longrightarrow \ \boxed{\text{对截断对象，坍缩蕴含的反驳（}C\text{-}3846\ §0④\text{）}\ \textbf{成立}}✓✓;\qquad \boxed{\text{对原始对象，}\textbf{不成立}}✗✓$$

$$\textbf{④ 其余条件全部通过（数字驱动）}✓✓：x \in [0,1]^5 ✓✓；s_1 = \tfrac{11}{4}\ \textbf{恰好取等}✓✓；s_2 = s_1 - \tfrac{9}{16}\ \textbf{恰好取等}✓✓；s_2 \ge \tfrac{11}{12}✓✓；F_2 = F_4 = \tfrac12\ \textbf{恰好取等}✓✓$$

$$\qquad \Longrightarrow \ \boxed{\textbf{唯一违反项} = r = 9}✓✓\ \longrightarrow\ \textbf{结论干净：证书"差一条谐波"}✓✓$$

$$\textbf{⑤ } \mathcal Z\ \text{归属判定（唐先生问 5）}✓✓：\ \mathcal Z = \Big\{(x,\sigma) : \sum_j \sigma_j y_j^{2m+1} = 0,\ m = 0,1,2,3\Big\}✓\ (y_j = \sqrt{x_j}✓)\ \text{（`C-350` §1 ✓✓）}$$

$$\qquad \Longrightarrow \ \mathcal Z \subset E✓；\ \text{它是 Bridge 的}\ \textbf{结构分析子集}✓✓，\ \textbf{不是} E_0\ \text{的定义条件}✗✓\ \text{（`C-380-9` §5 纪律：引}\ C\text{-}358／361／368\ \textbf{必须标「限}\ \mathcal Z\text{」}✓✓）$$

$$\textbf{⑥ 碰撞层／端点类归属}✓✓：E_{\mathrm{coll}}\ (x_i = x_j)\ \text{是}\ \textbf{独立层}✓（`C-380-11`：E_0\ \text{先于}\ E_{\mathrm{coll}}✓）\ \textbf{不属} E_0✓；$$

$$\qquad S_m／A(m)／s_\pm\ \text{等}\ \textbf{端点类}✓\ \text{是}\ C\text{-}380\ \text{为}\ \textbf{two-level 子问题} \text{引入的}\ \textbf{辅助量}✓✓ \Longrightarrow\ \textbf{不属} E_0\ \text{定义}✗✓$$

$$\textbf{⑦ ⭐ 新机制：循环解被高谐波排除}✓✓：\text{穷举}\ n \le 30\ \text{的全部 4-子集}✓ \Longrightarrow\ \textbf{满足}\ r = 1..12\ \text{者}\ \textbf{0 个}✓✓$$

$$\qquad \textbf{机理（和恒等式）}✓✓：f(k) := \Re\sum_{j \in S} z_j^k✓ \Longrightarrow\ \sum_{k=0}^{n-1} f(k) = 0✓ \Longrightarrow\ \boxed{\sum_{k=1}^{n-1} f(k) = -4}✓✓\ (\text{当}\ 0 \notin S✓)$$

$$\qquad \text{配合偶性}\ f(k) = f(n-k)✓：\ n \le 25\ \text{时镜像}\ n-k\ \text{全落}\ r \le 12\ \text{覆盖内}✓$$

$$\qquad \qquad \Longrightarrow\ \text{若全部}\ f(k) \le -\tfrac12\ (r \le 12)\ \Longrightarrow\ \sum \le -6 \ne -4✓ \Longrightarrow\ \textbf{矛盾}✓✓ \Longrightarrow\ \boxed{n \le 25\ \text{无循环解}}✓✓$$

$$\qquad \Longrightarrow \ \textbf{截断的解恰是}\ \textbf{共振洞}✓✓（k \equiv 0 \bmod 9\ \text{的洞在}\ r \le 6\ \text{内不可见}✗，在}\ r \le 12\ \text{内被}\ r = 9\ \text{钉死}✓✓）$$

$$\textbf{⑧ 采样级状态（不作结论）}✓✓：2 \times 10^6\ \text{采样}✓ \Longrightarrow\ K = 6\ \text{得}\ +0.0335✓；\ K = 12\ \text{得}\ +0.6864✓；\ \textbf{均 0 可行}✓✓$$

$$\qquad \Longrightarrow \ \text{原始}\ E_0\ \text{的空性}\ \textbf{仍未证}✓✓;\ \text{截断松弛本身在采样级也无可行点}✓✓（\text{找它}\ \textbf{必须} \text{精确构造}✓）$$

$$\textbf{⑨ 账本（见 §3）}✓✓$$

## §1 定义回填表（逐条 ✓✓）

| 条件 ✓ | 出处 ✓ | 是否 E_0 定义 ✓ | 证书是否通过 ✓ |
|---|---|---|---|
| `\sum_j T_{2r}(2x_j-1) \le \tfrac12`，r = 1..12 ✓ | `C-375`／`C-342`／`C-380-20A` ✓ | **是** ✓✓ | r=1..8 与 10..12 **通过** ✓；**r = 9 违反** ✗✗ |
| `x \in [0,1]^5` ✓ | 同上 ✓ | **是** ✓✓ | **通过** ✓✓ |
| 排序 / WLOG ✓ | `C-380-21A` §0③（S_5 对称，**可证** ✓✓） | **归一化，非条件** ✓✓ | 通过（可重排）✓ |
| `E_0 = \bigcup_j\{x_j = 0\}` ✓ | `C-380-21A` §0③ ✓ | **是** ✓✓ | **通过**（x_5 = 0）✓✓ |
| `s_1 \le \tfrac{11}{4}`（`\iff F_2 \le \tfrac12`）✓ | `C-349` §1 ✓ | 导出条件 ✓ | **通过（取等）** ✓✓ |
| `s_2 \le s_1 - \tfrac{9}{16}`（`\iff F_4 \le \tfrac12`）✓ | `C-349` §1 ✓ | 导出条件 ✓ | **通过（取等）** ✓✓ |
| `s_2 \ge \tfrac{11}{12}` ✓ | `C-349` §1 ✓ | 导出条件 ✓ | **通过** ✓✓ |
| `\mathcal Z`（零矩流形）✓ | `C-350` ✓ | **否**（子集／Bridge 条件）✗✓ | 不适用 ✓ |
| `E_{\mathrm{coll}}`／`D_{\mathrm{coll}}` ✓ | `C-380-11` ✓ | **否**（独立层）✗✓ | 不适用 ✓ |
| `\mathcal S_m`／`A(m)`／`s_\pm` 端点类 ✓ | `C-380-22..43` ✓ | **否**（two-level 子问题辅助）✗✓ | 不适用 ✓ |
| 奇频量 `F_{2r+1}`（带 \sigma、带 \sqrt{x}）✓ | `C-346`／`C-349` ✓ | **否**（**目标量**，非约束）✗✓ | 不适用 ✓ |

## §2 数字核验记录（数字驱动 ✓✓）

```
A 段（12 条逐项，S={1,2,3,4}, n=9）：
   r=1..8  Re sum z^r = -0.5  OK
   r=9     Re sum z^9 = +4.0  *** VIOLATION ***
   r=10..12 Re sum z^r = -0.5  OK
B 段（诱导五点）：y=(0.93969262,0.76604444,0.5,0.17364818,-1)  x=(0.96984631,0.88302222,0.75,0.58682409,0)
   x in [0,1] True ; s1=2.75 (=11/4 取等) ; s2=2.1875 (=s1-9/16 取等) ; s2>=11/12 True ; F2=F4=0.5
C 段（n=3..30 全扫）：满足 r=1..12 的 4-子集  **0 个**
D 段（2e6 采样）：K=6 min max=+0.033469（0 可行）；K=12 min max=+0.686425（0 可行）
```
- 脚本 ✓：`scripts/c380_47_backfill_audit.py`✓；输出 ✓：`scripts/out_c380_47_backfill.txt`✓

## §3 更正记录（对 `C-3846` ✓✓）

| `C-3846` 条目 ✓ | 更正后状态 ✓ |
|---|---|
| §0① `\mathcal F_0 \ne \varnothing` ✓ | **仅对截断松弛（k ≤ 6）成立** ✓；对原始 `E_0`（r ≤ 12）**不成立** ✗（r = 9） |
| §0② 循环来源／16 组 ✓ | **不变**（截断完全解集）✓✓ |
| §0③ 孤立性 ✓ | **不变** ✓✓ |
| §0④ 坍缩蕴含被反驳 ✓ | **限截断对象** ✓；原始对象**未反驳** ✗✓ |
| §0⑤ `\Psi(\Delta_4)` 形式为假 ✓ | **不变**（与约束条数无关）✓✓ |
| §0⑥ 非配对模态精确仿射 ✓ | **不变** ✓✓ |
| §0⑦ E_0 路线 NO-GO ✓ | **撤回** ⟹ **暂不判 NO-GO** ✓✓ |

$$\Longrightarrow \ \text{这正是唐先生判定树的}\ \textbf{第二支}✓✓：\ \boxed{\text{连续频率松弛非空，原始}\ E_0\ \text{尚未被反驳}}✓✓$$

## §4 新线索（登记，**不**立即追 ✓）

$$\textbf{(i)}✓：\text{截断（12} \to \text{6）会}\ \textbf{引入伪解}✓✓ \Longrightarrow\ \text{任何基于截断形式的封闭证明，可能是在证一个}\ \textbf{更强的假命题}✗✓$$
$$\textbf{(ii)}✓：\text{原始}\ E_0\ \text{的封闭证明}\ \textbf{必须} \text{用到}\ r = 9,\dots,12\ \text{的高谐波}✓✓ \Longrightarrow\ \text{高谐波}\ =\ \textbf{必需资源}✓，\ \textbf{不是}可选✗✓$$
$$\textbf{(iii)}✓：\text{循环类已被排除（n} \le 25\text{）}✓ \Longrightarrow\ \text{原始}\ E_0\ \text{的真问题仍是}\ \textbf{一般（非循环）四点}✓✓$$

## §5 边界（不得声称 ✗✓）

- **不**声称 `E_0 \ne \varnothing`；**不**声称 `E_0 = \varnothing`（两个方向都未证）✓
- **不**声称坍缩蕴含对**原始**对象成立或失败（两方向均未证）✓
- **不**声称 `\Psi(\Delta_4)` 有救（`C-3846` §0⑤ 仍成立）✓
- **不**声称"n ≤ 25 无循环解"可替代一般空性证明（只排除**一类**）✓
- **不**声称 Level 3 已开（仍 FROZEN）✓

## §6 【技术词回查】输出（**先跑后写** ✓）

```
技术词 定义回填     命中文件数=0    ::
技术词 高谐波       命中文件数=0    ::
技术词 截断松弛     命中文件数=0    ::
技术词 伪解         命中文件数=2    :: ./MASTER-STATUS-AND-CLOSURES.md ./E167-squarefree-factorisation-directed-test.md
技术词 循环解排除  命中文件数=0    ::
技术词 判词更正     命中文件数=0    ::
```
- 边界 ✓：`伪解` 的 2 处命中为**旧线**（`E167`／总图）语境不同，**非**本档重复 ✓

## §7 下一步（须唐先生发令 ✓）

$$\textbf{建议①}✓：\text{把}\ \textbf{原始}\ E_0\ (r = 1..12)\ \text{重述为}\ \textbf{唯一} \text{目标}✓✓\ \text{（同时废止截断形式的独立地位}✗）$$
$$\textbf{建议②}✓：\text{若攻}✓，\ \text{从}\ r = 9..12\ \text{的}\ \textbf{高谐波} \text{入手}✓✓\ \text{（新资源}✓；\ \text{共振洞由此被钉死}✓）$$
$$\textbf{建议③}✓：\textbf{不}开 Level 3✗；\ \textbf{不}追}\ \Psi(\Delta_4)\ ✗✓$$
