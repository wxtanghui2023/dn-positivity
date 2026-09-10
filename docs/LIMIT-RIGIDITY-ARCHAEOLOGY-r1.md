# LIMIT-RIGIDITY ARCHAEOLOGY 第一轮（三站模板考古）

**日期**：2026-09-10 16:56+ ｜ 依据：唐先生「不要先发明机制，先找已存在的同类定理」｜ 预算：纸面 + 文献核验
**第一轮纪律**：**只做** `Theorem → Hypotheses → 哪条假设阻止 moving-edge`；**不把模板搬进数论**（末节只留一个问题）

---

# 0. 方向登记（唐先生）

$$\boxed{\text{不要先发明机制；先寻找「机制已经存在」的同类定理}}$$
把上一轮 (a)(b) 合并为**一个**新任务：
$$\boxed{\textbf{LIMIT-RIGIDITY ARCHAEOLOGY}}:\ \text{finite/local control}\to\text{limit objects}\to\text{uniform nondegeneracy}\to\text{global rigidity}$$
**要找的四种结构**：① uniform coercivity｜② uniform invertibility｜③ compactness + nondegenerate limit｜④ critical degeneration with conserved balance
**同时登记 P0/P1/P2 三分法**：
```
P0 有限正性：Q_X≥0（已知太多；允许 inf Q_X→0 ⟹ 不能传 rigidity）
P1 统一正性：Q_X ≥ c‖f‖²（c 与 X 无关）⟹ 阻止 moving-edge 完全塌零
P2 临界退化但可控（**最有希望**）：Q_X ≥ cX^{−β}I 且第二量 R_X ≍ X^{−γ}
   ⟹ rigidity 来自二者平衡；若 primitive law 强迫 β+γ=1，配合外部 Φ(β,γ)=0
   ⟹ 唯一解 (β,γ)=(½,½)    —— 这〔不是〕H=X/H 式预设
```

---

# 站 1：Limit operator / finite-section / stability-at-infinity

## 1.1 定理与演进（文献级）
**经典形式**（Rabinovich–Roch–Silbermann 体系）：
$$A\ \text{(band-dominated)}\ \text{Fredholm}\iff\text{所有 limit operators 可逆【且其逆一致有界}$$
**⭐ 关键演进**：`一致有界` 这一条后来被证明是**自动的**——
* 1998 年综述明言："直到几年前，主定理还是写成……且逆一致有界"
* JFA 2014《An affirmative answer to a core issue on limit operators》：rich band-dominated 的 P-Fredholm 判据
* arXiv:1801.08442 直接写成：**band-dominated operator is Fredholm iff all of its limit operators are invertible**（无一致性附条）
⟹ **uniformity 是被【推导】出来的，不是被假设的**

## 1.2 定理骨架
```
① 局部结构（band-domination ⟹ 有限传播/局域性）⟹ 局部模型能穷尽信息
② 沿"走向无穷"的序列取 *-强极限 ⟹ 得到【limit operators 族】（operator spectrum）
③ 该族【紧】且参数化【连续】
④ 每个极限对象非退化（可逆）
⟹ ⑤ 一致非退化下界（逆一致有界）——【自动】
⟹ ⑥ 全局刚性（Fredholm / 指标）
```
## 1.3 不可替代的假设（本轮要抽的东西）
$$\boxed{\text{极限对象族的【紧性】+ 参数化的【连续性】}\ \Longrightarrow\ \text{uniformity}}$$
**这才是阻止 moving-edge 的那条假设**：不是"外加一致 gap"，而是"极限族不能跑到无穷远"。

---

# 站 2：正二次型的单调极限（B. Simon, JFA 28 (1978) 377–385）

## 2.1 定理（文献级，原文摘要）
> 对**任意正二次型**有**典范分解** $h=h_r+h_s$，其中 $h_r$ 刻画为**小于 $h$ 的最大可闭形式**；并给出单调收敛定理，且讨论非稠定形式。
（作者 B. Simon，1978，JFA 28(3)）

## 2.2 定理骨架
```
① 有限层次只有正性 Q_n ≥ 0（P0！）
② 取单调极限 ⟹ 可能出现【奇异部分 h_s】（正性"形式上"留下但失去可闭性）
③ 防退化的机制 = 消除/控制奇异部分（h_s = 0，或可闭性统一）
⟹ ④ 单调收敛（Fatou 型）成立
```
$$\boxed{\text{防退化条件 = 【奇异部分不积累】}\ \text{（等价于某类统一可闭性）}}$$
**⟹ 这正是我们 P0→P1 的形式化原型**：P0 允许 $h_s\neq0$（=moving edge），P1 = $h_s=0$ 类的统一版本。

---

# 站 3：最终正算子半群（Arora–Glück, Semigroup Forum 103 (2021) 791–811）

## 3.1 结果（文献级）
* 个别最终正 + **轨道相对紧** + **点谱∩虚轴有界** ⟹ 强收敛到 equilibrium
* 均匀最终正 + 持续不可约 ⟹ 谱界主导（dominance）的充分条件族
* **Positivity 本身不最终控制**：需谱 + 紧性共同决定长期行为
* 主要障碍：把（正半群的）谱结果推广到最终正时，**cyclicity 结果失效**

## 3.2 定理骨架
```
① 有限层次：positivity / eventual positivity（比 station 2 更弱）
② 长期极限（t→∞）：可能失去 equilibrium
③ 防退化 = 【轨道紧性】+【谱条件（虚轴不逼近 / 主导性）】
④ 障碍 = cyclicity 类结构在弱化正性时【丢失】
```
$$\boxed{\text{防退化条件 = 轨道紧性 + 谱不逼近临界轴}}$$
**⟹ 与我们"谱中心化（FE）"的死亡模式对照**：那里恰好是"谱逼近虚轴"未被排除。

---

# 4. ⭐ 矩阵（唐先生指定的输出格式）

| 已存在定理 | 有限性质 | 极限机制 | **防止什么退化** | 临界量如何产生 |
|---|---|---|---|---|
| Limit operators（RRS / JFA2014 / arXiv:1801.08442） | finite sections + band-domination（局域性） | 沿走向无穷序列取 *-强极限 ⟹ limit operators 族 | **逆的爆炸**（= 统一下界丢失） | 极限对象的**逆**（一致界），且一致性由**紧性+连续参数化**推出 |
| 正二次型典范分解（Simon 1978） | $Q_n\ge0$（P0 级） | 单调极限；$h=h_r+h_s$ | **奇异部分积累**（可闭性丢失） | $h_r$ = **小于 h 的最大可闭形式**（正则半径） |
| 最终正半群（Arora–Glück 2021） | positivity / eventual positivity | $t\to\infty$ 轨道 | **平衡丧失 + cyclicity 失效** | 谱界**主导性** + **轨道相对紧** |

# 5. ⭐⭐ 三站共同骨架（本轮的抽取）

$$\boxed{\text{finite/local control}\ \longrightarrow\ \text{极限对象族}\ \longrightarrow\ \underbrace{\text{族紧 + 参数连续 + 逐个非退化}}_{\text{防退化}}\ \longrightarrow\ \text{一致下界（自动）}\ \longrightarrow\ \text{全局刚性}}$$
**⭐ 最重要的一条结构性收获（会改变我们的框架）**：
$$\boxed{\text{uniformity 不是要我们【外加】的部件；它由【极限族的紧性】推出}}$$
**⟹ 我们此前把它写成"缺 dissipation / 缺统一正性"（P1）是**把结论当条件**。
**正确的待找物是**：$\boxed{\text{一个【紧】的算术极限对象族 + 连续参数化}}$
**⟹ 并立刻解释了我们历次 moving-edge 失败**：那些族**非紧**（边缘逃到无穷）——恰好是站 1/2/3 假设所排除的失败模式 ✓

# 6. P2 与 β=γ=½ 的位置（登记，不构造）
$$\text{P2}:\ Q_X\ge cX^{-\beta}I,\quad R_X\asymp X^{-\gamma};\quad \text{需两方程}\ \Phi(\beta,\gamma)=0\ (\text{外部极限定理}),\ \Psi(\beta,\gamma)=0\ (\text{arithmetic 相容性})$$
**模板对应**（结构性类比）：站 2 的 $h_r+h_s$ 与站 1 的"算子 / 逆"都提供**成对退化指数**的双对偶结构；
P2 的"守恒平衡"在模板中的对应物是**【对偶配对】**（正则/奇异、算子/逆）。⟹ P2 不是新发明的形态，而是模板的自然形态 ✓

# 7. ⭐ 末节：唯一留给 arithmetic 的问题（本轮**不**回答）
$$\boxed{\text{四种防退化条件中，哪一种【素数算术】天然可能提供？}}$$
候选（**均未研究**，仅列出以便下一轮）：
```
① 紧性：算术自然的紧族多为 profinite/adelic（0 维）——与我们的非紧尺度族结构不同
② 一致可逆性：需要算术对象上的范数结构；乘法 Haar 测度确实给出 L² 结构，且逆不变
③ 紧 + 非退化极限：?（未识别）
④ 临界退化 + 守恒平衡：P2 形态（β+γ=1）
```
**按唐先生纪律：本轮到此为止，不搬进数论。**

# 8. 诚实边界
```
· 第 0 节的 redefinition、四结构、P0/P1/P2、β+γ=1 构造原理、"本轮只做 Theorem→Hypotheses"、"末节才提问" —— 均为唐先生本轮
· 站 1/2/3 的定理陈述为【文献级】（站点 1：RRS 体系 + JFA 2014 + arXiv:1801.08442；
  站 2：B. Simon, JFA 28(3) 1978, 377–385，原文摘要核验；站 3：Arora–Glück, Semigroup Forum 103 (2021) 791–811，arXiv:2011.04296）
· "uniformity 自动"依据 arXiv:1801.08442 的无附条表述 + 1998 综述的历史陈述 ⟹ 文献级，**我未读全文证明**
· 站 2 的"防退化 = 奇异部分不积累"、站 3 的"防退化 = 轨道紧 + 谱不逼近"为【结构性归纳】
· §5 的共同骨架与"uniformity 由紧性推出 ⟹ 我们此前把结论当条件"为【结构性论证】，非定理；
  §5 末句"我们的族非紧"是对既有 moving-edge 登记的【结构性解释】
· §6 的模板对应为【结构性类比】；§7 全部为未研究问题
· 未写代码、未做数值；本轮使用文献（web 检索）；未使用 Λ；未引入 ζ 零点或谱算子
```

## 提交链
```
12d7627 ISRG 原型轮 → 本篇（LIMIT-RIGIDITY ARCHAEOLOGY r1）
```
