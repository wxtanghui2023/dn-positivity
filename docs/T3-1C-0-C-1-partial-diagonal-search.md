# T3-1C-0 ＋ T3-1C-1 · **BC 增益的抽象 ＋ partial diagonal 搜索**

> 依唐先生 2026-09-17 09:37 指令｜**第一轮不算指数**，只答 C1–C4 ✓
> 材料：BC 全文（`docs/ref-bc-ar5iv-plaintext.txt`，(4.9)–(4.29) 已逐字在手）✓

---

# T3-1C-0 · **BC 的 diagonal 为什么能被保留？**（抽象）

## 1. ⭐⭐⭐ C--S 的**重复结构**（先钉死对象）

$$\text{标准结构}：\text{C--S 施于变量集}\ T\ \text{时}\ \textbf{重复} \text{其补集}\ S：\ \Big|\sum_T K\Big|^2=\sum_{T,T'}K(T)\overline{K(T')}\ \text{（}\text{被重复者＝}S\text{）}✓$$
$$\text{BC (§4.1.2 逐字)}：\text{C--S 施于}\ T=\{n_1,n_2,a_2,p_1,p_2,q_1,q_2,c\} \Longrightarrow \textbf{重复}\ S=\{d,a_1,\ell_1,\ell_2\}✓✓$$
$$\qquad\Longrightarrow\ \text{(4.10) 中出现}\ d,d'；a_1,a_1'；\ell_1,\ell_1'；\ell_2,\ell_2'\ \textbf{——四对}✓✓✓$$
$$\text{DFI (对比，逐字)}：\text{C--S 施于除}\ \{\ell_1,\ell_2\}\ \text{外全部} \Longrightarrow \textbf{只重复}\ \{\ell_1,\ell_2\}✓$$

$$\boxed{\textbf{"longer diagonal" 的精确含义}＝\text{被重复集从}\ \{\ell_1,\ell_2\}\ \textbf{扩大} \text{到}\ \{d,a_1,\ell_1,\ell_2\}}✓✓✓$$

## 2. BC 的 diagonal 与 off-diagonal（精确定义）

$$x：＝(d,a_1,\ell_1,\ell_2),\qquad x'：＝(d',a_1',\ell_1',\ell_2')✓$$
$$\textbf{full diagonal}：x=x'（\text{四对全同}）✓\qquad\text{由 (4.10) 的条件}\ \textbf{显式安排}：$$
$$\qquad a_1\ne a_1'\Rightarrow(d,\ell_1,\ell_2)\ne(d',\ell_1',\ell_2')\quad\Longleftrightarrow\quad (d,\ell_1,\ell_2)=(d',\ell_1',\ell_2')\Rightarrow a_1=a_1'✓✓$$
$$\textbf{近对角}：\mathcal V^*＝\{d=d',\ell_1=\ell_1',\ell_2=\ell_2',a_1\ne a_1'\}\ \text{（§4.1.3.1 单独处理）}✓$$
$$\textbf{其余}：\mathcal V\ \text{由}\ \Delta=0/\Delta\ne0\ \text{分拆}＋u：＝(\tilde\ell_2'd-\tilde\ell_2d',b\mathfrak q_1\mathfrak p_2)\ \text{控制}✓$$

## 3. ⚠️ **精度点**（搜索前必须钉死，否则找错对象）

$$\text{唐先生消息中的示意式}\ \Delta=d\ell_1\ell_2-d'\ell_1'\ell_2'\ \textbf{并非} \text{BC 的实际}\ \Delta✓$$
$$\text{BC (4.19) 逐字}：\ \boxed{\Delta：＝a_2(d\tilde\ell_1'-d'\tilde\ell_1)\tilde\ell_2\tilde\ell_2'\mathfrak p_2-(da_1\tilde\ell_2'-d'a_1'\tilde\ell_2)\tilde\ell_1\tilde\ell_1'\mathfrak q_1}✓✓$$
$$\Longrightarrow\ \textbf{搜索必须用实际 }\Delta✓\quad(\text{两者不是同一对象：前者是}\ \textbf{单项乘积差}，\text{后者是}\ \textbf{两个交叉项之差})✓$$

---

# T3-1C-1 · **partial diagonal 搜索**（先答 C1–C4，不算指数）

## 4. 目标（严格定义）

$$\text{找}\ x\sim x'\ \text{的中间等价关系}：\ \boxed{x=x'\Rightarrow x\sim x'，\ \text{但}\ x\sim x'\not\Rightarrow x=x'}✓$$
$$\qquad\text{且}\ \boxed{\text{同一}\ \sim\text{-fiber 内仍存在可利用的振荡／正交性}}✓$$
$$\text{流程改写}：\text{C--S}\to\text{full diagonal}\quad\Longrightarrow\quad \boxed{\text{算术预聚类}\to\text{partial diagonal}\to\text{C--S}\to\text{second-stage cancellation}}✓$$

## 5. ⭐⭐⭐ 第一项检查：$(d,\tilde\ell_2)$ 与 $(d',\tilde\ell_2')$ 之间**可用的联合算术关系**

$$\text{穷举该处}\ \textbf{所有已知约束}（\text{逐字核过}）✓$$
$$\text{(i)}\ \text{互素}：\ (d,\tilde\ell_1\tilde\ell_2)=(d',\tilde\ell_1'\tilde\ell_2')=1\ \text{（L403 逐字）}\ \Longrightarrow \textbf{已用尽}（\text{最大化}）✗$$
$$\text{(ii)}\ \text{行列式}：\ \tilde\ell_2'd-\tilde\ell_2d'\ \Longrightarrow\ \textbf{BC 已用}：u：＝(\tilde\ell_2'd-\tilde\ell_2d',b\mathfrak q_1\mathfrak p_2)，v：＝(\tilde\ell_2'd-\tilde\ell_2d')/u✓$$
$$\text{(iii)}\ \text{交叉差}：\ \Delta\ \text{（上文 §3 实际式）}\ \Longrightarrow\ \textbf{BC 已用}（\Delta=0/\ne0\ \text{分拆}）✓$$
$$\text{(iv)}\ \text{同余 (4.26)}：\ \tilde\ell_2'd\equiv\tilde\ell_2d'\ (\mathrm{mod}\ u)\ \Longrightarrow\ \text{即 (ii) 的推论}✓$$

$$\Longrightarrow\ \boxed{\text{该处可用的联合算术关系}\ \textbf{只有行列式}；\ \text{它已被}\ u,v,\Delta\ \textbf{完全消耗}}✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{任何建立在}\ (d,\tilde\ell_2)\text{-}(d',\tilde\ell_2')\ \text{上的 partial diagonal}\ \textbf{必为}\ u,v,\Delta\ \text{的函数} \Longrightarrow \textbf{C2 失败}⟹\mathrm{DEAD}✓✓✓$$

## 6. 候选表（C1–C4 逐项）

| 候选 $I$ | C1（C–S 前可定义？） | C2（独立于 $u,\Delta$？） | C3（新正交性？） | C4（省长度因子？） | 判定 |
|:--|:--:|:--:|:--:|:--:|:--|
| $(\ell_1,\ell_2)$＝DFI 对角 | ✓ | ✓ | ？ | ✗（比 BC 更粗，DFI 已用） | ✗ |
| $\Delta$-类 | ✓ | **✗（就是定义）** | — | — | **DEAD（重命名）** |
| $u$-类／$\tilde\ell_2'd-\tilde\ell_2d'$ 类 | ✓ | **✗（}u,v\ \text{的函数）** | — | — | **DEAD（重命名）** |
| $(d,\tilde\ell_2)$ 联合关系 | ✓ | **✗（只有行列式可用，已耗尽）** | — | — | **DEAD** |
| $d\ell_1\ell_2$ 乘积类 | ✓ | ✓ | ？ | ？ | **GAP** |
| **更粗的** $\ell$**-类**（以**扩大**振荡区间） | ✓ | ✓ | **可能** ✓ | ？ | **GAP／唯一有前景** ✓ |

## 7. ⭐⭐ 判定

$$\boxed{\text{T3-1C-1}\ (\text{针对}\ (d,\tilde\ell_2)\ \text{型 partial diagonal})\ =\ \mathrm{DEAD}}✓✓✓$$
$$\qquad\text{坍缩点}\ \textbf{精确定位}：\ \text{partial diagonal}\iff\text{行列式}\ \tilde\ell_2'd-\tilde\ell_2d'\ \text{的类}\iff u,v\ \text{（或}\Delta\text{）的类}✓$$
$$\Longrightarrow\ \textbf{正是唐先生预判的结论}：\ \boxed{\text{BC 的 "longer diagonal"}\ \textbf{已经包含} \text{这一层可利用的联合关系}}✓✓✓$$

$$\textbf{由此：}\ \text{C--S 内部已无新 partial diagonal}\ \Longrightarrow\ \text{应转向}\ \textbf{T3-1A（Weil 前联合 Kloosterman cancellation）}✓✓$$

## 8. 保留的 GAP（**一条有前景的线索**）

$$\text{候选表最后一行值得单列}：\ \textbf{更粗的}\ \ell\text{-类} \Longrightarrow \text{把多个}\ (\ell_2,\ell_2')\text{-类}\ \textbf{聚合成一个 fiber}✓$$
$$\qquad\Longrightarrow\ \text{振荡变量}\ \tilde\ell_2\ \text{的有效区间}\ \textbf{被拉长} \Longrightarrow \textbf{或可绕过 T3-1B 的区间不足}（\frac{X}{\sqrt q}\asymp N^{-2/5}\ll1）✓✓$$
$$\qquad\text{剩余必答}：\ \text{聚合带来的项数增加是否小于振荡增益？}\quad(\textbf{C4 未答})✓\quad\text{登记为}\ \textbf{T3-1C-2}✓$$

## 9. 边界
$$\text{(i)}\ \text{§1 的重复结构}\ \textbf{由 (4.9)(4.10) 的变量出现方式确定}（\text{四对带撇变量}）✓\quad\text{(ii)}\ \text{§5 的穷举}\ \textbf{限定已读范围}✓$$
$$\text{(iii)}\ \textbf{未用 RH；零数值}✓\quad\text{(iv)}\ \text{§8 的聚合想法}\ \textbf{未量化}✓$$
