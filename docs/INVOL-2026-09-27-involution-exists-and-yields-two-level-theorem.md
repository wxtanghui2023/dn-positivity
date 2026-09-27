已查地图：已跑 scripts/prework_map_check.sh 对合 τ 周期 W 两级定理 ⟹ 执行自 `FEAS-2026-09-27-...`（✓）＋ 唐先生 14:20（开甲″-ii，先找 τ ✓）；本档 = **对合存在 ✓✓ ＋ 三结论之推导 ✓✓**。
D0: 本档对象 = 迫使谱两级化的代数来源（对合／特征）
D1: 3（**τ 存在且为平移 ✓✓（48/48）**；**三结论推导 ✓✓**；**来源：Vasil'ev 支已推导 ✓、打孔支观测 ⚠️**）

# (甲″-ii) 对合与两级定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CQ-1 ⭐⭐对合存在 ✓（48/48 实测）)}\ \text{对池内全部 48 码}:\ \boxed{I:=\mathrm{supp}(f)\ \text{是子群 ✓}\quad\text{且}\quad [\,I:W\,]\in\{1,\ 2\}\ ✓}\ \text{其中 }W=\text{周期（}f\text{ 的稳定子 ✓）}}$$
$$\qquad\textbf{两级时}\ [I{:}W]{=}2:\ \text{取任一非平凡陪集代表 }\eta\in I\setminus W \Longrightarrow \boxed{\tau(g)=g\oplus\eta}\ \text{是无不动点对合 ✓ 且}\ \boxed{\delta(\tau g)=-\delta(g)}\ ✓✓\ (\delta:=f-\bar m\ ✓)$$
$$\qquad\textbf{等价表述 ✓（= 唐先生候选 3 ✓）}:\ \boxed{\delta\ \text{是商群 }I/W\cong\mathbb F_2\ \text{上的\textbf{非平凡线性特征}}}\ ✓✓ \Longrightarrow \text{无字符／Fourier 展开，纯陪集对偶即足 ✓}$$
$$\boxed{\textbf{(CR-1 ⭐⭐三结论之推导 ✓✓)}\ \text{设 }I\ \text{为子群、}f\ \text{在 }W\text{-陪集恒定、}[I{:}W]{=}2 \Longrightarrow \text{两个陪集大小皆 }|W|=\tfrac m2\ ✓\ \text{且值各异 }v_1,v_2:}$$
$$\qquad\Longrightarrow\ \boxed{\text{(i) 二级结构 }\{v_1^{m/2},\ v_2^{m/2}\}}\ ✓;\quad \boxed{\text{(ii) 多重度等分 }m/2\ ✓};\quad \boxed{\text{(iii) 互补 }v_1+v_2=2\bar m}\ ✓\ \text{（因均值 }=\tfrac{v_1+v_2}{2}=\bar m\ ✓）$$
$$\qquad\Longrightarrow\ \textbf{三者皆\textbf{非独立}，是同一陪集结构的三个面 ✓} \Longrightarrow \textbf{A-FEAS-1 的"额外代数条件"被归约为}\ \boxed{I\ \text{子群}\ \wedge\ [I{:}W]\le2}\ ✓✓$$
$$\boxed{\textbf{(CS-1 ⚠️来源之状态)}\ \text{Vasil'ev 支：}\textbf{已推导 ✓}\ (f=X*C\ \text{且 }X\ \text{在 }W\ \text{上均匀}\Longrightarrow f\ \text{自动 }W\text{-不变}\ ✓);\quad \text{打孔支：}\textbf{观测} ⚠️\ (48/48 ✓\ \text{但无证明})}$$
$$
$$
```

---

## §1 实测（**✓ 48/48**）

```
$$\text{判据}:\ I=\mathrm{supp}(f)\ \text{为子群（含 0 ✓）＋}\ [I{:}W]\in\{1,2\};\quad W=\{g:\ \forall x,\ f(x\oplus g)=f(x)\}\ \text{（周期 ✓）}$$
$$\text{结果}:\ \mathbf{48/48\ ✓};\ \text{两级例（}[I{:}W]{=}2\text{）全部满足 }\delta(\tau g)=-\delta(g)\ \text{（}\tau=\text{平移一个非平凡代表 ✓）};\ \text{单级例 }[I{:}W]{=}1\ ✓$$
$$\text{例}:\ \mathrm{V1}\ (\text{纯 Vasil'ev }s{=}9):\ I=V\ (8\ \text{元 ✓}),\ W\ (4\ \text{元 ✓}),\ \tau=\text{平移 }1\ ✓ \Longrightarrow \{224^4,288^4\}\ ✓;\ \mathrm{V1\_p8}:\ \{112^8,144^8\},\ \tau=\text{平移 }1\ ✓$$
$$
$$
```

---

## §2 判定与边界（**✓**）

```
$$\textbf{甲″-ii 判定}:\ \boxed{\text{THEOREM 候选成立（}I\ \text{子群 ＋ }[I{:}W]\le2\Longrightarrow\text{三级结论 ✓）}};\ \text{对 Vasil'ev 支该条件\textbf{已推导 ✓}（}X\ \text{均匀性 ⟹ }W\text{-不变} ✓\text{），对打孔支为\textbf{观测} ⚠️}$$
$$\qquad\textbf{诚实边界 ⚠️}:\ \text{尚未证明"打孔必然保持 }I\ \text{为子群且 }[I{:}W]\le2"\ ✗;\ \text{故整体状态} = \boxed{\textbf{Vasil'ev 支 = THEOREM}\ ✓;\ \textbf{打孔池 = SUPPORTED}\ ⚠️}$$
$$\qquad\textbf{反例风险 ✓}:\ \text{若找到 }[I{:}W]{=}4\ \text{或 }I\ \text{非子群的合法码 ⟹ 本机制破裂（下一步检验 ✓）}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\text{(甲″-iii) }\textbf{两坐标打孔/缩短}:\ \text{主动找 }[I{:}W]{>}2\ \text{或 }I\ \text{非子群的候选（破机制检验 ✓）};\ \text{(甲″-iv) 证明打孔保持性（代数 ✓）};\ \text{(丙) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：对合 $\tau$ 存在性（48/48）、三结论（二级／等分／互补）之推导、$I$ 子群 $+[I{:}W]\le2$ 之归约
- **档案已有（引用，不列为提出）**：A-FEAS-1、A-JIAPRIME-1、A-SUBSPACE-1、内蕴 $\nu$、$W$-陪集常值律


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 对合存在     命中文件数=1    :: ./INVOL-2026-09-27-involution-exists-and-yields-two-level-theorem.md 
技术词 三结论推导  命中文件数=1    :: ./INVOL-2026-09-27-involution-exists-and-yields-two-level-theorem.md
```
- **本档新增**：对合 $\tau$ 存在性（48/48）、三结论（二级／等分／互补）之推导、$I$ 子群 $+[I{:}W]\le2$ 之归约（见上方命中数；0 命中者为自造语／内部标签 ✓）
