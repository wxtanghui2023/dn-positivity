# V286 · **乙：给"可证 off-line"对象（P–T／D–H 型）配局部数据** —— ⭐⭐ **半成功**：(a) 侧诊断**可修**（它们**确实能获得有限局部数据**）；但 ⭐⭐⭐ **阻塞换位**（off-line 侧 → **on-line 侧**）＋ ⭐ **REF 单向驳倒工具**（④ 的理由精确化为"**REF 有限，候选可绕开**"） ⭐⭐⭐⭐

$$\boxed{\text{(a) 侧}\ \textbf{可修}：\text{把}\ S\text{-层数据一般化为"前}\ N\ \text{个 Dirichlet 系数"（非"局部因子"）} ⟹ \text{组合型 off-line 对象}\ \textbf{确实获得有限局部数据}} ✓✓$$
$$\boxed{\textbf{引理 V286-L}：\text{D–H 型对象}\ b_n=u\chi(n)+v\bar\chi(n)\ \textbf{无 Euler 积}（b_{p^2}\ne b_p^2）\ ——\ \text{但有系数数据}} ✓✓$$
$$\boxed{\textbf{阻塞换位}：\text{打开 O1-1 需}\ \textbf{两侧状态皆可证};\ \text{off-line 侧可得}\（P–T／D–H）,\ \textbf{on-line 侧不可得}} ✓✓✓$$
$$\boxed{\textbf{REF 工具}：\exists x\in\mathrm{REF}:\pi_S(x)\in A_S \Longrightarrow \textbf{候选被驳倒}（\text{可计算}）;\ \text{但候选可}\textbf{绕开} \mathrm{REF} \Longrightarrow \text{④ 的理由＝}\textbf{REF 有限}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 11:45：**"先乙，再甲"** —— 即先**打破 (a)**：让 P–T／D–H 型对象**获得局部数据**，使其可进入纤维系统 ✓✓
> 查重 ✓（本档执行）：P–T 现象**已在档**（`D1-prime-history-audit` §45，标【引用，未验证】）；Davenport–Heilbronn 见 `p38-g1-deformation.md`；V285 §4(a) 为其新表述 ✓
> 依据 ✓ `V285` §1／§3／§4｜`E103` Lemma A｜`V279` §5｜`V274`-B｜**Hecke 反定理**（经典）✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V286`（`id_claim.sh` ✓；⚠️ 重试曾误领 `V287` 同 slug ⟹ **已清表并释放锁**，记入 `ID-ALIASES.tsv` 作废 ✓）

---

## §1 ⭐ (a) 侧的**向上修正**：S-层数据的正确一般化

$$\text{V285 §1 曾取}\ \pi_S=\big(\text{局部因子}\big)\ \Longrightarrow \text{对组合型对象}\ \textbf{无定义} \quad（\text{因组合型无 Euler 积}）⚠️$$
$$\qquad ⟹ \textbf{修正}：\boxed{\pi_S^{\rm gen}(F)：＝\big(a_1(F),\dots,a_N(F)\big)} \quad（\text{前}\ N\ \text{个 Dirichlet 系数};\ N=N(S)\ \text{有限}）✓✓$$
$$\qquad \text{性质}：\text{对}\ \textbf{任意}\ \text{Dirichlet 级数（含组合型）}\ \textbf{良定义、可计算、不引 RH} ✓✓$$
$$\qquad ⚠️\ \text{代价}：\text{一般化后}\ X_S\ \text{不再自动有限};\ \text{须按类}\ \mathcal C\ \text{另行验证（见 §6 边界 ⑤）}✓$$

---

## §2 ⭐⭐ 半成功之一：off-line 对象**确实获得**有限局部数据

$$\text{Epstein}\ \zeta_Q\ \text{（Potter–Titchmarsh 型）与}\ \text{D–H}\ \text{型对象}\ \text{均为}\ \textbf{有限个 Dirichlet}\ \mathrm L\ \text{的线性组合} ✓$$
$$\qquad ⟹ \text{其系数}\ b_n\ \text{是}\ \textbf{良定义的显式算术数据} ⟹ \pi_S^{\rm gen}\ \text{可直接求出} ✓✓$$
$$\qquad \text{例（D–H）}：b_n=u\,\chi(n)+v\,\bar\chi(n),\quad u=\tfrac{1-i\kappa}{2},\ v=\tfrac{1+i\kappa}{2};\quad u+v=1,\ uv=\tfrac{1+\kappa^2}{4}\ne0 ✓$$

$$\boxed{\textbf{引理 V286-L}（本档显式）}：\ \text{对}\ \chi(p)\ne1\ \text{的}\ p（\text{无穷多}）：$$
$$\qquad b_p^2-b_{p^2}\ =\ uv\big(2-\chi(p)^2-\bar\chi(p)^2\big)\ =\ uv\cdot 2\big(1-\Re\chi(p)^2\big)\ \ne\ 0\quad（\text{因}\ \chi(p)^2\ne1\ \text{当}\ \chi(p)\ne1,\ \text{阶}>2）✓✓$$
$$\qquad ⟹ \textbf{完全乘性在无穷多}\ p\ \text{处失败} ⟹ \textbf{无 Euler 积} ✓;\qquad \text{但}\ \textbf{系数数据仍在} ✓✓$$
$$\Longrightarrow \boxed{\text{"}\textbf{有局部数据}\text{"}\ \ne\ \text{"}\textbf{有 Euler 积}\text{"} —— \text{这正是本档的关键区分};\ \text{故 V285 §4(a) 的"无局部数据"}\ \textbf{可修，非硬障碍}} ✓✓✓$$

---

## §3 ⭐⭐⭐ 但立刻遇到**更强的一侧**：阻塞换位（off-line → **on-line**）

$$\text{打开 O1-1（＝使 C0 失败）需}\ \textbf{FQS 型同层异状态对}：\ \exists x,y:\ \pi_S(x)=\pi_S(y),\ \text{状态不同} ✓$$
$$\qquad \text{且为"可用"，两侧状态}\ \textbf{皆须可证}（\text{否则无法确认"不同"}）✓$$
$$\qquad \text{① off-line 侧}：\textbf{可得}（P–T／D–H 型，且现已有系数数据，§2）✓$$
$$\qquad \text{② on-line 侧}：\text{需"某}\ \textbf{非平凡算术对象} \text{全部零点在线上"} ＝ \text{该对象之 RH} ⟹ \textbf{对任何非平凡对象全部开放} ⚠️✓$$
$$\Longrightarrow \boxed{\text{阻塞}\ \textbf{从 off-line 侧换到 on-line 侧}} ✓✓✓$$
$$\qquad \text{（与 `V285` §4 的关系：彼处写"两侧互斥"；本档}\ \textbf{修正为"一侧可修、另一侧不可得"}，\text{结论方向不变但定位更准}）✓✓$$

---

## §4 ⭐ REF 单向工具（本档新增，可用于实战）

$$\boxed{\textbf{命题 V286-A（单向驳倒）}}：\text{令}\ \mathrm{REF}：＝\text{已知可证 off-line 对象之}\ \textbf{有限清单}（\text{非空}）✓$$
$$\qquad \text{对候选}\ (X_S,\sim_S,A_S)：\ \exists x\in\mathrm{REF}\ \text{使}\ \pi_S(x)\in A_S \Longrightarrow x\in\pi_S^{-1}(A_S)\ \text{而}\ x\notin\mathcal R \Longrightarrow A_S\ne\pi_S(\mathcal R) ✓✓$$
$$\qquad ⟹ \textbf{候选被驳倒};\ \text{且判定}\ \textbf{可计算}（\text{求}\ x\ \text{的前}\ N\ \text{个系数并检隶属}）✓✓$$
$$\boxed{\textbf{推论 V286-B（为何仍 ④）}}：\text{候选可}\textbf{设计为绕开}\ \mathrm{REF}（A_S：＝\text{排除全部已知 off-line 数据}）\Longrightarrow \textbf{不被}\ \mathrm{REF}\ \text{驳倒} ✓$$
$$\qquad ⟹ \text{其真值}\ \textbf{依赖未知 off-line 对象} ⟹ \text{④};\qquad \Longrightarrow \boxed{\text{④ 的真正理由}\ ＝\ \textbf{REF 有限},\ \text{而非"没有 off-line 对象"}} ✓✓✓$$
$$\qquad ⚠️\ \text{实操价值}：\mathrm{REF}\ \text{使"}\textbf{驳倒具体候选}"成为}\ \textbf{可执行动作} \text{（本档把它写成工具，供后续逐候选使用）}✓$$

---

## §5 ⚠️ 空虚者陷阱（N12 纪律执行）

$$\text{平凡空虚者}：\text{有限 Euler 积}\ F_P（`E103`\ \text{Lemma A：开临界带内}\ \textbf{无零点}）⟹ \text{空洞地"满足 RH"} ✓$$
$$\qquad \text{若用作 on-line 侧配对} ⟹ A_S\ \text{须含}\ \pi_S(\mathcal R)\supseteq\pi_S(\text{空虚者}) ⟹ \textbf{撞 P3（非平凡）} ⟹ \textbf{排除} ✓✓$$
$$\qquad ⟹ \text{故不能靠空虚者补上 §3 的 on-line 侧} ✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V286 判词}：\text{乙}\ ＝\ \textbf{半成功}：\text{① (a) 侧}\textbf{可修}（off-line 对象确有有限局部数据，§1–§2）;\ \text{② \textbf{阻塞换位}（off-line → on-line，§3）};\ \text{③ \textbf{REF 工具}＋"候选可绕开"（§4）}} ✓✓✓$$
$$\qquad \text{目标（打开 O1-1）}\ \textbf{未达成};\ \text{原因}\ \textbf{已钉死为 on-line 侧不可得} ✓✓$$

```
① ⚠️ P–T／D–H 的"已证离轴零点"为**引用**（原档标【未验证】）⟹ 本档沿用该标注，**未复核** ⚠️
② ⚠️ §1 的一般化使 $X_S$ 不再自动有限 ⟹ 须按类 $\mathcal C$ 另验（本档未做）⚠️
③ ⚠️ §3 的"on-line 侧不可得"是**当前知识状态**（不写成"不存在"）✓
④ ⚠️ 引理 V286-L 为**本档显式计算**（限于 $u,v,\chi$ 结构；$\chi$ 阶 > 2 时成立）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐ **(a) 侧向上修正**：S-层数据的正确一般化 ＝ 前 N 个 Dirichlet 系数 ⟹ off-line 对象**确实获得有限局部数据**
   ⟹ **V285 §4(a) 的"无局部数据"被修正为"可修，非硬障碍"** ✓✓
② ⭐ **引理 V286-L（显式）**：$b_p^2-b_{p^2}=2uv(1-\Re\chi(p)^2)\ne0$（无穷多 $p$）⟹ **无 Euler 积但有系数数据**
   ⟹ **"有局部数据" ≠ "有 Euler 积"** ✓✓
③ ⭐⭐⭐ **阻塞换位**：打开 O1-1 需两侧状态皆可证；**off-line 可得、on-line 不可得** ⟹ 阻塞换到 on-line 侧 ✓✓
④ ⭐ **REF 单向驳倒工具**（可计算）；**推论**：候选可绕开 REF ⟹ **④ 的理由精确化为"REF 有限"** ✓✓
⑤ ⚠️ 空虚者不可用作 on-line 侧（撞 P3）✓
【下一步】唐先生既定顺序 → **甲**：打破 (b)（在算术类内造可证 off-line 成员，直面 (b)）✓
```
