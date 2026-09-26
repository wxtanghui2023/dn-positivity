已查地图：已跑 scripts/prework_map_check.sh failure set W(x) holes minimality hypergraph ⟹ 执行自 PROOF-AUDIT-2026-09-26 档；本档为**失败集框架 ＋ 一条我方公式的否证 ＋ 修正恒等式**（唐先生 2026-09-26 14:42 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = private-point 失败集（W(x)、holes(S)）的全球结构框架、我方公式的否证、修正恒等式
D1: 1（新增：**失败集框架** ✓；**我方对公式被否** ✗；**修正恒等式 Σ_{pairs}|holes|=(M−1)N₁+N₂** ✓✓）

# FAILSET-2026-09-26

## §1 失败集框架（唐先生 #1/#3 的形式化 ✓）

```
$$\textbf{覆盖者集}: W(x):=\{c\in C:\ x\in B_1(c)\}\ ✓,\quad |W(x)|=b(x)\ ✓$$
$$\textbf{失败集}: \mathrm{holes}(S):=\{x:\ \varnothing\ne W(x)\subseteq S\}\ (S\subseteq C)\ ✓\ ——\ \text{删掉 }S\ \text{后失去覆盖的点}\ ✓$$
$$\textbf{minimality 的精确形式}: \boxed{\forall c\in C:\ \mathrm{holes}(\{c\})\ne\varnothing}\ \iff\ \forall c\ \exists x:\ W(x)=\{c\}\ (\text{私有点})\ ✓✓$$
$$\textbf{完整失败数据} = \text{精确覆盖者集的 census}: \quad \mathrm{holes}(S)=\sum_{\varnothing\ne T\subseteq S}\#\{x:\ W(x)=T\}\ ✓\ (\text{容斥}\ ✓)$$
$$\Longrightarrow\ \text{"minimality 超图"} = \text{多重族 }\{W(x)\}_{x\in\mathbb{F}_2^n}\ ✓\ \text{—— 这就是唐先生要的\textbf{全球对象}}\ ✓\ (\text{非局部量}\ ✓)$$
$$

## §2 ⛔ 我方公式被否（诚实记录 ✓）

```
$$\textbf{我原提}: |\mathrm{holes}(\{c,c'\})|=p(c)+p(c')+2\cdot[d(c,c')\le2]\ ✗$$
$$\textbf{数值}: (5,7):\ \textbf{72 处违反}\ ✗;\quad (9,64):\ \textbf{96 处违反}\ ✗;\quad \text{总数 }28224\ne\text{预测 }28416\ ✗$$
$$\textbf{根因（我方定位 ✓）}: d(c,c')\le2\ \text{时 }|B_1(c)\cap B_1(c')|=2\ ✓\ (\text{真}\ ✓),\ \text{但这 2 点\textbf{可能还被其它码字覆盖}}\ ✗\ \Longrightarrow\ \text{它们不一定属于 }W(x)=\{c,c'\}\ ✗✓$$
$$

## §3 ✅ 修正后的恒等式（干净 ✓✓）

```
$$\textbf{定义}: e(c,c'):=\#\{x:\ W(x)=\{c,c'\}\}\ \in\{0,1,2\}\ ✓\ (\text{由 }|B_1\cap B_1|\le2\ ✓)$$
$$\textbf{对公式（定义性 ✓）}: \mathrm{holes}(\{c,c'\})=p(c)+p(c')+e(c,c')\ ✓✓$$
$$\textbf{求和恒等式（新增 ✓）}: \sum_{\{c,c'\}}e(c,c')=N_2\ ✓\ (\text{每个 }|W(x)|=2\ \text{的点恰属一对}\ ✓)$$
$$\Longrightarrow\ \boxed{\sum_{\{c,c'\}}|\mathrm{holes}(\{c,c'\})|=(M-1)N_1+N_2}\ ✓✓$$
$$\textbf{数值验证（全过 ✓✓）}: (4,4):\ 3\cdot12+4=40=\text{实测 }40\ ✓;\quad (5,7):\ 6\cdot24+6=150=\text{实测 }150\ ✓;\quad (9,64):\ 63\cdot448+0=28224=\text{实测 }28224\ ✓✓$$
$$\qquad \text{且 }\sum_{\{c,c'\}}e(c,c')=N_2\ \text{全过}\ ✓✓\ (\text{逐样本验}: 4=4\ ✓,\ 6=6\ ✓,\ 0=0\ ✓)$$
$$\qquad \text{样本量}: (4,4)\ 15/15\ ✓;\quad (5,7)\ 15/15\ ✓$$
$$\textbf{附带}: e(c,c')>0\ \Longrightarrow\ d(c,c')\le2\ ✓\ (\text{独占对只出现在近对}\ ✓)$$
$$

## §4 由框架直接得到的三条干净事实（新增 ✓）

```
$$\textbf{F1}: \text{私有点集 }\{x:\ W(x)=\{c\}\}\ \text{对不同的 }c\ \textbf{两两不交}\ ✓\ \Longrightarrow\ \text{它们把 }N_1\ \text{个点\textbf{分割}成 }M\ \text{个非空块}\ ✓$$
$$\qquad\Longrightarrow\ N_1=\sum_cp(c)\ \ge M\ ✓;\quad \boxed{N_1=M\iff p(c)=1\ \forall c}\ ✓✓$$
$$\textbf{F2}: N_1=2^n-Q\ \Longrightarrow\ \boxed{Q=2^n-\sum_cp(c)}\ ✓\ (\text{总重复覆盖数 = 空间大小 − 私有总数}\ ✓)$$
$$\textbf{F3}: \text{minimality}\ \iff\ \text{族 }\{W(x)\}\ \text{包含全部 }M\ \text{个单点集}\ ✓\ \Longrightarrow\ \text{族的大小 }2^n\ge\text{不同 }W\ \text{数}\ge M\ ✓\ (\text{弱}\ ✗)$$
```

## §5 下一刀（唐先生三入口 ✓，用修正框架重述）

```
$$\text{入口 1（删除/私有点关联）}: \text{研究 }c\mapsto\mathrm{holes}(\{c\})\ \text{在 }\{c\}\ \text{上的\textbf{全局交叉}};\ \text{已知 }p(c)\ge1\ ✓;\ \text{问: minimality 是否给 }p(c)\ \text{的全局约束？}\ ⚠️$$
$$\text{入口 2（pair/triple 交点代数）}: \sum_x\binom{b(x)}2=E+Q_2\ \text{（已锁 ✓）};\ \text{新增候选}: \sum_x\binom{b(x)}3=\#\{\text{共点三元组}\}\ ✓\ (\text{三重交} \le1\ ✓)$$
$$\text{入口 3（minimality 超图）}: \text{把 }\{W(x)\}\ \text{当 set system 研究（本档 §1/§4 已给出第一层结构 ✓）}\ ✓✓$$
$$

## §6 状态（不改停机哲学 ✓，但**问题保持 OPEN** ✓）

```
$$\textbf{问题}: G\ (\text{minimality}+n\ \text{奇}+E>0\Rightarrow Q_2\ \text{钉住})\ —— \boxed{\textbf{KEEP OPEN}}\ ✓$$
$$\textbf{路线}: \text{局部弧全灭（ZB-1..7）}\ ✗;\ \textbf{新路线启动}: \text{失败集／覆盖者超图}\ ✓\ (\text{本档为第一次落地}\ ✓)$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓\ (\text{含义 = 当前 formulation 无 certificate}\ ✓,\ \textbf{非}问题死亡\ ✓)$$
$$

## §7 边界（诚实标注）

- §2 是**我方公式的否证**记录 ✓（未掩盖 ✓）；§3 的修正恒等式为**新增并数值验证** ✓
- §1/§4 为**框架与短推导** ✓（F1/F2 为既有事实的框架化重述 ✓，F3 为弱命题 ✗）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：失败集框架、覆盖者超图、独占对计数、私有分割
- **档案已有（引用，不列为提出）**：私有点、minimality、excess
