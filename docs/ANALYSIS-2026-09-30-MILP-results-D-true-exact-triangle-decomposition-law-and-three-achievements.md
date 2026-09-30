# ANALYSIS-2026-09-30 — MILP 结果分析：$D_{\rm true}$ 全表 ✓、**三角形分解律**、四项成果、三项缺口

> 空间 B｜非 C 号｜唐先生 22:08 令（取回结果并分析成果）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-MILP-validates-enumeration-…`／`ERRATUM-2026-09-30-graph-closure-…`／`SUMMARY-2026-09-30-all-routes-…`
D0: 本档对象 = **结果分析与结构律提炼**（分析类 ✓）
D1: 0（产出 = **四项成果 ＋ 一条结构律 ＋ 三项缺口** ⚠️✓）

---

## §0 **取回之数据**

| 量 | 值 |
|---|---|
| $D_{\rm true}(r),\ r{=}3..9$ | $\mathbf{1,1,2,2,3,4,6}$ ✓（MILP） |
| $r{=}8$ $h_{\min}$ | $m{=}0,3,5,9,12\rightarrow0,0,2,10,18$；$m{=}40\rightarrow\mathbf{236}$；$m{=}56\rightarrow\mathbf{420}$ |
| $r{=}9$ $h_{\min}$ | $m{=}0,3,5\rightarrow0,0,0$ |
| 超时 ✗ | $r{=}8$: $m{=}20,30$；$r{=}9$: $m\ge9$（每解 60 s） |

## §1 **成果一：交叉验证通过 ✓✓**

$$\text{MILP}\leftrightarrow\text{全枚举在 }r\le7\ \text{\textbf{逐位一致}}（1,1,2,2,3） \Longrightarrow \text{枚举无 bug} ✓;\ \textbf{\text{图闭合修正为真}} ✓$$
$$\Longrightarrow \textbf{\text{唐先生 §155 }h_{\min}\ \text{表与 §154 }D(r)\ \text{自 }r{=}4\ \text{起全部不可达}} ✗\ (r{=}9:\ 12\ \text{vs 真值}\ \mathbf6)$$

## §2 **成果二：结构律（本档核心 ✓）**

$$\boxed{h_q=0\iff\text{每条边恰属一个三角形}\iff L_q\ \text{是\ \textbf{三角形分解}}} \Longrightarrow D_{\rm true}(r)=\max\{\text{此类分解之尺寸}\}$$
$$\textbf{两类极值构造}:\ F_k\ (\text{友谊},2k{+}1\ \text{点},\ k\ \text{三角形})\ \text{给}\approx(r-1)/2;\quad \textbf{网格}\ k\times k\ (k\ \text{行}+k\ \text{列}=2k\ \text{三角形})\ \text{给}\ 2\lfloor\sqrt r\rfloor$$
$$r{=}9:\ \text{友谊 }4\ \textbf{<}\ \text{网格 }\mathbf6 ✓\ (\text{3×3 网格：}6\ \text{三角形、}18\ \text{边、每边恰属一}\ ✓) \Longrightarrow \textbf{\text{前档"}}D_{\rm true}\sim r/2\text{"应修正} ✗$$
$$\therefore\ D_{\rm true}\ \text{增长快于 }r/2\ \text{但远小于 packing}（r{=}9{:}\ 6\ \text{vs}\ 12）✓$$

## §3 **成果三：$\Sigma h\le2A_2(R)$ 比预想更紧 ✓**

$$r_q{=}9\ \text{之\ \textbf{免费复用仅 6}}（\text{非 12} ✗） \Longrightarrow \text{超过 6 次复用即需 }h\ge1 \Longrightarrow \textbf{\text{h 惩罚更早生效}} ✓\ (\text{对机制为收紧} ✓)$$

## §4 **成果四：校准律"Jensen 从不紧"** ✓

$$\text{3 例}:\ r{=}4,m{=}2:\ 0\ \text{vs}\ 1;\quad r{=}6,m{=}6:\ 3\ \text{vs}\ 7;\quad r{=}8,m{=}40:\ \mathbf{200}\ \text{vs}\ \mathbf{236}\ ✓$$
$$\Longrightarrow \textbf{\text{一切 }h\ \text{型界必须精算（Jensen 只能作下界）}} ✓$$

## §5 **三项缺口（诚实 ⚠️）**

$$\text{(i)}\ r{=}8\ m\in[13,55]\ \text{与}\ r{=}9\ m\in[6,84]\ \text{未精算} ✗\ (\text{超时};\ \text{可\ \textbf{提高单解时限}／加 warm-start 修} ✓);\quad \text{(ii)}\ W\ \text{下界} ✗;\quad \text{(iii)}\ A_2(R)\ \text{上界} ✗$$
$$\text{另}:\ \text{全链承重件}\ e(U)\le71-i\ \text{仍\ \textbf{未经核验}} ⚠️\ (\text{见 SUMMARY §3(7)})$$

## §7 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 三角形分解律   命中文件数=1    :: 本档
技术词 Jensen     命中文件数=2    :: 本档 ./RESULT-2026-09-30-MILP-…（同一系列）
```

$$\textbf{分类}：\textbf{本档新增}：\text{“三角形分解律”仅本档} ✓;\quad \textbf{档案已有（同一系列）}：\text{“Jensen”另一命中为本系列前档} ✓;\quad \textbf{通用词（不计）}：\text{“校准／分解”裸词} ✓$$


## §6 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{交叉验证✓；前档 }D_{\rm true}\sim r/2\ \text{之说\ \textbf{自我修正}} ✗;\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$
