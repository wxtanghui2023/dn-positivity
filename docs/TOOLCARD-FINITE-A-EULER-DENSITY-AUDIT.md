# 🧰 TOOLCARD · 有限 $A$ 的 Euler 密度审计（**解析版 EXACT NEGATIVE 判决器**）
> 建立 ✓ 2026-09-14 21:09（唐先生："以后任何有限 $A$ 一出现，先过这一关，再决定是否值得进入数值实验" ✓）
> 来源 ✓ E228（`docs/E228-terminal-density-audit-density-1-conjecture-dead.md`）｜配套 ✓ `ARCHIVE-E180-E228-finite-construction-arc-final.md` §层 III-b
> 定位 ✓ **通用审计工具 ✓**（非研究弧线 ✗）；**跑一趟 < 1 分钟 ✓，替代百万级窗口实验 ✓**

---

## 🔴 适用范围（顶部红框 ✓ 必读 ✓）

$$\boxed{\textbf{适用 ✓}：\text{【有限 }A\ \text{】＋【有限平移并集 }A+B(A)\ \text{】，}S=\text{平方自由数集 ✓}}$$
$$\boxed{\textbf{不适用 ✗}：\text{无限 }A\ ✗;\quad A=A(M)\ \text{随窗口增长 ✗};\quad \text{非平方自由目标集（未经验证的推广）✗}}$$
$$\qquad\textbf{理由 ✓}：\text{本卡的每一层都依赖【}A\ \text{有限】\ ⟹\ \sum_p\nu_p/p^2<\infty\ ⟹\ \text{Euler 积收敛到正值 ✓};\quad \text{平移并集的包含-排除仅 }2^{|A|}-1\ \text{项（有限 ✓）}$$

---

## §1 对象定义（层 1 ✓）

$$\boxed{B(A)=\bigcap_{a\in A}(S-a)=\{b\ge0:\ b+a\in S\ \ \forall a\in A\}},\qquad S=\{\text{squarefree positive integers}\}\ ✓$$
$$\qquad\text{覆盖集 ✓}：A+B(A)\ ✓（\subseteq S\ \text{自动成立 ✓}）;\qquad \text{残差 ✓}：E=S\setminus(A+B(A))\ ✓$$
$$\qquad\textbf{注意 ✓}：B(A)\ \text{已是【对 }A\ \text{的最大合法集 ✓】（E216 ✓）⟹ 无 "选更好 }B\text{" 的自由度 ✗$$

## §2 单交 Euler 密度（层 2 ✓）

$$\nu_p(A):=\big|\{a\bmod p^2:a\in A\}\big|\ ✓;\qquad \boxed{d(A):=\prod_p\Big(1-\frac{\nu_p(A)}{p^2}\Big)}\ ✓$$
$$\qquad\textbf{收敛性 ✓}：A\ \text{有限}\ \Longrightarrow\ \nu_p(A)\le|A|\ \Longrightarrow\ \sum_p\frac{\nu_p(A)}{p^2}\le|A|\sum_p\frac1{p^2}=0.4522\,|A|<\infty\ ✓$$
$$\qquad\Longrightarrow\ \prod_p(1-\nu_p/p^2)\ \text{【收敛到正值 ✓】（不会塌缩为 }0\ ✓）$$
$$\qquad\qquad d(A)=\delta\big(B(A)\big)\ ✓（\text{标准有限筛密度定理 ✓：有限 shift 集的平方自由交集为有限筛型 ✓）}$$

## §3 覆盖密度（层 3 ✓ 包含-排除）

$$\forall\,\varnothing\ne I\subseteq A\ ✓:\qquad \nu_p^{(I)}:=\big|\{a-a'\bmod p^2:\ a\in I,\ a'\in A\}\big|\ ✓;\qquad d_I:=\prod_p\Big(1-\frac{\nu_p^{(I)}}{p^2}\Big)\ ✓$$
$$\qquad\boxed{\delta\big(A+B(A)\big)=\sum_{\varnothing\ne I\subseteq A}(-1)^{|I|+1}d_I}\ ✓\qquad\big(\text{有限可加性 ✓，}2^{|A|}-1\ \text{项 ✓}\big)$$
$$\qquad\textbf{内部一致性自检 ✓（必做 ✓）}：|I|=1\ \text{的每一项必须 }=d(A)\ ✓（\text{因 }a+B\ \text{是 }B\ \text{的平移 ✓，密度不变 ✓）}$$
$$\qquad\textbf{基础对照 ✓}：\delta(S)=6/\pi^2=0.607927\ ✓;\qquad \boxed{R_\infty:=\frac{\delta(A+B(A))}{\delta(S)}}\ ✓$$

## §4 尾部精确性（✓ 可执行判决的关键 ✓ 必须实现 ✓）

$$\boxed{\ p^2>2\max A\ \Longrightarrow\ \nu_p^{(I)}=c_I:=\big|\{a-a':\ a\in I,\ a'\in A\}\big|\ \text{【精确 ✓】}\ }$$
$$\qquad\textbf{理由 ✓}：a-a'\in[-\max A,\max A]\ ⟹\ a-a'+\max A\in[0,2\max A]\subset[0,p^2)\ ⟹\ \text{【不同整数值 ⟹ 不同剩余 ✓】},\ \text{且 }\nu_p^{(I)}\ \text{与 }p\ \text{无关 ✓}（\text{恒等于不同差值个数 }c_I\ ✓）$$
$$\Longrightarrow\ \textbf{可执行 ✓}：\text{只需精确枚举 }\ p\le\sqrt{2\max A}\ \text{（有限 ✓）；其余素数用【严格解析 tail ✓】：}$$
$$\qquad\prod_{p>\sqrt{2\max A}}\Big(1-\frac{c_I}{p^2}\Big)\ \text{—— 由 }\ \sum_{p>X}p^{-2}\ \text{的精确值（可数值求到 }10^{-12}\ \text{✓）计算 ✓}$$
$$\qquad\Longrightarrow\ \textbf{本卡结果为【纯解析 ✓，无窗口误差 ✗】—— 这是它替代数值实验的根本原因 ✓✓}$$

## §5 硬判决（层 4 ✓ EXACT NEGATIVE）

$$\boxed{\delta\big(A+B(A)\big)<\delta(S)\ \Longrightarrow\ \lim_{M\to\infty}R_M=\frac{\delta(A+B(A))}{\delta(S)}<1\ \Longrightarrow\ \textbf{EXACT NEGATIVE}\ \🔒\ \text{（无需再跑窗口 ✗）}}$$
$$\qquad\textbf{判决流程 ✓}：$$
```
1. 算 d(A) = ∏(1−ν_p(A)/p²)                    → 得 δ(B(A)) 与比值 δ(B)/δ(S)
2. 对每个 I ⊆ A（2^|A|−1 个）算 d_I            → |I|=1 项必须 = d(A) ✓（自检）
3. 含排得 δ(A+B(A))；与 6/π² 比较              → 判 EXACT NEGATIVE ✓ / 或 δ=δ(S) ✓
4. 记录 R_∞ = δ(A+B(A))/δ(S)                   → 这是数值 R_M 的【真正解析极限 ✓】
```
$$\qquad\textbf{各情形解读 ✓}：$$
```
· δ(A+B(A)) < δ(S)  ⟹ EXACT NEGATIVE：∃ 正密度未覆盖集 ⟹ R_M↛1 ✗（终局 ✓）
· δ(A+B(A)) = δ(S)  ⟹ 【必要非充分 ✗】：只说明"密度意义下覆盖全部"✓；精确覆盖 S⊆A+B 仍需另行证明 ✗
· 若数值 R_M 上升 ⟹ 它收敛到 R_∞（上一条算出的数 ✓）而非必然到 1 ✓（E224→E228 的教训 ✓）
```

## §6 验证样例（✓ E228 实测 ✓ 用以自检实现 ✓）

$$\text{取 }A^*=900\{0,1,24,70,162,900\}\ ✓（|A^*|{=}6\ ✓,\ \max A^*{=}810000\ ✓,\ \sqrt{2\max A^*}\approx1273\ ✓）$$
```
δ(B)      = 0.465941          δ(B)/δ(S) = 0.7664  ← 与八尺度实测 0.7665 吻合到 4 位 ✓✓
δ(A*+B)   = 0.607853          δ(S) = 6/π² = 0.607927
R_∞       = 0.999878          δ(E)/δ(S) = 1.22e-4 > 0  ⟹ EXACT NEGATIVE 🔒
自检      : |I|=1 的六项全部 = 0.465941 = δ(B) ✓✓（实现正确性验证 ✓）
K_余项    : |K| ≈ 1e-6 量级（p≤1e6 枚举 ＋ 解析 tail ✓）
```
$$\qquad\textbf{耗时 ✓}：\text{单次判决 < 1 分钟 ✓（对比 E224 单尺度窗口扫描约 }10\ \text{分钟 ✗ 且需 }8M\ \text{内存 ✓）}$$

## §7 使用纪律与边界（✓）

```
① A 必须【有限】✓；若 A=A(M) 或无限 ⟹ 本卡【不适用 ✗】（须先证明有限性/极限交换 ✓）
② 目标集必须【平方自由数】✓；换其它局部定义集须重导 ν_p 与乘积收敛性 ✗
③ δ(A+B)=δ(S) 只给【密度覆盖 ✓】，不给【精确覆盖 ✗】—— 后者是本卡的能力边界 ✓
④ 结论只对该【具体 A】成立 ✓；不得外推为"所有有限 A 皆…" ✗
⑤ 与 RH/Goldbach 无逻辑连接 ✗；引用本卡不得暗示对二者的任何结论 ✓
⑥ 若 A 有限但 |A| 很大（如 >20）⟹ 2^|A| 项爆炸 ✗ ⟹ 需改用其它方法（如直接估计 δ(E) 上界）✓
```

## §8 引用与版本（✓）

```
来源     : E228（终局密度审计）✓；E224（长程数值对照 ✓）；E226（见证结构 ✓）
档案     : ARCHIVE-E180-E228-finite-construction-arc-final.md §层 III-b（定理形式 ✓）
主索引   : MASTER-STATUS-AND-CLOSURES.md §2.E（工具索引 ✓）＋ §2.H（弧线封口 ✓）
状态     : 🔒 已封口弧线的遗产工具 ✓；非研究弧线 ✗；不再扩展 E229 变体 ✗
```
$$\boxed{\textbf{一句话 ✓}：}\text{任何有限 }A\ \text{候选，先用本卡算 }d(A)\ \text{与含排 }2^{|A|}{-}1\ \text{项 ✓；若 }\delta(A{+}B(A))<\delta(S)\ \text{即可当场判 EXACT NEGATIVE 🔒（尾段靠 }p^2{>}2\max A\ \text{的精确性 ✓），无需再进数值实验 ✗}$$
