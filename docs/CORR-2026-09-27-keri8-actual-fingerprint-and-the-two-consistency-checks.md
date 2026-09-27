已查地图：已跑 scripts/prework_map_check.sh Kéri 库 K_8_1 fingerprint 一致性 ⟹ 执行自 `P1-2-...-n8-construction`（✓）＋ 唐先生 12:42（Kéri 库 ✓）；本档 = **Kéri 码实算 ＋ 两处一致性检验（含对唐先生数字的更正 ✓）**。
D0: 本档对象 = Kéri `K_8_1.txt` 的真实 fingerprint
D1: 1（新增：**Kéri 库定位 ✓**；**两条一致性检验 ✓**；**Q*(8)=0 未被否证 ✓**）

# Kéri 库 ＋ $K_8(8,1)$ 真实 fingerprint（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BE-1 Kéri 库已定位 ✓)}\ \texttt{old.sztaki.hu/\textasciitilde keri/codes-hu/lemez/Binary/}\ ✓\ \text{含 }K\_n\_R(\_classif/\_uniq).txt\ \text{全系列} ✓}$$
$$\qquad\textbf{但（关键 ⚠️）}:\ \text{该目录\textbf{没有} }K\_8\_1\_classif.txt\ ✗;\ \text{而 }K\_8\_1.txt\ \textbf{只含 1 个码}（32 行 ✓）\Longrightarrow \textbf{10 个代表不在库中} ✗$$
$$\boxed{\textbf{(BE-2 Kéri 码实算 ✓)}\ K\_8\_1.txt:\ (A_1,A_2)=\mathbf{(8,\,8)}\ ✓,\ A=A_1{+}A_2=\mathbf{16}\ ✓,\ E=32\ ✓,\ \boxed{Q=2A-E=\mathbf 0}\ ✓}$$
$$\qquad b\text{-剖面}=\{1{:}224,\ 2{:}32\}\ ✓\ \Longrightarrow\ \sum_xb=288=M(n{+}1)\ ✓,\ \sum_x\binom{b}2=32=2A\ ✓\ \text{（\textbf{两条一致性检验全过} ✓✓）}$$
$$\qquad J=(J_2,J_3,J_4,J_5,J_6,J_7,\sum a_i^2)=(16,\,0,\,0,\,0,\,0,\,64,\,64)\ ✓;\quad a=(0,\dots,0,8)\ ✓$$
$$\boxed{\textbf{(BE-3 ⚠️ 对唐先生数字的更正 ✓)}\ \text{报来的 }A_2{=}16,\ A{=}24,\ \sum\binom b2{=}48,\ J_7{=}0\ \textbf{与 }M(n{+}1){=}288\ \text{及 }E{=}32\ \text{矛盾} ✗}$$
$$\qquad\text{证据}:\ \text{若 }A{=}24\Longrightarrow\sum\binom b2{=}48\Longrightarrow\sum b\ \text{与 }E\ \text{不能同时为 }288/32\ ✗;\ \text{且 }J_3{=}0\wedge J_7{=}0\Longrightarrow q\equiv0\Longrightarrow A_2{=}0\ ✗\ \text{（自相矛盾 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{"}Q^*(8)\ne0\text{"\ 不成立} ✗;\ \text{两可用最优码}\ \text{（本档 Kéri 码 ＋ 乘积码 ✓）}\ \textbf{均有 }A=16,\ Q=0\ ✓\ \Longrightarrow\ \textbf{Q}^*(8)=0\ \text{仍站得住} ✓$$
$$
$$
```

---

## §1 两码对照（**✓ 本机**）

```
$$\begin{array}{c|c|c|c|c|c|c|c}
\text{码} & A_1 & A_2 & A & E & Q & \sum\binom b2 & b\text{-剖面}\\
\hline
\text{Kéri }K\_8\_1 & 8 & 8 & \mathbf{16} & 32 & \mathbf 0 & 32 & \{1{:}224,\ 2{:}32\}\\
H(7,4)\times\mathbb F_2 & 16 & 0 & \mathbf{16} & 32 & \mathbf 0 & 32 & \{1{:}224,\ 2{:}32\}\\
\end{array}$$
$$\Longrightarrow\ \text{两码 }\mathbf{A=A_1+A_2=16}\ \text{相同 ✓（}\Rightarrow\ \text{van Wee 取等型 ✓）};\ \text{但}\ \mathbf{(A_1,A_2)}\ \text{分解不同} ✓\ (8,8)\ \text{vs}\ (16,0)$$
$$\qquad\Longrightarrow\ \text{与档案"球交叠封顶"一致 ✓（}A\ \text{同、分裂自由 ✓）};\ \text{对 P1-2：仍需}\ \textbf{同 }A_1\ \text{的码对} ⚠️\ \text{（此两码 }A_1\ne ✗）}$$
$$
$$
```

---

## §2 库中还有什么（**✓**）

```
$$\text{可用（本档已确认存在 ✓）}:\ K\_6\_1\_classif.txt\ ✓\ (\text{分类码表 ✓}),\ K\_9\_1\_classif.txt\ ✓\ (2\ \text{码 ✓}),\ K\_7\_2\_classif.txt,\ K\_9\_2\_classif.txt,\ \dots$$
$$\text{缺口 ⚠️}:\ \textbf{无 }K\_8\_1\_classif.txt\ ✗ \Longrightarrow \text{10 个 }(8,32)_1\ \text{代表不在库中};\ \text{需 2018 switching 论文或 Östergård 分类输出 ✓}$$
$$\text{附带可用（下一步 ✓）}:\ K\_6\_1\_classif.txt\ \text{（}n=6\ \text{的 2 个码 ✓）} \Longrightarrow \text{可直接跑 }(A_1,A_2)\ \text{桶（验证文献的"2 类 ✓"并测 }J\ \text{分叉 ⚠️）}$$
$$
$$
```

---

## §3 边界（诚实标注）

- §1 为**本机实算 ＋ 两条独立一致性检验** ✓；§2 为**库内容清单** ✓
- ⚠️ **本档更正了唐先生的三个数字**（$A_2$、$\sum\binom b2$、$J_7$ ✓）——依据是 $M(n+1)=288$ 与 $E=32$ 两个**不可动**的恒等式 ✓
- **未**声称 $Q^*(8)=0$ 已证（仅 2 码支持 ✓，未覆盖全部 10 ✓）；**未**改动 119 UNKNOWN ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Kéri 库定位、$K_8_1$ 实算 fingerprint、两条一致性检验
- **档案已有（引用，不列为提出）**：$A_{\le2}$、$Q$、$E$、球交叠恒等式、van Wee 取等、matching 定理


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Kéri 库定位  命中文件数=1    :: ./CORR-2026-09-27-keri8-actual-fingerprint-and-the-two-consistency-checks.md 
技术词 一致性检验  命中文件数=14   :: ./IP-2-card3-first-theorem-lock-attempt.md ./R_8v-transform-chain-audit.md ./R-A8.3-verify.md
```
- **本档新增**：Kéri 库定位、$K_8_1$ 实算 fingerprint、两条一致性检验（见上方命中数；0 命中者为自造语／内部标签 ✓）
