已查地图：已跑 scripts/prework_map_check.sh 两坐标 证伪 反例 特征和 ⟹ 执行自 `INVOL-2026-09-27-...`（✓）＋ 唐先生 14:20（开甲″-iii，证伪导向 ✓）；本档 = **证伪成功 ✓ ＋ 精化律（特征和）✓**。
D0: 本档对象 = 两坐标打孔池的反例与精化规律
D1: 3（**反例命中 ✓✓（[I:W]=4，三级谱 ✓）**；**精化律 ✓（等差＋二项式多重度 ⟹ 特征和 ✓）**；**两资产相应限界/修订 ✓**）

# (甲″-iii) 证伪成功与特征和精化律（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CT-1 ⭐⭐证伪成功 ✓✓)}\ \text{池（去重）662 码} = 3\ \text{原}\ +\ 45\ \text{一坐标}\ +\ 647\ \text{二坐标}\ ✓\ \text{（皆过硬门 ✓：}|W|{=}2048\ \wedge\ \mathfrak B_1(W){=}\mathbb F_2^{15} \Longleftrightarrow |C|{=}4096\ \wedge\ \mathfrak B_1(C){=}\mathbb F_2^{16}\ ✓\text{）}}$$
$$\qquad\textbf{反例命中 ✓}:\ \boxed{3\ \text{例 }\ [I{:}W]=\mathbf 4}\ ✗\ \[I{:}W]\in\{1,2\}\ \text{的普遍陈述被打破 ✓}\ \Longrightarrow \textbf{A-INVOL-1 降级为"构造族规律"} ✓$$
$$\qquad\textbf{三例同一对象（或等价 ✓）}:\ \text{纤维谱}=\boxed{\{96{:}4,\ 128{:}8,\ 160{:}4\}}\ \textbf{三级} ✗;\ |I|{=}16,\ |W|{=}4;\ W\text{-陪集值}=[96,128,128,160]\ ✓$$
$$\qquad\Longrightarrow\ \textbf{A-FEAS-1 的"单级／平衡两级"二分亦被打破} ✗\ \text{（其 }J\ \text{公式仍成立 ✓，因 }J\ \text{是谱的恒等式 ✓）}$$
$$\boxed{\textbf{(CU-1 ⭐⭐精化律 ✓（662 码全中）)}\ \text{按 }I/W\ \text{陪集看值}:\ [I{:}W]{=}1\Rightarrow 1\ \text{值（566 例 ✓）};\ =2\Rightarrow 2\ \text{值（93 例 ✓）};\ =4\Rightarrow \mathbf 3\ \text{值（3 例 ✓）}}$$
$$\qquad\boxed{\text{陪集值成\textbf{等差数列}，多重度}=\textbf{二项式 }C(k',\cdot)\ (1{:}2{:}1)\ \Longrightarrow\ \delta=f-\bar m\ \text{是 }k'=\log_2[I{:}W]\ \text{个独立线性\textbf{特征之和}}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{两级律 = }k'{=}1\ \text{特例}};\quad k'{=}2\ \text{（三级：}m/4,\ m/2,\ m/4\ \text{多重度 ✓）为\textbf{新一般形}};\ \text{单级 = }k'{=}0\ ✓$$
$$
$$
```

---

## §1 数据（**✓ 本机**）

```
$$\text{池规模}:\ 662\ \text{（去重 ✓）};\quad [I{:}W]\ \text{分布}:\ \{1{:}566,\ 2{:}93,\ \mathbf{4{:}3}\}\ ✓$$
$$\text{反例谱}:\ \{96{:}4,128{:}8,160{:}4\}\ \Longrightarrow\ \sum=4{\cdot}96+8{\cdot}128+4{\cdot}160=384+1024+640=2048\ ✓;\ \bar m=128\ ✓;\ \text{偏差}=\{-32,\ 0,\ 0,\ +32\}\ (\text{AP ✓},\ 1{:}2{:}1\ ✓)$$
$$\text{其 }J_{\rm int}=300336-f(0)^{2}\in\{291120,\ 283952,\ 274736\}\ (\text{取决于 }f(0){=}A_1\in\{96,128,160\}\ ⚠️\ \text{待取 ✓})$$
$$
$$
```

---

## §2 资产修订（**✓**）

```
$$\textbf{A-FEAS-1 修订 ✓}:\ \text{谱分类改为}\ \boxed{\text{陪集值 = 等差列，多重度 = 二项式 }C(k',\cdot),\ k'\in\{0,1,2\}\ (\text{观测})};\ \text{原"单级／两级"是 }k'\le1\ \text{特例};\ J\ \text{公式 }J=\sum_j e_jm_j^2-v_0^2\ \textbf{不变 ✓}（恒等式 ✓）$$
$$\textbf{A-INVOL-1 修订 ✓}:\ \text{对合 }\tau\ \text{与 }\delta(\tau g)=-\delta(g)\ \textbf{仅 }k'{=}1\ \text{成立 ✓};\ k'{=}2\ \text{时存在\textbf{两个独立}对合／特征（并非单一 }\tau\ ✓）$$
$$\textbf{限界陈述 ✓（唐先生 gate ✓）}:\ \boxed{[I{:}W]\le2\ \text{是\textbf{一坐标} pool 的规律，非一般定律} ✗}\ \text{—— 两坐标即破 ✓}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\textbf{P2 判定 ✓}:\ \text{找到合法反例} \Longrightarrow \text{按唐先生 gate：机制降级 ✓，并\textbf{转向甲″-iv}（追"为何 }\delta\ \text{是特征和"}）}$$
$$\text{(甲″-iv) 目标}:\ \text{从构造（extend→puncture 与 }X*C\ \text{卷积 ✓）\textbf{推导}特征和律（}k'\ \text{与 }I/W\ \text{的商结构 ✓）；若成功则 }A\ \text{线从"分类"升为"定理" ✓}$$
$$\text{(备选) 三坐标打孔（看 }k'{=}3\ \text{是否出现，即 }[I{:}W]{=}8\ ✓）；\ (丙) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：两坐标证伪（$[I{:}W]{=}4$ 反例）、三级谱反例、特征和精化律（等差＋二项式多重度）、A-FEAS-1/A-INVOL-1 修订
- **档案已有（引用，不列为提出）**：A-INVOL-1、A-FEAS-1、A-JIA-1、内蕴 $\nu$、$\mathfrak B_1$ 硬门


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 证伪成功     命中文件数=1    :: ./THREE-2026-09-27-falsification-succeeded-character-sum-law.md 
技术词 特征和精化律 命中文件数=1    :: ./THREE-2026-09-27-falsification-succeeded-character-sum-law.md
```
- **本档新增**：两坐标证伪（$[I{:}W]{=}4$ 反例）、三级谱反例、特征和精化律（等差＋二项式多重度）、A-FEAS-1/A-INVOL-1 修订（见上方命中数；0 命中者为自造语／内部标签 ✓）
