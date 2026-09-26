已查地图：已跑 scripts/prework_map_check.sh pinning 命题 适用域 n=8 证伪 ⟹ 执行自 PINNING-2026-09-26-notation-lock-and-class-data 档；本档为**命题澄清 ＋ n=8 方法失败登记**（唐先生 2026-09-26 11:03 指令）；不开新方向 ✓。
D0: 本档对象 = 钉住命题的精确陈述与 n=8 证伪尝试（非新对象）
D1: 0（无新自由度；产出为命题澄清、sanity check、方法失败台账）

# PINNING-PROPOSITION-2026-09-26

## §1 ⚠️ **命题澄清（关键，防日后误用）**

```
$$\textbf{从未主张}:\ \text{"一切最优覆盖码皆 }Q=4"\ ✗\ ——\ \text{这个命题\textbf{已被 doubled-Hamming }(8,32)_1\ \text{的 }Q=0\ \text{反驳}\ ✗✗$$
$$\boxed{\textbf{我们的命题（逐 }n\text{ 钉住）}:\ \text{对每个 } n,\ \text{在 } M=K(n,1)\ \text{处，全部最优码共享同一个 } Q^*(n)}\ ✓$$
$$\text{已定}: Q^*(4)=0,\ Q^*(5)=2,\ Q^*(6)=4,\ Q^*(7)=0\ (\text{强制}),\ Q^*(8)\ni 0\ (\text{至少一例})$$
$$\Longrightarrow\ \text{doubled-Hamming 的 }Q=0\ \textbf{不是反例}\ ✗\ \text{——它只是把 }Q^*(8)=0\ \text{那一格钉住}\ ✓$$
$$\textbf{真正的证伪判据}: \text{同一个 } n\ \text{上出现两个不同的 } Q\ ✗$$
```

## §2 **记号锁定的 sanity check**（唐先生要求 ✓）

```
$$\textbf{最直接的复算例（}n=6\ \text{类1）}:\ (A_1,A_2,E,Q)=(4,\ 8,\ 20,\ 4)\qquad 2(4+8)-20=\mathbf{4}=Q\ ✓$$
$$b\ \text{分布}: \{1{:}48,\ 2{:}12,\ 3{:}4\}\ \Longrightarrow\ Q=4\cdot\binom{2}{2}=\mathbf{4}\ ✓\ (\text{全部来自 4 个三重覆盖点 }b=3\ ✓)$$
$$\text{而 }A_2=8\ne Q=4\ \Longrightarrow\ \textbf{符号混用在此例上立刻出错}\ ✗\ (\text{正是 notation lock 的意义}\ ✓)$$
```

## §3 ⛔ **n=8 证伪尝试：两次方法失败**（诚实登记 ✓，防重复劳动 ✓）

```
$$\text{尝试①}: (k,k)\ \text{-保覆盖切换（从 doubled Hamming 出发）}:\ 接受 3223\ \text{次但只收集到 1 个码}\ ✗$$
$$\qquad\text{根因}: \text{修复候选集未排除被移除的词}\ ✗\ \Longrightarrow\ \text{优雅退化（把原词放回）} ✗$$
$$\text{尝试②}: \text{同一设计修正后}（k=2,3）:\ \text{长时间无新码输出}\ ✗\ \Longrightarrow\ \text{该邻域几乎无可用修复} ✗$$
$$\text{尝试③}: \textbf{结构性族} C(A,B)=\{(a,0)\}\cup\{(b,1)\},\ A=H_7,\ B\ \text{任意 16 子集};\ \text{覆盖} \iff N(B)\cup A=\text{全空间}$$
$$\qquad\text{实测}: \textbf{接受 0 次 (1,1)-B 移动}\ ✗\ \Longrightarrow\ \text{该族内 } B=H_7\ \text{极刚（几乎唯一）}\ ✓$$
$$\boxed{\text{三次均为 \textbf{方法失败} ✗，非数学结论} ✗\ \text{——不得写成"n=8 只有 }Q=0\text{"}\ ✗}$$
```

## §4 n=8 剩余**唯一决定性**路线

```
$$\text{证伪目标可精确改写}: \exists\ (8,32)_1\ \text{码含 } b(x)\ge3\ \text{的点} \iff Q>0\ ✗\ (\text{一个例子即推翻}\ ✗)$$
$$\Longrightarrow\ \text{用 \textbf{CP/SAT 定向判定}（256 布尔变量 ＋ 恰好 32 个 ＋ 256 条覆盖约束 ＋ 一个"某点重数}\ge3\text{"约束）}\ ✓$$
$$\text{成本}: \text{模型远小于此前 11k 约束的失败案例}\ ✓;\ \text{须遵守"单次建模、不重建"纪律}\ ✓$$
```

## §5 状态（采用唐先生措辞 ✓）

```
$$\boxed{\text{至少两个已验证样本满足 } Q=4;\quad \textbf{pinning 尚未被证伪，也尚未被证明}}\ ✓$$
$$\text{OPEN}: B_6\text{-类数} ✗\ |\ B_8\text{-类数} ✗\ |\ n=8\ \text{是否存在 }Q\ne0\ ✗\ |\ \textbf{n=10, M=119: UNKNOWN}\ ✓$$
$$\text{域限定}: \text{"全部最优码 }Q=4"\ ✗\ \text{已被 }(8,32)_1\ \text{反驳}\ ✗\ \Longrightarrow\ \text{命题必须写作\textbf{逐 }n\ \text{钉住}}\ ✓$$
```

## §6 边界（诚实标注）

- §1/§2 为**命题澄清与复算** ✓；§3 为**我方方法失败** ✗（脚本 `work/k10/q10proto/{n8_falsify,n8_falsify2,n8_gendouble}.py` ✓）
- **未**排除任何 n ✗；**未**对 n=10 外推 ✗；**未**触碰 119 结论 ✓
- 后台进程已清（slots 1/2 ✓，无残留 ✓）

## 【技术词回查】（定稿前逐字输出）

```
技术词 逐n钉住       命中文件数=0    :: 
技术词 定向判定路线 命中文件数=0    :: 
技术词 方法失败记录 命中文件数=0    :: 
技术词 结构族刚性  命中文件数=0    ::
```

- **本档新增**（命中数=0）：逐n钉住、定向判定路线、方法失败记录、结构族刚性
- **档案已有（引用，不列为提出）**：—
