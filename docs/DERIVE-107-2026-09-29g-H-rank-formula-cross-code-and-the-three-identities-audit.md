# DERIVE-107-g（2026-09-29）—— **秩公式 $\text{rank}A{=}M{-}b(H)$ 跨四码精确成立；你 §3/§4 两条恒等式需修正；碰撞量 $S$ 之实测**

> **性质**：**纯推导 ＋ 全量实测 ＋ 账目审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 14:0x ✓
> **唐先生令**：把 $\delta(z)$ 完全代数化并审计；不先塞 $E$ ✓

**已查地图**：`DERIVE-107-f`（$H$ 与秩公式）／`DERIVE-107-e`（$G$ 谱）✓

D0: 本档对象 ＝ **档案已有**（$H$／incidence／signless Laplacian——皆经典 ✓）
D1: 0（产出＝**跨码验证 ＋ 两条恒等式之纠正 ＋ 一处新稳定比 ＋ $S$ 之实测** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 你的秩公式\ \textbf{跨四码精确成立}}:\ \text{rank}(A)=M-b(H)\ \text{（}90{=}120{-}30,\ 147{=}149{-}2,\ 142{=}147{-}5,\ 146{=}152{-}6\text{）}}$$
$$\boxed{\text{② ✗ 你 §4 之}\ \Sigma_z\tbinom{\mu(z)}2=2P_2\ \textbf{为假}:\ \text{实测 }\mathbf{398}=\mathbf{2}(N_1{+}N_2)\ (\ne2P_2{=}298)}$$
$$\boxed{\text{③ ✗ 你 §3 之}\ \Sigma_{z\in Q}r(z)=|Y_2|\ \textbf{为假}:\ \text{实测 }\mathbf{112}=|Y_2|-24=|Y_2|-\#\{y:z(y)\in C\}}$$
$$\boxed{\text{④ ✓ }S=\Sigma_c\tbinom{d_H(c)}2=\mathbf{273}\ (\text{C-S 下界 }173\ ✓);\ \text{且 }S/E\ \textbf{不恒定}\ (0.92\ \text{v.s.}\ 1.6{-}1.7)}$$
$$\boxed{\text{⑤ ★ 一处新稳定比}:\ |Y_2|/E\approx\mathbf{0.46}\ (\text{四码 }0.459/0.475/0.474/0.438)}$$

## §1 ① 秩公式之跨码验证（**✓✓ 四码全中**）

| 码 | $M$ | $E$ | $|Y_2|$ | $Q$ | 分量数（二分） | $\text{rank}A$ | $M-b(H)$ |
|---|---|---|---|---|---|---|---|
| 120-code | $120$ | $296$ | $136$ | $158$ | $38$（$30$） | $\mathbf{90}$ | $\mathbf{90}$ ✓ |
| greedy0 | $149$ | $615$ | $292$ | $381$ | $4$（$2$） | $\mathbf{147}$ | $\mathbf{147}$ ✓ |
| greedy1 | $147$ | $593$ | $281$ | $362$ | $7$（$5$） | $\mathbf{142}$ | $\mathbf{142}$ ✓ |
| greedy2 | $152$ | $648$ | $284$ | $376$ | $8$（$6$） | $\mathbf{146}$ | $\mathbf{146}$ ✓ |

$$\therefore\ \boxed{\text{rank}(A)=|V|-b(H)\ \text{对四码皆精确}\Longrightarrow\ \textbf{经典定理之确认}✓✓}$$
$$\text{且 }120\text{-code 之 }H\ \textbf{远比其他碎裂}（38\ \text{分量 vs }4{-}8）$$

## §2 ② 你 §4 恒等式之纠正（**✗**）

$$\text{你称}:\ \Sigma_z\tbinom{\mu(z)}2=2|\mathcal P_2|;\qquad \textbf{实测}:\ \Sigma_z\tbinom{\mu(z)}2=\mathbf{398}$$
$$2|\mathcal P_2|=2N_2^{\rm cw}=2\cdot149=\mathbf{298}\ ✗;\qquad 2(N_1{+}N_2)=2(50{+}149)=\mathbf{398}\ ✓✓$$
$$\textbf{根因}:\ \text{距离-1 之码字对（}50\ \text{对）之两个共同邻点}=\text{那两个码字\ \textbf{自身}};\ \text{亦计入 }\tbinom{\mu}{2}✓$$
$$\therefore\ \boxed{\Sigma_z\tbinom{\mu(z)}2=2(N_1+N_2)\ (\textbf{非}\ 2P_2)}\ ——\ \text{故它属\ \textbf{距离分布层}，非新量}✗$$

## §3 ③ 你 §3 恒等式之纠正（**✗**）

$$\text{你称}:\ \Sigma_{z\in Q}r(z)=|Y_2|=136;\qquad \textbf{实测}:\ \Sigma_{z\in Q}r(z)=\mathbf{112}$$
$$\textbf{精确修正}:\ \boxed{\Sigma_{z\in Q}r(z)=|Y_2|-\#\{y:z(y)\in C\}=136-24=\mathbf{112}}✓✓\ (\text{实测吻合})$$
$$\textbf{根因}:\ 24/136\ \text{个 }z(y)\ \text{是\ \textbf{码字}}（\notin Q）\Longrightarrow\ \text{其 owner pair 不在 }Q\ \text{之求和内}✗$$
$$\therefore\ \Sigma_{z\in Q}\delta(z)=\Sigma_{z\in Q}\tbinom{\mu(z)}2-112=\mathbf{145}\ (\text{实测})✓$$

## §4 ④ 碰撞量 $S$（**✓ 数值稳，但 $S/E$ 不恒定**）

$$d_H(c)=\#\{y\in Y_2:c\in O(y)\}\ (\text{即 }G\ \text{之对角});\quad \Sigma_c d_H(c)=272=2|Y_2|✓$$
$$d_H\ \text{分布}:\ \{0{:}14,1{:}18,2{:}38,3{:}23,4{:}26,5{:}1\}✓$$
$$\boxed{S=\Sigma_c\tbinom{d_H(c)}2=\mathbf{273}}\ (\text{C-S 下界 }(272^2/120-272)/2=172.27\Rightarrow173\ ✓)$$
$$\text{恒等式核查}:\ \Sigma_c d_H(c)^2=818=272+2\cdot273\ ✓$$
$$S/E:\ 120\text{-code }0.922\ \text{v.s. greedy }1.663/1.685/1.588\ \Longrightarrow\ S\ \textbf{不}\ \propto E\ ✗$$

## §5 ⑤ 一处新稳定比（**★ 值得记**）

$$|Y_2|/E:\ 0.459\ (120),\ 0.475,\ 0.474,\ 0.438\ \Longrightarrow\ \approx\mathbf{0.46}\ \textbf{稳定}$$
$$\therefore\ \text{若此稳定在其他码上保持}\Longrightarrow M=106\ (E{=}142)\ \text{时 }|Y_2|\approx65\ (\text{而非 }\ge\ )\ ——\ \text{但此为\ \textbf{经验规律}}✗\ (\text{非定理})$$

## §6 判定（**守你 §12 之纪律**）

$$\textbf{已证}:\ \text{rank}(A)=M-b(H)\ \text{（经典）};\ \Sigma\tbinom{\mu}2=2(N_1{+}N_2)\ \text{（距离分布层）};\ \Sigma_{z\in Q}r=|Y_2|-\#\{z(y)\in C\}$$
$$\therefore\ \text{你 §2 之}\ \delta(z)=\tbinom{\mu(z)}2-r(z)\ \text{之全局和}\ \textbf{由既有账目决定}\ (\text{秩公式 ＋ 距离分布})✗$$
$$\boxed{\text{判定}:\ \delta\text{-路线（含 }H\text{／秩／谱）}\ \textbf{落回经典};\ S\ \text{虽为真全局量但未建立 }E\text{-联系}}✗$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "秩公式跨码验证" "sumr=112" "碰撞量S"
技术词 秩公式跨码验证  命中文件数=0    ::
技术词 sumr=112     命中文件数=0    ::
技术词 碰撞量S       命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **四码全量实测 ＋ 两处我自身 bug 之更正（索引／未限制非码字）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；**未拟合** $S$ 与 $E$ ✓（仅报比值）
