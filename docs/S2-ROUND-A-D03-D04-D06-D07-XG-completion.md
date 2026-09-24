已查地图：命中（`S2-HANDOFF-zone-members-and-count-fix` ＋ `AMEND-18`）⟹ 本档为 Round A 第一组 X/G 补全，不开新案
D0: 本档对象 = **Zone-A 前四条（`D03,D04,D06,D07`）的 `X/G` 五元组补全** ＋ ⚠️**Zone-B `SPEC` 口径锁定（=8）**
D1: 1（首次把短命题补成可筛五元组；产出 SPEC 口径修正）
[RESEARCH]

# **Round A（第一组）：`D03 / D04 / D06 / D07` 的 X/G 补全**

## §0 ⚠️ 先核 `Zone-B` 的 `SPEC` 口径（我给的 9 与先生的 7 都不对 → **8**）

```
$$\textbf{逐条重数（Zone-B=16 条）}:\ \{M01,M02,M06,Au03,Au04,Au05,Au07,Au08\}=\mathbf{8}$$ ✓✓
$$\qquad \text{非 }\texttt{SPEC}\ \text{的 }8\ \text{条}:\ \{M03,M04,Au06,G01,G02,G05,G06,G08\}$$ ✓
$$\Longrightarrow\ \boxed{N=16,\quad \texttt{SPEC}=8,\quad U_{\rm research}=16-8=8}$$ ✓✓✓
$$\textbf{我此前写 9 有误};\ \text{先生数到 7 亦差 1};\ \textbf{以逐条为准 = 8};\ \text{待先生确认后锁定}$$ ⚠️
```

## §1 `D03`：给定参数非同构设计个数

```
$$\mathcal O:\ \text{两两非同构的 }2\text{-(v,k,}\lambda\text{) design 同构类集合}\ \mathcal D(v,k,\lambda)$$ ✓
$$\mathcal P:\ \textbf{未锁定} —— \text{"给定参数"不是窗口};\ \text{须指定具体 }(v,k,\lambda)\ \text{单一格}$$ ✗
$$\mathcal I:\ \#\{\text{iso classes}\}\ \text{（整数）};\ \text{可选升级：全部 iso classes 的完整列表}$$ ✓
$$\mathcal G:\ \text{STS(}v\text{) 计数已完成到 }v\le19\ (\text{Kaski–Östergård});\ \text{更广 }(v,k,\lambda)\ \text{格有分散结果与数据库};\ \textbf{本候选未指明哪一格未定}$$ ⚠️
$$\mathcal T:\ \text{canonical augmentation 枚举 ＋ 完备性证书（同构去重正确性可独立复核）}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G0}}\ (\text{窗口未闭合};\ \text{须先选定具体 }(v,k,\lambda)\ \text{且须证其未被 }STS\le19\ \text{型结果覆盖})$$ ✓✓
$$\text{Zone-A 归类（暂）}:\ \texttt{A?};\ \text{若选定格后仅为补格} \Rightarrow \texttt{A0}$$
```

## §2 `D04`：`2-(v,k,λ)` packing 数表缺口

```
$$\mathcal O:\ \text{packing}\ (V,\mathcal B)\ \text{with}\ \mathcal B\ \text{为 }k\text{-子集族},\ \text{每 }2\text{-子集}\le\lambda\ \text{次}$$ ✓
$$\mathcal P:\ \textbf{可锁定}:\ k=4,\ \lambda=1,\ v\le20\ (\text{或 }k=3,\ \lambda=1)\ \text{的有限格}$$ ✓
$$\mathcal I:\ D(v,k,\lambda):=\max|\mathcal B|\ \text{（精确整数）};\ \text{可选：极值 packing 的 iso 类数}$$ ✓
$$\mathcal G:\ \text{手册/文献已给大量 }D(v,k,\lambda)\ \text{的精确值与界};\ \textbf{缺口＝具体未定格（须逐格指出）}$$ ⚠️
$$\mathcal T:\ \text{SAT/ILP 穷举 ＋ 上界证书（对偶可行解）};\ \text{达到者枚举须同构去重}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G1}}\ (\text{窗口可闭合};\ \text{但 }\mathcal G\ \text{须落到单一格})$$ ✓
$$\text{Zone-A 归类（暂）}:\ \boxed{\texttt{A0}\ \text{倾向}}\ (\text{"补表"}风险高};\ \text{除非该格的极值结构本身产生新现象)$$ ⚠️
```

## §3 `D06`：给定参数差集存在性小例分类

```
$$\mathcal O:\ (v,k,\lambda)\text{-difference set}\ D\subseteq G\ (\text{首选 }G\ \text{循环})$$ ✓
$$\mathcal P:\ v\le100\ \text{或指定 }\lambda\ \text{与小 }v\ \text{窗口};\ \textbf{须锁定，不可"小例"}$$ ✓
$$\mathcal I:\ \text{存在性（}\exists/\nexists\text{）};\ \text{可选升级：等价类完全分类}$$ ✓
$$\mathcal G:\ \textbf{关键事实}:\ \text{difference-set 数据库已按 }(v,k,\lambda)\ \text{给出 exists/all known/does not exist/open（覆盖 }v<100000\text{）}$$ ✓✓
$$\Longrightarrow\ \text{"存在性表"}\ \textbf{基本已是现成输出};\ \text{真正缺口只剩两类}:\ (i)\ \text{数据库标 open 的格};\ (ii)\ \lambda=1\ \text{的非存在性（Singer 型开放）}$$ ✓✓
$$\mathcal T:\ (i)\ \text{构造搜索（群环/特征方法）；}(ii)\ \text{非存在性需数论/代数障碍（非枚举可解）}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G1}}\ (\text{但见 }\mathcal G:\ \text{两类缺口性质差别极大})$$ ✓
$$\text{Zone-A 归类（暂）}:\ \boxed{\texttt{A?}\ \text{或 }\texttt{A0}}\ ——\ \text{若攻 open 格} \Rightarrow \text{易退化为补数据库};\ \text{若攻 }\lambda=1\ \text{非存在性} \Rightarrow \text{非我方资产型（非枚举）}$$ ⚠️
```

## §4 `D07`：Turán 型小超图极值数未收割格

```
$$\mathcal O:\ \text{3-uniform 小超图 }H\ \text{的 extremal family};\ \text{ex}(n,H)=\max|E|$$ ✓
$$\mathcal P:\ \textbf{可锁定}:\ \text{固定小 }H\ (\text{如 }K_4^{(3)},F_5)\ \text{与 }n\le20\ \text{窗口}$$ ✓
$$\mathcal I:\ \text{两级}:\ (i)\ \text{ex}(n,H)\ \text{的精确值};\ (ii)\ \text{极值构型的同构类计数（extremizer census）}$$ ✓✓
$$\mathcal G:\ \text{已有一批小参数 exact values 与区间 bounds（如某些 }T(n,6,4)\text{）};\ \text{缺口＝未收割格的 exact value／extremizer census}$$ ⚠️
$$\mathcal T:\ \text{SAT/ILP 定 exact value ＋ 对偶证书};\ \text{extremizer census 须同构去重（nauty）}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G1}\ \text{或}\ \texttt{G2}}\ (\text{SAT 入口明确};\ n\le20\ \text{规模可控})$$ ✓
$$\text{Zone-A 归类（暂）}:\ \boxed{\texttt{A0}\ \text{倾向}}\ (\text{exact value 多为补格};\ \textbf{但 extremizer census 可能产生结构现象} \Rightarrow \text{须分开记})$$ ✓✓
$$\textbf{纪律}:\ \text{extremal value}\ \ne\ \text{extremizer census}\ \ne\ \text{non-isomorphic extremizer census};\ \text{不得混算}$$ ✓✓
```

## §5 本轮小结与下一步

```
$$\text{四条状态}:\ D03=\texttt{G0};\quad D04=\texttt{G1};\quad D06=\texttt{G1};\quad D07=\texttt{G1/G2}$$ ✓
$$\text{四条暂归}:\ D03\ \texttt{A?};\quad D04\ \texttt{A0};\quad D06\ \texttt{A?/A0};\quad D07\ \text{exact-value }\texttt{A0}\ +\ \text{census 待评}$$ ✓✓
$$\textbf{共性风险}:\ \text{四条都有"回到补格"的引力};\ \text{分水岭＝}\ \boxed{\text{缺口完成后是否产生\textbf{超出补表}的数学内容（结构现象／新不变量／一般模式）}}$$ ✓✓✓
$$\text{下一步（照先生）}:\ \text{继续 Round A 余下 6 条}\ (Mt06,Mt07,Mt08,C06,C07,C09)\ \to\ \text{再 }A+/A0/A?/AX$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §0 为口径修正（待确认）；§1–§4 的文献状态为**档级**（先生本轮检索）✓

## §附 【技术词回查】（补录）
```
技术词 schema           命中文件数=12   :: ./RIGOR-AUDIT-1-three-candidates-rigor-audit-and-V248-selected.md ./RESEARCH-CONSTITUTION.md ./RH-MODEL-FIRST-ENTRY-ROUTING.md 
技术词 extremizer       命中文件数=8    :: ./V313-optimality-theorem-audit-A-in-E-missing.md ./S2-ROUND-A-D03-D04-D06-D07-XG-completion.md ./RESEARCH-CONSTITUTION.md 
```
