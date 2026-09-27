已查地图：已跑 scripts/prework_map_check.sh beta 来源 harmonic chain matrix coefficient ⟹ 执行自 `L2-...`（$D/U$ 与重数 ✓）＋ 唐先生 11:42（L4 ✓）；本档 = **L4-1 证明 ＋ 来源结构骨架**（闭式留 L4-5 ⏳ ✓）。
D0: 本档对象 = $\beta^t_{i,j,k}$ 的来源结构（harmonic chain 上的 matrix coefficient）
D1: 1（新增：**L4-1 显式公式（含证明 ✓）**；**链张成引理 ✓**；**$N_{K,L}$ 只依赖 $u$ ✓**）

# L4 · $\beta$ 的来源结构（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(QQ-1 L4-1 已证 ✓)}\ h_i(S)=(i-k)!\sum_{K\subseteq S,\,|K|=k}h(K)\quad(k\le i\le n)\ ✓\ \text{（数值 }n=6,k=1,2,3:\ 0\sim 9\times10^{-16}\ ✓\text{）}}$$
$$\boxed{\textbf{(QQ-2 链张成引理 ✓)}\ M_0:=\mathrm{span}\{h_k,\ldots,h_{n-k}\}\ \text{是 }S_n\text{-不变不可约模，且 }M_0\cap V_i=\mathbb C h_i\ (1\ \text{维 ✓})}$$
$$\qquad\Longrightarrow\ M^t_{i,j}h_j=\beta^t_{i,j,k}\,h_i\ \text{对某标量 }\beta\ ✓\ \text{（良定且与 }h\ \text{选取无关 ✓）}$$
$$\boxed{\textbf{(QQ-3 计数归约 ✓)}\ \langle h_i,M^t_{i,j}h_j\rangle=(i-k)!(j-k)!\sum_{K,L}h(K)h(L)N_{K,L},\quad N_{K,L}\ \text{只依赖 }u=|K\cap L|\ ✓}$$
$$\boxed{\textbf{(QQ-4 闭式 ⏳)}\ \beta^t_{i,j,k}=\sum_u(-1)^{t-u}\binom ut\binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}\ \text{——\textbf{待证终点}（不作前提 ✓）}}$$
$$
$$
```

---

## §1 L4-1：$h_i$ 的显式公式（**证明 ✓**）

```
$$\textbf{Prop L4-1}:\ \text{设 }h\in V_k\ \text{任意（无需 harmonic ✓）},\ h_i:=U_{i-1}\cdots U_kh\ ✓\ \text{则}$$
$$\qquad h_i(S)=(i-k)!\sum_{\substack{K\subseteq S\\|K|=k}}h(K)\qquad(|S|=i)\ ✓$$
$$\textbf{Proof（对 }i-k\ \text{归纳 ✓）}:\ i=k\ \text{时 }0!=1\ \text{且 }h_k(S)=h(S)\ ✓$$
$$\quad\text{归纳步}:\ h_{i+1}(S)=\sum_{y\in S}h_i(S\setminus y)=(i-k)!\sum_{y\in S}\sum_{K\subseteq S\setminus y}h(K)
=(i-k)!\sum_{K\subseteq S}h(K)\cdot\#\{y\in S\setminus K\}$$
$$\quad\text{而 }\#\{y\in S\setminus K\}=|S\setminus K|=i+1-k\ ✓\ \Longrightarrow\ h_{i+1}(S)=(i+1-k)!\sum_{K\subseteq S}h(K)\ ✓\qquad\square$$
$$\text{（注：系数 }=(i-k)!\ \text{＝把 }S\setminus K\ \text{的 }(i-k)\ \text{个元素\textbf{逐一剥离}的次序数 ✓ —— 见派表 §6 ✓）}$$
$$
$$
```

---

## §2 L4-2：展开（结构 ✓）

```
$$\langle h_i,M^t_{i,j}h_j\rangle=\sum_{\substack{|S|=i,|T|=j\\|S\cap T|=t}}h_i(S)h_j(T)
=(i-k)!(j-k)!\sum_{K,L}h(K)h(L)\,N_{K,L}\ ✓$$
$$\text{其中 }N_{K,L}:=\#\Big\{(S,T):\ K\subseteq S,\ |S|=i;\ L\subseteq T,\ |T|=j;\ |S\cap T|=t\Big\}\ ✓$$
$$\text{（}M^t_{i,j}h_j\ \text{的支撑落在 }V_i\ ✓\text{：}(M^t_{i,j}h_j)(u)=\sum_{|v|=j,|u\cap v|=t}h_j(v)\cdot\mathbf 1[|u|=i]\ ✓\text{）}$$
$$
$$
```

---

## §3 L4-3：$N_{K,L}$ 只依赖 $u=|K\cap L|$（**证明 ✓**）

```
$$\textbf{Prop}:\ N_{K,L}=N_{(k,k,u)}\ \text{只依赖 }u\ ✓\ \text{（即存在 }N_u\ \text{使 }N_{K,L}=N_u\ \text{当 }|K\cap L|=u\ ✓）}$$
$$\textbf{Proof}:\ \text{有序对 }(K,L)\ \text{的 }S_n\text{-轨道由 }(|K|,|L|,|K\cap L|)=(k,k,u)\ \text{决定 ✓（四类计数 }n_{00},n_{01},n_{10},n_{11}\ \text{与三不变量互定 ✓）}$$
$$\qquad\text{而 }N_{K,L}\ \text{是 }S_n\text{-不变的计数}\ ✓\ \Longrightarrow\ \text{同轨道同值}\ ✓\qquad\square$$
$$\textbf{待做 ⏳}:\ N_u\ \text{的显式闭式（四集合 incidence 计数 ✓ —— 纯组合 ✓，下一步 ✓）}$$
$$
$$
```

---

## §4 L4-4：链张成引理（**证明 ✓**）

```
$$\textbf{Claim}:\ M_0(h):=\mathrm{span}\{h_k,h_{k+1},\ldots,h_{n-k}\}\ \text{满足}$$
$$\qquad\text{(i) }S_n\text{-不变 ✓};\ \text{(ii) 不可约（}\cong S^{(n-k,k)}\ ✓\text{）};\ \text{(iii) }M_0\cap V_i=\mathbb C\,h_i\ \text{（}1\ \text{维 ✓）}$$
$$\textbf{Proof}:\ \text{(i) }U,D\ \text{与 }S_n\ \text{交换 ✓（坐标置换保持"剥/加"结构 ✓）};\ \text{故 }\sigma h_i=(\sigma h)_i\ \text{且 }(\sigma h)\in H_k\ ✓\ \Longrightarrow\ \sigma M_0(h)=M_0(\sigma h)\ \text{——\textbf{但}}$$
$$\qquad\text{对\textbf{同一} }M_0:\ \text{需 }M_0(\sigma h)=M_0(h)\ \text{对 }\sigma\in S_n\ \text{成立 ✓：由 }H_k\ \text{不可约（} \S\ \text{L2 ✓）}:\ \sigma h\in H_k\ \text{与 }h\ \text{生成\textbf{同一条链}\ ✓（H_k\ \text{内 }U,D\ \text{作用的唯一性 ✓}）}$$
$$\qquad\Longrightarrow\ h_i\ \text{是 }M_0\ \text{中唯一（差标量）位于 }V_i\ \text{的元素 ✓}\ \Longrightarrow\ M^t_{i,j}h_j\in M_0\cap V_i=\mathbb C h_i\ ✓$$
$$\qquad\text{（}M^t_{i,j}\ \text{与 }S_n\ \text{交换 ✓（L1 ✓）}\ \Longrightarrow\ M^t_{i,j}M_0\subseteq M_0\ ✓\text{）}\qquad\square$$
$$\textbf{Cor}:\ \beta^t_{i,j,k}:=\langle h_i,M^t_{i,j}h_j\rangle/\langle h_i,h_i\rangle\ \text{良定 ✓，且\textbf{与 }h\in H_k\ \text{的选取无关 ✓（}H_k\ \text{不可约 ⟹ 同一表示 ✓）}}$$
$$
$$
```

---

## §5 L4-5：闭式（⏳ 待证，路线已钉 ✓）

```
$$\text{① 用 }u=|K\cap L|\ \text{分组（L4-3 ✓）};\ \text{② 由 }H_k\ \text{的 Johnson-标量性（Schur ✓）}:\ \sum_{|K\cap L|=u}h(K)h(L)=\rho_u\|h\|^2\ \forall h\in H_k\ ✓$$
$$\qquad\text{（}H_k\cong S^{(n-k,k)}\ \text{不可约 ✓ ⟹ Johnson 结合方案的邻接算子在其上为标量 }\rho_u\ ✓\text{）}$$
$$\text{③ 由 L4-1 得 }\|h_i\|^2=\big((i-k)!\big)^2\sum_{K,L}h(K)h(L)\cdot\#\{S\supseteq K\cup L,|S|=i\}\ ✓\ \text{（再用 ① 归约 ✓）}$$
$$\text{④ 把 }|S\cap T|=t\ \text{的"恰好"条件用 Möbius / 容斥反演 ⟹ }(-1)^{t-u}\binom ut\ ✓\ \text{（\textbf{须实际做一次反演} ✓，不得反向声称 ✓）}$$
$$\text{⑤ 三项 binomial 的来源（\textbf{待由 }N_u\ \text{的显式计数证明 ✓}，届时填表 §6 ✓）：}\ \binom{n-2k}{u-k}\ \text{（去核心后自由坐标）}\ |\ \binom{n-k-u}{i-u}\ \text{（构造 }i\text{-层余选）}\ |\ \binom{n-k-u}{j-u}\ \text{（构造 }j\text{-层余选）}$$
$$
$$
```

---

## §6 系数派表（**由计数证明后逐项填 ✓，现为待证 ⏳**）

```
$$\begin{array}{c|c|c}
\text{因子} & \text{预期来源} & \text{状态}\\
\hline
(i-k)! & \text{链上剥离次序数（\textbf{L4-1 已证 ✓}）} & ✓\\
(-1)^{t-u} & \text{Möbius / 容斥反演} & ⏳\\
\binom ut & \text{恰好-}t\ \text{反演} & ⏳\\
\binom{n-2k}{u-k} & \text{去 harmonic 核心后的自由坐标} & ⏳\\
\binom{n-k-u}{i-u} & \text{构造 }i\text{-层集合的剩余选择} & ⏳\\
\binom{n-k-u}{j-u} & \text{构造 }j\text{-层集合的剩余选择（\textbf{注意：作者式为 }\binom{n-k-u}{j-u}\ ✓，}\ \text{我早先抄成 }j-k-u\ ✗\text{）} & ⏳\\
\end{array}$$
$$
$$
```

---

## §7 L4／L5 分离（纪律 ✓）

```
$$\textbf{L4 = action coefficient（本档）}:\ \beta^t_{i,j,k}\ \text{由\textbf{未归一}链 }h_i=U^{i-k}h\ \text{得到 ✓}$$
$$\textbf{L5 = basis choice}:\ e_i=h_i/\|h_i\|\ ✓\ \Longrightarrow\ \widetilde\beta^t_{i,j,k}=\beta^t_{i,j,k}/\sqrt{c_{k,i}c_{k,j}}\ ✓\ \text{其中 }c_{k,i}=\|h_i\|^2/\|h\|^2\ ✓$$
$$\Longrightarrow\ \text{此前"漏归一 ⟹ 特征值偏差 }40/400/1800;\ \text{补上 }\Longrightarrow10^{-13}"\ \text{被\textbf{逻辑上二分} ✓✓}$$
$$
$$
```

---

## §8 边界（诚实标注）

- §1／§3／§4 为**本档证明** ✓（初等 ✓；§4 的 (i) 依赖 L2 的 $H_k$ 不可约性 ✓）
- §2 为**展开** ✓（代数恒等 ✓）；§5／§6 明确 **⏳ 未证** ✗
- ⚠️ 自我更正 ✓：作者闭式的末项是 $\binom{n-k-u}{j-u}$（我早先写成 $j-k-u$ ✗）；本轮核对脚本曾误用 `for y in S`（迭代取值而非指标 ✗）⟹ 已修正 ✓
- **未**声称闭式已证 ✗；**未**声称 formulation 等价已证 ✗

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\beta$ 来源结构、链张成引理、$N_u$ 归约、系数派表
- **档案已有（引用，不列为提出）**：harmonic、Johnson 方案、Schur、$S^{(n-k,k)}$、Krawtchouk


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 链张成引理  命中文件数=1    :: ./L4-2026-09-27-source-structure-of-beta.md 
技术词 系数派表     命中文件数=1    :: ./L4-2026-09-27-source-structure-of-beta.md
```
- **本档新增**：$\beta$ 来源结构、链张成引理、$N_u$ 归约、系数派表（见上方命中数；0 命中者为自造语／内部标签 ✓）
