已查地图：命中（`E-32`／`E-33`／`AMEND-6/7/8` 本线自档）⟹ **引用，不开新案** ✓

# **`B-EXACT`：`\mathcal A_{\rm old}^{(J\le4,W,W')}=\{0\}` 的形式化证明**（**零计算** ✓；`RUN` 仍待核 ✓）

**唐先生裁决（2026-09-23 14:12 ✓✓）**：$$\boxed{\text{修补 A 可以核 (PASS)；修补 B 的 }\mathcal A_{\rm old}=\{0\}\text{ 目前还不能直接核}}$$ ✓；
　**理由（照录）**："旧机制**不蕴含**" $\not\Rightarrow$ "旧关系空间**已被严格证明为** `\{0\}`" ✓；尤其 **Hecke 部分不能只用"乘法性"三个字结束** ✗；
　**须写成**：在**预先限定的坐标**、`J\le4`、**两个窗口**、**四个序列**下，**由预注册 Hecke/symmetry 规则能够生成的线性关系究竟是什么**，然后证明其生成空间在当前关系类型下为零 ✓✓
　**最小下一刀（照录）**：只补一份 `B-EXACT`，回答四问：**(1)** Hecke 在 `p_h`／`q_h` 坐标下能生成哪些**线性**关系｜**(2)** 水平 1、自对偶、归一化是否产生**跨 `f,g`** 关系｜**(3)** density／`\log p`／`\sqrt p` 为何在**精确有限关系空间**中贡献 `0`｜**(4)** ⛔ **不允许事后增加任何旧机制** ✓
　**命名（照录 ✓✓）**：第一层结果命名为 $$\boxed{\text{FORCED-OBJECT CANDIDATE}}$$ ⛔ 而非直接"`FORCED OBJECT`"（实验只证四固定序列存在共同 `c`，**尚未证明** `c` 有独立于有限数据的无限定义 ✓）；两阶段：$$\boxed{\text{exact common annihilator}\to\text{FORCED-OBJECT CANDIDATE}\to\text{independent object definition}}$$ ✓

D0: 本档对象 = **`B-EXACT`：`\mathcal A_{\rm old}` 生成空间的形式化证明（三引理＋推论）**（引本线自档；**未开 bridge 案** ✓）
D1: 0 （`[REVIEW]` 轮次：形式化证明，不主张新自由度 ✓）
FREEZE-ACK: D1=0 ✓
[REVIEW]

---

## §1 **定义（把"直觉"变成可审计定义 ✓）**

```
【关系类型（事前限定 ✓）】 坐标＝窗口内**素数下标**（`p_h`／`q_h`）；$$\mathcal C:=\Bigl\{c\in\mathbb Q^{J+1}:\ J\le4,\ \sum_{j=0}^{J}c_j\,x_{h+j}=0\ \ \forall h=0..600\Bigr\}$$ ✓
【`\mathcal A_{\rm old}` 的正式定义（照录唐先生结构 ✓✓）】
　$$\mathcal A_{\rm old}:=\operatorname{Span}_{\mathbb Q}\{\ \text{预注册旧机制\textbf{实际生成}的关系}\ \};\qquad c\in\mathcal A_{\rm old}\Rightarrow\text{OLD/absorbed};\quad c\notin\mathcal A_{\rm old}\Rightarrow\text{candidate FORCED OBJECT}$$ ✓
　⭐ 其中"**生成**"＝**由该机制的定义恒等式可推导（derivable）**，⛔ **不是**"对所有对象为真" ⟹ 这排除了"核相交即解释"的跳步 ✓✓
【预注册旧机制清单（**一次写死，⛔ 事后不得增补** ✓✓）】
　$$\text{(M1) Hecke 乘性}:\ a_{mn}=a_ma_n\ ((m,n)=1);\qquad \text{(M2) Hecke 递推}:\ a_{p^{r+1}}=a_pa_{p^r}-p^{k-1}a_{p^{r-1}}$$ ✓
　$$\text{(M3) 水平 1 自对偶/Fricke 平凡};\qquad \text{(M4) 归一化 } a_1=1;\qquad \text{(M5) density／}\log p／\sqrt p\ \text{渐近结构}$$ ✓
```

## §2 **问 1：Hecke 能生成哪些线性关系？⟹ `\mathcal A_{\rm Hecke}=\{0\}`（引理 1，严格 ✓✓）**

```
【模型】 取 Hecke 系数系统的**自由模型**：以 `\{a_p\}_{p\ \text{prime}}` 为**独立变量**，由 (M2) 归纳**定义** `a_{p^r}=:P_r(a_p)`，由 (M1) **定义** `a_n=:\prod_p P_{\nu_p(n)}(a_p)` ⟹ 全部落在 `\mathbb Q[a_p:p\ \text{prime}]` 中 ✓
【引理 1a（次数）】 `\deg P_r=r` ⟹（归纳：`P_{r+1}=a_pP_r-p^{k-1}P_{r-1}` ⟹ `\deg=r+1`；`\deg P_1=1` ✓）
【引理 1b（可复原性）】 `a_n` 在**每个变量 `a_p` 上的次数恰为 `\nu_p(n)`** ⟹ 由多项式**逐变量次数**可**唯一复原** `n` ✓（⟹ `n\ne m\Rightarrow a_n\ne a_m`，且 `\{a_n\}` 为 **`\mathbb Q`-线性无关** ✓✓）
【引理 1c（结论）】 故任何 $$\sum_{j=0}^{J}c_j\,a_{m_j}=0\quad(m_j\ \text{互异})$$ 作为 (M1)(M2) 模型中的**恒等式均为假** ⟹ **不可推导** ⟹ $$\boxed{\mathcal A_{\rm Hecke}=\{0\}}$$ ✓✓
　⭐ 注：此结论**强于**所需（连"不同下标同度数"的可能性也被排除 ✓）
【⛔ 与"机制不解释"的区别（照录）】 1c 证的是"**(M1)(M2) 生成不出这种关系**"，**不是**"Hecke 机制与现象无关"；两者不同，本档只主张前者 ✓✓
```

## §3 **问 2：水平 1／自对偶／归一化是否产生跨 `f,g` 关系？⟹ `\mathcal A_{\rm sym}=\{0\}`（引理 2 ✓）**

```
【水平 1 ⟹ Fricke 平凡 ⟹ 对偶序列＝原序列】 ⟹ (M3) **不产生**连接两个**不同**形式的线性关系 ✓
【归一化 `a_1=1`】 只**固定整体尺度**（消除"任意倍数"自由度）⟹ 不产生关系 ✓
【跨 `f,g` 可能性（逐一排查 ✓）】 预注册清单中**无任何**连接两形式的恒等式；
　⚠️ 已知的"**同余**"（如 `\tau(p)\equiv p^{11}+1\ (691)`）是**模 `p` 陈述**，**不是** `\mathbb Q` 上的**精确线性恒等式** ⟹ **不属本关系类型** ✓；且**不在预注册清单**内 ⟹ 事后亦**不得增补** ✓✓
【⟹】 $$\boxed{\mathcal A_{\rm sym}=0\ (\text{无跨 }f,g\ \text{关系})}$$ ✓
```

## §4 **问 3：density／`\log p`／`\sqrt p` 为何贡献 `0`？（引理 3 ✓）**

```
【结构事实】 在 `601` 个连续下标上满足 `J\le4` 常数系数线性递推 ⟹ 该序列片段属**线性递推序列类** `\{\sum_i\lambda_i^hP_i(h)\}` ⟹ **增长型必为** `h^{m}\lambda^{h}`（`|\lambda|\le1` 时为多项式 `h^m`，否则指数型）✓
【逐条排除】 `x_h=p_h\sim h\log h`、`x_h=\log p_h\sim\log h`、`x_h=\sqrt{p_h}\sim\sqrt h\log h` —— **均含 `\log` 因子**，**不属** `h^{m}\lambda^{h}` 型 ✓ ⟹ 三者均**不可能**满足任何 `J\le4` 常数系数递推 ⟹
　$$\boxed{\mathcal A_{\rm dens}=\mathcal A_{\rm log}=\mathcal A_{\rm sqrt}=\{0\}}$$ ✓（且**单块核** `\ker H_x=\{0\}` 对这三者亦成立 ✓）
【⭐ 一个（非分类性的）观测】 `\ker H_{\mathbf 1}=\{c:\sum_jc_j=0\}\ne\{0\}` ✓ —— 但"常序列"**不是**预注册的**生成机制**（它不解释任何形式的结构）⟹ 依 `E-33` 裁定，此项**只作诊断信息**，⛔ **不作 OLD/FORCED 分类依据** ✓✓
```

## §5 **问 4 ＋ 推论（`\mathcal A_{\rm old}=\{0\}` ✓✓）**

```
【问 4】 ⛔ 预注册清单 **(M1)–(M5) 一次写死**；`RUN` 之后**不得增补**任何旧机制（含"事后想到的等价表述"）✓
【推论】 由引理 1–3：$$\boxed{\mathcal A_{\rm old}^{(J\le4,W,W')}=\operatorname{Span}(\mathcal A_{\rm Hecke}\cup\mathcal A_{\rm sym}\cup\mathcal A_{\rm dens/log/sqrt})=\{0\}}$$ ✓✓
　⟹ 在该有限实验域与关系类型下，**吸收空间为空** ⟹ 任一命中 `c` **自动**"非旧机制解释" ⟹ `c` 进入 $$\boxed{\text{FORCED-OBJECT CANDIDATE}}$$（⛔ **非** `FORCED OBJECT` ✓）
【⭐ 反事后保护的真实来源（照录 `E-33` 结论，此处已由证明落实 ✓）】 不在"吸收判别"（其为空），而在 **(i)** 四块同系数的高超定**精确**判定；**(ii)** 两个**互不相交窗口**（修补 A ✓）；**(iii)** **全部事前固定**（形式/对/`J`/`h` 范围/窗口/机制清单）✓✓
【⚠️ 诚实边界（照录精神 ✓）】 引理 1–3 只证"**(M1)–(M5) 生成空间为零**"，⛔ **不证**"不存在任何旧机制解释实验现象"（超出预注册清单者**不在本判定之内**，且**不得事后加入** ✓）；`\ker` 相交**仅作诊断** ✓
```

## §6 **状态（照录唐先生表格 ✓✓）**

| 项目 | 当前判定 |
|:--|:--|
| `10` 个 `(f,g)` 全检 | ✓ |
| `J\le4` | ✓ |
| 四块 exact matrix | ✓ |
| 两个互不相交窗口 | **✓ PASS**（A 已核 ✓） |
| 同一 `c` 四块共用 | ✓ |
| 第二尺度独立性 | **✓ PASS** |
| 旧核并集作为吸收判据 | ✓ 已正确降级为**诊断** |
| `\mathcal A_{\rm old}` 的正式定义 | **✓ 已写死**（本档 §1） |
| `\mathcal A_{\rm old}=\{0\}` 的证明 | **✓ 本档 §2–§5 给出**（三引理＋推论） |
| FORCED 的命名 | **改为 `FORCED-OBJECT CANDIDATE`** ✓ |
| **`RUN`** | **LOCKED**（待您核可 ✓） |

```
【下一步（供裁 ✓，⛔ 仍不计算）】 若您核可本档三引理与推论 ⟹ $$S4\text{-EXACT}=\text{PASS}\Longrightarrow\text{方可授权 }RUN$$ ✓
【边界】 ✗ 未计算／⛔ 未改 `S4` 判定标准／⛔ 未事后增补机制／⛔ 未把"机制不解释"偷换为"关系空间为零"／⛔ 未把候选写成 `FORCED OBJECT` ✓
```


---

## §7 【**M5 引理 3 严格版**（唐先生 14:14 文字修正，照录 ✓✓）】

```
【结论保留，证明升级 ✓】 "含 `\log` 因子"**本身不是**排除常系数递推的充分条件（有些递推序列可含多项式/振荡因子）⟹ 改为标准渐近结构论证：
　若非零序列满足**固定阶常系数线性递推**，则其一般形式为 $$\boxed{x_h=\sum_iP_i(h)\lambda_i^h}$$（`P_i` 多项式）✓
　而 M5 中 $$\boxed{p_h\sim h\log h}\Longrightarrow\boxed{\log p_h\sim\log h},\qquad \boxed{\sqrt{p_h}\sim h^{1/2}(\log h)^{1/2}}$$ ✓
　这些量具**非整数幂的对数渐近因子**，**不可能等于有限个 `P_i(h)\lambda_i^h` 的非零组合** ✓ ⟹
　$$\boxed{\mathcal A_{\rm dens/log/sqrt}=\{0\}}\quad\text{（"含 log 因子"升级为"}\textbf{不属于有限阶常系数线性递推序列的渐近类}\text{"）}$$ ✓✓
【⚠️ 补充澄清（照录 ✓）】 "**density**"本身**不是单独的精确序列机制**；M5 的正式定义＝"**仅允许由 `p_h,\log p_h,\sqrt{p_h}` 的这些预注册渐近恒等式生成关系**" ⟹ 零空间结论成立 ✓
【⭐ 逻辑边界（照录 ✓✓）】 $$\mathcal A_{\rm old}=\{0\}$$ **不是**"不存在任何旧机制能解释命中关系"，而是
　$$\boxed{\text{M1–M5 事前规定的生成规则}\Longrightarrow\text{生成空间}=0}$$；RUN 后若得 `c\ne0` ⟹ 正确结论仍只是 $$c\notin\mathcal A_{\rm old}\Longrightarrow\boxed{\text{FORCED-OBJECT CANDIDATE}}$$（⛔ 非"证明了数学上全新的机制"）✓✓
【正式状态（照录 ✓✓）】 $$\boxed{\textbf{S4-EXACT}=\textbf{PASS}}\quad(\text{附 M5 wording fix：已落实 ✓})$$
```
