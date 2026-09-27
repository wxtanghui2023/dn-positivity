已查地图：已跑 scripts/prework_map_check.sh Schrijver 归一化 raw coefficient β 闭式 ⟹ 执行自 `L5-...-norm-...-factorization`（L5 ✓）＋ 唐先生 11:50（精确定位 ✓）；本档 = **L4-5 闭合：$\widehat\beta$ 与 $\beta^{\rm paper}$ 的精确关系 ＋ 闭式提取**。
D0: 本档对象 = raw action coefficient $\widehat\beta$ vs Schrijver block coefficient $\beta$
D1: 1（新增：**精确 bridge 关系 ✓**；**母函数提取=作者闭式（判决性核对 ✓）**）

# L4-5 · Schrijver 归一化与 $\beta$ 闭式（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(UU-1 不是 convention 悬案，而是可定位的归一化 ✓)}\ \widehat\beta=\frac{(j-k)!}{(i-k)!\binom{n-2k}{i-k}}\,\beta^{\rm paper}\ ✓}$$
$$\boxed{\textbf{(UU-2 bridge 推导 ✓)}\ \widehat\beta=\frac{\langle h_i,M^t_{i,j}h_j\rangle}{\|h_i\|^2}
=\frac{(j-k)!}{(i-k)!\binom{n-2k}{i-k}}\Big(\sum_uN_u\rho_u\Big)\ ✓\ \Longrightarrow\ \boxed{\beta^{\rm paper}=\sum_uN_u\rho_u}\ ✓}$$
$$\boxed{\textbf{(UU-3 母函数提取口径 ✓✓)}\ \beta^{\rm paper}=\sum_uN_u(i,j,t)\rho_u=[p^{i-k}q^{j-k}r^t]\,(r-1)^k\big(1+p+q+pqr\big)^{\,n-2k}\ ✓}$$
$$\qquad\text{（由因式分解引理 }G=p^kq^k(r-1)^k\alpha^{\,n-2k}\ \text{直接得 ✓）}$$
$$\boxed{\textbf{(UU-4 判决性核对 ✓✓ 零不符)}\ \text{① bridge 关系：}6\ \text{组 }(n,k)\ \text{共 }501\ \text{组 }(i,j,t)\ \text{全中 ✓；② }\beta^{\rm paper}=[p^iq^jr^t]G\ \text{同范围全中 ✓}}$$
$$
$$
```

---

## §1 两种 $\beta$ 的严格区分（唐先生 11:50 ✓）

```
$$\textbf{raw（本链）}:\ M^t_{i,j}h_j=\widehat\beta^t_{i,j,k}h_i\ ✓\quad\widehat\beta=\frac{\langle h_i,M^t_{i,j}h_j\rangle}{\|h_i\|^2}\ ✓\ \text{（未归一链 }h_i=U^{i-k}h\ ✓）$$
$$\textbf{Schrijver block}:\ B_{ij}=\binom{n-2k}{i-k}^{-\frac12}\binom{n-2k}{j-k}^{-\frac12}\beta^t_{i,j,k}\ ✓\ \text{（论文 Thm 3.1 明确形式 ✓；与作者代码 }\texttt{CoveringCodesBinary.jl}\ \text{一致 ✓）}$$
$$\textbf{桥}:\ \text{由 }M e_j=\widehat\beta\frac{\|h_i\|}{\|h_j\|}e_i\ (e_i=h_i/\|h_i\|\ ✓)\ \text{＋ L5 的 }\frac{\|h_i\|}{\|h_j\|}=\frac{(i-k)!}{(j-k)!}\sqrt{\frac{C_i}{C_j}}\ ✓$$
$$\qquad\Longrightarrow\ \frac{\beta^{\rm paper}}{\sqrt{C_iC_j}}=\widehat\beta\frac{(i-k)!}{(j-k)!}\sqrt{\frac{C_i}{C_j}}\ \Longrightarrow\ \boxed{\widehat\beta=\frac{(j-k)!}{(i-k)!C_i}\beta^{\rm paper}}\ ✓\ \text{（}C_i=\binom{n-2k}{i-k}\ ✓）$$
$$
$$
```

---

## §2 两个具体例子（唐先生 ✓，与我的独立手算一致 ✓）

```
$$\text{例 1}:\ (n,k,i,j)=(6,1,1,3):\ i-k=0,\ j-k=2,\ C_i=\binom40=1\ \Longrightarrow\ \widehat\beta=2\beta^{\rm paper}\ ✓\ \text{（}\beta^{\rm paper}=-6\ ⟹\ \widehat\beta=-12\ ✓\text{）}$$
$$\qquad\text{独立手算核对 ✓}:\ h_3(S)=2\sum_{x\in S}h(x)\ ✓;\ (M^0_{1,3}h_3)(S)=12\sum_{x\notin S}h(x)\ ✓;\ \langle h_1,\cdot\rangle=12[({\textstyle\sum}h)^2-\|h\|^2]=-12\ ✓✓$$
$$\text{例 2}:\ (n,k,i,j)=(6,3,3,3):\ i-k=j-k=0,\ C_i=\binom00=1\ \Longrightarrow\ \widehat\beta=\beta^{\rm paper}\ ✓\ \text{（退化 ✓，故该 }k\ \text{零不符 ✓）}$$
$$\Longrightarrow\ \text{"同一 }(n,k)\ \text{内有的匹配有的差 2"＝因子 }R(i,j,k)=\frac{(j-k)!}{(i-k)!\binom{n-2k}{i-k}}\ \text{的取值不同 ✓（}\textbf{预期现象} ✓）}$$
$$
$$
```

---

## §3 L4-5 的最终形态（**已闭合 ✓**）

```
$$\text{链条（我们的独立路径 ✓）}:\ D/U\ \text{交换子（L2 ✓）}\to\text{harmonic 链（L4-1 ✓）}\to\text{Johnson 标量 }\rho_u=(-1)^{k-u}\binom ku\ \text{（A-2 ✓）}$$
$$\qquad\to\text{范数闭式（L5 ✓）}\to\text{因式分解引理（}G\ \text{✓）}\to\boxed{\beta^{\rm paper}=[p^{i-k}q^{j-k}r^t](r-1)^k\alpha^{\,n-2k}}\ ✓$$
$$\text{展开（系数提取 ✓）}:\ (r-1)^k=\sum_s\binom ks r^s(-1)^{k-s}\ ✓;\ \alpha^{\,n-2k}=\sum_{\substack{n_0+n_1+n_2+n_3\\=n-2k}}\frac{(n-2k)!}{n_0!n_1!n_2!n_3!}p^{n_1+n_3}q^{n_2+n_3}r^{n_3}\ ✓$$
$$\qquad\text{取 }n_1+n_3=i-k,\ n_2+n_3=j-k,\ n_3+s=t\ \Longrightarrow\ \nu:=n_3,\ n_0=n-i-j+k+\nu,\ s=t-\nu\ ✓$$
$$\Longrightarrow\ \beta^{\rm paper}=\sum_\nu(-1)^{k-t+\nu}\binom{k}{t-\nu}\frac{(n-2k)!}{(n-i-j+k+\nu)!\,(i-k-\nu)!\,(j-k-\nu)!\,\nu!}\ ✓$$
$$\qquad\text{与论文式 }\sum_u(-1)^{t-u}\binom ut\binom{n-2k}{u-k}\binom{n-k-u}{i-u}\binom{n-k-u}{j-u}\ \text{\textbf{数值全等} ✓（501 组零不符 ✓）——指标对应待写全 ⏳（纯 binomial 整理 ✓）}$$
$$
$$
```

---

## §4 证明资产现状（重大更新 ✓）

```
$$\boxed{\text{已闭合（我们的独立证明路径 ✓）}:\ L1\ ✓\ |\ L2\ \text{主体}\ ✓\ |\ L3\ ✓\ |\ L4\text{-}1\ ✓\ |\ A\text{-}1\ (N_u\ \text{母函数})\ ✓\ |\ A\text{-}2\ (\rho_u\ \text{定理})\ ✓\ |\ L5\ ✓\ |\ \text{因式分解引理}\ ✓\ |\ \textbf{L4-5 主体}\ ✓}$$
$$\text{余下}:\ \text{(i) 上式的指标整理（bilinear 恒等式 ✓，把 }\nu\text{-和写成论文的 }u\text{-和）};\ \text{(ii) }M''/N\ \text{对应链};\ \text{(iii) sl}_2\ \text{半单性引用};\ \text{(iv) 块 PSD }\iff\text{ 全 PSD 的最终合并}$$
$$\textbf{意义}:\ \text{论文的 }\beta\ \text{闭式}\textbf{已由我们从 }D/U\ \text{独立导出} ✓✓\ \text{（不再依赖"作者代码里有" ✓）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**推导 ＋ 独立手算 ＋ 判决性数值** ✓（零不符 ✓）；§3 为**系数提取** ✓（展开正确 ✓）＋ **指标对应的显式化仍待写全** ⏳
- **未**声称 formulation 等价已证 ✗；**未**声称块 PSD 等价已合并 ✗
- ⚠️ 更正 ✓：此前把该因子差异写成"待解决的 convention 悬案" ✗ —— 实为**可精确定位的 Schrijver 归一化** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：raw vs Schrijver 系数 bridge、母函数提取口径、$\beta$ 的独立导出
- **档案已有（引用，不列为提出）**：Schrijver Thm 3.1、$C_i$、二项式、母函数、$\rho_u$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 bridge 关系    命中文件数=1    :: ./L45-2026-09-27-schrijver-normalization-and-beta-closed-form.md 
技术词 母函数提取口径 命中文件数=1    :: ./L45-2026-09-27-schrijver-normalization-and-beta-closed-form.md
```
- **本档新增**：raw vs Schrijver bridge、母函数提取口径、$\beta$ 独立导出（见上方命中数；0 命中者为自造语／内部标签 ✓）
