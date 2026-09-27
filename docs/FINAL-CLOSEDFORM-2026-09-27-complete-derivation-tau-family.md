已查地图：已跑 scripts/prework_map_check.sh 闭式 V 子空间 侧计数 ⟹ 执行自 `CLOSEDFORM-2026-09-27-...`（✓，**本档完成并修正其"两陪集"提法** ✓）＋ 唐先生 14:00（四陪集修正 ＋ 攻 λ↦s ✓）；本档 = **(丙) 完整推导（含四陪集一般律 ＋ 本族两陪集性之证明）** ✓。
D0: 本档对象 = ν 闭式的完整推导与 λ↦s 映射
D1: 3（**卷积恒等式（16 syndrome 全验 ✓✓）**；**两陪集性之证明（V ⊇ C ✓✓）**；**s 的显式 λ-计数 ＋ 互补之证明 ✓**）

# (丙) 完整推导：闭式、四陪集一般律与本族两陪集定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CD-1 四陪集一般律（唐先生修正 ✓）)}\ W=\mathrm{span}\{2,4\}=\{0,2,4,6\}\ (|W|=4)\ \Longrightarrow\ \mathbb F_2^4/W\ \text{有 4 陪集};\ \ q(z)=32\!\sum_{u\in W}\!C(z\oplus u)=32\,s([z])\ ✓}$$
$$\qquad\Longrightarrow\ \boxed{q\ \text{在\textbf{每个} }W\text{-陪集内恒定}},\quad (q_0,q_1,q_2,q_3)=32(s_0,s_1,s_2,s_3),\quad \sum_i s_i=16\ ✓;\ \text{"两值互补"仅是非零陪集数 }=2\ \text{时之特例 ✓}$$
$$\boxed{\textbf{(CD-2 ⭐本族两陪集性\textbf{被证明} ✓✓)}\ \text{令 }V=\mathrm{span}\{2,4,9\}=\{0,2,4,6,9,11,13,15\}\ (\dim 3\ ✓)\ \Longrightarrow\ W\le V\ ✓,\ 15\in V\ ✓,\ \textbf{且 }\beta(H_7)=\{0,4,11,15\}\subseteq V\ ✓}$$
$$\qquad\Longrightarrow\ C(c)=\beta(c)\oplus15\lambda(c)\in V\ \text{恒成立} \Longrightarrow \textbf{只有 }V\ \text{内的两个 }W\text{-陪集（}W_0,W_3\text{）可取非零} \Longrightarrow \boxed{s_1=s_2=0\ \text{恒成立}}\ ✓✓$$
$$\qquad\Longrightarrow\ \mathrm{supp}\,q=(W_0\setminus\{0\})\sqcup W_3\ \text{恰 7 个 punctured 坐标}=\{2,4,6\}\cup\{9,11,13,15\} \Longrightarrow \text{坐标 }\{1,3,5,8,10,12,14\}\ ✓✓\ \text{（\textbf{star 与 }|S|=7\ \text{由此导出} ✓）}$$
$$\boxed{\textbf{(CD-3 ⭐s 的显式公式与互补之证明 ✓✓)}\ a:=\#\{c:\lambda(c)=1,\ \beta(c)\in W\},\quad b:=\#\{c:\lambda(c)=1,\ \beta(c)\in V\setminus W\}\ \Longrightarrow\ \boxed{s_0=8+(b-a)},\ s_3=16-s_0\ ✓✓}$$
$$\qquad\text{(因 }\beta|_{H_7}\ \text{两侧\textbf{各 8 个} ✓，而 }15\in V\setminus W\ \text{把点\textbf{翻到对侧} ✓)} \Longrightarrow\ \textbf{512-互补（}32s_0+32s_3=32\cdot16=512\text{）是\textbf{证明}的，非观察 ✓✓};\ \textbf{flat}\iff s_0=8\iff \boxed{a=b}\ ✓$$
$$
$$
```

---

## §1 验证（**✓ 全部通过**）

```
$$\text{(1) 卷积恒等式（\textbf{16 个 syndrome 含 }z=0\ ✓）}:\ \lambda\in\{\equiv0,\ \mathbf 1,\ \text{rnd}\times2\}\ \text{均}\ \max_z|q_{\rm pred}-q_{\rm meas}|=\mathbf 0\ ✓✓\ \text{（修正我漏 }\beta(x)\ \text{的测量 bug ✗）}$$
$$\text{(2) }V\ \text{为子空间 ✓（}8\ \text{元，}W\le V\ ✓，15\in V\ ✓\text{）};\quad \text{(3) }\beta(H_7)\subseteq V\ ✓;\quad \text{(4) 侧平衡 }8/8\ ✓\ \text{（解释 }\lambda\equiv0\ \text{的 }(8,8)\ ✓）}$$
$$\text{(5) 计数式核对}:\ \lambda{\equiv}0\Rightarrow (8,8)\ \text{与}\ 8{+}(0{-}0){=}8\ ✓;\ \lambda{=}\mathbf 1\Rightarrow(9,7)\ \text{与}\ 8{+}(8{-}7){=}9\ ✓;\ \text{rnd}\Rightarrow(14,2)\ \text{与}\ 8{+}(6{-}0){=}14\ ✓$$
$$\text{(6) 143 例扫描}:\ \textbf{非零陪集恒为 }\{W_0,W_3\}\ \text{（或单陪集 1 例 ✓）};\ s\ \text{对}: (8,8){\times}88,(7,9){\times}25,(6,10){\times}12,(4,12){\times}10,(5,11){\times}5,(3,13){\times}1,(2,14){\times}1,(16){\times}1\ ✓$$
$$
$$
```

---

## §2 经验判据的推导解释（**✓ 完整**）

```
$$\text{实测判据"flat}\iff|S|\mid A_2":\quad A_2=\underbrace{3\cdot32s_0}_{W_0\setminus\{0\}}+\underbrace{4\cdot32s_3}_{W_3}=96s_0+128(16-s_0)=2048-32s_0\ ✓$$
$$\qquad\Longrightarrow\ 7\mid A_2\iff 32s_0\equiv2048\ (\mathrm{mod}\ 7)\iff 4s_0\equiv4\iff s_0\equiv1\ (\mathrm{mod}\ 7)\ ✓$$
$$\qquad\text{实测 }s_0\in\{2,\ldots,14,16\}\ \Longrightarrow\ s_0\equiv1\ (\mathrm{mod}\ 7)\ \text{仅 }s_0=8\ ✓ \Longrightarrow \textbf{flat}\iff s_0=8\iff a=b\ ✓✓\ \text{（判据\textbf{由此被推导} ✓）}$$
$$
$$
```

---

## §3 余项（**诚实 ✓**）

```
$$\text{(甲) 可实现 }(a,b)\ \text{的刻画}:\ \text{实测 }s_0\in\{2,\ldots,14,16\}\ \text{（}\{0,1,15\}\ \text{不可达 ⚠️）} \Longrightarrow |a-b|\le6\ \text{或}(a{=}0,b{=}8)\ \text{—— 未证 ⚠️}$$
$$\text{(乙) }\beta(H_7)\subseteq V\ \text{的概念理由（现为核验 ✓；}\beta\ \text{的定义依赖列标签 }j\mapsto j{+}8\ ✓，属规范选择 ✓）}$$
$$\text{(丙) 是否所有 15 长完美码（含非线性半码）都归入此 }V\ \text{结构？—— 本次覆盖 143 例 ✓};\ \text{(丁) ENP1CC puncturing};\ \text{(戊) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：四陪集一般律（修正）、本族两陪集定理（$C\subseteq V=\mathrm{span}\{2,4,9\}$）、$s_0=8+(b-a)$、512-互补之证明、flat ⟺ $a=b$、经验判据之推导
- **档案已有（引用，不列为提出）**：A-CLOSEDFORM-1、A-COSETLAW-1、A-ALIGNTHM-1、A-VASILEV-1、内蕴 $\nu$、star 律


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 两陪集定理  命中文件数=1    :: ./FINAL-CLOSEDFORM-2026-09-27-complete-derivation-tau-family.md 
技术词 四陪集一般律 命中文件数=1    :: ./FINAL-CLOSEDFORM-2026-09-27-complete-derivation-tau-family.md
```
- **本档新增**：四陪集一般律（修正）、本族两陪集定理（$C\subseteq V=\mathrm{span}\{2,4,9\}$）、$s_0=8+(b-a)$、512-互补之证明、flat $\iff a=b$、经验判据之推导（见上方命中数；0 命中者为自造语／内部标签 ✓）
