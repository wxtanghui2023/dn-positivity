# E173 · ⭐⭐⭐⭐⭐ **缝隙的精确刻画：模覆盖 ⟹ 精确覆盖 的【有界代表元判据】**
> 承接 ✓ 唐先生 14:20「继续」｜**攻引理 C 的缝隙本身 ✓**（非另加局部条件 ✗）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓；零新数值 ✓；**四层框架【未使用 ✗】**

---

## §0 判据（✓ 一段可证 ✓）

$$\textbf{命题（有界代表元判据 ✓）}：\text{固定目标 }n\ ✓。\ \textbf{若}\ \forall M\ \exists(a,b)\in A\times B:\ \boxed{a+b\equiv n\ (M)\ \text{且}\ 0\le a,b\le n}\ ✓，\ \textbf{则}\ \exists(a,b):\ a+b=n\ ✓$$
$$\textbf{证 ✓（紧性 ✓）}：\text{每 }M\ \text{给出一个 }(a_M,b_M)\in[0,n]^2\ ✓；\text{该盒【有限 ✓】}\ \Longrightarrow\ \text{某对 }(a,b)\ \text{对【无穷多 }M\ \text{】出现 ✓；}$$
$$\qquad\text{对该 }(a,b) ✓：\ M\mid(a+b-n)\ \text{对无穷多 }M\ ✓ \Longrightarrow\ a+b-n=0\ ✓ \Longrightarrow\ a+b=n\ \checkmark$$
$$\Longrightarrow\ \boxed{\text{【模覆盖 ✓】}\ \Longrightarrow\ \text{【精确覆盖 ✗】}\quad\textbf{当且仅当}\ \textbf{代表元可【一致有界 ✓】}}$$
$$\textbf{逆否（缝隙 ✓）}：\ \boxed{\text{缝隙开启}\iff\textbf{每个模数的解【都只能】用}\ \ge M\ \text{级的代表元 ✓}\ \Longrightarrow\ \text{模解"横向铺开" ✗，不收敛 ✓}}$$

## §1 ⭐ 为什么四层框架【结构上】看不到缝隙（✓ 本轮核心解释 ✓）

$$\text{四层工具（局部 ✓／CRT ✓／密度 ✓／提升 ✓）检验的都是【存在性 ✓】：}\exists\,(a_M,b_M)\ \text{使 }a_M+b_M\equiv n\ (M)\ ✓$$
$$\qquad\Longrightarrow\ \textbf{它们对【代表元的大小 ✗】完全不敏感 ✗} —— \text{而缝隙【正是】代表元大小问题 ✓}$$
$$\text{（}\textbf{一句话 ✓}：\text{四层工具作用于缝隙的【左侧 ✓】；判据表明缝隙的开启由【右侧 ✗】决定 ✓）}$$

## §2 新可观测量（✓ 缝隙的"温度计" ✓）

$$\text{对模 }M\ \text{与类 }c\ ✓：\ \boxed{N_M(c):=\#\{(a,b)\in A\times B:\ 0\le a,b<M,\ a+b\equiv c\ (M)\}}\ ✓$$
$$\qquad\text{则 ✓}：A_M+B_M=\mathbb Z/M\setminus\{0\}\ \Longrightarrow\ N_M(c)\ge1\ (c\ne0)\ ✓；\qquad \sum_{c}N_M(c)=|A_M|\,|B_M|\ ✓$$
$$\textbf{判据的重述 ✓}：\text{精确覆盖成立}\iff\ \exists M\ \exists(a,b)\in A\times B:\ a+b=n\ \text{且}\ a+b<n+M\ \text{（}\text{即该类的最小解不"绕一圈" ✗）}$$
$$\text{（}\text{对 }M>n:\ a+b\equiv n\ (M)\ \text{且}\ a+b<2M \Longrightarrow a+b\in\{n,\ n+M\}\ ✓\ \Longrightarrow\ \textbf{只需排除 }a+b=n+M\ ✗}）$$

## §3 与已知结构的接口（✓ 不引入新假设 ✓）

$$\text{① 与 §E172 引理 A 的联系 ✓}：\text{若 }(a_1,b_1),(a_2,b_2)\ \text{同给类 }c\ \text{且皆"绕一圈" ✗}，\text{则}(a_1-a_2)\equiv(b_2-b_1)\ (M)\ ✓\ \text{—— 【精确等号 ✗】才被 Lemma A 禁止 ✓}$$
$$\qquad\Longrightarrow\ \textbf{缝隙恰是"近似版 Lemma A"的存活空间 ✓（同余 ≠ 相等 ✓）}$$
$$\text{② 与 }A(X)\asymp\sqrt X\ \text{的联系 ✓}：|A_M|\le\prod_{p\mid M}|A_p|\approx\sqrt M\ ✓ \Longrightarrow\ \text{平均 }N_M(c)\approx|A_M||B_M|/M\approx1\ ✓$$
$$\qquad\Longrightarrow\ \textbf{"绕一圈解"与"精确解"在计数上【同量级 ✗】}\ \Longrightarrow\ \textbf{计数无法分离二者 ✓（这解释了 §E172 §6 路线 (a)(d) 的失败 ✓）}$$

## §4 边界（✓）

```
✅ **§0 判据【完整证明 ✓】（紧性 ✓ 三行 ✓）；§1 解释为结构性的 ✓；§2 新量 ✓；§3 双接口 ✓**
✅ **零新数值 ✓；未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓**
⚠️ **① 判据是【刻画 ✓】，不是 NO-GO ✗** —— 它把缝隙【定位】到"代表元大小 ✗"，未证明缝隙必然开启 ✗
⚠️ **② §2 的 }N_M(c)$ 未做任何估计 ✗** —— 下轮若要推进，须先证 }N_M(c)$ 的下界或"绕一圈解必存在"✗
⚠️ **③ 本档不声称原命题不可证 ✗**
⭐ **净产出 ✓**：① ⭐ **有界代表元判据（模覆盖 ⟹ 精确覆盖 的充要条件 ✓）**；
   ② ⭐ **四层工具看不见缝隙的【结构性解释 ✓】（它们对代表元大小不敏感 ✗）**；
   ③ **缝隙"温度计" }N_M(c)$ ✓**；④ **与 Lemma A／}\asymp\sqrt X$ 的两个接口 ✓**
```

## §5 一句话（✓）

$$\boxed{\text{缝隙 ＝ 【代表元大小问题 ✗】；模覆盖 ⟹ 精确覆盖 当且仅当代表元一致有界 ✓；}\textbf{这解释了为何四层工具（只问存在性 ✗）永远够不到它 ✓}}$$
