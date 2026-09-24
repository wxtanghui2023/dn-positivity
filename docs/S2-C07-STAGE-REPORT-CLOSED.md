已查地图：命中（`S2-C07-P2-certificate-VERIFIED-t20-9-equals-4`）⟹ `C07` 收口阶段报告，不开新案
D0: 本档对象 = **`C07` 阶段报告（CLOSED）**：两格结论表 ＋ `(20,9)` 完整证书链 ＋ **两项研究资产（证明链压缩／计数张力非充分条件）** ＋ `(乙)` 独立后续节点登记 ＋ `Zone-A` 终态与指针
D1: 1（首个以"证明链压缩＋本行机器证书"双路径收口的 `Zone-A` 条目）
[REPORT]

# **`C07` — Binary Linear Covering Codes：阶段 `CLOSED`**

## §1 两格结论

```
$$\begin{array}{c|c|c|c|c}
\text{Cell}&\text{结论}&P1\ (\text{下界})&P2\ (\text{上界})&\text{最终证据}\\
\hline
t_2[19,9]&\boxed{4}&\ell_2(10,3)\ge21\ (\text{Struik})\ ＋\ \text{球覆盖下界}&t_2[19,9]\le4\ (\text{历史})&\textbf{档级／外部引用}\\
t_2[20,9]&\boxed{4}&1{+}20{+}\binom{20}{2}{+}\binom{20}{3}=1351<2048\Rightarrow R\ge4&\text{显式 }11\times20\ \text{parity-check 矩阵},\ R{=}4&\boxed{\textbf{机器级／自有证书}}\\
\end{array}$$ ✓✓✓
$$\textbf{共同点}:\ \text{两格都是 }P1\ \text{与 }P2\ \textbf{正面碰撞};\ \text{没有一格靠"猜"或"未定型 bound"}$$ ✓✓
```

## §2 `(20,9)` 完整证书链（逐条）

```
$$\textbf{① 参数}:\ \operatorname{rank}_{\mathbb F_2}(H)=11 \Longrightarrow \text{码参数 }[20,20-11]=[20,9]$$ ✓
$$\textbf{② 列}:\ 484,1200,1437,325,491,1137,1,1124,1017,348,693,72,1433,1318,1591,1491,1301,44,1981,208\ (\text{全非零},\ \text{无重复})$$ ✓
$$\textbf{③ 覆盖}:\ \#\{s\in\mathbb F_2^{11}:\ \operatorname{wt}_H(s)\le4\}=\boxed{2048}\ (\text{即全部 syndrome})\ \Longrightarrow R\le4$$ ✓✓
$$\textbf{④ 紧性}:\ \max_s\operatorname{wt}_H(s)=\boxed{4}\ (\text{且重量分布 }\{0{:}1,1{:}20,2{:}190,3{:}949,4{:}888\})$$ ✓
$$\textbf{⑤ 下界}:\ 1+20+\binom{20}{2}+\binom{20}{3}=1+20+190+1140=\boxed{1351}<2^{11}=2048 \Longrightarrow \boxed{R\le3\ \text{不可能}}$$ ✓✓✓
$$\Longrightarrow\ \boxed{t_2[20,9]=4}$$ ✓✓✓
$$\textbf{独立复核}:\ \text{方法 A（组合枚举 }6196\text{）与方法 B（按重量 }BFS\text{）}\ \textbf{分布完全一致};\ \text{与先生独立核验逐项一致}$$ ✓✓
$$\text{归档}:\ \texttt{data/q2\_20\_9\_certificate.txt};\ \texttt{scripts/q2\_verify\_20\_9\_covering\_certificate.py};\ \texttt{out/out\_q2\_verify.txt}$$ ✓
```

## §3 两项研究资产

```
$$\boxed{\text{资产 A}:\ \textbf{证明链压缩}}\ ——\ \text{表格态 }t_2[20,9]=4\text{-}5 \Longrightarrow \text{经 parity-check 转换为\textbf{唯一构造节点} }\ell_2(11,4)\le20 \Longrightarrow \textbf{显式 }11\times20\ \text{构造解决},\ \textbf{完全不依赖历史表格}$$ ✓✓✓
$$\qquad \text{价值}:\ \text{把"补一个表格格"变成"造一个对象"};\ \text{该转换对任意 }t[n,k]\ \text{型 frontier cell 可复用}$$ ✓✓
$$\boxed{\text{资产 B}:\ \textbf{计数张力非充分条件}}\ ——\ \text{不可把"计数紧"当"不可行"，也不可把"计数松"当"可行"}$$ ✓✓✓
$$\qquad (19,9):\ 1160\ \text{vs}\ 1024\ (\text{紧},\ slack=136)\ \to\ \textbf{不可行}\ (\text{由外部下界封死});\qquad (20,9):\ 6196\ \text{vs}\ 2048\ (\text{松})\ \to\ \textbf{可行}\ (\text{构造存在})$$ ✓✓
$$\qquad \Longrightarrow\ \text{验证 }AMEND\text{-}19:\ \textbf{先判 }P1/P2\ \text{哪侧有真攻击点},\ \text{再决定是否计算};\ \text{本次 P2 一击即中}$$ ✓✓
```

## §4 `(乙)` 登记为**独立后续节点**（不是 `OPEN`）

```
$$\boxed{\ell_2(11,4)\le20\quad\textbf{CONSTRUCTED}} —— \textbf{不是 }OPEN,\ \textbf{也不是 }=20$$ ✓✓
$$\text{若日后开线}:\ \text{新 }P1 = \boxed{\ell_2(11,4)\ge20}\ (\text{即排除长度 }n\le19\ \text{的 }(11,4)\ \text{covering code})$$ ✓✓
$$\textbf{⚠️ 前置纪律}:\ \text{该节点与 }t\ \text{表参数的对换关系\textbf{必须逐步重推}},\ \textbf{不得}直接写成"排除 }t_2[19,8]=4\text{"后沿用现有证明$$ ✓✓✓
$$\text{原因}:\ \ell\ \text{与 }t\ \text{的对换涉及长度／协维的\textbf{同时变动}，且零列约定影响成立性};\ \text{每次对换都要逐项核}$$ ✓✓
$$\textbf{本节点不阻塞 }C07\ \text{的关闭};\ \text{现在追它会把已完成的 }C07\ \text{拖成新循环} \Longrightarrow \textbf{暂不开}$$ ✓
```

## §5 声明纪律（本轮确立）

```
$$\textbf{可写}:\ \text{"在\textbf{可及表}（GS-1985／CKMS-1985／1997 综述 Table B）中该格原记 }4\text{-}5,\ \text{本证书给出 }4\text{"}$$ ✓
$$\textbf{禁写}:\ \text{"文献从未有人做到"} —— \text{《Covering Codes》Table 7.3 与 BPW 1989 未取得};\ \text{该表的 }(11,4)\ \text{格状态\textbf{未知}}$$ ✗✗
$$\textbf{证据分级（本行标准）}:\ \boxed{\text{档级}}\ (\text{外部引用，未逐字核})\ <\ \boxed{\text{机器级}}\ (\text{自有可复核证书})$$ ✓✓
```

## §6 `Zone-A` 终态与指针

```
$$\begin{array}{c|c}
\text{ID}&\text{终态}\\
\hline
D03&G0/A?\ (\text{窗口未闭合})\\
D04&\textbf{DROP}\ (\text{全函数已知})\\
D06&\textbf{DROP}\ (\text{库覆盖＋替代障碍})\\
D07&\textbf{DROP}\ (\text{自然 }H\ \text{已收割/渐近/Erdős 注册})\\
Mt06&\textbf{DROP}\ (\text{母分类顺手做完})\\
Mt07&\text{保留} —— \text{需\textbf{非著名格}}\\
Mt08&\textbf{DROP}\ (\text{最小反例 }=6\ \text{已知})\\
C06&\texttt{G1}^*\ (\text{仅非线性读})\\
C07&\boxed{\textbf{CLOSED}}\ (\text{两格皆 }4)\\
C09&\textbf{DROP}\ (\text{observable 无独立性})\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \text{Zone-A}\ 10\ \text{条}:\ \textbf{6 DROP}\ +\ \textbf{1 CLOSED(本档)}\ +\ \textbf{2 保留(Mt07/C06)}\ +\ \textbf{1 G0(D03)}$$ ✓✓
$$\boxed{\text{指针}}:\ \text{C07 关闭};\ \text{余 }Mt07\ (\text{非著名格})\ \text{与 }C06_{\rm nonlinear}\ \text{挂起};\ \boxed{\text{下一步}=\text{Zone-B}}$$ ✓✓
【⛔ 纪律】 `U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；`(乙)` 暂不开 ✓
【边界】 `(19,9)` 的 `\ell_2(10,3)\ge21` 为**档级**；`(20,9)` 全链为**本行机器级** ✓

## §附 【技术词回查】（补录）
```
技术词 stage report     命中文件数=0    :: 
技术词 asset            命中文件数=54   :: ./GT-0-and-GT-STRATEGY-audit.md ./C121-conceptual-correction-scale-law-asset-beta-channel-priority.md ./P5-Y3-SOURCE-CARD-and-AMEND9-gate-REJECT.md 
```
