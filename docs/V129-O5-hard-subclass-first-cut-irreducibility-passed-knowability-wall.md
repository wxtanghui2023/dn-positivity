# V129 · ⭐⭐⭐⭐⭐ **O5 最硬子类（不可约高阶 primitive）：第一关通过 ✓（$\Delta^3$ 判据 ＝ 经典 ANOVA/Hoeffding，已被 × 您 2026-09-10 指定过 ✓）｜第二关不归约 ✓ 但两类塌缩 ✗｜第三关 ＝【可知性】墙 ✗（真三体装置已知清单全落禁列 ✗）⟹ O5 ＝ candidate failure ⛔，非类级 NO-GO ✓**
> 委托 ✓ 唐先生 2026-09-14 22:39（**"开 O5，只开最硬子类：不可分解的高阶 primitive／非线性全局约束；先证明 O5 的代数不可约性分类"** ✓）
> 查图 ✓ **同一题已在档** —— `O5-PRE1-P2-irreducible-3body.md`（2026-09-10 ✓，其中 §7 **正是您自己指定的 $\Delta_3$ 判据 ＋ 禁列** ✓）＋ `E176-moment-hierarchy-collapse.md`（第 3 阶＋整类，矩族塌缩 ✓）＋ `E175`（第 2 阶判死 ✓）＋ `G-SW6-CAT` ＋ `O3-mechanism-audit`
> 执行 ✓ 小灵｜**纸面 ＋ 小规模精确校验 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ V129 ✓

---

## §0 判定（✓ 四关逐条 ✓）

$$\boxed{\text{① 第一关（代数不可约性）\textbf{通过 ✓ —— 不构成封口 ✗}}：\Delta_x\Delta_y\Delta_z\Phi\not\equiv0\ \text{可达 ✓；判据本身 ＝ 经典 ANOVA／Hoeffding ✓}}$$
$$\boxed{\text{② 第二关（是否归约到 1／2 点）\textbf{不归约 ✓（一般情形 ✗）}，但两类特殊塌缩 ✗：指示函数／矩族（`E176` ✓）＋ 显式公式只能给 1-点的乘积型分解 ✗}}$$
$$\boxed{\text{③ 第三关（真三体 ∧ 原生 ∧ }\beta\text{-敏感 ∧ 可算）＝ \textbf{【未通过 ⛔】}：档案已枚举的"真三体装置"【全部落在禁列 ✗】}}$$
$$\boxed{\text{④ ⭐ 本档新结论 ✓：O5 的困难【不是代数性的，而是可知性的 ✗】—— 真三体要可用必须能被【算出 ✗】，而唯一已知"可算"机制是显式公式（1-点型 ＋ 乘积分解 ✗）}}$$

## §1 第一关的严格化（✓ $\Delta^3$ 判据 ＝ 经典分解 ✓）

$$\text{设 }\Phi:X\times Y\times Z\to\mathbb R\ ✓,\ (\Delta_x\Phi)(x,y,z):=\Phi(x{+}1,y,z)-\Phi(x,y,z)\ \text{（及 }y,z\ \text{同 ✓）}$$
$$\textbf{命题（经典 ✓）}:\quad \Delta_x\Delta_y\Delta_z\Phi\equiv0\iff \Phi(x,y,z)=f(x,y)+g(y,z)+h(x,z)+u(x)+v(y)+w(z)+c\ ✓$$
$$\textbf{方向 ⟸（我给出 ✓ 两行 ✓）}:\ \text{若 }\Phi=f(x,y)+g(y,z)+h(x,z)\ \text{（＋低阶 ✓）}，则$$
$$\qquad \Delta_z\Phi=\Delta_zg+\Delta_zh\ ✓（\text{不含 }f\ ✓）；\quad \Delta_y\Delta_z\Phi=\Delta_y\Delta_zg\ ✓（\text{因 }\Delta_y\Delta_zh=0\ ✓）$$
$$\qquad \Delta_x\Delta_y\Delta_z\Phi=0\ ✓（\text{因 }\Delta_y\Delta_zg\ \text{不含 }x\ ✓）\ \Longrightarrow\ \textbf{可归约 ⟹ }\Delta^3=0\ ✓✓$$
$$\textbf{方向 ⟹}：\text{由 }\textbf{ANOVA／Hoeffding 分解 ✓}：\Phi=\Phi_\varnothing+\Phi_{\rm unary}+\Phi_{\rm pair}+\Phi_{\rm pure3}\ ✓；$$
$$\qquad\text{每个低阶分量均被某个 }\Delta\ \text{杀死 ✓ ⟹ }\Delta_x\Delta_y\Delta_z\Phi=\Delta_x\Delta_y\Delta_z\Phi_{\rm pure3}\ ✓；\qquad\text{而 }\Phi_{\rm pure3}\ \text{（零边际 ✓）被 }\Delta^3\ \text{单射检出 ✓}$$
$$\qquad\textbf{小规模精确校验 ✓}：X{=}Y{=}Z{=}\{0,1\}\ ✓,\ \Phi=(2x-1)(2y-1)(2z-1)\ \text{（Walsh，纯三体 ✓，各边际为零 ✓）}$$
$$\qquad\qquad(\Delta_x\Delta_y\Delta_z\Phi)(0,0,0)=\sum_{x,y,z}(-1)^{x+y+z}\Phi=\Big(\sum_x(2x{-}1)(-1)^x\Big)^3=(1{+}1)^3=8\neq0\ ✓$$
$$\qquad\qquad\text{而 }\Phi=xy\ \text{型（无 }z\ ✓）\ \Longrightarrow\ \Delta_z=0\ \Longrightarrow\ \Delta^3=0\ ✓\ \text{—— 判据与分解一致 ✓✓}$$
$$\Longrightarrow\ \boxed{\text{您给的第一关是\textbf{正确且经典}的 ✓ —— 它是一把可用的【前筛 ✓】，但}\textbf{不构成对 O5 的封口 ✗（真三体核存在 ✓，如 Walsh 型 ✓）}}$$
$$\qquad\textbf{⚠️ 但不是新内容 ✓}：`O5-PRE1-P2` §7 \ \text{逐字（您 2026-09-10 ✓）}：\text{"寻找三体不可约性判据 }\Delta_3(a,b,c)\ \text{（}\Delta_3=0\iff\text{可由 pairwise data 解释）"}\ ✓\ ——\ \textbf{本档只是把该判据做成严格形式 ✓}$$

## §2 第二关：归约性与两类塌缩（✓）

$$\textbf{(i) 一般情形：纯三体【不归约 ✓】}：\Phi_{\rm pure3}\ \text{不能写成 }\sum f(\rho_i)+g(\rho_i,\rho_j)\ ✗（\text{否证 }E176\ \text{§2① 所留的"非矩型"开口 ✓ 的一般形式 ✓）}$$
$$\qquad\Longrightarrow\ \text{所以"二阶/一阶化"这条【不成立】✗ —— 即：}\textbf{代数层面 O5 不死 ✓}$$
$$\textbf{(ii) 但两处特殊塌缩 ✓（都在档 ✓）}：$$
$$\qquad\text{(a) }\textbf{指示／矩族塌缩 ✓（`E176` ✓ 一行严格 ✓）}：\text{若 }\Phi\ \text{只经由 }r(n)\in\{0,1\}\ \text{进入 ✓，则 }r^k\equiv r\ ✓$$
$$\qquad\qquad\Longrightarrow\ \sum_nr(n)^k=\sum_nr(n)\ \forall k\ ✓\ \Longrightarrow\ \textbf{全矩族塌缩为单一条件 }r\le1\ ✗\ \text{（＝唯一性）}$$
$$\qquad\text{(b) }\textbf{显式公式只能给 1-点的乘积型 ✓}：\sum_{\rho,\rho'}h_1(\gamma)h_2(\gamma')=\Big(\sum_\rho h_1\Big)\Big(\sum_\rho h_2\Big)\ ✓\ \text{—— 由显式公式可算出 ✓}$$
$$\qquad\qquad\textbf{但一般 }k\text{-点核 }h(\gamma_1,\dots,\gamma_k)\ \textbf{不被显式公式确定 ✗}：\text{2-点即 Montgomery 对相关【猜想】✗（未证 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{O5 的障碍形态 ＝ \textbf{【不可算】✗，不是【可归约】✗}} \Longrightarrow\ \text{与 W3／W4（输入边界）＋ `V127`（恒等式 }\beta\text{-盲）同类 ✓}$$

## §3 第三关：真三体装置的已知清单 —— **全部落在禁列** ✗

$$\text{档案 `O5-PRE1-P2` §8 逐字 ✓}：\text{"已知的三体不可约性装置清单 —— 【全部落在你的禁列内】"}$$
| 装置 | 性质 | 判定 |
|:--|:--|:--|
| 信息论 synergy／interaction information | 统计型 | **禁 ✗（N7）** |
| **Massey 积／$A_\infty$ 高阶运算** | 真高阶 ✓（$\langle a,b,c\rangle$ 仅在 pairwise 积消失时定义 ✓） | **禁 ✗**：定义在**上同调**中 ⟹ cohomology ✗ |
| det／cumulant／associator／coboundary／inclusion–exclusion／correlation | 各型 | **全在您 2026-09-10 的禁列 ✓** |
$$\text{此外 ✓}：O5\ \text{的候选来源 }T1\text{–}T5\ \text{已筛（档案 §6 ✓）}：T1\ \text{三元关系（易退化为 incidence ✗）}；T3\ \text{三元 incidence（大概率 O2／O4 ✗）}；T5\ \text{三体 invariant（置换不变 ⟹ N2／N5 ✗）}；\textbf{仅 }T2\ \text{（}F(a,b,c)=0\ \text{型三元约束 ✓）与 }T4\ \text{（三元 operation }\Phi(a,b,c)\ ✓\text{）值得看 ✓}$$
$$\Longrightarrow\ \boxed{\text{【未通过 ⛔】}：\text{档案已做第一轮搜索 ✓，真三体原生的算术实例【未找到 ✗】—— 但按终止规则这只是 }\textbf{candidate failure ⛔}\text{，非类级 NO-GO ✓}}$$

## §4 ⭐ 本档的结构性结论（✓ 新 ✓）

$$\boxed{\text{O5 的困难【不是代数性的，而是【可知性／可算性】的 ✗】}}$$
$$\qquad\text{论证 ✓}：\text{真三体对象要能用于 RH ✓，必须能被}\textbf{算出}（\text{或至少能被有效判定 ✓）；}$$
$$\qquad\qquad\text{而已知唯一"算出零点侧量"的机制 ＝ }\textbf{显式公式 ✓}\ \text{—— 它只给}\textbf{1-点型（及其乘积 ✓）}\ ✗；$$
$$\qquad\qquad\text{一般 }k\ \text{-点相关（}k\ge2\ ✓\text{）恰是【猜想级】✗（Montgomery 型 ✓）⟹ 真三体若要启动，必须先【假设】未证输入 ✗}$$
$$\qquad\Longrightarrow\ \boxed{\text{O5}\ \text{与前面各路的墙是【同一堵】✓}：\text{W3／W4（输入边界）＋ `V127`（机制是恒等式 }\Rightarrow\beta\text{-盲 ✓）}}$$
$$\qquad\textbf{唯一未被排除的形态 ✓（留给后续 ✓）}：\text{一个}\textbf{可算的 k-点型对象}（k\ge2\ ✓）\ \text{—— 即：不假设对相关猜想，而由算术结构本身【推出】高阶相关 ✓}$$
$$\qquad\qquad\text{（档案 `E176` §2 已点名的三个未分析形态与此对齐 ✓：(a) 非矩型非线性泛函 ✓；(b) 支撑几何（差集／Sidon／Bohr ✓）；(c) 非 }1_A*1_B\ \text{型卷积 ✓）}$$

## §5 MASTER 更新（✓）

$$\text{(i) §4.2 台账 ✓}：O5\ \text{状态 "⛔ 未审计"}\ \longrightarrow\ \textbf{"子类已开（}V129\text{）✓：第一／二关通过 ✓；第三关 ＝ candidate failure（已知装置全在禁列 ✗）；类级未封 ✓"}$$
$$\text{(ii) 待攻清单 ✓}：\text{恢复为 }\ \{\underbrace{O2}_{\text{未审计 ⛔}},\ \underbrace{O5}_{\text{子类已开，残量 ＝ 可算 k-点对象 ⛔}},\ O3^\star\}\ >\ \{\text{类 VI},\ SW6\}\ >\ J\ ✓$$

## §6 边界（✓）

```
⚠️ 第一关判据为【经典结果 ✓】（ANOVA/Hoeffding ✓）＋ 小规模精确校验 ✓；未新证 ↗ 未声称原创 ✗
   —— 且明确：该判据【您已于 2026-09-10 指定过】✓（`O5-PRE1-P2` §7 ✓）⟹ 本轮 ＝ 同一题的再次到达 ✓
⚠️ "真三体未找到"是【第一轮搜索 ✓】（档案 2026-09-10 ✓ ＋ 本档复核 ✓）；不得写成"不存在"✗
⚠️ 本档【不】声称 O5 已封 ✗ —— 按终止规则只到 candidate failure ⛔；亦不声称"必有新对象"✗
✅ 净产出 ✓：① 第一关做成严格形式 ＋ 校验 ✓；② 两关通过、第三关未通过之精确表述 ✓；
   ③ ⭐ 结构性结论：O5 障碍 ＝ 可知性（不可算）而非代数 ✓；④ 唯一未排除形态 ＝ 可算 k-点对象 ✓
```
$$\boxed{\text{O5 最硬子类（}V129\text{）✓：第一关 }\Delta_x\Delta_y\Delta_z\Phi\not\equiv0\ \text{（＝经典 ANOVA／Hoeffding 判据 ✓，Walsh 型校验 ✓，}\textbf{已被您 2026-09-10 指定过 ✓}\text{）}\ \textbf{通过但不封口 ✗}；第二关：纯三体不归约 ✓，但指示／矩族塌缩（`E176`：r\in\{0,1\}\Rightarrow r^k=r ✓）＋ 一般 k-点相关不被显式公式确定（Montgomery 型猜想 ✗）⟹ \textbf{障碍形态 ＝ 不可算 ✗，非可归约 ✗}；第三关：真三体装置已知清单（synergy／Massey–A_\infty／det／cumulant／associator／coboundary／inclusion–exclusion／correlation）\textbf{全落禁列 ✗} ⟹ \textbf{candidate failure ⛔，非类级 NO-GO ✓}；⭐ 结构性结论：O5 与 W3／W4＋`V127` 同墙；唯一未排除形态 ＝【可算的 k-点型对象】✓}$$
