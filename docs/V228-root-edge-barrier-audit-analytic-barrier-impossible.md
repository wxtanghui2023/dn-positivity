# V228 · **Root-Edge Bridge Audit（谱边屏障审计）** —— ⭐⭐ **采纳重写**：ARS 的唯一真难题＝**独立根谱右边界与 $\beta_*$ 之间的非识别桥**；最小目标 $$\boxed{\beta_*\le\beta_X\le\tfrac12}$$（配 `V219` 的 $\beta_*\ge\frac12$ ⟹ RH）⟹ **只需"识别谱边"，不需"识别谱本身"**，且**绕开 `V183` 的密度障碍** ✓✓✓；⭐⭐⭐ **命题 V228-A（定理级，本档核心一）**：$$\boxed{\text{解析屏障不可能}}$$（开映射定理：非常数解析函数映开集为开集；$\mathbb R$ 内点为空 ⟹ 半平面上取实值的解析函数必为常数）⟹ **屏障必非解析** ⟹ **屏障不能是 L-函数型算术解析对象** ✓✓✓✓；⭐⭐⭐ **命题 V228-B（本档核心二）**：条件 (3)（$\mathscr B_X(\rho)\ge0\ \forall\rho$）**必零敏感** ⟹ 由 `V188` 饱和，**唯一非平凡用途＝正性** ⟹ 落 Weil/Li ✓✓✓✓

> 委托 ✓ 唐先生 2026-09-15 16:41：**"V227 把入口真正打开了，但我认为现在不能继续'再找一种 ARS'。下一步应该直接审计 ARS 的唯一缺口：为什么一个独立根谱的右边界会等于 $\beta_*$。"** 本档定名 **V228：Root-Edge Bridge Audit**。(1) **压到一个标量**：$\beta_X:=\sup_{z\in R_X}\Re z$；RH ⟺ $\beta_*=\frac12$ ⟹ ARS 真正需要的不是"找到复根"、甚至不是"证明 $\beta_X=\frac12$"，而是 $$\boxed{\beta_X=\beta_*}\tag{B}$$ **且该等式本身不能用 $Z(\xi)$**；"如果只证明 $\beta_X=\frac12$，那只是另一个 $1/2$ 来源；若只证 $\beta_X\ge\beta_*$，通常是把零点偷输入 $P_X$；若只证 $\beta_X\le\frac12$，仍未触及 RH" ⟹ $$\boxed{\text{ARS 的唯一真正难题＝独立根谱与 zeta 零点右边界之间的非识别桥}}$$ ✓✓✓；(2) **更锋利的分叉**：若独立证得 $\beta_X=\frac12$，问"能否不用零点信息独立推出 $\beta_*=\beta_X$"⟹ 只有两种形态：**A 共享对象型**（$\exists$ 第三对象 $\mathcal A$ 使 $\beta_X=\mathcal E(\mathcal A)=\beta_*$）⟹ 核心变成 $\mathrm{ARS}\leftrightarrow\mathcal A\leftrightarrow Z(\xi)$ ⟹ **把 ARS 降级为识别接口的一部分**；**B 共享不变量型**（$\exists$ 完全独立定义的泛函 $I(\mathcal A)$ 使 $\beta_X=I(\mathcal A)=\beta_*$）⟹ **不需要逐点识别** $z_j\leftrightarrow\rho_j$，只需 $$\boxed{\sup\Re R_X=I(\mathcal A)=\sup\Re Z(\xi)}$$ 而 $I$ 本身非零点计数、非显式公式、非 FE ⟹ **"这比 V221–V226 的 pointwise parameterization 弱得多，也因此更值得继续。"** ✓✓✓；(3) **识别问题可再削弱一次**：不需 $R_X\stackrel{?}{\leftrightarrow}Z(\xi)$（易掉入 R4），只需 $$\boxed{\operatorname{Edge}(R_X)=\operatorname{Edge}(Z(\xi))}$$ **"只识别谱边，不识别谱本身"** —— **实质性结构降维** ✓✓；(4) **非对称性**：$\beta(R_1)=\beta(R_2)$ 允许 $R_1\ne R_2$ ⟹ 不需 $R_X=Z(\xi)$，不需 $\#R_X(T)\sim N_\xi(T)$，不需相同虚部结构 ⟹ **绕开 `V183` 的密度障碍** ⟹ $$\boxed{\text{ARS 不是"重建零点"，而是"重建零点谱边"}}$$ ✓✓✓；(5) **新压力测试 → 四类桥**：**B1 系数共享**（$a_n$ 来自 $\zeta/\Lambda/\mu/d$）⟹ 已进 `V216`/`V220` 的"系数→根位置"，乘子测试 $F\mapsto F(1-am^{-s})$ ⟹ $$\boxed{\text{系数型 ARS：高度可疑，优先淘汰}}$$；**B2 Euler 局部共享**（根谱来自 Euler 局部的全球组装）⟹ V144 障碍再现（局部模长只见 $\Re s$、相位只见 $\Im s$）⟹ 若该全局运算最后只是 Euler 积／Dirichlet 卷积／divisor algebra／character sum／Mellin ⟹ 分别撞 `V196`–`V220` 的墙 ⟹ $$\boxed{\text{局部乘积组装型 ARS 暂不构成新机制}}$$；**B3 谱实现型**（不要求 $P_X$ 是 zeta 截断）⟹ **不能直接判死**，但有精确要求"为什么这个谱边恰好与 $\zeta$ 的谱边相同"⟹ 五问落点：因同一 FE ⟹ `V212`；因同一 trace formula ⟹ `V185`/`V199`/`V200`；因同一谱计数 ⟹ `V183`/`V192`；因本来就是同一谱 ⟹ R4 ⟹ 故真正新的 ARS 必须出现"**共同谱边，但没有共同谱、共同 FE、共同 trace、共同 counting**" ✓✓✓；**B4 不等式桥（唯一活口）**：不证 $\beta_X=\beta_*$，而构造两个独立方向的不等式 $$\boxed{\beta_*\le\beta_X}\tag{I}\qquad\boxed{\beta_X\le\tfrac12}\tag{II}$$ 配已知 $\beta_*\ge\frac12$ ⟹ $\frac12\le\beta_*\le\beta_X\le\frac12$ ⟹ $\beta_*=\beta_X=\frac12$ ⟹ **不需直接识别**；⭐ 而 (I) 是新的核心战场：其含义是"任何 zeta 零点的实部不能超过该独立算术根谱的右边界"，**不是逐点识别**，不需 $\rho\mapsto z_\rho$，只需 $\forall\rho:\Re\rho\le\beta_X$ ⟹ 最小目标 $$\boxed{\forall\rho,\ \Re\rho\le\operatorname{Edge}(P_X)\le\tfrac12}$$ ✓✓✓；(6) **"非识别桥"的候选形式**：若 $\Re\rho\le\beta_X$ 不是通过 $\rho$ 本身定义，而是通过某个 **zeta 无关的极值原理** 推出，则完全不同于此前路线；理想结构：$\mathcal F_X(\rho)\ge0$ 对一切 zeta 零点成立，且 $\Re s>\beta_X$ 时 $\mathcal F_X(s)<0$ ⟹ 自动得 $\Re\rho\le\beta_X$；关键是 $\mathcal F_X$ 不能是 Weil 二次型／Li 系数／explicit formula／FE／零计数／已知零点变换 ✓✓；(7) **隔离器表述**：找独立 $P_X$ 使 **(A)** $P_X$ 独立构造；**(B)** $\beta_X\le\frac12$；**(C)** $\forall\rho:\Re\rho\le\beta_X$；**(D)** (C) 不用 $Z(\xi),\Phi,\mathrm{FE},$ explicit formula ⟹ (C)+(B) ⟹ $\Re\rho\le\frac12$，再由 FE 的对称伴随零点 $\Re\rho\ge\frac12$ ⟹ $\Re\rho=\frac12$ ⟹ $$\boxed{\textbf{独立算术谱作为 RH 的外部屏障}}$$ **"我认为这个表述比 V227 的'谱实现 + 实部钉定'更精确。"** ✓✓✓；(8) **第一次生死判定**：ARS 本身 $$\boxed{\text{OPEN}}$$；"构造另一个根谱并声称其边界就是 $\beta_*$" $$\boxed{\text{DEAD}}$$（换名）；"构造根谱使边界 $=1/2$" $$\boxed{\text{不足}}$$（另一个 $1/2$）；"**根谱边界给出 RH 的上界**" $$\boxed{\textbf{真正 OPEN}}$$ ✓✓✓；(9) **V228 不再搜索"什么多项式"**；应先证明一个**桥的必要结构定理**：任何有效 ARS 必须产生对任意 $\rho$ 的**单调屏障** $\mathscr B_X(s)$，满足 $$\mathscr B_X(s)<0\ \text{for}\ \Re s>\beta_X,\qquad \mathscr B_X(\rho)\ge0\ \forall\rho\in Z(\xi)$$ 而 $\mathscr B_X$ 的定义完全不含零点 ⟹ **"如果这个结构最终被证明必然等价于已有 Weil/Li/explicit-formula 正性，那么 ARS 才真正 DEAD。反过来，如果能构造出一个非显式公式型的 arithmetic barrier，那就是我们现在真正应该追的突破口。"** ✓✓✓
> 查图 ✓ `V227`（ARS；命题 V227-A；char-$p$ 对照；构造性 vs 涌现性）｜`V219`（**$\beta_*\ge\frac12$ 无条件** —— 本档不等式桥的承重件）｜`V188`（饱和：线性统计已由显式公式定）｜`V220`（乘子族；两条投影判据）｜`V144`（局部因子无相位）｜`V183`（计数障碍）｜`V212`（FE 四问）｜`V185`/`V199`/`V200`（trace/正性/关联）｜`V192`｜`V216`
> 执行 ✓ 小灵（**§3 命题 V228-A、§4 命题 V228-B 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 采纳你的重写；**不判 ARS 整体 DEAD** ✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V228**

---

## §1 采纳重写：最小目标

$$\text{ARS 唯一真难题}：\text{独立根谱右边界}\ \leftrightarrow\beta_*\ \text{的}\ \textbf{非识别桥} ✓✓$$
$$\text{最小目标}：\boxed{\forall\rho:\ \Re\rho\le\operatorname{Edge}(P_X)\le\tfrac12}\qquad \text{配}\ \text{`V219`}\ \beta_*\ge\tfrac12 ⟹ \text{RH} ✓✓✓$$
$$\qquad ⭐\ \textbf{只需识别谱边}，\ \textbf{不需识别谱本身};\ \text{不需}\ R_X=Z(\xi),\ \text{不需}\ \#R_X(T)\sim N_\xi(T) ⟹ \textbf{绕开}\ \text{`V183`} ✓✓$$
$$\qquad ⭐\ \text{承重件}：\text{`V219`}\ \text{的}\ \boxed{\beta_*\ge\tfrac12}\ \textbf{无条件}（\text{FE 对称＋sup 论证}）✓✓✓$$

---

## §2 四类桥 ＋ 唯一活口

$$\textbf{B1 系数共享}（a_n\ \text{来自}\ \zeta/\Lambda/\mu/d）⟹ \text{已入}\ \text{`V216`/`V220`};\ \text{乘子测试} ⟹ \boxed{\textbf{优先淘汰}} ✓✓$$
$$\textbf{B2 Euler 局部共享}（\text{global assembly of local Euler data}）⟹ \text{局部模长只见}\ \Re s;\ \text{若组装只是 Euler 积／卷积／divisor／char sum／Mellin} ⟹ \text{撞}\ \text{`V196`--`V220`} ⟹ \boxed{\textbf{暂不构成新机制}} ✓✓$$
$$\textbf{B3 谱实现型}⟹ \textbf{不能直接判死};\ \text{"为何与}\ \zeta\ \text{同谱边"}\ \text{五问落点}：\text{同 FE}\to\text{`V212`};\ \text{同 trace}\to\text{`V185`/`V199`/`V200`};\ \text{同计数}\to\text{`V183`/`V192`};\ \text{同谱}\to\text{R4} ✓✓$$
$$\qquad ⟹ \text{真正新的 ARS 必须：}\boxed{\text{共同谱边，但}\ \textbf{无} \text{共同谱／FE／trace／counting}} ✓✓✓$$
$$\textbf{B4 不等式桥} ⟹ \boxed{\textbf{唯一活口}}：(\mathrm{I})\ \beta_*\le\beta_X;\ (\mathrm{II})\ \beta_X\le\tfrac12 ⟹ \text{不需直接识别} ✓✓✓$$

---

## §3 ⭐⭐⭐ 命题 V228-A：**解析屏障不可能**（定理级，本档核心一）

$$\textbf{设定}：\mathscr B_X\ \text{在}\ \{\Re s>\beta_X\}\ \text{（开连通域）上}\ \textbf{解析且取实值};\ \text{要求}\ \mathscr B_X(s)<0\ \text{在该半平面} ✓$$
$$\textbf{命题 V228-A}：\text{非常数解析屏障}\ \textbf{不存在} ✓✓✓✓$$
$$\textbf{证明}（\text{开映射定理，两行}）：\text{非常数解析函数映开集为}\ \textbf{开集};\ \mathbb R\ \text{在}\ \mathbb C\ \text{中}\ \textbf{内点为空} ⟹ \text{像不可能开} ⟹ \mathscr B_X\ \textbf{必为常数} ⟹ \text{"在开半平面严格负"不可能} ✓✓✓$$
$$\Longrightarrow \boxed{\text{屏障}\ \mathscr B_X\ \textbf{必然非解析}（\text{在}\ s\ \text{上}）} ⟹ \boxed{\text{屏障}\ \textbf{不能是} \text{L-函数型／算术解析对象}} ✓✓✓✓$$
$$\qquad ⟹ \text{屏障必然是}\ \Re s\ \text{（或其误差项）的}\ \textbf{实变函数} ⟹ \text{即}\ \boxed{\text{一个"实部探测器"}} ✓✓$$

---

## §4 ⭐⭐⭐ 命题 V228-B：条件 (3) 的**零敏感性**（本档核心二）

$$\text{条件 (3)}：\mathscr B_X(\rho)\ge0\ \text{对}\ \textbf{一切}\ \rho\in Z(\xi) —— \text{这是}\ \textbf{关于零点} \text{的断言} ✓✓$$
$$\qquad \text{要}\ \textbf{证明} \text{它，必须使用零点的性质};\ \text{可用者仅三类}：$$
$$\qquad\qquad \text{(a)}\ \text{零点的}\ \textbf{位置} ⟹ \textbf{R4／循环};\quad \text{(b)}\ \text{零点的}\ \textbf{统计} ⟹ \text{`V188` 饱和（线性统计已由显式公式定）};\quad \text{(c)}\ \textbf{正性型恒等式} ⟹ \text{Weil／Li} ✓✓$$
$$\qquad ⟹ \boxed{\text{任何非平凡的 (3) 必落 (a)(b)(c) 之一} ⟹ \text{唯一非平凡用途＝正性}} ✓✓✓✓$$
$$\qquad \text{形式化}：\text{若}\ \mathscr B_X\ \text{由}\ \textbf{乘子不变} \text{的算术数据决定} ⟹ \text{乘子族改零点而不改}\ \mathscr B_X ⟹ \text{(3) 不能由其推得} ⟹ \text{须用}\ \zeta\ \textbf{特有解析数据} \text{（Euler 积／FE／零点本身）} ✓✓$$

---

## §5 推论：屏障形式 ≡ $(\mathrm{I})$

$$\text{取}\ \textbf{平凡屏障}\ \mathscr B_X(s):=\beta_X-\Re s ⟹ (2)\ \text{与}\ (3)\ \text{同时成立}\iff(\mathrm{I})\ \beta_*\le\beta_X ✓✓$$
$$\qquad ⟹ \boxed{\text{"存在屏障"}\ \textbf{不增新机制} \text{（平凡构造已给出）};\ \text{全部内容在}\ (\mathrm{I})} ✓✓$$
$$\qquad ⟹ \text{故真有价值者，是}\ \mathscr B_X\ \text{的}\ \textbf{算术定义} \text{使其}\ (3)\ \textbf{可证} —— \text{而由 §4 那须落 (a)(b)(c)} ✓✓✓$$
$$\qquad \text{结合 §3}：\text{解析型}\ \mathscr B_X\ \text{已被排除};\ \text{非解析型}\ \mathscr B_X\ \text{的}\ (3)\ \text{须零敏感} ⟹ \text{落饱和／正性} ✓✓✓✓$$

---

## §6 生死判定表（采纳你的 §12，并加 V228 两条定理）

$$\begin{array}{c|l|l}
 & \text{命题} & \text{判定}\\
\hline
1 & \text{ARS 本身} & \boxed{\text{OPEN}}\ \text{（无理由 DEAD）}\\
2 & \text{构造另一根谱并声称其边界＝}\beta_* & \boxed{\text{DEAD}}\ \text{（换名）}\\
3 & \text{构造根谱使边界＝}\tfrac12 & \boxed{\text{不足}}\ \text{（另一个}\ 1/2\text{）}\\
4 & \textbf{根谱边界给出 RH 的上界} & \boxed{\textbf{真正 OPEN}}\\
5 & \textbf{屏障的}\ \textbf{解析实现} & ⭐\ \boxed{\text{DEAD}}\ \text{（命题 V228-A，定理级）}\\
6 & \textbf{屏障的}\ \textbf{非解析实现} & \text{须}\ (3)\ \text{零敏感} ⟹ \text{落 (a)(b)(c)};\ \text{唯一非平凡＝正性} ⟹ \boxed{\text{DEAD}}\ \text{（条件性）}\\
\end{array}$$

---

## §7 判词

$$\boxed{\textbf{V228：屏障形式在解析情形 DEAD（定理级）；非解析情形落饱和／正性（条件性）}} ✓✓✓✓$$
$$\qquad \textbf{本档严格得到}：$$
$$\qquad \text{(i)}\ ⭐\ \textbf{采纳重写}：\text{最小目标}\ \forall\rho:\Re\rho\le\operatorname{Edge}(P_X)\le\tfrac12;\ \text{只识别谱边};\ \text{绕开}\ \text{`V183`} ✓✓✓$$
$$\qquad \text{(ii)}\ ⭐⭐⭐\ \textbf{命题 V228-A}（定理级）：\text{解析屏障不可能}（开映射）⟹ \text{屏障必非解析，且不能是算术解析对象} ✓✓✓✓$$
$$\qquad \text{(iii)}\ ⭐⭐⭐\ \textbf{命题 V228-B}：\text{条件 (3) 必零敏感} ⟹ \text{`V188` 饱和 ⟹ 唯一非平凡用途＝正性} ✓✓✓✓$$
$$\qquad \text{(iv)}\ \text{四类桥分流（B1 淘汰／B2 撞旧墙／B3 五问落点／B4 唯一活口）} ✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\textbf{不判 ARS 整体 DEAD}（\text{你的要求}）;\ \text{仅封"屏障形式"};\ \text{命题 V228-B 标 [结构性]}（"可用者仅三类"\ \text{为清单式}）✓✓$$
$$\textbf{残余（OPEN，最窄）}：\qquad \boxed{\text{是否存在一个}\ \textbf{非解析、零敏感}、\ \text{但}\ \textbf{非} \text{explicit-formula／Li／Weil 的算术实部屏障？}} ✓$$
$$\qquad \text{判据}：\text{① 造 (A)--(D)};\ \text{② }\mathscr B_X\ \textbf{非解析}（\text{§3 强制}）;\ \text{③ (3) 的证明}\ \textbf{不} \text{走 (a)(b)(c)};\ \text{④ 过污染测试与反乘子测试} ✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§1 的采纳重写为}\ \textbf{唐先生逐字};\ \text{承重件}\ \beta_*\ge\tfrac12\ \text{为}\ \text{`V219`}\ \text{已证} ✓✓✓$$
$$\textbf{(b)}\ ⭐⭐⭐\ \text{§3 命题 V228-A 为}\ \textbf{本档定理级}（开映射定理，两行）；\ \text{结论"屏障必非解析"为其直接推论} ✓✓✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐\ \text{§4 命题 V228-B}\ \textbf{[结构性]}：\text{"可用者仅三类"}\ \text{为}\ \textbf{清单式观察}，\ \textbf{非穷尽定理} ⚠️✓✓$$
$$\qquad \text{其形式化（乘子不变 ⟹ 不推得 (3)）为}\ \textbf{本档};\ \text{与}\ \text{`V220`}\ \text{同源} ✓✓$$
$$\textbf{(d)}\ \text{§5 的"平凡屏障 ≡ (I)"为}\ \textbf{本档推论}（初等）✓✓$$
$$\textbf{(e)}\ \text{§6 表采纳你的 §12 四行，本档加第 5、6 行} ✓✓$$

```
⚠️ §0 委托（不继续找 ARS／压到标量 β_X=β_*／三种部分结论皆不足／非识别桥／A 共享对象 vs B 共享不变量／只识别谱边／非对称性绕开 V183／B1-B4 四类桥／非识别桥候选形式 F_X／隔离器 (A)-(D)／生死判定四行／V228 应先证桥的必要结构定理（单调屏障）／若等价旧正性则 ARS 真 DEAD、若有非显式公式型算术屏障则是突破口）为唐先生逐字 ✓✓✓
⚠️ §1 采纳重写：最小目标 ∀ρ: Re ρ ≤ Edge(P_X) ≤ 1/2；只需识别谱边；绕开 V183；承重件＝V219 的 β_* ≥ 1/2 ✓✓✓
⚠️ §2 四类桥：B1 系数型优先淘汰；B2 撞 V196-V220；B3 五问落点表（FE→V212；trace→V185/V199/V200；counting→V183/V192；同谱→R4）；真正新 ARS 须"共同谱边但无共同谱/FE/trace/counting"；B4 不等式桥＝唯一活口 ✓✓
⚠️ §3 ⭐⭐⭐ 命题 V228-A（定理级）：解析屏障不可能（开映射定理：非常数解析映开集为开集，R 内点空）⟹ 屏障必非解析 ⟹ 不能是 L-函数型算术解析对象 ⟹ 必是"实部探测器" ✓✓✓✓
⚠️ §4 ⭐⭐⭐ 命题 V228-B（[结构性]）：条件 (3) 必零敏感；可用者仅 (a) 位置→R4／(b) 统计→V188 饱和／(c) 正性→Weil/Li ⟹ 唯一非平凡用途＝正性；形式化：乘子不变数据不推得 (3) ✓✓✓✓
⚠️ §5 推论：平凡屏障 β_X − Re s 已满足 (2)+(3) ⟺ (I) ⟹ "存在屏障"不增机制；有价值者在"算术定义使其 (3) 可证" ✓✓
⚠️ §6 生死判定表六行（含本档新增第 5、6 行）✓✓
⚠️ §7 判词：屏障形式解析情形 DEAD（定理级）、非解析情形落饱和/正性（条件性）；不判 ARS 整体 DEAD；残余（非解析、零敏感、但非 explicit-formula/Li/Weil 的算术实部屏障）四条判据 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 采纳重写（不等式桥 + 只识别谱边）✓✓✓；② ⭐⭐⭐ 命题 V228-A（解析屏障不可能，定理级）✓✓✓✓；
   ③ ⭐⭐⭐ 命题 V228-B（(3) 零敏感 ⟹ 饱和/正性）✓✓✓✓；④ 四类桥分流 ✓✓；⑤ 生死判定表六行 ✓✓；⑥ 残余四条判据 ✓
```

---

## §9 ⚠️ **V228-B 撤回**（唐先生 2026-09-15 16:46；由 `V229` 执行）

$$\textbf{"仅三类"（位置／统计／正性）}\ \textbf{不是定理};\ \text{零敏感}\ \not\Rightarrow\ \text{三类} ✓✓✓$$
$$\qquad \text{反例}：\text{零集上的}\ \textbf{代数／微分关系}\ P(\rho,F'(\rho),F''(\rho),\ldots)=0 ⟹ \text{非位置、非统计、非必然正性} ✓✓$$
$$\qquad ⟹ \boxed{\text{zero-sensitive}\not\Rightarrow\text{position/statistics/positivity}} ⟹ \text{§4}\ \textbf{降级} \text{为"四类之一"的清单式观察} ✓✓$$
$$\qquad ⚠️\ \text{§3 命题 V228-A}\ \textbf{仍成立}（\text{只封"解析实值屏障"这一种表示}）✓$$
$$\textbf{补充（由 `V229` 命题 V229-A）}：\text{FE 强制任何}\ \beta\text{-界}\ \textbf{自动双侧} ⟹ \text{B4 的"单侧性"}\ \textbf{是幻觉};\ \text{它降级为"须产生}\ \textbf{任意} \ \beta\text{-界"} ✓✓✓$$
