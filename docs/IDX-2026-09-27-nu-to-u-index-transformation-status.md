已查地图：已跑 scripts/prework_map_check.sh nu u 指标变换 求和恒等式 有限差分 ⟹ 执行自 `L45-...-schrijver-...`（L4-5 主体 ✓）＋ 唐先生 11:52（先做 (i) ✓）；本档 = **$\nu$-和的更正 ＋ $\nu\leftrightarrow u$ 变换的现状与正确路线**。
D0: 本档对象 = $\nu$-和与论文 $u$-和的严格对应
D1: 1（新增：**$\nu$-式更正 ✓**；**"无逐项双射"的判决 ✓**；**有限差分路线 ✓**）

# IDX · $\nu\leftrightarrow u$ 指标变换（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(VV-1 }\nu\text{-式更正 ✓)}\ \beta^{\rm paper}=\sum_\nu(-1)^{k-t+\nu}\binom{k}{t-\nu}\frac{(n-2k)!}{(n-i-j+\nu)!\,(i-k-\nu)!\,(j-k-\nu)!\,\nu!}\ ✓}$$
$$\qquad\text{（上一档我误写 }n_0=n-i-j+k+\nu\ ✗\ \text{应为 }n-i-j+\nu\ ✓\ \text{—— }n_0=(n-2k)-n_1-n_2-\nu=n-i-j+\nu\ ✓）$$
$$\boxed{\textbf{(VV-2 两式和全等 ✓)}\ \text{7 组逐项比对（本机 ✓）：}(6,1,1,3,0),(6,1,2,2,1),(6,1,3,3,0),(6,2,3,3,1),(7,2,3,4,1),(6,2,2,4,0),(7,3,4,4,1)\ \text{全部 }\Sigma_\nu=\Sigma_u\ ✓✓}$$
$$\boxed{\textbf{(VV-3 但\textbf{无逐项双射} ✗)}\ \text{反例：}(6,1,3,3,0):\ \nu\text{-和 }1\ \text{项}(-6)\ \text{vs }u\text{-和 }3\ \text{项}(-36,+36,-6)\ \Longrightarrow\ \text{这是\textbf{求和恒等式}，非重标签 ✓}}$$
$$\boxed{\textbf{(VV-4 正确路线 ✓)}\ \text{用有限差分（离散 Leibniz）}:\ \sum_u(-1)^{t-u}\binom utf(u)=(-1)^t(\Delta^tf)(0)\ \text{型 ✓}\ \text{（见 }\S3\ ✓）}$$
$$
$$
```

---

## §1 $\nu$ 与 $u$ 的语义（唐先生第 1 步 ✓）

```
$$\textbf{我们的 }\nu:\ \text{α}^{n-2k}=(1+p+q+pqr)^{n-2k}\ \text{展开中取 }(pqr)\ \text{因子的个数 ✓（即 }D\ \text{区被"双边选入"的坐标数 ✓）}$$
$$\qquad\text{配套}:\ n_1=i-k-\nu\ \text{（p-选）},\ n_2=j-k-\nu\ \text{（q-选）},\ n_0=n-i-j+\nu\ \text{（取 1）};\ (r-1)^k\ \text{给出 }s=t-\nu\ \text{与符号 }(-1)^{k-s}\ ✓$$
$$\textbf{论文的 }u:\ \text{进入 Schreier/Lasserre 系数的指标，满足 }u\ge k\ (\binom{n-2k}{u-k}\ ✓)\ \text{与 }u\ge t\ (\binom ut\ ✓)\ ✓$$
$$\qquad\text{形态差异}:\ \nu\le\min(t,i-k,j-k)\ \text{（}n_1,n_2\ge0\ ✓\text{）};\ u\ge\max(k,t)\ \text{——\textbf{范围形态相反} ✓\ \Longrightarrow\ 无逐项双射 ✓}$$
$$
$$
```

---

## §2 判决证据（✅ 无反例的求和恒等 ✓）

```
$$\begin{array}{c|c|c|c}
(n,k,i,j,t) & \nu\text{-项} & u\text{-项} & \Sigma\\
\hline
(6,1,1,3,0) & \{0:-6\} & \{1:-6\} & -6\ ✓\\
(6,1,2,2,1) & \{0:12,1:-4\} & \{1:16,2:-8\} & 8\ ✓\\
(6,1,3,3,0) & \{0:-6\} & \{1:-36,2:36,3:-6\} & -6\ ✓\\
(6,2,3,3,1) & \{0:-4,1:2\} & \{2:-8,3:6\} & -2\ ✓\\
(7,2,3,4,1) & \{0:-6,1:6\} & \{2:-18,3:18\} & 0\ ✓\\
(6,2,2,4,0) & \{0:1\} & \{2:1\} & 1\ ✓\\
(7,3,4,4,1) & \{1:-1\} & \{3:3,4:-4\} & -1\ ✓\\
\end{array}$$
$$\Longrightarrow\ \text{第 3、5、7 行\textbf{项数不同} ⟹ 必须用恒等式（非重标签 ✓）—— 唐先生第 2 步的"重指标变换"在此处\textbf{不成立} ✗，需改为有限差分/生成函数路线 ✓}$$
$$
$$
```

---

## §3 正确路线（唐先生第 3–5 步的可行版本 ✓）

```
$$\textbf{观察（关键 ✓）}:\ \text{论文和中的 }(-1)^{t-u}\binom ut\ \text{恰为\textbf{有限差分}核}:\ \sum_u(-1)^{t-u}\binom utf(u)=(\Delta^tf)(u_0)\ \text{型 ✓}$$
$$\qquad\text{故 }\beta^{\rm paper}=(\Delta^t\text{ 作用在 }u\mapsto\binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}\ \text{上})\ \text{的取值 ✓}$$
$$\textbf{可行证明（两步 ✓）}:\ \text{(A) 对三项乘积用\textbf{离散 Leibniz}}:\ \Delta^t(fg)=\sum_s\binom ts(\Delta^sf)(\Delta^{t-s}g)\ \text{型 ✓};\ \text{(B) 各 }\Delta^k\binom{m}{\cdot}\ \text{有闭式 ✓}（(-1)^k\binom{m-k}{\cdot-k}\ \text{型 ✓}）$$
$$\Longrightarrow\ \text{化到单重和 ⟹ 与 }\nu\text{-式逐项对齐（此时应为同范围 ✓）⟹ 目标：}\boxed{\text{两侧 ＝ }[p^{i-k}q^{j-k}r^t](r-1)^k\alpha^{\,n-2k}}\ ✓$$
$$\textbf{最强替代（更短 ✓）}:\ \text{直接算论文和的生成函数（对 }i,j,t\ \text{求和），证明其等于 }(r-1)^k\alpha^{n-2k}:\ \text{等价于验证一个三项生成函数恒等式 ✓（可用 }\alpha\ \text{的四类展开直接比对 ✓）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1–§2 为**本档核对** ✓（7 组逐项列出 ✓）；§3 为**路线** ⏳（未执行完 ✗）
- **未**声称 $\nu\leftrightarrow u$ 恒等式已证 ✗ —— 本档只**更正了 $\nu$-式**并**判决无逐项双射** ✓
- ⚠️ 更正 ✓：上一档 $n_0$ 写法有误 ✗（多写了 $+k$ ✓），本档已改 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\nu$-式更正、无逐项双射判决、有限差分路线
- **档案已有（引用，不列为提出）**：离散 Leibniz、有限差分、Vandermonde、母函数


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 无逐项双射  命中文件数=1    :: ./IDX-2026-09-27-nu-to-u-index-transformation-status.md 
技术词 有限差分路线 命中文件数=1    :: ./IDX-2026-09-27-nu-to-u-index-transformation-status.md
```
- **本档新增**：$\nu$-式更正、无逐项双射判决、有限差分路线（见上方命中数；0 命中者为自造语／内部标签 ✓）
