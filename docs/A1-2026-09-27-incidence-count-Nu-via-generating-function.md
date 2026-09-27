已查地图：已跑 scripts/prework_map_check.sh N_u incidence generating function Johnson 标量 ⟹ 执行自 `L4-...-source-structure-of-beta`（L4-1/3/4 ✓）＋ 唐先生 11:44（选 A ✓）；本档 = **A-1（$N_u$ 的母函数闭式）＋ A-2 计划**。
D0: 本档对象 = 固定 $(K,L)$ 的 incidence 计数 $N_u$（$\ne\beta$ ✓）
D1: 1（新增：**$F_u$ 母函数（含四区域证明 ✓）**；**$N_u\ne\beta_u$ 的严格分离 ✓**）

# A-1 · $N_u$ 的母函数（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(RR-1 $N_u$ 母函数 ✓)}\ F_u(p,q,r)=(pqr)^u\big[p(1+qr)\big]^{k-u}\big[q(1+pr)\big]^{k-u}\big(1+p+q+pqr\big)^{\,n-2k+u}\ ✓}$$
$$\qquad N_u(i,j,t)=[p^iq^jr^t]\,F_u(p,q,r)\ ✓\ \text{（}n=6,\ k=1,2,3,\ \text{全 }u\ \text{：暴力核对\textbf{零不符} ✓✓）}$$
$$\boxed{\textbf{(RR-2 提取式 ✓)}\ N_u(i,j,t)=[p^{i-k}q^{j-k}r^{t-u}]\ (1+qr)^{k-u}(1+pr)^{k-u}(1+p+q+pqr)^{\,n-2k+u}\ ✓}$$
$$\boxed{\textbf{(RR-3 严格分离 ✓)}\ N_u\ \text{系数\textbf{非负}};\ \ \beta\ \text{含}\ (-1)^{t-u}\binom ut\ \Longrightarrow\ \boxed{N_u\ne\beta_u}\ ✗\ \text{（交替符号来自 harmonic/Johnson 投影＋Möbius ✓）}}$$
$$\boxed{\textbf{(RR-4 必要性 ✓)}\ t<u\ \Longrightarrow\ N_u=0\ ✓\ \text{（}K\cap L\ \text{强制贡献 }u\ \text{个交元素 ✓；核对零反例 ✓）}}$$
$$
$$
```

---

## §1 四区域分解与母函数（**证明 ✓**）

```
$$\textbf{设 }|K|=|L|=k,\ |K\cap L|=u\ ✓;\ \text{四区域}:\ A=K\cap L\ (|A|=u),\ B=K\setminus L\ (|B|=k-u),\ C=L\setminus K\ (|C|=k-u),\ D=[n]\setminus(K\cup L)\ (|D|=n-2k+u)\ ✓$$
$$\textbf{定义}:\ F_u(p,q,r)=\sum_{S\supseteq K}\sum_{T\supseteq L}p^{|S|}q^{|T|}r^{|S\cap T|}\ ✓$$
$$\textbf{逐区域权重}:\ \text{（元素 }x\in A\ \text{强制入 }S,T\ \Longrightarrow\ pqr\ ✓;\ x\in B\ \text{必入 }S,\ \text{可选入 }T\ \Longrightarrow\ p+pqr=p(1+qr)\ ✓;\ x\in C\ \text{对称}\ \Longrightarrow\ q(1+pr)\ ✓;\ x\in D\ \text{自由}\ \Longrightarrow\ 1+p+q+pqr\ ✓）}$$
$$\Longrightarrow\ \textbf{RR-1}\ ✓\qquad\square$$
$$\text{（系数 }[p^iq^jr^t]F_u\ \text{恰为 }|S|=i,|T|=j,|S\cap T|=t\ \text{的 }(S,T)\ \text{数 ✓ ＝ }N_u(i,j,t)\ ✓）}$$
$$
$$
```

---

## §2 提取式与必要性（**✓**）

```
$$\text{强制因子}\ (pqr)^u p^{k-u}q^{k-u}=p^kq^kr^u\ \Longrightarrow\ \textbf{RR-2}\ ✓$$
$$\text{(i)}\ t\ge u\ ✓\ \text{（}r\ \text{的最低次幂为 }u\ ✓）;\ \text{(ii)}\ t-u\le(i-k)+(j-k)\ ✓\ \text{（}r\ \text{的幂次上界 ✓）};\ \text{(iii)}\ p,q\ \text{次幂 }i,j\ge k\ ✓$$
$$\text{语义}:\ u\ \text{个强制交元素已"预定"了 }r^u\ ✓\ \Longrightarrow\ \text{剩余 }t-u\ \text{个交必须从 }B,C,D\ \text{额外选入 ✓（＝唐先生 A2 的 }x+y+z=t-u\ ✓）}$$
$$
$$
```

---

## §3 $N_u\ne\beta_u$ 的严格分离（**✓ 重要纪律**）

```
$$\text{① }N_u\ \text{是固定 }(K,L)\ \text{的\textbf{计数}（非负整数 ✓），与 harmonic 无关 ✓}$$
$$\text{② }\beta^t_{i,j,k}\ \text{含 }(-1)^{t-u}\binom ut\ ✓\ \text{——\textbf{不可能}由非负计数直接产生 ✗}$$
$$\Longrightarrow\ \text{正确链条（唐先生 ✓）}:\ \boxed{N_u\longrightarrow\text{Johnson 标量 }\rho_u\longrightarrow\text{Möbius 反演}\longrightarrow\beta}\ ✓$$
$$\text{故 }\beta\ \text{的闭式\textbf{不作前提} ✓；本档只交 }N_u\ ✓$$
$$
$$
```

---

## §4 A-2 计划（**从 $N_u$ 到 Johnson 标量 $\rho_u$**）

```
$$\textbf{目标}:\ \text{证明}\quad \sum_{\substack{K,L\\|K\cap L|=u}}h(K)h(L)=\rho_u\|h\|^2\quad\forall h\in H_k\ ✓$$
$$\textbf{结构（待写全 ✓）}:\ \text{(i) }\Omega_u:=\text{Johnson 图 }J(n,k)\ \text{距离 }(k-u)\ \text{的邻接算子}\ ✓=\text{矩阵 }(\mathbf 1[|K\cap L|=u])_{K,L}\ ✓$$
$$\qquad\text{(ii) }\Omega_u\ \text{是 }S_n\text{-不变 ✓（轨道只依赖 }|K\cap L|\ ✓）\ \Longrightarrow\ \Omega_u\in\text{Johnson Bose--Mesner 代数 }\mathcal B\ ✓$$
$$\qquad\text{(iii) }V_k\ \text{是\textbf{无重} }S_n\text{-模（}V_k=\bigoplus_{j\le\min(k,n-k)}S^{(n-j,j)}\ ✓\ \text{各重数 }1\ ✓，经典 ✓）\ \Longrightarrow\ \mathcal B\ \text{的元在每个不可约上为\textbf{标量} ✓（Schur ✓）}$$
$$\qquad\text{(iv) }H_k\cong S^{(n-k,k)}\ \text{是其一 ✓（}\dim H_k=m_k=\dim S^{(n-k,k)}\ ✓\ \text{＋ }H_k\ \text{为 }S_n\text{-子模 ✓）}\ \Longrightarrow\ \Omega_u|_{H_k}=\rho_u I\ ✓$$
$$\textbf{预期产物}:\ \rho_u\ \text{的闭式（Eberlein 多项式／对偶 Hahn 型 ✓）\ ⟹\ 代入 }\S5\ \text{的二次型 ⟹ Möbius ⟹ }\beta\ \text{闭式 ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**证明 ＋ 独立数值核对** ✓（暴力 vs 母函数：零不符 ✓）
- §3 为**分离论断** ✓（非负 vs 交替 ⟹ 不可能相等 ✓）；§4 为**计划** ⏳（未做 ✗）
- **未**声称 $\beta$ 闭式已证 ✗；**未**声称 formulation 等价已证 ✗
- ⚠️ 纪律提醒（本轮无新错 ✓，沿用前两轮更正：作者式末项 $\binom{n-k-u}{j-u}$ ✓；脚本须用支撑／指标而非取值 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$N_u$ 母函数、四区域权重表、$N_u\ne\beta_u$ 分离
- **档案已有（引用，不列为提出）**：Johnson 方案、Eberlein 多项式、Schur、$H_k$、$S^{(n-k,k)}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 母函数        命中文件数=2    :: ./A1-2026-09-27-incidence-count-Nu-via-generating-function.md ./E28b-quasicrystal-verdict.md 
技术词 四区域权重  命中文件数=1    :: ./A1-2026-09-27-incidence-count-Nu-via-generating-function.md
```
- **本档新增**：$N_u$ 母函数、四区域权重表、$N_u\ne\beta_u$ 分离（见上方命中数；0 命中者为自造语／内部标签 ✓）
