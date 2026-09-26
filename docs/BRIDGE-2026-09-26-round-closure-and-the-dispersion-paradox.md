已查地图：已跑 scripts/prework_map_check.sh A≤2 桥 最小性 分散 ⟹ 执行自 PHI-2026-09-26 档；本档为**本轮收口 ＋ 桥的方向锐化**（唐先生 2026-09-26 12:58 指令）；纯整理＋引用既有实算，未跑 solver ✓。
D0: 本档对象 = A≤2 桥的锐化形式与其方向经验读数
D1: 1（新增：**"最小性阻止超额完全分散"**的经验读数 ✓；桥的等价锐化形式 ✓）

# BRIDGE-2026-09-26

## §1 本轮收口（台账固定 ✓）

```
$$\boxed{\text{Shadow}=NO\text{-}GO\ ✓,\qquad \Phi=\text{局部资产，不作路线}\ ✓}$$
$$\textbf{极值特异存活}: Q,\ A_{\le2},\ N_1,\ \text{剖面 }(N_j)\ ✓$$
$$\textbf{可复用局部资产}: \text{私有点引理}\ (L(c)=r(c)\ge1)\ ✓;\ \text{奇偶引理＋P1}\ ✓;\ \Phi=A_1+A_2\ ✓\ (\text{capacity defect ＋ coverage defect}\ ✓)$$
$$\textbf{其余路线全部隔离}\ ✓;\ \textbf{119 保持 UNKNOWN}\ ✓$$
$$

## §2 桥的**等价锐化形式**（把"求 A≤2"改成"求上界" ✓）

```
$$\text{恒等式}: Q=2A_{\le2}-E\ ✓;\quad A_{\le2}=\frac{\sum_x b(x)(b(x)-1)}{4}\ ✓$$
$$\text{已知下界}: A_{\le2}\ \ge\ \Bigl\lceil\frac E2\Bigr\rceil\ ✓\ (\text{来自 }Q\ge0\ ✓,\ \text{即 LP 界}\ ✓)$$
$$\text{但在 }M=K\ \text{处真值更大}\ ✗:$$
$$\qquad n=4:\ E/2=2,\ A_{\le2}=2\ ✓\ (\text{紧}\ ✓);\quad n=5:\ E/2=5,\ A_{\le2}=6\ ✗;\quad n=6:\ E/2=10,\ A_{\le2}=12\ ✗$$
$$\boxed{\Longrightarrow\ \text{桥}\ \equiv\ \textbf{在 }M=K\ \text{处 }Q\ \text{的上界}\ ✗\ (\text{等价地 }A_{\le2}\ \text{的上界}\ ✓)\ ——\ \text{下界方向已耗尽}\ ✗}$$
$$

## §3 ⭐ **反直觉读数：最小性"阻止"超额完全分散** ✓✓（本档头条）

```
$$\text{超额可"完全分散"}\iff Q=0\iff \text{全部 }b(x)\le2\ ✓$$
$$\begin{array}{c|c|c}
(n,M) & \text{是否有 }Q=0\ \text{的覆盖码} & \text{来源}\\
\hline
(5,7)=\mathbf K & \textbf{无}\ ✗\ (\text{全部 }320\ \text{个 }Q=2\ ✓) & \text{我方全枚举}\ ✓\\
(5,8)=K{+}1 & \textbf{有}\ ✓\ (603/8866\ ✓) & \text{我方全枚举}\ ✓\\
(4,4)=K & \text{有}\ ✓\ (40/40,\ Q=0\ ✓) & \text{完全分散可行}\ ✓\\
(4,5),(4,6) & \text{无}\ ✗\ (\text{奇偶禁 }\ ✓) & \text{parity}\ ✓\\
(n=6,12)=K & \text{无}\ ✗\ (Q=4\ \text{全部}\ ✓) & \text{采样}\ ✓\\
\end{array}$$
$$\boxed{\text{最小 }M\ \text{处超额\textbf{不能}完全分散；增大 }M\ \text{反而\textbf{可以}}\ ✓✓\ (\text{与"极值}\Rightarrow\text{更平坦"的直觉相反}\ ✗)}$$
$$\textbf{意义}: \text{桥的方向不是"证明 }M=K\ \text{时更平坦"}\ ✗,\ \text{而是 \textbf{"证明最小性迫使一定程度的聚集"}}\ ✓$$
$$

## §4 ⚠️ 线性外推警戒（本轮自我约束 ✓）

```
$$\text{数据点 }Q^*(4)=0,\ Q^*(5)=2,\ Q^*(6)=4\ \text{恰好落在直线 }Q=2(n-4)\ \text{上}\ ✓$$
$$\text{但}: Q^*(7)=0\ ✗,\ Q^*(8)=0\ ✗\ (\text{两者都\textbf{破坏}该直线}\ ✓✓)$$
$$\Longrightarrow\ \textbf{禁止}把 }Q=2(n-4)\ \text{当作公式}\ ✗\ (\text{三点拟合是陷阱}\ ✓;\ n=7,8\ \text{即为反例}\ ✓)$$
$$

## §5 下一步（桥的独立必要条件，按可执行性排序 ✓）

```
$$\text{① \textbf{证"}M=K\Rightarrow Q\ge1"\ \text{的普遍性}（= C1 开放半边）\ ✓:\ \text{已知 }P1\ \text{覆盖偶 }n\ \text{且 }K\ \text{奇的情形}\ ✓;\ \text{其余待补}\ ✗$$
$$\text{② \textbf{求 }Q\ \text{上界的几何来源}}: \text{用"球内聚集"}\ ⟹\ hmm\ (\text{注意}: b(x)=m\ \text{时 }m\ \text{个码字两两距离}\le2\ ✓\ \text{形成 }G_2\ \text{团}\ ✓)$$
$$\text{③ **局部-全局接口**}: \text{把 }\Phi\ \text{的 capacity/coverage 二缺陷观（\text{已有}\ ✓）\ \text{与 }Q\ \text{的上界需求对接}\ ✗\ (\text{尚未}\ ✗)$$
$$\text{④ 纪律}: \text{不跑 }n=9\ \text{盲跑}\ ✗;\ \textbf{119 保持 UNKNOWN}\ ✓$$
$$

## §6 边界（诚实标注）

- §2 的恒等式为**既有档案** ✓（2026-09-25/26 ✓）；§3 的数据为**我方全枚举/采样** ✓
- §4 的警戒为**我方自我约束** ✓（明确禁止三点外推 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 最小性阻止分散 命中文件数=0    :: 
技术词 超额分散     命中文件数=0    :: 
技术词 桥的锐化形式 命中文件数=0    :: 
技术词 线性外推警戒 命中文件数=0    ::
```

- **本档新增**（命中数=0）：最小性阻止分散、超额分散、桥的锐化形式、线性外推警戒
- **档案已有（引用，不列为提出）**：—
