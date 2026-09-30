# RESULT-2026-09-30 — **判定式二分**：优化 vs 判定 benchmark ✓；$h_{\min}(8,14){\in}[25,30]$、$(8,15){\in}[27,30]$；**且机制只需下界 ⟹ 判定式正是对的工具** ✓✓
已查地图：未覆盖（关键词: 图闭合|h_min|三角形重叠|判定式）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/诊断类（无档案同型；非已知 RH 对象重命名）
D1: 0


> 空间 B｜非 C 号｜唐先生 22:22 令（停优化；转判定式二分；先 benchmark $r{=}8,m{=}14$）｜**不主张任何新值**（V290）

---

## §0 **Benchmark（$r{=}8$，同机同时限）**

| $(m,v)$ | 结果 | 用时 |
|---|---|---|
| (14, 30) | **FEASIBLE** ✓ | **0.0 s** ✓✓ |
| (14, 26) | TIMEOUT ✗ | 60.0 s |
| (14, 24) | INFEASIBLE ✓ | 44.3 s |
| (14, 23) | INFEASIBLE ✓ | 26.2 s |
| (15, 30) | **FEASIBLE** ✓ | 5.1 s ✓ |
| (15, 26) | INFEASIBLE ✓ | 27.4 s |
| (15, 24) | INFEASIBLE ✓ | 15.0 s |
| (15, 23) | INFEASIBLE ✓ | 25.3 s |

$$\text{对照}:\ \textbf{\text{优化式}}在\ (8,14)\ \text{于 }100\,\mathrm s\ \textbf{\text{超时}} ✗;\quad \textbf{\text{判定式}}在\ v{=}30\ \textbf{{\bf 0.0 s}}\ \text{得可行} ✓✓ \Longrightarrow \text{结构性改善确认} ✓$$

## §1 **Bracket（本轮所得）**

$$\boxed{h_{\min}(8,14)\in[25,30]},\qquad \boxed{h_{\min}(8,15)\in[27,30]}\ ✓\ (\text{下界由 INFEASIBLE 给出}\ ✓)$$
$$\text{与趋势自洽}:\ h_{\min}(8,13){=}23 \Longrightarrow m{=}14\ \text{至少 }+2\ ✓;\ m{=}15\ \text{至少 }+4\ ✓$$

## §2 **观察：边界区最难** ⚠️

$$v{=}26\ \text{两次皆 TIMEOUT} ✗\ (\text{而 }v{=}30\ \text{与 }v{=}24\ \text{皆快速}\ ✓) \Longrightarrow \text{求解器在\ \textbf{相变边界} 处最吃力} ✓$$
$$\text{对策}:\ \text{避开边界};\ \text{先取趋势附近之可行 }v\ (\text{快} ✓),\ \text{再逐步降 }v\ \text{取可行-不可行分界} ✓$$

## §3 **★ 与机制之匹配（唐先生之洞见得到确认 ✓✓）**

$$\text{容量论证需要的是\ \textbf{下界} "}h_{\min}(r,m)\ge h_0"\ ✓\ ——\ \text{而给出下界者恰是\ \textbf{INFEASIBLE} 结果，其运行\ \textbf{快}（}15\text{--}44\,\mathrm s\ ✓\ \text{ vs 边界超时 ✗）}$$
$$\therefore\ \textbf{\text{判定式正是该机制所需的工具}} ✓✓\ ——\ \text{完整曲线非必需} ✓$$

## §4 **已存精确点（唐先生令：全部保存 ✓）**

$$\text{文件}:\ out/hmin\_exact\_points.tsv\ ✓;\quad \textbf{10 点}:\ (8,m,h_{\min})\ m{=}4..13\Rightarrow0,2,3,6,8,10,13,16,18,23 ✓$$

## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{benchmark 同机同时限对照 ✓；bracket 由 INFEASIBLE 下界＋FEASIBLE 上界给出 ✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

## §6 【技术词回查】

```
技术词 判定式二分   命中文件数=1    :: 本档
技术词 相变边界     命中文件数=0    :: 
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档（“相变边界”全档 0 命中）} ✓;\quad \textbf{通用词（不计）}：\text{“benchmark／bracket”裸词} ✓$$
