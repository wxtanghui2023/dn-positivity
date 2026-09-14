# E189 · ⭐⭐⭐⭐⭐ **单尺度自相似实验：$m(Q)=\infty$ ✗（不是 $O(1)$）—— 纯 free 层方案判死；但死因是一条【新定理 ✓】＝ E186 尺度两难的定形态**
> 依唐先生 2026-09-14 16:34 裁定 ✓（**打 (a) 自相似；第一目标＝锋利二分 $m(Q)=O(1)$? ✓；先验算再假设 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝精确整数枚举 ✓

---

## §0 实验设置与结果（✓ 数值 ✓）

$$Q_P=\prod_{p\le P}p^2\ ✓;\quad \text{低层 }A_0\ \text{取 E188 的万能 hitter}\ ✓;\quad B=\mathcal B(A_0)\ \text{（极大 ✓）};\quad \text{层元素 }a=iQ_P\ \text{（free ✓）}$$
$$U:=(S\cap[Q,Q^2))\setminus(A_0+B)\ \text{（待层元素补的缺口 ✓）}\ ✓;\qquad \text{dead}:=\{n\in U:\ \text{无任何 }i\ \text{使}\ n-iQ\in B\}\ ✗$$
```
P   Q      Lim       |S∩[Q,Lim)|   |B|      |U|        dead ✗      贪心 m(Q)  平移指数
2   4      16             8          7        0           0           0         —
3   36     1296         766        247      181         162          3 ✗     [3,4,5]
5   900    810000    491874     138394   122739      119643          5 ✗     [1,2,3,4,12]
```
$$\Longrightarrow\ \boxed{\textbf{用户生死点的答案 ✗}：m(Q)\neq O(1)\ \text{—— 是 }\infty\ ✗（P=3 有 162 个、P=5 有 119643 个 }n\ \text{根本无可用平移 ✓）}$$
$$\qquad\textbf{附带正面数据 ✓}：\text{【非 dead 部分】只需 }O(1)\ \text{个平移（P=3: 3 个 ✓；P=5: 5 个 ✓）⟹ free 层对"无障碍部分"确实高效 ✓（您的 §6 直觉局部成立 ✓）}$$

## §1 ⭐⭐ 死因定理（✓ 我推 ＋ 两尺度逐点核对 ✓✓）

$$\textbf{定理（free 平移保残类 ✓）}：\text{设 }a\equiv0\bmod p^2\ (p\le P)\ ✓\ \text{（即 }a=iQ_P\text{）}\ \Longrightarrow\ \forall p\le P:\ n-a\equiv n\bmod p^2\ ✓$$
$$\qquad\Longrightarrow\ \text{若 }\exists a_0\in A_0,\ p\le P:\ p^2\mid n+a_0\ ✓,\ \text{则}\ (n-iQ_P)+a_0\equiv n+a_0\equiv0\bmod p^2\ \forall i\ ✓\ \Longrightarrow\ n-iQ_P\notin S\ \Longrightarrow\ \boxed{n-iQ_P\notin B}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{n\notin (iQ_P)+B\ \ \forall i}\ ✓\ \text{—— 该 }n\ \textbf{不可能被任何 free 层元素覆盖 ✗}\ \blacksquare$$
$$\textbf{数值核对（精确集合相等 ✓）}：\text{dead}\ \overset{?}{=}\ \{n\in U:\exists a_0\in A_0,\ p\le P,\ p^2\mid n+a_0\}\ ✓$$
$$\qquad P=3：162=162\ ✓\ \text{（多出 0 ✓ 漏掉 0 ✓ 集合相等 ✓）};\qquad P=5：119643=119643\ ✓\ \text{（多出 0 ✓ 漏掉 0 ✓ 集合相等 ✓）}✓✓$$

## §2 判词（✓ 重要区分 ✓）

$$\boxed{\textbf{纯自相似 free 层方案【判死 ✗】}}\ ✓\ \text{（不是 }m(Q)=O(1)\ ✗\text{，而是 }m(Q)=\infty\ ✗）$$
$$\textbf{但它【不是】新的全局障碍 ✗ ✓}：\text{它正是 E186 尺度两难的}\ \boxed{\textbf{定理形态}}\ ✓✓：\text{低素数层（}p\le P\text{）的障碍在 free 平移下【恒定不变】✗}$$
$$\qquad\Longrightarrow\ \text{必须由【非 free】（小、昂贵）元素处理 ✓ —— 与 E186 §3 的结论逐字一致 ✓（免费元素下界 }4/36/900/44100\ ✓）$$
$$\textbf{且构造本身未被杀死 ✗ ✓}：\text{一个固定的非 free 元素 }a\ \text{与无穷 }B\ \text{相加可覆盖无穷多个此类 }n\ ✓\（\text{只需 }a\equiv-(n)\ \text{的残类匹配 ✓）}$$
$$\qquad\Longrightarrow\ \text{真正剩下的仍是最初的预算问题 ✓：}\ \frac{6}{\pi^2k}\lesssim D(A)\ ✓（E187 ✓）\ \text{—— 即"非 free 元素的需求量是否有界"✗}$$

## §3 (E190) 建议（✓ 混合方案 ✓）

```
混合方案 ✓：① 少量【非 free】小元素 ⊂ 低区间（承担 p ≤ P 的小素数障碍 ＋ 低区间命中 ✓，E188 的 τ⁰ 有界 ✓ 说明只需常数个 ✓）
           ② 【free】大元素逐层（各层 ≡ 0 mod ∏_{p≤P_k}p² ✓ 承担高区间 ✓，本轮的"非 dead 部分只需 3–5 个平移 ✓"）
判据 ✓：总 sieve 预算 6/(π²k) ≤ D(A) ✓（E187 ✓）＋ 层数 × 每层伤害（E186 §4 ✓）
最后一个未知量 ✗：非 free 元素的需求量是否有界 ✗ —— 这是现在唯一没被任何一轮数据触碰的量 ✓
```

## §4 边界与一句话（✓）

```
✅ 本轮 ✓：① 单尺度实验（P=2,3,5 ✓）；② ⭐ 死因定理（free 平移保残类 ✓，两尺度逐点核对 ✓✓）；
   ③ 判定 m(Q)=∞ ✗（不是 O(1) ✗）；④ 明确该死因＝E186 尺度两难的定形态 ✓（非新障碍 ✓）
⚠️ 仅在 A₀ = E188 低层 hitters ＋ B 极大的选择下验证 ✓；未穷尽 A₀ 的所有选择 ✗
⚠️ 仍不声称构造存在 ✗、不声称不可能 ✗
⭐ 净产出 ✓：把"逐层 free 构造"这条路关掉 ✗（定理级 ✓），同时把它归因到已知的尺度两难 ✓，
   并给出下一步唯一的未知量（非 free 元素需求量的界 ✓）
```
$$\boxed{m(Q)=\infty\ ✗（非 }O(1)\ ✗\text{）—— 死因 ＝ 定理"free 平移保 }p\le P\ \text{残类"✓（两尺度精确核对 ✓）；}\text{这是 E186 尺度两难的定形态 ✓，非新障碍 ✓；下一枪 (E190) 混合方案，唯一未知量 = 非 free 元素需求量是否有界 ✗}$$
