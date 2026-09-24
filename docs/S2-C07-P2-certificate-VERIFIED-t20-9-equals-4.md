已查地图：命中（`S2-C07-ell11-4-sharpened-to-20-or-21-and-P2-card`）⟹ `P2` 证书独立核验，不开新案
D0: 本档对象 = **[20,9] 覆盖半径 4 的构造证书（先生产出）之\textbf{独立核验}**（双算法 ＋ GF(2) 秩 ＋ 计数下界）＋ **记账修正（`t` 闭、`\ell` 只得上界）** ＋ **`C07` 两格收口**
D1: 1（首次由本行机器核验外部构造证书；两格同时收口）
[RESEARCH]

# **`P2` 证书已独立核验：`t_2[20,9]=4`**

## §1 证书内容（先生产出，已归档）

```
$$\text{列（整数 }0..2047\text{，即 11-bit 列向量）}:\ 484,1200,1437,325,491,1137,1,1124,1017,348,693,72,1433,1318,1591,1491,1301,44,1981,208$$ ✓
$$\text{归档}:\ \texttt{data/q2\_20\_9\_certificate.txt};\quad \text{核验脚本}:\ \texttt{scripts/q2\_verify\_20\_9\_covering\_certificate.py};\quad \text{输出}:\ \texttt{out/out\_q2\_verify.txt}$$ ✓
```

## §2 独立核验结果（**全 PASS**）

```
$$\textbf{⓪ 输入}:\ 20\ \text{列全非零、全 }<2^{11};\ \textbf{无重复列}$$ ✓
$$\textbf{① GF(2) 秩}:\ \operatorname{rank}_{\mathbb F_2}(H)=\boxed{11} \Longrightarrow \text{码参数 }[20,20-11]=[20,9]$$ ✓✓✓
$$\textbf{② 方法 A（组合枚举 }6196\ \text{个子集）}:\ \text{可达 syndrome }=\boxed{2048/2048}$$ ✓✓
$$\textbf{③ 方法 B（按重量 BFS，\textbf{独立算法}）}:\ \text{可达 }=\boxed{2048/2048}$$ ✓✓
$$\textbf{④ 双法一致性}:\ \textbf{分布完全相同} \Longrightarrow \text{实现层互校通过}$$ ✓✓
$$\textbf{⑤ 重量分布}:\ \boxed{\{0{:}1,\ 1{:}20,\ 2{:}190,\ 3{:}949,\ 4{:}888\}}\ (\text{合计 }2048) —— \textbf{与先生独立核验逐项一致}$$ ✓✓✓
$$\textbf{⑥ 下界}:\ \#\{\text{子集}\le3\}=1351<\ 2048 \Longrightarrow \boxed{R\ge4};\quad \text{实际可达 }\le3\text{-sums}=1160\ (\text{更紧})$$ ✓✓
$$\textbf{⑦ 上界}:\ \text{覆盖成立且最大最小重量}=4 \Longrightarrow \boxed{R\le4} \Longrightarrow \boxed{R(C)=4}$$ ✓✓✓
$$\Longrightarrow\ \boxed{t_2[20,9]=4}\ \textbf{（P1 计数下界与 P2 显式构造正面碰撞）}$$ ✓✓✓
```

## §3 记账修正（照先生）

```
$$\boxed{t_2[20,9]=4\quad\textbf{CLOSED}}\ (\text{双证：}1351<2048\ \text{下界}\ +\ \text{显式 }11\times20\ \text{矩阵})$$ ✓✓
$$\boxed{\ell_2(11,4)\le20\quad\textbf{已构造}}\ (\textbf{不得写成 }\ell_2(11,4)=20)$$ ✓✓
$$\qquad \text{理由}:\ \text{更短（}n\le19\text{）的协维 }11\text{、半径 }4\text{ 码可能存在};\ \text{它只会\textbf{更强地}推出 }t_2[20,9]=4,\ \text{与本构造不矛盾}$$
$$\ell_2(11,4)\ \text{是否恰为 }20 \Longrightarrow \textbf{仍需独立 }n\le19\ \text{下界}\ (\text{等价于排除 }t_2[19,8]=4\ \text{等})$$ ✓
```

## §4 `C07` 两格同时收口

```
$$\begin{array}{c|c|c|l}
\text{cell}&\text{结论}&\text{依据}&\text{证据等级}\\
\hline
(19,9)&\boxed{t_2=4}&\ell_2(10,3)\ge21\ (\text{Struik})\ \text{＋球覆盖下界 ＋ 历史上界}&\textbf{档级（外部引用）}\\
(20,9)&\boxed{t_2=4}&\textbf{本行双算法机器核验的 }11\times20\ \text{构造证书}&\textbf{机器级（自有）}\\
\end{array}$$ ✓✓✓
$$\Longrightarrow\ \boxed{C07\ \text{两个 frontier cell 均已收口}};\quad \text{不再需要 BPW 1989 原表}$$ ✓✓
$$\textbf{方法学对照（有价值）}:\ (19,9)\ \text{计数\textbf{紧}}（1160\ \text{vs}\ 1024）\to\ \text{不可行};\quad (20,9)\ \text{计数\textbf{松}}（6196\ \text{vs}\ 2048）\to\ \textbf{可构造}$$ ✓✓
```

## §5 新资产登记（供台账）

```
$$\boxed{A\text{-P2-1}}:\ \text{显式 }11\times20\ \text{覆盖矩阵}（20\ \text{列},\ \operatorname{rank}11,\ (\le4)\text{-覆盖满},\ R{=}4）—— \textbf{可复用、可机器复核}$$ ✓✓
$$\boxed{A\text{-P2-2}}:\ t_2[20,9]=4\ \textbf{的现代独立证书};\ \text{可达表（GS-1985／CKMS-1985／1997 综述 Table B）原记 }4\text{-}5$$ ⚠️
$$\qquad \textbf{声明纪律}:\ \text{可写"在可及表中原为 }4\text{-}5,\ \text{本证书给出 }4"——\textbf{不得写"文献从未有人做到"}（书内 Table 7.3 未取得）$$ ✓✓
【⛔ 纪律】 本轮计算\textbf{仅为核验}（`D` 层），非搜索；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §1 列向量来自先生；§2 全部结论本行实算；§3 记账修正已采纳 ✓

## §附 【技术词回查】（补录）
```
技术词 certificate      命中文件数=137  :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./C319-directed-recheck-C272-pending-box-set-semantics-GAP-CONFIRMED.md ./C3896-exact-symbolic-T3PASS-certificate.md 
技术词 covering radius  命中文件数=9    :: ./TARGET-L9-source-fetch-report.md ./S2-HANDOFF-zone-members-and-count-fix.md ./S2-BATCH-2-record.md 
```
