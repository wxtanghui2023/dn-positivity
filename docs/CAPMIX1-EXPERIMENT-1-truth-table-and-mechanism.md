已查地图：命中（`P5-YI-and-P7-round2-hits`／`TOPIC-INVENTORY-v2-asset-driven-research-space`）⟹ 执行其下一步（小型攻击实验），不开新案
D0: 本档对象 = **CAP-MIX-1 实验一**：真值表（26 个 cap 例）＋ **Frobenius 障碍机制抽出**（含"信息型 vs 退化型"判据）＋ 论文两例印证 ＋ **char 2 无限族异常**
D1: 1 （**新自由度**：抽出可计算的机制不变量 `I(p,n,d)`，并给出退化/信息型的判别）✓
FREEZE-ACK: D1-ESCAPE
[REVIEW]

# **CAP-MIX-1 实验一：真值表 ＋ 机制**

## §1 归约（已确认）

```
$$G=G_{q,d}=\{x\in\mathbb F_q^*:x^d=1\},\qquad d\mid q-1$$ ✓
$$G\ \text{非 cap}\iff\exists\ \text{相异}\ a,b,c\in G:\ a+b+c=0\iff\exists x,y\in G:\ x+y=-1\ \text{且}\ \{x,y,1\}\ \text{相异}$$ ✓✓
```

## §2 ⭐⭐ 机制：Frobenius 障碍（**本档抽出**）

```
**【推导】** 设 `x+y=-1`（`y=-(x+1)`），由 `\mathrm{Frob}^j` 与 `x^d=y^d=1`：$$\underbrace{(x+1)^{p^j}=x^{p^j}+1=x^{r}+1}_{r:=p^j\bmod d}\quad\text{且}\quad (x+1)^{p^j}=(-y)^{p^j}=(-1)^{p^j}y^{r}=(-1)^{p^j}(-(x+1))^{r}$$ ✓
$$\Longrightarrow\ \boxed{Q_j(x):=x^{r}+1-(-1)^{\,p^j+r}(x+1)^{r}=0},\qquad r=p^j\bmod d$$ ✓✓
**【⟹ 可计算不变量】** $$I(p,n,d):=\ \exists j\ \text{s.t.}\ Q_j\ \text{在}\ G\ \text{上的根}\ \text{全为平凡}\ \Longrightarrow\ G\ \text{是 cap}$$ ✓✓
**【⭐⭐ 关键判据（本档新增）】** `Q_j` **退化**（恒为 0，无信息）$$\iff r=p^j\bmod d\ \text{是}\ p\ \text{的幂}\ \text{且}\ (-1)^{p^j+r}=+1$$ ✓✓（因 `\mathrm{char}\,p` 下 `(x+1)^{p^i}=x^{p^i}+1`）
　⟹ **首个"信息型" `j` = 最小的使 `p^j\bmod d\notin\{p^0,p^1,\dots\}` 者** ✓✓
**【机制印证（论文逐字）】** 论文对 `q=243,d=22` 用 `27=3^3\equiv5\ (\mathrm{mod}\ 22)` ⟹ 信息型 `j=3,r=5`，得 `(x+1)^5-x^5-1=0`，因式分解 `-x(x+1)(x-1)^2` ⟹ `x=1` ⟹ cap ✓✓ **与本档判据完全一致** ✓✓
```

## §3 真值表（`p\in\{2,3,5,7,11,13\}`，`q\le729`；共 **26 个 cap 例**）

```
**【论文三例全部印证】** $$(81,20):\ \text{cap},\ \textbf{complete};\qquad (243,22):\ \text{cap},\ \textbf{complete};\qquad (729,28):\ \text{cap}$$ ✓✓✓（论文称 `G_{243,22}` 为 complete cap ✓；`G_{81,20}` 亦为 complete ✓）
**【新发现的 cap 例（论文未列）】** ✓✓
$$p=3:\ (9,4)^{c};\ (81,4),(81,5),(81,10),(81,20)^{c};\ (243,11),(243,22)^{c};\ (729,4),(729,7),(729,14),(729,28)$$
$$p=5:\ (25,4),(25,8)^{c};\ (125,4)\qquad p=7:\ (49,4),(49,8)\qquad p=11:\ (121,4),(121,5),(121,8)\qquad p=13:\ (169,4),(169,7),(169,8),(169,14)$$
$$p=2:\ (16,5)^{c};\ (256,5),(256,17)$$
　（上标 `c` = **complete cap**）✓
**【非 cap 例（极小 AP 已提取）】** 无 `cert` 者，如 `(729,8),(729,13),(729,26),(729,52),(729,56),(729,91),(729,104),(729,182),(81,8),(81,16),(81,40),(81,80),(49,16),(121,10),(169,21),(64,7),(64,9),(256,15),(256,51),(256,85)` ✓（**每个都附极小 AP 元素（域元素元组形式）**）✓
```

## §4 ⚠️ 异常：char 2 的"无限族"**不成立**（须核）

```
**【论文声称】** `\mathbb F_{2^{2n}}` 中 `(2^n-1)` 次幂子群（阶 `2^n+1`）是 cap ✓
**【本档实测】**
$$2n=4\ (q=16,\ d=5):\ \textbf{cap}\ \checkmark;\qquad 2n=8\ (q=256,\ d=17):\ \textbf{cap}\ \checkmark;\qquad \boxed{2n=6\ (q=64,\ d=9):\ \textbf{非 cap}}\ \times$$ ✓✓
**【反例（极小 AP，`G_{64,9}`）】** $$1,\ b,\ b+1\in G\quad\text{其中}\ b=(1,0,0,1,1,1)$$ ⟹ `1+b+(b+1)=0` ⟹ **三点共线 ⟹ 非 cap** ✓✓
**【⟹ 判定】** **或**论文的族另有奇偶条件（本档数据呈"`n` 为偶数 ⟹ cap"），**或**其"cap set"定义与本档不同 ⟹ **须逐字核原文定理陈述** ⚠️⚠️
　（**这是本档最有价值的异常**：若确为真，则论文该族需修正；若为本档误读，则须弄清定义差异）✓
```

## §5 下一步（三件，按序）

```
**(1)** **核 `§4` 异常**：取 `arXiv:2604.26989` 定理原文，核对族的**奇偶/参数条件**与"cap set"定义 ✓✓
**(2)** 实现**信息型 `j` 版 `I(p,n,d)`**，并在**新批次**参数上测其**预测力**（`PASS ⇒ cap` 是否成立；有无比直接枚举更强的推论）✓
**(3)** `m(q,d)`（coset 并的最大 cap 容量）：对 `(729,28)` 跑 coset 冲突分析（本档**未做**）✓
【⛔ 纪律】 **计算仅用于本次实验与真值表**（D 层）；`U_{2,3}` 暂停；`T-1` 仍为 calibration ✓
【数据】 `out/capmix1_truth_table.txt`；脚本 `scripts/capmix1b_truth_table.py` ✓

## §附 【技术词回查】（补录）
```
技术词 Frobenius obstruction 命中文件数=0    :: 
技术词 cap              命中文件数=285  :: ./V167-five-device-audit-double-obligation-structure.md ./EDR-CAP-1-run-invalid-and-Bn-equals-1-structural-point.md ./E177-E178-support-geometry-closure.md 
```
