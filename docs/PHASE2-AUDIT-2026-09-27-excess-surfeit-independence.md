已查地图：已跑 scripts/prework_map_check.sh excess surfeit 独立约束 换皮 ⟹ 执行自 `ALIGN-2026-09-25`／`EXCESS-2026-09-25`／`M2-PREWORK-2026-09-27`（✓）＋ 唐先生 12:13（审计 ✓）；本档 = **excess/surfeit 独立性审计（结论：STOP ✓）**。
D0: 本档对象 = excess/surfeit 是否给出 $A_1+A_2$ 之外的独立约束
D1: 0（审计 ＋ 换皮判定 ✓，不产生新数学命题 ✓）

# excess/surfeit 独立性审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AG-1 二阶层 = 换皮 ⟹ STOP ✓)}\ \sum_x\delta=\mathbf E\ ✓;\qquad \sum_x\delta^2+\sum_x\delta=4(A_1+A_2)\ \Longrightarrow\ \sum_x\delta^2=4(A_1+A_2)-\mathbf E\ ✓}$$
$$\qquad\Longrightarrow\ \text{excess 矩层级 }(\sum\delta,\ \sum\delta^2)\ \textbf{恒等于}\ (E,\ 4(A_1+A_2)-E)\ \Longrightarrow\ \text{二阶\textbf{无独立信息} ✗} \Longrightarrow \textbf{profile reparameterization} ✓$$
$$\boxed{\textbf{(AG-2 唯一非换皮对象 = surfeit }\zeta\ ✓，但档案已 BLOCK ✗)}\ \zeta=\sum_{v\notin C}\big(\mathrm{ball}(v)-1\big)\ \text{依赖码字\textbf{排列}（非仅 profile ✓）}\ \text{⟹ 非换皮 ✓}$$
$$\qquad\text{但}:\ \textbf{M-2A′ = BLOCKED}\ ✗\ \text{（割的有效性未证 ✗ ＋ pair 链不能闭合 ✗）—— 档案 }M2\text{-PREWORK-2026-09-27}\ ✓$$
$$\boxed{\textbf{(AG-3 结构结论 ✓)}\ \text{覆盖侧 → 距离侧的跨越，需要\textbf{同时超出 profile 与 excess 矩}的输入} ✓\ \text{（与档案"van Wee 强度之墙"一致 ✓）}}$$
$$
$$
```

---

## §1 档案原定义（逐字 ✓）

```
$$\delta(x):=|C\cap B_1(x)|-1\ \ge0\ ✓;\qquad \sum_x\delta(x)=(n+1)|C|-2^n=E\ ✓\ \text{（EXCESS-2026-09-25 L19 ✓）}$$
$$\sum_x\binom{m(x)}2=\sum_{\{c,c'\}}|B_1(c)\cap B_1(c')|=2(A_1+A_2)\ ✓;\qquad \Longleftrightarrow\ \boxed{\sum_x\delta^2+\sum_x\delta=4(A_1+A_2)}\ ✓\ \text{（同档 L21--22 ✓，\textbf{二阶恒等式} ✓）}$$
$$\zeta=\sum_{v\notin C}\big(\mathrm{ball}(v)-1\big),\quad \mathrm{ball}(v)=\sum_{u\in N[v]}\delta(u)\ ✓\ \text{（ALIGN L20/38 ✓；surfeit ＝ }S=V\ \text{的 }D\text{ 外部分 ✓）}$$
$$\text{档案已记}:\ \text{"}\sum_i\delta_i(x)=E\ \text{并非独立不变量}"\ ✓\ \text{（ALIGN L22 ✓——层重分配 ✓）；"surfeit 含二阶信息 ✓，但割的\textbf{有效性未证} ✗"（ALIGN L34/L54 ✓）}$$
$$
$$
```

---

## §2 换皮的代数证明（**两行 ✓**）

```
$$\delta=b-1\ \Longrightarrow\ \sum_x\delta=\sum_xb(x)-2^n=\underbrace{M(n+1)-2^n}_{=E}\ ✓\ \text{—— 一阶：}\textbf{已被 }M,K\ \text{钉死} ✓$$
$$\sum_x\delta^2+\sum_x\delta=\sum_x(b-1)b=2\sum_x\binom{b(x)}2=4(A_1+A_2)\ ✓\ \Longrightarrow\ \sum_x\delta^2=4(A_1+A_2)-E\ ✓$$
$$\Longrightarrow\ \text{excess 的全部一、二阶矩 ＝ }(E,\ A_1+A_2)\ \text{的函数} \Longrightarrow\ \textbf{与 }\sum_jN_j,\ \sum_jjN_j,\ \sum_jj(j-1)N_j\ \text{同一线性包络} ✗\ \Longrightarrow\ \textbf{换皮} ✓$$
$$\text{与唐先生判据对照 ✓}:\ \text{"完全落在 }\sum N_j=2^n,\ \sum jN_j=2^n+E,\ A_{\le2}=\frac12\sum j(j-1)N_j\ \text{的线性包络里"\ ⟹ 成立 ✓ ⟹ **STOP** ✓}$$
$$
$$
```

---

## §3 数值核对（**✓ 本机**）

```
$$\text{用 }n=9\ \text{档案 profile }\{1{:}432,2{:}62,3{:}8,4{:}10\}\ ✓:\ \sum b=620\ ✓,\ \sum b^2=912\ ✓\ \Longrightarrow\ \sum\delta=108=E\ ✓,\ \sum\delta^2=184\ ✓$$
$$\text{恒等式}:\ \sum\delta+\sum\delta^2=292=4(A_1+A_2)=4\cdot73\ ✓✓\ \text{—— 完全吻合 ✓}$$
$$
$$
```

---

## §4 surfeit 的非换皮性与既有 BLOCK（**诚实 ✓**）

```
$$\zeta\ \text{为何非换皮 ✓}:\ \zeta=\sum_{u}\delta(u)\cdot\#\{v\notin C:\ u\in N[v]\}-|V\setminus C|\ ✓\ \text{—— 权依赖于"哪些 }v\ \text{是非码字"\ ⟹ 依赖\textbf{排列} ✓，非仅 }(N_j)\ ✓$$
$$\text{但在 }z\text{-变量下}\ \zeta\ \text{是\textbf{双线性}}:\ \zeta=\sum_v(1-z_v)(\mathrm{ball}(v)-1),\ \mathrm{ball}(v)-1=\sum_{u\in N[v]}(\sum_{c}[u\in B_1(c)]z_c-1)\ ✓\ \text{（ALIGN L63 ✓）}$$
$$\text{档案 BLOCK ✓}:\ \text{(i)}\ \text{候选割 }B\ \text{在均匀点}=-(10/11)1024=-930.9091<0\ \text{但\textbf{有效性未证} ✗};\ \text{(ii)}\ \text{pair 链不能闭合 ✗} \Longrightarrow\ \textbf{M-2A′ BLOCKED}\ ✓$$
$$
$$
```

---

## §5 结构性结论与下一步（**不给假出路 ✓**）

```
$$\text{① 换皮判定}:\ \textbf{excess 矩 → profile → 前两矩+二阶阶乘矩}\ \text{全在该线性包络内} ✗\ \Longrightarrow\ \textbf{STOP} ✓\ \text{（唐先生 12:13 判据 ✓）}$$
$$\text{② 独立性：无} ✗:\ \text{未发现涉及 }A_i\ \text{的新关系（除 }A_{\le2}=A_1+A_2\ \text{本身 ✓，即 §2 的恒等式 ✓）}$$
$$\text{③ 因此"第二层 LP（Delsarte + excess）"}\ \textbf{不加} ✗\ \text{—— 因 excess 只能重述 }A_1+A_2\ ✓,\ \text{而纯 Delsarte 的上界已松 }4\sim16\times\ ✗$$
$$\text{④ 唯一存活方向}:\ \text{真正跨到\textbf{局部几何}的耦合} ✓\ \text{（如 surfeit 的有效性证明 ✓，或 }A_j(x)\ \text{分层场 }δ_i(x)=(n+1-i)A_{i-1}(x)+A_i(x)+(i+1)A_{i+1}(x)-\binom ni\ \text{的独立约束 ✓ —— 档案 EXCESS L111 ✓）}$$
$$\qquad\text{但后者仍是 }A\ \text{的线性组合} ⚠️\ \text{—— 若只给出 }A\ \text{的线性关系 ⟹ 仍可能与 LP 重复 ⟹ 须再测 ✓}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 逐字引档案 ✓；§2–§3 为**证明 ＋ 本机核对** ✓；§4–§5 为**既有 BLOCK 引用 ＋ 结构结论** ✓
- **未**登记任何"机制找到" ✗；**未**加入任何新 LP 约束 ✓（遵唐先生"不直接塞 excess" ✓）
- **未**改动 119 UNKNOWN ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：excess/surfeit 独立性审计、换皮代数证明、二阶恒等式对齐
- **档案已有（引用，不列为提出）**：$\delta$、$\zeta$、二阶恒等式、M-2A′、$A_j(x)$ 分层场、Haas、Wu--Chen


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 独立性审计  命中文件数=17   :: ./C3899l-k-le-3-cheap-certificates-first-cut-41-closed.md ./p2iv-selberg-riemann-bridge.md ./PHASE2-AUDIT-2026-09-27-excess-surfeit-independence.md 
技术词 换皮代数证明 命中文件数=1    :: ./PHASE2-AUDIT-2026-09-27-excess-surfeit-independence.md
```
- **本档新增**：excess/surfeit 独立性审计、换皮代数证明、二阶恒等式对齐（见上方命中数；0 命中者为自造语／内部标签 ✓）
