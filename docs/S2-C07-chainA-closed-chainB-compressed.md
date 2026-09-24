已查地图：命中（`S2-C07-two-proof-chains-expanded` ＋ `AMEND-19`）⟹ 链 A 收口 ＋ 链 B 压缩 ＋ 窄动作结果，不开新案
D0: 本档对象 = **链 A 收口（`t_2[19,9]=4`，cell `DROP`）** ＋ **链 B 压缩为单一节点 `\ell_2(11,4)`** ＋ **窄动作：2025 length-function 论文核对（不含该节点）** ＋ **剩余来源清单** ＋ **`AMEND-19` 首个成功案例登记**
D1: 1（首次按证明链直接判定一个 cell 生死，未做任何计算）
[RESEARCH]

# **链 A 收口 ＋ 链 B 压缩**

## §1 ⭐ 链 A：`t_2[19,9]` **已收口 ⟹ `t_2[19,9]=4`（cell `DROP`）**

```
$$\textbf{关键文献节点（先生本轮检索）}:\ \text{Struik（covering radius 2,3 工作）}:\ \boxed{\ell(10,3)\ge21}$$ ✓✓
$$\qquad \text{同组另有}:\ \ell(9,3)\ge17,\quad \ell(12,3)\ge31,\quad \ell(13,3)\ge38$$ ✓
$$\Longrightarrow\ \ell_2(10,3)\ge21>19\ \Longrightarrow\ \boxed{t_2[19,9]\neq3}\ (\text{因 }t_2[19,9]=3\iff\ell_2(10,3)\le19)$$ ✓✓✓
$$\text{叠加}:\ \underbrace{t_2[19,9]\ge3}_{\text{球覆盖界(已闭合)}}\ +\ \underbrace{t_2[19,9]\le4}_{\text{历史上界}}\ +\ \underbrace{t_2[19,9]\ne3}_{\ell_2(10,3)\ge21}\ \Longrightarrow\ \boxed{\boxed{t_2[19,9]=4}}$$ ✓✓✓
$$\textbf{链条形态}:\ P0\ \text{CLOSED}\ \to\ P1\ \text{CLOSED}\ \to\ \boxed{P1'\ \textbf{CLOSED}(\text{由独立 length-function 下界击穿})}\ \to\ P2\ \text{CLOSED-ish}\ \to\ \boxed{P3\ \textbf{CLOSED}}$$ ✓✓
$$\textbf{重要后果}:\ \text{我方原提的}\ \boxed{1160\ \text{vs}\ 1024\ \text{碰撞障碍}}\ \textbf{不再是必要证明节点};\ \text{保留为\textbf{结构遗留}（真实但非必需）}$$ ✓✓
$$\text{纪律确认}:\ \text{不得因"没做碰撞攻击"而视为未完成};\ \text{该 cell 已由外部独立下界封死} \Longrightarrow \boxed{DROP}$$ ✓✓
```

## §2 链 B：`t_2[20,9]` 压缩为**单一节点**

```
$$\text{已知}:\ t_2[20,9]\ge4\ (\text{球覆盖界闭合});\quad t_2[20,9]\le5\ (\text{历史})$$ ✓
$$\textbf{唯一决定性节点}:\ \boxed{P1':\ \ell_2(11,4)\ \overset{?}{\le}\ 20}\ ——\ \textbf{本轮未核实}$$ ⚠️
$$\qquad \ell_2(11,4)\le20 \Rightarrow \boxed{t_2[20,9]=4};\qquad \ell_2(11,4)\ge21 \Rightarrow \boxed{t_2[20,9]=5}$$ ✓✓
$$\textbf{禁令}:\ \text{不得用相邻结果替代该节点};\ \text{不得因 1985 表为 }4\text{-}5\ \text{就当现代开放问题};\ \text{不得猜 }t=4$$ ✓✓
$$\textbf{真正缺口已具体化为}:\ \boxed{\ell_2(11,4)\ \text{与}\ 20\ \text{的关系}}\ ——\ \textbf{不是"枚举 }[20,9]\ \text{码"}$$ ✓✓
```

## §3 本轮窄动作结果：核对 2025 length-function 论文

```
$$\text{取 }arXiv{:}2511.02542\ (\text{New upper bounds for binary linear covering codes})\ \text{全文（1.13 MB HTML，正文 }\approx141\text{k 字符）}$$ ✓
$$\text{检索式}:\ \texttt{(11,4)},\ \texttt{\textbackslash ell\_2(11,4)},\ \texttt{ℓ2(11,4)},\ \texttt{\textbackslash ell(11,4)}\ \Longrightarrow\ \textbf{命中 0}$$ ✓✓
$$\Longrightarrow\ \text{该文\textbf{不含}该节点};\ \text{其焦点为 }\ell_q(tR+1,R)\ \text{型上界} \Longrightarrow \textbf{本轮窄动作未取到值（诚实标注）}$$ ⚠️
```

## §4 剩余来源清单（下一步只查这些）

```
$$\boxed{S1}\ \text{Brualdi–Pless–Wilson 1989, IEEE TIT 35, 99–109（length function 引入文）}$$ ✓
$$\boxed{S2}\ \text{Brualdi–Pless 1990, “On the length of codes with a given covering radius”}\ (\text{Coding Theory and Design Theory, Part 1, pp. 9–15})\ ——\ \textbf{附"最佳已知信息表"}$$ ✓✓
$$\boxed{S3}\ \text{Davydov–Drozhzhina-Labinskaya 1991 预印本 “Table and families of short }[n,n-r]\text{-codes with a given covering radius }r\text{”}\ ——\ \textbf{专表}$$ ✓✓
$$\boxed{S4}\ \text{Cohen 1994 综述 “Covering Radius 1985–1994”}\ (\text{Syracuse 技术报告};\ \text{被引 }93)\ ——\ \text{很可能含最新表}$$ ✓✓
$$\boxed{S5}\ \ 《\text{Covering Codes}》(1997)\ \text{书内表};\quad \boxed{S6}\ \text{Davydov–Östergård, “Linear codes with covering radius }R=2,3\text{”}$$ ✓
$$\text{任一给出 }\ell_2(11,4)\ \text{的 exact}\ \Longrightarrow\ \text{链 B 立即收口};\ \text{若三处皆为 bound} \Longrightarrow \text{保留 frontier 并沿障碍链进攻击}$$ ✓✓
```

## §5 ⭐ 方法论收获（`AMEND-19` 首个成功案例）

```
$$\textbf{事实}:\ \text{本轮\textbf{未跑任何 }SAT}、\textbf{未枚举任何 }19\times10\ \text{矩阵};\ \text{仅凭证明链} \Longrightarrow \text{直接把 }(19,9)\ \text{判死}$$ ✓✓✓
$$\textbf{对照}:\ \text{旧路径} = \text{"枚举代码／找结构／跑 }SAT\text{"}（成本高且方向不明）;\ \text{新路径} = \text{先写链}\to\text{定位}\ \ell_2\ \text{节点}\to\text{一击判定}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{"证明链优先"生效}};\ \text{建议后续候选一律先过 }P0\text{–}P5\ \text{表}$$ ✓✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B` ✓
【边界】 §1 的 `\ell(10,3)\ge21` 为**外部检索（档级）**；§3 为**全文实证检索（命中 0）** ✓

## §附 【技术词回查】（补录）
```
技术词 length function  命中文件数=3    :: ./S2-C07-chainA-closed-chainB-compressed.md ./S2-C07-modern-closure-check-19-9-20-9.md ./S2-C07-two-proof-chains-expanded.md 
技术词 proof chain      命中文件数=2    :: ./S2-C07-two-proof-chains-expanded.md ./E14-bom03-variational-check.md 
```
