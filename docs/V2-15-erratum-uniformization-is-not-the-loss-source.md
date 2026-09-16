# V2-15 — **修正（勘误 T10）：uniformization 不是 17/33 的损失源**

> 唐先生 2026-09-16 21:15 拍板：**V2-15 要修正而不是重做**✓
> 依据＝V2-14 的原文取证（BCR §3.4 逐字）✓

---

## 1. 必须修正的旧表述
$$\text{旧（Q1b／Q2-A／Q2-B／V1-1 沿线）：}\ \text{"uniformization 可能造成 worst-case loss"} \Longrightarrow \boxed{\textbf{降级}}✓$$
$$\text{新表述}：\ \boxed{\text{在已核查的 BCR §3.4 架构中，}\textbf{没有证据表明 uniformization 是损失来源}；\ (1.3)\ \text{是}\ \textbf{逐配置调用} \text{的}}✓✓$$
$$\qquad\text{依据（V2-14 逐字）}：\text{"we use (1.3) instead of Proposition 1 in (3.7)"}＋\text{"Notice that (1.3) is applicable, since}\dots\text{"} \Longrightarrow \text{估算在 dyadic 求和}\ \textbf{内部逐次调用}✓$$

## 2. 必须保留的部分
$$\boxed{\text{single}\ (r,t)\ \text{是 BCR Theorem 2 的}\ \textbf{输入坐标}}✓\quad(\text{此点不变})$$
$$\qquad\textbf{但}：\ \textbf{不得} \text{再把它解释为"}\textbf{造成}\ 17/33\ \text{的压缩损失"}✓✓$$

## 3. Q1b／Q2-A 的计算如何处置
$$\text{Q2-A／Q2-A2／Q1b-1 的}\ \textbf{配置最大点计算} \text{（角点}\ (\theta_{\max},d=1)\text{、支配性与紧性重合、区域依赖不改善指数）：}$$
$$\qquad\text{若仅作为}\ \textbf{分析重构模型本身} \text{的结论} \Longrightarrow \textbf{保留}✓$$
$$\qquad\textbf{但不能再作为"17/33 的损失机制"}✓✓\quad(\text{它们描述的是}\ \textbf{该模型内} \text{的几何，而非}\ 17/33\ \text{的成因})✓$$

## 4. 由此得到的新逻辑位置
$$\boxed{17/33\ \text{的直接来源＝BC 第一项的指数}\ (\tfrac7{20},\tfrac14)}✓✓\quad(\text{V2-14 §3 复算：(33/20)}\log_T N\le17/20\iff\log_T N\le17/33)✓$$
$$\qquad\Longrightarrow\ \text{主线问题转换为}：\ \boxed{\text{"BC 第一项为什么只能给出}\ (r,t)=(\tfrac9{20},\tfrac7{20})\text{"}}✓✓$$

## 5. 边界
$$\text{① 本档为}\ \textbf{勘误} \text{（不改写旧档正文）；}\quad\text{② 取证＝BCR §3.4 逐字（外部来源）}✓；\quad\text{③ }\textbf{未用 RH}；\ \text{零数值}✓$$
