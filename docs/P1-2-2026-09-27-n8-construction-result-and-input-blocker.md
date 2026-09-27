已查地图：已跑 scripts/prework_map_check.sh n=8 乘积构造 semiflip 10 类 ⟹ 执行自 `LIT-2026-09-27-keri-table-audit`（✓）＋ 唐先生 12:39/12:41（取 n=8 码 ✓）；本档 = **n=8 显式构造成功 ＋ 输入阻塞（10 类代表未公开）** ✓。
D0: 本档对象 = $n=8$ 的 $K(8,1)=32$ 码的构造与 P1-2 可测性
D1: 1（新增：**显式乘积码 ＋ 其 $(A_1,A_2)=(16,0)$ ✓；van Wee 取等的独立印证 ✓；扰动刚性 ✓**）

# $n=8$ 构造结果 ＋ 输入阻塞（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BD-1 显式构造成功 ✓✓)}\ C=H(7,4)\times\mathbb F_2\subseteq\mathbb F_2^8\ ✓:\ |C|=32\ ✓,\ \text{覆盖半径 1} ✓,\ \textbf{极小} ✓}$$
$$\qquad\textbf{且}\ \boxed{(A_1,A_2)=(16,\,0)}\ \Longrightarrow\ A_1+A_2=16=\frac E2=\frac{32\cdot9-256}2\ \Longrightarrow\ \textbf{van Wee 取等} ✓✓$$
$$\qquad\Longrightarrow\ \text{\textbf{独立印证}档案的 }Q^*(8)=0\ \text{（nearly-perfect）} ✓✓\ \text{（走纯构造路径 ✓，非文献引用 ✓）}$$
$$\boxed{\textbf{(BD-2 结构读数 ✓)}\ J\text{-向量}=(32,0,0,0,0,0,256)\ \text{且}\ d_1(c)\le1\ \forall c\ ✓\ \text{（distance-1 图是\textbf{匹配} ✓——与档案 matching 定理一致 ✓✓）}}$$
$$\boxed{\textbf{(BD-3 扰动刚性 ⚠️)}\ \text{1-,2-,3-,4-随机替换：合格邻居}\ \mathbf{=0}\ \text{个}\ ✗\ \Longrightarrow\ \text{随机扰动\textbf{无法}到达其它类} ⟹ \textbf{必须走结构化 move（semiflip ✓）或直接取代表} ✓}$$
$$\boxed{\textbf{(BD-4 输入阻塞 ✗)}\ 10\ \text{个 }(8,32)_1\ \text{代表：}\textbf{公开渠道未提供}}$$
$$\qquad\text{已排除（本档 ✓）}:\ \text{Östergård 主页 2000 论文电子附件 = 仅 }(8,2,12)\ \text{的 277 码 ✗};\ \texttt{8-1-32}/\texttt{8-1.txt}\ \text{等猜测名 404 ✗};\ \texttt{tcs.hut.fi/\textasciitilde pat/}\ \text{目录已废 ✗};\ \texttt{old/cover/cover.zip}\ \text{仅 C 源码 ✗}$$
$$
$$
```

---

## §1 乘积构造（**✓ 本机验证**）

```
$$H=[7,4,3]\ \text{Hamming 码（16 码字 ✓，覆盖 }\mathbb F_2^7\ \text{✓）};\qquad C=\{h\oplus(b\cdot e_8):\ h\in H,\ b\in\{0,1\}\}\ ✓\ (|C|=32\ ✓)$$
$$\text{覆盖性证明（一行 ✓）}:\ \forall(y,b)\in\mathbb F_2^8,\ \exists h'\in H:\ d(h',y)\le1\ \Longrightarrow\ (h',b)\in C\ \text{且}\ d((h',b),(y,b))\le1\ ✓$$
$$\text{结构 ✓}:\ \text{两码字 }(h,b),(h',b'):\ d=d(h,h')+[b\ne b']\ ✓\ \Longrightarrow\ d(h,h')=0\Rightarrow d=1\ (A_1)\ ✓;\ d(h,h')=3\Rightarrow d\in\{3,4\}\ (A_2=0\ ✓)$$
$$
$$
```

---

## §2 扰动实验（**✓ 本机，结论：随机 move 无效 ⚠️**）

```
$$\begin{array}{c|c}
k\text{-替换} & \text{合格邻居数（仍覆盖 ∧ }|C|=32\ ✓\text{）}\\
\hline
1 & 0\ ✗\\
2 & 0\ ✗\\
3 & 0\ ✗\\
4 & 0\ ✗\ (6{,}000\ \text{次抽样/档 ✓})\\
\end{array}$$
$$\text{解释 ✓}:\ E=32\ \text{极小（}\frac{32\cdot9}{256}=1.125\ \text{覆盖重数 ✓）}\Longrightarrow \text{覆盖条件极紧 ⟹ 随机替换几乎必破坏覆盖 ✓}$$
$$\Longrightarrow\ \textbf{结论}:\ \text{要取其它 9 类，只能靠}\textbf{结构化 move（2018 论文的 semiflip ✓）}\ \text{或}\textbf{直接取文献代表} ✓$$
$$
$$
```

---

## §3 下一步（**两个选项，请唐先生定 ✓**）

```
$$\text{(a) 上传 2018 论文（Östergård--Weakley, Discrete Math 341(6):1778--1788, 2018 ✓）PDF} \Longrightarrow \text{我可抽取 semiflip 定义 ＋ 代表结构 ✓（最省 ✓）}$$
$$\qquad\text{（我已确认：该论文\textbf{专门研究} }K(8,1)=32\ \text{的 switching 与 semiautomorphism classes ✓ 摘要已取 ✓）}$$
$$\text{(b) 若暂无 PDF}:\ \text{我可用\textbf{结构性生成}（非随机 ✗）扫 }(8,32)_1\ \text{码族}:\ \text{以覆盖-保持的结构化 move 为主 ✓，代价较高 ⚠️}$$
$$\text{(c) 退路（唐先生原议 ✓）}:\ \text{若 (a)(b) 均不顺，则按"已知完整/穷举数据在 }n=5,6,7,8\ \text{均无 fixed-}(A_1,A_2)\ \text{分叉"}\ \text{转向 2-face/triple ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1–§2 为**本机构造 ＋ 验证** ✓（乘积码 ＋ 扰动实验 ✓）；§3 为**选项** ✓
- **未**声称取得 10 类代表 ✗（公开渠道无 ✓）；**未**声称 P1-2 成立或失败 ✗；**未**改动 119 UNKNOWN ✓
- ⚠️ 检索纪律 ✓：Tavily 432 ⟹ 切 Firecrawl ✓；猜测文件名一律先验证 ✓（本档 4 个猜测全 404 ✗）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$n=8$ 乘积构造、扰动刚性判定、输入阻塞清单
- **档案已有（引用，不列为提出）**：$K(8,1)=32$、van Wee 取等、nearly-perfect、matching 定理、semiflip


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 乘积构造     命中文件数=3    :: ./P1-2-2026-09-27-n8-construction-result-and-input-blocker.md ./FRONTIER-R3-2026-09-27-phase1-steiner-cells-mechanism-inventory.md ./FRONTIER-R1-CHECK-2026-09-26-rosqs-five-cells.md 
技术词 扰动刚性     命中文件数=2    :: ./p49-offline-obstruction.md ./P1-2-2026-09-27-n8-construction-result-and-input-blocker.md
```
- **本档新增**：$n=8$ 乘积构造、扰动刚性判定、输入阻塞清单（见上方命中数；0 命中者为自造语／内部标签 ✓）
