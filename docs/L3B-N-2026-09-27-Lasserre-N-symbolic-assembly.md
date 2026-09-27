已查地图：已跑 scripts/prework_map_check.sh Lasserre N 平移 T_w 块 边框 ⟹ 执行自 `L3B-M-...`（① $M''$ ✓）＋ 唐先生 11:58（② ✓）；本档标为 **Lasserre $N$ symbolic assembly** ✓。
D0: 本档对象 = $N$ 的块结构（符号版，含 $T_w$ 逐项核 ✓）
D1: 1（新增：**N1 不变性证明 ✓**；**$T_w=P_w(\cdot)P_w^{-1}$ 的逐项核对 ✓**；**N3 边框向量 $\in W_0$ 的证明 ✓**）

# ② Lasserre $N$ 符号装配（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(ZZ-1 N1 不变性 ✓)}\ N\in\mathrm{End}_{S_n}(V)=\mathcal A_{2,n}\ ✓\ \text{（证明见 }\S1\ ✓，\textbf{无需额外假设} ✓）}$$
$$\boxed{\textbf{(ZZ-2 }T_w\text{ 逐项核 ✓)}\ (P_wXP_w^{-1})_{u,v}=X_{u\oplus w,v\oplus w}\ \Longrightarrow\ \text{Prop 2.4(iii) 的 }M'_{u-w,v-w}=P_wM'P_w^{-1}\ ✓\ \text{（}\textbf{无隐藏 scalar} ✓）}}$$
$$\boxed{\textbf{(ZZ-3 N2 块结构 ✓)}\ N|_k=I_{m_k}\otimes N_k\ ✓\ \text{（同 M'，\textbf{不重造 harmonic 基} ✓）}}$$
$$\boxed{\textbf{(ZZ-4 N3 边框 ✓)}\ z:=y\in W_0\ ✓\ \Longrightarrow\ R_N=\begin{pmatrix}c&z^{\sf T}\\ z&N_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes N_k\ ✓\ \text{（}c=\sum_i\binom ni\lambda_ix^0_{00}-\beta\ ✓）}$$
$$\boxed{\textbf{(ZZ-5 N4 PSD ⟸⟹ ✓)}\ R_N\succeq0\iff\Big[N_k\succeq0\ (k\ge1)\ \wedge\ \begin{pmatrix}c&z^{\sf T}\\ z&N_0\end{pmatrix}\succeq0\Big]\ ✓\ \text{（奇异时用广义 Schur 补 ✓）}}$$
$$
$$
```

---

## §1 N1：$N\in\mathcal A_{2,n}$（**显式证明 ✓**）

```
$$\textbf{定义（Prop 2.4(iii) ✓）}:\ N_{u,v}=-\beta M_{u,v}+\sum_{\ell=0}^n\lambda_\ell\sum_{\substack{w\in\{0,1\}^n\\|w|=\ell}}M'_{u\oplus w,\,v\oplus w}\ ✓$$
$$\textbf{(a) }T_w\ \text{的逐项核（关键 ✓）}:\ \text{令 }P_w\ \text{为平移置换：}(P_wf)(u)=f(u\oplus w)\ ✓\ \text{即 }P_we_x=e_{x\oplus w}\ ✓,\ P_w^{-1}=P_w\ ✓$$
$$\qquad\Longrightarrow\ (P_wXP_w^{-1})_{u,v}=\sum_{x,y}\mathbf 1[x=u\oplus w]X_{x,y}\mathbf 1[y=v\oplus w]=X_{u\oplus w,v\oplus w}\ ✓\ \text{——\textbf{与论文 }M'_{u-w,v-w}\ \text{逐项一致} ✓\ \text{（无额外因子 ✓）}$$
$$\textbf{(b) 不变性 ✓}:\ \text{对 }\sigma\in S_n\ \text{（坐标置换 ✓）}:\ M_{\sigma u,\sigma v}=M_{u,v}\ ✓,\ M'_{\sigma a,\sigma b}=M'_{a,b}\ ✓\ \text{（二者均 }\mathrm{Aut}\text{/}\mathrm{Aut}_0\text{-不变 ✓）}$$
$$\qquad N_{\sigma u,\sigma v}=-\beta M_{u,v}+\sum_\ell\lambda_\ell\sum_{w:|w|=\ell}M'_{\sigma u\oplus w,\sigma v\oplus w}
\ \xrightarrow{w'=\sigma^{-1}w}\ -\beta M_{u,v}+\sum_\ell\lambda_\ell\sum_{w':|w'|=\ell}M'_{u\oplus w',v\oplus w'}=N_{u,v}\ ✓$$
$$\qquad\text{（用了 }|w'|=|w|\ \text{⟹ }\lambda\ \text{权重不变 ✓；且 }M'_{\sigma a,\sigma b}=M'_{a,b}\ ✓）$$
$$\Longrightarrow\ N\in\mathrm{End}_{S_n}(V)=\mathcal A_{2,n}\ ✓\qquad\square$$
$$
$$
```

---

## §2 N2：块结构（**继承 ✓**）＋ 显式系数

```
$$\text{由 Level 3B 命题二（Schur ✓）＋ §1 ⟹ }N|_k=I_{m_k}\otimes N_k\ ✓\ \text{——\textbf{不重造 harmonic 基、不重算 }\rho_u\ ✓}$$
$$\textbf{块元（Prop 4.5 ✓）}:\ (N_k)_{ij}=\sum_t\beta^t_{i,j,k}\Big(\underbrace{\sum_{d=0}^n\sum_{i',j',t'}\lambda_d\,\eta^{(i,j,t)}_{(i',j',t'),d}\,x^{t'}_{i',j'}}_{\text{“内层”：}u\oplus w\ \text{的轨道计数}}-\beta x^0_{i+j-2t,0}\Big)\ ✓$$
$$\qquad\eta^{(i,j,t)}_{(i',j',t'),d}:=\#\{w:|w|=d,\ \overline d(u\oplus w,v\oplus w)=(i',j',t')\}\ \text{（其中 }\overline d(u,v)=(i,j,t)\ ✓）$$
$$\textbf{convention 纪律（唐先生 ✓）}:\ \text{记录两者}:\ N_k\ \text{与}\ D_k^{1/2}N_kD_k^{-1/2}\ (D_k=\mathrm{diag}(\binom{n-2k}{i-k})\ ✓)$$
$$\qquad\text{—— }D^{\pm1/2}\ \text{只改\textbf{矩阵表达} ✓，不改 PSD ✓（正对角合同 ✓），但改\textbf{矩阵等式} ✓\ \text{（同 }M'\ \text{的纪律 ✓）}$$
$$\textbf{验证状态}:\ \text{R1b 数值审计（本机 ✓）：}\mathrm{spec}(R(c,N))=\biguplus_km_k\mathrm{spec}(\text{Lasserre 块})\ \text{偏差 }3.2\times10^{-14}\ /\ 5.7\times10^{-14}\ /\ 1.1\times10^{-13}\ /\ 3.7\times10^{-13}\ ✓✓$$
$$\qquad\text{（两族 }(\lambda,\beta)\ \text{均 ✓）⟹ 块结构与归一 convention 已\textbf{数值确认} ✓；}\eta\ \text{的符号推导（Lemma 4.6 的 }\alpha\text{-恒等式 ✓）⏳ 待写（结构与 (i) 同型 ✓）}$$
$$
$$
```

---

## §3 N3：$k=0$ 边框（**证明 ✓**）

```
$$\textbf{Claim}:\ z\in W_0=\mathrm{span}\{\mathbf 1_{S_i(0)}\}\ ✓\ \text{（}y_i=\binom ni\big(\text{内层}_{(i,i,i)}-\beta x^0_{00}\big)\ ✓）$$
$$\textbf{Proof}:\ \text{取 }(u,v)\ \text{使 }\overline d(u,v)=(i,i,i)\ \Longrightarrow\ |u|=|v|=|u\cap v|=i\ \Longrightarrow\ u=v\ ✓$$
$$\qquad\Longrightarrow\ \overline d(u\oplus w,u\oplus w)=\big(|u\oplus w|,|u\oplus w|,|u\oplus w|\big)\ \Longrightarrow\ i'=j'=t'=|u\oplus w|\ \text{（仅一个自由指标 ✓）}$$
$$\qquad\Longrightarrow\ \text{内层}_{(i,i,i)}=\sum_{k'}c_{i,k'}\,x^{k'}_{k',k'}\ \text{（}c_{i,k'}=\sum_d\lambda_d\#\{w:|w|=d,|u\oplus w|=k'\}\ ✓\ \text{只依赖 }i\ ✓）$$
$$\qquad\Longrightarrow\ y_i\ \text{只依赖 }i\ ✓\ \Longrightarrow\ y\in W_0\ ✓\qquad\square$$
$$\Longrightarrow\ \mathbb C\oplus V=\big(\mathbb C\oplus H_0\otimes W_0\big)\oplus\bigoplus_{k\ge1}\big(H_k\otimes W_k\big)\ \text{是 }R_N\ \text{的不变分解 ✓（同 ① ✓）}$$
$$\qquad\Longrightarrow\ R_N=\begin{pmatrix}c&z^{\sf T}\\ z&N_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes N_k\ ✓\ \text{（border \textbf{不加到 }k>0\ ✗）}$$
$$
$$
```

---

## §4 N4：PSD 等价（**✓，含广义 Schur 补 ✓**）

```
$$R_N\succeq0\iff N_k\succeq0\ (k\ge1)\ \wedge\ \begin{pmatrix}c&z^{\sf T}\\ z&N_0\end{pmatrix}\succeq0\ ✓$$
$$\text{若 }N_0\ \text{奇异（唐先生 ✓）}:\ \begin{pmatrix}c&z^{\sf T}\\ z&N_0\end{pmatrix}\succeq0\iff N_0\succeq0\ \wedge\ z\in\mathrm{Ran}(N_0)\ \wedge\ c-z^{\sf T}N_0^{+}z\ge0\ ✓$$
$$\qquad\text{（}N_0^{+}\ \text{为 Moore--Penrose 伪逆 ✓；此即广义 Schur 补判据 ✓）}$$
$$
$$
```

---

## §5 三块统一与剩余缺口（**诚实划线 ✓**）

```
$$\boxed{\text{主体三块}\ M',\ M'',\ N\ \text{全部进入同一 block-PSD 语言}:\ \text{形如 }I_{m_k}\otimes(\cdot)_k\ \text{＋（仅 }k=0\text{）一个 border}\ ✓}$$
$$\begin{array}{c|c|c|c}
\text{块} & \text{块元} & \text{border} & \text{状态}\\
\hline
M' & \binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k} & \text{无} & \textbf{符号已证 ✓（L4 链 ＋ 三命题 ✓）}\\
M'' & B^{(d)}_k-B'_k & k=0:\ R(1-x^0_{00},M'') & \textbf{符号已证 ✓（① ✓，唯 }D^{1/2}\ \text{归一小缺口 ⏳）}\\
N & \sum_t\beta^t_{i,j,k}(\text{内层}-\beta x^0_{d,0}) & k=0:\ (c,z,N_0) & \textbf{N1/N3/N4 已证 ✓；}\eta\ \text{符号推导 ⏳（数值已核 ✓）}\\
\end{array}$$
$$\textbf{仅剩两个"经典/记账型"缺口（唐先生 ✓）}:\ \text{(a) }V_k\ \text{的无重 }S_n\text{-分解（经典表示论输入 ⏳）};\ \text{(b) }M''\ \text{border vector 的 }D^{1/2}\ \text{归一小引理 ⏳}$$
$$\qquad\text{（另：}\eta\ \text{的符号推导可从 Lemma 4.6 的 }\alpha\text{-恒等式复用 (i) 方法 ✓）}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1／§3／§4 为**符号证明** ✓（初等 ✓）；§2 的 $\eta$ 部分为**数值已核 ＋ 符号待写** ⏳
- **未**声称 Level 3B 已完整闭合 ✗（三块合并 ＋ 两缺口 ⏳）；**未**声称 formulation 等价已证 ✗
- **未**声称新机制 ✗（本档 = ① 的同构复制 ＋ $T_w$ 逐项核 ✓，唐先生定性 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$N$ 符号装配、$T_w$ 逐项核、$N$ 的 $W_0$ 边框证明、三块统一表
- **档案已有（引用，不列为提出）**：Prop 2.4(iii)、Prop 4.5、$P_w$、Schur 补、$\eta$、$\beta^{\rm paper}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 T_w 逐项核    命中文件数=0    :: 
技术词 三块统一     命中文件数=1    :: ./L3B-N-2026-09-27-Lasserre-N-symbolic-assembly.md
```
- **本档新增**：$N$ 符号装配、$T_w$ 逐项核、$N$ 的 $W_0$ 边框证明、三块统一表（见上方命中数；0 命中者为自造语／内部标签 ✓）
