# CORRECTION-2026-09-30 — **逐坐标构造法不可能产 107** ✗（表格硬数据：包络 $M\lesssim20$、单步跑**逾一周**）⟹ BÖW-107 指纹须修正为**解析型 general bound**

> 空间 B｜非 C 号｜唐先生 16:43「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 17:3x

**已查地图** ✓：`RESULT-2026-09-30-coord-search`（我方实现：n=4/5 通过、n=6 超时 ✗）／`FINGERPRINT-2026-09-30`／L1554（支撑层＝自由度）
D0: 本档对象 = **档案已有**（Kéri 第 9 章表格）之**包络判定**（新数学对象：无 ✗）
D1: 0（产出 = **一条包络否证 ＋ 一条指纹修正 ＋ 两条工程手法留存** ⚠️✓）

---

## §0 **硬数据：该法之实践包络（Kéri 第 9 章表格逐字 ✓）**

$$\text{R=1 表}:K(2,3;1){=}12\ [35,123,138,23];\ K(3,2;1){=}16\ [42,2019,1840,3];\ K(1,5;1){=}16\ [34,342,1731,845,120];\ \color{red}{\mathbf{K(5,0;2){=}8\ [37,438,499,1]\ \leftarrow [130]\ \text{之二元结果}}}$$
$$\text{R=2 表（最大者）}:K(2,5;2){=}11\ [285,14037,263535,\mathbf{940216},179739,91];\quad K(3,4;2){=}13\ [710,122433,\mathbf{3964002},\mathbf{5878979},46185,1]$$
$$\textbf{时间（逐字译）}:\ \text{“因之，等待那}\textbf{\text{需逾一周机时}}\text{之末步结果时，我曾期望……”}\ (K(1,8;2){=}20\ \text{之证明})$$
$$\textbf{包络}⟹\ \boxed{M\lesssim20,\ \text{坐标数}\lesssim9,\ \text{文件大小}\lesssim6\times10^6,\ \text{单次运行可达\ \textbf{逾一周}}}\ ✗✓$$

## §1 **否证：该法\ \textbf{不可能} 产出 107** ✗

$$\text{我方目标}:\ n{=}10\ \text{二元},\ M{=}106\ (=\ K(10,1)\ \text{之目标值附近})\ ✗$$
$$\text{而包络为 }M\lesssim20\ ⟹\ \textbf{超出 2 个数量级以上};\ \text{且 }S_2,S_3\ \text{层之记录数}\ \binom{M+3}{3}\ \text{量级在 }M{=}106\ \text{时已然爆炸}\ ⚠️$$
$$\text{我方自实现亦独立印证}:\ n{=}6,M{=}11\ \text{已 100 s 超时（}\ge65682\ \text{nodes，末层仍增长）} ✗$$
$$\therefore\ \boxed{\text{逐坐标构造法\ \textbf{不是} 107 之来源}}\ ✗✓\ \text{（前一轮之假设须\ \textbf{撤销}} ⚠️)$$

## §2 **指纹修正（据 §0–§1 ✓）**

$$\text{[130]\ \textbf{\text{三部分}}}\ \text{（摘要＋Kéri 证言合成 ✓）}:\ \textbf{(i)}\ \text{general lower bound for }R{=}1\ \longrightarrow\ \textbf{\text{此为 107 之出处（解析型）}}\ ⚠️;\ \textbf{(ii)}\ \text{计算机分类（}\textbf{\text{小 }M}\text{：}K(5,0;2){=}8\ ✓,\ K(9,2){=}16\ ✓）;\ \textbf{(iii)}\ \text{自同构型新构造}$$
$$\Longrightarrow\ \text{“多计算机结果”＝ (ii)(iii)，而 107 ＝ (i)}\ ✓\ \text{—— 与我方档案定理 A（}\textbf{107\ \text{必出自非松弛／整性论证}}\text{）不冲突} ✓$$
$$\text{故下一步应攻}:\ \mathbf{[130]\ \text{之 general }R{=}1\ \text{lower bound}}\ \text{（而非其计算部分 ✗）} ⚠️\ \text{—— 但其正文不可得} ✗$$

## §3 **两条工程手法留存（可复用 ✓✓）**

$$\textbf{(a) 廉价同构约化（无需 nauty ✓✓）}:\ \text{“码内码字按坐标序\ \textbf{字典不减} 排列；对整个码之复形用\ \textbf{列优先字典序}”};\ \text{且}\ \textbf{\text{不真做排序}}\ ——\ \text{只查“是否有等价码在列优先字典序中\ \textbf{居前}}”，无则存} ✓$$
$$\textbf{(b) 坐标序逆转（}\ t\ \text{小、}b\ \text{大时大幅减文件 ✓✓）}:\ \text{逐字}\ \text{“当 }t\ \text{小、}b\ \text{大时}\ \textbf{\text{逆转坐标顺序}}\text{”};\ \text{例}\ K(1,5;1){=}16\ \text{之文件序 }11,35,115,72,120\ \text{（远小于原变体）};\ K(1,9;3){=}12\ \text{：}43,513,8502,154515,\mathbf{899477},206227,4496,51,5\ ✓$$
$$\qquad\text{（注：文件大小先增后}\ \textbf{崩落}\ ——\ \text{覆盖约束在末层强力剪枝 ✓✓）}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 实践包络     命中文件数=1    :: 本档
技术词 坐标序逆转  命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \text{两词仅本档命中} \Longrightarrow \textbf{本档新增} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓;\quad \text{通用词（不计）}:\ \text{“包络／逆转”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{前轮假设已\ \textbf{明示撤销}（不留错账 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
