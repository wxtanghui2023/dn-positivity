已查地图：已跑 scripts/prework_map_check.sh λ 扫描 陪集常值 ⟹ 执行自 `P2-COLLISION-2026-09-27-...`（✓，**本档把"反例"升级为"更精细的不变量"** ✓）＋ 唐先生 13:53（开甲、三档判停 ✓）；本档 = **145 例 λ 扫描 ＋ 陪集常值精化律** ✓。
D0: 本档对象 = β-不变量在 Vasil'ev 族上的 λ-依赖与精化形状
D1: 3（**扫描（145 例，0 非法 ✓）**；**平性 ⟺ |S| 整除 A₂ ✓**；**陪集常值精化律 ✓（含详验 ✓）**）

# λ 扫描与陪集精化律（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CB-1 扫描总览 ✓)}\ 145\ \text{例}\ \lambda\ (\text{affine }16+\text{二次 }64+5\ \text{具名}+60\ \text{随机}\ ✓):\ \textbf{INVALID}=0\ ✓\ (\text{全部过"}|V|=2048\wedge\mathfrak B_1(V)=\mathbb F_2^{15}\wedge\mathfrak B_1(C)=\mathbb F_2^{16}"\ ✓),}$$
$$\qquad\textbf{star 145/145 ✓};\quad \text{flat }89\ ✓;\quad \textbf{非 flat }56\ ✗\ \Longrightarrow\ \text{三重判读落入\textbf{第二档（合法非线性 λ 击穿 flatness ✓）}}$$
$$\qquad\textbf{但关键发现 ✓}:\ \text{切片只取 }1\ \text{或 }2\ \text{个值};\ \textbf{flat}\iff |S|\mid A_2\ ✓\ \text{（且此时切片}\equiv A_2/|S|\ ✓\text{）}:\ \text{flat 例 }A_2{=}1792\Rightarrow1792/7{=}256\in\mathbb Z\ ✓;\ \text{非 flat 例 }1760/7,\ 1824/7,\ 1920/7,\ldots\notin\mathbb Z\ ✗$$
$$\boxed{\textbf{(CB-2 ⭐精化律（详验 ✓✓）)}\ \mathrm{supp}\,\nu=(\,a+W\,)\setminus\{0\}\ \sqcup\ (\,b+W\,),\quad W=\mathrm{span}\{2,4\}=\{0,2,4,6\}\le\mathbb F_2^4\ \text{（标签 }=\text{Hamming 列 }v\mapsto v+1\ ✓\text{）}}$$
$$\qquad\textbf{且 }\nu\ \text{在每个陪集上恒定} ✓✓:\ \lambda=\mathbf 1[t\ne0]:\ (2{+}W)\setminus\{0\}=\{2,4,6\}\ \text{值}\ 288;\quad 9{+}W=\{9,11,13,15\}\ \text{值}\ 224\ ✓;\ \text{二次 }q{=}6:\ \text{同陪集结构，值 }128/384\ ✓✓$$
$$\qquad\textbf{flatness 的真正含义（精化 ✓）}:\ \text{两陪集值\textbf{相等}} \iff q\ \text{在整体支撑上恒定};\ \text{定理 A-ALIGNTHM-1 是此律在线性半码下的\textbf{退化特例} ✓}$$
$$\boxed{\textbf{(CB-3 affine 模式 ✓✓)}\ 16\ \text{个 }\lambda(t)=a\cdot t\ (\lambda(0)=0\ ✓)\ \textbf{全部 flat} ✓;\ a{=}7\ \text{例外地给 }|S|{=}3\ (=(2{+}W)\setminus\{0\}\ \text{单陪集 ✓}),\ A_2{=}1536{=}3\cdot512\ ✓\ \text{仍 flat} ✓}$$
$$
$$
```

---

## §1 十二个结果类（**✓ 全列表**）

```
$$\begin{array}{c|c|c|c|c|c|c}
\text{例数} & k=A_1 & A_2 & |S| & \text{切片值} & J & \text{flat?}\\ \hline
88 & 256 & 1792 & 7 & \{256\} & 458752 & ✓\\
14 & 288 & 1760 & 7 & \{224,288\} & 449536 & ✗\\
12 & 224 & 1824 & 7 & \{224,288\} & 482304 & ✗\\
8 & 128 & 1920 & 7 & \{128,384\} & 638976 & ✗\\
8 & 320 & 1728 & 7 & \{192,320\} & 454656 & ✗\\
5 & 192 & 1856 & 7 & \{192,320\} & 520192 & ✗\\
4 & 352 & 1696 & 7 & \{160,352\} & 474112 & ✗\\
2 & 448 & 1600 & 7 & \{64,448\} & 618496 & ✗\\
1 & 512 & 1536 & \mathbf 3 & \{512\} & 786432 & ✓\ (\text{单陪集 ✓})\\
1 & 416 & 1632 & 7 & \{96,416\} & 556032 & ✗\\
1 & 384 & 1664 & 7 & \{128,384\} & 507904 & ✗\\
1 & 160 & 1888 & 7 & \{160,352\} & 572416 & ✗\\
\end{array}$$
$$\textbf{恒等式始终成立 ✓}:\ A_1+A_2=M/2=2048\ ✓;\ \text{star ✓};\ \text{支撑坐标集恒为 }\{1,3,5,8,10,12,14\}\ ✓\ \text{（除单陪集例 ✓）}$$
$$
$$
```

---

## §2 陪集详验（**✓ 逐坐标**）

```
$$\lambda=\mathbf 1[t\ne0]:\ \text{坐标}\to\text{值}\ \{1{:}288,3{:}288,5{:}288,8{:}224,10{:}224,12{:}224,14{:}224\}\ ✓$$
$$\qquad\text{标签化}:\ \{2{:}288,4{:}288,6{:}288\}\ \text{与}\ \{9{:}224,11{:}224,13{:}224,15{:}224\}\ ✓$$
$$\qquad\text{第二组}=\text{完整陪集 }9+W\ ✓;\ \text{第一组}=(2+W)\setminus\{0\}\ ✓（因 }2{+}2{=}0\notin\mathrm{supp}\ ✓\text{）}$$
$$\text{二次 }q{=}6:\ \text{同一陪集结构，值改为 }128/384\ ✓ \Longrightarrow \textbf{陪集几何与 }\lambda\ \text{无关，仅陪集值变化 ✓}$$
$$\textbf{由此 ✓}:\ \text{不变量应表述为}\ \boxed{q\ \text{是"两陪集常值"}} \Longrightarrow \text{原"flatness"= 两值相等}\ ✓$$
$$
$$
```

---

## §3 判读（**✓ 唐先生三档映射**）

```
$$\text{第二档成立（击穿 ✓）但\textbf{需要更精确的读法} ✓:\ \text{被击穿的是"整体恒定"这一\textbf{过强}版本;} \text{真正的律是陪集常值 ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{反例升级为精化 ✓}:\ \text{A-ALIGNTHM-1 \textbf{仍正确}（线性半码 ⟹ 两值相等 ⟹ 常值 ✓）};\ \text{新律在其上\textbf{更精细} ✓}$$
$$\qquad\Longrightarrow\ \textbf{对 P2 的意义}:\ \text{"Theorem-13 β-shape 不通用"这一结论\textbf{保留} ✓,\ 但通用形状被替换为两陪集版 ✓（更强的候选普遍律 ✓）}$$
$$\qquad\textbf{诚实边界 ✓}:\ \text{145 例（非全 }2^{15}\ \text{个 }\lambda\ ✓\text{）};\ W\ \text{是否恒为 }\mathrm{span}\{2,4\}\ \text{未证 ⚠️};\ \text{无一般 }\lambda\ \text{的定理 ⚠️}$$
$$
$$
```

---

## §4 下一步（**✓**）

```
$$\text{(甲) 是否 }W\ \text{恒为 }\mathrm{span}\{2,4\}?\ \text{（扫描全 }\lambda\ \text{或结构化抽样 ✓）};\ \text{(乙) flat }\iff\ \text{两陪集值相等的}\ \lambda\ \text{刻画（affine ⟹ flat ✓；是否充要？）}$$
$$\text{(丙) 陪集值的闭式（}224{=}7\cdot2^5,\ 288{=}9\cdot2^5;\ 128{=}2^7,\ 384{=}3\cdot2^7\ ✓\ \text{—— 与 }\lambda\ \text{的真值表结构的关系 ✓）};\ \text{(丁) ENP1CC puncturing};\ \text{(戊) 119（你说过暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：145 例 λ 扫描、flat ⟺ $|S|\mid A_2$、两陪集常值精化律（含逐坐标详验）、affine λ ⟹ flat
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-VASILEV-1、A-P2COLLISION-1、内蕴 $\nu$、$\mathfrak B_1$ 覆盖门


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 陪集常值精化律 命中文件数=1    :: ./LAMBDA-SCAN-2026-09-27-coset-constant-refined-law.md 
技术词 λ 扫描        命中文件数=4    :: ./LAMBDA-SCAN-2026-09-27-coset-constant-refined-law.md ./p49-g274c2-compression.md ./p49-g274iia2-matrix-check.md
```
- **本档新增**：145 例 $\lambda$ 扫描、flat $\iff$ $|S|\mid A_2$、两陪集常值精化律（含逐坐标详验）、affine $\lambda\Longrightarrow$ flat（见上方命中数；0 命中者为自造语／内部标签 ✓）
