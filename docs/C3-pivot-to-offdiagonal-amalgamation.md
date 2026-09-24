已查地图：命中（`C3-self-correction-s4-is-indefinite-not-degenerate`／`C3-d1992-table-and-s4-audit-point`／`C3-citeseerx-and-RGPF-relations-extracted`）⟹ 引用，不开新案
D0: 本档对象 = **主攻换轨**（弃 `P_4`、立**非对角** amalgamation、首测点 `(2,3)`）＋ 新量 `D(a,b)` 与 defect-word 证书 ＋ 本地状态核验
D1: 0 （[REVIEW] 轮次：换轨与核验，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **换轨：非对角 amalgamation `U_{a,b}`**

## §1 换轨决定（照录）

```
$$\boxed{P_4\ \text{不再作为开放攻击点}}$$ ✓（`H_4` indefinite、`\det H_4=-4`；`1992` 的 `P_s` 只对 `s=4` 说 likely；`2010` 只有有限商；`2008` 逐字：self-dual 有限仅 `(1,1),(2,0),(3,0)`）✓
$$\boxed{\text{主攻}=\mathcal U_{a,b}=\{\{3,6\}_{(a,0)},\{6,3\}_{(b,0)}\},\ a\ne b}$$ ✓✓
【首测点】 $$\boxed{(a,b)=(2,3)}$$：二维参数空间中最小非对角点之一，且**避开**已知已决的 `(1,1)`、`(2,0;2,0)`、`(3,0;3,0)`、`(3r,0;r,r)`、`(s,s;s,0)` ✓✓
```

## §2 ⭐ 新量：`intersection defect`（照录）

```
【框架】 `existence = group quotient + intersection property`；rank 4 需 $$\langle\rho_0,\rho_1,\rho_2\rangle\cap\langle\rho_1,\rho_2,\rho_3\rangle=\langle\rho_1,\rho_2\rangle$$ ✓
【新量】 $$D(a,b)=\frac{|\Gamma_{012}\cap\Gamma_{123}|}{|\Gamma_{12}|};$$ $$D(a,b)>1\ \Longrightarrow\ \Gamma_{a,b}\ \text{不是 string C-group}\ \Longrightarrow\ \mathcal U_{a,b}\ \text{不存在}$$ ✓✓
【证书格式（本档最看重）】 找到**结构化 word** `x` 且 $$x\in\Gamma_{012},\quad x\in\Gamma_{123},\quad x\notin I_2(6)\ \Longrightarrow\ \boxed{\mathcal U_{2,3}\ \text{不存在}}$$ ✓✓ —— **比"GAP 说不对"强得多，属真 `G4`** ✓
【压缩设想】 defect 只发生在小接口 $$I_2(6)\hookrightarrow\Gamma_{012},\Gamma_{123}$$ ⟹ `translation lattice → interface module → rank/kernel` ✓
```

## §3 ⚠️ 层次/记号纪律（本档提出，须核）

```
【须核 1】**regular C-group vs chiral（偶子群）** —— 字符串 C-group 的 intersection property 定义在 **C-group 设定**（`\rho_0,\ldots,\rho_3`）下；若改用 `\sigma_1,\sigma_2,\sigma_3`（`[3,6,3]^+`），需给出**两设定的翻译**（chiral 侧另有条件）⟹ **不得混用** ✓
【须核 2】**两条额外关系的落位** —— 与《Handbook》逐字吻合："quotients of Euclidean or hyperbolic Coxeter groups … obtained from those by **either one or two extra defining relations**" ✓；但 `T_L`／`T_R` 具体落在 **facet 侧 `\langle\rho_0,\rho_1,\rho_2\rangle`** 还是 **vertex-figure 侧 `\langle\rho_1,\rho_2,\rho_3\rangle`**，须按 `§11E/§11F` 核 ✓
```

## §4 本地状态核验（本轮，两源）

```
【扫描范围】 `RGPF-II`（`math/0601502`）＋ `MS2008`（`0805.3479`）中凡含 `\{3,6\}` 或 `\{6,3\}` 且带 `(2,0)`／`(3,0)` 的行 ✓
【结果】**未出现 `(2,0)` 与 `(3,0)` 的混合对** ⟹ `U_{2,3}` **两源均未提及** ✓
【出现的是】 `\{\{6,3\}_{(3,0)},\{3,6\}_{(3,0)}\}`（对角，两不同 polytope 同群阶 `1944`）；**`\{\{3,6\}_{(1,1)},\{6,3\}_{(3,0)}\}`（非对角，但 `(1,1)\ne(2,0)`）**；`\{\{3,3\},\{3,6\}_{(3,0)}\}`；`\{\{3,6\}_{(3,0)},\{6,4\}_4\}` ✓
【⟹ 判定】**`U_{2,3}` 既未被证实"已决"，也未被证实"开放"** ⟹ **须继续审计（`§11E/§11H` 清单）**，**不得猜** ✓✓
【⚠️ 附带纪律】 上述出现者均为**构造出的类成员**，**不是 universal 判定** ⟹ **不得反过来当作"该类已决"** ✓
```

## §5 状态表（照录）

```
$$\begin{array}{c|c}
P_4\ \text{Hermitian 零特征值}&\textbf{CLOSED}\ (\det H_4=-4)\\
P_4\ \text{universal finiteness}&\text{不再作为开放攻击点}\\
P_s\ \text{自对角线}&\text{不作为主攻}\\
1992\ \text{sparse families}&\textbf{CLOSED/已知}\\
\text{Problem 17 全参数分类}&\textbf{仍开放}\\
\text{非对角 }(a,0),(b,0)&\textbf{下一主线}\\
\text{首测点 }(2,3)&\text{先文献核验，再 intersection-defect 推导}\\
\end{array}$$ ✓
```

## §6 下一步（不计算）

```
**【第 1 步】** `U_{2,3}` 文献状态核验（需 `§11E/§11H` 清单或您提供页）⟹ 若已决 ⟹ **该点关闭**；若未 ⟹ 进第 2 步 ✓
**【第 2 步】** `intersection-defect` 推导：展开 `T_L^2=1`、`T_R^3=1`，追踪 `\Gamma_{012}\cap\Gamma_{123}\setminus I_2(6)` 中**最小非平凡 word**；若塌回 `I_2(6)` ⟹ 顺次推进 `(2,4),(3,4),(3,5)` ✓✓
**【⛔ 边界】** 若第 2 步只得到"未找到 word"⟹ **不得升格为"不存在"**；须区分"未找到"与"证明不存在" ✓
【纪律】 **不计算、不实现**；`C2` 暂停 ✓
【边界】 §1–§2、§5 为**照录您的裁示与设计**；§3 为**本档提出的须核项**；§4 为**本地实测**；未制造候选／未启动搜索／未碰 RH。

## §7 【技术词回查】（补录）
```
技术词 intersection property 命中文件数=1    :: ./C3-pivot-to-offdiagonal-amalgamation.md 
技术词 amalgamation     命中文件数=3    :: ./final-milestone-primitive-gap-2026-09-09.md ./C104-mechanism-extraction-audit-five-primitives-vs-archive-FZ2-FZ3.md ./C3-pivot-to-offdiagonal-amalgamation.md 
```
