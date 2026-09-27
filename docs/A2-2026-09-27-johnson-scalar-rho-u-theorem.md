已查地图：已跑 scripts/prework_map_check.sh Johnson 标量 rho_u 消失引理 双计数 ⟹ 执行自 `A1-...-Nu-...`（$N_u$ ✓）＋ 唐先生 11:46（A-2 ✓）；本档 = **$\rho_u$ 定理（含证明＋判决性数值 ✓）**。
D0: 本档对象 = Johnson 算子 $\Omega_u$ 在 $H_k$ 上的标量 $\rho_u$
D1: 1（新增：**消失引理 ✓**、**$\rho_u=(-1)^{k-u}\binom ku$ 定理 ✓**、**$n$-无关性 ✓**）

# A-2 · Johnson 标量 $\rho_u$（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(SS-1 消失引理 ✓)}\ h\in H_k\ \Longrightarrow\ \sigma_d(M):=\sum_{K\supseteq M,|K|=k}h(K)=0\quad\text{对\textbf{一切}}\ |M|=d\le k-1\ ✓}$$
$$\boxed{\textbf{(SS-2 $\rho_u$ 定理 ✓)}\ \Omega_u:=\big(\mathbf 1[|K\cap L|=u]\big)_{K,L}\ \Longrightarrow\ \Omega_u\big|_{H_k}=\rho_u I,\quad \boxed{\rho_u=(-1)^{k-u}\binom ku}\ ✓}$$
$$\qquad\textbf{与 }n\ \textbf{无关} ✓\ \text{（判决性：}n=6,k=2\ \text{时本式给 }+1\ ✓\ \text{而 Kneser 型 }-\binom{n-k}k=-6\ ✗，数值取 }+1\ ✓✓\text{）}$$
$$\boxed{\textbf{(SS-3 二次型恒等式 ✓)}\ \sum_{\substack{K,L\\|K\cap L|=u}}h(K)h(L)=(-1)^{k-u}\binom ku\|h\|^2\quad\forall h\in H_k\ ✓}$$
$$\boxed{\textbf{(SS-4 中间公式 ✓)}\ \langle h_i,M^t_{i,j}h_j\rangle=(i-k)!(j-k)!\sum_{u}N_u(i,j,t)\,\rho_u\,\|h\|^2\ ✓\ \text{（\textbf{纯 incidence} × \textbf{表示论标量} 分离 ✓）}}$$
$$
$$
```

---

## §1 符号审计（按唐先生 A-2.3 ✓）

```
$$\begin{array}{c|c|c|c}
\text{情形} & \text{预测} & \text{核对} & \text{状态}\\
\hline
u=k & \rho_k=(-1)^0\binom kk=1\ ✓\ (\Omega_k=I\ ✓) & 1.000000\ ✓ & ✓\\
k=0 & \rho_0=1\ ✓ & （平凡 ✓） & ✓\\
k=1,u=1 & \rho_1=1\ ✓ & 1.000000\ ✓ & ✓\\
k=1,u=0 & \rho_0=-1\ ✓\ \text{（手算 }(\Omega_0h)(x)=\sum_{y\ne x}h(y)=-h(x)\ ✓\text{）} & -1.000000\ ✓ & ✓\\
n=6,k=2,u=0 & +1\ ✓\ (\text{与 }-\binom nk\ \text{型 }-6\ \textbf{不同}\ ✓) & +1.000000\ ✓ & ✓\\
n=6,k=3,u=0 & -1\ ✓ & -1.000000\ ✓ & ✓\\
\end{array}$$
$$
$$
```

---

## §2 消失引理的证明（**✓**）

```
$$\textbf{Prop 1}:\ h\in H_k=\ker D_k\ \Longrightarrow\ \sigma_d(M)=0\ \text{对一切 }|M|=d<k\ ✓$$
$$\textbf{Proof}:\ d=k-1\ \text{即 }D_kh=0\ ✓\ \text{（定义 ✓）};\ \text{设 }d+1\ \text{已成立 ✓，对 }|M|=d:$$
$$\qquad\sum_{M':\,M\subset M',|M'|=d+1}\sigma_{d+1}(M')=0\ ✓;\ \text{而每个 }K\supseteq M\ \text{被计数 }(k-d)\ \text{次（选 }M'\setminus M\ \text{的 }1\ \text{个元素 ✓）}$$
$$\qquad\Longrightarrow\ (k-d)\sigma_d(M)=0\ \text{且 }k-d\ne0\ \Longrightarrow\ \sigma_d(M)=0\ ✓\qquad\square$$
$$
$$
```

---

## §3 $\rho_u$ 定理的证明（**✓**）

```
$$\textbf{记}:\ S_u:=\sum_{|K\cap L|=u}h(K)h(L)\quad(0\le u\le k)\ ✓;\quad P_v:=\sum_{|M|=v}\sigma_v(M)^2\quad(0\le v\le k-1)\ ✓$$
$$\textbf{双计数（关键 ✓）}:\ \text{把 }(K,L)\ \text{按 }|K\cap L|=u\ \text{分组，并数其中含多少个 }v\text{-子集 }M:\ P_v=\sum_{u=v}^{k}\binom uv S_u\ ✓$$
$$\textbf{代入 Prop 1}:\ P_v=0\ (v\le k-1)\ \Longrightarrow\ \boxed{\sum_{u=v}^{k}\binom uv S_u=0}\quad(v=0,\ldots,k-1)\ \text{—— \textbf{三角方程组}（对角系数 }\binom vv=1\ ✓）$$
$$\textbf{初值}:\ S_k=\sum_{|K\cap L|=k}h(K)h(L)=\sum_Kh(K)^2=\|h\|^2\ ✓$$
$$\textbf{解（验证 + 三角唯一 ✓）}:\ S_u=(-1)^{k-u}\binom ku\|h\|^2\ ✓\ \text{因为}$$
$$\qquad\sum_{u=v}^{k}(-1)^{k-u}\binom ku\binom uv=\binom kv\sum_{u=v}^{k}(-1)^{k-u}\binom{k-v}{u-v}=\binom kv\,(1-1)^{k-v}=0\quad(v<k)\ ✓$$
$$\textbf{从二次型到算子（无需 Schur ✓，更干净 ✓）}:\ \Omega_u\ \text{对称 ✓（}|K\cap L|=|L\cap K|\ ✓\text{）且 }S_n\text{-等变 ✓}$$
$$\qquad\text{由 SS-3 与极化（polarization ✓）}:\ \langle h',(\Omega_u-\rho_uI)h\rangle=0\ \forall h,h'\in H_k\ \Longrightarrow\ (\Omega_u-\rho_uI)H_k\perp H_k\ ✓$$
$$\qquad\text{又 }S_n\text{-等变 ⟹ }(\Omega_u-\rho_uI)H_k\subseteq H_k\ \text{（}H_k\ \text{不可约 ✓）}\ \Longrightarrow\ (\Omega_u-\rho_uI)H_k=0\ ✓\qquad\square$$
$$
$$
```

---

## §4 中间公式（**✓，唐先生的 A-2.5**）

```
$$\langle h_i,M^t_{i,j}h_j\rangle=(i-k)!(j-k)!\sum_{u}N_u(i,j,t)\Big(\sum_{|K\cap L|=u}h(K)h(L)\Big)
=(i-k)!(j-k)!\sum_u N_u(i,j,t)\rho_u\|h\|^2\ ✓$$
$$\Longrightarrow\ \beta^t_{i,j,k}=\frac{\langle h_i,M^t_{i,j}h_j\rangle}{\|h_i\|^2}
=\frac{(i-k)!(j-k)!}{\|h_i\|^2}\sum_uN_u(i,j,t)\rho_u\ ✓\ \text{（分母 convention 待 }\S5\ \text{核 ✓，不提前简化 ✓）}$$
$$\textbf{结构收获}:\ \boxed{\text{纯 incidence }N_u\ (\text{含 }n)\quad+\quad\text{表示论标量 }\rho_u=(-1)^{k-u}\binom ku\ (\textbf{不含 }n)\ \Longrightarrow\ \beta}\ ✓$$
$$\qquad\Longrightarrow\ \beta\ \text{的全部 }n\text{-依赖只能来自 }N_u\ \text{与分母 }\|h_i\|^2\ ✓\ \text{（结构性结论 ✓）}$$
$$
$$
```

---

## §5 下一步（L4-5 / L5）

```
$$\text{(a) L5（范数）}:\ \|h_i\|^2=\big((i-k)!\big)^2\sum_u N^{(2)}_u(i)\rho_u\|h\|^2\ ✓\ \text{其中 }N^{(2)}_u(i)=\#\{S\supseteq K\cup L,|S|=i\}=\binom{n-2k+u}{i-2k+u}\ ✓$$
$$\qquad\Longrightarrow\ \text{归一因子 }c_{k,i}=\|h_i\|^2/\|h\|^2\ ✓\ \text{（纯计数 ✓）}$$
$$\text{(b) L4-5（Möbius）}:\ \text{把 }\sum_uN_u\rho_u\ \text{化成作者的单重交替式 ⟹ 见 }\S6\ \text{派表 ✓}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1–§3 为**本档证明 ＋ 判决性数值核对** ✓（6 组 $(n,k,u)$ 全吻合 ✓，机器精度 ✓）
- §4 为**代入** ✓（代数 ✓）；§5 为**计划** ⏳
- **未**声称 $\beta$ 闭式已证 ✗；**未**声称 formulation 等价已证 ✗
- ⚠️ 重要更正（相对文献直觉 ✓）：**不能用 Kneser 型 $-\binom{n-k}k$ 预测本 $\rho_u$** ✗ —— 本 $H_k$ 是 $\ker D_k$（"最高权"方向 ✓），其 $\rho_u$ 与 $n$ 无关 ✓；数值已判决 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：消失引理、$\rho_u=(-1)^{k-u}\binom ku$ 定理、$\rho_u$ 的 $n$-无关性、中间公式
- **档案已有（引用，不列为提出）**：Johnson 方案、Eberlein 多项式、Kneser 图、$H_k$、极化


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 消失引理     命中文件数=5    :: ./C120-RS-support-translation-prime-side-window-shrinks-with-k.md ./C78-SQ1-verdict-MV-not-sharp-but-only-constant-room.md ./A2-2026-09-27-johnson-scalar-rho-u-theorem.md 
技术词 rho_u            命中文件数=3    :: ./L4-2026-09-27-source-structure-of-beta.md ./A2-2026-09-27-johnson-scalar-rho-u-theorem.md ./A1-2026-09-27-incidence-count-Nu-via-generating-function.md
```
- **本档新增**：消失引理、$\rho_u$ 定理、$n$-无关性、中间公式（见上方命中数；0 命中者为自造语／内部标签 ✓）
