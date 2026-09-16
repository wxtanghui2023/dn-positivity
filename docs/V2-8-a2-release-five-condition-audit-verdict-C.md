# V2-8 — **$a_2$ 释放的五条件审计** ⟹ 判定 **C**

> 唐先生 2026-09-16 20:44 拍板：做 **V2-8**，把 $a_2$ 打到底（五条件逐项判死/判活）。
> 判据：$$\boxed{\text{A}：a_2\ \text{可释放且整体指数下降}\ \big|\ \text{B}：\text{释放必触发容量墙}\ \big|\ \text{C}：\text{现有 §4.1.3--§4.4}\ \textbf{不足以判定}}$$
> **陷阱警示（唐先生）**：即使 $a_2$ 能留在 diagonal，也 $\textbf{不能}$ 直接宣布 ALIVE；必须完成第五项整体 envelope 重优化 ✓

---

## 1. 取证（PDF 文本抽取，**外部来源，仅作数据**）
$$\textbf{§4.1.2 关键句（逐字）}：\ \text{"Next, we apply the Cauchy--Schwarz inequality}\ \textbf{with respect to the sums over}\ p_1,p_2,q_1,q_2,n'_1,n'_2,c,\mathbf{a_2}\text{."}\ ✓✓$$
$$\Longrightarrow\ \boxed{a_2\ \textbf{确在平方组} \text{（本节原文明确列出）}}✓\ \text{与 §2 摘要"not to the sums over}\ d,a_1,\ell_1,\ell_2\text{"}\ \textbf{一致}✓✓$$
$$\Longrightarrow\ \textbf{不对称性确认}：\ \mathbf{a_1\ \text{未平方}}\ \big|\ \mathbf{a_2\ \text{平方}}✓✓$$
$$\textbf{其余取证（(4.11)--(4.13)）}：\ T_{b,\eta}\ \text{定义为}\ p_1,p_2,q_1,q_2\ (\asymp L,\ p_1\ne q_1,\ p_2\ne q_2),\ n'_1,n'_2\ (\asymp N),\ 0\ne|d|,|d'|\le D=q_1p_2,\ c\ ((\mathrm{mod}\ bq_1p_2)),\ a_1,a'_1,a_2\ (\asymp A)\ \text{上的多重和}✓$$
$$\qquad\text{相位 (4.12) 含}\ \delta\ \text{型因子}：\ a_2(d\ell'_1-d'\ell_1)\ \text{（}\textbf{a}_2\ \text{以}\ \textbf{线性因子} \text{出现}）✓$$
$$\qquad T_{b,\eta}=U_{b,\eta}+U'_{b,\eta}，\ U＝(\ell_1\ell'_1,\ell_2\ell'_2)=1\ \text{的部分}；\ \text{§4.1.3 界}\ U，\ \text{§4.1.4 处理}\ U'✓$$

## 2. ⚠️ 取证障碍（本档诚实标注）
$$\textbf{PDF 数学式抽取有噪声}：\ (4.10)--(4.13)\ \text{的多重和上下标在抽取中}\ \textbf{大量错位} \Longrightarrow \textbf{无法可靠重建} \text{哪些变量最终留在}\ T\ \text{内、哪些被平方消去}✓$$
$$\qquad\text{具体冲突}：\ \text{句子列}\ a_2\ \text{入 C--S；但}\ (4.11)\ \text{的显示中出现}\ (a_1,a'_1)\ \text{成对与}\ a_2\ \text{单个} \Longrightarrow \text{与"}\ a_1\ \text{未平方"的摘要}\ \textbf{表面上不一致}✓$$
$$\qquad\Longrightarrow\ \textbf{须换更清晰的取源}（\text{arXiv HTML 版公式渲染更可读；或}\ \texttt{pdftotext -layout}）\ \text{方可定论}✓$$

## 3. 五条件逐项（**本档可判定度**）
$$\begin{array}{c|c|c}
\text{条件} & \text{所需证据} & \text{本档}\\
\hline
\text{(1) C--S 后可控性} & \text{释放}\ a_2\ \text{后的范数／对角和} & \textbf{无法判定}\\
\text{(2) diagonal 可解性} & \ell_1n_1=\ell_2n_2\ \text{加入}\ a_2\ \text{后能否参数化} & \textbf{无法判定}\\
\text{(3) Kloosterman／Weil 平均估计} & \text{是否仍落在可处理对象} & \textbf{无法判定}\\
\text{(4) off-diagonal 代价} & \text{增加的非对角是否超过 gain} & \textbf{无法判定}\\
\text{(5) 整体指数} & \inf_L E_{\rm new}(L)<\inf_L E_{\rm BC}(L)\ ? & \textbf{无法判定}
\end{array}$$
$$\Longrightarrow\ \text{五项皆}\ \textbf{无法判定} \Longrightarrow \text{按唐先生判据落}\ \boxed{\textbf{C}}✓$$

## 4. 判定：**C（现有 §4.1.3--§4.4 不足以判定）**
$$\boxed{\text{C}}：\ \text{本档}\ \textbf{不落 A／B} \Longrightarrow \text{容量}\ \textbf{OPEN} \text{保持}✓$$
$$\textbf{理由}：\ \text{决定性问题（}\textbf{BC 为何把}\ a_2\ \text{放入平方组}）\ \textbf{原文未明确陈述} \text{，}\ \text{而}\ (4.10)--(4.13)\ \text{的抽取噪声使其无法反推}✓$$
$$\qquad\Longrightarrow\ \text{这}\ \textbf{不是} \text{"容量为有限"的证据，}\ \textbf{也非} \text{"容量开放"的证据}✓$$

## 5. 本档的净收获（可传下去的三条硬信息）
$$\text{(i) }\ a_2\ \textbf{确在平方组}（\text{§4.1.2 原文明确列出}）⟹ \textbf{不对称性确认}：a_1\ \text{外／}a_2\ \text{内}✓✓$$
$$\text{(ii) }\ \text{相位 (4.12) 中}\ a_2\ \text{以}\ \textbf{线性因子} \text{出现（与}\ d,\ell',\ell\ \text{构成}\ \delta\ \text{型组合）}⟹ \text{若释放}\ a_2，}\ \textbf{该线性因子应仍在} \text{，故其"可控性"取决于 }a_2\ \text{在后续步骤中是否被用于消去变量}✓$$
$$\text{(iii) }\ \text{§4 的后续结构已定位}：\ \text{§4.1.3 界}\ U\ (\text{互素情形})；\ \text{§4.1.4 处理}\ U'；\ \text{§4.2 处理}\ (n'_1,n'_2)\ne1\ ⟹ \textbf{读证范围进一步缩小}✓$$

## 6. 残余（不得省略）
$$\text{残余 1：决定性数据（BC 把}\ a_2\ \text{放入平方组的}\ \textbf{理由}）\ \textbf{未取得}；\ \text{须以更清晰取源重读 §4.1.2--§4.1.3}✓$$
$$\text{残余 2：}D_b\ \text{六项中另四项仍未逐项溯源（承 V2-6b／V2-7）}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 不扩展问题（只打}\ a_2\text{）；}\ \text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 8. 净产出
$$\text{(i) 逐字取证：}\ a_2\ \textbf{确在 §4.1.2 的 C--S 平方组} \Longrightarrow \textbf{不对称性确认（}a_1\ \text{外／}a_2\ \text{内）}✓✓$$
$$\text{(ii) 取证障碍登记：PDF 数学抽取噪声 ⟹ 五条件皆无法判定；冲突点已具名}✓$$
$$\text{(iii) 判定}\ \boxed{\textbf{C}}（\text{现有 §4.1.3--§4.4 不足以判定}）\ \text{—— 既非 A 亦非 B}✓$$
$$\text{(iv) 三条可传硬信息（(i)(ii)(iii)）＋读证范围进一步缩小}✓$$
$$\text{(v) 下一步唯一动作：换更清晰取源（arXiv HTML／}\texttt{pdftotext -layout}\text{）重读 §4.1.2--§4.1.3，取得"为何平方}\ a_2\text{"的决定性依据}✓$$
