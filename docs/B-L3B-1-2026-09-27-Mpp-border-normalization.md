已查地图：已跑 scripts/prework_map_check.sh border 归一化 径向基 Gram D^{1/2} ⟹ 执行自 `A-L3B-2-...`（(A) ✓）＋ 唐先生 12:03（(B) ✓）；本档登记为 **B-L3B-1 — $M''$ border normalization** ✓（**不产生新数学资产** ✓）。
D0: 本档对象 = $M''$ border 向量的归一化坐标（convention lemma）
D1: 0（归一化/坐标变换引理 ✓，不产生新数学命题 ✓）

# (B) $M''$ border 归一化（2026-09-27）

## §0 引理（B-L3B-1，六条 ✓）

```
$$\boxed{\textbf{(1)}\ z\in W_0\ \text{（① 已证 ✓）}\qquad\textbf{(2)}\ \langle b_i,b_j\rangle=\delta_{ij}\binom ni\quad(b_i:=\mathbf 1_{S_i(0)}\ ✓)\ \Longrightarrow\ D_0=\mathrm{diag}\binom ni\ ✓}$$
$$\boxed{\textbf{(3)}\ Q_0:=E_0D_0^{-\frac12}\ \text{列正交归一}\ (Q_0^{\sf T}Q_0=I\ ✓)\qquad\textbf{(4)}\ \boxed{z_{\rm block}=Q_0^{\sf T}E_0z_{\rm raw}=D_0^{\frac12}z_{\rm raw}}\ ✓}$$
$$\boxed{\textbf{(5)}\ \text{与论文 }D^{\frac12}\ \text{形式一致（}\textbf{若论文 }D\ \text{取 reciprocal 则须注明转换} ✓\text{）}\qquad\textbf{(6)}\ \textbf{不产生新资产，仅关闭 Level 3B 的 normalization gap}\ ✓}$$
$$
$$
```

---

## §1 B-1：三个坐标（**含范围核对 ✓**）

```
$$\text{层基}:\ e_{i,S}=\mathbf 1_{\{S\}}\ (|S|=i)\ ✓;\qquad W_0\ \text{径向基}:\ b_i=\mathbf 1_{S_i(0)}\quad(i=0,\ldots,n)\ ✓$$
$$\text{（}z_u=M'_{0,0}-M'_{u,u}=f(|u|)\ ✓\ \Longrightarrow\ z=\sum_{i=0}^{n}f(i)b_i\ ✓\ \text{—— \textbf{原始径向坐标} ✓）}$$
$$\textbf{范围核对（本档 ✓）}:\ \{b_i\}\ \text{的指标是 }i=0,\ldots,n\ \text{（共 }n+1\ \text{个 ✓，}\dim W_0=n+1\ ✓\text{）};\ \lfloor n/2\rfloor\ \text{是 \textbf{harmonic 度 }k\ \text{的范围} ✓ —— \textbf{两者勿混} ✓}$$
$$\qquad\text{核对（本机 ✓）}:\ n=4\ \text{对角}=[1,4,6,4,1]\ ✓;\ n=6:[1,6,15,20,15,6,1]\ ✓;\ n=8:[1,8,28,56,70,56,28,8,1]\ ✓$$
$$
$$
```

---

## §2 B-2：$D$ 到底是什么（**reciprocal 陷阱 ✓**）

```
$$\langle b_i,b_j\rangle=|S_i(0)\cap S_j(0)|=\delta_{ij}\binom ni\ ✓\ \text{（不同球面不相交 ✓；}\mathbf 1\ \text{的自内积＝球大小 ✓）}$$
$$D_0:=\mathrm{diag}\Big(\binom n0,\binom n1,\ldots,\binom nn\Big)\ \Longrightarrow\ \text{正交归一基}\ \widehat b_i=\binom ni^{-\frac12}b_i\ ✓$$
$$\text{由 }z=\sum_iz_ib_i=\sum_i\big(z_i\binom ni^{\frac12}\big)\widehat b_i\ \Longrightarrow\ \boxed{\widehat z=D_0^{\frac12}z_{\rm raw}}\ ✓$$
$$\textbf{陷阱（唐先生 ✓）}:\ \text{\textbf{不是} }D_0^{-\frac12}z_{\rm raw}\ ✗\ \text{—— 原始坐标 }\to\ \text{正交归一坐标是"乘"}\ D_0^{+\frac12}\ ✓\ \text{（因 }b_i\ \text{长 }\binom ni^{\frac12}\ ✓\text{）}$$
$$
$$
```

---

## §3 B-4：最干净的矩阵证明（**✓**）

```
$$E_0:\ \text{径向原始坐标空间}\to W_0\ \text{的嵌入}\ ✓\ \text{（列 }=b_i\ ✓）\ \Longrightarrow\ E_0^{\sf T}E_0=D_0\ ✓$$
$$Q_0:=E_0D_0^{-\frac12}\ \Longrightarrow\ Q_0^{\sf T}Q_0=D_0^{-\frac12}E_0^{\sf T}E_0D_0^{-\frac12}=I\ ✓\ \text{（列即 }W_0\ \text{的标准正交基 ✓）}$$
$$\forall z_{\rm raw}:\ \text{其 block 坐标}=Q_0^{\sf T}E_0z_{\rm raw}=D_0^{-\frac12}\underbrace{E_0^{\sf T}E_0}_{=D_0}z_{\rm raw}=D_0^{\frac12}z_{\rm raw}\ ✓\qquad\Longrightarrow\ \textbf{(4)}\ ✓\qquad\square$$
$$
$$
```

---

## §4 B-5：论文 $D$ convention 的核对（**先定义 $D$，再判平方根 ✓**）

```
$$\text{论文 Prop 4.3 的 border}:\ y_i=\binom ni\big(x^0_{0,0}-x^0_{i,0}\big)\ ✓\ \Longrightarrow\ y=D_0\,z_{\rm raw}\ \text{（}z_{\rm raw}\ \text{坐标}=x^0_{00}-x^0_{i,0}\ ✓）}$$
$$\text{本档若取 }D:=D_0\ \text{（}D_{ii}=\binom ni\ ✓\text{）}\ \Longrightarrow\ \widehat z=D^{\frac12}z_{\rm raw}\ ✓\ \text{—— 与论文形式一致 ✓}$$
$$\text{若论文另取 }D_{ii}=\binom ni^{-1}\ ✓,\ \text{则论文的 }D^{\frac12}\ \text{即本档 }D_0^{-\frac12}\ ✓\ \text{—— 坐标关系\textbf{不变} ✓（\textbf{audit criterion = 先定义 }D,\ \text{再判平方根} ✓）}$$
$$\textbf{与 R1a 审计的一致（\textbf{独立交叉} ✓✓）}:\ \text{R1a 中用 }B_h=\begin{pmatrix}c&(D_0^{-\frac12}y)^{\sf T}\\ D_0^{-\frac12}y&D_0^{-\frac12}\widetilde LD_0^{-\frac12}\end{pmatrix}\ ✓$$
$$\qquad\Longrightarrow\ \widehat z=D_0^{-\frac12}y=D_0^{-\frac12}D_0z_{\rm raw}=D_0^{\frac12}z_{\rm raw}\ ✓\ \text{—— \textbf{与 (4) 完全一致} ✓✓（且该审计为 1e-13 级 ✓）}$$
$$
$$
```

---

## §5 数值核对（**✓ 本机**）

```
$$\text{① Gram}:\ \langle b_i,b_j\rangle=\delta_{ij}\binom ni\ ✓\ \text{（}n=4,6,8\ \text{全中 ✓）}$$
$$\text{② 坐标}:\ \widehat z=D_0^{1/2}z_{\rm raw}\ \text{与反算互逆 ✓（}n=6:\ z_{\rm block}[0..2]=[1,2.4495,3.873]\ \leftrightarrow\ z_{\rm raw}=[1,1,1]\ ✓\text{）}$$
$$\text{③ 与论文/R1a 一致 ✓（见 §4 ✓）}$$
$$
$$
```

---

## §6 登记（**✓，关闭 normalization gap**）

```
$$\boxed{\textbf{B-L3B-1 — }M''\ \text{border normalization}:\ \text{(1)-(6) 条 ✓；}\textbf{不产生新数学资产} ✓;\ \textbf{关闭 Level 3B 的 normalization gap} ✓}$$
$$\text{Level 3B 剩余缺口（唐先生 ✓ 两者正交 ✓）}:\ \text{(B) }\textbf{已关} ✓;\ \text{(C) }N\ \text{中 }\eta\ \text{的符号闭式} ⏳\ \text{（Lasserre coupling coefficient ✓）}$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1–§5 为**引理 ＋ 证明 ＋ 数值** ✓（初等 ✓，含 reciprocity 陷阱的显式标注 ✓）
- **未**声称新资产 ✗；**未**声称 Level 3B 完整闭合 ✗（(C) ⏳）
- ⚠️ 范围更正 ✓：$\{b_i\}$ 指标为 $i=0..n$（非 $0..\lfloor n/2\rfloor$ ✗ —— 后者是 harmonic 度 $k$ ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：border 归一化引理 B-L3B-1、radial Gram 矩阵 $D_0$、reciprocal 陷阱标注
- **档案已有（引用，不列为提出）**：Prop 4.3、$W_0$、$D^{1/2}$ 合同、R1a 审计


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 border 归一化引理 命中文件数=1    :: ./B-L3B-1-2026-09-27-Mpp-border-normalization.md 
技术词 reciprocal 陷阱 命中文件数=1    :: ./B-L3B-1-2026-09-27-Mpp-border-normalization.md
```
- **本档新增**：border 归一化引理 B-L3B-1、radial Gram 矩阵 $D_0$、reciprocal 陷阱标注（见上方命中数；0 命中者为自造语／内部标签 ✓）
