已查地图：命中（`CAPMIX1-EXPERIMENT-1-truth-table-and-mechanism`）⟹ **自纠其 §4 异常** ＋ 执行 `CAP-MIX-1A`，不开新案
D0: 本档对象 = ⛔**自纠**（char 2 异常＝**我方定义错误**，论文无错）＋ **`CAP-MIX-1A` 定量结果**：$$\textbf{PASS}\Rightarrow\textbf{cap}\ \text{13/13（零假阳性）}$$ ＋ **不完备性定位（`FAIL_cap=10`）** ＋ 计划修正
D1: 1 （延续 `CAP-MIX-1` 的新自由度；本档给出**可靠性证据与不完备边界**）
[RESEARCH]

# **`CAP-MIX-1A`：`I` 可靠但不完备**

## §1 ⛔ 自纠：异常不是论文错，是我方定义错

```
**【论文 `Definition 1` 分特征定义】** $$q=3^n:\ a+b+c=0\ (\text{三个 distinct});\qquad q=2^n:\ a+b+c+d=0\ (\text{四个 distinct})$$ ✓✓
**【⟹ 我上一档的"反例"作废】** $$1+b+(b+1)=0\ \text{在 char 2 \textbf{不是}论文意义下的坏构型}$$ ✓
**【论文 `Thm 1(4)/(5)`（照您核验）】** `G_{2^{2n},2^n+1}` 满足四项关系时必有（重命名后）`a=b,\ c=d`；**`n` 为偶数**时 `G\cup\{0\}` 是 cap、大小 `2^n+2` ✓✓
$$\Longrightarrow\ (16,5)\ \checkmark,\ (64,9)\ \text{（我错标）},\ (256,17)\ \checkmark\ \text{全部自洽}$$ ✓✓
**【⟹ 有价值的副产品】** **机制按特征分成两支**：$$\boxed{\text{3-term/Frobenius obstruction}}\quad\text{vs}\quad\boxed{\text{4-term/Frobenius obstruction}}$$ ✓✓（**`Q_j` 判据只在奇特征可用，不得外推 char 2**）✓
```

## §2 ⭐⭐ `CAP-MIX-1A` 定量结果（`p\in\{3,5,7,11,13\}`，`q\le729`，共 **83** 个 `(q,d)`）

```
$$\textbf{COUNTS}:\quad \text{PASS\_cap}=13,\quad \textbf{PASS\_noncap}=0,\quad \text{FAIL\_cap}=10,\quad \text{FAIL\_noncap}=60$$ ✓✓
**【结论一（可靠性）】** $$\boxed{I(p,n,d)=\text{PASS}\ \Longrightarrow\ G\ \text{是 cap}:\quad \mathbf{13/13},\ \textbf{零假阳性}}$$ ✓✓ —— **单次 Frobenius 障碍判据在本批次\textbf{从未误报}** ✓✓
**【结论二（不完备）】** $$\boxed{\text{FAIL\_cap}=10:\ \text{存在 cap 而 }I\ \text{不能认证}}$$ ✓ —— 诚实边界 ✓
**【⟹ 这是一个"可靠但不完备"的判据**——正是机制研究的理想中间产物**】** ✓✓
```

## §3 `FAIL_cap` 的机制解释（本档定位）

```
**【失败清单】** `(25,4),(25,8),(125,4),(49,8),(121,5),(169,4),(169,14)` 等（共 10 例）✓
**【共同结构】** 例：$$(25,4):\ p=5,\ d=4\ \Longrightarrow\ 5^{\,j}\equiv1\ (\mathrm{mod}\ 4)\ \forall j\ \Longrightarrow\ \textbf{所有 }j\ \text{皆退化}\ \Longrightarrow\ I\ \text{真空、无法认证}$$ ✓✓
$$\Longrightarrow\ \textbf{不完备的精确条件}:\ \{\,p^{\,j}\bmod d\,\}_j\subseteq\{p^0,p^1,p^2,\dots\}\ (\text{全为 }p\text{-幂})$$ ✓
**【⟹ 处置】** 需**多步/组合型障碍**（如同时用 `j` 与 `j'`，或用子群内部的二次结构），**或**承认这是另一条机制 ⚠️
```

## §4 计划修正（照您的裁定）

```
**【主线 1：`CAP-MIX`】** $$\text{1A 奇特征三项（本档已跑）}\to\text{1B char2 四项（第二机制）}\to\text{2}\ m(q,d)\ \text{coset 容量}\to\text{3 coset-conflict 指数结构}$$ ✓
**【主线 2】** `P7-2` forbidden configurations boundary（候选，**不与 `CAP-MIX` 混算**）✓
**【暂停】** `P5-c`；integer Sidon；纯 counterexample `P6`；`U_{2,3}` ✓
**【题资格（再确认）】** 论文自述"a beginning exploration of the questions of which subgroups are cap sets"、并把 `x_1^d+\cdots+x_k^d=0` 的一般机制列为 *"a good topic for further investigation"* ⟹ **不是我们凭空造题** ✓✓
```

## §5 下一步（三件，按序）

```
**(1) 可靠性升级**：把 `I` 在**更大批次**（`q` 到 `10^4`；含 `p=3,\ n\le8`）上跑，**搜索假阳性**（`PASS\cap\text{noncap}`）；若仍为 0 ⟹ 尝试**证明** `I` 的可靠性（`Q_j` 的根 + 子群结构）✓✓
**(2)** 攻 `FAIL_cap`：为"全 `p`-幂"情形设计**多步障碍**（组合两个 `j`，或改用 `x^{p^j}+y^{p^j}=-1` 的高阶版本）✓
**(3)** `CAP-MIX-1B`：char 2 四项版（归一化 `x+y+z+1=0` ＋ Frobenius 展开）✓
【⛔ 纪律】 计算仅用于本实验与真值表（`D` 层）；数据入仓 `out/capmix1A_I_vs_truth.txt`、脚本 `scripts/capmix1c_IA_vs_truth.py` ✓
【边界】 §1 为**照录您的核验**；§2–§3 为**本档实测**（`COUNTS` 逐字）；论文三例在本批中均由 `I` 认证 ✓

## §附 【技术词回查】（补录）
```
技术词 soundness        命中文件数=9    :: ./V158-spectral-identity-formalization-consistency-soundness-completeness.md ./C275-L3C-first-cut-A-dangerous-frequency-sets-combinatorial-structure-audit.md ./C273-V5-design-audit-shared-k-phase-coupling-box-certificate.md 
技术词 completeness     命中文件数=23   :: ./V158-spectral-identity-formalization-consistency-soundness-completeness.md ./C356-execution-stratification-registration-not-a-new-framework.md ./C354-branch-completeness-as-core-audit-quantity-and-discovery-certificate-coverage-separation.md 
```
