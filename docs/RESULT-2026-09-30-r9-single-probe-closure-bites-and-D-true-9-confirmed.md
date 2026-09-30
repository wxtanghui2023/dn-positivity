# RESULT-2026-09-30 — $r=9$ 单探针：**闭合亦咬** ✓✓（同型现象复现）；并**独立确认** $D_{\rm true}(9)=6$ ✓

结论: 已查地图：未覆盖（关键词: r9_diag|单探针|闭合咬）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/核验类（无档案同型；非已知 RH 对象重命名）
D1: 0

## §0 结果

| $m$ | $J$ | hyper-min | 图在 $v{=}$hyper 处 | 判读 |
|---|---|---|---|---|
| 6 | 0 | 0 | **FEASIBLE** (0.0 s) | 不咬（与 $D_{\rm true}(9){=}6$ 自洽 ✓✓） |
| 9 | 0 | 0 | **INFEASIBLE** (0.0 s) | **闭合咬** ✓ |
| 12 | 0 | 0 | **INFEASIBLE** (0.0 s) | **闭合咬** ✓ |
| 15 | 9 | TIMEOUT ✗ | — | hyper 自身超时 ⚠️ |
| 20 | 24 | TIMEOUT ✗ | — | 同上 ⚠️ |

## §1 两条收获

$$\textbf{(a) 现象复现} ✓✓:\ r{=}9\ \text{在}\ m\ge9\ \text{闭合同样咬} \Longrightarrow \text{与}\ r{=}8\ \text{同型} \Longrightarrow \text{唐先生升格判据之第一半满足} ✓$$
$$\textbf{(b) 独立交叉验证} ✓✓:\ m{=}6\ \text{可行}＋m{=}9\ \text{不可行}\ \Longrightarrow 6\le D_{\rm true}(9)<9\ \Longrightarrow \textbf{\text{确认 MILP 之 }D_{\rm true}(9){=}6} ✓$$

## §2 新障碍（诚实 ⚠️）

$$\text{大 }m\ \text{时\ \textbf{hyper-min 自身超时}} ✗\ (r{=}9:\ 84\ \text{三元组＋配对变量})\ \Longrightarrow \text{三级对比之大 }m\ \text{段需换法（如利用 }r=8\ \text{之结构或改判定式求 hyper 侧）} ⚠️$$

## §3 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{三项皆 0.0 s 实测} ✓;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §4 【技术词回查】

```
技术词 单探针    命中文件数=1
技术词 闭合咬    命中文件数=1
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{通用词（不计）}：\text{"探针／同型"裸词} ✓$$
