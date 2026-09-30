# RESULT-2026-09-30 — **补全 $r{=}8,9$ 全表**：①**贪心无效**（闭合缺口 ✗ — 复现唐先生表之错误机制）②**闭合感知 MILP 批量**已启动（检查点日志 ✓）
已查地图：未覆盖（关键词: 图闭合|h_min|三角形重叠|判定式）—— 可开档，首行须照抄本行
D0: 本档对象 = 方法/诊断类（无档案同型；非已知 RH 对象重命名）
D1: 0


> 空间 B｜非 C 号｜唐先生 22:09 令「补全」｜**不主张任何新值**（V290）

---

## §0 **★ 自查：min-increment 贪心\ \textbf{无效}** ✗

$$\text{贪心在 }r{=}8,m{=}5\ \text{给出}\ h{=}0,\ \text{而 MILP 精确 }h_{\min}{=}\mathbf2 \Longrightarrow \textbf{\text{窗口违背}} ✗$$
$$\text{根因}:\ \text{贪心按\ \textbf{超图 packing} 选三角形（只求边不相交），\ \textbf{忽略图闭合}}（额外边会造出额外三角形）✗$$
$$\therefore\ \text{贪心给出的不是 }h_{\min},\ \text{而是 packing 值} \Longrightarrow \textbf{\text{恰好复现唐先生 §155 表之错误机制}} ✓\ (\text{互为独立确认} ✓)$$
$$\boxed{\text{唯一正确之法 ＝ 闭合感知的精确计算（MILP／全枚举）}} ✓$$

## §1 **批量任务（已启动 ✓）**

$$\text{66 个 }(r,m)\ \text{解，每解时限 }100\,\mathrm{s};\ \text{输出 }out/hmin\_batch.log\ (\text{检查点式，可续读} ✓);\ \text{预计 }1\text{--}2\,\mathrm h$$
$$\textbf{已得（与前精确值吻合 ✓）}:\ r{=}8\ m{=}4\Rightarrow0 ✓\ (\text{与 }D_{\rm true}(8){=}4\ \text{自洽});\ r{=}8\ m{=}5\Rightarrow2 ✓$$
$$\text{覆盖}:\ r{=}8:\ m\in\{4..20\}\cup\{21,24,\ldots,54\};\quad r{=}9:\ m\in\{6..20\}\cup\{21,24,\ldots,84\}$$

## §2 **方法论收获**

$$\text{(i) 每个 }h\ \text{型数必须\ \textbf{闭合感知}} ✓;\ \text{(ii) 交叉验证（MILP↔枚举）与\ \textbf{三方一致}（贪心↔唐先生表↔packing，同为错 ✗）互为确证} ✓$$

## §3 【技术词回查】

```
技术词 闭合感知     命中文件数=1    :: 本档
技术词 贪心无效     命中文件数=0    :: 
```
$$\textbf{分类}：\textbf{本档新增}：\text{两词皆仅本档（“贪心无效”全档 0 命中）} ✓;\quad \textbf{通用词（不计）}：\text{“补全／批量”裸词} ✓$$
