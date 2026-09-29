# RESULT-2026-09-29-INV1 — 逆向重建 第 1 轮：**否定**（含一次**假命中作废**）

> 空间 B｜非 C 号｜唐先生 23:27「无文献可查 ⟹ 逆向重建」｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:2x

**已查地图**：承 `RESULT-DE1`（D/E STOP）／`AUDIT-zj`／`AUDIT-29e`（单条线性 ≤105.2223）
D0: 本档对象 = **档案已有量**（μ-剖面／$A_k$／三点构型总量）之**同余律反解**（新数学对象：无 ✗）
D1: 0（产出 = **一轮否决 ＋ 一次自我更正** ⚠️✓）

---

## §0 逻辑（为何搜同余）

$$\text{(a) 定理 A}:\ \text{Aut-不变线性/谱（松弛）}\le105.2223 \Longrightarrow 107\ \textbf{必为整性/组合型}$$
$$\text{(b) 聚合 ILP（μ-剖面＋}A_k\text{＋恒等式＋整数性）于 }M{=}106\ \textbf{可行} \Longrightarrow \text{聚合层整性不足}$$
$$\text{(c) 已知**唯一独立**于聚合的一维 } =\ \text{三点构型} \Longrightarrow \text{故在"聚合＋三点总量"上搜同余律，以**排除 }M{=}106\text{" 为约束}$$

## §1 搜索设置与结果（实跑）

$$35\ \text{个真覆盖码};\ 12\ \text{个统计量}(M,S_2,S_3,A_1,A_2,A_3,\mathrm{priv},P,E,n_3,n_4,\mu_{\max});\ m\le16;\ \text{单项/二项/三项}\ \pm1\ \text{系数}$$
$$\text{零反例律仅得 } \mathbf2\ \text{条（互为等价，mod 2）}:\quad S_3+n_3-n_4\equiv0\quad(\bmod 2)$$

## §2 ⚠️ **假命中作废**（自查 ✓）

$$\text{首版判定函数**未做** }M{=}106\ \text{之可行性检验（且候选解不完整）} \Longrightarrow \text{报出的"命中 2 条 ⟹ }K\ge107\text{"}\ \textbf{作废}\ ✗✗$$

## §3 正确重判（实跑 ILP）

$$\text{聚合系统于 }M{=}106:\ \textbf{可行}\ ✓;\ \text{取到一个极简解}\quad n_1{=}882,\ n_2{=}142,\ A_1{=}0,\ A_2{=}71,\ P{=}E{=}0$$
$$\Longrightarrow\ S_3{=}n_3{=}n_4{=}0 \Longrightarrow \text{该解**满足**所检之律} \Longrightarrow \text{律**不能**排除 }M{=}106\ ✗$$
$$\boxed{\therefore\ \text{逆向重建 第 1 轮 = }\textbf{否定}:\ \text{本电池内无任何同余律能排除 }M{=}106}$$

## §4 本轮之**结构性收获**（比结果更重要）

$$\text{聚合可行集在 }M{=}106\ \text{处**极大**，含高度退化解（}\mu\le2\ \text{处处成立},\ A_1{=}0,\ A_2{=}71,\ P{=}E{=}0\text{）}$$
$$\Longrightarrow\ \text{任何候选律/约束须**同时杀掉一大片**可行点（非一处），}\ \therefore\ \text{缺失机制应是**结构定理**而非单条同余} ⚠️✓$$

## §5 下一轮（明确、可执行）

$$\textbf{(i)}\ \text{统计量下沉到 **三点构型之 orbit 联合分布**（即档案 }RESULT\text{-}29o/29p\ \text{所证独立的那一维}\ \text{rank increment }13\text{）}$$
$$\textbf{(ii)}\ \text{系数域扩到 }|c|\le2、m\le32;\ \text{并加"杀一片"判据（须排除 }M{=}106\ \text{之**全部**整数可行剖面）}$$
$$\textbf{(iii)}\ \text{若再无律，则把搜索域改为 **构型蕴含**（不是同余），并按 }N1/N2/N3\ \text{三条件筛}$$

## §6 边界（硬 ✓）

- **不主张** 107／任何新值；**假命中已明示作废** ✓（自检纪律）
- 未取论文原文（R16–17）；未扩样本至无目标 ✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
