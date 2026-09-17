# 🧭 **PRE-WORK MAP CHECK**（开工前查地图 · 2026-09-17 唐先生立规）

> 唐先生原话（11:43）：**「每一次，你先搜索 NO-GO 地图和总图，我不想浪费时间一次次掉坑里」** ✓✓
> **适用范围**：任何**新案子／新方向／新构造／新候选**开工**之前**（含 (甲) (乙) (丙) (i) (ii) 各支）✓

---

## §1 必查五处（顺序）

| # | 档案 | 作用 |
|:--|:--|:--|
| 1 | **`CLOSED-ROUTES-MAP.md`** | **NO-GO 地图**（≈2700 行，含逐条判死点） |
| 2 | **`MASTER-STATUS-AND-CLOSURES.md`** | **总图**（V 条目与策略档索引） |
| 3 | **`MASTER-NOGO-AND-LIVE-PATHS.md`** | 已封／活路 |
| 4 | `ASSETS-REGISTRY.md` | 已登记资产（C-x／P-x／A 系列） |
| 5 | `INDEX-BY-DIRECTION.md`｜`ID-CLAIMS.tsv` | 方向索引／编号台账 |

## §2 命令配方（可直接粘）

```bash
cd ~/.openclaw/workspace/dn-project/docs
grep -a -n -E "<关键词1>|<关键词2>|<关键词3>" \
  CLOSED-ROUTES-MAP.md MASTER-STATUS-AND-CLOSURES.md MASTER-NOGO-AND-LIVE-PATHS.md | head -30
# 命中若提到某 V/E 号，再单独读该档：
ls | grep -E "^V[0-9]+-|^E[0-9]+-" | grep -i "<关键词>" | head
```
$$\text{（}\texttt{-a}\ \text{必需：抽取的 PDF 文本含控制字符，否则 grep 报 binary）}✓$$

## §3 判定规则（**硬**）
$$\text{命中"已 DEAD／已封／已登记"}\ \Longrightarrow\ \boxed{\textbf{不得开新案}}，\ \text{直接引既有条目}✓$$
$$\text{仅当确认}\ \textbf{未覆盖} \text{才开案}，\ \text{且新档首行须写}\ \textbf{「已查地图：未覆盖（列出所查档与关键词）」}✓✓$$

## §4 ⚠️ 血泪实例（2026-09-17 当日两次）

$$\text{(a)}\ \text{我称}\ \texttt{STRATEGY}\ \text{§7 Step 3 "未执行"} \Longrightarrow \textbf{错}：\texttt{V292}\ \text{已执行}（\text{含 7 类候选对表 E1--E4}）✓✗$$
$$\text{(b)}\ \text{我拟开新案"非显式公式动力学结构}\to\text{prime-pair correlation support}>1\text{"} \Longrightarrow \textbf{双重已覆盖}（\text{见}\ §5）✓✗✓$$

## §5 🔒 **本次查证结果**（下一刀已覆盖，不得开案）
$$\textbf{覆盖一}（\texttt{CLOSED-ROUTES-MAP.md}\ \text{L1007 逐字}）：$$
$$\qquad\text{"唯一}\ \textbf{非因子化} \text{的跨素数结构}\ ＝\ \text{素数元组／间隙相关}\ \sum_{n\le x}\Lambda(n)\Lambda(n+h_1)\cdots\Lambda(n+h_{k-1}) \Longrightarrow \text{即}\ \textbf{Hardy--Littlewood 区域}；$$
$$\qquad\text{其}\ \textbf{无条件} \text{控制恰为 (a) 水平分布}\ \theta=\tfrac12\ (\text{Bombieri--Vinogradov})、(b) \text{二阶矩型估计 (Selberg)}、(c)\ \text{pair correlation}\ \textbf{Fourier 支撑}\le1；$$
$$\qquad \text{越过须}\ \textbf{support}>1 \Longrightarrow \text{即}\ \texttt{V162}\ \text{承重墙} \Longrightarrow \boxed{\text{任何无条件的}\ P_{\rm comb}\ \text{必为 (a)--(c) 的变体}} \Longrightarrow \text{按唐先生清单}\ \boxed{\textbf{立即 DEAD}}"✓✓✓$$
$$\textbf{覆盖二}（\texttt{DISCOVERY-R3-scale-memory.md}）：\text{"}\textbf{算术没有内生动力学} \Longrightarrow \text{状态是尺度的函数} \Longrightarrow \text{路径依赖只能来自观察者的压缩，不能来自算术本身"}\ ⟹ \textbf{D1}\ =\ 0✓✓$$
$$\qquad(\text{配套}：\texttt{AOB2-scale-dynamics-phase-sources.md}\ \text{登记"char 0 算术尺度动力学"任务，约束：}\textbf{不借用显式公式／Weil／HP 作构造起点、无}\ 1/2\ \text{输入}；\ \texttt{ABD-1-equality-attractor.md}\ \text{已实算等式吸引子并预设"先杀"判据})✓$$

$$\Longrightarrow\ \boxed{\text{下一刀（动力学}\to\text{support}>1\text{）}\ \textbf{双重已覆盖} \Longrightarrow \textbf{不开}}✓✓✓$$

## §6 纪律
$$\text{(i)}\ \text{本协议}\ \textbf{每次开工前} \text{执行，}\ \text{结果写进新档首行}✓\quad\text{(ii)}\ \textbf{不因"上次查过"而省略}（\text{地图在长}\text{）}✓$$
$$\text{(iii)}\ \text{同日立规}\ \&\ \text{同步写进工作区}\ \texttt{AGENTS.md}\ \text{全局约束}✓$$
