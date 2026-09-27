# P1-TETRA-2026-09-27 — **$N_{\rm tetra}>0$ 攻坚**：几何刻画 ＋ 反证约束 ＋ 上界（**未成，诚实落判**）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:44 令 ✓）**：按 P1→P2→P3 顺序；本轮只做 $(P1)$：$N_{\rm tetra}>0$ 是否可证；**不碰 $T_4$／$n_j$／profile 极值** ✗；零程序计算 ✓。

**已查地图：命中（接续 R7-LOCK 与 R6／R7，非新案 ✓）**
所查：`docs/R7-LOCK-2026-09-27-status-lock-and-the-K4-deficit-interface-identity.md`（**接口 $\Delta_4=N_{\rm sq}+N_{\rm tet}$** ✓✓）｜`docs/R7-2026-09-27-…`｜`docs/R6-2026-09-27-…`｜`docs/C3-119-2026-09-27-…`（IA-1 交叉引用 ✓）｜`docs/R4-P1-2026-09-27-…`（$S(c)\cup V(H_c)$／451 ✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有** $K_4$ 亏空对象的 **P1 攻坚**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 tetra 的几何刻画（中点集 ＝ 3-coset 奇部）＋ $\Delta_4=0$ 可达反证 ＋ $N_{\rm tetra}\le T_3/4$ 上界** ✓）
**[RESEARCH]**

---

## §0 结论（**P1 未成 ✗；但得 3 条结构结果 ＋ 1 条反证约束 ＋ 1 条上界 ✓**）

$$\boxed{\textbf{(P1) 未证成 ✗}:\ N_{\rm tetra}>0\ \text{未能证明};\ \text{亦未找到矛盾};\ \text{本档\textbf{不}声称它成立}✗✓\ (\text{诚实落判 ✓})}$$
$$\boxed{\textbf{结果 1（几何刻画 ✓✓）}:\ \textbf{square}＝完整 2-维 coset\ \{v,v{+}e_i,v{+}e_j,v{+}e_i{+}e_j\};\quad \textbf{tetra}＝3\text{-维 coset 的\textbf{偶部}}✓✓}$$
$$\boxed{\textbf{结果 2（★中点定理 ✓✓）}:\ \text{tetra 的六对中点（12 个带重数实例）\textbf{集合}恰为该 3-coset 的\textbf{奇部}（4 点）；且每个奇点恰是 3 对的共同中点}✓✓}$$
$$\boxed{\textbf{结果 3（反证约束 ✓✓）}:\ \Delta_4=0\ \textbf{可达}:\ \text{球型码 }C=B_1(x)\ \text{有 }G_2=K_{11},\ T_4=\binom{11}4=330=\#K_4\Longrightarrow\Delta_4=0✓\ \Longrightarrow\ \textbf{无普适逼迫}✗✓}$$
$$\boxed{\textbf{结果 4（上界 ✓）}:\ 4N_{\rm tetra}\le\sum_x\binom{b(x)}3=T_3\Longrightarrow N_{\rm tetra}\le T_3/4\le\mathbf{842}✓\ (\text{\textbf{上界}，非所求下界 ✗})}$$

---

## §1 几何刻画（**结果 1／2 ✓✓**）

$$\textbf{square ✓}:\ \{v,\ v{+}e_i,\ v{+}e_j,\ v{+}e_i{+}e_j\}=v+\mathbb F_2^{\{i,j\}}\ \text{—— \textbf{完整的 2 维仿射子空间}✓✓\ (\text{对角线的中点落在该 square 内 ✓})}$$
$$\textbf{tetra ✓}:\ \{v,\ v{+}e_i{+}e_j,\ v{+}e_i{+}e_k,\ v{+}e_j{+}e_k\}=v+\big(\text{span}(e_i,e_j,e_k)\big)_{\rm even}\ \text{—— \textbf{3 维 coset 的偶部}✓✓}$$
$$\textbf{（结果 2）中点定理 ✓✓}:\ \text{六对、每对 2 个中点（共 12 实例）逐对列出}:$$
$$\quad (v,\ v{+}e_i{\oplus}e_j)\to\{v{+}e_i,\ v{+}e_j\};\quad (v,\ v{+}e_i{\oplus}e_k)\to\{v{+}e_i,\ v{+}e_k\};\quad (v,\ v{+}e_j{\oplus}e_k)\to\{v{+}e_j,\ v{+}e_k\}$$
$$\quad (v{+}e_i{\oplus}e_j,\ v{+}e_i{\oplus}e_k)\to\{v{+}e_j,\ v{+}e_i{\oplus}e_j{\oplus}e_k\};\quad (v{+}e_i{\oplus}e_j,\ v{+}e_j{\oplus}e_k)\to\{v{+}e_i,\ v{+}e_i{\oplus}e_j{\oplus}e_k\}$$
$$\quad (v{+}e_i{\oplus}e_k,\ v{+}e_j{\oplus}e_k)\to\{v{+}e_k,\ v{+}e_i{\oplus}e_j{\oplus}e_k\}$$
$$\Longrightarrow\ \text{集合}:\ \big\{v{+}e_i,\ v{+}e_j,\ v{+}e_k,\ v{+}e_i{\oplus}e_j{\oplus}e_k\big\}=\textbf{奇部}✓✓\ (\text{三奇权 1 ＋ 一奇权 3},\ \text{每点 12/4}=\mathbf 3\ \text{对 ✓})$$
$$\textbf{对照 ✓}:\ \text{square 的两条对角线的中点是 }\{v{+}e_i,v{+}e_j\}\ \text{与}\ \{v,v{+}e_i{+}e_j\}\ \text{—— \textbf{落在 square 内部}✗（故 square 不产生新点 ✓）}$$

## §2 配对级分析（**亏空不可由配对数据决定 ✓**）

| 形状 | 六对的配对谱 | 满图计数 |
|---|---|---|
| claw | $3\times$ 距 1 ＋ $3\times$ 距 2 | 122880 |
| square | $4\times$ 距 1 ＋ $2\times$ 距 2 | 11520 |
| star | $6\times$ 距 2 | 215040 |
| tetrahedron | $6\times$ 距 2 | 30720 |
$$\textbf{✓ 星与四面体配对谱完全相同（六距全 2）} \Longrightarrow \text{配对数据\textbf{不能}区分二者}✓✓\ (\text{＝R7-LOCK §1 的留档事实 ✓})$$
$$\textbf{⚠️ 修正（本档自查 ✓）}:\ \text{claw}(3{+}3)\ \textbf{与}\ \text{square}(4{+}2)\ \text{配对谱\textbf{不同}}✗\ \text{—— 故"亏空整体配对不可见"一语\textbf{不成立}✗✓}$$
$$\qquad\text{但关键结论仍成立 ✓}:\ N_{\rm square},N_{\rm tetra}\ \text{是\textbf{团计数}，不由}(N_1,N_2)\ \text{或任何 profile 矩决定}✓\ (\text{团计数 }\ne\ \text{配对重数 ✓})$$

## §3 $\Delta_4=0$ **可达**（**结果 3；反证约束 ✓✓**）

$$\text{取 }C=B_1(x)\ (11\ \text{点},\ \text{非覆盖码 ✓}):\quad \text{任两点 }d\le2\Longrightarrow G_2(C)=K_{11}✓\ \Longrightarrow\ \#K_4=\binom{11}4=\mathbf{330}✓$$
$$b(x)=11\Longrightarrow\binom{11}4=330✓;\quad y=x{+}e_i:\ B_1(y)\cap C=\{x,\ x{+}e_i\}\Longrightarrow b(y)=2\Longrightarrow\binom24=0✓;\ \text{其余 }b\le1✓$$
$$\Longrightarrow\ T_4=330=\#K_4\Longrightarrow\boxed{\Delta_4=0}\ ✓✓$$
$$\Longrightarrow\ \textbf{结论 ✓✓}:\ \Delta_4=0\ \text{在几何上\textbf{可被实现}} \Longrightarrow \textbf{不存在"任何码都有 }\Delta_4>0\text{"的普适逼迫}✗✓$$
$$\qquad\Longrightarrow\ \textbf{P1 必须使用 }\textbf{covering／近最优性}\ \text{的特异信息（球型码不是覆盖码 ✓）}\ ✓$$

## §4 excess／三阶预算 ⟹ $N_{\rm tetra}$ **上界**（**结果 4 ✓**）

$$\text{tetra 的偶部四点中，恰 }\mathbf 3\ \text{点与给定奇点 }o\ \text{相距 1}\ (\text{其余第 4 点距离 3 ✓}) \Longrightarrow \text{该三者在 }S(o)\ \text{内}✓$$
$$\Longrightarrow\ \#\{\text{tetra}:\ o\in\ \text{其奇部}\}\le\binom{b(o)}3✓\ \Longrightarrow\ \text{两端计数}: \ \sum_o\binom{b(o)}3\ \ge\ \#\{(o,T):o\in{\rm odd}(T)\}=4N_{\rm tetra}✓$$
$$\Longrightarrow\ \boxed{N_{\rm tetra}\le\tfrac14\sum_x\binom{b(x)}3=\tfrac{T_3}4}✓;\qquad T_3\le28\binom{10}3+\binom53=28\cdot120+10=3370\Longrightarrow N_{\rm tetra}\le\mathbf{842}✓$$
$$\textbf{⚠️ 方向提示 ✓}:\ \text{本档所得为\textbf{上界}（}\le842\text{）；P1 所求是\textbf{正下界} ✗ —— 二者方向相反 ✓}$$

## §5 P1 现状与下一步（**诚实 ＋ 具体 ✓**）

$$\textbf{现状 ✓}:\ \text{① 几何刻画（含中点定理）已备}✓;\ \text{② }\Delta_4=0\ \text{可达 ⟹ 须用 covering 特异性}✗;\ \text{③ 上界 }842\ \text{已得，下界\textbf{未得} ✗};\ \text{④ \textbf{未找到矛盾}✗}$$
$$\textbf{（P1 的\textbf{精确剩余任务} ✓）}:\ \text{证"任一 119-cover 恰含至少一个 square/tetra 型极大 }K_4\text{"};\ \text{其\textbf{必须}用到的信息（按 §3 反证约束 ✓）}:$$
$$\qquad\text{① 覆盖性本身（每点 }b\ge1\text{）};\ \text{② 近最优（}|C|=119,\ \sum b=1309\text{）};\ \text{③ }\sum_c|S(c)\cup V(H_c)|\le451\ (\text{局部占用预算 ✓})$$
$$\textbf{（P2 预告，照唐先生 ✓）}:\ \text{若 tetra 假设不矛盾 ⟹ 转向 }N_{\rm square}+N_{\rm tetra}\ \text{的\textbf{联合 cap}，找 }(S(c),H_c)\ \text{对四类 }K_4\ \text{的容量约束}✓$$
$$\text{（反例警示登记 ✓）}:\ \text{球型码 }\Delta_4=0\ \text{说明"局部密集"本身不逼出亏空}✗ ⟹ \text{须找的是\textbf{覆盖强制}的局部形状，而非"密"本身}✓$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "偶部"
技术词 偶部            命中文件数=7    :: ./S9-strict-and-D2-prescreen.md ./thh-tp-audit.md ./C3895-T2-root-pairing-structure-registration.md
$ bash scripts/tech_word_check.sh "奇部"
技术词 奇部            命中文件数=12   :: ./V316-B-precheck-affine-intercept-constant.md ./S9-strict-and-D2-prescreen.md ./V130-O5-residue-FE-annihilation-theorem-k-point-only-even-one-sided.md
$ bash scripts/tech_word_check.sh "中点映射"
技术词 中点映射        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "excess 预算"
技术词 excess 预算     命中文件数=0    ::
$ bash scripts/tech_word_check.sh "coset"
技术词 coset           命中文件数=15   :: ./P5-Y3-SOURCE-CARD-and-AMEND9-gate-REJECT.md ./LAMBDA-SCAN-2026-09-27-coset-constant-refined-law.md ./CAPMIX1A-I-vs-truth-sound-but-incomplete.md
```
- **本档新增**：**0** 个术语 ✓（`中点映射`／`excess 预算` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`偶部`／`奇部`／`coset` 为档案已有 ✓）
- **注 ✓**：本档实质＝**§1 中点定理 ＋ §3 可达反证 ＋ §4 上界**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未碰 $T_4$／$n_j$／profile 极值** ✓（照令 ✓）；**未上 SDP/SAT/Terwilliger** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** $N_{\rm tetra}>0$ ✗；**不声称** $\Delta_4>0$ 对 119-cover 成立 ✗（V290 ✓）—— 本档**只**给几何刻画、可达反证与上界 ✓
- §2 的"配对谱"修正**必须**与 R7-LOCK §1 的同型事实一同引用 ✓（防误传"亏空整体配对不可见" ✗）
