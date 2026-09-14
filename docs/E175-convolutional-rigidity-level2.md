# E175 · ⭐⭐⭐⭐⭐ **卷积刚性 · 第 2 阶终审：谱因子化【成立 ✓】但二级证书【等价于唯一性 ✗】⟹ 第 2 阶判**死**✗**
> 依唐先生 2026-09-14 14:35 裁定 ✓（**转主线 ✓；不作形式登记 ✓；逐级给活/死 ✓；防"渐近回退密度"✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；零新数值 ✓；未跑 Lean ✓

---

## §0 您给的对象（✓ 照录 ✓）

$$r:=\mathbf 1_A*\mathbf 1_B\ ✓,\qquad r(n)\ge1_S(n)\ ✓,\qquad r(n)=0\ (n\notin S)\ \Longrightarrow\ \operatorname{supp}r=S\ ✓$$
$$\textbf{二阶相关 ✓}：C_r(h)=\sum_d C_A(d)\,C_B(h-d)\ ✓,\qquad C_A(d)=|A\cap(A+d)|\ ✓,\quad C_B\ \text{同 ✓}$$
$$\textbf{与 }S\ \text{自身相关比较 ✓}：C_S(h)=\sum_n\mu^2(n)\mu^2(n+h)\ ✓\ \text{（Hardy–Littlewood 奇异级数 ✗）}$$

## §1 ⭐ 本轮【可证】的两条（✓ 新 ✓）

$$\textbf{(1) 二阶恒等式（精确 ✓）}：\ \boxed{C_r=C_A*C_B}\ ✓\ \text{—— 一般 }C_{r}=\sum_{d+e=h}C_A(d)C_B(e)\ ✓$$
$$\qquad\text{证 ✓}：\sum r(n)r(n+h)=\#\{(a,b,a',b'):a+b+h=a'+b'\}=\#\{(d,e):d+e=h\}\ \text{型因子化 ✓（令 }d=a'-a,e=b'-b\ ✓）$$
$$\textbf{(2) 谱因子化（✓ 更可用 ✓）}：\ \boxed{|\hat r|^2=|\hat A|^2\,|\hat B|^2}\ \text{（截断版精确且【有限 ✓】）}$$
$$\qquad\Longrightarrow\ ⭐\ \boxed{\textbf{平方自由指示函数的【谱测度】必须分解为两个【0/1 集谱测度的乘积】✗}}$$
$$\qquad\text{（}\textbf{这是【全局 ✓ 非局部 ✓】约束 —— 不属局部／CRT／密度／提升／aliasing 任一类 ✓）}$$

## §2 ⭐⭐ 第 2 阶的**证书候选**及其判定（✓ 按您的判据 ✓）

$$\text{唯一性 ⟹ }r\le1\ \Longrightarrow\ \sum_n r(n)^2=\sum_n r(n)\ \Longrightarrow\ \boxed{\int|\hat A|^2|\hat B|^2=\Bigl(\int|\hat A|^2\Bigr)\Bigl(\int|\hat B|^2\Bigr)}\ ✓$$
$$\qquad\text{即 }：\text{谱测度 }\mu_A:=|\hat A|^2/|A|\ ✓,\ \mu_B\ \text{满足}\ \int fg=\int f\cdot\int g\ \text{型"不相关" ✗}$$
$$\textbf{判定 ✓}：\ \boxed{\textbf{该等式【等价于】唯一性（}r\le1\text{）本身 ✗}}\ \text{—— 理由 ✓}：\sum r^2=\sum r\iff r\in\{0,1\}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{它【不产生】独立于唯一性的新不等式 ✗} \Longrightarrow \textbf{第 2 阶的"有限证书"失败 ✓}$$
$$\text{（}\textbf{唯一剩下的第 2 阶希望 ✓}：\text{把 }\mu_r=\mu_A*\mu_B\ \text{的【因子结构 ✗】与 }C_S(=\mu^2\ \text{的自相关 ✗})\ \text{的【奇异级数结构 ✗】比较 —— }$$
$$\qquad\text{但奇异级数 }\mathfrak S(h)=\prod_p\sigma_p(h)\ \text{的因子化是【乘法型（}h\text{-方向）✗】；而谱因子化是【频率卷积型 ✗】；}$$
$$\qquad\text{二者若要比较，}\textbf{只能经渐近 ✗} \Longrightarrow\ \text{按您的防回退判据 ✓ ⟹ }\textbf{掉回密度路线 ✗ ⟹ 第 2 阶判【死 ✗】}}）$$

## §3 ⭐⭐⭐ 第 3 阶的具体形式（✓ 下一级，未分析 ✓）

$$\text{唯一性给出【整族】恒等式 ✓}：\ \sum_nr(n)^k=\sum_nr(n)\quad\forall k\ge1\ ✓\quad（r\in\{0,1\}\ ✓）$$
$$\qquad\text{但【展开】不同 ✓}：k=2\ \text{展开为 }C_A*C_B\ ✓；\ k=3\ \text{展开为【三折卷积 ✗】}\ \Longrightarrow\ \textbf{作为 }C_A,C_B\ \text{的代数恒等式，k=3\ 【新 ✓】}$$
$$\boxed{\text{第 3 阶靶 ✓}：\text{写出 }k=3\ \text{的展开，检查是否蕴含 }C_A,C_B\ \text{的【有限三阶关系 ✗】，}\text{并与 }S\ \text{的三点相关比较 ✗}}$$
$$\qquad\text{（}\textbf{防回退检查 ✓}：\text{若第 3 阶也只能给出渐近 ✓ ⟹ 同样判死 ✗ ⟹ 整类封 ✗}）$$

## §4 边界（✓）

```
✅ **(1)(2) 皆【精确 ✓ 可证 ✓】；(2) 已用截断版 ✓ 使一切量【有限 ✓】**
✅ **零新数值 ✓；未用 RH ✓；未涉 ζ 解析 ✓（仅提到 Hardy–Littlewood 结构名 ✓，未用其值 ✓）**
⚠️ **① 判定"等价于唯一性"是【逻辑 ✓ 严格 ✓】，非估计不足 ✗**
⚠️ **② 第 2 阶判死不等于整类死 ✗** —— 第 3 阶【未分析 ✓】
⚠️ **③ 本档不声称原命题不可证 ✗**
⭐ **净产出 ✓**：① **二阶恒等式 }C_r=C_A*C_B$ ✓**；② ⭐ **谱因子化 }|\hat r|^2=|\hat A|^2|\hat B|^2$ ✓（新全局约束 ✓）**；
   ③ ⭐ **第 2 阶【判死 ✓】且理由是【等价于唯一性 ✗】（非估计弱 ✓）**；④ **第 3 阶具体靶 ✓ ＋ 防回退检查 ✓**
```

## §5 一句话（✓）

$$\boxed{\text{第 2 阶：}\textbf{谱因子化成立 ✓（新全局约束 ✓），但二级证书【等价于唯一性 ⟹ 判死 ✗】；}\text{第 3 阶（三折卷积）待攻 ✗}}$$
