已查地图：已跑 scripts/prework_map_check.sh ledger 119 OPEN BLOCKED 下一轮协议 RoSQS ⟹ 执行自 `SUPPVIS-2026-09-27`（✓）＋ 唐先生 2026-09-27 09:42 ✓；本档为**终局账目 ＋ 下一轮协议**。
D0: 本档对象 = 119 终局状态、p2b 资产登记、M-2 归档、候选 STOP 清单、下一轮协议
D1: 1（新增：**119 = OPEN/BLOCKED 终局措辞** ✓；**候选 STOP 清单** ✓；**source-first 协议** ✓）

# LEDGER-2026-09-27 · K(10,1) 账目与下一轮协议

## §0 终局账目（唐先生 09:42 裁定 ✓）

```
$$\boxed{\textbf{K(10,1)}\ge120?\quad\textbf{— OPEN / BLOCKED}}\ ✓$$
$$\qquad\textbf{我们证明的是}:\ \boxed{\text{当前这组方法没有提供新的 \textbf{size lower-bound lever}}}\ ✓$$
$$\qquad\textbf{不是}:\ \boxed{\text{不存在 }K(10,1)\ge120\ \text{的证明}}\ ✗\ \text{（此区别必须保留 ✓）}$$
$$
$$

$$\textbf{问题降维（剥壳后 ✓）}:\quad \boxed{C\subseteq\mathbb F_2^{10},\quad C+B_1=\mathbb F_2^{10}\ \Longrightarrow\ |C|\ge120\ ?}\ ✓$$
$$\qquad\text{已知下界仅到 }107\ (\text{Bertolo--Östergård--Weakley 2004})\ \text{（及 2025 SDP 型非整数改进 105.22 ✗）};\ \text{缺口＝}\textbf{至少 13 个单位}\ ✓$$
$$
$$
```

---

## §1 新资产登记（p2b ✓，按指定标签 ✓）

```
$$\boxed{\textbf{NEW ASSET}:\ \text{support--excess label determines Booleanity on }Q_4}\ ✓$$
$$\qquad\textbf{标签（唐先生指定 ✓）}:\ \boxed{\text{P1-A mechanism: verified at }n=4;\ \textbf{no leverage on P1-B}}\ ✓$$
$$\qquad\text{内容}:\ (\mathrm{supp}\,f,\ \delta|_{\mathrm{supp}f})\ \text{在 }\mathrm{Aut}(Q_4)\ \text{下\textbf{完全决定} Booleanity}\ (49\ \text{轨道，0 不定}\ ✓);\ \text{标签不含 }f\ ✓$$
$$\qquad\textbf{纪律}:\ \textbf{不得}包装成"119 取得进展" ✗\ \text{（仅 P1-A 侧、无载荷 ✓）}$$
$$
$$
```

---

## §2 M-2 整线一次归档（不再微调 ✗）

```
$$\begin{array}{c|c|c}
\text{分支} & \text{状态} & \text{原因}\\
\hline
\text{M-1 BQP} & \textbf{KILL}\ ✗ & \text{exact lift 下退化为 Booleanity（}f_u\le1\ \text{改写）}\\
\text{M-2A} & \textbf{CLOSED}\ ✗ & \text{Haas 单中心 refined-weight LP}\le119\ (=1024/11)\\
\text{M-2A′} & \textbf{BLOCKED}\ ✗ & \text{surfeit cut 未证有效 ＋ pair chain 无法闭合}\\
\text{M-2B} & \textbf{DROP}\ ✗ & \text{无非循环的 supercode embedding}\\
\end{array}$$
$$\Longrightarrow\ \textbf{禁止继续"微调 M-2"}\ ✗\ \text{（继续优化这些坐标＝换表示重述已识别瓶颈 ✓）}$$
$$
$$
```

---

## §3 候选 STOP 清单（唐先生 09:42 ✓，未来任何候选机制适用）

```
$$\text{若某候选机制只能做到下列任一，}\textbf{直接 STOP}\ ✗:$$
$$\qquad①\ \text{判断 Booleanity};\quad ②\ \text{重新表达 }0\le x\le1;\quad ③\ \text{给每个中心增加局部不等式};\quad ④\ \text{改写 excess};\quad ⑤\ \text{改写 support};\quad ⑥\ \text{给出另一个 moment};\quad ⑦\ \text{给出一个 relaxation}\ ✓$$
$$\textbf{唯一出路}:\ \boxed{\text{产生新的\textbf{跨中心耦合}／\textbf{全局整数障碍}}}\ ✓\ \text{并且必须回答}:\ \boxed{\text{它究竟在哪里产生 }|C|\ \text{的额外下界？}}\ ✓$$
$$
$$
```

---

## §4 下一轮协议：source-first frontier audit（唐先生 09:42 ✓）

```
$$\textbf{目标空间}:\ \text{停止覆盖码搜索}\ ✗\ \Longrightarrow\ \text{RoSQS／Steiner 类 cell}\ ✓$$
$$\textbf{流程（严格 ✓）}:\quad \text{frontier search}\ \to\ \text{object fingerprint}\ \to\ P0\ \to\ P1\ \to\ P2\ \to\ \text{attack}\ ✓$$
$$\textbf{要防的失败模式}:\ \text{"数据库写 Open}\ \to\ \text{我们开始算}\ \to\ \text{发现 1990/2000 年代已有定理"}\ ✗\ \Longrightarrow\ \textbf{source-first}\ ✓\ \text{（先读原文／权威表，再动算 ✓）}$$
$$\textbf{要找的不是"另一个 Open 数字"}\ ✗,\ \text{而是}:\ \boxed{\text{已有构造／分类对象}\ +\ \text{一个尚未被利用的压缩机制}\ +\ \text{一个小而明确的数量差距}}\ ✓$$
$$\textbf{首道硬门}:\ \boxed{\text{有没有一个新的 P1 障碍，能把"存在对象"转化为可证明的\textbf{整数／秩／谱／交数下界}？}}\ ✓\ \text{没有 ⟹ }\textbf{连 SAT 都不开}\ ✗$$
$$\textbf{优先检查族}:\ \text{Steiner／partial Steiner};\ \text{resolvable／almost-resolvable};\ \text{small-order RoSQS};\ \text{constant-weight／covering designs};\ \text{finite geometry 小参数 cell};\ \text{有显式 incidence matrix 的分类问题}\ ✓$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0 措辞为**唐先生指定** ✓（OPEN/BLOCKED ✓，非 CLOSED ✗）
- §1 资产标签为**指定标签** ✓；§2 状态依本日各档 ✓（全部引用 ✓）
- §3–§4 为**协议** ✓（未执行 ✓）；**未**主张 RoSQS 族必含可用机制 ✗
- 本轮未跑 SAT／求解器 ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 source-first 协议 命中文件数=1    :: ./LEDGER-2026-09-27-k101-closed-form-and-next-round-protocol.md 
技术词 候选 STOP 清单 命中文件数=1    :: ./LEDGER-2026-09-27-k101-closed-form-and-next-round-protocol.md
```
- **本档新增**：119 终局措辞（OPEN/BLOCKED）、候选 STOP 清单、source-first 协议（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：p2b 结果、M-1/M-2A/M-2A′/M-2B 状态、107 下界、Kramer–Mesner
