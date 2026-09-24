已查地图：命中（`S2-ROUND-A2-record-and-C06-C07-hardening` ＋ `AMEND-18`）⟹ Round A 收口 ＋ gap 覆盖点检，不开新案
D0: 本档对象 = **Round A 十条最终判定表** ＋ **三个 `DROP` 失败模板** ＋ **`C06`／`Mt07` 的 gap 覆盖点检结果**
D1: 1（Round A 收口；产出三类 DROP 模板与两项点检判定）
[RESEARCH]

# **Round A 收口 ＋ gap 覆盖点检**

## §1 Round A 十条最终判定（照先生 17:56）

```
$$\begin{array}{c|c|c|l}
\text{ID}&\texttt{G}&A&\text{判定原因}\\
\hline
D03&\texttt{G0}&A?&\text{参数窗口不得从 }STS(v)\le19\ \text{偷补}\\
D04&\texttt{G1}&A0?&\text{exact packing cell，table-completion 风险}\\
D06&\texttt{G1}&A?/A0&\text{数据库覆盖严重，真 gap 需另定}\\
D07&\texttt{G1/G2}&A0?&\text{exact extremal value／extremizer census 可分离}\\
Mt06&\text{—}&\text{—}&\boxed{\text{DROP}:\ \mathrm{Aut}\text{-order distribution 已被 }STS(19)\ \text{分类直接记录}}\\
Mt07&\texttt{G1}&A0?&\text{具体 Ramsey cell 可继续}\\
Mt08&\text{—}&\text{—}&\boxed{\text{DROP}:\ \text{最小 Tutte collision}=6\ \text{已知}}\\
C06&\texttt{G1}^*&A0?&\text{optimal value 已知、census 未知；须一次点检（§3 已做）}\\
C07&\texttt{G1}&A0?&\text{covering radius exact-cell 问题}\\
C09&\text{—}&\text{—}&\boxed{\text{DROP}:\ \text{硬化后只能落入标准 distance spectrum 或 }C06\ \text{census}}\\
\end{array}$$ ✓✓
```

## §2 ⭐ 三个 `DROP` 失败模板（长期资产）

```
$$\textbf{模板①}\ \boxed{Mt06}:\ \text{\textbf{母分类已把 observable 顺手做完}} ——\ STS(19)\ \text{完整分类同时记录了每个设计的 }|\mathrm{Aut}|;\ \text{上界 }v=21\ \text{又吞回整个分类母问题}$$ ✓✓
$$\textbf{模板②}\ \boxed{Mt08}:\ \text{\textbf{最小反例已被明确证明/记录}} ——\ \text{6 元素 rank-3 的那对（两相交三点线 vs 两平行三点线）即"唯一最小对"},\ \mu_T=6\ \text{已知}$$ ✓✓
$$\textbf{模板③}\ \boxed{C09}:\ \text{\textbf{observable 本身无独立性，硬化后必然退化成已有问题}}$$ ✓✓
$$\qquad \text{硬化四版本}:\ \text{可达距离集合／}d_{\max}\text{（＝}A_q(n,d)\ \text{反函数）／每距离非同构码数（＝code census）／单码 distance distribution（＝标准概念）}$$ ✓
$$\Longrightarrow\ \text{统一教训}:\ \boxed{\text{"能定义出来"}\ \ne\ \text{"形成独立数学问题"}}$$ ✓✓✓
$$\text{（三条模板与 }Po02/Gr03/G01/P02\ \text{等并列，均入回归集）}$$ ✓
```

## §3 点检①：`C06`（optimal-code census）—— **线性解读已被覆盖**

```
$$\textbf{点检结果（档级，本轮检索）}:\ \text{存在"optimal binary linear codes of length}\le30\ \text{已\textbf{完全分类}"的结论};\ \text{另有数据库式表：}\ [n,k,3]_2\ (n\le18)\ \text{与 even}\ [n\le19,k,4]_2\ \text{的\textbf{不等价码数表}}$$ ✓✓
$$\text{另有 2025 年工作对 binary/ternary 最大最小距离码做了大量 classification（除少数 inequivalent 数过大的参数集）}$$ ✓
$$\Longrightarrow\ \boxed{\text{若 }C06\ \text{按\textbf{线性}读}:\ \text{目标 census 已被覆盖}\ \Rightarrow\ \texttt{DROP}}$$ ✓✓✓
$$\text{若按\textbf{非线性}读}:\ \text{上表主要覆盖线性码};\ \text{非线性 optimal-code census 是否已被收割\textbf{尚无直接证据} \Rightarrow \text{保留为 }\texttt{G1}^*\ \text{待一次点检}}$$ ⚠️
$$\text{纪律}:\ \text{不得把"linear 已分类"当作"nonlinear 已分类"的证据};\ \text{两者须分开判}$$ ✓✓
```

## §4 点检②：`Mt07`（Ramsey cell）—— **最著名格已被收割**

```
$$\textbf{点检结果（档级）}:\ R(5,5):\ 43\le R(5,5)\le\boxed{46}\ (\text{Exoo 1989 下界};\ \text{Angeltveit–McKay 2024 上界});\ \text{另有 }R(3,k)\ \text{系列计算上界}$$ ✓
$$\Longrightarrow\ \boxed{\text{具体 open cell 存在（}R(5,5)\in[43,46]\text{）};\ \textbf{但属"著名＋算力密集"类} \Rightarrow \text{与早期台账}T\text{-}9/T\text{-}10\ \text{的 REJECT 同类风险}}$$ ✓✓
$$\text{判定}:\ \text{若 }Mt07\ \text{取 }R(5,5)\ \text{格} \Rightarrow \boxed{DROP\ \text{（已收割）}};\ \text{若要继续} \Rightarrow \text{须选\textbf{非著名}格（超图／多色／限制图类 Ramsey）并同做"是否已收割"点检}$$ ✓✓
$$\text{纪律}:\ \text{"有 open cell"}\ \ne\ \text{"有未被收割的 open cell"}$$ ✓✓
```

## §5 Round A 净产出与下一步

```
$$\textbf{DROP 三条}:\ Mt06,\ Mt08,\ C09;\quad \textbf{C06 线性读亦 DROP};\quad \textbf{Mt07 著名格 DROP}$$ ✓✓
$$\text{仍活}:\ D04,\ D06,\ D07,\ Mt07\ (\text{非著名格}),\ C06\ (\text{非线性读}),\ C07$$ ✓
$$\textbf{下一步}:\ \text{对 }D04/D06/D07\ \text{各做一次点检（该格是否已有 exact 值）};\ \text{对 }C06\ \text{做非线性读点检};\ \text{对 }Mt07\ \text{选定非著名格}$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §3/§4 为**外部检索（档级，未逐字核原文）**；§1 依先生 17:56 判定 ✓

## §附 【技术词回查】（补录）
```
技术词 harvested        命中文件数=0    :: 
技术词 template         命中文件数=14   :: ./ALIGN-variable-object-phase-three-level-audit.md ./C84-wall-breaking-phase-positivity-cone-source-enumeration-10-classes-classification-closed.md ./C254-B2-1-FROZEN-CLOSED-registration-and-methodology-template.md 
```
