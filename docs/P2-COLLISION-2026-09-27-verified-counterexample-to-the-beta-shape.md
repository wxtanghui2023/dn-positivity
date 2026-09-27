已查地图：已跑 scripts/prework_map_check.sh P2 collision 反例 flatness 违反 ⟹ 执行自 `P2-A-STEP2-2026-09-27-...`（✓）＋ 唐先生 13:52（source gate 解除 ✓）；本档 = **已验证 P2 反例（NP1CC ⊄ Theorem-13 β-shape）** ✓。
D0: 本档对象 = β-shape 通用性的反例（λ-依赖）
D1: 3（**反例（已验证 ✓✓）**；**两处实现 bug 更正 ✓**；**A-ALIGNTHM-1 适用范围收紧 ✓**）

# ⭐ P2 COLLISION（已验证）：2026-09-27

## §0 结论（先给）

```
$$\boxed{\textbf{(CA-1 🎯 反例存在 ✓✓)}\ \text{取 }C=(H_{15},0)\cup(V_\lambda,1)\ \text{其中 }V_\lambda=\{(x,\ x+c,\ p(x)\oplus\lambda(c))\},\ \lambda(c)=\mathbf 1[c\ne0]\Longrightarrow}$$
$$\qquad\textbf{(i) }V_\lambda\ \text{为完美码 ✓（掩码法 ＋ \textbf{修正版}暴力法 双验，400 目标 0 未覆盖 ✓✓）};\quad \textbf{(ii) }C\ \text{为 NP1CC ✓✓（}|C|=4096=2^{16}/16\ ✓,\ \text{覆盖 200 目标 0 未覆盖 ✓};\ \max b=2\ ✓,\ |Z|=M=4096\ ✓\text{）}$$
$$\qquad\textbf{(iii) 但其 β-不变量\textbf{不满足 flatness}} ✗:\ \nu=\{1:288,\ 2:1760\}\ \text{（star ✓ 公共坐标 }=15\ ✓\text{）},\ \text{但切片 }q_v\in\{288,224\}\ \textbf{两值} ✗;\ A_2/|S|=1760/7=251.43\notin\mathbb Z ✗$$
$$\qquad\Longrightarrow\ \boxed{\mathrm{NP1CC}\not\subseteq\text{Theorem-13 β-shape}}\ ✓✓\ \text{——\textbf{首个已验证反例（α 的 b≤2 与 ν 的 star 仍成立，唯独量化/平坦性崩溃 ✓）}}$$
$$\boxed{\textbf{(CA-2 对照（同构架，不同 }\lambda\textbf{）)}\ \lambda\equiv0\ (\text{线性 }V ✓)\ \text{与}\ \lambda=c_0c_1\ (\text{非线性 }V ✓)\ \textbf{均通过} ✓\ (\nu=\{1:256,2:1792\},\ \text{切片}\equiv256,\ A_2/|S|=256\in\mathbb Z ✓)}$$
$$\qquad\Longrightarrow\ \textbf{β-shape 的成立与否\textbf{依赖具体半码}}，不是构架自动性质 ✓✓\ \text{（这是比"单例通过/单例失败"更强的结构信息 ✓）}$$
$$
$$
```

---

## §1 三例完整数据（**✓ 每例均双验覆盖**）

```
$$\begin{array}{c|c|c|c|c|c|c}
\lambda & V\ \text{覆盖(掩码/暴力)} & k=|C_1\cap V| & C\ \text{覆盖(掩码/暴力)} & \nu & \text{切片} & \text{flatness}\\ \hline
0 & ✓/0 & 256 & ✓/0 & \{1{:}256,2{:}1792\} & 256 & ✓\\
\mathbf 1[c\ne0] & ✓/0 & \mathbf{288} & ✓/0 & \{1{:}288,2{:}\mathbf{1760}\} & \mathbf{\{288,224\}} & \mathbf{✗}\\
c_0c_1 & ✓/0 & 256 & ✓/0 & \{1{:}256,2{:}1792\} & 256 & ✓\\
\end{array}$$
$$\text{逐坐标计数（}\lambda=\mathbf 1\text{）}:\ [288,288,288,224,224,224,224]\ \text{对支撑 }\{1,3,5,8,10,12,14\}\ ✓ \Longrightarrow \text{多重集 }\{288^3,224^4\}\ \textbf{是码不变量} ✓$$
$$\qquad\Longrightarrow\ C(\lambda=\mathbf 1)\ \textbf{不与任何族内码等价} ✗\ \text{（族内切片恒定 ✓）};\ \text{且 }A_1+A_2=288+1760=2048=M/2\ ✓\ \text{（等号链仍成立 ✓）}$$
$$
$$
```

---

## §2 两处实现 bug（**✓ 均已定位并更正；这是本轮全部错误的根源**）

```
$$\text{(bug-1)}\ \text{第三块未截单比特}（(\mathrm{wt}\oplus\lambda)\ll14\ ✗）\ \Longrightarrow\ \text{字越界 }\ge2^{17};\ \text{更正}: \&1\ ✓\ \text{（此后形状 A 立即通过 ✓）}$$
$$\text{(bug-2)}\ \text{暴力检验把目标点写在生成式内部}（\text{每次比较重抽} ✗）\ \Longrightarrow\ \text{伪"未覆盖"计数};\ \text{更正}: \text{先固定目标列表} ✓$$
$$\qquad\Longrightarrow\ \textbf{纪律两次生效 ✓}:\ \text{第一次差点让我把"正确公式"误判为"必然失败" ✗};\ \text{第二次差点让我把"真反例"误判为"非法对象" ✗}$$
$$
$$
```

---

## §3 资产层面的含义（**✓ 重要**）

```
$$\text{(i) A-ALIGNTHM-1 \textbf{仍成立} ✓\ \text{但只对\textbf{线性半码族}}（}C_2=\pi H+e\ ✓\text{）——\textbf{不得}再当作全体 NP1CC 的通用不变量 ✗}$$
$$\text{(ii) P1-2 PASS（}\exists\text{同 }(A_1,A_2)\text{ 桶内 }J\text{ 分叉）\textbf{仍成立} ✓\ \text{（族内真命题 ✓）}}$$
$$\text{(iii) }\textbf{"β-shape 猜想"（Theorem-13 形 }\Longrightarrow\text{ gate）被\textbf{否证} ✗\ \text{——本档即证书 ✓}}$$
$$\text{(iv) 反例的\textbf{规模} }: \text{两值 }\{288,224\}\ \text{的差 }=64=2^6\ ✓;\ \text{且 }288=2^5\cdot9\ ✓,\ 224=2^5\cdot7\ ✓ \Longrightarrow \text{是否一般形如 }2^{?}\cdot(2^{d'}\pm c)\ \text{——待查 ✓（候选新问题 ✓）}$$
$$
$$
```

---

## §4 边界与下一步（**✓**）

```
$$\text{(甲) }\lambda\ \text{依赖图谱}:\ \text{哪些 }\lambda\ \text{给 flat、哪些不给？}\ \text{（}2^{15}\ \text{个 }\lambda\ \text{中做结构化分类 ✓；}\lambda=\mathbf 1[c\ne0]\ \text{属于"非代数"型 ✓）} \Longrightarrow \text{可能出现"flat }\iff \lambda\ \text{代数性"判据 ✓}$$
$$\text{(乙) 反例稳定性}:\ \text{换 }C_1\ \text{（其它长度 15 完美码 ✓）与 }V\ \text{的坐标置换 ✓，看 flatness 何时恢复 ✓}$$
$$\text{(丙) ENP1CC puncturing};\qquad \text{(丁) 119 主线重定位（你说过暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：已验证 P2 反例（λ=𝟙 时 flatness/量化崩溃）、两处实现 bug 更正、A-ALIGNTHM-1 适用范围收紧
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-VASILEV-1、A-E3-1、A-PERFCOND-1、内蕴 $\nu$、Theorem 13


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 P2 反例        命中文件数=3    :: ./P2-COLLISION-2026-09-27-verified-counterexample-to-the-beta-shape.md ./P2-A-2026-09-27-intrinsic-tooling-positive-control-and-candidate-pool.md ./P2-E1-2026-09-27-intrinsic-gate-definition-and-the-audit-plan.md 
技术词 flatness 崩溃  命中文件数=0    ::
```
- **本档新增**：已验证 P2 反例（$\lambda=\mathbf 1$ 时 flatness/量化崩溃）、两处实现 bug 更正、A-ALIGNTHM-1 适用范围收紧（见上方命中数；0 命中者为自造语／内部标签 ✓）
