# AUDIT-2026-09-29-INV2 — 第 2 轮：**细节审计**（van Wee 精确无细节空间；可调空间全压在"球 excess 同余层"）

> 空间 B｜非 C 号｜唐先生 23:32「2004 无 AI，必是我们推导里丢了细节；1 格差异只在细节上」｜**不主张任何新值**（V290）

**已查地图**：`AUDIT-28q`（107 公式链 ＋ van Wee 原式逐字）／`AUDIT-29i/j/l/m`（parity 同余三次同型纠错）／`AUDIT-28af`（excess 方法在 103 饱和）
D0: 本档对象 = **档案已有**（van Wee 原式／球 excess 同余）之**逐步审计**（新数学对象：无 ✗）
D1: 0（产出 = **一处新恒等式 ＋ 一处自查纠错 ＋ 细节空间定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① van Wee 一步\ \textbf{精确无细节空间}（n=10 代入 }11{-}\tfrac{10}5\times0.5{=}10\Rightarrow102.4\Rightarrow103\text{，全为精确算术）}}$$
$$\boxed{\text{② 可调空间**全部**压在"excess \textbf{分布} 之同余约束"层（Zhang 1991/92 · Habsieger 1997，且 }n{=}10\equiv4\bmod6\ \textbf{恰在其类内}）}}$$
$$\boxed{\text{③ 该层\ \textbf{已有一条 100\% 实测成立}之同余（球 excess parity：}904/904,\ 120/120\text{）——但方向为\textbf{上界}，非下界}}$$
$$\boxed{\text{④ 本档新导出：}\ \Sigma_{v\notin C}\delta_{N[v]}=11E-4N_{\le2}\ \text{＋\ 全奇 ⟹ }\ \boxed{N_{\le2}\ \le\ (11E-1024+M)/4}\ \text{（}M{=}106\Rightarrow\le161\text{）}}$$

## §1 逐步审计（**无细节错误**）

$$\textbf{(a) 体积项}\ \tfrac{2^{10}}{11}=93.09\ \text{精确}✓;\quad \textbf{(b) van Wee 修正}\ \tfrac{\binom{10}1}{\lceil9/2\rceil}\bigl(\lceil\tfrac{11}2\rceil-\tfrac{11}2\bigr)=\tfrac{10}5\times0.5=1\ \text{精确}✓$$
$$\textbf{(c)}\ \text{分母 }11-1=10\Rightarrow 102.4\Rightarrow\lceil\cdot\rceil=103\ \text{（整性，精确）}✓;\quad \textbf{(d) 反查}\ \texttt{arXiv:2203.16901}\ \text{摘要逐字一致}✓✓$$
$$\therefore\ \text{此三段\textbf{无可挖之处}；107 与 103 之差必在 (e) excess 分布同余层}$$

## §2 该层已知之**正确**同余对象（**三次同型纠错后固化**）

$$\text{Habsieger 之对象是\ \textbf{球 excess}：}\ \delta_{N[v]}:=\sum_{y\in N[v]}\bigl(\mu(y)-1\bigr)\quad(\textbf{非}\ \mu(v)-1)$$
$$\textbf{实测 100\%}:\quad v\in C\Rightarrow\delta_{N[v]}\equiv0\ (120/120 ✓);\qquad v\notin C\Rightarrow\delta_{N[v]}\equiv1\ \text{奇}\ (904/904 ✓)$$
$$\therefore\ \text{对 }v\notin C:\ \delta_{N[v]}\ge1;\ \text{且}\ \Sigma_{x\in V}\Sigma_{y\in N[x]}e(y)=11E\ (3256=11\cdot296 ✓)$$

## §3 本档新导出（**先跑后写 ✓**）

$$\text{由 }\ \Sigma_{x\in C}\Sigma_{y\in N[x]}e(y)=4N_{\le2}\ (796=4\cdot199 ✓)\ \Longrightarrow\ \Sigma_{v\notin C}\delta_{N[v]}=11E-4N_{\le2}\ (2460 ✓)$$
$$\text{与\ "}v\notin C\Rightarrow\delta_{N[v]}\ge1\text{" 合并}:\quad 11E-4N_{\le2}\ \ge\ 1024-M$$
$$\boxed{\therefore\ N_{\le2}\ \le\ \frac{11E-1024+M}4=\frac{122M-11264-1024}{4}=30.5M-3072}\quad(M{=}106:\ \le161)$$
$$\text{判定}:\ 161\ \text{vs 我们已知之下界}\ N_{\le2}\ge71\ \Longrightarrow\ \textbf{无对撞（方向为上界，太弱）}\ ✗\ \text{（与 }AUDIT\text{-}29j\ §4\ \text{同向）}$$

## §4 ⚠️ 自查纠错（**本档第二处**）

$$\text{我曾试图由"918 个奇数之和"推 }M\ \text{之同余}\ (M\equiv2\bmod4) \Longrightarrow \textbf{错误}\ ✗$$
$$\text{根因}:\ \text{918 个奇数之和 mod 4\ \textbf{不被 918 决定}}（1\ \text{与}\ 3\ \text{计数未知）⟹\ 无 }M\text{-同余}\ ✓\ (\text{自查即止})$$

## §5 第 2 轮判定与第 3 轮目标

$$\text{第 2 轮}:\ \textbf{未找到"丢失的细节"};\ \text{但把细节空间\ \textbf{压缩到唯一一层}（球 excess 同余），且该层的已知同余\ \textbf{方向为上界}}✗$$
$$\text{第 3 轮候选（按 }N1/N2/N3\ \text{筛后之唯一存活方向）}:\ \text{把球 excess 同余\ \textbf{与覆盖需求联立}成\ \textbf{双向夹逼}}$$
$$\qquad\text{即：}\ \underbrace{\delta_{N[v]}\ge1\ (v\notin C)}_{\text{下界侧}}\ \text{＋}\ \underbrace{\Sigma_{v\notin C}\delta_{N[v]}=11E-4N_{\le2}}_{\text{预算恒等式}}\ \text{＋}\ \underbrace{\delta\ \text{之局部上界}}_{\textbf{尚缺（即缺失细节候选）}}$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**审计**（含两处自查）✓
- 未取论文原文（R16–17）✓；未重攻 pair（R02）／fiber（R05）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
