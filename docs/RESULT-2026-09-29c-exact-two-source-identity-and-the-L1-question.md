# RESULT-c（2026-09-29）—— **精确两来源恒等式 $\mathrm{Def}=2(A_1+A_2)-\sum\tbinom{\mu-1}2$（$60/60$）＋ $L_1$ 问题的正确形式**

> **性质**：**问题特化续**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:05 ✓

**已查地图**：`RESULT-b`（母式 $40/40$）／`RESULT-2026-09-29`（$[47,59]$）／`AUDIT-29ze` ✓

D0: 本档对象 ＝ **档案已有**（双重计数／$A_1{+}A_2$—经典 ✓）
D1: 0（产出＝**一精确恒等式 ＋ 一条被否构造 ＋ 一数据** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 精确恒等式}:\ \mathrm{Def}(A)=2(A_1+A_2)-\sum_x\tbinom{\mu(x)-1}{2}\ (\text{实测 }60/60)}$$
$$\boxed{\text{② 含义}:\ \mathrm{Def}\ \text{有两个来源};\ \text{母式只算了第一个（撞 }P\text{）}✗}$$
$$\boxed{\text{③ 数据}:\ \text{真 }53\text{-子集: }A_1{=}5,A_2{=}50\Rightarrow2(A_1{+}A_2){=}110,T{=}28,\mathrm{Def}{=}\mathbf{82}\ >\ 71\ (\text{纤维允许上限})✓}$$
$$\boxed{\text{④ ✗ 构造失败}:\ L_1\ \text{含 packing 点自身（}m_P(p){=}1\ \text{平凡）}⟹\ \text{须问\ \textbf{非 packing} 的私有点}}$$

## §1 精确恒等式（✓✓ 自测）

$$\sum_x\tbinom{\mu(x)}2=2(A_1+A_2)\ (\text{已核实})\ \text{且}\ \tbinom{\mu}2=(\mu-1)+\tbinom{\mu-1}2$$
$$\therefore\ \boxed{\mathrm{Def}(A)=\sum_x(\mu(x)-1)=2(A_1+A_2)-\sum_x\tbinom{\mu(x)-1}{2}}\ ✓✓$$
$$\textbf{两来源}:\ \text{（i）近邻码字对数 }A_1{+}A_2;\ \text{（ii）三重以上覆盖修正 }T:=\sum\tbinom{\mu-1}2$$

## §2 母式之定位（✓ 说明为何弱）

$$\text{母式}:\ \mathrm{Def}\ \ge\ 2\sum_{c\in A\setminus P}m(c)\ ——\ \text{只记录"额外中心撞 }P"\ \text{之贡献}✗$$
$$\textbf{遗漏}:\ A\setminus P\ \text{之间互相撞击之贡献（即 }T\ \text{与 }A\setminus P\ \text{内部对数）}⟹\ \text{低重区集中时母式失效}⚠️$$
$$\therefore\ \boxed{\text{正确工具 ＝ \S1 恒等式（两来源同时计）},\ \text{而非继续强化母式}}$$

## §3 数据（✓ 有信息量）

$$62\text{-码之随机 }53\text{-子集}:\ A_1{=}5,\ A_2{=}50\ \Longrightarrow\ 2(A_1{+}A_2){=}110;\ T{=}28;\ \mathbf{Def{=}82}$$
$$\text{纤维允许上限}:\ 9\cdot53-406=\mathbf{71}\ \Longrightarrow\ 82>71\ ✗$$
$$\therefore\ \boxed{\text{真实"稠密"构型之 }\mathrm{Def}\ \text{超出纤维允许值}⟹\ \text{纤维条件\ \textbf{确有约束力}}✓\ (\text{启示性，非证明})}$$

## §4 ✗ 一条被否构造（诚实记录）

$$\text{拟构造}:\ A=P\cup(L_1\ \text{之点})\ \text{以压 }2\sum m\ \text{至最小}$$
$$\textbf{实测}:\ L_1\ \text{含 packing 元素自身}\ (m_P(p)=1\ \text{平凡})⟹\ \text{并集塌缩},\ \mathrm{Def}{=}0\ ✗\ \text{构造无意义}$$
$$\therefore\ \text{正确问题}:\ \#\{x\notin P:\ m_P(x)=1\}\ \text{之容量（\textbf{非 packing} 私有点）}✓$$

## §5 下一目标（修正版）

$$\therefore\ \text{须证}:\ 2(A_1+A_2)-T\ >\ 9a-406\ \text{对某 }a\ \text{成立，或互补对上总有一侧成立}$$
$$\text{工具}:\ \S1\ \text{恒等式}:\ \mathrm{Def}=2(A_1+A_2)-T;\quad \text{纤维条件}:\ \mathrm{Def}\le9a-406$$
$$\therefore\ \text{须证}:\ 2(A_1+A_2)-T\ >\ 9a-406\ \text{对某些 }a\ \text{必成立（或互补对上必成立）}$$

## §6 边界（硬 ✓）

- **恒等式自测 $60/60$** ✓；**数据（$53$-子集）实测** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本档含**一条被否构造**（诚实记录）✓
