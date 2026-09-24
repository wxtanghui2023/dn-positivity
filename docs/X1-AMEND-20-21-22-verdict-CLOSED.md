已查地图：命中（`HUNT-R3-3-coarse-supply-table`）⟹ `X1` 三闸判定，不开新案
D0: 本档对象 = **`X1`（`A000983`／`K(10,1)`／`γ(Q_{10})`）现行状态确认** ＋ **`AMEND-20`（族字面＋等价参数化）** ＋ **`AMEND-21`（三合一）** ＋ **`AMEND-22`（身份锁定）** ＋ 判定 `CLOSED` ＋ 覆盖码赛道三线占位校准
D1: 0（闸门判定型，零计算）
[REVIEW]

# **`X1`：`AMEND-20/21/22` 判定**

## §0 现行状态（先生已核 ＋ 本轮复核）

```
$$\textbf{权威记录}:\ \texttt{OEIS A000983}\ \text{页面}\ \textbf{2026-09-22}\ \text{修改过，仍写}\ \boxed{a(10)\in[107,120]};\ \text{未登记精确值}$$ ✓（先生核）
$$\textbf{上界证书}:\ \text{Kamenetsky《Best known solutions for }n\le11\text{》}\ \text{给出}\ \boxed{a(10)\le120},\ a(11)\le192,\ \text{并列出}\ \textbf{120-word、长 10、半径 1}\ \text{的覆盖码}\Longrightarrow\text{可机器复核的构造}$$ ✓✓
$$\textbf{下界来源}:\ 107\ \text{链接至 Bertolo–Östergård–Weakley 2004 mixed covering-code 表};\quad \textbf{证书形式尚未核定}$$ ⚠️
$$\textbf{结论}:\ \boxed{107\le K(10,1)\le120}\ \textbf{记录仍开};\quad \text{旁证（非权威）亦记 }107\ldots120$$ ✓
```

## §1 `AMEND-20`：族字面检索 ＋ 等价参数化（**命中，密集**）

```
$$\textbf{族字面}:\ \texttt{K(10,1)};\ \texttt{domination number }Q_{10};\ \text{binary length-10 radius-1 covering code};\ \texttt{A000983};\ \texttt{K(n,1)}\ \text{值表（}n\le8\ \text{已知 → 现 }\le9\text{）};\ \text{van Wee 界};\ \text{Habsieger 同余法}$$ ✓
$$\textbf{等价参数化（已建立且同名）}:\ \boxed{\text{超立方体支配集}\ \equiv\ \text{二元长 }n\ \text{半径 }1\ \text{覆盖码}}（\text{Wu–Chen 2024 开篇逐字}）;\ \text{另有帽子猜数游戏等价（OEIS 注）}$$
$$\textbf{近作}:\ \texttt{arXiv:2203.16901}\ (\text{Wu–Chen};\ \text{Discrete Math. }347(2)\ 2024):\ \boxed{\text{“It is still an open problem”}}\ \text{＋ 对 }6\mid n\ \text{改进下界}\ (\text{van Wee }\tfrac{2^n}n\to\tfrac{(n-2)2^n}{n^2-2n-2})$$
$$\qquad \text{（注：}n=10\ \text{非 }6\ \text{的倍数 ⟹ 该法不适用于本格，但证明该族\textbf{正在被攻关}）}$$
$$\textbf{渐近}:\ \lim\gamma(Q_n)/(2^n/n)=1\ (\text{Kabatyanskii–Panchenko 1988};\ \text{见 Griggs};\ \text{Covering Codes }\text{p.332})$$
```

## §2 `AMEND-21`：三合一未覆盖

```
$$\textbf{① 对象未覆盖}:\ \boxed{\text{不成立 ✗}}\ ——\ \text{对象是\textbf{长期被系统研究}的经典对象}（\text{van Wee 1988};\ \text{Habsieger 1997};\ \text{Litsyn 1998};\ \text{Östergård 等 tabu search};\ \text{Wu–Chen 2024}）$$
$$\textbf{② 参数化未覆盖}:\ \boxed{\text{不成立 ✗}}\ ——\ (\text{binary},\ n=10,\ R=1,\ \text{unrestricted})\ \text{即文献标准参数化};\ \text{等价表述亦已建立}$$
$$\textbf{③ 充要条件未覆盖}:\ \text{形式上成立（无 characterization），}\textbf{但按先生规则：}\boxed{\text{问题仍开而攻击接口已被覆盖}\Rightarrow\text{照样 CLOSED}}$$
$$\qquad \text{三条攻击线\textbf{全部有在跑的项目与已发表方法}}:$$
$$\qquad \quad (a)\ \textbf{下界（LP／同余）}:\ \text{van Wee};\ \text{Habsieger};\ \text{Wu–Chen 2024}\ \text{改进};\ \text{Litsyn 1998 新下界};$$
$$\qquad \quad (b)\ \textbf{不可行性（ILP/SAT/穷举）}:\ \boxed{\text{已撞线}}\ ——\ \text{先生指出之 IBM 社区项目}:\\ \qquad \qquad \text{“}\textbf{Proving infeasibility of binary ILPs, part 2}\text{”}\ \text{明确以 }\boxed{\text{585{,}090 configurations}}\ \text{的全排除为目标},\ \text{并称}:\ \text{若全部排除则得 }A000983(10)=120;$$
$$\qquad \quad (c)\ \textbf{上界（构造／搜索）}:\ \text{Kamenetsky best-known 表};\ \text{tabu search 系列};\ \text{120-word 码即其产物}$$
$$\Longrightarrow\ \boxed{\textbf{AMEND-21} = \text{FAIL}}$$ ✓✓
```

## §3 `AMEND-22`：身份锁定

```
$$\text{身份} = \boxed{\text{“二元、非线性、长 }10\text{、半径 }1\ \text{覆盖码的\textbf{精确值}”}}\ \text{—— 可锁定 ✓}$$
$$\text{与 }C07\ \text{关系}:\ \text{同族（覆盖码）但}\textbf{不同对象}（C07 = 线性协维格；X1 = 非线性半径 1）\Longrightarrow\ \text{不构成“改参数硬救”}$$ ✓
$$\qquad \text{但 AMEND-21 已 FAIL，故无需再讨论其可入场性}$$
```

## §4 判定

```
$$\boxed{X1 = \textbf{CLOSED}}$$ ✓✓
$$\qquad \text{依据}:\ \text{① 对象与参数化均已被系统覆盖};\ \text{② 充要条件缺失但}\textbf{攻击接口被三条现有线路覆盖};\ \text{③ \textbf{已撞上}正在进行的 ILP 不可行性项目（585{,}090 configurations）}$$
$$\textbf{措辞纪律}:\ \boxed{\text{记录仍开}\ \ne\ \text{可入场}}\ ——\ \text{不是“该问题已被解决”，而是“该格不满足我方入场条件”}$$ ✓✓
$$\textbf{本轮收获（正面）}:\ \text{如实检验了 }X1\ \text{的 }\textbf{PRE-G0 定位}\ ——\ \text{上一轮标其为 A 是\textbf{粗筛层面}的正确判断，本轮的细闸才判出 CLOSED};\ \text{两轮判定并不矛盾}$$
```

## §5 校准（写入来源评估）

```
$$\boxed{\text{校准 E3}:\ \textbf{覆盖码赛道已被三线占位}}\ ——\ (a)\ \text{LP／同余下界};\ (b)\ \text{ILP/SAT 不可行性};\ (c)\ \text{构造／搜索上界};\ \text{三线皆有在跑项目与已发表方法}$$
$$\qquad \Longrightarrow\ \text{该赛道内的所有“记录缺口”型候选（}X2,X3,X8,\ \text{含未来同族项}）\ \textbf{一律降权};\ \text{我方 }C07\ \text{的成功恰因当时\textbf{落在未被这三线覆盖的具体格}上}$$
$$\boxed{\text{校准 E4}}:\ \text{“权威源未更新精确值”}\ \text{不足以判定可入场};\ \text{必须同时核}\boxed{\text{是否有在跑项目正以同一技术路线攻击该格}}$$
```

## §6 下一步（不越权）

```
$$\text{余项状态}:\ X2,X3,X4,X8\ (\text{均落在 E3 降权赛道或活跃 ILP 赛道});\ X5\ \text{的 Extremal G.T./Coloring 子类（未细看）};\ X7\ (\text{来源补充，未抽取})$$
$$\textbf{建议（待先生定）}:\ \text{① 先细看 }OPG\ \text{Extremal G.T.（9 条）＋ Coloring（66 条）}\ \text{是否含}\textbf{记录型}条目;\ \text{② 若仍无，则离开 }X\ \text{轮，回 }L1/L3/L4\ \text{换来源}$$
$$\textbf{不建议}:\ \text{在覆盖码赛道内继续找格（E3）};\ \text{不重开 }X1$$
【⛔ 纪律】 本轮**零计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 全部为**检索抽取级** ＋ 先生所核 OEIS/证书文件；**下界证书形式未核定**；IBM 项目内容为先生所述（本轮未能直接取回该页） ✓

## §附 【技术词回查】（补录）
```
技术词 gate verdict     命中文件数=0    :: 
技术词 lane occupancy   命中文件数=0    :: 
```
