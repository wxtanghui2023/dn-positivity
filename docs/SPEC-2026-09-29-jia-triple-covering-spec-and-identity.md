# SPEC-2026-09-29-jia — 「甲」三重覆盖不等式（r=1 类比）· spec ＋ 第一步恒等式

> 空间 B｜非 C 号｜唐先生令（09-29 22:21）「**首先复现 107**」之第一步｜**不主张 107 已证**（V290）
> 时间：2026-09-29 22:2x

**已查地图**：未覆盖（关键词：三重覆盖／triple covering／构型账）—— 查 `CLOSED-ROUTES-MAP.md`／`MASTER-FAILURE-MAP-107-LINE.md` §3＋§6／`ROUTE-FINGERPRINTS.tsv`／`AUDIT-2026-09-29n`（pair-covering 开案审查）
D0: 本档对象 = 档案已有（三点构型／三重覆盖／μ-场）之**新恒等式形式**（新数学对象：无 ✗）
D1: 0（产出 = 引理 ＋ 恒等式核验 ＋ spec ⚠️✓）

---

## §1 为何走三重层（查地图结论，逐条可核）

| 路线 | 状态 | 依据 |
|---|---|---|
| pair 层（任何形式） | **CLOSED-103**（三次独立失败）✗ | R02／`AUDIT-29n` §1（甲） |
| Struik/van Wee **一阶局部**不等式 | **奇 n 处为空** ✗ | `ODDENGINE`（`AUDIT-29n` §1 乙） |
| **单条**线性不等式 | **已证不可能** ✗✓ | `AUDIT-29e`：任何单条 ≤ LP ≤ SDP-3 = 105.2223 < 107 |
| 高阶 SDP | DEAD-BY-AUTHORS ✗ | R15／`AUDIT-29d` |

$$\therefore\ \text{唯一未被封闭的\ \textbf{组合}入口} = \textbf{三重层}\ (\texttt{MASTER-FAILURE-MAP}\ \S6\ \text{甲})$$
$$\boxed{\text{关键}:\ \text{三重统计量对 }\mu\ \text{是\ \textbf{三次}的}\ \Longrightarrow\ \textbf{不在}\ \texttt{AUDIT-29e}\ \text{的"单条线性"禁令内}\ ✓✓}$$

## §2 第一步（**本档实跑，可复跑**）

### 引理 T（穷举核验，n=9,10 两例）

$$\text{两两距离}\le2\ \text{的码字三点组，轨道\ \textbf{仅两型}}\ (\text{Aut}(Q_n)=\text{平移}\times\text{坐标置换}):$$
- **(1,1,2)-路**：$\{u,\ u{\oplus}e_i,\ u{\oplus}e_i{\oplus}e_k\}$（$i\ne k$）—— 长边唯一
- **(2,2,2)-等边**：$\{u,\ u{\oplus}e_i{\oplus}e_j,\ u{\oplus}e_i{\oplus}e_k\}$（$i,j,k$ 互异）—— 两个 2-集交于 1 元

$$\boxed{\text{且每型之公共点\ \textbf{恰 1 个}}\ \Longrightarrow\ \text{三点组}\mapsto\text{公共点}\ \text{为\ \textbf{单射}}\ ✓}$$

### 恒等式 T

$$\boxed{\ \sum_x \binom{\mu(x)}3\ =\ \#\{\text{两两 }d\le2\ \text{的码字三点组}\}\ =\ P+E\ }$$
$$P:=\sum_{y\in C}\binom{a_y}2\quad(a_y:=\#\{c\in C:\ d(c,y)=1\}),\qquad E:=\#\{\text{等边三点组}\}$$

### 实测（逐字）

| 码 | μ 分布 | $A_1$ | $A_2$ | $P$ | $E$ | $\sum_x\binom{\mu}3$ | 恒等式 |
|---|---|---|---|---|---|---|---|
| $n{=}9$ 62-码 | $\{1{:}432,2{:}62,3{:}8,4{:}10\}$ | 7 | 66 | 6 | 42 | 48 | $48=6+42$ ✓✓ |
| $n{=}10$ 120-码 | $\{1{:}801,2{:}172,3{:}36,4{:}8,5{:}7\}$ | 50 | 149 | 41 | 97 | 138 | $138=41+97$ ✓✓ |

**旁证** ✓✓：$A_1{+}A_2=73／199$ 与档案 $\texttt{N}_{\le2}$ 值**逐字一致** ✓；$\sum_x\binom{\mu}2=2(A_1{+}A_2)$ 亦核 ✓
**脚本**：`scripts/triple_config_n10.py`

## §3 与 107 的接线（下一步目标）

$$\text{复现 }107\iff\text{排除 }M{=}106\ (\Sigma\delta=142)\ \Longleftrightarrow\ \text{证}\ \Sigma\delta\ge143$$
$$\text{恒等式 T 把\ \textbf{三次点统计}\ 换成\ \textbf{码字三点组计数}}\ \Longrightarrow\ \text{需要一对夹逼}:$$
- **（下界）** 由覆盖条件 ＋ $\Sigma\delta$ 强制 $P+E\ \ge\ f(M)$
- **（上界）** 由局部结构／packing 强 $P+E\ \le\ g(M,A_1,A_2)$
- 在 $M{=}106$ 处 $f>g$ ⟹ 矛盾 ⟹ $K\ge107$ ✓

## §4 边界（硬 ✓）

- **不主张 107** ✗；恒等式 T 是**等式**，**尚未**产生任何不等式 ⚠️
- **未重攻** pair 层（R02）✓；**未取任何论文原文／未转录公式**（R16／R17）✓；未动 RH ✓；零大规模计算（两例皆 $O(M^2)$ 级）✓

## §5 【技术词回查】（先跑后写，逐字粘贴）

```
技术词 三重覆盖        命中文件数=15   :: ./CHAIN-VW-2026-09-27-… ./AUDIT-2026-09-29d-… ./ALG-VW-2026-09-27-…
技术词 构型账          命中文件数=0    ::
技术词 公共点          命中文件数=6    :: ./BFREEZE-2026-09-27-… ./ASSETS-REGISTRY.md ./CALIBRATE-n5b-2026-09-29-…
技术词 triple covering 命中文件数=2    :: ./PROTOCOL-T0-T7-… ./AUDIT-2026-09-29n-…
```

分类 —— **本档新增 = 0**（`构型账` 命中 0 ⟹ 为**本档自造标签**，仅作结构命名，**不作新性主张** ✓）；
**档案已有（引用，不列为提出）** = 三重覆盖（15）｜公共点（6）｜triple covering（2）；
**通用词（不计）** = —（紧签名原则 ✓）

ROUTE-CHECK: R01=FINGERPRINT-CITED R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
