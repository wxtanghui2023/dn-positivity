# AUDIT-2026-09-29w — **坐标-cell／Walsh 系统\ \textbf{已测}：推导全对，但 $r\le7$ \textbf{无矛盾}；且该族线性松弛有\ \textbf{天花板}**

> **性质**：**推导核验 ＋ 决定性测试 ＋ 天花板定位**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:2x ✓
> **唐先生令**：「先只做 $r=2$ 的测试；若 $r=2$ 就矛盾才有新 P1」✓

**已查地图**：`AUDIT-29v`（结合方案层天花板）／`29m`（Delsarte 对 106 可行）／`SUBSPACELP`（LP 层零增益）✓

D0: 本档对象 ＝ **档案已有**（cell 覆盖计数／Walsh 系数——无新数学对象 ✓）
D1: 0（产出＝**推导核验 ＋ $r\le7$ 可行性判定 ＋ 该族天花板之证明** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 你的推导\ \textbf{全对}}:\ \text{cell 覆盖不等式在 120-code 上}\ r{=}1,2,3\ \text{\textbf{零违例}};\ \text{系数}\ 11-2|T|\ \textbf{核实}}$$
$$\boxed{\text{② ✗ 决定性测试}:\ M{=}106\ \text{时该 Walsh 系统}\ r{=}1,\ldots,7\ \text{\textbf{皆可行}} \Longrightarrow\ \textbf{无矛盾}}$$
$$\boxed{\text{③ ★ 结构性原因（\textbf{该族天花板}）}:\ r{=}10\ \text{之 cell 系统\ \textbf{就是}逐点覆盖条件；其线性松弛＝经典覆盖 LP}\Longrightarrow \text{对 }M{\ge}94\ \text{恒可行}}$$

## §1 ① 推导核验（**✓✓**）

$$\text{cell 覆盖恒等式}:\ (11-r)N_u+\sum_{i\in U}N_{u\oplus e_i}\ \ge\ 2^{10-r}\qquad(|U|{=}r)$$
$$\text{（说明}:\ \text{cell 内中心贡献 }11-r\ \text{点；相邻 cell（翻转一个固定坐标）各贡献 }1\ \text{点）}✓$$
$$\text{Walsh 展开}:\ \sum_{T\subseteq U}(11-2|T|)\chi_T(u)S_T\ \ge\ 2^{10}(=1024)✓\qquad(\text{系数 }11-2|T|\ \textbf{逐项核实})✓$$

**实测（120-code）**：$r{=}1$：$20$ 约束，$0$ 违例 ✓；$r{=}2$：$180$ 约束，$0$ 违例 ✓；$r{=}3$：$960$ 约束，$0$ 违例 ✓

$$\text{（次要}:\ \text{我的抽样打印把 }u\leftrightarrow\text{cell 之对应排错了一格（多重集 }\{31,29,28,32\}\ \text{与 }\{32,28,29,31\}\ \text{同集}）;\ \text{公式本身正确}✓）$$

## §2 ② 决定性测试（**✗ 无矛盾**）

$$\text{变量}:\ \{S_T:1\le|T|\le r\};\qquad \text{约束}:\ \text{每 }r\text{-cell}\times\text{每符号 }u:\ \sum(11-2|T|)\chi_T(u)S_T\ \ge\ -142$$
$$\text{（\textbf{单侧有效}：若不可行 ⟹ 106 被排除；可行 ⟹ 无结论）}$$

| $r$ | 变量 | 约束 | 可行? | 耗时 |
|---|---|---|---|---|
| $1$ | $10$ | $20$ | **✓ 可行** | $0.0$s |
| $2$ | $55$ | $180$ | **✓ 可行** | $0.0$s |
| $3$ | $175$ | $960$ | **✓ 可行** | $0.0$s |
| $4$ | $385$ | $3360$ | **✓ 可行** | $0.2$s |
| $5$ | $637$ | $8064$ | **✓ 可行** | $1.2$s |
| $6$ | $847$ | $13440$ | **✓ 可行** | $12.1$s |
| $7$ | $967$ | $15360$ | **✓ 可行** | $33.1$s |

$$\therefore\ \boxed{r=2\ \textbf{不产生矛盾};\ \text{且直到 }r{=}7\ \text{亦无}}✗$$

## §3 ★ ③ 该族之天花板（**证明 ✓✓**）

$$\text{取 }r{=}10:\ \text{cell}＝\text{单点};\ \text{不等式}＝\ \sum_{T}(11-2|T|)\chi_T(x)S_T\ \ge\ 1024\ \Longleftrightarrow\ \text{每点被覆盖}✓$$
$$\therefore\ \boxed{\text{r-层 cell 系统族之 }r{=}10\ \text{级\ \textbf{恰是}逐点覆盖条件本身}}$$
$$\text{而其\ \textbf{线性松弛}（对 }S_T\ \text{自由）＝经典覆盖 LP};\ \text{本会话已证其界 }=93.09\Rightarrow94$$
$$\therefore\ \boxed{\text{对任何 }M\ge94\ \text{（含 }106\text{），该线性松弛\ \textbf{恒可行}} \Longrightarrow\ \text{此族\ 作为线性松弛\ \textbf{永不能排除 }106}}✗✓$$

## §4 ⟹ 缺的那一件（**与你的 §8/§10 一致 ✓**）

$$\text{线性部分（cell 覆盖）\textbf{已到底}};\ \text{唯一可能的新内容＝\ \textbf{非线性＋整性}}$$
$$\text{你正确点名的\ \textbf{Parseval}:\ }\sum_T S_T^2=2^{10}|C|=1024M\ \Longleftrightarrow\ \sum_x f(x)^2=\sum_x f(x)\ (\textbf{即 }f\in\{0,1\})✓$$
$$\text{配合 }f\ge0\ \text{与 }\sum f=M,\ \text{这确实\ \textbf{强制 }f\ \text{为指示函数}}✓$$
$$\therefore\ \text{但}:\ \text{把 Parseval（二次）以 SDP 松弛，正是\ \textbf{SDP-3 ＝ }105.2223\Rightarrow106\ \text{之路}}✗$$
$$\therefore\ \boxed{\text{坐标-cell 路\ 最终仍落在同一天花板（线性 }94\text{ ／ SDP }105.22\text{）}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "cell覆盖不等式" "Walsh层无矛盾" "线性松弛天花板"
技术词 cell覆盖不等式   命中文件数=0    ::
技术词 Walsh层无矛盾    命中文件数=0    ::
技术词 线性松弛天花板   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- **120-code 全量 ＋ LP 逐 $r$ 实测** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 含**我之抽样打印映射错**之标注 ✓；**不主张** $107$ 不可达 ✗（V290）
