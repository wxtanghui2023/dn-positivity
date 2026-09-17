# 🔧 **勘误＋收紧**：光滑性**已分析过**（`E68`／`PAPERA-expsum`，2026-09-13）—— 且**光滑部分已被解决**

> 依唐先生 15:27「先搜索，我记得光滑性已经分析过」✓ **命中，且比预想更彻底** ✓✓
> **本档结果**：① 撤回 `5b9fd91` §5 候选 (A) 的"未开发"表述；② 光滑部分＝**已解决**；③ 揭示**第四条独立路径**收敛到同一瓶颈 ✓✓✓

---

## §1 `E68` 逐字（`docs/E68-average-vs-pointwise.md`）
$$\text{分解}：S_n=S_n^{\rm smooth}+D_n✓$$
$$\textbf{【光滑部分 ✓ 有抵消 ✓】}\ \theta\ \text{关于}\ \gamma\ \textbf{单调} \Longrightarrow \text{驻相／vdC 可用} \Longrightarrow \boxed{\textbf{已解决}}\（\text{我方：}|S^{\rm smooth}|\le\boxed{1704}）✓✓$$
$$\textbf{【偏差}\ D_n\ ✗\ \text{无手段}✗\textbf{】}\ D_n=\text{零点计数偏差（实际位置}\ -\ \text{光滑密度）的}\ \textbf{振荡变换}✓$$
$$\qquad \Longrightarrow \text{它是}\ \textbf{奇异测度}✗：\textbf{无受控二阶导数} \Longrightarrow \textbf{vdC 无从下手}✗\quad(\text{vdC 需}\ |\varphi''|\ge\lambda)✓✓$$
$$\text{⭐ 一句话逐字}：\boxed{\text{"障碍不在'抵消的量'，而在'输入的类型'：}\textbf{平均可得}✓／\textbf{逐点不可得}✗"}}✓✓✓$$

## §2 `PAPERA-expsum` (甲-1) 逐字：光滑部分**可证**
$$\varphi'(k)=-\frac{2\pi n}{\gamma\,2\log(\gamma/2\pi)},\quad \varphi''(k)=\frac{2\pi}{\gamma\log\gamma}\Big(2-\frac1{\log}\Big)\frac{2\pi}{\log}✓$$
$$\text{共振点}\ \gamma_{\rm res}=8.2683\times10^5,\ M_B=581491\ (29.1\%),\ \varphi''=6.58\times10^{-7}\Longrightarrow \boxed{|S^{\rm smooth}|\le471.7+1232.7=1704\ll6.55\times10^5}✓✓$$
$$\boxed{\text{"光滑(平均密度)模型已经把}\ \sqrt N\ \text{相消证出来了"}✓✓\qquad(\text{实测}\ |S_n^{\rm smooth}|=1.14e6/2373/1531/832，\text{与}\ |S_n|\ \text{同量级})✓$$
$$\textbf{(甲-2)}\ \text{唯一缺口＝刚性误差}\ D_n，\text{其显式恒等式（当时新导出）}：D_n\approx\sum_k(e^{i\lambda_kS_k}-1)e^{i\varphi_k},\ \lambda_k:=\frac{2\pi n}{\gamma_k2\log(\gamma_k/2\pi)},\ S_k:=k-\bar N(\gamma_k)✓✓$$

## §3 🔧 勘误（针对 `5b9fd91`）
$$\text{我在}\ §5\ \text{写：候选 (A) 导数／光滑性结构"}\textbf{未核}／\textbf{未开发}" \Longrightarrow \boxed{\textbf{错}✗（\text{已覆盖，且更彻底}）}$$
$$\text{正确状态（行⑤重填）}：\boxed{\text{光滑部分}\ \textbf{已解决}（\text{解析含常数＋数值双证）}；\ \textbf{墙在偏差}\ D_n}✓✓$$
$$\Longrightarrow \text{我}\ §4\ \text{表中行⑤的}\ "？"\ \text{应改为}\ "\boxed{\text{已解决（光滑）／墙在偏差}}"✓$$

## §4 ⭐⭐ 深一层：`E68` 的真障碍＝**输入类型**（与今日他路同址）
$$\text{我方无条件输入}\ \textbf{全是平均型}：\text{Montgomery 对相关（对高度平均）}／\text{大筛法（对频率平均）}／\text{零密度}／\text{E55 块二阶矩}✓$$
$$\text{而需求是}\ \textbf{逐点型}（\max_n） \Longrightarrow \boxed{L^2\to L^0\ \text{代价}=\sqrt N\approx1414\ \text{倍}=\textbf{缺口本身}}✓✓✓$$
$$\qquad ⚠️\ \text{唯一升级工具＝更高阶矩；而}\ \textbf{四阶矩需逐点对相关} \Longrightarrow \textbf{循环}✓✓$$
$$\qquad ⚠️\ \text{压缩效应}：n\approx T_0^2\ \text{处}\ n(\theta_\gamma-\theta_{\gamma'})\approx-\Delta\gamma \Longrightarrow \text{相位差}\approx\text{纵坐标差} \Longrightarrow \textbf{对}\ n\ \text{几乎不变}⟹\text{non-diagonal 不被平均掉}✓✓$$
$$\text{所需}：\ \textbf{一条逐点刚性输入}：S(T)=o(\log T)（\text{Titchmarsh }\S9.11，\text{无已知改进}）\ \text{或}\ \textbf{单位频率间隙统计}✓\qquad(\text{皆经典开放})✓$$

## §5 ⭐⭐⭐ 第三条独立路径收敛（加强唐先生的"同一瓶颈"判读）
$$\text{(i)}\ \text{ATD 型}：\text{局部／有限算术} \to \text{全局谱定位}\ \text{缺机制}\quad(\texttt{V211}\S5)✓$$
$$\text{(ii)}\ \text{parity／interface}：\text{素数提取需要}\ \textbf{局部有限型结构} \text{而素数没有}\quad(\text{本档前序})✓$$
$$\text{(iii)}\ \text{E68}：\textbf{平均型输入}\ vs\ \textbf{逐点型需求}，\text{代价}\ \sqrt N✓✓$$
$$\Longrightarrow \boxed{\text{三条路径}\ \textbf{各自独立} \text{出发，}\ \textbf{收敛到同一瓶颈}}✓✓✓\qquad(\text{}\textbf{机制级承重墙}\text{的}\ \textbf{第三条}\ \text{投影证据})✓$$

## §6 由此新任务的定义再收紧
$$\text{不是}：\text{"找光滑性新招"（\text{已做，且光滑部分已解}）}✗$$
$$\text{而是}：\boxed{\textbf{攻}\ D_n\ \text{的逐点刚性}\ \text{—— 或 }\S4\ \text{表中的 (C) Type II／level 1/2，或 (B) 部分提取}}✓✓$$
$$\text{判据不变（五条）}；\ \text{且新增一条}\ \textbf{否定判据}：\text{若方案需要"平均型→逐点型"的转换而不给新输入} \Longrightarrow \textbf{必付}\ \sqrt N⟹\text{即死}✓✓$$

## §7 边界
$$\text{(i)}\ §1--§2\ \textbf{全部逐字}（\texttt{E68}／\texttt{PAPERA-expsum}）✓✓\quad\text{(ii)}\ §4\ \text{为}\ \texttt{E68}\ \text{自身的结论}✓\quad\text{(iii)}\ §5\ \text{的"同址"为}\ [\textbf{结构}] \text{级判断}✓$$
$$\text{(iv)}\ \textbf{未用 RH}；\ \textbf{零数值}；\ \text{本档}\ \textbf{不新开方向}，\ \text{只做勘误＋收敛记录}✓✓$$
