# DS243-2026-09-30 — Survivor-1 具形化：**$(\mathbb Z_3\times\mathbb Z_9^2,\ 243,121,60)$** 之浮点定位 ＋ **乘子约化（99 轨道）** ＋ 商群必要条件 ＋ 构造探针

> 空间 B｜非 C 号｜唐先生 12:13「(丙) 升级版：只推 $\mathbb Z_3\times\mathbb Z_9^2$ 的群特异性必要条件」｜**不主张任何新值**（V290）
> 时间：2026-09-30 12:2x

**已查地图**：`POOL-2026-09-30-V2`（Survivor-1 ✓）／`ASSET-TO-PROBLEM-MATCHING-v1`（M9/M12 ✓）／`prework_map_check.sh`（四词，未覆盖 ✓）
D0: 本档对象 = **LJCR 差集库之 Open 格**（外部数据 ✓；无新数学对象 ✓）
D1: 0（产出 = **一处对象更正 ＋ 一张 7 群指纹表 ＋ 一条乘子约化 ＋ 一组商群条件 ＋ 一个探针** ⚠️✓）

---

## §0 **对象更正（唐先生指出，本档已用库逐字核实 ✓）**

$$\text{我上轮报的 }"G=3"\ \textbf{是解析漏位} ✗\ (v{=}243\ \text{须 }|G|{=}243);\ \text{正确之格由库文逐字给出如下}:$$

| $G$（阶 243 之全部 7 个交换群） | status | 依据（库之 comment 逐字） |
|---|---|---|
| $\mathbb Z_{243}$ | **No** | Lander, Theorem 4.38 |
| $\mathbb Z_3\times\mathbb Z_{81}$ | **No** | Lander, Theorem 4.38 |
| $\mathbb Z_3^2\times\mathbb Z_{27}$ | **No** | Lopez and Sanchez |
| $\mathbb Z_3^3\times\mathbb Z_9$ | **No** | Lopez and Sanchez |
| $\mathbb Z_9\times\mathbb Z_{27}$ | **No** | **Arasu and Ma, 2001**（＝唐先生所引文献 ✓） |
| $\mathbb Z_3^5$ | **Yes** | **Paley**（1 个已知集 ✓） |
| $\boxed{\mathbb Z_3\times\mathbb Z_9^2}$ | **Open** ✓ | （无 comment） |

$$\therefore\ \textbf{Survivor-1}\ \text{之精确对象} = \boxed{(\mathbb Z_3\times\mathbb Z_9^2,\ 243,121,60)}\ \text{——同一 }(v,k,\lambda)\ \text{下，\textbf{群结构决定难度}（Paley }\mathbb Z_3^5\ \text{有解 vs 本群 Open）} ✓✓$$

## §1 **乘子约化**（本档核心新工具 ✓）

$$n:=k-\lambda=61\ (\textbf{素数}\ ✓);\quad \gcd(61,243)=1\ ✓;\quad 61>\lambda=60\ ✓$$
$$\Longrightarrow\ \text{第一乘子定理（Hall–Ryser 型）条件满足} \Longrightarrow \boxed{61\ \text{是乘子}} ⚠️\ (\text{确切假设待核}：\text{须 }p\ \text{不整除群阶／且满足定理陈述之附加条件})$$
$$\text{其作用}:\ \sigma:x\mapsto 61x\equiv x^{7}\ (\text{逐分量},\ \exp(G){=}9\Rightarrow 61\equiv7\bmod 9)\quad\text{且}\ \sigma^3=\mathrm{id}\ ✓$$
$$\text{轨道结构（实测）}:\ \boxed{27\ \text{个不动点}\ +\ 72\ \text{个 3-轨道}\ =\ 99\ \text{轨道}}$$
$$\Longrightarrow\ \text{可设 }D\ \text{为 }\sigma\text{-不变} \Longrightarrow \textbf{搜索压到 }99\ \text{个布尔变量}\ ✓✓\ (\text{原 }C(243,121)\approx10^{72})$$

## §2 **商群/子群必要条件**（唐先生所指"quotient-group 约束" ✓）

$$\text{对子群 }H\le G:\ \text{陪集 }C\ \text{上记 }r_C:=|D\cap C|;\quad \sum_C r_C=k=121;\quad \sum_C r_C(r_C-1)=\lambda(|H|-1)$$
$$\text{（因每非零 }z\in H\ \text{恰被表 }\lambda\ \text{次；}z\ne0\ \text{之 }H\text{-差 ⟺ 同陪集 ✓）}\Longrightarrow \sum_C r_C^2=\lambda(|H|-1)+k$$
| $H$ | 陪集数 | $\sum r_C^2$ 目标 | **解数** | 排除？ |
|---|---|---|---|---|
| $\mathbb Z_9$ | 27 | 601 | $3.93\times10^{18}$ | ✗ |
| $\mathbb Z_3$ | 81 | 241 | $\sim10^{42}$ | ✗ |
| $\mathbb Z_3\times\mathbb Z_9$ | 9 | 1681 | $1.84\times10^{6}$ | ✗ |
| $\mathbb Z_3^2$ | 27 | 601 | $3.93\times10^{18}$ | ✗ |
| $\boxed{\mathbb Z_9^2}$ | **3** | 4921 | **6** ✓✓ | ✗（仅 6 个分布，极紧） |

$$\therefore\ \text{全部商群条件\ \textbf{不排除}（解数}>0\text{）} \Longrightarrow \text{无新非存在性} ✗;\ \text{但 }H=\mathbb Z_9^2\ \text{给出极紧之 6 分布（可作后续细筛）} ✓$$

## §3 构造探针（P2 侧）—— 两次运行（含一次 bug 修正 ✓）

$$\text{空间}:\ \sigma\text{-不变集（99 布尔，}|D|{=}121\text{）}；\quad \text{目标}:\ \Sigma_{z\ne0}(c_z-60)^2=0\ (242\ \text{个非零元各恰 60 次})$$

| 版本 | 结果 | 判定 |
|---|---|---|
| v2（`ds243_search_v2.py`） | 87,053,431 次迭代，obj 恒 7128，**\|D\|=120 ✗** | **无效探针** ✗ —— bug：初解把 27 个不动点**全选满** ⟹ 两类移动均不可行 ⟹ 全部空转 ✗（自查 ✓） |
| **v3（`ds243_search_v3.py`）** | **61,146 次迭代（61,143 可行移动），obj 1016 → 344，\|D\|=121 ✓** | **探针有效但未解出** ⚠️：真实下降（单调 ✓），180s 不够 |

$$\text{v3 之读数}:\ obj{=}344\ \text{在 242 个约束上} \Longrightarrow \text{平均 }(c_z-60)^2\approx1.4 \Longrightarrow \text{平均偏差}\approx1.2/\text{元} ⟹ \textbf{“接近”但不精确} ✗$$
$$\therefore\ \text{搜索机制可行（}|D|\ \text{保持 }121 ✓,\ \text{obj 单调降 ✓）}；\text{但需要更强算力或更好算子} ⚠️$$

## §4 判定与去向

$$\textbf{① }\text{群特异性条件}\ \textbf{未} \text{排除本群} ✗ \Longrightarrow \text{按唐先生流程进入 P2（构造）} ✓$$
$$\textbf{② 乘子约化是关键资产}:\ 99\ \text{布尔变量 ＋ 242 个差计数约束} \Longrightarrow \text{可上 MILP/SAT（线性化后 }\sim5\times10^3\ \text{变量）} ✓$$
$$\textbf{③ 若探针无解} \Longrightarrow \text{两点选择}:\ (a)\ \text{升级为完整 MILP/CP-SAT（更大算力）};\ (b)\ \text{改攻 }H{=}\mathbb Z_9^2\ \text{之 6 分布细筛} ✓$$
$$\textbf{④ 若探针有解} \Longrightarrow \text{显式差集} \Longrightarrow \text{秒级独立验证} \Longrightarrow \textbf{关闭一个 Open 格} ✓✓✓$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**对象更正 ＋ 工具化 ＋ 探针**（外部数据，LJCR 库 ✓）
- 乘子定理之确切假设**待核** ⚠️（未取文献原文 ✗）；未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
