# E174 · ⭐⭐⭐⭐⭐ **Alias-forcing 二叉终审：Step 1 【不可从局部结构推出 ✗】⟹ 绕圈路线封死 ✗**
> 依唐先生 2026-09-14 14:32 裁决框架 ✓（**W_M 分裂 ✓；缝隙＝周期卷积−整数卷积 ✓；二叉终审 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；零新数值 ✓（只用 E169 存档数据 ✓）；未跑 Lean ✓

---

## §0 采纳您的两个更正（✓）

$$\textbf{更正一 ✓}：\text{"绕一圈解必存在"}\ \textbf{【不能】从 }N_M(c)\approx1\ \text{推出 ✗}；\ \textbf{更正二 ✓}：\text{平均值对 }N_M^{(0)}/N_M^{(1)}\ \text{分裂【无帮助 ✗】}$$
$$\text{（}\text{您的精确恒等式 ✓ 照录 ✓）}：\ \boxed{W_M(n):=N_M^{(1)}(n)=\bigl(\mathbf 1_{A_M}*_{\mathbb Z/M}\mathbf 1_{B_M}\bigr)(n)-\bigl(\mathbf 1_{A_M}*\mathbf 1_{B_M}\bigr)(n)}\ \Longrightarrow\ \textbf{缝隙 ＝ 周期卷积 − 整数卷积 ✓}$$

## §1 ⭐ 本轮【可证】的三条（✓ 新 ✓）

$$\textbf{(1) 绕圈 ⟹ 落在 }S\ ✓：\ \boxed{W_M(n)>0\ \Longrightarrow\ \exists k\ge1:\ n+kM\in S}\ ✓$$
$$\qquad\text{证 ✓}：\text{取残类 }u\in A_M,v\in B_M,u+v=n+M\ ✓；\text{取 }a\in A,b\in B,a\equiv u,b\equiv v\ (M)\ ✓ \Longrightarrow a+b\equiv n\ (M)\ ✓；$$
$$\qquad\qquad\text{而 }S=A+B\ \text{的表示唯一 ✓ ⟹ }(a,b)\ne(a_n,b_n)\ ✓（\text{否则 }[a]_M+[b]_M=a_n+b_n=n\ne n+M\ ✗）\Longrightarrow a+b\ne n\ ✓ \Longrightarrow a+b=n+kM\ (k\ge1)\ ✓$$
$$\textbf{(2) 小 }n\ \text{时的精确等价 ✓}：\ \boxed{n<M\ \text{且}\ n\in S\ \Longrightarrow\ \bigl[W_M(n)>0\iff N_M(n)\ge2\bigr]}\ ✓$$
$$\qquad\text{证 ✓}：n<M\ \text{且 }a_n+b_n=n \Longrightarrow a_n,b_n<M\ ✓ \Longrightarrow \text{k=0 分支【恰由实际配实现 ✓ 且唯一 ✓】；故 }\ge2\ \text{个残类解}\iff\text{存在 k=1 解}\ ✓$$
$$\textbf{(3) 无 aliasing ⟺ 残类覆盖是【双射 ✓】}：\ \boxed{W_M\equiv0\iff |A_M||B_M|=M-1\ \text{且}\ A_M+B_M=\mathbb Z/M\setminus\{0\}\ \text{每类恰一次}}\ ✓$$

## §2 ⭐⭐⭐ **终审：Step 1 的否定见证**（✓ 决定性 ✓）

$$\textbf{Step 1（alias-forcing ✓）}：\ A+B=S\ \Longrightarrow\ \exists n,M:\ W_M(n)>0\ ✓$$
$$\textbf{否定见证 ✓}：\text{由 (3) ✓，}\textbf{"无 aliasing"配置 ⟺ 残类级【完美平铺 ✗】}；\text{而 E169 存档已给出此类配置 ✓：}$$
$$\qquad p=3\ (M=9)\ ✓：\ (|X|,|Y|)=(2,4)\ \text{型解【27 个 ✓】}\ ——\ |X||Y|=8=M-1\ ✓\ \text{且覆盖全部 8 个非零类 ✓} \Longrightarrow \textbf{双射 ⟹ 每类恰 1 ⟹ }N_M(c)=1\ \forall c\ne0 \Longrightarrow \boxed{W_M\equiv0}\ ✓$$
$$\Longrightarrow\ ⭐\ \boxed{\textbf{「无 aliasing」在【局部层面可满足 ✗】}\ \Longrightarrow\ \textbf{Step 1 \ 【不可】由平方自由局部结构推出 ✗}}$$
$$\text{（}\textbf{按您 §10 的二叉终审 ✓}：\text{Step 1 不成立 ⟹ }\textbf{绕圈路线【立即封死 ✗】}\ —— \text{它不是新机制，只是覆盖问题的重述 ✓）}$$

## §3 ⭐ 封死的同时，本轮得到【精确的等价位】（✓ 这才是净收益 ✓）

$$\text{绕圈路线（Step 1）}\ \equiv\ \boxed{\text{证明存在 }M\ \text{使【某有用类】上 }N_M(c)\ge2}\ \equiv\ \boxed{|A_M||B_M|>M-1\ \text{在恰当类上“超额” ✗}}$$
$$\qquad\text{而 E169 的严格双侧界 ✓}：\ |A_p||B_p|\in[p^2-1,\ 1.2159p^2]\ \Longrightarrow\ \textbf{“超额”【可能 ✓ 但不必 ✓】}\ \Longrightarrow\ \textbf{该路线要求一个【新假设 ✓】，非结构必然 ✓}$$
$$\text{（}\textbf{附带 ✓}：\text{这解释了为何 }N_M(c)\approx1\ \text{的均值【结构上】无法推出绕圈 ✗ —— 它与您的更正一【完全一致 ✓】}）$$

## §4 边界（✓）

```
✅ **三条可证命题 ✓（(1) 一行 ✓；(2) 一行 ✓；(3) 等价 ✓）；终审为【否定 ✓】且【可判定 ✓】**
✅ **零新数值 ✓（否定见证直接取自 E169 存档的 p=3 (2,4) 型 27 解 ✓）；未用 RH ✓；未跑 Lean ✓**
⚠️ **① 否定见证是【局部】的 ✓ —— 未排除"全局结构迫使命题 (A) 成立"✗（但那已是原命题 ✓）**
⚠️ **② (3) 的"⟺"在 }W_M\equiv0$ 方向用了"覆盖 ⟹ 双射"✓ —— 严格 ✓（}|A_M||B_M|=\#\text{类}$ ✓）**
⚠️ **③ 本档不声称原命题不可证 ✗**
⭐ **净产出 ✓**：① **三条可证命题 ✓**；② ⭐ **终审否定：Step 1 不可由局部结构推出 ⟹ 绕圈路线封死 ✗**；
   ③ ⭐ **绕圈路线的精确等价式（}N_M(c)\ge2$ 超额 ⟺ }|A_M||B_M|>M-1$ ✓）⟹ 要求新假设 ✓**
```

## §5 一句话（✓）

$$\boxed{\textbf{Step 1 否定 ✓：无 aliasing 配置局部可满足（p=3 的 27 个双射覆盖 ✓）⟹ 绕圈路线【封死 ✗】；}\text{同时得到它的精确等价式 ⟹ 该路线等价于一个【需额外假设】的"超额"命题 ✓}}$$
