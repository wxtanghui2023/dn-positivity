已查地图：命中（`S2-ROUND-A-status-update-D04-D06-DROP-and-D07-H-pool-check`）⟹ `C07` frontier 压缩 ＋ 四格点检，不开新案
D0: 本档对象 = **`C07` 从 `G1` 压到 `G1^★`（frontier 化）** ＋ **四格 `(19,9),(19,10),(20,9),(20,10)` 点检结果**（本轮未定论；给出决定性下一步）
D1: 1（首次把 Zone-A 活条压成 frontier 集合；产出四格的收割结构图）
[RESEARCH]

# **`C07` frontier 压缩 ＋ 四格点检**

## §1 对象与窗口（照先生，不扩张）

```
$$t_2[n,k]=\min\{R(C):C\ \text{binary linear }[n,k]\};\qquad n\le20,\ k\le10$$ ✓
$$\textbf{等价刻画（可证书化）}:\ H\in\mathbb F_2^{(n-k)\times n};\quad R(C)=\min\{r:\forall s\in\mathbb F_2^{n-k},\ s=\textstyle\sum_{i\in I}h_i,\ |I|\le r\}$$ ✓✓
$$\Longrightarrow\ \text{固定 }(n,k)\ \text{后＝有限列集覆盖问题}\ \Longrightarrow\ \textbf{可机器完备验证}$$ ✓✓
```

## §2 已收割区域（本轮点检，档级）

```
$$k=4,5:\ \text{Graham–Sloane 给出整个 }t[n,4],\ t[n,5]\ \text{的精确理论（非零散小格）}$$ ✓✓
$$k=6:\ \text{Baicheva–Bouyukliev 给出所有 }n\ \text{的 }t_2[n,6];\ \text{并分类 }k\le6,n\le15\ \text{的达到码};\ \text{后续用项目码做到 }n=19$$ ✓✓
$$\text{已收割高维小格}:\ t_2[17,6]=5,\ t_2[17,8]=4,\ t_2[18,7]=5,\ t_2[19,7]=5,\ t_2[20,8]=5\ (\text{Baicheva–Vavrek 2003, 经 covering-radius 分类证明})$$ ✓✓
$$k\le5,n\le14:\ \text{normality/complete-radius 结构理论};\ n\le18\ \text{或 redundancy}\le10\ \text{的 normality 结果}$$ ✓
$$\Longrightarrow\ \boxed{n\le20,k\le10\ \text{绝不能当"大片未知 exact table"}}$$ ✓✓
```

## §3 但 `C07` 不能 `DROP`（缺口在语言层面）

```
$$\text{现有文献\textbf{未给出} }n\le20,k\le10\ \text{全矩阵 }t_2[n,k]\ \text{已完成的证据};\ \text{高维区域仍以 bounds/constructions 表述}$$
$$\text{例}:\ t_2[n,8]\le\left\lfloor\frac{n-10}{2}\right\rfloor\ (n\ge16);\quad k=9\ \text{亦为上界型表述}$$ ✓
$$\Longrightarrow\ \boxed{C07:\ G1\to G1^\star},\quad \mathcal P_{\rm frontier}=\{(n,k):n\le20,k\le10,\ t_2[n,k]\ \text{尚未被现有 exact result 确认}\}$$ ✓✓
$$\text{区域分层}:\ k=4,5\ \text{收割};\ k=6\ \text{收割};\ k=7\ \text{部分收割（}n=18,19\text{）};\ k=8\ \text{部分收割（}n=17,20\text{）};\ \boxed{k=9,10\ \text{仍存未确认 exact 的格}};\ k=7,8\ \text{其余 }n\le20\ \text{待逐格}$$ ✓✓
```

## §4 四格点检结果（本轮）—— **未定论；但给出决定性下一步**

```
$$\text{本轮检索\textbf{未取得} }t_2[19,9],t_2[20,9],t_2[19,10],t_2[20,10]\ \text{的 exact 值或明确 open 声明}$$ ⚠️
$$\textbf{但发现三条结构性事实}:$$
$$\qquad (i)\ \textbf{存在 }t[n,k]\ \text{总表}:\ \text{Graham–Sloane 1985 综述}\ \text{Appendix B}\ \text{给出 }n\le32,k\le25\ \text{的 }t[n,k]\ \text{表（exact 处给 exact，其余给 bounds）}$$ ✓✓
$$\qquad (ii)\ \text{Baicheva–Vavrek 2003 的 "small lengths" 只证到 }k\le8\ (\text{即 }(17,6),(17,8),(18,7),(19,7),(20,8)\text{)};\ \textbf{未覆盖 }k=9,10$$ ✓✓
$$\qquad (iii)\ \text{2025 年仍有 "New upper bounds for binary linear covering codes"（长度函数 }\ell_2(r,R)\ \text{方向）}\Longrightarrow \textbf{该区域仍在活跃推进、未饱和}$$ ✓✓
$$\Longrightarrow\ \textbf{决定性下一步}:\ \text{查 \textbf{总表}（Graham–Sloane Appendix B／Cohen–Honkala–Litsyn–Lobstein《Covering Codes》表）中这四格的取值：}$$
$$\qquad \text{若四格表值皆为 exact} \Longrightarrow \boxed{C07=\mathrm{DROP}};\quad \text{若至少一格为 }L<U \Longrightarrow \text{该格升 }\boxed{G2\ \text{candidate}}\ \text{（可直接机器验证）}$$ ✓✓✓
```

## §5 状态与含义

```
$$\boxed{C07:\ G1^\star\ (\mathcal P_{\rm frontier}\ \text{已定义};\ \text{四格＝第一优先点检对象})};\quad \textbf{本轮不写死 }(20,9)\ \text{为 open}$$ ✓
$$\textbf{与 Zone-A 其它条的形态差异（重要）}:\ \text{本条不是"补格"},\ \text{而是"}\textbf{高维 frontier }\pm\textbf{ 证书}"\ ——\ \text{目标量单一（一个整数）、可完备验证、且社区仍在推进}$$ ✓✓
$$\text{故 }C07\ \text{是 Zone-A 中唯一"既非已收割、又非规格未闭合"的活条};\ \text{但仍须先过总表这一关}$$ ✓✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §2–§4 为**外部检索（档级，未逐字核原文）**；§4 的"未定论"是\textbf{诚实标注}而非结论 ✓

## §附 【技术词回查】（补录）
```
技术词 frontier         命中文件数=51   :: ./CEILING-LP-RECOMPUTE-results.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./E55-G1-closed.md 
技术词 harvested        命中文件数=2    :: ./S2-ROUND-A-CLOSURE-and-gap-coverage-spot-check.md ./S2-ROUND-A-status-update-D04-D06-DROP-and-D07-H-pool-check.md 
```
