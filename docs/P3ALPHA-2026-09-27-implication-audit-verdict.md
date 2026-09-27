已查地图：已跑 scripts/prework_map_check.sh P3-α B₂ q_v implication audit ⟹ 执行自 `P2-LOCK-2026-09-27-...`（✓）＋ 唐先生 13:28（开 P3-α，先审计禁计算 ✓）；本档 = **P3-α 判定：PASS（含归属更正 ✓）** ✓。
D0: 本档对象 = 文献距离/重量分布层能否蕴含 alignment 量子化
D1: 2（**implication 审计 ✓✓**；**归属更正（matching 已在文献 ✓）**）

# P3-α implication audit 判定（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BR-1 ⭐P3-}\alpha=\textbf{PASS ✓✓)}\ \text{文献的距离/重量分布层\textbf{不能}蕴含 alignment 量子化}\ ✓\ \text{—— 且有\textbf{自足证明}:}}$$
$$\qquad\text{我们自己的三个 }n=8\ \text{见证码（}P12\text{-PASS 档 ✓）拥有\textbf{完全相同的全距离分布}}\ A=(0,16,160,176,64,48,32,0)\ ✓\ \text{而 }q\ \text{不同（}J_7\in\{64,128,256\}\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{文献的 }B_i=B_i(\text{距离多重集})\ \text{对三者相同 ✓};\ \text{而 }q_v\ \text{不同 ✓}\ \Longrightarrow\ \boxed{B\ \not\Rightarrow\ q}\ \textbf{逐例否证} ✓✓$$
$$\boxed{\textbf{(BR-2 归属更正 ⚠️！)}\ \textbf{"完美匹配"半部分\textbf{已在文献}}: §II\ \text{Cor}\,14(2)\ \text{证明逐字}:\ \textit{"for each codeword }\mathbf c_1\in\mathcal C_1\text{ there exists }\mathbf c_2\in\mathcal C_2\text{ such that }d(\mathbf c_1,\mathbf c_2)=1"} ✓}$$
$$\qquad\Longrightarrow\ \text{我方的双计数引理（}H\leftrightarrow C_2\ \text{完美匹配 ✓）＝\textbf{文献的重推导} ✗，\textbf{不列为新结果}} ✓\ \text{（诚实标注 ✓）}$$
$$\boxed{\textbf{(BR-3 未覆盖层 ✓✓)}\ \text{文献\textbf{无 syndrome 语言}（关键词命中 }0\ ✓\text{）};\ \text{无 affine support 陈述};\ \text{无 }(d',s)\ \text{转移结构};\ \Longrightarrow\ \textbf{量子化律 + 仿射支撑律属未覆盖层} ✓✓}$$
$$
$$
```

---

## §1 文献层实际给了什么（**✓ 逐字取证**）

```
$$\text{(a) 距离分布（}§IV\text{ 定义 ✓）}:\ B_i=\frac1M\big|\{(\mathbf c,\mathbf c')\in\mathcal C^2:\ \mathsf d(\mathbf c,\mathbf c')=i\}\big|\ ✓;\ \text{且 }\mathbf B=\frac1M\sum_{\mathbf e\in\mathcal C}\mathbf A_{\mathbf e+\mathcal C}\ \text{（eq 7 ✓）}\ \Longrightarrow\ \textbf{平移平均的重分布} = \text{距离多重集} ✓$$
$$\text{(b) Theorem 20（✓）}:\ \mathrm{Supp}(\mathbf B')\subseteq\{0,n/2,n/2+1\}\ ✓\ \text{——\textbf{变换层}结果（}\mathbf B'\ \text{由 MacWilliams 变换 ✓）}$$
$$\text{(c) §V（✓）}:\ \text{"a class of }\textbf{Type A}\text{ codes in which the number of codeword pairs }\{\mathbf c,\mathbf c'\}\text{ that differ }\textbf{only on any given coordinate}\ \text{is the same for all coordinates"}\ ✓\ \text{——\textbf{概念先例} ✓\ 但}:\ \text{(i) 限 Type A};\ \text{(ii) 要求\textbf{全坐标相等}（对称性 ✓）而非量子化律};\ \text{(iii) Type B 时该量恒为 }0\ (A_1{=}0\ ✓)\ ✓$$
$$\text{(d) 重量分布（}§IV\text{ ✓, Theorem 4 ✓）}:\ \text{零化 NP1CC 恰两种重分布（Type A 一种、Type B 一种、Type C 共享 ✓）}\ \Longrightarrow\ \textbf{Type C 内部不可分} ✗\ \text{——正是我们 }(A_1,A_2)\ \text{分叉的粗化 ✓}$$
$$
$$
```

---

## §2 审计裁决表（**✓**）

```
$$\begin{array}{c|c|c}
\text{我方命题} & \text{文献状态} & \text{裁决}\\
\hline
H\leftrightarrow C_2\ \text{完美匹配} & §II\ \text{Cor}\,14(2)\ \text{证明内 ✓} & \textbf{重推导，不新} ✗\\
\text{距离分布层（}B_i,\ A_i\text{）} & §IV ✓\ \text{完整} & \text{已覆盖 ✓}\\
\text{坐标方向计数（概念）} & §V\ \text{对 Type A ✓} & \text{概念先例 ✓}\\
q_v\in\{0,\lambda\}\ \text{常值性} & \textbf{未出现} ✗ & \textbf{新} ✓\\
\mathrm{supp}(q)=(s+\mathrm{Im}f)\cap(\mathbb F_2^m\setminus\{0\}) & \textbf{未出现} ✗ & \textbf{新} ✓\\
|S|=2^{d'}-\mathbf 1_{[s\in\mathrm{Im}f]}\ \text{（仅 }n{=}2^m{-}1\text{）} & \textbf{未出现} ✗ & \textbf{新} ✓\\
J=A_2^2/|S| & \textbf{未出现} ✗ & \textbf{新} ✓\\
\end{array}$$
$$\textbf{判据（唐先生 ✓）}:\ \text{文献只给"由 Type/weight profile 决定的标量"（}B_2\ \text{层 ✓）；\textbf{不能}不加新论证推出 }q\ \text{的 support/multiplicity ⟹ }\boxed{\textbf{P3-}\alpha=\textbf{PASS}}\ ✓✓$$
$$
$$
```

---

## §3 与 2026 新工作的关系（**✓ 二次检查**）

```
$$\text{Etzion--Krotov--Shi--Song (arXiv:2605.12148, 2026 ✓)}\ \text{统一 1-perfect / extended perfect / NP1CC / extended NP1CC / diamond codes 的\textbf{重量分布} ✓}$$
$$\qquad\Longrightarrow\ \text{统一层仍是 }\textbf{weight distribution} ✓\ \text{（即 §2 的"已覆盖层" ✓）};\ \text{不触及 coordinate/syndrome-direction 层 ✓}\ \text{——与唐先生判断一致 ✓}$$
$$
$$
```

---

## §4 边界与下一步（**✓**）

```
$$\text{P3-}\alpha=\textbf{PASS}（q\ \text{层未被覆盖 ✓）；\ \text{但\textbf{归属必须诚实}}: matching 半部分属文献 ✓\ \text{（Cor 14 ✓），我方新增 = \textbf{量子化 + 仿射支撑 + }(d',s)\ \text{转移结构} ✓}$$
$$\text{下一步候选（禁计算 ✓）}:\ \text{(甲) 与 §V 的 Type A 坐标类对照，看量子化律在 Type A 是否有对应物（可能给"两类方向的统一" ✓）};\ \text{(乙) P3-}\beta\ \text{（分类剪枝 ✓）};\ \text{(丙) 若要求更进一步，则须问"量子化能否对独立对象给界"（P3-}\gamma\ ✓，险 ⚠️）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：P3-α implication 判定、归属更正（matching 在文献 ✓）、裁决表
- **档案已有（引用，不列为提出）**：P12-PASS、A-ALIGNTHM-1、Theorem 13、Cor 14、$B_i$、$J_7$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 implication 判定 命中文件数=1    :: ./P3ALPHA-2026-09-27-implication-audit-verdict.md 
技术词 归属更正     命中文件数=3    :: ./two-cover-explicit-construction.md ./P3ALPHA-2026-09-27-implication-audit-verdict.md ./FACE-CLOSURE-2026-09-26-structural-refinement.md
```
- **本档新增**：P3-α implication 判定、归属更正（matching 在文献）、裁决表（见上方命中数；0 命中者为自造语／内部标签 ✓）
