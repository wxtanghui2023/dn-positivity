已查地图：已跑 scripts/prework_map_check.sh 分类数据 n≤8 R=1 Östergård 数据 ⟹ 执行自 PINNING-2026-09-26-step1-step2-audit 档；本档为**数据接口探测的负结果登记**（唐先生 2026-09-26 09:55 指令）；不开新方向 ✓。
D0: 本档对象 = 2000 年分类论文的（n≤8, R=1）代表码数据定位（非新对象）
D1: 0（无新自由度；产出为负结果台账，防重复劳动 ✓）

# PINNING-DATA-HUNT-2026-09-26 · 负结果登记

## §0 唐先生纠正（已采纳 ✓）

```
$$\text{页面 }8\text{-}2\text{-}12.html\ \text{提供的是 }(n,M,r)=(8,12,\mathbf{2})\ \text{的 }277\ \text{个码}\ ✗\ \text{—— **半径 2**，不是我们要的 }r=1\ ✗$$
$$\text{论文范围本身正确}: \text{"length at most 8 or cardinality at most 4"}\ \text{的所有最优码，up to equivalence}\ ✓$$
$$\text{目标应为}: r=1,\ n=4..8,\ M=K(n,1)\ \text{的代表码数据}\ \boxed{\text{尚未找到}}\ ✗$$
```

## §1 探测清单与结果（9 处，**0 命中** ✓）

```
$$\begin{array}{c|c|c}
\text{探测目标} & \text{实际内容} & \text{判定}\\
\hline
\texttt{8-2-12.html}\ (+\texttt{8-2-12.txt}) & (8,2,12)\ \text{的 }277\ \text{个码，覆盖半径 2} & ✗\ \text{半径不对}\\
\texttt{old/cover/}\ \to\ \texttt{cover.zip} & \text{covering \textbf{design} 搜索程序（anneal.c 模拟退火等 18 文件）} & ✗\ \text{是 design}\\
\texttt{old/square/} & \text{若干 }n.dat\ \text{数据（square 问题）} & ✗\ \text{不同问题}\\
\texttt{codes/}\ (14\text{-}7\text{-}4,\ 20\text{-}10\text{-}6,\ 26\text{-}13\text{-}7) & \text{rate-1/2 线性码分类} & ✗\\
\texttt{opt23/}\ (0\_3\_2,\ 5\_1\_7,\dots) & \text{小二元/三元\textbf{纠错}码（packing）} & ✗\\
\texttt{bincodes.html} & \text{同上（rate-1/2）} & ✗\\
\texttt{table3.html} & \text{covering design }C(v,k,t)\ \text{上界表} & ✗\\
\texttt{23.html} & \text{小二元/三元纠错码电子站点} & ✗\\
\text{命名约定反查}: \texttt{\{6,7,8,5,4\}-1-\{12,16,32,7,4\}}（两主机） & \text{全部 404} & ✗\\
\end{array}$$
⟹ **结论**: 2000 年分类论文的（n≤8, R=1）代表码数据**未发布在作者站点** ✗；
   最可能仅存在于**论文附录**（Wiley 付费墙 ✗）
```

## §2 下一步（按成本）

```
$$\text{① 首选（便宜 ✓）}: \textbf{请唐先生下载} 2000 年论文 ⟹ \text{附录应含代表码}\ ✓$$
$$\qquad\text{DOI}: 10.1002/1520\text{-}6610(2000)8{:}6\langle 391{:}\rangle\text{AID-JCD1}\ \text{（J. Combin. Des. 8 (2000) 391–401 ✓）}$$
$$\text{② 备选（贵 ✗，我方自算）}: n=6\ \text{穷举} \Longrightarrow \text{有序生成（canonical 剪枝）或 SAT 判定路}（\text{需 pair 变量线性化, }2016\ \text{个 ✗）}$$
$$\text{③ 暂停}: \text{若 ①② 均不可行} \Longrightarrow \text{钉住线暂挂（其证据仅具 }n\le6\ \text{局部意义 ✓，对 }n=10\ \text{无推论力 ✗）}$$
```

## §3 纪律说明（AMEND-29 ✓）

```
$$\text{本档**未在错误数据集上做任何计算** ✓ —— 探测 9 处、全部落空后即停 ✗（未把 }8\text{-}2\text{-}12\ \text{的 }R=2\ \text{数据当作目标 ✓）}$$
$$\text{这正是 AMEND-29 §2 第三步"对象匹配"的执行实例}:\ \text{数据集的对象（R=2 / design / packing）}\ne\ \text{我方对象（}R=1\ \text{最优覆盖码）}\ ✓$$
```

## §4 边界（诚实标注）

- §1 探测结果均为**实测**（HTTP 200 + 正文核对 ✓）
- **未**声称该数据不存在 ✗（只能说"未在作者站点找到" ✓；"没找到 ≠ 不存在" ✓）
- 本档**未**排除任何 n ✗、**未**推进钉住猜想 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 数据接口探测 命中文件数=0    :: 
技术词 站点数据目录 命中文件数=0    :: 
技术词 附录依赖     命中文件数=0    :: 
技术词 负结果登记  命中文件数=0    ::
```

- **本档新增**（命中数=0）：数据接口探测、站点数据目录、附录依赖、负结果登记
- **档案已有（引用，不列为提出）**：—
- 注：四词含中文，回查解析器按首词匹配 ✓
