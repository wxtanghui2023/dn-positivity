# V287 · **甲：打破 (b) —— 在算术类内造"可证 off-line 成员"** —— ⭐⭐⭐ **等价：甲 ⟺ 合法类内的 GRH 反例**（故记 **④**，不是 ②）＋ ⭐ **定量窗口**（off-line 零点必"高且有界"）＋ ⭐⭐ **O1-1 的最终形态**：三种达成各需何种输入 ⭐⭐⭐⭐

$$\boxed{\textbf{V287-A}：\text{甲（合法类内可证 off-line 成员）}\iff \text{该类 GRH 为假}} ⟹ \textbf{④}\ \text{（目标＝著名开问题，非"族内失败"} \mathrm{②} \text{）} ✓✓✓$$
$$\boxed{\textbf{V287-B}（定量窗口）}：\text{off-line 零点若存在，必落}\ \Big(\tfrac12,\ 1-\tfrac{c}{\log(q(2+|t|))}\Big]\ \text{且需}\ q(2+|t|)\gtrsim e^{c/(1-\beta)}} ✓✓$$
$$\boxed{\textbf{V287-C}}：\text{已知一切"造出 off-line 零点"的方法}\ \textbf{全部破坏完全乘性}（`V286`-L）；\text{保乘法性的构造}\ \textbf{无已知实例} ✓✓$$
$$\boxed{\textbf{O1-1 最终形态}：\text{打开}\ \mathrm{C0}\ \text{需}\ \textbf{双向} \text{（可证 on-line ＋ 可证 off-line 且共享有限数据）};\ \text{逐候选驳倒只需}\ \textbf{单向}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 11:45：**"先乙，再甲"** —— 乙已毕（`V286`）；本轮＝**甲：打破 (b)**（在算术类内造可证 off-line 成员）✓
> 依据 ✓ `V286`（(a) 侧可修／阻塞换位／REF 工具）｜`V285` §4｜`V282`（$\mathrm{L3^\star}$ 的 E1–E5 分层）｜`V283` §3（零自由区＝A-leak）｜`E1`–`E5` 分类｜`POS1`／`POS2`（引用，不重复计分）✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V287`（`id_claim.sh` ✓；⚠️ 旧误领行已于 `V286` 轮清除并释放，本档为**正式启用**）✓

---

## §1 目标的形式化

$$\text{求}\ F\in\mathcal C_{\rm arith}\ \text{使}\ \exists\rho:\ \Re\rho>\tfrac12,\ \text{且}\ \textbf{"}\Re\rho>\tfrac12\text{" 已证};\qquad \mathcal C_{\rm arith}：＝\text{Euler 积}\ +\ \text{FE}\ +\ \textbf{算术局部因子} ✓$$
$$\qquad \text{（即：}\mathcal C_{\rm arith}\ \text{排除了 D–H／Epstein 的组合型与 Beurling 的非算术素数）✓$$

---

## §2 ⭐⭐⭐ 命题 V287-A：甲 ⟺ 合法类内的 GRH 反例

$$\text{若}\ \exists F\in\mathcal C_{\rm arith}\ \text{带可证 off-line 零点} \Longrightarrow \text{"}\forall F\in\mathcal C_{\rm arith},\ \text{零点全在线上"}\ \textbf{为假} \Longrightarrow \textbf{该类 GRH 为假} ✓✓$$
$$\qquad \text{反之，若该类 GRH 为假（且反例可指认）} \Longrightarrow \text{甲达成} ✓\qquad ⟹ \boxed{\text{甲}\iff\text{类内 GRH 反例}} ✓✓✓$$
$$\Longrightarrow \textbf{四态判定}：\text{记}\ \textbf{④}（\text{目标}\ ＝\ \text{著名开问题}）;\ \textbf{不是}\ \mathrm{②}\（\text{并非"在已审计族中失败"}）✓✓$$
$$\qquad ⚠️\ \text{纪律（N1／N2）}：\textbf{不得} \text{写成"甲不可能"} ✗;\ \textbf{不得} \text{写成"不存在这样的}\ F\text{"} ✗;\ \text{只能写"当前无实例、且其达成}\ =\ \text{GRH 反例"} ✓$$

---

## §3 ⭐⭐ 命题 V287-B：off-line 零点的**定量窗口**（本档新增）

$$\text{经典零自由区（de la Vallée Poussin 型）}：\text{度}\le d、\text{解析导子}\ C=q(2+|t|)\ \text{的算术对象}\ \textbf{无零点} \text{于}\ \sigma>1-\tfrac{c_d}{\log C} ✓$$
$$\qquad \Longrightarrow \text{off-line 零点}\（\beta>\tfrac12）\ \text{必满足}\ \beta\le1-\tfrac{c_d}{\log(q(2+|t|))} ⟹ \boxed{q(2+|t|)\ \gtrsim\ e^{c_d/(1-\beta)}} ✓✓$$
$$\qquad \text{读法}：\text{β 越接近 1，所需高度}\ \textbf{指数增长};\ \text{β 远离 1 时亦要求}\ \textbf{大导子／高}\ |t| ✓$$
$$\Longrightarrow \boxed{\text{甲的唯一可攻形态}：\text{在窗口}\ \big(\tfrac12,\ 1-\tfrac{c_d}{\log C}\big]\ \text{内构造或排除}} ✓✓\ \text{（与}\ `V283`\ \text{§3 的"零自由区＝archimedean／A-leak"一致）}$$

---

## §4 ⭐⭐ 命题 V287-C：构造侧的已知出路**全被 V286-L 封**

$$\text{已知一切"产生 off-line 零点"的构造}：\text{① D–H 型组合（}\mathcal C_{\rm arith}\ \text{外，无 Euler 积，`V286`-L）② Epstein 非可分解型 ③ Beurling 型（非算术素数）✓$$
$$\qquad ⟹ \textbf{全部破坏完全乘性}（\text{或放弃算术性}）⟹ \text{保乘法性的 off-line 构造}\ \textbf{无已知实例} ✓✓$$
$$\qquad ⚠️\ \text{引用而非新增}：\text{这与}\ `G10`（δ-几何封闭）／E1–E2 分类／`POS` 系列所撞之墙}\ \textbf{同址} ⟹ \textbf{本档不重复计分} ✓$$

---

## §5 ⭐⭐ O1-1 的**最终形态**（乙＋甲 合并结论）

$$\boxed{\text{(a) 打开}\ \mathrm{C0}\（＝\text{证}\ \mathrm{FQS}）}：\text{需}\ \textbf{双向} \text{—— 一个可证 on-line 对象 ＋ 一个可证 off-line 对象，}\textbf{共享有限数据} ⟹ \text{需在合法类内}\ \textbf{双向} \text{触碰 GRH} ✓✓$$
$$\boxed{\text{(b) 封口}\ \mathrm{C0}\（＝\text{证}\ \neg\mathrm{FQS}）}：\text{需证"某层}\ S\ \text{的有限数据}\ \textbf{决定} \text{状态"} ⟹ \text{若成立即得}\ \textbf{有限判据}（`V279`）⟹ \text{亦为开问题级} ✓✓$$
$$\boxed{\text{(c) 逐候选驳倒}（`V286`-A）}：\text{只需}\ \textbf{off-line 侧} \text{（可执行、可计算）};\ \text{但只能命中}\ \mathrm{REF}\ \text{内的已知者} ✓✓✓$$
$$\Longrightarrow \text{故}\：\text{乙（(a) 侧）\textbf{可修}};\ \text{阻塞}\ \textbf{换位到 on-line};\ \text{而 on-line 与 (b) 皆}\ \textbf{GRH 级} ⟹ \textbf{O1-1 的达成 ⟺ 在合法类内 settle GRH（任一方向）} ✓✓✓$$
$$\qquad ⚠️\ \text{与}\ `V285`\ \text{§5 的关系}：\text{彼处"可分性恰好在算术性丧失处可得"} \Longrightarrow \text{本档给出其}\ \textbf{双向精确形式} ✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V287 判词}：\text{① 甲}\iff\text{合法类内 GRH 反例}（⟹ ④，非 ②）;\ \text{② off-line 零点有}\ \textbf{定量窗口};\ \text{③ 保乘法性的 off-line 构造无已知实例};\ \text{④ O1-1 达成}\iff\text{在合法类内 settle GRH}} ✓✓✓$$

```
① ⚠️ §3 依赖经典零自由区（de la Vallée Poussin 型；**引用**，本档未逐条复核）⚠️
② ⚠️ §2 的等价为**定义级／逻辑级**（"类内 GRH 反例" ⟺ "存在可证 off-line 成员"），非新数学定理 ✓
③ ⚠️ 本档**不声称**类内 GRH 为真／为假；**不声称**此类 }F 不存在 ✗（严守 N1／N2）✓
④ ⚠️ §4 的"无已知实例"为**当前知识状态**；其"同址"判断依赖既有档案（引用）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐ **V287-A**：甲 ⟺ 合法类内 **GRH 反例**（记 **④**；不得写成"不可能"）✓✓✓
② ⭐⭐ **V287-B（新）**：off-line 零点必落 $\big(\tfrac12,1-\tfrac{c_d}{\log C}\big]$ 且 $q(2+|t|)\gtrsim e^{c_d/(1-\beta)}$ ⟹ **甲 的唯一可攻窗口** ✓✓
③ ⭐⭐ **V287-C**：构造侧已知出路（D–H／Epstein／Beurling）**全破坏乘法性** ⟹ 保乘法性构造无已知实例（同址于 G10／E1–E2，引用不重复计分）✓
④ ⭐⭐ **O1-1 最终形态**：打开 C0 需**双向**（on-line ＋ off-line 共享数据）；封口 C0 需**有限决定状态**；逐候选驳倒只需**单向** ⟹ **O1-1 达成 ⟺ 在合法类内 settle GRH（任一方向）** ✓✓✓
【建议】把 O1-1 的此最终形态**回写** `REVIEW-2026-09-16` 的第 5 节（O1 行）与 §7（决策意义），保持复盘档为最新口径 ✓
```
