# HANDOFF-2026-09-30-1830 — BÖW-107 线 会话状态与下一会话起点

> 空间 B（$K(10,1)$／119 线）｜**不主张任何新值**（V290）｜唐先生 17:01 令「继续」后收束
> 时段：2026-09-30 16:2x–18:3x（GMT+8）

**已查地图** ✓：本档为**交接登记型**（引用 `SOURCE-2026-09-30`／`CORRECTION-2026-09-30`／`LOCALIZE-2026-09-30`／`STATE-2026-09-30`／`RESULT-2026-09-30-tight-per-y…`／`…crosslevel…`／`…equality-case-rigidity…`）
D0: 本档对象 = **档案已有**（本日各档）之**汇总登记**（新数学对象：无 ✗）
D1: 0（产出 = **六项净结果 ＋ 三入口 ＋ 边界声明** ⚠️✓）

---

## §1 **本轮净结果（可复核 ✓）**

$$\textbf{(A) 文献事实（第一手 ✓）}:\ \text{Kéri 全文（我们实有）逐字给出 }K(10,1)\ \text{阶梯}\ 94\to96\ [18]\to97\ [46]\to103\ [52]\to105\ [67]\to\mathbf{107}\ [130]$$
$$\qquad\text{及 }n{=}9\ \text{阶梯}\ 52\to54\to55\ [82]\to56\ [112]\to57\ [103]\to\mathbf{62}\ [121];\quad \text{并载}\ \textbf{\text{[130] 因“含大量计算机结果”被首投期刊拒}}} ✓$$
$$\textbf{(B) 四重排除}:\ \text{BÖW-107}\ \textbf{\text{非}} \text{excess 族（含 mixed 应用；Haas 2008 逐字；其全部新界在 }(10,1)\ \text{皆 }103）;\ \textbf{\text{非}} \text{逐坐标分类（包络 }M\lesssim20\ \text{＋逾一周机时）};\ \textbf{\text{非}} \text{单线性不等式（}\le105.2223）;\ \textbf{\text{非}} \text{松弛（定理 A）}$$
$$\qquad\Longrightarrow\ \text{只能出自}\ \textbf{\text{混合码 }R{=}1\ \text{之新一般不等式（非松弛）}}\ ⚠️;\ \text{且 mixed 族}\ \textbf{\text{已含}}\ (b,t){=}(10,0)\ ⟹ \textbf{\text{无需“转移原理”}} ✗\ (\text{前轮误判已撤销})$$
$$\textbf{(C) 我方新工具与判定}:\ \text{逐坐标构造机器（}scripts/coord\_search.py\text{）}\ \textbf{\text{实现并校准通过}}\ ✓✓\ (n{=}4{:}\ \ge4;\ n{=}5{:}\ \ge7;\ \text{正对照}(4,4),(5,7)\ \text{皆找到覆盖}) —— \textbf{\text{首次具备“非松弛下界证书”能力}} ✓;\ \text{但标度爆炸（每维}\times130\text{–}250）⟹ n{=}10\ \text{不可行} ✗$$
$$\textbf{(D) 新必要条件族（支撑层 ✓）}:\ \text{块分层引理}\ T_y\cup U_y=\mathbb F_2^m\ ⟹\ \boxed{(m{+}1)|S_y|+|U_y|\ge2^m}\ \text{（健全；真码上多处取等）};\ \text{跨层：}\delta^{(2)}\ge\delta^{(1)}_0{+}\delta^{(1)}_1\ \text{（超加性 ✓）与上界（皆零违反）}$$
$$\textbf{(E) 取等刚性（实测两码 × 六层 ✓✓）}:\ \text{取等}\Longrightarrow\boxed{S_y=\varnothing,\ |U_y|=2^m}\ (\text{不属于任何层、却与每层距离}\le1);\ \text{可证内核}=球不交\Longleftrightarrow d(\sigma,\sigma')\ge3$$
$$\textbf{(F) 诚实弱点 ✗}:\ \text{上述一切\ \textbf{\text{聚合化}} 后果皆平凡（总和式恒真或弱于球界）};\ \textbf{\text{力量只在逐点}};\ \text{“取等刚性无法全局一致”之证明属\ \textbf{\text{研究级}} ✗$$

## §2 **下一会话之入口（按信息量排序）**

$$\textbf{① 追 [130] 之 general }R{=}1\ \text{界的}\ \textbf{\text{可达替代}}:\ \text{Kéri 第 9 章／Haas 2008（皆实有）已掘尽};\ \text{候补}:\ (a)\ \text{van Lint jr.–van Wee 之 1991 工作报告};\ (b)\ \text{Kaski--Östergård 书 §7.2};\ (c)\ \text{其他 survey} ⚠️\ (\text{须先查可得性})$$
$$\textbf{② 支撑层线（本会话唯一“非已穷尽”之数学方向）}:\ \text{把}\ \delta_y\ \text{之逐点结构与}\ \textbf{\text{取等刚性}} \text{合成\ \textbf{全局一致性} 论证};\ \text{入口＝}m{=}2\ \text{时之}\ (1,1)\ \text{型为何不出现} ⚠️$$
$$\textbf{③ 上界侧（证书型）}:\ \text{119 construction（档案标 LIVE；SA/局部搜索实测太弱 ✗）};\ \text{或具名受限族精确最小值＋穷举证（悬赏 PARTIAL）} ✓$$

## §3 边界

$$\textbf{不主张}:\ 107\ \text{可复现／不可达；}\ K(10,1)\ \text{之任何新值；}\ \text{未取禁用原文（R16/R17）};\ \text{未碰 RH} ✓$$

## §4 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 非松弛下界证书  命中文件数=1    :: 本档
技术词 块分层引理     命中文件数=1    :: 本档
技术词 取等刚性     命中文件数=1    :: 本档
```

$$\textbf{分类（三项如实 ✓）}:\ \textbf{本档新增}：\text{三词皆仅本档命中（“取等刚性”另有独立档 }RESULT\text{-equality-case-rigidity，同属本会话 ✓）};\quad \textbf{档案已有（不列）}：无;\quad \textbf{通用词（不计）}：\text{“证书／引理／刚性”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$

