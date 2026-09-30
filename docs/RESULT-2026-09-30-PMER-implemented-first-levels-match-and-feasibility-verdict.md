# RESULT-2026-09-30 — **PMER 已实现**：$N_1,N_2$ 与手算**逐位吻合** ✓✓；但**层数增长 ×17→×42** ⟹ $n{=}10$ **不可行**（有据 ✗）

> 空间 B｜非 C 号｜唐先生 17:0x–17:5x｜**不主张任何新值**（V290）
> 脚本：`scripts/pmer_recursion.py`（状态＝层 $k$ 之 multiplicity profile；转移＝整数分裂；剪枝＝$F_k$；商＝$\mathrm{Aut}(Q_k)$）

**已查地图** ✓：`RESEARCH-2026-09-30-local-to-global…`／`RESULT-2026-09-30-coord-search-machinery…`（逐词构造机器，$n{=}6$ 已超时 ✗）
D0: 本档对象 = **档案已有框架之首个实现 ＋ 实测标度数据**（新数学对象：无 ✗）
D1: 0（产出 = **两张 $N_k$ 表 ＋ 一条外推 ＋ 一条可行性判定** ⚠️✓）

---

## §1 **核验（与唐先生手算逐位吻合 ✓✓）**

$$\text{(a) }k{=}2,\ M{=}106:\ \text{有序解}\ (a,b,c,d),\ \sum{=}106,\ F_2\ \text{四式}:\ \mathbf{886}\ \text{（唐先生报 886 ✓✓）}$$
$$\text{(b) }I_k(S)\ \text{引理}:\ (11{-}2k)m(S)+106k\ge|S|2^{10-k}\ \text{——}\ k{=}3:\ m(S)\ge38.8\Rightarrow\mathbf{39}\ ✓;\ k{=}4:\ \ge29.33\Rightarrow\mathbf{30}\ ✓;\ k{=}5:\ -18\Rightarrow\textbf{\text{无力量}}\ ✓\ \text{（三处皆吻合 ✓✓）}$$
$$\qquad\text{（引理证明：对 }S\ \text{独立集求和 }F_k,\ \sum_{v\in S}\sum_{u\sim v}m(u)\le k(106-m(S))\ ✓\ ——\ \textbf{\text{正确}} ✓）}$$

## §2 **实测 $N_k$ 表（orbit 数，已按 $\mathrm{Aut}(Q_k)$ 商 ✓）**

| $(n,M)$ | $N_1$ | $N_2$ | $N_3$ | 断点 |
|---|---|---|---|---|
| $(9,61)$（回归，真值 $K{=}62$） | $\mathbf 6$（$(25,36)\ldots(30,31)$） | $\mathbf{65}$ | $\mathbf{1370}$ | $k{=}3{\to}4$ 于第 441/1370 超时 ✗ |
| $(10,106)$ | $\mathbf 8$（$(46,60)\ldots(53,53)$） | $\mathbf{134}$ | $\mathbf{5674}$ | $k{=}3{\to}4$ 于第 93/5674 超时 ✗ |

$$\textbf{增长因子}:\ (10,106):\ 8\to134\ (\times\mathbf{16.8})\to5674\ (\times\mathbf{42.3})\ ⚠️;\quad (9,61):\ 6\to65\ (\times{10.8})\to1370\ (\times{21.1})\ ⚠️$$
$$\Longrightarrow\ \textbf{\text{因子递增}} ⟹ \text{外推 }N_4\sim10^5,\ N_5\sim10^7,\ N_9\sim10^{14}\ ✗✗\ \text{——远超任何机器} ✗$$

## §3 **可行性判定（有据 ✗）**

$$\boxed{\text{PMER（以 }F_k\ \text{为剪枝）之第一层压缩极强（}10^{147}\to8\to134\to5674\ ✓✓\text{），但层增长}\ \times17\to\times42\ \textbf{\text{递增}} ⟹ n{=}10,M{=}106\ \textbf{\text{不可行}} ✗}$$
$$\text{结构性原因（可诊断 ✓）}:\ F_k\ \text{求和后}\ \textbf{\text{恰为球界}}\ (11M\ge1024)\ \text{——即它仍是\ \textbf{聚合型} 条件};\ \text{而 }\mathrm{Aut}\ \text{商已做到（本实现即轨道计数 ✓）} ⟹ \textbf{\text{无剩余压缩空间可挖}} ⚠️$$
$$\therefore\ \text{要使其可行，只能靠\ \textbf{更强的逐层必要条件}——即\ \textbf{\text{新的非聚合数学}} ⟹ \textbf{\text{回到原问题}} ✗✓}$$

## §4 **与逐坐标构造机器之交叉验证**

$$\text{两独立实现（本档 profile 递归 vs 前档 word-level 逐坐标搜索）皆报：}n\ge7\ \text{规模爆炸} ✗\ ⟹ \textbf{\text{互证}} ✓\ \text{（非实现失误，而是机制级标度墙 ✓）}$$

## §5 **诚实结论**

$$\textbf{已得 ✓}:\ \text{框架实现；}k{=}1,2\ \text{与唐先生手算逐位吻合（}6/8,\ 65/134\ ✓✓\text{）；}N_3\ \text{首次给出（1370/5674 ✓）；可行性\ \textbf{\text{从“未知”变为“有据的否”}} ✗$$
$$\textbf{未得 ✗}:\ S_k(106)=\varnothing\ \text{之任何一层；}K(10,1)\ \text{之新值} ✗$$
$$\textbf{建议}:\ \text{(甲) 保留 106 为可复现最优、本线记为\ \textbf{\text{机制级不可行}}（有数据 ✓）};\ \text{(乙) 若要继续，唯一入口＝\ \textbf{\text{设计新的逐层非聚合必要条件}}（研究级 ✗）}$$

## §7 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 层数增长     命中文件数=1    :: 本档
技术词 机制级不可行  命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{档案已有（不列）}：无;\quad \textbf{通用词（不计）}：\text{“增长／可行”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §6 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{两处手算核对吻合（886；39/30/无）✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
