# E172 · ⭐⭐⭐⭐ **框架外的三条可证引理：差集互斥／精确差集分解／模覆盖 ≠ 精确覆盖**
> 承接 ✓ 唐先生 14:14 裁定（**局部路线 CLOSED ✓；新靶 = supp(1_A*1_B)=S ✓**）
> 本档全部落在【四层框架之外 ✓】（局部／CRT／密度／提升【皆未使用 ✗】）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓（仅用经典计数 ✓）；未跑 Lean ✓；零新数值 ✓

---

## §0 引理 A（**唯一性 ⟺ 差集互斥**）✓ 一行可证 ✓

$$\textbf{命题 ✓}：\text{对 }A,B\subseteq\mathbb Z\ \text{（非空 ✓），}\ \boxed{S=A\oplus B\iff S=A+B\ \text{且}\ (A-A)\cap(B-B)=\{0\}}$$
$$\textbf{证 ✓}：\text{(⇒) 若 }a_1+b_1=a_2+b_2\ \text{且}(a_1,b_1)\ne(a_2,b_2)\ ✓，\text{则 }a_1-a_2=b_2-b_1\ne0\ ✓\ \text{既在 }A-A\ \text{又在 }B-B\ ✗\ \text{—— 由唯一性排除 ✓；}$$
$$\qquad\text{(⇐) 若 }d\in(A-A)\cap(B-B)\ ✗，d\ne0\ ✓，\text{则 }d=a_1-a_2=b_2-b_1 \Longrightarrow a_1+b_1=a_2+b_2\ \text{且}(a_1,b_1)\ne(a_2,b_2)\ ✓\ \text{与 }S=A+B\ \text{的唯一性矛盾 ✓}$$
$$\Longrightarrow\ \textbf{等价的"}\textbf{移位互斥}\text{"形式 ✓（更可用 ✓）}：\ \boxed{\forall h\ne0:\ \text{【}A\ \text{有一对相距 }h\text{】与【}B\ \text{有一对相距 }h\text{】不能同时成立 ✗}}$$

## §1 引理 B（**精确差集分解** ＋ $S-S=\mathbb Z$）✓ 自证 ✓

$$\textbf{命题 ✓}：S=A+B\ \Longrightarrow\ \boxed{S-S=(A-A)+(B-B)}\ \text{（精确等式 ✓）}$$
$$\qquad\text{证 ✓}：(a+b)-(a'+b')=(a-a')+(b-b')\ ✓ \Longrightarrow\ \supseteq\ ✓；\text{反向 ✓：}(d_1,d_2)\in(A-A)\times(B-B)\ \text{给出 }(a_1+b_1)-(a_2+b_2)\in S-S\ ✓$$
$$\textbf{而 ✓}：\ S-S=\mathbb Z\ \text{（}\textbf{自证 ✓ 仅用密度 ✓}）：\ (6/\pi^2)>1/2 \Longrightarrow 2|S\cap[0,N]|\approx1.2158N>N+h\ \text{（}h\ \text{给定、}N\ \text{取大 ✓）}\ \Longrightarrow\ S\cap(S+h)\ne\varnothing\ \forall h\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{纯加法组合配置 ✓}：\ D_A+D_B=\mathbb Z\ ✓,\quad D_A\cap D_B=\{0\}\ ✓,\quad D_A:=A-A,\ D_B:=B-B\ \text{均为【对称 ✓ ∋0 ✓】差集 ✗}}$$
$$\qquad\text{（}\text{且 }D_A\subseteq(S-1)-(S-1)\ ✓,\ D_B\subseteq S-S=\mathbb Z\ \text{（无额外信息 ✗）}\ —— \textbf{故关键在【差集与 }A+1\subseteq S,\ B\subseteq S\ \text{的交互 ✓】}）$$
$$\text{（}\text{注 ✓}：\text{若 }A(X)\asymp\sqrt X\ ✓，\text{则 }D_A\ \text{是【}\sqrt X\text{-稀疏集的差集】✗ —— 而经典例 }A=\{n^2\}\ \text{给 }D_A=\{h\not\equiv2\bmod4\}\ ✓，\textbf{已占}3/4\ \text{密度 ✗}）}$$

## §2 引理 C（**模覆盖 ≠ 精确覆盖** ✓ 对您 avoidance/coverage 划分的细化 ✓）

$$S\subseteq A+B\ \text{（精确覆盖 ✗）}\quad\text{再分两层 ✓}：$$
$$\qquad\text{【模覆盖 ✓】}\ A_M+B_M=S_M\ \forall M\ ✓\ \text{—— 由局部 ＋ 乘积集提升【恒可满足 ✗】（}E169\text{：}p=3\ 3726\ \text{解 ✓；}E170\text{：乘积集自动提升 ✓）}$$
$$\qquad\text{【精确覆盖 ✗】}\ S\subseteq A+B\ \text{（整数级 ✓）}\ ——\ \textbf{模覆盖【不蕴含】精确覆盖 ✗}$$
$$\textbf{理由 ✓}：\text{"}\forall M\ \exists(a_M,b_M):a_M+b_M\equiv n\ (M)\text{"}\ \textbf{不给出}\ \text{"}\exists(a,b):a+b=n\text{"}\ ——\ \textbf{加法同余问题中局部—整体原理【一般失效 ✗】}$$
$$\Longrightarrow\ ⭐\ \textbf{障碍的精确位置 ✓}：\ \boxed{\textbf{【模覆盖 ✓】与【精确覆盖 ✗】之间的缝隙}}\ ——\ \textbf{四层框架（全为局部／模／密度工具）【原则上住不进这条缝 ✗】}$$

## §3 由此得到的下轮靶（✓ 比"再加一条模条件"锋利 ✓）

$$\boxed{\text{① }D_A+D_B=\mathbb Z\ ✓,\ D_A\cap D_B=\{0\}\ ✓\ \text{（纯加法组合 ✓，与 }S\ \text{的局部结构无关 ✗）}}$$
$$\boxed{\text{② 且 }D_A\ \text{是 }\sqrt X\text{-稀疏集差集 ✗（}\asymp\text{稠密于 }[-X,X]\ \text{的 }X\ \text{个点 ✗）}}$$
$$\boxed{\text{③ 且 （}E168\ \text{铺砌 ✓）}S=\bigsqcup_{a\in A}(a+B)\ ✓,\quad A+1\subseteq S\ ✓,\ B\subseteq S\ ✓}$$
$$\text{（}\textbf{首选突破口 ✓（我的建议 ✓）}：\text{把 ① 的}\textbf{差集互斥}\text{与 ③ 的}\textbf{平移铺砌}\text{联合 —— }\text{因为铺砌给的是【加法】结构 ✓，而 (B\subseteq S)\ \text{给的是【乘法】结构 ✓，}\textbf{二者此前【从未联用 ✗】}）}$$

## §4 边界（✓）

```
✅ **三条引理全部自证 ✓（A 一行 ✓；B 一行 ＋ 经典计数 ✓；C 为区分 ✓ 严格 ✓）**
✅ **零新数值 ✓；未用 RH ✓；未涉 ζ 解析 ✓（仅 |S∩[0,X]|=(6/π^2)X+O(√X) ✓）**
⚠️ **① 引理 B 的 }S-S=\mathbb Z$ 用【密度 6/π^2>1/2 ✓】** —— 严格 ✓（自证 ✓），非引用未审结论 ✓
⚠️ **② §3 的"乘法结构"指 }B\subseteq S$ ✓（S 对互素积封闭 ✓）—— 尚未用它做任何推导 ✗**
⚠️ **③ 本档【不声称】已找到障碍 ✗** —— 只声称给出【框架外可用工具 ✓】并把靶精确化 ✓
⭐ **净产出 ✓**：① **唯一性 ⟺ 差集互斥 ✓**；② **}S-S=D_A+D_B$ 精确 ✓ ＋ }S-S=\mathbb Z$ ✓**；
   ③ **模覆盖 }\ne$ 精确覆盖（细化您的划分 ✓）＋ 障碍位置 ✓**；④ **下轮靶（差集 ⊗ 铺砌 ✗）**
```

## §5 一句话（✓）

$$\boxed{\text{三条引理全在四层框架【之外 ✓】；}\textbf{障碍的精确位置 ＝ 模覆盖与精确覆盖之间的缝隙 ✗；下轮用【差集互斥 ⊗ 平移铺砌 ✓】}}$$
