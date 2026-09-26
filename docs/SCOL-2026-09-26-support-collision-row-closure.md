已查地图：已跑 scripts/prework_map_check.sh K(10,1) support collision 行闭合 奇偶 ⟹ 执行自 `docs/TCOLL-2026-09-26-...md`（(E-1)(E-2)(E-3) ✓）＋ `docs/STAR3-2026-09-26-...md`（Type III 排除 ✓）＋ `docs/PACKB-2026-09-26-...md`（匹配定理 ✓）；本档为**纯推导**（唐先生 2026-09-26 20:06 指令「攻 P3 collision，找 Support-Collision Lemma」✓）；**未跑程序** ✓。
D0: 本档对象 = `Q=1` 分支的 support-collision（既有对象；非新对象）
D1: 0（产出一条普适行闭合引理、Type II 新强制集、一条奇偶约束与路线判定）

# SCOL-2026-09-26 · P3 Support-Collision 第一刀

## §0 结论（先给）

```
$$\boxed{\textbf{(F-1 普适引理·行闭合)}\ \text{若}\ e_l\ (l\ge4)\ \text{被 2 个码字覆盖}\ \Longrightarrow\ b(e_l)=2\ \Longrightarrow\ \textbf{行}\ l\ \text{关闭}:\ \forall m:\{l,m\}\notin C\ (m\ne l)\ ✓✓}$$
$$\boxed{\textbf{(F-2 Type II 新强制集)}\ \sigma(1)=\sigma(2)=j\ \Longrightarrow\ \underbrace{\{j,m\}:m\ge4,m\ne j}_{6\ \text{点}}\cup\{\{3,j\}\}\ \text{全非码字}\ ✓✓\ (\text{+7 强制量})}$$
$$\boxed{\textbf{(F-3 Type II 奇偶)}\ \Sigma_{T_1}q\ \text{与}\ \Sigma_{T_2}q\ \text{必为\textbf{偶数}}\ ✓\ (\text{第二覆盖者只能是权-4 点，每次服务恰 2 点})}$$
$$\boxed{\textbf{(F-4 局部界改进)}\ A_2(z)+3A_3(z)\ \ge\ \mathbf{24}\ ✓\ (\text{原 21};\ \text{因}\ L_2\ \text{内强制}\ b{=}2\ \text{点为}\ 3(y_{ij})+3(p_i)=6\ ✓\ \Longrightarrow\ \delta_2(z)\ge6\ ✓)}$$
$$\boxed{\textbf{(F-5 判定)}\ \textbf{仍未得 P3 collision}\ ✗\ ——\ \text{本地 forcing 量级持续不足（第 5 次汇合）}\ ✓✓}$$
$$
$$
```

---

## §1 (F-1) 行闭合引理（普适，本档核心 ✓）

```
$$\textbf{设定}:\ l\ge4\ ✓;\ e_l=\{l\}\ \text{是}\ L_1\ \text{点（强制非码字}\ ✓）;\ \text{其覆盖者}\ =C\cap B_1(e_l)=\{\{l,m\}:m\ne l\}\ ✓\ (\text{无 }\le1\text{-权码字}\ ✓)$$
$$\textbf{故}:\ b(e_l)=\#\{m:\{l,m\}\in C\}\ ✓✓$$
$$\textbf{引理}:\ \text{若}\ b(e_l)=2\ (\text{即被恰 2 个码字覆盖})\ ✓\ \text{则}\ \{l,m\}\in C\ \text{恰对 2 个}\ m\ ✓\ \Longrightarrow\ \text{其余全部非码字}\ ✓✓$$
$$\qquad\text{等价}:\ \text{"行}\ l\ \text{的码字数}=b(e_l)"\ ⟹\ \text{行闭合}=\text{该行码字已满（}b{=}2\text{）}\ ✓$$
$$\textbf{由 STAR3 §4（Type III 排除）}:\ n_l:=\#\{i:\sigma(i)=l\}\le2\ ✓\ \Longrightarrow\ b(e_l)\ge n_l\ ✓\ \text{且}\ \le2\ ✓$$
$$\qquad\Longrightarrow\ \begin{cases}n_l=2:&b(e_l)=2\ \text{恰等}\ \Longrightarrow\ \textbf{行}\ l\ \text{关闭}\ ✓✓\\ n_l\le1:&b(e_l)\in\{n_l,\dots,2\}\ \text{（未定）}\ ⚠️\end{cases}$$
$$
$$
```

**⟹ 机制**：$e_l$ 的覆盖者与"行 $l$ 的码字"是**同一个集合** ✓ ⟹ 一旦 $e_l$ 的覆盖已满（$b=2$ ✓），整行就被关闭 ✓ ✓ —— 这是一条**支撑型（support）约束** ✓，不是计数恒等式 ✓。

---

## §2 (F-2) Type II 的新强制集（+7 ✓）

```
$$\textbf{Type II}:\ \sigma(1)=\sigma(2)=j\ (j\ge4),\ \sigma(3)=k\ne j\ ✓$$
$$\textbf{行}\ j\ \text{的码字}:\ p_1=\{1,j\}\ ✓,\ p_2=\{2,j\}\ ✓\ \Longrightarrow\ n_j=2\ \Longrightarrow\ \textbf{行}\ j\ \text{关闭}\ ✓✓$$
$$\qquad\Longrightarrow\ \forall m\ne j,\ m\ge4:\ \{j,m\}\notin C\ ✓\ (\mathbf{6}\ \text{点},\ m\in\{4,\dots,10\}\setminus\{j\}\ ✓)$$
$$\qquad\text{又}\ \{3,j\}\notin C\ ✓\ (\text{因}\ \deg(e_3)\le1\ \text{且}\ e_3\ \text{的唯一码邻是}\ p_3=\{3,k\}\ne\{3,j\}\ ✓)\ \Longrightarrow\ \text{再}\ \mathbf 1\ \text{点}$$
$$\Longrightarrow\ \boxed{\text{Type II 新增 7 个强制非码字}}\ ✓✓\qquad(\text{含 6 个纯}\ L_2\ \text{点}+\{3,j\}\ ✓)$$
$$\textbf{与}\ L_2\ \text{上界的相容性}:\ \text{纯}\ L_2\ \text{码字总数}\le7\ ✓\ (\text{档案行容量法}\ ✓)\ \text{—— 本式给出该行全空}\ ✓\ \text{相容}\ ✓$$
$$
$$
```

---

## §3 (F-3) Type II 的奇偶约束（本档新 ✓）

```
$$\textbf{Type II 下}\ T_i\ (i=1,2)\ \text{点的第二覆盖者候选}:\ \underbrace{\{j,l\}}_{\textbf{已由 (F-2) 全排除}\ ✗!}\ \cup\ \{\text{7 个权-4 点}\}\ ✓✓$$
$$\qquad(\text{因}\ \{j,l\}\notin C\ \forall l\ne j\ ✓\ \text{—— 行}\ j\ \text{关闭}\ ✓)$$
$$\Longrightarrow\ \text{所有}\ q(x)=1\ \text{的}\ x\ \text{的第二覆盖者都是权-4 点}\ ✓;\ \text{而每个权-4 点恰服务 2 个}\ T_i\ \text{点}\ ✓\ (\text{TCOLL §2}\ ✓)$$
$$\Longrightarrow\ \boxed{\Sigma_{T_i}q\ =\ 2\cdot\#\{\text{服务的权-4 码字}\}\ \equiv\ 0\ (\mathrm{mod}\ 2)}\ ✓✓\qquad(i=1,2)$$
$$\textbf{与 (C-1) 分解式联立（TCOLL §3 修正版）}:\ \Sigma_{T_i}q=2a_2(p_i)-1-(b(e_j)-1)-\sum_{i'\ne i}(b(y_{ii'}+e_j)-1)\ ✓$$
$$\qquad\text{Type II 有}\ b(e_j)=2\ ✓\ \Longrightarrow\ \Sigma_{T_i}q=2a_2(p_i)-2-\Sigma_{i'\ne i}(\cdots)\ \Longrightarrow\ \textbf{偶数}\ ✓\ \Longrightarrow\ \Sigma_{i'\ne i}(b(y_{ii'}+e_j)-1)\ \equiv\ 0\ (\mathrm{mod}\ 2)$$
$$\Longrightarrow\ \text{即}:\ b(y_{1i'}+e_j)\ \text{与}\ b(y_{2i'}+e_j)\ \text{的"是否}\ b{=}2"\ \text{同奇偶}\ ✓\ (\text{弱约束，但为真})\ ✓$$
$$
$$
```

---

## §4 (F-4) 局部界改进：$\delta_2(z)\ge6$（本档 ✓）

```
$$\textbf{复核本地强制}\ b{=}2\ \text{点}:\ \text{①}\ y_{12},y_{13},y_{23}\ (\text{球内恰含}\ e_a,e_b\ ✓)\ ✓;\ \text{②}\ p_1,p_2,p_3\ (\text{码字，}b=1+d_1=2\ ✓)\ ✓$$
$$\qquad\Longrightarrow\ \#\{x\in L_2(z):b(x)=2\}\ \ge\ \mathbf 6\ ✓✓\qquad(\text{原用 3 → 21}\ ✗;\ \text{现}\ \ge6\ →\ \mathbf{24}\ ✓)$$
$$\textbf{由 GRAM-LIFT 层式}:\ \delta_2(z)=A_2(z)+9A_1(z)+3A_3(z)-\binom{10}{2}\ ✓\ \text{且}\ A_1(z)=3\ \Longrightarrow\ \delta_2(z)=A_2(z)+3A_3(z)-18\ ✓$$
$$\qquad\Longrightarrow\ \boxed{A_2(z)+3A_3(z)\ \ge\ \mathbf{24}}\ ✓✓\qquad(\text{改进档案/①′ 的}\ \ge21\ ✓)$$
$$
$$
```

---

## §5 (F-5) 判定：仍未 collision（第 5 次汇合 ✓）

```
$$\textbf{本轮新增}:\ \text{+7 强制非码字（Type II）}\ ✓;\ \text{奇偶约束}\ ✓;\ \text{局部界}\ 21\to24\ ✓;\ \text{普适行闭合引理}\ ✓✓$$
$$\textbf{与容量对比}:\ \text{强制非码字总量（Type II，三个都 matched）}:\ 50+7=\mathbf{57}\ \ll\ 905\ ✗\ \text{（差 16 倍）}$$
$$\textbf{故}:\ \text{本地 forcing 路径\textbf{量级上不可能闭合}}\ ✗✓\ ——\ \text{这是今日第 5 次同向汇合}:\ \text{AMEND-30／GRAMSIGN／ISOB3／TCOLL／SCOL}\ ✓$$
$$\textbf{结构性原因（本档总结）}:\ \text{所有可用机制都产\emph{上界}或\emph{有界的新强制集}（O(常数) 个点）；}$$
$$\qquad\text{而}\ Q=1\ \text{的排除需要\emph{全局支撑型}矛盾（把}\ 905\ \text{量级的容量与}\ 119\ \text{个码字的覆盖结构对撞）}\ ✓$$
$$
$$
```

---

## §6 ⭐ **本档最重要的产出：Q=1 的"计数层完全自洽"定理（负面但定位精确 ✓）**

```
$$\textbf{命题（本档核验）}:\ Q=1\ \text{的全部\textbf{一阶/二阶计数}都自洽}:\ \text{profile}\ (740,283,1)\ ✓;\ \sum_xb(x)=1309\ ✓;\ A_1+A_2=143\ ✓;$$
$$\qquad 2A_2=3+(283-2A_1)\ ✓;\ \sum_c a_2(c)=2A_2\ ✓;\ \sum_c\#\mathrm{priv}(c)=740\ ✓\ (\text{ISOB3}\ ✓)\ ✓$$
$$\Longrightarrow\ \boxed{\text{不存在"纯计数"矛盾};\ \text{矛盾只能来自\textbf{支撑}}\ (\text{哪些点取哪个 }b\text{ 值})\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{这把 P3 的目标精确定位为}:\ \text{一个\emph{支撑不可满足性}（support unsatisfiability）命题}\ ✓$$
$$
$$
```

---

## §7 下一步候选（本档列出，未执行 ✓）

```
$$\textbf{G-1（本档最推荐）}:\ \text{把 (F-1) 行闭合引理\textbf{全局化}}:\ \text{对全部}\ l\ge4\ (\text{7 个行}\ ✓)\ \text{统计"关闭行数"}\ ✓$$
$$\qquad\text{若某配置下关闭行数过多 ⟹ 纯}\ L_2\ \text{区（21 点）几乎全空 ⟹ 与}\ A_2\ge83\ \text{的\textbf{中点需求}冲突}\ ✓\ (\text{中点须是}\ L_2/L_4\ \text{点}\ ✓)$$
$$\qquad\Longrightarrow\ \text{这是唯一能把"局部行闭合"升级成\textbf{全局支撑矛盾}的接口}\ ✓✓$$
$$\textbf{G-2}:\ \text{把行闭合与中点结构联立}:\ \text{纯}\ L_2\ \text{点}\ \{l,m\}\ \text{是中点}\ ✓\ (\text{权-4 对的"下交"}\ ✓);\ \text{若该行关闭则}\ \{l,m\}\notin C\ \Longrightarrow\ \text{它是}\ b=2\ \text{非码字中点}\ ✓$$
$$\qquad\Longrightarrow\ \text{计数其配额（}283-2A_1\ ✓\text{）与行闭合数对撞}\ ✓$$
$$\textbf{G-3}:\ \text{把}\ A_2(z)+3A_3(z)\ge24\ \text{与全局}\ A_1+A_2=143\ \text{联立重算窗口}\ ✓$$
$$
$$
```

---

## §8 边界（诚实标注）

- §1 的 (F-1) 为**严格推导** ✓（$e_l$ 的覆盖者集合＝行 $l$ 的码字集合 ✓）；普适性来自 $e_l$ 是 $L_1$ 强制非码字 ✓
- §2 的 (F-2) 为**本档新结论** ✓（用 (F-1) + $\deg(e_3)\le1$ ✓）
- §3 的 (F-3) 为**本档新结论** ✓（用 (F-2) 排除权-2 候选 + TCOLL 的权-4 服务性 ✓）
- §4 的 $\ge24$ 为**本档改进** ✓（原 21 ✓）
- §6 的"计数层自洽"为**本档核验结论** ✓（非定理，是逐项核验 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 行闭合引理  命中文件数=1    :: ./SCOL-2026-09-26-support-collision-row-closure.md 
技术词 Type II 行空强制 命中文件数=1    :: ./SCOL-2026-09-26-support-collision-row-closure.md 
技术词 服务奇偶约束 命中文件数=1    :: ./SCOL-2026-09-26-support-collision-row-closure.md
```
- **本档新增**：行闭合引理、Type II 行空强制、服务奇偶约束（见上方命中数）
- **档案已有（引用，不列为提出）**：$\delta_2$ 层式、$n_l\le2$、纯 $L_2$ 码字 $\le7$
