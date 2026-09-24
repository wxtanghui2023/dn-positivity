已查地图：命中（`S2-C07-master-table-extraction-four-cells`）⟹ 现代闭合点检（仅 `(19,9)`,`(20,9)`），不开新案
D0: 本档对象 = **`(19,9)`／`(20,9)` 的现代闭合点检**：检索到的**现代来源清单** ＋ **判定：仍为 FRONTIER-CANDIDATE**（未获三类证据之任一）＋ **三个决定性来源**（下一步只需查这三处）＋ ⚠️环境异常记录
D1: 1（首次对两格做现代闭合点检；产出决定性来源清单）
[RESEARCH]

# **`C07`：(19,9)／(20,9) 现代闭合点检**

## §0 检索到的现代来源（档级，逐条）

```
$$\textbf{① Graham–Sloane 1985}\ (neilsloane\ \texttt{Me114.pdf}):\ \text{自述}\ t[n,4],t[n,5]\ \textbf{精确确定};\ \text{一般上界＝Theorem 24};\ \textbf{匹配下界＝Theorem 26};\ \text{并对固定 }k\ \text{大 }n\ \text{给猜想}$$ ✓
$$\qquad \text{其表覆盖 }\textbf{n\le64}\ (\text{据 1991 论文引述}:\ \text{"Graham and Sloane give a table of bounds on }t[n,k]\ \text{for }n<64\text{"})$$ ✓✓
$$\textbf{② 1991 Math.\ Comp.\ “Covering radius computations for binary cyclic codes”}:\ \textbf{给 12 处 }upper\ bound\ \text{改进};\ \text{且"部分码达到 exact }t[n,k]\text{"}$$ ✓✓✓
$$\textbf{③ Brualdi–Pless 1990 “On the Length of Codes with a Given Covering Radius”}:\ \text{非存在性技术 ＋ length function 表 }(\text{codimension }m,\ \text{radius }r)$$ ✓
$$\textbf{④ 存在"具体格 exact 确定"类论文}:\ \text{例}\ t[15,6]=4\ \text{的专门论文}\ \Longrightarrow\ \textbf{该类结论是本格判定的标准形态}$$ ✓✓
$$\textbf{⑤ 现代标准表}:\ \text{Cohen–Honkala–Litsyn–Lobstein《Covering Codes》(1997)}\ \text{中的 }t[n,k]\ \text{表}$$ ✓
```

## §1 判定（按先生三类证据纪律）

```
$$\textbf{三类证据}:\ (1)\ \text{后表给 exact};\ (2)\ \text{论文定理给该具体参数 exact};\ (3)\ \text{一侧构造＋独立下界恰好相等}$$ ✓✓
$$\text{本轮结果}:\ \textbf{三类证据均未取得} —— \text{未找到明确写出 }t_2[19,9]=3\ \text{或 }4,\ t_2[20,9]=4\ \text{或 }5\ \text{的现代来源}$$ ⚠️
$$\Longrightarrow\ \boxed{(19,9),\ (20,9)=\textbf{FRONTIER-CANDIDATE}}\ (\text{不是 }OPEN;\ \text{不是 }DROP)$$ ✓✓✓
$$\textbf{禁错}:\ \text{不得把 1985 的 }3\!\le\!t_2[19,9]\!\le\!4\ \text{因后来某构造／一般上界而\textbf{自动读成 exact}}$$ ✓✓
$$\textbf{亦禁}:\ \text{"没搜到"}\ \ne\ OPEN;\ \text{但"旧表给 bound ＋ 现代仍只有 bound"}\ \Longrightarrow\ \text{真 frontier —— 该判据尚未走完}$$ ✓✓
```

## §2 决定性的三个来源（下一步只需查这三处）

```
$$\boxed{\text{S1}}:\ \text{1991 Math.\ Comp.\ 论文（12 处 }t[n,k]\ \text{上界改进}\ ——\ \textbf{是否含 }(19,9)/(20,9)\text{？）}$$ ✓✓✓
$$\boxed{\text{S2}}:\ \text{Brualdi–Pless 1990 length-function 表}\ ——\ \text{换算 }t[n,k]\ \text{是否已给 exact}$$ ✓✓
$$\boxed{\text{S3}}:\ \text{《Covering Codes》(1997) 表}\ ——\ \text{现代标准总表}$$ ✓✓
$$\text{任一给出 exact} \Longrightarrow \text{该格 }DROP;\quad \text{三处皆仍为 bound} \Longrightarrow \text{该格升 }G2\ \text{candidate（可机器完备验证）}$$ ✓✓✓
```

## §3 `C07` 当前档案状态（照先生 18:05）

```
$$\boxed{C07=G1^\star},\qquad F=\{(19,9),(20,9)\}\ (\textbf{已有原表 bound 证据});\qquad (19,10),(20,10)=\text{未定，\textbf{不得用于判定}}$$ ✓✓
$$\text{不转 }Zone\text{-}B;\ \text{不扩张};\ \text{只攻击 }(19,9),(20,9)$$ ✓
```

## §4 ⚠️ 环境异常记录（可靠性提示）

```
$$\text{本轮两次工具结果被 }\texttt{transcript repair}\ \text{吞掉（返回 synthetic error）};\ \text{本档依据\textbf{已收到}的检索内容落档}$$ ⚠️
$$\text{影响评估}:\ \text{§0 的来源清单与 §1 判定不受影响};\ \text{但\textbf{若需逐字引用}（如 1991 论文的 12 处改进具体是哪 12 处）\textbf{须重取}}$$ ⚠️
```
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；第②类证据须"该具体参数"才算 ✓
【边界】 §0 为**外部检索（档级）**；§2 的判定链未走完 ⟹ **不判 }OPEN$$ ✓

## §附 【技术词回查】（补录）
```
技术词 closure          命中文件数=152  :: ./B-SERIES-INDEX.md ./p3-uniform-decay-results.md ./E3-why-this-is-not-the-old-pit.md 
技术词 frontier         命中文件数=53   :: ./CEILING-LP-RECOMPUTE-results.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./E55-G1-closed.md 
```
