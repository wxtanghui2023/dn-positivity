已查地图：已跑 scripts/prework_map_check.sh pinning (6,12) 代表元 1986 ⟹ 执行自 PINNING-2026-09-26-crossvalidation-and-status 档；本档为**n=6 文献码闭环**（唐先生 2026-09-26 10:57 指令）；不开新方向 ✓。
D0: 本档对象 = (6,12)_1 的文献显式码与我方 Q-管道对接（非新对象）
D1: 1（新增独立对接：1986 文献码 → 我方 Q=4，且与我方样本类2 B₆-等价 ✓）

# PINNING-N6-CLOSED-2026-09-26 · 文献码闭环

## §1 文献源与显式码（**逐字抽取** ✓）

```
$$\text{源}: \text{G. D. Cohen, A. C. Lobstein, N. J. A. Sloane, \textit{Further Results on the Covering Radius of Codes},}$$
$$\qquad \text{IEEE Trans. Inform. Theory } \mathbf{32}(5)\ (1986)\ 680\text{--}694\ ✓\ （\text{免费全文}: \texttt{neilsloane.com/doc/Me127.pdf}\ ✓）$$
$$\text{Fig. 3 逐字行}: \texttt{000 100 000 010 000 001 100 111 010 111 001 111 011 000 101 000 110 000 111 011 111 101 111 110}$$
$$\text{分割 } 6=3+3\text{（分段常值码 ✓）};\ \text{权型}: (w_1,w_2)=(0,1)^{\times3},\ (1,3)^{\times3},\ (2,0)^{\times3},\ (3,2)^{\times3}\ ✓\ \text{共 }12\ \text{字 ✓}$$
$$C=\{000100,\ 000010,\ 000001,\ 100111,\ 010111,\ 001111,\ 011000,\ 101000,\ 110000,\ 111011,\ 111101,\ 111110\}$$
$$\text{论文附注}: \text{Stanton--Kalbfleisch 早期发表版\textbf{有错}（其实 }R=2\ ✗）\Longrightarrow \textbf{以本版为准}\ ✓$$
```

## §2 我方管道实算（**闭环 ✓**）

```
$$E=12\cdot7-64=20\ ✓\qquad \min_x b(x)=1\ \Longrightarrow\ \text{覆盖 ✓}\qquad b\ \text{分布}=\{1{:}48,\ 2{:}12,\ 3{:}4\}$$
$$\boxed{A_1=\mathbf{0}\ (\text{无距离 1 对 ✓}),\quad A_2=12,\quad A_1+A_2=12,\quad Q=\mathbf{4}}\ ✓\ (\text{核验 }2\cdot12-20=4\ ✓)$$
$$\textbf{B}_6\text{-规范形比对}: \text{与本方样本\textbf{类2 完全相同}}\ ✓✓\quad(\text{与类1 不同}\ ✓)$$
$$\Longrightarrow\ \boxed{\text{文献码} = \text{我方枚举到的类2};\ \text{两者 }Q\ \text{一致}\ ✓✓}\quad(\text{第二例成功对接: n=5 ✓, n=6 ✓})$$
```

## §3 n=6 现状（我方 + 文献）

```
$$\text{我方}: 194\ \text{个不同最优码} \to \textbf{2 个 } B_6\text{-等价类},\ \text{两类 } Q\ \text{均}=4\ ✓$$
$$\text{文献}: 1986\ \text{码} = \text{类2}\ ✓\ (\text{已对接})$$
$$\Longrightarrow\ \text{目前\textbf{所有}已知 }(6,12)_1\ \text{码皆 } Q=4\ ✓\ —— \text{唯缺"类数恰为 2"的文献确认}\ ✗$$
$$\text{（对比 n=4: 2 类同值 ✓; n=5: 1 类 ✓; 故"多类同值"模式在 } n=4,6\ \text{各现一次 ✓）}$$
```

## §4 剩余缺口与下一步（按成本 ✓）

```
$$\text{缺 ①}: (6,12)_1\ \text{与}\ (8,32)_1\ \text{的\textbf{类数}}（\text{把"找到 2 类"升级为"共 2 类" ✓）\Longrightarrow 2000\ \text{论文} ✗/\ \text{Kaski--Östergård } \S7.2.6 ✗$$
$$\text{缺 ②}: (8,32)_1\ \text{的全部代表元} \Longrightarrow \textbf{2018 switching 文献当作"代表元发生器"}\ ✓\ (\text{不是取它的类数 ✗})$$
$$\text{缺 ③}: \text{2018 的 semiautomorphism} \ne B_8\ ✓ \Longrightarrow \text{须 }B_8\text{-规范化后再算 }Q\ ✓$$
```

## §5 边界（诚实标注）

- §1 为**逐字抽取**（`Me127.pdf` 免费全文 ✓，Fig. 3 行 ✓）
- §2 为**实算**（覆盖性、b 分布、A_1/A_2、Q、B_6-规范形 ✓）
- §3 的"类数恰为 2"**未证** ✗（抽样不能证明完全性 ✗）
- **未**排除任何 n ✗；**未**声称 pinning 为定理 ✗；**未**对 n=10 外推 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 文献码闭环  命中文件数=0    :: 
技术词 类数确认     命中文件数=0    :: 
技术词 代表元发生器 命中文件数=0    :: 
技术词 分段常值码  命中文件数=0    ::
```

- **本档新增**（命中数=0）：文献码闭环、类数确认、代表元发生器、分段常值码
- **档案已有（引用，不列为提出）**：—
