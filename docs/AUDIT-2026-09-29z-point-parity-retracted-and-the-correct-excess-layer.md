# AUDIT-2026-09-29z —— **point-excess parity 第二次被推翻；正确层 ＝ ball-excess 聚合；$\texttt{kam.txt}$ 截断冻结**

> **性质**：**审计**（非研究轮）——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B（119/107 线）✓
> **时间**：2026-09-29 15:35 ✓

**已查地图**：`AUDIT-2026-09-29j`（parity 管 ball-excess）／`AUDIT-29k/l`／`DERIVE-107*`✓

D0: 本档对象 ＝ **档案已有**（parity／ball-excess—皆经典 ✓）
D1: 0（产出＝**撤销清单 ＋ 两处实测推翻 ＋ 文件冻结裁定** ⚠️✓）

---

## §0 撤销清单（**全部确认** ✗）

$$\boxed{s(c)\in\{1,3,5,7,9\}\ ✗\ \big|\ r_x=\tfrac{\mu(x)-1}{2}\ ✗\ \big|\ q_c=\tfrac{s(c)-1}{2}\ ✗}$$
$$\boxed{P_1\ge53\ ✗\ \big|\ \sum q+\sum r=18\ ✗\ \big|\ P_2=9+\sum q^2+\sum r^2\ ✗\ \big|\ P_2\ \text{奇}\ ✗\ \big|\ P_1\ge60\Rightarrow\bot\ ✗}$$

$$\textbf{实测（真实覆盖码，}Q_{10}\text{）}:\ \text{码字 }\mu(c):\ \text{偶}42/\textbf{奇}76\ ✗;\quad \text{非码字 }\mu(x):\ \textbf{偶}148/\text{奇}758\ ✗$$
$$\therefore\ \text{两条 parity\ \textbf{均假}};\ \text{依赖它们的一切推论\ \textbf{全部删除}}✓$$

## §1 正确层（**✓ 与档案一致**）

$$\text{Habsieger 之量不是 }\mu(v)-1\text{ 之点态 parity，而是\ \textbf{ball-excess 聚合}}:\ \delta_{N[v]}=\sum_{x\in N[v]}\delta(x)$$
$$\text{文献}:n\equiv0\bmod6\Rightarrow\delta_{N[v]}\ \text{奇偶由 }v\in D\ \text{定};\quad \delta_{N_1[v]}+\delta_{N_2[v]}\equiv0\bmod3$$
$$\therefore\ \boxed{\text{可用的\ \textbf{仅}是 ball-excess 之局部同余，不是 }\mu(v)-1\ \text{自身}}\ ✓\ (\text{与 }\texttt{AUDIT-2026-09-29j}\ \text{一致})$$

## §2 $\texttt{kam.txt}$ 截断（**✓ 原因已定位**）

$$\text{实测}:\ \text{a(10) 段落}\ \mathbf{118}\ \text{词};\ \text{覆盖检验}\ \textbf{12 点未覆盖}\Longrightarrow \text{末 2 词被截断}\ ✗$$
$$\therefore\ \boxed{\texttt{/tmp/kam.txt}\ \textbf{冻结};\ \text{原因＝原始抓取不完整}（5534\ \text{B}\ \text{装不下 }120\ \text{词}）✓}$$
$$\therefore\ \text{本轮由它得出之}\ P_1{=}49,P_2{=}142,P_3{=}875\ \textbf{全部作废}\ ✗$$

## §3 $p{=}11$ 同余之自动性（**✓ 警告成立**）

$$n{=}10\Rightarrow n{+}1{=}11\ \text{素}\Rightarrow p{=}11;\quad \sum_{i=0}^{10}\Delta_i(v)\equiv-1\pmod{11}$$
$$\text{但}\ \sum_{i=0}^{10}\Delta_i(v)=E=11M-2^{10}\ \text{与 }v\ \text{无关},\ \text{且}\ E\equiv-1024\equiv-1\pmod{11}\ \textbf{恒成立}$$
$$\therefore\ \boxed{\text{粗 }p{=}11\ \text{同余\ \textbf{＝恒等式}，不能单独产生 }107}\ ✓$$
$$\Longrightarrow\ \text{须找\ \textbf{低阶局部}同余／线性组合}（\text{非对 }i{=}0..10\ \text{全求和}）✓$$

## §4 仍成立之骨架（**✓**）

$$\boxed{E=11\cdot106-1024=142\ ✓\ \big|\ 2P_1\le142\Rightarrow P_1\le71\ ✓\ \big|\ 2P_2=\sum_c\tbinom{s(c)}2+\sum_{x\notin C}\tbinom{\mu(x)}2\ ✓}$$
$$\text{（}2P_2\ \text{恒等式已于真实码上实测成立}\ ✓✓）$$

## §5 路线裁定（**不作方向决策** ✗，仅陈述状态）

$$\boxed{\text{失败的是\ \textbf{中间桥梁}（point-excess parity），不是 }107\ \text{主线}}$$
$$\text{下一步}:\ \text{重建 }n{=}10\ \text{之 Habsieger／van Wee 局部 excess 不等式}\to\text{转成 }106\text{-cover 之 }P_j\ \text{不等式}\to\ \text{矛盾}$$
$$\text{现状}:\ \textbf{尚无候选不等式};\ \text{且粗同余已证自动}\ ✗$$

## §6 边界（硬 ✓）

- **实测（parity 分布、$2P_2$ 恒等式、$\texttt{kam.txt}$ 覆盖检验）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$\texttt{kam.txt}$ 相关数据**全部冻结** ✓
