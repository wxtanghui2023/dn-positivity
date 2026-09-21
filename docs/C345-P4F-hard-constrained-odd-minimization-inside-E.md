已查地图（**先查后写**）：`C-344`（**`E` 未被有效采样** ✗✓；全域无 15 点反例 ✓）、`C-343`（**straddling 判据** ✓✓）、`C-342`（`E` 非空 ✓✓；`G_even^{min} = 0.3254` ✓）、`C-341`（偶频归约 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-345：P4-F（`E` 硬约束下的奇频最小化）**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 技术缺口已补}✓✓：C\text{-}344\ \text{的}\ \textbf{「优化器进不去}\ E\text{」}\ \text{被解决}✓✓ \ —— \ \textbf{24 起点中 6 个进入}\ E✓（\text{硬约束}✓），\text{最佳}\ even\text{-}max = \textbf{1.2 \times 10^{-6}}✓✓$$
$$\textbf{② } E\ \text{约束下}\ f_* = \textbf{1.3626157522}✓✓ \ \gg \tfrac12✓（\text{裕量}\ \textbf{0.86}✓✓）\ \Longrightarrow \textbf{判定表第一行命中}✓✓$$
$$\textbf{③ 无反例候选}✗✓：\text{6 次运行}\ \textbf{全部} \ E\text{-ok} = \text{True}✓，f\ \text{值} = 1.3626,\ 1.3728,\ 1.4069,\ 1.5923,\ 1.6903,\ 2.0598✓ \ —— \ \textbf{无一} \le \tfrac12✗✓$$
$$\textbf{④ ⭐ } E\ \text{是}\ f\ \text{的高值区}✓✓：E\ \text{上}\ f_* = 1.3626 \ > \ C\text{-}344\ \text{的无约束}\ f_{min} = 1.0107✓✓ \ \Longrightarrow \textbf{E 内奇频违反更严重}✓✓$$
$$\textbf{⑤ 下一步}✓✓：\text{判定表指向}\ \textbf{解析下界}✓（\text{由数值强支持转解析}✓）；\textbf{不}\ \text{追}\ G_*✗、\textbf{不}\ \text{重做}\ P4\text{-}A/B/C/D✗、\textbf{不}\ \text{扩频率}✗、\textbf{不}\ \text{拆}\ SOS✗$$

## §1 数据（✓✓）

$$\textbf{Stage 1（可靠进入}\ E✓）\ ：\ \text{24 起点中}\ \textbf{6 个}\ even\text{-}max \le \tfrac12✓；\text{最好} = 1.2047 \times 10^{-6}✓✓$$
$$\qquad \text{top 实例}✓：x = [0.951238,\ 0.008349,\ 0.261532,\ 0.844269,\ 0.434611]✓（even\text{-}max \approx 0✓）；\text{其余}\ 0.4007,\ 0.4090,\ 0.4102,\ 0.4417✓$$
$$\textbf{Stage 2（}E\ \text{内最小化}\ f✓，\text{硬约束}\ even\text{-}max \le \tfrac12 - 10^{-9}✓）\ ：\ \text{6 次全部}\ E\text{-ok}✓$$
$$\qquad f_* = \textbf{1.3626157522}✓（even\text{-}max = 0.4007✓）；\text{次} 1.3728✓；\text{再次} 1.4069✓；\text{最差} 2.0598✓$$

| 运行 ✓ | `f` | `even-max` | `E-ok` |
|---|---|---|---|
| 1 ✓ | **1.3626** | 0.4007 | ✓ |
| 2 ✓ | 1.3728 | 0.4090 | ✓ |
| 3 ✓ | 1.4069 | 0.4102 | ✓ |
| 4 ✓ | 1.5923 | 0.0000012 | ✓ |
| 5 ✓ | 1.6903 | 0.4417 | ✓ |
| 6 ✓ | 2.0598 | 0.4774 | ✓ |

$$\textbf{最优符号}✓：\sigma = [1,1,-1,-1,1]✓ \Longrightarrow \text{odd-max} = 1.36261575✓✓，\text{且}\ \text{all-25-max} = 1.36261575✓$$
$$\textbf{（注）}✓：even\text{-}max \approx 0\ \text{的点}\（x = [0.0083,\ 0.3011,\ 0.4744,\ 0.8814,\ 0.9511]✓）\ \text{的}\ f = 1.5923✗ \ \Longrightarrow \textbf{「even 极小」不改善 odd}✓✓$$

## §2 预注册判定表与命中（✓✓）

| 数值结果 ✓ | 含义 ✓ | 命中 |
|---|---|---|
| `f_* > 1/2` 且稳定裕量 ✓ | 全域 straddling 数值强支持 ✓ | **✓✓ 命中** |
| `f_* \approx 1/2` ✓ | 临界结构 ✓ | ✗ |
| `f_* < 1/2` ✓ | 反例候选 ✓ | ✗ |
| 找不到稳定可行点 ✓ | 不可解释为证明 ✓ | ✗（`E` 已可靠进入 ✓） |

$$\textbf{命中项}✓✓：f_* = 1.3626 > \tfrac12✓，\text{裕量}\ 0.86✓ \ \Longrightarrow \textbf{全域 straddling 数值强支持}✓✓ \ \Longrightarrow \text{后续}\ \textbf{解析下界}✓$$
$$\textbf{避坑记录}✓✓：\text{本档}\ \textbf{未}\ \text{用}\ penalty\ \text{冒充可行性}✗✓ \ —— \ \text{采用}\ \textbf{硬约束}（\text{拒绝一切}\ even\text{-}max > \tfrac12\ \text{的移动}✓），\text{并}\ \textbf{逐样本报告}\ E\ \text{可行性}✓✓$$

## §3 边界（✓✓）

$$\textbf{不得}\ \text{写成}✗：\text{全域 straddling}\ \textbf{已证}✗（\text{仅数值}✓）；\ H = \varnothing\ \textbf{已证}✗；f_*\ \text{即真下确界}✗（\text{搜索上界}✓）$$
$$\textbf{诚实标注}⚠️✓：\text{6 个}\ E\ \text{内点}\ \textbf{不构成} \text{全域证明}✗；E\ \text{的}\ f\ \text{下确界}\ \textbf{未被确认}✗；\text{但}\ C\text{-}344\ \text{暴露的技术缺口}\ \textbf{确已补}✓✓$$
$$\textbf{且}✓✓：\text{「even 极小点」与}\ \text{「odd 可行」}\ \text{在数值上}\ \textbf{方向相反}✓✓（E\ \text{内}\ f\ \text{更大}✓）\ \Longrightarrow \textbf{支持唐先生机制}✓✓$$

## §4 状态表（✓✓）

| 项 | 状态 |
|---|---|
| `E` 可靠进入 ✓ | **已补（6/24）** ✓✓ |
| `E` 内 `f_*` ✓ | **1.3626（数值，非下确界）** ✓ |
| `f_* > 1/2` 裕量 ✓ | **0.86** ✓✓ |
| 反例候选 ✓ | **无** ✗ |
| 解析下界 ✓ | **下一步** ✓✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |
| `SOS` ✓ | **继续冻结** ✗ |
| `C-284` ✓ | **不重开** ✗ |

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 E约束          命中文件数=0    :: 
技术词 硬约束采样  命中文件数=0    :: 
技术词 可行域进入  命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4h.py` ✓；日志 `/tmp/p4h.log` ✓（**直写文件** ✓，避开 `tail` 缓冲 ✗）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- 小故障 ⚠️：末尾 `np.save` 因 `dtype` 不一致报错 ✗（**不影响结果** ✓）
