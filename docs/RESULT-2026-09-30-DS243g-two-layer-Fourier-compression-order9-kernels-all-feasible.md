# RESULT-2026-09-30-DS243g — (a) 之**两层 Fourier 压缩**：群环恒等式 $C=121\delta_0+60\mathbf1_H$ ✓；阶-9 核（12 循环子群）条件**全部可行** ⟹ **无 P1** ✗

> 空间 B｜非 C 号｜唐先生 13:14「开 (a)；先做代数压缩（两层 Fourier/商群分解），不要一上来 CP-SAT」｜**不主张任何新值**（V290）
> 时间：2026-09-30 14:0x

**已查地图**：承 `DS243e`（σ-轨道精化）／`DS243f`（类值纠正）
D0: 本档对象 = **档案已有**（(a) 之群环形式）之**谱压缩与核可行性**（新数学对象：无 ✗）
D1: 0（产出 = **一处尺度纠正 ＋ 一条恒等式 ＋ 一条全可行判定** ⚠️✓）

---

## §0 **尺度钉死**（⚠️ 纠正唐先生二处归一化）

$$\text{我们}: H=\mathbb Z_9^2,\ |H|=\mathbf{81}\ (\text{不是 }9)\ ✗;\quad \text{fiber } R_i\subseteq H;\ |R_i|=(36,40,45)$$
$$\textbf{(a)}:\ \forall\,0\ne h\in H:\ C(h):=\sum_i|R_i\cap(R_i-h)|=60;\quad C(0)=36{+}40{+}45=121$$
$$\boxed{C=121\,\delta_0+60\,\mathbf 1_H}\quad(\textbf{群环恒等式 ✓ —— 唐先生此点完全正确 ✓✓})$$
$$\text{Fourier}:\ \hat C(\chi)=\sum_i|\hat f_i(\chi)|^2 \Longrightarrow \chi\ne1:\ \hat C(\chi)=121-60=\mathbf{61}\ ✓;\quad \chi=1:\ \hat C(1)=121+60\cdot80=\mathbf{4921}\ ✓$$
$$\text{非平凡总能量}:\ \sum_{\chi\ne1}\hat C(\chi)=81\cdot121-4921=\mathbf{4880}$$
$$\textbf{⚠️ 纠正}:\ \text{唐先生之 }\hat C(1)=61+60\cdot9=601\ \text{与“}480\text{”\ 是 }|H|=9\ \text{之归一化} ✗;\ \text{正确为 }4921/4880\ ✓$$
$$\qquad\text{（“}601\text{”}\ = \sum_{i,j}m_{i,j}^2\ \text{是\ \textbf{另一对象}（}3H\text{-陪集占用矩阵）；数值巧合 ⚠️）}$$

## §1 两层分解：两条**不同**的商结构

$$\textbf{层 1（mod-3 层 / 非循环阶-9 子群）}:\ 3H=\{0,3,6\}^2\cong\mathbb Z_3^2;\quad H/3H\cong\mathbb Z_3^2\ (9\ \text{陪集})$$
$$\qquad \text{承载\ \textbf{阶-3 字符}（8 个）⟹ 已用: 四条平行类方程} ✓\ (\text{即 }m_{i,j}\ \text{结构})$$
$$\textbf{层 2（mod-9 层 / 循环阶-9 子群）}:\ \text{阶-9 字符之核} = \textbf{12 个} \text{循环阶-9 子群 ✓✓（全新约束面）}$$
$$\qquad \text{每个核 }K:\ \text{9 陪集};\ \text{记 }n^{(K)}_{i,j}=|R_i\cap(\text{陪集 }j)|;\ \text{6 个阶-9 字符 }m\in(\mathbb Z_9)^\times\ \text{给: } \sum_i\Big|\sum_j n^{(K)}_{i,j}\zeta_9^{mj}\Big|^2=61$$

## §2 **层 2 之可满足性（本档执行 ✓）**

$$\text{方法}:\ \text{每核独立，局部搜索（1-单位转移，3×9 变量、}0\le n\le9,\ \sum_j n^{(K)}_{i,j}=r_i\text{）}$$
$$\textbf{结果}:\ 12/12\ \text{核皆达\ \textbf{偏差 0}（独立复验 ✓✓）};\ \text{例（}K_1,\varphi=(1,0)\text{）}:$$
$$R_0{:}\ n=[7,2,5,6,2,3,5,4,2]\ (36);\quad R_1{:}\ [5,8,4,5,3,3,3,5,4]\ (40);\quad R_2{:}\ [4,5,4,5,9,4,3,5,6]\ (45)$$
$$\Longrightarrow\ \sum_i|\hat f_i(\chi_m)|^2=61\ \text{对全部 }m\in\{1,2,4,5,7,8\}\ ✓\ (\text{复验: 偏差 }\sim10^{-27};\ \text{精确和式核验 ✓✓})$$
$$\text{附带确认（与本档早先之自查一致 ✓）}:\ |\hat f_i|^2=(4.317\dots,\ 48.432\dots,\ 8.251\dots)\ \textbf{非整数} ⟹ \hat a_i\ \text{为\ \textbf{实代数整数}，非有理整数} ✓$$

$$\therefore\ \boxed{\text{阶-9 核谱条件\ \textbf{全部可行} ⟹ \textbf{无 P1}} ✗}\quad(\text{按唐先生预设: 仍相容 ⟹ 继续进 (b) ✓})$$

## §3 判读（重要）

$$\text{层 2 全部可行 ⟹ \textbf{粗层（计数级）必要条件已饱和} —— 与总量层饱和同型 ✓}$$
$$\text{但注意}: \ \text{12 个核之 }n^{(K)}\ \textbf{并非独立} —— \text{它们同源于同一 }(R_0,R_1,R_2)\ ⚠️$$
$$\therefore\ \text{下一刀有两条（皆“非搜索优先”）}:$$
$$\textbf{(甲)}\ \textbf{跨核一致性}:\ \text{求 12 组计数向量\ \textbf{联合可实现}（同源约束 ⟹ 比逐核强）} ✓$$
$$\textbf{(乙)}\ \textbf{(b) 跨陪集条件}（唐先生原定路线）:\ \text{两非零方向之差亦须 }=60\text{（以相对位移表出）} ✓$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\quad \textbf{(D2)}\ \text{skew 分支已移出主链} ✓（仅存档 ⚠️）;\quad \textbf{(D3)}\ \text{61-乘子假设仍待核} ⚠️$$
$$\textbf{(D4)}\ \text{未主张任何新值／未取文献原文（R16–17）／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
