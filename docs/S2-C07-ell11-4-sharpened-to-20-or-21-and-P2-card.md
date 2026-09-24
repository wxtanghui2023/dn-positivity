已查地图：命中（`S2-C07-dblp-oa-link-all-auto-routes-blocked`）⟹ A/B 窄检索结果 ＋ 收紧 ＋ P2 规格，不开新案
D0: 本档对象 = **路线 A/B 窄检索结果（均未取到值）** ＋ ⭐**结构性收紧：`\ell_2(11,4)\le21` 已由原表精确值给出 ⟹ 节点收紧为"20 或 21"** ＋ **`P2` Source Card（七字段 ＋ 代价估计）**
D1: 1（首次把节点从一个开区间收紧为二值二分；并写出可执行的 P2 规格）
[RESEARCH]

# **`\ell_2(11,4)` 收紧为「20 或 21」＋ `P2` 规格**

## §1 路线 A/B 结果（均未取到值）

```
$$\textbf{路线 A（书内 Table 7.3 转录）}:\ \text{仅见 Davydov 2001 引其作基准（}R{=}4\ \text{项仅 }r\ge19\text{）};\ \text{未见任何免费转录} \Longrightarrow \textbf{未取到}$$ ✗
$$\textbf{路线 B（字面 }l(11,4)\text{）}:\ \text{命中} = \{A(n,d,w)\ \text{类}\}、\{t[n,k]\ \text{表}\}、\{\text{Brouwer 码表}\}\ \text{等}\ \textbf{同形异义};\ \text{无一处给 }\ell(11,4) \Longrightarrow \textbf{未取到}$$ ✗
$$\text{另核}:\ \texttt{neilsloane.com/doc/1218codes.pdf}\ =\ \text{GS-1985 同篇（65 页）},\ \textbf{无 length function 表}（\texttt{length function}\ \text{零命中}）$$ ✗
$$\Longrightarrow\ \boxed{\ell_2(11,4)\ \text{的具体值仍缺}};\ \text{免费路线\textbf{确认穷尽}}$$ ⚠️
```

## §2 ⭐ 结构性收紧（本轮实质收获）

```
$$\text{GS-1985 原表 }k=10\ \text{行（坐标法实读）}:\ N{=}12{:}1,\ 13{:}1,\ 14{:}2,\ 15{:}2,\ 16{:}2,\ 17{:}2\text{-}3,\ 18{:}3,\ 19{:}3a,\ 20{:}3\text{-}4,\ \boxed{21{:}4},\ 22{:}4\text{-}5$$ ✓✓
$$\Longrightarrow\ t_2[21,10]=\boxed{4}\ (\textbf{精确值}) \Longrightarrow \exists\ [21,10]\ \text{码},\ R{=}4 \Longrightarrow \text{协维}=21-10=11,\ \text{长}=21 \Longrightarrow \boxed{\ell_2(11,4)\le21}$$ ✓✓✓
$$\text{叠加}:\ t_2[20,9]=4\text{-}5\ (\text{三份独立表一致}) \Longrightarrow \ell_2(11,4)\le20\ \textbf{未知}$$
$$\Longrightarrow\ \boxed{\text{节点由开区间收紧为二值二分}}:\ \boxed{\ell_2(11,4)\le20}\quad\text{或}\quad\boxed{\ell_2(11,4)=21}$$ ✓✓✓
$$\text{等价形式（全部同值）}:\ \boxed{t_2[20,9]=4\ \text{或}\ 5}\iff\boxed{\exists\,H\in\mathbb F_2^{11\times20}:\ \forall s,\ s=\textstyle\sum_{i\in I}h_i,\ |I|\le4}$$ ✓✓✓
$$\text{另记（弱上界）}:\ t_2[22,11]=4 \Longrightarrow \ell_2(11,4)\le22$$ ✓
```

## §3 `P2` Source Card（七字段，照 `AMEND-15/18`）

```
$$P\ (\text{命题}):\ \boxed{\exists\,H\in\mathbb F_2^{11\times20}\ \text{使}\ \mathbb F_2^{11}\ \text{被}\le4\ \text{项列和覆盖}} \Longrightarrow t_2[20,9]=4$$ ✓✓
$$X\ (\text{对象}):\ \text{20 个列向量 }h_1,\dots,h_{20}\in\mathbb F_2^{11}\setminus\{0\}\ (\text{可重复})$$ ✓
$$K\ (\text{已知}):\ t_2[21,10]=4\ (\text{GS-1985 精确}) \Longrightarrow \ell_2(11,4)\le21;\ \text{三表 }t_2[20,9]=4\text{-}5;\ \text{球覆盖下界 }n\ge16$$ ✓
$$G\ (\text{缺口}):\ \boxed{\text{长度 }20\ \text{处是否有} R{=}4\ \text{的协维 }11\ \text{码}}\ ——\ \text{两侧皆无文献结论}$$ ✓✓
$$A\ (\text{资产}):\ D\ (\text{精确枚举／证书＋独立复核})\ \text{为主};\ G\ (\text{最小反例})\ \text{为辅};\ E\ (\text{结构约束})\ \text{备用}$$ ✓
$$N\ (\text{新量}):\ \text{一个显式 }11\times20\ \text{矩阵（构造侧）或一条不可行性证书（障碍侧）}$$ ✓
$$O\ (\text{外溢}):\ \text{covering-code 表更新};\ \text{不影响其它线}$$ ✓
$$\textbf{计数松动（关键）}:\ \#\{\text{子集}\le4\}=1{+}20{+}190{+}1140{+}4845=\boxed{6196}\ \text{vs}\ \boxed{2048}\ \text{个 syndrome};\ \text{随机 }H\ \text{期望覆盖}\approx 2048(1-e^{-3.03})\approx1949<2048$$ ✓✓
$$\qquad \Longrightarrow\ \text{随机不够，需\textbf{结构化搜索}；但松弛因子 }\approx3\ \text{说明构造\textbf{可能}存在} \Longrightarrow \textbf{P2 第一刀合法}$$ ✓✓
$$\textbf{代价估计}:\ \text{局部搜索（每候选 }O(6196)\ \text{覆盖核验）}\ \text{预计 }\le30\ \text{分钟};\ \text{证书独立复核 }\le5\ \text{分钟};\ \text{无大内存需求}$$ ✓
【⛔ 纪律】 本轮\textbf{零计算}；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B`；**P2 待授权** ✓
【边界】 §2 的 `t_2[21,10]=4` 为**原表实读**；§3 的 6196/2048/1949 为\textbf{实算估计}（随机模型仅作可行性强弱判断，非结论）✓

## §附 【技术词回查】（补录）
```
技术词 covering code    命中文件数=5    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./S2-C07-chainA-closed-chainB-compressed.md ./S2-C07-frontier-compression-and-four-cell-check.md 
技术词 local search     命中文件数=0    :: 
```
