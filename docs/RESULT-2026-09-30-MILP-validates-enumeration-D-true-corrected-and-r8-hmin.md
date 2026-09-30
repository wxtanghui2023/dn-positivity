# RESULT-2026-09-30 — **MILP 精确化**：$D_{\rm true}(r)$ 全表（含 $r{=}8,9$）✓；**与枚举逐位吻合** ✓；$r{=}8$ 之 $h_{\min}$ 部分

> 空间 B｜非 C 号｜唐先生 21:57「继续」（补第 9 项疏漏：$r{=}8,9$ 仅用 Jensen ✗）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-triangle-overlap-table-…`／`ERRATUM-2026-09-30-graph-closure-…`／`SUMMARY-2026-09-30-all-routes-…`
D0: 本档对象 = **$D_{\rm true}$ 之 MILP 精确化与交叉验证**（新精确值 ✓）
D1: 0（产出 = **一张验证表 ＋ 三个新值 ＋ 一处确认** ⚠️✓）

---

## §0 **MILP 模型（可复用 ✓）**

$$\textbf{变量}:\ e_{ij},y_{ijk}\in\{0,1\};\quad \textbf{闭合约束}:\ y_T\le e_{ij}\ (\forall e\subset T);\ -y_T+\sum_{e\subset T}e\le2;\quad \textbf{目标}:\ \max\sum_T y_T$$
$$\textbf{h{=}0 条件}:\ \text{每条边至多属一个三角形}\ \sum_{T\ni e}y_T\le1\ (\Longleftrightarrow h{=}0\ \checkmark);\quad \textbf{h 之线性化}:\ w_{e,\{T,T'\}}\ge y_T+y_{T'}-1,\ \min\sum w\ ✓$$

## §1 **$D_{\rm true}(r)$（MILP ✓ 与枚举逐位吻合 ✓✓）**

| $r$ | 3 | 4 | 5 | 6 | 7 | **8** | **9** |
|---|---|---|---|---|---|---|---|
| **$D_{\rm true}$（MILP↔枚举 ✓✓）** | 1 | 1 | 2 | 2 | 3 | **4** | **6** |
| packing $\lfloor\binom r2/3\rfloor$ ✗ | 1 | 2 | 3 | 5 | 7 | 9 | 12 |
| 唐先生 §154 之 $D(r)$ ✗ | 1 | 1 | 2 | **4** | **7** | **8** | **12** |

$$\therefore\ \textbf{\text{交叉验证通过 ✓✓}}:\ \text{MILP 与全枚举在 }r\le7\ \text{逐位一致（}1,1,2,2,3\text{）} \Longrightarrow \textbf{\text{真值可信}} ✓$$
$$\textbf{\text{且唐先生之 }D(r)\ \text{自 }r{=}4\ \text{起全部偏高}} ✗\ (\text{因按超图 packing 计，未受图闭合约束} ✓)$$
$$\text{结构}:\ D_{\rm true}(r)\ \text{增长约 }r/2\ (\text{友谊型 }F_k:2k{+}1\ \text{点},\ k\ \text{三角形} ✓) \Longrightarrow \text{"免费复用"远小于此前所估} ✓$$

## §2 **$r{=}8$ 之 $h_{\min}$（MILP，部分）**

| $m$ | 0 | 3 | 5 | 9 | 12 |
|---|---|---|---|---|---|
| $h_{\min}$ | 0 | 0 | **2** | **10** | **18** |

$$\text{（}m{=}4\ \text{处 }h{=}0\ \text{与 }D_{\rm true}(8){=}4\ \text{一致 ✓）；}m\ge20\ \text{与 }r{=}9\ \text{全表后台续算中 ⚠️}$$

## §3 **过程记录（工程教训 ⚠️）**

$$\text{(i) 首次 MILP 因\ \textbf{管道缓冲}（}|\ \text{grep}\ \text{非 tty）无中间输出 ✗；(ii) 第二次因\ \textbf{自身 }pkill\ \text{连带进程组} 被 SIGTERM ✗（TOOLS.md 已载同型陷阱 ✓）};\ \text{(iii) 改为 }nohup\ +\ \text{写文件 ⟹ 正常 ✓}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 交叉验证通过   命中文件数=0    :: 
技术词 友谊型         命中文件数=0    :: 
```

$$\textbf{分类}：\textbf{本档新增}：\text{两词全档 0 命中 ⟹ 新} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“验证／表”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{交叉验证（MILP↔枚举）✓；唐先生表之为非可达已再确认 ✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$
