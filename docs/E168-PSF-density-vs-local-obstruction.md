# E168 · ⭐⭐⭐⭐⭐ **P-SF：密度 × 模 $p^2$ 局部禁阻 —— 条件性矛盾 ＋ 数值核 $6/\pi^2<\pi/4$**
> 委托 ✓ 唐先生 13:51（**(ii) 但只攻 P-SF ✓；不做枚举 ✓；不碰 RH／ζ 解析／数值 ✓**）
> 执行 ✓ 小灵｜**纸面推演 ✓（零数值实验 ✓）**｜纪律 ✓ 未用 RH ✓；未涉 ζ 解析延拓 ✓；未跑 Lean ✓；先查档 ✓

---

## §0 勘误（✓ 您对 ✓）

$$\text{我提的"零集是有限个 AP 的并"}\ \textbf{【错 ✗】}：\text{非平方自由集}=\bigcup_{p}p^2\mathbb N\ \textbf{是【无限并 ✗】}\ ✓\ \text{（截断内才有限 ✓）}$$
$$\text{故靶只能是 ✓：}\ \boxed{\textbf{无限局部禁阻}\ \times\ \textbf{唯一加法分解}\ \text{是否相容 ✗}}$$

## §1 P-SF 精确定义（✓ 照录您 §9 ✓）

$$\textbf{P-SF ✓}：\text{若 }S=\{n:\mu^2(n)=1\}\ \text{有非平凡唯一加法分解}\ S=A\oplus B\ ✓，\text{则是否}\ \exists p:\ 0\in A_p+B_p\ ✗?$$
$$\text{若 P-SF 成立 ✓} \Longrightarrow M(x)\ \text{在 }\{0,1\}[[x]]\ \text{中【不可非平凡 Cauchy 分解 ✓】}$$

## §2 五条引理（✓ 前四条【自证 ✓】；第五条【严格 ✓】）

$$\textbf{引理 1（铺砌 ✓）}：S=A\oplus B\ \Longrightarrow\ S=\bigsqcup_{a\in A}(a+B)\ \text{（互不相交 ✓）}$$
$$\qquad\text{证 ✓}：S=\bigcup_{a\in A}(a+B)\ ✓\ \text{（定义 ✓）；若}\ a_1+b_1=a_2+b_2\ ✓\ \text{且}\ (a_1,b_1)\ne(a_2,b_2)\ \Longrightarrow\ \text{破坏唯一性 ✗} \Longrightarrow \text{不相交 ✓}$$
$$\textbf{引理 2 ✓}：0\in A,\ 1\in B\ \Longrightarrow\ B\subseteq S\ ✓\ \text{且}\ A\subseteq S-1\ ✓$$
$$\qquad\text{证 ✓}：b=0+b\in S\ ✓；a\in A\ \Longrightarrow\ a+1\in A+B=S\ ✓\ \text{（}1\in B\ ✓）\ ✓$$
$$\qquad\text{（}0\in A\ ✓\ \text{与}\ 1\in B\ ✓\ \text{由}\ [x^1]M=1\ \text{与}\ b_0=0\ \text{定 ✓；}a_1\in\{0,1\}\ \text{两种分支皆不影响下文 ✓）}$$
$$\textbf{引理 3 ⭐（把您的"⊆"强化为"＝"✓）}：\ \boxed{A_p+B_p=S_p=(\mathbb Z/p^2)\setminus\{0\}}$$
$$\qquad\text{证 ✓}：\text{(a) }S_p=(\mathbb Z/p^2)\setminus\{0\}\ ✓\ \text{（每非零类都有平方自由数 ✓，由 AP 中平方自由数正密度 ✓）}；\text{(b) }A+B=S\ \Longrightarrow\ A_p+B_p\supseteq S_p\ ✓；\text{(c) }A_p+B_p\subseteq S_p\ ✓\ \text{（}A,B\subseteq S\ ✓）$$
$$\textbf{引理 4 ✓}：|A_p|+|B_p|\le p^2-1\ ✓\ \text{（}A_p\cap(-B_p)=\varnothing\ ✓\ \text{且二者 ⊆ }(\mathbb Z/p^2)\setminus\{0\}\ ✓）$$
$$\textbf{引理 5 ⭐⭐（新 ✓ 严格 ✓）}：\ \boxed{A(p^2)\,B(p^2)\ \ge\ |A_p|\,|B_p|\ \ge\ |A_p+B_p|\ =\ p^2-1}$$
$$\qquad\text{证 ✓}：|X+Y|\le|X||Y|\ ✓\ \text{（经典 ✓）＋ 引理 3 ✓}$$

## §3 ⭐⭐⭐ 条件性矛盾（✓ 本轮主产出 ✓）

$$\textbf{① 局部下界 ✓}：\text{设 }A(X)\sim c_AX^\alpha,\ B(X)\sim c_BX^\beta\ ✓；\text{引理 5 取 }X=p^2\ \Longrightarrow c_Ac_Bp^{2(\alpha+\beta)}\ge p^2-1\ \Longrightarrow\ \boxed{c_Ac_B\ge1}$$
$$\textbf{② 全局上界 ✓}：\text{唯一性 ⟹ 双射 ✓}\ \{a+b:a\in A,b\in B\}=\mathbb N_0\ \text{上之 }S\ ✓；$$
$$\qquad|S\cap[0,M]|=\sum_{a\in A,a\le M}B(M-a)=\frac{6}{\pi^2}M+O(\sqrt M)\ ✓\ \text{（经典 ✓）} \Longrightarrow c_Ac_B\Gamma(\alpha+1)\Gamma(\beta+1)=\frac{6}{\pi^2}$$
$$\qquad\text{（}\Gamma(\alpha+1)\Gamma(\beta+1)\big|_{\alpha+\beta=1}=\frac{\pi\alpha(1-\alpha)}{\sin(\pi\alpha)}\in\left[\frac{\pi}{4},\,1\right]\ ✓,\ \text{最小在}\ \alpha=\beta=\tfrac12\ ✓）$$
$$\Longrightarrow\ \boxed{c_Ac_B=\frac{6/\pi^2}{\Gamma(\alpha+1)\Gamma(\beta+1)}\le\frac{24}{\pi^3}=0.77404<1}\ \Longrightarrow\ \textbf{与 ① 矛盾 ✗✓✓}$$
$$\boxed{\textbf{数值核 ✓}：\frac{6}{\pi^2}=0.60793<\frac{\pi}{4}=0.78540\ \text{—— 密度 < 局部禁阻壁垒 ✗}}$$
$$\text{即 ✓}：\text{① 说"因子【必须够大】"✓（覆盖够多剩余类 ✓）；② 说"因子【不够大】"✗ —— }\textbf{而矛盾由【密度常数】与【}\pi/4\text{ 壁垒】之不等式给出 ✓✓}$$

## §4 结论与**诚实边界**（✓ 这一节比结论重要 ✓）

$$\textbf{结论 ✓}：\text{P-SF 在【正则增长假设】下}\ \textbf{【成立 ✓】} \Longrightarrow M\ \text{在}\ \{0,1\}[[x]]\ \text{中不可非平凡 Cauchy 分解 ✓}$$
$$\text{⇒ }\textbf{（在 D1-B\* 的意义上 ✓）}\ \mu^2\ \text{不可由该类分解产生 ✓}$$
```
⚠️ **边界一 ✗**：§3 用了【正则增长假设 A(X) ~ c_A X^α ✓】—— **未证 ✗**（α,β 可能不存在 ✓；真实情形需 [0,1]-指数或上下密度 ✗）
   ⟹ **P-SF ＝ 条件性成立 ✓，未证明 ✗**
⚠️ **边界二 ✗**：**严格可得的只有引理 1–5 ✓**；只用它们（不用增长假设）时 ✓：A(M)B(M) ∈ [0.6079M, 1.2158M] ✓ —— **互相【不矛盾】✗** ⟹ **矛盾【必须】靠更细的渐近 ✓**（这正是缺口所在 ✓）
⚠️ **边界三 ✗**：引理 3 的 S_p = (ℤ/p²)\{0} 依赖"AP 中平方自由数正密度 ✓"（Mirsky 型 ✓）—— **须对象固定 ✗**（依组件 2 ✓）
⚠️ **边界四 ✗**：本轮**【未】触及一般乘法残差 F ≠ 1 ✗**（您 §10 的推广目标 ✓）—— 只做了 F = μ² ✓
⭐ **本轮不声称**：P-SF 已证 ✗｜M 不可约已证 ✗｜D1-B\* 已死 ✗
```

## §5 下一步（✓ 唯一具体靶 ✓）

$$\boxed{\textbf{攻【正则增长假设】✗}}\ —— \text{即：}\text{化 }A(X)\sim c_AX^\alpha\ \text{为【无需假设】的形式 ✓；}$$
$$\qquad\text{路线 ✓：用【上下密度】＋【平移铺砌的局部均匀性 ✓】替代 α,β —— }\text{若成功 ✓ ⟹ P-SF 无条件 ✓ } \Longrightarrow \textbf{真正的结构性 NO-GO ✓}$$
$$\qquad\text{（}\text{您 §10 的推广 ✓：}\text{把 }\mu^2\ \text{换成一般乘性 }F\ne1\ ✓\ \text{并按 }F(p^e)\ \text{的局部变化造禁阻 ✗ —— 待 P-SF 无条件后 ✓）$$
