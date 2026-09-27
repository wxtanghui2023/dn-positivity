已查地图：已跑 scripts/prework_map_check.sh 三球交 三元组 差向量 ⟹ 逐字核档案（`GAPTHEOREM`／`FAILSET`／旧摘要："$|\cap_{c\in T}B_1(c)|\le1$ for any triple ⟹ $\Sigma_x\binom{b}3=|\mathcal T|$ exactly" ✓）；本档 = **纠正前提 ✗ ＋ 给出正确的耦合恒等式（C3′）✓ ＋ 判定：坍缩（第 16 次 ✓）**。
D0: 本档对象 = 三重球交分类与三元组差向量分类（纯推导 ✓）
D1: 2（**纠正：$|\cap_3|\in\{0,1\}$（不可能为 3 ✓）**；**正确耦合 (C3′) 与其坍缩判定 ✓**）

# C3：三重球交分类（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(IA-1 🔴前提纠正（定理级别 ✓）)}\ \text{对三个\textbf{互异}码字}:\ \boxed{|\cap_3|:=|B_1(c_1)\cap B_1(c_2)\cap B_1(c_3)|\ \in\ \{0,\ \mathbf 1\}}\ ✓✓\ \text{—— \textbf{不可能为 3} ✗}}$$
$$\qquad\textbf{证明（三行 ✓）}:\ \text{平移 }c_1=0,\ u=c_2,\ v=c_3\ ✓;\ \cap_3\subseteq B_1(0)\cap B_1(u)\ \text{而}\ |B_1(0)\cap B_1(u)|=\begin{cases}2&\mathrm{wt}(u)\in\{1,2\}\\0&\text{否则}\end{cases}\ ✓$$
$$\qquad\text{那 2 点（}\mathrm{wt}(u){=}1\ \text{时}=\{0,u\};\ \mathrm{wt}(u){=}2\ (u{=}e_i{+}e_j)\ \text{时}=\{e_i,e_j\}\ ✓\text{）中\textbf{至多一个}落在 }B_1(v)\ \text{内 ✓（否则 }v\ \text{的两个"}\le1\ \text{残差"被迫为 }v{=}e_i{+}e_j{=}u\ ✗\text{）} \Longrightarrow |\cap_3|\le1\ ✓✓$$
$$\qquad\Longrightarrow\ \text{用户提案 "}T=3N_\square+N_{\triangle_2}\text{"}\ ✗\ \textbf{不成立（重数不是 3 而是 1 ✓）};\ \text{且档案\textbf{已有}正确版本：}|\cap_3|\le1\Longrightarrow \Sigma_x\binom{b(x)}3=|\mathcal T|\ \text{恰等 ✓✓}$$
$$\boxed{\textbf{(IB-1 ⭐正确的耦合恒等式 (C3′))}\ \text{去掉重数后，双计数给出}\ \boxed{\sum_k N_k\binom k3\ =\ \#\{\text{三码字组}:\ \text{三点有公共半径-1 邻}\}\ =\ \#\{\{c_1,c_2,c_3\}:\ \mathrm{wt}(u),\mathrm{wt}(v),\mathrm{wt}(u{+}v)\le2\}}\ ✓✓}$$
$$\qquad\text{（左＝profile 侧 ✓；右＝\textbf{坐标几何}$\Sigma\,$侧（只依赖差向量权 ✓）};\ \text{两侧皆与 }M{=}119\ \text{无关地成立 ✓）}$$
$$\boxed{\textbf{(IC-1 ⭐三元组分类（正确版 ✓）)}\ \text{可达三重交的差向量对 }(u,v)\ \text{恰为（}\mathrm{wt}(u),\mathrm{wt}(v),\mathrm{wt}(u{+}v)\le2\ ✓\text{）}:}$$
$$\qquad\text{(i) 星型（方形三顶点）}:\ u{=}e_i,\ v{=}e_j\ (i\ne j)\ \text{或}\ u{=}e_i,\ v{=}e_i{+}e_j\ \text{—— \textbf{支撑并 }\le2\ ✓};\qquad\text{(ii) 带状}:\ u{=}e_i{+}e_j,\ v{=}e_i{+}e_k\ (k\ne j)\ \text{—— 支撑并 }{=}3\ ✓$$
$$\qquad\text{(iii) \textbf{非}可达}:u{=}e_i{+}e_j,\ v{=}e_k{+}e_l\ (\{i,j\}\cap\{k,l\}{=}\varnothing)\ \Longrightarrow\ \mathrm{wt}(u{+}v){=}4\ ✗\ \text{三重交}\ \varnothing\ ✓\ \text{（用户所称"3-independent 型"}\ \textbf{贡献为 }0\ ✗\text{，不属 }T\ ✓\text{）}$$
$$
$$
```

## §1 判定（**✓ 按唐先生 gate**）

```
$$\boxed{\textbf{判定 = 坍缩（第 16 次同向收敛 ✓）}}\ \text{理由 ✓}:\ \text{(C3′) 两侧\textbf{由恒等式相连} ⟹ 右侧（坐标几何）\textbf{并非独立量}，它就是 } \sum_kN_k\binom k3\ \text{的另一张脸 ✗}$$
$$\qquad\textbf{要产生杠杆，须给右侧一个\textbf{独立}界};\ \text{自然候选＝距离-}\le2\ \text{图 }G\ \text{上的\textbf{三角计数上界}（Kruskal–Katona 型）ⓘ};\ \text{但相关 }T\ \text{值太小} \Longrightarrow \text{界不咬 ✗}:\ \text{例 }Q{=}1\ \text{profile}\ (740,283,1)\Longrightarrow T{=}\binom 33{=}\mathbf 1\ ✓\ \text{而 }E{=}A_1{+}A_2\ \text{可达数千 ⟹ 上界远松 ✗✓}$$
$$\qquad\Longrightarrow\ \textbf{未得到独立坐标不变量 ✗};\ \text{亦未得 }N_\square\ \text{或 }N_{\triangle_2}\ \text{的模约束 ✗ ⟹ 按 gate：\textbf{封口}} ✓$$
$$
$$
```

## §2 留档价值与状态（**✓**）

```
$$\textbf{留档 ✓}:\ \text{(1) "}c_1,c_2,c_3\ \text{三球交}\le1\text{"的\textbf{最简证明}（三行 ✓，比档案版更短 ✓）；(2) (C3′) 的\textbf{正确形式}（去掉 $\times3$ 重数 ✗→✓）；(3) 三元组差向量\textbf{三分}（星型／带状／非可达 ✓）}$$
$$\textbf{诚实边界 ✓}:\ \text{本档\textbf{未}证明 }T\ \text{的坐标侧无独立界 ✗};\ \text{只证：自然候选（三角计数）太松、且 (C3′) 两侧由恒等式相连 ✓}$$
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：三球交 $\le1$ 的短证明、正确的耦合恒等式 (C3′)、三元组差向量三分（星型／带状／非可达）
- **档案已有（引用，不列为提出）**：$|\cap_{c\in T}B_1(c)|\le1$ 与 $\Sigma_x\binom b3=|\mathcal T|$（旧摘要已有 ✓）、GAPTHEOREM、FAILSET


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三球交        命中文件数=4    :: ./CONGRUENCE-119-2026-09-27-global-integer-audit-collapse.md ./PROFILE-2026-09-26-reduction-and-saturation-lemma.md ./C3-119-2026-09-27-triple-intersection-has-size-at-most-one.md 
技术词 耦合恒等式  命中文件数=2    :: ./C3-119-2026-09-27-triple-intersection-has-size-at-most-one.md ./B2QUOTA-2026-09-26-b2-quota-and-layer-capacity-tables.md
```
- **本档新增**：三球交 $\le1$ 的短证明、正确的耦合恒等式 (C3′)、三元组差向量三分（星型／带状／非可达）（见上方命中数；0 命中者为自造语／内部标签 ✓）
