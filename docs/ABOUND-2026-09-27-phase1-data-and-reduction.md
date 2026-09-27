已查地图：已跑 scripts/prework_map_check.sh A≤2 上界 二阶矩 profile 钉住 ⟹ 执行自 `LEDGER-2026-09-27`（靶子 (A) ✓）＋ 唐先生 12:09（开 (A) ✓）；本档 = **(A) 第一阶段：数据表 ＋ 干净归约 ＋ 机制候选** ✓（无经验拟合 ✓）。
D0: 本档对象 = $M=K(n,1)$ 下 $A_{\le2}$ 的锐上界（$\equiv$ profile 二阶阶乘矩的界）
D1: 1（新增：**干净归约 $2A_{\le2}=\frac12\sum_jj(j-1)N_j$ ✓**；**数据一致性核算 ✓**；**已验证 $Q^*=0$ 的分类 ✓**）

# (A) 第一阶段：数据 → 归约 → 机制

## §0 结论（先给）

```
$$\boxed{\textbf{(AD-1 干净归约 ✓)}\ \text{profile 前两矩已钉死}:\ \sum_jN_j=2^n\ ✓,\quad\sum_jjN_j=M(n+1)=2^n+E\ ✓;\quad \boxed{Q=\tfrac12\sum_jj(j-1)N_j-E}\ ✓}$$
$$\qquad\Longleftrightarrow\ 2A_{\le2}=\tfrac12\sum_jj(j-1)N_j\ ✓\ \text{—— 故\textbf{唯一自由量} = profile 的\textbf{二阶阶乘矩}\ ✓（\textbf{靶子即此} ✓）}$$
$$\boxed{\textbf{(AD-2 双通道 ✓)}\ Q=Q_{\rm in}+Q_{\rm out},\quad Q_{\rm in}=\sum_{c\in C}\binom{d_1(c)}2\ ✓,\ Q_{\rm out}=\sum_{x\notin C}\binom{b(x)-1}2\ ✓\ \text{（码字侧／非码字侧分离 ✓）}}$$
$$\boxed{\textbf{(AD-3 已验证的 }Q^*=0\ \text{分类 ✓✓)}\ n\in\{2^m,2^m-1\}\ \Longrightarrow\ \text{van Wee 取等}\ \Longrightarrow\ \text{nearly-perfect}\ \Longrightarrow\ Q^*(n)=0\ ✓\ \text{（已证 ✓，档案 CLOSE-$n8$ ✓）}}$$
$$\qquad\textbf{反方向}:\ Q^*(n)=0\Longrightarrow n\in\{2^m,2^m-1\}\ \text{仍开} ⏳\ \text{（＝唐先生 C1 ✓；}\textbf{不能用 }n=4,7,8\ \text{样本外推} ✗\ ✓）$$
$$
$$
```

---

## §1 数据表（$n=4..9$，全部核算 ✓）

```
$$\begin{array}{c|c|c|c|c|c|c}
n & K(n,1) & 2^n & E=K(n+1)-2^n & A_{\le2} & Q=2A_{\le2}-E & Q/2\ (\text{超额})\\
\hline
4 & 4 & 16 & 4 & 2 & 0 & 0\\
5 & 7 & 32 & 10 & 6 & 2 & 1\\
6 & 12 & 64 & 20 & 12 & 4 & 2\\
7 & 16 & 128 & 0 & 0 & 0 & 0\\
8 & 32 & 256 & 32 & 16 & 0 & 0\\
9 & 62 & 512 & 108 & 73 & 38 & 19\\
\end{array}$$
$$\text{来源（档案 ✓）}:\ n=4,5,6\ \text{← BRIDGE-2026-09-26}\ ✓;\ n=7,8\ \text{← CLOSE-}\ldots\text{-}n8\text{-zero-via-nearly-perfect}\ ✓;\ n=9\ \text{← C62-WILLE-RECOVERED}\ ✓$$
$$\textbf{逐行核算（本档 ✓）}:\ n=9\ \text{的 profile }(N_j)=\{1{:}432,2{:}62,3{:}8,4{:}10\}\ ✓\ \Longrightarrow\ \sum N_j=512=2^9\ ✓,\ \sum jN_j=620=62\cdot10\ ✓,\ \sum j(j-1)N_j=292\ ✓$$
$$\qquad\Longrightarrow\ Q=\tfrac12\cdot292-108=38\ ✓\ \text{—— 与档案 }Q_2=38\ \text{完全一致 ✓✓（归约式 (AD-1) 实证 ✓）}$$
$$\textbf{关键读数}:\ Q/2 = 0,\ 1,\ 2,\ 0,\ 0,\ 19\ (\text{按 }n=4..9\ ✓)\ \Longrightarrow\ \textbf{不存在低阶常数形态} ✗\ \text{（唐先生 → 允许 }n\text{-增长 ✓）}$$
$$
$$
```

---

## §2 归约的证明（**一行 ✓**）

```
$$2A_{\le2}=\sum_x\binom{b(x)}2=\sum_j\binom j2N_j=\tfrac12\sum_jj(j-1)N_j\ ✓\ \text{（按 }b\ \text{值分组 ✓）}$$
$$Q=2A_{\le2}-E=\tfrac12\sum_jj(j-1)N_j-E\ ✓\ \text{（用 }E=\sum_jjN_j-2^n=-\sum_j(1-j)N_j\ \text{的一阶钉死 ✓）}$$
$$\Longrightarrow\ \text{靶子}:\ \textbf{在 }M=K(n,1)\ \text{下证 }\tfrac12\sum_jj(j-1)N_j\ \text{的\textbf{上界}}\ ✓\ \text{（下界方向 }\lceil E/2\rceil\ \text{已耗尽 ✗）}$$
$$
$$
```

---

## §3 机制候选（**诚实排序 ✓；本档不宣称任一已成功 ✓**）

```
$$\text{(i) 最小性}:\ M=K\iff\text{最小覆盖 ⟺ 每个 }c\in C\ \text{有私有点}\ ✓\ \text{（档案 FAILSET ✓）};\ \text{但"private 总量＝profile 换皮" ✗ 已关闭 ✓}$$
$$\qquad\Longrightarrow\ \text{须用\textbf{逐码字}私有结构（非总量 ✓）—— 档案记 }I\ \text{依赖码字度数而非剖面 ⚠️（CHARGING ✓）}$$
$$\text{(ii) 双通道分离（本档建议的主攻 ✓）}:\ Q=Q_{\rm in}+Q_{\rm out}\ \text{分别上界 ⟹ }Q\ \text{上界 ✓}$$
$$\qquad Q_{\rm in}\ \text{侧}: \sum_{c}\binom{d_1(c)}2\ \text{—— 受"距离 }1\ \text{图的匹配性"型约束 ✓（档案已有 }d_1\le1\ \text{型定理 ✓，在 }Q=1\ \text{情形 ✓）}$$
$$\qquad Q_{\rm out}\ \text{侧}: \sum_{x\notin C}\binom{b(x)-1}2\ \text{—— 受"C-外点的局部分布"约束 ✓（需新机制 ⚠️）}$$
$$\text{(iii) 已验证的 }Q^*=0\ \text{族}:\ n\in\{2^m,2^m-1\}\ ✓\ \text{—— 用 nearly-perfect 分类（文献结构定理 ✓）⟹ 提示一般 }n\ \text{的机制应与"缺陷密度"}\ (E/2^n)\ \text{相关 ✓}$$
$$
$$
```

---

## §4 第一阶段结论（**不含经验拟合 ✓**）

```
$$\text{① 归约干净 ✓}:\ \text{靶子 ＝ profile 二阶阶乘矩的上界（}\textbf{不是} $A_{\le2}\le2$ ✗\ \text{—— 该形式已被 }n=5,6,9\ \text{击穿 ✓）}$$
$$\text{② 数据不支持低阶常数 ✓}:\ Q/2=0,1,2,0,0,19\ \Longrightarrow\ \text{形态必含 }n\text{-增长（或含 }E/2^n\text{ 型缺陷密度 ✓）}$$
$$\text{③ 已证部分}:\ n\in\{2^m,2^m-1\}\Longrightarrow Q^*=0\ ✓\ \text{（走 van Wee 取等 ＋ nearly-perfect 分类 ✓，非自证 P1 ✓）}$$
$$\text{④ 下一步（第二阶段）}:\ \text{攻 }\S3\text{(ii) 的 }Q_{\rm out}\ \text{上界}:\ \text{"}C\ \text{外点的 }b\ \text{分布"}\ \text{在 }M=K\ \text{下是否被约束} ⚠️$$
$$\qquad\textbf{若 }Q_{\rm out}\ \text{同样只给"总量＝剖面换皮" ⟹ 立即 STOP（AMEND-30/31 纪律 ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 数据为**档案引用 ＋ 本档核算** ✓（$n=9$ 行逐项验算 ✓）；§2 为**一行恒等** ✓；§3 为**候选机制**（未宣称成功 ✗）
- **未**主张任何经验公式为猜想定理 ✗（遵唐先生 ✓）；**未**改动 119 的 UNKNOWN 状态 ✓
- ⚠️ 勘误沿用 `LEDGER-2026-09-27` ✓：旧"$A_{\le2}\le2$"形式作废 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：(A) 第一阶段数据表、二阶阶乘矩归约、双通道主攻排序
- **档案已有（引用，不列为提出）**：BRIDGE、C62、CLOSE-n8、FAILSET、CHARGING、van Wee、nearly-perfect


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 二阶阶乘矩归约 命中文件数=1    :: ./ABOUND-2026-09-27-phase1-data-and-reduction.md 
技术词 双通道主攻  命中文件数=1    :: ./ABOUND-2026-09-27-phase1-data-and-reduction.md
```
- **本档新增**：(A) 第一阶段数据表、二阶阶乘矩归约、双通道主攻排序（见上方命中数；0 命中者为自造语／内部标签 ✓）
