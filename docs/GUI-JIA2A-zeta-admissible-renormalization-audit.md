# 癸-甲2A — **ζ-admissible renormalization audit**（归一化不变量审计）

> 唐先生 2026-09-16 19:34 拍板：开癸-甲2A；**第一刀不是"换个归一化试试"**，而是
> $$\boxed{\text{证明哪些归一化是自由度，哪些被零检测强制固定}}$$
> 攻击对象（唐先生指定）：
> $$\boxed{\Gamma_w(\sigma)=\frac{\text{zero-detection threshold exponent}}{\text{intrinsic }L^2\ \text{scale exponent}}；\ \text{目标}\ \sup_{w\in\mathcal W_\zeta}\liminf_{\sigma\downarrow1/2}\Gamma_w(\sigma)>1\ ?}$$
> **禁令**：$\textbf{不得}$ 把"换归一化"理解成"给 $D$ 加权" ✓

---

## 1. 归一化不变量：整体缩放是**恒等变换**（必死）
$$D_w(t)=\sum_{N<n\le2N}a_nw_nn^{it},\qquad \mathcal V_2(w)：＝\Bigl(\sum_{N<n\le2N}|a_nw_n|^{2}\Bigr)^{1/2}$$
$$\text{若}\ w\mapsto cw：\ D_w\mapsto cD_w,\ \mathcal V_2\mapsto|c|\mathcal V_2,\ V_w\mapsto|c|V_w \Longrightarrow \boxed{\frac{V_w}{\mathcal V_2(w)}\ \textbf{完全不变}}$$
$$\Longrightarrow\ \textbf{整体 renormalization 必死}（\text{只改坐标，不改大值问题的实际难度}）✓$$

## 2. 二阶约束：阈值与尺度**必须一起动**（结构性）
$$\text{零检测}\ \Longrightarrow |D_w(\gamma)|\ge V_w\ \text{对}\ \beta\ge\sigma\ \text{的零点}\ \gamma$$
$$\textbf{关键}：\ D_w\ \textbf{不能任意选择} \text{——它必须由}\ \zeta\ \text{的零检测公式}\ \textbf{真实产生} \Longrightarrow \text{三角约束}$$
$$\qquad\boxed{\text{载体权重}\ +\ \text{零检测阈值}\ +\ \text{二阶典型尺度}}\ \text{三者中改一个，另两个}\ \textbf{通常一起变}✓$$
$$\text{例（本档结构分析）}：\ w_n=n^{-\epsilon}\Longrightarrow \mathcal V_2\asymp N^{1/2-\epsilon}；\ \text{而检测所用的}\ \zeta\ \text{恒等式也随}\ \epsilon\ \text{移动} \Longrightarrow \text{阈值同阶移动} \Longrightarrow \Gamma_w\ \textbf{不变}✓$$

## 3. ⭐ 核心识别（本档新信息）：$\Gamma_w$ **就是**已知的"mollifier 长度"参数
$$\text{零检测/密度路线的标准载体：}\textbf{mollifier 型权重}（\text{截断}\ \mu\text{、平滑权、Levinson--Conrey 型}）$$
$$\qquad\text{其关键参数＝}\textbf{mollifier 长度指数}\ \theta（\text{载体有效长度}）$$
$$\Gamma_w＝\frac{\text{阈值指数}}{\text{内在}\ L^2\ \text{尺度指数}} \equiv \text{“载体相对其自身尺度的}\ \textbf{有效放大}”＝\textbf{mollifier 强度}$$
$$\Longrightarrow\ \boxed{\Gamma_w\ \leftrightarrow\ \text{mollifier 长度参数}\ \theta}\quad(\textbf{[结构判定]}，\ \text{须核验：见 §6）}$$
$$\qquad\text{而}\ \text{该参数在文献中的已知天花板＝}\ \textbf{平方根型屏障}（\theta\ \text{不能越过}\ N^{1/2}\ \text{量级}）$$
$$\Longrightarrow\ \text{故}\ \Gamma_w\le1+o(1)\ \text{在}\ \sigma\to1/2\ \text{时}\ \textbf{与已知屏障同一位置}✓$$

## 4. ⭐⭐ 与 V316 的连接（本档最重要的结构后果）
$$\text{V316 的变分载体参数}\ \lambda＝\frac{\text{载体有效带宽}}{\text{基准}} \Longrightarrow \text{同样刻画"载体相对自身尺度的有效放大"}$$
$$\Longrightarrow\ \boxed{\Gamma_w\ \leftrightarrow\ \lambda}\quad(\textbf{[结构判定]}，\ \text{本档不宣告已证})$$
$$\qquad\text{若成立}：\ \text{则甲方向的"权重自由度"}\ \textbf{不是新自由度}，\ \text{而是}\ \textbf{已被审计的}\ \lambda；$$
$$\qquad\qquad\text{且天花板}\ \Gamma\le1\ \leftrightarrow\ \lambda\le1 \Longrightarrow \textbf{两语言中的墙}\ \textbf{同一}✓$$
$$\qquad\text{这}\ \textbf{部分填补} \text{了 E6 未建立的"两坐标映射"（E6-REVIEW §2(a) 的工作假设）——}\ \textbf{但仅为结构判定}✓$$

## 5. 判定：$\mathbf{WALL}$（并给出墙的身份）
$$\text{按唐先生三档}：$$
$$\qquad\text{ALIVE}：\ \text{未得}（\text{未找到}\ \liminf\Gamma_w>1\ \text{的合法}\ w）$$
$$\qquad\boxed{\mathbf{WALL}}：\ \textbf{所有自然／已知权重族都回到}\ \Gamma_w\to1 \Longrightarrow \text{无指数错位}；\ \textbf{但未证} \text{这是所有合法载体的必然结果}$$
$$\qquad\text{DEAD}：\ \text{未达}（\text{未对全}\ \mathcal W_\zeta\ \text{推出}\ \Gamma_w\le1+o(1)）$$
$$\textbf{本档的正面内容（比"没找到"强）}：\ \text{墙被}\ \textbf{识别} \text{为}\ \textbf{mollifier 长度屏障}（\text{且}\ \textbf{候选同一于}\ V316\ \text{的}\ \lambda）⟹ \text{不是新障碍，而是}\ \textbf{同一障碍的又一次出现}✓$$

## 6. 可证伪的核验项（把 [结构判定] 变成可检验）
$$\text{(V1)}\ \text{文献中 mollifier 长度参数}\ \theta\ \text{的天花板}\ \textbf{是否} \text{恰对应}\ \Gamma\le1\（\text{可由 Levinson／Conrey／AF 型的载体族逐一核验）}$$
$$\text{(V2)}\ \text{V316 的}\ \lambda\ \text{与密度/mollifier 路线的}\ \theta\ \text{是否存在}\ \textbf{显式映射} \（\text{即 E6 未建的桥}）$$
$$\text{(V3)}\ \text{是否存在}\ w\in\mathcal W_\zeta\ \text{使}\ \delta(\sigma)-\epsilon(\sigma)>0\ \textbf{在}\ \sigma\to1/2\ \text{仍有固定正余量}（\text{ALIVE 的唯一判据}）$$
$$\Longrightarrow\ \text{若 (V1)(V2) 皆成立} \Longrightarrow \text{甲方向与 V316 的墙}\ \textbf{同一} \Longrightarrow \text{甲方向}\ \textbf{在机制层封闭}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① §3／§4 的"}\Gamma_w\leftrightarrow\theta\leftrightarrow\lambda\text{"为}\ \textbf{[结构判定]}，\ \textbf{未证}；\quad\text{② §2 的"阈值与尺度同阶移动"为}\ \textbf{结构性分析}（\text{未逐式核验文献）}；$$
$$\text{③ }\textbf{未} \text{对全}\ \mathcal W_\zeta\ \text{推出}\ \Gamma\le1（\textbf{不宣告 DEAD}）；\quad\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}✓$$

## 8. 净产出
$$\text{(i) 归一化不变量：整体缩放恒等 ⟹ renormalization 必死；不变量＝}\ \Gamma_w=V_w/\mathcal V_2(w)；$$
$$\text{(ii) 二阶约束：阈值／误差／尺度}\ \textbf{三者链动} \Longrightarrow \text{权重不是自由参数}；$$
$$\text{(iii) ⭐ 核心识别：}\Gamma_w\ \leftrightarrow\ \textbf{mollifier 长度参数}\ \theta\（\text{已知天花板＝平方根型屏障}）；$$
$$\text{(iv) ⭐⭐ 结构后果：}\Gamma_w\ \textbf{候选同一} \text{于 V316 的}\ \lambda \Longrightarrow \text{甲方向的"最后自由度"}\ \textbf{不是新的}；$$
$$\text{(v) 判定}\ \mathbf{WALL}（\text{墙被识别，非 DEAD）＋三项可证伪核验 V1--V3}。$$
