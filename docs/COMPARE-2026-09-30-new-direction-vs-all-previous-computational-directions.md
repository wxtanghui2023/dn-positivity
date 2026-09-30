# COMPARE-2026-09-30 — 新方向（逐坐标构造＋同构约化）与**我们此前全部计算方向**之理论对比 ＋ 可行性判定

> 空间 B｜非 C 号｜唐先生 16:35「先从理论上对比分析，和我们之前所有计算方向有啥差别，是否可行？」｜**不主张任何新值**（V290）
> 时间：2026-09-30 17:1x

**已查地图** ✓：C-429／C-541／L3012（未做者＝`Layer 2+`）／L1554（支撑层＝自由度）／`MASTER-FAILURE-MAP` §2 定理 A（`107 必出自非松弛`）
D0: 本档对象 = **档案已有**（Kéri 第 9 章算法 ＋ 我方历史方向）之**对比分析**（新数学对象：无 ✗）
D1: 0（产出 = **一张五维对比表 ＋ 一条算法机理复原 ＋ 一条可行性判定** ⚠️✓）

---

## §0 **算法机理复原（Kéri 第 9 章续，逐字译 ✓）**

$$\textbf{主循环}:\ \text{由 }S_{k-1}\ \text{造 }S_k,\ k=2..n\ (\text{共 }n-1\ \text{次});\quad \text{每码}\ C\in S_{k-1}\ \text{考虑}\ \textbf{\text{加一坐标之全部延拓}}\ (\text{二元 }2M,\ \text{三元 }3M\ \text{种})$$
$$\textbf{剪枝（关键 ✓）}:\ \text{“并非存储一切延拓，}\textbf{\text{而只存满足某些条件（不等式）者}}\text{”};\quad \text{末步之条件＝}\textbf{\text{“所检之码其覆盖半径 }\le R\text{”}}$$
$$\textbf{同构约化（逐层 ✓）}:\ \text{“每一步皆只令}\ \textbf{\text{互不相同且互不等价}}\ \text{之码进入 }S_k”\ ✓✓$$
$$\textbf{逐步不等式之来源（可复用之机理 ✓✓）}:\ \text{置 }Z(v)=\text{固定前 }k\ \text{坐标为 }v_1..v_k\ \text{所得之 }n{-}k\ \text{维子空间};\ \text{若 }c\in D\ \text{以余 }n{-}k\ \text{坐标延拓，}$$
$$\qquad\text{则所成 }n\ \text{词与 }Z(v)\ \text{之距离}\ \le R\ \text{者\ \textbf{恰为半径 }R-d(c,v)\ \text{之球}}\ (\text{体积 }V(t,b;R)\ \text{＝混合球体积})$$
$$\qquad\Longrightarrow\ \textbf{\text{每点 }v\ \text{处之\ Hall 型体积不等式}}:\ \bigcup_{c}\big(\text{球}_{R-d(c,v)}\big)\ \supseteq\ Z(v)\ (\text{可容量}\ge|Z(v)|)\ ✓$$

## §1 **五维理论对比（唐先生所问 ✓）**

| 维度 | 我们此前之全部计算方向 | **新方向（BÖW／[121]／[103] 族）** |
|---|---|---|
| **① 对象** | 聚合统计（$\mu$-profile／$A_i$／矩／Walsh 谱／SDP 变量） | **个别码本身**（显式码字集，逐坐标生长） |
| **② 类型** | **松弛**（LP／SDP）或**启发式**（SA／局部搜索） | **精确穷举 ＋ 同构约化**（exact ✓） |
| **③ 证书** | 只有界值 ✗（且松弛被 **定理 A＝105.2223** 封顶 ✗） | **穷举之空集 ＝ 严格下界证书** ✓✓ |
| **④ 为何被卡** | 定理 A：Aut-不变松弛 $\le105.2223<107$ ⟹ 结构上够不到 ✗；局部搜索无界且停滞 ✗ | **不是松弛 ⟹ 不受定理 A 约束** ✓✓ |
| **⑤ 信息层** | 距离／谱层（**已饱和**，L1554 ✗） | **支撑／排列层**（档案标记之**未被吃掉的自由度** ✓✓） |

$$\therefore\ \boxed{\text{这是第一个\ \textbf{既精确又非松弛} 的方向；也正是档案定理 A 所指“}\textbf{107 必出自非松弛／整性论证}\text{”的那个类}}\ ✓✓$$

## §2 **与我方具体尝试之差异（为何我方失败不构成反面证据 ✓）**

$$\text{我方曾做}:\ \text{(a) 1024 点集合覆盖式 CP-SAT／HiGHS（}\textbf{\text{无同构约化、无逐坐标剪枝}} ✗\text{）};\ \text{(b) 聚合 LP／SDP（被定理 A 封顶 ✗）};\ \text{(c) 局部搜索（无界 ✗）}$$
$$\text{新方向要求}:\ \text{(i) }\textbf{\text{逐层同构约化}}\ (\text{canonical form});\ \text{(ii) }\textbf{\text{逐层体积／Hall 剪枝}};\ \text{(iii) }\textbf{\text{末步覆盖半径判据}}$$
$$\therefore\ \boxed{\text{我方之失败\ \textbf{不构成} 新方向之反面证据 —— 因为我们\ \textbf{从未实现} 该机制}}\ ✓\ (\text{档案仅留工具指针 }\texttt{MCOVER/OBREVERSE}，并标}\ \textbf{\text{未做}} = \texttt{Layer 2+}\ ✓)$$

## §3 **可行性判定（诚实 ✓）**

$$\textbf{(a) 理论上可行 ✓✓}:\ \text{精确、非松弛、直接作用于支撑层};\ \text{且}\ \textbf{\text{历史上在 n=9（+5）与 n=10（+2）上皆成功}}\ ✓✓$$
$$\textbf{(b) 成本（crux ⚠️）}:\ \text{搜索树＝逐步}\ \text{“延拓 }\times\ \text{同构约化 }\times\ \text{体积剪枝”};\ \text{对二元 }n{=}10,M{=}106:\ \text{朴素上界 }10^{147}\ ✗\ \text{（我方旧估）}$$
$$\qquad\text{但}\ \textbf{\text{同构约化 ＋ 逐步体积剪枝}} \text{可大减 }\cdots\ \textbf{\text{究竟减到多少＝未知}} ⚠️$$
$$\textbf{(c) 唯一真正未决 ⚠️（本档最重要）}:\ [130]\ \text{之 }107\ \text{究竟出自其}\ \textbf{\text{“general lower bound for }R{=}1”}}（\text{或为\ \textbf{\text{一般性定理}}} ✓）\ \text{抑或出自此\ \textbf{\text{计算分类机制}}}（\text{计算机 }} ✗）\ ——\ \textbf{\text{二者未分}} ⚠️$$
$$\qquad\text{线索}:\ [130]\ \text{摘要含“general lower bound for }R{=}1”\ \text{＋ Kéri 证言“多计算机结果”};\ \text{其正文\ \textbf{不可得}} ✗$$

## §4 **最便宜之决定性实验（建议 ✓）**

$$\boxed{\text{实现 Kéri 第 9 章算法（\textbf{我们持有其逐字描述 ✓}），先复现 }[121]\ \text{之 }n{=}9\ \text{结果（}57\to62\text{，即证 }M{\le}61\ \text{无码）}} ✓✓$$
$$\text{理由}:\ \text{(i) 目标是\ \textbf{已知真值}（}$K(9,1){=}62$ ✓）\ ⟹ \textbf{\text{完美验证器}};\ \text{(ii) 规模远小于 }M{=}106\ ✓;\ \text{(iii) 我们持有 }n{=}9\ \text{之 }62\text{-码作锚 ✓}$$
$$\text{通过后}:\ \text{再估 }n{=}10,\ M{=}106\ \text{之成本}\ \Longrightarrow\ \text{决定是否投入}\ ✓$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 同构约化     命中文件数=2    :: 本档 ＋ FINGERPRINT-2026-09-30
技术词 体积剪枝     命中文件数=1    :: 本档
技术词 逐坐标构造  命中文件数=2    :: 本档 ＋ FINGERPRINT-2026-09-30
```

$$\textbf{分类}:\ \text{三词命中皆\ \textbf{仅本会话两档}（未超出今日新建）} \Longrightarrow \textbf{本档新增} ✓;\quad \text{“体积剪枝”为\ \textbf{首次命名} ✓}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓;\quad \text{通用词（不计）}:\ \text{“剪枝”／“约化”裸词} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{未持有 }[130]/[121]/[138]\ \text{全文（不冒充）}\ ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未主张新值／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
