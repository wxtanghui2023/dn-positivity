已查地图：已跑 scripts/prework_map_check.sh 119 Krawtchouk Delsarte 谱 G₀₀≤287 ⟹ 执行自 SHADOW-LEDGER-2026-09-26 与 COMPRESSION-POINT-2026-09-26 两档；本档为**BM/Krawtchouk 刀的第一验收判定**（唐先生 2026-09-26 09:38 指定）；不开旁支 ✓。
D0: 本档对象 = 层向量 Gram 的 Krawtchouk 谱形式及 `G₀₀≤287` 的谱可达性（非新对象）
D1: 0（无新独立自由度；产出为正确对象、谱恒等式、一条严格 no-go 见证）

# KRAWTCHOUK-2026-09-26 · 第一验收：谱层能否独立给出 `G₀₀ ≤ 287`？

## §1 先把对象固定正确（关键纠正）

```
$$\textbf{正确}: \delta=(S_0+S_1)*\mathbf1_C-\mathbf1\ (\text{不是 }\mathbf1_C)\ \Longrightarrow\ \widehat\delta(u)=(11-2r)\,\widehat{\mathbf1_C}(u)\ (u\ne0),\ r=\mathrm{wt}(u)$$
（因 `\hat{S_0+S_1}(u) = K_0(r)+K_1(r) = 1+(10-2r) = 11-2r` ✓；`\widehat\delta(0)=11M-1024=E` ✓）
$$\delta_i=S_i*\delta\ \Longrightarrow\ \widehat{\delta_i}(u)=K_i(r)\widehat\delta(u)\ \checkmark\ (\text{与唐先生 $K_i(r)\widehat{\mathbf1_C}$ 同形，但基底是 }\delta\ \text{不是 }\mathbf1_C)$$
```

## §2 谱形式 = **恒等式**（无新信息）

```
$$Y_r:=\sum_{\mathrm{wt}(u)=r}|\widehat{\mathbf1_C}(u)|^2\ \ge0\ (r=0..10),\qquad \sum_{r}Y_r=1024M,\quad Y_0=M^2$$
$$\sum_x b(x)^2=\frac{1}{1024}\Big[(11M)^2+\underbrace{\sum_{r\ge1}(11-2r)^2Y_r}_{=:S}\Big],\qquad \sum_x\delta(x)^2=\frac{1}{1024}\Big[E^2+S\Big]$$
$$\boxed{M=119:\quad A_1+A_2\le143\iff Q\le1\iff \sum_x b^2\le1881\iff S\le212663}$$
**恒等式自检**（实算 ✓）: `S = 4096(A_1+A_2) − const` ✓（M=119: const=373065 ✓；用 120-码反验: S=424384 = 4096·199−390720 ✓ 双向吻合 ✓）
⟹ 权重 `(11-2r)²=(K_0+K_1)²` 恰好把 `S` 变成只含 `A_1+A_2`（其余 A_i 相消）⟹ **谱形式只是坐标变换** ✓（唐先生"第四层"判断成立 ✓）
```

## §3 唯一的额外内容 = **Delsarte 正性**（10 条显式线性约束）

```
$$Y_r=M\binom{10}{r}+2\sum_{i\ge1}A_iK_r(i)\ \ge0\quad(r=1..10)\qquad(\text{因 }Y_r=\sum_{\mathrm{wt}(u)=r}|\widehat{\mathbf1_C}(u)|^2\ \text{是平方和}\ ✓)$$
（自检: `Y_0 = M·1+2Σ_{i≥1}A_iK_0(i) = M² ✓`；正交性 `Σ_i C(10,i)K_r(i)=1024δ_{r0} ✓`）
```

## §4 ⛔ **判定：NO**（严格见证，符合唐先生"第一验收标准"）

```
$$\textbf{LP 见证}:\ A_i:=t\binom{10}{i},\ \ t:=\binom{119}{2}/1023=6.86315\ \Longrightarrow\ \sum_{i\ge1}A_i=7021\ \text{精确}\ ✓$$
$$\text{实测}: Y_r=\binom{10}{r}(119-2t)>0\ \textbf{全部成立}\ ✓(\min Y_r=105.274>0),\quad Y_0=14161=119^2\ \checkmark$$
$$\text{但}\ A_1+A_2=55t=\boxed{377.47}\ \gg143\ ✗$$
**更强的事实（无需 LP）**: `Y_r ≥ 0` 对**一切**码成立（平方和 ✓）⟹ **任意随机 119-集**自动满足全部 Delsarte 约束 ✓
$$\text{而随机 119-集}: \mathbb E[A_1+A_2]=\binom{119}{2}\cdot\frac{55}{1024}=377.1\ \gg143\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{谱/Delsarte 层原理上不可能推出 }A_1+A_2\le143\ ✗}\quad(\text{NO-GO 成立 ✓})$$
```

## §5 为什么必然失败（诊断，本档最有价值）

```
crux 的真身 = 「**覆盖条件 ⟹ 距离分布约束**」（`A_1+A_2` 是距离分布量，覆盖性不是 ✓）
而谱/Delsarte 机制**只约束距离分布**，且这些约束被**非覆盖**的随机集同样满足（平方和 ✓）
⟹ **谱层对"覆盖假设"结构性失明** ✗（无论做多少阶 BM 对角化、无论 PSD 还是 LP ✗）
⟹ 与另两条一致: 局部账本 no-go（成本 ≪ 余量 ✗）｜van Wee/Haas 墙（只到 107 ✗）
$$\boxed{\text{三条独立路径同指一个缺口}:\ \textbf{能"看见覆盖条件"的独立压缩机制}\ ✗}$$
```

## §6 下一步（唯一未被否掉的方向）

```
① **整数 + 覆盖** 联合：Delsarte 是"码性"约束（随机集也满足 ✗）；
   必须显式动用 `b(x)≥1 ∀x`（覆盖）与 `M=119` 的整数结构 ✓
② 已知能"看见覆盖"的机制只有 **同余型**（Habsieger/van Wee）✗ （已达 107 ✗）
   ⟹ 若要 >107，必须造**新的覆盖可见压缩**（不是谱、不是账本）✓
⚠️ 依唐先生标准: **不进入 SDP** ✗（谱层已被严格否掉 ✓）
```

## §7 边界（诚实标注）

- §2–§4 的数值均为**实算**（Krawtchouk 正交性、LP 见证、120-码反验 ✓）；本轮为**纯数论/线性代数小算**，未跑 SDP/ILP ✓
- **未**排除 Q=1 ✗、**未**排除 119 ✗；本档只否掉**方法类**（谱/Delsarte 层）✓
- `Y_r ≥ 0` 的成立性为**恒真**（平方和 ✓）——不依赖任何假设 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 覆盖盲        命中文件数=0    :: 
技术词 准随机见证  命中文件数=0    :: 
技术词 谱层           命中文件数=8    :: ./p59s-fixed-direction.md ./NOGO-registry-and-screens.md ./MASTER-NOGO-AND-LIVE-PATHS.md 
技术词 Delsarte 正性  命中文件数=0    ::
```

- **本档新增**（命中数=0）：`覆盖盲`、`准随机见证`、`Delsarte 正性`（含空格，回查解析器按首词匹配 ✓）
- **档案已有（引用，不列为提出）**：谱层
