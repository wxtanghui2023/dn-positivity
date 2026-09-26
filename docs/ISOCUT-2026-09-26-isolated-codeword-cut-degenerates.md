已查地图：已跑 scripts/prework_map_check.sh K(10,1) 孤立码字 private point 中点容量 ⟹ **命中既有档案**：`docs/ISOB3-2026-09-26-isolated-codewords-versus-distance-two-degree.md`（(C-1) 恒等式 ✓）＋ `docs/MIDSUP-...md`（中点 injectivity ✓）＋ `docs/K1AUDIT-...md`（Mid∖{z}=全部非码字 b=2 点 ✓）⟹ 本档为**更正＋判定**（唐先生 2026-09-26 21:24 稿 ✓）；含一次反例验证 ✓。
D0: 本档对象 = 孤立码字 → private points → 中点容量 链（既有对象，**已覆盖** ⚠️）
D1: 0（产出为三处更正与"tightening 非 leverage"判定）

# ISOCUT-2026-09-26 · 孤立码字一刀：三处更正与判定

## §0 结论（先给）

```
$$\boxed{\textbf{(T-1 更正①)}\ \text{profile 应为}\ N_2=283,\ N_1=740\ ✓;\ \text{唐稿 }286/737\ \textbf{自相矛盾}\ ✗\ (737+2\cdot286+3=1312\ne1309)}$$
$$\boxed{\textbf{(T-2 更正②)}\ \text{“孤立码字}\Rightarrow\text{10 个 }b{=}1\ \text{点”}\ \textbf{不成立}\ ✗;\ \text{正确式＝本线\textbf{已有}的 }(C{-}1):\ \sum_{x\in N(c)}(b(x)-1)=d_1(c)+2d_2(c)\ ✓}$$
$$\boxed{\textbf{(T-3 更正③)}\ \text{中点账目\textbf{无缺口}}\ ✗:\ 2A_2-3=283-2A_1\ \text{为恒等式};\ A_1\le49\ \text{使两侧\textbf{同向}移动}\ ✓}$$
$$\boxed{\textbf{(T-4 判定)}\ \Longrightarrow\ \textbf{本层精确饱和}\ \Longrightarrow\ A_1\le49\ \text{是 \textbf{tightening}，不是 \textbf{leverage}}\ ✓\ \text{（第 11 次同向汇合）}$$
$$
$$
```

---

## §1 (T-1) profile 算术更正（反例自检 ✓）

```
$$\text{设}\ N_k=\#\{x:b(x)=k\}\ ✓;\quad Q=1\Rightarrow N_3=1\ ✓$$
$$N_1+N_2+N_3=1024\ ✓;\qquad N_1+2N_2+3N_3=|C|\cdot11=1309\ ✓$$
$$\text{相减}:\ N_2+2N_3=1309-1024=285\ \Longrightarrow\ \boxed{N_2=283,\ N_1=740}\ ✓✓$$
$$\text{唐稿}\ (N_2,N_1)=(286,737):\quad 737+2\cdot286+3=1312\ne1309\ \textbf{自相矛盾}\ ✗✗;\quad 737+286+1=1024\ ✓\ \text{（故错在第二式）}$$
$$
$$
```

---

## §2 (T-2) “孤立 ⟹ 10 个 private point” 不成立（反例 ✓）

```
$$\textbf{正确关系}:\ \text{对任意 }c\ \text{（孤立或否）}\ \text{其 10 个邻点}\ x_i=c\oplus e_i:\ b(x_i)=1+\#\{j:c\oplus e_i\oplus e_j\in C\}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\sum_{x\in N(c)}(b(x)-1)=d_1(c)+2d_2(c)}\ ✓\ \textbf{＝本线已有 }(C{-}1)\ \text{恒等式}\（\texttt{ISOB3}\ ✓）$$
$$\textbf{反例（本档实测 ✓）}:\ C=\{0,\ e_1\oplus e_2\},\ c=0\ \text{孤立}\ (d_1=0\ ✓)\ \Longrightarrow\ b(e_1)=b(e_2)=\mathbf 2\ \ne1\ ✗✓$$
$$\qquad\text{实测}\ \sum_{N(c)}(b-1)=2=d_1+2d_2=0+2\cdot1\ ✓\ \text{恒等式精确成立}\ ✓$$
$$\Longrightarrow\ \text{孤立码字只\textbf{强制} }d_1+2d_2\ \text{的总量（＝}2d_2\ \text{），\textbf{不}强制 10 个 }b{=}1\ \text{点}\ ✗;\ \text{且 }b{=}1\ \text{点总数恒为}\ N_1=740\ \text{（固定）}\ ✓$$
$$
$$
```

---

## §3 (T-3) 中点账目：恒等式，无缺口

```
$$\text{每个 distance-2 pair 的 2 个中点均为 }b{=}2\（\text{injectivity}\ ✓）;\quad \text{且 非码字 }b{=}2\ \text{点}\ \textbf{恰好就是}\ \text{中点集}\（\texttt{K1AUDIT}\ ✓）$$
$$\Longrightarrow\ \text{需求}=2A_2-3\ ✓,\quad \text{容量}=283-2A_1\ ✓,\quad \text{二者由恒等式}\ 2A_2-3=283-2A_1\ \textbf{精确相等}\ ✗$$
$$A_1\le49\ \text{时}:\ 2A_2-3\in[188,283]\ ✓,\ 283-2A_1\in[185,283]\ ✓\ \text{——\textbf{等式逐点成立，无缺口}}\ ✗$$
$$
$$
```

---

## §4 (T-4) 判定与下一步（决策点 ✓）

```
$$\textbf{本层}:\ \text{精确饱和}\ ✗\ \Longrightarrow\ A_1\le49\ \text{为 tightening（参数窗收紧）而非 leverage（不产生新矛盾类型）}\ ✓$$
$$\textbf{真收获（保留 ✓）}:\ \text{① }A_1\le49\ \text{（Delsarte×}Q{=}1\ \text{恒等式，本线新界 ✓）};\ \text{② }|I|\ge21\ \text{（孤立码字，新结构事实但\textbf{非绑定} ✓）}$$
$$\textbf{三阶路线评估（诚实 ⚠️）}:\ \text{文 Taylor/Terwilliger 型三阶 SDP 正是 }2504.01932\ \text{之法};\ \text{其在 }(2,10,1)\ \text{格给}\ 105.22<107<119\ ✗\ \Longrightarrow\ \textbf{升三阶亦难闭合此 cell}\ ⚠️$$
$$\textbf{建议}:\ \text{(a) 廉价剩余杠杆：把 \textbf{Van Wee／球覆盖}不等式并入同一 LP（可再收紧 }A_1\text{，但预计仍属 tightening）};\ \text{(b) 或将 119 线以"结构未闭合＋11 类机制不足＋}A_1\le49\text{"正式封存，转新 asset-native 题}\ ✓$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为**算术** ✓；§2 的关键式 $(C{-}1)$ **属既有资产** ✓（本档仅更正措辞，**不列为新提出** ✓）；反例为**构造性验证** ✓
- §3 依赖两条既有资产（injectivity ✓、Mid∖{z} 等式 ✓）⟹ **无新数学** ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；$A_1\le49$ **不得**被读作"距 119 更近" ✗
- **未**跑搜索/求解器 ✓（仅 §2 反例 ＋ §1 算术 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 孤立码字一刀的判定 命中文件数=1    :: ./ISOCUT-2026-09-26-isolated-codeword-cut-degenerates.md 
技术词 中点账目无缺口 命中文件数=1    :: ./ISOCUT-2026-09-26-isolated-codeword-cut-degenerates.md
```
- **本档新增**：孤立码字一刀的判定、中点账目无缺口（见上方命中数）
- **档案已有（引用，不列为提出）**：$(C{-}1)$ 恒等式、中点 injectivity、Mid∖{z} 等式、profile (740,283,1)、$A_1\le49$
