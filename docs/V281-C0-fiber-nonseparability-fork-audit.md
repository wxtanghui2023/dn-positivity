# V281 · **C0 分叉审计（七步）：$\mathrm{C0}\iff\mathrm{FQS}$ 的精确形式 ＋ 纤维结构的具体计算 ＋ 卡点诊断** —— ⚠️ **T10 勘误：`V280` §3 越界（V258 接管尚需额外证明）**；⭐⭐⭐ **诊断：C0 卡在 Euler 全局约束本身（`V126`-L3），不是"我们没找到构造"** ⭐⭐⭐⭐

$$\boxed{\text{精确形式：}\mathrm{C0}（\text{存在层}）\iff\mathrm{FQS};\qquad \text{机制}\iff\neg\mathrm{FQS}\ +\ \text{(ii) canonical 可描述}\ +\ \text{(iii) 非循环可证}} ✓✓$$
$$\boxed{\text{七步审计结果}\ ＝\ \text{第三种}：\textbf{证明卡在真实的 Euler 全局约束}（`V126`-L3：B 层不可实现，强制约束 ＝ 显式公式）} ✓✓✓$$
$$\boxed{\text{缺失输入被唯一命名}：\textbf{"类内一个可证 off-line 的 Euler-积成员"}（＋同层数据的 RH 成员）} ✓✓$$
$$\boxed{\text{⚠️ 勘误}：`V280`\ \text{§3 的"}\ge2\ \text{素数 ⟹ 相关量 ⟹ `V258` 接管"}\ \textbf{过强};\ \text{降级为"}\textbf{分类成立、接管待证}"} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 11:23：**"先不要钉死 canonical representation，直接回到 C0 本体"**；**"V280-A 的不变量分类成立，但从它不能推出 '$k\ge2$ 必然落 `V258`'"**（理由：$\chi_\rho(g_{p_1}g_{p_2}^{-1})$ 是词字符，但"属 Chebotarev 型相关数据"≠"已被预算墙完全覆盖"；**固定有限 Galois 表示时，词的代数关系可能携带非交换的相对位置，而非单纯独立素数统计**）✓✓ —— **故 `V280` §3 只能记作 "V280-A：不变量分类成立；`V258` 接管则尚需额外证明"** ✓；**V281 指令**：做严格 C0 分叉审计（七步），只接受三种结果（FQS 成立／FQS 被反例击穿／**证明卡在真实 Euler 全局约束**）—— 并强调第三种"比又一个 DEAD 有价值，因为它精确告诉我们 C0 卡在 Euler 结构本身还是我们尚未找到构造" ✓✓
> 依据 ✓ `V126`-L3（B 层不可实现／强制约束＝显式公式）｜`V279`（$\mathrm{C0}\iff\neg\mathrm{FQS}$；三分）｜`V277`｜`E103` Lemma A｜**Chebotarev（经典）** ✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V281`（`id_claim.sh` ✓）

---

## §0 ⚠️ T10 勘误：`V280` §3 降级（采纳唐先生更正）

$$\text{原写} ✗：\ k\ge2\ \Longrightarrow\ \text{"恰是}\ k\text{-点 Chebotarev 相关量"}\ \Longrightarrow\ \text{"}\ `V258`\ \text{接管"} ⚠️$$
$$\qquad \textbf{过强之处}：\text{"属 Chebotarev 型数据"}\ \ne\ \text{"已被既有相关预算墙（`V102`／`V162`／`V217b`）完全覆盖"} ✗✓$$
$$\qquad \qquad \text{且}\ \text{固定有限 Galois 表示时，\textbf{词的代数关系}可能携带}\ \textbf{非交换的相对位置}，\ \text{而非单纯独立素数统计} ✓✓$$
$$\Longrightarrow \boxed{\text{降级为}：\textbf{V280-A：不变量分类成立};\quad \textbf{"}\ `V258`\ \text{接管"尚需额外证明}} ✓✓$$

---

## §1 C0-1：纤维不可分离形式（采纳唐先生）

$$\text{任何候选有限机制只能读}\ \pi_S(x)\in X_S;\ \text{若能证明}\ \exists x_{\mathcal R}\in\mathcal R,\ x_{\mathcal N}\in\mathcal N:\ \pi_S(x_{\mathcal R})=\pi_S(x_{\mathcal N})$$
$$\qquad ⟹ \text{不存在}\ A_S\subseteq X_S\ \text{使}\ \pi_S^{-1}(A_S)=\mathcal R ✓$$
$$\qquad \boxed{\text{注意（唐先生）}：\text{此处}\ \textbf{完全不需要} \text{讨论}\ A_S\ \text{是否 canonical}} ✓✓\ \text{—— canonicity 只在"下一步"（机制）处起作用} ✓$$

---

## §2 精确形式（本档）

$$\boxed{\mathrm{C0}（\text{存在层}）\iff\mathrm{FQS};\qquad \text{机制}\iff\neg\mathrm{FQS}\ +\ \text{(ii)}\ +\ \text{(iii)}} ✓✓$$
$$\qquad ⟹ \mathrm{FQS}\ \text{一旦成立} ⟹ \text{存在层封口} ⟹ \textbf{机制不可能} ⟹ \mathrm{D1_C}\ \text{封} ✓✓$$
$$\qquad ⟹ \text{故}\ \mathrm{FQS}\ \textbf{是}\ \mathrm{D1_C}\ \text{路线上唯一正确的靶}（`V279`\ \text{§2 的反转在此完成}）✓$$

---

## §3 ⭐⭐⭐ 七步分叉审计（执行）

$$\textbf{步骤 1（固定 }S\text{）}：\text{取任意有限素数集}\ S，\ \text{及类}\ \mathcal C（\text{degree 1、Euler 积、FE、与}\ \zeta\ \text{同 archimedean 因子与导子}）✓$$
$$\textbf{步骤 2（}\pi_S\ \text{能读什么）}：\qquad \pi_S(x)=\Big(\{a_{p^k}(x)\}_{p\in S,\ k\ge1};\ \text{degree／conductor／archimedean 因子}\Big) ✓$$
$$\qquad \text{即：}\textbf{前}\ |S|\ \text{个素数处的局部因子} \ ＋\ \text{类宽不变量} ✓$$

$$\textbf{步骤 3（求纤维）—— 本档给出具体族}：\text{取}\ \zeta\ \text{的层数据}；\text{求}\ \pi_S^{-1}(\pi_S(\zeta))：$$
$$\qquad \text{取二次特征}\ \chi_q（q\ \text{素数}）；\text{由}\ \textbf{Chebotarev} \text{应用于多二次域}\ \mathbb Q(\sqrt p:p\in S)：$$
$$\qquad \qquad \text{使"所有}\ p\in S\ \text{在}\ \mathbb Q(\sqrt q)\ \text{中完全分裂"的素数}\ q\ \text{有密度}\ 2^{-|S|}>0 ⟹ \textbf{无穷多个} ✓✓$$
$$\qquad \qquad \text{对这些}\ q：\chi_q(p)=1\ \forall p\in S ⟹ \mathrm L(s,\chi_q)\ \text{与}\ \zeta\ \text{在}\ p\in S\ \text{处}\ \textbf{局部因子相同} ✓✓$$
$$\Longrightarrow \boxed{\text{纤维}\ \textbf{非空且巨大}：\text{含无穷多}\ \textbf{真实算术对象}（\mathrm L(s,\chi_q)，\text{导子}\ q\notin S，\text{尾部不同}）} ✓✓✓$$
$$\qquad \text{即：唐先生要的"}\textbf{同一有限数据 ＋ 不同尾部}\text{"在两处都已实现 —— \textbf{差的只是 off-line 状态的可证性}} ✓$$

$$\textbf{步骤 4–5（纤维内是否存在 RH/非-RH 分离？构造？）}：\qquad \text{两条路都被卡住}：$$
$$\qquad \text{(a) }\textbf{同对象尾部替换} ⇒ \text{需在}\ \textbf{Euler 类内} \text{改变尾部而不动有限数据并移动零点}$$
$$\qquad \qquad ⟹ \textbf{不可能}：`V126`-L3 —— \text{（＋Euler 积／Dirichlet 级数）}\ \textbf{尾部替换不可实现} ✗;\ \text{强制约束 ＝ 显式公式} ✓✓$$
$$\qquad \text{(b) }\textbf{类内配对} ⇒ \text{需一个}\ \textbf{可证 off-line} \text{的 Euler-积成员}\ y\ \text{与某 RH 成员}\ x\ \text{同层数据}$$
$$\qquad \qquad ⟹ \textbf{不可得}：\text{已知 off-line 实例（Davenport–Heilbronn／Epstein／Beurling 型）}\ \textbf{全无 Euler 积} ⟹ \text{出类} ✗✓$$
$$\qquad \qquad ⚠️\ \text{且}\ \textbf{GRH-for-class 预期}\ \mathcal C\ \text{内全 on-line} ⟹ \text{该类成员可能}\ \textbf{没有一个} \text{off-line} ✓$$

$$\textbf{步骤 6（最小结构）}：\text{导致分离（}\neg\mathrm{FQS}）的\ \textbf{最小结构}＝\boxed{\text{S-数据}\ \textbf{决定} \text{RH 状态}} ⟹ \text{即一条}\ \textbf{有限判据} ⟹ \text{那本身就是证书} ✓✓$$
$$\qquad \text{而阻碍 FQS 的\ \textbf{最小结构}＝\boxed{\text{Euler 全局约束}（`V126`-L3：局部—整体耦合只在 Euler／显式公式层生效）}} ✓✓$$

$$\textbf{步骤 7（三选一）}：\qquad \boxed{\text{FQS 成立}} ✗\（\text{无法给出 off-line 见证}）;\quad \boxed{\text{FQS 被反例击穿}} ✗\（\text{无法给出有限判据}）;\quad \boxed{\textbf{证明卡在真实的 Euler 全局约束}} ✓✓✓$$

---

## §4 ⭐⭐ 诊断（本档核心价值）

$$\boxed{\textbf{诊断}：\mathrm{C0}\ \textbf{卡在 Euler 结构本身}，\ \textbf{不是} \text{"我们尚未找到构造"}} ✓✓$$
$$\qquad \text{依据}：\text{抽象尾部自由度}\ \textbf{存在}（`V126`\ \text{L1／L2：任意对称配置可实现}）⟹ \text{它会给出 FQS};$$
$$\qquad \qquad \text{但该自由度在}\ \textbf{Euler 类内可证不可实现}（`V126`\ \text{L3}）⟹ \textbf{卡点是结构性的、且已被证明} ✓✓✓$$
$$\textbf{三条能真正推动 FQS 的输入（本档枚举，供选择）}：$$
$$\qquad \text{① \textbf{打破}\ `V126`-L3}：\text{在 Euler 类内实现"有限数据不变 ＋ 零点移动"} ⟹ \mathrm{FQS}\ \text{立即有构造} ✓$$
$$\qquad \text{② \textbf{类内一个可证 off-line 的 Euler-积成员}}（＋同层 RH 成员）⟹ \mathrm{FQS}\ \text{有构造} ✓$$
$$\qquad \text{③（反向）\textbf{证明某层}\ S\ \text{的}\ S\text{-数据决定 RH} ⟹ \neg\mathrm{FQS} ⟹ \textbf{直接得证书}}（\text{＝唐先生七步的"若不存在，给出最小结构"}）✓$$

---

## §5 ⚠️ 退化警示（本档新增，防止"空虚的真"）

$$\text{若}\ \mathcal N=\varnothing（\text{GRH-for-class 成立}）⟹ \mathrm{FQS}\ \textbf{假};\ \text{分离存在但}\ A_S=\pi_S(\mathcal R)=X_S ⟹ \textbf{撞 P3（非平凡）} ✓$$
$$\qquad ⟹ \boxed{\text{此时}\ \mathrm{C0}\ \text{为"真"但}\ \textbf{空虚}：\text{不产生任何机制}} ✓✓$$
$$\qquad ⟹ \text{故}\ \mathrm{C0}\ \text{的}\textbf{有价值形式} \text{必须写成}：\boxed{\mathrm{FQS}\quad\text{或}\quad[\neg\mathrm{FQS}\ \wedge\ \text{分离由}\ \textbf{真子集} A_S\ \text{实现}]} ✓✓\ \text{（与 `V276` \text{P3 补丁同源}）$$

---

## §6 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V281 判词}：\text{① 勘误 `V280` §3（}\ge2\ \text{素数 ⟹ `V258` 接管改为"待证"}）;\ \text{②}\ \mathrm{C0}\iff\mathrm{FQS}（\text{存在层}）＋\text{机制三分};\ \text{③ 七步审计}＝\textbf{第三种};\ \text{④ 卡点}\ ＝\ \textbf{Euler 全局约束}（`V126`-L3）;\ \text{⑤ 缺失输入已命名}} ✓✓✓$$

```
① ⚠️ 本档**不声称** FQS 为真、也**不声称**其为假 ✗✓；只给七步审计与卡点诊断 ✓
② 步骤 3 的"无穷多 q"依赖 **Chebotarev**（引用·经典）；步骤 4-5 的 L3 依赖 `V126`（引用）⚠️
③ §5 的退化警示依赖"$\mathcal R\cup\mathcal N=X$ 且 $\mathcal N$ 可空"的读法 ⚠️
④ 本档**未**用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⚠️ **T10 勘误**：`V280` §3 降级为"分类成立、`V258` 接管待证"✓
② ⭐ **精确形式**：$\mathrm{C0}\iff\mathrm{FQS}$（存在层）＋ 机制三分（(ii)＋(iii)）✓
③ ⭐⭐ **纤维的具体计算**：$S$-层数据的纤维**非空且巨大**（Chebotarev：无穷多二次特征 $\mathrm L(s,\chi_q)$ 与 $\zeta$ 在前 $|S|$ 处局部因子相同）⟹ "同有限数据＋不同尾部"**已实现**；差的只是 off-line 可证性 ✓✓
④ ⭐⭐ **卡点诊断**：C0 卡在 **Euler 全局约束本身（`V126`-L3）**，非"未找到构造" ✓✓✓
⑤ ⭐ **缺失输入命名**：类内一个可证 off-line 的 Euler-积成员（或打破 L3）✓
⑥ ⚠️ **退化警示**：$\mathcal N=\varnothing$ 时 C0 为"空虚的真" ⟹ 有价值形式须加"真子集 $A_S$"条件 ✓
```
