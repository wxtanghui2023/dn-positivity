# E183 · ⭐⭐⭐⭐ **T2-a 判决：两条具体路线【判死 ✗】**（一阶计数 ✗｜δM 超额增长 ✗）**＋ 整数级精确等式 ✓ ＋ 投影刚性**（v1 被数值否证 ✗ → 修正版通过 ✓）
> 依唐先生 2026-09-14 16:08 裁定 ✓（**打 T2-a，但不得再用密度冲突 ✗；若证不出 δM 级超额增长则立即判死 ✗**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓；数值仅**精确整数核对**（平方自由筛 ✓，≤4×10⁵ ✓）

---

## §0 采纳修正（✓ 唐先生正确 ✓）：一阶计数【永不可能】产生矛盾 ✗ —— 封口 ✓

$$\text{覆盖所需 ✓}：|A_M|\cdot|B_M|\ \ge\ |H_M|\approx0.608M\ ✓\qquad\text{Kneser ✓}：|A_M|+|B_M|\ \le\ 0.608M+1\ ✓$$
$$\textbf{兼容区显式 ✓}：\text{取 }|A_M|\approx|B_M|\approx0.78\sqrt M\ ✓\ \Longrightarrow\ \underbrace{|A_M|+|B_M|\approx1.56\sqrt M\ll0.608M}_{\text{满足 Kneser ✓}},\ \underbrace{|A_M||B_M|\approx0.608M}_{\text{满足覆盖对数 ✓}}$$
$$\Longrightarrow\ \boxed{\text{一阶计数／密度路线【原则上】不可能产生矛盾 ✗}}\ ✓\qquad\textbf{我上一轮"硬数只能由 }a\ge M\ \text{覆盖 ⟹ 与 }0.608M\ \text{冲突"的提法【撤回 ✗】}\ ✓（\text{唐先生判断 ✓}）$$

## §1 ⭐ 整数级精确等式（✓ 新且正确 ✓；唐先生 (6) 在 $[0,M)$ 上的正确形式 ✓）

$$C_M:=A_M+B_M\ ✓\qquad\Longrightarrow\qquad\boxed{\ C_M\cap[0,M)\ =\ S\cap[0,M)\ }\ ✓$$
$$\text{证 ✓}：\subseteq\ \text{因 }A_M+B_M\subseteq A+B\subseteq S\ ✓；\supseteq\ \text{因 }n\in S,\ n<M\ ⟹\ n=a+b,\ a,b\le n<M\ ⟹\ a\in A_M,b\in B_M\ ✓\ \blacksquare$$
$$\text{（}\textbf{注意 ✗}：\text{该等式【只】在 }[0,M)\ \text{上成立 ✓；在 }[M,2M)\ \text{上不成立 ✗}（\text{那里只要求"平方自由"✓，不要求被覆盖 ✓）—— 故 }|C_M|\ \text{可大于 }|H_M|\ ✓）$$

## §2 ⚠️ "δM 超额增长"路线**被退化解否证 ✗**（→ 依裁定：立即判死 ✗）

$$\text{退化解 ✓}：(\{0\},\ S)\ ✓\ \Longrightarrow\ C_M=B_M=S\cap[0,M)\ ✓\ \Longrightarrow\ \boxed{|C_M|=|A_M|+|B_M|-1}\ ✓（\text{整数和集下界}）\ \textbf{恰好取等 ✗}$$
$$\text{数值核对 ✓（精确筛 ✓）}：M=50:\ 31=1+31-1\ ✓\quad M=200:\ 122=1+122-1\ ✓\quad M=1000:\ 608=1+608-1\ ✓\quad（\text{差}=0\ ✓）$$
$$\Longrightarrow\ \boxed{\text{不存在普适 }\delta>0\ \text{使}\ |A_M+B_M|\ge|A_M|+|B_M|-1+\delta M\ ✗}\ ✓$$
$$\qquad\text{任何 }\delta\text{-型结论都必须额外使用"非退化（两侧无限 ✓）"—— 而目前【没有】把非退化转成可用量的手段 ✗}$$
$$\Longrightarrow\ \textbf{依唐先生裁定：T2-a 的 }\delta\text{-路线【判死 ✗】}\ ✓\qquad\text{（}\textbf{新认识 ✓}：\text{退化极值的存在说明"极小和集"与"覆盖"并不冲突 ✗）}$$

## §3 ⭐⭐ 投影刚性（2D 禁带 → 1D 覆盖 的刚性 ✓）：**v1 被数值否证 ✗ → 修正版通过 ✓**

$$\textbf{v1（我的错误版本 ✗）}：\text{我原以为"交叉型表示"}a<a',\ b>b'\ \text{会给出区间【内】的平方自由数 ⟹ 矛盾 ✗} —— \textbf{写反 ✗}：$$
$$\qquad a+b'=n-(b-b')<n\ ✓,\qquad a'+b=n'+(b-b')>n'\ ✓\ \Longrightarrow\ \textbf{交叉和落在区间【外】✗}\ \text{（不是内 ✗）}$$
$$\qquad\text{数值核对立即否证 ✗}：286\ \text{对相邻表示中 250 对被误判为"违规"✓ ⟹ 打印实例定位到方向写反 ✓}$$
$$\textbf{修正版 ✓（正确 ✓，并已通过数值 ✓）}：\text{设 }n<n'\ \text{为}\ S\ \text{中相邻元 ✓},\ g:=n'-n\ ✓;\ (a,b)\in R(n),\ (a',b')\in R(n')\ ✓；\ \Delta a:=a'-a\ ✓（\text{则恒有 }\Delta a+\Delta b=g\ ✓）$$
$$\boxed{0<\Delta a<g\quad\textbf{不可能}\ ✗}\qquad\text{即}\quad \Delta a\le0\ \ \text{或}\ \ \Delta a\ge g\ ✓$$
$$\text{证 ✓}：0<\Delta a<g\ \Longrightarrow\ 0<\Delta b<g\ \Longrightarrow\ a'<a\ \text{不成立且}\ b'>b\ ⟹\ a'>a,\ b'>b\ ✓\ \Longrightarrow\ a'+b\in A+B\subseteq S\ \text{且}\ n<a'+b<n'\ ✓\ \perp\ \blacksquare$$
$$\Longrightarrow\ \boxed{\textbf{三型分类 ✓}：\text{交换型}}(\Delta a<0\ \text{或}\ \Delta a>g)\ \big|\ \text{同 }a\ \text{型}(\Delta a=0)\ \big|\ \text{同 }b\ \text{型}(\Delta a=g)\ ✓$$
$$\textbf{数值 ✓}：286\ \text{对相邻表示 ⟹ 违规 }0\ ✓；\text{类型分布：交换型 }250\ ✓、\text{同 }b\ 32\ ✓、\text{同 }a\ 4\ ✓（\textbf{无严格嵌套 ✓}）$$

## §4 刚性的直接推论（✓ 但**不闭合 ✗**——诚实标注 ✓）

$$\text{① 沿 }S\ \text{任取表示 ✓}：a\ \text{坐标"只能下降／持平，或按}\ \ge\ \text{局部间隙 }g\ \text{跳升"✓}（b\ \text{坐标对称 ✓}；二者每步恰有一个"不升"✓）$$
$$\text{② 定义 }\alpha(n):=\min\{a:(a,n-a)\in R(n)\}\ ✓,\ \omega(n):=\max\ ✓\ \Longrightarrow\ \alpha(n')-\alpha(n)\notin(0,g)\ ✓,\ \omega\ \text{同 ✓}$$
$$\text{③ }\textbf{但三型都自相容 ✗}：退化解正好落在"同 }a\ \text{型"（}A=\{0\}\Longrightarrow\Delta a\equiv0\ ✓）\ ✓\ \Longrightarrow\ \boxed{\text{刚性本身【不足以】产生矛盾 ✗}}$$
$$\Longrightarrow\ \textbf{与唐先生预期相比 ✓}：\text{本轮只到"识别出投影刚性的正确形态 ✓"，\textbf{未到"刚性 ⟹ 矛盾 ✗"}\ —— 这一步仍 OPEN ✗}$$

## §5 剩余入口（✓ 本审判词 ✓）

```
(T2-c) **"非退化 ⟹ 矛盾"**：δ-路线未覆盖的空间 ✓
    ⭐ 新自由度 ✓：E181 §0 只推出 B ⊆ S 与 A + 1 ⊆ S ✓，**未推出 A ⊆ S ✗**
    ⟹ A 的元素可取 ≡ 0 mod ∏_{p≤P} p² ✓（对 p ≤ P 自动免除对 B 的约束 ✓；只要 a + 1 平方自由 ✓）
    ⟹ A 的局部富度与 B 的稀疏度【解耦】✗ ⟹ 与覆盖相撞？—— 未核 ✗
(T2-d) **直接构造**：A = {0} ∪ {a ≡ 0 mod 小素数平方, a+1 平方自由 ✓}；B = 覆盖所需者 ✓
    难点仍是覆盖"无自由度"✗（n 固定 ⟹ n − b 必须是合法 A 元 ✓）
```

## §6 边界（✓）

```
✅ 本轮判定：一阶计数路线【死 ✗】（兼容区显式 ✓）；δM 超额增长路线【死 ✗】（退化解取等下界 ✓）
✅ 新正确工具 ✓：整数级精确等式（[0,M) 上 ✓）；投影刚性修正版（三型分类 ✓，数值 0 违规 ✓）
⚠️ 投影刚性【未】导致矛盾 ✗；覆盖侧【仍 OPEN】✗；不声称不可能 ✗
⚠️ 我上一轮两处提法被否证 ✗：① "密度冲突"✗（§0 ✓）；② "嵌套引理 v1"✗（§3 ✓）
   —— **两处都是先被数值核对抓到** ✓（与"结果不理想先怀疑自己"一致 ✓）
⭐ 净产出 ✓：① 计数封口 ✓；② 整数级精确等式 ✓；③ δ-路线判死 ＋ 退化极值认识 ✓；
   ④ ⭐ 投影刚性正确形态（三型分类 ✓）；⑤ 唯一未开发自由度（A ⊄ S ✓）✓
```
$$\boxed{\text{T2-a 按您的判据【判死 ✗】；新工具＝整数级精确等式 ＋ 投影刚性（三型 ✓）；下一枪只能打 (T2-c)：用 }A\not\subseteq S\ \text{的新自由度 ✗}}$$
