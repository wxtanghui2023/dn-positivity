已查地图：命中（`CAPMIX1B-B11-1-nonsubfield-extremal-E-half-supported-38-falsified`）⟹ 执行其 §5 之 `E_{1/2}` 触发搜索，不开新案
D0: 本档对象 = **`B11.3` 跨特征 `E_{1/2}` 触发搜索**（439 例）⟹ ⛔⛔**`E_{1/2}` 被 24 例非子域反例击穿**；⛔ **命题 `AA\setminus\{1\}\subseteq A` 被 50 例反证**；⭐ 尺度线索（两模型，一真一假，**不拟合**）
D1: 1 （新自由度：`E_{1/2}` 否定 ＋ 命题否定 ＋ 尺度问题的两候选模型与其失效点定位）
[RESEARCH]

# **`CAP-MIX-1B · B11.3`：`E_{1/2}` 否定与命题反证**

## §1 ⛔⛔ `E_{1/2}` **FALSE**（跨特征扫描，24 例非子域反例）

```
$$\text{网格}:\ p\in\{2,3,5,7,11,13\},\ q\le 28561,\ \text{全部 }d\ge3\ \Longrightarrow\ \text{总案例}=439;\qquad \rho>1/2:\ 101\ \text{例}$$ ✓
$$\boxed{\text{其中\textbf{非子域}者}=24}\ \Longrightarrow\ \boxed{E_{1/2}\ \textbf{否定}}$$ ✓✓✓
$$\begin{array}{c|c|c|c|c}
p,n&d&\lambda&\rho&\text{备注}\\
\hline
3,3&13&7&0.5385&d=(q-1)/2\ (\text{指标 }2)\\
3,5&121&61&0.5041&d=(q-1)/2\\
3,7&1093&547&0.5005&d=(q-1)/2\\
3,6&13&7&0.5385&d\mid q-1,\ \text{非子域}\\
3,9&13&7&0.5385&\text{同上}\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \text{"}\rho>1/2\Rightarrow G\cup\{0\}\ \text{是子域"}\ \textbf{不成立};\ \text{反例族}:\ \text{指标 }m\ \text{小的子群}\ (\text{尤 }m=2)$$ ✓✓
$$(\text{char 2 侧仍零反例}:\ \text{非子域 max }\rho=0.381=\frac8{21}\ \Longrightarrow\ \textbf{char 2 与奇特征行为不同})$$ ✓✓
```

## §2 ⛔ 命题 `AA\setminus\{1\}\subseteq A` **被反证**（50 例）

```
$$\textbf{实测}: 50\ \text{例失败},\ \text{含子域情形本身};\ \text{例}:\ (p{=}3,n{=}2,d{=}7),\ (3,3,13),\ (3,4,80),\dots$$ ✓✓
$$\textbf{解析原因（预判并获确认）}:\ \text{子域 }G=\mathbb F_{p^k}^\times\ \text{时}\ A=G\setminus\{-1\},\ AA=G\ (\text{需 }d\ge4)$$ ✓
$$\Longrightarrow\ -1\in AA\setminus\{1\}\ \text{但}\ -1\notin A\ \Longrightarrow\ \boxed{AA\setminus\{1\}\not\subseteq A}$$ ✓✓✓
$$\Longrightarrow\ \text{该命题\textbf{恰在其本应刻画的情形（子域）失效}};\ \Longrightarrow\ \text{此路线\textbf{关闭}}$$ ✓✓
```

## §3 ⭐ 尺度线索（**两模型，一真一假，不拟合**）

```
$$\text{模型甲}:\ \lambda\approx\frac{d^2}{q}\ (\text{随机/Weil 主项}):$$
$$\qquad \text{吻合}:d{=}5461(q{=}16384):\ 1820\ \text{vs}\ 1848;\quad d{=}1365:\ 455\ \text{vs}\ 440;\quad d{=}341:\ 114\ \text{vs}\ 120$$ ✓✓
$$\qquad \textbf{失效}: (n{=}12,d{=}21):\ \frac{441}{4096}=0.108\ \text{vs}\ \lambda=8\ (\text{差 }74\times)$$ ✗✗
$$\text{模型乙}:\ \rho\approx\frac1m,\ m:=\frac{p^{\mathrm{ord}_d(p)}-1}{d}\ (\text{在最小子域内的指标}):$$
$$\qquad \text{吻合}:m{=}1\ (\text{子域})\Rightarrow\rho\approx1;\quad m{=}3\Rightarrow\rho\approx\frac13\ (d{=}21,93,381,5461,1365,45,85\ \textbf{聚集在 }1/3);\quad m{=}2\Rightarrow\rho\approx\frac12$$ ✓✓
$$\qquad \textbf{失效}:(n{=}10,d{=}93, m{=}11):\ \text{预测}\approx8.45\ \text{vs}\ \lambda=32$$ ✗
$$\Longrightarrow\ \boxed{\text{尺度问题\textbf{未定}};\ \text{两模型各有吻合区与失效区}\ \Longrightarrow\ \text{须走 Weil/特征和的\textbf{精确}分析，不拟合}}$$ ✓✓✓
$$\textbf{关键观察}:\ d{=}21\ \text{在 } n{=}6\ \text{与}\ n{=}12\ \text{的}\ \lambda\ \textbf{完全相同}(=8)\ \Longrightarrow\ \lambda\ \text{只依赖最小包含子域}\ \mathbb F_{p^{\mathrm{ord}_d(p)}}$$ ✓✓
```

## §4 判词与本支线状态

```
$$\boxed{E_{1/2}\ \text{否定};\quad \text{命题否定};\quad \text{尺度未定（但已定位两模型）}}$$ ✓✓
$$\text{存活}:\ (i)\ \text{子域刻画}\ \rho\to1\iff G\cup\{0\}\ \text{是子域（}\Longleftarrow\ \text{已证；}\Longrightarrow\ \text{char 2 内经验成立）};\ (ii)\ \text{B9 定理};\ (iii)\ \text{尺度线索}$$ ✓
$$\text{关闭}:\ E_{1/2}\ \text{路线};\quad AA\setminus\{1\}\subseteq A\ \text{路线}$$ ✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停；**不回 RH**；**不做拟合** ✓
【数据】 `out/capmix1B11c_half.txt`；脚本 `scripts/capmix1B11c_half_test.py` ✓
【边界】 §1/§2 为实测（439 例）；§3 两模型均已标出吻合区与**失效点** ✓

## §附 【技术词回查】（补录）
```
技术词 character sum    命中文件数=3    :: ./C305-FSD-blind-spot-audit-program-four-classes-dual-ledger-five-rounds.md ./V228-root-edge-barrier-audit-analytic-barrier-impossible.md ./ref-bc-ar5iv-plaintext.txt 
技术词 index            命中文件数=101  :: ./B-SERIES-INDEX.md ./round2-index-status.md ./C293-astra-liouville-source-verification-and-mangerel-grh-anchor.md 
```
