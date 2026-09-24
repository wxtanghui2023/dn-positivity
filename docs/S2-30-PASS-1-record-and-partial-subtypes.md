已查地图：命中（`CANDIDATE-CENSUS-v1` ＋ `AMEND-15`）⟹ 本档为 `S2-30` 第一轮记录与细化，不开新案
D0: 本档对象 = **`S2-30/Pass-1` 记录**：唐先生逐项 `S2` 结果（含 3 例引用）＋ ⚠️**计数复核**（逐行 vs 摘要不一致）＋ `SPEC-REQUIRED` 三例补规格 ＋ `PARTIAL` 四分类逐条分型
D1: 1（首次 `S2` 批量执行；产出 `PARTIAL` 分型与规格补齐）
[RESEARCH]

# **`S2-30 / Pass-1` 记录与细化**

## §1 逐行结果（照先生表，原样）

```
$$\begin{array}{c|c|c}
\#&\text{ID}&\texttt{S2}\\
\hline
1&Gr01&U\\2&Gr02&U\\3&Gr03&P\\4&Gr04&P\\5&Gr05&\boxed{C}\\6&Gr07&P\\
7&C01&P\\8&C02&P\\9&C03&P\\10&D01&P\\11&D02&P\\12&D05&P\\13&D08&U\\14&Mt01&\boxed{C}\\15&Mt02&U\\
16&Au01&P\\17&L01&P\\18&L03&P\\19&Po02&U\\20&Po06&U\\21&FF02&P\\22&FF06&U\\23&FF07&P\\24&R03&\boxed{C}\\
25&Au06&U\\26&G04&P\\27&FF03&P\\28&R02&P\\29&M03&U\\30&M04&U\\
\end{array}$$ ✓
```

## §2 ⚠️ 计数复核（**逐行统计 vs 摘要不一致**）

```
$$\textbf{逐行统计}:\quad \boxed{C=3\ (Gr05,Mt01,R03)},\qquad \boxed{P=17},\qquad \boxed{U=10}$$ ✓✓
$$\qquad U\ \text{十例}:\ Gr01,Gr02,D08,Mt02,Po02,Po06,FF06,Au06,M03,M04$$ ✓
$$\textbf{先生摘要}:\quad C=3,\ P=15,\ U=12\ \Longrightarrow\ \text{与逐行统计差 }\mathbf{2}\ (\text{即 }P\ \text{多 }2,\ U\ \text{少 }2)$$ ⚠️
$$\Longrightarrow\ \boxed{\text{按本项目计数纪律，以\textbf{逐行}为准：}C=3,\ P=17,\ U=10};\ \text{待先生确认口径}$$ ✓✓
$$\text{（留池数同口径下仍为 }27/30\text{，与先生结论一致 —— 差异在 }P/U\ \text{边界而非留池数）}$$ ✓
```

## §3 `SPEC-REQUIRED` 三例规格补齐（照 `AMEND-16` §2）

```
$$\textbf{Au01}\ \Longrightarrow\ \text{状态数 }n\le10\ (\text{附 }k{=}3\ \text{时 }n\le6);\ \text{字母表 }k{=}2;\ \text{类别＝全部同步 DFA（最坏情形）＋ Černý 族};$$
$$\qquad \text{量}:\ c(n,k):=\max\ \text{最短同步字长};\quad \text{命题}:\ \text{给出 }n\le10,k{=}2\ \text{的精确 }c(n,k)\ \text{表，并判定 }c(n,2)=(n-1)^2\ \text{是否对全部 }n\le10\ \text{成立}$$ ✓
$$\textbf{Au06}\ \Longrightarrow\ \text{变体族 }qx{+}1\ (q\in\{5,7,9\});\ \text{域 }x\le10^8;\ \text{量}:\ \text{总停时 }T_q(x)\ \text{最大值与达到集};$$
$$\qquad \text{命题}:\ \text{给出 }q{=}5,7,9\ \text{在 }x\le10^8\ \text{内的精确 record-holder 集合与 }\max T_q,\ \text{并判定达到者是否唯一}$$ ✓
$$\textbf{FF03}\ \Longrightarrow\ q=2^n,\ n\le12\ (\text{可行则附 }13,14);\ \text{量}:\ N(q,t):=\#\{\text{primitive }x\in\mathbb F_q:\ \mathrm{Tr}(x)=t\};$$
$$\qquad \text{命题}:\ \text{给出 }(n,t)\ \text{的精确计数表，并给出与均匀预测的偏差谱（首次偏离 }\lfloor\cdot\rceil\ \text{的 }n)$$ ✓
$$\Longrightarrow\ \text{三例补齐后\textbf{重新进入 }S2}（\text{不再挂在 }P/U\ \text{的"规格不足"状态}）$$ ✓
```

## §4 `PARTIAL` 四分类逐条分型（`AMEND-16` §1）

```
$$\begin{array}{c|c|l}
\text{ID}&\text{类}&\text{依据}\\
\hline
Gr03&P1&\text{一般特征值重数上界／极值分类（未含 }n{=}11\ \text{完整极值分类）}\\
Gr04&P1,P3&\text{cubic 图 zero-forcing 结构类界与分类}\\
Gr07&P1&\text{maximum-nullity／rank 问题大量结果}\\
C01&P1&\text{covering-code bounds／tables}\\
C02&P1&\text{系统表 ＋ 历史 bounds}\\
C03&P1,P4&\text{exact values ＋ bounds ＋ 更新表}\\
D01&P1,P4&\text{La Jolla best-known 数据库}\\
D02&P3&\text{经典 existence spectrum ＋ 参数族（一般参数未全覆盖）}\\
D05&P3&\text{小 ordered orthogonal arrays 专门研究}\\
L01&P3&\text{已知 lattice packing 数据／经典格密度}\\
L03&P1&\text{维 }10,11\ \text{bounds}（2025\ \text{另有新 lower bounds）}\\
FF02&P2&\text{五次分圆数理论存在，无 }q=2^k\ \text{该族文本}\\
FF07&P2&\text{一般 shift／intersection 理论}\\
G04&P3,P4&\text{S}_n\ \text{子群分类与标准子群数据大量}\\
R02&P1,P2&\text{递推 mod }m\ \text{周期理论成熟}\\
\end{array}$$ ✓✓（15 条；另 Au01／FF03 归 `SPEC-REQUIRED`，补齐后重判）
```

## §5 校准判词（照先生 §当前结论）

```
$$\boxed{\text{`S2` \textbf{通过校准}:\ 首轮\textbf{未}再现"经典对象}\to REJECT"\text{ 的系统性误杀}}$$ ✓✓✓
$$\text{留池 }27/30;\ \text{结构上已同时出现四类}:\ \text{有部分结果者／有数据库无目标精确覆盖者／有一般理论未核具体有限命题者／尚无直接覆盖证据者}$$ ✓
$$\textbf{不作 }S3：\text{先把剩余 }27\ \text{条的 }S2\ \text{做扎实（}PARTIAL\ \text{四分型已做；}SPEC\ \text{三例已补）}$$ ✓✓
$$\textbf{关键纪律}:\ \text{不得把"尚未搜到"误当成"研究空白"}$$ ✓✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1/§5 为先生 Pass-1 记录；§2 为**逐行复核**（差 2，待确认）；§3/§4 为本档工作 ✓

## §附 【技术词回查】（补录）
```
技术词 coverage         命中文件数=31   :: ./C3843-global-endpoint-coverage-to-level2-closure.md ./C3-source-hunt-status-three-pdfs-and-remaining-gap.md ./C97-prime-gap-memory-analysis-real-data-N2e7.md 
技术词 specification    命中文件数=4    :: ./RESEARCH-CONSTITUTION.md ./E142-Q3-definitional-audit.md ./C71-identification-side-decision-procedure-five-steps-and-three-entry-fixed-deaths.md 
```
