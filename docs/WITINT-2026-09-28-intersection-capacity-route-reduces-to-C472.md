# WITINT-2026-09-28 — **② 审计：$|N(C_0)\cap N(C_1)|$ 容量路线\ \textbf{归约到 C-472 同一不等式}（✗ 非新方向）；$h$ 依赖被抵消；朴素容量界不碰撞**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:34 令 ✓）**：② 之共同邻域容量审计；**有限穷举/随机抽样** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-474／C-472／C-470，非新案 ✓）**
`docs/WITTHM-2026-09-28-…`（**Thm 2.5／4.9 抽取／$n{=}10$ 读数 ✓✓✓**）｜`docs/WITPOBJ-2026-09-28-…`（**单调下界障碍 ✓✓✓**）｜`docs/WITUOBJ-2026-09-28-…`（**$|X_L|\le2q$／$9|H|{+}2q$ 恒等式 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** 邻域／$q$／$H$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次证明 $N(C_0)\cap N(C_1)\subseteq N(H)\cup\{\text{距离-2 对之共同邻}\}$ ⟹ $|\cap|\le9h{+}2q$，从而 ② \textbf{归约到 C-472 同一不等式} ＋ 首次给出随机抽样数据（$|\cap|\approx222{\sim}258$ vs 需求 $\approx400$）＋ 首次证否朴素容量界之碰撞可能（$531>450$）** ✓）
**[RESEARCH]**

---

## §0 结论（**② 归约 ✗｜朴素界不碰撞 ✗｜数据 ✓**）

$$\boxed{\textbf{(1) ✗✗② 之容量路线归约到 C-472 同一不等式}:\ }\text{设 }x\in N(C_0)\cap N(C_1)\ \big(\text{开邻域 ✓}\big)\Longrightarrow\exists\,u\in C_0\cap N(x),\ v\in C_1\cap N(x)✓$$
$$\qquad d(u,v)\in\{0,2\}✓\ \big(\text{两者皆 }x\ \text{之邻 ✓}\big)\Longrightarrow\ \text{二分}:\ \text{(a)}\ d{=}0\ \big(u{=}v\in H\big)\Longrightarrow x\in N(H)✓;\quad\text{(b)}\ d{=}2\Longrightarrow x\ \text{为该对之共同邻 ✓}$$
$$\qquad\Longrightarrow\ \boxed{N(C_0)\cap N(C_1)\ \subseteq\ N(H)\ \cup\ \{\text{距离-2 对之共同邻}\}}\ ✓✓\ \big(\text{＝}\text{C-470 之分解 ✓，本档补证 ✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{\big|N(C_0)\cap N(C_1)\big|\ \le\ 9h\ +\ 2q}\ ✓✓\ \Big(h{=}|H|,\ q{=}\#\{(u,v)\in C_0{\times}C_1:d(u,v){=}2\}✓\Big)$$
$$\qquad\Longrightarrow\ \text{覆盖需求 }|\cap|\ge|P^c|{=}393+h\ \text{化为}\ \boxed{2q\ \ge\ 393-8h\ =\ 8s-559}\ ✓✓\ \big(s{=}|P|✓\big)$$
$$\qquad\Longrightarrow\ \boxed{\text{② 与 C-470／C-471／C-472 是\ \textbf{同一对象}（同一不等式之两种写法）}\Longrightarrow\ \textbf{非新信息方向}\ ✗✗}$$
$$\boxed{\textbf{(2) ✗朴素容量界不能产生碰撞}:\ }\text{平凡 }|\cap|\le\min(9a,9b)\le9\times59=\mathbf{531}✓\quad\text{vs 需求}\ |P^c|\le393+57=\mathbf{450}✓$$
$$\qquad 531>\mathbf{450}\Longrightarrow\ \boxed{\text{平凡容量界\ \textbf{不}排除碰撞}}\ ✗\ \big(\text{唐先生之 P1"\ 证 }|\cap|<393+h\text{"\ 无平凡证法 ✓}\big)$$
$$\boxed{\textbf{(3) ✓✓新数据（本档随机抽样）}:\ }(|C_0|,|C_1|){=}(60,59)\ \text{之随机对（5 次 ✓）}:$$
| 量 | 观测 |
|---|---|
| $\|N(C_0)\|$ | $343{\sim}355$ |
| $\|N(C_1)\|$ | $327{\sim}355$ |
| $\mathbf{\|\cap\|}$ | $\mathbf{222{\sim}258}$ |
| $h$ | $7{\sim}13$ |
| $\|P\|$ | $106{\sim}112$（$\ge62$ ✓） |
| 需求 $\|P^c\|$ | $400{\sim}406$ |
| 满足？ | **皆不满足** ✗（约 240 vs 400 ✓） |
$$\qquad\Longrightarrow\ \text{覆盖条件是\ \textbf{强}条件（随机对差得远 ✓）}\Longrightarrow\ \text{② 之问"}\cap\ \text{能否}\ge393+h\text{"\ \textbf{真开放}但难 ✗}$$
$$\qquad\textbf{（自纠 ✓）}:\ \text{本人先前猜测"generic 对给 }\cap\approx500\text{"}\ \textbf{错}✗\ \text{—— 实测 }\approx240✓\ \big(\text{幸而算实 ✓}\big)$$

---

## §1 $h$ 之双重作用为何不产生新杠杆（**✓✓ 算术抵消**）

$$\textbf{唐先生之观察 ✓✓}:\ H\uparrow\Longrightarrow P^c\downarrow\ \text{但需求}\uparrow\ \big(|P^c|{=}393+h✓\big);\quad\text{且 }H\subset C_0,C_1\ \text{强制共同邻域 ✓}$$
$$\qquad\textbf{但 ✓✓}:\ \text{容量侧亦随 }h\ \text{增长（}9h\ \text{项 ✓）}\Longrightarrow\ \text{不等式}\ 393+h\le9h+2q\iff393\le8h+2q✓$$
$$\qquad\Longrightarrow\ h\ \textbf{越大越宽松}✓\ \big(\text{容量增速 }9>1\big)\Longrightarrow\ \boxed{\text{最紧端＝}h\ \textbf{最小}}\ \big(h{=}0\iff s{=}119✓\big)\ \text{—— 与 C-472 之表完全一致 ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{h\ \text{不是新自由度};\ \text{两端}\ (h{=}0,\ s{=}119)\ \text{即全部压力}\ ✓}$$

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生之 }|P^c|{=}393+h\ \big(|P|{=}119-h✓\big)\ \text{正确};\ \text{两者共覆盖同一 }P^c\ \text{之提法正确};\ |\cap|{=}|N(C_0)|{+}|N(C_1)|{-}|\cup|\ \text{恒等式正确}✓$$
$$\textbf{✓✓}:\ \text{"刻意找\ \textbf{不依赖 }A_0\ \text{之全局结构"}\ ✓✓\ \text{方向正确（Type II 只触 41/119 ✓ C-473）}\ \text{—— 但 ② 恰好又落回同一不等式 ✗}}$$
$$\textbf{✗✗}:\ \text{"}|\cap|\ \textbf{之全局上界}"\ \text{与 }q\ \text{之上界\ \textbf{等价}（}9h{+}2q\ \text{界 ✓）}\Longrightarrow\ \text{与 C-472 同障 ✗}$$
$$\textbf{⚠️}:\ \text{唐先生 }P_0\ \text{"精确化 }N(C)\ \text{容量函数"}\ ✓\ \text{—— 但可用的只有 }|N(C)|\le9|C|\ ✓\ \text{（达界需 min-dist}\ge3✓\ \text{而 }A(9,3){=}40✗\big)\Longrightarrow\ \text{对 }|C|{=}60\ \text{只有粗界 ✓}$$

## §3 现状与建议（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }|\cap|\le9h{+}2q✓✓\ \text{（本档）};\ \text{② ② ⟺ C-472 不等式 ✓};\ \text{③ 朴素界 }531>450\ \text{不碰撞 ✓};\ \text{④ 随机对 }\cap\approx240\ll400✓;\ \text{⑤ }h\ \text{非新自由度 ✓};\ \text{⑥ ① 之 }n{=}10\ \text{读数 }105.2223\ll120✗;\ \text{⑦ Type I KILLED ✓✓✓};\ \text{⑧ Type III rigid-but-inert ✓}$$
$$\textbf{未确立 ⚠️}:\ q\ \text{之任何非平凡上界（＝① 之缺口、② 之缺口、C-472 之缺口 —— \textbf{三者同一}}✓\big);\ a{=}45\ \text{的排除};\ M\ \text{之真值}$$
$$\textbf{（建议之可选方向 ✓ 登记，不作裁定 ✗）}:\ \text{(a) 接受"三条路线同归一个缺口"，转去\ \textbf{换问题}（如 119 之其他等价形）};\ \text{(b) 找\ \textbf{真正新类型}之上界输入（等周/谱/距离分布 —— 但文献 SDP 已达 105.2 < 107 < 120 ✗）};\ \text{(c) 暂挂本线，转他线 ✓}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "共同邻域容量" "等价归约" "交集容量"
技术词 共同邻域容量 命中文件数=0    ::
技术词 等价归约     命中文件数=1    :: ./ASSETS-REGISTRY.md
技术词 交集容量     命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 共同邻域容量 | 0 | 0 | ✓（自造标签 ✓） |
| 等价归约 | **1**（`ASSETS-REGISTRY.md` ⟹ **本线既有 ⟹ 不计** ✗） | 0 | ✗（**非新增** ✓） |
| 交集容量 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §5 边界（硬 ✓）

- **有限穷举＋随机抽样** ✓（5+1 组 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处归约**（② ⟺ C-472 ✓）＋ **一处自纠**（generic $\cap$ 猜测 ✗）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a{=}45$ 已排除 ✗（V290）；**不声称** ② 已死 ✗（仅记其为同一对象 ✓）
