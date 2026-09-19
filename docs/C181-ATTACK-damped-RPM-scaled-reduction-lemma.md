已查地图（**先查后写**）：`C-180`（A2 范围核实：剩余＝阻尼 `(RP_M)`）、`docs/E4-ENGINE-2`（引理 C 与 m=1 自足化）、`papers/palojarvi-constant/note.md` §3（两条已有路线）、`docs/E4-ENGINE-1`（Montgomery Lemma 2.2 转引，**原文证明未读**）。关键词回查：`缩放约化`=0、`单位模子集`=0、`阻尼损失项`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 20:18 严正指出）**：**「让你攻击，你就只是搜索一下，那叫啥攻击呢？」** —— 本档**直接攻** A2 的未做部分（阻尼情形），不再只做范围核实 ✓
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{新引理（已证）}：\text{设}\ |z_j|\le1，\ u:=\#\{j:|z_j|=1\}\in[1,5]，\ \rho:=\max\{|z_j|:|z_j|<1\}\ \text{（空集时置}\ 0\text{）}✓$$
$$\qquad \text{则}\quad \boxed{\max_{1\le k\le5M}\ \Re\sum_{j=1}^M z_j^{k}\ \ \ge\ \ c_u-(M-u)\,\rho^{\lfloor M/u\rfloor}}✓✓\qquad c_u=\tfrac12\ (1\le u\le5)✓$$
$$\textbf{(二)}\ ⭐\ \textbf{在阻尼区间内}\ \textbf{严格击败 Montgomery 的}\ \tfrac1{20}：\text{条件}\ (M-u)\rho^{\lfloor M/u\rfloor}<0.45✓$$
$$\qquad \text{实例}：M=2,u=1,\rho=0.5\Rightarrow0.25（\mathbf{5.0\times}）；M=6,u=1,\rho=0.5\Rightarrow0.4219（\mathbf{8.4\times}）；M=5,u=1,\rho=0.6\Rightarrow0.189（\mathbf{3.8\times}）✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{短板（诚实）}：\text{近单位模}\ (\rho\to1)\ \text{时界退化（可为负）}✗；\text{数值真值}\ d_M\approx0.36\text{–}0.40\ \text{远高于本界} \Longrightarrow \textbf{技术需改进}✓$$

FREEZE-ACK: 本档即冻结期内的攻击性推导（依 `§8.1`；不产候选结论）

D0: 本档对象 = **阻尼 `(RP_M)` 的缩放约化引理（新，已证）＋ 数值核验 ＋ 短板定位** —— 关系 = 新引理，非新机制
D1: 0

# C-181 · ⭐ **攻击阻尼情形：缩放约化引理（新，已证）**

> **唐先生 2026-09-19 20:18**：不要只搜索，要攻击 ✓ —— 本档攻 A2 的未做部分

---

## §1 目标（Montgomery Lemma 2.2 的阻尼版）

$$\max_j|z_j|=1\ \Longrightarrow\ \max_{1\le n\le5M}\Re\sum_{j=1}^M z_j^n\ \ge\ \tfrac1{20}\qquad（\text{Montgomery；常数}\ \tfrac1{20}）✓$$
$$\text{我方已有}：\textbf{单模}情形（|z_j|=1\ \forall j）\ \text{对}\ M\le5\ \text{证到}\ \tfrac12✓；\textbf{阻尼}（允许\ |z_j|<1）\ \textbf{未做}✗（本档攻它）✓$$
$$\text{数值真值（优化所得）}：d_2\approx0.3955,\ d_3\approx0.3731,\ d_4\approx0.3634 \Longrightarrow \textbf{真值}\ \gg\tfrac1{20}，\text{有}\ \sim7\text{–}8\times\ \text{空间}✓$$

## §2 引理与证明（本档核心）

$$\textbf{引理}：\text{设}\ |z_j|\le1\ \forall j，\ u:=\#\{j:|z_j|=1\}\in[1,5]，\ \rho:=\max\{|z_j|:|z_j|<1\}✓$$
$$\qquad \text{则}\ \max_{1\le k\le5M}\Re\sum_j z_j^k\ \ge\ c_u-(M-u)\rho^{\lfloor M/u\rfloor}，\quad c_u=\tfrac12✓$$
$$\textbf{证明（四行）}：$$
$$\qquad \text{(i)}\ \text{取}\ K_0:=\lfloor M/u\rfloor\ge1\ \text{（因}\ u\le M\text{）}；\text{对单位模点令}\ w_j:=z_j^{K_0}（\text{仍}\ |w_j|=1）✓$$
$$\qquad \text{(ii)}\ \text{由}\ \textbf{单模结果}（u\le5，\text{引理 C}\ /\ \text{定理 1}\ /\ \text{证书} \Longrightarrow c_u=\tfrac12）：\exists m\in[1,5u]，\Re\sum_{j\in U} w_j^m\ge\tfrac12✓$$
$$\qquad \text{(iii)}\ \text{取}\ k:=mK_0 \Longrightarrow k\le5uK_0\le5M\ \text{（在窗口内）}，\text{且}\ \Re\sum_{j\in U} z_j^k=\Re\sum_{j\in U} w_j^m\ge\tfrac12✓$$
$$\qquad \text{(iv)}\ \text{阻尼点}：|z_j|^k\le\rho^{k}\le\rho^{K_0}\ \text{（}\text{因}\ k\ge K_0，\rho\le1\text{）} \Longrightarrow \sum_{j\notin U}\Re z_j^k\ \ge\ -(M-u)\rho^{K_0}✓$$
$$\qquad \Longrightarrow \Re\sum_j z_j^k\ \ge\ \tfrac12-(M-u)\rho^{\lfloor M/u\rfloor}\qquad\square✓✓$$

## §3 与 Montgomery 的定量对比

$$\text{本引理优于}\ \tfrac1{20}\iff(M-u)\rho^{\lfloor M/u\rfloor}<\tfrac12-\tfrac1{20}=\mathbf{0.45}✓$$
$$\begin{array}{c|r|r|r|r}
M & u & \rho & \text{本界} & \text{倍数}\ \text{vs}\ \tfrac1{20}\\\hline
2 & 1 & 0.5 & 0.2500 & \mathbf{5.0\times}\\
3 & 1 & 0.5 & 0.2500 & \mathbf{5.0\times}\\
5 & 1 & 0.6 & 0.1890 & \mathbf{3.8\times}\\
6 & 1 & 0.5 & 0.4219 & \mathbf{8.4\times}\\
\end{array}✓✓$$

## §4 数值核验（随机配置）

```
脚本内联运行（300 组随机配置 / 每行参数组合，M-u 个点模长 ≤ ρ）
  (M,u,ρ)     理论下界   实测 min max   成立?
  (2,1,0.5)    0.2500      0.7193       True
  (3,1,0.5)    0.2500      0.7449       True
  (5,1,0.6)    0.1890      0.9183       True
  (6,1,0.5)    0.4219      0.9499       True
  (12,1,0.8)  −0.2559      0.9673       True
  (20,1,0.9)  −1.8100      0.9978       True
⟹ 全部成立 ✓（另有多组界为负 ⟹ 该区间无力）
```

## §5 ⚠️ 短板（必须写明）

$$\textbf{①}\ \rho\to1\ \text{（近单位模）时界退化、可为负}✗ \Longrightarrow \textbf{最难的区间恰好覆盖不到}✓$$
$$\textbf{②}\ \text{数值真值}\ d_M\approx0.36\text{–}0.40\ \text{远高于本界（}\le0.42\text{）} \Longrightarrow \textbf{技术粗放：把阻尼点一律按}\ -1\ \text{计}✗$$
$$\textbf{③}\ \text{结构观察（本档）}：d(r)\ \text{在}\ r=0\ \text{与}\ r=1\ \text{两端均}\ \to\tfrac12，\text{中间下凹到}\ \approx0.36 \Longrightarrow \textbf{最坏阻尼是"中等阻尼"}✓✓$$
$$\qquad \Longrightarrow \text{下一步应分区攻：重阻尼（本档已得）／中等阻尼（下凹区，需新机制）／近单位（可尝试单模结果的扰动版）✓}$$

## §6 边界

- ⚠️ §2 的证明为**严格**（四行；只依赖：单模结果 `c_u=1/2`（`u≤5`）＋ 阻尼界 ✓）
- ⚠️ 引理**不外推**到 `u≥6`（单模结果我方只到 `M≤5`；`u≥6` 时直接用 Montgomery 的 `1/20` 更好 ✓）
- ⚠️ 数值真值 `d_M` 为**优化所得的数值**（非证明）✓
- ⚠️ **未读** Montgomery 原文证明（本地无 Ten Lectures；`E4-ENGINE-1` 已记录此事实）⟹ 本档**不比较证明技术**，只比较常数 ✓
- **未用** RH；**未改**他档 ✓
- **纪律**：先查后判 ✓、**先跑后写** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 20:2x）`[纪律]`

```
技术词 缩放约化    命中文件数=0 ::  ⟹ 本档新增
技术词 单位模子集   命中文件数=0 ::  ⟹ 本档新增
技术词 阻尼损失项   命中文件数=0 ::  ⟹ 本档新增
```

---

## §8 ⭐ 第二条引理：近单位模区间（本档第二击）

$$	extbf{引理 2}：	ext{设}\ |z_j|\in[1-\delta,\,1]\ orall j\ 	ext{（近单位模）}，	ext{且}\ M\le5\ 	ext{（单模常数}\ c=	frac12	ext{）}✓$$
$$\qquad 	ext{则}\quad \max_{1\le k\le5M}\Re\sum_j z_j^k\ \ge\ 	frac12-Mig[1-(1-\delta)^{5M}ig]✓✓$$
$$	extbf{证明（五行）}：	ext{令}\ z_j'=z_j/|z_j|（	ext{单位模}），r_j=|z_j|\in[1-\delta,1]✓$$
$$\qquad 	ext{(i)}\ 	ext{单模结果}（M\le5）：\exists k\le5M，\Re\sum_j (z_j')^k\ \ge\ 	frac12✓$$
$$\qquad 	ext{(ii)}\ 	ext{记}\ P:=\sum_{\Re (z_j')^k\ge0}\Re (z_j')^k\ge0，\ N_-:=\sum_{\Re (z_j')^k<0}\Re (z_j')^k\le0 \Longrightarrow P+N_-\ge	frac12✓$$
$$\qquad 	ext{(iii)}\ 	ext{阻尼效应}：	ext{正项被压}\ (r^k P\ge(1-\delta)^kP)；	extbf{负项被抬}（r_j^k x\ge x\ 	ext{当}\ x\le0，	ext{因}\ 0\le r_j^k\le1	ext{）}✓✓$$
$$\qquad 	ext{(iv)}\ \Longrightarrow \Re\sum_j z_j^k\ \ge\ (1-\delta)^kP+N_-=(P+N_-)+Pig[(1-\delta)^k-1ig]\ \ge\ 	frac12-Pig[1-(1-\delta)^kig]✓$$
$$\qquad 	ext{(v)}\ 	ext{用}\ 0\le P\le M\ 	ext{与}\ k\le5M：\ \ge\ 	frac12-Mig[1-(1-\delta)^{5M}ig]\qquad\square✓✓$$

$$	extbf{与}\ 	frac1{20}\ 	ext{对比（条件}\ M[1-(1-\delta)^{5M}]\le0.45）：$$
$$egin{array}{c|r|r}
M & \delta\ 	ext{上限} & 	ext{说明}\\hline
1 & pprox10.5\% & 	ext{较宽}✓\
2 & pprox2.2\% & \
5 & pprox0.37\% & 	ext{很窄}✗\
\end{array}✓$$
$$\Longrightarrow 	ext{两引理}\ 	extbf{互补覆盖两端}：	ext{重阻尼（引理 1，}ho\ 	ext{小或}\ M\ 	ext{大）／近单位（引理 2，}\delta\ 	ext{小）}✓$$
$$\qquad 	extbf{中间区（}hopprox0.75	ext{–}0.95\ 	ext{且}\ M\ 	ext{小）仍空}✗\ —— 	ext{恰是数值最坏区（}d_Mpprox0.36	ext{–}0.40	ext{）}✓✓$$

## §9 本档的直接结论

$$	extbf{①}\ 	ext{两条引理均为}	extbf{严格新结果}（	ext{四行／五行证明；只依赖我方已证的}\ M\le5\ 	ext{单模常数}）✓✓$$
$$	extbf{②}\ 	ext{它们共同给出}	extbf{阻尼情形的两段区间改进}（	ext{均严格优于 Montgomery 的}\ 	frac1{20}	ext{）}✓✓$$
$$	extbf{③}\ 	extbf{但中间区未覆盖}✗\ —— 	ext{下一步攻击点已明确：}ho\in[0.7,0.95]\ 	ext{且}\ M\ 	ext{小}✓$$
$$\qquad 	ext{该区需要}	extbf{联合对齐} 	ext{型论证（与}\ 	ext{OP-3}\ 	ext{同源）}⟹ 	ext{已知难点，但至少}\ 	extbf{攻击面已缩小到具体参数区}✓✓$$
