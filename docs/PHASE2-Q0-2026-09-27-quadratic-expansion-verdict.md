已查地图：已跑 scripts/prework_map_check.sh Q0 二次展开 δ 矩 独立性 ⟹ 执行自 `PHASE2-KEY-...-ball-collapse`（✓）＋ 唐先生 12:16（(i) ＋ Q0 Gate ✓）；本档 = **Q0 判定：两个 STOP 条件均命中 ⟹ 不上 SDP** ✓。
D0: 本档对象 = $\zeta+(2^n-M)\ge0$ 的二次展开与其独立性
D1: 1（新增：**恒等式 $\zeta+(2^n-M)=(n+1)E-4A=\sum_x\delta(x)(n-\delta(x))$ ✓**；**正确界 $A\le\frac{(n+1)E}{4}$ ✓**）

# Q0 判定（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AK-1 二次展开 ✓)}\ \zeta+(2^n-M)=(n+1)E-4A=\sum_x\delta(x)\big(n-\delta(x)\big)\ ✓\ \text{（本机 6/6 精确验证 ✓）}}$$
$$\boxed{\textbf{(AK-2 Q0-a 命中 ⟹ STOP ✓)}\ \text{该约束在码层\textbf{完全等价于}线性界 }A\le\frac{(n+1)E}{4}\ ✓\ \text{—— 无任何新的局部交叉项} ✗}$$
$$\boxed{\textbf{(AK-3 Q0-b 命中 ⟹ STOP ✓)}\ \text{它就是 }\delta\ \text{矩关系 }n\sum\delta-\sum\delta^2\ge0\ ✓\ \text{（由逐点 }\delta\le n\ ⟸\ b\le n+1\ ✓\ \text{即得）}}$$
$$\boxed{\textbf{(AK-4 ⟹ 不上 SDP ✓)}\ \text{二次型 }q(x)=\zeta(x)+(2^n-\sum_cx_c)\ \text{的\textbf{全部码层内容} = 上述线性界 ✓ ⟹ 任何 QCQP/SDP 至多复现它} ✗}$$
$$\qquad\text{而该线性界本身}\ \textbf{non-leveraging} ✗\ \text{（}3\times\sim4\times\ \text{高于实测 ✓）⟹ 按唐先生 Gate：\textbf{登记后停止，不堆 SDP} ✓}$$
$$
$$
```

---

## §1 二次展开与恒等式（**✓**）

```
$$\text{由 }d\ \text{≤2 的球交叠常数（塌缩定理 ✓）}:\ \zeta=M(n^2+2n+2)-(n+2)2^n-4A\ ✓\ \Longrightarrow$$
$$\zeta+(2^n-M)=M(n^2+2n+1)-(n+1)2^n-4A=(n+1)\big[M(n+1)-2^n\big]-4A=\boxed{(n+1)E-4A}\ ✓$$
$$\text{又}\ \sum\delta=E\ ✓,\ \sum\delta^2=4A-E\ ✓\ \Longrightarrow\ (n+1)E-4A=n\sum\delta-\sum\delta^2=\sum_x\delta(x)\big(n-\delta(x)\big)\ ✓$$
$$\textbf{本机核对 ✓}:\ n=4,5,6\ \text{各 2 码}:\ (n+1)E-4A\ \text{与}\ \sum\delta(n-\delta)\ \textbf{逐位相等} ✓✓$$
$$\Longrightarrow\ \text{该不等式的\textbf{逐点来源} = }b(x)\le n+1\Longrightarrow\delta(x)\le n\ ✓\ \text{—— \textbf{平凡真} ✓}$$
$$
$$
```

---

## §2 算术更正（**两处 ⚠️，诚实 ✓**）

```
$$\textbf{更正 ①（界的形式）}:\ \text{此前（本会话 }5f546be\ \text{与唐先生 12:18）写 }U_\zeta=\frac{M(n^2+2n+3)-(n+1)2^n}{4}\ ✗$$
$$\qquad\text{正确（本档 ✓）}:\ \boxed{A_1+A_2\le\frac{(n+1)E}{4}=\frac{(n+1)\big(M(n+1)-2^n\big)}{4}}\ ✓\ \text{（根因：}M(n^2+2n+2)-M=M(n^2+2n+1)=(n+1)^2M-2^n\ \text{的合并 ✓）}$$
$$\begin{array}{c|c|c|c|c|c}
n & M & E & \text{正确界}\ \frac{(n+1)E}{4} & \text{旧（错）} & U_{\rm Delsarte}\\
\hline
4 & 4 & 4 & 5.000 & 7.000 & 6.000\\
5 & 7 & 10 & 15.000 & 18.500 & 19.250\\
6 & 12 & 20 & 35.000 & 41.000 & 51.000\\
7 & 16 & 0 & 0.000 & 8.000 & 87.111\\
8 & 32 & 32 & 72.000 & 88.000 & 256.000\\
9 & 62 & 108 & 270.000 & 301.000 & 706.219\\
\end{array}$$
$$\Longrightarrow\ \text{正确界在 }\mathbf{6/6}\ \text{例中\textbf{仍强于}纯 Delsarte} ✓\ \text{（更强于此前认知 ✓）};\ \text{但仍 }3\times\sim4\times\ \text{高于实测} ✗$$
$$\textbf{更正 ②（均匀点）}:\ \text{均匀点 }x_c=1/11\ \text{处 }M_{\rm relax}=2^n/(n+1)\ \text{（}\ne119\ ✗\text{）};\ \text{按\textbf{定义式}评估 }q(x):\ \zeta_{\rm unif}=-2\cdot2^n\cdot\tfrac{n}{n+1}=-1861.8\ ✓$$
$$\qquad\text{而 }-(2^n-M_{\rm relax})=-930.9\ ✓\ \Longrightarrow\ \textbf{违反} ✓\ \text{——故二次型对均匀点\textbf{确有切割力} ✓（唐先生观察对 ✓）}$$
$$
$$
```

---

## §3 判定（**按 Gate 执行 ✓**）

```
$$\text{Q0-a（是否只是已有 pair-distance 计数？）}:\ \text{码层上 }q\equiv(n+1)E-4A\ ✓\ \text{（只含 }M,E,A\ ✓）\ \Longrightarrow\ \textbf{命中} ⟹ \text{STOP} ✓$$
$$\text{Q0-b（是否只是 }\delta^2\ \text{的另一种写法？）}:\ q=n\sum\delta-\sum\delta^2\ ✓\ \Longrightarrow\ \textbf{命中} ⟹ \text{STOP} ✓$$
$$\Longrightarrow\ \text{两者皆命中} ⟹ \textbf{不进入 SDP} ✓\ \text{（唐先生 Gate ✓）}$$
$$\text{登记类别（唐先生指定 ✓）}:\ \boxed{\textbf{valid, non-profile-appearing quadratic constraint, but no leverage beyond the linear bound }A\le\frac{(n+1)E}{4}} ✓$$
$$\qquad\text{即}:\ \text{它的"二次外貌"来自 }(1-x_v)x_c\ \text{项 ✓，但码层内容被球交叠完全压成线性 }A\ \text{界 ✓——这是塌缩定理的\textbf{更强版本} ✓✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1–§2 为**恒等式 ＋ 本机核对 ＋ 两处更正** ✓；§3 为 **Gate 执行** ✓（遵守"不堆 SDP" ✓）
- **未**声称新机制 ✗；**未**声称收紧 119 ✗；**未**改动 UNKNOWN ✓
- 本档净收益 ✓：**正确界 $(n+1)E/4$**（强于此前认知 ✓）＋ **二次外貌→线性内容的完整解释** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Q0 二次展开判定、正确界 $(n+1)E/4$、均匀点切割力的定义式评估
- **档案已有（引用，不列为提出）**：$\zeta$、$\delta$、$A_{\le2}$、Delsarte LP、球交叠常数、M-2A′


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Q0 二次展开判定 命中文件数=1    :: ./PHASE2-Q0-2026-09-27-quadratic-expansion-verdict.md 
技术词 正确界        命中文件数=2    :: ./V103-archive-tension-resolution.md ./PHASE2-Q0-2026-09-27-quadratic-expansion-verdict.md
```
- **本档新增**：Q0 二次展开判定、正确界 $(n+1)E/4$、均匀点切割力的定义式评估（见上方命中数；0 命中者为自造语／内部标签 ✓）
