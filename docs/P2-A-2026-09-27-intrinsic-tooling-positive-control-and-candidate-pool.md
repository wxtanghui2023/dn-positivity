已查地图：已跑 scripts/prework_map_check.sh 内蕴 ν 工具 正控 P2-A ⟹ 执行自 `P2-E1-2026-09-27-...`（✓）＋ 唐先生 13:41（乙结论：文献侧无反例；转 P2-A ✓）；本档 = **内蕴工具正控 ✓ ＋ 候选池钉死 ＋ E3 判据** ✓。
D0: 本档对象 = P2-A 的可执行工具与其正控验证
D1: 2（**内蕴 ν-gate 工具 ✓（正控通过 ✓✓）**；**候选池与判据 ✓**）

# P2-A：工具、正控与候选池（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BX-1 乙的文献审计结论（唐先生 ✓）)}\ \text{文献中\textbf{未找到}逃逸 β-gate 的 NP1CC} ✗;\ \text{Type A 已完全刻画};\ \textbf{Type B/C 未完全刻画} ✗;\ \text{论文 5 个 open problems 保留结构问题} ✓$$
$$\qquad\Longrightarrow\ \mathrm{NP1CC}\Rightarrow\text{Theorem-13 形}\ \textbf{未被文献证明} ✗\ \Longrightarrow\ \textbf{P2 是真实 gap}（非人造 ✓）$$
$$\boxed{\textbf{(BX-2 ⭐内蕴工具 ＋ 正控 ✓✓)}\ \nu:\binom{[16]}{2}\to\mathbb Z_{\ge0}\ \text{（伙伴对差向量分布 ✓，只用论文 §II 的伙伴对划分 ✓）};\ \text{实测 }n{=}16\ \text{Type C 码}:}$$
$$\qquad|C|=4096\ ✓,\ k=256\ ✓\ (\text{Type C}\ ✓),\ \text{伙伴对}=2048=M/2\ ✓,\ \nu=\{1:\mathbf{256},\ 2:\mathbf{1792}\}\ ✓\ (\text{后者}=A_2\ ✓)$$
$$\qquad\textbf{星性质 ✓}:\ \text{7 个重量-2 差集共有坐标 }\ell=15\ ✓✓;\qquad \textbf{flatness ✓}:\ \text{切片 }q_v\equiv256=\lambda\ ✓✓\ \Longrightarrow \text{族内码必过双 gate（与定理一致 ✓）}$$
$$\boxed{\textbf{(BX-3 缺失成分 ⚠️)}\ \text{要产生 P2 反例，需一个\textbf{非线性半码}的 NP1CC}（n{=}16\ \text{的半码是长 15 完美码，可非线性 ✓；}n{=}8\ \text{时唯一 ✗ 无测试空间 ✓）}$$
$$\qquad\Longrightarrow\ \text{唯一可行入口}:\ \textbf{Vasil'ev 型非线性完美码}（或论文 open problem 的 ENP1CC-puncturing ✓）；\ \text{验证便宜（覆盖检验 ✓）}$$
$$
$$
```

---

## §1 内蕴工具（**✓ 可执行，已测**）

```
$$\textbf{输入}:\ NP1CC\ \text{的码字集合 }C\ ✓\ \text{（无需构造参数 ✓，故对"任意"NP1CC 有定义 ✓）}$$
$$\textbf{步骤}:\ \text{(1) 用 }\mathfrak B_1\ \text{覆盖计数求 }b(x)\ ✓;\ \text{(2) }Z=\{b=2\}\ ✓;\ \text{(3) 每 }z\in Z\ \text{的两个覆盖者 = 伙伴对 ✓（论文 §II ✓）};\ \text{(4) 累加差向量分布 }\nu\ ✓$$
$$\textbf{输出}:\ \nu\ \text{（按差向量的重量与支撑分类 ✓）} \Longrightarrow \text{gate 检查}: \text{(i) 重量-1 部分是否全为"层坐标对"（Type I ✓）};\ \text{(ii) 重量-2 差集是否共有一个坐标 }\ell\ \text{（\textbf{星} ✓）};\ \text{(iii) 切片 }q_v:=\nu(\{v,\ell\})\ \text{是否恒定（\textbf{flatness} ✓）};\ \text{(iv) }q\ \text{的支撑是否 }\mathbb F_2^m\ \text{-几何集（linear/affine 去 0 ✓）}$$
$$\qquad\textbf{正控（本档 ✓）}:\ \text{上述四项在 }n{=}16\ \text{Type C 实例上全部通过 ✓✓（值 }\ell{=}15,\ \lambda{=}256,\ |S|{=}7,\ A_2{=}1792\ ✓）$$
$$
$$
```

---

## §2 候选池（**✓ 按唐先生优先级**）

```
$$\begin{array}{c|c|c|c}
\text{优先级} & \text{候选} & \text{可拿到码字?} & \text{是否族外}\\
\hline
1 & \textbf{ENP1CC puncturing}（论文 open problem ✓） & \text{可能（须构造 ✓）} & \text{待定（若半码非线性 ⟹ 族外 ✓）}\\
2 & \textbf{Type C 显式构造（非线性半码 ✓）} & \text{是（Vasil'ev 型 ✓）} & \textbf{是} ✓\\
3 & \text{小参数已分类 NP1CC} & \text{部分} & \text{否（多半族内 ✗）}\\
4 & \text{其它代数构造（cyclic/self-dual ✓）} & \text{可能} & \text{待定 ⚠️（须查 gate，不可因"构造新"即判新 ✓）}\\
\end{array}$$
$$\textbf{警告（唐先生 ✓）}:\ \text{"构造不同"}\ne\text{"gate 不同"} ✓;\ \text{必须实际算 }\nu\ \text{再判 ✓}$$
$$
$$
```

---

## §3 E3 判据（**✓ 形式化**）

```
$$\exists C\in\mathrm{NP1CC}:\ \text{(i)}\ \text{重量-2 差集无公共坐标（非星 ✗）}\ \vee\ \text{(ii) 切片 }q_v\ \text{不恒定（非 flat ✗）}\ \vee\ \text{(iii) 支撑非 }\mathbb F_2^m\text{-几何} ✗$$
$$\qquad\Longrightarrow\ \boxed{\mathrm{NP1CC}\not\subseteq\text{Theorem-13 β-shape}}\ ✓\ \text{（真 P2 collision ✓）};\ \text{反之} \Longrightarrow \text{Theorem-13 family}\subseteq\text{gate-满足 NP1CC 且文献无反例 ✓}$$
$$
$$
```

---

## §4 边界与自纠（**✓**）

```
$$\text{(i) 本档\textbf{自行更正}一处标注}:\ \text{覆盖链给出 }|Z|=M=4096\ ✓\ \text{（\textbf{非 }M/2\ ✗}）；\text{伙伴对数}=M/2=2048\ ✓\ \text{（两者不同 ✓）}$$
$$\text{(ii) §1 工具已实测 ✓；§2/§3 为方案（未执行 P2-A 反例搜索 ✗）；\textbf{未}声称任何反例 ✗；\textbf{未}涉 119 ✓}$$
$$\text{下一步（三选一 ✓）}:\ \text{(甲) 实现 Vasil'ev 非线性完美码（长 15 ✓）⟹ 造族外 Type C ⟹ 跑 §1 工具 ⟹ E3 判定};\ \text{(乙) 追 ENP1CC puncturing 的显式码表};\ \text{(丙) 重定位 119} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：内蕴 $\nu$ 工具与正控、候选池优先级、E3 形式化判据
- **档案已有（引用，不列为提出）**：A-P3BETACORE-1、伙伴对划分、Type A/B/C、Theorem 13/17、$\lambda$、$A_2$、$q_v$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 内蕴工具正控 命中文件数=1    :: ./P2-A-2026-09-27-intrinsic-tooling-positive-control-and-candidate-pool.md 
技术词 E3 形式化判据 命中文件数=1    :: ./P2-A-2026-09-27-intrinsic-tooling-positive-control-and-candidate-pool.md
```
- **本档新增**：内蕴 $\nu$ 工具与正控、候选池优先级、E3 形式化判据（见上方命中数；0 命中者为自造语／内部标签 ✓）
