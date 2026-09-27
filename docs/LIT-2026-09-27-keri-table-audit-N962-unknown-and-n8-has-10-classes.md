已查地图：已跑 scripts/prework_map_check.sh Kéri 表 分类 上标 inequivalent ⟹ 执行自 `P1-2-2026-09-27-controlled-construction-attempt`（✓）＋ 唐先生 12:37（(a) 文献核验 ✓）；本档 = **A1 确认 ✓ / A2 = 文献沉默（未分类）✓ / 新测试场 n=8 ✓**
D0: 本档对象 = $N_{6,12}$、$N_{9,62}$ 与可用测试场
D1: 1（新增：**Kéri 表逐格读数 ✓**；**$N_{9,62}$ 未分类的判定 ✓**；**$n=8$ 有 10 类的测试场 ✓**）

# Kéri 表审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BC-1 表规约 ✓)}\ \text{Kéri 表：}\textbf{粗体＋上标＝已完成分类};\ \textbf{上标数字＝不等价最优覆盖码个数} ✓\ \text{（逐字引自原页 ✓）}}$$
$$\boxed{\textbf{(BC-2 A1 确认 ✓)}\ n=6,R=1\ \text{格} = \texttt{c}\,\mathbf{12}^{2}\,\texttt{c}\ \Longrightarrow \textbf{恰 2 个不等价最优码} ✓✓\ \text{与我实验的 2 类一致} ✓✓\ \Longrightarrow n=6\ \textbf{退出主实验池} ✓}$$
$$\boxed{\textbf{(BC-3 A2 判定 ✓✓)}\ n=9,R=1\ \text{格} = \texttt{o}\,\textbf{62}\,\texttt{j}\ \text{—— \textbf{非粗体}\ ✗、\textbf{无上标}\ ✗} \Longrightarrow \textbf{K(9,1)=62 已定，但该格\textbf{未分类}} ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{N}_{9,62}\ \textbf{文献未给出} \Longrightarrow \text{按唐先生判据：}\textbf{P1-2 不能由文献关闭} ✗\ \text{（既不能证 =2，也不能证 >2 ✓）}$$
$$\boxed{\textbf{(BC-4 新测试场 ✓✓)}\ n=8,R=1\ \text{格} = \texttt{c}\,\mathbf{32}^{10} \Longrightarrow \textbf{10 个不等价最优码（Östergård–Weakly 2000 分类 ✓）} \Longrightarrow \textbf{当前最佳 P1-2 实验场} ✓✓}$$
$$
$$
```

---

## §1 逐格读数（**verbatim ✓**）

```
$$\begin{array}{c|c|c}
n & R=1\ \text{格（原样 ✓）} & \text{读数}\\
\hline
4 & \texttt{b}\,\mathbf{4}^{2} & \text{已分类 ✓，2 个不等价} ✓\\
5 & \texttt{b}\,\mathbf{7}^{1} & \text{已分类 ✓，1 个} ✓\ \text{（与我穷举 320 码\textbf{单类}一致 ✓✓）}\\
6 & \texttt{c}\,\mathbf{12}^{2}\,\texttt{c} & \text{已分类 ✓，\textbf{2 个}} ✓\ \text{（与我生成的 2 类一致 ✓✓）}\\
7 & \texttt{h}\,\mathbf{16}^{1}\,\texttt{h} & \text{已分类 ✓，1 个（完美码唯一 ✓）}\\
8 & \texttt{c}\,\mathbf{32}^{10} & \text{已分类 ✓，\textbf{10 个}} ✓\\
9 & \texttt{o}\,\textbf{62}\,\texttt{j} & \textbf{未分类} ✗\ \text{（下界 }\texttt{o}=\text{Östergård--Blass 2001 ✓；上界 }\texttt{j}=\text{Wille ✓）}\\
10 & \texttt{i}\,\textbf{107-120}\,\texttt{j} & \text{未分类 ✓}\ \text{（区间 }\texttt{i}=\text{BÖW 2004 ✓）}\\
\end{array}$$
$$\text{附（对照 ✓）}:\ n=15,R=1=\texttt{h}\,\mathbf{2048}^{5983}\ \text{（已分类，5983 个 ✓）—— 说明"上标"确实是分类个数 ✓}$$
$$
$$
```

---

## §2 A1／A2 的判定（**✓**）

```
$$\textbf{A1（}n=6\text{）} ✓:\ \text{文献明确 }\mathbf{2}\ \text{个不等价最优码} \Longrightarrow \text{我实验的 }(A_1,A_2)=(4,8)\ \text{与}\ (0,12)\ \text{就是全部} \Longrightarrow \textbf{桶全 singleton 是结构性事实，非生成器不足} ✓✓$$
$$\qquad\Longrightarrow\ n=6\ \textbf{退出"寻找固定 }(A_1,A_2)\ \text{分叉"的主实验池} ✓\ \text{（与唐先生判断一致 ✓）}$$
$$\textbf{A2（}n=9\text{）} ✓:\ \text{该格\textbf{未分类}} \Longrightarrow \textbf{N}_{9,62}\ \text{未知} \Longrightarrow$$
$$\qquad\text{• 不能断言}P1-2\text{关闭（}N=2\text{ ✗ 未证）};\qquad \text{• 也不能断言重开（}N>2\text{ ✗ 未证）} \Longrightarrow \textbf{P1-2 保持 OPEN} ✓$$
$$\qquad\text{补充（档案 ✓）}:\ \text{"the two known codes attaining }K(9,1)=62\ \text{belong to one switching class"}\ \text{—— 但 switching class ≠ }(A_1,A_2)\ \text{类 ✓；且我实测两码 }(A_1,A_2)\ \text{不同} ✓✓\ \text{（switching 不保 }(A_1,A_2) ✓）}$$
$$
$$
```

---

## §3 新测试场：$n=8$ 的 10 类（**✓✓ 最有价值**）

```
$$\text{为何 }n=8\ \text{最好 ✓}:\ \text{(i) 已分类且}\textbf{有 10 个不等价最优码} ✓\ \text{（不是 1-2 个 ✗）};\ \text{(ii) }n=8\ \text{是 nearly-perfect（van Wee 取等 ✓）}\Longrightarrow A_1+A_2=\lceil E/2\rceil=16\ \textbf{钉住} ✓✓$$
$$\qquad\Longrightarrow\ \text{若 10 个码中出现}\ \textbf{同 }(A_1,A_2)\ \text{而 }J\ \text{不同} \Longrightarrow \textbf{P1-2 成立} ✓✓;\ \text{若 10 个码的 }(A_1,A_2)\ \text{全不同} \Longrightarrow \text{再退一层 ✓}$$
$$\text{需要}:\ \text{Östergård--Weakley 2000 分类（"Classification of binary covering codes", J. Combin. Des. 8 (2000) 391--401 ✓）中的 10 个代表码} ✓$$
$$\qquad\text{获取途径（下一步 ✓）}:\ \text{(a) 论文附录／表格};\ \text{(b) Kaski--Östergård 书（分类算法）附码};\ \text{(c) 自行生成（}n=8,M=32\ \text{规模较大 ⚠️ 但可试 ✓）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**逐格 verbatim 读数** ✓（含"上标＝分类个数"的规约与对照 ✓）；§2–§3 为**判定 ＋ 下一步** ✓
- **未**声称 $N_{9,62}$ 的值 ✗（文献未给 ✓）；**未**声称 P1-2 关闭或重开 ✗（两侧均未证 ✓）；**未**改动 119 UNKNOWN ✓
- 检索纪律 ✓：Tavily 额度耗尽（432 ✓）⟹ 切 Firecrawl ✓（遵 MEMORY.md ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Kéri 表逐格读数、$N_{9,62}$ 未分类判定、$n=8$ 十类测试场
- **档案已有（引用，不列为提出）**：$K(n,1)$、switching class、van Wee 取等、nearly-perfect、BÖW 2004、Wille


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Kéri 表逐格读数 命中文件数=1    :: ./LIT-2026-09-27-keri-table-audit-N962-unknown-and-n8-has-10-classes.md 
技术词 十类测试场  命中文件数=1    :: ./LIT-2026-09-27-keri-table-audit-N962-unknown-and-n8-has-10-classes.md
```
- **本档新增**：Kéri 表逐格读数、$N_{9,62}$ 未分类判定、$n=8$ 十类测试场（见上方命中数；0 命中者为自造语／内部标签 ✓）
