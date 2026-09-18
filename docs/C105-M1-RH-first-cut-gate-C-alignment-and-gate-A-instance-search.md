已查地图（所查：`RESEARCH-CONSTITUTION.md`（**`N46` 登记原文 ＋ 附录 `N25–N46` 表 ＋ §4.3 禁止重复表**）、`V107-N31-formalization.md`（引用格式范式）、`FREEZE-AUDIT-FZ1-FZ4.md`（`FZ-2`／`FZ-3`／六筛子）、`CLOSED-ROUTES-MAP.md`、`C-104`（五 primitive 审计）、`MATH-STATEMENT-A-*`（`O_1`／支撑）、`W6-MAJORANT-1g`、`V226`／`V227`（完成化层））。**结论**：正式开 **`M1-RH: Hereditary Arithmetic Null Separation`** 第一刀 ⟹ **Gate C ✓**：`N46` 原文＝「**`null 能复现 ⟹ 无信号资格`**」（来源 `T4`，证据等级＝**方法学门槛**）⟹ **`N46` 是"零模型可复现性"筛子，与 `M1` 的量词结构不是同一件事 ⟹ `M1` 不是 `N46` 的重命名** ✓✓（但**实现须过 `N46`**）；**Gate E ✓**（`∀S` 形式上不是 `lim F_n` 有限局部聚合）；**Gate A ✗**：搜索 6 个具体 restriction family，**无一**同时满足 `A+B+C`；**最接近者＝部分欧拉积族**（有限 `S` **全无零点**，统一成立 ✓✓，但**对 ζ 的 `β` 无响应** ⟹ **B 失败**）⟹ 按预注册：**`M1` DEAD（bounded-family 意义）** ✓✓；⚠️ **不升级为"原则上不可能"** ✓

# C-105 · **`M1-RH` 第一刀：Gate C（对齐 `N46`）＋ Gate A（具体实例搜索）**

> **时间**：2026-09-18 15:44 唐先生：正式开 **`M1-RH: Hereditary Arithmetic Null Separation`**；按 5 gate（A–E）走；**第一阶段禁引入 Gaussian／随机矩阵／Gibbs／determinant**（除非由 arithmetic object 自然产生）；**第一问只有一个**：RH 中什么对象有**非平凡、可枚举**的 restriction family，且其上存在**统一的不退化界**？找不到 ⟹ **`M1` DEAD** ✓

---

## §0 结论（先行）

$$\textbf{Gate C}\ ✓：\text{`N46` 登记原文（逐字）}＝\boxed{\text{RH 中}\ \text{"null 能复现} \Longrightarrow \text{无信号资格"}}（\text{"非零／三体／非交换"永久失去资格}）✓$$
$$\qquad \text{来源}\ T4;\quad \textbf{证据等级＝方法学门槛};\quad \text{且 §4.3 禁止重复表：}\text{"新的 prime invariant"} \ ❌\ N3/N46✓$$
$$\qquad \Longrightarrow\ \text{`N46`＝}\textbf{"零模型可复现性"筛子};\quad \text{`M1`＝}\textbf{量词结构}（\forall S\ \text{一致}） \Longrightarrow \boxed{\text{不是同一件事，非重命名}}✓✓$$
$$\qquad \qquad ⚠️\ \text{但}\ \textbf{实现必须过}\ \text{`N46`}✓$$
$$\textbf{Gate E}\ ✓：\text{`M1` 的形态}\ \forall S\in\mathfrak R_T:\ \mathcal P(\mathcal O_{T,S})\ge B(T)\ \textbf{形式上}\ne\lim_n F_n✓✓\（\text{唯一已获绿灯}）$$
$$\textbf{Gate A}\ ✗：\text{审计 6 个具体 family}，\textbf{无一过}\ A+B+C✓$$
$$\qquad ⭐\ \textbf{最接近者＝部分欧拉积族}：\text{有限}\ S\ \textbf{全无零点}（\text{统一成立} ✓✓）；\ \text{但}\ \text{它是}\ \textbf{关于}\ P_S\ \text{而非 ζ} \Longrightarrow \textbf{对 ζ 的}\ \beta\ \textbf{无响应} \Longrightarrow \textbf{B 失败}✓$$
$$\Longrightarrow\ \text{按预注册}：\boxed{\text{`M1` DEAD（bounded-family 意义）}};\quad ⚠️\ \textbf{不升级} \text{为"原则上不可能"}✓✓$$
$$\qquad \text{`M2`}\ \textbf{不开}（\text{`M1` 未需要它}）✓$$

---

## §1 Gate C：`N46` 逐字登记与判定（对齐完成）

$$\text{【档 A】}\text{`RESEARCH-CONSTITUTION.md`}\ \text{§2.3 统计与数值类上方，第 55 行}：\text{`N46 Arithmetic Null Separation`} \Longrightarrow \text{若 null 模型可复现} \Longrightarrow \textbf{无信号资格}✓$$
$$\text{【档 B】附录}\ \text{`N25–N46`}\ \text{表：}\ \text{`| N46 | Arithmetic Null Separation | null 能复现 ⟹ 无信号资格（"非零/三体/非交换"永久失去资格）| T4 | 方法学门槛 |`}✓✓$$
$$\text{【档 C】§4.3 禁止重复表：}\ \text{"新的 prime invariant"} ❌\ \text{N3/N46}✓$$
$$\Longrightarrow\ \textbf{判定}：\text{`N46` 的}\ \textbf{逻辑内容＝"你的信号能否被零模型复现"}（\text{典型性／可复现性筛}）;\quad \text{`M1` 的}\ \textbf{逻辑内容＝"界对所有 restriction 一致"}（\text{量词顺序筛}）✓✓$$
$$\qquad \boxed{\text{两者正交}：\text{`N46`}\ \text{筛}\ \textbf{信号资格};\ \text{`M1`}\ \text{要求}\ \textbf{一致性}} \Longrightarrow \textbf{`M1` 不是 `N46` 的重命名}✓✓$$
$$\qquad ⚠️\ \textbf{但}：\text{`M1` 的任一候选}\ \textbf{必须过}\ \text{`N46`}\（\text{若其统一界能被零模型复现，则无信号资格}）✓$$

## §2 Gate E：`V259` 形式检查（`M1` 唯一绿灯）

$$\text{`V259` 判死判据}：P=\lim_{n\to\infty}F_n,\quad F_n＝\textbf{有限局部聚合} \Longrightarrow \textbf{DEAD}✓$$
$$\qquad \text{`M1` 的自然形态}：\forall S\in\mathfrak R_T,\ P(T,S)\ge B(T) \Longrightarrow \text{其}\ \textbf{主量词是}\ \forall S \Longrightarrow \textbf{形式上不触发}\ \text{`V259`}✓✓$$
$$\qquad \text{且}：\text{`M1` 要求的}\ \textbf{不是}\ \sum_{j\le n}f_j\ \text{型累加}，\ \text{而是}\ \textbf{同一界在整族上的稳定性} \Longrightarrow \textbf{形式区别真实存在}✓✓$$
$$\qquad ⚠️\ \text{但（唐先生原话）}：\text{escape from `V259` in form}\ \ne\ \text{escape from `FZ-3` in substance}✓$$
$$\qquad \qquad \text{`FZ-3`：canonical} \Longrightarrow \beta\ \text{盲};\ \text{携带零点位置} \Longrightarrow \textbf{循环}✓$$

## §3 Gate A：六个 restriction family 的逐项审计（**本档核心工作**）

$$\text{要求（唐先生）}：(\mathcal X_T,\mathfrak R_T,\mathcal P_T)\ \text{三者}\ \textbf{明确};\ \mathfrak R_T\ \textbf{可枚举非平凡};\ \mathcal P_T\ \text{有}\ \textbf{统一不退化界}✓$$

| 候选 | `X_T`（算术对象）| `R_T`（restriction 族）| `P_T`（统一界）| A 算术 | B **`β` 响应** | C 一致 | 判定 |
|:--|:--|:--|:--|:--:|:--:|:--:|:--|
| **`A1`** Euler 因子删除族 | ζ（或 `L`）删去 `p∈P` 的因子 | 有限 `P` | 统一不退化界？| ✓ | ✗ **FE 被破坏，无 `β` 响应** | ✗ | **DEAD（B/C）** |
| **`A2`** 垂直窗口族 | 零点计数测度 | `[T,T']` | 界在 `T'` 上一致 | ✓ | ✓ **但＝`S(T)` ⟺ RH** | ✓ | **DEAD（＝已知墙，非新形）** |
| **`A3`** Dirichlet 多项式支撑族 | `D(s)=Σ_{n≤X}a_n n^{-s}` | 支撑子集 | 离对角界一致 | ✓ | ✓ | ? | **＝`W6` 重编码** |
| **`A4`** 特征／`L` 函数族 | `{L(s,χ)}` | `χ mod q` | 大筛法型一致界 | ✓ | ✗ 工具类，界已知 | ✓ | **DEAD（工具类已用尽）** |
| **`A5`** 零点子多重集 | 零点多重集 | 子多重集 | 统一界 | ✗ | — | — | **DEAD（`FZ-3` ② 循环）** |
| **`A6`** ⭐ **部分欧拉积族** | `P_S(s)=∏_{p∈S}(1-p^{-s})^{-1}` | 有限素数集 `S` | `P_S` **无零点** | ✓ | ✗ **关于 `P_S` 而非 ζ** | ✓✓ | **DEAD（B 失败）** |

### `A6` 详析（**最接近的实例**，值得记录）

$$\text{定理级事实}：\text{有限}\ S \Longrightarrow P_S(s)=\prod_{p\in S}(1-p^{-s})^{-1}\ \text{是有限乘积},\ \text{其}\ \textbf{极点}\ \text{满足}\ 1-p^{-s}=0 \Longrightarrow p^{-s}=1 \Longrightarrow s=\frac{2\pi ik}{\log p}\ (\text{Re}\,s=0)✓$$
$$\qquad \text{分子无因子} \Longrightarrow P_S\ \textbf{全无零点};\quad \text{极点全在}\ \text{Re}\,s=0✓✓\（\text{"}\forall S\ \text{一致"}，\ \text{规则惊人地干净}）$$
$$\qquad \text{而}\ S\to\{\text{所有素数}\}：\zeta(s)\ \text{在临界带内}\ \textbf{有零点} \Longrightarrow \textbf{该统一性质在极限处断裂}✓✓$$
$$\Longrightarrow\ \text{这是}\ \textbf{一个具体的、可枚举的、arithmetic 的}\ \text{"hereditary 一致性 ＋ 极限断裂"} \text{实例}✓✓$$
$$\qquad ⚠️\ \textbf{但致命处（B）}：\text{该统一性}\ \textbf{关于}\ P_S;\ \text{它对 ζ 的}\ \beta \textbf{完全没有响应} \Longrightarrow \text{它给出}\ \textbf{零}\ \text{关于零点位置的约束}✓$$
$$\qquad \qquad \text{且其"极限断裂"}\ \text{与}\ \text{`FZ-3` ① 同址}：\text{canonical 对象}\ \Longrightarrow \text{关于 ζ 的}\ \beta\ \text{盲}✓✓$$
$$\qquad \qquad ⚠️\ \text{更根本}：\text{在}\ \textbf{每个有限层}\ \text{该性质}\ \textbf{平凡成立} \Longrightarrow \text{没有任何}\ \textbf{可运输} \text{的量到极限} \Longrightarrow \text{这正是}\ \text{`V259`}\ \text{形状的}\ \textbf{内容面}✓✓$$

## §4 Gate B／D 判定

$$\textbf{Gate B（三重 realization）}：\text{六个候选}\ \textbf{无一}\ \text{同时具备}\ A+B+C;\ \text{`A6` 有}\ A+C\ \text{但}\ \textbf{B 失败}✓$$
$$\qquad ⚠️\ \text{而}\ B\ \text{正是生死点（唐先生原话）}：\beta\ne\tfrac12 \Longrightarrow \textbf{可计算的 defect}✓$$
$$\textbf{Gate D（`FZ-3`）}：\text{`A6`}\ \text{落}\ \textbf{horn ①}（canonical \Longrightarrow \beta\ \text{盲}）;\ \text{`A5`}\ \text{落}\ \textbf{horn ②}（循环）✓$$
$$\qquad \Longrightarrow\ \text{六个候选}\ \textbf{全部落}\ \text{`FZ-3`}\ \text{两端之一}✓✓$$

## §5 判词与预注册

$$\boxed{\text{`M1-RH` 第一刀结论}：\text{Gate C ✓（非重命名）};\ \text{Gate E ✓（形式绿灯）};\ \text{Gate A ✗};\ \text{Gate B ✗};\ \text{Gate D ✗}}✓$$
$$\qquad \Longrightarrow\ \text{按唐先生预注册}：\boxed{\text{`M1` DEAD：只有形式新颖，没有 arithmetic realization}}✓✓$$
$$\qquad ⚠️\ \textbf{严格边界}：\text{这是}\ \textbf{bounded-family（6 族）} \text{意义下的 DEAD};\ \textbf{不升级} \text{为"原则上不可能"}✓✓$$
$$\qquad ⚠️\ \text{`M2`}\ \textbf{保持不开}（\text{`M1` 未需要它}）✓$$
$$\textbf{保留的唯一资产（可复用）}：\text{`A6`}\ \text{给出一个}\ \textbf{具体} \text{的"hereditary 一致性 ＋ 极限断裂"实例};$$
$$\qquad \text{其价值＝}\textbf{说明为何"有限层平凡 ⟹ 极限困难"}\ \text{在算术中是}\ \textbf{结构性的}，\ \text{而非技术不足}✓✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 15:4x）`[纪律]`（先跑后写）

```
技术词 Hereditary Arithmetic Null Separation  命中文件数=1  :: ./C105-M1-RH-first-cut-gate-C-alignment-and-gate-A-instance-search.md
技术词 M1-RH                              命中文件数=1  :: ./C105-M1-RH-first-cut-gate-C-alignment-and-gate-A-instance-search.md
技术词 极限断裂                             命中文件数=1  :: ./C105-M1-RH-first-cut-gate-C-alignment-and-gate-A-instance-search.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓

## §7 边界

- `[档案]` §1 的 `N46` 三处登记**逐字引用** ✓；§2 的 `V259`、§4 的 `FZ-3`／六筛子均为**档内引用** ✓
- `[本档]` §3 的六族审计表、`A6` 详析、§5 判词为**本档工作** ✓
- ⚠️ `A6` 的"有限层全无零点"＝**标准事实**（有限乘积）；其"极限断裂"＝ζ 零点存在 ⟹ **均非本档新数学** ✓
- **不声称**：`M1` 原则上不可能 ✗；`support>1` 相关结论不受影响 ✓；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓；**第一阶段未引入 Gaussian／随机矩阵／Gibbs／determinant** ✓✓

```
⚠️ 唐先生 15:44：正式开 M1-RH（Hereditary Arithmetic Null Separation），五 gate，第一阶段禁 Gaussian/随机矩阵/Gibbs/determinant；
   第一问只有一个: RH 中什么对象有非平凡可枚举 restriction family 且其上存在统一不退化界？找不到 ⟹ M1 DEAD
✅ Gate C（对齐 N46）: N46 登记原文三处 —— RESEARCH-CONSTITUTION.md §2.3 第55行 + 附录 N25–N46 表
   「| N46 | Arithmetic Null Separation | null 能复现 ⟹ 无信号资格（"非零/三体/非交换"永久失去资格）| T4 | 方法学门槛 |」
   + §4.3 禁止重复表「"新的 prime invariant" ❌ N3/N46」
   ⟹ N46＝"零模型可复现性"筛子；M1＝量词结构(∀S 一致) ⟹ **两者正交，M1 不是 N46 重命名** ✓✓；但 M1 实现必须过 N46 ✓
✅ Gate E（V259 形式）: M1 形态 ∀S∈R_T: P(O_{T,S}) ≥ B(T)，主量词是 ∀S ⟹ 形式上不是 lim F_n 有限局部聚合 ⟹ **不触发 V259** ✓✓（唯一绿灯）
✅ Gate A（六族审计）: A1 Euler 因子删除（B/C 失败）; A2 垂直窗口族（＝S(T) ⟺ RH，已知墙）; A3 Dirichlet 支撑族（＝W6 重编码）;
   A4 特征/L 函数族（大筛法工具类已用尽）; A5 零点子多重集（FZ-3 ② 循环）;
   ⭐A6 部分欧拉积族 P_S=∏_{p∈S}(1−p^{−s})^{−1}: 有限 S ⟹ **无零点**（极点全在 Re s=0）⟹ A ✓ C ✓✓（统一性极干净）;
     但关于 P_S 而非 ζ ⟹ **对 ζ 的 β 无响应** ⟹ **B 失败**；且"极限断裂"（S→全素数 ⟹ ζ 有临界带零点）与 FZ-3 ① 同址
✅ Gate B/D: 六族无一过 A+B+C；A6 落 FZ-3 horn ①（canonical ⟹ β 盲）；A5 落 horn ②（循环）
⭐ 判词: Gate C ✓ / Gate E ✓ / Gate A ✗ / Gate B ✗ / Gate D ✗ ⟹ 按预注册 **M1 DEAD（bounded-family 意义：6 族）**；
   ⚠️ 不升级为"原则上不可能"；M2 保持不开；第一阶段未引入 Gaussian/随机矩阵/Gibbs/determinant ✓
✅ 保留资产: A6 给出一个**具体**的"hereditary 一致性 + 极限断裂"实例 ⟹ 说明"有限层平凡 ⟹ 极限困难"在算术中是**结构性**的
✅ 净产出: ①N46 对齐（非重命名，但为必过筛子）✓ ②Gate E 形式绿灯确认 ✓ ③六族审计表 ✓ ④A6 最近实例＋B 失败根因 ✓ ⑤M1 DEAD 判定（bounded-family）✓
```

---

## §8 ⭐ **资产登记 ＋ 保留结论（唐先生 2026-09-18 15:48 指定）**

### §8.1 **独立资产：`A6`（有限层—极限断裂样本）**

$$\boxed{\text{finite arithmetic objects can be uniformly trivial while their infinite limit acquires the zero structure}}✓✓$$
$$\qquad \text{具体}：\forall\ \text{finite}\ S:\ P_S(s)=\prod_{p\in S}(1-p^{-s})^{-1}\ \textbf{无零点}（\text{极点全在}\ \text{Re}\,s=0）;\quad S\uparrow\mathbb P \Longrightarrow \zeta\ \textbf{在临界带获得零点}✓$$
$$\qquad \text{价值}：\text{它给出}\ \textbf{"有限层统一平凡 → 极限获得零点结构"}\ \text{的一个}\ \textbf{具体、可枚举、arithmetic}\ \text{样本}✓✓$$
$$\qquad \qquad \Longrightarrow\ \text{即}\ \text{`V259`}\ \text{的}\ \textbf{反例型资产}：\textbf{"每个有限层都没问题 ⟹ 极限也没问题"在算术中是危险推理}✓✓$$
$$\qquad ⚠️\ \text{边界}：\textbf{不是} RH 新桥（B 失败）;\ \text{仅作}\ \textbf{机制样本} \text{保存}✓$$

### §8.2 **三个必须保留的判词（唐先生指定）**

$$\textbf{(i)}\ \text{`M1` 的形式独立性（真区别）}：\underbrace{\forall S\in\mathfrak R_T}_{\text{M1 新形式}}\ \not\Rightarrow\ \underbrace{\lim_n F_n}_{\text{V259}} \Longrightarrow \boxed{\text{M1 在形式上逃过 V259}}✓✓$$
$$\qquad \text{但随后}：\text{六个具体}\ \mathfrak R_T \Longrightarrow A+B+C=0 \Longrightarrow \boxed{\text{bounded-family 意义下 M1 DEAD}} \ne \text{M1 impossible in principle}✓✓$$
$$\qquad \qquad ⚠️\ \textbf{该区分必须保留}（\text{与}\ \text{`R1`／`R2`}\ \text{同格式}）✓$$
$$\textbf{(ii)}\ \text{`N46` 与 `M1` 成功去重}：\boxed{\text{`N46`＝signal-validity sieve};\quad \text{`M1`＝restriction-quantifier mechanism}} \Longrightarrow \textbf{未发生"换名字重开旧路线"}✓✓$$
$$\textbf{(iii)}\ ⭐\ \text{Gate E 的绿灯是}\textbf{真绿灯}（\text{最易被忽略}）：\text{`M1` DEAD 的}\ \textbf{原因不是} \text{`M1`}\subset\text{`V259`}，\ 而是：✓$$
$$\qquad \boxed{\text{M1}\not\subset\text{`V259`}\quad\text{but}\quad \text{known arithmetic realizations fail B/D}} \Longrightarrow \textbf{比普通 NO-GO 更有信息量}✓✓$$

### §8.3 **重开门槛（六条，缺第一项不再开工）**

$$\text{若将来重开}\ \text{`M1`}，门槛直接写成：\exists\,(\mathcal X_T,\mathfrak R_T,\mathcal P_T)\ \text{满足}✓$$
$$\qquad \text{(1) Arithmetic realization};\ \text{(2) }\beta\text{-testable response};\ \text{(3) uniform over }\mathfrak R_T;\ \text{(4) passes }\text{`N46`};$$
$$\qquad \text{(5) avoids both }\text{`FZ-3`}\ \text{horns};\ \text{(6) not }\text{`V259`}\ \text{finite-local aggregation}✓$$
$$\qquad \Longrightarrow\ \boxed{\textbf{缺第一项具体对象，就不再开工}}✓✓$$
$$\qquad ⚠️\ \text{且}\ \text{唐先生 15:48}：\textbf{不继续扩大 `M1` 六族}（\text{继续枚举 Euler subsets／Dirichlet supports／characters／zero subsets 的变体}\ \Longrightarrow \textbf{易回到旧档案}）✓$$
