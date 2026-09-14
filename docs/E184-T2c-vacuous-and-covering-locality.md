# E184 · ⭐⭐⭐⭐ **T2-c 判决：锁定形式【空泛 ✗ ⟹ 判死 ✗】｜新得【覆盖局部性引理 ✓】（取等 ✓）｜不可能侧三连判死后的路线建议**
> 依唐先生 2026-09-14 16:13 裁定 ✓（**打 T2-c；目标锁死为"找出 H_a ⊆ S 使 H_a ∩ (a+B) = ∅"；若只得 density/residue/Kneser 型立即判死 ✗**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓；数值仅**精确整数核对**（平方自由筛 ≤2×10⁴ ✓）

---

## §0 ⭐ 审计判决：**锁定形式是【空泛的 ✗】**（它不使用覆盖 ⟹ 不可能是生死点 ✗）

$$\textbf{命题（平凡 ✓）}：\forall a\ge1,\ \forall B\subseteq S\ ✓,\ \text{取素数 }p\nmid a\ ✓,\ \text{令}\ H_a:=\{n\ \text{平方自由}:\ n\equiv a\bmod p^2\}\ ✓$$
$$\qquad\Longrightarrow\ n-a\equiv0\bmod p^2\ \text{且}\ n-a>0\ \Longrightarrow\ n-a\notin S\ \Longrightarrow\ \boxed{n-a\notin B}\ ✓（B\subseteq S\ ✓）\ \Longrightarrow\ \boxed{H_a\cap(a+B)=\varnothing}\ ✓\ \text{且 }|H_a|=\infty\ ✓$$
$$\textbf{数值核对 ✓}：(a,p)=(3,2)\Rightarrow H_a\ni7,11,15,19,23\ ✓；(7,3)\Rightarrow34,43,61,70,79\ ✓；(100,3)\Rightarrow109,118,\dots\ ✓\ \text{全部满足}\ n-a\notin S\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{判定 ✗}：H_a\ \text{对【每个】 }a\ge1\ \text{都平凡存在 ✓，且与 }B\ \text{的任何结构（乃至是否覆盖）【无关】✓}\ ⟹\ \text{它不是生死点 ✗}$$
$$\qquad\textbf{根因 ✓}：\text{覆盖 }S\subseteq A+B\ \text{从不要求【指定的】}a\ \text{负责某个 }n\ ✗\ \text{—— 它只要求"某一对"}(a,b)\ ✓$$
$$\qquad\Longrightarrow\ \text{唐先生设想的第三箭头（"A 的平方因子 ⟹ 定向禁类 ⟹ 某批平方自由整数失去【这一】A 元素的覆盖"）}$$
$$\qquad\qquad\textbf{在字面上是【平凡成立】的 ✗（对任意 A、任意 a、任意 B ⊆ S 都成立 ✓）}\ ⟹\ \text{按您的规则：判死 ✗}$$

## §1 您 §第一刀–§第四刀 的核对（✓ 结论与您一致 ✓；补一条关键定位 ✓）

$$\text{(1) 定向禁类 ✓ 成立 ✓}：a\equiv-r\bmod p^2\ \Longrightarrow\ B\cap(r+p^2\mathbb Z)=\varnothing\ ✓（\text{否则 }a+b\equiv0\bmod p^2\ ✗）$$
$$\qquad\textbf{特别 ✓}：a\equiv0\bmod p^2\ \Longrightarrow\ B\cap p^2\mathbb Z=\varnothing\ ✓\ \text{—— 但 }B\subseteq S\ \text{【已经】排除 }0\ \text{类 ✓ ⟹ 此 }\ a\ \text{在第 }p\ \text{层产生【零新增约束 ✗】}$$
$$\qquad\Longrightarrow\ \textbf{这正是新自由度 ✓，但注意 ✓}：\text{它只【放宽】约束 ✗，本身【不产生】覆盖缺口 ✗（与 §0 的空泛性一致 ✓）}$$
$$\text{(2) 多平方因子 ✓}：q^2\mid a,\ r^2\mid a'\ \text{只给两个独立避让 ✓（}B\not\equiv0\bmod q^2,\ B\not\equiv0\bmod r^2\ ✓）\ \text{无矛盾 ✗ —— 与您 §第四刀一致 ✓}$$
$$\text{(3) "A 含很多 }q^2\ \text{倍数"不够 ✓（您已标注 ✓）}：\text{同一 residue 只产生同一禁类 ✓ ⟹ 数量不转化为不相容 ✓}$$

## §2 ⭐⭐ 本轮真正的新结构：**覆盖局部性引理 ✓**（非空泛 ✓；且可达紧 ✓）

$$\text{设 }A=\{a_0=0<a_1<a_2<\cdots\}\ ✓\ \text{为递增枚举 ✓（}0\in A\ \text{由 E181 §0 ✓）}\ \Longrightarrow\ \forall k\ge1\ ✓：$$
$$\boxed{\ S\cap[0,a_k]\ \subseteq\ \bigcup_{i<k}\big(a_i+B\big)\ }\ ✓$$
$$\text{证 ✓}：n\in S,\ n\le a_k\ \Longrightarrow\ n=a+b\ \text{某}\ a\in A\ ✓；\ a\le n\le a_k\ ⟹\ a\in\{a_0,\dots,a_k\}\ ✓$$
$$\qquad\text{若 }a=a_k：\ b=n-a_k\le0\ \Longrightarrow\ b=0\notin B\ ✗\ \text{（}0\notin B\ \text{由 E181 §0 ✓）}\ \Longrightarrow\ a=a_i,\ i<k\ ✓\ \blacksquare$$
$$\textbf{数值核对 ✓（退化解 }A=S-1,\ B=\{1\}\ ✓）}：\forall k\le60\ \text{均成立 ✓，且}\ \boxed{\text{【取等】}\ ✓}\ \text{—— 引理在退化极值上可达紧 ✓}$$
$$\Longrightarrow\ \textbf{两个推论 ✓}：\text{① }\boxed{\text{每个 }a_k\ \text{只负责 }a_k\ \text{以上的覆盖}}\ ✓（\text{覆盖责任严格向上推 ✓}）；\ \text{② }\boxed{\{a_0..a_k\}\ \text{的硬数必}\ >a_{k+1}}\ ✓（E181 §4 ＋ 本引理 ✓）$$

## §3 ⚠️ 诚实标注：该链**仍不闭合 ✗**（我检查了三处可能收口，均失败 ✗）

```
① 计数方向 ✗：由局部性得 |S∩[0,a_k]| ≤ |∪_{i<k}(a_i+B)∩[0,a_k]| ≤ k·|B∩[0,a_k]| ✓
   —— 这是对 |B| 的【下】界 ✗（非上界 ✓），与 Kneser 的上界不冲突 ✓
② CRT 模数 ✗：硬数所在 AP 的模数 ∏p_i²（p_i ∤ e_i ✓）可被选得很大 ✓
   ⟹ 只给 a_{k+1} ≤ 某个大数 ✓（弱界 ✓），不产生矛盾 ✗
③ 硬数与覆盖元的相容性 ✗：覆盖元 a 需满足 n+(A-a) ⊆ S ✓，与证书 n+e_i ∉ S ✓
   只需 a ∉ {2a_i - a_{j(i)} : i ≤ k} ✓（有限避让 ✓）⟹ 大 a 总可避开 ✓ 相容 ✓
```

## §4 判词与路线建议（✓ 我的裁定 ✓）

$$\boxed{\textbf{T2-c（锁定形式）判死 ✗}}\ ✓（\S0\ \text{空泛性定理 ✓}）\qquad\textbf{不可能侧至此【三连判死 ✓】：}T1\ ✗\ \big|\ T2\text{-a（计数 ✗＋}\delta M\ ✗）\ \big|\ T2\text{-c}\ ✗$$
$$\qquad\text{且三次都是【内部审计/数值核对】先杀 ✓（T1 反例 ✓；}\delta M\ \text{被退化解否证 ✓；本论空泛性 ✓）\ ⟹\ \textbf{该信号本身有信息量 ✓}$$
$$\textbf{建议 ✓}：\text{转 T2-d（构造）✓，理由三条 ✓}：$$
$$\qquad\text{① 避让侧已被证明【完全自由 ✓】（E182 §1 ✓）；② 退化极值【饱和 ✓】（E183 §2 ✓，}M=1000\ \text{差}=0\ ✓）；$$
$$\qquad\text{③ 本轮的覆盖局部性引理给出【可操作的构造约束 ✓】：仅需让"责任向上推"的链仍覆盖全部 }S\ ✓$$
$$\textbf{若仍要打不可能侧 ✗}：\text{唯一未触发的量 ＝}\boxed{\text{覆盖局部性（}\S2\text{）}\times\text{投影刚性（E183 §3）在同一硬数上的交叉}}\ ✗（\text{未做 ✓}）$$

## §5 边界与一句话（✓）

```
✅ 本轮判定：T2-c 锁定形式【空泛 ✗ ⟹ 判死 ✗】（含定理、显式 H_a、数值 ✓）
✅ 新正确工具 ✓：覆盖局部性引理 S∩[0,a_k] ⊆ ∪_{i<k}(a_i+B)（数值 60 个 k 全通过 ✓，退化解取等 ✓）
⚠️ 局部性引理【不】闭合 ✗（三处收口均失败 ✓，已逐一记录 ✓）；不声称不可能 ✗
⭐ 净产出 ✓：① 空泛性定理（含根因：覆盖不指定 a ✓）；② 您四刀分析的核对 ＋ 定位（p² | a 在该层零新增约束 ✓）；
   ③ ⭐ 覆盖局部性引理（含取等 ✓）；④ 三连判死后的路线建议（转 T2-d ✓）
```
$$\boxed{\text{T2-c 空泛 ⟹ 判死 ✗；新得覆盖局部性引理（紧 ✓）；不可能侧已三连判死 ⟹ 建议转 T2-d 构造 ✓（避让自由 ✓＋退化饱和 ✓＋责任向上推 ✓）}}$$
