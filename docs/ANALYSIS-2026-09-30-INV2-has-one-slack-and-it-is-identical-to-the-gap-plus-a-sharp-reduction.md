# ANALYSIS-2026-09-30-INV2 — INV2 **只有一步松弛**，其 slack **与缺口代数同一**（⟹"近等号分析"循环）；但缺口**收敛到 $A_1\le21$ 区**＋**任何弱局部下界即可闭合**

> 空间 B｜非 C 号｜唐先生 10:10「展开 INV2，逐项找 slack」｜**不主张任何新值**（V290）

**已查地图**：`INV2`／`INV3`／`AUDIT-29j`／`RESULT-M106-DLA`／`REFUTE-2026-09-30c/d`
D0: 本档对象 = **档案已有**（INV2 之推导链）之**逐步展开与 slack 分析**（新数学对象：无 ✗）
D1: 0（产出 = **一条循环性判定 ＋ 一条缺口收敛 ＋ 一条可执行弱靶** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{① INV2 只有\ \textbf{一步} 松弛（每点 }\delta\ge1\text{），无 }\Delta_1..\Delta_k\ \text{可拆}\ ✗}$$
$$\boxed{\textbf{② 其唯一 slack } D:=\sum_{v\notin C}(\delta(v)-1)\ \textbf{与缺口代数同一}:\ N_{\le2}=30.5M-3072-\tfrac D4\ \Longrightarrow\ "D\ \text{之下界}"\equiv"A_2\ \text{之上界}"\ ✗\ (\textbf{循环})}$$
$$\boxed{\textbf{③ 但缺口收敛}:\ A_2\le139\iff m\ \ge\ 44-2A_1\ (m:=\#\{v\notin C:\delta\ge3\})\ \Longrightarrow\ \textbf{只需处理 }A_1\le21\ \text{之区}\ (A_1\ge22\ \text{自动成立})\ ✓}$$
$$\boxed{\textbf{④ 可执行弱靶}:\ \text{实测 }m/(2^n{-}M)\in[0.18,0.96]\ \Longrightarrow\ \textbf{任何 }m\ge c(2^n{-}M)\ \text{且 }c>0.048\ \text{即闭合}\ (4\times\ \text{余量})\ ✓✓}$$

## §1 INV2 之完整链（**逐步**）

$$\textbf{步 1}\ \text{逐点定义球 excess}:\ \delta_{N[v]}=\sum_{y\in N[v]}(\mu(y)-1)\ ✓$$
$$\textbf{步 2}\ \text{恒等式（INV3，1024/1024 ✓✓）}:\ \delta_{N[v]}=11\mathbf1_{v\in C}+2a_1(v)+2a_2(v)-11$$
$$\textbf{步 3}\ v\notin C\Rightarrow\delta=2(a_1+a_2)-11\ (\text{奇});\quad \textbf{步 4}\ \sum_{v\notin C}\delta=11E-4N_{\le2}\ (\text{恒等式})$$
$$\textbf{步 5（唯一的松弛）}\ v\notin C\Rightarrow\delta\ge1 \Longrightarrow 11E-4N_{\le2}\ge2^n-M \Longrightarrow N_{\le2}\le30.5M-3072$$
$$\therefore\ \textbf{INV2}\ \text{＝（恒等式）＋（一步粗界"}\delta\ge1\text{"）};\ \text{无第二/第三步可拆} ✗$$
$$\textbf{slack 之精确式}:\ D:=\sum_{v\notin C}(\delta-1)\ \Longrightarrow\ \boxed{N_{\le2}=30.5M-3072-\tfrac D4}\ \text{（}M{=}106:\ A_2\le161-A_1-\tfrac D4\text{）} ✓$$

## §2 循环性判定（**本档最重要之否定**）

$$\text{"证 }D\ \text{之下界}"\iff\text{"证 }N_{\le2}\ \text{之上界}"\quad(\text{因二者由恒等式相联}) \Longrightarrow \textbf{无独立"稳定性"内容} ✗$$
$$\text{等价地}:\ D=644-4N_{\le2}\ (M{=}106) \Longrightarrow \text{目标 }D+4A_1\ge88\iff N_{\le2}\le139+A_1\iff\mathbf{A_2\le139}\ ✗\ (\textbf{同一命题})$$
$$\therefore\ \textbf{"INV2 近等号/刚性"路线＝重述缺口} \Longrightarrow \text{不能作为第六条独立路线} ⚠️$$

## §3 但缺口收敛（**可入册之真收获 ✓**）

$$A_2\le139\iff 161-A_1-\tfrac D4\le139\iff D+4A_1\ge88;\qquad D\ge2m\ (m:=\#\{v\notin C:\delta\ge3\},\ \text{每点贡献}\ \delta-1\ge2)$$
$$\therefore\ \textbf{充分条件}:\quad \boxed{m\ \ge\ 44-2A_1}\quad\Longrightarrow\quad \textbf{凡 }A_1\ge22\ \text{之情形\ \textbf{自动成立}}\ (44-2A_1\le0\le m) ✓$$
$$\therefore\ \textbf{整个缺口只落在 }A_1\le21\ \text{之区};\ \text{且此时所需 }m\in[2,44]\ \text{（极小）} ✓✓$$

## §4 实测余量（**为何弱靶可行**）

| 量 | 实测范围（8 码） | 目标所需 | 余量 |
|---|---|---|---|
| $D=\sum(\delta-1)$ | $[446,\ 4566]$ | $\ge88-4A_1$ | $\ge5\times$ ✓ |
| $m=\#\{\delta\ge3\}$ | $[82,\ 853]$ | $\ge44-2A_1\in[-122,30]$ | $\ge2.7\times$ ✓ |
| $m/(2^n{-}M)$ | $[0.18,\ 0.96]$ | $>0.048$ 即闭合 | $\ge3.7\times$ ✓ |

$$\therefore\ \textbf{任何形如 }m\ge c\,(2^n-M)\ (c>0.048)\ \text{之局部下界即足够};\ \text{实测最小比 0.18 ⟹ 允许 }c\approx0.05\ ✓✓$$
$$\text{（对照：档案 }AUDIT\text{-}29j\ \text{只得到 }m\ \text{之上界（}m\le322-2N_{\le2}\text{），本档所需为\ \textbf{下界} ⟹ 方向缺失正是缺口）}$$

## §5 建议之下一刀（**可执行**）

$$\textbf{(甲)}\ \text{靶}:\ \text{证 }m\ge\tfrac1{20}(2^n-M)\ (M{=}106\Rightarrow m\ge46)\ \text{——比所需 }44-2A_1\ \text{更简单，且实测留 3.7 倍余量} ✓$$
$$\textbf{(乙)}\ \text{可用之局部材料（未试）}:\ \text{低度码字（}a_1(c){=}0\text{）之邻域必被"远"码字覆盖} \Longrightarrow \text{强制 }a_1{+}a_2\ \text{偏大之点};\ \text{或按 }v\notin C\ \text{之层计数 }(a_1,a_2)\ \text{作双计数}$$
$$\textbf{(丙)}\ \text{判定}:\ \text{若 }(\甲)\ \text{可证} ⟹ A_2\le139 ⟹ \text{闭合}; \text{若连 }m\ge0.05(2^n{-}M)\ \text{都不可得} ⟹\ \textbf{本线整体记 CLOSED-不足（与本档证据一致）}$$

## §6 边界（硬 ✓）

- **不主张**任何新值；本档为**链展开 ＋ 循环性判定 ＋ 缺口收敛**（含一条可执行弱靶）✓
- 未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
