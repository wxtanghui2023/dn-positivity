已查地图：已跑 scripts/prework_map_check.sh square Q_ours 4S 等号 private-point ⟹ 执行自 B-2026-09-26 档；未跑 solver ✓。
D0: 本档对象 = square–Q_ours incidence 不等式、其等号情形，及 (9,64) 码的等号实例
D1: 1（新增：**4S ≤ Q_ours 验证 ✓**；**(9,64) 取等 ✓✓**；面计数 4× 过计已修 ✗）

# SQUARE-2026-09-26

## §1 ⚠️ 我方计数错误（已修 ✓）

```
$$\text{上轮报 }S=32\ ✗\ ——\ \text{去重条件只排除了 4 分之一}\ ✗:\ \text{每个 2-面被 }(z,p,q)\ \text{三元组生成 8 次}\ ✓,\ \text{条件只留下 4 次}\ ✗$$
$$\text{修正（规范形：自由位全 0 的顶点唯一 ✓）}\Longrightarrow \textbf{S}(9,64)=\mathbf{16}\ ✓✓$$
$$

## §2 ✅ **不等式验证 ＋ 等号实例** ✓✓（唐先生的 §7/§8 ✓）

```
$$\text{逐点容量（唐先生 ✓）}: r(x):=\#\{\text{过 }x\ \text{的 code squares}\}\ \le\ \binom{b(x)-1}{2}\quad(x\in C)\ ✓✓$$
$$\qquad(\text{理}: r(x)\ \text{数的是 }x\ \text{的码字邻居对}\ ✓;\ x\in C\ \text{时 }b(x)-1=d_C(x)\ ✓)$$
$$\Longrightarrow\ 4S=\sum_x r(x)\ \le\ \sum_{x\in C}\binom{b(x)-1}{2}\ \le\ Q_{\mathrm{ours}}\ ✓✓$$
$$\textbf{核验（n=4,4/4,5/5,7 全枚举 ✓）}: r(x)\ \text{违反}=0\ ✓;\ 4S\le Q_{\mathrm{ours}}\ \textbf{全过}\ ✓$$
$$\boxed{\textbf{(9,64) 我方构造}: E=128,\ Q_{\mathrm{ours}}=64,\ N_{\ge3}=64,\ \mathbf{S=16},\ V=64,\ \Sigma r=4S=64\ \Longrightarrow\ \mathbf{4S=Q_{\mathrm{ours}}\ \text{取等}}\ ✓✓}$$
$$\qquad\text{结构}: 16\ \text{个 2-面\textbf{顶点不交}}\ ✓\ (V=4S\ ✓);\ \text{每个 hot 顶点}\ b=3\ \text{恰由"自身＋两个面邻点"构成}\ ✓;\ r(x)=1\ \forall\ hot\ ✓$$
$$\qquad\Longrightarrow\ \textbf{该码正是唐先生 §8 的"邻居对闭合"情形}\ ✓✓\ (\text{每个码字邻居对都闭成面}\ ✓)$$
$$

## §3 符号警告（我方补 ✓）

```
$$\text{唐先生写 }Q_{\mathrm{ours}}=\sum_x\binom{d_C(x)}2\ ⚠️\ ——\ \textbf{仅对 }x\in C\ \text{成立}\ ✗:\ x\notin C\ \text{时 }b(x)=d_1(x)\ \text{而 }b(x)-1\ne d_C(x)\ ✗$$
$$\text{正确}: Q_{\mathrm{ours}}=\sum_{x\in C}\binom{d_C(x)}2+\sum_{x\notin C,\ b(x)\ge3}\binom{b(x)-1}{2}\ ✓$$
$$

## §4 M=62 的严格预算（唐先生链 ✓ ＋ 我方 L2 ✓）

```
$$E=10\cdot62-512=108\ ✓$$
$$\textbf{我方新引理 L2}: N_{\ge3}\le E/2\ ✓\ (\text{由 }N_{\ge3}\le E-Q_{\text{user}}\ \text{与}\ Q_{\text{user}}\ge N_{\ge3}\ ✓)\ \Longrightarrow\ \textbf{62-码}: N_{\ge3}\le54\ ✓$$
$$\textbf{若 }b\in\{1,3\}:\ N_3=54\ \Longrightarrow\ Q_{\mathrm{ours}}=54\ \Longrightarrow\ \boxed{S\le13}\ ✓\ (\text{严格必要 ✓})$$
$$\qquad\text{若进一步取等 }4S=Q_{\mathrm{ours}}\Longrightarrow S=13.5\notin\mathbb Z\ \Longrightarrow\ \textbf{取等不可能}\ ✓✓\ (\text{强约束 ✓})$$
$$

## §5 ⚠️ 关键限定（支持唐先生自己的警告 ✓）

```
$$\text{小最优码 }(n=4,M=4),(n=4,M=5),(n=5,M=7):\ \textbf{S=0}\ ✓\ (\text{无任何 2-面}\ ✓)$$
$$\Longrightarrow\ \textbf{square 不是最优性的必要条件}\ ✗\ \Longrightarrow\ \text{Wille 的 square(\text{若真})是其\textbf{构造指纹}}\ ✓,\ \text{非 62-极值的必然结构}\ ✓$$
$$\text{另}: \text{唐先生引的 Kéri 匈牙利文献中，我方\textbf{未见} "Wille 码含 2-面" 的逐字陈述}\ ⚠️\ (\text{该源我抓到了 191 页全文 ✓，仅见 Wille 与 62 的一般叙述 ✓})\ \Longrightarrow\ \textbf{标注待核}\ ⚠️$$
$$

## §6 台账

```
$$\textbf{新资产}: 4S\le Q_{\mathrm{ours}}\ ✓\ (\text{＋(9,64) 取等实例}\ ✓);\ N_{\ge3}\le E/2\ ✓;\ r(x)\le\binom{b(x)-1}{2}\ ✓$$
$$\textbf{已淘汰}: \dots\ (\text{承前});\quad \text{修正}: S(9,64)=16\ \text{而非 }32\ ✗$$
$$\textbf{桥}: \text{未打通}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓$$
$$

## 【技术词回查】（定稿前逐字输出）

```
技术词 等号情形     命中文件数=5    :: ./C3814-sharp-closure-of-C380-13-trig-dual-type-sigma-a-le-6c0.md ./RESEARCH-CONSTITUTION.md ./ASSET-NATIVE-INDEPENDENT-PROBLEMS.md 
技术词 邻居对闭合  命中文件数=0    :: 
技术词 面不交        命中文件数=0    :: 
技术词 面计数规范形 命中文件数=0    ::
```

- **本档新增**（命中数=0）：邻居对闭合、面不交、面计数规范形
- **档案已有（引用，不列为提出）**：等号情形
