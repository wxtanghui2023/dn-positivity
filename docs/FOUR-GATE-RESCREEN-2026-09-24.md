已查地图：命中（`C06-CLOSED-final-g0-round` ＋ `CANDIDATE-CENSUS-v1` §10）⟹ 四维重筛（零计算），不开新案
D0: 本档对象 = **全余项池四维重筛（9 项）**：`D03/G05/G06/G08/M04/Au06/P5-乙-2/P6/P8` ＋ 逐项四闸树 ＋ 终局判定（`WAITING FOR NEW SOURCE`）＋ 复活条件
D1: 0（审计型，零计算）
[REVIEW]

# **四维重筛（`2026-09-24`）**

## §0 闸门定义（照先生）

```
$$G1\ \text{独立问题}:\ \text{本身是否独立数学问题（非 RH 变体／非已有资产换壳）};\quad \text{FAIL}\Rightarrow DROP$$
$$G2\ \text{新量}:\ \text{是否存在尚未被现有理论直接固定、可检验的新结构量};\quad \text{FAIL}\Rightarrow DROP$$
$$G3\ \text{可证明性}:\ \text{能否形成有限、明确、可证伪的证明链（而非开放式大搜索）};\quad \text{FAIL}\Rightarrow DROP$$
$$G4\ \text{前沿新性}:\ \text{精确对象／参数化／等价表述／充要条件／近期文献是否已覆盖};\quad \text{FAIL/WATCH}\Rightarrow \text{不 ENTER}$$
$$\textbf{候选合法性（}\textsc{amend-22}\text{）}:\ \text{仅从已登记 census 余项中取};\ \textbf{禁止为填池重新发明新问题}$$ ✓✓
$$\textbf{硬要求}:\ \boxed{\text{“这个问题还没人完全解决”}\ne\text{“我们有新的数学量可以攻击它”}}$$ ✓✓
```

## §1 逐项四闸树（9 项）

```
$$\textbf{A. Zone-A}$$
$$\textbf{D03}\ \text{【给定参数非同构设计个数】（}F9,P_4,\texttt{ED}\text{）}$$
$$\quad G1:\ \textbf{PASS}\ (\text{差集/设计存在性与同构分类是独立经典问题})$$
$$\quad G2:\ \boxed{\textbf{FAIL}}\ \text{“非同构个数”本身即计数，无独立于计数/自同构不变量之外的}\ \Phi;\ \textbf{且形态与刚 CLOSED 的 }C06\ \text{同型}$$
$$\quad G3:\ \textbf{FAIL}\ (\text{给定参数的设计枚举＝开放式穷举，非有限可证伪链})$$
$$\quad G4:\ \textbf{FAIL}\ (\text{设计理论已有成熟数据库与分类文献；}P_4\ \text{本身即"部分已覆盖"})$$
$$\quad \Longrightarrow\ \boxed{\textbf{CLOSED}}$$

$$\textbf{B. Zone-B WATCH}$$
$$\textbf{G05}\ \text{【小群中 }|H\cap gKg^{-1}|\ \text{的精确分布】}:\ G1\ \textbf{FAIL}\ (\text{群族}/n/\text{目标量未定}\Rightarrow\text{未形成良定义问题});\ \text{且交集数是古典双陪集/Hecke 对象}$$
$$\quad \Longrightarrow\ \boxed{\textbf{DROP-pending-spec}}\ (\text{复活条件：先生补 spec 后重筛})$$
$$\textbf{G06}\ \text{【}n\le256\ \text{阶群生成元对数最小值＋达到者分类】}:\ G1\ \textbf{PASS-ish}\ (\text{歧义澄清后良定义});\ G2\ \boxed{\textbf{FAIL}}\ (\text{最小生成元数 }d(G)\ \text{与"两元素生成概率"皆古典（Hall 1936 的 Möbius 公式；Dixon；Lucchini–Menegazzo）；"生成元对"⟹生成概率})$$
$$\quad G3:\ \text{PARTIAL}\ (\text{小阶群可由 GAP 穷举});\ G4\ \textbf{FAIL/WATCH}\ (\text{文献密集＋可算})$$
$$\quad \Longrightarrow\ \boxed{\textbf{CLOSED}}$$
$$\textbf{G08}\ \text{【小阶群特征标表上独立量的极值】}:\ G1\ \textbf{FAIL}\ (\text{“独立量”未定义}\Rightarrow\text{无对象})$$
$$\quad \Longrightarrow\ \boxed{\textbf{DROP-pending-spec}}$$
$$\textbf{M04}\ \text{【小尺寸 }(0,\pm1)\text{-矩阵 rank 分布】}:\ G1\ \text{PARTIAL}\ (n\ \text{与域未定});\ G2\ \boxed{\textbf{FAIL}}\ (\text{rank 分布＝计数本身，无新量});\ G3\ \textbf{FAIL}\ (\text{开放式穷举});\ G4\ \textbf{FAIL}\ (\pm1\ \text{矩阵 rank 已有成熟文献})$$
$$\quad \Longrightarrow\ \boxed{\textbf{CLOSED}}$$
$$\textbf{Au06}\ \text{【特定类 Collatz 型停时记录（有界域）】}:\ G1\ \textbf{FAIL}\ (\text{“特定类”未定});\ G2\ \textbf{FAIL}\ (\text{记录＝计算本身});\ G4\ \textbf{FAIL}\ (\text{Collatz 型属 AI 高收割区})$$
$$\quad \Longrightarrow\ \boxed{\textbf{CLOSED}}$$

$$\textbf{C. 其他合法余项}$$
$$\textbf{P5-乙-2}\ \text{【}2A\ \text{中 coset 的余维数（Green 100 问题之一；Sanders question）】}:\ G1\ \textbf{PASS}\ (\text{独立、具体、良定义})$$
$$\quad G2:\ \boxed{\textbf{FAIL}}\ (\text{加法能量／容量／coset 余维皆古典；且原判词已注明“}D\ \text{不进场 ⟹ 我方差异化弱”})$$
$$\quad G3:\ \textbf{FAIL}\ (\text{阈值附近 }\alpha\to\tfrac12^-\ \text{行为＝渐近问题，非有限链})$$
$$\quad G4:\ \textbf{FAIL}\ (\text{在 Green 的 100 问题公开清单上；Sanders question 已被研究；}\textbf{且邻近两个已关闭分支}：CAP-MIX（ARCHIVED）与加法组合/PFR 通道（REJECT）)$$
$$\quad \Longrightarrow\ \boxed{\textbf{CLOSED}}$$
$$\textbf{P6}\ \text{【最小反例/机制失效】}:\ G1\ \textbf{FAIL}\ (\text{清单中仅为}\textbf{形式}，\text{未登记任何具体 }P\Rightarrow Q\ \text{机制})$$
$$\quad \Longrightarrow\ \boxed{\textbf{DROP（形式受限）}}$$
$$\textbf{P8}\ \text{【算术数据驱动的独立问题】}:\ G1\ \textbf{FAIL}\ (\text{无具体实例};\ \text{且硬禁 }P8\ne\text{RH 变体})$$
$$\quad \Longrightarrow\ \boxed{\textbf{DROP（形式受限）}}$$
```

## §2 终局判定

```
$$\boxed{\text{ENTER G0 的候选数}=\textbf{0}}$$ ✓✓
$$\qquad \text{CLOSED}:\ D03,\ G06,\ M04,\ Au06,\ P5\text{-乙-}2\ (5\ \text{项})\ (\text{主因 }G2\ \text{新量不足，佐以 }G3/G4)$$
$$\qquad \text{DROP-pending-spec}:\ G05,\ G08\ (2\ \text{项})$$
$$\qquad \text{DROP（形式受限）}:\ P6,\ P8\ (2\ \text{项})$$
$$\Longrightarrow\ \boxed{\textbf{WAITING FOR NEW SOURCE}}\ (\text{与 E-40 §6 状态一致})$$ ✓✓
$$\textbf{措辞纪律}:\ \text{不是“这些问题没有价值”，而是}\boxed{\text{已登记余项池在本套闸门下无合格项}}$$ ✓
$$\textbf{不制造候选}:\ \text{不得为填池发明新问题};\ \text{不得让 }D03\ \text{因“Zone-A 最后一项”而获得优先权（照先生令）}$$ ✓✓
```

## §3 复活条件（唯一合法入口）

```
$$\textbf{(a) Zone-B 两项（}G05,G08\text{）}:\ \text{先生补 spec（群族/}n/\text{目标量；"独立量"定义）后重跑四闸};$$
$$\textbf{(b) 形式受限两项（}P6,P8\text{）}:\ \text{须登记}\textbf{具体机制／具体问题实例};\ \text{仅形式不得入场};$$
$$\textbf{(c) 已 CLOSED 五项}:\ \text{除非出现}\textbf{新数学量}（\text{可定义 }\Phi\ \text{且未被旧不变量耗尽}）\ \text{或新覆盖判定被推翻，否则不再重开};$$
$$\textbf{(d) 新来源}:\ \text{独立来源的具体数学问题（非从旧墙/旧资产反推）}\Rightarrow\ \text{直接进四闸}.$$
【⛔ 纪律】 本轮**零数学计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 逐项判定基于已登记字面＋检索抽取级证据；**未逐字核验**外部原文 ✓
