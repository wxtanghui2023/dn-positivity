# E155 · ⭐⭐⭐⭐ **TOL′ 反例审计：定理【成立 ✓（局部解析版）】，但"解析性"是【载重假设 ✗】**
### （撤回"必为二次型"✗；发现真空洞：去掉解析性，一行反例 ✓ —— $Q(z):=|\Re z|$ ✗）

> 委托 ✓ 唐先生 2026-09-14 12:29（**撤回"必为二次型"✗；采纳 TOL′ ✓；对 TOL′ 做反例审计 ✓，查四型 ✗**）
> 依据 ✓ `E154`（$i\mathbb R$ 非代数集 ✓）＋ 您 §1–§10 ✓
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 判定（✓ 五条）

```
✅ **① 受理 ✓：撤回"必为二次型"✗** —— 您的四反例【确认 ✓】：
   $$Q_2=x^2\ ✓\big|\ Q_4=x^4\ ✓\big|\ Q_6=x^6\ ✓\big|\ Q_{\exp}=e^{x^2}-1\ ✓\ \text{【皆】}Q\ge0\ \wedge\ (Q=0\Leftrightarrow x=0)\ ✓\ \text{但【非二次 ✗】}$$
   $$\Longrightarrow\ \text{"obstruction 必为二次型"}\ \textbf{【为假 ✗】}\ \text{（}\textbf{且非偶然 ✗：横向允许高阶退化 ⟹ 二次性不存在 ✓）}$$
✅ **② TOL′ 的证明【核查通过 ✓】**（您的 §3 ✓，逐行核 ✓）：
   $$\text{设 }Q\ \text{实解析 ✓、}Q\ge0\ ✓、Q(x,y)=0\Leftrightarrow x=0\ ✓\ \Longrightarrow\ Q(x,y)=\sum_{k\ge0}a_k(y)x^k\ ✓\ \text{且 }a_0(y)=Q(0,y)=0\ ✓$$
   $$\text{设 }a_m\ \text{为最低非零项 ✓：}m\ \text{奇 ⟹ }Q\ \text{在 }x=0\ \text{两侧【变号 ✗】⟹ 与 }Q\ge0\ \text{矛盾 ✓ ⟹ }m=2r\ \textbf{偶 ✓}$$
   $$\text{且 }a_{2r}(y)>0\ ✓（\text{因 }Q\ge0\ \text{且首项支配 ✓）}\ \Longrightarrow\ \boxed{Q=(\Re z)^{2m}W\ ✓,\ W(0,y)>0\ ✓},\ \ m\ge1\ ✓$$
   $$\text{⚠️ 两条【隐含假设 ✓】须写明 ✗：(i) }\textbf{局部 ✓}（围绕轴上每点 ✓）；\text{(ii) }W\ \text{在 }x\ne0\ \text{处【非零 ✓】}（\text{由零集假设 ✓，否则 }Q\ \text{多出零点 ✗）}$$
✅ **③ Level 1（纯全纯）【判死确认 ✓】**（您的 §9 ✓）：
   $$\text{非零全纯 }F\ \text{的零点【离散 ✗】；}i\mathbb R\ \text{是【连续一维 ✗】} \Longrightarrow \text{无解析 }F\ \text{其零集含 }i\mathbb R\ ✓$$
   $$\text{更强 ✓：若 }F\equiv0\ \text{于 }i\mathbb R\ ✓\ \text{则【恒等定理 ✗】⟹ }F\equiv0\ ⟹ \text{零集}=\mathbb C\ ✗\ \Longrightarrow\ \textbf{Level 1 【死 ✓】}$$
🔴 **④ ⭐ 反例审计四型（您 §10 指定 ✓）** —— 见 §1 ✓
🔴🔴 **⑤ ⭐⭐ 发现【真空洞 ✓】**：\textbf{TOL′ 的载重假设是【解析性 ✗】} —— **去掉它，一行反例 ✓**：
   $$Q(z):=|\Re z|\ ✓\ \text{—— canonical（由 }(\sigma,\tau)\ ✓\text{）、零集【恰为】}i\mathbb R\ ✓、\text{无正性 ✓、无度量 ✓、无二次型 ✓}$$
   $$\text{但【不解析 ✗】（}x\ \text{轴上不可导 ✓）}\ \Longrightarrow\ \boxed{\textbf{TOL′ ＝ 解析型定理 ✓，非一般定理 ✗}}$$
```

## 1. 四型反例审计（✓ 逐型 ✓）

$$\textbf{(甲) 积分型 ✓}：Q(z)=\int|f_z|^2d\mu\ \ge0\ ✓\ \text{解析（若被积解析 ✓）}\ \Longrightarrow\ \textbf{零集【通常过大 ✗】}$$
$$\qquad\Longrightarrow\ ⭐\ \textbf{与档内 POS1 逐字一致 ✓}：\text{"消失集【过宽 ⟹ 空洞 ✗】"}\ —— \ \textbf{积分型【不构成反例 ✓，反而落回已知类 ✓】}$$
$$\textbf{(乙) 行列式型 ✓}：Q=|\det M|^2\ \ge0\ ✓\ \text{解析 ✓} \Longrightarrow \textbf{TOL′ 【适用 ✓】}\ \text{（无逃逸 ✓）}；\ \text{但 }\det M\ \text{本身【不正定 ✗】}（\text{符号不定 ✓）}$$
$$\textbf{(丙) 谱流型 ✓}：\text{指标/流不变量【取整数值 ✗】} \Longrightarrow \textbf{太粗 ✓}（\text{无法等于【连续】轴 ✓；}E151\ \text{同结论 ✓）}$$
$$\textbf{(丁) 非局部型 ✓}：\text{两条分岔 ✓}：$$
$$\qquad\text{(i) 若经 }Z(\Xi)\ \text{本身定义 ✓} \Longrightarrow \textbf{循环 ✗}（\text{＝您的 Level-3 排除 ✓："不把 }\Re\rho\ \text{塞进去 ✓"}）$$
$$\qquad\text{(ii) 若经 }\Xi\ \text{的解析结构定义 ✓（例：谱行列式 ✓）} \Longrightarrow \textbf{归入解析型 ✓ ⟹ TOL′ 适用 ✓}$$
$$\Longrightarrow\ ⭐\ \textbf{四型【零逃逸 ✓】}\ \text{—— 但真实逃逸【在第五处 ✗】（解析性假设 ✓，见 §0⑤ ✓）}$$

## 2. ⭐ 因此新的判死/判活界线（✓ 本轮实质 ✓）

$$\boxed{\text{TOL′ 成立 ✓} \Longleftrightarrow \text{【解析性假设 ✓】}\ \text{—— 而该假设【未被】从 canonicity 推出 ✗✓}}$$
$$\textbf{关键追问 ✓}：\text{"canonical obstruction 是否【必然】解析 ✗？"}$$
$$\qquad\text{而 }C_2\ \text{的用途 ✓：}Z(\Xi)\ \text{是【离散 ✗】} \Longrightarrow \textbf{一个【非解析】obstruction 已足够 ✓} \Longrightarrow \text{解析性【不能由此推出 ✗】}$$
$$\Longrightarrow\ \text{故解析性【必须来自别处 ✓】：例如"由 }\Xi\ \text{的数据【局部、可计算】产生 ✓"}\ —— \ \textbf{这正是您 §7 的要求 ✓（constructive + local ✓）}$$
$$\textbf{但 ✓}：\text{"可计算 + 局部 + canonical"}\ \Longrightarrow\ \text{"解析"}\ ✗\ \textbf{【未证 ✓】}\ \text{（可计算函数可处处不可导 ✓）}$$

## 3. 一个【结构性重述 ✓】（附赠 ✓）

$$\text{为何轴【恰好】是"实超曲面"✓}：i\mathbb R\ \text{在 }\mathbb C\cong\mathbb R^2\ \text{中【实余维 1 ✗】}\ ✓$$
$$\text{而实值【解析】函数的零集【一般】正是【余维 1 ✓】} \Longrightarrow i\mathbb R\ \textbf{恰是"通有的"零集维数 ✓✓}$$
$$\Longrightarrow\ ⭐\ \text{"定位到轴"}\ = \text{"取一个【实值】（＝【用 }\tau\ \text{✗】）标量 ✓"}\ —— \ \textbf{故 Level 2 的存在性【不神秘 ✓】；}$$
$$\qquad\text{神秘的是它的【canonical 来源 ✗】}\ \text{（＝您的 Level 3 ✓）}$$

## 4. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；受理并撤回旧靶 ✓；TOL′ 证明逐行核过 ✓
⚠️ **① TOL′ 证明中我【补了两条隐含假设 ✓】**（局部性 ✓；W 在 x≠0 非零 ✓）—— 若您不认，请裁 ✗
⚠️ **② 反例 }Q(z)=|\Re z|$ 是【形式构造 ✓】** —— 其"allowedness"取决于您对"analytic"的最终裁定 ✓
⚠️ **③ 本轮【不声称】TOL′ 无用 ✗** —— 相反 ✓：它**精确地把载重压到【解析性】一条 ✓**，这是本方向**最锐的一次定位 ✓**
⚠️ **④ 未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **撤回二次型靶 ✓（您的四反例 ✓）**；② ⭐ **TOL′ 证明核查通过 ✓（＋两条隐含假设 ✓）**；
   ③ **Level 1 判死确认 ✓**；④ ⭐ **四型反例【零逃逸 ✓】**；⑤ ⭐⭐ **发现真空洞：载重假设＝解析性 ✗（}|\Re z|$ 反例 ✓）**；
   ⑥ **新锐靶 ＝ "canonical + constructive + local ⟹ 解析 ✗？"**
```

## 5. 一句话（✓）

$$\boxed{\text{TOL′【成立 ✓】；它的载重假设【解析性】未被 canonicity 推出 ✗ ⟹ 新的唯一靶 ＝ "canonical ＋ constructive ＋ local ⟹ 解析 ✗？"}}$$
