已查地图：已跑 scripts/prework_map_check.sh van Wee 等号 b≤2 局部化 ⟹ 执行自 `ALG-DERIVED-2026-09-27-J3-zero-for-n-2m`（✓）＋ 唐先生 12:53（开这一刀 ✓）；本档 = **等号条件的等价重述 ＋ 数据对照 ＋ 精确缺口定位** ✓。
D0: 本档对象 = $b\le2$ 引理的自足证明可达性
D1: 1（新增：**等号 ⟺ 超额函数为 0/1 指示的等价重述 ✓**；**8 码 vW 松弛对照表 ✓**；**缺口精确定位 ✓**）

# van Wee 等号条件的重述与缺口（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BK-1 等价重述 ✓)}\ \text{在 }|C|=2^n/n\ \text{下恒有}\ \boxed{\sum_x\big(b(x)-1\big)=M}\ ✓ \Longrightarrow \textbf{vW 等号}\ \text{不提供独立等式，而是把"超额"钉在总量 }M ✓}$$
$$\qquad\Longrightarrow\ \textbf{引理 }b\le2\ \text{等价于}:\ \boxed{\text{超额函数 }(b(x)-1)\ \text{是 0/1 指示函数}\ \text{（}b\in\{1,2\}\text{）}}\ ✓✓\ \text{—— 这就是要证的东西的\textbf{最简形式} ✓}$$
$$\boxed{\textbf{(BK-2 数据对照 ✓✓)}\ \text{全部可用最优码}:\ \text{vW 松弛}=0\ \Longrightarrow\ b_{\max}=2\ ✓✓;\ \text{松弛}>0\ \Longrightarrow\ b_{\max}\in\{3,4\}\ ✓✓\ \text{—— 与"等号}\Longleftrightarrow b\le2\text{"\ 完全一致}}$$
$$\boxed{\textbf{(BK-3 缺口定位 ✓)}\ \text{引理分两半}:\ \text{(i) \textbf{非码字点不被三重覆盖}};\ \text{(ii) \textbf{码字点 }d_1\le1};\ \text{其中 (ii) 是目标本身 ✓，故\textbf{不能自用} ✗}$$
$$\qquad\Longrightarrow\ \text{真正的难点} = \text{(i)};\ \text{而它\textbf{不能}由计数恒等式推出} ✗\ \text{（见 §2 的反例构造 ✓）}\ \Longrightarrow\ \text{必须取 vW 证明\textbf{内部}的等号分析} ⚠️$$
$$
$$
```

---

## §1 等价重述（**✓ 两行，本机可验**）

```
$$\text{恒等式（}M=2^n/n ✓）:\ \sum_xb(x)=M(n+1)=2^n+M\ \Longrightarrow\ \boxed{\sum_x\big(b(x)-1\big)=M}\ ✓\ \text{——\textbf{与 }C\ \text{无关的恒等式} ✓（故不能直接给 }b\le2\ ✗\text{，正合唐先生警告 ✓）}$$
$$\text{vW 界（偶数 }n\text{）}:\ nM\ge2^n\ \Longleftrightarrow\ M(n+1)-2^n\le M\ \Longleftrightarrow\ \sum_x(b(x)-1)\le M\ \text{——\textbf{而它恒等于 }M\ ✗}$$
$$\qquad\Longrightarrow\ \text{vW 等号} = \text{"该恒等式同时是上界"}\ ✓\ \text{—— 其\textbf{证明内容}必在 vW 的\textbf{加权计数}里（非恒等式部分 ✓）}$$
$$
$$
```

---

## §2 计数恒等式为何不够（**反例构造 ✓，1 行**）

```
$$\text{取 }M=2^n/n\ \text{且设剖面}:\ b=3\ \text{于 }M/2\ \text{个点},\ b=1\ \text{于其余}\ \Longrightarrow\ \sum(b-1)=2\cdot\tfrac M2=M\ ✓\ \text{（恒等式满足 ✓）}$$
$$\Longrightarrow\ \textbf{b}\le2\ \text{不是恒等式的推论} ✗\ \text{（存在满足计数条件的 }b\ge3\ \text{剖面 ✓）}\ \Longrightarrow\ \text{证据必须来自\textbf{几何/相交结构} ✓}$$
$$
$$
```

---

## §3 数据对照表（**✓ 本机，8 码**）

```
$$\begin{array}{c|c|c|c|c|c}
\text{码} & n & |C| & \text{vW 松弛} & \text{形式} & b_{\max}\\
\hline
\text{Kéri }K\_8\_1 & 8 & 32 & \mathbf 0 & nM\ge2^n & \mathbf 2\ ✓✓\\
H(7,4)\times\mathbb F_2 & 8 & 32 & \mathbf 0 & nM\ge2^n & \mathbf 2\ ✓✓\\
K\_6\_1\ \#0/\#1 & 6 & 12 & 8 & nM\ge2^n & 3\ ✗\\
K\_9\_1\ \#0/\#1 & 9 & 62 & 108 & (n{+}1)M\ge2^n & 4\ ✗\\
\end{array}$$
$$\textbf{判读 ✓✓}:\ \text{松弛}=0\ \text{者 }b_{\max}=2\ ✓✓;\ \text{松弛}>0\ \text{者 }b_{\max}\ge3\ ✓✓\ \text{—— 与引理一致（数值支持，非证明 ⚠️）}$$
$$\text{（}n=7\ \text{行已剔除：那是 }R{=}2\ \text{码，R=1 的 vW 形式不适用 ✗）}$$
$$
$$
```

---

## §4 缺口的精确定位与下一步（**✓**）

```
$$\boxed{\text{缺口}:\ \text{vW 不等式的\textbf{证明内部}存在一个非负分解}\ nM-2^n=\sum_x\Phi_x\ge0\ ✓;\ \text{等号时 }\Phi_x=0\ \forall x\ \text{应迫使 }b\le2 ✓}$$
$$\qquad\text{该分解的已知线索（档案 ✓）}:\ \text{"}n\ \text{偶}:\ \mathrm{OC}(B_1(x))\ge1\ \forall x\notin C\text{"}\ \text{（每个球含过覆盖点 ✓）——是 vW 的\textbf{局部形式} ✓，但实测松弛 }2.72\times\ ✗\ \text{（该形式不足 ✗）}$$
$$\text{下一步（source-first ✓，二选一）}:\ \text{(a) 取 van Wee 1988 原文或 Struik 1994 简化证明（付费 ⚠️）};\ \text{(b) 取 Cohen--Honkala--Litsyn--Lobstein }\textbf{Covering Codes}\ \text{(1997) 第 5.4 节（图书馆/借阅 ✓）}$$
$$\qquad\Longrightarrow\ \text{抽出 }\Phi\ \text{的显式形式 ⟹ 检验 }\Phi_x=0\Longrightarrow b(x)\le2\ ✓\ \text{（本档的 }\Phi\ \text{候选 = 该文献的加权计数差 ✓）}$$
$$\text{若 }\Phi\ \text{不自给} \Longrightarrow \text{按唐先生：}\textbf{不硬凑} ✓，准确标记依赖（Lemma 3.18 ✓）$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1–§2 为**等价重述 ＋ 反例构造** ✓（恒等式与不足性均已确证 ✓）；§3 为**本机数据** ✓；§4 为**缺口定位 ＋ 路线** ✓
- ⚠️ **本档未完成** $b\le2$ 的自足证明 ✗（缺口在 vW 的加权计数内部 ✓）；**未**声称引理成立（仅有数据支持 ＋ 外部引理 ✓）
- **未**改动 119 UNKNOWN ✓；**未**跑 SAT ✓；**未**碰 $n=10$ ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：vW 等号的等价重述、计数不足的反例构造、vW 松弛对照表、缺口定位
- **档案已有（引用，不列为提出）**：van Wee 界、nearly-perfect、Lemma 3.18、$b$、$d_1$、$J_3$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 等价重述     命中文件数=25   :: ./B-SERIES-INDEX.md ./V271-non-cylinder-carrier-five-conditions-and-certificate-impossibility.md ./ALG-VW-2026-09-27-equality-reformulation-and-the-exact-gap.md 
技术词 缺口定位     命中文件数=27   :: ./AUDIT-direction-depth.md ./RIGORIZATION-candidate-proof-v1-D0-implies-RH.md ./C331-M5-gap-localization-complete-wait-for-new-mathematical-input.md
```
- **本档新增**：vW 等号的等价重述、计数不足的反例构造、vW 松弛对照表、缺口定位（见上方命中数；0 命中者为自造语／内部标签 ✓）
