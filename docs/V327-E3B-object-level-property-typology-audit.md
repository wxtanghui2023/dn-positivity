# V327 / E3-B — **对象级性质类型学审计**（四类机制）

> 唐先生 2026-09-16 17:18 拍板。第一轮**只做类型学审计**；**不要求已产生 RH 后果**；R-H-blind 优先；**不预判 DEAD**。
> 立题动机（由 V326 逼出）：$$\boxed{\text{操作之间找不到 C3}} \Longrightarrow \text{改问}\ \boxed{\text{一个单独的算术对象，是否存在不可压缩的全局性质？}}$$
> 这正是**绕开 V277-A／V271-A 的"有限值／有限证书"前提**的入口。

---

## 1. 对象空间与四道门（B1–B4）
$$\text{设}\ M_T=(O_T,R_T)。\ \text{E3-B}\ \textbf{不要求}\ \mathcal P(M_T)\ \text{有限可计算}，\text{但：}$$
$$\textbf{B1 生成来源优先}：\text{须存在与 RH 无关的构造}\ M_T\longmapsto\mathcal P(M_T)，\text{且}\ \mathcal P\ \textbf{在研究开始前固定}$$
$$\qquad\textbf{禁止}：\mathcal P(M_T)：＝\text{"RH 成立时}\ M_T\ \text{具有的性质"}\ \text{及其隐式版}\ \mathcal P(M_T)\iff\text{某已知 RH criterion}\ \Longrightarrow\mathrm{DEAD}$$
$$\textbf{B2 放松"有限可计算"，但不得松到"任意命题"}：\text{V277-A 关（有限值＋可计算}\Rightarrow\text{柱型）；V271-A 关（有限证书}\Rightarrow\text{柱型）}$$
$$\qquad\text{可允许}\ \mathcal P\ \text{不是有限证书，但}\ \textbf{不能}\ \text{接受任意}\ \mathcal P\in\{\mathrm{True},\mathrm{False}\}\ \text{（否则对象空间}\ =\ \text{"所有关于}\ M_T\ \text{的命题"}，\text{即把 RH 塞进 predicate）}✗$$
$$\qquad\Longrightarrow\ \text{须新增约束}\ \boxed{\text{P-origin}}：\mathcal P\ \text{必须由}\ \textbf{对象自身的自然结构} \text{产生}$$
$$\textbf{B3 优先找"不可有限见证"的性质}：\text{不找}\ \exists C_T:C_T\Rightarrow\mathcal P，\text{而找}\ \boxed{\mathcal P\ \text{成立但不存在有限证书能压缩它}}$$
$$\textbf{B4 第五行所需强现象}：\mathcal P\ \textbf{对所有有限截断都不可充分见证}，\text{且}\ \mathcal P\Rightarrow\{\text{新 admissible restriction},\ \text{新 spectral localization},\ \lambda>1\}\ \text{之一}$$

## 2. 四类机制的类型学审计（每类回答三问）

### B-I 无限一致性：$\mathcal P(M)=\forall n,\ P_n(M)$
$$\textbf{自然来源}\ ✓\ \text{（截断全满足型：Mertens 型界、前}\ n\ \text{个零点位置型、有限 Euler 积逼近型）}$$
$$\textbf{结构判定（本档核心）}：\forall n\,P_n\ \text{的否定}\ \Longleftrightarrow\ \exists n\,\neg P_n\ \text{是}\ \textbf{有限见证} \Longrightarrow \forall n\,P_n\ \in\ \textbf{Π}_1\ \text{类}\ ✓$$
$$\textbf{为什么被吸收}：\text{V150 W2 ＋ E4 §2：}\textbf{RH 本身是 Π}_1（\text{经 Robin 定理）}\ \Longrightarrow\ \text{Π}_1\ \text{非平凡实例在算术中}\ \textbf{恰为已知 RH 等价判据}：$$
$$\qquad\text{(a) Mertens 型}\ \forall n\ \text{已被}\ \textbf{反证}（\text{Odlyzko--te Riele}）✗；\quad\text{(b) Robin 型}\ \forall n\ \text{与 RH 等价} \Longrightarrow \textbf{B1 违反}✗$$
$$\textbf{不可有限见证性}：\ \textbf{有}（Π_1\ \text{恰好是"无有限证书但有限可反驳"）—— \textbf{但这正是 RH 已知的形态}，\text{故不构成新机制}✓$$
$$\Longrightarrow\ \boxed{\mathrm{B\text{-}I}\ \text{坍缩}\to\text{Π}_1\ \text{＝已知 Robin 见证类}\ (\text{反证 或 RH 等价})}$$

### B-II 极限存在性：$\mathcal P(M)=\lim_n F_n(M)$ 存在
$$\textbf{自然来源}\ ✓\ \text{（部分 Euler 积的极限、归一化计数函数极限、原子测度极限）}$$
$$\textbf{为什么被吸收}：\text{自然极限对象恰是旧类的研究对象本身}：$$
$$\qquad\text{(a) 部分 Euler 积在边界}\ \to\ \textbf{值面／A-leak（V172 §5a）}✗；\quad\text{(b) 归一化零点测度}\ \to\ \textbf{pair correlation}（\text{第 3 行 finite correlation}）✗$$
$$\qquad\text{(c)}\ N(\sigma,T)/T\ \text{型密度极限}\ \to\ \textbf{值面／计数}（\text{V283 §1}）✗；\quad\text{(d) Mertens 型}\ \lim M(n)/\sqrt n\ \to\ \text{已反证}✗$$
$$\textbf{不可有限见证性}：\ \text{对 (a)–(c) 不适用（\text{极限对象本身即旧量}）}；\text{对 (d) 不成立（有限反例）}$$
$$\Longrightarrow\ \boxed{\mathrm{B\text{-}II}\ \text{坍缩}：\text{"极限存在"与"该量"} \text{在已审实例中}\ \textbf{无区别}}$$

### B-III 对象的不可分解性：$M\not\simeq M_1\oplus M_2$（primitive／indecomposable）
$$\textbf{自然来源}\ ✓\ \text{（整环的不可分解、motive 的单纯性、模范畴的 primitivity）}$$
$$\textbf{对本对象的决定性事实（V144）}：\zeta\ \text{的局部因子}\ \alpha_p\equiv1（\textbf{平凡 motive}）\ \Longrightarrow\ \text{ζ 的 motive 层}\ \textbf{无非平凡结构}；$$
$$\qquad\text{且 V144 进一步判定：}\textbf{零点／RH 不在 motive 层，而在 Archimedean 层} \Longrightarrow \text{在 motive 层问不可分解性}\ \textbf{问错了层}✗$$
$$\textbf{唐先生预警的风险}：\text{irreducible}\to\text{index/rank/dimension}\ \to\ \textbf{V211 指标类}✗$$
$$\Longrightarrow\ \boxed{\mathrm{B\text{-}III}\ \text{坍缩}：\text{对本对象}\ \textbf{层错配（V144）}；\text{一般情形}\ \to\ \textbf{V211 指标类}}$$

### B-IV 对象级极限缺陷：$\operatorname{Def}(M_\infty)=\mathcal P(\lim M_T)-\lim\mathcal P(M_T)\ne0$
$$\textbf{与 V321 的关系（本档辨析）}：\text{V321 关的是}\ \textbf{集合层} \text{的 lifting（}\pi_N(\varprojlim)=I_{\infty,N}）；$$
$$\qquad\text{B-IV 问的是}\ \textbf{不变量层} \text{的交换性（}\mathcal P\ \text{与}\ \lim\ \text{是否交换）}\ \text{—— }\textbf{确是不同的问题}\ ✓$$
$$\textbf{自然实例}：\text{(a) Iwasawa 型}\ \lambda\text{-不变量}：\lim\text{(Selmer 秩)}\ \text{vs}\ \text{rank(lim)}；\ \text{(b) 谱隙／正性型极限缺陷；}\ \text{(c) 密度型极限缺陷}$$
$$\textbf{为什么被吸收}：\text{(a) 是}\ \textbf{指标型}（\text{Iwasawa }\lambda\text{）}；\ \text{而 V211 §5 的排除表明确列出"}\textbf{非指标}\text{"} \Longrightarrow \textbf{指标型已属已分类}✗$$
$$\qquad\text{(b)}\ \to\ \textbf{POS 型}（\text{循环}）✗；\quad\text{(c)}\ \to\ \text{值面／计数}✗$$
$$\Longrightarrow\ \boxed{\mathrm{B\text{-}IV}\ \text{坍缩}：\text{自然实例全为指数型／密度型／正性型}}$$

## 3. 归约汇总
$$\begin{array}{c|c|c}
\text{类型} & \text{不可有限见证性} & \text{归约}\\ \hline
\mathrm{B\text{-}I}\ \text{无限一致性} & \text{有（Π}_1\text{）} & \text{Π}_1＝\text{已知 Robin 见证类（反证／RH 等价）}\\
\mathrm{B\text{-}II}\ \text{极限存在性} & \text{不适用} & \text{值面／correlation／计数（旧类）}\\
\mathrm{B\text{-}III}\ \text{不可分解性} & — & \text{层错配（V144）／V211 指标类}\\
\mathrm{B\text{-}IV}\ \text{对象级极限缺陷} & \text{部分} & \text{指数型（}\lambda\text{-不变量）／正性／密度}
\end{array}$$
$$\Longrightarrow\ \textbf{四类全数坍缩，无第五行实例}。$$

## 4. 硬判定树（唐先生原树，逐字保留）
$$\boxed{\mathcal P(M)}\ \downarrow$$
$$\begin{array}{ll}
\text{有限证书}&\to V271\\
\text{有限可计算标量}&\to V277\\
\text{count/support}&\to\text{旧类}\\
\text{correlation}&\to V294\\
\text{complexity}&\to V259\\
\text{index/rank/dimension}&\to V211\\
\text{explicit/Weil/zero criterion}&\to\text{旧墙}\\
\text{inverse-limit lifting}&\to V321\\
\boxed{\text{均非}}&\to\boxed{\text{真正 E3-B}}
\end{array}$$
$$\text{进入最后一格后才问：}\mathcal P(M)\Longrightarrow\text{新的 RH-relevant consequence?}$$

## 5. ⭐ 跨通道结构诊断（本档最大收获）
$$\text{三条 E3 自由度（放松**有限呈现**／**有限可计算**／**点态聚焦**）在}\ \textbf{各自已审实例中} \text{均坍缩回旧语言}：$$
$$\text{E3-A（动态深度）}\to\{\text{传播型},\ \text{复杂度型}\}；\quad\text{E3-C（关系不交换）}\to\{\text{coboundary},\ \text{A-leak},\ \mathrm{NC},\ \text{层错配}\}；$$
$$\qquad\text{E3-B（对象级性质）}\to\{\text{Π}_1\ \text{已知类},\ \text{值面},\ \text{correlation},\ \text{指标型},\ \text{层错配}\}$$
$$\Longrightarrow\ \boxed{\text{旧语言在三种放松方向下}\ \textbf{均具吸收性}}（\text{已审实例范围）}$$
$$\text{且坍缩的}\ \textbf{共同归宿} \text{收敛到同一小集合}：\textbf{计数／值面／correlation／指标型／层错配／复杂度}。$$

## 6. 判定（**不预判 DEAD**）
$$\textbf{第一轮结果}：\text{四类机制全数坍缩；第五行}\ \textbf{无实例}；$$
$$\text{但候选族为}\ \textbf{类型学枚举}，\ \textbf{未证完备}（N1/N2）\Longrightarrow \text{记作"未找到"，非"不存在"}；$$
$$\text{若须收口，所需＝}\textbf{E3-B 类型完备性定理}（\text{列尽"由对象自然结构生成的性质"，并证其必落已分类}）\ \text{—— 本档未给出}。$$

## 7. 边界（N1/N2 严守）
$$\text{① 本档}\ \textbf{不要求 RH 后果}（\text{唐先生指定），\text{也不预判 DEAD}；$$
$$\text{② B-I 的 Π}_1\ \text{判定（与 V150 W2／E4 §2 对接）为}\ \textbf{[结构判定]}；\ \text{B-III 的层错配（V144）与 B-IV 的指标型归约为}\ \textbf{[结构判定]}；$$
$$\text{③ V277／V271／V294／V259／V211／V144／V150／V172／V283／V287／V321 为档案既有结论，}\textbf{未逐行重验}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}。}$$

## 8. 净产出
$$\text{(i) E3-B 的四道门（B1 生成来源／B2 P-origin／B3 不可有限见证／B4 强现象）；}$$
$$\text{(ii) 四类机制审计：}\mathrm{B\text{-}I}\to\Pi_1\ \text{已知类}；\mathrm{B\text{-}II}\to\text{旧量本身}；\mathrm{B\text{-}III}\to\text{层错配／V211}；\mathrm{B\text{-}IV}\to\text{指标型}；$$
$$\text{(iii) 硬判定树落座（\text{八行归约}）；}$$
$$\text{(iv) ⭐ 跨通道诊断：}\textbf{旧语言在三种放松方向下均具吸收性，且归宿收敛到同一小集合}；$$
$$\text{(v) 未收口条件：所需＝E3-B 类型完备性定理（未给出）。}$$
