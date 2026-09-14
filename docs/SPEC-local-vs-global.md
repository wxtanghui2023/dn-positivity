# 📘 **局部可满足性与全局障碍：一个可复用排除框架**
### （(甲) 产物正式合并版 —— 定义问题 → 四层审计 → 局部路线失效判据 → 非局部搜索入口）

> 依唐先生 2026-09-14 14:14 裁定 ✓（**Q1 合并 ✓；Q2 标题采用本名 ✓；Q3 作为下轮【入口闸门】✓**）
> 方法论核心章节 ＝ `docs/AUDIT-local-vs-global-satisfiability.md` ✓（本档为**外壳与索引** ✓，不复制其正文 ✓）
> 状态 ✓：**E141–E171 局部路线 CLOSED ✓；原问题【未】CLOSED ✗**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## §1 问题（一般形式）

$$\text{设 }S\subseteq\mathbb N_0\ \text{由【局部（模）条件】定义}\ ✓:\ S=\{n:\forall p,\ n\bmod p^2\in S_p\}\ ✓\qquad\text{问}\ \exists\,A,B\ \text{非退化使}\ S=A\oplus B\ ✓$$
$$\text{特例 ✓}：S=\text{平方自由数}\ ✓（S_p=G_p\setminus\{0\}\ ✓）$$

## §2 ⭐ 核心结论（方法边界，**非**结构障碍）

$$\boxed{\textbf{局部有限模结构}\ \not\Rightarrow\ \textbf{全局加法分解障碍}}$$
$$\boxed{\text{local feasibility}+\text{multiplicative CRT compatibility}+\text{sieve density}\ \not\Rightarrow\ \text{global additive-decomposition obstruction}}$$
$$\boxed{\textbf{NO-GO 不是"还没找到" ✗，而是这些工具【原则上】看不到整体性障碍 ✗}}$$

## §3 方法论核心章节（四层审计 —— 详见 AUDIT ✓）

$$\text{L1 有限模层 ✓}：\text{单 }p\ \text{可满足 ✓（}p=3:\ 3726\ \text{解 ✓）}\ \big|\ \text{L2 乘积／CRT 层 ✓}：\textbf{乘积解自动提升 ✓}\ \big|\ \text{L3 筛法层 ✓}：\textbf{误差吞主项／相容 ✗} \big|\ \text{L4 提升层 ✓}：\textbf{提升 ⟺ 全局条件 ✗（无新判据 ✓）}$$
$$\textbf{失败链 ✓}：\text{单 }p\to\textbf{可满足 ✓}\ |\ p=2\to\textbf{强刚性不矛盾 ✗}\ |\ \text{CRT}\to\textbf{自动提升 ✓}\ |\ \text{筛法}\to\textbf{不矛盾 ✗}\ |\ \text{跨 }p\ \text{提升}\to\textbf{等价原命题 ✗}$$

## §4 ⭐⭐ 变量错位（唐先生 ✓）＋ 本轮细化（E172 ✓）

$$S=A+B\iff\begin{cases}A+B\subseteq S&\text{(avoidance —— 四层审计【只打穿这一侧 ✓】)}\\ S\subseteq A+B&\text{(coverage —— 此前【完全未触碰 ✓】)}\end{cases}$$
$$\textbf{本轮细化 ✓（E172 引理 C ✓）}：\text{coverage 还要再分两层}\ ✗：$$
$$\qquad\boxed{\text{【模覆盖 ✓】}A_M+B_M=S_M\ \forall M\ ✓\ \text{（局部＋乘积提升即可 ✓，}E169/E170\ \text{已证恒可满足 ✗）}}$$
$$\qquad\boxed{\text{【精确覆盖 ✗】}S\subseteq A+B\ \text{（整数级 ✓）}\ —— \textbf{模覆盖【不蕴含】精确覆盖 ✗（局部—整体原理在加法同余问题中一般失效 ✗）}}$$
$$\Longrightarrow\ \textbf{障碍就住在这条缝隙里 ✓ —— 而四层框架【永远看不到】它 ✗}$$

## §5 入口闸门（✓ 任何新候选先过此门 ✓）

```
Local → CRT → Density → Lift  四层【全部封闭】
⟹ 候选 M-模／p^k-模／筛／局部密度／CRT 拼接：**【直接 NO-GO ✗】不再投入推导时间 ✓**
⟹ 合法性检查脚本 ✓：`scripts/nogo_gate.py`（双重轨：对象名 ＋ 术语 ✓）
```

## §6 非局部搜索入口（✓ 下轮起点 ✓）

$$\boxed{\textbf{问 ✓}：\operatorname{supp}(\mathbf 1_A*\mathbf 1_B)=S\ \text{—— 是否存在【全局卷积障碍 ✗】？}}$$
$$\qquad r_{A,B}(n)=\sum_{a+b=n}\mathbf 1_A(a)\mathbf 1_B(b)\ ✓\qquad\text{原命题 ⟺ }r_{A,B}(n)\ge1\iff n\in S\ ✓$$
$$\textbf{E172 已给出三条【框架外】可用工具 ✓}：\ \text{① 唯一性 ⟺ 差集互斥 ✓}\ \big|\ \text{② }S-S=(A-A)+(B-B)\ \text{精确 ✓}\ \big|\ \text{③ 模覆盖}\ne\text{精确覆盖 ✓}$$

## §7 边界（✓）

```
✅ **AUDIT 为核心章节 ✓；本档不复制其内容 ✓（单一真相源 ✓）**
⚠️ **不声称原命题不可证 ✗**；只声称四层工具看不到障碍 ✓
⚠️ **框架不适用须标注 ✓**：局部结构非完全乘性／某模数局部解不存在／S 含非局部定义成分 ✓
```
