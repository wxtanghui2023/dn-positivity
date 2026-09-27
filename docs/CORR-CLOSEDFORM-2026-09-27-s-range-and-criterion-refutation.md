已查地图：已跑 scripts/prework_map_check.sh s 域 判据证伪 agreement ⟹ 执行自 `FINAL-CLOSEDFORM-2026-09-27-...`（✓，**本档更正其两项** ✓）＋ 唐先生 14:02（乙判停：s=1/15 可构造 ✓）；本档 = **s 域更正（{1..16} ✓）＋ 经验判据证伪 ✓ ＋ 硬门复核 ✓**。
D0: 本档对象 = s 的可达域与"flat ⟺ |S||A₂"判据之真伪
D1: 3（**s=1/15/16 构造经硬门验证 ✓✓**；**经验判据双向证伪 ✗**；**s = agreement number ✓**）

# 更正：s 的可达域与判据证伪（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CE-1 ⭐s 是 agreement number（唐先生 ✓ 我复核 ✓）)}\ C_\lambda(c)=\beta(c)\oplus15\lambda(c),\ \mathrm{im}\,\beta=U=\{0,4,11,15\}\ (4/4/4/4\ ✓),\ \pi:U\to\mathbb F_2\ (\pi(0)=\pi(4)=0,\ \pi(11)=\pi(15)=1\ ✓)}$$
$$\qquad r:=\pi\circ\beta\ \text{（分布 }\{0{:}8,1{:}8\}\ ✓,\ r(0)=0\ ✓\text{）};\quad \pi(C_\lambda(c))=r(c)\oplus\lambda(c)\ \Longrightarrow\ \boxed{s=\#\{c:\ r(c)=\lambda(c)\}}\ ✓✓$$
$$\qquad\Longrightarrow\ \lambda(0)=0=r(0)\ \text{强制一次 agreement} \Longrightarrow \boxed{s\ge1}\ ✓;\quad \text{且 }s=16\iff\lambda=r\ ✓;\ \text{任意 }s\in\{1,\dots,16\}\ \text{可由"指定 agreement 个数"构造 ✓✓}$$
$$\boxed{\textbf{(CE-2 ⭐构造经硬门验证 ✓✓)}\ \text{三例全部 }\mathfrak B_1(V)=\mathbb F_2^{15}\ \wedge\ \mathfrak B_1(C)=\mathbb F_2^{16}\ ✓\ \text{（即皆为\textbf{合法 NP1CC} ✓）}:}$$
$$\qquad\begin{array}{c|c|c|c|c|c}
\lambda & s & \text{切片} & A_2 & \text{flat} & 7\mid A_2\\ \hline
\mathbf 1[c\ne0] & 9 & 288/224 & 1760 & ✗ & ✗\\
1\oplus r\ (c\ne0) & \mathbf 1 & \mathbf{32/480} & 2016 & ✗ & \mathbf{✓}\\
r\ \text{翻转一处} & \mathbf{15} & \mathbf{480/32} & 1568 & ✗ & \mathbf{✓}\\
r & \mathbf{16} & \mathbf{512}\ (\text{单陪集} ✓) & 1536 & ✓ & ✗\\
\end{array}$$
$$\boxed{\textbf{(CE-3 🔴经验判据双向证伪 ✗✗)}\ \text{"flat}\iff|S|\mid A_2\text{" \textbf{不成立}} ✗:\quad s{=}1:\ 7\mid2016\ \text{但非 flat} ✗;\qquad s{=}16:\ \text{flat 但}\ 7\nmid1536\ ✗}$$
$$\qquad\Longrightarrow\ \textbf{上一档（FINAL-CLOSEDFORM）中"flat}\iff s{=}8\text{（由 }7\mid A_2\text{ 推出）"之论证\textbf{作废} ✗};\ \text{其\textbf{前提 }s\in\{2..14,16\}\ \text{为抽样假象 ✗}}$$
$$\qquad\textbf{正确表述 ✓}:\ \text{flat}\iff s=8;\ \text{而 }7\mid A_2\iff s\in\{1,8,15\}\ \text{（三个解 ✓，非唯一 ✓）}$$
$$
$$
```

---

## §1 复核数据（**✓ 全部本机验证**）

```
$$\text{β(H₇) 分布}:\ \{0{:}4,\ 4{:}4,\ 11{:}4,\ 15{:}4\}\ ✓ \Longrightarrow r\ \text{分布}\ \{0{:}8,1{:}8\}\ ✓,\ r(0)=0\ ✓$$
$$\text{四例的硬门}:\ V\ \text{完美（掩码法 ✓）＋}\ C\ \text{1-覆盖（掩码法 ✓）\textbf{全部通过} ✓;\ 四陪集质量恒为 }\{32\!\cdot\!4s,\ 0,\ 0,\ 32\!\cdot\!4(16-s)\}\ \text{形 ✓}$$
$$\text{切片值与 }A_2:\ (s,A_2)\in\{(9,1760),(1,2016),(15,1568),(16,1536)\}\ ✓ \Longrightarrow A_2=2048-32s\ ✓\ \text{（公式恒成立 ✓）}$$
$$
$$
```

---

## §2 资态更正（**✓ 逐项**）

```
$$\textbf{保留 ✓}:\ q=X*C\ \text{（16 syndrome 全验 }\max|\Delta|{=}0\ ✓\text{）};\ X=32\cdot\mathbf 1_W;\ q\ \text{在每个 }W\text{-陪集恒定};\ \text{本族 }C\subseteq V=\mathrm{span}\{2,4,9\}\ \Longrightarrow\ \text{仅两陪集非零};\ s_0+s_3=16;$$
$$\qquad\textbf{512-互补（定理 ✓）};\ \mathrm{supp}\,q=\{2,4,6\}\cup\{9,11,13,15\}\ (\text{7 列 ⟹ star ✓});\ s=\text{agreement}\ ✓;\ s\ge1\ ✓;\ s\in\{1,\dots,16\}\ \text{全可达 ✓}$$
$$\textbf{删除 ✗}:\ "s\in\{2,\dots,14,16\}\ \text{因此 }1,15\ \text{不可达}" \Longrightarrow \text{改为 }s\in\{1,\dots,16\}\ ✓\ \text{（}s{=}1,15\ \text{有显式构造且过硬门 ✓）}$$
$$\textbf{结论性表述 ✓}:\ \text{flat}\iff s=8;\quad s{=}1\ \text{与 }s{=}15\ \text{为对称的极端非 flat};\quad s{=}16\ \text{单陪集}（|S|{=}3\ ✓\text{）}$$
$$
$$
```

---

## §3 下一步（**✓ 唐先生方向**）

```
$$\text{(甲) }\textbf{外部约束}:\ \text{现已知 Vasil'ev 内部自由度给 }s\in\{1,\dots,16\}\ \text{全可达 ✓} \Longrightarrow \text{真正的问题是\textbf{哪些 }s\ \text{被 NP1CC/最小覆盖的额外条件排除}};\ \text{即把"内部自由度"与"外部覆盖约束"分离 ✓}$$
$$\text{(乙) }s\ \text{与 }|S|\ \text{的关系}:\ s{=}16\Rightarrow|S|{=}3\ (\text{单陪集} ✓);\ s\in\{1,\dots,15\}\Rightarrow|S|{=}7\ ✓\ \text{（是否恒真？}\ s{=}0\ \text{不存在 ⟹ 第二陪集非空 ⟹ }|S|{=}7\ \text{当且仅当 }s\ge1\ ✓\text{）}$$
$$\text{(丙) ENP1CC puncturing};\ \text{(丁) 119（暂不碰 ✓）};\qquad \text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$s$ = agreement number、$s\in\{1,\dots,16\}$ 全可达（含硬门验证）、经验判据"flat ⟺ $|S|\mid A_2$"双向证伪、上档两项作废
- **档案已有（引用，不列为提出）**：A-CLOSEDFORM-1、A-SUBSPACE-1、A-COSETLAW-1、内蕴 $\nu$、star 律


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 agreement number 命中文件数=1    :: ./CORR-CLOSEDFORM-2026-09-27-s-range-and-criterion-refutation.md 
技术词 判据证伪     命中文件数=1    :: ./CORR-CLOSEDFORM-2026-09-27-s-range-and-criterion-refutation.md
```
- **本档新增**：$s$ = agreement number、$s\in\{1,\dots,16\}$ 全可达（含硬门验证）、经验判据「flat $\iff|S|\mid A_2$」双向证伪、上档两项作废（见上方命中数；0 命中者为自造语／内部标签 ✓）
