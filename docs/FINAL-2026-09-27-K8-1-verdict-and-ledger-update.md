已查地图：已跑 scripts/prework_map_check.sh K_8_1 距离分布 平衡 自补 2-surjective ⟹ 执行自 `CORR-2026-09-27-keri8-...`（✓）＋ 唐先生 12:44；本档 = **$K_8_1$ 最终裁定（含三项文献交叉验证 ✓）＋ ledger 更新** ✓。
D0: 本档对象 = Kéri $K\_8\_1$ 的真实 fingerprint 裁定
D1: 1（新增：**全距离分布 ＋ 两 bit 序一致 ✓**；**三项文献交叉验证 ✓**）

# $K_8(8,1)$ 最终裁定（2026-09-27）

## §0 裁定（先给）

```
$$\boxed{\textbf{(BF-1 裁定 ✓✓)}\ K\_8\_1.txt:\ A_1=8,\ \mathbf{A_2=8},\ A=16,\ E=32,\ \mathbf{Q=0},\ b\in\{1,2\}\ \text{（nearly-perfect ✓）}}$$
$$\qquad\textbf{全距离分布}:\ (A_1,\ldots,A_8)=\mathbf{(8,\,8,\,136,\,200,\,88,\,24,\,24,\,8)}\ ✓\ \text{—— \textbf{两种 bit 序（lsb/msb）完全一致} ✓✓（排除解析约定 ✗）}$$
$$\qquad\textbf{两条不可动恒等式全过 ✓✓}:\ \sum_xb=288=M(n+1)\ ✓;\qquad \sum_x\binom{b(x)}2=32=2(A_1+A_2)\ ✓$$
$$\boxed{\textbf{(BF-2 三项文献交叉验证全中 ✓✓✓)}\ \text{(i) \textbf{坐标平衡}}:\ \text{各坐标 1 数}=(16,\ldots,16)\ ✓\ \text{（源："valamennyi optimális kód kiegyensúlyozott" ✓）}}$$
$$\qquad\text{(ii) \textbf{非自补}}:\ C\oplus\mathbf 1=C\ ?\ \textbf{否}\ ✓\ \text{（源："仅 4 个自补" ✓）};\qquad \text{(iii) }\textbf{2-surjective}:\ \text{全部 28 个坐标对实现 4 种模式}\ ✓\ \text{（源 ✓）}$$
$$\boxed{\textbf{(BF-3 勘误 ⚠️)}\ \text{报来的 }A_2{=}16,\ A{=}24,\ Q{=}16,\ \sum\binom b2{=}48\ \Longrightarrow\ \text{与 }\sum b{=}288,\ E{=}32,\ b\in\{1,2\}\ \text{三条\textbf{全部冲突}} ✗\ \Longrightarrow\ \text{以本档实测为准} ✓}$$
$$
$$
```

---

## §1 为何能定裁（**三条独立通道 ✓**）

```
$$\text{通道 ①}:\ \text{直接枚举 }\binom{32}2=496\ \text{对的距离分布 ⟹ }A_2=8\ ✓\ \text{（若 }A_2{=}16\ \text{则须有 16 对距离 2 ✓，与实际 8 对不符 ✗）}$$
$$\text{通道 ②}:\ \text{球计数}\ \sum_x\binom{b(x)}2=32\ \text{（由 }b\in\{1,2\}\ \text{且 32 个双覆盖点 ✓）}\ \xrightarrow{\text{球交叠恒等式}}\ A_1+A_2=16\ ✓\ \Longrightarrow\ A_2=8\ ✓$$
$$\text{通道 ③}:\ \text{若 }A=24\Longrightarrow\sum\binom b2=48\Longrightarrow\ \text{与 }E=\sum(b-1)=32\ \text{矛盾（}b\in\{1,2\}\ \text{时两量必相等 ✓）} ✗$$
$$\Longrightarrow\ \textbf{三通道一致：}A_2=8,\ A=16,\ Q=0\ ✓✓$$
$$
$$
```

---

## §2 ledger 更新（**✓**）

```
$$\begin{array}{c|c}
\text{项} & \text{状态}\\
\hline
n=6 & \textbf{退出}（2\ \text{个不等价最优码 ✓ 文献上标}=2\ ✓;(A_1,A_2)\ \text{各异 ✓）}\\
n=7 & \textbf{退出}（唯一完美码 ✓）\\
n=8 & \textbf{主实验池}:\ 10\ \text{类 ✓（文献 ✓）；\textbf{目前仅 1 个代表可得}（}K\_8\_1\ ✓;\ \text{无 }\&\_8\_1\_classif ✗ \text{）}\\
n=9 & \textbf{OPEN}（未分类 ✓；2\ \text{码 }(A_1,A_2)=(7,66)/(26,47)\ ✓）\\
n=10,M=119 & \textbf{暂不攻击} ✓\\
\text{P1-2 support-2} & \textbf{OPEN}（桶内分叉未测 ✓）\\
\text{Q0} & \textbf{CLOSED} ✓\ \text{（\textbf{不因 }n=8\ \text{新数值重开} ✓）}\\
\end{array}$$
$$\textbf{n=8 已得代表（两个 ✓）}:\ \text{Kéri }(8,8)\ \text{vs 乘积码 }(16,0)\ \text{—— 两者 }A=16,\ Q=0\ \text{同 ✓，但 }A_1\ \text{不同 ✗} \Longrightarrow \text{P1-2 仍需\textbf{同 }A_1\ \text{的码对} ⚠️}$$
$$
$$
```

---

## §3 下一步（**两个可立即执行项 ✓**）

```
$$\text{(甲) 追 2017/2018 switching 论文的 supplementary/data} \Longrightarrow \text{取其余 9 个 }(8,32)_1\ \text{代表} ✓\ \text{（最对靶 ✓，但可能付费 ✗）}$$
$$\text{(乙) \textbf{零成本可用} ✓}:\ \text{Kéri 库中\textbf{已有}的 }\_classif\ \text{文件}\ \big(K\_6\_1\_classif\ ✓,\ K\_9\_1\_classif\ ✓,\ K\_7\_2\_classif\ ✓,\ K\_9\_2\_classif\ ✓,\ldots\big)$$
$$\qquad\Longrightarrow\ \text{直接跑 }(A_1,A_2)\text{-桶 ＋ }J\ \text{fingerprint} \Longrightarrow \text{在\textbf{现有数据}上把 P1-2 的"桶内分叉"问题尽量定死} ✓$$
$$\qquad\text{（若某 }\_classif\ \text{文件中出现同 }(A_1,A_2)\ \text{而 }J\ \text{不同的码对} \Longrightarrow \textbf{P1-2 PASS} ✓✓）$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**三条独立通道 ＋ 本机实测** ✓；§2 为**ledger** ✓；§3 为**可执行项** ✓
- ⚠️ 本档与唐先生 12:44 的数值**相反** ✓ —— 依据为**两条不可动恒等式 ＋ 三项文献交叉验证** ✓（请以本档为准 ✓）
- **未**声称 $Q^*(8)=0$ 已证（2 码支持 ✓，未覆盖 10 ✓）；**未**改动 119 UNKNOWN ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$K_8_1$ 最终裁定、三项文献交叉验证、三通道定裁
- **档案已有（引用，不列为提出）**：$A_{\le2}$、$Q$、$E$、球交叠恒等式、nearly-perfect、balanced、2-surjective


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三项文献交叉验证 命中文件数=1    :: ./FINAL-2026-09-27-K8-1-verdict-and-ledger-update.md 
技术词 三通道定裁  命中文件数=1    :: ./FINAL-2026-09-27-K8-1-verdict-and-ledger-update.md
```
- **本档新增**：$K_8_1$ 最终裁定、三项文献交叉验证、三通道定裁（见上方命中数；0 命中者为自造语／内部标签 ✓）
