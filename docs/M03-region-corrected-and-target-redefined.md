已查地图：命中（`M03-SPEC-CLOSURE-and-N5-first-assembly` ＋ `AMEND-19`）⟹ `M03` 区域纠偏与目标重定义，不开新案
D0: 本档对象 = ⭐**文献纠偏**（`M03-B` ≡ `CLOSED`）＋ **`n=5` 区域表的显式化（含 2026 年新不可能区 `W`）** ＋ **目标区重定义为 `R\setminus W`** ＋ **`K_5` 待显式化清单** ＋ **收割风险判定与 `P1/P2` 重设计**
D1: 1（首次把 `M03` 的开放区用文献形式精确写出；产出"当前真正剩区"的显式定义）
[RESEARCH]

# **`M03` 区域纠偏：开放区现为 `R\setminus W`**

## §1 `M03-B` 已 `CLOSED`（文献完全解决）

```
$$\textbf{Spector 2011}:\ \text{trace-zero}\ 5\times5\ \text{SNIEP}\ \textbf{完全刻画};\ \text{在 }s_1=0\ \text{下可实现}\iff\boxed{\lambda_2+\lambda_5\le0\ \text{且}\ s_3\ge0}\ (\text{连同 Perron})$$ ✓✓（档级：先生检索）
$$\Longrightarrow\ \boxed{M03\text{-}B=\mathcal S_5^0\ \textbf{CLOSED}};\ \text{不得再作为开放攻击面}$$ ✓✓
$$\textbf{我方 \S 前档的 }s_3=6\sum_{i<j<k}a_{ij}a_{jk}a_{ki}\ge0:\ \textbf{不构成新 }P1\ —— \text{它正是已知完整判据中的一条}$$ ✓✓（登记为**机制解释**，非新结果）
```

## §2 ⭐ `n=5` 区域表（显式，档级）

```
$$\textbf{已完全解决区}:\quad \text{(i) }s_1=0\ (\text{Spector 2011});\quad \text{(ii) }S\ge\lambda_1/2\ (\text{Loewy–Spector 2017});\quad \text{(iii) }\le2\ \text{正特征值（分成主化／迹条件）};\ \text{(iv) }\lambda_3\le S$$ ✓✓
$$\textbf{⭐ 残区（Johnson–Marijuán–Pisonero 2017/2018 ＋ Jin–Ke–Sui 2026 形式化）}:\ S:=\textstyle\sum_i\lambda_i=\operatorname{tr}A$$
$$\qquad \boxed{R=\bigl\{\lambda:\ \lambda_1=\max_i|\lambda_i|,\ \lambda_1>\lambda_2\ge\lambda_3>0>\lambda_4\ge\lambda_5,\ 0<S<\min\{\lambda_3,\ \lambda_1/2\}\bigr\}}$$ ✓✓✓
$$\qquad \text{即：}\textbf{恰 3 正 2 负}\ \text{＋ 低迹}\ (\text{因 }\le2\ \text{正已解决};\ S<\lambda_3\ \text{与 }S<\lambda_1/2\ \text{两个限制叠加})$$
$$\textbf{⭐ 2026 年新不可能区（}Jin\text{–}Ke\text{–}Sui,\ arXiv{:}2608.19435,\ 2026\text{-}08\text{-}21\text{）}:\quad \boxed{W=\{\lambda\in R:\ 4\lambda_1\le 9\lambda_3-S\}}\ \Longrightarrow\ \textbf{不可实现}$$ ✓✓✓
$$\qquad \text{方法}:\ \text{对角移位 }c=\tfrac{\lambda_3-S}{4}>0,\ B=A+cI_5\ \text{把问题推到\textbf{临界高迹边界}};\ \text{再把交换矩阵约化为}\textbf{加权五环};\ \text{由其特征多项式／谱恒等式导出矛盾}$$ ✓✓
$$\Longrightarrow\ \boxed{\textbf{当前真正开放区}=\ R\setminus W=\bigl\{\lambda\in R:\ 4\lambda_1>9\lambda_3-S\bigr\}}$$ ✓✓✓
$$\text{归一化 }\lambda_1=1:\ R=\{1>\lambda_2\ge\lambda_3>0>\lambda_4\ge\lambda_5,\ 0<S<\min(\lambda_3,\tfrac12)\};\quad W=\{S\le9\lambda_3-4\}$$ ✓
```

## §3 `K_5`（充分族）待显式化清单

```
$$\text{清单（须写成\textbf{不等式区域}才能求差集）}:\ \text{Soules};\ \text{Laffey–Šmigoc};\ \text{Fiedler};\ \text{Soto};\ \text{递归构造（}Ellard\text{–}Šmigoc\ \text{框架）}$$ ✓
$$\text{关键文献}:\ \text{Marijuán–Pisonero, “A Map of Sufficient Conditions for SNIEP”}\ (\text{免费 PDF，}singacom.uva.es);\ \text{其中建立各充分条件间的\textbf{包含／独立关系}$$ ✓✓
$$\text{另}:\ \text{Johnson–Marijuán–Pisonero 2016 “Ruling out certain 5-spectra”}\ \text{给出残区的早期刻画（}\lambda_1+\lambda_2+\lambda_4+\lambda_5<0\ \text{型条件）}$$ ✓
```

## §4 差集判定（`③`）

```
$$\mathcal U^{\rm rem}\setminus\bigcup_j K_{5,j}\ \overset{?}{=}\ \emptyset? \Longrightarrow\ \textbf{非空}:\ R\setminus W\ \text{存在（否则 }n=5\ \text{已解决};\ 2026 论文只\textbf{吃掉}了 }W$$ ✓✓
$$\textbf{但"非空"}\ne\textbf{"未被攻击"}:\ \boxed{\textbf{收割风险高}} —— \text{证据}:$$
$$\qquad \text{(a) }2026\text{-}08\ \text{有一篇专门论文在\textbf{同一低迹区}给出新不可能区};\quad \text{(b) 该线由统计／矩阵分析专业组持续推进（}Jin\ \text{的 }NMF/NIEP\ \text{系列};\ Loewy/Spector/Šmigoc\ \text{等）};$$
$$\qquad \text{(c) 2016/2017/2018/2021/2026 连续产出}\ \Longrightarrow \textbf{活跃收割中}$$ ✓✓
$$\Longrightarrow\ \textbf{不能把 }R\setminus W\ \text{当"无人区"};\ \text{但它是\textbf{显式、可证书化}的开放区} \Longrightarrow \text{仍可置入 }KEEP\ \text{但须重定义攻击点}$$ ✓✓
```

## §5 `M03` 状态与 `P1/P2` 重设计

```
$$\boxed{M03=\textbf{KEEP（重新定义攻击区）}},\quad \text{攻击区}=\boxed{R\setminus W}\ (\text{归一化后显式})$$ ✓✓
$$\textbf{⚠️ 纠偏}:\ \text{原 }M03\text{-}B\ (\text{trace-zero})\ \Longrightarrow\ \boxed{\textbf{DROP/CLOSED}};\ \text{原 }s_1\ge\tfrac12\ \text{大片}\Longrightarrow\ \boxed{\textbf{去除（已完全刻画）}}$$ ✓✓
$$P2\ (\textbf{构造侧，我方强项}):\ \text{在 }R\setminus W\ \text{内取\textbf{有理参数族}}\ \lambda(t),\ \text{给出 }A(t)=A(t)^{\mathsf T}\ge0\ \text{使 }\chi_{A(t)}=\prod_i(x-\lambda_i(t))\ \Longrightarrow\ \textbf{精确可复核证书}$$ ✓✓✓
$$\qquad \text{意义}:\ \text{若成功}\ \Longrightarrow\ \text{(i) 证 }R\setminus W\ne\emptyset\ \text{（可实现侧）};\ \text{(ii) }\textbf{标定 }W\ \text{的边界紧性}\ (\text{是否存在贴边的可实现点})$$ ✓✓
$$P1\ (\text{障碍侧，门槛高}):\ \text{扩张 }W\ \text{（即证明更大子区不可实现）} —— \textbf{需与 }2026\ \text{年那套"移位＋加权五环"机制竞争};\ \text{我方无现成优势}$$ ⚠️
$$\Longrightarrow\ \textbf{建议}:\ \text{优先 }P2;\ P1\ \text{仅在 }P2\ \text{给出边界信息后再定}$$ ✓✓
```

## §6 下一步（严格按 ①→③）

```
$$\boxed{\text{①}}\ \text{已做（}\S2\ \text{区域表：含 }R\ \text{与 }W\ \text{的显式形式}）$$ ✓✓
$$\boxed{\text{②}}\ \text{取 Marijuán–Pisonero 2017 免费 PDF},\ \text{把各充分族 }K_{5,j}\ \text{写成\textbf{不等式区域}};\ \text{一并取 Johnson–Marijuán–Pisonero 2016 的残区刻画}$$ ✓✓
$$\boxed{\text{③}}\ \text{求 }(R\setminus W)\setminus\bigcup_j K_{5,j}:\ \text{若为空}\Rightarrow M03\ \textbf{DROP};\ \text{若非空}\Rightarrow \text{取其中最"贴边"的切片作 }P2\ \text{目标}$$ ✓✓
$$\boxed{\text{④}}\ \text{切片钉死后才动计算（}P2\ \text{构造＋证书）}$$ ✓
【⛔ 纪律】 本轮\textbf{零计算}；`U_{2,3}` 暂停；**不回 RH**；`C07` 已封口 ✓
【边界】 `\S2` 的 }R$$／`W\ \text{形式来自 2026 论文\textbf{原文实读}（已入档 }sources/Jin\text{-}Ke\text{-}Sui\text{-}2026\dots.pdf$$）；`Spector 2011`／`Loewy–Spector 2017`／`Loewy 2021` 为\textbf{档级（经 2026 论文复述 ＋ 先生检索）} ✓

## §附 【技术词回查】（补录）
```
技术词 residual region  命中文件数=0    :: 
技术词 impossibility    命中文件数=7    :: ./RH-prior-NOGO-checklist-2026-09-09.md ./ZF-3-minimal-arithmetic-input-audit.md ./ASSETS-REGISTRY.md 
```
