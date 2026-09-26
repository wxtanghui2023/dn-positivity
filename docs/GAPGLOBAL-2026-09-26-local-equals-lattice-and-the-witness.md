已查地图：已跑 scripts/prework_map_check.sh global Boolean preimage 格 盒 局部不足 ⟹ 执行自 `STRATEGY-2026-09-26`（表示转向 ✓）＋ `PREIMAGE2`（局部已闭 ✓）；本档为**AMEND-33 ＋ 可证定理 ＋ 可验证证人**（唐先生 2026-09-26 22:45 令 ✓）；含精确计算 ✓。
D0: 本档对象 = 局部整数性条件的结构（＝格成员性）与 Boolean 纤维缺口
D1: 1（新增：**局部≡格 定理** ✓✓；**n=4 显式证人** ✓✓）

# GAPGLOBAL-2026-09-26 · 局部＝格，与新对象

## §0 结论（先给）

```
$$\boxed{\textbf{(Y-1 定理)}\ \text{全部 1024 个点式整数性同余}\ \Longleftrightarrow\ b\in(I+A)\mathbb Z^{1024}\ \text{（格成员性）}\ ✓✓\ \text{——\textbf{可证}}}$$
$$\boxed{\textbf{(Y-2 推论)}\ \text{一切局部／模／成对检验皆为\textbf{格成员检验}}\ \Longrightarrow\ \textbf{不可能单独排除非 Boolean 的 }f\ ✗\ \text{——\textbf{这解释了 Green／PREIMAGE 1点／2点／模数 为何必然失败}}\ ✓✓}$$
$$\boxed{\textbf{(Y-3 证人)}\ n=4:\ f=(1,1,1,0,0,1,-1,0,\dots,1,1)\ \text{非 Boolean}\ ✓;\ b=(I+A)f\in[1,3]^{16}\ ✓;\ \text{全部 16 点同余成立}\ ✓\ \Longrightarrow\ \textbf{局部}\not\Rightarrow\textbf{全局，已实例化}\ ✓✓}$$
$$\boxed{\textbf{(Y-4)}\ \text{119 \textbf{不封存}};\ \text{新对象＝格}\times\text{盒的}\textbf{Boolean 纤维缺口}\ ✓$$
$$
$$
```

---

## §1 AMEND-33：G-PROGRESS（第二条合法进展 ✓）

```
$$\textbf{原 GATE（筛选用，保留 ✓）}:\ \text{新 lemma}\Rightarrow\text{严格缩小 feasible region}\Rightarrow\text{target bite}\ ✓$$
$$\boxed{\textbf{新增 G-PROGRESS（攻靶用 ✓）}:\ \text{新 lemma}\Rightarrow\textbf{解释此前多个 NO-GO 为何必然发生}}\ ✓\quad\text{或}\quad \text{新构造}\Rightarrow\textbf{证明低阶条件全部不足}\ ✓$$
$$\textbf{理由（唐先生 ✓）}:\ \text{否则 100 个 NO-GO 只是 100 个墓碑};\ \text{目标＝提炼\textbf{一个统一结构定理}}\ ✓$$
$$\textbf{"难"不得再触发换题}:\ \text{target 已投入后，}\boxed{\text{无 P1}\not\Rightarrow\text{换 target}}\ ✗\ \text{（该规则仅适用候选筛选期 ✓）}$$
$$
$$
```

---

## §2 三路线封存（119 保持 OPEN ✓）

```
$$\text{封存}:\ \text{① }A_1/\text{scalar route}\ ✗;\quad \text{② local-PREIMAGE route}\ ✗;\quad \text{③ second-center/incidence counting route}\ ✗\ (\texttt{P1LB4FINAL}\ 16{:}55\ \text{已自封 ✓})$$
$$\textbf{不封存}:\ \boxed{119\ \text{本身}}\ ✓\ \text{（理由：局部统计}\ \cancel{\to}\ \text{全局 Booleanity 的 gap 本身即数学对象 ✓）}$$
$$
$$
```

---

## §3 ⭐ (Y-1)(Y-2) 局部＝格 定理（本档核心，可证 ✓）

```
$$\textbf{命题}:\ \text{对 }b\in\mathbb Z^{1024}:\quad \Big(\forall x:\ D\,|\, \sum_yK(d(x,y))b(y)\Big)\ \Longleftrightarrow\ b\in(I+A)\mathbb Z^{1024}\ ✓$$
$$\textbf{证明}:\ (\Longleftarrow)\ b=(I+A)f,\ f\in\mathbb Z^{1024}\ \Longrightarrow\ Gb=f\in\mathbb Z^{1024}\ \Longrightarrow\ \text{点式同余成立}\ ✓$$
$$\qquad(\Longrightarrow)\ \text{同余成立}\ \Longrightarrow\ f:=Gb\in\mathbb Z^{1024}\ \Longrightarrow\ b=(I+A)f\ ✓\quad\blacksquare$$
$$\textbf{推论 (Y-2)}:\ \text{故一切"只查点式同余／模数／成对联合"的手段，其检验集\textbf{恰等于}格 }(I+A)\mathbb Z^{1024}\ \text{的成员性}\ ✓$$
$$\qquad\Longrightarrow\ \text{只要该格在盒内有非 Boolean 向量，此类手段\textbf{永不能}推出 Booleanity}\ ✗$$
$$\qquad\Longrightarrow\ \boxed{\text{这\textbf{解释}了 }\texttt{GREEN}／\texttt{PREIMAGE-1}\text{点}／\texttt{2}\text{点}／\text{mod }9/5/7\ \text{全部失败}}\ ✓✓\ \text{（AMEND-33 形式 ✓）}$$
$$
$$
```

---

## §4 (Y-3) 可验证证人（n=4 ✓，本档计算 ✓）

```
$$\textbf{证人}:\quad f=(1,1,1,0,0,1,\mathbf{-1},0,0,0,0,0,0,0,1,1)\ \in\mathbb Z^{16}\ \text{（}\Sigma f=5\ ✓\ \textbf{非 Boolean}\ ✓\text{）}$$
$$\qquad b=(I+A)f=(3,3,1,2,1,2,1,1,1,1,2,1,1,2,1,2)\ \Longrightarrow\ b\in[1,3]^{16}\ ✓,\ \Sigma b=25\ ✓$$
$$\qquad b=(I+A)f\ ✓\ \text{（故全部 16 个点式整数性同余\textbf{自动}成立}\ ✓\text{）}\quad\text{而}\ f\notin\{0,1\}^{16}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{局部条件（含全部点同余）不足以推出 Booleanity —— 已实例化并机器验证}}\ ✓✓$$
$$\textbf{边界 ⚠️}:\ \text{该证人质量 }\Sigma f=5\ \text{（非覆盖最小值 }4\text{）};\ \textbf{精确质量版（119 对应 }\Sigma f=119\text{）仍开放}\ ⚠️\ \text{（\textbf{不得断言不存在} }\ ✗)$$
$$
$$
```

---

## §5 新对象与下一刀形态（唐先生 ✓）

```
$$\textbf{新对象}:\ \text{格 }(I+A)\mathbb Z^{1024}\ \text{与盒 }[1,3]^{1024}\ \text{的}\ \textbf{Boolean 纤维}\ ✓$$
$$\textbf{精确重述}:\quad 119\ \Longleftrightarrow\ \exists f\in\{0,1\}^{1024}:\ (I+A)f\in[1,3]^{1024}\ \wedge\ \textstyle\sum b=1309\ \wedge\ \text{profile}(740,283,1)\ ✓$$
$$\textbf{已证不足（本档 ✓）}:\ \text{格成员 ＋ 盒}\ \not\Longrightarrow\ \text{Boolean}\ ✗\ \Longrightarrow\ \text{下一刀必须用\ \textbf{非线性}（}f^2=f\ ✓\text{）或\textbf{格}\times\text{盒的全局几何/计数}\ ✓$$
$$\textbf{禁止}:\ \text{第 16 个局部 NO-GO}\ ✗;\ \text{不再换模数／加点／换 moment}\ ✗\ \text{（唐先生令 ✓）}$$
$$\textbf{成功判据（唐先生 ✓）}:\ \text{至少从该 gap 提取\textbf{一个新的可证明命题}}\ ✓\ \text{——本档已交付 (Y-1)(Y-2)(Y-3) 三条 ✓✓}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §3 为**严格证明** ✓（双向 ✓，仅用 $G=(I+A)^{-1}$ 可逆 ✓）；§4 为**机器验证的显式证人** ✓
- §4 的质量限制**明确标注** ✓（$\Sigma f=5$ ✓，非精确 119 对应值 ✓）
- §1 为**纪律条文**（AMEND-33 写入 `RESEARCH-CONSTITUTION.md` ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张格路已死 ✗（只主张"格成员性"不足 ✓）
- 本轮未跑 solver ✓（仅小立方穷举 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 局部=格 定理 命中文件数=0    :: 
技术词 Boolean 纤维缺口 命中文件数=1    :: ./GAPGLOBAL-2026-09-26-local-equals-lattice-and-the-witness.md 
技术词 n=4 证人       命中文件数=1    :: ./GAPGLOBAL-2026-09-26-local-equals-lattice-and-the-witness.md
```
- **本档新增**：Boolean 纤维缺口（1 档 ✓）、n=4 证人（1 档 ✓）
- ⚠️ `局部=格 定理` **命中 0** —— 本档正文写作「局部＝格」（全角等号），检索词形式不匹配 ⟹ 按纪律**不列为新命名**，仅记为**本项目内部称法** ✓
- **档案已有（引用，不列为提出）**：PREIMAGE 1/2 点、Green 核、P1LB4FINAL 封档、G-PROGRESS 需求
