已查地图：已跑 scripts/prework_map_check.sh 二阶传播 119 excess E=285 ⟹ 命中 `PROPAGATION-2026-09-26-verified-lemma-and-refuted-ladder.md`（**直击** ✓）、`K101-119-ARCHIVE-2026-09-26.md`、`FAILSET-2026-09-26-...`、`SUM-P1P4-2026-09-26-...`、`GAPTHEOREM-2026-09-26-...`；本档 = **119 重启评估（未开新案 ✓）**。
D0: 本档对象 = 119 的"二阶传播 ⟹ E≥286"路线之可容许性评估
D1: 3（**E = 285 为强制恒等式 ✓**；**该路线已走过：引理成立 ✓ 但 ladder 被证伪 ✗ ＋ 不聚合 ✗**；**可容许性判据：必须支撑敏感（跨中心）✓**）

# 119 重启评估（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(EA-1 ⭐强制恒等式（先钉死 ✓）)}\ \text{对任何 }|C|=119\ \wedge\ B_1(C)=\mathbb F_2^{10}\ \text{的覆盖码}:\ \sum_x b(x)=119\cdot11=1309,\ \sum_x 1=1024 \Longrightarrow\ \boxed{E:=\sum_x\delta(x)=\sum_x(b(x)-1)=\mathbf{285}}\ \textbf{（无条件强制 ✓）}}$$
$$\qquad\Longrightarrow\ \boxed{\text{目标 "}E\ge286\text{"}\ \textbf{等价于}"119\text{-码不存在"}\ ——\ \text{即 }P1\ \text{本身} ✓}\ \text{（不是新的弱化目标 ✓）};\ \text{故任何此类论证 = 直接证 }K(10,1)\ge120\ ✓$$
$$\boxed{\textbf{(EB-1 🔴该路线已在档、且被证伪过一半 ✓（必须先摆出 ✓）)}\ \texttt{PROPAGATION-2026-09-26}:}$$
$$\qquad\textbf{① 传播引理（已证 ＋ 数值验证 ✓）}:\ Q{=}0\ \text{时对距离-2 对之中点 }m:\ \boxed{|C\cap S_2(m)|\ \ge\ \lceil (n-2)/2\rceil}\ ✓\ (n{=}4{:}40/40\ ✓;\ n{=}5{:}28/28\ ✓)$$
$$\qquad\textbf{② ladder 论断：数值证伪 ✗}:\ \text{两条迭代断言（共享壳下界 }|C\cap S_2(m)\cap S_2(m')|\ge n{-}2\ ✗\ \text{与 }u_l/v_l\ \text{占位 ✗）\textbf{均有反例} ✓}$$
$$\qquad\textbf{③ 关键限制（本档最重要 ✓）}:\ \text{该引理\textbf{不给奇偶障碍}、且\textbf{不聚合} ✗ —— 因不同中点可\textbf{共享同一个 }z\ ✓ \Longrightarrow \text{全局计数不受理 ✗}}$$
$$\qquad\Longrightarrow\ \boxed{\text{"二阶传播 ⟹ }E\ge286\text{" 这一形状\textbf{不能}由传播引理承担 ✗（局部容量下界 ≠ 全局 excess 下界 ✓）}}$$
$$\boxed{\textbf{(EC-1 ⭐可容许性判据（本档核心 ✓）)}\ \text{因 }E=\sum_x(b(x)-1)\ \text{是 }\delta\text{-型泛函};\ \text{而档案已建立：}\delta\text{-型泛函被 profile 恒等式\textbf{钉死}}（`SUM-P1P4`：线性局部泛函与码无关；`AMEND-30` LOCAL-AVG-GATE；`GAPTHEOREM`：十类 }\sum_xf(\delta(x))\ \text{全被 }Q{=}1\ \text{指纹钉住 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{任何只用 }b(x)\ \text{统计的论证\textbf{不可能}给出 }E\ge286\ ✗;\ \text{唯一可容许者 = \textbf{支撑敏感（跨中心）}不等式 ✓（STOP 清单唯一放行类 ✓）}}$$
$$
$$
```

---

## §1 可容许的两件既有工具（**✓ 支撑敏感**）

```
$$\text{(i) }\textbf{失败集／覆盖者超图}（`FAILSET-2026-09-26` ✓）:\ W(x)=\{c:x\in B_1(c)\},\ \mathrm{holes}(S)=\{x:\varnothing\ne W(x)\subseteq S\}\ ✓;\ \text{内含修正恒等式（}\sum_{\rm pairs}|\mathrm{holes}|\ \text{型 ✓）}$$
$$\qquad\textbf{其为支撑敏感 ✓（依赖"哪些码字"而非仅计数 ✓）} \Longrightarrow \text{合于判据 ✓};\ \text{但档案已注明其原公式被否 ✗、修正恒等式成立 ✓}$$
$$\text{(ii) }\textbf{行闭包／支撑碰撞}（`SCOL-2026-09-26` ✓）:\ n_l\le2,\ n_l{=}2\Rightarrow\text{行闭 ✓};\ \text{Type II }+7\ \text{forced};\ A_2(z)+3A_3(z)\ge24;\ |C\cap L_3|\le80\ ✓\ \text{—— 亦支撑敏感 ✓}$$
$$\boxed{\text{结论 ✓}:\ \text{下一步只能用 (i)/(ii) 这类对象，形如："若 }x_0\ \text{由\textbf{特定三个码字}覆盖，则\textbf{某个跨中心计数} $\ge\Theta$" ✓}$$
$$
$$
```

---

## §2 诚实风险标注（**⚠️ 唐先生纪律 ✓**）

```
$$\textbf{风险 ✓}:\ \text{档案记录显示该方向已有 }\ge12\ \text{次"同向收敛"（新论证最后都落回已知恒等式 ✓）};\ \text{故本档\textbf{不}宣称找到了新障碍 ✗}$$
$$\textbf{禁止表述（档案明文 ✓）}:\ \text{不写"119 被排除／该方向已死／证明不可能" ✗};\ \text{只写"该路线\textbf{未闭合}" ✓}$$
$$\textbf{状态 ✓}:\ \boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{结构路线未闭合};\ \text{八类机制不足以产生独立缺口}}\ ✓\ \text{（与 `K101-119-ARCHIVE` 一致 ✓）}$$
$$
$$
```

---

## §3 建议的下一步（**✓ 唯一符合判据的形状**）

```
$$\text{(119-甲) }\textbf{支撑敏感传播}:\ \text{取 }M{=}K\ \text{给出的 }x_0\ (b(x_0)\ge3\ ✓),\ \text{记其覆盖者集 }W(x_0)=\{c_1,c_2,c_3,\dots\}\ ✓\ \text{（\textbf{具体哪几个} ✓）};\ \text{问}:\ \text{可否由 }\{c_i\}\ \text{的几何（中点在 }B_2\ \text{中的分布 ＋ 行闭包）推出\textbf{一个跨中心计数}超过 profile 允许值 ✓}$$
$$\text{(119-乙) 若 (甲) 只得到 }\delta\text{-型推论 ⟹ 立即停 ✗（按判别式 ✓），}\ \text{并记为"同向收敛"（档案纪律 ✓）}$$
$$\text{(丙) 119 保持不跑 solver ✓（此前 CP-SAT 3600s UNKNOWN、0 incumbent 已记录 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$E=285$ 强制恒等式与"$E\ge286\iff$ 不存在"之等价、传播引理不聚合之限制、可容许性判据（支撑敏感类）
- **档案已有（引用，不列为提出）**：PROPAGATION-2026-09-26、FAILSET-2026-09-26、SCOL-2026-09-26、SUM-P1P4-2026-09-26、AMEND-30、GAPTHEOREM-2026-09-26、K101-119-ARCHIVE-2026-09-26


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 可容许性判据 命中文件数=1    :: ./RESTART-119-2026-09-27-assessment-of-the-second-order-route.md 
技术词 支撑敏感     命中文件数=1    :: ./RESTART-119-2026-09-27-assessment-of-the-second-order-route.md
```
- **本档新增**：$E=285$ 强制恒等式与「$E\ge286\iff$ 不存在」之等价、传播引理不聚合之限制、可容许性判据（支撑敏感类）（见上方命中数；0 命中者为自造语／内部标签 ✓）
