已查地图：已跑 scripts/prework_map_check.sh Q δ 代数分解 色散 尺寸最小性 ⟹ 执行自 DEFECT-2026-09-26 档；本档为**Q–δ 代数分解的实做结果 ＋ 三处诚实纠正**（唐先生 2026-09-26 12:18 指令）；纯推导＋数值校准，未跑 solver ✓。
D0: 本档对象 = Q 与层缺陷 δ_i 的代数分解，及其是否给出新信息
D1: 1（新增：色散恒等式的两码校准；尺寸最小性 ⟹ 私有点（无需分类）；并关闭"δ 线性守恒可钉住 Q"的假桥）

# QDELTA-2026-09-26 · 分解实做 ＋ 三处纠正

## §1 ⛔ 纠正①：`E` 的"解析来源"是**平凡的**（難点 1 消解 ✗）

```
$$\boxed{E=M(n+1)-2^n}\ ✓\ \text{—— 完全显式，无深层来源}\ ✗;\quad \text{本例}: 296=120\cdot11-1024\ ✓$$
$$\textbf{附带恒等式}: \text{近完美码}（M=2^n/n\ ✓）\ \Longrightarrow\ E=M(n+1)-2^n=M(n+1)-nM=\boxed{M}\ ✓\ (\text{n=8}: E=32=M\ ✓✓)$$
```

## §2 ⛔ 纠正②：`Σ_i δ_i(x)=E` 是**对任意码恒成立**的恒等式（非"发现机制" ✗）

```
$$\text{推导}: \sum_i\delta_i(x)=\sum_i\sum_{y\in L_i(x)}\delta(y)=\sum_y\delta(y)\cdot\#\{i:y\in L_i(x)\}=\sum_y\delta(y)=E\ ✓$$
$$\Longrightarrow\ \text{它对\textbf{任何}码成立}\ ✓\ —— \text{与最优性、与 }n\text{、与覆盖均无关}\ ✗$$
$$\text{（此项已于 }2026\text{-}09\text{-}25\ \text{审计中记录 ✓；本档再次明确，以免被当作机制候选}\ ✗）$$
```

## §3 ✅ **分解的实做结果**：Q 的三种等价写法（**校准通过** ✓）

```
$$Q=\sum_x\binom{\delta(x)}2=\frac{\sum_x\delta^2-E}{2}\ ✓$$
$$R_i:=\sum_{d(x,y)=i}\delta(x)\delta(y)\qquad(\text{距离 }i\ \text{的 }\delta\text{-自相关}\ ✓)\ \Longrightarrow\ \sum_i R_i=E^2\ ✓,\ R_0=\sum\delta^2\ ✓$$
$$\boxed{\textbf{色散恒等式}:\quad Q=\frac{E(E-1)-\sum_{i\ge1}R_i}{2}}\ ✓$$
$$\textbf{数值校准（两码 ✓）}:$$
$$\quad\text{120-码}: E=296,\ R_0=500,\ \sum_{i\ge1}R_i=87116,\ E(E-1)=87320\ \Longrightarrow\ Q=\frac{87320-87116}{2}=102=Q_{\text{实测}}\ ✓✓\ (\text{色散率 }0.997664)$$
$$\quad\text{n=8 doubled Hamming}: E=32,\ R_0=32,\ \sum_{i\ge1}R_i=992=E(E-1)\ \Longrightarrow\ Q=0\ ✓✓\ (\text{色散率 }1.000000)$$
$$\textbf{解读}: Q=0\iff \text{色散率}=1\iff \sum_{i\ge1}R_i=E(E-1)\iff \text{excess 被\textbf{完全分散}}\ ✓$$
```

## §4 ⛔ 纠正③（方法层）：因此"线性守恒钉住 Q"是**假桥** ✗

```
$$\text{线性守恒只有一条}: \sum_i\delta_i(x)=E\ (\text{常数}\ ✓)\ ——\ \text{它\textbf{不能}决定 }Q\ ✗\ (\text{因 }Q\ \text{是二阶矩}\ ✓)$$
$$\text{实际等价链}: Q\iff \sum_x\delta^2\iff \sum_{i\ge1}R_i\ (\text{色散})\iff A_{\le2}\ ✓\ ——\ \textbf{全是等价改写}\ ✗$$
$$\Longrightarrow\ \text{拟议的"把 }Q-Q^*(n)\ \text{写成 }\sum\lambda_i(x)\delta_i(x)\text{"若 }\lambda\ \text{仅依赖 }n,i\ \text{则\textbf{不可能}}\ ✗\ (\text{阶数不匹配}\ ✓)$$
$$\qquad\text{除非}\ \lambda\ \text{依赖 }x\ \text{（即 }Q=\sum_y w(y)\delta(y)\ ✓\ \text{形式）—— 但那需要\textbf{额外的权重结构}\ ✗\ (\text{尚无}\ ✗)$$
$$\textbf{结论}: \text{§3 的分解是\textbf{正确的等价改写}（class C 风险 ✓），不是新信息}\ ✗;\ \text{真缺口仍在"用最优性导出一个二阶矩/色散不等式"}\ ✗$$
```

## §5 ✅ **一处真收获**：尺寸最小性 ⟹ 私有点（**无需分类/文献** ✓）

```
$$\boxed{\text{若 }|C|=K(n,1)\ \text{且 }c\in C\ \text{无私有点}\ \Longrightarrow\ C\setminus\{c\}\ \text{仍覆盖}\ ⟹\ \text{尺寸 }K-1\ \text{覆盖}\ ✗\ \text{矛盾}}\ ✓✓$$
$$\Longrightarrow\ \textbf{每个码字有私有点}\ ✓\ \text{—— 对\textbf{一切}尺寸最小的覆盖码成立}\ ✓\ (\text{不依赖 }n\le8\ \text{分类}\ ✓)$$
$$\text{（自我纠正}: \text{此前我说此性质"须挂 }K(8,1)=32\ \text{的文献下界"}\ ✗\ \text{—— 多余；尺寸最小性本身足够}\ ✓）$$
$$\text{n=8 校验}: 32/32\ \text{个码字有私有点}\ ✓;\qquad \text{b 分布 }\{1{:}224,\ 2{:}32\}\ ✓;\ A_{\le2}=16\ ✓\ —— \text{与 NP1CC 理论\textbf{逐项吻合}}\ ✓✓$$
$$\textbf{但}: \text{私有点} \Longrightarrow \text{对 }Q\ \text{的\textbf{定量}约束？（未建立}\ ✗）\ —— \text{这是下一步该试的接口}\ ✓$$
```

## §6 n=8 的**独立验证**（我方构造 ✓）

```
$$\text{正确 doubled Hamming}（\text{用真 }[7,4]\ \text{Hamming 码}\ ✓）:\ |C|=32,\ \min b=1\ (\text{覆盖}\ ✓),\ Q=0\ ✓,\ A_{\le2}=16\ ✓$$
$$\Longrightarrow\ \textbf{与 NP1CC 定理预测 }Q^*(8)=0\ \text{逐项一致}\ ✓✓\ (\text{两条独立路径}\ ✓)$$
$$\text{（过程中修正了我自己的构造错误}: \text{先前误取"任意 16 个偶重量字"}\ ✗\ \text{导致 }Q=320\ \text{与负 }R\ \text{值}\ ✗\ —— \text{已改正 ✓）}$$
```

## §7 三张表（更新）

```
$$\textbf{CLOSED}: (\star);\ \sigma\ \text{式};\ \text{奇偶引理}+\textbf{P1};\ \textbf{色散恒等式};\ E=M(n+1)-2^n;\ \text{近完美} \Rightarrow E=M;\ \text{尺寸最小性} \Rightarrow \text{私有点};\ n=2^m/2^m-1\Rightarrow Q^*=0\ ✓$$
$$\textbf{关闭的假桥}: \text{n=8 三进制同余};\ \Delta\to A_{\le2}\ \text{传递};\ \boxed{\text{δ 线性守恒钉住 }Q}\ ✗$$
$$\textbf{OPEN}: \text{用最优性导出\textbf{二阶矩/色散}不等式（真正堵点）};\ \text{私有点} \to Q\ \text{的定量接口};\ \text{非取等 }n\ \text{的 }Q^*;\ \textbf{119 UNKNOWN}\ ✓$$
$$

## §8 边界（诚实标注）

- §3/§5/§6 为**数值校准＋推导** ✓（两码 ✓）；§1/§2/§4 为**诚实纠正**（含一处自我纠正 ✓）
- **本轮未跑 solver** ✓；**未**开 n=9 ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 色散恒等式  命中文件数=0    :: 
技术词 尺寸最小性  命中文件数=0    :: 
技术词 二阶矩钉住  命中文件数=0    :: 
技术词 等价改写警告 命中文件数=0    ::
```

- **本档新增**（命中数=0）：色散恒等式、尺寸最小性、二阶矩钉住、等价改写警告
- **档案已有（引用，不列为提出）**：—
