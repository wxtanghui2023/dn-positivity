已查地图：已跑 scripts/prework_map_check.sh 全局不变量 tightness slack 局部禁形 分离性 ⟹ 总命中 10 处（CLOSED-ROUTES-MAP 6 ／ MASTER-STATUS-AND-CLOSURES 3 ／ ASSETS-REGISTRY 1）。逐条判定：**本档为战略/方法论层梳理，引用既有条目，不开新研究方向**；所涉 d=4 三层 NO-GO 已按死因登记于本档同日新增的 CLOSED-ROUTES-MAP §D4-LANE-A（含 10 条 D4-* 条目）；RH 侧 interface 条款对应既有 V236/V278/V187 三族结论（已登记）。
D0: 本档对象 = 档案已有对象的**关系层梳理**（跨线方法论），非新对象、非已知 RH 对象重命名
D1: 0（本档无新独立自由度；产出为战略判断与 I(D) 计划的立项建议）

# STRATEGY-2026-09-25 · 两条线的共同缺口：**全局不变量（换状态变量）**

**来源**：唐先生 2026-09-25 22:49 战略判断（本日最重要结论）
**关联**：`docs/B1b-owner-structure-engine-and-results-d1-d4.md` §38F（d=4 收口）｜RH 线（space A）

---

## §1 判断（不绕弯）

以「得到一个新的、可证明的**结构定理**」为攻击成功的标准：

```
RH          : 未攻下
d=4 packing : 未攻下
```

但这**不是**「技术不够」。真正的问题是**层级**问题。

---

## §2 技术栈的能力边界（本日反推结论）

我们反复使用的手段：穷举／SAT／packing-covering／Hamming 码结构／extremal combinatorics／
owner-private 分配／容量鸽笼／对称性分解／参数化／一阶展开／非线性泛函／Fourier-谱-trace／
显式公式／零点统计／算术局部化／bridge-interface 构造。

它们绝大多数最终落在**两个能力范围**内：

$$
\boxed{\text{(i) 有限/局部约束}}\qquad\text{或}\qquad\boxed{\text{(ii) 把已有对象重组为另一种表示}}
$$

而两个目标问题要求的都是**第三种东西**：

$$
\boxed{\text{发现一个目前尚未进入模型的\textbf{全局不变量}}}
$$

---

## §3 RH 的真实缺口

反复出现的同一现象：找到一个量 $Q$，它能测某种零点结构，但最终只看到

$$\gamma,\ |\gamma|,\ \text{multiplicity},\ \text{statistics}$$

而没有真正看到所需的 **prime/arithmetic information**；或反过来：做出了 arithmetic object，
却无法证明它对所有零点产生**全局谱约束**。

```
缺的是:   arithmetic data  →  global spectral obstruction
而不是:   又一个更漂亮的 kernel
```

**判据（今后准入）**：RH 下一步候选必须满足

$$
\boxed{\text{它改变了「算术信息如何进入零点谱」的方式}}
$$

否则一律视为旧路线的新包装（新 kernel／新权函数／新 trace／新谱量／新零点统计量均不例外）。

---

## §4 d=4 packing 的真实缺口（同构）

今日已把该线压到干净状态，并逐层否证三类局部机制：

| 层级 | 原候选机制 | 检验结果 | 状态 |
|---|---|---|---|
| code geometry | private point + distance-3 禁形 | 3655/5472 反例 | NO-GO |
| owner layer | owner 容量鸽笼 | 容量矛盾不存在（97%/93%/88% 装得进 D） | NO-GO |
| D structure | $A_j=A_k=\varnothing$ | 2307/9576 非空（24.09%） | NO-GO |
| tight-instance empirical | separation ≥4 | 紧型稳定 | **仅经验事实** |
| finite exhaustive | 8.2M 全量枚举 | zero failure | **保留（证书）** |

剩下的问题层级已经不同：

$$
\boxed{\textbf{tight instance 为什么 tight？}}
\qquad\text{而不是}\qquad
\text{某一个局部点为什么不能出现？}
$$

---

## §5 战略变化（本日核心建议）

不再问「为什么第五个点放不进去」，而问：

$$
\boxed{\text{一个达到极限容量的系统，相对于任意非 tight 系统，多出了什么\textbf{全局守恒量}？}}
$$

已知 $d(q,x_i)\ge4$、$A_j=A_k=\varnothing$、owner capacity **单独都不是**一般律，
但它们在 tight instance **同时**出现 ⟹ 真正可能存在的不是单个条件 $P_1,P_2,P_3$，而是**联合饱和关系**：

$$
\boxed{P_1+P_2+P_3=\text{capacity identity}}\quad\text{或更抽象}\quad\boxed{\text{slack}(D)=0\ \Longrightarrow\ \text{全局守恒律}}
$$

**关键区别**：不再证明某局部构型「不可能」，而是找**所有局部构型的总 slack 是否被一个全局恒等式锁死**。
这正好绕开今日已关闭的三层。

---

## §6 具体可执行路线（I(D) 计划）

已有现成实验材料：

```
tight   : 138/138
general : 2307/9576
```

**第一步**：把 tight 与 non-tight 并列，寻找量 $I(D)$ 使

$$I(D)\ \ge\ 0,\qquad I(D)=0\ \text{在 tight cases 全部成立（一般 cases 出现正 slack）}$$

**第二步**（之后才做）：$I(D)=0\ \Longrightarrow\ \alpha_2=|D|$。

这是**不同层级**的攻击：目标不是新的局部禁形，而是**总 slack 的全局恒等式**。

**禁止重走**（今日已获得的信息）：
- ✗ 新的 distance-3 private-point 禁形
- ✗ 新的 owner pigeonhole
- ✗ $A_j=A_k=\varnothing$ 的普遍化
- ✗ 从一般 $D$-structure 重推 separation
- ✗ 对已否证机制换符号重写

**若重启该题**：从 **tightness/saturation 本身**出发，而不是回到 private-point／owner／distance-3 三层。

---

## §7 共同母题

```
RH:   缺 arithmetic → spectrum 的**新 interface**
d=4:  缺 tightness → global invariant 的**新 interface**
```

$$
\boxed{\text{真正的突破可能不是更强的局部工具，而是\textbf{换「状态变量」}}}
$$

这比「再试一种技术」更值得下一轮认真做。

---

## §8 落档纪律

- 本判断为**方法论级**，跨两线适用；提请（不擅自）在 `RESEARCH-CONSTITUTION.md` 立项为 AMEND（新候选的 interface 准入条款）。
- 与 `CLOSED-ROUTES-MAP.md` 的关系：d=4 的 10 条 NO-GO 已按其「死因」类别登记（见该档 §D4-LANE-A）。
