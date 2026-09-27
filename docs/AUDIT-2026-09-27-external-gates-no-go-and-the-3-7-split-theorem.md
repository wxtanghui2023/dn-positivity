已查地图：已跑 scripts/prework_map_check.sh 外部约束 minimality |S| 3-7 ⟹ 执行自 `CORR-CLOSEDFORM-2026-09-27-...`（✓）＋ 唐先生 14:04（开甲 ✓）；本档 = **(甲) 外部约束审计（覆盖＋最小性皆 NO-GO ✓）＋ (乙) 3/7 分裂定理 ✓**。
D0: 本档对象 = 外部条件是否含 s-信息；s 与 |S| 之精确关系
D1: 3（**External-Cover Gate = NO-GO（含最小性实测 ✓）**；**3/7 分裂定理 ✓**；**flat 判据再更正为 s∈{8,16} ✓**）

# (甲) 外部约束审计 ＋ (乙) 3/7 分裂定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CF-1 ⭐External-Cover Gate = NO-GO ✓)}\ \text{覆盖性（初等 ✓）与 \textbf{inclusion-minimality}（本机实测 ✓）均\textbf{不含 }s\text{-信息}}:}$$
$$\qquad b=0\ \text{层用 }H_{15}\ \text{（perfect ✓）};\ b=1\ \text{层用 }V_\lambda\ \text{（perfect ✓）} \Longrightarrow \mathfrak B_1(\mathcal C_\lambda)=\mathbb F_2^{16}\ \forall\lambda\ ✓\ \text{（与 }s\ \text{无关 ✓）}$$
$$\qquad\textbf{最小性实测 ✓}:\ \lambda\in\{\mathbf 1(s{=}9),\ 1{\oplus}r(s{=}1),\ r\text{翻一}(s{=}15),\ r(s{=}16)\}:\ V\ \text{最小 ✓✓},\ \mathcal C\ \text{最小 ✓✓（四例全过 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\forall s\in\{1,\dots,16\}:\ \exists\lambda\ \text{使 }\mathcal C_\lambda\ \text{既覆盖又最小 ✓✓}\ \Longrightarrow\ \textbf{"NP1CC}\Rightarrow s\in\text{小子集"已被 }s{=}1,15,16\ \text{击穿 ✓}}$$
$$\boxed{\textbf{(CF-2 ⭐⭐3/7 分裂定理（由 coset 律一步得 ✓✓）)}\ s<1\ \text{不可能（agreement ✓）};\ \text{而 }\mathrm{supp}\ \text{来自两陪集 }(W_0\setminus\{0\})\ (3\ \text{列})\ \sqcup\ W_3\ (4\ \text{列}):}$$
$$\qquad\boxed{1\le s\le15\ \Longrightarrow\ 32s>0\ \wedge\ 32(16-s)>0\ \Longrightarrow\ |S|=3+4=\mathbf 7\ ✓✓;\qquad s=16\ \Longrightarrow\ 32(16-s)=0\ \Longrightarrow\ |S|=\mathbf 3\ ✓✓}$$
$$\qquad\textbf{且 }A_2=3\cdot32s+4\cdot32(16-s)=2048-32s\ ✓\ \text{（}s\in\{1,\dots,16\}\ \text{全验 ✓）}$$
$$\boxed{\textbf{(CF-3 ⚠️再更正)}:\ \textbf{flat}\iff q\ \text{在 }\mathrm{supp}\ \text{上恒定}\iff \boxed{s\in\{8,\ \mathbf{16}\}}\ ✓\ \text{（}s{=}16\ \text{为单陪集，仍属 flat ✓）}\ \Longrightarrow\ \text{上一档"flat}\iff s{=}8\text{"\textbf{漏了 }s{=}16\ ✗}}$$
$$
$$
```

---

## §1 实测表（**✓ 本机**）

```
$$\begin{array}{c|c|c|c|c|c}
\lambda & s & V\ \text{最小} & \mathcal C\ \text{最小} & |S| & \text{切片值}\\ \hline
\mathbf 1[c\ne0] & 9 & ✓ & ✓ & 7 & 288/224\\
1\oplus r\ (c\ne0) & 1 & ✓ & ✓ & 7 & 32/480\\
r\ \text{翻转一处} & 15 & ✓ & ✓ & 7 & 480/32\\
r & 16 & ✓ & ✓ & \mathbf 3 & \mathbf{512}\\
\end{array}$$
$$\textbf{注 ✓}:\ s{=}16\ \text{时陪集值 }(512,0)\ \text{——第二陪集为空，故 }\mathrm{supp}\ \text{只剩 3 列且单值 ⟹ flat ✓（按"supp 上恒定"之定义 ✓）}$$
$$
$$
```

---

## §2 资态（**✓ 最终形态**）

```
$$\textbf{定理级 ✓}:\ (1)\ q=X*C,\ X=32\cdot\mathbf 1_W,\ W=\mathrm{span}\{2,4\}; \quad (2)\ q\ \text{在每个 }W\text{-陪集恒定};\ \text{本族 }C\subseteq V=\mathrm{span}\{2,4,9\}\ \Longrightarrow\ s_1=s_2=0;$$
$$\qquad(3)\ s=\#\{c:r(c)=\lambda(c)\}\in\{1,\dots,16\}\ \text{全可达};\ (4)\ \text{陪集值 }(32s,\ 32(16-s))\ \Longrightarrow\ \textbf{和恒 }512\ ✓;\ (5)\ |S|=7\ (1{\le}s{\le}15)\ \text{或 }3\ (s{=}16)\ ✓;\ (6)\ A_2=2048-32s\ ✓$$
$$\textbf{已证伪/删除 ✗}:\ \text{"flat}\iff|S|\mid A_2"\ ✗;\ \text{"flat}\iff s{=}8"\ ✗\ \text{（应为 }s\in\{8,16\}\ ✓\text{）};\ \text{"}s\in\{2..14,16\}\text{"\ ✗}$$
$$\textbf{外部约束 ✗}:\ \text{覆盖 ⟹ 否};\ \text{最小性 ⟹ 否} \Longrightarrow \textbf{若欲砍 }s,\ \text{须找\textbf{强于 NP1CC} 的性质（下一步候选见 §3 ✓）}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\text{(甲) }k=A_1=|H_{15}\cap V_\lambda|\ \text{与 }s\ \text{的关系（}s{=}9\Rightarrow k{=}288\ ✓;\ \text{其余待测 ⚠️}）—— 若 }k\ \text{亦由 }s\ \text{决定，则\textbf{整个 }(A_1,A_2)\ \text{由单参数 }s\ \text{决定 ✓✓}}$$
$$\text{(乙) Type 判定：本族皆为 Type C？}\ (k>0\ \text{且伙伴矩 1/2 混合 ✓)\ \Longrightarrow\ \text{与论文 A/B/C 分类对齐 ✓}$$
$$\text{(丙) 更强外部条件候选：Lasserre/DP 型界、puncturing 附加结构、119 特殊参数}\ \text{（119 暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：(甲) External-Cover Gate NO-GO（含最小性实测）、(乙) 3/7 分裂定理、flat 判据再更正（$s\in\{8,16\}$）
- **档案已有（引用，不列为提出）**：A-SAGREE-1、A-CLOSEDFORM-1、A-SUBSPACE-1、内蕴 $\nu$、star 律、$\mathfrak B_1$ 硬门


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 External-Cover Gate 命中文件数=1    :: ./AUDIT-2026-09-27-external-gates-no-go-and-the-3-7-split-theorem.md 
技术词 3/7 分裂定理 命中文件数=1    :: ./AUDIT-2026-09-27-external-gates-no-go-and-the-3-7-split-theorem.md
```
- **本档新增**：(甲) External-Cover Gate NO-GO（含最小性实测）、(乙) 3/7 分裂定理、flat 判据再更正（$s\in\{8,16\}$）（见上方命中数；0 命中者为自造语／内部标签 ✓）
