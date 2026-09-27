已查地图：已跑 scripts/prework_map_check.sh A≤2 桥 Q 钉住 最小性 ⟹ 执行自 BRIDGE-2026-09-26 / C62-WILLE-RECOVERED / CENSUS-2026-09-26 / CHANNELS-2026-09-26 ✓；本档 = **靶子形式更正 ＋ 下一步可测命题** ✓。
D0: 本档对象 = 119 主线"最小性 → 刚性"桥的精确形式
D1: 0（档案勘误 ＋ 靶子定型 ✓，不产生新数学命题 ✓）

# LEDGER-2026-09-27 · $A_{\le2}$ 桥的靶子更正

## §1 档案原定义（逐字 ✓，不改动）

```
$$A_{\le2}=\frac{\sum_x b(x)(b(x)-1)}{4}\ ✓\ \text{—— 等价于}\ \#\{\text{距离}\le2\ \text{的码字无序对}\}\ ✓\ \text{（因 }\sum_x\binom{b(x)}2=2A_{\le2}\ ✓\text{）}$$
$$Q=2A_{\le2}-E\ ✓;\qquad Q=Q_{\rm in}+Q_{\rm out},\quad Q_{\rm in}=\sum_{c\in C}\binom{d_1(c)}2\ ✓,\ Q_{\rm out}=\sum_{x\notin C}\binom{b(x)-1}2\ ✓$$
$$E=M(n+1)-2^n\ ✓;\qquad A_{\le2}\ge\Big\lceil\frac E2\Big\rceil\ \text{（来自 }Q\ge0\ ✓=\text{LP 界}\ ✓）$$
$$\text{极值特异存活量（K=62 双码钉住 ✓✓）}:\ Q,\ A_{\le2},\ N_1,\ (N_j)\ ✓;\qquad \text{已关闭}:\ \delta\text{-守恒}/private/P_2/\text{下界方向}\ ✓$$
$$
$$
```

## §2 勘误（**关键 ⚠️**）：$M=K\Rightarrow A_{\le2}\le2$ 不成立

```
$$\begin{array}{c|c|c|c|c}
n & M=K(n,1) & E=M(n+1)-2^n & A_{\le2}\ \text{（档案实测 ✓）} & Q=2A_{\le2}-E\\
\hline
4 & 4 & 4 & 2 & 0\ ✓\\
5 & 7 & 10 & 6 & 2\ ✓\\
6 & 12 & 20 & 12 & 4\ ✓\\
9 & 62 & 108 & 73 & 38=Q_2\ ✓\\
\end{array}$$
$$\Longrightarrow\ \text{"}A_{\le2}\le2\text{" 与 }n=5\ (6),\ n=6\ (12),\ n=9\ (73)\ \textbf{冲突} ✗\ \text{（BRIDGE-2026-09-26 §2 ✓）}$$
$$\text{同样，BRIDGE 档已把桥锐化为}:\ \textbf{在 }M=K\ \text{处 }Q\ (\text{等价 }A_{\le2})\ \text{的\textbf{上界}}\ ✗;\ \textbf{下界方向已耗尽} ✗$$
$$
$$
```

## §3 三种候选靶子（**请唐先生确认 ✓**）

```
$$\textbf{(A) 锐上界型}:\ \text{证 }A_{\le2}\le f(E,n)\ \text{（与 }\lceil E/2\rceil\ \text{相配 ✓）}\ \Longrightarrow\ \text{钉住 }Q\ ✓$$
$$\qquad\text{数据: }A_{\le2}-\lceil E/2\rceil = n=4:0\ ✓;\ n=5:1\ ✓;\ n=6:2\ ✓;\ n=9:73-54=19\ ✗$$
$$\textbf{(B) 超额归零型}:\ \text{证 }A_{\le2}-\lceil E/2\rceil\le 2\ \Longrightarrow\ Q\le4\ \text{—— 但 }n=9\ \text{反例（19）} ✗\ \text{除非对 }n\ \text{加限制 ⚠️}$$
$$\textbf{(C) 直接钉住型】}:\ \text{证 }\forall C,\ |C|=K(n,1)\Longrightarrow Q(C)=Q^*(n)\ ✓\ \text{（题面最干净 ✓）}$$
$$\qquad\text{已有}: Q^*(4)=0,\ Q^*(5)=2,\ Q^*(6)=4,\ Q^*(7)=Q^*(8)=0\ ✓;\ n=2^m\Longrightarrow Q^*=0\ ✓;\ \text{van Wee 取等}\Longrightarrow Q^*=0\ ✓$$
$$\qquad\text{反方向 }Q^*=0\Rightarrow n\in\{2^m,2^m-1\}\ \text{仍开} ⏳\ \text{（＝你标 C1 ✓）}$$
$$
$$
```

## §4 建议的下一步（**不猜靶子 ✓**；确认后即执行）

```
$$\text{① 先把"钉住"改写成可测命题}:\ \exists f:\ |C|=K(n,1)\Longrightarrow A_{\le2}=f(n)\ ✓\ \text{（或 }Q=f(n)\ ✓）$$
$$\text{② 逐 }n\ \text{校验表}:\ \text{汇总档案已有值 }(n=4,5,6,7,8,9\ ✓)\ \text{⟹ 找 }A_{\le2}\ \text{与 }(E,n,\ \text{van Wee 取等})\ \text{的精确公式候选 ✓}$$
$$\text{③ 再谈证明}:\ \text{上界机制（唯一未耗方向 ✓）}$$
$$\text{④ 纪律}:\ \text{不再走 }\delta\text{-守恒}/private/P_2/下界方向 ✗（档案已关闭 ✓）；每步须过 AMEND-31/32 的 D>0 与四门 ✓}$$
$$
$$
```

## §5 边界

- §1 逐字引档案 ✓；§2 为**勘误**（数据冲突已列 ✓）；§3 三种靶子待唐先生确认 ⚠️；§4 为路线 ✓
- 本档**不**主张任何新数学结果 ✗；**不**改动 119 的 UNKNOWN 状态 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$A_{\le2}$ 靶子勘误、三候选靶子表、逐 $n$ 校验路线
- **档案已有（引用，不列为提出）**：BRIDGE、C62、CENSUS、CHANNELS、$Q^*$、van Wee


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 靶子勘误     命中文件数=1    :: ./LEDGER-2026-09-27-A-le2-target-correction.md 
技术词 三候选靶子  命中文件数=1    :: ./LEDGER-2026-09-27-A-le2-target-correction.md
```
- **本档新增**：$A_{\le2}$ 靶子勘误、三候选靶子表、逐 $n$ 校验路线（见上方命中数；0 命中者为自造语／内部标签 ✓）
