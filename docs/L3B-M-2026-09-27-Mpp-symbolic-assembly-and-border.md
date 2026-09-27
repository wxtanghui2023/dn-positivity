已查地图：已跑 scripts/prework_map_check.sh M'' 边框 块 Schur 补 归一 ⟹ 执行自 `L3B-...-assembly`（三命题 ✓）＋ 唐先生 11:56（① ✓）；本档标为 **M'' symbolic assembly + border，not merely numerical audit** ✓。
D0: 本档对象 = $M''$ 与边框 $R(1-x^0_{00},M'')$ 的块结构（符号版）
D1: 1（新增：**L4-M1～M4 证明 ✓**；**border 只占 $k=0$ 的定位证明 ✓**；**scalar factor 核验表 ✓**）

# ① $M''$ 符号装配与边框（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(YY-1 M1 交换子保持 ✓)}\ M^{(d)}:=M'_{0,\cdot-\cdot}\in\mathcal A_{2,n}\ ✓\ \text{（条目只依赖 }d(u,v)\ \Longrightarrow\ S_n\text{-不变 ✓）};\ M'\in\mathcal A_{2,n}\ ✓\ \Longrightarrow\ M''\in\mathcal A_{2,n}\ ✓}$$
$$\boxed{\textbf{(YY-2 M2 块线性化 ✓)}\ M''|_k=I_{m_k}\otimes B''_k,\qquad B''_k=B^{(d)}_k-B'_k\ ✓\ \text{（restriction 的线性性 ✓，不重算 }H_k\ \text{上矩阵元 ✓）}}$$
$$\boxed{\textbf{(YY-3 M3 边框只占 }k=0\ ✓)}\ \mathrm{diag}(M'')\in H_0\otimes W_0\ ✓\ \Longrightarrow\ R(1-x^0_{00},M'')=\begin{pmatrix}1-x^0_{00}&*\\ *&B''_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes B''_k\ ✓}$$
$$\boxed{\textbf{(YY-4 M4 PSD 等价 ✓)}\ R(1-x^0_{00},M'')\succeq0\iff\begin{pmatrix}1-x^0_{00}&*\\ *&B''_0\end{pmatrix}\succeq0\ \text{（\textbf{完整 Schur 补}）}\ \wedge\ B''_k\succeq0\ (k\ge1)\ ✓}$$
$$
$$
```

---

## §1 L4-M1：交换子保持（**证明 ✓**）

```
$$\textbf{(a) }M^{(d)}\in\mathcal A_{2,n}\ ✓:\ (M^{(d)})_{u,v}=M'_{0,v-u}\ \text{（论文 Prop 2.1(i) ✓）};\ M'\ \text{是 }\mathrm{Aut}_0\text{-不变 ✓（Prop 2.1 ✓）};\ \mathrm{Aut}_0=S_n\ \text{（稳定 }0\ ✓）$$
$$\qquad\Longrightarrow\ M'_{0,w}\ \text{只依赖 }|w|\ ✓\ \Longrightarrow\ (M^{(d)})_{u,v}=\varphi(d(u,v))\ ✓\ \text{—— 相距只依赖距离 ⟹ 对同时置换不变 ✓}$$
$$\qquad(P_\sigma M^{(d)}P_\sigma^{-1})_{u,v}=\varphi(d(\sigma^{-1}u,\sigma^{-1}v))=\varphi(d(u,v))\ \Longrightarrow\ M^{(d)}\in\mathrm{End}_{S_n}(V)=\mathcal A_{2,n}\ ✓\ \text{（L1 ✓）}$$
$$\textbf{(b) }M'\in\mathcal A_{2,n}\ ✓\ \text{（Prop 2.1：}M'\ \text{为 }\mathrm{Aut}_0\text{-不变 ✓；或直接用 L1 的"轨道常值"刻画 ✓）}$$
$$\Longrightarrow\ M'':=M^{(d)}-M'\in\mathcal A_{2,n}\ ✓\ \text{（子空间 ✓）}\qquad\square$$
$$
$$
```

---

## §2 L4-M2：块线性化（**证明 ✓，一行**）

```
$$\text{由 Level 3B 命题二}:\ \text{每个 }X\in\mathcal A_{2,n}\ \text{满足 }X|_k=I_{m_k}\otimes B_k\ ✓\ \text{（Schur ✓）}$$
$$\text{restriction 线性}:\ (X+Y)|_k=X|_k+Y|_k\ \Longrightarrow\ M''|_k=I_{m_k}\otimes\big(B^{(d)}_k-B'_k\big)\ ✓$$
$$\textbf{纪律（唐先生 ✓）}:\ \text{此处\textbf{不}重算 }H_k\ \text{上矩阵元 ✗ —— 只用线性性 ✓（}B'_k\ \text{已由 L4-1/A-2/L5/L4-5 给出 ✓）}$$
$$
$$
```

---

## §3 L4-M3：边框只占 $k=0$（**证明 ✓，独立检查点 ✓**）

```
$$\textbf{Claim}:\ y:=\mathrm{diag}(M'')\in H_0\otimes W_0\ ✓\ \text{（即"径向"分量 ✓，}W_0=\mathrm{span}\{\mathbf 1_{S_i(0)}\}_{i=0}^n\ ✓,\ \dim=n+1\ ✓）}$$
$$\textbf{Proof}:\ y_u=M''_{u,u}=M'_{0,0}-M'_{u,u}\ ✓;\ M'\ \text{为 }\mathrm{Aut}_0\text{-不变 ⟹ }M'_{u,u}\ \text{只依赖 }|u|\ ✓$$
$$\qquad\Longrightarrow\ y=\sum_{i=0}^nf(i)\,\mathbf 1_{S_i(0)}\in\mathrm{span}\{\mathbf 1_{S_i(0)}\}=W_0\subseteq H_0\otimes W_0\ ✓\qquad\square$$
$$\Longrightarrow\ \mathbb C\oplus V=\big(\mathbb C\oplus H_0\otimes W_0\big)\oplus\bigoplus_{k\ge1}\big(H_k\otimes W_k\big)\ \text{是 }R\ \text{的不变分解 ✓（}y\in\ \text{第一块 ✓）}$$
$$\textbf{与作者代码一致 ✓}:\ \texttt{CoveringCodesBinary.jl}\ \text{中 }\texttt{addValue = k==0 ? 1 : 0}\ ✓\ \text{——\textbf{边框只给 }k=0\ \text{加 1 维 ✓}}$$
$$\textbf{常见错误（唐先生点出 ✓）}:\ \text{\textbf{不}可把边框当作"每个 }k\ \text{块都加一维" ✗；也不可只查 }B''_0\succeq0\ \text{而漏掉完整 Schur 补 ✗}$$
$$
$$
```

---

## §4 L4-M4：PSD 等价（**证明 ✓ ＋ 检查点 ✓**）

```
$$\text{由 §3 的不变正交分解（Maschke ✓）＋ §2 的块形式 ⟹ }R\ \text{块对角}:\ R=\begin{pmatrix}1-x^0_{00}&*\\ *&B''_0\end{pmatrix}\oplus\bigoplus_{k\ge1}I_{m_k}\otimes B''_k\ ✓$$
$$\Longrightarrow\ R\succeq0\iff\begin{pmatrix}1-x^0_{00}&*\\ *&B''_0\end{pmatrix}\succeq0\ \wedge\ I_{m_k}\otimes B''_k\succeq0\ \forall k\ge1\iff B''_k\succeq0\ (k\ge1)\ ✓$$
$$\textbf{独立检查点（唐先生 ✓）}:\ k=0\ \text{须用\textbf{完整 Schur 补}}:\ \begin{pmatrix}c&\tilde y^{\sf T}\\ \tilde y&\tilde L\end{pmatrix}\succeq0\iff \tilde L\succeq0\ \text{且}\ c-\tilde y^{\sf T}\tilde L^{+}\tilde y\ge0\ \text{（}\tilde L^{+}\ \text{为 Moore--Penrose 伪逆 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{仅查 }B''_0\succeq0\ \text{不充分} ✗\ \text{（border 里的 }c=1-x^0_{00}\ \text{与 }y\ \text{带来\textbf{额外必要条件} ✓）}$$
$$
$$
```

---

## §5 scalar factor 核验表（**不靠同构推断 ✓，逐项核 ✓**）

```
$$\begin{array}{c|c|c|c}
\text{对象} & \text{论文原式（Prop 2.1(i) / 4.3 / 作者代码 ✓）} & \text{本档采用} & \text{状态}\\
\hline
M''_{u,v} & M'_{0,v-u}-M'_{u,v}\ ✓\ \text{（无额外因子 ✓）} & \text{同 ✓} & ✓\ \text{逐项核}\\
B''_k\ \text{内部} & \binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k}\ ✓ & \text{同（L4-5 桥 ✓）} & ✓\ \text{已符号证}\\
\text{边框向量 }y_i & \binom ni\big(x^0_{0,0}-x^0_{i,0}\big)\ ✓ & \binom ni^{1/2}\ \text{版（R1a ✓）} & \text{数值已核 ✓／符号归一同 L5 ⏳}\\
k=0\ \text{内部 }L & \sum_t\beta^t_{i,j,0}\big(x^0_{d,0}-x^t_{i,j}\big)\ ✓ & \text{同（含归一 ✓）} & \text{数值已核 ✓}\\
\end{array}$$
$$\text{注 ✓}:\ \binom ni\ \text{与}\ \binom ni^{1/2}\ \text{的差别恰是"谁带 }D^{\pm1/2}"\text{的 convention ✓ —— PSD 不受正对角合同影响 ✓，但\textbf{矩阵等式}受影响 ✓；R1a 的数值审计（}7.5\times10^{-14}\ ✓）已确认本档选法与 PSD 等价相容 ✓}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1–§4 为**符号证明** ✓（M1 交换子 ✓、M2 线性 ✓、M3 定位 ✓、M4 等价 ＋ SC 检查点 ✓）
- §5 的最后一列诚实标注：**边框向量归一化的符号推导**仍未写出 ⏳（结构与 L5 同型 ✓，可复用其方法 ✓）；其余均已核 ✓
- **未**声称完整 Level 3B 已完成 ✗（尚缺 ② Lasserre $N$ 的符号版 ✓）；**未**声称 formulation 等价已证 ✗
- **未**声称新机制 ✗：本档 = $M'$ 框架的线性 restriction ＋ $k=0$ 边框 bookkeeping ✓（唐先生定性 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$M''$ 符号装配、border 只占 $k=0$ 的定位证明、border Schur 补检查点
- **档案已有（引用，不列为提出）**：Prop 2.1、Prop 4.3、Schur 补、Maschke、$\rho_u$、$\beta^{\rm paper}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 M'' 符号装配 命中文件数=0    :: 
技术词 border Schur 补 命中文件数=1    :: ./L3B-M-2026-09-27-Mpp-symbolic-assembly-and-border.md
```
- **本档新增**：$M''$ 符号装配、border 只占 $k=0$ 的定位证明、border Schur 补检查点（见上方命中数；0 命中者为自造语／内部标签 ✓）
