已查地图：命中（`M03-b-parametrized-soules1-and-epsilon-strip`）⟹ `(3a)` 2026 原文证明链对齐与 sharpness 判定，不开新案
D0: 本档对象 = **2026 原文（arXiv:2608.19435）证明链逐段对齐**（`R` 归约 → `Remark 2.3` → 临界移位 `c^*` → 条件 (6) → `4\lambda_1\le9\lambda_3-S` → `Lemma 4.2/4.3` → `C_5` → `Thm 2.1`）＋ **先生四问逐条作答** ＋ **sharpness 判定：方法锋利（无余量）** ＋ **与本行 `\varepsilon` 条带的叠合检查**
D1: 1（首次逐段对齐 2026 证明链并定位"临界步"，产出显式余量 `\delta/36`）
[RESEARCH]

# **`(3a)`：2026 证明链对齐与 sharpness**

## §1 证明链逐段对齐（原文实读）

```
$$\boxed{\text{原 PDF}}\ \texttt{sources/Jin-Ke-Sui-2026-new-impossibility-region-5x5-SNIEP.pdf}\ (42\ \text{页},\ 82740\ \text{字符})$$ ✓
$$\text{结构}:\ \text{Thm 2.1 (p5)}\ +\ \text{Remark 2.2/2.3/2.4 (p5–7)}\ +\ \text{Lemma 4.1–4.5 (p9–13)}\ +\ \text{App.\ (p22+)}\ +\ \text{Sec.3 网络建模}$$ ✓
$$\textbf{(a)}\ \text{残区归约（Remark 2.2）}:\ S\ge\lambda_3\Rightarrow(\lambda_1,\lambda_2,\lambda_4,\lambda_5)\ \text{四元可实现}\Rightarrow\text{块对角}\Rightarrow\text{可实现};\ \ S\ge\lambda_1/2\Rightarrow\text{与 }\lambda_3>S\ \text{矛盾}$$ ✓✓
$$\qquad \Longrightarrow\ \text{真正未覆盖区}=\ R:\ \lambda_1=\max|\lambda_i|,\ \lambda_1>\lambda_2\ge\lambda_3>0>\lambda_4\ge\lambda_5,\ 0<S<\min\{\lambda_3,\lambda_1/2\}$$ ✓
$$\textbf{(b)}\ ⭐\text{边界来源（Remark 2.3，本档核心）}:\ \text{对角移位 }B=A+cI_5\ (\text{把低迹对象推进高迹区})$$
$$\qquad \text{高迹要求}:\ \operatorname{tr}(B)\ge\lambda_1(B)/2\iff\boxed{c\ \ge\ \frac{\lambda_1-2S}{9}}\quad(6)$$ ✓✓
$$\qquad \text{关键选择（临界）}:\ c=c^*:=\frac{\lambda_3-S}{4}\ \text{使 }\boxed{\lambda_3(B)=\operatorname{tr}(B)}\ \text{（高迹必要条件的\textbf{边界上}}）$$ ✓✓✓
$$\qquad\qquad \text{理由（原文逐字）}:\ \text{"Merely placing }B\text{ in the high-trace regime does not by itself provide enough structure};\ \text{at equality }B\text{ lies on the boundary... the boundary condition is precisely what is used in Lemma 4.3 to obtain a complementary commuting matrix, whose support is eventually reduced to a five-cycle"}$$ ✓✓
$$\qquad \text{合并}:\ c^*\ge\frac{\lambda_1-2S}{9}\iff\boxed{4\lambda_1\le9\lambda_3-S}\ \Longleftarrow\ \textbf{即 }W\ \text{的定义式}$$ ✓✓✓
$$\textbf{(c)}\ \text{引擎（Lemma 4.2）}:\ \text{高迹区内的\textbf{严格正}矩阵必满足\textbf{严格} }\lambda_3(B)<\operatorname{tr}(B)\ \Longrightarrow\ \text{与 }\lambda_3(B)=\operatorname{tr}(B)\ \text{冲突}$$ ✓✓
$$\textbf{(d)}\ \text{后续（Lemma 4.3–4.5）}:\ \text{边界条件}\Rightarrow\text{互补交换矩阵}\Rightarrow\text{支撑约化为五环 }C_5\Rightarrow\text{矛盾}\Rightarrow\ \text{Thm 2.1}$$ ✓
```

## §2 先生四问逐条作答

```
$$\textbf{问 1（}4\le9b-S\ \text{首次出现处／性质）}:\ \text{它\textbf{不是}人为充分条件、\textbf{不是} AM–GM 型阈值、\textbf{不是}判别式零点；}$$
$$\qquad \text{而是}\ \boxed{\textbf{两个精确代数条件的可满足性阈值}}:\ (\text{i})\ \text{临界选择 }\lambda_3(B)=\operatorname{tr}(B);\ (\text{ii})\ \text{高迹要求 }\operatorname{tr}(B)\ge\lambda_1(B)/2$$ ✓✓✓
$$\textbf{问 2（}S\ \text{的使用方式）}:\ \text{全链对 }S\ \textbf{仿射};\ \text{只用}\ 4\lambda_1\le9\lambda_3-S\ \text{这一处（}S\ \text{以 }-S\ \text{线性出现）};$$
$$\qquad \operatorname{tr}(B)=S+5c,\ \lambda_1(B)=\lambda_1+c,\ \lambda_3(B)=\lambda_3+c\ \Longrightarrow\ \text{常数 }4=5-1,\ 9=10-1\ \textbf{（纯计数）}$$ ✓✓✓
$$\textbf{问 3（局部外推测试）}:\ \text{令 }\boxed{\delta:=9\lambda_3-S-4\lambda_1}\ \text{（本行族内 }\delta=2\varepsilon\text{）};\ \text{则 (6) 的余量为}$$
$$\qquad \frac{\lambda_3-S}{4}-\frac{\lambda_1-2S}{9}=\frac{9\lambda_3-9S-4\lambda_1+8S}{36}=\boxed{\frac{\delta}{36}}$$ ✓✓✓
$$\qquad \Longrightarrow\ \delta>0\ (\text{即 }4\lambda_1>9\lambda_3-S,\ \text{进入 }R\setminus W)\ \text{时 }c^*\ \textbf{恰好违反 (6)} \Longrightarrow B\ \text{不在高迹区} \Longrightarrow \textbf{Lemma 4.2 前提失效}$$
$$\qquad \Longrightarrow\ \text{不存在 }F(\lambda)\ge C\delta\ \text{型外推};\ \text{全链\textbf{没有丢掉任何正项}}$$ ✓✓✓
$$\textbf{问 4（sharpness 来源）}:\ \text{无粗估计、无被丢正项};\ \text{阈值来自}\textbf{可行性等式} \Longrightarrow \textbf{方法锋利}$$ ✓✓✓
$$\textbf{问 5（结论）}:\ \boxed{\textbf{证明方法本身 sharp}}\ ——\ \textbf{在 }\delta>0\ \text{时符号\textbf{立即翻转}的那一步} =\ \boxed{\text{条件 (6) ／ Lemma 4.2 的高迹前提}};\ \text{该机制无法外推}$$ ✓✓✓
$$\qquad \textbf{⚠️ 措辞边界}:\ \text{"方法锋利"}\ne\text{"结论锋利"}（\text{后者需存在 }W\ \text{外侧的可实现点，原文\textbf{未声称}；p4/p41 的 }sharp\ \text{均指 }Jin\ \text{的 }NMF\ \text{工作，与边界无关）$$ ✓✓
```

## §3 与本行 `\varepsilon` 条带的叠合检查（先生要求的合流判定）

```
$$\text{本行族}: \Lambda(t,\varepsilon),\ 9b-S=4+2\varepsilon \Longrightarrow \delta=2\varepsilon;\quad \text{2026 机制余量}=\frac{\delta}{36}=\frac{\varepsilon}{18}$$ ✓✓
$$\varepsilon\ge0\ (\text{即 }W): \text{余量}\ge0 \Longrightarrow \textbf{2026 机制可用} \Longrightarrow \text{不可实现}$$ ✓
$$\varepsilon\in(4t-2,\,0)\ (\text{即本行条带}): \text{余量}<0 \Longrightarrow \textbf{2026 机制不可用};\ \text{同时 Soules-1 被解析排除}$$ ✓✓
$$\Longrightarrow\ \textbf{合流判定}:\ \text{两者\textbf{不构成 }W\ \text{的外侧扩张}，而是从两侧\textbf{夹住}同一前沿}:$$
$$\qquad \boxed{\partial W\ \text{之左（}\varepsilon\ge0\text{）}:\ \text{2026 不可实现}\ |\ \partial W\ \text{之右（}(4t-2,0)\text{）}:\ Soules\text{-1 构造失败且 2026 机制失效}}$$ ✓✓✓
$$\text{交叉核验}:\ \text{原文 Remark 2.4 的例子 }\bigl(1,\tfrac12,\tfrac12,-\tfrac{19}{24},-\tfrac{19}{24}\bigr)\ \textbf{正是本行族形状}（t=\tfrac12,\ q=\tfrac{19}{24}>\tfrac{18}{24}=q(\tfrac12)\text{）};$$
$$\qquad 4\lambda_1-(9\lambda_3-S)=-\tfrac1{12}<0\ \text{（在 }W\ \text{内）}\ \checkmark;\quad \text{而本行 }\Lambda(\tfrac12)\ \text{恰在 }\partial W\ (9b-S=4)\ \checkmark$$ ✓✓（两族几何完全吻合）
$$W\supsetneq W\ \text{的真正扩张须靠\textbf{新机制}}（\text{不能靠"把 2026 论证外推"）$$ ✓✓✓
```

## §4 下一步

```
$$\boxed{\text{(3b)}}\ \text{条带 }(4t-2,0)\ \text{内换机制试 }P2:\ Soules\text{-}2（\text{需先补原文}）／LS／ES／直接矩阵构造$$ ✓
$$\boxed{\text{(3c)}}\ \text{把"两侧夹住同一前沿"登记为\textbf{靶区资产}（不宣称 }W\ \text{扩张）}$$ ✓
$$\boxed{\text{(3d)}}\ \text{若要做真扩张}:\ \text{须在条带内找到\textbf{与高迹必要条件无关}的新不可行机制（例如低迹区专用的必要条件）}$$ ✓✓
【⛔ 纪律】 本轮为**原文实读＋代数推导**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 为原文逐字实读（含 Remark 2.3 引语）；§2 的 `\delta/36` 为本行自证；§2 问 5 的"方法锋利 ≠ 结论锋利"为强制措辞 ✓

## §附 【技术词回查】（补录）
```
技术词 threshold        命中文件数=38   :: ./grh-goldbach-paper-draft-v2.md ./ALIGN-A4-A5-with-our-results.md ./PAPERA-v2-structure.md 
技术词 sharpness        命中文件数=29   :: ./C3814-sharp-closure-of-C380-13-trig-dual-type-sigma-a-le-6c0.md ./V2-28B-L52-mechanism-identified-verdict-OPEN.md ./C77-lemma32-erratum-confirmed-fork-resolved-and-SQ1-verdict.md 
```
