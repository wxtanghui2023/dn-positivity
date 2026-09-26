已查地图：已跑 scripts/prework_map_check.sh OB LP 反演 引文网络 审计 ⟹ 执行自 LAYERAB-2026-09-26 档；本档为**乙线第四 commit：后续文献反演 ＋ 候选指纹表 ＋ 重大审计发现**（唐先生 2026-09-26 18:17 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 引文网络（21 篇）、关键摘要逐字、候选 LP 指纹表、重建算法、**目标覆盖审计**
D1: 1（新增：**引文网络＋摘要逐字** ✓✓；**候选指纹表（含排除）** ✓✓；**审计发现：目标很可能已被分类文献覆盖** ⚠️✓）

# OBREVERSE-2026-09-26

## §1 ✅ **引文网络（OpenAlex：OB2001 被引 21 篇 ✓）**

```
$$\textbf{关键命中（逐字摘要 ✓）}:$$
$$\quad\text{[2009] Linderoth--Margot--Thain, INFORMS JoC, DOI 10.1287/ijoc.1090.0334}:$$
$$\qquad\text{"Using a combination of }\textbf{isomorphism pruning}\text{, }\textbf{subcode enumeration}\text{, and }\textbf{linear programming-based bounding}\text{, ...}$$
$$\qquad\text{improve the lower bound on the size of the optimal code from 65 to 71."}\ ✓✓$$
$$\quad\text{[2003] Östergård, IEEE TIT, DOI 10.1109/tit.2002.807307}: \text{"By using a }\textbf{computational method for classifying}$$
$$\qquad\textbf{covering codes}\text{, it is shown that there is }\textbf{no balanced code attaining }K(9,1)=62\text{."}\ ✓✓$$
$$\quad\text{[1998] Blass \& Litsyn, IEEE TIT 44(5) 1998--2002, DOI 10.1109/18.705582}\ (\textbf{OB 的参考文献}\ ✓✓):$$
$$\qquad\text{"We derive several new lower bounds on the size of binary codes with covering radius one. In particular, we prove K..."}\ ✓$$
$$\quad\text{[2004] Bertolo--Östergård--Weakley, JCD}: \text{"...and a }\textbf{general lower bound for }R=1\text{."}\ ✓$$
$$
$$

## §2 ⭐⭐ **候选 LP 指纹表（含排除 ✓）**

```
$$\begin{array}{c|c|c}
\text{候选} & \text{能否解释 OB 文字} & \text{依据}\\ \hline
\text{标准 covering LP} & ✗ & \text{OB 说 "distributions"}\ ✗\ ——\ \text{标准 LP 的变量是码字/点}\ ✗\\
M\text{-covering 的 LP 松弛} & \checkmark\checkmark & \text{吻合 "distributions in subspaces" + "inequivalent" + "repeatedly"}\ ✓\\
y\text{-SIP 的 LP 松弛} & \checkmark\ (\text{部分}) & \text{码级 IP 的松弛；但 OB 说 "distributions"，偏 }y\ \text{侧}\ ⚠️\\
\text{weighted-covering LP} & \checkmark\ (\text{作对偶}\ ✓) & \text{摘要明说 "a connection ... and weighted coverings"}\ ✓\\
\text{distribution-level LP + refinement} & \checkmark\checkmark & \text{与 "refined until dimension zero" 完全一致}\ ✓\\
\text{两层混合 LP} & \checkmark\ (\text{可能}) & \text{若 LP 同时含 }y\ \text{与 }x\ \text{变量}\ ⚠️\\
\end{array}$$
$$\Longrightarrow\ \textbf{最强候选} = M\text{-covering 的 LP 松弛}（\text{在 refinement 树上反复解}\ ✓）\Longrightarrow\ \text{其对偶 = weighted covering}\ ✓\ (\text{HYPOTHESIS 级}\ ⚠️)$$
$$
$$

## §3 ⭐ **重建算法（HYPOTHESIS，证据支持 ✓）**

```
$$\textbf{for each node }\nu\ (\text{一组 cell-count 约束，level }m)\text{:}$$
$$\qquad \text{① 解 LP 松弛：若\textbf{不可行} ⟹ 剪枝}\ ✗\ (\text{该节点下无码}\ ✓)$$
$$\qquad \text{② 若可行 ⟹ 按 }\textbf{inequivalent refinements}\ \text{分支}\ (m\to m+1)\ ✓$$
$$\qquad \text{③ 终止：cell 维数 0 ⟹ 精确 IP ⟹ certificate}\ ✓$$
$$\textbf{对偶意义}: \text{每个 LP 的对偶 = 一个\textbf{加约束的 weighted covering}（\text{权重落在节点/cell 结构上}\ ✓）\Longrightarrow \text{这就是 OB 所说 connection}\ ✓$$
$$\textbf{与 LMT 的三技术对应}: \text{isomorphism pruning}=\text{inequivalence}\ ✓;\ \text{subcode enumeration}=\text{refinement 分支}\ ✓;\ \text{LP-based bounding}=\text{①}\ ✓✓$$
$$
$$

## §4 ⚠️✓ **重大审计发现（必须报告 ✓）**

```
$$\textbf{事实}: \text{Kéri CD 的 }K\_9\_1\_classif.txt\ \text{给出\textbf{两份} 62 码}\ ✓;\ \text{ALCOMA10: "the two known codes attaining }K(9,1)=62\ \text{belong to }\textbf{one switching class}\text{"}\ ✓$$
$$\qquad\Longrightarrow\ \text{若该分类\textbf{完备}（"classif" 文件名 + 文献口径}\ ✓),\ \text{则\textbf{全部}最优码在该 switching class 内}\ ✓$$
$$\textbf{而 two codes 的 }b\text{-profile 相同}\ (\{1{:}432,2{:}62,3{:}8,4{:}10\}\ ✓✓)\ \text{且 switching 保 profile}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{全部 }(9,62)\ \text{最优码都有 }N_4=10\ \Longrightarrow\ \textbf{我方目标 }N_4\ge10\ \text{很可能已被分类文献覆盖}}\ ⚠️✓$$
$$\textbf{AMEND-24 口径}: \text{"kill 条件 = 目标命题已有 achieved result coverage"}\ ✓\ \Longrightarrow\ \textbf{按此口径，G 的靶心应判 COVERED}\ ⚠️✓$$
$$\textbf{我方工作的实际价值（重新定位 ✓）}: \text{① 显式刚性测定（10+ 项跨表示不变量）}\ ✓✓;\ \text{② Layer A/B 结构定理}\ ✓✓;\ \text{③ 方法学（14 条否证）}\ ✓\ ——\ \textbf{但不是新结果}\ ✗$$
$$
$$

## §5 状态与建议

```
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{未跑 solver/LP/SAT}\ ✓$$
$$\text{建议（\text{待唐先生裁定}\ ✓）}: \text{(甲) 按 AMEND-24 判 G 靶心 COVERED ⟹ 转独立问题}\ ✓;\ \text{(乙) 重构靶心为"分类无关的人类可读证明"}\ ⚠️;\ \text{(丙) 把方法迁移到 }n=10\ (119)\ ✗\ \text{——本轮不建议}\ ✓$$
$$
$$

## §6 边界（诚实标注）

- §1 为**第三方摘要逐字**（OpenAlex ✓）；§2–§3 为**反演与假设**（明确 HYPOTHESIS ⚠️）；§4 为**审计推论**（"若分类完备" ⚠️）
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 候选指纹表  命中文件数=1    :: ./OBREVERSE-2026-09-26-literature-reverse-engineering-and-audit-bombshell.md 
技术词 审计发现     命中文件数=43   :: ./AUDIT-direction-depth.md ./APPRECIATION-AUDIT-2026-09-11.md ./E90-karatsuba-audit.md 
技术词 反演算法     命中文件数=1    :: ./OBREVERSE-2026-09-26-literature-reverse-engineering-and-audit-bombshell.md
```
- **本档新增**（扣自引后 = 0）：候选指纹表、审计发现、反演算法
- **档案已有（引用，不列为提出）**：Layer A/B、M-covering、weighted covering
