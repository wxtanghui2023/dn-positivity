已查地图：已跑 scripts/prework_map_check.sh 119 整数性 同余 mod 11 P1 ⟹ 执行自 `PREIMAGE-2026-09-26`（同余 ✓）；本档为**对唐先生 2026-09-26 22:28 链条的逐步机器核验**（含一次**算术否证** ✓）；纯计算 ✓。
D0: 本档对象 = 同余链 $Df(x)\equiv0\pmod{3465}$ 的逐步核验（既有对象）
D1: 0（产出为否证：mod 11 支为恒等式）✗

# MOD11-CHECK-2026-09-26 · 逐步核验与算术否证

## §0 结论（先给）

```
$$\boxed{\textbf{唐稿第 5 步为\textbf{假}}:\ -1280\ {\equiv}\ 0\pmod{11}\ ✗\ \text{实际}\ (-1280)\bmod 11=\mathbf 7\ ✓\ (\text{验算 }1280=11\cdot116+4\ ⟹\ 1280\equiv4\ ⟹\ -1280\equiv-4\equiv7\ ✓)}$$
$$\boxed{\textbf{机器核验}:\ K=D g=(315,315,-70,-70,40,40,-48,-48,128,128,-1280)\ \text{的\ }11\ \text{个系数\ }\textbf{全部}\ \equiv7\pmod{11}\ ✗✗}$$
$$\boxed{\textbf{修正后的 mod 11 是\textbf{恒等式}}:\ 7\sum_{i=0}^{10}N_i(x)\equiv0\ \Longrightarrow\ \sum_iN_i(x)\equiv0;\ \text{而}\ \sum_iN_i(x)=\sum_yb(y)=1309=11\cdot119\equiv0\ ✗\ \text{——\textbf{不含 }b(x)\ \text{信息}}}$$
$$\Longrightarrow\ \textbf{"}b(x)\equiv1\pmod{11}\text{"及其后的 }\sum b=1024\ \text{矛盾\textbf{不成立}}\ ✗✗\ \text{（该 P1 为伪 ✓）}$$
$$
$$
```

---

## §1 逐步核验表（唐先生 10 步 ✓）

```
$$\begin{array}{c|l|l}
\text{步} & \text{唐稿} & \text{机器核验}\\
\hline
1 & D=3465 & ✓\ \text{正确}\\
2 & Dg_i\ \text{系数} & ✓\ \text{完全一致}:\ (315,315,-70,-70,40,40,-48,-48,128,128,-1280)\\
3 & f=Gb & ✓\ (11I-L=I+A\ \text{可逆 ✓})\\
4 & f\in\{0,1\}\Rightarrow Df\equiv0\ (\mathrm{mod}\ D) & ✓\ \text{正确}\\
\mathbf 5 & \mathbf K\bmod 11=(\ldots,0) & \mathbf{✗✗\ \text{全 11 个皆}\equiv7};\ \text{末项}\ (-1280)\bmod11=\mathbf7\ne0\\
6 & S_0+\cdots+S_4=1309-b(\bar x) & ✓\ (\text{注：应为 }b(\bar x)\ \text{即对径点 ✓，非 }b(x))\\
7 & 1309\equiv1\pmod{11} & \mathbf{✗}\ 1309=11\times119\equiv\mathbf 0\pmod{11}\\
8 & \Rightarrow b\equiv1\pmod{11} & ✗\ \text{由 5、7 之误所致}\\
9 & \Rightarrow b\equiv1 & ✗\\
10 & \text{与}\ \sum b=1309\ \text{矛盾} & ✗\ \text{前提已崩 ⟹ 无矛盾}\\
\end{array}$$
$$
$$
```

---

## §2 为何 mod 11 必然退化（结构性解释 ✓）

```
$$\textbf{恒等式来源}:\ \sum_{i=0}^{10}N_i(x)=\sum_y b(y)=1309=11\cdot119\ \text{对\textbf{一切} }x\ \text{成立}\ ✓$$
$$\qquad\Longrightarrow\ \text{任何"全部系数同余于同一值 }c\text{"的线性组合都退化为 }c\times1309\equiv0\ (\text{因 }11\mid1309\ ✓)$$
$$\Longrightarrow\ \textbf{mod 11 支\textbf{结构上}不可能给出 }b(x)\ \text{的约束}\ ✗\ \text{（非偶然 ✓）}$$
$$
$$
```

---

## §3 方法本身有效：其余模数给出**真**同余（✓ 但局部可满足 ✗）

```
$$\textbf{系数配对结构（唐先生观察 ✓ 正确）}:\ K_{2j}=K_{2j+1}\ (j=0..4)\ ✓\ \Longrightarrow\ \text{约化到 }S_j=N_{2j}+N_{2j+1}\ (j=0..4)\ \text{与}\ N_{10}\ ✓$$
$$\text{mod }9:\ (0,0,2,2,4,4,6,6,2,2,7)\ ✓;\quad \text{mod }5:\ (0,0,0,0,0,0,2,2,3,3,0)\ ✓;\quad \text{mod }7:\ (0,0,0,0,5,5,1,1,2,2,1)\ ✓$$
$$\textbf{局部可满足性检验（本档 ✓）}:\ \text{盒}\ S_j\in[\binom{10}{2j}+\binom{10}{2j+1},\ 3(\cdots)]\ ✓,\ \sum_jS_j+N_{10}=1309-b\ ✓$$
$$\qquad\Longrightarrow\ \textbf{找到显式可行解}:\ b=1,\ (S_0..S_4)=(11,165,462,331,126),\ N_{10}=213\ ✓\ \Longrightarrow\ \textbf{无矛盾}\ ✗$$
$$
$$
```

---

## §4 判定（按四门链 ✓）

```
$$\textbf{整数性（局部同余）支}:\ \text{四门中第 3 门（敏感）成立 ✓、第 4 门（方向）为等式 ✓ —— 但\textbf{局部可满足} ⟹ 无杠杆}\ ✗$$
$$\qquad\Longrightarrow\ \text{若要在此支取 P1，只能靠\textbf{跨 }x\ \text{的全局一致性}＋profile（CP-SAT 级 ⚠️）——即回到完整的 }0/1\ \text{条件（＝原问题 ⚠️）}$$
$$\textbf{119 状态}:\ \text{维持 }\texttt{BLOCKED — no known D>0 mechanism}\ ✓\ \text{（}\text{PREIMAGE}\ \text{档的重定位仍有效 ✓：}A_1\text{-route}\ne\text{problem}）$$
$$\textbf{纪律留痕}:\ \text{本档再次验证"先跑后写"：}\textbf{任何 P1 主张必须先过算术核验}\ ✓✓\ \text{（本次在提交前拦住 ✗）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§1 为**机器核验**（精确有理数 ＋ 模运算 ✓）；§2 为**结构性解释** ✓
- §3 的可行解为**显式构造** ✓（仅证明局部无矛盾 ✓，不证明真实码存在 ✗）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张同余支无用 ✗（只主张其局部形式无杠杆 ✓）
- 本轮未跑 solver ✓（仅模运算与穷举局部 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 mod 11 支的恒等式判定 命中文件数=1    :: ./MOD11-CHECK-2026-09-26-arithmetic-refutation.md 
技术词 同余支的局部可满足性 命中文件数=1    :: ./MOD11-CHECK-2026-09-26-arithmetic-refutation.md
```
- **本档新增**：mod 11 支的恒等式判定、同余支的局部可满足性（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：精确有理核、四门链、profile、1309=11×119
