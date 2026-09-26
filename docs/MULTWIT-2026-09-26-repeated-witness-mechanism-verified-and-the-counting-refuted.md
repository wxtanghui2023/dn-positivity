已查地图：已跑 scripts/prework_map_check.sh 重复见证 纤维 计数 L□ <= S+I_nw ⟹ 执行自 SHELLWIT-2026-09-26 档；本档为**重复见证机制验证＋计数式否证**（唐先生 2026-09-26 16:06 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 重复见证 ⟹ owner 在 ≥2 方阵 ⟹ d_C ≥ 3 的机制、L□ ≤ S+I_nw 的否证、加权替代
D1: 1（新增：**重复见证机制（已证＋实测）** ✓✓；**L□ ≤ S+I_nw 被否** ✗✓；**加权版成立** ⚠️）

# MULTWIT-2026-09-26

## §1 ⭐ **机制成立（已证 ＋ 实测 ✓✓）**

```
$$\Phi(Q,v,y)\ \text{的纤维}>1\ \Longrightarrow\ \text{同一 }v\ \text{有两个方阵 }Q,Q'\ \text{都使 }y\in\mathrm{Sh}(v)\ ✓$$
$$\Longrightarrow\ v\in Q\cap Q'\ ✓\ \text{且 }k\notin\mathrm{dirs}(Q)\cup\mathrm{dirs}(Q')$$
$$\text{方阵方向对}\ \mathrm{dirs}(Q)\ne\mathrm{dirs}(Q')\ ✓\ (\text{否则同一方阵}\ ✗)\ \Longrightarrow\ \text{并集}\ \ge3\ \Longrightarrow\ \boxed{d_C(v)\ \ge\ 3}\ ✓✓$$
$$\Longrightarrow\ v\ \text{对 }I\ \text{贡献}\ \binom{d_C(v)}2\ \ge\ 3\ \text{而基线 }|V_\square|\ \text{只计 }1\ \Longrightarrow\ \textbf{超出}\ \ge2\ \text{个 }I\ \text{单位}\ ✓✓$$
$$\textbf{实测}: n=4,M=7:\ v\in0000,0001\ \text{各在 2 方阵}\ ✓,\ d_C(v)=3\ \checkmark;\quad n=4,M=8:\ v\ \text{在 3 方阵},\ d_C=3\ \checkmark$$
$$

## §2 ⛔ **但计数式 `L□ ≤ S + I_nw` 被否** ✗✓（决定性反例 ✓）

```
$$\begin{array}{c|c|c|c|c|c|c}
\text{实例} & S_q & L_\square & S & I_{\rm nw} & S+I_{\rm nw} & L_\square\le S+I_{\rm nw}\\
\hline
n=4\ M=6 & 1 & 5 & 4 & 2 & 6 & \checkmark\\
n=4\ M=7 & 2 & 10 & 6 & 4 & 10 & \checkmark\ (\text{紧}\ ✓)\\
\mathbf{n=4\ M=8} & 6 & \mathbf{24} & 0 & 16 & 16 & \mathbf{\✗\ 违反}\ ✗✓\\
(5,8) & 1 & 3 & 12 & 0 & 12 & \checkmark\\
(4,6) & 1 & 5 & 4 & 2 & 6 & \checkmark\\
(9,64) & 16 & 0 & 0 & 0 & 0 & \checkmark\ (\text{零缺陷}\ ✓)\\
\end{array}$$
$$\textbf{根因}: \text{一个 incidence} \mapsto \text{一个 }I\ \text{单位\textbf{不成立}}\ ✗\ ——\ \text{顶点 }v\ \text{的超出量被 }\binom{d_C(v)}2-1\ \text{封顶},\ \text{而它可承载\textbf{许多}非 private incidence}\ ✗✓$$
$$

## §3 ⚠️ **加权替代（成立但更弱）**

```
$$\text{实测}: L_\square\ \le\ (n-2)(S+I_{\rm nw})\ ✓\ \text{在全部 6 个实例通过}\ ⚠️\ (\text{含 }n{=}4,M{=}8:\ 24\le2\cdot16=32\ ✓)$$
$$\text{但这是弱化版}\ ✗;\ \text{正确规范化应使用\textbf{每顶点的 shell incidence 并集}（distinct 非 private shell 点）},\ \text{而非逐方阵求和}\ ✓$$
```

## §4 状态与下一刀

```
$$\textbf{机制已立}\ ✓✓;\ \textbf{朴素计数式已否}\ ✗✓;\ \text{正确计数尚未找到}\ ✗$$
$$\text{下一刀}: \text{对每个顶点 }v:\ \text{令 }U(v):=\bigcup_{Q\ni v}\mathrm{Sh}_Q(v)\ \text{（并集而非求和}\ ✓);\ \text{则 }|U(v)|\ \text{才有干净容量意义}\ ✓$$
$$\qquad\text{待验}: \#\{U(v)\ \text{中非 private 点}\}\ \le\ \binom{d_C(v)}2-1+\text{(v 的 }S\text{-见证数)}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad (9,62)\ \text{全码}: \text{仍未获得}\ ✗$$
$$

## §5 边界（诚实标注）

- §1 为**我方证明＋实测** ✓✓；§2 为**决定性反例** ✗✓（未掩盖 ✓）；§3 为**弱化版实测** ⚠️（不升级为猜想 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：重复见证机制、纤维计数、并集容量
- **档案已有（引用，不列为提出）**：shell、见证、方阵、I_nw
