已查地图：命中（`S2-C07-frontier-compression-and-four-cell-check`）⟹ 原表提取与四格判定，不开新案
D0: 本档对象 = **取得原始表（`CKMS-1985` 综述，含 `TABLE II: values and bounds on t[n,k], n ≤ 32, k ≤ 25`）** ＋ **四格判定（`(19,9)`、`(20,9)` 已读；`(19,10)/(20,10)` 未能可靠提取）** ＋ ⚠️**文件名纠错**
D1: 1（首次取得总表原表并读出两格；产出"旧表为 bound"判定）
[RESEARCH]

# **`C07`：原表提取与四格判定**

## §0 ⚠️ 文件名纠错（我方命名错误）

```
$$\textbf{已纠正}:\ \text{该 PDF}\ \textbf{不是 Graham–Sloane};\ \text{实为}\ \boxed{\text{Cohen–Karpovsky–Mattson–Schatz 1985}},\ \text{“Covering Radius—Survey and Recent Results”},\ IEEE\ Trans.\ IT\ 31(3)$$ ✓✓
$$\qquad \text{文件已改名}:\ \texttt{sources/CKMS-1985-covering-radius-survey.pdf}\ (1.9\ MB,\ 16\ 页)$$ ✓
$$\textbf{表定位}:\ \text{page 13}\ \texttt{TABLE II: VALUES AND BOUNDS ON t[n,k] FOR n\le32 AND k\le25, PART 1};\ \text{page 14 = PART 2}$$ ✓
$$\textbf{结构（坐标法确认）}:\ \boxed{\text{行}=k,\ \text{列}=n};\ \text{表头 }x\ \text{位置}: n=3\,(x\!\approx\!176)\dots n=19\,(x\!\approx\!431),\ n=20\,(x\!\approx\!452),\ n=21\,(x\!\approx\!473)$$ ✓✓
$$\text{校验}:\ k=19,n=19\to0;\ k=20,n=20\to0;\ k=21,n=21\to0\ (\text{全空间, 自洽}\ \checkmark)$$ ✓
```

## §1 四格读数（原表）

```
$$\begin{array}{c|c|c}
(n,k)&\text{原表 (CKMS 1985)}&\text{性质}\\
\hline
(19,9)&3\text{-}4&\boxed{\text{bound}\ (L{=}3<U{=}4)}\\
(20,9)&4\text{-}5&\boxed{\text{bound}\ (L{=}4<U{=}5)}\\
(19,10)&\text{未能可靠提取}&\text{（}k{=}10\ \text{行在该扫描件 OCR 中缺失）}\\
(20,10)&\text{未能可靠提取}&\text{同上}\\
\end{array}$$ ✓✓
$$\textbf{旁证}:\ k=9\ \text{行其余格}:\ n{=}17\to3\ (\text{exact}),\ n{=}18\to3\text{-}4,\ n{=}21\to4\text{-}5;\quad k{=}8:\ n{=}18\to4\ (\text{exact}),\ n{=}19\to4\text{-}5$$ ✓
$$\textbf{自洽核对}:\ t[19,9]\ge3\ \text{与球覆盖下界一致（}1{+}19{+}171{=}191{<}2^{10}{=}1024;\ +\!\binom{19}{3}{=}1160{\ge}1024\Rightarrow\rho\ge3\text{）}$$ ✓✓
```

## §2 判定（按先生纪律，**只走有原表证据的路**）

```
$$\textbf{纪律}:\ \text{"现代文献没找到"}\ \textbf{不算 OPEN};\ \text{旧表给 bound 且现代仍只有 bound} \Longrightarrow \textbf{真 frontier}$$ ✓✓
$$\text{现状}:\ (19,9)\ \text{与}\ (20,9)\ \textbf{在 1985 总表中即为 bound};\ \text{而 2003 Baicheva–Vavrek 的 "small lengths" 只做到 }k\le8 \Longrightarrow \textbf{未闭合 }k{=}9$$ ✓
$$\Longrightarrow\ \boxed{(19,9),(20,9)\ \text{＝ frontier 候选（待现代闭合点检）}};\quad \textbf{本轮不判 }OPEN,\ \text{亦不判 }DROP$$ ✓✓
$$\textbf{待补}:\ (i)\ \text{现代闭合点检（post-1985，目标：}CKMS\ \text{后续表／《Covering Codes》1997 表／}Kéri\ \text{表／近年论文）；}(ii)\ k{=}10\ \text{行读数（需更清晰表或书内表）}$$ ✓
```

## §3 意义（对 `C07` 状态）

```
$$\text{C07 仍为 }\boxed{G1^\star};\ \text{但已获得}\ \textbf{原表级证据}:\ \text{两格在总表中为 bound} \Longrightarrow \text{至少两格\textbf{不是"已 exact"}}$$ ✓✓
$$\textbf{若现代闭合点检为空} \Longrightarrow \text{该格升 }\boxed{G2\ \text{candidate}}\ (\text{单一整数、可机器完备验证});\quad \textbf{若已被闭合} \Longrightarrow DROP$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；**未判 }OPEN$$ ✓
【边界】 §1 为**原表实读**（坐标法，0 处人工猜测）；`k=10` 行为**扫描件缺读**（诚实标注）✓

## §附 【技术词回查】（补录）
```
技术词 master table     命中文件数=2    :: ./D2-arith-CLOSED.md ./E18-NOGO-ALIGNMENT-2.md 
技术词 bound            命中文件数=391  :: ./EXT-4CT-2026-method-transfer.md ./B-SERIES-INDEX.md ./V2-10-section-4-1-3-2-a2-role-and-branch-lock.md 
```
