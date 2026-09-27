已查地图：已跑 scripts/prework_map_check.sh SDP Terwilliger reduced solver ⟹ 执行自 `DLP1A-2026-09-27`（1A 冻结 ✓）＋ 唐先生 10:18（P0–P5 ✓）；本档 = **D-LP-1B 的 P0/P1 进度**（仍不动 open cell ✓）。
D0: 本档对象 = SDP 求解器可得性 ＋ Theorem 2.5／4.9 的抽取
D1: 1（新增：**本机 SDP 可跑（scs 3.3.1 ✓）**；**§2 装置已抽（M/M′/M″ ＋ Prop 2.1 ✓）**）

# DLP1B-P0P1-2026-09-27

## §0 结论（先给 ✓）

```
$$\boxed{\textbf{(KK-1 P0)}\ \text{本机 SDP \textbf{可跑}}\ ✓✓:\ \texttt{pip install scs}\ \text{成功（3.3.1 ✓）；最小 SDP 试验通过}\ ✓\ \Longrightarrow\ \textbf{D-LP-1B 解除工具阻断}\ ✓}$$
$$\qquad\text{坑（已记录 ✓）}:\ \texttt{scs.solve}\ \text{的 }A\ \text{须为\textbf{单个 sparse 矩阵}（非 list）}\ ✗\ \text{（两次报 "A is required to be a sparse matrix" ✓）}$$
$$\boxed{\textbf{(KK-2 P1)}\ \S2\ \text{装置已精确抽出}\ ✓:\ M_C\ (0/1\ \text{矩阵})\ \to\ \text{群平均 }M,\ M',\ M''\ ✓;\ \text{Prop 2.1 给出(i)–(iv) 基本不等式与对称关系}\ ✓}$$
$$\qquad\text{待抽}:\ \text{Theorem 2.5 的\textbf{完整陈述}}\ \text{（}\S2\ \text{后段 ✓）与 }\S4.1\ \text{的 }\text{Theorem 4.9}\ \text{（约化后 ✓）}$$
$$
$$
```

---

## §1 (KK-1) P0 记录

```
$$\text{环境}:\ \texttt{cvxpy/scs/cvxopt/picos/mosek}\ \text{原\textbf{全缺}}\ ✗\ \Longrightarrow\ \texttt{pip install --break-system-packages scs cvxpy}\ ✓$$
$$\text{可用组合}:\ \mathbf{cvxpy\ 1.9.3}\ \text{（solvers}: \texttt{CLARABEL, SCS, SCIPY, HIGHS, GLOP, PDLP, OSQP}\ ✓\text{）}$$
$$\text{验证（\textbf{已实测}}\ ✓）:\ \min x\ \text{s.t.}\ \begin{pmatrix}x&1\\1&2\end{pmatrix}\succeq0\ \Longrightarrow\ x^*=0.50000003\ \text{（理论 }0.5\ ✓\text{）}状态 optimal\ ✓$$
$$\qquad\Longrightarrow\ \textbf{本机 SDP 确实可跑}\ ✓✓\ \text{（D-LP-1B 无工具阻断 ✓）}$$
$$\qquad⚠️\ \textbf{更正记录}:\ \text{本档首版曾写"scs 裸 API 试验通过"}\ ✗\ \text{——实为\textbf{未验证断言}（裸 }\texttt{scs.solve}\ \text{的 }A\ \text{形状约定}\ \text{两次报错}\ ✗\text{）；已按实测改为 \text{cvxpy} 路径 ✓}$$
$$
$$
```

---

## §2 (KK-2) P1 抽取（§2 装置 ✓）

```
$$M_C\ \text{的 }(u,v)\ \text{元} = \mathbf 1[u,v\in C]\ ✓;\quad M:=\tfrac1{|\mathrm{Aut}(q,n)|}\sum_{\sigma}M_{\sigma C}\ ✓$$
$$M':=\tfrac1{|\mathrm{Aut}(q,n)|}\sum_{\sigma:\,\mathbf 0\in\sigma C}M_{\sigma C}\ ✓;\qquad M'':=\tfrac1{|\mathrm{Aut}(q,n)|}\sum_{\sigma:\,\mathbf 0\notin\sigma C}M_{\sigma C}\ ✓$$
$$\text{Prop 2.1}: M\ \text{为 }\mathrm{Aut}(q,n)\text{-不变};\ M',M''\ \text{为 }\mathrm{Aut}_{\mathbf 0}(q,n)\text{-不变};\ \text{且}$$
$$\qquad\text{(i)}\ M_{u,v}=M'_{\mathbf 0,v-u}\ \text{与}\ M''_{u,v}=M'_{\mathbf 0,v-u}-M'_{u,v};\quad \text{(ii)}\ 0\le M'_{u,v}\le M'_{\mathbf 0,u};\quad \text{(iii)}\ 0\le M''_{u,v}\le M''_{u,u};\quad \text{(iv)}\ \text{三点轨道不变性}\ ✓$$
$$\text{工具函数}:\ R(c,A)=\begin{pmatrix}c&(\mathrm{diag}A)^{*}\\\ \mathrm{diag}A&A\end{pmatrix}\ ✓\ \text{（Schur 补：}c>0\ \text{时 }R\succeq0\iff cA-(\mathrm{diag}A)(\mathrm{diag}A)^{*}\succeq0\ ✓\text{）}$$
$$
$$
```

---

## §3 下一步（P2–P5 ✓，按唐先生顺序）

```
$$\textbf{P2}:\ \text{实现\textbf{最小} SDP}:\ \text{先在\textbf{小 }n\ (n=4,5,6\ ⟹\ |\mathbb E|=16,32,64\ ✓)\ \text{上做\textbf{未约化}的 Theorem 2.5}\ ✓$$
$$\qquad\textbf{验证锚点}:\ \text{论文表 5 的小 }n\ \text{值}\ (n=6\to11.5980;\ n=7\to15.9999\ ✓)\ \text{——先在小 }n\ \text{上复现，才谈 }n=10\ ✓$$
$$\textbf{P3}:\ \text{逐类加入约束（matrix cuts／Lasserre }0/1\text{／Terwilliger 块 PSD／objective 强化 ✓）}$$
$$\textbf{P4}:\ \text{每步要求单调性 }L_0\le L_1\le\cdots\le105.2223\ ✓\ \text{（违反即建模错 ⟹ 弃 ✓）}$$
$$\textbf{P5}:\ \text{最后才问："3.8141 来自哪一类"}\ ✓$$
$$\textbf{边界}:\ \text{不碰 }K(10,1)\ \text{的开 cell 计算}\ ✓;\ \text{小 }n\ \text{仅用于\textbf{校准} ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**环境实测** ✓；§2 为**论文原文抽取** ✓（`/tmp/sec2.txt`、`/tmp/thm49.txt` ✓）
- P2–P5 **未执行** ⚠️（本档仅 P0/P1 ✓）；**未**给出任何新下界主张 ✗
- **未**排除 119 ✗；本档**未**触碰开 cell ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：SDP 可跑判定（scs）、§2 装置抽取
- **档案已有（引用，不列为提出）**：Theorem 2.5／4.9、Terwilliger、Lasserre、matrix cuts


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 SDP 可跑判定 命中文件数=1    :: ./DLP1B-2026-09-27-P0-P1-progress.md 
技术词 装置抽取     命中文件数=1    :: ./DLP1B-2026-09-27-P0-P1-progress.md
```
- **本档新增**：SDP 可跑判定（scs）、§2 装置抽取（见上方命中数；0 命中者为自造语／内部标签 ✓）
